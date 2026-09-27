# 05_ROADMAP_v1.1.3.md

- **Document status:** FROZEN / AMENDED ROADMAP
- **Document version:** v1.1.3
- **Predecessor frozen version:** `archive/05_ROADMAP_v1.1.2.md`
- **SemVer transition:** `v1.1.2 → v1.1.3`
- **Last updated:** 2026-09-26
- **Authority:** sequences approved Product Law under frozen Architecture and Domain Law, including the Targeted Product Amendment sequencing decisions
- **Current Product authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`, `00_PLATFORM_v1.5.0.md`, `01_DECISIONS_v1.5.0.md`
- **Current Architecture authority:** `03_ARCHITECTURE_v1.1.1.md` and accepted Architecture Law (`reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` where exact legislative evidence is required)
- **Current Domain authority:** `04_DOMAIN_MAP_v1.2.0.md`
- **Current programme routing:** `README.md` and the current Open Work path it identifies (`02_OPEN_WORK_v1.2.47.md`)
- **Roadmap-freeze provenance (v1.1.2 source-at-freeze):** `archive/00_PLATFORM_v1.4.1.md`, `archive/01_DECISIONS_v1.4.1.md`, `archive/04_DOMAIN_MAP_v1.1.1.md`, `archive/02_OPEN_WORK_v1.2.45.md`
- **Roadmap Sequencing Grill evidence:** `working/TARGETED_ROADMAP_SEQUENCING_GRILL_WORKING_v0.1.0.md` (non-authoritative)
- **Historical working draft:** `archive/05_ROADMAP_WORKING_v0.1.0.md`
- **Historical frozen predecessor:** `archive/05_ROADMAP_v1.0.0.md`
- **Implementation status:** STOPPED; this document does not authorise Feature Pack preparation, JIT Domain Dossiers, Architectural Proof, Vertical Slices, TOON generation or implementation

## Amendment summary (v1.1.0)

Additive Roadmap amendment after Domain Law `v1.1.0`. Feature Pack identifiers `FP-001`–`FP-017` and the core dependency ladder are preserved. This successor:

1. records Platform Member Reference as **REQUIRED** inside the FP-001 Account outcome (encoding remains unfrozen; `FP001_RECONCILIATION_REQUIRED` remains downstream);
2. records Research & Feedback and Voting & Balloting as mature **FUTURE-GATED / FEATURE-PACK-UNASSIGNED** capabilities (not MVP; no new Feature Packs);
3. records Interactive Tools as purpose-distributed delivery mechanisms, not a Feature Pack family;
4. refreshes current-authority references to Product `v1.3.0`, Architecture `v1.1.0` and Domain Map `v1.1.0`.

No Research, Voting, PMR, Interactive Tools or Competitions Feature Pack is created. Executable development remains blocked.

## v1.1.1 Patch Scope

This patch synchronises current Product and Open Work references, removes resolved OQ-034 architecture selection as an FP-001 Roadmap blocker, and records its still-incomplete executable proof as a Phase 8 obligation. It preserves all 17 Feature Packs, does not perform FP-001 PMR reconciliation, does not finalise proof classification and does not authorise Phase 8 or implementation.

## v1.1.2 Patch Scope

This routing/status-only successor updates current Product authority and Open Work paths and corrects the §21 handoff to the already-established programme route. It preserves the outcome sequence, all 17 Feature Packs, gate classifications, capabilities and dependencies. It does not select or advance the active task, perform FP-001 reconciliation, finalise proof classification or authorise implementation.

## v1.1.3 Patch Scope

This routing/provenance-only successor separates current authority from Roadmap-freeze provenance, corrects the FP-006 source-at-freeze tracker label and defers current task/stage selection to README and current Open Work. It preserves Roadmap semantics, all 17 Feature Pack definitions, sequence, affected Domains, gates, dependencies, proof directions, critical path, future-gated Research/Voting treatment and Interactive Tools doctrine. It does not advance any task or stage.

---

# 1. Authority, purpose and boundaries

This Roadmap answers **what outcome is sequenced when, why it is positioned there, what it proves, what it unlocks, and which gates must be resolved**. It does not amend Product Law, Architecture Law or Domain Law.

The governing order is:

```text
Product Law
→ Architecture Law / 03_ARCHITECTURE
→ Domain Law / 04_DOMAIN_MAP
→ 05_ROADMAP
→ Phase 7 Feature Pack preparation + JIT Domain Dossiers
```

The Roadmap may sequence approved capability, cluster approved work into outcome-oriented delivery containers and defer approved branches. It may not:

- invent clinical, legal, commercial, payment-provider, retention or professional-record rules;
- assign or change Domain ownership;
- choose implementation-grade Resources, schemas, indexes, Redis structures, TTLs, workers, topics, packages or UI structure;
- turn a future gate into an MVP prerequisite without evidence that the protected behaviour needs it;
- create a Feature Pack for a Domain, page, form or technical layer merely because it exists;
- authorise executable development.

The current authority read found no material upstream contradiction affecting delivery order. Remaining unknowns are scheduled as gates at the earliest point where they are required to prevent downstream guessing.

Current Product, Decision, Architecture and Domain authority is identified in the versioned authority fields above and routed by README. The Roadmap-freeze provenance field records the sources used when v1.1.2 was frozen. Older version citations retained in Feature Pack sections, including Product `v1.4.1`, are source-at-freeze evidence for those frozen definitions; they do not claim current authority and are not replaced merely because newer authority exists. This v1.1.3 clarification does not re-derive any Feature Pack.

## 1.1 Planning vocabulary

`BLOCKS_THIS_FP` means the Feature Pack cannot reach its stated outcome while the gate is unresolved.

`BLOCKS_RELEASE_ONLY` means the capability can be shaped, tested with safe/internal boundaries or prepared, but the named release stage cannot proceed until the gate is resolved.

`NON_BLOCKING_FOR_THIS_FP` means the gate is relevant to a neighbouring or optional capability but is not needed for this Feature Pack's stated outcome.

`FUTURE_ONLY` means the gate belongs to a later approved branch and must not be pulled into this Feature Pack merely for completeness.

Anticipated proof labels are deliberately provisional. Phase 7 Final Feature Pack Contracts own the final `REUSE_EXISTING_PROOF` / `NEW_TRACER_BULLET` decision.

---

# 2. Ultimate mature-platform outcome

At maturity, NewYou is one coherent Christian, temperament-guided women’s health and lifestyle ecosystem. A participant can move from bilingual public discovery through temperament understanding, safe health routing, practical plans, sustainable behaviour, community and live participation, professional escalation and long-term maintenance. The platform also supports the surrounding operating ecosystem: purchasers and recipients, content and clinical authorities, moderators, support/finance/event staff, practitioners, facilitators, analysts and accountable release operators.

The mature participant/business ladder is:

```text
public visitor
→ free account / mailing-list contact
→ assessment customer
→ once-off plan customer
→ basic member
→ programme / Nuwe Jy participant
→ adjustment customer or Premium member
→ practitioner-reviewed customer where appropriate
→ community, live and event participant
→ repeat participant with long-term progress and maintenance
```

The mature platform must preserve:

| Mature capability family | Approved outcome represented in this Roadmap |
|---|---|
| Public and acquisition | Bilingual discovery, governed public content, product information, measurable acquisition and later governed experimentation. |
| Identity, privacy and trust | One canonical identity, verified access, Platform Member Reference as the required human-facing Account reference (not login, authentication, authorisation, verification, Membership, subscription, entitlement or voucher truth), scoped roles, consent, deletion/export, audit and operational recovery. |
| Temperament and assessment | Versioned, provenance-aware assessment and immutable report history reused across approved product families. |
| Health, safety and plans | Progressive health facts, deterministic eligibility, General Wellness fallback, explainable versioned plans and safe adjustment. Purpose-specific Interactive Tool/calculator results remain with the owning Domain; calculation is not authority. |
| Content and behaviour change | Approved bilingual content, programmes, habits, journals, progress, recovery and compassionate completion. Editorial Interactive Tool presentation may live with Content where that meaning applies; lasting self-tracking tool results belong with Habits only when that meaning fits. |
| Commerce and access | Assessments, plans, bundles, memberships, add-ons, gifts/sponsorships, refunds and one explicit entitlement system. |
| Community, live and events | Governed external validation, first-party community, live/replay access and later scarce-capacity event commerce. |
| Professional care | A limited, capacity-controlled practitioner service with consented scoped access and clear referral boundaries. |
| Research & Feedback | Bounded lightweight Research/Feedback and governed Research campaigns owned by Domain 19. Mature approved capability; **FUTURE-GATED / FEATURE-PACK-UNASSIGNED**. Not MVP. Not interpreted from FP-005 basic progress/feedback. Not automatically assigned to FP-006, FP-008 or FP-009. |
| Voting & Balloting | Governed voting/balloting with official-result capability owned by Domain 20. Mature approved capability; **FUTURE-GATED / FEATURE-PACK-UNASSIGNED**. Not MVP. Not required by FP-008 Nuwe Jy or FP-013 Community + Challenges. Research polls remain Research by purpose. |
| Learning and operations | Analytics, first-party experimentation, support, notifications, incident evidence, performance evidence and release control. |
| Controlled expansion | Future approved product spaces/markets reuse the shared platform without exposing unfinished products or creating generic tenancy by default. FP-017 does not automatically own Research or Voting merely because they are future-gated. |
| Interactive Tools doctrine | Interactive tools/calculators/decision aids are purpose-distributed delivery mechanisms, not an independent Feature Pack family; consequential authority stays with the owning Domain. No Tools Feature Pack and no generic Tools activation point. |

The mature outcome is not a generic LMS, calorie tracker, social network, practitioner marketplace, event-ticketing system or unrestricted multi-tenant SaaS product. Those capabilities are only admitted where an approved NewYou outcome requires them and where the relevant law and evidence exist.

---

# 3. Backward dependency model

## 3.1 Work backward from the mature ecosystem

The mature platform requires five dependency bands:

1. **Trust and authority:** identity, privacy/consent, scoped access, audit, current-policy checks, safe operational control and recoverability.
2. **Core paid value:** bilingual discovery, verified account, purchase truth, entitlement truth, temperament provenance/report, health/safety routing, deterministic plan delivery, purchased library access and lightweight feedback.
3. **Engagement and recurring value:** content publication, durable communications, live/replay, programmes, cohort delivery, community, membership and plan adjustment.
4. **Professional and scarce participation:** practitioner review, first-party moderation/challenges and event capacity/ticket truth.
5. **Evidence-led expansion:** experimentation, deeper behaviour-change capability and approved future product spaces/markets.

The shortest safe commercial route is therefore a narrow path through bands 1 and 2, followed by a dedicated operational evidence gate. It does not require first-party community, Nuwe Jy, memberships, Premium, practitioners, event commerce or experimentation to be pulled into MVP.

## 3.2 Dependency graph

```text
Frozen Product / Architecture / Domain Law
                    │
                    ▼
FP-001 Trusted bilingual entry and verified identity
                    │
                    ▼
FP-002 Purchase → verified payment → entitlement
                    │
                    ▼
FP-003 Temperament provenance, assessment and report
                    │
                    ▼
FP-004 Health intake → safety → eligibility
                    │
                    ▼
FP-005 Safe plan → purchased library → feedback
                    │
                    ▼
FP-006 Controlled operations → internal / paid pilot release
              ┌─────┼───────────────┬───────────────┬──────────────┐
              │     │               │               │              │
              ▼     ▼               ▼               ▼              ▼
           FP-007 FP-010         FP-012          FP-016        FP-017
           Live    Adjustment     Practitioner    Experiments   Approved
           /replay                  pilot                       space/market
              │       │
              ├──► FP-008 Nuwe Jy flagship edition
              │
              └──► FP-009 Basic Membership

