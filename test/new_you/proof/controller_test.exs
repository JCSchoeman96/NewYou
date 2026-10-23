defmodule NewYou.Proof.ControllerTest do
  use ExUnit.Case, async: false

  alias NewYou.Proof.{Barrier, CutPoints, Scenario}

  @cut_points [
    :"transaction.before_commit",
    :"transaction.after_commit",
    :"scheduling.before_enqueue",
    :"scheduling.after_enqueue",
    :"provider.before_invoke",
    :"provider.after_invoke_before_persist",
    :"evidence.before_materialize",
    :"evidence.after_materialize_before_commit"
  ]

  test "every cut point raises once for its matching worker" do
    assert CutPoints.names() == Enum.map(@cut_points, &Atom.to_string/1)

    Enum.each(@cut_points, fn point ->
      scenario = Scenario.start()
      parent = self()

      assert :ok = CutPoints.arm(scenario, Atom.to_string(point), :worker, :raise)

      {pid, monitor} =
        Scenario.spawn(scenario, :worker, fn ->
          result =
            try do
              CutPoints.hit(scenario, point, :worker)
              :continued
            rescue
              error in RuntimeError -> error.message
            end

          send(parent, {:result, self(), result})
        end)

      expected_message = "proof cut point #{point}"
      assert_receive {:result, ^pid, ^expected_message}
      assert_receive {:DOWN, ^monitor, :process, ^pid, :normal}
      assert :ok = CutPoints.verify_consumed(scenario)
      assert :ok = Scenario.stop(scenario)
    end)
  end

  test "every cut point can terminate its matching worker" do
    Enum.each(@cut_points, fn point ->
      scenario = Scenario.start()
      assert :ok = CutPoints.arm(scenario, point, :worker, :terminate)
      parent = self()

      {pid, monitor} =
        Scenario.spawn(scenario, :worker, fn ->
          CutPoints.hit(scenario, point, :worker)
          send(parent, :should_not_reach)
        end)

      assert_receive {:DOWN, ^monitor, :process, ^pid, :proof_terminated}
      refute_receive :should_not_reach
      assert :ok = CutPoints.verify_consumed(scenario)
      assert :ok = Scenario.stop(scenario)
    end)
  end

  test "wrong worker cannot consume an instruction and duplicate hits consume once" do
    scenario = Scenario.start()
    point = hd(@cut_points)
    parent = self()
    assert :ok = CutPoints.arm(scenario, point, :target, :raise)

    {other, other_ref} =
      Scenario.spawn(scenario, :other, fn ->
        result = CutPoints.hit(scenario, point, :other)
        send(parent, {:other_result, result})
      end)

    assert_receive {:other_result, :ok}
    assert_receive {:DOWN, ^other_ref, :process, ^other, :normal}

    workers =
      for _ <- 1..2 do
        Scenario.spawn(scenario, :target, fn ->
          try do
            CutPoints.hit(scenario, point, :target)
            send(parent, :continued)
          rescue
            RuntimeError -> send(parent, :raised)
          end
        end)
      end

    assert_receive :raised
    assert_receive :continued
    Enum.each(workers, fn {pid, ref} -> assert_receive {:DOWN, ^ref, :process, ^pid, :normal} end)
    assert :ok = CutPoints.verify_consumed(scenario)
    assert :ok = Scenario.stop(scenario)
    refute Process.alive?(scenario.controller)
  end

  test "duplicate arming and unknown cut points fail the scenario" do
    scenario = Scenario.start()
    point = hd(@cut_points)
    assert :ok = CutPoints.arm(scenario, point, :worker, :raise)
    assert {:error, :duplicate_arm} = CutPoints.arm(scenario, point, :worker, :raise)
    assert {:error, :unknown_cut_point} = CutPoints.arm(scenario, :unknown, :worker, :raise)
    assert {:error, failures} = Scenario.stop(scenario)
    assert :duplicate_arm in failures
    assert :unknown_cut_point in failures
  end

  test "unreached expected cut points fail verification" do
    scenario = Scenario.start()
    point = hd(@cut_points)
    assert :ok = CutPoints.arm(scenario, point, :worker, :raise)

    assert {:error, {:unreached_cut_points, [{^point, :worker}]}} =
             CutPoints.verify_consumed(scenario)

    assert {:error, _} = Scenario.stop(scenario)
  end

  test "stop fails when an expected cut point was never reached" do
    scenario = Scenario.start()
    assert :ok = CutPoints.arm(scenario, hd(@cut_points), :worker, :raise)
    assert {:error, [{:unreached_cut_points, [{_, :worker}]}]} = Scenario.stop(scenario)
  end

  test "a consumed cut point cannot be rearmed" do
    scenario = Scenario.start()
    point = hd(@cut_points)
    parent = self()
    assert :ok = CutPoints.arm(scenario, point, :worker, :raise)

    {worker, monitor} =
      Scenario.spawn(scenario, :worker, fn ->
        try do
          CutPoints.hit(scenario, point, :worker)
        rescue
          RuntimeError -> :ok
        end

        send(parent, :consumed)
      end)

    assert_receive :consumed
    assert_receive {:DOWN, ^monitor, :process, ^worker, :normal}
    assert {:error, :duplicate_arm} = CutPoints.arm(scenario, point, :worker, :raise)
    assert {:error, _} = Scenario.stop(scenario)
  end

  test "consumption survives worker replacement and scenarios remain isolated" do
    first = Scenario.start()
    second = Scenario.start()
    point = hd(@cut_points)
    parent = self()
    assert :ok = CutPoints.arm(first, point, :worker, :raise)

    {pid, ref} =
      Scenario.spawn(first, :worker, fn ->
        try do
          CutPoints.hit(first, point, :worker)
        rescue
          RuntimeError -> :ok
        end
      end)

    assert_receive {:DOWN, ^ref, :process, ^pid, :normal}

    {replacement, replacement_ref} =
      Scenario.spawn(first, :worker, fn ->
        send(parent, {:replacement, CutPoints.hit(first, point, :worker)})
      end)

    assert_receive {:replacement, :ok}
    assert_receive {:DOWN, ^replacement_ref, :process, ^replacement, :normal}
    assert :ok = CutPoints.verify_consumed(first)

    {second_worker, second_ref} =
      Scenario.spawn(second, :worker, fn ->
        send(parent, {:isolated, CutPoints.hit(second, point, :worker)})
      end)

    assert_receive {:isolated, :ok}
    assert_receive {:DOWN, ^second_ref, :process, ^second_worker, :normal}
    assert :ok = Scenario.stop(first)
    assert :ok = Scenario.stop(second)
  end

  test "controller death fails closed" do
    scenario = Scenario.start()

    {worker, worker_monitor} =
      Scenario.spawn(scenario, :worker, fn -> Process.sleep(:infinity) end)

    [{^worker, guardian}] = Scenario.owned_processes(scenario)
    guardian_monitor = Process.monitor(guardian)

    Process.exit(scenario.controller, :kill)
    assert_receive {:DOWN, ^worker_monitor, :process, ^worker, _reason}
    assert_receive {:DOWN, ^guardian_monitor, :process, ^guardian, _guardian_reason}
    assert {:error, :controller_down} = CutPoints.verify_consumed(scenario)
    assert {:error, :controller_down} = Scenario.stop(scenario)
  end

  test "parent death stops its controller and owned workers" do
    parent = self()

    {owner, owner_ref} =
      spawn_monitor(fn ->
        scenario = Scenario.start()

        {worker, _worker_ref} =
          Scenario.spawn(scenario, :worker, fn -> Process.sleep(:infinity) end)

        send(parent, {:controller, scenario.controller})
        send(parent, {:worker, worker})
      end)

    assert_receive {:controller, controller}
    assert_receive {:worker, worker}
    assert_receive {:DOWN, ^owner_ref, :process, ^owner, :normal}
    controller_ref = Process.monitor(controller)
    assert_receive {:DOWN, ^controller_ref, :process, ^controller, _}
    refute Process.alive?(worker)
    refute Process.alive?(owner)
  end

  test "barrier rejects missing and unknown participants and enforces its deadline" do
    scenario = Scenario.start()
    assert :ok = Barrier.define(scenario, :phase, [:one, :two])
    parent = self()

    {one, one_ref} =
      Scenario.spawn(scenario, :one, fn ->
        send(parent, {:one, Barrier.arrive(scenario, :phase, :one)})
      end)

    assert eventually(fn -> Barrier.arrivals(scenario, :phase) == [:one] end)
    assert {:error, {:missing_arrivals, [:two]}} = Barrier.release(scenario, :phase, 20)
    assert_receive {:one, {:error, {:missing_arrivals, [:two]}}}
    assert_receive {:DOWN, ^one_ref, :process, ^one, :normal}

    {stranger, stranger_ref} =
      Scenario.spawn(scenario, :stranger, fn ->
        send(parent, {:stranger, Barrier.arrive(scenario, :phase, :stranger)})
      end)

    assert_receive {:stranger, {:error, :unknown_participant}}
    assert_receive {:DOWN, ^stranger_ref, :process, ^stranger, :normal}

    assert :ok = Barrier.define(scenario, :deadline, [:late])
    assert {:error, :deadline} = Barrier.release(scenario, :deadline, 0)
    assert {:error, _} = Scenario.stop(scenario)
  end

  test "barrier releases only after every participant arrives" do
    scenario = Scenario.start()
    parent = self()
    assert :ok = Barrier.define(scenario, :phase, [:one, :two])

    workers =
      for label <- [:one, :two] do
        Scenario.spawn(scenario, label, fn ->
          send(parent, {label, Barrier.arrive(scenario, :phase, label)})
        end)
      end

    assert eventually(fn -> Barrier.arrivals(scenario, :phase) == [:one, :two] end)
    assert :ok = Barrier.release(scenario, :phase, 100)
    assert_receive {:one, :ok}
    assert_receive {:two, :ok}
    Enum.each(workers, fn {pid, ref} -> assert_receive {:DOWN, ^ref, :process, ^pid, :normal} end)
    assert :ok = Scenario.stop(scenario)
  end

  test "barrier rejects a duplicate participant arrival" do
    scenario = Scenario.start()
    parent = self()
    assert :ok = Barrier.define(scenario, :phase, [:one])

    first =
      Scenario.spawn(scenario, :one, fn ->
        send(parent, {:first, Barrier.arrive(scenario, :phase, :one)})
      end)

    assert eventually(fn -> Barrier.arrivals(scenario, :phase) == [:one] end)

    second =
      Scenario.spawn(scenario, :one, fn ->
        send(parent, {:second, Barrier.arrive(scenario, :phase, :one)})
      end)

    assert_receive {:second, {:error, :duplicate_arrival}}
    assert :ok = Barrier.release(scenario, :phase, 100)
    assert_receive {:first, :ok}

    Enum.each([first, second], fn {pid, ref} ->
      assert_receive {:DOWN, ^ref, :process, ^pid, :normal}
    end)

    assert {:error, _} = Scenario.stop(scenario)
  end

  test "barrier release fails when a participant dies before acknowledging" do
    scenario = Scenario.start()
    assert :ok = Barrier.define(scenario, :phase, [:one])

    {worker, worker_monitor} =
      Scenario.spawn(scenario, :one, fn -> Barrier.arrive(scenario, :phase, :one) end)

    assert eventually(fn -> Barrier.arrivals(scenario, :phase) == [:one] end)
    Process.exit(worker, :kill)
    assert_receive {:DOWN, ^worker_monitor, :process, ^worker, _reason}

    assert {:error, {:missing_acknowledgements, [:one]}} =
             Barrier.release(scenario, :phase, 100)

    assert {:error, _} = Scenario.stop(scenario)
  end

  test "barrier release waits only for its finite acknowledgement deadline" do
    scenario = Scenario.start()
    parent = self()
    assert :ok = Barrier.define(scenario, :phase, [:one])

    {worker, worker_monitor} =
      Scenario.spawn(scenario, :one, fn ->
        result = Scenario.request(scenario, {:barrier_arrive, :phase, :one})
        send(parent, {:released, result})
        receive do: (:finish -> :ok)
      end)

    assert eventually(fn -> Barrier.arrivals(scenario, :phase) == [:one] end)

    assert {:error, {:missing_acknowledgements, [:one]}} =
             Barrier.release(scenario, :phase, 25)

    assert_receive {:released, :released}
    send(worker, :finish)
    assert_receive {:DOWN, ^worker_monitor, :process, ^worker, :normal}
    assert {:error, _} = Scenario.stop(scenario)
  end

  test "a controller request that times out invalidates the scenario" do
    scenario = Scenario.start()
    assert {:error, :invalid_timeout} = Scenario.request(scenario, :verify_consumed, :infinity)
    assert {:error, :controller_timeout} = Scenario.request(scenario, {:delay_reply, 50}, 5)

    assert eventually(fn ->
             Scenario.request(scenario, :verify_consumed) == {:error, [:lost_reply]}
           end)

    assert {:error, [:lost_reply]} = Scenario.stop(scenario)
  end

  defp eventually(predicate, attempts \\ 100)
  defp eventually(_predicate, 0), do: false

  defp eventually(predicate, attempts) do
    if predicate.() do
      true
    else
      Process.sleep(1)
      eventually(predicate, attempts - 1)
    end
  end
end
