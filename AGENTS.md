# NewYou Engineering Contract

This file is manually owned by NewYou. Generated framework documentation never replaces it.

## Development Workflow

- ALWAYS make changes and implementations on a git branch.
- ALWAYS create a PR after work and implementations, so that your work can be reviewed.
- When a PR is merged and you sync local, make sure the repo is clean and ready for the next agent.
- Use a worktree when needed and necessary.
- Do not merge unless explicitly authorised.

## Authority

The live GitHub repository is canonical.

For governed decisions, start with `docs/00_platform/README.md` and the current authority manifest.

Governance is read-only during ordinary implementation. Stop on a genuine authority contradiction; do not silently repair upstream law in implementation.

## Required Skills

Before implementation, use `.agents/skills/project-implementation/SKILL.md`.

Before handoff or merge recommendation, use `.agents/skills/code-change-verification/SKILL.md`.

Load generated framework skills under `.agents/skills/` only when relevant.

Use Igniter first for supported structural or package changes; hand-edit only where Igniter does not safely support the change.

## Engineering Invariants

Every durable business truth has exactly one owning Domain. Mutations go through that owner.

Derived state, caches, analytics, PubSub, provider state and UI projections are never business authority.

Do not bypass owning Ash interfaces with ordinary Repo, Ecto or raw-SQL business writes. `mix check.architecture` enforces this (ARC-029).

Do not introduce Redis, extra services, extra Repos, ETS/process authority or speculative infrastructure without a demonstrated requirement.

Meaningful state transitions are intentional domain actions with appropriate guards, invariants, authorization, retries and idempotency.

## Evidence

Do not guess material framework or package APIs.

Prefer, in order: repository authority; relevant generated framework skills; Tidewave/runtime evidence; version-matched official HexDocs or source; model memory last.

Tidewave is development-only. It is diagnostic tooling and never business authority.

## Plane

Plane is the mandatory execution ledger.

Every delivery-affecting issue, blocker, dependency, deferred fix, follow-up, security concern, architecture concern or discovered missing prerequisite MUST be created or updated in Plane before handoff.

Search for an existing Plane issue first. Do not create duplicates. Update the existing owner where one exists. Add dependency relations where sequencing exists.

Do not leave delivery-affecting work only in chat, PR comments, TODO comments, handoff notes or memory.

Plane tracks delivery. GitHub governed sources remain architectural and product authority; Plane never overrides them.

## Verification

`mix check` is the canonical fast gate. `mix check.deep` is the slower engineering gate.

Application CI runs `mix check` and `mix check.deep`. Foundation Smoke runs for every PR. Historical Foundation Full runs only for governance-sensitive changes or deliberate exact-SHA certification.

Before handoff verify the exact diff, exact head SHA, relevant checks and tests, Plane state and a clean worktree.

## Local DevCore Credentials

DO NOT ASK THE USER FOR LOCAL DB PASSWORDS OR DEVCORE-MANAGED DB VARIABLES.

If `.devcore/project.conf` exists, local DEV and TEST DB credentials are managed by DevCore:

1. Run `devcore-project doctor`; if state is missing or stale, run `devcore-project activate`.
2. Run DB-dependent commands with `devcore-project run dev -- <command>` or `devcore-project run test -- <command>`.

Never request or print a password value. The repository must not start, stop, recreate or delete shared DevCore services or volumes. Redis is not used by NewYou. Both PostgreSQL roles must remain NOCREATEDB.
