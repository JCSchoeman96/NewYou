# NewYou Analytics & Measurement Pre-JIT Contract — Working v0.1.1

```text
FINAL COMPACT WORKING PACK / NON-AUTHORITATIVE
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
AUTHORITY: NONE
NOT PRODUCT LAW
NOT ARCHITECTURE LAW
NOT DOMAIN LAW
NOT FP-006 7C
```

- **Pack version:** `v0.1.1`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Canonical deep source:** `deep/NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_UNIFIED_HANDOFF_WORKING_v0.1.2.md`
- **Closure:** `HANDOFF-READY / STOP AT JIT BOUNDARY`
- **Default continuation:** `NO DEFAULT PASS 15`

This is the primary normal-context Analytics & Measurement Pre-JIT artifact. Live governed NewYou authority always wins. It compresses the corrected deep handoff; it does not create new semantics, start FP-006 Phase 7, classify dossiers, select proof, or authorise implementation.

**v0.1.1 semantic-fidelity patch:** restores deep-source detail that v0.1.0 compressed too aggressively: exact durable-truth ownership terms, the explicit price-value question, conditional-dossier adjudication before 7C, proof-execution obligations, and the hardening boundary. Deep v0.1.2 is routing/provenance-only over v0.1.1; substantive corrected semantics are unchanged.

---

## 1. Core doctrine

1. Every durable business truth has exactly one authoritative Domain owner.
2. Analytics owns only permitted **derived analytical representation**: governed analytical facts, projections, aggregates and dashboards.
3. A cross-domain metric does not create shared-write authority or a new metric-owner Domain.
4. Provider callback/state, UI state, caches, PubSub, dashboards and analytical ingestion/arrival are not substitutes for authoritative business truth.
5. Source correction remains source-owned. Analytics may restate derived output under a governed restatement policy; it may not rewrite source truth.
6. A Feature Pack may specify how source truths combine without taking ownership of those truths.
7. An unresolved source truth must fail closed where the governing contract requires it; Analytics may not infer a convenient value.
8. Authority ≠ acceleration: projections/caches may improve delivery but never silently become business authority.

---

## 2. Source ownership

| Durable truth used by measurement | Authoritative owner | Analytics boundary |
|---|---|---|
| Assessment methodology/version; attempt/answers/raw scores/result; selected current temperament profile | **Temperament** | derive approved analytical facts only |
| Health/lifestyle facts and provenance | **Health Records** | derive approved/minimised analytical facts |
| Eligibility/safety outcome; safety restriction/override | **Safety & Eligibility** | observe/derive; never decide eligibility |
| Plan generation request/outcome/version/provenance; immutable delivered plan snapshot; review/adjustment outcome | **Plans & Nutrition** | derive product/operational measures; never own plan lifecycle |
| Habit definition/schedule/occurrence; behavioural/progress/adherence entry; private journal/reflection | **Habits, Journals & Progress** | derive approved behavioural measures |
| Product/offer/price; purchase/payment/refund/dispute truth | **Commerce** | derive commercial/operational measures |
| Entitlement identity/scope/source/provenance/validity/expiry/revocation; access grant/consumption | **Entitlements** | derive fulfilment/access measures |
| Research campaign/instrument/version and governed participant Research/feedback response | **Research & Feedback** | derive response rates/distributions only when lawfully activated |
| Analytical fact/projection/aggregate/dashboard | **Analytics** | owner of derived/rebuildable analytical representation only |

No source-domain dossier automatically owns a whole cross-domain Product metric merely because its facts are inputs.

---

## 3. Correct metric classification

### Product gate metrics

| ID | Metric | Target |
|---|---|---:|
| `ANL-METRIC-001` | Assessment completion | ≥80% |
| `ANL-METRIC-002` | Health-onboarding completion | ≥80% |
| `ANL-METRIC-003` | Plan activation | ≥70% |
| `ANL-METRIC-004` | Meaningful seven-day use | ≥60% |

Before first paid participation, every **gate metric** must carry the complete prospective contract required by current Product Law.

### Operational targets

| ID | Metric | Aim |
|---|---|---:|
| `ANL-METRIC-005` | Successful plan generation | ≥95% |
| `ANL-METRIC-006` | Verified entitlement fulfilment | ≥95% |

`ANL-METRIC-005` and `ANL-METRIC-006` are **not automatically Product paid-entry gate metrics merely because they have percentage aims**. Preserve their operational measurement and lifecycle analysis, but do not re-promote them without future lawful authority.

