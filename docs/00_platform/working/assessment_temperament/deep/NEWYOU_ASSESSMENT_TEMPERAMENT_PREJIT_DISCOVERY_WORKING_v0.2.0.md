# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.2.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor **does not replace or rewrite** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.1.0.md`. The v0.1.0 bytes remain the preserved base ledger containing `AT-WD-001...005`, `AT-PT-001...017`, `AT-UPD-001...003`, lifecycle sketches and the open-question queue.
>
> This v0.2.0 file appends the accepted technical-failure recovery semantics and pressure tests below. For complete discovery provenance, read v0.1.0 followed by this successor. A later explicit consolidation may compress the cumulative ledger without deleting predecessor evidence.
>
> Nothing in this file is Product Law, Architecture Law, Domain Law, Roadmap authority, a governed JIT Domain Dossier, a Final Feature Pack Contract, proof classification, Tracer Bullet, Vertical Slice, Horizontal Hardening or release evidence.

- **Document version:** `v0.2.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.1.0.md`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-006 — Genuine technical-failure recovery preserves history

**Accepted:** `2026-10-08`

Technical recovery must not be implemented by pretending the original attempt or entitlement history never happened.

### AT-WD-006A — Failure before first-answer commitment

If the participant's first-answer operation never becomes authoritative:

- no Assessment Attempt has begun;
- no assessment right has been consumed;
- ordinary retry is sufficient;
- no recovery/replacement entitlement is required.

This is a direct consequence of `AT-WD-001...003`.

### AT-WD-006B — Temporary failure during a still-valid recoverable attempt

Where the authoritative attempt and accepted progress remain intact and the fixed deadline has not passed:

- resume the same attempt;
- retain the same pinned governed assessment context;
- retain all durably accepted answers;
- do not consume another assessment right;
- do not silently move the fixed expiry deadline merely because a temporary technical fault occurred.

A transient technical problem does not itself manufacture a replacement assessment.

### AT-WD-006C — Material genuine technical failure requiring replacement

If a genuine platform/system failure makes normal completion materially impossible or destroys the platform's ability to honour the already-started assessment contract, recovery must preserve the original historical attempt and consumption truth.

The default working recovery model is:

1. retain the original attempt and its accepted progress/version/consumption provenance as historical truth;
2. apply an explicit governed technical-recovery disposition rather than silently editing history;
3. authorise a distinct successor attempt without new customer payment;
4. do not resurrect an expired original attempt or silently extend its fixed 30-day lifetime.

The successor attempt:

- has a distinct attempt identity;
- begins only at its own first durably accepted scored answer;
- receives its own fixed 30-day lifetime;
- must start against a then-currently startable governed assessment context;
- is traceable to the technical-recovery disposition of the original attempt;
- must not silently import prior-version answers unless later methodology/version-compatibility authority explicitly permits that migration.

If the original assessment version has retired, the technical-recovery successor does **not** gain permission to start that retired version merely because the failed predecessor used it.

### AT-WD-006D — Unknown final-submit outcome must reconcile before replacement

A browser timeout, crash or other unknown outcome around final submission must not immediately produce a replacement attempt.

Before recovery replacement is authorised, the platform must determine whether an authoritative accepted submission and/or canonical result already exists.

Replacement is prohibited while a canonical completed result may already exist for the original attempt.

### AT-WD-006E — Failure after canonical result creation is not an assessment-attempt failure

Once the canonical immutable result exists:

- later report rendering, publication, download, notification or external-delivery failure does not invalidate the assessment result;
- recovery operates on the report/render/delivery path;
- the platform must not rescore merely because delivery failed;
- the platform must not grant a new assessment attempt merely because the report was not successfully delivered.

### AT-WD-006F — Technical recovery can survive later subscription termination

If the participant validly started an assessment while eligible and a genuine platform technical failure created a recovery obligation during that eligible attempt, later subscription termination does not automatically erase that already-arisen recovery obligation.

This is distinct from ordinary subscription replacement eligibility:

- ordinary incomplete expiry + subscription ended → no new subscription-funded replacement under `AT-WD-005C`;
- adjudicated genuine technical failure arising from an eligible started attempt → technical-recovery remedy may survive later subscription termination.

The exact start-by lifetime of such a recovery remedy remains open.

### AT-WD-006G — Technical-failure refund and technical recovery are separate remedies

Current Product Law permits a technical-failure exception to the ordinary assessment-refund cutover.

Working interpretation:

- for a standalone purchase, the default technical remedy should be recovery/replacement where the purchased service can still reasonably be fulfilled;
- where fulfilment cannot reasonably be provided, an authorised technical-failure refund may be available under the owning commercial/refund law;
- replacement and refund are not automatically cumulative remedies;
- a subscription-included assessment ordinarily uses recovery rather than inventing a standalone assessment refund, while subscription-level refund rights remain separately governed.

### AT-WD-006H — Narrow definition of genuine technical failure

