defmodule NewYou.Secrets do
  use AshAuthentication.Secret

  def secret_for(
        [:authentication, :tokens, :signing_secret],
        NewYou.Identity.Account,
        _opts,
        _context
      ) do
    case Application.get_env(:new_you, :identity_token_signing_secret) do
      secret when is_binary(secret) and byte_size(secret) >= 32 -> {:ok, secret}
      _ -> :error
    end
  end
end
