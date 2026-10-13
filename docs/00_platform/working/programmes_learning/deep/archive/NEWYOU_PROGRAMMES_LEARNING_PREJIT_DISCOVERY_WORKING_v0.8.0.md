# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.8.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.8.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 7 — Activity ownership / evidence across Domains
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.7.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused cross-Domain activity-evidence pass while preserving v0.1.0 through v0.7.0 unchanged.

> This is an append-only semantic successor. Read v0.1.0 → v0.2.0 → v0.3.0 → v0.4.0 → v0.5.0 → v0.6.0 → v0.7.0 → this pass. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work or any source Domain.

> Nuwe Jy remains the first concrete programme acceptance test. Do not solve cross-Domain evidence by creating a generic LMS completion/event store, by copying private source payloads into Programmes, or by treating Analytics/Audit/provider telemetry as source business truth.

---

# 58. Accepted working-lock status entering Pass 7

The user accepted Pass 6 after review.

Therefore Passes 1–6 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, deferred items and future explicit refinements.

Pass 7 inherits, without reopening:

- Programme owns activity structure/requirement/progression/completion meaning, not every underlying activity fact;
- Content & Media owns content bodies/versions/publication/withdrawal and exact delivered content provenance must remain explainable;
- Habits, Journals & Progress owns habit occurrences, private journals, behavioural/adherence/progress entries and qualifying lightweight programme check-in responses;
- Events & Live owns live/event registration and attendance/check-in truth;
- Community owns first-party community participation/moderation truth; external Facebook is not permanent platform authority;
- Safety & Eligibility owns safety/eligibility outcomes and restrictions;
- Entitlements owns current protected access;
- Analytics is derived and Audit & Evidence records governance/security evidence without becoming source-domain truth;
- visible/released/accessible/available/started/completed are distinct;
- exact completion thresholds/adjudication are reserved for Pass 8;
- exemptions/substitutions/equivalence are reserved for Pass 9;
- detailed recovery/catch-up is reserved for Pass 10.

---

# 59. Pass 7 — Activity ownership / evidence across Domains

## 59.1 Scope hard stop

This pass answers only:

1. which Domain owns the underlying fact for each major programme activity family;
2. what Programmes owns when an activity definition requires evidence from another Domain;
3. whether Programmes may retain a minimal accepted-evidence reference/provenance record without copying the source payload;
4. how programme-native self-attestation differs from a habit/progress/journal record;
5. why a content open/page-view/video-progress/download click is not automatically programme completion evidence;
6. how Nuwe Jy lightweight check-ins and deeper milestone check-ins can cross Domain boundaries without becoming one shared-write record;
7. how live attendance, replay use and Community participation evidence are treated;
8. why provider telemetry, Analytics events, Audit logs, PubSub and caches cannot silently become source authority;
9. how duplicate/reordered source observations and temporary source unavailability affect programme evidence consumption;
10. how later source correction/deletion must be reconciled without silently rewriting programme history;
11. how journal deletion/privacy constrains evidence retention;
12. whether facilitators/operators may manufacture source evidence; and
13. whether any new generic activity-evidence Product/Domain abstraction is required before FP-008 JIT.

This pass deliberately does **not** decide:

- programme-specific completion thresholds, minimum participation or final completion adjudication — Pass 8 / `OQ-019` / `OQ-025`;
- whether one activity may be exempted, substituted or satisfied by an alternate activity — Pass 9;
- replay-as-substitute policy — Pass 9;
- compassionate catch-up/recovery workloads — Pass 10;
- exact journal-retention/deletion implementation — `OQ-018` / later HJP+Privacy JIT;
- exact native Community evidence schema or external Facebook import/reconciliation machinery;
- exact Event provider attendance reconciliation implementation;
- exact Programme evidence Resources/tables/polymorphic references/event messages;
- a generic quiz/gradebook/watch-time/xAPI evidence model;
- a generic facilitator/admin “mark anything complete” power.

---

## 59.2 Pass-7 authority evidence

### PRG-EV-063 — Live authority baseline reconfirmed

Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413`.

README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` continue to route the same current Product, Decision, Architecture, Domain, Roadmap and Operating authority used by the preceding passes.

The Programmes/Learning ledgers remain working/non-authoritative.

### PRG-EV-064 — Programme activity meaning belongs to Programmes

Product §21F.7 and `DEC-153` require every activity to have an explicit requirement type:

```text
required_for_progression
required_for_completion
required_for_safety
recommended
optional
conditional
```

Current Domain Law gives Programmes & Challenges ownership of programme definitions/versions/modules/lessons/activity structure references plus progression/prerequisite/completion rule configuration and completion outcome.

This establishes Programme-owned **activity meaning**, but not universal ownership of the underlying source fact.

### PRG-EV-065 — Domain Law explicitly prevents Programmes from owning several source facts

Programmes & Challenges explicitly does **not** own:

- lesson/content body versions;
- participant journal/habit occurrence truth;
- commercial entitlement/payment;
- community posts/moderation;
- live-session registration/tickets; or
- central plan/safety engines.

Therefore an ActivityDefinition referencing one of these facts does not move that fact into Programmes.

