defmodule NewYou.Architecture.AshWriteBoundary do
  @moduledoc """
  Mechanical enforcement of ARC-029 (`docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`):
  ordinary business code does not use `Ecto.Repo` as a second business API.

  This is deliberately narrow. It rejects only the clear persistence bypasses
  that would route business state around owning Ash actions:

    * `:repo_write` - a mutating `NewYou.Repo` call (`insert`, `update`, `delete`, ...)
    * `:raw_sql_write` - `Repo.query`/`Ecto.Adapters.SQL.query` with mutating or non-literal SQL
    * `:ecto_multi_write` - a persisting `Ecto.Multi` operation
    * `:parallel_ecto_schema` - `use Ecto.Schema`, a second business model beside Ash resources
    * `:parse_error` - a file in scope that cannot be parsed, failing closed

  Ordinary reads, Ash actions, Sandbox configuration, migrations and the Repo
  module itself are not rejected. The analysis uses the compiler's own parser
  (`Code.string_to_quoted/2`), so no general static-analysis engine is involved.
  """

  @repo [:NewYou, :Repo]

  # Repo functions that persist. `transaction` is intentionally absent: writes
  # inside a transaction are themselves Repo calls and are caught individually.
  @repo_write_functions [
    :insert,
    :insert!,
    :insert_or_update,
    :insert_or_update!,
    :insert_all,
    :update,
    :update!,
    :update_all,
    :delete,
    :delete!,
    :delete_all
  ]

  @raw_sql_functions [:query, :query!, :query_many, :query_many!]
  @raw_sql_modules [@repo, [:Ecto, :Adapters, :SQL]]

  @multi_write_functions [
    :insert,
    :insert_all,
    :insert_or_update,
    :update,
    :update_all,
    :delete,
    :delete_all
  ]

  # Only literal, read-only statements may run through raw SQL.
  @read_only_prefix ~r/\A\s*(select|with|show|values|explain)\b/i
  @write_keyword ~r/\b(insert|update|delete|merge|truncate|alter|drop|create|grant|revoke|copy|do|call|set|reset|lock|vacuum|reindex|cluster|refresh|for\s+update)\b/i

  # Infrastructure exceptions. Each entry must name the exact file and the
  # reason it may touch the Repo. Keep this list short; prefer Ash actions.
  @infrastructure_allowlist %{
    "lib/new_you/repo.ex" => "Repo module definition and configuration"
  }

  @typedoc "A single architecture violation."
  @type violation :: %{
          required(:file) => String.t(),
          required(:line) => non_neg_integer(),
          required(:rule) => atom(),
          required(:message) => String.t()
        }

  @doc """
  Returns `:application` for files this rule governs, `:infrastructure` for
  allowlisted infrastructure files, and `:out_of_scope` for everything else
  (migrations, tests, sandbox configuration and other non-application code).
  """
  @spec scope(String.t()) :: :application | :infrastructure | :out_of_scope
  def scope(path) do
    normalized = String.replace(path, "\\", "/")

    cond do
      Map.has_key?(@infrastructure_allowlist, normalized) -> :infrastructure
      String.starts_with?(normalized, "lib/") and String.ends_with?(normalized, ".ex") -> :application
      true -> :out_of_scope
    end
  end

  @doc "Checks every governed application file under `root` and returns all violations."
  @spec check_app(String.t()) :: [violation()]
  def check_app(root \\ File.cwd!()) do
    root
    |> Path.join("lib/**/*.ex")
    |> Path.wildcard()
    |> Enum.sort()
    |> Enum.flat_map(fn absolute ->
      relative = Path.relative_to(absolute, root)

      case scope(relative) do
        :application -> check_source(File.read!(absolute), relative)
        _ -> []
      end
    end)
  end

  @doc """
  Checks one source string as if it lived at `path`. Returns `[]` when the
  file is out of scope or allowlisted.
  """
  @spec check_source(String.t(), String.t()) :: [violation()]
  def check_source(source, path) do
    case scope(path) do
      :application -> analyse(source, path)
      _ -> []
    end
  end

  defp analyse(source, path) do
    case Code.string_to_quoted(source, file: path, columns: false) do
      {:ok, ast} ->
        aliases = collect_aliases(ast)
        context = if String.starts_with?(path, "lib/new_you_web/"), do: "web layer", else: "application code"

        {_, violations} =
          Macro.prewalk(ast, [], fn node, acc ->
            {node, violations_for(node, aliases, path, context) ++ acc}
          end)

        violations
        |> Enum.reverse()
        |> Enum.uniq()

      {:error, {meta, message, token}} ->
        line = if is_list(meta), do: Keyword.get(meta, :line, 0), else: 0

        [
          violation(path, line, :parse_error, "cannot parse governed file: #{inspect(message)} #{token}")
        ]
    end
  end

  defp violations_for({:use, meta, [{:__aliases__, _, _} = target | _]} = _node, aliases, path, _context) do
    case resolve(target, aliases) do
      [:Ecto, :Schema] ->
        [
          violation(
            path,
            Keyword.get(meta, :line, 0),
            :parallel_ecto_schema,
            "`use Ecto.Schema` creates a parallel business model; model business state as an Ash resource"
          )
        ]

      _ ->
        []
    end
  end

  defp violations_for({{:., meta, [receiver, function]}, _call_meta, args}, aliases, path, context)
       when is_atom(function) and (is_list(args) or is_nil(args)) do
    line = Keyword.get(meta, :line, 0)

    case receiver do
      {:__aliases__, _, _} ->
        module = resolve(receiver, aliases)
        call_violations(module, function, args || [], line, path, context)

      _ ->
        []
    end
  end

  defp violations_for(_node, _aliases, _path, _context), do: []

  defp call_violations(module, function, args, line, path, context) do
    cond do
      module == @repo and function in @repo_write_functions ->
        [
          violation(
            path,
            line,
            :repo_write,
            "`NewYou.Repo.#{function}` persists business state directly from #{context}; use an owning Ash action"
          )
        ]

      module in @raw_sql_modules and function in @raw_sql_functions ->
        raw_sql_violations(args, line, path, context, function)

      module == [:Ecto, :Multi] and function in @multi_write_functions ->
        [
          violation(
            path,
            line,
            :ecto_multi_write,
            "`Ecto.Multi.#{function}` persists business state outside an Ash action"
          )
        ]

      true ->
        []
    end
  end

  defp raw_sql_violations([statement | _], line, path, _context, function) when is_binary(statement) do
    if Regex.match?(@read_only_prefix, statement) and not Regex.match?(@write_keyword, statement) do
      []
    else
      [
        violation(
          path,
          line,
          :raw_sql_write,
          "mutating or non-read-only raw SQL via `#{function}` bypasses Ash actions"
        )
      ]
    end
  end

  defp raw_sql_violations(_args, line, path, _context, function) do
    [
      violation(
        path,
        line,
        :raw_sql_write,
        "non-literal raw SQL via `#{function}` cannot be proven read-only; use an Ash read or an allowlisted infrastructure path"
      )
    ]
  end

  # Collects `alias A.B`, `alias A.B, as: C` and `alias A.{B, C}` into a
  # short-name -> full-name map. Scope is file-wide; this is a conservative
  # approximation that is sufficient for the boundary rule.
  defp collect_aliases(ast) do
    {_, aliases} =
      Macro.prewalk(ast, %{}, fn
        {:alias, _, [{:__aliases__, _, parts}]} = node, acc ->
          {node, Map.put(acc, List.last(parts), parts)}

        {:alias, _, [{:__aliases__, _, parts}, opts]} = node, acc when is_list(opts) ->
          name = Keyword.get(opts, :as, {:__aliases__, [], [List.last(parts)]})
          {:__aliases__, _, [as]} = name
          {node, Map.put(acc, as, parts)}

        {:alias, _, [{{:., _, [{:__aliases__, _, base}, :{}]}, _, subs}]} = node, acc ->
          acc =
            Enum.reduce(subs, acc, fn {:__aliases__, _, sub}, inner ->
              Map.put(inner, List.last(sub), base ++ sub)
            end)

          {node, acc}

        node, acc ->
          {node, acc}
      end)

    aliases
  end

  defp resolve({:__aliases__, _, [head | tail]}, aliases) do
    case Map.fetch(aliases, head) do
      {:ok, full} -> full ++ tail
      :error -> [head | tail]
    end
  end

  defp violation(path, line, rule, message) do
    %{file: path, line: line, rule: rule, message: message}
  end
end
