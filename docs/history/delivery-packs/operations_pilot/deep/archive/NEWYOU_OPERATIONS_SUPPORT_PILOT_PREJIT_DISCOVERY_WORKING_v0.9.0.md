# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.9.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.9.0`
- **Date:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch head before this successor:** `b4e76b17a50f47c25d3900650529c8ce1e3086fc`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.8.0.md`
- **Purpose:** perform one bounded pass on `OPS-UPD-001` — pilot admission, review-boundary, hard-cap, in-flight payment and historical cohort semantics.
- **Scope:** first-10 / toward-25 / maximum-50 progression; paid-demand qualification; place commitment versus payment verification; concurrent admission; failed/ambiguous/late payment; in-flight pause boundary; one-participant versus multiple-purchase counting; later refund/withdrawal; duplicate-human correction.
- **Explicit non-goals:** no Day-7/30/90 metric redesign, no general pause/resume design, no release-signoff redesign, no communications policy, no privacy/deletion policy, no clinical operations policy, no implementation mechanism selection, no new Domain/Resource, no PR, no authority amendment.
- **External evidence dates:** none added.
- **Current overall disposition:** `FOCUSED PASS CONVERGED / OPS-UPD-001 CONFIRMED AND FURTHER NARROWED / PRODUCT-LEVEL ADMISSION RULE STILL REQUIRED / BROAD STREAM FREEZE STILL BLOCKED`.

---

# 0. Append-only successor rule

Reasoning chain:

```text
v0.1.0
→ v0.2.0
→ v0.3.0
→ v0.4.0
→ v0.5.0
→ v0.6.0
→ v0.7.0
→ v0.8.0
→ this v0.9.0 focused pilot-admission pass
```

All predecessors remain preserved. This successor adds only the bounded pilot-admission material needed to refine `OPS-UPD-001`.

This version adds:

- `OPS-PT-140...OPS-PT-150`;
- no new `OPS-UPD`;
- no new `OPS-GAP`;
- a material refinement of existing `OPS-UPD-001` / `OPS-GAP-025`.

---

# 80. Live baseline and bounded authority route

Immediately before this pass, live GitHub `main` was re-fetched and remained:

```text
086ade7b28c000de1c387acb9760e5eb08bb0413
```

The current authority route remains the README route already recorded in prior versions. For this pass, only the authority needed for pilot admission was rechecked in depth:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` staged rollout and first-paid-cohort language;
- `00_PLATFORM_v1.6.0.md` §§21T.5–21T.9 paid-pilot evidence and paid-demand semantics;
- `01_DECISIONS_v1.6.0.md` `DEC-281`, `DEC-291`, `DEC-310...DEC-312`;
- `03_ARCHITECTURE_v1.1.1.md` concurrency, scarce-capacity correctness, provider-evidence and authoritative-state doctrine;
- `04_DOMAIN_MAP_v1.2.0.md` Commerce, Identity & Access, Analytics and Audit ownership boundaries;
- `05_ROADMAP_v1.2.0.md` FP-006 outcome, pilot progression and evidence contract.

No archive document was used to override current authority.

---

# 81. What current authority already fixes

The following are not open questions in this pass.

## 81.1 Who qualifies as paid-demand evidence

For the first paid cohort:

- participants are genuine self-paying adult women from the approved South African launch audience;
- they use the real bilingual product/catalogue and commercial contract;
- paid-demand evidence requires actual verified payment;
- free grants, staff accounts, complimentary or sponsored access, 100%-discount purchases and manual entitlement grants do not count;
- genuine discounted purchases may count when list price, promotion and actual amount paid remain distinguishable;
- warm-audience recruitment is permitted;
- the cohort must not be engineered to include only easy-to-automate cases or convenient temperament/eligibility outcomes.

A payment attempt, checkout start, provider browser success or manual Entitlement grant is therefore insufficient to make someone a paid-demand participant.

## 81.2 The progression is staged and review-led

Current Product/North-Star language gives the intended progression:

```text
internal validation
→ first 10 paid participants
→ review
→ expand toward 25
→ review
→ maximum 50 in first paid pilot
→ expanded / limited-public progression only with evidence
```

`DEC-281` states that the first paid pilot is limited to 50 participants and expands deliberately through **approximately** `10 → 25 → 50` only after safety, payment, entitlement, generation and support review.

Working consequence:

- **50 is explicitly a maximum for the first paid pilot**;
- **10 and 25 are governed review/progression points**;
- current authority does **not** safely justify treating 10, 25 and 50 as three identical hard-cap mechanisms.

## 81.3 Participant count is not purchase count

The governed language is participant-based. One participant making multiple purchases does not become multiple pilot participants. Duplicate collections for one order/participant do not increase participant headcount.

Purchase/revenue facts remain Commerce facts. Pilot participant headcount is a separate governed release/evidence concept.

## 81.4 Analytics and provider state are not admission authority

Analytics is derived only. A dashboard count cannot be the invariant that prevents the 51st admission.

Provider status is evidence to Commerce. Callback arrival order cannot decide pilot admission truth.

---

# 82. Semantic dimensions that must not be collapsed

The pilot boundary needs at least the following distinct concepts, regardless of later physical representation.

## 82.1 Purchase eligibility

Is this person currently allowed to attempt the relevant offer under Product/Identity/Commerce rules?

This is not yet a pilot place and not yet paid-demand evidence.

## 82.2 Capacity claim / in-flight admission claim

If Product chooses to prevent a charge that could exceed a hard stage boundary, the system needs a governed way to distinguish capacity already committed to an in-flight candidate from capacity still available to a new candidate.

This is a semantic requirement, **not** a decision here to create a particular Resource/table/lock/lease.

## 82.3 Verified paid admission

Paid-demand admission requires Commerce-authoritative verified actual payment plus the participant qualification rules.

Provider/browser evidence alone cannot create this state.

## 82.4 Historical pilot membership

Whether a participant was lawfully admitted to the first paid pilot is historical release/evidence truth. It must not be silently equated with whether the participant is still active, still entitled or later refunded.

The exact refund/withdrawal effect on historical headcount remains upstream policy under `OPS-UPD-001`.

## 82.5 Current participation / active obligation

A participant may later withdraw, be refunded, have an Entitlement consequence or no longer have an open fulfilment obligation. That later current state is distinct from the historical fact that she was previously admitted.

## 82.6 Evidence classification

A participant may be historically present yet excluded from a particular metric denominator for a governed reason. Metric inclusion/exclusion must not rewrite source admission history.

---

# 83. Focused pressure tests

## OPS-PT-140 — Checkout begins before any governed capacity commitment

**Scenario class:** pilot / concurrency / financial

**Why it matters**  
If a provider operation capable of producing a real charge starts before NewYou has any authoritative capacity claim, a strict cap can be crossed before local code knows which buyer should count.

**Relevant current authority**  
`DEC-281`; FP-006; Architecture zero-confirmed-oversell doctrine; paid-demand payment-verification rule.

**Owning Domain(s)**  
Commerce owns payment truth. Product/release authority must define the pilot-place commitment semantics. Exact persistence owner/representation remains JIT.

**Preconditions**  
One place remains under a hard boundary and two eligible buyers begin checkout concurrently.

**Timeline**

```text
buyer A starts charge-capable payment flow
buyer B starts charge-capable payment flow
→ both provider operations may succeed
→ NewYou later sees two genuine collections for one remaining place
```

**Expected invariant(s)**

- dashboard count cannot resolve this after the fact;
- provider callback order cannot choose who was lawfully admitted;
- a strict maximum cannot depend on refunding an avoidable 51st charge as the normal capacity mechanism.

**Questions under test**  
Must a place be provisionally committed before a charge-capable provider operation starts?

