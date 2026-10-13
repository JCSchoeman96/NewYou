# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.5.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.5.0`
- **Date:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.4.0.md`
- **Purpose:** append operator concurrency, pilot admission/counting, measurement, pause/resume, release progression and degradation semantics.
- **Scope:** all predecessor scope plus the FP-006 release/evidence boundary.
- **Explicit non-goals:** unchanged; no implementation, no admission algorithm selection, no thresholds beyond current Product Law, no authority amendment, no PR.
- **External evidence dates:** none added.
- **Current overall disposition:** `IN_PROGRESS / FP-006 RELEASE SEMANTICS BROADLY PRESSURE-TESTED / PILOT-ADMISSION GAP NARROWED / NOT FROZEN`.

---

# 0. Append-only successor rule

Reasoning chain:

```text
v0.1.0
→ v0.2.0
→ v0.3.0
→ v0.4.0
→ this v0.5.0 append
```

All predecessors remain historical reasoning evidence.

This version adds `OPS-PT-079...OPS-PT-111`. It adds no new `OPS-UPD`; instead it narrows and strengthens existing `OPS-UPD-001` and records downstream-only gaps.

---

# 45. Independent lifecycle dimensions for release operations

Do **not** model “pilot status” as one universal lifecycle.

At least these dimensions remain independent:

## 45.1 Product/commercial availability lifecycle

Current Product Law already uses:

```text
draft → internal → pilot → public → paused → retired
```

That is product availability, not a count of paid pilot participants.

## 45.2 Pilot expansion stage

The governed progression is conceptually:

```text
internal validation
→ first 10 paid participants
→ review
→ expansion toward 25
→ review
→ maximum 50 first paid pilot
→ limited public
→ general public decision
```

This is an evidence/release stage, not Commerce payment state.

## 45.3 Scoped stop controls

A stop can target one capability without rewriting product history or release evidence, for example:

```text
stop new sales
stop new payment initiation
stop new assessment admission
stop new personalised-Plan generation
safety-pause affected Plans
stop cohort expansion
stop optional communications
withdraw one content version
pause one provider-dependent capability
read-only / limited-capability / full-maintenance when justified
```

A stop-set is not itself the product lifecycle.

## 45.4 Incident / blocker state

An incident or open blocker is evidence/reason for a stop or release decision. It is not equivalent to the stop state and does not become source business truth.

## 45.5 Participant obligation state

Already accepted paid obligations continue to be governed by Commerce/Entitlements/Temperament/Safety/Plans even if **new admission** stops. Admission pause must not silently cancel existing obligations.

---

# 46. Operator-concurrency pressure tests

## OPS-PT-079 — Support and Finance act concurrently on the same payment problem

**Scenario class:** concurrency / operator / financial

**Why it matters**  
Role handoff must not become “last operator wins.”

**Relevant current authority**  
Commerce ownership; Work is attention not authority; `OPS-UPD-003`.

**Owning Domain(s)**  
Commerce for payment/refund; Entitlements for access consequences.

**Preconditions**  
Support has opened/escalated work; Finance begins investigation while Support still has a stale view.

**Exact scenario / timeline**

```text
Support reads unresolved state
→ Finance reconciles/commits owner transition
→ Support submits stale request
→ source owner revalidates current state and rejects/no-ops/reinterprets lawfully
```

**Expected invariant(s)**

- work assignment does not lock or own Commerce;
- current source state beats stale operator page;
- duplicate consequence remains impossible;
- participant-facing note/status refreshes from source truth.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-003` for who may issue which command.

**Evidence still required**  
Deterministic interleaving proof.

**Follow-up**  
None.

---

## OPS-PT-080 — Two Support agents work the same case

**Scenario class:** concurrency / operator

**Why it matters**  
Case assignment can reduce duplicate effort but cannot be a hard business correctness mechanism.

**Relevant current authority**  
Operating Model Work projection; Architecture current-state guards.

**Owning Domain(s)**  
Underlying source Domain(s).

**Preconditions**  
Two agents can see/claim the same operational work.

**Exact scenario / timeline**

- assignment/claim may coordinate responsibility;
- each consequential action still invokes owner policy/current state;
- one agent resolving the work projection does not certify source outcome if source remains unresolved;
- duplicate harmless participant communication is controlled separately from business idempotency.

**Expected invariant(s)**  
No double refund/grant/reset simply because two operators worked simultaneously.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none beyond `OPS-UPD-003`.

**Evidence still required**  
Work projection refresh/assignment rules and duplicate-command proof.

**Follow-up**  
None.

---

## OPS-PT-081 — Participant self-service action occurs during staff investigation

**Scenario class:** concurrency / operator / recovery

**Why it matters**  
A participant may cancel, update data, recover an account, choose a refund or change a relevant fact while staff are viewing the old state.

**Relevant current authority**  
Architecture current-authority rule; source Domain lifecycles.

**Owning Domain(s)**  
The Domain owning the participant self-service transition.

**Preconditions**  
Staff has stale page/work context.

**Exact scenario / timeline**

```text
staff opens state t0
→ participant commits lawful self-service transition t1
→ staff command at t2
→ owner revalidates current state/policy
```

**Expected invariant(s)**

- staff view does not freeze participant authority;
- stale command cannot undo participant action unless an explicit lawful transition permits it;
- Audit/work chronology is evidence only.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Stale-action rejection/re-evaluation proof.

**Follow-up**  
None.

---

## OPS-PT-082 — Stale admin page submits an old correction

**Scenario class:** concurrency / operator / correction

**Why it matters**  
Optimistic UI state must never become durable correction authority.

**Relevant current authority**  
Frontend authoritative-transition doctrine; Architecture; Product correction law.

