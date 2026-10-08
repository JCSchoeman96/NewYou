# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.14.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.13.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification, replacement/retake, execution-provenance, result-correction, profile-source, reassessment, report-lifecycle, identity-reconciliation and privacy-lifecycle semantics. This file appends the accepted Research & Feedback / Interactive Tools authority-isolation contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.14.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.13.0.md`
- **Predecessor blob SHA:** `efb5387491a8065f953cc054e6cc326a2e05d0ec`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-018 — Research/Feedback and Interactive-Tool authority isolation

**Accepted:** `2026-10-08`

Research/Feedback responses, optional assessment feedback and Interactive-Tool outputs remain within their approved purpose and do not directly create or mutate authoritative Temperament assessment or profile truth. Software calculation, visualisation, research participation or UI similarity does not itself confer Temperament authority.

### AT-WD-018A — Research response is never an Assessment Answer merely because content overlaps

A Research/Feedback response remains Research/Feedback truth even where the visible question wording, answer options or derived computation resembles or duplicates an assessment instrument.

Research participation does not by itself create:

- an Assessment Attempt;
- a scored Assessment Answer;
- a Score Set;
- a digital Temperament Result;
- an assessment report;
- assessment-entitlement consumption; or
- an annual-reassessment anchor.

Purpose and owning-Domain authority remain controlling.

### AT-WD-018B — Optional assessment feedback is non-scoring and separately owned

Optional feedback attached to an assessment experience may support research, support, content improvement or methodology review, but it is not a scored answer and may not:

- alter deterministic scoring;
- satisfy or block scored-input completeness merely by being present/absent;
- mutate a frozen submission/result; or
- give staff an alternate path for changing participant answers.

### AT-WD-018C — Interactive temperament output is non-authoritative by default

A quiz, calculator, visualisation, decision aid or other Interactive Tool may produce an educational/personalised output such as a suggested colour/profile, but that output is not a digitally assessed Temperament Result and receives none of the digital-assessment consequences by default.

In particular it does not create exact governed digital scores/report provenance, consume an assessment right, establish a qualifying completion or annual retake clock, or automatically become current-profile truth.

Being logged in does not change this authority boundary.

### AT-WD-018D — Anonymous/public tool output cannot be retroactively attached as participant truth

An anonymous or public interactive result has no canonical participant authority. Later authentication must not silently attach browser-local or previously anonymous tool output to a participant profile merely because the platform believes the same human used it.

### AT-WD-018E — Explicit participant declaration is the only permitted Temperament promotion path from tool context

A participant may intentionally use a non-authoritative tool result as context for a Temperament declaration only through an explicit Temperament-owned declaration action.

The participant-facing consequence must be clear enough to communicate that a durable declared profile/history fact will be created or updated. A generic save/bookmark interaction is insufficient authority.

The resulting Temperament truth is a **declared profile** with governed declaration provenance; it is never reclassified as digitally assessed merely because software suggested the declaration.

Exact UI wording/mechanics remain JIT/frontend work.

### AT-WD-018F — Declaring and selecting current profile remain separate durable truths

Creation of a declared profile from an explicit participant action does not automatically make that declaration the current profile unless Product Law explicitly governs a combined participant action whose separate consequences remain clear.

`AT-WD-013` current-profile selection semantics continue to apply.

### AT-WD-018G — Research response is not another Domain's command

Research/Feedback answers do not silently become Communications preferences, Temperament declarations, entitlement changes or other-Domain durable facts.

Where Product law permits a follow-on action, the participant must explicitly invoke the owning Domain's governed action. The reusable invariant is: **response does not equal command**.

### AT-WD-018H — Staff/researcher interpretation cannot promote participant truth

A researcher, support agent or staff reviewer may not convert Research/Feedback responses or Interactive-Tool outputs into authoritative Temperament declarations, digital results or current-profile selections merely because the data appears suggestive.

Any authoritative participant-specific change must use the separately governed owning-Domain path and authority.

### AT-WD-018I — Later tool/research algorithm changes do not rewrite Temperament history

If a participant explicitly created a declared profile after considering a prior tool output, later changes to the tool algorithm/content do not recalculate or rewrite the historical declaration. The declaration records the participant's durable choice at that time.

A later change requires a new governed declaration/current-profile action as applicable.

### AT-WD-018J — Research incentives route through Entitlements

Where an authorised Research/Feedback campaign grants an assessment-related incentive, Research may create only the governed grant/access intent permitted by its authority. Entitlements establishes/reconciles the actual commercial access right.

Research completion itself does not start an assessment attempt; ordinary first-answer commitment remains the Temperament start/consumption boundary.

---

# 2. Upstream position

No new upstream Product/Domain defect is created by this pass. Current Product and Domain Law already establish the key rule that Research/Feedback and Interactive-Tool outputs do not silently become other-Domain authority.

`AT-WD-018` narrows that existing rule for FP-003/JIT by defining the explicit participant-declaration crossing semantics and prohibiting implicit promotion.

