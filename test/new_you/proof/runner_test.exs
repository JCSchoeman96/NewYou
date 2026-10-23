defmodule NewYou.Proof.RunnerTest do
  use ExUnit.Case, async: false

  alias NewYou.Proof.{Catalog, Runner}

  test "CLI parsing accepts the approved modes and requires an output path" do
    for {mode, expected} <- [
          {"harness_self_test", :harness_self_test},
          {"tb001", :tb001},
          {"diagnostic", :diagnostic}
        ] do
      assert {:ok, %{mode: ^expected, output: "/tmp/proof.json", case_ids: []}} =
               Runner.parse_args(["--mode", mode, "--output", "/tmp/proof.json"])
    end

    assert {:error, :output_required} = Runner.parse_args(["--mode", "tb001"])

    assert {:error, :invalid_mode} =
             Runner.parse_args(["--mode", "phase9", "--output", "/tmp/proof.json"])
  end

  test "diagnostic selection is explicit and cannot name an unapproved case" do
    case_id = hd(Catalog.required().self_test.cases).case_id

    assert {:ok, %{mode: :diagnostic, case_ids: [^case_id]}} =
             Runner.parse_args([
               "--mode",
               "diagnostic",
               "--output",
               "/tmp/proof.json",
               "--case",
               case_id
             ])

    assert {:error, :unknown_case} =
             Runner.parse_args([
               "--mode",
               "diagnostic",
               "--output",
               "/tmp/proof.json",
               "--case",
               "phase9.business"
             ])
  end

  test "full mode exposes every missing business family and browser spine" do
    result = Runner.run(:tb001)

    assert result["coverage_inventory"] == Catalog.coverage_inventory()
    assert Enum.map(result["results"], & &1["coverage_id"]) == Catalog.coverage_inventory()
    assert Enum.all?(result["results"], &(&1["status"] == "missing"))
    assert Enum.all?(result["results"], &(&1["verdict"] == "FAIL"))
    assert Enum.all?(result["results"], &("missing.manifest" in &1["reason_codes"]))
    assert result["overall_verdict"] == "FAIL"
    assert result["exit_code"] in [1, 2]
    assert "browser_spine" == List.last(Enum.map(result["results"], & &1["coverage_id"]))
  end

  test "self-test records a failed controller reply as a passing fail-closed probe" do
    {[result], cleanup} = NewYou.Proof.SelfTest.run(["scenario.lost_reply"])

    assert result["status"] == "completed"
    assert result["verdict"] == "PASS"
    assert cleanup["verdict"] == "PASS"
    assert cleanup["workers_stopped"]
    assert cleanup["connections_released"]
    assert cleanup["locks_released"]
  end

  test "self-test confirms rollback after a PostgreSQL worker is killed" do
    {[result], cleanup} = NewYou.Proof.SelfTest.run(["db.worker_crash_cleanup"])

    assert result["status"] == "completed"
    assert result["verdict"] == "PASS"
    assert cleanup["verdict"] == "PASS"
    assert cleanup["workers_stopped"]
    assert cleanup["connections_released"]
    assert cleanup["locks_released"]
  end

  test "self-test observes fresh PostgreSQL ownership after worker replacement" do
    {[result], cleanup} = NewYou.Proof.SelfTest.run(["restart.fresh_connection"])

    assert result["status"] == "completed"
    assert result["verdict"] == "PASS"
    assert cleanup["verdict"] == "PASS"
    assert cleanup["workers_stopped"]
    assert cleanup["connections_released"]
    assert cleanup["locks_released"]
  end

  test "self-test rejects callback exceptions without exposing their canary" do
    {[result], cleanup} = NewYou.Proof.SelfTest.run(["result.callback_failures"])

    assert result["status"] == "completed"
    assert result["verdict"] == "PASS"
    assert cleanup["verdict"] == "PASS"
  end

  test "self-test cannot pass a callback that records no required assertion" do
    case_id = "cut.raise.transaction.before_commit"

    {[result], cleanup} =
      NewYou.Proof.SelfTest.run([case_id], callback_overrides: %{case_id => fn -> :ok end})

    assert result["verdict"] == "FAIL"
    assert result["assertion_ids"] == []
    assert "assertion.missing" in result["reason_codes"]
    assert cleanup["verdict"] == "PASS"
  end

  @tag timeout: 240_000
  test "production exclusion evidence comes from an isolated production build" do
    {[result], cleanup} = NewYou.Proof.SelfTest.run(["production.exclusion"])

    assert %{"code" => "production.build_succeeded", "value" => true} in result["observations"]
    assert %{"code" => "production.modules_absent", "value" => true} in result["observations"]

    assert %{"code" => "production.runtime_ineffective", "value" => true} in result[
             "observations"
           ]

    assert result["verdict"] == "PASS"
    assert cleanup["verdict"] == "PASS"
  end

  test "wrong worker cut-point probe records its required assertion" do
    {[result], cleanup} = NewYou.Proof.SelfTest.run(["cut.wrong_worker"])

    assert result["verdict"] == "PASS"
    assert result["assertion_ids"] == ["cut.wrong_worker.verified"]
    assert result["assertions_executed"] == 1
    assert cleanup["verdict"] == "PASS"
  end

  test "cleanup aggregation confirms the runner controller stopped after a simple probe" do
    {[result], cleanup} = NewYou.Proof.SelfTest.run(["provider.authentication_fixtures"])

    assert result["verdict"] == "PASS"
    assert cleanup["workers_stopped"]
    assert cleanup["verdict"] == "PASS"
  end
end
