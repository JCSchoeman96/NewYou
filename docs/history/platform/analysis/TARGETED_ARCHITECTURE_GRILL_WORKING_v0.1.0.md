# Targeted Architecture Grill

**NON-AUTHORITATIVE / STAGE 4A ARCHITECTURE GRILL EVIDENCE**

> **DOES NOT AMEND PRODUCT LAW**
> **DOES NOT AMEND AR-000**
> **DOES NOT AMEND ARCHITECTURE LAW**
> **NO ARC IDENTIFIERS CREATED**
> **NO DOMAIN OWNERSHIP CREATED**
> **NO IMPLEMENTATION AUTHORISED**
> **LIVE GITHUB AUTHORITY IS CANONICAL**

- **Artifact version:** v0.1.0
- **Date:** 2026-09-04
- **Programme:** Targeted Product Amendment → FP-001 Development Entry Readiness
- **Stage:** Stage 4A — Product-Derived Architecture Grill
- **Status:** Grill complete with explicit human acceptance; pending independent review of exact PR head
- **Baseline:** `main` at `a7cd4279cfddc67bb816f512231c3f7bfc8482c2`
- **Authority:** Current GitHub `main`, routed by `docs/00_platform/README.md` and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`
- **Input stream:** Product-derived AR-000 v1.1.0 amendment only (16 governed ARQs)

## Scope and stop boundary

This file records the Architecture-level HOW decisions required to satisfy the governed Product-derived ARQs introduced by Stage 3A.2.

It does not:

- amend Product Law, Decision Register, AR-000, Architecture Law or `03_ARCHITECTURE`;
- create `ARC-*`, Domain, Feature Pack, Engineering Standard or implementation artifacts;
- begin Engineering-Policy Grill or Architecture amendment;
- invent Domain ownership for Research, Voting, Interactive Tools or Platform Member Reference.

Architecture amendment remains a later separately authorised stage. This artifact is active working input for that later stage and remains outside `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.

## Provenance streams (must remain separate)

### Stream A — Product-derived Architecture Grill input

Governed by Stage 3A.2 / AR-000 v1.1.0. Exact ARQ scope:

`ARQ-SYS-007`…`ARQ-SYS-010`, `ARQ-IAM-009`…`ARQ-IAM-013`, `ARQ-STATE-008`…`ARQ-STATE-013`, `ARQ-ASYNC-004`.

### Stream B — Independent Stage 3B input

Stage 3B classification (`working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md`) contributes:

**ZERO CURRENT INDEPENDENT ARCHITECTURE GRILL PROPOSITIONS.**

This Grill does not reopen Errors & Diagnostics, Observability refinement, Native Compute/Rustler or Engineering Quality as Architecture decisions. Those remain Engineering-Policy, deferred or already-governed per Stage 3B.

## Authority and evidence baseline

### Resolved current paths

| Class | Current path | Use in this artifact |
|---|---|---|
| Product north star | `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` | Product boundary |
| Platform Product Law | `docs/00_platform/00_PLATFORM_v1.3.0.md` | §§21M–21Q Product WHAT |
| Decision Register | `docs/00_platform/01_DECISIONS_v1.3.0.md` | DEC-294–DEC-298 |
| Open Work at baseline | `docs/00_platform/02_OPEN_WORK_v1.2.33.md` | Programme sequence before Stage 4A |
| Architecture synthesis | `docs/00_platform/03_ARCHITECTURE_v1.0.0.md` | Frozen synthesis (417 ARQ era) |
| Domain Map | `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md` | Ownership constraint only |
| ARQ evidence | `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` | 16 new ARQs |
| Architecture-law evidence | `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md` | ARC-001…ARC-327 |
| Flow evidence | `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md` | Targeted review candidates only |
| Stage 3B classification | `docs/00_platform/working/TARGETED_ARCHITECTURE_ENGINEERING_CLASSIFICATION_WORKING_v0.1.0.md` | Zero independent Architecture queue |

### Protected baseline SHA-256 values

