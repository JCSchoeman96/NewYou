# HEALTH_SAFETY_PLAN_PREJIT_DISCOVERY_WORKING_v0.42.0.md

- **Document status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY
- **Document version:** v0.42.0
- **Date:** 2026-09-06
- **Purpose:** Capture structured discovery decisions and unresolved questions for future Health Records, Safety & Eligibility, Plans & Nutrition, and related Professional Care planning.
- **Authority boundary:** This document does not amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Feature Packs, JIT Domain Dossiers, or implementation authority.
- **Implementation status:** NOT AUTHORISED
- **Canonical source rule:** The live `JCSchoeman96/NewYou` GitHub repository remains authoritative. This working document must yield to current upstream authority if any conflict is found.
- **Primary future planning relevance:** FP-004 (Health intake → safety → eligibility), FP-005 (Safe plan → purchased library → feedback), and later professional-care/adjustment work.
- **Governance warning:** No exact Ash Resources, schemas, migrations, tables, indexes, workers, queues, cache structures, package choices, or implementation sequence are decided here.

---

# 1. Purpose

This document captures detailed pre-JIT discovery for the health → safety → eligibility → plan pipeline.

The objective is to make future JIT Domain Dossiers and Feature Pack planning easier without prematurely designing implementation or reopening already-frozen Product Law.

The discovery must remain strict about:

- safety;
- provenance;
- reproducibility;
- lifecycle modelling;
- conflict handling;
- fail-closed behaviour;
- explicit authority boundaries;
- concurrency and retry implications;
- MVP scope versus mature-platform capability.

The mature platform model must not be weakened merely to simplify MVP delivery.

---

# 2. SemVer policy

This is a working document.

Use:

- **v0.x.0** for substantive new discovery rounds, accepted doctrines, or meaningful structural additions;
- **v0.x.y** for clarifications, corrections, wording improvements, or source-reference hygiene that do not materially change discovery conclusions;
- **v1.0.0** only after an explicit freeze/review decision if this artifact is ever promoted into an approved planning artifact.

A new version must preserve prior conclusions or explicitly record what was revised and why. Do not silently rewrite a previously accepted conclusion.

---


## 2.1 Local working-design identifiers

This working pack uses stable local cross-reference keys of the form:

`HSP-WD-###`

These identifiers are **local working-document keys only**.

They:

- are not Product Law `DEC` identifiers;
- are not Architecture `ARC` or `ARQ` identifiers;
- are not `OQ`, `CAP`, `FP`, `TB`, `VS`, `HH`, or any other governed platform identifier;
- create no new authority layer;
- exist only so future review/JIT work can refer to accepted working conclusions without depending on fragile section numbers.

If any working conclusion is later promoted through governed authority, the governing process decides how it is represented there.

## 2.2 Working normative-strength classification

Every substantive statement in this pack should be treated under one of three working strengths:

### `UPSTREAM_DERIVED`

A direct restatement or unavoidable consequence of current upstream authority.

This pack does not create that rule and cannot change it.

If a downstream pressure test appears to contradict it, stop and resolve the contradiction at the correct upstream authority level.

### `WORKING_DESIGN_ACCEPTED`

A conclusion deliberately reasoned through and accepted in this pre-JIT design exercise.

It remains non-authoritative working design evidence.

Future JIT work should explicitly adopt, refine beneath, or reopen it with evidence/contradiction analysis rather than silently drifting away from it.

This expectation is a working-process discipline, not a new authority layer.

### `OPEN_HYPOTHESIS`

A proposition still under pressure test.

It may be revised freely until accepted or rejected.

## 2.3 Accepted working-decision register

The current accepted design conclusions are registered below.

