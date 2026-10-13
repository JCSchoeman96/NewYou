# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.10.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.10.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch head before this successor:** `2760d0a65426217457cdc2ef07e534bb0a198091`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.9.0.md`
- **Purpose:** perform one bounded pass on `OPS-UPD-002` — duplicate genuine collection, customer make-whole obligation, refund ambiguity/failure and partial commercial-loss attribution.
- **Scope:** duplicate provider evidence versus duplicate genuine money movement; one-order/one-right consequence; full excess make-whole; refund execution ambiguity/failure; competing correction channels; source/amount mismatch; partial final reversal attribution; deterministically attributable versus unattributable component consequence.
- **Explicit non-goals:** no pilot admission/count semantics, no operator-role assignment redesign, no assessment/clinical/Plan policy, no privacy/deletion policy, no release-control redesign, no provider implementation/API selection, no new Domain/Resource, no PR, no authority amendment.
- **External evidence dates:** none added. Current Paystack Pre-JIT working contract is reused as non-authoritative provider-independent evidence; its empirical provider validation remains explicitly not executed.
- **Current overall disposition:** `FOCUSED PASS CONVERGED / OPS-UPD-002 CONFIRMED AND NARROWED / PRODUCT CLARIFICATION READY FOR GOVERNED PROMOTION / EMPIRICAL PROVIDER PROOF STILL OPEN / BROAD STREAM FREEZE STILL BLOCKED`.

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
→ this v0.10.0 focused duplicate-collection / partial-attribution pass
```

All predecessors remain historical reasoning evidence.

This version adds:

- `OPS-PT-151...OPS-PT-162`;
- no new `OPS-UPD`;
- no new `OPS-GAP`;
- a material narrowing of existing `OPS-UPD-002`, `OPS-GAP-007` and `OPS-GAP-009`.

---

# 90. Live baseline and bounded authority route

Immediately before this pass:

```text
main = 086ade7b28c000de1c387acb9760e5eb08bb0413
working branch head = 2760d0a65426217457cdc2ef07e534bb0a198091
```

Only authority/evidence relevant to this bounded seam was rechecked in depth:

- `01_DECISIONS_v1.6.0.md`:
  - `DEC-290` paid-pilot zero duplicate charges/entitlements criterion;
  - `DEC-299` immutable accepted-order component allocation for component refunds;
  - `DEC-300` Commerce reversal/refund/duplicate-payment truth versus Entitlements component-level current-access consequence;
  - `DEC-307` refund classification and separation of technical/payment corrections from dissatisfaction evidence.
- `00_PLATFORM_v1.6.0.md` paid-pilot refund/evidence doctrine where relevant.
- `04_DOMAIN_MAP_v1.2.0.md` Commerce and Entitlements ownership boundaries.
- `03_ARCHITECTURE_v1.1.1.md` provider-evidence, idempotency, ambiguous-outcome and authoritative-state doctrine.
- `working/paystack_validation/NEWYOU_PAYSTACK_PREJIT_CONTRACT_WORKING_v1.0.0.md` only as current non-authoritative working evidence.

No archive document was used to override current authority.

---

# 91. What current authority already fixes

## 91.1 Duplicate evidence is not duplicate money

A repeated/replayed/reordered callback or provider read about **one** genuine collection is evidence duplication, not another customer charge.

Current authority already requires provider evidence to be interpreted by Commerce, not copied into business truth. Therefore:

```text
one genuine collection
+ repeated provider evidence
≠ two payments
≠ two entitlements
```

This is JIT/proof, not Product-policy work.

## 91.2 Duplicate genuine collection creates no duplicate right

`DEC-300` already fixes the access consequence:

> duplicate-payment correction leaves one valid right.

Therefore a second genuine successful collection for one accepted purchase cannot create:

- a second Entitlement;
- a second assessment credit;
- a second Plan right;
- a second paid period;
- a second paid-pilot participant.

The unresolved question is the **customer-money remedy**, not whether duplicate access is allowed.

## 91.3 Commerce and Entitlements remain separate

Current law already fixes:

- Commerce owns payment, refund, dispute, reversal and duplicate-payment truth;
- Entitlements owns current access/right truth;
- provider callback/browser/dashboard state is evidence only;
- commercial history and current access are distinct;
- component consequences must be idempotent.

A refund therefore does not directly toggle access, and an access correction does not itself prove customer money has been returned.

## 91.4 Full reversal is already substantially governed

`DEC-300` already states that:

- a final lost chargeback revokes affected current access;
- a post-delivery full reversal is exceptional and ends current access while preserving historical delivery and reversal records;
- restored payment restores access idempotently.

This pass therefore does **not** reopen full-reversal Product semantics.

## 91.5 Paid-pilot evidence classification is already governed

`DEC-290` requires zero duplicate charges/entitlements as a paid-pilot integrity criterion.

`DEC-307` already requires technical/payment refunds to be separated from dissatisfaction evidence.

Therefore correcting an excess collection must not be counted as participant dissatisfaction.

---

# 92. Exact unresolved semantic surface under `OPS-UPD-002`

Current Product authority still does not explicitly state all of the following:

1. whether every genuine excess customer collection beyond the one purchase amount creates an obligation to return the **full excess collected amount**;
2. whether that customer-money obligation remains open when provider refund execution is ambiguous, unavailable or fails;
3. whether a provider execution problem may ever convert the owed amount into “no longer owed”;
4. how to prevent refund/dispute/other correction paths from economically correcting the same excess twice;
5. whether a partial provider loss amount can identify a NewYou component/right merely because the amount happens to equal a component allocation;
6. what access consequence applies when a partial final loss is **not deterministically attributable** to a specific governed component/right.

The current Paystack working contract already records a candidate answer to these points, but explicitly labels it **not yet Product Law**.

---

# 93. Independent lifecycle dimensions

This pass rejects a single `payment_status` or `refund_status` lifecycle as insufficient.

At minimum keep these dimensions distinct:

## 93.1 Accepted purchase / order satisfaction

```text
accepted order
→ unsatisfied | satisfied_once
```

For the current one-off launch path, the purchase may be satisfied only once.

## 93.2 Genuine collection history

Each genuine customer collection remains a truthful financial event.

```text
collection A = successful
collection B = successful
```

A correction later does not make either historical collection fictitious.

## 93.3 Excess make-whole obligation

If Product adopts the existing working clarification:

```text
no_excess_obligation
→ excess_owed(amount, source)
→ correction_execution_pending
→ corrected
   | outcome_unknown
   | failed_needs_remedy
