defmodule NewYou.Identity.RegistrationOperationExpiry do
  @moduledoc """
  Periodically asks Identity to tombstone expired registration bindings.

  This process only schedules bounded sweeps. PostgreSQL rows and Identity Ash
  actions remain the authority, so duplicate sweeps from multiple nodes are safe.
  """

  use GenServer

  @default_interval_ms 60_000

  def start_link(opts \\ []) do
    GenServer.start_link(__MODULE__, opts, name: Keyword.get(opts, :name, __MODULE__))
  end

  @impl true
  def init(opts) do
    interval_ms = Keyword.get(opts, :interval_ms, @default_interval_ms)
    send(self(), :expire_registration_operations)
    {:ok, %{interval_ms: interval_ms}}
  end

  @impl true
  def handle_info(:expire_registration_operations, state) do
    case NewYou.Identity.expire_registration_operations() do
      {:ok, count} when count > 0 ->
        send(self(), :expire_registration_operations)

      _ ->
        Process.send_after(self(), :expire_registration_operations, state.interval_ms)
    end

    {:noreply, state}
  end
end
