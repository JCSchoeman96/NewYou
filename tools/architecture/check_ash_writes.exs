# Run via `mix check.architecture` (see the `aliases` in mix.exs).
# Enforces ARC-029: ordinary application code does not bypass owning Ash
# actions with direct Ecto.Repo business writes.

Code.require_file("ash_write_boundary.ex", __DIR__)

alias NewYou.Architecture.AshWriteBoundary

case AshWriteBoundary.check_app() do
  [] ->
    IO.puts("architecture: ARC-029 Ash write boundary PASS")

  violations ->
    IO.puts(:stderr, "architecture: ARC-029 Ash write boundary FAIL (#{length(violations)} violation(s))")

    for %{file: file, line: line, rule: rule, message: message} <- violations do
      IO.puts(:stderr, "  #{file}:#{line} [#{rule}] #{message}")
    end

    System.halt(1)
end
