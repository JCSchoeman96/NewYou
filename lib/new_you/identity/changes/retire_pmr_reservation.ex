defmodule NewYou.Identity.Changes.RetirePmrReservation do
  @moduledoc false

  use Ash.Resource.Change

  alias Ash.Changeset

  @identity_attributes [
    :first_name,
    :surname,
    :email,
    :preferred_language,
    :confirmed_age_18?,
    :terms_version_id,
    :privacy_version_id,
    :legal_accepted_at,
    :acceptance_locale,
    :credential_status,
    :hashed_password,
    :email_verified?
  ]

  @impl true
  def change(changeset, _opts, _context) do
    changeset = Changeset.force_change_attribute(changeset, :lifecycle_state, :retired)

    Enum.reduce(@identity_attributes, changeset, fn attribute, changeset ->
      Changeset.force_change_attribute(changeset, attribute, nil)
    end)
  end
end
