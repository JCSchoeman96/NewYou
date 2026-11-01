# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.22.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.22.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 21 — analytics / measurement semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch parent:** `7e3a95063f75238e5c0882b743d6c1f8e73d6756`
- **Working branch:** `prejit/programmes-learning`
- **Analytics supporting branch reviewed:** `prejit/analytics-measurement` @ `8ed7bc679caf2071cd7059bb4579898230bfdcf7`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.21.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose:** apply the already-corrected Analytics & Measurement Pre-JIT boundary to Programme/Edition/Cohort/Enrolment measurement without reopening generic Analytics discovery or resolving Product-owned Programme completion policy.

> This is an append-only semantic successor. It does not override Product, Architecture, Domain, Roadmap, current Open Work, the Analytics unified handoff, or approved Feature Pack/JIT authority.

> The Analytics unified handoff is supporting working evidence only. Where it conflicts with current authority, current authority wins. `OQ-019` remains Product Review.

---

# 169. Accepted working-lock status entering Pass 21

The user explicitly accepted Pass 20 and instructed the stream to continue.

Therefore Passes 1–20 are now:

`WORKING_LOCKED / NON-AUTHORITATIVE`

The user additionally pointed to the completed Analytics & Measurement Pre-JIT. The live corrected unified handoff was independently located at:

`docs/00_platform/working/analytics_measurement/NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_UNIFIED_HANDOFF_WORKING_v0.1.0.md`

on branch `prejit/analytics-measurement` head `8ed7bc679caf2071cd7059bb4579898230bfdcf7`.

Its explicit stop-state is reused rather than duplicated.

---

# 170. Pass 21 — analytics / measurement semantics

## 170.1 Scope hard stop

This pass asks only:

1. how Programme/Edition/Cohort/Enrolment truth is measured without transferring authority to Analytics;
2. what Programme version/cohort/time/correction provenance a governed metric requires;
3. how repeat enrolment, missing data, late evidence, corrections and restatements affect Programme measurement;
4. where `OQ-019` remains upstream Product policy; and
5. whether any new Programme analytics subsystem/gap is justified.

It does **not** define the programme-specific completion threshold, minimum participation, final check-ins, BI tooling, warehouse technology, event schemas, materialized views, metric storage representation or dashboard UX.

## 170.2 Authority finding

The corrected Analytics handoff already closes generic Analytics discovery:

`CORE ANALYTICS & MEASUREMENT PRE-JIT => HANDOFF-READY / STOP AT JIT BOUNDARY`

Pass 21 therefore applies—not re-designs—that contract.

The safe Programme relationship is:

`authoritative Programme/source facts + frozen metric-definition version -> derived Analytics result`

never:

`Analytics result -> Programme business truth`

`OQ-019` remains the Product-owned seam for programme-specific completion metric policy.

---

# 171. Pass-21 evidence register extension

