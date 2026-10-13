# NewYou Analytics & Measurement Pre-JIT Decision & Pressure-Test Ledger — Working v0.4.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
CUMULATIVE PRE-JIT LEDGER
COVERAGE: PASSES 1–10
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-Pass-10 branch head:** `90b4d4a840ee0ea9a2622578ef9d56979708b513`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DECISION_PRESSURE_TEST_LEDGER_WORKING_v0.3.0.md` — preserved unchanged.
- **Predecessor coverage:** Passes 1–8.
- **This successor records:** human acceptance of Pass 8 and corrected Pass 9, accepted Pass-9 metric-contract locks, and the Pass-10 shared cohort/time/correction pressure test pending human acceptance.

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

## 2. Current live authority at Pass-10 review point

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

### Pass 3 — source owner / Roadmap gap

`ANL-PT-001..006` remain `WORKING_LOCKED` exactly as recorded in ledger v0.2.0.

Key result: bounded FP-006 Research & Feedback activation is the smallest coherent source-owner repair; general Research activation, Analytics response ownership and provider response authority are rejected.

### Pass 4 — Roadmap amendment candidate

`ANL-PT-007..012` remain `WORKING_LOCKED`.

Key result: Roadmap is the correct semantic authority layer; no Product/Domain/Architecture amendment, no Research Feature Pack and no invented OQ/proof/provider detail.

### Pass 5 — promotion contract hardening

`ANL-PT-013..018` remain `WORKING_LOCKED`.

Key result: semantic successor v1.3.0; exact archive preservation; README/manifest/Open Work promotion collateral; no current FP-001 advancement; hashes must be real; Atlas initially classified as derived follow-up.

### Pass 6 — exact predecessor / patch-contract correction

`ANL-PT-019..021` remain `WORKING_LOCKED`.

Key result: narrow FP-005 and FP-017 anti-contradiction refinements; lawful predecessor is current live Roadmap v1.2.0 blob `5432991071d4d1a7cbd9dc4c8fca48c823129f40`.

### Pass 7 — exact Roadmap candidate

| ID | Result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-022` | Exact Roadmap v1.3.0 candidate blob `ddff1c2...` matches the accepted nine-location semantic patch plus lifecycle metadata | `PASS` | `WORKING_LOCKED` |
| `ANL-PT-023` | Promotion without independently proven SHA-256 is forbidden | `CONFLICT` for promotion-before-hash | `WORKING_LOCKED` rule; blocker superseded by PT-024 proof |

### Pass 8 — hash resolution + integrity stop

Human acceptance is now recorded. The Pass-8 findings below are `WORKING_LOCKED`.

