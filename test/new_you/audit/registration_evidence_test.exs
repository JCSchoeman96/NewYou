defmodule NewYou.Audit.RegistrationEvidenceTest do
  use NewYou.DataCase, async: false

  @terms_id "NEWYOU-TERMS-EN-DEV-2026-10-27-001"
  @privacy_id "NEWYOU-PRIVACY-EN-DEV-2026-10-27-001"

  setup do
    previous_keys = Application.get_env(:new_you, :identity_registration_binding_keys)
    previous_token_secret = Application.get_env(:new_you, :identity_token_signing_secret)

    Application.put_env(:new_you, :identity_registration_binding_keys, %{
      active_version: "test-v1",
      keys: %{"test-v1" => :crypto.strong_rand_bytes(32)}
    })

    Application.put_env(:new_you, :identity_token_signing_secret, :crypto.strong_rand_bytes(32))

    on_exit(fn ->
      restore_app_env(:identity_registration_binding_keys, previous_keys)
      restore_app_env(:identity_token_signing_secret, previous_token_secret)
    end)

    :ok
  end

  test "successful registration creates one open E2 obligation and its Audit job" do
    request = valid_request()

    assert {:ok, %{status: :verification_pending, account_id: account_id}} =
             NewYou.Identity.register(request)

    assert is_binary(account_id)

    account =
      Ash.get!(NewYou.Identity.Account, account_id, domain: NewYou.Identity, authorize?: false)

    assert NewYou.Identity.PMR.valid?(account.pmr)

    [obligation] = audit_records("EvidenceObligation")
    assert obligation.evidence_type == :account_registration_pmr_assignment
    assert obligation.source_operation_id == request.operation_id
    assert obligation.state == :open

    [job] = scheduled_audit_jobs()
    assert job.queue == "audit"

    assert job.args == %{
             "primary_key" => %{"id" => obligation.id},
             "metadata" => %{},
             "action_arguments" => %{},
             "tenant" => nil
           }
  end

  test "an identical registration retry does not multiply the obligation or schedule" do
    request = valid_request()

    assert {:ok, %{account_id: account_id}} = NewYou.Identity.register(request)

    assert {:ok, %{account_id: ^account_id, verification_proof: nil}} =
             NewYou.Identity.register(request)

    assert length(audit_records("EvidenceObligation")) == 1
    assert length(scheduled_audit_jobs()) == 1
  end

  test "a neutral duplicate-email registration creates no additional E2 obligation or job" do
    first_request = valid_request()
    duplicate_request = %{valid_request() | email: "alice+campaign.example@EXAMPLE.COM"}

    assert {:ok, %{account_id: account_id}} = NewYou.Identity.register(first_request)
    assert is_binary(account_id)

    assert {:ok, %{account_id: nil}} = NewYou.Identity.register(duplicate_request)

    assert length(audit_records("EvidenceObligation")) == 1
    assert length(scheduled_audit_jobs()) == 1
  end

  test "a failed Audit schedule rolls back all registration acceptance writes" do
    reject_inserts("oban_jobs", "audit_schedule_failure")

    assert {:error, :registration_unavailable} = NewYou.Identity.register(valid_request())

    assert NewYou.Identity.Account |> Ash.read!(domain: NewYou.Identity, authorize?: false) == []

    assert NewYou.Identity.RegistrationOperation
           |> Ash.read!(domain: NewYou.Identity, authorize?: false) == []

    assert audit_records("EvidenceObligation") == []
    assert row_count("tokens") == 0
    assert scheduled_audit_jobs() == []
  end

  test "a failed obligation creation rolls back all registration acceptance writes" do
    reject_inserts("evidence_obligations", "evidence_obligation_failure")

    assert {:error, :registration_unavailable} = NewYou.Identity.register(valid_request())

    assert NewYou.Identity.Account |> Ash.read!(domain: NewYou.Identity, authorize?: false) == []

    assert NewYou.Identity.RegistrationOperation
           |> Ash.read!(domain: NewYou.Identity, authorize?: false) == []

    assert audit_records("EvidenceObligation") == []
    assert row_count("tokens") == 0
    assert scheduled_audit_jobs() == []
  end

  test "a later Identity write failure rolls back the inserted Audit job" do
    reject_inserts("registration_operations", "late_identity_acceptance_failure")

    assert {:error, :registration_unavailable} = NewYou.Identity.register(valid_request())

    assert NewYou.Identity.Account |> Ash.read!(domain: NewYou.Identity, authorize?: false) == []

    assert NewYou.Identity.RegistrationOperation
           |> Ash.read!(domain: NewYou.Identity, authorize?: false) == []

    assert audit_records("EvidenceObligation") == []
    assert row_count("tokens") == 0
    assert scheduled_audit_jobs() == []
  end

  test "Audit materialisation is idempotent and leaves Identity truth unchanged" do
    request = valid_request()
    assert {:ok, %{account_id: account_id}} = NewYou.Identity.register(request)
    [obligation] = audit_records("EvidenceObligation")
    [job] = scheduled_audit_jobs()

    identity_before = identity_truth(account_id)

    worker =
      AshOban.Info.oban_trigger(NewYou.Audit.EvidenceObligation, :registration_evidence).worker

    oban_job = %Oban.Job{args: job.args, attempt: 1, max_attempts: 10}

    assert :ok = worker.perform(oban_job)
    assert :ok = worker.perform(oban_job)

    fulfilled =
      Ash.get!(NewYou.Audit.EvidenceObligation, obligation.id,
        domain: NewYou.Audit,
        authorize?: false
      )

    assert fulfilled.state == :fulfilled
    assert length(audit_records("EvidenceRecord")) == 1
    assert identity_truth(account_id) == identity_before

    assert {:error, _} =
             NewYou.Audit.create_evidence_record(%{obligation_id: obligation.id},
               authorize?: false
             )

    refute Ash.Resource.Info.action(NewYou.Audit.EvidenceRecord, :update)
    refute Ash.Resource.Info.action(NewYou.Audit.EvidenceRecord, :destroy)

    assert {:error, _} =
             Ash.update(fulfilled, %{},
               action: :fulfill,
               domain: NewYou.Audit,
               authorize?: false
             )
  end

  test "PostgreSQL rejects lifecycle values outside the EvidenceObligation contract" do
    assert {:ok, _} = NewYou.Identity.register(valid_request())
    [obligation] = audit_records("EvidenceObligation")

    assert_raise Postgrex.Error, fn ->
      Repo.query!("UPDATE evidence_obligations SET state = 'invalid' WHERE id = $1", [
        Ecto.UUID.dump!(obligation.id)
      ])
    end

    refreshed =
      Ash.get!(NewYou.Audit.EvidenceObligation, obligation.id,
        domain: NewYou.Audit,
        authorize?: false
      )

    assert refreshed.state == :open
  end

  test "PostgreSQL enforces one obligation per source operation and the EvidenceRecord foreign key" do
    request = valid_request()
    assert {:ok, _} = NewYou.Identity.register(request)
    [obligation] = audit_records("EvidenceObligation")

    assert {:error, _} =
             NewYou.Audit.establish_registration_obligation(
               %{
                 source_operation_id: request.operation_id,
                 source_occurred_at: DateTime.utc_now()
               },
               authorize?: false
             )

    assert {:error, _} =
             NewYou.Audit.create_evidence_record(
               %{obligation_id: Ecto.UUID.generate()},
               authorize?: false
             )

    assert length(audit_records("EvidenceObligation")) == 1
    assert audit_records("EvidenceRecord") == []
    assert length(scheduled_audit_jobs()) == 1
    assert is_binary(obligation.id)
  end

  defp valid_request do
    %{
      operation_id: Ecto.UUID.generate(),
      first_name: "Alice",
      surname: "Example",
      email: "alice+campaign.example@example.com",
      password: Base.url_encode64(:crypto.strong_rand_bytes(32), padding: false),
      preferred_language: :en,
      confirmed_age_18?: true,
      terms_version_id: @terms_id,
      privacy_version_id: @privacy_id
    }
  end

  defp audit_records(resource_name) do
    resource = Module.concat([NewYou, Audit, resource_name])

    if Code.ensure_loaded?(resource) do
      Ash.read!(resource, domain: Module.concat([NewYou, Audit]), authorize?: false)
    else
      []
    end
  end

  defp scheduled_audit_jobs do
    case Repo.query!("SELECT to_regclass('public.oban_jobs')") do
      %{rows: [[nil]]} ->
        []

      %{rows: [[_table]]} ->
        %{rows: rows} =
          Repo.query!(
            "SELECT queue, args FROM public.oban_jobs WHERE queue = $1 ORDER BY id",
            ["audit"]
          )

        Enum.map(rows, fn [queue, args] -> %{queue: queue, args: args} end)
    end
  end

  defp identity_truth(account_id) do
    account =
      Ash.get!(NewYou.Identity.Account, account_id, domain: NewYou.Identity, authorize?: false)

    operations =
      Ash.read!(NewYou.Identity.RegistrationOperation, domain: NewYou.Identity, authorize?: false)

    %{account: account, operations: operations, token_count: row_count("tokens")}
  end

  defp row_count(table) do
    %{rows: [[count]]} = Repo.query!("SELECT count(*) FROM #{table}")
    count
  end

  defp reject_inserts(table, name) do
    function_name = "#{name}_function"
    trigger_name = name

    Repo.query!("""
    CREATE FUNCTION #{function_name}() RETURNS trigger
    LANGUAGE plpgsql AS $$
    BEGIN
      RAISE EXCEPTION 'forced #{name}' USING ERRCODE = '23514';
    END;
    $$
    """)

    Repo.query!("""
    CREATE TRIGGER #{trigger_name}
    BEFORE INSERT ON #{table}
    FOR EACH ROW EXECUTE FUNCTION #{function_name}()
    """)
  end

  defp restore_app_env(key, nil), do: Application.delete_env(:new_you, key)
  defp restore_app_env(key, value), do: Application.put_env(:new_you, key, value)
end
