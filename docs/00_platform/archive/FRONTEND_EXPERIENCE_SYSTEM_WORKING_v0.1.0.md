# FRONTEND_EXPERIENCE_SYSTEM_WORKING_v0.1.0.md

- **Status:** WORKING / DERIVED FRONTEND-EXPERIENCE CANDIDATE
- **Version:** v0.1.0
- **Derived from:** `EXPERIENCE_DECISIONS_WORKING_v0.7.0.md`
- **Date:** 2026-08-24
- **Implementation:** NOT AUTHORISED BY THIS DOCUMENT
- **Authority boundary:** Product, Architecture, Domain and Roadmap authority remain upstream. Exact brand colours and font families remain explicitly deferred.

# 1. Experience objective

NewYou combines:

- warm, refined editorial wellness;
- modern disciplined product interaction;
- journey-first participant UX;
- efficient role-aware operator UX;
- first-class accessibility, responsiveness, SEO and performance.

# 2. Experience principles

1. Content-first public experience.
2. Persistent but non-aggressive `Create account` and `Log in`.
3. Participant Home answers “what should I do next?”
4. Staff Home answers “what needs my attention?”
5. UI never fabricates authoritative business success.
6. Progressive enhancement: semantic HTML + LiveView baseline, CSS/JS enhancement.
7. Accessibility is baseline correctness.
8. Afrikaans/English resilience begins at component level.
9. Full fluid responsiveness across the width continuum.
10. Token-first design authority.
11. Purpose-built dashboards, not dashboard-builder complexity.
12. SEO correctness from the first public slice.
13. First-party analytics capture should be useful but purpose/privacy bounded.

# 3. Information architecture

## Public

- Home
- content/discovery
- relevant product/programme/event pages
- search when justified
- persistent language switcher
- persistent account/login access

## Participant

- Home / Today
- My Journey
- Explore
- Programmes
- Community
- Events / Live
- My Access
- Account

Only relevant/current capabilities appear.

## Operator

- Command Centre
- Work
- People
- Content
- Health & Plans
- Programmes
- Commerce
- Community & Events
- Communications
- Experiments
- Analytics
- Platform

Navigation does not define Domain ownership.

# 4. Token-first design architecture

Design authority:

`foundation tokens → semantic tokens → component tokens where genuinely needed → product theme → components/patterns`

Native CSS custom properties are the runtime token substrate.

Examples:

- `--primary`
- `--surface`
- `--text-primary`
- `--space-m`
- `--section-space-m`
- `--radius-m`
- `--text-m`
- `--content-width`
- `--gutter`

Exact colour/font values are deferred.

# 5. Automatic.css study model

Automatic.css is a deliberate research reference for:

- variable-first styling;
- mathematical spacing/type scales;
- section spacing;
- global gutters/content widths;
- `calc()`/`clamp()` relationships;
- recipes/functions;
- semantic colours;
- contextual spacing;
- grid/layout approaches;
- accessibility defaults.

Study lawful/public or user-provided licensed source material.

Do not copy proprietary source or depend on WordPress/ACSS at runtime.

# 6. Tailwind integration

Tailwind v4 is implementation/build syntax, not design authority.

Do not add Sass/SCSS merely to imitate ACSS.

Preferred flow:

`NewYou CSS variables/tokens ↔ Tailwind @theme/utilities ↔ semantic components/patterns`

Avoid raw arbitrary values scattered through HEEx.

# 7. Markup cleanliness

Preferred hierarchy:

`Phoenix component/pattern → concise semantic class/API → token-driven CSS → small local utility usage where useful`

The goal is not the shortest class attribute; it is the least duplicated styling knowledge.

# 8. Theme architecture

`core/foundation → semantic experience tokens → NewYou women's theme`

Future product themes override semantic values without rewriting reusable core components.

# 9. Responsive system

Use modern responsive CSS as a system property:

- CSS Grid;
- Flexbox;
- `minmax()`;
- `repeat()`;
- `auto-fit` / `auto-fill`;
- `clamp()`;
- `calc()`;
- container queries;
- media queries;
- intrinsic sizing;
- logical properties;
- responsive media;
- subgrid where justified.

Breakpoints are composition thresholds, not device labels.

Container queries are preferred when a reusable component responds to its allocated width.

# 10. Responsive preview

Official preview pattern supports:

- draggable continuous width;
- visible current width;
- preset review widths;
- fullscreen;
- locale/language;
- applicable product theme.

Presets are shortcuts, not the responsiveness contract.

# 11. Typography and spacing

Exact fonts and final numeric scales remain deferred.

Use:

- governed fluid typography where appropriate;
- tokenised readable prose measure;
- compact t-shirt-style spacing scale;
- dedicated section-space/gutter tokens;
- token-derived `calc()` adjustments rather than magic numbers.

# 12. Forms — floating-label system

Default appropriate field pattern:

- empty/idle: real label appears inside the field area;
- focus/value/autofill: label floats upward and remains visible.

It must be a genuine associated label, never placeholder-only.

Support:

- keyboard;
- screen readers;
- autofill/password managers;
- populated values;
- validation;
- disabled/read-only;
- long Afrikaans/English labels;
- required/optional semantics;
- touch targets.

Hint/error text may appear beneath the control.

Controls where floating labels reduce usability may use an approved alternate pattern.

# 13. Form interaction state machine

## States

- `EMPTY_IDLE`
- `EMPTY_FOCUSED`
- `FILLED_IDLE`
- `FILLED_FOCUSED`
- `VALIDATING`
- `INVALID`
- `DISABLED`
- `READ_ONLY`

## Transitions

| From | Trigger | To | Guard | Side effect |
|---|---|---|---|---|
| EMPTY_IDLE | focus/tab | EMPTY_FOCUSED | control enabled | label floats, focus visible |
| EMPTY_FOCUSED | input/autofill | FILLED_FOCUSED | value accepted | label remains floated |
| FILLED_FOCUSED | blur | FILLED_IDLE | none | value remains visible |
| EMPTY_FOCUSED | blur | EMPTY_IDLE | no value/error forcing float | label returns inside |
| editable | validate fail | INVALID | validation executed | error associated/rendered |
| any allowed | disable | DISABLED | controlling state permits | interaction blocked |
| any allowed | read-only | READ_ONLY | controlling state permits | mutation blocked |

## Terminal states

None intrinsically. Form-field state is interaction state and remains revisitable while the parent workflow is active.

# 14. Async action UI state machine

## States

- `IDLE`
- `SUBMITTING`
- `PENDING_EXTERNAL` where applicable
- `SUCCESS`
- `VALIDATION_ERROR`
- `CONFLICT`
- `REQUIRES_ATTENTION`

## Transitions

| From | Trigger | To | Guard | Side effect |
|---|---|---|---|---|
| IDLE | submit | SUBMITTING | local form/action valid enough to submit | controls enter scoped pending state |
| SUBMITTING | authoritative success | SUCCESS | Domain action succeeds | success UI/navigation |
| SUBMITTING | external unresolved | PENDING_EXTERNAL | operation safely persisted/reconcilable | explain pending state |
| SUBMITTING | validation fail | VALIDATION_ERROR | server/domain validation fails | preserve input, focus errors |
| SUBMITTING | conflict | CONFLICT | concurrency/idempotency conflict | show safe resolution |
| PENDING_EXTERNAL | resolved success | SUCCESS | authoritative transition completes | refresh/reconcile UI |
| PENDING_EXTERNAL | operator/user action required | REQUIRES_ATTENTION | safe automatic resolution unavailable | actionable explanation/reference |

## Guards

- clicking never implies success;
- payment/access/safety/privilege success waits for authoritative response;
- optimistic UI only for harmless divergence;
- recoverable failures preserve user work where safe.

# 15. Loading pattern

Prefer:

`instant local feedback → scoped pending → skeleton when structure known → spinner where appropriate`

