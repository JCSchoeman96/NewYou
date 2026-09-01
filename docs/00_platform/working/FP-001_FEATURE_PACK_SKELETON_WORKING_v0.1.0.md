# FP-001 Feature Pack Skeleton and Preliminary Gate Manifest

## Artifact status

```text
PHASE 7A WORKING ARTIFACT
FEATURE PACK: FP-001
NON-IMPLEMENTATION
NOT DEVELOPMENT-ENTRY AUTHORITY
DOES NOT REPLACE PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW
```

This is a Phase 7A discovery and preparation artifact. It is derived from the approved Roadmap outcome and current stronger authority. It does not resolve an upstream Product, Architecture, Domain or Roadmap question.

```text
Phase 7A Skeleton
    -> Phase 7B required JIT Domain Dossiers
    -> Phase 7C Final Feature Pack Contract
```

Only the approved Phase 7C Final Feature Pack Contract may become development-entry authority. Phase 7A does not authorise implementation, proof execution, a Tracer Bullet, a Vertical Slice, Horizontal Hardening or TOON work.

## 1. Identity

| Field | Value |
|---|---|
| Feature Pack ID | `FP-001` |
| Name | Trusted bilingual entry and verified identity |
| Roadmap position | Phase 1, Trusted entry and commercial truth; position 1 of 17; first node on the approved core path |
| Delivery character | `FOUNDATIONAL` |
| Selected status | `SELECTED FOR PHASE 7A PREPARATION` |
| Approved dependencies | Frozen Product Law, Architecture Law and Domain Law only; no future Feature Pack is a prerequisite |
| Known unlock | `FP-002` purchase, verified payment and entitlement, plus the protected identity boundary used by later core journeys |

The Roadmap remains the authority for the Feature Pack identity, sequencing, outcome, dependencies, scope and gates. The Atlas is navigation only.

## 2. Outcome

The approved Roadmap outcome is preserved without broadening:

> A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, verify email, recover access and use a controlled support/admin path without exposing unfinished product spaces.

This outcome establishes a trusted public-to-protected boundary. It does not make FP-001 a complete participant-ready MVP and does not pull later purchase, health, plan, community or event outcomes into this pack.

## 3. Validation objective

The approved Roadmap validation objective is:

> Prove that public-to-verified-account entry is understandable, privacy/age/terms gates are respected, identity/session authority is reconstructible and operators can resolve ordinary account-access issues.

The product outcome is the participant and operator result. The technical proof question is whether the authoritative identity, session, policy, recovery, communication and evidence boundaries can support that result under the applicable gates. This skeleton records that distinction and does not select the eventual proof vehicle.

## 4. Validation objective type

The approved Roadmap types are:

`PRODUCT`, `BEHAVIORAL`, `ARCHITECTURAL`, `SECURITY`, `PRIVACY`, `OPERATIONAL`.

## 5. Scope

### 5.1 In scope

The smallest approved FP-001 planning boundary contains:

- useful bilingual public entry in Afrikaans and English;
- launch-facing product, Christian-positioning and safety-boundary understanding through governed public content;
- an individual free account for a person aged 18 or older;
- the frozen minimum registration boundary: first name, surname, email, authentication credential, preferred language, 18+ confirmation and terms/privacy acceptance; phone and city remain optional;
- one canonical platform identity with email verification, sign-in/session authority and account recovery;
- limited pre-verification activity only where current authority permits it, with protected capabilities blocked until the applicable verified-email gate is satisfied;
- identity-side scoped role and privilege checks, while relationship-owned business access remains with the owning Domain;
- purpose-specific privacy and consent boundaries for the entry/account journey;
- governed launch-facing content, translation and publication obligations where the public boundary depends on them;
- verification and recovery communication consequences, including delivery evidence and failure visibility, without choosing a provider or channel implementation;
- a controlled ordinary support/admin path using named, scoped and auditable staff authority, without introducing a generic operator-work Domain or universal task system; and
- restricted security and audit evidence for identity, recovery, privilege, support and other sensitive actions.

Analytics remains a consumer of approved derived evidence only. FP-001 does not introduce `CAP-027` or an Analytics-owned business truth.

### 5.2 Out of scope

