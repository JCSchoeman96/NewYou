# Delivery Atlas working v0.1.0

- **Artifact:** `ATLAS-02`
- **Document status:** **DERIVED DELIVERY PLANNING ARTIFACT**
- **Working state:** **WORKING / NON-AUTHORITATIVE**
- **Authority boundary:** **DOES NOT MODIFY PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW**
- **Implementation boundary:** **DOES NOT AUTHORISE IMPLEMENTATION**
- **Purpose:** Define the first medium-resolution delivery-navigation contract for the complete approved NewYou roadmap.
- **Scope:** Feature Pack relationships, shared capability movement, lifecycle coverage, journeys, cross-domain interaction, integrations, measurement, risk, proof, hardening and future-extension visibility.
- **Current content state:** ATLAS-01 contract plus the ATLAS-02 Feature Pack Portfolio Register. The other Atlas views remain unpopulated. No Feature Pack preparation, standalone domain inventory or matrix, lifecycle register, journey analysis or implementation detail is created by ATLAS-02.
- **Freeze state:** Not frozen. A later freeze requires a separate governance decision.

This document is the initial Delivery Atlas working artifact. It gives later delivery planning a common set of views and labels and defines the controlled lifecycle that moves an approved roadmap outcome through preparation, implementation, evidence, handoff and the next delivery decision. It leaves implementation-grade design to the affected Feature Pack and just-in-time (JIT) Domain Dossiers.

The working artifact remains outside `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` unless an explicit repository governance decision requires a later metadata change. ATLAS-01 and ATLAS-02 do not change that manifest.

---

# 1. Authority, purpose and boundaries

## 1.1 Authority hierarchy

The Delivery Atlas is subordinate to every upstream authority. The governing delivery chain is:

```text
Product Law
    → Architecture Law
    → Domain Law
    → Roadmap
    → Delivery Atlas
    → Feature Pack Contracts
    → JIT Domain Dossiers
    → Architectural Proof
    → Vertical Slices
    → Horizontal Hardening
    → Release / Readiness
```

The current sources that establish this chain are:

| Authority level | Current source | Atlas relationship |
|---|---|---|
| Product Law | `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`; `docs/00_platform/00_PLATFORM_v1.2.1.md`; `docs/00_platform/01_DECISIONS_v1.2.2.md` | Defines product purpose, approved outcomes, policy, MVP boundaries, non-negotiables and formal gates. |
| Architecture Law | `docs/00_platform/03_ARCHITECTURE_v1.0.0.md` and the accepted Architecture Law represented by it | Defines architectural authority, state authority, interaction rules, failure behaviour, performance doctrine and deferred mechanisms. |
| Domain Law | `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md` | Defines who owns durable business truth and the domain-level dependency direction. |
| Roadmap | `docs/00_platform/05_ROADMAP_v1.0.0.md` | Defines approved delivery phases, Feature Pack outcomes, dependencies, gates and sequencing. |
| Planning tracker | `docs/00_platform/02_OPEN_WORK_v1.2.28.md` | Tracks unresolved gates, planning sequence and development stop conditions. It does not outrank Product, Architecture, Domain or Roadmap authority. |
| Supporting cross-cutting contract | `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md` | Supplies stable operating workflow guidance beneath the four upstream law levels. |
| Supporting cross-cutting contract | `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` | Supplies frontend, interaction, accessibility, public-experience and measurement guidance beneath the four upstream law levels. |
| Routing and integrity evidence | `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` | Routes current and reference documents and records integrity expectations. It does not create a new authority layer. |

`PLATFORM_OPERATING_MODEL` and `FRONTEND_EXPERIENCE_SYSTEM` support Atlas work when their concerns are in scope. Neither may override Product Law, Architecture Law, Domain Law or the Roadmap.

## 1.2 Purpose

The Atlas exists to keep the mature platform and the approved delivery route visible at the same time. It may show:

- what a Feature Pack introduces, reuses, extends or composes;
- which domains participate in a delivery outcome;
- where a lifecycle first appears and where its full specification becomes mandatory;
- how participant, staff and frontend journeys progress;
- how authority and derived projections move across boundaries;
- which integrations, measurement concerns, safety controls, proof obligations and hardening categories become relevant;
- which future extensions have a legitimate approved seam;
- which dependencies and risks cross Feature Pack boundaries; and
- what JIT planning a later Feature Pack will need.

The Atlas is a delivery map, not a second Product, Architecture, Domain or Roadmap document. It may point to those sources and derive relationships from them. It may not create a new rule by implication.

## 1.3 Scope boundary

ATLAS-01 defined the views, labels, entry rules and STOP rules for the complete approved roadmap. ATLAS-02 populates only the Feature Pack Portfolio Register. Later Atlas work may populate another view only from current upstream authority, approved evidence and the relevant governance decision.

The Atlas must preserve these boundaries:

1. Product Law defines what NewYou is allowed and expected to do.
2. Architecture Law defines how the platform may make those outcomes true.
3. Domain Law defines which domain owns each durable business truth.
4. The Roadmap defines when an approved outcome is sequenced and what it unlocks.
5. The Atlas makes delivery relationships visible without changing any of the above.
6. JIT planning fixes implementation semantics only for an approved, affected Feature Pack.

## 1.4 Explicit non-authority

The Atlas must not:

- amend, reinterpret or silently repair Product, Architecture, Domain or Roadmap authority;
- turn a supporting operating or frontend rule into a higher authority;
- choose a Feature Pack outcome, scope or gate that is not already approved upstream;
- create a new business domain, shared-write owner or authoritative dependency;
- authorise Phase 7, FP-001 preparation, Architectural Proof, Vertical Slices, Horizontal Hardening or release work;
- create a JIT Domain Dossier, TB, VS, HH or TOON;
- treat a delivery seam as an implementation design; or
- use completeness of the Atlas as a reason to pull future capability into the current delivery stage.

## 1.5 Architectural or delivery seam versus implementation design

An **architectural or delivery seam** is a visible relationship that later work must respect. Examples include a domain-owned fact read by another domain, a capability reused by more than one Feature Pack, a lifecycle that needs a later full specification, or a proof boundary that must be exercised under an approved task.

An **implementation design** chooses the concrete mechanism that realizes that relationship. It includes exact Ash Resource or action names, schemas, tables, columns, indexes, keys, TTLs, queues, topics, modules, routes, components, packages, versions, deployment sizing and source code.

```text
architectural / delivery seam != implementation design
```

The Atlas may record the first. It must defer the second unless an upstream source has already frozen the exact detail.

---

# Delivery Lifecycle Governance

## Lifecycle purpose and operating flow

The Delivery Atlas governs how an approved roadmap outcome moves from a delivery relationship into implementation and returns as verified evidence. It makes the required handoffs and review points visible without authorising implementation or creating lower-level contracts.

The operating flow is:

```text
Roadmap
    → Delivery Atlas
    → Feature Pack preparation
    → TB / VS / HH preparation
    → Grill-Me review
    → Implementation
    → Evidence collection
    → Implementation handoff
    → Continuation review
    → Next delivery decision
```

The Roadmap supplies the approved outcome, scope, sequencing, dependencies and gates. The Atlas derives the delivery relationships and identifies the next required planning boundary. Feature Pack preparation turns an approved outcome into a controlled implementation boundary. TB, VS and HH preparation defines the proof, behaviour or hardening objective at the correct level. Grill-Me confirms that the proposed boundary is understood before meaningful implementation planning. Implementation then produces evidence, a handoff and a continuation decision.

This governance section is a working contract beneath the authority hierarchy in Section 1.1. It does not modify Product Law, Architecture Law, Domain Law or the Roadmap. It does not authorise implementation, freeze an implementation mechanism or replace a Feature Pack Contract, JIT Domain Dossier, Architectural Proof, Vertical Slice, Horizontal Hardening artifact, release decision or readiness decision.

## Feature Pack lifecycle

### Purpose

The Feature Pack lifecycle moves an approved roadmap outcome into a controlled implementation boundary.

### Stages

Every Feature Pack follows these stages in order, with a gate or explicit decision recorded when a stage cannot proceed:

1. **Selection.** Select an approved Roadmap outcome. Do not create a new outcome or expand the approved scope inside the Atlas.
2. **Discovery.** Gather the relevant authority documents, existing evidence, affected domains, dependencies, assumptions, policies, lifecycle concerns and open questions.
3. **Grill-Me.** Review the proposed outcome boundary and expose assumptions, dependencies, invalidation risks, future capability risks, affected domains and policy or lifecycle implications.
4. **Domain/architecture preparation.** Prepare the domain and architecture material needed for implementation-grade planning. This work must preserve domain ownership, architectural constraints, policy gates and known failure behaviour.
5. **Feature Pack contract approval.** Approve the Feature Pack Contract only after the outcome, boundary, dependencies, gates, acceptance criteria and required preparation are clear. ATLAS-01 defines this approval point but does not create the contract.
6. **TB/VS/HH selection.** Select the smallest applicable proof, behaviour and hardening boundaries. Record why each selected artifact is needed and what evidence it must produce.
7. **Implementation.** Execute only the approved Feature Pack Contract and lower-level contracts. Any material scope change returns to the relevant authority or review gate.
8. **Evidence review.** Compare implementation evidence with the acceptance criteria, assumptions, architecture, domain rules, lifecycle expectations, policies and operational requirements.
9. **Handoff.** Produce the Implementation Handoff with the final impact, evidence, limitations and operational requirements.
10. **Closure.** Record whether the Feature Pack is complete, needs more implementation or hardening, is blocked, or is ready for a next delivery decision. Closure requires the evidence and handoff requirements in this section.

The Feature Pack lifecycle may stop at any stage when authority, ownership, policy, evidence or scope is unresolved. A stopped stage is recorded and routed. It is not passed by filling the gap with an Atlas assumption.

## Tracer Bullet lifecycle

### Purpose

The Tracer Bullet lifecycle proves an architectural assumption or unknown path with the smallest realistic proof. A TB is a proof boundary, not a partial feature and not evidence that the complete product behaviour is ready.

### Required questions

Before a TB is selected, its contract must answer:

- What assumption is being proven?
- Why does existing evidence not prove it?
- What is the smallest realistic proof?
- What architecture layers are involved?
- What evidence determines success?
- What happens if proof fails?

The TB lifecycle frames the assumption, identifies the missing evidence, bounds the path, names the involved layers at the level required for the proof, runs the smallest realistic proof and records the result. A successful proof records what it proves and the boundary of that result. A failed proof records the failed assumption, the evidence, the affected authority or Feature Pack and the required rework, clarification or alternative. A failed TB never becomes an implicit approval to continue.

ATLAS-01 defines the TB lifecycle and selection questions only. It does not create a TB contract, proof task, `TB-nnn` identifier or executable proof.

## Vertical Slice lifecycle

### Purpose

The Vertical Slice lifecycle delivers one complete production-quality behaviour across every layer needed to make the stated user outcome true.

### Required considerations

Each VS contract must consider the following, marking an item as not applicable only with a reason:

- user outcome;
- domain ownership;
- policies;
- lifecycle changes;
- durable state;
- side effects;
- async behaviour;
- realtime behaviour;
- audit;
- tests; and
- operational evidence.

The VS lifecycle starts with a bounded behaviour and acceptance criteria, confirms its domain and policy boundaries, implements the complete path, exercises relevant failure and recovery behaviour, collects test and operational evidence, and ends with review against the stated outcome. A UI path, endpoint, projection or provider response alone is not a complete VS when the behaviour also requires authoritative state, side effects, audit, asynchronous work or operational controls.

