# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.11.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.11.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch head before this successor:** `a310a108c6f5dbd6198ded97a98760cdd2a658b5`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.10.0.md`
- **Purpose:** perform one bounded pass on `OPS-UPD-004` — the assessment-credit consumption contradiction between `DEC-055` and the later Product/Roadmap successful-delivery rule.
- **Scope:** assessment-credit availability/claim versus consumption; first-answer boundary; active/recoverable attempt; unsuccessful/expired attempt; technical failure; result/report creation versus delivery; notification failure; participant non-open; second-purchase blocking; refundability versus consumption; duplicate completion/consumption; operator correction boundary.
- **Explicit non-goals:** no assessment methodology redesign, no scoring/tie semantics, no clinical/Plan policy, no pilot admission/counting, no operator-role redesign, no privacy/deletion policy, no communications-provider selection, no implementation mechanism/Resource selection, no PR, no authority amendment.
- **External evidence dates:** none added.
- **Current overall disposition:** `FOCUSED PASS CONVERGED / OPS-UPD-004 CONFLICT CONFIRMED AND NARROWED / MINIMAL PRODUCT AMENDMENT SHAPE IDENTIFIED / CONFLICT STOP REMAINS UNTIL EXPLICIT GOVERNED SUPERSESSION OR AMENDMENT`.

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
→ this v0.11.0 focused assessment-credit conflict pass
```

All predecessors remain historical reasoning evidence.

This version adds:

- `OPS-PT-163...OPS-PT-174`;
- no new `OPS-UPD`;
- no new `OPS-GAP`;
- a material narrowing of existing `OPS-UPD-004` / `OPS-GAP-010`.

---

# 100. Live baseline and bounded authority route

Immediately before this pass:

```text
main = 086ade7b28c000de1c387acb9760e5eb08bb0413
working branch head = a310a108c6f5dbd6198ded97a98760cdd2a658b5
```

Only authority needed for this conflict was rechecked in depth:

- `01_DECISIONS_v1.6.0.md`:
  - `DEC-045` refund boundary;
  - `DEC-054` save/resume, one active attempt and controlled technical recovery;
  - `DEC-055` assessment entitlement consumption;
  - `DEC-056` unfinished-attempt expiry;
  - `DEC-061` immutable raw result;
  - `DEC-066` historical delivered report;
  - `DEC-067` completed-result/version immutability;
  - `DEC-303` repeat-assessment purchase limits.
- `00_PLATFORM_v1.6.0.md` temperament-provenance matrix, specifically:
  - `digitally_assessed → included assessment credit = consumed_only_after_successful_assessment_delivery`;
  - `later_digital_completion → consume_when_successfully_delivered`.
- `05_ROADMAP_v1.2.0.md` FP-003 exit condition:
  - included credit remains unused until successful digital assessment delivery.
- `04_DOMAIN_MAP_v1.2.0.md`:
  - Temperament owns attempt/answers/raw scores/result;
  - Entitlements owns current commercial right/credit state.

No archive document was used to override current authority.

---

# 101. Exact conflict statement

Current `DEC-055` remains `LOCKED` and says:

```text
Do not consume the entitlement until the first answer is saved.
Mark it used once the attempt begins.
```

Current later Product Law says:

```text
digitally_assessed
→ included assessment credit = consumed_only_after_successful_assessment_delivery