### PRG-EV-066 — Cross-Domain references do not transfer authority

Domain Law states:

- every major durable truth has one authoritative owner;
- a relationship/reference does not transfer mutation authority;
- cross-domain writes invoke the owner;
- derived projections/Analytics/PubSub/provider state never become hidden authority; and
- a dependent may hold a reference, immutable snapshot/provenance or rebuildable projection only where Product/Architecture permits.

A single UI form/check-in also does not imply one Domain owns every submitted fact.

### PRG-EV-067 — HJP owns habit, journal and behavioural-progress source truth

Habits, Journals & Progress owns:

- habit schedules and occurrence states;
- private journal entries and sharing state;
- behavioural/adherence/progress entries;
- lightweight programme check-in responses not owned as health facts; and
- qualifying self-tracking/reflective Interactive Tool results.

`DEC-160` gives habit occurrences explicit states including `completed`, `partial`, `intentional skip`, `missed`, `not applicable` and `safety blocked`.

Programmes may consume these facts but does not become their source owner.

### PRG-EV-068 — Journals are private and strongly deletion-sensitive

`DEC-165` keeps journals private by default.

`DEC-227` and Product §21I.9 require strong deletion treatment for eligible private journal content, attachments, indexes/caches and future AI-derived artefacts, and journal text is excluded from Analytics.

Therefore copying journal text into Programmes to prove participation would directly undermine the privacy/deletion model.

### PRG-EV-069 — Events & Live owns attendance/check-in

Domain Law assigns Events & Live ownership of live/event occurrences, registration/capacity/tickets and attendance/check-in truth.

`DEC-206` links Nuwe Jy sessions, registration, attendance and governed replays to the Edition/Cohort without moving attendance authority to Programmes.

Provider dashboards/streaming platforms remain external evidence, not the final attendance owner.

### PRG-EV-070 — Community owns native participation; Facebook is not permanent authority

Community owns first-party group/space participation and moderation truth when native Community is active.

Domain Law explicitly says external Facebook remains a launch channel, not permanent source of truth, and is not authoritative participant entitlement/moderation history for the future native platform.

`OQ-023` separately owns Facebook operating/privacy/evidence-handling policy.

### PRG-EV-071 — Content delivery provenance is not the same as participation/completion evidence

Content & Media owns the governed content/translation/publication version and Programmes references exact governed Content versions.

Pass 3 already locked that exact delivered ContentVersion/locale provenance matters.

But Content ownership of the thing delivered does not itself prove that a participant read, understood, watched enough of, acted on or completed a programme requirement.

### PRG-EV-072 — Nuwe Jy day composition spans several ownership families

Product §21H.6 permits controlled Nuwe Jy components such as:

```text
teaching
video_or_audio
scripture_or_devotional
practical_action
habit
meal_or_lifestyle_guidance
reflection
check_in
download
community_prompt
live_session
rest_or_recovery_day
```

The Today experience similarly composes lesson, practical action, habit, reflection, check-in, live session, community prompt, progress and recovery.

The page/day composition therefore cannot be treated as one Domain-owned evidence record.

### PRG-EV-073 — Nuwe Jy check-ins are explicitly distinct from journals

`DEC-214` requires lightweight daily interactions plus deeper versioned milestone check-ins and says to keep journals separate.

Domain Law places lightweight programme check-in responses in HJP when they are not health facts.

If a deeper check-in contains health facts, safety inputs/outcomes or other owned data, the owning Domain remains authoritative for those fields/results. The programme may separately own that its governed check-in requirement was satisfied.

### PRG-EV-074 — Safety and health evidence retain their owners

Domain Law gives Health Records ownership of health/lifestyle facts and Safety & Eligibility ownership of safety/eligibility outcomes/restrictions.

Programmes may read current Safety authority and configure `required_for_safety` activities, but that requirement label cannot duplicate the underlying health/safety record.

### PRG-EV-075 — Analytics cannot decide programme evidence

`DEC-169` permits governed behavioural events/aggregates while excluding journal text and unnecessary health detail.

Domain Law makes Analytics derived from authoritative sources and explicitly forbids Analytics from writing source truth.

Therefore page views, video telemetry, clickstream and analytics aggregates are observations unless a separately governed owner contract turns a concrete event into business truth.

### PRG-EV-076 — Audit evidence cannot become the activity source

Audit & Evidence owns append-only/minimised proof of sensitive actions, incidents and governance.

Domain Law explicitly says cross-cutting audit/security evidence is **never source-domain truth** and Audit never mutates source truth.

An audit row that an operator changed something is not proof that the participant performed the activity.

### PRG-EV-077 — Architecture preserves one owner and treats projections/events as non-authoritative

Architecture requires:

- one owner for each durable business truth;
- cross-boundary writes through the owner;
- read projections for usability/performance without write authority;
- PubSub as observation/freshness only; and
- correct refusal/bounded waiting instead of fabricated success when current authority is unavailable.

This supports source-owner reads/reconciliation without a shared evidence dumping-ground Domain.

### PRG-EV-078 — Existing gates already cover the material unresolved edges

Existing authority already routes:

