# FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md

- **Status:** FROZEN / COMPLETE FRONTEND EXPERIENCE SYSTEM
- **Document version:** v1.0.0
- **Frozen working source:** `archive/FRONTEND_EXPERIENCE_SYSTEM_WORKING_v0.2.0.md`
- **Frozen working source SHA-256:** `635cd997641409f876e9d6d5ff00b61aecffef8d75d310bec24f2e897f286aa4`
- **Previous source:** `archive/FRONTEND_EXPERIENCE_SYSTEM_WORKING_v0.1.0.md`
- **Previous source SHA-256:** `05ca75c89d12f9de1704f452be45edd07263a3c7fc9e6b4f176732e9cd91009a`
- **Derived from:** `working/EXPERIENCE_DECISIONS_WORKING_v0.7.0.md`
- **Current authority basis:** Product Law, Architecture, Domain Law, Roadmap and the frozen `PLATFORM_OPERATING_MODEL_v1.0.0.md`
- **Authority boundary:** Subordinate to Product Law, Architecture, Domain Law, Roadmap and the frozen Platform Operating Model. The Experience Decision Register is cumulative working provenance and does not override upstream authority.
- **Governs:** frontend-experience, design-system and interaction contracts for in-scope frontend, UI and public-experience planning.
- **Authority status:** CURRENT / CONDITIONALLY LOADED FRONTEND AUTHORITY
- **Date:** 2026-08-24
- **Implementation:** NOT AUTHORISED BY THIS DOCUMENT
- **JIT boundary:** Exact implementation and design detail remains deferred to the affected Feature Pack and JIT contracts.
- **Freeze status:** FROZEN / COMPLETE

This frozen artifact preserves the final v0.2.0 working synthesis without semantic expansion. The v0.2.0 working artifact is archived byte-for-byte, and the v0.1.0 source remains preserved as historical provenance.

---

# 1. Authority, scope and boundary

The governing order is:

```text
Product Law
→ Architecture
→ Domain Law
→ Roadmap
→ frozen Platform Operating Model
→ Experience Decision Register
→ Frontend Experience System
→ later Feature Pack / JIT frontend contracts
```

An upstream authority wins if wording conflicts. This document may govern:

- information architecture and navigation principles;
- participant and operator interaction doctrine;
- design-token architecture and styling hierarchy;
- responsive behaviour and preview principles;
- forms, loading, errors and degraded states;
- accessibility and progressive enhancement;
- dashboard interaction and frontend analytics boundaries;
- public publishing and SEO requirements;
- browser support and frontend performance review;
- component admission and reusable-pattern state contracts.

It must not become authority for:

- Product decisions or commercial policy;
- Domain business truth or business state machines;
- payment, eligibility, safety, entitlement or access truth;
- content publication authority or translation approval authority;
- analytics business facts or accounting truth;
- provider authority, provider configuration or provider-specific recovery policy;
- clinical, legal, professional, privacy or accounting conclusions.

Frontend state is a projection of current authoritative state. A LiveView assign, browser value, URL, cache, chart, dashboard, work queue, saved view or optimistic interaction cannot create or replace authoritative truth.

Exact routes, folder paths, Phoenix module names, Ash Resources/actions, CSS filenames, Tailwind configuration, token numbers, palette, fonts, hooks, chart versions, Cloudflare configuration and complete component/dashboard inventories remain JIT detail. This document is planning law, not implementation code.

---

# 2. Experience contract

NewYou uses **Editorial Wellness + Modern Product UI**:

- public content is warm, editorial, human and value-first;
- participant journeys are clear, structured, calm and predictable;
- operator work is role-aware, professional and information-dense where useful.

The character is refined and feminine without stereotypical pink, beauty or spa treatment. Real photography is the primary storytelling medium; illustration and restrained iconography support concepts, onboarding, empty states and instructional content.

Participant experiences are comfortably spacious and efficient. Operator experiences may use denser tables, queues and analytics while keeping essential triage, review, approval, communication and urgent actions mobile-safe. One design system serves both composition modes; a separate admin design system is not introduced.

The experience must be:

1. content-first and genuinely public where Product Law permits;
2. journey-oriented for participants and workflow-first for operators;
3. bilingual in Afrikaans and English at the component/content boundary;
4. honest about authoritative, pending, unavailable and degraded states;
5. accessible, responsive and progressively enhanced from the first relevant slice;
6. measurable with useful, minimised first-party signals;
7. compassionate and non-punitive around health, safety and progress.

Use subtle, purposeful motion only. Reduced-motion behaviour is mandatory. Status is never communicated through colour alone.

---

# 3. Conceptual information architecture

These are experience groupings, not a complete route map or a new business-domain model.

## 3.1 Public experience