| ID | Evidence | Finding |
|---|---|---|
| PRG-EV-351 | Live Programme baseline unchanged | Live main remains 086ade7b... and the Programmes branch enters Pass 21 from accepted Pass-20 head 7e3a9506.... |
| PRG-EV-352 | Corrected Analytics Pre-JIT exists as a unified handoff | Branch prejit/analytics-measurement head 8ed7bc67... adds NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_UNIFIED_HANDOFF_WORKING_v0.1.0.md as the corrected operational handoff. |
| PRG-EV-353 | Analytics handoff is working evidence only | The unified Analytics handoff explicitly remains WORKING / NON-AUTHORITATIVE and cannot amend Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority. |
| PRG-EV-354 | Generic Analytics discovery is already closed | The corrected Analytics handoff says CORE ANALYTICS & MEASUREMENT PRE-JIT is HANDOFF-READY / STOP AT JIT BOUNDARY and no further generic Analytics discovery pass is justified. |
| PRG-EV-355 | Analytics owns derived analytical representations only | Domain Law assigns analytical event/fact and analytical projection/aggregate/dashboard to Analytics as DERIVED from authoritative sources; those projections are rebuildable. |
| PRG-EV-356 | Programme lifecycle truth remains Programmes-owned | Domain Law assigns Edition/Cohort/Enrolment/completion and challenge participation/completion to Programmes & Challenges. |
| PRG-EV-357 | Nuwe Jy analytics must preserve repeat-enrolment history | DEC-219 requires health-aligned analytics and preservation of repeat-enrolment history. |
| PRG-EV-358 | Programme completion thresholds remain unresolved Product Review | OQ-019 remains PRODUCT REVIEW and requires programme-specific minimum participation, final check-ins and completion thresholds before each programme is published. |
| PRG-EV-359 | Gate metric contracts are prospectively versioned | Current Product Law/DEC-310 require numerator, denominator, qualifying event, measurement window, exclusions, missing-data treatment, cohort and metric-definition version for governed gate metrics, with no retroactive rewriting to make prior cohorts pass. |
| PRG-EV-360 | Small-cohort denominator gaming is forbidden | Current Product/Roadmap metric law requires counts with percentages for small cohorts and prohibits denominator shopping. |
| PRG-EV-361 | Metric membership comes from source authority | The Analytics handoff states denominator membership is determined by governing source truth under the frozen metric definition; Analytics cannot opportunistically add/remove members. |
| PRG-EV-362 | Occurrence, ingestion and correction time are distinct | The Analytics handoff requires authoritative business occurrence, analytical arrival/ingestion and source correction/supersession to remain separate. |
| PRG-EV-363 | Source corrections may restate derived results | The Analytics handoff permits governed analytical restatement after source correction while forbidding Analytics from rewriting source truth. |
| PRG-EV-364 | Missing data is not a hidden outcome | The Analytics handoff states missing/incomplete analytical data is not automatic exclusion, success, failure or zero unless the governing contract explicitly says so. |
| PRG-EV-365 | Metric machinery is applied only where material | The Analytics handoff explicitly rejects forcing timezone, reversal, retry or replacement machinery into every metric merely for symmetry. |
| PRG-EV-366 | Analytics failure cannot become business failure | Architecture states experiment/analytics failure may degrade measurement/freshness but cannot block unrelated authoritative business operations or fabricate evidence. |
| PRG-EV-367 | Historical Programme explanation already has version/provenance anchors | Accepted Pass 20 preserves ProgrammeVersion, Edition/Cohort/schedule context, exact ContentVersion/locale, rule basis, minimum source-owner references and correction lineage. |
| PRG-EV-368 | Repeat Enrolments are distinct attempts | Pass 20 and DEC-219 preserve separate historical attempts even when the same participant repeats the same ProgrammeVersion. |
| PRG-EV-369 | Duplicate/retry execution must not multiply measured business effects | Accepted Pass 18 requires duplicate-safe business effects and current-owner reconciliation rather than treating repeated jobs/observations as new business truth. |
| PRG-EV-370 | HJP remains source owner for behavioural participation evidence | Habits, Journals & Progress owns habit occurrences, behavioural/progress/adherence entries and private journal/reflection truth; Programmes consumes only governed consequences/minimum provenance. |
| PRG-EV-371 | Events remains source owner for attendance | Events & Live owns attendance/check-in; Analytics and Programmes may read that fact but provider telemetry does not replace Events authority. |
| PRG-EV-372 | Communications observations do not become Programme engagement truth | Message delivery/open/click evidence remains Communications-owned operational observation and is not Programme completion/participation evidence by default. |
| PRG-EV-373 | Metric-definition change and source correction are different operations | A prospective new metric definition changes how future measurement is interpreted; a source correction may restate a prior result under the same frozen definition without retroactively changing that definition. |
| PRG-EV-374 | Research/survey measurement has its own activation seam | The Analytics handoff keeps governed Research/Feedback survey measurement behind ANL-GAP-001 / current Roadmap activation and does not make Research a default FP-006 or Programme capability. |
| PRG-EV-375 | Analytics ANL-GAP-003 does not resolve OQ-019 | ANL-GAP-003 remains an FP-006 JIT metric-contract gap for the paid-pilot metrics; it is not authority for Programme-specific completion thresholds or Nuwe Jy completion semantics. |