FP-008 / FP-009 evidence ──► FP-013 First-party community + challenges
FP-008 programme proof ─────► FP-014 Foundation programme + habits/journals
FP-007 + FP-002 + FP-006 ────► FP-015 Event commerce + scarce capacity
FP-010 + FP-009 ─────────────► FP-011 Premium bundle
```

The graph has no circular authoritative dependency. A later branch may read current entitlement, safety, content or plan authority, but it does not become a prerequisite for the earlier core journey merely because it shares infrastructure.

## 3.3 Dependency challenges and decisions

| Assumption challenged | Roadmap decision |
|---|---|
| Every Domain needs its own early Feature Pack | Rejected. Domains are reused inside outcome packs; no Domain-only pack exists. |
| Assessment, safety and plan delivery can be one undifferentiated MVP pack | Rejected. Their validation and blocking expert gates are materially different, so FP-003, FP-004 and FP-005 remain separate while the critical path stays short. |
| Practitioner review is needed before automated plans | Rejected by Product Law. MVP may route cases to `professional_review_required` without selling or implementing an open practitioner service. |
| Basic Membership must precede Nuwe Jy | Rejected. FP-008 and FP-009 are sibling branches after shared live/operational readiness; Product Law permits Nuwe Jy before or alongside early membership. |
| Full event commerce is needed to run live sessions | Rejected. FP-007 proves governed live/replay access; FP-015 owns later scarce capacity and ticket commerce. |
| First-party community is an MVP prerequisite | Rejected. Facebook is the governed early validation channel; FP-013 waits for evidence. |
| Experimentation is needed to measure the first pilot | Rejected. FP-006 carries minimum governed product/operational measurement; FP-016 is later and evidence-led. |
| Generic programme/LMS infrastructure should precede Nuwe Jy | Rejected. FP-008 is the concrete first flagship acceptance test; FP-014 follows only when broader programme capability is justified. |
| New Domains 19/20 require new Feature Packs | Rejected. A Domain is not a Feature Pack. Research & Feedback and Voting & Balloting remain mature FUTURE-GATED / FEATURE-PACK-UNASSIGNED until a later governed Roadmap decision assigns an activating outcome. |
| Interactive Tools require a cross-cutting Feature Pack | Rejected. Tools are sequenced only inside the Feature Pack whose approved outcome requires them; calculation is not authority. |
| Public Nuwe Jy-style voting must enter with FP-008 | Rejected. Product Law admits the mode; Roadmap does not require Voting & Balloting for Nuwe Jy activation. |
| Redis, replicas, GenServers, specialist search or microservices should be built up front | Rejected. Frozen Architecture requires the simplest correct PostgreSQL/Oban/application path first, with acceleration and topology changes evidence-gated. |

---

# 3A. Future-gated mature capabilities (Feature-Pack-unassigned)

Some Product-approved mature capabilities are deliberately not assigned to any of `FP-001`–`FP-017` yet. They are **not rejected**. They remain available for a later governed Roadmap decision when a concrete Product outcome requires them.

Activation requires a later governed Roadmap amendment that names the activating Feature Pack (existing or new) and the bounded mode required. No Feature Pack may silently absorb these capabilities merely because a page, poll widget, challenge, pilot survey or tool surface could use them.

| Capability | Domain / ownership | Status | Explicit non-assignments |
|---|---|---|---|
| Research & Feedback | Domain 19 — Research & Feedback | `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` | Not MVP; not FP-005; not automatically FP-006, FP-008 or FP-009; no Research Feature Pack created now |
| Voting & Balloting | Domain 20 — Voting & Balloting | `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` | Not MVP; not required by FP-008; not required by FP-013; no Voting or Competitions Feature Pack created now |

Interactive Tools are not listed as a future-gated Feature Pack candidate: they have no Domain and no independent Roadmap delivery container. When a Feature Pack outcome requires a tool/calculator/decision aid, that pack sequences the tool under the owning Domain's authority.

These rows do **not** create present OQ blockers for FP-001–FP-017. Future public Voting may later require abuse/integrity evidence, and sensitive Research may later require stronger privacy/safety review, but those gates are scheduled only when an activating Feature Pack is assigned.

---

# 4. Delivery principles

1. **Outcome before layer.** A Feature Pack makes a participant, operator or platform capability observable; it is not a table, Domain, screen or provider adapter.
2. **Mature outcome backward, commercial route forward.** Future dependencies are protected without allowing them to contaminate the first paid slice.
3. **Authority before projection.** Commerce, entitlement, safety, plan, content, professional and event truths stay with their Domain owners.
4. **Safety before personalisation.** Temperament changes presentation and behavioural delivery; it never overrides clinical/safety authority.
5. **Payment truth before access truth.** Verified provider evidence reconciles into Commerce, then a durable idempotent consequence grants Entitlements.
6. **Prove the smallest enduring path.** Reuse existing architecture pressure-test evidence where the mechanism is the same; create a new tracer bullet only for a materially new path.
7. **Resolve gates just in time.** An unresolved future gate is not a present blocker unless the current outcome relies on it.
8. **Operational capability is part of the product.** Support, correction, withdrawal, incident handling, audit, recovery and release controls cannot be deferred past the behaviour they protect.
9. **Scale by evidence.** Bounded queries, PostgreSQL correctness, durable async work and safe degradation precede Redis, replicas, cache complexity or service extraction.
10. **One shared capability, many products.** Later products reuse Commerce, Entitlements, Safety, Plans, Content, Communications, Community and Analytics rather than creating parallel stacks.

---

# 5. Delivery phases

The phases describe outcomes and readiness, not code layers. Packs within a phase may be sequential or parallel only where the dependency graph says so.

## Phase 1 — Trusted entry and commercial truth

**Objective:** establish the bilingual public-to-account boundary and the first lawful path from an approved offer to verified payment and exactly one valid entitlement.

**Feature Packs:** `FP-001 → FP-002`.

**What becomes possible:** a person can discover the launch-facing women’s product, create a verified individual account, purchase an approved assessment/plan/bundle offer and receive current access only after authoritative payment reconciliation.

**Major dependencies:** frozen Product/Architecture/Domain Law; no future product capability.

**Major gates:** `OQ-004`, `OQ-035`; production-release implications of `OQ-001`, `OQ-036` and the paid-pilot readiness set.

**Authentication proof:** `OQ-034` architecture selection is resolved; its executable proof remains a Phase 8 obligation.

**Completion/readiness condition:** identity/session and payment/entitlement paths are independently reconcilable, idempotent, scoped and supportable; no paid health journey is released yet.

## Phase 2 — Core participant value loop

**Objective:** turn the commercial access path into the smallest safe paid proposition: assessment/report, health/safety outcome, plan or General Wellness fallback, purchased library and basic feedback.

**Feature Packs:** `FP-003 → FP-004 → FP-005`.

**What becomes possible:** an eligible participant can complete the approved core journey and receive an immutable, explainable, bilingual result and safe seven-day plan; a non-eligible participant receives the governed alternative outcome and no unsafe plan.

**Major dependencies:** Phase 1; approved assessment, clinical, calculation, translation and content versions.

**Major gates:** `OQ-005`, `OQ-008`, `OQ-010`, `OQ-013`, plus release-only privacy/content gates `OQ-009`, `OQ-016` and `OQ-029`.

**Completion/readiness condition:** no incomplete or duplicate assessment result, entitlement, eligibility decision or plan can be delivered; all safety-critical and paid bilingual content is approved.

## Phase 3 — Controlled paid evidence and pilot progression

**Objective:** make the core loop operable by named staff and safe to expose progressively to paid participants.

**Feature Pack:** `FP-006`.

**What becomes possible:** internal validation, then the Product-Law rollout of first real participants, review, expansion toward 25, maximum 50 in the first pilot, limited public release and later general public release decisions.

**Major dependencies:** all Phase 1–2 packs; cross-functional product, clinical, content, commerce, legal/privacy, security and operations ownership.

**Major gates:** `OQ-001`, `OQ-009`, `OQ-029...OQ-032`, `OQ-035...OQ-038`, plus every applicable Product Law paid-pilot sign-off.

**Completion/readiness condition:** release/rollback authority, support/incident ownership, restore/deletion tests, integrity telemetry and pilot evidence are operational; expansion is evidence-gated rather than capacity-assumed.

## Phase 4 — First recurring and flagship pathways

**Objective:** add governed live value, the first native Nuwe Jy edition, recurring Basic value, recurring plan adjustment and then Premium only after the underlying capabilities work.

**Feature Packs:** `FP-007`, `FP-008`, `FP-009`, `FP-010`, `FP-011`.

**What becomes possible:** live/replay participation, a native 60-day Nuwe Jy cohort, a genuinely operational Basic Membership, governed recurring adjustment, and a Premium bundle composed from already-proven component entitlements.

**Major dependencies:** core paid pilot evidence; `FP-007` is shared by Nuwe Jy, membership and later events; `FP-010` depends on stable plan delivery and useful check-ins; `FP-011` depends on `FP-009` and `FP-010` where the approved Premium packaging uses the recurring membership contract.

**Major gates:** `OQ-003`, `OQ-004`, `OQ-011`, `OQ-012`, `OQ-017`, `OQ-019...OQ-027`, `OQ-036` and the relevant operating/legal gates.

**Completion/readiness condition:** each branch passes its own product, safety, operational, provider and capacity gate; no branch is released merely because shared technical capability exists.

## Phase 5 — Professional care and evidence-led community/behaviour change

**Objective:** introduce scarce professional capacity and first-party participation only after the core and external/community/flagship evidence justify them.

**Feature Packs:** `FP-012`, `FP-013`, `FP-014`.

**What becomes possible:** a controlled practitioner-review pilot, a first-party moderated community with safe challenges, and broader foundation-programme/habit/journal/progress experiences.

**Major dependencies:** `FP-006`; `FP-012` reuses the automated safety/plan path; `FP-013` depends on evidence from governed Nuwe Jy/Membership community use; `FP-014` uses Nuwe Jy as the concrete programme acceptance path before broader generalisation.

**Major gates:** `OQ-009`, `OQ-017...OQ-019`, `OQ-023`, `OQ-033`, practitioner agreements, moderation staffing and journal/privacy review.

**Completion/readiness condition:** professional capacity and record authority are explicit; moderation, consent, deletion and journal boundaries are proven; no open practitioner marketplace or generic social network is implied.

## Phase 6 — Scarce commerce, experimentation and approved future expansion

**Objective:** add event commerce and first-party experimentation when their evidence boundaries are real, then activate a concrete approved product space or market without inventing generic tenancy.

**Feature Packs:** `FP-015`, `FP-016`, `FP-017`.

**What becomes possible:** paid events with zero confirmed oversell, governed A/B/n learning, and a deliberately approved future product-space/market activation using shared platform truth.

**Major dependencies:** `FP-002`, `FP-006`, `FP-007` for events; stable measurable product surfaces for experimentation; a concrete approved product/market direction for `FP-017`.

**Major gates:** `OQ-004`, `OQ-014`, `OQ-022`, `OQ-030`, `OQ-032`, `OQ-035`, `OQ-036`, `OQ-040` and new market/product expert approvals.

**Completion/readiness condition:** each high-concurrency or variant-sensitive path has its required Phase 7/8/10/11 evidence; future product activation is explicit and does not expose unfinished spaces.

---

# 6. Feature Pack register

The following packs are stable Roadmap containers. Their names and boundaries are sufficient to select Phase 7 work without fixing implementation-grade semantics. Feature Pack count remains **17** (`FP-001`–`FP-017`). No Research, Voting, PMR, Interactive Tools or Competitions Feature Pack is created by the v1.1.0 amendment.

## FP-001 — Trusted bilingual entry and verified identity

**ID:** `FP-001`

**Name:** Trusted bilingual entry and verified identity

**Outcome:** A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, receive that Account's required human-facing Platform Member Reference (PMR), verify email, recover access and use a controlled support/admin path without exposing unfinished product spaces.

**Validation Objective:** Prove that public-to-verified-account entry is understandable, privacy/age/terms gates are respected, identity/session authority is reconstructible, a successful individual Account creation assigns exactly one canonical active PMR under Identity & Access ownership, and operators can resolve ordinary account-access issues.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `ARCHITECTURAL`, `SECURITY`, `PRIVACY`, `OPERATIONAL`.

**Why Now:** Every protected purchase, assessment, health, plan, support and deletion action requires one canonical identity and current server-side authority. The Platform Member Reference is required Account truth assigned at successful individual Account creation (`DEC-297`, `ARC-330`) and therefore belongs in this identity outcome rather than a later pack. Bilingual entry is a launch invariant, not a later translation enhancement.

**Dependencies:** Frozen Product Law, Architecture Law and Domain Law only. No future product pack is a prerequisite.

**Affected Domains:** `Identity & Access` (including Platform Member Reference Account truth); `Privacy & Consent`; `Content & Media`; `Communications`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md §§10–13`; `00_PLATFORM_v1.4.1.md §§15–17, 21L.1–21L.4, 21P, 21Q`; `DEC-017...DEC-028`, `DEC-244...DEC-267`, `DEC-297`, `DEC-298`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§4, 6, 6.6, 8, 9, 12, 14–15`; `ARC-330`; `FLOW-01`; identity, session, PMR lifecycle/non-authority, policy, durable-consequence, observability and degradation themes.

**Major Gates:** `OQ-035` abuse-control thresholds; `OQ-036` email/in-app provider and channel policy; `OQ-038` incident ownership for later production operation. Exact PMR encoding remains downstream (`ARQ-IAM-013`) and is not a Roadmap decision.

**Resolved architecture and proof status:** `OQ-034` authentication architecture selection is resolved; executable authentication proof remains a Phase 8 obligation and is not complete or finalised.

**Gate Classification:**

- `OQ-034 — RESOLVED / ARCHITECTURE SELECTION`: the selected authentication architecture is recorded in the Decision Register. Executable proof remains a Phase 8 obligation; this Roadmap does not claim that proof complete, finalise its classification or authorise Phase 8.
- `OQ-035 — BLOCKS_RELEASE_ONLY`: account flows may be prepared behind the platform-owned abuse boundary, but protected public/pilot release cannot proceed without the approved thresholds and recovery behaviour.
- `OQ-036 — BLOCKS_RELEASE_ONLY`: email verification and mandatory notices need a valid launch channel; future reminder/SMS/WhatsApp choices do not block this pack.
- `OQ-038 — FUTURE_ONLY`: named incident ownership is a paid-pilot/release condition owned by FP-006, not a reason to delay safe internal identity work.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — the first real authentication/session/recovery path materially exercises the accepted identity boundary; Phase 7 decides whether one proof can cover the complete path.

**Performance / Scaling Concern:** Password hashing, registration/login bursts, verification-delivery backlog and abuse controls are the material concerns. PostgreSQL plus durable async delivery is the default; no Redis, replica, GenServer or realtime mechanism is pulled forward except a justified distributed abuse-control boundary.

**Security / Privacy / Safety Concern:** Verification, age confirmation, terms/privacy acceptance, session revocation, recovery, field minimisation and non-enumerating abuse responses must be server-authoritative. The Platform Member Reference is non-secret but private-by-default; possession never proves authentication, authorisation, verification, Membership, subscription or entitlement. Health data is not collected merely to create an account.

**Release Effect:** Internal trusted entry capability; prerequisite for every protected core journey and for the first paid pilot.

**Exit Condition:** A verified account can register, receive one canonical active Platform Member Reference, verify, sign in, recover and be re-authorised after restart/reconnect; support can resolve access issues; sensitive actions are scoped/audited; no duplicate identity/session/PMR effect is observed under retry. The approved architecture selection does not satisfy the still-required Phase 8 executable proof.

**Deferred From This FP:** Social login, passkeys, advanced participant MFA configuration, future product spaces, household accounts, generic tenancy, native applications, implementation-grade auth package choices, and exact Platform Member Reference encoding/prefix/alphabet/grouping/length/checksum/generator/schema (`ARQ-IAM-013`). `FP001_RECONCILIATION_REQUIRED` remains for later narrow FP-001 artifact reconciliation of PMR sequencing meaning; this Roadmap entry does not reopen unrelated FP-001 decisions.

## FP-002 — Purchase to verified payment and entitlement

**ID:** `FP-002`

**Name:** Purchase to verified payment and entitlement

**Outcome:** A participant can purchase one of the three approved South African/ZAR launch products through the launch payment gateway and receive exactly one valid component entitlement only after verified, reconciled payment truth.

**Validation Objective:** Prove commercial willingness and the payment-to-access invariant: browser/provider returns are evidence, Commerce owns payment truth, Entitlements owns access truth, duplicate/reordered/retried provider delivery cannot multiply payment or access, and any component refund follows the versioned allocation accepted and snapshotted at checkout.

**Validation Objective Type:** `COMMERCIAL`, `ARCHITECTURAL`, `SECURITY`, `RELIABILITY`, `OPERATIONAL`, `PERFORMANCE`.

**Why Now:** The approved MVP is a paid product, not an assessment demo. Payment and entitlement truth must exist before assessment credits, plans or purchased-library access can be consumed safely.

**Dependencies:** `FP-001`; approved initial product catalogue and versioned prices.

**Affected Domains:** `Commerce`; `Entitlements`; `Identity & Access`; `Privacy & Consent`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md §§11–13`; `00_PLATFORM_v1.4.1.md §§21L.4–21L.6, 21L.13–21L.18, 21R.1–21R.2, 21R.5`; `DEC-029...DEC-050`, `DEC-258`, `DEC-268...DEC-285`, `DEC-292`, `DEC-299`, `DEC-300`, `DEC-303`.

**Product Hardening Contract:** `paid_right_held_until_delivery_or_terminal_closeout`; `bundle_refund_uses_accepted_order_allocation_snapshot`; `duplicate_payment_preserves_one_valid_right`; `unused_credit_blocks_second_standalone_or_bundle_sale`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 7, 8, 10.4, 12–15`; `FLOW-02`; provider evidence, durable reconciliation, idempotency, authority-before-access and bounded failure themes.

**Major Gates:** `OQ-004` Paystack behaviour validation; `OQ-035` payment/checkout abuse thresholds; `OQ-001` operating entity before production subscriptions/sensitive scale; `OQ-002` is resolved for MVP prices and remains provisional only for future membership pricing.

**Gate Classification:**

- `OQ-004 — BLOCKS_THIS_FP`: exact webhook, retry, refund, dispute and provider-ambiguity behaviour is material to the stated verified-payment outcome.
- `OQ-035 — BLOCKS_RELEASE_ONLY`: the payment boundary may be prepared and internally tested, but paid public/pilot release needs approved abuse thresholds and recovery.
- `OQ-001 — BLOCKS_RELEASE_ONLY`: internal/test commerce work may proceed, but production subscription/payment and sensitive processing cannot be activated before operating authority is sufficient.
- `OQ-002 — NON_BLOCKING_FOR_THIS_FP`: the three MVP prices are already locked as versioned business configuration; the future Basic anchor is not needed here.
- `OQ-036 — NON_BLOCKING_FOR_THIS_FP`: ordinary payment truth does not require the future reminder/channel policy, aside from any mandatory launch communication already handled by FP-001/FP-006.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — this is the first material cross-domain provider-reconciliation path and must prove one payment effect plus one entitlement effect under duplicate/ambiguous execution.

**Performance / Scaling Concern:** Provider-bound latency, callback bursts, checkout contention, retry storms and finite PostgreSQL/worker capacity matter. Use bounded synchronous authority and durable reconciliation; do not introduce event-style Redis/holds, replicas or speculative payment services.

**Security / Privacy / Safety Concern:** Provider credentials stay behind the adapter; browser return cannot grant access; purchaser/recipient separation, refund consequences, scoped support access and audit evidence remain active. Bundle amounts and component allocations are versioned and disclosed before checkout, and component refunds use the immutable order snapshot. One valid right survives duplicate-payment correction; an unused assessment credit blocks a second standalone or bundled assessment sale. No health data is needed to take payment.

**Release Effect:** Internal paid-offer capability and the commercial prerequisite for assessment, plan and library entitlements; not by itself a participant-ready MVP.

**Exit Condition:** Each active price resolves to one authoritative version; verified and pending provider outcomes are distinguishable; retries/reordering are idempotent; refunds/reconciliation are visible; exactly one valid entitlement is granted for the governed purchase; a bundle cannot be sold without a disclosed allocation snapshot that reconciles to its accepted amount; component refunds use that snapshot; and unused-credit repeat purchases are blocked as Product Law requires.

**Deferred From This FP:** Recurring memberships, international/multi-currency billing, event tickets/holds, large promotion systems, future gateways, open sponsorship programmes and provider-specific package/module choices.

## FP-003 — Temperament provenance, assessment and immutable report

**ID:** `FP-003`

**Name:** Temperament provenance, assessment and immutable report

**Outcome:** A purchaser can use a self-reported, book-derived or digitally assessed temperament path and retain immutable assessment/report history under deletion law. Declared self-reported and book-derived results do not receive exact digital scores or the paid digital report; those outputs follow a successfully delivered digital assessment with its own provenance.

**Validation Objective:** Prove that the paid assessment has perceived value and that attempt eligibility, credit consumption, provenance-specific outputs, scoring, result immutability, report versioning and approved bilingual delivery remain reproducible under retry and later digital completion.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `ARCHITECTURAL`, `PRIVACY`, `SECURITY`, `RELIABILITY`.

**Why Now:** Temperament is the differentiating input to the core proposition and is required before plan personalisation. The MVP permits existing known temperament while preserving the authoritative digital assessment credit.

**Dependencies:** `FP-001`, `FP-002`; approved initial methodology and assessment content.

**Affected Domains:** `Temperament`; `Entitlements`; `Identity & Access`; `Content & Media`; `Privacy & Consent`; `Analytics`; `Audit & Evidence`.

**Product Authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md §§8, 11–13`; `00_PLATFORM_v1.4.1.md §§21B, 21L.5–21L.6, 21R.4–21R.5`; `DEC-031...DEC-036`, `DEC-051...DEC-072`, `DEC-272...DEC-273`, `DEC-302`, `DEC-303`.