Do not block the entire page for a small LiveView update.

# 16. Participant experience

Participant Home composes authoritative next actions.

Long journeys use:

- purposeful steps;
- honest section progress;
- durable save/resume;
- clear saved state;
- interruption recovery.

Unavailable capabilities are hidden unless a locked state is genuinely useful for discovery/commercial context.

# 17. Purchase/payment UX

- verified success only after authoritative confirmation;
- ambiguous result becomes explicit pending/verifying state;
- discourage duplicate payment;
- successful purchase leads to the next authorised journey action.

# 18. Health/safety UX

Health forms are calm, plain-language and safety-explicit.

Preserve distinctions such as:

- unknown;
- not tested;
- prefer not to answer;

where governing law permits.

Safety-blocked flows explain the permitted next outcome without exposing unnecessary internal rules.

# 19. Content/editorial frontend

Provide:

- Library;
- Work Queue;
- Editorial Calendar;
- structured content-type editor;
- extensible governed block/section/component catalogue;
- reusable templates;
- translation/review workflow;
- exact experience preview;
- responsive resizable preview;
- scheduling;
- correction/supersession/withdrawal;
- concise content analytics.

# 20. Content blocks/templates

A reusable block/component enters the catalogue only with:

- a real use case;
- meaningful reuse;
- understood states;
- accessibility behaviour;
- responsive behaviour.

Templates may precompose governed sections/slots/defaults.

Updating a template must not silently rewrite historical published content unless explicitly designed.

# 21. Dashboards

Provide purpose-built canonical dashboards only.

Expected families as scope matures:

- Executive / Business
- Sales & Commerce
- Content & Acquisition
- Product Funnel
- Participant Outcomes
- Operations & Exceptions
- Platform Health

No user-facing dashboard builder.

# 22. Dashboard query interaction state machine

## States

- `CURRENT`
- `REFRESHING`
- `CURRENT_UPDATED`
- `STALE`
- `PARTIAL`
- `DELAYED`
- `ERROR`
- `NO_DATA`
- `RESTRICTED`

## Transitions

| From | Trigger | To | Guard | Side effect |
|---|---|---|---|---|
| CURRENT | filter/date/comparison/refresh | REFRESHING | viewer authorised for requested dimensions | relevant region queries automatically |
| REFRESHING | successful data load | CURRENT_UPDATED | quality checks acceptable | chart/KPI/table rerender |
| REFRESHING | quality incomplete | PARTIAL/DELAYED | governed freshness contract | warning shown |
| REFRESHING | query/source failure | ERROR | none | retain context, explain failure |
| any current-like | freshness threshold exceeded | STALE | metric contract says stale | freshness warning |
| REFRESHING | zero observations | NO_DATA | semantically no observations | do not render numeric zero falsely |
| any | permission restriction | RESTRICTED | viewer lacks access | no sensitive leakage |

Filters/date/comparison/refresh apply automatically; browser reload is not required.

# 23. Charting

Chart.js is the preferred initial candidate, subject to JIT validation.

Requirements:

- responsive resizing;
- useful hover/click/touch interaction;
- bounded LiveView/JS Hook integration;
- accessible text/table alternatives;
- acceptable bundle/runtime cost.

Do not adopt a heavier charting system without need.

# 24. Analytics / content attribution

NewYou first-party event/business contracts should allow useful linkage among:

- public content;
- CTA/funnel interaction;
- permissioned email;
- account;
- product interest;
- verified purchase;
- assessment/programme outcomes.

Third-party analytics complements these facts.

Avoid covert device fingerprinting and indiscriminate event collection.

# 25. Cloudflare analytics integration

Preferred when Cloudflare is used:

`NewYou first-party event contracts → Cloudflare Zaraz → native supported tools such as GA4`

Use Zaraz consent/privacy controls where applicable.

Do not default to GTM-through-Zaraz. Current Cloudflare guidance permits it but recommends native Zaraz tools because GTM-contained tools cannot be optimised or restricted through Zaraz privacy controls.

