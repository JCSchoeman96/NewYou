
# 04_DOMAIN_MAP_v1.2.0.md

- **Document status:** FROZEN / AMENDED DOMAIN MAP + DOMAIN ARCHITECTURE PROFILE BASELINE
- **Document version:** v1.2.0
- **Predecessor frozen version:** `archive/04_DOMAIN_MAP_v1.1.1.md`
- **SemVer transition:** `v1.1.1 → v1.2.0` — substantive Domain-law clarification implementing Product Law §21S and DEC-304; owner boundaries remain unchanged.
- **Started:** 2026-08-17
- **Last updated:** 2026-09-26
- **Authority:** Implements current Product Law §21S and DEC-304 while preserving `03_ARCHITECTURE_v1.1.1.md`; it defines owner boundaries and request direction without implementation mechanics.
- **Primary inputs:** `archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`, `archive/00_PLATFORM_v1.3.0.md`, `archive/01_DECISIONS_v1.3.0.md`, `03_ARCHITECTURE_v1.1.1.md`, `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`, `archive/02_OPEN_WORK_v1.2.37.md`, `working/TARGETED_DOMAIN_PRESSURE_TEST_WORKING_v0.1.0.md`
- **Architecture deep reference:** `reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md` only where the frozen synthesis needs deeper legislative detail
- **Governance boundary:** This document decides **WHO owns durable business truth**. It does not invent new platform mechanisms, implementation schemas or source code.
- **Current result:** TARGETED DOMAIN AMENDMENT COMPLETE / PASS — 20 approved ownership domains, additive PMR/Research/Voting/Tool-boundary ownership, 20/20 lightweight Domain Architecture Profiles, 0 shared-write ambiguities, 0 circular authoritative control dependencies, 0 Product/Architecture contradictions.

## 1. Purpose and authority

`03_ARCHITECTURE_v1.1.1.md` answers how the platform works. This Domain Map assigns concrete ownership of the mature platform's approved business truth under that frozen architecture, including the Product-derived Research, Voting, Interactive Tool and Platform Member Reference constraints in `DEC-294`–`DEC-298` and `ARC-328`–`ARC-332`.

The v1.0.0 predecessor remains historical Domain Law for its original Product/Architecture baseline. The archived v1.1.0 successor adds Domains 19–20 while preserving Domains 1–18 identity and numbering. The archived v1.1.1 path-only predecessor preserves that amendment. This v1.2.0 successor implements Product §21S and DEC-304: purpose-level marketing permission remains Privacy & Consent truth, while channel/category preference remains Communications truth, with an owner-mediated request edge for purpose withdrawal.

The governing rules are:

1. Every major durable business truth has exactly one authoritative owning domain.
2. A relationship/reference does not transfer mutation authority.
3. Cross-domain writes invoke the owning domain's application interface; no domain reaches into another domain's persistence as an alternate business API.
4. Derived projections, search, cache, analytics, PubSub observations and external-provider state never become hidden business authority.
5. Cross-cutting orchestration (for example full deletion) may request domain-owned transitions but does not acquire ownership of the underlying records.
6. The Domain Map may combine capabilities when they share durable truth/lifecycle/invariants; it must not create a domain merely because a feature, page, table or staff screen exists.
7. Final Ash Resource names, schemas, indexes, Redis structures, TTLs, PubSub topics, Oban worker/queue names and implementation code remain downstream JIT dossier/Feature Pack work.

## 2. Boundary decisions from the discovery pass

The pre-existing 22-name list was treated as a hypothesis, not a target. The resulting model deliberately makes these consolidations/non-domains:

- `Accounts` + `IdentityAndAccess` → **Identity & Access** because account lifecycle, authentication, sessions and identity-side privilege share one canonical authority.
- `Consent` + privacy/data-lifecycle orchestration → **Privacy & Consent** because purpose authority, withdrawal, deletion, retention, legal hold and export are one participant-data-rights/governance boundary.
- `Programmes` + `Challenges` → **Programmes & Challenges** because both own versioned structured participation, enrolment/participation and completion semantics; social discussion remains Community.
- `Habits` + `Journals` + behavioural progress → **Habits, Journals & Progress** because these are participant self-tracking/reflective truths with closely related privacy/recovery semantics.
- `Memberships` is **not** a separate domain: Commerce owns the commercial membership/subscription contract; Entitlements owns the resulting access rights.
- `Recommendations` is **not** a durable-truth domain: feed ranking/recommendations are derived capabilities over Content, Plans, Safety, Temperament and Analytics signals.
- `Administration` is **not** a business domain: admin/support screens invoke the owning domains under policy; UI/operator grouping does not create ownership.
- `Nuwe Jy` is **not** a separate domain: it is a configured flagship composition of Programmes & Challenges plus shared Safety, Plans, Community, Events/Live, Communications and Analytics capabilities.
- `Interactive Tools` is **not** a Domain: calculation is not authority; public/anonymous execution is non-authoritative by default; purpose-specific protocols and results remain with existing owners.
- `Interactive Evidence` / `Engagement` are **not** Domains: shared primitives do not create shared business authority.
- `Platform Member Reference` is **not** a Domain: it is Identity & Access Account truth.
- `Competitions` is **not** a Domain: a competition may compose Voting & Balloting with Programmes, Community, Safety, Commerce, Entitlements, Events and Communications.

The model keeps the following boundaries deliberately separate because combining them would blur authority:

- Health Records vs Safety & Eligibility: facts are not decisions.
- Commerce vs Entitlements: money/contract truth is not access truth.
- Identity & Access vs Professional Care: being a practitioner identity/role is not an active care relationship or professional record.
- Experimentation vs Analytics: experiment configuration/assignment/decision authority is not the derived measurement pipeline.
- Content & Media vs Communications: governed message/template content is not durable delivery state.
- Programmes & Challenges vs Community: structured participation/completion is not social/moderation truth.
- Events & Live vs Commerce: scarce capacity/ticket truth is not payment truth.

## 3. Approved domain set

| # | Domain | Core authoritative truth |
|---:|---|---|
| 1 | **Identity & Access** | canonical human/platform identity and individual account lifecycle |
| 2 | **Privacy & Consent** | purpose-specific consent/lawful-basis grants, withdrawals and current consent state |
| 3 | **Temperament** | assessment methodology versions, questions/answer options/scoring configuration under methodology authority |
| 4 | **Health Records** | progressively collected health/lifestyle intake facts |
| 5 | **Safety & Eligibility** | eligibility evaluations and outcomes |
| 6 | **Plans & Nutrition** | plan generation request/outcome and immutable delivered plan snapshot |
| 7 | **Content & Media** | conceptual content identity and immutable content versions |
| 8 | **Programmes & Challenges** | programme definitions/versions/modules/lessons/activity structure references |
| 9 | **Habits, Journals & Progress** | habit catalogue entries allowed by Product Law, participant habits and practitioner-assigned habit references |
| 10 | **Commerce** | commercial product/catalogue lifecycle and versioned prices/offers/discounts |
| 11 | **Entitlements** | entitlement identity, scope, source/provenance, validity/expiry and revocation |
| 12 | **Community** | first-party community groups/spaces and participation state |
| 13 | **Events & Live** | live session/event definitions, versions and occurrences |
| 14 | **Professional Care** | practitioner professional profile/relationship metadata beyond canonical identity role |
| 15 | **Communications** | mailing-list/subscriber communication contact state for people without full accounts, linked/reconciled when appropriate |
| 16 | **Experimentation** | experiment identity/configuration/version, variants, eligibility/protected-invariant exclusions and activation state |
| 17 | **Analytics** | governed product/behaviour/operational analytical event facts as permitted |
| 18 | **Audit & Evidence** | append-only audit evidence for sensitive/domain-governed actions where central evidence is required |
| 19 | **Research & Feedback** | governed Research/feedback campaign, instrument/version and participant response lifecycle |
| 20 | **Voting & Balloting** | governed vote rules, submission/integrity evidence, accepted tally, finalisation, official result and adjudication |


The names above are Domain Law names, not final Elixir module/file names. Later JIT dossiers may refine implementation grouping but may not move ownership without an explicit Domain Law amendment. Domains 1–18 retain their historical numbers. Domains 19 and 20 are appended; they are not inserted among the original set.

## 4. Platform-wide business-truth ownership matrix

| Business truth | Authoritative domain | Principal dependents | Interaction rule |
|---|---|---|---|
| Canonical platform identity/account | **Identity & Access** | All domains | READ actor/context; COMMAND owner for identity lifecycle |
| Credentials, sessions, devices and privilege grants | **Identity & Access** | All protected domains | READ current authority; COMMAND owner |
| Account closure/recovery | **Identity & Access** | Privacy & Consent, Entitlements | COMMAND owner; full deletion remains Privacy |
| Purpose-specific consent/current consent, including marketing-purpose permission | **Privacy & Consent** | IAM/business domains, Communications | READ/check; sole COMMAND owner for grant/withdraw |
| Full deletion orchestration/suppression truth | **Privacy & Consent** | Every data-owning domain | ORCHESTRATE deletion contracts; no shared writes |
| Retention policy/legal hold/export lifecycle | **Privacy & Consent** | All retained data domains | GOVERNANCE/ORCHESTRATION |
| Assessment methodology/version | **Temperament** | Content, Plans, Programmes | READ immutable config |
| Assessment attempt/answers/raw scores/result | **Temperament** | Plans, Analytics | READ governed projection |
| Selected current temperament profile | **Temperament** | Plans, Content, Programmes | READ current profile |
| Participant health/lifestyle facts | **Health Records** | Safety, Plans, Professional Care | READ minimum necessary |
| Laboratory/measurement provenance | **Health Records** | Safety, Professional Care | READ scoped facts |
| Eligibility/safety outcome | **Safety & Eligibility** | Plans, Programmes, Professional Care | READ current authority |
| Safety case/restriction/override | **Safety & Eligibility** | Plans, Professional Care | COMMAND owner; PubSub/Oban consequence allowed |
| Plan generation/version/provenance | **Plans & Nutrition** | Entitlements, Programmes, Participant | READ; COMMAND owner |
| Plan review/adjustment outcome | **Plans & Nutrition** | Safety, Professional Care | COMMAND owner; inputs read cross-domain |
| Governed content/translation/publication version | **Content & Media** | All delivery domains | READ exact version; COMMAND owner |
| Editorial media identity/derivatives/publication | **Content & Media** | Events, Communications, Content consumers | READ/protected delivery |
| Taxonomy/search source metadata | **Content & Media** | Analytics/discovery projection | DERIVE projection; source remains owner |
| Programme/challenge definition/version | **Programmes & Challenges** | Content, Entitlements, Community | READ |
| Edition/cohort/enrolment/completion | **Programmes & Challenges** | Community, Events, Analytics | READ/COMMAND owner |
| Challenge participation/completion | **Programmes & Challenges** | Community, Analytics | READ |
| Habit definition/schedule/occurrence | **Habits, Journals & Progress** | Programmes, Plans | READ participant progress |
| Private journal/reflection | **Habits, Journals & Progress** | Professional Care only when shared | SCOPED READ; owner controls share state |
| Behavioural/progress/adherence entry | **Habits, Journals & Progress** | Plans, Programmes, Analytics | READ minimum approved fields |
| Commercial product/offer/price | **Commerce** | Public UI, Entitlements | READ immutable/current commercial config |
| Purchase/payment/refund/dispute truth | **Commerce** | Entitlements, Events, Analytics | COMMAND owner; emit consequence/evidence |
| Membership/subscription/add-on commercial contract | **Commerce** | Entitlements | READ/CONSEQUENCE to access owner |
| Entitlement/access grant | **Entitlements** | All protected product domains | READ current access; COMMAND owner |
| Access redemption code/consumable credit | **Entitlements** | Commerce, Temperament, Plans | COMMAND owner; idempotent consumption |
| Native community group/participation | **Community** | Programmes, Entitlements | READ/COMMAND owner |
| Community content/moderation/sanction/appeal | **Community** | Audit, Analytics | READ derived/minimised evidence |
| Event/live occurrence/registration/waitlist | **Events & Live** | Programmes, Communications | READ/COMMAND owner |
| Scarce event hold/capacity allocation/ticket | **Events & Live** | Commerce, Entitlements | COMMAND owner; payment evidence consumed |
| Attendance/check-in | **Events & Live** | Analytics, Programmes | READ observation/business fact |
| Practitioner care/review relationship | **Professional Care** | IAM, Health, Safety | READ scoped relationship |
| Professional review case/outcome/platform-held record | **Professional Care** | Safety, Plans | COMMAND owner; downstream commands to owners |
| Practitioner saleable-capacity/referral state | **Professional Care** | Commerce/Operations | READ for sale gating |
| Notification/subscriber communication contact | **Communications** | Identity, Privacy | READ linked destination; no canonical-email mutation |
| Notification and marketing channel/category preferences, quiet-hours/caps | **Communications** | Originating domains, Privacy & Consent | COMMAND owner for preferences; READ at delivery |
| Message intent/delivery attempt/provider evidence | **Communications** | Originating domains, Analytics | READ delivery observation only |
| Experiment definition/version/variant | **Experimentation** | Content, Communications, Analytics | READ immutable active config |
| Experiment assignment | **Experimentation** | Delivery surfaces, Analytics | READ assignment; no business authority |
| Experiment final governed decision/learning | **Experimentation** | Product/Content owners | READ evidence-backed decision |
| Analytical event/fact | **Analytics** | Dashboards/experiments | DERIVED from authoritative sources |
| Analytical projection/aggregate/dashboard | **Analytics** | Operators/Product | DERIVED/REBUILDABLE |
| Experiment exposure/outcome measurement aggregate | **Analytics** | Experimentation | EVIDENCE to experiment decision |
| Cross-cutting audit/security evidence | **Audit & Evidence** | Governance/Operators | APPEND/READ restricted; never source-domain truth |
| Incident/release decision evidence | **Audit & Evidence** | Operations/Product authority | APPEND/READ restricted |
| Platform Member Reference lifecycle | **Identity & Access** | Commerce, Entitlements, Events, Communications | READ minimum-disclosure lookup; COMMAND owner for assignment/retirement/merge; never authentication or entitlement proof |
| Research/feedback campaign, instrument and published version | **Research & Feedback** | Content, Identity, Analytics | READ exact published version; COMMAND owner |
| Participant Research/feedback response | **Research & Feedback** | Analytics, Privacy, Audit | READ governed projection; COMMAND owner; not Health/Safety/Plan/Temperament truth |
| Research correction, withdrawal and de-link lifecycle | **Research & Feedback** | Privacy & Consent | COMMAND owner; Privacy orchestrates deletion/retention decisions without rewriting Research meaning |
| Staff Research annotation/classification | **Research & Feedback** | Audit & Evidence | COMMAND owner; distinguishable from participant-submitted truth |
| Governed vote/poll rules | **Voting & Balloting** | Identity, Entitlements, Programmes, Community | READ eligibility context; COMMAND owner; surface location does not transfer ownership |
| Vote submission and integrity disposition evidence | **Voting & Balloting** | Audit, Identity | COMMAND owner; integrity assurance is not identity assurance |
| Accepted vote tally | **Voting & Balloting** | Analytics | COMMAND owner; Analytics/caches/provider counts are not tally authority |
| Governed vote finalisation | **Voting & Balloting** | Audit & Evidence | COMMAND owner; durable, auditable, rule-tied |
| Official voting result | **Voting & Balloting** | Commerce, Entitlements, Content, Analytics | READ result; COMMAND owner; reward/entitlement is a separately owned consequence |
| Vote exception, adjudication, correction and rerun | **Voting & Balloting** | Audit & Evidence | COMMAND owner; Audit appends evidence only |
| Published Interactive Tool editorial/presentation artifact | **Content & Media** | delivery surfaces | READ published copy/configuration where the meaning is Content publication; Content does not own calculation or consequential results |
| Account-linked educational/self-tracking Interactive Tool result | **Habits, Journals & Progress** | Analytics | COMMAND owner only when the business meaning is self-tracking, behavioural progress or reflective/non-clinical personal progress |