- social login and passkeys, which remain deferred or future extensions;
- advanced participant MFA configuration beyond the locked optional-participant and high-risk step-up boundary;
- household accounts, generic tenancy and unrestricted multi-tenant behaviour;
- native applications and unfinished or future product spaces;
- purchase, payment, entitlement, assessment, health, safety, plan, programme, community, live-session or event outcomes belonging to later approved packs;
- full data-rights, retention and deletion orchestration as a reusable capability (`CAP-004`, introduced by `FP-006`), except for the identity-side gates and distinctions needed to protect the entry boundary;
- a reusable operator-work capability (`CAP-029`), generic admin lifecycle or dashboard; the controlled support/admin path is a bounded FP-001 use of source-owned actions;
- `Commerce` participation, payment truth or commercial catalogue work; generic support listed by `CAP-005` does not override the explicit FP-001 Roadmap Domain set;
- health, medical or full date-of-birth data collected merely for registration;
- exact authentication packages, Resources, schemas, routes, components, deployment topology, queues, caches, workers or other implementation mechanisms;
- implementation-grade lifecycle state machines, final acceptance, final proof classification, Architectural Proof, TB, VS, HH or TOON artifacts.

## 6. Material capability input

ATLAS-04 was checked against the current matrix and reverse summary. FP-001 has exactly seven material relationships, all `I` introductions. The reverse row has no `R`, `E` or `S` relationships:

| CAP | Relationship | Capability | Authoritative boundary | Why material to FP-001 | Exact authority anchors | Phase 7B detail indication |
|---|---|---|---|---|---|---|
| `CAP-001` | `I` | Canonical identity and authentication | Identity & Access owns canonical identity, credentials, sessions, devices, recovery and account-closure state | The approved outcome requires one recoverable identity, verified email and authenticated access boundary | `04_DOMAIN_MAP_v1.0.0.md §6.1`; `03_ARCHITECTURE_v1.0.0.md §6.1`; `05_ROADMAP_v1.0.0.md §6 FP-001` | `YES` for implementation-grade identity, verification, session, recovery and abuse-boundary detail |
| `CAP-002` | `I` | Scoped authorisation and relationship access | Identity & Access owns identity-side grants; relationship-owning Domains retain relationship truth | The pack must protect current actor, scope, purpose, expiry and revocation without creating a shared access owner | `04_DOMAIN_MAP_v1.0.0.md §§3-5, 6.1`; `03_ARCHITECTURE_v1.0.0.md §6.2`; `05_ROADMAP_v1.0.0.md §1.1` | `YES` for exact policy composition, field projection and revocation behaviour where required |
| `CAP-003` | `I` | Consent and purpose control | Privacy & Consent owns purpose-specific consent and lawful-basis state | Terms/privacy and purpose boundaries must be respected and remain distinct from identity and role authority | `04_DOMAIN_MAP_v1.0.0.md §§4, 6.2`; `03_ARCHITECTURE_v1.0.0.md §6.3`; `00_PLATFORM_v1.2.1.md §§21C.19, 21I.13` | `CONDITIONAL`; current law may be sufficient unless exact entry-purpose and withdrawal semantics are needed |
| `CAP-005` | `I` | Public discovery and acquisition | No single owner; Content, Communications, source Domains, Privacy and Identity retain their own truth | FP-001 introduces the public-to-account boundary and must keep useful public discovery separate from forced signup or protected access | `05_ROADMAP_v1.0.0.md §6 FP-001`; `00_PLATFORM_v1.2.1.md §§7.2-7.3`; `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md §§3.1, 5.1` | `CONDITIONAL`; exact public copy and acquisition surfaces are downstream only if materially new |
| `CAP-006` | `I` | Governed content, translation and publication | Content & Media owns content versions, locale branches, approval and publication | Launch-facing product, safety, terms and onboarding understanding depends on governed approved bilingual content | `04_DOMAIN_MAP_v1.0.0.md §6.7`; `00_PLATFORM_v1.2.1.md §§21E.1-21E.10`; `PLATFORM_OPERATING_MODEL_v1.0.0.md §§9-13` | `CONDITIONAL`; frozen content and translation law may support reuse, with exact detail only if the active slice needs it |
| `CAP-017` | `I` | Communications and notification delivery | Communications owns subscriber contact, message intent, delivery status and provider evidence; it does not own canonical account email or originating business facts | Verification and recovery are part of the outcome and need durable, retry-aware, privacy-sensitive delivery consequences | `04_DOMAIN_MAP_v1.0.0.md §6.15`; `03_ARCHITECTURE_v1.0.0.md §10.4`; `PLATFORM_OPERATING_MODEL_v1.0.0.md §§7, 12, 21`; `01_DECISIONS_v1.2.2.md DEC-261-DEC-263` | `YES` for the domain contract around verification/recovery intent, deduplication, retry, failure and provider evidence; OQ-036 remains unresolved |
| `CAP-028` | `I` | Audit and security evidence | Audit & Evidence owns restricted append-only evidence; source Domains retain business truth | Sensitive identity, recovery, privilege, support and security actions require minimised, auditable evidence | `04_DOMAIN_MAP_v1.0.0.md §6.18`; `03_ARCHITECTURE_v1.0.0.md §§12.3, 12.4, 14`; `PLATFORM_OPERATING_MODEL_v1.0.0.md §§22, 25, 28` | `CONDITIONAL`; the current evidence boundary may suffice until exact FP-001 evidence events and retention are needed |

