# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.14.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.14.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 13 — Safety / clinical / professional-boundary semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.13.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused Safety / clinical / Professional Care seam pass while preserving Passes 1–12 and their accepted working-lock boundaries.

> This is an append-only semantic successor. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work, approved Feature Pack/JIT contracts, clinical authority, Safety & Eligibility authority, Health Records authority, Plans & Nutrition authority or Professional Care authority.

> Nuwe Jy remains a configured Programme composition over shared platform authorities. Do not create a Nuwe Jy-specific safety engine, duplicate health record, shadow professional case, facilitator clinical workflow, or Programme-owned eligibility state merely because safety affects programme participation.

---

# 102. Accepted working-lock status entering Pass 13

The user explicitly accepted Pass 12 and instructed the stream to continue with the next pass.

Therefore Passes 1–12 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, named authority gates, deferred items and later explicit refinements.

Pass 13 inherits without reopening:

- ProgrammeVersion owns programme/activity requirement, progression, exception and completion meaning;
- source Domains retain ownership of the underlying facts that Programmes consumes;
- Safety & Eligibility owns safety/eligibility outcomes, restrictions, cases, clearance and governed clinical overrides;
- Health Records owns health/lifestyle facts and provenance, not safety decisions;
- Plans & Nutrition owns plan generation/version/current-use truth and must consume current Safety authority;
- Professional Care owns practitioner relationship/review/case/outcome truth but does not own final Safety or Plan authority;
- `required_for_safety` is a Programme requirement type, not a transfer of Safety authority;
- `safety_blocked`, exempt, substituted, skipped and not-applicable states do not fabricate completion;
- compassionate recovery cannot bypass Safety, extend Entitlements or silently waive safety-required work;
- Community, live/replay and other source-Domain states do not become clinical truth;
- facilitator/support/operator authority remains bounded and cannot become generic completion, waiver or source-evidence authority;
- exact Nuwe Jy safety routing, required activities and completion consequences remain gated by `OQ-025` and applicable clinical/Product authority.

---

# 103. Pass 13 — Safety / clinical / professional-boundary semantics

## 103.1 Scope hard stop

This pass answers only:

1. how core Safety/eligibility truth differs from Nuwe Jy programme-route truth;
2. what Programmes may store/configure when Safety determines which programme path is currently permitted;
3. why `required_for_safety` does not make Programmes the Safety owner;
4. what essential Nuwe Jy safety screening means at the Programme boundary without pulling full plan intake forward;
5. how a material Safety change during an active Enrolment affects future programme guidance while preserving history;
6. how `safety_blocked` source/activity state composes with Programme requirement and exception semantics;
7. how `professional_review_required` routes through Professional Care without creating a Programme-owned clinical case;
8. how a practitioner outcome reaches Safety and Plans through owner-mediated commands rather than direct cross-domain mutation;
9. how facilitator, moderator, live-host, support-agent and programme-admin roles remain non-clinical by default;
10. how health-sensitive daily/milestone check-ins route by business meaning rather than by screen ownership;
11. how urgent-help information can be surfaced without implying continuous clinical monitoring or guaranteed follow-up;
12. how insufficient information, safe modification and General Wellness paths avoid punitive Programme failure semantics;
13. how current Safety changes interact with recovery, catch-up, completion and certificate history;
14. how minimum-data access prevents Programmes/facilitators from copying diagnoses, medication, plans, journals or professional records; and
15. whether any new Product, Architecture or Domain gap is required before later FP-008 JIT.

This pass deliberately does **not** decide:

- the exact low/moderate/high clinical eligibility matrix — `OQ-005`;
- exact country-specific emergency/urgent-help wording, acknowledgements or escalation boundaries — `OQ-008`;
- exact Nuwe Jy safety routing, milestone check-ins, required activities or completion rules — `OQ-025`;
- exact Programme completion thresholds — `OQ-019`;
- final professional-record authority, participant access, addendum or disposition rules — `OQ-033`;
- practitioner-service commercial promise/capacity or FP-012 activation;
- exact clinical override protocols beyond already-locked Product Law;
- exact health/safety/Professional Care Resources, actions, schemas, queues, PubSub topics or UI;
- exact participant-specific clinical treatment or diagnosis;
- a generic clinical workflow engine inside Programmes;
- a generic medical triage chatbot or continuous-monitoring service; or
- journals/habits edge semantics reserved for Pass 14.

---

## 103.2 Pass-13 authority evidence

### PRG-EV-163 — Live authority baseline reconfirmed

Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413`. README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` continue to route Product Law v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and Platform Operating Model v1.0.1 as current authority. These Programmes/Learning ledgers remain working/non-authoritative.

### PRG-EV-164 — Health fact, Safety decision and Programme consequence have different owners

Current Domain Law assigns Health Records the participant health/lifestyle facts and provenance; Safety & Eligibility the eligibility outcomes, restrictions, cases, clearance and governed overrides; and Programmes & Challenges the programme/challenge configuration, enrolment, progression and completion meaning.

Programmes explicitly does not own the central Safety engine.

### PRG-EV-165 — Safety authority is current, deterministic and fail-closed

Safety & Eligibility owns current safety/eligibility authority and may block or restrict automated pathways. Unsafe or missing critical information must fail closed to an approved non-personalised/review pathway, and safety revocation must invalidate dependent plan authority rather than waiting for stale cache expiry.

### PRG-EV-166 — Core eligibility outcomes are Safety-owned

`DEC-078` locks the core Safety eligibility outcomes:

```text
eligible_automated
general_wellness_only
professional_review_required
insufficient_information
```

`OQ-005` remains a clinical-review gate for the exact risk-routing matrix. This pass cannot infer the clinical mapping.

### PRG-EV-167 — Nuwe Jy has a distinct Product-facing participation-route vocabulary

Product §21H.12 and `DEC-209` define Nuwe Jy challenge outcomes including:

```text
eligible_for_full_challenge
eligible_with_safe_modifications
general_wellness_components_only
professional_review_required
insufficient_information
```

These are programme/challenge participation-route outcomes. The overlapping labels do not prove that the entire Nuwe Jy route vocabulary is identical to the core Safety eligibility vocabulary.

### PRG-EV-168 — Exact mapping between Safety eligibility and Nuwe Jy route remains gated

`OQ-025` is `CLINICAL / PRODUCT REVIEW` and requires approval of exact challenge safety routing, milestone check-ins, required activities and completion rules. Roadmap classifies `OQ-025` as `BLOCKS_THIS_FP` for FP-008 activation.

Therefore this Pre-JIT pass may protect the authority boundary and route shape but may not manufacture a one-to-one mapping between core eligibility outcomes and Nuwe Jy route outcomes.

### PRG-EV-169 — Progressive Nuwe Jy onboarding does not equal full plan intake

`DEC-208` and Product §21H.12 require account, age confirmation, terms/privacy, challenge consent/boundaries, essential safety screening, preferred language and temperament provenance before participation. Product explicitly keeps the deeper personalised-plan health intake separate.

Therefore FP-008 cannot require the full personalised-plan intake merely because Safety participates in Nuwe Jy routing unless the concrete approved pathway requires it.

### PRG-EV-170 — Approved safe/general-wellness components may remain available when personalised nutrition is blocked

Product §21H.12 states that approved education, faith, community and General Wellness may remain available where personalised nutrition is blocked if Safety permits.

This proves that `professional_review_required`, General Wellness routing or a plan restriction does not automatically mean every Programme surface must disappear.

### PRG-EV-171 — Current Safety outranks temperament and Programme convenience

Domain Law states that medical/clinical safety outranks temperament, convenience and commercial entitlement. Product §21H.7 similarly says temperament never changes safety rules or core programme requirements.

A recovery recommendation, facilitator preference, completion target or temperament adaptation therefore cannot override current Safety authority.

### PRG-EV-172 — Plans remain centrally owned and Nuwe Jy references them

`DEC-216` and Product §21H.19 require the platform's authoritative Safety and Plan system and prohibit a separate Nuwe Jy nutrition engine. Nuwe Jy references the current authoritative approved plan; plan correction, withdrawal or safety pause changes dependent guidance.

Programmes must therefore not copy mutable plan content/state into Programme progress and then treat the copy as current plan authority.

### PRG-EV-173 — Safety changes are allowed to have programme consequences without transferring ownership

Programmes & Challenges depends on Safety & Eligibility for activity/path restrictions. Safety can change which path or activity is permitted; Programmes owns the resulting programme guidance/progression consequence under its versioned rules.

A dependency/reference does not transfer mutation authority.

### PRG-EV-174 — Professional review is a separate relationship/case lifecycle

Professional Care owns participant-practitioner relationship metadata, professional review/case lifecycle, structured outcomes and professional capacity. Practitioner role alone never grants participant-record access; access requires consent, active relationship, scope, expiry and audit.

A Programme Enrolment, Community membership, live attendance or support contact does not create a Professional Care relationship.

### PRG-EV-175 — Practitioner outcomes route back through Safety and Plans owners

`DEC-091` requires scoped, time-bound, audited clinical overrides without replacing the original automated outcome. `DEC-092` constrains high-risk downgrade approval. `DEC-093` records structured professional outcomes.

Domain Law requires Professional Care to request Safety override/clearance through Safety and practitioner-authored Plan changes through Plans. Professional Care does not directly rewrite either owner.

### PRG-EV-176 — Programme/facilitator roles are deliberately non-clinical by default

Product §21H.16 allows scoped challenge/programme roles but limits facilitators to appropriate non-clinical information such as display name/roster, enrolment state, broad participation state, milestones and participant-submitted facilitator questions. Clinical access is a separate consented role.

Facilitators do not automatically see diagnoses, medication, assessment answers, plans, journals, weight, laboratory data or professional records.

### PRG-EV-177 — Check-in business meaning determines owner

Product §21H.17 permits lightweight daily interactions and deeper versioned milestone check-ins while keeping journals separate. Domain Law gives HJP lightweight programme check-in responses not owned as health facts and requires health-sensitive responses that materially affect safety to route to Health Records/Safety.

A single check-in screen therefore may orchestrate multiple owners; the UI does not decide authority.

### PRG-EV-178 — Support routing includes Safety but does not imply monitoring

`DEC-215` and Product §21H.18 provide deterministic self-service/recovery/support/professional-review/safety outcomes. Clinical concerns use Safety; the programme does not imply unlimited coaching or guaranteed clinical follow-up.

Safety Domain policy also says urgent-help messaging never implies continuous monitoring.

### PRG-EV-179 — Urgent-help wording remains a clinical/legal gate

`OQ-008` requires country-specific urgent-help wording, acknowledgements and escalation boundaries. Programme discovery may preserve the fail-closed routing boundary but cannot author that wording or promise.

### PRG-EV-180 — Completion/certification is not clinical certification

`DEC-217` and Product §21H.20 say certificates state participation/completion only and never claim medical competence, guaranteed transformation or weight loss. Safety pathway, professional review or completion history therefore cannot be represented as a clinical clearance certificate.

### PRG-EV-181 — Existing gates already own the unresolved concrete decisions

Current authority already routes:

- `OQ-005` — exact clinical eligibility matrix;
- `OQ-008` — urgent-help wording/acknowledgement/escalation boundaries;
- `OQ-019` — programme-specific completion metrics;
- `OQ-025` — exact Nuwe Jy safety routing, milestone check-ins, required activities and completion rules;
- `OQ-033` — professional record authority/access/addendum/disposition;
- `OQ-026` — Nuwe Jy operational ownership/capacity where facilitator/support/clinical ownership is operationally material.

The owner seams are already explicit enough that Pass 13 does not need a new Product, Architecture or Domain identifier merely to restate them.