### 4.1 Ownership interpretation

- The matrix assigns **one owner per listed durable truth**. A dependent may hold a reference, immutable snapshot/provenance or rebuildable projection only where Architecture/Product Law permits it.
- Composite user journeys may invoke multiple owners. A single UI form/check-in does not imply a single database/domain owner for every submitted fact.
- Identity & Access owns canonical identity-side grants; a business domain owns its scoped relationship/assignment truth. A cohort facilitator relationship, community participation or practitioner-care relationship does not become IAM-owned merely because policy uses the actor grant.
- Cross-cutting Privacy deletion/export and Audit evidence edges are orchestration/evidence relationships, not shared-write ownership.
- Read dependency cycles are not automatically defects. A **circular control dependency** exists only when two domains require one another to mutate authoritative state in an unresolvable loop. No such cycle is accepted in this map.

## 5. Cross-domain command/dependency doctrine

| From | To | Contract / dependency |
|---|---|---|
| Communications | Privacy & Consent | Owner-mediated purpose-withdrawal request only when a participant explicitly selects purpose-level marketing withdrawal; Privacy & Consent alone commits permission state. |
| Commerce | Entitlements | Durable grant/revoke intent after authoritative commercial transition |
| Health Records | Safety & Eligibility | Safety reads current scoped health facts; health owner accepts fact changes |
| Safety & Eligibility | Plans & Nutrition | Current eligibility is required input; safety transitions may trigger durable pause/re-evaluation consequence |
| Temperament | Plans & Nutrition | Plans read selected current temperament for approved presentation/behavioural variation |
| Habits, Journals & Progress | Plans & Nutrition | Plans read approved check-in/adherence inputs; Plans owns adjustment decision |
| Professional Care | Safety & Eligibility | Professional outcome requests governed clearance/restriction through Safety owner |
| Professional Care | Plans & Nutrition | Practitioner-authored change becomes a new Plan version through Plans owner |
| Content & Media | Programmes & Challenges | Programmes reference immutable approved content versions |
| Programmes & Challenges | Community | Cohort/challenge association configures community context; Community owns discussion/moderation |
| Programmes & Challenges | Events & Live | Programme links sessions/events; Events owns registration/attendance |
| Entitlements | Programmes & Challenges | Programmes checks current access; does not mutate entitlement |
| Entitlements | Community | Community admission checks current access |
| Entitlements | Events & Live | Protected session/replay admission may check general access; event ticket/admission authority itself remains Event truth |
| Events & Live | Commerce | Event checkout requests commercial payment; Events retains capacity/ticket authority |
| Content & Media | Communications | Communications references exact governed template/content version |
| Privacy & Consent | Communications | Delivery re-checks current marketing-purpose permission when applicable; the applicable Communications preference remains Communications-owned. |
| Privacy & Consent | Professional Care | Professional access requires current consent/share scope |
| Privacy & Consent | All data-owning domains | Deletion/export/retention orchestration through owner contracts, not direct persistence |
| Experimentation | Analytics | Analytics supplies exposure/outcome evidence; Experimentation owns governed experiment decision |
| All authoritative domains | Analytics | Publish/derive minimum governed facts; Analytics never writes source truth |
| All sensitive domains | Audit & Evidence | Append minimum audit/security evidence; Evidence domain never mutates source truth |
| Research & Feedback | Content & Media | Authorised publication of findings/content artifacts; Content owns the published artifact, not the response |
| Research & Feedback | Communications | Follow-up/escalation communication intent; Communications owns delivery |
| Research & Feedback | Safety & Eligibility | Owner-mediated safety-escalation request; Safety establishes safety truth |
| Research & Feedback | Professional Care | Owner-mediated practitioner follow-up request; Professional Care establishes care truth |
| Research & Feedback | Commerce | Incentive/reward grant intent after authorised participation; Commerce establishes commercial truth |
| Research & Feedback | Entitlements | Incentive/access grant intent after authorised participation; Entitlements establishes access truth |
| Research & Feedback | Analytics | Derived research measurement only; Analytics never writes Research truth |
| Research & Feedback | Audit & Evidence | Append research/governance evidence; Audit never owns the response |
| Voting & Balloting | Commerce | Official-result consequence/reward intent; duplicate/retry-safe at the Commerce boundary |
| Voting & Balloting | Entitlements | Official-result access/prize grant intent; duplicate/retry-safe at the Entitlements boundary |
| Voting & Balloting | Analytics | Derived counts/projections/leaderboards only; not official-result authority |
| Voting & Balloting | Audit & Evidence | Append finalisation/adjudication evidence; Audit never owns the winner |
| Voting & Balloting | Community | Contextual surface/reference only; Community does not own the vote |
| Voting & Balloting | Programmes & Challenges | Contextual surface/reference only; Programmes does not own the vote |
| Privacy & Consent | Research & Feedback | Deletion/export/retention orchestration through the Research owner contract |
| Privacy & Consent | Voting & Balloting | Deletion/export/retention orchestration through the Voting owner contract |
| Identity & Access | Research & Feedback | Account/identity-assurance facts where the declared participation mode requires them |
| Identity & Access | Voting & Balloting | Account/identity-assurance facts where the declared participation mode requires them |
| Identity & Access | Commerce / Entitlements / Events | PMR lookup may identify a candidate beneficiary; the owning Domain validates its own rules |


The interaction table is intentionally architectural/domain-level. It does not define Ash action names, modules, events, topics or transaction implementation.

## 6. Domain laws and lightweight Architecture Profiles

### 6.1 — Identity & Access

**Product Law basis:** `DEC-017...DEC-028; DEC-244...DEC-256; DEC-268...DEC-270; DEC-297; ARC-330`

**Purpose:** Own the canonical platform identity and the durable authority needed to authenticate a human or system actor and determine the identity-side grants through which other domains evaluate current access, including the human-facing Platform Member Reference as Account truth.

**Owns:**

- canonical human/platform identity and individual account lifecycle;
- account email and verification state;
- authentication credential/recovery state, sessions, trusted devices and session revocation;
- platform identity-side role/privilege grants, scoped staff/practitioner role grants and break-glass authority records;
- duplicate-account reconciliation/merge authority and compromise-containment identity state;
- account closure/recovery state distinct from full deletion;
- Platform Member Reference assignment after successful individual Account creation, uniqueness, canonical active reference, normal immutability, reactivation continuity, permanent retirement/non-reuse, merge-survivor semantics, exceptional replacement/retirement under approved reasons, and minimum-disclosure PMR lookup as an Identity interface;

**Explicitly does not own:**

- purpose-specific consent or lawful-basis state;
- commercial membership contracts or product entitlements;
- practitioner care relationships or professional records;
- business-domain relationships/assignments (for example care relationship, cohort facilitator assignment or community participation) and permissions that derive from those relationships/consent;
- Platform Member Reference as database identity, login, authentication proof, authorisation, verification assurance, paid Membership, subscription, entitlement, voucher, coupon or discount authority;

**Major concepts/entities:**

- Identity;
- Account;
- Credential/Authentication Proof;
- Session;
- Trusted Device;
- Role Grant;
- Privilege Grant;
- Recovery Case;
- Account Merge;
- Account Closure;
- Platform Member Reference;

**Major lifecycle/state:** account creation → verification → active/restricted/closed/recoverable; sessions/devices are independently revocable; privileges are scoped/time-bounded; recovery restores identity control but never manufactures domain authority. PMR: unassigned/pre-Account → assigned/canonical active after successful individual Account creation → retained on legitimate reactivation → retired and permanently non-reusable after retirement, merge of the non-survivor, or final deletion; exceptional replacement requires an approved security, privacy, integrity, reconciliation or equivalent operational-correctness reason. Exact prefix, alphabet, grouping, length, checksum, generator and database representation remain unfrozen (`ARQ-IAM-013`).

**Domain capabilities:**

- register/verify/authenticate/recover identity;
- issue/revoke sessions and device trust;
- grant/revoke scoped roles and privileges;
- contain compromised accounts;
- merge duplicate identities through governed reconciliation;
- assign, look up, retire and exceptionally replace a Platform Member Reference;

**Key policies:**

- 18+ and product capability gates remain Product/domain rules; identity only supplies verified actor context;
- staff/practitioner MFA and privileged step-up are mandatory where locked;
- no universal Super Admin bypass; break-glass is named, reasoned, time-bounded and audited;
- non-enumerating authentication/recovery behaviour;
- a Platform Member Reference is a stable human-facing Account reference: non-secret but private-by-default; possession never proves Account control, authentication, authorisation, verification, payment, membership, subscription or entitlement;

**Key invariants/data-integrity rules:**

- one canonical platform identity per reconciled human identity;
- session/device state cannot grant authority beyond current role/relationship/consent policy;
- account recovery cannot recreate entitlement, care relationship, consent or other domain truth;
- account closure is not full deletion;
- one canonical active PMR per ordinary individual Account; retired values are never reassigned; lookup is purpose-scoped and minimum-disclosure;

**Sensitive-data classification:** PERSONAL + SECURITY; credential secrets and privileged grants are highly restricted.

**External dependencies:**

- email delivery via Communications for verification/recovery notices;
- edge/application abuse controls under frozen Architecture;

**Cross-domain dependencies:**

- Privacy & Consent for consent-sensitive access and full deletion;
- Audit & Evidence for security/audit evidence;
- Professional Care for practitioner relationship context;
- all business domains consume actor/identity context without mutating Identity directly;

**Principal unresolved gates:**

- OQ-034 authentication implementation architecture;
- OQ-035 abuse-control thresholds/recovery;
- `FP001_RECONCILIATION_REQUIRED` because PMR is assigned at successful individual Account creation already in FP-001; this Domain amendment does not modify FP-001 artifacts;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority; one-purpose secrets stored only through approved protected secret/token mechanisms. |
| Hot / warm / cold | Cold/durable identity, grants and sessions; hot/warm acceleration only for explicitly safe current-session/policy lookups. |
| Transaction / concurrency sensitivity | HIGH correctness sensitivity for registration, login, recovery, merge, privilege/session revocation and velocity controls. |
| Major scaling risks | login/recovery bursts, password-hashing cost, distributed velocity state, session revocation propagation. |
| Redis | POTENTIALLY_APPLICABLE for distributed velocity/risk state where required; never identity authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for safe immutable/config/session lookup acceleration with revocation bypass. |
| GenServer | NONE initially; only if later hot aggregation/coordination proves necessary. |
| PubSub | POTENTIALLY_APPLICABLE for revocation/freshness observation only. |
| Oban | POTENTIALLY_APPLICABLE for durable verification/recovery/security notifications and non-authoritative follow-up. |
| Replica relevance | NONE for current-authority decisions; stale-tolerant admin/report reads may later use replicas. |
| Streaming / pagination | Pagination relevant for sessions/devices/grants/security history; no unbounded loads. |


### 6.2 — Privacy & Consent

**Product Law basis:** `DEC-025...DEC-026; DEC-094; DEC-220...DEC-243`

**Purpose:** Own purpose-specific consent and participant data-rights/lifecycle authority, including full deletion, retention governance, legal holds and participant export orchestration.

**Owns:**

- purpose-specific consent/lawful-basis grants, withdrawals and current consent state;
- purpose-specific consent/share authority used by practitioner and other scoped access; the target relationship/entry-share record remains with its owning business domain;
- full-deletion request/cancellation/execution orchestration and deletion-completion state;
- retention-policy assignments/versions, retained-by-obligation classification and legal holds;
- participant export requests and protected export lifecycle;
- minimal deletion/suppression/replay truth required to prevent resurrection after restore;

**Explicitly does not own:**

- canonical account closure/recovery state;
- the underlying health, plan, journal, commercial, professional, Research/Feedback or Voting & Balloting records being governed;
- audit/security evidence produced by actions in other domains;
- professional record retention durations not yet approved by expert authority;

**Major concepts/entities:**

- Consent Grant;
- Consent Withdrawal;
- Processing Purpose;
- Deletion Request;
- Deletion Run;
- Retention Policy;
- Legal Hold;
- Export Request;
- Suppression/Deletion Replay Record;

**Major lifecycle/state:** consent granted/versioned → active → withdrawn/superseded; deletion requested → cancellation window → durable orchestration → verified completion; legal hold scoped → active/reviewed → released → deferred deletion resumes.

**Domain capabilities:**

- grant/withdraw purpose-specific consent;
- evaluate current consent state;
- initiate/cancel/execute full deletion across domain deletion contracts;
- place/release legal holds;
- request/build/deliver/expire participant exports;
- reapply deletion/withdrawal truth after restore;

**Key policies:**

- consent is purpose-specific and cannot be inferred from unrelated participation;
- withdrawal stops dependent future processing and invalidates derived authority;
- full deletion is distinct from closure and cannot reconstruct completed participant access;
- retained-by-obligation records are isolated/minimised and unavailable for normal product use;

**Key invariants/data-integrity rules:**

- deletion completion covers live, derived, cached, external and access paths required by law;
- backup restore may not resurrect deleted/withdrawn participant authority;
- pseudonymisation is not treated as irreversible anonymisation;
- legal holds are narrow and do not freeze unrelated data indefinitely;

**Sensitive-data classification:** PERSONAL + HEALTH/PROFESSIONAL linkage metadata; highly privacy-sensitive governance state.

**External dependencies:**

- external processors participate through deletion/export contracts;
- object storage/search/analytics/cache representations are governed targets, not Privacy-owned business data;

**Cross-domain dependencies:**

- Identity & Access for destructive-action verification and actor identity;
- every data-owning domain exposes its deletion/export/retention contract;
- Audit & Evidence records governance actions without becoming deletion authority;

**Principal unresolved gates:**

