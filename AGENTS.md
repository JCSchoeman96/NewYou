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

The local agent is a planner and implementer, not a source of Product, Architecture, Domain or Roadmap law. It may make JIT implementation choices only where authority intentionally leaves them open. Never improvise missing product, architecture, domain, clinical, legal, commercial, safety or entitlement law.

The authority order is Product Law, Architecture Law, Domain Law, Roadmap, supporting operating/frontend/engineering contracts, current Open Work, approved Feature Pack/JIT contracts, proof/evidence, then implementation. The README and manifest route current files. Working and derived artifacts are navigation or evidence, not governing authority; archive is historical evidence.

## Reconnaissance and planning

Before `/grilling`, `to-spec`, `to-tickets` or material implementation, inspect the relevant live state: README routing and the current authority manifest; applicable Product/Decision, Architecture, Domain, Roadmap, Operating and Frontend authority; current Open Work; relevant Feature Pack, JIT and proof contracts; Plane work, blockers and dependencies; and actual code, tests, migrations and dependencies. Follow evidence as far as the task requires, not the entire repository or every authority document.

Classify material questions before deciding:

- `LOCKED`: authority already answers it; follow it.
- `JIT IMPLEMENTATION CHOICE`: authority intentionally leaves it open; choose the simplest compliant option.
- `UNRESOLVED GOVERNED QUESTION`: stop, record it in Plane and escalate to the appropriate authority.

For insufficiently defined work, the normal sequence is repository reconnaissance, `/grilling`, `to-spec` only if genuinely needed, `to-tickets`, Plane, independent Master Gate review, then implementation after applicable gates pass. Do not re-grill or re-spec settled decisions without new evidence, contradiction or changed scope.

Implementation begins only from an authorised Plane ticket or contract and after its applicable prerequisites are satisfied.

Use focused, test-first development and applicable repository checks for material implementation or behaviour work.

## Required Skills

Before implementation, use `.agents/skills/project-implementation/SKILL.md`.

Before handoff or merge recommendation, use `.agents/skills/code-change-verification/SKILL.md`.

Load generated framework skills under `.agents/skills/` only when relevant.

Use Igniter first for supported structural or package changes; hand-edit only where Igniter does not safely support the change.

## Engineering Invariants

Every durable business truth has exactly one owning Domain. Mutations go through that owner.

Derived state, caches, analytics, PubSub, provider state and UI projections are never business authority.

Business writes use the owning Ash interface. Controllers, LiveViews and workers call the owning Domain/application interface; owning application code may implement those interfaces with Ash actions. Do not use `NewYou.Repo`, raw SQL or `Ecto.Multi` write/run operations as parallel business-write paths. `mix check.architecture` enforces these boundaries (ARC-029).

Do not introduce Redis, extra services, extra Repos, ETS/process authority or speculative infrastructure without a demonstrated requirement.

Meaningful state transitions are intentional domain actions with appropriate guards, invariants, authorization, retries and idempotency.

### Defect fixes and regression proof

Every material bug, defect, security issue, or unintended behavioural regression discovered in implemented software MUST leave permanent automated regression coverage.

Where technically possible, the implementing agent MUST:

1. reproduce the defect with a focused automated test before changing the production implementation;
2. demonstrate that the test fails against the defective behaviour;
3. implement the smallest compliant fix;
4. demonstrate that the regression test passes after the fix;
5. retain that test in the permanent test suite; and
6. run the applicable broader repository verification gates to prove the correction did not introduce regressions elsewhere.

The regression test SHOULD exercise the affected behaviour or boundary as directly as practical. A test that merely asserts a configuration literal, implementation detail, or mock interaction is insufficient when the real defect can reasonably be exercised.

If a defect genuinely cannot be reproduced with a deterministic automated test, the work MUST record why in Plane, provide the strongest repeatable alternative proof available, and receive explicit reviewer acceptance of that exception.

A material defect fix without adequate regression proof is incomplete and MUST NOT receive implementation handoff or Master Gate PASS.

## Evidence

Do not guess material framework or package APIs.

Prefer, in order: repository authority; relevant generated framework skills; Tidewave/runtime evidence; version-matched official HexDocs or source; model memory last.

Tidewave is development-only. It is diagnostic tooling and never business authority.

## Plane

Plane is the mandatory execution ledger.

All material delivery work MUST be created or updated in Plane before handoff: parent and Feature Pack work, every broken-down executable implementation ticket, blockers, dependencies, bugs and defects, security, privacy and architecture concerns, discovered or deferred work, missing prerequisites, test or proof gaps, and release blockers.

Search for an existing Plane issue first. Do not create duplicates. Update the existing owner where one exists. Add dependency relations where sequencing exists.

Do not leave delivery-affecting work only in chat, PR comments, TODO comments, handoff notes or memory.

Plane tracks delivery. GitHub governed sources remain architectural and product authority; Plane never overrides them.

## Verification

`mix check` is the canonical fast gate. `mix check.deep` is the slower engineering gate.

Application CI runs `mix check` and `mix check.deep`. Foundation Smoke runs for every PR and is part of the required `Foundation Integrity` merge gate. Governance-sensitive PRs also start Foundation Full automatically as non-blocking historical evidence; the required merge gate does not wait for it. Deliberate exact-SHA certification is dispatched directly through Foundation Full. Scheduled and manual nightly hardening runs Foundation Full plus `mix check.deep` on `main`; ordinary application pushes and PRs do not run Full.

The current operational CI routing contract is `docs/development/foundation-integrity-merge-gate.md`.

Before handoff verify the exact diff, exact head SHA, relevant required checks and tests, Plane state and a clean worktree. Do not wait for non-blocking Foundation Full unless the task or governing authority explicitly requires full certification.

The implementing agent implements the authorised ticket, verifies it, updates Plane, creates the PR and provides exact evidence. It does not self-certify integration authority or silently merge. Final Master Gate review and merge recommendation are external to the implementing agent.

## Local DevCore Credentials

DO NOT ASK THE USER FOR LOCAL DB PASSWORDS OR DEVCORE-MANAGED DB VARIABLES.

If `.devcore/project.conf` exists, local DEV and TEST DB credentials are managed by DevCore:

1. Run `devcore-project doctor`; if state is missing or stale, run `devcore-project activate`.
2. Run DB-dependent commands with `devcore-project run dev -- <command>` or `devcore-project run test -- <command>`.

Never request or print a password value. The repository must not start, stop, recreate or delete shared DevCore services or volumes. Redis is not used by NewYou. Both PostgreSQL roles must remain NOCREATEDB.
