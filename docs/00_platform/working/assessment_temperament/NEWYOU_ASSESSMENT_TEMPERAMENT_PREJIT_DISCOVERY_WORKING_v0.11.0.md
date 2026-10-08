# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.11.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.10.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification, replacement/retake, execution-provenance, result-correction, profile-source and reassessment semantics. This file appends the accepted assessment-report lifecycle contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.11.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.10.0.md`
- **Predecessor blob SHA:** `9334323ca516c03a707539778543c36959e8f225`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-015 — Assessment report lifecycle, delivery and permanent access

**Accepted:** `2026-10-08`

A paid digital assessment report is a governed immutable delivery snapshot derived from exactly one canonical digital result and bound to the exact approved participant-facing report interpretation/content version and locale that produced it. Report production, delivery and access remain downstream of immutable assessment-result truth and may not silently recreate, mutate or rescore that truth.

### AT-WD-015A — Report snapshot binds exact producing provenance

Every durable assessment report snapshot must remain traceable to:

1. exactly one canonical digital result;
2. that result's immutable assessment/methodology provenance;
3. the exact governed report interpretation/content version used;
4. the exact approved participant-facing locale/language variant used; and
5. sufficient rendering/template provenance where materially necessary to explain or reproduce the delivered artifact without falsely presenting a later rendering as the original.

A historical report must never resolve its content by dereferencing "whatever the current score/report copy/template is now" and then claim that rendering was the originally delivered report.

Exact Resource/schema/storage representation is deferred to JIT work.

### AT-WD-015B — Canonical result precedes report success

A valid canonical digital result remains authoritative even if downstream report generation, storage, rendering, notification or participant retrieval fails.

Where report production fails after result creation:

- do not rescore;
- do not reopen submitted answers;
- do not create another assessment attempt;
- do not consume another assessment entitlement;
- retry/recover report production from the same canonical result and governed report inputs.

Report failure is a downstream delivery/recovery concern, not an assessment-computation failure.

### AT-WD-015C — Report generation/delivery retries converge idempotently

For a given canonical result + governed report interpretation/content version + locale obligation, retries must converge on one canonical report-snapshot/version relationship rather than creating uncontrolled competing "original" reports.

A timeout or ambiguous acknowledgement after snapshot production must reconcile existing report state before creating another snapshot.

This does not prohibit later explicit interpretation/content successors or corrected-result reports; it prohibits accidental semantic duplication caused by retries.

### AT-WD-015D — Successful paid report delivery means durable authorised availability

For the assessment product obligation, successful report delivery means a valid governed immutable report snapshot has been durably produced and made available through the participant's authorised permanent-access surface.

Successful delivery does **not** require proof that:

- an email was successfully delivered;
- an email was opened;
- the participant clicked a notification;
- the participant viewed the report; or
- the participant downloaded a file.

Those are separate Communications/engagement facts.

A notification may tell the participant that the report is ready, but Communications delivery/open state does not own report existence or paid-report fulfilment truth.

### AT-WD-015E — Earned report access survives ordinary subscription termination

Once a participant has earned a paid assessment report through a qualifying completed digital assessment, ordinary later subscription termination does not revoke access to that historical report merely because recurring membership ended.

Permanent report access remains subject to governing identity, privacy, deletion, legal-hold and other explicit authority. It is not an exemption from lawful deletion.

Subscription entitlement and historical earned-report access must therefore not be silently coupled as the same access truth.

### AT-WD-015F — Bilingual reports are governed counterpart deliveries of one result

Afrikaans and English report variants are separately governed participant-facing language variants of the same underlying canonical digital result where the paid product requires bilingual report support.

Producing or accessing the counterpart locale:

- does not create a second assessment result;
- does not create another assessment completion;
- does not consume another assessment entitlement;
- must use the approved counterpart content/interpretation compatible with the underlying result/report version.

Exact materialisation may be eager or lazy at JIT implementation time; the product right and reproducibility requirement must not depend on pre-rendering both artifacts at result creation.

### AT-WD-015G — Missing required locale fails closed

If the approved governed report content for the participant's requested/required locale is unavailable, the platform must not silently substitute another locale, machine-translate, or use stale/unapproved content and then mark the requested report obligation satisfied.

The canonical result remains valid. The affected locale report may remain pending/unavailable until approved content exists or governed recovery/remediation resolves the issue.

Required bilingual publication readiness remains a separate release/governance concern from runtime lazy materialisation.

### AT-WD-015H — Original delivered report and later approved interpretation remain distinct

Where report wording/interpretation improves without changing the immutable raw result:

- preserve the original delivered report snapshot and its provenance;
- separately provide the later approved interpretation/report successor;
- never mutate the original bytes/content/provenance and pretend the participant always received the newer wording.

Participant-facing history may distinguish the original delivered report from the latest approved interpretation.

### AT-WD-015I — Purely cosmetic rendering change does not automatically create semantic report version

A genuinely non-semantic presentation-only change, such as harmless spacing, page breaks or equivalent cosmetic rendering, need not create a new methodology or business interpretation version merely because rendering changed.

However, technical presentation changes must not falsify historical delivery evidence. If reproduction/explanation of an already delivered artifact depends materially on renderer/template provenance, sufficient provenance must be retained.

Semantic meaning changes require governed content/interpretation versioning rather than being disguised as presentation changes.

### AT-WD-015J — Corrected/invalidated result history drives report succession

Where a result is computationally corrected under `AT-WD-012B`:

- the original report remains historical evidence linked to the defective predecessor;
- it must not continue masquerading as the valid current report where the predecessor is superseded for active use;
- a corrected governed report derives from the corrective result and retains its own exact report/version/locale provenance.

