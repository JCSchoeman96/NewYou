# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.6.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.5.0`. Read those predecessors first for the accepted start, entitlement, expiry, subscription, technical-recovery, submission, concurrency and notification semantics. This file appends the accepted subscription replacement / retake boundary and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.6.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.5.0.md`
- **Predecessor blob SHA:** `7e6994a9e5752fe16bafd810c18b1ffd722daec4`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-010 — Subscription initial-assessment replacement boundary

**Accepted:** `2026-10-08`

An expired incomplete Assessment Attempt used while pursuing an **unfulfilled included initial digital assessment** is not, by itself, an assessment retake/reassessment and does not consume the annual completed-assessment retake allowance.

The participant is still pursuing fulfilment of the original included initial-assessment benefit until one qualifying digital assessment successfully completes.

### AT-WD-010A — Ordinary replacement eligibility

A new ordinary subscription-funded attempt may become available only when all applicable conditions are true:

1. the qualifying subscription is active and in good standing at the new attempt start;
2. the initial included qualifying digital assessment remains unfulfilled;
3. no Assessment Attempt is currently active;
4. the preceding attempt is terminally incomplete/expired or otherwise lawfully closed without producing the qualifying completed assessment;
5. no separate rule or technical-recovery path already governs the next attempt.

The new attempt remains subject to the ordinary first-answer start boundary, fixed 30-day lifetime, pinned governed assessment context, submission rules and history-preservation requirements.

### AT-WD-010B — Replacement opportunities do not accumulate as credits

Repeated incomplete expiry does not build a numerical balance of unused replacement credits.

The durable commercial meaning is closer to:

`included initial digital assessment = unfulfilled`

than:

`replacement-credit balance = N`.

At any time the participant may have at most the currently applicable opportunity permitted by owner truth. Expired predecessors remain historical evidence and are not converted into stored future credits.

### AT-WD-010C — Repeated ordinary expiry alone is not abuse

Repeated failure to complete an assessment is not, by itself, fraud or abuse and does not extinguish the accepted working promise of one included qualifying completed initial digital assessment while the subscription remains eligible.

This Pre-JIT therefore does not create an arbitrary assessment-specific maximum such as two, three or five failed attempts.

General fraud, account-security, payment, rate-limiting and platform-abuse controls may still apply under their owning authorities, but they may not silently redefine the assessment entitlement or fabricate completed/consumed assessment truth.

Evidence-backed Product Law may introduce a future bounded policy if real operational or commercial evidence demonstrates a justified need. That future policy must be explicit rather than inferred from this working discovery.

### AT-WD-010D — Incomplete predecessors do not consume annual retake allowance

The annual retake/reassessment interval applies to a participant seeking another qualifying assessment after a prior qualifying completed digital assessment, subject to valid entitlement.

An attempt that expires or otherwise terminates before authoritative final submission/result completion does not itself become the participant's annual completed-assessment retake.

Therefore a sequence such as:

`Attempt A expired incomplete`
→ `Attempt B expired incomplete`
→ `Attempt C completed initial assessment`

contains one qualifying completed initial digital assessment, not three annual retakes.

### AT-WD-010E — Completion closes the initial-replacement pathway

Once one qualifying digital assessment successfully completes under the initial included-assessment benefit:

- the initial inclusion becomes fulfilled;
- no further ordinary replacement attempts arise from that initial inclusion;
- later assessment eligibility is governed by ordinary paid retake/reassessment and Premium reassessment law;
- historical incomplete attempts remain preserved subject to retention/deletion law.

### AT-WD-010F — Subscription termination and later resubscription

If the subscription ends while no active attempt and no technical-recovery obligation survives, ordinary replacement eligibility from that ended subscription ends.

A later qualifying subscription purchase may establish a new or restored commercial assessment inclusion only if the then-governing product/offer/entitlement terms say so. Temperament does not infer that commercial right merely from historical subscription status.

Historical expired attempts are never erased merely because the participant later resubscribes.

### AT-WD-010G — Support may not erase history or manufacture ordinary credits

Support may:

- explain attempt status and expiry;
- assist the participant to use a legitimately available next attempt;
- initiate or adjudicate governed technical-recovery processes where authorised;
- request correction of an entitlement error through the owning Domain.

Support may not silently:

- erase an expired attempt;
- mark an incomplete attempt as though it never consumed its start consequence;
- manufacture an ordinary replacement credit outside governing entitlement truth;
- bypass annual retake or Premium reassessment law.

---

# 2. Pressure-test additions — v0.6.0

## AT-PT-054 — First subscription attempt expires incomplete

