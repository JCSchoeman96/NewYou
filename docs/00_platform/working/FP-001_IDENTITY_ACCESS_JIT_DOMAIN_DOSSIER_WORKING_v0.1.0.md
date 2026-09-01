# FP-001 Identity & Access JIT Domain Dossier

```text
PHASE 7B JIT DOMAIN DOSSIER
FEATURE PACK: FP-001
DOMAIN: IDENTITY & ACCESS
IMPLEMENTATION-GRADE PLANNING LAW
NON-EXECUTABLE
NOT PHASE 7C DEVELOPMENT-ENTRY AUTHORITY
DOES NOT OVERRIDE PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW
```

**Status:** Working dossier for independent review and owner-controlled `OQ-034` resolution. This document selects the smallest coherent implementation contract inside the approved Identity & Access boundary. It creates no source code, migration, package installation, proof artifact, TOON, Phase 7C contract or authority amendment.

```text
Phase 7A Skeleton
→ this Identity & Access JIT Domain Dossier
→ required remaining Phase 7B work
→ explicit blocking-gate resolution
→ Phase 7C Final Feature Pack Contract
```

## A. Baseline and scope

The dossier starts from `main` at `2836e87f281c23877128a786fb1ff5a64e5f44e9`, the approved Phase 7A skeleton and current Product, Architecture, Domain and Roadmap authority. It covers Identity & Access only for the FP-001 outcome: a public visitor can become a verified individual 18+ account holder, authenticate, recover access and traverse a controlled support/admin boundary without exposing unfinished product spaces.

In scope are the minimum account, email verification, password/magic-link authentication, session, device assurance, recovery, primary-email change, identity-side grant, compromise and duplicate-reconciliation contracts needed for that outcome. Social login, passkeys, native clients, generic tenancy, participant-ready MFA configuration, full deletion orchestration, relationship permissions, Commerce and Communications implementation remain outside this dossier.

This is a planning contract, not a claim that `OQ-034` is already resolved. Exact threshold values remain `OQ-035`; notification provider/channel policy remains `OQ-036`.

## B. Authority review

The governing sequence is Product Law → Architecture Law → Domain Law → Roadmap → approved Phase 7A Skeleton → this dossier. Relevant current anchors are `01_DECISIONS_v1.2.2.md` DEC-017–028 and DEC-244–267, `00_PLATFORM_v1.2.1.md` §§15, 16 and 21J.1–21J.24, `03_ARCHITECTURE_v1.0.0.md` §§4–16, `04_DOMAIN_MAP_v1.0.0.md` §§3–6.1, `05_ROADMAP_v1.0.0.md` FP-001, the Phase 7A skeleton §§5–17, and FLOW-01 §§3.1–3.8.

No contradiction was found. The dossier does not add a Product rule, move durable truth, create a Domain, decide relationship authority, choose Communications infrastructure, resolve `OQ-035`, amend `01_DECISIONS`, start Phase 7C, or select a final proof classification.

## C. Outcome and design test

Every proposed concept was tested against the outcome. It is accepted only if it owns an independently durable invariant, lifecycle, concurrency boundary, security boundary or recovery/reconciliation obligation. A browser, LiveView process, cache, queue and audit record are not identity authority.

The minimum path is:

```text
anonymous request
→ Account.register with 18+/terms/privacy gates
→ Security Challenge(verify_email) + durable communication intent
→ Challenge.consume proves email; Account becomes verified
→ authenticate password or optional magic link
→ Session issued with current assurance
→ current Account/Grant/Consent/relationship authority checked at each protected action
→ recovery, email change, revocation and support actions revalidate current authority
```

## D. Resource map first

### D.1 Accepted resources

#### 1. Account

* **Purpose/owner/authority:** Canonical human identity and individual account; owned by Identity & Access; PostgreSQL is durable authority.
* **Identifier and key categories:** UUIDv7 opaque primary identifier; canonicalised email identity key; immutable creation/provenance metadata; no identifier is a bearer secret.
* **Attributes:** required first name, surname, canonical email, preferred language, 18+ confirmation, terms/privacy acceptance references, verification timestamp, account lifecycle state, security-hold/compromise markers, closure/recovery markers, and optimistic version. Phone and city are optional. Full DOB, health and medical data are absent.
* **Relationships:** many Credentials, Challenges, Sessions, Device Assurances, Grants and Reconciliation Cases; external references to communications intent, Privacy consent and owning business-domain records are identifiers/provenance only.
* **Sensitive/immutability:** email, security state, closure state and acceptance references are restricted; name/language are personal; provenance, creation and closure facts are append-only or superseding. Current fields may change only through named actions.
* **Retention/closure:** account closure is not full deletion. Identity retains only what approved retention/deletion contracts permit; full deletion orchestration belongs to Privacy & Consent.
* **Authoritative actions:** `register`, `mark_email_verified`, `change_primary_email`, `place_security_hold`, `release_security_hold`, `close`, and `restore_after_recovery`.
* **Policy/audit/integration:** self-service field policy plus current session/assurance; staff actions require scoped grant and reason. Audit material lifecycle transitions. Communications receives intent, never verification truth; Privacy is checked, not written by Identity.
* **Persistence:** independent persistence is required because identity, verification gate, closure and security state must survive restart and be queried by every protected Domain.

#### 2. Authentication Credential

* **Purpose/owner/authority:** Password credential and authentication-method status for one Account; Identity & Access/PostgreSQL.
* **Attributes:** account reference, method (`password` or optional `magic_link` capability), password hash metadata, credential status, created/changed/revoked timestamps, and version. Raw passwords, magic-link tokens and recovery secrets are never persisted.
* **Relationships:** belongs to Account; invalidates linked Sessions and Device Assurances when a security-changing action requires it.
* **Sensitive/immutability:** hash and security metadata are highly restricted; hashes are replaceable, raw secrets never recoverable. History is retained only as minimal security evidence.
* **Lifecycle/actions:** password credential `absent → active → replaced/revoked`; `set_password`, `authenticate_password`, `reset_password`, `revoke_credential`. Magic link is an authentication strategy, not a second identity.
* **Policy/audit/integration:** password fields are sensitive and write-only; authentication returns a generic failure. Password hashing is delegated to the selected maintained provider. Credential changes emit revocation/security consequences and audit evidence.
* **Persistence:** independent persistence is required for credential rotation, compromise containment and assurance checks.

#### 3. Security Challenge

