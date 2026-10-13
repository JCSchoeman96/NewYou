# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.15.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.15.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 14 — journals / habits / private-reflection edge semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.14.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused Habits, Journals & Progress / Programme seam pass while preserving Passes 1–13 and their accepted working-lock boundaries.

> This is an append-only semantic successor. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work, approved Feature Pack/JIT contracts, Privacy & Consent authority, Safety & Eligibility authority, Health Records authority, Professional Care authority or Habits, Journals & Progress authority.

> A Programme may ask for a habit action, reflection or journal-linked activity and may decide whether approved source evidence satisfies its own requirement. It does not thereby acquire the participant's private journal text, habit-occurrence truth, health facts, sharing authority, professional record, reminder-delivery truth or clinical interpretation.

---

# 110. Accepted working-lock status entering Pass 14

The user explicitly accepted Pass 13 and instructed the stream to continue with the next pass.

Therefore Passes 1–13 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, named authority gates, deferred items and later explicit refinements.

Pass 14 inherits without reopening:

- ProgrammeVersion owns programme/activity structure, requirement type, progression, exception/substitution and completion meaning;
- Habits, Journals & Progress (HJP) owns participant habit schedules/occurrences, private journals/reflections and non-clinical behavioural progress truth;
- Programmes explicitly does not own participant journal or habit-occurrence truth;
- source evidence and Programme satisfaction remain distinct; Programmes consumes minimum governed evidence and owns only its requirement consequence;
- `completed`, `partially_completed`, `skipped_intentionally`, `missed`, `not_applicable` and `safety_blocked` are source states, not universal Programme outcomes;
- `safety_blocked`, exempt, substituted, skipped and not-applicable never fabricate completion by inference;
- current Safety constrains future Programme guidance without silently rewriting historical participation;
- one screen may orchestrate several owning Domains without becoming a shared-write record;
- operator/facilitator/support authority remains bounded and cannot become generic source-evidence, mark-complete, waiver, Safety-override or professional-review authority;
- private participant progress is not automatically shared to Community, facilitators, purchasers or Analytics;
- exact Programme/Nuwe Jy completion thresholds remain behind `OQ-019` / `OQ-025`;
- exact journal encryption, retention, export, deletion and professional-record handling remain behind `OQ-018` and applicable lifecycle gates.

---

# 111. Pass 14 — journals / habits / private-reflection edge semantics

## 111.1 Scope hard stop

This pass answers only:

1. how Programme habit/reflection/journal-linked activities compose with HJP-owned source truth;
2. how Programme requirement satisfaction can be proven without copying private journal content;
3. why a Programme prompt, participant response and Programme satisfaction decision are separate truths;
4. how the seven HJP habit-occurrence states affect Programme evidence without becoming universal completion outcomes;
5. how participant-created and practitioner-assigned habits differ at the Programme boundary;
6. how programme-relative habit schedules compose with Edition timing, late enrolment, recovery and participant timezone;
7. how reminder delivery/failure differs from habit occurrence and Programme compliance;
8. how Habit pause, Enrolment pause and reminder pause remain independent lifecycle dimensions;
9. how private reflection differs from a private journal record, a structured check-in and a health/safety fact;
10. how required reflection can remain private while still supplying minimum Programme evidence;
11. how journal sharing, accountability sharing and professional-record copying remain distinct;
12. how share expiry/revocation affects future access without rewriting source or Programme history by implication;
13. how journal deletion, attachment deletion and Programme provenance avoid covert retention of private content;
14. how free-text journal safety boundaries avoid continuous monitoring, AI triage and hidden clinical intake;
15. how health-sensitive information discovered through a governed reflective/check-in flow routes to Health Records/Safety without moving journal authority;
16. how source corrections reconcile with Programme satisfaction and the existing post-award correction gap;
17. how journal/habit Analytics remains derived and privacy-minimised;
18. how duplicate occurrence submissions, timezone changes and share/revoke races constrain later JIT proof without prescribing implementation; and
19. whether any new Product, Architecture or Domain gap is required before later FP-008/FP-014 JIT.

This pass deliberately does **not** decide:

- exact Programme or Nuwe Jy minimum participation/completion thresholds — `OQ-019` / `OQ-025`;
- exact journal encryption, field-policy, retention, export, deletion or professional-record-copy handling — `OQ-018` plus applicable `OQ-029` / `OQ-032` / `OQ-033`;
- exact reminder channels, retry schedules, quiet-hour implementation, provider choice or delivery evidence — `OQ-017` / `OQ-036` as applicable;
- exact clinical interpretation of any health/safety input — Safety/Health authority and existing clinical gates;
- exact participant-specific habit limits, exercise prescriptions or clinical habit protocols;
- exact journal attachment storage/encryption/resource representation;
- exact Ash Resources/actions/tables/indexes/authorization policies;
- automatic free-text crisis detection, sentiment scoring or AI journal monitoring;
- AI journal summarisation/assistance — `DEC-167`, outside MVP unless separately activated;
- translation/version-localisation semantics reserved for Pass 15;
- communications orchestration reserved for its later dedicated pass; or
- the broader FP-014 second-lens convergence pass reserved for later in this stream.

---

## 111.2 Pass-14 authority evidence

### PRG-EV-182 — Live authority baseline reconfirmed

Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413`. README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` continue to route Product Law v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and Platform Operating Model v1.0.1 as current authority. These Programmes/Learning ledgers remain working/non-authoritative.

### PRG-EV-183 — Product Law has an explicit Habit/Journal/Progress model

Product §21F.12–§21F.23 and `DEC-158...DEC-169` govern approved/participant-created/practitioner-assigned habits, schedule and occurrence semantics, compassionate consistency, reminder controls, accountability sharing, journal types/privacy/safety, deferred AI assistance, progress recognition and Analytics boundaries.

Pass 14 therefore refines an existing authority model; it does not invent a new journaling or habit capability.

### PRG-EV-184 — Programmes and HJP have explicit non-overlapping ownership

Domain Law §6.8 gives Programmes ownership of activity structure, progression and completion-rule configuration but explicitly excludes participant journal/habit occurrence truth. Domain Law §6.9 gives HJP ownership of habits, schedules, occurrences, private journals/reflections and non-clinical behavioural progress while explicitly excluding Programme completion rules.

The cross-domain seam is therefore source evidence → Programme adjudication, not shared write ownership.

### PRG-EV-185 — Habit occurrence has seven locked source states

Product §21F.14 / `DEC-160` define:

```text
pending
completed
partially_completed
skipped_intentionally
missed
not_applicable
safety_blocked
```

