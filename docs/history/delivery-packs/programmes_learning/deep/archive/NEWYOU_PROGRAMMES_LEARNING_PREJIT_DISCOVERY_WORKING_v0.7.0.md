# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.7.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.7.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 6 — Delivery, availability and sequencing semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.6.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused delivery / availability / sequencing pass while preserving v0.1.0 through v0.6.0 unchanged.

> This is an append-only semantic successor. Read v0.1.0 → v0.2.0 → v0.3.0 → v0.4.0 → v0.5.0 → v0.6.0 → this pass. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work or any owning Domain.

> Nuwe Jy remains the first concrete programme acceptance test. Do not replace NewYou’s approved guided delivery with a speculative generic LMS unlock/prerequisite engine.

---

# 50. Accepted working-lock status entering Pass 6

The user accepted Pass 5 after review.

Therefore Passes 1–5 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, deferred items and future explicit refinements.

Pass 6 inherits, without reopening:

- Programme is stable conceptual/catalogue identity;
- ProgrammeVersion is the version-pinned participant-semantic contract;
- Edition is a governed delivery configuration where required;
- Nuwe Jy Edition owns the shared participant-facing schedule contract;
- Cohorts beneath one Nuwe Jy Edition share that Edition schedule;
- Enrolment is durable participant attempt/history, not access authority;
- Entitlements owns current protected programme access;
- current access loss does not itself pause/abandon/complete an Enrolment;
- exact delivered ContentVersion/locale provenance remains Content/Programme boundary truth;
- restart creates a new linked Enrolment without silently consuming a new paid right;
- Edition archive/completion/catch-up dates are not Entitlement validity dates by default;
- Pass 6 may refine bootstrap `PRG-PT-007`, but must not solve Pass 7 activity evidence, Pass 8 completion, Pass 9 exemptions/substitutions or Pass 10 compassionate recovery policy.

---

# 51. Pass 6 — Delivery, availability and sequencing semantics

## 51.1 Scope hard stop

This pass answers only:

1. what “released”, “visible”, “available”, “accessible”, “started” and “completed” mean at the delivery boundary;
2. how evergreen self-paced, scheduled cohort and facilitated cohort delivery differ semantically without inventing generic LMS machinery;
3. how explicit prerequisites, recommended ordering, milestone gates and safety acknowledgements affect availability;
4. how activity requirement types compose with progression without treating every requirement as an unlock gate;
5. how Nuwe Jy’s Edition schedule determines the shared current day;
6. how late enrolment joins the current day while preserving guided catch-up;
7. how upcoming-item visibility differs from participant access to unreleased content;
8. how schedule authority composes with current Entitlement access and current safety restrictions;
9. how scheduled release behaves under duplicate execution, delay, restart, notification failure and realtime lag;
10. what participant pause/resume may and may not do to a shared Edition schedule;
11. whether facilitated delivery implies facilitator-controlled manual unlocks; and
12. whether the current authority requires any new generic delivery/availability Product rule before FP-008 JIT.

This pass deliberately does **not** decide:

- exact source-Domain evidence contracts for activities — Pass 7;
- completion thresholds, completion adjudication or certificate rules — Pass 8;
- exemptions, substitutions and equivalence — Pass 9;
- detailed compassionate catch-up/recovery planning after misses or pauses — Pass 10;
- exact safety routing/rule values under `OQ-025`;
- exact ContentVersion correction mechanics already bounded by Pass 3;
- exact Communications channels, retry counts, quiet hours or reminder timing under `OQ-017`/`OQ-027`;
- exact Ash Resources, fields, indexes, transactions, Oban jobs, workers, cron expressions or UI components;
- a generic prerequisite DAG/rules engine;
- a facilitator-controlled release feature unless a concrete approved programme requires it.

---

## 51.2 Pass-6 authority evidence

### PRG-EV-048 — Live authority baseline reconfirmed

Live `main` remains:

`086ade7b28c000de1c387acb9760e5eb08bb0413`

Current README and authority manifest continue to route current authority to Product/North Star, Product Law v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and Platform Operating Model v1.0.1.

The Programmes/Learning ledgers remain working/non-authoritative.

### PRG-EV-049 — Product Law defines three delivery modes, not one universal unlock model

`DEC-149` locks:

```text
evergreen_self_paced
scheduled_cohort
facilitated_cohort
```

The generic programme model therefore requires a declared delivery mode but does not require every programme to share one sequencing/release mechanism.

### PRG-EV-050 — Guided progression uses explicit prerequisites and separates hard gates from guidance

Product §21F.5 and `DEC-151` require guided progression with **explicit prerequisites** and recommended pacing without punitive failure for ordinary delay.

