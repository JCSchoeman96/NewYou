defmodule NewYou.Identity do
  use Ash.Domain, otp_app: :new_you

  require Ash.Query

  alias NewYou.Identity.{
    Account,
    Email,
    PMR,
    RegistrationBinding,
    RegistrationOperation,
    RegistrationResult,
    Token
  }

  @operation_lifetime_seconds 24 * 60 * 60
  @registration_operation_expiry_batch_size 100
  @verification_token_lifetime {24, :hours}
  @verifier_provider "AshAuthentication.Argon2Provider"
  @verifier_version "argon2_elixir-4.1.3"
  @development_terms_id "NEWYOU-TERMS-EN-DEV-2026-10-27-001"
  @development_privacy_id "NEWYOU-PRIVACY-EN-DEV-2026-10-27-001"

  resources do
    resource Account
    resource Token
    resource RegistrationOperation
  end

  @doc "Accept a valid registration into Identity and return a neutral pending result."
  @spec register(map()) :: {:ok, RegistrationResult.t()} | {:error, atom()}
  def register(request) when is_map(request) do
    with {:ok, operation_id} <- operation_id(request),
         {:ok, existing} <- read_operation(operation_id) do
      case existing do
        nil -> register_new(request, operation_id)
        operation -> replay_or_reject(operation, request)
      end
    else
      _ -> {:error, :invalid_registration}
    end
  end

  def register(_), do: {:error, :invalid_registration}

  @doc "Tombstone live registration bindings linked to an Account after an Identity invalidation."
  @spec invalidate_registration_operations(String.t()) :: :ok | {:error, atom()}
  def invalidate_registration_operations(account_id) when is_binary(account_id) do
    with {:ok, account_id} <- Ecto.UUID.cast(account_id),
         query <- Ash.Query.filter(RegistrationOperation, created_account_id == ^account_id),
         {:ok, operations} <- Ash.read(query, domain: __MODULE__, authorize?: false),
         {:ok, :ok} <-
           Ash.transaction([RegistrationOperation], fn ->
             tombstone_operations(operations)
           end) do
      :ok
    else
      _ -> {:error, :registration_unavailable}
    end
  end

  def invalidate_registration_operations(_), do: {:error, :registration_unavailable}

  @doc "Tombstone expired registration bindings in bounded Identity-owned batches."
  @spec expire_registration_operations() :: {:ok, non_neg_integer()} | {:error, atom()}
  def expire_registration_operations do
    now = now()

    query =
      Ash.Query.filter(
        RegistrationOperation,
        state == :bound and expires_at <= ^now
      )
      |> Ash.Query.sort(expires_at: :asc)
      |> Ash.Query.limit(@registration_operation_expiry_batch_size)

    with {:ok, operations} <- Ash.read(query, domain: __MODULE__, authorize?: false),
         {:ok, count} <- tombstone_expired_operations(operations) do
      {:ok, count}
    else
      _ -> {:error, :registration_unavailable}
    end
  rescue
    _ -> {:error, :registration_unavailable}
  catch
    _, _ -> {:error, :registration_unavailable}
  end

  defp tombstone_operations(operations) do
    Enum.reduce_while(operations, :ok, fn operation, :ok ->
      case tombstone_if_bound(operation) do
        :ok -> {:cont, :ok}
        {:error, _} = error -> {:halt, error}
      end
    end)
  end

  defp tombstone_expired_operations([]), do: {:ok, 0}

  defp tombstone_expired_operations(operations) do
    case Ash.transaction([RegistrationOperation], fn -> tombstone_expired_batch(operations) end) do
      {:ok, count} when is_integer(count) -> {:ok, count}
      _ -> {:error, :registration_unavailable}
    end
  end

  defp tombstone_expired_batch(operations) do
    case tombstone_operations(operations) do
      :ok -> length(operations)
      {:error, _} = error -> error
    end
  end

  defp register_new(request, operation_id) do
    with {:ok, input} <- validate_request(request, operation_id),
         {:ok, fingerprint, key_version} <- RegistrationBinding.fingerprint(input) do
      allocate_account(input, fingerprint, key_version, 1)
    else
      _ -> {:error, :invalid_registration}
    end
  end

  defp replay_or_reject(operation, request) do
    now = now()

    cond do
      operation.state == :tombstoned ->
        {:error, :registration_unavailable}

      is_nil(operation.expires_at) or DateTime.compare(now, operation.expires_at) != :lt ->
        _ = tombstone(operation)
        {:error, :registration_unavailable}

      operation.state != :bound ->
        {:error, :registration_unavailable}

      true ->
        with {:ok, input} <- validate_request(request, operation.operation_id),
             {:ok, fingerprint} <-
               RegistrationBinding.fingerprint_for_version(
                 input,
                 operation.fingerprint_key_version
               ),
             true <- RegistrationBinding.equal?(operation.request_fingerprint, fingerprint),
             true <- password_matches?(operation, input.password) do
          {:ok,
           %RegistrationResult{
             status: operation.outcome,
             account_id: operation.created_account_id,
             verification_proof: nil
           }}
        else
          _ -> {:error, :registration_unavailable}
        end
    end
  end

  defp allocate_account(input, fingerprint, key_version, attempt) do
    case next_pmr() do
      {:ok, pmr} -> create_registration_with_pmr(input, fingerprint, key_version, pmr, attempt)
      _ -> {:error, :registration_unavailable}
    end
  end

  defp create_registration_with_pmr(input, fingerprint, key_version, pmr, attempt) do
    result =
      Ash.transaction([Account, Token, RegistrationOperation], fn ->
        with {:ok, account} <- create_account(input, pmr),
             {:ok, verification_proof} <- issue_verification_proof(account),
             committed_at <- now(),
             {:ok, _operation} <-
               create_operation(%{
                 operation_id: input.operation_id,
                 request_fingerprint: fingerprint,
                 fingerprint_key_version: key_version,
                 password_verifier: account.hashed_password,
                 verifier_provider: @verifier_provider,
                 verifier_version: @verifier_version,
                 outcome: :verification_pending,
                 committed_at: committed_at,
                 expires_at: DateTime.add(committed_at, @operation_lifetime_seconds, :second),
                 created_account_id: account.id
               }) do
          %RegistrationResult{
            status: :verification_pending,
            account_id: account.id,
            verification_proof: verification_proof
          }
        end
      end)

    case result do
      {:ok, %RegistrationResult{} = accepted} ->
        {:ok, accepted}

      {:error, error} ->
        route_allocation_error(error, input, fingerprint, key_version, attempt)

      _ ->
        {:error, :registration_unavailable}
    end
  end

  defp route_allocation_error(error, input, fingerprint, key_version, attempt) do
    cond do
      attempt < 5 and error_has_unique_field?(error, :pmr) ->
        allocate_account(input, fingerprint, key_version, attempt + 1)

      error_has_unique_field?(error, :email) ->
        bind_duplicate_email(input, fingerprint, key_version)

      operation_id_collision?(error) ->
        replay_after_race(input)

      true ->
        {:error, :registration_unavailable}
    end
  end

  defp bind_duplicate_email(input, fingerprint, key_version) do
    case hash_password(input.password) do
      {:ok, password_verifier} ->
        store_duplicate_email_operation(input, fingerprint, key_version, password_verifier)

      _ ->
        {:error, :registration_unavailable}
    end
  end

  defp store_duplicate_email_operation(input, fingerprint, key_version, password_verifier) do
    operation_result =
      Ash.transaction([RegistrationOperation], fn ->
        committed_at = now()

        persist_duplicate_email_operation(
          input,
          fingerprint,
          key_version,
          password_verifier,
          committed_at
        )
      end)

    case operation_result do
      {:ok, %RegistrationResult{} = accepted} ->
        {:ok, accepted}

      {:error, error} ->
        if operation_id_collision?(error),
          do: replay_after_race(input),
          else: {:error, :registration_unavailable}

      _ ->
        {:error, :registration_unavailable}
    end
  end

  defp persist_duplicate_email_operation(
         input,
         fingerprint,
         key_version,
         password_verifier,
         committed_at
       ) do
    attributes = %{
      operation_id: input.operation_id,
      request_fingerprint: fingerprint,
      fingerprint_key_version: key_version,
      password_verifier: password_verifier,
      verifier_provider: @verifier_provider,
      verifier_version: @verifier_version,
      outcome: :verification_pending,
      committed_at: committed_at,
      expires_at: DateTime.add(committed_at, @operation_lifetime_seconds, :second),
      created_account_id: nil
    }

    case create_operation(attributes) do
      {:ok, _operation} -> %RegistrationResult{status: :verification_pending, account_id: nil}
      {:error, error} -> {:error, error}
    end
  end

  defp replay_after_race(input) do
    case read_operation(input.operation_id) do
      {:ok, %RegistrationOperation{} = operation} -> replay_or_reject(operation, input)
      _ -> {:error, :registration_unavailable}
    end
  end

  defp create_account(input, pmr) do
    attributes = %{
      first_name: input.first_name,
      surname: input.surname,
      email: input.email,
      preferred_language: input.preferred_language,
      confirmed_age_18?: true,
      terms_version_id: input.terms_version_id,
      privacy_version_id: input.privacy_version_id,
      legal_accepted_at: now(),
      acceptance_locale: input.acceptance_locale,
      pmr: pmr,
      password: input.password
    }

    Ash.create(Account, attributes,
      action: :register,
      domain: __MODULE__,
      authorize?: false
    )
  end

  defp create_operation(attributes) do
    Ash.create(RegistrationOperation, attributes,
      action: :bind,
      domain: __MODULE__,
      authorize?: false
    )
  end

  defp issue_verification_proof(account) do
    case AshAuthentication.Jwt.token_for_user(
           account,
           %{"purpose" => "email_verification"},
           purpose: :email_verification,
           token_lifetime: @verification_token_lifetime,
           domain: __MODULE__,
           authorize?: false
         ) do
      {:ok, token, _claims} -> {:ok, token}
      _ -> {:error, :token_creation_failed}
    end
  rescue
    _ -> {:error, :token_creation_failed}
  end

  defp read_operation(operation_id) do
    query = Ash.Query.filter(RegistrationOperation, operation_id == ^operation_id)

    case Ash.read(query, domain: __MODULE__, authorize?: false) do
      {:ok, [operation]} -> {:ok, operation}
      {:ok, []} -> {:ok, nil}
      {:ok, _} -> {:error, :registration_unavailable}
      {:error, _} -> {:error, :registration_unavailable}
    end
  end

  defp tombstone_if_bound(%RegistrationOperation{state: :bound} = operation),
    do: tombstone(operation)

  defp tombstone_if_bound(%RegistrationOperation{}), do: :ok

  defp tombstone(operation) do
    case Ash.update(operation, %{},
           action: :tombstone,
           domain: __MODULE__,
           authorize?: false
         ) do
      {:ok, _operation} -> :ok
      {:error, _} -> {:error, :registration_unavailable}
    end
  end

  defp validate_request(request, operation_id) do
    with {:ok, first_name} <- nonblank_text(Map.get(request, :first_name)),
         {:ok, surname} <- nonblank_text(Map.get(request, :surname)),
         {:ok, email_input} <- required_text(Map.get(request, :email)),
         {:ok, email} <- Email.canonicalize(email_input),
         {:ok, password} <- required_password(Map.get(request, :password)),
         {:ok, preferred_language} <- language(Map.get(request, :preferred_language)),
         true <- Map.get(request, :confirmed_age_18?) == true,
         {:ok, terms_version_id, privacy_version_id} <- legal_versions(request) do
      {:ok,
       %{
         operation_id: operation_id,
         first_name: first_name,
         surname: surname,
         email: email,
         password: password,
         preferred_language: preferred_language,
         acceptance_locale: preferred_language,
         confirmed_age_18?: true,
         terms_version_id: terms_version_id,
         privacy_version_id: privacy_version_id
       }}
    else
      _ -> {:error, :invalid_registration}
    end
  end

  defp operation_id(request) do
    with {:ok, operation_id} when is_binary(operation_id) <-
           Ecto.UUID.cast(Map.get(request, :operation_id)),
         {:ok, <<_timestamp::48, 4::4, _random_a::12, 2::2, _random_b::62>>} <-
           Ecto.UUID.dump(operation_id) do
      {:ok, operation_id}
    else
      _ -> {:error, :invalid_registration}
    end
  end

  defp nonblank_text(value) do
    with {:ok, value} <- required_text(value),
         true <- String.trim(value) != "" do
      {:ok, value}
    else
      _ -> {:error, :invalid_registration}
    end
  end

  defp required_text(value) when is_binary(value) and byte_size(value) > 0,
    do: {:ok, value}

  defp required_text(_), do: {:error, :invalid_registration}

  defp required_password(value) when is_binary(value) and byte_size(value) > 0,
    do: {:ok, value}

  defp required_password(_), do: {:error, :invalid_registration}

  defp language(:af), do: {:ok, :af}
  defp language(:en), do: {:ok, :en}
  defp language("af"), do: {:ok, :af}
  defp language("en"), do: {:ok, :en}
  defp language(_), do: {:error, :invalid_registration}

  defp legal_versions(request) do
    terms = Map.get(request, :terms_version_id)
    privacy = Map.get(request, :privacy_version_id)

    if allowed_development_legal_versions?() and terms == @development_terms_id and
         privacy == @development_privacy_id do
      {:ok, terms, privacy}
    else
      {:error, :invalid_registration}
    end
  end

  defp allowed_development_legal_versions? do
    Application.get_env(:new_you, :identity_registration_legal_versions) == %{
      terms_version_id: @development_terms_id,
      privacy_version_id: @development_privacy_id
    }
  end

  defp password_matches?(%RegistrationOperation{} = operation, password) do
    operation.verifier_provider == @verifier_provider and
      operation.verifier_version == @verifier_version and
      is_binary(operation.password_verifier) and
      safe_password_verify(password, operation.password_verifier)
  end

  defp safe_password_verify(password, verifier) do
    AshAuthentication.Argon2Provider.valid?(password, verifier)
  rescue
    _ -> false
  end

  defp hash_password(password) do
    case AshAuthentication.Argon2Provider.hash(password) do
      {:ok, verifier} when is_binary(verifier) -> {:ok, verifier}
      _ -> {:error, :password_hash_failed}
    end
  rescue
    _ -> {:error, :password_hash_failed}
  end

  defp next_pmr do
    generator = Application.get_env(:new_you, :identity_pmr_generator, &PMR.generate/0)

    case generator.() do
      {:ok, pmr} when is_binary(pmr) ->
        if PMR.valid?(pmr), do: {:ok, pmr}, else: {:error, :generation_failed}

      _ ->
        {:error, :generation_failed}
    end
  rescue
    _ -> {:error, :generation_failed}
  end

  defp error_has_unique_field?(error, field) do
    case error do
      %Ash.Error.Changes.InvalidAttribute{field: ^field, private_vars: private_vars} ->
        Keyword.get(private_vars || [], :constraint_type) == :unique

      %{errors: errors} when is_list(errors) ->
        Enum.any?(errors, &error_has_unique_field?(&1, field))

      _ ->
        false
    end
  end

  defp operation_id_collision?(error) do
    error_has_unique_field?(error, :operation_id) or
      case error do
        %Ecto.ConstraintError{
          type: :unique,
          constraint: "registration_operations_opaque_operation_id_index"
        } ->
          true

        %{errors: errors} when is_list(errors) ->
          Enum.any?(errors, &operation_id_collision?/1)

        _ ->
          false
      end
  end

  defp now do
    clock = Application.get_env(:new_you, :identity_clock, &DateTime.utc_now/0)
    clock.() |> DateTime.truncate(:microsecond)
  end
end
