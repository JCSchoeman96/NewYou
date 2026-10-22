# Local database activation

Run `devcore-project doctor` from this worktree. If local state is missing or stale,
run `devcore-project activate`. Activation provisions only the allocated NewYou
roles/databases and renders ignored `.env.dev.local` and `.env.test.local` credentials. It does not manage
the shared stack. Redis is disabled. Both roles use NOCREATEDB.

Use `devcore-project run dev -- <command>` or
`devcore-project run test -- <command>` for database commands.
