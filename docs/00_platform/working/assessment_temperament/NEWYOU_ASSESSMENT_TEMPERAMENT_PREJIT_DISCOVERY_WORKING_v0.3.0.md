# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.3.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` or `v0.2.0`. Read those predecessors first for the accepted start, entitlement, expiry, subscription and technical-recovery semantics. This file appends the accepted final-submission commitment boundary and its pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.3.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.2.0.md`
- **Predecessor blob SHA:** `4ed3beae14b6b8bad15a7b36683f69c49221476e`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-007 — Authoritative final-submission commitment boundary

**Accepted:** `2026-10-08`

Participant click/request intent is not itself the irreversible submission event. An Assessment Attempt remains active/editable until the platform authoritatively validates and durably accepts one exact final answer snapshot for the pinned governed assessment context.

Authoritative final-submit acceptance requires, at minimum:

1. the attempt is still active and inside its fixed deadline;
2. the request belongs to that exact canonical attempt and pinned governed context;
3. every methodology-required scored input is complete;
4. any methodology-required conditional inputs, including approved tie-break inputs where applicable, are satisfied or the approved methodology explicitly permits the unresolved outcome;
5. the exact answer snapshot being committed is known and durably accepted.

A failed/rejected final-submit request does not freeze the attempt. Missing required inputs leave the attempt active/editable. Optional feedback that is not part of scoring must not block assessment completion merely because it is unanswered.

### AT-WD-007A — Submission acceptance freezes participant answers

Once authoritative final-submit acceptance occurs:

- the committed scored-answer snapshot is immutable while retained;
- ordinary participant answer editing is permanently closed for that attempt;
- later stale/autosave writes may not become authoritative behind the frozen submission;
- duplicate/retried final-submit requests resolve to the same canonical submission rather than creating another submission.

Submitted answers must never be reopened merely because later scoring, report generation or delivery encounters a technical problem.

### AT-WD-007B — Timely accepted submission ends expiry risk

The fixed 30-day deadline governs whether final submission may still be authoritatively accepted.

If submission is accepted before the deadline, the participant has completed the participant-controlled portion of the assessment in time. Later deterministic scoring/result persistence may finish after the deadline without turning that already-accepted submission into an expired attempt.

If submission has not been authoritatively accepted before expiry, expiry wins and a late request may not resurrect the attempt.

### AT-WD-007C — Canonical result issuance is a required deterministic consequence

Authoritative submission acceptance and canonical result persistence are distinct semantic boundaries even if a later implementation can safely make them atomic.

After accepted submission:

- the platform owns deterministic completion from the same frozen inputs and pinned governed methodology/version;
- process crash, worker failure or delayed computation must not reopen answers, consume another right or issue a replacement attempt;
- replay/recovery must converge to exactly one canonical result for that accepted submission;
- duplicate result creation is prohibited.

A submitted-but-result-not-yet-persisted state may therefore exist as lifecycle truth; this Pre-JIT does not require it to be a separate Resource.

### AT-WD-007D — Conditional methodology completeness

Base-question completion does not automatically equal final methodology completeness.

If the approved methodology requires conditional scored inputs such as tie-break questions, those inputs are part of the completeness predicate for final-submit acceptance. The platform must not first create an immutable result and then mutate it merely because required tie-break input was collected afterwards.

If the approved methodology permits a still-equal/mixed result after its governed tie workflow, that unresolved result is legitimate and the platform must not invent another tie-resolution rule.

### AT-WD-007E — Submission/result/report boundaries stay distinct

The working lifecycle now distinguishes:

`active/editable attempt`
→ `authoritatively accepted/frozen submission`
→ `exactly one canonical immutable result`
→ `governed report/render/publication/delivery lifecycle`

Failure in a downstream boundary does not silently roll back a valid upstream boundary.

---

# 2. Pressure-test additions — v0.3.0

## AT-PT-027 — Missing required scored answer at final submit

**Scenario:** participant clicks final submit with one required scored answer missing.