ATLAS-01 defines these VS boundaries only. It does not create a VS contract, implementation task or `VS-nnn` identifier.

## Horizontal Hardening lifecycle

### Purpose

The Horizontal Hardening lifecycle strengthens already-correct functionality based on evidence. It does not replace missing implementation or hide an unproven behaviour behind a hardening label.

### Required evidence

Every HH contract must require:

- a measured reason;
- an identified failure mode;
- an improvement objective;
- before/after evidence; and
- regression validation.

The HH lifecycle identifies the measured pressure or failure, states the improvement objective, applies the smallest justified change, measures the before and after behaviour, validates regression risk and records the remaining safe boundary. If the underlying functionality is not correct or the failure is not understood, the work returns to implementation, proof or upstream clarification rather than being labelled hardening.

ATLAS-01 defines these HH boundaries only. It does not create an HH contract, hardening task or `HH-nnn` identifier.

## Grill-Me review gates

Grill-Me reviews are required before meaningful implementation planning. The review is an evidence and boundary check. It does not grant permission to change upstream law, and a positive review does not replace a required authority or expert decision.

### Feature Pack Grill-Me

The Feature Pack review must ask:

- What assumptions exist?
- What dependencies exist?
- What could invalidate the approach?
- What future capability could be blocked?
- What domains are affected?
- What policies/lifecycles are involved?

The review records the answers, missing evidence, required gates and the decision to proceed, revise, stop or seek upstream clarification.

### TB/VS/HH Grill-Me

The TB/VS/HH review must ask:

- Is this the correct implementation boundary?
- Are acceptance criteria clear?
- Are failure modes understood?
- Are security/privacy/performance requirements identified?
- Is the task small enough?
- Does it require upstream clarification?

The review must identify the artifact type, its acceptance boundary, evidence required, dependencies and unresolved questions. If the boundary is wrong or the task is too large, the review returns it for re-scoping. If an upstream rule is unclear, the review routes the question rather than deciding it locally.

## Implementation handoff

Completed implementation work must produce an Implementation Handoff artifact. The handoff is the durable record that connects the approved implementation boundary to the repository state, collected evidence and the next review. It records facts and decisions; it does not become a new authority source.

The handoff must capture:

- what was implemented;
- final architecture impact;
- domain impact;
- lifecycle changes;
- state machine changes;
- database changes;
- performance characteristics;
- security/privacy changes;
- tests/evidence;
- operational requirements;
- known limitations; and
- unlocked future work.

Each item must be stated explicitly or marked not applicable with a reason. The handoff must distinguish measured results from assumptions, link evidence to the relevant acceptance criteria or invariant and identify any work that remains gated, deferred or unsafe to continue.

## Continuation review

Before continuing development after previous work, the current system state must be compared against:

- previous handoff documentation;
- current repository state;
- current tests; and
- current authority documents.

The continuation review must verify:

- implementation matches the intended outcome;
- no undocumented scope expansion occurred;
- assumptions remain valid;
- no upstream authority was violated; and
- next work remains correctly scoped.

The review records the comparison, evidence, discrepancies and next delivery decision. A discrepancy stops continuation until it is corrected, accepted by the proper authority or explicitly routed. The review must not treat an unchanged plan or a passing narrow test as proof that the current repository still matches the previous handoff.

## Evidence and closure requirements

Evidence must be tied to the claim it supports. Depending on the lifecycle, it may include source references, approved decisions, domain and architecture checks, proof results, acceptance tests, failure and recovery tests, security or privacy checks, performance measurements, audit records and operational observations. Evidence must identify its scope, date or revision where relevant, and any limitation that prevents a broader claim.

Closure requires all of the following:

- the approved outcome and implementation boundary are identifiable;
- required Grill-Me reviews and authority gates are recorded;
- the selected TB, VS and HH objectives have a reviewed result, or an explicit reason they were not required;
- acceptance, regression, security/privacy, performance and operational evidence is present for the claims being closed;
- failed, pending or degraded behaviour is recorded with its owner, recovery path and next decision;
- the Implementation Handoff is complete, including known limitations and unlocked future work;
- the Continuation Review confirms the repository and authority state; and
- the next delivery decision is recorded as continue, harden, revise, stop, or proceed to the next approved outcome.

An artifact remains open, gated or stopped when any required evidence is missing or contradictory. Code completion alone is not lifecycle closure. Closure of a Feature Pack or lower-level artifact does not promote the Atlas or any handoff into Product Law, Architecture Law, Domain Law or Roadmap authority.

## Decision Escalation Matrix

Every planning or implementation discovery must be routed to the lowest correct authority that owns the decision. "Lowest correct" means the most specific authority that can decide the question without changing a higher-level rule. The Atlas may record the route and its downstream effect, but it must not decide for that authority.

The detailed authority hierarchy remains the one in Section 1.1. For escalation and execution routing, the relevant path is:

```text
Product Law
    → Architecture Law
    → Domain Law
    → Roadmap
    → Delivery Atlas
    → Feature Pack Contracts
    → JIT Domain Dossiers
    → TB / VS / HH
    → Implementation
```

This abbreviated path does not remove the Architectural Proof, Release or Readiness boundaries defined in Section 1.1 and the later Atlas views. It shows where a discovery is routed before work continues.

| Discovery Type | Example Question | Escalation Authority |
|---|---|---|
| Product truth | What should the platform/business do? | Product Law / Decision Register |
| Commercial model | Pricing, packaging, business rules | Product Law / Commercial decisions |
| Legal requirement | Compliance, contracts, obligations | Legal/Product authority |
| Clinical/safety rule | Health, safety, professional judgement | Clinical/Safety authority |
| Domain ownership | Who owns this durable truth? | Domain Map / Domain Law |
| Lifecycle semantics | What states, transitions, guards exist? | Owning Domain |
| Architecture mechanism | How should the platform support this? | Architecture Law |
| Cross-domain interaction | How should domains communicate? | Architecture + affected Domains |
| Delivery sequencing | What comes first? | Roadmap |
| Feature Pack scope | Included/excluded work | Feature Pack Contract |
| Implementation semantics | How exactly should code implement it? | JIT Domain Dossier / TB / VS / HH |
| Execution ambiguity | Coding task unclear | TB / VS / HH contract |
| Evidence problem | Cannot prove completion | Validation/evidence review |
| Operational concern | Monitoring, support, ownership | Operating Model |

### Lower-level artifacts do not resolve higher-level uncertainty

Lower-level artifacts must not resolve higher-level uncertainty. In particular:

- A TOON must not invent missing Product decisions.
- A Vertical Slice must not redefine Domain ownership.
- A JIT Dossier must not override Architecture Law.
- Implementation code must not become the source of business truth.

When a lower-level artifact discovers a question outside its authority, it records the question, the evidence, the affected work and the escalation route. It does not turn a plausible answer into a local rule.

### Escalation response

When uncertainty is discovered, the correct response is:

```text
identify owner
    → escalate
    → update correct authority artifact
    → continue only after resolution
```

The receiving authority updates its own artifact. The Atlas then revalidates the affected relationship, gate or STOP condition before downstream work continues. If the authority declines to decide, the discovery remains open or stopped and the next delivery decision records that state.

### Assumption prohibition

Plausible assumptions are not acceptable when:

- financial truth is affected;
- health/safety truth is affected;
- privacy/security boundaries are affected;
- durable ownership is unclear;
- lifecycle semantics are unclear; or
- architecture constraints are violated.

The absence of an immediate failure is not evidence that one of these assumptions is safe. Route the question to its owner and wait for the required resolution or authority decision.

### Escalation STOP conditions

A planner or coding agent must STOP when:

- the required decision belongs to a higher authority layer;
- two authority documents conflict;
- ownership of durable truth is unclear;
- a lifecycle cannot be correctly modelled;
- implementation would require inventing business rules; or
- acceptance criteria depend on unresolved policy.

The STOP record must name the discovery, evidence, current authority boundary, escalation authority, affected work and the condition required before continuation. No lower-level artifact may silently absorb the unresolved decision.

## Future template registry

Future authorized work will provide templates in `docs/templates/`. The templates will standardize the contracts and records described by this governance model:

| Future template | Purpose |
|---|---|
| `FEATURE_PACK_TEMPLATE.md` | Define the approved outcome, implementation boundary, dependencies, gates, acceptance criteria and required lower-level preparation for a Feature Pack. |
| `TB_TEMPLATE.md` | Define an architectural assumption, the smallest proof, involved layers, success evidence and the failure route for a Tracer Bullet. |
| `VS_TEMPLATE.md` | Define one complete production-quality behaviour, its domain and policy boundaries, acceptance criteria and implementation evidence for a Vertical Slice. |
| `HH_TEMPLATE.md` | Define the measured failure or pressure, improvement objective, before/after evidence and regression validation for Horizontal Hardening. |
| `IMPLEMENTATION_HANDOFF_TEMPLATE.md` | Capture final implementation impact, tests, evidence, operational requirements, limitations and unlocked future work. |
| `CONTINUATION_REVIEW_TEMPLATE.md` | Compare prior handoff, repository, tests and authority documents, then record discrepancies and the next delivery decision. |

This registry is conceptual. ATLAS-01 does not create these files, populate them or create any Feature Pack Contract, JIT Domain Dossier, TB, VS, HH or TOON prompt.

# 2. Atlas terminology and classification system

All Atlas labels describe planning relationships. They are not product state values, database values or implementation interfaces.

## 2.1 Core terms

| Term | Atlas meaning |
|---|---|
| Atlas entry | A derived planning statement with an exact source reference, an owner of the source truth and a stated confidence or gate status. |
| Capability | An outcome-level ability approved by Product Law or the Roadmap. It is not a module, screen, table or provider. |
| Delivery seam | A relationship, boundary or pressure point that later delivery must preserve or prove. |
| Feature Pack | A Roadmap delivery container organized around an outcome and validation objective. The Atlas does not redefine it. |
| Introduction | The first approved delivery use of a capability or cross-cutting concern. |
| Reuse | Use of an already-proven or already-governed capability in another outcome without creating a parallel authority. |
| Extension | An approved additional outcome or lifecycle branch that builds on an existing capability while preserving its authority and invariants. |
| Composition | An outcome assembled from multiple existing capabilities or domains, such as a configured product experience. |
| Projection | A derived, rebuildable or presentation-oriented view of authoritative facts. It never becomes source authority. |
| Lifecycle coverage | The Atlas record of whether a lifecycle exists, who owns it, what upstream semantics are known and where a full implementation-grade specification is required. |
| JIT boundary | The point at which the affected Feature Pack must create or update implementation-grade planning rather than rely on the Atlas. |
| Stop | A controlled halt because the current evidence is missing, contradictory or requires an authority decision not available at the Atlas level. |

## 2.2 Classification axes

Each populated Atlas entry uses only the labels needed for its view. Multiple relationship and pressure labels may apply.