---

# 104. Pass-13 semantic model

These are working semantic conclusions, not Resource/schema prescriptions.

## 104.1 Keep core Safety eligibility and Nuwe Jy route as separate semantic dimensions

Do not collapse these two vocabularies:

```text
CORE SAFETY / ELIGIBILITY AUTHORITY
eligible_automated
general_wellness_only
professional_review_required
insufficient_information

NUWE JY PARTICIPATION ROUTE
eligible_for_full_challenge
eligible_with_safe_modifications
general_wellness_components_only
professional_review_required
insufficient_information
```

The exact approved mapping belongs to `OQ-025` and applicable clinical authority.

A later implementation may make the mapping mechanically simple, but it must not assume semantic identity merely because two labels overlap.

## 104.2 Programme safety configuration is routing/configuration, not clinical judgement

Programmes may own versioned configuration such as:

- which approved Nuwe Jy route is allowed for a given Safety-owned outcome/context;
- which Programme activities/paths are available or blocked under that approved route;
- which Programme requirements need current Safety confirmation;
- what Programme consequence follows a changed route, subject to approved Product/clinical rules.

Programmes must not own or recompute:

- diagnoses;
- clinical risk classification;
- eligibility evaluation;
- Safety Case state;
- clinical override authority; or
- professional review outcome.

## 104.3 `required_for_safety` is programme meaning, not Safety authority

A ProgrammeVersion can classify an activity as `required_for_safety`.

That classification answers a programme question: this activity/acknowledgement must satisfy a safety-related programme requirement under the approved contract.

It does not authorise Programmes to:

- decide clinical eligibility;
- mark a participant medically safe;
- waive a Safety restriction;
- reinterpret a health fact;
- create a clinical override; or
- use a Programme checkbox as a substitute for Safety authority.

## 104.4 Essential safety screening is a bounded participation prerequisite

For Nuwe Jy, essential safety screening belongs before participation under Product Law. The deeper personalised-plan intake remains separate.

Therefore the safe model is:

```text
minimum governed Nuwe Jy onboarding
        ↓
Safety-owned evaluation / current authority
        ↓
approved Nuwe Jy route
        ↓
Programme participation under that route
```

Do not force a participant through unrelated plan-intake depth simply to satisfy programme architecture convenience.

## 104.5 Safety route changes constrain future behaviour but preserve history

When authoritative Safety changes during an active Enrolment:

- historical health facts remain Health Records truth;
- historical Safety outcomes/overrides remain auditable;
- accepted Programme participation/evidence remains historical truth unless a separately governed correction invalidates it;
- future Programme guidance must respect the new current Safety authority;
- unsafe future actions/paths must stop or change as the approved route requires;
- Plan-dependent guidance must re-read the current authoritative Plan/Safety state;
- the Enrolment is not silently deleted, restarted, failed, completed or abandoned.

Any additional Enrolment/completion consequence must come from the approved ProgrammeVersion / `OQ-019` / `OQ-025` contract.

## 104.6 `safety_blocked` is truthful source/activity state, not automatic completion consequence

When HJP or another owner records an activity occurrence as safety-blocked, Programmes may consume that fact.

It must not silently translate it into:

- completed;
- failed;
- exempt;
- not applicable;
- substituted; or
- abandoned.

Pass-9 exception/substitution rules and the concrete Programme contract govern any resulting requirement consequence.

## 104.7 `insufficient_information` is not participant misconduct

Missing safety-critical information must fail closed for the affected safety-sensitive route.

It does not prove that the participant:

- failed the Programme;
- refused care;
- abandoned the Enrolment;
- deserves a punitive progress reset; or
- completed a safety requirement.

The Programme may present the governed next action needed to establish current authority without shaming or fabricating progress.

## 104.8 Safe modification must be governed, not facilitator improvisation

`eligible_with_safe_modifications` cannot mean “a facilitator edits the programme until it looks safe.”

A safe-modification route must be bounded by approved clinical/Product routing and Programme configuration. If the modification affects a personalised Plan, Plans owns the resulting Plan version. If it changes Safety authority, Safety owns the decision.

Programme facilitators may communicate or guide within the approved route but do not manufacture clinical modifications.

## 104.9 General Wellness path is not failed full-challenge participation

Where Product permits `general_wellness_components_only`, approved education, faith, community and General Wellness components may remain available if Safety permits.

This is an approved route, not a dishonest `completed` full challenge and not automatically a Programme failure.

The concrete completion/outcome meaning for that route remains `OQ-019` / `OQ-025` work.

## 104.10 Professional review route creates no Programme-owned clinical case

When the governed route is `professional_review_required`:

```text
Safety owns the current restriction/routing authority
        ↓
Professional Care owns any actual consented review relationship/case
        ↓
professional outcome requests owner-mediated Safety/Plan consequence
        ↓
Programmes consumes the resulting current authority
```

Programmes may know that the participant is awaiting an approved route decision only to the minimum extent needed for participation guidance. It does not own practitioner notes, diagnosis, professional record or clearance.

## 104.11 A recommendation for professional review is not a completed professional review

Support routing may recommend professional review. That recommendation does not prove:

- an active practitioner relationship;
- professional acceptance/capacity;
- consent to record access;
- a completed review;
- a Safety clearance; or
- a Plan modification.

Keep referral/recommendation, relationship/case, professional outcome, Safety consequence and Programme consequence separate.

## 104.12 Facilitator/support access is minimum and non-clinical

Programme/facilitator dashboards may use broad non-clinical state needed to operate the cohort.

Do not expose health or professional detail merely because it would make facilitation easier. If a facilitator also holds a separately authorised clinical role, access follows that clinical role/relationship/purpose — not the facilitator role.

## 104.13 One check-in experience may create several owner records

A milestone/check-in interaction may contain:

- ordinary manageability/progress response → HJP;
- health/lifestyle fact → Health Records;
- Safety evaluation/outcome → Safety & Eligibility;
- participant request for ordinary catch-up help → Programmes/HJP as appropriate;
- professional-care response → Professional Care only when that relationship/case exists;
- Programme requirement satisfaction → Programmes may record the satisfaction decision/minimum provenance.

One screen must not become one shared-write clinical record.

## 104.14 A facilitator question is not automatically a clinical intake

Participants may submit facilitator questions. If the content becomes health-sensitive and materially affects safety, the governed system must route the relevant meaning to the owning Health/Safety pathway rather than leave it as an informal facilitator note that silently drives clinical decisions.

The facilitator is not required or authorised to diagnose the submission.

## 104.15 Urgent-help information is a bounded safety surface, not monitoring

If a check-in or other governed interaction reaches an approved urgent-help outcome:

- show only approved `OQ-008` wording/actions;
- preserve the applicable Safety-owned event/outcome evidence;
- do not imply that a clinician is continuously watching;
- do not imply guaranteed follow-up unless a separately activated service contract actually promises it;
- do not rely on ordinary facilitator/community messages as the urgent-response system.

## 104.16 Current Safety outranks recovery recommendations

Pass-10 recovery logic may suggest the next smallest useful action only inside current authority.

If Safety newly blocks or restricts an activity/path, the recovery backlog/recommendation must update. A stale catch-up plan cannot make unsafe work permissible.

Safety-blocked work is not ordinary overdue work.

## 104.17 Safety clearance does not retroactively manufacture missed satisfaction

If a later Safety transition permits activity again:

- current future participation may resume under the approved route;
- historical `safety_blocked`/unperformed activity does not become `completed` merely because clearance exists now;
- catch-up, exemption, substitution or completion consequences follow the approved Programme rules.

## 104.18 Safety/clinical outcomes do not alter Entitlement by implication

A participant may hold a valid commercial/Entitlement right while Safety limits which programme/plan components may currently be used.

Likewise, Safety clearance does not create or extend an Entitlement.

Commercial remedy/offer promises remain Commerce/Entitlements/Product concerns rather than Safety or Programmes invention.

## 104.19 Completion and certificates must remain clinically humble

Programme completion may depend on approved safety acknowledgements or routes, but the final Programme/certificate outcome cannot be presented as:

- medically cleared;
- cured;
- clinically treated;
- safe for all future activity;
- professionally approved unless a separate professional record says so; or
- proof of guaranteed transformation/weight loss.

The certificate states participation/completion only.

## 104.20 Historical reproducibility needs references, not copied clinical payloads

Programmes may need to explain why a particular Programme path/requirement consequence was applied.

The safe boundary is minimum provenance to the governing Safety/route decision/version where permitted. Programmes does not need a duplicate diagnosis, medication list, health intake, Safety Case file or practitioner record.

Exact retention/de-link behaviour remains subject to Privacy/professional-record law.

## 104.21 No generic Programme clinical engine is justified

FP-008 needs explicit owner-mediated Safety routing and bounded Programme consequences. It does not need:

- a Programme-owned risk score;
- generic triage rules;
- a duplicate clinical case state machine;
- facilitator clinical overrides;
- medical decision DSLs;
- a Nuwe Jy-specific plan engine;
- a generic care-management platform; or
- continuous health monitoring.

Those would create competing authority and/or unjustified complexity.

---

# 105. Pass-13 focused pressure tests

## PRG-PT-483 — Programme stores its own clinical eligibility state

**Scenario:** FP-008 adds a mutable Programme field that independently says `medically_eligible=true`.

**Expected invariants / analysis:** Reject competing authority. Safety & Eligibility owns current eligibility. Programmes may hold a bounded route/reference/projection but cannot become a second Safety source.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-484 — Nuwe Jy route is assumed identical to core Safety outcome

**Scenario:** Implementation maps `eligible_automated` directly to `eligible_for_full_challenge` and treats the vocabularies as one enum without an approved rule.

**Expected invariants / analysis:** Reject premature equivalence. `OQ-025` owns exact challenge routing. Preserve the two semantic dimensions until the approved mapping exists.

**Disposition:** `PASS_REJECTED_MODEL / EXISTING_GATE`.

---

## PRG-PT-485 — Approved mapping later becomes one-to-one

**Scenario:** Clinical/Product authority later approves a deterministic direct mapping for a particular ProgrammeVersion.

**Expected invariants / analysis:** Permissible downstream. The mapping may be simple, but Safety still owns its source outcome and Programmes owns the route consequence/configuration.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-486 — Essential challenge safety screen requires full plan intake

**Scenario:** FP-008 blocks all participation until the participant completes every field required for a personalised nutrition plan.

**Expected invariants / analysis:** Reject as generic assumption. Product explicitly separates essential challenge safety screening from deeper personalised-plan intake.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-487 — Essential safety information is missing

**Scenario:** Participant has not supplied a safety-critical answer required for the applicable route.

**Expected invariants / analysis:** Fail closed to the approved `insufficient_information`/bounded route; do not infer full-challenge permission or participant failure. Exact rule belongs to `OQ-005`/`OQ-025`.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-488 — Participant qualifies for full challenge

**Scenario:** Current approved Safety and route rules permit the full challenge.

**Expected invariants / analysis:** Programmes may expose the approved full-challenge path; it does not persist a duplicate clinical rationale. Current Safety is rechecked where material.

**Disposition:** `PASS`.

---

## PRG-PT-489 — Participant is routed to safe modifications

**Scenario:** Current approved route is `eligible_with_safe_modifications`.

**Expected invariants / analysis:** Use the approved bounded modified Programme path. Facilitator/admin improvisation is not the modification authority. Safety/Plans remain owners where their truths are affected.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-490 — Facilitator manually decides safe modification

**Scenario:** Facilitator marks an activity “safe for this participant” based on a conversation.