No other capability is material to this Phase 7A boundary. In particular, `CAP-004`, `CAP-027` and `CAP-029` are not introduced by FP-001. The generic CAP support list does not convert a capability or Domain into active-FP materiality.

## 7. Domain participation

The approved starting set is the six Domains named by the Roadmap. The role, durable-consequence and dossier columns are separate decisions:

| Domain | Phase 7A role | Durable consequence | JIT dossier | Boundary and reason |
|---|---|---|---|---|
| Identity & Access | `PRIMARY` | `YES` | `YES` | Owns canonical identity/account, verification, session, recovery, device and identity-side grant truth. |
| Privacy & Consent | `SUPPORTING` | `YES` | `CONDITIONAL` | Owns purpose-specific consent state; current law may be enough unless exact entry-purpose, acceptance or withdrawal propagation must be finalised. |
| Content & Media | `SUPPORTING` | `YES` | `CONDITIONAL` | Owns governed launch-facing content, bilingual variants and publication truth. The working Atlas compression of this involvement as `Consumer` does not override the Roadmap affected set or the material `CAP-006` relationship. |
| Communications | `SUPPORTING` | `YES` | `YES` | Owns verification/recovery communication intent and delivery evidence, while Identity owns account email and verification truth. |
| Audit & Evidence | `SUPPORTING` | `YES` | `CONDITIONAL` | Owns restricted evidence and security-event linkage; it never owns the identity or consent transition being evidenced. |
| Analytics | `CONSUMER` | `NO` | `NO` | May consume minimum governed derived entry evidence. It does not introduce `CAP-027`, source business truth or an Analytics architecture in FP-001. |

`Affected Domain` is not the same as `Change Domain`, and neither implies a JIT dossier. The durable-consequence column identifies whether the Domain's own truth may change or be persisted by the outcome. A dossier is selected only where Phase 7C would otherwise need to invent implementation-grade Domain semantics.

Commerce is deliberately absent. `CAP-005` has generic Commerce support in the capability inventory, but the explicit FP-001 Roadmap affected set and current Domain authority do not make Commerce a participating FP-001 Domain.

## 8. Phase 7B dossier discovery

### Required dossiers

1. **Identity & Access: `YES`.** Phase 7C cannot truthfully finalise the verified-identity outcome without implementation-grade clarification of the account/identity boundary, verification gate, session and device revocation, graduated recovery, scoped grants, duplicate/retry handling, authority reconstruction and abuse/security boundary. The dossier must preserve current Domain and Architecture law and must not resolve `OQ-034` or select a package or mechanism.
2. **Communications: `YES`.** Verification and recovery delivery are material consequences of the selected outcome. Phase 7C needs a domain-level contract for message intent, destination distinction, privacy minimisation, retry/deduplication, terminal failure and provider evidence. The dossier must not choose a provider/channel policy or resolve `OQ-036`.

### Conditional candidates

- **Privacy & Consent: `CONDITIONAL`.** Existing purpose-specific consent, withdrawal and data-lifecycle law may be sufficient. A dossier becomes necessary only if the entry journey requires exact implementation-grade acceptance, purpose catalogue, withdrawal or invalidation semantics not already frozen.
- **Content & Media: `CONDITIONAL`.** Existing governed bilingual content, locale, approval and publication law may support the launch-facing boundary. A dossier is needed only if FP-001 introduces materially new content/publication semantics rather than consuming approved patterns.
- **Audit & Evidence: `CONDITIONAL`.** Current restricted evidence and security-audit law may be sufficient. A dossier is needed if exact FP-001 evidence event, minimisation, access or retention contracts cannot be stated without invention.

### No dossier selected

- **Analytics: `NO`.** Analytics is an affected consumer, not a material introduced capability. Minimum derived evidence can be confirmed at the later contract boundary without creating a separate Analytics dossier.

