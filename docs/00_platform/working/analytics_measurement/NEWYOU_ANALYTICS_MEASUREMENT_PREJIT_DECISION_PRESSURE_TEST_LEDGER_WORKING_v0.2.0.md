# NewYou Analytics & Measurement Pre-JIT Decision & Pressure-Test Ledger — Working v0.2.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
CUMULATIVE PRE-JIT LEDGER
COVERAGE: PASSES 1–7
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DECISION_PRESSURE_TEST_LEDGER_WORKING_v0.1.0.md` — preserved unchanged.
- **Predecessor coverage:** Passes 1–3.
- **This successor adds:** accepted Passes 4–6 and Pass-7 exact-candidate / promotion-integrity result.
- **Purpose:** preserve stable working decisions, pressure tests, evidence/source-truth records, gaps, proposed upstream deltas and reopening rules so later passes cannot silently reinterpret prior accepted work.

---

## 1. Working-lock semantics

`WORKING_LOCKED` means:

1. accepted as the current premise of this Analytics & Measurement Pre-JIT stream;
2. later passes use it unless a valid reopening condition occurs;
3. it cannot be silently rewritten for convenience;
4. it may be reopened only for changed live authority, new evidence, demonstrated contradiction or explicit upstream amendment/human decision;
5. changes are recorded only in a new SemVer ledger successor with the superseded entry identified.

`WORKING_LOCKED` does **not** amend Product Law, Architecture Law, Domain Law, Roadmap authority, Open Work authority or implementation permissions.

Status vocabulary used here:

- `WORKING_LOCKED`
- `OPEN`
- `UPSTREAM_ACTION_REQUIRED`
- `SUPERSEDED`
- `DEFERRED`
- `BLOCKED`

Pressure-test dispositions remain:

- `PASS`
- `PASS_WITH_REFINEMENT`
- `NEEDS_WORKING_DELTA`
- `INSUFFICIENT_AUTHORITY`
- `CONFLICT`
- `DEFER`

---

## 2. Current authority route at Pass-7 review point

Live `main` rechecked during Pass 7:

```text
086ade7b28c000de1c387acb9760e5eb08bb0413
```

Current live authority routing remained:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when frontend/UI/public/analytics experience concerns apply.

The Analytics branch contains a reviewed Roadmap v1.3.0 **candidate**. That branch candidate is not current authority until governed routing/promotion completes on `main`.

---

## 3. Pass-1 working locks

- Analytics Pre-JIT is bounded to early product + paid-pilot measurement; it is not experimentation-platform design or vendor selection.
- Source Domains own durable business truth; Analytics owns permitted analytical facts/projections/aggregates.
- Event-first design is rejected; source truth and measurement question come first.
- FP-016 experimentation is not activated by FP-006 minimum measurement.
- Candidate seams identified: FP-006 value survey versus future-gated Research; support operational truth; anonymous acquisition continuity; small-cohort disclosure/suppression.

**Pass-1 disposition:** `PASS`.

---

## 4. Source-class legend

- `S1_SOURCE_DOMAIN_AUTHORITY` — durable business truth owned by a source Domain.
- `S2_ANALYTICS_GOVERNED_FACT` — durable analytical/operational fact whose business meaning is analytical and does not replace a source Domain.
- `S3_BEST_EFFORT_OBSERVATION` — telemetry/browser/UI observation that may be delayed, missing, duplicated or reordered.
- `S4_EXTERNAL_EVIDENCE` — provider/offline/external evidence requiring reconciliation/admission before business use.
- `S5_SOURCE_AUTHORITY_UNRESOLVED` — source owner not yet lawfully resolved.

`ANL-EV-*` records are measurement evidence/source-truth contracts, not an event-name catalogue.

---

## 5. Evidence/source-truth register

| ID | Measurement area | Current working source-truth result | Status |
|---|---|---|---|
| `ANL-EV-001` | Paid-pilot cohort qualification/context | Commerce + Safety + Temperament + Identity attributes where lawful; Analytics acquisition context; do not invent permanent Identity truth solely for segmentation | `WORKING_LOCKED` |
| `ANL-EV-002` | Acquisition/invitation/channel | Best-effort anonymous telemetry unless stronger; Communications owns invitation/delivery; Analytics owns acquisition/attribution interpretations; invited pilot ≠ ordinary funnel | `WORKING_LOCKED` |
| `ANL-EV-003` | Checkout/payment | Commerce owns purchase/payment/refund/reconciliation; provider/browser evidence remains external until reconciled | `WORKING_LOCKED` |
| `ANL-EV-004` | Entitlement fulfilment | Entitlements owns access; Commerce supplies causal payment truth; Analytics derives rates | `WORKING_LOCKED` |
| `ANL-EV-005` | Assessment start/completion | Temperament attempt/answer/submission/result authority; UI telemetry is not independent completion truth | `WORKING_LOCKED` |
| `ANL-EV-006` | Health onboarding | Health Records + Safety + Commerce/Entitlements population; Analytics derives metric; exact formula later | `WORKING_LOCKED` |
| `ANL-EV-007` | Safety pathway | Safety owns outcome; Health Records supports facts; Analytics counts; correct General Wellness is not personalised activation failure | `WORKING_LOCKED` |
| `ANL-EV-008` | Plan generation/delivery | Plans owns generation/delivered plan/provenance; Entitlements owns access/consumption; Commerce owns closeout/refund | `WORKING_LOCKED` |
| `ANL-EV-009` | Activation | Plans lifecycle + genuine participant action evidence; single plan open alone is insufficient | `WORKING_LOCKED` |
| `ANL-EV-010` | Meaningful 7-day use | HJP durable behaviour/progress + plan-delivery anchor; Analytics distinct-day derivation; qualifying action set remains later metric-contract work | `WORKING_LOCKED` ownership / `OPEN` formula |
| `ANL-EV-011` | Purchased library availability/use | Entitlements + owning content/report/plan source for availability; actual read/open commonly best-effort; availability ≠ use | `WORKING_LOCKED` |
| `ANL-EV-012` | Value/relevance/price-value response | Research & Feedback is source owner for the mandatory bounded FP-006 controlled-pilot instrument once Roadmap activation is governed; Analytics derives response-rate/distribution/release evidence; FP-005 HJP feedback remains HJP by purpose | `WORKING_LOCKED` owner / `UPSTREAM_ACTION_REQUIRED` activation |
| `ANL-EV-013` | Refunds | Commerce owns refund/reason; Safety/technical evidence may supply reason; Analytics aggregates | `WORKING_LOCKED` |
| `ANL-EV-014` | Support | Business corrections remain with owning Domains/Audit; bounded support contact/minutes/category/intervention may be Analytics operational facts when their sole durable purpose is pilot measurement | `WORKING_LOCKED` |
| `ANL-EV-015` | Pilot economics | Commerce owns payment/refund/settlement; provider fees external until reconciled; staff/founder effort may be Analytics operational fact; Analytics derives CAC/contribution with non-accounting limitation | `WORKING_LOCKED` |
| `ANL-EV-016` | No-go/readiness | Source Domains own duplicate charge/entitlement/plan/safety/exposure truths; Audit owns evidence; Analytics counts; missing telemetry never proves zero incidents | `WORKING_LOCKED` |

---

## 6. Pressure-test register — Passes 3–7

### Pass 3 — source owner / Roadmap gap

| ID | Question/result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-001` | Put whole FP-006 survey under HJP? Rejected; exceeds progress/self-tracking purpose | `CONFLICT` | `WORKING_LOCKED` |
| `ANL-PT-002` | Let Analytics own participant survey response? Rejected shadow Research authority | `CONFLICT` | `WORKING_LOCKED` |
| `ANL-PT-003` | External survey/provider as source authority? Rejected; provider may collect evidence, not own business meaning | `CONFLICT` | `WORKING_LOCKED` |
| `ANL-PT-004` | Split one logical pilot instrument across HJP/Research to avoid activation? Rejected as workaround; separate mechanisms may differ only when purposes genuinely differ | `PASS_WITH_REFINEMENT` / `CONFLICT` workaround | `WORKING_LOCKED` |
| `ANL-PT-005` | Explicitly activate bounded Research & Feedback mode inside FP-006? Smallest coherent repair | `NEEDS_WORKING_DELTA` | `WORKING_LOCKED` |
| `ANL-PT-006` | Pull general Research into MVP? Rejected scope inflation | `CONFLICT` | `WORKING_LOCKED` |

