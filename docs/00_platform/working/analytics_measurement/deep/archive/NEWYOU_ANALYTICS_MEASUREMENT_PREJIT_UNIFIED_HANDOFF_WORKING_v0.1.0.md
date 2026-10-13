# NewYou Analytics & Measurement Pre-JIT — Unified Corrected Handoff Working v0.1.0

```text
WORKING / NON-AUTHORITATIVE
CORRECTED UNIFIED PRE-JIT HANDOFF
IMPLEMENTATION NOT AUTHORISED
NO DEFAULT PASS 15
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Verified live-main baseline before correction:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Verified pre-correction Analytics branch head:** `aa9ac8dd817cec855d80dc9abec7de6d56b5d8c2`
- **Purpose:** provide one self-contained, corrected Pre-JIT handoff for future FP-006 planning and retire the multi-pass sequence as required operational reading.
- **Authority status:** this document is working evidence only. It does not amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, any Feature Pack contract or implementation authority.
- **Supersession rule:** Passes 1–14, cumulative ledgers and Roadmap-promotion collateral remain historical provenance. For Analytics Pre-JIT operational handoff, this document supersedes their cumulative conclusions wherever they conflict with the corrections explicitly recorded here.

---

# 1. Executive disposition

The independent review identified two material authority errors and two material handoff defects in the accepted Pre-JIT sequence. Each was independently rechecked against the live repository.

The corrected result is:

```text
CORE ANALYTICS & MEASUREMENT PRE-JIT
=> HANDOFF-READY / STOP AT JIT BOUNDARY

RESEARCH / SURVEY ACTIVATION
=> UPSTREAM ROADMAP ACTION REQUIRED

ROADMAP v1.3.0 CANDIDATE
=> NON-CURRENT EVIDENCE ONLY

ANL-GAP-002
=> RETIRED AS A SEPARATE GOVERNANCE GAP
=> UNDERLYING WORK RECLASSIFIED AS ORDINARY ROADMAP-PROMOTION COLLATERAL

ANL-GAP-003
=> OPEN / FP-006 JIT REQUIRED

FP-006 PHASE 7
=> NOT CREATED BY THIS PRE-JIT STREAM

IMPLEMENTATION
=> NOT AUTHORISED
```

No further generic Analytics discovery or pressure-test pass is justified. The next legitimate work is either:

1. lawful upstream Roadmap work for the Research/survey activation seam; or
2. lawful FP-006 Phase 7 work for the core paid-pilot measurement contract.

This handoff does **not** mean the paid pilot is ready, Phase 7 has started, all metric contracts are frozen, proof has been executed, or implementation is authorised.

---

# 2. Current authority baseline

The live authority route verified at `main` commit `086ade7b28c000de1c387acb9760e5eb08bb0413` is:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` where applicable.

`docs/00_platform/README.md` and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` are routing/inventory pointers. They make working artifacts non-authoritative.

## 2.1 Material current authority used by this handoff

### Product Law / North Star

Current authority establishes:

- before first paid participation, every **gate metric** must define numerator, denominator, qualifying event, measurement window, exclusions, missing-data treatment, cohort and metric-definition version;
- metric definitions may change prospectively but may not be rewritten retroactively to make an observed cohort pass;
- small cohorts report both count and percentage;
- denominator shopping is prohibited;
- assessment completion, health onboarding, plan activation and meaningful seven-day use have explicit Product-Law definitions;
- the controlled-pilot value/relevance interpretation retains a 70% positive target and requires at least 70% survey response, with non-response visible;
- critical platform-caused safety failures, duplicate charges, duplicate entitlements, unreproducible delivered plans and unauthorised sensitive-data exposures have zero-tolerance integrity criteria;
- successful plan generation and verified entitlement fulfilment are separate **operational targets** with an aim of at least 95%.

The distinction between Product targets and operational targets is material and is preserved below.

### Decision Register

`DEC-310` requires the complete prospective contract for every paid-cohort **gate metric** and directs the paid cohort to the approved assessment-completion, health-onboarding, plan-activation and meaningful-seven-day-use definitions, plus the value/relevance survey treatment.

### Domain Law

Current `04_DOMAIN_MAP_v1.2.0.md` preserves one owner per durable truth. Analytics owns analytical facts/projections/aggregates as permitted, derived from authoritative sources; analytical projections/aggregates/dashboards are rebuildable.

### Roadmap

Current Roadmap is `05_ROADMAP_v1.2.0.md`.

It provides the canonical Phase 7 direction and explicitly states that anticipated proof labels are provisional and that the **Phase 7 Final Feature Pack Contract owns the final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` decision**.