**Product Hardening Contract:** `declared_temperament_has_no_exact_digital_score_or_report`; `declared_profile_keeps_assessment_credit_unused`; `later_digital_result_appends_without_replacing_prior_provenance`; `ordinary_assessment_credit_cap_and_attempt_interval_apply`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§4–8, 10–15`; `FLOW-03`; immutable/versioned state, deterministic bounded computation, current entitlement and privacy lifecycle themes.

**Major Gates:** `OQ-006` score-distance thresholds if optional labels are activated; `OQ-013` translation-resource design; `OQ-009`/`OQ-029` retention categories for release; methodology/content and rights approval.

**Gate Classification:**

- `OQ-013 — BLOCKS_RELEASE_ONLY`: a bilingual report needs the approved governed translation/version path; core scoring can be modelled before exact Resource detail is fixed.
- `OQ-006 — FUTURE_ONLY`: core launch scoring does not require optional dominance/close/balanced labels unless the Feature Pack explicitly activates them.
- `OQ-009` and `OQ-029 — BLOCKS_RELEASE_ONLY`: retention and deletion categories must be sufficiently approved before paid pilot release, but do not block safe internal assessment modelling.
- Methodology/content/IP approval — `BLOCKS_THIS_FP` for the released assessment version: the Roadmap cannot choose the methodology or rights.

**Anticipated Architectural Proof:** `DECIDE_IN_PHASE_7` — FLOW-03 is architecturally coherent and may reuse the core application/provenance path, but Phase 7 must decide whether assessment submission/report generation has a materially distinct proof claim.

**Performance / Scaling Concern:** Completion bursts, bounded scoring input, report reads and result-history depth matter. PostgreSQL is the authority; immutable methodology/config may be accelerated only if evidence warrants it; history is paginated rather than eagerly loaded; no GenServer or replica is assumed.

**Security / Privacy / Safety Concern:** Answers and raw results are private, immutable while retained, provenance-labelled and participant-accessible under policy; declared profiles never receive exact digital scores or the paid digital assessment report; staff access is minimum-loaded and audited. Temperament never becomes medical authority.

**Release Effect:** Assessment product capability and a required input to the personalised-plan path.

**Exit Condition:** One active attempt and one immutable result are enforced; duplicate/retried submission cannot create a second result; self-reported/book-derived outputs remain distinct from digital scores and reports; included credit remains unused until successful digital assessment delivery; later digital completion appends provenance without replacing prior results; the active unused-credit cap and annual attempt interval prevent stranded repeat purchases; report output is reproducible and bilingual where required.

**Deferred From This FP:** Future assessment families, social quizzes, optional score-distance labels unless gated, advanced psychometric claims, implementation schemas/indexes and non-approved methodology changes.

## FP-004 — Safe health onboarding and deterministic eligibility

**ID:** `FP-004`

**Name:** Safe health onboarding and deterministic eligibility

**Outcome:** A participant completes progressive, purpose-specific health/lifestyle onboarding and receives exactly one current eligibility outcome: `eligible_automated`, `general_wellness_only`, `professional_review_required` or `insufficient_information`.

**Validation Objective:** Prove that safety facts and provenance are collected only for the approved purpose, high-risk/incomplete cases fail closed, General Wellness is available where allowed, urgent guidance is displayed correctly and no automated personalised plan can bypass current safety authority. Safety selects the eligibility pathway; it does not consume a paid right or decide its refund.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `SAFETY`, `PRIVACY`, `SECURITY`, `ARCHITECTURAL`, `RELIABILITY`.

**Why Now:** Eligibility is the safety gate for plan generation. Delaying it until after plan work would allow the most expensive downstream behaviour to guess at clinical policy.

**Dependencies:** `FP-001`, `FP-003` where temperament context is requested; approved clinical eligibility and urgent-help content.

**Affected Domains:** `Health Records`; `Safety & Eligibility`; `Privacy & Consent`; `Identity & Access`; `Content & Media`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md §§8, 12–15`; `00_PLATFORM_v1.4.1.md §§12, 21C, 21L.4, 21L.21, 21R.1`; `DEC-073...DEC-095`, `DEC-271`, `DEC-299`.

**Product Hardening Contract:** `safety_selects_pathway_without_consuming_or_refunding_commercial_right`; `incomplete_information_or_review_keeps_paid_plan_right_held`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5–8, 11, 14–15`; `FLOW-04`, `FLOW-06`; current-authority reads, minimum-data access, fail-closed safety, durable consequences and invalidation themes.

**Major Gates:** `OQ-005` clinical eligibility matrix; `OQ-008` urgent-support wording; `OQ-007` laboratory validity only if laboratory inputs enter this scope; `OQ-009`/`OQ-029` health retention categories.

**Gate Classification:**

- `OQ-005 — BLOCKS_THIS_FP`: exact low/moderate/high routing is the safety outcome and cannot be invented in Roadmap or implementation.
- `OQ-008 — BLOCKS_THIS_FP`: urgent-safety behaviour must carry approved country-specific wording and boundaries before participant release.
- `OQ-007 — FUTURE_ONLY`: the MVP excludes laboratory integration; laboratory validity blocks a later lab-enabled path, not this initial intake unless Phase 7 explicitly discovers a required dependency.
- `OQ-009` and `OQ-029 — BLOCKS_RELEASE_ONLY`: health/professional retention must be sufficiently approved for pilot release; internal safe modelling may proceed without inventing statutory durations.
- `OQ-033 — NON_BLOCKING_FOR_THIS_FP`: a professional-review outcome can be recorded/routed without activating practitioner record authority or practitioner service.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — safety/eligibility is a materially protected authority path; proof must demonstrate fail-closed behaviour and current-state re-evaluation, not only a happy-path form.

**Performance / Scaling Concern:** Safety evaluation must remain bounded under onboarding bursts without broad health-data loads or unsafe caches. PostgreSQL is authoritative; no Redis/ETS copy of raw health data; durable safety consequences and narrow freshness observations are used only where required.

**Security / Privacy / Safety Concern:** Health facts have provenance, purpose-specific consent, minimum access, audit and deletion contracts. High-risk, pregnancy/breastfeeding, eating-disorder, medication, supplement and incomplete cases cannot silently become automated-plan eligible.

**Release Effect:** Unlocks safe plan generation for eligible participants and a lawful General Wellness fallback; does not activate practitioner review.

**Exit Condition:** All four outcomes are reproducible from versioned inputs; current high-risk facts block automated plans; `safety_paused` behaviour is possible; urgent messaging and audit evidence are present; pathway selection alone does not consume or refund a commercial right; incomplete information and pending review keep the purchased plan right held; no stale session/cache can override current safety authority.

**Deferred From This FP:** Laboratory integration, automated complex clinical cases, pregnancy-specific plans, eating-disorder treatment, document interpretation, wearables and practitioner-review workflow.

## FP-005 — Safe seven-day plan, purchased library and basic feedback

**ID:** `FP-005`

**Name:** Safe seven-day plan, purchased library and basic feedback

**Outcome:** An eligible participant receives an immutable, explainable, bilingual seven-day plan or approved General Wellness Starter Pathway, can access purchased report/plan content, switch approved language and energy-unit presentation, and record lightweight daily/weekly progress and feedback. General Wellness does not fulfil a purchased personalised-plan entitlement.

**Feedback classification guardrail:** FP-005 “basic feedback” and daily/weekly progress entries are participant progress / self-tracking / usefulness evidence under `Habits, Journals & Progress` for the core plan loop. They do **not** activate Domain 19 Research & Feedback. Research & Feedback remains `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` until a later governed Roadmap decision. Plan/protocol calculations required by this outcome remain Plans & Nutrition authority (`calculation != authority` for Interactive Tools elsewhere).

**Validation Objective:** Prove the central paid proposition: safe temperament-guided guidance is useful in real life, deterministic plan generation is reproducible, no partial/duplicate plan is delivered, paid-plan rights are consumed only after successful delivery or closed through the governed component-refund path, consent withdrawal controls future processing, content versions are traceable and basic usage evidence can be collected without turning feedback into clinical authority.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `SAFETY`, `ARCHITECTURAL`, `PRIVACY`, `RELIABILITY`, `PERFORMANCE`.

**Why Now:** This is the first point where the participant receives the promised paid value. It follows both assessment/provenance and safety/eligibility so the plan engine never becomes a substitute for either authority.

**Dependencies:** `FP-001` through `FP-004`; approved calculation, content, recipe/substitution, safety and bilingual versions.

**Affected Domains:** `Plans & Nutrition`; `Content & Media`; `Entitlements`; `Habits, Journals & Progress`; `Safety & Eligibility`; `Temperament`; `Privacy & Consent`; `Identity & Access`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md §§8, 9, 12–16`; `00_PLATFORM_v1.4.1.md §§10–14, 21D–21E, 21L.4–21L.6, 21L.21–21L.23, 21R.1–21R.3`; `DEC-096...DEC-122`, `DEC-271...DEC-273`, `DEC-299`, `DEC-300`, `DEC-301`.