```

`outcome_unknown` and `failed_needs_remedy` are **not** equivalent to `corrected`.

## 93.4 Refund/correction execution attempt

Provider execution attempt state is separate:

```text
not_started
→ dispatched
→ processed
   | known_failure
   | outcome_unknown
```

Provider execution state does not decide whether NewYou owes the money.

## 93.5 Dispute / chargeback / final reversal

A provider dispute/reversal is a distinct later financial dimension. It is not the same lifecycle as merchant-initiated refund correction.

## 93.6 Entitlement consequence

Entitlements applies only the lawful component/right consequence derived from governed Commerce truth.

A financial amount alone is not component identity.

---

# 94. Focused pressure tests

## OPS-PT-151 — Replayed provider evidence for one genuine collection

**Scenario class:** financial / idempotency / provider evidence

**Why it matters**  
A duplicated webhook/read must not be misdiagnosed as a duplicate customer charge.

**Preconditions**  
One genuine provider transaction succeeded; the same provider event/transaction is observed repeatedly or out of order.

**Expected invariants**

- Commerce records one genuine collection effect;
- repeated evidence may update evidence chronology but cannot create another payment effect;
- Entitlements sees at most the one lawful purchase consequence;
- no make-whole obligation is created merely from duplicated evidence.

**Analysis**  
This is already governed by provider-evidence/idempotency doctrine and the Paystack working invariants. It is not part of the unresolved Product clarification.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

**Upstream delta:** none.

---

## OPS-PT-152 — Two distinct genuine successful collections for one accepted order

**Scenario class:** financial / correction / customer money

**Why it matters**  
Idempotent business code cannot assume the provider will never produce two real economic effects.

**Timeline**

```text
one accepted order for amount X
→ collection A genuinely succeeds for X
→ collection B also genuinely succeeds for X
→ purchase/right must still be satisfied once
```

**Expected invariants**

- both collections remain truthful history;
- exactly one purchase/right consequence exists;
- the participant must not receive duplicate economic benefit;
- the customer-money treatment of the excess must be explicit rather than left to provider/JIT convention.

**Analysis**  
Current authority settles the one-right result but not the exact full-excess make-whole promise. The existing Paystack working clarification is therefore still a real Product-level candidate.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-002`.

