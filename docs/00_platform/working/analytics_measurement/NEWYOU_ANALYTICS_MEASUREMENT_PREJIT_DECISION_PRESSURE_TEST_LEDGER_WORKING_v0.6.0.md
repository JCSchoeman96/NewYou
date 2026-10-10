# NewYou Analytics & Measurement Pre-JIT Decision & Pressure-Test Ledger — Working v0.6.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
CUMULATIVE PRE-JIT LEDGER
COVERAGE: PASSES 1–12
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-Pass-12 branch head:** `2b1a9993582bc1b7e6ed0d56beec01bfc290335e`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DECISION_PRESSURE_TEST_LEDGER_WORKING_v0.5.0.md` — preserved unchanged.
- **Predecessor coverage:** Passes 1–11.
- **This successor records:** human acceptance of Pass 11, all Passes 1–11 as working-locked, and the Pass-12 metric-contract closure-evidence pressure test pending human acceptance.

---

## 1. Working-lock semantics

`WORKING_LOCKED` means an accepted premise of this Pre-JIT stream and may be reopened only by changed live authority, new contradictory evidence, demonstrated inconsistency or explicit human decision. It is not platform authority.

Status vocabulary:

- `WORKING_LOCKED`
- `OPEN`
- `UPSTREAM_ACTION_REQUIRED`
- `SUPERSEDED`
- `DEFERRED`
- `BLOCKED`
- `PENDING HUMAN ACCEPTANCE`

Pressure-test dispositions:

- `PASS`
- `PASS_WITH_REFINEMENT`
- `NEEDS_WORKING_DELTA`
- `INSUFFICIENT_AUTHORITY`
- `CONFLICT`
- `DEFER`

---

## 2. Current live authority at Pass-12 review point

Live `main`:

```text
086ade7b28c000de1c387acb9760e5eb08bb0413
```

Current live route remains:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when applicable.

README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` were rechecked at this baseline.

The Analytics branch still contains the reviewed-but-unpromoted Roadmap v1.3.0 working candidate from Passes 4–8. It is not current authority.

---

## 3. Accepted evidence/source-truth locks

### Passes 1–8

`ANL-PT-001..027` remain `WORKING_LOCKED` exactly as previously accepted.

Key cumulative result: source ownership, bounded Research routing intent, the Roadmap v1.3.0 semantic candidate, promotion-contract hardening and exact candidate/predecessor/hash evidence remain working-locked. Authority promotion remains blocked by repository routing/Foundation Integrity lifecycle work.

### Pass 9 — core FP-006 metric contract pressure test

`ANL-PT-028..033` remain `WORKING_LOCKED`.

Key accepted results:

- the six core non-survey metrics can proceed independently of the blocked Research survey path;
- `ANL-METRIC-001` and `ANL-METRIC-002` are semantically contractable, with complete prospective JIT lock still required before first paid participation;
- `ANL-METRIC-003..006` require FP-006 JIT completion before paid-pilot gating;
- small-cohort rates show count + percentage and cannot denominator-shop;
- Plans owns plan generation/outcome truth but not automatically every possible generation-rate denominator; and
- Analytics may not create shadow business lifecycles.

### Pass 10 — shared cohort / time / correction semantics

`ANL-PT-034..039` remain `WORKING_LOCKED`.

Key accepted results:

- one paid pilot does not imply one universal denominator;
- measurement windows/cutoffs may not move after outcomes are visible;
- Analytics ingestion time is not universal business-event authority;
- authoritative source correction may restate a derived value only under governed restatement with the frozen definition preserved;
- analytical incompleteness may not be repaired by denominator deletion; and
- count + percentage is already locked.

### Pass 11 — FP-006 JIT owner / question handoff

Pass 11 was human-accepted at branch head:

```text
2b1a9993582bc1b7e6ed0d56beec01bfc290335e
```

`ANL-PT-040..046` are now `WORKING_LOCKED`.