### Pass 4 — Roadmap amendment candidate

| ID | Question/result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-007` | Correct authority layer is Roadmap; Product/Domain/Architecture amendment not justified | `PASS` | `WORKING_LOCKED` |
| `ANL-PT-008` | Editing only §3A + FP-006 is insufficient; Roadmap summaries must remain internally coherent | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-009` | Bounded activation must not generalise Research into MVP | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-010` | New Research Feature Pack? Rejected; Domain ≠ Feature Pack | `CONFLICT` | `WORKING_LOCKED` |
| `ANL-PT-011` | Invent OQ/full dossier/proof/provider/resource detail in Pre-JIT? Rejected; normal FP-006 Phase 7 adjudicates | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-012` | “Roadmap-only amendment” means semantic target only; promotion still needs README/manifest/Open Work collateral | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |

### Pass 5 — promotion contract hardening

| ID | Question/result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-013` | Semantic Roadmap successor should be v1.3.0 and preserve exact v1.2.0 predecessor | `PASS` | `WORKING_LOCKED` |
| `ANL-PT-014` | README + manifest routing are mandatory; exact SHA-256 cannot be guessed | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-015` | Open Work successor records Roadmap change without advancing FP-001/Phase 7C/proof/implementation | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-016` | Delivery Atlas is derived follow-up, not promotion authority | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-017` | §3A no-present-blocker wording must acknowledge normal FP-006 JIT/gate adjudication after bounded activation | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-018` | Exact hashes/certification require exact candidate bytes first | `PASS` | `WORKING_LOCKED` |

### Pass 6 — exact predecessor / patch-contract correction

| ID | Question/result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-019` | FP-005 whole-Domain future-gated wording would contradict bounded FP-006 activation; preserve HJP guardrail and add explicit exception | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-020` | FP-017 whole-Domain unassigned wording would become inaccurate; preserve FP-017 non-ownership while acknowledging bounded FP-006 exception | `PASS_WITH_REFINEMENT` | `WORKING_LOCKED` |
| `ANL-PT-021` | Exact lawful predecessor is current live v1.2.0 blob `54329910...`, not an older same-version PR blob | `PASS` | `WORKING_LOCKED` |

### Pass 7 — exact candidate / promotion-integrity gate

| ID | Question/result | Disposition | Ledger state |
|---|---|---|---|
| `ANL-PT-022` | Exact Roadmap v1.3.0 candidate blob `ddff1c2...` matches only the accepted nine-location semantic patch plus lifecycle metadata | `PASS` | `WORKING_LOCKED` |
| `ANL-PT-023` | May current routing be promoted without an independently proven candidate SHA-256? No; fail closed rather than weaken manifest integrity | `CONFLICT` for promotion-now | `BLOCKED` |

---

## 7. Gap register

### ANL-GAP-001 — FP-006 requires feedback whose rightful Domain is Roadmap-future-gated

**Classification:** `ROADMAP SEQUENCING / ACTIVATION GAP`.

**Working finding:** Product Law requires controlled-pilot value/relevance/price-value evidence; Domain Law assigns the bounded instrument/participant response to Research & Feedback by purpose; Roadmap v1.2.0 leaves Research generally future-gated and not automatically FP-006.

**Current state after Pass 7:** semantic repair candidate exists and passes exact diff review, but live Roadmap authority on `main` remains v1.2.0 until complete promotion integrity/routing is proven.

**Status:** `UPSTREAM_ACTION_REQUIRED`.

**Implementation effect:** STOP for FP-006 controlled-pilot survey JIT/implementation specification that depends on this owner until governed Roadmap promotion completes. Unrelated Analytics Pre-JIT work may continue only in later separately accepted passes.

---

## 8. Upstream-delta register

### ANL-UPD-001 — bounded FP-006 Research & Feedback Roadmap activation

**Semantic target:** Roadmap only.

**No Product Law / Domain Law / Architecture amendment required.**

**Working semantic contract:**

1. Research & Feedback participates in existing FP-006 only for the Product-Law-required controlled-pilot value/relevance/price-value instrument.
2. Governed instrument/question version and participant response lifecycle are Research & Feedback truth.
3. Analytics owns only permitted projections/aggregates/response-rate/value distributions/cohort and release evidence.
4. FP-005 daily/weekly/basic progress/usefulness feedback remains HJP where its purpose is participant self-tracking/progress.
5. Broader Research campaigns/studies/arbitrary instruments/generic survey-builder capability remain future-gated / Feature-Pack-unassigned.
6. No new Research Feature Pack.
7. Normal FP-006 Phase 7 decides minimum Research/Privacy/gate/JIT/proof detail; Pre-JIT does not choose provider/schema/identity mode/retention/proof classification.
8. Voting & Balloting remains future-gated.
9. FP-016 experimentation remains later and is not activated.

**Accepted exact edit surface:** nine Roadmap locations per Pass 6.

**Exact Pass-7 candidate:**

```text
path: docs/00_platform/05_ROADMAP_v1.3.0.md
git blob: ddff1c2fa34b3b9185bef8eb72e49f8513479887
candidate commit: 25cef5c3eb6462292cb5c34fff2e4c59d3be2078
semantic diff: PASS
```

**Exact predecessor preserved:**

```text
archive/05_ROADMAP_v1.2.0.md
blob: 5432991071d4d1a7cbd9dc4c8fca48c823129f40
SHA-256: 601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0
```

**Promotion state:** `UPSTREAM_ACTION_REQUIRED / BLOCKED ON EXACT CANDIDATE SHA-256 + COMPLETE ROUTING INTEGRITY`.

The working promotion-collateral contract is:

`NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_ROADMAP_PROMOTION_COLLATERAL_WORKING_v0.1.0.md`.

---

## 9. Effective working decision locks after Pass 7

1. **Source truth first.** Analytics does not become source authority merely because a fact is useful for measurement.
2. **No shadow authority.** Participant/business truth comes from the owning Domain or a deliberately governed Analytics operational fact where no source-domain business truth is implied.
3. **No event-first design.** Do not start by naming telemetry events.
4. **FP-006 measurement does not activate FP-016.** Experimentation remains later.
5. **Support facts stay narrow.** Analytics may own bounded pilot operational facts such as support minutes/category when that is their sole durable purpose; business corrections remain source-Domain mutations.
6. **Mandatory FP-006 value/relevance/price-value instrument belongs to Research & Feedback by purpose.**
7. **FP-005 ordinary progress/basic usefulness feedback remains HJP.**
8. **Broader Research remains out of MVP.** The bounded FP-006 exception is not a generic survey/research platform.
9. **Roadmap is the only semantic upstream repair needed for ANL-GAP-001.**
10. **No Research Feature Pack.** Domain participation occurs inside existing FP-006.
11. **No new OQ or proof classification is invented by this Pre-JIT stream.** Normal FP-006 Phase 7 owns downstream adjudication.
12. **Exact current Roadmap v1.2.0 bytes are the lawful predecessor.** Historical same-version blobs cannot replace current authority bytes.
13. **Exact candidate blob `ddff1c2...` passes the nine-location semantic diff.** Any byte change requires re-review.
14. **Manifest integrity fails closed.** No SHA-256 guessing, SHA-1 substitution or placeholder routing.
15. **Current programme does not advance because of this amendment.** FP-001/Communications/conditional dossiers/Phase 7C/proof/implementation remain governed by current Open Work.
16. **No metric formulas yet.** Population, numerator, denominator, windows, dedupe, late correction, refunds, deletion, freshness and limitations remain downstream metric-contract work.

---

## 10. Open / deferred queue after Pass 7

| Work item | State |
|---|---|
| Compute exact SHA-256 for candidate blob `ddff1c2...` and build complete Roadmap promotion routing package | `BLOCKED / NEXT UPSTREAM INTEGRITY STEP` |
| README / manifest / Open Work authority promotion | `UPSTREAM_ACTION_REQUIRED` |
| Delivery Atlas reconciliation after successful promotion | `DEFERRED DERIVED FOLLOW-UP` |
| Core gate metric contracts | `OPEN`; FP-006 value-instrument contract remains blocked until Roadmap promotion |
| Duplicate/missing/late/reordered/correction/backfill semantics | `OPEN` |
| Refund/reversal metric semantics beyond source owner | `OPEN` |
| Privacy minimisation/deletion/retention analytics pressure tests | `OPEN` |
| Anonymous-to-known continuity | `OPEN` |
| Small-cohort disclosure/suppression | `OPEN` |
| Attribution | `OPEN` |
| Dashboard/freshness/incompleteness | `OPEN` |
| Vendor/tool selection | `DEFERRED` |
| Experimentation platform / assignment / statistics | `DEFERRED` |

---

## 11. Change-control rule for future passes

Every later Analytics Pre-JIT pass must:

1. recheck live `main`, README and the current authority manifest;
2. compare against this ledger successor;
3. preserve `WORKING_LOCKED` entries unless a valid reopening condition exists;
4. use stable `ANL-*` identifiers;
5. record a disposition and proof route for each new pressure test;
6. create a new SemVer discovery successor and, when ledger state changes, a new SemVer ledger successor;
7. never silently rewrite predecessor working artifacts;
8. explicitly mark superseded entries/replacements;
9. stop at the correct upstream authority when a contradiction is exposed;
10. never claim current authority from a working branch candidate merely because the candidate wording passes review.

---

## 12. Current ledger disposition

**PASS AS CUMULATIVE WORKING RECORD THROUGH PASS 7.**

Pass-7 programme outcome remains:

```text
ROADMAP v1.3.0 SEMANTIC CANDIDATE = PASS
AUTHORITY PROMOTION = BLOCKED / STOP ON UNPROVEN CANDIDATE SHA-256 + COMPLETE ROUTING INTEGRITY
IMPLEMENTATION = NOT AUTHORISED
```
