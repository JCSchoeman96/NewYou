# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.12.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.12.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch head before this successor:** `2603076a0a7f68222f758416ddf1cc456ee7869e`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.11.0.md`
- **Purpose:** perform one bounded pass on `OPS-UPD-005` — material participant Plan change-of-intent after paid Request admission but before first successful fulfilment.
- **Scope:** current-request versus future-only participant edits; immutable Plan-generation basis; pre-generation, in-generation and generated-but-not-delivered change timing; stale completion/delivery races; Plan entitlement consumption versus reuse/rebinding; refundability versus replacement; post-delivery boundary; narrow existing complimentary regeneration exception; repeated changes; correction/safety-change negative controls.
- **Explicit non-goals:** no generic Plan-input schema design, no clinical eligibility/routing redesign, no Health correction design, no recurring membership adjustment design, no operator-role redesign, no privacy/deletion policy, no broader `HSP-UPD-007` review-gated refund analysis, no implementation Resource/job/lock selection, no new Domain, no PR, no authority amendment.
- **External evidence dates:** none added. Existing HSP working artifacts are reused only as non-authoritative discovery evidence.
- **Current overall disposition:** `FOCUSED PASS CONVERGED / OPS-UPD-005 CONFIRMED AND NARROWED / STALE-REQUEST SEMANTICS SEPARATED FROM COMMERCIAL REBINDING / PRODUCT-LEVEL PRE-FIRST-FULFILMENT RIGHT TREATMENT STILL REQUIRED / BROAD STREAM FREEZE STILL BLOCKED`.

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
→ v0.9.0
→ v0.10.0
→ v0.11.0
→ this v0.12.0 focused pre-first-fulfilment Plan change-of-intent pass
```

All predecessors remain historical reasoning evidence.

This version adds:

- `OPS-PT-175...OPS-PT-186`;
- no new `OPS-UPD`;
- no new `OPS-GAP`;
- a material narrowing of existing `OPS-UPD-005` / `OPS-GAP-015`;
- explicit reuse, not duplication, of existing `HSP-UPD-008`.

---

# 110. Live baseline and bounded authority route

Immediately before this pass:

```text
main = 086ade7b28c000de1c387acb9760e5eb08bb0413
working branch head = 2603076a0a7f68222f758416ddf1cc456ee7869e
```

Only authority/evidence relevant to this seam was rechecked in depth:

- `01_DECISIONS_v1.6.0.md`:
  - `DEC-036` narrow complimentary regeneration after a materially different digital assessment result;
  - `DEC-038` preference/progress re-personalisation requires a new purchase or qualifying membership/add-on;
  - `DEC-045` Plan refund boundary at generation;
  - `DEC-107` every generation/adjustment creates an immutable, reproducible, linked Plan version;
  - `DEC-299` paid Plan entitlement remains unconsumed until successful governed Plan delivery, with technical generation failure preserving the right.
- `00_PLATFORM_v1.6.0.md`:
  - Plan is refundable before generation and ordinarily non-refundable once delivered;
  - existing Product/paid-plan ownership and commercial boundaries.
- `04_DOMAIN_MAP_v1.2.0.md`:
  - Plans & Nutrition owns Plan generation/result truth;
  - Entitlements owns the commercial right;
  - Commerce owns refund/payment truth.
- `05_ROADMAP_v1.2.0.md` FP-005:
  - safe, reproducible Plan generation and purchased-plan delivery remain the governed outcome.
- `working/health_safety_plans/NEWYOU_HSP_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.2.md` only as non-authoritative prior discovery:
  - `HSP-UPD-008` records this exact unresolved Product/Commerce/Entitlements question.
- `archive/HEALTH_SAFETY_PLAN_PREJIT_DISCOVERY_WORKING_v0.42.0.md` only as historical working evidence:
  - `HSP-WD-031` first fulfilment is a delivered/made-available final Plan under governed access, not mere generation;
  - `HSP-WD-033` a participant-owned material current-Request input edit does not silently mutate the immutable Generation Basis and blocks stale-basis fulfilment.

No archive or working document was used to override current authority.

---

# 111. What current authority already fixes

## 111.1 Successful Plan delivery is the entitlement-consumption boundary

`DEC-299` already establishes:

```text
paid Plan entitlement
→ held / unconsumed before fulfilment
→ consumed only after successful governed Plan delivery
```

Technical generation failure preserves the right.

Therefore:

```text
generation started
≠ entitlement consumed