**Expected invariants / analysis:** Reject. Facilitator role is non-clinical by default and cannot create Safety clearance/override. Route the concern through the governed owner.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-491 — General Wellness components remain available

**Scenario:** Personalised nutrition is blocked but Safety permits approved General Wellness, faith, education or community components.

**Expected invariants / analysis:** Valid Product path. Do not treat reduced component scope as fabricated full completion or automatic failure; exact outcome is governed by `OQ-019`/`OQ-025`.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-492 — `professional_review_required` hides all Programme content automatically

**Scenario:** Programme removes every education/community/faith surface whenever professional review is required.

**Expected invariants / analysis:** Not universally authorised. Product says approved non-personalised components may remain where Safety permits. Exact route restrictions belong to the approved Nuwe Jy routing policy.

**Disposition:** `PASS_REJECTED_UNIVERSAL_RULE`.

---

## PRG-PT-493 — Programme creates a Professional Review Case

**Scenario:** Programme admin creates/updates a shadow clinical case directly inside Programmes when route is `professional_review_required`.

**Expected invariants / analysis:** Reject shared-write ownership. Professional Care owns the actual review/case lifecycle; Safety owns the restriction/routing authority.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-494 — Professional review recommendation is treated as case acceptance

**Scenario:** Support recommends professional review and Programmes assumes a practitioner is now responsible.

**Expected invariants / analysis:** Reject. Recommendation/referral is not an active consented care/review relationship, practitioner acceptance, capacity allocation or completed review.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-495 — Practitioner role alone grants cohort participant clinical access

**Scenario:** A person assigned `clinical_reviewer` or practitioner role can open all cohort health data.

**Expected invariants / analysis:** Reject. Professional access requires consent + active relationship + scope + expiry + audit; role alone is insufficient.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-496 — Facilitator also holds a separately authorised clinical relationship

**Scenario:** Same human is both facilitator and authorised practitioner for one participant.

**Expected invariants / analysis:** Multiple roles may coexist, but data access follows the clinical relationship/purpose when acting clinically. Facilitator scope does not inherit clinical fields.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-497 — Practitioner approves Safety downgrade

**Scenario:** High-risk participant is proposed for lower-risk/automated eligibility.

**Expected invariants / analysis:** Follow `DEC-091`/`DEC-092` and Safety-owned override/clearance rules. Programmes must consume the resulting Safety authority; it cannot record the downgrade itself.

**Disposition:** `PASS`.

---

## PRG-PT-498 — Practitioner modifies nutrition plan

**Scenario:** Professional review recommends a modified personalised plan.

**Expected invariants / analysis:** Professional Care records the professional outcome/request; Plans creates/owns the resulting Plan version through its governed interface. Programmes references current Plan guidance and does not copy the plan as challenge state.

**Disposition:** `PASS`.

---

## PRG-PT-499 — Safety changes mid-Enrolment to restricted

**Scenario:** Participant has valid prior progress but a new health fact leads Safety to restrict future activity.

**Expected invariants / analysis:** Future unsafe path is blocked/changed immediately under current authority. Preserve Enrolment/history/prior evidence; do not auto-delete, reset, complete or fail the Enrolment.

**Disposition:** `PASS`.

---

## PRG-PT-500 — Safety change while participant is offline

**Scenario:** Safety restriction changes after a Programme page was previously opened.

**Expected invariants / analysis:** Stale page/session/projection does not preserve old permission. Authoritative protected action rechecks current Safety where material; recovery guidance updates on reconnect/current action.

**Disposition:** `PASS`.

---

## PRG-PT-501 — Safety restriction races with activity submission

**Scenario:** Participant submits an activity while a material Safety transition is being committed.

**Expected invariants / analysis:** Do not let UI timing establish clinical permission. The authoritative action/consequence must resolve against the approved current-authority/concurrency contract; no stale acceptance may bypass Safety. Exact transaction mechanics remain JIT/proof detail.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-502 — Existing accepted progress is erased after restriction

**Scenario:** Safety restriction causes Programme to delete earlier legitimate completion/evidence.

**Expected invariants / analysis:** Reject. Current restriction governs current/future permission; historical truth remains unless a separately governed source correction invalidates it.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-503 — Safety-blocked habit/activity marked complete

**Scenario:** An occurrence is `safety_blocked`, and Programmes marks the requirement completed for convenience.

**Expected invariants / analysis:** Reject fabricated completion. `safety_blocked` remains truthful source state; exception/substitution/completion consequence needs an approved Programme rule.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-504 — Safety-blocked activity is repeatedly nagged as ordinary overdue work

**Scenario:** Recovery treats safety-blocked work like ordinary missed backlog.

**Expected invariants / analysis:** Reject. Pass 10 already requires recovery to respect current Safety. The item may need an approved alternative/exemption/waiting state rather than ordinary catch-up prompting.

**Disposition:** `PASS`.

---

## PRG-PT-505 — Safety later clears blocked activity

**Scenario:** Current Safety later permits an activity that was previously blocked.

**Expected invariants / analysis:** Future activity may become available under current Programme rules. Historical non-performance is not silently rewritten as completion; catch-up/exception rules decide what remains required.

**Disposition:** `PASS`.

---

## PRG-PT-506 — Programme pause is used as Safety Case state

**Scenario:** `Enrolment.paused` is treated as the canonical clinical restriction/case status.

**Expected invariants / analysis:** Reject lifecycle collapse. Safety Case/restriction remains Safety authority. Programme pause may be a distinct participation consequence only if separately governed.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-507 — Safety restriction automatically pauses Enrolment

**Scenario:** Any Safety restriction triggers Programme `paused` unconditionally.

**Expected invariants / analysis:** No universal rule is authorised. Safety constrains the unsafe path; the exact Programme lifecycle consequence must be defined by the approved route/ProgrammeVersion. Preserve history meanwhile.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-508 — Safety restriction automatically abandons or fails Enrolment