**Analysis**  
For a genuinely hard cap, some authoritative pre-payment capacity commitment is architecturally necessary unless Product explicitly accepts a post-charge rejection/remedy model. Current Product authority does not choose that business rule.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` → `JIT` → `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-001`.

**Evidence still required**  
Explicit commitment semantics and concurrency proof.

---

## OPS-PT-141 — Participant 10 / 11 overlap at the first review point

**Scenario class:** pilot / release / concurrency

**Why it matters**  
The North Star says first 10 → review, while `DEC-281` describes approximately 10 → 25 → 50.

**Expected invariant(s)**

- implementation does not invent whether 10 is an exact temporary closure point or an approximate review checkpoint;
- any admission after the review boundary follows the approved expansion rule;
- no dashboard-only gate.

**Analysis**  
Current authority strongly requires deliberate review before expansion but does not define the exact concurrent closure/tolerance rule around participant 10.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-001`.

**Proof route:** `PRODUCT_DECISION_PROMOTION`.

---

## OPS-PT-142 — Participant 25 / 26 overlap at the second review point

**Scenario class:** pilot / release / concurrency

**Why it matters**  
“Toward 25” is even less safely interpretable as an exact hard cap than maximum 50.

**Expected invariant(s)**

- 25 is not silently implemented as a hard inventory cap merely because it is a convenient integer;
- the Product/release rule defines when the next review closes or pauses expansion;
- concurrent admissions cannot make the review meaningless.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-001`.

**Proof route:** `PRODUCT_DECISION_PROMOTION`.

---

## OPS-PT-143 — Participant 50 / 51 overlap at the first-pilot maximum

**Scenario class:** pilot / release / concurrency / financial

**Why it matters**  
Unlike 10 and 25, 50 is explicitly the maximum first paid-pilot capacity.

**Expected invariant(s)**

- no more than 50 qualifying participants are lawfully admitted to the first paid pilot;
- the invariant survives simultaneous requests, retries, reordering and restart;
- provider success alone cannot force a 51st admission;
- any charge that can succeed after capacity is exhausted requires an explicit customer-remedy rule rather than silent over-cap admission.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-001`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-144 — Known payment failure after a provisional capacity claim

**Scenario class:** pilot / financial / recovery

**Why it matters**  
A failed attempt must not permanently consume scarce pilot capacity.

**Preconditions**  
Product has chosen a provisional capacity-claim model; provider/Commerce reaches a known final failure before admission.

**Expected invariant(s)**

- no paid-demand admission occurs;
- the provisional claim can be released through governed semantics;
- failure history remains evidence;
- another candidate may use capacity only after the claim is authoritatively released.

**Analysis**  
This is downstream once Product defines the capacity-claim lifecycle. It does not require a separate upstream delta.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-001` for the lifecycle definition only.

---

## OPS-PT-145 — Ambiguous payment outcome while a place is claimed

**Scenario class:** pilot / financial / recovery / concurrency

**Why it matters**  
Releasing capacity because a provider request timed out can later produce 51 confirmed paid admissions if the supposedly failed charge eventually proves successful.

**Expected invariant(s)**

- unknown outcome is not treated as known failure;
- the unresolved commercial obligation remains visible;
- strict capacity cannot be reissued as if the in-flight attempt were definitively dead unless Product defines a compensating/remedy model;
- reconciliation, not repetition/guessing, resolves the outcome.

**Analysis**  
The existing correction doctrine already locks `unknown → reconcile`, not `unknown → retry/release`. Applied to a hard pilot cap, the capacity consequence remains unresolved until the business outcome is reconciled or a Product-authorised remedy resolves the conflict.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-001` for exact place-claim semantics.

---

## OPS-PT-146 — Payment later verifies successful after stage closes or pauses

**Scenario class:** pilot / financial / release / recovery

**Why it matters**  
A genuine collection may become known only after the review boundary changed.

**Timeline**

```text
stage open
→ candidate begins governed in-flight flow
→ provider outcome ambiguous
→ stage closes/pauses for review
→ reconciliation later proves genuine successful payment
```

**Questions under test**

