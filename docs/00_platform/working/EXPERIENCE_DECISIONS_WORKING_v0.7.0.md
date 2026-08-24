# EXPERIENCE_DECISIONS_WORKING_v0.7.0.md

- **Document status:** WORKING / CUMULATIVE / APPEND-ONLY EXPERIENCE DECISION REGISTER
- **Document version:** v0.7.0
- **Last updated:** 2026-08-24
- **Purpose:** Preserve every accepted NewYou operating-model, participant-workflow, operator-workflow, UX, frontend, dashboard and design-system decision before synthesis into the Platform Operating Model and Frontend Experience System.
- **Authority boundary:** This register does not override Product Law, Architecture Law, Domain Law or the Roadmap. It records accepted experience/operating decisions beneath those authorities.
- **Implementation status:** PLANNING ONLY. No implementation is authorised by this document.

---

# 1. Permanent Maintenance Rule

This document is cumulative and append-only.

Once an experience decision is accepted:

1. do not delete it;
2. do not silently weaken it;
3. do not silently reinterpret it;
4. do not renumber it merely for neatness;
5. do not replace it through implementation convenience;
6. do not allow a generated skill, TOON prompt, Feature Pack, Resource Dossier, UI screen or coding-agent choice to contradict it.

If a later decision materially changes an accepted decision:

1. retain the original;
2. mark it `AMENDED`, `SUPERSEDED`, or `INVALIDATED`;
3. append the new decision;
4. identify the reason and affected downstream artifacts;
5. update the Platform Operating Model / Frontend Experience System synthesis;
6. run a regression review against previously accepted experience decisions.

## 1.1 Decision statuses

Use only:

- `LOCKED`
- `LOCKED_WITH_JIT_DETAIL`
- `AMENDED`
- `SUPERSEDED`
- `INVALIDATED`
- `PENDING`

## 1.2 Anti-regression rule

Every new experience-planning round must begin by preserving all prior `LOCKED` decisions.

A new proposal that contradicts a locked decision must not be silently accepted. Work must STOP and the conflict must be surfaced as an explicit amendment decision.

---

# 2. Foundational Operating / UX Decisions

## UX-FND-001 — Staff landing experience
**Status:** LOCKED

The default staff/operator landing experience is a **role-aware Command Centre** centred on work requiring attention, not a generic resource list or one identical analytics dashboard for every role.

## UX-FND-002 — Content operating model
**Status:** LOCKED

Content operations use a **Content Library + Work Queue + Editorial Calendar** hybrid.

## UX-FND-003 — Dashboard philosophy
**Status:** LOCKED

Use **governed canonical dashboards + permitted saved views** rather than unrestricted free-form BI by default.

## UX-FND-004 — Participant Home
**Status:** LOCKED

Participant Home is **next-best-authorised-action / journey oriented**.

## UX-FND-005 — Content authoring model
**Status:** LOCKED

Content uses **structured content types + controlled block composition**, not one universal free-form rich-text blob.

---

# 3. UX-001 — Visual Direction & Interaction Character

## UX-001-01 — Overall visual personality
**Status:** LOCKED

Use **Editorial Wellness + Modern Product UI**.

- content: warm, editorial, beautiful, human;
- participant application: clear, structured, fast, predictable;
- operator application: dense where appropriate, efficient and professional.

## UX-001-02 — Feminine character
**Status:** LOCKED

Use a **refined feminine** character: warm and distinctly feminine without stereotypical pink/beauty/spa styling.

## UX-001-03 — Colour philosophy
**Status:** LOCKED_WITH_JIT_DETAIL

Use a **warm neutral base + one distinctive brand colour family + restrained natural accents**, plus semantic success/warning/danger/information colours.

## UX-001-04 — Typography
**Status:** LOCKED_WITH_JIT_DETAIL

Use an **editorial serif for expressive/headline/content moments + highly legible sans-serif for application UI**.

## UX-001-05 — Shape language
**Status:** LOCKED_WITH_JIT_DETAIL

Use **moderately soft, restrained rounding**.

## UX-001-06 — Imagery
**Status:** LOCKED

Use **high-quality real photography as the primary storytelling medium**. Illustration and icons support concepts, onboarding, empty states and instructional material.

## UX-001-07 — Participant density
**Status:** LOCKED

Participant UI is **comfortably spacious but efficient**.

## UX-001-08 — Operator density
**Status:** LOCKED

Operator UI uses a comfortable default density, with denser tables, queues and analytics where useful.

## UX-001-09 — Motion
**Status:** LOCKED

Use **subtle, purposeful motion only**. Reduced-motion support is mandatory.

## UX-001-10 — Participant navigation
**Status:** LOCKED

Use **journey-oriented navigation** rather than exposing internal Domain structure.

## UX-001-11 — Operator global search
**Status:** LOCKED_WITH_JIT_DETAIL

Provide **policy-aware global search** across authorised entities, with command capabilities added incrementally.

## UX-001-12 — Operator work surface
**Status:** LOCKED

Provide a **unified operator Work surface over domain-owned work truth**.

---

# 4. UX-002 — Workflows, Approvals & Operator Behaviour

## UX-002-01 — Work assignment
**Status:** LOCKED

New work may enter a shared queue and becomes explicitly claimed/assigned when someone begins handling it.

Common operating projection:

`UNASSIGNED → ASSIGNED → IN_PROGRESS → RESOLVED`

Where review returns work, the projection may branch through `CHANGES_REQUESTED` and return to `IN_PROGRESS`.

Claiming or assigning is the operator action that produces the `ASSIGNED` projection. This is a common UI/operating projection over Domain-owned obligations, not a universal `Task` Resource or state machine. Domain-specific work lifecycles remain owned by the relevant Domain and are detailed only when affected JIT planning requires them.

## UX-002-02 — Due / target times
**Status:** LOCKED_WITH_JIT_DETAIL

Workflows may define optional due/target times according to workflow class. There is no universal SLA.

## UX-002-03 — Escalation
**Status:** LOCKED_WITH_JIT_DETAIL

Approved urgent/ageing workflows may escalate automatically. There is no universal “send every overdue item to Super Admin” rule.

## UX-002-04 — Approval model
**Status:** LOCKED

Where Product/Domain Law requires approval, approval is an explicit role/policy action separate from ordinary editing.

## UX-002-05 — Self-approval
**Status:** LOCKED_WITH_JIT_DETAIL

Self-approval may be permitted for low-risk workflows where policy allows it, but is prohibited for sensitive/high-risk workflows requiring separation of duties.

## UX-002-06 — Changes requested
**Status:** LOCKED

Review rejection becomes `CHANGES_REQUESTED` rather than silently closing the item. Reviewer context/history is preserved and the work returns to the responsible operator.

## UX-002-07 — Bulk actions
**Status:** LOCKED

Bulk actions are permitted only when each selected item can still satisfy its own policy and invariants.

## UX-002-08 — Work vs notifications vs toast
**Status:** LOCKED

Keep these separate:

- **Work:** action required;
- **Notification:** useful durable information;
- **Toast:** transient UI acknowledgement.

Required work must never exist only as a toast or email.

## UX-002-09 — Internal notes
**Status:** LOCKED

Support scoped internal notes/comments within relevant work/case contexts.

Internal notes are distinct from participant-visible messages, professional clinical records and immutable audit evidence.

## UX-002-10 — Human-readable activity history
**Status:** LOCKED

Important records should expose a curated, permission-aware business timeline derived from authoritative/audit evidence.

## UX-002-11 — Participant support workspace
**Status:** LOCKED

Support uses a scoped participant workspace summarising only permitted identity/access/commercial/support context. Routine impersonation is prohibited.

## UX-002-12 — View-as-participant
**Status:** LOCKED

Prefer safe preview/simulation without assuming participant identity. True impersonation may exist only if later proven necessary and explicitly governed, visible and audited.

## UX-002-13 — Content scheduling
**Status:** LOCKED

Scheduling requires an approved/publishable version, explicit timezone, previewable schedule and visible scheduled/queued state.

## UX-002-14 — Editorial calendar scope
**Status:** LOCKED

The editorial calendar covers relevant governed publishable/scheduled content types and major communication/programme publication milestones, with filtering by type/team/product.

## UX-002-15 — Dashboard publishing rights
**Status:** LOCKED

Analysts may prepare and validate dashboard drafts. Publishing canonical/shared dashboards requires governed approval appropriate to metric meaning and data sensitivity.

## UX-002-16 — Dashboard annotations
**Status:** LOCKED

Allow governed time-bound annotations for material launches, incidents, methodology changes and other events that materially affect interpretation.

## UX-002-17 — Participant notification centre
**Status:** LOCKED_WITH_JIT_DETAIL

An in-app participant notification centre is an approved eventual capability, but it is not an FP-001 prerequisite.