No Phase 7B dossier is created by this artifact. Domain participation, durable consequence and dossier selection remain distinct.

## 9. Lifecycle pressure

Phase 7A records obligations, not an FP-001 state machine. The following are the independently owned truths that require lifecycle attention:

| Truth and owner | Known lifecycle obligation from current authority | Guards, invalidation, concurrency and evidence pressure | Phase 7A route |
|---|---|---|---|
| Identity/account, Identity & Access | Account creation, verification, active/restricted/closed/recoverable account context; one canonical reconciled identity; account closure remains distinct from full deletion | 18+ and entry-policy gates; duplicate-account reconciliation; recovery cannot create other Domain authority; concurrent create/merge/recovery actions must be repeat-safe; security evidence required | Broad lifecycle is known. Exact action/state contract belongs to the required Identity dossier. |
| Email verification, Identity & Access with Communications consequence | Limited unverified onboarding, request/resend capability and verified email before protected capabilities | Server-authoritative proof; one-purpose replay-controlled verification; duplicate/reordered delivery must not create extra identity effects; delivery failure is not verification success; audit evidence required | `YES` dossier detail; no invented token or implementation state. |
| Sessions and trusted devices, Identity & Access | Individually identifiable, role/risk-bounded, expiring and revocable sessions/devices; user-visible revocation | Current authority must be reconstructed after restart or reconnect; revocation and security changes invalidate stale assurance; concurrent sign-out, recovery and sensitive actions require current checks; audit required | `YES` dossier detail; exact expiry parameters remain downstream. |
| Recovery, email change and compromise, Identity & Access | Graduated automated/manual recovery, security holds, verified-channel notification, reauthentication, old-address notice, session review/revocation and compromise containment | Recovery restores identity control only; privileged recovery has stronger review; duplicate/retry/replay and concurrent recovery must not weaken assurance; support action is scoped and audited | `YES` dossier detail; `OQ-035` thresholds and `OQ-034` implementation architecture remain open. |
| Identity-side grants, Identity & Access plus relationship owners | Explicit, scoped, assignable, removable, auditable, time-bounded grants; relationship and purpose remain with their owners | Current role/relationship/purpose/expiry must be re-evaluated at protected action; revocation must not be bypassed by stale presentation; no shared grant owner | `YES` dossier detail for the exact policy boundary, not a new shared Domain. |
| Consent, Privacy & Consent | Purpose-specific consent is versioned and may be active, withdrawn or superseded; withdrawal stops dependent future processing and invalidates derived authority | Consent cannot be inferred from account, language, support or participation; exact acceptance and invalidation semantics may need confirmation; governance actions are audited | `CONDITIONAL` dossier candidate. No new legal rule is created here. |
| Governed content/translation/publication, Content & Media | Governed variants move through the approved content and translation review/publication lifecycle; published versions are immutable and may be superseded or withdrawn | Approved bilingual content is required where the content risk demands it; source and locale changes invalidate stale approvals; publication/correction/withdrawal evidence is required | `CONDITIONAL` dossier candidate; no content state beyond current law is invented. |
| Communication intent/delivery, Communications | Durable message intent and delivery may progress through created, queued, sent, delivered, failed, retried and terminal outcomes; preferences can change | Must-not-lose intent precedes delivery; duplicate execution cannot multiply logical messages; provider evidence is not source truth; outage degrades communication, not identity truth | `YES` dossier detail; provider policy remains `OQ-036`. |
| Audit/security evidence, Audit & Evidence | Evidence is appended immutably, restricted and retained or lawfully expired/anonymised by category; corrections add evidence rather than rewrite history | Evidence absence cannot manufacture business success; access to evidence is privileged; minimisation and retention remain material | `CONDITIONAL` dossier candidate; no retention schedule is invented. |
| Operator support projection, source-owning Domains and Operating Model | Work is attention over Domain-owned obligations, not a universal business lifecycle; support resolves permitted ordinary account-access issues | Queue/work visibility grants no business authority; sensitive actions require the owning policy, separation of duties and audit; no generic task state is created | No new Domain or lifecycle. Use scoped source-owned actions and projections. |

Known lifecycle obligation is separate from implementation-grade lifecycle definition. Exact transition ordering, action contracts, resource representation, expiry values, retry budgets and storage/mechanism choices are not frozen by this Skeleton. No synthetic global FP-001 state machine is created.

## 10. Preliminary Gate Manifest