---

# 3. Pressure-test additions — v0.14.0

## AT-PT-136 — Research survey responses resemble Blue

**Scenario:** research responses strongly resemble a Blue temperament pattern.

**Expected:** no Assessment Attempt, digital score/result, declaration, current-profile change or entitlement consumption occurs.

**Result:** `PASS` under AT-WD-018A.

## AT-PT-137 — Research instrument duplicates assessment wording

**Scenario:** an approved research instrument happens to use textually identical questions/options to the assessment.

**Expected:** responses remain Research/Feedback truth because purpose/authority differ; they are not Assessment Answers.

**Result:** `PASS` under AT-WD-018A.

## AT-PT-138 — Research system computes four colour values

**Scenario:** research analytics computes four colour-like values from research responses.

**Expected:** those values do not become canonical Temperament Score Set, digital result or report provenance.

**Result:** `PASS` under AT-WD-018A/C.

## AT-PT-139 — Optional feedback blank at final submission

**Scenario:** all required scored inputs are complete but optional assessment feedback is blank.

**Expected:** blank feedback does not block final submission and has no scoring effect.

**Result:** `PASS` under AT-WD-018B + AT-WD-007.

## AT-PT-140 — Optional feedback criticises scored answer

**Scenario:** participant answers a scored item then writes feedback saying the item was confusing.

**Expected:** feedback remains separate and does not alter the scored answer/result. Any future methodology/content correction follows governed authority rather than mutating this submission.

**Result:** `PASS` under AT-WD-018B + AT-WD-012.

## AT-PT-141 — Anonymous public temperament quiz returns Green

**Scenario:** unauthenticated visitor completes a public quiz and receives a Green suggestion.

**Expected:** educational output only; no participant profile/result exists and later login must not silently attach it.

**Result:** `PASS` under AT-WD-018C/D.

## AT-PT-142 — Logged-in quiz returns Yellow

**Scenario:** authenticated participant completes a non-authoritative interactive quiz.

**Expected:** login identity does not elevate the output into Temperament truth. No profile/result/current mutation occurs automatically.

**Result:** `PASS` under AT-WD-018C.

## AT-PT-143 — Participant explicitly declares tool-suggested Green

**Scenario:** after a tool suggests Green, participant knowingly invokes a Temperament action equivalent to declaring Green as her profile.

**Expected:** a new declared-profile fact may be created through Temperament with governed declared provenance. It is not a digital assessment result.

**Result:** `PASS` under AT-WD-018E.

## AT-PT-144 — Participant closes tool without declaration

**Scenario:** tool displays a result but participant takes no explicit Temperament declaration action.

**Expected:** no durable Temperament profile mutation.

**Result:** `PASS` under AT-WD-018E.

## AT-PT-145 — New declaration versus current-profile selection

**Scenario:** participant explicitly declares Green from tool context but does not explicitly select it as current.

**Expected:** declaration history may append; current-profile selection remains unchanged.

**Result:** `PASS` under AT-WD-018F + AT-WD-013.

## AT-PT-146 — Research answer resembles preference

**Scenario:** research asks whether weekly reminders are preferred and participant answers weekly.

**Expected:** Communications preference remains unchanged unless participant separately invokes the governed preference action.

**Result:** `PASS` under AT-WD-018G.

## AT-PT-147 — Staff promotes research response to Blue

**Scenario:** staff reviewer decides research responses imply Blue and tries to set participant Temperament truth directly.

**Expected:** prohibited; staff/research interpretation is not declaration/digital-assessment authority.

**Result:** `PASS` under AT-WD-018H.

## AT-PT-148 — Tool algorithm changes after declaration

**Scenario:** Tool V1 suggested Green and participant explicitly declared Green; Tool V2 would later suggest Yellow from the same inputs.

**Expected:** historical Green declaration is not recalculated/rewritten. Participant may create a new declaration later through the ordinary governed path.

**Result:** `PASS` under AT-WD-018I.

## AT-PT-149 — Research campaign awards assessment access

**Scenario:** authorised research participation earns an assessment-related incentive.

**Expected:** Research/Feedback may emit the authorised grant intent; Entitlements owns creation/reconciliation of the actual right. No Assessment Attempt starts until ordinary first-answer commitment.

**Result:** `PASS` under AT-WD-018J.

---

# 4. Open-question queue after v0.14.0

The Research/Feedback / Interactive Tools boundary is now materially constrained by `AT-WD-018` and `AT-PT-136...149` without creating a new upstream amendment.

Next unresolved cluster:

- **Methodology Authority Input Contract:** define the minimum externally approved, rights-backed, versioned methodology package FP-003 must receive before proprietary assessment content/scoring/tie/mask/interpretation behavior may be encoded or published. Distinguish methodology authority from Product application, Content/translation publication, Health review and Super Admin operation; fail closed on incomplete or contradictory authority inputs.

After that, perform the final adversarial cross-decision sweep before determining whether Assessment / Temperament Pre-JIT is eligible to park.
