# Delivery Atlas working v0.1.0

- **Artifact:** `ATLAS-01`
- **Document status:** **DERIVED DELIVERY PLANNING ARTIFACT**
- **Working state:** **WORKING / NON-AUTHORITATIVE**
- **Authority boundary:** **DOES NOT MODIFY PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW**
- **Implementation boundary:** **DOES NOT AUTHORISE IMPLEMENTATION**
- **Purpose:** Define the first medium-resolution delivery-navigation contract for the complete approved NewYou roadmap.
- **Scope:** Feature Pack relationships, shared capability movement, lifecycle coverage, journeys, cross-domain interaction, integrations, measurement, risk, proof, hardening and future-extension visibility.
- **Current content state:** Contract and empty population structure only. No Feature Pack, domain, lifecycle, journey or implementation analysis is populated by ATLAS-01.
- **Freeze state:** Not frozen. A later freeze requires a separate governance decision.

This document is the initial Delivery Atlas working artifact. It gives later delivery planning a common set of views and labels and defines the controlled lifecycle that moves an approved roadmap outcome through preparation, implementation, evidence, handoff and the next delivery decision. It leaves implementation-grade design to the affected Feature Pack and just-in-time (JIT) Domain Dossiers.

The working artifact remains outside `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` unless an explicit repository governance decision requires a later metadata change. ATLAS-01 does not change that manifest.

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

ATLAS-01 defines the views, labels, entry rules and STOP rules for the complete approved roadmap. It does not populate substantive Feature Pack analysis. Later Atlas work may populate a view only from current upstream authority, approved evidence and the relevant governance decision.

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

ATLAS-01 defines the map but does not reproduce or analyse individual Feature Packs. It does not select FP-001 or begin Phase 7.

## 4.2 Population structure

| Feature Pack | Roadmap anchor | Outcome relationship to mature platform | Entry dependencies | Introduces | Reuses | Extends | Affected domains | Lifecycle and journey impact | Gates | Proof boundary | Hardening categories | Future seams | Cross-pack risks | Atlas readiness |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _Populate in a later Atlas task._ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Each future entry must point back to the corresponding Roadmap section. The Atlas may summarize a Roadmap relationship, but any disagreement is a Roadmap STOP and must not be corrected inside the Atlas.

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

This task does not perform steps 6 through 10. ATLAS-01 ends after defining the navigation and lifecycle governance contract.

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

ATLAS-01 is ready for review only when the evidence shows all of the following:

| Requirement | Required evidence |
|---|---|
| Authority contract exists | This artifact names the upstream hierarchy, source set and subordinate role of the Atlas. |
| Working status is explicit | The artifact is marked derived, working and non-authoritative, and says it does not authorise implementation. |
| Scope is explicit | The artifact defines medium-resolution navigation across the complete approved roadmap. |
| Delivery lifecycle governance is explicit | The Delivery Lifecycle Governance section defines the Roadmap-to-next-decision flow, Feature Pack, TB, VS and HH lifecycles, Grill-Me gates, handoff, continuation review and evidence/closure requirements. |
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

## 26.2 Review protocol

The ATLAS-01 delivery report must:

1. inspect the full diff;
2. confirm the branch and changed-file set;
3. run the existing applicable foundation integrity and documentation checks;
4. run `git diff --check`;
5. confirm no implementation tooling or implementation artifact was introduced;
6. confirm no Feature Pack, JIT dossier, TB, VS, HH or TOON was prepared;
7. record any contradiction found, or state that none was found; and
8. report `PASS` only when every requirement above is evidenced. Otherwise report `STOP` with the exact route.

ATLAS-01 ends here. The next task must be separately named and authorised. This artifact does not execute the next task and does not begin ATLAS-02.