| Axis | Permitted labels | Use |
|---|---|---|
| Authority basis | `PRODUCT`, `ARCHITECTURE`, `DOMAIN`, `ROADMAP`, `SUPPORTING`, `ATLAS_DERIVED`, `JIT`, `EVIDENCE`, `STOP` | Identifies where the statement comes from or where an unresolved matter must be routed. |
| Delivery relationship | `INTRODUCE`, `REUSE`, `EXTEND`, `COMPOSE`, `PROJECT`, `GATED`, `FUTURE_SEAM` | Describes how a capability or boundary relates to delivery. |
| Readiness | `VISIBLE`, `DEPENDENT`, `GATED`, `JIT_REQUIRED`, `PROVEN`, `STOPPED` | Shows whether a relationship is visible, blocked by a gate, ready for JIT specification, supported by executable evidence or stopped. |
| Lifecycle coverage | `NONE`, `EXISTENCE_ONLY`, `UPSTREAM_SEMANTICS`, `FULL_SPEC_REQUIRED`, `PROOF_REQUIRED` | Separates lifecycle visibility from implementation-grade lifecycle design. |
| Temperature | `HOT`, `WARM`, `COLD`, `UNCLASSIFIED` | Records broad expected use character only. It does not set infrastructure. |
| Pressure | `CONCURRENCY`, `BURST`, `DATABASE`, `ASYNC`, `PROVIDER`, `REALTIME`, `PROJECTION_FRESHNESS`, `EXPORT`, `NONE` | Records a broad pressure that may require later evidence. |
| Risk | `PRODUCT_POLICY`, `OWNERSHIP`, `SAFETY`, `PRIVACY`, `SECURITY`, `LEGAL`, `CLINICAL`, `PROFESSIONAL`, `PROVIDER`, `FAILURE_RECOVERY`, `PERFORMANCE`, `SCOPE` | Identifies why a relationship or gate matters. |

## 2.3 Evidence rule

Every populated entry must include:

- the exact current source path and section, decision, requirement, flow or gate;
- the authority level of that source;
- the Atlas relationship being derived;
- the confidence or readiness label;
- any blocking or future-only gate;
- the next lower-level artifact required, if any; and
- a note when the entry is intentionally broad because exact semantics are JIT.

If an entry cannot meet this evidence rule, the Atlas records `STOPPED` and routes the issue under Section 24 rather than filling the gap with a plausible assumption.

---

# 3. Mature-platform delivery view

## 3.1 View purpose

This view keeps the approved mature-platform outcome in frame while delivery proceeds through smaller outcomes. It must show how a later capability relates to the whole ecosystem without requiring every future capability to be implemented or specified now.

The view may later answer:

- what mature outcome or capability family an entry supports;
- which approved delivery container introduces it;
- which shared capabilities it depends on or reuses;
- which domains and actors participate;
- what lifecycle, journey, integration, measurement, safety, proof and hardening concerns are exposed;
- what remains gated or future-only; and
- which future seam must not be closed by a local implementation choice.

## 3.2 Population structure

The following is an empty planning view. ATLAS-01 does not populate its rows.

| Mature capability or outcome family | Upstream anchor | Delivery relationship | First relevant Feature Pack | Reused or extended by | Domain participation | Lifecycle coverage | Gate / proof / hardening hooks | Future seam | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

The view must not become a duplicate of the North Star, Platform, Domain Map or Roadmap. It records relationships between those sources and later delivery work.

---

# 4. Feature Pack portfolio map

## 4.1 Portfolio rule

The portfolio map must eventually cover the complete approved Feature Pack portfolio exactly as defined by `docs/00_platform/05_ROADMAP_v1.0.0.md`. The Roadmap remains the authority for Feature Pack identity, outcome, scope, sequencing, dependencies, gates and release effect.

ATLAS-01 defined the map. ATLAS-02 populates only the Feature Pack Portfolio Register from the frozen Roadmap. It does not select FP-001, prepare a Feature Pack or begin Phase 7.

## Feature Pack Portfolio Register

This register is derived from the frozen Roadmap and does not change its Feature Pack identities, sequence, dependencies, gates or release effects. It covers all 17 approved Feature Packs in Roadmap order.

The domain classifications use only the frozen Domain Map names and ownership boundaries:

- **Primary** means the Feature Pack introduces or materially establishes capability whose durable truth belongs to that domain.
- **Supporting** means the Feature Pack interacts with the domain's existing authority.
- **Consumer** means the Feature Pack uses an existing capability from that domain.

These labels describe delivery involvement. They do not move ownership. Gate statuses are recorded as stated by the Roadmap and current Open Work tracker. They are not resolved by this register.

### Portfolio summary

| Feature Pack | Purpose | Delivery Position | Primary Outcome |
|---|---|---|---|
| FP-001 | Establish a trusted bilingual boundary from public entry to verified identity. | Phase 1, position 1, foundational | Verified individual account entry. |
| FP-002 | Convert an approved offer into verified payment and valid access. | Phase 1, position 2, foundational | One reconciled payment and entitlement outcome. |
| FP-003 | Make temperament assessment and report provenance part of the paid core. | Phase 2, position 3, foundational | Bilingual immutable assessment report. |
| FP-004 | Gate personalised guidance through safe intake and eligibility. | Phase 2, position 4, foundational | Current eligibility or governed fallback outcome. |
| FP-005 | Deliver the first safe paid plan, purchased library and feedback value. | Phase 2, position 5, foundational | Seven-day plan or approved General Wellness pathway. |
| FP-006 | Make the core journey operable and ready for staged paid release. | Phase 3, position 6, foundational | Controlled pilot and release decisions. |
| FP-007 | Prove governed live-session and replay value. | Phase 4, position 7, expansion | Protected live and replay experience. |
| FP-008 | Prove the first native Nuwe Jy flagship edition. | Phase 4, position 8, expansion | Operable 60-day Nuwe Jy cohort. |
| FP-009 | Validate genuine recurring value before Basic Membership sale. | Phase 4, position 9, expansion | Operational Basic Membership. |
| FP-010 | Add governed recurring review and plan adjustment. | Phase 4, position 10, expansion | Safe monthly review or adjusted plan. |
| FP-011 | Package proven recurring capabilities as Premium. | Phase 4, position 11, expansion | Versioned Premium bundle. |
| FP-012 | Test a limited professional review service with controlled capacity. | Phase 5, position 12, maturity | Controlled practitioner-review pilot. |
| FP-013 | Use external/community evidence to justify first-party community and challenges. | Phase 5, position 13, maturity | Moderated community and governed challenges. |
| FP-014 | Extend programme evidence into broader habits, journals and progress. | Phase 5, position 14, maturity | Foundation programme and reflective progress capability. |
| FP-015 | Add payment and capacity truth for scarce paid events. | Phase 6, position 15, maturity | Capacity-controlled event commerce. |
| FP-016 | Add governed first-party experimentation when a real decision surface exists. | Phase 6, position 16, maturity | Auditable product learning. |
| FP-017 | Activate a separately approved future product space or market. | Phase 6, position 17, later capability | Controlled future expansion. |

## FP-001 — Trusted bilingual entry and verified identity

### Purpose

This Feature Pack establishes the trusted boundary between a public visitor and every protected NewYou journey. It solves the need for one canonical identity, bilingual launch-facing entry, verified access and controlled account support before purchase, assessment, health, plan or deletion actions can be used safely.

### Intended Outcome

A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, verify email, recover access and use a controlled support/admin path without seeing unfinished product spaces.

### Roadmap Position

- Phase 1, Trusted entry and commercial truth.
- Relative position: 1 of 17 and the first node on the approved core path.
- Delivery character: foundational.

### Approved Dependencies

- Frozen Product Law, Architecture Law and Domain Law only.
- No future product Feature Pack is a prerequisite.

### Known Unlocks

- `FP-002` purchase, verified payment and entitlement.
- The protected identity boundary required by every later core journey and the staged paid-release path in `FP-006`.

### High-Level Domain Involvement

- **Primary:** Identity & Access.
- **Supporting:** Privacy & Consent; Communications; Audit & Evidence.
- **Consumer:** Content & Media; Analytics.

### Known Gates

- `OQ-034 — BLOCKS_THIS_FP`: authentication implementation architecture is required for the stated verified identity/session outcome.
- `OQ-035 — BLOCKS_RELEASE_ONLY`: abuse-control thresholds and recovery behaviour are required before protected public or pilot release.
- `OQ-036 — BLOCKS_RELEASE_ONLY`: email verification and mandatory notices require an approved launch channel policy.
- `OQ-038 — FUTURE_ONLY`: named incident ownership is a paid-pilot and release condition owned by `FP-006`, not a reason to delay safe internal identity work.

### Release Significance

This provides the trusted entry capability that every protected core journey and the first paid pilot depends on. It is foundational, but it is not the participant-ready MVP by itself.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-001`, with dependency and phase context in §§3.2, 5 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-002 — Purchase to verified payment and entitlement

### Purpose

This Feature Pack establishes the commercial truth needed for a paid product. It solves the risk that a browser return, provider callback or retry could grant access before payment is verified or multiply a purchase outcome.

### Intended Outcome

A participant can purchase one of the three approved South African/ZAR launch products through the launch payment gateway and receive exactly one valid component entitlement only after payment is verified and reconciled.

### Roadmap Position

- Phase 1, Trusted entry and commercial truth.
- Relative position: 2 of 17, immediately after `FP-001` on the approved core path.
- Delivery character: foundational.

### Approved Dependencies

- `FP-001`.
- The approved initial product catalogue and versioned prices.

### Known Unlocks

- `FP-003` and the paid core capabilities that consume assessment, plan and library access.
- The payment and entitlement relationship later reused by `FP-009`, `FP-011` and `FP-015` where their approved commercial outcomes apply.

### High-Level Domain Involvement

- **Primary:** Commerce; Entitlements.
- **Supporting:** Identity & Access; Privacy & Consent; Audit & Evidence.
- **Consumer:** Analytics.

### Known Gates

- `OQ-004 — BLOCKS_THIS_FP`: provider webhook, retry, refund, dispute and ambiguity behaviour is material to verified payment.
- `OQ-035 — BLOCKS_RELEASE_ONLY`: payment and checkout abuse thresholds and recovery are required before paid public or pilot release.
- `OQ-001 — BLOCKS_RELEASE_ONLY`: operating authority is required before production subscriptions, payment and sensitive processing are activated.
- `OQ-002 — NON_BLOCKING_FOR_THIS_FP`: the three MVP prices are locked; future Basic Membership pricing is not needed here.
- `OQ-036 — NON_BLOCKING_FOR_THIS_FP`: ordinary payment truth does not require a future reminder/channel decision beyond mandatory launch communication.

### Release Significance

This creates the commercial prerequisite for assessment, plan and purchased-library access. It is necessary for the paid core, but it is not by itself a participant-ready MVP.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-002`, with dependency and phase context in §§3.2, 5, 7 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; gate context in `05_ROADMAP_v1.0.0.md §14` and current unresolved-work context in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-003 — Temperament provenance, assessment and immutable report

### Purpose

This Feature Pack makes temperament a trustworthy input to the core proposition. It solves the need to distinguish self-reported, book-derived and digitally assessed temperament, preserve the approved assessment history and deliver a report that can be reproduced and understood in both launch languages.

### Intended Outcome

A purchaser can use a self-reported, book-derived or digitally assessed temperament path, complete the approved assessment when entitled, receive a bilingual report with primary and secondary result and provenance, and retain immutable assessment/report history under deletion law.

### Roadmap Position

- Phase 2, Core participant value loop.
- Relative position: 3 of 17 and the first assessment node after commercial access.
- Delivery character: foundational.

### Approved Dependencies

- `FP-001` and `FP-002`.
- Approved initial methodology and assessment content.

### Known Unlocks

- `FP-004` safety and eligibility work where approved temperament context is requested.
- `FP-005` personalised-plan delivery, which requires the approved temperament input and report path.

### High-Level Domain Involvement

- **Primary:** Temperament.
- **Supporting:** Content & Media; Privacy & Consent; Audit & Evidence.
- **Consumer:** Entitlements; Identity & Access; Analytics.

### Known Gates