Public visitors can reach useful educational content, discovery/search when justified, and relevant product, programme or event information without arbitrary client-JavaScript dependence. The public layer exposes:

- a sensible default language immediately;
- a visible Afrikaans / English switcher that remains available;
- clearly discoverable `Create account` and `Log in` access;
- contextual next steps rather than generic forced signup;
- terms, privacy and safety boundaries where relevant.

Public content remains genuinely public where Product Law says it is public. The public surface must not become a wall of disabled future capabilities.

Do not use a blocking language-choice modal before useful public content is visible.

## 3.2 Participant experience

There is one evolving participant Home, conceptually a Home/Today surface, that composes the next best authorised action from current Domain state. It may surface:

- incomplete or resumable journeys;
- active plans and programmes;
- upcoming authorised live/events;
- relevant governed content;
- useful progress and feedback actions.

Do not create a separate Home for each purchased product or a universal participant `Task` authority merely to drive checklists. Navigation follows the participant journey, not internal Domain structure. Only relevant/current capabilities appear; a locked explanation is shown only when discovery or commercial understanding is genuinely useful.

Account/settings areas are grouped conceptually around Profile, Language, Security, Privacy & Consent, Notifications, Purchases/Billing and Data & Account, with only applicable areas shown.

An in-app participant notification centre is an approved eventual capability, not an FP-001 prerequisite.

## 3.3 Operator experience

The default staff landing surface is a role-aware **Command Centre** answering:

- what needs attention;
- what is assigned, unassigned, overdue or at risk;
- what is scheduled or upcoming;
- what exceptions/incidents are active;
- what important data/platform conditions require awareness.

Conceptual operator groupings may include Command Centre, Work, People, Content, Health & Plans, Programmes, Commerce, Community & Events, Communications, Experiments, Analytics and Platform/Audit. These groupings are navigation and operating projections only; they do not create Domains or transfer ownership.

Operator global search is policy-aware across authorised entities. Command capabilities are added only where a real governed action exists. Support receives a scoped workspace with minimum necessary identity/access/commercial/support context. Routine impersonation is prohibited; safe preview/simulation is preferred. Any future true impersonation requires separate governed design, visibility and audit.

---

# 4. Frontend authority and lifecycle rule

The frontend owns presentation and interaction lifecycle state. It does not reproduce universal business lifecycle state machines.

For authoritative transitions, the frontend:

1. submits untrusted intent through the authorised application boundary;
2. shows local and scoped pending feedback;
3. reflects the authoritative Domain result or current state;
4. preserves recoverable work and explains the safest next action;
5. re-reads current authority when a long-lived view or external operation may be stale.

Payment, eligibility, safety, entitlement, access, plan, content publication, professional and accounting success may never be fabricated optimistically. External ambiguity is a pending/verifying/degraded truth, not a convenient success state.

---

# 5. Participant journey and acquisition

## 5.1 Content-led relationship building

The preferred relationship is:

```text
useful public content
→ contextual relevant next step
→ optional permissioned email or account relationship
→ product/programme discovery
→ purchase or entitlement when appropriate
```

Email capture may be offered through a clear, non-blocking exchange of value such as a useful subscription, relevant resource, programme/event update or product follow-up. Do not hide most useful public content behind email, use repeated generic popups as the default, or degrade reading/discovery to force conversion.

Keep these concepts distinct in wording and behaviour:

```text
mailing-list contact ≠ account holder ≠ purchaser ≠ recipient
≠ participant ≠ customer/member ≠ entitlement
```

## 5.2 Registration and verification

Registration is minimal and collects only the current Product-Law account requirements. Health and product-specific data are collected progressively when a defined journey needs them; do not create a universal upfront wizard.

Before email verification, provide a useful verification-pending experience with:

- what happened and why verification matters;
- resend verification;
- change-email recovery where permitted;
- legitimate public/non-sensitive actions that remain available.

Protected application access remains blocked until the applicable verification gate is satisfied.

After verification, provide lightweight orientation. Product-specific onboarding begins when the participant enters that product journey.

## 5.3 Purchase and external ambiguity

After authoritative payment verification and entitlement grant, show a clear confirmation followed by the next authorised action for that purchase.

Before that point, use a distinct `PAYMENT_PENDING` / `VERIFYING` experience:

- do not show access as granted;
- explain what is known and what is still being reconciled;
- discourage duplicate payment;
- provide the safest next action and a reference where useful.

Provider return pages and browser events are evidence/intent, not payment or entitlement authority.

## 5.4 Long journeys, save/resume and progress

Assessment, health intake and other substantial journeys use purposeful sections, clear progress and minimal cognitive load. Not every form is a wizard.

