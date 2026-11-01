# NewYou Programmes & Learning Pre-JIT Contract Working v0.1.0

- **Status:** FINAL COMPACT WORKING CONTRACT / NON-AUTHORITATIVE
- **Authority:** NONE
- **Implementation authority:** NONE
- **Frozen semantic source:** `deep/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.25.1.md`
- **Acceptance/provenance source:** `deep/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.25.2.md`
- **Broad discovery:** WORKING_FROZEN / HANDOFF-READY
- **Default broad Pass 25:** NO

> This file compresses the accepted frozen Programmes/Learning Pre-JIT. It must not override current Product, Architecture, Domain, Roadmap, Open Work or approved Feature-Pack/JIT authority.

# 1. Reusable semantic centre

The reusable semantic centre is:

```text
Programme
→ ProgrammeVersion
→ Enrolment / attempt

plus explicit:
requirement
progression
completion

with delivery-mode-specific composition
rather than universal LMS machinery
```

`ProgrammeVersion + Enrolment/attempt` is a semantic centre, **not** an exhaustive schema prescription. Stable `Programme` identity and owner-specific source evidence remain explicit.

Within the versioned Programme structure, the governed hierarchy remains:

```text
Programme → ProgrammeVersion → Module → Lesson → Activity
```

A screen, Day/Today composition, delivery grouping or external LMS concept does not silently insert another universal structural layer. `Participation` likewise does not justify a duplicate generic `ProgrammeParticipation` authority beside Enrolment/attempt history.

# 2. Programme and ProgrammeVersion

- `Programme` is the stable conceptual/catalogue identity.
- Programme catalogue lifecycle (`draft → internal → pilot → public → paused → retired`) is distinct from participant lifecycle and must not be mirrored automatically into ProgrammeVersion.
- `ProgrammeVersion` is the version-pinned participant-semantic contract.
- A material approved semantic change requires a successor `ProgrammeVersion`.
- New Enrolments normally use the applicable approved ProgrammeVersion under the concrete Programme/Edition contract; an explicit deliberate pin may override a simple “latest” selection where authorised.
- Active Enrolments do not silently float to the latest ProgrammeVersion.
- Completed and historical participation remains explainable against the version that governed it.
- A non-semantic Content correction does not automatically require a new ProgrammeVersion.
- Current authority does not justify a universal mirrored ProgrammeVersion lifecycle enum.
- SemVer is not business meaning by convenience.
- Programme catalogue lifecycle must not be copied into ProgrammeVersion merely for symmetry.
- A proposed change that may redefine the Programme's fundamental purpose, intended outcome, audience or risk identity is **not** automatically ‘just another ProgrammeVersion’; route the concrete identity question through `PRG-GAP-010` / Product review.

# 3. Enrolment / attempt

`Enrolment` is durable participant-specific Programme attempt/history.

Fixed invariants:

- repeat/restart creates a **new linked Enrolment** rather than destructively reusing history;
- historical attempts remain preserved;
- current access is not Enrolment;
- purchaser is not participant;
- restart does not silently consume a new paid Entitlement;
- duplicate simultaneous same-ProgrammeVersion Enrolments are prohibited unless explicitly authorised;
- active Enrolments stay pinned to their ProgrammeVersion unless governed correction, migration or Safety authority applies;
- migration requires explicit progress mapping;
- correction does not automatically mean lifecycle reopen.

## 3.1 Critical anti-overreach

The Product verbs:

```text
enrol
schedule
begin
pause
resume
complete
abandon
restart
```

are vocabulary and authorised operations. They do **not** prove a universal persisted Enrolment graph.

Compact lifecycle handoff:

| Verb / checkpoint | Frozen safe meaning | Remaining boundary |
|---|---|---|
| `enrol` | Create a distinct, version-pinned durable attempt only when the ProgrammeVersion is approved/selectable and current access/eligibility permits it; duplicate simultaneous same-Version attempts remain prohibited unless explicitly allowed | No universal persisted start-state enum is implied |
| `schedule` | Authorised where the concrete delivery mode uses participant scheduling; Nuwe Jy shared schedule remains Edition/Cohort truth | Exact generic self-paced scheduling checkpoint/from-state is Product/Programme-specific |
| `begin` | Authorised when current access, Safety and applicable prerequisites/Programme guards permit participation | No universal predecessor such as `scheduled` is required for every delivery mode |
| `pause` | Non-punitive; preserves the same attempt/history/progress and does not itself mutate Entitlement, Safety or shared Edition schedule truth | Exact edge legality remains Programme/Product-specific |
| `resume` | Re-evaluates current owner guards and continues the existing attempt where permitted | Exact clock, catch-up, schedule and progression consequences are not universally fixed |
| `complete` / evaluate | Uses the version-pinned approved completion rule and authoritative accepted evidence | Universal terminality and completion-while-paused legality are not authorised generically |
| `abandon` | Records an explicit Programme participation outcome/history without deleting the attempt | Universal terminality and complete-vs-abandon ordering are not authorised generically |
| `restart` | Creates a new linked Enrolment, preserves prior history, re-checks access, and cannot silently consume a new paid Entitlement | Source conditions are not universally limited to `completed`/`abandoned` |
| migration | Requires governed migration plus explicit progress mapping; active Enrolment never silently follows latest | Same-Enrolment vs successor-Enrolment identity is unresolved when a concrete migration needs it |
| correction | Owner-mediated correction/supersession preserves provenance | Correction does not automatically reopen the original Enrolment |
| Edition/Cohort conclusion | Triggers whatever governed evaluation/policy the concrete Programme defines | No generic automatic complete/abandon/terminate/reopen transition exists |