---

## OPS-PT-153 — Second genuine collection discovered after fulfilment was already delivered

**Scenario class:** financial / historical truth / correction

**Why it matters**  
Delivery of the valid purchased benefit must not turn a later-discovered excess collection into legitimate additional revenue.

**Preconditions**  
One valid collection already satisfied the purchase and the assessment/Plan/report benefit was lawfully delivered. A second genuine collection is discovered later.

**Expected invariants**

- historical lawful delivery remains true;
- no second right is created;
- the second collection remains financial history rather than being deleted;
- if Product adopts the working clarification, the full excess remains owed regardless of the already-delivered valid benefit.

**Analysis**  
The benefit was owed once, not twice. Current authority still does not explicitly state the full customer-money make-whole obligation.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-002`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `EMPIRICAL_PROVIDER`.

---

## OPS-PT-154 — Excess correction completes successfully

**Scenario class:** financial / correction / recovery

**Preconditions**  
The Product rule has established an exact excess amount owed; provider correction completes and Commerce verifies it.

**Expected invariants**

- the original genuine collections remain truthful history;
- the successful correction is a later true financial event;
- the make-whole obligation closes exactly once for the corrected amount/source;
- exactly one valid purchase/right remains;
- technical/payment correction remains separate from dissatisfaction evidence.

**Analysis**  
Once the Product obligation is governed, the success path is downstream Commerce/JIT/proof. No additional Product rule is required.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-002` only for the obligation definition.

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-155 — Refund/correction mutation times out and outcome is ambiguous

**Scenario class:** financial / recovery / ambiguous outcome

**Why it matters**  
Blindly repeating a consequential refund can itself over-correct the participant.

**Timeline**

```text
exact make-whole amount owed
→ refund/correction request dispatched
→ response lost / timeout
→ provider outcome unknown
```

**Expected invariants**

- timeout ≠ known failure;
- the financial obligation remains visible;
- the execution attempt is unresolved until reconciled;
- no blind duplicate mutation is issued;
- a later verified processed correction closes only the exact outstanding amount/source once.

**Analysis**  
`unknown → reconcile` is already working-locked doctrine. Exact Paystack ambiguity behaviour remains empirical `OQ-004` proof, not another Product delta.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-002` for the underlying owed-money rule only.

**Proof route:** `EMPIRICAL_PROVIDER` + `JIT` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-156 — Provider cannot execute an owed correction

**Scenario class:** financial / customer remedy / provider degradation

**Why it matters**  
Provider balance/outage/refusal must not silently decide whether NewYou still owes customer money.

**Preconditions**  
A governed customer-money obligation exists; provider correction is known not to have completed.

**Expected invariants**

- execution failure does not fabricate `corrected`;
- the exact owed amount/source remains durable and visible;
- valid unrelated access/right remains unchanged;
- Support/Finance work remains open/routed;
- no blind retry storm;
- another lawful correction route, if later approved/available, satisfies the same obligation rather than creating a second one.

**Analysis**  
This is a core part of the existing Paystack working clarification (`PAY-INV-026`) but is not yet explicit Product Law. Because it changes the customer promise under provider failure, it belongs in the governed `OPS-UPD-002` promotion rather than JIT invention.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-002`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `EMPIRICAL_PROVIDER` + `OPERATIONS_POLICY`.

---

## OPS-PT-157 — Refund and another correction channel race for the same excess

**Scenario class:** financial / concurrency / correction

**Why it matters**  
A participant must not receive a double financial correction because two truthful recovery paths act concurrently.

**Examples**

- merchant refund in flight while provider reversal later appears;
- manual restricted correction route begins while automated refund reconciliation completes;
- dispute outcome changes while a make-whole correction is open.

**Expected invariants**

- one economic obligation has one remaining balance;
- every financial correction is source/amount linked;
- already-corrected amount cannot be corrected again;
- historical events remain truthful even when the final net obligation becomes zero;
- operator work state does not decide net financial truth.