- Was the participant already protected by a valid capacity claim?
- Does late verification complete that earlier admission, or is a refund/remedy required?
- May the system count the participant after the stage has otherwise closed?

**Analysis**  
Current law does not answer this. Provider timing cannot choose the policy.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-001`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `EMPIRICAL_PROVIDER`.

---

## OPS-PT-147 — Stage pauses after place claim but before payment verification

**Scenario class:** pilot / release / concurrency

**Why it matters**  
“Stop new admissions” may mean stop new claims, cancel existing claims, or allow already-admitted/in-flight obligations to finish. Those are materially different customer promises.

**Expected invariant(s)**

- a pause is not interpreted from UI timing;
- new claims can be stopped without silently deciding the fate of already-valid claims;
- an immediate safety/technical stop may lawfully be narrower or stronger according to its explicit scope;
- the exact in-flight rule must be stated before implementation.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-001` for admission-boundary treatment. Broader pause/resume policy remains outside this pass.

**Proof route:** `PRODUCT_DECISION_PROMOTION` then `JIT`.

---

## OPS-PT-148 — Lawfully admitted participant later receives a refund or withdraws

**Scenario class:** pilot / historical evidence / financial

**Why it matters**  
If later outcomes erase historical admission, the first-10/25/50 evidence can be rewritten after the fact and capacity can be silently recycled.

**Expected invariant(s)**

- refund/withdrawal is a later true event, not automatic proof that the original admission never occurred;
- historical admission, current participation, current entitlement and refund state remain separate dimensions;
- Analytics may not retroactively rewrite source history to improve cohort shape.

**Questions under test**  
Does a later legitimate refund/withdrawal leave historical pilot membership intact? Does it free a pilot place?

**Analysis**  
The evidence-integrity argument strongly favours preserving historical admission while recording later state separately, but current Product Law does not explicitly make that policy choice. This remains an upstream decision rather than a downstream inference.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-001`.

**Proof route:** `PRODUCT_DECISION_PROMOTION`.

---

## OPS-PT-149 — Same participant makes multiple qualifying purchases or duplicate collections occur

**Scenario class:** pilot / counting / financial

**Why it matters**  
Revenue/purchase events must not inflate participant headcount.

**Expected invariant(s)**

- one human participant counts at most once in the participant-based pilot progression;
- multiple products/orders remain separate Commerce evidence;
- duplicate successful collections do not create an additional participant;
- correction of duplicate money follows Commerce/Entitlements rules without changing human headcount.

**Analysis**  
This follows directly from participant-based Product language and prior `OPS-PT-092` / `OPS-PT-096` findings. No new Product rule is needed for multiple purchases by the same known participant.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`.

**Upstream delta:** none beyond `OPS-UPD-001` where identity uncertainty affects cap correction.

---

## OPS-PT-150 — Two Accounts are later discovered to represent the same human participant

**Scenario class:** pilot / identity / counting / correction

**Why it matters**  
The Product contract counts participants, not Account rows. Duplicate identity can otherwise inflate the first-10/25/50 headcount.

**Owning Domain(s)**  
Identity & Access owns duplicate-account reconciliation; Commerce retains each truthful payment; pilot/release policy owns the headcount consequence; Analytics remains derived.

**Expected invariant(s)**

- duplicate Account reconciliation does not erase truthful purchases;
- one human participant does not become two pilot participants merely because two Accounts existed;
- correction is evidenced rather than silently editing historical dashboards;
- whether a corrected duplicate frees/backfills a pilot place is an explicit Product/release rule.

**Analysis**  
The count correction follows participant semantics, but the **replacement/backfill consequence at a closed review/cap boundary is not governed**.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-001`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` + Identity JIT/reconciliation proof.

---

# 84. `OPS-UPD-001` — refined decision surface

`OPS-UPD-001` remains one upstream Product/release-policy delta. This pass does **not** split it into multiple IDs because the open questions are one coupled admission lifecycle.

The required upstream rule must answer, explicitly:

1. **Review-boundary semantics:** Is first-10 closure exact, approximate within a governed tolerance, or another explicitly defined review rule? What exactly does “toward 25” mean operationally?
2. **Place commitment:** What governed event creates a provisional capacity claim before verified payment, if any?
3. **Admission point:** What event turns a qualifying candidate into a historical paid-pilot participant?
4. **Hard maximum:** How must the maximum-50 rule behave when multiple charge-capable flows overlap?
5. **Known failure:** When may a provisional place be released?
6. **Unknown outcome:** Does an unresolved payment continue to hold/occupy capacity until reconciliation, or is a different explicit customer-remedy model intended?
7. **In-flight stop:** What happens to a valid in-flight claim when new admissions are paused/closed?
8. **Late success:** What happens when a previously ambiguous payment verifies successful after the stage closes?
9. **Historical membership:** Does a later legitimate refund/withdrawal preserve historical cohort membership and consume the historical place?
10. **Invalid-from-inception correction:** When a person is later proven non-qualifying or duplicate-human counting is corrected, may/should the cohort be backfilled, and under what review boundary?

Until those questions are answered, FP-006 JIT must not choose a convenient database/checkout rule and present it as Product policy.

---

# 85. Recommended minimum upstream shape — not authority

The following is a **recommendation for the eventual Product/release decision**, not a rule created by this ledger.

The smallest coherent lifecycle appears to be:

```text
eligible candidate
→ provisional capacity claim
→ payment in flight
→ admitted on Commerce-authoritative verified actual payment
```

with non-success paths such as:

```text
known final payment failure
→ claim released

outcome unknown
→ claim remains unresolved
→ reconciliation
→ admitted | released/remedied
```

and independent later history:

```text
admitted
→ later refund / withdrawal / entitlement consequence
```

without rewriting the original admission fact merely because a later legitimate event occurred.

Why this shape is recommended:

- it can protect a strict hard cap before an external charge succeeds;
- it keeps provider state as evidence rather than authority;
- it preserves the existing `unknown → reconcile` doctrine;
- it separates historical cohort truth from current participation;
- it does not create a new Domain by itself;
- it leaves transaction/lock/expiry/storage/provider details to JIT.

However, Product must explicitly decide the first-10/toward-25 review semantics, in-flight pause rule, late-success rule and historical/backfill rule before this recommendation can become a JIT contract.

---

# 86. Downstream work that remains JIT/proof, not Product policy

Once `OPS-UPD-001` is resolved upstream, downstream work may choose/prove:

- which existing boundary durably represents the admission/release-control state;
- transaction/locking/compare-and-set strategy;
- unique/idempotency identity for a place claim;
- claim expiry/cancellation mechanics where Product permits expiry;
- provider-attempt correlation and reconciliation;
- crash/restart recovery;
- concurrent 50/51 proof;
- operator observability and support projection;
- Analytics derivation from authoritative admission facts.

Do **not** create an Operations Domain, Release Domain or Analytics-owned admission record merely to solve the concurrency mechanism.

---

# 87. Focused-pass disposition

```text
NEW PRESSURE TESTS: OPS-PT-140...150
NEW UPSTREAM DELTAS: none
NEW GAPS: none
OPS-UPD-001: CONFIRMED / NARROWED / STILL OPEN
OPS-GAP-025: OPEN / PRODUCT_AUTHORITY_GAP
HARD FIRST-PAID-PILOT MAXIMUM: 50
10 / 25: REVIEW-PROGRESSION POINTS; EXACT CONCURRENT CLOSURE STILL UNRESOLVED
PAID-DEMAND QUALIFICATION: ALREADY GOVERNED
PARTICIPANT COUNT != PURCHASE COUNT: WORKING LOCK
UNKNOWN PAYMENT: RECONCILE; DO NOT GUESS/RETRY/RELEASE AS KNOWN FAILURE
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
```

**Focused pass outcome:** `PASS / CONVERGED FOR DISCOVERY PURPOSES`.

The next semantic pass must be separate. This document does not begin it.