- `OQ-018` — journal encryption, retention, export, deletion and professional-record handling;
- `OQ-019` — programme-specific minimum participation/final check-ins/completion thresholds;
- `OQ-023` — Facebook moderation/privacy/evidence handling;
- `OQ-025` — exact Nuwe Jy safety routing, milestone check-ins, required activities and completion rules.

These are sufficient owners for the unresolved concrete semantics. Pass 7 does not need a new upstream Product identifier merely to restate them.

---

# 60. Pass-7 semantic model

These are working discovery semantics, not Resource/schema prescriptions.

## 60.1 Keep four evidence layers separate

For a programme activity, distinguish:

1. **Activity definition/requirement meaning** — Programmes.
2. **Source occurrence/result/fact** — the Domain that owns that business truth.
3. **Programme acceptance/satisfaction decision** — Programmes decides whether the available governed evidence satisfies this ProgrammeVersion’s progression/completion rule.
4. **Overall completion outcome** — Programmes, deferred in detail to Pass 8.

Do not collapse these into one generic `ActivityCompletion` authority.

## 60.2 Programmes may preserve minimal accepted-evidence provenance without copying the source payload

Because Programmes owns progression/completion meaning, it must be able to explain why a requirement was treated as satisfied.

The safe semantic boundary is:

```text
source Domain owns fact
        ↓
Programmes reads/receives governed minimum evidence
        ↓
Programmes records its own satisfaction/acceptance decision + minimum provenance
```

The exact representation is JIT detail.

The provenance may identify the relevant source record/version/status/time/decision basis where permitted. It must not become a duplicate mutable source record.

## 60.3 Programme-native self-attestation is allowed only when the activity meaning is genuinely programme participation

A simple activity such as “I have read/considered/done this practical action” may, if the ProgrammeVersion explicitly defines self-attestation as sufficient evidence, create a Programme-owned participation fact.

That does **not** mean every checkbox belongs in Programmes.

If the durable business meaning is actually:

- habit occurrence;
- behavioural/adherence progress;
- journal/reflection content;
- health fact;
- safety outcome;
- attendance;
- community participation; or
- another separately owned result,

the source owner remains authoritative.

Classification follows business meaning, not widget type.

## 60.4 Content delivery/opening is not completion by default

Programmes may know the exact ContentVersion/locale delivered.

But these observations do not automatically prove requirement satisfaction:

- page rendered;
- content opened;
- media started;
- media reached an arbitrary percentage;
- file download initiated;
- browser tab stayed open.

If a concrete programme requires a reading/watching acknowledgement, the ProgrammeVersion must define an acceptable evidence contract. Generic watch-time/SCORM/xAPI semantics are not implied.

## 60.5 Check-ins may be one experience but several authoritative records

A Nuwe Jy check-in UI may collect different meanings.

Examples:

- low-risk behavioural/progress response → HJP;
- health/lifestyle fact → Health Records;
- safety evaluation/outcome → Safety & Eligibility;
- Research response → Research & Feedback if that is the approved purpose;
- programme requirement “required check-in submitted” → Programmes may record its own satisfaction decision/reference.

A shared screen does not justify shared-write ownership.

## 60.6 Live attendance is Events truth

If a programme requires live attendance, Programmes consumes Events & Live’s authoritative attendance/check-in fact.

A provider join event, Zoom/Restream dashboard row, email registration or calendar RSVP is not direct Programme evidence until Events reconciles it under its own rules.

Programmes should not copy the attendance lifecycle.

## 60.7 Replay evidence is not currently a generic substitute

Events owns the session/replay association and Content owns governed replay media/publication.

Current authority does not define a universal “replay watched enough” completion fact.

If Nuwe Jy completion later permits replay as a substitute for live attendance, Pass 9 / `OQ-025` must define the substitution and the acceptable evidence source. Player analytics alone must not silently become the rule.

## 60.8 Community evidence depends on native authoritative participation

For future first-party Community, Programmes may consume minimum Community-owned participation evidence where a Product-approved programme actually requires it.

For the initial Facebook route, NewYou does not have native authoritative community-post history. Therefore Facebook activity must not silently become FP-008 completion-critical.

`PRG-GAP-006` remains `DEFER_YAGNI` unless Product explicitly requires a governed evidence route.

## 60.9 Journal evidence is existence/participation at most, never copied private text

A programme may require a reflection/journal activity, but Programmes must not copy or inspect private journal text merely to prove completion unless a separately approved purpose/consent/owner rule permits it.

The most Programmes could need is a minimal satisfaction fact/reference such as “required reflection submitted” — and even retention of that fact after journal deletion remains subject to `PRG-GAP-007`, `OQ-018` and Privacy law.

Do not resolve that retention question in this pass.

## 60.10 Source corrections do not silently rewrite programme history

If a source Domain corrects/reverses a fact after Programmes has accepted it:

- the source Domain remains authoritative for the corrected fact;
- Programmes must not pretend the old source fact is still current;
- Programmes must not silently erase/rewrite its own prior decision/history;
- any material programme consequence must occur through an explicit reconciliation/correction path with before/after provenance.

Exact completion correction consequences remain `PRG-GAP-002` / Pass 8.