- `OQ-013 — BLOCKS_RELEASE_ONLY`: the bilingual report needs the approved governed translation and version path before release.
- `OQ-006 — FUTURE_ONLY`: optional score-distance labels are not required for core launch scoring unless that scope is activated.
- `OQ-009` and `OQ-029 — BLOCKS_RELEASE_ONLY`: retention and deletion categories must be sufficiently approved before paid pilot release.
- Methodology, content and rights approval — `BLOCKS_THIS_FP` for the released assessment version.

### Release Significance

This is the assessment product capability and a required input to personalised plan delivery. It gives the paid core an authoritative, provenance-labelled temperament result rather than an unqualified personalisation claim.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-003`, with dependency and phase context in §§3.2, 5 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-004 — Safe health onboarding and deterministic eligibility

### Purpose

This Feature Pack establishes the safety boundary before plan generation. It solves the risk that incomplete, high-risk or purpose-mismatched health information could be treated as permission for an automated personalised plan.

### Intended Outcome

A participant completes progressive, purpose-specific health and lifestyle onboarding and receives exactly one current eligibility outcome: `eligible_automated`, `general_wellness_only`, `professional_review_required` or `insufficient_information`.

### Roadmap Position

- Phase 2, Core participant value loop.
- Relative position: 4 of 17, immediately before plan delivery on the approved core path.
- Delivery character: foundational.

### Approved Dependencies

- `FP-001`.
- `FP-003` where temperament context is requested.
- Approved clinical eligibility and urgent-help content.

### Known Unlocks

- `FP-005` safe plan generation for eligible participants and the approved General Wellness fallback.
- The safety boundary reused by the later controlled practitioner path in `FP-012`.

### High-Level Domain Involvement

- **Primary:** Health Records; Safety & Eligibility.
- **Supporting:** Privacy & Consent; Audit & Evidence.
- **Consumer:** Identity & Access; Content & Media; Analytics.

### Known Gates

- `OQ-005 — BLOCKS_THIS_FP`: the clinical eligibility matrix cannot be invented locally.
- `OQ-008 — BLOCKS_THIS_FP`: urgent-safety wording and boundaries need approval before participant release.
- `OQ-007 — FUTURE_ONLY`: laboratory validity belongs to a later laboratory-enabled path, not the initial intake unless that scope changes through authority.
- `OQ-009` and `OQ-029 — BLOCKS_RELEASE_ONLY`: health and professional retention categories are required for pilot release.
- `OQ-033 — NON_BLOCKING_FOR_THIS_FP`: a professional-review outcome can be recorded or routed without activating the practitioner service.

### Release Significance

This unlocks safe plan generation and a lawful General Wellness fallback. It keeps professional review downstream and does not activate a practitioner service.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-004`, with dependency and phase context in §§3.2, 5 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-005 — Safe seven-day plan, purchased library and basic feedback

### Purpose

This Feature Pack delivers the first promised paid value. It solves the need for a safe, temperament-guided plan and purchased content experience that remains explainable, bilingual and useful without turning participant feedback into clinical authority.

### Intended Outcome

An eligible participant receives an immutable, explainable, bilingual seven-day plan or approved General Wellness Starter Pathway, can access purchased report and plan content, switch approved language and energy-unit presentation, and record lightweight daily or weekly progress and feedback.

### Roadmap Position

- Phase 2, Core participant value loop.
- Relative position: 5 of 17 and the final participant-value node on the initial core path.
- Delivery character: foundational.

### Approved Dependencies

- `FP-001` through `FP-004`.
- Approved calculation, content, recipe/substitution, safety and bilingual versions.

### Known Unlocks

- `FP-006` controlled operations and staged paid release.
- `FP-008` Nuwe Jy, `FP-010` recurring adjustment, `FP-012` practitioner review and `FP-014` foundation-programme work, each of which depends on the proven core plan path.

### High-Level Domain Involvement

- **Primary:** Plans & Nutrition; Habits, Journals & Progress.
- **Supporting:** Content & Media; Safety & Eligibility; Temperament; Privacy & Consent; Audit & Evidence.
- **Consumer:** Entitlements; Identity & Access; Analytics.

### Known Gates

- `OQ-010 — BLOCKS_THIS_FP`: calculation values and bounded weight-reduction rules are part of safe plan truth.
- `OQ-013 — BLOCKS_THIS_FP`: the paid and safety-critical bilingual plan path needs approved locale and version semantics.
- `OQ-016 — BLOCKS_RELEASE_ONLY`: publication, stale-approval and correction/withdrawal operations must be ready before pilot release.
- `OQ-014 — NON_BLOCKING_FOR_THIS_FP`: advanced shared edge delivery is not required to prove plan correctness.
- `OQ-011` and `OQ-012 — FUTURE_ONLY`: automatic monthly adjustment is excluded from this once-off MVP path and belongs to `FP-010`.

### Release Significance

This completes the participant-facing paid core journey. `FP-006` remains necessary before real paid pilot release because participant value alone does not establish operational readiness.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-005`, with dependency and phase context in §§3.2, 5 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-006 — Controlled core operations and staged paid release

### Purpose

This Feature Pack turns a technically complete core journey into a service that named people can operate. It solves the release gap between working participant behaviour and a paid pilot that can be supported, observed, corrected, withdrawn and stopped safely.

### Intended Outcome

Named operators can run, support, observe, correct, withdraw, reconcile and safely stop the approved core journey through internal validation, the first 10 paid participants, review, expansion toward 25, a maximum of 50 in the first paid pilot, limited public release and general public release decisions.

### Roadmap Position

- Phase 3, Controlled paid evidence and pilot progression.
- Relative position: 6 of 17 and the release/evidence boundary for the foundational core.
- Delivery character: foundational.

### Approved Dependencies

- `FP-001` through `FP-005`.
- Named product, clinical, content, commerce, legal/privacy, security and operations owners.

### Known Unlocks

- The Phase 4 branches: `FP-007`, `FP-008`, `FP-009`, `FP-010` and `FP-011`.
- The Phase 5 and Phase 6 branches: `FP-012`, `FP-013`, `FP-014`, `FP-015`, `FP-016` and `FP-017`, subject to their own gates and evidence.

### High-Level Domain Involvement

- **Primary:** Audit & Evidence.
- **Supporting:** Analytics; Identity & Access; Privacy & Consent; Commerce; Entitlements; Temperament; Health Records; Safety & Eligibility; Plans & Nutrition; Content & Media; Communications.

### Known Gates

- `OQ-001 — BLOCKS_RELEASE_ONLY`: operating authority must support production subscriptions and sensitive health processing.
- `OQ-009` and `OQ-029 — BLOCKS_THIS_FP`: pilot operation needs approved enough retention categories for the records it handles.
- `OQ-030`, `OQ-031` and `OQ-032 — BLOCKS_THIS_FP`: external processor deletion/export, deletion-safe restore and operational deletion/export behaviour must protect the pilot.
- `OQ-035`, `OQ-036`, `OQ-037` and `OQ-038 — BLOCKS_RELEASE_ONLY`: abuse, communications, continuity and incident ownership are release-readiness conditions.
- `OQ-039 — NON_BLOCKING_FOR_THIS_FP`: implementation-grade mapping remains scoped to later affected delivery work.
- The Product Law cross-functional paid-pilot readiness gate remains required.

### Release Significance

This is the operational boundary for internal validation, the first 10 paid participants, expansion toward 25, the first pilot maximum of 50 and later limited or general public release decisions. It is the release backbone of the foundational journey.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-006`, with dependency and phase context in §§3.2, 5, 7, 8 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §§5 and 7`.

## FP-007 — Governed live sessions and replay

### Purpose

This Feature Pack proves live value as a governed participant experience before scarce event commerce is considered. It solves the need for protected live access, recording and replay with clear provider, consent and recovery boundaries.

### Intended Outcome

A participant can discover and register for an approved live session, pass current entitlement and access checks, join protected playback and receive a governed replay where recording and consent rules allow. Operators can see provider or delivery failure without changing platform truth.

### Roadmap Position

- Phase 4, First recurring and flagship pathways.
- Relative position: 7 of 17 and the first later branch after the controlled core release boundary.
- Delivery character: expansion.

### Approved Dependencies

- `FP-006`.
- An approved session owner and live/replay content and policy.

### Known Unlocks

- `FP-008` Nuwe Jy live integration.
- `FP-009` recurring live value.
- `FP-015` event commerce, together with the approved `FP-002` payment path and `FP-006` operational evidence.

### High-Level Domain Involvement

- **Primary:** Events & Live.
- **Supporting:** Entitlements; Content & Media; Communications; Privacy & Consent; Audit & Evidence.
- **Consumer:** Identity & Access; Analytics.

### Known Gates

- `OQ-020 — BLOCKS_THIS_FP`: the provider path and failure behaviour are part of the live/replay outcome.
- `OQ-021 — BLOCKS_THIS_FP`: recording, attendee, replay and withdrawal rules require approval.
- `OQ-036 — BLOCKS_THIS_FP` for a promised live notification journey.
- `OQ-017 — NON_BLOCKING_FOR_THIS_FP`: reminders are optional until a governed reminder promise is added.
- `OQ-022 — FUTURE_ONLY`: scarce reservations and flash-sale mechanics belong to `FP-015`.

### Release Significance

This unlocks governed live and replay value for Nuwe Jy and early Membership. It does not activate paid event commerce or scarce-capacity ticketing.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-007`, with dependency and phase context in §§3.2, 5, 12 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-008 — Native Nuwe Jy flagship edition

### Purpose

This Feature Pack makes Nuwe Jy the first concrete test of native programme delivery. It solves the need to turn the approved flagship experience into an operable scheduled cohort without building a generic programme platform before evidence requires one.

### Intended Outcome

The first native Nuwe Jy edition can operate as an approved 60-calendar-day scheduled cohort with a Today experience, daily releases, habits, check-ins, progress and recovery, temperament-aware delivery, central safety and plan integration, governed cohort community, live/replay, support, communications and compassionate completion evidence.

### Roadmap Position

- Phase 4, First recurring and flagship pathways.
- Relative position: 8 of 17, a sibling branch with `FP-009` after the shared live and operational foundation.
- Delivery character: expansion.
- `FP-009` is not a hard prerequisite for this pack.

### Approved Dependencies

- `FP-005`, `FP-006` and `FP-007`.
- Approved Nuwe Jy content/source inventory and edition owners.

### Known Unlocks

- `FP-013` first-party community and governed challenges, where the required evidence is present.
- `FP-014` broader foundation-programme capability, using Nuwe Jy as the concrete programme acceptance path.

### High-Level Domain Involvement

- **Primary:** Programmes & Challenges.
- **Supporting:** Habits, Journals & Progress; Community; Events & Live; Content & Media; Entitlements; Temperament; Safety & Eligibility; Plans & Nutrition; Communications; Privacy & Consent; Audit & Evidence.
- **Consumer:** Identity & Access; Analytics.

### Known Gates

- `OQ-024 — BLOCKS_THIS_FP`: source content, media, rights and translation inventory must be approved.
- `OQ-025 — BLOCKS_THIS_FP`: Nuwe Jy safety, milestone and completion rules must be approved.
- `OQ-026 — BLOCKS_THIS_FP`: cohort, facilitator, moderator, support, live ownership and saleable capacity must be clear.
- `OQ-027 — BLOCKS_THIS_FP`: scheduled communication channels, deduplication, caps and failure ownership are required.
- `OQ-019 — BLOCKS_THIS_FP`: edition completion metrics are part of the product outcome.
- `OQ-020`, `OQ-021`, `OQ-017` and `OQ-036 — BLOCKS_RELEASE_ONLY`: applicable live, recording, reminder and notification paths must be resolved before activation.
- `OQ-023` and `OQ-028 — BLOCKS_RELEASE_ONLY`: governed external community operation and legacy cutover obligations must be clear before activation.
- Inherited clinical, translation and retention gates remain applicable.

