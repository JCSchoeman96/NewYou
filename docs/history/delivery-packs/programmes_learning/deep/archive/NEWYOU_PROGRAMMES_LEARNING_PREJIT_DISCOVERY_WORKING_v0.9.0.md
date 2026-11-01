# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.9.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.9.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 8 — Completion semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.8.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused completion-semantics pass while preserving v0.1.0 through v0.8.0 unchanged.

> This is an append-only semantic successor. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work, approved Feature Pack/JIT contracts or source-Domain truth.

> Nuwe Jy remains the first concrete programme acceptance test. Completion must remain compassionate, participation-based, versioned and explainable. Do not replace NewYou completion law with LMS grades, points, pass marks, streaks, page-view percentages or generic certificate machinery.

---

# 66. Accepted working-lock status entering Pass 8

The user accepted Pass 7 after review.

Therefore Passes 1–7 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, deferred items and later explicit refinements.

Pass 8 inherits without reopening:

- completion meaning and completion/certificate outcome belong to Programmes & Challenges;
- source activity facts retain their source-Domain owners;
- Programmes may record minimum accepted-evidence provenance without copying source payloads;
- ProgrammeVersion is the pinned participant-semantic contract;
- material completion-semantic change requires a successor ProgrammeVersion rather than mutation of an approved/in-use version;
- Enrolment is a durable participant attempt/history and restart/repeat creates a new linked Enrolment;
- scheduled Nuwe Jy uses the Edition calendar, while cohort conclusion and approved individual catch-up may differ;
- current Entitlement/access is separate from completion history;
- exact exemptions/substitutions/equivalence remain Pass 9;
- compassionate recovery/catch-up mechanics remain Pass 10.

---

# 67. Pass 8 — Completion semantics

## 67.1 Scope hard stop

This pass answers only:

1. what completion is authoritative for and what it is not;
2. how completion binds to Enrolment and ProgrammeVersion;
3. which completion criteria families Product Law already authorises;
4. how Nuwe Jy’s Product-defined outcome vocabulary should be interpreted without inventing threshold values;
5. the distinction between completion-required, progression-required, safety-required, recommended and optional work;
6. why elapsed time, Edition conclusion, weight loss, streaks, page views and engagement telemetry cannot manufacture completion;
7. how minimum participation / approved-proportion thresholds are governed;
8. how late enrolment, catch-up windows and completion deadlines interact with completion without creating automatic outcomes;
9. how repeat/restart Enrolments preserve independent outcomes;
10. how completion and certificate truth survive Entitlement expiry, ProgrammeVersion retirement and future editions;
11. how completion evaluation must behave under duplicate/reordered evidence and concurrent reevaluation;
12. what a certificate may attest;
13. what must happen when accepted source evidence is later corrected/reversed/deleted; and
14. how `PRG-GAP-001` and `PRG-GAP-002` should be narrowed before Pass 9.

This pass deliberately does **not** decide:

- the exact Nuwe Jy percentage/minimum participation/final-check-in thresholds — `OQ-019` / `OQ-025`;
- exemption, waiver, substitute, equivalence or alternate-evidence semantics — Pass 9;
- replay substitution for live attendance — Pass 9;
- safety-blocked / not-applicable / intentional-skip substitution consequences — Pass 9;
- detailed pause/resume/catch-up workload shaping or deadline extension policy — Pass 10;
- the exact certificate document template, numbering scheme, QR/verification mechanism or storage representation;
- exact Ash Resources, actions, tables, indexes, jobs or UI components;
- a generic grading, points, credential, badge, SCORM or LMS completion engine.

---

## 67.2 Pass-8 authority evidence