**Owning Domain(s)**  
Source owner.

**Preconditions**  
Operator page was loaded before another valid state transition.

**Exact scenario / timeline**  
Command includes explicit target/expected context; owner validates current state and either lawfully applies, rejects as stale, or returns already-resolved result.

**Expected invariant(s)**

- button enabled at mount time is not permission at submit time;
- stale correction cannot overwrite newer truth;
- no universal client-side lock is treated as correctness.

**Semantic disposition:** `PASS`

**Proof route:** `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Stale-version/interleaving proof.

**Follow-up**  
None.

---

## OPS-PT-083 — One operator pauses while another resumes

**Scenario class:** concurrency / release / operator

**Why it matters**  
A stale resume must not defeat a new safety/security/technical stop.

**Relevant current authority**  
`DEC-291`; Product rollback/re-entry doctrine; narrowest safe rollback.

**Owning Domain(s)**  
Release-control authority composes governed product/commercial, clinical/safety and technical/operations authority; source Domains remain owners of business truth.

**Preconditions**  
A scoped stop and a resume/re-entry action can overlap.

**Exact scenario / timeline**

```text
resume candidate checks blockers at t0
→ authorised safety/technical stop becomes effective at t1
→ stale resume submits at t2
→ current blocker/stop authority wins; resume fails closed
```

**Expected invariant(s)**

- immediate scoped stop can narrow capability without waiting for unrelated approval;
- resume cannot be “last write wins”;
- re-entry requires current blocker closure and evidence;
- stop history is preserved.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE` + `RELEASE_ONLY`

**Upstream delta:** `OPS-UPD-003` for named human authority.

**Evidence still required**  
Release-control lifecycle and concurrency proof.

**Follow-up**  
Pause/resume scenarios below.

---

## OPS-PT-084 — Operator requests refund while provider reconciliation completes

**Scenario class:** concurrency / financial / operator

**Why it matters**  
Refund eligibility/outcome must be evaluated against current Commerce truth, not the state visible when the form opened.

**Relevant current authority**  
Commerce lifecycle; `OPS-PT-019...022`; provider ambiguity doctrine.

**Owning Domain(s)**  
Commerce.

**Preconditions**  
Payment/refund status unresolved; human and provider-driven transitions overlap.

**Exact scenario / timeline**

- Commerce serialises/interprets lawful transition from current state;
- unknown provider outcome remains unresolved rather than blindly repeated;
- one refund obligation cannot execute twice;
- Entitlements follows the resulting source-specific consequence.

**Semantic disposition:** `PASS`

**Proof route:** `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-002` where duplicate/excess collection applies; `OPS-UPD-003` for operator authority.

**Evidence still required**  
Provider + deterministic race proof.

**Follow-up**  
None.

---

# 47. Pilot admission and cohort-counting pressure tests

## OPS-PT-085 — First qualifying paid participant

**Scenario class:** pilot / release / financial

**Why it matters**  
The first real participant is the first point where internal validation becomes real paid-pilot evidence.

**Relevant current authority**  
`DEC-280`, `DEC-281`, `DEC-307...DEC-312`; Roadmap FP-006 paid-pilot contract.

**Owning Domain(s)**  
Commerce owns verified payment; IAM owns participant identity; Analytics derives evidence; release authority owns stage decision.

**Preconditions**  
All paid-pilot readiness gates pass and the relevant stage is open.

**Exact scenario / timeline**  
A real target adult woman makes a verified actual payment under the real catalogue/commercial contract.

**Expected invariant(s)**

- no staff/free/manual grant counts;
- participant evidence fields are captured under the versioned metric contract;
- payment/entitlement truth remains with source owners.

**Questions under test**  
What exact event consumes one admission place?

**Analysis**  
The person and paid-demand qualification are governed. The exact **admission-slot commitment event** remains `OPS-UPD-001`.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` then `JIT`/`CONTROLLED_LIVE`.

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
Atomic admission boundary.

**Follow-up**  
Boundary races.

---

## OPS-PT-086 — Participant 10 / 11 race the first review gate

**Scenario class:** pilot / concurrency / financial

**Why it matters**  
A dashboard count cannot prevent simultaneous real payments from crossing a capped stage.

**Relevant current authority**  
First-10 Product contract; `DEC-281`; `OPS-UPD-001`.

**Owning Domain(s)**  
Commerce + release admission authority; Analytics is derived only.

**Preconditions**  
Nine qualifying participants admitted; two eligible purchases/payments overlap.

**Expected invariant(s)**

- stage cap does not depend on UI disabling or delayed analytics;
- provider callback order is not release authority;
- participant 11 cannot be silently accepted beyond governed cap without an explicit rule;
- already accepted obligations cannot be abandoned.

**Questions under test**  
What reserves/commits the tenth place, and what lawful outcome applies to the eleventh in-flight purchase?

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
Admission lifecycle and concurrency proof.

**Follow-up**  
Same issue at later boundaries.

---

## OPS-PT-087 — Participant 25 / 26 race the next review boundary

**Scenario class:** pilot / concurrency / release

**Why it matters**  
The same admission invariant must generalise without assuming 25 is a hard capacity service limit rather than a review point.

**Relevant current authority**  
Product staged rollout approximately 10 → 25 → 50 review points.

**Owning Domain(s)**  
Release admission authority + Commerce evidence.

**Preconditions**  
Stage is open toward 25 and two qualifying admissions overlap.

**Expected invariant(s)**  
Review boundary semantics are explicit; implementation must not invent whether exactly 25 is a hard stop or a target review point under concurrent admission.

**Analysis**  
The Product language uses “toward 25” / review, while first-pilot maximum is 50. Exact concurrent boundary treatment still belongs in `OPS-UPD-001`; do not hard-code “26 is impossible” from wording alone.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION`.

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
Explicit review-point admission semantics.