| Local key | Working conclusion | Strength |
|---|---|---|
| `HSP-WD-001` | Risk-sensitive reuse and deliberate reconfirmation | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-002` | Changes, corrections, observations, verification and contradiction remain distinct | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-003` | Safety-relevant corrections are Safety events | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-004` | Conflict-aware health authority; unresolved safety conflict fails closed | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-005` | MVP automation requires positive admission, not absence of blockers | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-006` | Safety permission and Plans capability are separate gates | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-007` | Generation failures are classified and delivery is all-or-nothing | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-008` | Generation uses immutable basis plus current-authority revalidation | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-009` | Single-active-workspace LiveView behaviour is defence-in-depth UX only | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-010` | Generation Request ≠ Generation Attempt ≠ Plan Version | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-011` | Generation Request lifecycle is `open → fulfilled | cancelled | invalidated | unfulfillable` | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-012` | Attempt execution status and Attempt outcome are separate | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-013` | Every Plan Version has an immutable minimum-necessary Generation Basis | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-014` | Plan inputs classify as Direct Plan Input / Safety-Derived Plan Constraint / Not a Plan Input | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-015` | Hard constraints and soft preferences remain distinct | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-016` | Unsatisfied hard constraint may terminate an otherwise-safe request as `unfulfillable` | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-017` | Intake is automation-grade structured evidence, not merely a form | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-018` | Temporal truth separates freshness, effective time, known time and provenance | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-019` | Intake completion is purpose/version-relative; rule changes declare active-case impact | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-020` | Health changes have impact-sensitive Safety reevaluation consequences | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-021` | Safety Adjudication has distinct purposes: Eligibility Evaluation and Safety Impact Assessment; Safety Case remains a separate stateful process | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-022` | Professional Care does not bypass the single Safety & Eligibility gateway into Plans | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-023` | Generation Request admission, entitlement authorization/claim, and entitlement consumption are distinct; each logical Request binds to specific Entitlements authority and successful fulfilment finalises the entitlement consequence exactly once | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-024` | Immutable pre-generation input/dependency basis is distinct from immutable successful Plan result provenance; each delivered Plan Version links both | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-025` | `safety_paused` and `withdrawn` are distinct Plan consequences: pause is potentially recoverable current-use suspension; withdrawal means that exact Plan Version is no longer valid for current use while history may remain | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-026` | A `safety_paused` Plan may resume as the same immutable Plan Version only when current Safety authority permits that exact Plan and no material Plan input/constraint/dependency change requires different Plan content; otherwise a new immutable Plan Version is required | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-027` | For safety-relevant evidence, authoritative known/received time is established when evidence is durably accepted into its owning authority boundary, not when an async projection, worker, cache or downstream consumer later processes it | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-028` | Safety-relevant health concepts may preserve multiple concurrent source assertions while materially conflicted; unresolved evidence must not be erased by a lossy scalar current value, and any resolved current fact remains traceable to evidence and resolution authority | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-029` | Evidence correction/retraction distinguishes “wrong when made” from genuine later participant-state change; historical decisions retain the evidence actually relied on while current evidence usability changes from the correction/retraction’s authoritative known time | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-030` | Immutability and retention are orthogonal: Health/Safety/Plan evidence is protected from silent mutation while retained, but category-specific Privacy/deletion/retention authority determines whether it continues to exist in identifiable form; retained evidence cannot reconstruct deleted product authority | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-031` | Request fulfilment requires one final Plan Version to satisfy every required pre-delivery gate and be durably delivered/made available under governed participant access, with the corresponding Entitlements consequence finalised exactly once; review-gated Requests may contain multiple immutable pre-fulfilment versions but exactly one fulfilled deliverable | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-032` | Same-lineage replacement/adjustment Requests bind to the Plan lineage/predecessor they intend to advance; fulfilment revalidates current lineage authority so only one competing Request may successfully advance the same predecessor, while stale competitors cannot silently overwrite or auto-merge onto the newer current Plan | `WORKING_DESIGN_ACCEPTED` |
| `HSP-WD-033` | Participant-owned Plan-input edits after Request admission require explicit applicability semantics (current Request versus future/other purpose); the immutable Generation Basis is never silently mutated, and a material edit explicitly applying to the current Request blocks fulfilment from the stale basis while unrelated/future-only edits do not automatically invalidate in-flight work | `WORKING_DESIGN_ACCEPTED` |

### Traceability caution

The register above intentionally classifies the **composite working conclusions** as `WORKING_DESIGN_ACCEPTED`, even where parts are already required by Product/Architecture/Domain Law.

A later traceability pass may separately mark individual clauses as `UPSTREAM_DERIVED` only after exact source mapping.

This avoids falsely promoting a broader working conclusion merely because one part of it has an upstream anchor.


# 3. Authority and ownership boundaries

Current Domain Law remains authoritative:

- **Health Records** owns progressively collected health/lifestyle facts and their provenance.
- **Safety & Eligibility** owns eligibility evaluations, restrictions, safety cases, and safety authority.
- **Plans & Nutrition** owns plan generation/outcomes and immutable delivered plan versions.
- **Professional Care** owns professional-care relationships/review records, while practitioner-authored plan changes become new plan versions through the Plans & Nutrition owner.

Core doctrine:

> health fact ≠ safety interpretation ≠ eligibility decision ≠ plan decision

No downstream plan logic may independently reinterpret conflicting raw health evidence in order to bypass Safety & Eligibility authority.

---

# 4. Mature-platform doctrine versus MVP scope

## 4.1 Mature-platform doctrine

The platform must be designed from the beginning to preserve the hard cases even when MVP automation does not support them yet.

The platform model must be able to support, over time:

- changing health facts;
- corrections;
- multiple observations over time;
- provenance and later verification;
- conflicting evidence;
- stale/time-limited evidence;
- safety re-evaluation;
- safety pauses;
- professional review;
- practitioner-authored or practitioner-modified plans;
- restrictions;
- follow-up requirements;
- immutable plan history;
- later broadening of approved automated case classes.

MVP simplification must occur by narrowing **which cases may enter automated plan generation**, not by weakening these underlying truths.

## 4.2 MVP automation doctrine

MVP automated plan generation should use a **positive automation allow-list**.

Automation is permitted only when the participant falls inside an explicitly clinically approved automated case class and all required current information, evidence, safety checks, and plan-generation preconditions pass.

The automated lane should therefore be intentionally conservative.

Examples of cases that may initially be excluded from automation include medication use, clinically complex conditions, unresolved symptoms, conflicting safety-sensitive information, or other cases not yet explicitly approved for automated handling.

This document does **not** decide the final eligibility matrix. Exact clinical inclusion/exclusion rules remain behind the existing clinical gates.

Core rule:

> absence of a known blocker is not sufficient for automation; the case must positively satisfy an approved automated pathway.

## 4.3 Professional/manual pathway boundary

The mature platform must support explicit professional/manual review and practitioner-authored or modified plans.

However, current Roadmap sequencing does not make a participant-facing practitioner service an MVP prerequisite. Current authority permits MVP cases to route to `professional_review_required` without selling or implementing the later practitioner service.

Therefore, until upstream authority is explicitly amended:

- MVP automation may be narrow;
- unsupported/complex cases must not receive an unsafe automated plan;
- those cases may receive the governed safe alternative such as `professional_review_required`, `general_wellness_only`, or `insufficient_information` as applicable;
- a full participant-facing manual plan creation/follow-up service must not be silently pulled into MVP merely as a fallback;
- mature professional/manual capability should still be considered during discovery so today's design does not block it later.

If the product decision becomes “all excluded MVP cases must receive manual professional plan creation and follow-up inside the platform,” that is a deliberate Product/Roadmap scope change and must be handled at the correct authority level.

---

# 5. Discovery decisions

## 5.1 `HSP-WD-001` — Risk-sensitive reuse and reconfirmation

**Accepted.**

Existing authoritative health information should be reused rather than needlessly duplicated.

Current usability of a health fact is separate from historical existence of that fact.

Information should conceptually be treated according to risk/currentness, including:

- stable facts;
- current low-risk facts;
- safety-sensitive current facts;
- time-sensitive evidence.

Safety-sensitive current facts must be deliberately reconfirmed at every relevant plan-generation or reassessment boundary.

Good UX should:

- show the existing answer;
- require deliberate confirmation or change;
- avoid unnecessary re-entry;
- not reduce the requirement to a weak blanket “everything is still correct” confirmation where specific safety reconfirmation is needed.

“Every relevant boundary” does not mean repeatedly asking safety questions during ordinary viewing or unrelated interactions. Exact triggering boundaries remain future JIT/clinical-policy work.

---

## 5.2 `HSP-WD-002` — Changes, corrections, observations and verification are distinct

**Accepted.**

A generic “edit health profile” operation must not collapse materially different meanings.

The discovery distinguishes at least:

### New observation
A later valid measurement or observation that does not invalidate an earlier valid observation.

### Genuine state change
The earlier information may have been correct, but the participant’s actual situation later changed.

### Correction
Earlier supplied information was wrong and is being corrected.

### Verification/provenance change
The underlying reported information may remain the same while its evidence/provenance status changes.

### Contradiction
New evidence conflicts with existing evidence and cannot safely be treated as a straightforward state change or correction without resolution.

Prior evidence/history must not be silently destroyed merely because a newer record exists.

Plans must retain enough provenance to reproduce what information and authority were actually used at generation time.

---

## 5.3 `HSP-WD-003` — Safety-relevant corrections are safety events

**Accepted.**

If corrected information could have changed an earlier eligibility or plan decision, the correction must immediately trigger re-establishment of current Safety & Eligibility authority.

A participant’s statement that an answer was “only a correction” does not reduce the safety consequence.

The existing historical plan must not be rewritten as though the corrected information had been known when that plan was generated.

Where the corrected information creates a possible current risk, the currently active personalised plan must be treated conservatively while safety is re-evaluated, including `safety_paused` behaviour where the governing rules require it.

---

## 5.4 `HSP-WD-004` — Conflict-aware health authority

**Accepted.**

The newest answer does not automatically win for safety-sensitive information.

Likewise, stronger provenance does not make a health fact permanently immutable or eternally current.

New evidence may represent:

- a genuine later change;
- a correction;
- new observation;
- verification;
- or a real unresolved contradiction.

For safety-relevant unresolved conflicts:

> fail closed and use the safer operational interpretation until the conflict is clarified and current Safety authority is re-established.

A participant-reported update must not silently remove a safety restriction merely because it is newer than previously verified contradictory evidence.

Provenance informs how evidence is handled, but provenance is not itself clinical truth.

There must not be a universal context-free ranking such as:

`laboratory > practitioner > participant`

for every type of fact.

Source authority depends on the fact type and intended use. Exact evidence-resolution rules remain future clinical/JIT work.

---


## 5.5 `HSP-WD-005` — MVP Automation Admission Rule

**Accepted.**

A participant may enter MVP automated plan generation only when every required positive condition passes.

Conceptually, automation requires all applicable conditions to be satisfied, including:

- required intake is complete and current;
- required safety-sensitive answers have been deliberately reconfirmed at the relevant boundary;
- no unresolved safety-relevant health-data conflict exists;
- no active safety restriction or case prevents automation;
- the participant belongs to an explicitly approved MVP automated case class;
- the requested goal/pathway is supported by the MVP automated engine;
- required food exclusions and other constraints can be safely satisfied by the approved plan catalogue;
- required calculation inputs are present, valid, current, and authorised for use;
- current Safety & Eligibility authority permits automated generation.

Core asymmetry:

> Automation must be positively authorised. It is not allowed merely because the platform failed to find a blocker.

A missing, conflicting, stale, unsupported, professionally gated, or otherwise unapproved condition must not be treated as implicit permission.

The participant does not carry the burden of proving why automation should stop. The platform must be able to prove why automation was permitted.

The exact clinical case classes, thresholds, and eligibility matrix remain governed by existing clinical gates and are not decided by this document.



## 5.6 `HSP-WD-006` — Safety Permission and Plan Capability Are Separate Gates

**Accepted.**

Safety & Eligibility and Plans & Nutrition answer different questions and must not collapse into one decision.

### Gate 1 — Safety / eligibility authority

Safety & Eligibility determines whether automated personalisation is currently permitted under the applicable approved eligibility protocol.

The eligibility outcome must remain one of the governed outcomes:

- `eligible_automated`;
- `general_wellness_only`;
- `professional_review_required`;
- `insufficient_information`.

`eligible_automated` means the participant's current authoritative input state positively satisfies the approved automated eligibility protocol. It must not merely mean that no blocker was detected.

Eligibility decisions should be reproducible against the exact health-input snapshot/provenance and eligibility protocol/rule version used at the time.

### Gate 2 — Plan-generation capability

Plans & Nutrition separately determines whether an approved deterministic generation pathway exists for the case that Safety has authorised.

Conceptually, after `eligible_automated`, Plans still needs to establish that:

- the requested goal/pathway is supported;
- the required calculation protocol exists and is approved;
- the required approved content, plan components, recipes, substitutions, and other dependencies are available;
- exclusions and constraints can be satisfied;
- the engine can deterministically produce one valid complete plan;
- no current plan-specific invariant blocks generation.

A participant may therefore be `eligible_automated` while the current plan engine still cannot produce an approved plan for that exact case.

That situation must not be misclassified as:

- `professional_review_required` when professional judgement is not clinically required;
- `general_wellness_only` merely because software capability is incomplete;
- `insufficient_information` when the required information is actually complete.

Core rule:

> Eligibility says whether automated personalisation is permitted. Plans separately says whether an approved automated plan can actually be produced.

If Gate 2 fails, Plans must fail closed and produce no partial or plausible-looking plan. The eligibility outcome remains truthful and unchanged unless Safety authority itself changes.

Exact failure classifications and participant/operator handling for Gate-2 failure remain to be grilled.



## 5.7 `HSP-WD-007` — Generation Failure Classification and All-or-Nothing Commit

**Accepted.**

A failed plan-generation attempt must not collapse into a generic undifferentiated “generation failed” state.

Every failed generation attempt should preserve a machine-meaningful failure classification and enough provenance to determine the correct next action.

At minimum, future planning must distinguish conceptually between:

### Temporary technical failure

Examples include process failure, transient infrastructure problems, temporary dependency failure, or another condition where the same still-authorised request may be safely retried.

### Approved-pathway capability gap

Safety permits automated personalisation, but the current Plans capability does not yet contain an approved deterministic generation pathway for the exact case.

Retrying the same unchanged request is not useful.

### Content/catalogue incompleteness

An approved generation pathway exists, but the required approved plan components, recipes, substitutions, translations, or other governed dependencies cannot produce one complete valid plan.

This is not automatically a participant problem and must not be disguised as a clinical eligibility failure.

### Upstream authority changed or became stale

During generation, a relevant authoritative condition changes or becomes invalid, such as:

- a safety-relevant health update;
- a changed eligibility/restriction;
- entitlement loss or invalidation;
- withdrawal/supersession of an applicable approved protocol;
- another current-authority change that invalidates the in-flight request.

The generation must abort and return to the appropriate upstream authority/re-evaluation path rather than commit against stale assumptions.

### Deterministic invariant failure

The generation engine reaches a state that should be impossible under the approved rules or produces an internally invalid result.

This is treated as a possible product/implementation defect or governed-rule contradiction, not as an ordinary participant failure.

Core doctrine:

> A generation failure must say what kind of failure occurred and whether the correct response is retry, upstream re-evaluation, operator/content intervention, capability expansion, or defect investigation.

### Entitlement preservation

A failed generation attempt must not consume the participant's plan entitlement merely because generation was attempted.

Entitlement consumption/fulfilment semantics must preserve the participant's right when no valid complete plan was successfully delivered, subject to the exact downstream commercial/entitlement contract.

### All-or-nothing generation

Partial plans must never become active or participant-delivered plans.

The generation boundary is conceptually:

`validate current authority and inputs`
→ `deterministically build complete candidate`
→ `validate complete candidate`
→ `atomically persist immutable plan snapshot + provenance`
→ `success`

or:

`no delivered plan`

A crash, invalid intermediate result, missing component, stale authority, or other failure must not expose or activate a partially generated plan.

Exact transaction, persistence, worker, retry, and schema mechanics remain JIT/implementation detail.



## 5.8 `HSP-WD-008` — Concurrent Generation: Immutable Basis + Current-Authority Revalidation

**Accepted.**

One logical generation must preserve both reproducibility and current-authority safety.

### Generation basis

Before deterministic generation begins, the system conceptually captures the exact authorised generation basis, including the material authoritative inputs and version identities used for the attempt.

That basis exists to answer:

> What exact approved inputs and rule/content/protocol versions caused this candidate to be produced?

Generation proceeds against that immutable basis rather than drifting as records change underneath it.

### Current-authority revalidation

An old valid generation basis does not grant permanent authority to deliver a plan.

Immediately before successful commit/activation/delivery, all material current authorities must be revalidated.

If a material authority changed in a way that invalidates the candidate, the candidate must not be activated or delivered.

Examples include:

- safety-relevant health information changed;
- eligibility/restriction authority changed;
- entitlement authority changed;
- an applicable approved protocol or governed dependency was withdrawn or invalidated;
- another material current-authority condition no longer passes.

Core doctrine:

> The immutable basis explains what was attempted; current authority decides whether it may still be committed and delivered.

### Idempotent logical generation identity

Duplicate clicks, browser retries, reconnects, multiple tabs, process retries, and equivalent repeat execution of the same logical generation request must converge on one logical outcome.

They must not:

- create multiple successful plan versions for the same logical request;
- consume multiple entitlements;
- create competing active plans merely because execution was duplicated.

A genuinely new authorised generation, regeneration, adjustment, practitioner-derived replacement, or otherwise distinct business event receives its own lineage/version rather than being treated as a retry.

### Material dependency rule

Not every unrelated participant/profile change should abort an in-flight generation.

Only a change to a material authoritative dependency of that generation, or to current authority required for delivery, should invalidate the candidate.

Exact dependency/version representation and transaction mechanics remain JIT detail.

---

## 5.9 `HSP-WD-009` — Single-Active-Workspace UX Hardening

**Accepted.**

LiveView may be used to reduce accidental duplicate work by detecting or coordinating concurrent tabs/windows for selected sensitive workflows.

Possible future UX behaviour includes:

- warn when the same participant/workflow is already active in another tab;
- make a secondary tab read-only;
- offer an explicit “take over here” action;
- coordinate same-browser tabs using client-side mechanisms;
- use Phoenix Presence or equivalent server-side observation to detect concurrent connected views where useful.

This is **defence in depth only**.

It must never be a correctness dependency because:

- users may open another browser or device;
- connections may drop or reconnect;
- browser-local coordination may fail or be unavailable;
- presence is observation, not durable business authority;
- stale/disconnected tabs may not disappear immediately;
- network partitions and process restarts must not weaken correctness.

Therefore:

> one-tab UX may reduce accidental duplication, but authoritative actions must remain safe under multiple tabs, devices, retries, reconnects, and simultaneous requests.

Do not hold a long-lived business lock merely because a browser page is open.

If future workflow exclusivity is truly required for business correctness, it must use the owning Domain's durable/transactional authority and explicit lifecycle rather than LiveView process state or Presence.



## 5.10 `HSP-WD-010` — Generation Request ≠ Generation Attempt ≠ Plan Version

**Accepted.**

Generation Request, Generation Attempt, and Plan Version are independent lifecycle dimensions and must not be collapsed into one state machine.

### Generation Request

The Generation Request represents the durable business intent to produce one authorised personalised plan from a defined generation basis.

It owns the logical idempotency identity for that business request.

Repeated browser submissions, reconnects, duplicate clicks, worker retries, and equivalent repeated execution must resolve to the same logical request rather than creating new business intent.

A genuinely new authorised generation, regeneration, adjustment, practitioner-derived replacement, or other distinct business event requires a new logical request/lineage as governed by the applicable domain rules.

### Generation Attempt

A Generation Attempt represents one execution attempt against the logical Generation Request.

One request may have multiple attempts.

Attempts may fail for technical, capability, content, stale-authority, invariant, or other classified reasons.

Failed attempts:

- do not create Plan versions;
- do not consume additional entitlement merely by executing;
- remain available as operational/audit evidence as appropriate;
- do not alter the governed Plan lifecycle.

Retries belong to attempt history, not to the Plan lifecycle.

### Plan Version

#### Superseding clarification from `HSP-WD-031`

The original wording below predates `HSP-PT-017` / `HSP-WD-031` and is preserved as accepted-history provenance rather than current interpretation.

Current interpretation is:

- a review-gated Request may create multiple immutable **pre-fulfilment** Plan Versions/candidates;
- those versions do not themselves fulfil the Request or consume the Plan fulfilment right;
- exactly one final Plan Version may become the fulfilled participant deliverable for that Request.

Therefore the old statements:

> “Only successful fulfilment ... may create the durable immutable Plan Version”

and

> “A successfully fulfilled logical request must produce at most one successful Plan Version”

are superseded **only to the extent that they prohibit immutable pre-fulfilment versions**.

The core `Request ≠ Attempt ≠ Plan Version` separation remains accepted.

##### Preserved original wording

Only successful fulfilment of the logical Generation Request may create the durable immutable Plan Version.

A successfully fulfilled logical request must produce at most one successful Plan Version.

The resulting Plan Version then follows the separately governed Plan lifecycle and remains immutable/reproducible according to current Product Law.

### Material invalidation ends the request

If a material safety, eligibility, entitlement, protocol, or other delivery authority invalidates the logical Generation Request before successful fulfilment, that request must not later be resurrected.

If the participant later becomes eligible/authorised again:

`new current authoritative basis`
→ `new eligibility / authority evaluation as applicable`
→ `new authorised generation basis`
→ `new logical Generation Request`

The old invalidated request remains historical evidence.

Core rule:

> A generation basis that has lost material delivery authority does not regain business authority merely because similar conditions become true again later.

### Cancellation remains distinct

Participant/operator cancellation, where allowed, is distinct from:

- authority invalidation;
- technical failure;
- capability failure;
- content/catalogue failure;
- deterministic invariant failure.

Cancellation must preserve an explicit reason/evidence trail and must not be silently treated as a technical failure.

Exact cancellation rights and consequences remain future product/JIT work.



## 5.11 `HSP-WD-011` — Minimal Generation Request Lifecycle

**Accepted.**

The Generation Request lifecycle should remain deliberately small and represent durable business fulfilment status rather than worker/queue execution state.

Candidate lifecycle:

`open`
→ `fulfilled` | `cancelled` | `invalidated` | `unfulfillable`

### Superseding fulfilment clarification — `HSP-WD-031`

`HSP-WD-031`, accepted at v0.37.0 after `HSP-PT-017`, supersedes only the earlier `HSP-WD-011` shorthand that defined `fulfilled` as creation of exactly one valid immutable Plan Version.

For current interpretation:

> `fulfilled` means one final Plan Version has passed every required pre-delivery gate for the governed pathway and has been durably delivered/made available under governed participant access, with the corresponding Entitlements consequence finalised exactly once.

A review-gated Request may therefore contain multiple immutable pre-fulfilment Plan Versions while the Request remains `open`.

The minimal Request state set itself remains unchanged.

### `open`

The logical business request exists and has not yet reached a terminal outcome.

An `open` request may have:

- no execution attempt yet;
- one current attempt;
- multiple historical failed attempts;
- temporary retry delay;
- an operational condition requiring intervention.

Queue state, worker state, retry scheduling, and operator attention do not by themselves require new Generation Request lifecycle states.

### `fulfilled` — terminal

Exactly one valid immutable Plan Version has been successfully created for the logical request.

A fulfilled request may not create another successful Plan Version later.

### `cancelled` — terminal

The request was deliberately cancelled, by an actor/process authorised to cancel it, before successful fulfilment.

Cancellation remains distinct from technical failure and authority invalidation.

Exact cancellation rights and UX remain future work.

### `invalidated` — terminal

A material upstream authority ceased to permit fulfilment before success.

Examples may include changed Safety authority, eligibility, entitlement, or another material governed dependency.

An invalidated request must never reopen.

### `unfulfillable` — terminal

The request was validly authorised, but the current approved Plans capability proves that one valid complete plan cannot be produced for that exact generation basis.

This is distinct from:

- a transient technical failure;
- incomplete health information;
- a clinical professional-review decision;
- participant cancellation;
- changed Safety authority.

Retrying unchanged execution must not be used to hide a proven unfulfillable business request.

If later content, protocol, or capability expansion makes a similar case supportable, the platform must re-establish current authority and create a new logical Generation Request rather than resurrecting the old one.

### Terminal-state doctrine

All terminal Generation Request outcomes are irreversible:

- `fulfilled`;
- `cancelled`;
- `invalidated`;
- `unfulfillable`.

A terminal request must never transition back to `open`.

Any later legitimate work creates a new request, linked to prior lineage where appropriate.

### Execution-state separation

States such as:

- queued;
- running;
- retrying;
- retry-exhausted;
- worker-failed;
- awaiting-worker;
- operator-attention

must not be added to the durable Generation Request lifecycle merely to represent execution machinery.

Those belong to Generation Attempt history and/or an independent operational condition where needed.



## 5.12 `HSP-WD-012` — Generation Attempt Execution Status and Outcome Are Separate

**Accepted.**

Generation Attempt execution state and Generation Attempt outcome are separate dimensions.

### Execution status

An Attempt exists only once actual execution has started.

The durable execution status should remain minimal:

`in_progress`
→ terminal

Being queued or scheduled for future execution does not itself mean an Attempt has begun.

A retry creates a new Attempt identity. A prior terminated Attempt must never be reopened or reused as though execution simply continued.

### Attempt outcome

When an Attempt terminates, it must retain an explicit classified outcome explaining why execution ended.

Future JIT planning should distinguish at least the conceptual outcomes required to represent:

- successful durable plan commit;
- transient technical failure;
- interrupted/crashed execution;
- cancellation while execution was active;
- material authority invalidation;
- request proven unfulfillable by current approved capability;
- content/catalogue inability to produce one valid complete plan;
- deterministic invariant violation;
- other explicitly governed terminal execution outcomes if evidence requires them.

Exact enum names and persistence mechanics remain downstream JIT/implementation detail.

Core rule:

> Attempt status says whether execution is still happening. Attempt outcome says why execution ended.

### Recovery and reconciliation

An orphaned or apparently `in_progress` Attempt after node/process failure must be recoverable and reconcilable.

Recovery must determine durable business truth before deciding whether another Attempt may begin.

Conceptually:

`recover prior attempt`
→ `determine whether durable fulfilment already occurred`
→ `inspect current Generation Request state`
→ `revalidate current material authority`
→ only then decide whether a new Attempt may be created.

A crashed process must not cause the platform to forget that an Attempt existed.

### Retry authority

A retry must not blindly replay old assumptions.

Before a new Attempt begins:

- the Generation Request must still be `open`;
- current Safety/eligibility authority must still permit generation;
- entitlement/current business authority must still permit fulfilment;
- no durable successful fulfilment may already exist;
- other material generation authorities must still pass.

### Crash after durable success

If the Plan Version was durably committed but the process/worker crashed before recording or emitting a success acknowledgement, recovery must reconcile to the already committed success.

It must not create a second plan, a second successful fulfilment, or consume entitlement again.

Core doctrine:

> Worker acknowledgement is not business authority. Durable committed business state is authoritative.



## 5.13 `HSP-WD-013` — Immutable Generation Basis and Minimum-Necessary Cross-Domain Data

**Accepted.**

Every successfully generated Plan Version must be reproducible from an immutable Generation Basis that identifies the exact material authoritative inputs, decisions, and governed protocol/content versions used to generate it.

The Generation Basis must not rely on mutable notions such as “the participant's current profile” for historical reproduction.

### Material authoritative inputs

The basis should conceptually identify only the material inputs and authorities actually required for generation, which may include:

- participant identity;
- exact entitlement/product authority;
- exact material health inputs legitimately required by Plans;
- exact authoritative Safety & Eligibility evaluation/result;
- exact applicable eligibility protocol/rule version;
- exact current restrictions, clearances, or overrides materially relied upon;
- exact selected eligible temperament profile/version where relevant to approved presentation behaviour;
- exact supported goal/pathway;
- exact participant selections relevant to generation;
- exact calculation protocol/version;
- exact deterministic plan-generation ruleset/version;
- exact approved content/recipe/substitution/equivalence versions actually selected;
- exact language/presentation version where materially relevant.

Exact persistence design remains downstream JIT work.

### No mutable-current-state historical dependency

A historical Plan Version must not require re-reading mutable “current” records in order to explain or reproduce what happened.

Changes after generation do not rewrite the historical Generation Basis.

A later generation using changed inputs creates a new Generation Basis and a new Plan Version.

### No indiscriminate mega-snapshot

The Generation Basis must not become a duplicate Health Records, Safety & Eligibility, or participant-profile database.

Do not copy all participant data merely because it is technically accessible.

Core rule:

> Freeze the minimum material evidence required for reproducibility without creating competing authority.

Some material values may need durable snapshot values when their owning record is mutable by design.

Other material authorities may be represented through immutable version identities/references.

Exact choices belong to future JIT design.

### Domain ownership remains intact

The Generation Basis is evidence of what was used. It does not become a new owner of the underlying business truth.

In particular:

- Health Records remains authority for health/lifestyle facts and provenance;
- Safety & Eligibility remains authority for eligibility, restrictions, safety cases, and safety decisions;
- Plans & Nutrition remains authority for plan generation and Plan Versions.

Plans must not independently reconstruct clinical eligibility from raw health facts already adjudicated by Safety & Eligibility.

### Minimum-necessary sensitive-data transfer

Sensitive health data should cross into Plans only when Plans has a legitimate and explicit generation need for that specific information.

Where Safety & Eligibility can authoritatively express the decision Plans needs, Plans should consume the decision rather than copying the detailed underlying clinical facts.

Example principle:

If medication information affected Safety's eligibility decision but Plans does not need the medication identity/dose to perform an approved plan calculation, Plans should not copy that medication detail merely for convenience.

This reduces:

- competing authority;
- privacy exposure;
- accidental clinical reinterpretation;
- unnecessary coupling between Domains.

Core doctrine:

> Plans receives the minimum authoritative information required to generate the plan, not the participant's entire health record.



## 5.14 `HSP-WD-014` — Three-Way Classification of Plan-Relevant Inputs

**Accepted.**

Every candidate input to plan generation should eventually be classified into one of three conceptual categories.

### Direct Plan Input

Plans & Nutrition legitimately consumes the authoritative value because that value directly affects deterministic plan generation.

Examples may include:

- goal/pathway;
- approved calculation inputs;
- meal structure;
- participant selections relevant to composition;
- non-clinical food preferences;
- approved presentation inputs;
- other values the generation algorithm genuinely requires.

The owning Domain remains authoritative for the underlying value.

### Safety-Derived Plan Constraint

The underlying health/clinical facts require interpretation by Safety & Eligibility before Plans may act.

Plans must consume the authoritative constraint/instruction rather than independently reconstructing clinical meaning from raw health evidence.

Conceptually:

`Health Records fact/evidence`
→ `Safety & Eligibility interpretation`
→ `authorised plan constraint`
→ `Plans applies constraint deterministically`

Safety & Eligibility owns why the constraint exists.

Plans & Nutrition owns correct execution of the constraint during plan generation.

Examples may include clinically governed exclusions, restricted pathways, bounded behaviour, or other approved safety-derived instructions.

Exact constraint vocabulary and clinical mapping remain future JIT/clinical-gate work.

### Not a Plan Input

Information remains upstream when Plans does not need it to generate, explain, reproduce, or govern the Plan Version.

The mere existence of a health fact does not justify copying it into Plans.

### No generic pass-through Domain

No Domain should become a generic relay simply because data crosses a boundary.

The owning Domain must expose the correct authoritative fact, decision, or constraint.

### Safety is not a universal router

Not every participant preference or plan choice should flow through Safety & Eligibility.

Non-clinical preferences and ordinary plan-composition inputs should remain with their legitimate owning source and flow directly to Plans where appropriate.

Core doctrine:

> Plans consumes direct plan inputs where it legitimately needs the value, safety-derived constraints where upstream clinical interpretation is required, and nothing else.

This classification exists to prevent:

- duplicate clinical logic inside Plans;
- unnecessary sensitive-data propagation;
- accidental shared ownership;
- Safety & Eligibility becoming a generic data-routing Domain;
- participant preferences being misrepresented as medical restrictions.



## 5.15 `HSP-WD-015` — Hard Constraints and Soft Preferences

**Accepted.**

Plan-generation constraints must preserve both their meaning and their strength.

A flat durable list such as `excluded_foods` is insufficient because the same excluded item may represent materially different business and safety truths.

Examples include:

- medical allergy;
- intolerance;
- religious exclusion;
- ethical exclusion;
- dislike;
- ordinary preference.

These classifications must remain distinct even where the immediate generation behaviour is superficially similar.

### Hard constraints

A hard constraint is mandatory for generation.

A valid Plan Version must satisfy every applicable hard constraint.

If the approved generation pathway cannot satisfy one, no valid plan may be produced.

Examples may include:

- Safety-derived allergy exclusions;
- clinically governed restrictions;
- participant-declared mandatory religious exclusions;
- other upstream-authorised non-negotiable constraints.

Exact classification rules remain future Product/JIT/clinical work.

### Soft preferences

A soft preference should influence optimisation or selection where reasonably possible but does not necessarily invalidate an otherwise valid plan.

Examples may include:

- ordinary food dislikes;
- preferred proteins;
- preferred preparation style;
- preferred variety/repetition;
- other non-clinical preferences.

Exact product behaviour when a soft preference cannot be satisfied remains future work.

### Constraint strength comes from authority, not Plans

Plans & Nutrition must not independently decide whether an upstream fact is a hard or soft constraint.

The owning source/authority determines the classification and, where clinical interpretation is required, Safety & Eligibility determines the governed plan constraint.

Plans applies the resulting instruction deterministically.

### No convenience override of Safety-derived hard constraints

A participant may be able to change ordinary preferences through the appropriate participant workflow.

A participant must not be able to bypass a Safety-derived hard constraint from within Plan generation merely for convenience.

Changing/removing such a constraint must go through the owning Health Records / Safety & Eligibility workflow and must re-establish current authority before generation proceeds.

Core rule:

> Plans may apply upstream safety authority but may never weaken it.

### Traceability

Every material hard constraint used by Plans must remain traceable to its authoritative classification/provenance.

The Plan Version does not need to duplicate all underlying clinical detail, but it must retain enough immutable evidence to explain which mandatory constraints governed generation and from which authoritative decision/version they came.



## 5.16 `HSP-WD-016` — Unsatisfied Hard Constraints and `unfulfillable`

**Accepted.**

A hard constraint that cannot be satisfied by the current approved Plans capability means no valid Plan Version may be produced.

Where Safety & Eligibility authority remains valid but Plans cannot satisfy one or more mandatory constraints, the Generation Request should terminate as:

`unfulfillable`

This is a Plans capability truth, not a clinical eligibility truth.

### Safety outcome must remain truthful

Plans must not convert a capability/content/catalogue gap into:

- `professional_review_required`;
- `general_wellness_only`;
- `insufficient_information`.

Those remain governed Safety & Eligibility outcomes and may only be issued for their legitimate reasons.

Core boundary:

> Safety complexity produces a Safety outcome. Plan capability deficiency produces a Plans outcome.

### Professional review is not a generic repair path

Professional review must not be invoked merely because:

- the approved catalogue lacks a suitable recipe;
- a substitution is missing;
- an approved deterministic pathway is not implemented;
- another Plans/content capability is incomplete.

Professional review is appropriate only where current Product/Safety authority actually requires professional judgement.

### No silent pathway switching

If the requested pathway cannot be fulfilled but another approved pathway might work, Plans must not silently switch the participant to that alternative unless an explicit governed rule authorises that substitution.

Otherwise:

`current request unfulfillable`
→ `participant/operator informed of the legitimate next option`
→ `new choice/authority as required`
→ `new Generation Request`

The old request remains terminal historical evidence.

### Internal precision, participant-safe explanation

The platform should preserve a precise machine-meaningful internal reason for `unfulfillable`.

Participant-facing wording should remain calm and useful and must not expose unnecessary engineering detail.

### Capability-expansion evidence

Repeated `unfulfillable` cases may be analysed as evidence for future:

- catalogue expansion;
- new approved substitutions;
- new deterministic pathways;
- new content families;
- broader automation support.

Such evidence may justify future expansion but must never weaken the current hard constraint or retroactively change the old request.



## 5.17 `HSP-WD-017` — Automation-Grade Information Capture

**Accepted.**

Health intake used for automated safety and plan decisions must be structured enough to produce deterministic meaning.

The participant-facing UI is a capture surface. Health Records remains the business authority.

### Structured authoritative inputs

Automation-critical information must use explicit structured inputs.

Free text may supplement structured information, provide participant context, or support later professional review, but free text must not silently satisfy a structured safety requirement or be interpreted as an asserted negative.

If automation-critical structured information remains unresolved, automation must fail closed.

### Every material datum needs a legitimate purpose

Every material question or datum collected should have an explicit justified purpose, such as:

- safety / eligibility;
- approved plan calculation;
- plan composition;
- professional review;
- progress / reassessment;
- regulatory / operational requirement;
- another explicitly governed purpose.

Do not collect health data merely because similar products normally collect it.

If a material datum has no legitimate purpose, its collection should be challenged.

### Conditional UI does not define business truth

Showing or hiding a field must not silently create, erase, or reinterpret health truth.

Conditional branches must have explicit semantic consequences.

Example:

`medication = yes`
→ collect relevant medication detail.

If later changed to:

`medication = no`

the system must explicitly represent the change in current medication state rather than merely hiding the old medication-detail controls.

### Dependent-answer applicability

When a parent answer changes so that previous dependent answers no longer apply:

- prior answers remain historical evidence;
- they must not remain silently active as current applicable facts;
- their applicability/currentness must change explicitly according to the owning Domain's rules.

History is preserved; current applicability is not inferred from UI visibility.

### Missing-state semantics remain distinct

Where allowed by Product Law and clinical rules, values such as:

- `no`;
- `unknown`;
- `not_tested`;
- `prefer_not_to_answer`;
- legitimately governed `not_applicable`

must remain semantically distinct.

They must not collapse into a generic blank/null/false meaning.

Safety-critical questions must require explicit semantic answers rather than treating absence or an unchecked control as `no`.

### Partial intake and save/resume

Participants may durably save and resume partial intake.

Partial intake must not be treated as a completed current eligibility basis.

Unanswered required items remain unresolved and must never be inferred as negative answers.

### Intake completion and reconfirmation evidence

Completion/reconfirmation should preserve enough evidence to determine:

- which questionnaire/intake version was used;
- which required questions existed at that version;
- which answers were newly supplied;
- which prior answers were deliberately reconfirmed;
- which answers remained unresolved;
- when the participant completed/reconfirmed the intake;
- the relevant purpose/context of that completion.

Exact persistence structures remain future JIT work.

Core doctrine:

> The platform must know not only what health information it holds, but what was explicitly answered, reconfirmed, unresolved, applicable, and current at the exact safety/plan boundary.



## 5.18 `HSP-WD-018` — Temporal Truth, Freshness, Effective Time, and Reconfirmation

**Accepted.**

Health information must use fact-specific temporal semantics rather than one universal freshness/expiry rule.

### Stable facts

Stable facts may be reused without needless recollection.

Where a derived value changes with time, the stable source fact should remain authoritative and the time-dependent value should be derived for the relevant decision boundary.

Example principle:

`date_of_birth`
remains stable, while
`age_at_generation`
is derived for the relevant generation/evaluation date.

### Current-state facts

Current-state facts may change at any time.

Safety-sensitive current-state facts require deliberate reconfirmation at relevant safety/plan boundaries even when supplied recently.

Recent entry may support better UX and prefill, but it does not replace explicit reconfirmation where the fact is safety-critical.

### Historical facts/events

Historical facts remain part of history and are not deleted or made irrelevant merely because they are old.

Their current significance is determined by the applicable approved rule/protocol.

### Measurements and observations

Measurements/observations retain their own observation/effective time and historical sequence.

A later measurement does not overwrite an earlier valid observation.

Where a measurement has a clinically governed validity window, that validity must come from approved clinical policy rather than an arbitrary software default.

### Effective time versus recorded/known time

Where materially relevant, the platform should preserve separately:

- when the fact/event is said to have become true (`effective time`);
- when NewYou recorded or became aware of it (`recorded/known time`).

These are different truths.

Late-arriving information may therefore describe a fact that was already true before the platform learned about it.

### Late-arriving information and historical plans

Late-arriving information must never rewrite the historical Generation Basis of an already generated Plan Version.

The platform must preserve:

- what may actually have been true about the participant;
- what the platform actually knew and was authorised to use when it acted.

Late-arriving safety-relevant information may nevertheless trigger immediate current Safety re-evaluation and governed consequences such as safety pause or review.

### Reconfirmation does not upgrade provenance

Reconfirmation improves evidence of currentness but does not change the original provenance/verification class.

Example:

participant-reported information remains participant-reported merely because the participant later reconfirms it.

Freshness/currentness and provenance/verification strength are independent dimensions.

### Core temporal doctrine

1. Health information uses fact-specific temporal semantics.
2. Stable facts may be reused without needless recollection.
3. Safety-sensitive current-state facts require deliberate reconfirmation at relevant safety/plan boundaries.
4. Historical facts remain historical and are interpreted under current approved rules.
5. Measurements/observations retain observation time and history.
6. Clinically meaningful validity windows come from approved clinical policy, not arbitrary software defaults.
7. Effective time and recorded/known time remain distinct where material.
8. Late-arriving information never rewrites an already historical Generation Basis.
9. Late-arriving safety-relevant information may trigger immediate current Safety re-evaluation.
10. Reconfirmation does not change provenance/verification class.
11. Safety and Plans must reason from the appropriate temporal context without pretending the platform knew information before it actually received it.



## 5.19 `HSP-WD-019` — Version-Relative Intake Completion and Rule-Change Impact

**Accepted.**

Health-intake completion is purpose- and version-relative. It is not a permanent lifetime state.

### Intake completion is version-relative

A participant who completed an earlier intake version remains historically complete for that version and purpose.

That historical completion must not be rewritten or erased merely because a newer questionnaire exists.

However, current automation readiness must satisfy the current applicable intake requirements.

### Delta reconfirmation

A new questionnaire version must not automatically force full re-entry of all prior information.

Where prior authoritative answers remain semantically valid and current enough for the new version, they should be reused according to the normal reconfirmation rules.

Only the material delta should be requested where possible.

Examples include:

- newly required safety questions;
- questions whose meaning changed materially;
- newly required evidence/reconfirmation;
- other current-version requirements not satisfied by the participant's prior completion.

### New safety-critical requirements

If a newer approved intake introduces a mandatory safety-critical question or requirement that the participant has never satisfied, current automated generation must not proceed until that requirement is satisfied.

The old completion remains historically valid, but current automation readiness is incomplete.

### Health evidence and interpretation rules are separately versioned

Health evidence/facts and the clinical/safety protocols that interpret those facts are independent versioned concerns.

The same health basis may therefore produce different current eligibility results under different approved protocol versions.

Historical decisions remain reproducible under the exact protocol version that produced them.

Current Safety authority follows the current applicable approved protocol.

### Rule publication must define impact scope

Every materially safety-relevant rule/protocol change must explicitly define its operational effect on already active participants/plans.

At minimum, future governance must distinguish whether the change is:

- prospective only;
- requires reassessment at the next governed boundary;
- requires immediate current reassessment.

Implementation must not infer or invent this impact policy.

### Supersession versus safety withdrawal

Supersession and safety withdrawal are materially different governance events.

**Supersession** means a newer approved version replaces the old one for new/current decisions while preserving historical use as valid evidence.

**Safety withdrawal** means the old rule/protocol is no longer considered safe for applicable continued use and may require active reassessment or other governed consequences.

A new version must not automatically be assumed to imply either behaviour without explicit authority.

### Core doctrine

1. Intake completion is purpose- and version-relative.
2. New questionnaire versions preserve old completion history.
3. Current automation readiness must satisfy current applicable requirements.
4. Existing authoritative answers are reused where still semantically valid.
5. Only material delta should be recollected/reconfirmed where possible.
6. New mandatory safety-critical requirements must be satisfied before automation continues.
7. Health evidence and interpretation protocols are versioned separately.
8. Current Safety authority uses the current applicable approved protocol.
9. Historical eligibility decisions remain reproducible under their original protocol version.
10. Material safety-rule publication must define prospective, next-boundary, or immediate impact on existing active cases.
11. Implementation must never invent that migration/reassessment policy.
12. Supersession and safety withdrawal remain distinct governance events.



## 5.20 `HSP-WD-020` — Impact-Sensitive Safety Re-evaluation

**Accepted.**

Health changes must have impact-sensitive Safety consequences rather than one universal reaction.

### Three conceptual consequence classes

A committed health change may, under the current approved Safety protocol, be classified conceptually as:

1. **No immediate Safety impact**
   - no immediate Safety reevaluation is required;
   - the change may still affect future plan composition or another downstream concern.

2. **Re-evaluation required before the next personalised action**
   - current authority must be re-established before a new generation, adjustment, or other governed personalised decision;
   - the existing active plan does not automatically pause unless the governing impact rule requires it.

3. **Immediate Safety re-evaluation**
   - the change potentially undermines current safety authority;
   - current Safety authority must be re-established immediately;
   - governed consequences such as `safety_paused`, restriction, clarification, or professional review may apply according to current Product/clinical policy.

The exact mapping of facts/changes into these classes is clinical/Safety policy and must not be invented by implementation.

### Domain responsibility

Health Records owns the fact that health information changed.

Health Records must not decide the clinical consequence of that change.

Safety & Eligibility owns interpretation of the change under the current approved protocol.

Plans & Nutrition obeys the resulting Safety authority and must not independently infer clinical significance from raw Health Records changes.

Core flow:

`Health Records commits changed truth`
→ `Safety & Eligibility evaluates impact`
→ `current Safety authority updated`
→ `Plans obeys current Safety authority`

### Durable/reconcilable consequence

Relevant committed health changes must lead to Safety consideration through a durable or reconcilable mechanism.

Realtime delivery mechanisms may improve responsiveness, but realtime notification alone must never be treated as the durable business guarantee.

Core rule:

> Durable health truth first; guaranteed/reconcilable Safety consequence second.

### Re-evaluation gap

Once a material change is known to require Safety re-evaluation, the old eligibility decision must not authorise new personalised actions while reevaluation is outstanding.

Examples of new personalised actions that should be blocked include:

- new plan generation;
- plan adjustment;
- other governed new personalised decisions that depend on current Safety authority.

Whether an already active plan may continue to be used during the reevaluation interval is a separate governed impact decision.

### Immutable Safety evaluation basis

Every Safety evaluation must identify the exact material health/evidence basis it evaluated.

If a material input changes while Safety is evaluating an older basis, the older evaluation must not silently become current Safety authority for the newer basis.

Conceptually:

`capture Safety evaluation basis`
→ `evaluate deterministically/professionally as governed`
→ `revalidate current material basis/authority`
→ `commit current Safety decision only if still valid`

Historical stale evaluations may remain evidence of what was evaluated, but they cannot masquerade as current authority.

### Core doctrine

1. Health changes have impact-sensitive Safety consequences.
2. Some changes have no immediate Safety impact.
3. Some require reevaluation before the next personalised action.
4. Some require immediate reevaluation and may trigger governed active-plan consequences.
5. Clinical consequence mapping belongs to Safety/clinical policy.
6. Health Records records changed truth, not clinical consequence.
7. Plans obeys Safety authority rather than raw health changes.
8. Relevant committed health changes must reach Safety through durable/reconcilable handling.
9. Old eligibility cannot authorise new personalised actions once required reevaluation is outstanding.
10. Active-plan continuation during reevaluation is governed separately.
11. Safety evaluations identify an immutable evaluation basis.
12. A stale evaluation cannot become current authority for a newer material basis.



## 5.21 `HSP-WD-021` — Safety Adjudication ≠ Safety Case

**Accepted; refined at v0.23.0 after `HSP-PT-004`.**

Safety & Eligibility performs multiple adjudication purposes. Those adjudications must not be collapsed into the stateful Safety Case lifecycle.

### Broader concept: Safety Adjudication

A Safety Adjudication is an immutable decision over:

- an exact material health/evidence basis;
- an exact applicable Safety protocol/rule version;
- an explicit adjudication purpose/context.

At least two conceptually distinct adjudication purposes are now accepted.

### Eligibility Evaluation

An Eligibility Evaluation answers:

> Is this participant currently permitted to enter/proceed through the relevant personalised pathway under this exact basis and protocol?

It produces one of the governed Product-Law eligibility outcomes:

- `eligible_automated`;
- `general_wellness_only`;
- `professional_review_required`;
- `insufficient_information`.

A later Eligibility Evaluation creates a new immutable adjudication rather than editing the previous result.

### Safety Impact Assessment

A Safety Impact Assessment answers:

> Given this material change and the affected active Plan/current context, what current Safety consequence is required?

It is conceptually distinct from eligibility because its purpose is not merely to decide entry into a pathway. It may determine consequences for an already-active Plan or current personalisation authority.

The exact machine outcome vocabulary is **not frozen in this working pack**.

Potential governed consequences may include, depending on approved upstream policy:

- no current-plan consequence;
- block new personalised actions pending reevaluation;
- restriction/clearance consequence;
- participant clarification or professional review;
- `safety_paused`;
- another explicitly governed active-plan consequence.

### Conceptual split does not require implementation duplication

This distinction does **not** require:

- two Ash Resources;
- two PostgreSQL tables;
- two services;
- a new Domain.

Future JIT may prove that Eligibility Evaluations and Safety Impact Assessments share one generalized Safety-adjudication Resource/representation with an explicit purpose/context.

The working invariant is:

> Do not assume eligibility adjudication and active-plan impact adjudication have the same contract merely because Safety & Eligibility owns both.

### Current Safety authority

“Current Safety authority” is the currently valid operational authority established from applicable adjudications, professional authority/overrides where governed, and current material basis.

It must not be implemented conceptually as mutation of historical adjudications.

Historical adjudications remain immutable evidence of what was decided from their exact basis/protocol/context.

### Safety Case

A Safety Case remains a separate stateful process used only when an actual ongoing governed safety matter requires tracked resolution.

An Eligibility Evaluation or Safety Impact Assessment may:

- create a Safety Case;
- reference an existing Safety Case;
- advance/affect a Safety Case through governed rules;

but the adjudication itself is not the Case.

Safety Case must not become a generic workflow/task container.

### Stale adjudication evidence

A completed adjudication that becomes stale before it can establish current authority may remain historical evidence.

It must not be represented as having current authority for a newer material basis.

### Professional review and override

Professional review, clearance, restriction, or override does not rewrite the original automated adjudication.

The automated result remains historical evidence.

Practitioner-derived authority is represented through its own governed, scoped and auditable authority and then consumed through the Safety & Eligibility gateway.

### Core doctrine

1. Safety Adjudication is broader than Eligibility Evaluation.
2. Eligibility Evaluation and Safety Impact Assessment are distinct adjudication purposes.
3. Eligibility Evaluation produces the four locked Product-Law eligibility outcomes.
4. Safety Impact Assessment governs consequences of material changes affecting current/active-plan Safety context.
5. Exact Safety Impact outcome vocabulary remains future governed/JIT detail.
6. Both adjudication purposes may share implementation representation if future JIT proves that design.
7. Historical adjudications are immutable.
8. Current Safety authority is separate from historical adjudication existence.
9. Safety Case remains a distinct stateful safety-resolution process.
10. Professional authority does not rewrite automated adjudication history.


## 5.22 `HSP-WD-022` — Professional Review Uses a Single Safety Gateway

**Accepted.**

Professional Care must not become a second direct safety gateway into Plans & Nutrition.

Practitioner outcomes must flow through the governed Safety & Eligibility authority boundary before they permit, restrict, or otherwise alter personalised planning.

### Single Safety gateway

Conceptual flow:

`Professional Care records structured practitioner outcome`
→ `Safety & Eligibility consumes governed professional authority`
→ `current Safety authority / restrictions / clearance established`
→ `Plans & Nutrition consumes current Safety authority`

Plans must not accept independent direct “approved” commands from Professional Care that bypass Safety & Eligibility ownership.

Core rule:

> Plans has one safety-authority interface: Safety & Eligibility.

### Automated evaluations remain historical truth

A professional outcome does not rewrite the original automated Safety Evaluation.

For example:

`automated evaluation = professional_review_required`

may remain historically true even when later professional review establishes current authority for personalised planning.

Historical automated adjudication and later professional authority are separate truths.

### Structured practitioner outcome

Professional review outcomes must be structured, attributable, justified, and auditable.

Future planning should preserve enough evidence to determine:

- practitioner identity/authority;
- review context;
- relevant Safety Case where applicable;
- material evidence reviewed;
- structured outcome;
- restrictions;
- justification;
- issue time;
- scope;
- expiry/time-bound conditions where applicable;
- follow-up requirements;
- applicable pathway/product/plan context.

Exact data structures remain future JIT work.

### Professional authority is scoped

Professional authority must not become universal lifetime approval.

It should be scoped as appropriate to:

- purpose/pathway;
- relevant health/evidence basis;
- conditions/restrictions;
- time period/expiry where applicable;
- specific follow-up obligations;
- other governed limits.

Material health/evidence changes may invalidate or require reassessment of prior professional authority.

### Practitioner-derived restrictions

Where professional review produces plan-relevant restrictions, those restrictions must reach Plans as authoritative constraints through the proper Safety & Eligibility boundary.

Plans applies them deterministically and must not reconstruct or reinterpret the underlying clinical reasoning.

Their professional provenance remains traceable.

### Professional review ≠ clinical override

Ordinary professional review and exceptional clinical override are distinct.

A clinical override specifically permits or alters something the automated authority would otherwise not permit.

Overrides must remain:

- explicit;
- scoped;
- time-bound;
- audited;
- subject to any additional approval requirements in current Product Law.

There must be no generic “force eligible” or administrator bypass that silently defeats Safety authority.

### Professionally cleared automation versus practitioner-authored planning

Two distinct downstream paths must remain distinguishable:

#### Professionally cleared automated generation

Professional/Safety authority permits the standard deterministic plan engine to generate within governed restrictions.

The resulting Plan Version remains automated in provenance, with professional/Safety constraints clearly traceable.

#### Practitioner-authored or practitioner-modified plan

Professional judgement directly authors or materially modifies the plan.

The resulting Plan Version must preserve practitioner-authored/practitioner-modified provenance and must never masquerade as automatically generated output.

Core doctrine:

> Professional authority may change current operational permission or constraints, but it does so through Safety & Eligibility and never erases the provenance of either the automated adjudication or the practitioner-authored decision.



## 5.23 `HSP-WD-023` — Request-Bound Entitlements Authority and Exactly-Once Fulfilment

**Accepted at v0.25.0 after `HSP-PT-006`.**

Generation admission, execution, Plan fulfilment, and Entitlements consumption are distinct business moments.

### Request-bound Entitlements authority

Every logical Generation Request must be bound to the specific governed Entitlements authority/right under which it was admitted.

Plans must not reconstruct commercial authority from copied subscription/payment state.

The authoritative question is:

> Does the Entitlements authority bound to this Generation Request permit this fulfilment under its governed semantics?

### Admission is not consumption

Creation of a Generation Request or start of a Generation Attempt must not itself irreversibly consume the entitlement.

A failed Generation Attempt must preserve the entitlement according to current upstream law.

Retries of the same logical Request reuse the same request-bound Entitlements authority rather than attempting to spend the right again.

### Successful fulfilment boundary

The accepted working candidate for entitlement consumption/finalisation is:

> one logical Generation Request is durably fulfilled by one valid immutable Plan Version, with the corresponding Entitlements fulfilment/access consequence recorded exactly once.

The following are not authoritative consumption boundaries:

- Request submission;
- Attempt start;
- worker acknowledgement;
- notification delivery;
- email delivery;
- first participant view.

### Exactly-once cross-Domain effect

A successful business outcome requires durable convergence between:

- Plans & Nutrition:
  - one fulfilled logical Generation Request;
  - one valid immutable Plan Version;

and

- Entitlements:
  - one corresponding entitlement-use/access consequence.

Crash, retry, duplicate delivery, or partial failure must not result in:

- duplicate Plan fulfilment;
- duplicate entitlement consumption;
- a committed Plan whose right can be spent again;
- a consumed entitlement with no recoverable valid Plan outcome.

Exact transaction/reconciliation mechanics remain future JIT/implementation design.

### Consumable rights

For a one-use generation right, the platform needs durable claim semantics equivalent to:

- one logical Request is authorised against the right;
- competing Requests cannot both consume the same right;
- failed Attempts do not consume it;
- retries remain part of the same logical Request;
- terminal non-fulfilment preserves/releases the right where governed;
- successful fulfilment finalises exactly one use.

This doctrine does not prescribe a Resource, table, reservation object, or implementation mechanism.

### Domain boundary

- Commerce owns payment/contract truth.
- Entitlements owns generation/access-right truth and entitlement fulfilment/consumption.
- Safety & Eligibility owns clinical permission.
- Plans & Nutrition owns Request/Attempt/Plan fulfilment.

No Domain may silently reconstruct another owner's authority.

### Time-scoped expiry remains governed separately

This accepted doctrine does **not** resolve whether a time-scoped membership benefit must remain active through Plan fulfilment.

The recommended working direction is recorded separately in `HSP-WH-003`:

> a validly admitted Request should receive a bounded completion right even if the underlying membership/access period ends during execution.

That commercial policy remains subject to explicit upstream Product/Entitlements governance.




### `HSP-WD-023` accepted fulfilment refinement — `HSP-WD-031`

`HSP-WH-011` was accepted at v0.37.0 as `HSP-WD-031`.

`HSP-WD-031` supersedes only the earlier `HSP-WD-023` shorthand that could be read as “immutable Plan Version exists = Request fulfilled”.

The still-valid `HSP-WD-023` principles remain:

- admission ≠ consumption;
- the Request binds to governed Entitlements authority;
- retries do not spend repeatedly;
- non-fulfilment preserves the right;
- Plans + Entitlements must converge exactly once.

The refined fulfilment boundary is:

> one final Plan Version has satisfied all required pre-delivery gates and is durably delivered/made available under governed participant access, with the corresponding Entitlements consequence finalised exactly once.


## 5.24 `HSP-WD-024` — Generation Input Basis and Plan Result Provenance Are Distinct

**Accepted at v0.27.0 after `HSP-PT-007`.**

The platform must keep two concepts distinct:

### Immutable Generation Input Basis

Captured before deterministic execution and identifies the exact authoritative state/dependency context against which the Attempt is authorised to run.

It answers:

> What exact authorised state did this Attempt execute against?

### Immutable Plan Result Provenance Manifest

Finalised for a successful Plan candidate/version and identifies the exact governed result dependencies actually selected or calculated.

It answers:

> What exact governed components make up this delivered Plan Version?

### Delivered Plan linkage

A successful immutable Plan Version must link both:

`Generation Input Basis`
+
`Plan Result Provenance Manifest`

Historical version pinning explains the result but does not grant perpetual delivery authority if a dependency is later withdrawn.

Exact Ash/PostgreSQL representation remains JIT detail.



## 5.25 `HSP-WD-025` — `safety_paused` and `withdrawn` Are Different Plan Consequences

**Accepted at v0.28.0 after `HSP-PT-008`.**

The two already-locked Plan states must not be treated as synonyms.

### `safety_paused`

Represents potentially recoverable current-use suspension.

The specific Plan Version is preserved and may still be structurally valid, but current Safety authority does not presently permit normal current use and/or new personalised actions.

A later governed Safety outcome may permit:

- resumption of that exact Plan Version; or
- replacement/modification through a new immutable Plan Version.

The pause itself does not determine which.

### `withdrawn`

Means the specific Plan Version is no longer valid as the current usable Plan under governing authority.

Historical visibility and provenance may remain.

A withdrawn Plan Version does not return to ordinary current use merely because later Safety authority changes.

Continued current planning requires a governed correction/replacement/successor where applicable.

### Historical visibility remains separate

Both states may preserve historical evidence.

The participant experience must distinguish:

`visible in history`
from
`currently authorised for use`.

### Ownership

Safety & Eligibility determines clinical/current-use Safety authority where clinical interpretation is required.

Plans & Nutrition owns the Plan lifecycle consequence.

Content/legal/other upstream owners provide their governed withdrawal/correction authority without silently acquiring Plan ownership.

Exact transition tables remain future JIT detail and must respect the locked Product lifecycle.



## 5.26 `HSP-WD-026` — Safety-Paused Plan Resumption Requires Exact-Plan Revalidation

**Accepted at v0.29.0 after `HSP-PT-009`.**

A `safety_paused` Plan does not automatically require a replacement, and Safety clearance does not automatically reactivate it.

The governing question is:

> Does current Safety authority permit this exact immutable Plan Version, and does this exact Plan still satisfy all material current-use requirements?

### Same-Version resumption

The same immutable Plan Version may resume only when:

- current Safety authority permits that exact Plan;
- no material hard constraint changed in a way that makes the Plan invalid;
- no material calculation/input change requires different Plan content;
- no selected dependency is withdrawn or otherwise non-usable;
- the Plan has not already been superseded or withdrawn by another authoritative event.

Resumption changes current lifecycle/use authority, not immutable Plan content.

### Replacement required

If current Safety authority requires materially different Plan content, the old Plan is not edited in place.

A new immutable Plan Version is required with its own:

- Generation Input Basis where generated;
- Plan Result Provenance;
- safety/replacement lineage.

### Safety workflow state is not Plan authority

`Safety Case = cleared`

does not by itself mean:

`Plan = active`.

Plans & Nutrition must consume the actual current Safety authority and revalidate the exact Plan.

### Entitlements

Same-Version resumption is not a new paid generation.

Where a replacement is required solely as a governed safety correction/replacement, current Product Law governs it as a correction/replacement rather than ordinary paid re-personalisation.



## 5.27 `HSP-WD-027` — Authoritative Known/Received Time Is Set at Durable Owner-Boundary Receipt

**Accepted at v0.30.0 after `HSP-PT-010`.**

For safety-relevant evidence, the platform must distinguish:

- observation/effective time;
- authoritative known/received time;
- downstream processing time;
- decision/use time.

### Authoritative known/received time

NewYou's authoritative known/received time is established when the evidence is durably accepted into its owning authoritative boundary.

It is **not** postponed until:

- an async worker runs;
- a projection catches up;
- a cache refreshes;
- PubSub delivers;
- a downstream Domain notices;
- an operator opens the record.

### Consequence

Once authoritative safety-relevant evidence has been durably received, downstream lag may not redefine that evidence as “unknown”.

Correctness must rely on authoritative durable state or on a derived representation whose guarantees make stale omission impossible at the correctness boundary.

### Historical evidence

If authoritative evidence was received before a decision but missed because of internal lag, preserve:

- receipt time;
- decision time;
- stale/missed processing evidence;
- correction/reconciliation consequence.

Historical decisions still are not silently rewritten.

This doctrine selects no queue, cache, transaction, event or database implementation.



## 5.28 `HSP-WD-028` — Materially Conflicted Health Evidence Must Preserve Concurrent Assertions

**Accepted at v0.31.0 after `HSP-PT-011`.**

A safety-relevant health concept must not be forced into one scalar `current value` while materially conflicting evidence remains unresolved.

### Preserve assertion semantics

Material source assertions may need to preserve:

- the actual semantic claim;
- provenance/source;
- verification state;
- observation/effective time;
- authoritative known/received time;
- applicability/context;
- contradiction/correction/supersession relationships.

### Provenance is not universal rank

No generic rule such as:

`laboratory > practitioner > participant`

is authorised.

Provenance informs evidence handling but does not automatically establish clinical truth.

### Health ownership remains singular

Health Records owns health evidence and resolved health fact history.

Preserving multiple assertions does not create shared ownership.

Safety & Eligibility determines the operational Safety consequence of unresolved conflict.

Plans & Nutrition never decides which raw evidence source “wins”.

### Fail closed without fabricating truth

Safety may prohibit automated personalisation while evidence remains materially conflicted without falsely asserting that one source is clinically correct.

Where a current resolved health fact is legitimately established, its evidence and resolution authority remain traceable.

Exact assertion/resource representation remains JIT detail.



## 5.29 `HSP-WD-029` — Evidence Retraction Is Not the Same as Later Participant-State Change

**Accepted at v0.32.0 after `HSP-PT-012`.**

Evidence correction/retraction must explicitly distinguish:

- **wrong when made** — the earlier assertion should not have represented the participant's state at that earlier time;
- **later state change** — the earlier assertion remains valid historically, but a later observation establishes a different later state.

### Historical evidence remains

The original assertion is not silently deleted or mutated when later corrected.

Historical Safety adjudications and Plan Generation Input Bases retain the evidence/status they actually relied on at decision time.

### Current evidence usability changes prospectively

Once the correction/retraction is authoritatively known:

- the retracted assertion must no longer silently act as current usable evidence;
- current Health/Safety views incorporate the correction;
- new adjudications use the corrected evidence state.

### Two truths may coexist

The platform may later know:

> the earlier assertion was clinically wrong about the participant at T1

while also preserving:

> NewYou actually possessed and relied on that assertion before the correction became known.

Both are required for honest reconstruction.

### Correction authority remains governed

A disagreement from another source may create conflict but does not automatically retract practitioner-verified evidence.

Retraction/correction authority and professional-record boundaries remain governed by the owning Health/Professional Care contracts.

Exact representation remains JIT detail.



## 5.30 `HSP-WD-030` — Immutability and Retention Are Orthogonal

**Accepted at v0.34.0 after `HSP-PT-014`.**

Governed Health, Safety and Plan evidence is immutable against silent mutation **while retained**.

Immutability does not create indefinite identifiable-retention authority.

Privacy & Consent and category-specific deletion/retention authority determine whether retained evidence may later be deleted, irreversibly anonymised/de-linked, restricted under an approved retained obligation, or retained temporarily under professional/legal authority.

Any retained professional, financial, security or audit evidence must remain purpose-restricted and minimum-necessary and must not reconstruct deleted Account access, Entitlements, current Safety authority or personalised Plan use.

A consuming Domain must not copy sensitive source payloads merely to simplify provenance or audit. Immutability of a downstream copy cannot become a deletion loophole.

Exact deletion-contract representation remains future Privacy/JIT work.



## 5.31 `HSP-WD-031` — Fulfilment Is Final Governed Delivery, Not Mere Generation

**Accepted at v0.37.0 after `HSP-PT-017`.**

This is a superseding clarification of the `fulfilled` clause in `HSP-WD-011` and the fulfilment shorthand in `HSP-WD-023`.

A Generation Request becomes `fulfilled` only when:

1. one final Plan Version has satisfied every required pre-delivery gate for that governed pathway;
2. that Plan Version is durably made available/delivered under the participant's governed access;
3. the corresponding Entitlements fulfilment/access consequence is finalised exactly once.

### Review-gated requests may contain multiple immutable Plan Versions

A logical Request may contain:

- generated candidate P1;
- reviewed/rejected/superseded candidate P2;
- final approved deliverable P3;

while still producing exactly one fulfilled participant deliverable.

Immutable internal/review artifacts do not themselves consume the Plan fulfilment right.

### These are not universal fulfilment boundaries

- generation completion;
- reviewer approval alone;
- Plan `active`;
- first participant view/download;
- notification/email delivery;
- worker acknowledgement.

### Existing Request lifecycle remains

The state set remains:

`open → fulfilled | cancelled | invalidated | unfulfillable`.

A Request waiting on mandatory professional review remains `open` unless and until a governed terminal outcome occurs.

### Exactly-once convergence remains

Plans and Entitlements must still converge on:

- exactly one fulfilled participant deliverable;
- exactly one corresponding entitlement consequence.

Exact transaction/command representation remains JIT detail.



## 5.32 `HSP-WD-032` — Same-Lineage Successor Requests Must Revalidate the Predecessor They Advance

**Accepted at v0.39.0 after `HSP-PT-019`.**

Exactly-once fulfilment per Generation Request does not by itself protect the correctness of a Plan lineage.

Any Request that may replace/supersede a current Plan must bind to the Plan lineage/predecessor it intends to advance.

### Fulfilment guard

At the current-head/fulfilment transition, Plans revalidates that:

- the expected predecessor/current lineage authority is still valid;
- no incompatible successor has already advanced that same predecessor;
- all other current Safety/dependency/pathway gates still hold.

At most one competing Request may successfully advance the same lineage from the same predecessor.

### Stale competitor

A Request made stale by another successor:

- does not become a duplicate merely because it lost the race;
- may preserve its own intent/professional/candidate evidence where governed;
- cannot silently overwrite the newer current Plan;
- cannot be mechanically auto-merged/rebased where doing so would change the reviewed or authorised basis;
- requires a governed non-fulfilment/review/new-Request decision.

### Scope

This is not a universal “one Plan per participant” rule.

It applies to Requests competing to advance the same mutually exclusive Plan lineage/current-use position.

Exact locking/transaction/compare-and-swap implementation remains JIT proof detail.



## 5.33 `HSP-WD-033` — Participant-Owned Plan-Input Edits Need Explicit Applicability

**Accepted at v0.41.0 after `HSP-PT-021`.**

A participant-owned Plan-input edit made after Request admission does not silently mutate the immutable Generation Basis.

Each material edit must have explicit applicability semantics:

- applies to the current in-flight Request;
- applies to future Requests only;
- applies to another purpose/context.

If a material edit explicitly applies to the current Request and makes its basis/candidate stale:

- the old Request cannot fulfil from that stale basis;
- the old Generation Basis remains historical evidence;
- a governed terminal outcome is required;
- a newly authorised Request/basis is required where the participant still wants personalisation.

Unrelated or explicitly future-only edits do not automatically invalidate in-flight work.

This rule does **not** mean ordinary profile/progress logging triggers Plan regeneration.

### Upstream-derived cadence clarification

Current locked Product Law separately establishes that:

- participants may make daily or weekly progress entries;
- those entries do not regenerate the Plan immediately;
- ordinary Plan adjustments occur monthly using trends over an approved review window rather than isolated measurements;
- a formal review requires the applicable entitlement period, minimum Plan exposure and a complete check-in;
- an unused review can expire after a defined grace period;
- a no-change review may still count as the entitled review.

Therefore ordinary observations/profile logging and Plan-adjustment entitlement/fulfilment are separate lifecycles.

The current locked baseline does **not** authorise ordinary weekly Plan adjustments. A future product tier with weekly adjustment cadence would require an explicit Product/entitlement rule rather than being inferred from the fact that progress can be logged weekly.

Safety-critical new information remains a separate exception: it may trigger immediate Safety reevaluation/pause without constituting an ordinary periodic Plan adjustment.


# 6. Core fail-closed principles discovered so far

1. Historical existence does not equal current usability.
2. A newer health answer does not automatically invalidate prior evidence.
3. A correction that could affect safety triggers current safety re-evaluation.
4. Safety-sensitive unresolved conflicts block unsafe automation.
5. Plans do not independently choose which conflicting health evidence to believe.
6. Historical plans retain the exact provenance and authority context used when they were generated.
7. MVP automation is opt-in by approved case class, not opt-out by a blacklist of known problems.
8. Unsupported MVP cases do not receive a plausible-looking automated plan.
9. Expansion of automated eligibility must be explicit, clinically approved, testable, and versioned.

---

# 7. Expansion doctrine for future automation

A new case class should not become automated merely because implementation can technically handle it.

Before a previously excluded case class is admitted to automated plan generation, future planning should require evidence that at least the following are defined:

- required input facts;
- freshness/reconfirmation rules;
- provenance requirements;
- conflict-resolution behaviour;
- clinical safety rules;
- eligibility outcome rules;
- deterministic plan-generation rules;
- exclusion/substitution behaviour;
- explainability;
- failure behaviour;
- safety-pause/reassessment behaviour;
- versioning;
- test/proof expectations;
- operational visibility and escalation.

Exact approval authority and proof gates remain subject to current Product/Architecture/Domain law.

---

# 8. Current unresolved discovery areas

The following areas remain to be grilled in later rounds:

1. Health information catalogue and why each fact is collected.
2. Stable vs current vs safety-sensitive vs time-sensitive classification.
3. Reconfirmation triggers and validity windows.
4. Health fact effective-time semantics.
5. Correction workflow and downstream impact discovery.
6. Conflict resolution and clarification workflow.
7. Minimum current facts required before eligibility can be evaluated.
8. Explicit MVP automated allow-list principles.
9. Exact boundary between `insufficient_information`, `general_wellness_only`, and `professional_review_required`.
10. Safety Case creation triggers and relationship to eligibility evaluation.
11. Professional/manual review workflow for the mature platform.
12. Practitioner-authored plan lifecycle and follow-up.
13. Plan-generation input contract.
14. Deterministic plan generation stages.
15. Generation concurrency/idempotency.
16. Mid-generation health/safety changes.
17. Plan activation, supersession, withdrawal, and safety pause.
18. Reassessment and adjustment.
19. Recovery/reconciliation after partial failure.
20. Participant UX for safe refusal, clarification, and professional escalation.

---



## 2.4 Open working hypotheses register

Open hypotheses use local keys of the form `HSP-WH-###`.