### PRG-EV-079 — Live authority baseline reconfirmed

Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413` and the current README/manifest authority routes remain unchanged from Pass 7.

### PRG-EV-080 — Product Law requires versioned participation-based completion

`DEC-155` is LOCKED:

> Use versioned participation-based completion rules that do not require weight loss, perfect adherence or uninterrupted streaks.

This is the controlling completion doctrine.

### PRG-EV-081 — Generic programme completion criteria are already bounded by Product Law

Product §21F.9 says programme completion uses versioned rules and **may require**:

- all completion-required lessons;
- safety acknowledgements;
- required activities;
- a final check-in; and
- minimum participation where appropriate.

It explicitly says completion never requires weight loss, a specific measurement, perfect adherence or an uninterrupted streak.

### PRG-EV-082 — Activity requirement type remains separate from completion evaluation

`DEC-153` authorises:

- required-for-progression;
- required-for-completion;
- required-for-safety;
- recommended;
- optional; and
- conditional.

Pass 6 already established that requirement type does not silently create every sequencing edge. Pass 8 applies the corresponding completion boundary: not every activity type is automatically completion-blocking.

### PRG-EV-083 — Nuwe Jy has a concrete Product-defined completion criteria family

Product §21H.20 says versioned Nuwe Jy completion criteria may require:

- safety acknowledgements;
- required foundation lessons;
- an approved proportion of required activities;
- milestone check-ins;
- final reflection/check-in; and
- no unresolved completion-blocking requirement.

The exact approved proportion and concrete required-item set remain Product-gated.

### PRG-EV-084 — Nuwe Jy has an explicit Product-defined outcome vocabulary

Product §21H.20 authorises these possible outcomes:

```text
completed
completed_with_optional_items_remaining
participated
partially_completed
withdrawn_for_safety
abandoned
```

Pass 8 must not replace these with a generic LMS `passed/failed` model.

### PRG-EV-085 — Nuwe Jy completion is not automatic at day 60

`DEC-199` is LOCKED:

> Use a 60-calendar-day guided rhythm with catch-up and recovery rather than punitive reset or false automatic completion.

Therefore Edition Day 60 / cohort conclusion is not itself completion evidence or a completion command.

### PRG-EV-086 — Cohort conclusion and individual catch-up may differ

Product Law says:

- missed days do not reset progress;
- participants may recover and catch up;
- required work remains visible;
- the cohort may formally conclude while approved individual catch-up remains open; and
- completion does not require perfect adherence.

Therefore cohort conclusion is not a universal terminal participant outcome.

### PRG-EV-087 — Edition configuration explicitly declares completion/catch-up time boundaries

A ChallengeEdition defines, among other things:

- completion deadline;
- catch-up window; and
- archive date.

These dates are Programme/Edition configuration, not Entitlement validity and not automatic completion outcome selectors.

### PRG-EV-088 — Exact programme thresholds are an existing Product Review gate

`OQ-019 — Programme completion metrics` is `PRODUCT REVIEW` and requires programme-specific minimum participation, final check-ins and completion thresholds before each programme is published.

This is an explicit authority gate, not missing JIT implementation detail.

### PRG-EV-089 — Exact Nuwe Jy completion rules block FP-008 activation

Roadmap FP-008 classifies `OQ-025` as `BLOCKS_THIS_FP`: Nuwe Jy safety routing, milestones and completion rules must be approved before activation.

The Pre-JIT stream must therefore preserve the gap rather than invent threshold numbers.

### PRG-EV-090 — Programmes owns completion/certificate outcome

Current Domain Law §6.8 gives Programmes & Challenges ownership of:

- progression/prerequisite/completion rule configuration; and
- completion/certificate outcome.

Source evidence remains with the source Domain under Pass 7.

### PRG-EV-091 — Certificates are compassionate participation/completion attestations, not health credentials

`DEC-217` is LOCKED:

> Use versioned compassionate completion outcomes and certificates that state participation or completion only.

Current Product also permits private, health-aligned milestone messages, optional badges and completion certificates without weight rankings or shame.

### PRG-EV-092 — Enrolment history and repeat attempts must be preserved

`DEC-152` preserves enrolment attempts, pauses, restarts and completions without deleting progress or silently consuming entitlements.

`DEC-219` preserves repeat-enrolment history.

Therefore completion is attached to a particular durable attempt, not a permanent person-wide “course completed” bit.

### PRG-EV-093 — ProgrammeVersion pinning protects historical completion meaning

Product §21F.10 / `DEC-156` keep active participants on their enrolled ProgrammeVersion unless governed migration/safety correction applies. Material changes create a new ProgrammeVersion and completed history does not change silently.

Therefore the completion rule meaning used for an attempt must remain identifiable after future ProgrammeVersion changes.

### PRG-EV-094 — Pass 7 establishes completion evidence ownership and reconciliation boundaries

Pass 7 working-locked conclusions establish:

- source facts retain one owner;
- Programmes owns evidence acceptance/satisfaction under its rules;
- duplicate/reordered source observations cannot multiply progress;
- source corrections require explicit reconciliation rather than silent history rewrite; and
- completion/certificate correction consequences were intentionally routed to this pass / `PRG-GAP-002`.

---

# 68. Pass-8 semantic model

These are working semantic conclusions, not schema prescriptions.

## 68.1 Completion is an Enrolment-attempt outcome under one ProgrammeVersion

Completion is not a global property of a person or Programme.

The durable business question is:

> What outcome did this Enrolment attempt receive under the completion rules of the ProgrammeVersion that governed it (and the relevant Edition where applicable)?

A later repeat/restart Enrolment has its own completion evaluation and does not inherit a terminal result automatically.

## 68.2 Completion rules are pinned participant semantics

The completion policy used for an Enrolment must be historically identifiable.

For approved/in-use ProgrammeVersions:

- material threshold/required-item changes cannot be silently mutated in place;
- future ProgrammeVersions may use different approved criteria;
- completed history remains explainable against the rule meaning that governed the attempt.

This does **not** require a separate generic `CompletionRuleVersion` resource. ProgrammeVersion is already the primary semantic version boundary unless JIT proves a narrower representation is necessary.

## 68.3 Product defines criteria families; Product review supplies exact values

Current law already defines the kinds of things completion may depend on.

It does **not** authorise developers/JIT to choose:

- the minimum participation percentage;
- the required-activity proportion;
- which exact Nuwe Jy activities/milestones are completion-critical;
- the final check-in requirement/shape; or
- the threshold separating `participated` from `partially_completed`.

Those values/mappings belong `OQ-019` and `OQ-025` before publication/activation.

## 68.4 The Product-defined Nuwe Jy outcomes are not a generic lifecycle enum for every programme

The §21H.20 outcomes are authoritative for Nuwe Jy’s configured completion model.

A later programme should reuse them only where its Product-approved semantics genuinely fit. Do not force every programme into Nuwe Jy labels or invent a generic credential-status state machine.

## 68.5 `completed` means governed completion criteria are satisfied

`completed` is a Programme-owned outcome based on the versioned criteria and accepted evidence.

It does not mean:

- participant lost weight;
- health measurements improved;
- every optional activity was done;
- every day was perfect;
- every released item was opened; or
- sixty calendar days passed.

## 68.6 `completed_with_optional_items_remaining` preserves optionality

Product explicitly authorises this outcome.

It confirms that optional items may remain incomplete without converting a qualifying completion into failure.

Exact programme policy for when to distinguish `completed` from `completed_with_optional_items_remaining` remains part of the approved completion rule, not a developer heuristic.

## 68.7 `participated` and `partially_completed` are valid but their threshold boundary is not yet globally defined

Product authorises both outcomes, but current law does not provide a platform-wide numerical boundary between them.

Do not invent a percentage.

`OQ-019` / `OQ-025` must define any concrete outcome mapping that matters for participant promises, reporting or certificates.

## 68.8 `withdrawn_for_safety` is not failure

Where authoritative Safety policy ends/withdraws participation, Nuwe Jy may record `withdrawn_for_safety`.

The outcome preserves history and must not imply participant fault, failed adherence, or a clinical diagnosis owned by Programmes.

## 68.9 `abandoned` must not be a punitive synonym for ordinary delay

Product has an abandoned Enrolment/outcome concept, but compassionate-recovery law forbids treating an ordinary missed day or temporary pause as failure.

An abandonment transition/outcome requires an explicit governed basis; cohort end or a missed streak cannot silently manufacture it.

## 68.10 Optional/recommended work does not silently block completion

Recommended and optional items remain non-blocking unless a concrete approved rule explicitly gives them another role.

A `required-for-completion` activity may block completion.

A `required-for-progression` activity is not automatically a separate final-completion requirement merely because it once gated sequence; the ProgrammeVersion’s completion rule remains authoritative.

Safety-required work may be completion-blocking where Product/Safety rules declare it so.

## 68.11 Minimum participation must be explicit and evidence-backed

“Minimum participation” cannot be inferred from:

- login days;
- page views;
- video telemetry;
- notification opens;
- time-on-page;
- analytics engagement score; or
- calendar duration.

If Product approves a participation metric, its numerator/denominator and qualifying evidence must be explicit enough to reproduce the completion decision from authoritative sources.

## 68.12 Completion deadline is a rule boundary, not an automatic outcome event

Reaching the completion deadline does not itself mean:

```text
completed
abandoned
partially_completed
```

The Edition’s approved completion policy must define what evaluation/action occurs at or after that boundary.

Catch-up may allow completion after cohort conclusion where the Edition permits it.

Detailed extensions/rescheduling remain Pass 10.

## 68.13 Completion can survive loss of current access

A completed Enrolment remains historical Programme truth if the participant later loses an Entitlement, a membership ends, an Edition archives or a ProgrammeVersion is retired.

Current access and completion history are different authorities.

## 68.14 Repeat/restart does not inherit completion

A new linked Enrolment represents a new attempt.

Prior completion remains historical and does not automatically mark the new attempt complete, consume a new paid right, or exempt future required work unless an explicit Product rule says so.

## 68.15 Completion evaluation must be repeat-safe

Duplicate messages, concurrent source updates or repeated evaluation must not create:

- duplicate authoritative completion outcomes;
- multiple certificates for the same issuance intent;
- multiplied progress; or
- contradictory terminal history.

Exact transactional/materialisation design is JIT.

## 68.16 Certificate authority derives from Programme completion/participation outcome

A certificate is an attestation of the governed Programme outcome; it is not an independent source of completion truth.

If issued, it must remain traceable to the relevant Enrolment, ProgrammeVersion and applicable Edition/outcome provenance.

Exact document/verification representation is JIT.

## 68.17 Certificate wording is strictly bounded

Certificates may state **participation** or **completion** only.

They must not certify:

- weight loss;
- health improvement;
- medical clearance;
- clinical competency;
- perfect adherence;
- streak performance; or
- another outcome owned by a different Domain/profession.

If a participation certificate is offered for a non-completed outcome, its wording must not imply completion.

## 68.18 Post-award evidence correction requires explicit supersession/reconciliation

If accepted source evidence is later corrected, reversed or lawfully deleted:

- the source owner remains authoritative for the source fact;
- the original Programme completion decision/history must not be silently erased or overwritten;
- Programmes must create an explicit correction/reconciliation decision where the change is material;
- before/after provenance and reason must remain explainable subject to retention/privacy law.

What exact corrected outcome applies, and whether an already-issued certificate becomes invalid/superseded, is **not fully governed** and remains `PRG-GAP-002` / Product rule territory.

## 68.19 Completion is not an Entitlement grant or commercial reward by default

Completion may trigger separately governed recognition/benefits only where Product/Entitlements/Commerce explicitly authorise them.

The completion outcome itself does not manufacture future programme access, a future Edition seat, refund, discount, membership or credential privilege.

## 68.20 Analytics derives from completion outcomes; it never decides them

Analytics may calculate completion/dropout/participation metrics from authoritative Programme outcomes and source evidence as governed.

An Analytics threshold/dashboard must not become the hidden completion engine.

---

# 69. Pass-8 focused pressure tests

## PRG-PT-236 — Material completion threshold changes after participants start
**Scenario:** Product wants to change the required completion proportion for an approved/in-use ProgrammeVersion.
**Expected:** Do not mutate active/completed participant semantics in place. Material completion-rule change requires a successor ProgrammeVersion or explicit governed migration/safety path.
**Disposition:** `PASS`.

## PRG-PT-237 — Developer invents an 80% completion threshold
**Scenario:** OQ-019/OQ-025 are unresolved and implementation chooses 80% because it is common in LMS products.
**Expected:** Rejected. Exact proportion is Product authority and blocks publication/FP-008 activation where required.
**Disposition:** `BLOCKED_BY_EXISTING_PRODUCT_GATE`.

## PRG-PT-238 — Day 60 automatically completes every Nuwe Jy participant
**Scenario:** The Edition reaches Day 60.
**Expected:** Rejected by DEC-199. Elapsed schedule is not completion evidence.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-239 — Cohort conclusion automatically marks incomplete participants abandoned
**Scenario:** Shared cohort formally concludes while individual catch-up remains approved.
**Expected:** Rejected. Cohort conclusion is not an automatic participant terminal outcome.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-240 — Weight-loss target required for completion
**Scenario:** Participant must lose 5 kg to complete.
**Expected:** Direct Product-law violation. Completion is participation-based and cannot require weight loss.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-241 — Specific measurement improvement required
**Scenario:** Waist/body-fat/blood-marker improvement is a completion threshold.
**Expected:** Rejected as universal programme completion condition. Product explicitly forbids requiring a specific measurement for completion.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-242 — Perfect adherence required
**Scenario:** Any missed required day makes completion impossible.
**Expected:** Rejected. Product explicitly forbids perfect adherence as completion requirement.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-243 — Uninterrupted streak required
**Scenario:** One missed day resets completion eligibility.
**Expected:** Rejected by DEC-155 / compassionate recovery.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-244 — All configured completion-required lessons satisfied
**Scenario:** Every completion-required lesson is satisfied plus the other approved criteria.
**Expected:** Eligible for the configured completed outcome; evaluation still uses all required criteria, blockers and exact ProgrammeVersion rules.
**Disposition:** `PASS`.

## PRG-PT-245 — Required-for-completion activity is missing
**Scenario:** Participant meets participation percentage but one explicitly completion-required activity remains unsatisfied.
**Expected:** It remains a completion blocker unless an approved exemption/substitution resolves it. Pass 9 owns that resolution.
**Disposition:** `PASS / DEFER_EXCEPTION_TO_PASS_9`.

## PRG-PT-246 — Required-for-progression activity is not separately marked required-for-completion
**Scenario:** Participant previously satisfied enough progression to reach the end, but the historical activity is not a completion requirement.
**Expected:** Do not infer a second final-completion obligation solely from the progression label. Versioned completion rules decide.
**Disposition:** `PASS_WITH_REFINEMENT`.

## PRG-PT-247 — Optional activity remains incomplete
**Scenario:** All approved completion requirements are satisfied; optional activity remains.
**Expected:** Optional work must not convert qualifying completion into failure. Product explicitly permits `completed_with_optional_items_remaining`.
**Disposition:** `PASS`.

## PRG-PT-248 — Recommended activity remains incomplete
**Scenario:** Participant skipped a recommended reflection.
**Expected:** Recommended is not completion-blocking merely by label.
**Disposition:** `PASS`.

## PRG-PT-249 — Conditional activity condition never became true
**Scenario:** Conditional activity was never applicable.
**Expected:** It cannot be silently counted as missing completion work. Exact conditional/not-applicable semantics intersect Pass 9.
**Disposition:** `PASS_WITH_REFINEMENT / DEFER_TO_PASS_9`.

## PRG-PT-250 — Safety acknowledgement required and unresolved
**Scenario:** Other participation criteria are met but an approved safety acknowledgement is missing.
**Expected:** Completion remains blocked where the versioned completion rule makes the safety requirement blocking.
**Disposition:** `PASS`.

## PRG-PT-251 — Safety clearance result is adverse
**Scenario:** Participant has faithfully participated but authoritative Safety requires withdrawal.
**Expected:** Do not turn the safety outcome into personal failure. Product authorises `withdrawn_for_safety`; Safety retains underlying authority.
**Disposition:** `PASS`.

## PRG-PT-252 — Final check-in required but missing
**Scenario:** Activity proportion is satisfied, but the approved final check-in has not occurred.
**Expected:** Completion remains unresolved/blocked if final check-in is required by the governing rule.
**Disposition:** `PASS`.

## PRG-PT-253 — Final check-in completed but health result is not “good”
**Scenario:** Participant completes final check-in; health/weight outcomes did not improve as hoped.
**Expected:** Health outcome cannot become a hidden pass mark. Safety may separately govern restrictions, but participation-based completion remains distinct.
**Disposition:** `PASS`.

## PRG-PT-254 — Milestone check-in required but missing
**Scenario:** One approved milestone check-in is absent.
**Expected:** Treat according to the versioned Nuwe Jy completion rule; JIT may not ignore it or invent a substitute.
**Disposition:** `BLOCKED_BY_OQ019_OQ025_FOR_EXACT_POLICY`.

## PRG-PT-255 — Exact “approved proportion” is unknown
**Scenario:** Product has not supplied the Nuwe Jy required-activity proportion.
**Expected:** FP-008 activation remains blocked; no default percentage.
**Disposition:** `BLOCKED_BY_EXISTING_PRODUCT_GATE`.

## PRG-PT-256 — Minimum participation inferred from login days
**Scenario:** System counts 40 login days as “minimum participation”.
**Expected:** Rejected unless Product explicitly defines login days as qualifying evidence. Telemetry cannot invent completion metrics.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-257 — Minimum participation inferred from page views
**Scenario:** 80% of lesson pages were opened.
**Expected:** Rejected as default completion evidence under Pass 7.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-258 — Minimum participation inferred from video watch percentage
**Scenario:** Analytics reports 90% average watch-through.
**Expected:** Rejected absent explicit Product evidence contract.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-259 — Late enrollee is held to a private 60-day completion clock
**Scenario:** Participant joins Nuwe Jy on cohort Day 12.
**Expected:** Rejected. She remains on the shared Edition schedule with guided catch-up; completion policy must be explicit, not silently transformed into personal-day rules.
**Disposition:** `PASS`.

## PRG-PT-260 — Late enrollee receives an unapproved lower completion threshold
**Scenario:** Implementation halves the required proportion because the participant joined late.
**Expected:** Rejected. Any differentiated completion rule must be Product-approved/versioned; developer sympathy cannot invent policy.
**Disposition:** `BLOCKED_BY_EXISTING_PRODUCT_GATE`.

## PRG-PT-261 — Participant completes during approved catch-up after cohort conclusion
**Scenario:** Cohort formally concludes, catch-up remains open, participant then satisfies all approved criteria before her completion boundary.
**Expected:** Completion remains possible where Edition/Product rules permit; cohort conclusion alone does not prevent it.
**Disposition:** `PASS`.

## PRG-PT-262 — Completion deadline passes while criteria remain unsatisfied
**Scenario:** Deadline is reached.
**Expected:** Do not automatically select `abandoned`, `participated` or `partially_completed` without the approved rule mapping.
**Disposition:** `BLOCKED_BY_OQ019_OQ025_FOR_OUTCOME_MAPPING`.

## PRG-PT-263 — Completion criteria satisfied before the configured deadline
**Scenario:** All required criteria become satisfied early.
**Expected:** Deadline is not a requirement to wait by itself; however Nuwe Jy’s concrete earliest-completion rule and unreleased required work must follow approved Product/Edition configuration. Do not invent early-award behaviour.
**Disposition:** `PASS_WITH_REFINEMENT / JIT_CONSUME_APPROVED_RULE`.

## PRG-PT-264 — Archive date treated as completion cutoff
**Scenario:** Edition archives but completion deadline/access promise differs.
**Expected:** Archive is not automatically the completion rule. Use the explicit Edition completion/catch-up configuration and current access policy.
**Disposition:** `PASS`.

## PRG-PT-265 — Entitlement expires after completion
**Scenario:** Membership-only access ends after a participant completed.
**Expected:** Completion history remains Programmes truth; current protected access may end independently.
**Disposition:** `PASS`.

## PRG-PT-266 — ProgrammeVersion is retired after completion
**Scenario:** Participant completed V1 years ago; V1 is no longer selectable.
**Expected:** Historical completion remains tied to V1 and must not disappear or be relabelled as V2.
**Disposition:** `PASS`.

## PRG-PT-267 — New ProgrammeVersion changes completion rules
**Scenario:** V2 requires different milestone/check-in policy.
**Expected:** Existing V1 completion remains judged/explained under V1; new applicable Enrolments use the approved V2 rule.
**Disposition:** `PASS`.

## PRG-PT-268 — Prior completed Enrolment automatically completes a repeat Enrolment
**Scenario:** Participant joins a future Edition after having completed an earlier one.
**Expected:** Rejected. Repeat/restart is a new linked Enrolment with independent outcome unless explicit Product rule grants credit/exemption (Pass 9).
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-269 — Restart mutates old completion into active state
**Scenario:** Participant restarts after completion.
**Expected:** Rejected. Preserve old completed attempt and create a new linked Enrolment.
**Disposition:** `PASS`.

## PRG-PT-270 — Duplicate completion evaluation
**Scenario:** Same qualifying evidence triggers evaluation twice.
**Expected:** One authoritative outcome; repeat-safe evaluation/issuance.
**Disposition:** `PASS`.

## PRG-PT-271 — Concurrent final evidence arrives
**Scenario:** final check-in and last required activity settle concurrently.
**Expected:** Completion outcome must converge deterministically without duplicate/contradictory terminal records.
**Disposition:** `PASS_WITH_JIT_PROOF`.

## PRG-PT-272 — Duplicate certificate issuance request
**Scenario:** Completion consequence retries after timeout.
**Expected:** Certificate issuance must be idempotent for the same authoritative outcome/issuance intent.
**Disposition:** `PASS_WITH_JIT_PROOF`.

## PRG-PT-273 — Certificate claims weight-loss success
**Scenario:** Certificate text says participant successfully lost weight.
**Expected:** Rejected. DEC-217 permits participation/completion attestation only.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-274 — Certificate claims medical/clinical clearance
**Scenario:** Certificate wording implies medical safety or professional competence.
**Expected:** Rejected; Programmes cannot certify another Domain/profession’s authority.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-275 — Participation certificate implies completion
**Scenario:** `participated` outcome receives a document styled as “Programme Completed”.
**Expected:** Rejected. Any participation certificate must state participation only; exact issuance policy remains Product configuration.
**Disposition:** `PASS_WITH_REFINEMENT`.

## PRG-PT-276 — Certificate exists but completion record is missing
**Scenario:** Support finds a PDF but no authoritative Programme outcome.
**Expected:** The document cannot manufacture completion truth; reconcile from Programmes authority.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-277 — Certificate generation fails after completion
**Scenario:** authoritative completion succeeds but document generation fails.
**Expected:** Completion remains true; certificate delivery/generation may retry independently and must not roll back the completion outcome.
**Disposition:** `PASS_WITH_JIT_PROOF`.

## PRG-PT-278 — `completed_with_optional_items_remaining` is coerced to partial completion
**Scenario:** Optional items are unfinished but all completion requirements are satisfied.
**Expected:** Rejected; Product explicitly recognises a completed outcome with optional work remaining.
**Disposition:** `PASS`.

## PRG-PT-279 — Platform-wide numeric boundary between `participated` and `partially_completed`
**Scenario:** Developer defines 25%/75% thresholds globally.
**Expected:** Not authorised. Outcome mapping is programme-specific Product authority under OQ-019/OQ-025 where it matters.
**Disposition:** `BLOCKED_BY_EXISTING_PRODUCT_GATE`.

## PRG-PT-280 — `abandoned` used after one missed week
**Scenario:** Participant falls behind and is automatically classified abandoned.
**Expected:** Rejected as punitive ordinary-delay treatment. Compassionate recovery applies; abandonment needs explicit governed basis.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-281 — Safety withdrawal rewritten as abandonment
**Scenario:** participant leaves because Safety requires withdrawal.
**Expected:** Preserve `withdrawn_for_safety` rather than misclassifying participant conduct.
**Disposition:** `PASS`.

## PRG-PT-282 — Source evidence corrected after completion
**Scenario:** Events corrects attendance that was previously accepted toward completion.
**Expected:** Source correction is authoritative for source fact; Programmes must explicitly reconcile/supersede its prior decision if material. No silent rewrite.
**Disposition:** `INSUFFICIENT_AUTHORITY_FOR_FINAL_CONSEQUENCE / PRG-GAP-002`.

## PRG-PT-283 — Habit source evidence reversed after certificate issuance
**Scenario:** HJP correction means one accepted occurrence no longer qualifies.
**Expected:** Same explicit reconciliation boundary. Whether completion/certificate remains, is corrected, or is invalidated requires approved correction policy.
**Disposition:** `INSUFFICIENT_AUTHORITY / PRG-GAP-002`.

## PRG-PT-284 — Journal evidence lawfully deleted after completion
**Scenario:** a private reflection had been completion evidence and its source is deleted.
**Expected:** Do not retain forbidden journal payload. Minimum surviving completion provenance remains constrained by PRG-GAP-007/OQ-018; certificate consequence is not invented here.
**Disposition:** `INSUFFICIENT_AUTHORITY / EXISTING_GAPS`.

## PRG-PT-285 — Required content withdrawn with no approved replacement
**Scenario:** completion-critical lesson becomes unavailable.
**Expected:** Do not auto-waive, auto-fail or auto-complete. PRG-GAP-011 remains a completion-blocker consequence requiring Pass 9/OQ-approved resolution.
**Disposition:** `INSUFFICIENT_AUTHORITY / PRG-GAP-011`.

## PRG-PT-286 — Facebook comment counts toward required completion proportion
**Scenario:** external Facebook community activity is used in the completion denominator.
**Expected:** Rejected by Pass 7 unless Product creates an authoritative evidence route. PRG-GAP-006 remains DEFER_YAGNI.
**Disposition:** `PASS_REJECTED_MODEL / EXISTING_GAP`.

## PRG-PT-287 — Source Domain temporarily unavailable during final evaluation
**Scenario:** Events/HJP/Safety source cannot be authoritatively read.
**Expected:** Hard completion evaluation must defer/fail closed rather than substitute Analytics/cache/provider telemetry.
**Disposition:** `PASS`.

## PRG-PT-288 — Analytics completion score determines the Programme outcome
**Scenario:** dashboard computes 82% engagement and marks completed.
**Expected:** Rejected. Analytics derives from authoritative outcome/evidence; it never owns completion.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-289 — Completing programme automatically grants future Edition access
**Scenario:** completion is treated as an Entitlement grant.
**Expected:** Rejected absent explicit Product/Entitlements rule. Completion and access authority remain separate.
**Disposition:** `PASS_REJECTED_MODEL`.

## PRG-PT-290 — Generic grade / pass-mark engine proposed for future-proofing
**Scenario:** implementation adds points, grades, pass marks and certificate levels although Nuwe Jy needs participation-based completion only.
**Expected:** No approved outcome justifies it. Keep bounded completion rules/outcomes only.
**Disposition:** `DEFER_YAGNI`.

---

# 70. Pass-8 gap adjudication

## PRG-GAP-001 — Programme-specific completion thresholds — confirmed and narrowed

**Prior:** `PRODUCT_AUTHORITY_GAP`; framework locked, exact thresholds unresolved; consume `OQ-019` and `OQ-025`.

**Pass-8 finding:** the semantic framework is now substantially resolved. Current Product Law already defines:

- participation-based / versioned completion doctrine;
- permitted criteria families;
- Nuwe Jy’s permitted criteria family;
- Nuwe Jy’s possible outcome vocabulary; and
- certificate claim boundary.

What remains genuinely unresolved is **programme-specific configuration/value authority**, especially:

- exact minimum participation;
- exact approved proportion of required activities;
- exact completion-critical lesson/activity/milestone set;
- final-check-in requirement/details; and
- exact mapping into `completed`, `completed_with_optional_items_remaining`, `participated`, `partially_completed`, `withdrawn_for_safety` and `abandoned` where mapping is not already self-evident.

**Revised status:** `CONFIRMED / FRAMEWORK_RESOLVED / EXACT_VALUES_AND_OUTCOME_MAPPING_PRODUCT_GATED`.

**Gate effect:** `OQ-019` blocks programme publication where these values are needed; `OQ-025` blocks FP-008 Nuwe Jy activation.

**No new PRG-UPD:** existing Product gates already own the decision.

## PRG-GAP-002 — Completion exceptions/corrections — partially resolved; split boundary preserved

Pass 8 resolves the **correction mechanism constraints** far enough to prevent implementation invention:

- source correction never silently rewrites Programme history;
- material correction requires explicit Programme reconciliation/supersession with reason and before/after provenance;
- certificate document state cannot become the authority over the Programme outcome;
- exact corrected outcome / certificate invalidation-or-supersession policy is not yet authorised.

The **exception** half remains deliberately outside this pass:

- exemptions;
- substitutes;
- equivalence;
- safety-blocked/not-applicable treatment;
- alternate live/replay evidence; and
- one source occurrence satisfying multiple requirements.

These move to Pass 9.

**Revised status:** `PARTIALLY_RESOLVED / CORRECTION_PROCESS_BOUNDED / FINAL_CONSEQUENCE_AND_EXCEPTION_POLICY_OPEN`.

**Route:** `OQ-019` / `OQ-025` + Pass 9 + JIT; no generic admin override.

## PRG-GAP-011 — Required content withdrawn/unavailable with no approved replacement — still completion-relevant

Pass 8 confirms this cannot be solved by completion arithmetic.

A completion-critical withdrawn requirement cannot be silently:

- counted complete;
- ignored;
- failed; or
- waived.

It remains an unresolved completion-blocking requirement until Product-approved substitution/exemption/withdrawal policy resolves it. Route to Pass 9 / existing Product gates.

## PRG-GAP-007 — Journal evidence after deletion/correction — completion consequence remains constrained

Pass 8 does not elevate Programme completion convenience above Privacy/HJP deletion law. If private journal evidence is completion-critical, the minimal surviving provenance/certificate-correction consequences remain subject to `OQ-018` and the existing gap.

## PRG-GAP-008 — Programme analytics denominator — no authority change

Authoritative Programme outcome is upstream of Analytics. Exact reporting denominator remains controlled-programme measurement work and must not redefine completion.

## No new Product / Architecture / Domain gap promoted

The dedicated completion pass does not justify a new `PRG-GAP-###` or `PRG-UPD-###`.