generated artifact exists
≠ entitlement consumed

participant changes intent before delivery
≠ automatically consumed
```

This pass must not invent a forfeiture/consumption event merely because compute or staff effort has already occurred.

## 111.2 Generation is commercially meaningful, but refundability is a different dimension

`DEC-045` says Plan refunds end after generation. Current Platform prose also says a Plan is refundable before generation and ordinarily non-refundable once delivered.

Therefore:

```text
refundability
≠ entitlement consumption
≠ replacement/rebinding permission
```

A participant can be past the ordinary refund boundary while the Plan entitlement remains unconsumed because first successful delivery has not occurred.

That generated-but-not-fulfilled interval is exactly why `OPS-UPD-005` cannot be solved by quoting `DEC-045` alone.

## 111.3 Post-delivery preference/progress re-personalisation is already governed

`DEC-038` says preference- or progress-based re-personalisation requires a new purchase or active qualifying membership/add-on.

That clearly constrains the **post-valid-fulfilment** case.

It does not explicitly settle a different state where:

```text
paid Request admitted
+ no first successful fulfilment yet
+ participant materially changes the intended Plan inputs
```

Applying `DEC-038` automatically to that pre-fulfilment state would silently decide the existing `HSP-UPD-008` Product gap.

## 111.4 Existing complimentary regeneration is deliberately narrow

`DEC-036` grants one complimentary regeneration within 90 days when an included assessment credit later produces a materially different digital result.

That explicit exception proves that complimentary regeneration is a governed Product right, not something JIT may generalise from convenience.

`DEC-036` does not answer ordinary participant preference/progress change before first fulfilment.

## 111.5 Plan versions cannot be silently rewritten

`DEC-107` requires every generation and adjustment to create an immutable, reproducible, linked Plan version.

Historical HSP working evidence further refines the useful pre-JIT model:

- the in-flight Generation Basis is immutable;
- a material participant edit explicitly intended for the current Request blocks fulfilment from the stale basis;
- future-only/unrelated edits do not automatically invalidate the in-flight Request.

The immutable-history direction is consistent with current authority. Exact Request/Basis Resource design remains JIT.

---

# 112. Semantic dimensions that must remain separate

This seam requires at least six independent dimensions.

## 112.1 Participant input truth

The participant's current preference/progress/Plan-input state.

A later change may be:

- intended for the current in-flight Request;
- future-only;
- unrelated to this Plan;
- a correction rather than changed intent;
- safety-relevant evidence rather than ordinary preference/progress.

Those meanings cannot be inferred from “profile updated”.

## 112.2 Plan Request intent

The logical Request that is being fulfilled.

A material edit explicitly intended to change the current Request may invalidate/supersede that Request's basis. It does not rewrite the Request's history.

## 112.3 Generation attempt / immutable Plan version

Generation work and any immutable version produced from the old basis remain historically true.

They are not automatically the participant's valid first fulfilment after material intent changes.

## 112.4 Plan entitlement/right state

The commercial Plan right remains owner-Domain truth under Entitlements.

Before successful governed delivery, `DEC-299` says it is unconsumed.

Whether that **same unconsumed right may be rebound to a replacement Request** after participant-driven material intent change is the central unresolved Product question.

## 112.5 Refundability

`DEC-045` controls ordinary refund timing.

Refund eligibility does not by itself answer whether the same paid right can fund replacement work.

## 112.6 Fulfilment / delivered Plan lineage

If successful delivery wins before the participant's new intent becomes applicable, the first fulfilment exists and later ordinary preference/progress change falls under `DEC-038`.

If the material current-Request change wins first, stale work must not later manufacture fulfilment from obsolete intent.

---

# 113. Current working boundary for `OPS-UPD-005`

The focused pass narrows the gap to this question:

> When a participant deliberately changes a material, non-safety Plan input and explicitly applies that change to an already-admitted but not-yet-fulfilled paid Plan Request, may the existing still-unconsumed Plan entitlement authorize the replacement Request, and does that treatment change once qualifying generation has begun?

That question has two Product/commercial sub-parts:

1. **replacement-right treatment** — same unconsumed right versus new purchase/other governed consequence;
2. **generation-boundary treatment** — whether the answer differs before generation, during generation, or after generated-but-before-delivery.

If Product chooses that a new purchase is required after generation, it must also state what becomes of the original still-unconsumed paid Plan right. Downstream code must not silently “consume”, forfeit, expire, strand or convert it merely to make the ledger balance.

---

# 114. Focused pressure tests

## OPS-PT-175 — Material participant intent change before generation begins

**Scenario class:** Plan / entitlement / participant intent

**Preconditions**

- paid Plan Request is lawfully admitted;
- current Safety authority permits the pathway;
- no successful Plan delivery has occurred;
- qualifying generation has not begun;
- participant changes a material ordinary Plan input and explicitly wants the current Request to use the new value.

**Expected invariants**

- the original Request/basis is not silently mutated;
- stale old-intent work cannot later become first fulfilment;
- Plan entitlement remains unconsumed under `DEC-299`;
- refundability and replacement-right treatment remain separate.

**Question under test**

May the same unconsumed right authorize the replacement Request before any generation work has begun?

**Analysis**

Current authority does not explicitly answer. The case is commercially simpler than a post-generation change, but “unconsumed” does not automatically mean “freely rebindable”. JIT may not choose the customer right.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-005` / reuse `HSP-UPD-008`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` → `JIT` → `PHASE8_EXECUTABLE`.

---

## OPS-PT-176 — Material change after immutable basis capture but before generation execution

**Scenario class:** Plan / concurrency / participant intent

**Why it matters**

Capturing an immutable basis cannot turn the participant's earlier intent into irrevocable business authority.

**Expected invariants**

- captured basis remains historical evidence;
- if the edit explicitly applies to the current Request and is material, generation from the old basis must not be treated as current fulfilment;
- old Request cancellation/invalidation and replacement Request admission remain distinct from entitlement treatment;
- no direct basis edit.

**Analysis**

The stale-basis rule is supported by immutable/reproducible Plan doctrine and HSP working evidence. The commercial rebinding question remains upstream.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-005`.