### 10.1 Authoritative Product Decisions

Only the material Product/Decision surfaces are carried forward:

- `DEC-017`, `DEC-018`, `DEC-019`, `DEC-027`, `DEC-028`: public/free entry, adult-only launch, individual-account model, minimum fields and Afrikaans/English launch.
- `DEC-021`, `DEC-022`: multiple explicit auditable roles and the named staff categories used by a controlled support/admin path.
- `DEC-244` through `DEC-255`: participant authentication, verification gating, participant and privileged-user MFA boundaries, sessions, trusted devices, recovery, email change, duplicate reconciliation, compromise containment, scoped grants and break-glass access.
- `DEC-256`: layered authentication abuse-control obligation; thresholds and concrete implementation remain gated/downstream.
- `DEC-261` through `DEC-264`: notification channel, preference, delivery and graceful-degradation obligations relevant to verification/recovery consequences.
- `DEC-267`: operational observability for material identity, delivery and provider-outage outcomes.
- `DEC-268` through `DEC-270`: controlled product spaces, launch-facing scope and South Africa-first launch context.

Product Law context: `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md §§5.1, 8, 10-12`; `00_PLATFORM_v1.2.1.md §§7.2-7.3, 21J.1-21J.12, 21L.1-21L.4`.

### 10.2 Applicable Architecture Decisions

The material Architecture Law surfaces are:

- `03_ARCHITECTURE_v1.0.0.md §§4.1-4.2, 5, 6.1-6.4`: authoritative application boundaries, canonical identity, current authorisation, consent, revocation, recovery, compromise, abuse and non-enumerating behaviour;
- `03_ARCHITECTURE_v1.0.0.md §§7.1-7.3`: durable authority and projection boundaries; no browser, process or acceleration state becomes business truth;
- `03_ARCHITECTURE_v1.0.0.md §§8.1-8.4`: authoritative work, durable consequences, provider evidence, idempotency and external ambiguity;
- `03_ARCHITECTURE_v1.0.0.md §§10.1, 10.4`: governed bilingual content and messaging/provider boundaries;
- `03_ARCHITECTURE_v1.0.0.md §§12.1-12.4`: failure isolation, restart/recovery, observability, incident evidence and operational proof;
- `03_ARCHITECTURE_v1.0.0.md §§13.1-13.5`: workload-specific scaling and adversarial proof obligations without premature infrastructure selection;
- `03_ARCHITECTURE_v1.0.0.md §§14-15`: server-authoritative security, least privilege, revocable secrets/sessions, audit separation and enforceable boundaries; and
- `FLOW-01` in `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md §§2-3`: existing conceptual registration-to-verification-to-login evidence.

This Skeleton selects no authentication package, Resource, schema, queue, cache, worker, topology or other implementation mechanism.

### 10.3 Affected Domains

The preliminary manifest carries exactly the six Roadmap Domains:

`Identity & Access`; `Privacy & Consent`; `Content & Media`; `Communications`; `Audit & Evidence`; `Analytics`.

Their role, durable-consequence and dossier decisions are recorded in §7. No Commerce Domain is added.

### 10.4 Required JIT Dossiers

| Domain | Decision | Reason and boundary |
|---|---|---|
| Identity & Access | `YES` | Required to make the identity, verification, session, recovery, grant, duplicate and abuse boundary implementation-grade without inventing it in Phase 7A. |
| Communications | `YES` | Required to make verification/recovery intent, destination distinction, retry/deduplication, delivery failure and provider-evidence semantics implementation-grade without resolving OQ-036. |

Conditional candidates remain Privacy & Consent, Content & Media and Audit & Evidence. Analytics is `NO`. No dossier is authored here.

### 10.5 Blocking OQs

| OQ | Classification | Protected behaviour | Deciding authority and Phase 7A effect |
|---|---|---|---|
| `OQ-034` | `BLOCKS_THIS_FP` | The verified identity/session outcome cannot be accepted without the approved authentication implementation architecture and proof boundary. | Architecture/Product authority and the applicable evidence boundary decide. Phase 7A may define scope and dossier discovery, but must not resolve it. Phase 7C/development-entry acceptance stops while it remains unresolved. |

### 10.6 Non-blocking / later gates

