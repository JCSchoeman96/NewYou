defmodule NewYou.Proof.CutPoints do
  @moduledoc false

  @points [
    {"transaction.before_commit", :"transaction.before_commit"},
    {"transaction.after_commit", :"transaction.after_commit"},
    {"scheduling.before_enqueue", :"scheduling.before_enqueue"},
    {"scheduling.after_enqueue", :"scheduling.after_enqueue"},
    {"provider.before_invoke", :"provider.before_invoke"},
    {"provider.after_invoke_before_persist", :"provider.after_invoke_before_persist"},
    {"evidence.before_materialize", :"evidence.before_materialize"},
    {"evidence.after_materialize_before_commit", :"evidence.after_materialize_before_commit"}
  ]

  @spec names() :: [String.t()]
  def names, do: Enum.map(@points, &elem(&1, 0))

  @spec normalize_name(atom() | String.t()) :: {:ok, atom()} | :error
  def normalize_name(name) when is_atom(name) do
    if Enum.any?(@points, fn {_text, atom} -> atom == name end), do: {:ok, name}, else: :error
  end

  def normalize_name(name) when is_binary(name) do
    case Enum.find(@points, fn {text, _atom} -> text == name end) do
      {_text, atom} -> {:ok, atom}
      nil -> :error
    end
  end

  def normalize_name(_name), do: :error

  @spec validate_name(term()) :: :ok | {:error, :unknown_cut_point}
  def validate_name(name) do
    case normalize_name(name) do
      {:ok, _name} -> :ok
      :error -> {:error, :unknown_cut_point}
    end
  end

  @spec arm(
          NewYou.Proof.Scenario.t(),
          String.t() | atom(),
          NewYou.Proof.Scenario.worker_label(),
          :raise | :terminate
        ) :: term()
  def arm(scenario, name, worker_label, mode) when mode in [:raise, :terminate] do
    NewYou.Proof.Scenario.request(scenario, {:arm, name, worker_label, mode})
  end

  def arm(scenario, _name, _worker_label, _mode),
    do: NewYou.Proof.Scenario.request(scenario, {:invalid_arm})

  @spec hit(
          NewYou.Proof.Scenario.t(),
          String.t() | atom(),
          NewYou.Proof.Scenario.worker_label()
        ) :: term()
  def hit(scenario, name, worker_label) do
    case NewYou.Proof.Scenario.request(scenario, {:hit, name, worker_label}) do
      {:raise, point} -> raise "proof cut point #{point}"
      result -> result
    end
  end

  @spec verify_consumed(NewYou.Proof.Scenario.t()) :: :ok | {:error, term()}
  def verify_consumed(scenario), do: NewYou.Proof.Scenario.verify_consumed(scenario)
end
