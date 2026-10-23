defmodule NewYou.Proof.Provider do
  @moduledoc "Deterministic provider observations for test scenarios only."

  @max_scripts 32
  @max_steps 64
  @max_label 64
  @outcomes [
    :not_invoked,
    :rejected_before_submission,
    :accepted,
    :delivered,
    :bounced_or_failed,
    :unknown,
    :backlog,
    :confirmed_no_operation,
    :reconciliation_rejected,
    :reconciliation_accepted,
    :reconciliation_delivered,
    :reconciliation_failed
  ]

  @type safe_ref :: String.t()
  @type step :: atom() | String.t()

  @spec configure(NewYou.Proof.Scenario.t(), map()) :: :ok | {:error, :invalid_script | term()}
  def configure(scenario, scripts)
      when is_map(scripts) and map_size(scripts) > 0 and map_size(scripts) <= @max_scripts do
    with {:ok, normalized} <- normalize_scripts(scripts) do
      NewYou.Proof.Scenario.request(scenario, {:provider_configure, normalized})
    end
  end

  def configure(_scenario, _scripts), do: {:error, :invalid_script}

  @spec next(NewYou.Proof.Scenario.t(), safe_ref(), step()) :: {:ok, map()} | {:error, atom()}
  def next(scenario, operation_ref, script_step) do
    if valid_ref?(operation_ref) and valid_label?(script_step) do
      NewYou.Proof.Scenario.request(scenario, {:provider_next, operation_ref, script_step})
    else
      {:error, :invalid_script}
    end
  end

  @spec release_backlog(NewYou.Proof.Scenario.t(), safe_ref()) :: {:ok, map()} | {:error, atom()}
  def release_backlog(scenario, operation_ref) do
    if valid_ref?(operation_ref),
      do: NewYou.Proof.Scenario.request(scenario, {:provider_release_backlog, operation_ref}),
      else: {:error, :invalid_script}
  end

  @doc "Authenticates a synthetic fixture. This is not a Communications ingress boundary."
  @spec authenticate_fixture({safe_ref(), safe_ref(), binary()} | term(), binary(), binary()) ::
          {:ok, :authenticated}
          | {:error, :invalid_fixture | :invalid_signature | :operation_reference_mismatch}
  def authenticate_fixture({expected_ref, operation_ref, body}, signature, key)
      when is_binary(expected_ref) and is_binary(operation_ref) and is_binary(body) and
             is_binary(signature) and is_binary(key) do
    with :ok <- validate_fixture_refs(expected_ref, operation_ref),
         :ok <- validate_fixture_signature(operation_ref, body, signature, key),
         :ok <- validate_expected_ref(expected_ref, operation_ref) do
      {:ok, :authenticated}
    end
  end

  def authenticate_fixture(_fixture, _signature, _key), do: {:error, :invalid_fixture}

  defp normalize_scripts(scripts) do
    Enum.reduce_while(scripts, {:ok, %{}}, fn {operation_ref, steps}, {:ok, acc} ->
      case normalize_steps(operation_ref, steps) do
        {:ok, normalized} -> {:cont, {:ok, Map.put(acc, operation_ref, normalized)}}
        :error -> {:halt, {:error, :invalid_script}}
      end
    end)
  end

  defp normalize_steps(operation_ref, steps)
       when is_list(steps) and length(steps) in 1..@max_steps do
    with true <- valid_ref?(operation_ref),
         {:ok, normalized} <- Enum.reduce_while(steps, {:ok, []}, &append_step/2) do
      {:ok, Enum.reverse(normalized)}
    else
      _ -> :error
    end
  end

  defp normalize_steps(_, _), do: :error

  defp append_step(step, {:ok, acc}) do
    case normalize_step(step) do
      {:ok, normalized} -> {:cont, {:ok, [normalized | acc]}}
      :error -> {:halt, :error}
    end
  end

  defp normalize_step({label, outcome}) when outcome in @outcomes and is_atom(label) do
    if valid_label?(label), do: {:ok, basic_event(label, outcome)}, else: :error
  end

  defp normalize_step({label, %{outcome: outcome, event_ref: event_ref, logical_order: order}})
       when outcome in @outcomes and is_binary(event_ref) and is_integer(order) and order >= 0 do
    if valid_label?(label) and valid_label?(event_ref),
      do: {:ok, safe_event(label, outcome, event_ref, order)},
      else: :error
  end

  defp normalize_step(_), do: :error

  defp basic_event(label, outcome), do: %{step: label, outcome: outcome}

  defp safe_event(label, outcome, event_ref, order),
    do: %{step: label, outcome: outcome, event_ref: event_ref, logical_order: order}

  defp valid_ref?(value),
    do:
      is_binary(value) and byte_size(value) in 1..96 and
        Regex.match?(~r/\A[a-zA-Z0-9_-]+\z/, value)

  defp valid_label?(value),
    do: (is_atom(value) or is_binary(value)) and byte_size(to_string(value)) in 1..@max_label

  defp valid_signature?(data, signature, key) do
    expected = :crypto.mac(:hmac, :sha256, key, data)
    Plug.Crypto.secure_compare(expected, signature)
  end

  defp validate_fixture_refs(expected_ref, operation_ref) do
    if valid_ref?(expected_ref) and valid_ref?(operation_ref),
      do: :ok,
      else: {:error, :invalid_fixture}
  end

  defp validate_fixture_signature(operation_ref, body, signature, key) do
    if valid_signature?(operation_ref <> "|" <> body, signature, key),
      do: :ok,
      else: {:error, :invalid_signature}
  end

  defp validate_expected_ref(expected_ref, expected_ref), do: :ok

  defp validate_expected_ref(_expected_ref, _operation_ref),
    do: {:error, :operation_reference_mismatch}
end