**Scenario:** Safety route changes and Programme marks `abandoned` or failed.

**Expected invariants / analysis:** Reject punitive inference. Current authority does not equate Safety restriction/professional review/insufficient information with abandonment or failure.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-509 — Safety withdrawal leads to `withdrawn_for_safety`

**Scenario:** Approved Programme completion/outcome policy explicitly uses `withdrawn_for_safety` after a governed Safety consequence.

**Expected invariants / analysis:** Product permits this outcome family, but exact trigger is `OQ-025`/ProgrammeVersion policy. Programmes owns the Programme outcome; Safety owns the underlying restriction/decision.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-510 — `withdrawn_for_safety` certificate implies clinical diagnosis

**Scenario:** Participant-facing certificate/status explains diagnosis or claims medical unfitness.

**Expected invariants / analysis:** Reject. Programme certificate/status must remain participation/completion scoped and privacy-minimised. Clinical detail remains with its owner.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-511 — Daily manageability check-in remains behavioural

**Scenario:** Participant records ordinary manageability/difficulty with no material health/safety meaning.

**Expected invariants / analysis:** HJP may own the lightweight progress/check-in response. Programmes may consume the minimum requirement evidence; no Health record is created merely because the screen is in Nuwe Jy.

**Disposition:** `PASS`.

---

## PRG-PT-512 — Check-in contains a new safety-relevant health fact

**Scenario:** Participant reports a materially safety-relevant health/medication/symptom change in a governed field.

**Expected invariants / analysis:** Route the health fact to Health Records and Safety evaluation to Safety. Do not leave the information only inside HJP/Programme notes or make Programmes clinically interpret it.

**Disposition:** `PASS`.

---

## PRG-PT-513 — Free-text facilitator question contains urgent disclosure

**Scenario:** Participant types urgent health information into a facilitator-question surface.

**Expected invariants / analysis:** The programme cannot promise continuous monitoring. Use only the approved bounded detection/routing contract if such a surface is governed for it; otherwise do not falsely claim the facilitator is a clinical safety channel. `OQ-008` remains authoritative for urgent-help wording/boundaries.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-514 — Community post contains health concern

**Scenario:** Participant discloses a safety concern in cohort Community.

**Expected invariants / analysis:** Pass 12 Community moderation/sensitive-disclosure rules apply. Community location does not create Programme or clinical authority; any governed clinical escalation uses Safety/Professional pathways without copying the post into Programme completion evidence.

**Disposition:** `PASS`.

---

## PRG-PT-515 — Live-session host gives participant-specific medical instruction

**Scenario:** Live host attempts diagnosis/dosing/treatment for an individual participant.

**Expected invariants / analysis:** Reject under live/Q&A and peer/professional boundaries. A live host/facilitator is not converted into an authorised care relationship merely by the session role.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-516 — Support agent marks participant safe to continue

**Scenario:** Support resolves a ticket by manually overriding Safety and clearing the programme path.

**Expected invariants / analysis:** Reject. Support may resolve operational issues but cannot create clinical clearance. Owner-mediated Safety action/authorised override is required.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-517 — Programme admin marks safety acknowledgement complete

**Scenario:** Admin corrects a genuinely misrecorded Programme-owned acknowledgement under bounded correction authority.

**Expected invariants / analysis:** Possible only for the Programme-owned satisfaction record and with audit/provenance. It does not create Safety clearance or rewrite the source clinical decision. Generic mark-anything-complete remains rejected.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-518 — Urgent-help information shown

**Scenario:** Approved Safety routing requires urgent-help information.

**Expected invariants / analysis:** Display the exact approved `OQ-008` content/acknowledgement/escalation boundary. Do not improvise country-specific advice or imply monitoring/guaranteed response.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-519 — Participant ignores professional-review recommendation

**Scenario:** Participant does not establish a Professional Care relationship after a professional-review route/recommendation.

**Expected invariants / analysis:** Do not fabricate review completion or Safety clearance. Apply current Safety/Programme route restrictions; preserve Enrolment/history. Exact programme completion consequence remains governed by `OQ-019`/`OQ-025`.

**Disposition:** `PASS_WITH_EXISTING_GATE`.

---

## PRG-PT-520 — Professional Care capacity unavailable

**Scenario:** Safety indicates professional review but no saleable/available professional capacity exists.

**Expected invariants / analysis:** Do not pretend review occurred or relax Safety. Programme may remain on the approved safe/non-personalised route where Product permits; FP-012 capacity/service semantics remain separate.

**Disposition:** `PASS`.

---

## PRG-PT-521 — Safety route changes after completion award

**Scenario:** Participant completed under then-valid authority; a later health change now restricts current participation/plan use.

**Expected invariants / analysis:** Current Safety changes future/current use, not historical completion automatically. If a source correction proves the original award basis was invalid, existing post-award correction gap `PRG-GAP-002` remains the governing unresolved seam.

**Disposition:** `PASS_WITH_EXISTING_GAP`.

---

## PRG-PT-522 — Certificate claims participant is medically cleared

**Scenario:** Completion certificate states or implies medical clearance.

**Expected invariants / analysis:** Reject. Product limits certificates to participation/completion and forbids medical-competence/guaranteed-outcome implication.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-523 — Programme copies Safety Case notes for reproducibility

**Scenario:** Programmes duplicates Safety Case narrative/health detail to explain routing history.

**Expected invariants / analysis:** Reject excess copying. Preserve only minimum lawful route/provenance references needed to explain Programme consequence. Safety/Health/Professional records retain their own privacy lifecycle.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-524 — Analytics risk score drives Programme route

**Scenario:** Analytics model predicts risk and directly switches participant from full challenge to modified route.

**Expected invariants / analysis:** Reject. Analytics is derived and cannot become Safety or Programme routing authority. Any future model would need explicit governed owner integration and clinical approval.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-525 — Cached Safety result extends old route

**Scenario:** Cached route/eligibility still permits an activity after authoritative Safety restriction.