Use durable save/autosave where semantics are safe, a visible `Saved` state or timestamp, and an explicit resume path. Browser-local state alone is not sufficient for important governed progress. On return after interruption, Home offers `Continue` at the correct safe resume point without trapping the participant inside the unfinished flow.

Use exact percentages only when the denominator and completion meaning are honest and stable. Otherwise prefer meaningful section/step progress. Progress language recognises consistency and recovery; missed days do not erase progress, and streaks, failure language, shame and unnecessary leaderboards are avoided.

Completion acknowledgement is proportional: subtle for routine actions, warmer for genuine milestones, without indiscriminate confetti or gamification.

## 5.5 Health and safety interaction

Health forms are calm, plain-language, concise about why sensitive questions are needed, non-judgmental and explicit about safety. Warmth must not weaken safety precision.

Where Product Law permits, preserve the distinctions:

- `unknown`;
- `not_tested`;
- `prefer_not_to_answer`.

When automated personalisation is not permitted, explain the governed safe next outcome—General Wellness, more information required or professional review—as applicable. Do not expose unnecessary internal rule logic, allow participant override of Safety authority, invent clinical thresholds or imply continuous monitoring. External health/provider ambiguity remains pending/degraded truth.

## 5.6 Plan delivery and history

Use a native structured plan experience as the primary participant delivery format. Approved printable/downloadable representations are secondary; a PDF is not the primary authoritative experience.

Default to the current/latest applicable plan/report version while keeping historical delivered versions accessible and clearly labelled. Corrections, replacements and safety withdrawals must not silently erase participant history.

## 5.7 Privacy, security and error recovery

Provide understandable participant-facing Privacy & Data and Security areas for applicable consent, export/data requests, deletion state and consequences, credentials, recovery and supported session/device controls. High-risk actions may require confirmation and re-authentication. Do not expose raw technical authentication telemetry.

Recoverable errors:

- explain the issue in user terms;
- preserve entered work where safe;
- say whether work was saved;
- give the safest next action;
- provide an opaque support/reference identifier where useful;
- never expose stack traces, secrets or provider internals.

---

# 6. Operator Work and workflow doctrine

NewYou presents a unified **Work** experience over Domain-owned obligations. Work is attention, not authority. There is no universal `Task` Resource or universal work lifecycle.

## 6.1 Common work projection

Where the owning workflow supports it, the common operator projection is:

```text
UNASSIGNED → ASSIGNED → IN_PROGRESS → RESOLVED
                         ↘ CHANGES_REQUESTED → IN_PROGRESS
```

Claiming/assigning produces the `ASSIGNED` projection. Domain-specific lifecycle, due times, cancellation and business outcome remain with the owning Domain; `CANCELLED` is shown only where that owner permits it.

## 6.2 Guards and operator semantics

- Queue visibility never grants business-action authority.
- Approval is an explicit role/policy action separate from ordinary editing where law requires it.
- Self-approval is permitted only for low-risk workflows where policy allows it; separation of duties applies to sensitive/high-risk work.
- Bulk actions are allowed only when every selected item can still pass its own policy and invariant checks.
- Due/target times and escalation are workflow-specific; there is no universal SLA or automatic “send every overdue item to Super Admin” rule.
- Changes requested preserve reviewer context/history and return work to the responsible actor; review rejection must not silently close the item.

## 6.3 Work, notifications and evidence

Keep these separate:

- **Work:** an action is required;
- **Notification:** useful durable information;
- **Toast:** transient UI acknowledgement.

Required work must never exist only as a toast, email or ephemeral LiveView state. Internal notes are scoped to the relevant work/case context and remain distinct from participant-visible messages, professional records and append-only audit evidence. Important records may expose a curated, permission-aware business timeline derived from authoritative/audit evidence; the timeline is not a second source of truth.

Essential operator triage, review, approval, communication and urgent actions are mobile-safe. Complex content authoring, dense analytics and advanced data workflows may remain desktop-first while remaining responsively correct.

---

# 7. Content, editorial and media experience

Content operations use the locked **Library + Work Queue + Editorial Calendar** model:

- **Library:** what governed content/media exists;
- **Work Queue:** what requires assignment, review, translation, correction or other action;
- **Editorial Calendar:** what governed content, communication or programme publication milestone is scheduled and when.

The calendar supports relevant content types/milestones and filters such as type, team, product and date. It is not a separate publication authority.

## 7.1 Authoring and composition

Content may begin as an authorised idea/request or direct authorised draft. Both converge on the same governed workflow. Each active item has a responsible editor/owner; reviewers and approvers remain separate roles where applicable.

The creator selects a governed content type before composing. Type controls structure, metadata and applicable workflow. Content uses an extensible, approved catalogue of blocks, sections, content components and composed patterns. The catalogue grows only from real content needs and review; it is not an unrestricted page builder.