- OQ-009 early retention categories;
- OQ-029 full retention schedule matrix;
- OQ-030 external processor deletion/export inventory;
- OQ-031 backup restore/deletion replay;
- OQ-032 export/deletion operations;
- OQ-033 professional record authority where retention intersects care records;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority for consent, lifecycle orchestration, holds, export/deletion state and suppression truth. |
| Hot / warm / cold | Cold/durable governance truth; small current-consent/suppression checks may receive bounded acceleration with immediate invalidation. |
| Transaction / concurrency sensitivity | HIGH correctness sensitivity around withdrawal, deletion, restore replay, hold release and concurrent downstream writes. |
| Major scaling risks | large deletion/export fan-out, processor coordination, restore replay, mass policy changes. |
| Redis | NONE initially for authority; potentially useful only for non-authoritative orchestration coordination if proven. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable policy metadata/current-consent acceleration only with authoritative bypass. |
| GenServer | NONE initially. |
| PubSub | POTENTIALLY_APPLICABLE for consent/deletion invalidation freshness only. |
| Oban | APPLICABLE for durable deletion/export orchestration and processor follow-up. |
| Replica relevance | NONE for consent/deletion authority; stale-tolerant compliance reporting may later use replicas. |
| Streaming / pagination | Streaming/pagination relevant for large exports/deletion scans; never load complete participant estates into memory. |


### 6.3 — Temperament

**Product Law basis:** `DEC-031...DEC-036; DEC-051...DEC-072; DEC-272`

**Purpose:** Own the Four-Colour temperament methodology representation, assessment attempts/results and the participant-selected current temperament profile used by approved downstream personalisation.

**Owns:**

- assessment methodology versions, questions/answer options/scoring configuration under methodology authority;
- assessment attempts, saved/submitted answers and attempt consumption state;
- immutable calculated colour scores/raw result and reviewed interpretation history;
- self_reported, book_derived and digitally_assessed provenance;
- participant-selected current eligible temperament profile;
- delivered assessment report provenance/version relationship;

**Explicitly does not own:**

- health/safety truth or clinical eligibility;
- plan nutritional calculations;
- general editorial content outside temperament/report content references;
- commercial entitlement to start an assessment;

**Major concepts/entities:**

- Methodology Version;
- Assessment Attempt;
- Answer;
- Score Set;
- Temperament Result;
- Reviewed Interpretation;
- Current Temperament Profile;
- Assessment Report Snapshot;

**Major lifecycle/state:** methodology draft/approved/active/retired; attempt available → started → saved/resumed → submitted/expired; result immutable; current profile explicitly selected and may change without deleting history.

**Domain capabilities:**

- publish approved methodology versions;
- start/save/resume/submit assessment;
- score deterministically and resolve approved ties;
- record reviewed interpretation without rewriting raw result;
- select current profile;
- produce/retrieve immutable report provenance;

**Key policies:**

- methodology authority is restricted to approved Venessa/Super Admin authority under IP agreement;
- all scored questions required; one active attempt;
- historical results/answers remain immutable while retained;
- temperament may influence presentation/behavioural delivery but never safety or nutritional truth;

**Key invariants/data-integrity rules:**

- submitted answers + score + methodology version reproduce the raw result;
- later results never silently overwrite earlier results;
- current profile selection is explicit;
- self/book-derived results remain clearly labelled and cannot masquerade as digital assessment evidence;

**Sensitive-data classification:** PERSONAL; temperament results are sensitive personalisation data but not clinical diagnosis.

**External dependencies:**

- Content & Media supplies governed translated/report content blocks;
- Entitlements supplies authority to start paid/reassessment attempts;

**Cross-domain dependencies:**

- Identity & Access for participant actor;
- Entitlements for assessment/reassessment rights;
- Content & Media for bilingual approved report content;
- Plans, Programmes & Challenges and Content may read current temperament profile;

**Principal unresolved gates:**

- OQ-006 score-distance thresholds;
- IP/licence authority under OQ-001/legal work where applicable;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority. |
| Hot / warm / cold | Cold/durable attempts/results/methodology; approved immutable methodology/current-profile lookups may be warm/hot candidates. |
| Transaction / concurrency sensitivity | Moderate; one-active-attempt, entitlement consumption and submit/idempotency are correctness-sensitive. |
| Major scaling risks | assessment campaign bursts, report generation/read demand, result-history depth. |
| Redis | NONE initially. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable active methodology/scoring metadata if evidence warrants. |
| GenServer | NONE. |
| PubSub | POTENTIALLY_APPLICABLE for current-profile/report freshness only. |
| Oban | POTENTIALLY_APPLICABLE for non-immediate report composition/delivery consequences where semantics justify. |
| Replica relevance | NONE for scoring/current-profile authority; historical/report analytics may later use stale-tolerant reads. |
| Streaming / pagination | Pagination relevant for long result/attempt history; ordinary scoring must use bounded input. |


### 6.4 — Health Records

**Product Law basis:** `DEC-073...DEC-088; DEC-226; DEC-228`

**Purpose:** Own participant-provided and verified health/lifestyle facts used by Safety, Plans and Professional Care, preserving provenance and history without itself deciding eligibility or treatment.

**Owns:**

- progressively collected health/lifestyle intake facts;
- date of birth when collected for plan/safety purpose;
- food exclusions, medication/supplement declarations, symptoms and relevant health context;
- laboratory result records, units/reference ranges/source/verification/validity evidence;
- health measurements and clinically relevant check-in facts;
- health-document/upload semantic records and provenance while retained;

**Explicitly does not own:**

- eligibility/safety decisions or clinical overrides;
- plan generation/adjustment decisions;
- private journal narrative and habit occurrence truth;
- professional practitioner records that must be retained under professional authority;

**Major concepts/entities:**

- Health Profile;
- Health Fact;
- Health Intake;
- Food Exclusion;
- Medication/Supplement Declaration;
- Laboratory Result;
- Measurement;
- Health Check-in Fact;
- Health Document;

**Major lifecycle/state:** facts are captured with provenance → corrected/superseded/versioned as appropriate → may expire for decision use while remaining historical → deleted/anonymised where eligible.

**Domain capabilities:**

- capture/update permitted self-guided health facts;
- record provenance/verification status;
- record measurements/labs and validity metadata;
- provide minimum approved data views to Safety/Plans/Professional Care;
- correct/supersede historical health facts according to record type;

**Key policies:**

- collect progressively for defined purpose;
- unverified data may prioritise education but cannot independently trigger clinical treatment;
- minimum necessary fields supplied to consuming domains;
- participant access/correction subject to immutable/professional record boundaries;

**Key invariants/data-integrity rules:**

- source/provenance is never lost when a health fact matters to safety;
- expired/superseded lab facts remain historical but cannot silently act current;
- health records do not themselves manufacture eligibility or plan authority;
- sensitive health data is not copied into feeds/analytics by default;

**Sensitive-data classification:** HEALTH / HIGHLY SENSITIVE PERSONAL DATA.

**External dependencies:**

- object storage for uploaded lab/health files under architecture; external lab integration is future only;

**Cross-domain dependencies:**

- Identity & Access for participant identity;
- Privacy & Consent for processing/sharing/deletion;
- Safety & Eligibility consumes approved health facts;
- Plans & Nutrition consumes only approved required facts;
- Professional Care consumes scoped health views with consent;

**Principal unresolved gates:**

- OQ-007 laboratory validity matrix;
- OQ-009/OQ-029 retention rules;
- OQ-030 external processor inventory where health processors exist;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority; protected object storage for health documents with domain metadata/control. |
| Hot / warm / cold | Cold/durable health history; narrowly derived current flags may be warm but never replace source facts. |
| Transaction / concurrency sensitivity | HIGH correctness/sensitivity for concurrent corrections, new risk facts and safety-triggering updates. |
| Major scaling risks | historical depth, document assets, check-in bursts, privacy/deletion fan-out. |
| Redis | NONE initially for health authority; do not duplicate raw health data for generic acceleration. |
| ETS / Cachex | NONE for participant health data; immutable clinical metadata may later be safe if separately approved. |
| GenServer | NONE. |
| PubSub | POTENTIALLY_APPLICABLE for freshness signals after authoritative health changes, with minimum payload. |
| Oban | POTENTIALLY_APPLICABLE for document processing/validation and durable derived consequences. |
| Replica relevance | NONE for current safety/plan reads; carefully scoped analytics/reporting may use stale-tolerant projections. |
| Streaming / pagination | Pagination/streaming required for histories/exports; protected files delivered via bounded capabilities. |


### 6.5 — Safety & Eligibility

**Product Law basis:** `DEC-078...DEC-095; DEC-208...DEC-209`

**Purpose:** Own deterministic safety/eligibility determinations, safety cases and governed overrides that decide which automated or professional pathway is currently permitted.

**Owns:**

- eligibility evaluations and outcomes;
- safety flags/cases and their lifecycle;
- approved routing outcome: automated/general wellness/professional review/insufficient information;
- safety pause/restriction authority and clearance state;
- scoped audited clinical overrides of automated safety outcomes;
- risk-routing evidence/version of the rules applied;

**Explicitly does not own:**

- underlying health facts;
- professional care records/review encounter details;
- plan content/version itself;
- clinical rule values still awaiting expert approval;

**Major concepts/entities:**

- Eligibility Evaluation;
- Eligibility Outcome;
- Safety Flag;
- Safety Case;
- Safety Restriction;
- Clinical Override;
- Rule/Protocol Version Reference;

**Major lifecycle/state:** evaluation from current inputs → eligible/general-wellness/review-required/insufficient; new risk may open safety case → paused/restricted/review → cleared/resolved; overrides expire/supersede without rewriting original outcome.

**Domain capabilities:**

- evaluate approved safety rules;
- open/update/resolve safety cases;
- block or restrict automated pathways;
- request Professional Care review;
- apply authorised scoped override;
- re-evaluate when material health/consent state changes;

**Key policies:**

- medical/clinical safety outranks temperament, convenience and commercial entitlement;
- high-risk participants cannot receive automated personalised weight-loss plans;
- lowering high-risk status requires approved second-authority/protocol rules;
- urgent-help messaging never implies continuous monitoring;

**Key invariants/data-integrity rules:**

- every plan-eligible participant has an explicit current eligibility outcome;
- unsafe/missing critical information fails closed to an approved non-personalised/review pathway;
- original automated outcome remains auditable when overridden;
- safety revocation invalidates dependent plan authority immediately rather than waiting for cache TTL;

**Sensitive-data classification:** HEALTH / SAFETY-CRITICAL.

**External dependencies:**

- professional/clinical authority supplies approved rules; urgent-help external services are referenced through approved content, not monitored by platform;

**Cross-domain dependencies:**

- Health Records supplies facts;
- Identity & Access supplies actor context;
- Privacy & Consent supplies processing/share authority;
- Professional Care supplies review/clearance outcomes through governed commands;
- Plans & Nutrition must consume current Safety authority;

**Principal unresolved gates:**

- OQ-005 clinical eligibility matrix;
- OQ-008 urgent-help wording;
- OQ-025 Nuwe Jy safety/completion thresholds where relevant;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority. |
| Hot / warm / cold | Current eligibility/safety state is hot in business importance but durable in PostgreSQL; safe projections may be warm/hot only with immediate invalidation/bypass. |
| Transaction / concurrency sensitivity | VERY HIGH correctness sensitivity when new health facts, reviews and plan actions race. |
| Major scaling risks | mass re-evaluation after rule changes, safety fan-out to plans/programmes, current-state read pressure. |
| Redis | NONE initially for authority; only proven acceleration/coordination with fail-closed semantics where required. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable approved rule metadata, never participant safety truth. |
| GenServer | NONE initially. |
| PubSub | APPLICABLE for freshness/invalidation after safety transitions; authoritative consumers still re-read. |
| Oban | APPLICABLE for durable downstream re-evaluation/fan-out where not required synchronously. |
| Replica relevance | NONE for safety decisions. |
| Streaming / pagination | Pagination/streaming relevant for operational review queues; individual evaluations use bounded input. |


### 6.6 — Plans & Nutrition

**Product Law basis:** `DEC-096...DEC-122; DEC-038; DEC-042; DEC-216; DEC-276`

**Purpose:** Own deterministic personalised plan generation, immutable plan versions, review/adjustment lifecycle and nutrition-plan decision provenance under approved protocols.

**Owns:**

- plan generation request/outcome and immutable delivered plan snapshot;
- plan lifecycle and activation state;
- approved calculation/protocol version references and internal generation trace;
- plan reviews/adjustments and linked superseding versions;
- practitioner-derived plan versions once accepted into the platform plan history;
- shopping-list/recipe selections as part of immutable delivered plan provenance where applicable;

**Explicitly does not own:**

- source health facts;
- safety eligibility authority;
- temperament assessment truth;
- commercial entitlement to receive/review a plan;
- editorial recipe/content master versions outside the delivered plan snapshot;

**Major concepts/entities:**

- Plan;
- Plan Version;
- Generation Request;
- Plan Protocol Version;
- Plan Review;
- Adjustment Outcome;
- Practitioner-derived Plan;
- Plan Correction/Withdrawal;

**Major lifecycle/state:** pending → generated → review/approval/scheduled → active → safety_paused/completed → superseded/withdrawn; every material generation/adjustment creates an immutable linked version.

**Domain capabilities:**

- generate deterministic plan from approved current inputs;
- explain plan decisions/provenance;
- activate/revalidate plan;
- review/adjust within approved rules;
- accept practitioner-authored/modified version;
- issue correction/replacement/withdrawal without erasing history;

**Key policies:**

- generation fails closed; no partial plan/double charging;
- temperament changes delivery/presentation, never nutritional/safety truth;
- current Safety authority is revalidated at required boundaries;
- weight alone never drives adjustment;

**Key invariants/data-integrity rules:**

- delivered plan is reproducible from captured input/protocol/content/version references;
- one governed generation identity cannot create duplicate durable plan effects;
- new versions supersede rather than mutate historical delivered plans;
- safety pause prevents new unsafe adjustments while retaining history;

**Sensitive-data classification:** HEALTH + PAID PERSONALISED CONTENT.

**External dependencies:**

- approved clinical/nutrition methodology authority; Content & Media for governed recipe/instruction content;

**Cross-domain dependencies:**

- Safety & Eligibility;
- Health Records;
- Temperament;
- Entitlements;
- Content & Media;
- Professional Care for reviewed changes;
- Habits, Journals & Progress for approved review inputs;

**Principal unresolved gates:**

- OQ-003/OQ-012 monthly review contract/timing;
- OQ-010 calculation values;
- OQ-011 adjustment thresholds;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority for plan/version/provenance; protected object storage only for generated export artifacts if used. |
| Hot / warm / cold | Cold/durable plan history; current-plan view may be warm/hot projection with immediate safety invalidation. |
| Transaction / concurrency sensitivity | HIGH for duplicate generation, review entitlement use, simultaneous safety change and adjustment. |
| Major scaling risks | generation bursts, recipe/content joins, immutable history, monthly review waves. |
| Redis | NONE initially; potentially useful only for proven non-authoritative generation/read acceleration. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable approved calculation metadata/content lookup acceleration. |
| GenServer | NONE initially. |
| PubSub | APPLICABLE for plan-current-state freshness after generation/adjustment/safety pause. |
| Oban | POTENTIALLY_APPLICABLE for heavy non-immediate generation/export/fan-out when business confirmation semantics permit. |
| Replica relevance | NONE for current generation/safety decisions; historical library/reporting may later tolerate replicas. |
| Streaming / pagination | Pagination relevant for plan history; generation must remain bounded and stream large exports if introduced. |