Product §21F.5 permits a programme to define:

- required sequential lessons;
- optional lessons;
- recommended ordering;
- milestone gates;
- safety acknowledgements; and
- freely browsable support resources.

Therefore hard availability restrictions must come from explicit governed rules; recommended order alone is not a hidden prerequisite.

### PRG-EV-051 — Requirement type and prerequisite meaning are separate dimensions

`DEC-153` locks activity requirement types:

```text
required-for-progression
required-for-completion
required-for-safety
recommended
optional
conditional
```

These labels do not all mean the same thing.

In particular:

- `required-for-progression` can intentionally gate later progression;
- `required-for-completion` does not automatically mean “block the next lesson”;
- `required-for-safety` may gate progression where safety requires it;
- `recommended` and `optional` are not hard progression gates merely because they appear in sequence;
- `conditional` requires an explicit condition rather than generic inference.

The exact completion consequences remain Pass 8.

### PRG-EV-052 — Ordinary delay does not reset progression

Product §21F.8 and `DEC-154` require compassionate recovery:

- progress is never reset merely because time passed;
- missed work may be identified;
- the next smallest useful action may be recommended;
- unfinished work may be caught up/rescheduled/simplified;
- reminders may be paused; and
- there is no punitive failure state for ordinary delay.

This pass consumes only the availability/sequencing boundary; detailed recovery policy remains Pass 10.

### PRG-EV-053 — Nuwe Jy’s 60 days are an Edition/cohort calendar rhythm, not participant-age sequencing

`DEC-198` makes scheduled cohort the Nuwe Jy flagship mode.

`DEC-199` defines a 60-calendar-day guided rhythm with catch-up/recovery, not punitive reset or false automatic completion.

Pass 4 already resolved that the Edition owns the shared schedule contract and Cohorts beneath the Edition share it.

Therefore “Nuwe Jy Day N” is derived from the Edition’s governed schedule, not from `today - enrolment_created_at`.

### PRG-EV-054 — The participant may see upcoming structure before it is actionable

Product §21H.4 says the participant may:

- resume where she stopped;
- enter guided catch-up;
- view upcoming items;
- view completed history; and
- browse permitted programme structure.

Therefore discoverability/visibility of an upcoming item is distinct from the participant being authorised to open or perform it now.

### PRG-EV-055 — Nuwe Jy daily release is preconfigured, Edition-scheduled and operationally robust

Product §21H.5 and `DEC-201` require:

- all 60 days configured and approved before the Edition begins;
- timezone-aware daily release;
- idempotency;
- observability;
- recovery;
- protection against duplicate release;
- independence from daily administrator action; and
- validation of the full release calendar before activation.

This is a concrete scheduled-delivery contract, not a generic “unlock anything at any time” engine.

### PRG-EV-056 — Late enrolment stays on the shared cohort schedule

Product §21H.15 and `DEC-212` require an allowed late enrollee to:

- join the cohort’s current day;
- receive missed content through guided catch-up;
- not be expected to complete every missed item immediately;
- remain subject to required safety/foundation gates;
- keep daily release tied to the cohort;
- begin notification delivery from enrolment; and
- use explicit completion/catch-up windows.

The platform must not silently create a private 60-day clock for that participant.

### PRG-EV-057 — Edition configuration carries schedule dates/timezone; Cohort does not gain competing schedule authority

Product §21H.14 requires each ChallengeEdition to define, among other items:

- start date;
- all 60 release dates;
- timezone;
- completion deadline;
- catch-up window; and
- archive date.

Combined with Pass 4, multiple Cohorts under one Edition share this schedule contract unless future Product Law explicitly authorises a divergent Cohort schedule.

### PRG-EV-058 — Programmes owns schedule/prerequisite/progression configuration

Current Domain Law §6.8 assigns Programmes & Challenges ownership of:

- programme delivery-mode configuration;
- Edition/Cohort schedule;
- Enrolment lifecycle;
- progression/prerequisite/completion rule configuration; and
- Nuwe Jy Edition/day schedule/configuration.

It does not transfer Content, Entitlement, Safety, Event, Community or habit/journal authority into Programmes.

### PRG-EV-059 — Architecture treats scheduled access as business authority and notifications/realtime as consequences

Current Reference Flow `FLOW-07` traces:

```text
approved edition/version + durable schedule
→ business-effective release rule
→ durable scheduled execution where a transition/consequence is required
→ bounded durable work
→ authoritative programme/content access becomes correct
→ governed notification intent
→ provider delivery
→ PubSub observation
→ LiveView refresh/re-authorises from current authority
```

Its hard invariants include:

