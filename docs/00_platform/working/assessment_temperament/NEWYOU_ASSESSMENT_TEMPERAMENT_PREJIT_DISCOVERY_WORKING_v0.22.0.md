# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.22.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.21.0`. Read those predecessors first for `AT-WD-001...019`, the final adversarial sweep, accepted upstream/cross-domain correction contracts, and the identity-reconciliation successor.
>
> Nothing in this file itself amends Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.22.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.21.0.md`
- **Predecessor blob SHA:** `e6e097d98b970e26f800b6a46534218c32880b4c`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Live canonical `main` revalidation pin:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `FINAL REVALIDATION — AT-WD-020 + AT-UPD-007 ACCEPTED`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET PARKED — FINAL CONDITIONAL-GATE CHECK REQUIRED`

---

# 1. Accepted semantic correction

## AT-WD-020 — Dual-clock ordinary annual reassessment guard

**Accepted:** `2026-10-08`

`AT-WD-020` partially supersedes only the annual-timing portions of `AT-WD-014B`, `AT-WD-014E`, and `AT-WD-014F`. All unaffected `AT-WD-014` semantics remain in force.

Current Product Law distinguishes a qualifying completed assessment from the annual assessment-use/retake interval. A completion-only clock is insufficient because an ordinary reassessment could start, expire incomplete, and otherwise leave the participant able to start another ordinary reassessment immediately.

The corrected ordinary reassessment model therefore uses two independent rolling 12-calendar-month guards plus entitlement eligibility.

### AT-WD-020A — Completion-recency guard

An ordinary participant-initiated reassessment may not start until at least 12 calendar months have elapsed from the most recent qualifying valid digital assessment completion.

The completion anchor remains the authoritative final-submission acceptance timestamp for that qualifying assessment once its frozen submission has converged to exactly one canonical valid result.

The completion guard is not reset by:

- report generation, delivery, opening or download;
- current-profile selection changes;
- declaration changes;
- reviewed interpretation;
- same-assessment corrective result generation;
- calendar-year rollover;
- membership anniversary by itself.

### AT-WD-020B — Ordinary reassessment-use guard

Once an ordinary reassessment actually starts at the first durably accepted scored-answer commitment, another ordinary reassessment may not start until at least 12 calendar months have elapsed from that ordinary reassessment start.

This use guard is established even if the reassessment later:

- is abandoned;
- expires incomplete;
- closes without a qualifying result for an ordinary non-technical reason.

Opening/viewing the assessment or reaching a Start surface does not establish this guard. The boundary remains the first durably accepted scored answer.

### AT-WD-020C — Start gate

For an ordinary reassessment, all applicable conditions must independently be satisfied:

1. the completion-recency guard is open;
2. the ordinary reassessment-use guard is open;
3. an applicable valid assessment entitlement/right exists;
4. all other ordinary attempt guards pass.

Conceptually:

`next ordinary reassessment start >= max(latest qualifying completion + 12 calendar months, latest ordinary reassessment start + 12 calendar months)`

with a valid entitlement still required independently.

### AT-WD-020D — Successful reassessment naturally advances the stricter completion anchor

If an ordinary reassessment starts and later successfully completes, the qualifying completion occurs after the reassessment start. That later completion becomes the relevant completion-recency anchor and will normally be the stricter next ordinary boundary.

If the reassessment never produces a qualifying valid result, the reassessment-start/use guard remains the blocker for the next ordinary reassessment.

### AT-WD-020E — Premium entitlement remains independent

DEC-035 Premium annual reassessment entitlement availability is a separate commercial clock.

Premium entitlement availability does not override either annual reassessment guard. A Premium right may exist while an ordinary reassessment remains temporally ineligible. If membership ends before the participant can lawfully use that Premium right, the existing non-accumulating/expiry-on-membership-end rule remains authoritative unless Product Law is separately amended.

Once a Premium reassessment starts, first durable scored-answer commitment consumes the applicable Premium right under the accepted first-answer consumption contract and establishes the ordinary reassessment-use guard.

Ordinary abandonment/expiry does not regenerate the Premium right and does not erase the use guard.

### AT-WD-020F — Corrections and remediation

A same-assessment corrective result derived from the same frozen answers and same valid governed methodology context does not create a new assessment and does not reset either ordinary annual guard.

Explicit technical or methodology-defect remediation remains outside the ordinary retake restriction where separately authorised. If remediation requires and successfully completes a genuinely fresh governed assessment, that valid remediation completion becomes the qualifying completion baseline for later ordinary reassessment timing.

---

# 2. Accepted upstream Product-law correction contract

