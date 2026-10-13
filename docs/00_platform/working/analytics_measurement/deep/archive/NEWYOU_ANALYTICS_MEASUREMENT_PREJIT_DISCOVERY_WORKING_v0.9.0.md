# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.9.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 9 ONLY — CORE FP-006 METRIC CONTRACT PRESSURE TEST
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-pass branch head:** `6231403d807e97397137a8b0e157339be21863c1`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.8.0.md` — preserved unchanged.
- **Accepted predecessor result:** Pass 8 accepted by human review.
- **Purpose:** pressure-test the smallest source-owned FP-006 product/operational metric contracts that can proceed independently of the blocked Research survey path.
- **Scope boundary:** no Research survey contract, no event catalogue, no schema, no vendor/provider selection, no dashboard design, no experimentation platform, no Roadmap promotion work, no Foundation Integrity repair, no FP-006 implementation/JIT authorisation.

---

## 1. Why this pass proceeds while ANL-GAP-002 remains open

Pass 8 proved that Roadmap v1.3.0 promotion is blocked by a repository governance/tooling lifecycle gap. Three subsequent repair attempts in isolated verification work did not reach a green targeted suite. This pass does **not** attempt a fourth speculative tooling repair.

The source-owned product metrics below do not depend on the unresolved Research & Feedback activation. Their source authority already exists in current Product/Domain law. Therefore Analytics Pre-JIT can continue on this independent surface while:

- `ANL-GAP-001` remains `UPSTREAM_ACTION_REQUIRED` for the bounded FP-006 Research survey path; and
- `ANL-GAP-002` remains `OPEN / UPSTREAM_ACTION_REQUIRED` for Roadmap promotion integrity/tooling lifecycle.

No current authority route is changed by this pass.

---

## 2. Contract rule carried from Product Law

Before first paid participation every gate metric must prospectively version at least:

- numerator;
- denominator;
- qualifying event/condition;
- measurement window;
- exclusions;
- missing-data treatment;
- cohort;
- metric-definition version.

This pass additionally keeps the Pre-JIT contract fields required by the Analytics workstream:

- authoritative source(s);
- projection/correlation rule;
- deduplication rule;
- late correction treatment;
- refund treatment where relevant;
- deletion/suppression treatment;
- anonymous continuity treatment;
- freshness/incompleteness behaviour;
- limitations.

For small pilot cohorts, every reported rate must show both count and percentage, for example `8 / 10 (80%)`. Denominator selection follows the prospectively frozen metric contract and may not be changed retrospectively to improve the reported result.

A target percentage without these semantics is **not** treated as a complete paid-pilot gate metric contract.

---

# 3. Metric contracts

## ANL-METRIC-001 — Assessment completion rate

**Product target:** `≥ 80%`.

**Population / denominator:** authoritative assessment starters in the applicable FP-006 cohort. A starter exists when the first assessment answer is persisted or submitted.

**Numerator:** starters who produce both:

1. a valid assessment submission; and
2. a successfully produced governed result.

**Exclusions:** people who never become an authoritative starter. Invalid/abandoned attempts after an authoritative starter remain denominator-only unless a stronger current source explicitly invalidates the attempt itself.

**Time rule:** measure from authoritative starter time through the prospectively frozen cohort metric cutoff. The exact cohort cutoff must be fixed before the cohort begins; it may not be changed retroactively to pass the cohort.

**Authoritative sources:** Temperament attempt/answer/submission/result/report provenance (`ANL-EV-005`).

**Projection / correlation:** Analytics derives the rate from Temperament authority; UI page-load/click observations are not needed to manufacture start/completion.

**Deduplication:** count a participant once per governed assessment opportunity included by the prospectively versioned cohort contract. If the product contract permits more than one qualifying assessment opportunity, the cohort contract must state which opportunity is measured; Analytics may not choose retrospectively.

**Late correction:** authoritative Temperament correction/invalidation may restate the metric only under the prospectively governed correction policy; historical report provenance is not silently rewritten.

**Refund treatment:** no direct effect on whether an assessment starter completed; commercial cohort eligibility may be reported separately where required.

**Deletion/suppression:** follow Privacy & Consent/source-domain deletion law. Rebuilds must respect deletion/suppression; Analytics must not preserve a deleted identifiable assessment trail merely to retain the percentage.

**Anonymous continuity:** not required.

**Freshness/incompleteness:** if the authoritative source extract is incomplete/unavailable, publish the metric as incomplete/unavailable rather than treating missing source data as zero or success. A confirmed starter with no qualifying completion by the frozen cutoff is a non-completion.

**Limitations:** this measures governed assessment completion, not report usefulness, correctness of self-reported/book-derived temperament, or paid conversion.

**Pre-JIT state:** `CONTRACTABLE WITH JIT COMPLETION REQUIRED BEFORE FIRST PAID PARTICIPATION`; the remaining cohort cutoff/measurement-window extraction details and metric-definition version must be prospectively frozen before the cohort begins.

---

## ANL-METRIC-002 — Health-onboarding completion rate

**Product target:** `≥ 80%`.

**Population / denominator:** paid participants entitled to a personalised-plan pathway who reach the point where required health onboarding is available.

**Numerator:** denominator participants who provide sufficient required information for a deterministic eligibility outcome.

**Explicit exclusion:** assessment-only customers.

**Pathway rule:** a correctly governed `general_wellness_only`, `professional_review_required` or other deterministic Safety outcome is not automatically a health-onboarding failure if sufficient required information was provided. The metric measures onboarding sufficiency, not whether the participant qualified for automated personalisation.

**Time rule:** from the point required onboarding becomes available through the prospectively frozen cohort metric cutoff. The cutoff must be fixed before paid participation and cannot be changed retrospectively.

**Authoritative sources:** Commerce/Entitlements for paid personalised-plan-pathway population; Health Records for required facts; Safety & Eligibility for deterministic outcome sufficiency (`ANL-EV-006`, `ANL-EV-007`).

**Projection / correlation:** Analytics combines minimum necessary source facts only; raw health detail is not required in Analytics.

**Deduplication:** one participant per qualifying paid personalised-plan pathway within the versioned cohort. Multiple intake edits do not create multiple denominator members.

**Late correction:** a source-domain correction that changes whether sufficient required information existed by the frozen cutoff may restate the metric under the governed correction policy. A later newly supplied fact after the cutoff does not silently make the earlier cohort pass.

**Refund treatment:** refund status does not rewrite historical onboarding completion. If the cohort contract excludes a commercial case prospectively, that exclusion must be explicit and reported rather than denominator-shopped after the fact.

**Deletion/suppression:** Analytics retains only the minimum derived qualification needed under current privacy law; rebuild/backfill must respect deletion/suppression.

**Anonymous continuity:** not required; this is an authenticated paid-pathway metric.

**Freshness/incompleteness:** source-data incompleteness makes the analytical result partial/unavailable; it must not be converted to a fabricated success/failure. Confirmed denominator members lacking sufficient information by cutoff remain non-completions.

**Limitations:** this does not measure clinical appropriateness, plan activation or value.

**Pre-JIT state:** `CONTRACTABLE WITH JIT COMPLETION REQUIRED BEFORE FIRST PAID PARTICIPATION`; the remaining cohort cutoff/extraction details and metric-definition version must be prospectively frozen before the cohort begins.

---

## ANL-METRIC-003 — Personalised-plan activation rate

**Product target:** `≥ 70%`.

**Denominator:** successfully delivered personalised plans.

**Minimum numerator semantics fixed by Product Law:** a genuine post-delivery participant action. Generation or notification alone does not count. A qualifying example is opening the delivered plan and beginning or confirming the first planned action/day.

**Authoritative sources:** Plans & Nutrition plan delivery/lifecycle/activation state; HJP participant action/progress facts where the owning workflow uses them (`ANL-EV-009`).

**What is not yet safely frozen:**

1. the exhaustive qualifying-action set — Product Law gives the governing principle and example, not a complete closed vocabulary;
2. the activation measurement window/cutoff after successful delivery;
3. treatment of corrected/replaced plans where more than one delivered personalised plan exists for one participant.

**Why Analytics cannot fill the gap:** deriving activation from clicks would create an Analytics-owned shadow lifecycle and could count a single open despite Product Law explicitly rejecting that as sufficient by itself.

**Missing/freshness rule already safe:** source incompleteness yields an incomplete metric; it does not create success. A source-confirmed delivered plan can enter the denominator only under the eventual versioned window contract.

**Refund/deletion/late-correction rule:** must follow the eventual owning Plan/Commerce/Privacy lifecycle contract; Analytics may restate derived output only from governed source changes.

**Anonymous continuity:** not required.

**Pre-JIT state:** `NEEDS_JIT_WORKING_DELTA` before first paid participation.

---

## ANL-METRIC-004 — Meaningful seven-day usage rate

**Product target:** `≥ 60%`.

**Numerator semantics fixed by Product Law:** engagement on at least three distinct days in the first seven days, including at least one engagement after Day 1. A single plan open is not meaningful usage.

**Time window:** first seven days anchored to the governed delivery/use-start contract; at least one qualifying engagement must occur after Day 1.

**Authoritative source candidates already resolved:** durable HJP habit/progress/check-in/adherence facts, with Plans & Nutrition supplying the governed plan-delivery anchor; best-effort read/open telemetry may be supplementary only (`ANL-EV-010`). Raw journal text is not required.

**What is not yet safely frozen:**

1. denominator population — current Product wording fixes the meaningful-use threshold but does not explicitly define the denominator for the `≥ 60%` rate;
2. exhaustive qualifying-engagement set — not every click/open is meaningful, and the current authority does not enumerate a closed set;
3. exact anchor for Day 1 where delivery, activation and first planned day differ.

**Why this matters:** choosing “all paid participants”, “all delivered plans”, “all activated plans” or “all eligible participants” changes the metric materially. Analytics may not select the denominator that makes the cohort pass.

**Deduplication:** distinct-day logic must collapse multiple qualifying actions on the same governed local day to one qualifying day; exact timezone/day-boundary semantics remain JIT and must be prospective.

**Late correction/deletion/freshness:** source corrections may restate the derived rate under a governed correction policy; deletion/suppression applies to rebuilds; incomplete source feeds produce partial/unavailable status rather than false zeroes.

**Anonymous continuity:** not required for the core paid-plan measurement.

**Pre-JIT state:** `NEEDS_JIT_WORKING_DELTA` before first paid participation.

---

## ANL-METRIC-005 — Successful plan-generation rate

**Product operational aim:** `≥ 95% successful plan generation`.

**Authoritative sources:** Plans & Nutrition owns generation request/outcome and immutable delivered-plan provenance (`ANL-EV-008`). The denominator source remains dependent on the prospectively selected denominator unit: if the denominator is broader than generation requests, the qualifying population may additionally require Commerce, Entitlements and Safety & Eligibility source truth. Analytics does not own or infer that denominator.

**Current safe statement:** Analytics may derive successful generation only from governed source-domain facts. Plans & Nutrition supplies generation/outcome truth; any broader qualifying-population denominator must come from its authoritative source Domain(s). Generation, successful delivery, General Wellness output, held personalised right and final unfulfillable/refunded outcomes must remain distinct.

**Missing contract semantics:** current Product wording does not explicitly freeze:

- denominator unit (generation requests, participants, eligible personalised-plan obligations, or another governed unit);
- whether a valid General Wellness output belongs in this operational rate or a separate pathway rate;
- whether retries/duplicate requests collapse to one business obligation;
- the measurement window for eventual success after durable retry/recovery;
- exclusions for intentionally blocked/review-required/insufficient-information paths.

**Hard boundary:** `general_wellness_only` must not be counted as fulfilment of a purchased personalised-plan right. The metric contract must not erase that Product/Roadmap distinction.

**Pre-JIT state:** `NEEDS_JIT_WORKING_DELTA`; the `≥95%` target is not usable for paid-pilot gating until the denominator/business-obligation unit and remaining complete metric contract are prospectively frozen before first paid participation.

---

## ANL-METRIC-006 — Successful verified-entitlement-fulfilment rate

**Product operational aim:** `≥ 95% successful verified entitlement fulfilment`.

**Authoritative sources:** Commerce payment/commercial consequence and Entitlements grant/scope/provenance/current access (`ANL-EV-003`, `ANL-EV-004`).

**Current safe statement:** payment success is not entitlement success. Analytics may derive fulfilment only by correlating authoritative Commerce and Entitlements truth.

**Missing contract semantics:** current Product wording does not explicitly freeze:

- denominator unit (verified paid commercial obligations requiring entitlement, entitlement grant intents, orders/components, or another governed unit);
- the window allowed for durable fulfilment/recovery;
- treatment of refunded/reversed/disputed obligations before or after grant;
- deduplication where provider retries or duplicate delivery attempts occur;
- whether a final correctly revoked/closed entitlement after refund is classified outside this operational success rate or as a separate lifecycle outcome.

**Zero-tolerance interaction:** duplicate entitlements remain a separate zero-tolerance integrity failure and must never be hidden by a high aggregate fulfilment percentage.

**Pre-JIT state:** `NEEDS_JIT_WORKING_DELTA`; the `≥95%` target is not usable for paid-pilot gating until the business-obligation denominator, recovery window and remaining complete metric contract are prospectively frozen before first paid participation.

---

# 4. Pressure tests

## ANL-PT-028 — Can a target percentage be treated as a complete paid-pilot gate metric without the Product-Law contract fields?

**Analysis:** No. Product Law expressly requires prospective numerator, denominator, qualifying condition, window, exclusions, missing-data treatment, cohort and version before first paid participation. A percentage alone is not a gate contract.

**Disposition:** `CONFLICT` for denominator/window-by-implication.

---

## ANL-PT-029 — Is assessment completion sufficiently specified for Pre-JIT contracting?

**Analysis:** Yes at semantic/source level. Starter, completion and authoritative owner are explicit. The remaining cohort cutoff/measurement-window extraction details and metric-definition version must be prospectively frozen before first paid participation.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## ANL-PT-030 — Is health-onboarding completion sufficiently specified for Pre-JIT contracting?

**Analysis:** Yes at semantic/source level. Population, exclusion and numerator meaning are explicit; the remaining cohort cutoff/extraction details and metric-definition version must be prospectively frozen before first paid participation.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## ANL-PT-031 — May Analytics close plan-activation semantics from UI telemetry?

**Analysis:** No. Product Law requires a genuine post-delivery action and Domain Law assigns plan activation to Plans. A telemetry-derived shadow activation lifecycle would create competing authority. The closed qualifying-action set and activation window require owning-Domain/FP-006 JIT adjudication.

**Disposition:** `NEEDS_WORKING_DELTA`.

---

## ANL-PT-032 — May Analytics choose the meaningful-seven-day denominator from the most convenient cohort?

**Analysis:** No. Current authority fixes the three-distinct-day threshold but does not explicitly name the denominator for the percentage target. Denominator-shopping would directly violate prospective metric governance.

**Disposition:** `NEEDS_WORKING_DELTA`.

---

## ANL-PT-033 — Are the two `≥95%` operational aims already release-grade metrics?

**Analysis:** No. The targets are authoritative aims, but current authority does not fully freeze the business-obligation denominator, retry/recovery window and lifecycle exclusions. These must be completed prospectively in FP-006 JIT before first paid participation without weakening source-domain ownership.

**Disposition:** `NEEDS_WORKING_DELTA`.

---

# 5. ANL-GAP-003 — Core metric contract completion gap

**Classification:** `FP-006 JIT METRIC-CONTRACT GAP`.

**Not an upstream contradiction:** Product Law intentionally requires prospective metric versioning before paid participation; it does not require every operational denominator to be frozen globally in Product Law.

**Resolved enough for JIT preparation:**

- `ANL-METRIC-001` Assessment completion;
- `ANL-METRIC-002` Health-onboarding completion.

**Requires owning-Domain / FP-006 JIT completion before first paid participation:**

- `ANL-METRIC-003` Plan activation — exhaustive qualifying action + window + replacement-plan treatment;
- `ANL-METRIC-004` Meaningful seven-day use — denominator + qualifying engagement + Day-1 anchor/timezone rule;
- `ANL-METRIC-005` Successful plan generation — business-obligation denominator + pathway/retry/recovery rules;
- `ANL-METRIC-006` Verified entitlement fulfilment — business-obligation denominator + recovery/refund/reversal/dedupe rules.

**Status:** `OPEN / FP-006 JIT REQUIRED`.

This gap does not justify a Product, Architecture or Domain amendment on current evidence.

---

# 6. Pass-9 disposition

**PASS WITH REQUIRED JIT FOLLOW-UP — FIRST CORE METRIC CONTRACT TRANCHE PRESSURE-TESTED; NO NEW UPSTREAM CONTRADICTION.**

The safe working result is:

1. assessment completion and health-onboarding completion are semantically contractable now, with the remaining complete metric-contract details prospectively frozen before first paid participation;
2. plan activation, meaningful seven-day use and both `≥95%` operational aims are **not usable for paid-pilot gating** until their missing denominator/window/qualifying semantics and other required contract fields are frozen prospectively in FP-006 JIT before first paid participation;
3. Analytics must derive from source-domain authority and must not repair those gaps with UI events, denominator choice or retry heuristics;
4. small-cohort reporting must show counts with percentages under the frozen denominator; denominator shopping remains prohibited;
5. Research/value survey metrics remain outside this pass and still depend on `ANL-GAP-001` / Roadmap activation;
6. Roadmap promotion/tooling remains outside this pass and still depends on `ANL-GAP-002`.

**Recommended next focused pass after human acceptance:** pressure-test the remaining cohort/time/correction semantics shared across these six core metrics (cohort membership, cutoff immutability, late-arriving facts and historical restatement) while treating count-plus-percentage reporting and anti-denominator-shopping as already locked Product Law, and without defining event names or storage schemas.