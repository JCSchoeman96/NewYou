# Health / Safety / Plans Pre-JIT Contract — Working Consolidation v0.1.2

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT CONTRACT
- **Purpose:** Small implementation-facing planning contract for future FP-004 / FP-005 JIT work.
- **Authority:** None. This document cannot amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Feature Pack contracts or JIT Domain Dossiers.
- **Implementation:** NOT AUTHORISED.
- **v0.1.2 hygiene patch:** No contract semantics changed. This successor only standardises the canonical `Phase 7C Final Feature Pack Contract` terminology and replaces chat-specific “uploaded” source wording with durable source-artifact wording.
- **Source evidence:** `HEALTH_SAFETY_PLAN_PREJIT_DISCOVERY_WORKING_v0.42.0.md`, rebuilt against current live repository authority.
- **Conflict rule:** Live higher authority always wins. If a later JIT task discovers a contradiction, stop at the correct authority level rather than repairing it here.

## Live authority baseline used for this consolidation

Verified against the live `JCSchoeman96/NewYou` default branch at commit:

`c4ed5ce95b151c060c104bbec6b25edefb271814`

Current routed authority:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.39.md`
5. `03_ARCHITECTURE_v1.1.0.md`
6. `04_DOMAIN_MAP_v1.1.0.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.0.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` only when frontend/experience planning is in scope.

The current `v1.3.0` Product amendment and `v1.1.0` Architecture/Domain/Roadmap amendments are additive for Research & Feedback, Voting & Balloting, Interactive Tools and Platform Member Reference. They do not alter the Health → Safety → Plans authority model or FP-004/FP-005 sequencing used here.

The source `HEALTH_SAFETY_PLAN_PREJIT_DISCOVERY_WORKING_v0.42.0.md` remains working evidence only.


## 1. Scope

This contract preserves only the durable design constraints needed to plan and prove the Health → Safety → Eligibility → Plan path without repeatedly loading the full discovery artifact.

It applies primarily to:

- FP-004 — safe health onboarding and deterministic eligibility;
- FP-005 — safe seven-day plan, purchased library and basic feedback;
- later plan review/adjustment and professional-review work only where a stable boundary must be preserved now.

It does **not** decide:

- clinical eligibility thresholds or case matrices;
- calculation values, limits or adjustment thresholds;
- professional-service commercial promises;
- exact refund/credit remedies;
- exact retention periods;
- exact Ash Resources, actions, schemas, tables, indexes or constraints;
- exact transaction, worker, queue, cache, PubSub or process design;
- exact UI routes/components;
- package selection.

The contract is intentionally conceptual. A distinction below does **not** imply a separate Resource, table, process, service or queue.

## 2. Governing ownership

Every durable truth retains one authoritative owner.

| Truth | Owner | Boundary |
|---|---|---|
| Participant health/lifestyle facts, evidence, provenance and historical observations | **Health Records** | Facts are not safety decisions. |
| Eligibility evaluations, current safety authority, restrictions, governed overrides and Safety Cases | **Safety & Eligibility** | Safety interpretation is not Plan authority. |
| Plan-generation business intent/outcome, immutable Plan Versions, Plan review/adjustment outcomes and Plan provenance | **Plans & Nutrition** | Plans must obey Safety and cannot reinterpret raw health evidence to bypass it. |
| Purpose-specific consent, deletion/retention orchestration and data-right lifecycle | **Privacy & Consent** | Orchestration does not acquire ownership of domain records. |
| Commercial purchase, payment, refund and subscription contract truth | **Commerce** | Payment/commercial truth is not access truth. |
| Access/right identity, validity, expiry, revocation and consumable entitlement history | **Entitlements** | Entitlement truth is not Plan truth. |
| Practitioner relationship, professional review/case/outcome evidence and professional capacity | **Professional Care** | Professional Care must route Safety changes through Safety and Plan changes through Plans. |
| Behavioural/progress/adherence entries | **Habits, Journals & Progress** | Logging is input evidence; Plans owns any later adjustment decision. |
| Governed plan/content dependencies and publication/withdrawal state | **Content & Media** where applicable | Content authority does not become Plan fulfilment authority. |
| Cross-cutting evidence | **Audit & Evidence** where current law requires it | Evidence is not source-domain business truth. |

Cross-domain mutation always invokes the owner. Projections, analytics, caches, worker state, provider state, PubSub and LiveView are never alternate business authority.

Core separation:

`health fact ≠ safety interpretation ≠ eligibility outcome ≠ plan decision ≠ commercial right ≠ entitlement right`

## 3. Canonical concepts

These are conceptual contracts only.

### 3.1 Health evidence semantics

A health-related update must preserve its business meaning. At minimum distinguish:

- **new observation** — a later valid measurement/observation;
- **genuine state change** — earlier information may have been correct, but the participant later changed;
- **correction/retraction** — earlier information was wrong when made or is withdrawn by an authorised source;
- **verification/provenance change** — evidentiary status changes without necessarily changing the underlying assertion;
- **contradiction/conflict** — material evidence cannot safely be reduced to one unqualified current value.

For safety-sensitive facts, “newest wins” is not a valid universal rule. Provenance is relevant evidence but is not a universal clinical hierarchy.

When materially conflicting safety evidence remains unresolved, the system must fail closed for automated personalisation without fabricating which source is clinically correct.

### 3.2 Temporal truth

Historical reconstruction must distinguish, where applicable:

- observation/effective time — when the fact applied in the participant’s world;
- authoritative known/received time — when the owning boundary durably accepted the evidence;
- decision/use time — when Safety or Plans relied on it;
- freshness/current-usability — whether that evidence is still permitted for the current purpose;
- provenance/source and later correction/retraction.

Async processing time is not authoritative known time. If NewYou durably accepted safety-relevant evidence before a decision, downstream delay cannot make the platform pretend it did not know it.

A later correction may establish that an earlier assertion was wrong while still preserving that NewYou genuinely possessed and relied on it before the correction became known.

### 3.3 Intake readiness

Health intake is automation-grade evidence, not merely a form-completion flag.

Completion/readiness is purpose- and version-relative. The platform must be able to establish that the current required information for the applicable pathway is:

- present where required;
- semantically structured;
- sufficiently current;
- appropriately reconfirmed for safety-sensitive facts;
- provenance-aware;
- free of unresolved safety conflict;
- evaluated under the applicable governed intake/Safety protocol.

A historical “completed intake” does not permanently establish current automation readiness.

### 3.4 Eligibility Evaluation, Safety Impact Assessment and Safety Case

Do not collapse three different concerns:

- **Eligibility Evaluation:** determines the governed eligibility outcome for the relevant purpose.
- **Safety Impact Assessment:** determines what a new fact, correction, protocol change or other event means for current dependent activity/Plans.
- **Safety Case:** the stateful governed process used when an actual safety workflow is required.

The Product-authorised eligibility outcomes remain:

- `eligible_automated`
- `general_wellness_only`
- `professional_review_required`
- `insufficient_information`

These outcomes are not worker states and are not substitutes for a Safety Case lifecycle.

### 3.5 Generation Request, Generation Attempt and Plan Version

These are independent lifecycle dimensions.

**Generation Request** is the durable logical business intent to produce one authorised Plan deliverable from a defined basis. It owns the business idempotency identity.

**Generation Attempt** is one execution attempt against an open Request. Technical retries produce new Attempt history; they do not create new participant business intent.

**Plan Version** is an immutable Plan artifact/version in the governed Plan lifecycle. Review-gated pathways may contain multiple immutable pre-fulfilment Plan Versions before one final deliverable is fulfilled.

Therefore:

`Request ≠ Attempt ≠ Plan Version`

and:

`generated ≠ fulfilled`

## 4. Safety and automation admission

### 4.1 Positive admission

Automated personalised Plan generation is allowed only by positive proof that the participant is inside an approved automated pathway.

Absence of a detected blocker is not sufficient.

Admission requires every applicable current condition to pass, including current intake, reconfirmation, conflict handling, Safety authority, supported pathway and other governed prerequisites.

Missing, stale, conflicting, unsupported or professionally gated conditions must not be interpreted as permission.

### 4.2 Safety permission and Plans capability are separate

Safety & Eligibility answers:

> Is automated personalisation currently permitted for this participant and purpose?

Plans & Nutrition separately answers:

> Does the current approved Plans capability contain a valid deterministic path that can satisfy this authorised case?

A participant can truthfully be `eligible_automated` while Plans cannot produce a valid Plan for the exact hard constraints or approved catalogue.

Plans must not falsify that as:

- `professional_review_required` when no professional judgement is required;
- `insufficient_information` when information is complete;
- `general_wellness_only` merely because software/catalogue capability is incomplete.

### 4.3 Safety-relevant changes and corrections

A safety-relevant correction or new material fact is a Safety event when it could affect current authority.

Where current Safety reevaluation is required:

- new personalised actions must not proceed under stale authority;
- in-flight fulfilment must revalidate and fail closed if the old authority no longer permits delivery;
- an active Plan follows the governed Safety consequence, including `safety_paused` where applicable;
- historical eligibility and Plan provenance are not rewritten.

The exact clinical impact matrix remains behind existing clinical gates.

## 5. Plan input and provenance contract

### 5.1 Input classification

Plan-relevant information should be reasoned about in three conceptual classes:

- **Direct Plan Input** — information Plans legitimately needs to make the approved Plan decision.
- **Safety-Derived Plan Constraint** — authoritative restriction/permission supplied by Safety; Plans does not independently recompute the underlying clinical judgement.
- **Not a Plan Input** — information that may exist elsewhere but is not necessary for the Plan decision.

This classification is a privacy and authority boundary, not a schema prescription.

### 5.2 Hard constraints versus soft preferences

A **hard constraint** must be satisfied for the candidate Plan to be valid. The engine must not silently weaken it to get a result.

A **soft preference** may influence selection/presentation within the approved rules but cannot override safety or other mandatory constraints.

If an otherwise authorised Request cannot satisfy all mandatory hard constraints under current approved Plans capability, the Request may become `unfulfillable`. That is a truthful Plans outcome, not a Safety failure.

The commercial remedy for that outcome remains an open Product/Commerce issue and must not be invented by Plans.

### 5.3 Immutable Generation Input Basis

Each logical generation uses an immutable minimum-necessary basis identifying the material authorised inputs and versioned authorities used to generate the candidate.

The basis must support historical explanation without depending on mutable “current” values.

It must not become a copy of entire Health Records or Safety history. Prefer the minimum material snapshot/reference needed to explain and reproduce the Plan decision.

### 5.4 Immutable Plan Result Provenance

Pre-generation input/dependency basis and successful result provenance are different.

Result provenance identifies the exact governed versions actually selected/used in the resulting Plan: calculation protocol, ruleset, relevant content/recipe/substitution versions, language/presentation versions and other material dependencies.

A delivered Plan Version must link enough evidence from both sides to answer:

- what authorised inputs/constraints were used;
- what exact governed result dependencies were selected;
- why that Plan was produced;
- what current authority allowed final delivery.

Historical provenance does not itself create continuing current-use authority.

## 6. Generation Request lifecycle

The compressed working Request lifecycle is:

`open → fulfilled | cancelled | invalidated | unfulfillable`

All four outcomes other than `open` are terminal. A terminal Request never reopens.

### 6.1 `open`

The logical business request exists and has not reached a terminal outcome.

An open Request may be queued, executing, retrying, waiting for review or waiting for operator intervention without adding those execution/work states to the Request lifecycle.

### 6.2 `fulfilled`

A Request is fulfilled only when:

1. one final Plan Version satisfies every required pre-delivery gate for its governed pathway;
2. material current authority has been revalidated;
3. that final Plan is durably delivered/made available under governed participant access;
4. the corresponding Entitlements fulfilment/consumption consequence is finalised exactly once.

A generated object, professional approval, activation flag, worker acknowledgement, notification or first participant view is not by itself the universal fulfilment boundary.

A review-gated Request may have multiple immutable generated/review Plan Versions while still `open`, but exactly one Plan Version may become the fulfilled participant deliverable.

### 6.3 `cancelled`

An authorised cancellation before fulfilment terminates the Request.

Cancellation is not:

- technical failure;
- safety invalidation;
- physical deletion;
- automatic entitlement consumption;
- automatic supersession of a prior still-valid Plan.

Stale generation/review work finishing after cancellation cannot resurrect or fulfil the Request.

The exact cancellation and commercial-remedy rules remain upstream/JIT as classified in the Delta Register.

### 6.4 `invalidated`

A material current authority ceased to permit fulfilment before success.

Examples include changed Safety authority, entitlement authority, required consent/relationship authority or a material governed dependency becoming unavailable/withdrawn.

An invalidated Request never regains authority simply because similar conditions become true later. Later legitimate work uses a new authorised basis and new Request.

### 6.5 `unfulfillable`

The Request was validly admitted, but current approved Plans capability proves that no complete valid Plan can satisfy the mandatory basis/constraints.

This is not a transient failure and unchanged retries must not be used to hide it.

Later capability/content expansion may support a new Request; it does not reopen the terminal old Request.

## 7. Generation Attempt and recovery rules

Attempt execution status and Attempt outcome remain separate.

An Attempt begins when actual execution begins; queued/scheduled work is not itself an Attempt.

One Attempt may terminate due to:

- success;
- transient technical failure;
- interruption/crash;
- cancellation;
- material authority invalidation;
- proven unfulfillable case;
- content/catalogue inability;
- deterministic invariant violation;
- another explicitly governed reason admitted in JIT.

Exact names remain JIT.

Core recovery invariant:

`recover durable business truth → inspect current Request → establish whether fulfilment already occurred → revalidate current material authority → only then decide whether another Attempt is allowed`

Worker acknowledgement is not business authority.

A crash after durable fulfilment must reconcile to the already committed success. It must not create a second Plan or consume the entitlement twice.

## 8. Fulfilment and Entitlements boundary

Request admission, entitlement authorisation/claim, Plan generation and entitlement consumption are distinct business moments.

Each logical Request binds to the specific Entitlements authority that admitted it.

Retries and failed Attempts do not create additional rights and do not spend the right merely because execution occurred.

For FP-005, the durable invariant is:

> exactly one successful participant Plan fulfilment corresponds to exactly one finalised entitlement consequence for the bound Request.

Non-fulfilment due to a generation failure preserves the participant’s Plan entitlement under current DEC-109. More detailed treatment for cancellation, material participant change, time-scoped membership expiry and customer remedies remains governed by the Delta Register.

No Plans worker may invent Commerce policy. No Commerce decision may fabricate a Plan fulfilment that did not occur.

## 9. Plan current-use lifecycle boundaries

Product Law owns the Plan lifecycle:

`pending, generated, review, approval, scheduled, active, safety-paused, completed, superseded, withdrawn`

This contract does not replace or redesign those states.

Two distinctions matter for JIT:

### 9.1 `safety_paused` versus `withdrawn`

`safety_paused` is a potentially recoverable current-use suspension while current Safety authority is re-established.

`withdrawn` means that exact Plan Version is no longer valid for current use under the governing withdrawal reason/scope, while history may remain subject to retention law.

Do not treat one as the other.

### 9.2 Resume of an exact paused Plan

The same immutable Plan Version may resume only when:

- current Safety authority permits that exact Plan;
- its material dependencies remain deliverable/currently usable as required;
- no material Plan input/constraint/dependency change requires different Plan content.

Otherwise create a new immutable successor Plan Version through the governed pathway. Never edit the paused Plan in place.

### 9.3 Supersession and withdrawal

Ordinary supersession does not automatically mean withdrawal. A withdrawn dependency cannot be used to authorise participant delivery merely because it was historically valid when the generation basis was captured.

The exact in-flight policy for ordinary superseded-but-not-withdrawn dependencies is intentionally left to JIT/governance unless a Product promise requires an upstream rule.

## 10. Professional-review boundary

Professional Care is not a second Safety gateway and is not a second Plan owner.

A practitioner may:

- record professional review/case outcomes within Professional Care;
- request governed clearance/restriction/override through Safety & Eligibility;
- author/modify Plan content only by causing a new Plan Version through Plans & Nutrition.

Professional role alone does not grant participant access; current consent, relationship, scope and expiry remain required.

Required professional review may be a pre-delivery gate for a later pathway. While that gate is unresolved:

- the Request may remain `open`;
- generated/review candidate Plans may remain pre-fulfilment;
- no participant delivery is authorised;
- reviewer reassignment does not create a new commercial Plan right;
- stale practitioner completion cannot mutate a terminal/cancelled Request;
- current professional, Safety, Request and Plan-lineage authority must be revalidated before a review outcome can result in delivery.

FP-004 may route to `professional_review_required` without implementing or selling the later practitioner service. FP-005’s once-off MVP does not need to pull practitioner workflow forward.

## 11. Plan lineage and concurrent successor work

A replacement, correction, adjustment or practitioner-derived Request that intends to advance a Plan lineage must bind to the predecessor/current lineage authority it intends to replace.

If two independently valid Requests race to advance the same predecessor:

- both may have legitimate business intent;
- both may generate immutable candidates;
- only one may successfully advance that predecessor under current lineage authority;
- the stale competitor must not silently overwrite, auto-merge onto, or supersede the newer current Plan.

The stale Request follows an explicit governed terminal/consequence path selected in JIT consistent with the existing Request states; this contract does not invent another Plan lifecycle state.

Concurrency correctness must be enforced by durable server-side authority, never by one-tab UX or LiveView presence.

## 12. Participant input edits during in-flight work

The immutable basis is never silently edited.

A participant-owned Plan input change after Request admission must have enough applicability semantics to distinguish:

- applies to the current Request;
- applies only to future Requests;
- applies to another purpose/context.

A material change explicitly applying to the current Request blocks fulfilment from the stale basis and requires a new authorised basis/Request as governed.

An unrelated or future-only edit does not automatically invalidate all in-flight work.

The commercial consequence of such pre-fulfilment change remains open in `HSP-UPD-008`; JIT may not guess whether the same unconsumed right, a new right or another commercial treatment applies.

## 13. Progress, review and adjustment model

Frequent progress logging and Plan adjustment are separate Product concepts.

Current Product Law is explicit:

- daily or weekly progress entries are permitted;
- daily/weekly logging does not immediately regenerate a Plan;
- ordinary Plan adjustments occur monthly;
- adjustment uses trends across an approved review window, not isolated fluctuations;
- one qualifying formal review requires the applicable entitlement period, minimum Plan exposure and complete check-in;
- incomplete review data does not justify an ordinary adjustment;
- “no change required” may still count as a completed review;
- an unused review may expire after its governed grace period;
- exact review timing, trend windows and adjustment thresholds remain gated;
- safety-critical new information may trigger immediate Safety reevaluation and does not wait for the ordinary monthly review.

The generation mechanism may remain technically cadence-generic later, but Product authority decides which cadence is permitted. Do not generalise monthly ordinary adjustment into weekly Product Law.

FP-005 collects lightweight progress/feedback. Recurring adjustment belongs to FP-010 and its OQ-003/OQ-011/OQ-012 gates.

## 14. Correction versus later re-personalisation

Do not collapse two fundamentally different rights.

### 14.1 Defective delivered Plan correction/replacement

If a delivered Plan is materially incorrect, unsafe, affected by a governed correction/withdrawal or otherwise requires a Product-authorised correction/safety replacement:

- preserve historical Plan evidence;
- issue a governed correction/replacement/new version;
- do not consume a new ordinary Plan entitlement merely to repair the defect, consistent with current Product Law.

### 14.2 Later preference/progress re-personalisation

If the delivered Plan was correct for its original authorised basis and the participant later wants different personalisation because goals, preferences or progress changed:

- this is later re-personalisation/adjustment;
- current Product Law requires the applicable new purchase or qualifying membership/add-on/review entitlement;
- a profile edit alone does not regenerate the Plan.

A correction is not a free later personalisation pathway, and later personalisation is not a “correction” merely because the participant wants different content.

## 15. Concurrency, idempotency and recovery invariants

JIT must preserve correctness under:

- duplicate clicks/submissions;
- multiple tabs/devices;
- simultaneous Requests;
- retry and redelivery;
- process/node crash;
- stale worker completion;
- event/review reordering;
- partial failure;
- current-authority changes mid-flight.

Required invariants:

1. equivalent duplicate execution converges on one logical business Request/outcome;
2. no duplicate Plan fulfilment for one logical Request;
3. no duplicate entitlement consumption for one fulfilment;
4. a crash after durable success reconciles rather than repeats success;
5. terminal Request states cannot be resurrected by stale technical work;
6. current Safety/Entitlements/dependency/professional authority is revalidated before final delivery where material;
7. same-lineage competing successor work cannot both become current;
8. partial/internally invalid Plan candidates never become participant deliverables;
9. LiveView/Presence/browser coordination may improve UX but never supplies business correctness;
10. queue uniqueness, PubSub, cache or provider idempotency is not a substitute for business idempotency.

The exact PostgreSQL/Ash/Oban mechanism belongs to JIT/Architectural Proof.

## 16. Privacy, retention and deletion boundary

Immutability while retained and retention authority are separate dimensions.

Historical Health/Safety/Plan evidence must not be silently mutated merely because current truth changed.

But immutability does **not** authorise indefinite identifiable retention.

Current Product/Architecture direction requires:

- full deletion permanently ends participant product access and retained financial evidence cannot recreate it;
- self-guided health records are deleted or anonymised as governed;
- formal professional records are subject to approved professional recordkeeping/retention authority;
- business lifecycle and data lifecycle remain separate;
- deletion/export/retention is orchestrated through Privacy & Consent while each Domain applies its own data contract.

Exact category-specific treatment of Plan Versions, bases/provenance, Safety records and practitioner-derived variants remains open under retention/professional-record gates and must be completed before the applicable release/JIT freeze point without weakening current deletion law.

## 17. Fail-closed rules

The system must fail closed when any material authority required for protected personalisation is absent, stale, conflicted, withdrawn, invalid or no longer provable.

In particular:

- unresolved safety-relevant evidence conflict blocks automation;
- missing safety-critical information does not become permission;
- Safety permission cannot be inferred from Plans capability;
- Plans capability failure cannot be mislabelled as Safety permission;
- hard constraints cannot be softened silently;
- withdrawn required dependency cannot be delivered;
- stale Safety/Entitlement/professional authority cannot be bypassed by cached/UI/worker state;
- incomplete/partial Plan output cannot be delivered;
- deterministic invariant violation is an exception/defect condition, not participant success;
- ambiguous durable success is reconciled from authoritative state before retry;
- privacy/deletion ambiguity cannot be resolved by retaining everything “for safety”.

Correct refusal or bounded pending state is preferable to fabricated success.

## 18. Explicit JIT proof obligations

These are proof obligations, not a new pressure-test programme and not implementation prescriptions.

### 18.1 FP-004 obligations

JIT/Architectural Proof must demonstrate, at minimum:

- positive automation admission cannot be obtained from mere absence of blockers;
- the four eligibility outcomes are reproducible from the exact applicable governed basis/version;
- materially conflicting safety evidence cannot be collapsed into unsafe automatic eligibility;
- safety-relevant correction/retraction or material new fact can re-establish current Safety authority without rewriting history;
- authoritative received/known time is not delayed by downstream async processing;
- a Safety protocol/rule change has an explicit current-case/current-Plan impact contract;
- duplicate/retried reevaluation converges without competing current Safety authority;
- stale UI/cache/session state cannot override current Safety authority;
- current privacy/consent/minimum-data boundaries are preserved.

Existing Roadmap blockers `OQ-005` and `OQ-008` remain upstream gates for FP-004. Lab validity remains future-only unless FP-004 scope explicitly includes lab evidence.

### 18.2 FP-005 obligations

JIT/Architectural Proof must demonstrate, at minimum:

- one logical Request survives duplicate submissions/retries without duplicate fulfilment;
- no partial Plan can become delivered;
- failure preserves the Plan entitlement as required by Product Law;
- crash after durable success reconciles to one Plan/one entitlement consequence;
- current Safety/Entitlement/material dependency authority is revalidated before fulfilment;
- hard constraints cannot be weakened and a genuinely unsupported mandatory case can terminate as `unfulfillable`;
- withdrawn dependencies cannot be newly delivered from stale captured provenance;
- generated/review candidate does not equal fulfilled deliverable;
- a terminal cancellation/invalidation cannot be defeated by stale technical completion;
- same-lineage competing Requests cannot both advance the same predecessor;
- material current-Request participant input edits cannot fulfil from the stale basis;
- historical Generation Input Basis and Plan Result Provenance can explain a delivered Plan without becoming competing authority;
- safety pause/resume preserves exact-Plan revalidation;
- correction/replacement remains distinct from later repersonalisation;
- business deletion does not permit retained evidence to recreate deleted product/access authority.

Before the FP-005 Phase 7C Final Feature Pack Contract can freeze commercial behaviour, the Product/Commerce issues identified as `HSP-UPD-005` and `HSP-UPD-008` must be resolved.

## 19. Intentionally unspecified

The following are deliberately deferred:

- exact clinical eligibility and risk matrices;
- exact evidence-source conflict-resolution rules by health fact type;
- exact freshness/reconfirmation periods;
- exact calculation formulas, limits, rounding and adjustment thresholds;
- exact Request/Attempt/Plan persistence representation;
- exact enums beyond upstream Product states and the compressed working Request lifecycle;
- exact transaction/locking/idempotency technique;
- exact Ash Resource/action/interface design;
- exact Oban design;
- exact cache/Redis/ETS/GenServer use;
- exact participant cancellation rights;
- exact customer refund/credit/remedy policy for open commercial deltas;
- exact ordinary-supersession behaviour for every governed dependency class;
- exact category-specific retention periods and professional recordkeeper obligations;
- exact professional-review SLA/capacity policy;
- exact operational alert/queue design.

A future JIT dossier may refine these beneath authority. It may not silently change the durable invariants in this contract or decide an upstream Product/commercial/clinical/legal gap.

## 20. Consolidation conclusion

The v0.42.0 discovery suite can be compressed without reopening architecture discovery.

No current live Product/Architecture/Domain/Roadmap contradiction was found.

The stable model is small:

`versioned health evidence`
→ `current Safety authority`
→ `positive automation admission`
→ `immutable authorised Plan basis`
→ `logical Request + repeatable Attempts`
→ `one valid final fulfilled Plan`
→ `exactly-once Entitlements consequence`
→ `immutable history + current-use revalidation`

Everything else should remain either:

- an upstream governed Product/clinical/privacy/commercial decision;
- a later JIT representation/proof decision;
- or an operating implementation detail.