**Analysis**  
This is a Commerce/JIT/proof invariant once the Product obligation is known. It does not require a new Product delta.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** none beyond `OPS-UPD-002`.

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-158 — Provider says refund processed but source/amount does not match the obligation

**Scenario class:** financial / evidence binding / correction

**Why it matters**  
A provider “processed” status cannot close the wrong NewYou customer obligation.

**Expected invariants**

- correction evidence must bind to the expected provider transaction/source and amount/currency;
- mismatched evidence remains investigation/reconciliation evidence;
- the NewYou obligation remains open until the correct amount/source is verified;
- no access consequence is derived from provider refund status alone.

**Analysis**  
Current authority and provider-independent working invariants are sufficient. This is proof, not Product policy.

**Semantic disposition:** `PASS`

**Upstream delta:** none.

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-159 — Partial final reversal amount happens to equal one bundle component allocation

**Scenario class:** financial / partial reversal / entitlement attribution

**Why it matters**  
Amount coincidence is tempting but may have no semantic relationship to what the provider reversed.

**Example**

```text
bundle accepted amount = 549
assessment allocation = 249
provider final partial loss = 249
```

**Expected invariants**

- `249 == assessment allocation` does not by itself prove the assessment component is the affected right;
- current catalogue prices are irrelevant;
- callback ordering does not choose a component;
- Entitlements may change only a component/right identified by governed NewYou commercial evidence.

**Analysis**  
`DEC-300` requires component-level consequences but does not explicitly forbid using amount coincidence to manufacture component identity. The existing Paystack working clarification correctly identifies this as a Product-level attribution gap.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-002`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `JIT`.

---

## OPS-PT-160 — Partial final reversal cannot be mapped to any specific component

**Scenario class:** financial / partial reversal / adjudication

**Preconditions**  
Provider establishes a genuine final financial loss less than the original purchase amount, but NewYou has no governed evidence that identifies which purchased component/right the lost amount represents.

**Expected invariants**

- Commerce records the financial loss truth;
- Finance/Commerce adjudication remains visible;
- Entitlements does not arbitrarily revoke a component;
- proportional allocation, arbitrary ordering or current price matching cannot invent the affected right;
- historical purchase/delivery remains truthful.

**Analysis**  
The financial fact and entitlement consequence must remain decoupled until deterministic component identity exists. This exact participant-access consequence is not explicit in current Product authority.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-002`.

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `JIT` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-161 — Partial final loss is deterministically attributable to a governed component

**Scenario class:** financial / partial reversal / entitlement consequence

**Preconditions**  
Governed NewYou commercial evidence—not provider amount coincidence—explicitly identifies the affected component/right.

**Expected invariants**

- Commerce records the financial correction/loss;
- Entitlements applies only the identified component-level current-access consequence;
- unrelated components/independent sources survive;
- delivery/payment/reversal history remains preserved;
- duplicate/retry execution remains idempotent.

**Analysis**  
Once deterministic component identity exists and the upstream attribution rule is governed, `DEC-300` already supplies the owner split and component-level consequence model.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-002` only for the no-manufactured-attribution Product rule.

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`.

---

## OPS-PT-162 — Full final reversal after delivery

**Scenario class:** financial / reversal / historical truth

**Why it matters**  
This test checks whether `OPS-UPD-002` is accidentally reopening already-governed full-reversal semantics.

**Expected invariants**

- Commerce records the verified final reversal;
- current affected access ends under `DEC-300`;
- historical delivery and reversal records remain;
- no historical event is erased;
- restored payment, if later validly established, restores access idempotently under current law.

**Analysis**  
Current `DEC-300` is already explicit. No `OPS-UPD-002` extension is justified.

**Semantic disposition:** `PASS`