### 6.7 — Content & Media

**Product Law basis:** `DEC-123...DEC-146; DEC-188...DEC-190; DEC-293 message/page experiment content boundary; DEC-296 published Interactive Tool presentation boundary only`

**Purpose:** Own governed runtime content, translations, taxonomy, publication, public/private discovery metadata and editorial/media version lineage.

**Owns:**

- conceptual content identity and immutable content versions;
- locale branches/translations and approval/publication lifecycle;
- content risk classification, approvals, corrections/withdrawals and attribution;
- taxonomy and authoritative search/discovery metadata source;
- governed editorial media identity, rights, derivatives and publication state;
- message/template content versions; exact delivery belongs Communications;
- published Interactive Tool editorial/presentation artifacts, copy, explanatory content and bounded presentation/configuration only where that meaning is genuinely Content publication;

**Explicitly does not own:**

- user-specific feed authority as independent durable business truth; feeds are derived from approved signals;
- participant health records or private journal assets;
- live-session/event registration/ticket truth;
- notification delivery attempts;
- experiment assignment/exposure truth;
- Interactive Tool calculation algorithms, consequential decision logic, Health calculations, Plan protocols, Safety rules or business-authoritative tool results; publication of UI/explanation does not transfer those authorities;
- participant Research responses, ballots, official voting results or Platform Member Reference;

**Major concepts/entities:**

- Content Item;
- Content Version;
- Locale Version;
- Approval;
- Publication;
- Correction/Withdrawal;
- Taxonomy;
- Media Asset;
- Media Derivative;
- Template Version;

**Major lifecycle/state:** draft/machine-draft/review/approved/published → superseded/withdrawn; locale branches advance independently subject to risk rules; published governed versions are immutable.

**Domain capabilities:**

- author/review/approve/publish governed content;
- manage translations/fallback rules;
- schedule publication through durable business schedule;
- manage taxonomy/search source metadata;
- manage governed media derivatives/protected publication;
- withdraw/correct content and trigger downstream invalidation;

**Key policies:**

- paid/safety/clinical/core onboarding content requires approved bilingual variants;
- machine translation never self-publishes where human approval is required;
- critical content cannot silently fallback;
- protected/private content is policy-checked before bounded delivery;
- search/discovery remains projection, not authority;

**Key invariants/data-integrity rules:**

- every delivered governed version retains exact content/locale provenance;
- published versions are immutable; corrections supersede/withdraw;
- private/paid content cannot leak through public cache/search;
- media derivatives preserve lineage and deletion/withdrawal propagation;

**Sensitive-data classification:** PUBLIC through SENSITIVE/CLINICAL/LEGAL depending content risk; media may be protected.

**External dependencies:**

- object storage/CDN/Cloudflare;
- Restream/Cloudflare Stream or future media providers behind provider boundary;

**Cross-domain dependencies:**

- Identity & Access/Entitlements for protected access;
- Privacy & Consent for personalised/marketing purposes where applicable;
- Safety & Eligibility for safety-sensitive content withdrawal;
- Analytics for derived content performance only;

**Principal unresolved gates:**

- OQ-013 translation resource model;
- OQ-014 edge/cache design;
- OQ-015 search configuration;
- OQ-016 scheduled publication operations;
- OQ-020/OQ-021 live/video and recording validation where media intersects live;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable content/media metadata authority + external object storage for bytes. |
| Hot / warm / cold | Cold/durable versions; hot/warm public metadata/taxonomy/search projections and CDN content where safe. |
| Transaction / concurrency sensitivity | Moderate; publication/correction/withdrawal correctness and cache invalidation are sensitive. |
| Major scaling risks | public read fan-out, search, media delivery, scheduled publication bursts, cache stampede. |
| Redis | POTENTIALLY_APPLICABLE for proven shared read acceleration/invalidation coordination, never publication authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable taxonomy/config/content metadata hot reads. |
| GenServer | NONE initially. |
| PubSub | APPLICABLE for publication/withdrawal freshness and LiveView refresh. |
| Oban | APPLICABLE for scheduled publication, media processing, search/projection refresh and fan-out consequences. |
| Replica relevance | POTENTIALLY_APPLICABLE for explicitly stale-tolerant discovery/reporting reads when evidence warrants. |
| Streaming / pagination | Streaming/pagination relevant for media delivery, search results and large content/admin lists. |


### 6.8 — Programmes & Challenges

**Product Law basis:** `DEC-147...DEC-157; DEC-183...DEC-185; DEC-196...DEC-219; DEC-274; DEC-286`

**Purpose:** Own reusable structured participation products: programmes, editions/cohorts, enrolments/progression/completion and challenge definitions/participation, including Nuwe Jy as a configured flagship experience rather than a separate engine.

**Owns:**

- programme definitions/versions/modules/lessons/activity structure references;
- programme lifecycle and delivery-mode configuration;
- edition/cohort schedule and enrolment lifecycle;
- progression/prerequisite/completion rule configuration and completion/certificate outcome;
- challenge definitions/modes, eligibility/completion/safety configuration and participation;
- Nuwe Jy edition/day schedule/configuration and repeat-enrolment history;

**Explicitly does not own:**

- lesson/content body versions;
- participant journal/habit occurrence truth;
- commercial entitlement or payment;
- community posts/moderation;
- live-session registration/tickets;
- central plan/safety engines;
- governed voting/balloting globally; a competition may compose Voting & Balloting with this Domain, but surface location does not transfer vote ownership;

**Major concepts/entities:**

- Programme;
- Programme Version;
- Module;
- Lesson Reference;
- Activity Definition;
- Edition;
- Cohort;
- Enrolment;
- Challenge;
- Challenge Participation;
- Completion/Certificate;

**Major lifecycle/state:** programme draft/internal/pilot/public/paused/retired; version immutable for active enrolment unless governed migration; enrolment active/paused/restarted/completed; challenge participation follows explicit configured eligibility/completion/safety lifecycle.

**Domain capabilities:**

- configure/publish programme/challenge versions;
- create/activate editions/cohorts;
- enrol/pace/progress participants;
- release scheduled daily/programme availability;
- evaluate participation/completion under versioned rules;
- support catch-up/recovery/repeat participation;

**Key policies:**

- missed days do not erase progress;
- temperament affects behavioural delivery only;
- challenge metrics cannot create public weight/calorie/body competition;
- Nuwe Jy reuses central Safety, Plans, Community, Events/Live and Communications capabilities;

**Key invariants/data-integrity rules:**

- active enrolment remains tied to its programme/version unless governed migration/safety correction;
- completion cannot require weight loss/perfect adherence/uninterrupted streaks;
- challenge/programme participation never becomes commercial entitlement authority;
- Nuwe Jy does not create a separate nutrition or identity engine;

**Sensitive-data classification:** PERSONAL PARTICIPATION; may reference health/safety state but should minimise copied health data.

**External dependencies:**

- legacy LearnDash only as retirement obligation; no importer/domain authority;

**Cross-domain dependencies:**

- Entitlements for access;
- Content & Media for lesson/content versions;
- Safety & Eligibility for activity/path restrictions;
- Habits, Journals & Progress for participant activity evidence;
- Community for cohort social space;
- Events & Live for sessions;
- Communications for scheduled messages;

**Principal unresolved gates:**

- OQ-019 programme-specific completion metrics;
- OQ-024 Nuwe Jy source-content/media inventory;
- OQ-025 Nuwe Jy thresholds;
- OQ-026 Nuwe Jy operational capacity;
- OQ-028 LearnDash obligations/retirement;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority. |
| Hot / warm / cold | Cold/durable programme/enrolment history; current Today/release/enrolment views may be warm/hot projections. |
| Transaction / concurrency sensitivity | Moderate-to-high for mass releases, enrolment, completion and scheduled cohort transitions. |
| Major scaling risks | scheduled release fan-out, cohort peaks, progress reads, large programme histories. |
| Redis | POTENTIALLY_APPLICABLE for proven cohort/release/read acceleration, never enrolment/completion authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable active programme/version metadata. |
| GenServer | NONE initially; only if hot cohort aggregation later proves useful. |
| PubSub | APPLICABLE for release/progress freshness. |
| Oban | APPLICABLE for scheduled releases and durable fan-out/communications consequences. |
| Replica relevance | POTENTIALLY_APPLICABLE for stale-tolerant catalogue/reporting reads later. |
| Streaming / pagination | Pagination relevant for cohorts/enrolments/progress; mass fan-out must be bounded/batched. |


### 6.9 — Habits, Journals & Progress

**Product Law basis:** `DEC-158...DEC-169; DEC-087...DEC-088; DEC-214; DEC-296 narrow educational/self-tracking Interactive Tool result boundary`

**Purpose:** Own participant self-tracking and reflective journey truth that is not itself a clinical health record: habits, occurrences, journals, behavioural progress, reflections and compassionate progress recognition.

**Owns:**

- habit catalogue entries allowed by Product Law, participant habits and practitioner-assigned habit references;
- habit schedules and occurrence states;
- private journal entries/attachments metadata and entry-specific sharing state;
- behavioural/adherence/progress entries and lightweight programme check-in responses not owned as health facts;
- private milestones/badges/certificates evidence where this domain is the progress source;
- Account-linked Interactive Tool results only when their business meaning is genuinely participant self-tracking, behavioural progress or reflective/non-clinical personal progress and that meaning fits this Domain's lifecycle;

**Explicitly does not own:**

- clinical health/lab/medication facts;
- programme/challenge definition or completion rules;
- plan adjustment decision;
- practitioner professional record copy of shared material;
- notification delivery/reminder sending;
- generic persisted Interactive Tool results merely because they are not obviously clinical; Health, Plans, Safety, Identity or another purpose owner remains authoritative where the result's meaning belongs there; transient/public/anonymous calculations are not this Domain's truth;

**Major concepts/entities:**

- Habit;
- Habit Schedule;
- Habit Occurrence;
- Journal Entry;
- Reflection;
- Progress Entry;
- Milestone;
- Sharing Grant Reference;

**Major lifecycle/state:** habit active/paused/retired with scheduled occurrences; occurrences pending/completed/partial/skip/missed/not-applicable/safety-blocked; journals private by default and deleted/shared only under explicit rules; progress accumulates without punitive reset.

**Domain capabilities:**

- create/schedule/record habits;
- record private journal/reflection;
- record lightweight progress/adherence;
- share selected entries under scoped consent;
- calculate compassionate consistency/progress indicators;
- supply approved review inputs to Plans/Programmes;

**Key policies:**

- journal private by default; no promise of continuous free-text monitoring;
- AI journal assistance remains deferred and participant-initiated if ever enabled;
- no streak/reset/shame mechanics that contradict compassionate consistency;
- health-sensitive responses that materially affect safety must route to Health Records/Safety rather than remain hidden here;

**Key invariants/data-integrity rules:**

- missed day never erases historical progress;
- journal sharing is entry-specific/scoped/revocable and does not grant general record access;
- private journal text is excluded from analytics by default;
- behavioural progress cannot masquerade as clinical safety authority;

**Sensitive-data classification:** PRIVATE JOURNAL + PERSONAL BEHAVIOURAL DATA; some entries may become health-sensitive.

**External dependencies:**

- object storage for journal/progress images only under protected asset rules;

**Cross-domain dependencies:**

- Identity & Access;
- Privacy & Consent;
- Safety & Eligibility for safety-blocked activity state;
- Programmes & Challenges;
- Plans & Nutrition;
- Communications for reminders;

**Principal unresolved gates:**

- OQ-017 reminder delivery design;
- OQ-018 journal encryption/retention;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority; protected object storage for optional attachments/photos. |
| Hot / warm / cold | Cold/durable history; current habit schedule/today progress may be warm/hot projection. |
| Transaction / concurrency sensitivity | Moderate; duplicate occurrence/check-in submission and share/revoke races matter. |
| Major scaling risks | daily habit/check-in write volume, journal history, reminder fan-out, participant dashboards. |
| Redis | NONE initially; potentially useful for non-authoritative current-progress counters if proven. |
| ETS / Cachex | NONE for private participant data; immutable habit metadata may later be cached. |
| GenServer | NONE initially. |
| PubSub | POTENTIALLY_APPLICABLE for progress/today freshness. |
| Oban | POTENTIALLY_APPLICABLE for reminder scheduling consequences and derived progress calculations. |
| Replica relevance | NONE for current participant truth; stale-tolerant historical reporting may use projections. |
| Streaming / pagination | Pagination/streaming relevant for journals/progress histories and export. |


### 6.10 — Commerce

**Product Law basis:** `DEC-029...DEC-050; DEC-192...DEC-194 payment intersection; DEC-231; DEC-258; DEC-273; DEC-282...DEC-284; DEC-292`

**Purpose:** Own the commercial contract: product catalogue/pricing/offers, purchase/payment/refund/subscription/membership billing truth and provider reconciliation independent of access entitlement.

**Owns:**

- commercial product/catalogue lifecycle and versioned prices/offers/discounts;
- purchase/order and purchaser/recipient commercial relationship;
- payment attempt/transaction state, verified provider evidence, refunds/disputes/settlement reconciliation;
- membership/subscription/add-on commercial contract, billing period and cancellation/upgrade/downgrade state;
- commercial gift/sponsor purchase records and financial retention state;
- Paystack adapter-facing reconciliation semantics while durable payment truth remains provider-independent;

**Explicitly does not own:**

- access entitlement itself;
- participant/private recipient journey;
- event ticket/capacity allocation;
- assessment/plan content;
- marketing consent;
- provider-reported state as unverified platform truth;

**Major concepts/entities:**

- Product;
- Offer/Price Version;
- Discount;
- Purchase/Order;
- Payment;
- Refund/Dispute;
- Subscription/Membership Contract;
- Billing Period;
- Commercial Gift/Sponsorship;

**Major lifecycle/state:** product draft/internal/pilot/public/paused/retired; purchase initiated → pending/verified-paid/failed/refunded/etc.; subscription active/grace/suspended/cancel-at-period-end/ended according to locked policy; provider ambiguity reconciles before irreversible success.

**Domain capabilities:**

- publish price/catalogue configuration;
- create checkout/purchase intent;
- verify/reconcile payment evidence;
- refund/reconcile disputes;
- manage membership/add-on billing lifecycle;
- emit durable access-grant/revoke intent to Entitlements after authoritative commercial transition;

**Key policies:**

- Paystack is launch gateway but not business authority;
- browser/provider return alone cannot create paid truth;
- failed payment follows governed grace/retry lifecycle without unsafe repeated charges;
- purchaser never receives recipient private health/plan/assessment data;

**Key invariants/data-integrity rules:**

- duplicate provider delivery cannot duplicate payment effect;
- timeout means unknown/pending, not success/failure;
- financial history is retained only under approved obligations and cannot reconstruct deleted participant access;
- membership contract and entitlement are separate truths;

**Sensitive-data classification:** FINANCIAL + PERSONAL; card secrets remain with provider boundaries, not platform domain data.

