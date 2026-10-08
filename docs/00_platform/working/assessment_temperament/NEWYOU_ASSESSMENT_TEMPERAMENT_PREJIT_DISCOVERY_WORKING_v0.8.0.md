# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.8.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.7.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification, replacement/retake and execution-provenance semantics. This file appends the accepted immutable result correction / invalidation / supersession contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.8.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.7.0.md`
- **Predecessor blob SHA:** `379b3a7ec526eadaa4bf82fb1602064486ee0ee4`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-012 — Immutable result correction, invalidation and supersession

**Accepted:** `2026-10-08`

Submitted answers and every produced result remain immutable historical evidence while retained. Correction, invalidation, recalculation or later interpretation must append explicit relationship/evidence and may never silently rewrite the producing answers, original scores or producing assessment context.

### AT-WD-012A — Interpretation/wording correction does not change raw result

Where submitted answers and calculated scores remain valid and only participant-facing wording or interpretation changes:

- the raw result remains unchanged;
- a separate governed reviewed interpretation/report interpretation may be added;
- original delivered report provenance remains preserved;
- no new attempt, entitlement consumption or annual retake occurs.

### AT-WD-012B — Proven platform computation defect may create a corrective result

Where a platform implementation defect caused the system to calculate a result incorrectly despite valid frozen answers and a valid pinned governed assessment context, the original result is not edited.

A separately immutable corrective/recalculated result may be produced from:

- the same frozen submitted answers;
- the same valid pinned governed assessment execution context;
- the corrected faithful implementation of that same governed methodology/version.

The corrective result must explicitly reference the defective predecessor and carry sufficient reason, provenance, authority and audit evidence to explain why it supersedes the predecessor for active product use.

This corrective result is not a new participant assessment, does not consume another assessment right and does not count as an annual retake.

### AT-WD-012C — Material methodology defect does not authorise silent cross-version recalculation

If the producing methodology/instrument itself is later found materially defective, engineering may not automatically apply a later methodology/version to the old submitted answers.

Default rule:

- preserve the original answers, producing governed context and original result;
- mark/apply explicit invalidation or ineligibility-for-use semantics where governing authority determines the result can no longer safely/faithfully be used;
- require explicit methodology authority before any backwards-compatible correction/recalculation of historical answers is permitted;
- otherwise use explicitly governed participant remediation/replacement rather than pretending the participant answered the later instrument.

### AT-WD-012D — Participant regret or changed answer is not correction

After authoritative final submission, participant regret, changed self-perception or a claim that an answer should have been different does not permit answer/result mutation or staff rescore.

A genuinely new assessment outcome requires a later valid assessment entitlement under ordinary reassessment/retake rules.

### AT-WD-012E — Invalidated/superseded results remain historical but lose active-product eligibility

Preservation of historical evidence does not imply continued eligibility for personalisation/current-profile use.

Where a result is explicitly invalidated or superseded for active use:

- it remains part of historical result provenance while retained;
- it may not continue acting as eligible authoritative input to current product personalisation merely because it once was valid;
- if it was the selected current profile source, that selection can no longer remain effective once the source becomes ineligible.

The platform must not silently choose a replacement current profile for the participant.

### AT-WD-012F — Corrective result does not automatically become the participant-selected current profile

A corrective result may become eligible while its defective predecessor becomes ineligible, but participant current-profile selection remains explicit under Product Law.

The platform may require reselection/confirmation and may explain the correction, but must not silently substitute the corrected result as current solely because it supersedes the defective calculation.

### AT-WD-012G — Report history follows result history

Where only interpretation wording improves, preserve the original delivered report and expose the later approved interpretation according to governing report law.

Where a result is computationally corrected:

- the original report remains historical evidence;
- it must not continue masquerading as the current valid report where its underlying result was superseded;
- a corrected governed report may be generated from the corrective result with its own exact content/language provenance.

Where the underlying methodology/result is invalidated, affected reports remain historical but must not continue acting as valid current product output.

### AT-WD-012H — Material correction/invalidation creates a participant-notification obligation

A material result correction or invalidation must not be silently repaired only in backend state.

The participant-facing outcome must be able to communicate, as applicable:

- which assessment/result is affected;
- whether it was corrected or invalidated;
- whether a previously delivered report is affected;
- whether participant action is required;
- whether remediation/replacement is available.

Exact Communications mechanics remain later governed/JIT work.

---

# 2. Upstream amendment addition

## AT-UPD-004 — Product Law must govern computational correction / invalidation / supersession-for-use

**Status:** `REQUIRED BEFORE GOVERNED FP-003 CONTRACT COMPLETION`

Current Product Law clearly requires immutable submitted answers/raw result and separately audited reviewed interpretation. Current Architecture also requires explicit correction/recalculation/supersession evidence rather than historical falsification.

