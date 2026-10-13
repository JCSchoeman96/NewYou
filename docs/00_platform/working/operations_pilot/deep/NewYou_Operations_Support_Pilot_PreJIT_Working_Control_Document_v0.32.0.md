# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.11.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.10.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch entering pass:** `b22edeb06ce409acbdf518e6686a772b8a058bf1`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_CONTROL_REGISTER_WORKING_v0.9.0.md`
- **Discovery source through:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.14.0.md`
- **Corrected OPS-UPD-004 candidate:** `NEWYOU_OPS_UPD_004_AUTHORITY_PROMOTION_CANDIDATE_WORKING_v0.2.0.md`
- **Formal build contract:** `NEWYOU_OPS_UPD_004_AUTHORITY_SUCCESSOR_BUILD_WORKING_v0.1.0.md`
- **Independent review:** `NEWYOU_OPS_UPD_004_AUTHORITY_SUCCESSOR_INDEPENDENT_REVIEW_WORKING_v0.1.0.md`
- **v0.10.0 bounded change:** formal `OPS-UPD-004` Product/Decision successor build contract + independent review only. No new pressure tests, no new UPD/GAP, no implementation, no current-authority routing change.
- **Compression rule:** all unchanged v0.9.0/v0.8.0 convergence state remains inherited. This successor records only the material authority-build/review delta.

---

# 1. Current identifier and authority state

```text
latest semantic discovery = v0.14.0
contiguous PT coverage = OPS-PT-001...210
new PTs in this pass = 0
current upstream deltas = OPS-UPD-001...007
current normalized gaps = OPS-GAP-001...025
new OPS-UPD = 0
new OPS-GAP = 0
current Product Law = 00_PLATFORM_v1.6.0.md
current Decision Register = 01_DECISIONS_v1.6.0.md
live OPS-UPD-004 = CONFLICT_STOP
live OPS-GAP-010 = OPEN / CONFLICT_STOP
```

Nothing in this working register overrides current authority.

---

# 2. Independent-review corrections to the v0.1.0 promotion candidate

The prior `NEWYOU_OPS_UPD_004_AUTHORITY_PROMOTION_CANDIDATE_WORKING_v0.1.0.md` is historical evidence but is **not suitable for direct promotion unchanged**.

The independent review found four corrections now locked in v0.2.0:

1. `DEC-034`, not `DEC-057`, is the annual retake rule; `DEC-057` is launch scoring.
2. Ownership must remain explicit: Temperament owns attempt/result/report truth; Entitlements owns current credit/right truth; Identity & Access governs access assurance.
3. Product §21B.3 must be corrected as well as adding §21R.6; otherwise Product v1.7.0 would retain an internal contradiction.
4. No Roadmap semantic successor is justified because current FP-003 already says the credit remains unused until successful digital assessment delivery. A later Roadmap routing/reference PATCH may be needed after Product/Decision promotion.

No new semantic class emerged, so no new PT/UPD/GAP is justified.

---

# 3. Corrected OPS-UPD-004 candidate semantics

Candidate lifecycle:

| Situation | Candidate consequence |
|---|---|
| valid ordinary paid credit; no first answer | `available_unused` |
| first answer saved; active/recoverable attempt | `held_unconsumed` |
| immutable result exists but paid report not durably participant-available | `held_unconsumed` |
| immutable result + paid report durably available to authorised participant | `consume_exactly_once` |
| attempt expires before first answer | `release_to_available_unused` |
| post-first-answer nontechnical expiry without live recovery | `close_unconsumed` |
| genuine technical failure | preserve same paid obligation / recover existing lineage where present |
| valid technical-failure refund | close affected right; not delivery/consumption |

Additional locks:

- notification/provider success/failure is not assessment-credit consumption authority;
- participant open/read/view telemetry is not consumption authority;
- assessment-completion metrics are not Entitlements authority;
- refundability remains governed separately by `DEC-045`;
- `DEC-034` retake interval remains separate and is not redefined by this repair;
- duplicate/retried submission, recovery, delivery or consumption converges on one logical credit/result/report lineage.

The material Product choice remains:

```text
post-first-answer nontechnical expiry
→ close_unconsumed
```

This establishes no legal sufficiency and must remain explicit in the formal authority review/promotion trail.

---

# 4. Formal deterministic successor build

The formal build contract pins exact live source blobs:

```text
00_PLATFORM_v1.6.0.md
blob = bb98081841b432a5a3d5e961929acf494ac9c8ba

01_DECISIONS_v1.6.0.md
blob = 85402cb169e095771f03482981d0691e08efb021
```

Target semantic successors:

```text
00_PLATFORM_v1.7.0.md
01_DECISIONS_v1.7.0.md
```

Both are MINOR successors because the repair adds/changes Product semantics.

## Product transformation only

- version/header/amendment-scope metadata;
- replace the two conflicting §21B.3 first-answer consumption bullets;
- add §21R.6 assessment-credit claim/delivery/closure/consumption rule;
- update §24 internal current-version sentence;
- no other Product semantic change.

## Decision transformation only

- version/header/amendment-scope metadata;
- preserve historical DEC-055 wording but mark `SUPERSEDED BY DEC-313`;
- append `DEC-313`;
- no other DEC/OQ semantic change.

## Explicit non-changes

- no North Star semantic successor;
- no Roadmap semantic successor;
- no Architecture amendment;
- no Domain Map amendment;
- no provider/channel choice;
- no operator permission rule;
- no implementation representation.

---

# 5. Independent review outcome

The corrected candidate and deterministic build contract were reviewed independently against `OPS-PT-163...174` and adjacent authority.

| Review area | Outcome |
|---|---|
| Product authority level | PASS |
| DEC-055 explicit supersession | PASS |
| Product §21B.3 internal conflict removal | PASS |
| §21R.6 lifecycle | PASS |
| Domain ownership | PASS |
| DEC-045 refund separation | PASS |
| DEC-054/056 recovery/expiry composition | PASS |
| DEC-061/066/067 immutable result/report lineage | PASS |
| DEC-303 purchase-cap composition | PASS |
| DEC-034 non-expansion | PASS WITH BOUNDED NON-EXPANSION |
| North Star metric vs commercial consumption | PASS WITH EXPLICIT SEPARATION |
| OPS-PT-163...174 | PASS, 12/12 |
| Roadmap semantic change | NOT JUSTIFIED |
| Architecture/Domain change | NOT JUSTIFIED |

The review certifies the **deterministic build contract**, not cumulative v1.7.0 bytes and not current authority.

---

# 6. Materialisation hard gate

Before `OPS-UPD-004` can close, a separate exact materialisation/promotion pass must:

1. generate cumulative `00_PLATFORM_v1.7.0.md` from the pinned Product blob;
2. generate cumulative `01_DECISIONS_v1.7.0.md` from the pinned Decisions blob;
3. prove the exact diffs match the build contract and nothing else;
4. archive predecessor authority byte-identically;
5. update/add Foundation Integrity assertions for DEC-055 supersession, DEC-313, §21B.3 and §21R.6;
6. prove a negative check prevents first-answer consumption from remaining current authority;
7. run exact-head CI;
8. independently review the materialised head;
9. only then update README/manifest/current routing and any required routing-only downstream PATCH successors;
10. reverify resulting-main after any eventual merge before claiming current-status closure.

Until that pass completes:

```text
OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
implementation = NOT AUTHORISED to choose a rule
```

---

# 7. Other upstream deltas remain unchanged

No other upstream delta is reopened or promoted in this pass:

- `OPS-UPD-001` pilot admission/cap — unchanged / open;
- `OPS-UPD-002` duplicate collection/make-whole — unchanged / open;
- `OPS-UPD-003` consequential command authority — unchanged / principally operations-policy;
- `OPS-UPD-005` pre-first-fulfilment Plan change — unchanged / open;
- `OPS-UPD-006` export + Full Deletion — unchanged / open, legal/privacy validation still required;
- `OPS-UPD-007` General Wellness clock start — unchanged / open.

Do not begin `OPS-UPD-001` until `OPS-UPD-004` materialisation/promotion has completed or the user explicitly changes the serial order.

---

# 8. v0.10.0 disposition

```text
SEMANTIC PRESSURE TESTS ADDED: NONE
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
DISCOVERY SUCCESSOR: NONE (v0.14.0 REMAINS LATEST)
OPS-UPD-004 V0.1.0 CANDIDATE: SUPERSEDED FOR PROMOTION PURPOSES
OPS-UPD-004 V0.2.0 CORRECTED CANDIDATE: PASS
FORMAL AUTHORITY-SUCCESSOR BUILD CONTRACT: PASS
INDEPENDENT REVIEW: PASS
12/12 OPS-PT-163...174: PASS UNDER CORRECTED CANDIDATE
TARGET PRODUCT SUCCESSOR: v1.7.0
TARGET DECISION SUCCESSOR: v1.7.0 / DEC-313
ROADMAP SEMANTIC SUCCESSOR: NOT JUSTIFIED
ARCHITECTURE AMENDMENT: NOT JUSTIFIED
DOMAIN MAP AMENDMENT: NOT JUSTIFIED
CURRENT AUTHORITY MODIFICATION: NONE
LIVE OPS-UPD-004 CONFLICT_STOP: REMAINS
MATERIALISED CUMULATIVE v1.7.0 BYTES: REQUIRED NEXT
IMPLEMENTATION: NOT AUTHORISED
PR: NONE
AUTHORITY BUILD/REVIEW PASS: PASS / CONVERGED
BROAD PRE-JIT FREEZE: NOT READY
NEXT PASS: OPS-UPD-004 EXACT CUMULATIVE v1.7.0 MATERIALISATION + DIFF/INTEGRITY REVIEW ONLY
```


---

# 9. v0.11.0 — Exact v1.7 materialisation and integrity-review gate

> **WORKING / NON-AUTHORITATIVE**  
> **AUTHORITY CANDIDATE MATERIALISED — CURRENT ROUTING UNCHANGED**  
> **EXACT-HEAD FOUNDATION INTEGRITY CI NOT YET RUN — STOP BEFORE PROMOTION**

## 9.1 Clean authority branch

The authority-materialisation work is isolated from the long-lived Pre-JIT discovery branch.

```text
branch = authority/ops-upd-004-assessment-credit-v1.7.0
base/main = 086ade7b28c000de1c387acb9760e5eb08bb0413
candidate head = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
ahead = 1 commit
behind = 0
```

The candidate commit adds exactly three paths:

1. `docs/00_platform/working/operations_pilot/authority_candidates/00_PLATFORM_v1.7.0.md`;
2. `docs/00_platform/working/operations_pilot/authority_candidates/01_DECISIONS_v1.7.0.md`;
3. `tests/test_ops_upd_004_authority_materialization.py`.

No README, authority manifest, current Product/Decision path, Roadmap, Architecture or Domain file is changed in this candidate.

## 9.2 Materialised candidate review

Independent document review confirms the materialised candidates implement the corrected v0.2.0 contract at the required surfaces:

- Product §21B.3 changes first-answer handling from consumption to claim/hold;
- Product §21R.6 defines `available_unused`, `held_unconsumed`, successful-delivery consumption, terminal `close_unconsumed`, and technical-recovery/refund composition;
- Product ownership remains Temperament = attempt/result/report truth, Entitlements = credit/right truth, Identity & Access = access assurance;
- Product §24 is internally self-consistent as a prospective v1.7 candidate;
- `DEC-055` preserves its historical wording while becoming `SUPERSEDED BY DEC-313`;
- `DEC-313` uses `DEC-034` for the annual retake rule and limits supersession to assessment-credit claim/closure/consumption semantics;
- no Roadmap semantic successor is introduced.

## 9.3 Full-file deterministic integrity test already present

The candidate commit already contains a stronger purpose-built regression suite than an additional spot-check file would provide. `tests/test_ops_upd_004_authority_materialization.py`:

- pins the exact v1.6 Product and Decisions Git blob SHAs;
- reverses every authorised Product v1.7 delta and requires byte-for-byte equality with `00_PLATFORM_v1.6.0.md`;
- reverses every authorised Decisions v1.7 delta and requires byte-for-byte equality with `01_DECISIONS_v1.6.0.md`;
- rejects current candidate semantics that consume at first answer;
- requires one `DEC-313` and explicit `DEC-055` supersession;
- verifies the owner/retake boundaries;
- requires README/manifest to remain on v1.6 until promotion;
- requires DEC identifiers to be contiguous through `DEC-313`.

A duplicate review test briefly created during this pass was removed with a lease-protected branch reset. The candidate branch is again exactly the original one-commit materialisation head above.

## 9.4 Remaining hard gate

The repository's `Foundation Integrity` workflow runs the complete unittest suite and the manifest-backed foundation audit. It triggers on pull requests, pushes to `main`, or explicit `workflow_dispatch` of an exact SHA.

At the reviewed candidate head:

```text
exact-head Foundation Integrity workflow runs = NONE
open PR from authority branch = NONE
```

The available connector can inspect or rerun existing workflow runs but cannot initiate a new `workflow_dispatch`. Opening a PR would trigger CI, but no PR is created without explicit user authorisation.

Therefore the correct disposition is:

```text
MATERIALISED CUMULATIVE v1.7 BYTES: PRESENT
DOCUMENT-LEVEL INDEPENDENT REVIEW: PASS
FULL-FILE DETERMINISTIC REGRESSION TESTS: PRESENT / REVIEWED
CURRENT README/MANIFEST ROUTING: v1.6 / UNCHANGED
EXACT-HEAD FOUNDATION INTEGRITY CI: NOT RUN / REQUIRED
AUTHORITY PROMOTION: NOT AUTHORISED YET
OPS-UPD-004: CONFLICT_STOP REMAINS
OPS-GAP-010: OPEN / CONFLICT_STOP
IMPLEMENTATION: NOT AUTHORISED TO CHOOSE A RULE
NEXT ACTION: obtain exact-head Foundation Integrity CI for feaacff6...; then independently review that exact head before promotion/routing
```

## 9.5 No semantic expansion

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
DISCOVERY SUCCESSOR: NONE
ROADMAP SEMANTIC SUCCESSOR: NOT JUSTIFIED
ARCHITECTURE AMENDMENT: NOT JUSTIFIED
DOMAIN MAP AMENDMENT: NOT JUSTIFIED
BROAD PRE-JIT FREEZE: NOT READY
```


---

# 10. v0.12.0 — Append-only current-state update for PR #90 review handoff

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — EARLIER SECTIONS PRESERVED AS HISTORICAL WORKING STATE**  
> **PR #90 REMAINS REVIEW-ONLY / NOT MERGE-AUTHORISED**  
> **IMPLEMENTATION REMAINS NOT AUTHORISED**

## 10.1 Append-only maintenance rule

This control document is maintained as Markdown only.

```text
artifact format = Markdown
maintenance mode = append-only
DOCX derivative = not required
historical sections = preserve; do not silently rewrite
current status = latest appended section wins for time-sensitive working-state statements
```

The predecessor bytes are preserved unchanged as the prefix of this successor.

```text
predecessor file = NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.11.0.md
predecessor SHA-256 = 9541a6bd9d4da23e5a97ed78f1fd98c99da2f43573acf507655c142c686f94c6
```

This maintenance rule changes no Product, Architecture, Domain, Roadmap, supporting authority, Feature Pack, JIT or implementation semantics.

## 10.2 Live repository state reverified — 2026-10-10

The live GitHub repository was rechecked before this append.

```text
repository = JCSchoeman96/NewYou
main = 086ade7b28c000de1c387acb9760e5eb08bb0413
PR = #90
PR state = OPEN
PR draft = false
PR merged = false
PR base = main
PR base SHA = 086ade7b28c000de1c387acb9760e5eb08bb0413
PR head branch = authority/ops-upd-004-assessment-credit-v1.7.0
PR head SHA = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
PR commits = 1
PR changed files = 3
requested individual reviewers = none
requested team reviewers = none
submitted PR reviews = none
```

The exact three changed paths remain:

1. `docs/00_platform/working/operations_pilot/authority_candidates/00_PLATFORM_v1.7.0.md`
2. `docs/00_platform/working/operations_pilot/authority_candidates/01_DECISIONS_v1.7.0.md`
3. `tests/test_ops_upd_004_authority_materialization.py`

No README/current-authority routing change is part of PR #90.

## 10.3 Exact-head CI state supersedes §9.4's earlier snapshot

Section 9.4 recorded the state before a PR-triggered exact-head run existed. That statement is preserved as historical working evidence but is no longer the current status.

Current exact-head evidence:

```text
workflow = Foundation Integrity
run number = 293
head SHA = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
status = completed
conclusion = success
```

Interpretation:

- the configured Foundation Integrity workflow passed on the exact PR head;
- this removes the earlier "exact-head CI not yet run" blocker;
- CI success is evidence of configured mechanical/integrity checks only;
- CI success is **not** semantic approval;
- the fresh independent hostile semantic review remains mandatory before any promotion recommendation.

## 10.4 Current authority routing remains unchanged

The current repository README still routes default authority through:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `00_PLATFORM_v1.6.0.md`
- `01_DECISIONS_v1.6.0.md`
- `02_OPEN_WORK_v1.2.59.md`
- `03_ARCHITECTURE_v1.1.1.md`
- `04_DOMAIN_MAP_v1.2.0.md`
- `05_ROADMAP_v1.2.0.md`
- `PLATFORM_OPERATING_MODEL_v1.0.1.md`
- `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` where relevant

Therefore:

```text
00_PLATFORM_v1.7.0.md = WORKING AUTHORITY CANDIDATE ONLY
01_DECISIONS_v1.7.0.md = WORKING AUTHORITY CANDIDATE ONLY
current Product Law = 00_PLATFORM_v1.6.0.md
current Decision Register = 01_DECISIONS_v1.6.0.md
OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
implementation = NOT AUTHORISED to choose a rule
```

## 10.5 Independent-review gate is still open

No submitted PR review is recorded and no requested individual/team reviewer is currently recorded.

The earlier authoring-session review material remains prior evidence only. It does not satisfy the required fresh impartial review of the exact PR head.

The next bounded work remains:

1. inspect the exact PR #90 diff and changed candidate files at `feaacff6fb0ca05ed7c0a341852b8f114483dcb7`;
2. inspect the materialisation test itself, not merely its passing result;
3. re-read current Product v1.6, Decisions v1.6, Roadmap FP-003, Domain Map ownership and `OPS-PT-163...174`;
4. pressure-test the candidate independently, especially:
   - post-first-answer `close_unconsumed`;
   - technical versus nontechnical failure ambiguity;
   - qualifying delivery boundary;
   - `DEC-303` composition;
   - `DEC-045` refund separation;
   - Temperament / Entitlements / Identity & Access ownership;
   - `DEC-055` → `DEC-313` supersession scope;
   - duplicate/retry/concurrency convergence;
   - participant-rights consequences;
   - deterministic-test blind spots;
   - SemVer/archive/promotion hygiene;
5. return one formal disposition:
   - `PASS`;
   - `PASS WITH NON-BLOCKING CORRECTIONS`;
   - `CHANGES REQUIRED`; or
   - `BLOCKED / STOP`.

If the result is `CHANGES REQUIRED` or `BLOCKED / STOP`, stop. Do not repair and certify the repair in the same review pass.

## 10.6 Current bounded disposition

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
DISCOVERY SUCCESSOR: NONE
PR #90: OPEN / REVIEW-ONLY / NOT MERGED
EXACT-HEAD FOUNDATION INTEGRITY CI: PASS
FRESH INDEPENDENT SEMANTIC REVIEW: NOT YET COMPLETE
CURRENT AUTHORITY ROUTING: v1.6 PRODUCT / v1.6 DECISIONS
OPS-UPD-004: CONFLICT_STOP REMAINS
OPS-GAP-010: OPEN / CONFLICT_STOP
AUTHORITY PROMOTION: NOT AUTHORISED
IMPLEMENTATION: NOT AUTHORISED
COMPRESSION: NOT YET AUTHORISED
NEXT: FRESH INDEPENDENT ADVERSARIAL REVIEW OF EXACT PR #90 HEAD
```

No `OPS-UPD-008` is created by this append. No existing Product, Decision, Roadmap, Architecture, Domain, Open Work or candidate authority file is amended by this append.


---

# 11. v0.13.0 — Independent PR #90 review outcome: CHANGES REQUIRED

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.12.0 BYTES PRESERVED UNCHANGED**  
> **INDEPENDENT REVIEW OUTCOME: CHANGES REQUIRED**  
> **PR #90: DO NOT MERGE**  
> **AUTHORITY PROMOTION: NOT AUTHORISED**  
> **IMPLEMENTATION: NOT AUTHORISED**  
> **COMPRESSION: NOT READY**

## 11.1 Maintenance and provenance

This successor preserves the complete v0.12.0 document byte-for-byte and appends only the newly supplied independent review outcome plus live-state re-verification.

```text
predecessor file = NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.12.0.md
predecessor SHA-256 = 40a07adb20072159f7a40ecf4f47f6f4acd5bbe1c28a605d09e636a9b879fa1b
maintenance mode = append-only
artifact format = Markdown only
DOCX derivative = not required
```

This append does not alter Product, Architecture, Domain, Roadmap, supporting authority, current Open Work, candidate authority files, tests, CI configuration or implementation.

## 11.2 Review binding

The supplied independent review is bound to:

```text
repository = JCSchoeman96/NewYou
PR = #90
base branch = main
base SHA = 086ade7b28c000de1c387acb9760e5eb08bb0413
head branch = authority/ops-upd-004-assessment-credit-v1.7.0
head SHA = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
merge base = 086ade7b28c000de1c387acb9760e5eb08bb0413
current main = 086ade7b28c000de1c387acb9760e5eb08bb0413
PR state = OPEN
PR draft = false
PR merged = false
changed paths = exactly 3
```

The three changed paths remain:

1. `docs/00_platform/working/operations_pilot/authority_candidates/00_PLATFORM_v1.7.0.md`
2. `docs/00_platform/working/operations_pilot/authority_candidates/01_DECISIONS_v1.7.0.md`
3. `tests/test_ops_upd_004_authority_materialization.py`

Current README routing remains on Product `v1.6.0` and Decisions `v1.6.0`; the `v1.7.0` files remain working authority candidates only.

## 11.3 Superseding correction to v0.12.0 exact-head CI wording

Section 10.3 / 10.6 recorded run #293 as satisfying the exact-head Foundation Integrity requirement.

That interpretation is **incorrect and is superseded by this section**.

The live workflow/run evidence establishes:

```text
workflow = Foundation Integrity
run number = 293
run id = 38057612942
event = pull_request
status = completed
conclusion = success
candidate head SHA = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
Verify exact-head checkout = SKIPPED
```

The workflow's explicit `Verify exact-head checkout` step runs only for `workflow_dispatch` with an exact 40-character SHA input.

Therefore:

- run #293 is valid green PR CI evidence;
- it is useful evidence that the configured tests/audit passed for the PR workflow;
- it does **not** satisfy the repository's stronger SHA-bound exact-head certification gate;
- the current candidate therefore still lacks the required exact-head workflow-dispatch proof.

Historical v0.12.0 text remains preserved; this section is the controlling working-state correction.

## 11.4 Independent review disposition

```text
DISPOSITION = CHANGES REQUIRED
MERGE RECOMMENDATION = DO NOT MERGE PR #90
PROMOTION = NOT AUTHORISED
COMPRESSION = NOT READY
```

The review accepts that:

- the original assessment-credit contradiction is real;
- explicit Product/Decision supersession is required;
- claim/hold versus commercial consumption is directionally sound;
- refundability and consumption are correctly separate lifecycle dimensions;
- current Domain ownership separation is broadly preserved;
- provider/notification/open-read telemetry should remain non-authoritative;
- duplicate/retry/concurrency convergence belongs in the repair.

However, the current candidate is not safe to promote.

## 11.5 Blocking finding IR-B01 — `close_unconsumed` is an unapproved Product/customer-right rule

**Severity:** HIGH — Product authority / participant rights.

The candidate proposes:

```text
post-first-answer nontechnical expiry
→ close_unconsumed
```

This creates a material customer consequence:

```text
pay
→ start assessment
→ save at least one answer
→ nontechnical expiry
→ no successful delivery
→ ordinary refundability already ended under DEC-045
→ paid assessment credit closes without consumption
```

The review finds that this is not merely a mechanical reconciliation of conflicting wording.

It is an explicit new Product/customer-right choice and current authority does not itself authorise that outcome.

**Required correction:**

Product authority must explicitly adjudicate the post-first-answer nontechnical-expiry consequence before DEC-313 can be promoted.

Do not allow JIT, Entitlements or implementation to choose the remedy.

## 11.6 Blocking finding IR-B02 — qualifying delivery is narrower than the current paid assessment promise

**Severity:** HIGH — paid-product fulfilment / commercial correctness.

Current Product/Decision authority includes more than result + report.

Current `DEC-007` states that the paid digital assessment includes:

```text
report + introductory personalised guidance
```

Current Product §7.4 separately lists:

- completion of the digital assessment;
- a temperament result report;
- primary and secondary temperament guidance;
- introductory personalised guidance.

The candidate currently consumes the credit when the immutable governed digital result and paid digital report are durably participant-available.

That does not prove that the full current paid Product promise has been delivered.

Material failure case:

```text
immutable result ready
+ paid report ready
+ separately promised guidance absent/failed
→ candidate currently permits consumption
```

**Required correction:**

Define qualifying delivery against the complete governed paid assessment deliverable required by current Product Law, or explicitly amend Product Law to establish the required guidance as part of the qualifying paid report/delivery boundary.

Do not leave this equivalence to downstream inference.

## 11.7 Blocking finding IR-B03 — `close_unconsumed` leaves DEC-034 / next-purchase eligibility indeterminate

**Severity:** HIGH — entitlement lifecycle / repeat purchase / participant rights.

Current Product §21R.5 deliberately distinguishes:

- purchase eligibility;
- unused paid assessment credit;
- completed attempt;
- annual retake interval;
- Premium reassessment credit.

Current `DEC-034` says:

```text
Permit no more than one assessment retake per year when a valid entitlement exists.
```

The candidate creates a new terminal path:

```text
paid credit
→ first answer
→ nontechnical expiry
→ close_unconsumed
```

but expressly leaves the annual-retake clock/eligibility semantics unchanged.

That creates two plausible but materially different outcomes:

```text
A. no completed/delivered assessment
→ immediate new purchase/attempt may be allowed

B. first answered attempt counts as the annual retake
→ another attempt may be blocked for a year
```

Neither JIT nor Entitlements may choose between these outcomes.

**Required correction:**

Product authority must explicitly state whether a post-first-answer expired/`close_unconsumed` attempt counts against `DEC-034` and identify the Product event from which the relevant interval is evaluated.

Implementation mechanics remain downstream.

## 11.8 Blocking finding IR-B04 — SHA-bound exact-head certification has not been satisfied

**Severity:** BLOCKING GOVERNANCE / EVIDENCE.

The live Foundation Integrity workflow supports a stronger certification route:

```text
workflow_dispatch
+ required exact 40-character SHA input
+ Verify exact-head checkout
```

The existing run #293 was a `pull_request` run and the explicit exact-head verification step was skipped.

Because IR-B01 through IR-B03 require semantic changes, the current SHA should not be certified now merely to satisfy procedure.

**Required correction sequence:**

```text
resolve Product blockers
→ produce corrected candidate
→ obtain new exact head SHA
→ run Foundation Integrity through SHA-bound workflow_dispatch
→ verify exact-head checkout executes and passes
→ perform fresh independent review bound to that exact new SHA
```

Any changed candidate head invalidates the present review for promotion purposes.

## 11.9 Non-blocking governance findings

### IR-N01 — review-only PR is currently non-draft

PR #90 remains `draft = false` despite its review-only / do-not-merge posture.

This is not the substantive reason for `CHANGES REQUIRED`, but it weakens the human safety boundary.

Preferred correction:

```text
restore draft state
or
apply an equivalent enforced protection
```

No PR mutation is performed by this control-register append.

### IR-N02 — earlier working control snapshots are stale by design

Earlier sections preserve historical states such as:

- no PR yet;
- no exact-head run yet;
- review not yet complete;
- v0.12.0's incorrect classification of run #293 as exact-head certification.

These are preserved as historical working evidence and are not silently rewritten.

The latest appended section controls time-sensitive working-state interpretation.

## 11.10 OPS-UPD-004 adjudication after independent review

| Question | Current verdict |
|---|---|
| Original DEC-055 contradiction real? | **YES** |
| Explicit supersession required? | **YES** |
| Claim/hold versus consumption separation sound? | **YES** |
| Result + report delivery boundary sufficient? | **NO / PARTIAL** |
| `close_unconsumed` currently authorised? | **NO** |
| Refundability and consumption separate? | **YES** |
| Product-level duplicate/retry/concurrency invariants directionally sufficient? | **YES** |
| DEC-313 materially over-specifies implementation? | **NO** |
| Existing Domain ownership broadly preserved? | **YES** |
| Safe to promote current candidate? | **NO** |

The candidate is therefore structurally improved over current DEC-055, but structural improvement is not sufficient for Product-law promotion.

## 11.11 Broader Pre-JIT integrity after review

The broader workstream remains useful and materially substantive.

Strengths retained:

- operator work/queues remain separate from business authority;
- provider observations remain evidence rather than financial/business truth;
- notification state remains separate from assessment-credit consumption truth;
- Analytics remains derived;
- exact Resources/locks/retry mechanisms/storage representation remain downstream;
- the stream has exercised duplicate calls, ambiguous outcomes, stale authority, recovery, expiry races and source-domain revalidation;
- no Operations / Support / Admin Domain is currently justified.

However, broad convergence is **not complete**.

The OPS-UPD-004 stream has a false-convergence problem specifically around:

1. post-first-answer `close_unconsumed` becoming concrete before explicit Product acceptance;
2. paid-assessment delivery being reduced to result + report without fully reconciling the separately promised guidance;
3. DEC-034 / next-purchase eligibility remaining unresolved after the new terminal path.

No new `OPS-UPD` identifier is created by this review.

These findings remain within the existing OPS-UPD-004 repair surface unless later Product adjudication demonstrates a genuinely separate upstream class.

## 11.12 Other upstream deltas remain open / unchanged

This review does not close or promote the other existing upstream classes:

- `OPS-UPD-001` — pilot admission/cap;
- `OPS-UPD-002` — duplicate genuine collection/make-whole;
- `OPS-UPD-003` — consequential human-command authority / principally FP-006 operations policy;
- `OPS-UPD-005` — pre-first-fulfilment Plan change;
- `OPS-UPD-006` — valid export followed by Full Deletion; legal/privacy validation remains required;
- `OPS-UPD-007` — General Wellness choice-window clock start.

Do not create another upstream identifier merely to make this review fit the register.

## 11.13 Compression-readiness verdict

```text
COMPRESSION READINESS = NOT READY
```

Do not begin broad compression yet.

Compression remains downstream of:

1. explicit Product adjudication of the three semantic blockers;
2. corrected candidate materialisation;
3. exact-SHA Foundation Integrity dispatch proof;
4. fresh independent review of the changed exact head;
5. separate governed promotion/routing/archive pass;
6. resulting-main verification;
7. continuation of the existing serial upstream-disposition work;
8. final convergence audit.

Once genuinely clean, the intended compact shape remains:

- `README.md`;
- compact Pre-JIT Contract;
- Upstream Delta Register;
- Evidence Index;
- focused Grill where materially justified;
- Compression Audit;
- Source↔Compact Verification;
- hash-bearing Pack Manifest;
- retained `deep/` cumulative discovery/control/promotion evidence outside default context.

## 11.14 Required next actions

The bounded next sequence is:

1. return OPS-UPD-004 to Product adjudication;
2. explicitly decide:
   - the participant right after post-first-answer nontechnical expiry;
   - whether/how that terminal state counts under `DEC-034`;
   - what complete paid assessment deliverable must be durably available before consumption;
3. revise only the v1.7 Product/Decision candidates and deterministic regression evidence necessary to encode the approved semantics;
4. keep README/manifest/current routing on v1.6;
5. obtain the corrected candidate's exact new SHA;
6. run SHA-bound Foundation Integrity via `workflow_dispatch`;
7. verify the exact-head checkout assertion executes and passes;
8. conduct a fresh independent hostile review of that exact new head;
9. only after a clean review, perform the separate governed promotion/routing/archive pass;
10. reverify resulting `main` before closing `OPS-UPD-004` / `OPS-GAP-010`;
11. continue existing serial upstream-disposition work;
12. perform final convergence audit;
13. only then begin compression.

## 11.15 v0.13.0 controlling working-state disposition

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
DISCOVERY SUCCESSOR: NONE
PR #90: OPEN / NON-DRAFT / REVIEW-ONLY / NOT MERGED
PR #90 HEAD: feaacff6fb0ca05ed7c0a341852b8f114483dcb7
PR #90 CHANGED PATHS: 3
PR RUN #293: PASS AS pull_request CI
SHA-BOUND EXACT-HEAD WORKFLOW_DISPATCH: NOT SATISFIED
FRESH INDEPENDENT SEMANTIC REVIEW: COMPLETE
INDEPENDENT REVIEW DISPOSITION: CHANGES REQUIRED
BLOCKERS: IR-B01 / IR-B02 / IR-B03 / IR-B04
CURRENT AUTHORITY ROUTING: v1.6 PRODUCT / v1.6 DECISIONS
OPS-UPD-004: CONFLICT_STOP REMAINS
OPS-GAP-010: OPEN / CONFLICT_STOP
AUTHORITY PROMOTION: NOT AUTHORISED
IMPLEMENTATION: NOT AUTHORISED
COMPRESSION: NOT READY
MERGE RECOMMENDATION: DO NOT MERGE PR #90
NEXT: PRODUCT ADJUDICATION OF OPS-UPD-004 BLOCKERS
```

This append records the supplied independent review and the independently reverified live PR/CI/routing state. It does not repair PR #90, does not certify a replacement candidate, does not merge or mutate repository state, and does not promote v1.7 authority.


---

# 12. v0.14.0 — Accepted OPS-UPD-004 Product adjudication and corrected successor contract

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.13.0 BYTES PRESERVED UNCHANGED**  
> **HUMAN DIRECTION: INDEPENDENT REVIEW CORRECTIONS ACCEPTED**  
> **CURRENT PR #90 HEAD REMAINS UNSAFE / DO NOT MERGE**  
> **CORRECTED PRODUCT SEMANTICS DEFINED BELOW FOR THE NEXT CANDIDATE**  
> **CURRENT AUTHORITY ROUTING REMAINS v1.6 UNTIL A SEPARATE GOVERNED PROMOTION**

## 12.1 Maintenance and provenance

This successor preserves the complete v0.13.0 document byte-for-byte and appends the accepted correction contract only.

```text
predecessor file = NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.13.0.md
predecessor SHA-256 = 0088d5d4e2735e2a15b8c51ab786ee2da103b7b7a234e29cb8559d0af0c3f6fc
maintenance mode = append-only
artifact format = Markdown only
DOCX derivative = not required
```

No existing historical section is rewritten.

The live repository was reverified before this append:

```text
repository = JCSchoeman96/NewYou
current main = 086ade7b28c000de1c387acb9760e5eb08bb0413
PR #90 = OPEN / NOT MERGED / NON-DRAFT
PR #90 current head = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
changed paths = 3
current Product authority = 00_PLATFORM_v1.6.0.md
current Decision authority = 01_DECISIONS_v1.6.0.md
```

Therefore the current PR #90 bytes remain the reviewed `CHANGES REQUIRED` candidate. This append does **not** claim that GitHub already contains the corrected successor.

## 12.2 Explicit Product adjudication — accepted correction set

The independent review corrections are accepted as Product direction for the next OPS-UPD-004 authority candidate.

The corrected Product rule is intentionally participant-safe and minimal:

1. saving the first answer claims/holds the existing ordinary paid assessment credit but does not consume it;
2. commercial consumption occurs only after the **complete current paid digital-assessment deliverable** is durably available to the authorised participant;
3. post-first-answer nontechnical expiry ends the expired attempt but **does not destroy the paid right**;
4. that same credit returns to `available_unused`;
5. an expired undelivered attempt does **not** count as the annual retake event under `DEC-034`;
6. the annual retake interval is evaluated from the prior **successful digital assessment delivery**;
7. refundability remains a separate lifecycle dimension under `DEC-045`;
8. genuine technical failure continues to preserve the same paid obligation for controlled recovery or the existing technical-failure refund path;
9. notification/provider/open/read telemetry remains non-authoritative for consumption;
10. retries, duplicate processing and recovery must converge on one logical paid credit/result/deliverable lineage and may consume at most once.

This adjudication resolves IR-B01, IR-B02 and IR-B03 at the Product-policy level.

IR-B04 remains an evidence/governance gate and can only be satisfied after corrected candidate bytes exist.

## 12.3 Corrected lifecycle model

Assessment-attempt state and assessment-credit state remain separate lifecycle dimensions.

### 12.3.1 Ordinary paid credit states

```text
available_unused
held_unconsumed
consumed
closed_after_refund
```

`close_unconsumed` is removed from the corrected Product model.

### 12.3.2 Core transitions

| Situation | Credit transition | Guard | Product consequence |
|---|---|---|---|
| valid ordinary paid credit; no active answered attempt | `available_unused → available_unused` | entitlement valid | credit may admit one permitted assessment attempt |
| first scored answer saved | `available_unused → held_unconsumed` | one active attempt; current attempt otherwise valid | credit is claimed/held, not consumed |
| active/recoverable attempt continues | `held_unconsumed → held_unconsumed` | no qualifying delivery yet | no commercial consumption |
| result exists but complete paid deliverable is not yet durably available | `held_unconsumed → held_unconsumed` | one or more paid-deliverable components still absent/unavailable | no commercial consumption |
| complete qualifying paid deliverable becomes durably participant-available | `held_unconsumed → consumed` | successful delivery contract in §12.4 satisfied | consume exactly once |
| attempt expires before first answer | `available_unused → available_unused` | DEC-056 expiry | attempt closes; credit remains unused |
| attempt expires after first answer without successful delivery; nontechnical | `held_unconsumed → available_unused` | attempt expired; no successful delivery; no live technical-recovery case | expired attempt becomes terminal; same paid credit is released for a later permitted fresh attempt |
| genuine technical failure under controlled recovery | `held_unconsumed → held_unconsumed` | failure qualifies under existing technical-failure rule | preserve same paid obligation and recover existing lineage where present |
| valid technical-failure refund | `held_unconsumed → closed_after_refund` | refund valid under DEC-045 | close affected right; not delivery and not consumption |

### 12.3.3 Terminal-state interpretation

For the **attempt** lifecycle:

- an expired attempt is terminal;
- it is not resumed as the same ordinary nontechnical expired attempt;
- a later attempt is a fresh attempt using the same still-valid ordinary paid credit where Product eligibility permits.

For the **credit** lifecycle:

- `consumed` is terminal for that logical paid credit;
- `closed_after_refund` is terminal for that logical paid credit;
- `available_unused` is not terminal;
- `held_unconsumed` is not terminal.

An attempt terminal state therefore does not automatically imply a credit terminal state.

## 12.4 Corrected successful-delivery / consumption boundary

The paid assessment promise must be treated as a complete Product deliverable, not reduced to a convenient implementation artifact.

For ordinary paid assessment-credit consumption, successful digital assessment delivery requires:

1. the digital assessment has lawfully completed;
2. the immutable governed digital temperament result exists;
3. the paid temperament result report required by current Product Law is durably participant-available;
4. the required primary and secondary temperament guidance is durably participant-available;
5. the required introductory personalised guidance is durably participant-available;
6. all required paid outputs are available to the authorised participant through an approved participant-access path.

Packaging is not authority.

The guidance may be presented inside the governed paid report or in separately governed participant-visible output. If it is inside the report, the report satisfies that component only when the delivered report version actually contains the required guidance.

Therefore:

```text
result available
+ report available
+ required primary/secondary guidance available
+ required introductory personalised guidance available
= qualifying paid digital assessment delivery
```

Until that complete boundary is satisfied:

```text
credit = held_unconsumed
```

The following remain insufficient on their own:

- result creation;
- report generation;
- notification-provider acceptance;
- email/message delivery;
- participant open/read/view telemetry;
- Analytics completion events;
- provider callbacks unrelated to the complete governed in-product deliverable.

Consumption remains:

```text
complete qualifying paid delivery
→ consume same logical ordinary paid credit exactly once
```

## 12.5 Corrected DEC-034 interaction

The annual retake interval is a Product eligibility rule separate from credit claim/hold and attempt expiry.

For the corrected OPS-UPD-004 semantics:

```text
DEC-034 annual retake reference event
= successful digital assessment delivery
```

The annual interval is **not** started or reset by:

- purchase alone;
- credit grant;
- attempt admission;
- first answer save;
- ordinary credit claim/hold;
- nontechnical attempt expiry;
- technical failure before successful delivery;
- refund without successful delivery.

Consequences:

1. an initial paid assessment with no prior successful digital assessment is not blocked by a nonexistent prior retake clock;
2. once a successful digital assessment has been delivered, a later retake remains subject to the one-per-year rule;
3. when an otherwise permitted later attempt expires without successful delivery, the expired attempt does not itself consume the annual retake opportunity or restart the annual interval;
4. the same paid credit may return to `available_unused`, but a fresh attempt may start only when current Product eligibility, including the annual interval where applicable, permits it;
5. Premium annual reassessment-credit accrual/expiry remains a separate rule and is not redefined by this adjudication.

This removes the ambiguity identified in IR-B03 without collapsing entitlement state and retake eligibility into one lifecycle.

## 12.6 DEC-045 refund separation remains unchanged

Current refundability remains governed separately.

The accepted correction does **not** reopen the existing Product rule that ordinary assessment refunds end after the first answer except for technical failure.

Therefore the post-first-answer nontechnical-expiry consequence is deliberately:

```text
ordinary cash refund = not newly created by this correction
paid assessment right = preserved as the same available_unused credit
attempt = expired / terminal
consumption = no
```

This avoids the rejected outcome where a participant receives no completed paid deliverable, no ordinary refund and also loses the paid assessment right.

## 12.7 Corrected target Product §21R.6 contract

The next Product candidate should replace the rejected `close_unconsumed` semantics with the following substantive meaning:

```markdown
## 21R.6 Assessment-credit claim, delivery, release and consumption

Assessment-attempt/result/report state, paid-deliverable state, annual-retake eligibility and commercial credit state are separate.

Saving the first scored answer claims/holds the existing ordinary paid assessment credit for the active or recoverable attempt. Claiming the credit does not consume it.

Successful digital assessment delivery occurs only when the complete paid digital-assessment deliverable required by current Product Law has been durably made available to the authorised participant through an approved participant-access path. The complete deliverable includes the immutable governed digital result, the paid temperament result report, the required primary/secondary temperament guidance and the required introductory personalised guidance. These outputs may be packaged together or separately; packaging does not alter the delivery requirement.

Participant open/read/view behaviour is not required. Notification-provider acceptance, message delivery, Analytics events, result creation alone, report generation alone, or any incomplete subset of the paid Product promise does not establish the consumption event.

The ordinary paid assessment credit is consumed exactly once only at successful delivery of that complete paid deliverable.

If an attempt expires before the first answer is saved, the attempt ends and the ordinary paid credit remains available and unused.

If an attempt expires after the first answer has been saved, without successful delivery, and the case is not still governed as genuine technical-failure recovery, the expired attempt ends and the same ordinary paid credit is released back to available-unused state. The expired attempt itself cannot be resumed. This release is not a refund, successful delivery or consumption and does not mint a new credit.

A genuine technical failure resolves through controlled recovery of the same paid obligation and existing result/report/guidance lineage where present, or through the existing technical-failure refund path. Recovery must not mint a duplicate credit, result, report, guidance deliverable or consumption.

A valid technical-failure refund closes the affected paid right and is not recorded as successful delivery or consumption.

Duplicate or retried submission, result/report/guidance recovery, delivery processing and consumption signals must converge on one logical paid credit and paid-deliverable lineage and may consume at most once.

For DEC-034, the annual retake interval is evaluated from the prior successful digital assessment delivery. Purchase, credit claim, first-answer save, attempt expiry, technical failure or refund without successful delivery does not start or reset that interval. A fresh attempt after an expired undelivered attempt remains subject to whatever DEC-034 eligibility already applies from the prior successful delivery.

DEC-045 refundability remains separate. DEC-054, DEC-056, DEC-061, DEC-066, DEC-067 and DEC-303 otherwise remain unchanged.
```

The final promoted wording may be editorially tightened, but it must preserve these semantics exactly.

## 12.8 Corrected target DEC-313 contract

The next Decision candidate should replace the rejected DEC-313 body with the following substantive decision:

```markdown
## DEC-313 — Assessment-credit claim, complete delivery, release and consumption
**Status:** LOCKED

An ordinary paid digital-assessment credit is not consumed when an assessment attempt is admitted or when the first scored answer is saved. Saving the first scored answer claims/holds the existing credit for the active or recoverable attempt.

Successful digital assessment delivery requires durable authorised-participant availability of the complete paid assessment deliverable required by Product Law: the immutable governed digital result, paid temperament result report, required primary/secondary temperament guidance and required introductory personalised guidance. These outputs may be packaged together or separately. Participant open/read/view behaviour and notification/provider/Analytics state are not consumption authority.

The ordinary paid credit is consumed exactly once only at that complete successful-delivery boundary.

If an attempt expires before the first answer is saved, the attempt ends and the credit remains available unused. If an attempt expires after the first answer is saved without successful delivery and the case is not still governed as genuine technical-failure recovery, the expired attempt ends and the same paid credit returns to available-unused state. The expired attempt cannot be resumed; release does not mint a new credit and is neither refund nor consumption.

A genuine technical failure preserves the same paid obligation for controlled recovery of the existing lineage where present or the existing technical-failure refund path. A valid technical-failure refund closes the affected right and is not successful delivery or consumption. Duplicate/retried processing must converge on one logical paid credit/deliverable lineage and may consume at most once.

For DEC-034, the annual retake interval is evaluated from the prior successful digital assessment delivery. An undelivered expired attempt does not itself start, reset or consume that annual interval. Any later fresh attempt must still satisfy current DEC-034 eligibility.

DEC-045 refundability remains separate. DEC-054, DEC-056, DEC-061, DEC-066, DEC-067 and DEC-303 otherwise remain unchanged. DEC-313 supersedes DEC-055 for ordinary paid assessment-credit claim, complete-delivery, release and consumption semantics.
```

## 12.9 Corrected deterministic materialisation-test obligations

The next candidate's deterministic regression test must continue proving predecessor-scope discipline and must additionally prove the accepted semantic corrections.

At minimum it must prove:

1. Product and Decision successors reverse to the exact pinned v1.6 predecessor blobs after removal of only authorised OPS-UPD-004 deltas;
2. no current first-answer consumption rule survives;
3. no `close_unconsumed` Product consequence survives in the corrected candidate;
4. post-first-answer nontechnical expiry releases the **same** ordinary paid credit to available-unused state;
5. the expired attempt remains terminal and is not silently resumed;
6. release does not create a second credit;
7. qualifying delivery requires the complete Product-paid deliverable, not only result + report;
8. primary/secondary temperament guidance is represented in the qualifying-delivery contract;
9. introductory personalised guidance is represented in the qualifying-delivery contract;
10. incomplete paid delivery cannot trigger consumption;
11. DEC-034's reference event is successful digital assessment delivery;
12. purchase, claim, first answer, expiry, technical failure and refund without successful delivery do not start/reset the annual retake interval;
13. a later fresh attempt still remains subject to any already-running DEC-034 interval from the prior successful delivery;
14. DEC-045 remains a separate refundability rule;
15. Temperament / Entitlements / Identity & Access ownership remains unchanged;
16. notification/provider/open-read/Analytics state remains non-authoritative for consumption;
17. duplicate/retry/recovery semantics converge on one logical paid credit/deliverable lineage;
18. consumption remains at-most-once;
19. DEC-055 is explicitly superseded by DEC-313 only for the bounded assessment-credit semantics;
20. DEC identifiers remain contiguous;
21. README/manifest/current routing remains on v1.6 during review-only materialisation.

The deterministic test remains mechanical evidence. It cannot substitute for the fresh semantic review of the corrected exact head.

## 12.10 Corrected successor build scope

The next candidate remains deliberately narrow.

### Product successor

Permitted semantic changes:

- Product version/amendment metadata;
- remove first-answer consumption wording where still present;
- replace rejected post-first-answer `close_unconsumed` with release to the same `available_unused` credit;
- define complete paid-deliverable consumption boundary;
- define DEC-034 successful-delivery reference event;
- preserve DEC-045 separation;
- update internal current-version metadata where required.

No unrelated Product semantic expansion is authorised.

### Decision successor

Permitted semantic changes:

- version/amendment metadata;
- preserve DEC-055 historically but mark it superseded by DEC-313 for the bounded assessment-credit semantics;
- replace DEC-313 with the accepted corrected rule;
- no unrelated DEC/OQ change.

### Explicit non-changes

Still not justified by this correction:

- North Star semantic successor;
- Architecture amendment;
- Domain Map amendment;
- new Operations/Admin/Support Domain;
- provider/channel selection;
- implementation Resource/action/schema choice;
- queue/worker/lock/storage representation;
- legal-sufficiency finding;
- compression;
- implementation authorisation.

Roadmap should only receive a later routing/reference patch if needed after Product/Decision promotion; no new Roadmap semantic rule is created by this correction unless a fresh contradiction is found.

## 12.11 Governance/certification sequence after corrected materialisation

The present PR #90 head is no longer promotable and must not be merged.

The correction sequence is:

```text
accepted Product adjudication
→ materialise corrected v1.7 candidate bytes from current v1.6 authority
→ update deterministic materialisation test
→ produce new exact candidate SHA
→ keep README/manifest/current routing on v1.6
→ run Foundation Integrity through SHA-bound workflow_dispatch
→ Verify exact-head checkout must execute and pass
→ fresh independent hostile review of that exact SHA
→ if PASS / PASS WITH NON-BLOCKING CORRECTIONS only:
     separate governed promotion/routing/archive pass
→ resulting-main Foundation Integrity + independent post-merge verification
→ only then close OPS-UPD-004 / OPS-GAP-010
```

If the corrected exact-head review returns `CHANGES REQUIRED` or `BLOCKED / STOP`, stop again.

Do not self-certify a repair in the same review pass.

## 12.12 PR #90 handling

Current live state remains:

```text
PR #90 head = feaacff6fb0ca05ed7c0a341852b8f114483dcb7
review outcome on that head = CHANGES REQUIRED
merge recommendation = DO NOT MERGE
```

This append does not mutate PR #90.

If PR #90 is reused for the corrected candidate, the branch must receive new corrected bytes and therefore a new head SHA. The prior semantic review then becomes historical evidence only.

If governance prefers a replacement clean branch/PR instead, that is also acceptable provided the new candidate is still materialised from current `main`/v1.6 authority and receives the same exact-head proof/review.

## 12.13 Compression readiness

Compression remains blocked.

```text
COMPRESSION = NOT READY
```

The accepted Product adjudication resolves the three semantic questions conceptually, but the corrected authority candidate has not yet been materialised, SHA-certified, independently re-reviewed, promoted or resulting-main certified.

Do not compress the broad Pre-JIT stream until OPS-UPD-004 has completed that governed cycle and the remaining serial upstream-disposition/convergence work is clean.

## 12.14 v0.14.0 controlling working-state disposition

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
DISCOVERY SUCCESSOR: NONE

INDEPENDENT REVIEW FINDINGS: ACCEPTED
IR-B01 PRODUCT POLICY: RESOLVED BY EXPLICIT HUMAN ADJUDICATION
IR-B02 COMPLETE PAID-DELIVERABLE BOUNDARY: RESOLVED BY EXPLICIT HUMAN ADJUDICATION
IR-B03 DEC-034 INTERACTION: RESOLVED BY EXPLICIT HUMAN ADJUDICATION
IR-B04 SHA-BOUND EXACT-HEAD CERTIFICATION: STILL OPEN

CORRECTED POST-FIRST-ANSWER NONTECHNICAL EXPIRY:
  expired attempt terminal
  same paid credit → available_unused
  no refund created
  no consumption
  no duplicate credit

CORRECTED CONSUMPTION BOUNDARY:
  complete paid assessment deliverable
  = immutable governed result
    + paid result report
    + required primary/secondary guidance
    + required introductory personalised guidance
  all durably available to authorised participant
  → consume exactly once

CORRECTED DEC-034 REFERENCE EVENT:
  prior successful digital assessment delivery

CURRENT PR #90 HEAD: feaacff6fb0ca05ed7c0a341852b8f114483dcb7
CURRENT PR #90 REVIEW STATUS: CHANGES REQUIRED / SUPERSEDED FOR PROMOTION
CURRENT AUTHORITY ROUTING: v1.6 PRODUCT / v1.6 DECISIONS
OPS-UPD-004: CONFLICT_STOP REMAINS UNTIL CORRECTED GOVERNED PROMOTION
OPS-GAP-010: OPEN / CONFLICT_STOP
IMPLEMENTATION: NOT AUTHORISED
COMPRESSION: NOT READY
MERGE CURRENT PR #90 HEAD: DO NOT MERGE

NEXT:
  MATERIALISE CORRECTED v1.7 PRODUCT/DECISION CANDIDATE
  + UPDATE DETERMINISTIC TEST
  + NEW EXACT SHA
  + SHA-BOUND WORKFLOW_DISPATCH
  + FRESH INDEPENDENT REVIEW
```

This append records the accepted Product correction contract. It does not claim corrected GitHub bytes, does not merge or mutate repository state, and does not make v1.7 current authority.


---

# 13. v0.15.0 — OPS-UPD-004 correction pass: TDD RED complete, candidate materialisation safely stopped

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.14.0 BYTES PRESERVED UNCHANGED**  
> **CORRECTION PASS STATUS: PARTIAL / CONTROLLED STOP**  
> **TDD RED: COMPLETE AND VERIFIED**  
> **CORRECTED PRODUCT/DECISION BYTES: NOT YET MATERIALISED**  
> **PR #90: DRAFT / DO NOT MERGE**  
> **CURRENT AUTHORITY: v1.6 PRODUCT / v1.6 DECISIONS**  
> **COMPRESSION: NOT READY**

## 13.1 Maintenance and provenance

This successor preserves the complete v0.14.0 document byte-for-byte and appends only the verified results of the next correction pass.

```text
predecessor file = NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.14.0.md
predecessor SHA-256 = 699296f9b9152a9d9ec230ab6e8ffc03f49c18651c50d7d116946bbbb33067a3
maintenance mode = append-only
artifact format = Markdown only
DOCX derivative = not required
```

This pass intentionally does **not** claim successful materialisation of corrected Product/Decision candidates.

## 13.2 Live repository binding before and after the pass

The canonical live repository remained:

```text
repository = JCSchoeman96/NewYou
current main = 086ade7b28c000de1c387acb9760e5eb08bb0413
```

`main` was independently reverified after the branch mutation and remained unchanged.

PR #90 now has:

```text
PR = #90
state = OPEN
draft = true
merged = false
base = main
base SHA = 086ade7b28c000de1c387acb9760e5eb08bb0413
head branch = authority/ops-upd-004-assessment-credit-v1.7.0
head SHA = c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
commits = 2
changed paths = 3
```

The three changed paths remain exactly:

1. `docs/00_platform/working/operations_pilot/authority_candidates/00_PLATFORM_v1.7.0.md`
2. `docs/00_platform/working/operations_pilot/authority_candidates/01_DECISIONS_v1.7.0.md`
3. `tests/test_ops_upd_004_authority_materialization.py`

No README, manifest, Roadmap, Architecture, Domain Map or current-authority-path change was made.

## 13.3 Test-first correction commit

The accepted v0.14.0 Product correction contract was encoded into the deterministic regression test **before** changing the candidate documents.

Commit:

```text
c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
message = test: encode accepted OPS-UPD-004 corrections
```

The updated test now requires, among other invariants:

- no surviving `close_unconsumed`;
- post-first-answer nontechnical expiry to terminate the expired attempt and release the **same** credit to `available_unused`;
- no duplicate/replacement credit creation;
- complete paid assessment delivery before consumption:
  - immutable governed result;
  - paid temperament result report;
  - required primary/secondary temperament guidance;
  - required introductory personalised guidance;
- incomplete paid delivery cannot trigger consumption;
- DEC-034 annual-retake reference event = prior successful digital assessment delivery;
- purchase/claim/first answer/expiry/technical failure/refund without successful delivery do not start or reset that interval;
- DEC-045 remains a separate refundability lifecycle dimension;
- existing Domain ownership remains unchanged;
- notification/provider/open-read/Analytics state remains non-authoritative;
- duplicate/retry/recovery processing converges on one logical paid credit/complete-deliverable lineage;
- consumption remains at-most-once;
- DEC-055 is superseded only for the bounded OPS-UPD-004 semantics;
- current README/manifest routing remains on v1.6 while the candidate is under review;
- the Product and Decision candidates remain reversible byte-for-byte to the exact pinned v1.6 predecessor blobs after removing only the authorised delta.

## 13.4 TDD RED evidence

Foundation Integrity automatically ran on the test-only head.

```text
workflow = Foundation Integrity
run number = 294
run id = 38075935696
event = pull_request
head SHA = c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
status = completed
conclusion = failure
tests run = 313
failures = 4
Verify exact-head checkout = skipped
manifest-backed foundation audit = skipped after unit-test failure
```

The four failures were the intended semantic failures:

1. the old Product candidate still contains `close_unconsumed`;
2. the old Product candidate still closes the paid credit after post-first-answer nontechnical expiry;
3. the old Decision candidate still contains the rejected DEC-055 / DEC-313 wording;
4. the old Product amendment scope still describes the rejected candidate semantics.

No syntax failure, broken test harness or unrelated regression was observed in this RED pass.

Therefore the TDD RED gate is valid:

```text
NEW TEST EXPECTATIONS = ACTIVE
OLD CANDIDATE SEMANTICS = PROVEN INCOMPATIBLE
RED CAUSE = INTENDED OPS-UPD-004 CORRECTION DELTA
```

## 13.5 Why Product/Decision materialisation was stopped

The next required operation is a bounded textual replacement inside two large cumulative frozen-authority candidate files:

```text
00_PLATFORM_v1.7.0.md  ≈ 6,700 lines
01_DECISIONS_v1.7.0.md ≈ 1,600 lines
```

The available authenticated GitHub write interface for repository files supports **complete-file replacement**, not safe server-side patch/hunk replacement.

The current environment can read exact repository ranges, but it cannot pipe the existing full remote file bytes directly into a byte-preserving authenticated patch operation.

Reconstructing roughly eight thousand lines of cumulative Product/Decision text through generated full-file replacement would create an unacceptable risk of:

- accidental unrelated textual drift;
- whitespace/newline drift;
- historical-law corruption;
- hidden changes outside OPS-UPD-004;
- a false sense of safety merely because later tests might cover only enumerated transformations.

That would violate the project's correctness-first governance posture and the purpose of the deterministic reverse-transform test.

Therefore this pass **stopped rather than perform an unsafe whole-file rewrite**.

This is a tooling/write-path limitation, not a semantic uncertainty about the accepted Product correction.

## 13.6 PR #90 safety correction

Because the current branch is intentionally RED and incomplete, PR #90 was converted back to **draft**.

Its body was also updated to state accurately that:

- original head `feaacff6...` received `CHANGES REQUIRED`;
- current head `c00aa9f0...` is the test-first RED step only;
- the two authority candidates still contain the rejected semantics;
- run #294 is RED evidence, not certification;
- Product v1.6.0 and Decisions v1.6.0 remain current authority;
- the corrected candidate still needs materialisation, exact-SHA certification and fresh independent review;
- the PR must not be merged.

This closes the earlier non-blocking governance weakness where a review-only unsafe candidate was non-draft.

## 13.7 Current semantic status

The accepted Product adjudication from v0.14.0 remains the governing **working correction contract** for the next candidate.

Conceptually resolved:

```text
IR-B01 = Product choice adjudicated
IR-B02 = complete paid-deliverable boundary adjudicated
IR-B03 = DEC-034 interaction adjudicated
```

Not yet materially resolved in candidate bytes:

```text
IR-B01 = NOT YET ENCODED IN PRODUCT/DECISION CANDIDATE
IR-B02 = NOT YET ENCODED IN PRODUCT/DECISION CANDIDATE
IR-B03 = NOT YET ENCODED IN PRODUCT/DECISION CANDIDATE
```

Still open independently:

```text
IR-B04 = SHA-BOUND EXACT-HEAD CERTIFICATION NOT SATISFIED
```

This distinction is important: human Product adjudication is complete, but governed authority materialisation and proof are not.

## 13.8 Current authority and conflict state

Nothing in this pass changes current authority.

```text
current Product Law = 00_PLATFORM_v1.6.0.md
current Decision Register = 01_DECISIONS_v1.6.0.md
candidate Product v1.7.0 = working / non-authoritative / rejected bytes still present
candidate Decisions v1.7.0 = working / non-authoritative / rejected bytes still present
OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
```

DEC-055 therefore remains live current Decision authority until a corrected successor is lawfully promoted.

## 13.9 Exact next safe materialisation operation

The next authoring environment must support one of these safe mechanisms:

1. a normal Git worktree/checkout with authenticated push access;
2. a repository-edit capability that can apply exact patches/hunks to existing files;
3. another mechanism that reads the existing full candidate bytes locally, applies deterministic substitutions, verifies the reverse transform, and pushes the resulting exact files without generative reconstruction.

The required candidate transformation remains exactly the v0.14.0 contract:

### Product candidate

- replace v1.7 amendment scope with the accepted complete-delivery/release/DEC-034 semantics;
- replace the §21B.3 assessment-credit pointer from `closure` to `release`;
- replace old §21R.6 with corrected `claim, complete delivery, release and consumption`;
- make post-first-answer nontechnical expiry:
  - expired attempt terminal;
  - same credit → `available_unused`;
  - no refund created;
  - no consumption;
  - no duplicate credit;
- require complete paid deliverable before consumption;
- define DEC-034 reference event as prior successful digital assessment delivery;
- keep all unrelated Product text byte-identical.

### Decision candidate

- replace v1.7 amendment scope with accepted bounded semantics;
- preserve DEC-055 historically but mark it superseded by DEC-313 for the bounded assessment-credit semantics;
- replace DEC-313 with the accepted complete-delivery/release/DEC-034 rule;
- keep all unrelated Decision text byte-identical.

### Test

The current test-first head already contains the accepted regression expectations. It should not be loosened to make the old candidate pass.

## 13.10 Required proof after materialisation

Once corrected bytes are safely materialised:

```text
corrected Product/Decision candidate
→ deterministic reverse-transform test GREEN
→ all unit tests GREEN
→ manifest-backed foundation audit GREEN
→ new exact candidate SHA
```

Then the stronger certification gate remains mandatory:

```text
Foundation Integrity workflow_dispatch
ref = exact corrected 40-character candidate SHA
Verify exact-head checkout = EXECUTED + PASS
unit tests = PASS
manifest-backed foundation audit = PASS
```

A normal `pull_request` run is useful but is **not** a substitute for this exact-SHA dispatch proof.

## 13.11 Independent-review boundary

This correction pass authored the test-first repair expectations.

Therefore this pass may verify mechanics, but it must **not** provide the required fresh independent semantic certification of the eventual corrected candidate.

After corrected bytes and exact-SHA CI exist:

```text
new exact head
→ fresh independent hostile review by a reviewer who did not author/modify that candidate
```

Accepted review outcomes remain:

- `PASS`
- `PASS WITH NON-BLOCKING CORRECTIONS`
- `CHANGES REQUIRED`
- `BLOCKED / STOP`

Only a clean result permits the later governed promotion pass.

## 13.12 Compression and implementation remain blocked

```text
IMPLEMENTATION = NOT AUTHORISED
COMPRESSION = NOT READY
```

No JIT implementation, OPS-UPD-001 work, compression, archive migration or authority promotion should start from this partial RED head.

The serial order remains:

```text
finish OPS-UPD-004 corrected authority cycle
→ resulting-main certification
→ close OPS-UPD-004 / OPS-GAP-010
→ continue remaining serial upstream-disposition work
→ final convergence audit
→ compression
```

## 13.13 v0.15.0 controlling working-state disposition

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0

USER PRODUCT ADJUDICATION: ACCEPTED
TDD TEST-FIRST COMMIT: COMPLETE
TEST-FIRST HEAD: c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
FOUNDATION INTEGRITY RUN #294: EXPECTED RED
RUN #294 TESTS: 313
RUN #294 FAILURES: 4 / ALL INTENDED SEMANTIC FAILURES
CORRECTED PRODUCT CANDIDATE BYTES: NOT YET MATERIALISED
CORRECTED DECISION CANDIDATE BYTES: NOT YET MATERIALISED
EXACT-SHA WORKFLOW_DISPATCH: NOT YET APPLICABLE / NOT SATISFIED
FRESH INDEPENDENT REVIEW OF CORRECTED HEAD: NOT YET APPLICABLE

PR #90: OPEN / DRAFT / DO NOT MERGE
PR #90 HEAD: c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
CURRENT MAIN: 086ade7b28c000de1c387acb9760e5eb08bb0413
CURRENT AUTHORITY ROUTING: v1.6 PRODUCT / v1.6 DECISIONS
OPS-UPD-004: CONFLICT_STOP
OPS-GAP-010: OPEN / CONFLICT_STOP
IMPLEMENTATION: NOT AUTHORISED
COMPRESSION: NOT READY

PASS OUTCOME FOR THIS AUTHORING PASS:
  TDD RED = PASS
  SAFE BYTE-PRESERVING MATERIALISATION = BLOCKED BY AVAILABLE WRITE PATH
  UNSAFE FULL-FILE RECONSTRUCTION = REJECTED

NEXT SAFE ACTION:
  APPLY THE EXACT v0.14.0 PRODUCT/DECISION DELTAS IN AN AUTHENTICATED
  BYTE-PRESERVING CHECKOUT/PATCH ENVIRONMENT, THEN RETURN WITH THE NEW
  EXACT CANDIDATE SHA FOR GREEN CI + SHA-BOUND CERTIFICATION + FRESH REVIEW.
```

This append records only verified work completed in the pass. It does not pretend that RED is GREEN, does not treat Product adjudication as authority promotion, and does not weaken the requirement for byte-preserving candidate materialisation.


---

# 14. v0.16.0 — OPS-UPD-004 corrected candidate materialised; ordinary CI green; exact-SHA certification remains blocking

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.15.0 BYTES PRESERVED UNCHANGED**  
> **CORRECTED CANDIDATE MATERIALISATION: PASS**  
> **BOUNDED DIFF VERIFICATION: PASS**  
> **PR-TRIGGERED FOUNDATION INTEGRITY: PASS**  
> **SHA-BOUND `workflow_dispatch` CERTIFICATION: NOT YET SATISFIED**  
> **FRESH INDEPENDENT SEMANTIC REVIEW: REQUIRED AFTER SHA CERTIFICATION**  
> **PR #90: OPEN / DRAFT / DO NOT MERGE**  
> **CURRENT AUTHORITY: v1.6 PRODUCT / v1.6 DECISIONS**  
> **COMPRESSION / IMPLEMENTATION / PROMOTION: NOT AUTHORISED**

## 14.1 Maintenance and provenance

This successor preserves the complete v0.15.0 document byte-for-byte and appends only the verified results of the corrected-candidate materialisation and mechanical proof pass.

```text
predecessor file = NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.15.0.md
predecessor SHA-256 = a80cf68cc820c4b3c096aad8a0d143080a52fded02182b6b6490debc51ff3734
maintenance mode = append-only
artifact format = Markdown only
DOCX derivative = not required
```

The earlier v0.15.0 safe-write-path stop is historical context only. This pass found and used a lower-level authenticated Git-data route that could preserve the current candidate bytes and expose the correction atomically.

## 14.2 Live repository state after materialisation

The canonical live repository state was independently reverified after the candidate commit.

```text
repository = JCSchoeman96/NewYou
main = 086ade7b28c000de1c387acb9760e5eb08bb0413

PR = #90
state = OPEN
draft = true
merged = false
base = main
base SHA = 086ade7b28c000de1c387acb9760e5eb08bb0413
head branch = authority/ops-upd-004-assessment-credit-v1.7.0
head SHA = bdb174e31259714081cfd9348f1b0175699b2059
commits = 3
changed paths = 3
```

The PR remains explicitly review-only and **DO NOT MERGE**.

The three PR paths remain:

1. `docs/00_platform/working/operations_pilot/authority_candidates/00_PLATFORM_v1.7.0.md`
2. `docs/00_platform/working/operations_pilot/authority_candidates/01_DECISIONS_v1.7.0.md`
3. `tests/test_ops_upd_004_authority_materialization.py`

No README, authority manifest, Roadmap, Architecture, Domain Map or current-authority route was changed.

## 14.3 Atomic candidate materialisation

The RED-head candidate bytes were used as the exact base.

```text
RED head = c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
RED-head tree = 095b1035dade1754fb9c32044f28268e74397771

old Product candidate blob =
  e35b7c941146ab630fda0f3931ad38b57d491b24

old Decisions candidate blob =
  ae40e13b6cdabb441df82f5fac2e8f64208b2544
```

The accepted v0.14.0 correction contract was applied to those exact candidate contents and materialised as new Git blobs:

```text
corrected Product blob =
  bf4f2b2f70d1464de77b4c0fcc100e982cdcbbee

corrected Decisions blob =
  259b2b1e3a10ade991a788d8a8c183ffb7719e80

corrected tree =
  96c3e336b171721731c85062e15a00759aea1a33
```

One commit was created with parent `c00aa9f0...`:

```text
commit =
  bdb174e31259714081cfd9348f1b0175699b2059

message =
  docs: correct OPS-UPD-004 v1.7 authority candidate
```

The branch reference was then advanced with a lease:

```text
expected old head =
  c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae

new head =
  bdb174e31259714081cfd9348f1b0175699b2059

force = false
result = success
```

Therefore the repository was not exposed to a half-corrected Product-only or Decision-only intermediate head.

## 14.4 Exact correction-commit diff boundary

The immutable comparison:

```text
c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
→
bdb174e31259714081cfd9348f1b0175699b2059
```

showed exactly two changed files:

```text
00_PLATFORM_v1.7.0.md
  +11 / -11
  22 line changes

01_DECISIONS_v1.7.0.md
  +10 / -8
  18 line changes

total = 40 line changes
other paths changed by materialisation commit = 0
```

The existing test-first regression file did not change in the materialisation commit.

The inspected hunks were confined to the accepted OPS-UPD-004 correction surface:

### Product

- corrected the v1.7.0 amendment-scope description;
- changed §21B.3's assessment-credit pointer from `closure` semantics to `release` semantics;
- replaced §21R.6 with the accepted claim / complete-delivery / release / consumption contract;
- defined complete paid deliverable before consumption;
- made post-first-answer nontechnical expiry release the same credit;
- defined the DEC-034 reference event as prior successful digital assessment delivery.

### Decisions

- corrected the v1.7.0 amendment-scope description;
- corrected DEC-055's supersession pointer;
- replaced DEC-313 with the accepted claim / complete-delivery / release / DEC-034 interaction rule.

No unrelated Product or Decision area was intentionally changed.

## 14.5 Corrected semantics now encoded

The current candidate at `bdb174e3...` encodes the accepted Product adjudication:

```text
first answer saved
→ claim / hold same ordinary paid assessment credit
→ not consumed
```

Successful consumption boundary:

```text
immutable governed digital result
+ paid temperament result report
+ required primary/secondary temperament guidance
+ required introductory personalised guidance
+ durable authorised-participant availability through approved access path
→ consume ordinary paid credit exactly once
```

Incomplete subsets do not qualify.

Post-first-answer nontechnical expiry now means:

```text
expired attempt = terminal
same ordinary paid credit = available_unused
expired attempt = cannot resume
new/replacement credit = not minted
refund = not created merely by expiry
consumption = no
successful delivery = no
```

DEC-034 interaction now means:

```text
annual retake interval reference event =
  prior successful digital assessment delivery
```

The following do not start or reset that interval in the absence of successful delivery:

- purchase;
- ordinary credit grant/claim;
- attempt admission;
- first-answer save;
- nontechnical attempt expiry;
- technical failure before successful delivery;
- refund without successful delivery.

DEC-045 refundability remains a separate lifecycle dimension.

Existing ownership remains:

```text
Temperament
→ attempt / result / report truth

Entitlements
→ assessment-credit / right truth

Identity & Access
→ access assurance
```

Provider state, notification state, open/read/view telemetry and Analytics remain non-authoritative for consumption.

Duplicate/retried submission, recovery, delivery and consumption processing must converge on one logical paid-credit / complete-deliverable lineage with at-most-once consumption.

## 14.6 TDD RED → GREEN progression

The test-first RED head remained:

```text
c00aa9f0ccac983bd1ebe10e2b1fcd0a476174ae
```

Foundation Integrity #294 had already proved the old candidate incompatible with the accepted correction contract:

```text
run number = 294
run id = 38075935696
result = expected failure
semantic failures = 4
```

After materialisation, Foundation Integrity ran automatically on the corrected exact PR head:

```text
workflow = Foundation Integrity
run number = 295
run id = 38078038949
head SHA = bdb174e31259714081cfd9348f1b0175699b2059
event = pull_request
status = completed
conclusion = success
```

Verified job steps:

```text
Check out repository = PASS
Verify exact-head checkout = SKIPPED
Set up Python = PASS
Run unit tests = PASS
Run manifest-backed foundation audit = PASS
Complete job = PASS
```

This gives a valid RED → corrected candidate → ordinary GREEN sequence.

## 14.7 What Foundation Integrity #295 proves — and what it does not

Run #295 proves that the corrected PR head passes the repository's normal pull-request mechanical gates:

```text
unit-test suite = PASS
deterministic OPS-UPD-004 materialisation regression = PASS as part of suite
manifest-backed foundation audit = PASS
```

It also materially strengthens the no-drift evidence because the deterministic candidate test is designed to reverse the authorised v1.7 deltas back to the exact pinned v1.6 predecessor blobs.

However:

```text
Verify exact-head checkout = SKIPPED
```

That skip is expected for a `pull_request` workflow event.

Therefore:

```text
Foundation Integrity #295 PASS
≠
SHA-bound certification
```

The stronger IR-B04 proof remains outstanding.

## 14.8 SHA-bound workflow contract independently confirmed

The live `.github/workflows/foundation-integrity.yml` at the corrected head was inspected.

It requires a `workflow_dispatch` path with a required `ref` input containing the exact 40-character SHA for the explicit exact-head verification step.

The required certification target is:

```text
workflow = Foundation Integrity
event = workflow_dispatch
ref input = bdb174e31259714081cfd9348f1b0175699b2059

Verify exact-head checkout = EXECUTED + PASS
Run unit tests = PASS
Run manifest-backed foundation audit = PASS
overall workflow = PASS
```

A normal pull-request run or a rerun of that pull-request event is not equivalent.

## 14.9 Connected-tool limitation at IR-B04

The connected authenticated GitHub capability was exhaustively checked for the relevant Actions write surface.

It exposes workflow/rerun read and rerun capabilities but does **not** expose a `workflow_dispatch` mutation.

A rerun would preserve the original pull-request event and would again skip the exact-head assertion.

Therefore this pass deliberately did **not**:

- pretend that #295 satisfies IR-B04;
- rerun #295 and relabel it as SHA-bound proof;
- modify the workflow to manufacture an equivalent event;
- weaken the certification requirement.

Current status:

```text
IR-B04 = OPEN / BLOCKING
reason = required workflow_dispatch mutation unavailable in connected authoring surface
semantic uncertainty = no
mechanical candidate failure = no
```

The next capable environment must invoke the repository's existing Foundation Integrity `workflow_dispatch` with the exact `ref` input above.

## 14.10 Independent-review separation remains mandatory

This pass authored and materialised the corrected candidate.

It is therefore **not eligible** to provide the required fresh independent semantic certification for `bdb174e3...`.

After IR-B04 is satisfied on exactly the same SHA:

```text
bdb174e31259714081cfd9348f1b0175699b2059
→ fresh hostile semantic review
→ reviewer must not have authored or modified this corrected candidate
```

The reviewer must independently inspect at least:

- exact PR #90 diff and three changed paths;
- Product v1.6 predecessor;
- Decisions v1.6 predecessor;
- Roadmap FP-003;
- Domain Map ownership;
- DEC-034;
- DEC-045;
- DEC-054;
- DEC-055 historical wording and bounded supersession;
- DEC-056;
- DEC-061;
- DEC-066;
- DEC-067;
- DEC-303;
- DEC-313 candidate wording;
- complete paid-deliverable boundary;
- post-first-answer expiry participant-right consequences;
- retries, duplicates, recovery, concurrency and at-most-once consumption;
- provider / notification / telemetry non-authority;
- deterministic materialisation test blind spots;
- SemVer, archive and promotion requirements.

Accepted review outcomes remain:

- `PASS`
- `PASS WITH NON-BLOCKING CORRECTIONS`
- `CHANGES REQUIRED`
- `BLOCKED / STOP`

Any candidate-head change invalidates that review.

## 14.11 PR #90 governance state corrected

The PR description was updated after run #295 completed so it no longer claims that the run is in progress.

It now states:

- original `feaacff6...` review outcome = `CHANGES REQUIRED`;
- `c00aa9f0...` = TDD RED head;
- `bdb174e3...` = current corrected candidate;
- exact materialisation diff = 40 total line changes across only Product/Decisions;
- Foundation Integrity #295 = SUCCESS;
- unit tests = PASS;
- manifest-backed foundation audit = PASS;
- exact-head verification = SKIPPED because the event was `pull_request`;
- SHA-bound `workflow_dispatch` remains blocking;
- fresh independent semantic review remains blocking;
- current Product/Decisions authority remains v1.6;
- PR remains draft and must not be merged.

Current PR governance:

```text
PR #90 = OPEN
draft = true
DO NOT MERGE = yes
requested reviewers = none verified in current PR metadata
```

## 14.12 Current authority and conflict state remain unchanged

No authority promotion occurred in this pass.

```text
current main =
  086ade7b28c000de1c387acb9760e5eb08bb0413

current Product Law =
  00_PLATFORM_v1.6.0.md

current Decision Register =
  01_DECISIONS_v1.6.0.md

candidate Product v1.7.0 =
  corrected working candidate / non-authoritative

candidate Decisions v1.7.0 =
  corrected working candidate / non-authoritative

OPS-UPD-004 =
  CONFLICT_STOP

OPS-GAP-010 =
  OPEN / CONFLICT_STOP
```

DEC-055 remains current live authority until the governed v1.7 successor is lawfully promoted.

## 14.13 Promotion, compression and implementation remain blocked

The corrected candidate is materially healthier, but its existence and normal CI success do not authorise promotion.

Required remaining sequence:

```text
SHA-bound Foundation Integrity workflow_dispatch
  on exact bdb174e31259714081cfd9348f1b0175699b2059
→ exact-head assertion PASS
→ unit tests PASS
→ manifest-backed audit PASS
→ fresh independent hostile semantic review on the same SHA
→ clean review outcome
→ separate governed promotion / archive / README / manifest routing pass
→ resulting-main certification
→ close OPS-UPD-004 / OPS-GAP-010 if promotion evidence is clean
→ continue remaining serial upstream-disposition work
→ final convergence audit
→ compression
```

Accordingly:

```text
AUTHORITY PROMOTION = NOT AUTHORISED
PR MERGE = NOT AUTHORISED
IMPLEMENTATION = NOT AUTHORISED
OPS-UPD-001 = DO NOT START
COMPRESSION = NOT READY
```

## 14.14 v0.16.0 controlling working-state disposition

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0

USER PRODUCT ADJUDICATION: ACCEPTED
TDD RED: PASS
CORRECTED PRODUCT CANDIDATE MATERIALISED: PASS
CORRECTED DECISION CANDIDATE MATERIALISED: PASS
CORRECTION COMMIT: bdb174e31259714081cfd9348f1b0175699b2059
CORRECTION COMMIT DIFF BOUNDARY: PASS
CORRECTION COMMIT PATHS: 2
CORRECTION COMMIT TOTAL LINE CHANGES: 40

FOUNDATION INTEGRITY #295: PASS
RUN #295 EVENT: pull_request
RUN #295 UNIT TESTS: PASS
RUN #295 MANIFEST-BACKED FOUNDATION AUDIT: PASS
RUN #295 EXACT-HEAD ASSERTION: SKIPPED / EXPECTED FOR PR EVENT

IR-B04 SHA-BOUND CERTIFICATION: OPEN / BLOCKING
CONNECTED WORKFLOW_DISPATCH MUTATION: UNAVAILABLE
RERUN AS SUBSTITUTE: REJECTED

FRESH INDEPENDENT SEMANTIC REVIEW: REQUIRED
CURRENT AUTHORING PASS ELIGIBLE TO SELF-CERTIFY: NO

PR #90: OPEN / DRAFT / DO NOT MERGE
PR #90 HEAD: bdb174e31259714081cfd9348f1b0175699b2059
CURRENT MAIN: 086ade7b28c000de1c387acb9760e5eb08bb0413
CURRENT AUTHORITY ROUTING: v1.6 PRODUCT / v1.6 DECISIONS
OPS-UPD-004: CONFLICT_STOP
OPS-GAP-010: OPEN / CONFLICT_STOP

AUTHORITY PROMOTION: NOT AUTHORISED
IMPLEMENTATION: NOT AUTHORISED
OPS-UPD-001: DO NOT START
COMPRESSION: NOT READY

PASS OUTCOME FOR THIS MATERIALISATION PASS:
  CORRECTED CANDIDATE MATERIALISATION = PASS
  BOUNDED DIFF VERIFICATION = PASS
  ORDINARY PR CI = PASS
  SHA-BOUND CERTIFICATION = BLOCKED / STOP AT IR-B04
  INDEPENDENT SEMANTIC CERTIFICATION = PENDING AFTER IR-B04

NEXT SAFE ACTION:
  INVOKE FOUNDATION INTEGRITY VIA workflow_dispatch WITH:
    ref = bdb174e31259714081cfd9348f1b0175699b2059
  AND REQUIRE:
    Verify exact-head checkout = PASS
    Run unit tests = PASS
    Run manifest-backed foundation audit = PASS
    overall workflow = PASS

  THEN OBTAIN A FRESH INDEPENDENT HOSTILE SEMANTIC REVIEW
  FROM A REVIEWER WHO DID NOT AUTHOR OR MODIFY THIS CANDIDATE.
```

This append records a successful corrected-candidate materialisation and ordinary mechanical GREEN state without collapsing that evidence into authority promotion or independent semantic certification.


---

# 15. v0.17.0 — IR-B04 live revalidation; exact-SHA dispatch still absent; review gate remains closed

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.16.0 BYTES PRESERVED UNCHANGED**  
> **FORMAL PASS OUTCOME: BLOCKED / STOP**  
> **BLOCKER: IR-B04 SHA-BOUND FOUNDATION INTEGRITY DISPATCH**  
> **SEMANTIC CANDIDATE STATE: UNCHANGED FROM v0.16.0**  
> **PR #90: OPEN / DRAFT / DO NOT MERGE**  
> **CURRENT AUTHORITY: v1.6 PRODUCT / v1.6 DECISIONS**  
> **INDEPENDENT SEMANTIC REVIEW: NOT YET ELIGIBLE TO START**  
> **PROMOTION / IMPLEMENTATION / COMPRESSION: NOT AUTHORISED**

## 15.1 Maintenance and provenance

This successor preserves the complete v0.16.0 file byte-for-byte and appends only the live revalidation performed after the user accepted continuation.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.16.0.md

predecessor SHA-256 =
  13a49dd13fc94d71c6b16d28fc4c101209c94f91ca5a5ab57031c4962c1d6010

maintenance mode =
  append-only

artifact format =
  Markdown only

repository mutation in this pass =
  none
```

## 15.2 Live repository state reverified

```text
repository = JCSchoeman96/NewYou
main = 086ade7b28c000de1c387acb9760e5eb08bb0413

PR = #90
PR state = OPEN
PR draft = true
PR merged = false
PR head branch = authority/ops-upd-004-assessment-credit-v1.7.0
PR head SHA = bdb174e31259714081cfd9348f1b0175699b2059
PR base = main
PR base SHA = 086ade7b28c000de1c387acb9760e5eb08bb0413
```

The corrected candidate head has not changed since v0.16.0. No authority promotion occurred.

## 15.3 Exact-head workflow-run search

The live GitHub Actions run collection was queried by exact candidate head SHA.

```text
head SHA = bdb174e31259714081cfd9348f1b0175699b2059
total workflow runs found = 1
```

The only run remains:

```text
workflow = Foundation Integrity
run number = 295
run id = 38078038949
event = pull_request
status = completed
conclusion = success
```

No `workflow_dispatch` run exists for the corrected candidate head at this revalidation point.

Therefore:

```text
SHA-bound Foundation Integrity evidence = ABSENT
```

## 15.4 IR-B04 gate definition reverified at the corrected head

The live workflow at the corrected head still requires:

```text
workflow_dispatch:
  inputs:
    ref:
      required: true
      type: string
```

Its exact-head verification runs only when:

```text
github.event_name == 'workflow_dispatch'
```

and validates:

```text
input ref is a 40-character commit SHA
AND
GITHUB_SHA == input ref
AND
git rev-parse HEAD == input ref
```

The normal pull-request path does not execute that assertion.

Therefore:

```text
pull_request success
≠
SHA-bound exact-head certification
```

## 15.5 Connected GitHub capability rechecked

The connected GitHub tool surface was queried again for a dispatch action.

```text
workflow-dispatch mutation exposed = no
```

Rerun capabilities remain available, but a rerun preserves the original pull-request event and is not an acceptable substitute for the repository's SHA-bound gate.

No rerun or workflow mutation was performed.

## 15.6 Formal disposition

There is no new semantic defect and no new corrected-candidate head.

The remaining blocker is proof:

```text
IR-B04 = OPEN / BLOCKING
reason = required SHA-bound workflow_dispatch evidence does not exist
connected environment able to create required event = no
```

# BLOCKED / STOP

This is not a request to change Product or Decision semantics again, and it is not permission to weaken the proof gate.

## 15.7 Independent semantic review gate remains closed

The required fresh hostile semantic review must be bound to the same exact SHA that receives valid exact-head certification.

Required sequence:

```text
1. Run Foundation Integrity via workflow_dispatch.

2. Supply:
   ref = bdb174e31259714081cfd9348f1b0175699b2059

3. Require:
   Verify exact-head checkout = PASS
   Run unit tests = PASS
   Run manifest-backed foundation audit = PASS
   overall workflow = PASS

4. Reverify PR #90 head still equals:
   bdb174e31259714081cfd9348f1b0175699b2059

5. Only then obtain a fresh independent hostile semantic review
   from a reviewer who did not author or modify the candidate.

6. Only after a clean review may a separate governed
   promotion / archive / routing pass be considered.
```

Any head change invalidates previously bound certification/review.

## 15.8 Authority and workstream state remain unchanged

```text
current Product Law = 00_PLATFORM_v1.6.0.md
current Decision Register = 01_DECISIONS_v1.6.0.md

candidate Product v1.7.0 = working / non-authoritative
candidate Decisions v1.7.0 = working / non-authoritative

OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
OPS-UPD-001 = DO NOT START

PR #90 = DO NOT MERGE
authority promotion = NOT AUTHORISED
implementation = NOT AUTHORISED
compression = NOT READY
```

## 15.9 v0.17.0 controlling status

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0

PR #90: OPEN / DRAFT / DO NOT MERGE
PR #90 HEAD: bdb174e31259714081cfd9348f1b0175699b2059
CURRENT MAIN: 086ade7b28c000de1c387acb9760e5eb08bb0413

CORRECTED CANDIDATE HEAD CHANGED SINCE v0.16.0: NO
NEW EXACT-HEAD WORKFLOW RUN FOUND: NO

FOUNDATION INTEGRITY #295:
  event = pull_request
  result = PASS
  exact-head assertion = SKIPPED

LIVE WORKFLOW_DISPATCH CONTRACT:
  present = YES
  required input = exact 40-character ref
  exact-head verification = workflow_dispatch only

CONNECTED workflow_dispatch MUTATION:
  unavailable

IR-B04:
  OPEN / BLOCKING

FRESH INDEPENDENT SEMANTIC REVIEW:
  NOT YET ELIGIBLE TO START

FORMAL PASS OUTCOME:
  BLOCKED / STOP

AUTHORITY PROMOTION:
  NOT AUTHORISED

IMPLEMENTATION:
  NOT AUTHORISED

OPS-UPD-001:
  DO NOT START

COMPRESSION:
  NOT READY

NEXT SAFE ACTION:
  invoke Foundation Integrity through workflow_dispatch with:

  ref = bdb174e31259714081cfd9348f1b0175699b2059

  and require:
    Verify exact-head checkout = PASS
    Run unit tests = PASS
    Run manifest-backed foundation audit = PASS
    overall workflow = PASS

  then return to a fresh independent hostile reviewer on that same SHA.
```

No candidate, PR, authority, workflow or repository state was mutated during this revalidation pass.


---

# 16. v0.18.0 — IR-B04 second-path revalidation; no dispatch evidence and no independent PR review

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.17.0 BYTES PRESERVED UNCHANGED**  
> **FORMAL OUTCOME: BLOCKED / STOP**  
> **IR-B04: STILL OPEN / BLOCKING**  
> **SHA-BOUND FOUNDATION INTEGRITY DISPATCH: NOT FOUND**  
> **PR #90 FORMAL REVIEWS: NONE**  
> **PR #90: OPEN / DRAFT / DO NOT MERGE**  
> **CURRENT AUTHORITY: v1.6 PRODUCT / v1.6 DECISIONS**  
> **PROMOTION / IMPLEMENTATION / COMPRESSION: NOT AUTHORISED**

## 16.1 Maintenance and provenance

This successor preserves the complete v0.17.0 document byte-for-byte and appends only the additional live verification performed in this pass.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.17.0.md

predecessor SHA-256 =
  0524c4a9889360bfd265cfc5f984f1a0b11d0f8f50379e4944f03126db867d22

maintenance mode =
  append-only

artifact format =
  Markdown only

repository mutation in this pass =
  none
```

## 16.2 PR #90 exact live state

PR #90 was re-read from the live repository.

Verified:

```text
PR = #90
state = open
draft = true
merged = false

base = main
base SHA = 086ade7b28c000de1c387acb9760e5eb08bb0413

head branch = authority/ops-upd-004-assessment-credit-v1.7.0
head SHA = bdb174e31259714081cfd9348f1b0175699b2059

current branch head changed since v0.17.0 = no
```

The PR body still accurately records:

- the original `feaacff6...` candidate as `CHANGES REQUIRED`;
- the `c00aa9f0...` RED test-first head;
- the corrected `bdb174e3...` candidate head;
- Foundation Integrity #295 as ordinary PR-triggered mechanical success;
- `Verify exact-head checkout` as skipped for that PR event;
- the SHA-bound dispatch and independent review as remaining blockers;
- `DO NOT MERGE`.

No PR mutation was required in this pass.

## 16.3 Exact-head Actions lookup repeated

The repository's Actions run collection was queried again using:

```text
head_sha =
  bdb174e31259714081cfd9348f1b0175699b2059
```

Result:

```text
total matching workflow runs = 1
```

The only matching run is still:

```text
workflow = Foundation Integrity
run number = 295
run id = 38078038949
event = pull_request
status = completed
conclusion = success
```

No later `workflow_dispatch` run exists for the corrected head.

## 16.4 Repository-wide Actions lookup used as independent cross-check

A second lookup was performed against the repository-wide Actions run collection rather than only the exact-head scoped collection.

The newest Foundation Integrity run remains:

```text
run number = 295
head SHA = bdb174e31259714081cfd9348f1b0175699b2059
event = pull_request
conclusion = success
```

No more recent Foundation Integrity `workflow_dispatch` run appears ahead of #295 in the live repository run history.

This independently cross-checks the exact-head lookup.

Therefore:

```text
IR-B04 exact-SHA certification evidence =
  still absent
```

## 16.5 Formal PR review evidence checked

The live PR Reviews API was queried for PR #90.

Result:

```text
formal submitted reviews = 0
```

Therefore there is no GitHub-hosted independent semantic review evidence to evaluate in this pass.

This does not establish that no person has discussed the candidate elsewhere; it establishes only that no formal review is present on PR #90 in the canonical live repository.

## 16.6 Why semantic certification still cannot begin

The project sequence remains intentionally serial:

```text
exact corrected candidate
→ SHA-bound Foundation Integrity workflow_dispatch
→ exact-head verification PASS
→ unit tests PASS
→ manifest-backed foundation audit PASS
→ fresh independent hostile semantic review
→ only then governed promotion consideration
```

The required dispatch proof is still missing.

Even if an independent reviewer were available, starting formal certification before IR-B04 would break the agreed gate ordering and create review evidence against an uncertified proof state.

Therefore:

# BLOCKED / STOP

at IR-B04.

## 16.7 Connected capability remains insufficient for the blocking action

The connected GitHub surface was rechecked for a workflow-dispatch action.

Result:

```text
workflow_dispatch mutation exposed = no
```

Available rerun actions are not equivalent because a rerun preserves the original event class and would not execute the `workflow_dispatch`-only exact-head assertion.

No rerun was triggered.

No workflow file was modified.

No weaker substitute was accepted.

## 16.8 Current authority and serial-work state remain unchanged

```text
main =
  086ade7b28c000de1c387acb9760e5eb08bb0413

current Product Law =
  00_PLATFORM_v1.6.0.md

current Decision Register =
  01_DECISIONS_v1.6.0.md

candidate Product v1.7.0 =
  corrected working candidate / non-authoritative

candidate Decisions v1.7.0 =
  corrected working candidate / non-authoritative

OPS-UPD-004 =
  CONFLICT_STOP

OPS-GAP-010 =
  OPEN / CONFLICT_STOP

OPS-UPD-001 =
  DO NOT START

authority promotion =
  NOT AUTHORISED

implementation =
  NOT AUTHORISED

compression =
  NOT READY
```

## 16.9 v0.18.0 controlling state

```text
SEMANTIC PRESSURE TESTS ADDED: 0
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0

PR #90:
  OPEN / DRAFT / DO NOT MERGE

PR #90 HEAD:
  bdb174e31259714081cfd9348f1b0175699b2059

CURRENT MAIN:
  086ade7b28c000de1c387acb9760e5eb08bb0413

EXACT-HEAD ACTIONS LOOKUP:
  total runs = 1
  only run = Foundation Integrity #295
  event = pull_request
  result = success

REPOSITORY-WIDE ACTIONS CROSS-CHECK:
  no later dispatch evidence found

PR #90 FORMAL REVIEWS:
  0

IR-B04:
  OPEN / BLOCKING

CONNECTED workflow_dispatch MUTATION:
  unavailable

FORMAL OUTCOME:
  BLOCKED / STOP

NEXT SAFE ACTION:
  invoke Foundation Integrity via GitHub workflow_dispatch on the
  candidate branch with:

  ref = bdb174e31259714081cfd9348f1b0175699b2059

  require:
    Verify exact-head checkout = PASS
    Run unit tests = PASS
    Run manifest-backed foundation audit = PASS
    overall workflow = PASS

  then reverify the PR head is unchanged and obtain a fresh independent
  hostile semantic review from a reviewer who did not author or modify
  the corrected candidate.

PROMOTION:
  NOT AUTHORISED

IMPLEMENTATION:
  NOT AUTHORISED

OPS-UPD-001:
  DO NOT START

COMPRESSION:
  NOT READY
```

No repository mutation occurred during this pass.


---

# 17. v0.19.0 — Pre-JIT sequence reset + OPS-UPD-001 pilot admission/cap pressure-test pass

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.18.0 BYTES PRESERVED UNCHANGED**  
> **REPOSITORY / PR / ACTIONS GATES DEFERRED UNTIL AFTER PRE-JIT + INDEPENDENT REVIEW + COMPRESSION**  
> **SUBSTANTIVE PRE-JIT WORK RESUMED**  
> **OPS-UPD-001: WORKING CANDIDATE RESOLUTION CONVERGED FOR LATER INDEPENDENT REVIEW**  
> **NEW PRESSURE TESTS: OPS-PT-211...230**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **IMPLEMENTATION NOT AUTHORISED**

## 17.1 Maintenance and provenance

This successor preserves the complete v0.18.0 document byte-for-byte and appends only the revised work-sequencing instruction and the substantive OPS-UPD-001 Pre-JIT pressure-test pass.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.18.0.md

predecessor SHA-256 =
  763e296bfc8beb0b97381063a6d508b3873592c4ee10023b2bb68549109a6c44

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 17.2 User-directed sequence reset

The controlling work order is now:

```text
finish substantive Pre-JIT pressure testing in this Markdown artifact
→ complete all existing upstream-delta dispositions
→ perform final cross-delta / convergence audit
→ independent hostile review of the completed Pre-JIT artifact
→ correct any material review findings
→ compress the reviewed Pre-JIT evidence
→ only then add/promote repository artifacts and inspect CI/Actions/integration mechanics
```

Accordingly, the GitHub/PR/Actions material appended in v0.16.0...v0.18.0 remains historical evidence only. It does **not** block completion of the working Pre-JIT discovery artifact.

For substantive Pre-JIT status, the prior `IR-B04` workflow-dispatch gate is therefore **DEFERRED TO POST-COMPRESSION REPOSITORY INTEGRATION**. It is not treated as a current Pre-JIT stop.

This sequencing change does not make any working candidate authoritative and does not authorise implementation.

## 17.3 OPS-UPD-001 — source problem restatement

Existing Product/Roadmap law already establishes the intended first-pilot progression:

```text
internal/test validation
→ first 10 real participants / paid participants
→ review
→ expand toward 25
→ review
→ maximum 50 in first paid pilot
```

The first-pilot maximum is explicitly an **operating release boundary, not a database-capacity limit**. Expansion is evidence-gated and cannot occur merely because technical capacity exists.

Current law also requires cross-functional readiness, stage-expansion authority and immediate scoped safety/technical stop capability.

The unresolved OPS-UPD-001 question is narrower:

> **Exactly what constitutes pilot admission, what counts against the 10/25/50 ceiling, when capacity may be released, and which existing authority owns the participant-specific admission truth?**

Without that clarification, several materially different implementations could all claim compliance while exposing more real people than the intended first-pilot boundary.

## 17.4 Core semantic distinction — release ceiling is not reusable inventory

The central Pre-JIT conclusion is:

```text
first-pilot cap
≠ concurrent active-user count
≠ number of paid orders
≠ number of active entitlements
≠ number of completed plans
≠ database throughput limit
≠ endlessly reusable seat pool
```

The cap exists to bound **real external participant exposure during a governed release stage**.

Therefore a participant who has already crossed the governed admission boundary cannot later disappear from the historical first-pilot exposure count merely because they:

- refund;
- withdraw;
- stop using the product;
- have an entitlement revoked;
- are safety-paused;
- request deletion;
- fail to complete the journey; or
- receive a support/commercial remedy.

Otherwise the nominal “first 50” could silently become 60, 70 or more distinct real participants.

## 17.5 Working candidate model

### 17.5.1 Stage ceiling

The current authorised pilot-admission ceiling is a governed stage value:

```text
initial stage ceiling = 10

after required review/sign-off:
  ceiling may increase toward, but not beyond, 25

after next required review/sign-off:
  ceiling may increase toward, but not beyond, 50

first-pilot hard maximum = 50
```

“Toward 25” does not require an automatic jump from 10 to 25. A responsible release decision may choose a smaller next ceiling.

No stage transition is automatic.

### 17.5.2 Invitation / waitlist

A prospect who is merely:

- identified;
- invited;
- waitlisted; or
- shown public/pilot information

has **not** yet become a counted pilot participant.

These states cannot manufacture participant access.

### 17.5.3 Pre-admission capacity reservation

A bounded pre-admission reservation may exist where needed to prevent concurrent checkout/admission from exceeding the current stage ceiling.

It is conceptually:

```text
reserved_for_possible_admission
```

not:

```text
counted_real_participant
```

A reservation:

- temporarily consumes available admission capacity;
- is bound to one intended participant identity;
- cannot be duplicated by retries;
- may be released only while the person has **not** crossed the counted-admission boundary;
- must not become a generic ticketing/seat-inventory platform;
- has exact expiry/locking/storage mechanics deferred to JIT/proof.

### 17.5.4 Counted admission boundary

A real external person becomes a counted first-pilot participant when the platform durably establishes that participant's **pilot-qualified production access to the protected core pilot journey**.

For the normal paid path, this requires the lawful Commerce → Entitlements path to have reached current usable access; a pending/ambiguous provider event alone is not admission truth.

For an explicitly approved sponsored/complimentary/goodwill external pilot path, the corresponding governed external access grant can establish the same participant exposure even without a positive price.

Therefore:

```text
invitation / waitlist
  = not counted

pre-admission reservation
  = capacity held, not yet counted exposure

payment pending / ambiguous
  = not counted exposure; reservation remains protected until reconciled

pilot-qualified external production access durably established
  = counted exactly once
```

### 17.5.5 Monotonic first-pilot exposure count

Once counted:

```text
first_pilot_counted = true
```

is historically monotonic for the first-pilot cohort.

Refund, cancellation, inactivity, withdrawal, support remediation, safety pause, entitlement revocation or participant deletion does not mint a replacement place in the first-pilot exposure budget.

Privacy/deletion may change what identifying information may lawfully remain. It must not turn historical release exposure into reusable admission capacity. Exact deletion-safe representation remains part of the privacy/deletion workstream and is not invented here.

## 17.6 What counts as one participant

The first-pilot cap is participant-centric, not transaction-centric.

Working rule:

```text
one real external participant
→ at most one first-pilot counted admission
```

Consequences:

- two orders by the same participant do not consume two pilot places;
- assessment + plan + bundle combinations do not multiply the participant count;
- retry/duplicate entitlement processing does not multiply the count;
- a refunded participant remains historically counted after admission;
- a participant using an approved external complimentary/sponsored route still counts against the real-participant exposure cap;
- internal/test/staff-only accounts do not count where they remain genuinely internal/test and do not masquerade as external pilot participants;
- if purchaser and participant/recipient are distinct, the **real participant/recipient** is the relevant exposure identity, not merely the payer.

Known duplicate identities/accounts must not be deliberately used to bypass the cap. Exact duplicate-person detection and account-reconciliation mechanics remain Identity/JIT concerns.

## 17.7 Existing ownership — no Operations/Admin Domain

OPS-UPD-001 does **not** justify a new Operations, Pilot, Admission or Admin Domain.

The required truths decompose across existing owners:

### Commerce

Owns the commercial product/release lifecycle, saleability and payment truth.

It remains responsible for whether the pilot product/offer is currently saleable under the authorised release stage.

### Entitlements

Owns the participant-specific durable right to enter/use governed product capability.

The participant-specific pilot-admission/access right belongs here rather than in an operator queue or Analytics counter. A pre-admission reservation, if materialised, must converge into this same governed admission lineage rather than become a second capacity authority.

### Identity & Access

Owns canonical account/identity and authentication/role truth. It does not decide commercial pilot capacity.

### Audit & Evidence

Records release/go-no-go decision evidence and sensitive/operator action evidence. It does not own the admission or stage state being audited.

### Analytics

May project invited, reserved, admitted, paid, completed, refunded and withdrawn cohort metrics. Those projections never authorise the next admission.

### Operating UI / Support / Admin

May present and command authorised admission work, but **work is attention, not authority**. No queue, dashboard, spreadsheet or feature flag becomes pilot-cap truth.

## 17.8 Stage stop, rollback and re-entry

A safety or technical stop must immediately prevent new protected admissions where the stop applies.

It does **not** automatically mean:

- silently revoke all already-purchased participant rights;
- erase prior counted participants;
- reset the first-pilot count;
- open replacement places; or
- let one authority waive another authority's blocker.

Existing participant treatment follows the scope of the actual stop plus the owning Product/Safety/Commerce/Entitlement rules.

Re-entry or stage expansion requires the existing cross-functional decision authorities and evidence.

## 17.9 Concurrency and fail-closed invariants

The working Product-level invariants are:

```text
counted participants <= authorised stage ceiling

reserved-but-not-counted capacity
+ counted admissions still consuming first-pilot budget
<= authorised stage ceiling

one participant admission lineage = counted at most once

stale projections cannot authorise admission

failed/ambiguous capacity authority = no new admission
```

Exact database constraint/transaction/lock design remains JIT/Architectural Proof.

The simplest correct PostgreSQL-authoritative path is preferred. Redis, ETS, Cachex, GenServers or a generic scarce-inventory service are not justified by a first-pilot ceiling of 50.

## 17.10 OPS-PT-211...230

The candidate semantics were pressure-tested as follows.

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-211` | 9 counted participants; two operators concurrently attempt to reserve the final stage-10 place | At most one additional reservation/admission lineage succeeds; the other fails closed or remains waitlisted | PASS |
| `OPS-PT-212` | 10 participants already counted; operator tries to admit participant 11 before review | Admission denied regardless of technical headroom | PASS |
| `OPS-PT-213` | Stage-10 review passes but decision authorises only ceiling 15, not 25 | System may admit only through 15; “toward 25” is not automatic 25 | PASS |
| `OPS-PT-214` | Person is invited or waitlisted but never receives protected pilot access | Does not enter counted participant history | PASS |
| `OPS-PT-215` | Pre-admission reservation is created; checkout is abandoned before lawful access exists | Reservation may be released; no counted participant created | PASS |
| `OPS-PT-216` | Payment provider is pending/ambiguous while a place is reserved | Do not count admission from provider ambiguity and do not resell the protected reserved capacity until reconciliation resolves it | PASS |
| `OPS-PT-217` | Verified payment exists but entitlement/access consequence is delayed or failing | Preserve participant's reserved place while reconciling; do not oversubscribe and do not treat provider state alone as access truth | PASS |
| `OPS-PT-218` | External participant receives lawful pilot access, then later refunds | Participant remains in historical first-pilot exposure count; refund does not reopen a place | PASS |
| `OPS-PT-219` | External participant receives access, then voluntarily withdraws/inactivates | Count remains; no replacement capacity is minted | PASS |
| `OPS-PT-220` | External participant receives access, then Full Deletion is requested | Deletion/privacy rules apply, but first-pilot capacity cannot be silently replenished; exact deletion-safe evidence representation remains with privacy/deletion work | PASS |
| `OPS-PT-221` | Same participant purchases Assessment and Plan separately | Count once, not once per order/product | PASS |
| `OPS-PT-222` | Duplicate checkout/webhook/entitlement retries replay for the same participant | Admission lineage and count remain idempotent; no duplicate place consumption | PASS |
| `OPS-PT-223` | Real external participant receives approved sponsored/complimentary full-pilot access | Counts against exposure cap despite zero/discounted price | PASS |
| `OPS-PT-224` | Staff/internal test account exercises production-like path solely for validation | Does not consume real-participant cap if it remains genuinely internal/test and cannot be used as an external-participant bypass | PASS |
| `OPS-PT-225` | Purchaser and intended participant/recipient differ under a permitted future grant/gift route | Count the admitted real participant/recipient, not merely the payer | PASS |
| `OPS-PT-226` | Participant is safety-paused after admission | Historical count remains; Safety can restrict journey without freeing pilot capacity | PASS |
| `OPS-PT-227` | Stage is paused/rolled back at 18 counted participants | Stop new admissions immediately; preserve 18 historical exposures; existing rights change only under scoped owning rules | PASS |
| `OPS-PT-228` | Analytics dashboard lags and shows 9 while authoritative admissions already equal 10 | Dashboard cannot authorise participant 11; authoritative admission path fails closed | PASS |
| `OPS-PT-229` | Process/node restarts during concurrent reservation/admission | Durable authoritative state reconstructs the correct count/reservations; node-local memory cannot be cap authority | PASS |
| `OPS-PT-230` | Operator attempts to delete/revoke a counted admission solely to create room for another participant | Historical exposure remains counted; ordinary operator action cannot recycle the cap | PASS |

All 20 tests pass under the working candidate semantics.

This is an **authoring/pressure-test result**, not the later independent-review certification.

## 17.11 Candidate Product clarification for eventual compression

The smallest upstream Product clarification needed for OPS-UPD-001 is conceptually:

```text
The first paid-pilot limits are cumulative real-participant release-exposure ceilings,
not concurrent-user, order, entitlement or database-capacity limits.

The authorised admission ceiling begins at 10, may increase only after the
required review toward a ceiling no greater than 25, and may increase only
after the next required review toward a first-pilot ceiling no greater than 50.

Invitations and waitlist entries do not count as admissions. A bounded
pre-admission reservation may protect capacity before the participant is
lawfully admitted, but it may be released only before counted admission.

A real external participant becomes counted once pilot-qualified production
access to the protected core journey is durably established. Each participant
counts at most once. External sponsored/complimentary participants count where
they receive the same real pilot exposure; genuine internal/test accounts do not.

Once counted, the participant remains part of the first-pilot exposure count
even after refund, withdrawal, inactivity, safety pause, entitlement revocation
or deletion. Those later lifecycle events do not mint replacement capacity.

New admissions fail closed when the current authoritative stage ceiling or
admission state cannot be established. Expansion remains cross-functionally
governed and is never automatic.
```

No new DEC identifier is invented in this Pre-JIT artifact.

## 17.12 Architecture / Domain / operating consequences

### Architecture

No architecture amendment is currently justified. Existing doctrine already requires durable authority, contention-safe transitions, fail-closed protected behaviour and PostgreSQL-first correctness.

The exact atomic enforcement mechanism remains JIT/proof.

### Domain Map

No new Domain is justified.

Existing ownership can support the rule:

```text
Commerce
→ current pilot product/release saleability + payment truth

Entitlements
→ participant-specific pilot admission/access right and its idempotent lineage

Identity & Access
→ canonical identity/authentication

Audit & Evidence
→ release/admission decision evidence, not business authority

Analytics
→ derived cohort metrics only
```

If later JIT analysis demonstrates that the participant-specific admission right cannot be expressed cleanly inside existing Entitlements without shared-write ownership, that is a Domain-law stop at that time. Current evidence does not justify such a stop.

### Operating model

Operators require views/actions for:

- invite/waitlist;
- capacity-reserved but not yet admitted;
- counted participant;
- paused/withdrawn/refunded/deleted participant status as permitted;
- current authorised stage ceiling;
- pending stage-review evidence;
- stop/rollback state.

Those are projections/workflows over the owning truths, not a new Operations authority.

## 17.13 What remains deliberately JIT / later proof

This Pre-JIT pass does **not** choose:

- Resource/table names;
- exact admission/reservation state-machine representation;
- transaction/locking primitive;
- unique/index constraints;
- reservation expiry duration;
- operator UI component structure;
- queue/worker names;
- Redis/ETS/GenServer mechanisms;
- exact waitlist-selection policy;
- exact identity-duplicate detection algorithm;
- final deletion-safe historical evidence representation.

Those choices must implement the semantic invariants above rather than redefine them.

## 17.14 OPS-UPD-001 disposition

```text
OPS-UPD-001 =
  WORKING PRE-JIT CANDIDATE RESOLUTION CONVERGED

root issue =
  Product Law defines 10→25→50 release progression but does not fully define
  admission/count/release semantics under refunds, complimentary access,
  duplicate identities/orders, concurrency and rollback.

recommended authority level =
  Product Law clarification

new Domain required =
  NO

Architecture amendment required =
  NO, based on current evidence

new OPS-UPD =
  0

new OPS-GAP =
  0

independent review =
  DEFERRED UNTIL COMPLETE PRE-JIT ARTIFACT

compression =
  DEFERRED UNTIL AFTER INDEPENDENT REVIEW
```

## 17.15 Updated workstream state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 210
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 230
CONTIGUOUS PT COVERAGE = OPS-PT-001...230

OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = OPEN / NEXT SUBSTANTIVE PASS
OPS-UPD-003 = OPEN
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT; REPO PROMOTION DEFERRED
OPS-UPD-005 = OPEN
OPS-UPD-006 = OPEN
OPS-UPD-007 = OPEN

NEW OPS-UPD = 0
NEW OPS-GAP = 0

GITHUB / PR / ACTIONS = DEFERRED
INDEPENDENT REVIEW = AFTER ALL SUBSTANTIVE PRE-JIT CONVERGES
COMPRESSION = AFTER CLEAN INDEPENDENT REVIEW
IMPLEMENTATION = NOT AUTHORISED

NEXT SUBSTANTIVE PASS = OPS-UPD-002 — duplicate genuine collection / make-whole
```

This section supersedes earlier **working-sequence** statements that made repository/action proof a prerequisite to continuing Pre-JIT discovery. It does not rewrite or erase their historical evidence.


---

# 18. v0.20.0 — OPS-UPD-002 duplicate genuine collection / payer make-whole pressure-test pass

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.19.0 BYTES PRESERVED UNCHANGED**  
> **SUBSTANTIVE PRE-JIT PASS — REPOSITORY / PR / ACTIONS REMAIN DEFERRED**  
> **OPS-UPD-002: WORKING CANDIDATE RESOLUTION CONVERGED FOR LATER INDEPENDENT REVIEW**  
> **NEW PRESSURE TESTS: OPS-PT-231...250**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **IMPLEMENTATION NOT AUTHORISED**

## 18.1 Maintenance and provenance

This successor preserves the complete v0.19.0 file byte-for-byte and appends only the OPS-UPD-002 Pre-JIT analysis.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.19.0.md

predecessor SHA-256 =
  d3a949b574b8d5e0ade708cd2bc78286389fa4030eb89e49fa283392bcd4c2d3

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 18.2 Source-law position

The current working authority snapshots already establish several important invariants:

```text
Commerce owns:
  purchase/payment/refund/dispute/settlement reconciliation

Entitlements owns:
  access rights independently of payment truth

provider evidence:
  is evidence, not platform financial authority

duplicate provider delivery:
  must not duplicate payment effect

duplicate payment/job/callback execution:
  must not multiply access

paid-pilot integrity target:
  0 duplicate charges
  0 duplicate entitlements
```

Current Product refund wording also says:

```text
Assessment:
  ordinary refund ends after first answer except technical failure

Plan:
  ordinary refund ends after generation/delivery

Membership:
  no ordinary partial-period refund
  duplicate or erroneous billing is refundable
```

That wording leaves a material ambiguity for once-off products:

> If one assessment or plan purchase is genuinely collected twice, may the ordinary post-consumption refund cutoff be used to retain the second collection?

The answer required by payment integrity is **no**.

This is the OPS-UPD-002 gap.

## 18.3 Three cases that must remain distinct

### 18.3.1 Duplicate evidence only

Example:

```text
one real provider collection
→ webhook delivered three times
```

or:

```text
one payment
→ provider status polled/reported repeatedly
```

This is duplicate/reordered evidence.

It must reconcile to one Commerce payment effect.

It does **not** create a second customer refund obligation because no second economic collection occurred.

### 18.3.2 Genuine duplicate collection

Example:

```text
one intended purchase / one commercial obligation
→ payment attempt A actually collects
→ retry/replacement attempt B also actually collects
```

There are now two genuine collections for one valid commercial obligation.

Commercial truth is:

```text
one amount was owed
two amounts were collected
one amount is excess
```

The excess collection creates a make-whole obligation.

### 18.3.3 Two genuine intended purchases

Example:

```text
purchase intent A
→ product/recipient X
→ collected

purchase intent B
→ separately intended product/recipient Y
→ collected
```

Similarity of:

- payer;
- amount;
- product;
- timestamp; or
- provider

is not sufficient by itself to call one payment a duplicate.

Two genuinely intended purchases remain two purchases.

Ambiguous intent must reconcile before automatic refund or entitlement destruction.

## 18.4 Logical commercial obligation is the comparison boundary

The duplicate-collection question is evaluated against the **logical commercial obligation**, not merely against provider transaction IDs.

Conceptually:

```text
one intended governed purchase
→ one commercial amount due
→ one payment obligation
→ one governed entitlement consequence
```

A logical purchase may have multiple technical/provider attempts because of:

- retry;
- timeout;
- browser interruption;
- replacement checkout;
- provider ambiguity;
- callback loss;
- manual reconciliation.

Those attempts do not automatically become separate commercial obligations.

The exact schema/identifier for purchase/payment-attempt lineage remains JIT.

## 18.5 Working definition — genuine duplicate collection

A genuine duplicate collection exists when Commerce verifies that:

1. more money was successfully collected from a payer than the amount lawfully due for one logical commercial obligation;
2. the extra collection is not merely a duplicate callback/status event;
3. the extra collection is not a separately intended valid purchase; and
4. provider/settlement evidence is sufficient to treat the excess as real financial collection under the approved provider contract.

A pending authorisation, temporary card hold or ambiguous provider outcome is not silently promoted to a genuine collected payment.

It remains:

```text
pending / unresolved / reconciling
```

until provider-safe reconciliation establishes the economic outcome.

## 18.6 Make-whole principle

For one genuine commercial obligation:

```text
amount lawfully due = D
verified total genuine collection = C

where C > D:

excess collection = C - D
```

The payer must be restored for the **verified excess collection**.

Working rule:

```text
valid intended collection
  remains payment for the purchase

excess genuine collection(s)
  → reversal/refund/remediation obligation

entitlement consequence
  → exactly one valid governed right
```

If three genuine collections settle against one obligation, two are excess.

The make-whole obligation is not satisfied merely because:

- a refund was requested;
- a support ticket was closed;
- a provider API returned an ambiguous response;
- Analytics reflects an expected refund; or
- an operator manually labels the case resolved.

Completion requires authoritative Commerce reconciliation sufficient to establish that the excess obligation has been extinguished by the provider-supported reversal/refund path or other legally valid resolution.

Exact Paystack refund/reversal/settlement status mapping remains under the existing provider validation gate.

## 18.7 Duplicate-collection make-whole is independent of ordinary refund eligibility

This distinction is critical:

```text
ordinary product refund
≠
return of money never owed
```

Therefore:

### Assessment

If a participant has submitted the first answer or even received the full assessment deliverable:

```text
ordinary intended-charge refund eligibility
  follows assessment refund law

verified duplicate/excess collection
  must still be returned
```

### Plan

If the plan has already been generated or delivered:

```text
ordinary intended-charge refund eligibility
  follows plan refund law

verified duplicate/excess collection
  must still be returned
```

### Membership

Existing Product Law already states duplicate or erroneous billing is refundable. OPS-UPD-002 generalises the same payment-integrity principle across governed products rather than leaving once-off purchases exposed to a contradictory interpretation.

### Event / later products

Product-specific cancellation/refund rules continue to govern the valid intended purchase.

They cannot convert an excess collection into money lawfully owed.

## 18.8 Access consequences remain separate

A duplicate genuine collection must not create a duplicate entitlement.

Normal case:

```text
one logical purchase
+ two genuine collections
=
one valid entitlement
+ one valid intended payment
+ one excess-payment remediation obligation
```

Refunding/reversing the excess collection does **not** revoke the one valid entitlement.

The valid entitlement changes only if the **intended purchase itself** is separately refunded/cancelled/revoked under its own Product law.

If payment duplication also caused duplicate entitlement grants, there are two independent integrity defects:

```text
duplicate collection
→ Commerce remediation

duplicate entitlement
→ Entitlements correction
```

Entitlements must preserve the one valid purchased right and neutralise the unintended duplicate right where possible without rewriting legitimate historical consumption/evidence.

An accidental duplicate entitlement does not transform an unauthorised duplicate collection into an intended second sale.

Fraud/abuse evidence, if any, remains a separate governed question.

## 18.9 Payer / recipient separation

Purchaser, payer, recipient and participant remain separate concepts.

Where the payer bought access for another recipient:

```text
duplicate collection remediation
  belongs to payer/commercial payment relationship

one valid entitlement
  remains with the intended recipient
```

The payer is not granted recipient-private assessment, health, plan or usage information merely because a refund/reversal is being processed.

## 18.10 Reversal, refund, dispute and chargeback interaction

The platform must not make the payer whole twice.

Examples:

### Provider reversal before final settlement

If the provider successfully reverses the excess collection before settlement:

```text
excess economic obligation extinguished
→ no second cash refund
```

provided Commerce reconciliation confirms that outcome.

### Chargeback/dispute already credits the payer

If a bank/provider dispute has already returned the excess money:

```text
do not issue an additional duplicate refund
```

Reconcile the dispute/chargeback into Commerce truth first.

### Chargeback pending

A pending dispute is not final make-whole evidence.

The obligation remains open/reconciling until outcome is known.

### Duplicate refund request/retry

Refund/reversal execution itself must be idempotent.

Repeated jobs, operator clicks or callbacks must not reimburse more than the verified excess amount.

## 18.11 Make-whole amount and currency boundary

At minimum, the platform-level make-whole obligation is:

```text
return the verified excess platform collection
in the original governed transaction currency / provider-supported equivalent path
```

For the first launch this is ordinarily ZAR.

This Pre-JIT pass does **not** invent legal compensation rules for:

- card-issuer fees;
- foreign-card FX movement;
- bank fees;
- consequential loss;
- statutory interest; or
- damages.

Applicable consumer/statutory rights remain in force, and exact provider/legal handling of those secondary amounts belongs to the existing legal/provider validation boundary.

No support credit, coupon or goodwill entitlement silently substitutes for returning the excess collected money unless an independently lawful, explicit payer choice permits that treatment.

## 18.12 Full Deletion does not erase an unresolved commercial make-whole obligation

Participant data lifecycle and financial obligation lifecycle remain separate.

If Full Deletion is requested after a genuine duplicate collection is identified but before make-whole completes:

```text
eligible participant data
  follows Privacy & Consent deletion law

lawfully retained financial/remediation evidence
  remains only as required to complete/prove the financial obligation

participant access
  must not be resurrected from retained finance

payer make-whole obligation
  does not disappear merely because participant-facing data is deleted
```

The exact deletion-safe retained representation remains part of OPS-UPD-006 / legal-retention detail and is not invented here.

## 18.13 Pilot-integrity consequence

A genuine duplicate collection is a real `duplicate charge` for the paid-pilot integrity criterion.

Refunding it later does **not** rewrite history to:

```text
0 duplicate charges
```

for the affected evidence window.

Instead:

```text
duplicate charge occurs
→ integrity incident recorded
→ payer made whole
→ root cause corrected
→ relevant payment path re-proved
→ deliberate re-entry/repeat evidence decision
```

The historical incident remains visible.

A duplicate webhook with only one actual collection is not counted as a duplicate charge, although repeated evidence handling may still expose an idempotency/reconciliation defect.

If evidence indicates a systemic risk of further duplicate genuine collection, existing rollback authority supports the narrowest safe protection, including stopping new sales/checkout while preserving already-valid customer rights.

## 18.14 Ownership — no new Finance / Refund / Reconciliation Domain

OPS-UPD-002 does not justify a new Domain.

### Commerce

Authoritative owner of:

- purchase obligation;
- payment attempts;
- verified provider collection evidence;
- duplicate/excess collection classification;
- refund/reversal/dispute/chargeback reconciliation;
- make-whole obligation state.

### Entitlements

Authoritative owner of:

- the one valid purchased access right;
- correction of any duplicate entitlement effect;
- consumption/revocation history.

It does not decide whether money was genuinely collected twice.

### Audit & Evidence

Records material financial/operator/release evidence where required.

It does not own payment truth.

### Analytics

May report duplicate-charge incidents, refund latency, reconciliation status and related aggregates.

It cannot classify a payment as duplicate or authorise a refund.

### Finance / Support operating roles

Finance may work reconciliation/refund exceptions.

Support may communicate status and permitted remediation.

Neither role/screen/queue becomes business authority.

## 18.15 Failure, retry and concurrency invariants

The working Product-level invariants are:

```text
one logical commercial obligation
→ at most one amount lawfully retained

one logical governed purchase
→ at most one valid governed entitlement consequence

duplicate/reordered provider evidence
→ no duplicate payment effect

multiple genuine collections for one obligation
→ all excess collection becomes explicit remediation obligation

remediation retries
→ at most one net make-whole effect per excess collection

provider ambiguity
→ pending/reconcile, never guessed success

ordinary refund eligibility
→ does not cancel duplicate-collection remediation

refund/chargeback/reversal
→ reconcile before further irreversible reimbursement
```

Exact transaction boundaries, provider idempotency keys, unique constraints, worker structure and refund API calls remain JIT/proof.

## 18.16 OPS-PT-231...250

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-231` | Provider sends the same successful-payment webhook three times for one actual collection | One Commerce payment effect, one entitlement consequence, no duplicate-refund obligation | PASS |
| `OPS-PT-232` | Two distinct provider captures settle for one logical assessment purchase | One valid intended payment, one excess collection, one assessment entitlement, excess amount enters make-whole | PASS |
| `OPS-PT-233` | Three genuine collections settle against one logical plan purchase | Retain one lawful collection; remediate two excess collections; exactly one governed plan entitlement | PASS |
| `OPS-PT-234` | Same payer deliberately makes two separately authorised purchases for two recipients | Treat as two commercial obligations; no automatic duplicate refund merely because amount/product/timing are similar | PASS |
| `OPS-PT-235` | First checkout times out, user follows the safe retry/replacement path for the same logical purchase, and both provider attempts later settle | Reconcile as one obligation with one valid collection and one excess make-whole obligation | PASS |
| `OPS-PT-236` | A second card authorisation/hold appears but is not captured/settled | Keep unresolved/provider exception; do not invent a collected-payment refund or second entitlement | PASS |
| `OPS-PT-237` | Provider reverses the excess collection before settlement | Reconciled reversal may satisfy the excess obligation; do not issue an additional refund | PASS |
| `OPS-PT-238` | Assessment answer already submitted when duplicate genuine collection is discovered | Ordinary assessment refund cutoff does not protect the excess collection; refund/reverse excess while preserving the valid purchased assessment right | PASS |
| `OPS-PT-239` | Plan already generated/delivered when duplicate genuine collection is discovered | Ordinary plan refund cutoff does not protect the excess collection; return excess and preserve one valid plan purchase | PASS |
| `OPS-PT-240` | Membership billing collects the same period twice | Refund/reverse excess collection; preserve the one valid paid-period entitlement under ordinary membership law | PASS |
| `OPS-PT-241` | Duplicate collection also caused two entitlement grants | Commerce remediates excess money; Entitlements preserves one valid grant and corrects the unintended duplicate access effect | PASS |
| `OPS-PT-242` | Accidental duplicate entitlement was already partly/fully consumed before detection | Do not rewrite historical consumption; genuine excess collection remains a Commerce remediation obligation; any abuse question is separate | PASS |
| `OPS-PT-243` | Duplicate amount has already been credited through a completed chargeback | Reconcile chargeback and do not issue a second refund for the same excess collection | PASS |
| `OPS-PT-244` | Refund worker/operator action is submitted repeatedly | Business idempotency prevents reimbursement exceeding the verified excess amount | PASS |
| `OPS-PT-245` | Provider accepts refund request but final outcome is ambiguous | Keep remediation pending/reconciling; do not mark make-whole complete and do not blindly issue another refund | PASS |
| `OPS-PT-246` | Payer and recipient are different people | Refund/reverse the payer's excess collection; preserve recipient's one valid entitlement; do not expose recipient-private journey data | PASS |
| `OPS-PT-247` | Full Deletion is requested while duplicate-collection remediation is unresolved | Continue only lawfully required financial remediation evidence; complete make-whole without resurrecting participant access | PASS |
| `OPS-PT-248` | Analytics flags a likely duplicate but Commerce has only one verified collection | Analytics cannot create financial truth; investigate/reconcile before refund | PASS |
| `OPS-PT-249` | Duplicate genuine collection is found after a pilot review report was prepared | Historical integrity evidence is corrected; refund does not erase the duplicate-charge incident; re-entry/repeat evidence is deliberate | PASS |
| `OPS-PT-250` | Duplicate genuine collection affects an international card and issuer FX/fees differ on refund | Return the verified excess governed transaction amount; secondary FX/fee/statutory compensation remains legal/provider policy, not silently invented by Product implementation | PASS |

All 20 tests pass under the working candidate semantics.

This remains authoring/pressure-test evidence, not independent certification.

## 18.17 Smallest upstream clarification for eventual compression

### Product Law

A general duplicate/excess-collection rule should sit above product-specific ordinary refund cutoffs:

```text
Duplicate or excess genuine collection is a payment-integrity remediation,
not an ordinary product refund.

Where Commerce verifies that more money was collected than was lawfully due
for one logical commercial obligation, the platform retains only the valid
intended collection and must return every verified excess collection through
the approved reversal/refund path.

This rule applies regardless of whether the valid product has already crossed
its ordinary refund cutoff. The ordinary assessment, plan, membership, event
or other refund rules continue to govern only the valid intended purchase.

Duplicate provider evidence with only one genuine collection does not create
a refund. Separately intended purchases are not duplicates. Ambiguous cases
remain unresolved until reconciled.

Returning an excess collection does not revoke the one valid entitlement.
Any duplicate entitlement effect is corrected separately by Entitlements.
Refund, reversal, dispute and chargeback outcomes must reconcile so the payer
is neither under-remediated nor reimbursed twice.
```

### Decision Register

The eventual Decision clarification should make explicit that:

```text
DEC-045 ordinary product refund boundaries
do not authorise retention of duplicate/excess genuine collection.

Duplicate/excess collection remediation applies across governed products.
```

No new DEC number is invented here.

## 18.18 Architecture / Domain consequence

### Architecture

No new Architecture Law is currently justified.

Existing architecture already requires:

- provider evidence rather than provider authority;
- durable Commerce truth;
- reconciliation of ambiguous irreversible provider outcomes;
- business-scoped idempotency;
- duplicate/reordered/retried execution safety;
- durable async remediation where required;
- fail-closed financial truth.

OPS-UPD-002 therefore clarifies **Product commercial semantics**, while exact proof remains under the existing FP-002 / OQ-004 path.

### Domain Map

No Domain amendment is currently required.

Commerce already owns the complete payment/refund/dispute/settlement authority needed for this rule.

Entitlements already owns non-duplication of access.

A generic Refund, Finance, Reconciliation or Make-Whole Domain would create competing authority and is rejected.

## 18.19 Deliberately deferred to JIT / provider / legal validation

This pass does not decide:

- Paystack-specific refund/reversal API calls;
- exact provider statuses that prove capture, settlement, reversal or refund;
- provider idempotency-key format;
- database table/Resource names;
- exact reconciliation job topology;
- refund SLA;
- bank/card posting latency;
- statutory compensation amounts;
- card-issuer fee reimbursement;
- foreign-exchange loss treatment;
- accounting journal implementation;
- chargeback-fee allocation;
- manual Finance approval thresholds.

Those details may refine execution but cannot weaken the Product-level rule that excess genuine collection is not money the platform may retain.

## 18.20 OPS-UPD-002 disposition

```text
OPS-UPD-002 =
  WORKING PRE-JIT CANDIDATE RESOLUTION CONVERGED

root issue =
  current law prevents duplicate effects and explicitly refunds duplicate
  membership billing, but does not clearly state that a genuine excess
  collection on a once-off assessment/plan is independent of the ordinary
  post-consumption refund cutoff.

recommended authority level =
  Product Law + bounded Decision Register clarification

new Domain required =
  NO

Architecture amendment required =
  NO, based on current evidence

existing provider gate reused =
  OQ-004

new OPS-UPD =
  0

new OPS-GAP =
  0

independent review =
  DEFERRED UNTIL COMPLETE PRE-JIT ARTIFACT

compression =
  DEFERRED UNTIL AFTER INDEPENDENT REVIEW
```

## 18.21 Updated workstream state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 230
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 250
CONTIGUOUS PT COVERAGE = OPS-PT-001...250

OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = OPEN / NEXT SUBSTANTIVE PASS
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT; REPO PROMOTION DEFERRED
OPS-UPD-005 = OPEN
OPS-UPD-006 = OPEN
OPS-UPD-007 = OPEN

NEW OPS-UPD = 0
NEW OPS-GAP = 0

GITHUB / PR / ACTIONS = DEFERRED
INDEPENDENT REVIEW = AFTER ALL SUBSTANTIVE PRE-JIT CONVERGES
COMPRESSION = AFTER CLEAN INDEPENDENT REVIEW
IMPLEMENTATION = NOT AUTHORISED

NEXT SUBSTANTIVE PASS =
  OPS-UPD-003 — consequential human-command authority / principally FP-006 operations policy
```


---

# 19. v0.21.0 — OPS-UPD-003 consequential human-command authority pressure-test pass

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.20.0 BYTES PRESERVED UNCHANGED**  
> **SUBSTANTIVE PRE-JIT PASS — REPOSITORY / PR / ACTIONS REMAIN DEFERRED**  
> **OPS-UPD-003: WORKING CANDIDATE RESOLUTION CONVERGED FOR LATER INDEPENDENT REVIEW**  
> **PRIMARY HOME: FP-006 OPERATING POLICY / PLATFORM OPERATING MODEL, WITH DOMAIN-SPECIFIC JIT ENFORCEMENT**  
> **NEW PRESSURE TESTS: OPS-PT-251...270**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **IMPLEMENTATION NOT AUTHORISED**

## 19.1 Maintenance and provenance

This successor preserves the complete v0.20.0 file byte-for-byte and appends only the OPS-UPD-003 Pre-JIT analysis.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.20.0.md

predecessor SHA-256 =
  05bcd58a0e72277c7362c8cb256d469d2f1f76983b006342c2e6e2c90e071164

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 19.2 Source-law position

The existing authority already establishes the essential boundaries:

```text
Platform Operating Model:
  work is attention, not authority
  queue visibility never grants business-action authority
  cross-domain action invokes the owning Domain
  sensitive/high-risk operations use explicit policy,
    current authority and durable evidence
  self-approval exists only where policy permits
  separation of duties applies where governing law requires it
  bulk action is permitted only where each selected item still passes
    its own policy/invariants

Product Law:
  staff roles are explicit/scoped
  sensitive actions require elevated authentication and tightly scoped access
  Super Admin is not an everyday unrestricted role
  Support goodwill authority may be tightly capped
  high-value / long-duration / lifetime grants require elevated
    commercial approval
  one authority may not waive another authority's blocker
  designated clinical/safety authority may stop unsafe behaviour
  technical/operations authority may disable a failing capability
  release/rollback decisions record evidence and re-entry criteria

Architecture:
  authorisation = role/capability
                + relationship
                + purpose
                + scope
                + expiry
                + current authoritative state
  there is no universal Super Admin bypass
  cross-boundary writes invoke the owning Domain
  authoritative action re-checks current server authority
  durable consequences preserve human/business causation separately
    from system execution authority
  retries/duplicates cannot multiply durable effects
```

The unresolved problem is not whether operators need controls.

They do.

The unresolved problem is:

> **What uniform rule determines when a human operator command may cause a durable or externally consequential business effect, without turning staff roles, queues, dashboards or Super Admin into a second write authority?**

That is OPS-UPD-003.

## 19.3 Working definition — consequential human command

A **consequential human command** is an authenticated human intent which, if accepted, directly establishes or causes a material durable or externally consequential effect such as:

- money movement or refund/reversal intent;
- entitlement grant/revoke/expiry/correction;
- account/role/security authority change;
- consent/export/deletion lifecycle transition;
- safety pause, clearance or governed override;
- plan correction/withdrawal/replacement;
- governed content correction/withdrawal/publication where material;
- privileged access / break-glass elevation;
- product/release stop, rollback, re-entry or stage expansion;
- another Domain-owned business transition whose effect survives the current UI interaction.

The following are **not automatically consequential business commands** merely because an operator clicks them:

- open/view a case;
- claim/assign work;
- add an internal note;
- filter/sort/search;
- acknowledge a notification;
- navigate a timeline;
- mark local presentation state;
- preview/simulate an outcome without mutation.

A work-queue action and a business command may be initiated from the same screen, but they are not the same authority.

## 19.4 Role label is not command authority

The staff labels:

```text
Support
Finance
Super Admin
Content
Moderator
Data Analyst
Event Admin
Developer
```

classify operators.

They do not, by themselves, mean:

```text
Support can change any participant record
Finance can issue any refund
Developer can repair business state directly
Content can clear safety restrictions
Super Admin can bypass every Domain policy
```

A consequential command is permitted only when the actor's **current** authority satisfies the owning action's policy.

Conceptually:

```text
authenticated actor
+ current authentication assurance
+ explicit role/capability
+ required relationship
+ allowed purpose
+ target scope
+ unexpired authority
+ required approval(s), where applicable
+ current owning-Domain state/invariants
=
command may be accepted
```

Missing any required component means the command is rejected or held for the required approval.

## 19.5 The owning Domain remains the mutation boundary

The operating surface may offer a convenient command.

It must not become a generic business-write API.

Examples:

```text
Support workspace
→ may request permitted Entitlements grant
→ Entitlements decides/commits grant

Finance workspace
→ may request permitted refund/remediation
→ Commerce decides/commits commercial transition

Safety work
→ authorised clinical/safety actor requests pause/clear/override
→ Safety & Eligibility decides/commits safety transition

Privacy work
→ permitted actor initiates governed deletion/export step
→ Privacy & Consent owns lifecycle/orchestration

Plan operations
→ permitted actor requests correction/withdrawal/replacement
→ Plans & Nutrition owns plan transition

Release control
→ named authority records stop/rollback/re-entry decision
→ affected owners enforce their own resulting transitions
```

No operator screen directly edits another Domain's persistence to “make the state match.”

## 19.6 Current authority is checked at execution, not screen load

Seeing a button is not proof of current authority.

Long-lived operator views may become stale because:

- role/capability is revoked;
- relationship expires;
- participant consent changes;
- case ownership changes;
- a refund already completed;
- entitlement already changed;
- safety state changed;
- release mode changed;
- another operator acted first.

Therefore every consequential command must re-evaluate its current authoritative guards when executed.

A stale page may produce:

```text
rejected
conflict
already_satisfied / idempotent convergence
requires fresh approval
requires attention
```

according to the owning workflow.

It must not convert stale visibility into mutation authority.

## 19.7 Authentication assurance and step-up

Ordinary authenticated staff access is not sufficient for every consequential command.

Where the risk requires it, the command policy may require stronger current assurance, including MFA/step-up.

The exact step-up mechanism and timeout remain downstream authentication/JIT detail.

The invariant is:

```text
high-risk command
→ appropriate current assurance before authoritative acceptance
```

not:

```text
actor logged in once
→ actor may perform every later sensitive action indefinitely
```

Emergency containment must remain possible through the approved emergency authority path; security controls must not be designed so poorly that the only way to stop harm is an unaudited bypass.

## 19.8 Approval and separation of duties

Not every consequential command requires a second approver.

Requiring universal dual approval would add bureaucracy not justified by current law.

Instead:

```text
low-risk / explicitly delegated command
  may be single-actor where policy allows

command whose law/policy requires approval
  must have the required independent/current approval

high-value / long-duration / lifetime commercial grant
  requires elevated commercial approval

cross-functional release expansion
  requires the existing separate authorities

clinical/safety blocker
  cannot be waived by commercial/technical authority

security/privacy blocker
  cannot be waived by commercial authority
```

Where separation of duties is required, one identity holding several roles does not automatically satisfy both sides of the approval.

The policy must evaluate whether the required approval is genuinely independent for that action.

Exact approval thresholds that are not already frozen remain FP/JIT operating policy; they are not invented here.

## 19.9 Human causation and system execution remain distinct

For a consequential human command, durable evidence must preserve enough causation to answer:

- who initiated it;
- under which current authority/capability;
- what command was requested;
- which governed target/scope was affected;
- why, where a reason is required;
- which approval(s) authorised it, where required;
- what authoritative outcome occurred;
- what later durable consequence/reconciliation remains pending;
- what superseding/reversal action occurred, if later corrected.

A background worker executing an already-authorised durable consequence is a **system executor**, not the human decision-maker.

Conceptually:

```text
human/business causation
≠
system execution identity
```

This prevents later audit from falsely attributing an automated retry to the worker as though it independently decided to refund, revoke, delete or withdraw.

Evidence remains minimised; it does not duplicate sensitive payloads unnecessarily.

## 19.10 Accepted command is not always completed consequence

Some commands complete inside the owning authoritative transition.

Others create a must-not-lose durable consequence.

Examples may include:

- provider refund execution;
- deletion fan-out;
- notification of a material correction;
- external processor deletion;
- asset invalidation;
- other provider reconciliation.

Therefore the operator experience must distinguish:

```text
command rejected
command authoritatively accepted
required consequence pending
consequence completed
terminal failure / requires attention
```

without requiring those exact labels as a universal business lifecycle.

Closing a support/work item must never fabricate that the underlying refund, deletion, withdrawal or other business outcome completed.

The owning Domain outcome remains truth.

## 19.11 Duplicate clicks, retries and concurrent operators

Every consequential command whose repeated execution could multiply effects requires a stable business-level operation identity or equivalent invariant.

Consequences:

- double-clicking “refund” cannot double-refund;
- two operators granting the same goodwill entitlement cannot multiply the right;
- repeated revoke/withdraw commands converge safely;
- duplicate release-stop commands do not create contradictory release truth;
- a retry after timeout re-reads authoritative state before deciding whether anything remains to do.

UI submit disabling is useful ergonomics, not the idempotency boundary.

## 19.12 Bulk commands

Bulk operator convenience may exist only where each selected target still passes its own current policy and invariants.

Bulk selection does not create collective authority.

A command must not say:

```text
actor may change item A
therefore actor may change A...Z
```

Exact batch atomicity and partial-failure UX remain JIT.

The semantic invariant is:

```text
every durable per-target effect
must itself be authorised and valid
```

An unauthorised/stale target may not slip through because it was part of an otherwise valid batch.

## 19.13 Emergency stop versus ordinary mutation

Emergency containment is deliberately asymmetric.

### Clinical/safety stop

A designated authorised clinical/safety owner may immediately stop or pause unsafe behaviour within that authority.

They do not thereby gain:

- commercial refund authority;
- identity administration authority;
- privacy-law authority;
- technical release authority outside the stop's scope.

### Technical/operations containment

A technical/operations owner may immediately disable a failing capability to protect payment, entitlement, security, privacy or data integrity.

They do not thereby gain authority to:

- declare a clinical case safe;
- alter payment truth;
- create entitlements;
- erase participant history;
- waive a Product blocker.

### Re-entry

The ability to stop does not imply unilateral authority to re-open.

Re-entry must evaluate the recorded remediation/re-entry criteria and every still-applicable specialist blocker.

The original stopper may participate in re-entry only within their actual authority.

## 19.14 Break-glass / Super Admin

Super Admin is not the answer to an awkward permission model.

Ordinary Super Admin access does not bypass:

- clinical authority;
- commercial approval;
- consent;
- participant relationship/scope;
- entitlement invariants;
- deletion law;
- release-sign-off requirements.

A true break-glass path, if required by the affected action, remains:

```text
exceptional
strongly authenticated
reasoned
scoped
time-bounded where appropriate
durably evidenced
alerted/reviewed
```

Break-glass may provide exceptional technical/privileged access.

It does not manufacture specialist business authority that the person does not hold.

## 19.15 Impersonation boundary

Routine impersonation remains prohibited.

Safe preview/simulation is preferred and does not mutate participant business truth.

A staff member must not impersonate a participant simply to bypass operator-command policies.

Any future true impersonation mechanism requires its own governed design and audit and cannot be presumed by FP-006.

## 19.16 Corrective commands do not rewrite history

Where the owning Domain preserves immutable/versioned or superseding history, an operator correction must use that owner's correction model.

Examples:

```text
wrong delivered plan
→ governed replacement/supersession
not silent destructive rewrite

wrong published governed content
→ correction/supersession/withdrawal
not history erasure

incorrect audit evidence
→ superseding evidence where permitted
not editing history

commercial remediation
→ explicit refund/reversal/reconciliation
not overwriting the original collection
```

The operator action is a command to the owner, not permission to mutate historical rows directly.

## 19.17 FP-006 command-policy requirement

OPS-UPD-003 should primarily be compressed into the FP-006 operating contract / Platform Operating Model.

Before the first real paid participant, FP-006 must identify the **actual consequential command families required by the core journey** and, for each family, define enough policy to avoid routine invention:

```text
command purpose
owning Domain
who may initiate / under which capability
required current scope/relationship
authentication assurance
approval / separation-of-duty requirement, if any
reason/evidence requirement, if any
authoritative guard / fail-closed condition
idempotency/retry expectation
business outcome versus pending consequence
reversal/correction path
audit/evidence expectation
```

This is a contract section, not a new universal Task Resource and not a new governance artifact type.

Exact Ash action names, schemas, UI placement and permission implementation remain JIT.

## 19.18 Core FP-006 command families that must be covered

The first paid-pilot operating policy should cover only command families actually needed for FP-001...FP-006, including as applicable:

1. **Identity/support**
   - ordinary governed account-access/recovery assistance;
   - staff role/privilege actions only through Identity authority;
   - no routine impersonation.

2. **Commerce**
   - refund/remediation command;
   - provider reconciliation exception handling;
   - sale/product pause where authorised.

3. **Entitlements**
   - permitted correction/reconciliation;
   - tightly capped goodwill/support grant where Product Law permits;
   - revocation/expiry only under owning policy.

4. **Safety & Eligibility**
   - immediate safety stop/pause;
   - governed clearance/override only by authorised clinical/safety actor.

5. **Plans & Nutrition**
   - correction/withdrawal/replacement under current safety and plan law.

6. **Content & Media**
   - material correction/withdrawal required by the core paid journey.

7. **Privacy & Consent**
   - participant export/deletion support/orchestration actions under current privacy authority;
   - legal hold remains specialist-governed.

8. **Release / platform operation**
   - stop new sales;
   - stop new plan generation;
   - disable a failing product/capability;
   - limited/read-only/maintenance containment;
   - staged release decision and re-entry evidence.

The list is deliberately bounded to the first-paid operating need.

It does not pull Membership, community moderation, practitioner-service, event-commerce or future-product command catalogues into FP-006.

## 19.19 Ownership — no Operations/Admin authority

No new Operations, Admin, Support or Command Domain is justified.

The authority model remains:

```text
Identity & Access
→ human/system identity, role/capability grants, assurance,
  privileged/break-glass authority context

owning business Domain
→ permission for and authoritative execution of its business mutation

Audit & Evidence
→ immutable/minimised evidence for sensitive actions,
  privileged access, incidents and release decisions

Operating UI / Work projection
→ discovery, attention, workflow, command presentation

Oban / workers
→ execution machinery for durable consequences,
  never independent business decision-maker
```

The same operator screen may compose several owners for usability.

It does not gain shared-write ownership.

## 19.20 OPS-PT-251...270

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-251` | Support can see a participant entitlement case but lacks the required grant/revoke capability | Case visibility does not authorise mutation; owning Entitlements action rejects the command | PASS |
| `OPS-PT-252` | Support issues a goodwill grant within the explicitly delegated capped policy | Allowed only through Entitlements with current scope, reason/evidence and idempotent grant semantics; no generic admin write | PASS |
| `OPS-PT-253` | Support attempts a high-value, long-duration or lifetime grant without elevated commercial approval | Command is blocked/held for required approval; Support cap cannot be stretched by role convenience | PASS |
| `OPS-PT-254` | Finance opens a refund case, but a chargeback settles before Finance clicks refund | Commerce re-reads current payment/remediation truth and prevents duplicate reimbursement | PASS |
| `OPS-PT-255` | Developer sees corrupted entitlement projection and directly edits persistence to “repair” it | Rejected as an operating pattern; correction must invoke Entitlements' governed repair/reconciliation path | PASS |
| `OPS-PT-256` | Ordinary Super Admin session attempts a clinical safety override | Super Admin label is insufficient; command requires actual scoped clinical/safety authority and appropriate assurance/evidence | PASS |
| `OPS-PT-257` | Authorised clinical/safety owner sees an immediate unsafe condition | Narrow safety stop may execute immediately; it does not grant unrelated commercial/technical authority | PASS |
| `OPS-PT-258` | Technical/operations owner disables plan generation because current integrity cannot be trusted | Narrow technical containment is allowed; technical actor cannot declare participants clinically safe or mutate Safety truth | PASS |
| `OPS-PT-259` | Operator opens a work item while authorised, then the relevant role/relationship is revoked before submit | Current authority is re-evaluated at command execution; stale UI does not preserve mutation permission | PASS |
| `OPS-PT-260` | Two operators concurrently submit the same entitlement correction/refund command | Business idempotency/invariants converge to one valid durable effect | PASS |
| `OPS-PT-261` | Bulk goodwill operation contains nine permitted grants and one item outside the actor's scope/cap | Every target requires its own valid policy evaluation; invalid item cannot inherit authority from the batch | PASS |
| `OPS-PT-262` | A sensitive command requires independent approval and the initiator attempts to approve it using another role held by the same identity | Reject unless the governing policy explicitly permits self-approval; multiple role labels do not defeat separation of duties | PASS |
| `OPS-PT-263` | Required approval was recorded, but the participant/domain state materially changes before command execution | Owning Domain revalidates current guards; stale approval is not an unconditional mutation token | PASS |
| `OPS-PT-264` | Support marks work “resolved” while provider refund/deletion consequence is still pending or has failed | Work projection cannot fabricate business completion; authoritative pending/failure remains visible/owned | PASS |
| `OPS-PT-265` | A human command was validly accepted and committed, then the operator's role is revoked while a durable consequence is executing | Human causation remains the accepted command; worker revalidates owning business preconditions. Later role revocation cancels execution only where current policy makes continuing actor authority a required precondition | PASS |
| `OPS-PT-266` | Support assists with a Full Deletion request and tries to directly delete records across Domains | Support may initiate only the permitted Privacy & Consent path; Privacy owns orchestration and each Domain applies its deletion contract | PASS |
| `OPS-PT-267` | Content operator withdraws incorrect plan-related copy and then tries to clear a safety restriction | Content command may affect Content truth only; Safety restriction requires Safety authority | PASS |
| `OPS-PT-268` | The actor who issued an emergency stop later attempts unilateral re-entry while another specialist blocker remains | Re-entry denied until recorded criteria and all applicable authorities are satisfied; stop authority is not blanket reopen authority | PASS |
| `OPS-PT-269` | Support uses participant impersonation to perform an action that Support cannot perform directly | Prohibited; simulation/preview cannot mutate truth and impersonation cannot be an authority bypass | PASS |
| `OPS-PT-270` | Generic telemetry/audit export is degraded during an immediate safety stop | Safety containment must not depend on non-authoritative telemetry; the owning transition must still preserve required durable causation/evidence or mandatory evidence intent. Ordinary high-risk commands fail closed if their required durable evidence cannot be established | PASS |

All 20 tests pass under the working candidate semantics.

This remains authoring/pressure-test evidence, not independent certification.

## 19.21 Smallest eventual clarification

The candidate operating rule for later compression is:

```text
A human-facing operator control does not itself grant business authority.

Every consequential human command must invoke the authoritative owning Domain
and be authorised from current server state using the actor's applicable
capability, relationship, purpose, scope, expiry, authentication assurance
and required approval(s). Queue visibility, staff role labels, stale UI state,
Analytics, audit views and Super Admin status do not bypass owning policy.

Sensitive/high-risk commands require the assurance, reason, approval and
durable evidence appropriate to their risk. Separation of duties applies only
where the governing policy requires it; low-risk explicitly delegated actions
must not acquire unnecessary approval bureaucracy.

Consequential commands are repeat-safe. Duplicate clicks, retries, reordered
execution and concurrent operators must not multiply refunds, grants,
revocations, withdrawals, release transitions or other durable effects.

Human/business causation is preserved separately from system execution.
Asynchronous consequences re-read the current owning-Domain preconditions and
remain visibly pending/failed until their actual completion contract is met.

Emergency safety or technical containment may execute immediately under its
named authority, but grants no unrelated business authority. Re-entry requires
the recorded remediation/re-entry criteria and all still-applicable specialist
authority.

Operating screens and work queues remain projections and command surfaces.
They never become a second business-write API.
```

## 19.22 Authority-level disposition

### Product Law

No Product Law amendment is currently required for OPS-UPD-003.

Existing Product Law already establishes:

- scoped staff roles;
- sensitive-action assurance;
- bounded Support goodwill;
- elevated commercial approval where required;
- specialist/non-waivable release authority;
- immediate safety/technical stop authority;
- no unrestricted everyday Super Admin model.

### Architecture Law

No Architecture amendment is required.

Existing Architecture already establishes:

- current authorisation composition;
- no universal Super Admin bypass;
- owning-Domain write boundary;
- current-state reauthorisation;
- business idempotency;
- durable async/revalidation;
- human causation versus system execution;
- audit/privileged-access doctrine.

### Domain Law

No Domain Map amendment is required.

Existing owners already own the relevant truths.

### Operating authority / FP-006

This is the principal correction surface.

The final FP-006 operating/JIT contract must make the consequential-command doctrine explicit and instantiate only the command families needed to operate the first paid core journey.

No new governance artifact type is required.

## 19.23 Deliberately deferred to FP-006 JIT / implementation proof

This pass does not decide:

- exact Ash action names;
- exact role/capability identifiers;
- exact permission-policy code;
- exact goodwill/refund approval thresholds not already frozen;
- exact MFA/step-up mechanism or timeout;
- exact reason-code taxonomy;
- exact approval UI;
- exact bulk-transaction semantics;
- exact audit-event schema;
- exact break-glass duration;
- exact command idempotency-key representation;
- exact worker/queue names;
- exact case/work projection states beyond existing operating vocabulary;
- a universal command ledger or universal Task Resource.

Those details must implement the doctrine above without creating a second authority layer.

## 19.24 OPS-UPD-003 disposition

```text
OPS-UPD-003 =
  WORKING PRE-JIT CANDIDATE RESOLUTION CONVERGED

root issue =
  Product/Architecture/Domain law already protects authority boundaries,
  but the first-paid operating contract needs an explicit uniform rule for
  when human operator commands may cause durable or externally consequential
  effects.

principal authority surface =
  Platform Operating Model / FP-006 operating policy

Product Law amendment required =
  NO, based on current evidence

Architecture amendment required =
  NO

Domain Map amendment required =
  NO

new Operations/Admin Domain required =
  NO

new governance artifact type required =
  NO

new OPS-UPD =
  0

new OPS-GAP =
  0

independent review =
  DEFERRED UNTIL COMPLETE PRE-JIT ARTIFACT

compression =
  DEFERRED UNTIL AFTER INDEPENDENT REVIEW
```

## 19.25 Updated workstream state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 250
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 270
CONTIGUOUS PT COVERAGE = OPS-PT-001...270

OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT; REPO PROMOTION DEFERRED
OPS-UPD-005 = OPEN / NEXT SUBSTANTIVE PASS
OPS-UPD-006 = OPEN
OPS-UPD-007 = OPEN

NEW OPS-UPD = 0
NEW OPS-GAP = 0

GITHUB / PR / ACTIONS = DEFERRED
INDEPENDENT REVIEW = AFTER ALL SUBSTANTIVE PRE-JIT CONVERGES
COMPRESSION = AFTER CLEAN INDEPENDENT REVIEW
IMPLEMENTATION = NOT AUTHORISED

NEXT SUBSTANTIVE PASS =
  OPS-UPD-005 — pre-first-fulfilment Plan change-of-intent
```


---

# 20. v0.22.0 — OPS-UPD-005 pre-first-fulfilment Plan change-of-intent pressure-test pass

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.21.0 BYTES PRESERVED UNCHANGED**  
> **SUBSTANTIVE PRE-JIT PASS — REPOSITORY / PR / ACTIONS REMAIN DEFERRED**  
> **OPS-UPD-005: WORKING CANDIDATE RESOLUTION CONVERGED FOR LATER INDEPENDENT REVIEW**  
> **NEW PRESSURE TESTS: OPS-PT-271...290**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **IMPLEMENTATION NOT AUTHORISED**

## 20.1 Maintenance and provenance

This successor preserves the complete v0.21.0 file byte-for-byte and appends only the OPS-UPD-005 Pre-JIT analysis.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.21.0.md

predecessor SHA-256 =
  ae6adbcc144b762da946fa0cebb6758f936fd21a90cc71391207fc6fbf03f221

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 20.2 Source-law position

Current Product / Decision / Roadmap law already establishes all of the following:

```text
plan onboarding
→ collects desired outcome, safety-relevant health facts,
  meal-frequency preferences and other generation inputs

initial automated plan pathways
→ health_foundation
→ weight_reduction
→ weight_maintenance

generated plan
→ immutable input / eligibility / temperament / protocol /
  content / generation-reason snapshot

generation failure
→ fail closed
→ no partial plan
→ entitlement remains available until successful delivery
→ retries safe and idempotent
→ duplicate plans prohibited

once-off plan
→ permanent access to the delivered plan
→ corrections and safety replacements included

post-delivery preference/progress re-personalisation
→ requires new purchase or qualifying membership/add-on

ordinary cash refund
→ available before plan generation
→ DEC-045 ends ordinary Plan refund eligibility after generation
```

FP-005 is explicitly the first point at which the participant receives the promised paid plan value.

The unresolved ambiguity is:

> **If the participant changes her lawful plan intent before the first plan fulfilment is successfully delivered, is that still part of completing the purchased plan, or has it already become a second paid re-personalisation?**

Without clarification, one implementation could charge again merely because the participant corrected or changed an onboarding choice before receiving any paid plan, while another could permit unlimited post-delivery regeneration under the label “change of intent.”

OPS-UPD-005 resolves that boundary.

## 20.3 Core distinction — onboarding intent is not post-delivery re-personalisation

The central working rule is:

```text
before first successful plan fulfilment
→ participant is still completing the purchased initial plan obligation

after first successful plan fulfilment
→ material preference/progress-based change is re-personalisation
  and follows DEC-038 / later adjustment law
```

Therefore a lawful change to the intended initial plan **before first fulfilment** does not require a second plan purchase merely because:

- the participant previously saved different onboarding choices;
- eligibility was calculated from an earlier draft;
- a generation request had already been queued;
- an undelivered immutable candidate snapshot was produced; or
- a stale worker is still processing old inputs.

This rule does not create a general free-regeneration entitlement after delivery.

## 20.4 Three plan-intent boundaries

### 20.4.1 Boundary A — mutable pre-generation intent

Before a plan generation snapshot is committed:

```text
purchased plan entitlement
→ available / unfulfilled

plan onboarding
→ participant may correct or change permitted intent
```

Examples may include:

- selected approved goal/pathway;
- meal-frequency preference;
- ordinary food preferences/exclusions;
- current valid temperament-profile selection;
- intended start timing;
- other approved generation inputs.

Safety-relevant factual changes are not treated as mere preferences. They update the owning Health/Safety truth and require eligibility to be re-evaluated before generation.

At this boundary:

- no plan has been fulfilled;
- no second purchase is required for a lawful change of initial intent;
- if the participant requests an ordinary refund while generation has not occurred, existing DEC-045 refund law applies;
- the participant may instead pause and retain the still-valid purchased plan right where current entitlement law permits;
- no new expiry is invented by this pass.

### 20.4.2 Boundary B — generation started or generated, but first fulfilment not successfully delivered

This is the key OPS-UPD-005 edge.

Current law says the entitlement remains available until successful delivery.

Therefore:

```text
generation work exists
≠
first paid plan fulfilment completed
```

If a lawful material change of initial intent is accepted before successful delivery:

1. the old generation lineage must not later become the delivered/current plan;
2. any already-generated immutable snapshot remains historical/internal evidence only as required by the owning model and must not be destructively rewritten;
3. the same still-unfulfilled purchased plan right may be used to produce the one eventual qualifying first delivery from the latest valid intent;
4. no second entitlement or second charge is created;
5. only one first-delivered plan outcome may become the participant's fulfilled initial once-off plan for that purchase.

This is **pre-first-fulfilment supersession**, not post-delivery re-personalisation.

The exact Resource/state representation for obsolete/cancelled/superseded pre-delivery generation remains JIT.

### 20.4.3 Boundary C — first successful plan fulfilment delivered

After the participant has received the first qualifying paid plan outcome:

```text
initial once-off plan obligation
→ fulfilled
```

Thereafter a material preference- or progress-based new plan request follows existing Product Law:

```text
new purchase
OR
active qualifying membership/add-on
```

unless an existing explicit exception applies, such as:

- correction of an error;
- safety replacement;
- the specific 90-day complimentary regeneration after a materially different later digital temperament result where the purchase included that assessment credit;
- another separately governed future entitlement.

OPS-UPD-005 creates no new generic post-delivery regeneration right.

## 20.5 Refund boundary remains separate from fulfilment boundary

These two questions are independent:

```text
Has the participant received the first paid plan fulfilment?
```

and:

```text
Is an ordinary cash refund still available?
```

Current law places them at different boundaries.

Working interpretation:

```text
before generation:
  first fulfilment = no
  ordinary Plan refund = available under current law

after generation but before successful delivery:
  first fulfilment = no
  ordinary Plan refund = already closed by DEC-045
  purchased plan obligation = still owed
  plan entitlement = remains available until successful delivery

after successful delivery:
  first fulfilment = yes
  ordinary Plan refund = closed
```

OPS-UPD-005 does **not** reopen ordinary cash refunds after generation.

If generation/delivery fails for technical reasons, the existing failure and applicable refund/remediation law remains separate.

## 20.6 Latest lawful intent wins before first fulfilment

The participant may have only one currently accepted initial-plan intent for a given unfulfilled purchase.

Conceptually:

```text
intent v1
→ superseded by intent v2
→ superseded by intent v3
→ one eventual first fulfilled plan
```

This does not require a universal “Intent” Resource.

It is a Product semantic requiring the affected JIT design to preserve:

- which input set was authoritative for generation;
- which earlier request was superseded/cancelled;
- safe concurrent update handling;
- immutable delivered-plan provenance.

The system must not race the participant by delivering an older request after a newer lawful intent has already been accepted.

## 20.7 Safety truth outranks participant intent

Participant change-of-intent never overrides Safety & Eligibility.

Examples:

```text
participant changes desired outcome to weight_reduction
+ current Safety outcome = general_wellness_only
→ no personalised weight-reduction plan

participant corrects health information
+ new Safety outcome = professional_review_required
→ stale personalised generation must not deliver

participant changes meal preference
+ allergy rule conflicts
→ allergy/safety rule wins
```

A material Health/Safety change before delivery invalidates stale plan-generation assumptions and requires current eligibility revalidation at the authoritative boundary.

The participant cannot preserve an unsafe prior eligibility decision by asking the platform to “use the old answers.”

## 20.8 General Wellness and blocked pathways

The initial commercial MVP explicitly supports:

```text
personalised seven-day plan
OR
approved General Wellness pathway
```

according to current eligibility.

Therefore:

### `eligible_automated`

The one initial paid plan obligation may be fulfilled by the lawful personalised plan generated from current valid inputs.

### `general_wellness_only`

The platform must not generate a personalised plan merely because a plan was purchased.

The approved General Wellness pathway is the governed safe outcome where current Product Law permits it.

### `professional_review_required`

The platform must not fabricate an automated personalised plan.

Professional review is a separately governed service and cannot be silently included merely to discharge the once-off plan purchase.

The purchased plan right is not consumed by a prohibited personalised-plan attempt.

### `insufficient_information`

Generation remains blocked until required information is completed or clarified.

The right remains unfulfilled.

Exact commercial/refund handling for a participant who never becomes eligible remains governed by existing refund/consumer law and is not silently expanded here.

## 20.9 Participant pause / abandonment before fulfilment

The platform must not force generation or delivery merely to consume an entitlement.

If the participant stops midway before first fulfilment:

```text
no qualifying delivery
→ initial plan obligation remains unfulfilled
```

Subject to current Commerce/Entitlement law, the participant may:

- resume later;
- update stale required information;
- re-enter current eligibility evaluation;
- request an ordinary refund if the refund boundary has not yet closed.

If plan generation has already occurred, OPS-UPD-005 does not invent a new cash-refund right.

Any later resume revalidates current Safety and other time-sensitive generation inputs rather than replaying stale authority.

## 20.10 Concurrent generation and change-of-intent

A change may arrive while plan generation is:

- queued;
- executing;
- committing;
- generated but not yet delivered;
- awaiting another governed pre-delivery step.

The implementation must define an atomic/current-authority boundary such that:

```text
accepted newer lawful intent
→ stale generation cannot later become first fulfilment
```

Safe outcomes may include:

- cancellation before generation starts;
- generation abort before commit;
- immutable stale candidate retained but marked non-deliverable;
- new generation from the latest valid snapshot;
- conflict requiring the participant/operator to re-read current state.

The exact mechanism is JIT/proof.

What is not permitted is two participant-visible “first plans” from one entitlement because two workers raced.

## 20.11 Display-only changes are not re-personalisation

Existing Product Law already distinguishes presentation from plan truth.

Examples:

- switching between approved kilojoule and Calorie display uses one underlying value and never regenerates the plan;
- approved language presentation may change according to governed content/version rules without creating a new nutritional entitlement merely because the participant changed interface/content language;
- normal use of alternatives already contained in the delivered immutable plan does not automatically create a new generated plan.

OPS-UPD-005 concerns material inputs that would change the initial generated plan, not ordinary viewing/presentation choices.

## 20.12 Temperament-profile change before first delivery

Product Law lets the participant select one current eligible temperament profile and does not automatically make the newest digital result current.

Therefore, before first plan fulfilment:

```text
participant lawfully selects a different valid current temperament profile
→ latest selected valid profile is used at generation/re-generation
→ same initial plan purchase
```

This is not the DEC-036 complimentary **post-delivery** regeneration case.

After an initial plan has already been delivered, the specific 90-day DEC-036 rule governs the complimentary regeneration triggered by a materially different later digital result where applicable.

The two rights must not be conflated.

## 20.13 Ownership — no new Plan Intent Domain

OPS-UPD-005 does not justify a new Domain.

### Plans & Nutrition

Owns:

- generation request/outcome;
- immutable generated/delivered plan snapshots;
- plan lifecycle;
- supersession/correction/withdrawal mechanics.

### Entitlements

Owns:

- whether the purchased plan right is still available/unfulfilled;
- consumption/redemption history;
- protection against duplicate plan-right effects.

### Safety & Eligibility

Owns:

- current eligibility and safety routing;
- whether personalised generation is currently permitted.

### Health Records

Owns:

- corrected/current participant health facts and provenance.

### Temperament

Owns:

- valid temperament results/current-profile truth.

### Commerce

Owns:

- ordinary cash refund eligibility and commercial refund transition.

No owner may collapse these into one generic “plan order state.”

## 20.14 Required Product invariants

The working candidate requires:

```text
before first successful delivery:
  lawful initial-plan intent may change without a second purchase

one unfulfilled purchased plan right:
  produces at most one qualifying first fulfilment

latest accepted lawful intent:
  wins over stale pre-delivery generation

safety / eligibility:
  revalidated before delivery where relevant
  and always outranks participant preference

generated-but-undelivered:
  does not equal fulfilled
  does not consume the right merely by existing

ordinary cash refund:
  remains governed independently by DEC-045
  and is not reopened by OPS-UPD-005

after first successful delivery:
  new preference/progress-based material plan change
  requires new purchase or qualifying recurring/add-on entitlement,
  except explicit existing correction/safety/regeneration rights
```

## 20.15 OPS-PT-271...290

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-271` | Participant selects `weight_reduction`, then changes to `health_foundation` before generation | Latest lawful goal is used; same unfulfilled plan entitlement; no second purchase | PASS |
| `OPS-PT-272` | Participant changes approved meal-frequency preference before generation | Updated preference may feed first generation subject to current rules; not post-delivery re-personalisation | PASS |
| `OPS-PT-273` | Participant corrects an allergy/medication fact before generation | Health/Safety truth updates and eligibility is re-evaluated; preference intent cannot bypass safety | PASS |
| `OPS-PT-274` | Participant lawfully changes the selected current temperament profile before first generation | First plan uses latest valid selected profile; no DEC-036 regeneration credit is consumed | PASS |
| `OPS-PT-275` | Participant requests cancellation/refund before generation | Existing ordinary Plan refund law applies; no generated plan; entitlement closes only through the governed Commerce/Entitlements consequence | PASS |
| `OPS-PT-276` | Participant pauses onboarding before generation but does not refund | No forced generation; unfulfilled plan right remains available subject to current entitlement law and later current-state revalidation | PASS |
| `OPS-PT-277` | Generation job is queued from intent v1; participant changes to lawful intent v2 before the job runs | Job must re-read/current-check or be superseded; stale v1 cannot become first delivered plan | PASS |
| `OPS-PT-278` | Immutable plan snapshot from v1 is generated but not yet delivered; participant's lawful v2 change is accepted | v1 remains non-deliverable historical/internal evidence as required; same unfulfilled right may produce one v2 first fulfilment; no second charge | PASS |
| `OPS-PT-279` | Old v1 worker completes after v2 generation has become authoritative | v1 cannot overwrite/deliver as current first plan; authoritative lineage converges on latest accepted valid intent | PASS |
| `OPS-PT-280` | Two concurrent participant intent changes race before delivery | One authoritative latest accepted intent wins; at most one first fulfilment is delivered | PASS |
| `OPS-PT-281` | Safety-relevant fact changes after generation but before delivery and now blocks personalisation | Stale personalised plan is not delivered; Safety re-evaluation wins; entitlement is not consumed by unsafe output | PASS |
| `OPS-PT-282` | Current eligibility changes to `general_wellness_only` before first fulfilment | No personalised plan is delivered; approved General Wellness path is used where Product Law permits | PASS |
| `OPS-PT-283` | Current eligibility becomes `professional_review_required` before delivery | No automated plan; professional service is not silently bundled; purchased plan right is not consumed by prohibited generation | PASS |
| `OPS-PT-284` | After a successfully delivered once-off plan, participant changes from weight reduction to weight maintenance | This is post-fulfilment re-personalisation and requires a new purchase or qualifying membership/add-on unless another explicit right applies | PASS |
| `OPS-PT-285` | After delivery, participant wants a different ordinary preference-based regenerated plan | DEC-038 applies; no generic free regeneration created by OPS-UPD-005 | PASS |
| `OPS-PT-286` | Participant switches energy-unit display or approved presentation language | Presentation change does not itself consume a new plan entitlement or require nutritional regeneration | PASS |
| `OPS-PT-287` | Later digital assessment materially changes temperament within the existing 90-day qualifying rule after initial plan delivery | DEC-036 specific complimentary regeneration applies; it is separate from pre-first-fulfilment change-of-intent | PASS |
| `OPS-PT-288` | Technical generation fails and participant changes a lawful preference before retry | Entitlement remains available; retry uses current valid inputs and stays idempotent | PASS |
| `OPS-PT-289` | Operator attempts to deliver a stale generated plan merely to avoid regeneration cost after a newer lawful pre-delivery intent was accepted | Prohibited; stale output cannot be used to manufacture fulfilment or consume the entitlement | PASS |
| `OPS-PT-290` | Duplicate/retried generation creates two internal candidate snapshots before any successful delivery | At most one may become qualifying first delivery; duplicate durable participant-facing fulfilment is prohibited | PASS |

All 20 tests pass under the working candidate semantics.

This remains authoring/pressure-test evidence, not independent certification.

## 20.16 Smallest upstream clarification for eventual compression

### Product Law

The smallest clarification is conceptually:

```text
A once-off Plan purchase is fulfilled only when its first qualifying governed
plan outcome is successfully delivered.

Before that first fulfilment, the participant may change lawful initial-plan
intent within the purchased product's approved scope without buying the Plan
again. This includes permitted changes to goal/pathway or generation
preferences and correction of onboarding information. Safety-relevant changes
must re-run current Safety/Eligibility authority.

If an accepted change occurs after generation has started or an undelivered
snapshot already exists, stale generation must not later become the delivered
current plan. The same still-unfulfilled plan right may produce the one
eventual qualifying first delivery from the latest lawful current inputs.
Generated historical/candidate state is not destructively rewritten.

This pre-first-fulfilment rule is not a general regeneration entitlement.
After successful first delivery, material preference- or progress-based
re-personalisation requires a new purchase or qualifying membership/add-on
unless an explicit existing correction, safety-replacement or complimentary
regeneration rule applies.

Plan refund eligibility remains a separate Commerce rule. Current DEC-045
continues to end ordinary Plan cash-refund eligibility after generation;
pre-first-fulfilment change-of-intent does not reopen that refund window.
```

### Decision Register

The eventual bounded Decision clarification should make explicit that:

```text
DEC-038 post-delivery re-personalisation
does not classify a lawful pre-first-fulfilment change of initial plan intent
as a second paid plan.

DEC-045 ordinary Plan refund cutoff remains separate:
generation may close ordinary cash-refund eligibility even though the Plan
entitlement remains unfulfilled until successful delivery.
```

No new DEC identifier is invented here.

## 20.17 Architecture / Domain consequences

### Architecture

No new Architecture Law is required.

Existing law already provides:

- current-authority checks;
- short authoritative transitions;
- durable async execution;
- business idempotency;
- immutable/versioned history;
- retry/reorder/concurrency safety;
- owner-bound cross-domain mutation.

The JIT proof must demonstrate that stale generation cannot race into delivery after a newer authoritative intent/safety state exists.

### Domain Map

No new Domain is required.

Existing ownership is sufficient:

```text
Plans & Nutrition
→ generation request/outcome + immutable plan lineage

Entitlements
→ unfulfilled/fulfilled purchased plan right

Safety & Eligibility
→ current permitted pathway

Health Records
→ corrected/current health inputs and provenance

Temperament
→ selected valid current profile

Commerce
→ cash refund eligibility and execution
```

## 20.18 Deliberately deferred to JIT / proof

This pass does not choose:

- exact plan-intent Resource/table names;
- exact generation-request states;
- exact obsolete/cancelled/superseded candidate labels;
- exact transaction/locking primitive;
- exact worker cancellation semantics;
- exact snapshot retention policy beyond existing immutable-history law;
- exact UI wording/button names;
- exact stale-input time thresholds;
- exact entitlement-consumption schema;
- exact participant resume UX;
- any new refund window;
- any new complimentary regeneration quota.

Those details must implement the semantic boundary above without weakening Safety or charging twice for the first undelivered obligation.

## 20.19 OPS-UPD-005 disposition

```text
OPS-UPD-005 =
  WORKING PRE-JIT CANDIDATE RESOLUTION CONVERGED

root issue =
  current law says an unfulfilled Plan entitlement survives until successful
  delivery and separately requires payment for post-delivery re-personalisation,
  but it does not explicitly classify a participant's lawful change of initial
  Plan intent before first fulfilment.

recommended authority level =
  Product Law + bounded Decision Register clarification

Product Law change type =
  semantic clarification; no new product capability

Architecture amendment required =
  NO

Domain Map amendment required =
  NO

new Domain required =
  NO

new OPS-UPD =
  0

new OPS-GAP =
  0

independent review =
  DEFERRED UNTIL COMPLETE PRE-JIT ARTIFACT

compression =
  DEFERRED UNTIL AFTER INDEPENDENT REVIEW
```

## 20.20 Updated workstream state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 270
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 290
CONTIGUOUS PT COVERAGE = OPS-PT-001...290

OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT; REPO PROMOTION DEFERRED
OPS-UPD-005 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-006 = OPEN / NEXT SUBSTANTIVE PASS
OPS-UPD-007 = OPEN

NEW OPS-UPD = 0
NEW OPS-GAP = 0

GITHUB / PR / ACTIONS = DEFERRED
INDEPENDENT REVIEW = AFTER ALL SUBSTANTIVE PRE-JIT CONVERGES
COMPRESSION = AFTER CLEAN INDEPENDENT REVIEW
IMPLEMENTATION = NOT AUTHORISED

NEXT SUBSTANTIVE PASS =
  OPS-UPD-006 — valid export followed by Full Deletion
```


---

# 21. v0.23.0 — OPS-UPD-006 valid export followed by Full Deletion pressure-test pass

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.22.0 BYTES PRESERVED UNCHANGED**  
> **SUBSTANTIVE PRE-JIT PASS — REPOSITORY / PR / ACTIONS REMAIN DEFERRED**  
> **OPS-UPD-006: WORKING CANDIDATE RESOLUTION CONVERGED, SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES**  
> **PRIMARY EXTERNAL VALIDATION GATE: OQ-032 — EXPORT AND DELETION OPERATIONS**  
> **SUPPORTING GATES: OQ-029, OQ-030, OQ-031, OQ-033 AS APPLICABLE**  
> **NEW PRESSURE TESTS: OPS-PT-291...310**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **IMPLEMENTATION NOT AUTHORISED**

## 21.1 Maintenance and provenance

This successor preserves the complete v0.22.0 file byte-for-byte and appends only the OPS-UPD-006 Pre-JIT analysis.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.22.0.md

predecessor SHA-256 =
  59852a58ad508fa4128ed46e207437d25eb369b5d7427235093a32fd7b888e20

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 21.2 Source-law position

Current Product, Decision, Architecture and Domain law already establishes:

```text
full deletion
→ is distinct from recoverable account closure
→ is deliberately irreversible after execution
→ has a 14-day cancellation window
→ must permit a secure export before execution
→ ends account-linked purchased access
→ cannot reconstruct the participant from transactions,
  backups or retained records

participant export
→ is secure and verified
→ contains human-readable + structured eligible data
→ may include original uploaded files
→ uses asynchronous generation where needed
→ uses secure short-lived / expiring delivery
→ may require redaction
→ is audited

deletion completion
→ requires live, derived, cached, file, external and access paths
  to be processed
→ isolates retained-by-obligation records
→ leaves no ordinary account recovery/reconstruction path

backup restore
→ must replay deletion/suppression before normal service

Privacy & Consent
→ owns export request/protected-delivery lifecycle
→ owns full-deletion orchestration/completion
→ does not own the underlying domain records
```

The unresolved interaction is:

> **What happens when a participant has a valid export, or a valid export is still being generated/delivered, and Full Deletion then executes?**

Without an explicit rule, one implementation might:

- keep a long-lived export link after deletion;
- regenerate a deleted account from an earlier export;
- delete the source data while leaving a future export job able to disclose it later;
- treat a legitimately downloaded participant copy as a platform deletion failure;
- or retain the entire export archive as “audit evidence.”

OPS-UPD-006 resolves those semantics while preserving the existing legal/privacy gates.

## 21.3 Core principle — export is a governed release, not a recovery mechanism

A participant export is a **point-in-time governed release of eligible data**.

It is not:

```text
a live mirror of the account
a portable entitlement
an account backup
a login credential
a reactivation token
a reconstruction authority
a way to bypass completed Full Deletion
```

Therefore:

```text
valid export delivered
+ later completed Full Deletion
=
participant may retain the copy already lawfully received
BUT
platform-held account/access/entitlement remains deleted
AND
the export cannot restore the prior identity relationship
```

The platform cannot guarantee deletion of a copy already downloaded onto a participant-controlled device.

Full Deletion governs NewYou-controlled and processor-controlled representations and access paths, not independent participant-held copies that were lawfully released before deletion.

## 21.4 Export is a snapshot with explicit time/scope

Each completed export must be understood as a snapshot assembled from eligible authoritative records at a defined generation/delivery boundary.

Conceptually it should make clear enough provenance to avoid implying:

```text
this archive always equals the participant's current account
```

Relevant export metadata may include, as appropriate:

- export/request identifier;
- generated-at / data-as-of time;
- requested/included categories;
- redactions or excluded categories where disclosure is restricted;
- delivery expiry;
- format/version.

Exact export manifest/schema remains JIT.

The export payload does not become an authoritative substitute for the source Domains.

## 21.5 Full-Deletion request does not silently remove the promised pre-execution export opportunity

Current Product Law says:

```text
full deletion requested
→ normal access revoked
→ 14-day cancellation window
...
```

and separately:

```text
Before execution, explain consequences and permit a secure export.
```

These must coexist.

Therefore the working semantic is:

```text
normal participant product access may be revoked
while
a narrowly scoped, strongly verified export pathway remains available
before deletion execution under the approved deletion/export policy
```

That pathway:

- does not reactivate ordinary account use;
- does not restore entitlements;
- does not reopen optional processing;
- does not permit editing business data merely because an export is being prepared;
- revalidates identity/authority appropriate to a sensitive export.

The exact UX and verification method remain OQ-032 / Identity JIT.

## 21.6 Export/deletion ordering

### 21.6.1 Export completes before deletion execution

Normal safe sequence:

```text
export requested
→ verified
→ generated
→ protected delivery made available
→ participant downloads / delivery expires
→ Full Deletion executes
```

On deletion execution, all platform-controlled export artefacts and delivery capabilities are themselves subject to the deletion/export lifecycle.

### 21.6.2 Export requested but unresolved when deletion would execute

A pre-execution export request must not remain in an unresolved state that can later disclose data after deletion is declared complete.

Minimum invariant:

```text
before deletion completion:
  every accepted pre-execution export request is in a terminal governed state
```

Examples of terminal outcome may include, under the approved OQ-032/legal policy:

- delivered and platform copy subsequently expired/deleted;
- participant-cancelled;
- expired;
- failed with the required participant notice/escalation;
- another legally approved terminal disposition.

This Pre-JIT pass does **not** invent the exact operational deadline or whether a particular legally valid export request must delay deletion execution.

That remains OQ-032 / legal/privacy validation.

What is prohibited is:

```text
deletion marked complete
while
an old export worker/link can later produce or expose the deleted participant estate
```

## 21.7 Platform-held export artefacts are deletion targets

An export may create platform-controlled temporary representations such as:

- archive files;
- PDF/JSON/CSV artefacts;
- copied original uploads;
- object-storage objects;
- thumbnails/previews created for the package;
- temporary worker files;
- download records;
- signed-link capabilities;
- delivery tokens;
- external processor copies.

These are not exempt merely because they were generated for the participant.

After Full Deletion execution/completion, NewYou-controlled export artefacts must be:

```text
deleted
or
expired / cryptographically or authoritatively inaccessible
```

according to the approved export/deletion contract.

A database row saying `deleted` while an old signed URL still works is not deletion completion.

## 21.8 Already-downloaded participant copy

Once a participant has successfully downloaded a valid export to a device/storage location she controls:

```text
participant-held copy
≠ platform-held live account
```

Full Deletion:

- does not remotely erase that independent copy;
- does not make the prior lawful export retroactively invalid;
- does not convert that copy into an entitlement;
- does not require NewYou to keep a matching server copy;
- must not permit that copy to reconstruct the deleted account.

Deletion/export messaging should make the boundary understandable:

```text
deleting your NewYou account/data does not delete files
you have already downloaded or independently copied
```

Exact legal wording remains legal/privacy review.

## 21.9 No reconstruction from a prior export

After completed Full Deletion:

```text
old export
→ cannot restore old account
→ cannot restore entitlements
→ cannot restore delivered plan/report access
→ cannot restore journal/progress history
→ cannot silently recreate health-profile authority
```

If the person later creates a new account, it is a new identity relationship under existing Product Law.

If a future capability ever permits a user to submit information from an old export:

```text
participant-supplied file/data
→ new untrusted input with explicit provenance
```

not:

```text
authoritative recovery of the deleted account
```

No broad import/recovery capability is authorised by this pass.

## 21.10 Ordinary post-deletion export versus legally required record access

Completed Full Deletion ends the ordinary participant-account export path because the account relationship and ordinary product access no longer exist.

However, current law separately allows:

- restricted financial records retained by obligation;
- professional records retained under approved professional authority;
- legal holds;
- minimised audit/security evidence.

This Pre-JIT pass does **not** claim that a person can never exercise a legally required data-access right concerning retained records after account deletion.

If law/professional duty requires such access, it must occur through the separately governed privacy/legal/professional process:

```text
verified legal/data-subject access
≠ account recovery
≠ entitlement restoration
≠ ordinary product export
```

Exact scope, verification, exclusions and recordkeeper responsibility remain with OQ-029 / OQ-033 and applicable legal review.

## 21.11 Retained-by-obligation records do not make the export a recovery archive

Commercial, professional, audit, security or legal-hold records may remain where current law requires.

Those records:

- remain minimised;
- remain isolated from ordinary participant/product use;
- cannot be used to recreate the prior participant estate;
- are not copied wholesale into a permanent “deleted user export” archive merely for convenience.

An export may include eligible records at the time it is lawfully generated.

Retention after deletion follows the underlying category's authority, not the existence of the export.

## 21.12 Legal holds and partial deletion

A scoped legal hold may delay destruction of the specific records it governs.

It does not justify retaining unrelated participant data or keeping ordinary product access alive.

For export:

- legally disclosable held records may be included where policy permits;
- restricted material may be omitted/redacted where required;
- the export should not falsely imply that omitted data does not exist;
- exact participant wording/disclosure rules remain legal/professional review.

For deletion:

```text
held record
→ restricted retention under its authority

all unrelated eligible records
→ continue through deletion
```

When the hold ends, deferred deletion resumes under current retention law.

## 21.13 Backup and restore interaction

A historical backup may contain:

- participant data that was later deleted;
- an export request;
- a generated export artefact;
- a delivery token/link state.

Restore cannot make those historically valid objects current again.

Before normal service after restore:

```text
replay current deletion/suppression truth
→ reapply export expiry/deletion truth
→ remove/revoke resurrected delivery capability
→ verify deleted identity cannot reappear
```

A restored export archive is no more authoritative than a restored deleted account.

OQ-031 remains the executable restore/replay proof gate.

## 21.14 External processors and storage

If an export or deletion path touches external processors:

- object storage;
- support tooling;
- analytics;
- communication providers;
- professional systems;
- other approved processors;

their exact export/deletion/evidence obligations remain OQ-030 inventory/contract work.

The Product-level invariant is:

```text
processor-held copy or delivery capability
cannot remain a hidden ordinary access path after deletion completion
```

Provider confirmation is evidence of processor handling, not a replacement for Privacy & Consent deletion-completion authority.

## 21.15 Sensitive delivery links

Export delivery is explicitly short-lived/protected.

Therefore:

- URL possession alone must not become permanent participant authority;
- current delivery authorisation is revalidated where the approved delivery design requires it;
- a link/token must expire;
- deletion execution must revoke/invalidate platform-controlled remaining delivery capability;
- caches/CDNs must not preserve a still-usable protected export after the authoritative path is closed.

Exact signed-URL duration, token format, CDN invalidation and in-flight-transfer behaviour remain Architecture/JIT/OQ-032 proof detail.

Minimum semantic rule:

```text
no new export download may be authorised from the deleted account
after deletion execution begins
```

and:

```text
deletion completion requires no remaining platform-controlled
ordinary download path for that deleted export
```

## 21.16 Export audit evidence is not the export payload

It may be necessary and lawful to retain minimised evidence that:

- an export was requested;
- verification occurred;
- generation completed/failed;
- delivery was made available;
- download/delivery status was observed where appropriate;
- artefacts expired/deleted;
- deletion later completed.

That does not justify retaining the entire exported health/journal/plan archive in Audit & Evidence.

Conceptually:

```text
audit fact that export occurred
≠
retained duplicate of export payload
```

Audit remains minimised and governed by its own retention rule.

## 21.17 Export freshness during the deletion window

An export is not a live synchronisation channel.

If participant/business state changes after an export is generated but before deletion execution, an earlier export may be stale by definition.

The system should not silently label an old snapshot as “current”.

If the participant requests a newer export before deletion execution, that request follows the approved export policy and current authoritative state.

This pass does not require unlimited regeneration or indefinite extension of the deletion window.

Exact request cutoffs/deadlines/retry limits remain OQ-032.

## 21.18 Security / compromise interaction

Export and Full Deletion are high-risk actions.

A deletion request does not weaken export verification.

If account compromise is suspected:

- existing compromise containment may freeze sensitive actions;
- export delivery may require stronger re-verification/manual recovery;
- deletion processing may continue only according to approved current policy;
- support must not send a sensitive archive merely because a deletion deadline is approaching.

Security containment cannot silently become permanent retention authority; unresolved legal/privacy handling routes through the existing gates.

## 21.19 Ownership — no Export Archive / Deletion Domain

OPS-UPD-006 does not justify a new Domain.

### Privacy & Consent

Owns:

- export request/protected lifecycle;
- Full Deletion request/cancellation/execution/completion;
- retention-policy assignment;
- legal holds;
- deletion/suppression replay truth.

### Data-owning Domains

Own:

- which authoritative records exist;
- their category-specific export representation;
- deletion/anonymisation/retention behaviour.

Privacy orchestrates but does not take ownership of their underlying business truth.

### Identity & Access

Owns:

- participant identity;
- authentication/step-up context;
- account lifecycle consequences.

### Audit & Evidence

Owns:

- minimised governance/security evidence;
- not a duplicate export payload.

### Object storage / workers / processors

Are execution/storage mechanisms.

They do not become privacy authority.

## 21.20 Required Product-level invariants

```text
secure export opportunity exists before Full Deletion execution

export is a point-in-time governed release
not a recovery or entitlement mechanism

participant-downloaded copy:
  may remain outside platform control
  and is not itself a failure of platform Full Deletion

platform-controlled export copy/link:
  must be expired/deleted/revoked as part of deletion/access closure

accepted pre-execution export request:
  cannot remain unresolved in a way that may later disclose data
  after deletion is declared complete

completed Full Deletion:
  no ordinary account export/recovery/reconstruction path remains

old export:
  cannot restore old identity, entitlements or participant history

retained-by-obligation data:
  remains isolated
  and may support only separately governed legal/professional duties

restore:
  must replay deletion plus export suppression before service resumes

audit:
  may retain minimised evidence of export/deletion
  but not the full export archive by convenience
```

## 21.21 OPS-PT-291...310

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-291` | Participant downloads a valid export, then Full Deletion completes | Platform account/data/access are deleted according to policy; participant's independent downloaded copy may remain; it cannot restore the deleted account | PASS |
| `OPS-PT-292` | Export is generated and link is still valid but participant has not downloaded when deletion execution begins | Platform revokes/deletes remaining delivery capability; link cannot remain an ordinary post-deletion access path | PASS |
| `OPS-PT-293` | Full Deletion is requested and normal account access is revoked; participant then requests the promised export during the pre-execution window | Narrow strongly verified export path remains possible without restoring ordinary product/account access | PASS |
| `OPS-PT-294` | Export generation is still running when deletion would otherwise complete | Export request must first reach a terminal governed outcome; deletion cannot be declared complete while the job may later disclose deleted data | PASS |
| `OPS-PT-295` | Export job fails near the deletion boundary | Failure becomes explicit/terminal under OQ-032 policy with required notice/escalation; no stale job may deliver after deletion completion; exact legal deadline is not invented here | PASS |
| `OPS-PT-296` | Participant cancels Full Deletion within the 14-day window after downloading an export | Deletion cancellation follows existing policy; export remains only a bounded snapshot and does not become authority over current account state | PASS |
| `OPS-PT-297` | Participant later creates a new account and uploads an old pre-deletion export asking NewYou to “restore everything” | Reject reconstruction; any future accepted data import would be new participant-supplied input with explicit provenance, not recovered authority | PASS |
| `OPS-PT-298` | Tax/payment records remain retained after Full Deletion | They stay isolated/minimised and cannot restore ordinary participant access; any legally required later access is a separate verified privacy/legal process | PASS |
| `OPS-PT-299` | Professional records remain under approved professional retention after Full Deletion | Professional-record access, if applicable, follows recordkeeper/legal authority; it does not reactivate account/entitlement/product export | PASS |
| `OPS-PT-300` | Legal hold covers one professional/dispute record category during Full Deletion | Hold only scoped records; unrelated eligible data still deletes; export inclusion/redaction follows the approved legal policy | PASS |
| `OPS-PT-301` | Disaster recovery restores a backup containing a previously valid export object/link for a now-deleted participant | Deletion/export suppression replay revokes/removes it before normal service; restore cannot resurrect delivery capability | PASS |
| `OPS-PT-302` | Old signed export URL is present in browser history/CDN after deletion | Possession/cache cannot provide durable authority; deletion completion requires the platform-controlled protected delivery path to be invalid/expired | PASS |
| `OPS-PT-303` | Export archive was temporarily stored with an approved external processor/object store | Processor-held temporary copy follows the deletion/export contract; external evidence feeds Privacy completion but is not itself authority | PASS |
| `OPS-PT-304` | Export expires before participant downloads it and Full Deletion later completes | Expired export does not survive as a hidden recovery copy; no ordinary post-deletion regeneration from the deleted account | PASS |
| `OPS-PT-305` | Export contains copies of original participant uploads; Full Deletion then deletes platform originals and derivatives | Participant-held exported copies may remain; platform-controlled originals/derivatives/export artefacts are still deleted according to policy | PASS |
| `OPS-PT-306` | Participant changes data after an export snapshot is generated but before deletion | Earlier export remains an as-of snapshot, not current authority; any newer export follows current policy rather than silently mutating the old archive | PASS |
| `OPS-PT-307` | Duplicate/retried export workers create multiple temporary copies | All copies remain part of the same governed export lifecycle and deletion scope; retries cannot leave an orphaned downloadable archive | PASS |
| `OPS-PT-308` | Account-compromise signal appears while deletion/export is pending | Strong verification/containment governs sensitive export; support cannot bypass security just to finish the export quickly | PASS |
| `OPS-PT-309` | Audit implementation proposes keeping the full export ZIP permanently to prove it was delivered | Rejected; retain minimised export/deletion evidence, not a convenience duplicate of sensitive payload | PASS |
| `OPS-PT-310` | After Full Deletion, participant asks NewYou to delete the copy she downloaded to her own device | NewYou deletes only representations/capabilities it controls; participant-controlled copy is outside platform deletion control and should have been explained in deletion/export messaging | PASS |

All 20 pressure tests are internally consistent with the working candidate semantics.

This remains authoring/pressure-test evidence, **not** independent certification and **not** legal advice or final legal validation.

## 21.22 Smallest upstream clarification for eventual compression

### Product Law

The smallest clarification is conceptually:

```text
A participant export is a secure point-in-time release of eligible participant
data. It is not an account backup, entitlement, recovery token or source of
business authority.

Full Deletion must permit the governed secure export opportunity before
execution. A deletion request may revoke normal product/account access while
still allowing the narrowly scoped verified export path required by the
approved deletion/export policy.

Once Full Deletion executes, every NewYou-controlled export artefact,
temporary copy and delivery capability is subject to expiry/deletion/revocation.
Deletion may not be declared complete while an unresolved pre-execution export
could later disclose the deleted participant estate.

A copy already lawfully downloaded by the participant is outside NewYou's
ordinary technical control. Full Deletion does not remotely erase that copy,
but the copy cannot restore the deleted account, entitlements, plans, reports,
journals, health profile or prior identity relationship.

Any access after deletion to records lawfully retained for financial,
professional, legal, audit or security reasons is a separately governed
privacy/legal/professional process and does not constitute account recovery.

Exact export/deletion deadlines, retry/failure handling, processor obligations,
participant notices and retained-record access remain subject to the existing
legal/privacy/operations gates.
```

### Decision Register

The eventual bounded Decision clarification should make the relationship explicit:

```text
DEC-240 participant export
+ DEC-223 irreversible completed deletion
+ DEC-225 purchased-access consequence
+ DEC-239 backup deletion boundary
+ DEC-243 deletion completion

mean:

  exported participant copy may survive outside platform control,
  but no platform-controlled export/recovery path may survive completed
  Full Deletion and no export may reconstruct the deleted account.
```

No new DEC identifier is invented here.

## 21.23 External validation that remains required

OPS-UPD-006 can converge at Pre-JIT without pretending to resolve expert-owned law.

The following remain genuine downstream gates:

### OQ-029 — Retention schedule matrix

Must establish exact approved category durations, exceptions, retained-obligation handling and deletion actions.

### OQ-030 — External processor deletion inventory

Must establish which processors/storage/providers receive data and their deletion/export/evidence behaviour.

### OQ-031 — Backup restore and deletion replay

Must prove restored data/export artefacts cannot resurrect deleted authority or access.

### OQ-032 — Export and deletion operations

Primary operational gate.

Must define:

- verification levels;
- job deadlines;
- retries;
- pending/terminal states;
- participant notices;
- failure alerts;
- completion evidence;
- the exact race policy when export is unresolved as deletion execution approaches.

### OQ-033 — Professional record authority

Applies where retained professional records or later participant access intersect the deleted account boundary.

No Pre-JIT wording here supersedes those gates.

## 21.24 Architecture / Domain consequences

### Architecture

No new Architecture Law is required.

Existing Architecture already requires:

- export as governed data release;
- short-lived protected delivery;
- deletion across live/derived/cache/file/external paths;
- suppression replay after restore;
- bounded durable async;
- current-authority verification;
- provider evidence rather than provider authority.

The later proof must demonstrate the export/deletion races and non-resurrection invariants above.

### Domain Map

No new Domain is required.

Existing ownership is sufficient:

```text
Privacy & Consent
→ export lifecycle + deletion orchestration/completion + suppression truth

Identity & Access
→ identity + verification + account lifecycle

source Domains
→ category-specific authoritative data + export/delete contract

Audit & Evidence
→ minimised evidence only

external processors / object storage / workers
→ mechanisms, not authority
```

## 21.25 Deliberately deferred to JIT / legal / operations proof

This pass does not decide:

- exact export file/manifest schema;
- exact export object-store path;
- exact signed-link/token format or lifetime;
- exact encryption/password packaging mechanism;
- exact export job SLA;
- exact deletion deadline extension rules;
- exact participant notice wording;
- exact legal subject-access process after deletion;
- exact retained-record disclosure exclusions;
- exact professional recordkeeper duties;
- exact processor deletion APIs;
- exact CDN/cache invalidation mechanism;
- exact in-flight download behaviour at the deletion boundary;
- exact operational escalation thresholds;
- exact proof/audit event schema.

Those are downstream details/gates and must not weaken the semantic invariants above.

## 21.26 OPS-UPD-006 disposition

```text
OPS-UPD-006 =
  WORKING PRE-JIT CANDIDATE RESOLUTION CONVERGED
  SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS VALIDATION

root issue =
  current law separately defines secure participant export and irreversible
  Full Deletion, but does not fully state the lifecycle interaction when an
  export has already been delivered or remains pending as deletion executes.

recommended authority level =
  Product Law semantic clarification
  + bounded Decision interpretation
  + existing OQ-029...OQ-033 validation

Product Law change type =
  boundary clarification; no new product capability

Architecture amendment required =
  NO

Domain Map amendment required =
  NO

new Domain required =
  NO

new OPS-UPD =
  0

new OPS-GAP =
  0

legal/privacy validation =
  STILL REQUIRED; NOT CLAIMED RESOLVED

independent review =
  DEFERRED UNTIL COMPLETE PRE-JIT ARTIFACT

compression =
  DEFERRED UNTIL AFTER INDEPENDENT REVIEW
```

## 21.27 Updated workstream state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 290
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 310
CONTIGUOUS PT COVERAGE = OPS-PT-001...310

OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT; REPO PROMOTION DEFERRED
OPS-UPD-005 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-006 = WORKING CANDIDATE RESOLUTION CONVERGED
              SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES
OPS-UPD-007 = OPEN / NEXT SUBSTANTIVE PASS

NEW OPS-UPD = 0
NEW OPS-GAP = 0

GITHUB / PR / ACTIONS = DEFERRED
INDEPENDENT REVIEW = AFTER ALL SUBSTANTIVE PRE-JIT CONVERGES
COMPRESSION = AFTER CLEAN INDEPENDENT REVIEW
IMPLEMENTATION = NOT AUTHORISED

NEXT SUBSTANTIVE PASS =
  OPS-UPD-007 — General Wellness choice-window clock start
```


---

# 22. v0.24.0 — OPS-UPD-007 General Wellness choice-window clock-start pressure-test pass

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.23.0 BYTES PRESERVED UNCHANGED**  
> **SUBSTANTIVE PRE-JIT PASS — REPOSITORY / PR / ACTIONS REMAIN DEFERRED**  
> **OPS-UPD-007: WORKING CANDIDATE RESOLUTION CONVERGED FOR LATER INDEPENDENT REVIEW**  
> **CURRENT SOURCE LAW DOES NOT DEFINE A GENERAL-WELLNESS CHOICE-WINDOW DURATION OR ITS COMMERCIAL OPTION SET**  
> **THIS PASS RESOLVES THE CLOCK-START INVARIANT ONLY; IT DOES NOT INVENT THE WINDOW ITSELF**  
> **NEW PRESSURE TESTS: OPS-PT-311...330**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **IMPLEMENTATION NOT AUTHORISED**

## 22.1 Maintenance and provenance

This successor preserves the complete v0.23.0 file byte-for-byte and appends only the OPS-UPD-007 Pre-JIT analysis.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.23.0.md

predecessor SHA-256 =
  54668c5dd398d647ad2a5b8b7e2bb1153294c26cd53d2bf485ccc736fe28b28a

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 22.2 Source-law position

Current Product / Decision / Roadmap law establishes:

```text
plan onboarding
→ produces one current eligibility outcome

eligibility outcomes =
  eligible_automated
  general_wellness_only
  professional_review_required
  insufficient_information

general_wellness_only
→ only the approved General Wellness Starter Pathway is permitted

moderate-risk routing
→ may provide General Wellness
→ may request clarification
→ may request professional review / escalation

pregnancy / breastfeeding
→ personalised eating plan requires professional review
→ General Wellness may remain available while awaiting review

first-paid critical path
→ eligibility
→ personalised seven-day plan
   OR governed General Wellness fallback

frontend
→ must explain the governed safe next outcome
→ must not permit participant override of Safety authority
→ long-lived/stale views re-read current authority

Safety & Eligibility
→ owns the current routing outcome
```

However, the current source snapshots do **not** define:

- a General Wellness participant `choice window`;
- the duration of such a window;
- a universal set of commercial choices inside it;
- a refund/credit/professional-review election created merely by `general_wellness_only`;
- a timeout consequence if a participant does not choose.

Therefore this pass must not invent any of those.

The narrower existing OPS-UPD-007 question is valid:

> **If Product Law or the final Feature Pack contract gives a participant a bounded choice after a General Wellness routing outcome, what authoritative event starts that participant-facing clock?**

## 22.3 Core distinction — eligibility time is not choice-window time

The answer is:

```text
eligibility outcome committed
≠
participant choice durably available
```

Safety & Eligibility may authoritatively establish:

```text
general_wellness_only
```

before the participant can actually exercise any associated Product-approved choice.

A participant-facing deadline must not lose time because:

- evaluation completed in a background transaction;
- the participant was signed out;
- the result page was not yet available;
- required bilingual/safety content was unavailable;
- a worker had not yet materialised the governed choice;
- a stale session was showing old state;
- the platform was degraded;
- an operator had not yet resolved a blocking workflow required by the approved option set.

Therefore:

```text
T1 = current eligibility outcome committed
T2 = complete governed participant choice durably available and exercisable

choice-window start = T2
not T1
```

where a choice window actually exists under approved Product law.

## 22.4 Working definition — `choice_available_at`

This is a Product semantic, not a required database field name.

The choice becomes durably available when all requirements for the approved participant election are simultaneously true:

1. the relevant current Safety & Eligibility outcome is authoritative and still current;
2. the participant has the applicable current product/entitlement context;
3. the complete Product-approved option set for that outcome is known;
4. the participant-facing explanation and consequences required for an informed choice are available in the applicable governed language/content version;
5. the participant has an authorised durable path through which the choice can actually be submitted;
6. no current safety, identity, privacy, commercial or release blocker makes the displayed choice false or non-exercisable.

Conceptually:

```text
current authoritative outcome
+ complete approved choice contract
+ authorised participant access to exercise it
=
choice_available_at
```

The exact persistence representation remains JIT.

## 22.5 Events that do NOT start the clock

None of the following alone starts a participant-facing choice window:

```text
health intake submitted
eligibility evaluation requested
eligibility evaluation completed
general_wellness_only written to the database
operator work item created
support case assigned
worker/job enqueued
notification intent created
email/SMS/WhatsApp accepted by provider
notification delivered
notification opened/read
page component mounted
Analytics event emitted
dashboard count updated
```

Why:

- internal/domain timestamps may precede participant availability;
- provider communication state is delivery evidence, not Product authority;
- open/read telemetry is optional/unreliable and can be blocked;
- UI render/Analytics are projections;
- operator work assignment is attention, not business authority.

## 22.6 Durable availability does not require participant open/read telemetry

The opposite failure is also unsafe.

The clock must not depend on:

```text
participant opens page
participant reads message
participant clicks notification
participant scrolls to choice
```

as the authority event.

Otherwise a participant could indefinitely prevent a legitimate bounded Product window from starting simply by never opening the app, and the business rule would become dependent on unreliable surveillance-style telemetry.

Therefore, once the complete governed choice is durably available through the authorised participant path:

```text
window may start
even if
participant has not yet opened/read it
```

if an approved Product window exists.

Communications may improve awareness but do not define clock truth.

## 22.7 Choice availability must be real, not nominal

A link/button existing in a projection is insufficient if exercising it cannot succeed.

Examples:

```text
choice screen visible
+ entitlement authority unavailable
→ not safely exercisable

choice CTA visible
+ Safety state already superseded
→ stale / not valid

choice available only in unapproved language
where governed bilingual content is required
→ release defect; do not manufacture clock start

choice page cached
+ authoritative action disabled by platform degradation
→ projection cannot create availability truth
```

The authoritative path must fail closed where current truth cannot be established.

## 22.8 Safety outcome changes before choice availability

If:

```text
T1: general_wellness_only committed
T1+Δ: new/corrected health fact changes current eligibility
before T2 choice availability
```

then the stale General Wellness outcome does not create a historical participant deadline.

Current Safety authority wins.

Examples:

```text
general_wellness_only
→ eligible_automated
```

may move the participant to the newly permitted plan path.

```text
general_wellness_only
→ professional_review_required
```

may remove an option that is no longer safe/permitted.

```text
general_wellness_only
→ insufficient_information
```

may require clarification before any affected election.

No clock starts against an option set that never became validly exercisable.

## 22.9 Safety outcome changes after the clock has started

A started Product choice window does not freeze Safety authority.

If current health/safety truth changes materially:

```text
old option set
→ re-evaluate
```

Any option that is no longer permitted is immediately invalid regardless of remaining window time.

The old window cannot authorise a stale unsafe transition.

This pass does not invent whether:

- the old window is cancelled;
- a new window begins;
- remaining time carries over;
- commercial remedies change.

Those are Product/JIT contract questions for the concrete option set.

The only invariant locked here is:

```text
stale timer state never outranks current Safety authority
```

## 22.10 Participant access problems before clock start

A participant-facing deadline cannot start merely because the server internally knows the outcome if the participant has no valid means to exercise the choice.

Examples:

- account verification/recovery state currently blocks the protected action;
- platform outage prevents authoritative choice submission;
- required content failed publication;
- deployment/degradation mode intentionally disables the transition.

In such a condition:

```text
choice_available_at = not yet established
```

This does not require optional notification delivery to succeed.

It requires the authoritative Product action itself to be available.

## 22.11 Platform interruption after clock start

This pass is deliberately narrower than a full choice-window policy.

If the platform later becomes unavailable for a material period after a valid `choice_available_at`, the fair expiry/extension rule depends on the Product-approved duration and consequence.

Therefore this pass does not invent:

- pause semantics;
- automatic extension length;
- outage grace;
- business-day calculation;
- manual exception authority.

The eventual Product/Feature Pack contract must state the behaviour if the window can expire into a material commercial or access consequence.

What implementation may not do is silently choose a punitive interpretation from infrastructure convenience.

## 22.12 Time basis and timezone

The authoritative start must be recorded as a durable instant sufficient to reconstruct when the choice became available.

This pass does not decide whether the eventual window is:

- elapsed hours;
- elapsed days;
- calendar days;
- business days;
- participant-local dates.

If Product later defines a calendar-based window, timezone semantics must be explicit.

For the South African first launch, Africa/Johannesburg is the platform default, but this pass does not turn that into a universal future market rule.

Browser-local clocks are not authority.

## 22.13 Choice-window ownership

No new General Wellness / Choice / Timer Domain is justified.

### Safety & Eligibility

Owns:

- current `general_wellness_only` outcome;
- safety routing;
- supersession/re-evaluation;
- whether personalised automation is permitted.

It does **not** automatically own commercial remedies or every participant election created downstream.

### Entitlements

Owns:

- current paid access/right affected by the participant election;
- any entitlement consequence explicitly authorised by Product law.

### Commerce

Owns:

- refund/credit/commercial consequence if the approved option set actually includes one.

OPS-UPD-007 does not create such a remedy by itself.

### Plans & Nutrition / Content & Media

Own their applicable governed outputs/content.

### Identity & Access

Owns the current authorised participant relationship/session/action context.

### Communications

May notify the participant.

It does not own `choice_available_at`.

### Analytics

May measure:

- time from eligibility to choice availability;
- time from availability to participant action;
- expiry/selection rates where governed.

It cannot start or end the window.

## 22.14 The choice contract must be complete before timing begins

A time-limited choice is meaningful only if the participant can understand what she is deciding.

If Product later authorises a choice window, the final contract must define, before release:

```text
who receives the choice
under which eligibility outcome(s)
available options
option consequences
window duration
clock-start rule
expiry consequence
whether choice is revocable before execution
effect of later Safety changes
effect of platform outage/degradation
support/manual-exception authority, if any
commercial/refund interaction, if any
```

OPS-UPD-007 settles only:

```text
clock-start rule
```

The remaining fields may already be governed elsewhere in a future/current authority successor; if not, they must be resolved before implementation rather than guessed.

## 22.15 General Wellness availability is not necessarily a choice

This distinction prevents over-expansion.

Current Product Law says General Wellness may be the permitted safe pathway.

That can mean:

```text
current safe output is General Wellness
```

without implying:

```text
participant gets a timed commercial election
```

Therefore:

```text
general_wellness_only
does not automatically create a timer
```

A timer exists only if the relevant Product authority explicitly creates a bounded participant election.

If no bounded election is authorised:

```text
OPS-UPD-007 clock-start mechanism is dormant / not applicable
```

and General Wellness proceeds under its ordinary governed pathway.

## 22.16 Interaction with OPS-UPD-005

OPS-UPD-005 established that a once-off Plan remains unfulfilled until first successful qualifying fulfilment and that current Safety authority controls what may be delivered.

OPS-UPD-007 composes with that rule:

```text
paid Plan right
+ current general_wellness_only outcome
→ no unsafe personalised plan

if Product provides a bounded participant election:
  start only at durable governed choice availability

if Product does not provide such an election:
  no invented timer
```

Neither rule silently creates:

- a cash refund;
- a professional-review entitlement;
- a second Plan;
- an expiry of the paid right;
- a new General Wellness entitlement.

Those consequences require their own Product authority.

## 22.17 Interaction with OPS-UPD-003

If Support or another operator assists the participant with an authorised choice:

- operator visibility does not create the choice;
- the participant's available option set comes from current owning-domain authority;
- assistance may not bypass current Safety;
- a consequential operator command still follows OPS-UPD-003 authority rules;
- an operator cannot backdate `choice_available_at` merely to force expiry.

## 22.18 Required Product-level invariants

```text
general_wellness_only timestamp
≠ participant-facing choice-window start

choice window exists only when Product explicitly creates one

if a choice window exists:
  start = first durable instant at which the complete,
          current, authorised choice is actually exercisable

provider notification state:
  not clock authority

participant read/open telemetry:
  not clock authority

stale UI / Analytics / operator queue:
  not clock authority

current Safety state:
  always outranks old choice/timer state

before valid choice availability:
  no participant time may be consumed

after valid choice availability:
  read/open is not required to start the approved window

duration / expiry / outage grace / commercial consequences:
  must be explicitly Product-governed
  and are not invented by this pass
```

## 22.19 OPS-PT-311...330

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-311` | Eligibility commits `general_wellness_only` at 09:00; governed participant choice becomes exercisable at 09:07 | Any approved choice window starts at 09:07, not 09:00 | PASS |
| `OPS-PT-312` | Eligibility commits while participant is signed out and the protected choice path has not yet been established | Internal eligibility timestamp does not consume participant choice time | PASS |
| `OPS-PT-313` | Choice is durably available in-app; notification email is delayed for hours | Clock may start from durable choice availability; email delivery does not control it | PASS |
| `OPS-PT-314` | Email provider says delivered before the authoritative in-app choice exists | Provider delivery cannot start the choice clock | PASS |
| `OPS-PT-315` | Choice is durably available but participant never opens the app/email | Approved window can still run; open/read telemetry is not required authority | PASS |
| `OPS-PT-316` | Analytics records a `general_wellness_choice_shown` event before the authoritative action is usable | Analytics cannot create `choice_available_at`; no clock from the projection event | PASS |
| `OPS-PT-317` | Support manually marks “choice offered” while the participant action is still unavailable | Work/support projection cannot start clock authority | PASS |
| `OPS-PT-318` | Cached page shows an old General Wellness choice after Safety has changed to `professional_review_required` | Stale choice is invalid; current Safety wins; old clock cannot authorise action | PASS |
| `OPS-PT-319` | New health fact changes `general_wellness_only` to `eligible_automated` before choice availability | No General Wellness choice clock starts from the superseded outcome | PASS |
| `OPS-PT-320` | New health fact changes the outcome after the choice window started | Unsafe/stale options are invalidated immediately; exact restart/carry-over rule remains Product contract, not implementation guesswork | PASS |
| `OPS-PT-321` | Required governed bilingual choice explanation is unavailable in the participant's applicable release language | Choice is not release-ready/exercisable; do not manufacture clock start | PASS |
| `OPS-PT-322` | Platform is in a degradation mode where the choice page loads but submission is intentionally disabled | Nominal page visibility is insufficient; clock does not start until authoritative action is genuinely available | PASS |
| `OPS-PT-323` | Platform outage begins after a valid choice window has already started | Do not invent pause/extension semantics; route to explicit Product window policy while preserving the original start evidence | PASS |
| `OPS-PT-324` | Browser/client clock is wrong by several hours | Server/durable authoritative instant governs; browser clock cannot shift the start | PASS |
| `OPS-PT-325` | Participant timezone changes after clock start | Existing start instant remains immutable; any calendar-day expiry calculation must follow the explicit Product timezone rule rather than recomputing start | PASS |
| `OPS-PT-326` | `general_wellness_only` is the safe fallback and Product defines no participant election at all | No choice timer is created merely because the outcome exists | PASS |
| `OPS-PT-327` | Future Product contract offers a bounded election including a commercial remedy | Clock-start invariant remains durable choice availability; Commerce owns the actual authorised commercial consequence | PASS |
| `OPS-PT-328` | Participant has an unfulfilled Plan right under OPS-UPD-005 and routes to General Wellness | No personalised plan is forced; no refund/credit/pro-review right is invented; timer exists only if separately authorised | PASS |
| `OPS-PT-329` | Support assists a participant during an active choice window | Assistance uses current owning-domain policy; Support cannot extend/backdate/override Safety unless explicit authority permits it | PASS |
| `OPS-PT-330` | Duplicate worker/retry attempts try to establish choice availability multiple times | One logical choice episode has one authoritative first valid availability instant; retries cannot reset/manipulate the clock | PASS |

All 20 pressure tests are internally consistent with the working candidate semantics.

This remains authoring/pressure-test evidence, not independent certification.

## 22.20 Smallest upstream clarification for eventual compression

The smallest safe Product clarification is:

```text
A `general_wellness_only` eligibility outcome does not itself create or start
a participant-facing choice deadline.

Where Product Law explicitly gives the participant a bounded election after a
General Wellness routing outcome, the window begins only when the complete
current governed choice is durably available and actually exercisable through
an authorised participant path.

The start is not the health-intake submission time, internal eligibility
timestamp, queue/work timestamp, notification send/delivery state, participant
open/read telemetry, Analytics event or UI render.

Current Safety authority always supersedes stale choice/timer state. A bounded
choice must define its duration, available options, expiry consequence,
commercial effect, outage/degradation treatment and any manual exception
authority before implementation. If no bounded participant election is
explicitly authorised, no General Wellness choice timer exists.
```

No new choice duration or remedy is created by this clarification.

## 22.21 Authority-level disposition

### Product Law

A bounded semantic clarification is justified because the existing OPS-UPD-007 gap concerns when a participant-facing Product clock begins.

The clarification must **not** imply that current law already contains a time-limited General Wellness election where the source authority does not show one.

### Decision Register

If the eventual governed Product successor contains such a choice window, its Decision wording should explicitly distinguish:

```text
eligibility outcome established
from
choice durably available
```

and should state the actual duration/consequence separately.

No new DEC identifier is invented here.

### Architecture Law

No amendment required.

Current Architecture already supports:

- server-side authority;
- current-state revalidation;
- durable state;
- stale-projection invalidation;
- reliable time sources;
- retries/idempotency;
- frontend as untrusted intent/projection.

### Domain Map

No amendment required.

Safety & Eligibility owns the route; affected business consequence remains with its actual owner.

No Timer, Choice, General Wellness, Operations or Support Domain is justified.

## 22.22 Deliberately deferred to Product / JIT / proof

This pass does not decide:

- whether a General Wellness choice window exists in the final first-paid Product contract;
- exact duration;
- exact option set;
- refund/credit consequence;
- professional-review entitlement;
- Plan-entitlement expiry consequence;
- business-day/calendar-day/elapsed-hour calculation;
- outage pause/extension rule;
- participant timezone treatment for calendar windows;
- manual exception/extension authority;
- exact persistence field/Resource/state names;
- exact notification cadence;
- exact UI wording;
- exact timer implementation;
- exact clock source/library.

These must be supplied by the owning authority where the concrete first-paid contract actually requires them.

## 22.23 OPS-UPD-007 disposition

```text
OPS-UPD-007 =
  WORKING PRE-JIT CANDIDATE RESOLUTION CONVERGED

root issue =
  Safety & Eligibility can establish `general_wellness_only` before a
  participant can actually exercise any Product-approved bounded choice.
  Starting a participant deadline from the internal eligibility timestamp
  would consume choice time before the choice is genuinely available.

resolution =
  if a bounded Product choice exists, its clock starts only when the complete
  current governed choice is durably available and exercisable.
  eligibility/notification/read/Analytics/UI timestamps are not clock authority.

important non-expansion =
  current source snapshots do not themselves define a General Wellness
  choice-window duration or universal option set.
  this pass does not create either.

recommended authority level =
  Product Law semantic clarification where the concrete choice window is governed

Architecture amendment required =
  NO

Domain Map amendment required =
  NO

new Domain required =
  NO

new OPS-UPD =
  0

new OPS-GAP =
  0

independent review =
  DEFERRED UNTIL COMPLETE PRE-JIT ARTIFACT

compression =
  DEFERRED UNTIL AFTER INDEPENDENT REVIEW
```

## 22.24 Substantive upstream-delta convergence status

All seven previously identified upstream classes now have a substantive working disposition:

```text
OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT
OPS-UPD-005 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-006 = WORKING CANDIDATE RESOLUTION CONVERGED
              SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES
OPS-UPD-007 = WORKING CANDIDATE RESOLUTION CONVERGED
```

This does **not yet** mean Pre-JIT is complete.

The next required substantive pass is a **cross-delta / final convergence audit** over the complete working artifact.

That audit must determine whether the seven dispositions:

- contradict each other;
- create accidental duplicate authority;
- leave a lifecycle hole between Commerce / Entitlements / Safety / Plans / Privacy / Operations;
- create any unowned durable truth;
- create hidden implementation commitments;
- create a new upstream question that genuinely cannot fit an existing OPS-UPD;
- or require correction before independent review.

Only after that audit is clean should the artifact be labelled substantively Pre-JIT complete and handed to an independent hostile reviewer.

## 22.25 Updated workstream state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 310
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 330
CONTIGUOUS PT COVERAGE = OPS-PT-001...330

OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT
OPS-UPD-005 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-006 = WORKING CANDIDATE RESOLUTION CONVERGED
              SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES
OPS-UPD-007 = WORKING CANDIDATE RESOLUTION CONVERGED

OPEN SUBSTANTIVE OPS-UPD DISPOSITION PASSES = 0
NEW OPS-UPD = 0
NEW OPS-GAP = 0

PRE-JIT =
  NOT YET DECLARED COMPLETE
  PENDING FINAL CROSS-DELTA / CONVERGENCE AUDIT

GITHUB / PR / ACTIONS = DEFERRED
INDEPENDENT HOSTILE REVIEW = AFTER CLEAN FINAL CONVERGENCE AUDIT
COMPRESSION = AFTER CLEAN INDEPENDENT REVIEW
IMPLEMENTATION = NOT AUTHORISED

NEXT SUBSTANTIVE PASS =
  FINAL CROSS-DELTA / PRE-JIT CONVERGENCE AUDIT
```


---

# 23. v0.25.0 — Final cross-delta / Pre-JIT convergence audit

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.24.0 BYTES PRESERVED UNCHANGED**  
> **FINAL AUTHORING-SIDE CROSS-DELTA AUDIT — NOT THE LATER INDEPENDENT HOSTILE REVIEW**  
> **VERDICT: CHANGES REQUIRED**  
> **ONE ROOT BLOCKER FOUND — EXISTING OPS-UPD-007 REOPENED; NO OPS-UPD-008**  
> **OPS-UPD-001...006: CROSS-DELTA CONVERGENCE CLEAN SUBJECT TO ALREADY-NAMED DOWNSTREAM GATES**  
> **NEW CROSS-DELTA PRESSURE TESTS: OPS-PT-331...350**  
> **PRE-JIT: NOT YET SUBSTANTIVELY COMPLETE**  
> **GITHUB / PR / ACTIONS REMAIN DEFERRED**  
> **IMPLEMENTATION NOT AUTHORISED**

## 23.1 Maintenance and provenance

This successor preserves the complete v0.24.0 file byte-for-byte and appends only the final authoring-side convergence audit.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.24.0.md

predecessor SHA-256 =
  6f78064aa633211aec14ca47c08bdc58df2bdde8de36038d687497e42f12be37

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 23.2 Audit purpose

This pass does not attempt to make each individual delta sound internally plausible.

It asks the harder whole-artifact questions:

```text
Do the seven working dispositions contradict each other?

Does any durable business truth have zero owners or multiple owners?

Do refunds, entitlements, pilot admission, assessment consumption,
plan fulfilment, safety routing, deletion and operator commands compose
without a lifecycle hole?

Did any earlier pass defer a Product decision that another pass quietly
assumes has already been made?

Did the working artifact accidentally turn a UI timestamp, provider event,
Analytics event, queue state or Audit record into business authority?

Did any pressure-test resolution smuggle in implementation detail or a new
Domain that current law does not justify?

Can the complete artifact now be handed to an independent hostile reviewer
without requiring that reviewer to guess missing Product semantics?
```

The last question currently answers **NO** because of one bounded Product-level gap described below.

## 23.3 Cross-delta ownership matrix

The combined ownership model is coherent once the OPS-UPD-001 release/admission seam is made explicit:

| Durable truth / consequence | Authoritative owner | Cross-delta note |
|---|---|---|
| commercial product / pilot saleability and authorised current stage ceiling | Commerce | cross-functional release sign-off authorises movement; Audit records evidence but does not own the stage |
| participant-specific pilot admission / counted exposure lineage | Entitlements | one external participant counts at most once; deletion must not turn historical exposure into reusable capacity |
| payment obligation, collection, excess collection, refund/dispute/reconciliation | Commerce | OPS-UPD-002 |
| product access / assessment or Plan right / consumable credit | Entitlements | OPS-UPD-002, 004, 005 |
| assessment attempt/result/report | Temperament | OPS-UPD-004 |
| current safety/eligibility route | Safety & Eligibility | OPS-UPD-005, 007 |
| health facts | Health Records | Safety consumes; does not duplicate |
| generated/delivered Plan lineage | Plans & Nutrition | OPS-UPD-005 |
| deletion/export lifecycle and suppression orchestration | Privacy & Consent | OPS-UPD-006 |
| identity, role/capability and authentication assurance | Identity & Access | OPS-UPD-003 |
| minimised immutable governance/security evidence | Audit & Evidence | never business authority |
| provider/worker execution state | mechanism only | never becomes durable business authority |
| operator Work / dashboards / Analytics / notifications | projection/evidence only | never becomes durable business authority |

No new Operations, Support, Admin, Pilot, Refund, Timer, Choice, Export Archive or Plan Intent Domain is justified.

## 23.4 OPS-UPD-001 ownership seam — converged without new upstream law

OPS-UPD-001 originally put the participant-specific admission/access right in Entitlements and saleability in Commerce.

The final audit makes the split explicit:

```text
Commerce
→ owns current commercial product lifecycle / pilot saleability
→ owns the authorised current stage ceiling as governed offer/release config

Entitlements
→ owns each participant's admission/access lineage
→ owns whether that lineage has already consumed one counted external-exposure slot

cross-functional Product/Clinical/Technical release authorities
→ authorise stage expansion / stop / rollback under Product Law
→ do not become a separate data-owning Domain

Audit & Evidence
→ records the release decision/sign-off evidence
→ is not the stage/cap authority
```

This uses existing Domain Law; it is not a new Product capability.

### Deletion interaction

A participant who has crossed the counted-admission boundary remains part of the historical first-pilot exposure budget even after Full Deletion.

That does **not** require retaining a reconstructable participant estate.

The later Privacy/JIT contract must preserve a deletion-safe, minimised representation sufficient to prevent the slot from being reused while still satisfying approved deletion/retention law.

Exact representation remains under the existing Privacy/retention gates.

This is a downstream representation question, not a new upstream delta.

## 23.5 Clean cross-delta compositions

### 23.5.1 Admission × payment remediation

```text
one real admitted participant
+ duplicate genuine collection
→ one counted pilot exposure
→ one valid entitlement consequence
→ excess collection returned
→ pilot slot does not reopen
```

Refund/remediation does not rewrite the fact that a real participant was exposed to the pilot.

### 23.5.2 Admission × assessment-credit lifecycle

```text
participant admitted
+ assessment credit claimed
+ attempt expires without paid delivery
→ same assessment credit returns available_unused
→ pilot admission remains counted
→ no second participant admission created
```

Assessment retryability and pilot exposure are separate dimensions.

### 23.5.3 Admission × Plan change-of-intent

```text
participant admitted
+ Plan intent v1 superseded by v2 before first fulfilment
→ same unfulfilled Plan right
→ one eventual first fulfilment
→ same single pilot admission
```

Generation retries do not create additional pilot exposure.

### 23.5.4 Operator commands × all business owners

OPS-UPD-003 composes cleanly with every other delta:

```text
operator action
→ current actor authority
→ owning Domain action
→ owning Domain invariant
→ durable evidence
```

No operator screen directly edits:

- pilot count;
- payment truth;
- entitlement/credit truth;
- Safety outcome;
- Plan history;
- deletion/export state.

### 23.5.5 Payment remediation × Full Deletion

A Full Deletion request does not cancel a genuine unresolved financial make-whole obligation.

Commerce may retain/reconcile the minimum financial record required by approved retention/legal authority while:

```text
deleted participant access
remains deleted
```

The retained finance/reconciliation record cannot restore identity, entitlements or product history.

This composes OPS-UPD-002 and OPS-UPD-006 without conflict.

### 23.5.6 Export × Full Deletion × operator work

Support may assist through the governed Privacy export/deletion pathway.

Closing the Support work item:

```text
≠ export completed
≠ deletion completed
```

Privacy & Consent remains completion authority.

## 23.6 Root blocker — paid Plan disposition under `general_wellness_only`

The final audit found a lifecycle hole at the OPS-UPD-005 × OPS-UPD-007 seam.

Current working semantics say:

```text
once-off Plan right
→ remains unfulfilled until successful first fulfilment

eligible_automated
→ personalised Plan may fulfil the paid Plan obligation

professional_review_required
→ prohibited automated generation does not consume the paid Plan right

insufficient_information
→ paid Plan right remains unfulfilled

general_wellness_only
→ General Wellness is the permitted safe pathway
```

But the working artifact never answers:

```text
Does delivery/acceptance of General Wellness
FULFIL / CONSUME
the paid once-off Plan entitlement?

OR

Does the paid Plan entitlement remain unfulfilled?

OR

Does Product Law give the participant a bounded election among
specific commercial/access outcomes?
```

The source Product material also does not safely answer that question.

It establishes both:

```text
paid offer:
  one safe seven-day personalised Plan when eligible
```

and:

```text
core MVP:
  personalised seven-day Plan OR governed General Wellness fallback
```

and:

```text
general_wellness_only:
  only General Wellness Starter Pathway is permitted
```

Those statements are compatible at the safety-routing level, but they do not define the **commercial / entitlement consequence** of the fallback.

This is Product Law, not an implementation detail.

## 23.7 Why OPS-UPD-007 v0.24.0 is not sufficient to close the blocker

v0.24.0 correctly established the conditional invariant:

```text
if an approved bounded participant choice exists,
its clock cannot start before the complete choice is durably exercisable
```

That remains valid.

But a clock-start rule cannot close a Product contract whose other essential dimensions are still unknown:

```text
does the choice exist?
who receives it?
what are the options?
what happens to the paid Plan entitlement under each option?
does General Wellness fulfil the paid obligation?
is any refund/credit permitted?
does professional review form part of an option?
what is the expiry consequence?
which Domain owns the durable election/window state?
what happens if Safety changes during the window?
```

Without those answers, `choice_available_at` is only a conditional design invariant.

It is not enough to certify OPS-UPD-007 as a completed upstream disposition.

## 23.8 Durable-owner consequence of the blocker

The unresolved Product option set also prevents final ownership assignment.

If the future election is principally:

```text
keep/release/consume a paid Plan right
```

the durable election may naturally belong with Entitlements.

If it is principally:

```text
refund / credit / commercial remedy
```

Commerce may own the authoritative commercial transition.

If it creates a genuinely mixed cross-domain Product lifecycle, Product Law / JIT must identify one orchestrating owner and keep the other Domain consequences subordinate.

The audit must not choose among these before Product semantics are known.

Therefore:

```text
unowned universal Timer/Choice Resource = REJECTED

conditional clock-start invariant = RETAINED

final durable owner =
  BLOCKED on Product definition of the actual election/consequence
```

This is not evidence for a new Domain.

## 23.9 Required OPS-UPD-007 Product adjudication

OPS-UPD-007 is reopened at the existing identifier.

No `OPS-UPD-008` is created.

The Product-owner adjudication must answer, at minimum:

### A. Paid right disposition

For a purchaser whose current authoritative route is `general_wellness_only` before first Plan fulfilment:

```text
what happens to the paid once-off Plan right?
```

The answer must explicitly say whether General Wellness:

- fulfils/consumes it;
- leaves it unfulfilled;
- or participates in a defined participant election.

### B. Option set, if an election exists

If there is a participant election, define the exact Product-approved options.

Do not infer:

- cash refund;
- store credit;
- future personalised Plan;
- professional review;
- complimentary entitlement;
- General Wellness acceptance;

unless Product explicitly approves them.

### C. Duration and expiry, if bounded

If the election is time-bounded, define:

- duration;
- elapsed/calendar/business-day semantics;
- expiry consequence;
- outage/degradation treatment;
- Safety-change treatment;
- manual exception authority, if any.

The v0.24 clock-start invariant should remain:

```text
start only when the complete current governed choice
is durably available and exercisable
```

### D. Ownership

After A–C are known, assign the durable election state to the existing Domain that owns the principal business consequence.

No new Domain should be created unless the Product decision reveals genuinely independent durable business meaning that no current Domain can own.

## 23.10 Existing downstream gates remain downstream

The following are **not** reasons to block semantic Pre-JIT convergence once OPS-UPD-007 is adjudicated:

- OQ-004 provider refund/reconciliation mechanics;
- OPS-UPD-004 repository promotion / exact-head proof;
- OQ-029 retention matrix;
- OQ-030 external processor deletion inventory;
- OQ-031 backup restore/deletion replay;
- OQ-032 export/deletion operations;
- OQ-033 professional-record authority;
- exact MFA/step-up mechanics;
- exact database locks/indexes/idempotency keys;
- exact worker/queue names;
- exact UI components;
- GitHub / PR / Actions proof.

Those remain correctly placed later.

## 23.11 Cross-delta pressure tests — OPS-PT-331...350

| PT | Cross-delta scenario | Required outcome | Audit result |
|---|---|---|---|
| `OPS-PT-331` | Final pilot slot receives duplicated/reordered provider callbacks for one purchase | One payment effect, one entitlement, one counted admission | PASS |
| `OPS-PT-332` | One logical purchase is genuinely collected twice and the participant is already admitted | Excess collection is remediated; valid access remains singular; counted pilot exposure remains one | PASS |
| `OPS-PT-333` | Participant receives duplicate-collection remediation/refund after admission | Financial correction does not reopen a first-pilot slot | PASS |
| `OPS-PT-334` | Approved complimentary/goodwill access is granted by Support while current pilot ceiling is already exhausted | OPS-UPD-003 cannot bypass OPS-UPD-001; owning admission/access policy rejects a new external admission | PASS |
| `OPS-PT-335` | Counted pilot participant later completes Full Deletion | Participant estate/access deletes; historical exposure budget is not reusable; deletion-safe representation remains under existing Privacy/retention gate | PASS WITH EXISTING DOWNSTREAM GATE |
| `OPS-PT-336` | Admitted participant's paid assessment attempt expires after first answer without complete delivery | Same assessment credit returns `available_unused`; admission count does not change | PASS |
| `OPS-PT-337` | Assessment purchase is genuinely double-collected and attempt later succeeds | One valid assessment right/consumption; excess collection remediated; no duplicate admission | PASS |
| `OPS-PT-338` | Admitted participant changes initial Plan intent repeatedly before first delivery | Same Plan right and admission lineage; at most one qualifying first Plan fulfilment | PASS |
| `OPS-PT-339` | Unfulfilled paid Plan routes to `general_wellness_only` | Safety routing is clear, but paid Plan entitlement disposition is undefined | **BLOCKED — OPS-UPD-007 PRODUCT ADJUDICATION REQUIRED** |
| `OPS-PT-340` | General Wellness content is successfully delivered to a paid Plan purchaser | Working artifact cannot determine whether that delivery consumes/fulfils the paid Plan right | **BLOCKED — SAME ROOT ISSUE** |
| `OPS-PT-341` | A future bounded General Wellness election is shown | Clock-start invariant is known, but option set/expiry consequence/principal durable owner are undefined until Product adjudication | **BLOCKED — SAME ROOT ISSUE** |
| `OPS-PT-342` | Support tries to force stale personalised Plan delivery after current Safety route becomes General Wellness | Current Safety wins; operator authority cannot bypass it | PASS |
| `OPS-PT-343` | Full Deletion executes while duplicate-payment make-whole remains unresolved | Minimum lawful Commerce reconciliation may continue without restoring participant/product access | PASS WITH EXISTING RETENTION/LEGAL GATE |
| `OPS-PT-344` | Export/deletion work and payment remediation are concurrently pending | Privacy owns export/deletion completion; Commerce owns money remediation; neither completion fabricates the other | PASS |
| `OPS-PT-345` | Chargeback/refund occurs after counted pilot admission | Commerce/Entitlements reconcile current access according to law; historical pilot exposure slot remains consumed | PASS |
| `OPS-PT-346` | Release stage is rolled back below the already-counted historical exposure count | No new admissions until authorised ceiling safely permits them; rollback does not silently rewrite historical exposure | PASS |
| `OPS-PT-347` | Operator edits a dashboard/configuration attempting to reset pilot count | Projection/command surface cannot rewrite authoritative Commerce/Entitlements truths | PASS |
| `OPS-PT-348` | Full Deletion removes participant identifiers but pilot cap still needs monotonic exposure accounting | Preserve only the approved minimised/deletion-safe release-accounting truth; exact representation remains Privacy/JIT | PASS WITH EXISTING DOWNSTREAM GATE |
| `OPS-PT-349` | Analytics says 9 admitted while authoritative lineages show 10 | Analytics is corrected; it cannot authorise an 11th participant | PASS |
| `OPS-PT-350` | Whole-artifact owner review after OPS-UPD-001...007 | All durable truths have an owner except the conditional General Wellness election/window, whose principal consequence is not yet Product-defined | **BLOCKED — SAME OPS-UPD-007 ROOT ISSUE** |

Cross-delta result:

```text
20 tests executed conceptually
16 PASS
2 PASS WITH EXISTING DOWNSTREAM GATE
4 BLOCKED
1 root blocker
0 new upstream classes
```

The four blocked scenarios are manifestations of the same unresolved Product contract, not four separate gaps.

## 23.12 Contradiction audit

### OPS-UPD-001 × OPS-UPD-002

PASS.

Payment remediation does not alter historical pilot exposure.

### OPS-UPD-001 × OPS-UPD-006

PASS WITH EXISTING PRIVACY/RETENTION GATE.

Deletion must not resurrect capacity, but the representation must remain minimised and non-reconstructive.

### OPS-UPD-002 × OPS-UPD-004

PASS.

Duplicate money and assessment-credit consumption are independent dimensions:

```text
one logical commercial obligation
→ one lawful retained amount
→ one assessment credit
→ consume only on complete assessment delivery
```

### OPS-UPD-003 × all other deltas

PASS.

Operator authority never becomes owner authority.

### OPS-UPD-004 × OPS-UPD-005

PASS.

Assessment and Plan fulfilment are separate product-right lifecycles.

### OPS-UPD-005 × OPS-UPD-007

**CHANGES REQUIRED.**

Safety routing is coherent.

Paid Plan entitlement/commercial disposition under `general_wellness_only` is not.

### OPS-UPD-006 × financial retention

PASS WITH EXISTING LEGAL/RETENTION GATE.

Retained financial obligations cannot restore deleted participant access.

## 23.13 Hidden implementation-commitment audit

No blocking premature implementation choice was found in OPS-UPD-001...006.

The working artifact correctly leaves downstream:

- tables/Resources;
- indexes;
- transaction isolation/locking;
- Redis/ETS/GenServer choices;
- queue/worker names;
- idempotency-key representation;
- exact MFA implementation;
- object-store/link mechanics;
- exact deletion/export deadlines;
- exact audit schema.

`choice_available_at` in OPS-UPD-007 must remain a **semantic label**, not a mandated column/Resource.

No implementation may materialise it until the Product election itself is defined.

## 23.14 Historical stale-status audit

Because this is an append-only artifact, earlier sections still contain historical statements such as:

```text
OPS-UPD-004 = CONFLICT_STOP
OPS-UPD-001 = DO NOT START
COMPRESSION = NOT READY pending repository proof
```

Those statements remain valid evidence of the earlier sequence but are not the controlling current Pre-JIT workflow after the user-directed sequence reset in v0.19.0.

The controlling working sequence remains:

```text
finish substantive Pre-JIT semantics
→ final convergence
→ independent hostile review
→ corrections/re-review if needed
→ compression
→ only then repository/GitHub/Actions integration
```

This audit does not erase the historical text.

## 23.15 Final authoring-side convergence verdict

```text
VERDICT =
  CHANGES REQUIRED

BLOCKERS =
  1 root Product blocker

BLOCKER =
  OPS-UPD-007 — General Wellness / paid Plan disposition

WHY BLOCKING =
  the complete first-paid participant journey cannot be specified without
  knowing what happens to the paid Plan right when current Safety permits
  General Wellness but not a personalised Plan.

NOT A BLOCKER =
  GitHub / Actions / exact-head proof
  provider mechanics
  deletion/export operational mechanics
  retention schedule detail
  implementation schema
  independent review itself

NEW OPS-UPD =
  0

OPS-UPD-008 =
  DO NOT CREATE

PRE-JIT SUBSTANTIVE COMPLETION =
  NOT YET

INDEPENDENT HOSTILE REVIEW =
  NOT YET
```

The artifact is **not** ready to enter independent hostile review because the reviewer would have to invent Product semantics to close this lifecycle.

## 23.16 Required next pass

The next pass stays inside the existing upstream register:

```text
NEXT =
  OPS-UPD-007 PRODUCT ADJUDICATION

REQUIRED DECISION =
  define the paid Plan entitlement/commercial consequence of
  `general_wellness_only` before first Plan fulfilment

THEN =
  complete the General Wellness election/window contract if one exists
  → re-run the affected cross-delta pressure tests
  → re-run final convergence audit

ONLY IF CLEAN =
  declare substantive Pre-JIT complete
  → independent hostile review
```

No repository work is required for this next pass.

## 23.17 Updated workstream state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 330
NEW CROSS-DELTA PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 350
CONTIGUOUS PT COVERAGE = OPS-PT-001...350

OPS-UPD-001 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT
OPS-UPD-005 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-006 = WORKING CANDIDATE RESOLUTION CONVERGED
              SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES
OPS-UPD-007 = REOPENED / PRODUCT ADJUDICATION REQUIRED

NEW OPS-UPD = 0
NEW OPS-GAP = 0

FINAL CROSS-DELTA AUDIT =
  CHANGES REQUIRED

PRE-JIT =
  NOT YET SUBSTANTIVELY COMPLETE

GITHUB / PR / ACTIONS =
  DEFERRED

INDEPENDENT HOSTILE REVIEW =
  BLOCKED UNTIL OPS-UPD-007 ADJUDICATION + CLEAN RE-AUDIT

COMPRESSION =
  BLOCKED UNTIL CLEAN INDEPENDENT REVIEW

IMPLEMENTATION =
  NOT AUTHORISED

NEXT SUBSTANTIVE PASS =
  OPS-UPD-007 PRODUCT ADJUDICATION —
  GENERAL WELLNESS / PAID PLAN ENTITLEMENT DISPOSITION
```


---

# 24. v0.26.0 — OPS-UPD-007 Product adjudication + targeted convergence re-audit

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.25.0 BYTES PRESERVED UNCHANGED**  
> **OPS-UPD-007 PRODUCT ADJUDICATION COMPLETED IN WORKING PRE-JIT**  
> **GENERAL WELLNESS DOES NOT FULFIL OR CONSUME THE PAID PERSONALISED-PLAN RIGHT**  
> **NO BOUNDED GENERAL-WELLNESS CHOICE WINDOW IS AUTHORISED FOR THE CURRENT FIRST-PAID MVP**  
> **V0.24 CLOCK-START RULE RETAINED ONLY AS A CONDITIONAL FUTURE INVARIANT**  
> **TARGETED CROSS-DELTA RE-AUDIT: PASS**  
> **NEW PRESSURE TESTS: OPS-PT-351...370**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **SUBSTANTIVE PRE-JIT: COMPLETE / READY FOR INDEPENDENT HOSTILE REVIEW**  
> **GITHUB / PR / ACTIONS REMAIN DEFERRED**  
> **IMPLEMENTATION NOT AUTHORISED**

## 24.1 Maintenance and provenance

This successor preserves the complete v0.25.0 file byte-for-byte and appends only the OPS-UPD-007 Product adjudication and the required targeted convergence re-audit.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.25.0.md

predecessor SHA-256 =
  35e6ec4df9cf596b88706f4abe39f2b5ad853ba9274ca8e6cd493a0303c1d8b9

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 24.2 Product-law evidence controlling the adjudication

The current source law establishes all of the following:

```text
Product 2 =
  7-Day Personalised Plan

Product 2 is available only when:
  temperament provenance is sufficient
  required health/safety onboarding is complete
  participant is eligible for the relevant automated pathway

paid core bundle includes:
  one safe seven-day personalised Plan when eligible

general_wellness_only =
  only the General Wellness Starter Pathway is permitted

core MVP loop =
  eligibility
  → personalised seven-day Plan OR General Wellness

Plan refund =
  available before Plan generation

professional review =
  separate paid service / not automatically included

bundles =
  decompose into explicit component entitlements
```

These rules do **not** support treating General Wellness as though it were the purchased personalised Plan.

The smallest coherent adjudication is therefore:

```text
General Wellness
≠ paid 7-Day Personalised Plan fulfilment

General Wellness delivery/use
≠ Plan entitlement consumption

general_wellness_only
→ blocks personalised Plan generation now
→ does not destroy the purchased Plan right
```

## 24.3 Product adjudication — paid Plan disposition under `general_wellness_only`

For a participant who owns an unfulfilled once-off Plan entitlement and whose current authoritative Safety outcome is:

```text
general_wellness_only
```

the working Product rule is:

1. **No personalised Plan is generated or delivered.**
2. **The approved General Wellness Starter Pathway may be made available where current Product/Safety rules permit.**
3. **General Wellness does not fulfil, redeem or consume the paid 7-Day Personalised Plan entitlement.**
4. **The paid Plan entitlement remains active/unfulfilled.**
5. **No second Plan purchase is required merely because current Safety temporarily or persistently blocks automated personalisation.**
6. **If current authoritative eligibility later becomes `eligible_automated`, the same still-valid unfulfilled Plan entitlement may fund exactly one first qualifying personalised-Plan fulfilment.**
7. **If the participant instead obtains an authoritative pre-generation Plan refund, the refunded Plan right closes/revokes through the existing Commerce → Entitlements consequence.**
8. **Completed Full Deletion permanently ends the remaining Plan access/right under existing deletion law.**
9. **No expiry through inactivity or passage of time is invented by this adjudication.**

This is the Product-level answer to the blocker found in v0.25.0.

## 24.4 Why General Wellness cannot consume the Plan right

Treating General Wellness as Plan fulfilment would contradict the shape of the approved commercial product:

```text
7-Day Personalised Plan
```

is explicitly available only to a participant eligible for the relevant automated pathway.

General Wellness is intentionally constrained educational/wellness guidance that excludes the prohibited personalised-plan behaviours for affected Safety states.

Therefore:

```text
safe fallback value
does not become
commercial equivalence with the personalised Plan
```

merely because both appear in the same end-to-end MVP journey.

This avoids:

- silently substituting a different product for a paid personalised Plan;
- marking an entitlement consumed by an output Safety law says is not the Plan;
- forcing a participant to repurchase if later eligibility legitimately changes;
- creating hidden refund/credit semantics.

## 24.5 No special first-paid General Wellness choice window

The convergence blocker arose partly because v0.24 treated a possible participant election conditionally.

This Product adjudication resolves the current MVP more simply:

```text
CURRENT FIRST-PAID MVP:
  no special bounded General-Wellness commercial choice window
```

The participant does not have to make a timed election merely because current eligibility is `general_wellness_only`.

Instead:

```text
General Wellness
→ available where Product/Safety rules permit

paid Plan entitlement
→ remains unfulfilled

ordinary pre-generation Plan refund
→ remains separately available under DEC-045
```

No special timer, expiry consequence, credit election or professional-review election is added.

Therefore the current MVP needs no durable `Choice`, `Timer` or `Election` business truth.

## 24.6 Status of the v0.24 clock-start invariant

The v0.24 rule remains logically correct but is **not active current-MVP Product behaviour**.

Retained future invariant:

```text
IF a future Product amendment explicitly creates a bounded participant election,
THEN its clock starts only when the complete current governed choice
is durably available and actually exercisable.
```

It still must not start from:

- internal eligibility timestamps;
- notification provider state;
- read/open telemetry;
- Analytics;
- stale UI;
- operator queue state.

For the current first-paid MVP:

```text
choice window = NOT AUTHORISED / NOT APPLICABLE
choice_available_at = no required current durable business truth
```

## 24.7 Ordinary refund remains independent

DEC-045 already governs Plan refund timing:

```text
before Plan generation
→ ordinary Plan refund remains available

after Plan generation
→ ordinary refund boundary closes
```

Under `general_wellness_only`:

```text
no personalised Plan generation is permitted
```

therefore General Wellness access/use does **not** cross the Plan-generation refund boundary.

Consequently:

```text
participant may use/receive General Wellness
without silently losing
the still-unfulfilled Plan's ordinary pre-generation refund eligibility
```

subject to applicable statutory rights and the authoritative Commerce refund transition.

This is not a new exceptional refund.

It is the existing pre-generation Plan refund rule applied consistently.

## 24.8 Refund versus retain-right — not a timed election

The participant may, while the Plan remains ungenerated and otherwise valid:

```text
retain the unfulfilled Plan right
OR
request the ordinary permitted Plan refund
```

This does not create a Product `choice window`.

There is no special countdown and no automatic outcome merely because the participant does nothing.

If she retains the right:

```text
General Wellness may continue where permitted
Plan right stays unfulfilled
current Safety is re-evaluated before any future personalisation
```

If the authoritative Plan refund completes:

```text
Commerce
→ owns refund/commercial truth

Entitlements
→ closes/revokes the corresponding Plan right

later automated eligibility
→ cannot use the refunded right
→ a new qualifying purchase/grant would be required
```

Exact provider refund mechanics remain under OQ-004.

## 24.9 `professional_review_required` remains separate

This adjudication does not bundle a practitioner service into the once-off Plan.

If current eligibility becomes:

```text
professional_review_required
```

then:

- automated personalised Plan generation remains prohibited;
- the existing unfulfilled Plan right is not consumed by the prohibition;
- General Wellness may remain available only where current Safety/Product law permits;
- professional review remains a separately governed and separately priced service when that product is active.

No automatic conversion of a Plan purchase into professional review is authorised.

## 24.10 `insufficient_information` remains separate

If current outcome is:

```text
insufficient_information
```

then:

```text
personalised Plan generation = blocked
Plan right = unfulfilled
```

The participant must complete/clarify the required information before current eligibility can permit generation.

No General Wellness timer or automatic Plan consumption is inferred.

## 24.11 Later eligibility change

If a participant remains on General Wellness and later provides new/corrected facts such that current Safety becomes:

```text
eligible_automated
```

then before generation:

- current inputs are re-read/revalidated;
- the same existing unfulfilled Plan entitlement is checked;
- any stale prior General Wellness/safety projection is ignored;
- exactly one first personalised Plan may be generated/delivered;
- successful first fulfilment consumes/fulfils the Plan right according to OPS-UPD-005.

General Wellness history does not count as an earlier Plan version.

## 24.12 Bundle handling

Current Product/Domain law already says bundles grant explicit component entitlements.

Therefore an Assessment + Plan Bundle contains conceptually separate rights:

```text
assessment component
plan component
```

A `general_wellness_only` outcome affects the Plan component.

It does not automatically refund, revoke or recreate the assessment component.

Examples:

### Assessment unused

```text
assessment credit = follows assessment law
Plan entitlement = active/unfulfilled
General Wellness = safe fallback where permitted
```

### Assessment already consumed/delivered

```text
assessment component = already fulfilled under its own law
Plan component = still unfulfilled under general_wellness_only
```

The two lifecycles remain independent.

## 24.13 Discounted bundle refund allocation

The current launch bundle is discounted relative to separate list prices.

If a participant is entitled to refund the still-ungenerated Plan component of a discounted bundle, the runtime must **not invent** the refundable rand amount from:

- current standalone list price;
- naive subtraction;
- equal split;
- proportional allocation;
- operator discretion.

The safe Commerce rule is:

```text
every versioned bundled offer containing independently refundable components
must define and preserve its component refund allocation/rule
as part of the accepted commercial offer/order truth
```

The exact launch-rand allocation is **not selected in this Pre-JIT artifact**.

Before the Assessment + Plan Bundle may be sold to real paid participants, Commerce/Product release configuration must define that allocation and prove the refund path.

This is an existing paid-pilot refund-readiness obligation, not:

- a new Domain;
- a new OPS-UPD;
- a new OQ identifier;
- or a reason to invent a runtime pricing formula.

If the allocation is absent:

```text
affected bundle sale = NO-GO
```

until refund behaviour is defined.

## 24.14 Ownership after adjudication

No ownership hole remains.

### Safety & Eligibility

Owns:

- current route (`eligible_automated`, `general_wellness_only`, etc.);
- whether personalised automation is currently permitted.

### Entitlements

Owns:

- the Plan component right;
- whether it remains active/unfulfilled;
- its eventual fulfilment/consumption;
- its closure/revocation following authoritative refund/deletion consequence.

### Commerce

Owns:

- Plan/bundle commercial offer;
- versioned bundle refund allocation;
- refund request/outcome;
- payment/provider reconciliation.

### Plans & Nutrition

Owns:

- actual personalised Plan generation/delivery lineage once authorised.

### Content & Media / applicable owner

Supplies governed General Wellness content/pathway.

General Wellness content access does not become Entitlements' Plan-consumption truth.

### Analytics / Communications / Work

Remain projections/evidence only.

No `Choice`/`Timer` owner is needed for the current MVP because no bounded election exists.

## 24.15 Interaction with OPS-UPD-005

OPS-UPD-005 now composes without ambiguity:

```text
unfulfilled paid Plan
+ eligible_automated
→ one qualifying first personalised fulfilment may occur

unfulfilled paid Plan
+ general_wellness_only
→ no personalised fulfilment
→ General Wellness may be used
→ Plan right remains unfulfilled

unfulfilled paid Plan
+ professional_review_required
→ no automated personalised fulfilment
→ Plan right remains unfulfilled

unfulfilled paid Plan
+ insufficient_information
→ generation blocked
→ Plan right remains unfulfilled
```

Only successful qualifying personalised-Plan fulfilment consumes the once-off Plan right unless another explicit future Product amendment says otherwise.

## 24.16 Interaction with OPS-UPD-002

If the original Plan purchase was genuinely double-collected:

```text
one valid Plan commercial obligation
→ one valid Plan entitlement

general_wellness_only
→ does not consume it

duplicate collection
→ excess money still remediated under OPS-UPD-002
```

A later Plan refund must reconcile with prior duplicate-collection remediation so the payer is neither under- nor over-refunded.

## 24.17 Interaction with OPS-UPD-003

Support may:

- explain the current Safety route;
- help the participant understand that the Plan remains unfulfilled;
- initiate permitted refund/support workflows where authorised.

Support may not:

- mark General Wellness as Plan fulfilment;
- consume the Plan entitlement;
- backdate a fictional choice window;
- create an ad hoc bundle refund amount;
- bypass current Safety to generate a personalised Plan.

## 24.18 Interaction with OPS-UPD-006

Completed Full Deletion remains a true terminal boundary:

```text
active/unfulfilled Plan entitlement
→ deleted/ended according to deletion law

retained financial record
→ may remain only where law requires
→ cannot restore the Plan right
```

A prior General Wellness pathway does not alter that rule.

## 24.19 Targeted re-test of v0.25 blockers

The four previously blocked convergence cases are now resolved:

### Historical `OPS-PT-339`

```text
unfulfilled paid Plan
→ general_wellness_only
```

Outcome:

```text
General Wellness permitted where governed
Plan right remains active/unfulfilled
```

**RE-AUDIT: PASS**

### Historical `OPS-PT-340`

General Wellness is successfully delivered/used.

Outcome:

```text
no Plan entitlement consumption
no personalised Plan fulfilment
ordinary pre-generation Plan refund boundary remains uncrossed
```

**RE-AUDIT: PASS**

### Historical `OPS-PT-341`

The previous hypothetical bounded choice is no longer part of the current MVP adjudication.

Outcome:

```text
no current-MVP choice window
no timer/election durable owner required

future explicit bounded election
→ v0.24 availability-start invariant applies
```

**RE-AUDIT: PASS**

### Historical `OPS-PT-350`

Whole-artifact ownership review.

Outcome:

```text
all current durable business truths have an existing owner
no conditional current-MVP choice/timer truth remains
```

**RE-AUDIT: PASS**

## 24.20 OPS-PT-351...370

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-351` | Standalone Plan purchaser becomes `general_wellness_only` before any personalised generation | General Wellness may be offered; paid Plan right remains active/unfulfilled | PASS |
| `OPS-PT-352` | Participant completes/uses General Wellness content | General Wellness use does not consume or fulfil the paid personalised-Plan entitlement | PASS |
| `OPS-PT-353` | Months later current Safety changes from `general_wellness_only` to `eligible_automated` and no refund/deletion occurred | Same unfulfilled Plan right may fund one qualifying first personalised Plan after current revalidation | PASS |
| `OPS-PT-354` | Participant requests ordinary Plan refund while still `general_wellness_only` and no personalised Plan was generated | DEC-045 pre-generation refund path remains available; authoritative refund closes the Plan right through Commerce → Entitlements | PASS |
| `OPS-PT-355` | Participant used General Wellness before requesting the Plan refund | General Wellness use does not cross the personalised Plan generation/refund boundary | PASS |
| `OPS-PT-356` | Bundle participant has not used assessment credit and becomes `general_wellness_only` | Assessment credit follows assessment law independently; Plan component stays unfulfilled | PASS |
| `OPS-PT-357` | Bundle participant already completed the assessment and then becomes `general_wellness_only` | Assessment stays fulfilled; Plan component remains separately unfulfilled/refundable before generation | PASS |
| `OPS-PT-358` | Discounted bundle lacks a versioned component refund allocation | No ad hoc amount may be invented; affected real-paid bundle sale is NO-GO until Commerce/Product config defines refund allocation | PASS |
| `OPS-PT-359` | Participant remains `general_wellness_only` and takes no refund action for an extended period | No special choice-window expiry; no inactivity-based Plan expiry is invented | PASS |
| `OPS-PT-360` | Participant never opens General Wellness | Plan right remains unfulfilled; no timer/read telemetry changes it | PASS |
| `OPS-PT-361` | Safety stays `general_wellness_only` indefinitely | Personalised generation stays blocked; Plan right remains unfulfilled unless refund, deletion or another explicit terminal law occurs | PASS |
| `OPS-PT-362` | Safety changes from `general_wellness_only` to `professional_review_required` | Automated Plan remains blocked; Plan right unfulfilled; professional review is not silently bundled | PASS |
| `OPS-PT-363` | Safety changes to `insufficient_information` | Generation remains blocked; Plan right remains unfulfilled pending valid clarification/re-evaluation | PASS |
| `OPS-PT-364` | Safety changes to `eligible_automated`, but a stale General Wellness page remains open | Current Safety + Entitlement are re-read; stale page cannot block or authorise Plan generation | PASS |
| `OPS-PT-365` | After later eligibility, duplicate generation workers race on the same retained Plan right | At most one qualifying first personalised Plan fulfils the entitlement | PASS |
| `OPS-PT-366` | Participant begins refund flow, provider outcome is ambiguous, then Safety becomes `eligible_automated` | Commerce/Entitlements current state must reconcile before irreversible personalised fulfilment; implementation must not guess whether the right remains spendable | PASS |
| `OPS-PT-367` | Plan refund completes, then participant later becomes `eligible_automated` | Refunded/closed Plan right cannot generate a Plan; new qualifying purchase/grant required | PASS |
| `OPS-PT-368` | Full Deletion completes while retained Plan right is still unfulfilled | Plan right ends permanently under deletion law; finance retention cannot restore it | PASS |
| `OPS-PT-369` | Support operator tries to mark the Plan entitlement consumed because General Wellness was delivered | Rejected; General Wellness is not Plan fulfilment and Support does not own entitlement truth | PASS |
| `OPS-PT-370` | Final owner/convergence review after adjudication | Safety owns routing, Entitlements owns Plan right, Commerce owns refund/offer allocation, Plans owns fulfilment; no Timer/Choice Domain/truth required | PASS |

All 20 new tests pass under the adjudicated working semantics.

## 24.21 Targeted final convergence re-audit

The v0.25 blocker is resolved.

### OPS-UPD-005 × OPS-UPD-007

PASS.

```text
first personalised Plan fulfilment
→ consumes/finally fulfils the once-off Plan right

General Wellness fallback
→ does not
```

### OPS-UPD-002 × OPS-UPD-007

PASS.

Duplicate/excess money remediation remains separate from whether the valid Plan right is still unfulfilled.

### OPS-UPD-003 × OPS-UPD-007

PASS.

Operator assistance never becomes Safety, Entitlement or Commerce authority.

### OPS-UPD-006 × OPS-UPD-007

PASS WITH EXISTING LEGAL/RETENTION GATES.

Deletion terminates the unfulfilled right without allowing retained finance to resurrect access.

### OPS-UPD-001 × OPS-UPD-007

PASS.

A participant routed to General Wellness has still crossed the pilot exposure boundary if already admitted; retaining/refunding the Plan component does not reopen pilot capacity.

## 24.22 New issue check

This adjudication does **not** create a new upstream class.

The discounted-bundle refund allocation is a concrete Commerce/Product offer configuration required before first-paid sale because refund behaviour must be defined.

It does not require a new `OPS-UPD` because the governing semantics are now clear:

```text
component is independently refundable before its cutoff
→ offer version must preserve the approved refund allocation
```

Exact rand values belong to the final commercial configuration/release contract.

Therefore:

```text
NEW OPS-UPD = 0
NEW OPS-GAP = 0
OPS-UPD-008 = DO NOT CREATE
```

## 24.23 Smallest eventual Product / Decision clarification

The working upstream wording for later governed compression is:

```text
The General Wellness Starter Pathway is a safe fallback and does not itself
fulfil, redeem or consume a purchased 7-Day Personalised Plan entitlement.

Where a participant owns an unfulfilled Plan entitlement but current Safety
returns `general_wellness_only`, no personalised Plan may be generated.
General Wellness may remain available where Product/Safety rules permit, while
the Plan entitlement remains unfulfilled.

If current authoritative eligibility later permits automated personalisation,
the same still-valid unfulfilled Plan entitlement may produce one qualifying
first personalised Plan after current-state revalidation.

General Wellness access/use does not cross the ordinary Plan refund boundary.
Until personalised Plan generation occurs, the existing pre-generation Plan
refund remains available under the approved refund rules. A completed refund
closes the corresponding Plan right through the normal Commerce-to-Entitlements
consequence.

The current first-paid MVP has no special bounded General-Wellness commercial
choice window and no inactivity-based expiry of the unfulfilled Plan right.
Any future bounded election requires an explicit Product amendment; if one is
created, its clock begins only when the complete current governed choice is
durably available and exercisable.

For discounted bundles, every offer version containing independently refundable
components must define and preserve the approved component refund allocation
before sale. Runtime code and operators may not invent the allocation.
```

No new DEC identifier is invented here.

## 24.24 Architecture / Domain disposition

No Architecture amendment is required.

Existing mechanisms already support:

- current Safety reads;
- entitlement authority;
- Commerce refund transitions;
- bundle component entitlements;
- idempotent fulfilment;
- fail-closed ambiguity;
- immutable Plan lineage.

No Domain Map amendment is required.

Existing owners are sufficient.

No new General Wellness, Choice, Timer, Refund or Operations Domain is justified.

## 24.25 Final authoring-side Pre-JIT convergence verdict

```text
VERDICT =
  PASS

OPS-UPD-001 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-002 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-003 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-004 =
  SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT

OPS-UPD-005 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-006 =
  WORKING CANDIDATE RESOLUTION CONVERGED
  SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES

OPS-UPD-007 =
  SEMANTICALLY ADJUDICATED / CONVERGED IN WORKING PRE-JIT

OPEN SUBSTANTIVE OPS-UPD =
  0

NEW OPS-UPD =
  0

NEW OPS-GAP =
  0

UNOWNED DURABLE BUSINESS TRUTH =
  0 FOUND

NEW DOMAIN REQUIRED =
  NO

NEW ARCHITECTURE MECHANISM REQUIRED =
  NO

PRE-JIT SUBSTANTIVE COMPLETION =
  PASS

INDEPENDENT HOSTILE REVIEW =
  NEXT REQUIRED STAGE

COMPRESSION =
  NOT YET — ONLY AFTER CLEAN INDEPENDENT REVIEW

GITHUB / PR / ACTIONS =
  DEFERRED UNTIL AFTER REVIEW + COMPRESSION

IMPLEMENTATION =
  NOT AUTHORISED
```

## 24.26 Updated pressure-test state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 350
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 370
CONTIGUOUS PT COVERAGE = OPS-PT-001...370

HISTORICAL BLOCKED CROSS-DELTA CASES
OPS-PT-339 = RESOLVED BY v0.26.0 ADJUDICATION
OPS-PT-340 = RESOLVED BY v0.26.0 ADJUDICATION
OPS-PT-341 = RESOLVED BY v0.26.0 ADJUDICATION
OPS-PT-350 = RESOLVED BY v0.26.0 ADJUDICATION

FINAL AUTHORING-SIDE CONVERGENCE AUDIT =
  PASS

PRE-JIT =
  SUBSTANTIVELY COMPLETE
  READY FOR INDEPENDENT HOSTILE REVIEW

GITHUB / PR / ACTIONS =
  DEFERRED

COMPRESSION =
  DEFERRED UNTIL CLEAN INDEPENDENT REVIEW

IMPLEMENTATION =
  NOT AUTHORISED

NEXT STAGE =
  INDEPENDENT HOSTILE / ADVERSARIAL REVIEW OF COMPLETE PRE-JIT ARTIFACT
```


---

# 25. v0.27.0 — Independent hostile / adversarial review of complete Pre-JIT artifact

> **INDEPENDENT REVIEW STAGE A**  
> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.26.0 BYTES PRESERVED UNCHANGED**  
> **REVIEW MODE: BREAK THE MODEL; DO NOT REPAIR IN THIS PASS**  
> **VERDICT: CHANGES REQUIRED**  
> **BLOCKING FINDINGS: 2**  
> **NON-BLOCKING CORRECTIONS: 2**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **NO NEW OPS-PT ADDED BY REVIEW**  
> **PRE-JIT SUBSTANTIVE COMPLETION CLAIM: WITHDRAWN PENDING REPAIR + FRESH RE-REVIEW**  
> **COMPRESSION: BLOCKED**  
> **GITHUB / PR / ACTIONS: DEFERRED**  
> **IMPLEMENTATION: NOT AUTHORISED**

## 25.1 Review protocol

This pass intentionally did **not** continue authoring from the v0.26 conclusions.

It reviewed the complete append-only artifact adversarially against the current supplied Product / Decision / Domain / Roadmap snapshots.

The review asked:

```text
Can an invariant be false in a scenario the artifact itself marks PASS?

Can a participant enter a paid state with no defined lawful exit?

Does any “downstream configuration” actually decide customer money
and therefore require Product/Commercial authority?

Does a later adjudication really close earlier cross-delta gaps?

Does any current claim rely on a stale projection, operator role,
provider event or audit evidence as authority?

Did the artifact call itself complete while retaining a material
customer-right or release-integrity ambiguity?
```

Per the Stage-A protocol, this section records findings only.

It does not repair them and does not certify any proposed fix.

## 25.2 Review verdict

```text
VERDICT =
  CHANGES REQUIRED

BLOCKERS =
  2

NEW OPS-UPD =
  0

NEW OPS-GAP =
  0

REPAIR IN THIS REVIEW PASS =
  PROHIBITED / NOT PERFORMED

PRE-JIT =
  NOT READY FOR COMPRESSION

NEXT =
  SEPARATE CORRECTION PASS
  → THEN FRESH INDEPENDENT HOSTILE RE-REVIEW
```

## 25.3 Blocking finding 1 — OPS-UPD-001 stage-ceiling invariant contradicts rollback semantics

The current OPS-UPD-001 candidate declares:

```text
counted participants <= authorised stage ceiling

reserved-but-not-counted capacity
+ counted admissions still consuming first-pilot budget
<= authorised stage ceiling
```

But the same candidate also marks as PASS:

```text
stage paused/rolled back at 18 counted participants
→ preserve all 18 historical exposures
→ stop new admissions
```

and the later cross-delta audit explicitly pressure-tests:

```text
release stage rolled back below the already-counted historical exposure count
→ preserve the historical count
→ no new admissions
```

Those propositions cannot all be simultaneously true if `authorised stage ceiling`
is allowed to become lower than the historical count.

Example:

```text
historical counted exposure = 18
rolled-back authorised stage ceiling = 10

then:
18 <= 10
is false
```

### Source-law problem

Current Product Law describes:

- deliberate expansion toward approximately 10 → 25 → 50; and
- rollback as scoped stop / disable / limited-capability actions.

The supplied source does **not** establish that rollback means rewriting the numeric cumulative exposure ceiling downward below already-exposed participants.

### Why blocking

This is not cosmetic terminology.

The model currently conflates at least two independent dimensions:

```text
cumulative authorised / historical exposure accounting
and
current admission-open / stop / rollback state
```

Until those are coherently distinguished, JIT cannot know which state is authoritative for:

- admission;
- rollback;
- re-entry;
- reservation arithmetic;
- invariant enforcement;
- stage reporting.

A database or policy implementation could otherwise faithfully encode an impossible invariant.

### Required repair surface

Stay inside `OPS-UPD-001`.

Do **not** create a new upstream delta.

The correction pass must explicitly reconcile:

- numeric stage ceiling semantics;
- historical cumulative exposure count;
- stop/rollback state;
- re-entry behaviour;
- the two current arithmetic invariants;
- historical `OPS-PT-227`;
- historical `OPS-PT-346`.

The repair must be checked against Product Law's actual rollback modes rather than inventing a numeric rollback model.

## 25.4 Blocking finding 2 — post-generation Safety invalidation can strand a paid Plan with no defined customer remedy

OPS-UPD-005 correctly distinguishes:

```text
after generation but before successful delivery:
  first fulfilment = no
  ordinary Plan refund = already closed by DEC-045
  purchased Plan obligation = still owed
  Plan entitlement remains available until successful delivery
```

It also correctly pressure-tests:

```text
Safety-relevant fact changes after generation but before delivery
→ stale personalised Plan must not be delivered
→ Safety re-evaluation wins
→ entitlement is not consumed
```

and:

```text
current eligibility becomes general_wellness_only or professional_review_required
before delivery
→ no unsafe automated personalised Plan
→ purchased Plan right not consumed
```

v0.26 then adjudicates the easier case where `general_wellness_only` exists
**before any personalised Plan generation**:

```text
General Wellness does not consume the Plan right
ordinary pre-generation refund remains available
```

That does **not** resolve the harder sequence:

```text
T1 participant is eligible_automated
T2 personalised Plan is generated
   → DEC-045 ordinary refund boundary closes
T3 before successful delivery, new/corrected Safety truth arrives
T4 current route becomes general_wellness_only
   OR professional_review_required
   OR another route that prohibits delivery
T5 stale generated Plan cannot lawfully be delivered
```

The working artifact then has:

```text
Plan entitlement = unfulfilled
ordinary refund = closed
stale Plan delivery = prohibited
General Wellness = not Plan fulfilment
professional review = separate paid service
```

If eligibility never returns, the participant can remain indefinitely in a state where:

- NewYou still owes the purchased Plan obligation;
- NewYou is prohibited from delivering the generated Plan;
- the entitlement cannot be consumed;
- the ordinary refund has already closed;
- General Wellness cannot discharge the obligation;
- professional review cannot be silently substituted.

### Why blocking

This is a customer-right / commercial-obligation deadlock.

It is exactly the kind of gap Pre-JIT must resolve before implementation agents can act safely.

An implementation agent cannot decide whether the correct remedy is:

- reopening/refunding the Plan;
- a specific safety-failure refund exception;
- a credit;
- preservation of the obligation until eligibility returns;
- another Product-approved discharge path;
- or some combination with time/notice rules.

Those are Product / Commercial semantics, not JIT mechanics.

### Required repair surface

Stay within the existing `OPS-UPD-005` + `OPS-UPD-007` cross-delta surface.

Do **not** create `OPS-UPD-008` merely because the gap was found during independent review.

The correction pass must explicitly adjudicate at least:

```text
what happens when personalised Plan generation has already occurred,
but current Safety later prohibits first delivery?

does DEC-045 remain absolute in that safety-invalidated case?

if ordinary refund remains closed, what lawful Product obligation/remedy
prevents indefinite stranded value?

does the answer differ for:
  general_wellness_only
  professional_review_required
  insufficient_information
  temporary vs durable safety restriction?

how does the outcome affect standalone Plan vs discounted bundle?

what authoritative transition closes or preserves the Plan entitlement?
```

No repair answer is selected in this review pass.

## 25.5 Non-blocking correction 1 — discounted bundle refund allocation remains an explicit unresolved commercial release gate

v0.26 correctly identifies that the R549 Assessment + Plan Bundle is discounted and that a partial component refund cannot be invented from:

- current standalone price;
- equal split;
- proportional split;
- naive subtraction;
- operator discretion.

It also correctly states:

```text
affected bundle sale = NO-GO
until refund behaviour is defined
```

The independent review agrees that runtime code must not invent the amount.

However, the compression/repaired artifact must be precise about status:

```text
the component allocation RULE is working Product/Commerce semantics

the actual approved launch allocation/value is still unresolved
commercial release configuration

it must be approved before first-paid bundle sale
```

This is not currently treated as a third Pre-JIT blocker because:

- the artifact already fails closed on bundle sale;
- the durable owners are known;
- the missing value is explicitly routed to Product/Commerce release configuration.

But if the repair to Blocking Finding 2 uses a refund/credit consequence after generation,
the bundle allocation may become directly material to that Product adjudication and must be revisited.

## 25.6 Non-blocking correction 2 — append-only historical states must not survive compression as competing current truth

The artifact intentionally preserves earlier states such as:

```text
OPS-UPD-004 = CONFLICT_STOP
OPS-UPD-001 = DO NOT START
earlier convergence PASS/CHANGES REQUIRED states
older GitHub sequencing
```

That is appropriate historical evidence in the append-only working control document.

It is dangerous in the later compressed governed artifact if copied without status selection.

The future compression pass must:

- preserve provenance/history separately where required;
- emit only the final reviewed semantic state as current authority candidate;
- not merge superseded lifecycle tables or obsolete “next step” instructions into live law;
- make all retained downstream gates explicit.

This is a compression discipline issue, not a current semantic blocker.

## 25.7 Areas that survived hostile review

The following areas did **not** produce a new blocking finding in this Stage-A pass:

### OPS-UPD-002 — duplicate genuine collection

The separation remains coherent:

```text
one commercial obligation
→ at most one lawful retained amount
→ excess genuine collection remediated

one intended purchase
→ one valid entitlement consequence
```

Chargeback/refund/reversal reconciliation is correctly treated as Commerce truth.

### OPS-UPD-003 — consequential human commands

The owner boundary remains sound:

```text
operator intent
→ current authority check
→ owning Domain command
→ owner invariants
```

No universal Super Admin / Support / Operations write authority was introduced.

### OPS-UPD-004 — assessment-credit semantics

Within the accepted working Product adjudication, the distinction remains coherent:

```text
first answer
→ hold/claim, not consume

complete paid digital assessment delivery
→ consume

expired undelivered nontechnical attempt
→ same credit returns available_unused
```

The repository-promotion/exact-head evidence remains deliberately deferred by the user-directed sequence and was not treated as a semantic review blocker here.

### OPS-UPD-006 — export then Full Deletion

The distinction remains coherent:

```text
participant-held lawful downloaded copy
≠ platform-controlled live/recovery authority
```

Existing legal/privacy/processor/restore gates remain real and correctly downstream.

### OPS-UPD-007 — General Wellness before any Plan generation

The v0.26 adjudication is coherent for the pre-generation case:

```text
General Wellness
≠ personalised Plan fulfilment

no Plan generation
→ Plan right remains unfulfilled
→ ordinary pre-generation Plan refund remains available
```

The blocker is specifically the **post-generation / pre-delivery Safety invalidation** path, not this pre-generation rule.

## 25.8 Review coverage summary

The Stage-A hostile review pressure-tested the complete artifact across:

```text
authority hierarchy
Domain ownership
pilot-cap arithmetic
release / rollback
payment / refund / dispute
assessment-credit lifecycle
Plan generation / delivery / refund
Safety re-evaluation
General Wellness
bundle component entitlements
human operator commands
export / deletion / restore
historical append-only state
downstream gate discipline
```

Result:

```text
BLOCKING FINDINGS = 2

1. OPS-UPD-001:
   numeric stage-ceiling invariant contradicts rollback-below-count semantics

2. OPS-UPD-005 × OPS-UPD-007:
   post-generation Safety invalidation can create an unfulfilled,
   undeliverable, ordinarily non-refundable paid Plan obligation

NON-BLOCKING CORRECTIONS = 2

1. discounted-bundle component allocation must remain explicit unresolved
   Product/Commerce release configuration until approved

2. historical append-only states must be cleaned during later compression

NEW UPSTREAM CLASS = 0
NEW DOMAIN = 0
NEW ARCHITECTURE MECHANISM = 0
```

## 25.9 Independent-review certification status

```text
STAGE A HOSTILE REVIEW =
  CHANGES REQUIRED

v0.26 PRE-JIT SUBSTANTIVE COMPLETION CLAIM =
  WITHDRAWN

INDEPENDENT CERTIFICATION =
  NOT GRANTED

COMPRESSION =
  BLOCKED

REPOSITORY / GITHUB / ACTIONS =
  STILL DEFERRED

IMPLEMENTATION =
  NOT AUTHORISED
```

Per the review protocol, no same-pass repair is performed.

## 25.10 Required next sequence

```text
1. separate correction pass:
   repair Blocking Finding 1 inside OPS-UPD-001

2. same correction pass or bounded second correction pass:
   Product-adjudicate Blocking Finding 2 inside the existing
   OPS-UPD-005 / OPS-UPD-007 surface

3. re-run only the materially affected authoring/cross-delta tests

4. perform a NEW independent hostile/adversarial review
   of the corrected complete artifact

5. only if that review is clean:
   proceed to compression

6. only after reviewed compression:
   resume repository / GitHub / Actions integration
```

No compression or repository promotion is authorised by this v0.27 review.


---

# 26. v0.28.0 — Separate correction pass for Stage-A hostile-review blockers

> **WORKING / NON-AUTHORITATIVE**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.27.0 BYTES PRESERVED UNCHANGED**  
> **CORRECTION PASS ONLY — NOT AN INDEPENDENT RE-REVIEW**  
> **STAGE-A BLOCKER 1: REPAIRED IN OPS-UPD-001 CANDIDATE SEMANTICS**  
> **STAGE-A BLOCKER 2: REPAIRED IN OPS-UPD-005 × OPS-UPD-007 CANDIDATE SEMANTICS**  
> **NEW PRESSURE TESTS: OPS-PT-371...390**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **V0.27 CHANGES-REQUIRED REVIEW REMAINS HISTORICAL EVIDENCE**  
> **PRE-JIT CERTIFICATION: NOT YET RESTORED — FRESH HOSTILE RE-REVIEW REQUIRED**  
> **COMPRESSION: BLOCKED UNTIL CLEAN RE-REVIEW**  
> **GITHUB / PR / ACTIONS: DEFERRED**  
> **IMPLEMENTATION: NOT AUTHORISED**

## 26.1 Maintenance and provenance

This successor preserves the complete v0.27.0 file byte-for-byte and appends only the corrections required by the Stage-A hostile review.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.27.0.md

predecessor SHA-256 =
  3e0d2511cf17faeaf0071ff66790669379424cbd99fbf9426d2d063fc5c345bf

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 26.2 Correction discipline

This pass repairs only the two blockers recorded in v0.27.0.

It does not:

- reopen clean OPS-UPD-002 / 003 / 004 / 006 semantics;
- invent `OPS-UPD-008`;
- compress the append-only history;
- claim independent certification;
- inspect GitHub / PR / Actions;
- select implementation schemas, Ash actions, workers, indexes or lock primitives.

The corrected candidate must undergo a **fresh independent hostile review** before compression.

# 26A. BLOCKER 1 REPAIR — PILOT CEILING / ROLLBACK SEMANTICS

## 26.3 Root correction — numeric admission ceiling and rollback gate are independent dimensions

The v0.19 OPS-UPD-001 candidate incorrectly allowed the phrase:

```text
stage rollback below the already-counted exposure
```

to coexist with:

```text
counted participants <= authorised stage ceiling
```

The repaired semantics distinguish:

### A. Effective cumulative admission ceiling

The exact current numeric maximum of cumulative real-participant admission exposure that may be admitted under the latest cross-functionally authorised release decision.

It remains bounded by the Product progression:

```text
initial decision
→ ceiling <= 10

after required review
→ ceiling may be raised toward <= 25

after next required review
→ ceiling may be raised toward <= 50

hard first-pilot maximum
→ 50
```

A review may authorise an intermediate ceiling such as 15, 18, 20 or 23.

### B. New-admission gate

A separate current release-control dimension answering:

```text
may any new protected pilot admission occur now?
```

Conceptually:

```text
open
or
stopped
```

Exact implementation/state names remain JIT.

Safety/technical rollback may immediately close this gate.

### C. Historical cumulative exposure

The already-counted real-participant exposure lineage remains monotonic for the first pilot.

Rollback does not erase it.

## 26.4 Corrected rollback rule

A scoped rollback / stop:

```text
closes the new-admission gate
```

It does **not**, by itself:

- lower the numeric effective cumulative admission ceiling;
- rewrite historical exposure;
- revoke valid participant rights;
- reopen used pilot capacity;
- create a replacement slot.

Example:

```text
counted exposure = 18
effective cumulative admission ceiling = 25
new-admission gate = OPEN

technical/safety rollback occurs

then:

counted exposure = 18
effective cumulative admission ceiling = 25
new-admission gate = STOPPED
```

The invariant remains true:

```text
18 <= 25
```

and no participant 19 may be admitted because the gate is stopped.

This matches Product Law's rollback model of scoped stop/disable/limited-capability action rather than treating rollback as a retroactive numeric rewrite.

## 26.5 Explicit numeric ceiling change is a separate release decision

A later Product/Commercial + Clinical/Safety + Technical/Operations governed release decision may supersede the exact cumulative admission ceiling.

That is distinct from an emergency stop.

A newly authorised ceiling must satisfy:

```text
historical counted exposure
+ protected reserved-but-not-counted capacity
<= newly authorised effective cumulative admission ceiling
<= applicable reviewed progression maximum
<= 50
```

Therefore:

```text
counted = 18
protected reservations = 0

new authorised ceiling = 20
→ valid if the required review authority permits up to that level

new authorised ceiling = 17
→ invalid
```

A lower ceiling than an earlier historical ceiling may be explicitly authorised only if it remains at or above already committed exposure/capacity.

Historical release decisions remain auditable; current authority is the latest valid release decision.

## 26.6 Re-entry

Re-entry after a stop requires the existing recorded remediation/re-entry criteria and all applicable authorities.

Re-entry may:

```text
reopen new admissions under the still-current ceiling
```

or:

```text
approve a new exact cumulative ceiling
then reopen admissions
```

It is never implied merely because the underlying technical capability recovered.

## 26.7 Corrected pilot-cap invariants

Replace the overloaded v0.19 interpretation with:

```text
historical counted exposure
+ protected reserved-but-not-counted capacity
<= effective cumulative admission ceiling

effective cumulative admission ceiling
<= currently authorised progression-band maximum
<= 50

new admission is allowed only when:
  new-admission gate = OPEN
  AND
  the resulting committed exposure remains <= effective cumulative admission ceiling

one real participant lineage
→ counted at most once

refund / withdrawal / safety pause / deletion
→ does not reduce historical counted exposure

rollback / emergency stop
→ may close admissions immediately
→ does not by itself rewrite the numeric ceiling

stale projections
→ cannot authorise admission

ambiguous admission/cap authority
→ fail closed
```

Exact database representation is still JIT.

No generic inventory system is justified.

## 26.8 Historical test corrections

### Historical `OPS-PT-227`

Earlier wording:

```text
Stage is paused/rolled back at 18 counted participants
```

Correct interpretation:

```text
counted = 18
current authorised cumulative ceiling remains whatever valid ceiling
was already in force (for example 25)
new-admission gate closes immediately
historical 18 remain counted
```

**CORRECTED RESULT: PASS**

### Historical `OPS-PT-346`

Earlier wording allowed:

```text
release stage rolled back below the already-counted historical exposure count
```

That numeric interpretation is superseded.

Correct interpretation:

```text
rollback closes new admissions;
it does not set a numeric ceiling below committed exposure.

Any later explicit ceiling supersession must remain >= counted + protected reservations.
```

**CORRECTED RESULT: PASS**

# 26B. BLOCKER 2 REPAIR — POST-GENERATION SAFETY INVALIDATION / FAILED FULFILMENT

## 26.9 Root distinction — ordinary refund cutoff versus safety-invalidated failed fulfilment

DEC-045's generation cutoff continues to govern the **ordinary Plan refund** case.

The hostile-review blocker is a different case:

```text
participant was eligible_automated
→ personalised Plan was generated
→ no qualifying first delivery occurred
→ current Safety truth changes
→ current Safety now prohibits any qualifying automated personalised Plan delivery
```

This is not an ordinary change-of-mind refund.

It is a **safety-invalidated failed-fulfilment case**.

The repaired working Product rule is:

> **Generation may close the ordinary refund window, but it does not authorise NewYou to retain payment indefinitely where current Safety later prohibits the first paid Plan from ever being lawfully delivered under the current state.**

## 26.10 Safety-invalidated failed-fulfilment remedy

Where all of the following are true:

1. a valid paid Plan right exists;
2. a personalised Plan was generated;
3. no qualifying first personalised Plan was successfully delivered;
4. the generated snapshot is no longer lawfully deliverable under current Safety/Eligibility authority; and
5. current authority does not permit a qualifying replacement personalised Plan at that moment;

the participant has two governed Product paths:

### Path A — retain the Plan right

```text
Plan entitlement
→ remains active / unfulfilled / unconsumed

unsafe/stale generated snapshot
→ remains historical evidence
→ cannot be delivered as current

General Wellness
→ may remain available where permitted
→ does not consume the Plan right

later eligible_automated
→ same still-valid Plan right may fund one qualifying first personalised Plan
```

No inactivity expiry or forced election window is invented.

### Path B — request a safety-invalidated failed-fulfilment refund

This is an explicit **non-ordinary refund exception** to the generation cutoff.

If the authoritative refund completes:

```text
Commerce
→ records/refunds the authoritative refundable Plan-component amount

Entitlements
→ closes/revokes the affected Plan right

later eligibility
→ cannot use the refunded right
→ new qualifying purchase/grant required
```

This refund is not evidence that the original generation never happened.

The generated snapshot remains historical while retained under normal Plan/deletion rules.

## 26.11 When the exception does not apply

A generated Plan becoming stale does not automatically create a refund exception.

If new/corrected information changes the required generation inputs but current Safety still permits a qualifying automated personalised Plan:

```text
eligible_automated remains current
→ stale snapshot is not delivered
→ same Plan right regenerates/replaces safely
→ ordinary post-generation refund boundary remains closed
```

This preserves the existing corrections/safety-replacement model.

The exceptional failed-fulfilment refund applies when current authority blocks **qualifying personalised first fulfilment**, not merely when a regeneration is required.

## 26.12 Outcomes covered by the safety-invalidated remedy

The remedy applies where current Safety/Eligibility authority after generation makes qualifying personalised first delivery impermissible, including as applicable:

```text
general_wellness_only
professional_review_required
insufficient_information
another governed restriction that blocks automated personalised delivery
```

`insufficient_information` does not force a refund.

The participant may retain the right and complete/clarify information.

But the Product may not make “you can never receive or refund the paid right” the only state merely because generation happened earlier.

No automated refund is required.

No timed election is created.

## 26.13 General Wellness remains non-substitutive

The v0.26 adjudication remains unchanged:

```text
General Wellness
≠ paid personalised Plan fulfilment
```

Therefore, after post-generation Safety invalidation:

- General Wellness may still provide safe value;
- it does not consume the Plan right;
- it does not extinguish the failed-fulfilment refund option;
- it does not become a reason to charge for a second Plan later if the original right was retained.

## 26.14 Professional review remains separate

A `professional_review_required` outcome does not convert the Plan purchase into a practitioner service.

Professional review remains separately governed/priced when active.

The participant may:

```text
retain the original Plan right pending later safe eligibility
OR
request the safety-invalidated failed-fulfilment Plan refund
```

A later practitioner outcome may change Safety authority, but does not silently rewrite the prior commercial contract.

## 26.15 Refund-race rule

A dangerous race exists if the participant requests the failed-fulfilment refund while Safety later returns to `eligible_automated`.

The Product-level invariant is:

```text
once the safety-invalidated refund request is authoritatively accepted
for execution/reconciliation,
no new personalised Plan fulfilment may consume that right
until the refund outcome is reconciled.
```

If the refund completes:

```text
right closes
```

If the refund definitively fails/is cancelled without another terminal commercial consequence:

```text
the same Plan right may return to active/unfulfilled
subject to current Safety authority
```

Exact cross-domain action/state names and transaction mechanics remain JIT.

## 26.16 Refund amount — standalone Plan

For a standalone Plan purchase, the refundable amount is the authoritative amount attributable to that accepted Plan purchase/order under its actual accepted offer/discount history.

Do not use the current list price if the participant paid a different governed amount.

Duplicate-payment remediation, prior refunds, disputes and chargebacks must reconcile before issuing another irreversible reimbursement.

## 26.17 Refund amount — Assessment + Plan Bundle

The v0.27 non-blocking bundle finding becomes directly relevant to this repair.

Bundle law already requires explicit component entitlements.

Therefore:

```text
assessment component lifecycle
≠
Plan component lifecycle
```

If the Plan component qualifies for the safety-invalidated failed-fulfilment refund:

- already-valid assessment fulfilment is not reversed merely because the Plan component is refunded;
- the refundable Plan-component amount comes from the accepted offer's approved versioned component-refund allocation;
- current standalone list price is not the allocation authority;
- operators/runtime may not invent the split.

The current first-paid Assessment + Plan Bundle may not be sold until that component-refund allocation is approved/configured and the refund behaviour is proved.

This remains a **release/configuration gate**, not a new upstream semantic class.

## 26.18 Product/Decision clarification required for eventual promotion

The eventual governed Product / Decision successor should make explicit:

```text
DEC-045 defines the ordinary Plan refund cutoff at generation.

That ordinary cutoff does not eliminate the participant's remedy where,
before first successful Plan delivery, current Safety/Eligibility authority
newly makes qualifying personalised Plan fulfilment impermissible.

In that safety-invalidated failed-fulfilment case, the participant may retain
the still-unconsumed Plan right for future lawful fulfilment or request a refund
of the authoritative Plan-component amount.

General Wellness and professional review do not substitute for or consume
the paid personalised Plan right.

If current Safety still permits a qualifying personalised Plan and only the
generated snapshot is stale, the existing right is safely regenerated/replaced;
the exceptional refund does not arise merely because regeneration is needed.

A refund request accepted for execution blocks concurrent new fulfilment of
that right until the commercial outcome is reconciled.

Discounted bundles must preserve an approved versioned component-refund
allocation before sale.
```

No new DEC identifier is invented here.

# 26C. TARGETED PRESSURE TESTS AFTER REPAIR

## 26.19 OPS-PT-371...390

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-371` | 18 counted participants, effective ceiling 25, technical rollback occurs | New-admission gate closes; ceiling remains 25; 18 historical exposures remain; no new admission | PASS |
| `OPS-PT-372` | Technical operator attempts to represent rollback by changing ceiling from 25 to 10 with 18 already counted | Reject invalid ceiling; technical stop authority closes the gate instead of creating `18 <= 10` contradiction | PASS |
| `OPS-PT-373` | After rollback, cross-functional re-entry explicitly authorises cumulative ceiling 20 with 18 counted and no reservations | Ceiling 20 is valid if within the reviewed progression band; admissions may reopen only under re-entry authority | PASS |
| `OPS-PT-374` | Cross-functional decision attempts new ceiling 17 while 18 are already counted | Reject; current numeric ceiling may never fall below committed historical exposure | PASS |
| `OPS-PT-375` | 18 counted + 2 protected reservations, ceiling 25, stop occurs | Gate closes; committed total 20 remains protected; stop itself does not rewrite ceiling or recycle reservations | PASS |
| `OPS-PT-376` | One protected reservation is lawfully released during stop | Historical count stays 18; committed reservation budget falls accordingly; no admission occurs while gate remains stopped | PASS |
| `OPS-PT-377` | First review authorises only cumulative ceiling 15 rather than 25 | Exact ceiling is 15; progression-band maximum 25 is not automatic admission authority | PASS |
| `OPS-PT-378` | Re-entry opens admissions under exact ceiling 20; participants 19 and 20 are admitted | Both may be admitted safely; participant 21 is denied until another authorised ceiling change | PASS |
| `OPS-PT-379` | Analytics/UI still says admissions open during an authoritative stop | Projection cannot override stopped gate; admission fails closed | PASS |
| `OPS-PT-380` | Cross-functional operator attempts ceiling 51 | Reject; first-pilot hard maximum 50 remains absolute | PASS |
| `OPS-PT-381` | Plan generated while eligible; before delivery current Safety becomes `general_wellness_only` | Generated Plan is not delivered; right remains unconsumed; participant may retain it or request safety-invalidated failed-fulfilment refund | PASS |
| `OPS-PT-382` | Same sequence, but current outcome becomes `professional_review_required` | No automated Plan/professional-service substitution; retain-right or failed-fulfilment refund paths remain | PASS |
| `OPS-PT-383` | Same sequence, but current outcome becomes `insufficient_information` | Delivery remains blocked; participant may clarify/retain the right or request failed-fulfilment refund; no forced timer | PASS |
| `OPS-PT-384` | New safety-relevant fact invalidates old snapshot but current outcome remains `eligible_automated` | Regenerate safely under same right; exceptional failed-fulfilment refund does not arise merely because replacement generation is needed | PASS |
| `OPS-PT-385` | Participant retains the right after post-generation `general_wellness_only`; later becomes `eligible_automated` | Same right may fund one new qualifying first personalised Plan; stale prior snapshot cannot deliver | PASS |
| `OPS-PT-386` | Participant requests failed-fulfilment refund and refund completes; later becomes `eligible_automated` | Refunded Plan right is closed; new purchase/grant required | PASS |
| `OPS-PT-387` | Failed-fulfilment refund is pending/ambiguous when Safety becomes `eligible_automated` | No new fulfilment until refund outcome reconciles; neither Commerce nor Entitlements guesses | PASS |
| `OPS-PT-388` | Participant uses General Wellness after post-generation Safety invalidation, then requests failed-fulfilment refund | General Wellness does not consume the Plan or extinguish the remedy | PASS |
| `OPS-PT-389` | Bundle assessment component is already fulfilled; Plan generated but becomes safety-invalid before delivery | Assessment remains fulfilled; Plan-component refund uses accepted offer's approved allocation; Plan right closes only after authoritative refund | PASS |
| `OPS-PT-390` | Bundle offer has no approved Plan-component refund allocation | Real paid bundle sale is NO-GO; runtime/operator cannot invent an amount | PASS |

All 20 targeted authoring tests pass under the corrected candidate semantics.

These are not an independent certification.

## 26.20 Corrected status of the two hostile-review blockers

```text
STAGE-A BLOCKER 1 =
  AUTHORING-SIDE REPAIR APPLIED
  OPS-UPD-001 ceiling / rollback dimensions separated

STAGE-A BLOCKER 2 =
  AUTHORING-SIDE REPAIR APPLIED
  post-generation Safety invalidation now has a governed failed-fulfilment remedy

INDEPENDENT RE-REVIEW =
  STILL REQUIRED

v0.27 CHANGES REQUIRED VERDICT =
  HISTORICAL AND STILL CONTROLLING FOR CERTIFICATION
  UNTIL A FRESH REVIEW PASSES
```

## 26.21 Current complete candidate state after correction

```text
CUMULATIVE PRESSURE TESTS = 390
CONTIGUOUS PT COVERAGE = OPS-PT-001...390

OPS-UPD-001 = CORRECTED CANDIDATE CONVERGED; RE-REVIEW REQUIRED
OPS-UPD-002 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-003 = WORKING CANDIDATE RESOLUTION CONVERGED
OPS-UPD-004 = SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT
OPS-UPD-005 = CORRECTED CANDIDATE CONVERGED; RE-REVIEW REQUIRED
OPS-UPD-006 = WORKING CANDIDATE RESOLUTION CONVERGED
              SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES
OPS-UPD-007 = CORRECTED / COMPOSED WITH OPS-UPD-005; RE-REVIEW REQUIRED

NEW OPS-UPD = 0
NEW OPS-GAP = 0
NEW DOMAIN = 0
NEW ARCHITECTURE MECHANISM = 0

BUNDLE COMPONENT REFUND ALLOCATION =
  REQUIRED RELEASE CONFIGURATION BEFORE REAL PAID BUNDLE SALE
  EXACT VALUE NOT INVENTED HERE

PRE-JIT CERTIFICATION =
  NOT YET RESTORED

NEXT STAGE =
  FRESH INDEPENDENT HOSTILE / ADVERSARIAL RE-REVIEW
  OF THE COMPLETE v0.28.0 CANDIDATE

COMPRESSION =
  BLOCKED UNTIL CLEAN RE-REVIEW

GITHUB / PR / ACTIONS =
  DEFERRED

IMPLEMENTATION =
  NOT AUTHORISED
```


---

# 27. v0.29.0 — Product / Commercial authority correction after independent review

> **WORKING / NON-AUTHORITATIVE UNTIL GOVERNED PROMOTION**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.28.0 BYTES PRESERVED UNCHANGED**  
> **EXPLICIT HUMAN-DIRECTED PRODUCT / COMMERCIAL ADJUDICATION**  
> **REVIEW BLOCKER 1: DEC-045 EXCEPTION NOW TREATED AS AN EXPLICIT AMENDMENT / SUPERSESSION REQUIREMENT, NOT A CLARIFICATION**  
> **REVIEW BLOCKER 2: R549 LAUNCH BUNDLE COMPONENT REFUND ALLOCATION SET TO ASSESSMENT R249 + PLAN R300**  
> **PILOT NON-BLOCKING CORRECTION: NUMERIC CEILING IS MONOTONIC WITHIN CURRENT 10 → 25 → 50 FIRST-PILOT PROGRESSION; ROLLBACK CLOSES ADMISSIONS INSTEAD OF LOWERING THE CEILING**  
> **NEW PRESSURE TESTS: OPS-PT-391...410**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **NO NEW DEC IDENTIFIER INVENTED**  
> **FORMAL PRODUCT LAW / DECISION REGISTER PROMOTION REMAINS DEFERRED UNTIL THE REVIEWED COMPRESSION / REPOSITORY STAGE**  
> **IMPLEMENTATION REMAINS NOT AUTHORISED**

## 27.1 Maintenance and provenance

This successor preserves the complete v0.28.0 file byte-for-byte and appends only the corrections requested by the latest independent reviewer.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.28.0.md

predecessor SHA-256 =
  02841277e3aa113cea12604626d5eb854825338d88a03040c8baf4df82d7bba5

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 27.2 Evaluation of the independent review

The independent review is accepted on both blocking findings.

### Accepted Blocker 1

The v0.28 wording:

```text
ordinary refund cutoff remains at generation
BUT
post-generation Safety invalidation creates a failed-fulfilment refund
```

is not merely an interpretation of locked `DEC-045`.

It changes the commercial rule.

Therefore the correction must be represented as:

```text
explicit bounded Product Law / Decision Register amendment
```

not:

```text
clarification of existing DEC-045
```

### Accepted Blocker 2

The current R549 Assessment + Plan Bundle cannot support deterministic component refunds until the accepted offer defines the component allocation.

Calling the amount “configuration” does not remove the Product/Commercial decision.

The launch allocation is therefore decided explicitly in this working Pre-JIT:

```text
Assessment component = R249
Plan component       = R300
Total bundle         = R549
Bundle saving        = R99
```

The R99 launch bundle discount is allocated entirely to the Plan component.

This is governed commercial offer data and must be preserved on the accepted offer/order.

## 27.3 Authority status of this section

The user explicitly instructed this workstream to evaluate and implement the independent review changes.

Accordingly, this section records the **intended working Product/Commercial amendment semantics** for final review.

It does not silently mutate the frozen Product Law or Decision Register snapshots.

Governance remains:

```text
current frozen source
→ preserved historically

this working amendment instruction
→ explicit proposed successor semantics

after clean independent review + compression
→ promote through explicit Product Law / Decision Register amendment/supersession
  with normal SemVer/history preservation

before that promotion
→ no implementation
```

A later JIT/implementation agent may not treat v0.29 alone as permission to bypass the governed promotion step.

# 27A. PRODUCT LAW / DECISION AMENDMENT — DEC-045 SAFETY-INVALIDATED FAILED FULFILMENT

## 27.4 Ordinary Plan refund rule remains intact

The ordinary rule remains:

```text
before personalised Plan generation
→ ordinary Plan refund available

after personalised Plan generation
→ ordinary change-of-mind Plan refund closed
```

Generation therefore remains the normal commercial cutoff.

The new rule is a **bounded exception**, not a redefinition of ordinary refunds.

## 27.5 Explicit bounded amendment

The eventual Product Law / Decision Register successor must amend or supersede the relevant part of `DEC-045` to state conceptually:

```text
Ordinary Plan refunds end after personalised Plan generation.

Exception:
If, before the first successful qualifying personalised-Plan delivery,
new or corrected authoritative Safety/Eligibility information invalidates
the generated Plan and current authority no longer permits a qualifying
personalised first fulfilment, the participant is not forced to lose the
paid Plan value merely because generation occurred earlier.

Where the blocking state qualifies under the rules below, the participant may:
  A. retain the still-unconsumed Plan entitlement for future lawful fulfilment;
  OR
  B. request a refund of the authoritative Plan-component amount.

A successful refund closes the corresponding Plan entitlement.
General Wellness and professional review do not substitute for or consume
the paid personalised Plan entitlement.
```

No new DEC number is assigned in Pre-JIT.

The eventual governed update must explicitly amend/supersede `DEC-045` rather than rewriting its historical text.

## 27.6 Outcome-specific scope

The exception is not universal for every transient Safety state.

### `general_wellness_only`

If post-generation, pre-delivery current authority becomes:

```text
general_wellness_only
```

then:

- the generated personalised Plan is non-deliverable;
- General Wellness may be available where governed;
- General Wellness does not consume the paid Plan right;
- the participant may immediately choose:
  - retain the unconsumed Plan right for possible later lawful fulfilment; or
  - request the safety-invalidated failed-fulfilment Plan refund.

No determination that the condition is “permanent” is required.

The platform may not force indefinite waiting merely because future eligibility could theoretically improve.

### `professional_review_required`

If current authority becomes:

```text
professional_review_required
```

then:

- the generated automated Plan cannot be delivered;
- professional review remains a separately governed/priced service;
- the participant is not required to purchase professional review to preserve paid value;
- the participant may immediately:
  - retain the Plan right pending a later lawful route; or
  - request the safety-invalidated failed-fulfilment Plan refund.

If the participant separately obtains professional review and later becomes lawfully eligible before refund completion, the normal refund/fulfilment race rules below apply.

### `insufficient_information`

`insufficient_information` is treated differently because it ordinarily identifies a participant-remediable information gap.

When post-generation current authority becomes:

```text
insufficient_information
```

and there is a clear current participant action required to resolve the missing/unclear information:

```text
failed-fulfilment refund exception = NOT YET ACTIVE
```

The Plan right remains unfulfilled.

The participant is given the governed clarification/completion path.

Then:

```text
clarification → eligible_automated
→ safely regenerate/replace under the same right
→ no exceptional refund

clarification → general_wellness_only
→ retain-right OR failed-fulfilment refund

clarification → professional_review_required
→ retain-right OR failed-fulfilment refund
```

If the participant has completed all currently requested clarification and the platform still cannot identify any further participant action that can produce a lawful personalised-Plan decision, the case is no longer treated as merely pending participant information.

At that point, if qualifying personalised first fulfilment remains prohibited:

```text
retain-right OR failed-fulfilment refund
```

is available.

This avoids converting a brief, actionable clarification state into an immediate post-generation refund while still preventing an indefinite no-exit state.

### `eligible_automated` with stale/invalidated snapshot

If current Safety still permits:

```text
eligible_automated
```

but the old generated snapshot is stale because the underlying inputs changed:

```text
same Plan right
→ safely regenerate / replace
→ no failed-fulfilment refund exception merely because regeneration is needed
```

The ordinary post-generation refund cutoff remains intact.

## 27.7 Other blocking Safety states

A future approved Safety outcome or restriction that prohibits qualifying personalised first fulfilment follows the same Product principle:

```text
if an included participant action can currently cure the block
→ complete that action first

if no included participant action can currently produce lawful first fulfilment
→ participant may retain the Plan right or request the failed-fulfilment refund
```

This does not authorise a JIT agent to invent new Safety outcomes.

It only defines the commercial consequence if approved current Safety authority blocks first fulfilment.

## 27.8 No automatic refund and no timed election

The exception does not create:

- automatic refund;
- automatic credit;
- a special General Wellness countdown;
- an entitlement expiry;
- a mandatory professional review;
- a mandatory wait period.

The participant may retain the right indefinitely subject to existing deletion/other terminal law.

The participant may request the exceptional refund when the qualifying conditions are met.

## 27.9 Refund / fulfilment concurrency

Once Commerce authoritatively accepts a qualifying failed-fulfilment refund request for execution/reconciliation:

```text
affected Plan right
→ cannot be consumed by a new first personalised fulfilment
until the commercial outcome is terminally reconciled
```

If refund succeeds:

```text
Commerce = refunded
Entitlements = Plan right closed/revoked
```

If refund is definitively cancelled/failed and no refund value left the platform:

```text
Plan right
→ may return to active/unfulfilled
→ current Safety must be re-read before generation/delivery
```

If provider state is ambiguous:

```text
do not refund twice
do not fulfil simultaneously
reconcile first
```

The exact cross-domain transaction/workflow mechanism remains JIT.

## 27.10 Full Deletion

If Full Deletion completes before the participant elects the failed-fulfilment refund:

```text
Plan entitlement/access
→ terminates under deletion law
```

Any already-accepted or legally surviving financial refund obligation must be reconciled from the minimum lawful Commerce evidence without reconstructing the deleted participant estate.

Privacy deletion does not silently erase an already-created money obligation.

# 27B. CURRENT R549 BUNDLE COMPONENT REFUND ALLOCATION

## 27.11 Launch allocation decision

For the current locked South African launch offer:

```text
Digital Temperament Assessment list price = R249
7-Day Personalised Plan list price        = R399
Separate list total                       = R648

Assessment + Plan Bundle accepted price   = R549
Bundle saving                             = R99
```

The approved working component allocation is:

```text
Assessment component = R249
Plan component       = R300

R249 + R300 = R549
```

Commercial interpretation:

```text
the Assessment retains its full standalone launch value
the R99 bundle saving is allocated entirely to the Plan component
```

This is the simplest deterministic launch rule because the bundle can be understood as:

```text
Assessment at R249
+ discounted Plan add-on at R300
```

No proportional/equal-split calculation is used.

## 27.12 Refund consequences for launch offer version

For the R549 launch bundle:

### Both components refundable

Where both component refund conditions are independently satisfied:

```text
Assessment refund = R249
Plan refund       = R300
Total             = R549
```

subject to any prior refund/reversal/chargeback/duplicate-collection reconciliation.

### Assessment already fulfilled, Plan refundable

```text
customer retains completed Assessment
Plan component refund = R300
```

After successful Plan refund:

```text
Assessment/report right remains according to Assessment law
Plan entitlement closes
```

### Plan fulfilled, Assessment still independently refundable before its cutoff

Where the Assessment component has not crossed its own refund cutoff:

```text
Assessment component refund = R249
customer retains fulfilled Plan
```

The participant therefore retains the bundle-discounted Plan value of R300 rather than being repriced after purchase to the R399 standalone price.

### Plan pre-generation ordinary refund

```text
Plan component refund = R300
```

for the launch bundle.

### Plan safety-invalidated failed-fulfilment refund after generation

```text
Plan component refund = R300
```

for the launch bundle.

No current standalone list price lookup is used at refund time.

## 27.13 Offer-version persistence

The accepted order must preserve the allocation that applied to the accepted offer version.

Conceptually:

```text
accepted bundle price
+ component allocation
+ discount/promotion provenance
= immutable commercial offer evidence for later partial refund
```

Future price changes do not alter historical refunds.

If a future promotional/pilot bundle price differs from R549, that offer version must explicitly define its own component allocation before sale.

Do not infer the new allocation from this R249/R300 launch split unless the future offer explicitly reuses it.

## 27.14 Commercial invariants

```text
for every refundable bundle offer:
  sum(component allocations) = accepted bundle price

component refund:
  uses accepted offer-version allocation
  not current list price

already refunded component amount:
  cannot be refunded twice

duplicate collection:
  reconciled separately before final customer-money result

fulfilled component:
  remains fulfilled unless its own governing law says otherwise

partial refund:
  must not silently reprice retained component after purchase
```

Commerce owns the offer/refund truth.

Entitlements owns the corresponding access/right consequence.

## 27.15 Bundle NO-GO status resolved for this semantic gap

The specific Pre-JIT commercial gap identified by the reviewer is now resolved for the R549 launch bundle:

```text
Assessment allocation = R249
Plan allocation       = R300
```

The bundle remains subject to normal first-paid release proof:

- payment/refund path tested;
- provider behaviour validated where required;
- duplicate collection/reimbursement safety;
- offer configuration/version preservation.

But the Product/Commercial decision itself is no longer undefined.

# 27C. PILOT NON-BLOCKING CORRECTION

## 27.16 Monotonic ceiling for current first-pilot progression

The reviewer correctly noted that v0.28 did not need to introduce a general capability for deliberately lowering an already-authorised numeric cumulative ceiling.

For the current first-pilot contract, the candidate is simplified:

```text
effective cumulative admission ceiling
→ monotonic non-decreasing within the authorised progression

initial:
  <= 10

after required review:
  may increase toward <= 25

after required review:
  may increase toward <= 50

never > 50
```

An emergency or ordinary rollback:

```text
closes the new-admission gate
```

It does not lower the cumulative numeric ceiling.

A later Product amendment could define a different release-cap model if ever required.

The current first-paid implementation does not need one.

## 27.17 Superseded v0.28 ceiling language

The v0.28 statement that:

```text
a later release decision may explicitly authorise a lower ceiling,
so long as it remains >= committed exposure
```

is no longer part of the current candidate semantics.

For this first pilot:

```text
numeric ceiling = monotonic
rollback = admission gate stop
```

Historical counted exposure remains monotonic independently.

# 27D. PRESSURE-TEST RECLASSIFICATION + NEW TESTS

## 27.18 Historical OPS-PT-381...389 status after explicit Product amendment instruction

The latest independent reviewer correctly rejected the v0.28 PASS labels because the exception had not yet been represented as an explicit Product/Decision amendment.

With v0.29, their semantic status becomes:

```text
OPS-PT-381 = PASS UNDER EXPLICIT WORKING DEC-045 AMENDMENT INSTRUCTION
OPS-PT-382 = PASS UNDER EXPLICIT WORKING DEC-045 AMENDMENT INSTRUCTION
OPS-PT-383 = SUPERSEDED BY NARROWER INSUFFICIENT_INFORMATION RULE
OPS-PT-384 = PASS
OPS-PT-385 = PASS
OPS-PT-386 = PASS UNDER EXPLICIT WORKING DEC-045 AMENDMENT INSTRUCTION
OPS-PT-387 = PASS UNDER EXPLICIT WORKING DEC-045 AMENDMENT INSTRUCTION
OPS-PT-388 = PASS UNDER EXPLICIT WORKING DEC-045 AMENDMENT INSTRUCTION
OPS-PT-389 = PASS WITH R249/R300 LAUNCH BUNDLE ALLOCATION
```

`OPS-PT-383` is not retained as originally written because v0.29 no longer grants the exceptional refund merely on entering a participant-remediable `insufficient_information` state.

## 27.19 OPS-PT-391...410

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-391` | Plan generated; before first delivery current Safety becomes `general_wellness_only` | Generated Plan cannot deliver; participant may retain unconsumed Plan right or request bounded failed-fulfilment refund | PASS |
| `OPS-PT-392` | Same sequence becomes `professional_review_required` | No forced practitioner purchase; retain-right or failed-fulfilment refund available | PASS |
| `OPS-PT-393` | Plan generated; current state becomes `insufficient_information` with one clear participant clarification still outstanding | Plan remains unfulfilled; clarification path is required first; exceptional refund not yet active solely from this temporary actionable state | PASS |
| `OPS-PT-394` | Participant completes all requested clarification; outcome becomes `eligible_automated` | Regenerate safely under same right; no exceptional refund merely because prior snapshot was invalidated | PASS |
| `OPS-PT-395` | Participant completes clarification; outcome becomes `general_wellness_only` | Retain-right or failed-fulfilment refund becomes available | PASS |
| `OPS-PT-396` | Participant completes clarification; outcome becomes `professional_review_required` | Retain-right or failed-fulfilment refund becomes available; review is not silently bundled | PASS |
| `OPS-PT-397` | All requested clarification completed but platform can identify no further participant action and still cannot lawfully permit first personalised fulfilment | Case cannot remain indefinitely stranded; retain-right or failed-fulfilment refund available | PASS |
| `OPS-PT-398` | Refund request accepted, then Safety becomes `eligible_automated` before provider outcome settles | Do not fulfil concurrently; reconcile refund first | PASS |
| `OPS-PT-399` | Accepted failed-fulfilment refund succeeds | Close Plan right; later eligibility requires new qualifying purchase/grant | PASS |
| `OPS-PT-400` | Accepted failed-fulfilment refund definitively fails before any money leaves platform | Right may return active/unfulfilled subject to current Safety; no duplicate grant | PASS |
| `OPS-PT-401` | R549 bundle, Assessment completed, Plan pre-generation refund requested | Refund R300 Plan component; retain Assessment | PASS |
| `OPS-PT-402` | R549 bundle, Assessment completed, Plan generated then safety-invalid before delivery and refund chosen | Refund R300 Plan component; retain fulfilled Assessment | PASS |
| `OPS-PT-403` | R549 bundle, Plan fulfilled while Assessment never started and Assessment refund requested within its own cutoff | Refund R249 Assessment component; retain Plan at its accepted R300 bundle allocation | PASS |
| `OPS-PT-404` | Both R549 bundle components satisfy refund conditions | Total refund cannot exceed authoritative R549 accepted order after reconciliation | PASS |
| `OPS-PT-405` | Current standalone Plan list price later changes to R449; historical R549 bundle Plan component is refunded | Refund remains R300 because accepted historical allocation is authority | PASS |
| `OPS-PT-406` | Future pilot promotion sells bundle for a different total but has no explicit component allocation | Sale is NO-GO; v0.29 R249/R300 split is not silently reused | PASS |
| `OPS-PT-407` | Duplicate genuine collection occurred on R549 bundle and later Plan-component refund is due | Commerce reconciles duplicate excess plus legitimate component refund without double reimbursement | PASS |
| `OPS-PT-408` | 18 counted participants, ceiling 25, rollback occurs | Gate closes; numeric ceiling remains 25; no new admission | PASS |
| `OPS-PT-409` | After rollback, re-entry is approved but no higher reviewed ceiling is approved | Admissions may resume only up to still-current ceiling; numeric ceiling does not decrease or increase implicitly | PASS |
| `OPS-PT-410` | Current first-pilot operator tries to lower numeric ceiling from 25 to 20 as a rollback mechanism | Reject as current pilot model; close admission gate instead | PASS |

All 20 new authoring tests pass under the v0.29 working amendment semantics.

These tests remain subject to fresh independent hostile review.

## 27.20 Reviewer-blocker disposition

```text
REVIEW BLOCKER 1 =
  PRODUCT SEMANTIC RESOLVED IN WORKING PRE-JIT

resolution form =
  EXPLICIT DEC-045 AMENDMENT / SUPERSESSION INSTRUCTION
  NOT A CLARIFICATION

ordinary refund cutoff =
  generation

bounded exception =
  post-generation / pre-first-delivery Safety invalidation
  according to the outcome-specific rules in this section

formal Product Law / Decision Register promotion =
  REQUIRED AFTER CLEAN REVIEW / COMPRESSION
  BEFORE IMPLEMENTATION

REVIEW BLOCKER 2 =
  PRODUCT / COMMERCIAL SEMANTIC RESOLVED IN WORKING PRE-JIT

R549 launch bundle allocation =
  Assessment R249
  Plan R300

future offer versions =
  must explicitly define own allocations
```

## 27.21 Current candidate state

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 390
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 410
CONTIGUOUS PT COVERAGE = OPS-PT-001...410

OPS-UPD-001 =
  CORRECTED CANDIDATE CONVERGED
  monotonic numeric ceiling + independent admission gate

OPS-UPD-002 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-003 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-004 =
  SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT

OPS-UPD-005 =
  CORRECTED CANDIDATE CONVERGED
  includes explicit Product-amendment requirement for safety-invalidated failed fulfilment

OPS-UPD-006 =
  WORKING CANDIDATE RESOLUTION CONVERGED
  SUBJECT TO EXISTING LEGAL/PRIVACY/OPERATIONS GATES

OPS-UPD-007 =
  CORRECTED / COMPOSED WITH OPS-UPD-005
  General Wellness remains non-substitutive

NEW OPS-UPD = 0
NEW OPS-GAP = 0
NEW DOMAIN = 0
NEW ARCHITECTURE MECHANISM = 0

R549 BUNDLE COMPONENT ALLOCATION =
  ASSESSMENT R249
  PLAN R300

CURRENT PRODUCT AMENDMENT REQUIREMENT =
  EXPLICITLY DEFINED
  FORMAL PROMOTION DEFERRED

PRE-JIT AUTHORING / CORRECTION STATE =
  COMPLETE CANDIDATE
  NOT YET INDEPENDENTLY CERTIFIED

NEXT STAGE =
  FRESH INDEPENDENT HOSTILE / ADVERSARIAL REVIEW
  OF COMPLETE v0.29.0 ARTIFACT

COMPRESSION =
  BLOCKED UNTIL CLEAN INDEPENDENT REVIEW

GITHUB / PR / ACTIONS =
  DEFERRED UNTIL REVIEW + COMPRESSION

IMPLEMENTATION =
  NOT AUTHORISED
```

## 27.22 Compression note

If the next independent review is clean, compression must not preserve superseded append-only candidate law as competing current truth.

In particular, the compressed current-state artifact must exclude as live normative semantics:

- old `CONFLICT_STOP` / `DO NOT START` statuses;
- older GitHub-first sequencing;
- the v0.24 hypothetical current General Wellness timer;
- rejected `close_unconsumed`;
- the overloaded pilot ceiling interpretation;
- v0.28's broader immediate `insufficient_information` refund interpretation;
- v0.28's optional downward numeric ceiling concept;
- any wording that presents the new failed-fulfilment refund as if it were already contained in historical `DEC-045`.

The compressed artifact must instead clearly label the required Product/Decision amendment for formal promotion.


---

# 28. v0.30.0 — Failed-fulfilment refund × Full Deletion lifecycle hardening

> **WORKING / NON-AUTHORITATIVE UNTIL GOVERNED PROMOTION**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.29.0 BYTES PRESERVED UNCHANGED**  
> **BOUNDED CORRECTION ONLY — OPS-UPD-005 × OPS-UPD-006 × OPS-UPD-007**  
> **LATEST REVIEW BLOCKER: RESOLVED IN WORKING PRODUCT / DECISION AMENDMENT CANDIDATE**  
> **ACCRUED FAILED-FULFILMENT REFUND REMEDY SURVIVES FULL DELETION**  
> **FULL DELETION MAY NOT SILENTLY WAIVE OR EXTINGUISH THAT ACCRUED CUSTOMER-MONEY RIGHT**  
> **NEW PRESSURE TESTS: OPS-PT-411...430**  
> **HISTORICAL OPS-PT-368 RECLASSIFIED / SUPERSEDED FOR THE ACCRUED-REMEDY CASE**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **NO NEW ARCHITECTURE MECHANISM**  
> **NO NEW DEC IDENTIFIER INVENTED**  
> **FORMAL PRODUCT LAW / DECISION REGISTER PROMOTION STILL REQUIRED AFTER CLEAN REVIEW / COMPRESSION**  
> **IMPLEMENTATION REMAINS NOT AUTHORISED**

## 28.1 Maintenance and provenance

This successor preserves the complete v0.29.0 file byte-for-byte and appends only the narrow correction requested by the latest independent reviewer.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.29.0.md

predecessor SHA-256 =
  579761ff80d02c961d3a0c7ea5864c8fb29152f970d2414c694e6923680850ae

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 28.2 Evaluation of the latest independent review

The reviewer's single blocking finding is accepted.

v0.29 correctly established:

```text
post-generation / pre-first-delivery
Safety-invalidated failed fulfilment
→ bounded refund remedy may arise
```

but it left the survival boundary too late by saying, in effect:

```text
accepted refund obligation survives deletion
```

without defining what happens when the participant has already qualified for the remedy but has not yet reached Commerce acceptance.

That is insufficient.

The correction is:

> **Once the failed-fulfilment Product conditions are authoritatively satisfied, the participant has an accrued customer-money remedy. Full Deletion may end the Plan entitlement, but it may not silently extinguish the accrued refund remedy.**

This composes with existing deletion law because:

- Full Deletion ends plans and entitlements;
- commercial/refund/dispute evidence may remain separately restricted;
- business lifecycle and data lifecycle are separate;
- deletion orchestration does not acquire Commerce ownership.

## 28.3 Scope discipline

This correction does **not** reopen:

- the R249/R300 launch bundle allocation;
- the explicit DEC-045 amendment/supersession classification;
- the v0.29 `insufficient_information` narrowing;
- General Wellness non-substitution;
- professional-review separation;
- pilot ceiling/admission semantics;
- export/deletion semantics unrelated to the refund-remedy composition.

It also does not create a generic Refund Domain.

Commerce remains money authority.

Privacy & Consent remains deletion orchestration authority.

Entitlements remains access/right authority.

# 28A. ACCRUED FAILED-FULFILMENT REFUND REMEDY

## 28.4 Qualification boundary

The failed-fulfilment refund becomes an **accrued Product/Commerce remedy** at the first authoritative instant when the v0.29 qualification conditions are satisfied.

Conceptually:

```text
valid paid Plan component exists
AND
personalised Plan was generated
AND
no qualifying first personalised Plan was successfully delivered
AND
current Safety/Eligibility state meets the v0.29 failed-fulfilment exception
AND
the case is not merely a still-actionable temporary `insufficient_information` state
=
failed-fulfilment refund remedy qualified / accrued
```

The exact Resource/field/state name remains JIT.

The Product meaning does not.

At this boundary:

- no money has necessarily moved;
- the participant has not necessarily requested the refund;
- the Plan entitlement may still be retained for future lawful fulfilment;
- but the monetary remedy now exists as a durable customer-right consequence and may not be silently erased by later data deletion.

## 28.5 Qualification is distinct from refund execution

Keep these dimensions separate:

```text
remedy qualification
≠ participant refund request/election
≠ Commerce acceptance/commitment
≠ provider settlement
≠ terminal net financial outcome
```

This prevents provider or workflow state from defining whether the participant ever had the Product remedy.

## 28.6 Conceptual refund-remedy lifecycle

Without mandating implementation state names, the Product lifecycle is:

```text
not_qualified

→ qualified_available
   accrued remedy exists;
   participant may retain Plan right or request refund

→ refund_requested
   participant has elected refund

→ refund_committed
   Commerce has accepted the valid monetary obligation for execution/reconciliation

→ settlement_pending
   provider / payment rail / reconciliation work remains

→ terminal_refunded
   authoritative refund settled

OR

→ terminal_net_satisfied
   chargeback / reversal / other governed financial outcome has already
   satisfied the amount and Commerce records the correct net result
```

A qualified remedy may also end without refund only through:

```text
successful qualifying first personalised Plan delivery
before any refund has been committed
```

because that fulfils the paid Plan obligation the remedy existed to protect.

Conceptually:

```text
qualified_available
→ participant retains right
→ later lawful first personalised Plan successfully delivered
→ remedy resolved_by_fulfilment
```

Once a refund is committed, fulfilment remains blocked until the financial outcome is reconciled.

## 28.7 Full Deletion request does not immediately force settlement

Full Deletion has a 14-day cancellation window.

Therefore:

```text
full deletion requested
≠ immediate automatic refund settlement
```

During `deletion_pending`:

- the accrued remedy remains durable;
- the Plan entitlement remains subject to the deletion flow and ordinary access revocation;
- the participant may still use an authorised verified financial/support path to elect the refund;
- cancellation of Full Deletion returns the account/deletion dimension according to existing law;
- cancellation of deletion does not cancel an independently requested/committed refund.

This avoids making a reversible deletion request itself an irreversible money event.

## 28.8 Mandatory pre-execution commercial reconciliation

Before Full Deletion executes and destroys the Plan entitlement, Privacy & Consent must obtain an authoritative Commerce/Entitlements determination for any relevant unfulfilled paid Plan component.

For the failed-fulfilment remedy specifically, the deletion pre-execution check must determine whether:

```text
no remedy ever qualified

OR

qualified remedy was resolved by successful first fulfilment

OR

qualified remedy is available / requested / committed / settlement-pending / terminal
```

Deletion may not complete by simply deleting the entitlement first and asking Commerce later whether money was still owed.

Cross-domain orchestration calls the owners; it does not become the owner.

## 28.9 Deletion execution is the final election boundary for an unelected accrued remedy

If, immediately before Full Deletion execution:

```text
failed-fulfilment remedy = qualified_available
AND
no successful qualifying first delivery occurred
AND
no terminal financial outcome already satisfied the remedy
```

then the participant's choice to retain the Plan right can no longer survive deletion, because deletion itself permanently terminates that entitlement.

Therefore:

> **Full Deletion execution automatically converts the still-unelected accrued failed-fulfilment remedy into a durable Commerce refund obligation before the Plan entitlement is destroyed.**

Conceptually:

```text
qualified_available
+ Full Deletion reaches irreversible execution boundary
→ deletion-triggered refund commitment
→ Commerce owns settlement/reconciliation
→ Entitlements may then terminate the Plan right
```

The platform does not treat deletion as a waiver/donation of the accrued remedy.

No separate participant click is required at that final boundary.

## 28.10 Refund requested but not yet accepted when deletion executes

If the participant already submitted the refund request but Commerce has not yet reached its ordinary acceptance/commitment state:

```text
refund_requested
+ deletion execution boundary
```

the request must not disappear.

Before entitlement destruction, Commerce must either:

1. confirm the qualifying accrued remedy and durably commit the refund obligation; or
2. record a genuinely authoritative reason that the remedy was never valid/already satisfied.

For a valid accrued remedy, deletion execution forces path 1.

A queue delay, worker delay or provider delay is not a reason to extinguish the request.

## 28.11 Committed or settlement-pending refund when deletion executes

If the refund is already:

```text
refund_committed
or
settlement_pending
```

Full Deletion does not cancel it.

The financial business lifecycle continues through restricted Commerce evidence after participant/product data deletion.

Deletion may complete once:

- the refund obligation is durably preserved as a restricted Commerce obligation;
- no product-access/entitlement reconstruction path remains;
- deletion requirements for other data categories are satisfied.

Deletion completion does **not** require the external payment provider to have already settled the refund.

Otherwise a provider outage could improperly block privacy deletion.

## 28.12 Refund after completed Full Deletion

After completed Full Deletion:

```text
account recovery = prohibited
Plan entitlement restoration = prohibited
personalised Plan reconstruction = prohibited
```

but an already-accrued/committed refund obligation may still settle.

Processing uses only the minimum restricted financial identity/payment/reference evidence required to:

- identify the original transaction/order;
- prevent duplicate refund;
- reconcile reversal/chargeback;
- issue or verify the refund;
- evidence terminal settlement.

It must not reconstruct the deleted participant profile, health record, Plan or entitlement.

Exact retained fields and durations remain under approved legal/financial retention policy.

## 28.13 Provider failure after deletion

If a refund obligation survives deletion but the original provider/rail cannot immediately complete it:

```text
provider failure
≠ refund obligation erased
```

Commerce continues governed reconciliation until there is a terminal authoritative net outcome.

Exact provider retry, alternate-payment or manual payout mechanics remain under the existing provider/operations/legal gates.

The platform may not restore the deleted Plan entitlement as a substitute for a failed refund after deletion.

## 28.14 Chargeback / reversal / dispute after deletion

If a chargeback, reversal or other customer-money event overlaps the surviving refund:

```text
Commerce reconciles net economic outcome
```

so that:

- NewYou does not keep money it owes;
- the participant is not reimbursed twice;
- provider evidence remains evidence until reconciled;
- deletion does not reconstruct the account.

A terminal `net_satisfied` outcome may close the refund obligation without a second outbound refund when another authoritative financial mechanism already returned the same value.

## 28.15 Deletion cancellation

If Full Deletion is cancelled within the existing 14-day window:

### Remedy merely qualified / available

```text
deletion cancelled
→ Plan entitlement remains according to ordinary account law
→ accrued refund remedy remains available
→ participant may later retain/fulfil the Plan or elect refund
```

### Refund already requested/committed

```text
deletion cancelled
→ does not automatically cancel/refund-reverse the financial action
```

Refund and deletion are independent business/data dimensions.

A refund cancellation, where permitted, must follow Commerce policy rather than being inferred from deletion cancellation.

## 28.16 Safety later returns to `eligible_automated`

If the participant has only:

```text
qualified_available
```

and has not requested/committed the refund, a later return to `eligible_automated` may still allow the participant to retain the Plan right and receive one qualifying first personalised Plan.

If successful first delivery occurs:

```text
Plan obligation fulfilled
→ accrued failed-fulfilment refund remedy closes as resolved_by_fulfilment
```

If a refund has already been committed:

```text
do not deliver
→ reconcile money first
```

If Full Deletion has reached execution:

```text
no fulfilment path remains
→ deletion-triggered refund obligation survives
```

## 28.17 No health-data retention merely to prove refund

The surviving Commerce record must not become a hidden retained health file.

Commerce needs only minimised evidence sufficient to establish:

```text
qualified failed-fulfilment remedy existed
applicable Product/Decision policy version
authoritative amount
order/payment references
refund/reconciliation state
necessary timestamps/reason category
```

It does not need the detailed medical facts that caused Safety to block the Plan.

Safety/health records follow their own deletion/retention rules.

## 28.18 Late and reordered work

Deletion orchestration must reconcile relevant current business state before completion.

A delayed worker must not produce:

```text
entitlement deleted
→ late job discovers refund qualification
→ refund silently lost
```

Likewise, after completed deletion:

- stale generation workers cannot deliver a Plan;
- stale refund workers cannot pay twice;
- restore/replay must preserve both deletion suppression and the already-recorded financial obligation/terminal outcome.

Exact ordering, locking and worker mechanics remain JIT.

# 28B. AUTHORITY / OWNERSHIP COMPOSITION

## 28.19 Commerce

Commerce owns:

- whether the Product qualification has produced an accrued financial remedy;
- authoritative refund amount;
- participant refund election/request;
- refund commitment;
- provider/refund reconciliation;
- terminal net financial outcome;
- restricted financial evidence after deletion.

For the R549 launch bundle:

```text
Plan component amount = R300
```

remains unchanged.

## 28.20 Entitlements

Entitlements owns:

- active/unfulfilled Plan right;
- whether first fulfilment has consumed it;
- blocking fulfilment after committed refund;
- terminal closure on successful refund / Full Deletion.

It does not own money settlement.

## 28.21 Privacy & Consent

Privacy & Consent owns:

- Full Deletion request/cancellation/execution/completion orchestration;
- deletion contracts across domains;
- suppression/replay truth.

It does not decide whether NewYou owes the refund.

At deletion execution it invokes Commerce/Entitlements to establish their required business transitions before deletion completes.

## 28.22 Safety & Eligibility

Safety owns the routing state that can trigger the failed-fulfilment Product qualification.

It does not own:

- refund amount;
- refund settlement;
- deletion;
- entitlement closure.

## 28.23 Audit & Evidence

Audit may retain minimised evidence of:

- qualification;
- deletion-triggered conversion;
- refund action;
- terminal outcome.

Audit does not become refund authority.

# 28C. FORMAL PRODUCT / DECISION AMENDMENT REQUIREMENT

## 28.24 Required eventual governed wording

The reviewed compression / formal Product Law and Decision Register promotion must preserve this concept:

```text
Where the bounded post-generation failed-fulfilment exception to DEC-045
has authoritatively qualified before first successful Plan delivery,
the resulting refund remedy is an accrued customer-money right.

Full Deletion permanently ends the Plan entitlement and does not restore or
reconstruct it, but Full Deletion does not waive or extinguish an accrued
failed-fulfilment refund remedy.

During the deletion cancellation window the remedy remains independently
available. If deletion reaches irreversible execution while the accrued remedy
is still unelected and unresolved, deletion execution automatically converts
that remedy into a durable Commerce refund obligation before the Plan
entitlement is destroyed.

A requested, committed or settlement-pending qualifying refund survives
completed Full Deletion. It may be settled using only the minimum restricted
commercial evidence required for payment/refund/dispute reconciliation and may
never reconstruct the deleted account, Plan, health record or entitlement.

Deletion may complete before external provider settlement once the financial
obligation is durably preserved and all ordinary deletion-completion conditions
are otherwise met.

Chargeback, reversal and refund are reconciled to one authoritative net
customer-money outcome; no duplicate reimbursement is permitted.
```

No new DEC identifier is invented here.

This wording must be formally integrated with the eventual DEC-045 amendment/supersession and the existing DEC-223/225/231 deletion boundary without rewriting historical decisions.

# 28D. PRESSURE-TEST HARDENING

## 28.25 Historical OPS-PT-368 reclassification

Historical `OPS-PT-368` said, in substance:

```text
Full Deletion completes while retained Plan right is unfulfilled
→ Plan right ends permanently
```

That remains correct for entitlement truth but is incomplete where an accrued failed-fulfilment remedy exists.

Current interpretation:

```text
no accrued failed-fulfilment refund remedy
→ Full Deletion ends Plan entitlement under deletion law

accrued failed-fulfilment refund remedy exists
→ Full Deletion ends Plan entitlement
→ refund remedy/obligation survives according to v0.30
```

Therefore:

```text
OPS-PT-368 =
  SUPERSEDED / QUALIFIED BY v0.30 FOR THE ACCRUED-REMEDY CASE
```

## 28.26 OPS-PT-411...430

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-411` | Failed-fulfilment remedy qualifies under `general_wellness_only`; participant requests Full Deletion without requesting refund | Remedy remains accrued during cancellation window; deletion execution auto-converts it into durable Commerce refund obligation before Plan right is destroyed | PASS |
| `OPS-PT-412` | Same as 411, but participant cancels Full Deletion within 14 days | No deletion-triggered refund is forced; accrued remedy and Plan right remain independently available | PASS |
| `OPS-PT-413` | Participant requests failed-fulfilment refund during deletion-pending window | Request survives deletion; fulfilment remains blocked once refund is committed | PASS |
| `OPS-PT-414` | Refund request submitted but Commerce worker has not processed it when deletion reaches execution | Queue delay cannot erase request; valid accrued remedy must be durably committed before entitlement destruction | PASS |
| `OPS-PT-415` | Refund already committed and provider settlement is pending when deletion executes | Full Deletion may complete once obligation is durably preserved; provider settlement continues under restricted Commerce evidence | PASS |
| `OPS-PT-416` | Provider settles refund after Full Deletion completed | Record terminal refund without restoring account, Plan or entitlement | PASS |
| `OPS-PT-417` | Provider refund fails after Full Deletion | Refund obligation remains for reconciliation; deleted entitlement is not restored as substitute | PASS |
| `OPS-PT-418` | Chargeback returns the same R300 bundle Plan value while refund is also pending after deletion | Commerce resolves one net R300 customer-money outcome; no double reimbursement | PASS |
| `OPS-PT-419` | R549 bundle Assessment is fulfilled; R300 Plan failed-fulfilment remedy qualifies; Full Deletion executes | Plan entitlement ends; accrued R300 refund survives; Assessment/account access still ends under deletion law | PASS |
| `OPS-PT-420` | Standalone Plan was bought at a governed discount; failed-fulfilment remedy survives deletion | Refund uses the accepted historical Plan-component amount, not current list price | PASS |
| `OPS-PT-421` | Remedy qualifies before deletion request but participant never opens refund UI | Read/open telemetry irrelevant; deletion execution still preserves/converts accrued money right | PASS |
| `OPS-PT-422` | Remedy qualifies under `professional_review_required`; participant deletes account instead of buying review | Deletion cannot force forfeiture of accrued remedy; refund obligation survives | PASS |
| `OPS-PT-423` | Post-generation state is still-actionable `insufficient_information`; participant immediately requests Full Deletion | No failed-fulfilment remedy has yet accrued solely from actionable insufficient information; deletion follows ordinary deletion consequence for that Plan right | PASS |
| `OPS-PT-424` | During deletion cancellation window, completed clarification changes outcome from actionable `insufficient_information` to `general_wellness_only` | Failed-fulfilment remedy accrues before execution; deletion execution preserves/converts it | PASS |
| `OPS-PT-425` | Remedy accrued under General Wellness, then Safety later returns `eligible_automated` while deletion is pending and no Plan was delivered | Accrued remedy remains until first successful fulfilment or refund; if deletion executes first, refund is committed because fulfilment path is terminated | PASS |
| `OPS-PT-426` | Remedy accrued; deletion cancelled; participant later receives successful qualifying first Plan delivery without having committed refund | Remedy resolves by fulfilment; no later exceptional refund for the same obligation | PASS |
| `OPS-PT-427` | Stale generation worker runs after completed deletion while refund obligation survives | Worker cannot deliver/recreate Plan; refund lifecycle remains independent | PASS |
| `OPS-PT-428` | Backup restore contains pre-deletion entitlement and refund-pending records | Replay deletion prevents entitlement resurrection; financial obligation/terminal refund truth is reconciled idempotently without duplicate payment | PASS |
| `OPS-PT-429` | Privacy asks Commerce to preserve entire health intake to prove refund qualification | Reject; retain only minimised commercial qualification/policy evidence, not detailed health data | PASS |
| `OPS-PT-430` | Whole-lifecycle review: qualified_available → deletion execution → refund committed → deletion complete → provider settlement | Entitlement ends permanently; refund settles from restricted Commerce evidence; no account reconstruction and no customer-money dead end | PASS |

All 20 new authoring tests pass under the v0.30 working amendment semantics.

These are not an independent certification.

# 28E. CURRENT CANDIDATE STATE

## 28.27 Latest-review blocker disposition

```text
LATEST REVIEW BLOCKER =
  RESOLVED IN WORKING PRODUCT / DECISION AMENDMENT CANDIDATE

root question =
  when does failed-fulfilment refund survive Full Deletion?

answer =
  at authoritative failed-fulfilment qualification,
  the monetary remedy becomes accrued

deletion request =
  does not immediately force refund during 14-day cancellation window

deletion execution =
  if accrued remedy remains unelected/unresolved,
  automatically commits durable Commerce refund obligation
  before Plan entitlement destruction

refund requested / committed / settlement pending =
  survives completed deletion

deletion completion =
  need not wait for external provider settlement
  once durable restricted financial obligation is preserved

account / entitlement restoration after deletion =
  NEVER

detailed health-data retention for refund =
  NOT PERMITTED BY THIS RULE
```

## 28.28 Updated Pre-JIT status

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 410
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 430
CONTIGUOUS PT COVERAGE = OPS-PT-001...430

OPS-UPD-001 =
  CORRECTED CANDIDATE CONVERGED
  monotonic first-pilot numeric ceiling + independent admission gate

OPS-UPD-002 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-003 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-004 =
  SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT

OPS-UPD-005 =
  CORRECTED CANDIDATE CONVERGED
  explicit future DEC-045 failed-fulfilment amendment required

OPS-UPD-006 =
  CORRECTED / COMPOSED WITH FAILED-FULFILMENT REFUND SURVIVAL
  existing legal/privacy/operations gates remain

OPS-UPD-007 =
  CORRECTED / COMPOSED WITH OPS-UPD-005
  General Wellness remains non-substitutive

R549 BUNDLE COMPONENT ALLOCATION =
  Assessment R249
  Plan R300

NEW OPS-UPD = 0
NEW OPS-GAP = 0
NEW DOMAIN = 0
NEW ARCHITECTURE MECHANISM = 0

PRE-JIT AUTHORING / HARDENING STATE =
  COMPLETE CANDIDATE
  NOT YET INDEPENDENTLY CERTIFIED

NEXT STAGE =
  FRESH INDEPENDENT HOSTILE / ADVERSARIAL REVIEW
  OF COMPLETE v0.30.0 ARTIFACT

COMPRESSION =
  BLOCKED UNTIL CLEAN INDEPENDENT REVIEW

GITHUB / PR / ACTIONS =
  DEFERRED UNTIL CLEAN REVIEW + COMPRESSION

IMPLEMENTATION =
  NOT AUTHORISED
```

## 28.29 Compression obligations if the next review is clean

Compression must preserve:

- accrued-remedy survival across deletion;
- deletion-triggered refund commitment at irreversible execution;
- no account/entitlement reconstruction;
- provider settlement may continue after deletion;
- minimised Commerce evidence only;
- R249/R300 bundle allocation and no repricing of retained component;
- explicit DEC-045 amendment/supersession status rather than pretending historical DEC-045 already contained the exception;
- v0.29 narrower actionable `insufficient_information` rule;
- monotonic pilot ceiling + independent stop gate.

Compression must remove as current normative law:

- v0.29 wording that protects only already-accepted refunds after deletion;
- historical unqualified `OPS-PT-368`;
- all earlier superseded refund/deletion survival interpretations.


---

# 29. v0.31.0 — Payer / purchaser / recipient failed-fulfilment authority hardening

> **WORKING / NON-AUTHORITATIVE UNTIL GOVERNED PROMOTION**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.30.0 BYTES PRESERVED UNCHANGED**  
> **BOUNDED CORRECTION ONLY — OPS-UPD-002 × OPS-UPD-005 × OPS-UPD-006 × OPS-UPD-007**  
> **LATEST REVIEW BLOCKER: RESOLVED IN WORKING PRODUCT / COMMERCIAL / DECISION AMENDMENT CANDIDATE**  
> **REDEEMED RECIPIENT CONTROLS WHETHER TO RETAIN OR RELINQUISH HER PLAN RIGHT**  
> **REFUND MONEY RETURNS TO THE ORIGINAL PAYER / COMMERCIAL PAYMENT RELATIONSHIP**  
> **PAYER RECEIVES NO RECIPIENT SAFETY / HEALTH EXPLANATION**  
> **RECIPIENT FULL DELETION WITH AN ACCRUED ELECTIVE REMEDY TRIGGERS REFUND TO THE PAYER WITHOUT PAYER ACTION**  
> **ZERO-PRICE COMPLIMENTARY / SPONSORED RIGHTS DO NOT CREATE CASH REFUND VALUE**  
> **NEW PRESSURE TESTS: OPS-PT-431...450**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **NO NEW ARCHITECTURE MECHANISM**  
> **NO NEW DEC IDENTIFIER INVENTED**  
> **FORMAL PRODUCT LAW / DECISION REGISTER PROMOTION STILL REQUIRED AFTER CLEAN REVIEW / COMPRESSION**  
> **IMPLEMENTATION REMAINS NOT AUTHORISED**

## 29.1 Maintenance and provenance

This successor preserves the complete v0.30.0 file byte-for-byte and appends only the payer / purchaser / recipient correction required by the latest independent review.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.30.0.md

predecessor SHA-256 =
  be123fdcfb46a950f4a5b7e6e16d36ba1b9523f2904559d977e4a98138a0b913

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 29.2 Evaluation of the latest independent review

The reviewer's blocker is accepted.

The project already distinguishes:

```text
purchaser
payer
recipient
participant
account holder
```

and already requires:

```text
money remediation
→ commercial / payer relationship

recipient entitlement
→ recipient / participant relationship

paying for another person
→ no access to recipient-private health / assessment / Plan journey
```

v0.30 closed the failed-fulfilment refund × Full Deletion lifecycle for a self-purchased Plan, but did not define who may make the refund election or receive the money when those actors differ.

That omission is Product/commercial/privacy law, not JIT mechanics.

The correction is:

> **After redemption, the recipient controls whether her redeemed Plan entitlement is retained or relinquished. If a qualifying failed-fulfilment refund is elected or deletion-triggered, the monetary refund belongs to the original payer/commercial payment relationship. The payer does not gain access to the recipient's Safety/health reason, and the recipient cannot redirect another person's refund money to herself merely because she owns the entitlement.**

## 29.3 Terminology hardening

The v0.30 term:

```text
accrued customer-money right
```

is narrowed for the pre-election state to:

```text
accrued elective refund remedy
```

This is more precise because `qualified_available` may still resolve through:

```text
later successful first personalised Plan fulfilment
```

rather than money movement.

Use:

```text
qualified_available
= accrued elective refund remedy

refund_committed
= durable Commerce refund obligation
```

This distinction must survive compression.

# 29A. SPLIT-IDENTITY COMMERCIAL MODEL

## 29.4 Actor dimensions

For refund semantics, keep these concepts distinct:

### Purchaser

The actor who placed/accepted the commercial order.

### Payer

The monetary relationship/payment source that supplied the funds and to which ordinary refund value is returned, subject to Commerce/provider/legal rules.

Purchaser and payer may be the same person, but the Product model must not rely on that being universal.

### Recipient

The intended grantee of the purchased access.

### Participant

The redeemed recipient/account holder whose private Safety/health journey determines whether personalised Plan fulfilment is lawful.

After redemption, recipient and participant will ordinarily refer to the same entitlement holder for this Plan path.

### Commercial refund beneficiary

For the failed-fulfilment remedy:

```text
original payer / authoritative commercial payment relationship
```

not automatically:

```text
recipient
participant
purchaser
```

unless those identities coincide with the payer.

## 29.5 Before redemption

Before a gift/recipient Plan right is redeemed:

- no participant Safety/health Plan-generation lifecycle exists for that recipient;
- the failed-fulfilment exception cannot have qualified merely from an unredeemed code/grant;
- purchaser reassignment/refund/cancellation follows the existing pre-redemption gift/commercial rules.

This v0.31 correction governs the **redeemed paid Plan** path.

## 29.6 After redemption — recipient controls the entitlement decision

Once the paid Plan entitlement has been redeemed by the recipient:

```text
redeemed Plan entitlement
→ belongs to recipient/participant access relationship
→ non-transferable under existing Product rules
```

Therefore, if a failed-fulfilment remedy later qualifies:

### Recipient may

- retain the unconsumed Plan right for possible later lawful fulfilment;
- elect to relinquish that Plan right through the failed-fulfilment refund path;
- request Full Deletion, which permanently relinquishes the Plan right and invokes the deletion/refund composition below.

### Payer/purchaser may not

merely because they funded the purchase:

- force the recipient to keep using the Plan;
- force the recipient to surrender a redeemed Plan entitlement through the Safety-dependent failed-fulfilment path;
- access recipient Safety outcome, health facts, Plan, assessment, progress or deletion reason;
- redirect the recipient's redeemed entitlement to someone else.

Independent payer rights such as:

- genuine duplicate-collection remediation;
- chargeback/dispute rights;
- statutory rights;
- an otherwise applicable pre-redemption/ordinary commercial refund;

remain separate and do not require disclosure of recipient Safety data.

## 29.7 Recipient refund election

Where:

```text
payer A
→ bought paid Plan for recipient B

recipient B
→ redeemed Plan

B's failed-fulfilment remedy
→ qualified_available
```

the Product election belongs to **B as the redeemed entitlement holder**:

```text
retain Plan right
OR
relinquish Plan right via refund
```

If B elects refund:

```text
B controls relinquishment of B's entitlement
A receives the authoritative refund value
```

B does **not** acquire ownership of A's payment merely by making the entitlement decision.

The refund normally returns through the authoritative original payer/payment relationship.

Exact provider/refund-destination mechanics remain Commerce/JIT/provider work.

## 29.8 Payer cannot independently invoke the Safety-dependent exception after redemption

Where A paid and B redeemed:

```text
A
→ cannot independently elect the failed-fulfilment refund
solely because A is payer
```

because doing so would terminate B's non-transferable redeemed entitlement and could expose/infer B's private Safety state.

A may contact Commerce/Support about the order.

The platform may process independent payer-side rights where applicable.

But the Safety-dependent failed-fulfilment election itself requires:

```text
recipient entitlement authority
```

or the deletion-triggered automatic transition defined below.

## 29.9 Disagreement between payer and recipient

If:

```text
payer A wants refund
recipient B wants to retain the redeemed Plan right
```

then, for the failed-fulfilment exception:

```text
B's entitlement decision controls
```

unless A has an independent commercial/legal refund right unrelated to B's private Safety-dependent remedy.

If:

```text
B elects refund
A would prefer B to keep the Plan
```

then:

```text
B may relinquish B's redeemed entitlement
Commerce refunds A
```

A's preference cannot force B to continue a personal health-related service.

This does not permit B to redirect A's refund value.

## 29.10 Refund destination

A qualifying refund is returned to:

```text
authoritative original payer/payment relationship
```

subject to:

- provider capabilities;
- chargeback/reversal state;
- verified alternate refund mechanics where the original rail cannot receive the refund;
- legal/accounting requirements.

The recipient is not a substitute refund beneficiary merely because the recipient initiated the entitlement relinquishment.

Where payer and participant are the same person, this distinction collapses naturally.

## 29.11 Purchaser and payer differ

If:

```text
purchaser P
payer A
recipient B
```

then:

- P may retain only the commercial visibility authorised by the accepted order relationship;
- B controls the redeemed Plan entitlement election;
- A/payment relationship is the monetary refund beneficiary;
- no actor receives B's private Safety/health details by virtue of purchase/payment status.

Commerce must preserve the accepted order's authoritative purchaser/payer/recipient relationships sufficiently for later reconciliation without making them one identity.

# 29B. PRIVACY BOUNDARY

## 29.12 Payer-facing information

When a refund is created because the recipient's failed-fulfilment remedy qualified, payer-facing communication may disclose only the minimum commercial information required to explain/reconcile the order, such as:

- original order/payment reference;
- affected commercial product/component;
- refund amount;
- refund status;
- refund date/transaction reference where available;
- generic statement that the refund was issued under the applicable product fulfilment/refund policy.

It must not disclose:

- `general_wellness_only`;
- `professional_review_required`;
- `insufficient_information`;
- diagnosis, symptoms, pregnancy, medication, allergy or other health facts;
- detailed Safety reason;
- participant assessment result;
- Plan content;
- participant progress;
- participant's Full Deletion decision as the reason for the refund;
- any other recipient-private journey data not independently authorised.

## 29.13 No privacy side channel through refund reason codes

A payer-visible refund reason must not encode or expose a recipient Safety class.

Internal Commerce evidence may record a minimised non-clinical qualification reference/policy version sufficient to prove the commercial remedy.

Detailed Safety facts remain with their owning domains and applicable deletion rules.

Conceptually:

```text
Commerce may know:
  failed_fulfilment_refund_qualified
  policy/version
  amount
  order/payment refs
  entitlement consequence
  refund state

Commerce/payer need not know:
  the recipient's underlying health facts
```

Exact implementation naming remains JIT.

# 29C. FULL DELETION WHEN PAYER ≠ RECIPIENT

## 29.14 Recipient Full Deletion with accrued elective remedy

Where:

```text
payer A
recipient/participant B

B's failed-fulfilment remedy = qualified_available
B requests Full Deletion
```

the v0.30 cancellation-window rule remains:

```text
deletion_requested
→ does not immediately force money settlement
```

If B cancels deletion within the 14-day window:

- B retains the Plan right subject to ordinary law;
- the accrued elective refund remedy remains available;
- A receives no recipient-private deletion/Safety explanation.

If deletion reaches irreversible execution:

```text
B's Plan entitlement must terminate
```

so B can no longer choose the retain-right branch.

Therefore:

> **Recipient Full Deletion execution acts as B's final relinquishment of the redeemed Plan right and automatically converts B's accrued elective refund remedy into a durable Commerce refund obligation payable to A/the authoritative payer relationship.**

No additional payer election or consent is required.

## 29.15 Payer cannot block recipient deletion

Payer A cannot prevent B's Full Deletion because a future refund may be payable to A.

B's privacy/deletion authority over B's account and private journey remains independent.

At deletion execution:

```text
Privacy terminates B's entitlement/access
Commerce preserves/processes A's refund
```

without restoring or exposing B's private data.

## 29.16 Payer need not act to receive deletion-triggered refund

If B Full Deletes with a qualified remedy:

```text
refund to A
→ does not require A to know why B's entitlement ended
→ does not require A to approve B's deletion
→ does not require B to access a refund UI
```

Commerce may notify A of the resulting commercial refund/adjustment without disclosing that B deleted the account or what Safety condition existed.

## 29.17 Payer account deletion / closure does not destroy recipient entitlement

Where:

```text
A paid for B
A later closes or Full Deletes A's own account/identity relationship
B's redeemed Plan entitlement remains valid
```

unless another independent commercial law says otherwise.

A's deletion must not revoke B's redeemed non-transferable entitlement merely because A was payer.

If B later qualifies for and elects a failed-fulfilment refund:

- Commerce uses the minimum retained commercial/payment evidence lawfully available;
- the refund remains payable to the authoritative payer/payment relationship;
- A's deleted account is not reconstructed;
- B is not made monetary beneficiary by default.

Exact edge handling where the original payment rail is no longer refundable remains provider/legal/Commerce operations work.

## 29.18 Recipient deletion before remedy qualification

Where B Full Deletes while:

```text
failed-fulfilment remedy = not_qualified
```

this v0.31 correction does not create a new exceptional cash refund merely because B chose deletion.

Examples include the v0.29 actionable `insufficient_information` state where the exceptional remedy had not yet accrued.

Existing ordinary/statutory/payer-side commercial rights remain separately governed.

# 29D. COMPLIMENTARY / SPONSORED / THIRD-PARTY PAID RIGHTS

## 29.19 Positive monetary consideration is required for the cash refund remedy

The failed-fulfilment **cash** refund exists only where there is:

```text
a positive paid commercial amount
attributable to the affected Plan component
```

Therefore:

### Zero-price complimentary Plan grant

```text
paid Plan component amount = R0
```

Result:

- no cash failed-fulfilment refund;
- recipient may retain the grant where lawful;
- Full Deletion ends it;
- another goodwill/replacement grant requires its own authority.

### Zero-price sponsored grant

Where the recipient's Plan access is granted at no attributable paid amount to any payer:

```text
cash failed-fulfilment refund = R0 / not applicable
```

Do not create money where no commercial payment obligation existed.

## 29.20 Genuinely paid third-party gift

Where A paid a positive governed amount for B's redeemed Plan:

```text
recipient B
→ controls retain/relinquish election

payer A
→ receives refund amount
```

For the R549 launch bundle:

```text
Plan component refund amount = R300
```

when that accepted offer applies.

## 29.21 Paid sponsorship / bulk sponsored access

If a sponsor/payer has paid a positive commercial amount for recipient Plans:

- the sponsor/payer is the financial refund beneficiary;
- each redeemed recipient controls her own entitlement retain/relinquish decision;
- sponsor/payer receives no recipient-private Safety/health reason;
- the accepted sponsored offer must define an attributable per-recipient/per-Plan refund amount or an equivalent deterministic allocation before activation.

If a paid bulk sponsored offer lacks such an allocation:

```text
activation / sale = NO-GO
```

for a pathway that could require component refund.

Runtime/operator discretion may not invent a per-recipient refund amount later.

## 29.22 Sponsor reporting

Sponsor reporting remains bounded to approved commercial/aggregate information.

A sponsor must not receive:

- which recipient became `general_wellness_only`;
- which recipient required professional review;
- which recipient deleted her account;
- individual Safety reason;
- private Plan/assessment/health details;

merely because the sponsor received a refund or commercial adjustment.

# 29E. CONCURRENCY / COMMAND AUTHORITY

## 29.23 Recipient refund election is consequential

A redeemed recipient's refund election is consequential because it relinquishes an entitlement and initiates a third-party monetary consequence.

Therefore it requires:

- authenticated recipient/participant authority;
- current entitlement identity;
- current remedy qualification;
- idempotency;
- clear participant-facing consequence;
- owner-domain transitions rather than direct UI mutation.

Exact step-up/authentication mechanics remain JIT/policy detail.

## 29.24 Fulfilment race after recipient election

Once B's valid refund election is durably accepted:

```text
no new first personalised Plan fulfilment
```

may race ahead while Commerce processes A's refund.

If the refund ultimately fails/cancels without money leaving the platform and B's entitlement is not deleted:

```text
return to active/unfulfilled
```

must follow the existing v0.29/v0.30 reconciliation semantics and current Safety must be re-read.

## 29.25 Duplicate money + split identities

Where A suffered genuine duplicate collection and B later also qualifies for a Plan-component failed-fulfilment refund:

```text
duplicate excess remediation
+
legitimate Plan-component refund
→ both belong to A/payer commercial relationship
```

Commerce reconciles the net result so A is made whole exactly once for each valid monetary claim and never twice for the same value.

B's private Safety context remains undisclosed.

# 29F. FORMAL PRODUCT / DECISION AMENDMENT REQUIREMENT

## 29.26 Required eventual governed wording

The eventual Product Law / Decision Register amendment/supersession must preserve this concept:

```text
Purchaser, payer, recipient and participant remain distinct.

For a redeemed paid Plan purchased for another person, the redeemed
recipient/participant controls whether to retain or relinquish the Plan
entitlement when the bounded failed-fulfilment refund remedy has qualified.

A payer/purchaser does not obtain authority over the recipient's redeemed
Plan or private Safety/health journey merely by funding the purchase.

If the recipient elects the qualifying refund, the Plan entitlement is
relinquished through the governed refund path and the monetary refund is
payable to the original payer/authoritative payment relationship, not to the
recipient merely because she made the entitlement election.

The payer receives only minimum commercial refund information and no
recipient Safety/health explanation.

If the recipient reaches irreversible Full Deletion while an accrued elective
failed-fulfilment remedy remains available, deletion acts as final relinquishment
of the recipient's Plan right and automatically commits the refund to the
authoritative payer relationship before entitlement destruction. No payer
action or consent is required, and the payer may not block recipient deletion.

A payer's own account deletion does not terminate a recipient's redeemed Plan
and does not erase a later valid refund obligation; restricted commercial
evidence may be used without reconstructing the payer or recipient account.

Zero-price complimentary or sponsored Plan rights create no cash
failed-fulfilment refund. Paid third-party/sponsored offers must preserve an
authoritative attributable Plan refund amount before activation.
```

No new DEC identifier is invented here.

This must be integrated with the eventual DEC-045 failed-fulfilment amendment and existing purchaser/gift/privacy/deletion decisions without rewriting historical law.

# 29G. PRESSURE-TEST HARDENING

## 29.27 Historical OPS-PT-411...430 scope correction

The deletion-survival logic of v0.30 remains valid.

The split-identity cases are now interpreted as follows:

```text
OPS-PT-411
→ generalises to payer ≠ participant:
   recipient deletion auto-refunds authoritative payer

OPS-PT-413 / 414
→ refund election/request actor is the redeemed recipient;
   monetary beneficiary remains payer

OPS-PT-419
→ R300 bundle Plan refund goes to payer, not recipient by default

OPS-PT-421
→ recipient need not open refund UI;
   deletion execution can convert accrued remedy automatically

OPS-PT-430
→ complete lifecycle now includes separate entitlement actor and payer
```

Their v0.30 self-purchased outcomes remain valid special cases.

## 29.28 OPS-PT-431...450

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-431` | A pays for B's redeemed standalone Plan; B's failed-fulfilment remedy qualifies; B elects refund | B relinquishes Plan right; refund goes to A/original payer relationship; no Safety detail disclosed to A | PASS |
| `OPS-PT-432` | A paid; B's remedy qualifies; A asks to invoke the Safety-dependent refund while B wants to retain the Plan | A cannot terminate B's redeemed entitlement via this exception; B controls retain/relinquish; A's independent rights remain separate | PASS |
| `OPS-PT-433` | A paid; B elects refund; A wants B to keep the Plan | B may relinquish B's entitlement; Commerce refunds A; A cannot force B to continue | PASS |
| `OPS-PT-434` | A paid; B elects refund and asks that the money be sent to B instead | Reject by default; refund belongs to authoritative payer/payment relationship unless independent Commerce/legal authority establishes otherwise | PASS |
| `OPS-PT-435` | Purchaser P, payer A and recipient B are three distinct actors | B controls redeemed entitlement election; A receives monetary refund; P receives only authorised commercial visibility; no B-private Safety disclosure | PASS |
| `OPS-PT-436` | A pays for B; B has accrued remedy and requests Full Deletion without refund election | During cancellation window remedy remains elective; irreversible deletion auto-commits refund to A before B's entitlement is destroyed | PASS |
| `OPS-PT-437` | Same as 436, but B cancels Full Deletion | No forced refund; B's Plan right and accrued elective remedy remain; A receives no deletion/Safety explanation | PASS |
| `OPS-PT-438` | A pays for B; B Full Deletes after remedy accrued; A never logs in or responds | Payer action not required; refund to A/payment relationship proceeds from durable Commerce obligation | PASS |
| `OPS-PT-439` | A receives deletion-triggered refund and asks why | Provide minimum commercial refund status only; do not reveal B's deletion, Safety route or health information | PASS |
| `OPS-PT-440` | A Full Deletes A's own payer account after B redeemed the Plan | B's entitlement remains; A's deletion does not revoke B's non-transferable redeemed right | PASS |
| `OPS-PT-441` | A's payer account is deleted; later B qualifies and elects failed-fulfilment refund | Refund uses restricted original commercial/payment evidence without reconstructing A's account; B does not become refund beneficiary by default | PASS |
| `OPS-PT-442` | Zero-price complimentary Plan becomes non-fulfillable | No cash refund is created; entitlement follows retain/delete/other approved grant rules | PASS |
| `OPS-PT-443` | Zero-price sponsored Plan becomes non-fulfillable | No cash failed-fulfilment refund exists where no positive attributable Plan payment exists | PASS |
| `OPS-PT-444` | Paid sponsor funds B's Plan with explicit per-recipient Plan refund allocation; B elects refund | B relinquishes entitlement; sponsor/payer receives allocated refund; no B-private reason disclosed | PASS |
| `OPS-PT-445` | Paid bulk sponsor offer has no attributable per-recipient Plan refund allocation | Offer activation is NO-GO for this path; runtime/operator cannot invent allocation after failure | PASS |
| `OPS-PT-446` | A paid R549 bundle for B; Assessment retained; B elects qualifying Plan refund | B's Plan right closes; authoritative R300 Plan component is refunded to A; Assessment follows its own entitlement law | PASS |
| `OPS-PT-447` | A was genuinely double-collected for B's bundle and B later elects R300 Plan refund | Duplicate excess remediation and valid R300 Plan refund both reconcile to A without double reimbursement | PASS |
| `OPS-PT-448` | Refund provider reason visible to A contains `general_wellness_only` or other recipient Safety code | Reject/redact; payer-visible financial evidence may not expose recipient Safety class | PASS |
| `OPS-PT-449` | B's refund election is durably accepted while stale Plan-delivery worker is racing | Delivery is blocked; Commerce refunds A; no stale Plan fulfilment may defeat B's accepted relinquishment | PASS |
| `OPS-PT-450` | Whole split lifecycle: A pays → B redeems → B becomes safety-invalidated → remedy accrues → B Full Deletes → refund settles to A | B's entitlement/account end permanently; A receives correct refund; no B health/Safety/deletion reason leaks; no reconstruction or dead end | PASS |

All 20 new authoring tests pass under the v0.31 working amendment semantics.

These are not an independent certification.

# 29H. CURRENT CANDIDATE STATE

## 29.29 Latest-review blocker disposition

```text
LATEST REVIEW BLOCKER =
  RESOLVED IN WORKING PRODUCT / COMMERCIAL / DECISION AMENDMENT CANDIDATE

split identity rule =
  recipient controls redeemed entitlement retain/relinquish election

monetary beneficiary =
  original payer / authoritative payment relationship

payer authority =
  cannot unilaterally invoke Safety-dependent exception
  against recipient's redeemed entitlement

recipient authority =
  can relinquish own redeemed entitlement
  cannot redirect another person's refund money by default

payer-facing privacy =
  commercial status / amount only
  no recipient Safety / health / deletion reason

recipient Full Deletion =
  if accrued elective remedy exists,
  irreversible deletion auto-commits refund to payer

payer Full Deletion =
  does not terminate recipient's redeemed entitlement
  does not erase later valid refund obligation

zero-price complimentary/sponsored access =
  no cash failed-fulfilment refund

paid third-party/sponsored access =
  requires authoritative attributable Plan refund amount
```

## 29.30 Updated Pre-JIT status

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 430
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 450
CONTIGUOUS PT COVERAGE = OPS-PT-001...450

OPS-UPD-001 =
  CORRECTED CANDIDATE CONVERGED
  monotonic first-pilot numeric ceiling + independent admission gate

OPS-UPD-002 =
  CORRECTED / COMPOSED WITH SPLIT-IDENTITY FAILED-FULFILMENT MONEY FLOW

OPS-UPD-003 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-004 =
  SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT

OPS-UPD-005 =
  CORRECTED CANDIDATE CONVERGED
  explicit future DEC-045 failed-fulfilment amendment required

OPS-UPD-006 =
  CORRECTED / COMPOSED WITH FAILED-FULFILMENT REFUND SURVIVAL
  AND SPLIT PAYER/RECIPIENT DELETION

OPS-UPD-007 =
  CORRECTED / COMPOSED WITH OPS-UPD-005
  General Wellness remains non-substitutive

R549 BUNDLE COMPONENT ALLOCATION =
  Assessment R249
  Plan R300

NEW OPS-UPD = 0
NEW OPS-GAP = 0
NEW DOMAIN = 0
NEW ARCHITECTURE MECHANISM = 0

PRE-JIT AUTHORING / HARDENING STATE =
  COMPLETE CANDIDATE
  NOT YET INDEPENDENTLY CERTIFIED

NEXT STAGE =
  FRESH INDEPENDENT HOSTILE / ADVERSARIAL REVIEW
  OF COMPLETE v0.31.0 ARTIFACT

COMPRESSION =
  BLOCKED UNTIL CLEAN INDEPENDENT REVIEW

GITHUB / PR / ACTIONS =
  DEFERRED UNTIL CLEAN REVIEW + COMPRESSION

IMPLEMENTATION =
  NOT AUTHORISED
```

## 29.31 Compression obligations if the next review is clean

Compression must preserve:

- purchaser / payer / recipient / participant separation;
- recipient control over the redeemed entitlement election;
- refund to authoritative payer relationship;
- no payer Safety/health/deletion disclosure;
- recipient Full Deletion as automatic relinquishment/refund trigger where remedy accrued;
- payer deletion not cancelling recipient entitlement;
- zero-price grant vs paid third-party distinction;
- explicit attributable refund allocation for paid sponsored offers;
- v0.30 accrued-remedy survival and deletion-triggered commitment;
- R249/R300 bundle allocation;
- explicit DEC-045 amendment/supersession status;
- v0.29 actionable `insufficient_information` narrowing;
- monotonic pilot ceiling + independent stop gate.

Compression must remove as current normative law:

- v0.30 wording that implicitly treats the participant as both entitlement actor and monetary beneficiary;
- any historical wording suggesting payer status grants recipient-private journey access;
- any older split-party interpretation inconsistent with this section.


---

# 30. v0.32.0 — Redeemed third-party ordinary pre-generation refund authority hardening

> **WORKING / NON-AUTHORITATIVE UNTIL GOVERNED PROMOTION**  
> **APPEND-ONLY SUCCESSOR STATUS — v0.31.0 BYTES PRESERVED UNCHANGED**  
> **BOUNDED CORRECTION ONLY — OPS-UPD-002 × OPS-UPD-005 / GIFT-REFUND PRODUCT SURFACE**  
> **LATEST REVIEW BLOCKER: RESOLVED IN WORKING PRODUCT / COMMERCIAL / DECISION AMENDMENT CANDIDATE**  
> **BEFORE REDEMPTION: PAYER/PURCHASER COMMERCIAL REFUND AUTHORITY REMAINS UNDER EXISTING GIFT/OFFER LAW**  
> **AFTER REDEMPTION: ORDINARY PRE-GENERATION REFUND REQUIRES REDEEMED RECIPIENT RELINQUISHMENT OF THE PLAN RIGHT**  
> **PAYER/PURCHASER MAY REQUEST BUT MAY NOT UNILATERALLY TERMINATE A REDEEMED RECIPIENT PLAN**  
> **REFUND MONEY RETURNS TO THE AUTHORITATIVE PAYER/PAYMENT RELATIONSHIP**  
> **PAYER/RECIPIENT DISAGREEMENT: REDEEMED PLAN REMAINS; ORDINARY REFUND DOES NOT COMMIT**  
> **NEW PRESSURE TESTS: OPS-PT-451...470**  
> **NO NEW OPS-UPD**  
> **NO NEW OPS-GAP**  
> **NO NEW DOMAIN**  
> **NO NEW ARCHITECTURE MECHANISM**  
> **NO NEW DEC IDENTIFIER INVENTED**  
> **FORMAL PRODUCT LAW / DECISION REGISTER PROMOTION STILL REQUIRED AFTER CLEAN REVIEW / COMPRESSION**  
> **IMPLEMENTATION REMAINS NOT AUTHORISED**

## 30.1 Maintenance and provenance

This successor preserves the complete v0.31.0 file byte-for-byte and appends only the narrow correction requested by the latest independent reviewer.

```text
predecessor file =
  NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.31.0.md

predecessor SHA-256 =
  63a01a10ce0dbcac14c40351628c8901c5304d86aaa014c2bf838f65f628897c

maintenance mode =
  append-only

artifact format =
  Markdown only
```

## 30.2 Evaluation of the latest independent review

The reviewer's single blocker is accepted.

Existing current Product/Decision law establishes both:

```text
redeemed gifted access
→ non-transferable
```

and:

```text
Plan ordinary refund
→ available before generation
```

The missing semantic was not the refund amount or destination.

It was:

```text
after a third-party paid Plan has been redeemed
but before Plan generation,
who has authority to relinquish the redeemed entitlement
so that the ordinary refund may commit?
```

The correction is:

> **Once a paid third-party Plan is redeemed, the redeemed recipient controls relinquishment of that entitlement. A payer/purchaser may request an ordinary pre-generation refund, but Commerce may not commit it unless the redeemed recipient has explicitly authorised relinquishment of the Plan right, or another independently governed legal/commercial authority requires a different outcome. The refund money returns to the authoritative payer/payment relationship.**

This keeps:

- money authority with Commerce;
- access/right authority with Entitlements;
- human authority over redeemed access with the recipient;
- payer/recipient privacy separation intact.

## 30.3 Scope discipline

This correction does **not** reopen:

- v0.31 payer/recipient failed-fulfilment semantics;
- v0.30 failed-fulfilment refund survival through Full Deletion;
- v0.29 DEC-045 amendment classification;
- v0.29 R249/R300 launch bundle allocation;
- General Wellness non-substitution;
- `insufficient_information` narrowing;
- pilot ceiling/admission semantics;
- zero-price grant rules.

It addresses only:

```text
redeemed third-party paid Plan
+ no Plan generation yet
+ ordinary DEC-045 refund requested
```

# 30A. ORDINARY PRE-GENERATION REFUND AUTHORITY

## 30.4 Before redemption

Before a third-party Plan entitlement is redeemed:

```text
payer/purchaser commercial relationship
→ controls any otherwise-valid pre-redemption refund/cancellation
according to the accepted offer/gift policy
```

No participant entitlement has yet become a redeemed, non-transferable right.

Therefore the payer/purchaser may exercise the ordinary commercial refund path where current Product law permits it.

Exact purchaser-versus-payer handling follows the accepted commercial order and payment relationship.

## 30.5 Redemption is the authority-transfer boundary for entitlement relinquishment

Once the recipient redeems the Plan entitlement:

```text
commercial purchase history remains with Commerce
money remains attributable to the payer relationship
but
redeemed Plan access becomes the recipient's non-transferable entitlement
```

Redemption therefore changes **who may authorise termination of the entitlement** for an optional ordinary refund.

It does not change who receives the money.

## 30.6 After redemption — payer may request, recipient must relinquish

Where:

```text
A paid for Plan for B
B redeemed the Plan
no personalised Plan has yet been generated
ordinary DEC-045 refund window remains open
A requests refund
```

the Product rule is:

```text
A may request ordinary refund review

Commerce verifies:
  refund window still open
  payment/order valid
  Plan not generated
  entitlement still active

BUT

Commerce may not commit refund
until B explicitly authorises relinquishment
of B's redeemed Plan entitlement
```

If B authorises relinquishment:

```text
Entitlements
→ closes/revokes B's redeemed Plan right

Commerce
→ commits refund to authoritative payer/payment relationship
```

The exact cross-domain transaction/ordering mechanism remains JIT.

## 30.7 Recipient may also initiate the relinquishment

B does not need to wait for A to ask first.

If B decides before generation that she no longer wants the redeemed Plan:

```text
B may elect to relinquish B's redeemed Plan right
through the ordinary pre-generation refund path
```

Commerce then refunds:

```text
the authoritative payer/payment relationship
```

not B by default.

B controls the entitlement relinquishment.

B does not acquire A's money.

## 30.8 Payer / recipient disagreement

### Payer wants refund; recipient wants to retain Plan

```text
A wants ordinary refund
B wants to keep redeemed Plan
```

Outcome:

```text
B's redeemed entitlement remains active
ordinary refund does not commit
```

A cannot use the ordinary pre-generation refund path to unilaterally revoke B's redeemed non-transferable right.

Independent payer rights outside this optional ordinary refund path remain separately governed.

### Recipient wants refund/relinquishment; payer prefers no refund

```text
B wants to relinquish redeemed Plan
A wants B to retain it
```

Outcome:

```text
B may relinquish B's entitlement
Commerce refunds A/payment relationship
```

A cannot force B to continue a personal health-related service merely because A paid.

## 30.9 No refund while retaining the redeemed Plan

The platform must never produce:

```text
payer refunded
+
recipient Plan entitlement still active
```

for the same ordinary pre-generation refund.

The authoritative transition must preserve the invariant:

```text
ordinary refund committed
→ corresponding redeemed Plan entitlement is closed/revoked
```

or, if entitlement closure cannot be authoritatively established:

```text
refund fails closed / does not commit
```

## 30.10 No entitlement revocation without valid refund commitment path

The inverse must also be protected.

Do not close B's redeemed Plan merely because A submitted a refund request.

Conceptually:

```text
payer refund request
≠ recipient relinquishment
≠ refund commitment
```

B's right remains until the recipient has authorised relinquishment and the ordinary refund transition can be committed under current Commerce rules.

Exact atomicity/saga/transaction design remains JIT.

## 30.11 Refund destination

Where A is the authoritative payer:

```text
refund beneficiary
→ A / authoritative payer/payment relationship
```

Use the more precise wording:

```text
authoritative payer/payment relationship
```

rather than assuming:

```text
original card always available
```

Provider inability to refund the original rail is an execution/reconciliation problem, not permission to redirect the commercial value to B by default.

## 30.12 Purchaser, payer and recipient all differ

Where:

```text
purchaser P
payer A
recipient B
```

then for a redeemed ordinary pre-generation refund:

- B controls whether B's Plan entitlement is relinquished;
- A/payment relationship receives the refund value;
- P may request/support the commercial process only to the extent the accepted order relationship authorises;
- P does not gain power to terminate B's entitlement merely by being purchaser;
- neither P nor A receives B's private onboarding/health/Safety information.

## 30.13 Privacy boundary

Ordinary pre-generation refund does not require disclosure of recipient private journey data to the payer.

Payer-facing information may include:

- product/component;
- refund eligibility/commercial status;
- amount;
- refund status/reference;
- generic indication that the redeemed entitlement was relinquished where needed for order reconciliation.

It must not disclose:

- B's onboarding answers;
- B's health/Safety state;
- assessment/result data;
- Plan preferences;
- personal reason for relinquishment;
- whether B is pursuing General Wellness or professional review.

The payer only needs commercial truth.

## 30.14 Recipient relinquishment must be explicit and authenticated

After redemption, recipient relinquishment is consequential.

It must therefore be:

- made by the authenticated redeemed recipient or authorised lawful representative;
- scoped to the exact Plan entitlement;
- explicit about permanent loss of that redeemed right if refund commits;
- idempotent;
- auditable;
- checked against current generation/refund state.

A generic Support note or payer instruction is not sufficient authority.

Exact authentication/step-up mechanics remain JIT/policy detail.

# 30B. RACES AND BOUNDARIES

## 30.15 Generation races with ordinary refund

The ordinary refund remains available only while the Product generation cutoff has not been crossed.

Therefore, if:

```text
B authorises relinquishment
but
Plan generation commits first
```

then:

```text
ordinary pre-generation refund path closes
```

and the system must not pretend the earlier recipient intent rewound generation.

Any later refund must qualify under another governed rule, such as the bounded failed-fulfilment amendment if its conditions arise.

Conversely, once the ordinary refund transition is authoritatively committed:

```text
no Plan generation may consume the closing entitlement
```

Exact serialization/locking/idempotency remains JIT.

## 30.16 Refund request races with recipient use/onboarding

Recipient onboarding progress does not itself close the Plan ordinary refund.

The authoritative cutoff remains Plan generation.

Therefore:

```text
B redeemed
B completed some onboarding
no Plan generated
B authorises relinquishment
→ ordinary refund may proceed
```

subject to the current accepted offer/refund rules.

## 30.17 Full Deletion before generation

If B Full Deletes before Plan generation and no failed-fulfilment remedy has accrued:

```text
Full Deletion ends B's redeemed Plan entitlement
```

For a **paid third-party redeemed Plan still ordinarily refundable before generation**, deletion execution is treated as B's final relinquishment of the redeemed entitlement.

Therefore, before entitlement destruction:

```text
Commerce must commit the still-valid ordinary pre-generation refund
to the authoritative payer/payment relationship
```

unless another authoritative financial outcome has already satisfied the amount.

This avoids:

```text
A paid
B redeemed
no Plan generated
B Full Deletes
→ NewYou keeps money while entitlement is destroyed
```

No additional payer approval is required.

The payer receives no private deletion reason.

This ordinary-refund deletion rule is distinct from the post-generation failed-fulfilment deletion rule, but both follow the same ownership principle:

```text
recipient deletion ends recipient entitlement
money consequence belongs to payer relationship
```

## 30.18 Deletion cancellation

During the 14-day deletion cancellation window:

```text
no automatic ordinary refund commitment solely because deletion was requested
```

If B cancels deletion:

- B keeps the redeemed Plan entitlement;
- the ordinary refund window remains governed by whether generation has occurred;
- A cannot force refund without B's relinquishment.

If B independently authorised ordinary refund and Commerce committed it during the deletion-pending window:

```text
deletion cancellation
→ does not automatically undo committed refund
```

## 30.19 Payer deletion

A's own closure/Full Deletion does not grant B refund money or revoke B's redeemed entitlement.

If B later authorises an ordinary pre-generation refund:

```text
Commerce uses minimum lawfully retained commercial/payment evidence
→ refunds authoritative payer/payment relationship
→ does not reconstruct A's deleted account
```

## 30.20 Chargeback / unauthorised-payment / statutory rights

This section does not redefine:

- chargeback;
- fraud/unauthorised-payment remediation;
- statutory consumer rights;
- duplicate genuine collection.

Those may create independent payer-side monetary consequences under their own authority.

Where an independent authoritative payer-side outcome requires entitlement consequences, Commerce must invoke Entitlements through the governing rule.

JIT may not infer that the optional ordinary pre-generation refund rule overrides or eliminates those independent rights.

# 30C. GIFTS, SPONSORSHIP AND ZERO-PRICE ACCESS

## 30.21 Individually paid gift

For an individually paid redeemed gift Plan:

```text
before redemption
→ payer/purchaser ordinary refund authority under offer policy

after redemption
→ recipient relinquishment required for optional ordinary pre-generation refund

money
→ authoritative payer/payment relationship
```

## 30.22 Paid sponsored individual access

Where a sponsor/payer funds a specific recipient's Plan and the recipient redeems it:

```text
recipient relinquishment
→ required for optional ordinary pre-generation refund after redemption

sponsor/payer
→ monetary beneficiary
```

Sponsor/payer may not unilaterally revoke redeemed access through this ordinary refund path.

## 30.23 Paid bulk sponsorship

For bulk paid sponsored access:

- unredeemed allocations may follow the approved sponsor/offering cancellation/refund policy;
- redeemed recipient Plan entitlements follow the same recipient-relinquishment rule as individually paid gifts;
- the sponsor receives no recipient-private reason;
- attributable refund amount must be deterministic before activation.

Any future sponsor contract that intentionally gives the sponsor a post-redemption termination power would be a separate explicit Product/commercial rule and must satisfy privacy/fairness requirements; it is **not** implied here.

## 30.24 Zero-price grants

Where:

```text
paid Plan component amount = R0
```

there is no ordinary cash Plan refund amount to return.

Recipient relinquishment or Full Deletion may end the zero-price entitlement, but no cash value is invented.

# 30D. FORMAL PRODUCT / DECISION AMENDMENT REQUIREMENT

## 30.25 Required eventual governed wording

The eventual Product Law / Decision Register amendment/supersession must preserve this concept:

```text
For a third-party paid Plan, refund authority changes at redemption.

Before redemption, an otherwise-valid ordinary commercial refund may be
controlled through the purchaser/payer relationship according to the accepted
offer and gift policy.

After redemption, the Plan entitlement is the recipient's non-transferable
redeemed right. An optional ordinary pre-generation Plan refund may not be
committed merely because the payer/purchaser requests it. The redeemed
recipient must explicitly relinquish the Plan entitlement.

The recipient may independently elect relinquishment, but the monetary refund
is paid to the authoritative payer/payment relationship, not to the recipient
merely because she controlled the entitlement decision.

If payer and recipient disagree, the recipient's decision controls whether the
redeemed entitlement is surrendered for this ordinary refund path. Payer-side
independent rights such as chargeback, fraud, duplicate collection or statutory
rights remain separately governed.

A committed ordinary refund and the corresponding redeemed Plan entitlement
may not coexist. Refund commitment closes/revokes the Plan right; if entitlement
closure cannot be established, refund must fail closed.

If a redeemed paid Plan remains pre-generation refundable and the recipient
reaches irreversible Full Deletion before generation, deletion acts as final
relinquishment of the Plan entitlement and the still-valid ordinary refund is
committed to the authoritative payer/payment relationship before entitlement
destruction, without disclosing the recipient's private deletion/health context.
```

No new DEC identifier is invented here.

This should be integrated with DEC-044 gift/sponsored access, DEC-045 refund boundaries, purchaser-separation law and the v0.31 split-identity amendment during formal governed promotion.

# 30E. PRESSURE-TEST HARDENING

## 30.26 OPS-PT-451...470

| PT | Scenario | Required outcome | Result |
|---|---|---|---|
| `OPS-PT-451` | A pays for B; B redeems; no Plan generated; A requests ordinary DEC-045 refund; B agrees to relinquish | Close B's Plan entitlement and refund authoritative payer/payment relationship A | PASS |
| `OPS-PT-452` | A pays for B; B redeems; no Plan generated; A requests refund; B wants to retain Plan | Refund does not commit; B keeps non-transferable redeemed entitlement | PASS |
| `OPS-PT-453` | A pays for B; B redeems; B independently wants ordinary pre-generation refund; A prefers B keep Plan | B may relinquish B's right; refund goes to A/payment relationship | PASS |
| `OPS-PT-454` | A pays for B; B requests ordinary refund and asks money be redirected to B | Reject by default; B controls entitlement relinquishment but not A's payment beneficiary status | PASS |
| `OPS-PT-455` | Purchaser P, payer A, recipient B differ; B authorises ordinary refund before generation | B relinquishes entitlement; A/payment relationship receives refund; P receives only authorised commercial visibility | PASS |
| `OPS-PT-456` | A requests refund after B redeemed, but Support closes B's entitlement without B authority | Reject; payer request alone is not recipient relinquishment authority | PASS |
| `OPS-PT-457` | B authorises relinquishment, but Plan generation commits before ordinary refund transition commits | Ordinary DEC-045 pre-generation path closes; do not backdate/pretend generation did not occur | PASS |
| `OPS-PT-458` | Ordinary refund commits first while generation worker is racing | Entitlement closes and stale generation cannot fulfil it | PASS |
| `OPS-PT-459` | B completed onboarding/preferences but no Plan generation occurred; B authorises relinquishment | Ordinary pre-generation refund remains available; onboarding alone is not cutoff | PASS |
| `OPS-PT-460` | A asks why B refused or accepted relinquishment | Do not disclose B's private reason/onboarding/Safety data; payer gets commercial status only | PASS |
| `OPS-PT-461` | Paid gift is still unredeemed and payer requests otherwise-valid refund | Existing pre-redemption commercial/gift refund authority applies; recipient relinquishment not required | PASS |
| `OPS-PT-462` | Paid sponsor funds B; B redeemed; sponsor requests ordinary pre-generation refund without B consent | Sponsor cannot unilaterally revoke B's redeemed entitlement through this optional refund path | PASS |
| `OPS-PT-463` | Paid sponsor funds B; B authorises relinquishment before generation | Refund sponsor/payment relationship; close B's entitlement; no private reason disclosed | PASS |
| `OPS-PT-464` | Bulk sponsored offer has redeemed B and an attributable refund amount; sponsor wants refund but B refuses relinquishment | B retains entitlement; optional ordinary refund does not commit for B's redeemed right | PASS |
| `OPS-PT-465` | Zero-price complimentary Plan redeemed; recipient relinquishes before generation | Close grant if authorised; no cash refund created | PASS |
| `OPS-PT-466` | A paid for B; B Full Deletes before Plan generation; ordinary refund still open | At irreversible deletion execution, B's relinquishment is final; refund authoritative payer/payment relationship before entitlement destruction | PASS |
| `OPS-PT-467` | Same as 466, but B cancels deletion within 14 days | No deletion-triggered refund; B keeps entitlement; ordinary refund still requires B relinquishment if later requested | PASS |
| `OPS-PT-468` | A's own account was deleted; B later authorises ordinary pre-generation refund | Use minimum retained Commerce evidence to refund authoritative payer/payment relationship; do not reconstruct A account | PASS |
| `OPS-PT-469` | A has a chargeback/unauthorised-payment claim while B wants to retain redeemed Plan | Do not misuse ordinary refund rule; independent payer-side outcome follows its own authority and any entitlement consequence must be explicitly governed | PASS |
| `OPS-PT-470` | Whole ordinary split lifecycle: A pays → B redeems → no generation → A requests refund → B consents → entitlement closes → refund settles to A | No double authority, no live refunded entitlement, no privacy leakage, no customer-money dead end | PASS |

All 20 new authoring tests pass under the v0.32 working Product/commercial semantics.

These are not an independent certification.

# 30F. CURRENT CANDIDATE STATE

## 30.27 Latest-review blocker disposition

```text
LATEST REVIEW BLOCKER =
  RESOLVED IN WORKING PRODUCT / COMMERCIAL / DECISION AMENDMENT CANDIDATE

ordinary pre-generation third-party refund authority =

  before redemption:
    purchaser/payer commercial authority
    under accepted offer/gift policy

  after redemption:
    redeemed recipient relinquishment required

payer may request after redemption =
  YES

payer may unilaterally terminate redeemed recipient Plan =
  NO

recipient may initiate relinquishment/refund =
  YES

refund beneficiary =
  authoritative payer/payment relationship

payer/recipient disagreement =
  recipient decision controls entitlement surrender
  optional ordinary refund does not commit without recipient relinquishment

committed refund + live entitlement =
  FORBIDDEN

recipient Full Deletion before generation =
  irreversible deletion is final relinquishment
  still-valid ordinary refund commits to payer relationship

payer privacy boundary =
  commercial status only
  no recipient private reason / health / Safety / Plan data
```

## 30.28 Updated Pre-JIT status

```text
PREVIOUS CUMULATIVE PRESSURE TESTS = 450
NEW PRESSURE TESTS = 20
CUMULATIVE PRESSURE TESTS = 470
CONTIGUOUS PT COVERAGE = OPS-PT-001...470

OPS-UPD-001 =
  CORRECTED CANDIDATE CONVERGED
  monotonic first-pilot numeric ceiling + independent admission gate

OPS-UPD-002 =
  CORRECTED / COMPOSED WITH
  duplicate-money,
  split-identity failed-fulfilment,
  and redeemed-gift ordinary-refund semantics

OPS-UPD-003 =
  WORKING CANDIDATE RESOLUTION CONVERGED

OPS-UPD-004 =
  SEMANTICALLY ADJUDICATED IN WORKING PRE-JIT

OPS-UPD-005 =
  CORRECTED CANDIDATE CONVERGED
  ordinary pre-generation intent/refund authority now split-identity complete
  explicit future DEC-045 failed-fulfilment amendment still required

OPS-UPD-006 =
  CORRECTED / COMPOSED WITH
  failed-fulfilment refund survival
  and split payer/recipient deletion

OPS-UPD-007 =
  CORRECTED / COMPOSED WITH OPS-UPD-005
  General Wellness remains non-substitutive

R549 BUNDLE COMPONENT ALLOCATION =
  Assessment R249
  Plan R300

NEW OPS-UPD = 0
NEW OPS-GAP = 0
NEW DOMAIN = 0
NEW ARCHITECTURE MECHANISM = 0

PRE-JIT AUTHORING / HARDENING STATE =
  COMPLETE CANDIDATE
  NOT YET INDEPENDENTLY CERTIFIED

NEXT STAGE =
  FRESH INDEPENDENT HOSTILE / ADVERSARIAL REVIEW
  OF COMPLETE v0.32.0 ARTIFACT

COMPRESSION =
  BLOCKED UNTIL CLEAN INDEPENDENT REVIEW

GITHUB / PR / ACTIONS =
  DEFERRED UNTIL CLEAN REVIEW + COMPRESSION

IMPLEMENTATION =
  NOT AUTHORISED
```

## 30.29 Compression obligations if the next review is clean

Compression must preserve:

- redemption as the authority-transfer boundary for optional ordinary refund;
- before-redemption payer/purchaser authority under gift/offer law;
- after-redemption recipient relinquishment requirement;
- refund to authoritative payer/payment relationship;
- no payer unilateral revocation of redeemed Plan through ordinary refund;
- payer/recipient disagreement outcome;
- recipient Full Deletion pre-generation as final relinquishment + ordinary refund trigger where still valid;
- committed refund and live entitlement may not coexist;
- recipient privacy boundary;
- all v0.31 failed-fulfilment split-identity semantics;
- all v0.30 deletion-survival semantics;
- R249/R300 bundle allocation;
- explicit DEC-045 amendment/supersession requirement;
- monotonic pilot ceiling + independent stop gate.

Compression must remove as current normative law:

- v0.31 wording that leaves an “otherwise applicable ordinary commercial refund” ambiguous after redemption;
- any historical implication that payer/purchaser can revoke redeemed third-party access merely because money came from them.