**Follow-up**  
Maximum-50 boundary.

---

## OPS-PT-088 — Participant 50 / 51 race the first-pilot maximum

**Scenario class:** pilot / concurrency / release

**Why it matters**  
Unlike “toward 25,” current Product calls 50 the maximum first paid pilot. The cap must survive concurrency.

**Relevant current authority**  
`DEC-281`; FP-006.

**Owning Domain(s)**  
Release admission authority + Commerce.

**Preconditions**  
Forty-nine qualifying admissions and two in-flight candidates.

**Expected invariant(s)**

- no more than the governed maximum are lawfully accepted into the first paid pilot;
- uncertain payment cannot be guessed merely to fill the last place;
- legitimate in-flight customer obligation at the boundary is governed explicitly.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
Hard-cap atomicity and customer-remedy rule.

**Follow-up**  
None.

---

## OPS-PT-089 — Payment is ambiguous at the stage boundary and later reconciles successful

**Scenario class:** pilot / financial / recovery / concurrency

**Why it matters**  
“Paid-demand evidence requires verified actual payment,” but an eventual success may arrive after the stage is paused/reviewed.

**Relevant current authority**  
FP-006 paid-demand contract; Commerce reconciliation; `OPS-UPD-001`.

**Owning Domain(s)**  
Commerce; release admission authority.

**Preconditions**  
Payment initiated while stage open; outcome unresolved when gate pauses/closes; later reconciliation proves success.

**Expected invariant(s)**

- ambiguous does not count as verified paid evidence yet;
- later true success cannot be falsified;
- Product must state whether the participant was already admitted/owed service or requires a capped-stage remedy.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
In-flight admission rule and provider proof.

**Follow-up**  
None.

---

## OPS-PT-090 — Failed payment

**Scenario class:** pilot / financial

**Why it matters**  
Checkout interest is evidence but not a paid participant.

**Relevant current authority**  
FP-006 paid-demand contract.

**Owning Domain(s)**  
Commerce; Analytics derives funnel evidence.

**Preconditions**  
Payment attempt fails authoritatively.

**Expected invariant(s)**

- does not count as a qualifying paid participant;
- remains funnel/payment-friction evidence;
- no entitlement/admission is fabricated.

**Semantic disposition:** `PASS`

**Proof route:** `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Metric/event implementation.

**Follow-up**  
None.

---

## OPS-PT-091 — Qualifying participant later receives a refund or withdraws

**Scenario class:** pilot / financial / measurement

**Why it matters**  
Current law requires refund evidence but does not explicitly say whether a once-lawfully admitted/refunded participant is removed from the historical 10/25/50 cohort count or only from a current-active view.

**Relevant current authority**  
FP-006 cohort and refund contract; `OPS-UPD-001`.

**Owning Domain(s)**  
Commerce owns refund; release cohort membership/count semantics require Product authority; Analytics derives metrics.

**Preconditions**  
Participant was a genuine verified payer and later refunds/withdraws.

**Expected invariant(s)**

- refund remains visible in evidence and reason category;
- staff cannot erase the participant from history to improve metrics;
- historical cohort membership and current active participation are separate dimensions.

**Questions under test**  
Does a refund free a pilot admission place for another participant? Does the participant remain in first-10 outcome denominators?

**Analysis**  
Current Product Law does not answer these count/replacement semantics clearly enough. This belongs inside the existing pilot-admission delta rather than a new one.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION`

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
Historical cohort-membership/replacement rule.

**Follow-up**  
Refine `OPS-UPD-001` below.

---

## OPS-PT-092 — Duplicate successful collection for one participant/order

**Scenario class:** pilot / financial / measurement

**Why it matters**  
Duplicate money movements must not inflate paid-participant count or purchase conversion.

**Relevant current authority**  
First 10 = ten women; duplicate charge integrity rule; `OPS-UPD-002`.

**Owning Domain(s)**  
Commerce; Analytics.

**Expected invariant(s)**

- one human participant cannot count twice merely because money was collected twice;
- excess collection is correction/refund evidence, not extra demand;
- accepted purchase identity and participant identity remain explicit.

**Semantic disposition:** `PASS`

**Proof route:** `CONTROLLED_LIVE` + `EMPIRICAL_PROVIDER`

**Upstream delta:** `OPS-UPD-002` for the money remedy only.

**Evidence still required**  
Deduplicated cohort metric derivation.

**Follow-up**  
None.

---

## OPS-PT-093 — Staff/test Account makes a payment

**Scenario class:** pilot / measurement / abuse

**Why it matters**  
Real money alone is not enough if the actor is not a real target participant.

**Relevant current authority**  
FP-006 first-10 contract excludes staff/test evidence from paid demand.

**Owning Domain(s)**  
IAM identifies actor/account; Commerce records truthful payment; Analytics excludes from qualifying cohort by governed rule.

**Expected invariant(s)**  
Payment history remains true but does not count toward first-10 paid-demand evidence.

**Semantic disposition:** `PASS`

**Proof route:** `DOCUMENTARY` + `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Cohort eligibility classification.

**Follow-up**  
None.

---

## OPS-PT-094 — Complimentary, sponsored, gift-recipient, 100%-discount or manual-grant access

**Scenario class:** pilot / measurement / financial

**Why it matters**  
Access can be commercially valid without proving self-paying demand.

**Relevant current authority**  
FP-006 paid-demand exclusions and first-10 “self-paying” rule.

**Owning Domain(s)**  
Commerce/Entitlements own source truth; Analytics applies cohort qualification.

**Expected invariant(s)**

- complimentary/sponsored/manual entitlement/100%-discount do not count as paid demand;
- a gift recipient is not a self-paying participant merely because another person paid;
- all may still produce useful operational/safety evidence if labelled separately;
- purchaser and participant remain distinct.

**Semantic disposition:** `PASS`

**Proof route:** `DOCUMENTARY` + `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Source/provenance classification.