Intentional skips do not equal failure, safety-blocked occurrences reflect professional/platform restrictions, future occurrences are not missed before the window ends and staff may not silently alter participant history.

### PRG-EV-186 — Compassionate consistency rejects punitive streak semantics

Product §21F.15 / `DEC-161` preserve progress through misses, use trend/recovery indicators rather than fragile streak resets and state that safety pauses do not count as failures.

A Programme cannot silently reintroduce punitive streak authority through a habit-linked requirement.

### PRG-EV-187 — Habit scheduling includes timezone and programme-relative semantics

Product §21F.13 / `DEC-159` permit daily, selected-weekday, times-per-week, weekly, specific-date and programme-relative schedules. Participant timezone changes must not duplicate completions; completion windows must behave predictably around late-night entries; missed occurrences remain historical.

HJP therefore remains the source owner for occurrence/window truth even when the schedule is Programme-linked.

### PRG-EV-188 — Participant-created and practitioner-assigned habits are deliberately distinguishable

Product §21F.12 / `DEC-158` allow approved habits plus participant-created low-risk habits and require practitioner-assigned habits to remain distinguishable. Participant-created habits may not claim diagnosis, treatment or replacement of professional recommendations.

This prevents Programmes from treating all habits as interchangeable evidence by name alone.

### PRG-EV-189 — Accountability sharing excludes journals/health by default and does not grant mutation authority

Product §21F.17 / `DEC-163` make accountability sharing optional, scoped and revocable. Selected habits, milestones, completion summaries or participant-written updates may be shared, but journals, health data and assessment details are excluded by default; recipients cannot alter participant history.

### PRG-EV-190 — Journal privacy is private-by-default and entry-specific

Product §21F.19 / `DEC-165` keep journals private by default. Ordinary support, content, moderator and administrator roles cannot browse journals. Selected entries may be shared with an authorised practitioner only with recorded recipient, scope, purpose and expiry, and access is audited.

### PRG-EV-191 — Journal sharing and professional records are separate lifecycles

Product §21F.19 says revocation ends future platform access to a shared journal entry subject to professional retention obligations where an entry has entered a professional record. Domain Law §6.9 explicitly says HJP does not own the practitioner professional-record copy.

Thus `journal share` ≠ `professional record`, and revoking one cannot silently erase or manufacture the other.

### PRG-EV-192 — Structured health check-ins remain separate from private journals

Product §21F.18 explicitly separates structured health check-ins from private journals. Product §21H.17 likewise keeps journals separate from Nuwe Jy daily/milestone check-ins.

A reflective UI label does not decide whether the durable truth is journal, behavioural progress or health data; business meaning does.

### PRG-EV-193 — Free-text journals are not a continuous safety-monitoring channel

Product §21F.20 / `DEC-166` require a non-monitoring boundary. Structured check-ins and explicit help actions may trigger safety workflows; free-text AI monitoring is excluded from the MVP. Any future assistive detection requires disclosure, expert approval, tested escalation capacity and a staffed response process.

### PRG-EV-194 — AI journal assistance is explicitly deferred

`DEC-167` / Product §21F.21 put future AI journal assistance outside the MVP and require participant initiation, selected scope, labelling, non-diagnostic behaviour and no automatic sharing.

Therefore AI scoring/summarisation cannot be introduced as an invisible Programme completion mechanism.

### PRG-EV-195 — Journal text is excluded from Analytics and support-copy shortcuts

Product §21F.19 prohibits journal excerpts being copied into support tickets or Analytics. Product §21F.23 / `DEC-169` allow behavioural events/aggregates while excluding journal text and unnecessary health detail. Analytics never changes completion or Safety truth.

### PRG-EV-196 — Journal deletion receives stronger content-level treatment than Programme history

`DEC-227` prioritises deletion of private journal content, attachments and derived artefacts while separately governing professional copies. `DEC-228` requires deletion propagation to originals, derivatives, previews, extracted values, indexes, cached links and temporary artefacts.

A Programme cannot defeat those lifecycle rules by copying journal text or attachments into its own provenance.

### PRG-EV-197 — Privacy owns lifecycle authority, not journal business truth

Domain Law §6.2 assigns Privacy & Consent purpose-specific consent/share authority and deletion/retention/export orchestration while explicitly excluding ownership of the underlying journal records. Withdrawal stops dependent future processing and invalidates derived authority.

HJP still owns the journal/share record; Privacy governs whether relevant processing/access remains authorised.

### PRG-EV-198 — HJP is the source for approved Programme/Plan review inputs, not the decision owner

Domain Law §6.9 allows HJP to supply approved review inputs to Plans/Programmes while explicitly excluding Programme completion rules and Plan adjustment decisions.

Thus a habit or reflection fact may be evidence, but Programmes/Plans separately own their decisions.

### PRG-EV-199 — Nuwe Jy uses private multidimensional progress but does not turn every reflection into a journal

Product §21H permits Today components including habit/reflection/check-in and private multidimensional progress. Product §21H.17 permits optional private reflection in a check-in while stating that journals remain separate and private.

A private reflection interaction can therefore exist without automatically becoming a full journal subsystem or journal-content completion requirement.

### PRG-EV-200 — Roadmap deliberately defers private journals/richer reflective practice to FP-014

Current Roadmap places “Private journals and richer reflective practice” in `FP-014`, gated by `OQ-018`, and explicitly warns that basic progress/feedback must not become a journal system by accident. FP-014 itself targets broader programme/habit/private-reflection capability with `OQ-017`, `OQ-018`, `OQ-019`, translation/publication and retention gates.

Pass 14 must therefore preserve an FP-008-safe minimum boundary while leaving full private-journal implementation for the correctly gated Feature Pack.

### PRG-EV-201 — Reminder delivery does not belong to HJP or Programmes

`DEC-162` governs participant reminder controls, while Domain Law §6.9 explicitly excludes reminder sending/delivery truth from HJP and depends on Communications. `OQ-017` remains the architecture/operations gate for channels, scheduling, retries, quiet hours, observability and rate limits.

A reminder attempt or failure cannot become habit-occurrence authority.

### PRG-EV-202 — Programme completion remains Product-gated

`OQ-019` requires programme-specific minimum participation, final check-ins and completion thresholds before publication. `OQ-025` separately requires exact Nuwe Jy safety routing, milestone check-ins, required activities and completion rules.

Pass 14 may define evidence boundaries but may not decide how many habit/reflection occurrences are sufficient for completion.

### PRG-EV-203 — Journal encryption/retention remains an explicit security/legal gate

