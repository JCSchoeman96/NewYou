# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.12.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 12 ONLY — FP-006 METRIC-CONTRACT CLOSURE EVIDENCE
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-pass branch head:** `2b1a9993582bc1b7e6ed0d56beec01bfc290335e`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.11.0.md` — preserved unchanged.
- **Accepted predecessor result:** Pass 11 accepted by human review.
- **Purpose:** define the minimum reproducible evidence required for the future FP-006 JIT process to mark each unresolved `ANL-METRIC-003..006` metric contract semantically complete before first paid participation.
- **Scope boundary:** this pass does not answer any unresolved metric semantic, create an FP-006 Phase 7 artifact, create or approve a JIT Domain Dossier, create a Final Feature Pack Contract, choose `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`, define events/storage/provider/dashboard implementation, promote Roadmap authority, or authorise implementation.

---

# 1. Authority and accepted working locks carried into Pass 12

Current live authority remains the route headed by:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`;
2. `00_PLATFORM_v1.6.0.md`;
3. `01_DECISIONS_v1.6.0.md`;
4. `02_OPEN_WORK_v1.2.59.md`;
5. `03_ARCHITECTURE_v1.1.1.md`;
6. `04_DOMAIN_MAP_v1.2.0.md`;
7. `05_ROADMAP_v1.2.0.md`;
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`; and
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when applicable.

The README and current authority manifest were rechecked at the live-main baseline above.

Accepted Passes 9–11 working-lock that:

- every paid-pilot gate metric must have a prospectively frozen numerator, denominator, qualifying event/condition, measurement window, exclusions, missing-data treatment, cohort and metric-definition version before first paid participation;
- definitions may change prospectively, never retroactively to make an earlier cohort pass;
- count + percentage reporting and anti-denominator-shopping are already locked;
- source Domains retain durable business truth and lifecycle authority;
- Analytics owns derived analytical facts/projections/aggregates only;
- `ANL-METRIC-003..006` remain semantically incomplete and require FP-006 JIT completion;
- FP-006 JIT freezes the cross-domain metric contract while source Domains retain component truth;
- an unresolved required metric contract at first paid participation is not gate-eligible and makes paid participation `BLOCKED / NO-GO`; and
- `ANL-GAP-003` remains `OPEN / FP-006 JIT REQUIRED`.

Pass 12 does not reopen any accepted semantic answer. It defines only what evidence must exist before future FP-006 governance may legitimately call one of the four contracts complete.

---

# 2. Closure has three separate meanings

Pass 12 rejects collapsing three different things into one “done” state.

## 2.1 Semantic metric-contract closure

A metric is semantically closed only when the future FP-006 JIT / Phase 7 process has explicitly resolved every required metric field and every material extra semantic identified by accepted Passes 9–11.

This is the subject of Pass 12.

## 2.2 Implementation / architectural proof

Implementation proof asks whether the selected architecture and implementation actually enforce the approved contract. Current delivery governance later requires explicit proof classification such as `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`.

Pass 12 does **not** make that classification and does not require implementation proof in order to know what the metric contract means.

## 2.3 Analytical production/reporting evidence

Analytical evidence demonstrates that the approved metric can be derived from authoritative source facts under the frozen contract and reported correctly.

A generated percentage does not retroactively prove the semantic contract was valid.

Therefore:

```text
SEMANTIC CLOSURE
    != IMPLEMENTATION PROOF
    != ANALYTICAL OUTPUT