## UX-002-18 — Participant next-action model
**Status:** LOCKED

Participant Home composes next actions from authoritative Domain states. Do not create a second universal participant Task authority merely to drive checklists.

## UX-002-19 — Operator mobile scope
**Status:** LOCKED

Essential triage, review, approval, communication and urgent actions must be mobile-safe. Complex content authoring, dense analytics and advanced data workflows may remain desktop-first.

## UX-002-20 — Unsaved changes
**Status:** LOCKED

Substantial editors/forms require explicit dirty-state handling, autosave where semantics are safe, clear saved-state indication and navigation protection for unsaved governed changes.

---

# 5. Locked Cross-Cutting Experience Principles

1. **Workflow-first, not CRUD-first.**
2. **Role-aware, policy-aware experiences.**
3. **Participant UI follows the journey, not internal Domains.**
4. **Operator Work aggregates attention but never steals Domain ownership.**
5. **Frontend state is a projection of authoritative business state.**
6. **Critical success states may not be fabricated optimistically.**
7. **Accessibility is baseline correctness, not deferred hardening.**
8. **Afrikaans + English resilience starts at component level.**
9. **Participant experiences are mobile-first; operator experiences are desktop-efficient but mobile-safe for essential work.**
10. **Canonical analytics semantics are governed and versioned.**
11. **Content lifecycle, translation lifecycle and specialist approval are separate concerns and must not be collapsed into one ambiguous status.**
12. **High-risk actions require explicit policy, confirmation and audit appropriate to their risk.**
13. **No UI element, dashboard, work queue or saved view creates hidden business authority.**

---

# 6. Pending Experience Decisions

## UX-003 — Participant Journey & Account Experience
**Status:** COMPLETE / LOCKED in v0.2.0

Detailed decisions are recorded in Section 7.

## UX-004 — Content / Editorial / Media Detailed Operations
**Status:** COMPLETE / LOCKED in v0.3.0

Detailed decisions are recorded in Section 10.

## UX-005 — Analytics & Dashboard Detailed Experience
**Status:** COMPLETE / LOCKED in v0.5.0

Detailed decisions are recorded in Section 13.

## UX-006 — Visual Design System & Token Architecture
**Status:** COMPLETE / LOCKED in v0.6.0, with exact palette and font families explicitly deferred.

Detailed decisions are recorded in Section 16.

---

# 7. Synthesis Rule

This register is the source decision record.

Future Operating Model and Frontend Experience System documents are syntheses and must never contradict it.

If a downstream artifact conflicts with this register:

**STOP → classify the conflict → amend/supersede explicitly if intended → update downstream artifacts → rerun regression review.**

---

# 7. UX-003 — Participant Journey & Account Experience

## UX-003-01 — Public first visit
**Status:** LOCKED

Show the public experience immediately in a sensible default language, prominently offer Afrikaans/English on first entry, remember the choice, and keep language switching permanently accessible.

Do not force a blocking language-choice modal before useful public content is visible.

## UX-003-02 — Public-to-account progression
**Status:** LOCKED

Account creation should appear when it enables a meaningful action such as purchase, assessment, saved progress or programme participation.

Public educational discovery remains genuinely public.

### Refinement — Header account access and acquisition posture
**Status:** LOCKED

`Create account` and `Log in` must remain clearly available from the public header.

They should not be pushed aggressively.

The public experience is primarily **content-first and value-first**:

- useful public content is a primary acquisition surface;
- genuine educational value should lead naturally into relevant next steps;
- funnels should be contextual to the content or user intent rather than dominated by generic signup prompts;
- email capture is commercially valuable and should be encouraged through useful, honest value exchanges;
- account creation, mailing-list subscription and purchase remain distinct concepts;
- the platform should grow known users and permissioned email contacts without degrading the reading/discovery experience.

The preferred funnel shape is:

```text
useful public content
→ contextual relevant next step
→ optional email / account relationship where useful
→ product or programme discovery
→ purchase / entitlement when appropriate
```

Avoid:

```text
landing page
→ immediate forced signup
→ repeated generic popups
→ content hidden primarily to capture email
```

## UX-003-03 — Registration experience
**Status:** LOCKED

Use minimal account creation with only required registration data. Collect health and product-specific information progressively later.

## UX-003-04 — Verification-pending experience
**Status:** LOCKED

After registration but before email verification, show a useful verification-pending state with:

- explanation of what happened;
- resend control;
- change-email control;
- legitimate public/non-sensitive actions that remain available.

Do not grant protected application access before verification.

## UX-003-05 — Initial participant onboarding
**Status:** LOCKED

After verification, use lightweight orientation only.

Do not create a universal up-front wizard collecting unrelated future information.

Product-specific onboarding begins only when the participant enters that journey.

## UX-003-06 — Evolving participant Home
**Status:** LOCKED

Maintain one evolving participant Home that composes current:

- next actions;
- active programmes;
- plans;
- upcoming live/events;
- relevant content;

from authoritative Domain states.

Do not create a separate Home for each purchased product.

## UX-003-07 — Locked / unavailable capabilities
**Status:** LOCKED

Hide capabilities that do not meaningfully apply.

Show a locked state only when discovering or understanding the capability is useful and commercially appropriate.

Do not expose the mature-platform roadmap as a wall of disabled features or “coming soon” navigation.

## UX-003-08 — Successful purchase handoff
**Status:** LOCKED

After authoritative payment verification and access grant, show a clear purchase confirmation followed by the next authorised journey action associated with the purchase.

The UI may not fabricate payment or entitlement success before authoritative state exists.

## UX-003-09 — Pending / ambiguous payment
**Status:** LOCKED

When payment outcome is not yet authoritative, show a distinct `PAYMENT_PENDING` / `VERIFYING` experience.

- access is not yet shown as granted;
- reconciliation continues safely;
- the participant is discouraged from making a duplicate payment;
- the UI explains the next safe step.

## UX-003-10 — Long multi-step journeys
**Status:** LOCKED

Use purposeful multi-step flows for long or cognitively complex journeys such as assessment and health intake.

Require:

- clear sections;
- visible progress;
- safe save/resume;
- minimal cognitive load.

Do not force every form into a wizard.

## UX-003-11 — Progress indicators
**Status:** LOCKED

Prefer meaningful section/step progress.

Use exact percentages only when the percentage is honest and stable.

## UX-003-12 — Save/resume visibility
**Status:** LOCKED

Use durable save/autosave where appropriate plus visible reassurance such as `Saved` or a saved timestamp.

Returning participants receive an explicit resume path.

Browser-local state alone is not sufficient for important governed progress.

## UX-003-13 — Sensitive health-intake tone
**Status:** LOCKED

Health forms are:

- calm;
- plain-language;
- non-judgmental;
- safety-explicit;
- concise about why sensitive questions are needed.

Warmth must not weaken safety precision.

## UX-003-14 — Distinct missing-information meanings
**Status:** LOCKED

Where Product Law permits them, expose meaningful distinctions such as:

- `unknown`;
- `not_tested`;
- `prefer_not_to_answer`.

Do not collapse them into a generic skip/null state.

## UX-003-15 — Safety-blocked participant experience
**Status:** LOCKED

When automated personalisation is not permitted, explain the governed safe next outcome:

- General Wellness;
- more information required;
- professional review;

as applicable.

Do not expose unnecessary internal rule logic and do not allow participant override of Safety authority.

## UX-003-16 — Plan delivery
**Status:** LOCKED

Use a native structured plan experience as the primary delivery format.

Approved printable/downloadable representations may be secondary.

A PDF is not the platform's primary authoritative participant experience.

## UX-003-17 — Historical versions
**Status:** LOCKED

Default to the current/latest applicable version while keeping historical delivered versions intentionally accessible and clearly labelled.

Do not silently replace participant history.

## UX-003-18 — Account settings structure
**Status:** LOCKED

Use a grouped account/settings model:

```text
Profile
Language
Security
Privacy & Consent
Notifications
Purchases / Billing
Data & Account
```

Show only applicable sections.

## UX-003-19 — Privacy & Data centre
**Status:** LOCKED

Provide a dedicated Privacy & Data area for:

- applicable consent;
- export/data requests;
- deletion state;
- understandable consequences.

High-risk actions may require confirmation and re-authentication.

## UX-003-20 — Security centre
**Status:** LOCKED

Provide a focused Security area for:

- credentials;
- recovery;
- sessions/devices where supported;
- relevant participant-facing security events.

Do not expose raw technical auth telemetry.

## UX-003-21 — Recoverable error UX
**Status:** LOCKED

For recoverable errors:

- explain the issue in user terms;
- preserve entered work;
- state whether work was saved;
- present the safest next action;
- expose a support/reference identifier where useful.

Do not expose stack traces/provider internals.