* **Purpose/owner/authority:** One-purpose, bounded proof capability for email verification, password reset, recovery proof or email-change confirmation; Identity & Access/PostgreSQL.
* **Attributes:** UUIDv7 id, account reference where known, purpose, secret fingerprint/hash, issued/expiry/consumed/revoked timestamps, supersession reference, attempt/usage metadata, and correlation/provenance. The presented secret is never stored.
* **Relationships:** belongs to Account or a Recovery Case; may be linked to an Email Change attempt by purpose/reference. Communications receives a separate intent id.
* **Lifecycle/actions:** `issued → valid → consumed`; `issued → expired`, `revoked` or `superseded`; replay is a terminal rejected observation, not a second transition.
* **Policy/audit/integration:** purpose-specific action only; no generic “verify anything” endpoint. Confirmation establishes Identity truth only after server-side fingerprint, purpose, expiry and account-state checks.
* **Persistence:** independent persistence is required for single-use replay control, expiry, replacement and crash-safe proof consumption.

#### 4. Session

* **Purpose/owner/authority:** Individually identifiable browser authentication session; Identity & Access/PostgreSQL plus the maintained authentication token subsystem where selected.
* **Attributes:** UUIDv7 id, account, credential/method, opaque token fingerprint or framework token reference, assurance level, user-agent/device summary, created/last-seen timestamps, inactivity/absolute expiry, revoked timestamp/reason, and version.
* **Relationships:** belongs to Account and may reference Device Assurance; never embeds relationship authority or consent.
* **Sensitive/immutability:** token fingerprints and network/device security evidence are highly restricted; token secret is never stored. Creation and revocation facts are append-only; last-seen is mutable bounded telemetry/security state.
* **Lifecycle/actions:** `active → expired`, `revoked` or `logged_out`; session-specific and global revocation are distinct actions.
* **Policy/audit/integration:** secure HttpOnly cookie transport; every protected Ash action rechecks current session/revocation and required assurance. LiveView only reconstructs current actor context. Audit creation for privileged/high-risk sessions and revocation, not raw tokens.
* **Persistence:** independent persistence is required for multi-node reconstruction, visible session listing and revocation.

#### 5. Device Assurance

* **Purpose/owner/authority:** Limited, participant-consented trust associated with a device/session family; Identity & Access/PostgreSQL.
* **Attributes:** UUIDv7 id, account, device-token fingerprint, name, assurance level, created/last-used, expiry, revoked timestamp/reason and version. No raw fingerprinting payload or invasive device profile is required.
* **Relationships:** belongs to Account; can authorise session convenience but not high-risk step-up.
* **Lifecycle/actions:** `pending → trusted → expired/revoked`; suspicious activity and credential/security changes revoke it.
* **Policy/audit/integration:** explicit consent, stricter staff policy, no bypass of email change, export, deletion, MFA or other high-risk step-up. Audit grant/revoke and suspicious invalidation.
* **Persistence:** independent persistence is required by locked trusted-device policy and user-visible revocation.

#### 6. Identity Grant

* **Purpose/owner/authority:** Identity-side role/privilege assignment, including named staff/practitioner roles and exceptional break-glass records; Identity & Access/PostgreSQL.
* **Attributes:** subject, role/capability, scope, reason, approver, start, expiry/review date, source relationship reference, state and revocation metadata. It does not contain relationship-owned permission.
* **Relationships:** belongs to Account; may reference an organisation/practitioner relationship owned elsewhere.
* **Sensitive/immutability:** grants, approvals, reasons and revocations are highly restricted; history is append-only; current state is superseding projection over history.
* **Lifecycle/actions:** `requested → approved/assigned → active → expired/revoked`; break-glass is `requested → active → expired/revoked → reviewed` and is never an ordinary role.
* **Policy/audit/integration:** no self-approval; MFA and named actor required; least privilege, narrow scope, expiry and review. Business Domains re-evaluate their own relationship/purpose/consent authority.
* **Persistence:** independent persistence is required for scoped policy, revocation, review and audit.

#### 7. Recovery Case

* **Purpose/owner/authority:** Graduated automated/manual recovery coordination and assurance state; Identity & Access/PostgreSQL.
* **Attributes:** UUIDv7 id, claimant/account reference where known, requested method, assurance level, state, hold/review requirements, reviewer/approver references, expiry, completion/cancellation/failure timestamps, operation identity and version. It stores references to evidence, not raw identity documents or secrets.
* **Relationships:** belongs to Account where safely known; has Security Challenges and may cause Account/Credential/Session/Device changes.
* **Sensitive/immutability:** recovery evidence references, reviewer identity, reasons and security state are highly restricted; case history is append-only/superseding.
* **Lifecycle/actions:** `requested`, `proof_pending`, `additional_assurance`, `held_manual_review`, `completed`, `failed`, `expired` and `cancelled`; `start_recovery`, `submit_proof`, `approve_manual_recovery`, `complete_recovery`, `cancel_recovery`.
* **Policy/audit/integration:** non-enumerating claimant boundary; stronger assurance and second-person approval for privileged users; all completion effects remain Identity-only. Communications receives notice intent, not proof authority.
* **Persistence:** independent persistence is required for graduated assurance, manual review, duplicate/replay control, crash recovery and support audit.

#### 8. Reconciliation Case

* **Purpose/owner/authority:** Safe duplicate-identity detection, review and merge provenance; Identity & Access/PostgreSQL.
* **Attributes:** candidate accounts, detection basis, verification evidence references, reviewer/approver, conflict set, selected canonical account, status, timestamps, and reversal/correction references. No demographic-only automatic merge.
* **Relationships:** references Accounts and domain-owned records without directly rewriting them.
* **Sensitive/immutability:** matching evidence and reviewer notes are restricted; original identity and provenance are immutable; current reconciliation status is mutable through actions.
* **Lifecycle/actions:** `detected → candidate → review → approved/rejected/conflict → applied`; correction can create a compensating case, never erase history.
* **Policy/audit/integration:** high-risk review and verified control of both identities where practical; each affected Domain confirms its own record/provenance consequence. Audit the case and all source-domain commands.
* **Persistence:** independent persistence is required for human review, conflict, retry, provenance and reversal.

### D.2 Rejected separate resources