## 60.11 Deletion and retention can constrain what evidence Programmes is allowed to keep

A completion system does not automatically trump Privacy/retention law.

Programmes should retain only the minimum evidence/provenance lawfully required for its own durable outcome.

Private source payloads—especially journal text—must not be copied simply to make completion reconstruction convenient.

## 60.12 Source events can trigger reevaluation but are not the authority themselves

A source-domain event/message may prompt Programmes to reevaluate progression.

However:

- duplicate messages cannot double-count;
- reordered messages cannot replace current source authority;
- stale cached projections cannot overrule the owner;
- temporary source unavailability must defer/fail closed where a hard gate depends on it rather than fabricate success.

Exact sync/async mechanics remain JIT.

## 60.13 Facilitator/operator roles do not gain universal evidence-authority

A facilitator, programme admin or support operator cannot fabricate an HJP occurrence, Event attendance, Community post or Safety outcome merely because Programmes needs evidence.

If a future programme supports a genuine manual attestation/review activity, its owner, guards, reason, audit, reversibility and participant visibility must be explicit.

This reinforces `PRG-GAP-009`; no generic “mark complete” override is admitted.

---

# 61. Pass-7 focused pressure tests

## PRG-PT-191 — Activity definition references an HJP habit occurrence

**Scenario:** A Programme activity requires a daily habit that exists in HJP.

**Expected invariants / analysis:** HJP owns the habit schedule/occurrence. Programmes owns the requirement and may accept the minimum occurrence evidence for progression/completion; it must not create a duplicate habit occurrence.

**Disposition:** `PASS`.

---

## PRG-PT-192 — Programmes copies journal text to prove a reflection was done

**Scenario:** A required reflection is entered in the private journal.

**Expected invariants / analysis:** Rejected. Journal content stays HJP/private. Programmes may at most consume a minimal permitted satisfaction/reference fact; exact retention after deletion remains PRG-GAP-007.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-193 — Programme-native self-attestation for a practical action

**Scenario:** A bounded activity says “confirm when you have completed today’s practical action” and no separate durable business fact exists.

**Expected invariants / analysis:** If the ProgrammeVersion explicitly declares participant self-attestation sufficient, the resulting participation fact may be Programme-owned. Do not manufacture an HJP record merely because there is a checkbox.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-194 — Page render automatically marks lesson complete

**Scenario:** Participant opens a teaching page.

**Expected invariants / analysis:** A page render proves delivery/access, not comprehension or requirement satisfaction. Auto-completion is not justified absent an explicit ProgrammeVersion evidence rule.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-195 — Video start automatically marks activity complete

**Scenario:** Participant starts a video and leaves after seconds.

**Expected invariants / analysis:** Content/player telemetry is observation, not governed programme evidence by default.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-196 — Generic 80% or 90% watch threshold

**Scenario:** A developer proposes a universal video-completion percentage.

**Expected invariants / analysis:** No current Product rule defines such a threshold. Generic watch-time completion is DEFER_YAGNI; a concrete ProgrammeVersion must define any required evidence contract.

**Disposition:** `DEFER_YAGNI`.

---

## PRG-PT-197 — Download click equals completed activity

**Scenario:** Participant clicks a PDF download.

**Expected invariants / analysis:** The click can prove an attempted delivery at most. It does not prove reading/action/completion unless an explicit bounded self-attestation or other governed rule exists.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-198 — Habit occurrence completed

**Scenario:** HJP records the required habit occurrence as completed.

**Expected invariants / analysis:** Programmes may accept the owner-managed occurrence state as evidence. It must not duplicate or mutate the HJP occurrence.

**Disposition:** `PASS`.

---

## PRG-PT-199 — Habit occurrence is partial

**Scenario:** HJP records partial rather than completed.

**Expected invariants / analysis:** Programmes receives the actual source state. Whether partial satisfies a programme requirement is ProgrammeVersion/completion policy, reserved to Pass 8 rather than silently coercing partial to complete.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-200 — Habit occurrence intentional skip or safety blocked

**Scenario:** HJP records intentional_skip or safety_blocked.

**Expected invariants / analysis:** Programmes must preserve the source meaning and not rewrite it as ordinary completion/failure. Completion/exemption consequences belong Passes 8–10.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-201 — Required journal/reflection entry exists

**Scenario:** HJP records that a programme reflection entry was submitted.

**Expected invariants / analysis:** Programmes may consume only the minimum permitted existence/satisfaction evidence; private text remains HJP.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-202 — Journal is deleted after Programmes accepted evidence

**Scenario:** Participant exercises deletion rights after a reflection satisfied a requirement.

**Expected invariants / analysis:** Programmes must not retain copied journal content. Whether a minimal historical satisfaction fact/reference may survive is still PRG-GAP-007/OQ-018/Privacy work; do not invent it here.

**Disposition:** `INSUFFICIENT_AUTHORITY / EXISTING_GAP`.

---

## PRG-PT-203 — Journal entry is corrected/edited

**Scenario:** Participant edits a reflection after initial submission.