- notification delivery is not programme-release authority;
- PubSub echo is not confirmation of release;
- scheduled/retried work is idempotent and cannot duplicate participant consequences; and
- node restart/deployment cannot permanently lose a required release consequence.

### PRG-EV-060 — Architecture explicitly requires scheduled access to remain correct while notification/realtime may lag

`FLOW-07`’s later proof obligation is explicit:

> scheduled access remains correct while notification/realtime may lag; recovery cannot duplicate release effects.

This is crucial for Pass 6: an email, push, worker observation or LiveView refresh must never become the authority for whether a day is released.

### PRG-EV-061 — Durable async execution revalidates current preconditions

Architecture §8.2 defines the must-not-lose consequence pattern as:

```text
authoritative transaction
→ durable execution intent
→ commit
→ durable executor
→ repeat-safe/idempotent handler
→ current preconditions re-read/revalidated
→ success / retry / terminal-visible state
```

Queue uniqueness does not replace business idempotency.

Therefore delayed/retried release consequences must not apply stale configuration blindly.

### PRG-EV-062 — Reminder and notification mechanics already have explicit downstream gates

`OQ-017` owns reminder channels, scheduling, retries, quiet-hour behaviour, observability and rate limits.

`OQ-027`/FP-008 owns concrete Nuwe Jy communications-channel decisions.

Pass 6 therefore does not need to invent notification timing or delivery semantics in order to define release/availability.

---

# 52. Pass-6 semantic model

These are working discovery semantics, not Resource/schema prescriptions.

## 52.1 Keep six delivery concepts separate

For a participant-facing programme item, NewYou must not collapse these concepts:

| Concept | Working meaning |
|---|---|
| **Visible/discoverable** | The participant may know the item/structure exists, including “upcoming”. |
| **Released** | The programme/Edition schedule says the item’s release boundary has been reached. |
| **Accessible** | Current Entitlement/policy allows the protected programme surface/action. |
| **Available** | The participant may act on/open the item now after the applicable schedule, prerequisite, current-access and current safety/content gates are satisfied. |
| **Started/delivered** | Participant-specific interaction/delivery actually occurred. Exact source truth depends on the activity/content boundary. |
| **Completed** | Programme completion/progression evidence has been accepted under governed rules; exact semantics remain Passes 7–9. |

A UI may show an upcoming item while `released == false`.

A released item may still be unavailable to one participant because a required prerequisite or current-access/safety gate fails.

A participant may access/open an item without that fact automatically proving completion.

## 52.2 Availability is a governed decision, not a universal stored status

At the semantic level, “may this participant do this now?” can depend on:

- ProgrammeVersion delivery/progression rules;
- Edition schedule when applicable;
- explicit prerequisites/milestone gates;
- current Entitlement/access;
- current Safety restrictions where applicable;
- current Content publication/withdrawal availability; and
- explicit exception/substitution policy where later approved.

This does **not** require one universal `availability_status` enum or generic rules engine.

Exact action/resource representation remains JIT.

## 52.3 Evergreen self-paced does not automatically mean “everything unlocked”

`evergreen_self_paced` removes the need for a shared cohort calendar, but current Product Law still permits:

- required sequential lessons;
- explicit prerequisites;
- milestone gates;
- freely browsable resources; and
- recommended ordering.

Therefore:

> `evergreen_self_paced != automatically all content available immediately`.

Each ProgrammeVersion declares the bounded progression semantics it actually needs.

Do not build an arbitrary LMS prerequisite graph merely to support the possibility.

## 52.4 Scheduled cohort availability uses the shared Edition calendar

For Nuwe Jy:

- the Edition schedule determines the shared current day;
- release is not based on participant enrolment age;
- one late enrollee does not receive a private shifted schedule;
- pausing one Enrolment cannot pause the Edition clock for everyone;
- multiple Cohorts under the same Edition do not create competing release calendars.

The participant may later use catch-up/recovery, but that does not rewrite the Edition calendar.

## 52.5 Release and prerequisite are independent gates

A scheduled item may be:

```text
released by time
but
not yet available because explicit prerequisite/safety gate fails
```

Conversely, completing prerequisites early does not allow access to a future scheduled day before its Edition release boundary unless Product explicitly authorises early release.

For Nuwe Jy, the safe rule is:

> schedule opens the temporal gate; explicit programme/safety prerequisites may still constrain participant progression.

## 52.6 Requirement type does not automatically create a sequencing edge

Do not infer:

```text
required-for-completion → must complete before next item
recommended → prerequisite
optional → hidden prerequisite
```

Only explicit progression/sequencing rules create those edges.

`required-for-safety` may block progression where the governed safety rule requires it, but Safety remains the source authority for the underlying safety state.

## 52.7 “Upcoming” visibility must not leak protected/unreleased content