**Expected invariants / analysis:** Reject stale authority. Current protected action must respect authoritative Safety; cache/projection may reduce freshness but never override revocation/restriction.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-526 — Duplicate Safety notifications create duplicate Programme transitions

**Scenario:** Same Safety change is observed multiple times and Programmes duplicates a durable path/exception consequence.

**Expected invariants / analysis:** Consequences must be idempotent/reconcilable. Programme outcome/provenance cannot multiply because PubSub/jobs/events repeat. Exact idempotency mechanics remain JIT.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-527 — Safety transition events arrive out of order

**Scenario:** Programme receives an older Safety observation after a newer restriction/clearance.

**Expected invariants / analysis:** Observations do not become authority by arrival order. Reconcile from current owner-managed state/version/provenance before a hard Programme decision; never regress current route from stale event order.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-528 — Safety owner temporarily unavailable during hard progression decision

**Scenario:** Progression into an activity requires current Safety authority, but the owner cannot be reliably read.

**Expected invariants / analysis:** Fail closed/bounded wait for the protected action rather than inventing permission from stale UI/session/analytics. Availability degradation must not weaken safety.

**Disposition:** `PASS`.

---

# 106. Pass-13 gap adjudication

## Core Safety-to-Programme mapping — bounded, exact values remain existing gates

The owner boundary is sufficient for later FP-008 JIT:

```text
Health Records owns health facts/provenance
        ↓
Safety & Eligibility owns current clinical/safety interpretation
        ↓
approved OQ-025 / ProgrammeVersion policy maps to Nuwe Jy route
        ↓
Programmes owns route-dependent activity/progression/completion consequence
```

What remains unresolved is intentionally concrete and already owned by `OQ-005`, `OQ-008`, `OQ-019` and `OQ-025`.

No new `PRG-GAP-012` is justified merely because the exact mapping is not yet approved.

## Professional-review boundary — no new Programme gap

The route into professional review is already owner-safe:

- Safety owns restriction/routing;
- Professional Care owns an actual consented relationship/case/outcome;
- Safety owns clearance/override consequence;
- Plans owns any resulting Plan version;
- Programmes consumes current resulting authority.

`OQ-033` remains the professional-record-authority gate for the Professional Care service boundary. FP-008 does not need to duplicate that record authority inside Programmes.

## Existing-gap interactions

- `PRG-GAP-002` remains open for a post-award corrected outcome/certificate consequence when a later correction invalidates the original award basis. A later change in current health state alone does not trigger retroactive rewrite.
- `PRG-GAP-009` remains narrowed: operator/facilitator/support actions cannot become generic waiver, mark-complete, source-evidence or Safety-override power.
- `PRG-GAP-011` remains unchanged: withdrawn required content without approved replacement cannot be repaired by Safety or recovery logic.
- `PRG-GAP-006` remains unrelated but compatible: external Community activity is not clinical or completion authority.

## No new Product / Architecture / Domain gap promoted

Pass 13 finds the current ownership model coherent. Exact clinical values and Programme consequences are already deliberately gated at the correct authority level.

No new Domain, `PRG-GAP-###`, `PRG-UPD-###`, generic Safety abstraction or Nuwe Jy-specific clinical engine is justified.

---

# 107. Pass-13 refinements to the working synthesis

## PRG-REF-123 — Core Safety eligibility and Nuwe Jy participation route are related but not identical authority concepts

Keep both semantic dimensions until an approved `OQ-025` mapping says how they compose for the concrete ProgrammeVersion.

## PRG-REF-124 — Programmes may own safety-routing configuration, never clinical eligibility truth

A ProgrammeVersion can configure path consequences of a Safety-owned result; it cannot recompute or override the result.

## PRG-REF-125 — `required_for_safety` remains a Programme requirement classification

It does not mean the Programme acknowledgement itself is a clinical clearance or Safety Case decision.

## PRG-REF-126 — Essential Nuwe Jy safety screening is not automatically the deeper personalised-plan intake

Preserve Product's progressive onboarding boundary; collect deeper Plan facts only for the defined Plan/Safety purpose that requires them.

## PRG-REF-127 — Current Safety change constrains future Programme guidance without erasing participation history

Historical Enrolment/evidence remains truthful; current unsafe actions/paths fail closed or change under the approved route.

## PRG-REF-128 — `safety_blocked` is not completed, failed, exempt or substituted by inference

Programmes consumes the truthful source state, then applies only an approved exception/completion consequence.

## PRG-REF-129 — `insufficient_information` is a fail-closed authority state, not participant misconduct

The participant may be asked for the governed missing information; the Programme does not fabricate failure or abandonment.

## PRG-REF-130 — Safe modification must be configuration/protocol driven, not facilitator improvisation

Facilitators guide within approved non-clinical scope; Safety/Plans own clinical and Plan consequences.

## PRG-REF-131 — Professional-review recommendation, Professional Care case, professional outcome, Safety clearance and Programme consequence remain distinct

Do not collapse this chain into one Programme `reviewed` flag.

## PRG-REF-132 — Facilitator identity never grants health/professional access by itself

Any same-person clinical access derives from a separately authorised clinical role, relationship, purpose, scope and audit trail.

## PRG-REF-133 — Check-in UI composition does not create shared-write clinical authority

Health fields, Safety decisions, behavioural progress, professional outcomes and Programme satisfaction remain with their owners even when collected/displayed together.

## PRG-REF-134 — Urgent-help surfaces must not imply continuous monitoring or guaranteed follow-up

Exact participant wording/actions stay behind `OQ-008`; ordinary Programme/Community/facilitator channels do not become emergency monitoring.

## PRG-REF-135 — Recovery and recommendations always re-enter through current Safety authority

A stale backlog, recommendation or previously opened screen cannot authorise an activity now restricted by Safety.

## PRG-REF-136 — Later clearance enables future participation but does not rewrite historical non-performance