**Follow-up**  
None.

---

## OPS-PT-095 — Discounted genuine purchase

**Scenario class:** pilot / measurement / financial

**Why it matters**  
Discount must not be confused with free demand or full-list-price willingness.

**Relevant current authority**  
FP-006 paid-demand contract.

**Expected invariant(s)**

- counts when actual positive payment is verified and participant otherwise qualifies;
- list price, promotion and actual amount remain distinct;
- stated willingness to pay full price remains weaker evidence than actual purchase.

**Semantic disposition:** `PASS`

**Proof route:** `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Metric capture.

**Follow-up**  
None.

---

## OPS-PT-096 — Same participant makes multiple qualifying purchases

**Scenario class:** pilot / measurement

**Why it matters**  
The pilot progression is participant-count based, while product/revenue evidence may be purchase based.

**Relevant current authority**  
First 10 = ten genuine self-paying adult women; purchaser/participant separation.

**Expected invariant(s)**

- one participant is one human participant for cohort headcount;
- multiple valid purchases remain multiple Commerce facts/revenue/product observations;
- product-specific denominators may include the relevant purchase/pathway, but first-10 headcount is not inflated.

**Semantic disposition:** `PASS`

**Proof route:** `DOCUMENTARY` + `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Canonical participant identity mapping and metric-definition version.

**Follow-up**  
None.

---

## OPS-PT-097 — New admissions pause while checkout/payment is already in flight

**Scenario class:** pilot / release / financial / concurrency

**Why it matters**  
This is the concrete commercial form of `OPS-UPD-001`.

**Relevant current authority**  
Narrow rollback; first-pilot cap; Commerce payment ambiguity.

**Expected invariant(s)**

- stop_new_sales/payment-initiation applies at a defined boundary;
- already-accepted/in-flight participant obligation is not guessed;
- late provider success does not silently overrun cap or get discarded;
- existing participants continue owed safe service where permitted.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
Admission/payment in-flight rule.

**Follow-up**  
None.

---

# 48. Pilot measurement contract pressure tests

## OPS-PT-098 — Operational support-burden metrics are versioned before first paid participation

**Scenario class:** pilot / measurement / operator

**Why it matters**  
“Support contacts” and “support minutes” are easy to redefine after seeing the data.

**Relevant current authority**  
FP-006 requires versioned numerator, denominator, qualifying event, window, exclusions, missing-data treatment, cohort and metric version before first paid participation.

**Owning Domain(s)**  
Source Domains own facts; Analytics owns derived analytical facts/projections; operator/work tooling may supply operational observations without becoming business authority.

**Working metric contract**

| Metric | Numerator / unit | Denominator / population | Time basis | Source facts | Correction / limits |
|---|---|---|---|---|---|
| Participants needing support | distinct governed pilot participants with ≥1 qualifying human support interaction in window | governed cohort participants eligible for the relevant observation window | cohort + named window | support/work interaction evidence + IAM participant identity | factual corrections may recompute under same definition version; automated notices do not count as human support |
| Support contacts per participant | count of versioned `support_interaction` units, not raw messages/clicks | participants in stated cohort (show distribution plus total) | cohort/window | operational interaction evidence | interaction-unit definition frozen prospectively; avoid inflating one conversation into many contacts |
| Support minutes | active human handling minutes attributable to participant issue, excluding queue/wait time | report total + per participant; no success threshold yet | cohort/window | operator handling evidence | timer/manual method disclosed; approximation limitations visible |
| Issue category | count of interactions/cases by versioned non-exclusive or primary category rule | qualifying support interactions | cohort/window | operational category + source truth references | taxonomy versioned; reclassification provenance retained |
| Manual intervention | participant/pathway with a human consequential intervention beyond explanation/ordinary support | relevant cohort/pathway | cohort/window | owner-command evidence + work context | distinguish harmless assistance from business-state intervention |
| Developer intervention | participant/incident needing developer/platform action to restore/diagnose service | relevant cohort/pathway | cohort/window | incident/technical evidence linked minimally | developer access to sensitive data is not implied |
| Expert/clinical intervention | participant/pathway needing governed expert/clinical action | relevant eligible pathway | cohort/window | Safety/Professional/approved expert outcome | Support routing alone does not count as clinical decision |

**Expected invariant(s)**

- Analytics/work projection does not become owner of underlying refund/payment/safety truth;
- metric definition changes are prospective;
- counts accompany percentages;
- no time threshold is invented before observation.

**Questions under test**  
Is a Support “contact” each message, each conversation, each case or each day?

**Analysis**  
Product intentionally requires the operational unit to be versioned before first paid participation rather than freezing one universal historical definition in Product Law. Pre-JIT can supply the constraints above; FP-006 Final Contract/JIT must choose and freeze the exact interaction-unit definition before live evidence begins.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Exact v1 metric definitions before first paid participant.

**Follow-up**  
Record downstream gap, not Product gap.

---

## OPS-PT-099 — Assessment, health-onboarding and Plan operational-funnel metrics

**Scenario class:** pilot / measurement

**Why it matters**  
The current Product denominator rules deliberately prevent denominator shopping.

**Relevant current authority**  
Product §21T.7 / Roadmap FP-006.

**Working contract from current authority**