Product allows upcoming-item visibility and permitted structure browsing.

Therefore the experience may disclose bounded metadata such as the existence/order/title/status of an upcoming item where approved, while still refusing protected content/body/action access before release/prerequisites/current access allow it.

Exact metadata exposure belongs Content/Frontend/JIT and privacy/access policy.

## 52.8 Scheduled release authority is independent of notification and realtime freshness

Release correctness cannot depend on:

- email delivery;
- push/SMS delivery;
- provider acceptance;
- PubSub receipt;
- LiveView socket state;
- browser refresh;
- a participant opening the Today page.

A notification can be late/duplicated/failed while release remains correct.

An early notification or stale UI cannot unlock an item.

## 52.9 Release execution must recover from duplicate/delayed work without duplicate business effect

Current Product/Architecture already require:

- idempotent scheduled work;
- recoverability;
- no duplicate release consequence;
- current precondition revalidation; and
- terminally visible failure where durable work cannot complete.

The exact choice between directly evaluating the business-effective schedule and materialising a durable transition remains JIT.

Do not create a second release authority merely because a worker exists.

## 52.10 Participant pause does not rewrite a shared schedule

An Enrolment may be paused/resumed under Product Law.

For a scheduled Nuwe Jy Edition:

- the Edition calendar continues independently of one participant’s pause;
- the participant’s prior progress is preserved;
- pause must not silently shift all future Edition dates into a personal calendar.

Exactly what a paused participant may view/do, and how catch-up workload is shaped on resume, belongs the dedicated recovery pass/JIT unless Product law already states it.

## 52.11 Facilitated cohort does not imply manual facilitator unlocking

`facilitated_cohort` is an approved delivery mode, but current authority does not define “facilitator presses unlock” as a universal capability.

Therefore:

- do not infer manual release authority from the word “facilitated”;
- facilitator assignment/support is separate from Edition schedule authority;
- add facilitator-controlled release only when a concrete approved programme outcome requires it.

Disposition: `DEFER_YAGNI`.

## 52.12 Schedule amendments after participant commitment are exceptional

Pass 4 already established that participant-impacting post-commit schedule/timezone changes are exceptional rather than ordinary editing.

Pass 6 reinforces:

- pre-activation schedule changes require full validation;
- post-activation changes must not silently rewrite already-effective release meaning;
- notification queues/projections cannot become authority for the revised schedule;
- exact cancellation/postponement exceptional policy remains `PRG-UPD-001`.

---

# 53. Pass-6 focused pressure tests

## PRG-PT-151 — Delivery mode is declared, not inferred from page shape

**Scenario:** Programme contains the same lesson structure but is configured once as evergreen and once as scheduled cohort.

**Expected invariants / analysis:** Delivery mode is Programme-owned configuration. A UI route/page shape does not infer delivery semantics.

**Disposition:** `PASS`.

---

## PRG-PT-152 — Visible upcoming item is not yet available

**Scenario:** Day 12 appears in an upcoming list on Day 10.

**Expected invariants / analysis:** The participant may see bounded upcoming metadata while protected Day-12 content/actions remain unavailable until release and other gates pass.

**Disposition:** `PASS`.

---

## PRG-PT-153 — Evergreen self-paced is treated as all-at-once by default

**Scenario:** A future evergreen programme has an explicit sequential foundation lesson.

**Expected invariants / analysis:** Self-paced removes the shared cohort clock; it does not erase explicit prerequisites. All-at-once availability is not a universal invariant.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-154 — Recommended order becomes a hard prerequisite

**Scenario:** Lesson B is recommended after Lesson A but no prerequisite is declared.

**Expected invariants / analysis:** B must not be blocked merely because ordering is recommended. Guidance is not authority.

**Disposition:** `PASS`.

---

## PRG-PT-155 — Required sequential lesson gates later progression

**Scenario:** ProgrammeVersion explicitly requires Lesson A before Lesson B.

**Expected invariants / analysis:** Programmes may withhold B until the explicit prerequisite is satisfied. The prerequisite must be versioned programme meaning, not UI convention.

**Disposition:** `PASS`.

---

## PRG-PT-156 — Required-for-completion is treated as required-for-progression

**Scenario:** Activity X is required for completion but no progression gate references it.

**Expected invariants / analysis:** X cannot automatically block the next lesson merely because it matters at final completion. Exact completion treatment is Pass 8.

**Disposition:** `PASS`.

---

## PRG-PT-157 — Required-for-safety gates progression

**Scenario:** A required safety acknowledgement/evaluation has not been satisfied.

**Expected invariants / analysis:** Where the programme’s governed safety rule requires it, progression may fail closed. Programmes does not manufacture the underlying Safety truth.

