defmodule NewYou.Audit.Changes.FulfillEvidenceObligation do
  use Ash.Resource.Change

  @impl true
  def change(changeset, _opts, _context) do
    case changeset.data.state do
      :open ->
        case NewYou.Audit.get_evidence_record_by_obligation(changeset.data.id,
               authorize?: false
             ) do
          {:ok, %NewYou.Audit.EvidenceRecord{}} ->
            changeset
            |> Ash.Changeset.change_attribute(:state, :fulfilled)
            |> Ash.Changeset.change_attribute(:fulfilled_at, DateTime.utc_now())

          {:ok, nil} ->
            Ash.Changeset.add_error(changeset,
              field: :state,
              message: "requires its materialised evidence record"
            )

          {:error, _error} ->
            Ash.Changeset.add_error(changeset,
              field: :state,
              message: "could not verify materialised evidence record"
            )
        end

      _ ->
        Ash.Changeset.add_error(changeset,
          field: :state,
          message: "only an open evidence obligation can be fulfilled"
        )
    end
  end
end