**Expected invariants / analysis:** HJP owns the entry history/correction semantics. Programmes should not diff or copy content; only a material satisfaction-state change, if governed, should trigger explicit reconciliation.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-204 — Lightweight daily Nuwe Jy check-in

**Scenario:** Daily interaction records behavioural/progress response without health facts.

**Expected invariants / analysis:** Domain Law places this response in HJP. Programmes may own the requirement that a check-in be submitted and consume minimal evidence that it occurred.

**Disposition:** `PASS`.

---

## PRG-PT-205 — One milestone check-in contains progress and health facts

**Scenario:** A single UI asks behavioural progress questions plus health/lifestyle facts.

**Expected invariants / analysis:** The UI may orchestrate multiple owners: HJP for progress, Health Records for health facts. Programmes may separately record requirement satisfaction. One form does not create one owner.

**Disposition:** `PASS`.

---

## PRG-PT-206 — Milestone check-in triggers safety routing

**Scenario:** A check-in answer requires a Safety evaluation/restriction.

**Expected invariants / analysis:** Health/Safety owners establish those facts/outcomes. Programmes consumes current Safety authority for its requirement/progression consequences; it does not copy the safety engine.

**Disposition:** `PASS`.

---

## PRG-PT-207 — Live-session attendance satisfies a programme activity

**Scenario:** Events & Live records authoritative check-in/attendance.

**Expected invariants / analysis:** Programmes may reference/accept Events-owned attendance. Registration alone or programme cohort membership is insufficient.

**Disposition:** `PASS`.

---

## PRG-PT-208 — Provider dashboard says participant joined but Events has not reconciled attendance

**Scenario:** Restream/Zoom provider evidence exists.

**Expected invariants / analysis:** Provider state is evidence to Events, not direct Programme authority. Programmes waits for/re-reads Events-owned attendance truth for a hard requirement.

**Disposition:** `PASS`.

---

## PRG-PT-209 — Replay viewed as a substitute for live attendance

**Scenario:** Participant watches the governed replay after missing live.

**Expected invariants / analysis:** Current law links governed replays but does not define universal replay-completion evidence or substitution. Route substitution/evidence rule to Pass 9/OQ-025; analytics alone is insufficient.

**Disposition:** `DEFER_TO_PASS_9`.

---

## PRG-PT-210 — Attendance corrected after initial check-in

**Scenario:** Events corrects an attendance fact after Programmes accepted it.

**Expected invariants / analysis:** Events remains source owner. Programmes requires explicit reconciliation if the change materially affects progression/completion; no silent history rewrite. Final completion-correction policy is Pass 8/PRG-GAP-002.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-211 — First-party Community participation used as evidence

**Scenario:** A future approved programme requires a native Community contribution.

**Expected invariants / analysis:** Community owns participation/post/moderation truth. Programmes may consume minimum governed evidence if Product explicitly makes it requirement-critical; raw post content need not be copied.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-212 — Facebook comment used as FP-008 completion evidence

**Scenario:** Initial Nuwe Jy participant comments in the external Facebook cohort group.

**Expected invariants / analysis:** External Facebook is not permanent platform authority. Keep such participation non-completion-critical unless Product creates a governed evidence route. PRG-GAP-006 remains DEFER_YAGNI.

**Disposition:** `DEFER_YAGNI / EXISTING_GAP`.

---

## PRG-PT-213 — Native Community post later removed/moderated

**Scenario:** A post that once satisfied a requirement is removed under Community policy.

**Expected invariants / analysis:** Community owns the moderation/source lifecycle. Programmes must not preserve the raw post; any effect on accepted completion evidence requires explicit reconciliation policy, not hidden reversal.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-214 — Participant leaves or loses Community access after earlier participation

**Scenario:** Historical Community participation exists but current membership/access changes.

**Expected invariants / analysis:** Current Community access and historical source evidence are distinct. Programmes cannot infer deletion of prior programme history from current Community membership alone.

**Disposition:** `PASS`.

---

## PRG-PT-215 — Safety outcome is used as required-for-safety evidence

**Scenario:** Safety & Eligibility records a current outcome/restriction.

**Expected invariants / analysis:** Programmes may reference the current authoritative Safety outcome for progression. The required_for_safety label does not create duplicate Safety truth.

**Disposition:** `PASS`.

---

## PRG-PT-216 — Safety acknowledgement versus safety clearance

**Scenario:** A participant clicks “I understand” while a separate Safety evaluation remains unresolved.

**Expected invariants / analysis:** A programme-native acknowledgement may be Programmes participation evidence if explicitly required, but it cannot stand in for Safety-owned eligibility/clearance.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-217 — Temperament assessment result satisfies a programme prerequisite

**Scenario:** A programme requires a qualifying completed assessment.

**Expected invariants / analysis:** Temperament owns attempt/result truth. Programmes reads the governed eligible result/provenance; it does not copy scoring answers/result authority.

**Disposition:** `PASS`.

---

## PRG-PT-218 — Plan/adherence activity

**Scenario:** Programme asks participant to follow an assigned plan and report adherence.

**Expected invariants / analysis:** Plans owns delivered plan truth; HJP owns behavioural/adherence entries. Programmes may consume the minimum evidence required by its activity rule, not become plan/adherence authority.