**Disposition:** `PASS`.

---

## PRG-PT-158 — Optional/recommended activity silently gates next day

**Scenario:** Participant skips an optional reflection.

**Expected invariants / analysis:** Skipping it cannot create a hidden sequencing block absent explicit conditional/progression law.

**Disposition:** `PASS`.

---

## PRG-PT-159 — Conditional activity without an explicit condition

**Scenario:** Programme labels an activity conditional but supplies no governed condition.

**Expected invariants / analysis:** JIT must not invent a condition from user attributes/UI assumptions. Missing governing condition is invalid configuration for that activity.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-160 — Nuwe Jy day is derived from days since Enrolment creation

**Scenario:** Participant enrols on cohort Day 9.

**Expected invariants / analysis:** She joins the shared cohort current day. No private Day-1 clock is created.

**Disposition:** `PASS`.

---

## PRG-PT-161 — Late enrollee must finish Days 1–8 before seeing current Day 9

**Scenario:** Late participant enters on Day 9.

**Expected invariants / analysis:** Product says she joins current day and missed content enters guided catch-up; she is not forced to clear every missed item immediately, except explicit safety/foundation progression gates.

**Disposition:** `PASS`.

---

## PRG-PT-162 — Late enrollee gets all missed items blindly unlocked

**Scenario:** Participant joins on Day 20 but has not satisfied a required foundation/safety gate.

**Expected invariants / analysis:** Past release by calendar does not override an explicit prerequisite/safety gate. Catch-up visibility/availability remains governed.

**Disposition:** `PASS`.

---

## PRG-PT-163 — Early prerequisite completion unlocks future scheduled day

**Scenario:** Participant completes all current prerequisites on Day 5 and asks for Day 6 content before its release date.

**Expected invariants / analysis:** For scheduled Nuwe Jy, temporal release remains Edition-controlled. Prerequisite satisfaction does not override a future release boundary.

**Disposition:** `PASS`.

---

## PRG-PT-164 — Scheduled day released but prerequisite incomplete

**Scenario:** Day 10 release boundary passes but participant has an explicit progression gate outstanding.

**Expected invariants / analysis:** Day 10 can be Edition-released while participant-specific availability remains blocked by the gate. Release and availability are separate.

**Disposition:** `PASS`.

---

## PRG-PT-165 — Access valid but future item unreleased

**Scenario:** Participant has permanent/current programme access and opens Day 40 on Day 12.

**Expected invariants / analysis:** Entitlement permits the programme surface but does not override Edition sequencing. Protected future item remains unavailable.

**Disposition:** `PASS`.

---

## PRG-PT-166 — Item released but Entitlement access revoked

**Scenario:** Day 12 is released, but participant’s only qualifying entitlement is revoked.

**Expected invariants / analysis:** Protected access fails closed. Release state does not manufacture entitlement.

**Disposition:** `PASS`.

---

## PRG-PT-167 — Item released but source content withdrawn

**Scenario:** Schedule says Day 12 is released but the referenced governed ContentVersion is withdrawn.

**Expected invariants / analysis:** Schedule cannot override Content authority. Delivery fails/withholds safely; programme consequence remains bounded by Pass-3 `PRG-GAP-011`.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-168 — Notification email is delayed

**Scenario:** Day 8 becomes business-effective, but the reminder email is delivered two hours late.

**Expected invariants / analysis:** Day 8 access remains correct independently. Notification lag is not release lag.

**Disposition:** `PASS`.

---

## PRG-PT-169 — Notification arrives early

**Scenario:** A provider/queue bug sends tomorrow’s reminder before the release boundary.

**Expected invariants / analysis:** The message cannot unlock future content. Current Programmes authority still denies unreleased content.

**Disposition:** `PASS`.

---

## PRG-PT-170 — PubSub event is missed

**Scenario:** Release consequence is authoritative, but one connected LiveView misses the PubSub message.

**Expected invariants / analysis:** Reconnection/refresh re-reads current authority; PubSub loss affects freshness, not truth.

**Disposition:** `PASS`.

---

## PRG-PT-171 — Duplicate release execution

**Scenario:** The same scheduled release work executes twice after retry/restart.

**Expected invariants / analysis:** Business effect remains one release; duplicate work cannot duplicate programme consequence. Notification dedupe belongs Communications.

**Disposition:** `PASS`.

---

## PRG-PT-172 — Node restarts at release boundary

**Scenario:** The application restarts while Day 15 release work is due.

**Expected invariants / analysis:** Durable schedule/intent and recovery must restore correct access; process memory cannot be required for release correctness.

**Disposition:** `PASS`.

---

## PRG-PT-173 — Scheduled work is delayed beyond release boundary