**Product Hardening Contract:** `general_wellness_is_not_personalised_plan_fulfilment`; `paid_plan_right_waits_for_delivery_or_component_refund_closeout`; `purpose_withdrawal_stops_future_processing_without_itself_ending_commercial_right`; `component_refund_uses_accepted_order_snapshot`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§4–10, 11, 13–15`; `FLOW-05`, `FLOW-06`; deterministic bounded work, immutable snapshots, content provenance, current safety checks, durable async and degradation themes.

**Major Gates:** `OQ-010` calculation values; `OQ-013` translation-resource design; `OQ-016` content publication operations; `OQ-014` edge/cache design only for any shared public/personalised cache; `OQ-011`/`OQ-012` for later adjustment, not the once-off MVP.

**Gate Classification:**

- `OQ-010 — BLOCKS_THIS_FP`: formulas, limits, minimums and bounded weight-reduction values are part of safe plan truth.
- `OQ-013 — BLOCKS_THIS_FP`: the paid/safety-critical bilingual plan path needs approved locale/version semantics before release.
- `OQ-016 — BLOCKS_RELEASE_ONLY`: approved publication, stale-approval checks and correction/withdrawal operations must be live before the pilot; ordinary planning can precede exact scheduler implementation.
- `OQ-014 — NON_BLOCKING_FOR_THIS_FP`: the MVP can use safe non-shared delivery; advanced edge caching is not required to prove plan correctness.
- `OQ-011` and `OQ-012 — FUTURE_ONLY`: automatic monthly adjustment is explicitly excluded from the smallest once-off MVP and belongs to FP-010.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — deterministic plan generation, immutable snapshotting, content fan-in and safety pause/replacement form a materially new enduring path even though it reuses the accepted transaction/authority doctrine.

**Performance / Scaling Concern:** Generation cost, content/query fan-in, duplicate requests, queue backlog and participant history reads matter. Use bounded generation and durable execution where required; stream/paginate history; do not add Redis, replicas, GenServers or realtime merely to make a seven-day plan feel like a platform-scale workload.

**Security / Privacy / Safety Concern:** Eligibility is re-read at the authoritative boundary; plan snapshots retain input/version provenance; protected content checks current entitlement; safety correction/withdrawal can pause or replace a plan; purpose withdrawal stops affected future processing without itself cancelling the paid entitlement or rewriting delivered plan history; component refunds follow the order's accepted allocation snapshot; no raw health details are copied into feeds/analytics unnecessarily.

**Release Effect:** Completes the participant-facing paid core journey; still requires FP-006 before real paid pilot release.

**Exit Condition:** Eligible and General Wellness outcomes produce the correct governed output, with General Wellness never counted as fulfilment of the purchased personalised-plan right; incomplete/review outcomes preserve the unconsumed paid right; eligible delivery consumes it only after successful delivery and final unfulfillable outcomes close it through the accepted component-refund snapshot; consent withdrawal stops future purpose processing without itself ending commercial rights or rewriting delivered plan truth; plans are deterministic/reproducible, immutable and bilingual; purchased access is correct; progress/feedback is private, bounded and auditable.

**Deferred From This FP:** Monthly automatic adjustment, Premium, full foundation programme, first-party community, direct messaging, advanced feed ranking/search, calorie diary, wearables, AI-generated plans/recipes/translations, native apps, Domain 19 Research campaigns/instruments, and any generic Interactive Tools catalogue not required by this pack's stated outcome.

## FP-006 — Controlled core operations and staged paid release

**ID:** `FP-006`

**Name:** Controlled core operations and staged paid release

**Outcome:** Named operators can run, support, observe, correct, withdraw, reconcile and safely stop the approved core journey through internal validation, the first 10 paid participants, review, expansion toward 25, maximum 50 in the first paid pilot, limited public release and general public release decisions.

**Validation Objective:** Prove that the core commercial journey is operable as a real service: payment/entitlement support works, critical safety and plan failures are visible, corrections and withdrawals are safe, deletion/restore and incident procedures are exercised, and release authority can make evidence-based proceed/iterate/repeat/pause/rollback decisions.

**Validation Objective Type:** `OPERATIONAL`, `RELIABILITY`, `SECURITY`, `PRIVACY`, `SAFETY`, `COMMERCIAL`, `PERFORMANCE`, `ARCHITECTURAL`.

**Why Now:** A technically complete journey is not a paid pilot until responsible owners can operate it. This pack is the release/evidence boundary for the core MVP rather than a generic administration layer.

**Dependencies:** `FP-001` through `FP-005`; named product, clinical, content, commerce, legal/privacy, security and operations owners.

**Affected Domains:** `Identity & Access`; `Privacy & Consent`; `Commerce`; `Entitlements`; `Temperament`; `Health Records`; `Safety & Eligibility`; `Plans & Nutrition`; `Content & Media`; `Communications`; `Analytics`; `Audit & Evidence`.

**Product Authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md §§15–17A, 19A–24`; `00_PLATFORM_v1.4.1.md §§21L.13–21L.24`; `DEC-280...DEC-291`; source-at-freeze tracker `archive/02_OPEN_WORK_v1.2.45.md §§8, 11`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§7–15`; `FLOW-01...FLOW-06`, `FLOW-08`, `FLOW-11`; release/degradation, deletion/recovery, observability, audit and staged performance-proof themes.

**Major Gates:** `OQ-001`, `OQ-009`, `OQ-029`, `OQ-030`, `OQ-031`, `OQ-032`, `OQ-035`, `OQ-036`, `OQ-037`, `OQ-038`, plus the Product Law cross-functional paid-pilot readiness gate.

**Gate Classification:**

- `OQ-001 — BLOCKS_RELEASE_ONLY`: operating authority must be sufficient for production subscriptions and sensitive health processing; internal validation is not a substitute for the production gate.
- `OQ-009` and `OQ-029 — BLOCKS_THIS_FP`: the pilot cannot safely run without approved enough retention categories for health, professional, financial and audit evidence.
- `OQ-030`, `OQ-031`, `OQ-032 — BLOCKS_THIS_FP`: external processor deletion/export, deletion-safe restore and operational deletion/export behaviour protect the data handled by the pilot.
- `OQ-035`, `OQ-036`, `OQ-037`, `OQ-038 — BLOCKS_RELEASE_ONLY`: these are required for pilot/release readiness; earlier pack construction may proceed behind bounded interfaces and safe internal controls.
- `OQ-039 — NON_BLOCKING_FOR_THIS_FP`: the Phase-5 lightweight profiles are complete; implementation-grade mapping belongs to Phase 7/affected slices and evidence, not to Roadmap closure.

**Anticipated Architectural Proof:** `REUSE_EXISTING_PROOF` for mechanisms already pressure-tested/proven by FP-001 through FP-005, followed by the required hardening/release evidence. A new tracer bullet is not justified merely because operators need dashboards or controls.

**Performance / Scaling Concern:** Use Product Law's progressive gates: internal validation, first 10, review, toward 25, review, maximum 50, then limited/general public only with evidence. Prove bounded queries, no core N+1, idempotent checkout/entitlement, bounded generation, visible queues and recovery; do not demand 100,000-user load for the first 10.

**Security / Privacy / Safety Concern:** Cross-functional sign-off is non-waivable across Product, Clinical, Content, Commerce, Legal/Privacy, Security and Operations. Correction/withdrawal, staff MFA, sensitive access, backup/restore, deletion, incident response and immediate safety/technical stop actions must be usable before pilot expansion.

**Release Effect:** Internal capability; first 10 paid participants; expansion toward 25; maximum 50 first paid pilot; limited public and general public release gates.

**Exit Condition:** Required owners sign off; zero duplicate charges/entitlements, unreproducible plans, critical platform-caused safety failures and unauthorised sensitive-data exposures; support, alerts, queues, restore, deletion, rollback and stop controls are exercised; pilot evidence is recorded.

**Deferred From This FP:** Broad public scale, first-party community, memberships, Premium, practitioner services, event commerce, experimentation, multi-market activation and any infrastructure justified only by those later paths.

## FP-007 — Governed live sessions and replay

**ID:** `FP-007`

**Name:** Governed live sessions and replay

**Outcome:** A participant can discover and register for an approved live session, pass current entitlement/access checks, join protected playback, and receive a governed replay where recording/consent rules allow; operators can see provider or delivery failure without changing platform truth.

**Validation Objective:** Prove the early live value required by Nuwe Jy and Membership without introducing full event commerce: live provider integration, registration, access, recording notice, replay publication and recovery are coherent and operationally owned.

**Validation Objective Type:** `PRODUCT`, `OPERATIONAL`, `ARCHITECTURAL`, `PRIVACY`, `SECURITY`, `RELIABILITY`, `PERFORMANCE`.

**Why Now:** Product Law requires live value before Basic Membership can be sold and places live/replay in the first Nuwe Jy activation gate. Live must be proven as a governed experience before later event scarcity is considered.

**Dependencies:** `FP-006`; approved session owner and live/replay content/policy.

**Affected Domains:** `Events & Live`; `Entitlements`; `Identity & Access`; `Content & Media`; `Communications`; `Privacy & Consent`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§21G.14–21G.16, 21L.7–21L.12, 21L.19`; `DEC-186...DEC-190`, `DEC-206`, `DEC-274`, `DEC-279`, `DEC-286`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§7–10, 12–15`; `FLOW-07`; provider boundary, protected playback, PubSub-as-observation, durable scheduled consequence and recovery themes.

**Major Gates:** `OQ-020` Restream/Cloudflare validation; `OQ-021` video consent and retention; `OQ-036` notification/channel policy; `OQ-017` only for optional reminders; `OQ-022` for later ticket/hold commerce.

**Gate Classification:**

- `OQ-020 — BLOCKS_THIS_FP`: the approved provider path and failure behaviour are part of the live/replay outcome.
- `OQ-021 — BLOCKS_THIS_FP`: recording, attendee, replay and withdrawal rules protect participants and presenters.
- `OQ-036 — BLOCKS_THIS_FP` for any promised live notification journey; the live capability itself cannot assume an unapproved provider/channel.
- `OQ-017 — NON_BLOCKING_FOR_THIS_FP`: reminder scheduling is optional until a governed reminder promise is added.
- `OQ-022 — FUTURE_ONLY`: scarce event reservations and flash-sale mechanics belong to FP-015, not ordinary live access.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — external stream/replay/provider evidence and protected delivery are materially new, even though registration and entitlement authority are reused.

**Performance / Scaling Concern:** Live fan-out, reconnects, provider capacity and replay delivery are the material risks. Start with bounded sessions and provider-supported delivery; PubSub may signal freshness but is not attendance/replay truth; no event hold or Redis admission infrastructure is pulled forward.

**Security / Privacy / Safety Concern:** Current entitlement and policy are checked before playback; recording notice/consent, replay scope, participant privacy and provider minimisation are mandatory; live failure cannot manufacture access or erase attendance truth.

**Release Effect:** Unlocks Nuwe Jy live integration, early Membership live value and a reusable live/replay path; does not unlock paid event commerce.

**Exit Condition:** A governed session can be published, registered, joined, recorded/replayed under approved policy, reconciled after provider failure and audited; notification failure is visible; protected playback never leaks through stale access.

**Deferred From This FP:** Ticket types, scarce reservations, waitlists, flash-sale admission, reserved seating, transfers/refunds/credits for paid events and generic streaming infrastructure.

## FP-008 — Native Nuwe Jy flagship edition

**ID:** `FP-008`

**Name:** Native Nuwe Jy flagship edition

**Outcome:** The first native Nuwe Jy edition can operate as an approved 60-calendar-day scheduled cohort with a Today experience, daily releases, habits/check-ins/progress/recovery, temperament-aware delivery, central safety/plan integration, governed cohort community, live/replay, support/communications and compassionate completion evidence.

**Validation Objective:** Prove the first concrete flagship composition and use it to drive only the reusable programme/version/edition/cohort primitives that the platform genuinely needs. Prove scheduled release idempotency, recovery, safe routing, participant/purchaser separation and operational capacity.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `OPERATIONAL`, `SAFETY`, `PRIVACY`, `ARCHITECTURAL`, `RELIABILITY`, `PERFORMANCE`.

**Why Now:** Product Law names Nuwe Jy as the first native flagship after the paid core MVP is proven and hardened. It is the concrete acceptance test for programme capability; a generic LMS is deliberately not a prerequisite.

**Dependencies:** `FP-005`, `FP-006`, `FP-007`; approved Nuwe Jy content/source inventory and edition owners.

**Affected Domains:** `Programmes & Challenges`; `Habits, Journals & Progress`; `Content & Media`; `Entitlements`; `Temperament`; `Safety & Eligibility`; `Plans & Nutrition`; `Community`; `Events & Live`; `Communications`; `Identity & Access`; `Privacy & Consent`; `Analytics`; `Audit & Evidence`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§21F, 21G, 21H, 21L.7, 21L.19`; `DEC-196...DEC-219`, `DEC-274`, `DEC-286`; `GQ-NY-001` acceptance rules.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 8–13, 15`; `FLOW-07`, `FLOW-06`, `FLOW-08`; durable scheduling, bounded fan-out, programme composition, notification, realtime observation and recovery themes.

**Major Gates:** `OQ-017`, `OQ-019`, `OQ-020`, `OQ-021`, `OQ-023`, `OQ-024`, `OQ-025`, `OQ-026`, `OQ-027`, `OQ-028`, `OQ-036`; inherited clinical/translation/retention gates.

**Gate Classification:**

- `OQ-024 — BLOCKS_THIS_FP`: the native edition cannot be activated without an approved source-content/media/rights/translation inventory.
- `OQ-025 — BLOCKS_THIS_FP`: Nuwe Jy safety routing, milestones and completion rules must be approved before activation.
- `OQ-026 — BLOCKS_THIS_FP`: cohort/facilitator/moderator/support/live ownership and saleable capacity are part of the outcome.
- `OQ-027 — BLOCKS_THIS_FP`: scheduled communication channels, deduplication, caps and failure ownership are required for the edition.
- `OQ-020`, `OQ-021`, `OQ-017`, `OQ-036 — BLOCKS_RELEASE_ONLY`: the applicable live/reminder/notification paths must be resolved before edition activation; core programme composition can be prepared earlier.
- `OQ-023` and `OQ-028 — BLOCKS_RELEASE_ONLY`: governed Facebook operation and LearnDash retirement/cutover obligations must be clear before the native edition is activated, but do not block core MVP work.
- `OQ-019 — BLOCKS_THIS_FP`: edition completion metrics are part of the approved product outcome.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — scheduled release, durable recovery, cohort fan-out and cross-domain participant state are materially new; the proof must be one real edition path, not a ceremonial scheduler demo.

**Performance / Scaling Concern:** Cohort release bursts, notification fan-out, queue catch-up, reconnect storms and progress writes matter. Release work must be durable, idempotent and bounded; lists/history are paginated; no generic hot cache, GenServer or multi-node topology is assumed before evidence.

**Security / Privacy / Safety Concern:** Progressive onboarding, consent, safety route, purchaser/participant separation, private progress/journals, scoped facilitator/moderator access, recording consent, deletion and urgent escalation cannot be weakened for cohort convenience.

**Release Effect:** First native Nuwe Jy edition and the concrete reusable programme/edition/cohort acceptance path.

**Exit Condition:** All applicable Nuwe Jy activation gates pass; all 60 days, translations, schedules, safety/completion/recovery rules and owners are approved; duplicate releases are prevented; communications/live/community failure is visible; recovery is tested.

**Voting guardrail:** FP-008 does **not** require Voting & Balloting merely because public Nuwe Jy-style voting is an approved Product mode. Voting & Balloting remains `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` until a later governed Roadmap decision assigns an activating outcome.

**Deferred From This FP:** Generic LMS/page builder, LearnDash importer/converter, evergreen programme before evidence, first-party community implementation, open practitioner network, mass event commerce, unlimited coaching, and Voting & Balloting / official-result capability.

## FP-009 — Basic Membership recurring value

**ID:** `FP-009`

**Name:** Basic Membership recurring value

**Outcome:** A participant can buy and maintain Basic Monthly or Annual Membership and receive genuinely operational moderated community access, at least one approved member-content release per month, at least one live session per month, group Q&A submission and correct entitlement/cancellation behaviour.

**Validation Objective:** Prove that recurring value exists before recurring revenue is sold, and that the membership contract, access rights, content/live operations, community moderation and cancellation lifecycle are coherent.

**Validation Objective Type:** `COMMERCIAL`, `PRODUCT`, `OPERATIONAL`, `RELIABILITY`, `PRIVACY`, `SECURITY`, `ARCHITECTURAL`.

**Why Now:** Basic Membership is deliberately gated after minimum recurring value is operational. It may launch alongside or after Nuwe Jy; it must not be sold on a promise that benefits will be built later.

**Dependencies:** `FP-002`, `FP-006`, `FP-007`; governed community operating path and approved monthly value owners. `FP-008` is useful evidence but is not a circular hard dependency.

**Affected Domains:** `Commerce`; `Entitlements`; `Community`; `Content & Media`; `Events & Live`; `Communications`; `Identity & Access`; `Privacy & Consent`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§8, 21G, 21L.8, 21L.11–21L.18`; `DEC-039...DEC-043`, `DEC-170...DEC-190`, `DEC-275`, `DEC-278`, `DEC-283...DEC-285`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 7–10, 12–15`; recurring Commerce/Entitlements, communications, live/replay, privacy and provider-boundary themes.

**Major Gates:** `OQ-001`, `OQ-002`, `OQ-004`, `OQ-016`, `OQ-017`, `OQ-020`, `OQ-021`, `OQ-023`, `OQ-036`; operating/moderation and content approvals.

**Gate Classification:**

- `OQ-004 — BLOCKS_THIS_FP`: recurring billing, failed-payment, proration, cancellation, refund and webhook behaviour is the commercial contract.
- `OQ-016 — BLOCKS_THIS_FP`: monthly approved content must have reliable publication and stale-approval recovery.
- `OQ-023 — BLOCKS_THIS_FP`: the governed early community channel needs moderation, privacy, disclosure and escalation policy.
- `OQ-020` and `OQ-021 — BLOCKS_RELEASE_ONLY`: live/replay value reuses FP-007's resolved path; any new membership-specific live promise must pass its own operational gate.
- `OQ-001` and `OQ-002 — BLOCKS_RELEASE_ONLY`: operating authority and final evidence-based public pricing are required before selling, but neither blocks reuse of the one entitlement system in earlier packs.
- `OQ-017` and `OQ-036 — BLOCKS_RELEASE_ONLY`: recurring reminders/notifications cannot be promised until channel, consent, quiet-hour and retry behaviour is approved.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — the recurring provider/billing lifecycle is materially new beyond once-off payment, although entitlement and reconciliation mechanisms are reused.

**Performance / Scaling Concern:** Billing waves, monthly content fan-out, group access checks, Q&A volume and cancellation changes are the material risks. Use bounded/paginated reads, durable communications and current entitlement checks; no membership-specific cache or service is justified at launch.

**Security / Privacy / Safety Concern:** Membership access is current-policy checked; community disclosures remain moderated; marketing consent stays separate from mandatory notices; purchaser/participant and private health boundaries remain intact; cancellation must not accidentally restore or remove unrelated purchased rights.

**Release Effect:** Basic Membership public/controlled release once its promised recurring value is genuinely operational.

**Exit Condition:** A member receives the promised monthly content/live/community/Q&A value through a complete billing period; cancellation/failed-payment/grace behaviour is correct; moderation/support/notification failure is visible; no entitlement corruption occurs.

**Deferred From This FP:** Premium, plan adjustment, first-party community, unrestricted direct messaging, generic social feed, challenges, open practitioner access and event ticketing.

## FP-010 — Recurring plan review and governed adjustment

**ID:** `FP-010`

**Name:** Recurring plan review and governed adjustment

**Outcome:** An entitled participant with sufficient approved check-ins can receive a monthly trend-based review and, where allowed, an immutable governed plan adjustment with explicit grace/incomplete-check-in behaviour and renewed safety evaluation. Withdrawing personalisation or automated-recommendation consent stops future adjustment processing without rewriting delivered plan history.

**Validation Objective:** Prove that recurring adjustment is useful, clinically bounded, versioned and operationally safe before it is packaged as Premium; prove that progress inputs inform Plans without becoming Safety authority, and purpose withdrawal blocks future personalisation/automated adjustments while preserving historical plan truth.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `SAFETY`, `ARCHITECTURAL`, `PRIVACY`, `RELIABILITY`, `PERFORMANCE`.

**Why Now:** Product Law explicitly requires stable once-off plan delivery and useful check-ins before recurring adjustment. The smallest MVP excludes automatic monthly adjustment, so this is a later evidence boundary. Recurring adjustment calculations required by this outcome remain Plans & Nutrition authority; this is not an Interactive Tools Feature Pack activation.

**Dependencies:** `FP-005`, `FP-006`; approved trend/check-in evidence and clinical/product review rules. `FP-009` is not required unless the adjustment is packaged through membership.

**Affected Domains:** `Plans & Nutrition`; `Habits, Journals & Progress`; `Health Records`; `Safety & Eligibility`; `Entitlements`; `Temperament`; `Content & Media`; `Privacy & Consent`; `Audit & Evidence`; `Analytics`; `Commerce` where an add-on is sold.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§14, 21D.8–21D.14, 21L.9, 21R.3`; `DEC-087`, `DEC-096...DEC-122`, `DEC-276`, `DEC-301`; `OQ-003`/`OQ-011`/`OQ-012` definitions.

