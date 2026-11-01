# NewYou Analytics & Measurement Pre-JIT Decision & Pressure-Test Ledger — Working v0.5.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
CUMULATIVE PRE-JIT LEDGER
COVERAGE: PASSES 1–11
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-Pass-11 branch head:** `94c0475403f6827790412e3280b0b7edfcf72d6a`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DECISION_PRESSURE_TEST_LEDGER_WORKING_v0.4.0.md` — preserved unchanged.
- **Predecessor coverage:** Passes 1–10.
- **This successor records:** human acceptance of Pass 10, all Passes 1–10 as working-locked, and the Pass-11 FP-006 JIT owner/question handoff pending human acceptance.

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

## 2. Current live authority at Pass-11 review point

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

The Analytics branch still contains the reviewed-but-unpromoted Roadmap v1.3.0 working candidate from Passes 4–8. It is not current authority.

---

## 3. Evidence/source-truth locks from Passes 1–3

- Source Domains own durable business truth; Analytics owns permitted analytical facts/projections/aggregates.
- No event-first design.
- FP-016 experimentation is not activated by FP-006 minimum measurement.
- `ANL-EV-001..016` ownership/source mapping remains working-locked as recorded in ledger v0.2.0.
- `ANL-EV-012`: Research & Feedback is the rightful source owner for the mandatory bounded FP-006 controlled-pilot value/relevance/price-value instrument once Roadmap activation is governed; Analytics derives response-rate/distribution/release evidence; FP-005 HJP feedback remains HJP by purpose.

---

## 4. Pressure-test register

### Passes 3–7

`ANL-PT-001..023` remain `WORKING_LOCKED` exactly as previously accepted.

Key cumulative result: source ownership, bounded Research routing intent, the Roadmap v1.3.0 semantic candidate, promotion-contract hardening and exact candidate/predecessor routing remain working-locked; none of those passes authorises authority promotion or implementation.

### Pass 8 — hash resolution + integrity stop

`ANL-PT-024..027` remain `WORKING_LOCKED`.

Key result: the Roadmap v1.3.0 candidate hash is proven; promotion remains blocked by repository routing/Foundation Integrity lifecycle work, not by a Product/Architecture/Domain contradiction.

### Pass 9 — core FP-006 metric contract pressure test

Corrected Pass 9 was human-accepted at branch head:

```text
90b4d4a840ee0ea9a2622578ef9d56979708b513
```

`ANL-PT-028..033` remain `WORKING_LOCKED`.

Key accepted results:

- the six core non-survey metrics can proceed independently of the blocked Research survey path;
- `ANL-METRIC-001` and `ANL-METRIC-002` are semantically contractable, with complete prospective JIT lock still required before first paid participation;
- `ANL-METRIC-003..006` require FP-006 JIT completion before paid-pilot gating;
- small-cohort rates show count + percentage and cannot denominator-shop;
- Plans owns plan generation/outcome truth but not automatically every possible generation-rate denominator; and
- Analytics may not create shadow business lifecycles.

### Pass 10 — shared cohort / time / correction semantics

Pass 10 was human-accepted after exact-head review. `ANL-PT-034..039` are now `WORKING_LOCKED`.

| ID | Accepted result | Disposition |
|---|---|---|
| `ANL-PT-034` | One paid pilot does not imply one universal denominator across all six metrics | `CONFLICT` for universal-denominator interpretation |
| `ANL-PT-035` | Measurement window/cutoff may not move after cohort outcomes are visible | `CONFLICT` |
| `ANL-PT-036` | Analytics ingestion time is not universal business-event authority; exact per-metric source anchors/horizons remain JIT | `NEEDS_WORKING_DELTA` |
| `ANL-PT-037` | Authoritative source correction may restate a derived metric under the same frozen definition only through governed restatement with provenance | `PASS_WITH_REFINEMENT` |
| `ANL-PT-038` | Incomplete analytical data may not be repaired by silently dropping source-confirmed denominator members | `CONFLICT` |
| `ANL-PT-039` | Count-plus-percentage reporting is already locked | `PASS` |

### Pass 11 — FP-006 JIT owner / question handoff

`ANL-PT-040..046` are `PENDING HUMAN ACCEPTANCE`.

| ID | Candidate result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-040` | No single source Domain owns the full cross-domain gate-metric definition; FP-006 JIT freezes the contract while source Domains retain component truth | `CONFLICT` for single-Domain metric ownership | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-041` | Analytics derived/projection ownership does not authorise it to choose unresolved denominator/action/window semantics | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-042` | `ANL-METRIC-003` routes to FP-006 JIT with Plans & Nutrition + HJP source truth; semantic answers remain open | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-043` | `ANL-METRIC-004` routes to FP-006 JIT with HJP + Plans and denominator-dependent source owners; denominator/action/day semantics remain open | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-044` | `ANL-METRIC-005` routes generation/outcome to Plans with denominator source ownership conditional on the selected business unit | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-045` | `ANL-METRIC-006` routes commercial truth to Commerce and grant/access truth to Entitlements; provider state remains evidence only | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-046` | A required metric contract still unresolved at first paid participation is not gate-eligible and blocks paid-pilot readiness; it must not be represented as an invented percentage | `PASS` | `PENDING HUMAN ACCEPTANCE` |

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