Current generic authority does **not** decide:

- completion terminality;
- abandonment terminality;
- completion while paused;
- a universal resume-before-completion rule;
- completion-vs-abandonment precedence;
- pause-vs-completion precedence;
- generic resume clock/catch-up semantics;
- generic self-paced scheduling checkpoints;
- same-Enrolment vs successor-Enrolment migration identity;
- exhaustive restart source conditions;
- an automatic Enrolment transition when an Edition/Cohort concludes.

When a concrete behaviour depends on one of those unanswered semantics:

```text
NOT AUTHORISED
→ PRODUCT DECISION REQUIRED
```

Technical lock acquisition, optimistic-concurrency order, transaction commit order, job arrival order or queue order must **never** become Product precedence by accident.

## 3.2 Concurrency/retry boundary

Architecture/JIT may prove invariant-safe mechanics, including PostgreSQL uniqueness, atomic mutation, optimistic checks, row locking or transaction isolation where justified.

The semantic requirements are:

- revalidate current authoritative state/guards before protected mutation;
- retries/duplicates do not multiply one logical business effect;
- logical business-command/effect identity remains distinct from worker/provider attempt identity and observation identity;
- stale work cannot blindly overwrite current owner truth;
- technical ordering cannot choose an unresolved participant-semantic winner;
- queue/job uniqueness is not business idempotency;
- provider/worker/PubSub/Analytics arrival order is not business precedence;
- must-not-lose asynchronous consequences use durable recoverable intent and repeat-safe execution where required;
- crash/restart recovery derives work from durable truth/intent, not process memory;
- partial cross-domain success is recovered through owner-mediated retry/reconciliation, not shared-write rollback or a global transaction owner;
- reusing one business-idempotency identity for materially different intent must be rejected/treated as a conflict rather than silently coalesced;
- repair/backfill/reconciliation jobs obey the same owner, idempotency, current-state and provenance invariants as live paths.

# 4. Delivery modes, Edition and Cohort

Approved delivery modes remain distinct:

```text
evergreen_self_paced
scheduled_cohort
facilitated_cohort
```

Product support for a mode does not require implementing all modes now.

Keep these delivery meanings distinct:

```text
visible / discoverable
!= released
!= accessible
!= available to this participant now
!= started / delivered
!= completed
```

Participant-specific availability is a governed decision over the applicable release/schedule rule, explicit prerequisites, current Entitlements access, current Safety/content constraints and any approved exception policy. Do not create one universal stored `available` status or generic unlock/rules engine.

Requirement class and sequencing/prerequisite edge are separate meanings. A recommended ordering is not automatically a hard prerequisite. `required-for-completion` does not automatically block progression; conversely `required-for-progression` is not automatically an additional final-completion criterion merely by its label. `required-for-safety` gates only where the approved Programme/Safety rule says it does. Early prerequisite completion does not bypass a future Edition release boundary. A released item may still be unavailable to a participant because an explicit current gate fails.

`Edition` / `Cohort` is **conditional composition**, not universal Programme structure.

An Edition is a governed delivery configuration over one approved `ProgrammeVersion`. Multiple Editions may reuse the same ProgrammeVersion; once participant-facing commitment/activation occurs, the Edition's source ProgrammeVersion does not silently float to a newer approved version.

Preserve:

- Edition is required for Nuwe Jy;
- Cohort is required for scheduled Nuwe Jy;
- a simple evergreen/self-paced Programme must not manufacture a fake Cohort;
- exact self-paced Edition representation remains JIT/concrete-contract work;
- `evergreen_self_paced` does not universally mean every item is immediately available; availability still follows explicit Programme rules;
- the Nuwe Jy shared schedule belongs to Edition; the participant's current Nuwe Jy day comes from that Edition schedule, not from Enrolment age;
- one Edition may have one or more Cohorts where the delivery contract actually needs them; Cohorts under the same Edition share the Edition schedule rather than creating a second release-calendar authority;
- per-Cohort capacity/facilitator/moderator/support/live allocation may differ where governed without making Cohort the schedule owner;
- ordinary pre-commit configuration change remains distinct from a material post-commit schedule change; the latter is exceptional lifecycle work routed through `PRG-GAP-003` / `PRG-UPD-001` when applicable;
- late enrolment joins the current shared Cohort day with guided catch-up;
- participant pause/recovery does not rewrite the shared Edition schedule;
- Edition/Cohort conclusion does not generically complete, abandon or terminate Enrolments;
- a materially different schedule/timezone normally needs a separate Edition or explicit Product authority;
- `facilitated_cohort` does not by itself authorise facilitator-controlled manual unlock/release; that capability remains YAGNI unless a concrete Programme contract requires it;
- Nuwe Jy Edition activation validates the configured Content/translations, release calendar, live/Safety/facilitation, product/access, Community and Communications readiness that its governed contract requires; that flagship checklist is not automatically a universal activation contract for every Programme.

Do not universalise Nuwe Jy's 60-day rhythm, Today view, daily drip, shared Cohort, Community, Live sessions or flagship operational roles. FP-014's second lens established those as composition, not the reusable Programme core.

# 5. Entitlements and current access

Keep the dimensions independent:

```text
Entitlement / right
!= current access result
!= Enrolment / history
```

Entitlements owns:

- scope and provenance;
- validity;
- expiry;
- revocation;
- current access.

Concrete Programme access may be public, free-account, membership-included/add-on, once-off purchased, bundle-included, sponsored or practitioner-assigned only as the governed Product/Entitlement contract permits. Packaging/funding source does not become Programme participation authority.

Programmes owns:

- participation attempt/history;
- progression;
- Programme completion consequence.

An Entitlement does not itself create an Enrolment, and an Enrolment does not create an Entitlement. Historical Enrolment/progress does not prove current access.

Access loss does not automatically pause, abandon, complete or delete an Enrolment. Access restoration does not automatically resume, restart or create an Enrolment.

Protected actions re-check current authority. Provider/payment observations are evidence to their owning systems; they never become Programme access authority.

Additional fixed boundaries:

- Edition start/completion/catch-up/archive dates are not Entitlement validity dates by default;
- once-off purchase may grant permanent delivered-version access only when the governed offer says so;
- permanent delivered-version access does not automatically include unlimited new Enrolments, future ProgrammeVersions/Editions, facilitated seats or ongoing service;
- restart/re-enrolment coverage must be explicit in the governed right/offer;
- multiple valid grant/payment sources do not multiply Enrolments or Programme attempts;
- purchaser, intended recipient, redeemed participant and Enrolment remain distinct;
- commercial reversal may change current access while historical delivery/participation remains truthful;
- ending membership-only/current-right access does not erase truthful Enrolment/progress history; any continuing historical visibility follows the governed Product/Entitlement promise rather than a Programme-side copy of access state.

The remaining `PRG-GAP-004` work is concrete offer/JIT declaration and enforcement, not a generic Programmes-owned access lifecycle.

# 6. Content, localisation and historical delivery

Owner boundary:

```text
Content & Media
→ content bodies
→ immutable versions
→ locale/translation versions
→ publication/correction/withdrawal

Programmes
→ structural role
→ requirement/progression/completion consequence
```

Historical delivery must be explainable against exact:

```text
ProgrammeVersion
+ ContentVersion
+ locale/version provenance
```

Do not reconstruct history from current/latest Content.

Preserve:

- approved is not synonymous with published/current;
- machine translation is draft only until governed approval;
- Afrikaans and English are symmetric source-language possibilities; there is no universal master language;
- locale branches/translation versions may legitimately advance at different times/version numbers; numeric equality between sibling locale versions is not a correctness invariant;
- interface language, saved preference, selected content language and exact delivered locale/version are distinct;
- required bilingual paid/core/safety-sensitive content fails closed if a required approved locale is unavailable; sibling-locale or machine fallback is not silently substituted;
- optional low-risk public fallback is permitted only where Product explicitly allows/discloses that fallback; it is not a generic escape hatch for required content;
- changing language between approved sibling variants does not by itself create a new ProgrammeVersion, Enrolment or progress history; an active Enrolment need not migrate merely because an approved translation version advances while Programme semantics remain unchanged;
- each translation remains bound to exact source-version provenance and may become stale/review-sensitive when its source changes;
- language review and clinical/Safety/legal approval are separate scoped authorities; translation approval cannot silently substitute for another required approval;
- translation/localisation wording cannot independently change Programme requirement class, qualifying evidence, completion rule, Safety truth or Entitlement promise; a material semantic change must route through the owning Programme/Product authority;
- ordinary translation/content correction does not silently erase prior valid progress/completion; where corrected authoritative truth later undermines an issued outcome, reconcile explicitly and route the post-award consequence through `PRG-GAP-002`;
- Content withdrawal removes delivery authority but does not itself decide the participant's Programme consequence;
- locale-specific titles/slugs/URLs are not durable Programme identity;
- Content correction and Programme semantic/version change are separate owner decisions;
- approved text/translation readiness does not by itself prove linked video/download/media readiness; each governed asset keeps its own Content/media readiness and provenance;
- a Safety-driven correction/withdrawal path may require governed migration/restriction, but ordinary editorial change cannot be relabelled ‘Safety’ to bypass ProgrammeVersion/change governance.