These are non-governed working keys only.

| Local key | Hypothesis | Strength | Trigger |
|---|---|---|---|
| `HSP-WH-001` | Eligibility Evaluation and active-plan Safety Impact Assessment are conceptually distinct adjudications, even if future implementation shares infrastructure | `RESOLVED → HSP-WD-021` | Raised by `HSP-PT-004`; accepted at v0.23.0 |
| `HSP-WH-002` | Generation admission and entitlement consumption are distinct; a logical Generation Request should be bound to a specific durable Entitlements authorization/claim, with consumable rights finalised only on successful fulfilment | `RESOLVED → HSP-WD-023` | Raised by `HSP-PT-006`; accepted at v0.25.0 |
| `HSP-WH-003` | For time-scoped membership benefits, a validly admitted Generation Request should receive a bounded completion right that may survive expiry of the underlying period; no new Request may start after expiry | `RECOMMENDED DIRECTION / UPSTREAM PRODUCT-ENTITLEMENTS POLICY NEEDED` | Raised by `HSP-PT-006`; Policy B preferred at v0.25.0 |
| `HSP-WH-004` | Separate the immutable pre-generation input/dependency basis from the exact post-generation Plan result provenance manifest; the final Plan Version links both | `RESOLVED → HSP-WD-024` | Raised by `HSP-PT-007`; accepted at v0.27.0 |
| `HSP-WH-005` | `safety_paused` and `withdrawn` represent different Plan consequences: `safety_paused` is potentially recoverable current-use suspension; `withdrawn` means the Plan Version itself is no longer valid for current use, while historical visibility may remain | `RESOLVED → HSP-WD-025` | Raised by `HSP-PT-008`; accepted at v0.28.0 |
| `HSP-WH-006` | A `safety_paused` Plan may resume as the same Plan Version only when current Safety authority explicitly permits that exact Plan and no material Plan input/constraint/dependency change requires different Plan content; otherwise a new immutable Plan Version is required | `RESOLVED → HSP-WD-026` | Raised by `HSP-PT-009`; accepted at v0.29.0 |
| `HSP-WH-007` | For safety-relevant evidence, authoritative `known/received` time is established when NewYou durably receives/records the evidence in its owning authority boundary, not when an asynchronous projection, worker or downstream consumer later processes it | `RESOLVED → HSP-WD-027` | Raised by `HSP-PT-010`; accepted at v0.30.0 |
| `HSP-WH-008` | Safety-relevant health concepts must preserve multiple concurrent source assertions when they materially conflict; a single scalar `current value` must not erase unresolved evidence. Provenance, semantic claim, temporal scope and resolution status remain explicit | `RESOLVED → HSP-WD-028` | Raised by `HSP-PT-011`; accepted at v0.31.0 |
| `HSP-WH-009` | Evidence correction/retraction must distinguish “the earlier assertion was wrong when made” from “the earlier assertion was true then but the participant state later changed”; historical decisions retain the exact assertion status they relied on, while current evidence usability changes prospectively from the correction/retraction’s authoritative known time | `RESOLVED → HSP-WD-029` | Raised by `HSP-PT-012`; accepted at v0.32.0 |
| `HSP-WH-010` | Immutability and retention are orthogonal: governed Health/Safety/Plan evidence is immutable against silent mutation while retained, but full deletion/anonymisation/retained-obligation policy may later remove or de-identify eligible records; retained audit/professional evidence must remain minimum-necessary and must not reconstruct deleted product access | `RESOLVED → HSP-WD-030` | Raised by `HSP-PT-014`; accepted at v0.34.0 |
| `HSP-WH-011` | Refine `HSP-WD-011` and `HSP-WD-023`: Request fulfilment is not the mere existence of a generated immutable Plan Version. A Request is fulfilled only when one final Plan Version has satisfied every required pre-delivery gate for that pathway and is durably made available/delivered under the participant’s governed access, with the corresponding Entitlements consequence finalised exactly once. Review-gated Requests may contain multiple immutable generated/review versions but exactly one fulfilled deliverable; activation/first view/notification are not universal consumption boundaries | `RESOLVED → HSP-WD-031` | Raised by `HSP-PT-017`; accepted at v0.37.0; explicit superseding clarification of the fulfilment clause in `HSP-WD-011` and `HSP-WD-023` |
| `HSP-WH-012` | Requests that may replace/supersede the same current Plan lineage must bind to the predecessor/current-head authority they intend to replace and revalidate that lineage at fulfilment. Exactly-once fulfilment per Request is insufficient: only one competing Request may successfully advance the same lineage head from the same predecessor; a stale competitor must not later overwrite the newer current Plan merely because its own Request is otherwise valid | `RESOLVED → HSP-WD-032` | Raised by `HSP-PT-019`; accepted at v0.39.0 |
| `HSP-WH-013` | Participant-owned Plan-input edits made after Request admission need explicit applicability semantics: future-only versus intended to supersede the in-flight Request. The immutable Generation Basis must never be silently mutated. A material edit explicitly applicable to the current Request must prevent fulfilment from the stale basis and require governed cancellation/invalidation plus a newly authorised Request; unrelated or future-only edits do not automatically invalidate in-flight work | `RESOLVED → HSP-WD-033` | Raised by `HSP-PT-021`; accepted at v0.41.0 |



## 2.5 Upstream policy / authority delta register

Delta identifiers use local keys of the form `HSP-UPD-###`.

They are non-governed working references only. They do not amend Product, Architecture, Domain, Roadmap, Content, Entitlements, or JIT authority.

| Local key | Missing/unclear policy | Required authority level | Working direction | Status |
|---|---|---|---|---|
| `HSP-UPD-001` | Whether a time-scoped membership benefit must remain active through Plan fulfilment when the Generation Request was validly admitted before expiry | Product / Entitlements semantics | Prefer bounded completion authority for the already-admitted Request (Policy B) | OPEN — upstream policy required |
| `HSP-UPD-002` | Whether an already-admitted in-flight generation may finish using an ordinary **superseded but not withdrawn** plan-content/rules dependency, or must restart on the successor version | Content/Plan governance; escalate to Product only if commercial promise changes | Distinguish supersession from withdrawal; never infer one policy from the other | OPEN — authority clarification required |
| `HSP-UPD-003` | Exact mapping from a withdrawn delivered dependency to affected Plan consequence (`correct/replace`, `safety_paused`, `withdrawn`, participant warning, Safety adjudication where clinically relevant) | Content/Plan/Safety governance according to withdrawal reason and affected scope | Withdrawal declaration must include affected-delivery impact semantics; do not make Plans or UI infer them | OPEN — authority/JIT clarification required |
| `HSP-UPD-004` | Category-specific full-deletion treatment for Plan Versions, Generation Input Bases, Plan Result Provenance, Safety adjudications/cases and practitioner-derived variants | Privacy & Consent orchestration + owning Domain deletion contracts; professional retention authority where applicable | Immutability applies while retained; no blanket indefinite identifiable retention; exact delete/anonymise/restrict/retain mapping must be explicit before JIT freeze | OPEN — Privacy/JIT deletion-contract clarification required |
| `HSP-UPD-005` | Customer remedy when a paid/consumable Plan entitlement is validly admitted but current approved Plans capability is `unfulfillable` for mandatory hard constraints | Product / Commerce / Entitlements semantics | Preserve the entitlement at minimum; do not let Plans invent refund/credit rules. Define whether/when refund, credit, alternate product, expiry or later retry is owed | OPEN — upstream commercial policy required |
| `HSP-UPD-006` | Maximum pending/resolution promise and customer remedy when a required professional Plan review cannot be completed within the governed service window because of reviewer/capacity/provider failure | Product / Professional Care / Commerce / Entitlements; exact escalation timers may be downstream operating/JIT policy | Reviewer loss must not consume another Plan entitlement or silently terminate the Request. Define participant-facing resolution promise, authorised timeout/cancellation semantics, refund/credit/alternate-review remedy and interaction with time-scoped entitlements | OPEN — upstream service/commercial policy required |
| `HSP-UPD-007` | Meaning/application of locked `DEC-045` “plan refunds end after generation” for review-gated or practitioner-reviewed Plans where an immutable generated artifact may exist before approved participant delivery, including participant cancellation, provider cancellation and stale late completion after a terminal Request | Product / Commerce / Entitlements, informed by Plans/Professional Care workflow | Do not equate refund boundary with Request fulfilment or entitlement consumption. Clarify what qualifying `generation` means for this commercial rule and whether review-gated/provider-failure cases require an explicit exception/amendment | OPEN — upstream Product/Commerce clarification required |
| `HSP-UPD-008` | Commercial/entitlement consequence when the participant deliberately changes material Plan inputs after paid Request admission but before first fulfilment, especially after generation has begun | Product / Commerce / Entitlements | Distinguish pre-fulfilment change-of-intent from post-delivery `DEC-038` re-personalisation. Define whether the same unconsumed right may fund the replacement Request, whether a fee/new right is ever required, and interaction with `DEC-045` once generation has occurred | OPEN — upstream Product/Commerce clarification required |

A delta stays open until the correct governed authority explicitly resolves it.

Implementation and JIT work must not silently choose an open delta.


# 9. Scenario pressure-test register

Scenario identifiers use local keys of the form `HSP-PT-###`.

They are non-governed working evidence only.

Every scenario should prove, at minimum:

- initiating fact/event;
- authoritative owner(s);
- current authority before the event;
- lifecycle transitions;
- guards/invariants;
- side effects;
- participant-visible outcome;
- historical evidence retained;
- retry/recovery behaviour;
- conflict with any accepted working decision or upstream authority;
- verdict.

## `HSP-PT-001` — Safety-relevant medication change during in-flight generation

**Status:** PRESSURE-TESTED  
**Verdict:** PASS  
**New contradiction found:** NO

### Preconditions

Assume:

- the participant has a valid `open` Generation Request;
- current Safety authority is `eligible_automated`;
- an immutable Generation Basis has been captured;
- a Generation Attempt is `in_progress`;
- the participant records a medication change;
- the current approved Safety protocol classifies that medication change as requiring immediate Safety re-evaluation.

The scenario intentionally does **not** decide which medications trigger this consequence. That remains clinical/Safety authority.

### Ownership

- **Health Records:** owns the newly recorded medication truth, provenance, effective/known time, and history.
- **Safety & Eligibility:** owns the impact classification, reevaluation, current eligibility/Safety authority, restriction/case consequence where applicable.
- **Plans & Nutrition:** owns the Generation Request/Attempt/Plan outcome and must obey current Safety authority.
- **Commerce / Entitlements:** remains authoritative for the participant's entitlement; generation failure/invalidation must not silently consume it.

### Expected flow

1. Health Records durably commits the medication change.
2. The old eligibility authority no longer authorises a **new** personalised action once reevaluation is required.
3. Safety reevaluation is durably/reconcilably triggered against a new immutable Safety evaluation basis.
4. The in-flight Generation Attempt may finish internal computation, but its candidate may not be committed/delivered using the stale authority.
5. At the current-authority revalidation boundary, generation detects that its Safety basis is no longer current.
6. The Attempt terminates with an authority-invalidated/stale-authority outcome classification.
7. The logical Generation Request becomes `invalidated`, because its original material authority context no longer permits fulfilment.
8. No Plan Version is created from that request.
9. The participant's plan entitlement is preserved because no valid complete plan was successfully delivered/fulfilled.
10. If current policy requires impact on an already-active prior Plan, Safety applies that separately (including `safety_paused` where upstream law requires it).
11. If later Safety authority again permits automated generation, the platform creates a **new** Generation Basis and **new** logical Generation Request. The invalidated request is never resurrected.

### Guards / invariants proven

- `HSP-WD-003` — safety-relevant changes/corrections drive Safety consequence.
- `HSP-WD-008` — immutable generation basis does not outrank current delivery authority.
- `HSP-WD-010` — Request, Attempt and Plan remain separate.
- `HSP-WD-011` — invalidated Generation Request is terminal.
- `HSP-WD-013` — historical Generation Basis remains evidence of what the attempt used.
- `HSP-WD-020` — old eligibility cannot authorise new personalised action while required reevaluation is outstanding.

### Historical evidence retained

The system must be able to reconstruct:

- the original Generation Request;
- the original Generation Basis;
- the Attempt and its classified terminal outcome;
- the medication change and its temporal/provenance evidence;
- the Safety reevaluation basis/result;
- the reason the request became invalidated;
- the fact that no Plan Version was produced/fulfilled from the invalidated request.

### Retry / recovery

A worker/process retry must not simply replay the old generation.

Recovery first reconciles durable truth:

- Is the old request still `open`? **No — it is `invalidated`.**
- Has current Safety authority been re-established? Possibly, but that cannot resurrect the old request.
- Was a Plan already durably committed? If yes, reconcile that separately; this scenario assumes no valid commit occurred before the authority change was enforced.

### Participant outcome

The participant must not receive the stale candidate Plan.

