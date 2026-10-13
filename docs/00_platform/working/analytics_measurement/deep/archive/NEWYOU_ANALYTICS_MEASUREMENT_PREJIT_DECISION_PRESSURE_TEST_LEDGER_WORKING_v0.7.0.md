# NewYou Analytics & Measurement Pre-JIT Decision & Pressure-Test Ledger — Working v0.7.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
CUMULATIVE PRE-JIT LEDGER
COVERAGE: PASSES 1–13
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-Pass-13 branch head:** `18f23266e26546906f44a33bc906bf1ce4f77bc4`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DECISION_PRESSURE_TEST_LEDGER_WORKING_v0.6.0.md` — preserved unchanged.
- **Predecessor coverage:** Passes 1–12.
- **This successor records:** human acceptance of Pass 12, all Passes 1–12 as working-locked, and the Pass-13 FP-006 Phase 7 insertion-map pressure test pending human acceptance.

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

## 2. Current live authority at Pass-13 review point

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

## 3. Accepted pressure-test state through Pass 12

### Passes 1–8

`ANL-PT-001..027` remain `WORKING_LOCKED`.

Key cumulative result: source ownership, bounded Research routing intent, Roadmap v1.3.0 semantic candidate, promotion-contract hardening and candidate/hash evidence remain working-locked. Authority promotion remains blocked by `ANL-GAP-002`.

### Pass 9 — core FP-006 metric contracts

`ANL-PT-028..033` remain `WORKING_LOCKED`.

Key accepted result:

- six core non-survey metrics are separable from the blocked Research survey path;
- metrics 001/002 are semantically contractable but still need complete prospective JIT lock before first paid participation;
- metrics 003..006 require JIT semantic completion;
- count + percentage and anti-denominator-shopping are locked;
- Plans does not automatically own every generation-rate denominator; and
- Analytics may not create shadow business truth.

### Pass 10 — cohort / time / correction semantics

`ANL-PT-034..039` remain `WORKING_LOCKED`.

Key accepted result:

- denominators are metric-specific;
- windows/cutoffs cannot move after outcomes are visible;
- Analytics ingestion time is not universal business-event authority;
- source correction and metric-definition change are distinct;
- denominator members cannot be deleted to repair analytical incompleteness; and
- count + percentage is already governed.

### Pass 11 — owner / question handoff

`ANL-PT-040..046` remain `WORKING_LOCKED`.

Key accepted result:

- FP-006 JIT freezes the full metric contract;
- source Domains retain component business truth;
- Analytics remains derived-only;
- exact unanswered questions and fail-closed defaults are routed for metrics 003..006; and
- an unresolved required metric at first paid participation is not gate-eligible.

### Pass 12 — closure-evidence contract

Pass 12 was human-accepted at branch head:

```text
18f23266e26546906f44a33bc906bf1ce4f77bc4
```

`ANL-PT-047..056` are now `WORKING_LOCKED`.

Accepted closure bundle requires:

1. explicit resolved decision record;
2. exact controlling authority references;
3. bounded material source-owner lifecycle evidence;
4. complete Product-Law metric payload;
5. every additional accepted metric-specific semantic;
6. metric-definition version + cohort/effective point;
7. JIT/Phase 7 artifact path/version + exact accepted repository commit;
8. explicit fail-closed rule;
9. contradiction check / upstream stop rule;
10. required dossier satisfaction; and
11. carry-forward into the approved 7C Final Feature Pack Contract.

Semantic closure remains distinct from architectural proof and analytical output.

---

## 4. Pass 13 — minimum Phase 7 insertion map

`ANL-PT-057..067` are `PENDING HUMAN ACCEPTANCE`.

| ID | Candidate result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-057` | 7A routes the metric gate; it does not solve JIT semantics | `CONFLICT` for 7A semantic closure | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-058` | A source-domain dossier cannot own the whole cross-domain metric contract | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-059` | Pass 11 source routing does not automatically imply a JIT dossier for every named Domain | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-060` | A conditional dossier capable of changing metric semantics must be explicitly adjudicated before 7C freeze | `CONFLICT` for silent non-adjudication | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-061` | 7C must expose the complete final metric contract; dossier links alone are insufficient | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-062` | Proof classification / Tracer Bullet may not choose missing metric semantics | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-063` | Implementation/hardening may not substitute easier analytical semantics for the frozen contract | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-064` | Release readiness may not rewrite the definition after cohort evidence is visible | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-065` | Pass 13 does not require an Analytics JIT Domain Dossier; future Gate Manifest owns classification | `PASS` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-066` | Unresolved required metric semantics block paid-participation scope; unrelated internal preparation is governed separately and must explicitly exclude the blocked capability if allowed | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-067` | The insertion map does not close ANL-GAP-003 | `PASS` | `PENDING HUMAN ACCEPTANCE` |

Candidate insertion map:

```text
7A
- identify metric gate, affected Domains, unresolved questions and dossier/gate routing
- do not answer metric semantics

7B
- required Domain dossiers resolve / validate Domain-owned lifecycle truth only
- conditional dossiers that could affect the metric are explicitly adjudicated
- do not assign the full cross-domain metric to one dossier

PRE-7C SYNTHESIS
- existing Phase 7 process assembles complete answers from accepted inputs
- no new governed artifact or identifier is invented by Pass 13

7C
- carry the complete explicit final metric contract into development-entry authority
- preserve source-Domain ownership
- paid-participation scope remains blocked while a required contract is unresolved

PROOF / IMPLEMENTATION / HARDENING
- prove and implement the frozen contract
- never choose or rewrite missing semantics

RELEASE READINESS
- trace exact authority -> 7C version/cohort -> source evidence -> proof -> implementation -> analytics
- may fail closed, but may not denominator-shop or redefine the observed cohort
```

Pass 13 does not answer any metric semantic or create any FP-006 Phase 7 artifact.

---

## 5. Gap register

### ANL-GAP-001 — bounded FP-006 Research owner not activated by live Roadmap

**Status:** `UPSTREAM_ACTION_REQUIRED`.

Roadmap v1.3.0 semantic candidate remains working-locked but non-current.

### ANL-GAP-002 — authority-promotion integrity/tooling lifecycle gap

**Status:** `OPEN / UPSTREAM_ACTION_REQUIRED`.

The accepted promotion stop remains unchanged.

### ANL-GAP-003 — core FP-006 metric-contract completion gap

**Status:** `OPEN / FP-006 JIT REQUIRED`.

Passes 9–13 now provide:

- semantic boundaries;
- shared cohort/time/correction invariants;
- owner/question routing;
- closure-evidence requirements; and
- the Phase 7 insertion map.

Still JIT-required before first paid participation:

- `ANL-METRIC-003` — activation action/window/replacement + temporal/restatement semantics;
- `ANL-METRIC-004` — denominator/engagement/Day-1/timezone + temporal/restatement semantics;
- `ANL-METRIC-005` — denominator/General-Wellness/retry-recovery/exclusion + temporal/restatement semantics;
- `ANL-METRIC-006` — denominator/recovery/refund-reversal-dispute/dedup/revocation + temporal/restatement semantics.

Metrics 001/002 also retain their accepted complete prospective JIT-lock requirement.

If a required metric contract remains unresolved at the paid-participation boundary, paid participation remains `BLOCKED / NO-GO`.

No new gap identifier is created by Pass 13.

---

## 6. Roadmap-promotion working state remains unchanged

The accepted Roadmap v1.3.0 semantic candidate and exact hash evidence from Passes 4–8 remain working-locked:

```text
Roadmap path: docs/00_platform/05_ROADMAP_v1.3.0.md
Roadmap git blob: ddff1c2fa34b3b9185bef8eb72e49f8513479887
Roadmap candidate commit: 25cef5c3eb6462292cb5c34fff2e4c59d3be2078
Roadmap SHA-256: bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261
```

Current live Roadmap remains v1.2.0 on `main`.

No Pass 9–13 work changes the authority-promotion stop.

---

## 7. Effective state after Pass-13 candidate

```text
PASSES 1–12: HUMAN-ACCEPTED / WORKING_LOCKED
PASS 13: PENDING HUMAN ACCEPTANCE

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
- PASS 12 CLOSURE-EVIDENCE CONTRACT: WORKING_LOCKED
- PASS 13 PHASE 7 INSERTION MAP: PENDING HUMAN ACCEPTANCE

PAID-PILOT METRIC CONTRACTS 003..006: NOT YET COMPLETE
PAID PARTICIPATION IF REQUIRED CONTRACT REMAINS UNRESOLVED: BLOCKED / NO-GO

FP-006 PHASE 7 ARTIFACTS: NOT CREATED BY THIS STREAM
DOSSIER CLASSIFICATIONS: NOT SELECTED BY THIS STREAM
ARCHITECTURAL PROOF CLASSIFICATION: NOT SELECTED
IMPLEMENTATION: NOT AUTHORISED
PR: NOT OPENED
MAIN: UNCHANGED
```

---

## 8. Pass-13 candidate disposition

**PASS WITH REQUIRED JIT FOLLOW-UP — THE CLOSURE-EVIDENCE CONTRACT HAS A MINIMUM PHASE 7 INSERTION MAP; THE REMAINING SEMANTIC WORK STAYS IN FP-006 JIT.**

No Product, Architecture, Domain or Roadmap amendment is justified by Pass 13 on current evidence.

The remaining risk is over-planning rather than missing routing.

**Recommended next focused pass after human acceptance:** perform a Pre-JIT termination/readiness assessment. Verify whether any further Analytics & Measurement question can legitimately be answered before FP-006 JIT or upstream gap resolution. If not, produce the smallest final Pre-JIT handoff and explicit stop-state rather than continuing speculative design.