| Path | SHA-256 |
|---|---|
| `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` | `5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20` |
| `00_PLATFORM_v1.3.0.md` | `4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445` |
| `01_DECISIONS_v1.3.0.md` | `43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96` |
| `03_ARCHITECTURE_v1.0.0.md` | `87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b` |
| `04_DOMAIN_MAP_v1.0.0.md` | `f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a` |
| `05_ROADMAP_v1.0.0.md` | `b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20` |
| `PLATFORM_OPERATING_MODEL_v1.0.1.md` | `884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811` |
| `reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md` | `971556eb0f08193a203b12612e6b96cdf8e10c0fbea194618c64c4ac06a31d91` |
| `reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md` | `a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639` |
| `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md` | `f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20` |

Stage 4A must leave those protected files and hashes unchanged.

## Coverage dispositions used in this Grill

Local working labels only (not governed identifiers):

- `EXISTING_ARCHITECTURE_SUFFICIENT`
- `EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION`
- `NEW_ARCHITECTURE_DECISION_REQUIRED`
- `DOWNSTREAM_DETAIL_ONLY`
- `UPSTREAM_CONTRADICTION_STOP`

Only the second and third dispositions may generate human Grill questions.

## Human Grill decisions

All five material questions received explicit human acceptance on 2026-09-04.

### Q1 — Bounded capability surfaces

- **ARQs:** `ARQ-SYS-007`, `ARQ-SYS-008`, `ARQ-SYS-009`
- **Recommendation:** Purpose-classified capability modes + primitive non-authority
- **Human decision:** `ACCEPT OPTION 1 WITH REFINEMENT`
- **Accepted doctrine:** Architecture preserves Product-defined distinctions between lightweight interaction/feedback and governed Research; lightweight opinion polls, Research polls and governed voting/balloting; and approved Interactive Tool types with bounded administrator configuration. Reusable forms, questions, polls, calculators, dashboards and shared UI/application primitives remain interaction/presentation mechanisms only and must not acquire shared-write business authority or decide purpose, eligibility, lifecycle, finality or consequence.
- **Refinement:** Capability/mode classification must be explicit at the governing application-operation/contract level and must not be inferred merely from UI component, route/page or reused generic primitive. This establishes shared architectural doctrine, not a shared Research/Voting/Tools store, Resource, service or Domain. Product non-promises remain: no unrestricted survey-building platform; no generic civic-election platform; no unrestricted CMS/no-code executable environment.
- **Flow impact:** `NO_MATERIAL_FLOW_IMPACT` unless later Architecture amendment introduces a new mechanism.

### Q2 — Participation identity vs uniqueness

- **ARQs:** `ARQ-IAM-009`
- **Recommendation:** Declared participation-identity contract
- **Human decision:** `ACCEPT OPTION 1 WITH REFINEMENT`
- **Accepted doctrine:** Every governed Research instrument and governed vote carries an explicit participation identity mode (Account-linked, pseudonymous or anonymous/public where applicable). Identity assurance and uniqueness/integrity assurance are separate claims. Architecture must not secretly retain Account linkage under genuine anonymity; must not treat integrity signals as stronger identity assurance than they provide; and must not describe anonymous/public voting as verified one-human-one-vote unless that assurance is genuinely provided.
- **Refinement:** Declared identity mode and allowed linkage semantics are part of the governed participation contract for the published instrument/vote configuration and must not silently change in a way that retroactively changes already-collected participation evidence. Pseudonymous linkage remains purpose-scoped and must not become a generic backdoor identity graph. Longitudinal linkage is allowed only where the declared identity mode and approved purpose permit it.
- **Flow impact:** `TARGETED_FLOW_REVIEW_REQUIRED` — primarily FLOW-01.

### Q3 — Platform Member Reference contract