**Disposition:** `PASS`.

---

## PRG-PT-219 — Practical action has no independent durable source fact

**Scenario:** Activity is a bounded one-off programme action with explicit self-attestation.

**Expected invariants / analysis:** A Programme-owned self-attestation is acceptable when that is genuinely the approved business meaning and evidence rule; no generic cross-domain record is required.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-220 — Practical action actually creates durable behavioural progress

**Scenario:** The same UI action records an ongoing self-tracking/adherence entry.

**Expected invariants / analysis:** Business meaning now fits HJP; UI reuse does not transfer ownership to Programmes.

**Disposition:** `PASS`.

---

## PRG-PT-221 — Facilitator marks an HJP habit complete from programme admin

**Scenario:** Facilitator uses a programme screen to manufacture an external source fact.

**Expected invariants / analysis:** Rejected. A Programmes role cannot mutate HJP truth through a shadow write path. Any owner-authorised staff correction belongs HJP’s own contract.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-222 — Programme admin marks live attendance complete

**Scenario:** Admin toggles a programme checkbox rather than correcting Events attendance.

**Expected invariants / analysis:** Rejected as shared-write authority. Attendance correction must go through Events & Live; Programmes can then re-evaluate evidence.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-223 — Audit log is used as participant activity evidence

**Scenario:** Audit records that a staff member opened/changed a record.

**Expected invariants / analysis:** Audit proves governance/action evidence, not the participant’s underlying activity. Audit never becomes source truth.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-224 — Analytics page_view event is used as completion evidence

**Scenario:** Analytics records a lesson page view.

**Expected invariants / analysis:** Analytics is derived. A page_view cannot silently decide programme satisfaction/completion.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-225 — PubSub event is treated as evidence

**Scenario:** A source-domain PubSub notification says an occurrence changed.

**Expected invariants / analysis:** PubSub is freshness/observation only. Programmes re-reads durable owner authority where correctness matters.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-226 — Duplicate source event/message

**Scenario:** Programmes receives the same habit/attendance consequence twice.

**Expected invariants / analysis:** Reevaluation/acceptance must be repeat-safe; one source fact cannot multiply programme progress merely because messages duplicate.

**Disposition:** `PASS`.

---

## PRG-PT-227 — Out-of-order source events

**Scenario:** A correction message arrives before/after an older completion observation.

**Expected invariants / analysis:** Message order cannot replace current source authority. Programmes reconciles against the owner’s governed state/provenance.

**Disposition:** `PASS`.

---

## PRG-PT-228 — Source Domain temporarily unavailable during a hard progression check

**Scenario:** Events/HJP/Safety cannot be read at that moment.

**Expected invariants / analysis:** Correct bounded waiting/refusal is safer than fabricated success. Cached/Analytics/provider observations cannot be promoted to hard authority merely for availability.

**Disposition:** `PASS`.

---

## PRG-PT-229 — Source record corrected after evidence acceptance

**Scenario:** Owner changes a source state with governed correction semantics.

**Expected invariants / analysis:** Programmes preserves its prior decision/history and processes an explicit reconciliation if the correction is material. Exact completion correction consequences remain Pass 8/PRG-GAP-002.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-230 — Source record deleted for privacy

**Scenario:** A source item is lawfully deleted after programme participation.

**Expected invariants / analysis:** Programmes may not retain a forbidden duplicate payload. Minimum surviving provenance, if any, depends on source/privacy/retention rules; journal case remains PRG-GAP-007.

**Disposition:** `PASS_WITH_EXISTING_GAP`.

---

## PRG-PT-231 — Same source occurrence is accidentally counted twice

**Scenario:** Two programme projections/reference rows point to one HJP/Event occurrence.

**Expected invariants / analysis:** Duplicate references must not multiply satisfaction. Exact representation is JIT, but the source identity/provenance must permit repeat-safe acceptance.

**Disposition:** `PASS`.

---

## PRG-PT-232 — One source occurrence is intended to satisfy two requirements

**Scenario:** Product designer wants one check-in/attendance fact to fulfil two explicit programme activities.

**Expected invariants / analysis:** Do not infer equivalence automatically. ProgrammeVersion must explicitly define that mapping; broader substitution/equivalence semantics belong Pass 9.

**Disposition:** `DEFER_TO_PASS_9`.

---

## PRG-PT-233 — Research response appears inside a programme day

**Scenario:** A future programme embeds a governed research instrument.

**Expected invariants / analysis:** Research & Feedback owns the response/instrument lifecycle. Programmes is only a contextual surface/consumer of any explicitly approved participation evidence.

**Disposition:** `PASS / FUTURE_ONLY`.

---

## PRG-PT-234 — Governed vote appears inside a challenge/programme

**Scenario:** A future challenge embeds a governed vote.

**Expected invariants / analysis:** Voting & Balloting owns vote submission/tally/result; Programmes surface location does not transfer vote authority. No generic programme evidence ownership follows.

**Disposition:** `PASS / FUTURE_ONLY`.

---

## PRG-PT-235 — Interactive tool result appears as an activity

**Scenario:** A programme uses a calculator/decision aid/self-tracking tool.

