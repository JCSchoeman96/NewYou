unless Code.ensure_loaded?(NewYou.Proof.ProviderFixtures) do
  Code.require_file("../../proof/fixtures/provider_fixtures.exs", __DIR__)
end

defmodule NewYou.Proof.ProviderTest do
  use ExUnit.Case, async: false

  alias NewYou.Proof.{Provider, ProviderFixtures, Scenario}

  @operation "synthetic-op-1"
  @key NewYou.Proof.ProviderFixtures.key()

  test "scripts provide each bounded provider outcome without changing its meaning" do
    steps = [
      {:no_call, :not_invoked},
      {:rejection, :rejected_before_submission},
      {:accepted, :accepted},
      {:delivered, :delivered},
      {:failed, :bounced_or_failed},
      {:uncertain, :unknown},
      {:confirmed_absent, :confirmed_no_operation},
      {:reconciled_rejection, :reconciliation_rejected},
      {:reconciled_acceptance, :reconciliation_accepted},
      {:reconciled_delivery, :reconciliation_delivered},
      {:reconciled_failure, :reconciliation_failed}
    ]

    scenario = Scenario.start()
    assert :ok = Provider.configure(scenario, %{@operation => steps})

    Enum.each(steps, fn {step, outcome} ->
      assert {:ok, %{operation_ref: @operation, step: ^step, outcome: ^outcome}} =
               Provider.next(scenario, @operation, step)
    end)

    assert {:error, :script_exhausted} = Provider.next(scenario, @operation, :uncertain)
    assert :ok = Scenario.stop(scenario)
  end

  test "backlog remains unreleased until the owner releases it" do
    scenario = Scenario.start()
    assert :ok = Provider.configure(scenario, %{@operation => [{:queue, :backlog}]})

    assert {:ok, %{outcome: :backlog, released: false}} =
             Provider.next(scenario, @operation, :queue)

    assert {:ok, %{outcome: :backlog, released: true}} =
             Provider.release_backlog(scenario, @operation)

    assert :ok = Scenario.stop(scenario)
  end

  test "each backlog step needs its own explicit release" do
    scenario = Scenario.start()

    assert :ok =
             Provider.configure(scenario, %{
               @operation => [{:first_queue, :backlog}, {:second_queue, :backlog}]
             })

    assert {:ok, %{step: :first_queue, released: false}} =
             Provider.next(scenario, @operation, :first_queue)

    assert {:ok, %{step: :first_queue, released: true}} =
             Provider.release_backlog(scenario, @operation)

    assert {:ok, %{step: :second_queue, released: false}} =
             Provider.next(scenario, @operation, :second_queue)

    assert {:ok, %{step: :second_queue, released: true}} =
             Provider.release_backlog(scenario, @operation)

    assert :ok = Scenario.stop(scenario)
  end

  test "duplicate and reordered observations retain event and operation identity" do
    scenario = Scenario.start()

    steps = [
      {:event_b, %{outcome: :delivered, event_ref: "event-b", logical_order: 2}},
      {:event_a, %{outcome: :accepted, event_ref: "event-a", logical_order: 1}},
      {:event_a_again, %{outcome: :accepted, event_ref: "event-a", logical_order: 1}}
    ]

    assert :ok = Provider.configure(scenario, %{@operation => steps})

    for {step, event_ref, order} <- [
          {:event_b, "event-b", 2},
          {:event_a, "event-a", 1},
          {:event_a_again, "event-a", 1}
        ] do
      assert {:ok, %{operation_ref: @operation, event_ref: ^event_ref, logical_order: ^order}} =
               Provider.next(scenario, @operation, step)
    end

    assert :ok = Scenario.stop(scenario)
  end

  test "unknown scripts and mismatched steps fail without consuming another script" do
    scenario = Scenario.start()
    assert :ok = Provider.configure(scenario, %{@operation => [{:first, :accepted}]})
    assert {:error, :unknown_script} = Provider.next(scenario, "synthetic-op-2", :first)
    assert {:error, :script_step_mismatch} = Provider.next(scenario, @operation, :wrong)
    assert {:ok, %{outcome: :accepted}} = Provider.next(scenario, @operation, :first)
    assert :ok = Scenario.stop(scenario)
  end

  test "scripts are isolated between scenarios" do
    first = Scenario.start()
    second = Scenario.start()
    assert :ok = Provider.configure(first, %{@operation => [{:first, :accepted}]})
    assert {:error, :unknown_script} = Provider.next(second, @operation, :first)
    assert {:ok, %{outcome: :accepted}} = Provider.next(first, @operation, :first)
    assert :ok = Scenario.stop(first)
    assert :ok = Scenario.stop(second)
  end

  test "concurrent workers consume a provider step at most once" do
    scenario = Scenario.start()
    assert :ok = Provider.configure(scenario, %{@operation => [{:single, :accepted}]})
    parent = self()

    workers =
      for _ <- 1..2 do
        Scenario.spawn(scenario, :provider_worker, fn ->
          send(parent, {:provider_result, Provider.next(scenario, @operation, :single)})
        end)
      end

    results =
      for _ <- 1..2,
          do:
            (
              assert_receive({:provider_result, result})
              result
            )

    assert Enum.count(results, &match?({:ok, %{outcome: :accepted}}, &1)) == 1
    assert Enum.count(results, &(&1 == {:error, :script_exhausted})) == 1

    Enum.each(workers, fn {pid, monitor} ->
      assert_receive {:DOWN, ^monitor, :process, ^pid, :normal}
    end)

    assert :ok = Scenario.stop(scenario)
  end

  test "fixture authentication verifies HMAC and operation reference" do
    body = "synthetic reconciliation payload"
    valid = ProviderFixtures.sign("#{@operation}|#{body}", @key)

    assert {:ok, :authenticated} =
             Provider.authenticate_fixture({@operation, @operation, body}, valid, @key)

    assert {:error, :invalid_signature} =
             Provider.authenticate_fixture({@operation, @operation, body}, <<0::256>>, @key)

    wrong_operation = ProviderFixtures.sign("other-operation|#{body}", @key)

    assert {:error, :operation_reference_mismatch} =
             Provider.authenticate_fixture(
               {@operation, "other-operation", body},
               wrong_operation,
               @key
             )
  end

  test "fixture authentication rejects a trusted boolean bypass" do
    assert {:error, :invalid_fixture} =
             Provider.authenticate_fixture(%{authenticated: true}, <<>>, @key)
  end

  test "fixture authentication rejects oversized payloads and keys before hashing" do
    oversized_body = String.duplicate("x", 4_097)
    oversized_key = String.duplicate("k", 257)
    signature = ProviderFixtures.sign("#{@operation}|small", @key)

    assert {:error, :invalid_fixture} =
             Provider.authenticate_fixture(
               {@operation, @operation, oversized_body},
               signature,
               @key
             )

    assert {:error, :invalid_fixture} =
             Provider.authenticate_fixture(
               {@operation, @operation, "small"},
               signature,
               oversized_key
             )
  end

  test "script length and identifiers are bounded and diagnostics redact inputs" do
    scenario = Scenario.start()
    secret = "synthetic-secret-canary"
    too_long = List.duplicate({:step, :accepted}, 65)
    assert {:error, :invalid_script} = Provider.configure(scenario, %{secret => too_long})

    assert {:error, :invalid_script} =
             Provider.configure(scenario, %{make_ref() => [{:step, :accepted}]})

    assert {:error, :invalid_script} =
             Provider.configure(scenario, %{
               @operation => [
                 {:step,
                  %{outcome: :delivered, event_ref: "person@example.test", logical_order: 1}}
               ]
             })

    refute inspect(Scenario.stop(scenario)) =~ secret
  end
end
