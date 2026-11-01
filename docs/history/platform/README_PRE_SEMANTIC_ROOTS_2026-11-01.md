# NewYou Platform Documentation

This directory contains NewYou's durable governance, supporting authority, semantic delivery contracts and historical evidence.

The live routing contract is intentionally small. **Durable law lives in GitHub; live execution state lives in Plane.** Do not use historical status prose or the final Open Work snapshot as a second delivery ledger.

## Current routing

Start with `CURRENT_AUTHORITY_ROUTER_v1.0.0.json`. It is the lean current-authority router used by agents and Foundation Smoke.

For durable governance, read only what the task requires in this order:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.13.0.md`
3. `01_DECISIONS_v1.13.0.md`
4. `03_ARCHITECTURE_v1.1.1.md`
5. `04_DOMAIN_MAP_v1.2.0.md`
6. `05_ROADMAP_v1.2.5.md`
7. `PLATFORM_OPERATING_MODEL_v1.3.0.md`
8. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when frontend/public-experience scope makes it relevant

The current Product/Decision successors include approved decisions through DEC-320.

Current deep-reference evidence is also routed by the current router. Load these only when exact source tracing, identifier-level reasoning or legislative Architecture evidence is genuinely required; they are not additional default governing roots:

- `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`
- `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`
- `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`

Supporting authority is routed by the current router and presently includes:

- `reference/ENGINEERING_STANDARDS_v1.0.1.md`
- `reference/DELIVERY_GOVERNANCE_STANDARD_v1.1.0.md`

The current P8-05 verification-message semantic contract is `docs/execution/p8-05-registration-jit-spec.md`; its development-only EN/AF fixture and separate runtime/release evidence are recorded in `working/content_media/verification_messages/VERIFICATION_MESSAGE_EVIDENCE_PACKET_v0.2.0.json`.

Durable authority precedence remains Product Law → Architecture Law → Domain Law → governing Roadmap → applicable supporting Operating/Frontend/Engineering/Delivery authority → semantic Feature/JIT/proof contracts → implementation.

## Plane is live execution authority

Plane project `WELL` is authoritative for current delivery state beneath durable GitHub law: active delivery-roadmap projection, exact work items, priorities, blockers, dependencies, sequencing, acceptance criteria, discovered/deferred work, review/merge state and implementation readiness.

The only Symphony/local-agent executable state is **`Ready`**. Symphony and local coding agents consume focused Ready Plane tickets; they do not infer scope from governance prose.

If Plane conflicts with durable GitHub authority, stop the affected work and reconcile the smallest correct upstream authority. Plane never silently changes Product, Architecture, Domain, Roadmap, security, privacy, safety, entitlement or other governed law.

## Planning proportionality

For narrow work whose authority and acceptance criteria are settled, use one focused Plane ticket.

For major slices, perform repository reconnaissance first. Use `/grilling` only where material ambiguity exists. Use `to-spec` only if a durable implementation contract is genuinely missing. Use `to-tickets` only when decomposition produces independently testable/reviewable work or necessary sequencing. Put the resulting executable work in Plane and move only dependency-cleared work to Ready.

Do not pre-populate Plane with speculative future implementation tasks merely for completeness.

## Implementation discoveries

Classify material discoveries as defined in `reference/DELIVERY_GOVERNANCE_STANDARD_v1.1.0.md`:

- `LOCKED` — current authority already answers it.
- `JIT IMPLEMENTATION CHOICE` — intentionally open implementation detail; choose the simplest compliant option.
- `UPSTREAM GOVERNANCE CONTRADICTION` — conclusive missing/conflicting upstream law, ownership, lifecycle, security/privacy/safety or another expensive-to-reverse governed semantic; stop the affected work, record the blocker in Plane and amend the smallest correct upstream authority.

Ordinary implementation learning does not require a governance amendment.

## Open Work is frozen legacy

`02_OPEN_WORK_v1.2.90.md` is the final **frozen legacy** Open Work snapshot. Its SHA-256 is pinned in the current router.

It preserves the pre-WELL-66 planning state for historical evidence only. It is not live execution authority and requires no successor for status-only changes.

Ready/In Progress/Blocked/Done movement, dependency changes, PR/review state and ordinary discovered work are Plane-only.

The pre-transition README that routed Open Work and mirrored ticket status is preserved byte-identically at `archive/README_PRE_WELL66_2026-10-30.md`.

## Semantic working artifacts

`working/` contains semantic delivery/planning contracts and derived evidence. Current semantic routes are listed in `CURRENT_AUTHORITY_ROUTER_v1.0.0.json`.

Delivery Atlas, Feature Pack Skeleton, HARDEN, JIT dossiers, proof contracts and similar artifacts change when their **semantic** meaning changes. They are not status dashboards and do not get successors merely because Plane status, blockers, dependencies or PR state changed.

Existing status prose inside those artifacts is freeze-time/historical context unless the semantic contract itself makes the statement durable. For current status, use Plane.

## Historical evidence and Foundation Full

`CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` is the frozen pre-WELL-66 historical/provenance integrity baseline. Foundation Full continues to validate that manifest and the historical governance suite.

It is no longer the live current-delivery router. Do not edit it merely to reflect Plane state.

`archive/` remains historical evidence. Do not treat archived material as current law merely because a current document cites it for provenance.

## CI and review

- Foundation Smoke always validates the lean current router and required merge-gate topology.
- Application CI runs for engineering changes.
- Foundation Full is historical/provenance evidence for material governance/provenance/workflow changes and nightly/manual certification; it is non-blocking unless a specific contract requires it.
- Exact-head Master Gate review remains mandatory for material PRs.
- Merge is not completion: resulting-main SHA/tree and required CI/proof must be verified before Plane is reconciled to Done or dependent work is opened.

See `docs/development/foundation-integrity-merge-gate.md` for CI topology and `reference/DELIVERY_GOVERNANCE_STANDARD_v1.1.0.md` for the complete delivery-governance contract.