later_digital_completion
→ consume_when_successfully_delivered
```

Current FP-003 Roadmap exit condition independently says:

```text
included credit remains unused until successful digital assessment delivery
```

No explicit current supersession or amendment of `DEC-055` was found.

Therefore this remains a real same-authority-layer contradiction. This stream must not resolve it by silently redefining `used`, `consume`, `attempt begins` or `successful delivery`.

**Current status:** `CONFLICT / STOP AT PRODUCT AUTHORITY`.

---

# 102. The conflict is narrower than one universal entitlement lifecycle

The pressure-test evidence shows at least four independent dimensions.

## 102.1 Credit consumption

The commercial question:

```text
unconsumed
→ consumed
```

Current later Product/Roadmap text places this transition at successful digital assessment delivery. `DEC-055` places it at attempt start/first answer.

This is the direct authority conflict.

## 102.2 Credit availability / claim

A credit may need to be unavailable for another purchase/attempt without already being commercially consumed.

`DEC-303` proves that `unused` credit state matters independently because a second sale is blocked while an ordinary paid assessment credit is unused.

This creates a necessary distinction between:

```text
available_unused
held_or_claimed_by_active_or_recoverable_attempt
consumed
```

The exact state names/representation remain JIT; the semantic distinction is the important finding.

## 102.3 Temperament attempt/result lifecycle

Temperament separately owns:

```text
attempt admission
answers/save-resume
submission/scoring
immutable result
report/delivery recovery
attempt expiry
```

Attempt/result state cannot be replaced by an Entitlement boolean.

## 102.4 Refundability

`DEC-045` says ordinary assessment refunds end after the first answer, except technical failure.

That means:

```text
refundability boundary
≠ credit consumption boundary
```

A participant can be past the ordinary refund boundary while the later Product/Roadmap text still calls the credit unconsumed until successful delivery.

This is not itself a contradiction if the dimensions are explicitly separated.

---

# 103. Minimal semantic model recommended for upstream adjudication

This is **working recommendation, not current Product Law**.

A minimal reconciliation shape is:

```text
credit available + unconsumed
→ first answer / governed attempt claim
→ credit held/claimed + unconsumed
→ successful governed digital assessment delivery
→ credit consumed exactly once
```

Where delivery has not succeeded:

```text
credit remains unconsumed
+ current attempt/recovery state decides whether it remains held or can return to available
```

That last branch cannot be invented by JIT. Product authority must explicitly define the participant promise for terminal non-delivery/expiry cases, while Temperament/Entitlements JIT may choose the physical representation only after the rule is governed.

The model intentionally does **not** say that a held credit is reusable, refundable or available for another assessment. Those are separate governed questions.

---

# 104. Focused pressure tests

## OPS-PT-163 — First answer is saved

**Scenario class:** assessment / entitlement / authority conflict

**Why it matters**  
This is the exact boundary where the conflicting rules diverge.

**Relevant current authority**  
`DEC-054`, `DEC-055`, Product temperament-provenance matrix, FP-003 exit condition, `DEC-303`.

**Owning Domain(s)**  
Temperament owns the attempt/answer. Entitlements owns credit state.

**Timeline**

```text
valid unused credit
→ assessment attempt admitted
→ first answer saved
```

**Expected invariant(s)**

- there is still one logical credit and one active attempt;
- another ordinary assessment sale must not be allowed merely because the credit is not yet successfully delivered;
- downstream code must not choose whether the credit is consumed from conflicting authority.

**Analysis**  
`DEC-055` says consumption/used at this point. Later Product/Roadmap says the credit remains unused until successful delivery. `DEC-303` additionally shows that “unused” need not mean “freely available for another sale”.

**Semantic disposition:** `CONFLICT`

**Proof route:** `PRODUCT_DECISION_PROMOTION` then `JIT` / `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-004`.

---

## OPS-PT-164 — Participant abandons an attempt after answering questions but before delivery

**Scenario class:** assessment / lifecycle / abandonment

**Why it matters**  
An unfinished attempt can remain active and later expire. The participant has used platform effort and entered immutable answers, but no successful digital assessment delivery occurred.

**Relevant current authority**  
`DEC-054...DEC-056`, Product successful-delivery consumption rule, `DEC-303`.

**Expected invariant(s)**

- answers/history are not erased merely to make the credit reusable;
- a second sale is not admitted from a stale interpretation of “unused”;
- consumption cannot be chosen downstream;
- attempt expiry and credit consequence are not the same lifecycle.

**Analysis**  
The current conflict affects whether this credit is already consumed. Separately, current authority does not explicitly state what happens to credit availability after a terminal expired non-delivered attempt.

**Semantic disposition:** `CONFLICT / NEEDS_UPSTREAM_REFINEMENT`

**Upstream delta:** `OPS-UPD-004`.

**Evidence still required**  
Explicit terminal non-delivery/expiry entitlement rule.

---

## OPS-PT-165 — Genuine technical failure after first answer, before a final result exists

**Scenario class:** assessment / technical failure / recovery

**Why it matters**  
Technical failure must not create a free duplicate right or strand a paid participant.

**Relevant current authority**  
`DEC-045`, `DEC-054`, `DEC-055`, successful-delivery rule.

**Expected invariant(s)**

- controlled recovery is allowed for genuine technical failure;
- no second credit is manufactured;
- failed delivery does not become fake success;
- ordinary operator convenience cannot decide consumption/restoration.

**Analysis**  
Later Product/Roadmap text says no successful delivery means no consumption. `DEC-055` says the opposite after first answer. `DEC-045` separately allows a technical-failure refund exception, proving refund/remedy is another dimension rather than a substitute for consumption semantics.

**Semantic disposition:** `CONFLICT`

**Upstream delta:** `OPS-UPD-004`.

---

## OPS-PT-166 — Immutable result exists but governed report/delivery is incomplete

**Scenario class:** assessment / recovery / delivery

**Why it matters**  
Result creation and participant delivery can be separated by crash, rendering failure or access-path failure.

**Relevant current authority**  
`DEC-061`, `DEC-066`, Product/Roadmap successful-delivery consumption rule.

**Expected invariant(s)**

- immutable result is not recreated merely because delivery failed;
- result existence alone must not be silently equated with successful delivery;
- credit consequence occurs exactly once at the governed consumption boundary;
- recovery converges on the existing result/report lineage.

**Analysis**  
This pressure test confirms that `result_created` and `successful_delivery` cannot be one implicit event. Exact delivery terminal semantics remain to be defined after Product resolves the consumption rule.

**Semantic disposition:** `CONFLICT_WITH_DOWNSTREAM_REFINEMENT`

**Upstream delta:** `OPS-UPD-004`.

**Proof route:** Product amendment → Temperament/Entitlements JIT → executable crash/recovery proof.

---

## OPS-PT-167 — Assessment is available in-product but notification email fails

**Scenario class:** assessment / communications / delivery

**Why it matters**  
A notification provider must not accidentally control commercial entitlement truth.

**Relevant current authority**  
Successful-delivery consumption rule; general Communications/source-authority doctrine from current platform authority.

**Expected invariant(s)**

- notification attempt state remains separate from Temperament delivery and Entitlement consumption;
- provider email failure cannot by itself create a second assessment credit;
- exact approved participant-delivery terminal event must be explicit enough that JIT does not invent whether email is required.

**Analysis**  
Current sources do not explicitly define whether successful assessment delivery requires a notification channel. This should be resolved as part of the consumption-boundary amendment or an explicitly subordinate delivery contract, not by provider convention.

**Semantic disposition:** `NEEDS_UPSTREAM_REFINEMENT`

**Upstream delta:** `OPS-UPD-004`.

---

## OPS-PT-168 — Participant never opens an otherwise available assessment report

**Scenario class:** assessment / customer-delivery boundary

**Why it matters**  
If consumption waits for participant opening/read behaviour, a commercial right could remain indefinitely unconsumed despite a completed deliverable.

**Expected invariant(s)**

- the governed delivery event must be deterministic and platform-verifiable;
- Analytics/open tracking cannot become entitlement authority;
- participant non-open cannot silently create a second credit unless Product explicitly promises that behaviour.

**Analysis**  
Current authority says “successful digital assessment delivery,” not “participant read/open,” but does not define the terminal event precisely enough to freeze implementation. The upstream repair should make the customer promise explicit enough to exclude analytics/open tracking as authority unless deliberately chosen.

**Semantic disposition:** `NEEDS_UPSTREAM_REFINEMENT`

**Upstream delta:** `OPS-UPD-004`.

---

## OPS-PT-169 — Participant tries to buy another assessment while an active attempt holds the existing credit

**Scenario class:** assessment / purchase / entitlement

**Why it matters**  
This tests whether “unconsumed until delivery” accidentally means “available for another sale.”

**Relevant current authority**  
`DEC-303`.

**Expected invariant(s)**

- second standalone assessment sale is blocked while the ordinary paid credit is unused;
- active attempt/credit claim prevents double-use even if consumption has not yet occurred;
- purchase eligibility remains distinct from consumption.

**Analysis**  
Current authority is sufficient for the negative sale rule. This is strong evidence that availability/claim and consumption must be distinct concepts.

**Semantic disposition:** `PASS`

**Upstream delta:** none beyond resolving `OPS-UPD-004` terminology/lifecycle.

---

## OPS-PT-170 — Active attempt expires after 30 days without successful delivery

**Scenario class:** assessment / expiry / entitlement

**Why it matters**  
`DEC-056` terminates the attempt, but current authority does not state the resulting availability of a credit that later Product/Roadmap still calls unconsumed.

**Expected invariant(s)**

- expiry does not retroactively fabricate successful delivery;
- expired attempt history remains truthful;
- a credit must not remain indefinitely stranded solely because lifecycle dimensions were collapsed;
- JIT must not invent whether the participant receives controlled restart/recovery, reuse of the same credit, or another commercial remedy.

**Analysis**  
This is not a new semantic class; it is a concrete terminal branch of `OPS-UPD-004` that the upstream amendment must address or route explicitly.

**Semantic disposition:** `NEEDS_UPSTREAM_REFINEMENT`

**Upstream delta:** `OPS-UPD-004`.

---

## OPS-PT-171 — Controlled recovery occurs after technical interruption

**Scenario class:** assessment / recovery / idempotency

**Why it matters**  
Recovery must continue one paid obligation rather than mint another credit or another immutable result.

**Relevant current authority**  
`DEC-054`, `DEC-061`, `DEC-067`.

**Expected invariant(s)**

- controlled recovery preserves the same commercial obligation;
- if an immutable result already exists, recovery delivers that result rather than scoring again;
- any consumption consequence is applied at most once;
- exact physical attempt/resource strategy remains JIT.

**Analysis**  
The recovery principle is governed. The only blocked part is when Entitlements changes from held/unconsumed to consumed.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-004` only for the consumption boundary.