The current Roadmap also leaves Research & Feedback `FUTURE-GATED / FEATURE-PACK-UNASSIGNED`; it is not automatically activated by FP-006.

---

# 3. Corrections applied after independent review

The following statements explicitly supersede incompatible conclusions in Passes 1–14 and ledger v0.8.0.

## 3.1 Correction A — `ANL-METRIC-005` and `ANL-METRIC-006` are operational targets, not automatic paid-entry gate metrics

Earlier Pre-JIT passes treated all six core metrics as if each required the same pre-paid gate-contract/fail-closed status.

That was too strong.

Current Product Law distinguishes:

### Product gate targets

- `ANL-METRIC-001` — assessment completion, target ≥80%
- `ANL-METRIC-002` — health-onboarding completion, target ≥80%
- `ANL-METRIC-003` — plan activation, target ≥70%
- `ANL-METRIC-004` — meaningful seven-day use, target ≥60%

### Operational targets

- `ANL-METRIC-005` — successful plan generation, aim ≥95%
- `ANL-METRIC-006` — verified entitlement fulfilment, aim ≥95%

Therefore:

- metrics 005/006 remain important operational measurement;
- their source ownership and lifecycle analysis remain valid;
- FP-006 may need precise operational definitions to measure and act on them;
- they are **not automatically subject to the Product-Law rule that every gate metric must have a complete contract before first paid participation** merely because the percentages exist;
- absence of a fully frozen “gate metric contract” for 005/006 does not by itself create a Product-Law paid-entry NO-GO;
- a future lawful FP-006 Final Feature Pack Contract may impose stronger requirements only where then-current authority permits or requires them.

Zero-tolerance integrity rules remain separate. For example, duplicate entitlements remain prohibited even though verified-entitlement-fulfilment percentage is an operational target.

## 3.2 Correction B — final proof classification belongs in Phase 7C

Earlier Pass 13/14 wording placed final architectural-proof classification downstream of approved 7C.

That contradicts current Roadmap law.

The corrected sequence is:

```text
7A — FEATURE PACK SKELETON + GATE MANIFEST
        |
        v
7B — REQUIRED JIT DOMAIN DOSSIERS
        |
        v
ORDINARY DRAFTING / RECONCILIATION
(no new artifact type or stage)
        |
        v
7C — FINAL FEATURE PACK CONTRACT
     - complete cross-domain contract
     - final REUSE_EXISTING_PROOF / NEW_TRACER_BULLET classification
        |
        v
PROOF EXECUTION / RESULT
        |
        v
IMPLEMENTATION + HARDENING
        |
        v
RELEASE READINESS
```

Proof execution may expose an upstream contradiction. It may not silently redesign the frozen contract.

## 3.3 Correction C — `ANL-GAP-002` is retired as a separate governance gap

The earlier stream correctly found version-pinned routing/tests and other promotion collateral that would need updating for a lawful Roadmap successor.

It incorrectly elevated that ordinary successor work into a new “authority-promotion integrity/tooling lifecycle gap”.

Current repository governance already defines the promotion/integrity mechanism through the authority route, manifest, Foundation Integrity tooling/tests and exact-commit evidence.

Corrected status:

```text
ANL-GAP-002:
SUPERSEDED AS A DISTINCT GOVERNANCE GAP

UNDERLYING WORK:
ROADMAP-PROMOTION COLLATERAL / INTEGRITY MAINTENANCE
```

That collateral can block promotion of a Roadmap successor. It does **not** block core FP-006 non-survey JIT merely by existing.

No replacement gap identifier is created.

## 3.4 Correction D — the Analytics branch authority route must remain internally valid