If required Content is withdrawn and no approved replacement/substitution exists, route through `PRG-GAP-011`; JIT must not invent the remedy.

# 7. Activity requirements and evidence

The six intrinsic Programme requirement classes are:

```text
required-for-progression
required-for-completion
required-for-safety
recommended
optional
conditional
```

Do not create extra intrinsic requirement types from:

```text
exempt
substituted
not-applicable
skipped
safety-blocked
```

Those are participant/requirement adjudications or source states, not seventh/eighth intrinsic requirement classes.

Owner rule:

```text
Programmes
→ owns requirement / progression / completion meaning

source Domain
→ owns the authoritative source fact
```

Examples of source ownership:

- HJP owns habits, schedules, occurrences, journals/reflections and its behavioural/progress source truth;
- Events & Live owns occurrence, registration/capacity and attendance/check-in;
- Safety & Eligibility owns Safety/eligibility/restriction authority;
- Content & Media owns delivered Content/version/locale truth;
- Community owns native participation and moderation;
- Temperament owns assessment/result truth;
- Plans owns Plan truth;
- Communications owns message delivery/provider evidence;
- Entitlements owns current access/right truth;
- Health Records, Research, Voting and other Tool/result Domains retain their own durable source truth when a Programme consumes those results.

Programmes may retain only the minimum permitted provenance necessary for its own adjudication. It must not copy private source payloads merely to prove satisfaction.

Programme-native self-attestation is valid only when self-attestation is itself the approved participant meaning and no separately owned durable fact is being impersonated. A single check-in/form may orchestrate several owners; field/business meaning determines authority, not the screen that collected it.

Not every visible Day/Lesson/Activity component requires durable completion evidence. Tracking is justified by an explicit Programme requirement or another governed purpose, not by LMS convention.

If a hard decision depends on source-owner evidence that is temporarily unavailable or ambiguous, defer/refuse/reconcile from the owner rather than fabricate success or failure.

The following are **not generic completion evidence** absent an explicit governed owner contract:

- page view;
- content open;
- video start/watch percentage;
- download;
- provider telemetry;
- Analytics;
- Audit;
- PubSub;
- Facebook interaction.

## 7.1 Exceptions, substitutions and adjudication

Requirement definition and participant-specific adjudication are separate dimensions.

- **Exempt** means an approved requirement is non-blocking/not owed for the scoped context; it does not mean the activity was performed.
- **Substituted** means an explicitly approved alternative satisfies the original requirement while preserving the original requirement and source provenance.
- **Alternate evidence** is a different approved evidence route for the same requirement; it is not automatically a substitution.
- **Not applicable** may result from an explicit conditional predicate; it is not completion. Any conditional requirement that can affect progression/completion/Safety needs an authoritative predicate plus defined evaluation timing/re-evaluation policy and consequence.
- **Skipped**, **missed** and **safety-blocked** do not themselves satisfy a requirement.
- Safety-required exceptions fail closed absent explicit Product/Safety authority.
- Late enrolment, participant pause, Cohort conclusion, completion deadline and Edition archive do not automatically exempt unfinished required work.
- Adjudications are Enrolment/requirement scoped by default and do not silently carry into restart, repeat, migration or a future ProgrammeVersion.
- Human exception commands require explicit authority, guards, reason/provenance, duplicate safety and supersession/correction history. Admin UI is not authority.
- Exceptions/substitutions must never fabricate the underlying source-Domain fact.

Exact Programme-specific exemption/substitution/equivalence mapping remains Product-gated where applicable. Any governed completion/participation metric must explicitly define how exempt, not-applicable and substituted requirements affect its numerator/denominator rather than treating exemption as performance. `PRG-GAP-011` may not be converted into an automatic waiver when required Content has no approved replacement.

# 8. Completion and certificates

