defmodule NewYou.Proof.FullCatalog do
  @moduledoc false

  alias NewYou.Proof.{Catalog, SelfTest}

  @spec execute(map(), [Catalog.registration()]) ::
          {:ok, [map()], map()} | {:error, [atom()]}
  def execute(manifests, registrations)
      when is_map(manifests) and is_list(registrations) do
    with :ok <- Catalog.validate_compiled_registrations(manifests, registrations),
         {:ok, registration_index} <- registration_index(registrations) do
      {observed_cases, cleanup} = do_execute(manifests, registration_index)
      {:ok, observed_cases, cleanup}
    end
  end

  defp do_execute(manifests, registration_index) do
    {observations, cleanup, _stopped?} =
      Enum.reduce(Catalog.coverage_inventory(), {[], SelfTest.initial_cleanup_state(), false}, fn
        _coverage_id, {observations, cleanup, true} ->
          {observations, cleanup, true}

        coverage_id, {observations, cleanup, false} ->
          case Map.get(manifests, coverage_id) do
            manifest when is_map(manifest) ->
              execute_family(coverage_id, manifest, registration_index, observations, cleanup)

            _ ->
              {observations, cleanup, false}
          end
      end)

    {Enum.reverse(observations), SelfTest.finalize_cleanup(cleanup)}
  end

  defp registration_index(registrations) do
    Enum.reduce_while(registrations, {%{}, []}, fn registration, {index, _errors} ->
      key = {registration.coverage_id, registration.case_id}

      if Map.has_key?(index, key) do
        {:halt, {:error, [:duplicate_case]}}
      else
        {:cont, {Map.put(index, key, registration.callback), []}}
      end
    end)
    |> case do
      {:error, reasons} -> {:error, reasons}
      {index, _} -> {:ok, index}
    end
  end

  defp execute_family(coverage_id, manifest, registration_index, observations, cleanup) do
    cases = Map.get(manifest, :cases, [])

    Enum.reduce(cases, {observations, cleanup, false}, fn case_manifest, acc ->
      execute_family_case(coverage_id, manifest, case_manifest, registration_index, acc)
    end)
  end

  defp execute_family_case(
         _coverage_id,
         _family_manifest,
         _case_manifest,
         _registration_index,
         {observations, cleanup, true}
       ) do
    {observations, cleanup, true}
  end

  defp execute_family_case(
         coverage_id,
         family_manifest,
         case_manifest,
         registration_index,
         {observations, cleanup, false}
       ) do
    manifest = case_manifest(coverage_id, family_manifest, case_manifest)

    case Map.fetch(registration_index, {coverage_id, manifest.case_id}) do
      {:ok, callback} ->
        {case_result, case_cleanup} = SelfTest.execute_registered_case(manifest, callback)
        observation = observation_from_case(coverage_id, case_result)

        {
          [observation | observations],
          SelfTest.merge_cleanup_state(cleanup, case_cleanup),
          case_result["verdict"] != "PASS"
        }

      :error ->
        {observations, cleanup, true}
    end
  end

  defp case_manifest(coverage_id, family_manifest, case_manifest) when is_map(case_manifest) do
    timeout_ms = Map.get(case_manifest, :timeout_ms, 10_000)

    Map.merge(case_manifest, %{
      coverage_id: coverage_id,
      version: Map.get(family_manifest, :version, "1.0.0"),
      timeout_ms: timeout_ms,
      timeout_override_reason: Map.get(case_manifest, :timeout_override_reason),
      expected:
        Map.get(case_manifest, :expected) ||
          "the registered proof callback completes under runner-owned assertions"
    })
  end

  defp observation_from_case(coverage_id, case_result) when is_map(case_result) do
    %{
      "coverage_id" => coverage_id,
      "case_id" => case_result["case_id"],
      "invariant_id" => case_result["invariant_id"],
      "status" => case_result["status"],
      "verdict" => case_result["verdict"],
      "assertion_ids" => case_result["assertion_ids"],
      "assertions_executed" => case_result["assertions_executed"],
      "observations" => case_result["observations"],
      "reason_codes" => case_result["reason_codes"],
      "duration_ms" => case_result["duration_ms"]
    }
  end
end