**External dependencies:**

- Paystack launch gateway; future gateways behind provider adapter;

**Cross-domain dependencies:**

- Identity & Access for purchaser actor;
- Privacy & Consent for commercial data lifecycle/marketing separation;
- Entitlements receives governed grant/revoke commands;
- Events & Live for event reservation/ticket checkout context;
- Audit & Evidence;

**Principal unresolved gates:**

- OQ-004 Paystack recurring/webhook/retry/proration/refund/chargeback validation;
- OQ-001 operating entity before production commercial scale;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority. |
| Hot / warm / cold | Cold/durable financial truth; current checkout/product-price reads may be warm/hot safe projections. |
| Transaction / concurrency sensitivity | VERY HIGH for checkout, duplicate callbacks, subscription transitions, refunds and flash-sale payment confirmation. |
| Major scaling risks | provider callback bursts, payment reconciliation, membership billing waves, checkout contention. |
| Redis | POTENTIALLY_APPLICABLE for abuse/temporary coordination only; never payment authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable product/price configuration reads. |
| GenServer | NONE initially. |
| PubSub | POTENTIALLY_APPLICABLE for payment/checkout UI freshness only. |
| Oban | APPLICABLE for durable reconciliation/retry/follow-up consequences under provider-safe rules. |
| Replica relevance | NONE for payment/current billing decisions; financial reporting may later use replicas/projections. |
| Streaming / pagination | Pagination relevant for ledgers/reconciliation/admin; batch provider reconciliation must be bounded. |


### 6.11 — Entitlements

**Product Law basis:** `DEC-008; DEC-030...DEC-050 access semantics; DEC-150; DEC-171; DEC-186; DEC-225; DEC-257; DEC-284...DEC-285`

**Purpose:** Own durable rights to access products, reports, plans, memberships/add-ons, programmes, community, sessions or other governed capabilities independent of how the right was purchased or granted.

**Owns:**

- entitlement identity, scope, source/provenance, validity/expiry and revocation;
- bundle decomposition into explicit component entitlements;
- membership/add-on-derived access rights as consequences of commercial contract state;
- book/event/gift/sponsored/complimentary/lifetime access grants and access redemption codes;
- reassessment/review/adjustment credits or similar consumable rights where Product Law defines them;
- entitlement consumption/redemption/idempotency history;

**Explicitly does not own:**

- payment/subscription billing contract;
- the protected resource/content itself;
- event ticket/capacity reservation;
- identity or consent;
- technical feature flags used only for rollout;

**Major concepts/entities:**

- Entitlement;
- Grant;
- Grant Source;
- Access Scope;
- Redemption Code;
- Consumable Credit;
- Entitlement Consumption;
- Revocation/Expiry;

**Major lifecycle/state:** granted → active → consumed/expired/revoked/ended while historical provenance remains; codes unredeemed → redeemed/expired/cancelled; membership-derived rights end according to commercial contract while purchased durable rights persist until deletion/other law.

**Domain capabilities:**

- grant/revoke/expire entitlements;
- redeem access codes idempotently;
- consume limited credits;
- answer current access checks;
- reconcile commercial/product consequences without duplicating grants;

**Key policies:**

- one entitlement system, including Premium bundle components; no parallel bundle-entitlement engine;
- payer/recipient separation maintained;
- lifetime access always names explicit scope;
- access is current-policy checked; stale caches cannot override revocation;

**Key invariants/data-integrity rules:**

- at most one valid grant for a governed entitlement identity;
- duplicate payment/job/callback/redeem execution cannot multiply access;
- commercial payment success does not itself equal entitlement until authoritative grant transition;
- full deletion permanently removes participant access and retained finance cannot restore it;

**Sensitive-data classification:** PERSONAL + COMMERCIAL ACCESS METADATA; generally not health data.

**External dependencies:**

- none as authority; provider evidence arrives through Commerce;

**Cross-domain dependencies:**

- Commerce for purchased/subscription grant intent;
- Identity & Access for grantee identity;
- Privacy & Consent for deletion;
- all protected product domains query current entitlement through owning interface;

**Principal unresolved gates:**

- OQ-004 where payment-provider behaviour affects grant timing;
- OQ-035 exact redemption-abuse thresholds;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority. |
| Hot / warm / cold | Current entitlement checks are hot reads but durable authority remains PostgreSQL; safe acceleration requires immediate revocation bypass/invalidation. |
| Transaction / concurrency sensitivity | VERY HIGH for duplicate grants, redemptions, consumption and revocation races. |
| Major scaling risks | high-frequency protected access checks, campaign redemptions, membership lifecycle fan-out. |
| Redis | POTENTIALLY_APPLICABLE for distributed abuse controls/read acceleration only, not entitlement authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for safe current-access acceleration with version/revocation guardrails. |
| GenServer | NONE initially. |
| PubSub | APPLICABLE for entitlement freshness/invalidation only. |
| Oban | APPLICABLE for durable grant/revoke fan-out when not required in same authoritative transaction. |
| Replica relevance | NONE for current access decisions. |
| Streaming / pagination | Pagination relevant for entitlement libraries/admin history; access checks remain bounded. |


### 6.12 — Community

**Product Law basis:** `DEC-170...DEC-182; DEC-205; DEC-278`

**Purpose:** Own first-party community/group participation and moderation truth when native community is activated; external Facebook remains a launch channel, not permanent source of truth.

**Owns:**

- first-party community groups/spaces and participation state;
- member-selected community display profile fields/badges that are community-specific;
- posts/comments/replies when first-party community exists;
- moderation reports, triage/actions/sanctions/appeals and restricted moderation evidence linkage;
- community participation restrictions/suspension/ban state;

**Explicitly does not own:**

- canonical identity/profile;
- membership billing or entitlement;
- challenge/programme definition/progress;
- private health/journal data;
- Facebook as durable platform truth;
- governed voting/balloting truth merely because a vote is displayed on a Community surface;

**Major concepts/entities:**

- Community Space;
- Community Membership;
- Community Profile;
- Post/Comment;
- Moderation Report;
- Moderation Case;
- Sanction;
- Appeal;

**Major lifecycle/state:** space configured/active/archived; participation active/read-only/restricted/suspended/banned/ended; report → triage → review → action/appeal → closure.

**Domain capabilities:**

- join/leave/use entitled community;
- post/comment under group policy;
- report/moderate content;
- apply/appeal sanctions;
- preserve/anonymise content under deletion rules;

**Key policies:**

- moderated by design; highly sensitive health/private disclosures are warned/redirected;
- peer experience allowed but diagnosis/prescription/dangerous restriction prohibited;
- reporter identity protected;
- former membership ends active participation without blindly deleting independently authored context;

**Key invariants/data-integrity rules:**

- community participation cannot expose private account/health/plan/journal data by default;
- moderation authority is scoped and auditable;
- external Facebook group is not authoritative participant entitlement or moderation history for future native platform;

**Sensitive-data classification:** PERSONAL + USER-GENERATED CONTENT; moderation evidence may be sensitive.

**External dependencies:**

- Facebook during validation phase only; eventual native platform authority as activated;

**Cross-domain dependencies:**

- Identity & Access;
- Entitlements;
- Privacy & Consent;
- Programmes & Challenges for cohort association;
- Audit & Evidence for sensitive moderation actions;

**Principal unresolved gates:**

- OQ-023 Facebook moderation/privacy operating policy;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority for native community state; object storage for governed attachments if introduced. |
| Hot / warm / cold | Cold/durable moderation/history; current feeds/permissions may use warm/hot derived projections. |
| Transaction / concurrency sensitivity | Moderate-to-high for feeds, moderation races, sanctions and high-traffic cohort discussions. |
| Major scaling risks | feed fan-out, pagination, moderation queues, attachment delivery, hot threads. |
| Redis | POTENTIALLY_APPLICABLE for feed/read acceleration/rate controls when native community scale proves need. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable group policy/config metadata. |
| GenServer | NONE initially. |
| PubSub | APPLICABLE for realtime discussion freshness only. |
| Oban | POTENTIALLY_APPLICABLE for moderation notifications/fan-out/derived work. |
| Replica relevance | POTENTIALLY_APPLICABLE for stale-tolerant feed/search/reporting reads later. |
| Streaming / pagination | Pagination/streaming is essential for feeds, threads and moderation queues. |


### 6.13 — Events & Live

**Product Law basis:** `DEC-186...DEC-195; DEC-206; DEC-279`

**Purpose:** Own live-session/event scheduling, registration/capacity, event occurrence/policy, scarce reservations, tickets and attendance/check-in truth while delegating payment and general product/replay entitlement authority to their owners.

**Owns:**

- live session/event definitions, versions and occurrences;
- registration/capacity/waitlist state;
- event-specific policy version accepted before checkout;
- scarce inventory reservation/hold state and authoritative capacity allocation;
- ticket identity/lifecycle, ticket holder/attendee relationship and check-in/attendance;
- session/event recording notice/association; media bytes/publication remain Content & Media;

**Explicitly does not own:**

- payment/refund financial authority;
- general entitlement system (event ticket/admission authority remains Events & Live even if separate product/replay entitlements are checked through Entitlements);
- replay/media asset publication;
- community discussion;
- provider stream delivery state as business truth;

**Major concepts/entities:**

- Live Session;
- Event;
- Event Version;
- Occurrence;
- Registration;
- Waitlist;
- Reservation/Hold;
- Ticket Type;
- Ticket;
- Attendance/Check-in;
- Event Policy;

**Major lifecycle/state:** event draft/published/etc. as configured; hold available → reserved → confirmed/expired/released; ticket reservation/payment/issue/transfer/check-in/cancel/refund-credit/expire/void; session registration → attended/no-show with governed replay association.

**Domain capabilities:**

- schedule/publish occurrence;
- register/waitlist participants;
- create/expire/confirm capacity hold;
- issue/transfer/check-in ticket after required commercial/access evidence;
- apply versioned event policy;
- associate governed replay/attendance evidence;

**Key policies:**

- confirmed allocations never exceed authoritative capacity;
- purchaser/ticket holder/attendee remain distinct;
- provider capture/stream status cannot manufacture registration/ticket truth;
- recording notice/privacy controls are explicit;

**Key invariants/data-integrity rules:**

- confirmed allocations <= capacity with zero oversell;
- hold expiry/retry/duplicate checkout cannot duplicate confirmed allocation;
- payment confirmation and ticket issuance reconcile safely across crashes;
- event policy accepted is the exact version governing the transaction;

**Sensitive-data classification:** PERSONAL ATTENDANCE + COMMERCIAL linkage; potentially protected live participation.

**External dependencies:**

- Restream/Cloudflare Stream for transport/playback; Paystack only through Commerce;

**Cross-domain dependencies:**

- Commerce for payment/refund;
- Entitlements for access rights/replay eligibility;
- Identity & Access;
- Content & Media for replay/media;
- Communications for reminders/changes;
- Programmes & Challenges for linked cohort sessions;

**Principal unresolved gates:**

- OQ-020 Restream/Cloudflare validation;
- OQ-021 recording/video consent/retention;
- OQ-022 event reservation/performance architecture;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority for capacity/tickets/attendance; external media platform/object storage for streams/replays. |
| Hot / warm / cold | Capacity/hold state is hot and correctness-critical; durable authority remains governed by approved reservation protocol. |
| Transaction / concurrency sensitivity | EXTREME on scarce inventory/flash-sale paths. |
| Major scaling risks | flash sales, hold expiry, payment reconciliation, check-in bursts, live registration/connection fan-out. |
| Redis | POTENTIALLY_APPLICABLE for proven temporary reservation/queue/rate coordination only under explicit crash/failure contract; not final ticket authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable event configuration/availability projection. |
| GenServer | POTENTIALLY_APPLICABLE only for hot aggregation/coordination proven safe; never sole reservation authority. |
| PubSub | APPLICABLE for capacity/waitlist/check-in freshness. |
| Oban | APPLICABLE for hold expiry, reconciliation and event communication/fan-out. |
| Replica relevance | NONE for capacity/hold/ticket confirmation; stale-tolerant event catalogue/reporting may later use replicas. |
| Streaming / pagination | Pagination/streaming relevant for attendee/ticket lists; high-volume check-in/exports must be bounded. |


### 6.14 — Professional Care

**Product Law basis:** `DEC-011...DEC-012; DEC-024...DEC-025; DEC-091...DEC-093; DEC-117; DEC-229; DEC-277; DEC-287`

**Purpose:** Own practitioner-specific professional relationships, review/case workflow, platform-held professional record/provenance handling and care outcomes while reusing canonical identity, consent, health, safety and plan domains; final legal/professional recordkeeper authority remains governed by OQ-033.

**Owns:**

- practitioner professional profile/relationship metadata beyond canonical identity role;
- active participant-practitioner care/review relationship and scope/expiry reference;
- professional review/case lifecycle and structured review outcomes;
- platform-held professional-care case/record set and provenance; OQ-033 determines the final legal/professional record authority, participant-access boundary and disposition;
- practitioner workload/saleable-capacity state and external referral record;
- professional recommendation/change request that is then enacted through owning Safety/Plans interfaces;

**Explicitly does not own:**

- canonical login identity/role grant;
- participant consent grant;
- self-guided health record;
- final Safety eligibility truth;
- plan version authority once a practitioner-derived plan is accepted into Plans;
- commercial payment for the service;

**Major concepts/entities:**

- Practitioner Profile;
- Care/Review Relationship;
- Professional Review Case;
- Platform Professional Record / External Record Reference;
- Review Outcome;
- Referral;
- Capacity Allocation;

**Major lifecycle/state:** relationship proposed/consented/active/expired/revoked; review requested → triage/under-review → outcome/follow-up/closed/referral; platform professional records corrected additively and retained under expert-approved rules; an external practitioner record may remain externally authoritative where OQ-033 so determines.

**Domain capabilities:**

- establish/expire care relationship;
- perform structured professional review;
- record professional outcome/restriction/referral;
- request Safety override/clearance through owner;
- author/approve practitioner plan change through Plans;
- manage practitioner capacity and saleability;

**Key policies:**

- access requires consent + active relationship + scope + expiry + audit;
- staff/practitioner MFA mandatory;
- professional records may survive product deletion only where legally/ethically required and are isolated; OQ-033 may establish an external practitioner/entity as the professional record authority;
- capacity protection prevents unlimited member expectation;

**Key invariants/data-integrity rules:**

- professional role alone never grants participant-record access;
- revoked/expired relationship ends future platform access;
- professional record authority cannot silently alter self-guided source history or raw assessment result;
- practitioner changes create explicit downstream owned versions rather than direct cross-domain writes;

**Sensitive-data classification:** PROFESSIONAL + HEALTH / HIGHLY SENSITIVE.

**External dependencies:**

- external referral partners and potentially contracted/employed practitioners under different legal relationships;

**Cross-domain dependencies:**

- Identity & Access;
- Privacy & Consent;
- Health Records;
- Safety & Eligibility;
- Plans & Nutrition;
- Commerce/Entitlements for purchased review access;
- Audit & Evidence;