| Metric | Numerator | Denominator | Time basis | Authoritative source facts | Correction / limits |
|---|---|---|---|---|---|
| Assessment completion | valid assessment submission + governed result successfully produced | starters = first answer persisted/submitted | attempt/cohort window | Temperament | do not count page opens; consumption conflict `OPS-UPD-004` does not change completion formula |
| Health onboarding completion | participants providing sufficient facts for deterministic eligibility | paid participants entitled to personalised-plan pathway who reach required onboarding; assessment-only excluded | pathway/cohort | Health Records + Safety outcome | `general_wellness_only` is a legitimate eligibility outcome, not completion failure |
| Plan delivery success | successful governed personalised-Plan deliveries | eligible paid personalised-Plan fulfilment obligations reaching delivery path under the frozen metric definition | fulfilment/cohort | Plans + Entitlements/Safety references | distinguish terminal governed component-refund closeout from technical delivery failure |
| Plan activation | genuine post-delivery participant action opening/beginning/confirming first planned action/day | successfully delivered personalised Plans | first seven days from successful delivery under current Product meaning | Plans/access + progress facts | generation, notification or passive single open alone insufficient |
| Meaningful seven-day use | engagement on ≥3 distinct days including ≥1 after Day 1 | successfully delivered personalised Plans in applicable window | first seven days after delivery | Habits/Progress + Plans delivery | no invented engagement from notification/generation |
| General Wellness pathway | correctly routed GW outcomes and later retain/refund choice outcome | applicable paid personalised-plan-pathway participants reaching GW | governed decision/choice window | Safety + Commerce/Entitlements | not counted as failed personalised-plan activation; `OPS-UPD-007` blocks exact choice-clock start |

**Expected invariant(s)**  
No metric is allowed to use an easier denominator retroactively.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `CONTROLLED_LIVE`

**Upstream delta:** existing `OPS-UPD-004` and `OPS-UPD-007` only where their seams apply.

**Evidence still required**  
Exact metric version and analytics/event mapping.

**Follow-up**  
None.

---

## OPS-PT-100 — Day-7 / Day-30 / Day-90 evidence timing

**Scenario class:** pilot / measurement / release

**Why it matters**  
Evidence maturity must not be overstated or used to manufacture a release delay.

**Relevant current authority**  
Product §21T.8; North Star pilot evidence; FP-006.

**Working contract**

| Evidence point | Qualifying population | Time anchor | What it may support | What it must not claim |
|---|---|---|---|---|
| Day 7 | participants reaching the relevant paid delivered experience under the versioned metric contract | product/pathway-specific delivered/start anchor fixed prospectively before first participant | comprehension, safety, relevance, practicality, activation, initial use, perceived value | sustainable habits / long-term durability |
| Day 30 | applicable participants reaching Day 30 | same cohort-specific anchor family | continuation, reuse, interruptions, return, continuing usefulness | guaranteed long-term behaviour change |
| Day 90 | applicable participants reaching Day 90 | same versioned anchor family | directional durability/recovery, personally appropriate behaviours | prerequisite for every earlier cohort expansion |

Do not manufacture setbacks. Recovery denominator includes only participants who experienced/reported a relevant interruption; participants with no interruption are reported separately.

**Expected invariant(s)**

- Day-90 evidence is not required before every stage expansion;
- each participant/pathway's clock anchor is versioned before live collection;
- missing/not-yet-mature evidence is shown as such, not zero/failure.

**Analysis**  
Product governs interpretation strongly and deliberately requires metric window/qualifying-event versioning. Exact per-product anchor is an FP-006 metric-definition decision before first paid evidence, not a new Product threshold.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Metric-definition v1 anchors before live pilot.

**Follow-up**  
None.

---

## OPS-PT-101 — Perceived value, survey response and refund evidence

**Scenario class:** pilot / measurement / financial

**Why it matters**  
Small-cohort percentage claims can be misleading if non-response/refund types are hidden.

**Relevant current authority**  
FP-006 Product evidence contract.

**Working contract**

- positive value/relevance target remains ≥70%; controlled-pilot interpretation also requires ≥70% survey response;
- report counts + percentages + non-response;
- price-value asks “Considering what you paid…” separately from generic usefulness;
- discounted participants' stated full-price intent is weaker evidence than purchase;
- refund reasons use the governed taxonomy;
- first-10 dissatisfaction stop signal: 0–1 not strong negative, 2 review before expansion, ≥3 pause pending investigation; technical/payment corrections and eligibility refunds do not count as dissatisfaction refunds.

**Expected invariant(s)**  
No refund reason may be recoded after the fact simply to avoid the pause threshold.

**Semantic disposition:** `PASS`