---

## OPS-PT-172 — Ordinary refund requested after first answer but before successful delivery

**Scenario class:** assessment / refund / entitlement

**Why it matters**  
This tests whether refundability and consumption are incorrectly treated as synonyms.

**Relevant current authority**  
`DEC-045`; successful-delivery consumption rule.

**Expected invariant(s)**

- ordinary refund boundary can already be closed after first answer;
- the credit can still be commercially unconsumed under the later successful-delivery rule;
- lack of ordinary refundability does not prove successful delivery;
- credit state is not changed by an operator merely because refund is refused.

**Analysis**  
These two rules can coexist only if refundability and consumption are separate dimensions. The Product amendment should preserve that distinction rather than moving the refund boundary accidentally.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-004` for explicit consumption semantics only; `DEC-045` itself is not reopened by this pass.

---

## OPS-PT-173 — Duplicate/retried completion races the credit-consumption consequence

**Scenario class:** assessment / concurrency / idempotency

**Why it matters**  
Once Product selects the consumption event, duplicate submit/delivery/recovery signals must not consume twice.

**Relevant current authority**  
One active attempt, immutable result, general idempotency/current-state doctrine.

**Expected invariant(s)**

- one logical paid credit is consumed at most once;
- duplicate/retried delivery attempts observe/converge on the existing consumption outcome;
- transport request identity cannot be the only business idempotency key;
- no duplicate result or duplicate commercial consequence.

**Analysis**  
No new Product gap beyond the disputed consumption boundary. Exact idempotency mechanism is JIT/proof.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-004` only for event selection.