Editors may compose approved building blocks but may not inject arbitrary HTML, scripts, styles, ungoverned components or arbitrary embeds. Rich content is allow-listed and sanitised. Reusable templates may precompose approved sections, slots, defaults, metadata and CTA placements, but do not bypass content-type, review, translation, accessibility or publication rules.

Substantial editors/forms use explicit dirty-state handling, safe autosave and a clear saved-state indication. Autosave never implies approval or publication. Meaningful review/publication boundaries create immutable/versioned snapshots; template changes and later edits do not silently rewrite historical published content.

## 7.2 Translation, risk and approval

Afrikaans and English are separately governed variants of one conceptual content identity/version lineage. Translation, content review and specialist/clinical approval remain distinct concerns.

The applicable translation lifecycle is:

```text
missing → draft → machine_draft → language_review
→ clinical_review_required (where risk requires it)
→ approved → published → superseded / withdrawn
```

Each variant has independent state. Translation is explicit assignable work with source version, target locale, assignee, state and required review. Machine translation creates draft material only, records its source version, becomes stale when the source changes and never self-publishes where human or clinical review is required.

Risk/type classification occurs early and can trigger reclassification and renewed review. Derived specialist-review routing places work in the correct queues. Review comments are contextual internal work linked to the relevant draft/version, with history and resolution preserved.

Paid, contractual, assessment, plan, clinical, safety and core-onboarding content require approved bilingual variants. Optional low-risk editorial content may use only an explicit fallback that tells the participant the selected translation is unavailable; it must not silently switch language. Exact translation-resource and approval implementation remains JIT.

## 7.3 Preview, scheduling and publication

Authorised operators can preview the exact target experience with:

- selected locale;
- applicable product/theme context;
- real governed content presentation;
- component/template composition;
- continuously draggable/resizable width;
- visible current simulated width;
- convenient preset widths;
- fullscreen where useful.

Presets are review shortcuts, not the definition of responsiveness. Preview is not an unstyled generic approximation.

Scheduling requires an approved/publishable version, explicit timezone, previewable schedule and visible scheduled/queued state. Conflicts/dependency issues are warnings unless a governed requirement is actually violated; the system must not silently reschedule.

Scheduled publication is durable, idempotent, observable and reconciled. If publication cannot complete within the approved window, show a visible operator exception/work item. A scheduler attempt never proves that content was published.

Corrections preserve provenance. Ordinary corrections create corrected/superseding versions. Safety, legal/consent or materially incorrect content has an expedited withdrawal/correction path with dependency discovery, affected-delivery handling, participant/operator consequences where required and audit/evidence. Withdrawn content stops public delivery while governed internal history remains; historical participant references receive a clear withdrawn/replaced explanation where needed.

Review-by/freshness dates are optional or required according to content type/risk. There is no universal one-year expiry rule.

## 7.4 Content analytics and funnels

Editors may see concise governed performance summaries and links into deeper Analytics. Only approved metric definitions appear.

Approved contextual CTA/funnel definitions may be placed within content according to user intent. Funnel semantics, eligibility, consent and tracking remain governed. Reusable CTA/funnel definitions avoid repeated hardcoded markup and do not turn the frontend into a conversion authority.

## 7.5 Media and editorial search

The governed Media Library preserves source/provenance, metadata, rights/attribution where applicable, derivatives, usage references and replacement/version semantics. Serve appropriate responsive derivatives rather than unnecessarily large originals; material replacements preserve lineage and update references according to usage semantics.

Operator editorial search/filtering may include text, type, locale, lifecycle, risk, owner, reviewer, taxonomy, publication date/status and product/programme association. It is policy-aware and not arbitrary SQL-style querying.

---

# 8. Design-system and token architecture

Design authority is token-first:

```text
foundation tokens
→ semantic experience tokens
→ component tokens only where a stable local contract is justified
→ product/theme overrides
→ semantic components and patterns
```

Native CSS custom properties are the runtime token substrate. The product/theme layer may override semantic values without rewriting reusable component logic.

Use semantic relationships such as surface, text, border, focus, success, warning, danger and information. The exact NewYou palette is deferred. The exact editorial/application font families are deferred. No component or template may depend on remembered raw colour values or font names.

The deferred visual direction remains a warm neutral base with one distinctive brand-colour family, restrained natural accents and semantic status colours. Typography remains conceptually an editorial serif for expressive/headline/content moments paired with a highly legible sans-serif for application UI. Shape language is moderately soft with restrained rounding.

## 8.1 Mathematical and responsive token rules

Keep the token system lean. Use governed fluid typography, readable prose measure, a compact spacing scale, section-spacing/gutter/content-width tokens, restrained radius/elevation/motion tokens and token-derived calculations. Prefer:

- `calc()` for relationships;
- `clamp()` for governed fluid scales;
- `min()` and `max()` for bounded values;
- `minmax()` for intrinsic grid tracks;
- semantic colour relationships;
- logical properties;
- reusable recipes when a calculation recurs.

Avoid scattered magic numbers, duplicate variables, enormous unused token sets and arbitrary one-off utilities.

Automatic.css is research/inspiration for variable-first and mathematical systems, not a WordPress dependency or runtime library. Only lawful public or user-provided licensed material may be studied or copied; proprietary source is not copied into NewYou. Do not add Sass/SCSS merely to imitate Automatic.css.

Before a future token-engine implementation or major design-system expansion, review relevant current public Automatic.css documentation where available. This remains a study/reference step; it does not make Automatic.css a runtime dependency or permit copying proprietary source.

Tailwind v4 is implementation/build syntax. It may map to and consume NewYou tokens, but class availability does not authorise arbitrary design values. The preferred composition is:

```text
semantic Phoenix/component API
→ semantic/token-driven CSS
→ Tailwind utilities for clear local composition where useful
```

Avoid both giant uncontrolled utility strings and unnecessary custom abstraction for every trivial element. Repeated visual contracts belong in semantic components/patterns and token-driven CSS; markup should communicate structure and intent.

## 8.2 Layout and composition

Use CSS Grid for two-dimensional layout and Flexbox for one-dimensional alignment. Prefer intrinsic sizing, `minmax()`, `repeat()`, `auto-fit`, `auto-fill`, `subgrid` where justified, fluid scales and responsive media.

Breakpoints are composition thresholds, not device labels. Use container queries when component allocation drives behaviour; use media queries for viewport, environment and page-level constraints. Participant composition is calmer, spacious and guided; operator composition is denser and queue/table efficient within the same design system.

Use a limited action hierarchy (primary, secondary, tertiary/ghost, destructive, link), cards only for meaningful grouping, and one restrained icon language. Prefer surface contrast and subtle borders before heavy shadows. Applicable plans, recipes, reports and content receive intentional print styles.

Use named semantic container roles such as prose, narrow, standard, wide, dashboard and full; exact dimensions remain tokenised. Motion uses a small duration/easing token set and always honours reduced-motion preferences.

## 8.3 Forms

Floating labels are the preferred field pattern where appropriate:

- empty/idle: a real associated label appears inside the field area;
- focus, value, autofill or prepopulation: the label floats and remains visible.

Never use placeholder-only labels. The pattern must be keyboard-safe, screen-reader-safe, autofill/password-manager-safe and validation-safe, and must support:

- visible focus;
- disabled/read-only states;
- required/optional semantics;
- long bilingual labels;
- adequate contrast and touch targets;
- textarea/select/date/combobox variants where appropriate.

Hint and error text may appear beneath the control. Where floating labels reduce usability for a control, use an explicitly justified alternate presentation.

## 8.4 Component admission and state contract

A reusable component/pattern enters the system only with a real use case, meaningful reuse, understood applicable states, accessibility behaviour and responsive behaviour. Do not build a speculative component inventory.

Reusable contracts document only relevant states, such as default, hover, focus, active, disabled, loading, error, empty, selected, restricted and responsive variants. A component contract cannot create business authority.

---

# 9. Responsive, browser and accessibility contract

Full responsiveness is a property of the supported width continuum, not a mobile/tablet/desktop checklist. Use intrinsic layouts, fluid scales, logical properties, responsive media, container queries and page-level media queries as appropriate.

The implementation/release process maintains an explicit tested evergreen-browser matrix. Do not freeze permanent version numbers here, constrain the product to one browser, or carry legacy-browser complexity without evidence. Modern CSS is valid within that matrix; provide graceful fallback only where a genuinely supported environment needs it.

Accessibility is baseline correctness:

- semantic HTML;
- keyboard access and visible focus;
- real associated labels;
- errors linked to controls;
- adequate contrast and no colour-only status;
- reduced motion;
- zoom/reflow and responsive text/layout;
- adequate touch targets;
- accessible chart/data alternatives;
- correct LiveView focus handling.

Verify common failures with automation and verify meaningful workflows with human keyboard, screen-reader and interaction checks. Automated checks alone are insufficient. Use visual regression selectively for stable reusable components and high-value flows/responsive states; do not blanket pixel-test every screen.

---

# 10. Frontend presentation state and feedback

## 10.1 Form presentation state machine

These are frontend interaction states, not business states:

```text
EMPTY_IDLE → EMPTY_FOCUSED → FILLED_FOCUSED → FILLED_IDLE
                         ↘ INVALID
any permitted state → DISABLED
any permitted state → READ_ONLY
```