Zero-tolerance integrity criteria are separate from these percentage targets.

---

## 4. `ANL-METRIC-001` — Assessment completion

**Classification:** Product gate metric.
**Target:** ≥80%.
**Owner:** Temperament.

Already governed:

- starter = first answer persisted/submitted;
- completed = valid assessment submission + governed result successfully produced;
- rate = completed / starters;
- count + percentage reporting;
- no denominator shopping;
- prospective metric-definition/version requirement.

Still reserved for the lawful FP-006 contract where applicable:

- cohort/effective point;
- exact cutoff/window;
- exclusions not already fixed;
- missing-data treatment;
- authoritative occurrence timestamp(s);
- source correction/finality/restatement where material;
- metric-definition version.

**Fail closed:** if the required gate contract is incomplete at the paid-participation boundary, do not fabricate a percentage or pass/fail.

---

## 5. `ANL-METRIC-002` — Health-onboarding completion

**Classification:** Product gate metric.
**Target:** ≥80%.

Already governed:

- denominator = paid participants entitled to a personalised-plan pathway who reach the point where required onboarding is available;
- numerator = participants who provide sufficient required information for a deterministic eligibility outcome;
- assessment-only customers are excluded.

Authoritative sources:

- Commerce / Entitlements — lawful paid/access context;
- Health Records — health/lifestyle facts;
- Safety & Eligibility — deterministic eligibility outcome.

Still reserved:

- precise cohort/effective point;
- timeout/cutoff or recovery treatment;
- correction timing;
- exclusions/missing-data handling not already fixed;
- authoritative timestamps;
- metric-definition version.

Analytics may not define “sufficient information” or manufacture eligibility.

---

## 6. `ANL-METRIC-003` — Plan activation

**Classification:** Product gate metric.
**Target:** ≥70%.

Already governed:

- denominator = successfully delivered personalised plans;
- activation requires a genuine post-delivery participant action;
- generation or notification alone does not count;
- a bare single plan open is not sufficient where the governed action requires beginning/confirming the first planned action/day;
- correctly routed `general_wellness_only` is not a failed personalised-plan activation.

Authoritative sources:

- Plans & Nutrition — delivered-plan lifecycle/provenance;
- Habits, Journals & Progress — applicable participant action/progress truth.

FP-006 JIT must resolve/freeze:

- exhaustive qualifying action set;
- activation window;
- authoritative timestamp(s);
- replacement/superseded-plan treatment;
- duplicate/retry handling where material;
- late-evidence horizon;
- correction/finality/restatement.

Do not resolve those questions during Pre-JIT compression.

---

## 7. `ANL-METRIC-004` — Meaningful seven-day use

**Classification:** Product gate metric.
**Target:** ≥60%.

Already governed:

- engagement on at least three distinct days in the first seven;
- at least one engagement after Day 1;
- a single plan open is not meaningful use.

Authoritative sources:

- Habits, Journals & Progress — durable behavioural/progress/adherence truth;
- Plans & Nutrition — applicable delivered-plan anchor;
- any additional denominator owner only if lawful FP-006 scope requires that truth.

FP-006 JIT must resolve/freeze:

- denominator population;
- exhaustive qualifying engagement set;
- Day-1 anchor;
- timezone/day-boundary rule;
- authoritative occurrence timestamps;
- duplicate/reordered evidence treatment where material;
- late-evidence horizon;
- correction/finality/restatement.

Timezone/day-boundary machinery is materially relevant here; do not impose identical lifecycle machinery on unrelated metrics merely for symmetry.

---

## 8. `ANL-METRIC-005` — Successful plan generation

**Classification:** Operational target.
**Aim:** ≥95%.
**Primary owner:** Plans & Nutrition for generation request/outcome/version/provenance.

Useful operational questions, without converting the measure into a Product gate:

- denominator/business-obligation unit;
- `general_wellness_only` treatment;
- retries/duplicate generation attempts;
- recovery/retry horizon;
- terminal versus recoverable failure;
- exclusions;
- authoritative occurrence timestamps;
- correction/finality/restatement where material.

If FP-006 uses this rate for a governed operational decision, define it sufficiently to be reproducible and non-gameable. A missing gate-style contract for this operational rate does **not by itself** create a Product-Law first-paid NO-GO.

The separate zero-tolerance rule for unreproducible delivered plans remains intact.

---

## 9. `ANL-METRIC-006` — Verified entitlement fulfilment