---

## OPS-PT-174 — Operator manually marks the credit consumed because the attempt started

**Scenario class:** operator / correction / authority conflict

**Why it matters**  
A staff action must not become the mechanism that chooses between contradictory Product rules.

**Expected invariant(s)**

- Support/Finance cannot resolve an upstream contradiction by editing Entitlement state;
- current owner-Domain guards must fail closed where the governing consumption rule is ambiguous;
- operator notes/Audit history do not make one interpretation lawful;
- after upstream amendment, any manual recovery still uses an explicit owner-Domain operation.

**Analysis**  
This is a direct STOP. Human convenience cannot repair Product Law.

**Semantic disposition:** `PASS / NEGATIVE AUTHORITY PROOF`

**Upstream delta:** `OPS-UPD-004` remains prerequisite.

---

# 105. Adjudication of `OPS-UPD-004`

## 105.1 What is definitely contradictory

The contradiction is specifically:

```text
DEC-055:
first answer / attempt begins
→ consume / mark used

versus

current Product matrix + FP-003 Roadmap:
successful digital assessment delivery
→ consume
```

No lower-level artifact may choose between them.

## 105.2 What can already be separated without changing Product promises

The following distinctions are now sufficiently supported to treat as working constraints:

1. **attempt state ≠ entitlement consumption**;
2. **credit availability/claim ≠ credit consumption**;
3. **refundability ≠ credit consumption**;
4. **result creation ≠ successful delivery**;
5. **notification/provider delivery evidence ≠ source assessment delivery authority**;
6. **operator correction ≠ Product-policy selection**.