The remaining uncertainty is already correctly owned by `OQ-019`, `OQ-025`, existing privacy/content gaps and the dedicated Pass 9 exception/substitution pass.

---

# 71. Pass-8 refinements to earlier working synthesis

## PRG-REF-053 — Completion is Enrolment-attempt truth, not a person-wide programme flag

Every durable completion outcome belongs to a particular Enrolment attempt under its governing ProgrammeVersion and applicable Edition context.

## PRG-REF-054 — ProgrammeVersion is the completion-semantic pin

Do not add a generic completion-rule versioning engine by default. Material completion-rule change is a ProgrammeVersion semantic change unless JIT evidence proves a narrower lawful representation.

## PRG-REF-055 — Completion criteria families are Product-defined; exact values are Product-gated

JIT may implement approved thresholds but may not choose them.

## PRG-REF-056 — Nuwe Jy outcome vocabulary is already Product Law

Use the §21H.20 outcomes; do not introduce LMS `pass/fail` semantics.

## PRG-REF-057 — Outcome mapping between `participated` and `partially_completed` is not globally numeric

No platform-wide percentage may be invented. Mapping is programme-specific where needed.

## PRG-REF-058 — Day 60, cohort conclusion, completion deadline and completion outcome are separate concepts

None of those time boundaries automatically manufactures another.