The pre-correction Analytics branch had:

- README/manifest routing current Roadmap to root `05_ROADMAP_v1.2.0.md`;
- the root v1.2.0 file removed;
- the unpromoted v1.3.0 candidate placed at the current Roadmap root;
- the v1.2.0 current file placed in `archive/`.

That branch shape was internally inconsistent and unsafe for integration.

The correction restores current `05_ROADMAP_v1.2.0.md` at its canonical root and removes the unpromoted v1.3.0 candidate from the canonical current-authority path. The v1.3.0 candidate remains recoverable as historical candidate evidence by exact commit/blob.

## 3.5 Correction E — semantic closure and repository certification are separate

A metric is semantically complete when its required meaning has been prospectively resolved under the correct authority and source-Domain constraints.

Repository path/version/commit evidence proves which bytes were accepted and is essential for certification/traceability. It is not itself part of the business meaning of a metric.

Use this distinction:

```text
SEMANTIC COMPLETENESS
!= REPOSITORY / ARTIFACT CERTIFICATION
!= ARCHITECTURAL PROOF RESULT
!= ANALYTICAL OUTPUT
```

## 3.6 Correction F — no fourth “pre-7C” stage

Any reconciliation of dossier answers and cross-domain metric wording before finalising 7C is ordinary drafting within the existing Phase 7 process.

It does not create:

- a new governed artifact;
- a new gate class;
- a fourth Phase 7 stage; or
- a new authority layer.

---

# 4. Source-truth ownership map

The following is the minimum source map future FP-006 planning may rely on, subject to fresh authority recheck.

| Durable truth | Authoritative owner | Analytics relationship |
|---|---|---|
| Assessment methodology/version; attempt/answers/raw scores/result; selected current temperament profile | **Temperament** | read/derive approved analytical facts only |
| Health/lifestyle facts and provenance | **Health Records** | derive only approved/minimised analytical facts |
| Eligibility/safety outcome, safety restriction/override | **Safety & Eligibility** | read/derive; never decide eligibility |
| Plan generation/version/provenance; generation outcome; plan review/adjustment outcome; immutable delivered plan snapshot | **Plans & Nutrition** | derive operational/product measures; never become plan authority |
| Habit definition/schedule/occurrence; behavioural/progress/adherence entry; private journal/reflection | **Habits, Journals & Progress** | derive approved behavioural measures |
| Product/offer/price; purchase/payment/refund/dispute truth | **Commerce** | derive commercial/operational measures |
| Entitlement identity/scope/source/provenance/validity/expiry/revocation; access grant/consumption | **Entitlements** | derive access/fulfilment measures |
| Research campaign/instrument/version and participant Research/feedback response | **Research & Feedback** | derive response rates/distributions when capability is lawfully activated |
| Governed analytical event/fact; analytical projection/aggregate/dashboard | **Analytics** | owner of the derived analytical representation only |

## 4.1 Non-negotiable ownership rules

1. A metric spanning several Domains does not create a new shared-write Domain.
2. No single source Domain automatically owns the whole cross-domain Product metric.
3. A Feature Pack contract may specify how authoritative facts combine without taking ownership of those facts.
4. Analytics ingestion time is not a substitute for the authoritative business occurrence time.
5. A provider callback, cache, projection, dashboard, UI state or PubSub message never becomes durable business authority merely because it is convenient to measure.
6. Source corrections remain source-owned; Analytics may restate a derived result under a governed restatement policy without rewriting the source.
7. An unresolved source truth must fail closed where the governing Product/Feature-Pack contract requires it; Analytics may not infer a convenient answer.

---

# 5. Correct metric classification and handoff

## `ANL-METRIC-001` — Assessment completion

**Classification:** Product gate metric.

**Target:** ≥80%.

**Current governed definition:**

- starter = first answer persisted/submitted;
- completed = valid assessment submission + governed result successfully produced;
- rate = completed / starters.

**Primary source owner:** Temperament.

**Already fixed by authority:**

- starter meaning;
- completion meaning;
- target;
- count + percentage reporting;
- prospective definition/version requirement;
- no denominator shopping.

**Still to be explicit in FP-006 contract as applicable:**