`OQ-018` requires encryption, field-policy boundaries, retention, export, deletion and professional-record handling for journal data. `OQ-029`, `OQ-032` and `OQ-033` remain applicable where exact retention, deletion/export operations or professional-record disposition is involved.

This pass must not manufacture those concrete rules.

### PRG-EV-204 — HJP concurrency risks are already recognised without prescribing mechanisms

Domain Law §6.9 identifies duplicate occurrence/check-in submission and share/revoke races as correctness-sensitive. It keeps participant journal/private data out of generic caches and leaves exact implementation to later JIT/proof.

Pass 14 may state required invariants but should not select queues, locks, resources or cache mechanisms.

### PRG-EV-205 — Existing gates are sufficient to route the remaining concrete unknowns

The unresolved concrete questions in this pass already route to `OQ-017`, `OQ-018`, `OQ-019`, `OQ-025`, `OQ-029`, `OQ-032` and `OQ-033` as applicable. The Product/Domain ownership boundary itself is not ambiguous enough to justify a new Domain or upstream Product amendment.

---

# 112. Pass-14 semantic model

These are working semantic conclusions, not Resource/schema prescriptions.

## 112.1 Programme prompt, participant response and Programme satisfaction are three distinct truths

For a habit/reflection/journal-linked activity, keep the chain explicit:

```text
ProgrammeVersion prompt / requirement meaning        -> Programmes & Challenges
participant habit/journal/reflection source response -> Habits, Journals & Progress
Programme requirement-satisfaction decision          -> Programmes & Challenges
```

A shared Today page or activity card does not collapse these authorities.

## 112.2 Programme satisfaction should consume minimum evidence, not private content

Where an approved Programme rule permits a private reflection/journal response to satisfy an activity, Programmes should consume only the minimum HJP-owned evidence needed to adjudicate the requirement, such as a governed source fact/reference that the qualifying response exists under the applicable activity/version.

Programmes does not need, by default:

- journal body text;
- attachment bytes;
- sentiment;
- word count;
- private tags;
- practitioner comments;
- health details contained in narrative; or
- a copy of the HJP record.

The exact qualifying evidence contract and thresholds remain `OQ-019` / `OQ-025` JIT/Product work.

## 112.3 A required private reflection must not require staff reading

Product can require completion-relevant activities/reflections while journals remain private-by-default and ordinary staff cannot browse them.

Therefore a valid completion contract cannot rely on a facilitator, moderator, support agent or Programme admin routinely reading private journal prose to decide whether the participant “reflected well enough.”

If a future programme genuinely requires professionally reviewed written work, that is a different explicitly governed activity/relationship and cannot be smuggled in through private-journal semantics.

## 112.4 Reflection is not automatically a Journal Entry

`reflection` is a user-experience/business concept that may map to different owning meanings:

- lightweight non-clinical reflection/progress response → HJP;
- full private journal entry → HJP journal lifecycle/privacy rules;
- structured health/safety answer → Health Records / Safety as applicable;
- participant-written accountability update → HJP sharing scope if explicitly shared;
- professional note/outcome → Professional Care when a valid care relationship exists.

The screen label “reflection” or placement inside a Programme does not determine the durable Resource/owner.

## 112.5 FP-008 must not accidentally require the FP-014 private-journal subsystem

Nuwe Jy may include habit/reflection/check-in experiences and minimum private progress evidence under existing Product Law. Current Roadmap explicitly defers private journals and richer reflective practice to FP-014 behind `OQ-018`.

Therefore FP-008 JIT should use the smallest approved evidence form needed by its concrete ProgrammeVersion and must not create journal encryption/retention/sharing/attachment machinery unless actual private journals enter scope.

## 112.6 Habit occurrence state is source truth, not Programme outcome

Programmes may consume HJP occurrence state, but it must not universally translate:

- `completed` → Programme complete;
- `partially_completed` → Programme failed or complete;
- `skipped_intentionally` → exemption/failure;
- `missed` → failure/abandonment;
- `not_applicable` → exemption/completion;
- `safety_blocked` → failure/completion; or
- `pending` → failure.

The ProgrammeVersion requirement plus Pass-9 exception/substitution semantics determine the programme consequence.

## 112.7 Participant-created habits are not automatic substitutes for named Programme habits

A participant-created low-risk habit is valid HJP truth, but it satisfies a Programme requirement only when the approved ProgrammeVersion explicitly accepts that habit/category/evidence or an authorised substitution decision exists.

Similarity in label, schedule or intent is not a generic equivalence engine.

## 112.8 Practitioner-assigned habit truth remains distinct from professional review and Programme satisfaction

HJP may retain the practitioner-assigned habit/reference and occurrence history. Professional Care retains the professional relationship/record/outcome where applicable. Programmes may accept the HJP-owned occurrence as requirement evidence only under an explicit Programme rule.

Programmes cannot edit the professional instruction, mark it clinically satisfied or infer professional clearance from the habit occurrence.

## 112.9 Programme-relative schedules reference Programme time; they do not create a second Programme calendar

HJP may schedule a habit relative to an approved Programme/Enrolment anchor. That schedule consumes authoritative Programme/Edition timing; it does not rewrite it.

For a scheduled Nuwe Jy Edition:

- late enrolment still joins the cohort's current day;
- catch-up does not create a private shifted Edition calendar;
- HJP occurrences may be derived/reconciled from the approved relative schedule and participant timezone;
- Programme release/history remains Programmes truth.

Exact anchor/resource mechanics remain JIT.

## 112.10 Timezone changes must reconcile HJP occurrences without duplicating Programme evidence

HJP owns occurrence-window semantics. If timezone changes alter local-day boundaries, no duplicate occurrence/completion may be manufactured. Programmes should consume the reconciled source fact rather than independently calculating a second habit day.

Historical evidence remains explainable; a timezone correction is not permission to erase prior activity silently.

## 112.11 Habit pause, Enrolment pause and reminder pause are independent

Keep separate:

```text
Habit active/paused/retired           -> HJP
Programme Enrolment active/paused/... -> Programmes
Reminder enabled/paused/delivery      -> Communications + participant preference authority
```

One state may influence another through explicit policy, but none silently mutates the others.

## 112.12 Reminder failure is not a missed habit or participant failure

A Communications/provider failure cannot set an HJP occurrence to `missed` before the occurrence window semantics say so, and it cannot make a Programme requirement fail.

The participant may still complete the habit without receiving a reminder. Delivery evidence is operational truth, not adherence truth.

## 112.13 Optional habit notes do not become hidden Programme or clinical evidence

Product allows optional notes on habit occurrences. Those notes remain HJP/private participant data according to their business meaning.