* **Email Change:** not a separate durable Resource for FP-001. It is an Account action plus a purpose-specific Security Challenge and durable consequences. A separate resource would duplicate account/email truth; the action still has its own explicit lifecycle and operation identity.
* **Verification Challenge, Recovery Challenge and Reset Token:** one Security Challenge with a closed purpose enum is safer and smaller than one table/resource per token flow. Purpose, fingerprint, expiry and single-use guards prevent cross-use.
* **Security Hold/Compromise:** authoritative state on Account plus revocation actions; a separate incident resource would overlap Audit/Operations. A later incident system may reference identity state.
* **Support Case:** no generic operator-work resource. Support invokes source-owned recovery/hold/release actions with named grants, reason and audit.
* **Role and Privilege Grant:** one Identity Grant resource with typed capabilities; separate role/privilege resources would flatten or duplicate the same identity-side authority.
* **Audit Event:** owned by Audit & Evidence, not identity truth. Identity emits minimum evidence.
* **Communication Message/Delivery:** owned by Communications; Identity emits intent containing only the necessary destination/reference and causal identity event.

## E. Relationships and ownership

These invariants are non-negotiable:

```text
identity role/grant       != relationship-owned business authority
canonical account email   != Communications subscriber/contact state
identity verification     != communication delivery evidence
account closure           != full privacy deletion orchestration
audit evidence            != identity business truth
authentication            != role/grant != consent/purpose != entitlement
```

Identity provides a current actor reference and identity-side grants. Privacy & Consent supplies current consent/purpose decisions. Practitioner, household, programme, community, event, entitlement, professional and other relationship owners retain their authority. Content is consumed from Content & Media. Audit records what Identity did without authorising it.

## F. Lifecycle state machines

### F.1 Account / identity

States: `unverified`, `verified`, `security_hold`, `closed_recoverable`, `closed_terminal`. Creation enters `unverified` only after all registration validations commit. `unverified → verified` is initiated only by consuming a valid email challenge. `unverified/verified → security_hold` is initiated by authorised compromise containment. `security_hold → verified` requires verified recovery and current security review. `verified/unverified/security_hold → closed_recoverable` is an authorised closure action. `closed_recoverable → verified` is governed restoration after recovery; `closed_recoverable → closed_terminal` is the identity-side terminal closure only when the applicable deletion/retention authority permits it.

Guards are canonical-email uniqueness, 18+ confirmation, terms/privacy acceptance, valid current actor/assurance, no contradictory hold, and current Privacy checks where required. Side effects are challenge/communication intent, credential/session/device revocation, security hold, and minimum audit evidence. Registration retry is idempotent by client operation identity where supplied and by canonical-email uniqueness otherwise; public responses remain non-enumerating. Account state is never inferred from delivery, LiveView assigns or cache. A mistaken hold is corrected by an authorised release; terminal closure cannot be reversed by login or recovery and does not imply complete cross-domain deletion.

### F.2 Email verification

States: `issued`, `valid`, `consumed`, `expired`, `superseded`, `revoked`. Issuance follows account creation or an allowed resend. Resend atomically supersedes the prior active challenge for the same account/purpose and creates one durable communication intent. Consumption locks or conditionally updates the challenge and Account in one short transaction; exactly one consumer can establish verification. Expiry is time-derived and cleanup is non-authoritative. Replayed, expired or superseded secrets return a safe generic result and create bounded audit/telemetry. Delivery or provider status never changes `verified`; only proof consumption does. Correction is a new challenge, never mutation of consumed history; a mistaken revocation is handled by a new issuance.

### F.3 Credential

States: `absent`, `active`, `replaced`, `revoked`. Password authentication validates a hash with bounded cost and generic failure. Reset replaces the credential only after a valid reset/recovery proof, invalidates affected sessions/devices and records a security event. A replacement is atomic with its credential version and revocation consequence. Old credentials cannot authenticate; retries with the same operation identity return the committed result. Credential revocation is not undone; correction requires a new authenticated credential and evidence.

### F.4 Session

States: `active`, `expired`, `revoked`, `logged_out`. Creation occurs after successful authentication and current account/hold/verification/assurance checks. Logout revokes one session; sign-out-all revokes all active sessions for the account. Recovery, credential change, email change where risk requires, compromise and grant/security changes revoke the relevant session set. Expiry is both inactivity and absolute; validation rejects either. Browser reconnect and LiveView remount reconstruct from the secure cookie and durable current state; a connection process never grants authority. Revocation racing login is resolved by transaction/version ordering: a session created before a committed global-revocation boundary is revoked, and a login after it rechecks current security state. Revocation is not reversed; correction requires a new session after reauthentication.

### F.5 Device assurance

States: `pending`, `trusted`, `expired`, `revoked`. Trust requires explicit consent and an authenticated session; use requires a current unrevoked fingerprint, expiry and account security state. Suspicious activity, credential changes, recovery, global logout or explicit user revocation terminates trust. It is never accepted for high-risk step-up. Duplicate trust requests converge on one active device assurance by account/fingerprint purpose key. Revocation is not reversed; correction requires fresh consent and a new device assurance.

### F.6 Recovery

Recovery is a lifecycle on Account plus `RecoveryCase` semantics and Security Challenges: `requested → proof_pending → additional_assurance → held/manual_review → completed`, with `failed`, `expired` and `cancelled` terminal outcomes. Normal recovery uses a verified channel and single-use proof; missing ordinary assurance enters a temporary hold and manual review. Privileged recovery requires stronger assurance and second-person approval. Completion changes only Identity authority, rotates/revokes credentials as applicable, removes stale sessions/devices, and sends security notices. It never creates consent, entitlement, relationship or professional authority. Duplicate requests are safe, simultaneous attempts cannot lower assurance, replay is rejected, and an incomplete/crashed transition is resumed from durable state. Recovery completion is not reversible by replay; correction requires a new reviewed case.

### F.7 Primary-email change

The action lifecycle is `requested → reauthenticated → new_address_pending → confirmed → delayed/reviewed → applied`, with `cancelled`, `expired`, `rejected` and `held` terminals. Reauthentication proves control of the current session; a new-address challenge proves the new address; old-address notification is a Communications consequence, not proof. The current canonical email remains unchanged until the authoritative apply transaction succeeds. Concurrent changes serialize on Account version and active-change purpose; the newest explicitly accepted operation supersedes older pending challenges. Loss of old address uses graduated recovery, never informal support override. Applying the change rotates relevant session/device assurance according to risk policy, preserves old-address provenance and audits the consequence.

### F.8 Identity grants