- cohort/effective point;
- exact measurement cutoff/window where needed;
- exclusions not already fixed;
- missing-data treatment;
- authoritative occurrence timestamp(s);
- source correction/finality/restatement rule where material;
- metric-definition version.

**Fail-closed rule:** if the required paid-pilot gate contract remains incomplete at the paid-participation boundary, do not fabricate a percentage or pass/fail.

---

## `ANL-METRIC-002` — Health-onboarding completion

**Classification:** Product gate metric.

**Target:** ≥80%.

**Current governed definition:**

- denominator = paid participants entitled to a personalised-plan pathway who reach the point where required health onboarding is available;
- numerator = participants who provide sufficient required information for a deterministic eligibility outcome;
- assessment-only customers are excluded.

**Source owners:**

- Commerce / Entitlements for lawful paid/access context;
- Health Records for health/lifestyle facts;
- Safety & Eligibility for deterministic eligibility outcome.

**Still to be explicit in FP-006 contract as applicable:**

- precise cohort/effective point;
- timeout/cutoff or recovery treatment;
- source correction timing;
- exclusions/missing-data handling not already fixed;
- authoritative timestamps;
- metric-definition version.

Do not turn Analytics into the owner of “sufficient information” or eligibility.

---

## `ANL-METRIC-003` — Plan activation

**Classification:** Product gate metric.

**Target:** ≥70%.

**Current governed definition:**

- denominator = successfully delivered personalised plans;
- activation requires a genuine post-delivery participant action;
- generation or notification alone does not count;
- a single plan open alone is not sufficient where Product Law requires a meaningful beginning/confirmation action;
- correctly routed `general_wellness_only` is not a failed personalised-plan activation.

**Source owners:**

- Plans & Nutrition for delivered plan and plan lifecycle/provenance;
- Habits, Journals & Progress for applicable participant action/progress truth.

**FP-006 JIT must resolve/freeze:**

- exhaustive qualifying action set;
- activation window;
- authoritative timestamp(s);
- replacement/superseded-plan treatment;
- duplicate/retry handling where material to evidence;
- late evidence horizon;
- correction/finality/restatement treatment.

No source-domain dossier owns the cross-domain metric merely because its facts are required.

---

## `ANL-METRIC-004` — Meaningful seven-day use

**Classification:** Product gate metric.

**Target:** ≥60%.

**Current governed definition:**

- engagement on at least three distinct days in the first seven;
- at least one engagement after Day 1;
- a single plan open is not meaningful use.

**Primary source owners:**

- Habits, Journals & Progress for durable behavioural/progress/adherence facts;
- Plans & Nutrition for the applicable delivered-plan anchor;
- any additional denominator owner only if lawful FP-006 scope actually requires that truth.

**FP-006 JIT must resolve/freeze:**

- denominator population;
- exhaustive qualifying engagement set;
- Day-1 anchor;
- timezone/day-boundary rule;
- authoritative occurrence timestamps;
- duplicate/reordered evidence treatment where material;
- late-evidence horizon;
- correction/finality/restatement treatment.

Timezone/day-boundary machinery is material here; do not force the same machinery into unrelated metrics merely for symmetry.

---

## `ANL-METRIC-005` — Successful plan generation

**Classification:** Operational target, **not an automatic paid-entry gate metric**.

**Operational aim:** ≥95%.

**Primary source owner:** Plans & Nutrition for generation request/outcome/version/provenance.

**Potential supporting owners:** only those required by the operational denominator actually chosen under lawful FP-006 scope.

**Measurement questions that remain useful:**

- denominator/business-obligation unit;
- treatment of `general_wellness_only`;
- retries and duplicate generation attempts;
- recovery/retry horizon;
- terminal versus recoverable failures;
- exclusions;
- authoritative occurrence timestamps;
- correction/finality/restatement where material.

**Correct rule:**

Do not turn the operational percentage into a new Product gate. If FP-006 uses the percentage for a governed proceed/iterate/repeat/pause decision, define it clearly enough to be reproducible and non-gameable. Stronger gate status requires then-current authority, not this Pre-JIT document.

