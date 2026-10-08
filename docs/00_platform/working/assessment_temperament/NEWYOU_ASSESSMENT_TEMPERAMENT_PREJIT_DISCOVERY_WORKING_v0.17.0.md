# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.17.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.16.0`. Read those predecessors first for `AT-WD-001...019`, the final adversarial sweep, and the complete upstream-delta register. This file records the user's acceptance of the `AT-UPD-001` assessment-credit consumption correction contract and the additional pressure tests needed to preserve that correction across Product, Domain and Roadmap authority.
>
> Nothing in this file itself amends Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.17.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.16.0.md`
- **Predecessor blob SHA:** `3f620dc8da5681a6f487d96246d985868d3b6a03`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Live canonical `main` revalidation pin:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `UPSTREAM RECONCILIATION — AT-UPD-001 ACCEPTED; AT-UPD-002 NEXT`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `CHANGES REQUIRED UPSTREAM / NOT ELIGIBLE FOR PARK`

---

# 1. Accepted upstream correction contract

## AT-UPD-001 — Align assessment-credit consumption authority

**Accepted working correction direction:** `2026-10-08`

The upstream Product/Domain/Roadmap successor set must converge on one consumption boundary:

> **An assessment right is consumed when the first scored answer is durably accepted into the authoritative Assessment Attempt.**

Opening the assessment, viewing questions, pressing a participant-facing Start control, loading an attempt shell, or saving optional non-scoring feedback does not consume the assessment right.

The same authoritative first-scored-answer commitment establishes the attempt start semantics already accepted in `AT-WD-001...003`:

- exactly one authoritative active attempt exists for the participant/right combination;
- the first scored answer is durably saved;
- the governed assessment execution context/version is pinned;
- the fixed 30-day attempt lifetime begins;
- Entitlements consumes exactly one applicable assessment right idempotently; and
- Temperament records its own attempt commitment/lifecycle state without becoming commercial-credit authority.

Result calculation, report generation, protected report availability, notification delivery, email receipt/opening and participant report download are later fulfilment/delivery events. They do not determine whether the original assessment right was consumed.

## 1.1 Product wording corrections required

A future Product-law successor must remove or supersede wording that says a digitally assessed/included assessment credit is consumed only after successful assessment delivery.

The provenance/credit matrix should instead express the commercial boundary conceptually as:

- `digitally_assessed` → assessment right consumed at first durably accepted scored answer;
- `later_digital_completion` → same consumption boundary for the applicable new assessment right;
- self-reported/book-derived declarations do not consume a digital assessment right.

`DEC-055` should be sharpened from generic "first answer saved" wording to the materially precise rule: **first scored answer durably accepted**. Optional feedback or other non-scoring input must not accidentally trigger consumption.

## 1.2 Technical-failure correction required

The commercial-reversal/technical-failure model must distinguish failure timing rather than using a generic `unconsumed until success/replacement` phrase.

Required semantics:

1. **Before first-scored-answer commitment:** no assessment use occurred; the original right remains unused if a technical failure prevents commitment.
2. **After commitment, attempt still recoverable:** the original right remains consumed; recover the same attempt without manufacturing a replacement right.
3. **After commitment, material genuine platform failure makes attempt unrecoverable:** preserve original consumed attempt/right history and use an explicit no-additional-payment recovery successor or applicable refund/remedy authority.
4. **Unknown final-submit outcome:** reconcile before granting replacement or refund that assumes no canonical result exists.
5. **Canonical result already exists:** assessment consumption remains historical; downstream report/render/delivery recovery cannot restore or manufacture an assessment right.
6. **Refund after consumed use:** preserve attempt, consumption, failure and refund evidence. Refund does not rewrite history to say the right was never consumed.

These rules compose with `AT-WD-006`; they do not create a second technical-recovery model.

## 1.3 Domain ownership correction required

Current Domain Law correctly gives Entitlements command authority over access redemption/consumable credit, but the detailed Temperament profile uses the phrase `attempt consumption state`.

A future Domain-law hygiene successor should make the distinction explicit:

- **Temperament owns:** attempt commitment/lifecycle state and the assessment-side fact that first-answer commitment occurred;
- **Entitlements owns:** the actual commercial assessment-right identity, availability, consumption/redemption, validity and replacement/remediation access consequence.

`attempt consumption state` should therefore be replaced or qualified as `attempt commitment/lifecycle state`. No shared-write commercial-credit authority is permitted.

## 1.4 Roadmap correction required

FP-003 must no longer state or imply that the included assessment credit remains unused until successful assessment delivery.

The FP-003 exit/validation contract should instead require proof that:

- first-scored-answer commitment consumes exactly one applicable assessment right;
- duplicate/retried commitment cannot double-consume or create duplicate active attempts;
- duplicate/retried final submission cannot create a second canonical result;
- result/report generation and report delivery remain independently recoverable after consumption; and
- genuine technical remediation never silently converts a consumed historical right back into an unused right.

---

# 2. Accepted invariant

The cross-authority invariant is now:

```text
paid/granted right exists but no scored answer committed
→ assessment right is UNUSED