## PRG-REF-059 — Optional/recommended work remains non-blocking unless explicitly promoted by approved programme rules

`completed_with_optional_items_remaining` confirms optionality has durable semantic meaning.

## PRG-REF-060 — Minimum participation must be reproducible from authoritative evidence

Analytics/page-view/watch-time heuristics do not become completion truth by convenience.

## PRG-REF-061 — Completion survives access/lifecycle changes

Entitlement expiry, ProgrammeVersion retirement, Edition archive or future editions do not erase an authoritative historical completion outcome.

## PRG-REF-062 — Repeat/restart Enrolment receives an independent completion evaluation

Prior completion remains historical; it is not silently inherited by a new attempt.

## PRG-REF-063 — Certificate is an attestation/projection of Programme outcome, not independent authority

Certificate generation/delivery may fail/retry without changing completion truth.

## PRG-REF-064 — Certificate claim scope is participation/completion only

No health, weight, clinical, competency or adherence claim may be smuggled into certification.

## PRG-REF-065 — Post-award correction uses explicit reconciliation/supersession

Never silently mutate/delete the original decision history. Final revocation/invalidation consequence remains Product-gated.

## PRG-REF-066 — Completion does not grant Entitlement/commercial benefit by default

Any post-completion access, discount, future Edition seat or reward requires separate owning-Domain authority.