```

All three eventually matter, but they occur at different authority/proof layers.

---

# 3. Minimum closure-evidence bundle

For `ANL-METRIC-003..006`, future FP-006 governance may treat a metric contract as semantically complete only when the closure evidence contains all of the following.

## 3.1 Explicit decision record

The governing FP-006 JIT / Phase 7 artifact must contain an explicit resolved decision for every previously unanswered metric question.

A vague statement such as “use normal analytics conventions”, “use product events”, “use the source of truth”, “TBD”, or “to be confirmed during implementation” is not closure.

The record must identify:

- the metric;
- the resolved semantic choice for every required field/question;
- the metric-definition version;
- the prospective cohort/effective point to which that version applies; and
- its lifecycle/approval state under the normal Phase 7 process.

This Pre-JIT document cannot itself supply that approval state.

## 3.2 Exact authority basis

The closure record must cite the exact current authority that constrains the decision, including as applicable:

- Product / North Star metric requirement;
- Product Law §21T.7 and the relevant operational/product target;
- DEC-310;
- current Roadmap FP-006 evidence/gate language;
- current Domain Map ownership/lifecycle rules; and
- any other current authority actually required by the chosen semantic.

Generic references such as “per Product Law” are insufficient for closure when a specific section/rule determines the answer.

## 3.3 Source-owner lifecycle evidence

For every authoritative source Domain used by the metric, closure evidence must prove that the chosen metric semantics are consistent with the relevant source lifecycle.

The evidence is deliberately **bounded**. It should identify only what is material to the metric, such as:

- the authoritative business truth being read;
- the relevant lifecycle states/transitions;
- terminal/recovery states where material;
- retry/idempotency/deduplication behaviour where material;
- correction/supersession/reversal semantics where material;
- the authoritative time anchor needed by the metric; and
- invariants that prohibit a proposed interpretation.

It must not copy an entire Domain lifecycle into Analytics or create a second source of authority.

Where the Feature Pack Gate Manifest requires a JIT Domain Dossier, semantic closure cannot bypass that dossier. The approved dossier must carry or validate the source-lifecycle semantics consumed by the final metric contract. Pass 12 does not decide which future FP-006 dossiers the Gate Manifest will require.

## 3.4 Complete metric payload

The accepted closure record must explicitly freeze every Product-Law-required field:

1. numerator;
2. denominator;
3. qualifying event/condition;
4. measurement window;
5. exclusions;
6. missing-data treatment;
7. cohort; and
8. metric-definition version.

It must also freeze every metric-specific semantic that accepted Passes 9–11 identified as material.

If one required field remains implicit, inferred, contradictory or `TBD`, the contract is not complete.

## 3.5 Prospective version/effective-scope pin

The closure evidence must make it possible to answer, unambiguously:

> Which metric definition applied to which cohort, from what prospective effective point?

At minimum it must preserve:

- metric-definition version;
- cohort identity/scope;
- cohort cutoff/effective point;
- the JIT/Phase 7 artifact path and version carrying the decision; and
- the exact repository commit SHA at which that accepted decision is reviewed/frozen.

If a later definition supersedes it prospectively, predecessor/version lineage must remain visible. The earlier cohort must not be silently reinterpreted under the successor.

An additional standalone SHA-256 is not made a new semantic prerequisite by this Pass. The exact repository commit plus path/version pins repository bytes for this closure-evidence purpose unless future governed FP-006 process explicitly requires an additional hash.

## 3.6 Fail-closed declaration

Each completed contract must state what happens if required source authority or measurement prerequisites are unavailable or ambiguous.

For a required paid-pilot gate, the default must preserve the already accepted rule:

```text
UNRESOLVED REQUIRED METRIC CONTRACT
=> NOT GATE-ELIGIBLE
=> PAID PARTICIPATION BLOCKED / NO-GO
```

This is not the same as a measured `0%`.

After semantic closure, missing or late analytical/source data follows the frozen missing-data, freshness and restatement rules rather than reopening the definition.

## 3.7 Contradiction check

Before closure, the JIT decision must be checked against higher authority and source-Domain law.

If the proposed metric semantic would require:

- Analytics to own business truth;
- a source Domain to surrender or duplicate its truth;
- a Product/Roadmap rule to be weakened;
- an unresolved upstream rule to be invented downstream; or
- lifecycle semantics inconsistent with the owning Domain,

the metric cannot be marked complete.

The process must stop at the authority level that owns the contradiction.

---

# 4. Evidence required for `ANL-METRIC-003` — personalised-plan activation

Pass 11 routed source truth to **Plans & Nutrition** plus **Habits, Journals & Progress**.

Closure evidence must contain explicit decisions for:

- the exhaustive qualifying post-delivery activation action set;
- the activation measurement window/cutoff;
- correction/replacement/supersession treatment for delivered personalised plans;
- authoritative source timestamp(s);
- late-arrival reconciliation horizon where material; and
- finality/restatement semantics.

The closure record must demonstrate from current Product/Decision/Roadmap authority that:

- generation or notification alone is not activation;
- a single plan open is insufficient by itself; and
- the frozen definition is prospective.

The source-lifecycle evidence must show that the selected interpretation does not create an Analytics-owned activation lifecycle or contradict Plans/HJP ownership.

**Closure status until this evidence exists:** `OPEN / FP-006 JIT REQUIRED`.

---

# 5. Evidence required for `ANL-METRIC-004` — meaningful seven-day usage

Pass 11 routed source truth to **Habits, Journals & Progress**, **Plans & Nutrition**, plus whichever Domain lawfully owns the denominator population chosen by JIT.

Closure evidence must contain explicit decisions for:

- denominator population;
- exhaustive qualifying-engagement set;
- authoritative Day-1 anchor;
- timezone/day-boundary rule;
- authoritative source timestamp(s);
- late-arrival reconciliation horizon where material; and
- finality/restatement semantics.

The closure record must preserve the already-governed minimum:

- engagement on at least three distinct days in the first seven days; and
- at least one qualifying day after Day 1.

It must demonstrate that neither Analytics ingestion time nor an arbitrary UI-open stream became the business authority for Day-1/day-membership semantics.

If the chosen denominator requires an additional source Domain, that Domain’s relevant lifecycle evidence becomes part of the closure bundle.

**Closure status until this evidence exists:** `OPEN / FP-006 JIT REQUIRED`.

---

# 6. Evidence required for `ANL-METRIC-005` — successful plan generation

Pass 11 routed generation/outcome truth to **Plans & Nutrition**, with denominator ownership conditional on the selected lawful business unit.

Closure evidence must contain explicit decisions for:

- denominator business unit;
- treatment of valid General Wellness outcomes;
- retry/duplicate-request collapse semantics;
- recovery/measurement window;
- intentionally blocked/review-required/insufficient-information exclusions;
- authoritative source timestamp(s);
- late-arrival reconciliation horizon where material; and
- finality/restatement semantics.

The closure record must prove that:

- the denominator was not chosen merely because Plans generation requests are easiest to count;
- `general_wellness_only` is not treated as fulfilment of a purchased personalised-plan right;
- retries cannot inflate success counts; and
- any broader denominator is sourced from the Domain(s) that own the qualifying obligation/population.

The source evidence must be limited to the lifecycle facts material to the selected business unit rather than copying Commerce, Entitlements, Safety or Plans state into Analytics.

**Closure status until this evidence exists:** `OPEN / FP-006 JIT REQUIRED`.

---

# 7. Evidence required for `ANL-METRIC-006` — verified entitlement fulfilment

Pass 11 routed commercial truth to **Commerce** and grant/access truth to **Entitlements**.

Closure evidence must contain explicit decisions for:

- denominator business unit;
- recovery window;
- refund/reversal/dispute classification;
- retry/duplicate/convergence deduplication;
- revocation/closure treatment;
- authoritative source timestamp/correlation semantics;
- late-arrival reconciliation horizon where material; and
- finality/restatement semantics.

The closure record must prove that:

- payment success is not treated as entitlement success;
- provider callback state remains evidence rather than direct grant/remove/restore authority;
- Commerce and Entitlements truth remain distinct; and
- the aggregate `≥95%` operational rate does not weaken the independent zero-tolerance duplicate-entitlement integrity criterion.

A lifecycle path that is lawfully reversed/refunded/revoked must be classified by the frozen contract; Analytics may not silently call it success or failure based on convenience.

**Closure status until this evidence exists:** `OPEN / FP-006 JIT REQUIRED`.

---

# 8. Phase-7 placement rule

Pass 12 is a Pre-JIT evidence contract, not an FP-006 Phase 7 artifact.

The eventual routing must preserve the platform’s existing delivery sequence:

```text
Phase 7A Skeleton + Gate Manifest
    -> Phase 7B required JIT Domain Dossiers
    -> resolve required gates / conditional dossiers
    -> Phase 7C Final Feature Pack Contract
    -> explicit architectural-proof classification