GTM remains an explicitly justified fallback/integration option.

# 26. Consent UI

Consent UI is:

- clear;
- minimal;
- non-manipulative;
- persistent/manageable later;
- integrated with applicable optional analytics/marketing loading.

First-party does not automatically mean privacy-exempt.

# 27. SEO system

SEO is first-class from the start.

Relevant public page contracts include as applicable:

- semantic HTML;
- canonical URL;
- title/meta;
- Open Graph/social metadata;
- XML sitemap participation;
- `robots.txt` / indexability;
- breadcrumbs + `BreadcrumbList` schema;
- content-specific structured data such as Article/Recipe/Event/FAQ where legitimate;
- redirects;
- language metadata/alternates;
- internal linking;
- responsive images/performance;
- noindex handling for non-public/private/system pages.

SEO belongs in JIT acceptance for public slices.

# 28. Public search/discovery

Native search is approved when content scale justifies it.

Start deterministic.

Performance/revenue signals may later be bounded ranking inputs but never completely override relevance, safety, quality or editorial governance.

# 29. Third-party embeds

Use approved provider wrappers controlling:

- consent/privacy;
- responsiveness;
- loading/performance;
- failure state;
- provider allow-list.

No arbitrary embed HTML/scripts in ordinary content.

# 30. Degraded/offline behaviour

Non-authoritative third-party outages do not break core use.

Critical provider ambiguity uses explicit pending/degraded state.

Full offline/PWA capability is evidence-gated.

# 31. Browser support

Use a release-time tested evergreen-browser matrix.

Use modern CSS within that matrix and graceful fallback where genuinely required.

# 32. Accessibility

Baseline requirements include:

- semantic HTML;
- keyboard operation;
- visible focus;
- associated labels;
- error association;
- contrast;
- no colour-only meaning;
- reduced motion;
- zoom/reflow;
- touch targets;
- accessible chart alternatives;
- LiveView focus handling.

Use automated checks plus meaningful human verification.

# 33. Visual regression

Use selectively for:

- stable reusable components;
- critical flows;
- high-value responsive states.

Avoid blanket brittle pixel snapshots.

# 34. Media

Use governed responsive media and CDN/server derivatives.

Do not ship oversized originals when smaller derivatives are appropriate.

# 35. Print

Provide intentional print presentation for applicable plans, recipes, reports and content.

Remove irrelevant navigation/controls while preserving essential safety/version/source information where applicable.

# 36. Frontend observability

Capture privacy-safe:

- LiveView/browser errors;
- release/version correlation;
- useful frontend/perceived performance;
- opaque correlation IDs where support value is high.

Never indiscriminately capture credentials, health responses or private content.

# 37. JIT frontend performance pass

Every slice reviews high-leverage issues such as:

- N+1/repeated queries;
- oversized LiveView assigns/diffs;
- unnecessary rerenders;
- unbounded collections;
- oversized JS/assets/images;
- expensive synchronous work;
- unnecessary third-party scripts;
- obvious preload/index opportunities.

Fix cheap high-value issues.

Escalate material performance problems rather than over-engineering speculative optimisation.

# 38. Component admission and state contracts

Reusable components must have:

- real need;
- meaningful reuse;
- responsive behaviour;
- accessibility behaviour;
- applicable interaction states.

Do not build a speculative design-system inventory.

# 39. Exact values still deferred

Do not freeze in this document:

- exact brand palette;
- exact font families;
- every component pixel measurement;
- final chart package version;
- final Cloudflare/GA provider configuration;
- exact dashboard metric sets outside JIT scope.

# 40. STOP conditions

STOP if frontend work would:

- bypass Product/Domain authority;
- fabricate critical authoritative state;
- weaken privacy/consent/accessibility;
- reintroduce raw magic-value styling outside the token rules;
- introduce a dashboard builder without a new approved need;
- make third-party analytics authoritative;
- require exact colour/font decisions before the visual-brand round;
- contradict the cumulative Experience Decision Register.