The explicit state vocabulary is:

- `EMPTY_IDLE`;
- `EMPTY_FOCUSED`;
- `FILLED_IDLE`;
- `FILLED_FOCUSED`;
- `VALIDATING`;
- `INVALID`;
- `DISABLED`;
- `READ_ONLY`.

States remain revisitable while the parent workflow is active. Validation errors preserve input where safe, associate errors with controls and do not rely on colour alone.

Form presentation guards are limited to interaction conditions such as focus, value, autofill, validation progress and parent-workflow permission for disabled/read-only presentation. Side effects are limited to label, focus, error and feedback presentation plus safe input preservation; they do not mutate Domain truth. Form states remain revisitable while the parent workflow permits it, so correction and recovery remain possible.

## 10.2 Asynchronous interaction state machine

For a meaningful frontend action, the presentation lifecycle may be:

```text
IDLE → SUBMITTING → SUCCESS
              ↘ VALIDATION_ERROR
              ↘ CONFLICT
              ↘ PENDING_EXTERNAL → SUCCESS
                                  ↘ REQUIRES_ATTENTION
```

`PENDING_EXTERNAL` is used for authoritative provider/system ambiguity where reconciliation is safe. `REQUIRES_ATTENTION` is used when a safe automatic resolution is unavailable. The frontend never skips from click to critical success without authoritative confirmation.

Async guards are scoped to actionable intent, current permission and authoritative confirmation where correctness requires it. Side effects are scoped pending feedback, duplicate-submit protection, recoverable-work preservation and re-reading the authoritative projection. `SUCCESS` terminates the current interaction only after confirmation; validation errors, conflicts and requires-attention outcomes remain recoverable through correction, retry or support where permitted.

## 10.3 Loading and error hierarchy

Prefer:

```text
instant local feedback
→ scoped pending state
→ skeleton where structure is known
→ spinner where appropriate
```

Do not use a full-page blocking spinner for a small LiveView operation. Preserve recoverable work. Friendly unexpected-error messages contain no stack trace and may include a short opaque correlation/reference ID.

Third-party non-authoritative analytics, marketing, search or embed failures must not break core public/participant use where avoidable. A provider-critical operation that cannot resolve gets an explicit pending/degraded state describing what was persisted, what is unknown and the safest next action.

## 10.4 Progressive enhancement and offline boundary

Server-rendered semantic HTML and authoritative LiveView behaviour form the baseline. CSS and JavaScript progressively enrich the experience without becoming hidden business authority. Public content/navigation remains useful without arbitrary client-JavaScript dependence. Use JavaScript only for genuine browser-side interaction.

Connection loss may receive graceful retry and safe local preservation where justified. Full offline/PWA capability is evidence-gated and is not a default architectural requirement.

---

# 11. Dashboards and analytics UI

Analytics opens to a role-aware Analytics Home with approved canonical dashboards, supported saved filter/view presets, freshness/data-health state and concise relevant insights. It must not open to a blank builder, raw event explorer or unrestricted database view.

## 11.1 Canonical dashboard governance

Use purpose-built canonical dashboards and permitted saved views, not a general dashboard builder. Each canonical dashboard has a business owner accountable for meaning/use and an analytical steward accountable for metric/data quality. Analysts may prepare/validate drafts; governed approval is required to publish canonical/shared dashboards.

Canonical dashboards use governed metric contracts, dimensions, filters, charts/tables, comparisons, drill-down paths and freshness semantics. A canonical metric has an explicit semantic/business owner and lifecycle such as:

```text
DRAFT → REVIEW → APPROVED → ACTIVE → SUPERSEDED / RETIRED
```

Metric definition versions preserve compact meaning—formula, authoritative source facts, time basis/timezone, dimensions/exclusions, freshness and quality rules—not duplicate copies of all raw data. Historical snapshots are retained only where a material decision/report requires reproducibility.

## 11.2 Query interaction and trust states

Filters, date ranges, comparison periods, timezone semantics and sensible default periods are explicit and permission-aware. A filter/date/comparison/refresh interaction updates the relevant LiveView/data region automatically; a browser reload is not required.

Dashboard presentation states include:

- `CURRENT`;
- `REFRESHING`;
- `CURRENT_UPDATED`;
- `STALE`;
- `PARTIAL`;
- `DELAYED`;
- `UNAVAILABLE`;
- `ERROR`;
- `NO_DATA`;
- `RESTRICTED`.

Show material freshness and data-quality warnings. Distinguish, where meaningful:

```text
true zero ≠ no observations ≠ not applicable
         ≠ not yet available ≠ restricted ≠ unavailable/error
```