**Classification:** Operational target.
**Aim:** ≥95%.

Authoritative sources:

- Commerce — purchase/payment/refund/dispute/commercial truth;
- Entitlements — grant/right/current access/consumption/revocation truth.

Useful operational questions:

- business-obligation denominator;
- fulfilment/recovery window;
- refunds/reversals/disputes;
- retry/duplicate/convergence deduplication;
- revocation/terminal closeout;
- correlation and authoritative timestamps;
- late evidence;
- correction/finality/restatement.

Payment success is not entitlement success. Provider state is evidence, not authority. Duplicate-entitlement zero tolerance is independent of the ≥95% operational percentage.

Do not make a missing gate-style contract for this operational rate an automatic Product-Law first-paid NO-GO unless future current authority explicitly does so.

---

## 10. Shared metric doctrine

### 10.1 Prospective contracts

Gate metric definitions/versions are fixed prospectively at the point required by authority. They may evolve for future cohorts; they may not be rewritten after outcomes are observed to make a prior cohort pass.

### 10.2 Membership and denominator integrity

A denominator member belongs because governing source truth and the frozen metric definition say so.

Analytics must not:

- choose denominator members opportunistically;
- remove inconvenient failures;
- discard incomplete analytical data to improve a rate;
- infer eligibility/entitlement from UI/provider state.

### 10.3 Small cohorts

Always report count + percentage, for example:

```text
8 / 10 (80%)
```

### 10.4 Missing data

Missing/incomplete analytical data is not automatically:

- success;
- failure;
- 0%;
- permission to delete a denominator member.

Distinguish unknown/unavailable source truth from a negative source truth.

### 10.5 Time and correction

Keep distinct:

1. authoritative business occurrence;
2. analytical arrival/ingestion;
3. source-domain correction/supersession.

Late analytical arrival is not necessarily late business occurrence. A governed source correction may restate a derived historical result under the same frozen metric definition, subject to the approved restatement policy.

### 10.6 Lifecycle machinery only where material

Apply retry, recovery, replacement, reversal, timezone, dedupe and restatement rules where the metric's real lifecycle requires them—not for formal symmetry.

---

## 11. Zero-tolerance integrity criteria

Keep the current integrity criteria distinct from percentage metrics:

- 0 critical platform-caused safety failures;
- 0 duplicate charges;
- 0 duplicate entitlements;
- 0 unreproducible delivered plans;
- 0 unauthorised sensitive-data exposures.

Do not collapse those rules into `ANL-METRIC-005` or `ANL-METRIC-006`.

---

## 12. Research / survey boundary

Current Product Law requires controlled-pilot value evidence including:

- ≥70% positive value/relevance among respondents;
- ≥70% survey response for the controlled-pilot interpretation;
- visible non-response;
- counts + percentages;
- separate price-value question/evidence: “Considering what you paid, did the product provide good value?”;
- discounted-purchase intent treated as weaker than actual purchase.

Where the measurement is a governed Research/Feedback instrument:

- Research & Feedback owns campaign/instrument/version and participant response lifecycle;
- Analytics derives permitted response rates/distributions;
- Research responses do not mutate Health, Safety, Plans, Temperament, Commerce or Entitlements.

Current Roadmap `05_ROADMAP_v1.2.0.md` still leaves Research & Feedback:

```text
FUTURE-GATED / FEATURE-PACK-UNASSIGNED
```

Analytics Pre-JIT cannot activate Research. The prior v1.3.0 candidate is non-current evidence only.

`ANL-GAP-001` therefore remains `UPSTREAM_ACTION_REQUIRED`. See the Delta Register.

---

## 13. FP-006 Phase 7 handoff

Correct process:

```text
7A — Feature Pack Skeleton + Gate Manifest
→ 7B — required JIT Domain Dossiers
→ ordinary drafting / reconciliation
→ 7C — Final Feature Pack Contract
→ proof execution / result
→ implementation + hardening
→ release readiness
```

There is **no fourth “pre-7C” stage**.

### 13.1 7A

7A routes actual FP-006 scope, affected Domains, real gate obligations, unresolved questions and required/conditional/not-required dossiers.

It must not assume:

- every source Domain needs a dossier;
- Analytics needs a dossier because output is analytical;
- 005/006 are Product gates;
- an anticipated Roadmap proof direction is final proof classification.

### 13.2 7B

A required dossier may decide legitimate Domain-owned semantics: states, transitions, guards, invariants, authoritative timestamps, correction/replacement/reversal and retry/idempotency/reconciliation effects on that Domain's truth.