### Release Significance

This is the first native flagship edition and the concrete acceptance path for reusable programme, edition and cohort capability. It is an expansion outcome after the paid core has been proven and operated.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-008`, with dependency and phase context in §§3.2, 5, 9, 12 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-009 — Basic Membership recurring value

### Purpose

This Feature Pack tests whether NewYou can sell recurring value honestly. It solves the need for an operational Membership contract with real content, live, community and Q&A value before recurring revenue is promised.

### Intended Outcome

A participant can buy and maintain Basic Monthly or Annual Membership and receive genuinely operational moderated community access, at least one approved member-content release per month, at least one live session per month, group Q&A submission and correct entitlement and cancellation behaviour.

### Roadmap Position

- Phase 4, First recurring and flagship pathways.
- Relative position: 9 of 17, a sibling branch with `FP-008`; the Roadmap does not require `FP-008` to come first.
- Delivery character: expansion.

### Approved Dependencies

- `FP-002`, `FP-006` and `FP-007`.
- A governed community operating path and approved monthly value owners.
- `FP-008` is useful evidence but is not a circular hard dependency.

### Known Unlocks

- `FP-011` Premium bundle, where the approved packaging uses the Membership contract.
- Evidence for `FP-013` first-party community and governed challenges.

### High-Level Domain Involvement

- **Primary:** Commerce; Entitlements.
- **Supporting:** Community; Content & Media; Events & Live; Communications; Identity & Access; Privacy & Consent; Audit & Evidence.
- **Consumer:** Analytics.

### Known Gates

- `OQ-004 — BLOCKS_THIS_FP`: recurring billing, failed-payment, cancellation, refund and provider-delivery behaviour is the commercial contract.
- `OQ-016 — BLOCKS_THIS_FP`: monthly approved content needs reliable publication and stale-approval recovery.
- `OQ-023 — BLOCKS_THIS_FP`: the governed community path needs moderation, privacy, disclosure and escalation policy.
- `OQ-020` and `OQ-021 — BLOCKS_RELEASE_ONLY`: any Membership-specific live promise must pass its operational gate.
- `OQ-001` and `OQ-002 — BLOCKS_RELEASE_ONLY`: operating authority and evidence-based public pricing are required before sale.
- `OQ-017` and `OQ-036 — BLOCKS_RELEASE_ONLY`: recurring reminders and notifications cannot be promised before channel, consent, quiet-hour and retry policy is approved.

### Release Significance

This enables Basic Membership only after its promised recurring value is operational through a complete billing period. It does not justify Premium, first-party community or event commerce by itself.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-009`, with dependency and phase context in §§3.2, 5, 10, 12 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; gate context in `05_ROADMAP_v1.0.0.md §14` and current unresolved-work context in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-010 — Recurring plan review and governed adjustment

### Purpose

This Feature Pack establishes a safe recurring review boundary after once-off plan delivery is useful. It solves the need for governed plan adjustment based on approved check-ins and trends without allowing progress data to become Safety authority.

### Intended Outcome

An entitled participant with sufficient approved check-ins can receive a monthly trend-based review and, where allowed, an immutable governed plan adjustment with explicit grace or incomplete-check-in behaviour and renewed safety evaluation.

### Roadmap Position

- Phase 4, First recurring and flagship pathways.
- Relative position: 10 of 17, after stable once-off plan delivery and useful check-ins.
- Delivery character: expansion.
- `FP-009` is not required unless the adjustment is packaged through Membership.

### Approved Dependencies

- `FP-005` and `FP-006`.
- Approved trend and check-in evidence and clinical/product review rules.
- `FP-009` only when the adjustment is packaged through Membership.

### Known Unlocks

- The recurring adjustment capability used by `FP-011` Premium packaging.
- A governed adjustment add-on where that commercial outcome is approved.

### High-Level Domain Involvement

- **Primary:** Plans & Nutrition.
- **Supporting:** Habits, Journals & Progress; Health Records; Safety & Eligibility; Entitlements; Temperament; Content & Media; Privacy & Consent; Audit & Evidence; Commerce where an add-on is sold.
- **Consumer:** Identity & Access; Analytics.

### Known Gates

- `OQ-003`, `OQ-011` and `OQ-012 — BLOCKS_THIS_FP`: monthly review contract, adjustment thresholds and review timing define the outcome.
- `OQ-010 — BLOCKS_RELEASE_ONLY`: calculation approval is required if an adjustment changes approved calculation values.
- `OQ-005 — BLOCKS_RELEASE_ONLY`: current eligibility and safety rules must still be applied before an adjusted plan is activated.
- `OQ-018 — NON_BLOCKING_FOR_THIS_FP`: basic check-ins need not become private journals.
- `OQ-004 — FUTURE_ONLY` unless a new recurring payment contract is included; packaged billing belongs to `FP-011`.

### Release Significance

This unlocks the plan-adjustment add-on and provides the capability prerequisite for Premium. It is deliberately later than the once-off MVP because recurring adjustment carries additional safety and review obligations.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-010`, with dependency and phase context in §§3.2, 5, 10 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-011 — Premium bundle around proven capability

### Purpose

This Feature Pack turns already-proven recurring capabilities into a commercial Premium offer. It solves the risk that Premium becomes a promise for unresolved clinical, billing or operational work or creates a second access model.

### Intended Outcome

Premium is sold as a versioned bundle of working recurring review and adjustment and approved benefits through the existing Commerce and Entitlements model, including governed reassessment rules where applicable, without promising unlimited practitioner access.

### Roadmap Position

- Phase 4, First recurring and flagship pathways.
- Relative position: 11 of 17, after the applicable Membership and adjustment capabilities are proven.
- Delivery character: expansion.

### Approved Dependencies

- `FP-010`.
- `FP-009` when Premium uses the Membership contract.
- `FP-002`, `FP-005` and `FP-006`.
- Approved benefits and pricing.

### Known Unlocks

- The validated higher-value Premium commercial tier and its approved component benefits.
- No later Feature Pack is an explicit prerequisite of this pack's outcome.

### High-Level Domain Involvement

- **Primary:** Commerce.
- **Supporting:** Entitlements; Plans & Nutrition; Habits, Journals & Progress; Health Records; Safety & Eligibility; Content & Media; Communications; Privacy & Consent; Audit & Evidence.
- **Consumer:** Identity & Access; Analytics.

### Known Gates

- `OQ-003`, `OQ-011` and `OQ-012 — BLOCKS_THIS_FP`: Premium cannot promise monthly review or adjustment before those rules operate.
- `OQ-004 — BLOCKS_THIS_FP`: billing, failed-payment, cancellation, reassessment and refund consequences need validated provider behaviour.
- `OQ-001` and `OQ-002 — BLOCKS_RELEASE_ONLY`: operating authority and evidence-based Premium pricing are required before public sale.
- `OQ-036 — BLOCKS_RELEASE_ONLY`: recurring benefit communications need approved channel, consent and retry behaviour.
- Existing Commerce and Entitlements ownership — `NON_BLOCKING_FOR_THIS_FP`: Product and Domain Law require reuse of the existing owners.

### Release Significance

This enables a validated higher-value commercial tier only after its component capabilities pass their own gates. It preserves one commercial and access model and does not create an unlimited practitioner expectation.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-011`, with dependency and phase context in §§3.2, 5, 10 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; gate context in `05_ROADMAP_v1.0.0.md §14` and current unresolved-work context in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-012 — Controlled practitioner review pilot

### Purpose

This Feature Pack tests whether limited professional review is safe, useful and operable after automated plan delivery is stable. It solves the need for a capacity-controlled service without turning NewYou into an open practitioner marketplace.

### Intended Outcome

An eligible participant can purchase a limited practitioner-review service, provide explicit consent, receive a scoped active relationship and structured review outcome, and receive an approved modification, restriction, follow-up or referral with capacity and turnaround visible to operators and participants.

### Roadmap Position

- Phase 5, Professional care and evidence-led community/behaviour change.
- Relative position: 12 of 17 and the first professional-care branch.
- Delivery character: maturity.

### Approved Dependencies

- `FP-004`, `FP-005` and `FP-006`.
- Authorised practitioner(s), explicit service price and approved turnaround and capacity.

### Known Unlocks

- A limited priced practitioner-review service with evidence about demand, safety, capacity and economics.
- A governed professional-care pathway, without opening a practitioner marketplace.

### High-Level Domain Involvement

- **Primary:** Professional Care.
- **Supporting:** Identity & Access; Privacy & Consent; Health Records; Safety & Eligibility; Plans & Nutrition; Commerce; Entitlements; Communications; Audit & Evidence.
- **Consumer:** Analytics.

### Known Gates

- `OQ-033 — BLOCKS_THIS_FP`: professional record authority, participant access, addendum and disposition rules are necessary.
- `OQ-001 — BLOCKS_THIS_FP`: practitioner contracting and sensitive professional processing require operating authority.
- `OQ-009` and `OQ-029 — BLOCKS_THIS_FP`: professional and health retention categories must be approved before cases are sold.
- Practitioner agreements and saleable-capacity approval — `BLOCKS_THIS_FP`.
- `OQ-004 — BLOCKS_RELEASE_ONLY` if the service introduces a new recurring billing contract; a once-off review may reuse the approved payment path.

### Release Significance

This enables a limited, priced and capacity-controlled practitioner-review pilot. It validates professional care as a scarce service while preserving the automated MVP boundary.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-012`, with dependency and phase context in §§3.2, 5, 11 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-013 — First-party community and governed challenges

### Purpose

This Feature Pack moves first-party community work behind evidence from Nuwe Jy, Membership and governed external participation. It solves the need for NewYou-specific community and challenge value without building a generic social network or skipping moderation and privacy policy.

### Intended Outcome

Participants can join a first-party moderated community and safe governed challenges with current entitlement checks, privacy-aware profiles, private progress and recognition, reporting, moderation, sanctions, appeals and deletion or anonymisation behaviour.

### Roadmap Position

- Phase 5, Professional care and evidence-led community/behaviour change.
- Relative position: 13 of 17, after the required Nuwe Jy or Membership evidence.
- Delivery character: maturity.

### Approved Dependencies

- `FP-006`.
- Evidence from `FP-008` and/or `FP-009`.
- `FP-007` if live or challenge sessions are included.

### Known Unlocks

- A first-party community pilot and governed challenges where evidence supports them.
- A NewYou-owned participation path beyond the governed external validation channel.

### High-Level Domain Involvement

- **Primary:** Community; Programmes & Challenges.
- **Supporting:** Habits, Journals & Progress; Entitlements; Privacy & Consent; Content & Media; Communications; Safety & Eligibility; Audit & Evidence.
- **Consumer:** Identity & Access; Analytics.

### Known Gates

- `OQ-023 — BLOCKS_THIS_FP`: first-party community needs operating, privacy, moderation and evidence policy.
- `OQ-019 — BLOCKS_THIS_FP`: challenge completion and recognition rules must be approved before a challenge is published.
- `OQ-018 — BLOCKS_RELEASE_ONLY` when private journals or attachments enter scope.
- `OQ-017` and `OQ-036 — BLOCKS_RELEASE_ONLY`: reminders and notifications are conditional surfaces.
- `OQ-035 — BLOCKS_RELEASE_ONLY`: distributed abuse thresholds are required before high-volume public community release.
- Moderation staffing and safety escalation remain known operational gates.

### Release Significance

This enables first-party community and governed challenges only when external and flagship evidence justifies them. It is a maturity outcome, not an MVP prerequisite.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-013`, with dependency and phase context in §§3.2, 5, 12 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-014 — Foundation programme, habits and reflective progress