**Proof route:** `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Survey instrument wording/version and refund-category application proof.

**Follow-up**  
None.

---

## OPS-PT-102 — Founder/staff effort and variable fulfilment costs

**Scenario class:** pilot / measurement / operational

**Why it matters**  
Pilot economics can be falsely improved by hiding unpaid founder labour or manual fulfilment.

**Relevant current authority**  
FP-006 requires variable economics + founder/staff effort without inventing hard CAC/LTV/margin thresholds.

**Working contract**

| Measure | Unit | Population/time | Source | Limitation |
|---|---|---|---|---|
| Founder/staff effort | active handling minutes/hours by role/category | cohort/window | operational evidence | distinguish active effort from elapsed waiting; disclose estimation method |
| Variable fulfilment cost | actual variable provider/operational cost attributable to cohort/product where measurable | cohort/product | Commerce/provider invoices/operational facts | do not allocate fixed costs as if variable without method disclosure |
| Support/fulfilment cost | versioned labour-cost model × observed effort plus direct variable costs | cohort/product | derived Analytics/finance evidence | model assumptions versioned; not accounting authority |
| Payment/provider fees | actual/estimated fees attributable to accepted commercial transactions | cohort | Commerce/provider evidence | provider statement remains evidence; reconcile to Commerce |

**Expected invariant(s)**  
No success threshold is invented merely because measurement exists.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `CONTROLLED_LIVE`

**Upstream delta:** none.

**Evidence still required**  
Operational capture method and finance reconciliation.

**Follow-up**  
None.

---

## OPS-PT-103 — Acquisition/channel evidence at limited-public release

**Scenario class:** pilot / release / measurement

**Why it matters**  
Invited warm-pilot conversion cannot be represented as ordinary funnel or CAC proof.

**Relevant current authority**  
FP-006 paid-pilot contract.

**Working contract**  
During controlled first-10/25/50, record acquisition source/exposure but do not treat deliberately invited conversion as ordinary visitor-to-purchase conversion. At limited-public release begin channel spend, attributed purchasers, CAC, revenue, refunds, fees, support/fulfilment and contribution measurement under versioned attribution rules.

**Expected invariant(s)**  
Warm reach and book/media familiarity remain visible confounders; acquisition attribution never becomes purchase authority.

**Semantic disposition:** `PASS`

**Proof route:** `CONTROLLED_LIVE` + `RELEASE_ONLY`

**Upstream delta:** none.

**Evidence still required**  
Versioned attribution contract when limited-public activates.

**Follow-up**  
None.

---

# 49. Pause / resume / safe-stop pressure tests

## OPS-PT-104 — “Pause the platform” request is decomposed into scoped stop dimensions

**Scenario class:** release / recovery / operator

**Why it matters**  
A universal pause can unnecessarily deny owed service or fail to stop the actual unsafe capability.

**Relevant current authority**  
Product rollback modes; `DEC-264`, `DEC-291`; narrowest safe rollback.

**Expected invariant(s)**

- operator names the capability being stopped;
- existing obligations are evaluated separately;
- pause has reason/evidence/authority/time and re-entry criteria;
- resume revalidates current blockers.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE` + `RELEASE_ONLY`

**Upstream delta:** `OPS-UPD-003` for named human authority; `OPS-UPD-001` for in-flight admission boundary.

**Evidence still required**  
Concrete release-control lifecycle.

**Follow-up**  
Incident classes below.

---

## OPS-PT-105 — Payment provider outage

**Scenario class:** degradation / financial / release

**Why it matters**  
Provider outage should not make NewYou guess payments or unnecessarily stop participants with already-valid access.

**Expected behaviour**

