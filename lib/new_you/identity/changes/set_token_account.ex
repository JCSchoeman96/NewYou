defmodule NewYou.Identity.Changes.SetTokenAccount do
  @moduledoc false

  use Ash.Resource.Change

  alias Ash.Changeset

  @impl true
  def change(changeset, _opts, _context) do
    case get_in(changeset.context, [:ash_authentication, :user]) do
      %{id: account_id} -> Changeset.force_change_attribute(changeset, :account_id, account_id)
      _ -> changeset
    end
  end
end