Participant-facing messaging should explain that new health information requires the platform to re-check safety before creating/adjusting the personalised plan, without exposing unnecessary internal engine terminology.

### Result

**PASS.**

The current working model handles this scenario coherently without requiring a new Domain or a new accepted design doctrine.

This scenario specifically validates the separation between:

`historical generation basis`
and
`current authority to deliver`.



## `HSP-PT-002` — Plan commits successfully, then worker crashes before acknowledging success

**Status:** PRESSURE-TESTED  
**Verdict:** PASS  
**New contradiction found:** NO

### Preconditions

Assume:

- the participant has one valid `open` Generation Request;
- current Safety and entitlement authority permit fulfilment;
- one Generation Attempt is executing;
- the complete valid Plan Version and fulfilment business state are durably committed;
- the worker/process crashes before it records/emits its normal execution acknowledgement.

### Ownership and authority

- **Plans & Nutrition durable business state** owns whether the Generation Request was fulfilled and whether the immutable Plan Version exists.
- Worker/process acknowledgement is operational evidence only.
- Commerce/Entitlements must consume fulfilment through the governed durable business boundary rather than a transient worker acknowledgement.

### Expected recovery flow

1. Process restarts / job is retried / reconciliation occurs.
2. Recovery checks durable Generation Request and Plan business state before doing new generation work.
3. Durable state shows:
   - the request is already `fulfilled`;
   - exactly one Plan Version was committed for the request.
4. The previous Attempt is reconciled to successful durable fulfilment (or otherwise linked to the committed success according to future JIT representation).
5. No new Generation Attempt is permitted to create another Plan Version for that logical request.
6. No second entitlement consumption may occur.
7. Any missed notifications/projections may be repaired separately and idempotently.

### Guards / invariants proven

- `HSP-WD-007` — all-or-nothing plan commit.
- `HSP-WD-010` — Request/Attempt/Plan separation.
- `HSP-WD-011` — fulfilled request is terminal.
- `HSP-WD-012` — worker acknowledgement is not business authority.
- `HSP-WD-013` — committed Plan Version remains reproducible from its basis.

### Historical evidence retained

The platform must be able to distinguish:

- business fulfilment succeeded;
- execution acknowledgement was interrupted;
- any later reconciliation/retry occurred;
- no second Plan was created.

### Participant outcome

The participant has one valid Plan Version.

A transient worker crash after durable success must not surface as “generation failed” if durable business truth shows success.

### Result

**PASS.**

The current model correctly treats durable committed business state as authoritative over worker/process acknowledgement.

---

## `HSP-PT-003` — Two tabs/devices submit generation concurrently

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH JIT PROOF OBLIGATION  
**New contradiction found:** NO

### Preconditions

Assume:

- the participant is currently authorised for automated plan generation;
- the participant has one logical entitlement/use right for the generation;
- two browser tabs or devices submit the same intended generation nearly simultaneously;
- LiveView single-active-workspace UX either fails, races, or is absent.

The test intentionally assumes the UX protection does **not** save us.

### Required business result

The system must converge on:

- one logical Generation Request for the one business intent/right;
- at most one successful Plan Version;
- at most one entitlement fulfilment/consumption;
- duplicate execution safely rejected, coalesced, reconciled, or rendered harmless.

### Expected flow

1. Both requests arrive independently at server authority.
2. Server-side business guards determine whether they represent the same logical generation right/request.
3. At most one durable open logical request is authorised for that same business identity/entitlement context.
4. Duplicate execution may:
   - resolve to the existing request;
   - observe that fulfilment is already in progress;
   - create separate execution Attempts only where the future JIT model explicitly allows safe execution races;
   - never create a second successful business fulfilment.
5. If both executions race through computation, commit authority must still allow only one successful Plan fulfilment.
6. The losing/racing execution reconciles to the already authoritative outcome rather than creating a competing Plan Version.
7. LiveView/Presence may warn or make one workspace read-only, but correctness does not depend on that behaviour.

### Guards / invariants proven

- `HSP-WD-005` — automation requires positive authority.
- `HSP-WD-008` — current authority is revalidated before successful commit.
- `HSP-WD-009` — single-active-workspace is defence in depth only.
- `HSP-WD-010` — one logical request is not equivalent to each browser submission.
- `HSP-WD-011` — fulfilled request is terminal.
- `HSP-WD-012` — execution races do not redefine business truth.

### JIT proof obligation

The conceptual model passes, but the future JIT/implementation proof must demonstrate an actual durable uniqueness/idempotency mechanism sufficient under:

- simultaneous server requests;
- multiple BEAM processes;
- retries;
- reconnects;
- multiple devices;
- process/node restart.

The proof must not rely solely on:

- LiveView process state;
- Phoenix Presence;
- browser-local storage;
- client-side debounce;
- UI disablement.

The exact PostgreSQL/Ash transaction/constraint/idempotency mechanism remains future implementation design.

### Participant outcome

The participant receives or ultimately resolves to one Plan fulfilment, not two.

Duplicate user interaction may produce a benign “already processing/already generated” UX, but never duplicate business effects.

### Result

**PASS WITH JIT PROOF OBLIGATION.**

The working model is coherent, but concurrency correctness is intentionally not considered proven until future implementation-grade evidence demonstrates the durable server-side mechanism.

---


## `HSP-PT-004` — Serious allergy correction after an active Plan has already been delivered

**Status:** PRESSURE-TESTED  
**Verdict:** CHANGES REQUIRED TO WORKING DESIGN  
**Upstream contradiction found:** NO  
**Working-design issue found:** YES — `HSP-WD-021` is too narrow if one “Safety Evaluation” concept is expected to represent both eligibility and active-plan impact.

### Preconditions

Assume:

- the participant already has one immutable delivered Plan Version in the governed `active` Plan lifecycle state;
- that Plan was generated from the health/evidence and Safety authority actually known at the time;
- the participant later corrects an earlier answer and reports a serious food allergy;
- the correction indicates the allergy was already true before the active Plan was generated, but NewYou did not know that at generation time;
- the current approved clinical/Safety protocol classifies this corrected allergy as a safety-relevant high-risk fact requiring immediate current reevaluation and active-plan safety consequence.

The scenario intentionally does **not** decide which allergies or severities trigger high-risk handling. That remains behind current clinical/Safety authority.

### Ownership

- **Health Records** owns:
  - the original historical answer;
  - the correction event;
  - the corrected current allergy fact;
  - provenance;
  - effective time versus recorded/known time;
  - the fact that the platform learned the correction only after plan delivery.

- **Safety & Eligibility** owns:
  - interpretation of the corrected fact under the current approved protocol;
  - current eligibility/Safety authority;
  - any Safety Case;
  - the authoritative active-plan safety consequence.

- **Plans & Nutrition** owns:
  - the immutable historical Plan Version;
  - the Plan lifecycle transition required by current Safety authority;
  - any later correction/replacement Plan Version.

### Expected flow

1. Health Records durably records the correction without overwriting the original historical submission.
2. The corrected allergy becomes current health truth with explicit provenance and temporal semantics.
3. The historical Generation Basis of the already-delivered Plan is **not rewritten**. It must continue to show what the platform actually knew and used when it generated that Plan.
4. Because the approved current protocol classifies the correction as requiring immediate Safety reevaluation, the old eligibility authority no longer authorises new personalised actions.
5. Safety evaluates the corrected/current basis.
6. Where current Product/clinical authority requires it, Safety issues the authoritative consequence that the active Plan may no longer remain normally usable.
7. Plans applies the governed lifecycle consequence, including `safety-paused` where upstream Product Law requires that state.
8. The historical Plan Version remains visible as historical evidence; it is not deleted or mutated to pretend the allergy was known during original generation.
9. New adjustments/regeneration remain blocked until current Safety authority permits them.
10. If a replacement/corrected Plan is later authorised, it is a **new immutable Plan Version** with a new basis/provenance lineage.

### Historical-truth invariant

Two facts must remain simultaneously true:

> The allergy may actually have existed before the Plan was generated.

and

> NewYou did not know/possess that corrected allergy information when the historical Plan was generated.

The platform must preserve both.

Late-arriving correction changes **current safety authority** but must not falsify historical system knowledge.

### Participant outcome

The participant should receive a clear safety-oriented explanation that newly corrected health information means the current personalised Plan must be re-checked before continued personalised use/adjustment.

The participant should not receive an engineering explanation or be led to believe the prior historical Plan was generated using the corrected allergy information.

Historical access may remain available according to Product Law, but the UI must clearly distinguish historical visibility from current safe-use authority.

### Pressure test against existing working decisions

The scenario strongly validates:

- `HSP-WD-002` — correction is distinct from genuine state change.
- `HSP-WD-003` — safety-relevant correction is a Safety event.
- `HSP-WD-013` — historical Generation Basis is immutable evidence.
- `HSP-WD-015` — allergy-derived mandatory exclusion is a hard constraint when authorised as such.
- `HSP-WD-018` — effective time and recorded/known time remain distinct.
- `HSP-WD-020` — immediate Safety reevaluation can block new personalised actions.
- `HSP-WD-022` — Plans obeys Safety authority rather than reinterpreting the allergy itself.

### The model weakness

`HSP-WD-021` currently defines a Safety Evaluation as an immutable adjudication producing one of the four eligibility outcomes:

- `eligible_automated`;
- `general_wellness_only`;
- `professional_review_required`;
- `insufficient_information`.

That is coherent for the question:

> May this participant enter/proceed through this personalised pathway?

But this scenario also requires Safety to answer a different question:

> What must happen to an already-active Plan because this material health fact changed?

Those are not obviously the same adjudication contract.

The active-plan consequence may include:

- no current-plan change;
- block new personalisation until reevaluation;
- apply a restriction;
- require clarification/review;
- require `safety-paused`;
- another governed active-plan consequence.

Forcing those consequences into the four eligibility outcomes would either:

- overload eligibility semantics;
- make Plan lifecycle consequences implicit side effects with weak provenance;
- or encourage Plans to interpret raw health/eligibility information itself.

### Proposed refinement — `HSP-WH-001`

Pressure-test the following conceptual split:

#### Eligibility Evaluation

Answers:

> Is this participant currently permitted to enter/proceed through the relevant personalised pathway under this exact basis and protocol?

Produces the governed four eligibility outcomes.

#### Safety Impact Assessment

Answers:

> Given this material current change and any affected active Plan/context, what current Safety consequence is required?

Its exact outcome vocabulary is **not yet frozen**.

It may establish an authoritative Plan-safety consequence and/or create/advance a Safety Case.

#### Shared implementation is still possible later

This conceptual split does **not** require two Ash Resources, two tables, two services, or a new Domain.

Future JIT may prove that both are represented by one generalized Safety adjudication model with explicit purpose/context.

The working requirement is only:

> Do not assume eligibility adjudication and active-plan impact adjudication have the same contract merely because both belong to Safety & Eligibility.

### Result

**CHANGES REQUIRED TO WORKING DESIGN.**

No upstream Product/Architecture/Domain contradiction was found.

The accepted working model remains broadly sound, but `HSP-WD-021` should not be treated as complete until `HSP-WH-001` is resolved.



## `HSP-PT-005` — Safety protocol withdrawn while a large population has active Plans

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH GOVERNANCE + JIT PROOF OBLIGATIONS  
**Upstream contradiction found:** NO

### Preconditions

Assume:

- Safety Protocol P7 was previously approved and effective;
- many participants hold current Eligibility Evaluations and active Plans whose authority/provenance depends materially on P7;
- a new governed decision withdraws P7 for safety reasons;
- the withdrawal declares that affected existing participants require **immediate reassessment**;
- the population may be very large (for example, tens of thousands of active participants).

The exact clinical reason for withdrawal is out of scope for this design test.

### First critical distinction: withdrawal policy must be complete

`immediate reassessment`

does **not by itself** answer:

> Must every affected active Plan become `safety_paused` immediately at the withdrawal effective time?

Nor does it answer:

> May an affected Plan continue until its individual reassessment finishes?

Those are separate governed consequences.

Therefore a safety-relevant protocol withdrawal/release must define at least:

- effective time;
- affected cohort / applicability criteria;
- whether existing current eligibility authority remains usable during the reassessment window;
- whether new personalised actions are blocked immediately;
- whether existing active Plans may continue, are restricted, or must enter `safety_paused`;
- required reassessment deadline/urgency where applicable;
- how already-in-flight generation/adjustment is treated;
- what happens where an affected participant cannot be reassessed immediately.

Implementation must not infer these clinical/product consequences.

### Ownership

- **Safety & Eligibility** owns:
  - protocol applicability to current Safety authority;
  - identification semantics for the affected safety cohort;
  - reevaluation/adjudication;
  - authoritative Safety consequences.

- **Plans & Nutrition** owns:
  - applying the resulting governed Plan lifecycle consequence;
  - preserving immutable historical Plan Versions;
  - blocking/allowing new generation or adjustment according to current Safety authority.

- **Health Records** remains source authority for participant health facts and does not decide protocol impact.

- Operational infrastructure may accelerate fan-out/reconciliation but must not become authority.

### Required conceptual flow

1. The protocol withdrawal is durably governed and becomes effective at its explicit effective time.
2. Historical adjudications performed under P7 remain immutable evidence that P7 was the applicable protocol when those decisions were made.
3. P7 is no longer usable for new current adjudications where the withdrawal says it is withdrawn.
4. The withdrawal's explicit impact policy determines whether prior P7-derived current authority:
   - remains temporarily usable;
   - is limited to historical visibility only;
   - blocks new personalised actions;
   - requires immediate active-plan Safety consequence.
5. The affected participant cohort must be deterministically/reconcilably discoverable from authoritative data and protocol/basis provenance.
6. Each affected participant receives a new current Safety adjudication under the applicable replacement/current protocol or governed fallback path.
7. Where the withdrawal policy requires active-plan suspension, Plans applies `safety_paused` while preserving history.
8. In-flight generation/adjustment based on withdrawn P7 authority cannot commit if current-authority revalidation fails.
9. Reassessment/fan-out failures remain discoverable and retryable until every required affected participant reaches a governed terminal/current state.

### Historical evidence invariant

Withdrawal does not make earlier historical decisions fraudulent or rewrite them.

The system must preserve:

> At time T1, P7 was approved/effective and produced adjudication E7.

and separately:

> At time T2, P7 was withdrawn and could no longer provide current authority according to the withdrawal impact policy.

### Safety Adjudication model pressure test

The refinement of `HSP-WD-021` passes this scenario.

Two different adjudication purposes are useful:

- new/replacement **Eligibility Evaluations** determine current pathway eligibility under the applicable protocol;
- **Safety Impact Assessments** determine the consequence of P7 withdrawal for affected active Plans/current context.

They may share infrastructure later, but forcing the protocol-withdrawal impact into the four eligibility outcomes would be inadequate.

### Scale does not justify new authority

A withdrawal affecting 50,000 participants may require substantial operational fan-out, batching, queues or reconciliation mechanisms.

That scale does **not** justify:

- moving Safety authority into a queue;
- treating an event bus as the source of truth;
- adding a new Domain merely for bulk processing;
- allowing incomplete fan-out to disappear silently.

Authority remains in the owning durable Domains.

### Governance obligation

Before a materially safety-relevant protocol version can become effective, its publication/withdrawal contract must define its impact on already-authorised participants/Plans.

A withdrawal that says only:

> `P7 withdrawn`

without affected-cohort and active-authority consequences is operationally incomplete.

This is a governance completeness requirement, not an implementation detail.

### Future JIT proof obligation

Future implementation-grade design/proof must demonstrate a durable and reconcilable mechanism that can:

- identify every affected participant/Plan;
- process very large cohorts incrementally;
- survive process/node restarts;
- retry safely;
- avoid duplicate or conflicting Safety consequences;
- expose unresolved backlog;
- prove completion or remaining population;
- prevent stale P7 authority from being used after its permitted boundary.

The exact mechanism is not selected here.

### Result

**PASS WITH GOVERNANCE + JIT PROOF OBLIGATIONS.**

The current conceptual ownership model survives large-scale protocol withdrawal.

The test strengthens one requirement:

> A protocol impact declaration must specify not only reassessment timing but the operational authority/consequence during the reassessment window.

No new Domain is justified.



## `HSP-PT-006` — Entitlement expires or membership access ends while generation is in progress

**Status:** PRESSURE-TESTED  
**Verdict:** CHANGES REQUIRED TO WORKING DESIGN + UPSTREAM COMMERCIAL POLICY CLARIFICATION  
**Upstream contradiction found:** NO  
**Working-design gap found:** YES — generation admission, entitlement authorization/claim, fulfilment and consumption are not yet precise enough.

### Preconditions

Assume:

- the participant is Safety-authorised for generation;
- Plans receives authority to start one legitimate Generation Request;
- the request is based on a qualifying commercial/access right;
- a Generation Attempt is already in progress;
- before the Plan can be successfully fulfilled, the participant's relevant membership/access period ends or another time-scoped entitlement ceases to be current.

This test deliberately distinguishes:

1. a **consumable entitlement/right** such as a once-off or specifically granted generation right; and
2. a **time-scoped permission** such as generation/re-personalisation available only while a qualifying membership/add-on is active.

Those are not necessarily the same commercial semantics.

### Existing upstream boundaries

Current Domain Law separates:

`Commerce contract/payment truth`
from
`Entitlements access-right truth`.

Therefore Plans must not decide fulfilment authority by interpreting payment-provider or subscription state directly.

Plans needs a governed Entitlements answer.

Current Product Law also establishes relevant boundaries including:

- once-off delivered Plans retain permanent access;
- new preference/progress re-personalisation requires a new purchase or active qualifying membership/add-on;
- after membership cancellation, historical/purchased assets remain while new adjustments end;
- failed generation must preserve entitlements and avoid duplicate generation/double charge.

The exact **mid-flight expiry** rule is not explicitly resolved by those statements.

### Finding 1 — admission is not consumption

Starting a Generation Request or Attempt cannot itself be treated as irreversible entitlement consumption.

If generation later fails before valid fulfilment, current upstream law requires the entitlement to be preserved.

Therefore at least three conceptual moments exist:

`entitlement permits/adopts request`
→ `generation executes`
→ `successful fulfilment causes the governed entitlement consequence`

This does not yet prescribe a Resource/table/state machine.

### Finding 2 — generation must bind to a specific Entitlements authority

The Generation Basis must not merely record:

`membership_active = true`

as a copied commercial fact.

It should identify the exact governed Entitlements authority/right under which that Generation Request was admitted.

Future retries and commit-time revalidation must reason about that specific authority rather than re-deriving access independently inside Plans.

### Finding 3 — a consumable right needs durable claim semantics

For an entitlement that can fund only one generation, concurrent requests must not both successfully spend it.

Conceptually, the platform needs durable semantics equivalent to:

- the right is valid for this logical Generation Request;
- competing logical requests cannot simultaneously consume the same one-use right;
- failed Attempts do not consume it;
- retries of the same Request reuse the same logical entitlement authorization;
- terminal non-fulfilment releases/preserves the right where upstream policy says it remains usable;
- successful fulfilment causes exactly one durable entitlement consumption/fulfilment consequence.

This may later be implemented as reservation, claim, allocation, grant-use linkage, transactional guard, or another proven mechanism.

The implementation representation is intentionally not chosen here.

### Finding 4 — membership expiry mid-flight is a Product/Entitlements policy question

Two coherent product policies are possible for a time-scoped membership benefit.

#### Policy A — validity required through fulfilment

The participant must still hold qualifying current Entitlements authority at the successful commit/fulfilment boundary.

If the period ends first:

- the candidate Plan may not be committed/delivered under stale commercial authority;
- the Generation Request becomes invalidated or otherwise terminates under the exact future governed contract;
- no entitlement consumption occurs.

#### Policy B — valid admission grants a bounded completion right

If the participant validly created the Generation Request while entitled, that request receives a scoped completion authority that may survive the membership period ending.

Then:

- no new Generation Request may start after the membership benefit ends;
- the already-authorised request may finish within its governed completion rules/window;
- retries remain tied to the original request/authorization;
- no unlimited post-expiry regeneration right is created.

Both policies are technically coherent.

The working pack must **not choose between them silently**, because this affects what the customer purchased/earned.

Current upstream law does not appear to state the mid-flight boundary precisely enough.

Therefore `HSP-WH-003` is an upstream commercial/Product-policy clarification obligation before the relevant implementation contract is frozen.

### Finding 5 — current membership state is not the same as request authority

Whichever policy is chosen, the correct commit question is not necessarily:

> Is the participant's membership active at this instant?

The correct question is:

> Does the exact Entitlements authority bound to this Generation Request still permit this fulfilment under its governed semantics?

That distinction supports both Policy A and Policy B without letting Plans own commercial logic.

### Finding 6 — worker completion, notification and first view are not entitlement consumption

The following must not define commercial consumption:

- worker returned `ok`;
- background job acknowledged;
- notification sent;
- email delivered;
- participant opened the Plan;
- participant first viewed the Plan.

Those are operational/delivery events, not the authoritative entitlement-use boundary.

### Finding 7 — Plan fulfilment and Entitlements fulfilment need an exactly-once cross-Domain contract

A successful Plan-generation business outcome requires durable agreement between the two owners:

- Plans has exactly one valid immutable Plan Version fulfilling the logical Generation Request;
- Entitlements records the corresponding entitlement-use/access consequence exactly once.

A crash, retry, duplicate event, or partial failure must not produce:

- Plan exists but entitlement can be spent again;
- entitlement consumed but no valid Plan can ever be recovered;
- double entitlement consumption;
- duplicate Plan fulfilment.

The exact transaction/reconciliation mechanism remains future JIT/implementation work.

### Fulfilment-boundary pressure test

This scenario narrows the likely boundary significantly.

**Too early:**

- Request creation;
- Attempt start.

These cannot be irreversible consumption because failed generation must preserve entitlements.

**Too late:**

- notification delivery;
- first participant view.

These are not business-generation authority.

**Candidate business boundary:**

> successful durable fulfilment of one logical Generation Request by one valid immutable Plan Version, coupled to exactly one durable Entitlements fulfilment/access consequence.

This candidate is opened as `HSP-WH-002` rather than silently frozen here.

### Domain ownership

- **Commerce:** commercial/payment/recurring-contract truth.
- **Entitlements:** access/right-to-generate/use truth and entitlement fulfilment/consumption.
- **Safety & Eligibility:** clinical permission.
- **Plans & Nutrition:** Generation Request/Attempt/Plan Version and successful Plan-generation business outcome.

No Domain may reconstruct another owner's authority from copied state.

### Recovery rules

After any crash/retry:

1. reconcile durable Plan Request/Version truth;
2. reconcile the exact Entitlements authority/claim bound to the Request;
3. determine whether the Request is already fulfilled, still authorised, invalidated, or terminal for another reason;
4. never create a second Plan because entitlement finalisation/notification acknowledgement was missed;
5. never consume the entitlement again merely because a worker retries.

### Result

**CHANGES REQUIRED TO WORKING DESIGN + UPSTREAM COMMERCIAL POLICY CLARIFICATION.**

The current model is insufficiently precise about commercial authority.

Two open conclusions are now explicit:

- `HSP-WH-002` — admission, logical entitlement claim and successful entitlement consumption should be separated and linked to the Generation Request;
- `HSP-WH-003` — time-scoped entitlement types require an explicit mid-flight expiry/completion rule from the appropriate Product/Entitlements authority.

No new Domain is justified.



## `HSP-PT-007` — Plan content / recipe / ruleset is superseded or withdrawn during in-flight generation

**Status:** PRESSURE-TESTED  
**Verdict:** CHANGES REQUIRED TO WORKING DESIGN + AUTHORITY CLARIFICATION  
**Upstream contradiction found:** NO  
**Working-design issue found:** YES — current `Generation Basis` wording conflates pre-generation inputs with post-generation selected-result provenance.

### Preconditions

Assume:

- one logical Generation Request is validly `open`;
- Safety and Entitlements authority permit generation;
- a Generation Attempt is in progress;
- deterministic generation depends on an approved plan ruleset plus governed content such as recipes, substitutions, equivalence rules, or other Plan dependencies;
- during execution, a dependency changes lifecycle state.

Two materially different cases are pressure-tested:

1. **ordinary supersession** — a successor version becomes current, but the old version is not withdrawn for safety/legal/material-invalidity reasons;
2. **withdrawal** — the dependency is explicitly withdrawn and may no longer be publicly delivered/used according to current governing authority.

### Existing authority distinction

Current Content governance distinguishes `superseded` from `withdrawn`.

Current Experience authority also states that:

- ordinary corrections create corrected/superseding versions;
- safety, legal/consent, or materially incorrect content uses an expedited withdrawal/correction path;
- withdrawn content stops public delivery while governed internal history remains.

Therefore:

> `superseded` must not be treated as synonymous with `withdrawn`.

### Case A — ordinary supersession

Suppose Recipe R3 v1 is replaced by R3 v2 while an Attempt is running.

If v1 is merely superseded and remains historically valid/non-withdrawn, at least two coherent policies exist:

#### Policy A1 — admitted generation may finish on the captured predecessor dependency

- no new generation starts from v1 after the successor policy boundary;
- the already-admitted Attempt may complete on v1;
- the delivered Plan records exact v1 provenance.

#### Policy A2 — all not-yet-fulfilled generation must migrate to the successor

- the current Attempt cannot commit using v1;
- the old Attempt is abandoned/invalidated;
- generation restarts against the successor dependency set.

Both are technically coherent.

Current authority does not appear to specify the generic plan-generation rule precisely enough.

Therefore `HSP-UPD-002` remains open.

Implementation must not decide that:

`superseded = still deliverable`

or:

`superseded = immediately invalid`

without the correct authority.

### Case B — safety/legal/material withdrawal

Suppose Recipe R3 v1 is withdrawn while the candidate Plan would contain it.

Current authority is materially stronger here:

> withdrawn content stops public delivery.

Therefore the immutable historical generation context does **not** grant a right to deliver the withdrawn dependency.

Expected flow:

1. withdrawal becomes durably effective;
2. the in-flight Attempt may continue internal computation accidentally or due to race, but that does not create delivery authority;
3. immediately before successful Plan fulfilment, current dependency authority is revalidated;
4. if the candidate contains or materially depends upon the withdrawn artifact/ruleset, it cannot be committed/delivered as a valid Plan outcome;
5. the Attempt terminates with a governed dependency/authority-invalidated outcome;
6. under accepted `HSP-WD-011`, a material governed dependency invalidation makes that exact logical Request terminal `invalidated`;
7. no Plan Version is fulfilled from that Request;
8. `HSP-WD-023` preserves/releases the request-bound entitlement authority according to its governed non-fulfilment semantics rather than consuming it;
9. if a valid successor dependency exists and all current Safety/Entitlements authority still passes, a **new** Generation Request and new immutable pre-generation basis may be created;
10. this replacement must not cause double charge, double entitlement consumption, or duplicate Plan delivery.

The replacement Request may potentially be created automatically as recovery policy later, but that is not decided here.

### Why withdrawal is not `unfulfillable`

The withdrawn dependency means the **old Request/basis lost authority**.

That is `invalidated`, not automatically `unfulfillable`.

A subsequent new Request against the current approved dependency set may then prove:

- fulfilable; or
- `unfulfillable` if the current catalogue/capability cannot produce a complete valid Plan.

This preserves the distinction between:

`authority changed`
and
`current capability cannot satisfy a valid basis`.

### Working-model inconsistency discovered

`HSP-WD-008` currently says the immutable Generation Basis is conceptually captured **before deterministic generation begins**.

But `HSP-WD-013` says that same Generation Basis identifies the exact approved content/recipe/substitution/equivalence versions **actually selected**.

If content selection is itself a result of deterministic generation, those statements cannot both literally describe one pre-existing artifact.

The design needs a clearer conceptual separation.

### `HSP-WH-004` — proposed two-layer provenance model

#### A. Immutable Generation Input Basis

Captured before deterministic execution.

Conceptually identifies the exact authoritative inputs and governed dependency context required to execute, such as:

- participant/material plan inputs;
- current Safety authority;
- request-bound Entitlements authority;
- calculation protocol;
- deterministic generation ruleset;
- approved content/catalogue/dependency universe or exact versioned source set available to the generator;
- other material preconditions.

Its purpose is:

> What exact authorised state did this Attempt execute against?

#### B. Immutable Plan Result Provenance Manifest

Finalised only for a successful candidate/Plan.

Conceptually identifies the exact result dependencies actually chosen, such as:

- recipes;
- substitutions;
- equivalence mappings;
- content blocks;
- calculated outputs;
- language/presentation variants;
- exact versions of all result components materially delivered.

Its purpose is:

> What exact governed components make up this delivered Plan Version?

#### Final Plan linkage

A successfully delivered immutable Plan Version should link both:

`Generation Input Basis`
+
`Plan Result Provenance Manifest`

This provides stronger reproducibility without pretending the generator knew its own selected output before execution.

Exact Resource/table/schema representation remains JIT work.

### Revalidation boundary

Before Plan fulfilment, the system must revalidate all material **selected result dependencies** that require current delivery authority.

The rule should be:

> Historical version pinning explains the result; current dependency authority decides whether that result may still be delivered.

This is the content-side analogue of the already accepted Safety/current-authority rule.

### Historical evidence

Even where a dependency is later withdrawn, preserve enough governed internal history to explain:

- which version was available to the Attempt;
- which version was selected by the candidate;
- when it was superseded/withdrawn;
- whether the Attempt was prevented from fulfilment;
- why a replacement Request was created if applicable.

Withdrawal must not rewrite history.

### Delivered Plan is a separate future scenario

This test covers withdrawal **before successful Plan fulfilment**.

It deliberately does not yet settle what happens when a dependency is withdrawn **after a Plan has already been delivered/activated**.

That deserves a separate pressure test because it may require:

- affected-delivery discovery;
- participant warning;
- safety impact assessment;
- correction/replacement Plan;
- continued historical visibility;
- entitlement/safety replacement semantics.

### Result