## UX-003-22 — Interrupted-journey recovery
**Status:** LOCKED

When a participant returns after an interruption, Home recognises meaningful incomplete journeys and offers a clear `Continue` action at the correct safe resume point.

Do not automatically trap the participant inside the unfinished flow.

## UX-003-23 — Completion acknowledgement
**Status:** LOCKED

Use warm acknowledgement proportional to the event.

- routine actions: subtle confirmation;
- genuine milestones: stronger celebration.

Avoid indiscriminate confetti/gamification.

## UX-003-24 — Progress language
**Status:** LOCKED

Use encouraging, recovery-friendly progress language.

Recognise consistency without punishing interruptions.

Avoid aggressive streak/failure language and unnecessary leaderboard mechanics.

---

# 8. UX-003 Cross-Cutting Acquisition Principle

## UX-ACQ-001 — Content-led relationship building
**Status:** LOCKED

NewYou's public acquisition experience should prioritise **genuine useful content and contextual funnels**.

The platform should intentionally grow:

- permissioned email contacts;
- registered users;
- purchasers;
- programme participants;

but should do so through relevant value and clear next steps rather than aggressive account gating.

The header must keep `Create account` and `Log in` persistently discoverable.

Email capture should be offered where there is a real exchange of value, for example:

- useful newsletter/subscription;
- relevant guide/resource;
- programme/event updates;
- saved/continued journey;
- product-specific follow-up;

subject to Privacy & Consent authority.

This principle governs funnel UX only. It does not create consent, subscriber, identity or entitlement authority.

---

# 9. Regression Gate for Future Rounds

Before accepting UX-004 or any later experience decision, verify that it does not regress:

- UX-FND-001...005;
- UX-001-01...12;
- UX-002-01...20;
- UX-003-01...24;
- UX-ACQ-001.

Any contradiction requires explicit amendment/supersession.

---

# 10. UX-004 — Content / Editorial / Media Detailed Operations

## UX-004-01 — Content initiation
**Status:** LOCKED

New content may begin either as an editorial request/idea or as direct authorised draft creation. Both converge on the same governed content workflow.

Do not require a formal request ticket for every ordinary piece of content.

## UX-004-02 — Operational content ownership
**Status:** LOCKED

Each active content item has an explicit responsible editor/owner. Reviewers and approvers remain separate roles where applicable.

Operational assignment does not change Content & Media Domain authority.

## UX-004-03 — Governed content type first
**Status:** LOCKED

A creator selects a governed content type before composing content. The content type determines the allowed structure, required metadata and applicable workflow.

Do not use one universal blank-page content type.

## UX-004-04 — Extensible governed block / section / component catalogue
**Status:** LOCKED_WITH_JIT_DETAIL

Content composition uses an approved reusable catalogue of:

- blocks;
- sections;
- content components;
- composed patterns.

The catalogue is **intentionally extensible over time**. New reusable blocks, sections and components may be created as real content needs emerge, reviewed against the Frontend Experience System, and then reused by future content and templates.

Each content type may permit an appropriate subset of the catalogue.

This is not an unrestricted page builder. A content editor may compose approved building blocks but may not inject arbitrary HTML, arbitrary scripts, arbitrary styling or an ungoverned component system.

### Template relationship
**Status:** LOCKED

The platform supports reusable governed **content templates** similar in purpose to configured WordPress templates/patterns.

A template may predefine:

- allowed/expected sections;
- ordering;
- default blocks/components;
- required structural slots;
- recommended metadata;
- standard CTA placements;
- presentation defaults.

Templates accelerate repeatable publishing but do not create new content authority and do not bypass content-type, review, translation, accessibility or publication rules.

Templates may evolve through governed versioning. Existing published content must not silently change merely because a template later changes unless that relationship is explicitly designed as dynamic.

## UX-004-05 — Draft autosave
**Status:** LOCKED

Working drafts support safe autosave and a clear saved-state indication.

Autosave never implies review, approval or publication.

## UX-004-06 — Durable content versions
**Status:** LOCKED

Working drafts may evolve during editing, but meaningful review/publication boundaries create immutable/versioned snapshots according to the governed content lifecycle.

Do not create an immutable version for every keystroke and do not maintain only one mutable published record forever.

## UX-004-07 — Language variant model
**Status:** LOCKED

Afrikaans and English are separately governed language variants of one conceptual content identity.

They have independent translation/review states while preserving their relationship to the same conceptual item/version lineage.

The Product-Law translation lifecycle remains exact and independently governed per locale:

`missing → draft → machine_draft → language_review → clinical_review_required (where risk requires it) → approved → published → superseded → withdrawn`

Not every translation requires clinical review. Machine output is draft material only, records its source version, requires human language review and becomes stale when the source changes. Paid or contractual content, terms/consent/privacy notices, assessments, plans, clinical or safety content, and core-onboarding content must not publish or deliver without the required approved bilingual variants; optional low-risk content follows only the explicit fallback rule.

## UX-004-08 — Translation assignment
**Status:** LOCKED

Translation is explicit assignable work with:

- source version;
- target locale;
- assignee;
- state;
- required review.

Do not rely on spreadsheets or informal messages as authoritative workflow.

## UX-004-09 — Machine-assisted translation
**Status:** LOCKED

AI/machine translation may assist an approved draft workflow, but machine output does not become publishable governed content without the required human language review.

## UX-004-10 — Early content risk classification
**Status:** LOCKED

Content risk/type classification occurs early in drafting. Material changes may require reclassification and renewed review.

Do not postpone risk classification until final publication.

## UX-004-11 — Derived specialist-review routing
**Status:** LOCKED_WITH_JIT_DETAIL

Approved risk/type metadata determines which review classes are required and routes the item into appropriate work queues.

Editors should not have to remember specialist-review requirements manually.

Exact review rules remain governed by Product/Domain/JIT authority.

## UX-004-12 — Review comments
**Status:** LOCKED

Review feedback is contextual internal work linked to the relevant draft/version with history and resolution preserved.

Do not depend on external email/WhatsApp as the authoritative review trail.

## UX-004-13 — Exact experience preview
**Status:** LOCKED

Before publication, authorised operators can preview the actual target experience using:

- selected language;
- applicable product-space theme;
- real content presentation;
- applicable component/template composition.

An unstyled generic preview is insufficient.

## UX-004-14 — Fluid responsive design and resizable preview
**Status:** LOCKED_WITH_JIT_DETAIL

NewYou must use **fully responsive frontend design across the supported width continuum**, not merely a handful of hard-coded device layouts.

Frontend implementation should use the appropriate modern CSS mechanisms, including where suitable:

- CSS Grid;
- flexible layouts;
- `minmax()`;
- `calc()`;
- `clamp()`;
- container queries;
- media queries;
- intrinsic sizing;
- fluid typography/spacing where appropriate;
- logical properties;
- responsive images/media.

Components should prefer container-aware responsiveness when their behaviour depends on the space allocated by their parent rather than the global viewport.

Media queries remain appropriate for viewport/device/environment concerns and page-level composition.

### Preview workspace
**Status:** LOCKED

The editorial/design preview should provide a **continuously resizable / draggable viewport panel** so an operator can grow and shrink the preview and observe real responsive behaviour at arbitrary widths.

It should also provide convenient preset widths/breakpoints for repeatable review, but those presets are **testing shortcuts, not the definition of responsiveness**.

The preview should expose the current simulated width and allow verification around breakpoint boundaries rather than only at exact named device sizes.

## UX-004-15 — Scheduling warnings vs policy failures
**Status:** LOCKED

The system surfaces scheduling conflicts and dependency-readiness warnings.

Warnings do not block publication unless a governed requirement is actually violated.

The platform must not silently reschedule editorial work.

## UX-004-16 — Scheduled publication failure
**Status:** LOCKED

Scheduled publication uses durable execution/retry/reconciliation.

If publication cannot complete within the approved operational window, create a visible operator exception/work item.

Never mark content published merely because a scheduler attempted it.

## UX-004-17 — Published corrections
**Status:** LOCKED

Ordinary corrections create corrected/superseding governed versions while preserving historical publication provenance.

Do not silently rewrite governed published history in place.

## UX-004-18 — Safety-critical correction / withdrawal
**Status:** LOCKED

Materially unsafe or incorrect content has an expedited governed withdrawal/correction path including:

- dependency discovery;
- affected delivery handling;
- participant/operator consequences where required;
- audit/evidence.

It must not wait for a normal editorial cycle merely for convenience.

## UX-004-19 — Withdrawn-content experience
**Status:** LOCKED

Public delivery of withdrawn content stops.

Internal governed history remains.

Where historical participant references require context, show an appropriate withdrawn/replaced explanation rather than silently returning misleading old content.

## UX-004-20 — Content review / freshness dates
**Status:** LOCKED_WITH_JIT_DETAIL

