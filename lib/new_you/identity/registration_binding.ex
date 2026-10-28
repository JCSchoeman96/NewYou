defmodule NewYou.Identity.RegistrationBinding do
  @moduledoc false

  @domain_separator "registration-binding:v1"
  @keyring_env "NEWYOU_IDENTITY_REGISTRATION_BINDING_KEYS_JSON"
  @active_key_env "NEWYOU_IDENTITY_REGISTRATION_BINDING_KEY_ACTIVE_VERSION"

  @spec fingerprint(map()) :: {:ok, binary(), String.t()} | {:error, :key_unavailable}
  def fingerprint(input) do
    with {:ok, keyring} <- keyring(),
         version when is_binary(version) <- keyring.active_version,
         {:ok, key} <- key_for_version(keyring, version),
         digest <- digest(input, key) do
      {:ok, digest, version}
    else
      _ -> {:error, :key_unavailable}
    end
  end

  @spec fingerprint_for_version(map(), String.t()) ::
          {:ok, binary()} | {:error, :key_unavailable}
  def fingerprint_for_version(input, version) when is_binary(version) do
    with {:ok, keyring} <- keyring(),
         {:ok, key} <- key_for_version(keyring, version) do
      {:ok, digest(input, key)}
    else
      _ -> {:error, :key_unavailable}
    end
  end

  def fingerprint_for_version(_, _), do: {:error, :key_unavailable}

  @spec equal?(binary(), binary()) :: boolean()
  def equal?(left, right)
      when is_binary(left) and is_binary(right) and byte_size(left) == byte_size(right),
      do: :crypto.hash_equals(left, right)

  def equal?(_, _), do: false

  defp digest(input, key) do
    payload =
      frame("version", "domain", @domain_separator) <>
        frame("uuid", "operation_id", input.operation_id) <>
        frame("string", "first_name", input.first_name) <>
        frame("string", "surname", input.surname) <>
        frame("string", "canonical_email", input.email) <>
        frame("enum", "preferred_language", Atom.to_string(input.preferred_language)) <>
        frame("enum", "acceptance_locale", Atom.to_string(input.acceptance_locale)) <>
        frame("boolean", "confirmed_age_18", <<if(input.confirmed_age_18?, do: 1, else: 0)>>) <>
        frame("identifier", "terms_version_id", input.terms_version_id) <>
        frame("identifier", "privacy_version_id", input.privacy_version_id)

    :crypto.mac(:hmac, :sha256, key, payload)
  end

  defp frame(type, name, value) do
    type = :erlang.iolist_to_binary(type)
    name = :erlang.iolist_to_binary(name)

    <<byte_size(type)::unsigned-big-32, type::binary, byte_size(name)::unsigned-big-32,
      name::binary, byte_size(value)::unsigned-big-64, value::binary>>
  end

  defp key_for_version(keyring, version) do
    case Map.get(keyring, :keys) do
      keys when is_map(keys) ->
        case Map.fetch(keys, version) do
          {:ok, key} when is_binary(key) and byte_size(key) >= 32 -> {:ok, key}
          _ -> {:error, :key_unavailable}
        end

      _ ->
        {:error, :key_unavailable}
    end
  end

  defp keyring do
    case Application.fetch_env(:new_you, :identity_registration_binding_keys) do
      {:ok, value} -> validate_keyring(value)
      :error -> keyring_from_runtime_environment()
    end
  end

  defp keyring_from_runtime_environment do
    with version when is_binary(version) and version != "" <- System.get_env(@active_key_env),
         encoded_keys when is_binary(encoded_keys) <- System.get_env(@keyring_env),
         {:ok, encoded_keys} when is_map(encoded_keys) <- Jason.decode(encoded_keys),
         {:ok, keys} <- decode_keys(encoded_keys) do
      validate_keyring(%{active_version: version, keys: keys})
    else
      _ -> {:error, :key_unavailable}
    end
  end

  defp decode_keys(encoded_keys) do
    Enum.reduce_while(encoded_keys, {:ok, %{}}, fn
      {version, encoded}, {:ok, keys} when is_binary(version) and is_binary(encoded) ->
        case Base.decode64(encoded) do
          {:ok, key} when byte_size(key) >= 32 -> {:cont, {:ok, Map.put(keys, version, key)}}
          _ -> {:halt, {:error, :key_unavailable}}
        end

      _, _ ->
        {:halt, {:error, :key_unavailable}}
    end)
  end

  defp validate_keyring(%{active_version: version, keys: keys} = keyring)
       when is_binary(version) and version != "" and is_map(keys) do
    with {:ok, _} <- key_for_version(keyring, version) do
      {:ok, keyring}
    end
  end

  defp validate_keyring(_), do: {:error, :key_unavailable}
end
