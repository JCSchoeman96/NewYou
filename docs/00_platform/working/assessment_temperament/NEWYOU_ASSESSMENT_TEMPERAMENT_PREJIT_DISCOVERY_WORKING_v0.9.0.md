# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.9.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.8.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification, replacement/retake, execution-provenance and result-correction semantics. This file appends the accepted temperament profile-source separation contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.9.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.8.0.md`
- **Predecessor blob SHA:** `33abf23b541b94c2ff13f19c3fde25757b62710e`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-013 — Temperament profile-source separation

**Accepted:** `2026-10-08`

Declared temperament profiles, immutable digital assessment results, current-profile selection, and participant/learned personalisation preferences are distinct durable concepts. None may silently become or overwrite another.

### AT-WD-013A — Declared profiles remain declared provenance

A self-reported or book-derived temperament profile records that the participant declared a profile with that provenance at a point in time.

A declared profile:

- is not a digital assessment result;
- does not gain exact digital assessment scores merely because it is selected current;
- does not gain a paid digital report merely because it is selected current;
- may support approved low-risk personalisation where governing Product/safety rules permit;
- retains declaration provenance and sufficient historical timing/context to explain later governed use.

### AT-WD-013B — Digital assessment appends a distinct result

A digitally assessed result records the immutable outcome produced from frozen submitted answers and the exact governed assessment execution context.

Later digital completion does not convert, mutate or overwrite an earlier declared profile. Both remain distinct historical facts subject to retention/deletion law.

Example:

`book_derived Yellow`
→ later `digitally_assessed Blue`

means two distinct provenance-bearing historical truths. The later digital result does not rewrite the earlier declaration.

### AT-WD-013C — Current-profile selection is separate mutable participant-controlled truth

Current-profile selection represents which **currently eligible profile source** the participant has chosen for applicable current low-risk personalisation.

Changing current-profile selection:

- does not alter declared-profile history;
- does not alter digital-result history;
- does not alter any immutable score/result;
- does not create a reassessment;
- does not consume an assessment entitlement;
- must retain sufficient audit/history to explain which source was current over time where downstream reproducibility requires it.

Exact Resource/schema representation is deferred to JIT work.

### AT-WD-013D — New digital result does not automatically become current

Where a participant has a current declared profile and later completes a digital assessment, the digital result is surfaced as a new eligible source but does not silently replace the participant-selected current profile.

The participant must explicitly select an eligible source according to Product Law.

A declared source may remain current where still eligible, but being current never upgrades its provenance or output rights to digitally assessed status.

### AT-WD-013E — Meaningful declaration changes append history

If the participant meaningfully changes a self-reported/book-derived temperament declaration, the prior declaration must not be silently rewritten as though it never existed.

The later declaration appends new declaration history. The participant may then select the later eligible declaration as current.

Declared-profile changes do not themselves consume digital assessment credits, annual reassessment rights or Premium reassessment entitlement.

### AT-WD-013F — Multiple legitimate digital results remain historical

A later legitimately completed reassessment appends another immutable digital result. Earlier valid results remain historical and are not overwritten merely because a later result exists.

A later result does not automatically become current. Current-profile selection remains explicit among eligible sources.

### AT-WD-013G — Invalid/ineligible sources cannot remain effective current sources

If the source currently selected becomes invalidated or otherwise ineligible for active use under `AT-WD-012`, the source remains historical but can no longer continue as effective current personalisation authority.

The platform must not silently choose a replacement source. Participant reselection/confirmation is required where another eligible source exists.

### AT-WD-013H — Personalisation preferences do not rewrite temperament truth

Explicit participant preferences and learned behavioural preferences remain distinct from temperament profile/result history.

Feedback or observed behaviour may influence approved personalisation behavior where governing Product/safety rules permit, but must not silently:

- change a declared temperament profile;
- change a digital assessment result;
- fabricate a new temperament provenance;
- alter historical current-profile selections.

Higher-precedence clinical, safety, nutritional and contextual authority remains unaffected.

### AT-WD-013I — Durable personalised outputs retain producing profile provenance where reproducibility matters

A durable materially personalised output whose later explanation/reproduction depends on temperament must retain sufficient provenance to identify the eligible profile source/current selection used when that output was produced.

A later current-profile change must not make historical outputs appear to have been generated from the new source.

