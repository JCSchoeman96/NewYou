# NewYou Engineering Contract

This file is manually owned by NewYou. Generated framework documentation never replaces it.

## Development Workflow

- ALWAYS make changes and implementations on a git branch.
- ALWAYS create a PR after work and implementations so the work can be reviewed.
- When a PR is merged and local state is synced, leave the repository clean and ready for the next agent.
- Use a worktree when needed and available.
- Do not merge unless explicitly authorised.

## Authority split

The live GitHub repository is canonical for **durable governance and implementation evidence**. Plane is canonical for **live execution state beneath that durable law**.

For current durable routing, start with:

1. `docs/00_platform/README.md`; and
2. `docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json`.

Do not use `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` as the live delivery router. It is the frozen pre-WELL-66 historical/provenance baseline used by Foundation Full.

Durable authority order is:

Product Law → Architecture Law → Domain Law → governing Roadmap → applicable Operating/Frontend/Engineering/Delivery supporting authority → semantic Feature/JIT/proof contracts where required → implementation.

The local agent is a planner and implementer, not a source of Product, Architecture, Domain or Roadmap law. It may make JIT implementation choices only where authority intentionally leaves them open. Never improvise missing product, architecture, domain, clinical, legal, commercial, safety or entitlement law.

Durable governance is read-only during ordinary implementation. Update it only for a deliberate governed decision or when implementation supplies conclusive evidence of an upstream governance contradiction. Do not silently repair upstream law in implementation.

Plane owns the active delivery-roadmap projection, work-item state/priority, blockers, dependencies, sequencing, acceptance criteria, discovered/deferred work, review/merge state and implementation readiness. Plane may not silently amend or override durable GitHub law. If they conflict, STOP the affected work, record the conflict in Plane and reconcile the smallest correct upstream authority.

`docs/00_platform/02_OPEN_WORK_v1.2.90.md` is the final frozen legacy Open Work snapshot. It is historical evidence only after WELL-66; never use it as live execution authority and never create a successor merely to mirror ticket state.

Working/derived artifacts such as Delivery Atlas, Skeleton, HARDEN, JIT dossiers and proof contracts change when their **semantic contract** changes. Existing ticket/status prose in them is freeze-time/historical context unless the semantic contract itself makes it durable. Live execution status comes from Plane.

## Plane and Symphony execution boundary

Plane project `WELL` is the authoritative execution ledger and delivery roadmap beneath durable GitHub law.

The only state that authorises a fresh Symphony/local implementation agent to begin a ticket is **`Ready`**. The existing Ready state is the Symphony-routable implementation state.

- `Backlog`, `Planning` and `Blocked` are not executable.
- `In Progress`, `In Review`, `Changes Requested`, `Ready to Merge` and `Merging` describe work already in the delivery/review lifecycle; they are not permission to pull unrelated scope.
- `Done` is terminal execution state after required post-merge/resulting-main reconciliation.

Search Plane before creating work. Do not create duplicates. All material delivery work belongs in Plane: active slice/Feature Pack work, executable tickets, blockers, dependencies, bugs/defects, security/privacy/architecture issues, discovered/deferred work, test/proof gaps and release blockers.

Keep Plane focused. Do not pre-create every speculative future implementation task. Maintain the active delivery projection and near-term decomposition needed to identify exact next work.

Do not leave delivery-affecting work only in chat, PR comments, TODO comments, handoff notes or memory.

## Reconnaissance and proportional planning

Before `/grilling`, `to-spec`, `to-tickets` or material implementation, inspect the relevant live state:

1. `docs/00_platform/README.md` and `CURRENT_AUTHORITY_ROUTER_v1.0.0.json`;
2. applicable Product/Decision, Architecture, Domain, Roadmap, Operating, Frontend, Engineering and Delivery authority;
3. the relevant semantic Feature Pack/JIT/proof contracts;
4. live Plane work, blockers, dependencies and ticket acceptance criteria;
5. actual code, tests, migrations and dependencies.

Follow evidence only as far as the task requires; do not load the entire historical archive by default.

Use the lightest process that safely resolves the work:

- Narrow, settled single-purpose work: one focused Plane ticket.
- Major slice with material ambiguity: repository reconnaissance → `/grilling`.
- `to-spec`: only when reconnaissance/grilling proves a durable implementation contract is genuinely missing.
- `to-tickets`: only when decomposition creates independent testable/reviewable parts, necessary sequencing or materially safer delivery.
- Do not re-grill, re-spec or re-ticket settled decisions without new evidence, contradiction or changed scope.

Only dependency-cleared, adequately specified work should move to `Ready`.

Use focused, test-first development and applicable repository checks for material implementation or behaviour work.

## Material question classification

Classify material questions and discoveries before expanding scope:

- `LOCKED`: current authority already answers it; follow it.
- `JIT IMPLEMENTATION CHOICE`: authority intentionally leaves it open; choose the simplest compliant implementation and test it.
- `UPSTREAM GOVERNANCE CONTRADICTION`: implementation conclusively exposes missing/conflicting Product, Architecture, Domain, Roadmap, ownership, lifecycle, security, privacy, safety, entitlement or another expensive-to-reverse governed semantic. STOP the affected work, record the blocker/evidence in Plane and amend the smallest correct upstream authority before continuing.

Ordinary implementation learning does not become governance merely because it was discovered during coding.

## Required Skills

Before implementation, use `.agents/skills/project-implementation/SKILL.md`.

Before handoff or merge recommendation, use `.agents/skills/code-change-verification/SKILL.md`.

Load generated framework skills under `.agents/skills/` only when relevant.

Use Igniter first for supported structural or package changes; hand-edit only where Igniter does not safely support the change.

## Mandatory Ash Capability Evaluation

Ash is the default application framework. Do not choose bespoke Elixir, Ecto, OTP or infrastructure mechanisms merely because an Ash capability or extension was not considered.

For every Grill, `to-spec`, implementation plan and implementation ticket that touches business behaviour, durable state, authorization, authentication, lifecycle, history, async work, audit/evidence, cross-Domain coordination or an Ash-backed web flow:

1. **Load the Ash skill first.** Read `.agents/skills/ash-framework/SKILL.md` and relevant generated references before selecting the mechanism.
2. **Perform an explicit Ash capability/extension evaluation.** Do not limit it to packages already present in `mix.exs`. Verify plausible capabilities against current official Ash/HexDocs/Hex sources.
3. **Record material decisions in the Grill/spec/ticket where needed.** Use `USE`, `NOT APPLICABLE`, `DEFER`, or `BLOCKED / NEEDS AUTHORITY` with the requirement, reason, governing authority and primary source checked. A ticket must not move to Ready while a material Ash decision is unresolved.
4. **At minimum consider relevant Ash surfaces.** Domains/Resources/actions/code interfaces, policies/authorization, identities/constraints, relationships, calculations/aggregates, changes/validations, Ash Signals, Temporal Resources, AshPostgres, AshAuthentication/Phoenix integration, AshPhoenix, AshOban, AshStateMachine, AshCloak, AshArchival/AshPaperTrail and any other current official extension whose capability directly matches the ticket. This is a minimum review set, not permission to install every package.
5. **Signals require an explicit decision.** For cross-Domain reactions, event-like coordination or post-action reactions, explicitly evaluate Ash Signals. If Signals are not selected, state why. Signals are coordination only: they never become durable business authority, a universal event bus or a substitute for the receiving Domain's owning Ash interface.
6. **Temporal Resources require an explicit decision when time/history is material.** For historical/as-of truth, correction, reconstruction or effective-period requirements, explicitly evaluate Ash Temporal Resources. Do not introduce Temporal merely as a second audit/history authority when the governed lifecycle/evidence model already owns that truth. If a real capability-specific temporal requirement conflicts with durable authority, STOP and route the contradiction upward.
7. **Prefer a fitting Ash mechanism over bespoke plumbing** when it satisfies the requirement without violating governing law. If bespoke machinery is selected instead, document why the Ash option is insufficient or forbidden.
8. **Evaluation is not installation authority.** Do not add a package because it exists or looks convenient. A new dependency requires a concrete requirement, compatibility with the locked stack, current stable-version/API verification from primary sources and any required Architecture/Security/Domain approval.
9. **Re-evaluate at implementation boundary** when versions, capabilities, scope or authority changed since planning.

## Authorization and capability authority — mandatory STOP rule

