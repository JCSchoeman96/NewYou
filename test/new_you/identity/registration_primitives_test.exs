defmodule NewYou.Identity.RegistrationPrimitivesTest do
  use NewYou.DataCase, async: false

  @terms_id "NEWYOU-TERMS-EN-DEV-2026-10-27-001"
  @privacy_id "NEWYOU-PRIVACY-EN-DEV-2026-10-27-001"

  setup do
    previous_keys = Application.get_env(:new_you, :identity_registration_binding_keys)
    previous_token_signing_secret = Application.get_env(:new_you, :identity_token_signing_secret)
    previous_clock = Application.get_env(:new_you, :identity_clock)
    previous_pmr_generator = Application.get_env(:new_you, :identity_pmr_generator)

    Application.put_env(:new_you, :identity_registration_binding_keys, %{
      active_version: "test-v1",
      keys: %{"test-v1" => :crypto.strong_rand_bytes(32)}
    })

    Application.put_env(:new_you, :identity_token_signing_secret, :crypto.strong_rand_bytes(32))

    Application.put_env(:new_you, :identity_clock, fn -> DateTime.utc_now() end)

    on_exit(fn ->
      restore_app_env(:identity_registration_binding_keys, previous_keys)
      restore_app_env(:identity_token_signing_secret, previous_token_signing_secret)
      restore_app_env(:identity_clock, previous_clock)
      restore_app_env(:identity_pmr_generator, previous_pmr_generator)
    end)

    :ok
  end

  test "canonical email follows the accepted ASCII normalization contract" do
    assert {:ok, "Alice+campaign.Example@example.com"} =
             email_canonicalize(" \tAlice+campaign.Example@EXAMPLE.COM\t ")

    assert {:ok, "Alice.Example+tag@example.com"} =
             email_canonicalize("Alice.Example+tag@EXAMPLE.COM")

    assert {:ok, "!#$%&'*+-/=?^_`{|}~@a1.example"} =
             email_canonicalize("!#$%&'*+-/=?^_`{|}~@A1.EXAMPLE")

    assert {:ok, "Alice@example.com"} = email_canonicalize("Alice@EXAMPLE.COM")
    assert {:ok, "alice@example.com"} = email_canonicalize("alice@example.com")

    refute elem(email_canonicalize("Alice@EXAMPLE.COM"), 1) ==
             elem(email_canonicalize("alice@example.com"), 1)
  end

  test "canonical email rejects unapproved syntax, whitespace and non-ASCII input" do
    rejected = [
      "\nAlice@example.com",
      "Alice\v@example.com",
      "Alice Smith@example.com",
      "Alice\u00a0@example.com",
      "Alice\u200b@example.com",
      "Alice@exämple.com",
      "álîce@example.com",
      "\"Alice Example\"@example.com",
      "Alice(comment)@example.com",
      ".alice@example.com",
      "alice.@example.com",
      "alice..smith@example.com",
      "alice@localhost",
      "alice@example..com",
      "alice@-example.com",
      "alice@example-.com",
      "alice@xn--example.com",
      "alice@[127.0.0.1]",
      "alice@example.com\tother"
    ]

    for email <- rejected do
      assert {:error, _} = email_canonicalize(email)
    end
  end

  test "canonical email enforces the locked local, label and mailbox limits" do
    local_64 = String.duplicate("a", 64) <> "@example.com"
    local_65 = String.duplicate("a", 65) <> "@example.com"
    label_63 = "alice@" <> "a" <> String.duplicate("b", 61) <> "c.com"
    label_64 = "alice@" <> "a" <> String.duplicate("b", 62) <> "c.com"

    assert {:ok, ^local_64} = email_canonicalize(local_64)
    assert {:error, _} = email_canonicalize(local_65)
    assert {:ok, ^label_63} = email_canonicalize(label_63)
    assert {:error, _} = email_canonicalize(label_64)

    mailbox_254 =
      String.duplicate("a", 64) <>
        "@" <>
        String.duplicate("b", 63) <>
        "." <> String.duplicate("c", 63) <> "." <> String.duplicate("d", 61)

    mailbox_255 =
      String.duplicate("a", 64) <>
        "@" <>
        String.duplicate("b", 63) <>
        "." <> String.duplicate("c", 63) <> "." <> String.duplicate("d", 62)

    assert byte_size(mailbox_254) == 254
    assert byte_size(mailbox_255) == 255
    assert {:ok, ^mailbox_254} = email_canonicalize(mailbox_254)
    assert {:error, _} = email_canonicalize(mailbox_255)

    domain_252 =
      "a@" <>
        String.duplicate("a", 63) <>
        "." <>
        String.duplicate("b", 63) <>
        "." <>
        String.duplicate("c", 63) <>
        "." <>
        String.duplicate("d", 60)

    domain_253 =
      "a@" <>
        String.duplicate("a", 63) <>
        "." <>
        String.duplicate("b", 63) <>
        "." <>
        String.duplicate("c", 63) <>
        "." <>
        String.duplicate("d", 61)

    assert {:ok, ^domain_252} = email_canonicalize(domain_252)
    assert {:error, _} = email_canonicalize(domain_253)
  end

  test "distinct local-part case remains distinct in PostgreSQL canonical identity" do
    assert {:ok, _} = register(%{valid_request() | email: "Alice@example.com"})

    lowercase_request = %{valid_request() | email: "alice@example.com"}
    assert {:ok, _} = register(lowercase_request)

    assert resource_count("Account") == 2
    assert resource_count("Token") == 2
    assert resource_count("RegistrationOperation") == 2
  end

  test "PMR checksum matches the approved MOD 37,2 vector and validates exact form" do
    assert "PMR-0123456789ABCDEFA" == pmr_check("PMR0123456789ABCDEF")
    assert true == pmr_valid?("PMR-0123456789ABCDEFA")
    assert false == pmr_valid?("PMR-0123456789ABCDEF0")
    assert false == pmr_valid?("pmr-0123456789ABCDEFA")
    assert false == pmr_valid?("PMR-0123456789ABCDEFA ")
  end

  test "PMR allocation returns a canonical 16-character Base36 value with a check character" do
    assert {:ok, pmr} = pmr_generate()
    assert Regex.match?(~r/^PMR-[0-9A-Z]{16}[0-9A-Z*]$/, pmr)
    assert pmr_valid?(pmr)
  end

  test "registration rejects missing required fields and failed gates without creating records" do
    requests = [
      Map.delete(valid_request(), :first_name),
      Map.delete(valid_request(), :surname),
      Map.delete(valid_request(), :email),
      Map.delete(valid_request(), :password),
      Map.delete(valid_request(), :preferred_language),
      Map.delete(valid_request(), :confirmed_age_18?),
      Map.put(valid_request(), :confirmed_age_18?, false),
      Map.put(valid_request(), :preferred_language, "fr"),
      Map.delete(valid_request(), :terms_version_id),
      Map.delete(valid_request(), :privacy_version_id),
      Map.put(valid_request(), :terms_version_id, "unapproved-terms"),
      Map.put(valid_request(), :privacy_version_id, "unapproved-privacy"),
      Map.put(valid_request(), :password, "")
    ]

    for request <- requests do
      assert {:error, _} = register(request)
    end

    assert resource_count("Account") == 0
    assert resource_count("Token") == 0
    assert resource_count("RegistrationOperation") == 0
  end

  test "a valid request creates one active credential, PMR, verification token and operation" do
    request = valid_request()

    result = register(request)
    assert match?({:ok, %{status: :verification_pending}}, result)
    assert {:ok, %{verification_proof: verification_proof}} = result

    assert is_binary(verification_proof)
    assert length(String.split(verification_proof, ".")) == 3
    refute String.contains?(inspect(result), verification_proof)

    [account] = records("Account")
    [token] = records("Token")
    [operation] = records("RegistrationOperation")

    assert account.first_name == request.first_name
    assert account.surname == request.surname
    assert account.email == "Alice+campaign.Example@example.com"
    assert account.preferred_language == :af
    assert account.confirmed_age_18?
    assert account.terms_version_id == @terms_id
    assert account.privacy_version_id == @privacy_id
    assert account.acceptance_locale == :af
    assert account.credential_status == :active
    assert is_binary(account.hashed_password)
    assert account_does_not_retain_raw_password?(account, request.password)

    assert {:ok, <<_timestamp::48, 7::4, _random_a::12, 2::2, _random_b::62>>} =
             Ecto.UUID.dump(account.id)

    assert Regex.match?(~r/^PMR-[0-9A-Z]{16}[0-9A-Z*]$/, account.pmr)
    assert pmr_valid?(account.pmr)
    refute account.email_verified?

    assert token.account_id == account.id
    assert token.purpose == "email_verification"
    assert is_binary(token.jti)
    assert token.expires_at > DateTime.utc_now()
    refute Map.has_key?(Map.from_struct(token), :token)
    assert :binary.match(:erlang.term_to_binary(token), verification_proof) == :nomatch

    assert operation.operation_id == request.operation_id
    assert operation.outcome == :verification_pending
    assert operation.created_account_id == account.id
    assert operation.expires_at == DateTime.add(operation.committed_at, 24 * 60 * 60, :second)
    assert byte_size(operation.request_fingerprint) == 32
    assert operation.password_verifier == account.hashed_password
    refute Map.has_key?(Map.from_struct(operation), :password)
    assert :binary.match(:erlang.term_to_binary(operation), request.password) == :nomatch
    refute Code.ensure_loaded?(Module.concat(NewYou.Identity, "Session"))
    refute Enum.any?(Ash.Resource.Info.actions(NewYou.Identity.Account), &(&1.type == :destroy))
  end

  test "an identical operation retry replays without creating duplicate consequences" do
    request = valid_request()

    assert {:ok, %{status: :verification_pending}} = register(request)
    assert {:ok, %{status: :verification_pending}} = register(request)

    assert resource_count("Account") == 1
    assert resource_count("Token") == 1
    assert resource_count("RegistrationOperation") == 1
  end

  test "reusing an operation ID with changed input rejects without mutation" do
    request = valid_request()
    assert {:ok, _} = register(request)

    assert {:error, _} = register(%{request | surname: "Changed"})
    changed_password = Base.url_encode64(:crypto.strong_rand_bytes(32), padding: false)
    assert {:error, _} = register(%{request | password: changed_password})

    assert resource_count("Account") == 1
    assert resource_count("Token") == 1
    assert resource_count("RegistrationOperation") == 1
  end

  test "a distinct existing-email operation returns the neutral result without new identity records" do
    first = valid_request()
    second = %{valid_request() | operation_id: Ecto.UUID.generate()}

    assert {:ok, first_result} = register(first)
    assert {:ok, second_result} = register(%{second | email: first.email})
    assert first_result.status == second_result.status

    assert resource_count("Account") == 1
    assert resource_count("Token") == 1
    assert resource_count("RegistrationOperation") == 2
  end

  test "a duplicate-email operation replays its own slow verifier without consulting the account credential" do
    first = valid_request()
    second = %{valid_request() | operation_id: Ecto.UUID.generate(), email: first.email}

    assert {:ok, %{status: :verification_pending}} = register(first)
    assert {:ok, %{status: :verification_pending}} = register(second)
    assert {:ok, %{status: :verification_pending}} = register(second)
    changed_password = Base.url_encode64(:crypto.strong_rand_bytes(32), padding: false)
    assert {:error, _} = register(%{second | password: changed_password})

    [account] = records("Account")
    operations = records("RegistrationOperation")
    duplicate = Enum.find(operations, &(&1.operation_id == second.operation_id))

    assert account.hashed_password != duplicate.password_verifier
    assert duplicate.created_account_id == nil
    assert duplicate.outcome == :verification_pending
    assert resource_count("Account") == 1
    assert resource_count("Token") == 1
    assert resource_count("RegistrationOperation") == 2
  end

  test "expiry tombstones sensitive binding fields and prevents operation ID reuse" do
    request = valid_request()
    assert {:ok, _} = register(request)

    [bound] = records("RegistrationOperation")
    expired_at = DateTime.add(bound.expires_at, 1, :second)
    Application.put_env(:new_you, :identity_clock, fn -> expired_at end)

    assert {:error, _} = register(request)
    [operation] = records("RegistrationOperation")

    assert operation.state == :tombstoned
    assert is_nil(operation.request_fingerprint)
    assert is_nil(operation.fingerprint_key_version)
    assert is_nil(operation.password_verifier)
    assert is_nil(operation.verifier_provider)
    assert is_nil(operation.verifier_version)
    assert is_nil(operation.outcome)
    assert is_nil(operation.committed_at)
    assert is_nil(operation.expires_at)
    assert is_nil(operation.created_account_id)
    assert {:error, _} = register(request)

    assert resource_count("Account") == 1
    assert resource_count("Token") == 1
    assert resource_count("RegistrationOperation") == 1
  end

  test "a same-request replay does not extend the 24-hour registration binding" do
    request = valid_request()
    assert {:ok, _} = register(request)
    [before_replay] = records("RegistrationOperation")

    replay_time = DateTime.add(before_replay.committed_at, 12 * 60 * 60, :second)
    Application.put_env(:new_you, :identity_clock, fn -> replay_time end)

    assert {:ok, _} = register(request)
    [after_replay] = records("RegistrationOperation")
    assert after_replay.expires_at == before_replay.expires_at
    assert after_replay.committed_at == before_replay.committed_at
  end

  test "a live operation fails closed when its recorded HMAC key version is unavailable" do
    request = valid_request()
    assert {:ok, _} = register(request)

    Application.put_env(:new_you, :identity_registration_binding_keys, %{
      active_version: "test-v2",
      keys: %{"test-v2" => :crypto.strong_rand_bytes(32)}
    })

    assert {:error, _} = register(request)
    assert resource_count("Account") == 1
    assert resource_count("Token") == 1
    assert resource_count("RegistrationOperation") == 1
  end

  test "registration fails closed when its dedicated binding key is unavailable" do
    request = valid_request()
    previous = Application.get_env(:new_you, :identity_registration_binding_keys)
    Application.delete_env(:new_you, :identity_registration_binding_keys)

    try do
      assert {:error, _} = register(request)
      assert resource_count("Account") == 0
      assert resource_count("Token") == 0
      assert resource_count("RegistrationOperation") == 0
    after
      if is_nil(previous) do
        Application.delete_env(:new_you, :identity_registration_binding_keys)
      else
        Application.put_env(:new_you, :identity_registration_binding_keys, previous)
      end
    end
  end

  test "registration rolls back all identity writes when token signing material is unavailable" do
    request = valid_request()
    previous = Application.get_env(:new_you, :identity_token_signing_secret)
    Application.delete_env(:new_you, :identity_token_signing_secret)

    try do
      assert {:error, _} = register(request)
      assert resource_count("Account") == 0
      assert resource_count("Token") == 0
      assert resource_count("RegistrationOperation") == 0
    after
      restore_app_env(:identity_token_signing_secret, previous)
    end
  end

  test "registration rejects operation IDs outside the approved UUIDv4 format" do
    invalid = %{valid_request() | operation_id: "018ecb40-c457-73e6-a400-000398daddd9"}

    assert {:error, _} = register(invalid)
    assert resource_count("Account") == 0
    assert resource_count("Token") == 0
    assert resource_count("RegistrationOperation") == 0
  end

  test "PMR allocation collision retries stop at five candidates and then fail closed" do
    candidate = "PMR-0123456789ABCDEFA"
    attempts = self()

    Application.put_env(:new_you, :identity_pmr_generator, fn ->
      send(attempts, :pmr_candidate_generated)
      {:ok, candidate}
    end)

    first = valid_request()
    assert {:ok, _} = register(first)

    for _ <- 1..1, do: assert_receive(:pmr_candidate_generated)

    second = %{valid_request() | email: "second@example.com"}
    assert {:error, _} = register(second)

    for _ <- 1..5, do: assert_receive(:pmr_candidate_generated)
    refute_receive :pmr_candidate_generated

    assert resource_count("Account") == 1
    assert resource_count("Token") == 1
    assert resource_count("RegistrationOperation") == 1
  end

  defp valid_request do
    %{
      operation_id: Ecto.UUID.generate(),
      first_name: "Alice",
      surname: "Example",
      email: " \tAlice+campaign.Example@EXAMPLE.COM\t ",
      password: Base.url_encode64(:crypto.strong_rand_bytes(32), padding: false),
      preferred_language: :af,
      confirmed_age_18?: true,
      terms_version_id: @terms_id,
      privacy_version_id: @privacy_id
    }
  end

  defp email_canonicalize(value), do: NewYou.Identity.Email.canonicalize(value)

  defp pmr_check(value), do: NewYou.Identity.PMR.check(value)

  defp pmr_valid?(value), do: NewYou.Identity.PMR.valid?(value)

  defp pmr_generate, do: NewYou.Identity.PMR.generate()

  defp register(request), do: NewYou.Identity.register(request)

  defp records(name) do
    resource = Module.concat(NewYou.Identity, name)
    Ash.read!(resource, authorize?: false)
  end

  defp resource_count(name), do: length(records(name))

  defp account_does_not_retain_raw_password?(account, password) do
    is_binary(account.hashed_password) and account.hashed_password != password and
      not Map.has_key?(Map.from_struct(account), :password)
  end

  defp restore_app_env(key, nil), do: Application.delete_env(:new_you, key)
  defp restore_app_env(key, value), do: Application.put_env(:new_you, key, value)
end