**Expected invariants / analysis:** Ownership follows purpose/business meaning: Content for published artifact, HJP for qualifying self-tracking result, or another existing owner for consequential truth. Programmes does not create a generic ToolResult/evidence authority.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

# 62. Pass-7 gap adjudication

## PRG-GAP-006 — External community as completion evidence — confirmed / narrowed

**Prior classification:** `DOMAIN_BOUNDARY_GAP / DEFER_YAGNI`.

**Pass-7 finding:** the owner boundary is now explicit:

- future first-party Community owns authoritative native participation/moderation truth;
- Programmes may consume minimum Community evidence only when an approved ProgrammeVersion genuinely requires it;
- external Facebook is not durable NewYou participation authority;
- FP-008 must not treat Facebook comments/posts/reactions as completion-critical by developer convention.

**Revised status:** `CONFIRMED / NATIVE_ROUTE_POSSIBLE_WHEN_APPROVED / EXTERNAL_FACEBOOK_DEFER_YAGNI`.

No upstream Product delta is justified until Product actually requires external-community participation to determine progression/completion.

## PRG-GAP-007 — Journal evidence after deletion/correction — confirmed / sharpened

**Prior classification:** `PRIVACY_JOURNAL_GATE / FUTURE_FP014`.

**Pass-7 finding:** broad ownership is resolved but the deletion/retention consequence is not:

- HJP owns the journal entry/text;
- Programmes must not copy journal text or attachments as completion evidence;
- Programmes may only need a minimum satisfaction/reference fact;
- whether that minimum fact may lawfully survive eligible journal deletion, and how it de-links/reconciles, remains `OQ-018`/Privacy/HJP JIT work.

**Revised status:** `CONFIRMED / RAW_PAYLOAD_PROHIBITED / MINIMAL_EVIDENCE_RETENTION_UNRESOLVED`.

This remains non-blocking for FP-008 **provided Nuwe Jy does not make private journal content a completion-critical requirement before the gate is resolved**.

## PRG-GAP-009 — Operator exception authority — reinforced

Pass 7 confirms that a facilitator/programme admin/support actor cannot manufacture another Domain’s source evidence through a generic programme override.

If a future exception command is required, it needs an explicit owner, guard, reason, audit, reversibility/correction model and participant visibility appropriate to that business truth.

This remains `JIT_ONLY + PRODUCT PREREQ WHERE NEEDED`; no new `PRG-UPD` is justified.

## PRG-GAP-002 — Completion exceptions/corrections — future Pass-8 route preserved

Source evidence may later be corrected/reversed/deleted.

Pass 7 establishes that source correction does not silently rewrite Programme history, but the exact consequences for an already-awarded completion/certificate remain a completion-semantic question.

Route that consequence to Pass 8 / `PRG-GAP-002`; do not solve it here.

## No new Product / Architecture / Domain gap promoted

The dedicated evidence pass did **not** justify a new `PRG-GAP-###` or `PRG-UPD-###`.

The current authority hierarchy is sufficient to define the owner boundary. The remaining unknowns are already correctly located in concrete programme-completion, privacy/journal, Facebook-evidence and exception gates.

---

# 63. Pass-7 refinements to earlier working synthesis

## PRG-REF-039 — Activity definition and activity source fact are different authorities

Programmes owns the activity’s place/requirement/evidence meaning in a ProgrammeVersion.

The underlying fact remains with the Domain whose business meaning it represents.

## PRG-REF-040 — Programmes owns evidence acceptance, not every evidence source

Programmes may durably explain that a requirement was treated as satisfied under its versioned rules while referring to minimum source provenance.

That does not transfer mutation authority or justify duplicating source payloads.

## PRG-REF-041 — Programme-native self-attestation is bounded by business meaning

A simple one-off programme participation attestation may be Programme-owned if the ProgrammeVersion explicitly defines it as sufficient evidence and no separately owned durable truth is being represented.

Widget shape never decides ownership.

## PRG-REF-042 — Content delivery provenance is not completion evidence

Exact ContentVersion/locale delivered remains essential historical provenance.

It does not by itself prove reading, comprehension, watch-time or action completion.

## PRG-REF-043 — Check-in UI can orchestrate multiple owners

A check-in may write HJP progress, Health Records facts and trigger Safety while Programmes records only requirement satisfaction/provenance.

One form does not imply one Domain or table.

## PRG-REF-044 — Live attendance evidence comes from Events & Live

Programme linkage/registration/provider telemetry cannot substitute for Events-owned attendance/check-in truth.

## PRG-REF-045 — Replay-as-evidence requires explicit substitution semantics

A governed replay exists, but universal replay-watch completion evidence is not established.

Do not create watch-percentage rules or analytics-driven substitutes before Pass 9/OQ-025 resolves the concrete need.

## PRG-REF-046 — Community evidence requires an authoritative Community route

Future native Community evidence may be consumed where explicitly approved.

External Facebook participation remains non-completion-critical by default.

## PRG-REF-047 — Journal text never belongs in Programme evidence

Programmes must not retain journal body/attachments to prove a reflection requirement.

