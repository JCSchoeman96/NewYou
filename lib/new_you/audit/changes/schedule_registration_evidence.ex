defmodule NewYou.Audit.Changes.ScheduleRegistrationEvidence do
  use Ash.Resource.Change

  @impl true
  def change(changeset, _opts, context) do
    Ash.Changeset.after_action(changeset, fn changeset, result ->
      trigger = AshOban.Info.oban_trigger(changeset.resource, :registration_evidence)

      job =
        result
        |> AshOban.build_trigger(
          trigger,
          context
          |> Ash.Context.to_opts()
          |> Keyword.take([:actor, :tenant])
          |> Keyword.update(:tenant, nil, &Ash.ToTenant.to_tenant(&1, changeset.resource))
        )

      # The owner action already opened the source transaction, so Oban must not retry a nested transaction error.
      try do
        case Oban.insert(job, retry: false) do
          {:ok, _job} -> {:ok, result}
          {:error, error} -> {:error, error}
        end
      rescue
        error -> {:error, error}
      end
    end)
  end
end