Ordinary states are `requested`, `assigned`, `active`, `expired`, `revoked`; break-glass adds `reviewed`. Assignment requires an authorised approver distinct from the subject where required, valid scope/reason, start and expiry/review. Current policy reads active grants and rejects expired/revoked grants. Revoke wins over concurrent use once committed; assignment and revoke use grant version/conditional update. Break-glass is named, MFA-protected, narrow, short-lived, alerted and post-reviewed; it never grants clinical or relationship authority. Expiry is a guard at read/action time even if cleanup has not run. Revocation is corrected only by a new separately approved grant, never by reopening history.

### F.9 Duplicate identity reconciliation

States: `detected`, `candidate`, `review`, `approved`, `rejected`, `conflict`, `applied`, `corrected`. Detection may use canonical email or strong verified evidence; name/demographics alone cannot merge. Review confirms control and asks each affected Domain to resolve purchases, entitlements, assessments, health, plans, journals, community and professional provenance. Apply creates one canonical identity and durable references while preserving original account ids/history; it does not directly merge other Domain truth. Conflicts block apply. Duplicate apply returns the prior committed case; a wrong decision is corrected with compensating provenance, not destructive deletion.

## G. Action model

All actions run through Ash/application interfaces, use the smallest transaction that establishes the source truth, and return authoritative state. External I/O is post-commit. Inputs are untrusted intent; actors are current server actors.

| Action | Actor/guard and validation | Transaction, retry and concurrency | Consequences/evidence |
|---|---|---|---|
| `register` | Anonymous; required minimum fields, canonical email, 18+, terms/privacy and language; non-enumerating duplicate response | Unique canonical-email constraint plus operation id; one Account and Credential transition; concurrent same-email requests converge | Verification intent after commit; registration event; no account existence leak |
| `issue/resend_verification` | Account owner with allowed unverified state; purpose and resend admission boundary | Replace active challenge conditionally; one active purpose challenge; duplicate request id returns result | Durable Communications intent; requested/superseded audit; delivery cannot verify |
| `consume_verification` | Anonymous proof presenter; fingerprint/purpose/expiry/Account checks | Atomic challenge-consume + Account verify; replay safe | Verification evidence and optional session consequence; no raw token |
| `authenticate_password` | Anonymous; email/password; current Account state, hold and verification capability checks | Hash outside DB lock where possible; create Session only after re-read; generic failure | Login success/failure class, risk signal; no enumeration |
| `authenticate_magic_link` | Presenter of one-purpose challenge; optional launch method; current state | Same single-use challenge transaction and Session creation | Login/verification result; challenge replay evidence |
| `logout` / `revoke_session` | Current account or scoped support/admin actor | Conditional session revoke; duplicate is success if already revoked | Session event and audit where material |
| `revoke_all_sessions` | Current actor with step-up for sensitive contexts or scoped support action | Account/session-set revocation boundary; concurrent login rechecks boundary | Security event, audit and optional notice |
| `start/complete_recovery` | Account claimant; recovery proof or scoped manual reviewer; stronger rules for privileged accounts | Recovery case and challenge idempotency; completion serializes with email/credential changes | Credential/session/device changes, security notice intent, audit |
| `request/apply_email_change` | Current actor; reauthentication, new proof, current Account version | Pending challenge then atomic canonical-email uniqueness apply; old email remains until commit | Old-address notice intent, session review, audit |
| `place/release_security_hold` | Security-authorised staff/system; reason, scope, current grant; release requires verified recovery/review | Account state conditional transition; hold wins over stale actions | Session/device revocation, security audit, alert/notice intent |
| `assign/revoke_grant` | Named approver with MFA; no self-approval; scope/reason/expiry | Unique active assignment key and grant version; revoke is idempotent and wins after commit | Audit, privilege-change notice/telemetry |
| `open/approve/apply_reconciliation` | Scoped staff; verified control and affected-domain review | Case state/version; apply is one identity transaction plus durable domain commands, not cross-domain direct writes | Provenance and conflict evidence; reconciliation audit |

Error categories are stable and safe: `invalid_input`, `invalid_or_expired_proof`, `authentication_failed`, `verification_pending`, `restricted`, `requires_step_up`, `requires_manual_review`, `conflict`, `already_completed`, `temporarily_unavailable`, and `internal_failure`. Public surfaces collapse existence-sensitive categories; internal audit preserves precise classes without secrets.

## H. Policy / permission model

Policy composition is:

```text
current actor identity
→ current session and assurance
→ Identity-side grant/scope/expiry
→ owning Domain relationship authority
→ Privacy purpose/consent where applicable
→ action-specific invariant and risk guard
```

Authentication proves an actor; it does not authorise a role. Identity grants do not authorise practitioner relationships, household membership, entitlements, consent, health access or purpose. Protected actions re-read current actor, session revocation, Account security state, active grant and all owning-Domain authority at the action boundary. Long-lived LiveViews must not rely on stale assigns for protected actions.

Field policy is deny-by-default: raw password, challenge secret, session token and device fingerprint are never returned; names/email/language are projected only to the minimum actor/context; support sees minimum necessary identity and security status. There is no universal `Super Admin`. Break-glass is a distinct exceptional path with named identity, MFA, reason, scope, expiry, alert, audit and review.

## I. Cross-domain seams

* **Communications:** Identity emits verification, recovery, email-change and security-notice intent after authoritative transitions. Communications owns subscriber/contact relationship, message body/template, provider and delivery evidence. `delivered != verified`; provider outage leaves Identity truth unchanged and creates pending/retry/terminal visibility.
* **Privacy & Consent:** Identity reads/checks current purpose/consent for applicable actions and supplies identity/closure references. Privacy owns consent, withdrawal, retention and full deletion orchestration. Identity does not infer consent from login, language or support.
* **Audit & Evidence:** Identity emits minimum material security, recovery, grant, support, reconciliation and revocation evidence. Audit owns restricted append-only evidence; evidence cannot authorize or rewrite identity state.
* **Content & Media:** Identity/public surfaces consume approved bilingual governed content. Identity owns no content lifecycle.
* **Future relationship Domains:** Identity supplies actor id and identity-side grants. Practitioner, household, programme, community, event, entitlement and other business relationships remain with their owners.

## J. Durable consequence / async boundary

The Account transition and its identity invariant are Class A synchronous work. A verification/recovery/email-change/security notice intent is a must-not-lose Class B consequence: establish a minimal durable intent atomically with the source transition, commit, execute through the Communications-owned durable path, retry with business idempotency and re-read current preconditions. Oban is the default executor under Architecture Law, but no worker name/queue is frozen here.