- Completion is Programmes-owned for one Enrolment under one ProgrammeVersion.
- Completion is versioned and compassionate.
- There is no universal passed/failed LMS model.
- Completion does not require weight loss, perfect adherence or uninterrupted streaks.
- Optional work does not silently block completion.
- Exact Programme thresholds/outcome mapping remain Product-gated, including `OQ-019` where applicable; any minimum-participation rule must be reproducible from authoritative evidence rather than Analytics telemetry.
- Current Nuwe Jy outcome vocabulary includes `completed`, `completed_with_optional_items_remaining`, `participated`, `partially_completed`, `withdrawn_for_safety` and `abandoned`; these labels do not by themselves establish a universal Enrolment state graph or terminality rule.
- Cohort/day/time boundaries do not automatically manufacture completion or abandonment.
- late enrolment/recovery does not silently invent a private completion standard or lower the approved Programme threshold;
- Repeat Enrolments have independent outcomes.
- Certificates may attest only approved participation/completion.
- Certificates do not certify medical improvement, weight loss, clinical clearance, competency or perfect adherence.
- Completion does not automatically create/refund/revoke an Entitlement, future Edition seat, discount, refund or other commercial right.
- Certificates/recognition are Programme-specific optional outputs where approved, not a universal requirement for every Programme.
- Later ProgrammeVersion retirement, Edition archive or Entitlement expiry does not silently erase a historical completion outcome.

When later corrected authoritative truth undermines an already-issued award/certificate, `PRG-GAP-002` is conditional Product-first. JIT must not invent revoke/reissue/display/notification/review/appeal semantics.

# 9. Compassionate recovery

Recovery preserves:

- the same Enrolment unless restart explicitly occurs;
- accepted progress/evidence/history;
- ordinary delay as non-punitive;
- pre-enrolment backlog for an approved late joiner as catch-up, not participant failure;
- missed/catch-up backlog as derived guidance rather than a new requirement type or durable authority;
- the shared Nuwe Jy Edition calendar — recovery does not create a private shifted 60-day schedule;
- current-authority revalidation on resume/protected action rather than stale pre-pause state;
- Entitlement ownership — recovery cannot mint/extend rights;
- Safety authority — recovery cannot bypass current restriction or turn safety-blocked work into ordinary overdue work;
- explicit exception/substitution authority — recovery consumes approved adjudications but cannot invent them;
- Content authority — recovery cannot repair withdrawn required content by convenience.

Participant-facing recovery guidance should derive the next-smallest useful action from current schedule, prerequisites, Safety, access, Content and accepted evidence. Exact prioritisation is JIT-specific, but ordinary recovery must not dump the entire backlog indiscriminately or convert recommended pacing into participant failure.

Simplification may reduce cognitive/presentation load and deprioritise optional/recommended work, but it may not remove required obligations, lower completion thresholds or fabricate completion. Recovery may reorder participant-facing guidance inside approved policy, but it does not rewrite Edition release dates, source timestamps or Events-owned schedules.

Catch-up is bounded by the governed Edition/Programme completion and catch-up policy. A deadline/window/archive boundary triggers governed evaluation; it does not automatically abandon, fail, reset, exempt or complete an Enrolment. Participant-specific extension beyond the configured policy is not an assumed compassionate default.

Do not create a generic Recovery Domain or recovery state machine.

# 10. HJP and private reflection

Boundary:

```text
HJP
→ habits
→ schedules
→ occurrences
→ journals/reflections
→ behavioural/progress source truth

Programmes
→ requirement/progression/completion consequence
```

Private journal prose/attachments must not be copied into Programmes. Where a private-reflection fact may satisfy a Programme requirement, consume only the minimum lawful source fact/provenance allowed by HJP/Privacy/retention authority.

Participant-created habits, practitioner-assigned habits and Programme-required habits remain distinct truths. Similar labels/schedules do not create automatic equivalence or substitution. HJP occurrence states remain HJP source states: intentional skip is not automatic Programme failure/exemption, `missed` is not automatic Programme failure, and `safety_blocked` is not participant failure.

Programme-relative habit scheduling may consume Programme/Edition timing, but HJP owns habit occurrence windows/timezone reconciliation; it must not create a private shifted Nuwe Jy calendar. Habit pause, Enrolment pause and reminder pause are independent lifecycle dimensions.

A required private reflection must not depend on ordinary staff reading private prose. A reflection UI does not automatically imply full Journal lifecycle semantics. Basic Nuwe Jy reflection/check-in must not force FP-014 private-journal machinery.

Structured health/safety check-ins remain distinct from private journal prose. Free-text journals are not a continuous Safety-monitoring channel, and deferred AI journal assistance must not become invisible scoring, triage or Programme completion authority.

Journal sharing/accountability is scoped access, not mutation authority, professional-review proof or Programme-adjudication authority. Share expiry/revocation ends future access without silently rewriting independent HJP/Programme/professional history.

Journal deletion/anonymisation/retention authority must not be defeated by Programme shadow copies. Where a minimum satisfaction fact may lawfully survive source deletion, that retention contract must be explicit; otherwise the platform accepts reduced later reconstructibility.

`PRG-GAP-007` remains open/conditional-material where private-reflection evidence actually enters scope.

# 11. Live / replay

Events & Live owns occurrence, capacity, registration and attendance/check-in. Programmes may reference a live requirement but does not duplicate Event truth.