Content may have optional or required review-by dates based on content type/risk.

Approaching review dates generate work according to approved policy.

There is no universal one-year expiry rule.

## UX-004-21 — Concise governed content analytics
**Status:** LOCKED_WITH_JIT_DETAIL

Editors may see a concise governed performance summary for published content where useful.

The editor links to deeper Analytics rather than becoming a full BI application.

Only approved metric definitions may appear.

## UX-004-22 — Contextual content funnel configuration
**Status:** LOCKED

Editors may choose from approved contextual CTA/funnel definitions appropriate to the content and user intent.

Funnel semantics, eligibility, tracking and consent remain governed.

Avoid one generic signup banner forced onto every page.

## UX-004-23 — Non-blocking value-led email capture
**Status:** LOCKED

Email capture may appear at meaningful content points with:

- clear value exchange;
- non-blocking interaction;
- appropriate consent semantics.

Do not gate most genuinely useful public content behind email and do not use immediate aggressive popups as the default acquisition strategy.

## UX-004-24 — Reusable CTA / funnel definitions
**Status:** LOCKED

Reusable CTA/funnel definitions are governed reusable content/configuration and may be placed contextually within approved content structures.

Do not hardcode repeated CTA markup independently across many pages.

## UX-004-25 — Governed Media Library
**Status:** LOCKED

Use a central governed Media Library supporting:

- reuse;
- metadata;
- provenance;
- rights/attribution where applicable;
- derivatives;
- usage references.

## UX-004-26 — Media rights / licence metadata
**Status:** LOCKED_WITH_JIT_DETAIL

Where applicable, media can represent:

- source;
- owner/rights;
- permitted use;
- expiry/review constraints.

Do not rely on filename conventions or external spreadsheets as the only rights record.

## UX-004-27 — Media derivatives
**Status:** LOCKED

Preserve authoritative source media and generate/serve appropriate derivatives through governed media infrastructure.

Do not make editors manually upload every responsive size or serve full-resolution originals everywhere.

## UX-004-28 — Media replacement
**Status:** LOCKED_WITH_JIT_DETAIL

Preserve media/version provenance where material.

Corrections/replacements intentionally update references or create a governed replacement according to usage semantics rather than blindly overwriting source bytes everywhere.

## UX-004-29 — Editorial search/filtering
**Status:** LOCKED

Operator content search supports, where applicable:

- text search;
- content type;
- locale;
- lifecycle state;
- risk;
- owner;
- reviewer;
- taxonomy;
- publication status/date;
- product/programme associations.

Do not expose arbitrary SQL-style querying to ordinary editorial users.

## UX-004-30 — Editorial templates
**Status:** LOCKED

Editors can start from approved reusable templates for recurring content formats.

Templates may precompose approved block structure/defaults and are optional unless a particular governed content type requires one.

Do not require cloning old content as the normal templating strategy.

---

# 11. Operational Scheduling Decision

## UX-OPS-001 — Durable Scheduling & Periodic Operations
**Status:** LOCKED

NewYou uses PostgreSQL-backed durable job scheduling for business-significant scheduled and periodic work.

### Rules

1. **Oban is the default durable background/scheduling mechanism.**
2. Future business-effective actions use persisted durable work.
3. Static periodic operations may use core Oban Cron or an equivalent cluster-safe scheduler where applicable.
4. AshOban remains the preferred Ash-native integration candidate only where an operation naturally maps to an Ash Resource/action; exact package, version and integration remain JIT.
5. Exact scheduler/resource integration remains downstream and must not be fixed here.
6. In-memory GenServer/OTP heartbeat loops are not authoritative business schedulers.
7. A scheduled/periodic worker must re-check current Domain authority and applicable guards before performing a governed transition.
8. Failed required scheduling uses durable retry/reconciliation and eventually creates operator-visible exceptions/work where required.
9. Recurring sweeps must be bounded and designed to avoid large peak-time scans.
10. PubSub may announce successful changes but is never the durable scheduler or business authority.
11. Scheduling infrastructure must not directly mutate another Domain's persistence as an alternate business API.
12. A single global heartbeat scanning the entire platform is explicitly rejected.

`OQ-016` remains the gate for exact scheduler reliability, retry, alert ownership, stale-authority checks and recovery behaviour.

### Typical applicable capability families

- scheduled content publication;
- content review/freshness reminders;
- work-item ageing/escalation;
- assessment or entitlement expiry where governed;
- payment/provider reconciliation;
- notification scheduling;
- programme/content releases;
- event lifecycle operations;
- retention/deletion orchestration;
- analytics maintenance/materialisation where appropriate.

### Business-effective time rule

A scheduled job firing does not itself prove that the business transition is valid. At execution time the relevant owning Domain/action must revalidate current authority and state before committing the transition.

---

# 12. Regression Gate for Future Rounds

Before accepting UX-005 or later decisions, verify they do not regress:

- UX-FND-001...005;
- UX-001-01...12;
- UX-002-01...20;
- UX-003-01...24;
- UX-ACQ-001;
- UX-004-01...30;
- UX-OPS-001.

Any contradiction requires explicit amendment/supersession.

---

# 13. UX-005 — Analytics, Dashboards & Reporting Operations

## UX-005-01 — Analytics landing experience
**Status:** LOCKED

Analytics opens to a role-aware Analytics Home showing:

- approved canonical dashboards;
- relevant recent/saved filter views where supported;
- data-health/freshness status;
- concise relevant insights.

Do not open to a blank report/dashboard builder or raw event explorer.

## UX-005-02 — Canonical dashboard ownership
**Status:** LOCKED

Each canonical dashboard has:

- a named business owner accountable for its business meaning/use;
- an analytical steward responsible for metric/data quality and analytical implementation.

## UX-005-03 — Metric ownership
**Status:** LOCKED

Each canonical metric has an explicit semantic/business owner and governed metric contract.

Analytics may derive/calculate the metric but does not acquire ownership of the authoritative source business facts.

## UX-005-04 — Metric lifecycle
**Status:** LOCKED

Approved canonical metric definitions use a governed lifecycle such as:

`DRAFT → REVIEW → APPROVED → ACTIVE → SUPERSEDED / RETIRED`

Exact implementation state names may be refined JIT without weakening lifecycle semantics.

## UX-005-05 — Compact metric-definition versioning, not data duplication
**Status:** LOCKED

Metric versioning preserves **the meaning of a metric**, not duplicate copies of all underlying analytics data.

A metric-definition version is expected to be a compact semantic record containing, as applicable:

- name/identifier;
- formula/definition;
- source authoritative facts;
- time basis/timezone;
- permitted dimensions;
- exclusions;
- freshness contract;
- effective period/version;
- quality/reconciliation rules.

### Anti-bloat rule

Do not copy raw events, aggregates or full dashboard data merely because a metric definition changes.

Approved metric versions referenced by historical reports, release/pilot decisions or other governed evidence must remain interpretable.

Working drafts or obsolete analytical artifacts that have no governance/evidence obligation may follow an explicit retention/archive policy rather than being retained forever by default.

Historical report snapshots are preserved only where reproducibility of a material decision/report requires them.

Raw/high-volume analytics data has a separate retention, aggregation and archival strategy and must not be conflated with metric-definition history.

## UX-005-06 — No general dashboard builder
**Status:** LOCKED

NewYou will **not build a user-facing general dashboard creation/builder capability** for the initial platform.

The platform provides deliberate, purpose-built canonical dashboards with the filters, comparisons, drill-downs and actions required for NewYou operations.

Illustrative dashboard families are not a future KPI catalogue or a commitment to build every family:

- Commercial / Sales;
- Acquisition / Content;
- Product Funnel;
- Participant Outcomes;
- Operations / Exceptions;
- Platform Health;
- programme/cohort dashboards when those capabilities exist.

If later evidence demonstrates a real need for dashboard composition/building, it may be introduced as a separately approved future capability.

## UX-005-07 — Curated dashboards with governed analytical building blocks
**Status:** LOCKED

Canonical dashboards are designed intentionally rather than assembled by ordinary users from arbitrary database fields.

They use governed:

- metric contracts;
- dimensions;
- filters;
- charts/tables;
- comparisons;
- drill-down paths;
- freshness semantics.

Implementation may reuse internal chart/dashboard components, but those components do not imply a user-facing dashboard builder.

## UX-005-08 — Governed analytical exploration
**Status:** LOCKED_WITH_JIT_DETAIL

Data Analysts may receive deeper governed analytical exploration where justified, using permitted metrics, dimensions, cohorts, funnels and comparisons.

Do not expose a raw PostgreSQL console or unrestricted sensitive-field exploration through the application.

## UX-005-09 — Explicit filters
**Status:** LOCKED

Dashboard filters are visible, explicit, semantically safe and permission-aware.