**Principal unresolved gates:**

- OQ-001 operating entity/contracts;
- OQ-009/OQ-029 retention;
- OQ-033 professional record authority;
- clinical gates relevant to reviewed pathway;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority; protected object storage for professional attachments if required. |
| Hot / warm / cold | Cold/durable professional records/cases; current review queue may be warm projection. |
| Transaction / concurrency sensitivity | HIGH sensitivity for access revocation, review outcomes, capacity and simultaneous Safety/Plan changes. |
| Major scaling risks | professional queue/capacity constraints more important than raw throughput; protect scarce reviewer capacity. |
| Redis | NONE initially. |
| ETS / Cachex | NONE for participant/professional records. |
| GenServer | NONE initially. |
| PubSub | POTENTIALLY_APPLICABLE for case/queue freshness only. |
| Oban | APPLICABLE for review notifications, follow-up and durable downstream consequences. |
| Replica relevance | NONE for care/access decisions; stale-tolerant operational reporting may later use replica/projection. |
| Streaming / pagination | Pagination relevant for case queues/records; exports must remain bounded/protected. |


### 6.15 — Communications

**Product Law basis:** `DEC-017 mailing-list allowance; DEC-162; DEC-218; DEC-261...DEC-263`

**Purpose:** Own outbound/in-app communication intent, subscriber contacts, channel/category preferences and durable delivery lifecycle while purpose permission and originating business events remain with their respective owners.

**Owns:**

- mailing-list/subscriber communication contact state for people without full accounts, linked/reconciled when appropriate;
- notification and marketing channel/category preferences, quiet hours and frequency caps;
- durable message/notification intent and deduplication identity;
- delivery attempts/status/provider evidence and terminal-visible failure;
- in-app notification/inbox state where introduced;
- scheduled communication journey configuration that is communication-specific, referencing governed content versions;

**Explicitly does not own:**

- marketing consent/lawful basis;
- canonical account email;
- template/content body versions;
- the originating business fact such as payment, safety, programme release or event change;
- provider delivery/open/click observations as authoritative business conversion;

**Major concepts/entities:**

- Subscriber Contact;
- Notification Preference;
- Message Intent;
- Delivery Attempt;
- Channel;
- In-app Notification;
- Communication Journey;

**Major lifecycle/state:** intent created durably → queued → sent/delivered/failed/retried/terminal; each channel/category preference is independently active/paused/changed; subscriber contact lifecycle remains distinct from Privacy & Consent purpose permission. A scoped opt-out changes the selected Communications preference only; purpose-level withdrawal is requested through Privacy & Consent.

**Domain capabilities:**

- create deduplicated durable communication intent;
- select allowed channel from current preference/mandatory rules;
- deliver/retry through providers;
- record provider evidence;
- respect quiet hours/frequency caps;
- surface terminal failures and in-app notices;

**Key policies:**

- email + in-app first; SMS/WhatsApp later; push deferred;
- marketing consent is separate from product/safety mandatory notices; channel/category opt-out changes only Communications preference; an explicit purpose-withdrawal request is committed only by Privacy & Consent;
- Communications may not directly mutate Privacy & Consent persistence;
- provider subscription/unsubscribe state is external evidence and cannot establish or restore platform permission;
- accountless contact linking cannot create, transfer, broaden or restore purpose permission;
- provider delivery/engagement observation never rewrites originating business truth;
- sensitive payloads are minimised; templates are governed versions;

**Key invariants/data-integrity rules:**

- must-not-lose messages have durable intent before provider call;
- retry/duplicate execution cannot multiply logical communication beyond policy;
- preference/consent changes are re-evaluated before non-mandatory delivery where required;
- provider outage degrades communication, not payment/safety/entitlement truth;

**Sensitive-data classification:** PERSONAL CONTACT + potentially sensitive message metadata; avoid embedding raw health data.

**External dependencies:**

- email provider initially; future SMS/WhatsApp providers behind channel adapters;

**Cross-domain dependencies:**

- Content & Media for template versions;
- Privacy & Consent for purpose-level permission and owner-mediated withdrawal requests;
- Identity & Access for account destinations;
- all business domains may request communication through the owner interface;
- Analytics may consume minimum delivery/engagement observations;

**Principal unresolved gates:**

- OQ-017 reminder delivery design;
- OQ-027 Nuwe Jy communication configuration;
- OQ-036 notification providers/channel policy;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable intent/delivery authority via Oban-backed execution; provider evidence stored minimally. |
| Hot / warm / cold | Current preferences/in-app unread state may be warm/hot; durable delivery history cold. |
| Transaction / concurrency sensitivity | Moderate-to-high for campaign/programme release fan-out, deduplication and retry storms. |
| Major scaling risks | burst fan-out, provider rate limits, backlog recovery, quiet-hour scheduling. |
| Redis | POTENTIALLY_APPLICABLE for provider rate-control/temporary counters where justified, not delivery authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable channel/config/template metadata. |
| GenServer | NONE initially. |
| PubSub | POTENTIALLY_APPLICABLE for in-app notification freshness. |
| Oban | CORE/APPLICABLE — default durable execution mechanism. |
| Replica relevance | NONE for send/preference decisions; historical reporting may use analytics/projections. |
| Streaming / pagination | Batch/fan-out must be bounded; pagination relevant for inbox/history/admin. |


### 6.16 — Experimentation

**Product Law basis:** `DEC-293; Architecture ARC-177...ARC-188 and ARC-325/327 synthesis doctrine`

**Purpose:** Own governed first-party experiment configuration, deterministic assignment authority, treatment lifecycle and immutable decision/learning record without becoming a feature-flag or business-truth bypass.

**Owns:**

- experiment identity/configuration/version, variants, eligibility/protected-invariant exclusions and activation state;
- deterministic sticky assignment decision/provenance for eligible subjects;
- canonical exposure contract/definition and experiment measurement specification;
- experiment stop/decision record and immutable historical learning/result snapshot derived from approved evidence;

**Explicitly does not own:**

- underlying page/email content version;
- business conversion/payment/entitlement truth;
- general analytics event store/aggregates;
- feature rollout flags unrelated to experiments;
- raw health data for assignment by default;
- Research/Feedback campaigns, instruments, participant submissions, withdrawal/correction lifecycle or research findings authority;

**Major concepts/entities:**

- Experiment;
- Experiment Version;
- Variant;
- Assignment;
- Exposure Definition;
- Metric Definition;
- Experiment Decision/Result;

**Major lifecycle/state:** draft → reviewed/approved → activated immutable version → running/paused/stopped/completed; assignment sticky per approved identity; decision/result preserved historically.

**Domain capabilities:**

- configure/approve/activate experiment;
- assign deterministically;
- resolve anonymous-to-known continuity under approved rules;
- define exposure/metric semantics;
- stop/decide experiment using Analytics evidence;
- preserve historical learning/searchability;

**Key policies:**

- experiments cannot alter protected safety/payment/entitlement/accounting invariants;
- canonical public URLs remain clean; variant-sensitive caching is isolated/bypassed;
- assignment != exposure;
- experiment failure cannot corrupt unrelated authoritative operations;

**Key invariants/data-integrity rules:**

- activated experiment config/version is immutable;
- same governed subject+experiment identity yields stable assignment under the versioned algorithm;
- business conversion comes from authoritative source-domain facts, not client event assertion;
- material unexplained sample-ratio mismatch blocks validity/decision;

**Sensitive-data classification:** PERSONALISATION/ANALYTICS metadata; assignment must minimise identity and health detail.

**External dependencies:**

- none required as authority; implementation package/statistics remain proof-gated;

**Cross-domain dependencies:**

- Content & Media and Communications for eligible treatment content;
- Analytics for exposure/outcome aggregates and statistical evidence;
- Privacy & Consent for purpose/deletion rules;
- Identity & Access for known-subject continuity where applicable;

**Principal unresolved gates:**

- OQ-040 first-party experimentation architecture proof;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable experiment/config/assignment/decision authority; analytics measurements remain Analytics-owned. |
| Hot / warm / cold | Active immutable config/assignment lookups may be hot/warm; historical learning cold. |
| Transaction / concurrency sensitivity | Moderate; deterministic concurrent assignment and anonymous-known reconciliation are correctness-sensitive. |
| Major scaling risks | high-volume assignment/exposure traffic, concurrent experiments, cache partitioning, analytics lag. |
| Redis | NONE initially for authority; potential acceleration only if assignment semantics remain deterministic/rebuildable. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable active experiment configuration. |
| GenServer | NONE. |
| PubSub | POTENTIALLY_APPLICABLE for activation/stop freshness only. |
| Oban | POTENTIALLY_APPLICABLE for analysis/rebuild/finalisation consequences. |
| Replica relevance | POTENTIALLY_APPLICABLE for historical experiment browsing; not assignment authority. |
| Streaming / pagination | Pagination relevant for experiment history; measurement evidence handled through Analytics pipelines. |


### 6.17 — Analytics

**Product Law basis:** `DEC-072; DEC-122; DEC-145; DEC-169; DEC-195; DEC-219; DEC-235; DEC-267; DEC-289...DEC-290; DEC-293`

**Purpose:** Own governed analytical observations, derived facts/projections, aggregates, dashboards and measurement pipelines while remaining downstream of authoritative business domains.

**Owns:**

- governed product/behaviour/operational analytical event facts as permitted;
- derived read models/materialised aggregates and analytical dimensions;
- acquisition evidence and attribution interpretations as separate analytical concepts;
- dashboard/report/export analytical projections;
- experiment exposure/outcome measurement facts and aggregates under Experimentation definitions;
- real-time business/product aggregate metric state where business authority is not implied; generic infrastructure observability remains Architecture/Operations;

**Explicitly does not own:**

- payment, entitlement, safety, plan, identity, consent or other source-domain business truth;
- experiment configuration/assignment/final governed decision;
- audit/security evidence;
- raw journal text or unnecessary health detail;
- Research responses, accepted vote tally, official voting result, Platform Member Reference or consequential Interactive Tool result merely because they can be analysed or shown on a dashboard;

**Major concepts/entities:**

- Analytical Event/Fact;
- Projection;
- Aggregate;
- Metric;
- Acquisition Evidence;
- Attribution Model;
- Dashboard;
- Experiment Measurement;

**Major lifecycle/state:** source-domain fact/observation accepted under governed schema → projected/aggregated → refreshed/rebuilt/backfilled → retained/anonymised/deleted according to privacy policy; derived models are rebuildable.

**Domain capabilities:**

- ingest governed minimum analytical facts;
- build/rebuild aggregates/read models;
- serve dashboards/reports;
- measure funnels/outcomes;
- support experiment measurement/statistical evidence;
- remove/suppress identifiable analytics on deletion;

**Key policies:**

- business-material facts originate from authoritative state where applicable;
- no peak-time full scans of large OLTP tables;
- analytics freshness degrades before critical OLTP correctness;
- privacy minimisation excludes journal text/raw clinical data by default;

**Key invariants/data-integrity rules:**

- derived projection can be rebuilt and never becomes write authority for source domain;
- deletion/suppression rules apply to rebuilds/backfills;
- provider analytics reports remain external evidence;
- experiment SRM/validity blockers are surfaced rather than hidden;

**Sensitive-data classification:** DERIVED PERSONAL/BEHAVIOURAL DATA; may become sensitive by linkage, so minimise and govern access.

**External dependencies:**

- external analytics/provider reports as evidence only; optional warehouse/search tooling evidence-gated;

**Cross-domain dependencies:**

- all source domains publish/derive approved facts;
- Privacy & Consent governs deletion/minimisation;
- Experimentation supplies experiment measurement definitions;
- Audit & Evidence remains separate;

**Principal unresolved gates:**

- OQ-030/OQ-032 where external analytics processors participate in deletion/export;
- OQ-040 experiment measurement proof;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL-first derived models/materialised aggregates initially; other analytical stores/replicas only when evidence justifies. |
| Hot / warm / cold | Hot real-time counters may use approved in-memory/Redis; warm cached aggregates; cold durable facts/projections. |
| Transaction / concurrency sensitivity | Lower write-authority risk but high workload-isolation importance; backfills/exports must not starve OLTP. |
| Major scaling risks | event volume, large date ranges, dashboard concurrency, rebuild/backfill lag, experiment measurement. |
| Redis | POTENTIALLY_APPLICABLE for real-time counters/aggregates where rebuildable. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for node-local metric aggregation/config where safe. |
| GenServer | POTENTIALLY_APPLICABLE for hot bounded metric aggregation where proven. |
| PubSub | POTENTIALLY_APPLICABLE for dashboard freshness only. |
| Oban | APPLICABLE for aggregation, backfill, exports and pipeline recovery. |
| Replica relevance | POTENTIALLY_APPLICABLE / likely future for stale-tolerant analytical reads when evidence warrants. |
| Streaming / pagination | HIGH relevance for exports, backfills and large result sets; stream/batch instead of loading whole datasets. |


### 6.18 — Audit & Evidence

**Product Law basis:** `DEC-021/DEC-025 audit obligations; DEC-051; DEC-091; DEC-177...DEC-180; DEC-233...DEC-234; DEC-242; DEC-247...DEC-255; DEC-266...DEC-267; DEC-291`

**Purpose:** Own cross-cutting immutable/minimised audit and security evidence needed to prove sensitive actions, privileged access, incidents and governance without becoming the source of the business facts being audited.

**Owns:**

- append-only audit evidence for sensitive/domain-governed actions where central evidence is required;
- security/fraud event evidence under security-specific identifiers;
- break-glass/privilege-access evidence and review linkage;
- incident record/evidence linkage and release/go-no-go decision evidence where retained centrally;
- audit query/access controls and evidence retention-class metadata;

**Explicitly does not own:**

- the underlying business transition being audited;
- generic operational logs/metrics/traces;
- professional clinical record;
- payment/provider reconciliation evidence except minimal audit linkage;
- moderation case business state owned by Community;
- Research responses, official voting results or Platform Member Reference as business truth; those remain with their owning Domains while this Domain may append evidence that governed actions occurred;

**Major concepts/entities:**

- Audit Event;
- Security Event;
- Evidence Link;
- Privileged Access Evidence;
- Incident Record;
- Release Decision Evidence;
- Audit Retention Class;

**Major lifecycle/state:** evidence appended immutably → retained/restricted according to class → legal hold/approved expiry → deletion/anonymisation where lawful; corrections add superseding evidence rather than rewrite.

**Domain capabilities:**

- record sensitive action evidence;
- record security/privilege/break-glass events;
- correlate incidents/releases with evidence;
- serve restricted audit review/export;
- apply category-specific retention/access policy;

**Key policies:**

- minimum necessary evidence; do not duplicate full sensitive payloads;
- audit/security evidence separated from generic logs;
- access itself is privileged/audited;
- retention is category/purpose-specific and expert-governed where required;

**Key invariants/data-integrity rules:**

- audit evidence cannot be edited to rewrite history;
- absence/failure of telemetry cannot fabricate business success;
- audit store is not an alternate business API or source of entitlement/payment/safety truth;
- correlation identifiers must be safe and bounded in cardinality/privacy;