**Product Hardening Contract:** `personalisation_or_recommendation_withdrawal_stops_future_adjustments`; `withdrawal_does_not_rewrite_delivered_plan_history`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 7–9, 11–15`; `FLOW-06`; current safety authority, immutable plan versions, durable scheduled work and failure/recovery themes.

**Major Gates:** `OQ-003` monthly review contract; `OQ-011` adjustment thresholds; `OQ-012` review timing; `OQ-010` where calculation values are changed; inherited `OQ-005` and retention gates.

**Gate Classification:**

- `OQ-003`, `OQ-011`, `OQ-012 — BLOCKS_THIS_FP`: exact deadlines, grace, trend windows, adherence and recalculation thresholds define this outcome.
- `OQ-010 — BLOCKS_RELEASE_ONLY`: only if the adjustment changes approved calculation values; otherwise it remains inherited from FP-005.
- `OQ-005 — BLOCKS_RELEASE_ONLY`: current eligibility/safety rules must still be applied before any adjusted plan is activated, but no new matrix is invented here.
- `OQ-018 — NON_BLOCKING_FOR_THIS_FP`: basic check-ins need not become private journals; journal encryption/retention belongs to FP-014 if journals enter scope.
- `OQ-004 — FUTURE_ONLY` for this pack unless an adjustment add-on introduces new recurring payment behaviour; FP-011 owns the packaged billing gate.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — adjustment has a new trend/schedule/version/safety interaction; Phase 7 may reuse the FP-005 generation proof if the enduring mechanism is genuinely the same.

**Performance / Scaling Concern:** Monthly review batches, check-in history and plan-generation bursts must be bounded and durable. Use pagination/streaming and batchable async consequences; do not build a continuous recalculation service, hot counter system or replica before evidence.

**Security / Privacy / Safety Concern:** Health/progress inputs remain purpose-scoped; personalisation or automated-recommendation withdrawal blocks future adjustment processing; safety can pause/restrict adjustment; historical plan versions remain visible under policy and are not rewritten by withdrawal; no isolated adjustment engine may bypass Plans or Safety ownership.

**Release Effect:** Unlocks the plan-adjustment add-on and the capability prerequisite for Premium.

**Exit Condition:** Approved check-in/trend cases produce one reproducible reviewed outcome or explicit no-change/insufficient-data outcome; adjusted plans are immutable, safe, explainable and auditable; withdrawal stops future adjustment processing without rewriting delivered plan history; incomplete data cannot silently trigger a change.

**Deferred From This FP:** Once-off MVP adjustment, clinical weight restoration, AI recommendations, continuous wearable/CGM input, unrestricted recalculation and Premium packaging.

## FP-011 — Premium bundle around proven capability

**ID:** `FP-011`

**Name:** Premium bundle around proven capability

**Outcome:** Premium is sold as a versioned bundle of working recurring review/adjustment and approved benefits through the existing Commerce and Entitlements model, including governed reassessment rules where applicable, without promising unlimited practitioner access.

**Validation Objective:** Prove that Premium is a commercial composition of validated capabilities rather than a parallel entitlement architecture or a promise of unfinished service.

**Validation Objective Type:** `COMMERCIAL`, `PRODUCT`, `ARCHITECTURAL`, `SECURITY`, `PRIVACY`, `OPERATIONAL`, `RELIABILITY`.

**Why Now:** Premium follows, rather than funds, recurring adjustment. Packaging it earlier would make unresolved clinical, billing and operational assumptions a customer promise.

**Dependencies:** `FP-009` where Premium uses the membership contract; `FP-010`; `FP-002`, `FP-005`, `FP-006`; approved benefits and pricing.

**Affected Domains:** `Commerce`; `Entitlements`; `Plans & Nutrition`; `Habits, Journals & Progress`; `Health Records`; `Safety & Eligibility`; `Content & Media`; `Communications`; `Identity & Access`; `Privacy & Consent`; `Analytics`; `Audit & Evidence`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§8, 21A.5–21A.8, 21L.9, 21L.16–21L.18`; `DEC-035`, `DEC-038...DEC-046`, `DEC-276`, `DEC-283...DEC-284`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 7–8, 11, 14–15`; Commerce/Entitlements separation, current access, provider reconciliation, privacy and durable adjustment themes.

**Major Gates:** `OQ-001`, `OQ-002`, `OQ-003`, `OQ-004`, `OQ-011`, `OQ-012`, `OQ-036`; inherited safety, retention, content and operational gates.

**Gate Classification:**

- `OQ-003`, `OQ-011`, `OQ-012 — BLOCKS_THIS_FP`: Premium cannot promise monthly review/adjustment before those rules are operating.
- `OQ-004 — BLOCKS_THIS_FP`: Premium billing, failed payments, cancellation, reassessment and refund consequences need validated provider behaviour.
- `OQ-001` and `OQ-002 — BLOCKS_RELEASE_ONLY`: operating authority and evidence-based Premium pricing are needed before public sale; the shared model can be prepared earlier.
- `OQ-036 — BLOCKS_RELEASE_ONLY`: recurring benefit communications must have approved channel/consent/retry behaviour.
- No separate membership/entitlement engine — `NON_BLOCKING_FOR_THIS_FP`: Product and Domain Law require reuse of the existing owners.

**Anticipated Architectural Proof:** `REUSE_EXISTING_PROOF` — reuse FP-002/FP-009 commercial reconciliation and FP-010 plan-adjustment proof; only a materially different provider or authority path would justify a new tracer bullet.

**Performance / Scaling Concern:** Recurring billing waves, review scheduling and current access checks share finite database/worker/provider budgets. Use durable bounded work and current-policy reads; do not create Premium-specific caches, queues or services by product name alone.

**Security / Privacy / Safety Concern:** Premium never weakens consent, safety, practitioner boundaries, deletion or payment integrity; reassessment credits are scoped/consumable; access after cancellation follows the relevant entitlement law.

**Release Effect:** Premium public/controlled release and a validated higher-value commercial tier.

**Exit Condition:** The bundle resolves to explicit component entitlements; all component capabilities pass their own gates; upgrade/downgrade/cancellation/failed-payment paths preserve purchased access rules; no unlimited practitioner expectation is created.

**Deferred From This FP:** Open practitioner marketplace, unlimited messaging, unapproved clinical pathways, customer-specific dynamic pricing and parallel bundle infrastructure.

## FP-012 — Controlled practitioner review pilot

**ID:** `FP-012`

**Name:** Controlled practitioner review pilot

**Outcome:** An eligible participant can purchase a limited practitioner-review service, provide explicit consent, receive a scoped active relationship and structured review outcome, and receive an approved modification, restriction, follow-up or referral with capacity and turnaround visible to operators and participants.

**Validation Objective:** Prove the professional-service model, record/consent boundary, practitioner capacity model, safety escalation and economics before any wider practitioner network is considered.

**Validation Objective Type:** `PRODUCT`, `COMMERCIAL`, `SAFETY`, `PRIVACY`, `SECURITY`, `OPERATIONAL`, `RELIABILITY`.

**Why Now:** Practitioner review is a later controlled service after automated plan delivery is stable. It is scarce professional capacity, not a prerequisite for the automated MVP.

**Dependencies:** `FP-004`, `FP-005`, `FP-006`; authorised practitioner(s), explicit service price and approved turnaround/capacity.

**Affected Domains:** `Professional Care`; `Identity & Access`; `Privacy & Consent`; `Health Records`; `Safety & Eligibility`; `Plans & Nutrition`; `Commerce`; `Entitlements`; `Audit & Evidence`; `Analytics`; `Communications`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§15–18, 21C, 21D, 21L.10, 21L.20`; `DEC-011`, `DEC-012`, `DEC-024...DEC-026`, `DEC-091...DEC-093`, `DEC-277`, `DEC-287`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5–8, 11, 14–15`; `FLOW-10`; scoped authority, professional record, consent, current policy, audit and capacity themes.

**Major Gates:** `OQ-001` operating entity; `OQ-009`/`OQ-029` retention; `OQ-033` professional record authority; practitioner agreements; relevant clinical gates; staff/practitioner MFA and incident ownership.

**Gate Classification:**

- `OQ-033 — BLOCKS_THIS_FP`: professional record authority, participant access, addendum and disposition rules are necessary for a professional service.
- `OQ-001 — BLOCKS_THIS_FP`: practitioner contracting and sensitive professional processing require operating authority.
- `OQ-009` and `OQ-029 — BLOCKS_THIS_FP`: professional/health retention categories must be approved before cases are sold.
- Practitioner agreements and saleable-capacity approval — `BLOCKS_THIS_FP`: the service cannot promise human review without named authority, scope and capacity.
- `OQ-004 — BLOCKS_RELEASE_ONLY`: only if the service uses a new recurring billing contract; once-off review may reuse FP-002 validation.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — consented practitioner access, scoped record handling and cross-domain professional outcomes are materially new and security-sensitive.

**Performance / Scaling Concern:** Capacity and turnaround, not raw throughput, are the dominant constraints. Case queues and histories are paginated; no cache of sensitive professional records, no GenServer ownership and no open marketplace are justified.

**Security / Privacy / Safety Concern:** Access requires consent + active relationship + scope + expiry + audit; staff/practitioner MFA is mandatory; professional outcomes command Safety/Plans owners rather than mutating their truth; urgent and external-referral boundaries remain explicit.

**Release Effect:** Limited priced practitioner-review pilot with capacity-controlled saleability.

**Exit Condition:** Every case has an authorised practitioner, consent/scope/expiry, visible capacity/turnaround, structured outcome, audit, follow-up/referral handling and approved record disposition; demand, safety and economics evidence are recorded.

**Deferred From This FP:** Open practitioner marketplace, unlimited messaging, automatic practitioner matching, broad practitioner network, replacement of clinical authority and any claim that platform records are the final external professional record.

## FP-013 — First-party community and governed challenges

**ID:** `FP-013`

**Name:** First-party community and governed challenges

**Outcome:** Participants can join a first-party moderated community and safe governed challenges with current entitlement checks, privacy-aware profiles, private progress/recognition, reporting/moderation/sanctions/appeals and deletion/anonymisation behaviour.

**Validation Objective:** Use evidence from Nuwe Jy/Membership external communities to prove what NewYou-specific first-party community and challenge capabilities are worth building; preserve safe peer experience without creating a generic social network.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `OPERATIONAL`, `SAFETY`, `PRIVACY`, `SECURITY`, `PERFORMANCE`, `ARCHITECTURAL`.

**Why Now:** Product Law explicitly defers first-party community until evidence shows its need. It must follow governed external moderation/participation learning, not precede it as speculative infrastructure.

**Dependencies:** `FP-006`; evidence from `FP-008` and/or `FP-009`; `FP-007` if live/challenge sessions are included.

**Affected Domains:** `Community`; `Programmes & Challenges`; `Habits, Journals & Progress`; `Entitlements`; `Identity & Access`; `Privacy & Consent`; `Content & Media`; `Communications`; `Safety & Eligibility`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§21F–21G, 21L.8, 21L.11`; `DEC-170...DEC-185`, `DEC-205`, `DEC-278`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 7–10, 11, 13–15`; community moderation, access-first feeds, privacy/deletion, pagination and realtime-observation themes.

**Major Gates:** `OQ-023` community operating policy; `OQ-017` reminder design if reminders are included; `OQ-018` journal encryption/retention if journals enter the community experience; `OQ-019` challenge/programme completion metrics; `OQ-036` notification policy; abuse/moderation staffing and safety escalation.

**Gate Classification:**

- `OQ-023 — BLOCKS_THIS_FP`: migration from external validation to first-party community needs the operating, privacy, moderation and evidence policy.
- `OQ-019 — BLOCKS_THIS_FP`: challenge completion/recognition rules must be approved before a challenge is published.
- `OQ-018 — BLOCKS_RELEASE_ONLY`: only if private journals/attachments are included; community can begin without journal capability.
- `OQ-017` and `OQ-036 — BLOCKS_RELEASE_ONLY`: reminders/notifications are conditional surfaces, not a reason to build first-party community before evidence.
- `OQ-035 — BLOCKS_RELEASE_ONLY`: exact distributed abuse thresholds must be ready before a high-volume public community release; internal moderation design may precede them.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — native feed/moderation/privacy/access interaction is a materially new path; no generic social proof is assumed.

**Performance / Scaling Concern:** Feeds, hot threads, moderation queues, attachments, reporting bursts and pagination matter. Start with bounded PostgreSQL-backed reads and current access checks; Redis/read replicas/realtime fan-out are evidence-gated; raw journal/health data is never copied into feed infrastructure by default.

**Security / Privacy / Safety Concern:** Moderation is designed in; peer advice cannot become diagnosis/prescription; sensitive disclosures are redirected; reporter identity and participant/private health boundaries are protected; deletion/anonymisation preserves only lawful restricted moderation evidence.

**Release Effect:** First-party community pilot and governed challenges where evidence supports them.

**Exit Condition:** Moderation staffing, reports/sanctions/appeals, safe challenge rules, entitlement admission, deletion behaviour, rate/abuse handling and operator visibility work under representative pilot load.

**Voting guardrail:** FP-013 does **not** require Voting & Balloting merely because challenges or community surfaces could use polls or competitions. Voting & Balloting remains `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` until a later governed Roadmap decision assigns an activating outcome. Research polls remain Research by purpose.

**Deferred From This FP:** Unrestricted direct messaging, public weight/calorie/body-measurement rankings, generic social graph, unmoderated groups, AI moderation as sole authority, a Facebook clone, and Voting & Balloting / official-result capability.

## FP-014 — Foundation programme, habits and reflective progress

**ID:** `FP-014`

**Name:** Foundation programme, habits and reflective progress

**Outcome:** Participants can enrol in a broader approved foundation programme, receive structured lessons/activities/habits, record private reflections and progress, recover after missed days and receive compassionate versioned completion/continuation outcomes.

**Validation Objective:** Extend the concrete Nuwe Jy programme evidence into a broader behaviour-change capability only where participant value and operational demand justify it; keep journals/private reflections separate from clinical and community authority.

**Validation Objective Type:** `PRODUCT`, `BEHAVIORAL`, `OPERATIONAL`, `PRIVACY`, `SAFETY`, `ARCHITECTURAL`, `PERFORMANCE`.

**Why Now:** Product Law places longer foundation programmes after the initial plan is validated. Nuwe Jy is the first concrete programme acceptance test; a broader programme is not an MVP prerequisite.

**Dependencies:** `FP-005`, `FP-006`, `FP-008` or equivalent approved programme proof; approved programme content, translations, completion and communication rules.

**Affected Domains:** `Programmes & Challenges`; `Habits, Journals & Progress`; `Content & Media`; `Entitlements`; `Plans & Nutrition`; `Safety & Eligibility`; `Communications`; `Community`; `Privacy & Consent`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§21F, 21H, 21L.7, 21L.11`; `DEC-010`, `DEC-158...DEC-169`, `DEC-196...DEC-219`.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 7–13, 15`; scheduled durable work, private data, content versions, deletion, pagination and analytics-minimisation themes.

**Major Gates:** `OQ-017` reminders; `OQ-018` journal encryption/retention; `OQ-019` programme metrics; `OQ-013` translations; `OQ-016` publication operations; `OQ-009`/`OQ-029` retention.

**Gate Classification:**

- `OQ-018 — BLOCKS_THIS_FP` for journal/attachment scope: private journal protection and deletion/export cannot be guessed.
- `OQ-019 — BLOCKS_THIS_FP`: each programme needs approved completion/participation rules before publication.
- `OQ-017` and `OQ-016 — BLOCKS_RELEASE_ONLY`: scheduled reminders/publication must be resolved for the promised delivery mode; programme modelling can be prepared earlier.
- `OQ-013 — BLOCKS_RELEASE_ONLY`: required bilingual programme content needs the approved translation/resource path.
- `OQ-009` and `OQ-029 — BLOCKS_RELEASE_ONLY`: retention categories are required before handling the broader record set in a pilot/release.

**Anticipated Architectural Proof:** `REUSE_EXISTING_PROOF` where the programme uses the same edition/release/consequence mechanism proven by FP-008; Phase 7 must split out a new tracer only for a materially different mechanism.

**Performance / Scaling Concern:** Scheduled release populations, habit/check-in writes, journal history, reminder fan-out and progress dashboards require bounded batch work and pagination. Journals are never cached generically; Redis/GenServer/replicas are not assumed.

**Security / Privacy / Safety Concern:** Journals are private by default; health-sensitive responses route to Safety/Health; missed days cannot erase history; deletion/export handles attachments and derivatives; programme participation never becomes clinical authority.

**Release Effect:** Longer foundation programme and durable habit/reflective progress capability.

**Exit Condition:** Approved programme version, translations, schedules, completion/recovery rules, journal privacy/retention, notifications, safety routing, support and deletion behaviour are tested and operationally owned.

**Deferred From This FP:** AI journal assistance, continuous wearable/CGM integrations, detailed calorie-tracking diary, unrestricted page builder, generic LMS and automatic clinical adjustment.

## FP-015 — Event commerce and scarce capacity

**ID:** `FP-015`

**Name:** Event commerce and scarce capacity

**Outcome:** A participant can browse an approved paid event, obtain an expiring capacity hold, pay, receive a ticket, transfer/check in/cancel/refund/credit under the accepted event policy, with zero confirmed oversell under concurrency and failure.

**Validation Objective:** Prove the scarce-inventory contract, not merely checkout UI: admission/rate limiting, hold expiry, payment/issuance reconciliation, retry/idempotency, waitlist behaviour, thundering-herd/cache-stampede resistance and zero oversell.

**Validation Objective Type:** `COMMERCIAL`, `ARCHITECTURAL`, `PERFORMANCE`, `RELIABILITY`, `SECURITY`, `OPERATIONAL`, `PRIVACY`.

**Why Now:** Events are an approved mature capability but explicitly later than live integration. Pulling scarce-capacity infrastructure into MVP would add risk without validating the core paid proposition.

**Dependencies:** `FP-002`, `FP-006`, `FP-007`; approved event policy, provider path and event operator.

**Affected Domains:** `Events & Live`; `Commerce`; `Entitlements`; `Identity & Access`; `Privacy & Consent`; `Communications`; `Content & Media`; `Audit & Evidence`; `Analytics`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§21G.17–21G.22, 21L.12`; `DEC-186...DEC-195`, `DEC-279`; event capacity/ticket rules.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§5, 7–10, 12–15`; `FLOW-09`; contention, transactional capacity, durable reconciliation, current access, edge/rate and performance-proof themes.

**Major Gates:** `OQ-022` event reservation architecture; `OQ-004` provider/payment behaviour; `OQ-035` abuse/rate thresholds; `OQ-020`/`OQ-021` where the event includes live/recorded delivery; `OQ-036` event communication policy.

**Gate Classification:**

- `OQ-022 — BLOCKS_THIS_FP`: locking/reservation/expiry/waitlist and flash-sale protection are the core outcome.
- `OQ-004 — BLOCKS_THIS_FP`: event payment and ticket issuance must reconcile with the provider path.
- `OQ-035 — BLOCKS_THIS_FP`: admission/rate/abuse behaviour is part of safe scarce-capacity operation.
- `OQ-020` and `OQ-021 — BLOCKS_RELEASE_ONLY`: only for live/recorded event variants; ordinary ticket commerce can be modelled separately.
- `OQ-014 — NON_BLOCKING_FOR_THIS_FP`: public event information may use ordinary safe delivery; advanced edge caching is not the capacity authority.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — mandatory FLOW-09 proof of zero confirmed oversell under multi-node contention, retries, expiry, provider ambiguity and failure.

**Performance / Scaling Concern:** This is the first deliberately high-concurrency scarce-inventory path. Later proof must cover admission/rate limiting, expiring holds, DB locks/contention, duplicate/retry storms, cache stampedes, backlog recovery and horizontal operation. No event infrastructure is built in MVP.

**Security / Privacy / Safety Concern:** Tickets, purchaser, holder and attendee remain separate; current event policy is accepted before checkout; provider state cannot manufacture ticket truth; attendance/replay privacy and deletion are governed.

**Release Effect:** Paid event catalogue and capacity-controlled ticket commerce.

**Exit Condition:** Under the approved proof envelope, confirmed allocations never exceed capacity; holds expire/release correctly; payment/ticket/retry/reconciliation paths are idempotent; waitlist and rollback/credit rules are observable and owned.

**Deferred From This FP:** Reserved seating unless separately approved, arbitrary flash-sale scale, generic ticketing platform, unbounded event bundles and infrastructure choices not supported by proof.

## FP-016 — First-party experimentation and learning

**ID:** `FP-016`

**Name:** First-party experimentation and learning

**Outcome:** Operators can run approved first-party A/B/n experiments on governed web/page and eligible message experiences with stable assignment, exposure evidence, protected-invariant exclusions, authoritative conversion/income reconciliation, privacy/deletion handling and durable auditable learning.

**Validation Objective:** Prove that product learning improves decisions without changing payment, entitlement, safety, consent, accessibility, security, accounting or clinical truth; distinguish assignment, exposure, outcome and decision evidence.

**Validation Objective Type:** `PRODUCT`, `ARCHITECTURAL`, `PRIVACY`, `SECURITY`, `OPERATIONAL`, `PERFORMANCE`, `RELIABILITY`.

**Why Now:** Pilot measurement and basic funnel evidence belong in FP-006. First-party experimentation is valuable only after there is a real decision surface and enough product learning need to justify its proof cost.

**Dependencies:** `FP-006`; a concrete approved experiment hypothesis and measurable governed surface; `FP-002`/`FP-009` only when commerce outcomes are the readout.

**Affected Domains:** `Experimentation`; `Analytics`; `Content & Media`; `Communications`; `Commerce`; `Identity & Access`; `Privacy & Consent`; `Audit & Evidence`.

**Product Authority:** `00_PLATFORM_v1.4.1.md §§21K.6A, 21L.13, 21L.23`; `DEC-293`; product learning and protected-invariant rules.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§7–10, 11, 13–15`; `FLOW-12`; assignment/exposure separation, canonical URLs, variant-safe delivery, OLTP isolation and immutable learning themes.