- **ARQs:** `ARQ-IAM-011`, `ARQ-IAM-012` (constraints for `ARQ-IAM-013`; exact encoding remains downstream)
- **Recommendation:** External human Account reference contract
- **Human decision:** `ACCEPT OPTION 1 WITH REFINEMENT`
- **Accepted doctrine:** Platform Member Reference is a stable human-facing identifier for an individual Account. It is not database identity, authentication, authorisation, identity-verification assurance, paid Membership, subscription state, entitlement, discount authority or coupon/voucher authority. Under ordinary lifecycle there is one canonical active reference per Account: assigned on successful individual Account creation; non-secret but private-by-default; unique; normally immutable; retained on legitimate reactivation; never reassigned; permanently non-reusable after retirement/final deletion; merge leaves one canonical active reference and permanently retires the non-surviving reference. Exceptional retirement/replacement only for Product-approved security, privacy, integrity, reconciliation or equivalent operational-correctness reasons.
- **Refinement:** Allocation must be collision-safe and concurrency-correct without selecting the generation algorithm in Stage 4A. Replacement must not return the retired value to the allocatable namespace. Lookup/beneficiary association is purpose-scoped, minimum-disclosure, non-authoritative and fail-closed for authentication/authorisation/entitlement claims. Exact encoding (`VG`, alphabet, grouping, payload length, checksum/check algorithm, generator, database representation) remains deferred.
- **Flow impact:** `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-01, FLOW-02, FLOW-08, FLOW-10.

### Q4 — Versioned interactive evidence lifecycle

- **ARQs:** `ARQ-STATE-008`, `ARQ-STATE-013`
- **Recommendation:** Apply immutable-version/supersession doctrine with capability-specific edges
- **Human decision:** `ACCEPT OPTION 1 WITH REFINEMENT`
- **Accepted doctrine:** Published governed Research instruments are immutable in meaning. Persisted Research responses retain the exact instrument/question version of submission. Persisted or materially consequential Interactive Tool results retain the approved tool/calculation version that produced them. Material meaning changes create a new governed version. Correction/recalculation may establish a new interpretation/result without falsifying historical result. Architecture also preserves anonymous withdrawal limitations; participant submission versus staff annotation/classification as distinct evidence; public/anonymous tool inputs/results non-persistent by default; and Account-linked persistence only where Product value, participant expectation and approved purpose justify it.
- **Refinement:** Do not create a generic shared “Interactive Evidence” business authority, Resource, store or Domain. This is shared architectural history/versioning doctrine applied within the relevant owning capability. Shared implementation primitives later must not create shared durable business ownership. Declared participation identity mode from Q2 is part of the governed meaning of the published Research participation contract and must not silently change for responses already collected under that version.
- **Flow impact:** `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-03, FLOW-08, FLOW-11.

### Q5 — Governed voting evidence → official result → exceptions