---

# 72. Pass-8 anti-LMS / YAGNI outcome

Pass 8 explicitly rejects:

- generic pass/fail course grading;
- arbitrary numeric pass marks;
- universal 80%/90% completion defaults;
- points/GPA/gradebooks;
- completion from page views, login days, time-on-page or generic watch percentage;
- streak-based completion;
- weight/measurement outcome requirements;
- automatic completion at day 60;
- automatic abandonment at cohort conclusion/deadline;
- one global `course_completed` bit across repeat Enrolments;
- silently inheriting old completion into a new Enrolment;
- certificate documents as completion authority;
- generic certificate levels/credential framework;
- completion as an automatic Entitlement grant;
- silent certificate revocation after source correction;
- a generic admin “mark completed” bypass;
- a generic completion rule engine beyond the bounded criteria/outcomes actually required by Product.

Generic LMS gradebook/credential/completion machinery remains `DEFER_YAGNI`.

---

# 73. Pass-8 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Completion is a durable Programmes-owned outcome for a specific Enrolment attempt under a specific ProgrammeVersion, not a person-wide programme flag.
2. ProgrammeVersion is the participant-semantic completion pin; material approved/in-use completion-rule changes require successor version/governed migration rather than silent mutation.
3. Product Law already defines the permissible completion criteria families.
4. Product Law already defines Nuwe Jy’s possible completion outcomes: `completed`, `completed_with_optional_items_remaining`, `participated`, `partially_completed`, `withdrawn_for_safety`, `abandoned`.
5. Do not replace those outcomes with generic `passed/failed` LMS semantics.
6. Exact threshold values and concrete Nuwe Jy outcome mapping remain Product-gated under `OQ-019` / `OQ-025` and may not be invented by JIT.
7. `PRG-GAP-001` is narrowed to exact values/outcome mapping, not the completion framework itself.
8. Completion never requires weight loss, a specific measurement, perfect adherence or an uninterrupted streak.
9. Day 60, cohort conclusion, completion deadline and archive date do not automatically create a completion/abandonment outcome.
10. Approved catch-up may permit completion after cohort conclusion where Edition rules allow it.
11. Optional/recommended work does not silently block completion; Product explicitly allows completion with optional items remaining.
12. `required-for-completion` can block completion; `required-for-progression` is not automatically a second final requirement merely by label.
13. Required safety/foundation/milestone/final-check-in requirements block only according to the approved ProgrammeVersion/Product rule; exact Nuwe Jy set remains OQ-gated.
14. Minimum participation must be explicitly defined and reproducible from authoritative evidence; Analytics telemetry cannot invent it.
15. Late enrolment does not create a private 60-day completion standard or an unapproved lower threshold.
16. Historical completion survives later Entitlement expiry, ProgrammeVersion retirement and Edition archive.
17. Repeat/restart Enrolments have independent completion outcomes; prior completion is preserved but not inherited automatically.
18. Completion evaluation and certificate issuance must be duplicate/retry safe.
19. Certificate authority derives from the Programme outcome and may attest participation or completion only.
20. Certificates may not certify weight loss, health improvement, clinical clearance, competency, perfect adherence or another Domain’s truth.
21. Post-award source correction requires explicit Programme reconciliation/supersession; the original decision history is not silently rewritten.
22. Exact corrected outcome / certificate invalidation or supersession consequence remains open under `PRG-GAP-002` / Product rules.
23. Exemptions, substitutes, equivalence, safety-blocked/not-applicable treatment, replay substitution and multi-requirement evidence remain Pass 9.
24. Required-content withdrawal without replacement remains `PRG-GAP-011` and cannot be solved by automatic waiver/failure/completion.
25. Completion does not automatically grant Entitlements, future Edition seats, refunds, discounts or other commercial rights.
26. Analytics consumes authoritative Programme outcomes; it never decides them.
27. No new Domain, `PRG-GAP-###` or `PRG-UPD-###` is justified by Pass 8.
28. Generic LMS grading/credential/completion machinery remains `DEFER_YAGNI`.

**Pass hard stop:** Pass 9 has not started. Required/optional/conditional/exempt/substitute semantics, equivalence, safety-blocked/not-applicable treatment, alternate evidence, replay substitution and exception authority remain deliberately unexamined beyond the minimum boundary statements above.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.
