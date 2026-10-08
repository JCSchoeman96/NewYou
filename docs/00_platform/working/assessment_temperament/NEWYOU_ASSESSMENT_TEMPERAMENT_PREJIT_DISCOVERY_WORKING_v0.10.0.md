# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.10.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.9.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification, replacement/retake, execution-provenance, result-correction and profile-source semantics. This file appends the accepted qualifying-completion / annual reassessment interval contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.10.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.9.0.md`
- **Predecessor blob SHA:** `64c50eb50e3f486d601af2ac7f79e588d6e84a87`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-014 — Qualifying completion and annual reassessment interval

**Accepted:** `2026-10-08`

A qualifying completed digital assessment exists only where an authoritatively accepted frozen submission has converged to exactly one canonical valid digital result. For annual-interval purposes, the qualifying completion anchor is the authoritative final-submission acceptance timestamp rather than a later scoring-worker, report-generation or delivery timestamp.

### AT-WD-014A — Accepted submission ends participant work but canonical valid result is required for qualifying completion

Once final submission is authoritatively accepted under `AT-WD-007`, the participant's answer set is frozen and the participant has completed her submission obligation.

However, the platform does not treat the assessment as a qualifying completed digital assessment for future reassessment eligibility until that frozen submission has converged to exactly one canonical valid digital result.

While canonical result generation is pending:

- no second ordinary assessment/reassessment attempt may start from the same participant lifecycle;
- the pending submitted attempt is not treated as expired or abandoned;
- the platform must complete/recover deterministic result production from the same frozen submission;
- no new assessment entitlement is consumed merely because backend result production is delayed.

### AT-WD-014B — Annual interval uses a rolling 12-month boundary

After a qualifying completed digital assessment, an ordinary participant-initiated reassessment may not start until 12 months have elapsed from that assessment's authoritative final-submission acceptance timestamp.

The interval is not reset by:

- calendar-year rollover;
- membership anniversary alone;
- report generation or download;
- current-profile selection change;
- declaration change;
- corrective recalculation that is not a new assessment.

The reassessment start boundary is the ordinary first-answer commitment. Viewing/opening the assessment before eligibility does not create an attempt, but a first scored answer must fail closed while the annual interval remains closed.

### AT-WD-014C — Entitlement and interval are independent gates

A valid commercial reassessment entitlement does not by itself make an early reassessment lawful.

An ordinary reassessment may start only where both are true:

1. an applicable reassessment entitlement/right is valid; and
2. the rolling annual interval is open.

This applies to ordinary paid retakes and Premium annual reassessment unless a separately governed remediation rule expressly supersedes ordinary reassessment timing.

### AT-WD-014D — Premium anniversary/renewal does not override the annual interval

DEC-035 Premium eligibility and DEC-034 annual reassessment frequency are separate constraints.

A Premium annual reassessment entitlement may exist while the ordinary annual interval remains closed. The participant may not start the reassessment until both gates are satisfied.

Exact Entitlements Resource/state representation is deferred to JIT work.

### AT-WD-014E — Premium annual reassessment is one annual opportunity, not a guarantee of one completed reassessment

Once a Premium reassessment attempt begins through the first durably accepted scored answer, the applicable annual Premium reassessment entitlement is consumed under the ordinary first-answer consumption rule.

Ordinary abandonment or expiry of that Premium reassessment attempt:

- does not automatically regenerate the annual Premium reassessment right;
- does not produce a qualifying completed result;
- therefore does not establish a new annual completed-assessment anchor;
- remains distinct from the accepted initial-subscription promise of one included successfully completed first digital assessment.

Technical recovery remains separately governed under `AT-WD-006`.

### AT-WD-014F — Incomplete ordinary attempts do not create or move the completed-assessment anchor

An expired or otherwise incomplete attempt that never produces a qualifying canonical valid result does not establish a new annual reassessment baseline.

Whether a later attempt is commercially available depends on the owning entitlement/recovery semantics applicable to the consumed right; Temperament must not infer a replacement merely from the absence of a result.

### AT-WD-014G — Corrective results do not reset the interval

A corrective result created under `AT-WD-012B` from the same frozen answers and same valid governed assessment context is not a new participant assessment.

Therefore it does not reset the annual interval. The original qualifying final-submission timestamp remains the anchor.

### AT-WD-014H — Governed remediation is not an ordinary retake

A technical-recovery successor or methodology-defect remediation authorised because the platform could not validly honour the participant's assessment obligation is not an ordinary participant-initiated retake and is not blocked merely because the ordinary annual interval is closed.

The remediation must remain explicitly linked to the failed/invalidated assessment history and may not be disguised as an ordinary free retake.

Once a valid remedial assessment completes, that valid completion becomes the baseline for subsequent ordinary reassessment timing.

### AT-WD-014I — Plan regeneration remains downstream of assessment result truth

DEC-036 complimentary plan regeneration, where applicable, is a downstream consequence of a materially different qualifying digital result. It does not create, consume, move or reset assessment/reassessment eligibility by itself.

Assessment result truth remains upstream of plan regeneration.

---

# 2. Upstream clarification addition

## AT-UPD-005 — Product Law must define the annual retake interval anchor and remediation interaction

**Status:** `REQUIRED BEFORE GOVERNED FP-003 CONTRACT COMPLETION`

