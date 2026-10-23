defmodule NewYou.Proof.Scenario do
  @moduledoc false

  defstruct [:controller, :reference, :owner]

  @type t :: %__MODULE__{
          controller: pid(),
          reference: reference(),
          owner: pid()
        }
  @type worker_label :: atom() | binary()

  @request_timeout 5_000
  @max_timeout 30_000

  @spec start() :: t()
  @spec start(keyword()) :: t()
  def start(_opts \\ []) do
    owner = self()
    reference = make_ref()
    {controller, monitor} = spawn_monitor(fn -> init(owner, reference) end)

    receive do
      {:scenario_ready, ^reference} ->
        Process.demonitor(monitor, [:flush])
        %__MODULE__{controller: controller, reference: reference, owner: owner}
    after
      @request_timeout ->
        Process.exit(controller, :kill)
        raise "proof scenario controller did not start"
    end
  end

  @spec spawn(t(), worker_label(), (-> term())) :: {pid(), reference()}
  def spawn(%__MODULE__{} = scenario, label, fun) when is_function(fun, 0) do
    owner!(scenario)

    {pid, monitor} =
      spawn_monitor(fn ->
        worker = self()
        guardian = spawn(fn -> worker_guard(worker, scenario.controller, scenario.owner) end)
        send(scenario.owner, {:scenario_guard_ready, scenario.reference, worker, guardian})

        receive do
          {:scenario_start, reference} when reference == scenario.reference -> fun.()
          _ -> :ok
        end
      end)

    guardian =
      receive do
        {:scenario_guard_ready, reference, ^pid, guardian} when reference == scenario.reference ->
          guardian
      after
        @request_timeout ->
          Process.exit(pid, :kill)
          raise "proof worker guardian did not start"
      end

    case request(scenario, {:register_worker, label, pid, guardian}) do
      :ok ->
        send(pid, {:scenario_start, scenario.reference})
        {pid, monitor}

      {:error, reason} ->
        Process.demonitor(monitor, [:flush])
        Process.exit(pid, :kill)
        raise "could not register proof worker: #{inspect(reason)}"
    end
  end

  @spec stop(t()) :: :ok | {:error, term()}
  def stop(%__MODULE__{} = scenario) do
    owner!(scenario)
    monitor = Process.monitor(scenario.controller)
    result = request(scenario, :stop, @request_timeout + 1_000)

    receive do
      {:DOWN, ^monitor, :process, controller, _reason} when controller == scenario.controller ->
        result
    after
      5_000 ->
        Process.demonitor(monitor, [:flush])
        {:error, :cleanup_timeout}
    end
  end

  @spec verify_consumed(t()) :: :ok | {:error, term()}
  def verify_consumed(%__MODULE__{} = scenario), do: request(scenario, :verify_consumed)

  @spec owned_processes(t()) :: [{pid(), pid()}] | {:error, term()}
  def owned_processes(%__MODULE__{} = scenario), do: request(scenario, :owned_processes)

  @spec request(t(), term()) :: term()
  @spec request(t(), term(), pos_integer()) :: term()
  def request(scenario, operation, timeout \\ @request_timeout)

  def request(%__MODULE__{} = scenario, operation, timeout)
      when is_integer(timeout) and timeout > 0 and timeout <= @max_timeout do
    reference = make_ref()
    monitor = Process.monitor(scenario.controller)

    send(
      scenario.controller,
      {:scenario_request, scenario.reference, reference, self(), operation}
    )

    receive do
      {:scenario_reply, ^reference, result} ->
        Process.demonitor(monitor, [:flush])
        result

      {:DOWN, ^monitor, :process, _pid, _reason} ->
        {:error, :controller_down}
    after
      timeout ->
        Process.demonitor(monitor, [:flush])

        send(
          scenario.controller,
          {:scenario_request, scenario.reference, make_ref(), self(),
           {:record_failure, :lost_reply}}
        )

        {:error, :controller_timeout}
    end
  end

  def request(%__MODULE__{}, _operation, _timeout), do: {:error, :invalid_timeout}

  defp owner!(%__MODULE__{owner: owner}) when owner == self(), do: :ok
  defp owner!(_scenario), do: raise("proof scenario operation must run in its owner")

  defp init(owner, reference) do
    owner_monitor = Process.monitor(owner)
    send(owner, {:scenario_ready, reference})

    loop(%{
      owner: owner,
      owner_monitor: owner_monitor,
      reference: reference,
      workers: %{},
      guardians: %{},
      cuts: %{},
      failures: [],
      barriers: %{}
    })
  end

  defp loop(state) do
    receive do
      {:scenario_request, reference, request_ref, caller, operation}
      when reference == state.reference ->
        {state, response, stop?} = dispatch(operation, caller, request_ref, state)

        if stop? do
          cleanup(state, response)
          send(caller, {:scenario_reply, request_ref, response})
        else
          if response != :deferred, do: send(caller, {:scenario_reply, request_ref, response})
          loop(state)
        end

      {:DOWN, ref, :process, _pid, _reason} when ref == state.owner_monitor ->
        cleanup(state, :owner_down)

      {:barrier_release_timeout, phase, timer_ref} ->
        loop(barrier_release_timeout(state, phase, timer_ref))

      {:DOWN, ref, :process, pid, reason} ->
        state = worker_down(state, ref, pid, reason)
        loop(state)
    end
  end

  defp dispatch({:barrier_arrive, phase, label}, caller, request_ref, state),
    do: handle_barrier_arrive(phase, label, caller, request_ref, state)

  defp dispatch({:barrier_release, phase, timeout}, caller, request_ref, state),
    do: release_barrier(phase, timeout, caller, request_ref, state)

  defp dispatch({:barrier_ack, phase, label}, caller, _request_ref, state),
    do: handle_barrier_ack(phase, label, caller, state)

  defp dispatch({:barrier_define, phase, participants, timeout}, caller, _request_ref, state),
    do: handle_barrier_define(phase, participants, timeout, caller, state)

  defp dispatch({:barrier_status, phase}, _caller, _request_ref, state) do
    case Map.get(state.barriers, phase) do
      nil -> {state, {:error, :unknown_phase}, false}
      barrier -> {state, MapSet.to_list(barrier.arrived) |> Enum.sort(), false}
    end
  end

  defp dispatch({:record_failure, failure}, _caller, _request_ref, state),
    do: fail(state, failure, :ok)

  defp dispatch({:delay_reply, milliseconds}, _caller, _request_ref, state)
       when is_integer(milliseconds) and milliseconds > 0 and milliseconds <= 1_000 do
    Process.sleep(milliseconds)
    {state, :ok, false}
  end

  defp dispatch(operation, caller, _request_ref, state),
    do: handle_operation(operation, caller, state)

  defp handle_operation({:register_worker, label, pid, guardian}, caller, state)
       when caller == state.owner do
    monitor = Process.monitor(pid)
    guardian_monitor = Process.monitor(guardian)

    worker = %{
      label: label,
      monitor: monitor,
      guardian: guardian,
      guardian_monitor: guardian_monitor,
      expected_exit: false,
      worker_down: false,
      guardian_down: false
    }

    workers = Map.put(state.workers, pid, worker)
    guardians = Map.put(state.guardians, guardian, pid)
    {%{state | workers: workers, guardians: guardians}, :ok, false}
  end

  defp handle_operation({:register_worker, _label, _pid, _guardian}, _caller, state),
    do: fail(state, :owner_only, {:error, :owner_only})

  defp handle_operation(:owned_processes, caller, state) when caller == state.owner do
    children = Enum.map(state.workers, fn {worker, info} -> {worker, info.guardian} end)
    {state, children, false}
  end

  defp handle_operation({:arm, name, label, mode}, caller, state) do
    case NewYou.Proof.CutPoints.normalize_name(name) do
      :error ->
        fail(state, :unknown_cut_point, {:error, :unknown_cut_point})

      {:ok, canonical_name} ->
        cond do
          caller != state.owner ->
            fail(state, :owner_only, {:error, :owner_only})

          mode not in [:raise, :terminate] ->
            fail(state, :invalid_mode, {:error, :invalid_mode})

          Map.has_key?(state.cuts, {canonical_name, label}) ->
            fail(state, :duplicate_arm, {:error, :duplicate_arm})

          true ->
            {%{
               state
               | cuts:
                   Map.put(state.cuts, {canonical_name, label}, %{mode: mode, consumed: false})
             }, :ok, false}
        end
    end
  end

  defp handle_operation({:hit, name, label}, caller, state) do
    with {:ok, canonical_name} <- NewYou.Proof.CutPoints.normalize_name(name),
         {:ok, ^label, worker} <- worker_for(state, caller),
         %{mode: mode, consumed: false} = cut <- Map.get(state.cuts, {canonical_name, label}) do
      cuts = Map.put(state.cuts, {canonical_name, label}, %{cut | consumed: true})
      state = %{state | cuts: cuts}

      case mode do
        :raise ->
          {state, {:raise, canonical_name}, false}

        :terminate ->
          workers = Map.update!(state.workers, worker, &%{&1 | expected_exit: true})
          state = %{state | workers: workers}
          Process.exit(worker, :proof_terminated)
          monitor = Map.fetch!(state.workers, worker).monitor

          receive do
            {:DOWN, ^monitor, :process, ^worker, reason} ->
              {worker_down(state, monitor, worker, reason), :terminated, false}
          after
            1_000 -> fail(state, :termination_timeout, {:error, :termination_timeout})
          end
      end
    else
      :error ->
        fail(state, :unknown_cut_point, {:error, :unknown_cut_point})

      {:error, :worker_mismatch} ->
        fail(state, :worker_mismatch, {:error, :worker_mismatch})

      {:ok, _other_label, _worker} ->
        {state, :ok, false}

      nil ->
        {state, :ok, false}

      %{consumed: true} ->
        {state, :ok, false}
    end
  end

  defp handle_operation(:verify_consumed, _caller, state) do
    unreached =
      state.cuts
      |> Enum.filter(fn {_key, cut} -> not cut.consumed end)
      |> Enum.map(&elem(&1, 0))
      |> Enum.sort()

    cond do
      unreached != [] ->
        failure = {:unreached_cut_points, unreached}
        {%{state | failures: Enum.uniq([failure | state.failures])}, {:error, failure}, false}

      state.failures == [] ->
        {state, :ok, false}

      true ->
        {state, {:error, Enum.reverse(state.failures)}, false}
    end
  end

  defp handle_operation(:stop, caller, state) when caller == state.owner do
    unreached =
      state.cuts
      |> Enum.filter(fn {_key, cut} -> not cut.consumed end)
      |> Enum.map(&elem(&1, 0))
      |> Enum.sort()

    failures =
      if unreached == [],
        do: state.failures,
        else: [{:unreached_cut_points, unreached} | state.failures]

    state = cleanup_workers(%{state | failures: Enum.uniq(failures)})

    if state.failures == [],
      do: {state, :ok, true},
      else: {state, {:error, Enum.reverse(state.failures)}, true}
  end

  defp handle_operation(_operation, _caller, state),
    do: fail(state, :invalid_request, {:error, :invalid_request})

  defp handle_barrier_define(phase, participants, timeout, caller, state) do
    case barrier_definition_error(state, phase, participants, timeout, caller) do
      nil ->
        barrier = new_barrier(participants, timeout)
        {put_barrier(state, phase, barrier), :ok, false}

      {failure, response} ->
        fail(state, failure, response)
    end
  end

  defp barrier_definition_error(state, phase, participants, timeout, caller) do
    cond do
      caller != state.owner ->
        {:owner_only, {:error, :owner_only}}

      Map.has_key?(state.barriers, phase) ->
        {:duplicate_phase, {:error, :duplicate_phase}}

      invalid_participants?(participants) ->
        {:invalid_participants, {:error, :invalid_participants}}

      invalid_timeout?(timeout) ->
        {:invalid_deadline, {:error, :invalid_deadline}}

      true ->
        nil
    end
  end

  defp invalid_participants?(participants) do
    not is_list(participants) or participants == [] or
      length(Enum.uniq(participants)) != length(participants)
  end

  defp invalid_timeout?(timeout),
    do: not is_integer(timeout) or timeout <= 0 or timeout > @max_timeout

  defp new_barrier(participants, timeout) do
    %{
      participants: MapSet.new(participants),
      arrived: MapSet.new(),
      waiters: %{},
      acknowledged: MapSet.new(),
      released: false,
      release_waiter: nil,
      timer_ref: nil,
      timer_handle: nil,
      release_deadline: nil,
      deadline: now_ms() + timeout
    }
  end

  defp handle_barrier_arrive(phase, label, caller, request_ref, state) do
    case {Map.get(state.barriers, phase), worker_for(state, caller)} do
      {nil, _} ->
        fail(state, :unknown_phase, {:error, :unknown_phase})

      {_barrier, {:error, _}} ->
        fail(state, :worker_mismatch, {:error, :worker_mismatch})

      {barrier, {:ok, ^label, _pid}} ->
        cond do
          now_ms() > barrier.deadline ->
            fail(state, :barrier_deadline, {:error, :deadline})

          not MapSet.member?(barrier.participants, label) ->
            fail(state, :unknown_participant, {:error, :unknown_participant})

          MapSet.member?(barrier.arrived, label) ->
            fail(state, :duplicate_arrival, {:error, :duplicate_arrival})

          true ->
            updated = %{
              barrier
              | arrived: MapSet.put(barrier.arrived, label),
                waiters: Map.put(barrier.waiters, label, {caller, request_ref})
            }

            {%{state | barriers: Map.put(state.barriers, phase, updated)}, :deferred, false}
        end

      {_barrier, {:ok, _other, _pid}} ->
        fail(state, :worker_mismatch, {:error, :worker_mismatch})
    end
  end

  defp handle_barrier_ack(phase, label, caller, state) do
    case {Map.get(state.barriers, phase), worker_for(state, caller)} do
      {nil, _} ->
        fail(state, :unknown_phase, {:error, :unknown_phase})

      {_barrier, {:error, _}} ->
        fail(state, :worker_mismatch, {:error, :worker_mismatch})

      {barrier, {:ok, ^label, _pid}} ->
        acknowledge_barrier(state, phase, label, barrier)

      {_barrier, {:ok, _other_label, _pid}} ->
        fail(state, :worker_mismatch, {:error, :worker_mismatch})
    end
  end

  defp acknowledge_barrier(state, phase, label, barrier) do
    cond do
      not MapSet.member?(barrier.participants, label) ->
        fail(state, :unknown_participant, {:error, :unknown_participant})

      not barrier.released or is_nil(barrier.release_waiter) ->
        {state, {:error, :release_failed}, false}

      now_ms() >= barrier.release_deadline ->
        expire_barrier_release(state, phase, barrier)

      MapSet.member?(barrier.acknowledged, label) ->
        fail(state, :duplicate_acknowledgement, {:error, :duplicate_acknowledgement})

      true ->
        record_barrier_ack(state, phase, label, barrier)
    end
  end

  defp record_barrier_ack(state, phase, label, barrier) do
    acknowledged = MapSet.put(barrier.acknowledged, label)
    updated = %{barrier | acknowledged: acknowledged}

    if MapSet.equal?(acknowledged, barrier.participants) do
      {owner, request_ref, _timer_ref} = barrier.release_waiter
      Process.cancel_timer(barrier.timer_handle)
      send(owner, {:scenario_reply, request_ref, :ok})
      updated = %{updated | release_waiter: nil, timer_ref: nil, timer_handle: nil}
      {put_barrier(state, phase, updated), :ok, false}
    else
      {put_barrier(state, phase, updated), :ok, false}
    end
  end

  defp barrier_release_timeout(state, phase, timer_ref) do
    case Map.get(state.barriers, phase) do
      %{timer_ref: ^timer_ref, release_waiter: {owner, request_ref, ^timer_ref}} = barrier ->
        missing =
          MapSet.difference(barrier.participants, barrier.acknowledged)
          |> MapSet.to_list()
          |> Enum.sort()

        response = {:error, {:missing_acknowledgements, missing}}
        send(owner, {:scenario_reply, request_ref, response})

        updated = %{
          barrier
          | released: false,
            release_waiter: nil,
            timer_ref: nil,
            timer_handle: nil
        }

        failure = {:missing_acknowledgements, missing}
        put_barrier(%{state | failures: Enum.uniq([failure | state.failures])}, phase, updated)

      _ ->
        state
    end
  end

  defp expire_barrier_release(state, phase, barrier) do
    {owner, request_ref, _timer_ref} = barrier.release_waiter

    missing =
      MapSet.difference(barrier.participants, barrier.acknowledged)
      |> MapSet.to_list()
      |> Enum.sort()

    response = {:error, {:missing_acknowledgements, missing}}
    send(owner, {:scenario_reply, request_ref, response})
    if barrier.timer_handle, do: Process.cancel_timer(barrier.timer_handle)
    updated = %{barrier | released: false, release_waiter: nil, timer_ref: nil, timer_handle: nil}
    failure = {:missing_acknowledgements, missing}

    {put_barrier(%{state | failures: Enum.uniq([failure | state.failures])}, phase, updated),
     response, false}
  end

  defp put_barrier(state, phase, barrier),
    do: %{state | barriers: Map.put(state.barriers, phase, barrier)}

  defp release_barrier(phase, timeout, caller, request_ref, state) when caller == state.owner do
    case Map.get(state.barriers, phase) do
      nil ->
        fail(state, :unknown_phase, {:error, :unknown_phase})

      barrier ->
        case release_problem(barrier, timeout) do
          :ok ->
            begin_barrier_release(state, phase, timeout, caller, request_ref, barrier)

          {failure, response, notify_arrivals?} ->
            fail_barrier_release(state, barrier, failure, response, notify_arrivals?)
        end
    end
  end

  defp release_barrier(_phase, _timeout, _caller, _request_ref, state),
    do: fail(state, :owner_only, {:error, :owner_only})

  defp release_problem(barrier, timeout) do
    missing =
      MapSet.difference(barrier.participants, barrier.arrived) |> MapSet.to_list() |> Enum.sort()

    missing_acknowledgements =
      barrier.waiters
      |> Enum.filter(fn {_label, {pid, _ref}} -> not Process.alive?(pid) end)
      |> Enum.map(&elem(&1, 0))
      |> Enum.sort()

    cond do
      not is_integer(timeout) or timeout < 0 or timeout > @max_timeout ->
        {:invalid_deadline, {:error, :invalid_deadline}, false}

      timeout == 0 or now_ms() > barrier.deadline ->
        {:barrier_deadline, {:error, :deadline}, true}

      missing != [] ->
        {{:missing_arrivals, missing}, {:error, {:missing_arrivals, missing}}, true}

      missing_acknowledgements != [] ->
        {{:missing_acknowledgements, missing_acknowledgements},
         {:error, {:missing_acknowledgements, missing_acknowledgements}}, true}

      true ->
        :ok
    end
  end

  defp notify_barrier_waiters(barrier, response),
    do: Enum.each(Map.values(barrier.waiters), &reply_waiter(&1, response))

  defp fail_barrier_release(state, barrier, failure, response, notify_arrivals?) do
    maybe_notify_barrier_waiters(barrier, response, notify_arrivals?)
    fail(state, failure, response)
  end

  defp maybe_notify_barrier_waiters(barrier, response, true),
    do: notify_barrier_waiters(barrier, response)

  defp maybe_notify_barrier_waiters(_barrier, _response, false), do: :ok

  defp begin_barrier_release(state, phase, timeout, caller, request_ref, barrier) do
    wait_ms = min(timeout, max(barrier.deadline - now_ms(), 1))
    timer_ref = make_ref()

    timer_handle =
      Process.send_after(self(), {:barrier_release_timeout, phase, timer_ref}, wait_ms)

    notify_barrier_waiters(barrier, :released)

    updated = %{
      barrier
      | released: true,
        release_waiter: {caller, request_ref, timer_ref},
        timer_ref: timer_ref,
        timer_handle: timer_handle,
        release_deadline: min(barrier.deadline, now_ms() + timeout)
    }

    {put_barrier(state, phase, updated), :deferred, false}
  end

  defp reply_waiter({pid, request_ref}, response),
    do: send(pid, {:scenario_reply, request_ref, response})

  defp worker_for(state, caller) do
    case Map.get(state.workers, caller) do
      %{label: label} -> {:ok, label, caller}
      nil -> {:error, :worker_mismatch}
    end
  end

  defp fail(state, failure, response),
    do: {%{state | failures: Enum.uniq([failure | state.failures])}, response, false}

  defp worker_down(state, ref, pid, reason) do
    case Map.get(state.workers, pid) do
      %{monitor: ^ref} = worker ->
        handle_worker_down(state, pid, worker, reason)

      _ ->
        handle_guardian_down(state, pid, reason)
    end
  end

  defp handle_worker_down(state, pid, worker, reason) do
    failures =
      if expected_worker_exit?(worker, reason),
        do: state.failures,
        else: [:worker_failed | state.failures]

    state = update_worker(state, pid, %{worker | worker_down: true}, failures)
    fail_barriers_for_worker(state, pid)
  end

  defp expected_worker_exit?(%{expected_exit: true}, reason),
    do: reason in [:killed, :proof_terminated]

  defp expected_worker_exit?(_worker, :normal), do: true
  defp expected_worker_exit?(_worker, _reason), do: false

  defp handle_guardian_down(state, guardian, reason) do
    case Map.get(state.guardians, guardian) do
      nil -> state
      worker_pid -> guardian_process_down(state, worker_pid, reason)
    end
  end

  defp guardian_process_down(state, worker_pid, reason) do
    worker = Map.fetch!(state.workers, worker_pid)
    failures = if reason == :normal, do: state.failures, else: [:guardian_failed | state.failures]
    if not worker.worker_down, do: Process.exit(worker_pid, :kill)
    update_worker(state, worker_pid, %{worker | guardian_down: true}, failures)
  end

  defp update_worker(state, pid, worker, failures) do
    if worker.worker_down and worker.guardian_down do
      %{
        state
        | workers: Map.delete(state.workers, pid),
          guardians: Map.delete(state.guardians, worker.guardian),
          failures: failures
      }
    else
      %{state | workers: Map.put(state.workers, pid, worker), failures: failures}
    end
  end

  defp fail_barriers_for_worker(state, worker_pid) do
    Enum.reduce(state.barriers, state, fn {phase, barrier}, acc ->
      if waiting_worker?(barrier, worker_pid),
        do: fail_barrier_acknowledgement(acc, phase, barrier),
        else: acc
    end)
  end

  defp waiting_worker?(barrier, worker_pid) do
    not is_nil(barrier.release_waiter) and
      Enum.any?(barrier.waiters, fn {_label, {pid, _ref}} -> pid == worker_pid end)
  end

  defp fail_barrier_acknowledgement(state, phase, barrier) do
    {owner, request_ref, _timer_ref} = barrier.release_waiter

    missing =
      MapSet.difference(barrier.participants, barrier.acknowledged)
      |> MapSet.to_list()
      |> Enum.sort()

    response = {:error, {:missing_acknowledgements, missing}}
    send(owner, {:scenario_reply, request_ref, response})
    if barrier.timer_handle, do: Process.cancel_timer(barrier.timer_handle)

    updated = %{
      barrier
      | released: false,
        release_waiter: nil,
        timer_ref: nil,
        timer_handle: nil
    }

    failure = {:missing_acknowledgements, missing}
    put_barrier(%{state | failures: Enum.uniq([failure | state.failures])}, phase, updated)
  end

  defp cleanup_workers(state) do
    workers =
      Map.new(state.workers, fn {pid, worker} -> {pid, %{worker | expected_exit: true}} end)

    state = %{state | workers: workers}
    Enum.each(Map.keys(state.workers), &Process.exit(&1, :kill))
    deadline = now_ms() + 5_000
    await_workers(state, deadline)
  end

  defp await_workers(state, deadline) do
    if map_size(state.workers) == 0 or now_ms() >= deadline do
      if map_size(state.workers) == 0,
        do: state,
        else: %{state | failures: [:cleanup_timeout | state.failures]}
    else
      receive do
        {:DOWN, ref, :process, pid, reason} ->
          await_workers(worker_down(state, ref, pid, reason), deadline)
      after
        max(deadline - now_ms(), 0) -> %{state | failures: [:cleanup_timeout | state.failures]}
      end
    end
  end

  defp cleanup(state, _reason), do: cleanup_workers(state)

  defp now_ms, do: System.monotonic_time(:millisecond)

  defp worker_guard(worker, controller, owner) do
    worker_monitor = Process.monitor(worker)
    controller_monitor = Process.monitor(controller)
    owner_monitor = Process.monitor(owner)

    receive do
      {:DOWN, ^worker_monitor, :process, ^worker, _reason} ->
        :ok

      {:DOWN, ref, :process, _pid, _reason}
      when ref == controller_monitor or ref == owner_monitor ->
        Process.exit(worker, :kill)

        receive do
          {:DOWN, ^worker_monitor, :process, ^worker, _worker_reason} -> :ok
        after
          1_000 -> :ok
        end
    end
  end
end