Keep separate:

- registration;
- admission/seat;
- attendance;
- Programme satisfaction.

Provider join/leave/watch telemetry is evidence only. Protected join/playback re-checks current access.

Replay is not universally live attendance substitution. Content owns the replay asset/publication/version, Events owns the session/recording association, Entitlements owns current protected playback access, and Programmes owns Programme acceptance. Provider recording existence alone is not governed replay publication. Any approved replay substitute must define the replaced requirement, accepted evidence source, validity window/scope and any non-substitutable live interaction/Safety obligation.

Capacity/waitlist exclusion, organiser cancellation/postponement, provider outage and replay unavailability are not participant non-compliance. If live attendance is completion/progression/Safety critical, activation must provide adequate approved capacity or an explicit governed alternative. Included Programme live sessions do not by themselves justify a separate ticket-commerce engine or full event-marketplace capability.

Late enrolment after a past occurrence, participant pause, or later replay publication does not automatically create failure, exemption or equivalence. Manual attendance correction belongs Events & Live; any Programme exception/substitution remains separately authorised.

Replay correction/withdrawal changes future delivery authority but does not silently erase already accepted historical evidence; a material post-award consequence still routes through `PRG-GAP-002`. Group Q&A remains moderated educational interaction and cannot be turned into required private diagnosis/prescription/treatment; provider chat/comments are not Programme or Community completion evidence by default.

# 12. Community

Community owns native participation/content/moderation. External Facebook is an early governed operating channel, not durable completion authority. Future first-party Community may provide minimum Community-owned participation evidence only where an approved ProgrammeVersion explicitly requires that evidence.

`PRG-GAP-006 = DEFER_YAGNI` unless Product explicitly activates a governed external-evidence route.

Keep Community access/admission, reading/presence, submission, publication, reaction, moderation state and Programme satisfaction distinct. Community membership, views, posts, comments, reactions, provider engagement and moderation dashboards do not become Programme satisfaction by default.

Sensitive health/journal/trauma/plan/weight disclosure must never be made the price of Programme completion.

Community restriction/suspension/ban does not automatically mutate Programme Enrolment/completion. External/provider outage, identity ambiguity or missing Community evidence is not participant non-compliance; a hard dependent decision must defer/reconcile rather than fabricate truth.

Community deletion/anonymisation must not be defeated by Programme shadow copies; retain only minimum lawful provenance needed for an approved Programme consequence.

# 13. Communications

Communications owns message intent/delivery/provider evidence. Programmes owns the originating business context/reason. Content & Media owns approved message/template content version/locale/publication/correction/withdrawal; Privacy & Consent owns purpose-level permission.

```text
delivery / open / click
!= Programme activity
!= Programme completion
!= Programme schedule authority
```

Message failure cannot manufacture participant failure. A message/deep link cannot bypass current Entitlements/Identity/Safety checks.

Privacy/Consent purpose authority, Communications channel/category preferences, quiet hours/caps, reminder pause and Programme Enrolment/pause are separate dimensions. Programmes cannot relabel ordinary reminders as mandatory to bypass those authorities, and restoring a channel preference cannot silently restore withdrawn purpose-level consent. Conversely, opting out of optional reminders does not by implication suppress a separately governed mandatory notice; exact mandatory-message rules remain message-specific authority.

Programme release correctness is independent of notification delivery, PubSub, LiveView or browser refresh. Where a participant notification is a must-not-lose consequence, durable Communications intent/retry/reconciliation belongs to Communications; duplicate/reordered delivery evidence must not multiply Programme effects or rewrite schedule truth. Stale queued messages must revalidate current Programme/Event/Content/Privacy authority rather than outrank a postponement, withdrawal or changed recovery path. Late enrolment/recovery does not imply blanket replay of historical reminders.

Participant communications do not default to a purchaser/sponsor merely because that actor paid. Programme communications minimise sensitive source data and must not copy Health facts, Safety case detail or private journal prose merely for message convenience.

# 14. Safety and professional boundaries

Safety & Eligibility remains authoritative for Safety/eligibility/restriction. Health Records owns health/lifestyle facts; Professional Care owns its actual consented relationship/review/case/outcome; Plans owns Plan truth.

Programmes owns only the approved Programme consequence.

Safety, commercial access, recovery and temperament remain independent authorities. Programme convenience cannot override Safety. Temperament may adapt approved framing/pacing/reminders/reflection prompts, but it does not become clinical Safety, factual health, requirement or professional-restriction authority.

A `required-for-safety` Programme requirement is Programme meaning; it is not itself clinical clearance. Missing safety-critical information fails closed for the affected protected behaviour; it is not participant failure. Core Safety eligibility and the Nuwe Jy participation route remain separate semantic dimensions; exact mapping belongs to Safety/clinical-Product authority.

