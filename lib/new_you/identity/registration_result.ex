defmodule NewYou.Identity.RegistrationResult do
  @moduledoc false

  @derive {Inspect, only: [:status, :account_id]}
  defstruct [:status, :account_id, :verification_proof]

  @type t :: %__MODULE__{
          status: :verification_pending | nil,
          account_id: Ecto.UUID.t() | nil,
          verification_proof: String.t() | nil
        }
end
