# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.19.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.18.0`. Read those predecessors first for `AT-WD-001...019`, the final adversarial sweep, and accepted `AT-UPD-001` / `AT-UPD-002` correction contracts.
>
> Nothing in this file itself amends Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.19.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.18.0.md`
- **Predecessor blob SHA:** `22e3c9c395c04e1bafcde17f49c78e41a8166a73`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Live canonical `main` revalidation pin:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `UPSTREAM RECONCILIATION — AT-UPD-001/002/004 ACCEPTED; AT-UPD-005 NEXT`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `CHANGES REQUIRED UPSTREAM / NOT ELIGIBLE FOR PARK`

---

# 1. Accepted upstream correction contract

## AT-UPD-004 — Assessment result correction, invalidation and supersession

**Accepted working correction direction:** `2026-10-08`

Current Product Law already establishes immutable submitted answers/scores/version, audited Reviewed Interpretation, explicit historical-report preservation and participant-controlled current-profile selection. The missing Product meaning is how known-wrong or no-longer-valid completed results are corrected or removed from active authority without rewriting history.

The upstream Product successor must preserve the following distinctions.

### AT-UPD-004A — Interpretation-only correction remains Reviewed Interpretation

Where submitted answers, calculated scores and producing methodology remain valid and only wording/interpretation changes:

- retain the existing immutable raw result;
- append an audited Reviewed Interpretation;
- preserve the original delivered report while exposing the later approved interpretation according to existing report law;
- do not create a new assessment result;
- do not consume another entitlement;
- do not create a retake or reset the ordinary reassessment interval.

### AT-UPD-004B — Proven platform computation defect may create an immutable corrective-result successor

Where the frozen submission and pinned approved methodology are valid but the platform demonstrably computed the result incorrectly:

- never edit or erase the defective original result;
- create a separately immutable corrective-result successor derived from the same frozen submission and same valid governed methodology context;
- record an explicit predecessor/supersession relationship, defect basis, corrective computation provenance and approval/evidence sufficient for audit;
- mark the defective original superseded/ineligible for active product use while retaining it as historical evidence subject to privacy/deletion law;
- treat the corrective successor as remediation of the same assessment, not a new participant assessment;
- do not consume another assessment right, count an annual retake or reset the ordinary reassessment interval.

The one-canonical-result submission invariant remains intact: the original submission produced one original canonical result; a later corrective-result successor is an explicit correction event, not a competing second completion.

### AT-UPD-004C — Material methodology defect defaults to invalidation/remediation, not silent later-version rescoring

Where the implementation correctly applied M1 but the methodology authority later determines M1 itself materially invalid:

- preserve the M1 result historically while retained;
- permit the result to become invalid/ineligible for active product use;
- do not silently run M1 answers through M2 or another later methodology;
- permit cross-version correction only where the methodology authority explicitly establishes that the historical inputs support a valid backwards-compatible correction within the approved scope;
- otherwise provide explicitly governed remediation/replacement rather than an ordinary participant-requested retake.

A platform or methodology defect must not force the participant to wait for the ordinary annual retake interval merely to receive remediation for an invalid product output.

### AT-UPD-004D — Participant regret or changed self-understanding is not correction

A participant later wishing she had answered differently, disagreeing with the result, or changing self-understanding does not authorise mutation/recalculation of the submitted digital assessment.

The participant may create a later declared profile or complete a future entitled reassessment, but the submitted assessment and result history remain intact.

Staff disagreement likewise does not create correction authority.

### AT-UPD-004E — Eligibility and current-profile consequences

A result that is materially invalidated or superseded as known-wrong may remain historical but cannot continue as an effective eligible current-profile source.

If that source was selected current:

- the selection becomes ineffective/ineligible for current personalisation;
- no alternative profile is silently selected;
- a corrective successor or another eligible source is surfaced for participant selection/confirmation according to current-profile law.

A corrective successor is not automatically made current merely because it deterministically corrects the predecessor.

### AT-UPD-004F — Report succession follows result succession

For a computation defect:

- preserve the original report as historical evidence while retained;
- mark it explicitly superseded/ineligible for current valid use where appropriate;
- derive a corrected report from the corrective result under the governed report-content/locale rules.

For methodology invalidation:

- preserve historical report evidence while retained;
- do not continue presenting it as a valid current report;
- follow the governed remediation path.

Interpretation-only wording changes continue to use existing Reviewed Interpretation / historical-report law rather than manufacturing a corrective result.

### AT-UPD-004G — Participant notification and downstream impact identification

Material result correction or invalidation creates a participant-facing service obligation sufficient to explain:

- which assessment/result is affected;
- whether it was corrected or invalidated;
- report consequences;
- current-profile consequences;
- required participant action, if any;
- available remediation/replacement.

Temperament owns the correction/invalidation truth. Communications owns delivery evidence. Notification failure cannot make a defective result valid again.

Where durable downstream products were produced from the affected result, Temperament must expose an owner-mediated, duplicate/retry-safe impact consequence identifying the affected provenance. It must not directly rewrite Plans, Programmes, Content or other Domain-owned business truth. Each owning Domain applies its own governed correction behaviour.

### AT-UPD-004H — Authority to establish the defect remains scoped

A computation defect requires verified technical/audit evidence that the platform failed to apply the approved pinned methodology correctly.

A methodology defect or backwards-compatible methodology correction requires the methodology authority established by DEC-309 / the governing IP agreement.

Health/Clinical authority may govern health/safety-sensitive wording or downstream safety consequences without silently becoming scoring-methodology authority.

A generic admin/staff action is not sufficient to invalidate or correct a result.

---

# 2. Product-authority delta required

The eventual authoritative Product/Decision successor should extend, not replace, existing DEC-061/062/063/066 semantics:

- DEC-061 remains the immutability rule for submitted answers, original calculated score/result and version evidence;
- DEC-062 remains the interpretation-only reviewed-interpretation path;
- DEC-063 remains participant-controlled selection among eligible current-profile sources;
- DEC-066 remains original-report preservation plus later approved interpretation;
- new Product wording must add explicit computational-correction, methodology-invalidation, active-use supersession, remediation and downstream-impact semantics without weakening those existing rules.

Architecture FLOW-03's existing correction/recalculation supersession invariant supports implementation of this Product meaning but does not itself create it.

---

# 3. Pressure tests added for the accepted correction

## AT-PT-198 — Correct arithmetic defect under same pinned methodology

**Scenario:** frozen answers under M1 should deterministically produce R2, but deployed code produced defective R1.

**Expected:** preserve R1; create immutable corrective successor R2 under M1; R1 becomes superseded for active use; no new assessment/credit/retake/interval reset.

**Result:** `PASS` under AT-UPD-004B.

## AT-PT-199 — Wrong deployed lookup table while approved M1 inputs are known

**Scenario:** production code accidentally used a lookup table inconsistent with the approved pinned M1 package.

**Expected:** verified computation defect may use same-context deterministic correction; do not opportunistically use current M2.

**Result:** `PASS` under AT-UPD-004B/H.

## AT-PT-200 — Methodology M1 itself is rejected later

**Scenario:** software applied M1 perfectly, but methodology authority later determines M1 materially invalid.

**Expected:** no silent M2 rescoring; preserve historical R1, mark ineligible/invalid for active use, and route explicit remediation unless methodology authority explicitly approves backwards-compatible correction.

**Result:** `PASS` under AT-UPD-004C.

## AT-PT-201 — Participant says submitted answer was a mistake

**Scenario:** participant later says she meant to select another option.

**Expected:** no correction of frozen submission/result. Future declared-profile change or entitled reassessment only.

**Result:** `PASS` under AT-UPD-004D.

## AT-PT-202 — Staff disagrees with participant result

**Scenario:** support/admin believes another colour would be more appropriate.

**Expected:** no staff result edit or manufactured correction. Staff may explain or route legitimate review/remediation authority only.

**Result:** `PASS` under AT-UPD-004D/H.

## AT-PT-203 — Current R1 is invalidated

**Scenario:** R1 is the participant-selected current source when material invalidation occurs.

**Expected:** R1 remains historical but ceases effective current eligibility; no automatic alternative selection.

**Result:** `PASS` under AT-UPD-004E.

## AT-PT-204 — Corrective R2 exists for current R1

**Scenario:** R1 was current and deterministic corrective R2 is created.

**Expected:** R1 ceases eligible active use; R2 is eligible where otherwise valid but is not silently auto-selected. Participant confirmation/selection remains required.

**Result:** `PASS` under AT-UPD-004E and DEC-063 direction.

## AT-PT-205 — Original paid report already delivered before correction

**Scenario:** participant received report for R1 before R2 correction exists.

**Expected:** preserve original report as historical/superseded evidence; provide corrected report from R2 under governed report rules; never rewrite original bytes/content into R2.

**Result:** `PASS` under AT-UPD-004F.

## AT-PT-206 — Corrected result materially affects an existing personalised plan

**Scenario:** Plans produced durable Plan P1 from R1, then R1 is materially corrected/invalidated.

**Expected:** Temperament emits/records owner-mediated affected-provenance consequence; Plans decides governed correction/replacement. Temperament never rewrites P1 directly.

**Result:** `PASS` under AT-UPD-004G.

## AT-PT-207 — Correction discovered after membership ends

**Scenario:** participant's subscription ended after a paid historical assessment/report, then a material platform result defect is discovered.

**Expected:** correction/remediation obligation is not automatically extinguished by ordinary subscription end; historical purchased-result correction follows the governing Product/Privacy/identity contract.

**Result:** `PASS` under AT-UPD-004B/G plus permanent-report semantics.

## AT-PT-208 — Full deletion completed before defect discovered

**Scenario:** participant completed irreversible full deletion before a defect affecting former assessment data is later discovered.

**Expected:** do not reconstruct deleted personal assessment data to run correction; any remaining non-personal operational/legal consequence follows Privacy authority.

**Result:** `PASS` under AT-UPD-004 + AT-WD-017.

---

# 4. Disposition after acceptance

`AT-UPD-004` is accepted as a required Product-law correction direction. It remains non-authoritative until the proper Product/Decision successor is governed and merged.

The working stream remains:

**CHANGES REQUIRED UPSTREAM / NOT ELIGIBLE FOR PARK.**

Next upstream reconciliation target:

**AT-UPD-005 — Route OQ-017 to FP-003 for the mandatory assessment-expiry-warning path without pulling unrelated later reminder capability into FP-003.**
