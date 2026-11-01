# NewYou Analytics & Measurement Pre-JIT Decision & Pressure-Test Ledger — Working v0.1.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
CUMULATIVE PRE-JIT LEDGER
```

- **Prepared:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Authority drift at ledger creation:** NONE.
- **Coverage:** Passes 1–3 of Analytics & Measurement Pre-JIT discovery.
- **Source working artifacts:**
  - `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.1.0.md`
  - `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.2.0.md`
  - `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.3.0.md`
- **Purpose:** provide one cumulative, stable working register of decisions, pressure tests, evidence/source mappings, gaps and proposed upstream deltas so later passes cannot silently reinterpret earlier conclusions.

---

## 1. What “locked” means in this ledger

This ledger is **working provenance**, not Product Law, Architecture Law, Domain Law or Roadmap authority.

`WORKING_LOCKED` means:

1. the conclusion is accepted for this Analytics Pre-JIT stream;
2. later passes must treat it as the current working premise;
3. it may not be silently rewritten because a later design would be more convenient;
4. it may be reopened only for one of:
   - changed live authority;
   - new evidence;
   - a demonstrated contradiction;
   - an explicit upstream amendment that changes the premise;
5. any change must be made in a new SemVer successor of this ledger and must identify the predecessor entry being superseded.

`WORKING_LOCKED` **does not** amend or override upstream authority and **does not** authorise implementation.

### Ledger statuses

| Status | Meaning |
|---|---|
| `WORKING_LOCKED` | Current accepted working conclusion; do not silently reopen. |
| `OPEN` | Deliberately unresolved and assigned to a later focused pass. |
| `UPSTREAM_ACTION_REQUIRED` | Working conclusion is clear but an authority-level amendment/action is required before downstream implementation/JIT reliance. |
| `SUPERSEDED` | Replaced by a later explicitly referenced ledger entry or pressure-test result. |
| `DEFERRED` | Valid concern, intentionally outside the current pass/scope. |

---

## 2. Governing source route locked for this stream

Live `main` at ledger creation remains `086ade7b28c000de1c387acb9760e5eb08bb0413`.

README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` route current authority to:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` for analytics/public/frontend concerns.

All entries below are subordinate to that authority route.

---

## 3. Pass-1 working locks — authority and architectural boundary

| Working conclusion | Status | Reopen condition |
|---|---|---|
| Analytics is downstream analytical authority and must not become payment, entitlement, safety, plan, identity, consent or other source-domain business authority. | `WORKING_LOCKED` | Upstream Domain Law change only. |
| FP-006 requires governed measurement without requiring FP-016 experimentation. | `WORKING_LOCKED` | Product/Roadmap amendment only. |
| A/B/n assignment, bucketing, layers, significance/stopping and generic feature-flag infrastructure are outside this Pre-JIT stream. | `WORKING_LOCKED` | Explicit later FP-016 scope. |
| Gate-metric meaning is partly already fixed by Product Law; Analytics may refine contracts but may not denominator-shop or retroactively redefine a prior cohort. | `WORKING_LOCKED` | Product Law amendment. |
| Analytics projections/aggregates must remain rebuildable and cannot resurrect deleted/suppressed identity linkage during rebuild/backfill. | `WORKING_LOCKED` | Privacy/Architecture authority amendment. |
| Analytics failure/freshness degradation must not block or fabricate unrelated authoritative business operations. | `WORKING_LOCKED` | Architecture amendment. |
| Anonymous-to-known continuity is gated and cannot assume covert fingerprinting or unapproved identity stitching. | `WORKING_LOCKED` | Later privacy/attribution pass may define a permitted bounded mechanism, not remove the constraint. |
| Support operational truth was a candidate seam requiring source-owner analysis. | `SUPERSEDED` | Resolved by `ANL-EV-014`. |
| Pilot value-survey truth was a candidate seam requiring dedicated purpose/ownership testing. | `SUPERSEDED` | Resolved by Pass 3 / `ANL-GAP-001` + `ANL-UPD-001`. |
| Small-cohort disclosure/suppression remains untested. | `OPEN` | Dedicated privacy/small-cohort pass. |

---

## 4. Evidence/source-truth register from Pass 2

`ANL-EV-*` means measurement evidence/source-truth record, **not** an analytics event-name catalogue.

### Source-class legend

| Class | Meaning |
|---|---|
| `S1_SOURCE_DOMAIN_AUTHORITY` | Durable business truth owned by the relevant non-Analytics Domain. |
| `S2_ANALYTICS_GOVERNED_FACT` | Permitted first-party analytical/acquisition/operational fact whose purpose is measurement rather than business authority. |
| `S3_BEST_EFFORT_OBSERVATION` | Fallible behavioural/client observation that may be missing, duplicated, delayed or reordered. |
| `S4_EXTERNAL_EVIDENCE` | Provider/offline/external evidence, not NewYou business authority by itself. |
| `S5_SOURCE_AUTHORITY_UNRESOLVED` | Legacy Pass-2 state for a source meaning not yet safely classified. |

### Evidence index

| ID | Measurement question / evidence | Current working result | Status |
|---|---|---|---|
| `ANL-EV-001` | Paid-pilot cohort qualification/context | Commerce/Safety/Temperament/Identity source truth + Analytics acquisition context; no new Domain. | `WORKING_LOCKED` |
| `ANL-EV-002` | Acquisition, invitation/exposure and channel path | Client/provider evidence is weaker; Commerce owns purchase; Analytics owns acquisition evidence/attribution interpretation, not causality. | `WORKING_LOCKED` |
| `ANL-EV-003` | Checkout/payment attempt/verified paid state | Commerce is source authority; provider/browser state is evidence only. | `WORKING_LOCKED` |
| `ANL-EV-004` | Entitlement fulfilment/access consequence | Entitlements owns access; payment success does not equal entitlement truth. | `WORKING_LOCKED` |
| `ANL-EV-005` | Assessment start/submission/governed result | Temperament owns attempt/result; Analytics derives Product-Law start/completion measurement. | `WORKING_LOCKED` |
| `ANL-EV-006` | Health onboarding / sufficient facts | Health Records + Safety/Eligibility own the required source truth; Analytics cannot create an independent health-completeness state. | `WORKING_LOCKED` |
| `ANL-EV-007` | Safety/eligibility pathway outcome | Safety & Eligibility owns pathway truth; `general_wellness_only` is not flattened into personalised-plan failure. | `WORKING_LOCKED` |
| `ANL-EV-008` | Plan generation/delivery/paid-plan fulfilment | Plans owns generation/delivery, Entitlements owns right/consumption, Commerce owns refund closeout. | `WORKING_LOCKED` |
| `ANL-EV-009` | Plan activation | Plans owns activation state; click/open telemetry alone cannot manufacture activation. | `WORKING_LOCKED` |
| `ANL-EV-010` | Meaningful seven-day use | HJP source progress/check-in facts + Plans delivery anchor; Analytics derives distinct-day result. Exact qualifying-action set remains later metric work. | `WORKING_LOCKED` for source route; qualifying-action contract `OPEN`. |
| `ANL-EV-011` | Purchased-library availability versus actual use | Entitlements/Temperament/Plans/Content prove availability; actual read/open may remain best-effort observation. | `WORKING_LOCKED` |
| `ANL-EV-012` | Value/relevance/price-value response | Pass 2 `S5` unresolved state superseded. Pass 3 resolves mandatory FP-006 controlled-pilot instrument response to Research & Feedback source authority, but Roadmap activation is blocked pending `ANL-UPD-001`. | `UPSTREAM_ACTION_REQUIRED` |
| `ANL-EV-013` | Refund truth/dissatisfaction classification | Commerce owns refund/reason truth with source-domain evidence; Analytics derives category aggregates. | `WORKING_LOCKED` |
| `ANL-EV-014` | Support burden/manual intervention | Business corrections stay with source Domains; support contact/minutes/category/intervention can be Analytics operational facts when measurement-only. No Support Domain/universal Task authority justified. | `WORKING_LOCKED` |
| `ANL-EV-015` | Pilot economics / limited-public acquisition economics | Commerce owns commercial truth; external costs/fees remain evidence unless reconciled to an owner; Analytics derives economics without pretending accounting authority. | `WORKING_LOCKED` |
| `ANL-EV-016` | Release-integrity/no-go evidence | Zero-tolerance/readiness claims must come from source Domains + Audit evidence; missing telemetry cannot equal zero incidents. | `WORKING_LOCKED` |

---

## 5. Pass-3 pressure-test register

### ANL-PT-001 — Whole FP-006 survey under Habits, Journals & Progress

- **Question:** Can FP-006 controlled-pilot value/relevance/price-value responses simply reuse FP-005 basic-feedback ownership?
- **Finding:** No. FP-005's carve-out is narrow core-loop progress/self-tracking/usefulness evidence. Price-value, normal-list-price purchase intent, cohort response-rate and version-sensitive release evidence exceed that meaning.
- **Disposition:** `CONFLICT`.
- **Lock:** Do not stretch HJP into a generic survey/feedback owner.
- **Status:** `WORKING_LOCKED`.

### ANL-PT-002 — Analytics owns participant survey response

- **Question:** Can Analytics persist the participant answer as canonical analytical truth?
- **Finding:** No. Domain Law explicitly prevents Analytics from becoming response/business authority merely because the response is measured.
- **Disposition:** `CONFLICT`.
- **Lock:** Analytics may derive permitted aggregates/projections only.
- **Status:** `WORKING_LOCKED`.

### ANL-PT-003 — External survey/provider is source authority

- **Question:** Can survey SaaS/provider/export data be treated as the authoritative participant response?
- **Finding:** No. External state is evidence/collection mechanism, not NewYou business authority.
- **Disposition:** `CONFLICT`.
- **Lock:** Provider choice can never repair source ownership.
- **Status:** `WORKING_LOCKED`.

### ANL-PT-004 — Split one FP-006 instrument across HJP and Research question-by-question

- **Question:** Can one logical pilot survey route some answers to HJP and others to Research solely for ownership convenience?
- **Finding:** Only genuinely independent purposes may have different owners. Splitting one logical instrument to avoid activation creates fragmented version/correction/withdrawal/retry semantics and is unjustified.
- **Disposition:** `PASS_WITH_REFINEMENT` for genuinely separate mechanisms; `CONFLICT` as a workaround for one FP-006 instrument.
- **Lock:** UI composition does not justify mixed ownership; purpose does.
- **Status:** `WORKING_LOCKED`.

### ANL-PT-005 — Bounded Research & Feedback activation in FP-006

- **Question:** Can the Roadmap explicitly activate only the minimum Domain-19 capability required by mandatory FP-006 pilot evidence?
- **Finding:** Yes in principle. Product Law already requires the evidence and Domain Law already owns it. The missing step is Roadmap activation.
- **Disposition:** `NEEDS_WORKING_DELTA`.
- **Lock:** This is the preferred smallest-safe resolution.
- **Status:** `UPSTREAM_ACTION_REQUIRED` via `ANL-UPD-001`.

### ANL-PT-006 — General Research capability becomes MVP

- **Question:** Does one mandatory pilot instrument justify generic research/survey infrastructure in MVP?
- **Finding:** No. Broader campaigns/studies/arbitrary survey-builder capability remain future-gated.
- **Disposition:** `CONFLICT`.
- **Lock:** Bounded activation only; no generic Domain-19 product expansion.
- **Status:** `WORKING_LOCKED`.

---

## 6. Gap register

### ANL-GAP-001 — FP-006 mandatory feedback owner is currently Roadmap-future-gated

- **Type:** Roadmap sequencing / activation gap.
- **Upstream facts:**
  - Product Law requires controlled-pilot value/relevance survey evidence and the price-value/full-price-intent questions.
  - Domain Law assigns bounded lightweight feedback campaign/instrument/participant-response truth to Research & Feedback when that is the purpose.
  - The FP-006 controlled-pilot instrument fits that purpose more directly than HJP progress/self-tracking.
  - Roadmap §3A leaves Research & Feedback future-gated and explicitly disallows silent activation merely because a pilot survey exists.
- **Risk if ignored:** downstream work must violate Domain ownership, violate Roadmap sequencing, or leave a Product-Law gate without a lawful source owner.
- **Disposition:** `CONFLICT`.
- **Required response:** smallest safe Roadmap amendment only; do not repair in Analytics implementation/JIT artifacts.
- **Status:** `UPSTREAM_ACTION_REQUIRED`.

---

## 7. Upstream-delta register

### ANL-UPD-001 — Bounded FP-006 Research & Feedback Roadmap activation

- **Target authority:** Roadmap.
- **Product Law change:** NONE proposed.
- **Domain Law change:** NONE proposed.
- **Required intent:**
  1. keep Research & Feedback generally future-gated / Feature-Pack-unassigned;
  2. explicitly activate a bounded FP-006 mode solely for the mandatory controlled-pilot value/relevance/price-value feedback instrument required by Product Law §21T;
  3. add Research & Feedback to FP-006 Affected Domains for that bounded mode;
  4. state that instrument/question version + participant response are Research & Feedback truth;
  5. state that Analytics derives response-rate/distribution/release evidence only;
  6. preserve FP-005 HJP basic progress/usefulness feedback as a distinct core-loop meaning;
  7. keep broader Research studies/campaigns/arbitrary survey-builder capability future-gated;
  8. create no new Feature Pack merely because Domain 19 participates;
  9. defer exact JIT dossier/proof/resource/provider detail to normal FP-006 Phase 7 adjudication.
- **Disposition:** `NEEDS_WORKING_DELTA`.
- **Status:** `UPSTREAM_ACTION_REQUIRED`.
- **Blocking effect:** blocks implementation/JIT specification of the mandatory FP-006 controlled-pilot instrument until explicitly resolved; does not rewrite unrelated completed source-truth work.

---

## 8. Current working decision locks

The following are the effective working decisions after Pass 3:

1. **Source truth first:** business-material Analytics facts derive from their authoritative Domains wherever such truth exists. `WORKING_LOCKED`.
2. **No shadow authority:** Analytics never becomes the canonical payment, entitlement, assessment, health, safety, plan, consent, Research-response or audit owner. `WORKING_LOCKED`.
3. **No event-first design:** measurement questions and source meaning precede event names/payloads. `WORKING_LOCKED`.
4. **FP-006 without experimentation:** minimum governed pilot measurement does not activate FP-016. `WORKING_LOCKED`.
5. **Support measurement:** measurement-only support burden may live as Analytics operational facts; corrective business actions remain source-Domain truth. `WORKING_LOCKED`.
6. **Value instrument owner:** the mandatory FP-006 controlled-pilot value/relevance/price-value instrument belongs to Research & Feedback by purpose. `WORKING_LOCKED` as a working interpretation, subject only to changed upstream authority/new contradictory evidence.
7. **FP-005 distinction:** ordinary participant progress/basic-usefulness feedback remains HJP where its primary meaning is core-loop progress/self-tracking. `WORKING_LOCKED`.
8. **Roadmap gap:** Domain-19 source ownership is not implementation-authorised for FP-006 until `ANL-UPD-001` is resolved at Roadmap level. `UPSTREAM_ACTION_REQUIRED`.
9. **Broader Research remains out:** this finding does not authorise general Research campaigns/studies/survey-builder capability in MVP. `WORKING_LOCKED`.
10. **No metric formulas yet:** numerator/denominator/window/missing-data/dedupe/late-correction contracts remain downstream; Product-Law meanings already frozen must be preserved. `OPEN` for later focused passes.

---

## 9. Open/deferred queue after Pass 3

| Topic | Current state | Earliest safe next action |
|---|---|---|
| `ANL-UPD-001` Roadmap activation | `UPSTREAM_ACTION_REQUIRED` | Explicit authority-level amendment/review before FP-006 value-instrument JIT/implementation. |
| Core gate metric contracts | `OPEN` | May be pressure-tested later, but `ANL-EV-012` must remain flagged blocked until Roadmap resolution. |
| Duplicate/missing/late/reordered/correction/backfill semantics | `OPEN` | Dedicated pass. |
| Refund/reversal measurement semantics | `OPEN` beyond source owner | Dedicated pass after metric-contract boundaries. |
| Privacy minimisation/deletion/retention | `OPEN` | Dedicated pass; no retention periods inferred. |
| Anonymous-to-known continuity | `OPEN` | Dedicated privacy/attribution pass. |
| Small-cohort disclosure/suppression | `OPEN` | Dedicated privacy/small-cohort pass. |
| Attribution model | `OPEN` | Dedicated pass; attribution remains interpretation, not causality. |
| Dashboards/freshness/incompleteness | `OPEN` | Dedicated pass after metric semantics. |
| Vendor/tool selection | `DEFERRED` | Only after semantic requirements exist. |
| FP-016 experimentation | `DEFERRED` | Later concrete learning need only. |

---

## 10. Change-control rule for future passes

Every future Analytics Pre-JIT pass must:

1. recheck live `main` and the current authority route;
2. compare the new pass against this ledger's latest successor;
3. preserve all `WORKING_LOCKED` conclusions unless a listed reopen condition exists;
4. create stable `ANL-PT-*`, `ANL-EV-*`, `ANL-GAP-*`, `ANL-UPD-*` or later `ANL-METRIC-*` identifiers as appropriate;
5. record disposition and proof route for every pressure test;
6. create a new SemVer successor of this ledger rather than silently rewriting a prior version;
7. explicitly mark superseded entries and their replacement;
8. stop at the correct upstream authority level when a contradiction is exposed.

This ledger is the working anti-drift control for the Analytics & Measurement Pre-JIT stream.