**Major Gates:** `OQ-040` experimentation proof; `OQ-014` if experiment-sensitive shared edge caching is proposed; `OQ-013`, `OQ-015`, `OQ-016`, `OQ-036` as affected surfaces; `OQ-030`/`OQ-032` for external measurement deletion/export.

**Gate Classification:**

- `OQ-040 — BLOCKS_THIS_FP`: assignment, exposure, measurement, statistical validity, privacy/deletion and failure/recovery proof are the pack's outcome.
- `OQ-014 — BLOCKS_RELEASE_ONLY`: only if shared edge caching is used for experiment-sensitive HTML; safe cache bypass is not blocked by the gate.
- `OQ-013`, `OQ-015`, `OQ-016`, `OQ-036 — NON_BLOCKING_FOR_THIS_FP`: each becomes blocking only when the selected experiment surface uses that content/search/publication/message mechanism.
- `OQ-030` and `OQ-032 — BLOCKS_RELEASE_ONLY`: external analytics/measurement processors need deletion/export inventory before a participant-facing experiment release.

**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — FLOW-12 identifies a materially unproven assignment/exposure/cache/statistical path; no feature-flag convenience choice is accepted as proof.

**Performance / Scaling Concern:** Assignment must stay bounded and stable; exposure volume and analytical rebuilds must not starve core OLTP. Start with PostgreSQL-first governed facts/projections and batch/streaming analytics; no warehouse, Redis assignment authority or specialist service is assumed without evidence.

**Security / Privacy / Safety Concern:** Raw health data is not a default assignment signal; variants cannot weaken safety/legal/accessibility/security/payment/entitlement invariants; canonical public URLs and cache isolation prevent treatment leakage; deletion removes identifiable exposure where required.

**Release Effect:** Evidence-backed product/content/commerce learning and governed optimisation of public or eligible message surfaces.

**Exit Condition:** Activated experiment versions are immutable; assignment is stable; exposure is real and deduplicated; authoritative outcomes reconcile; material sample-ratio mismatch blocks a decision; aggregate learning is auditable and privacy-safe.

**Deferred From This FP:** Dynamic pricing, unrestricted experimentation on protected flows, client-asserted conversion truth, AI-driven winner selection, generic feature-flag replacement and premature analytics infrastructure.

## FP-017 — Approved product-space or market expansion

**ID:** `FP-017`

**Name:** Approved product-space or market expansion

**Outcome:** A concrete, separately approved future product space or market can activate through the shared platform's identity, commerce, entitlement, content, safety, privacy, analytics and operational boundaries without exposing unfinished products or creating unrestricted generic tenancy.

**Future-gated capability boundary:** FP-017 does not automatically own Research & Feedback or Voting & Balloting. Those remain Feature-Pack-unassigned unless a concrete approved product-space/market direction explicitly requires them and a later governed Roadmap decision assigns them.

**Validation Objective:** Prove that an approved future expansion reuses enduring authority and can be activated/rolled back as a controlled product space or market. The pack is conditional and does not authorise a speculative second product.

**Validation Objective Type:** `PRODUCT`, `COMMERCIAL`, `ARCHITECTURAL`, `SECURITY`, `PRIVACY`, `OPERATIONAL`, `PERFORMANCE`.

**Why Now:** The mature platform preserves future men’s/specialist products and controlled market activation, but no concrete future launch direction is required for the first paid route. This pack remains last and trigger-based.

**Dependencies:** `FP-006`; the relevant proven shared capabilities; a new explicit Product Law/commercial/legal/clinical direction identifying the product space or market; no generic-tenancy assumption.

**Affected Domains:** `Identity & Access`; `Privacy & Consent`; `Commerce`; `Entitlements`; `Temperament`; `Health Records`; `Safety & Eligibility`; `Plans & Nutrition`; `Content & Media`; `Programmes & Challenges`; `Habits, Journals & Progress`; `Community`; `Events & Live`; `Professional Care`; `Communications`; `Experimentation`; `Analytics`; `Audit & Evidence`.

**Product Authority:** `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md §§6–7, 19`; `00_PLATFORM_v1.4.1.md §§21L.1–21L.3`; `DEC-005`, `DEC-268...DEC-270`; future product-space and market activation boundaries.

**Architecture Authority:** `03_ARCHITECTURE_v1.1.1.md §§3, 5–15`; controlled product spaces, replaceable application topology, current authority, privacy, provider and evidence-gated scaling themes.

**Major Gates:** New approved Product Law direction; operating/IP/legal/consumer authority; relevant clinical, translation, payment, retention, provider, security and performance gates; `OQ-001`, `OQ-009`, `OQ-029`, `OQ-030`, `OQ-033`, `OQ-037`, `OQ-039` as applicable.

**Gate Classification:**

- Concrete product/market approval — `BLOCKS_THIS_FP`: without a real approved outcome there is no lawful scope to build.
- Market legal/payment/privacy/safety review — `BLOCKS_THIS_FP`: a successful foreign payment or shared code path cannot authorise a market.
- Existing core gates — `NON_BLOCKING_FOR_THIS_FP` only where the shared mechanism is already proven and the new activation does not change its protected invariant; affected gates re-open at the relevant release boundary.
- Generic multi-tenant/corporate platform work — `FUTURE_ONLY`: it is not an approved expansion path merely because product spaces exist.

**Anticipated Architectural Proof:** `DECIDE_IN_PHASE_7` — the concrete future product/market determines whether shared proof is sufficient or a new product-space/market tracer is warranted.

**Performance / Scaling Concern:** Expansion must identify its workload, data temperature, concurrency and shared-resource impact before activation. No 100k-user provisioning, service split, replica, cache or tenancy isolation is pulled forward without an approved workload and evidence.

**Security / Privacy / Safety Concern:** Product-space visibility, identity roles, content, health/safety rules, consent, deletion, practitioner access and market-specific urgent support are independently reviewed; unfinished navigation remains invisible.

**Release Effect:** A deliberately approved future product-space or market activation; not a current launch dependency.

**Exit Condition:** The concrete expansion has approved law, affected Domain/JIT detail, gate manifest, proof/release evidence, rollback and operational ownership; shared platform truth remains single and auditable.

**Deferred From This FP:** Generic multi-tenant SaaS, corporate dashboards, unrestricted partner tenancy, future men’s implementation without an approved launch decision, true multi-currency without market activation and any unapproved specialist product.

---

# 7. MVP / FIRST-PAID CRITICAL PATH

The shortest safe route to the first participant completing the approved paid core journey is:

```text
FP-001
→ FP-002
→ FP-003
→ FP-004
→ FP-005
→ FP-006
```

This path explicitly covers:

```text
discover / public bilingual experience
→ account / verified identity / required Platform Member Reference
→ purchase / checkout / payment verification
→ exactly one entitlement
→ temperament provenance / assessment
→ immutable result / report
→ health / safety onboarding
→ eligibility
→ eligible personalised 7-day plan
   OR governed General Wellness fallback
→ purchased report / plan library access
→ light progress / feedback
→ controlled operational/admin/support capability
→ staged paid-pilot evidence
```

`FP-006` is not an optional technical afterthought. It is the release boundary that makes the preceding participant behaviour safe to sell. No Feature Pack for Nuwe Jy, Membership, Premium, practitioner review, native community, event commerce or experimentation is a prerequisite for this path.

## 7.1 First-paid gate chain

| Critical-path point | Required packs | Material gates before the next protected behaviour |
|---|---|---|
| Verified account + required PMR | `FP-001` | `OQ-035` and `OQ-036` before protected public/pilot release; PMR encoding remains downstream (`ARQ-IAM-013`). |
| Paid access | `FP-002` | `OQ-004`; `OQ-035`; `OQ-001` before production payment/sensitive processing. |
| Assessment/report | `FP-003` | Approved methodology/content/rights; `OQ-013` for governed bilingual delivery; `OQ-006` only if optional labels are enabled. |
| Safety outcome | `FP-004` | `OQ-005`, `OQ-008`; applicable retention approval; `OQ-007` only if lab inputs are included. |
| Plan/library/feedback | `FP-005` | `OQ-010`, `OQ-013`, publication/correction operations; current Safety and Entitlement authority. |
| First real paid participant | `FP-006` | Cross-functional paid-pilot readiness; `OQ-009`, `OQ-029...OQ-032`, `OQ-035...OQ-038`, operating/IP/terms/privacy authority and all Product Law no-go conditions. |

---

# 8. Pilot progression

The Product Law pilot progression is:

```text
internal validation
→ first 10 real paid participants
→ review
→ expand toward 25
→ review
→ maximum 50 in the first paid pilot
→ review
→ limited public release
→ general public release
```

The first 50 is an operating release boundary, not a database capacity limit. The next controlled cohort may expand toward approximately 100–250 after successful evidence, as already permitted by Product Law; no new numeric gate is invented here.

| Stage | Prerequisite packs | Required evidence/gates |
|---|---|---|
| Internal validation | `FP-001...FP-006` in safe internal mode | End-to-end core journey; reproducible results/plans; correction/withdrawal; support; critical telemetry; no production sale. |
| First 10 paid | `FP-001...FP-006` | Product Law cross-functional sign-off; operating authority sufficient; payment/entitlement/idempotency; safety/clinical/content/translation; privacy/security; support/restore/deletion readiness. |
| Review before 25 | Same packs | Evidence review by responsible product/commercial, clinical/safety and technical/operations authorities; no unresolved critical stop condition. |
| Toward 25 | Same packs | Controlled expansion under existing rollback/stop authority; support and queue/capacity evidence remains manageable. |
| Review before 50 | Same packs | Repeat safety/payment/entitlement/generation/support/privacy review; no automatic expansion from technical capacity alone. |
| Maximum 50 first pilot | Same packs | Product Law first-pilot cap; integrity criteria and operational/product/value targets recorded. |
| Limited public | `FP-001...FP-006` plus approved release decision | Product/clinical/technical authorities separately sign; public content/product visibility and support/incident ownership ready. |
| General public | `FP-001...FP-006` plus successful limited-public evidence | Go/no-go evidence, rollback/re-entry criteria and next-cohort decision; future branch packs remain independent. |

---

# 9. Nuwe Jy path

```text
FP-001...FP-006 core paid foundation
→ FP-007 governed live/replay
→ FP-008 first native Nuwe Jy edition
→ later FP-013 / FP-014 where community and broader programme evidence justifies them
```

Nuwe Jy is the first native flagship expansion after the paid core MVP is proven and hardened. It uses the central Temperament, Safety, Plans, Entitlements, Content, Progress, Communications, Community and Events/Live owners. It does not create a Nuwe Jy domain, nutrition engine, importer or parallel entitlement system.

The native edition cannot activate until its core platform, programme, operations, safety, live/community and technical gates pass, including source inventory, all 60 days, translations, scheduled release, support/facilitation/moderation/live ownership, safety/completion rules, communication configuration and recovery evidence.

The early cohort community may use the governed Facebook path while first-party Community remains deferred to FP-013. This preserves the approved validation sequence and prevents external Facebook state from becoming platform business truth.

---

# 10. Membership / Adjustment / Premium path

## 10.1 Basic Membership

```text
FP-001...FP-006
→ FP-007 governed live/replay
→ FP-009 Basic Membership
```

Basic Membership is a sibling branch to Nuwe Jy, not a prerequisite for it. It may launch before or alongside early Nuwe Jy only if its own minimum recurring value is operational: moderated community, approved monthly content, monthly live, group Q&A, correct entitlement and cancellation lifecycle.

## 10.2 Adjustment and Premium

```text
FP-001...FP-006
→ FP-010 recurring review and governed adjustment
→ FP-011 Premium bundle
```

If Premium is packaged on the recurring membership contract, `FP-009` also precedes `FP-011`:

```text
FP-009 + FP-010
→ FP-011
```

The plan-adjustment capability must be useful and safe before it becomes a named commercial promise. Premium reuses the single Commerce/Entitlements model, carries no unlimited practitioner promise and does not alter the safety authority boundary.

---

# 11. Practitioner path

```text
FP-001...FP-006
→ FP-012 controlled practitioner review pilot
```

Practitioner review is introduced only after automated plan delivery is stable. It requires an explicitly priced, capacity-controlled service, authorised practitioner(s), consent, active relationship, scoped/expiring access, structured outcomes, approved record authority, expected turnaround, follow-up/referral handling and a hard stop before saleable capacity is exceeded.

The first practitioner pack is a pilot, not a marketplace. Practitioner role does not itself grant participant-record access; Professional Care invokes Health, Safety and Plans owners rather than becoming their authority.

---

# 12. Community / Live / Events path

## 12.1 Community

```text
FP-008 / FP-009 governed external community evidence
→ FP-013 first-party community + governed challenges
```

Facebook remains the early validation channel under governed operating/privacy/moderation policy. First-party community enters only when evidence shows the platform needs native groups, moderation, reporting, sanctions, appeals, privacy controls or challenge integration.

## 12.2 Live sessions

```text
FP-006
→ FP-007 governed live sessions and replay
→ reused by FP-008 Nuwe Jy, FP-009 Basic Membership and FP-015 events
```

Live is intentionally earlier than full event commerce because it provides approved recurring/flagship value without scarce ticket inventory. Provider failure may reduce availability/freshness but cannot create or revoke platform entitlement truth.

## 12.3 Event commerce

```text
FP-002 + FP-006 + FP-007
→ FP-015 event commerce and scarce capacity
```

FP-015 is the only current Roadmap pack that owns the future flash-sale/event proof boundary. It must prove admission/rate limiting, expiring holds, zero confirmed oversell, retry/idempotency, waitlist allocation, thundering-herd/cache-stampede behaviour and multi-node contention before public event commerce.

---

# 13. Experimentation / learning path

```text
FP-006 minimum governed pilot measurement
→ concrete product learning need
→ FP-016 first-party experimentation
```

FP-006 may measure the core funnel and pilot outcomes using Analytics without first-party A/B/n. FP-016 is activated only for a real approved decision surface. It must preserve clean/canonical URLs, stable assignment, separate exposure/outcome evidence, authoritative downstream conversion, privacy/deletion rules and protected invariants.

Experimentation is decision support, never payment, entitlement, safety, consent or accounting truth. A material unexplained sample-ratio mismatch blocks a decision rather than being hidden by a convenient aggregate.

---

# 14. Gate schedule

The schedule resolves a gate when the first dependent outcome would otherwise require guessing. It does not resolve every gate before Roadmap freeze.