---

# 172. Pass-21 semantic model

## 172.1 Four separate dimensions

1. **Programme/source truth** — Programmes and other owning Domains.
2. **Metric definition** — governed prospective analytical meaning/version.
3. **Analytical result** — Analytics-owned derived fact/aggregate/projection.
4. **Restatement/provenance** — why a derived result changed without rewriting source history or the metric definition.

No dimension silently becomes another.

## 172.2 Minimum Programme analytical provenance

Where material to a governed Programme metric, preserve/reference:

- Programme / ProgrammeVersion;
- Edition/Cohort;
- Enrolment/attempt identity;
- metric-definition version;
- denominator/cohort membership basis;
- authoritative occurrence/window anchor;
- material timezone/day-boundary basis;
- source-owner references actually used;
- correction/restatement lineage; and
- count + percentage context for small cohorts.

This is analytical provenance, not a second Programme source of truth.

---

# 173. Pass-21 pressure tests

| ID | Test | Disposition | Key conclusion / route |
|---|---|---|---|
| PRG-PT-867 | Analytics completion percentage is written back as the participant's Programme completion state | REJECT | Analytics owns the derived percentage; Programmes owns individual completion truth. |
| PRG-PT-868 | Dashboard count disagrees with Programmes and is used to correct Enrolment state | REJECT | A derived dashboard cannot mutate or override the Programme owner. |
| PRG-PT-869 | Completion-rate denominator excludes incomplete participants after results are seen | REJECT / DENOMINATOR SHOPPING | Membership must follow the prospective metric contract/source truth. |
| PRG-PT-870 | Abandoned or withdrawn Enrolments are excluded because they lower the rate | CONTRACT-DEPENDENT / NO ANALYTICS INVENTION | Their treatment must be prospective in the metric definition; Analytics cannot decide after observing outcomes. |
| PRG-PT-871 | Repeat enrolments by one participant are deduplicated into one attempt by default | REJECT | DEC-219 preserves repeat-enrolment history; attempt-level metrics keep attempts distinct unless an explicitly person-level metric says otherwise. |
| PRG-PT-872 | Completion rates pool ProgrammeVersion v1 and v2 without disclosure | REJECT BY DEFAULT | Different governed Programme semantics require stratification or an explicitly valid cross-version metric contract. |
| PRG-PT-873 | Two Editions with materially different schedules are silently pooled into one cohort metric | REJECT BY DEFAULT | Edition/schedule context can materially change opportunity windows; pooling requires an explicit defensible metric definition. |
| PRG-PT-874 | Metric definition changes halfway through an Edition and new rules are applied immediately to the same observed cohort | REJECT | Definitions are prospective/versioned; mid-observation surgery undermines comparability. |
| PRG-PT-875 | A new completion metric definition is applied retroactively to make an earlier cohort pass | REJECT | Current Product metric law expressly forbids retroactive rewriting for observed cohorts. |
| PRG-PT-876 | Events corrects attendance after reporting and Analytics restates the rate under the same metric definition | PASS | Source correction may drive governed analytical restatement with provenance. |
| PRG-PT-877 | A restated metric silently overwrites the previously published result with no lineage | REJECT | Preserve definition version and restatement/correction provenance. |
| PRG-PT-878 | Participant action occurred inside the window but Analytics ingested it after the cutoff | CONTRACT-DEPENDENT | Use authoritative occurrence plus the frozen late-evidence/restatement policy, not ingestion time alone. |
| PRG-PT-879 | An event occurred outside the window but arrived before cutoff and is counted | REJECT | Fast ingestion cannot move authoritative business occurrence into the measurement window. |
| PRG-PT-880 | Retry emits duplicate analytical facts and doubles activity count | REJECT | Measurement must converge on the logical authoritative effect rather than technical retry multiplicity. |
| PRG-PT-881 | Analytics misses an event while Programmes source truth is intact | MEASUREMENT DEGRADED / BUSINESS CONTINUES | Repair/reconcile measurement; do not fabricate or block Programme truth. |
| PRG-PT-882 | Analytics outage blocks participant completion or content release | REJECT | Analytics failure cannot block unrelated authoritative Programme operations. |
| PRG-PT-883 | Dashboard says 100% complete while Programmes owner records 90% | PROGRAMMES WINS | Analytics is derived and must be rebuilt/reconciled. |
| PRG-PT-884 | Programme owner corrects an individual from completed to incomplete after source correction | PASS WITH RESTATEMENT | Analytics may restate affected aggregates; post-award certificate consequence remains PRG-GAP-002. |
| PRG-PT-885 | Programme owner applies a governed exemption/substitution and Analytics still counts the participant as failed | REJECT STALE PROJECTION | Analytics must derive from current authoritative Programme consequence under the frozen metric definition. |
| PRG-PT-886 | Habit occurrence directly counts as Programme completion without Programme mapping | REJECT | HJP source evidence requires the governed Programme requirement/satisfaction mapping. |
| PRG-PT-887 | Email open is counted as Programme participation/completion by default | REJECT | Communications observation is not Programme participation truth unless a separately approved analytical metric explicitly measures communication engagement and is labelled as such. |
| PRG-PT-888 | Provider attendance telemetry is counted without Events authoritative attendance | REJECT | Events owns attendance; provider telemetry is evidence only. |
| PRG-PT-889 | Historical cohort is segmented using today's ProgrammeVersion instead of the attempt's version | REJECT | Use historical ProgrammeVersion/attempt provenance. |
| PRG-PT-890 | Participant timezone changes and earlier day-based engagement is rebucketed under the new timezone | REJECT | Historical day/window interpretation must use the material timezone/effective context that governed the event/metric. |
| PRG-PT-891 | A cohort metric uses participant-local days but does not preserve which timezone applied | REJECT / INCOMPLETE PROVENANCE | If timezone is material, the basis must be historically explainable. |
| PRG-PT-892 | UTC is used for a day-based adherence metric merely because it is easy | REJECT IF CONTRACT REQUIRES OTHER DAY BOUNDARY | Technical convenience cannot redefine the governed metric. |
| PRG-PT-893 | Late enrolment creates an ambiguous Day-1 anchor and Analytics chooses enrolment time unilaterally | REJECT | The Programme/metric contract must define the anchor; Analytics cannot invent it. |
| PRG-PT-894 | Paused Enrolments are removed from denominator by default | REJECT | Pause treatment belongs in the prospective Programme metric contract/OQ-019 resolution. |
| PRG-PT-895 | Safety-restricted participants are excluded after outcomes are known | REJECT | Any exclusion must be prospectively defined and source-authoritative; Analytics cannot improve rates by retrospective exclusion. |
| PRG-PT-896 | Entitlement loss is counted as Programme completion failure | REJECT BY DEFAULT | Access truth and Programme completion are separate; a metric may analyse access effects but cannot rewrite participant outcome meaning. |
| PRG-PT-897 | Edition cancellation automatically counts all Enrolments as failures | REJECT / PRG-GAP-003 | Exceptional Edition lifecycle/remedy semantics are unresolved Product law. |
| PRG-PT-898 | Cancelled and normally completed Editions are silently combined into one completion-rate trend | REJECT BY DEFAULT | Exceptional lifecycle context must be segmented or explicitly governed before comparison. |
| PRG-PT-899 | Analytics invents an 80% Nuwe Jy completion threshold because OQ-019 is still open | REJECT / STOP AT PRODUCT | OQ-019 is Product Review; Pass 21 cannot resolve it. |
| PRG-PT-900 | Product manager changes the threshold retrospectively after seeing a weak cohort | REJECT | Prospective metric-definition versioning forbids this. |
| PRG-PT-901 | FP-014 Foundation Programme automatically reuses Nuwe Jy metric thresholds | REJECT | Programme-specific thresholds are not generic Programme law; FP-014 gets its own governed lens. |
| PRG-PT-902 | Analytics derives 'requirements satisfied / requirements applicable' as a progress percentage | PASS AS DERIVED PROJECTION | It must be clearly labelled derived and cannot replace authoritative Programme completion/state. |
| PRG-PT-903 | Derived progress percentage rounds to 100% and writes completion=true | REJECT | A presentation/analytical projection cannot author completion. |
| PRG-PT-904 | Analytics fills a missing Programme completion row based on inferred activity evidence | REJECT | Missing owner truth is not permission for Analytics to infer business authority. |
| PRG-PT-905 | Small cohort report shows only 80% without 8/10 | REJECT | Current metric law requires counts with percentages for small cohorts. |
| PRG-PT-906 | A governed Programme gate report shows a count but omits denominator/window/definition version | REJECT / INCOMPLETE CONTRACT | The result is not safely interpretable without its governing metric contract/provenance. |
| PRG-PT-907 | Unknown source facts are coerced to zero failures for easier reporting | REJECT | Missing data is not automatically failure, success or exclusion. |
| PRG-PT-908 | Lawful participant deletion changes a later recomputation and Analytics reconstructs deleted source data from cached extracts | REJECT | Privacy/deletion authority outranks reproducibility; report limitations rather than resurrecting deleted data. |
| PRG-PT-909 | Analytics stores raw private journal text to support future segmentation | REJECT | Use minimised approved facts; HJP/Privacy retain raw private authority. |
| PRG-PT-910 | Experiment assignment alters Programme completion semantics | REJECT | Experimentation/Analytics cannot override Programme lifecycle authority or protected invariants. |
| PRG-PT-911 | Two cohort reports use different metric-definition versions but a trend line presents them as directly comparable | REJECT WITHOUT DISCLOSURE/SEGMENTATION | Definition version is material analytical provenance. |
| PRG-PT-912 | Source corrections legitimately change a historical dashboard aggregate | PASS WITH RESTATEMENT PROVENANCE | Derived results may change under the same frozen definition after owner correction; do not hide the restatement. |
| PRG-PT-913 | A material approved report is later reopened without its original time-window/timezone/filter context | REJECT / INCOMPLETE REPORT PROVENANCE | Governed reporting must preserve the context needed to interpret the result. |
| PRG-PT-914 | Facilitator receives unrestricted participant-level analytical exports because they run the cohort | REJECT BY DEFAULT | Role/privacy/minimum-necessary boundaries still apply; facilitation does not grant universal analytical data access. |
| PRG-PT-915 | Nuwe Jy creates its own authoritative analytics/completion table separate from Programmes | REJECT | Nuwe Jy is not a separate Domain; Analytics remains derived and Programmes remains lifecycle owner. |
| PRG-PT-916 | Programme metrics trigger a new warehouse/Kafka/ClickHouse/Redis authority before PostgreSQL limits are measured | REJECT / DEFER_YAGNI | Architecture remains PostgreSQL-first; scale infrastructure requires evidence and cannot become business authority. |