Catch-up/exemption/substitution/completion remains Programme policy; Safety only supplies current authority.

## PRG-REF-137 — Safety and Entitlement remain orthogonal authorities

A valid right does not make an unsafe activity permissible; Safety clearance does not grant or extend commercial access.

## PRG-REF-138 — Programme completion/certificate is not clinical certification

It may state participation/completion only and must not imply diagnosis, treatment, medical competence, clearance or guaranteed outcome.

## PRG-REF-139 — Historical explainability uses minimum route/provenance references, not copied clinical payloads

Programmes should be able to explain its consequence while Health, Safety and Professional Care retain their own sensitive-data lifecycles.

## PRG-REF-140 — Duplicate/reordered Safety observations are reconciled from owner authority

PubSub/jobs/events can trigger re-evaluation but never become the source of current Safety truth or regress a route merely by arrival order.

---

# 108. Pass-13 anti-clinical-engine / YAGNI outcome

Pass 13 explicitly rejects:

- a Programme-owned clinical eligibility enum as competing Safety truth;
- treating the core eligibility enum and Nuwe Jy route enum as identical before `OQ-025` approval;
- a Nuwe Jy-specific Safety engine;
- a Nuwe Jy-specific nutrition/Plan engine;
- duplicating Health Records into Programme progress;
- copying Safety Case or Professional Care notes into Programmes;
- full Plan intake as an automatic prerequisite for every Nuwe Jy participant;
- absence-of-blocker as proof of safety;
- facilitator/support/admin clinical overrides;
- facilitator improvisation of safe modifications;
- Programme pause as a Safety Case lifecycle;
- Safety restriction as automatic Enrolment failure/abandonment/deletion;
- `safety_blocked` as fabricated completion;
- professional-review recommendation as proof of completed professional care;
- practitioner role alone as participant-record access;
- Community/live/facilitator surfaces as continuous clinical monitoring;
- generic medical triage/chatbot logic inside Programmes;
- Analytics-derived risk scores as Safety authority;
- stale Safety caches/projections as current authority;
- duplicate/out-of-order observation delivery as Programme route authority;
- certificates that imply medical clearance or treatment success; and
- a generic shared clinical-workflow Domain created for convenience.

The simplest correct model remains owner-mediated current Safety authority plus Programme-owned route consequence.

---

# 109. Pass-13 disposition

**Outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Health facts, Safety interpretation, Professional Care and Programme consequence remain distinct owner truths.
2. Core Safety eligibility and Nuwe Jy participation route are separate semantic dimensions; exact mapping remains `OQ-025`/clinical-Product authority.
3. Programmes may own versioned route/activity consequence configuration but not clinical eligibility/risk truth.
4. `required_for_safety` is Programme requirement meaning, not Safety clearance authority.
5. Nuwe Jy essential safety screening is required before participation, while deeper personalised-plan intake remains separately purpose-bound.
6. Missing safety-critical information fails closed for affected protected behaviour and is not participant failure/abandonment.
7. Safe-modification routing must be governed; facilitator improvisation cannot create clinical authority.
8. Approved General Wellness/education/faith/community components may remain available where personalised nutrition/full challenge is blocked if Safety permits.
9. `professional_review_required` does not itself create a Professional Care relationship/case or prove a review occurred.
10. Professional Care changes Safety through Safety-owned interfaces and Plans through Plans-owned interfaces; Programmes consumes the resulting authority.
11. Practitioner/facilitator/support/admin roles do not grant clinical access/override by role name alone.
12. Mid-Enrolment Safety changes constrain future Programme guidance immediately while preserving historical Enrolment/progress/evidence.
13. Safety changes do not automatically pause, fail, abandon, complete, restart or delete an Enrolment; exact Programme consequence is explicit policy.
14. `safety_blocked` remains truthful source/activity state and is not silently completed/exempted/substituted/failed.
15. Later Safety clearance permits future activity only; it does not retroactively satisfy missed/blocked Programme requirements.
16. Recovery/catch-up/recommendation logic always respects current Safety and cannot use stale authority.
17. One check-in experience may orchestrate HJP, Health, Safety, Professional Care and Programmes while preserving one owner per durable truth.
18. Health-sensitive participant input must not remain only in facilitator/Programme notes when it materially affects Safety.
19. Urgent-help surfaces use approved `OQ-008` wording/boundaries and do not imply continuous monitoring or guaranteed follow-up.
20. Safety and Entitlement are independent: access cannot override Safety, and Safety clearance cannot grant access.
21. Nuwe Jy references current authoritative Plan/Safety truth and never creates a parallel nutrition engine.
22. Programme completion/certificates state participation/completion only, not clinical clearance/treatment/outcome.
23. Historical Programme explainability should use minimum route/provenance references rather than copied diagnoses, health intake, Safety cases or professional notes.
24. Duplicate/reordered Safety observations trigger reconciliation from owner authority; they do not create/regress route truth by themselves.
25. `PRG-GAP-002`, `PRG-GAP-009` and `PRG-GAP-011` retain their existing scopes; no new gap is needed here.
26. `OQ-005`, `OQ-008`, `OQ-019`, `OQ-025`, `OQ-033` and applicable `OQ-026` operational ownership remain the correct unresolved gates.
27. No new Product, Architecture or Domain amendment is justified by this pass.
28. A generic Programme clinical engine, care-management abstraction or Nuwe Jy-specific Safety/Plan stack remains `DEFER_YAGNI` / rejected.

**Pass hard stop:** Pass 14 — journals / habits / private-reflection edge semantics — has not started. Do not pull journal/habit retention, sharing, safety-sensitive reflection, attachment or completion-evidence detail into this Pass-13 candidate.

**Broad discovery remains unfrozen.** Later translation, communications, operator correction, concurrency/retry, cancellation/transfer, historical reproducibility, analytics, FP-014 second-lens and final adversarial-convergence passes remain separate.