**CHANGES REQUIRED TO WORKING DESIGN + AUTHORITY CLARIFICATION.**

The current model correctly blocks delivery of withdrawn dependencies, but two refinements are now explicit:

- `HSP-WH-004` — pre-generation input basis and post-generation exact result provenance should be conceptually separated;
- `HSP-UPD-002` — generic in-flight semantics for ordinary supersession must be resolved by the correct governing authority rather than inferred.

No new Domain is justified.



## `HSP-PT-008` — A Plan dependency is withdrawn after the Plan has already been delivered and is active

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH WORKING REFINEMENT + AUTHORITY/JIT CLARIFICATION  
**Upstream contradiction found:** NO

### Core result

Current Product Law already requires governed Plan corrections, replacements and safety withdrawals to preserve history **without consuming a new entitlement**.

Therefore a platform-caused safety/content correction is not ordinary paid re-personalisation.

### Historical Plan remains immutable

The original Plan Version and its Result Provenance remain unchanged.

Withdrawal does not rewrite what was delivered.

Historical visibility may remain, but:

> historical access ≠ current-use authority.

A participant may still see the withdrawn/replaced Plan for history while being clearly told that it is no longer current for use.

### Not every withdrawal is a Safety event

- editorial/material correction may be handled through Content/Plans;
- legal/consent withdrawal follows the governing legal/content authority;
- safety/clinical withdrawal may require a Safety Impact Assessment where participant-specific clinical interpretation is needed.

Safety must not become a generic content workflow.

### `safety_paused` versus `withdrawn`

This scenario raises `HSP-WH-005`.

Working interpretation:

- `safety_paused` = potentially recoverable current-use suspension while Safety authority is unresolved/re-established;
- `withdrawn` = that specific Plan Version itself is no longer valid for current use, though historical visibility may remain.

Exact transition rules remain to be proven against Product/Plan/Safety authority.

### Whole-Plan effect is not automatic

A withdrawn dependency does not always mean the entire Plan must be withdrawn.

The affected-delivery consequence depends on scope:

- replaceable explanatory content;
- one recipe requiring correction;
- safety-critical ruleset defect invalidating the Plan;
- participant-specific risk requiring Safety action.

The governing withdrawal/correction authority must supply enough affected-delivery semantics. This is recorded as `HSP-UPD-003`.

### Replacement lineage

If a corrected Plan is required:

1. preserve the old immutable Plan Version;
2. apply its governed current-use consequence;
3. use current Safety authority where required;
4. generate/author a new immutable replacement Plan Version;
5. preserve correction/replacement provenance;
6. consume no new commercial entitlement under current Product Law;
7. never reopen the old fulfilled Generation Request.

The original request remains historically fulfilled. The later correction is a new governed business event/lineage.

### Failure during replacement

If replacement fails:

- do not silently reactivate the withdrawn/unsafe Plan;
- preserve the participant's correction/replacement right;
- keep current-use handling fail-closed;
- retry/reconcile through the correction pathway.

### Result

**PASS WITH WORKING REFINEMENT + AUTHORITY/JIT CLARIFICATION.**

No new Domain is justified.



## `HSP-PT-009` — A `safety_paused` Plan receives later clearance/restriction/review outcome

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH WORKING REFINEMENT  
**Upstream contradiction found:** NO  
**New Plan Version always required:** NO  
**Automatic same-Version resumption always allowed:** NO

### Preconditions

Assume:

- Plan Version P3 was validly delivered and became `active`;
- approved new high-risk information caused P3 to enter `safety_paused`;
- history remains visible and new adjustments are stopped under current Product Law;
- a Safety Case and/or professional review later produces new current Safety authority.

Current Product Law permits Safety Cases to reach `cleared` or `restricted`, supports scoped/time-bound overrides, and records practitioner outcomes including approval, modification and restrictions.

Therefore “Safety resolved” is not one uniform business result.

### Case A — cleared with no material Plan change required

Assume the new Safety authority explicitly establishes that:

- P3 is permitted for continued current use;
- no new hard constraint changes P3's actual content/composition;
- no calculation input requires recomputation;
- no selected Plan dependency has become withdrawn/non-usable;
- P3 has not already been superseded or withdrawn by another Plan event.

Then creating P4 merely to restate identical Plan content would add version noise without preserving additional business truth.

Working result:

> the same immutable Plan Version P3 may be eligible to transition from `safety_paused` back to `active`.

The Plan Version content is not edited.

Instead, preserve durable evidence of:

- the original pause;
- the adjudication/review basis;
- the new Safety authority;
- the governed resumption event.

### Case B — cleared/restricted but Plan content must change

Assume Safety permits personalised planning only with a new restriction, exclusion, portion/calculation constraint, follow-up condition, or other material Plan requirement that P3 does not already satisfy.

Then P3 must **not** be edited in place.

Expected result:

1. P3 remains immutable;
2. current Safety authority authorises only a Plan satisfying the new constraints;
3. Plans creates a new governed generation/modification/replacement lineage;
4. P4 is a new immutable Plan Version with its own Input Basis and Result Provenance;
5. when P4 becomes the current Plan, P3 receives the appropriate governed successor consequence, commonly `superseded` unless another authority requires `withdrawn`;
6. no ordinary new entitlement is consumed where the change qualifies as a governed safety correction/replacement under current Product Law.

### Case C — review outcome remains restricted / professional action required

If current Safety authority does not permit P3's return to current use:

- P3 must not resume merely because a review completed;
- it may remain `safety_paused` while required governed follow-up/replacement is unresolved;
- or receive another governed lifecycle consequence if the review establishes that the exact Plan itself should no longer be current.

`case resolved`
does not automatically mean
`Plan active`.

### Case D — later Safety authority clears the person, but P3 has independently become non-current

Suppose clinical/Safety review clears continued personalised planning, but meanwhile:

- P3 was withdrawn;
- P4 already superseded it;
- a material content dependency was withdrawn;
- another authoritative Plan input changed.

Safety clearance alone cannot resurrect P3.

Plans must revalidate the exact Plan's own current-use authority.

### Core invariant

The resumption question is:

> Does current Safety authority explicitly permit this exact immutable Plan Version, and does that exact Plan still satisfy every material current-use requirement?

Not:

> Has the Safety Case reached `cleared`?

This prevents Safety Case workflow state from becoming Plan authority.

### No mutation on resumption

If P3 resumes:

- P3's content snapshot does not change;
- P3's historical Generation Input Basis does not change;
- P3's Result Provenance does not change;
- the new Safety authority/resumption evidence is linked as later operational authority/history.

If any material Plan content must change, resumption of P3 is the wrong operation; produce P4.

### Plan versioning rule proven

This scenario gives a sharper rule:

> New Safety evidence does not automatically require a new Plan Version.  
> A material change to Plan content/constraints/result does.

That avoids two bad extremes:

- **always resume** — unsafe when the Plan no longer satisfies current constraints;
- **always regenerate** — unnecessary version churn when the exact Plan remains valid.

### Concurrency pressure

Clearance/resumption must still survive races.

Before P3 returns to `active`, revalidate:

- the exact current Safety authority;
- any current hard restrictions;
- P3's current lifecycle state;
- P3's selected dependency authority;
- whether a successor Plan has already become current.

If authority changes during resumption, fail closed.

### Entitlements

Resuming the same Plan Version after a temporary Safety pause is not a new generation purchase.

Where a new P4 is required solely as a governed safety correction/replacement, current Product Law says that correction/replacement does not consume a new entitlement.

Ordinary participant-requested re-personalisation remains commercially separate.

### Working refinement — `HSP-WH-006`

Proposed rule:

> A `safety_paused` Plan may resume as the same Plan Version only when current Safety authority explicitly permits that exact Plan and no material Plan input, constraint or dependency change requires different Plan content. Any material Plan-content change requires a new immutable Plan Version.

This is a conceptual lifecycle/immutability rule.

Exact transition guards, commands and data representation remain JIT detail.

### Result

**PASS WITH WORKING REFINEMENT.**

The existing model supports both safe resumption and immutable replacement without introducing a new Plan state or Domain.

`HSP-WH-006` should be resolved before a complete Plan state-machine register is frozen.



## `HSP-PT-010` — Late-arriving laboratory/clinical evidence predates an already-delivered Plan

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH WORKING REFINEMENT  
**Upstream contradiction found:** NO  
**Historical Plan rewritten:** NO  
**Historical fulfilled Generation Request reopened:** NO

### Preconditions

Assume:

- participant health intake was completed;
- Safety authorised automated personalisation from the evidence NewYou possessed at the time;
- Generation Request R1 successfully produced immutable Plan Version P3;
- P3 became current/active;
- laboratory result L7 is later received by NewYou;
- L7's specimen/observation/effective time predates R1/P3;
- L7 is still valid for current decision-making under the applicable clinically approved test-specific validity policy;
- L7 is materially safety-relevant.

This scenario is about evidence whose underlying observation predates the Plan but whose authoritative receipt/knowledge by NewYou occurs later.

### Existing upstream authority

Current platform law already establishes that:

- laboratory results remain permanently visible as historical information;
- current use follows a clinically approved test-specific validity policy;
- health-data provenance distinguishes laboratory-verified evidence;
- approved new high-risk information may place an active Plan into `safety_paused`;
- historical Plans remain immutable/reproducible.

These rules are compatible with late-arriving evidence.

### Three different temporal truths

The scenario requires at least three concepts to remain distinct.

#### 1. Clinical/observation/effective time

When the underlying result or health state was observed/applicable.

Example:

`specimen collected: 1 June`

#### 2. NewYou authoritative known/received time

When the evidence entered NewYou's authoritative health-record boundary in a durable form that could legitimately affect platform decisions.

Example:

`lab result received/recorded by NewYou: 15 June`

#### 3. Decision/use time

When Safety or Plans made a specific decision using the evidence available to it.

Example:

`Plan generated: 10 June`

These times can legitimately be ordered:

`observation 1 June`
→ `Plan generation 10 June`
→ `NewYou receives result 15 June`

### Historical truth must preserve both realities

After L7 arrives, it may be true that:

> The participant's underlying clinical state existed before P3 was generated.

And simultaneously:

> NewYou did not possess L7 when it authorised/generated P3.

The system must preserve both.

Therefore:

- P3's historical Generation Input Basis is not rewritten;
- P3's Result Provenance is not rewritten;
- R1 remains historically `fulfilled`;
- the original historical Safety adjudication remains immutable evidence of the decision made from the then-known basis.

A later result does not make the historical record pretend that L7 was known earlier.

### Current Safety authority may change immediately

Late arrival does not mean current operations may ignore the evidence.

Once L7 is durably known to Health Records:

1. Health Records records the result with provenance and temporal evidence;
2. current clinical validity is determined through the approved policy;
3. Safety & Eligibility applies the governed impact policy;
4. where L7 is high-risk/material, a new Safety adjudication / Safety Impact Assessment is performed;
5. old current Safety authority cannot authorise new personalised actions while required reevaluation is outstanding;
6. if current Product/clinical rules require it, P3 enters `safety_paused`;
7. any later continuation or replacement follows `HSP-WD-026`.

### Historical eligibility is not retroactively mutated

The new evidence may show that the participant's real-world state was different from what the platform could establish at T1.

That does **not** justify editing the old eligibility outcome.

Instead:

- old adjudication remains historical;
- new adjudication is linked to the new evidence/basis;
- current authority points to the new adjudication.

If an audit later needs to distinguish:

- evidence genuinely unavailable at T1;
- participant withheld/misreported information;
- evidence was already in NewYou possession but ignored;
- protocol/process defect;

those are different evidentiary situations and must not be collapsed.

This working pack does not assign legal fault/responsibility.

### Critical boundary: genuinely late-arriving vs internally delayed

Two cases must be treated differently.

#### Case A — genuinely late-arriving

L7 was not yet durably received by NewYou before P3 generation.

Then:

- historical P3 remains a truthful record of what was known/used;
- L7 changes current authority only from the point it becomes authoritatively known, subject to its effective time and clinical policy;
- retrospective observation time is preserved but does not rewrite historical system knowledge.

#### Case B — already received, but processing/projection lagged

Suppose L7 was durably received into NewYou's authoritative Health Records boundary on 8 June, but:

- a queue was delayed;
- a projection was stale;
- a worker had not processed it;
- PubSub failed;
- a cache still showed the old state;

and P3 was generated on 10 June as though L7 did not exist.

That is **not** ordinary late arrival.

The platform already possessed authoritative safety-relevant evidence before generation.

Authority must not depend on asynchronous acceleration completing.

Generation must read/revalidate authoritative current state or a safely authoritative derived state that cannot lag past the correctness boundary.

A worker/projection delay cannot redefine:

`known to NewYou`
as
`not yet known`.

### `HSP-WH-007` — proposed authoritative-known-time rule

Proposed rule:

> For safety-relevant evidence, NewYou's authoritative `known/received` time is established when the evidence is durably accepted into the owning authoritative boundary, not when an asynchronous worker, projection, cache, PubSub subscriber or downstream Domain later notices it.

This supports the architecture doctrine:

> authority ≠ acceleration.

It does not prescribe a specific database schema/event architecture.

### If evidence was already possessed but missed

Where Case B occurs, the platform should preserve evidence sufficient to distinguish:

- authoritative receipt time;
- generation decision time;
- stale processing/projection state;
- resulting Safety/Plan consequence;
- reconciliation/correction.

The historical Plan still should not be silently rewritten.

But the incident may require:

- Safety impact assessment;
- governed Plan correction/replacement;
- audit/operational review;
- potentially another authority-level incident classification outside this pack.

### Lab validity is assessed for current use, not historical existence

A lab result can remain historically visible even after it is no longer valid for current decision-making.

Conversely, a late-arriving result with an earlier observation date may still be valid for current decision-making if the approved test-specific policy says so.

The software must not invent a universal age/expiry rule.

### Participant outcome

If L7 materially affects safety:

- participant messaging should explain that newly received clinical information requires a current safety re-check;
- the platform should not imply that the historical Plan originally used L7;
- where current rules require stopping Plan use, messaging must clearly distinguish historical visibility from current safe-use authority.

### Result

**PASS WITH WORKING REFINEMENT.**

The existing temporal-truth, immutable-history, Safety Adjudication, Plan pause/resumption and provenance models survive the scenario.

The new refinement is `HSP-WH-007`:

> authoritative known/received time attaches to durable receipt in the owning authority boundary, not downstream asynchronous processing.

No new Domain is justified.



## `HSP-PT-011` — Participant, practitioner and laboratory evidence materially conflict

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH WORKING REFINEMENT  
**Upstream contradiction found:** NO  
**Universal provenance ranking justified:** NO

### Preconditions

Assume the participant is completing plan onboarding.

For one safety-relevant health concept, the platform has three durable pieces of evidence:

1. participant/member-reported statement:
   - “no known allergy”;
2. practitioner-verified evidence:
   - a current/relevant practitioner record asserts a documented allergy;
3. laboratory-verified evidence:
   - a test/result exists, but the currently approved clinical protocol treats that result as **non-dispositive / insufficient by itself** to resolve whether the practitioner assertion is wrong.

This scenario is deliberately synthetic.

It does **not** assert that any particular real laboratory test proves or excludes food allergy.

The point is to pressure-test conflicting evidence semantics.

### Existing Product authority

Current Product Law already requires distinct health-data provenance classes, including:

- member-reported;
- document-uploaded;
- practitioner-entered;
- practitioner-verified;
- laboratory-verified.

It also requires missing safety-critical information to fail closed into the governed eligibility model.

Those rules do not establish a universal:

`laboratory > practitioner > participant`

truth hierarchy.

### Finding 1 — provenance is not semantic truth

`laboratory_verified`

means the evidence has laboratory provenance/verification.

It does not automatically mean:

> this evidence conclusively resolves every clinical question to which it might be related.

Likewise:

`practitioner_verified`

does not mean:

> this assertion can never later be corrected.

And:

`member_reported`

does not mean:

> it is always wrong when another source differs.

Provenance is one evidence dimension.

It is not universal adjudicative rank.

### Finding 2 — claims must preserve their actual semantics

The participant statement:

> “no known allergy”

must not silently become:

> “allergy definitively absent”.

Those are different claims.

The first describes the participant's current knowledge/report.

The second is a much stronger clinical assertion.

Similarly, an older practitioner note saying:

> “possible allergy”

must not be normalized into:

> “confirmed allergy”

merely to fit a boolean field.

Safety-relevant structured data must preserve the actual semantic claim strongly enough for governed interpretation.

### Finding 3 — one scalar `current value` is insufficient while conflict remains unresolved

If the system stores only:

`allergy = false`

or:

`allergy = true`

then one source assertion necessarily erases or silently defeats another.

That breaks:

- provenance;
- contradiction history;
- temporal truth;
- future audit;
- current Safety interpretation.

During a material unresolved conflict, the platform may need to preserve multiple concurrent source assertions.

This does **not** mean multiple Domains own the health truth.

Health Records remains the owner of the health evidence/fact history.

The conflict itself remains explicit rather than being hidden behind a lossy scalar projection.

### Finding 4 — conflict detection and Safety consequence are separate

Health Records may preserve:

- the assertions;
- their semantic meaning;
- provenance;
- observation/effective time;
- known/received time;
- correction/supersession/contradiction relationships.

Safety & Eligibility owns:

> What does this unresolved conflict mean for current automated personalisation?

Safety must not ask Plans to infer that.

Plans must not inspect raw evidence and decide which source “wins”.

### Finding 5 — unresolved safety conflict fails the positive automation admission test

The accepted automation model requires positive authorisation.

Therefore a material safety-relevant contradiction cannot be treated as:

> no blocker found, therefore automated generation allowed.

Unless the current approved Safety/clinical protocol explicitly resolves the conflict deterministically, automation is not positively authorised.

The exact governed eligibility result may be:

- `insufficient_information`; or
- `professional_review_required`;

depending on the approved protocol and what resolution is required.

This working pack does not invent which outcome applies to every conflict.

### Finding 6 — stronger provenance does not erase historical weaker provenance

If later professional review establishes that the practitioner assertion was erroneous, the participant's earlier statement is not retrospectively deleted.

Likewise, the erroneous practitioner evidence is not deleted as though it never existed.

The platform records:

- original assertions;
- later correction/resolution;
- who/what authorised the resolution;
- effective/known time;
- current usable health fact where one can legitimately be established.

Historical Safety/Plan decisions remain reproducible from the evidence actually available at their decision time.

### Finding 7 — a conservative Safety interpretation does not necessarily resolve the underlying health fact

Safety may be able to say:

> automated personalisation is not permitted while this conflict remains unresolved

without claiming:

> the practitioner assertion is definitely the true clinical fact.

That distinction matters.

Fail-closed Safety routing can occur while Health Records still honestly represents unresolved evidence.

### Finding 8 — professional resolution must return through the owning authority boundary

If professional review later resolves the health fact:

- Professional Care does not directly rewrite Plans;
- the resolved/verified health evidence must enter through the governed Health Records boundary where appropriate;
- Safety then establishes new current Safety authority;
- Plans consumes Safety authority.

This preserves single ownership.

### Existing active-Plan variant

If the same material contradiction is discovered after a Plan is active:

1. Health Records durably records the conflicting evidence;
2. Safety evaluates current impact;
3. where governing rules require immediate protection, current Plan authority is restricted / `safety_paused` as applicable;
4. historical Plan provenance remains immutable;
5. later resolution follows `HSP-WD-026` for same-Version resumption versus replacement.

### `HSP-WH-008` — proposed multi-assertion conflict model

Proposed conceptual rule:

> A safety-relevant health concept must be able to preserve multiple concurrent evidence assertions when they materially conflict. A lossy single scalar “current value” must not erase unresolved evidence.

Each material assertion may need enough conceptual information to preserve:

- semantic claim;
- provenance/source;
- verification state;
- observation/effective time;
- authoritative known/received time;
- applicability/context;
- correction/supersession/contradiction relationship.

Where a current resolved health fact is legitimately established, its resolution authority/provenance must remain traceable to the underlying evidence.

This does **not** require a new Domain or prescribe an Ash Resource/schema.

### Clinical/JIT obligation

Condition-specific conflict-resolution rules may be clinically governed.

Future JIT must not invent generic rules such as:

- newest always wins;
- laboratory always wins;
- practitioner always wins;
- participant negative always clears a prior positive.

Where current clinical authority cannot resolve the conflict deterministically, fail closed through the approved Safety route.

### Result

**PASS WITH WORKING REFINEMENT.**

The existing conflict-aware doctrine survives.

The new refinement is `HSP-WH-008`: explicit preservation of multiple concurrent evidence assertions when a safety-relevant concept remains materially conflicted.

No new Domain is justified.



## `HSP-PT-012` — Practitioner retracts/corrects an earlier practitioner-verified assertion after Safety decisions and Plans relied on it

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH WORKING REFINEMENT  
**Upstream contradiction found:** NO  
**Historical evidence deleted:** NO  
**Historical Safety/Plan decisions rewritten:** NO

### Preconditions

Assume:

- at T1, a practitioner-verified health assertion A1 is durably accepted into Health Records;
- A1 is safety-relevant and materially affects Safety;
- Safety adjudications at T2 and T4 legitimately rely on A1;
- immutable Plan Versions P1 and P2 are generated/delivered from those then-current authorities;
- at T5, the same practitioner or another authorised professional submits a governed correction/retraction stating that A1 was **incorrect when originally entered**.

This scenario deliberately distinguishes a source correction from a later change in the participant's underlying health state.

### Existing authority supports preservation rather than silent overwrite

Current Domain Law requires source/provenance not to be lost when health facts matter to Safety and places participant/professional correction behind immutable/professional-record boundaries.

Current Architecture Law also treats governed published/activated evidence as immutable history and uses explicit correction/supersession/withdrawal rather than silent mutation.

That direction is compatible with this scenario.

### Finding 1 — source retraction is not the same event as participant state change

Two events that may produce the same present-day answer can have very different histories.

#### Correction/retraction

> “A1 was wrong when entered.”

Meaning:

- the source now says the earlier assertion should not have represented the participant's clinical state at T1;
- the correction changes how A1 should be interpreted as evidence now;
- it does **not** mean the participant's health changed at T5.

#### Genuine later state change

> “A1 was true at T1, but the participant's condition changed later.”

Meaning:

- A1 remains a valid historical assertion about T1;
- a new health observation describes a later state.

Those events must not be collapsed into one generic edit.

### Finding 2 — do not delete or mutate A1

A1 remains necessary historical evidence because it answers:

> What evidence did NewYou actually possess and rely on at T2/T4?

The correction/retraction must therefore create explicit new evidence/history linked to A1.

Conceptually preserve:

- original assertion A1;
- original provenance/verification;
- A1's authoritative known time;
- correction/retraction C1;
- who/what authorised C1;
- C1's known time;
- whether C1 says “wrong when made” versus “later state changed”;
- the resulting current evidence/fact resolution.

Exact statuses/fields remain JIT detail.

### Finding 3 — the retraction can change current evidence usability without rewriting past reliance

After C1 is authoritatively accepted:

- A1 must no longer silently continue to act as current usable evidence if C1 validly retracts it;
- current Health/Safety views must incorporate the correction;
- new Safety adjudication uses the corrected evidence state.

But historical Safety Evaluation E1 can still truthfully say:

> E1 relied on A1 because A1 was the then-current practitioner-verified evidence known to the platform.

That is not the same as claiming:

> A1 was ultimately clinically correct.

### Finding 4 — “wrong when made” creates a two-time evidence problem

The scenario exposes a useful distinction between:

- **claim effective truth** — what the corrected record now says about the participant at T1;
- **evidence operational availability/usability** — what NewYou reasonably had available and treated as usable at T2 before the retraction became known.

After C1, the platform may know:

> A1 should not represent the participant's real historical clinical state.

Yet it must also preserve:

> A1 was the evidence actually used by Safety/Plans before C1 existed in NewYou.

Both are required for honest reconstruction.

### Finding 5 — historical Plan Versions remain immutable

P1/P2 are not regenerated in place or rewritten to pretend A1 was never used.

Their Generation Input Basis remains what it was.

Their Plan Result Provenance remains what it was.

If the corrected evidence changes current Plan safety or correctness:

1. Health Records records C1;
2. Safety performs the governed current impact/adjudication;
3. active Plan consequence is applied as required;
4. a correction/replacement Plan Version is generated/authored where necessary;
5. historical versions remain visible according to governing access rules.

### Finding 6 — current Plan action depends on impact, not embarrassment about the old evidence

The platform must not automatically withdraw every historical Plan merely because an upstream assertion was retracted.

The governing question is:

> Does the correction materially change current safe-use authority or require different Plan content?

Possible outcomes include:

- no current Plan change;
- Safety reevaluation only;
- `safety_paused`;
- same-Version resumption under `HSP-WD-026`;
- governed correction/replacement;
- another explicitly governed consequence.

The exact result depends on current Safety/Plan authority.

### Finding 7 — correction/replacement is not ordinary paid re-personalisation

Where P1/P2 require a governed correction/replacement because the platform's prior authoritative evidence is later corrected/retracted, the replacement is conceptually a correction/safety replacement—not a participant preference change.

Current Product Law already says governed Plan corrections/replacements/safety withdrawals do not consume a new entitlement.

Entitlements remains the owner of the resulting access/right truth.

### Finding 8 — downstream derived records need lineage, not retroactive deletion

Derived objects may include:

- Safety adjudications;
- Safety Cases;
- Plan Generation Input Bases;
- Plan Versions;
- audit/evidence records.

They should retain links showing:

> relied on A1 as known at decision time

and, where useful:

> A1 later corrected/retracted by C1.

They must not be rewritten to remove A1 from historical provenance.

### Finding 9 — correction authority matters

Not every later assertion can retract practitioner-verified evidence.

A participant disagreement may create conflict under `HSP-WD-028`, but it does not automatically rewrite professional evidence.

Likewise, a practitioner correction must enter through the governed professional/Health Records boundary and retain attribution/audit.

The exact authority rules for who may retract which professional record belong to JIT/professional-record governance.

### `HSP-WH-009` — proposed evidence-correction semantic rule

Proposed rule:

> Evidence correction/retraction must explicitly distinguish “earlier assertion was wrong when made” from “earlier assertion was valid then but the participant state later changed.”

Further:

> Historical decisions retain the exact evidence assertion/status they actually relied on, while current evidence usability changes from the correction/retraction's authoritative known time onward.

This does not mean the false assertion remains current.

It means the system preserves both:

- corrected understanding of the participant's real-world history;
- truthful evidence of what NewYou knew/used before the correction arrived.

### Result

**PASS WITH WORKING REFINEMENT.**

The existing correction, temporal truth, provenance, conflict and immutable-decision models survive.

The new refinement is `HSP-WH-009`, which makes evidence correction semantics explicit enough to prevent correction from being confused with a later state change.

No new Domain is justified.



## `HSP-PT-013` — Professional clearance/override exists, then material health state changes

**Status:** PRESSURE-TESTED  
**Verdict:** PASS  
**Upstream contradiction found:** NO  
**New working doctrine required:** NO — existing accepted rules are sufficient.

### Preconditions

Assume:

- participant initially routes to professional review;
- an authorised practitioner reviews a defined health/evidence basis B1;
- Professional Care records a governed outcome;
- Safety & Eligibility converts that outcome into scoped current Safety authority A1;
- A1 may be:
  - ordinary professional clearance/restriction; or
  - an exceptional clinical override where Product Law permits it;
- a Plan is generated/active under A1;
- later, Health Records receives a new material health fact H2.

The scenario tests whether A1 remains usable.

### Existing Product authority

Current Product Law already requires a clinical override to be:

- scoped;
- time-bound;
- audited;
- preserved separately from the original automated outcome.

It also requires high-risk downgrades to use authorised clinical approval/protocol and supports structured practitioner outcomes including approval, modification, restrictions and follow-up.

Those rules are compatible with change-sensitive professional authority.

### Existing working doctrine already covers the required basis binding

`HSP-WD-022` already requires practitioner-derived authority to be scoped by:

- purpose/pathway;
- evidence;
- conditions;
- time;

and states that material health changes can invalidate/reassess professional authority.

`HSP-WD-020` separately requires impact-sensitive Safety reevaluation rather than universal invalidation.

Therefore no new concept is required.

### Case A — new fact is irrelevant to the clearance scope

Suppose H2 is genuinely unrelated to:

- the reviewed risk;
- the evidence relied upon;
- conditions of clearance;
- pathway;
- Plan safety constraints;
- time/validity conditions.

Then A1 does not need to be destroyed merely because “something changed”.

Safety may determine:

> no impact on this professional authority.

This avoids unnecessary professional-review churn.

### Case B — new fact materially touches the reviewed basis/scope

Suppose H2 changes a fact that was material to the practitioner's judgement or to a condition/restriction supporting A1.

Then A1 cannot silently continue authorising new personalised actions as if B1 were still current.

Expected flow:

1. Health Records durably records H2;
2. Safety applies the approved change-impact policy;
3. A1 becomes non-usable for the affected purpose while reevaluation is required;
4. a Safety Impact Assessment and/or new professional review is initiated as governed;
5. new generation/adjustment cannot rely on stale A1;
6. any in-flight Generation Request revalidates current Safety authority before fulfilment and fails closed if A1 is no longer applicable;
7. active Plan consequence is determined separately under current Safety policy;
8. later clearance/override creates new current authority A2 rather than mutating A1.

### Case C — exceptional override

An exceptional clinical override is not a permanent “force allow”.

Its scoped/time-bound nature makes the change-sensitive rule even stronger.

A later material basis change does not inherit the old override merely because:

- the same participant is involved;
- the same practitioner issued it;
- the old override has not yet reached its wall-clock expiry.

If the new fact is material to its scope/conditions, the override's current applicability ends or requires explicit reevaluation under governed policy.

### Case D — health change occurs during generation

Assume Request R1 captured A1 and generation is in progress.

H2 arrives before Plan fulfilment and materially invalidates A1.

Then:

- historical Generation Input Basis still records A1;
- candidate computation may exist internally;
- current-authority revalidation prevents stale fulfilment;
- the Attempt terminates with the appropriate authority-invalidated outcome;
- R1 follows the existing invalidation rules;
- no Plan is delivered under obsolete professional authority;
- entitlement handling follows `HSP-WD-023`.

### Case E — health change occurs after Plan activation

Assume Plan P3 is active under A1.

H2 materially affects current Safety authority.

Then:

1. historical P3 remains immutable;
2. Safety determines current active-Plan impact;
3. P3 may enter `safety_paused` where governing rules require;
4. later professional/Safety authority A2 determines whether:
   - exact P3 can resume under `HSP-WD-026`; or
   - a new immutable successor Plan is required.

The old professional authority does not get rewritten.

### Clearance history remains evidence

Even after A1 becomes stale/non-applicable, preserve:

- practitioner identity/authority;
- review basis B1;
- structured outcome;
- restrictions/conditions;
- scope;
- effective/expiry timing;
- later invalidating/change event where applicable.

This distinguishes:

> valid professional decision on the evidence then

from:

> current authority now.

### Professional Care remains outside the direct Plans safety gateway

The scenario confirms `HSP-WD-022`.

Professional Care may:

- review;
- author;
- modify;
- recommend;
- clear/restrict within its governed role.

But current personalised Plan safety authority still reaches Plans through Safety & Eligibility.

A practitioner outcome does not become a second evergreen direct Safety channel into Plans.

### No universal invalidation rule

The correct rule is:

> material change to the professional authority's reviewed basis/scope/conditions requires reevaluation.

Not:

> any health edit invalidates all professional authority.

And not:

> professional clearance survives until its date expires regardless of changed facts.

This is exactly the impact-sensitive approach already accepted in `HSP-WD-020` and `HSP-WD-022`.

### Concurrency/recovery

If H2 and professional clearance/re-clearance race:

- current Safety authority must be derived from durable ordered/known evidence and governed applicability;
- stale professional authority cannot win merely because its command/event is processed later;
- authoritative consumers re-read/revalidate current Safety state;
- retries must converge on the same current authority outcome.

The exact transaction/event mechanism remains JIT detail.

### Result

**PASS.**

No new Domain, Resource, lifecycle state or working hypothesis is required.

The scenario validates:

- `HSP-WD-020` — impact-sensitive Safety reevaluation;
- `HSP-WD-022` — Professional Care uses the Safety gateway and professional authority is scoped/basis-sensitive;
- `HSP-WD-025` — Safety pause differs from withdrawal;
- `HSP-WD-026` — exact-Plan revalidation before resumption;
- `HSP-WD-027` — authoritative known time is not async processing time.

The important conclusion is:

> Professional authority is durable historical evidence, but its **current applicability is contingent on the scope, conditions and material evidence basis it actually reviewed**.



## `HSP-PT-014` — Participant requests full deletion after Health evidence, Safety adjudications and Plans exist

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH WORKING CORRECTION + PRIVACY/JIT DELETION-CONTRACT OBLIGATION  
**Upstream contradiction found:** NO  
**Blanket indefinite retention justified:** NO  
**Completed deletion reconstructable from retained commercial/audit evidence:** NO

### Preconditions

Assume:

- the participant has an Account;
- Health Records contains structured self-guided health evidence and possibly uploaded/laboratory assets;
- Safety & Eligibility contains historical adjudications and possibly Safety Cases;
- Plans & Nutrition contains one or more immutable delivered Plan Versions with Generation Input Basis and Plan Result Provenance;
- the participant may also have Commerce/Entitlements history;
- optionally, formal Professional Care records may exist;
- the participant requests **full deletion**, not ordinary recoverable account closure.

This scenario tests the interaction between:

- immutable/reproducible business evidence;
- privacy/deletion rights;
- professional/legal retention;
- Plan access/entitlements;
- audit;
- backup/restore and derived copies.

### Existing Product authority is explicit

Current Product Law already establishes that:

- recoverable account closure and irreversible full deletion are separate;
- full deletion has a 14-day cancellation window before execution;
- completed deletion has no account-recovery or reconstruction path;
- assessment immutability applies **while records exist**, not as indefinite identifiable retention;
- full deletion permanently ends participant access to reports, Plans, programmes, progress and entitlements;
- self-guided health/check-in data is deleted or irreversibly anonymised where eligible;
- formal professional records may be retained only under approved professional retention obligations;
- private journal/file derivatives and other copies receive category-specific deletion treatment;
- retained financial/dispute evidence is restricted and cannot reconstruct product access;
- audit retention is minimised and must not copy full sensitive payloads.

Therefore this pressure test must not invent an “immutable forever” exception.

### Finding 1 — business immutability and data retention are different dimensions

The existing pack repeatedly uses terms such as:

- immutable Health evidence/history;
- immutable Safety adjudication;
- immutable Generation Input Basis;
- immutable Plan Version;
- immutable Plan Result Provenance.

Those statements protect against **silent mutation while the record is governed and retained**.

They do not create an independent indefinite-retention authority.

The correct conceptual relationship is:

> **immutability answers whether retained evidence may be silently rewritten; privacy/data-lifecycle authority answers whether that evidence may continue to exist in identifiable form.**

Current Architecture Law already states that business lifecycle and data lifecycle are separate dimensions.

### Finding 2 — full deletion terminates product authority, not merely UI visibility

The full-deletion flow is not:

`hide account from UI`
→ keep all product truth indefinitely.

Once the governed deletion process reaches completion:

- participant product access is ended;
- Plans/entitlements are not recoverable through retained payment history;
- deleted/anonymised health evidence cannot continue driving personalisation;
- caches, search/index state and derived signals must be invalidated;
- retained records cannot silently restore current Account, Safety or Plan authority.

A later registration is a new identity relationship under current Product Law.

### Finding 3 — the 14-day cancellation period is not normal continued use

During the full-deletion process, current Product Law revokes normal access and stops optional processing before category-specific destruction/anonymisation completes.

Therefore the deletion cancellation window must not be treated as:

> “the Account and personalised health/Plan lifecycle continue normally for fourteen days.”

At minimum, new personalised generation/adjustment must not be inferred to remain authorised merely because physical deletion has not finished.

Exact product behaviour during the cancellation window belongs to the governed Privacy/IAM/domain deletion contracts.

### Finding 4 — self-guided Health evidence can be deleted/anonymised despite earlier Safety/Plan reliance

Suppose Health assertion H1 was legitimately used by:

- Safety Evaluation E1;
- Generation Request R1;
- Plan P1.

On completed full deletion, eligible self-guided Health evidence may be deleted or irreversibly anonymised according to Product Law.

The platform must **not** keep H1 identifiable forever solely because E1/P1 once depended on it.

That would silently let Plans/Safety override Privacy authority.

### Finding 5 — downstream copies cannot become a deletion loophole

This is especially important for the accepted Generation Input Basis / Result Provenance model.

If Plans copied more sensitive Health data than it actually needed, deleting Health Records while leaving a full clinical snapshot inside Plans would make the deletion boundary meaningless.

Therefore existing minimum-necessary doctrine becomes stronger under this pressure test:

> A consuming Domain must not retain copied sensitive payloads merely to make its own provenance easier.

Where reproducibility can be satisfied through:

- governed reference;
- derived Safety constraint;
- minimised fact;
- protocol/version reference;
- category-appropriate retained evidence,

prefer that over duplicating full clinical records.

Exact persistence design remains JIT work.

### Finding 6 — Safety adjudication immutability also does not automatically imply indefinite identifiable retention

A historical Safety adjudication may be immutable while retained.

But after full deletion, its exact treatment must follow the category-specific Privacy & Consent deletion contract and any legitimate professional/legal retention authority.

Potential governed treatments may include:

- deletion;
- irreversible anonymisation/de-linking;
- restricted retained-obligation evidence;
- retention as part of a formal professional record where authorised.

This working pack must not choose the category mapping itself.

That mapping is recorded as `HSP-UPD-004`.

### Finding 7 — Plan access ends even where “permanent access” existed

Earlier Product Law may describe purchased assessment/Plan access as permanent.

GQ-010 explicitly qualifies that promise:

> purchased/permanent access lasts while the Account relationship exists and does not override completed full deletion.

Therefore:

- Plan P1 may have been legitimately sold with permanent access;
- completed full deletion still ends access;
- Commerce/financial retention cannot recreate P1 access later;
- a returning person creates a new Account/identity relationship.

This is not a commercial contradiction.

### Finding 8 — exact Plan payload retention after full deletion is not fully specified in this working pack

Product Law clearly settles **access** and the general category-aware deletion model.

It does not justify this pack declaring one universal rule such as:

- “all Plan Versions must always be retained identifiable”; or
- “all Plan Versions must always be physically destroyed immediately.”

The exact treatment may differ among:

- self-guided Plan Version payload;
- Generation Input Basis;
- Plan Result Provenance;
- practitioner-authored/modified Plan that forms part of professional records;
- minimised audit evidence;
- non-identifiable aggregate evidence.

Therefore future Privacy & Consent / Plans / Safety / Professional Care JIT work needs explicit deletion contracts.

This is `HSP-UPD-004`.

### Finding 9 — professional records are a separate retention category

A formal practitioner record may have retention obligations that outlive the consumer Account relationship.

Where that applies:

- the retained professional record is restricted;
- it does not remain ordinary product data;
- it cannot restore Account access, Entitlements or personalisation;
- correction uses the governing professional record process;
- deletion occurs when the approved obligation ends.

This does not permit copying all self-guided Health/Plan data into Professional Care merely to evade deletion.

### Finding 10 — audit evidence must be minimised

Audit immutability does not justify duplicating:

- full Health questionnaire;
- full laboratory documents;
- full Plan snapshot;
- full practitioner notes

into an “audit log” and retaining them forever.

Current Product Law explicitly requires minimised, category-specific audit retention without full sensitive payload copying.

Therefore audit should prove relevant events/authority without becoming a shadow clinical database.

Exact identifiers/hashes/metadata are implementation detail and are not designed here.

### Finding 11 — deletion must be representation-complete and non-resurrecting

A compliant deletion outcome cannot leave personal data effectively active in:

- search indexes;
- caches;
- projections;
- file derivatives;
- temporary processing artefacts;
- embeddings/summaries where applicable;
- external processors;
- restored backups that reintroduce deleted state.

Current Architecture Law requires representation-complete, non-resurrecting deletion.

Therefore:

> backup restore must not become a path that silently resurrects Health/Safety/Plan authority after completed deletion.

The exact restore/deletion replay mechanism is downstream engineering detail.

### Finding 12 — historical truth does not require perpetual participant-identifiable history

This scenario refines several earlier statements such as:

> “historical Plan remains immutable evidence.”

The more precise formulation is:

> **while a historical record is retained under governing data-lifecycle authority, it remains immutable and reproducible according to its contract.**

If full deletion law later requires deletion or irreversible anonymisation:

- the participant-identifiable historical artifact may cease to exist;
- retained minimised/anonymised evidence must not be used to reconstruct the deleted Account/product relationship.

This is not rewriting history.

It is the data lifecycle reaching a governed terminal consequence.

### `HSP-WH-010` — proposed immutability-versus-retention rule

Proposed rule:

> Immutability and retention are orthogonal.

More precisely:

> Health/Safety/Plan evidence is protected from silent mutation while retained, but Privacy & Consent and category-specific retention law determine whether it may continue to exist in identifiable form.

Further:

> Any retained professional, financial, security or audit evidence must be purpose-restricted and minimum-necessary and must not reconstruct deleted product access, Entitlements, Safety authority or personalised Plan use.

### JIT proof obligations

Future Privacy/deletion JIT and implementation proof should demonstrate that completed full deletion:

- invokes deletion contracts across every owning Domain;
- deletes/anonymises/restricts each category according to current authority;
- removes copied/derived/index/cache/file representations;
- does not let retained audit/commercial/professional evidence restore product authority;
- survives retries and partial failures;
- exposes incomplete deletion work;
- remains non-resurrecting after backup restore;
- preserves only the minimum retained evidence actually authorised.

This does not prescribe the queue, transaction, tombstone, backup or storage implementation.

### Result

**PASS WITH WORKING CORRECTION + PRIVACY/JIT DELETION-CONTRACT OBLIGATION.**

The architecture survives, but the working pack must stop using “immutable historical evidence” as shorthand for “retain forever”.

`HSP-WH-010` captures that correction.

`HSP-UPD-004` records the exact category-specific deletion treatment still required for Plan/Safety/professional variants.

No new Domain is justified.



## `HSP-PT-015` — Safety authorises automation, but mandatory hard constraints make the approved Plan catalogue impossible

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH UPSTREAM COMMERCIAL POLICY DELTA  
**Upstream contradiction found:** NO  
**New architecture doctrine required:** NO  
**Safety outcome changed by catalogue failure:** NO

### Preconditions

Assume:

- the participant has completed all required Health/Safety information;
- current Safety authority is `eligible_automated`;
- Entitlements validly authorises one Plan-generation Request;
- all relevant hard constraints are current and authoritative;
- one or more hard constraints may arise from medical/Safety exclusions, clinically governed restrictions, participant-declared mandatory religious exclusions, participant-declared mandatory ethical exclusions, or another explicitly authorised non-negotiable category;
- the current approved deterministic Plan rules/content/substitution catalogue cannot produce any complete Plan satisfying all hard constraints.

This is:

> valid Safety authority + valid Plan request + valid hard constraints + insufficient current approved Plans capability.

### Existing upstream authority supports the separation

Current Product Law requires food exclusions to preserve distinct medical, intolerance, religious, ethical, dislike and preference classifications.

Current Product Law also requires the Plan engine to be deterministic and built from approved calculations, templates, substitutions and content.

Therefore the Plan engine is not authorised to improvise outside approved capability merely to force a result.

### Finding 1 — `eligible_automated` is not “Plan guaranteed”

Safety answers whether automated personalisation is clinically/permissibly allowed under current evidence and protocol.

Plans answers whether approved deterministic capability can produce a complete valid Plan for the exact authorised basis.

Those are different truths.

Therefore:

`eligible_automated`
+
`no valid catalogue solution`

must not become `professional_review_required` merely because Plans lacks content.

### Finding 2 — Plans must not relax hard constraints

If no complete Plan exists, Plans must not create one by dropping an allergy exclusion, weakening a clinical restriction, substituting outside the approved catalogue, treating mandatory religious/ethical exclusions as preferences, silently changing pathway, or inventing unapproved content.

The correct result is no Plan.

### Finding 3 — constraint ownership still matters

A Safety/clinical hard restriction cannot be waived in Plans and requires the correct Health/Safety/professional authority to change.

A participant-owned mandatory religious/ethical declaration also cannot be silently weakened, but the participant may deliberately revise her own declaration through the owning governed boundary.

Any material basis change requires new validation and a new logical Request rather than mutation of the old failed basis.

### Finding 4 — soft preferences may degrade; hard constraints may not

Approved fallback behaviour may optimise around soft preferences.

If a hard constraint cannot be satisfied:

> no valid Plan exists.

### Finding 5 — Request lifecycle is `unfulfillable`

The Request was validly authorised, current authority is not stale, Safety remains valid, and approved capability cannot produce a complete valid Plan.

Therefore:

> Request → `unfulfillable`

rather than `invalidated`, `cancelled`, `fulfilled`, or a fabricated Safety outcome.

### Finding 6 — do not retry unchanged impossibility forever

An Attempt may discover the capability gap, but the business reason is not a technical crash.

Retries against the same unchanged capability/basis must not spin indefinitely.

A later attempt is justified only after a material change such as approved catalogue expansion, authorised constraint change, or governed pathway/goal change, followed by new validation/new Request lineage.

### Finding 7 — professional review is not generic catalogue repair

The platform must not send every `unfulfillable` automated Plan to a practitioner solely because the algorithm lacks recipes/content.

Professional review is appropriate only when Product/Safety/professional policy requires actual human judgement.

### Finding 8 — General Wellness is not a silent fallback

Plans must not silently replace the intended personalised pathway with General Wellness because the personalised catalogue is incomplete.

Any alternate-pathway offer must be explicit and governed.

### Finding 9 — entitlement is not consumed by non-fulfilment

No valid immutable Plan Version was produced.

Under fail-closed generation law and `HSP-WD-023`, a one-use entitlement is not finalised as consumed merely because computation occurred.

At minimum, the entitlement remains preserved/recoverable under its governing semantics.

### Finding 10 — preserved entitlement does not fully answer the customer-remedy question

If the participant paid specifically for a Plan and current approved capability cannot produce it, “your entitlement remains unused” may be commercially inadequate when the gap is indefinite.

Possible governed remedies could include refund, credit, alternate accepted product/pathway, future-use entitlement, or participant choice.

This pack must not choose that commercial remedy.

No specific governed rule for this exact paid-`unfulfillable` case was found in the current Product Law search.

Therefore this is recorded as `HSP-UPD-005`.

### Finding 11 — UX must not pressure unsafe waiver

Where the blocker is Safety-owned, the UI must not encourage removal of the restriction just to obtain a Plan.

Where the blocker is participant-owned religious/ethical choice, the UI may truthfully explain the catalogue limitation and allow the participant to revisit her own declaration if she independently chooses.

### Finding 12 — capability telemetry is evidence, not authority

Repeated `unfulfillable` outcomes can inform Content/Plans product expansion and Analytics.

They do not authorise weakening constraints or publishing unapproved content.

### Result

**PASS WITH UPSTREAM COMMERCIAL POLICY DELTA.**

The existing architecture survives without new Domain, Resource, lifecycle state or working hypothesis.

The scenario validates `HSP-WD-006`, `HSP-WD-011`, `HSP-WD-015`, `HSP-WD-016` and `HSP-WD-023`.

The only new unresolved item is commercial:

`HSP-UPD-005`
→ define the customer remedy when a paid Plan cannot currently be fulfilled.



## `HSP-PT-016` — Practitioner authors/modifies a Plan that conflicts with current Safety hard constraints

**Status:** PRESSURE-TESTED  
**Verdict:** PASS  
**Upstream contradiction found:** NO  
**New working doctrine required:** NO  
**Professional Care becomes a second Safety authority:** NO

### Preconditions

Assume:

- a participant has current Health evidence;
- Safety & Eligibility has established current Safety authority including one or more hard Plan constraints;
- a practitioner is acting through a governed Professional Care relationship;
- the practitioner authors or materially modifies a proposed personalised Plan;
- the proposed Plan content conflicts with one current Safety hard constraint.

Examples are deliberately conceptual:

- a prohibited ingredient is included;
- a clinically governed restriction is not respected;
- a required exclusion/limit is exceeded;
- the practitioner intends a different clinical treatment of the risk than current Safety authority presently permits.

The scenario does **not** decide whether the practitioner's clinical judgement is correct.

It tests authority routing.

### Existing Domain Law already separates the two professional consequences

Current Domain Law requires:

`Professional Care`
→ `Safety & Eligibility`
for governed clearance/restriction outcomes

and separately:

`Professional Care`
→ `Plans & Nutrition`
for practitioner-authored Plan changes, with the resulting Plan version owned by Plans.

That means:

> professional clinical authority and practitioner-authored Plan content are related but not the same write.

### Existing Product Law supports practitioner-authored plans without creating bypass authority

Current Product Law recognises structured practitioner outcomes including:

- approval;
- modification;
- practitioner-authored plans;
- restrictions;
- follow-up;
- decline;
- referral.

It separately governs clinical overrides as explicit, scoped, time-bound and audited authority.

Therefore:

> a practitioner-authored Plan does not itself constitute an implicit clinical override.

### Case A — practitioner-authored Plan is already consistent with current Safety authority

Suppose the practitioner produces P4 and every material Safety constraint is satisfied.

Expected result:

1. Professional Care preserves the practitioner review/decision record;
2. the practitioner-authored change enters Plans through the Plans owner;
3. Plans creates the governed new immutable Plan Version;
4. practitioner-authored/practitioner-modified provenance is explicit;
5. activation still uses the normal Plan lifecycle/current-authority guards;
6. Safety remains the authoritative current Safety input.

No extra override is required merely because a human authored the Plan.

### Case B — practitioner Plan conflicts with current Safety authority and no override exists

Suppose P4 violates current Safety constraint S1.

Then P4 cannot become the current usable Plan merely because the author is a qualified practitioner.

The platform must not allow:

`practitioner saves Plan`
→ `Safety constraint silently bypassed`

Expected result:

- the practitioner-authored proposal/change may be preserved as review/professional evidence where governed;
- it cannot cross the Plan approval/activation boundary as a current authorised Plan while S1 remains current;
- Plans must reject/block current use of the conflicting Plan under its current Safety-authority guard;
- existing current Plan handling remains governed separately.

This is a fail-closed authority conflict, not a software validation nuisance.

### Case C — practitioner intends to clinically override or replace S1

The practitioner cannot embed the override semantics only inside Plan content.

Instead:

1. Professional Care records the governed professional outcome/justification;
2. if the action qualifies as a clinical override, the override follows current Product Law:
   - explicit;
   - scoped;
   - time-bound;
   - audited;
   - subject to any required second approval/protocol;
3. Professional Care requests the appropriate governed change through Safety & Eligibility;
4. Safety establishes new current Safety authority S2;
5. only after S2 permits the relevant Plan content may Plans accept/activate the practitioner-authored Plan against S2.

Conceptually:

`professional judgement`
→ `governed Safety authority`
→ `practitioner-authored Plan`
→ `Plans validation/current Plan`

Not:

`professional Plan content`
→ `implicit Safety override`.

### Case D — practitioner is authorised to review but not authorised for the relevant override

Role/care relationship alone does not imply authority for every clinical downgrade/override.

If current Product/protocol rules require:

- another authorised reviewer;
- a second clinical approval;
- an approved single-practitioner protocol;
- a particular professional scope;

then the Plan remains non-current until those requirements are satisfied.

There must be no generic administrator/practitioner “force save as active” path.

### Case E — Safety changes after practitioner submission but before activation

Assume:

1. practitioner authors P4 under current Safety authority S1;
2. P4 is submitted for review/approval;
3. new Health evidence arrives;
4. Safety establishes S2 or requires reevaluation;
5. P4 reaches the activation boundary later.

P4 must be revalidated against current Safety authority.

Product Law already permits immediate/near-term Plan activation only with revalidation where information/timing has become stale.

Therefore a Plan that was valid when authored may still fail activation if current Safety authority has changed.

Historical professional authorship/provenance remains intact.

### Case F — Safety changes after practitioner-authored Plan is already active

If P4 is already active and new Safety authority materially changes:

- P4 remains immutable historical Plan evidence while retained;
- current Plan consequence follows the same Safety Impact Assessment/pause rules as an automated Plan;
- practitioner authorship does not immunise P4 from later Safety reevaluation;
- later continuation follows `HSP-WD-026`:
  - same-Version resumption only if exact P4 remains valid;
  - otherwise a new immutable successor is required.

### Plan ownership remains Plans & Nutrition

Professional Care owns:

- professional relationship;
- review record;
- practitioner judgement/outcome;
- authorship/modification evidence.

Safety & Eligibility owns:

- current Safety authority;
- restrictions;
- clearance;
- governed override effect.

Plans & Nutrition owns:

- Plan Version;
- Plan lifecycle;
- current Plan selection/activation consequence;
- Plan provenance linkage.

No shared-write ownership is needed.

### Practitioner provenance must not masquerade as automation

A practitioner-authored or materially practitioner-modified Plan must remain distinguishable from:

- deterministic automated generation;
- professionally cleared automated generation.

The platform must preserve enough evidence to explain:

- who authored/modified;
- what Safety authority/restrictions applied;
- relevant review context;
- exact Plan content/result provenance;
- later approval/activation lineage.

Human clinical judgement is not falsely represented as deterministic engine output.

### The current Plan lifecycle is sufficient

Current Product Law already includes:

- `pending`;
- `generated`;
- `review`;
- `approval`;
- `scheduled`;
- `active`;
- `safety-paused`;
- terminal/successor states.

This scenario does not justify another Plan state.

Exact mapping of a practitioner draft/change proposal into those states remains JIT detail.

The key invariant is independent of that representation:

> conflicting practitioner-authored content must not become current until current Safety authority actually permits it.

### No duplicate Safety interpretation inside Plans

Plans may validate that required Safety constraints are satisfied.

Plans must not independently decide:

> the practitioner probably knows better, so ignore S1.

Nor should Plans parse professional free text and manufacture a new Safety override.

Clinical authority changes through Safety & Eligibility.

### Concurrency and retries

If practitioner authoring, Safety change and Plan activation race:

- current authoritative Health/Safety state wins over stale UI/session state;
- activation revalidates current Safety authority;
- retries must converge on the same allowed/blocked Plan outcome;
- duplicate saves/submissions must not create multiple current Plan Versions;
- stale practitioner Plan content must not become active simply because its command is processed last.

Exact transaction/idempotency mechanism remains JIT work.

### Entitlements

A practitioner-authored replacement/change must use the governing entitlement/service semantics for that professional pathway.

This scenario does not invent whether a particular practitioner service consumes:

- a professional-review entitlement;
- an existing correction/replacement right;
- another paid service entitlement.

But Plans must not infer commercial authority from practitioner identity.

Commerce/Entitlements remain separate.

### Result

**PASS.**

The existing architecture already resolves the authority seam.

The scenario validates:

- `HSP-WD-022` — Professional Care uses one Safety gateway into Plans;
- `HSP-WD-015` — hard constraints cannot be silently weakened;
- `HSP-WD-020` — material health/Safety changes are impact-sensitive;
- `HSP-WD-025` / `HSP-WD-026` — later Safety impact and Plan resumption/replacement rules;
- practitioner-authored provenance already accepted under `HSP-WD-022`.

No new Domain, lifecycle state, working hypothesis or upstream policy amendment is required.

The core rule is:

> A practitioner may author the Plan, but only Safety & Eligibility may change the current Safety authority that determines whether that Plan is allowed to become current.



## `HSP-PT-017` — Plan is generated but requires professional review/approval before participant delivery/use

**Status:** PRESSURE-TESTED  
**Verdict:** CHANGES REQUIRED TO WORKING FULFILMENT WORDING  
**Upstream contradiction found:** NO  
**Accepted working doctrine challenged:** YES — `HSP-WD-023` fulfilment clause  
**New upstream Product policy required:** NO for the core boundary  
**New working hypothesis:** `HSP-WH-011`

### Preconditions

Assume:

- a logical Generation Request R1 is validly admitted;
- Safety and Entitlements authority permit the relevant pathway;
- generation produces immutable Plan Version P1;
- current Product/pathway rules require professional review and/or approval before the participant may receive/use the Plan as the governed deliverable;
- P1 has not yet passed that required review/approval.

The scenario tests whether:

> `P1 exists`

is enough to mean:

> `R1 fulfilled + entitlement consumed`.

### Existing Product authority already distinguishes generation from review/approval

Current Product Law has distinct Plan lifecycle states including:

`generated`
→ `review`
→ `approval`
→ `scheduled`
→ `active`.

Current Product Law also describes once-off purchased access in terms of the **delivered Plan**, not merely an internally generated Plan object.

Therefore:

> generated existence and participant fulfilment are not universally the same business event.

### Finding 1 — internal generation is not participant fulfilment where a mandatory gate remains

If P1 is in `generated` or `review` and cannot yet be delivered as the governed participant Plan:

- R1 is not yet fulfilled;
- the participant has not yet received the promised usable deliverable;
- the Plan entitlement must not be irreversibly consumed merely because generation computation succeeded.

This is the direct correction to the broad wording in `HSP-WD-023`.

### Finding 2 — Attempt success and Request fulfilment are different

The generation Attempt may have succeeded computationally:

> valid immutable P1 created.

But the business Request can still be incomplete because required review/approval remains.

Therefore:

`Attempt execution success`
≠
`Request fulfilled`.

This reinforces `HSP-WD-010` and `HSP-WD-012`.

### Case A — review approves P1 unchanged

Assume:

1. P1 is generated;
2. professional review is required;
3. reviewer approves P1 without material modification;
4. current Safety/dependency/Entitlements authority still permits delivery;
5. P1 is durably made available/delivered as the participant's governed Plan.

Then R1 may become `fulfilled`.

The exactly-once boundary should converge:

- Plans:
  - one final fulfilled/delivered Plan Version P1 for R1;
- Entitlements:
  - one corresponding fulfilment/access/consumption consequence.

The review completion alone is necessary where required but is not sufficient if participant delivery/access consequence has not durably committed.

### Case B — review modifies the Plan

Assume reviewer determines P1 must be materially changed.

Because Plan Versions are immutable, P1 is not edited in place.

Instead:

1. P1 remains immutable generated/review evidence;
2. practitioner modification creates successor Plan Version P2 through Plans;
3. P2 carries practitioner-modified/authored provenance;
4. P2 passes all required Safety/review/approval/current-authority gates;
5. P2 becomes the one final participant deliverable;
6. R1 is fulfilled by P2;
7. the entitlement consequence occurs once.

This proves an important refinement:

> A logical Request may legitimately contain more than one immutable generated/review Plan Version before fulfilment, while still having exactly one fulfilled participant deliverable.

Therefore earlier shorthand such as “one Request = one Plan” must be read as:

> one Request = at most one **fulfilled/delivered result**, not necessarily only one immutable internal review/version artifact.

### Case C — reviewer declines/rejects P1

Suppose professional review concludes that P1 cannot be approved.

Then:

- P1 remains immutable review evidence while retained;
- P1 never becomes the participant's fulfilled Plan;
- the entitlement is not consumed merely because P1 was generated;
- R1 does not become `fulfilled`.

The exact terminal Request outcome depends on the governed reason:

- Safety/current authority invalidated;
- current capability unfulfillable;
- professional pathway declined/referred;
- another governed outcome.

This pressure test does not invent one universal terminal mapping.

The critical invariant is:

> rejected/non-deliverable P1 does not consume the Plan fulfilment right.

### Case D — approval occurs, then the process crashes before participant delivery/access consequence

Suppose:

1. P1 is approved;
2. process crashes before the durable participant-access/Entitlements consequence is finalised.