**Expected:** finalisation is rejected; no frozen submission exists; attempt remains active/editable while inside deadline.

**Result:** `PASS` under AT-WD-007.

## AT-PT-028 — Optional feedback unanswered

**Scenario:** every methodology-required scored input is complete, but an optional feedback question is blank.

**Expected:** optional non-scoring feedback does not itself block valid final submission.

**Result:** `PASS` under AT-WD-007 + existing DEC-053 semantics.

## AT-PT-029 — Tie workflow requires additional inputs

**Scenario:** base scored answers trigger an approved methodology tie workflow requiring additional tie-break questions; participant attempts final submission before those required inputs are complete.

**Expected:** no immutable final submission/result yet; attempt remains active for the governed conditional inputs. No provisional result is created and later mutated.

**Result:** `PASS` under AT-WD-007D.

## AT-PT-030 — Approved tie workflow remains unresolved

**Scenario:** all governed tie workflow inputs are complete and the approved methodology still permits an equal/mixed outcome.

**Expected:** final submission may be accepted and the legitimate unresolved/equal result preserved. Platform engineering must not invent a deciding rule.

**Result:** `PASS` under AT-WD-007D.

## AT-PT-031 — Accepted at end of Day 30, result computed later

**Scenario:** authoritative final submission is accepted immediately before the fixed deadline; result persistence finishes after the deadline.

**Expected:** participant does not expire. Answers remain frozen and the platform must finish deterministic result issuance.

**Result:** `PASS` under AT-WD-007B/C.

## AT-PT-032 — Final-submit request arrives after expiry

**Scenario:** participant has a stale browser and sends final submit only after the fixed deadline has become authoritative.

**Expected:** expiry wins; late submission may not resurrect the attempt.

**Result:** `PASS` under AT-WD-007B.

## AT-PT-033 — Scoring process crashes after accepted submission

**Scenario:** submission is durably accepted and answers frozen; scoring process crashes before canonical result persistence.

**Expected:** no reopening, no replacement attempt, no new consumption. Recovery/replay uses the same frozen inputs and converges to exactly one result.

**Result:** `PASS` under AT-WD-007C.

## AT-PT-034 — Duplicate concurrent final submits

**Scenario:** two final-submit requests race for the same active attempt.

**Expected:** at most one authoritative submission commitment exists; duplicate/retry resolves to that same commitment/result and cannot create a second result.

**Result:** `PASS AS REQUIRED INVARIANT`; implementation mechanism deferred.

## AT-PT-035 — Answer save races final submission

**Scenario:** one device saves an answer while another device final-submits the same attempt.

**Expected:** one exact snapshot becomes authoritative. A write authoritative before submission snapshot formation may be included; any write losing to the accepted submission boundary is rejected/stale and may not alter frozen answers.

**Result:** `PASS AT SEMANTIC LEVEL`; exact revision/conflict mechanics remain AT-OI-003.

## AT-PT-036 — Browser timeout after accepted submission

**Scenario:** server accepts final submission but participant sees a timeout and retries.

**Expected:** retry reconciles to the existing frozen submission/canonical result path; it does not reopen editing or create another submission.

**Result:** `PASS` under AT-WD-007A/C.

---

# 3. Open-question queue after v0.3.0

`AT-OI-002` is resolved by `AT-WD-007` and `AT-PT-027...036`, subject to later governed formalisation.

Next unresolved:

- **AT-OI-003 — Active-attempt answer concurrency:** multiple tabs/devices, stale writes, same-question conflicts, autosave and participant intent.
- **AT-OI-004 — Notification policy detail:** exact warning cadence/channel hierarchy and evidence expectations.
- **AT-OI-005 — Subscription replacement abuse/fair-use boundary:** bounded controls without redefining the one-included-completed-assessment promise.

Later passes still include result correction/supersession, reassessment/current-profile semantics, report lifecycle, language/version provenance, identity merge, privacy/retention, Research/Interactive isolation and the Methodology Authority Input Contract.