Programmes should not scan or copy them to award completion. If a governed structured field records a material health/safety fact, route that fact to Health Records/Safety rather than silently treating free text as clinical authority.

## 112.14 A private journal cannot be a disguised mandatory clinical intake

A Programme may invite or require a bounded private reflection under approved Product rules, but it must not require the participant to disclose diagnoses, medication, trauma, laboratory details, weight/body data or other sensitive clinical material merely to earn completion.

When structured health information is genuinely required, collect it through the governed Health/Safety pathway with its own purpose, consent and authority.

## 112.15 Sharing a journal entry does not prove practitioner review

The following remain distinct:

```text
entry exists
entry is shared / practitioner can access
practitioner opened/read entry
professional review relationship/case exists
professional outcome recorded
Safety/Plan consequence applied
Programme consequence applied
```

Do not collapse these into one `shared_or_reviewed` flag.

## 112.16 Accountability sharing does not make the recipient an editor or Programme adjudicator

An approved accountability partner/future facilitator may see only the selected shared habit/progress information within scope. The recipient cannot alter occurrence history, mark Programme requirements complete or gain journal/health access by implication.

## 112.17 Share expiry/revocation ends future access; it does not rewrite historical source truth

When a journal/accountability share expires or is revoked:

- future access ends according to current Privacy/HJP authority;
- the original HJP entry/occurrence remains subject to its own lifecycle;
- Programme satisfaction is not silently erased merely because sharing ended;
- if a lawful professional record copy already exists, its disposition follows Professional Care/retention authority, not the revoked HJP share.

## 112.18 Programme provenance must not defeat journal deletion

If journal text/attachments are deleted or anonymised under governing Privacy/HJP rules, Programmes must not preserve a hidden copy merely to defend a completion decision.

Where lawful and sufficient, Programme provenance should retain only the minimum independently meaningful satisfaction/source-reference fact permitted by the lifecycle contract. If the final `OQ-018` / retention/deletion contract requires that fact to disappear or de-link, Programmes must reconcile explicitly rather than covertly retain private content.

## 112.19 Attachment existence is not universal completion evidence

A Journal Entry may have an approved attachment, but Programme completion must not assume “attachment uploaded = activity complete” unless the explicit activity contract requires a bounded attachment fact and the content/privacy model permits it.

Health documents, lab evidence or practitioner correspondence must not be routed through a journal attachment merely to avoid the owning Health/Professional boundary.

## 112.20 Free-text journal content is not a Safety monitoring feed

No background Programme/HJP job, facilitator queue, Analytics model or AI service may be treated as silently monitoring journal prose for crisis/safety as part of MVP.

Approved structured check-ins and explicit help actions are the safe Product route. Any future free-text detection is a separately governed capability with disclosure, expert approval, response capacity and proof.

## 112.21 Health-sensitive reflective data routes by meaning, not by where it was typed

If a governed interaction captures a structured health/safety fact, the authoritative fact belongs to Health Records and any Safety interpretation to Safety & Eligibility even when the field appears alongside a reflection.

The private reflective narrative can remain HJP. One submission may therefore orchestrate multiple owner writes without producing one shared-write “check-in blob.”

## 112.22 Source correction and Programme reconciliation stay separate

HJP owns correction/reconciliation of habit occurrence or journal/reflection source truth. If that correction materially affects an already-recorded Programme satisfaction decision, Programmes performs an explicit owner-side reconciliation with before/after provenance.

A correction does not grant HJP permission to rewrite Programme completion directly, and Programmes does not rewrite HJP history to preserve its prior decision.

Post-award certificate/outcome consequences remain the existing `PRG-GAP-002` seam.

## 112.23 Deleting a private journal does not automatically mean the participant never participated

Content deletion and Programme participation history are distinct lifecycle questions. Current authority permits strong deletion of private journal content while Programme history may retain separately governed participation/satisfaction facts.

The exact retention/de-link rule for any minimum derived evidence is intentionally deferred to `OQ-018` / `OQ-029` / `OQ-032`; this pass does not claim a universal right to retain it.

## 112.24 Analytics may count events, never inspect prose to create authority

Governed analytics may count events such as habit completion, intentional skip, reflection creation or milestone occurrence. Journal text remains excluded; Analytics cannot infer requirement satisfaction, Safety status or participant failure and override the source owners.

## 112.25 Duplicate submissions must not multiply source or Programme effects

A repeated client request, retry, reconnect or job must not create duplicate HJP occurrence/completion evidence or duplicate Programme satisfaction consequences for the same governed identity.

Exact idempotency identity/transaction design remains JIT, but the durable result must be repeat-safe.

## 112.26 Share/revoke races resolve from current owner authority

If sharing, expiry, revocation and practitioner access race, the system must resolve current access from HJP/Privacy/Professional relationship authority rather than stale UI/session/provider state.

A stale access projection cannot extend private-journal access after revocation.

## 112.27 A generic habit-equivalence/reflection-scoring engine is not justified

FP-008/FP-014 can be satisfied with explicit ProgrammeVersion activity contracts, HJP source truth and bounded evidence acceptance. There is no evidence-backed need for:

- semantic similarity scoring of habits;
- generic reflection quality scoring;
- sentiment-based completion;
- journal-content rubrics;
- free-text clinical classifiers;
- a universal “evidence blob”; or
- a new shared Progress/Journal Domain.

---

# 113. Pass-14 focused pressure tests

## PRG-PT-529 — Programme stores duplicate habit-occurrence state

**Scenario:** FP-008 stores `habit_completed=true` in Programmes independently from HJP occurrence truth.

**Expected invariants / analysis:** Reject competing authority. Programmes may store its own requirement-satisfaction decision/minimum provenance; HJP remains source owner for the occurrence.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-530 — Completed HJP occurrence automatically completes Programme

**Scenario:** Any `completed` occurrence linked to an activity clears the Programme requirement.

**Expected invariants / analysis:** Reject universal translation. ProgrammeVersion requirement/evidence rules decide whether this specific occurrence satisfies this specific activity.

**Disposition:** `PASS_REJECTED_UNIVERSAL_RULE`.

---

## PRG-PT-531 — Partial occurrence is treated as failure

**Scenario:** `partially_completed` causes a failed Programme day.

**Expected invariants / analysis:** Reject. Partial is truthful HJP state. Programme consequence is explicit and may remain incomplete/recoverable without punitive failure.

**Disposition:** `PASS`.

---

## PRG-PT-532 — Intentional skip is automatically exempt

**Scenario:** `skipped_intentionally` is translated to an exemption so completion denominator is reduced.