| OQ | Classification | Why planning may continue |
|---|---|---|
| `OQ-035` | `BLOCKS_RELEASE_ONLY` | Internal account-flow preparation may proceed behind the platform-owned abuse boundary. Protected public or pilot release cannot proceed without approved thresholds and recovery behaviour. |
| `OQ-036` | `BLOCKS_RELEASE_ONLY` | Identity planning and the Communications dossier may define the required delivery contract without choosing a provider/channel policy. Release of promised verification or mandatory-notice communication cannot proceed without the approved launch policy. |
| `OQ-038` | `FUTURE_ONLY` | Named incident ownership is a later paid-pilot/release condition owned by `FP-006`; it does not delay safe internal FP-001 planning. |

`OQ-001` and `OQ-004` are not FP-001 Roadmap gates. `OQ-039` remains a downstream implementation-grade performance/scaling mapping requirement where an affected action enters a later implementation boundary; it is not added as an FP-001 Roadmap classification here.

### 10.7 Entry STOP condition

While `OQ-034` remains unresolved, Phase 7A and the selected Phase 7B dossiers may:

- preserve the approved outcome and boundaries;
- define the authoritative Domain and communication contracts at the required planning level;
- record known lifecycle, security, privacy, frontend, data and performance obligations;
- identify unresolved gates and route them to their owners; and
- prepare questions needed for Phase 7C.

They may not:

- resolve or locally reinterpret `OQ-034`;
- select an authentication package, exact implementation mechanism or implementation-grade state/schema contract;
- accept the verified identity/session outcome as development-ready;
- finalise proof classification or create a TB; or
- start executable development.

Any new contradiction in Product, Architecture, Domain ownership or Roadmap truth is a STOP and must be routed to the owning authority rather than absorbed here.

## 11. Preliminary performance and scaling review

This is pressure identification only. It does not select a mechanism or create an OQ-039 implementation mapping.

| Pressure area | Correctness/performance obligation | Downstream boundary |
|---|---|---|
| Password hashing | Cost must be benchmarked and bounded so registration/login remain safe under expected bursts without weakening credential protection | Architecture/JIT and later proof; no cost or package is selected here |
| Registration/login bursts | Admission and abuse behaviour must remain non-enumerating, bounded and recoverable while identity authority remains correct | `OQ-035`; later performance evidence |
| Verification delivery backlog | Must-not-lose verification intent, duplicate-safe resend and honest pending/failure visibility are required; delivery backlog must not be treated as verification truth | Communications dossier and `OQ-036` release boundary |
| Abuse/rate pressure | Layered controls must preserve privacy, non-enumeration and multi-node correctness where required; thresholds remain unresolved | `DEC-256`, `OQ-035`, Architecture §6.4 |
| Session authority reconstruction | Current session, role and revocation authority must be reconstructible after restart/reconnect and not depend on a local presentation state | Identity dossier and Architecture §§7, 12 |
| Retry/idempotency | Repeated, reordered or replayed registration, verification, recovery, email-change and support actions must not multiply logical identity effects | Identity/Communications dossiers; exact operation contracts remain JIT |
| Account enumeration | Public responses must not reveal whether sensitive identities or recovery targets exist, while internal evidence remains precise | Identity dossier and Architecture §6.4 |
| Support/recovery concurrency | Support cannot bypass current authority; concurrent participant and staff recovery actions require scoped review, safe holds and audit | Identity dossier, Operating Model and `OQ-034`/`OQ-035` |
| Restart/reconnect and degraded dependencies | Communication or telemetry failure may degrade the dependent capability but cannot fabricate verification, access or recovery success | Architecture §§8, 12; FES §§4, 5.7 |

Correctness invariants are recorded separately from candidate mechanisms. No cache, queue, worker, database setting, topology or package is frozen by this review.

## 12. Security, privacy and safety

The planning boundary preserves the following approved obligations:

- the initial platform serves people aged 18 or older;
- registration uses the minimum approved account fields, and health, medical and full date-of-birth information are not collected merely to create an account;
- terms/privacy acceptance and purpose-specific consent remain distinct from authentication and role assignment;
- email verification is server-authoritative and gates protected capabilities; limited unverified onboarding does not imply protected access;
- participant authentication, session revocation, trusted-device expiry and high-risk step-up remain current-authority checks;
- recovery is graduated, replay-controlled and auditable; it restores identity control but never manufactures entitlement, relationship, consent or other Domain authority;
- duplicate-account reconciliation preserves immutable history and original provenance;
- privileged access uses MFA, named scoped grants, least privilege, separation of duties and governed break-glass evidence; there is no universal Super Admin bypass;
- public authentication and recovery behaviour is non-enumerating;
- Communications minimises sensitive payloads and rechecks applicable consent/preferences without changing the originating business truth;
- Audit & Evidence receives restricted minimum-necessary evidence and never becomes identity, consent or communication truth; and
- graceful degradation must not guess identity, payment, entitlement, health or safety truth.

