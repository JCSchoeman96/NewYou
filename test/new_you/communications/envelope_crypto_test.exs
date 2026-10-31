defmodule NewYou.Communications.EnvelopeCryptoTest do
  use ExUnit.Case, async: true
  alias NewYou.Communications.EnvelopeCrypto

  test "authentication binds the intent, source and purpose and rejects malformed or tampered data" do
    key = :crypto.strong_rand_bytes(32)
    bearer = :crypto.strong_rand_bytes(32)
    binding = {"intent", "challenge", "email_verification"}

    result =
      try do
        with {:ok, envelope} <-
               EnvelopeCrypto.encrypt(key, binding, bearer, :crypto.strong_rand_bytes(12)),
             {:ok, ^bearer} <- EnvelopeCrypto.decrypt(key, binding, envelope) do
          <<cipher_byte, cipher_rest::binary>> = envelope.ciphertext
          <<tag_byte, tag_rest::binary>> = envelope.tag

          bad = [
            {key, {"other", "challenge", "email_verification"}, envelope},
            {key, {"intent", "other", "email_verification"}, envelope},
            {key, {"intent", "challenge", "other"}, envelope},
            {key, binding,
             %{envelope | ciphertext: <<Bitwise.bxor(cipher_byte, 1), cipher_rest::binary>>}},
            {key, binding, %{envelope | tag: <<Bitwise.bxor(tag_byte, 1), tag_rest::binary>>}},
            {key, binding, %{envelope | tag: binary_part(envelope.tag, 0, 15)}},
            {key, binding, %{envelope | nonce: <<0>>}},
            {:crypto.strong_rand_bytes(32), binding, envelope},
            {nil, binding, envelope}
          ]

          Enum.all?(bad, fn {k, b, e} ->
            EnvelopeCrypto.decrypt(k, b, e) == {:error, :invalid_envelope}
          end)
        else
          _ -> false
        end
      rescue
        _ -> false
      end

    assert result, "crypto boundary did not reject an invalid envelope"
  end

  test "unknown and missing key versions fail closed" do
    key = :crypto.strong_rand_bytes(32)
    bearer = :crypto.strong_rand_bytes(32)
    binding = {"intent", "challenge", "email_verification"}

    valid =
      try do
        {:ok, encrypted} =
          EnvelopeCrypto.encrypt(key, binding, bearer, :crypto.strong_rand_bytes(12))

        keyring = %{"v1" => key}

        EnvelopeCrypto.decrypt_versioned(keyring, "v1", binding, encrypted) == {:ok, bearer} and
          EnvelopeCrypto.decrypt_versioned(keyring, "unknown", binding, encrypted) ==
            {:error, :invalid_envelope} and
          EnvelopeCrypto.decrypt_versioned(%{}, "v1", binding, encrypted) ==
            {:error, :invalid_envelope}
      rescue
        _ -> false
      end

    assert valid, "versioned decryption did not fail closed"
  end
end