**Expected invariants / analysis:** Reject. Product says intentional skip does not equal failure, not that it equals exemption. Pass-9 exception authority remains explicit.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-533 — Missed habit causes enrolment failure

**Scenario:** One missed HJP occurrence automatically fails or resets Programme participation.

**Expected invariants / analysis:** Reject under compassionate consistency/recovery. Preserve history; Programme completion remains versioned and threshold-gated.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-534 — `not_applicable` is silently treated as complete

**Scenario:** HJP emits `not_applicable` and Programmes credits completion without an explicit rule.

**Expected invariants / analysis:** Reject. Source state is not Programme satisfaction. Conditional/exception semantics must govern.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-535 — Safety-blocked habit is counted as failure

**Scenario:** A Safety restriction produces `safety_blocked`; Programme marks non-compliance.

**Expected invariants / analysis:** Reject. Pass 13 governs current Safety; safety-blocked is not participant failure. Programme consequence requires explicit approved rule/alternative/exception.

**Disposition:** `PASS`.

---

## PRG-PT-536 — Later Safety clearance rewrites old safety-blocked occurrence

**Scenario:** Participant becomes cleared and the system changes old `safety_blocked` to `completed`.

**Expected invariants / analysis:** Reject history rewrite. Future activity may resume; historical non-performance remains truthful unless an actual source correction is warranted.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-537 — Participant-created habit with same name satisfies required habit

**Scenario:** Participant creates “Walk” and Programme automatically substitutes it for a named required approved habit “Walk”.

**Expected invariants / analysis:** Name equality is not governed equivalence. Require an explicit Programme acceptance/substitution rule.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-538 — Programme accepts an approved habit category

**Scenario:** ProgrammeVersion explicitly says any approved HJP habit in a bounded category may satisfy an activity.

**Expected invariants / analysis:** Permissible. HJP owns the chosen habit/occurrence; Programmes owns the category/evidence acceptance decision.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-539 — Practitioner-assigned habit automatically becomes Programme-required

**Scenario:** Practitioner assigns a habit and Programmes begins requiring it for completion without ProgrammeVersion authority.

**Expected invariants / analysis:** Reject. Professional assignment and Programme requirement are separate truths. A Programme consequence needs explicit Product/Programme policy.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-540 — Programme changes practitioner-assigned schedule

**Scenario:** Catch-up logic rewrites a practitioner-assigned habit frequency to make the Programme easier.

**Expected invariants / analysis:** Reject cross-domain/professional authority bypass. HJP/professional assignment rules own the habit schedule; Programme may adjust its own guidance/requirement consequence only.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-541 — Programme-relative habit follows Edition day

**Scenario:** A Nuwe Jy habit is configured relative to a shared Edition day.

**Expected invariants / analysis:** Valid. HJP may derive occurrence windows from the authoritative Programme/Edition anchor; the occurrence does not become Programme-owned.

**Disposition:** `PASS`.

---

## PRG-PT-542 — Late enrolment shifts programme-relative habit into a private 60-day calendar

**Scenario:** Late participant gets a new personal Day 1 and all habit schedules shift.

**Expected invariants / analysis:** Reject for scheduled Nuwe Jy. Pass-10/§21H late-enrolment semantics keep the shared Edition calendar; HJP schedule/recovery must compose with it rather than rewrite it.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-543 — Participant timezone changes near midnight

**Scenario:** Timezone change could cause one habit occurrence to appear twice or vanish.

**Expected invariants / analysis:** HJP must reconcile without duplicate completions and preserve historical explanation. Programmes consumes reconciled source evidence rather than calculating its own day.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-544 — Reminder delivery fails

**Scenario:** Provider never sends a habit reminder.

**Expected invariants / analysis:** Delivery failure is Communications/operations truth. It does not automatically mark HJP occurrence missed or Programme requirement failed.

**Disposition:** `PASS`.

---

## PRG-PT-545 — Reminder delivered twice

**Scenario:** Duplicate notification delivery occurs but participant completes the habit once.

**Expected invariants / analysis:** Duplicate reminder delivery must not duplicate occurrence/completion/Programme satisfaction. Source/action identities remain separate.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-546 — Enrolment pause automatically pauses every habit

**Scenario:** Pausing Programme Enrolment mutates all HJP habits to paused.

**Expected invariants / analysis:** Reject universal coupling. Enrolment pause, habit lifecycle and reminder controls are separate; explicit ProgrammeVersion/policy may request bounded effects without rewriting independent habits by assumption.

**Disposition:** `PASS_REJECTED_UNIVERSAL_RULE`.

---

## PRG-PT-547 — Habit pause pauses Programme Enrolment

**Scenario:** Participant pauses one habit and Programme is marked paused.

**Expected invariants / analysis:** Reject. HJP habit lifecycle cannot manufacture Programmes Enrolment lifecycle.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-548 — Required private reflection completion is checked by reading prose

**Scenario:** Facilitator/admin reads journal body and decides whether it is “good enough” to count.

**Expected invariants / analysis:** Reject private-by-default violation and subjective shadow authority. Use only approved minimum evidence; ordinary staff cannot browse journals.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-549 — Reflection existence is minimum Programme evidence

**Scenario:** An approved ProgrammeVersion says a private reflection response must exist, but content quality is not evaluated.

**Expected invariants / analysis:** Permissible if the concrete Product/JIT completion contract approves that evidence. HJP retains content; Programmes stores only minimum satisfaction provenance.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-550 — Programme requires minimum journal word count

**Scenario:** Completion requires 250 words in a private journal entry.

**Expected invariants / analysis:** Not authorised as a universal rule. It would require explicit Product/Programme justification and creates unnecessary content inspection. Do not infer it from “reflection required.”

**Disposition:** `DEFER_YAGNI / PRODUCT_RULE_REQUIRED_IF_INTRODUCED`.

---

## PRG-PT-551 — Programme sentiment-scores reflection

**Scenario:** AI/NLP checks whether participant expressed sufficient positivity/accountability to count completion.

**Expected invariants / analysis:** Reject. AI journal assistance is deferred and non-diagnostic; sentiment is neither source truth nor authorised completion authority.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-552 — Private reflection is automatically stored as full journal

**Scenario:** Every Nuwe Jy optional private reflection creates a journal entry with full journal retention/sharing semantics.

**Expected invariants / analysis:** Reject automatic expansion. Product/Roadmap keep basic check-ins/reflection distinct from richer journal system. Choose the smallest business meaning in JIT.

**Disposition:** `PASS_REJECTED_UNIVERSAL_RULE`.

---

## PRG-PT-553 — Structured hunger marker is hidden only in journal text