No new legal, clinical, Product or security rule is created here.

## 13. Frontend and experience boundary

The Phase 7C experience contract must preserve only these surface categories and obligations:

- **Public entry:** useful launch-facing content, clear product/safety boundaries, visible Afrikaans/English switching and discoverable account entry; no blocking language modal before useful content;
- **Participant identity/account:** minimal progressive registration, accessible bilingual fields, verification-pending visibility, resend/change-email recovery where permitted, sign-in/session and recovery feedback;
- **Protected-access boundary:** protected capabilities remain blocked until authoritative verification and current permission are satisfied;
- **Scoped support/admin:** a policy-aware staff projection for permitted account-access work, with minimum necessary context and no routine impersonation or universal task authority;
- **State visibility:** honest loading, validating, pending, conflict, restricted, unavailable, degraded, error and requires-attention presentation where the frozen FES rules apply; and
- **Accessibility and responsive behaviour:** semantic accessible forms, visible focus, long bilingual-label support, keyboard/screen-reader safety, responsive reflow and mobile-safe essential support actions.

The frontend submits untrusted intent and reflects authoritative results. It never becomes authority for identity, verification, sessions, grants, consent or audit evidence. This section defines no routes, pages, components, layouts, tokens, exact forms or client-side implementation.

Relevant frozen experience authority: `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md §§3.1, 4, 5.1-5.2, 5.7, 6.1-6.3, 7.2, 9, 10.2-10.4`.

## 14. Data authority and projection boundary

| Data relationship | Authoritative source truth | Consequence/projection/evidence boundary |
|---|---|---|
| Identity and account | Identity & Access owns canonical identity, individual account, account email, credentials, verification, sessions, trusted devices, recovery and identity-side grants | Other Domains read current actor context. A support view or frontend is a projection, not authority. |
| Consent and purpose | Privacy & Consent owns purpose-specific consent, withdrawal and current consent state | Identity and other Domains check it for their own actions; withdrawal can invalidate derived authority but does not transfer source ownership. |
| Public governed content | Content & Media owns content identity, immutable versions, locale variants, approval and publication/withdrawal truth | Public/account surfaces receive approved projections. Communications may consume governed templates but does not own content body truth. |
| Account communication | Communications owns subscriber/contact relationship where applicable, message intent, delivery status and provider evidence | `canonical account email != communications subscriber contact`; provider delivery/open/click evidence is not identity or business truth. |
| Audit/security evidence | Audit & Evidence owns restricted append-only evidence and security/privilege linkage | `audit evidence != source business truth`; evidence can show what happened without authorising or rewriting the source transition. |
| Analytics | Analytics owns governed derived measurement facts, projections and aggregates only | Analytics consumes approved facts; it does not own identity, consent, content, communication, payment or access truth. No `CAP-027` architecture is introduced. |
| Temporary UI/read model | Browser, LiveView or support presentation holds temporary intent/projection state only | It may show pending or stale/requires-attention status and must re-read current authority where required; it cannot grant access or confirm verification. |

No schema, table, Resource, index, cache, queue, worker, topic, TTL or provider configuration is selected.

## 15. Proof pressure

Existing evidence:

- `FLOW-01` covers Registration -> verification -> login and is recorded as `PASS_WITH_DOWNSTREAM_GATES` with no architecture gap and no governing contradiction.
- The existing evidence identifies password-hashing cost, login bursts, abuse controls, verification backlog, replay control and durable reconstruction after node/process loss as later proof obligations.
- Exact authentication implementation architecture and abuse thresholds remain `OQ-034` and `OQ-035` boundaries.

Roadmap anticipation:

`PROBABLY_NEW_TRACER_BULLET` is recorded by the Roadmap because the first real authentication/session/recovery path materially exercises the identity boundary.

Possible unproven execution pressure includes registration-to-verification-to-login, recovery and revocation under duplicate/reordered requests, session reconstruction after restart/reconnect, non-enumerating abuse bursts, consent changes during protected actions, communication provider ambiguity and restricted audit evidence. These are possible proof obligations, not a final proof classification.

```text
Final proof classification: NOT FINALISED IN PHASE 7A
No REUSE_EXISTING_PROOF or NEW_TRACER_BULLET decision is made here.
No TB ID or proof artifact is created.
```