---

## OPS-PT-177 — Material participant change while generation is in progress

**Scenario class:** Plan / concurrency / resource cost / participant intent

**Timeline**

```text
Request admitted
→ immutable basis captured
→ generation starts
→ participant submits material current-Request change
→ old generation may still finish
```

**Expected invariants**

- process completion does not outrank newer authoritative Request intent;
- stale output cannot fulfil merely because compute completed first at a worker;
- generated history/provenance may remain if retained;
- Plan right remains unconsumed until lawful successful delivery;
- sunk compute cost is not itself entitlement authority.

**Question under test**

Does generation start force a new purchase for the replacement?

**Analysis**

`DEC-045` makes generation relevant to refundability, but current law does not state that generation consumes the Plan right or answers replacement-right treatment.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-005`.

---

## OPS-PT-178 — Generation completes before the material change, but delivery has not happened

**Scenario class:** Plan / commercial / pre-fulfilment

**Why it matters**

This is the sharpest seam between `DEC-045` and `DEC-299`.

**State**

```text
generation complete
+ no successful governed delivery
+ Plan right still unconsumed under DEC-299
+ ordinary refund boundary may already be closed under DEC-045
+ participant now changes material current-Request intent
```

**Expected invariants**

- refund closure does not silently become entitlement consumption;
- generated artifact cannot be retroactively edited;
- if the new intent is accepted for the current Request before delivery, obsolete content cannot be deliberately delivered just to manufacture fulfilment;
- the disposition of the still-unconsumed right requires Product authority.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-005`.

