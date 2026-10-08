# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.7.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.6.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification and replacement/retake semantics. This file appends the accepted governed assessment-execution provenance contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.7.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.6.0.md`
- **Predecessor blob SHA:** `3d83c1ae2c6b89333171b9578d35240d91ce22b2`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-011 — Governed assessment execution provenance

**Accepted:** `2026-10-08`

The first durably accepted scored answer pins one complete governed assessment execution context sufficient to reproduce both the participant-facing assessment instrument and the deterministic scoring semantics used by that Assessment Attempt.

This is a semantic provenance bundle. This Pre-JIT does **not** require a Resource named `AssessmentExecutionContext` and does not choose schema boundaries.

### AT-WD-011A — Minimum pinned governed context

The pinned context must resolve, at minimum:

1. the exact approved methodological version;
2. the exact assessment instrument/question set applicable to that methodological version;
3. stable identities for scored questions and answer options;
4. required and conditional-input rules that affect completion;
5. scoring-affecting mappings, weights and other approved deterministic scoring inputs belonging to that governed version;
6. approved tie/conditional workflow definitions where methodology requires them;
7. the governed language variants compatible with that instrument/version.

A later result must not be reproduced by dereferencing whatever methodology, question set, answer mapping or weight is current at replay time.

### AT-WD-011B — Governed language switching within one pinned context

Afrikaans and English remain separately governed language variants of one methodological version.

During an active attempt, the participant may switch language only between approved language variants that belong to the same pinned methodological/instrument context.

A language switch may not silently move the attempt onto a different methodological or instrument version merely because a newer translation or assessment version has become current.

### AT-WD-011C — Preserve participant-facing variant provenance

Each accepted scored answer must remain sufficiently traceable to establish:

- the exact governed question identity;
- the exact governed answer-option identity or equivalent governed response identity;
- the participant-facing governed language variant under which that answer was accepted.

This provenance requirement does not imply that language changes scoring. It exists so the platform can later establish what governed wording/context produced the accepted answer.

### AT-WD-011D — Ordinary publication changes do not mutate a started attempt

After first-answer commitment, ordinary publication of a successor assessment, translation correction, wording improvement or version retirement does not silently mutate the pinned execution context of the active attempt.

New attempts use the then-current startable governed context. Existing active short-lived attempts may continue their pinned context according to existing version law.

### AT-WD-011E — Critical defects require explicit invalidation/recovery, never silent rebinding

If a materially defective or invalid assessment version is discovered while an attempt is active, the platform must not repair provenance by silently rebinding that attempt to a corrected version.

Any stop, invalidation, replacement or recovery must be explicit, preserve the original historical provenance and compose with the technical-recovery and later result-correction/invalidation semantics.

The exact invalidation authority and state model are deferred to the next Pre-JIT pass.

### AT-WD-011F — Report content is a downstream versioned lifecycle

The attempt-start execution context governs assessment inputs and scoring semantics. It does not freeze future report wording/template/content merely because the assessment has started.

Report interpretation, rendering, language and delivery provenance are downstream governed concerns that must bind to the canonical result and their own governed content/version context.

---

# 2. Pressure-test additions — v0.7.0

## AT-PT-063 — Participant switches English to Afrikaans mid-attempt

**Scenario:** participant starts under an approved English variant and later switches to Afrikaans while the attempt remains active.

**Expected:** switch is allowed only to the approved Afrikaans counterpart within the same pinned methodological/instrument context. Scoring semantics do not change merely because display language changes.

**Result:** `PASS` under AT-WD-011B.

## AT-PT-064 — Translation successor published while attempt is active

**Scenario:** a newer Afrikaans translation is published after the participant already started an attempt.

**Expected:** the active attempt does not silently adopt the newer translation if it belongs to a different governed variant/version set. Historical answer provenance remains tied to the governed participant-facing variant actually used.

**Result:** `PASS` under AT-WD-011B/C/D.

## AT-PT-065 — Future scoring weights change

**Scenario:** V2 introduces versioned question or answer weights while a participant remains active on V1.

**Expected:** the V1 attempt continues and, if submitted, scores using the V1 governed scoring inputs. Replaying the result later must not use V2 weights.

**Result:** `PASS` under AT-WD-011A/D.

## AT-PT-066 — Question removed from successor assessment

**Scenario:** V2 removes or materially changes a V1 question while a V1 attempt is already active.

**Expected:** the active V1 attempt retains its V1 instrument. New V2 publication does not rewrite the V1 participant's question set.

**Result:** `PASS` under AT-WD-011D.

## AT-PT-067 — Version retires after first answer

**Scenario:** V1 retires after first-answer commitment but before final submission.

**Expected:** the already-started short-lived attempt retains its pinned V1 context and may finish within its valid lifetime unless a separate critical-defect invalidation applies.

**Result:** `PASS` under AT-WD-011D + existing DEC-067 semantics.

## AT-PT-068 — Version retires before first answer

**Scenario:** participant viewed V1 but saved no scored answer before V1 retires, then attempts a stale first-answer write.

**Expected:** no V1 attempt existed; stale start fails closed and cannot pin a retired context.

**Result:** `PASS` under AT-WD-011 + AT-WD-002.

## AT-PT-069 — Material scoring defect discovered in active pinned version

**Scenario:** methodology authority establishes that the pinned version contains a material scoring defect.

**Expected:** platform must not silently replace V1 scoring with corrected V2 scoring inside the existing attempt. Explicit invalidation/recovery semantics are required and original provenance remains visible.

**Result:** `PASS AS REQUIRED INVARIANT`; exact invalidation semantics remain next-pass work.

## AT-PT-070 — Report copy changes during active assessment

**Scenario:** report wording/template improves after the participant has started but before result/report generation.

**Expected:** attempt scoring provenance is unaffected. Report generation later binds its own governed report/content version to the canonical result; report copy was not frozen merely by attempt start.

**Result:** `PASS` under AT-WD-011F.

---

# 3. Open-question queue after v0.7.0

Assessment/methodology/content/language execution provenance is now materially constrained by `AT-WD-011` and `AT-PT-063...070`, subject to later JIT Resource design and the methodology/IP gate.

Next unresolved cluster:

- **Result correction / invalidation / supersession:** distinguish immutable raw result from reviewed interpretation, materially defective methodology/scoring, corrected recomputation if ever authorised, historical visibility, current-profile effects and report consequences.

Later passes still include declared vs assessed vs historical/current-profile semantics; reassessment interactions; report generation/publication/access/delivery; identity merge; privacy/retention; Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