| ID | Accepted result | Disposition |
|---|---|---|
| `ANL-PT-040` | No single source Domain owns the full cross-domain gate-metric definition; FP-006 JIT freezes the contract while source Domains retain component truth | `CONFLICT` for single-Domain metric ownership |
| `ANL-PT-041` | Analytics derived/projection ownership does not authorise it to choose unresolved denominator/action/window semantics | `CONFLICT` |
| `ANL-PT-042` | `ANL-METRIC-003` routes to FP-006 JIT with Plans & Nutrition + HJP source truth; semantic answers remain open | `PASS_WITH_REFINEMENT` |
| `ANL-PT-043` | `ANL-METRIC-004` routes to FP-006 JIT with HJP + Plans and denominator-dependent source owners; denominator/action/day semantics remain open | `PASS_WITH_REFINEMENT` |
| `ANL-PT-044` | `ANL-METRIC-005` routes generation/outcome to Plans with denominator source ownership conditional on the selected business unit | `PASS_WITH_REFINEMENT` |
| `ANL-PT-045` | `ANL-METRIC-006` routes commercial truth to Commerce and grant/access truth to Entitlements; provider state remains evidence only | `PASS_WITH_REFINEMENT` |
| `ANL-PT-046` | A required metric contract still unresolved at first paid participation is not gate-eligible and blocks paid-pilot readiness; it must not be represented as an invented percentage | `PASS` |

---

## 4. Pass 12 — metric-contract closure evidence

`ANL-PT-047..056` are `PENDING HUMAN ACCEPTANCE`.

| ID | Candidate result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-047` | This Pre-JIT document cannot itself mark metrics 003..006 contract-complete | `CONFLICT` for Pre-JIT self-closure | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-048` | Prose answers without exact authority + material source-lifecycle evidence are insufficient | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-049` | Authority citations do not substitute for an explicit answer to every required semantic | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-050` | Implementation tests or dashboard output cannot compensate for an unresolved metric definition | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-051` | Metric-definition version without cohort/effective point permits retrospective ambiguity and is insufficient | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-052` | Closure needs bounded material source-lifecycle evidence, not a copied/shadow Domain lifecycle | `PASS` / `CONFLICT` for shadow copying | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-053` | A JIT Domain Dossier classified as required by the future Gate Manifest cannot be bypassed | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-054` | Pass 12 should not invent a standalone SHA-256 requirement; exact accepted commit SHA + artifact path/version is the minimum reproducible pin unless future governed process requires more | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-055` | Semantic metric closure is distinct from subsequent architectural-proof classification | `PASS` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-056` | JIT semantic answers must be carried into the approved 7C Final Feature Pack Contract before becoming development-entry authority | `CONFLICT` for dossier-only development-entry authority | `PENDING HUMAN ACCEPTANCE` |

Pass-12 candidate closure bundle requires:

1. explicit resolved decision record;
2. exact controlling authority references;
3. bounded material source-owner lifecycle evidence;
4. complete Product-Law metric payload;
5. every additional accepted metric-specific semantic;
6. metric-definition version + cohort/effective point;
7. JIT artifact path/version + exact accepted repository commit;
8. explicit fail-closed rule;
9. contradiction check / upstream stop rule;
10. required 7B dossier satisfaction; and
11. carry-forward into the approved 7C Final Feature Pack Contract.

No metric semantic is answered by Pass 12.

---

## 5. Gap register

### ANL-GAP-001 — bounded FP-006 Research owner is not yet activated by live Roadmap

**Status:** `UPSTREAM_ACTION_REQUIRED`.

Roadmap v1.3.0 semantic candidate exists and is byte/hash reviewed, but live current authority remains v1.2.0 until a complete promotion candidate passes repository integrity.

### ANL-GAP-002 — authority-promotion integrity/tooling lifecycle gap

**Classification:** `GOVERNANCE ROUTING + FOUNDATION INTEGRITY TOOLING GAP`.

**Status:** `OPEN / UPSTREAM_ACTION_REQUIRED`.

The accepted Pass-8 stop remains unchanged.

### ANL-GAP-003 — core FP-006 metric-contract completion gap

**Classification:** `FP-006 JIT METRIC-CONTRACT GAP`.

**Status:** `OPEN / FP-006 JIT REQUIRED`.

Accepted Passes 9–11 define the available core semantics, shared cohort/time/correction invariants, source-owner routing and fail-closed behaviour.