**Scenario:** A safety/plan-relevant structured hunger response is persisted only inside a journal body.

**Expected invariants / analysis:** Reject. Structured health/safety meaning routes to Health Records/Safety as applicable; private narrative can remain HJP.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-554 — Food/hunger reflective narrative remains non-clinical

**Scenario:** Participant writes a general reflective narrative with no governed health/safety consequence.

**Expected invariants / analysis:** HJP may own it as reflective journal/progress truth. Do not manufacture a Health record merely from journal type/name.

**Disposition:** `PASS`.

---

## PRG-PT-555 — Journal contains urgent free text

**Scenario:** Participant writes an urgent medical disclosure in free text.

**Expected invariants / analysis:** The platform must not claim continuous monitoring. Do not make hidden AI/facilitator review the MVP safety path. Structured help/safety surfaces remain the governed route; exact urgent wording stays `OQ-008`.

**Disposition:** `PASS`.

---

## PRG-PT-556 — Future AI journal detector is introduced silently

**Scenario:** Background model scans every journal and opens safety cases without disclosure/staffed escalation proof.

**Expected invariants / analysis:** Reject. Product explicitly requires disclosure, expert approval, tested escalation capacity and staffed response for any later assistive detection.

**Disposition:** `PASS_REJECTED_MODEL / FUTURE_GOVERNANCE_REQUIRED`.

---

## PRG-PT-557 — Participant shares one journal entry with practitioner

**Scenario:** Entry-specific share is granted to an authorised practitioner with scope/purpose/expiry.

**Expected invariants / analysis:** Valid. HJP owns entry/share state; Privacy supplies processing/share authority; Professional Care relationship/scope must separately be valid where required.

**Disposition:** `PASS`.

---

## PRG-PT-558 — Sharing entry proves professional review complete

**Scenario:** Programmes clears a professional-review requirement because a journal entry was shared.

**Expected invariants / analysis:** Reject. Share/access, case/review, outcome, Safety consequence and Programme consequence are distinct.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-559 — Practitioner copies shared entry into professional record

**Scenario:** A selected journal entry legitimately enters a professional record before the HJP share is later revoked.

**Expected invariants / analysis:** HJP share revocation ends future HJP access but does not silently delete an independently governed professional record. Final disposition remains `OQ-033`/retention authority.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-560 — Accountability partner gains full journal access

**Scenario:** Sharing a habit milestone exposes journal history or health data to the accountability partner.

**Expected invariants / analysis:** Reject. Accountability sharing is selected/scoped; journals/health are excluded by default.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-561 — Accountability partner edits completion history

**Scenario:** Partner/facilitator marks a habit occurrence complete for participant.

**Expected invariants / analysis:** Reject. Recipient cannot alter participant history. Any future delegated logging capability would require explicit Product authority and owner-safe auditing.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-562 — Journal share expires while Programme remains active

**Scenario:** Practitioner/facilitator can no longer see the entry after expiry, but Programme satisfaction had already been validly recorded.

**Expected invariants / analysis:** Access expiry does not silently erase historical Programme satisfaction. Programmes retains only lawful minimum provenance; current access remains revoked.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-563 — Participant deletes private journal after completion

**Scenario:** Journal content/attachment is deleted after its existence had validly satisfied a Programme requirement.

**Expected invariants / analysis:** Do not retain a hidden content copy. Whether minimum Programme satisfaction provenance may remain or must be de-linked is governed by `OQ-018`/retention/deletion contracts. Preserve explicit reconciliation rather than assume either universal erasure or universal retention.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-564 — Programme copies attachment for audit

**Scenario:** Private journal photo/file is copied to Programmes so completion can later be proven.

**Expected invariants / analysis:** Reject duplication. HJP/Privacy lifecycle owns the attachment; Programmes should retain minimum approved provenance only.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-565 — Health document uploaded through journal attachment

**Scenario:** Participant uploads a lab report or detailed health document into a reflection to satisfy Programme work.

**Expected invariants / analysis:** Do not treat journal as a Health Records bypass. If health evidence is genuinely required, route it through the governed Health/document path; Programme should not require public/private reflective disclosure as a workaround.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-566 — Journal deletion leaves search/cache derivative

**Scenario:** Entry body is deleted but extracted text/search index/preview remains accessible.

**Expected invariants / analysis:** Reject incomplete deletion under DEC-227/228. Exact mechanisms stay behind `OQ-018`/Privacy JIT, but product semantics require derivative cleanup.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-567 — HJP corrects duplicate occurrence after Programme satisfaction

**Scenario:** HJP determines one of two recorded completions was a duplicate and corrects source truth.

**Expected invariants / analysis:** HJP corrects its occurrence; Programmes re-evaluates its satisfaction if material. Neither owner silently rewrites the other's history.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-568 — HJP correction happens after certificate award

**Scenario:** Corrected occurrence means original completion basis may no longer have been valid.

**Expected invariants / analysis:** Reconcile source and Programme evidence, but post-award outcome/certificate consequence remains existing `PRG-GAP-002`; do not invent revocation policy here.

**Disposition:** `PASS_WITH_EXISTING_GAP`.

---

## PRG-PT-569 — Admin “fixes” habit by overwriting occurrence history

**Scenario:** Support/admin changes participant occurrence state without bounded correction reason/provenance.

**Expected invariants / analysis:** Reject. Product forbids silent staff history alteration. HJP correction must be explicit/auditable; Programme admin cannot use a shadow mark-complete route.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-570 — Duplicate habit completion submission

**Scenario:** Double-click/retry/reconnect sends the same completion twice.

**Expected invariants / analysis:** One governed occurrence effect only; duplicate delivery cannot create two completions or two Programme satisfaction effects. Exact idempotency mechanics remain JIT proof.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-571 — Offline/late occurrence arrives after window evaluation

**Scenario:** Participant genuinely completed inside an allowed window, but evidence is synchronised later.

**Expected invariants / analysis:** JIT must distinguish source/effective occurrence timing from sync/processing time sufficiently to avoid fabricating a miss merely because transport was delayed. Exact offline support is not promised here; if unsupported, UI must not imply otherwise.

**Disposition:** `PASS_WITH_JIT_BOUNDARY`.

---

## PRG-PT-572 — Share/revoke race

**Scenario:** Practitioner opens an entry while participant revokes sharing concurrently.

**Expected invariants / analysis:** Current future access resolves from authoritative share/consent/relationship state; stale session/cache cannot extend access. Already-lawful professional-copy consequences remain separate.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-573 — Analytics says participant is highly consistent