## AT-UPD-007 — Ordinary annual reassessment timing

**Accepted working correction direction:** `2026-10-08`

Product Law must define the one-retake-per-year rule as a rolling 12-calendar-month ordinary assessment-use restriction rather than a calendar-year reset.

An ordinary reassessment may start only when:

1. at least 12 calendar months have elapsed from the most recent qualifying valid digital assessment completion;
2. at least 12 calendar months have elapsed from the most recent ordinary reassessment first-answer/start commitment, where one exists;
3. an applicable valid entitlement exists;
4. all other attempt guards pass.

Starting an ordinary reassessment establishes the annual use guard even if the attempt later expires incomplete. A later valid completion establishes the later completion anchor.

Premium entitlement availability under DEC-035 remains independent and cannot override either annual interval. Same-assessment corrective results do not reset either guard. Explicit platform/methodology remediation is not an ordinary retake; a fresh successfully completed remediation becomes the qualifying completion baseline for subsequent ordinary reassessment.

### AT-UPD-007A — Traceability renumbering

The annual-retake upstream item was originally labelled `AT-UPD-005` in `v0.10.0`. That predecessor remains immutable.

For current traceability only, the annual-retake correction is now `AT-UPD-007` because `AT-UPD-005` is already the accepted assessment-expiry reminder-routing correction recorded in `v0.20.0`.

These are local non-governed working identifiers; the renumbering changes no semantic authority.

---

# 3. Pressure tests

## AT-PT-202 — First reassessment after initial valid completion

**Scenario:** qualifying assessment completes 15 March 2027; valid reassessment entitlement exists before March 2028.

**Expected:** no ordinary reassessment may start before 15 March 2028.

**Result:** `PASS` under AT-WD-020A/C.

## AT-PT-203 — Reassessment starts and expires incomplete

**Scenario:** earliest lawful reassessment starts 15 March 2028 and later expires without a qualifying result.

**Expected:** another ordinary reassessment cannot start before 15 March 2029 even though the most recent qualifying result remains the 2027 result.

**Result:** `PASS` under AT-WD-020B/D.

## AT-PT-204 — Reassessment starts and completes later

**Scenario:** ordinary reassessment starts 15 March 2028 and qualifying final submission is accepted 4 April 2028.

**Expected:** next ordinary reassessment may not start before 4 April 2029 because the later completion anchor is stricter than the March start anchor.

**Result:** `PASS` under AT-WD-020A/B/D.

## AT-PT-205 — Premium right matures while interval remains closed

**Scenario:** Premium entitlement becomes available 1 January 2028; latest qualifying completion was 1 December 2027.

**Expected:** Premium right may exist but reassessment cannot start until the annual guards permit it. Membership ending before then follows the existing Premium expiry rule.

**Result:** `PASS` under AT-WD-020C/E.

## AT-PT-206 — Viewing assessment early

**Scenario:** participant opens the reassessment surface one day before the interval opens.

**Expected:** no attempt/start/use guard or entitlement consumption occurs; first scored answer fails closed while timing is ineligible.

**Result:** `PASS` under AT-WD-002 + AT-WD-020B/C.

## AT-PT-207 — Same-answer corrective result

**Scenario:** a software defect is corrected after the prior valid assessment using the same frozen answers and methodology context.

**Expected:** neither annual guard changes.

**Result:** `PASS` under AT-WD-012B + AT-WD-020F.

## AT-PT-208 — Methodology remediation inside annual interval

**Scenario:** methodology authority invalidates the prior assessment and explicit fresh remediation is required before 12 months.

**Expected:** remediation may proceed outside the ordinary retake restriction. A successfully completed remediation becomes the new future completion baseline.

**Result:** `PASS` under AT-WD-012C + AT-WD-020F.

---

# 4. Status after acceptance

Accepted working semantics now include `AT-WD-001...020`.

Accepted upstream/cross-domain correction contracts:

- `AT-UPD-001` — first scored-answer assessment-credit consumption authority;
- `AT-UPD-002` — methodology-authority Domain wording alignment;
- `AT-UPD-004` — result correction/invalidation/supersession Product semantics;
- `AT-UPD-005` — FP-003 / OQ-017 assessment-expiry reminder routing;
- `AT-UPD-006` — cross-domain identity reconciliation;
- `AT-UPD-007` — ordinary annual reassessment timing.

`AT-UPD-003` remains a conditional Product-law gap concerning a future subscription offer that promises one included successfully completed initial digital assessment. It must be formalised before such an offer is activated; final revalidation must decide whether that conditional gap blocks parking FP-003 itself.

**Next:** perform final live-authority and conditional-gate revalidation before any park decision.