---

# 174. Pass-21 gap / upstream-boundary adjudication

No new `PRG-GAP` or `PRG-UPD` is justified.

## OQ-019

**Status remains:** `PRODUCT REVIEW`.

Pass 21 does not define:

- programme-specific minimum participation;
- final check-ins;
- completion thresholds; or
- whether a particular derived metric is a release/commercial gate for Nuwe Jy or any later Programme.

Those are Product-policy decisions before publication, not Analytics implementation choices.

## Analytics Pre-JIT gaps

- `ANL-GAP-001` remains the separate Research/survey Roadmap activation seam.
- `ANL-GAP-002` remains retired/reclassified as ordinary Roadmap-promotion collateral.
- `ANL-GAP-003` remains `OPEN / FP-006 JIT REQUIRED` for the corrected FP-006 metric contract.

None of those identifiers is silently imported as Programme Domain Law.

Existing Programme gaps `PRG-GAP-002`, `003`, `007` and `011` retain their prior responsibilities.

---

# 175. Pass-21 refinements

| ID | Refinement | Effect |
|---|---|---|
| PRG-REF-289 | Reuse the corrected Analytics unified handoff instead of reopening generic Analytics discovery. | Pass 21 is a Programme seam application, not a duplicate Analytics Pre-JIT. |
| PRG-REF-290 | Keep individual Programme lifecycle truth and analytical aggregate truth explicitly separate. | Prevents dashboards/percentages from becoming completion authority. |
| PRG-REF-291 | Version every governed Programme metric definition prospectively. | Preserves comparability and prevents retrospective target surgery. |
| PRG-REF-292 | Source-authoritative denominator membership is mandatory. | Prevents denominator shopping and post-hoc exclusion. |
| PRG-REF-293 | Segment/retain ProgrammeVersion in analytical provenance. | Prevents later Programme semantics from rewriting cohort interpretation. |
| PRG-REF-294 | Segment/retain Edition/Cohort and material schedule context where it affects opportunity/window meaning. | Supports fair comparisons without overcapturing irrelevant schedule detail. |
| PRG-REF-295 | Treat repeat Enrolments as distinct attempts unless a metric is explicitly person-level. | Preserves DEC-219 history. |
| PRG-REF-296 | Keep authoritative occurrence time, Analytics ingestion time and source correction time distinct. | Prevents arrival-time metrics from falsifying business chronology. |
| PRG-REF-297 | Define late-evidence/restatement horizons where a metric materially needs them. | Avoids indefinite mutable reporting or arbitrary ingestion cutoffs. |
| PRG-REF-298 | Preserve restatement lineage separately from metric-definition change. | A corrected source result is not a retroactively changed metric contract. |
| PRG-REF-299 | Make missing-data treatment explicit rather than defaulting to pass/fail/exclusion. | Keeps unknown distinct from negative. |
| PRG-REF-300 | Report counts with percentages for small Programme cohorts. | Maintains current Product metric integrity. |
| PRG-REF-301 | Apply timezone/day-boundary rules only to metrics where they materially affect meaning. | Avoids symmetry-driven complexity. |
| PRG-REF-302 | Use source-owner corrections to drive derived analytical restatement. | Analytics never edits source truth. |
| PRG-REF-303 | Minimise participant-level analytical fields and never copy raw journal/health data for convenience. | Preserves privacy and Domain boundaries. |
| PRG-REF-304 | Keep OQ-019 open at Product authority. | This pass must not invent programme-specific minimum participation/final check-ins/completion thresholds. |
| PRG-REF-305 | Do not treat ANL-GAP-003 as a substitute for Programme OQ-019. | FP-006 paid-pilot metric JIT and Programme completion policy are separate authority seams. |
| PRG-REF-306 | Derived progress percentages must remain projections, never write-side lifecycle inputs. | Prevents circular analytics authority. |
| PRG-REF-307 | Analytics outages degrade measurement/freshness, not Programme truth. | Supports resilient owner-first operation. |
| PRG-REF-308 | Treat dashboards/aggregates as rebuildable from durable owner facts plus frozen metric definitions. | Avoids hidden durable authority in BI/projection stores. |
| PRG-REF-309 | Do not add analytical infrastructure before measured need. | Preserves PostgreSQL-first/YAGNI doctrine. |
| PRG-REF-310 | Carry Pass-21 rules into the FP-014 second lens without assuming Nuwe Jy thresholds generalise. | Prepares the next isolated pass. |