Any minimal satisfaction fact is separately constrained by Privacy/HJP retention/deletion rules.

## PRG-REF-048 — Analytics/Audit/provider/PubSub observations cannot satisfy hard programme requirements by themselves

They may trigger refresh/reconciliation or support evidence investigation, but they do not replace the authoritative business owner.

## PRG-REF-049 — Cross-Domain evidence acceptance must be duplicate/reorder safe

Duplicate or reordered messages/observations cannot multiply programme progress or overwrite newer source truth.

Exact transport/materialisation remains JIT.

## PRG-REF-050 — Source correction requires explicit programme reconciliation, not silent retroactive rewrite

The source owner may correct its fact.

Programmes preserves its historical decision/provenance and applies any material consequence through an explicit governed correction path.

## PRG-REF-051 — Facilitator/admin role is not universal evidence authority

Roles may operate approved owner actions; they do not gain a cross-Domain “mark complete” bypass.

## PRG-REF-052 — Do not force every day component into tracked evidence

Teaching, devotional, download, community prompt, rest/recovery and other day components may exist without being completion-tracked activities.

Only an explicit ProgrammeVersion requirement/evidence contract justifies durable satisfaction tracking.

---

# 64. Pass-7 anti-LMS / YAGNI outcome

Pass 7 explicitly rejects:

- one generic cross-Domain `ActivityCompletion` or `Evidence` store as shared business authority;
- copying journal text, Community posts, Event provider payloads, health facts or Safety records into Programmes;
- page-view/open/download events as automatic completion;
- generic video watch-percentage completion;
- SCORM/xAPI merely to obtain activity telemetry;
- treating Analytics events as hard programme evidence;
- treating Audit logs as source facts;
- treating PubSub/messages/caches as source facts;
- treating provider dashboards as source facts;
- facilitator/admin “mark anything complete” authority;
- one form/table owning all fields in a multi-purpose check-in;
- external Facebook post/comment scraping/import as a prerequisite for FP-008;
- a generic replay-equivalence engine before a concrete substitution requirement;
- a generic quiz/gradebook engine without an approved NewYou outcome;
- tracking every Nuwe Jy day component merely because LMS products track everything.

Generic LMS evidence/completion plumbing remains `DEFER_YAGNI`.

---

# 65. Pass-7 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Programmes owns ActivityDefinition/requirement/progression/completion meaning; it does not automatically own the source fact for the activity.
2. Every durable source fact keeps exactly one authoritative Domain owner.
3. Programmes may record its own requirement-satisfaction/evidence-acceptance decision and minimum permitted provenance without duplicating source payloads.
4. Programme-native self-attestation is acceptable only when that is genuinely the approved participation meaning and no separately owned durable truth is being represented.
5. Page render, content open, video start/progress, download click and similar telemetry are not completion evidence by default.
6. Exact delivered ContentVersion/locale provenance remains distinct from activity satisfaction.
7. HJP owns habit occurrences, journals, behavioural/adherence/progress entries and qualifying lightweight programme check-in responses.
8. Private journal text/attachments must never be copied into Programmes merely to prove completion.
9. `PRG-GAP-007` remains open for whether/how a minimal journal-satisfaction fact may survive eligible journal deletion; FP-008 should not depend on that unresolved semantic.
10. A single Nuwe Jy check-in may orchestrate multiple owners; field/business meaning determines authority, not the screen/form.
11. Events & Live owns attendance/check-in; provider telemetry/registration alone cannot satisfy a programme attendance requirement.
12. Replay-as-substitute evidence is not universal and remains Pass 9/OQ-025 work.
13. First-party Community may supply minimum participation evidence when explicitly approved; external Facebook cannot silently become FP-008 completion authority.
14. `PRG-GAP-006` remains DEFER_YAGNI for external-community completion evidence.
15. Safety/Health/Temperament/Plans/Research/Voting/Tool results retain their existing owners when used in a programme context.
16. Analytics, Audit, PubSub, caches and provider state can support observation/reconciliation but cannot become source evidence authority.
17. Duplicate/reordered source events must not multiply or regress programme satisfaction; hard checks reconcile from owner authority.
18. Temporary source unavailability may defer/refuse a hard progression decision rather than fabricate success.
19. Source correction/deletion does not silently rewrite Programme history; material consequences require explicit reconciliation with before/after provenance.
20. Completion/certificate correction consequences remain Pass 8 / `PRG-GAP-002`.
21. Facilitators/admins cannot manufacture source-Domain evidence through a generic Programmes override; `PRG-GAP-009` remains the exception-authority route.
22. Not every day component needs durable evidence/tracking; only explicit ProgrammeVersion requirements justify it.
23. No new Domain, `PRG-GAP-###` or `PRG-UPD-###` is justified by Pass 7.
24. Generic LMS evidence/gradebook/watch-time/SCORM/xAPI machinery remains `DEFER_YAGNI`.

**Pass hard stop:** Pass 8 has not started. Exact completion thresholds, minimum participation, final check-ins, completion evaluation timing, certificate outcomes, completion corrections and similar completion semantics remain deliberately unexamined beyond the minimum references needed to preserve evidence ownership boundaries.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.