Only filters relevant to a dashboard and metric set are provided.

## UX-005-10 — Safe shareable filter state
**Status:** LOCKED_WITH_JIT_DETAIL

Filtered dashboard state may be bookmarkable/shareable where useful and safe.

Do not embed sensitive participant identifiers or other protected data directly into shareable URLs.

## UX-005-11 — Explicit comparison baseline
**Status:** LOCKED

Any comparative value must clearly state its baseline, such as:

- previous period;
- previous year;
- selected period;
- selected cohort.

Never present a percentage change without making `compared with what` clear.

## UX-005-12 — Explicit timezone semantics
**Status:** LOCKED

Metrics/reports have explicit time/timezone semantics.

Current South African business reporting normally uses `Africa/Johannesburg` unless a metric contract explicitly defines otherwise.

## UX-005-13 — Freshness visibility
**Status:** LOCKED

Important dashboards expose material freshness state and `last updated` information where useful.

Supported semantic states include as applicable:

- `CURRENT`;
- `STALE`;
- `PARTIAL`;
- `DELAYED`;
- `UNAVAILABLE`;
- `ERROR`;
- `NO_DATA`;
- `RESTRICTED`.

## UX-005-14 — Data-quality warnings
**Status:** LOCKED

If a metric or data source fails reconciliation/quality checks, affected dashboard areas visibly communicate that condition rather than presenting the value as unquestionably current/correct.

Do not guess or silently fill missing authoritative values.

## UX-005-15 — Governed drill-down
**Status:** LOCKED

Dashboards may provide useful drill-down while inheriting or tightening the viewer's row/field/purpose permissions.

Dashboard visibility never automatically grants sensitive underlying-record access.

## UX-005-16 — Sensitive data minimisation
**Status:** LOCKED

General management dashboards use approved aggregates/minimised dimensions.

Private journals and full clinical/professional records do not belong in general dashboards.

## UX-005-17 — Export is a separate permission
**Status:** LOCKED

Dashboard visibility does not imply export permission.

Exports independently enforce applicable:

- row access;
- field access;
- purpose;
- privacy;
- data-volume controls.

## UX-005-18 — Large exports are asynchronous
**Status:** LOCKED

Large exports use bounded durable background jobs with:

- secure artifact lifecycle;
- expiry where appropriate;
- operator notification when ready;
- auditing/permissions.

Do not synchronously load large exports into a LiveView or browser memory.

## UX-005-19 — Saved filter views, not dashboard forks
**Status:** LOCKED_WITH_JIT_DETAIL

Where useful, users may save personal or authorised team **filter/view presets** for an existing canonical dashboard.

A saved view may preserve items such as:

- filters;
- date range;
- sort/grouping;
- permitted presentation preferences.

It does not become a new dashboard, redefine canonical metrics or fork dashboard governance.

Saved-view capability may be deferred until a real dashboard demonstrates sufficient value.

## UX-005-20 — Canonical dashboards remain canonical
**Status:** LOCKED

Ordinary users do not edit canonical dashboard definitions.

Changes to canonical dashboard composition/meaning follow governed product/analytics change workflow.

## UX-005-21 — Governed dashboard annotations
**Status:** LOCKED

Authorised operators/analysts may add provenance-bearing, time-bound annotations for material interpretation context such as:

- launch;
- campaign;
- incident;
- pricing change;
- content release;
- methodology change;
- provider disruption.

## UX-005-22 — Threshold alerts
**Status:** LOCKED_WITH_JIT_DETAIL

Approved deterministic thresholds may produce durable operator work/notifications.

Avoid generic user-defined alert engines and noisy alerts without an actionable operational purpose.

Exact thresholds remain JIT/domain policy.

## UX-005-23 — Anomaly detection is evidence-gated
**Status:** LOCKED

Begin with governed deterministic checks/thresholds.

Statistical/ML anomaly detection may be added later where evidence shows clear value.

Do not require AI anomaly detection for MVP.

## UX-005-24 — Reactive dashboard refresh
**Status:** LOCKED

Dashboard interaction is **reactive**.

When a user:

- changes a filter;
- changes a date range;
- selects a comparison;
- clicks a refresh control;
- performs another dashboard query interaction;

the relevant LiveView/data region must update automatically from the new state.

The user must **not** be required to select a filter and then separately reload/refresh the browser page to apply it.

Where operational data changes through approved realtime/freshness mechanisms, the view may update automatically or reconcile according to its freshness contract.

Full-page browser reload is not the normal interaction model.

## UX-005-25 — Reconcilable operational projections
**Status:** LOCKED_WITH_JIT_DETAIL

High-frequency operational counters use authoritative facts plus reconcilable projections/cached aggregates where justified.

Redis/cache projections never become source business authority.

## UX-005-26 — Dashboard-specific default periods
**Status:** LOCKED

Each dashboard receives a sensible, clearly visible default period appropriate to its purpose.

There is no forced universal `last 30 days` default for every dashboard.

## UX-005-27 — Governed funnels
**Status:** LOCKED

NewYou supports governed funnels using explicit milestone definitions and authoritative facts where appropriate.

Examples include acquisition and core paid-journey funnels.

Frontend pageview sequences alone are not authoritative business funnel outcomes.

## UX-005-28 — Governed cohort analysis
**Status:** LOCKED_WITH_JIT_DETAIL

Support cohort comparison where useful, using explicit cohort definitions and privacy-safe dimensions.

Likely examples include programme editions, acquisition cohorts and membership-start cohorts.

## UX-005-29 — Native content-to-outcome attribution + external marketing evidence
**Status:** LOCKED_WITH_JIT_DETAIL

NewYou must be able to understand which content/pages/funnels contribute most strongly to valuable downstream outcomes such as:

- permissioned email subscriptions;
- account creation;
- product interest;
- verified purchases/revenue;
- assessment starts/completions;
- programme enrolments;
- other approved conversions.

### First-party/native layer

NewYou should capture privacy-governed first-party content/funnel facts sufficient to connect approved content engagement with authoritative downstream NewYou business outcomes.

This native layer is the platform's basis for business-result attribution and future content-ranking/recommendation algorithms.

It must not claim that correlation is necessarily causal proof.

### External complementary layer

GA4 / Google Tag Manager / Google Search Console may be integrated as complementary acquisition/search/marketing evidence.

They do not replace NewYou's authoritative business facts.

Google Search Console data is particularly useful for search traffic/query/page/device performance, while GA4 can supply web-session/acquisition behaviour and Measurement Protocol can supplement tagged data with approved server-side events when appropriate.

### Future optimisation

Architecture should preserve the option for later governed algorithms that use trusted content-performance signals to:

- feature high-performing content;
- prioritise recommendations;
- select related content;
- inform editorial promotion.

Such algorithms remain derived/presentation mechanisms and may not silently become Content, Commerce or Experimentation authority.

## UX-005-30 — Privacy-governed anonymous-to-known continuity
**Status:** LOCKED_WITH_JIT_DETAIL

Support first-party continuity from anonymous/public activity to known identity only where privacy/consent rules permit and the architecture proves it safely.

Do not use covert/aggressive device fingerprinting as identity.

## UX-005-31 — Experiment-specific analytical view
**Status:** LOCKED

Experiment result views use governed exposure/outcome facts.

Analytics provides measurement evidence; Experimentation retains final governed experiment-decision authority.

## UX-005-32 — Explicit financial measure semantics
**Status:** LOCKED_WITH_JIT_DETAIL

Avoid one ambiguous generic `Revenue` number.

Financial/commercial dashboards distinguish the measures actually approved, such as:

- gross sales;
- amount due;
- cash collected;
- discounts;
- refunds;
- gateway fees;
- settlements/net proceeds;
- recurring run-rate;
- formally recognised accounting revenue where accounting policy exists.

Do not equate verified payment with recognised accounting revenue.

## UX-005-33 — Reproducible material reporting snapshots
**Status:** LOCKED_WITH_JIT_DETAIL

Preserve report/metric/time-window context where reproducibility matters for a material decision, such as:

- release/pilot review;
- experiment decision;
- monthly/period management pack.

Do not snapshot every ordinary dashboard interaction.

## UX-005-34 — Scheduled reports
**Status:** LOCKED_WITH_JIT_DETAIL

Approved recurring management/report packs may be durably scheduled using UX-OPS-001.

Do not automatically email every dashboard on a generic cadence.

## UX-005-35 — Secure report delivery
**Status:** LOCKED

Prefer secure in-app/report access, with notifications/links and governed downloadable artifacts where allowed.

Avoid unrestricted public links or uncontrolled sensitive attachments.

## UX-005-36 — Concise executive/owner overview
**Status:** LOCKED

Provide a concise management overview composed from canonical metrics with governed drill-down into specialist dashboards.