It may not claim authority for cross-domain Product meaning it does not own.

Do not manufacture a dossier where current Domain Law already answers the question.

If a conditional dossier could materially change a final 7C decision, it must be explicitly adjudicated before 7C is approved.

### 13.3 Reconciliation

Before finalising 7C, reconcile source-Domain answers and the cross-domain Product metric contract. This is ordinary drafting, not a new artifact/stage.

### 13.4 7C

For each Product gate metric in scope, freeze the complete required contract: numerator, denominator, qualifying condition/event, window, exclusions, missing-data treatment, cohort, version, material temporal/correction/replacement/restatement semantics, source references, prospective effective point and fail-closed behavior.

For 005/006 define operational measurement only to the depth lawful FP-006 scope needs; do not silently promote them to Product gates.

**7C owns the final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` classification.**

The Analytics Pre-JIT stream does **not** select that classification.

### 13.5 Proof execution / result

After approved 7C, proof executes the route selected by 7C and must not redesign metric semantics. The proof must, where material to the selected route:

- prove authoritative correlation and failure behaviour;
- prove Analytics does not become shadow business authority;
- prove relevant concurrency, retry and idempotency boundaries;
- preserve metric-definition, cohort and source-version provenance;
- demonstrate fail-closed behaviour where the frozen contract requires it.

Proof execution cannot choose a missing denominator, rewrite a window or redefine a qualifying action. If proof exposes a genuine contradiction with higher authority, stop at the owning upstream authority level.

### 13.6 Implementation and hardening

Implementation may choose representation details—events, schema shape, projections, workers, indexes, storage/query/dashboard representation and dedupe mechanism—only where those choices preserve the approved contract.

Hardening may strengthen recovery, reconciliation, observability, resilience and performance without changing business meaning.

### 13.7 Release readiness

Release readiness verifies observed evidence against the frozen prospective contract; it cannot move definitions after outcomes are visible.

---

## 14. Semantic closure distinction

```text
SEMANTIC COMPLETENESS
!= ARTIFACT / REPOSITORY CERTIFICATION
!= ARCHITECTURAL PROOF
!= ANALYTICAL OUTPUT
```

- Semantic completeness: required business meaning is prospectively resolved under lawful authority.
- Artifact/repository certification: exact bytes/path/version/commit and required verification evidence.
- Architectural proof: whether selected architecture can preserve the contract/invariants under the required envelope.
- Analytical output: derived result produced from authoritative source facts under the frozen contract.

A passing test/dashboard cannot compensate for unresolved semantics.

---

## 15. Corrected gap state

This contract does not duplicate the full register; see `NEWYOU_ANALYTICS_MEASUREMENT_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.1.md`.

- `ANL-GAP-001` — `UPSTREAM_ACTION_REQUIRED` — Roadmap/Research activation seam.
- `ANL-GAP-002` — `SUPERSEDED / RECLASSIFIED` — ordinary Roadmap-promotion collateral/integrity maintenance; not an active independent Analytics semantic gap.
- `ANL-GAP-003` — `OPEN / FP-006 JIT REQUIRED` — remaining lawful metric-contract/JIT work.

No new gap is created by this compact pack.

---

## 16. Stop state and resume

```text
CORE ANALYTICS & MEASUREMENT PRE-JIT
HANDOFF-READY / STOP AT JIT BOUNDARY

NO DEFAULT PASS 15
```

This does not mean:

- FP-006 is ready;
- first paid participation is authorised;
- all metric contracts are complete;
- Research is activated;
- 7A exists;
- dossiers are classified;
- 7C exists;
- proof has run;
- implementation is authorised;
- release is ready.

Resume only for:

1. material current authority change;
2. `ANL-GAP-001` state change;
3. lawful FP-006 7A/JIT exposing a new contradiction;
4. required dossier contradiction;
5. 7C unable to reconcile source authority without upstream amendment;
6. proof exposing a genuine upstream semantic contradiction;
7. explicit human reopening with new evidence/scope.

On re-entry, reread live README/manifest/current authority and reopen only affected conclusions.

---

## 17. Closure

**PASS — PARK BROAD ANALYTICS & MEASUREMENT PRE-JIT DISCOVERY.**

The compact contract preserves the corrected deep handoff. Legitimate future routes are only the routed upstream/JIT work recorded in the Delta Register. Implementation remains NOT AUTHORISED.