| ID | Result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-024` | Repository-native exact-byte verification proves Roadmap v1.3.0 SHA-256 `bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261` for blob `ddff1c2...` | `PASS` | `WORKING_LOCKED` |
| `ANL-PT-025` | README + manifest + Open Work alone are insufficient under actual Foundation Integrity; active Atlas/HARDEN explicit current routes must be reconciled | `NEEDS_WORKING_DELTA` | `WORKING_LOCKED` |
| `ANL-PT-026` | Foundation Integrity / roadmap regression checks cannot remain permanently pinned to outgoing current filenames after a lawful successor; checks must advance without weakening fail-closed behaviour | `NEEDS_WORKING_DELTA` | `WORKING_LOCKED` |
| `ANL-PT-027` | Historical/source-at-freeze references must not be globally rewritten during current-route promotion | `PASS` | `WORKING_LOCKED` |

### Pass 9 — core FP-006 metric contract pressure test

Corrected Pass 9 was human-accepted at branch head:

```text
90b4d4a840ee0ea9a2622578ef9d56979708b513
```

Accepted artifact:

```text
docs/00_platform/working/analytics_measurement/NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.9.0.md
```

`ANL-PT-028..033` are now `WORKING_LOCKED`.

Key accepted results:

- the six core metric contracts may proceed independently of the blocked Research survey path;
- `ANL-METRIC-001` Assessment completion and `ANL-METRIC-002` Health-onboarding completion are semantically contractable, with complete prospective JIT lock still required before first paid participation;
- `ANL-METRIC-003..006` require FP-006 JIT working deltas before paid-pilot gating;
- small-cohort rates must show count + percentage and may not denominator-shop;
- `ANL-METRIC-005` generation/outcome truth belongs to Plans & Nutrition, while any broader qualifying-population denominator must come from the authoritative source Domain(s) for that denominator;
- no Analytics shadow lifecycle is permitted; and
- `ANL-GAP-003` is `OPEN / FP-006 JIT REQUIRED`.

### Pass 10 — shared cohort / time / correction semantics

| ID | Result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-034` | One paid pilot does not imply one universal denominator across all six metrics | `CONFLICT` for universal-denominator interpretation | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-035` | Measurement window/cutoff may not move after cohort outcomes are visible | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-036` | Analytics ingestion time is not universal business-event authority; exact per-metric source anchors/horizons remain JIT | `NEEDS_WORKING_DELTA` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-037` | Authoritative source correction may restate a derived metric under the same frozen definition only through governed restatement with provenance | `PASS_WITH_REFINEMENT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-038` | Incomplete analytical data may not be repaired by silently dropping source-confirmed denominator members | `CONFLICT` | `PENDING HUMAN ACCEPTANCE` |
| `ANL-PT-039` | Count-plus-percentage reporting is already locked; Pass 10 does not reopen it | `PASS` | `PENDING HUMAN ACCEPTANCE` |

---

## 5. Gap register

### ANL-GAP-001 — bounded FP-006 Research owner is not yet activated by live Roadmap

**Status:** `UPSTREAM_ACTION_REQUIRED`.

Roadmap v1.3.0 semantic candidate exists and is byte/hash reviewed, but live current authority remains v1.2.0 until a complete promotion candidate passes repository integrity.

### ANL-GAP-002 — authority-promotion integrity/tooling lifecycle gap

**Classification:** `GOVERNANCE ROUTING + FOUNDATION INTEGRITY TOOLING GAP`.

Foundation Integrity proved that active derived/governance routing and executable regression expectations still encode the outgoing Roadmap/Open Work baseline. These must be advanced coherently before authority promotion can pass.

**Status:** `OPEN / UPSTREAM_ACTION_REQUIRED`.

### ANL-GAP-003 — core FP-006 metric-contract completion gap

**Classification:** `FP-006 JIT METRIC-CONTRACT GAP`.

**Status:** `OPEN / FP-006 JIT REQUIRED`.

Accepted Pass 9 established the six core metric contracts and separated the contractable metrics from the four metrics requiring owning-Domain JIT completion.

Pass 10 candidate narrows the shared surface:

Resolved enough for JIT preparation:

- metric populations/denominators are metric-specific rather than universally shared;
- membership derives from frozen metric contract + authoritative source truth;
- measurement windows/cutoffs may not be moved after outcomes are observed;
- metric-definition changes are prospective only;
- Analytics ingestion time is not universal business-event authority;
- incomplete Analytics data may not cause silent denominator deletion;
- late analytical arrival, late business occurrence and source correction are distinct; and
- count + percentage / anti-denominator-shopping remain locked.

Still JIT-required before first paid participation:

- exact source timestamp/anchor where not already fixed;
- metric-specific late-arrival reconciliation horizon where material;
- restatement/finality policy and auditable restatement presentation;
- `ANL-METRIC-003` qualifying actions/window/replacement-plan treatment;
- `ANL-METRIC-004` denominator/qualifying engagement/Day-1 anchor/timezone;
- `ANL-METRIC-005` business-obligation denominator/pathway/retry/recovery;
- `ANL-METRIC-006` business-obligation denominator/recovery/refund/reversal/deduplication.

No new gap identifier is created by Pass 10.

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

No Pass 9 or Pass 10 work changes the authority-promotion stop.

---

## 7. Effective state after Pass-10 candidate

```text
PASSES 1–9: HUMAN-ACCEPTED / WORKING_LOCKED
PASS 10: PENDING HUMAN ACCEPTANCE

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
- PASS 10 SHARED SEMANTICS: PENDING HUMAN ACCEPTANCE

IMPLEMENTATION: NOT AUTHORISED
PR: NOT OPENED
MAIN: UNCHANGED
```

---

## 8. Pass-10 candidate disposition

**PASS WITH REQUIRED JIT FOLLOW-UP — SHARED COHORT / TIME / CORRECTION INVARIANTS PRESSURE-TESTED; `ANL-GAP-003` NARROWED, NOT RESOLVED.**

No Product, Architecture, Domain or Roadmap amendment is justified by the Pass-10 candidate on current evidence.

**Next focused pass after human acceptance:** build the smallest owner/question handoff for unresolved `ANL-METRIC-003..006` JIT decisions — exact owning Domain(s), question, required authority evidence and fail-closed default — without answering the JIT questions, defining events/storage schemas or starting implementation.
