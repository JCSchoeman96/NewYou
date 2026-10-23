defmodule NewYou.Proof.ProviderFixtures do
  @moduledoc "Synthetic provider authentication material for proof tests only."

  @key Path.expand("provider_auth.key", __DIR__) |> File.read!() |> String.trim()

  @spec key() :: binary()
  def key, do: @key

  @spec sign(binary(), binary()) :: binary()
  def sign(body, key), do: :crypto.mac(:hmac, :sha256, key, body)
end