Nuwe Jy essential Safety screening must not be used as a reason to force deeper personalised-plan/clinical intake before its separate purpose requires it. Safe-modification routing must be governed; facilitator/support improvisation does not create clinical authority.

Safety changes constrain future protected Programme behaviour without silently erasing prior valid history. `safety_blocked` does not automatically become completed, failed, exempt, substituted or abandoned. A restriction affecting personalised/full-challenge behaviour does not automatically remove every otherwise-approved general wellness/education/faith/community component; the current Safety route decides what remains permitted. Later Safety clearance enables future permitted action but does not retroactively satisfy a missed/blocked Programme obligation.

A recommendation for professional review does not itself create a Professional Care relationship/case or prove review occurred. Programme/facilitator/support/admin roles remain non-clinical unless a separately valid role/relationship/purpose grants clinical access.

A combined check-in experience may orchestrate HJP, Health Records, Safety, Professional Care and Programmes, but the UI does not merge their authority. Health-sensitive input that materially affects Safety must route to the proper Health/Safety owner rather than remain only in Programme/facilitator notes. Urgent-help surfaces are bounded pathways, not promises of continuous monitoring or guaranteed professional follow-up.

# 15. Corrections, operator surfaces and provenance

Core rule:

```text
one durable truth
→ one authoritative owner
```

Operator/admin/support/facilitator UI is a projection/orchestration surface, never a shared-write Domain. Read/explain visibility is not mutation authority, and correction workflows use least privilege/minimum evidence for the action.

Correction chain:

```text
source owner corrects its truth
→ Programmes re-evaluates its own consequence
```

not:

```text
support/admin patches both owner records
```

Programmes may correct Programmes-owned truth. It may not directly correct HJP occurrence, Event attendance, Safety override, Entitlement, Content publication/translation, Communications provider evidence, canonical Identity or Commerce payment/refund truth. A generic `mark complete`/operator note cannot fabricate a foreign source fact; operator-attested Programme evidence is valid only when an explicitly governed Programme evidence type authorises it.

Correction preserves original assertion and correction provenance where material. Direct update is appropriate only where the owning Domain's law permits it; history-sensitive truth uses additive/superseding correction rather than silent deletion. Correction/adjudication time is distinct from an earlier effective business time that the owner may establish. Participant dispute starts review/adjudication; it does not itself overwrite authoritative history.

Audit may prove governance/correction evidence but cannot author the underlying business transition.

Historical explanation resolves through durable owner records and exact version/provenance, including the ProgrammeVersion, relevant Edition/Cohort schedule/effective-time context, exact delivered ContentVersion/locale and the governed requirement/completion rule or threshold basis that actually applied. It does not resolve from Analytics, Audit, caches, current Today view, provider dashboards or replaying old side effects.

Historical reproducibility means being able to explain the governed Programme outcome from the durable owner records and materially relevant provenance that lawfully remain. Historical truth and current permission are distinct: a route/access/Safety state may have been valid then while current authority blocks future action now. It does **not** require replaying side effects, retaining every UI/worker/provider observation, archiving executable application versions or introducing event sourcing. Historical reconstruction is side-effect free by default.

The clean LearnDash cutover does not promote legacy LMS internal completion history into native NewYou Programme truth. No generic legacy completion importer is justified by historical reproducibility.

Business occurrence/effective time is distinct from job retry/provider observation/ingestion time. Retry must not rewrite history to “now”.

Lawful deletion, anonymisation or restriction outranks reproducibility. The platform must not resurrect deleted private payloads from Audit, Analytics, caches, backups or shadow Programme copies merely to improve historical explanation.

# 16. Analytics

Analytics is:

```text
DERIVED / REBUILDABLE
```

It never owns:

- Programme lifecycle;
- completion;
- denominator-membership source truth;
- participant evidence.

Preserve prospective/versioned metric definitions, source-authoritative membership, occurrence-vs-ingestion-vs-correction time, governed restatement after source correction and explicit missing-data treatment. Late-arriving analytical evidence follows the frozen occurrence/window/late-evidence policy rather than ingestion time alone. A source correction may cause governed restatement under the same metric definition; that is distinct from changing the definition. Missing analytical data remains unknown unless the frozen metric contract explicitly defines another treatment. Timezone/day-boundary rules are applied only where they materially define a metric, not for symmetry. Analytics must not replicate raw journal/Health/private payloads for segmentation or convenience when minimised governed facts suffice.

Repeat Enrolments remain distinct attempts unless a metric is prospectively defined at person level. Cross-Version or cross-Edition aggregation requires explicit comparability/segmentation where schedule, opportunity or semantics materially differ. Do not shop denominators, exclusions or thresholds post hoc to improve a result; changes to governed definitions are prospective/versioned. Derived progress percentages may exist as labelled projections but cannot write Programme lifecycle state. Analytics outage may degrade freshness/measurement, not unrelated Programme correctness.

