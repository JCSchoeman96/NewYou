# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.1.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 1 ONLY — AUTHORITY BOOTSTRAP AND BASELINE
```

- **Prepared:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Creation-time / live-main baseline checked:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Main drift at bootstrap:** NONE — creation-time main equals live main.
- **Purpose:** establish the exact governing baseline and ownership/privacy/experimentation boundaries before any Analytics metric-contract or pressure-test pass.
- **Scope of this version:** authority resolution only. No vendor selection, schema, event catalogue, implementation design, A/B/n design, metric contract set, compact pack or implementation work.

---

## 1. Pass discipline

This stream is deliberately executed in separate focused passes. v0.1.0 records only the mandatory authority bootstrap and the minimum boundary conclusions needed to begin later semantic discovery safely.

No `ANL-PT-*`, `ANL-METRIC-*`, `ANL-EV-*`, `ANL-UPD-*` or `ANL-GAP-*` identifier is created in this pass. Candidate seams identified during authority reading are queued for later pressure testing rather than prematurely promoted into findings.

---

## 2. Current authority route resolved from live main

`docs/00_platform/README.md` and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` resolve the current baseline as:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` for analytics/public/frontend concerns.

The uploaded older Project files are orientation snapshots only and are not used as current authority where they differ from the live repository.

Current Open Work states that, for the active FP-001 Phase 7 conditional-dossier adjudication, **Analytics remains NOT REQUIRED**. That statement is scoped to the FP-001 dossier programme. It does not remove the Analytics Domain, alter FP-006 measurement requirements or authorise this Pre-JIT stream to modify current programme state.

---

## 3. Analytics Domain Law baseline

Current Domain Law §6.17 establishes Analytics as downstream analytical authority, not business authority.

### Analytics owns

- governed permitted product/behaviour/operational analytical facts;
- derived projections/read models/materialised aggregates;
- acquisition evidence and attribution interpretations as separate analytical concepts;
- dashboard/report/export analytical projections;
- experiment exposure/outcome measurement facts and aggregates under Experimentation definitions;
- aggregate metric state where business authority is not implied.

### Analytics explicitly does not own

- payment, entitlement, safety, plan, identity, consent or other source-domain business truth;
- experiment configuration, assignment or final governed experiment decision;
- audit/security evidence;
- raw journal text or unnecessary health detail;
- unrelated consequential truths merely because they can be analysed or displayed.

### Analytics lifecycle/invariants already frozen

- governed source fact/observation accepted;
- projected/aggregated;
- refreshed/rebuilt/backfilled;
- retained/anonymised/deleted under privacy law;
- derived models remain rebuildable;
- deletion/suppression applies to rebuild/backfill;
- business-material analytical facts originate from authoritative state where applicable;
- analytics freshness degrades before critical OLTP correctness.

This is the non-negotiable ownership boundary for later passes.

---

## 4. FP-006 measurement baseline

Roadmap FP-006 is the controlled operational/release evidence boundary for the paid core MVP. Current law explicitly rejects the assumption that experimentation is needed to measure the first pilot.

FP-006 requires minimum governed product/operational measurement and staged evidence for:

- internal validation;
- first 10 genuine self-paying adult women in the approved South African launch audience;
- review toward 25;
- review toward maximum 50 in the first paid pilot;
- limited public release;
- later general public release decisions.

Before first paid participation, each gate metric must have versioned numerator, denominator, qualifying event, measurement window, exclusions, missing-data treatment, cohort and metric-definition version. Definitions may change prospectively but may not be retroactively changed to make a prior cohort pass.

Current Product/Roadmap law already fixes important pilot meanings, including:

- assessment-completion denominator semantics;
- health-onboarding denominator semantics;
- plan activation as a genuine post-delivery participant action;
- meaningful seven-day use as engagement on at least three distinct days in the first seven including one after Day 1;
- `general_wellness_only` not being treated as failed personalised-plan activation;
- value survey response visibility and controlled-pilot response threshold;
- support-burden dimensions;
- refund classification/reporting distinctions;
- Day 7 / Day 30 / directional Day 90 evidence boundaries;
- progressive economics measurement without invented early CAC/LTV/margin thresholds.

Later passes must refine these into measurement contracts without silently changing Product Law.

---

## 5. FP-016 experimentation boundary

FP-016 is explicitly later and evidence-led.

Current Roadmap says:

```text
FP-006 minimum governed pilot measurement
→ concrete product learning need
→ FP-016 first-party experimentation
```

FP-016 owns approved first-party A/B/n experimentation only after a real approved decision surface exists. Experimentation owns experiment configuration/version, deterministic assignment and governed decision/learning records. Analytics may supply exposure/outcome measurement facts and aggregates.

This Pre-JIT stream therefore MUST NOT design assignment, bucketing, layers, significance/stopping machinery, feature-flag replacement or a generic experimentation platform.

---

## 6. Privacy & Consent baseline

Privacy & Consent owns purpose-specific consent/lawful-basis state, withdrawals, full-deletion orchestration, retention-policy assignments, legal holds, exports and minimal suppression/replay truth.

Relevant frozen rules:

- consent is purpose-specific and cannot be inferred from unrelated participation;
- withdrawal stops dependent future processing and invalidates derived authority;
- deletion covers live, derived, cached, external and access paths where required;
- restore may not resurrect deleted/withdrawn participant authority;
- pseudonymisation is not automatically irreversible anonymisation;
- Analytics representations are governed deletion/export targets, not Privacy-owned business data.

Analytics Domain Law additionally requires identifiable analytics to be removable/suppressible and excludes raw journal text/raw clinical data by default.

No retention period or legal conclusion is inferred in this pass.

---

## 7. Architecture analytical/read-load baseline

Current Architecture requires:

- PostgreSQL-first authoritative business truth;
- analytical readouts as governed derived models/materialised or cached aggregates;
- rebuildable projections;
- large analytical scans not to starve primary OLTP;
- heavy analytical aggregation/backfill/export work to be bounded and asynchronous where appropriate;
- analytics/experiment failure to degrade measurement/freshness rather than block unrelated authoritative operations;
- derived analytics/search/read models after restore to rebuild only through current privacy/deletion rules;
- replicas, Redis, specialist stores and other acceleration only when evidence justifies them.

`Authority ≠ acceleration` applies to Analytics as elsewhere.

---

## 8. Frontend/public measurement baseline

Current Frontend Experience System fixes these boundaries:

- third-party non-authoritative analytics failure must not break core public/participant use where avoidable;
- public content/navigation should remain useful without arbitrary JavaScript dependence;
- dashboards are projections and expose freshness/data-health states rather than silently presenting missing data as zero;
- canonical metrics have governed semantic/business ownership and versioned meaning;
- dashboard visibility/export does not grant sensitive record access;
- NewYou first-party facts remain authoritative for business results while external analytics data is complementary evidence;
- attribution is not automatically causal proof;
- anonymous-to-known continuity is allowed only under explicit privacy/consent rules and proven architecture;
- covert fingerprinting is prohibited.

---

## 9. Boundary conclusions from Pass 1

### 9.1 Confirmed

1. **Source Domains remain authoritative.** Analytics derives and measures; it does not decide business outcomes.
2. **FP-006 measurement is required without FP-016 experimentation.** Pulling A/B/n machinery forward would violate Roadmap intent.
3. **Gate-metric denominator semantics are partly already Product Law.** Later discovery must not treat all metric meaning as greenfield Analytics design.
4. **Analytics must remain rebuildable and privacy-aware.** Rebuild/backfill cannot resurrect deleted/suppressed identity linkage.
5. **Analytics failure must not become a core-journey failure.** Measurement/freshness yields before authoritative OLTP correctness.
6. **Anonymous-to-known linkage is gated, not assumed.** No covert fingerprinting or implied cross-device identity is authorised.

### 9.2 Candidate seams queued for later passes — NOT YET FINDINGS

These require focused pressure testing before any `ANL-GAP-*` or `ANL-UPD-*` is created:

- **Pilot value-survey truth versus future-gated Research & Feedback:** FP-006 requires value-survey evidence, while the Roadmap explicitly forbids silently pulling Research & Feedback into FP-006 merely because a pilot survey exists. The owning durable truth for the required pilot survey response must be resolved without making Analytics a shadow Research owner.
- **Support operational truth:** Product Law requires support-incidence/minutes/intervention measurement, while the operating model describes a unified support/work presentation over Domain-owned obligations rather than a universal Support business Domain. Later pressure testing must identify the authoritative source fact(s) without inventing ownership for metric convenience.
- **Anonymous acquisition continuity:** FES permits linkage only under explicit privacy/consent rules and proven architecture. Exact permitted continuity for FP-006/limited-public acquisition measurement remains to be bounded.
- **Small-cohort analytical disclosure:** current privacy/minimisation law is strong, but this pass has not established whether additional governed suppression/aggregation semantics are required for rare pilot segments.

These are deliberately left unclassified in v0.1.0.

---

## 10. Pass 1 disposition

**PASS — AUTHORITY BOOTSTRAP COMPLETE.**

The live authority baseline is coherent enough to begin focused semantic pressure testing. No authority amendment is proposed in this pass. No implementation, event catalogue, vendor selection, metric pack or experiment design is authorised.

**Next pass must be selected explicitly and remain narrow.**