The separate zero-tolerance rule for unreproducible delivered plans remains intact.

---

## `ANL-METRIC-006` — Verified entitlement fulfilment

**Classification:** Operational target, **not an automatic paid-entry gate metric**.

**Operational aim:** ≥95%.

**Source owners:**

- Commerce for purchase/payment/refund/dispute/commercial truth;
- Entitlements for grant/right/current access/consumption/revocation truth.

**Measurement questions that remain useful:**

- business-obligation denominator;
- fulfilment/recovery window;
- refunds/reversals/disputes;
- retry/duplicate/convergence deduplication;
- revocation/terminal closeout;
- correlation/authoritative timestamps;
- late evidence;
- correction/finality/restatement.

**Correct rule:**

Payment success is not entitlement success. Provider state is evidence, not authority. Duplicate-entitlement zero tolerance remains independent of the ≥95% operational percentage.

Do not make a missing “gate metric contract” for this operational rate an automatic Product-Law first-paid NO-GO unless future current authority explicitly makes it one.

---

# 6. Value/relevance and Research/survey measurement

Current Product Law requires, for controlled-pilot interpretation:

- ≥70% positive value/relevance among survey respondents;
- ≥70% survey response;
- visible non-response;
- counts + percentages for small cohorts;
- a separate price-value question;
- discounted-purchase intent treated as weaker than actual purchase.

## 6.1 Ownership

Where the measurement is a governed Research/Feedback instrument:

- Research & Feedback owns campaign/instrument/version and participant response lifecycle;
- Analytics derives response rates/distributions;
- Research responses do not directly mutate Health, Safety, Plans, Temperament, Commerce or Entitlements.

## 6.2 Current Roadmap activation seam

Current `05_ROADMAP_v1.2.0.md` leaves Research & Feedback:

```text
FUTURE-GATED / FEATURE-PACK-UNASSIGNED
```

Therefore the bounded Research/survey activation proposed by the prior Roadmap v1.3.0 candidate is **not current Roadmap authority**.

This is the real remaining upstream seam recorded as `ANL-GAP-001`.

The core non-survey Analytics handoff does not need to wait for a speculative Research design. The governed survey path must not start as Research JIT until lawful Roadmap authority activates it.

---

# 7. Shared metric-contract rules

The following rules apply wherever relevant to the governed metric being measured.

## 7.1 Membership is source-authoritative

A denominator member belongs because the governing source truth says so under the frozen metric definition.

Analytics cannot:

- choose members opportunistically;
- remove inconvenient failures;
- exclude incomplete data merely to improve the rate;
- infer eligibility/entitlement from UI or provider state;
- use analytical arrival as the business occurrence.

## 7.2 Prospective definitions

Freeze the applicable definition/version before the cohort is observed at the point required by authority.

Never:

- move a cutoff after seeing outcomes;
- substitute a different denominator to obtain a preferred result;
- rewrite the definition retroactively to make an earlier cohort pass.

## 7.3 Counts and percentages

For small cohorts report both, for example:

```text
8 / 10 (80%)
```

A percentage without its small-cohort count is insufficient.

## 7.4 Missing data

Missing/incomplete analytical data is not:

- permission to delete a denominator member;
- automatically 0%;
- automatically success;
- automatically failure unless the governing contract explicitly says so.

Distinguish “business truth unknown/unavailable” from “business truth is negative”.

## 7.5 Time distinctions

Keep separate:

1. authoritative business occurrence;
2. analytical arrival/ingestion;
3. source-domain correction or supersession.

Late analytical arrival is not necessarily a late business event.

A source correction may legitimately restate a historical analytical result under the same frozen metric definition, subject to a governed correction/restatement policy.

## 7.6 Lifecycle machinery only where material

Do not apply every mechanism to every metric for formal symmetry.

Examples:

- timezone/day boundary is central to meaningful seven-day use;
- replacement-plan handling is material to activation;
- retry/recovery is material to generation/fulfilment;
- refund/reversal/revocation materially affects entitlement fulfilment;
- assessment completion does not need entitlement-style reversal machinery unless a real authority path makes it relevant.

---

# 8. FP-006 Phase 7 handoff