**Sensitive-data classification:** SECURITY + potentially PERSONAL/HEALTH metadata; highly restricted.

**External dependencies:**

- observability platforms may receive minimised operational telemetry, not replace Audit authority;

**Cross-domain dependencies:**

- all domains emit approved audit evidence through bounded interface;
- Privacy & Consent governs retention/deletion exceptions where lawful;
- Identity & Access supplies actor/system-causation context;

**Principal unresolved gates:**

- OQ-029 retention schedule;
- OQ-038 incident ownership where organisational responsibility is unresolved;

**Lightweight Domain Architecture Profile:**

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable append-only evidence authority; generic telemetry may use separate observability systems. |
| Hot / warm / cold | Cold/durable evidence; small security/risk summaries may be warm operational projections. |
| Transaction / concurrency sensitivity | Moderate write volume, high integrity; evidence recording must not silently disappear for mandatory actions. |
| Major scaling risks | high event volume/cardinality, retention depth, incident queries, security bursts. |
| Redis | NONE for evidence authority; potentially useful only for transient risk counters owned elsewhere. |
| ETS / Cachex | NONE for durable evidence; local telemetry aggregation belongs observability, not this domain truth. |
| GenServer | NONE. |
| PubSub | NONE for authority; optional operational freshness only. |
| Oban | POTENTIALLY_APPLICABLE for non-blocking evidence enrichment/export, not for losing mandatory audit intent. |
| Replica relevance | POTENTIALLY_APPLICABLE for restricted historical audit reads if consistency requirements permit. |
| Streaming / pagination | HIGH relevance for large audit exports/reviews; strict pagination/streaming and access controls. |



### 6.19 — Research & Feedback

**Product Law basis:** `DEC-294; DEC-298; archive/00_PLATFORM_v1.3.0.md §21M; ARC-328; ARC-329; ARC-331`

**Purpose:** Own the durable truth required to conduct bounded lightweight feedback and governed Research activities: campaign/study identity, declared purpose, participation identity/uniqueness contract, published instrument versions, participant submissions, correction/withdrawal/de-link and distinguishable staff annotation. This Domain is not a generic survey-builder, forms platform or shared Interactive Evidence store.

**Owns:**

- Research/feedback campaign or study identity, declared purpose and campaign lifecycle including draft, publication, closure and supersession;
- declared participation identity mode and the associated participation/uniqueness contract for that campaign/instrument;
- campaign-specific eligibility/cohort rule configuration as references to other Domains' truths, not copies of those truths;
- published Research/feedback instrument and immutable published instrument/question version;
- participant Research/feedback submission, including the exact producing instrument/question version;
- correction, withdrawal, de-linking/anonymisation state where approved, and Research-record retention/deletion interaction through this Domain's lifecycle;
- staff annotation/classification as evidence distinct from participant-submitted truth;

**Explicitly does not own:**

- canonical Account identity or Identity assurance;
- Privacy & Consent grants, lawful-basis state or deletion orchestration;
- authoritative Health facts, Safety decisions, Temperament truth or Plans;
- Commerce, Entitlements, Communications delivery or Professional Care cases;
- Analytics products or Audit evidence;
- published editorial Content artifacts (Content owns authorised publication of findings copy);
- generic Experimentation assignment/exposure/decision;
- Research polls' UI widgets, shared form primitives, or any vote whose purpose is a governed collective official result;

Persisted lightweight feedback belongs here only where Product purpose classifies it as Research/Feedback truth. Transient reactions or presentation-only interactions do not become durable records merely because a widget exists.

**Major concepts/entities:**

- Research Campaign/Study;
- Participation Identity Mode / Uniqueness Contract;
- Research Instrument Version;
- Participant Submission/Response;
- Correction/Withdrawal/De-link Record;
- Staff Annotation/Classification;

Exact Resource names remain JIT work.

**Major lifecycle/state:** campaign/instrument draft → approved → published/active with immutable published meaning → participating/collecting → closed, withdrawn or superseded. A material meaning or participation-mode change creates a new governed version rather than editing published meaning in place. Submission binds the producing version and declared identity-mode meaning. Correction, withdrawal, later interpretation and staff annotation add explicit relationship/supersession evidence and do not falsify the original participant submission. Genuine anonymous withdrawal limits remain honest. Duplicate, retried, reordered or recovered submissions are evaluated against durable campaign/instrument authority. Historical interpretation remains bound to the producing version. Privacy/deletion decisions enter through this Domain's record lifecycle; Account deletion does not automatically invalidate historically legitimate Research truth.

**Domain capabilities:**

- configure/publish/close/supersede governed Research/feedback campaigns and instruments;
- collect participant submissions under the declared participation contract;
- correct, withdraw or de-link eligible records without silent overwrite;
- distinguish staff annotation from participant truth;
- request owner-mediated follow-up, incentive, safety, care or publication consequences;

**Key policies:**

- Research/Feedback responses remain Research/Feedback truth and do not directly mutate Health, Safety, Plans, Temperament, Commerce or Entitlements;
- identity mode and uniqueness guarantee are separate promises; genuine anonymity cannot conceal Account linkage;
- a Research poll is Research truth even when the UI looks like a vote widget;
- incentives are never automatic and must be granted through Commerce/Entitlements;
- free-text submission does not create a universal continuous-monitoring promise;

**Key invariants/data-integrity rules:**

- every persisted response retains the exact producing instrument/question version and declared participation identity meaning;
- published instrument meaning is not edited in place;
- staff annotation cannot silently replace participant-submitted truth;
- targeting does not transfer ownership of source Health/Safety/Identity attributes to this Domain;

**Sensitive-data classification:** PERSONAL + potentially HEALTH-RELATED RESEARCH DATA; remains Research truth unless a separate owner-mediated action establishes another Domain's fact.

**External dependencies:**

- none as authority; later authoring/anti-abuse mechanisms remain JIT/evidence-gated;

**Cross-domain dependencies:**

- Identity & Access for Account-linked participation facts;
- Privacy & Consent for purpose-specific consent and deletion/retention orchestration;
- Content & Media for authorised publication of findings copy;
- Communications, Safety & Eligibility, Professional Care, Commerce and Entitlements for owner-mediated consequences;
- Analytics and Audit & Evidence for derived measurement and evidence only;

**Principal unresolved gates:**

- `ROADMAP_REVIEW_REQUIRED` for Feature Pack placement; this Domain amendment does not sequence launch;
- exact retention durations remain expert/legal/privacy gates;
- JIT Domain Dossier and Resource design remain downstream and are not started here;

**Lightweight Domain Architecture Profile:**

Authority ≠ acceleration. A new Domain does not justify Redis, ETS, GenServers, services or queues.

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority. |
| Hot / warm / cold | Cold/durable campaign, instrument and response history; current published-instrument metadata may be a warm projection with authoritative bypass. |
| Transaction / concurrency sensitivity | Moderate-to-high for concurrent submission, correction, withdrawal and duplicate/retry recovery. |
| Major scaling risks | campaign bursts, longitudinal history depth, deletion/de-link fan-out, export. |
| Redis | NONE initially for authority; potentially useful only for proven non-authoritative rate/integrity coordination. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable published instrument/version metadata, never participant responses. |
| GenServer | NONE initially. |
| PubSub | POTENTIALLY_APPLICABLE for campaign open/close freshness only. |
| Oban | POTENTIALLY_APPLICABLE for durable follow-up/consequence handoff and deletion-contract work. |
| Replica relevance | NONE for current campaign/response authority; stale-tolerant reporting may later use projections. |
| Streaming / pagination | Pagination/streaming relevant for response history, exports and admin review; ordinary collection remains bounded. |


### 6.20 — Voting & Balloting

**Product Law basis:** `DEC-295; DEC-298; archive/00_PLATFORM_v1.3.0.md §21N; ARC-328; ARC-329; ARC-332`

**Purpose:** Own the governed voting/balloting lifecycle required where eligibility, integrity, opening/closing, finality, official result or adjudication matter. The Domain name is **Voting & Balloting**. It does not own competitions as a whole, Community participation, Programme completion, Research polls, rewards or entitlements.

**Owns:**

- governed vote/poll rules, including eligibility, limits, changeability, open/close timing, visibility and uniqueness claims;
- ballot/submission and integrity disposition evidence, including submitted, accepted, rejected/invalidated and held/requires-review where used;
- accepted tally;
- governed finalisation;
- official result;
- exception, adjudication, correction and rerun/cancellation authority under approved rules;

Lightweight opinion polls whose persisted meaning is a collective displayed outcome belong here with a simpler lifecycle. A Research poll remains Research & Feedback truth even if the UI looks identical. A vote displayed in Community or a Programme remains this Domain's truth when the purpose is a governed collective outcome.

**Explicitly does not own:**

- Research polls or other Research/Feedback truth;
- general competition lifecycle, Programme enrolment/completion or Community participation/moderation;
- Safety restrictions; existing wellness/competition safety remains controlling;
- Account identity, Commerce, Entitlements or rewards/prizes/discounts;
- Analytics products, Audit evidence or publication Content;
- provisional leaderboards, caches or provider counts as official-result authority;

**Major concepts/entities:**

- Vote/Poll Rules;
- Ballot/Submission Evidence;
- Integrity Disposition;
- Accepted Tally;
- Finalisation Record;
- Official Result;
- Adjudication/Correction/Rerun Record;

These are logical dimensions, not a mandate for seven Resources, tables, columns, services or a universal status enum.

**Major lifecycle/state:** rules approved before opening; submissions move through applicable integrity dispositions; only accepted eligible evidence contributes to the governed tally; provisional counts/leaderboards are not official results; finalisation is a durable, auditable, idempotent, rule-tied transition; official result is published or explicitly corrected; ties, disqualification, material integrity failure, outage/disruption, cancellation, extension, rerun and adjudication follow approved exception policy and cannot invent a preferred winner after the fact. Duplicate, simultaneous, reordered or retried submissions and delayed reward handoffs recover from durable authority without creating duplicate financial or access truth. Individual voter identity and ballot choice are private by default. Account deletion does not automatically invalidate a historically legitimate vote, accepted tally, adjudicated outcome or official result.

**Domain capabilities:**

- publish and version governed vote rules;
- accept, hold, reject or invalidate submissions under those rules;
- maintain accepted tally distinct from provisional display;
- finalise, record official result and perform governed adjudication/correction/rerun;
- request owner-mediated reward/entitlement consequences without becoming commercial authority;

**Key policies:**

- purpose and consequence classify the operation, not widget shape or page location;
- public unauthenticated voting is a legitimate mode and does not imply verified one-human-one-vote;
- integrity assurance is not identity assurance;
- operators may not arbitrarily alter counts or choose a preferred winner outside approved rules;
- reward/discount/entitlement fulfilment is granted only through Commerce/Entitlements;

**Key invariants/data-integrity rules:**

- a provisional count cannot promote itself to official result;
- Analytics, leaderboards, caches and provider counts are not result authority;
- finalisation is restart/recovery-safe and does not invent a post-hoc winner;
- official-result correction is explicit and evidence-bearing and identifies affected dependent consequences;
- duplicate/retry of a reward handoff is deduplicated at the owning consequence boundary;

**Sensitive-data classification:** PERSONAL PARTICIPATION + BALLOT PRIVACY; voter identity and ballot choice are restricted by default.

**External dependencies:**

- none as authority; exact anti-abuse, CAPTCHA, device, cookie or threshold mechanisms remain downstream;

**Cross-domain dependencies:**

- Identity & Access for Account-linked participation facts and PMR non-requirement for approved public voting;
- Privacy & Consent for deletion/retention orchestration through this Domain's contract;
- Commerce and Entitlements for official-result consequences;
- Safety & Eligibility and Programmes & Challenges for existing wellness/competition restrictions that this Domain must not weaken;
- Community and Programmes as contextual surfaces only;
- Analytics and Audit & Evidence for derived presentation and evidence only;

**Principal unresolved gates:**

- `ROADMAP_REVIEW_REQUIRED` for Feature Pack placement; this Domain amendment does not sequence launch;
- exact anti-abuse thresholds remain OQ/JIT/security work;
- JIT Domain Dossier and Resource design remain downstream and are not started here;

**Lightweight Domain Architecture Profile:**

Authority ≠ acceleration. A new Domain does not justify Redis, ETS, GenServers, services or queues.

| Profile field | Phase-5 baseline |
|---|---|
| Authoritative storage | PostgreSQL durable authority. |
| Hot / warm / cold | Rules and official result are durable; current provisional display may be a warm/hot projection that never becomes result authority. |
| Transaction / concurrency sensitivity | HIGH for duplicate/simultaneous submissions, integrity disposition, finalisation and retry-safe consequence handoff. |
| Major scaling risks | public-vote bursts, duplicate storms, finalisation windows, leaderboard read pressure. |
| Redis | NONE initially for authority; POTENTIALLY_APPLICABLE only for proven non-authoritative rate/integrity coordination, never tally or official-result authority. |
| ETS / Cachex | POTENTIALLY_APPLICABLE for immutable published vote-rule metadata. |
| GenServer | NONE initially; never sole tally/result authority. |
| PubSub | POTENTIALLY_APPLICABLE for provisional-display freshness only. |
| Oban | POTENTIALLY_APPLICABLE for durable consequence handoff, adjudication follow-up and deletion-contract work. |
| Replica relevance | NONE for tally/finalisation/official-result authority; stale-tolerant leaderboard/reporting may later use projections. |
| Streaming / pagination | Pagination relevant for evidence review and admin adjudication; public collection paths remain bounded. |


## 7. Mature-platform capability coverage

| Approved capability family | Domain home(s) |
|---|---|
| Public/acquisition and bilingual discovery | Content & Media; Commerce; Communications; Analytics |
| Identity, access and participant data rights | Identity & Access; Privacy & Consent; Audit & Evidence |
| Temperament assessment and reporting | Temperament; Content & Media; Entitlements |
| Health intake, records and safety routing | Health Records; Safety & Eligibility; Privacy & Consent |
| Personalised plans and review | Plans & Nutrition; Safety & Eligibility; Health Records; Temperament |
| Programmes, Nuwe Jy, habits, journals and progress | Programmes & Challenges; Habits, Journals & Progress; Communications |
| Content, translation, search, media and personalisation delivery | Content & Media; Experimentation; Analytics |
| Commerce, memberships, gifts and access | Commerce; Entitlements |
| Community, challenges, live sessions and events | Community; Programmes & Challenges; Events & Live |
| Professional services | Professional Care; Health Records; Safety & Eligibility; Plans & Nutrition |
| Operations, notifications, evidence and analytics | Communications; Audit & Evidence; Analytics |
| Research and bounded feedback | Research & Feedback; Content & Media; Communications |
| Governed voting and balloting | Voting & Balloting; Commerce; Entitlements |
| Interactive Tools / calculators / decision aids | Purpose-distributed among existing owners; **not** a Domain |


This coverage matrix is about **capability home**, not duplicated ownership. Where multiple domains are listed, Section 4 still identifies the singular owner for each durable truth.

## 8. Domain dependency and cycle review