- new provider-dependent payment initiation/reconciliation may pause/degrade;
- unresolved outcomes remain unresolved and discourage duplicate payment;
- new paid admissions likely pause when authoritative payment cannot be verified;
- already-valid Entitlements and safe owed fulfilment continue where independent of provider;
- release expansion may pause if backlog/integrity cannot be reviewed.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`

**Upstream delta:** none beyond `OPS-UPD-001` at in-flight stage boundary.

**Evidence still required**  
OQ-004 provider failure/recovery evidence.

**Follow-up**  
Degradation matrix.

---

## OPS-PT-106 — Severe safety concern

**Scenario class:** safety / release / recovery

**Why it matters**  
Safety authority must be able to narrow dangerous fulfilment immediately without waiting for commercial/product convenience.

**Expected behaviour**

- immediate scoped safety stop/pause of affected Plan/content/pathway;
- stop new affected fulfilment/admission if necessary;
- unaffected public/account/payment capabilities may remain if safe;
- participant remedies/communications proceed under approved safety policy;
- re-entry requires clinical/safety blocker closure.

**Semantic disposition:** `PASS`

**Proof route:** `EXPERT_REVIEW` + `PHASE8_EXECUTABLE` + `RELEASE_ONLY`

**Upstream delta:** none.

**Evidence still required**  
OQ-005/OQ-008 and affected-scope proof.

**Follow-up**  
None.

---

## OPS-PT-107 — Privacy/security incident

**Scenario class:** privacy / security / release

**Why it matters**  
The safe response may be to revoke sessions/privileges or disable a narrow feature, not automatically erase business state or take every public page offline.

**Expected behaviour**

- immediate authority narrowing/revocation where required;
- affected data/action surface pauses;
- preserve evidence and incident ownership;
- new admissions may pause if participant trust/protected-data path is compromised;
- unrelated safe public/read-only capability may continue if approved;
- re-entry requires incident remediation/evidence.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `PHASE8_EXECUTABLE` + `RELEASE_ONLY`

**Upstream delta:** none.

**Evidence still required**  
`OQ-035`, `OQ-037`, `OQ-038`, incident runbook/proof.

**Follow-up**  
None.

---

## OPS-PT-108 — One bad/unsafe content version is discovered

**Scenario class:** safety / content / release

**Why it matters**  
One version defect should not require “pause the platform” if exact affected delivery can be withdrawn/replaced.

**Expected behaviour**

- Content owner withdraws/corrects exact version;
- affected Plans/content delivery re-evaluate through owning Domains;
- only impacted capability/version/language stops where possible;
- historical provenance preserved;
- new release/admission only pauses if the defect affects required core journey and no safe replacement exists.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Content publication/correction `OQ-016` and affected-dependency mapping.

**Follow-up**  
None.

---

## OPS-PT-109 — Reconciliation backlog or support load becomes operationally unsafe

**Scenario class:** release / degradation / operator

**Why it matters**  
Capacity/support pressure can justify pausing new admissions even without a source-truth defect.

**Relevant current authority**  
FP-006 evidence-led expansion; narrow rollback; named operations authority.

**Expected behaviour**

- current participant obligations remain visible and prioritised;
- new admissions/cohort expansion may pause before existing service is abandoned;
- backlog/support load is evidence, not a reason to mutate payment/entitlement truth;
- resume only after capacity/recovery criteria are met.

**Questions under test**  
Does Product need a fixed “X support minutes = pause” threshold now?

**Analysis**  
No. Product explicitly says measure support burden before setting a time threshold. Operators still need authority to pause expansion based on material operational risk; exact runbook thresholds may be added from controlled evidence later.

**Semantic disposition:** `PASS`

**Proof route:** `CONTROLLED_LIVE` + `RELEASE_ONLY`

**Upstream delta:** none.

**Evidence still required**  
Observed pilot burden and versioned re-entry criteria.

**Follow-up**  
None.

---

## OPS-PT-110 — Stage progression, pause, resume and re-entry decision

**Scenario class:** pilot / release / operator

**Why it matters**  
One authority must not waive another authority's blocker; historical evidence must not be confused with current blocker state.

**Relevant current authority**  
`DEC-288...DEC-291`; Product §21L.21–21L.24; FP-006.

**Expected lifecycle intent**

```text
current stage open
→ evidence review
→ proceed / iterate / repeat / pause / rollback
→ remediation + blocker closure
→ re-entry review
→ next stage only with required current authorities
```

**Guards**

- product/commercial, clinical/safety and technical/operations authorities remain separate;
- legal/privacy/security/content gates apply where current release stage requires them;
- immediate safety/technical narrowing can occur without waiting for expansion approval;
- resume/expansion requires current blocker closure and recorded evidence/re-entry criteria;
- Day-90 maturity is not manufactured as a universal expansion prerequisite.

**Expected invariant(s)**  
Dashboard green does not waive a blocker; one historical incident does not permanently block release after current integrity is restored and re-entry evidence passes.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `CONTROLLED_LIVE` + `RELEASE_ONLY`

**Upstream delta:** `OPS-UPD-003` for exact named actors/scopes.

**Evidence still required**  
FP-006 sign-off/runbook contract and controlled-live evidence.

**Follow-up**  
None.

---

# 50. Degradation matrix

## OPS-PT-111 — Dependency-by-dependency degradation classification

**Scenario class:** degradation / recovery / release

**Why it matters**  
A generic “platform up/down” state is too coarse. Dependencies fail independently and must not become hidden business authority.

**Relevant current authority**  
Architecture: correct refusal/bounded waiting/reduced freshness over fabricated success; Product graceful degradation and rollback.

| Dependency / failure | Core journey classification | New admissions | Existing owed service | Human intervention | Full release stop? |
|---|---|---|---|---|---|
| Payment provider | affected payment/reconciliation action pauses or remains unresolved | **pause provider-dependent paid admissions** if authoritative verification unavailable | continue existing valid access/independent fulfilment | Finance/ops reconcile backlog | not automatically; pause affected commercial admission |
| Email provider | degraded delivery; business truth remains | may effectively pause new verified-account admission if no approved verification route; otherwise capability-specific | existing product access continues; required notices remain durable obligations | Communications/ops | only if required release communication has no safe approved route |
| Analytics | service continues; measurement freshness degraded | current stage may continue only within already-authorised boundary; **do not expand** without required trustworthy evidence | continues | data/ops investigate | no participant-service stop by default |
| Audit materialiser | action-specific E1/E2/E3 | protected E1 broadening may pause; expansion may pause if evidence integrity uncertain | safer E2 narrowing/remedies may continue only with lossless obligation | security/ops | scoped, not automatic full stop |
| Live provider | not FP-006 core | N/A to core | N/A to core | later FP-007 | FUTURE_ONLY for this pilot |
| Content delivery/storage | affected content/Plan access degrades | pause affected paid path if required paid/safety content cannot be delivered lawfully | preserve rights; continue unaffected content; repair/replace exact dependency | content/ops | scoped unless core journey broadly unavailable |
| Background queue | async-dependent obligations backlog; no fabricated completion | pause admission if critical obligations cannot be met within safe capacity | durable obligations remain; synchronous safe paths may continue | ops/developer | only if backlog threatens integrity/safety/owed service broadly |
| Search | discovery freshness/availability degraded | core direct paid paths may continue if discovery/offer path remains lawful | continues | ops | no by default |
| One application node | launch runtime unavailable; committed DB truth remains | pauses while app unavailable | owed obligations persist for restart/recovery | ops/developer | temporary service outage, not truth failure |
| Slow database / pool pressure | bounded waiting/refusal; never stale fabricated success | throttle/pause admission before invariant risk | prioritise existing owed/safety work; queues/backpressure visible | ops/developer | scoped or full maintenance only when correctness/availability requires |
| Generic third-party API | isolate affected capability; provider evidence not authority | capability-specific | unaffected owners continue; affected obligations remain unresolved/recoverable | owning operator/team | only if the failed dependency protects a release-critical invariant with no safe degradation |

**Expected invariant(s)**

- Analytics/search/dashboard outage never changes payment/entitlement/safety truth;
- provider outage never converts unknown to success/failure;
- queued obligations survive restart;
- safe narrowing remains possible during evidence/communications degradation where current authority permits;
- scope of stop matches scope of threatened invariant.

**Questions under test**  
Is a universal health endpoint/status page enough to govern degradation?

**Analysis**  
No. A status/health projection is useful but not authority. FP-006 JIT needs capability-specific runbooks using this semantic matrix and current owner truth.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE` + `CONTROLLED_LIVE` + `RELEASE_ONLY` as applicable.

**Upstream delta:** none.

**Evidence still required**  
Concrete provider/queue/DB failure proof and OQ-037/OQ-038 operations decisions.

**Follow-up**  
Use as the degradation baseline for the second adversarial pass.

---

