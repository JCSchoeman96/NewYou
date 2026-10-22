defmodule NewYou.Architecture.AshWriteBoundaryTest do
  # Pure AST tests: no database, no application start.
  use ExUnit.Case, async: true

  Code.require_file(Path.expand("../../../tools/architecture/ash_write_boundary.ex", __DIR__))

  alias NewYou.Architecture.AshWriteBoundary

  @app_path "lib/new_you/accounts.ex"
  @web_path "lib/new_you_web/controllers/profile_controller.ex"

  defp rules(source, path \\ @app_path) do
    source
    |> AshWriteBoundary.check_source(path)
    |> Enum.map(& &1.rule)
  end

  describe "negative fixtures: bypasses that must FAIL" do
    test "ordinary Repo business insert fails" do
      source = """
      defmodule NewYou.Accounts do
        def create(attrs), do: NewYou.Repo.insert(Ecto.Changeset.change(%{}, attrs))
      end
      """

      assert [%{rule: :repo_write, line: 2}] = AshWriteBoundary.check_source(source, @app_path)
    end

    test "aliased Repo update and delete_all fail" do
      source = """
      defmodule NewYou.Accounts do
        alias NewYou.Repo
        def touch(cs), do: cs |> Repo.update!()
        def purge(query), do: Repo.delete_all(query)
      end
      """

      assert [:repo_write, :repo_write] == rules(source)
    end

    test "raw mutating SQL fails" do
      source = """
      defmodule NewYou.Accounts do
        def hack, do: NewYou.Repo.query!("UPDATE accounts SET locked = true")
      end
      """

      assert [:raw_sql_write] == rules(source)
    end

    test "non-literal raw SQL fails closed" do
      source = """
      defmodule NewYou.Accounts do
        def run(sql), do: Ecto.Adapters.SQL.query!(NewYou.Repo, sql, [])
      end
      """

      assert [:raw_sql_write] == rules(source)
    end

    test "Ecto.Multi business write fails" do
      source = """
      defmodule NewYou.Accounts do
        def go(cs) do
          Ecto.Multi.new()
          |> Ecto.Multi.insert(:account, cs)
          |> NewYou.Repo.transaction()
        end
      end
      """

      assert :ecto_multi_write in rules(source)
    end

    test "parallel Ecto business schema fails" do
      source = """
      defmodule NewYou.Accounts.User do
        use Ecto.Schema

        schema "users" do
          field :email, :string
        end
      end
      """

      assert [:parallel_ecto_schema] == rules(source)
    end

    test "controller direct write fails" do
      source = """
      defmodule NewYouWeb.ProfileController do
        def update(conn, params) do
          NewYou.Repo.update(Ecto.Changeset.change(%{}, params))
          conn
        end
      end
      """

      assert [%{rule: :repo_write, message: message}] =
               AshWriteBoundary.check_source(source, @web_path)

      assert message =~ "web layer"
    end

    test "worker direct delete fails" do
      source = """
      defmodule NewYou.Workers.Cleanup do
        def perform, do: NewYou.Repo.delete_all(Ecto.Query.from(t in "tokens"))
      end
      """

      assert [:repo_write] == rules(source, "lib/new_you/workers/cleanup.ex")
    end

    test "unparseable governed file fails closed" do
      assert [:parse_error] == rules("defmodule Broken do def x(", @app_path)
    end
  end

  describe "positive fixtures: legitimate use that must PASS" do
    test "Ash domain action passes" do
      source = """
      defmodule NewYou.Accounts do
        def create(attrs), do: Ash.create!(NewYou.Accounts.Account, attrs, action: :register)
      end
      """

      assert [] == rules(source)
    end

    test "ordinary Repo reads pass" do
      source = """
      defmodule NewYou.Accounts do
        alias NewYou.Repo
        def fetch(id), do: Repo.get(NewYou.Accounts.Account, id)
        def count(query), do: Repo.aggregate(query, :count)
      end
      """

      assert [] == rules(source)
    end

    test "approved read-only connectivity query passes" do
      source = """
      defmodule NewYou.Health do
        def ping, do: NewYou.Repo.query!("SELECT 1", [])
      end
      """

      assert [] == rules(source)
    end

    test "Repo module definition passes" do
      source = """
      defmodule NewYou.Repo do
        use Ecto.Repo, otp_app: :new_you, adapter: Ecto.Adapters.Postgres
        def mutate(cs), do: insert(cs)
      end
      """

      assert [] == rules(source, "lib/new_you/repo.ex")
    end

    test "migration SQL passes because migrations are out of scope" do
      source = """
      defmodule NewYou.Repo.Migrations.Seed do
        use Ecto.Migration
        def up, do: execute("INSERT INTO accounts (id) VALUES (1)")
      end
      """

      assert [] == rules(source, "priv/repo/migrations/20261022000000_seed.exs")
    end

    test "sandbox configuration in test support passes" do
      source = """
      Ecto.Adapters.SQL.Sandbox.mode(NewYou.Repo, :manual)
      """

      assert [] == rules(source, "test/test_helper.exs")
      assert [] == rules(source, "lib/new_you/sandbox_probe.ex")
    end
  end

  test "the real application tree satisfies the boundary" do
    root = Path.expand("../../..", __DIR__)
    assert [] == AshWriteBoundary.check_app(root)
  end
end
