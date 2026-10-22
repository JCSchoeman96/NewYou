## Development Workflow
- ALWAYS make changes and implementations on a git branch
- ALWAYS create a PR after work and implementations, so that your work can be reviewed
- When a PR is merged and you sync local, make sure the repo is clean and ready for the next agent
- Use a worktree when needed and necessary

## Local DevCore credentials

DO NOT ASK THE USER FOR LOCAL DB PASSWORDS OR DEVCORE-MANAGED DB VARIABLES.

If `.devcore/project.conf` exists, all local DEV/TEST DB credentials are already managed by DevCore.

Before requesting credentials:
1. Read `.devcore/project.conf`.
2. Read `.devcore/render-map.tsv`.
3. Run `devcore-project doctor`.
4. If local state is missing/stale, run `devcore-project activate`.
5. Execute DB-dependent commands with:
   `devcore-project run dev -- <command>`
   or
   `devcore-project run test -- <command>`.

Only report a bootstrap/service failure if these steps fail.
Never request or print the password value.

The repository must not start, stop, recreate, or delete shared DevCore services or volumes.
Redis is not used by NewYou. Both PostgreSQL roles must remain NOCREATEDB.