# 51. `OPS-UPD-001` refinement after pilot-count pressure testing

No new ID is created. `OPS-UPD-001` remains the correct single upstream delta, but v0.5.0 narrows its required decision surface.

The explicit Product/release rule must answer:

1. **Admission commitment point** — which governed event consumes a pilot place?
2. **Concurrency** — how is a 10/11 or 50/51 race resolved without dashboard/provider authority?
3. **Review point vs hard cap** — how exactly does “toward 25” differ from maximum 50?
4. **In-flight pause** — what happens to a checkout/payment already admitted/initiated before a pause?
5. **Late reconciliation** — what happens when an ambiguous in-flight payment becomes verified after the stage closes?
6. **Historical cohort membership** — does a later refund/withdrawal remove the participant from historical cohort headcount or only current-active status?
7. **Replacement** — if a participant refunds/withdraws, may a new participant fill the numerical stage place, and how are both kept visible in evidence?

Already governed and **not** part of the gap:

- first 10 are ten genuine self-paying adult women;
- staff/free/complimentary/sponsored/100%-discount/manual grants do not count as paid demand;
- discounted real positive-payment purchases count;
- gift recipients are not self-paying first-10 participants merely because someone else paid;
- duplicate collections do not create extra participants;
- same participant's multiple purchases do not create multiple human participants;
- failed payment does not count as verified paid demand.

---

# 52. Gap register additions

## OPS-GAP-022 — FP-006 support-interaction measurement unit

- **Classification:** `JIT_ONLY`
- **Origin:** `OPS-PT-098`
- **Rule:** exact `support_interaction`/episode and active-handling-time definitions must be versioned before the first paid participant; no threshold is invented.
- **Status:** OPEN DOWNSTREAM.

## OPS-GAP-023 — Per-product Day-7/30/90 clock anchors

- **Classification:** `JIT_ONLY`
- **Origin:** `OPS-PT-100`
- **Rule:** current Product already requires qualifying event/window to be versioned before live measurement; exact product/pathway anchor must be frozen prospectively and cannot be rewritten after seeing results.
- **Status:** OPEN DOWNSTREAM, NOT PRODUCT GAP.

## OPS-GAP-024 — Capability-specific degradation runbooks

- **Classification:** `PHASE8_PROOF`
- **Origin:** `OPS-PT-104...111`
- **Rule:** semantic classification is sufficient for Pre-JIT; executable fail-closed/degraded/recovery behaviour requires JIT/proof/controlled-live exercises.
- **Status:** DEFERRED CORRECTLY.

## OPS-GAP-025 — Pilot admission/cap lifecycle

- **Classification:** `PRODUCT_AUTHORITY_GAP`
- **Origin:** `OPS-PT-085...097`
- **Route:** existing `OPS-UPD-001`, now narrowed by §51.
- **Status:** OPEN.

---

# 53. Batch E findings

## 53.1 Operator concurrency

- assignment is coordination, never a hard business lock;
- current source state wins over stale operator pages;
- participant self-service remains authoritative under owner policy;
- pause/resume must be current-state guarded, not last-writer-wins;
- human/automated correction races settle at the source Domain, not Audit/Work/UI.

## 53.2 Pilot counting

Current Product Law is much stronger than a naive “counter to 10/25/50.” Most inclusion/exclusion questions are already governed.

The real unresolved seam is narrower but serious: **the atomic admission/cap lifecycle**, including in-flight and later-refund historical cohort semantics.

## 53.3 Measurement

Current Product Law deliberately mandates metric-definition versioning before the first paid participant. This means Pre-JIT should not manufacture success thresholds or pretend an operational unit is already law.

The correct downstream contract is:

```text
source-owner facts
→ versioned metric definition
→ Analytics-derived measure
→ counts + percentages + missingness/limitations
→ no retroactive definition shopping
```

## 53.4 Safe stop / degradation

The correct model is capability-scoped, not platform-global. New admissions are often the first thing to pause; already-owed safe participant service should continue where the failed dependency does not invalidate it.

---

# 54. Cumulative inventory after v0.5.0

```text
OPS-PT-001...111 executed
OPS-UPD-001...007 open/working
```

No new upstream delta was added in this version.

---

# 55. Next highest-value batch

Next MINOR successor should attack **privilege/abuse + release decision misuse + bulk correction** and then run the required **second-pass adversarial coverage inventory**.

Priority first-pass abuse cases:

- Support grants paid access to a friend;
- Finance changes assessment result;
- developer browses health data;
- Super Admin bypasses Safety;
- operator deletes Audit trail;
- operator refunds but leaves duplicate economic benefit intentionally;
- operator changes participant identity incorrectly;
- bulk correction targets wrong users;
- staff copies sensitive data to uncontrolled spreadsheet/chat (already semantically covered; mutate for abuse rather than repeat);
- malicious release operator hides blockers/changes metric definition;
- one authority attempts to waive another blocker.

Then inventory all `OPS-PT-001...111`, group by semantic class and generate 15–30 candidate duplicate/reorder/retry/timeout/crash/restart/stale/concurrency/misuse/deletion/provider-outage mutations. Execute only genuinely new semantic classes.

---

# 56. v0.5.0 disposition

```text
CUMULATIVE PRESSURE TESTS: 111
UPSTREAM DELTAS: OPS-UPD-001...007
CURRENT BLOCKING PRODUCT CONFLICT: OPS-UPD-004
PILOT ADMISSION GAP: OPS-UPD-001 NARROWED, NOT RESOLVED
METRIC THRESHOLDS INVENTED: NONE
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
BROAD PRE-JIT FREEZE: NOT READY
NEXT: PRIVILEGE/ABUSE + SECOND-PASS ADVERSARIAL INVENTORY
```
