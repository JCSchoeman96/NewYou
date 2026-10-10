# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.10.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 10 ONLY — SHARED COHORT / TIME / CORRECTION SEMANTICS PRESSURE TEST
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-pass branch head:** `90b4d4a840ee0ea9a2622578ef9d56979708b513`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.9.0.md` — preserved unchanged.
- **Accepted predecessor result:** Pass 9 accepted by human review.
- **Purpose:** pressure-test the shared cohort-membership, measurement-window, late-arrival and historical-restatement semantics that apply across the six core FP-006 metrics established in accepted Pass 9.
- **Scope boundary:** no Research survey contract, no event catalogue, no storage schema, no vendor/provider selection, no dashboard design, no experimentation platform, no Roadmap promotion work, no Foundation Integrity repair, no FP-006 implementation/JIT authorisation, and no attempt to answer the remaining metric-specific JIT questions for `ANL-METRIC-003..006`.

---

## 1. Authority and accepted working locks carried into Pass 10

Current Product Law, Decision Law and Roadmap require every paid-pilot gate metric, before first paid participation, to prospectively define at least:

- numerator;
- denominator;
- qualifying event/condition;
- measurement window;
- exclusions;
- missing-data treatment;
- cohort; and
- metric-definition version.

Definitions may evolve prospectively. They may not be rewritten retroactively to make an earlier cohort pass.

For small pilot cohorts, reporting must show count and percentage together. Denominator shopping is prohibited. Where non-response is relevant, non-response must remain visible.

Accepted Pass 9 additionally working-locks that:

1. source Domains retain durable business truth;
2. Analytics derives analytical facts/projections/aggregates from those sources and must not create a shadow business lifecycle;
3. missing or unavailable source extracts must not be converted into fabricated success or failure;
4. `ANL-METRIC-001` and `ANL-METRIC-002` are semantically contractable subject to complete prospective JIT lock before first paid participation;
5. `ANL-METRIC-003..006` still require FP-006 JIT working deltas before paid-pilot gating; and
6. `ANL-GAP-003` remains the bounded core metric-contract completion gap.

Pass 10 does not reopen those accepted conclusions.

---

# 2. Shared cohort semantics

## 2.1 A single paid pilot does not imply one denominator across all metrics

The same human pilot cohort may feed several metrics, but the metric populations are not interchangeable.

Examples already fixed by Product Law demonstrate the distinction:

- assessment completion begins from authoritative assessment starters;
- health-onboarding completion excludes assessment-only customers and uses the paid personalised-plan-pathway population that reaches required onboarding;
- plan activation begins from successfully delivered personalised plans;
- the meaningful-seven-day-use denominator is still unresolved;
- the two `≥95%` operational aims still require their own prospectively frozen business-obligation denominator.

Therefore the shared cohort field does **not** authorise Analytics to impose a universal denominator across the six metrics.

## 2.2 Cohort/denominator membership is contract-derived, not Analytics-selected

For each metric:

1. the cohort/population rule must be frozen prospectively before first paid participation;
2. membership must be determined from the authoritative source facts named by that metric contract;
3. Analytics may correlate those facts but may not create eligibility, payment, entitlement, safety, plan-delivery or behavioural truth;
4. participants or obligations may not be added to or removed from the denominator after observing outcomes merely to improve the percentage; and
5. a source-confirmed denominator member may not be silently dropped merely because an analytical extract is incomplete.

A later source-domain lifecycle change — for example refund, reversal, replacement or correction — does not have one universal cross-metric effect. Where such a lifecycle can alter metric membership or classification, the metric contract must state that treatment prospectively.

---

# 3. Shared measurement-window and cutoff semantics

## 3.1 Cutoffs are immutable for the governed metric version

The measurement window/cutoff is part of the required metric definition. Once the paid cohort begins under that definition:

- Analytics may not extend the window because too few successes occurred;
- Analytics may not shorten the window because an early snapshot already passes;
- Analytics may not move the cohort boundary to remove inconvenient denominator members; and
- a later prospective definition change requires a new metric-definition version and applies only prospectively.

The frozen cutoff answers **which business facts are eligible for that metric version**. It is distinct from when Analytics happened to ingest or project those facts.

## 3.2 Analytics ingestion time is not universal business-event authority

Current Domain Law makes Analytics derived from source-domain authority. Therefore Analytics ingestion/arrival time cannot silently become the authoritative time boundary for every metric.

Before first paid participation, each metric contract that needs temporal adjudication must identify the authoritative source time/anchor needed to determine whether a qualifying fact belongs inside the frozen measurement window.

Pass 10 does **not** invent those anchors. In particular:

- the activation window for `ANL-METRIC-003` remains JIT;
- the Day-1 anchor/timezone rule for `ANL-METRIC-004` remains JIT;
- the retry/recovery windows for `ANL-METRIC-005` and `ANL-METRIC-006` remain JIT.

---

# 4. Late-arriving facts and analytical incompleteness

Three cases must remain distinct:

1. **late analytical arrival:** an authoritative source fact belongs to the governed business window but reaches Analytics after the initial analytical snapshot;
2. **late business occurrence:** the business fact itself occurs after the frozen measurement window; and
3. **source correction/invalidation:** the owning Domain later corrects the authoritative truth about a fact relevant to the governed window.

Analytics must not collapse these into one generic “late event” category.

Minimum safe rules are:

- analytical arrival time alone may not redefine source truth;
- a business fact that genuinely occurs outside the frozen window may not be backdated by Analytics to make the metric pass;
- an incomplete or delayed analytical extract must be reported as incomplete/unavailable rather than repaired by denominator deletion or fabricated zero/success; and
- the exact acceptance/reconciliation horizon for a late-arriving in-window fact must be frozen in FP-006 JIT where material to the metric.

This pass therefore resolves the ownership boundary but does **not** invent a universal lateness duration.

---

# 5. Historical restatement versus retroactive redefinition

Two different operations must not be conflated.

## 5.1 Metric-definition change

A change to numerator, denominator, qualifying condition, measurement window, exclusion, missing-data rule, cohort rule or other meaning of the metric requires a new metric-definition version.

It is prospective only. A new definition may not be applied backwards merely to improve an earlier cohort.

## 5.2 Source-truth correction under the same frozen definition

A later authoritative source correction may change the derived value of an earlier metric without changing the metric definition itself.

That kind of restatement is permissible only under a prospectively governed correction/restatement policy. The policy must preserve auditable provenance so an earlier published result is not silently rewritten as though it never existed.

At minimum, FP-006 JIT must decide, where material:

- which authoritative source corrections are eligible for restatement;
- how late a qualifying correction may be reconciled;
- whether/when a cohort result becomes operationally final;
- how the restated value is labelled and traced to the same frozen metric-definition version; and
- how deletion/suppression obligations interact with analytical rebuild/restatement.

Pass 10 does not set a universal finality period.

---

# 6. Small-cohort reporting is already locked

Pass 10 does not reopen whether count-plus-percentage reporting is required.

For each reported gate rate, the visible result must preserve the frozen denominator and show count with percentage, for example:

```text
8 / 10 (80%)
```

The percentage is a derivation from the governed numerator and denominator; it is not a substitute for them.

If the analytical result is incomplete because authoritative source data is unavailable or delayed, that incompleteness must remain visible. It must not be hidden by omitting uncertain denominator members or by reporting only a percentage.

The controlled-pilot survey non-response rule remains outside this pass because the Research path remains blocked by `ANL-GAP-001`; Pass 10 creates no substitute survey authority.

---

# 7. Pressure tests

## ANL-PT-034 — Does one FP-006 paid cohort require one identical denominator across all six core metrics?

**Analysis:** No. Product Law fixes materially different populations for assessment completion, health onboarding and plan activation, while other denominators remain JIT. A universal denominator would override metric-specific Product Law and could distort the funnel.

**Disposition:** `CONFLICT` for universal-denominator interpretation.

---

## ANL-PT-035 — May a measurement window or cutoff move after cohort outcomes are visible?

**Analysis:** No. Window/cutoff is part of the prospectively versioned metric contract. Moving it after observing outcomes is a retroactive definition change and creates denominator/window shopping.

**Disposition:** `CONFLICT`.

---

## ANL-PT-036 — May Analytics use ingestion time as the universal event-time boundary or discard an authoritative in-window fact solely because it arrived late analytically?

**Analysis:** No. Analytics is derived from source-domain truth. The relevant source time/anchor must be prospectively selected by the metric contract. The exact source timestamp and reconciliation horizon remain metric-specific JIT where current authority does not already fix them.

**Disposition:** `NEEDS_WORKING_DELTA` for exact per-metric temporal anchors/horizons; source-ownership boundary is resolved.

---

## ANL-PT-037 — May an authoritative source correction restate a historical rate without changing the metric definition?

**Analysis:** Potentially yes, but only under a prospectively governed correction/restatement policy. The frozen metric-definition version and cutoff remain fixed; the derived value may change because authoritative source truth changed. Historical reporting provenance must not be silently erased.

**Disposition:** `PASS_WITH_REFINEMENT`; exact reconciliation/finality/restatement presentation remains FP-006 JIT.

---

## ANL-PT-038 — May incomplete analytical data be handled by dropping uncertain denominator members?

**Analysis:** No. Product Law requires explicit missing-data treatment and prohibits denominator shopping. Source-confirmed denominator membership cannot be silently removed because Analytics is delayed or incomplete.

**Disposition:** `CONFLICT`.

---

## ANL-PT-039 — Is count-plus-percentage reporting still an open semantic question for the paid pilot?

**Analysis:** No. Product Law and DEC-310 already lock count-plus-percentage reporting for small cohorts. Pass 10 carries the rule; it does not defer or rediscover it.

**Disposition:** `PASS`.

---

# 8. ANL-GAP-003 after Pass 10

**Status:** `OPEN / FP-006 JIT REQUIRED`.

Pass 10 narrows `ANL-GAP-003`; it does not create a new gap identifier.

## Shared semantics resolved enough for JIT preparation

- metric populations/denominators are metric-specific rather than universally shared;
- membership derives from frozen contract + authoritative source facts;
- measurement windows/cutoffs may not be moved after observing outcomes;
- metric-definition changes are prospective only;
- Analytics ingestion time is not universal business-event authority;
- analytical incompleteness may not be repaired through denominator deletion;
- late analytical arrival, late business occurrence and source correction are distinct cases; and
- count-plus-percentage reporting and anti-denominator-shopping are already locked.

## Still requires FP-006 JIT completion before first paid participation

Shared:

- exact source timestamp/anchor where current authority does not already fix it;
- metric-specific late-arrival reconciliation horizon where material;
- restatement/finality policy and auditable restatement presentation.

Metric-specific from accepted Pass 9:

- `ANL-METRIC-003` — exhaustive qualifying action + activation window + replacement-plan treatment;
- `ANL-METRIC-004` — denominator + qualifying engagement + Day-1 anchor/timezone rule;
- `ANL-METRIC-005` — business-obligation denominator + pathway/retry/recovery rules;
- `ANL-METRIC-006` — business-obligation denominator + recovery/refund/reversal/deduplication rules.

No Product, Architecture, Domain or Roadmap amendment is justified by this pass on current evidence.

---

# 9. Pass-10 disposition

**PASS WITH REQUIRED JIT FOLLOW-UP — SHARED COHORT / TIME / CORRECTION INVARIANTS PRESSURE-TESTED; `ANL-GAP-003` NARROWED, NOT RESOLVED.**

The safe working result is:

1. a common paid pilot does not create a common metric denominator;
2. metric cohort/window/version semantics must be frozen prospectively before first paid participation;
3. Analytics cannot move cutoffs, choose a convenient denominator or elevate ingestion time into business authority;
4. late analytical arrival, late business occurrence and source correction require distinct treatment;
5. source-truth correction may justify governed restatement without retroactively redefining the metric;
6. exact restatement/finality and remaining per-metric temporal semantics stay in FP-006 JIT;
7. count-plus-percentage reporting remains already locked;
8. `ANL-GAP-001` and `ANL-GAP-002` remain unchanged; and
9. no event/schema/vendor/experimentation or implementation detail is authorised.

**Recommended next focused pass after human acceptance:** build the smallest owner/question handoff for the unresolved `ANL-METRIC-003..006` JIT decisions — identifying the exact owning Domain(s), question, required authority evidence and fail-closed default for each unresolved semantic — without answering those JIT questions, defining events/storage schemas or starting implementation.