This requirement does not make every page view a durable snapshot and does not prescribe the downstream Resource design; each owning Feature Pack/JIT contract must bind the provenance required for its durable governed output.

---

# 2. Pressure-test additions — v0.9.0

## AT-PT-081 — Book-derived Yellow then digital Blue

**Scenario:** participant onboards with book-derived Yellow, selects it current, and later completes a digital assessment producing Blue.

**Expected:** preserve both provenance-bearing truths. Blue does not silently replace Yellow as current; participant chooses among eligible sources.

**Result:** `PASS` under AT-WD-013A-D.

## AT-PT-082 — Participant chooses the later digital result

**Scenario:** after AT-PT-081, participant explicitly selects digital Blue as current.

**Expected:** current-profile selection changes to Blue; historical Yellow declaration remains unchanged; no new assessment or entitlement consumption is created by selection.

**Result:** `PASS` under AT-WD-013C/F.

## AT-PT-083 — Participant later switches back to eligible declared profile

**Scenario:** digital Blue exists, but participant later explicitly selects still-eligible declared Yellow as current for applicable low-risk personalisation.

**Expected:** selection may change back where Product/safety rules permit. Yellow remains declared provenance only and acquires no digital scores/report rights.

**Result:** `PASS` under AT-WD-013A/C/D.

## AT-PT-084 — Self-reported Yellow changes to self-reported Green

**Scenario:** participant later changes her declaration from Yellow to Green.

**Expected:** append a later Green declaration; preserve prior Yellow declaration/history; no digital assessment entitlement is consumed merely by declaration change.

**Result:** `PASS` under AT-WD-013E.

## AT-PT-085 — Feedback suggests another temperament

**Scenario:** behavioural feedback/learned preference patterns look inconsistent with the current temperament profile.

**Expected:** feedback may influence separately governed preferences/personalisation but must not rewrite declaration/result history or silently fabricate another temperament source.

**Result:** `PASS` under AT-WD-013H.

## AT-PT-086 — Later legitimate digital reassessment differs from earlier digital result

**Scenario:** R1 is a valid historical digital result; a later entitled reassessment produces R2 with materially different scores/profile.

**Expected:** preserve R1 and R2; R2 does not overwrite R1 and does not automatically become current.

**Result:** `PASS` under AT-WD-013F.

## AT-PT-087 — Current digital result later invalidated

**Scenario:** R1 was selected current and later becomes invalid/ineligible under result-correction law.

**Expected:** R1 remains historical but stops acting as effective current authority. Platform does not silently choose a declared profile or another digital result; participant reselection/confirmation is required.

**Result:** `PASS` under AT-WD-013G + AT-WD-012E/F.

## AT-PT-088 — Declared profile remains current despite digital result existing

**Scenario:** participant deliberately keeps book-derived Yellow current after valid digital Blue becomes available.

**Expected:** allowed where otherwise eligible. Personalisation must not describe Yellow as digitally assessed and must not expose Blue's digital scores/report as attributes of Yellow.

**Result:** `PASS` under AT-WD-013A/D.

## AT-PT-089 — Historical plan generated while Yellow was current

**Scenario:** a durable personalised plan was generated while declared Yellow was current; participant later switches current to digital Blue.

**Expected:** historical plan remains traceable to Yellow as the producing profile source and does not appear retroactively generated from Blue.

**Result:** `PASS` under AT-WD-013I.

## AT-PT-090 — Explicit behavioural preference conflicts with temperament tendency

**Scenario:** current profile is Blue but participant explicitly prefers less structure/shorter reminders.

**Expected:** preference may influence allowed delivery/personalisation without rewriting Blue, changing scores, or fabricating another profile.

**Result:** `PASS` under AT-WD-013H.

---

# 3. Open-question queue after v0.9.0

The declared/digital/historical/current-profile separation cluster is now materially constrained by `AT-WD-013` and `AT-PT-081...090`, subject to later JIT Resource design and downstream Feature Pack provenance contracts.

Next unresolved cluster:

- **Reassessment interactions:** ordinary paid retakes, annual interval, Premium annual reassessment, initial subscription-completion semantics, invalidated/corrected prior results, current-profile selection, one-active-attempt constraints, entitlement ordering and whether remediation counts as a retake.

Later passes still include report generation/publication/access/delivery; identity merge; privacy/retention; Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