**Scenario:** active/good-standing subscriber starts the included initial assessment; it expires incomplete; no prior qualifying completed digital assessment exists.

**Expected:** predecessor attempt remains terminal history; initial inclusion remains unfulfilled; participant may become eligible to start the next ordinary replacement attempt. The expired attempt is not counted as an annual reassessment.

**Result:** `PASS` under AT-WD-010A/D; upstream Product Law amendment remains required by AT-UPD-003.

## AT-PT-055 — Three consecutive incomplete expiries

**Scenario:** subscriber repeatedly starts an attempt, allows each fixed 30-day window to expire, and still has no qualifying completed digital assessment.

**Expected:** no accumulated credit balance is created; no completed results/reports are produced; repeated expiry alone does not extinguish the initial inclusion while the subscription remains eligible. Only one active attempt may exist at a time.

**Result:** `PASS` under AT-WD-010A/B/C.

## AT-PT-056 — Arbitrary support cap after third expiry

**Scenario:** support policy tries to deny any further initial-assessment attempt solely because three ordinary attempts expired.

**Expected:** rejected under the accepted working model unless explicit future Product Law establishes an evidence-backed cap. Support cannot silently convert the promise into a fixed number of chances.

**Result:** `PASS` under AT-WD-010C/G.

## AT-PT-057 — Incomplete attempts followed by first completion

**Scenario:** Attempts A and B expire incomplete; Attempt C is authoritatively submitted and produces the first qualifying digital result.

**Expected:** initial inclusion becomes fulfilled exactly once at completion. A and B remain historical incomplete attempts. Future assessment eligibility now follows retake/reassessment rules rather than initial-replacement semantics.

**Result:** `PASS` under AT-WD-010D/E.

## AT-PT-058 — Completed assessment then participant asks for another 'replacement'

**Scenario:** subscriber has already completed the initial included digital assessment and requests another ordinary replacement on the basis that an earlier historical attempt expired.

**Expected:** no initial-replacement eligibility remains. Historical earlier expiry does not reopen the fulfilled initial benefit. Any new assessment requires valid retake/reassessment entitlement and timing.

**Result:** `PASS` under AT-WD-010E.

## AT-PT-059 — Subscription ends after incomplete expiry

**Scenario:** attempt expires incomplete, then subscription ends before another attempt is started; no genuine technical-recovery obligation exists.

**Expected:** ordinary subscription replacement eligibility ends with the subscription. Historical attempt remains. No free-standing replacement credit survives merely because the inclusion was unfulfilled.

**Result:** `PASS` under AT-WD-010F and AT-WD-005C.

## AT-PT-060 — Later resubscription

**Scenario:** participant had prior incomplete expired attempts, subscription ended, and months later purchases another subscription offer.

**Expected:** historical attempts remain unchanged. Whether a new initial-assessment inclusion exists is determined by the new offer/Entitlements truth, not inferred by Temperament and not automatically denied because of historical failed attempts.

**Result:** `PASS` under AT-WD-010F.

## AT-PT-061 — Support 'reset attempts' action

**Scenario:** participant asks support to reset all failed attempts so the history looks unused.

**Expected:** prohibited. Support may enable only a legitimately authorised new attempt/recovery path; historical attempt and consumption evidence remains truthful.

**Result:** `PASS` under AT-WD-010G.

## AT-PT-062 — Security/fraud concern during repeated attempts

**Scenario:** repeated attempt activity coincides with evidence of account compromise or automated abuse.

**Expected:** owning security/fraud controls may suspend or constrain activity according to their authority, but the platform must not rewrite historical assessment truth or silently invent a new assessment-specific entitlement rule.

**Result:** `PASS` under AT-WD-010C/G; exact security response remains outside this Pre-JIT stream.

---

# 3. Open-question queue after v0.6.0

`AT-OI-005` is resolved by `AT-WD-010` and `AT-PT-054...062`, subject to the upstream Product Law amendment already tracked by `AT-UPD-003`.

The first attempt/entitlement/expiry/submission/concurrency/notification/replacement pass is now semantically stable enough to move to the next discovery cluster.

Next major unresolved cluster:

- **assessment/methodology/content/language version provenance:** define exactly what is pinned at attempt start, what may change before submission, what version inputs reproduce the result, and how language/content variants relate to one methodology version without becoming competing methodology authority;
- **result correction/invalidation/supersession**;
- **declared vs assessed vs historical/current-profile semantics**;
- **reassessment interactions**;
- **report generation/publication/access/delivery**;
- **identity merge**;
- **privacy/retention**;
- **Research/Interactive isolation**;
- **Methodology Authority Input Contract**;
- **final adversarial sweep**.