**Scenario:** Derived analytics score conflicts with HJP occurrence history and Programmes uses the score to award completion.

**Expected invariants / analysis:** Reject. Analytics is derived; HJP source truth and Programme rules remain authoritative.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-574 — Journal text copied into analytics feature store

**Scenario:** Reflection prose is duplicated to support future engagement prediction.

**Expected invariants / analysis:** Reject under Product analytics/privacy boundaries. Journal text is excluded; a future new purpose would require explicit governance rather than silent reuse.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-575 — Completion requires public/community sharing of reflection

**Scenario:** Participant must publish a journal/reflection excerpt to cohort Community to earn completion.

**Expected invariants / analysis:** Reject as a default completion mechanism. Pass 12 prohibits sensitive disclosure as the price of completion; journal privacy is private-by-default. Any safe optional participant-controlled sharing remains separate.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-576 — Basic Nuwe Jy reflection forces OQ-018 private-journal implementation

**Scenario:** FP-008 implementer claims every reflection/check-in requires full journal encryption, attachment, practitioner-sharing and retention machinery before Programme work can proceed.

**Expected invariants / analysis:** Reject over-scope. Roadmap deliberately prevents basic progress/feedback from becoming a journal system by accident. Full private journals/richer reflective practice belong to FP-014 behind `OQ-018`; use the smallest approved FP-008 evidence model.

**Disposition:** `PASS_REJECTED_MODEL`.

---

# 114. Pass-14 gap adjudication

## Programme ↔ HJP source-evidence seam — sufficiently bounded for later JIT

The owner-safe path is:

```text
ProgrammeVersion defines activity / requirement / accepted evidence meaning
        ↓
HJP records participant habit/reflection/journal source truth
        ↓
Programmes consumes minimum governed evidence
        ↓
Programmes records requirement-satisfaction / completion consequence
```

This model preserves private-source ownership while allowing Programmes to evaluate its own rules.

No new `PRG-GAP-012` is justified merely because the exact evidence threshold is still gated by `OQ-019` / `OQ-025`.

## Basic private reflection versus full journal — Roadmap already provides the YAGNI boundary

FP-008 may use approved habit/reflection/check-in evidence without implementing the complete private-journal subsystem. Private journals/richer reflective practice are an FP-014 outcome and `OQ-018` applies when that capability enters scope.

This is not a Product contradiction; it is deliberate sequencing.

## Journal lifecycle and professional-copy boundary — existing gates remain correct

The concrete encryption/retention/export/deletion/professional-copy rules remain governed by:

- `OQ-018` — journal encryption/field policy/retention/export/deletion/professional handling;
- `OQ-029` — record-category retention durations/owners/actions;
- `OQ-032` — export/deletion operation contracts; and
- `OQ-033` — professional record authority/disposition.

Pass 14 does not need a new privacy or Professional Care Domain seam.

## Reminder boundary — existing gate remains correct

Communications owns notification/reminder channel-category preferences, quiet-hours/caps and delivery lifecycle under current Domain Law; HJP/Programmes may supply the originating habit/Programme context without becoming delivery authority. Exact delivery architecture/operations remain `OQ-017` / `OQ-036` as applicable.

No Programme/HJP queue/provider design is selected here.

## Existing-gap interactions

- `PRG-GAP-002` remains open for post-award corrected completion/certificate consequences. Pass 14 adds HJP source correction as another possible trigger but does not settle the Product policy.
- `PRG-GAP-009` remains narrowed: staff/operator correction cannot become generic habit/journal mark-complete, waiver or private-content browsing authority.
- `PRG-GAP-011` remains unchanged: withdrawn required Programme content cannot be repaired by inventing a journal/habit substitute.
- `PRG-GAP-006` remains compatible: private journal/reflection truth cannot be routed through Community to manufacture Programme evidence.

## No new Product / Architecture / Domain gap promoted

Current Product and Domain authority already separates Programme meaning, HJP source truth, Privacy lifecycle authority, Safety/Health meaning and Professional Care copies. Exact remaining values/operations are deliberately assigned to existing OQs.

No new Domain, `PRG-GAP-###`, `PRG-UPD-###`, journal-scoring authority, generic evidence Domain or cross-domain Progress authority is justified.

---

# 115. Pass-14 refinements to the working synthesis

## PRG-REF-141 — Programme habit/reflection requirement meaning and HJP source truth remain separate

Programmes defines the obligation and accepts evidence; HJP owns the participant occurrence/reflection/journal fact.

## PRG-REF-142 — Private Programme evidence should be content-minimised

Where a reflection/journal-linked activity may satisfy a requirement, Programmes should consume the minimum governed source fact/provenance rather than journal text/attachments.

## PRG-REF-143 — Required private reflection cannot depend on ordinary staff reading prose

Privacy-by-default and role boundaries remain intact even when the activity is completion-relevant.

## PRG-REF-144 — Reflection UI does not imply Journal Resource semantics

Choose owner/record type by business meaning; basic Nuwe Jy reflection/check-in must not automatically create the richer FP-014 journal subsystem.

## PRG-REF-145 — HJP occurrence states are never universal Programme outcomes

`completed`, partial, skip, missed, not-applicable and safety-blocked each retain source meaning; Programme consequence is explicit rule/exception logic.

## PRG-REF-146 — Participant-created habits require explicit Programme acceptance or substitution

Similarity is not equivalence. Generic habit-matching remains unjustified.

## PRG-REF-147 — Practitioner-assigned habit occurrence does not transfer professional authority to Programmes

Professional instruction/outcome and Programme satisfaction remain separate owner decisions.

## PRG-REF-148 — Programme-relative habit schedules consume authoritative Programme timing

They do not create a private shifted Edition calendar or rewrite Programme release history.

## PRG-REF-149 — HJP owns timezone/window reconciliation for occurrences

Programmes consumes reconciled source evidence and must not calculate a competing habit day.

## PRG-REF-150 — Habit pause, Enrolment pause and reminder pause remain independent lifecycle dimensions

Any coordination is an explicit consequence, not shared state.

## PRG-REF-151 — Reminder delivery is not adherence evidence

Provider success/failure cannot manufacture completed/missed habit or Programme failure.

## PRG-REF-152 — Habit notes and journal prose are not hidden clinical intake

Structured health/safety meaning routes to Health Records/Safety; reflective narrative remains HJP when non-clinical.

## PRG-REF-153 — Journal share, professional record and professional review are different truths

Sharing provides bounded access only; it does not prove review, outcome, clearance or Programme satisfaction.

## PRG-REF-154 — Share revocation ends future access without granting cross-domain rewrite authority