Session/device revocation required to prevent access is atomic Identity work. LiveView refresh, PubSub freshness and analytics are Class C observations and may be lost, delayed, duplicated or reordered. They never establish verification, revocation, recovery or grant truth. Provider outage yields retry/terminal failure and support-visible reconciliation; it never causes a guessed success. No generic event bus or durable PubSub delivery is introduced.

## K. OQ-034 Architecture Evaluation

### K.1 Recommended smallest path

The primary hypothesis is maintained Ash Authentication plus its Phoenix integration, at implementation-time compatible current versions, configured for the existing Ash 3.x application:

* email/password as the required strategy and optional email magic-link strategy around the same Account;
* Argon2id through the maintained Ash Authentication hash-provider boundary, with cost benchmarked and bounded for the deployment budget;
* confirmation add-on for new-account email proof and monitored primary-email changes, with interaction required where the browser must not mutate state by GET;
* password reset/recovery strategy for ordinary recovery, extended by Identity-owned graduated/manual Recovery Case and security-hold actions;
* Token Resource with stored token presence enabled for durable revocation semantics where needed, secret material hashed/fingerprinted, one-purpose challenges, bounded expiry and no raw token persistence;
* secure HttpOnly, Secure, appropriate SameSite browser cookie transport; session identity is server-governed and linked to a durable Session record or framework token reference. No bearer API is needed for FP-001: `API/Bearer = NONE` unless a later approved client requires it;
* Phoenix/Plug browser CSRF protection on cookie-authenticated state-changing requests, with LiveView event handling remaining server-authorised and current-state checked;
* Ash Authentication Phoenix LiveSession/on-mount integration to reconstruct authenticated subjects on LiveView mount/reconnect, followed by Identity policy checks for current session, grant and hold state. A LiveView process is never session authority;
* participant MFA remains optional; privileged staff/practitioner MFA and high-risk step-up are integration boundaries requiring a maintained MFA authenticator and proof, not a bespoke FP-001 cryptosystem;
* trusted device is an Identity-owned persisted Device Assurance record and is not silently delegated to browser local storage or a library convenience flag;
* secrets/keys are supplied by deployment secret management, rotated with overlapping verification and explicit revocation/recovery testing; no signing secret is committed.

### K.2 What the framework handles and what Identity owns

Ash Authentication provides the maintained strategy, password hashing boundary, token/challenge plumbing, confirmation/reset flow, authentication plugs and Phoenix LiveView subject propagation. The official documentation states that the current ecosystem supports password and magic-link strategies, confirmation, a Token Resource, token presence storage and Phoenix LiveSession integration.

Identity still owns Account lifecycle, verified-capability gates, graduated/manual recovery, holds, session/device policy, email-change delay/risk consequences, identity-side grants, duplicate reconciliation, non-enumerating public result mapping, domain seams, audit minimisation and all current-authority rechecks. Communications owns message intent/delivery; the library is not permitted to become provider or verification authority.

### K.3 Extension and risk boundary

The main lifecycle mismatch is that a turn-key authentication package does not by itself encode NewYou's graduated manual recovery, domain-aware merge, scoped staff/break-glass grants, relationship/consent composition or exact session/device invalidation policy. Those are application/domain actions around the framework boundary. The framework's token-presence and stored-token options must be proven for the required revocation model; a self-contained token accepted without presence would be unsafe for global revocation.

Custom authentication is rejected unless proof shows a frozen requirement cannot be met safely by the maintained path. A custom password, token, cookie or cryptographic implementation would increase attack surface, maintenance and rotation risk without an identified requirement benefit. A separate identity provider is also rejected for FP-001 because it adds a new operational/provider boundary while the required local email/password flow is available.

### K.4 Evidence required before implementation acceptance

The later tracer-bullet/proof boundary must verify pinned compatible versions, Argon2id cost/resource envelope, confirmation and reset replay/expiry, token hashing/presence/revocation, cookie/session fixation behaviour, CSRF, LiveView disconnected/connected reconstruction, multi-node shared PostgreSQL behaviour, restart/reconnect, global/session-specific revocation, manual recovery/hold races, privileged MFA/step-up and secret rotation. It must include failure injection and no-enumeration tests. This is evidence still required, not a final proof classification.

### K.5 Current technical source record

Research was limited to OQ-034 and used current official primary documentation accessed 2026-09-01:

* [Ash Authentication v4.14.2 — Get started](https://ash-authentication.hexdocs.pm/get-started.html): current password/magic-link installation path, Token Resource, secret handling and Plug/session/bearer integration.
* [Ash Authentication v4.14.2 — Tokens](https://ash-authentication.hexdocs.pm/tokens.html): token presence storage, `store_all_tokens?`, sign-in tokens and LiveView exchange use.
* [Ash Authentication v4.14.1 — Confirmation](https://ash-authentication.hexdocs.pm/dsl-ashauthentication-addon-confirmation.html): confirmation for account/email changes, token lifetime, interaction and hijacking protections.
* [Ash Authentication Phoenix v2.17.2 — LiveSession](https://ash-authentication-phoenix.hexdocs.pm/AshAuthentication.Phoenix.LiveSession.html): copying authenticated subjects into LiveView session/assigns and token-expiry/presence behaviour.
* [Plug v1.20.3 — Plug.Session](https://plug.hexdocs.pm/Plug.Session.html): cookie/session options and CSRF consideration.
* [Phoenix LiveView v1.2.11 — LiveView](https://phoenix-live-view.hexdocs.pm/Phoenix.LiveView.html): LiveView process and `on_mount` authentication boundary.

Versions are evidence snapshots, not package pins or authority amendments.

## L. OQ-034 Resolution Recommendation

**READY_FOR_EXPLICIT_RESOLUTION**

Recommended resolution: approve the maintained Ash Authentication/Ash Authentication Phoenix path for FP-001 email/password plus optional magic-link authentication, Argon2id, confirmation/reset facilities, stored/presence-checked tokens, secure first-party browser cookies, Phoenix CSRF and LiveView integration, with the Identity-owned Account/Session/Device Assurance/Recovery Case/Grant lifecycles and current-authority policy described in this dossier. `API/Bearer = NONE` and trusted-device cryptography remain outside the public FP-001 API; trusted device is an Identity-owned persisted record. Exact versions and cost values are selected and benchmarked at implementation/proof time within the approved compatibility window.

This satisfies Product and Architecture law because it keeps one canonical identity, uses maintained security primitives, preserves PostgreSQL durable authority, supports revocation/reconstruction across nodes, treats email proof as server-authoritative, composes authentication with current grants/relationships/consent, and avoids a universal privileged bypass. Alternatives rejected are custom authentication, external identity-provider infrastructure, browser-local session authority and a Redis/ETS/GenServer identity store.

Residual risks are package/configuration drift, hash-cost overload, token-presence misconfiguration, incomplete MFA integration, recovery abuse and provider outage. Required evidence is listed in K.4 and remains a later executable proof obligation. The authority document to amend later is `docs/00_platform/01_DECISIONS_v1.2.2.md`, under owner-controlled `OQ-034`; this PR must not amend it.

Suggested concise resolution wording:

> Resolve OQ-034 for FP-001 by approving maintained Ash Authentication and Ash Authentication Phoenix, at then-current compatible pinned versions, for email/password plus optional magic-link authentication, Argon2id password hashing, confirmation/reset, stored presence-checked tokens, secure first-party browser sessions, CSRF protection and LiveView actor reconstruction. Identity & Access remains authoritative for Account, verification gates, Session/Device Assurance, graduated recovery, revocation, scoped grants, compromise, duplicate reconciliation and all current-policy checks. API/bearer tokens are not required for FP-001. Exact cost, MFA/step-up integration, key rotation and revocation/restart/multi-node behaviour require executable proof before development-entry acceptance.

## M. OQ-035 boundary

OQ-035 is **not resolved**. Admission attaches in layers: Cloudflare edge → application action boundary → shared distributed velocity/risk mechanism where required → account/device/network signals → temporary challenge or recoverable hold. Required dimensions must support canonical action/purpose, account when known, network/edge identity, device signal and deployment-wide time window without revealing account existence. Public failure is non-enumerating; internal telemetry/audit remains precise. Cross-node correctness is required for any control relied on under multi-node traffic. PostgreSQL is not the immediate high-velocity counter store. Hammer/shared semantics remain an evidence candidate only. Final thresholds, escalation levels and false-positive recovery require OQ-035 owner approval and proof.

## N. Data integrity and indexes

PostgreSQL is the default durable authority. Every persistent resource requires UUIDv7 opaque ids, foreign keys, not-null/check constraints for closed enums and timestamps, immutable provenance/created fields, optimistic version where concurrent mutation exists, and bounded cleanup of expired challenges/sessions/devices.

Required constraint/query decisions are:

| Resource | Integrity and critical indexes |
|---|---|
| Account | unique canonical email; indexes on canonical email lookup, state+verification, security hold, and closure review; FK-safe references from all child resources |
| Credential | unique account+method; index account+active method; sensitive hash excluded from public projections |
| Security Challenge | unique secret fingerprint; index account+purpose+active/expiry; index expiry for cleanup; conditional uniqueness for one active challenge per account/purpose; FK to Account/Recovery Case |
| Session | unique token fingerprint; index account+active, account+last-seen, expiry and revocation boundary; FK to Account; no raw cookie/token column |
| Device Assurance | unique account+device-fingerprint/purpose while active; index account+active and expiry; FK to Account |
| Identity Grant | index subject+active+expiry, role/scope review and revocation; conditional uniqueness only for the exact grant identity key; FK to Account; immutable approver/reason history |
| Recovery Case | unique active case/operation identity as applicable; index account+state+expiry, reviewer queue status+updated, and claimant-safe lookup; FK to Account where known; no raw recovery evidence |
| Reconciliation Case | indexes each candidate account, status+updated, selected canonical account and conflict review; FKs preserve source accounts; no cascade that destroys provenance |

Query paths must be bounded: login by canonical email, session validation by token fingerprint, protected action by session/account/grant state, challenge by fingerprint/purpose, and support lists by bounded status/time pages. No login/session validation scans, load-all session/grant history or unbounded reconciliation query is permitted. Exact SQL/migrations are deferred to implementation and proof.

## O. Concurrency and idempotency

| Race | Authority → invariant → strategy → recovery/evidence |
|---|---|
| Duplicate/same-email registration | Account → one canonical email → unique constraint plus operation id → return committed/non-enumerating result; audit duplicate class |
| Resend/verification replay | Challenge+Account → one active challenge and one verify transition → conditional update/version → expired/replay is terminal; evidence records safe result |
| Verification vs email change | Account → verified proof cannot apply to wrong purpose/email → purpose-bound challenge and Account version → one wins in transaction; later request reissued |
| Login vs revocation/compromise | Session/Account → no session survives committed revocation/hold → transaction boundary/revocation epoch and re-read → stale session rejected; multi-node test |
| Recovery vs login/email change | Account/Recovery Case → recovery cannot lower assurance or overwrite newer email → Account version, hold and serialized sensitive transitions → pending case resumes/cancels safely |
| Simultaneous recovery/support recovery | Recovery Case → one assurance path completes; privileged second-person review → unique active case/conditional state transition → duplicate returns prior result; audit reviewers |
| Grant assign/revoke | Grant → revoke wins after commit and expired grant cannot authorize → version/conditional update → action rechecks current grant; audit both operations |
| Duplicate reconciliation | Reconciliation Case → one applied canonical decision with history → case version/idempotency and source-domain review → conflict blocks; compensating correction |
| Crash during authoritative transition | PostgreSQL → no half-transition → short atomic transaction and durable intent → retry/reconcile by operation id; crash-window test |
| Duplicate/reordered async consequence | source transition + intent → one logical notice/consequence → durable intent key and idempotent consumer → retry/terminal failure reconciliation; provider evidence separate |

Distributed locks are not required by the model. PostgreSQL uniqueness, conditional updates, row/version coordination and durable operation identity are the default; stronger coordination requires proof of a specific invariant.

## P. Hot / warm / cold data

* **HOT:** canonical-email login lookup, active session validation, active challenge proof, active hold/grant checks, and OQ-035 velocity state. PostgreSQL indexed authority for identity/session/challenge/grant; velocity mechanism remains OQ-035 shared and non-authoritative. No cache may bypass revocation. Proof: p90 ≤100ms for suitable hot interactions excluding password hashing/provider latency, no scans, burst and multi-node tests.
* **WARM:** bounded active-session/device lists, recent recovery/support/reconciliation status and current grant review projections. PostgreSQL first; safe rebuildable read acceleration only after evidence. Pagination required. Empty-cache and revocation tests required.
* **COLD:** credential history metadata, consumed/expired challenge history, reconciliation provenance and security evidence. PostgreSQL/Audit authority, append-only or superseding records, retention-controlled bounded queries. No participant load-all.

## Q. Mechanism decisions

| Mechanism | Status | Decision |
|---|---|---|
| PostgreSQL | REQUIRED | Durable structured authority for all accepted Identity resources, constraints, current state and operation evidence. |
| Redis | POTENTIALLY_APPLICABLE | Only for OQ-035 distributed velocity/risk state if proof selects it; never identity/session/grant authority and exact keys/TTL/failure mode remain unresolved. |
| ETS | NONE initially | No identity authority or required cache is demonstrated; reconsider only for reconstructible safe lookup acceleration. |
| Cachex | NONE initially | No cache abstraction is justified before measured lookup pressure and invalidation proof. |
| GenServer | NONE | No process owns durable identity state or required global coordination. |
| Oban | APPLICABLE | Default durable executor for post-commit Communications/security consequences when the affected contract is ready; no generic event bus. |
| PubSub | APPLICABLE | Best-effort revocation/freshness observation only; never durable delivery or authorization. |
| Browser-local storage | NONE for authority | May hold safe UI convenience only; no session, challenge, credential, grant or authoritative security secret. |
| CDN | NONE for Identity authority | Public governed content may use approved content policy; authenticated identity/session responses are not CDN authority. |
| API/bearer tokens | NONE for FP-001 | No approved native/API consumer requires them; re-open only through a later scope decision. |
| Trusted-device library state | NONE | Device Assurance is persisted Identity state with explicit expiry/revocation. |

## R. Security review

Argon2id hashes passwords with benchmarked bounded cost; raw passwords/tokens never enter storage/logs. Challenge secrets are random, purpose-bound, fingerprinted, single-use, expiring and superseded/revoked. Cookies are Secure, HttpOnly and appropriate SameSite; session id is rotated on authentication and sensitive transitions to prevent fixation. Plug/Phoenix CSRF protects cookie-authenticated mutations; LiveView assigns and params remain untrusted.

Public registration/login/recovery responses do not reveal account existence or challenge validity beyond safe categories. Cloudflare/application/shared velocity controls address stuffing/brute force; OQ-035 retains thresholds. Recovery and email change require verified proof, reauthentication, holds/delay where risk demands and old-address/security notices. Current grant/session/relationship/consent checks prevent stale authorization and privilege escalation. Compromise revokes sessions/devices, freezes sensitive actions and requires verified recovery. Staff recovery is named, scoped, MFA-protected and second-person controlled for privileged accounts. Break-glass is exceptional, expiring, alerted and reviewed.

Key rotation uses overlapping verification/controlled retirement and tests old-session/token treatment. Logs and audit redact raw email where unnecessary, raw tokens, hashes, passwords and recovery evidence. Timing and error mapping are deliberately generic on public sensitive paths. Concurrent compromise response is fail-closed for sensitive actions. Product rules prevent unfinished spaces and relationship misuse; Domain invariants enforce state/ownership; Architecture supplies secure transport, current server authority, durable storage and async semantics; OQ-034 selects the maintained auth path; OQ-035 later selects thresholds; executable proof validates the whole chain.

## S. Privacy review

Registration collects only first name, surname, canonical email, credential, preferred language, 18+ confirmation and terms/privacy acceptance; phone and city are optional. It does not collect health, medical or full DOB data. Email is personal identity data; credential hashes, challenge fingerprints, session/device security data, IP/network/device signals and recovery evidence are sensitive security data and are restricted/minimised. Support receives minimum necessary context.

Identity keeps canonical email distinct from Communications contact state, security evidence distinct from analytics, and closure distinct from full deletion. Account closure prevents ordinary access according to Identity policy; Privacy & Consent owns full deletion orchestration, retention categories, legal holds, export and non-resurrection replay. No FP-006 deletion design is created here.

## T. Frontend contract

The frontend submits untrusted intent and renders authoritative categories only. It may rely on:

| Operation | Authoritative categories |
|---|---|
| Registration | accepted/verification pending; invalid input; duplicate or ambiguous safe response; temporarily unavailable |
| Verification | pending; complete; invalid/expired/replayed proof; restricted |
| Resend | accepted/pending; rate-limited or temporarily unavailable without enumeration |
| Login | authenticated; invalid credentials; unverified/restricted; requires step-up; temporarily unavailable |
| Recovery | started; completed; pending/manual review; expired/failed/cancelled; restricted |
| Session | active; revoked; expired; requires reauthentication |
| Email change | pending new-address confirmation; applied; cancelled/expired/conflict/held |
| Support recovery | accepted for review; requires second approval; completed; rejected; audited |

No pages, routes, components or screen state are designed here. Protected spaces must remain inaccessible until current verified identity, session, grant, relationship, consent and entitlement checks succeed.

## U. Observability and audit

Operational telemetry uses bounded-cardinality metrics for registration attempts/success, verification requested/consumed/expired/replayed, login result classes, recovery started/completed/rejected, session revocation, grant changes, support/reconciliation actions, suspected abuse, hash latency/resource use, challenge/session query latency, DB locks/pool pressure, queue age/retries and provider failure.

Security audit is separate and restricted: account lifecycle, verification proof, credential/security changes, recovery/hold/release, session/device revocation, grant/break-glass, support-assisted action, reconciliation/conflict and material policy denials. It records actor, target, reason/scope, correlation, result and causal references, never credentials, raw secrets or unnecessary personal payloads. Analytics receives only approved derived facts. Telemetry failure reduces visibility, not identity correctness.

## V. Test contract

Future executable work must include resource/action, policy, field-policy, state-transition and invalid-transition tests; property tests for one canonical email, one-use proof, no authority from delivery and no grant beyond current scope; idempotency/retry/concurrency tests for every table in section O; token replay/expiry, session fixation, CSRF, cookie flags, enumeration, stuffing/rate boundary and logging-redaction tests; recovery/manual-review/hold and email-change races; session/device/global revocation and restart/reconnect/multi-node reconstruction; grant self-approval/break-glass expiry; duplicate reconciliation/provenance/conflict/correction; audit completeness/minimisation; provider outage and durable consequence tests; hash-cost and bounded-resource tests; and failure/degradation tests proving no guessed identity, verification or access.

The proof must test empty-cache/restart behaviour for any later acceleration, queue duplicate/reorder semantics, current-policy re-read on long-lived LiveView actions, secret rotation, and representative burst/contention. It must not be replaced by a clean happy-path test or final proof label at dossier time.

## W. Recommended future folder/module structure

No source directories are created. If implementation is authorised, follow the existing Ash/Phoenix convention if one is established; otherwise use the smallest domain-oriented structure:

* `NewYou.Identity` (or the repository's established Identity & Access Domain context) for Ash code interfaces and boundary orchestration;
* `NewYou.Identity.Account`, `Credential`, `SecurityChallenge`, `Session`, `DeviceAssurance`, `IdentityGrant` and `ReconciliationCase` as coherent Ash Resources;
* an application-owned recovery/email-change boundary module only if the action orchestration cannot remain on the relevant resource; no generic `Services` or `Utils` dump;
* an Ash Authentication adapter/configuration boundary for maintained strategies, hash provider, token resource and Phoenix plugs;
* a Communications intent adapter boundary, not provider calls inside identity transactions;
* policy modules only for genuinely shared, independently testable current-session/assurance or staff/break-glass composition;
* tests mirroring each resource/action and cross-domain seam.

Resource names represent business concepts, not database tables, screens or workflow buttons.

## X. Open questions / remaining gates

### `BLOCKS_OQ034_RESOLUTION`

* Owner must accept the recommended maintained Ash Authentication path and concise wording, then amend the authoritative Decisions record in a separate owner-controlled task.
* Implementation/proof must verify compatible versions, token-presence revocation, Argon2id cost, MFA/step-up integration, key rotation and multi-node/restart semantics.

### `BLOCKS_PHASE7C`

* `OQ-034` must be explicitly resolved before Phase 7C/development-entry acceptance.
* Remaining Phase 7B work includes the separately authorised Communications dossier and any conditional dossiers only if their current law proves insufficient. Phase 7C must consume their contracts without inventing identity semantics.

### `BLOCKS_RELEASE_ONLY`

* `OQ-035` thresholds/escalation/false-positive recovery.
* `OQ-036` notification provider/channel policy.

### `JIT_IMPLEMENTATION_DETAIL`

* Exact package pins, Ash action syntax, migration shape, field names, TTL values, queue/worker names, cookie key, deployment secret product, pool/concurrency values, MFA product, and exact audit/metric schemas.

### `FUTURE_ONLY`

* Social login, passkeys, API/bearer clients, native clients, generic tenancy, full deletion orchestration, operator-work capability, men’s/specialist spaces and future relationship Domains.

No item is classified as a blocker merely because implementation detail is not yet selected.

## Y. Decision register

| ID | Decision | Authority basis | Alternatives considered | Why selected | Evidence required | Revisit trigger |
|---|---|---|---|---|---|---|
| IAM-01 | Eight-resource minimum set | Domain Map §6.1; Phase 7A §9 | one resource per workflow; table-driven model | Independent invariants/lifecycles without resource sprawl; recovery review requires durable state | Ash resource/policy tests | New independent lifecycle appears |
| IAM-02 | PostgreSQL identity authority | Architecture §§7–8 | Redis/ETS/cache/process authority | durable, reconstructible, constraint-capable | restart/multi-node proof | measured bottleneck with preserved authority |
| IAM-03 | Maintained Ash Authentication primary hypothesis | OQ-034; Ash official docs | custom auth; external IdP | maintained primitives fit Ash/Phoenix and reduce crypto risk | K.4 proof set | material unmet frozen requirement |
| IAM-04 | Argon2id with benchmarked bounded cost | Architecture §6.1; DEC-244 | unbounded/high-cost hash; weaker fallback | preferred frozen direction with resource governance | hash benchmark/burst proof | unacceptable resource envelope |
| IAM-05 | Secure browser session; API/bearer none | Architecture §6.1; FP-001 scope | public bearer API; browser-local token | smallest approved web boundary | fixation/CSRF/revocation proof | approved client scope |
| IAM-06 | Persist Device Assurance | DEC-249; 21J.6 | browser-only trust; no trust | locked revocable/expiring trust needs authority | revocation/step-up proof | Product scope removes trusted devices |
| IAM-07 | Account action, not Email Change resource | ownership/minimum model | separate change resource | avoids duplicate email truth while preserving lifecycle | race/rollback tests | independent retention/review needed |
| IAM-08 | Generic Security Challenge by purpose | replay/control invariant | separate token resources | fewer resources with closed purpose guard | cross-purpose/replay proof | purpose-specific independent retention emerges |
| IAM-09 | Recovery Case and reconciliation remain durable concepts | DEC-250/252 | ephemeral support workflow | manual review, provenance and crash recovery require state | duplicate/manual/recovery proof | authority moves upstream |
| IAM-10 | Oban for durable consequences; PubSub observation only | Architecture §§8–9; DEC-267 | generic event bus; PubSub delivery | preserves must-not-lose boundary and small scope | crash/duplicate/reorder proof | Communications contract selects another lawful executor |
| IAM-11 | Redis/ETS/Cachex/GenServer not identity authority | Architecture §7.3; OQ-035 | multilayer auth stack | no evidence requires acceleration yet | empty-cache/failure proof if introduced | measured need and explicit contract |
| IAM-12 | OQ-034 ready for explicit owner resolution | OQ-034 owner-controlled | silently resolve; defer indefinitely | architecture hypothesis and evidence boundary are concrete | owner decision plus K.4 proof | owner finds contradiction |

## Z. STOP review

No hard-stop condition was encountered. Identity ownership remains compatible with frozen Domain Law; no Product or Architecture amendment, new Domain, Commerce work, Communications implementation, OQ-035 threshold, Decisions edit, Phase 7C work, final proof classification, TB/VS/HH/TOON, source code, migration, package install, database runtime, browser test or Atlas expansion was started. If independent review finds a contradiction or a requirement for another file, work must stop and route to the owning authority.

## AA. Final state

```text
PHASE 7A: COMPLETE
IDENTITY & ACCESS DOSSIER: COMPLETE
COMMUNICATIONS DOSSIER STARTED: NO
OTHER CONDITIONAL DOSSIERS STARTED: NO
OQ-034 AUTHORITY STATUS MODIFIED: NO
OQ-034 RECOMMENDATION: READY_FOR_EXPLICIT_RESOLUTION
OQ-035 RESOLVED: NO
PHASE 7C STARTED: NO
FINAL PROOF CLASSIFICATION: NOT FINALISED
IMPLEMENTATION STARTED: NO
MIGRATIONS CREATED: NO
ATLAS EXPANDED: NO
MERGED: NO
```

Independent review is now required.
