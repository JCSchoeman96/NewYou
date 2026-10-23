defmodule NewYou.Proof.ResultTest do
  use ExUnit.Case, async: true

  alias NewYou.Proof.{Catalog, Result, Scenario}

  test "expect records the actual assertion and returns the observation" do
    scenario = Scenario.start()
    :ok = Scenario.require_assertions(scenario, "case.one", ["case.one.verified"])

    assert :observed =
             Result.expect!(scenario, "case.one", "case.one.verified", :observed, :observed)

    assert %{"case.one" => %{assertion_ids: ["case.one.verified"], failed_ids: [], count: 1}} =
             Scenario.assertion_snapshot(scenario)

    assert :ok = Scenario.stop(scenario)
  end

  test "mismatch and duplicate or unknown assertion ids fail closed" do
    scenario = Scenario.start()
    :ok = Scenario.require_assertions(scenario, "case.one", ["case.one.verified"])

    assert_raise RuntimeError, "proof assertion failed", fn ->
      Result.expect!(scenario, "case.one", "case.one.verified", :wrong, :expected)
    end

    assert_raise RuntimeError, "proof assertion failed", fn ->
      Result.expect!(scenario, "case.one", "case.one.verified", :expected, :expected)
    end

    assert_raise RuntimeError, "proof assertion failed", fn ->
      Result.expect!(scenario, "case.one", "case.one.unknown", true, true)
    end

    assert {:error, _} = Scenario.stop(scenario)
  end

  test "result verdict and exit code are derived from cleanup and actual assertions" do
    result =
      Result.verdict(
        mode: :harness_self_test,
        metadata_complete: true,
        checks: [:pass],
        cleanup: :pass
      )

    assert result == %{overall_verdict: "PASS", exit_code: 0}

    assert Result.verdict(
             mode: :harness_self_test,
             metadata_complete: false,
             checks: [:pass],
             cleanup: :pass
           ) ==
             %{overall_verdict: "FAIL", exit_code: 2}

    assert Result.verdict(mode: :tb001, metadata_complete: true, checks: [:fail], cleanup: :pass) ==
             %{overall_verdict: "FAIL", exit_code: 1}
  end

  test "schema and cross-field validation reject caller counts and inconsistent pass" do
    malformed = %{"overall_verdict" => "PASS", "exit_code" => 0, "assertions_executed" => 100}
    assert {:error, _} = Result.validate(malformed, mode: :harness_self_test)
  end

  test "source capture uses the current checkout and lockfile" do
    source = Result.capture_source()
    assert source.head == System.cmd("git", ["rev-parse", "HEAD"]) |> elem(0) |> String.trim()
    assert is_boolean(source.clean)

    assert source.lock_sha256 ==
             :crypto.hash(:sha256, File.read!("mix.lock")) |> Base.encode16(case: :lower)
  end

  test "PostgreSQL metadata comes from the TEST connection and checks its role" do
    assert {:ok, version} = Result.capture_postgresql()
    assert is_binary(version)
    assert String.match?(version, ~r/^\d+(\.\d+)+/)
  end

  test "atomic publication refuses an existing target and preserves its bytes" do
    directory = Path.join(System.tmp_dir!(), "proof-result-#{System.unique_integer([:positive])}")
    File.mkdir!(directory)
    target = Path.join(directory, "result.json")
    File.write!(target, "canary-existing-artifact")

    assert {:error, :output_failure} = Result.write_atomic(target, %{safe: "result"})
    assert File.read!(target) == "canary-existing-artifact"

    File.rm!(target)
    assert :ok = Result.write_atomic(target, %{safe: "result"})
    assert File.read!(target) == "{\"safe\":\"result\"}"
    assert Bitwise.band(File.stat!(target).mode, 0o777) == 0o600

    File.rm_rf!(directory)
  end

  test "metadata and source changes cannot claim a complete result" do
    assert {:error, reasons} =
             Result.validate(%{"mode" => "tb001", "metadata_complete" => true}, mode: :tb001)

    assert :incomplete_metadata_claim in reasons or :schema_properties in reasons

    assert Result.verdict(
             mode: :diagnostic,
             metadata_complete: false,
             checks: [:pass],
             cleanup: :pass
           ) ==
             %{overall_verdict: "FAIL", exit_code: 2}
  end

  test "full results preserve the fixed coverage inventory order" do
    result = unavailable_full_result()
    reversed = %{result | "results" => Enum.reverse(result["results"])}

    assert {:error, reasons} = Result.validate(reversed, mode: :tb001)
    assert :incomplete_tb001_results in reasons
  end

  test "self-test results cannot claim a different manifest digest" do
    digest = Catalog.required().self_test.digest
    wrong_digest = String.duplicate(if(String.first(digest) == "0", do: "1", else: "0"), 64)

    assert {:error, reasons} =
             Result.validate(self_test_result(wrong_digest), mode: :harness_self_test)

    assert :invalid_self_test_manifest in reasons
  end

  test "self-test result accepts bounded natural-language expectations from its manifest" do
    digest = Catalog.required().self_test.digest

    assert :ok = Result.validate(self_test_result(digest), mode: :harness_self_test)
  end

  test "complete metadata must include every dependency from the current lockfile" do
    result = unavailable_full_result()

    result = %{
      result
      | "metadata_complete" => true,
        "git" => %{
          "head_before" => String.duplicate("a", 40),
          "head_after" => String.duplicate("a", 40),
          "clean_before" => true,
          "clean_after" => true,
          "lock_sha256_before" => String.duplicate("b", 64),
          "lock_sha256_after" => String.duplicate("b", 64)
        },
        "runtime" => %{
          "elixir" => "1.18.0",
          "otp" => "27",
          "erts" => "15.2",
          "postgresql" => "17.2",
          "mix_env" => "test"
        },
        "dependencies" => [
          %{
            "name" => "proof_not_in_lock",
            "source" => "hex",
            "locked_version" => "1.0.0",
            "loaded_version" => nil,
            "revision" => nil,
            "runtime_required" => false
          }
        ],
        "exit_code" => 1
    }

    assert {:error, reasons} = Result.validate(result, mode: :tb001)
    assert :dependency_lock_mismatch in reasons
  end

  test "database preflight rejects DEV and production identities" do
    test_config = NewYou.LocalConfig.repo(:test)

    test_server = %{
      database: "new_you_test",
      username: "new_you_test",
      role_createdb?: false
    }

    assert Result.test_connection_valid?(:test, test_config, test_server)

    dev = [hostname: "127.0.0.1", port: 55432, database: "new_you_dev", username: "new_you_dev"]
    dev_server = %{database: "new_you_dev", username: "new_you_dev", role_createdb?: false}

    refute Result.test_connection_valid?(:test, dev, dev_server)
    refute Result.test_connection_valid?(:prod, test_config, test_server)

    refute Result.test_connection_valid?(:test, test_config, %{test_server | role_createdb?: true})

    refute Result.test_connection_valid?(
             :test,
             Keyword.put(test_config, :url, "redacted"),
             test_server
           )
  end

  defp unavailable_full_result do
    inventory = Catalog.coverage_inventory()

    results =
      Enum.map(inventory, fn coverage_id ->
        %{
          "coverage_id" => coverage_id,
          "manifest_sha256" => nil,
          "required_case_ids" => [],
          "status" => "missing",
          "verdict" => "FAIL",
          "reason_codes" => ["missing.manifest"],
          "cases" => []
        }
      end)

    %{
      "schema_version" => "1.0.0",
      "run_id" => "run-test",
      "mode" => "tb001",
      "contract" => "TB-001/v0.1.2",
      "metadata_complete" => false,
      "git" => %{
        "head_before" => nil,
        "head_after" => nil,
        "clean_before" => nil,
        "clean_after" => nil,
        "lock_sha256_before" => nil,
        "lock_sha256_after" => nil
      },
      "runtime" => %{
        "elixir" => nil,
        "otp" => nil,
        "erts" => nil,
        "postgresql" => nil,
        "mix_env" => nil
      },
      "dependencies" => test_dependency_metadata(),
      "coverage_inventory" => inventory,
      "results" => results,
      "cleanup" => %{
        "verdict" => "FAIL",
        "workers_stopped" => false,
        "connections_released" => false,
        "locks_released" => false,
        "reason_codes" => ["not.run"]
      },
      "overall_verdict" => "FAIL",
      "exit_code" => 2,
      "reason_codes" => ["metadata.unavailable"]
    }
  end

  defp self_test_result(digest) do
    manifests = Catalog.required().self_test.cases

    cases =
      Enum.map(manifests, fn manifest ->
        %{
          "case_id" => manifest.case_id,
          "invariant_id" => manifest.invariant_id,
          "boundary" => manifest.boundary,
          "cut_point" => manifest.cut_point,
          "race_id" => nil,
          "status" => "completed",
          "verdict" => "PASS",
          "expected" => manifest.expected,
          "observations" => [%{"code" => "fixture.result", "value" => true}],
          "assertion_ids" => manifest.assertion_ids,
          "assertions_executed" => length(manifest.assertion_ids),
          "duration_ms" => 0,
          "timeout_ms" => manifest.timeout_ms,
          "timeout_override_reason" => nil,
          "reason_codes" => []
        }
      end)

    %{
      "schema_version" => "1.0.0",
      "run_id" => "run-test",
      "mode" => "harness_self_test",
      "contract" => "TB-001/v0.1.2",
      "metadata_complete" => false,
      "git" => %{
        "head_before" => nil,
        "head_after" => nil,
        "clean_before" => nil,
        "clean_after" => nil,
        "lock_sha256_before" => nil,
        "lock_sha256_after" => nil
      },
      "runtime" => %{
        "elixir" => nil,
        "otp" => nil,
        "erts" => nil,
        "postgresql" => nil,
        "mix_env" => nil
      },
      "dependencies" => test_dependency_metadata(),
      "coverage_inventory" => Catalog.coverage_inventory(),
      "results" => [
        %{
          "coverage_id" => "harness",
          "manifest_sha256" => digest,
          "required_case_ids" => Enum.map(cases, & &1["case_id"]),
          "status" => "completed",
          "verdict" => "PASS",
          "reason_codes" => [],
          "cases" => cases
        }
      ],
      "cleanup" => %{
        "verdict" => "PASS",
        "workers_stopped" => true,
        "connections_released" => true,
        "locks_released" => true,
        "reason_codes" => []
      },
      "overall_verdict" => "FAIL",
      "exit_code" => 2,
      "reason_codes" => ["metadata.unavailable"]
    }
  end

  defp test_dependency_metadata do
    case Result.capture_dependencies() do
      {:ok, dependencies} -> dependencies
      {:error, _reason} -> []
    end
  end
end