### Purpose

This Feature Pack extends the concrete Nuwe Jy programme evidence into a broader behaviour-change capability. It solves the need for structured programmes, habits, private reflections and compassionate progress without making a generic LMS an early prerequisite.

### Intended Outcome

Participants can enrol in a broader approved foundation programme, receive structured lessons and activities and habits, record private reflections and progress, recover after missed days and receive compassionate versioned completion or continuation outcomes.

### Roadmap Position

- Phase 5, Professional care and evidence-led community/behaviour change.
- Relative position: 14 of 17, after Nuwe Jy or equivalent approved programme proof.
- Delivery character: maturity.

### Approved Dependencies

- `FP-005` and `FP-006`.
- `FP-008` or equivalent approved programme proof.
- Approved programme content, translations, completion and communication rules.

### Known Unlocks

- A longer foundation programme and durable habit, journal and reflective-progress capability.
- Broader programme delivery only after the concrete programme evidence supports generalisation.

### High-Level Domain Involvement

- **Primary:** Programmes & Challenges; Habits, Journals & Progress.
- **Supporting:** Content & Media; Entitlements; Plans & Nutrition; Safety & Eligibility; Communications; Community; Privacy & Consent; Audit & Evidence.
- **Consumer:** Identity & Access; Analytics.

### Known Gates

- `OQ-018 — BLOCKS_THIS_FP` for journal or attachment scope: private journal protection and deletion/export cannot be guessed.
- `OQ-019 — BLOCKS_THIS_FP`: programme completion and participation rules need approval before publication.
- `OQ-017` and `OQ-016 — BLOCKS_RELEASE_ONLY`: reminders and publication operations must be resolved for the promised delivery mode.
- `OQ-013 — BLOCKS_RELEASE_ONLY`: required bilingual programme content needs the approved translation path.
- `OQ-009` and `OQ-029 — BLOCKS_RELEASE_ONLY`: retention categories are required before a broader record set enters pilot or release.

### Release Significance

This enables the longer foundation programme and durable habit and reflective-progress capability. It keeps journals private and separate from clinical and community authority.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-014`, with dependency and phase context in §§3.2, 5, 12 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-015 — Event commerce and scarce capacity

### Purpose

This Feature Pack introduces scarce-capacity commerce only after ordinary live access and core operations are proven. It solves the need to sell paid events without treating checkout UI as proof that capacity, payment, ticket issuance and failure handling are correct.

### Intended Outcome

A participant can browse an approved paid event, obtain an expiring capacity hold, pay, receive a ticket, transfer, check in, cancel, refund or receive credit under the accepted event policy, with zero confirmed oversell under concurrency and failure.

### Roadmap Position

- Phase 6, Scarce commerce, experimentation and approved future expansion.
- Relative position: 15 of 17 and the first scarce-capacity commerce path.
- Delivery character: maturity.

### Approved Dependencies

- `FP-002`, `FP-006` and `FP-007`.
- Approved event policy, provider path and event operator.

### Known Unlocks

- A paid event catalogue and capacity-controlled ticket commerce.

### High-Level Domain Involvement

- **Primary:** Events & Live.
- **Supporting:** Commerce; Entitlements; Privacy & Consent; Communications; Content & Media; Audit & Evidence.
- **Consumer:** Identity & Access; Analytics.

### Known Gates

- `OQ-022 — BLOCKS_THIS_FP`: reservation, expiry, waitlist and scarce-capacity protection are the core outcome.
- `OQ-004 — BLOCKS_THIS_FP`: event payment and ticket issuance must reconcile with the provider path.
- `OQ-035 — BLOCKS_THIS_FP`: admission, rate and abuse behaviour is part of safe scarce-capacity operation.
- `OQ-020` and `OQ-021 — BLOCKS_RELEASE_ONLY` for live or recorded event variants.
- `OQ-036` is a conditional release gate for event communications: it applies before an event communication promise is released. Roadmap §14 schedules it at the affected notification boundary; ordinary ticket commerce does not add that dependency.
- `OQ-014 — NON_BLOCKING_FOR_THIS_FP`: ordinary event information delivery is not the capacity authority.

### Release Significance

This enables paid events with capacity and ticket truth. It is intentionally later than governed live sessions and is not part of the core MVP.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-015`, with dependency and phase context in §§3.2, 5, 12 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-016 — First-party experimentation and learning

### Purpose

This Feature Pack creates a governed way to learn from real product decisions after pilot measurement is already available. It solves the need for evidence-backed comparison without allowing experimentation to alter payment, entitlement, safety, consent, accessibility, security, accounting or clinical truth.

### Intended Outcome

Operators can run approved first-party A/B/n experiments on governed web/page and eligible message experiences with stable assignment, exposure evidence, protected-invariant exclusions, authoritative conversion and income reconciliation, privacy/deletion handling and durable auditable learning.

### Roadmap Position

- Phase 6, Scarce commerce, experimentation and approved future expansion.
- Relative position: 16 of 17, after `FP-006` has established a real measurable decision surface.
- Delivery character: maturity.

### Approved Dependencies

- `FP-006`.
- A concrete approved experiment hypothesis and measurable governed surface.
- `FP-002` and/or `FP-009` only when a commerce outcome is the readout.

### Known Unlocks

- Evidence-backed product, content and commerce learning.
- Governed optimisation of public or eligible message surfaces where the approved decision warrants it.

### High-Level Domain Involvement

- **Primary:** Experimentation; Analytics.
- **Supporting:** Content & Media; Communications; Commerce when the experiment readout is commercial; Privacy & Consent; Audit & Evidence.
- **Consumer:** Identity & Access.

### Known Gates

- `OQ-040 — BLOCKS_THIS_FP`: assignment, exposure, measurement, statistical validity, privacy/deletion and failure/recovery proof are the pack outcome.
- `OQ-014 — BLOCKS_RELEASE_ONLY` if experiment-sensitive shared edge delivery is proposed.
- `OQ-013`, `OQ-015`, `OQ-016` and `OQ-036 — NON_BLOCKING_FOR_THIS_FP` until the selected experiment surface uses the corresponding content, search, publication or message mechanism.
- `OQ-030` and `OQ-032 — BLOCKS_RELEASE_ONLY` for participant-facing experiments using external measurement processors.

### Release Significance

This enables auditable product learning after a real decision surface exists. It is not a generic feature-flag replacement and does not become a prerequisite for the first pilot's basic measurement.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-016`, with dependency and phase context in §§3.2, 5, 13 and 14; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

## FP-017 — Approved product-space or market expansion

### Purpose

This conditional Feature Pack protects the approved future direction without inventing a second product or market now. It solves the need to activate a concrete future expansion through shared platform boundaries only after Product, commercial, legal, clinical and market authority approves it.

### Intended Outcome

A concrete, separately approved future product space or market can activate through the shared identity, commerce, entitlement, content, safety, privacy, analytics and operational boundaries without exposing unfinished products or creating unrestricted generic tenancy.

### Roadmap Position

- Phase 6, Scarce commerce, experimentation and approved future expansion.
- Relative position: 17 of 17, last in the current approved sequence and trigger-based.
- Delivery character: later capability.

### Approved Dependencies

- `FP-006`.
- The relevant proven shared capabilities.
- A new explicit Product Law, commercial, legal and clinical direction identifying the product space or market.
- No generic-tenancy assumption.

### Known Unlocks

- A deliberately approved future product-space or market activation.
- Controlled reuse of shared platform capabilities after the concrete expansion receives its own authority and evidence.

### High-Level Domain Involvement

- **Conditional impact set from the Domain Map:** Identity & Access; Privacy & Consent; Temperament; Health Records; Safety & Eligibility; Plans & Nutrition; Content & Media; Programmes & Challenges; Habits, Journals & Progress; Commerce; Entitlements; Community; Events & Live; Professional Care; Communications; Experimentation; Analytics; Audit & Evidence.
- **Primary:** Not assigned at Atlas level. The domain or domains owning the approved expansion outcome must be named by the new Product Law direction.
- **Supporting:** Not assigned before that direction defines the concrete product or market scope.
- **Consumer:** Not assigned before that direction defines the concrete product or market scope. No domain role is inferred merely because the shared platform can be reused.

### Known Gates

- Concrete product or market approval — `BLOCKS_THIS_FP`.
- Market legal, payment, privacy and safety review — `BLOCKS_THIS_FP`.
- Existing core gates — `NON_BLOCKING_FOR_THIS_FP` only where the shared mechanism and protected invariant remain unchanged; affected gates reopen at the relevant release boundary.
- Generic multi-tenant or corporate platform work — `FUTURE_ONLY` and not an approved expansion path by itself.

### Release Significance

This is the controlled path for a future product-space or market activation. It is not a launch dependency and must remain invisible until a concrete approved direction exists.

### Authority Anchors

`05_ROADMAP_v1.0.0.md §6 FP-017`, with dependency and phase context in §§3.2, 5, 13, 14 and 16; `04_DOMAIN_MAP_v1.0.0.md §§3–5`; current gate definitions in `02_OPEN_WORK_v1.2.28.md §5`.

---

# 5. Capability introduction/reuse register

## 5.1 Register rule

This register shows where a shared capability first appears and how later Feature Packs use it. It prevents parallel authority, duplicated semantics and accidental reimplementation of a capability that the Roadmap intends to share.

The register may describe capability-level reuse, extension or composition. It may not prescribe the internal mechanism, package, resource, route or file structure.

## 5.2 Population structure

| Capability | Product / Architecture / Domain anchor | First introduction point | Owning domain or authority | Reusing Feature Packs | Approved extension points | Invariant or safety dependency | JIT boundary | Evidence / gate | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

`REUSE` means the same authority and invariant are used again. It does not mean that later work may copy or fork the authority.

---

# 6. Domain × Feature Pack matrix

## 6.1 Matrix rule

The matrix connects the exact domain names in `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md` to the exact Feature Pack identities in the Roadmap. ATLAS-01 does not copy the row or column population.

The matrix must not turn participation into ownership. A domain may participate by reading, contributing a durable consequence through its owner, exposing a projection or supplying a governed dependency without owning another domain's truth.

## 6.2 Cell vocabulary

Permitted cell labels are:

- `OWNER`: the domain owns the relevant durable truth for this outcome;
- `PARTICIPATES`: the domain contributes an approved capability or outcome;
- `READS`: the domain supplies a governed read dependency;
- `CONSEQUENCE`: the domain receives or performs an owner-controlled durable consequence;
- `PROJECTS`: the domain or its approved projection supplies derived information;
- `GATED`: the relationship exists but cannot proceed until a named gate is resolved;
- `JIT_CONFIRM`: the relationship is visible but implementation-grade scope remains to be confirmed;
- `NOT_IN_SCOPE`: no participation is present in the approved outcome.

## 6.3 Population structure

| Domain \ Feature Pack | _Feature Pack_ | _Feature Pack_ | _Feature Pack_ |
|---|---|---|---|
| _Domain_ | _Cell_ | _Cell_ | _Cell_ |

The final matrix must identify its source section and date. It must not create a second ownership matrix or alter the Domain Map.

---

# 7. Lifecycle coverage register

## 7.1 State-machine rule

Every meaningful domain concept with a lifecycle must eventually have:

- states;
- transitions;
- transition guards;
- side effects;
- terminal states; and
- correction, reversal or invalidation semantics where applicable.

The Atlas records only:

- that the lifecycle exists;
- which domain owns it;
- which upstream semantics are already known;
- which delivery relationships depend on it; and
- the Feature Pack where a complete implementation-grade specification becomes mandatory.