- **ARQs:** `ARQ-STATE-009`, `ARQ-STATE-010`, `ARQ-STATE-011`
- **Recommendation:** Layered voting authority stack
- **Human decision:** `ACCEPT OPTION 1 WITH REFINEMENT`
- **Accepted doctrine:** Architecture preserves logically independent dimensions for vote rules; submission/integrity evidence (`submitted` / `accepted` / `rejected|invalidated` / `held|requires-review`); accepted tally from accepted eligible evidence; governed finalisation; official result separate from provisional counts/caches/leaderboards/Analytics; reward/entitlement consequence initiated from the official outcome but independently established by the owning commercial/entitlement capability; and exception/adjudication policy covering ties, disqualification, material integrity failure, outage/disruption, cancellation, extension, rerun and governed operator adjudication. Individual voter identity and ballot choice remain private by default. Integrity evidence does not upgrade identity assurance.
- **Refinement:** These are logical authority/state dimensions, not a requirement for seven Resources/tables/status columns. Architecture must not collapse them into one generic status for convenience. Finalisation must be durable, auditable and retry/idempotency-safe against a clearly identified governed rule/evidence basis. Later approved correction must be explicit and evidence-bearing. Reward/entitlement handoff must tolerate retry/duplication without duplicate commercial authority. FLOW-09 is included only if later Architecture amendment determines voting burst/concurrency materially exercises an unproven flow assumption; do not rerun merely by analogy.
- **Flow impact:** `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-02, FLOW-06, FLOW-11.

## 16-ARQ closure matrix

| ARQ | Coverage disposition | Relevant existing ARCs / Architecture | Human question | Accepted human answer | Likely later Architecture amendment treatment | Downstream-only detail | Flow-impact flag |
|---|---|---|---|---|---|---|---|
| `ARQ-SYS-007` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-043`, `049`, `124` | Q1 | Accept option 1 + refinement | Descriptive capability-mode doctrine amendment/addition; no ARC allocated here | Domain ownership, Resources, schemas, admin UX | `NO_MATERIAL_FLOW_IMPACT` |
| `ARQ-SYS-008` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-032`, `049`, `055` | Q1 | Accept option 1 + refinement | Same capability-mode doctrine as SYS-007 | Competition policy text, widget catalogs | `NO_MATERIAL_FLOW_IMPACT` |
| `ARQ-SYS-009` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-044`, `045`, `190` | Q1 | Accept option 1 + refinement | Same capability-mode doctrine; bounded admin configuration / no-code non-promise | Sandbox mechanics, validation, authoring representation | `NO_MATERIAL_FLOW_IMPACT` |
| `ARQ-SYS-010` | `EXISTING_ARCHITECTURE_SUFFICIENT` | `ARC-046`, `047`, `049`, `055`, `061`, `152`, `168`, `231`; `03_ARCHITECTURE` §5 | None | N/A — existing ownership/handoff HOW already sufficient; Product ARQ applies it to Research/Voting/Tools/PMR | Naming/traceability only if amendment stage chooses explicit application language | Cross-capability APIs, Domain owners | `NO_MATERIAL_FLOW_IMPACT` |
| `ARQ-IAM-009` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-037`, `144`, `150` | Q2 | Accept option 1 + refinement | Declared participation-identity contract | CAPTCHA/fingerprint/cookie/device/rate-limit/verification thresholds | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-01 |
| `ARQ-IAM-010` | `EXISTING_ARCHITECTURE_SUFFICIENT` | `ARC-038`, `039`, `042`, `118`, `123`, `126`, `203`; `03_ARCHITECTURE` §§6.2–6.3 | None | N/A — purpose/minimise/field-policy doctrine already locks the HOW | Optional application language only | Clinical/privacy policy, exact access mechanisms, cohort engines | `NO_MATERIAL_FLOW_IMPACT` |
| `ARQ-IAM-011` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-098`, `110`, `138`, `241` | Q3 | Accept option 1 + refinement | External human Account reference lifecycle/non-authority contract | Generator algorithm, Domain owner | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-01, FLOW-08 |
| `ARQ-IAM-012` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-039`, `042`, `110`, `046` | Q3 | Accept option 1 + refinement | Minimum-disclosure lookup/beneficiary association under PMR contract | Lookup UX, response shaping, throttling | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-02, FLOW-10 |
| `ARQ-IAM-013` | `DOWNSTREAM_DETAIL_ONLY` | Product §21P.4 constraints + `ARC-098` external-ID allowance | None | N/A — exact encoding deferred by Product; Stage 4A freezes no format | Proof/JIT representation selection under Product constraints | Prefix, alphabet, grouping, length, check algorithm, DB representation | `NO_MATERIAL_FLOW_IMPACT` |
| `ARQ-STATE-008` | `EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION` | Strong: `ARC-065`, `191`, `192`, `197`; gaps closed by Q4 | Q4 | Accept option 1 + refinement | Apply version/supersession doctrine to Research with anonymous-withdrawal and annotation edges; no shared Interactive Evidence Domain | Retention durations, Resources, authoring UI | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-03, FLOW-08, FLOW-11 |
| `ARQ-STATE-009` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-061`, `068`, `124`, `144` | Q5 | Accept option 1 + refinement | Vote rules + submission/integrity evidence dimensions | Anti-abuse thresholds, exact state vocabularies in Domain Law | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-11 |
| `ARQ-STATE-010` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-046`, `061`, `168`, `231` | Q5 | Accept option 1 + refinement | Tally ≠ official result ≠ fulfilment authority separation | Fulfilment workflow details, result Resource names | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-02, FLOW-06 |
| `ARQ-STATE-011` | `NEW_ARCHITECTURE_DECISION_REQUIRED` | Partial: `ARC-041`, `124`, `129`, `130` | Q5 | Accept option 1 + refinement | Finalisation/exception/adjudication/privacy/safety contract | Competition wording, operator UX, clinical safety review | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-11 |
| `ARQ-STATE-012` | `EXISTING_ARCHITECTURE_SUFFICIENT` | `ARC-066`, `233`, `237`, `238`, `240`, `241`, `242`; `03_ARCHITECTURE` §11 | None | N/A — deletion/history separation already locks the HOW; Research/Voting are category applications | Optional naming under deletion contracts | Retention schedules, anonymisation schemas | `NO_MATERIAL_FLOW_IMPACT` |
| `ARQ-STATE-013` | `EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION` | Strong: `ARC-044`, `065`, `046`; edges closed by Q4 | Q4 | Accept option 1 + refinement | Apply version/persistence doctrine to consequential tool results without Content Domain ownership | Storage, recalculation UX, version records | `TARGETED_FLOW_REVIEW_REQUIRED` — FLOW-03, FLOW-11 |
| `ARQ-ASYNC-004` | `EXISTING_ARCHITECTURE_SUFFICIENT` | `ARC-146`, `155`, `170`, `171`; `03_ARCHITECTURE` §8 Class B | None | N/A — explicit durable consequence / notification-intent separation already forbids universal monitoring-by-default | Optional application language only | Notification mechanism, monitoring service selection, Domain owner | `NO_MATERIAL_FLOW_IMPACT` |

### Disposition counts

| Disposition | Count |
|---|---:|
| `NEW_ARCHITECTURE_DECISION_REQUIRED` | 9 |
| `EXISTING_ARCHITECTURE_NEEDS_EXTENSION_DECISION` | 2 |
| `EXISTING_ARCHITECTURE_SUFFICIENT` | 4 |
| `DOWNSTREAM_DETAIL_ONLY` | 1 |
| `UPSTREAM_CONTRADICTION_STOP` | 0 |
| **Total** | **16** |

## Existing Architecture closures (no new decision)

### `ARQ-SYS-010`

Existing Domain Interaction Doctrine already requires that durable business truth has one owner, cross-boundary writes enter the owning contract (`ARC-046`), relationships do not transfer mutation authority (`ARC-047`), shared technical primitives are not shared business-semantics dumping grounds (`ARC-049`), Phoenix components are presentation not authority (`ARC-055`), and projections/provider evidence are not business truth (`ARC-061`/`168`/`231`). The Product ARQ applies that HOW to Research responses, tool results, votes, incentives and shared primitives. No material Architecture choice remains.

### `ARQ-IAM-010`

Purpose/relationship/scope authorisation (`ARC-038`/`118`), field privacy and minimum-data loading (`ARC-039`/`042`/`123`), purpose-specific consent (`ARC-126`) and minimum-signal health personalisation (`ARC-203`) already define the privacy/access HOW. Remaining targeting/publication/clinical detail is expert/Domain/policy work.

### `ARQ-IAM-013`

Product Law already locks human-usability, non-semantic, non-obviously-sequential, error-detection-compatible and namespace constraints while forbidding format freeze. `ARC-098` already allows a non-UUIDv7 external/public identifier. Exact encoding is deliberately deferred.

### `ARQ-STATE-012`

Business lifecycle and data lifecycle are separate (`ARC-066`/`233`). Full deletion uses capability-owned deletion contracts (`ARC-240`) with irreversible anonymisation where permitted (`ARC-237`) and without silently rewriting historically valid facts. Research/Voting history after Account deletion is a category application of that law.

### `ARQ-ASYNC-004`

Mandatory follow-on work is an explicit Class B durable consequence (`ARC-146`/`155`). Notification intent is separate from the originating business event and revalidated before delivery (`ARC-170`/`171`). Free-text Research submission therefore cannot imply a universal continuous monitoring promise under existing Architecture.

## Architecture delta for later amendment (descriptive; no ARC numbers)

The later Architecture amendment stage, if authorised, will need to consider durable Architecture Law language for:

1. Purpose-classified bounded capability modes for Research, Voting and Interactive Tools, with primitive non-authority and explicit application-operation classification (Q1).
2. Declared participation-identity contract separating identity assurance from uniqueness/integrity assurance, including non-retroactive contract meaning (Q2).
3. Platform Member Reference as an external human Account reference with assignment, uniqueness, non-reuse, merge retirement, exceptional replacement and minimum-disclosure non-authoritative lookup (Q3).
4. Application of immutable-version/supersession doctrine to Research instruments/responses and consequential Interactive Tool results, including anonymous-withdrawal honesty, annotation distinguishability and tool persistence defaults, without creating a shared Interactive Evidence Domain (Q4).
5. Layered voting authority/state dimensions: rules, submission evidence, accepted tally, finalisation, official result, fulfilment handoff and exception/adjudication policy (Q5).

No `ARC-*` identifier is allocated in Stage 4A.

## Downstream-only inventory

Deliberately left for Domain Law, expert policy, JIT dossier, Engineering Policy or implementation:

- Domain ownership for Research, Voting, Tools and PMR;
- Ash Resources/tables/schemas;
- exact PMR encoding/generator/check algorithm/DB representation;
- CAPTCHA, fingerprinting, cookies, device signals, rate-limit thresholds and verification providers;
- anti-abuse thresholds and competition wording;
- retention durations;
- admin authoring UX and recalculation UX;
- sandbox/validation mechanisms for bounded tool configuration;
- fulfilment workflow internals beyond the owner-mediated handoff boundary;
- Stage 3B Engineering-Policy queue items.

## Flow-pressure summary

| Decision / ARQ set | Flag | Existing FLOWs |
|---|---|---|
| Q1 / SYS-007…009 | `NO_MATERIAL_FLOW_IMPACT` | — |
| Q2 / IAM-009 | `TARGETED_FLOW_REVIEW_REQUIRED` | FLOW-01 |
| Q3 / IAM-011…012 | `TARGETED_FLOW_REVIEW_REQUIRED` | FLOW-01, FLOW-02, FLOW-08, FLOW-10 |
| Q4 / STATE-008, STATE-013 | `TARGETED_FLOW_REVIEW_REQUIRED` | FLOW-03, FLOW-08, FLOW-11 |
| Q5 / STATE-009…011 | `TARGETED_FLOW_REVIEW_REQUIRED` | FLOW-02, FLOW-06, FLOW-11 |
| Closed-by-existing (SYS-010, IAM-010, IAM-013, STATE-012, ASYNC-004) | `NO_MATERIAL_FLOW_IMPACT` | — |

No FLOW was rerun or rewritten in Stage 4A. No new FLOW identifiers were created. Actual targeted flow closure belongs with later Architecture amendment if material.

## Contradiction and Stage 3B confirmation

- Upstream Product/Architecture contradictions found: **0**
- Independent Stage 3B Architecture Grill propositions reintroduced: **0**
- Architecture amendment begun: **no**
- Engineering-Policy Grill begun: **no**
- `ARC-*` created: **none**

## Programme routing after Stage 4A

```text
Architecture Grill: COMPLETE
Engineering-Policy Grill: NOT_STARTED / NEXT
Architecture amendment: NOT_STARTED
Domain/Roadmap/Atlas/HARDEN-02/FP-001 reconciliation: DOWNSTREAM / NOT CURRENT
Executable development: BLOCKED
```

## Mandatory STOP

After the Stage 4A PR opens, work must **STOP** pending independent review of the exact PR head.

Do not merge this PR, begin Engineering-Policy Grill, create ARC identifiers, amend Architecture Law, modify `03_ARCHITECTURE`, create Engineering Standards, amend Domain Map or Roadmap, reconcile Delivery Atlas, execute HARDEN-02, modify FP-001, or implement any capability.