## 105.3 What the minimal upstream amendment must decide

At minimum Product/Decision authority must explicitly answer:

1. Does the later successful-delivery rule supersede `DEC-055`'s “mark it used once the attempt begins” statement?
2. When the first answer is saved, is the credit merely **held/claimed and unavailable** while remaining unconsumed?
3. What exact customer-facing event constitutes `successful digital assessment delivery` for consumption purposes?
4. Does notification failure matter to that event, or only the availability of the governed digital result/report through an approved product path?
5. What happens to credit availability when an unfinished attempt expires or becomes terminally unrecoverable without successful delivery?
6. How does the technical-failure refund/recovery path resolve the held credit without creating a duplicate right or double consumption?

The first two are necessary to remove the direct contradiction. Questions 3–6 are needed to prevent the amendment from merely moving ambiguity downstream.

---

# 106. Recommended promotion shape — not current law

The smallest coherent Product/Decision repair appears to be an explicit `DEC-055` supersession/refinement rather than a new assessment entitlement regime.

A candidate shape is:

> **Assessment-credit claim and consumption.** An ordinary paid assessment credit remains commercially unconsumed until successful governed digital assessment delivery. Saving the first answer / beginning the governed attempt claims or holds that credit for the active/recoverable attempt and makes it unavailable for another ordinary assessment purchase or independent attempt, but does not itself consume it. Successful governed delivery consumes the credit exactly once. Technical interruption, retry, reconciliation or recovery must not manufacture a second credit, result or consumption. Product authority must define the terminal treatment of a non-delivered expired/unrecoverable attempt and the minimum event that constitutes successful digital delivery; notification/open analytics do not become entitlement authority merely by implementation convention.

This is deliberately a **promotion candidate**, not authority.

It also deliberately leaves concrete state names, tables, Resources, transactions and retry mechanisms to JIT.

---

# 107. Downstream work after upstream repair

Once `OPS-UPD-004` is governed, FP-003/FP-006 JIT may define:

- Entitlements representation of available/held/consumed state;
- the cross-Domain command/effect connecting Temperament delivery to Entitlements consumption;
- exact delivery terminal evidence consistent with the governed customer promise;
- expiry/recovery mechanics;
- idempotency identity for consumption;
- stale-state/operator recovery commands;
- crash/restart/retry proof;
- negative proof that no second purchase/attempt is admitted while the credit is held;
- evidence that notification/open analytics do not mutate entitlement state unless Product explicitly chose that rule.

JIT may not choose the Product answer first and then backfill the authority text.

---

# 108. Gap/register result

No new gap class was found.

`OPS-GAP-010` remains the correct gap record and is refined to:

```text
Assessment-credit claim/availability versus consumption conflict
+ successful-delivery terminal boundary
+ terminal non-delivery/expiry consequence
```

all routed through existing `OPS-UPD-004`.

No new `OPS-UPD` is justified.

---

# 109. Focused pass disposition

```text
SEMANTIC PRESSURE TESTS ADDED: OPS-PT-163...174
CUMULATIVE PRESSURE TESTS: 174
NEW OPS-UPD: 0
NEW OPS-GAP: 0
OPS-UPD-004: CONFLICT CONFIRMED + NARROWED
OPS-GAP-010: OPEN / CONFLICT STOP
DIRECT CONFLICT: DEC-055 ATTEMPT-BEGIN CONSUMPTION VS LATER SUCCESSFUL-DELIVERY CONSUMPTION
MINIMAL SAFE PROMOTION TARGET: EXPLICIT DEC-055 SUPERSESSION/REFINEMENT + CLAIM VS CONSUMPTION SEPARATION
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED BY EXISTING UPSTREAM DELTAS + REQUIRED REVIEW/PROMOTION
```