## 16. Known later Roadmap authority debt

```text
KNOWN LATER ROADMAP AUTHORITY DEBT:
FP-015 lists OQ-036 as a Major Gate but does not assign it a local four-way classification.
This does not affect FP-001.
Resolve before canonical FP-015 preparation/finalisation.
```

This handoff does not amend the Roadmap or Atlas.

## 17. Phase 7A handoff and provenance

If Phase 7B and then Phase 7C are separately authorised, they receive:

- the approved Roadmap outcome and validation objective;
- exactly seven material introduced capabilities: `CAP-001`, `CAP-002`, `CAP-003`, `CAP-005`, `CAP-006`, `CAP-017`, `CAP-028`;
- exactly six affected Domains and their separate role, durable-consequence and dossier decisions;
- the known lifecycle obligations without invented implementation states;
- the Identity & Access and Communications dossier requirements plus conditional Privacy, Content and Audit candidates;
- the `OQ-034` entry block and the non-entry-blocking `OQ-035`, `OQ-036` and `OQ-038` classifications;
- the preliminary performance, security, privacy, frontend and data-authority pressures;
- the existing `FLOW-01` evidence and deferred proof pressure; and
- the exact source trail below.

### Source trail used

| Source | Targeted use |
|---|---|
| `docs/00_platform/README.md` | Authority order, current-authority routing, Atlas non-authority status and selective Atlas sections |
| `docs/00_platform/05_ROADMAP_v1.0.0.md §§1.1, 6 FP-001, 14` | Exact identity, outcome, objective, type, position, dependencies, affected Domains, gates and anticipated proof |
| `docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.1.0.md` portfolio/FP-001 view, §§5.2-5.4, 6-12, 23-25 | Derived FP-001 route, seven-CAP matrix/reverse row, capability authority anchors and active-FP lifecycle, dependency, participant, operator, frontend and data contracts |
| `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md §§5.1, 8, 10-12` | Public entry, adult individual account, minimum fields, bilingual launch and protected product boundary |
| `docs/00_platform/00_PLATFORM_v1.2.1.md §§7.2-7.3, 21J.1-21J.12, 21L.1-21L.4` | Public content, registration/language, authentication, verification, session, recovery, role, notification and controlled-product-space rules |
| `docs/00_platform/01_DECISIONS_v1.2.2.md DEC-017-DEC-028, DEC-244-DEC-267, DEC-268-DEC-270` | Locked account, language, role, identity, recovery, abuse, communication, resilience and launch-space decisions |
| `docs/00_platform/03_ARCHITECTURE_v1.0.0.md §§4-15 and Appendix C` | Authority, interaction, identity, recovery, consent, durability, provider evidence, failure, observability, scaling, security and enforcement boundaries |
| `docs/00_platform/04_DOMAIN_MAP_v1.0.0.md §§3-5, 6.1, 6.2, 6.7, 6.15, 6.17, 6.18` | Domain ownership, cross-domain doctrine, lifecycle and evidence boundaries |
| `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md §§4-6, 9-13, 24-26` | Named staff roles, scoped support, content operations, communication/evidence separation, performance boundary and Phase 7 handoff |
| `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md §§3.1, 4, 5.1-5.2, 5.7, 6, 7.2, 9-10` | Public, registration, recovery, operator, bilingual, accessibility and presentation-state rules |
| `docs/00_platform/02_OPEN_WORK_v1.2.28.md §§5.6-5.7, 7, 8` | OQ ownership/context, Phase 7A required fields, dossier boundary and development hard stop |
| `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md §§1.1, 2, 3` | Existing FLOW-01 evidence and deferred executable proof pressure |

No archive document was needed. No global matrix, global journey, permanent FP-specific state machine or Atlas expansion was used.

## 18. Scope audit and STOP review

This working artifact contains planning categories only. It does not create:

- a Phase 7B JIT Domain Dossier;
- a Final Feature Pack Contract or development-entry authority;
- an implementation Resource, schema, route, component, package or infrastructure decision;
- a final proof classification, TB, VS, HH or TOON;
- an Atlas correction, ATLAS-12 work, global matrix or new permanent derivation capability; or
- any change to Product Law, Architecture Law, Domain Law, Roadmap, Decisions, Open Work or application code.

The correct next action is independent review of this Phase 7A artifact. If review identifies an authority contradiction, ownership ambiguity, missing Product rule, unresolved blocking gate or requirement for implementation-grade semantics outside the selected dossiers, STOP and route it to the owning authority.