On recovery:

- do not generate another fulfilled Plan merely because the worker did not acknowledge;
- do not consume the entitlement twice;
- do not mark R1 fulfilled unless the durable fulfilment boundary actually converged;
- reconcile from durable Plans + Entitlements truth.

This is the same exactly-once convergence problem already accepted in `HSP-WD-023`, but the boundary moves later for review-gated pathways.

### Case E — participant first view occurs much later

The participant may not open the approved delivered Plan immediately.

First view/download is therefore a poor consumption boundary.

Otherwise:

- participant delay would change commercial fulfilment;
- an offline/unread Plan could remain spendable indefinitely;
- duplicate views could create ambiguity.

Therefore:

> first view is not the universal fulfilment/consumption boundary.

### Case F — notification/email fails after durable delivery

If the Plan is durably available to the participant but:

- email fails;
- push notification fails;
- PubSub event is missed;

the Plan may still be fulfilled.

Communications are repairable side effects, not the business fulfilment boundary.

### Finding 3 — `active` is also too late as a universal consumption boundary

Product Law permits scheduled/near-term activation.

A Plan may be a valid delivered participant asset before its effective start date.

Therefore:

> `active` is not the universal entitlement-consumption boundary.

A scheduled Plan should not remain commercially unfulfilled merely because its approved start date is tomorrow.

### Finding 4 — `approval` is not sufficient as a universal boundary either

Approval may exist internally before the Plan is durably made available under the participant's governed access.

Therefore the boundary is not simply:

`Plan.state == approval`.

The business condition is closer to:

> all pathway-required pre-delivery gates satisfied + one final Plan Version durably committed as the participant deliverable + corresponding Entitlements consequence recorded exactly once.

Exact commands/transactions remain JIT detail.

### Finding 5 — pathway-relative gates, common fulfilment invariant

Different pathways may have different pre-delivery gates.

Examples:

#### Fully automated self-guided pathway

Generation, final validation and durable delivery may converge quickly.

No human review is invented merely to satisfy the model.

#### Review-gated pathway

Generated Plan remains pre-fulfilment until the required professional review/approval completes and the approved result is durably delivered.

#### Practitioner-authored pathway

The practitioner-authored Plan Version still must satisfy current Safety/Plan activation requirements before it becomes the fulfilled participant deliverable.

The invariant is common even though the workflow differs.

### Finding 6 — current authority must still be revalidated before delivery

Professional approval at T1 does not freeze authority forever.

Before final participant delivery/fulfilment, revalidate material current authority including as applicable:

- Safety;
- Plan dependency/content authority;
- Entitlements authority;
- required review/approval validity;
- lifecycle/successor state.

If material authority changed after review but before delivery, fail closed.

### Finding 7 — this does not require a new Plan lifecycle state

The locked Product lifecycle already distinguishes generated/review/approval/scheduled/active.

The working gap is not missing Plan state.

It is the **cross-domain Request/Entitlements fulfilment definition**.

No new Plan lifecycle state is justified.

### Finding 8 — `HSP-WD-023` must be refined, not discarded

The following accepted parts of `HSP-WD-023` still hold:

- Request admission ≠ entitlement consumption;
- retries do not spend repeatedly;
- failed/non-fulfilled generation preserves the right;
- fulfilment must converge exactly once across Plans and Entitlements;
- first view/notification/worker acknowledgement are not the boundary.

The clause needing refinement is the shorthand:

> one logical Generation Request durably fulfilled by one valid immutable Plan Version.

That phrase is insufficient because a review-pending or rejected immutable Plan Version can exist without fulfilling the participant's Request.

### `HSP-WH-011` — proposed refined fulfilment rule

Proposed replacement/refinement:

> A Generation Request is fulfilled only when one final Plan Version has satisfied every required pre-delivery gate for its governed pathway and is durably made available/delivered as the participant's Plan, with the corresponding Entitlements fulfilment/access consequence recorded exactly once.

Further:

> A review-gated Request may contain multiple immutable generated/review Plan Versions before fulfilment, but exactly one Plan Version may become the fulfilled participant deliverable for that Request.

And:

> Plan activation, first participant view, notification delivery and worker acknowledgement are not universal entitlement-consumption boundaries.

### Time-scoped entitlement expiry remains separate

If a membership-derived entitlement expires while professional review is still pending, that still depends on the unresolved bounded-completion policy already tracked in `HSP-UPD-001` / `HSP-WH-003`.

PT-017 does not silently resolve that commercial question.

### Result

**CHANGES REQUIRED TO WORKING FULFILMENT WORDING.**

No upstream contradiction was found.

Current Product Law already gives enough direction to reject “generated object exists = fulfilled” for mandatory-review pathways.

The architecture remains sound, but accepted `HSP-WD-023` needs an explicit refinement through `HSP-WH-011` before the fulfilment model is treated as stable.

No new Domain or Plan lifecycle state is justified.



## `HSP-PT-018` — Required professional review is abandoned, delayed or loses its assigned reviewer

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH UPSTREAM SERVICE/COMMERCIAL POLICY DELTA  
**Upstream contradiction found:** NO  
**New Request lifecycle state required:** NO  
**New working doctrine required:** NO  
**New upstream delta:** `HSP-UPD-006`

### Preconditions

Assume:

- logical Generation Request R1 is validly admitted;
- one or more immutable pre-fulfilment Plan Versions may already exist;
- the pathway requires professional review/approval before fulfilment under `HSP-WD-031`;
- Professional Review Case C1 exists;
- practitioner Q1 is the current reviewer or current care/review relationship;
- R1 remains `open`;
- the Plan entitlement has not yet been consumed.

Then one of these happens:

- Q1 leaves the organisation;
- Q1 becomes unavailable;
- Q1's scoped review relationship/access expires;
- review is not completed by the expected operational time;
- professional capacity is temporarily unavailable;
- the review remains unresolved for an extended period.

### Existing Domain Law already separates case truth from individual practitioner access

Current Domain Law assigns to Professional Care:

- practitioner care/review relationship;
- professional review case/outcome/platform-held record;
- practitioner saleable-capacity/referral state.

Therefore the platform has a durable Professional Care obligation/case boundary that is not equivalent to:

> “whatever is in Q1's personal work queue”.

The reviewer is an authorised actor within the case.

The reviewer is not the durable owner of R1, the Plan entitlement or the participant's whole service right.

### Finding 1 — loss of one reviewer does not terminate the Generation Request

If Q1 becomes unavailable:

- R1 does not become `fulfilled`;
- R1 does not become `unfulfillable`;
- R1 does not become `invalidated` merely because one reviewer disappeared;
- the entitlement is not consumed;
- a second Plan purchase is not required.

The review case remains unresolved and Professional Care may reassign it under governed professional-access/capacity rules.

R1 can remain `open` because `HSP-WD-011` already permits an operational condition requiring intervention.

### Finding 2 — reassignment must not create a second commercial fulfilment right

Suppose C1 moves:

`Q1 → Q2`.

That assignment change is not:

- a new Plan purchase;
- a new participant request for re-personalisation;
- a second consumption of the same entitlement;
- permission to create duplicate fulfilled Plans.

The same logical R1 and bound entitlement remain in force, subject to current authority.

If Q2 materially modifies the candidate, immutable Plan versioning applies, but `HSP-WD-031` still allows only one fulfilled deliverable.

### Finding 3 — expired reviewer access must actually end

Current Product Law requires practitioner access to depend on:

- participant consent;
- active care/review relationship;
- defined scope and expiry.

Therefore if Q1's review relationship expires or is terminated:

- Q1 must lose access according to the governed relationship;
- leaving the Request open cannot justify indefinite practitioner access;
- reassignment to Q2 requires Q2's own valid professional relationship/access authority.

Operational convenience must not turn stale professional access into authority.

### Finding 4 — a pending review does not authorise participant delivery

While mandatory review remains unresolved:

- generated candidate Plans remain pre-fulfilment;
- they cannot be exposed as the participant's approved current Plan merely to reduce queue pressure;
- no entitlement consumption occurs under `HSP-WD-031`;
- current Safety/Plan authority remains fail-closed.

The platform may show an appropriate participant-facing pending status without revealing unapproved clinical content.

### Finding 5 — review delay must not cause stale evidence to be blindly approved later

Suppose P1 waits two weeks.

During that time:

- Health facts change;
- Safety authority changes;
- Plan content is withdrawn/superseded;
- entitlement/commercial authority changes under a governing policy;
- the participant's pathway inputs become stale.

When review resumes, the system cannot simply approve the old snapshot because it was once valid.

Before final approval/delivery, revalidate the material current authorities already required by `HSP-WD-008`, `HSP-WD-020`, `HSP-WD-026` and `HSP-WD-031`.

If the old Request basis has lost authority:

- use the existing `invalidated` rules;
- do not resurrect it after later clearance;
- create new governed lineage where required.

### Finding 6 — reviewer absence is not `unfulfillable`

`unfulfillable` is reserved for:

> valid authority + approved Plans capability proves no complete valid Plan can be produced for that exact basis.

A missing reviewer is different.

It is a Professional Care capacity/workflow problem.

Calling it `unfulfillable` would misstate the business truth.

### Finding 7 — provider-side inability may eventually require authorised cancellation

The Request cannot remain `open` forever merely because the platform has not decided what to do.

If the platform reaches a governed service threshold where it cannot provide required professional review:

- an authorised process may need to terminate/cancel the pending service/request;
- the terminal reason must preserve that this was provider/service inability rather than participant cancellation;
- the entitlement must not be falsely marked consumed;
- participant remedy must follow Product/Commerce policy.

The existing `cancelled` terminal can represent deliberate authorised termination without adding a new lifecycle state.

Exact cancellation authority/reason semantics remain future JIT/Product work.

### Finding 8 — participant cancellation is a different reason

If the participant herself withdraws from review before fulfilment:

- R1 may become `cancelled` if current cancellation policy permits;
- professional access/case handling ends or changes appropriately;
- entitlement/refund consequences follow the applicable Product/Commerce/Entitlements policy.

Participant cancellation and provider failure may share a high-level Request terminal state while retaining different durable reasons and commercial consequences.

### Finding 9 — indefinite pending is a Product/service promise problem, not a queue problem

The platform must not let:

- queue retry count;
- Oban timeout;
- database timestamp;
- reviewer inbox age

silently define the participant's commercial rights.

The unanswered policy questions include:

- what service-resolution window is promised;
- when escalation/reassignment becomes mandatory;
- when provider-side cancellation becomes authorised;
- what participant notice is required;
- whether refund, credit, alternate reviewer/service or another remedy is owed;
- how the policy interacts with a membership-derived/time-scoped entitlement.

These are recorded as `HSP-UPD-006`.

Exact internal escalation timers may be downstream operating/JIT policy, but the participant's commercial/service right must be upstream-governed.

### Finding 10 — capacity should be sale-gated before creating obligations

Current Product Law says the initial practitioner-reviewed service should be offered to a limited number of customers to protect professional capacity and validate the workflow.

Current Domain Law also gives Professional Care saleable-capacity/referral state.

Therefore:

> known unavailable professional capacity should be used to prevent or constrain creation/sale of new review obligations where governed.

That is preferable to accepting unlimited paid reviews and relying on timeout/refund handling later.

Capacity projection is not perfect, so post-admission failure still needs `HSP-UPD-006`.

### Finding 11 — communications are required operationally but not business authority

A participant should not be left with an unexplained pending review.

The system should support:

- pending-state explanation;
- material delay notice;
- reassignment/update notice where appropriate;
- terminal/remedy notice.

But notification delivery remains a side effect.

A failed email must not lose the durable review obligation or mutate Request/Entitlements truth.

### Finding 12 — crash/retry/reassignment convergence

If assignment and review processing race:

- Q1 and Q2 must not both create separate fulfilled Plans;
- stale Q1 completion after reassignment must be rejected or reconciled against current case/authority;
- current Professional Care assignment/review authority must be revalidated;
- Plans still allows exactly one fulfilled deliverable;
- Entitlements still finalises exactly once.

No new distributed service or cache authority is justified.

### Time-scoped membership rights remain an existing open policy seam

If R1 was validly admitted from a membership-derived Plan benefit and membership expires while professional review remains pending:

- this scenario does not resolve the commercial right;
- `HSP-UPD-001` / `HSP-WH-003` remains the governing open policy question;
- the preferred working direction remains a bounded completion right for already-admitted work.

`HSP-UPD-006` adds the separate requirement that the platform itself cannot exploit that bounded-completion concept to leave the participant pending indefinitely.

### Result

**PASS WITH UPSTREAM SERVICE/COMMERCIAL POLICY DELTA.**

No new Domain, Plan state or Generation Request lifecycle state is justified.

The existing model already supports:

- an `open` Request waiting on professional work;
- reviewer reassignment as Professional Care workflow;
- entitlement preservation before fulfilment;
- immutable pre-fulfilment Plan versions;
- current-authority revalidation;
- deliberate `cancelled` termination where authorised.

The missing piece is upstream service/commercial policy:

`HSP-UPD-006`
→ define the participant-facing maximum pending/resolution promise and remedy when required professional review cannot be completed because of platform/provider capacity or reviewer failure.



## `HSP-PT-019` — Two valid Requests concurrently attempt to replace the same current Plan lineage

**Status:** PRESSURE-TESTED  
**Verdict:** CHANGES REQUIRED TO WORKING CONCURRENCY MODEL  
**Upstream contradiction found:** NO  
**New Plan lifecycle state required:** NO  
**New working hypothesis:** `HSP-WH-012`

### Preconditions

Assume:

- P1 is the participant's current Plan for one defined Plan lineage/purpose;
- P1 is valid and active;
- two independently valid Requests are created close together:
  - R2 — an ordinary governed adjustment/re-personalisation;
  - R3 — a practitioner-driven correction/modification;
- both Requests are legitimately admitted under their own Safety/Entitlements/professional authority;
- both Requests intend to replace/supersede P1;
- neither Request is a duplicate of the other;
- both may produce internally valid immutable successor Plan Versions.

The scenario intentionally targets the **same Plan lineage**.

It does not assert that the platform may never support multiple simultaneous Plans for genuinely different purposes.

### Existing Product authority already implies linked versioning

Current Product Law requires:

- every adjustment to create a linked new Plan Version;
- immutable Plan snapshots;
- an explicit `superseded` lifecycle state.

Therefore successor lineage is already part of the Product model.

The missing question is concurrent advancement of that lineage.

### Finding 1 — exactly-once per Request is not enough

Suppose:

1. R2 reads P1 as current;
2. R3 reads P1 as current;
3. R2 produces P2;
4. R3 produces P3;
5. R2 fulfils successfully and P2 becomes current;
6. R3 later fulfils successfully based on its stale assumption that P1 is still the predecessor.

If both Requests are treated independently, the platform could produce:

- R2 fulfilled exactly once;
- R3 fulfilled exactly once;
- two entitlement consequences correctly recorded;
- but the Plan lineage is semantically wrong because R3 overwrites P2 without ever evaluating P2.

Therefore:

> Request-level idempotency does not by itself protect lineage correctness.

### Finding 2 — the Request must know what it is replacing

A Request that can replace/supersede an existing current Plan needs enough immutable basis to identify:

> the Plan lineage/current predecessor it was authorised to advance from.

Conceptually R2 and R3 both say:

> `expected current predecessor = P1`.

This is not merely UI context.

It is a material business precondition for fulfilment.

Exact persistence shape remains JIT detail.

### Finding 3 — first successful successor changes current authority for the competitor

If R2 successfully makes P2 the new current head:

> P1 is no longer the current predecessor for a future replacement operation in that same lineage.

R3 must revalidate before fulfilment.

R3 cannot say:

> “my Safety and entitlement are still valid, therefore I may supersede P1.”

The current Plan lineage itself has changed.

That is a material current-authority change.

### Finding 4 — stale competitor must fail closed rather than overwrite the new head

If R3 still targets P1 after P2 became current:

- P3 may remain immutable internal/review evidence where legitimately created;
- R3 must not make P3 current from stale predecessor authority;
- R3 must not supersede P2 without evaluating P2;
- R3 must not consume its fulfilment entitlement solely because computation finished.

The Request must take a governed non-fulfilled outcome.

The exact outcome depends on why/how the Request should continue.

Possible working treatments include:

- invalidate the stale Request because its material Plan-predecessor basis ceased to be current; or
- explicitly create a new Request/review lineage rebased on P2 where the governing pathway permits.

This pack should not silently “auto-rebase” a clinical/professional Request because doing so may change the evidence and judgement basis.

### Finding 5 — automatic rebase is unsafe for material changes

Suppose R3 was a practitioner correction authored after reviewing P1.

If P2 later changes:

- meal composition;
- portions/macros;
- exclusions;
- Safety constraints;
- participant goal/pathway;

then applying R3's modification automatically onto P2 may not preserve the practitioner's actual judgement.

Therefore:

> stale professional work cannot be mechanically replayed against a new current Plan unless the governing professional/Plans contract explicitly says that transformation remains valid.

Usually the safe response is new review/revalidation, not silent merge.

### Finding 6 — not all concurrent Requests necessarily compete

Two Requests are only competing for this rule when they can advance the same mutually exclusive Plan lineage/current-use position.

This pressure test does not create a global:

> “one Plan total per participant”

rule.

The required invariant is narrower:

> one current lineage head cannot be independently advanced twice from the same predecessor without explicit governed reconciliation.

### Finding 7 — predecessor revalidation belongs at fulfilment/current-head transition

Checking only when R2/R3 is created is insufficient.

The race occurs afterward.

The decisive boundary must revalidate that:

- the expected predecessor/current head is still current for that lineage;
- the candidate is still valid against current Safety/dependency authority;
- no incompatible successor has already won;
- all pathway-required gates still hold.

### Finding 8 — the losing Request does not become a duplicate

R3 is not a duplicate of R2.

It may represent legitimate separate participant/professional intent.

Therefore duplicate-suppression semantics are not enough.

Preserve both Request identities, reasons, attempts/candidates, which Request advanced the lineage, and why the competitor could not fulfil from its original predecessor.

### Finding 9 — entitlement handling follows actual fulfilment

If R2 fulfils and R3 becomes stale before fulfilment:

- R2 receives its one governed entitlement consequence;
- R3 must not consume its Plan-fulfilment entitlement merely because P3 was generated;
- any later new/rebased Request uses whatever Entitlements authority the governing product policy permits.

### Finding 10 — participant-facing current Plan must be unambiguous

The participant should never receive two contradictory banners saying:

> “This is your current Plan”

for the same Plan lineage.

Historical access can preserve P1/P2/P3 according to lifecycle/privacy rules.

But current-use presentation must derive from Plans' authoritative lineage state, not last notification, last browser tab or last worker completion.

### Finding 11 — scheduled future Plans need the same concept

Suppose P2 is approved and scheduled for Monday while P1 remains active through Sunday.

A later R3 cannot ignore the already-committed P2 merely because P1 is still active today.

This does not justify inventing a new Plan state; `scheduled` already exists.

It does mean concurrency checks must consider committed successor authority, not only `active`.

### Finding 12 — priority is not invented here

A safety correction and an ordinary monthly adjustment may race.

It may be reasonable for one class to pre-empt another.

However this working pack must not invent a universal priority hierarchy.

The safe invariant is independent of priority:

> once one Request has governed authority to advance the lineage, competing stale Requests cannot independently fulfil from the superseded predecessor.

### `HSP-WH-012` — proposed Plan-lineage concurrency rule

Proposed rule:

> Any Request that may replace/supersede a current Plan must bind to the Plan lineage/predecessor it intends to advance from.

And:

> At fulfilment/current-head transition, Plans must revalidate that the expected predecessor/current lineage authority is still valid. At most one competing Request may successfully advance the same lineage from the same predecessor.

Further:

> A Request made stale by another successor must not silently overwrite, merge onto or supersede that newer Plan. It requires a governed non-fulfilment/review/rebase decision.

This is conceptual concurrency doctrine.

It does not prescribe database locks, compare-and-swap, SQL constraints, transaction isolation, advisory locks, queues or GenServers.

### JIT proof obligation

Future Plans JIT should prove the same-lineage race under:

- two BEAM processes;
- two nodes where applicable;
- duplicate/retried commands;
- scheduled successor;
- professional review completion racing automated adjustment;
- crash after candidate creation but before lineage transition.

Required outcome:

> never two incompatible fulfilled current successors from the same lineage predecessor.

### Result

**CHANGES REQUIRED TO WORKING CONCURRENCY MODEL.**

No upstream Product contradiction was found.

Existing Product Law already supplies immutable linked Plan Versions and the `superseded`/`scheduled` lifecycle semantics.

The missing working rule is `HSP-WH-012`:

> exactly-once per Request must be complemented by concurrency protection for the Plan lineage/current predecessor being advanced.

No new Domain or Plan lifecycle state is justified.



## `HSP-PT-020` — Request is cancelled, then stale generation/review completion tries to fulfil it

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH UPSTREAM COMMERCIAL CLARIFICATION  
**Upstream contradiction found:** NO architectural contradiction  
**New working doctrine required:** NO  
**New upstream delta:** `HSP-UPD-007`

### Preconditions

Assume:

- Generation Request R1 is `open`;
- Safety/Entitlements authority was valid when R1 was admitted;
- an Attempt and/or mandatory professional review is in progress;
- R1 has not yet crossed the `HSP-WD-031` fulfilment boundary;
- an authorised cancellation of R1 is durably accepted;
- afterward, stale work completes and attempts to deliver/fulfil R1.

Cancellation may originate from:

- the participant, where Product policy permits;
- a governed provider/service termination;
- another authorised cancellation path.

This scenario is about terminal Request concurrency.

It does not decide refund policy.

### Finding 1 — accepted terminal Request truth wins over stale work

`HSP-WD-011` already makes terminal Request outcomes irreversible.

Therefore once R1 is durably `cancelled`:

- R1 cannot later become `fulfilled`;
- a stale Attempt cannot reopen R1;
- a late reviewer approval cannot reopen R1;
- a late notification cannot imply fulfilment;
- a generated candidate cannot become the participant's delivered Plan through R1.

The durable Request truth outranks worker/session/queue state.

### Case A — cancellation wins before candidate generation completes

Suppose:

1. R1 is open;
2. Attempt A1 is computing;
3. cancellation commits;
4. A1 completes afterward.

Then:

- R1 remains `cancelled`;
- A1's completion is stale relative to the terminal Request;
- any candidate produced cannot cross the participant fulfilment boundary;
- no Plan fulfilment entitlement consequence is recorded;
- recovery/cleanup follows durable truth rather than trying to “finish what the worker started”.

The exact retention of an internal candidate is JIT/data-lifecycle detail.

### Case B — immutable generated Plan exists, but mandatory review/delivery has not completed

Suppose:

1. P1 has already been generated;
2. R1 remains open because professional review/approval is mandatory;
3. cancellation commits;
4. reviewer later approves P1 from stale work context.

Under `HSP-WD-031`:

- P1's existence was not fulfilment;
- review approval after cancellation cannot make R1 fulfilled;
- P1 cannot become the participant's delivered/current Plan through cancelled R1;
- the Plan entitlement is not consumed by that late approval.

Historical review/provenance may remain where governing retention law permits.

### Case C — fulfilment wins before cancellation

The reverse race must also be deterministic.

Suppose the full `HSP-WD-031` fulfilment boundary commits first:

- final Plan Version passed required gates;
- governed participant delivery/access was durably established;
- corresponding Entitlements consequence finalised exactly once;
- R1 became `fulfilled`.

A later cancellation command cannot rewrite R1 to `cancelled`.

Any later participant right to stop using the Plan, delete the Account, request a correction, or pursue a refund is a separate governed event.

Terminal history is not rewritten.

### Finding 2 — there must be one winning terminal outcome

The system must never converge to:

- Plans: `R1 = cancelled`;
- Entitlements: consumed as fulfilled;
- participant access: delivered Plan current;

or the inverse inconsistent combination.

Cancellation and fulfilment are competing terminal business transitions.

Whichever authoritative transition legitimately wins must be reflected consistently across the owning Domains.

Exact cross-domain command/reconciliation mechanics remain JIT detail.

### Finding 3 — late professional work must revalidate case/request authority

A practitioner can be legitimately working on C1 while R1 is cancelled elsewhere.

Professional Care must not assume:

> “I still have an open screen, therefore the review is still actionable.”

Before a review outcome triggers Plan delivery/current use, downstream handling must revalidate:

- current professional case/relationship authority;
- current Request status;
- current Safety authority;
- current Plan lineage authority where relevant.

A late review record may remain professional evidence without becoming a current Plan mutation.

### Finding 4 — cancellation does not necessarily mean candidate deletion

Business cancellation answers:

> may R1 still fulfil?

It does not by itself answer the data-lifecycle question:

> must every intermediate/generated/review artifact be physically deleted immediately?

Retention/deletion follows `HSP-WD-030` and the category-specific Privacy/professional rules.

So cancellation must not be confused with physical erasure.

### Finding 5 — cancellation does not automatically define the Entitlements remedy

If cancellation occurs before fulfilment:

> the fulfilment entitlement must not be marked consumed merely because work occurred.

But the eventual Entitlements/commercial consequence may depend on the cancellation reason and Product policy.

Possible concepts include:

- release/preserve the right;
- forfeit/terminate a right under an authorised participant cancellation rule;
- credit/refund through Commerce;
- transfer into another governed service outcome.

This pack does not select among them universally.

### Finding 6 — refund boundary is not the fulfilment boundary

Current locked Product Law states:

> “plan refunds end after generation”.

`HSP-WD-031` separately establishes that, for a review-gated pathway:

> generation may occur before participant fulfilment/delivery.

Therefore two business boundaries now clearly exist:

1. **commercial refund boundary**;
2. **Plan Request fulfilment / Entitlements consumption boundary**.

They must not be collapsed.

A Plan can conceptually be:

> generated but not yet fulfilled.

### Finding 7 — review-gated cancellation exposes a Product/Commerce clarification need

Consider:

1. P1 is generated;
2. required professional review has not completed;
3. participant or provider cancels R1;
4. P1 was never an approved delivered participant Plan.

Locked `DEC-045` says Plan refunds end after generation, but the current Product wording does not explicitly explain how that rule applies to:

- review-gated Plans;
- practitioner-reviewed services;
- provider inability to complete required review;
- generated-but-never-deliverable artifacts;
- stale generation completing after cancellation.

This pack must not invent an exception to locked Product Law.

It records the ambiguity as `HSP-UPD-007`.

### Finding 8 — stale technical completion cannot be allowed to manufacture commercial truth

A worker that finishes after authoritative cancellation must not itself decide:

> “generation happened now, therefore refund rights just disappeared.”

Commercial rights must be determined from governed Product/Commerce semantics and authoritative event ordering, not from whichever asynchronous process happened to finish last.

The exact meaning of qualifying `generation` for `DEC-045` needs the upstream clarification in `HSP-UPD-007`.

### Finding 9 — cancellation before fulfilment does not supersede a current prior Plan by itself

If R1 was intended to replace current P0:

- cancelling R1 does not imply P0 was superseded;
- if P0 remains otherwise valid/current, it remains governed by its existing lifecycle;
- cancellation only terminates the successor Request.

This avoids a gap where cancelling an unfinished replacement accidentally removes the participant's safe current Plan.

### Finding 10 — retry/restart cannot resurrect cancelled Request identity

If the participant later wants another Plan after R1 cancellation:

- do not reset R1 to `open`;
- create a new governed Request if current Product/Entitlements/Safety rules permit;
- retain R1 as terminal history while retained.

This preserves terminal-state irreversibility and audit.

### Result

**PASS WITH UPSTREAM COMMERCIAL CLARIFICATION.**

The architecture requires no new Request state or new working doctrine.

Existing accepted rules are sufficient:

- `HSP-WD-011` — terminal Request states are irreversible;
- `HSP-WD-012` — recovery follows durable business truth, not worker acknowledgements;
- `HSP-WD-023` / `HSP-WD-031` — admission/generation differs from exactly-once fulfilment;
- `HSP-WD-030` — cancellation and data retention are separate dimensions;
- `HSP-WD-032` — stale successor work cannot override current lineage authority.

The new unresolved issue is upstream commercial semantics:

`HSP-UPD-007`
→ clarify locked `DEC-045` for generated-but-not-yet-delivered review-gated Plans and cancellation/provider-failure races.



## `HSP-PT-021` — Participant changes Plan inputs after Request admission but before fulfilment

**Status:** PRESSURE-TESTED  
**Verdict:** PASS WITH WORKING REFINEMENT + UPSTREAM COMMERCIAL CLARIFICATION  
**Upstream contradiction found:** NO  
**New working hypothesis:** `HSP-WH-013`  
**New upstream delta:** `HSP-UPD-008`

### Preconditions

Assume:

- R1 is a valid `open` Generation Request;
- R1's immutable Generation Input Basis B1 includes participant-owned Direct Plan Inputs;
- generation and/or review has begun;
- R1 has not crossed the `HSP-WD-031` fulfilment boundary;
- the participant later edits one or more Plan-relevant inputs.

Examples include:

- goal/pathway;
- meal frequency/structure;
- a mandatory ethical exclusion;
- a mandatory religious exclusion;
- a non-clinical food preference/dislike.

This scenario deliberately excludes new clinical facts already covered by Health/Safety pressure tests.

### Existing Product authority

Current Product Law:

- separates allergies, intolerances, religious exclusions, ethical exclusions, dislikes and preferences;
- requires generated Plans to preserve a participant-input snapshot;
- treats goal, pathway, meal frequency and major preferences as material Plan explanation/provenance;
- requires a new purchase or qualifying membership/add-on for preference/progress-based **re-personalisation**.

Those rules support immutable request basis but do not fully define edits made before the first Request is fulfilled.

### Finding 1 — the old Generation Basis must never be silently edited

Suppose B1 contains:

> ethical exclusion = none

and after generation starts the participant changes:

> ethical exclusion = vegan

The platform must not mutate B1 in place and pretend the same execution always used the new value.