## 8.1 Phase 7A — Skeleton + Gate Manifest

7A must:

- use current authority, not this working document as law;
- define the actual FP-006 scope being prepared;
- identify affected Domains;
- identify actual Product/Decision/Roadmap gate obligations;
- route unresolved metric questions;
- classify dossiers using the normal required/conditional/not-required mechanism;
- expose any unresolved blocking planning gate.

For core measurement, 7A should at minimum recognise:

- the four Product gate metrics 001–004;
- the value/relevance/survey Product requirement and its current Research activation seam;
- operational measurement for 005/006 where FP-006 needs it;
- source owners and the unresolved questions listed in this handoff.

7A must **not** assume:

- every source Domain requires a JIT dossier;
- Analytics requires a JIT dossier merely because the result is analytical;
- 005/006 are paid-entry gates;
- a provisional Roadmap proof direction is the final proof classification.

## 8.2 Phase 7B — required JIT Domain Dossiers

A required dossier may make legitimate decisions inside its Domain authority.

Examples include:

- authoritative states/transitions;
- guards/invariants;
- authoritative Domain timestamps;
- correction/replacement/reversal semantics;
- retry/idempotency/dedup effect on that Domain's truth;
- recovery/reconciliation rules.

The correction to earlier Pass 13 wording is important:

> A dossier is not prohibited from deciding Domain semantics. It is prohibited only from claiming authority over cross-domain Product meaning it does not own.

If current Domain Law already answers the needed question, do not manufacture a dossier for completeness.

If a conditional dossier could materially change a final 7C decision, it must be explicitly adjudicated before 7C is approved.

## 8.3 Ordinary reconciliation before 7C

Before drafting/finalising 7C, the planner must reconcile the source-Domain answers and Product metric contract.

This is ordinary drafting activity, not a new stage.

For each gate metric, verify:

- all authority-required fields are explicit;
- source-Domain semantics are compatible;
- the definition is prospective;
- unresolved contradictions have been stopped upstream;
- required dossiers/gates are satisfied.

## 8.4 Phase 7C — Final Feature Pack Contract

7C must make the final development-entry contract explicit.

For each Product gate metric in scope, include at minimum:

- numerator;
- denominator;
- qualifying event/condition;
- measurement window;
- exclusions;
- missing-data treatment;
- cohort;
- metric-definition version;
- material timing/correction/replacement/restatement semantics;
- authoritative source references;
- prospective effective point;
- fail-closed behaviour.

For operational measures 005/006, 7C should define the operational measurement only to the depth required by the Feature Pack's accepted scope and decisions. It must not silently promote them to Product gates.

**7C also owns the final architectural-proof classification:**

```text
REUSE_EXISTING_PROOF
or
NEW_TRACER_BULLET
```

Dossier links are evidence; they are not a substitute for an explicit final contract.

## 8.5 Proof execution / result

After approved 7C:

- execute the proof path selected by 7C;
- prove authoritative correlation and failure behaviour;
- prove no Analytics shadow authority;
- prove material concurrency/retry/idempotency boundaries;
- preserve version/cohort provenance;
- fail closed where the frozen contract requires it.

Proof execution cannot choose a missing denominator, rewrite a window or redefine a qualifying action.

If proof reveals a real contradiction with higher authority, stop upstream.

## 8.6 Implementation and hardening

Implementation may legitimately decide representation details that were deliberately left downstream, including where authorised:

- event/message names;
- schema shape;
- indexes;
- workers/jobs;
- projection/query shape;
- storage representation;
- dashboard implementation;
- retry/dedup mechanisms.

Those decisions must implement—not redefine—the approved business contract.

Hardening may strengthen recovery, reconciliation, observability, resilience and performance without changing the business meaning.

## 8.7 Release readiness

Release readiness verifies evidence against the frozen prospective contract.

It may not:

- change denominators;
- move windows/cutoffs;
- remove inconvenient members;
- substitute Analytics ingestion time;
- rewrite observed-cohort semantics.

A failing result triggers the governed release decision; it does not authorise metric surgery.

---

# 9. Semantic closure, certification, proof and output

These are distinct checks.

