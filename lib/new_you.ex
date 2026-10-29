defmodule NewYou do
  @moduledoc "Application-wide configuration access."

  @doc "Returns the configured participant-facing platform name."
  def platform_name, do: Application.fetch_env!(:new_you, :platform_name)
end