Do not create one giant screen containing every available metric.

## UX-005-37 — Responsive dashboard hierarchy
**Status:** LOCKED

Essential KPIs/summaries are mobile-safe.

Dense analytical exploration remains desktop-first where necessary while preserving responsive correctness.

## UX-005-38 — Interactive charting; Chart.js preferred candidate
**Status:** LOCKED_WITH_JIT_DETAIL

Charts should support useful accessible interaction such as:

- tooltips/details;
- click/select/drill-down where appropriate;
- keyboard/touch-compatible alternatives;
- responsive resizing.

**Chart.js is the preferred initial charting-library candidate** because its current official API supports responsive resizing and configurable hover/click/touch interaction modes.

Final package/version/integration remains a JIT implementation decision and must prove:

- Phoenix LiveView integration is clean and bounded;
- responsive behaviour is correct;
- accessibility requirements are met with suitable textual/tabular alternatives;
- bundle/performance impact is acceptable.

Do not introduce a heavier charting framework without a demonstrated need.

## UX-005-39 — No-data semantics
**Status:** LOCKED

Where semantically meaningful, distinguish:

- true zero;
- no observations;
- not applicable;
- not yet available;
- restricted;
- data error.

Do not render missing/unknown data as numeric zero.

## UX-005-40 — Analytics trust principle
**Status:** LOCKED

**A smaller number of semantically trustworthy metrics is better than a large dashboard full of ambiguous metrics.**

Do not promote every tracked event into a KPI.

---

# 14. DELIV-PERF-001 — JIT High-Leverage Performance Pass

**Status:** LOCKED / MUST PROPAGATE TO DELIVERY EXECUTION STANDARD

Every approved implementation slice must include a proportionate performance review before it is considered complete.

The operating sequence is:

```text
BUILD CORRECTLY
→ VERIFY CORRECTNESS
→ COMPLETE THE SLICE
→ HIGH-LEVERAGE PERFORMANCE PASS
→ ACCEPTANCE
→ STOP
```

## Purpose

Catch inexpensive, structurally valuable performance improvements while implementation context is fresh, without turning every slice into a premature optimisation project.

## Required review questions

For the affected path, check at minimum:

- obvious N+1 queries;
- missing critical indexes;
- avoidable repeated DB queries;
- unbounded list/query/payload behaviour;
- unnecessarily large LiveView assigns/diffs;
- avoidable rerenders;
- expensive synchronous work that should be durable async;
- straightforward batching/preloading opportunities;
- obviously wasteful client assets/JS;
- obvious cache opportunity only when justified;
- unnecessary provider calls;
- algorithmic/data-structure problems with meaningful payoff.

## Bias

Prefer **small changes with large rewards**.

Do not spend disproportionate time micro-optimising:

- tiny allocations;
- negligible helper calls;
- speculative caches;
- speculative Redis/GenServer layers;
- obscure optimisations without evidence.

## Escalation

If the lightweight pass reveals a material performance risk that cannot be resolved cheaply without broadening scope:

- record it;
- determine whether it blocks the current slice;
- route it to the appropriate TB/VS/HH/performance gate;
- do not silently over-engineer the slice.

This performance pass does not replace later load/stress/soak/hardening evidence where required.

---

# 15. Regression Gate for Future Rounds

Before accepting UX-006 or later decisions, verify they do not regress:

- UX-FND-001...005;
- UX-001-01...12;
- UX-002-01...20;
- UX-003-01...24;
- UX-ACQ-001;
- UX-004-01...30;
- UX-OPS-001;
- UX-005-01...40;
- DELIV-PERF-001.

Any contradiction requires explicit amendment/supersession.
---

# 16. UX-006 — Visual Design System & Token Architecture

## UX-006-01 — Exact brand palette deferred
**Status:** LOCKED_WITH_JIT_DETAIL

The exact NewYou colour palette is not frozen yet.

The eventual palette must be introduced through the governed token system defined below. Components and templates must not depend on remembered raw colour values.

Previously proposed colour directions remain examples only and are not authoritative.

## UX-006-02 — Exact font families deferred
**Status:** LOCKED_WITH_JIT_DETAIL

The exact heading/editorial and application font families are not frozen yet.

The eventual typography choice must be introduced through font and typography tokens so families can change globally without rewriting component markup.

Previously proposed font pairings remain examples only and are not authoritative.

## UX-006-03 — Token-first design authority
**Status:** LOCKED / FOUNDATIONAL

NewYou uses a token-first visual architecture inspired by the maintainability principles demonstrated by Automatic.css.

Developers and designers should normally work with governed tokens such as:

- `--primary`;
- `--surface`;
- `--text-primary`;
- `--space-m`;
- `--section-space-m`;
- `--radius-m`;
- `--text-m`;
- `--heading-size`;
- `--content-width`;
- `--gutter`;

rather than memorising raw colour, spacing, radius or typography values.

## UX-006-04 — Token layers
**Status:** LOCKED

Use a lean three-layer model:

1. primitive/foundation tokens;
2. semantic tokens;
3. component tokens only where a component genuinely needs a stable local contract.

Do not pre-create thousands of component tokens.

## UX-006-05 — Native CSS variables are the runtime token substrate
**Status:** LOCKED

CSS custom properties are the primary runtime representation of visual tokens.

They must support global and contextual overrides so themes, calculations, responsive values and components remain centrally adjustable.

## UX-006-06 — ACSS-inspired mathematical system
**Status:** LOCKED_WITH_JIT_DETAIL

NewYou should adopt useful mathematical ideas demonstrated by Automatic.css, adapted for Phoenix/Tailwind:

- fluid responsive spacing;
- fluid responsive typography;
- consistent mathematical scales;
- dedicated section spacing where useful;
- global gutter/content-width variables;
- small `calc()` adjustments based on existing tokens;
- `clamp()`, `min()`, `max()` and `minmax()` where appropriate;
- semantic colour relationships;
- logical properties;
- reusable calculations/recipes where repetition justifies them.

Avoid magic numbers when a governed token or token-derived calculation expresses the intent correctly.

## UX-006-07 — ACSS study/reference requirement
**Status:** LOCKED

Before freezing the NewYou token engine and during major design-system expansions, the planning/implementation agent should review relevant current Automatic.css public documentation.

Where the user lawfully provides access to licensed ACSS source/SCSS material, the agent may study implementation patterns for:

- variables;
- spacing and section-spacing scales;
- typography scales;
- fluid formulas;
- colour relationships/partials;
- recipes/functions;
- auto-spacing;
- grid/layout patterns;
- accessibility-oriented defaults.

Automatic.css is a research/reference input, not a runtime dependency.

Do not copy proprietary source code without appropriate rights.

## UX-006-08 — No unnecessary Sass/SCSS layer with Tailwind v4
**Status:** LOCKED

Tailwind v4 is treated as the CSS build/theme integration layer.

Do not add Sass/SCSS merely to reproduce Automatic.css internals.

Prefer modern CSS capabilities and Tailwind's CSS-first theme mechanism.

A future additional preprocessor requires a concrete justification.

## UX-006-09 — Tailwind maps to tokens; Tailwind is not design authority
**Status:** LOCKED

Tailwind may expose and consume NewYou tokens.

Tailwind class availability does not authorise arbitrary palette, spacing, radius, typography or breakpoint values outside the design system.

## UX-006-10 — Clean-markup styling hierarchy
**Status:** LOCKED

Preferred hierarchy:

semantic reusable component/pattern
→ concise semantic class or Phoenix component API
→ governed CSS using tokens
→ Tailwind utilities where they add clear local composition value.

Avoid both repeated long utility strings everywhere and giant monolithic classes that hide unrelated behaviour.

## UX-006-11 — Component markup cleanliness
**Status:** LOCKED

Repeated visual contracts should be encapsulated in reusable Phoenix components/patterns and semantic CSS rather than repeated long class strings throughout HEEx.

HTML/HEEx should communicate structure and intent first.

Do not create a custom class for every single element merely for class-count aesthetics.

## UX-006-12 — Fluid typography system
**Status:** LOCKED_WITH_JIT_DETAIL

Typography uses a governed fluid scale where appropriate.

Exact font families and final numerical scale remain deferred.

Major text sizes may use token-derived `clamp()` behaviour across the supported width continuum.

## UX-006-13 — Readable prose measure
**Status:** LOCKED_WITH_JIT_DETAIL

Long-form prose uses a controlled readable measure rather than stretching across wide displays.

The final value is tokenised and globally adjustable.

## UX-006-14 — Governed fluid spacing system
**Status:** LOCKED_WITH_JIT_DETAIL

Use a compact t-shirt-style spacing scale such as:

`3xs / 2xs / xs / s / m / l / xl / 2xl / 3xl`

or final approved equivalent.