Do not silently fill missing authoritative values or render unknown data as zero. Realtime refresh/freshness is a projection; the source Domain remains authoritative.

## 11.3 Drill-down, export and views

Drill-down inherits or tightens row/field/purpose permissions; dashboard visibility never grants sensitive record access. Export is a separate permission enforcing the same controls. Large exports use bounded durable async generation, secure artifact lifecycle, expiry where appropriate, notification and audit; do not load large exports into LiveView or browser memory.

Saved views may preserve filters, periods, sorting/grouping and permitted presentation preferences, but never create dashboard forks or redefine canonical metrics. Time-bound governed annotations may record launches, incidents, methodology changes, pricing/content releases or provider disruptions.

If filter state is bookmarkable or shareable, it must not place sensitive participant identifiers or protected data in the URL.

Start with deterministic thresholds and actionable work/notifications. Anomaly detection is evidence-gated; it is not an MVP requirement. General management dashboards use minimised aggregates; private journals and full clinical/professional records do not belong there.

Governed cohort analysis may compare explicit cohorts such as programme editions, acquisition cohorts or membership-start cohorts using privacy-safe dimensions. It does not create a general-purpose segmentation builder.

## 11.4 Attribution and experimentation

First-party event contracts may connect approved public content/funnel activity to permissioned email, account, verified purchase, assessment, programme and other authorised outcomes. Native NewYou facts remain authoritative for business results. External GA4/GTM/Zaraz/Search Console data is complementary evidence.

Selected Search Console aggregates may feed a focused Content & Organic Acquisition view when that materially improves editorial/SEO decisions. This is not a replacement for Search Console or a full SEO-tool product.

Attribution is not automatically causal proof. Trusted content-performance signals may later inform derived ranking/recommendation/promotion without overriding relevance, safety, quality or editorial governance.

Anonymous-to-known continuity is allowed only under explicit privacy/consent rules and proven architecture. Covert fingerprinting is prohibited. Experiment views use governed exposure/outcome facts; Analytics supplies measurement evidence, while Experimentation retains assignment/decision authority.

Financial measures are explicit and not collapsed into one ambiguous `Revenue`: distinguish approved concepts such as gross sales, due, collected cash, discounts, refunds, fees, settlements/net proceeds and formally recognised accounting revenue where accounting policy exists. Verified payment is not automatically recognised accounting revenue.

Material release/pilot/experiment/management reports may preserve metric, time-window, timezone and filter context. Approved reports may be durably scheduled and delivered through secure in-app access or governed artifacts; unrestricted public links and uncontrolled sensitive attachments are not acceptable. A concise executive/owner overview drills into specialist canonical dashboards rather than becoming one giant metric screen.

Essential summaries are mobile-safe; dense analytical exploration may remain desktop-first. Chart.js remains a preferred JIT charting candidate, not a frozen package choice. Any chart must have responsive, bounded LiveView/JS integration and accessible textual/tabular alternatives.

---

# 12. SEO, search and public publishing

SEO is first-class public-page correctness from the first relevant slice. Applicable public contracts evaluate:

- semantic HTML and crawl/indexability;
- clean, stable human-readable canonical URLs not coupled unnecessarily to internal identifiers;
- title/meta description and content-aware Open Graph/social metadata with governed fallbacks;
- `robots.txt`, XML sitemap participation and safe noindex for private/system pages;
- breadcrumbs and legitimate BreadcrumbList/schema output;
- legitimate content-type structured data such as Article, Recipe, Event or FAQ where applicable;
- governed redirects without loops, excessive chains or silent historical-route destruction;
- language/locale metadata and alternate-language relationships;
- internal links;
- responsive images and public-page performance.

Exact schema fields remain JIT by page/content type. SEO is a frontend/publishing requirement, not an SEO Domain, Feature Pack or hidden authority.

Native public search is evidence-timed. When content volume/usefulness justifies it, start with deterministic relevance over approved public fields, taxonomy, recency, bounded performance signals and editorial rules. Semantic/vector/AI ranking requires evidence and may not override safety, relevance, quality or editorial governance. Search configuration remains JIT.

---

# 13. Consent, integrations, embeds and frontend observability

Consent/tracking UX is clear, minimal and non-manipulative. Necessary functionality uses its applicable lawful basis; optional analytics/marketing categories follow Privacy & Consent law. Applicable choices remain discoverable and changeable later. First-party does not mean privacy-exempt.

Where Cloudflare is used, Zaraz is the preferred integration boundary for supported analytics/marketing tools such as GA4. Prefer NewYou first-party event contracts and native supported integrations. Use GTM only for a concrete residual need that Zaraz does not satisfy cleanly; do not hardcode optional scripts across templates. Provider configuration remains JIT and must be revalidated when used.

