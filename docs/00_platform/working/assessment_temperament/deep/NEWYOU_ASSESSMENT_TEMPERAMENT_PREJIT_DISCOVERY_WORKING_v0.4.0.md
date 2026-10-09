# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.4.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0`, `v0.2.0` or `v0.3.0`. Read those predecessors first for the accepted start, entitlement, expiry, subscription, technical-recovery and final-submission semantics. This file appends the accepted active-attempt answer-concurrency contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.4.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.3.0.md`
- **Predecessor blob SHA:** `4c9d759b7762d9c82fd59b82be29bbed3b6d5d3c`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-008 — Conflict-aware active-attempt answer concurrency

**Accepted:** `2026-10-08`

While an Assessment Attempt remains active/editable, the platform may accept answer changes from more than one participant editing surface, but concurrency must preserve participant intent and may not silently overwrite a newer authoritative answer with stale state.

### AT-WD-008A — Different-question edits may merge

Concurrent edits to different questions do not inherently conflict.

If two valid editing surfaces change different answers and both mutations satisfy current attempt/version/deadline guards, both may become authoritative without requiring an exclusive attempt-level editing lock.

### AT-WD-008B — Same-question stale writes must not silently overwrite

A mutation to an answer may replace only the authoritative answer state that the editing context reasonably believed it was modifying.

If another mutation has already changed that same authoritative answer, a stale mutation must not silently win merely because it arrives later.

The stale editing surface must instead receive a conflict/stale-state outcome and reconcile with the current authoritative answer before any deliberate replacement.

This is a semantic correctness requirement only. This Pre-JIT does not yet choose revision columns, ETags, optimistic locking, Ash mechanisms or API shapes.

### AT-WD-008C — No exclusive browser/session lock required by Product semantics

The platform is not required to make one browser, tab or device the exclusive editor merely to achieve correctness.

The stable business model remains one authoritative Assessment Attempt with potentially multiple editing surfaces and conflict-safe durable writes.

An exclusive technical editing lock may be considered later only if separately justified; it is not created as durable business truth by this discovery.

### AT-WD-008D — Local state is not authoritative saved progress

An editing surface must distinguish local/unsaved state from durably accepted authoritative progress.

A UI must not present an authoritative `Saved` state merely because a browser retained a local value. Failed, offline or conflict-rejected mutations remain unsaved/non-authoritative until the server accepts them.

This preserves the current frontend requirement for durable save/autosave where safe, visible saved-state indication and explicit resume from authoritative progress.

### AT-WD-008E — Final submission requires a coherent known current snapshot

A stale editing surface may not silently final-submit an authoritative answer set that materially differs from the answer state that surface is known to be submitting.

If authoritative scored answers changed outside the submitting context after that context's last known coherent saved snapshot, finalisation must fail closed for reconciliation/review rather than silently freeze unseen changes.

The exact UX for reconciliation is deferred. The semantic requirement is that participant final-submit intent must correspond to the coherent authoritative answer snapshot being frozen under `AT-WD-007`.

### AT-WD-008F — Submission remains the terminal write cutover

Answer writes that become authoritative before the accepted submission snapshot may contribute to that snapshot.

Once `AT-WD-007` final-submission acceptance is authoritative:

- later or delayed answer writes are rejected/stale;
- no autosave may mutate the frozen submission;
- answer concurrency rules cannot reopen submitted answers.

---

# 2. Pressure-test additions — v0.4.0

## AT-PT-037 — Two devices edit different questions

**Scenario:** phone changes Q12 while laptop changes Q27 during the same active attempt.

**Expected:** both writes may be accepted if independently valid; no attempt-level conflict is required merely because two devices were active.

**Result:** `PASS` under AT-WD-008A.

## AT-PT-038 — Two devices edit the same question from the same prior state

**Scenario:** phone and laptop both display Q12=`A`; laptop durably changes it to `B`; a delayed phone write attempts to replace Q12 using its stale `A` context.

**Expected:** the stale mutation must not silently overwrite `B`. It receives a conflict/stale outcome and must reconcile before any deliberate replacement.

**Result:** `PASS` under AT-WD-008B.

## AT-PT-039 — Offline autosave reconnects with stale answers

**Scenario:** a browser goes offline, accumulates local changes, then reconnects after another device has changed some of the same answers.

**Expected:** non-conflicting different-question changes may be admitted; stale same-answer mutations conflict rather than overwrite newer authoritative values. Local persistence alone never made the offline values authoritative.

**Result:** `PASS` under AT-WD-008A/B/D.

## AT-PT-040 — Browser shows local value but durable save failed

**Scenario:** participant changes an answer; browser retains it locally but server save fails.

**Expected:** UI must not claim authoritative `Saved`; resume from another device uses the last durably accepted answer. Participant must receive failure/retry/reconciliation semantics rather than false confidence.

**Result:** `PASS` under AT-WD-008D.

## AT-PT-041 — Stale tab final-submits after another device changed an answer

**Scenario:** laptop last knew Q20=`A`; phone later durably changes Q20=`B`; stale laptop still displays `A` and attempts final submission.

**Expected:** final submission must not silently freeze an answer set containing unseen `B`. The stale submitting context fails closed for reconciliation/review before a coherent snapshot may be finalised.

**Result:** `PASS` under AT-WD-008E + AT-WD-007.

## AT-PT-042 — Answer save races final submission

**Scenario:** a valid answer write and final-submit operation race.

**Expected:** exactly one coherent authoritative snapshot boundary wins. A write authoritative before snapshot commitment may be included; a losing/stale write after submission is rejected and cannot mutate frozen answers.

**Result:** `PASS AT SEMANTIC LEVEL` under AT-WD-008F + AT-WD-007; technical revision/locking mechanism deferred.

## AT-PT-043 — Delayed autosave arrives after accepted submission

**Scenario:** browser queues an autosave before submission; network delay causes it to arrive only after final submission is authoritative.

**Expected:** delayed autosave is rejected/stale. Submitted answers remain immutable.

**Result:** `PASS` under AT-WD-008F.

## AT-PT-044 — Stale device attempts deliberate overwrite after conflict

**Scenario:** device receives a conflict because its same-question state is stale; participant reviews the authoritative value and deliberately chooses a new replacement.

**Expected:** a later explicit mutation may succeed if based on current authoritative state and the attempt remains editable. Conflict protection prevents accidental overwrite; it does not permanently lock the answer.

**Result:** `PASS` under AT-WD-008B.

---

# 3. Open-question queue after v0.4.0

`AT-OI-003` is resolved by `AT-WD-008` and `AT-PT-037...044`, subject to later governed formalisation.

Next unresolved:

- **AT-OI-004 — Notification policy detail:** exact warning cadence/channel hierarchy and evidence expectations while notification remains non-authoritative over Temperament expiry.
- **AT-OI-005 — Subscription replacement abuse/fair-use boundary:** bounded controls without redefining the promised one included completed assessment.

Later passes still include assessment/methodology/content/language version provenance; result correction/invalidation/supersession; declared vs assessed vs historical/current-profile semantics; reassessment interactions; report generation/publication/access/delivery; identity merge; privacy/retention; Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