Spacing tokens may be mathematically generated from base values/scales and fluidly interpolate where useful.

Use dedicated section spacing and gutter tokens where appropriate.

## UX-006-15 — Token-derived calculations
**Status:** LOCKED

Fine adjustments should normally derive from existing tokens rather than introducing unrelated raw values.

If a calculation recurs, promote it to a named token/recipe.

## UX-006-16 — Radius system
**Status:** LOCKED_WITH_JIT_DETAIL

Use a small governed radius scale with restrained rounding.

Exact values remain tokenised and adjustable.

## UX-006-17 — Border-first, shadow-second elevation
**Status:** LOCKED

Prefer surface contrast and subtle borders before heavy shadowing.

Use a small elevation token set rather than pervasive floating-card treatment.

## UX-006-18 — Semantic container system
**Status:** LOCKED_WITH_JIT_DETAIL

Use named containers such as:

- prose;
- narrow;
- standard;
- wide;
- dashboard;
- full.

Exact dimensions remain tokenised.

## UX-006-19 — Grid/layout doctrine
**Status:** LOCKED

Prefer modern intrinsic layout:

- CSS Grid for two-dimensional composition;
- Flexbox for one-dimensional alignment;
- `minmax()`;
- `repeat()`;
- `auto-fit` / `auto-fill`;
- `subgrid` where justified.

## UX-006-20 — Breakpoints are composition thresholds
**Status:** LOCKED_WITH_JIT_DETAIL

Breakpoints represent layout/composition thresholds, not named devices.

Final values are governed tokens.

## UX-006-21 — Container-query-first reusable components
**Status:** LOCKED

When reusable component behaviour depends primarily on allocated width, prefer container queries.

Use media queries for viewport/environment/page-level concerns.

## UX-006-22 — Resizable responsive preview
**Status:** LOCKED

The official preview pattern supports:

- continuously draggable/resizable width;
- visible current simulated width;
- preset widths;
- fullscreen;
- locale/language;
- applicable theme/product space.

Preset widths are review shortcuts, not the definition of responsiveness.

## UX-006-23 — Floating-label form pattern
**Status:** LOCKED / REPLACES TRADITIONAL ABOVE-FIELD DEFAULT

NewYou forms use a minimal floating-label pattern by default where appropriate.

Visual behaviour:

empty / idle:
label appears inside the input area

focus or existing value:
label moves upward within the control and remains visible.

The field must use a real programmatically associated label, not placeholder-only text.

The label remains visible while typing and after a value exists.

The system must correctly handle:

- keyboard focus/tab navigation;
- browser autofill;
- password managers;
- pre-populated values;
- validation errors;
- disabled/read-only states;
- required/optional semantics;
- long Afrikaans and English labels;
- screen readers;
- adequate contrast;
- touch targets;
- textarea/select/date/combobox variants where appropriate.

Helpful hint text and errors may appear beneath the field.

Where floating labels would reduce usability for a specific control type, an explicitly justified alternate pattern is allowed.

## UX-006-24 — Limited action hierarchy
**Status:** LOCKED

Standardise a small hierarchy:

- primary;
- secondary;
- tertiary/ghost;
- destructive;
- link.

## UX-006-25 — Cards are not universal layout wrappers
**Status:** LOCKED

Use cards only for meaningful grouping/object/interaction.

Editorial layouts should often rely on whitespace, typography, grid and separators.

## UX-006-26 — Consistent restrained iconography
**Status:** LOCKED_WITH_JIT_DETAIL

Use one coherent icon language.

A package such as Lucide may be evaluated JIT, but is not frozen.

## UX-006-27 — Photography direction
**Status:** LOCKED

Primary photography direction:

- natural light;
- real environments;
- realistic women;
- restrained processing;
- everyday movement/life;
- food/nature/human connection;
- representative ages/body shapes/contexts where appropriate.

Avoid generic spa, medical-stock and influencer aesthetics.

## UX-006-28 — Status is never colour-only
**Status:** LOCKED

Status meaning uses text/labels and, where useful, icons/shapes in addition to colour.

## UX-006-29 — Small motion token system
**Status:** LOCKED_WITH_JIT_DETAIL

Use a small motion duration/easing token set.

Exact timings remain tokenised.

Reduced-motion behaviour is mandatory.

## UX-006-30 — Loading hierarchy
**Status:** LOCKED

Prefer:

- instant local feedback;
- scoped pending state;
- skeleton where structure is known;
- spinner where appropriate.

Avoid whole-page blocking spinners for small LiveView updates.

## UX-006-31 — Responsive media
**Status:** LOCKED

Use responsive media techniques and server/CDN derivatives.

Avoid serving unnecessarily oversized media and relying on CSS alone to shrink it.

## UX-006-32 — One system, participant/operator composition modes
**Status:** LOCKED

Use one design system:

participant composition:
calmer, more spacious, editorial/guided.

operator composition:
more information-dense, queue/table/action efficient.

Do not create a separate admin design system.

## UX-006-33 — Intentional print styles
**Status:** LOCKED_WITH_JIT_DETAIL

Provide intentional print styling for applicable plans, recipes, reports and content.

Not every screen needs print support.

## UX-006-34 — Component admission rule
**Status:** LOCKED

A reusable component enters the system only when there is a real requirement, meaningful reuse, understood states, accessibility behaviour and responsive behaviour.

Do not build speculative component libraries.

## UX-006-35 — Reusable component state contract
**Status:** LOCKED

Reusable components document only applicable states, including where relevant:

- default;
- hover;
- focus;
- active;
- disabled;
- loading;
- error;
- empty;
- selected;
- restricted;
- responsive variants.

## UX-006-36 — Theme architecture
**Status:** LOCKED

Use:

core/foundation tokens
→ semantic experience tokens
→ NewYou women's theme.

Future product themes override semantic values without rewriting reusable component logic.

## UX-006-37 — CSS-first frontend restraint
**Status:** LOCKED

Prefer semantic HTML + modern CSS + LiveView before adding JavaScript.

Use JavaScript for interactions that genuinely require it.

## UX-006-38 — Frontend token/performance discipline
**Status:** LOCKED

Keep the token system lean.

Avoid:

- enormous unused token sets;
- duplicate equivalent variables;
- many arbitrary one-off utilities;
- unnecessary CSS/JS frameworks;
- runtime work that modern CSS can express statically.

The JIT performance pass applies to frontend CSS/JS/component work.

---

# 17. UX-006 Source-Study Rule

Automatic.css is an explicit design-system research reference for NewYou because its public documentation demonstrates useful approaches to:

- variable-first styling;
- mathematical fluid spacing;
- mathematical fluid typography;
- contextual/section spacing;
- token-based calculations;
- semantic colour systems;
- minimal utility use with reusable classes;
- recipes/functions;
- maintainable global adjustment.

NewYou is not an Automatic.css port and does not depend on WordPress.

Tailwind remains the implementation/build framework, while NewYou's semantic token model remains design authority.

---

# 18. Regression Gate for UX-007

Before accepting UX-007 or later decisions, verify they do not regress:

- UX-FND-001...005;
- UX-001-01...12;
- UX-002-01...20;
- UX-003-01...24;
- UX-ACQ-001;
- UX-004-01...30;
- UX-OPS-001;
- UX-005-01...40;
- DELIV-PERF-001;
- UX-006-01...38.

Any contradiction requires explicit amendment/supersession.

---

# 19. UX-007 — Integration, SEO, Search, Consent & Frontend Reliability

## UX-007-01 — SEO is first-class launch correctness
**Status:** LOCKED / FOUNDATIONAL

SEO is important from the start and is part of public publishing correctness, not a post-launch marketing enhancement.

Every relevant public Feature Pack/JIT slice must explicitly evaluate and implement the applicable SEO contract, including where relevant:

- crawlability/indexability;
- canonical URLs;
- title and meta description;
- Open Graph/social metadata;
- XML sitemap participation;
- `robots.txt`;
- breadcrumb navigation and breadcrumb structured data;
- content-type-appropriate structured data/schema;
- redirect handling;
- language/locale metadata and alternate-language relationships where applicable;
- image metadata/performance;
- internal linking;
- public-page performance;
- safe noindex behaviour for non-public/private/system pages.

SEO correctness is included in acceptance criteria for public pages where applicable.

## UX-007-02 — Clean stable canonical public URLs
**Status:** LOCKED

Public content uses clean, stable, human-readable canonical URLs that are not coupled unnecessarily to internal Resource IDs or database implementation.

## UX-007-03 — Governed redirects
**Status:** LOCKED

When an established public URL changes, use a governed redirect where appropriate. Redirect handling must avoid loops, excessive chains and silent destruction of historical public routes.

## UX-007-04 — Content-derived structured data
**Status:** LOCKED_WITH_JIT_DETAIL