Third-party analytics, marketing, Search Console and provider dashboards are complementary evidence. They never replace NewYou payment, entitlement, safety, eligibility, content, participant or accounting truth. Their failure must not break core use.

Approved third-party embeds use governed wrappers controlling consent, responsiveness, loading/performance, provider allow-lists and degraded behaviour. Ordinary content cannot inject arbitrary scripts/styles/embeds. Participant/community rich content uses strict allow-listed sanitisation.

Privacy-safe frontend observability may collect release/version correlation, technical context, actionable browser/LiveView errors and proportionate perceived-performance/web-vital-style signals. It must not indiscriminately capture credentials, health responses, sensitive form values or private content. An opaque user-visible correlation reference may be shown when it helps Support connect a failure to evidence.

---

# 14. JIT frontend performance pass

Every later implementation slice applies:

```text
BUILD CORRECTLY
→ VERIFY CORRECTNESS
→ COMPLETE THE SLICE
→ HIGH-LEVERAGE PERFORMANCE PASS
→ ACCEPTANCE
→ STOP
```

Review the affected path for:

- N+1/repeated queries and missing critical indexes;
- oversized LiveView assigns/diffs and avoidable rerenders;
- unbounded collections, payloads and histories;
- expensive synchronous work that should be durable async;
- obvious batching/preloading opportunities;
- oversized JS/assets/images and unnecessary third-party scripts;
- unnecessary provider calls;
- cache opportunities only where justified by authority, invalidation and evidence.

Prefer small, high-return fixes. Escalate material risk to the affected Feature Pack, Architectural Proof, Horizontal Hardening or Release Gate. Do not introduce speculative caches or infrastructure. Frozen Architecture remains Postgres-first; Redis, ETS/Cachex, GenServer, replicas and service extraction are evidence-gated and never frontend authority.

---

# 15. Deferred detail and freeze boundary

The following remain deliberately deferred:

- exact palette, font families, typography/spacing/radius numeric values;
- exact component pixel measurements and complete component inventory;
- exact route map, folder paths, Phoenix component/module names and CSS filenames;
- exact Tailwind config, hooks and browser-storage design;
- final chart package/version and integration details;
- exact Cloudflare/Zaraz/GA4/GTM/Search Console configuration;
- exact schema fields, search configuration and dashboard/KPI catalogue;
- full offline/PWA requirement;
- provider-specific payment, analytics, video, notification and embed semantics.

No implementation, FP-001, JIT Domain/Resource dossier, TOON prompt, Phoenix/LiveView/Ash build or component-library build is authorised by this document. Any future change to this authority requires a separate governance decision.

---

# 16. Freeze-review checklist

This frozen synthesis was compared against the cumulative Experience Decision Register. Future amendments must confirm that no `LOCKED` decision is deleted, weakened, silently reinterpreted or replaced by implementation convenience. At minimum verify:

- Command Centre, Library/Work Queue/Calendar, canonical dashboards/saved views and next-authorised-action Home;
- workflow-first operator Work with assignment/history, changes-requested, safe bulk actions, scoped support and no universal Task authority;
- content-first public discovery, persistent account access, bilingual switching, minimal/progressive onboarding, safe payment ambiguity and compassionate progress;
- governed content types/blocks/templates, translation and specialist approval separation, exact preview, responsive scheduling/correction/withdrawal and Media Library;
- token-first CSS-variable architecture, semantic Tailwind boundary, ACSS research boundary, fluid/layout math and deferred palette/fonts;
- explicit frontend form/async/dashboard presentation states without inventing business state machines;
- full fluid responsiveness, accessible forms/charts/focus, progressive enhancement, evergreen matrix and evidence-gated offline/PWA;
- SEO-first public publishing, first-party analytics boundaries, Zaraz preference, provider-outage isolation and privacy-safe telemetry;
- `DELIV-PERF-001` sequence and Postgres-first evidence-gated performance doctrine.

Any genuine contradiction with upstream frozen law or a `LOCKED` Experience decision is a STOP condition. Do not modify the Experience Register to make this synthesis pass.

---

# 17. STOP conditions

STOP and report the smallest exact blocker if:

- the canonical provenance source is missing or ambiguous;
- a `LOCKED` Experience decision conflicts with Product, Architecture, Domain, Roadmap or the frozen Operating Model;
- hardening would require changing the frozen Operating Model;
- exact palette/font choices become necessary;
- unresolved clinical, legal, accounting, professional or provider rules are required;
- the work expands into FP-001, JIT dossiers, TOONs or implementation;
- the only way to proceed is to invent implementation detail.

This artifact is frozen current authority for frontend-experience, design-system and interaction planning when those concerns are in scope. It is not default context for unrelated routine tasks, and it does not authorise implementation.
