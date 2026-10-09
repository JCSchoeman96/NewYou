# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.5.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.4.0`. Read those predecessors first for the accepted start, entitlement, expiry, subscription, recovery, submission and concurrency semantics. This file appends the accepted unfinished-assessment notification contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.5.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.4.0.md`
- **Predecessor blob SHA:** `cfc2e52b6ee8dd2c6b55631fd756259c0732ecf7`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-009 — Unfinished-assessment notification contract

**Accepted:** `2026-10-08`

Every authoritative started Assessment Attempt must expose its exact authoritative expiry deadline and a persistent in-product continuation path while the attempt remains active.

### AT-WD-009A — Required participant-facing warning schedule

The accepted launch working schedule is:

1. start confirmation when the first scored answer is durably accepted;
2. reminder at 14 days remaining;
3. reminder at 7 days remaining;
4. reminder at 3 days remaining;
5. reminder at 24 hours remaining;
6. expiry outcome notice if the attempt terminates unfinished.

All reminder timing derives from the fixed authoritative attempt expiry timestamp. Participant activity does not slide the expiry deadline or create a rolling reminder window.

### AT-WD-009B — Required launch surfaces

At launch:

- in-app state is the persistent product surface for unfinished assessment status, exact expiry and `Continue assessment` access;
- email is the required proactive reach surface for the scheduled reminders and expiry outcome;
- push, SMS, WhatsApp or other channels are not made FP-003 requirements by this decision and remain separately governed future channels.

The exact provider, queue, retry and operational delivery implementation remains outside this Pre-JIT decision.

### AT-WD-009C — Assessment-expiry reminders are service/transactional, not marketing

Unfinished-assessment expiry notices are product/service communications tied to an active paid or entitled assessment obligation. Marketing unsubscribe/preference state must not silently suppress these required product-expiry notices merely because both may use email.

This working semantic does not itself make a legal/privacy sufficiency finding; applicable legal/privacy review remains separate.

### AT-WD-009D — Communications does not own attempt validity

Temperament remains authoritative for the attempt and its expiry timestamp. Communications owns communication-obligation/delivery evidence according to its own governed boundaries.

Therefore:

- failed email delivery does not extend the assessment attempt;
- an unopened reminder does not extend the attempt;
- missing open/click tracking does not invalidate the expiry;
- Communications state must not become a second source of truth for whether the Assessment Attempt is active or expired.

### AT-WD-009E — Material platform warning failure may inform technical-recovery adjudication

A material platform failure to establish the required warning obligations — for example a defect causing no start warning, no usable in-app warning and no required expiry reminders to be established — does not automatically resurrect, extend or reverse an expired attempt.

However, that failure may be relevant evidence in the governed technical-recovery adjudication defined by `AT-WD-006`.

### AT-WD-009F — Reminder obligations stop when no longer applicable

Future unfinished-attempt reminders cease when:

- authoritative final submission is accepted;
- the attempt expires or is otherwise terminally disposed;
- another governed lifecycle event makes the unfinished-attempt reminder no longer truthful.

The expiry outcome notice may still be issued after terminal expiry where applicable.

### AT-WD-009G — Expiry outcome must reflect current entitlement truth

Expiry messaging must be rendered from current authoritative owner truth rather than a generic hard-coded promise.

Examples:

- standalone ordinary expiry must not falsely promise a free replacement;
- an eligible active subscriber whose initial included completed assessment remains unfulfilled may be told that another attempt is available under the accepted subscription working model;
- an ended subscription must not be told that ordinary subscription replacement remains available unless another valid entitlement or technical-recovery obligation actually exists.

---

# 2. Pressure-test additions — v0.5.0

## AT-PT-045 — Start confirmation after first-answer commitment

**Scenario:** first scored answer is durably accepted and the attempt starts.

**Expected:** participant can see the exact expiry deadline and persistent continuation route; launch communication obligations for the started attempt are established.

**Result:** `PASS` under AT-WD-009A/B.

## AT-PT-046 — Participant actively answers near reminder milestones

**Scenario:** participant saves answers shortly before the 14-day or 7-day reminder milestone.

**Expected:** activity does not reset the fixed deadline or reminder schedule. Reminder truth derives from the remaining time to authoritative expiry.

**Result:** `PASS` under AT-WD-009A.

## AT-PT-047 — Email bounces but participant later logs in

**Scenario:** required reminder email fails externally; participant later returns to the application.

**Expected:** in-app unfinished status, exact expiry and continue path remain available. Email failure does not change Temperament expiry truth.

**Result:** `PASS` under AT-WD-009B/D.

## AT-PT-048 — Marketing unsubscribe exists

**Scenario:** participant has unsubscribed from marketing email while an unfinished paid/entitled assessment is active.

**Expected:** marketing suppression does not silently suppress the required transactional assessment-expiry notice. Purpose/channel legality remains governed separately.

**Result:** `PASS` under AT-WD-009C.

## AT-PT-049 — Reminder email not opened

**Scenario:** reminder is sent but no reliable evidence proves the participant opened it.

**Expected:** attempt still follows its authoritative deadline. Open/click evidence is not required to establish expiry truth.

**Result:** `PASS` under AT-WD-009D.

## AT-PT-050 — Platform defect creates no required reminders

**Scenario:** a platform bug means required reminder obligations were never established while the attempt proceeds to expiry.

**Expected:** expiry is not automatically rolled back or extended. The warning failure becomes evidence that may be considered under governed technical-recovery adjudication.

**Result:** `PASS` under AT-WD-009E + AT-WD-006.

## AT-PT-051 — Submission accepted before later reminder job runs

**Scenario:** participant final-submits successfully before a queued future reminder executes.

**Expected:** future unfinished-attempt reminder is suppressed/cancelled or revalidated away; the system must not tell a participant a completed assessment is still unfinished.

**Result:** `PASS` under AT-WD-009F.

## AT-PT-052 — Standalone attempt expires

**Scenario:** ordinary standalone assessment expires incomplete.

**Expected:** expiry outcome accurately states that the attempt ended and does not promise an ordinary free replacement. Technical recovery remains separate where justified.

**Result:** `PASS` under AT-WD-009G + AT-WD-005A.

## AT-PT-053 — Active subscriber attempt expires with initial inclusion unfulfilled

**Scenario:** qualifying subscription remains active/good-standing; the initial included completed assessment is still unfulfilled; current attempt expires incomplete.

**Expected:** expiry outcome may offer the governed new-attempt path without erasing the expired attempt or promising multiple completed assessments.

**Result:** `PASS` under AT-WD-009G + AT-WD-005B; upstream Product Law amendment remains required by AT-UPD-003.

---

# 3. Open-question queue after v0.5.0

`AT-OI-004` is resolved by `AT-WD-009` and `AT-PT-045...053`, subject to later governed formalisation and Communications implementation proof.

Next unresolved:

- **AT-OI-005 — Subscription replacement abuse/fair-use boundary:** bounded controls without redefining the one-included-completed-assessment promise.

Later passes still include assessment/methodology/content/language version provenance; result correction/invalidation/supersession; declared vs assessed vs historical/current-profile semantics; reassessment interactions; report generation/publication/access/delivery; identity merge; privacy/retention; Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