**Scenario:** Worker backlog delays a consequence after the business-effective release time.

**Expected invariants / analysis:** Scheduled access must still converge to the correct business-effective state and recovery must be visible/repeat-safe. Exact materialisation strategy is JIT/proof.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-174 — Participant is offline across several releases

**Scenario:** Participant returns after five days offline.

**Expected invariants / analysis:** Current authority reflects the Edition schedule and participant-specific gates; browser history/socket absence cannot freeze the programme clock.

**Disposition:** `PASS`.

---

## PRG-PT-175 — Participant refreshes repeatedly around a release boundary

**Scenario:** Multiple concurrent requests arrive near the same boundary.

**Expected invariants / analysis:** Availability/release evaluation must be deterministic from authoritative state and duplicate-safe; refresh count cannot create multiple releases.

**Disposition:** `PASS`.

---

## PRG-PT-176 — Edition timezone differs from participant device timezone

**Scenario:** Participant device/browser is in another timezone.

**Expected invariants / analysis:** Edition schedule timezone remains the release authority. Device timezone cannot shift the shared cohort day.

**Disposition:** `PASS`.

---

## PRG-PT-177 — Operator changes Edition timezone after activation

**Scenario:** An operator tries to change timezone mid-run to move future day boundaries.

**Expected invariants / analysis:** Pass 4 already treats participant-impacting schedule/timezone change as exceptional. It cannot be an ordinary edit; existing history must remain explainable.

**Disposition:** `PASS`.

---

## PRG-PT-178 — Participant changes interface/content language

**Scenario:** Participant switches Afrikaans ↔ English on Day 22.

**Expected invariants / analysis:** Language choice may change delivered locale/version under Pass-3 rules; it does not change Edition day/release schedule.

**Disposition:** `PASS`.

---

## PRG-PT-179 — One participant pauses Enrolment

**Scenario:** Participant pauses for a week in a scheduled cohort.

**Expected invariants / analysis:** Her pause cannot pause the Edition clock or other participants. Exact paused-participant interaction/catch-up treatment is deferred to Pass 10.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-180 — Resume shifts participant to a private calendar

**Scenario:** Paused participant resumes and the system shifts future releases by seven days for her only.

**Expected invariants / analysis:** Rejected for Nuwe Jy scheduled cohort. Resume/catch-up must preserve the shared Edition schedule unless Product explicitly creates another delivery mode.

**Disposition:** `PASS`.

---

## PRG-PT-181 — Cohort A and Cohort B under one Edition release different days

**Scenario:** Parallel Cohorts under one Edition are configured with different release calendars.

**Expected invariants / analysis:** Pass 4 rejected competing per-Cohort calendars under one Edition. Materially divergent schedule requires another Edition or explicit Product amendment.

**Disposition:** `PASS`.

---

## PRG-PT-182 — Facilitated cohort implies facilitator manual unlock

**Scenario:** A facilitator wants to release tomorrow’s lesson early.

**Expected invariants / analysis:** Current authority does not make facilitation a release-authority override. Manual unlock is not admitted without concrete Product law.

**Disposition:** `DEFER_YAGNI`.

---

## PRG-PT-183 — Daily admin action is required to publish each Nuwe Jy day

**Scenario:** Operator must press Publish every morning.

**Expected invariants / analysis:** Directly contradicts Product: all 60 days are preconfigured and release is independent of daily administrator action.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-184 — Today page load performs the release

**Scenario:** The first participant opening Today causes the day to unlock.

**Expected invariants / analysis:** UI/browser access cannot be release authority. Release correctness must exist independently of page load.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-185 — Upcoming structure exposes full protected content body

**Scenario:** Future lesson is visible as upcoming and full body/media URL is served to the browser but hidden with CSS.

**Expected invariants / analysis:** Visibility does not authorise protected content delivery. Bounded metadata and protected body/action access must remain distinct.

**Disposition:** `PASS`.

---

## PRG-PT-186 — Freely browsable support resource is forced into sequence

**Scenario:** ProgrammeVersion explicitly marks a support resource freely browsable.

**Expected invariants / analysis:** The resource must not inherit a hidden sequential prerequisite merely because it sits under a module/lesson hierarchy.

**Disposition:** `PASS`.

---

## PRG-PT-187 — Programme hierarchy order is treated as prerequisite graph

**Scenario:** Lesson 3 follows Lesson 2 structurally, but no sequential rule is declared.

**Expected invariants / analysis:** Structural ordering alone cannot silently become a hard prerequisite. Explicit progression rule is required.

**Disposition:** `PASS`.

---

## PRG-PT-188 — Edition release is treated as completion evidence

**Scenario:** Day 60 release occurs for the cohort.