**Upstream delta:** none.

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`.

---

# 95. `OPS-UPD-002` adjudication after focused pressure testing

## 95.1 Already governed — do not re-decide

The following are already fixed and must not be reopened in the Product clarification:

1. Commerce owns payment/refund/dispute/reversal truth.
2. Entitlements owns current access/right truth.
3. Provider callbacks/browser/dashboard state are evidence only.
4. Duplicate-payment correction leaves one valid right.
5. Commercial history and current access are distinct.
6. A full final reversal / post-delivery full reversal already has governed current-access and historical-record consequences under `DEC-300`.
7. Technical/payment correction is separate from dissatisfaction evidence.
8. Component refunds use the accepted-order allocation snapshot where a Product rule authorises a component refund.
9. Unknown consequential outcome is reconciled rather than blindly retried.
10. A genuine duplicate collection does not create a second pilot participant.

## 95.2 Still requires governed Product clarification

The smallest safe promotion target is:

> **Duplicate genuine collection and partial-loss attribution clarification.**  
> For one accepted Purchase Intent/order in the current one-off launch path, the purchase may be satisfied only once. Any additional genuine successful customer collection remains truthful financial history but creates no second entitlement, credit, paid period or other right. The full excess amount genuinely collected from the customer remains owed for make-whole correction. Ambiguous, unavailable or failed provider execution does not extinguish that obligation; the exact remaining owed amount/source stays open until lawfully reconciled or satisfied. Financial correction paths must not apply the same economic correction twice. A partial provider dispute/chargeback/final reversal establishes financial loss only; its amount does not by itself identify a NewYou product component/right. Entitlements may permanently alter only a component/right deterministically identified by governed NewYou commercial evidence. Amount coincidence, provider aggregate status, callback ordering, current prices, arbitrary ordering or proportional allocation do not manufacture component identity. An unattributable partial loss remains visible Commerce/Finance adjudication work without arbitrary entitlement mutation. Historical payment, delivery, refund and reversal truth remains preserved.

This wording intentionally reuses the substance of the existing Paystack working clarification rather than inventing a competing rule.

## 95.3 What remains provider/JIT proof after promotion

Even after Product promotion, these remain downstream/empirical:

- exact Paystack refund/dispute API/status behaviour;
- how ambiguous refund execution is read/reconciled;
- insufficient-balance and provider-outage operational paths;
- provider rate limits/retries/timeouts;
- concrete Commerce Resources/actions/states;
- exact idempotency keys/constraints;
- Finance/support work representation;
- reconciliation jobs/scans;
- executable duplicate/reordered/restart proof.

`OPS-GAP-004` / `OQ-004` therefore remains open. Product clarification does not certify provider behaviour.

---

# 96. Gap and delta state after this pass

No new gap or upstream delta is created.

Current relevant records:

```text
OPS-UPD-002 — CONFIRMED REAL PRODUCT GAP
→ narrowed to full-excess make-whole persistence + no-manufactured partial component attribution
→ candidate governed wording ready for promotion
→ provider/JIT proof remains separate

OPS-GAP-007 — OPEN
→ duplicate collection / make-whole clarification not yet governed
→ route: OPS-UPD-002

OPS-GAP-009 — OPEN
→ partial reversal component attribution
→ route: OPS-UPD-002

OPS-GAP-004 — OPEN / EXISTING PROVIDER EMPIRICAL GATE
→ Paystack one-off operational empirical proof
→ route: OQ-004 / FP-002 proof
```

Do not merge `OPS-GAP-004` into `OPS-UPD-002`: one is provider proof; the other is Product/customer-remedy semantics.

---

# 97. Focused convergence result

This pass found no new semantic class and no justification for a new ID family.

It **did** materially narrow `OPS-UPD-002`:

```text
NOT:
"duplicate/refund/dispute behaviour generally"

BUT:
1. excess genuine customer collection creates a full make-whole obligation;
2. provider inability/ambiguity does not erase that obligation;
3. same economic correction cannot be applied twice;
4. partial provider financial loss does not manufacture component identity;
5. only deterministic governed NewYou commercial evidence may drive component access consequence;
6. unattributable partial loss remains Commerce/Finance work, not arbitrary Entitlement mutation.
```

## Disposition

```text
NEW PTs: OPS-PT-151...162
CUMULATIVE PTs: 162
NEW UPDs: 0
NEW GAPS: 0
OPS-UPD-002: CONFIRMED + NARROWED + READY FOR GOVERNED PROMOTION
OPS-GAP-007: OPEN
OPS-GAP-009: OPEN
OPS-GAP-004 / OQ-004: PROVIDER EMPIRICAL PROOF STILL OPEN
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED
```

Stop after this bounded pass.
