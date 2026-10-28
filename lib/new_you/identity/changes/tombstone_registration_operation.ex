defmodule NewYou.Identity.Changes.TombstoneRegistrationOperation do
  @moduledoc false

  use Ash.Resource.Change

  alias Ash.Changeset

  @sensitive_attributes [
    :request_fingerprint,
    :fingerprint_key_version,
    :password_verifier,
    :verifier_provider,
    :verifier_version,
    :outcome,
    :committed_at,
    :expires_at,
    :created_account_id
  ]

  @impl true
  def change(changeset, _opts, _context) do
    changeset = Changeset.force_change_attribute(changeset, :state, :tombstoned)

    Enum.reduce(@sensitive_attributes, changeset, fn attribute, changeset ->
      Changeset.force_change_attribute(changeset, attribute, nil)
    end)
  end
end