**Expected invariants / analysis:** Release proves only temporal availability state; it does not prove participant viewing, activity evidence or completion.

**Disposition:** `PASS`.

---

## PRG-PT-189 — Edition concludes while catch-up is open

**Scenario:** Shared cohort formally concludes but approved individual catch-up remains open.

**Expected invariants / analysis:** Conclusion does not retract already-released work by itself and does not auto-complete participants. Exact recovery/completion treatment remains later passes.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-190 — Archive date is treated as automatic content lock

**Scenario:** Edition reaches archive date while a participant has a separately valid entitlement/catch-up promise.

**Expected invariants / analysis:** Archive is Programmes lifecycle/config truth, not automatically Entitlement expiry. Concrete offer/Edition access promise governs; Pass 5 boundary remains.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

# 54. Pass-6 gap adjudication

## Bootstrap PRG-PT-007 — Sequencing and release modes — refined by Pass 6

The bootstrap conclusion remains valid and is now made precise:

- NewYou needs **bounded delivery/availability semantics**, not one universal unlock engine;
- delivery mode is explicit configuration;
- evergreen does not imply all-at-once;
- scheduled Nuwe Jy uses the Edition calendar;
- explicit prerequisites are separate from recommended ordering;
- requirement type is separate from sequencing edge;
- notifications/realtime do not determine release;
- facilitator-controlled manual release is not currently justified.

**Revised status:** `RESOLVED_ENOUGH_FOR_FP008_JIT / NO_NEW_UPSTREAM_DELTA`.

## No new Product / Architecture / Domain gap promoted

This dedicated pass did **not** justify a new `PRG-GAP-###` or `PRG-UPD-###`.

Reasons:

1. FP-008’s concrete scheduled-delivery semantics are sufficiently governed by Product §21H, `DEC-198...DEC-212`, Domain Law and `FLOW-07`.
2. Generic evergreen/facilitated variants may declare only the bounded progression rules a concrete future programme actually needs.
3. Unknown exact worker/resource/job representation is JIT/proof detail, not missing Product Law.
4. Reminder timing/channel mechanics are already routed to `OQ-017`/`OQ-027`.
5. Paused-participant recovery workload and catch-up shaping are intentionally deferred to Pass 10.
6. Required-content withdrawal consequences remain the already-recorded `PRG-GAP-011`.
7. Post-commit Edition cancellation/postponement remains `PRG-GAP-003` / `PRG-UPD-001`.

### Daily release clock-time clarification

Current Product Law defines **release dates + Edition timezone**, not an additional universal clock-time policy.

This pass therefore does not invent a new platform-wide `release_at HH:MM` rule.

For FP-008 JIT, the Edition schedule must be interpreted consistently as a business-effective local-calendar rule from the governed configuration. If Product/operations wants a non-calendar-boundary release hour (for example 05:00 local), that becomes explicit Edition Product/operations configuration before activation rather than a developer convention.

This clarification does not justify a new gap identifier because the existing law already defines date/timezone schedule authority and the concrete Edition must be fully configured/validated before activation.

---

# 55. Pass-6 refinements to earlier working synthesis

## PRG-REF-028 — Released, visible, accessible, available, started and completed are separate meanings

Do not use one `unlocked/completed` flag to carry all delivery semantics.

An upcoming item can be visible without being released. A released item can be unavailable to a participant because a prerequisite/current-access/safety gate fails. Opening an item does not itself prove completion.

## PRG-REF-029 — Evergreen self-paced does not mean all-at-once

Evergreen removes shared cohort timing. It does not erase explicit prerequisites, milestone gates or sequential lessons.

A future programme may choose broad immediate browsing, but that is concrete programme configuration rather than a universal law.

## PRG-REF-030 — Requirement type does not imply sequencing edge

`required-for-completion`, `recommended`, `optional` and `conditional` must not silently become progression prerequisites.

Only explicit progression rules create hard sequencing edges.

## PRG-REF-031 — Nuwe Jy schedule opens the temporal gate; participant-specific gates still apply

Edition release and participant availability are distinct.

For scheduled Nuwe Jy:

- Edition schedule controls temporal release;
- explicit prerequisite/safety rules may still block progression;
- current Entitlement access still applies;
- Content withdrawal still applies.

## PRG-REF-032 — Upcoming visibility is not protected content delivery

Product may show upcoming items and permitted structure without exposing unreleased protected bodies/actions.

Frontend hiding cannot substitute for server-side availability/access authority.

## PRG-REF-033 — Notification/PubSub/LiveView are never release authority

Messages and realtime events are consequences/freshness mechanisms.

They may lag, duplicate or fail while scheduled access remains correct.