---

## OPS-PT-179 — Accepted intent change races stale generation/delivery completion

**Scenario class:** Plan / concurrency / stale authority

**Timeline**

```text
material current-Request change is durably accepted
→ old Request is no longer eligible to fulfil from old basis
|| stale worker / delivery path completes
```

**Expected invariants**

- current Request authority is revalidated at fulfilment;
- stale work rejects/no-ops as fulfilment;
- no entitlement consumption occurs from stale delivery attempt;
- historical attempt/version evidence is preserved as appropriate;
- replacement-right commercial decision remains separate.

**Analysis**

Once Product/JIT has a governed way to establish that the current Request was superseded/invalidated, current-state revalidation is downstream correctness, not a new Product choice.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-005` only for the replacement-right rule.

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-180 — Successful delivery wins before the participant changes intent

**Scenario class:** Plan / boundary / post-fulfilment

**Timeline**

```text
Plan successfully delivered
→ entitlement consumed exactly once
→ participant later changes preferences/progress
```

**Expected invariant**

The later ordinary preference/progress change is no longer a pre-first-fulfilment case.

**Analysis**

`DEC-038` governs ordinary re-personalisation after the existing Plan has been validly fulfilled: new purchase or active qualifying membership/add-on is required, subject only to separately governed exceptions such as `DEC-036`.

**Semantic disposition:** `PASS`

**Upstream delta:** none for this case.

---

## OPS-PT-181 — Participant edits a future-only or unrelated preference during in-flight generation

**Scenario class:** Plan / applicability / negative control

**Why it matters**

A profile edit is not automatically a command to cancel current work.

**Expected invariants**

- applicability is explicit;
- future-only/unrelated edit does not silently invalidate the current Request;
- old basis is not mutated;
- future work may use the new value under its own Request.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** none beyond `OPS-UPD-005` defining what counts as a material current-Request change.

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-182 — Participant changes a non-material field

**Scenario class:** Plan / applicability / negative control

**Expected invariants**

- immaterial/non-Plan-input edits do not cause gratuitous cancellation/regeneration;
- materiality is assessed under the governed Plan input/rule contract, not arbitrary UI field change;
- audit/profile update history may exist without Plan consequence.

**Analysis**

Exact field-level materiality belongs in Plans JIT/rule governance unless it changes the Product promise. This does not justify a broader Product amendment.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** none beyond the existing `OPS-UPD-005` material-change definition.

---

## OPS-PT-183 — Safety-relevant new information is presented as a “preference change”

**Scenario class:** safety / Plan / negative control

**Why it matters**

A preference UI must not become a bypass around Safety & Eligibility.

**Expected invariants**

- safety-relevant evidence routes through Health/Safety authority;
- current Safety eligibility is re-established before Plan fulfilment;
- ordinary `OPS-UPD-005` commercial change-of-intent semantics do not decide the safety outcome;
- any governed safety/eligibility refund/remedy follows current Product law.

**Semantic disposition:** `PASS / OUTSIDE OPS-UPD-005`

**Upstream delta:** none created.

---

## OPS-PT-184 — Participant corrects an earlier wrong Plan input rather than changing her mind

**Scenario class:** correction / Plan / negative control

**Why it matters**

“Wrong when entered” and “true then, changed now” are different histories.

**Expected invariants**

- correction provenance is preserved;
- stale basis cannot fulfil if the corrected fact is material to the current Request;
- the correction is not automatically labelled ordinary post-delivery re-personalisation;
- operator/UI must not overwrite the old basis.

**Analysis**

The source-truth correction distinction is already part of the stream's working doctrine. Exact pre-fulfilment commercial treatment should not be silently inferred from `DEC-038`; if Product wishes to distinguish correction from discretionary change-of-intent economically, that belongs in the same narrow upstream Plan-right policy rather than a generic admin rule.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-005` only if the governed commercial rule distinguishes correction from deliberate change-of-intent.