first scored answer durably accepted
→ exactly one attempt starts
→ exactly one applicable assessment right becomes CONSUMED

all later assessment/result/report failures
→ recovery / remediation / refund / delivery handling
→ never retroactive ordinary unconsumption
```

The first-answer operation is a cross-domain convergence problem, not shared ownership. The implementation mechanism remains JIT/Architecture-proof work; the durable semantic outcome above is the required authority contract.

---

# 3. Pressure-test additions — v0.17.0

## AT-PT-191 — Optional feedback saved before first scored answer

**Scenario:** participant opens the assessment and saves an optional feedback field before answering any scored item.

**Expected:** no attempt consumption and no 30-day assessment lifetime begins merely from optional non-scoring feedback.

**Result:** `PASS` under accepted AT-UPD-001 + AT-WD-001/002.

## AT-PT-192 — First scored answer commits while response is lost

**Scenario:** the first scored answer is durably accepted and Entitlements consumes the right, but the browser loses the success response and retries.

**Expected:** retry reconciles to the same attempt/consumption commitment; no second consumption, second attempt or restored unused right.

**Result:** `PASS` under AT-WD-003 + accepted AT-UPD-001.

## AT-PT-193 — First scored answer rejected before durable acceptance

**Scenario:** validation/database failure prevents the first scored answer from being durably accepted.

**Expected:** no attempt start and no commercial consumption. Retry may proceed against the still-unused right.

**Result:** `PASS` under AT-WD-001/002 + accepted AT-UPD-001.

## AT-PT-194 — Result generation fails after first-answer consumption

**Scenario:** participant completes and submits correctly, but deterministic result generation temporarily fails.

**Expected:** the assessment right remains consumed; resume/replay the same frozen submission path. Do not grant an ordinary unused credit merely because result generation is delayed.

**Result:** `PASS` under AT-WD-006/007 + accepted AT-UPD-001.

## AT-PT-195 — Support refund after material post-start technical failure

**Scenario:** genuine platform defect irrecoverably destroys a started attempt and the governed remedy is refund rather than successor recovery.

**Expected:** Commerce/Entitlements apply the refund/access consequence, while historical evidence continues to show that the original attempt crossed first-answer consumption before failure. Refund does not rewrite the original use event.

**Result:** `PASS` under AT-WD-006G + accepted AT-UPD-001.

## AT-PT-196 — Temperament tries to restore commercial credit directly

**Scenario:** assessment support code sees a failed Temperament attempt and attempts to mark an assessment credit unused without invoking Entitlements.

**Expected:** prohibited. Temperament may establish the recovery/failure fact and request the governed consequence; Entitlements owns commercial right mutation.

**Result:** `PASS` under AT-WD-003 + accepted AT-UPD-001 Domain refinement.

## AT-PT-197 — Roadmap proof tests report success but not first-answer consumption

**Scenario:** FP-003 proves report delivery but never proves first-answer consumption idempotency/convergence.

**Expected:** insufficient proof. Successful downstream delivery cannot substitute for proof of the authoritative consumption boundary.

**Result:** `ROADMAP/FP CONTRACT CORRECTION REQUIRED` under accepted AT-UPD-001.

---

# 4. Status after acceptance

`AT-UPD-001` is **semantically resolved in this working stream** but remains **unresolved in governing authority** until an explicit upstream Product/Domain/Roadmap successor is approved and this stream is revalidated against its resulting canonical SHA.

No current authority file was modified by this acceptance.

Next upstream defect for adjudication:

- **AT-UPD-002 — Align Temperament methodology-authority wording to DEC-309.**

The overall disposition remains:

**CHANGES REQUIRED UPSTREAM / DO NOT PARK.**