Where a result is invalidated, its historical report remains preserved while governing retention law permits but must not continue being presented as valid current product output.

Report succession may never silently mutate the original result/report lineage.

### AT-WD-015K — Permanent access belongs to the rightful participant/result owner, not a transient login identifier

Permanent report access attaches to the participant/rightful result ownership established by governing Identity & Access / entitlement truth, not to a particular browser session or an email-address string in isolation.

Account recovery, identifier change or later identity consolidation must not casually duplicate, transfer, orphan or destroy report ownership. Exact merge/recovery semantics remain the next Pre-JIT pass.

---

# 2. Pressure-test additions — v0.11.0

## AT-PT-102 — Result commits and renderer crashes

**Scenario:** canonical digital result exists; report renderer crashes before producing the report.

**Expected:** canonical result remains valid. Retry report generation from the same result/content/locale inputs; no rescore, answer reopening, new attempt or second entitlement consumption.

**Result:** `PASS` under AT-WD-015B.

## AT-PT-103 — Renderer succeeds but acknowledgement times out

**Scenario:** report snapshot was durably produced, but the worker/client times out before learning success.

**Expected:** retry reconciles the existing canonical report snapshot/version relationship before creating anything else. No competing "original" report is manufactured by retry.

**Result:** `PASS` under AT-WD-015C.

## AT-PT-104 — Email report-ready notification bounces

**Scenario:** governed report snapshot is durably available in the participant's authorised access surface, but the readiness email bounces.

**Expected:** report-delivery/fulfilment truth remains satisfied; Communications records/recovers its own failure. Email bounce does not recreate or invalidate the report.

**Result:** `PASS` under AT-WD-015D.

## AT-PT-105 — Participant never opens or downloads report

**Scenario:** report is permanently and authoritatively available but participant never views/downloads it.

**Expected:** paid report delivery may still be fulfilled. View/download is engagement evidence, not report-existence truth.

**Result:** `PASS` under AT-WD-015D.

## AT-PT-106 — Subscription terminates after earned report

**Scenario:** participant completes a qualifying paid assessment, report is available, then ordinary subscription terminates.

**Expected:** earned historical report access remains; subscription termination does not silently revoke the report. Governing deletion/privacy authority remains applicable.

**Result:** `PASS` under AT-WD-015E.

## AT-PT-107 — English report exists but approved Afrikaans counterpart is missing

**Scenario:** canonical result exists and English report content is approved, but the required compatible Afrikaans report content is unavailable when participant requests Afrikaans.

**Expected:** do not silently substitute English or machine translation as the Afrikaans report. Preserve result; fail/pending closed on the requested locale until governed content/recovery resolves it.

**Result:** `PASS` under AT-WD-015F/G.

## AT-PT-108 — Participant changes application language after result

**Scenario:** participant originally accessed English report and later switches application language to Afrikaans; approved counterpart exists.

**Expected:** platform may expose/materialise the approved Afrikaans counterpart linked to the same result. No new assessment/result/entitlement consumption occurs.

**Result:** `PASS` under AT-WD-015F.

## AT-PT-109 — Report interpretation wording improves later

**Scenario:** original report E1 was delivered; later approved interpretation E2 improves wording without changing raw result.

**Expected:** preserve E1 as original delivered snapshot and expose E2 separately as latest approved interpretation/successor. Never rewrite E1 into E2.

**Result:** `PASS` under AT-WD-015H + existing DEC-066 semantics.

## AT-PT-110 — Cosmetic PDF layout changes only

**Scenario:** spacing/page-break/logo-placement changes without participant-facing semantic meaning change.

**Expected:** do not invent a new methodology/business interpretation version solely for cosmetic rendering. Historical delivered evidence must nevertheless remain truthful/reproducible enough not to present the new rendering as the old artifact.

**Result:** `PASS` under AT-WD-015I.

## AT-PT-111 — Corrective result supersedes defective result

**Scenario:** R1/report S1 existed; platform computation defect produces corrective R2.

**Expected:** preserve S1 as historical report linked to R1, mark lineage/status appropriately, generate corrected report from R2, and never rewrite S1 or R1.

**Result:** `PASS` under AT-WD-015J + AT-WD-012.

## AT-PT-112 — Repeated report-generation job execution

**Scenario:** the same logical report job runs repeatedly because of retries/restarts.

**Expected:** one canonical report-snapshot/version relationship for the same result/content/locale obligation; retries do not create duplicate semantic deliveries.

**Result:** `PASS` under AT-WD-015C.

## AT-PT-113 — Account identifier changes after report delivery

**Scenario:** participant changes login email/identifier after earning permanent report access.

**Expected:** report ownership does not move merely because an identifier string changed, nor is access lost solely because the old identifier is no longer used. Governing participant identity continuity owns the mapping.

**Result:** `PASS AS REQUIRED INVARIANT` under AT-WD-015K; exact identity recovery/consolidation semantics remain next-pass work.

---

# 3. Open-question queue after v0.11.0

The report generation/publication/access/delivery cluster is now materially constrained by `AT-WD-015` and `AT-PT-102...113`, subject to later JIT Resource/storage/rendering design, Content & Media publication authority, identity/privacy law and explicit upstream amendments already recorded where applicable.

Next unresolved cluster:

- **Identity continuity / merge / recovery:** preserve participant ownership of attempts, immutable results, current-profile selections and permanent reports across login-identifier change, verified account recovery, duplicate-account consolidation and purchaser/recipient separation without duplicate rights or silent transfer.

Later passes still include privacy/retention; Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