The Atlas must not invent exact Ash/resource-level lifecycle design. Exact state names, actions, validations, persistence representation, asynchronous mechanisms and other implementation semantics remain JIT unless an upstream authority already froze them.

If a later delivery projection requires missing lifecycle semantics, the Atlas marks the entry `FULL_SPEC_REQUIRED` or `STOPPED` and routes it. It does not infer the missing transition.

## 7.2 Population structure

| Lifecycle-bearing concept | Owning domain | Upstream lifecycle evidence | Atlas coverage | First delivery relevance | Feature Pack requiring full specification | Guards / side effects known at broad level | Terminal / correction / reversal concern | JIT dossier need | Blocking gate / STOP | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |  |

---

# 8. Cross-domain dependency map

## 8.1 Dependency rule

The dependency map records domain-level direction and delivery impact. It does not define calls, events, messages, topics, queues, schemas or modules.

Permitted edge classes are:

- authoritative read dependency;
- owner-controlled command or durable consequence;
- projection or observation dependency;
- privacy, deletion or consent orchestration;
- audit or evidence dependency;
- external-provider evidence dependency; and
- future or gated dependency.

Each edge must identify the source domain, target owner, business purpose, authority direction, affected Feature Packs, broad failure consequence and exact upstream reference.

## 8.2 Cycle rule

Read composition can be cyclic without creating a control defect. A circular authoritative dependency exists when domains require one another to mutate authoritative state in an unresolvable loop. That condition is a global STOP.

The Atlas must preserve the Domain Map rules that:

- one domain owns each major durable truth;
- relationships do not transfer mutation authority;
- cross-boundary writes invoke the owner;
- projections, caches, analytics, PubSub observations and provider state do not become hidden authority; and
- privacy and audit orchestration does not acquire ownership of the records it governs or proves.

## 8.3 Population structure

| From | To / owner | Edge class | Delivery effect | Lifecycle or invariant affected | Failure / recovery concern | Feature Pack relationship | Upstream reference | Readiness |
|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |

---

# 9. Participant journey progression

## 9.1 Journey rule

This view may show how participant outcomes progress across the Roadmap, using approved Product Law journey language and the relevant Feature Pack outcome. It must not add a promise, entitlement, clinical route or product-space behaviour absent from upstream authority.

It must distinguish:

- public discovery and free access;
- protected or purchased access;
- safety and eligibility routing;
- delivery, use, feedback and recovery;
- recurring or programme progression;
- professional escalation; and
- deletion, correction, withdrawal and long-term access boundaries where relevant.

These are planning lenses. They are not frontend routes, screens or implementation workflows.

## 9.2 Population structure

| Participant outcome / milestone | Product Law anchor | First relevant Feature Pack | Prerequisite relationship | Reused capability | Safety / privacy boundary | Feedback or recovery seam | Later progression | JIT boundary | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 10. Staff/operator journey progression

## 10.1 Journey rule

This view follows the operating model's workflow-first approach. It may show how staff, reviewers, operators, moderators, analysts and other approved actors encounter work, exceptions, decisions and evidence as capabilities enter operation.

Operator navigation groupings, work queues, dashboards and timelines are projections over domain-owned truth. They do not create a universal Task domain or a second business-write API.

## 10.2 Population structure

| Actor / role | Operating outcome | Work or decision encountered | Required authority / relationship | Upstream operating anchor | First relevant Feature Pack | Exception / escalation path | Evidence / audit need | JIT boundary | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 11. Frontend surface progression

## 11.1 Frontend rule

This view translates approved participant and operator outcomes into broad experience progression. It may show public, participant, staff, operator, dashboard, publishing or support surface categories.

The frozen `FRONTEND_EXPERIENCE_SYSTEM` remains subordinate to Product Law, Architecture, Domain Law and the Roadmap. The Atlas may record an experience seam, but it must not freeze:

- routes or endpoints;
- Phoenix or LiveView module names;
- exact component or file structures;
- token values, palette, fonts or package versions;
- frontend business state machines; or
- provider configuration.

Frontend presentation state remains distinct from domain lifecycle state. Accessibility, bilingual delivery, SEO, privacy-safe measurement and graceful degradation are recorded as cross-cutting obligations when relevant.

## 11.2 Population structure

| Experience surface category | Actor / journey | Outcome supported | Authority / access dependency | Frontend contract anchor | Feature Pack progression | Accessibility / bilingual / SEO concern | Analytics boundary | JIT frontend contract need | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 12. Data authority and projection flows

## 12.1 Authority rule

The Atlas preserves the frozen evidence-led architecture:

- each durable business truth has one domain owner;
- PostgreSQL remains the default authority for structured business state;
- durable binary ownership and business metadata remain governed by their approved boundaries;
- external provider responses are evidence until the owning domain reconciles them;
- projections, analytics, caches, LiveView state and realtime observation are not authoritative business state; and
- current privacy, consent, access and safety policy is checked before protected delivery or projection use where required.

The Atlas records authority and projection relationships at broad level. It must not turn a flow label into a storage schema, key format, cache contract or transport design.

## 12.2 Flow classes

| Flow class | Atlas question |
|---|---|
| Authoritative state | Which domain owns the fact, and which upstream rule proves that ownership? |
| Durable consequence | Which owner receives a consequence after an authoritative transition? |
| External evidence | Which domain reconciles provider evidence and handles ambiguity? |
| Derived projection | Which source facts are projected, for what purpose, and with what broad freshness and rebuild expectation? |
| Privacy lifecycle | Which authority governs consent, deletion, retention, export or suppression across owners? |
| Analytics / measurement | Which governed facts support the measure, and what remains non-authoritative? |
| Presentation / observation | Which current authority is represented, and what happens when it is stale, unavailable or restricted? |

## 12.3 Population structure

| Source authority | Consuming surface / domain | Flow class | Purpose | Broad freshness | Privacy / deletion boundary | Failure or withdrawal effect | Feature Pack relationship | JIT design trigger | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 13. Integration progression

## 13.1 Integration rule

The Atlas may show when an external provider or integration becomes relevant to an approved outcome, which domain owns the platform meaning, what evidence must be validated and which failure state must remain visible.

It must not freeze provider configuration, retry values, routes, credentials, webhook names, package choices, deployment topology or provider-specific state as platform law.

Every populated integration entry must identify:

- the approved capability it supports;
- the platform-owned authority boundary;
- the external evidence or service dependency;
- the relevant legal, clinical, privacy, security or operational gate;
- the broad success, pending, degraded and recovery classes; and
- the Feature Pack and JIT contract where exact behaviour becomes mandatory.

## 13.2 Population structure

| Integration / provider capability | Owning platform domain | Approved outcome | External evidence required | Gate / authority | Broad failure class | First relevant Feature Pack | Reuse / replacement seam | JIT contract need | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 14. Analytics and measurement progression

## 14.1 Measurement rule

Analytics remains derived from governed authoritative facts. The Atlas may show when a product, operational or learning measure becomes necessary and how the measure relates to a Feature Pack or release decision.

The view must preserve these boundaries:

- native NewYou facts remain authoritative for payment, entitlement, safety, eligibility, content, participant and approved conversion outcomes;
- purpose-built canonical dashboards are preferred over an unrestricted dashboard builder;
- experiment assignment and decision authority remain distinct from Analytics measurement;
- external analytics, search and provider dashboards are complementary evidence; and
- privacy, consent, minimisation, deletion and restricted access apply to measurement.

ATLAS-01 does not create a KPI catalogue, metric contract, dashboard, experiment or analytics implementation.

## 14.2 Population structure

| Measure / evidence need | Semantic owner | Authoritative source facts | Feature Pack / release purpose | Freshness / quality concern | Privacy / deletion boundary | Experiment relationship | Operational response | JIT analytics need | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 15. Security, privacy and safety escalation

## 15.1 Escalation rule

The Atlas must make the first delivery point for a protection visible. It must not lower a protection to preserve sequencing or convenience.

The following priorities remain in force:

```text
clinical and safety authority
    → privacy, consent and security
    → payment, entitlement and accounting integrity
    → confirmed capacity and inventory integrity
    → correctness and recoverability
    → freshness, latency, convenience and UI polish
```

The ordering is a planning priority, not a substitute for the source law. Temperament never overrides clinical or safety authority. A protected data path requires current purpose, policy and access checks. A material correction, withdrawal, revocation or deletion effect must remain visible across affected projections and delivery surfaces.

## 15.2 Population structure

| Protection concern | Protected outcome / data class | First relevant Feature Pack | Upstream authority | Trigger for escalation | Required owner / expert authority | Broad consequence if unresolved | JIT dossier / proof need | Status |
|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |

The Atlas must record unresolved clinical, legal, professional, provider or privacy policy as a gate or STOP. It must not invent thresholds, wording, retention periods, consent interpretations or access exceptions.

---

# 16. Performance and scaling progression

## 16.1 Performance rule

The Atlas preserves the frozen, evidence-led architecture:

- record authoritative data layer and broad hot, warm or cold character;
- record broad concurrency sensitivity, burst behaviour and DB or async pressure;
- record possible acceleration candidates only as candidates;
- record the evidence that would justify acceleration; and
- keep PostgreSQL authority and simplest-correct-path-first doctrine intact unless upstream Architecture Law says otherwise.

The Atlas must not introduce Redis, ETS/Cachex, GenServers, replicas, specialist services, microservices, queue topology or caching merely because they may be useful. Any such mechanism remains evidence-gated and JIT unless already mandated upstream.

Performance entries describe future proof obligations. They do not claim measured latency, capacity, workload, safe envelope or breakpoint evidence before the appropriate proof stage exists.

## 16.2 Population structure

| Capability / flow | Authoritative layer | Temperature | Concurrency / burst character | DB / async pressure | Candidate acceleration | Evidence required before use | Architectural Proof / Hardening stage | JIT OQ-039 need | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 17. Failure and recovery progression

## 17.1 Failure rule

The Atlas may show which broad failure and recovery classes become relevant as an outcome enters delivery. It must preserve the architecture's distinction between authoritative refusal, pending external ambiguity, durable asynchronous recovery, stale or unavailable projection, provider outage, overload, correction or withdrawal, deletion/restore behaviour and release rollback.

A failure class is a delivery seam. It is not an implementation choice.

## 17.2 Population structure

| Outcome / flow | Failure class | Authority affected | Participant / operator effect | Recovery or correction expectation | Proof / hardening stage | Feature Pack relationship | JIT need | Status |
|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |

The Atlas must not claim recovery is complete until the relevant evidence exists at the correct stage. A provider response, queue state, projection or UI message is not proof of authoritative success by itself.

---

# 18. Architectural proof map

## 18.1 Proof rule

The Atlas may identify likely architectural-proof boundaries and the invariant or failure pressure that makes them material. It must not create a tracer bullet or decide a final proof task.

The affected Feature Pack later decides whether its requirement is `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`, as required by the Roadmap and Open Work contract. The Atlas may record that decision only after the approved lower-level artifact exists.

## 18.2 Population structure

| Architectural claim / path | Upstream DEC / ARC / FLOW anchor | Affected Feature Pack | Affected domains | Hard invariant | Failure / pressure to prove | Existing evidence relationship | Required proof stage | Final proof decision owner | JIT task dependency | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |  |

No `TB-nnn` is created by ATLAS-01. No executable proof is prepared here.

---

# 19. Horizontal hardening map

## 19.1 Hardening rule

The Atlas may identify categories of hardening that a proven capability could require. It must tie them to evidence or an explicit release gate. It must not create `HH-nnn` work or add a hardening category merely because a technology exists.