B1 remains evidence of what R1/its Attempt actually executed against.

If a new Plan must reflect the participant's changed input:

> new authorised basis B2  
> → new logical Request as governed.

This preserves `HSP-WD-008`, `HSP-WD-013` and reproducibility.

### Finding 2 — a profile edit is not automatically an instruction to alter an in-flight Request

A dangerous implementation would assume:

> any Plan-relevant field changed anywhere  
> → abort every open Request.

That would be too broad.

A participant may change:

- a preference intended only for future Plans;
- a value unrelated to R1's pathway;
- a non-material display choice;
- an input that Product UX explicitly says takes effect next generation.

Therefore every edit needs enough business semantics to answer:

> Does this change apply to R1, future Requests only, or another purpose?

Database recency alone is not sufficient.

### Finding 3 — explicit current-Request change of intent makes the stale basis non-deliverable

Suppose the participant explicitly says:

> “Apply this new mandatory ethical exclusion to the Plan I am currently waiting for.”

If P1 generated from B1 would violate that newly applicable current intent:

- P1 must not be delivered as though it still satisfies the participant's Request;
- B1 must not be mutated;
- R1 must reach a governed non-fulfilment terminal outcome;
- a new Request/B2 is required if the participant still wants the Plan and current authority permits it.

The exact terminal classification may depend on the action:

- explicit participant stop/restart may be `cancelled`;
- a material owning-authority input becoming non-current may be `invalidated`.

This pack does not force one universal label for every UX path.

### Finding 4 — future-only edit does not invalidate R1

Suppose the participant explicitly chooses:

> “Use this preference next time.”

Then:

- B1 remains valid for R1;
- R1 may continue;
- the new value becomes available to future authorised Requests;
- historical P1/B1 explains what was delivered.

This avoids needless cancellation/re-generation.

### Finding 5 — mandatory participant-owned constraints are not soft merely because they are non-clinical

A religious or ethical exclusion can be a participant-owned hard constraint.

Plans may not silently weaken it merely because Safety does not own it.

If the new declaration is explicitly applicable to current R1 and the candidate violates it:

> delivery fails closed for participant-intent correctness.

This is different from clinical fail-closed authority, but still a governed hard constraint.

### Finding 6 — ordinary soft preference edits may have different applicability

If the participant changes:

> dislike mushrooms

while a Plan is being generated, Product UX may legitimately define that as:

- future-only;
- current-Request superseding;
- non-blocking if the current candidate remains acceptable under explicitly disclosed rules.

The architecture should not invent that product rule.

The critical requirement is that the effect is explicit and reproducible.

### Finding 7 — old Request cannot “follow” mutable profile state

R1 must not mean:

> “generate from whatever her profile happens to contain when each worker reads it.”

That would destroy determinism and make retries disagree.

Instead:

- R1 binds B1;
- later participant changes have their own known time and scope;
- current delivery checks only the changes that governing semantics say are material to R1.

### Finding 8 — participant intent is a current delivery consideration where it is explicitly applicable

`HSP-WD-008` already says current authority decides whether a candidate may still be delivered and that unrelated profile changes should not abort generation.

PT-021 refines this:

> explicitly current-request participant intent can itself be a material delivery precondition even when it is not a Safety authority.

This does not make Plans owner of the participant's source preference/goal truth.

Plans consumes the governed value/applicability from the owning boundary.

### Finding 9 — a new Request is not a retry

If the participant materially changes current-request intent:

- do not reuse the old Attempt as though it merely retried;
- do not overwrite B1;
- establish B2;
- create a new logical Request if permitted.

This follows `HSP-WD-010`.

### Finding 10 — entitlement consumption still waits for fulfilment

If R1 is cancelled/invalidated before `HSP-WD-031` fulfilment:

- the Plan fulfilment entitlement is not marked consumed merely because work happened;
- candidate generation alone does not change that rule.

However the right to use the **same commercial entitlement** for B2 is not fully determined by architecture.

### Finding 11 — `DEC-038` creates a pre-fulfilment commercial boundary question

Locked `DEC-038` says preference/progress-based **re-personalisation** requires a new purchase or qualifying membership/add-on.

But PT-021 concerns a participant who changes her choices **before receiving her first fulfilled Plan**.

Two interpretations are possible:

1. this is still the original purchased fulfilment being corrected before delivery; or
2. once generation has materially begun, changing preference constitutes another paid personalisation.

The working pack must not choose between those Product meanings.

This is `HSP-UPD-008`.

### Finding 12 — `DEC-045` can interact with the same scenario

If P1 has technically been generated before the participant changes her intent:

- `DEC-045` may say ordinary Plan refund rights have ended;
- `HSP-WD-031` may still say R1 is not yet fulfilled;
- `HSP-UPD-008` therefore needs to be reconciled with existing `HSP-UPD-007`.

Again:

> refund boundary, entitlement consumption, Request fulfilment and permission to create B2 are distinct business questions.

### Finding 13 — UI must make applicability explicit

A future participant experience should not create ambiguity such as:

> “Saved successfully”

when the participant cannot tell whether the change affects:

- the Plan currently being generated;
- only future Plans;
- her general profile;
- current Safety evaluation;
- a later monthly review.

For material Plan inputs, the UX should communicate effect/scope clearly.

The exact interaction design belongs to Frontend/JIT.

### `HSP-WH-013` — proposed participant-intent applicability rule

Proposed rule:

> Participant-owned Plan-input edits made after Request admission must have explicit applicability semantics: current Request versus future Requests/other purpose.

Further:

> The immutable Generation Basis of an existing Request is never silently mutated. If a material participant-owned input is explicitly intended to apply to the current Request and makes its basis/candidate stale, that Request must not fulfil from the old basis; governed cancellation/invalidation and a newly authorised Request are required.

And:

> Unrelated or explicitly future-only edits do not automatically invalidate in-flight generation.

### Result

**PASS WITH WORKING REFINEMENT + UPSTREAM COMMERCIAL CLARIFICATION.**

No new Domain or lifecycle state is justified.

The architecture already has the right primitives:

- immutable Generation Basis;
- Direct Plan Inputs;
- hard-vs-soft constraint classification;
- material current-authority revalidation;
- irreversible Request terminals;
- new Request for genuinely new intent;
- fulfilment-based entitlement consumption.

The missing working clarification is `HSP-WH-013`.

The remaining Product/Commerce question is `HSP-UPD-008`:

> how a pre-fulfilment participant change of Plan intent interacts with `DEC-038`, the original entitlement and `DEC-045`.



## `HSP-PT-022` — Delivered Plan correction versus new paid/entitled re-personalisation

**Status:** PRESSURE-TESTED  
**Verdict:** PASS  
**Upstream contradiction found:** NO  
**New working doctrine required:** NO  
**New upstream Product amendment required:** NO for the core distinction

### Preconditions

Assume:

- P1 has already crossed the `HSP-WD-031` fulfilment boundary and is the delivered participant Plan;
- P1 has an immutable Generation Input Basis B1 and Plan Result Provenance;
- the participant later says that some aspect of P1 should be different.

Two superficially similar participant statements are tested:

#### Case A — delivered Plan was wrong against its own governed basis

Example:

- B1 says a mandatory exclusion or approved input was `no mushrooms`;
- the approved deterministic rules should have respected that input;
- P1 nevertheless contains mushrooms.

#### Case B — delivered Plan was correct when generated, but participant intent later changes

Example:

- B1 correctly recorded that mushrooms were acceptable;
- P1 legitimately contains mushrooms;
- after delivery the participant decides she no longer wants mushrooms.

The UI complaint may look almost identical.

The commercial meaning is not.

### Existing Product authority already creates the distinction

Current locked Product Law says:

- a once-off purchaser retains access to the delivered Plan and receives corrections and safety replacements;
- preference/progress-based re-personalisation requires a new purchase or active qualifying membership/add-on;
- governed corrections, replacements and safety withdrawals preserve history without consuming a new entitlement.

Therefore correction and re-personalisation are already separate Product concepts.

### Finding 1 — correction classification is provenance-relative

A Plan correction is not established merely because:

> “the participant wants something changed.”

The platform must determine whether P1 materially failed to conform to the governed truth it was supposed to satisfy at fulfilment.

Relevant evidence includes:

- B1;
- applicable Direct Plan Inputs;
- current-at-generation Safety constraints;
- calculation/ruleset version;
- approved content/substitution universe;
- Plan Result Provenance;
- any documented generation/selection defect.

Conceptually:

> **correction asks whether the delivered result was wrong relative to the authorised basis/rules that governed that delivery.**

### Case A — basis said “exclude”, Plan incorrectly included

If B1 and governing rules required exclusion but P1 violated it:

- P1 is not retrospectively edited;
- preserve P1 and its provenance/history while retained;
- issue a governed correction/replacement Plan Version;
- correction lineage points to the affected delivered Plan;
- no new ordinary re-personalisation entitlement is consumed under current Product Law;
- if the defect is Safety-relevant, Safety consequences may additionally apply.

This remains true even if the participant notices the defect days later.

The passage of time does not transform a platform/Plan defect into a new paid preference.

### Finding 2 — correction does not mean silently changing historical inputs

Suppose the correction reveals that:

- B1 was correct;
- the Plan engine/result was wrong.

Then B1 remains unchanged.

The successor Plan fixes the result.

Suppose instead that evidence proves the platform captured the participant's submitted input incorrectly.

Then the Health/input correction model applies:

- preserve what the platform actually recorded/used;
- preserve correction provenance;
- do not rewrite historical decision-time evidence;
- establish corrected current truth;
- issue the appropriate governed replacement.

Again, history is corrected by lineage/supersession rather than silent mutation.

### Case B — basis was correct, participant later changes preference

If B1 correctly allowed mushrooms and P1 correctly followed B1:

- P1 is not defective;
- the participant's new preference is a new current input;
- save the new preference according to its owning domain/applicability;
- do not regenerate P1 merely because the profile changed;
- future re-personalisation follows the applicable Product/Entitlements cadence.

Under current locked Product Law, preference/progress re-personalisation requires:

- a new purchase; or
- an active qualifying membership/add-on.

For Premium ordinary progress-driven adjustment, current Product Law separately provides the monthly review entitlement model.

Therefore:

> **new preference after correct delivery is not reclassified as a free correction merely because the requested visual change is small.**

### Finding 3 — same visible change can have different entitlement consequences

Consider the same desired output:

> “Remove mushrooms from my Plan.”

#### Scenario 1 — correction

B1 already required no mushrooms.

Outcome:

> governed correction/replacement  
> → no new ordinary Plan entitlement consumed.

#### Scenario 2 — new preference

B1 allowed mushrooms; preference changes after delivery.

Outcome:

> store the new preference  
> → current Plan remains historically correct  
> → next authorised re-personalisation occurs only through a qualifying review/adjustment entitlement or new purchase/add-on.

The UI may offer similar wording, but the business provenance must preserve why the change occurred.

### Finding 4 — participant report alone does not prove historical platform error

Suppose the participant says:

> “I definitely selected no mushrooms originally.”

But B1 records mushrooms as allowed.

Do not automatically choose either extreme:

- charge immediately because “the database says allowed”; or
- silently rewrite B1 because “the participant says otherwise now”.

Use available evidence:

- submitted input/version evidence;
- durable receipt/audit evidence;
- correction history;
- known platform defect evidence;
- support/professional evidence where relevant.

If the platform can establish that the original capture or Plan generation was defective, use the correction path.

If the evidence shows a genuine later change of preference, use re-personalisation rules.

If historical cause cannot be established, the exact customer-remedy/support policy may need governed operational judgement; that uncertainty does not justify rewriting provenance.

### Finding 5 — safety correction remains stronger than ordinary preference handling

If the discrepancy concerns:

- allergy;
- contraindication;
- medication-related restriction;
- another Safety hard constraint;

do not wait for ordinary monthly review.

Use the immediate Health/Safety correction and impact path already established by earlier pressure tests.

The replacement may then be a safety correction under current Product Law and does not become paid ordinary re-personalisation.

### Finding 6 — ordinary post-delivery profile logging still does not adjust immediately

PT-022 preserves the v0.41.0 cadence clarification.

If the participant logs:

- weight;
- water;
- exercise;
- eating habits;
- adherence;
- sleep;
- ordinary preferences;

that does not automatically produce a new Plan.

For ordinary progress/preference re-personalisation:

> observations accumulate  
> → qualifying review/adjustment entitlement becomes actionable  
> → complete check-in / required exposure  
> → review outcome  
> → new Plan only if warranted.

### Finding 7 — no-change review remains valid fulfilment of a review right

An entitled monthly review may conclude:

> P1 remains appropriate; no new Plan Version needed.

That still satisfies the Product review right where current Product Law says no-change counts as a completed review.

Therefore:

> review entitlement ≠ guaranteed generation.

This reinforces the decision not to model recurring access as a simplistic “generation token”.

### Finding 8 — correction/replacement should retain causation provenance

The successor Plan should be distinguishable as applicable from:

- correction of platform/Plan defect;
- Safety replacement;
- practitioner correction;
- periodic re-personalisation;
- new participant preference;
- progress-driven adjustment.

This does not require a new Domain.

The purpose is explainability, commercial correctness and future dispute/support handling.

Exact fields/enums remain JIT design.

### Finding 9 — replacement lineage still obeys `HSP-WD-032`

If a correction Request races with another adjustment Request against P1:

- both cannot independently advance the same Plan lineage from P1;
- current-head/predecessor authority is revalidated;
- stale work does not overwrite the winning successor.

Correction entitlement semantics do not exempt the operation from Plan-lineage concurrency correctness.

### Finding 10 — no new architecture concept is needed

The distinction is already fully expressible through accepted concepts:

- immutable Generation Basis;
- Result Provenance;
- correction/supersession lineage;
- participant-input known/effective time;
- Request/Attempt/Plan separation;
- Entitlements authority;
- periodic review entitlement;
- current Safety authority;
- Plan-lineage concurrency.

The scenario therefore does not justify another Resource, lifecycle state or working hypothesis.

### Result

**PASS.**

The core discriminator is:

> **Was the delivered Plan wrong relative to the authoritative basis/rules it was required to satisfy, or did the participant's intent/progress change after a correct delivery?**

If wrong at delivery:

> correction/replacement path  
> → preserve history  
> → no new ordinary entitlement consumed.

If correct at delivery and intent later changes:

> new current input  
> → no immediate profile-triggered regeneration  
> → re-personalise only through the applicable purchase/membership/add-on/review entitlement.

This is already supported by current Product Law and accepted working doctrine.

---

## Discovery-suite exit decision at v0.42.0

`HSP-PT-022` is the planned final pressure test for this pre-JIT discovery grill.

The suite now shows convergence:

- recent scenarios mostly PASS using existing doctrine;
- genuine remaining gaps are predominantly upstream Product/Commerce/service-policy deltas;
- no recent pressure test justifies a new Domain;
- no recent pressure test justifies expanding the core Request or Plan lifecycle;
- concurrency, provenance, Safety, fulfilment, correction and periodic-adjustment boundaries have all been attacked directly.

Therefore:

> **STOP adding ordinary hypothetical pressure tests to this working pack unless new evidence, a contradiction, changed Product scope or JIT work exposes a genuinely new seam.**

The next recommended activity is:

1. consolidate/open-owner the `HSP-UPD-*` authority deltas;
2. compress accepted `HSP-WD-*` doctrine into a small implementation-facing Pre-JIT Contract;
3. retain `HSP-PT-*` scenarios as deep evidence rather than default implementation context;
4. proceed to the governed upstream amendment/JIT sequence when authorised.

This is a discovery stop, not an implementation authorisation.


# 10. Working conclusion at v0.42.0

The emerging design principle is:

> Build the mature safety and provenance model from the beginning, but admit only a narrow, positively approved low-complexity population into MVP automated plan generation.

The platform should become more capable over time by expanding the set of proven automated pathways, not by changing the meaning of historical health facts, weakening safety controls, or replacing professional authority with automation.

Complexity belongs in explicit governed pathways, not hidden inside a permissive plan generator.

At v0.2.0, MVP automation is explicitly treated as a positively authorised pathway rather than a default path from which exceptions are removed.

At v0.3.0, Safety permission and Plan capability are explicitly separated: a truthful `eligible_automated` outcome does not guarantee that the current Plans capability can produce an approved deterministic plan.

At v0.4.0, generation failure is explicitly classified and plan delivery is all-or-nothing: no failed attempt may silently consume entitlement or expose a partial plan.

At v0.5.0, concurrent generation preserves an immutable generation basis while revalidating current authority before delivery. Single-active-workspace LiveView behaviour was recorded as proposed defence-in-depth UX hardening, not as business correctness authority.

At v0.6.0, single-active-workspace behaviour is accepted as selective defence-in-depth UX hardening. It must never replace durable server-side idempotency, authority checks, transactional guards, or correctness under multiple tabs/devices/retries.

At v0.7.0, Generation Request, Generation Attempt, and Plan Version are explicitly separated. Materially invalidated requests are terminal historical records and must never be resurrected; later renewed authority creates a new logical request.

At v0.8.0, the Generation Request lifecycle is accepted as `open → fulfilled | cancelled | invalidated | unfulfillable`, with terminal states irreversible and execution/worker conditions kept outside business lifecycle truth.

At v0.9.0, Generation Attempt execution status is separated from Attempt outcome. Retries create new Attempt identities, orphaned attempts must reconcile, and durable committed business state outranks worker acknowledgement.

At v0.10.0, every Plan Version is tied to an immutable Generation Basis containing only the minimum material authoritative inputs and version identities required for reproducibility. Cross-domain evidence must not become competing authority or unnecessary sensitive-data duplication.

At v0.11.0, plan-relevant data is explicitly classified as Direct Plan Input, Safety-Derived Plan Constraint, or Not a Plan Input. Safety & Eligibility must not become a generic router, and Plans must not reconstruct clinical meaning from raw upstream evidence.

At v0.12.0, plan-generation constraints preserve both meaning and strength. Safety-derived mandatory constraints are hard constraints, ordinary preferences remain soft unless explicitly governed otherwise, and Plans may never provide a convenience override that weakens upstream Safety authority.

At v0.13.0, an unsatisfied hard constraint terminates the Generation Request as `unfulfillable` when Safety authority remains valid. Plans capability/content gaps must never be disguised as Safety outcomes or generic professional-review requirements.

At v0.14.0, intake is treated as an automation-grade evidence workflow rather than a generic form. Structured semantics, explicit applicability, partial-save boundaries, missing-state distinctions, and questionnaire-version/reconfirmation evidence are required so downstream Safety and Plans decisions remain trustworthy.

At v0.15.0, temporal truth is explicit: fact-specific freshness, effective time, recorded/known time, historical observations, and reconfirmation are separate concerns. Late-arriving information can change current Safety authority without rewriting what the platform actually knew when an earlier Plan Version was generated.

At v0.16.0, intake completion is explicitly purpose- and version-relative. Current automation readiness follows current applicable intake/protocol authority, while historical completion and eligibility remain reproducible under the versions that originally governed them. Safety-rule changes must explicitly declare their impact on already active participants/plans.

At v0.17.0, health changes receive impact-sensitive Safety consequences. Required reevaluation blocks new personalised actions until current authority is re-established, and every Safety evaluation is bound to an immutable material basis so stale evaluations cannot silently become current authority.

At v0.18.0, immutable Safety Evaluations are explicitly separated from stateful Safety Cases. Current eligibility authority may change without rewriting historical evaluations, and Safety Case is reserved for genuine governed safety processes rather than generic workflow/task management.

At v0.19.0, Professional Care is explicitly prevented from becoming a second safety gateway into Plans. Practitioner outcomes remain structured/scoped/audited, flow through Safety & Eligibility, and preserve clear provenance between professionally cleared automation and practitioner-authored or modified Plan Versions.

At v0.20.0, the pack enters structural-hardening mode: stable local working-design IDs, explicit non-authoritative normative-strength classes, a decision register, and scenario pressure testing are introduced. `HSP-PT-001` passes without contradiction.

At v0.21.0, `HSP-PT-002` (durable commit followed by worker crash) passes and `HSP-PT-003` (concurrent duplicate generation) passes conceptually with an explicit future JIT proof obligation for durable server-side uniqueness/idempotency.

At v0.22.0, `HSP-PT-004` (serious allergy correction after active Plan delivery) validates the temporal/history/safety model but exposes a working-design gap: eligibility adjudication and active-plan Safety impact may require distinct conceptual contracts. `HSP-WH-001` is opened for explicit resolution; no upstream contradiction is identified.

At v0.23.0, `HSP-WH-001` is accepted and folded into refined `HSP-WD-021`: Safety Adjudication now explicitly contains distinct Eligibility Evaluation and Safety Impact Assessment purposes while Safety Case remains separate. `HSP-PT-005` (large-population safety protocol withdrawal) passes with governance and future JIT proof obligations, and clarifies that reassessment timing and active-authority/Plan consequence must both be explicitly governed.

At v0.24.0, `HSP-PT-006` exposes a material cross-Domain commercial gap: generation admission, entitlement authorization/claim, Plan fulfilment and entitlement consumption need a precise exactly-once contract. `HSP-WH-002` proposes request-bound Entitlements authority with consumption only on successful fulfilment. `HSP-WH-003` records that mid-flight expiry semantics for time-scoped membership benefits require explicit upstream Product/Entitlements policy rather than implementation guesswork.

At v0.25.0, `HSP-WH-002` is accepted as `HSP-WD-023`: logical Generation Requests bind to specific Entitlements authority, admission is distinct from consumption, and successful Plan/Entitlements fulfilment must converge exactly once. `HSP-WH-003` records Policy B as the preferred working direction—valid admission grants a bounded completion right across membership expiry—but remains explicitly subject to upstream Product/Entitlements policy approval.

At v0.26.0, the explicit upstream-policy delta register is introduced. `HSP-PT-007` confirms that withdrawn plan dependencies cannot be delivered despite historical version pinning, while ordinary supersession semantics remain an open authority delta (`HSP-UPD-002`). The test also exposes a working-model inconsistency in the current Generation Basis wording and opens `HSP-WH-004` to separate immutable pre-generation input/dependency basis from exact successful Plan result provenance.

At v0.27.0, `HSP-WH-004` is accepted as `HSP-WD-024`. `HSP-PT-008` confirms that post-delivery withdrawal preserves historical Plan evidence while current-use authority may change, governed corrections/replacements/safety withdrawals consume no new entitlement, and replacement forms a new governed lineage rather than reopening the fulfilled Generation Request. `HSP-WH-005` and `HSP-UPD-003` capture the remaining lifecycle/affected-delivery semantics.

At v0.28.0, `HSP-WH-005` is accepted as `HSP-WD-025`, distinguishing recoverable Safety pause from Plan withdrawal. `HSP-PT-009` shows that the same immutable Plan Version may resume only when current Safety authority permits that exact Plan and no material Plan content/constraint/dependency change is required; otherwise a new immutable successor Plan Version is required. `HSP-WH-006` records that proposed resumption rule for explicit acceptance.

At v0.29.0, `HSP-WH-006` is accepted as `HSP-WD-026`. `HSP-PT-010` validates the existing effective-time/known-time/history model for genuinely late-arriving laboratory evidence, while exposing a critical boundary: evidence already durably received by NewYou cannot be treated as unknown merely because asynchronous processing/projection lagged. `HSP-WH-007` records the proposed authoritative-known-time rule.

At v0.30.0, `HSP-WH-007` is accepted as `HSP-WD-027`. `HSP-PT-011` confirms that provenance is not a universal truth hierarchy and that unresolved safety-relevant contradictions must fail the positive automation-admission test. The scenario opens `HSP-WH-008`: material conflicting health evidence must be preservable as multiple concurrent source assertions rather than being collapsed into a lossy scalar current value.

At v0.31.0, `HSP-WH-008` is accepted as `HSP-WD-028`. `HSP-PT-012` pressure-tests a practitioner retraction after downstream Safety/Plan reliance and confirms that corrections must not rewrite the original assertion or historical decisions. `HSP-WH-009` records the required distinction between “wrong when made” evidence correction and genuine later participant-state change.

At v0.32.0, `HSP-WH-009` is accepted as `HSP-WD-029`. `HSP-PT-013` pressure-tests professional clearance/override against later material health change and passes without new doctrine: existing impact-sensitive reevaluation and scoped evidence/condition/time-bound professional authority are sufficient. Unrelated health changes need not invalidate professional authority; material changes to its reviewed basis/scope/conditions require current Safety authority to be re-established.

At v0.33.0, `HSP-PT-014` pressure-tests full deletion across Health, Safety, Plans, Entitlements, audit and professional-record boundaries. Current Product/Architecture Law resolves the core direction: full deletion is irreversible, ends Plan/entitlement access, deletes/anonymises eligible self-guided Health data, allows only category-authorised restricted retention, and must be non-resurrecting. The working pack is corrected to treat immutability and retention as separate dimensions. `HSP-WH-010` records that proposed rule, while `HSP-UPD-004` records the remaining category-specific deletion-contract detail for Plan/Safety/professional variants.

At v0.34.0, `HSP-WH-010` is accepted as `HSP-WD-030`. `HSP-PT-015` proves the canonical `unfulfillable` case: valid Safety and Entitlements authority can coexist with a Plans capability failure when mandatory hard constraints have no solution in the approved deterministic catalogue. Plans must not weaken constraints, falsify Safety outcomes, misuse professional review as catalogue repair, or consume the entitlement. `HSP-UPD-005` records the remaining upstream commercial question: what customer remedy is owed when a paid Plan cannot currently be fulfilled.

At v0.35.0, `HSP-PT-016` pressure-tests practitioner-authored/modified Plans against current Safety hard constraints and passes without new doctrine. Professional Care may author or materially modify Plan content, but any clinical clearance/restriction/override consequence must first become current Safety authority through Safety & Eligibility. Plans owns the resulting Plan Version and must revalidate current Safety authority before approval/activation; practitioner-authored content cannot operate as an implicit Safety bypass.

At v0.36.0, `HSP-PT-017` directly challenges the accepted `HSP-WD-023` fulfilment shorthand. Product Law distinguishes generated/review/approval lifecycle states and promises access to the delivered Plan, so a generated immutable Plan Version cannot universally equal Request fulfilment. `HSP-WH-011` proposes the refinement: fulfilment occurs only when one final Plan Version has passed every required pre-delivery gate and is durably delivered/made available under governed participant access, with exactly one corresponding Entitlements consequence. Review-gated Requests may contain multiple immutable pre-fulfilment versions but exactly one fulfilled deliverable.

At v0.37.0, `HSP-WH-011` is accepted as `HSP-WD-031`, explicitly refining both the `HSP-WD-011` fulfilled definition and `HSP-WD-023` fulfilment shorthand without changing the minimal Request state set. `HSP-PT-018` pressure-tests reviewer loss, reassignment and prolonged pending review. The architecture passes: reviewer assignment is Professional Care workflow, R1 remains open and unconsumed during legitimate reassignment, stale reviewer access must expire, and provider capacity failure is not `unfulfillable`. `HSP-UPD-006` records the unresolved participant-facing service/commercial promise for maximum pending duration, authorised cancellation and remedy.

At v0.38.0, `HSP-PT-019` attacks same-lineage Plan concurrency: two independently valid Requests can each be exactly-once and still produce an invalid result if both supersede the same predecessor. The test therefore opens `HSP-WH-012`: replacement/adjustment Requests must bind to the Plan lineage/predecessor they intend to advance, and fulfilment must revalidate that current-head authority so only one competing Request can successfully advance the same predecessor. Stale competitors require governed non-fulfilment/review/rebase handling rather than silent overwrite or merge.

At v0.39.0, `HSP-WH-012` is accepted as `HSP-WD-032`. `HSP-PT-020` pressure-tests cancellation racing stale generation/review completion and passes: once cancellation is durably terminal, stale work cannot fulfil or consume the Plan right; if fulfilment wins first, later cancellation cannot rewrite history. The test also exposes a distinct upstream commercial ambiguity: locked `DEC-045` ends Plan refunds after generation, while `HSP-WD-031` permits review-gated Plans to be generated before delivery/fulfilment. `HSP-UPD-007` records the required Product/Commerce clarification rather than silently equating refund, generation and fulfilment boundaries.

At v0.40.0, a superseding clarification is added to `HSP-WD-010` so its older “Plan Version only on fulfilment” wording no longer conflicts with accepted `HSP-WD-031` review-gated pre-fulfilment versioning. `HSP-PT-021` pressure-tests participant-owned Plan-input changes during in-flight generation. It opens `HSP-WH-013`: edits require explicit applicability semantics and never silently mutate an immutable Generation Basis. Material current-Request intent changes block fulfilment from the stale basis; future-only/unrelated edits do not. `HSP-UPD-008` records the remaining Product/Commerce question around pre-fulfilment change-of-intent versus locked `DEC-038` re-personalisation and `DEC-045` refund timing.

At v0.41.0, `HSP-WH-013` is accepted as `HSP-WD-033`. An upstream-derived cadence clarification is added: ordinary progress logging is explicitly decoupled from Plan regeneration; current locked Product Law allows daily/weekly progress entries but ordinary Plan adjustments remain monthly, entitlement-period gated, trend-based and check-in dependent. Weekly ordinary Plan adjustment is not silently inferred and would require an explicit future Product/entitlement rule. Safety-critical new information remains an immediate Safety path rather than an ordinary adjustment trigger.

At v0.42.0, `HSP-PT-022` closes the planned pressure-test suite by proving the correction-versus-re-personalisation boundary. A delivered Plan that was wrong relative to its authoritative basis/rules follows governed correction/replacement lineage without consuming a new ordinary entitlement; a Plan that was correct when delivered but later becomes undesirable because participant preference/progress changed follows the applicable new-purchase or qualifying membership/add-on/review-entitlement path and does not regenerate on profile edit. No new architecture doctrine is required. The pre-JIT discovery grill therefore reaches an explicit STOP condition: further ordinary scenario expansion is not recommended absent new evidence, contradiction, scope change or JIT-discovered seam.