| Gate | Affected Feature Pack(s) | Earliest point it must be resolved | What it blocks | Why it does not block earlier work |
|---|---|---|---|---|
| `OQ-001` Final operating entity | `FP-006`, `FP-009`, `FP-011`, `FP-012`, `FP-014`, `FP-015`, `FP-017` | Before production subscriptions, large-scale sensitive processing, practitioner contracting or relevant activation | Production paid pilot/release and practitioner/subscription activation | It does not block safe internal planning or non-production core path preparation. |
| `OQ-002` Exact launch pricing | `FP-002` (resolved MVP prices), `FP-009`, `FP-011` | Future membership/Premium commercial review | Future public membership/Premium price release | MVP prices are already locked as versioned configuration; the Basic anchor remains provisional until its own review. |
| `OQ-003` Monthly review contract | `FP-010`, `FP-011` | Before recurring adjustment is enabled | Adjustment and Premium review promise | Once-off MVP deliberately has no automatic monthly adjustment. |
| `OQ-004` Paystack retry/subscription/refund behaviour | `FP-002`, `FP-009`, `FP-011`, `FP-015` | Before the first payment/entitlement implementation is accepted; recurring/event variants before those variants | Provider reconciliation, recurring billing and event payment/ticket paths | Later recurring/event semantics are not required for once-off product modelling, but once-off provider behaviour is. |
| `OQ-005` Clinical eligibility matrix | `FP-004`, `FP-005`, `FP-008`, `FP-010`, `FP-012` | Before automated plan/safety release | Automated eligibility, plan generation, Nuwe Jy routing and adjusted/practitioner pathways | It does not block public discovery, identity, or safe non-clinical commerce preparation. |
| `OQ-006` Score-distance thresholds | `FP-003` only if optional labels are enabled | Before the gated result labels are released | Dominance/close/balanced/mixed labels | Core launch scoring and report can proceed without optional labels. |
| `OQ-007` Laboratory validity matrix | `FP-004`, later `FP-012`/`FP-017` if lab inputs are approved | Before lab-derived facts influence current eligibility or care | Laboratory-enabled safety/care decisions | MVP excludes laboratory integration; ordinary intake is not blocked. |
| `OQ-008` Emergency and urgent-support wording | `FP-004`, `FP-005`, `FP-008`, `FP-012` | Before any participant-facing urgent-safety outcome | Urgent messaging and safe release | It does not block public content/account work that contains no clinical decision. |
| `OQ-009` Early retention categories | `FP-006`, `FP-012`, `FP-014`, `FP-017` | Before pilot/release of health/professional/journal records | Paid pilot readiness and later sensitive capabilities | Internal modelling can use no production sensitive data and cannot invent retention durations. |
| `OQ-010` Calculation values | `FP-005`, `FP-010` | Before plan generation release; again if adjustment changes formulas | Safe initial/adjusted plan output | Assessment, identity, commerce and eligibility work do not require formula values. |
| `OQ-011` Adjustment thresholds | `FP-010`, `FP-011` | Before recurring review/adjustment | Adjustment and Premium | Explicitly excluded from once-off MVP. |
| `OQ-012` Review timing | `FP-010`, `FP-011` | With the adjustment contract before release | Monthly review/grace behaviour | No recurring review is promised in FP-005. |
| `OQ-013` Translation resource design | `FP-003`, `FP-005`, `FP-008`, `FP-009`, `FP-014`, `FP-016` as surfaces require | Before governed paid/safety/programme content is released | Locale/version-safe paid, safety and programme delivery | Public/account scaffolding and non-content planning can proceed; exact Resource design stays downstream. |
| `OQ-014` Cloudflare/edge-cache design | `FP-005`, `FP-007`, `FP-013`, `FP-016` only where shared caching is used | Before the affected public/protected/experiment-sensitive cache path | Safe cache delivery/invalidation | MVP can use safe non-shared delivery; cache is never authority. |
| `OQ-015` Search configuration | Later public content/search surface, chiefly `FP-014`, `FP-016`, `FP-017` | When search is an approved product outcome | Search ranking/index/pagination path | MVP has a small approved content library and no required search feature. |
| `OQ-016` Content publication operations | `FP-005`, `FP-008`, `FP-009`, `FP-014` | Before paid/safety/programme/monthly content is activated | Publication, correction, withdrawal and scheduler reliability | Content can be planned and authored before exact publication operations are fixed. |
| `OQ-017` Reminder delivery design | `FP-008`, `FP-009`, `FP-013`, `FP-014` | Before reminders or scheduled notification promises | Reminder scheduling, quiet hours, retries and rate limits | Basic MVP feedback does not require reminders. |
| `OQ-018` Journal encryption and retention | `FP-013`, `FP-014` | Before private journals/attachments are stored | Journal privacy/export/deletion and professional handling | MVP progress/feedback can remain lightweight and separate from journals. |
| `OQ-019` Programme completion metrics | `FP-008`, `FP-013`, `FP-014` | Before each programme/challenge edition is published | Completion, recognition and challenge outcomes | No programme/challenge is in MVP. |
| `OQ-020` Restream/Cloudflare live validation | `FP-007`, `FP-008`, `FP-009`, `FP-015` as live variants require | Before governed live/replay production use | Live transport, recording/input and provider recovery | Full live path is later than core paid MVP. |
| `OQ-021` Video consent and retention | `FP-007`, `FP-008`, `FP-015` | Before recording/replay/clip delivery | Recording, replay, withdrawal and retention | No live/recording capability is needed for MVP. |
| `OQ-022` Event reservation architecture | `FP-015` | Before any scarce paid capacity path | Holds, expiry, zero oversell, waitlist and flash-sale proof | Live registration without scarce paid inventory is FP-007 and does not need event holds. |
| `OQ-023` Facebook community operating policy | `FP-008`, `FP-009`, `FP-013` | Before governed external cohort/member community use; revalidated for migration | Moderation, privacy, disclosure and escalation | Community is excluded from MVP. |
| `OQ-024` Nuwe Jy source-content inventory | `FP-008` | Before native edition activation | Rights, missing content/translations/media and edition readiness | Nuwe Jy is a later flagship, not core MVP. |
| `OQ-025` Nuwe Jy safety/completion thresholds | `FP-008` | Before edition activation | Challenge routing, milestone and completion rules | Core MVP uses its own approved safety/plan rules. |
| `OQ-026` Nuwe Jy edition operations | `FP-008` | Before edition activation/sale | Cohort, facilitator, moderator, support and live capacity | No cohort is sold in MVP. |
| `OQ-027` Nuwe Jy communication channels | `FP-008` | Before scheduled edition communications | Channels, caps, quiet hours, retries and ownership | Core MVP does not promise Nuwe Jy communication journeys. |
| `OQ-028` LearnDash retirement obligations | `FP-008` | Before native Nuwe Jy cutover/activation | Legacy promises, records, access and retirement conditions | It does not block a new core path that is explicitly not a LearnDash migration. |
| `OQ-029` Retention schedule matrix | `FP-006`, `FP-012`, `FP-014`, `FP-017` | Before affected paid pilot/sensitive release | Category-specific retention, deletion and legal exceptions | Roadmap does not invent durations; non-production work can proceed without them. |
| `OQ-030` External processor deletion inventory | `FP-006`, `FP-016`, `FP-017` and any processor-using branch | Before pilot/release with those processors | Deletion/export/reconciliation across payment, messaging, analytics, storage/video | Processor inventory is not needed to sequence the core outcome, but is release-blocking when used. |
| `OQ-031` Backup restore/deletion replay | `FP-006`, later `FP-008`, `FP-014`, `FP-017` | Before first paid pilot and any new sensitive release tier | Non-resurrection, restore isolation and recovery promotion | It does not block document planning; it blocks live release readiness. |
| `OQ-032` Export/deletion operations | `FP-006`, `FP-012`, `FP-014`, `FP-016`, `FP-017` | Before participant data is processed in the affected release | Verified export/deletion operations and completion evidence | Exact operational deadlines are downstream; no participant release occurs without them. |
| `OQ-033` Professional record authority | `FP-012` | Before practitioner cases are sold | Record authority, access, addendum, retention and disposition | Automated MVP can route to review without activating practitioner service. |
| `OQ-034` Resolved authentication architecture selection / executable proof | `FP-001` | Architecture selection resolved; proof required in Phase 8 before implementation acceptance | Auth, MFA/recovery/trusted-device/step-up executable proof | Proof remains incomplete and classification is not finalised. |
| `OQ-035` Abuse-control thresholds | `FP-001`, `FP-002`, `FP-006`, `FP-009`, `FP-013`, `FP-015` | Before protected public/pilot release; before high-concurrency/event/community activation | Layered rate limits, escalation and false-positive recovery | Exact thresholds are not needed to write outcome-level sequencing; they are release/proof gates. |
| `OQ-036` Notification providers/channel policy | `FP-001`, `FP-006`, `FP-007...FP-009`, `FP-013...FP-016` | Before the affected email/in-app/notification promise | Provider, consent, retry, delivery evidence and failure ownership | Future channels do not block account/payment/plan modelling; each promised channel is gated at use. |
| `OQ-037` RPO/RTO targets | `FP-006`, later every materially higher release tier | Before paid pilot/recovery promotion | Class-specific recovery and restore evidence | Architecture already provides recovery doctrine; exact targets belong to the affected release. |
| `OQ-038` Incident response ownership | `FP-006`, later all public/paid expansion packs | Before first paid pilot | Named incident command, escalation and after-hours handling | Planning and safe internal work can proceed; customer-facing release cannot. |
| `OQ-039` Performance/scaling domain mapping | All packs at Phase 7 for affected actions; Phase-5 profiles already complete | Before affected implementation slice and executable proof | Index/cache/async/concurrency/100k mapping for the selected slice | The Roadmap must not invent implementation detail; future untouched Domains/actions do not block this Roadmap. |
| `OQ-040` First-party experimentation proof | `FP-016` | Before first governed A/B/n activation | Assignment/exposure/statistics/cache/privacy/learning validity | Core pilot measurement does not require experimentation. |

## 14.1 Non-OQ expert/vendor gates

| Gate family | Earliest relevant pack | Classification and reason |
|---|---|---|
| Operating entity, IP/licence/model/book/translation/contributor rights, terms/privacy/consumer wording | `FP-002...FP-006`, then each product branch | `BLOCKS_RELEASE_ONLY` for internal preparation; `BLOCKS_THIS_FP` when the affected paid/sensitive product is sold. The Roadmap records the gate and does not solve it. |
| Clinical authority, approved formulas, safety wording, pregnancy/medication/supplement rules | `FP-004...FP-005`; again for `FP-008`, `FP-010`, `FP-012` | `BLOCKS_THIS_FP` whenever the behaviour would make a new clinical/safety decision. Future clinical rules are `FUTURE_ONLY`. |
| Practitioner agreements and professional capacity | `FP-012` | `BLOCKS_THIS_FP`; no practitioner promise exists earlier. |
| Sponsor/partner agreements, book-linked or gift/sponsored commercial rules | Concrete commerce extension after `FP-006`, likely `FP-017` | `FUTURE_ONLY` unless a specific approved launch bundle activates them; no generic grant system is pulled into MVP beyond governed explicit grants. |
| Nuwe Jy staffing, facilitation, moderation and source/media rights | `FP-008` | `BLOCKS_THIS_FP`; no Nuwe Jy edition is activated without them. |
| Restream/Cloudflare plan, notification vendor and external processor contracts | `FP-007...FP-009`, `FP-016` as used | `BLOCKS_THIS_FP`/`BLOCKS_RELEASE_ONLY` for the affected provider path; not a core MVP prerequisite. |

---

# 15. Anticipated Architectural Proof map

| Feature Pack | Material architectural claim/path | Likely proof status | Why |
|---|---|---|---|
| `FP-001` | Canonical identity, verification, session, recovery, policy and abuse boundary | `PROBABLY_NEW_TRACER_BULLET` | FLOW-01 is coherent but no executable authentication path has yet proven the implementation boundary. |
| `FP-002` | Provider evidence → Commerce truth → durable Entitlement effect | `PROBABLY_NEW_TRACER_BULLET` | FLOW-02 preserves the cross-domain/reconciliation claim; duplicate and ambiguous provider effects need real proof. |
| `FP-003` | Entitled assessment attempt → deterministic scoring → immutable report/provenance | `DECIDE_IN_PHASE_7` | FLOW-03 passes; a separate tracer is only needed if report/scoring complexity is materially distinct. |
| `FP-004` | Health facts → current Safety authority → fail-closed eligibility | `PROBABLY_NEW_TRACER_BULLET` | Safety correctness cannot be inferred from a form or from plan proof. |
| `FP-005` | Eligibility → deterministic plan → immutable snapshot → protected delivery and feedback | `PROBABLY_NEW_TRACER_BULLET` | Plan generation, content fan-in, safe replacement and reproducibility are an enduring path. |
| `FP-006` | Reuse of core authority, async, audit, deletion, observability and release controls | `REUSE_EXISTING_PROOF` | It is the operational/release evidence boundary; it must harden existing paths rather than invent a technical layer. |
| `FP-007` | Live provider/playback/replay through current access and governed consent | `PROBABLY_NEW_TRACER_BULLET` | External live/media evidence and protected playback are materially new. |
| `FP-008` | Scheduled cohort release, recovery, fan-out, notifications, progress and live/community composition | `PROBABLY_NEW_TRACER_BULLET` | FLOW-07 identifies a real durable scheduling/fan-out path. |
| `FP-009` | Recurring billing, cancellation/grace, monthly value and component entitlements | `PROBABLY_NEW_TRACER_BULLET` | Recurring provider semantics are not proven by once-off checkout. |
| `FP-010` | Trend/check-in review → safety re-evaluation → immutable adjusted plan | `PROBABLY_NEW_TRACER_BULLET` | New schedule/trend/plan-version interaction; may reuse generation proof if identical. |
| `FP-011` | Premium composition over existing Commerce/Entitlements/adjustment truth | `REUSE_EXISTING_PROOF` | Product Law explicitly forbids a parallel entitlement architecture. |
| `FP-012` | Consent + active professional relationship + scoped record access + downstream Safety/Plan command | `PROBABLY_NEW_TRACER_BULLET` | FLOW-10 is coherent but professional access is high-sensitivity and unproven. |
| `FP-013` | First-party feed, moderation, safe challenge, deletion and current access | `PROBABLY_NEW_TRACER_BULLET` | Native community is a new concurrency, privacy and moderation path. |
| `FP-014` | Reusable programme/release/habit/journal path beyond Nuwe Jy | `REUSE_EXISTING_PROOF` subject to Phase 7 | Nuwe Jy is intentionally the concrete programme acceptance test; new proof only if mechanisms diverge. |
| `FP-015` | Scarce holds/payment/ticket issue with zero confirmed oversell | `PROBABLY_NEW_TRACER_BULLET` | FLOW-09 requires adversarial multi-node/contention proof. |
| `FP-016` | Assignment → exposure → authoritative outcome → immutable decision/learning | `PROBABLY_NEW_TRACER_BULLET` | FLOW-12 and OQ-040 identify a materially unproven path. |
| `FP-017` | Controlled product-space/market activation reusing shared authority | `DECIDE_IN_PHASE_7` | No concrete future activation exists yet; proof depends on its approved scope and workload. |

No Tracer Bullet is created by this Roadmap. Final proof classification belongs to Phase 7.

---

# 16. Deferred capability map