- Resolve authorization through governed roles, scopes and applicable relationships.
- Capabilities belong to governed roles/scopes/relationships; named people may be subjects of explicit grants, never definitions of capability authority.
- Agents MUST NOT attach a business capability directly to a named user. A proposed direct user-to-capability shortcut is an `UPSTREAM GOVERNANCE CONTRADICTION`: STOP and escalate.
- Governed bootstrap may establish the first explicit role/scope grants, but bootstrap does not hold business capability. After bootstrap, sensitive grants require the appropriate role-based independent approver, distinct from the subject.
- Platform Administrator does not imply expert authority. Developer, founder or administrator status alone does not create Domain authority.
- Multiple valid roles on one identity are expected and supported.
- Super Admin is break-glass and not a universal bypass.
- An unresolved approver authority is a STOP condition.

## Engineering Invariants

Every durable business truth has exactly one owning Domain. Mutations go through that owner.

Derived state, caches, analytics, PubSub, provider state and UI projections are never business authority.

Business writes use the owning Ash interface. Controllers, LiveViews and workers call the owning Domain/application interface; owning application code may implement those interfaces with Ash actions. Do not use `NewYou.Repo`, raw SQL or `Ecto.Multi` write/run operations as parallel business-write paths. `mix check.architecture` enforces these boundaries (ARC-029).

Do not introduce Redis, extra services, extra Repos, ETS/process authority or speculative infrastructure without a demonstrated requirement.

Meaningful state transitions are intentional domain actions with appropriate states, guards, invariants, side effects, terminal states, authorization, concurrency behaviour, idempotency, retries and recovery/reconciliation.

## Defect fixes and regression proof

Every material bug, defect, security issue or behavioural regression must leave permanent regression coverage. Where technically possible, reproduce it with a focused failing automated test before changing production code, then implement the fix and prove that test passes. If deterministic automation is genuinely impossible, record the reason and strongest repeatable alternative proof in Plane for explicit reviewer acceptance. A material defect fix without adequate regression proof is not complete.

## Evidence

Do not guess material framework or package APIs.

Prefer, in order: current repository authority; relevant generated framework skills; Tidewave/runtime evidence; version-matched official HexDocs/source; model memory last.

Tidewave is development-only diagnostic tooling and never business authority.

## CI and verification

`mix check` is the canonical fast engineering gate. `mix check.deep` is the slower engineering gate.

Foundation Smoke runs on every PR and validates `CURRENT_AUTHORITY_ROUTER_v1.0.0.json` plus merge-gate topology. Application CI runs for routed engineering changes.

Foundation Full is historical/provenance evidence: it validates the historical Python governance suite and the frozen `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`. Material governance/provenance/workflow PRs start Full automatically as non-blocking evidence; nightly/manual exact-SHA certification also runs it. Ordinary Plane status changes produce no repository PR and therefore no Full run.

The operational CI topology is `docs/development/foundation-integrity-merge-gate.md`.

Before handoff, verify the exact diff, exact head SHA, relevant required checks/tests and current Plane state. Do not wait for non-blocking Foundation Full unless the task or governing authority explicitly requires full certification, but investigate any WELL-66-caused Full regression rather than dismissing it.

The implementing agent implements the authorised Ready ticket, verifies it, updates Plane, creates the PR and provides exact evidence. It does not self-certify integration authority or silently merge.

Final Master Gate review independently verifies the exact PR head, complete diff, durable authority, Plane acceptance contract, relevant lifecycle/ownership/security/privacy/persistence behaviour and exact-head CI before recommending merge. Any head change invalidates prior exact-head certification.

Merge alone does not complete delivery. Verify resulting-main SHA/tree, candidate integration/no drift and required resulting-main CI/proof before moving work to Done or opening dependent work.

## Local DevCore Credentials

DO NOT ASK THE USER FOR LOCAL DB PASSWORDS OR DEVCORE-MANAGED DB VARIABLES.

If `.devcore/project.conf` exists, local DEV and TEST DB credentials are managed by DevCore:

1. Run `devcore-project doctor`; if state is missing or stale, run `devcore-project activate`.
2. Run DB-dependent commands with `devcore-project run dev -- <command>` or `devcore-project run test -- <command>`.

Never request or print a password value. The repository must not start, stop, recreate or delete shared DevCore services or volumes. Redis is not used by NewYou. Both PostgreSQL roles must remain NOCREATEDB.