HJP/Privacy revoke access; historical source/Programme/professional records follow their own governed lifecycle.

## PRG-REF-155 — Programme provenance must survive without covertly retaining journal content

Use minimum lawful evidence; final retention/de-link requirements remain behind `OQ-018` and lifecycle gates.

## PRG-REF-156 — Journal deletion and Programme participation are distinct lifecycle questions

Neither universal historical erasure nor universal retention is inferred before the governing retention/deletion contract is approved.

## PRG-REF-157 — Free-text journal monitoring remains outside MVP

Safety uses structured pathways/explicit help actions; any future assistive detection requires separate governance, capacity and proof.

## PRG-REF-158 — HJP source corrections trigger explicit Programme reconciliation when material

No silent cross-domain rewrite; post-award consequence remains `PRG-GAP-002`.

## PRG-REF-159 — Analytics remains event/aggregate-only for journal/habit use

Journal text is excluded and derived scores cannot override HJP or Programme authority.

## PRG-REF-160 — Duplicate/reordered/private-access observations reconcile from owner authority

Retries, reconnects, timezone changes and share/revoke races must not duplicate effects or extend stale access; exact mechanics remain JIT proof.

---

# 116. Pass-14 anti-journal-engine / YAGNI outcome

Pass 14 explicitly rejects:

- a Programme-owned duplicate habit-occurrence state;
- a generic rule that any completed habit occurrence completes the Programme activity;
- treating intentional skip as exemption or miss as failure by default;
- safety-blocked as participant failure;
- participant-created habit name matching as automatic equivalence;
- Programme mutation of practitioner-assigned habit instructions;
- a private shifted Nuwe Jy habit calendar for late enrolment;
- reminder delivery as adherence or completion authority;
- automatic cross-pausing of Habit, Enrolment and reminder lifecycles;
- ordinary staff reading private journal prose to grade completion;
- minimum word-count, sentiment or “quality” scoring as inferred reflection semantics;
- automatically creating a full journal record for every lightweight reflection/check-in;
- using journals as a hidden Health Records intake path;
- free-text journal monitoring/AI triage in MVP;
- sharing a journal entry as proof of completed professional review;
- accountability sharing as mutation or journal/health access authority;
- retaining copied journal text/attachments inside Programmes for audit;
- using journal attachments as a Health-document bypass;
- Analytics feature stores containing journal prose;
- Community publication as the default price of reflection completion;
- a generic habit equivalence engine;
- a generic reflection scoring/rubric engine;
- a universal evidence-blob Domain;
- a new shared Progress Domain; and
- implementing FP-014 private-journal machinery merely because FP-008 has a reflection control.

The simplest correct model remains explicit Programme activity/evidence meaning over HJP-owned source truth, with minimum-data provenance and existing lifecycle gates.

---

# 117. Pass-14 disposition

**Outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Passes 1–13 remain accepted/working-locked and Pass 14 does not reopen them.
2. Programmes owns habit/reflection/journal-linked activity meaning and requirement satisfaction; HJP owns participant habit/journal/reflection source truth.
3. A Programme prompt, participant response and Programme satisfaction decision are distinct truths even on one UI surface.
4. Programmes should consume minimum governed evidence for private reflection/journal-linked requirements and should not copy journal prose or attachments.
5. A required private reflection cannot depend on routine facilitator/admin/moderator/support reading of private prose.
6. Basic Nuwe Jy reflection/check-in does not automatically become the richer FP-014 private-journal subsystem.
7. HJP occurrence states retain source meaning and never universally map to Programme completion/failure/exemption/substitution.
8. Intentional skip is not failure but is also not automatic exemption; missed is not automatic Programme failure; safety-blocked is not participant failure.
9. Participant-created habits satisfy named Programme requirements only under explicit Programme acceptance/substitution policy.
10. Practitioner-assigned habits remain distinguishable; HJP occurrence, Professional Care instruction/outcome and Programme satisfaction remain separate.
11. Programme-relative habit schedules consume Programme/Edition timing but do not rewrite or privately shift the shared Nuwe Jy calendar.
12. HJP owns occurrence-window/timezone reconciliation; timezone change cannot duplicate completion/evidence.
13. Habit pause, Programme Enrolment pause and reminder pause are independent lifecycle dimensions.
14. Communications reminder delivery/failure is not habit occurrence or Programme adherence authority.
15. Optional habit notes/journal prose do not become hidden completion or clinical evidence by default.
16. Structured health/safety meaning captured alongside reflection routes to Health Records/Safety; reflective narrative may remain HJP.
17. Private journals cannot be used as disguised mandatory diagnosis/medication/trauma/weight disclosure to earn Programme completion.
18. Journal/accountability sharing is scoped access only; recipients do not gain mutation, Programme-adjudication or general journal/health authority.
19. Journal sharing does not prove practitioner review; share, professional case/outcome, Safety/Plan consequence and Programme consequence remain distinct.
20. Share expiry/revocation ends future access but does not silently rewrite independent HJP/Programme/professional history.
21. Programme provenance must not defeat journal deletion by retaining hidden copies of text/attachments.
22. Whether minimum satisfaction provenance remains after journal deletion/de-linking is governed by `OQ-018` / lifecycle gates, not assumed universally here.
23. Journal attachments remain HJP/private assets and cannot be used as a workaround for Health/Professional document authority.
24. Free-text journal monitoring/AI triage remains outside MVP; structured safety/help pathways remain the governed route.
25. HJP source correction triggers explicit Programme reconciliation when material; post-award outcome/certificate consequence remains `PRG-GAP-002`.
26. Analytics may use governed behavioural events/aggregates but not journal text and cannot override source/completion/Safety truth.
27. Duplicate occurrence/check-in submissions, timezone changes and share/revoke races require idempotent/current-authority reconciliation at JIT/proof.
28. `OQ-017`, `OQ-018`, `OQ-019`, `OQ-025`, `OQ-029`, `OQ-032` and `OQ-033` remain the correct existing gates as applicable; no new upstream gap is justified.
29. No new Product, Architecture or Domain amendment is justified by this pass.
30. Generic habit-equivalence, reflection-scoring, evidence-blob or Programme-owned journal/progress engines remain `DEFER_YAGNI` / rejected.

**Pass hard stop:** Pass 15 — translation / version-localisation semantics — has not started. Do not pull bilingual content-version, translation fallback, source-locale, approval or delivery-snapshot detail into this Pass-14 candidate.

**Broad discovery remains unfrozen.** Later communications, operator correction, concurrency/retry, cancellation/transfer, historical reproducibility, analytics, FP-014 second-lens and final adversarial-convergence passes remain separate.