Programme-specific thresholds remain Product/OQ-019 work. Research/survey measurement remains separately activated/governed and is not silently created by Programme analytics. Do not duplicate the Analytics Pre-JIT here.

# 17. Nuwe Jy and FP-014 reuse boundary

Nuwe Jy is the first concrete Programme acceptance test, not the generic architecture.

FP-014's second lens demonstrated that reusable primitives must support a wider Programme without forcing:

- 60-day rhythm;
- shared Cohort;
- Today;
- daily drip;
- Community;
- Live;
- Nuwe Jy operational roles.

Conversely, generic versioning, Enrolment history, requirements, progression, completion, recovery, evidence ownership and owner boundaries must not be weakened just because Nuwe Jy uses one concrete composition.

Foundation/FP-014 access is not intrinsically Premium or Membership access; it consumes whatever explicit Entitlement mode its governed contract approves. Foundation also does not make certificates/recognition, Community, Live sessions or every delivery mode universal Programme requirements.

# 18. Committed scheduled-Edition exceptional lifecycle

`PRG-UPD-001` is the sole currently named `PRG-UPD`:

**Committed scheduled Programme Edition exceptional lifecycle contract**

It exists because current Product authority does not yet define organiser-side committed scheduled Edition cancellation/postponement/termination consequences.

Participant Enrolment abandonment, organiser Edition cancellation/termination and participant Safety withdrawal are distinct lifecycle meanings. Event/session cancellation is Events truth and does not equal Edition cancellation. A Safety, Content, Event, provider or force-majeure reason may motivate an organiser decision without transferring Edition lifecycle authority to that source Domain.

Before participant/commercial commitment, ordinary schedule correction may remain governed configuration editing; after commitment, a material postponement/reschedule is an exceptional Product lifecycle decision. Cancellation never means deletion and does not automatically choose refund/credit, access, completion, certificate, transfer or participant-remedy policy.

Its exact scope is maintained in the Upstream Delta Register. This compact contract does not resolve it.

# 19. Authority hard stops and Product-first routing

The **Product-first** stops are:

- `PRG-GAP-002` — corrected authoritative truth undermines an issued award/certificate;
- `PRG-GAP-011` — required Content is withdrawn and no approved replacement/substitution exists;
- `PRG-GAP-003` / `PRG-UPD-001` — committed scheduled Edition exceptional lifecycle;
- lifecycle cells explicitly marked `NOT AUTHORISED / PRODUCT DECISION REQUIRED` in v0.25.1;
- concrete Programme completion/exception policy still owned by Product/OQs where the rule/value is not already governed.

Other fail-closed authority gates are **not automatically Product-first**. For example, `PRG-GAP-007` routes to the applicable HJP + Privacy/Consent + retention/legal authority when private-reflection evidence enters scope. Safety, Entitlements, Content, Events and other source-owner gates remain with their owning authority.

A Feature Pack/JIT may implement an approved consequence. It may not create business meaning merely because a technical owner or convenient default is known.

# 20. Anti-LMS / YAGNI

The frozen Pre-JIT does **not** justify a generic:

- LMS engine;
- page builder;
- programme builder;
- generic quiz builder;
- gradebook;
- SCORM/xAPI layer;
- arbitrary prerequisite graph/rules engine;
- universal watch-time completion rule;
- generic waiver/equivalence engine;
- workflow engine;
- universal transfer engine;
- Cohort merge/split engine;
- global event store;
- global saga or distributed transaction;
- all-delivery-modes implementation;
- LearnDash importer or legacy-completion migration engine;
- Facebook completion-import engine;
- course/instructor marketplace machinery;
- generic points/badges/gamification platform;
- arbitrary multi-tenant authoring engine;
- Recovery Domain;
- generic translation/localisation Domain or locale-specific Programme graph;
- Programme-specific notification/campaign/journey engine or duplicate consent/preference store;
- generic admin-override/correction service detached from owning Domains;
- journal/reflection scoring engine;
- Analytics shadow-authority/KPI engine for Programme lifecycle;
- duplicated Nuwe Jy/Foundation Safety, Plan, habit, journal, Community or Live engine.

Nuwe Jy first and FP-014 second-lens pressure testing are acceptance tests for reusable primitives, not justification for speculative generic infrastructure.

# 21. Freeze / reopen contract

Broad Programmes/Learning Pre-JIT remains:

```text
WORKING_FROZEN / HANDOFF-READY
```

No default broad Pass 25 exists.

Reopen broad discovery only for changed higher authority, a Product resolution/change to a named Product-first seam, a genuine Feature-Pack/JIT upstream contradiction, proof invalidating a material invariant, or explicit human reopening.

Implementation remains:

```text
NOT AUTHORISED
```