Relevant public content types may emit valid structured data derived from authoritative governed fields. Candidate schema families include Article, Recipe, Event, FAQ, BreadcrumbList, Organization/WebSite and other legitimate site-level schema. Do not fabricate schema fields merely to increase search visibility. Exact schema contracts remain JIT by content/page type.

## UX-007-05 — Content-aware social metadata
**Status:** LOCKED

Public content uses content-aware social title/description/image metadata with governed site-level fallbacks.

## UX-007-06 — Native public search is approved but evidence-timed
**Status:** LOCKED_WITH_JIT_DETAIL

NewYou may provide native policy-aware public search over approved public content once content volume/usefulness justifies it. Search is not an FP-001 prerequisite merely for completeness.

## UX-007-07 — Deterministic search first
**Status:** LOCKED

Initial public search should use deterministic relevance over approved content fields/taxonomies/recency/boosts. Semantic/vector/AI ranking is evidence-gated and must demonstrate value before introduction.

## UX-007-08 — Bounded performance signals in discovery
**Status:** LOCKED_WITH_JIT_DETAIL

Trusted content-performance signals may later contribute to search/recommendation/promotion ranking alongside semantic relevance, freshness, quality, eligibility and editorial governance. Commercial performance must not completely override relevance or safety/editorial rules.

## UX-007-09 — Minimal non-manipulative consent UX
**Status:** LOCKED_WITH_JIT_DETAIL

Consent/tracking UX is clear, minimal and non-manipulative. Genuinely necessary functionality may operate under its applicable lawful basis; optional analytics/marketing categories follow Privacy & Consent law. Exact consent categories, wording and legal basis remain expert/privacy authority.

## UX-007-10 — Persistent consent controls
**Status:** LOCKED

Applicable consent/privacy choices remain discoverable and changeable after the initial decision. Users must not need to clear browser data or contact Support merely to manage applicable consent.

## UX-007-11 — Cloudflare Zaraz is preferred analytics/tag integration boundary
**Status:** LOCKED_WITH_JIT_DETAIL

Where NewYou uses Cloudflare, Cloudflare Zaraz is the preferred initial integration boundary for supported third-party analytics/marketing tools, including Google Analytics 4.

Rationale from current Cloudflare documentation:

- Zaraz has native support for Google Analytics / GA4;
- Zaraz can offload supported third-party tooling to Cloudflare;
- Zaraz provides consent-management integration and supports Google Consent Mode v2;
- Cloudflare states that Google Tag Manager can be loaded through Zaraz but does not recommend doing so because tools configured inside GTM cannot be optimised by Zaraz or restricted through Zaraz privacy controls and still require additional client-side JavaScript.

Therefore:

1. prefer native Zaraz integrations for supported tools;
2. prefer NewYou first-party event contracts as the source application instrumentation;
3. map approved events into Zaraz/GA4 where useful;
4. use GTM only when a concrete tag-management/integration requirement remains that Zaraz does not satisfy cleanly;
5. do not hardcode optional analytics/marketing scripts across page templates;
6. preserve replaceability of Cloudflare/Google tooling.

Final provider configuration remains JIT and must be reverified against then-current provider capabilities.

## UX-007-12 — Preserve useful analytics under privacy governance
**Status:** LOCKED / FOUNDATIONAL

NewYou should preserve as much analytically useful, trustworthy first-party behavioural, content, funnel and performance signal as is lawfully and ethically appropriate because those signals enable UX, funnel, content, SEO, operational, product and performance improvement and future governed recommendation/promotion algorithms.

This is not permission to collect everything. Every signal remains subject to purpose, minimisation, consent/legal basis where required, retention, deletion, sensitive-data restrictions, access controls and data-quality semantics. Prefer high-value explicit event contracts over indiscriminate DOM/event surveillance.

## UX-007-13 — Third-party non-authoritative outage isolation
**Status:** LOCKED

Failure of non-authoritative analytics/marketing integrations such as GA4/GTM/Zaraz/Search Console ingestion must not break core public/participant functionality.

## UX-007-14 — Provider-critical degraded states
**Status:** LOCKED

When an externally dependent critical operation cannot resolve, expose a governed pending/degraded state that clearly distinguishes what is known, what is not yet known, what was safely persisted and the safest next action. Never fabricate success.

## UX-007-15 — HTML/server-rendered baseline
**Status:** LOCKED

Public content and fundamental navigation use server-rendered semantic HTML as the baseline. JavaScript progressively enhances the experience rather than becoming a prerequisite for reading ordinary public content.

## UX-007-16 — Full offline/PWA is evidence-gated
**Status:** LOCKED

Do not build full offline/PWA capability without a demonstrated requirement. Provide graceful connection-loss/retry behaviour and safe local preservation only where justified.

## UX-007-17 — Modern evergreen browser support
**Status:** LOCKED_WITH_JIT_DETAIL

Target an explicit implementation/release-tested matrix of current supported evergreen browsers. Do not freeze permanent version numbers in this planning law. Do not constrain the platform to Chrome only or carry indefinite legacy-browser complexity without evidence.

## UX-007-18 — Modern CSS within support matrix
**Status:** LOCKED

Use modern CSS capabilities such as Grid, container queries, `clamp()`, `minmax()` and other approved features when supported by the release browser matrix. Provide graceful fallbacks only where a genuinely supported browser needs them.

## UX-007-19 — Privacy-safe frontend observability
**Status:** LOCKED_WITH_JIT_DETAIL

Collect governed browser/LiveView error telemetry sufficient for actionable diagnosis, including release/version correlation and relevant technical context. Do not indiscriminately capture sensitive form values, health data, credentials or private user content in telemetry.

## UX-007-20 — Proportionate real-user frontend performance evidence
**Status:** LOCKED_WITH_JIT_DETAIL

Collect useful first-party frontend/perceived-performance signals where justified, including appropriate page/asset/LiveView responsiveness and web-vital-style measurements. Telemetry must remain proportionate and purpose-bound.

## UX-007-21 — User-visible correlation reference
**Status:** LOCKED_WITH_JIT_DETAIL

Unexpected user-facing failures may expose a short opaque correlation/reference ID when it materially helps Support connect the user report to backend/frontend telemetry. Do not expose internal stack traces or sensitive identifiers.

## UX-007-22 — Automated + human accessibility verification
**Status:** LOCKED

Accessibility uses both automated regression checks for common failures and human keyboard/screen-reader/interaction verification for meaningful workflows. Automated tooling alone is insufficient proof.

## UX-007-23 — Selective visual regression
**Status:** LOCKED

Use visual regression selectively for stable reusable components and critical flows where it offers strong protection. Do not blanket pixel-test every screen when that produces brittle maintenance with low value.

## UX-007-24 — Selective Search Console ingestion
**Status:** LOCKED_WITH_JIT_DETAIL

NewYou may ingest selected Search Console aggregates/metrics when doing so materially improves editorial/SEO/acquisition decisions. Do not attempt to reproduce the entire Search Console product.

## UX-007-25 — Focused Content & Organic Acquisition dashboard
**Status:** LOCKED_WITH_JIT_DETAIL

Provide a focused Content & Organic Acquisition dashboard when required by delivery scope, combining trusted first-party content/funnel data with selected Search Console/approved external evidence. It should answer useful questions such as which pages gain/lose organic traffic, attract search users but under-convert, convert strongly but have weak organic reach, and contribute to downstream email/account/purchase outcomes. Do not build a full Ahrefs/Semrush replacement.

## UX-007-26 — Governed third-party embed wrappers
**Status:** LOCKED

Approved third-party embeds use explicit governed components/wrappers controlling privacy/consent behaviour, responsiveness, loading/performance, provider allow-listing and failure/degraded behaviour. Do not permit arbitrary embed scripts/HTML in ordinary content.

## UX-007-27 — Strict rich-content sanitisation
**Status:** LOCKED

Any participant/community rich-content capability must use allow-listed rendering/sanitisation. Arbitrary scripts/styles/embeds are prohibited.

## UX-007-28 — Progressive enhancement doctrine
**Status:** LOCKED / FOUNDATIONAL

Server-rendered semantic HTML and authoritative LiveView behaviour form the baseline; CSS and JavaScript progressively enrich the experience without becoming hidden business authority.

---

# 20. Final UX Register Regression Gate

Before synthesis/freeze:

- preserve all prior LOCKED decisions;
- exact colour palette remains deferred;
- exact font families remain deferred;
- no dashboard builder is introduced;
- SEO remains first-class from the start;
- analytics capture is maximised only within explicit privacy/purpose constraints;
- Cloudflare Zaraz is preferred over GTM-through-Zaraz where supported;
- native NewYou facts remain authoritative over third-party analytics;
- no implementation is authorised by this register alone.

Any contradiction requires explicit amendment/supersession.