## PRG-REF-034 — Scheduled release is Edition-level, not one durable participant release per Enrolment by default

Current semantics require one shared Edition schedule for Nuwe Jy.

Do not infer a separate participant-relative release clock or per-Enrolment schedule merely because participant projections may need individual availability decisions.

Exact persistence/materialisation remains JIT.

## PRG-REF-035 — Pausing Enrolment does not pause a scheduled Edition clock

An individual pause does not rewrite Edition dates or other participants’ shared current day.

The participant’s recovery/catch-up interaction after pause remains Pass 10.

## PRG-REF-036 — Facilitated delivery does not imply facilitator unlock authority

Facilitation can mean support/accountability/shared delivery context without creating a new manual-release power.

Manual facilitator-controlled unlocking remains `DEFER_YAGNI` until a concrete approved programme requires it.

## PRG-REF-037 — Structural ordering is not automatically a prerequisite graph

Module/Lesson/Activity hierarchy and ordering may support navigation/recommended sequence.

Hard progression edges must be explicit; the platform must not infer them solely from adjacency.

## PRG-REF-038 — Release correctness must survive execution/freshness failure

Duplicate or delayed scheduler/worker execution, lost PubSub and stale LiveView state must not redefine the business-effective release outcome.

Recovery re-reads current authority and must remain repeat-safe.

---

# 56. Pass-6 anti-LMS / YAGNI outcome

Pass 6 explicitly rejects:

- one universal `unlocked` status combining schedule/access/prerequisite/completion;
- a generic arbitrary prerequisite DAG/rules engine;
- making every structural lesson edge a hard prerequisite;
- treating recommended order as a hard gate;
- treating `required-for-completion` as automatically `required-for-progression`;
- all-content-immediately-open as a universal evergreen rule;
- per-participant personal clocks for scheduled Nuwe Jy;
- per-Cohort competing calendars under one Edition;
- facilitator manual unlock authority without a concrete approved requirement;
- daily administrator publishing as the Nuwe Jy release mechanism;
- page-load-triggered release;
- notification delivery as release authority;
- PubSub/LiveView/cache as release authority;
- CSS-only hiding of protected unreleased content;
- participant-specific durable release rows solely because an LMS normally models them;
- a general course-prerequisite/term/section engine beyond evidence-backed NewYou needs.

Generic LMS sequencing/unlock machinery remains `DEFER_YAGNI`.

---

# 57. Pass-6 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Delivery mode is explicit Programme/Edition configuration; it is not inferred from UI structure.
2. Visible/discoverable, released, accessible, available, started/delivered and completed are separate concepts.
3. Current participant availability is a governed decision over the applicable schedule, explicit prerequisites, current access, current safety/content constraints and later approved exception policy.
4. NewYou does not need one universal stored availability status or generic unlock/rules engine.
5. Evergreen self-paced does not universally mean every item is immediately available.
6. Hard progression gates must be explicit; recommended ordering is not a prerequisite.
7. Activity requirement type and sequencing edge are separate meanings.
8. `required-for-completion` does not automatically block progression; exact completion semantics remain Pass 8.
9. `required-for-safety` may gate progression where governed safety rules require it; Safety remains source authority.
10. Nuwe Jy’s shared current day comes from the Edition schedule, not Enrolment age.
11. Late enrolment joins the cohort current day; missed work enters guided catch-up without a private 60-day schedule.
12. Completing prerequisites early does not unlock a future scheduled Nuwe Jy day before its Edition release boundary.
13. A day may be Edition-released while participant-specific availability remains blocked by an explicit prerequisite/access/safety/content gate.
14. Upcoming-item visibility/permitted structure browsing does not authorise delivery of protected unreleased content.
15. Daily release correctness is independent of notification, provider delivery, PubSub, LiveView and browser refresh.
16. Scheduled/retried release work is idempotent/recoverable and revalidates current authority; duplicate execution cannot duplicate business effects.
17. Participant pause/resume does not rewrite the shared Edition schedule; detailed recovery remains Pass 10.
18. Multiple Cohorts under one Edition share its schedule; materially divergent schedule/timezone requires another Edition or explicit Product amendment.
19. Facilitated cohort does not currently justify facilitator-controlled manual unlock; that capability is `DEFER_YAGNI`.
20. `PRG-PT-007` is refined/resolved enough for FP-008 JIT; no new Domain, `PRG-GAP-###` or `PRG-UPD-###` is justified by Pass 6.

**Pass hard stop:** Pass 7 has not started. Activity ownership/evidence contracts across Content, Habits/Journals/Progress, Events, Community, Safety and other Domains remain deliberately unexamined beyond the minimum authority references required to decide availability/prerequisite semantics.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.
