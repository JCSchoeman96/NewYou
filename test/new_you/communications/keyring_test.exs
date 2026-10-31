defmodule NewYou.Communications.KeyringTest do
  use ExUnit.Case, async: true
  alias NewYou.Communications.Keyring

  test "runtime keyring accepts only explicit active 256-bit keys and fails closed" do
    key = :crypto.strong_rand_bytes(32)
    encoded = Jason.encode!(%{"v1" => Base.encode64(key)})

    result =
      try do
        {:ok, %{active: "v1", keys: %{"v1" => ^key}}} = Keyring.from_environment("v1", encoded)

        Keyring.from_environment(nil, encoded) == :error and
          Keyring.from_environment("v2", encoded) == :error and
          Keyring.from_environment("v1", "invalid") == :error and
          Keyring.from_environment("v1", Jason.encode!(%{"v1" => Base.encode64(<<0>>)})) == :error
      rescue
        _ -> false
      end

    assert result, "invalid keyring configuration was accepted"
  end
end
