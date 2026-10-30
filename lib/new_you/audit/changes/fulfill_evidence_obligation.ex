defmodule NewYou.Audit.Changes.FulfillEvidenceObligation do
  use Ash.Resource.Change

  @impl true
  def change(changeset, _opts, _context) do
    case changeset.data.state do
      :open ->
        changeset
        |> Ash.Changeset.change_attribute(:state, :fulfilled)
        |> Ash.Changeset.change_attribute(:fulfilled_at, DateTime.utc_now())

      _ ->
        Ash.Changeset.add_error(changeset,
          field: :state,
          message: "only an open evidence obligation can be fulfilled"
        )
    end
  end
end