For this Pre-JIT stream, a genuine technical failure means a platform/system failure, corrupted or unrecoverable authoritative state, or material service unavailability that demonstrably prevented normal completion or made the platform unable to honour the assessment contract.

It does not automatically include:

- participant inactivity;
- forgetting to continue;
- change of mind;
- intentional abandonment;
- ordinary personal scheduling constraints;
- repeatedly closing the browser;
- loss of the participant's personal device;
- an operation that was never accepted by the platform while the service otherwise remained functional.

Exceptional support judgement may later exist, but it must not become an unaudited bypass that silently issues duplicate assessment rights or results.

---

# 2. Pressure-test additions — v0.2.0

## AT-PT-018 — First-answer request fails before commitment

**Scenario:** participant attempts the first answer; the request fails before any authoritative first-answer commitment exists.

**Expected:** no attempt, no consumption, no recovery grant; participant retries normally.

**Result:** `PASS` under AT-WD-006A.

## AT-PT-019 — Two-hour outage on Day 12

**Scenario:** active attempt is intact; platform is unavailable for two hours; service returns well before expiry.

**Expected:** same attempt resumes with same answers/context/deadline. No new assessment right and no automatic deadline extension.

**Result:** `PASS` under AT-WD-006B.

## AT-PT-020 — Platform defect makes active attempt unrecoverable

**Scenario:** authoritative progress cannot be safely restored because of a platform defect and normal completion is materially impossible.

**Expected:** preserve predecessor attempt/consumption history; explicitly adjudicate technical recovery; authorise a distinct successor attempt without new payment; never rewrite predecessor history.

**Result:** `PASS AS REQUIRED RECOVERY MODEL`; exact adjudication representation remains later JIT detail.

## AT-PT-021 — Failed V1 attempt requires recovery after V1 retirement

**Scenario:** technical failure invalidates practical completion of a V1 attempt; V1 retires before recovery successor starts.

**Expected:** historical failed attempt remains V1. Recovery successor must use a currently startable governed version. No implicit V1 resurrection and no silent answer migration.

**Result:** `PASS` under AT-WD-006C.

## AT-PT-022 — Final-submit browser timeout, result status unknown

**Scenario:** participant submits; browser times out; support cannot initially tell whether final submission/result creation committed.

**Expected:** reconcile authoritative attempt/result state first. Do not issue a replacement while an existing canonical result may exist.

**Result:** `PASS` under AT-WD-006D.

## AT-PT-023 — Canonical result exists but report renderer fails

**Scenario:** final submission and canonical result are authoritative; paid report rendering fails.

**Expected:** preserve result; retry/recover report pipeline; no rescore and no replacement assessment attempt.

**Result:** `PASS` under AT-WD-006E.

## AT-PT-024 — Subscription ends while technical recovery is being adjudicated

**Scenario:** participant validly started while subscription was eligible; platform fault materially prevented completion; subscription then ends before recovery disposition is completed.

**Expected:** ordinary future subscription replacement eligibility ends, but the already-arisen technical-recovery obligation is not erased solely because subscription ended.

**Result:** `PASS` under AT-WD-006F; exact recovery start-by period remains open.

## AT-PT-025 — Standalone participant asks for refund and replacement

**Scenario:** genuine technical failure occurs after first answer; participant requests both refund and another free assessment.

**Expected:** technical-failure refund and recovery are separately governed remedies, not automatically cumulative. Owning commercial policy must resolve the remedy without falsifying assessment history.

**Result:** `PASS` under AT-WD-006G.

## AT-PT-026 — Ordinary abandonment described as technical failure

**Scenario:** participant leaves the assessment untouched for 30 days and asks support to classify inactivity as a technical failure.

**Expected:** ordinary inactivity does not meet the working technical-failure definition. No support bypass may silently rewrite the expired attempt or produce a recovery entitlement merely for abandonment.

**Result:** `PASS` under AT-WD-006H.

---

# 3. Open-question queue after v0.2.0

`AT-OI-001` is resolved by `AT-WD-006` and `AT-PT-018...026`, subject to later upstream/JIT formalisation.

The next unresolved items remain:

- **AT-OI-002 — Attempt submission commitment boundary:** editable progress → final-submit intent → accepted complete submission → deterministic scoring → canonical result issuance; crash/retry/concurrency between each boundary.
- **AT-OI-003 — Active-attempt answer concurrency:** multi-tab/device stale writes and answer-conflict semantics.
- **AT-OI-004 — Notification policy detail:** exact warning cadence/channel hierarchy and evidence expectations.
- **AT-OI-005 — Subscription replacement abuse/fair-use boundary:** bounded controls without redefining the promised one included completed assessment.

Additional later queues remain necessary for result correction/supersession, reassessment/current-profile semantics, report lifecycle, language/version provenance, identity merge, retention/deletion, Research/Interactive isolation and the Methodology Authority Input Contract.