Accepted Passes 9–10 establish the core metric definitions available from current authority, shared prospective cohort/time/correction rules, source-Domain ownership boundaries and the prohibition on denominator/window shopping.

Pass 11 candidate narrows the routing surface without answering the remaining JIT questions:

- **contract decision layer:** FP-006 JIT under Product/Decision/Roadmap authority;
- **`ANL-METRIC-003`:** Plans & Nutrition + HJP source truth;
- **`ANL-METRIC-004`:** HJP + Plans source truth, plus whichever Domain lawfully owns the denominator population selected in JIT;
- **`ANL-METRIC-005`:** Plans generation/outcome truth, plus conditional Commerce/Entitlements/Safety & Eligibility denominator sources where the selected business unit requires them;
- **`ANL-METRIC-006`:** Commerce + Entitlements source truth;
- **Analytics:** derived measurement only after the contract is frozen.

Still JIT-required before first paid participation:

- `ANL-METRIC-003` qualifying activation actions/window/replacement treatment plus temporal/restatement details;
- `ANL-METRIC-004` denominator/qualifying engagement/Day-1 anchor/timezone plus temporal/restatement details;
- `ANL-METRIC-005` denominator/General-Wellness classification/retry-recovery/exclusions plus temporal/restatement details;
- `ANL-METRIC-006` denominator/recovery/refund-reversal-dispute/dedupe/revocation classification plus temporal/restatement details.

If any required metric contract remains unresolved at first paid participation, paid-pilot readiness fails closed as NO-GO. No new gap identifier is created by Pass 11.

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

No Pass 9–11 work changes the authority-promotion stop.

---

## 7. Effective state after Pass-11 candidate

```text
PASSES 1–10: HUMAN-ACCEPTED / WORKING_LOCKED
PASS 11: PENDING HUMAN ACCEPTANCE

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
- PASS 11 OWNER / QUESTION HANDOFF: PENDING HUMAN ACCEPTANCE

PAID-PILOT METRIC CONTRACTS 003..006: NOT YET COMPLETE
PAID PARTICIPATION IF REQUIRED CONTRACT REMAINS UNRESOLVED: BLOCKED / NO-GO

IMPLEMENTATION: NOT AUTHORISED
PR: NOT OPENED
MAIN: UNCHANGED
```

---

## 8. Pass-11 candidate disposition

**PASS WITH REQUIRED JIT FOLLOW-UP — OWNER / QUESTION HANDOFF FOR `ANL-METRIC-003..006` IS DECISION-READY; NO JIT SEMANTICS HAVE BEEN DECIDED.**

No Product, Architecture, Domain or Roadmap amendment is justified by the Pass-11 candidate on current evidence.

**Next focused pass after human acceptance:** pressure-test the closure evidence contract for the four JIT handoffs — exact decision record, authority references, source-owner lifecycle evidence, version pin and fail-closed proof required to mark each metric contract complete before first paid participation — without selecting the semantic outcomes themselves.