| Approved or possible mature capability | Roadmap home / trigger | Deliberate deferral |
|---|---|---|
| Native first-party community | `FP-013` after Nuwe Jy/Membership evidence | No MVP community or generic social graph. |
| Governed challenges | `FP-013`, using `Programmes & Challenges` and `Habits, Journals & Progress` | No challenge catalogue, badges or public competition in MVP. |
| Foundation programme | `FP-014` after Nuwe Jy/programme proof | No generic LMS or broad programme build before a concrete acceptance test. |
| Private journals and richer reflective practice | `FP-014`, gated by `OQ-018` | Basic progress/feedback does not become a journal system by accident. |
| Automatic recurring adjustment | `FP-010`, gated by `OQ-003`, `OQ-011`, `OQ-012` | Explicitly excluded from the once-off MVP. |
| Basic Membership | `FP-009`, after recurring value | No membership sale on future promises. |
| Premium | `FP-011`, after Basic/adjustment as applicable | No Premium bundle or parallel entitlement path early. |
| Practitioner-reviewed service | `FP-012` | Limited capacity-controlled pilot only; no marketplace. |
| Live sessions/replay | `FP-007` | Early governed live is allowed; full event commerce waits for FP-015. |
| Paid event commerce/ticketing | `FP-015`, gated by `OQ-022` and adversarial proof | No scarce-capacity infrastructure in MVP. |
| First-party A/B/n experimentation | `FP-016`, gated by `OQ-040` | Pilot analytics remains sufficient until a real learning decision justifies proof cost. |
| Search, semantic search and richer discovery | Later content/learning surface, likely `FP-014`, `FP-016` or `FP-017` | Small MVP content set does not require speculative search infrastructure. |
| Content publication, advanced edge/cache and media derivatives | `FP-005`, `FP-007`, `FP-008`, `FP-014` only as used | Exact cache/resource/scheduler choices remain OQ/JIT/proof work. |
| Gifts, sponsorships, book-linked access and event-linked bundles | Concrete Commerce extension after core, likely `FP-017` or a separately justified pack | Explicit grants and small bundle model are reused; no broad grant catalogue is prebuilt. |
| Laboratory records, document assets, wearables and other health integrations | Concrete approved health/product direction after core, likely `FP-012` or `FP-017` | No clinical/data-integration infrastructure without a real approved need and gate. |
| AI journal assistance or AI-generated plans/translations | No current Feature Pack; only after a new approved direction and safety/privacy review | Product Law explicitly excludes independent diagnosis/prescription/unapproved plans and MVP AI generation. |
| Future men’s or specialist product space | Conditional `FP-017` | No unfinished navigation, generic tenancy or shared product assumptions exposed. |
| International markets / true multi-currency | Conditional `FP-017` | Foreign-card success alone cannot activate a market. |
| Native mobile apps, household accounts, corporate dashboards, unrestricted multi-tenant SaaS | No approved current Roadmap pack | Explicit MVP/product exclusions or absent approved direction; do not convert them into prerequisites. |

---

# 17. Performance and scaling review

This is a Roadmap-level review. Exact indexes, Redis structures/keys, TTLs, workers, topics, pool sizes, replica topology and concurrency numbers remain Phase 7/JIT/Architectural Proof/Hardening work.

| Feature Pack(s) | Broad data temperature | Concurrency / pressure | Roadmap decision |
|---|---|---|---|
| `FP-001` | Durable identity/session/security history; current session/policy reads hot/warm | Login/recovery bursts, password hashing, verification backlog | PostgreSQL authority and durable delivery first; distributed abuse state only where required; no node-local authority. |
| `FP-002` | Durable cold financial/payment/access history; current product/entitlement reads hot | Checkout/provider callback bursts, duplicate/retry storms, DB/worker contention | Short authoritative transitions + durable reconciliation; no event-style holds, replicas or cache authority. |
| `FP-003` | Cold immutable attempts/results/reports; active methodology may be warm | Assessment completion/report bursts | Bounded scoring and paginated history; no Redis/GenServer needed by default. |
| `FP-004` | Cold sensitive health history; narrow current safety state warm | Onboarding bursts and concurrent corrections | Never duplicate raw health data into generic acceleration; current Safety authority wins; no unsafe cache. |
| `FP-005` | Cold immutable plan snapshots/content versions; current plan/access hot | Generation bursts, content fan-in, feedback writes | Bounded generation, durable async where required, pagination; no eager full history or premature replicas. |
| `FP-006` | Mixed operational evidence and durable source truth | Pilot load, queue/provider failures, support/admin queries | Progressive 10→25→50 evidence; measure shared DB/worker/queue budgets; no 100k load gate for first 10. |
| `FP-007` | Durable session/registration/replay metadata; media bytes external | Live fan-out, reconnect, playback/provider capacity | Provider/edge delivery and narrow realtime observation; no scarce inventory or Redis admission path. |
| `FP-008...FP-009` | Warm current access/cohort/member state; cold content/history | Cohort release fan-out, monthly billing/content, community/live bursts | Durable scheduled work, bounded batches, pagination and current entitlement checks; add acceleration only from evidence. |
| `FP-010...FP-014` | Cold trend/journal/history; warm today/review/progress projections | Monthly review, habits/check-ins, feed/moderation and reminder fan-out | Stream/batch histories, protect private data, isolate analytics; no generic cache/GenServer by default. |
| `FP-015` | Durable event/ticket truth; hot temporary hold/capacity state | Highest planned contention: flash-sale, holds, payment/retry, waitlist | Mandatory adversarial proof before release: admission/rate, expiring holds, zero oversell, stampede, multi-node and recovery. |
| `FP-016` | Durable experiment config/decisions; derived analytical facts/aggregates | Assignment/exposure volume, concurrent experiments, analytics rebuild | Analytics is derived and rebuildable; protect OLTP; no warehouse/specialist store without measured need. |
| `FP-017` | Depends on concrete future space/market | Shared resource pressure and cross-product policy | Map workload before activation; no generic multi-tenant or scale infrastructure in advance. |

Across all packs:

- PostgreSQL remains the default structured authority.
- Oban is used for durable consequences only where the outcome requires must-not-lose work; it is not a business domain.
- PubSub is optional freshness/observation, never payment, safety, entitlement, capacity or completion truth.
- Redis/ETS/GenServer/replicas are not pulled forward without a concrete workload, authority boundary, failure mode and evidence.
- Streaming/pagination is preferred for histories, feeds, queues, exports, analytics and cohort/admin views.
- Multi-node proof is attached to the first affected path and release stage; it is not a blanket MVP prerequisite.

---

# 18. Security, privacy and safety review

| Protected behaviour | Roadmap placement | Non-deferrable condition |
|---|---|---|
| Identity/session/recovery | `FP-001` | Current server authority, verification, scoped roles, revocation, abuse controls and minimum data before protected release. |
| Payment/access | `FP-002` | Verified provider evidence, Commerce/Entitlements separation, idempotency, purchaser separation and current access checks. |
| Assessment/report | `FP-003` | Immutable provenance, private answers/results, approved methodology/content and deletion/retention contract. |
| Health/eligibility/plan | `FP-004`/`FP-005` | Clinical approval, fail-closed routing, urgent wording, current safety recheck, no partial plan, plan provenance and scoped health access. |
| Pilot operation | `FP-006` | Staff/practitioner MFA where relevant, audit, correction/withdrawal, deletion/export, restore, incident and safety-stop authority. |
| Live/replay | `FP-007`/`FP-008` | Current entitlement, recording/consent/retention, protected playback, provider minimisation and failure visibility. |
| Membership/community | `FP-009`/`FP-013` | Moderation, disclosure warnings, private health boundary, consent, deletion/anonymisation, sanctions/appeals and cancellation correctness. |
| Adjustment | `FP-010`/`FP-011` | Approved thresholds/timing, safety suspension, immutable versions, no silent clinical escalation or unlimited practitioner promise. |
| Professional care | `FP-012` | Consent + relationship + scope + expiry + audit, professional MFA, record authority and capacity stop. |
| Journals/programmes | `FP-014` | Journal privacy/encryption/retention, safety routing, compassionate progress and representation-complete deletion. |
| Events | `FP-015` | Event policy, purchaser/holder/attendee separation, zero oversell, capacity/ticket truth and safe payment reconciliation. |
| Experiments | `FP-016` | Protected-invariant exclusions, variant-safe URL/cache, privacy/deletion, authoritative outcomes and SRM validity blocker. |
| Future spaces/markets | `FP-017` | Explicit product/legal/clinical/market approval, controlled visibility, no generic tenant assumptions and release rollback. |

No pack may defer a control until after the participant behaviour that creates the risk. A lower-level task must stop and route a missing policy to Product, Architecture, Domain Law or the named gate rather than inventing it.

---

# 19. Anti-overengineering and development-friction review

The Roadmap was challenged against the requested ten questions.

| Question | Finding | Classification |
|---|---|---|
| Are there too many Feature Packs? | Seventeen packs cover the core plus the explicitly approved expansion branches. The packs are not one per Domain/page; each has a distinct outcome or evidence boundary. Conditional FP-017 is retained only to make future product-space activation visible, not to start work. | `EDITORIAL` / accepted after review |
| Could adjacent packs be merged? | Assessment, safety/eligibility, plan delivery, live/replay, adjustment, practitioner and event/experiment proof boundaries would lose meaningful gates if merged. No merge is required. | `ROADMAP_GAP` resolved in draft design |
| Is any pack only a technical layer? | FP-006 is operational/release capability; FP-007 is participant live/replay value; FP-016 is decision-making capability. No pack is a table, Domain or framework layer. | `EDITORIAL` pass |
| Is infrastructure scheduled before need? | No Redis, replicas, GenServers, microservices, generic LMS, full event holds, native community or specialist search is an MVP prerequisite. | `EDITORIAL` pass |
| Is a future product contaminating MVP? | Nuwe Jy, Basic, Premium, practitioner, community, live, events and experimentation are downstream of FP-006; live is an explicit later shared outcome, not core contamination. | `ROADMAP_GAP` resolved by explicit branch graph |
| Is a Tracer Bullet demanded where proof can be reused? | FP-006, FP-011 and FP-014 explicitly reuse existing proof where the enduring mechanism is the same; provisional new-proof flags are limited to materially new paths. | `DOWNSTREAM_DETAIL` final authority remains Phase 7 |
| Are gates resolved too early? | Future OQs are scheduled at the first affected pack. OQ-006, OQ-007, OQ-011, OQ-012, OQ-017, OQ-018, OQ-019, OQ-022 and OQ-040 do not block MVP. | `EDITORIAL` pass |
| Are full Domain Dossiers required for untouched Domains? | No. OQ-039 profiles are already complete; implementation-grade mapping is deferred to affected Phase 7 slices. | `DOWNSTREAM_DETAIL` |
| Are planning documents duplicating upstream law? | The Roadmap uses concise IDs/sections and only repeats sequencing consequences, gates and exit conditions. | `EDITORIAL` pass |
| Can a later implementation agent follow it without routine invention? | Yes for selection/order/dependencies/gates/proof direction; exact reversible implementation choices remain explicitly downstream. | `ROADMAP_GAP` pass after gate/proof tables |

### Consolidated review result

One consolidated review was performed after the first working draft using the required lenses. The result is **PASS after one correction pass**.

| Review lens | Result | Finding |
|---|---|---|
| Backward-planning integrity | PASS | Mature ecosystem, branches and dependency direction are explicit; the core path is not a chronology copied from Product Law. |
| MVP integrity | PASS | `FP-001...FP-006` is the smallest safe commercial path; future products do not become prerequisites. |
| Product Law coverage | PASS | MVP, pilot, Nuwe Jy, Membership, Adjustment/Premium, practitioner, community, live, events and experimentation are all placed. |
| Domain compatibility | PASS | Exact frozen Domain names are used; no ownership or circular control dependency is changed. |
| Architecture compatibility | PASS | Only accepted authority, transaction, async, provider, privacy, realtime and scaling mechanisms are referenced. |
| Gate timing | PASS | Current OQs are scheduled at first need; future gates are explicitly non-blocking/future-only. |
| Safety/clinical | PASS | Safety/eligibility precedes plan; practitioner and adjustment gates cannot be bypassed. |
| Privacy/security | PASS | Controls are placed before the behaviour they protect; deletion/export/retention gates are visible. |
| Payment/entitlement | PASS | Commerce precedes Entitlements and both precede consumed assessment/plan access. |
| Failure/recovery | PASS | FP-002, FP-005, FP-006, FP-007, FP-008 and FP-015 own their material failure/proof obligations. |
| Performance/scale | PASS | Scale concerns are visible without premature infrastructure; event/experiment proof is later and explicit. |
| Anti-overengineering | PASS | Packs are outcome/evidence-oriented and future branches are gated. |
| Development friction | PASS | Phase 7 can select FP-001 without inventing upstream policy or implementation semantics. |

### Correction pass applied

- `ROADMAP_GAP`: added FP-007 as the explicit governed live/replay outcome so Basic Membership and Nuwe Jy do not smuggle live capability into unrelated packs.
- `ROADMAP_GAP`: added FP-006 as the explicit operational/release evidence boundary so the first paid pilot is not treated as an implied consequence of feature completion.
- `EDITORIAL`: clarified that FP-008 and FP-009 are sibling branches and that FP-009 is not a hard prerequisite for Nuwe Jy.
- `DOWNSTREAM_DETAIL`: made the provisional proof labels, OQ-039 mapping and exact infrastructure choices explicitly Phase 7/Architectural-Proof work.

No `UPSTREAM_CONTRADICTION` was found. No upstream file was changed.

---

# 20. Roadmap closure audit

| Closure criterion | Result | Evidence in this Roadmap |
|---|---|---|
| Mature platform outcome represented | PASS | §2 mature participant/business ecosystem and capability table |
| Backward dependency model coherent | PASS | §3 graph, challenges and no-cycle statement |
| Every approved delivery path has a place | PASS | §§5, 9–13, 16 |
| Smallest safe MVP/first-paid path explicit | PASS | §7 `FP-001 → FP-006` |
| Pilot progression explicit | PASS | §8 internal → 10 → 25 → 50 → limited public → public |
| Nuwe Jy preserved | PASS | `FP-008`, §9 |
| Membership/Premium preserved | PASS | `FP-009`, `FP-010`, `FP-011`, §10 |
| Practitioner path preserved | PASS | `FP-012`, §11 |
| Community/live/events preserved | PASS | `FP-007`, `FP-013`, `FP-015`, §12 |
| Experimentation appropriately scheduled | PASS | `FP-016`, §13 |
| Feature Packs outcome-oriented | PASS | §6; no Domain/page/technical-only pack |
| Dependency graph has no unresolved circular dependency | PASS | §3.2 and §3.3 |
| Every FP has validation objective and type | PASS | §6, FP-001...FP-017 |
| Major Domains identified per FP | PASS | `Affected Domains` on every FP; exact frozen names used |
| Blocking gates scheduled before need | PASS | FP gate classifications and §14 |
| Future/non-blocking gates not pulled forward | PASS | §14 and §19 |
| Architectural proof needs visible | PASS | FP fields and §15 |
| Performance obligations sequenced without premature infrastructure | PASS | FP fields and §17 |
| Privacy/security/safety before protected behaviour | PASS | FP fields and §18 |
| No Product Law invented | PASS | Authority references and review result |
| No Architecture mechanism invented | PASS | Architecture references and deferred detail boundaries |
| No Domain ownership changed | PASS | Exact `04_DOMAIN_MAP` names and authority rule |
| No implementation-grade dossier work performed | PASS | No schemas, Resources, indexes, keys, queues, topics or code |
| Phase 7 can select FP-001 | PASS | §7, FP-001 entry conditions/gates/proof direction |

## 20.1 Phase 6 verdict

**PASS — PHASE 6 COMPLETE / ROADMAP FROZEN v1.0.0 (historical).**

**v1.1.0 amendment:** Additive Targeted Product Amendment Roadmap sequencing — PASS. Feature Pack count remains 17; Research/Voting remain FUTURE-GATED / FEATURE-PACK-UNASSIGNED; PMR is REQUIRED in FP-001; Interactive Tools remain purpose-distributed; no upstream contradiction.

This verdict does not authorise Phase 7 continuation beyond already-approved preparation, FP-001 artifact reconciliation, JIT Domain Dossiers for Domains 19/20, Architectural Proof, Vertical Slices, TOON generation or implementation. `ATLAS_RECONCILIATION_REQUIRED` and `FP001_RECONCILIATION_REQUIRED` remain downstream.

---

# 21. Phase 7 handoff

This Roadmap defines the approved outcome sequence, dependencies and gates. It does not select or own the active task or stage, grant execution authorisation, or record current programme status. README and current Open Work own programme routing and current task/stage selection; use those current sources for operational status. This Roadmap records the approved sequence and gate boundaries only.

FP-001 has existing Phase 7A work and an Identity & Access dossier. The narrow PMR artifact reconciliation remains required after certified Engineering Standards Authority Promotion and has not been performed. Phase 7C remains gated, proof classification is not finalised, and executable authentication proof is incomplete.

When current Open Work authorises a Phase 7 task, that task must:

- use this Roadmap's `FP-001` outcome and dependencies;
- preserve upstream Product, Architecture and Domain authority;
- create only the JIT Domain Dossiers required by the selected pack;
- use the resolved `OQ-034` architecture selection and preserve its incomplete Phase 8 proof obligation; resolve `OQ-035`/`OQ-036` only at the affected depth;
- perform implementation-grade `OQ-039` mapping only for affected domains/actions;
- make the final proof choice `REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`;
- stop if a task would need to invent product policy, clinical thresholds, ownership, provider semantics, retention, security exceptions or implementation-grade domain semantics.

```text
PHASE 0 — COMPLETE
PHASE 1 — COMPLETE
PHASE 2 — COMPLETE
PHASE 3 — COMPLETE
PHASE 4 — COMPLETE / Architecture frozen
PHASE 5 — COMPLETE / Domain Map frozen
PHASE 6 — COMPLETE / Roadmap frozen

ACTIVE NEXT STAGE:
SEE CURRENT OPEN WORK §9
```

Do not advance the current stage from this Roadmap patch.