---

# 176. Pass-21 anti-analytics-authority / YAGNI outcome

Rejected / deferred:

- Programme-owned analytics warehouse as business authority;
- Nuwe Jy-specific completion analytics database;
- generic KPI/score engine that writes Programme state;
- global event stream solely for Programme metrics;
- Kafka solely for Programme measurement;
- ClickHouse/warehouse before measured PostgreSQL need;
- Redis as authoritative metric store;
- deduplicating repeat Enrolments into one hidden attempt;
- retroactive cohort-definition editor;
- automatic denominator cleaner that removes missing/failing members;
- current-rule recomputation of historical Programme cohorts;
- automatic metric-threshold inheritance from Nuwe Jy to all Programmes;
- raw journal/health replication into Analytics for segmentation;
- every-message-open as Programme engagement;
- provider-attendance telemetry as attendance truth;
- analytics-driven mark-complete action;
- Analytics outage as Programme fail-closed lifecycle gate;
- one universal timezone/window policy for all Programme metrics;
- Research/survey activation hidden inside Programme analytics;
- new Programme Analytics / Measurement Domain;

The simplest correct model remains:

`PostgreSQL owner truth -> governed/versioned metric derivation -> rebuildable Analytics projection`

with no circular write-back to Programme lifecycle truth.

---

