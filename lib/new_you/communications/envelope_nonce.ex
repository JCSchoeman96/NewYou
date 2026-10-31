defmodule NewYou.Communications.EnvelopeNonce do
  @moduledoc false
  # Reservations are non-secret cryptographic bookkeeping. They outlive envelope
  # deletion so a key and nonce cannot be reused after the ciphertext is cleared.
  use Ash.Resource,
    otp_app: :new_you,
    domain: NewYou.Communications,
    data_layer: AshPostgres.DataLayer,
    authorizers: [Ash.Policy.Authorizer]

  postgres do
    table "communications_envelope_nonces"
    repo NewYou.Repo

    check_constraints do
      check_constraint :nonce, "communications_reserved_nonce_length",
        check: "octet_length(nonce) = 12",
        message: "is invalid"
    end
  end

  actions do
    create :reserve do
      public? false
      accept [:nonce]
    end
  end

  policies do
    policy always() do
      forbid_if always()
    end
  end

  attributes do
    attribute :nonce, :binary do
      primary_key? true
      allow_nil? false
      sensitive? true
      public? false
    end
  end
end