Current Product Law states that no more than one assessment retake per year is permitted when a valid entitlement exists, but does not explicitly define:

1. whether the year is rolling or calendar-based;
2. which event anchors the interval;
3. whether Premium annual entitlement can exist while the interval remains closed;
4. whether incomplete/expired reassessment attempts move the interval;
5. whether corrective result generation resets the interval;
6. how technical or methodology-defect remediation composes with the ordinary retake interval.

The accepted working direction is the rolling 12-month model in `AT-WD-014`. This requires explicit upstream Product Law clarification rather than silent implementation inference.

---

# 3. Pressure-test additions — v0.10.0

## AT-PT-091 — Submission accepted before delayed canonical result

**Scenario:** final submission is accepted on 8 October 2026 at 14:00; canonical result is not persisted until 9 October because backend scoring is delayed.

**Expected:** participant cannot start another assessment while result generation is pending. Once the valid result exists, the annual interval anchor remains 8 October 2026 at 14:00, not the later worker/result timestamp.

**Result:** `PASS` under AT-WD-014A/B.

## AT-PT-092 — Calendar year changes shortly after completion

**Scenario:** qualifying assessment completes on 20 December; participant has a valid paid reassessment right on 2 January.

**Expected:** January calendar rollover does not reopen reassessment. The rolling 12-month interval remains closed until the corresponding December boundary.

**Result:** `PASS` under AT-WD-014B/C.

## AT-PT-093 — Premium anniversary arrives one month after first completed result

**Scenario:** Premium condition becomes satisfied on 1 January but participant's first qualifying digital assessment completed on 1 December.

**Expected:** Premium entitlement may exist, but no Premium reassessment attempt may start until 1 December of the following year, assuming entitlement remains valid and no separate remediation applies.

**Result:** `PASS` under AT-WD-014C/D.

## AT-PT-094 — Reassessment started exactly when rolling interval opens

**Scenario:** 12 months have elapsed from the prior qualifying final-submission timestamp and an applicable valid reassessment entitlement exists.

**Expected:** first-answer commitment may start the new reassessment subject to all other ordinary guards.

**Result:** `PASS` under AT-WD-014B/C.

## AT-PT-095 — Attempt to start reassessment one day early

**Scenario:** valid entitlement exists but the annual interval opens tomorrow.

**Expected:** viewing may occur, but first scored answer/start fails closed. No attempt is created and no reassessment entitlement is consumed merely by viewing.

**Result:** `PASS` under AT-WD-014B/C + AT-WD-002.

## AT-PT-096 — Premium reassessment starts then expires incomplete

**Scenario:** eligible Premium annual reassessment begins, first answer is accepted, and the attempt later expires without final submission.

**Expected:** Premium annual right was consumed at first answer; ordinary expiry does not regenerate it. No qualifying result exists, so no new completed-assessment anchor is created.

**Result:** `PASS` under AT-WD-014E/F.

## AT-PT-097 — Corrective recalculation issued after software defect

**Scenario:** March assessment is validly completed; April correction produces R2 from the same frozen answers/context because of a platform computation bug.

**Expected:** R2 does not count as a new assessment and does not move the rolling annual interval. March final-submission timestamp remains the anchor.

**Result:** `PASS` under AT-WD-014G + AT-WD-012B.

## AT-PT-098 — Technical recovery needed while ordinary interval would be closed

**Scenario:** platform technical failure invalidates the participant's attempt/result and a governed recovery successor is authorised before 12 months have elapsed.

**Expected:** ordinary retake interval does not block the explicit remediation. Recovery remains linked to the failed service obligation rather than being treated as an ordinary retake.

**Result:** `PASS` under AT-WD-014H + AT-WD-006.

## AT-PT-099 — Methodology defect invalidates previous result

**Scenario:** prior result is invalidated because the governed methodology itself is materially defective; authorised remediation requires a fresh assessment before 12 months.

**Expected:** remediation may proceed under explicit methodology/product authority; no silent V2 recalculation occurs. Completed valid remediation becomes the future ordinary reassessment baseline.

**Result:** `PASS` under AT-WD-014H + AT-WD-012C.

## AT-PT-100 — Current profile changes without new assessment

**Scenario:** participant switches current profile from one eligible historical source to another.

**Expected:** annual reassessment interval is unchanged because profile selection is not a new assessment.

**Result:** `PASS` under AT-WD-014B + AT-WD-013.

## AT-PT-101 — Materially different reassessment triggers plan regeneration

**Scenario:** a legitimate later reassessment produces a materially different digital result and DEC-036 plan-regeneration conditions apply.

**Expected:** result may create a downstream complimentary plan-regeneration opportunity, but plan regeneration does not alter assessment completion history or reassessment interval.

**Result:** `PASS` under AT-WD-014I.

---

# 4. Open-question queue after v0.10.0

The reassessment-interaction cluster is now materially constrained by `AT-WD-014`, `AT-UPD-005` and `AT-PT-091...101`, subject to explicit upstream Product Law clarification and later Entitlements/Temperament JIT representation.

Next unresolved cluster:

- **Report generation / publication / access / delivery:** bind immutable result to exact governed report content and locale, distinguish original delivered snapshot from later approved interpretation, define retry/idempotency and missing-locale fail-closed behavior, preserve permanent access semantics, and determine what constitutes successful delivery without rescoring.

Later passes still include identity merge; privacy/retention; Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