# 177. Pass-21 disposition

**Discovery outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Passes 1–20 remain accepted/working-locked and Pass 21 does not reopen them.
2. The corrected Analytics & Measurement unified handoff is supporting lower-level evidence and should be reused rather than duplicating generic Analytics discovery.
3. Programmes remains authoritative for Edition/Cohort/Enrolment/progression/completion truth; Analytics owns only derived analytical facts/projections/aggregates/dashboards.
4. A Programme metric spanning several source Domains does not create shared-write ownership or a new Programme Analytics Domain.
5. Individual Programme lifecycle state and aggregate measurement are independent truths; a percentage/dashboard can never mark an individual complete, failed, abandoned or exempt.
6. OQ-019 remains PRODUCT REVIEW and this pass does not choose programme-specific minimum participation, final check-ins or completion thresholds.
7. ANL-GAP-003 remains an FP-006 metric-contract/JIT seam and is not authority to resolve OQ-019 or Nuwe Jy completion policy.
8. Governed Programme metric definitions must be prospective and versioned; prior observed cohorts are never redefined merely to pass a target.
9. Where a governed metric is used, denominator membership comes from authoritative source truth under the frozen definition, not from Analytics convenience.
10. Small Programme cohorts report count and percentage; denominator shopping and post-hoc exclusion are rejected.
11. Missing/incomplete analytical data remains distinct from negative business truth unless the governing metric explicitly defines treatment.
12. Authoritative business occurrence, analytical ingestion and source correction/supersession times remain distinct.
13. Late-arriving analytical evidence is governed by the frozen occurrence/window/late-evidence policy rather than ingestion time alone.
14. Source-owner correction may cause governed analytical restatement under the same metric definition; restatement lineage must not be confused with a definition change.
15. ProgrammeVersion is material analytical provenance for Programme attempts and comparisons.
16. Edition/Cohort/schedule context is retained/segmented where it materially affects opportunity, window or interpretation.
17. Repeat Enrolments remain distinct attempts unless a metric is explicitly and prospectively defined at person level.
18. Cross-version or cross-Edition aggregation requires explicit comparability/segmentation; silent pooling is rejected.
19. Timezone/day-boundary rules are applied only where they materially determine the metric, not universally for symmetry.
20. HJP, Events, Communications, Safety, Entitlements and other Domains retain their source truth; Analytics consumes approved/minimised facts and cannot promote observations into Programme authority.
21. Derived Programme progress percentages are permissible as labelled projections but cannot write completion or other lifecycle state.
22. Analytics failure may degrade freshness/measurement but cannot block unrelated Programme release/progression/completion or fabricate evidence.
23. Dashboards, caches and aggregates remain rebuildable and may not become shadow Programme history.
24. Lawful privacy deletion/anonymisation/restriction may constrain later measurement/recomputation; Analytics must not resurrect deleted private source data.
25. Research/survey measurement remains separately subject to its current Roadmap activation seam; Pass 21 does not silently activate it for Programmes.
26. Existing PRG-GAP-002/003/007/011 boundaries remain unchanged and no new Programme gap is created by analytics semantics.
27. No new Product, Architecture, Domain, PRG-GAP or PRG-UPD is justified by Pass 21.
28. No analytics warehouse, Kafka/ClickHouse/Redis authority, generic KPI engine or Nuwe Jy-specific measurement subsystem is justified.
29. Exact event schemas, query models, materialized views, BI/report tooling, indexes, retention mechanics and dashboard implementation remain JIT/proof decisions.
30. Broad discovery remains unfrozen; FP-014 Foundation Programme second-lens pressure testing is the next isolated pass.

**Pass hard stop:** Pass 22 — FP-014 Foundation Programme second-lens pressure test — has not started.

**Broad discovery remains unfrozen.**