### 8.1 Authority direction

The critical authoritative directions are intentionally asymmetric:

```text
Identity & Access ──actor context──> business domains
Health Records ──facts──> Safety & Eligibility ──current authority──> Plans & Nutrition
Temperament ──profile──> Plans / Content / Programmes
Commerce ──durable commercial consequence──> Entitlements
Entitlements ──access check──> protected product domains
Professional Care ──governed command──> Safety / Plans
Content & Media ──version reference──> Programmes / Communications / delivery surfaces
Programmes & Challenges ──association──> Community / Events & Live
Experimentation <──measurement evidence── Analytics
Research & Feedback ──owner-mediated request──> Safety / Professional Care / Communications / Commerce / Entitlements / Content
Voting & Balloting ──owner-mediated consequence──> Commerce / Entitlements
Identity & Access ──PMR lookup──> Commerce / Entitlements / Events
All domains ──minimum evidence──> Audit & Evidence
Privacy & Consent ──orchestration/request──> each owner's deletion/export contract
```

No domain receives permission to directly mutate another domain's tables/state because it depends on that domain.

### 8.2 Potential cycles that were rejected or constrained

- **Safety ↔ Plans:** Plans reads current Safety authority; Safety may require a plan pause/re-evaluation consequence. Safety never edits Plan persistence directly, and Plan state never becomes Safety authority.
- **Professional Care ↔ Safety/Plans:** Professional Care records the professional review, then invokes the owning domain to enact eligibility/plan changes. It does not own their state.
- **Experimentation ↔ Analytics:** Analytics measures; Experimentation configures/assigns/decides. Analytical evidence can inform the decision without acquiring experiment authority.
- **Privacy & Consent ↔ every data domain:** Privacy orchestrates lifecycle requests and verifies completion; each domain owns the actual eligible record transition. This is governance orchestration, not mutual write authority.
- **Audit & Evidence ↔ every domain:** source domains append evidence; Audit cannot use that evidence to mutate source truth.
- **Research & Feedback ↔ Safety/Care/Commerce/Entitlements/Content/Communications:** Research may request a consequence; each owner independently establishes its own truth.
- **Voting & Balloting ↔ Commerce/Entitlements:** official result may request a reward/access grant; Voting never writes commercial or entitlement authority.
- **Identity & Access ↔ Commerce/Entitlements/Events for PMR lookup:** lookup identifies a candidate; the owning Domain validates eligibility.

**Circular authoritative control dependencies accepted:** `0`.

## 9. Deliberately non-domain concerns

The following remain important but are not independent business-truth domains at this stage:

| Concern | Why it is not a separate domain |
|---|---|
| Product spaces | Logical activation/experience context under frozen Architecture; exact representation is downstream and must not create generic tenancy. |
| Recommendations/personalised feed | Derived decision/presentation capability over authoritative signals; durable source truth remains Content/Temperament/Health/Safety/Plans. |
| Administration / Support UI | Operator surface over owning domain interfaces and policies; screen grouping does not confer ownership. |
| Infrastructure/Deployment/Observability | Architecture/operations mechanisms, not business truth. |
| Search index/cache/read models | Derived projections owned semantically by their source domain or Analytics where analytical; never independent write authority. |
| Provider state | External evidence/capability behind domain adapter, never a domain owner. |
| Nuwe Jy | Flagship composition of reusable domains, not a parallel platform/domain stack. |
| Interactive Tools / calculators / decision aids | Capability, not a Domain. Calculation is not authority. Transient/public/anonymous use is non-authoritative by default. Purpose-specific protocols and results remain with existing owners. Content may publish presentation artifacts; Habits may own only narrowly fitting self-tracking results. |
| Interactive Evidence / Engagement | Shared primitives do not create shared business authority. |
| Platform Member Reference as a Domain | PMR is Identity & Access Account truth, not a nineteenth-plus identity Domain. |
| Competitions as a Domain | A competition may compose Voting & Balloting with Programmes, Community, Safety, Commerce, Entitlements, Events and Communications. Voting does not own the whole competition. |

## 10. Consolidated Phase-5 review rubric

The working map must pass one consolidated review before freeze:

1. **Ownership completeness** — every major mature-platform durable truth has exactly one owner.
2. **Boundary coherence** — domain boundaries follow truth/lifecycle/invariant vocabulary rather than pages/features/tables.
3. **Shared-write/cycle safety** — no unresolved shared mutation or circular authoritative control.
4. **Product Law coverage** — mature capabilities and MVP path all have a domain home.
5. **Architecture compliance** — domains use frozen mechanisms and do not invent a new transaction/state/cache/async/realtime/provider/security model.
6. **Privacy/security** — consent, health, professional, journal, financial and audit boundaries remain explicit.
7. **Performance/scaling proportionality** — each domain has the required lightweight OQ-039 profile without speculative keys/TTLs/queues/indexes.
8. **Anti-fragmentation** — no domain exists only because a feature/module/table could exist; no giant catch-all domain confuses ownership.

## 10.1 Consolidated review result

| Review lens | Result | Finding |
|---|---|---|
| Ownership completeness | **PASS** | 61 major durable-truth rows have exactly one listed owner; all owners are in the approved 20-domain set. |
| Boundary coherence | **PASS** | Boundaries follow distinct durable truth/lifecycle/policy vocabulary; feature/page/module names were not promoted automatically. Research polls follow Research purpose; governed votes follow Voting purpose. |
| Shared-write / circular control | **PASS** | 0 accepted shared-write ambiguities and 0 circular authoritative control dependencies. Cross-cutting deletion/audit/analytics edges are orchestration/evidence/derived edges. Research/Voting consequences are owner-mediated. |
| Product Law coverage | **PASS** | 14 mature-platform capability families, including the MVP, approved future Nuwe Jy/membership/practitioner/community/event/experiment paths, Research & Feedback, Voting & Balloting and purpose-distributed Interactive Tools, have domain homes. |
| Architecture compliance | **PASS** | No new transaction, state-authority, async, realtime, provider, cache or scaling mechanism was invented. |
| Privacy / security | **PASS** | Identity, consent, health, safety, journal, professional, financial, audit evidence, Research and ballot-privacy boundaries remain explicit and non-interchangeable. |
| Performance / scaling proportionality | **PASS** | 20/20 domains contain the required lightweight OQ-039 profile without exact keys, TTLs, queues, topics, indexes or infrastructure sizing. |
| Anti-fragmentation | **PASS** | The original 22-name hypothesis remains reduced; Interactive Tools, Interactive Evidence, Engagement, PMR and Competitions were rejected as Domains. Research & Feedback and Voting & Balloting were added because no existing Domain could own those lifecycles without distortion. |

### Review corrections applied from v0.1.0

- **EDITORIAL:** corrected an invalid Health Records DEC cross-reference; no Product Law meaning changed.
- **BOUNDARY CLARIFICATION:** distinguished identity-side role/privilege grants from domain-owned business relationships/assignments.
- **BOUNDARY CLARIFICATION:** distinguished general Entitlements from event-owned ticket/admission authority under the locked event model.
- **BOUNDARY CLARIFICATION:** OQ-033 remains authoritative for the legal/professional recordkeeper. Professional Care owns the platform care-case/workflow and any platform-held professional record representation; an external practitioner/entity may remain the professional record authority. This gate constrains storage/retention/disposition but does not require a second platform domain.
- **BOUNDARY CLARIFICATION:** generic infrastructure telemetry remains Architecture/Operations; Analytics owns governed product/domain analytical facts and aggregates only.

### Material challenges considered

- **Privacy & Consent kept combined:** consent, withdrawal, deletion, retention, legal hold and export all govern authorised processing/data rights and strongly interact. The profile explicitly recognises hot current-consent checks versus heavy lifecycle orchestration; this does not create shared ownership.
- **Audit & Evidence kept separate:** append-only evidence has independent retention/access/integrity rules and must not become the source of the business facts it proves. Folding it into IAM or Privacy would blur those boundaries.
- **Programmes & Challenges combined:** Product Law describes challenges as governed structured participation, and Nuwe Jy is explicitly a programme delivered through a challenge experience. Community conversation/moderation remains separate.
- **Commerce and Entitlements kept separate:** provider/payment/subscription truth and access-grant truth have different invariants and failure semantics; combining them would weaken duplicate/reconciliation safety.
- **Research kept out of Experimentation:** experiment assignment/exposure/decision is not Research instrument/response/withdrawal truth.
- **Voting kept out of Community and Programmes:** surface location does not transfer governed-vote authority; competitions compose multiple Domains.
- **PMR kept in Identity & Access:** human-facing Account reference, not a new Domain or an Entitlements credential.
- **Interactive Tools kept non-Domain:** calculation is not authority; Content is not generic calculation owner; Habits is not a generic persisted-result bucket.

**Owner questions requiring a new Grill-Me round:** `0` remaining after the targeted Domain Grill. Human decisions `DQ-1` and `DQ-2` accepted the Research & Feedback Domain and the Voting & Balloting Domain with naming refinement. Interactive Tools and Platform Member Reference required no new Domain.

## 11. Phase-5 closure criteria

Freeze only when all are true:

- all approved mature-platform capability families have a home;
- every major durable truth in Section 4 has exactly one authoritative owner;
- every approved domain has an Owns/Does-not-own boundary and lightweight Architecture Profile;
- no unresolved shared-write ambiguity or circular authoritative control remains;
- no new platform mechanism was invented;
- MVP sequencing is possible without dead-ending Nuwe Jy, membership/Premium, practitioner services, community/live/events or experimentation;
- remaining unknowns are correctly routed to OQ/JIT/Feature Pack/Architectural Proof rather than guessed;
- `05_ROADMAP_v1.1.1.md` can sequence outcomes without implementation-grade dossiers for every future domain.

## 11.1 MVP and future-path sequencing check

The ownership model supports the approved evolution without a structural dead end:

```text
MVP
Identity & Access
→ Commerce → Entitlements
→ Temperament
→ Health Records → Safety & Eligibility
→ Plans & Nutrition
→ Habits, Journals & Progress
+ Content & Media / Communications / Audit & Evidence / Analytics

Nuwe Jy
→ Programmes & Challenges
+ Community + Events & Live + Communications
+ existing Safety / Plans / Entitlements

Basic Membership / Premium
→ Commerce contract + Entitlements
→ Content / Community / Events & Live
→ Habits/Progress + recurring Plans review when enabled

Practitioner pilot
→ Professional Care
+ scoped Health / Safety / Plans

Experimentation
→ Experimentation + Analytics
without changing source-domain authority
```

**Sequencing verdict:** PASS. Roadmap can introduce these domains incrementally while preserving the mature ownership model.

## 12. Phase-5 freeze record

### 12.1 Mechanical closure

```text
Approved domains:                         20
Ownership-matrix durable truths:          61
Duplicate truth labels:                    0
Matrix owners outside approved domains:    0
Lightweight Domain Architecture Profiles: 20 / 20
Mature capability families represented:   14 / 14
Shared-write ambiguities:                  0
Circular authoritative control deps:       0
New platform mechanisms invented:          0
Owner questions requiring Grill-Me:        0
```

The Phase-5 v1.0.0 mechanical closure (18 domains / 48 ownership rows) remains historical in `archive/04_DOMAIN_MAP_v1.0.0.md`.

### 12.2 Phase-5 verdict

**PASS.** Every known approved mature-platform capability has a domain home at the level required before Roadmap. Every major durable truth represented in the ownership matrix has one authoritative platform domain. Remaining gates constrain activation, policy values, legal/professional authority or implementation detail rather than leaving the platform with an unresolved shared-write model.

### 12.3 Roadmap readiness

**PASS.** `05_ROADMAP_v1.1.1.md` may now sequence outcome-oriented Feature Packs using these ownership boundaries and lightweight profiles. It must not redesign Domain Law, invent implementation-grade dossiers for every future domain, or begin executable development.

## 13. STOP conditions

Stop Domain Law and route upstream only if:

- one major business truth still has two plausible authoritative owners that Product Law cannot resolve;
- Domain modelling requires a platform mechanism absent from frozen Architecture;
- a legal/clinical/provider gate determines **ownership**, rather than merely later implementation/activation;
- a proposed ownership boundary contradicts frozen Product or Architecture Law.

Do **not** stop over naming preferences, fields, Ash Resource names, schemas, indexes, Redis keys/structures, TTLs, PubSub topics, Oban queues/workers, package selection, provider settings or other JIT implementation detail.

## 14. Targeted Domain amendment record (v1.1.0)

### 14.1 Predecessor preservation

- Predecessor: `archive/04_DOMAIN_MAP_v1.0.0.md`
- Archived predecessor path: `archive/04_DOMAIN_MAP_v1.0.0.md`
- Predecessor SHA-256: `f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a`
- Successor from the v1.0.0 baseline: `archive/04_DOMAIN_MAP_v1.1.0.md`
- Historical SemVer transition: `v1.0.0 → v1.1.0` because this amendment adds approved durable-truth ownership without invalidating the original 18 Domain histories.

### 14.2 Amendment scope

Additive Domain Law only. Product Law, Decision Register, AR-000, Architecture Law, Architecture synthesis, Reference Flows, Roadmap, Operating Model, Frontend Experience System, Delivery Atlas, FP-001 artifacts and Engineering Standards are unchanged.

Human decisions implemented:

- `DQ-1` ACCEPT — create Domain 19 **Research & Feedback**.
- `DQ-2` ACCEPT WITH NAMING REFINEMENT — create Domain 20 **Voting & Balloting**. The Domain is not named Competitions, Voting / Balloting / Competitions, or Engagement.

Rejected pseudo-Domains: Interactive Tools; Interactive Evidence; Engagement; Platform Member Reference; Competitions.

### 14.3 Existing-Domain additive amendments

- **Identity & Access:** Platform Member Reference lifecycle and minimum-disclosure lookup. `FP001_RECONCILIATION_REQUIRED`; exact representation remains `ARQ-IAM-013`.
- **Content & Media:** narrow published Interactive Tool editorial/presentation artifact boundary. Content is not generic tool-calculation authority.
- **Habits, Journals & Progress:** narrow Account-linked educational/self-tracking Interactive Tool result boundary. Habits is not a generic persisted-tool-result bucket.
- **Privacy & Consent, Analytics, Audit & Evidence, Community, Programmes & Challenges, Experimentation:** non-ownership clarifications only.

### 14.4 Downstream routing

- `ROADMAP_REVIEW_REQUIRED` — new mature owners exist; Feature Pack sequencing is not decided here.
- `FP001_RECONCILIATION_REQUIRED` — PMR is assigned at Account creation already in FP-001; FP-001 is not amended here.
- Engineering Standards, Atlas reconciliation, HARDEN-02, JIT dossiers for Domains 19 and 20, Resource/schema design and implementation remain not started.

### 14.5 Verdict

**PASS — DOMAIN AMENDMENT COMPLETE / DOMAIN MAP FROZEN v1.1.0.** Twenty Domains; one owner per listed durable truth; Interactive Tools remain purpose-distributed; PMR remains Identity & Access Account truth; 0 Product/Architecture contradictions.
