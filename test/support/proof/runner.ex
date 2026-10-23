Code.require_file("../../proof/self_test.exs", __DIR__)

defmodule NewYou.Proof.Runner do
  @moduledoc """
  Deterministic P8-04 proof runner. It emits infrastructure evidence while
  keeping future TB-001 business families explicitly unavailable.
  """

  alias NewYou.Proof.{Catalog, Result, SelfTest}

  @modes %{
    "harness_self_test" => :harness_self_test,
    "tb001" => :tb001,
    "diagnostic" => :diagnostic
  }

  @spec parse_args([String.t()]) ::
          {:ok, %{mode: atom(), output: String.t(), case_ids: [String.t()]}}
          | {:error, atom()}
  def parse_args(args) when is_list(args) do
    case OptionParser.parse(args,
           strict: [mode: :string, output: :string, case: :keep]
         ) do
      {options, [], []} -> normalize_options(options)
      _ -> {:error, :invalid_arguments}
    end
  rescue
    _ -> {:error, :invalid_arguments}
  end

  def parse_args(_args), do: {:error, :invalid_arguments}

  @spec run(Result.mode(), keyword()) :: map()
  def run(mode, opts \\ [])

  def run(mode, opts) when mode in [:harness_self_test, :tb001, :diagnostic] do
    root = Keyword.get(opts, :root, File.cwd!())
    before = capture_metadata(root)

    {results, cleanup} =
      case mode do
        :tb001 -> {missing_business_results(), clean_cleanup()}
        :harness_self_test -> run_self_test(self_test_case_ids(), root)
        :diagnostic -> run_self_test(diagnostic_case_ids(opts), root)
      end

    after_run = capture_source(root)
    metadata = combine_metadata(before, after_run)
    build_result(mode, results, cleanup, metadata)
  rescue
    _error ->
      failure_envelope(mode, Keyword.get(opts, :root, File.cwd!()), "runner.failure")
  catch
    _kind, _reason ->
      failure_envelope(mode, Keyword.get(opts, :root, File.cwd!()), "runner.failure")
  end

  def run(_mode, _opts), do: failure_envelope(:diagnostic, File.cwd!(), "runner.invalid_mode")

  @spec run_cli([String.t()]) :: 0 | 1 | 2
  def run_cli(args) do
    with {:ok, %{mode: mode, output: output, case_ids: case_ids}} <- parse_args(args),
         true <- Mix.env() == :test do
      result = run(mode, case_ids: case_ids)

      case Result.validate(result, mode: mode) do
        :ok ->
          publish_result(output, result)

        {:error, _reasons} ->
          IO.puts(:stderr, "proof result validation failure")
          2
      end
    else
      false ->
        IO.puts(:stderr, "proof runner requires TEST environment")
        2

      {:error, :output_required} ->
        IO.puts(:stderr, "proof output path required")
        2

      {:error, :invalid_mode} ->
        IO.puts(:stderr, "proof mode invalid")
        2

      {:error, :unknown_case} ->
        IO.puts(:stderr, "proof case unknown")
        2

      {:error, _reason} ->
        IO.puts(:stderr, "proof arguments invalid")
        2
    end
  rescue
    _error ->
      IO.puts(:stderr, "proof runner failure")
      2
  catch
    _kind, _reason ->
      IO.puts(:stderr, "proof runner failure")
      2
  end

  defp normalize_options(options) do
    modes = Keyword.get_values(options, :mode)
    outputs = Keyword.get_values(options, :output)
    case_ids = Keyword.get_values(options, :case)

    cond do
      length(modes) != 1 ->
        {:error, :invalid_mode}

      length(outputs) != 1 or not valid_output?(List.first(outputs)) ->
        {:error, :output_required}

      true ->
        with {:ok, mode} <- Map.fetch(@modes, List.first(modes)),
             :ok <- validate_case_selection(mode, case_ids) do
          {:ok, %{mode: mode, output: List.first(outputs), case_ids: case_ids}}
        else
          :error -> {:error, :invalid_mode}
          {:error, reason} -> {:error, reason}
        end
    end
  end

  defp publish_result(output, result) do
    case Result.write_atomic(output, result) do
      :ok ->
        IO.puts("proof result: #{result["overall_verdict"]} (#{result["exit_code"]})")
        result["exit_code"]

      {:error, :output_failure} ->
        IO.puts(:stderr, "proof output failure")
        2
    end
  end

  defp validate_case_selection(:diagnostic, case_ids) do
    required = MapSet.new(Enum.map(Catalog.required().self_test.cases, & &1.case_id))

    cond do
      length(case_ids) != length(Enum.uniq(case_ids)) -> {:error, :duplicate_case}
      Enum.any?(case_ids, &(not MapSet.member?(required, &1))) -> {:error, :unknown_case}
      true -> :ok
    end
  end

  defp validate_case_selection(_mode, []), do: :ok
  defp validate_case_selection(_mode, _case_ids), do: {:error, :invalid_arguments}

  defp valid_output?(path),
    do: is_binary(path) and byte_size(path) in 1..1_024 and String.trim(path) != ""

  defp self_test_case_ids, do: Enum.map(Catalog.required().self_test.cases, & &1.case_id)

  defp run_self_test(case_ids, root) do
    {cases, cleanup} = SelfTest.run(case_ids, root: root)

    passed? =
      cases != [] and length(cases) == length(case_ids) and
        Enum.all?(cases, &(&1["verdict"] == "PASS"))

    entry = %{
      "coverage_id" => "harness",
      "manifest_sha256" => Catalog.required().self_test.digest,
      "required_case_ids" => case_ids,
      "status" => if(passed?, do: "completed", else: "error"),
      "verdict" => if(passed?, do: "PASS", else: "FAIL"),
      "reason_codes" => if(passed?, do: [], else: ["self_test.incomplete"]),
      "cases" => cases
    }

    {[entry], cleanup}
  end

  defp diagnostic_case_ids(opts) do
    case Keyword.get(opts, :case_ids, []) do
      [] -> self_test_case_ids()
      case_ids -> case_ids
    end
  end

  defp capture_metadata(root) do
    source = Result.capture_source(root)
    runtime = Result.capture_runtime()

    dependencies =
      case Result.capture_dependencies(root) do
        {:ok, entries} -> entries
        {:error, _reason} -> []
      end

    postgresql =
      case Result.capture_postgresql() do
        {:ok, version} -> version
        {:error, _reason} -> nil
      end

    %{source: source, runtime: runtime, dependencies: dependencies, postgresql: postgresql}
  end

  defp capture_source(root), do: Result.capture_source(root)

  defp combine_metadata(before, after_source) do
    source_before = before.source
    runtime = before.runtime
    dependencies = before.dependencies

    %{
      complete:
        metadata_sources_complete?(source_before, after_source) and
          metadata_dependencies_complete?(dependencies) and
          metadata_postgresql_complete?(before.postgresql) and metadata_runtime_complete?(runtime),
      source_before: source_before,
      source_after: after_source,
      runtime: runtime,
      dependencies: dependencies,
      postgresql: before.postgresql,
      mix_env: if(Mix.env() == :test, do: "test", else: nil)
    }
  end

  defp metadata_sources_complete?(before, after_source),
    do: complete_source?(before) and complete_source?(after_source)

  defp metadata_dependencies_complete?(dependencies),
    do: dependencies != [] and dependency_entries_complete?(dependencies)

  defp metadata_postgresql_complete?(version),
    do: is_binary(version) and valid_version?(version)

  defp metadata_runtime_complete?(runtime),
    do: Enum.all?(Map.values(runtime), &(is_binary(&1) and &1 != "")) and Mix.env() == :test

  defp complete_source?(source),
    do: is_binary(source.head) and is_boolean(source.clean) and is_binary(source.lock_sha256)

  defp dependency_entries_complete?(entries) do
    Enum.all?(entries, fn entry ->
      is_binary(entry.name) and is_binary(entry.source) and
        (not entry.runtime_required or is_binary(entry.loaded_version))
    end)
  rescue
    _ -> false
  end

  defp valid_version?(version), do: Regex.match?(~r/^\d+(\.\d+)+/, version)

  defp build_result(mode, results, cleanup, metadata) do
    source_changed? =
      metadata.source_before.head != metadata.source_after.head or
        metadata.source_before.lock_sha256 != metadata.source_after.lock_sha256

    dirty_full? =
      mode == :tb001 and
        (metadata.source_before.clean != true or metadata.source_after.clean != true)

    cleanup_ok? = cleanup["verdict"] == "PASS"
    selected_pass? = results != [] and Enum.all?(results, &(&1["verdict"] == "PASS"))

    {verdict, exit_code} =
      overall_verdict(
        mode,
        metadata.complete,
        cleanup_ok?,
        source_changed?,
        dirty_full?,
        selected_pass?
      )

    reason_codes =
      result_reasons(
        metadata.complete,
        cleanup_ok?,
        source_changed?,
        dirty_full?,
        selected_pass?,
        mode
      )

    result_document(mode, results, cleanup, metadata, verdict, exit_code, reason_codes)
  end

  defp overall_verdict(
         mode,
         metadata_complete?,
         cleanup_ok?,
         source_changed?,
         dirty_full?,
         selected_pass?
       ) do
    cond do
      not metadata_complete? or not cleanup_ok? or source_changed? or dirty_full? -> {"FAIL", 2}
      not selected_pass? or mode == :tb001 -> {"FAIL", 1}
      true -> {"PASS", 0}
    end
  end

  defp result_reasons(
         metadata_complete?,
         cleanup_ok?,
         source_changed?,
         dirty_full?,
         selected_pass?,
         mode
       ) do
    []
    |> add_reason(not metadata_complete?, "metadata.unavailable")
    |> add_reason(source_changed?, "source.changed")
    |> add_reason(dirty_full?, "source.dirty")
    |> add_reason(not cleanup_ok?, "cleanup.failed")
    |> add_reason(not selected_pass? or mode == :tb001, "coverage.incomplete")
  end

  defp result_document(mode, results, cleanup, metadata, verdict, exit_code, reason_codes) do
    %{
      "schema_version" => "1.0.0",
      "run_id" => run_id(),
      "mode" => Atom.to_string(mode),
      "contract" => "TB-001/v0.1.2",
      "metadata_complete" => metadata.complete,
      "git" => %{
        "head_before" => metadata.source_before.head,
        "head_after" => metadata.source_after.head,
        "clean_before" => metadata.source_before.clean,
        "clean_after" => metadata.source_after.clean,
        "lock_sha256_before" => metadata.source_before.lock_sha256,
        "lock_sha256_after" => metadata.source_after.lock_sha256
      },
      "runtime" => %{
        "elixir" => metadata.runtime.elixir,
        "otp" => metadata.runtime.otp,
        "erts" => metadata.runtime.erts,
        "postgresql" => metadata.postgresql,
        "mix_env" => metadata.mix_env
      },
      "dependencies" => metadata.dependencies,
      "coverage_inventory" => Catalog.coverage_inventory(),
      "results" => results,
      "cleanup" => cleanup,
      "overall_verdict" => verdict,
      "exit_code" => exit_code,
      "reason_codes" => reason_codes
    }
  end

  defp missing_business_results do
    Enum.map(Catalog.coverage_inventory(), fn coverage_id ->
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
  end

  defp clean_cleanup do
    %{
      "verdict" => "PASS",
      "workers_stopped" => true,
      "connections_released" => true,
      "locks_released" => true,
      "reason_codes" => []
    }
  end

  defp failure_envelope(mode, root, reason) do
    metadata =
      try do
        before = Result.capture_source(root)
        after_source = Result.capture_source(root)

        %{
          complete: false,
          source_before: before,
          source_after: after_source,
          runtime: Result.capture_runtime(),
          dependencies: [],
          postgresql: nil,
          mix_env: if(Mix.env() == :test, do: "test", else: nil)
        }
      rescue
        _ ->
          empty_metadata()
      end

    failure_results =
      if mode == :tb001,
        do: missing_business_results(),
        else: []

    build_result(mode, failure_results, failure_cleanup(), metadata)
    |> Map.put("reason_codes", [reason, "metadata.unavailable"])
    |> Map.put("exit_code", 2)
  rescue
    _ -> %{}
  end

  defp empty_metadata do
    source = %{head: nil, clean: nil, lock_sha256: nil}

    %{
      complete: false,
      source_before: source,
      source_after: source,
      runtime: %{elixir: nil, otp: nil, erts: nil},
      dependencies: [],
      postgresql: nil,
      mix_env: nil
    }
  end

  defp failure_cleanup do
    %{
      "verdict" => "FAIL",
      "workers_stopped" => false,
      "connections_released" => false,
      "locks_released" => false,
      "reason_codes" => ["cleanup.unconfirmed"]
    }
  end

  defp add_reason(reasons, true, reason), do: reasons ++ [reason]
  defp add_reason(reasons, false, _reason), do: reasons

  defp run_id do
    "p8-04-" <> Base.encode16(:crypto.strong_rand_bytes(12), case: :lower)
  end
end
