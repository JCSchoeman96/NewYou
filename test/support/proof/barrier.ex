defmodule NewYou.Proof.Barrier do
  @moduledoc false

  @spec define(NewYou.Proof.Scenario.t(), term(), [NewYou.Proof.Scenario.worker_label()]) ::
          term()
  @spec define(
          NewYou.Proof.Scenario.t(),
          term(),
          [NewYou.Proof.Scenario.worker_label()],
          pos_integer()
        ) :: term()
  def define(scenario, phase, participants, timeout_ms \\ 5_000) do
    NewYou.Proof.Scenario.request(
      scenario,
      {:barrier_define, phase, participants, timeout_ms}
    )
  end

  @spec arrive(NewYou.Proof.Scenario.t(), term(), NewYou.Proof.Scenario.worker_label()) :: term()
  def arrive(scenario, phase, participant) do
    case NewYou.Proof.Scenario.request(
           scenario,
           {:barrier_arrive, phase, participant},
           30_000
         ) do
      :released ->
        NewYou.Proof.Scenario.request(scenario, {:barrier_ack, phase, participant}, 30_000)

      result ->
        result
    end
  end

  @spec release(NewYou.Proof.Scenario.t(), term(), non_neg_integer()) :: term()
  def release(scenario, phase, timeout_ms) do
    request_timeout =
      if is_integer(timeout_ms), do: min(max(timeout_ms + 1_000, 1_000), 30_000), else: 1_000

    NewYou.Proof.Scenario.request(
      scenario,
      {:barrier_release, phase, timeout_ms},
      request_timeout
    )
  end

  @spec arrivals(NewYou.Proof.Scenario.t(), term()) ::
          [NewYou.Proof.Scenario.worker_label()] | {:error, term()}
  def arrivals(scenario, phase) do
    NewYou.Proof.Scenario.request(scenario, {:barrier_status, phase})
  end
end