## 9.1 Semantic completeness

For a Product gate metric, semantic completeness means the required metric meaning is explicit and prospectively frozen under lawful authority.

## 9.2 Artifact/repository certification

Certification answers:

- which exact artifact/path/version was accepted;
- at which repository commit;
- whether required workflows/evidence passed.

This provides provenance, not business meaning.

## 9.3 Architectural proof

Proof answers whether the selected architecture/implementation path can preserve the approved contract and invariants under the relevant failure/concurrency envelope.

## 9.4 Analytical output

Analytical output is the derived result produced from authoritative facts under the frozen metric contract.

A dashboard or passing test cannot compensate for an unresolved semantic contract.

---

# 10. Corrected gap register

## `ANL-GAP-001` — Research/survey Roadmap activation seam

**Status:** `UPSTREAM_ACTION_REQUIRED`.

**Real:** yes.

**Owner/stage:** Roadmap/upstream governance.

**Scope:** bounded Research/Feedback activation needed before the governed survey path can be assigned to FP-006 or another activating Feature Pack.

**Effect:**

- blocks Research/survey JIT under the proposed bounded Research ownership path;
- does not block ordinary core non-survey FP-006 Phase 7 planning.

**Resolution:** lawfully promote, amend, replace or reject the candidate through normal Roadmap governance.

---

## `ANL-GAP-002` — retired as a distinct governance gap

**Status:** `SUPERSEDED / RECLASSIFIED`.

Earlier wording:

```text
authority-promotion integrity/tooling lifecycle gap
```

is superseded.

Underlying facts remain useful:

- successor promotion requires routing/manifest/integrity collateral;
- version-pinned tests/current-route assertions may require lawful update;
- exact-commit Foundation Integrity evidence must match the candidate promotion.

Correct classification:

```text
ROADMAP-PROMOTION COLLATERAL / INTEGRITY MAINTENANCE
```

It may block promotion of the Roadmap candidate. It is not a separate Analytics governance gap and does not block core non-survey FP-006 JIT.

---

## `ANL-GAP-003` — FP-006 metric-contract/JIT completion

**Status:** `OPEN / FP-006 JIT REQUIRED`.

Corrected scope:

1. complete prospective gate contracts for `ANL-METRIC-001..004`;
2. resolve remaining cross-domain semantics for 003/004;
3. define 005/006 operational measurement to the depth FP-006 actually needs, without automatic gate promotion;
4. route/adjudicate required and conditional dossiers;
5. freeze final contracts in 7C;
6. make the final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` choice in 7C;
7. execute proof downstream;
8. preserve all current source ownership.

The Research/survey path remains separately constrained by `ANL-GAP-001`.

No new gap identifier is justified by this correction.

---

# 11. Roadmap v1.3.0 candidate provenance

Current Roadmap authority remains `05_ROADMAP_v1.2.0.md`.

The earlier bounded v1.3.0 Research-activation candidate remains useful **historical candidate evidence**, not current authority:

```text
Original candidate path at candidate commit:
docs/00_platform/05_ROADMAP_v1.3.0.md

Original candidate git blob:
ddff1c2fa34b3b9185bef8eb72e49f8513479887

Original candidate commit:
25cef5c3eb6462292cb5c34fff2e4c59d3be2078