---

## OPS-PT-185 — Participant makes successive material changes while replacement work is in flight

**Scenario class:** Plan / concurrency / abuse / commercial

**Timeline**

```text
Request A admitted
→ material change creates/requires Request B
→ before B fulfils, another material change creates/requires Request C
```

**Expected invariants**

- A/B/C histories remain distinct;
- only the current authorised Request may fulfil;
- stale competitors cannot consume the right;
- repeated participant changes do not create duplicate Plan rights;
- the number/cost/allowance of participant-driven pre-fulfilment replacements is not invented by JIT.

**Question under test**

Does one paid Plan right permit unlimited participant-driven replacements before first fulfilment, a bounded number, or none after some boundary?

**Analysis**

Current law does not answer. Resource-abuse concerns are real, but infrastructure cost cannot silently become Product policy. The upstream rule should define the customer entitlement; JIT/security may then enforce abuse/rate controls beneath it.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-005`.

---

## OPS-PT-186 — Operator edits the old basis or deliberately delivers stale Plan to avoid the gap

**Scenario class:** operator / Plan / authority bypass

**Why it matters**

A support/admin shortcut could manufacture either “same Request” or “first fulfilment” and thereby select the commercial outcome.

**Expected invariants**

- operator cannot mutate immutable basis/version history;
- operator cannot knowingly deliver stale content merely to trigger consumption/`DEC-038`;
- any replacement invokes owner-Domain operations under current guards;
- unresolved Product entitlement treatment remains unresolved until governed.

**Semantic disposition:** `PASS / NEGATIVE AUTHORITY PROOF`

**Upstream delta:** `OPS-UPD-005`.

---

# 115. Adjudication of `OPS-UPD-005`

## 115.1 Already governed — do not reopen

The following do **not** need a new Product decision:

1. successful governed Plan delivery is the entitlement-consumption boundary under `DEC-299`;
2. technical generation failure preserves the paid Plan right;
3. every generation/adjustment creates immutable reproducible linked Plan history (`DEC-107`);
4. ordinary Plan refunds end after generation (`DEC-045`);
5. post-fulfilment preference/progress re-personalisation requires new purchase or qualifying membership/add-on (`DEC-038`);
6. `DEC-036` is a narrow explicit complimentary-regeneration exception and does not create a generic free-regeneration rule;
7. safety-relevant information routes through Health/Safety authority rather than ordinary preference semantics;
8. stale operator/UI state cannot override current source authority.

## 115.2 Still genuinely open

Product/Commerce/Entitlements authority must decide:

1. whether the same still-unconsumed paid Plan right may authorize a replacement Request when the participant makes a material current-Request change before first fulfilment;
2. whether that treatment differs:
   - before qualifying generation begins;
   - after generation begins;
   - after generation completes but before successful delivery;
3. if a new purchase/right is required at any pre-fulfilment point, what happens to the original still-unconsumed Plan right and why that outcome is consistent with `DEC-299`;
4. whether participant-driven repeated pre-fulfilment changes have a governed allowance/cap or other commercial consequence;
5. whether genuine correction of an earlier wrong participant input receives different commercial treatment from discretionary change-of-intent;
6. how the replacement-right rule composes with `DEC-045` without equating refundability, generation, fulfilment and entitlement consumption.

This is the full remaining `OPS-UPD-005` surface. Request/version concurrency mechanics stay downstream.

---

# 116. Recommended minimal Product shape

This is a **working recommendation**, not current Product Law.

The simplest coherent rule that preserves current doctrine would be:

> A participant-owned material Plan-input change explicitly intended for the current paid Request before first successful fulfilment supersedes the stale Request for fulfilment and never rewrites its immutable generation history. The paid Plan entitlement remains unconsumed until successful governed Plan delivery. Product authority must state whether that existing unconsumed right may authorize the replacement Request and whether the rule changes after qualifying generation has begun. Refundability remains governed separately by `DEC-045`. If a new purchase/right is required before first fulfilment, the disposition of the original still-unconsumed right must be stated explicitly rather than inferred as consumed, forfeited, expired or silently reusable. After first successful fulfilment, ordinary preference/progress re-personalisation follows `DEC-038`, subject only to explicit governed exceptions such as `DEC-036`.

### Simplicity recommendation for adjudication

For the once-off MVP, the least contradictory customer-right model appears to be:

```text
one paid Plan right
→ one successful first Plan fulfilment
```

with pre-fulfilment participant changes superseding stale Requests without themselves consuming the right.

However, that model still needs Product to decide how many participant-driven replacement generations are included and whether generation start creates any explicit commercial boundary short of successful delivery. Those are customer-right choices, not implementation details.

---

# 117. Explicit non-inferences from this pass

Do not infer that:

- every profile edit cancels in-flight Plan work;
- every preference change is material;
- an edit intended only for future Plans applies to the current Request;
- generation start consumes the Plan entitlement;
- the `DEC-045` refund boundary automatically requires a second purchase for pre-fulfilment change-of-intent;
- `DEC-038` automatically applies before first fulfilment;
- `DEC-036` grants a general complimentary regeneration right;
- a safety-relevant change is ordinary re-personalisation;
- a correction and a discretionary change-of-intent have identical commercial treatment;
- compute/staff cost authorizes forfeiting an unconsumed right;
- an operator can resolve the gap by editing the basis, granting a new right manually, or delivering stale content first.

---

# 118. Upstream delta status after focused pass

`OPS-UPD-005` remains one existing delta; no parallel Product delta is created.

Updated status:

```text
OPS-UPD-005
= material participant Plan change-of-intent before first fulfilment
→ stale current-Request basis may not fulfil after material applicable change
→ successful delivery remains entitlement-consumption boundary
→ refundability remains separate
→ post-delivery DEC-038 remains separate
→ exact pre-first-fulfilment same-right rebinding / new-purchase rule remains open
→ repeated-change allowance and correction distinction require only the minimum Product clarification actually needed
→ classification: CONFIRMED PRODUCT / COMMERCE / ENTITLEMENT GAP
→ reuse HSP-UPD-008
```

`OPS-GAP-015` remains the discovery gap index for this same semantic class.

---

# 119. Focused-pass convergence

No new semantic class emerged beyond existing `OPS-UPD-005`.

The focused pass establishes:

- current authority already prevents a number of unsafe downstream shortcuts;
- the Plan right is not consumed merely because generation starts or completes;
- refund boundary and entitlement/replacement right are separate;
- post-delivery re-personalisation and the narrow assessment-result regeneration exception are already governed;
- the exact unresolved decision is pre-first-fulfilment treatment of the still-unconsumed Plan right after participant-driven material current-Request change;
- repeated-change and correction variants can be adjudicated beneath the same Product rule rather than creating new upstream deltas.

Focused discovery is therefore converged enough to stop.

---

# 120. v0.12.0 disposition

```text
NEW PTs: OPS-PT-175...OPS-PT-186
CUMULATIVE PTs: 186
NEW OPS-UPD: 0
NEW OPS-GAP: 0
OPS-UPD-005: CONFIRMED + NARROWED
OPS-GAP-015: OPEN / SAME SEMANTIC CLASS
HSP-UPD-008: REUSED, NOT DUPLICATED
STALE-REQUEST / IMMUTABLE-HISTORY RULE: SUFFICIENTLY DERIVED/WORKING-LOCKED FOR THIS STREAM
PRE-FIRST-FULFILMENT PLAN-RIGHT REBINDING: OPEN PRODUCT/COMMERCE/ENTITLEMENT DECISION
REFUNDABILITY VS REBINDING: EXPLICITLY SEPARATED
POST-DELIVERY DEC-038: NOT REOPENED
DEC-036 NARROW REGENERATION EXCEPTION: NOT GENERALIZED
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED BY EXISTING UPSTREAM DELTAS + REQUIRED REVIEW/PROMOTION
```