Pass 12 candidate defines what future evidence is necessary before `ANL-METRIC-003..006` may be called semantically complete. It does not close the semantics.

Still JIT-required before first paid participation:

- `ANL-METRIC-003` — qualifying activation actions/window/replacement treatment + temporal/restatement details;
- `ANL-METRIC-004` — denominator/qualifying engagement/Day-1 anchor/timezone + temporal/restatement details;
- `ANL-METRIC-005` — business-unit denominator/General-Wellness classification/retry-recovery/exclusions + temporal/restatement details; and
- `ANL-METRIC-006` — business-unit denominator/recovery/refund-reversal-dispute/deduplication/revocation + temporal/restatement details.

Closure requires exact authority, material source-lifecycle evidence, complete contract payload, prospective version/effective-scope pin, fail-closed rule, required dossier satisfaction and 7C carry-forward.

If any required metric contract remains unresolved at first paid participation, paid-pilot readiness remains `BLOCKED / NO-GO`.

No new gap identifier is created by Pass 12.

---

## 6. Roadmap-promotion working state remains unchanged

The accepted Roadmap v1.3.0 semantic candidate and exact hash evidence from Passes 4–8 remain working-locked.

```text
Roadmap path: docs/00_platform/05_ROADMAP_v1.3.0.md
Roadmap git blob: ddff1c2fa34b3b9185bef8eb72e49f8513479887
Roadmap candidate commit: 25cef5c3eb6462292cb5c34fff2e4c59d3be2078
Roadmap SHA-256: bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261
```

Current live Roadmap remains v1.2.0 on `main`.

No Pass 9–12 work changes the authority-promotion stop.

---

## 7. Effective state after Pass-12 candidate

```text
PASSES 1–11: HUMAN-ACCEPTED / WORKING_LOCKED
PASS 12: PENDING HUMAN ACCEPTANCE

ANL-GAP-001: UPSTREAM_ACTION_REQUIRED
ANL-GAP-002: OPEN / UPSTREAM_ACTION_REQUIRED
ANL-GAP-003: OPEN / FP-006 JIT REQUIRED

CURRENT LIVE ROADMAP: v1.2.0
CURRENT LIVE OPEN WORK: v1.2.59

ROADMAP v1.3.0 SEMANTIC CANDIDATE: WORKING_LOCKED / NOT CURRENT
AUTHORITY PROMOTION: BLOCKED / STOP
FP-006 SURVEY JIT/IMPLEMENTATION: BLOCKED AT ROADMAP AUTHORITY

CORE NON-SURVEY METRIC PRE-JIT:
- PASS 9 CONTRACT TRANCHE: WORKING_LOCKED
- PASS 10 SHARED SEMANTICS: WORKING_LOCKED
- PASS 11 OWNER / QUESTION HANDOFF: WORKING_LOCKED
- PASS 12 CLOSURE-EVIDENCE CONTRACT: PENDING HUMAN ACCEPTANCE

PAID-PILOT METRIC CONTRACTS 003..006: NOT YET COMPLETE
PAID PARTICIPATION IF REQUIRED CONTRACT REMAINS UNRESOLVED: BLOCKED / NO-GO

PHASE 7 ARTIFACTS FOR FP-006: NOT CREATED BY THIS STREAM
ARCHITECTURAL PROOF CLASSIFICATION: NOT SELECTED
IMPLEMENTATION: NOT AUTHORISED
PR: NOT OPENED
MAIN: UNCHANGED
```

---

## 8. Pass-12 candidate disposition

**PASS WITH REQUIRED JIT FOLLOW-UP — THE METRIC-CONTRACT CLOSURE-EVIDENCE REQUIREMENTS ARE DECISION-READY; NO UNRESOLVED METRIC SEMANTIC HAS BEEN ANSWERED.**

No Product, Architecture, Domain or Roadmap amendment is justified by the Pass-12 candidate on current evidence.

**Next focused pass after human acceptance:** pressure-test the minimum FP-006 Phase 7 insertion map for metric-contract closure evidence — 7A routing, required 7B dossier resolution/validation, 7C carry-forward and later proof/release-readiness separation — without creating FP-006 artifacts, proof classifications or metric-semantic answers.