However, current Product Law does not yet sufficiently define the product semantics for:

1. proven platform computation defects;
2. separately immutable corrective results;
3. result invalidation/ineligibility for active use;
4. methodology-defect consequences and backwards-compatible correction authority;
5. current-profile consequences when a selected source becomes invalid/superseded;
6. participant remediation and notification obligations.

An explicit Product Law amendment is therefore required. This working decision must not be treated as silently creating authoritative Product Law from Architecture.

---

# 3. Pressure-test additions — v0.8.0

## AT-PT-071 — Report interpretation wording improves

**Scenario:** raw answers/scores remain valid; approved report wording improves.

**Expected:** original result remains unchanged; append/use a governed reviewed interpretation/report successor while preserving original delivered provenance. No new assessment or retake.

**Result:** `PASS` under AT-WD-012A/G.

## AT-PT-072 — Software arithmetic bug produced wrong score

**Scenario:** frozen answers plus valid pinned V1 rules should yield score 21, but implementation bug persisted score 17.

**Expected:** do not edit the 17-result. Produce separately immutable corrected result from the same answers and same V1 context, explicitly linked as corrective/superseding-for-use. No new attempt/entitlement/retake.

**Result:** `PASS` under AT-WD-012B.

## AT-PT-073 — Wrong scoring lookup deployed

**Scenario:** code used an incorrect lookup table while the approved governed methodology itself was correct.

**Expected:** preserve every defective historical result; identify affected results; append deterministic corrective results under the same governed context with explicit defect provenance rather than batch-overwriting rows.

**Result:** `PASS` under AT-WD-012B.

## AT-PT-074 — Methodology V1 itself later declared materially defective

**Scenario:** implementation faithfully produced V1 results, but methodology authority later determines V1 rules were materially invalid.

**Expected:** preserve V1 answers/context/results; do not silently run answers through V2. Apply explicit invalidation/ineligibility/remediation according to governing authority unless methodology authority explicitly approves a backwards-compatible historical correction.

**Result:** `PASS` under AT-WD-012C; exact Product Law remediation remains AT-UPD-004.

## AT-PT-075 — Material mistranslation changes question meaning

**Scenario:** a governed Afrikaans question variant is later found to have materially changed the meaning participants answered.

**Expected:** do not treat this as a mere report-copy correction. Affected answer/result validity must be handled as instrument/methodology/content validity with explicit authority; no assumption that another locale/version can simply replace the historical meaning.

**Result:** `PASS` under AT-WD-011 + AT-WD-012C.

## AT-PT-076 — Participant says submitted answer was a mistake

**Scenario:** participant asks support to change Q14 after canonical result creation.

**Expected:** no answer mutation or rescore. Historical result remains; future new outcome requires legitimate reassessment/retake entitlement.

**Result:** `PASS` under AT-WD-012D.

## AT-PT-077 — Staff disagrees with participant result

**Scenario:** staff believes the result "looks wrong" but no proven platform/methodology defect exists.

**Expected:** staff disagreement alone confers no authority to mutate/recalculate/invalidate raw result. Any exceptional reviewed interpretation remains separately audited and governed.

**Result:** `PASS` under AT-WD-012A/D.

## AT-PT-078 — Defective result was selected current

**Scenario:** participant previously selected R1 as current; R1 is later proven defective and superseded/ineligible.

**Expected:** R1 remains historical but cannot continue as eligible active personalisation authority. Platform does not silently select another profile; participant must reselect/confirm an eligible source according to Product Law.

**Result:** `PASS` under AT-WD-012E/F.

## AT-PT-079 — Original report already downloaded before correction

**Scenario:** participant downloaded a report based on R1 before a scoring defect is discovered and corrected to R2.

**Expected:** platform cannot falsify/retract historical delivery; preserve original report provenance, clearly mark supersession in current product surfaces, and provide corrected governed report from R2.

**Result:** `PASS` under AT-WD-012G.

## AT-PT-080 — Material correction performed silently

**Scenario:** backend corrects an affected result but participant receives no indication and continues using an old report/profile.

**Expected:** unacceptable. Material correction/invalidation establishes a participant-facing notification/remediation obligation; exact delivery mechanics are later Communications work.

**Result:** `PASS` under AT-WD-012H.

---

# 4. Open-question queue after v0.8.0

The result correction / invalidation / supersession cluster is now materially constrained by `AT-WD-012`, `AT-UPD-004` and `AT-PT-071...080`, subject to explicit upstream Product Law amendment and later JIT representation/proof.

Next unresolved cluster:

- **Declared vs digitally assessed vs historical/current-profile semantics:** precisely distinguish declaration provenance, digital result history, eligibility, current-profile selection, later digital completion, invalidated sources and downstream personalisation authority.

Later passes still include reassessment interactions; report generation/publication/access/delivery; identity merge; privacy/retention; Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