```

Therefore:

- 7A may identify the metric-contract gate and affected Domains but may not pretend the unresolved semantics are already closed;
- required 7B dossiers must resolve/validate the source-Domain lifecycle questions assigned to them;
- 7C must carry the final resolved metric contract into the development-entry authority;
- semantic closure must not be inferred merely because a dossier exists;
- a JIT answer that never reaches the approved 7C Final Feature Pack Contract is not sufficient development-entry authority; and
- later proof classification verifies implementation architecture; it does not retroactively choose metric semantics.

Pass 12 does not create or approve any of those future FP-006 artifacts.

---

# 9. Pressure tests

## ANL-PT-047 — Can this Pre-JIT Pass 12 document itself mark `ANL-METRIC-003..006` contract-complete?

**Analysis:** No. This file is working/non-authoritative. It may define a closure-evidence requirement, but the unresolved semantic answers must be resolved through the future governed FP-006 Phase 7/JIT path and carried into the approved Final Feature Pack Contract.

**Disposition:** `CONFLICT` for Pre-JIT self-closure.

---

## ANL-PT-048 — Is a prose answer to every question sufficient without exact authority and source-owner lifecycle evidence?

**Analysis:** No. A plausible answer can still contradict Product Law or the owning Domain. Closure must be reproducible against exact current authority plus the material source lifecycle evidence.

**Disposition:** `CONFLICT`.

---

## ANL-PT-049 — Are authority citations alone sufficient if one required semantic remains implicit or `TBD`?

**Analysis:** No. Product Law requires the complete prospectively versioned metric contract. Authority references constrain the answer but do not substitute for the explicit answer.

**Disposition:** `CONFLICT`.

---

## ANL-PT-050 — Can passing implementation tests or a produced dashboard number compensate for an unresolved metric definition?

**Analysis:** No. Tests can prove implementation against a contract; they cannot invent the contract. A dashboard can calculate a number under hidden assumptions while still violating Product/Domain law.

**Disposition:** `CONFLICT`.

---

## ANL-PT-051 — Is a metric-definition version sufficient without an explicit cohort/effective point?

**Analysis:** No. Prospective evolution is only auditable when it is clear which definition governed which cohort. Version without effective scope permits silent retrospective reinterpretation.

**Disposition:** `CONFLICT`.

---

## ANL-PT-052 — Must the closure bundle reproduce an entire source Domain lifecycle?

**Analysis:** No. That would increase drift and create competing authority. Closure evidence should cite the authoritative lifecycle and extract only the states/transitions/invariants material to the metric decision.

**Disposition:** `PASS` for bounded source-lifecycle evidence; `CONFLICT` for shadow lifecycle copying.

---

## ANL-PT-053 — May metric closure bypass a JIT Domain Dossier that the future FP-006 Gate Manifest classifies as required?

**Analysis:** No. Current delivery governance requires every required JIT Domain Dossier to be approved before the Final Feature Pack Contract. Pass 12 cannot pre-classify every future FP-006 dossier, but closure cannot route around a dossier once the Gate Manifest requires it.

**Disposition:** `CONFLICT`.

---

## ANL-PT-054 — Must Pass 12 invent a standalone SHA-256 requirement for every future metric decision artifact?

**Analysis:** No. Current Product metric law requires metric-definition versioning, not a new metric-artifact hash field. For this closure-evidence contract, exact accepted repository commit SHA + artifact path/version provides reproducible byte provenance. A future governed FP-006 process may require stronger artifact hashing, but Pre-JIT must not invent it.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## ANL-PT-055 — Must architectural proof classification be completed before the metric’s semantic contract can be considered resolved?

**Analysis:** No. Semantic closure belongs in the Phase 7/JIT contract lineage and must reach the approved 7C Final Feature Pack Contract. `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` is the subsequent architectural-proof classification. Conflating them would either delay semantic decisions unnecessarily or let implementation proof substitute for Product/Domain decisions.

**Disposition:** `PASS` for separation of semantic closure from proof classification.

---

## ANL-PT-056 — Is an approved JIT answer sufficient if it is not carried into the approved Phase 7C Final Feature Pack Contract?

**Analysis:** No for development-entry authority. The JIT artifact may supply the resolved source/domain decision, but current delivery governance makes the approved Final Feature Pack Contract the development-entry authority. The final metric contract must therefore be carried forward without semantic drift.

**Disposition:** `CONFLICT`.

---

# 10. `ANL-GAP-003` after Pass 12

**Status:** `OPEN / FP-006 JIT REQUIRED`.

Pass 12 does not close a single unresolved semantic question from Pass 11.

It narrows the definition of legitimate future closure:

A metric may move from open to semantically complete only when:

1. every required semantic has an explicit answer;
2. exact controlling authority is cited;
3. the material lifecycle evidence from every required source Domain is cited/validated;
4. all Product-Law-required metric fields are frozen;
5. metric-definition version + cohort/effective point are pinned prospectively;
6. JIT artifact path/version + accepted repository commit are pinned;
7. fail-closed behaviour is explicit;
8. no upstream contradiction remains;
9. required 7B dossier obligations are satisfied; and
10. the resolved contract is carried into the approved 7C Final Feature Pack Contract.

Until then, the existing paid-participation NO-GO rule remains.

`ANL-GAP-001` and `ANL-GAP-002` remain unchanged.

---

# 11. Pass-12 disposition

**PASS WITH REQUIRED JIT FOLLOW-UP — THE CLOSURE-EVIDENCE CONTRACT IS DEFINED; NO METRIC SEMANTICS, PHASE-7 ARTIFACTS OR ARCHITECTURAL-PROOF CLASSIFICATION HAVE BEEN CREATED.**

The safe working result is:

- Pass 11 owner/question routing is preserved;
- semantic closure is separated from implementation proof and analytical output;
- exact authority + bounded source-lifecycle evidence are required;
- complete metric payload + version/effective-cohort pin are required;
- exact repository commit + path/version provides the minimum reproducible artifact pin for this Pre-JIT contract;
- required JIT dossiers cannot be bypassed;
- the approved Phase 7C Final Feature Pack Contract must carry the resolved metric contract before it becomes development-entry authority;
- an unresolved required contract still blocks first paid participation; and
- no Product, Architecture, Domain or Roadmap amendment is justified by Pass 12 on current evidence.

**Recommended next focused pass after human acceptance:** pressure-test the minimum FP-006 Phase 7 insertion map for metric-contract closure evidence — what belongs in 7A Gate Manifest routing, what must be resolved/validated in required 7B Domain Dossiers, what must be carried into 7C Final Feature Pack Contract, and what is deferred to later proof/release-readiness evidence — without creating FP-006 artifacts or choosing the unresolved metric semantics.