Recorded candidate SHA-256:
bfd0d99818d68ba3826015eed17da76424fb7d3b8148e8f686f7964915b23261
```

Its semantic intent is not silently discarded. It can be evaluated by the future upstream Roadmap workstream for `ANL-GAP-001`.

This corrected Analytics branch must not make that candidate look current merely by placing it in the canonical current Roadmap slot.

---

# 12. What future FP-006 planning may rely on

Future FP-006 planning may treat this document as a concise working handoff for:

- source-Domain ownership;
- current metric classification;
- known unresolved contract questions;
- cross-cutting cohort/time/correction rules;
- Research activation boundary;
- correct Phase 7 placement;
- corrected proof-classification placement;
- explicit non-authority of Analytics.

It must still re-read live GitHub authority.

This handoff does **not** pre-decide:

- actual 7A dossier classification;
- a new Domain;
- final metric details reserved for JIT;
- final proof classification;
- implementation representation;
- release result.

---

# 13. Historical supersession map

Passes 1–14 and ledger versions remain provenance.

They are no longer the required operational reading chain.

The following cumulative conclusions are explicitly superseded:

| Historical conclusion | Corrected conclusion |
|---|---|
| Metrics 003–006 all require paid-entry gate-contract completion | Only 001–004 are established Product gate metrics. 005/006 are operational targets unless future lawful authority strengthens them. |
| Unresolved 005/006 gate contracts automatically block first paid participation | Not supported by current authority. Separate integrity gates remain in force. |
| Final proof classification occurs after 7C | 7C owns final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET`; proof execution/result follows. |
| `ANL-GAP-002` is a distinct governance/tooling lifecycle gap | Retired; underlying work is ordinary Roadmap-promotion collateral/integrity maintenance. |
| “pre-7C synthesis” may be read as a process stage | It is ordinary drafting/reconciliation inside the existing 7A→7B→7C flow. |
| Semantic closure includes artifact SHA/path/commit as part of metric meaning | Semantic completeness and repository certification/provenance are separate checks. |
| Pass-14 handoff conclusion was safe without correction | Superseded by this corrected unified handoff. |

All non-conflicting source-ownership, anti-denominator-shopping, prospective-versioning, late-arrival/correction and no-shadow-authority conclusions are retained.

---

# 14. Stop state and resume triggers

After this corrective supersession is verified:

```text
CORE ANALYTICS & MEASUREMENT PRE-JIT:
HANDOFF-READY / STOP AT JIT BOUNDARY

NO DEFAULT PASS 15
```

## 14.1 Not ready / not authorised

This stop-state does not claim:

- paid-pilot release readiness;
- completed contracts for all Product gate metrics;
- Roadmap v1.3.0 promotion;
- Research/survey activation;
- FP-006 7A creation;
- required dossier classification;
- approved 7C;
- executed architectural proof;
- implementation authorisation.

## 14.2 Resume triggers

Resume Analytics Pre-JIT only if:

1. current Product/Decision/Domain/Roadmap authority materially changes;
2. `ANL-GAP-001` changes state;
3. lawful FP-006 7A/JIT exposes a new contradiction not already routed;
4. a required Domain dossier contradicts an assumption in this handoff;
5. 7C cannot reconcile source authority without an upstream amendment;
6. proof execution exposes a genuine upstream semantic contradiction;
7. human review explicitly reopens a conclusion with new evidence/scope.

The passage of time or a desire for more documentation is not a trigger.

## 14.3 Re-entry protocol

On re-entry:

1. inspect live `main`;
2. read `docs/00_platform/README.md`;
3. read the current authority manifest;
4. identify current authoritative versions;
5. inspect current FP-006 artifacts/branch;
6. compare changed authority with this handoff;
7. reopen only affected conclusions;
8. stop at the authority level that owns any contradiction.

---

# 15. Minimum operational reading set

For future FP-006 planning, the minimum Analytics Pre-JIT reading set is:

1. current live authority required by README/manifest; and
2. this unified corrected handoff.

Historical Passes 1–14, ledgers and Roadmap-collateral files are optional provenance unless a specific reasoning chain must be audited.

The original Roadmap v1.3.0 candidate should be inspected only when working `ANL-GAP-001`.

This deliberately reduces the prior 27-document working chain to one operational handoff.

---

# 16. Final disposition

**PASS — CORRECTIONS APPLIED TO THE ANALYTICS & MEASUREMENT PRE-JIT HANDOFF.**

The corrected core non-survey Pre-JIT analysis is sufficient to stop discovery and hand off to lawful FP-006 Phase 7 when current programme authority permits it.

`ANL-GAP-001` remains an upstream Roadmap action for the Research/survey path.

`ANL-GAP-002` is retired as a distinct governance gap and retained only as ordinary promotion collateral.

`ANL-GAP-003` remains open for FP-006 JIT, narrowed to the corrected metric classifications and correct 7C proof-classification responsibility.

No Product, Architecture, Domain or current Roadmap law is amended by this document.

No implementation is authorised.
