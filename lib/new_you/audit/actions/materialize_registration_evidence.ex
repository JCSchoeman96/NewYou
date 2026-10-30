defmodule NewYou.Audit.Actions.MaterializeRegistrationEvidence do
  use Ash.Resource.Actions.Implementation

  @impl true
  def run(input, _opts, _context) do
    with {:ok, id} <- obligation_id(input.arguments.primary_key),
         {:ok, obligation} <- NewYou.Audit.get_evidence_obligation(id, authorize?: false),
         {:ok, record} <- materialize_or_replay(obligation) do
      {:ok, %{obligation_id: obligation.id, evidence_record_id: record.id}}
    else
      {:error, error} -> {:error, error}
      _ -> {:error, :evidence_materialisation_unavailable}
    end
  end

  defp materialize_or_replay(%NewYou.Audit.EvidenceObligation{state: :open} = obligation) do
    case NewYou.Audit.get_evidence_record_by_obligation(obligation.id, authorize?: false) do
      {:ok, nil} ->
        with {:ok, record} <-
               Ash.create(
                 NewYou.Audit.EvidenceRecord,
                 %{obligation_id: obligation.id},
                 action: :materialize,
                 domain: NewYou.Audit,
                 authorize?: false
               ),
             {:ok, _fulfilled} <-
               Ash.update(obligation, %{},
                 action: :fulfill,
                 domain: NewYou.Audit,
                 authorize?: false
               ) do
          {:ok, record}
        end

      {:ok, _record} ->
        {:error, :evidence_obligation_integrity_mismatch}

      {:error, error} ->
        {:error, error}
    end
  end

  defp materialize_or_replay(%NewYou.Audit.EvidenceObligation{state: :fulfilled} = obligation) do
    case NewYou.Audit.get_evidence_record_by_obligation(obligation.id, authorize?: false) do
      {:ok, %NewYou.Audit.EvidenceRecord{} = record} -> {:ok, record}
      _ -> {:error, :evidence_obligation_integrity_mismatch}
    end
  end

  defp materialize_or_replay(_), do: {:error, :evidence_materialisation_unavailable}

  defp obligation_id(%{"id" => id}), do: Ecto.UUID.cast(id)
  defp obligation_id(%{id: id}), do: Ecto.UUID.cast(id)
  defp obligation_id(_), do: {:error, :evidence_materialisation_unavailable}
end