Possible categories include load and contention, provider failure, queue saturation, restore and deletion replay, security, accessibility, observability, multi-node behaviour, cache stampede, migration pressure and operational rehearsal. The applicable category is determined by the affected outcome and evidence.

## 19.2 Population structure

| Capability / outcome | Hardening category | Evidence or gate trigger | Affected invariant | Relevant Feature Pack | Proof already available | Release / readiness effect | JIT HH contract need | Status |
|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |

---

# 20. Future-extension seam register

## 20.1 Seam rule

This register protects approved future direction without designing it early. A seam may be recorded only when an upstream source identifies an approved future capability, a controlled expansion path or a legitimate reuse boundary.

The Atlas must not create generic tenancy, unrestricted product spaces, parallel commerce or entitlement systems, or specialist infrastructure without an approved outcome and the authority needed to support it.

Each seam must state:

- the current authority that creates or permits the future direction;
- what must remain stable for reuse;
- what new authority, policy or evidence will be required;
- the trigger for moving the seam into a Feature Pack;
- what is explicitly not being designed now; and
- the STOP condition if the future direction conflicts with current law.

## 20.2 Population structure

| Future seam | Upstream basis | Stable shared boundary | Future trigger | New authority / evidence required | Explicitly deferred detail | Risk if closed early | Candidate Feature Pack | JIT boundary | Status |
|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |

---

# 21. Feature Pack delivery projections

## 21.1 Projection rule

The delivery projection is the Atlas's medium-resolution view of how a Feature Pack travels through preparation, proof, slices, hardening and readiness. It may show dependencies and expected evidence without becoming a Feature Pack contract.

The Roadmap remains authoritative for the Feature Pack outcome and sequencing. The Feature Pack contract remains authoritative for implementation-entry scope and gates. The Atlas must link to both and must not substitute for either.

## 21.2 Population structure

| Feature Pack | Roadmap phase | Outcome anchor | Entry dependencies | Capability movement | Domain / lifecycle impact | Journey / frontend impact | Integration / measurement impact | Safety / privacy impact | Performance / failure pressure | Proof expectation | Hardening expectation | Readiness dependency | Atlas status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |  |  |  |  |

This view may project a relationship such as "reuse existing capability" or "full lifecycle specification required here". It may not project exact implementation tasks.

---

# 22. Cross-Feature-Pack risk register

## 22.1 Risk rule

The risk register tracks a risk that crosses an outcome boundary or could make later reuse unsafe. A risk must have an authority source, an owner or routing target, a trigger and a response boundary.

Risk entries are not issue tickets, implementation tasks or replacement Product/Architecture/Domain decisions.

## 22.2 Population structure

| Risk | Feature Packs affected | Domain / capability affected | Risk class | Upstream evidence | Trigger | Owner / authority route | Consequence | Mitigation boundary | JIT / proof / hardening dependency | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |  |

---

# 23. Development navigation rules

The Atlas is used for navigation in this order:

1. Start with the approved Roadmap outcome or Feature Pack.
2. Load the applicable Product, Architecture, Domain and Roadmap sources.
3. Use the Atlas to find shared capabilities, domain participation, lifecycle coverage, journeys, integrations, measurement, risks, proof and hardening relationships.
4. Confirm every Atlas statement against its exact upstream source.
5. Treat a missing implementation detail as a JIT boundary, not as an invitation to fill it in here.
6. Prepare a Feature Pack only when a separate task authorises the applicable Phase 7 work.
7. Create only the JIT Domain Dossiers required by that approved Feature Pack.
8. Resolve or explicitly exclude blocking gates before the final Feature Pack contract.
9. Choose `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET` in the approved Feature Pack contract.
10. Create TB, VS, HH or TOON artifacts only under the authority and sequence already defined upstream.
11. Recheck Atlas relationships after an approved upstream amendment. Do not patch around a changed authority inside the Atlas.
12. Stop when a relationship cannot be proven without missing policy, ownership, mechanism or evidence.

This ATLAS-02 task does not perform steps 6 through 10. It populates only the Feature Pack Portfolio Register. ATLAS-01 ended after defining the navigation and lifecycle governance contract; ATLAS-02 does not begin ATLAS-03 or any Phase 7 deliverable.

---

# 24. Atlas governance/change policy

## 24.1 Change classes

Atlas changes are classified before editing:

| Change class | Allowed handling |
|---|---|
| Editorial clarification | May correct wording without changing a relationship or authority claim. Preserve source references. |
| Derived navigation correction | May correct an Atlas relationship when current upstream sources prove the correction. Record the source and review the affected views. |
| Structural Atlas change | May add or refine a view or classification only through an explicit working-artifact review. It must not create a new authority layer. |
| Upstream amendment required | Stop Atlas work and route the issue to the authority that owns the rule. |
| Implementation detail required | Stop the Atlas entry and route the detail to the affected Feature Pack/JIT Domain Dossier. |

Working changes must preserve the artifact status. A working Atlas update does not freeze the Atlas and does not modify the current-authority manifest unless a separate governance decision requires it.

## 24.2 Mandatory routing

| Finding | Route |
|---|---|
| Upstream contradiction | **STOP** and route to the conflicting upstream authority. |
| Missing Product policy | Product Law and a formal Product decision or gate. |
| Architecture mechanism conflict | Architecture Law / Architecture authority. |
| Ownership or invariant conflict | Domain Law / Domain Map. |
| Sequencing or scope conflict | Roadmap authority. |
| Missing implementation semantics | Affected JIT Domain Dossier under the selected Feature Pack. |
| Execution ambiguity | TB / VS / HH contract, after the upstream gates are satisfied. |

The Atlas must state the exact source references, the unresolved question, the route and the downstream effect. It must never silently repair upstream authority.

## 24.3 Revalidation

Revalidate the affected Atlas entries when:

- a Product, Architecture, Domain or Roadmap source is amended;
- an upstream gate changes status;
- proof evidence changes the known safe boundary;
- a release or hardening result contradicts a planning assumption; or
- a new approved future direction changes a shared capability seam.

Revalidation may mark an entry stale, gated or stopped. It may not hide the change by rewriting history.

---

# 25. Global STOP conditions

STOP Atlas work and report the exact source references and required authority level if any of the following occurs:

- Product Law conflicts;
- Architecture Law conflicts;
- Domain ownership is ambiguous;
- a circular authoritative dependency is found;
- Roadmap sequencing conflicts;
- an unresolved expert or vendor OQ is required to continue;
- legal, clinical, commercial or provider policy would need to be invented;
- Atlas work requires concrete implementation semantics;
- the Atlas would effectively amend a Feature Pack outcome;
- current authority documents disagree materially;
- existing foundation integrity validation fails;
- the work would create or imply an exact Ash Resource or action name;
- the work would create or imply schemas, tables, columns, migrations, indexes, Redis keys or structures, TTLs, Oban workers or queues, PubSub topics, GenServer modules, routes, API endpoints, frontend component/file structures, package choices or versions, deployment sizing or source code;
- the work would create a TOON implementation task;
- the work would begin FP-001 preparation or any other Phase 7 deliverable; or
- the work would create Architectural Proof, Vertical Slice, Horizontal Hardening or release/readiness artifacts.

When STOP occurs, record:

1. the exact source path and section or identifier;
2. the finding and the evidence that produced it;
3. the authority level that must decide or correct it;
4. the affected Atlas view and Feature Pack relationship;
5. the safe downstream action after resolution; and
6. the fact that no Atlas-level guess was made.

---

# 26. Closure/readiness audit

## 26.1 ATLAS-01 completion standard

This subsection records the completion standard for the ATLAS-01 contract layer. It remains the historical baseline for the ATLAS-02 update.

ATLAS-01 is ready for review only when the evidence shows all of the following:

| Requirement | Required evidence |
|---|---|
| Authority contract exists | This artifact names the upstream hierarchy, source set and subordinate role of the Atlas. |
| Working status is explicit | The artifact is marked derived, working and non-authoritative, and says it does not authorise implementation. |
| Scope is explicit | The artifact defines medium-resolution navigation across the complete approved roadmap. |
| Delivery lifecycle governance is explicit | The Delivery Lifecycle Governance section defines the Roadmap-to-next-decision flow, Feature Pack, TB, VS and HH lifecycles, Grill-Me gates, handoff, continuation review and evidence/closure requirements. |
| Decision escalation is explicit | The Decision Escalation Matrix routes discoveries to the lowest correct authority and defines lower-level boundaries, escalation response and STOP conditions. |
| Future templates remain conceptual | The future template registry names the expected files and their purposes without creating any files under `docs/templates/`. |
| Proposed views are defined | Sections 3 through 22 define the mature-platform view, portfolio map, registers, matrices, journeys, flows, proof, hardening, seams and risks without substantive pack analysis. |
| Lifecycle boundary is explicit | Section 7 records the eventual state-machine requirements and limits Atlas lifecycle coverage to existence, ownership, known upstream semantics and the Feature Pack where full specification becomes mandatory. |
| Performance boundary is explicit | Section 16 preserves PostgreSQL authority, evidence-led acceleration and simplest-correct-path-first sequencing. |
| Governance is explicit | Section 24 defines amendment classes and routes each finding to the correct authority. |
| STOP conditions are explicit | Section 25 includes upstream contradiction, ambiguity, unresolved gates, implementation semantics, foundation integrity failure and scope expansion. |
| No authority source was changed | `git diff` shows only the requested working artifact, apart from an explicitly approved repository convention if one exists. |
| Foundation remains intact | The existing foundation integrity audit and applicable documentation tests pass. |
| No implementation or lower-level preparation was created | No product code, Feature Pack preparation, JIT Domain Dossier, TB, VS, HH or TOON exists as part of ATLAS-01. |
| Atlas remains unfrozen | No freeze verdict or current-authority promotion is made by this artifact. |

## 26.2 ATLAS-01 review protocol

The ATLAS-01 delivery report used the following protocol:

1. inspect the full diff;
2. confirm the branch and changed-file set;
3. run the existing applicable foundation integrity and documentation checks;
4. run `git diff --check`;
5. confirm no implementation tooling or implementation artifact was introduced;
6. confirm no Feature Pack, JIT dossier, TB, VS, HH or TOON was prepared;
7. record any contradiction found, or state that none was found; and
8. report `PASS` only when every requirement above is evidenced. Otherwise report `STOP` with the exact route.

ATLAS-01 ended with the contract captured above. ATLAS-02 adds only the Feature Pack Portfolio Register under that same authority boundary. The next Atlas content layer must be separately named and authorised; this artifact does not begin ATLAS-03.

## 26.3 ATLAS-02 completion standard

ATLAS-02 is ready for review only when the evidence shows all of the following:

| Requirement | Evidence in this artifact |
|---|---|
| Complete portfolio coverage | The summary and register contain all 17 approved Roadmap Feature Packs in Roadmap order. |
| Required entry structure | Each pack has Purpose, Intended Outcome, Roadmap Position, Approved Dependencies, Known Unlocks, High-Level Domain Involvement, Known Gates, Release Significance and Authority Anchors. |
| Authority fidelity | Purpose, outcomes, positions, dependencies, unlocks and release significance derive from the frozen Roadmap; domain names and ownership boundaries derive from the frozen Domain Map; gate references remain tied to current authority. |
| Dependency and gate discipline | No dependency, unlock, gate or domain role is added by inference; conditional FP-017 remains explicitly unassigned until its required future direction exists. |
| Navigation scope | The register remains outcome-level delivery navigation and does not become implementation planning or another Atlas view. |
| Working boundary | The artifact remains derived, working, non-authoritative and unfrozen, and does not begin ATLAS-03. |
