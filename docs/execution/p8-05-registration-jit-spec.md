# P8-05 registration JIT specification

**Status:** Candidate for independent planning review
**Plane:** WELL-6, currently in Planning
**Planning baseline:** `main@dad135827cb1107634585a58c25c3d9f53fab437`
**Scope:** Specification and proposed ticket decomposition only. This file does not change governed authority or authorize implementation.

## Purpose and current boundary

P8-05 is the first production-path Phase 8 proof slice. Its bilingual browser path presents approved launch and safety content before registration and enforces the required 18+ and exact Terms/Privacy acceptance gates before Account creation. The TB-001 PostgreSQL acceptance transaction commits one Identity-owned Account with an active password credential and its hash, its canonical active PMR, a verification Token, the selected Audit EvidenceObligation, a Communications MessageIntent, and both required owner-specific initial durable scheduling consequences: Communications delivery scheduling reconstructable from `MessageIntent.id` and Audit E2 materialisation scheduling reconstructable from `EvidenceObligation.id`. Password validation, Account creation, credential activation, and password-hash establishment are one accepted Identity transition. Raw passwords are never persisted.

The Account remains unverified and has no Session. The participant sees a localized verification-pending page. P8-05 does not consume verification proof, log the participant in, execute Communications or Audit durable workers, contact a provider, or certify the full TB-001 proof.

The current authority is Open Work v1.2.80, especially §12.36. WELL-5 / P8-04 is complete, and the harness is available to later authorized Phase 8 slices. The current TB-001 proof remains `INCOMPLETE / COVERAGE-INCOMPLETE`, ten required business/browser manifests remain unavailable, and Phase 8 is not certified. Phase 9 remains `NOT STARTED / NOT AUTHORISED`.

This spec follows the outcome contract in Plane WELL-6. Live GitHub authority controls if a Plane description or this planning artifact becomes stale. It does not change Product, Architecture, Domain, Roadmap, TB-001, or the JIT dossiers.

## Fixed design decisions

| Area | P8-05 boundary |
|---|---|
| Identity ownership | Identity owns Account, canonical email, PMR, verification Token, and registration/resend operation truth. PMR remains Account-owned truth, not a separate Resource, login name, secret, or authorization mechanism. |
| Required registration data | Collect the complete DEC-027 minimum set: first name, surname, email, authentication credential (password), preferred language, 18+ confirmation, and Terms/Privacy acceptance. The selected Afrikaans or English locale becomes the Account's preferred language. Phone and city remain optional under DEC-027 and are outside this proof path. Identity validates the credential, marks it active, and establishes its password hash in the same transition as Account creation; this does not create a Session or log the participant in. Raw passwords are never persisted. |
| Entry and account gates | The participant selects Afrikaans or English and sees the exact approved launch and safety content before registration. Identity enforces 18+ confirmation and acceptance of the exact approved Terms and Privacy versions before creating an Account. A failed or missing gate creates no Account or PMR. |
| Registration operation | The browser creates one opaque operation ID for each logical registration and reuses it across retries. Identity binds the ID to one immutable request. Reuse with changed input safely rejects; a corrected request uses a new ID. |
| Duplicate email | A distinct operation for an existing canonical email returns the same neutral public response as a newly accepted registration. It creates no second Account, PMR, Token, EvidenceObligation, MessageIntent, Communications durable schedule, or Audit durable schedule. The response must not reveal whether the address exists. |
| Account and Session | Successful registration creates an unverified Account and no Session. Protected access stays blocked. Proof consumption and credential login are later slices. |
| Pending experience | Show a localized verification-pending view with an explicit resend action. Do not offer email correction in this slice. |
| Resend | Resend is a separate Identity operation. Replaying the same resend ID returns its prior result. A later explicit click uses a new ID. An accepted resend supersedes the old active challenge and creates one new MessageIntent and its Communications durable schedule, whose only executor argument is `MessageIntent.id`. Ordinary accepted resends are not selected as central E2: they create no resend EvidenceObligation and no Audit durable schedule. Identity records the resend operation in its own audit trail; Communications owns the MessageIntent and delivery schedule. |
| Terms and Privacy | Before Account creation, the participant accepts the exact approved Terms and Privacy versions for the selected locale. Identity records those exact version references, accepted locale, and acceptance time on the Account. The same selected locale is stored as the Account's preferred language. Identity does not retain a complete registration-copy manifest. Purpose-specific consent remains separate. |
| Durable scheduling | Initial registration establishes owner-specific Communications and Audit durable execution through the approved Oban/`ash_oban` direction inside the same PostgreSQL acceptance transaction. Communications scheduling is reconstructable from `MessageIntent.id`. Audit E2 scheduling is reconstructable from `EvidenceObligation.id`. Neither worker executes inside the acceptance transaction or as part of the P8-05 acceptance proof. The exact AshOban function or API remains implementation JIT and must be verified against locked dependency versions before coding. |
| Audit | The selected initial Account-plus-PMR E2 requires both an EvidenceObligation and Audit materialisation scheduling inside the source acceptance boundary. An ordinary accepted resend is not selected as central E2 and creates no resend EvidenceObligation or Audit durable schedule; Identity records the resend operation in its own audit trail, and Communications owns its intent and delivery schedule. P8-05 may include only the minimum real Audit materialisation executor seam needed for the initial registration's committed Audit schedule to target a valid owner path, within the frozen EvidenceObligation and EvidenceRecord Resource set. P8-11 retains exhaustive E2 hardening and proof. |
| Abuse thresholds | OQ-035 remains unresolved and release-only. P8-05 selects no numeric rate, retry, or abuse threshold. |

## Accepted WELL-46 protected-delivery mechanism

Security/Architecture accepted this mechanism for P8-05. This section refines the protected-storage seam for this execution contract without changing Product, Architecture, Domain, or JIT-dossier ownership rules. It records the decision for canonical merge; it does not authorize implementation. Until this revision is merged to `main` and independently verified, WELL-46 remains `PASS PENDING CANONICAL RECORDING`. WELL-45 remains a separate open gate. WELL-47 is unchanged.

Use a private PostgreSQL authenticated-encryption envelope, bound one-to-one to a Communications `MessageIntent`. The envelope is sensitive delivery machinery. Private implementation-only PostgreSQL storage is permitted; the envelope is not a new Domain, Ash business Resource, Identity verification record, Communications delivery-attempt record, or second token/challenge store. Keep it in the same PostgreSQL Repo and transaction as the required acceptance consequences. Its only purpose is to preserve the bearer already issued for an already-authorized communication across process or node failure and durable retry. Row presence does not grant send authority.

Identity remains the sole authority for challenge purpose, validity, expiry, supersession, revocation, and consumption. Communications remains the sole authority for `MessageIntent`, `DeliveryAttempt`, delivery admission, provider-delivery lifecycle, and durable delivery scheduling. Communications owns the private, purpose-scoped capability writer and reader because the envelope exists only for delivery. The issuance/orchestration path invokes the Communications-owned capability writer through Communications' owner interface. Communications must use Identity's current non-secret eligibility result and cannot decide whether an Identity challenge remains valid. This mechanism creates no shared-write ownership.

At rest, store only the authenticated ciphertext containing the bearer, its unique `MessageIntent.id` association, the corresponding durable Identity source reference and purpose, a non-secret key version, and the nonce and authentication data required by the chosen AEAD representation. A copied source expiry may be stored only when it helps bound cleanup. Do not copy a token fingerprint, Identity validity or lifecycle state, destination, provider-attempt state, or delivery state. The implementation must enforce the one-to-one association. Associated data binds the immutable `MessageIntent.id`, Identity source reference, and purpose. It must not include duplicated mutable verification truth. If the implementation cannot reconstruct those values unambiguously at decryption, stop before coding and resolve the contract.

The accepted encryption direction is application-level AEAD using OTP `:crypto`, with AES-256-GCM as the current implementation candidate. Before coding, verify the exact API, key size, nonce generation and uniqueness requirements, authentication-tag handling, associated-data encoding, and error behavior against the supported Erlang/OTP version. AshCloak is not selected for this capability. Ash owner actions/interfaces, AshPostgres, and relevant Ash policies implement the existing business boundaries. AshOban/Oban may schedule and execute delivery only; they never store the bearer. Signals, Reactor, Temporal Resources, AshStateMachine, Archival, and PaperTrail are not part of protected-capability recovery.

Encryption keys are separate for each deployment environment. Keep them outside PostgreSQL, source control, committed configuration, and built release/container artifacts. Supply and validate them through the platform's runtime secret/configuration boundary. Store only the non-secret key version with each envelope. New envelopes use the active key. Earlier keys may remain decrypt-only during rotation and may be removed only after no live envelope or required retained recovery context depends on them. Rotation may re-encrypt live rows or let short-lived rows expire when safe. If a key is unavailable or compromised, fail closed. Do not fall back to plaintext, a default key, or a regenerated challenge. Identity owns any required challenge invalidation. Do not select a particular KMS or secret manager here.

For accepted initial registration, envelope creation commits in the same PostgreSQL acceptance transaction as the Account, PMR, credential and hash, Identity Token/challenge, accepted Terms and Privacy references, selected initial EvidenceObligation, MessageIntent, Communications schedule, and Audit schedule. A capability failure rolls back the accepted operation and leaves no recoverable orphan. For accepted resend, Identity's replacement/resend truth, the new MessageIntent, its envelope, and the Communications schedule commit or roll back together. The locked WELL-47 rule remains: resends create no central EvidenceObligation or Audit schedule. A committed transaction remains deliverable after process or node restart through the durable MessageIntent-ID-only schedule.

The durable job argument is only `MessageIntent.id`. The worker loads the MessageIntent through Communications, checks current Communications eligibility, resolves its Identity source reference and purpose server-side, obtains current non-secret Identity eligibility, admits the appropriate DeliveryAttempt, and only then retrieves the unique envelope by `MessageIntent.id` through the private Communications interface. The reader checks the source and purpose binding before decryption; the job never carries the source reference. No generic Ash read or ordinary application interface can return decrypted material. The worker then renders the participant-facing communication and submits it through the approved provider boundary. Missing, mismatched, expired, superseded, revoked, consumed, or cancelled authority fails closed. A worker never decrypts before current send authority and attempt admission are established.

Plaintext may exist only transiently in application memory in the narrow authorized delivery path needed to render and submit the verification message. It must not enter PostgreSQL plaintext, ordinary Identity or Communications fields, durable or general-purpose application coordination messages, durable jobs or their arguments or error payloads, unrelated process state, logs or Logger metadata, telemetry, traces/APM, crash reports, persisted exception details, Audit, Analytics, provider metadata, provider request logs, HTTP-client debug logs, LiveView/socket assigns, operator interfaces, committed test fixtures, or test failure output. Transient transport internal to the purpose-scoped provider-delivery stack may occur where required by the selected client, but it must remain bounded to that delivery operation and must not become durable or observable application state. The provider request body containing the participant-facing verification link/message is the intended external disclosure boundary. Do not promise BEAM memory zeroization.

A conclusively safe retry may reuse the same envelope only after current Communications and Identity authorization passes again. A retry never creates another challenge, MessageIntent, or envelope, and never revives superseded material. An unknown or ambiguous provider outcome is not a retryable failure until Communications reconciliation permits another submission. If Identity invalidation wins before DeliveryAttempt admission, deny the send. If admission wins first, that already-admitted provider operation may finish under the existing Communications contract. The owning database transitions decide admission and cleanup races; process-local locks do not establish correctness. A later accepted resend makes the prior envelope unavailable for any new send; cleanup may follow idempotently. Provider acceptance alone does not require immediate deletion when a legitimate retry or reconciliation still needs the envelope.

Delete the live envelope when no legitimate retry or reconciliation needs it, and no later than the Identity source becoming expired, superseded, revoked, consumed, or cancelled, subject only to an already-admitted provider operation finishing under the cutover rule. Cleanup is idempotent; cleanup failure does not restore send authority. Ordinary PostgreSQL backup retention and expiry are accepted. Do not promise immediate cryptographic erasure from retained backups. After restore, keep outbound delivery blocked until current Identity authority, Communications state, suppression/current-policy state, and required reconciliation have been re-established. Revisit this mechanism only if a future Security/Privacy requirement demands immediate irrecoverability from backups.

Missing capabilities or schedules, unknown key versions, authentication/decryption failures, mismatched bindings, and orphan envelopes fail closed. Reconcile or quarantine them through the governed recovery path; never regenerate bearer material or manufacture business truth. Central Audit receives no bearer, ciphertext, key, secret-bearing URL, or duplicate delivery ledger. Existing selected accountability evidence may include safe identifiers and result classifications only where already governed.

## WELL-45 content-governance framework

This section records the settled planning framework for WELL-45. It separates approval and binding rules from the actual participant-facing content versions. It contains no approved content strings or content-version IDs. The content versions remain subject to the approvals below.

| Decision | P8-05 rule |
|---|---|
| Approval routing | Ordinary editorial and platform copy uses the `Content Approver`; Afrikaans quality uses the `Afrikaans Language Reviewer`; English quality uses the `English Language Reviewer`; general health education and non-clinical launch wellness framing use the `Health Content Approver`; personalised or clinical guidance goes to Venessa or an authorised clinical approver; safety-critical content goes to Venessa plus any second approval required by the applicable protocol; legal and consent content goes to an authorised legal or privacy approver. Record each approval separately against the exact version. One person may hold multiple roles, with each approval still recorded separately. |
| Content ownership | Content & Media owns the immutable content and locale versions. Afrikaans and English are separately reviewed variants; do not use runtime translation, silent locale fallback, or an unpinned “latest” version. |
| Message binding | Each Communications MessageIntent binds to its exact approved message-content version and locale. MessageIntent records Communications intent; it does not prove provider delivery or Identity verification. |
| Registration acceptance | Identity records the exact accepted Terms and Privacy version references, accepted locale, and acceptance time. It does not bind a complete registration UI-copy manifest to the Account. |
| Expiry wording | Defer participant-facing verification-expiry wording unless an applicable authority requires it. |
| Verification-email scope | Add no extra safety or privacy copy to the verification email unless an applicable authority requires it. The message must use neutral wording that says a request was made to verify the address; it must not claim the recipient initiated the request. Exact Afrikaans and English strings require their scoped content and language approvals. |
| Urgent-support wording | Add no emergency or urgent-support wording to this path unless current authority defines an urgent-safety outcome for it. |
| Current gate | WELL-45 remains in Planning. Its content gate is `BLOCKED / NEEDS LEGAL/PRIVACY APPROVAL`: approved Afrikaans and English Terms and Privacy versions with immutable IDs and approval references have not been verified outside the repository. This status does not mark WELL-45 passed or authorize implementation. |
| Scope boundary | This framework does not resolve WELL-46 or change the locked WELL-47 decision. |

## Registration and retry contract

Before the registration form, the participant chooses Afrikaans or English and receives the approved launch and safety content for that locale. Do not infer locale through an unreviewed fallback. The registration path requires an affirmative 18+ confirmation and acceptance of the exact approved Terms and Privacy versions for the selected locale before Account creation. Identity validates these gates; browser state alone is not authority. A failed age gate, absent acceptance, or missing/unapproved Terms or Privacy version creates no Account or PMR. The selected locale becomes the Account's preferred language. On acceptance, the Account records the exact Terms and Privacy version references, accepted locale, and acceptance time.

The complete required form data is first name, surname, email, authentication credential (password), preferred language, 18+ confirmation, and Terms/Privacy acceptance. The chosen Afrikaans or English locale supplies the preferred-language value stored on the Account. Identity validates the password before accepting registration, marks the password credential active, and establishes its hash on the Account in the same accepted transition. Invalid credentials and missing required fields reject before Account creation and leave no Account or PMR. The credential is stored only in the approved Identity password representation, never as raw password data. Phone and city are optional in DEC-027 and are not required for this proof.

The browser allocates an opaque ID before the first registration request. The proposed format is a random 128-bit UUIDv4 generated by a cryptographically secure browser source. The browser retains it for retries of that logical request and discards it after a terminal response. A changed form submission gets a new ID. The ID is an idempotency key, not a credential or proof of identity.

Identity treats the operation ID and request as one immutable pair. An identical retry after a committed acceptance returns the same neutral result without creating another business consequence. A request that reuses the ID with changed input is rejected without mutation. A failure before commit leaves no accepted operation and may be retried with the same unchanged request. A corrected request uses a new ID.

Before code, the implementation plan must choose a safe durable request-binding representation. It must bind all registration inputs, including the credential, without persisting a raw password or creating a second Identity authority. The storage owner, secret/key dependency if any, versioning, retention, and behavior after a committed Account changes must be explicit. If no approved safe design fits, stop for Identity/Security review. The browser ID alone must never authorize a read or mutation.

Identity owns one email canonicalizer and a database uniqueness constraint. The concrete normalization proposal for independent review is:

1. Strip only leading and trailing ASCII space and tab characters.
2. Accept an ASCII dot-atom local part and ASCII DNS domain labels. Reject display-name syntax, quoted local parts, controls, embedded whitespace, and non-ASCII email input until SMTPUTF8/IDNA support has its own reviewed rule.
3. Preserve local-part bytes and case. Lowercase the domain. Preserve plus signs and dots; do not apply provider-specific alias rules.
4. Store and compare the resulting canonical value through Identity. The database uniqueness constraint is the final concurrent-registration guard.

The canonicalizer contract should include fixtures equivalent to these examples:

| Input | Result |
|---|---|
| ` Alice+campaign.Example@EXAMPLE.COM ` | `Alice+campaign.Example@example.com` |
| `alice+campaign.Example@example.com` | Remains distinct from the preceding local-part because local-part case is preserved. |
| `Alice.Example+tag@example.com` | Dots and plus tag remain unchanged. |
| `"Alice Example"@example.com` | Rejected because quoted local parts are outside the accepted subset. |
| `alice@example.com` with a non-ASCII local or domain character | Rejected until SMTPUTF8/IDNA support has a reviewed rule. |

This is a candidate Identity/Product policy, not a complete rule dictated by SMTP. RFC 5321 requires preserving local-part case and says exploiting that distinction is discouraged. A provider that treats local-part case as insensitive may route two case variants to one mailbox even though Identity treats them as distinct. Before code, Identity and Product owners must explicitly approve the full policy: whitespace handling, accepted syntax, non-ASCII handling, local-part comparison, domain normalization, and plus/dot treatment. They may return any part for revision. Code must not silently broaden the accepted syntax or case-fold the local part.

A distinct operation that loses the canonical-email uniqueness race returns the same public response as a newly accepted registration and creates no second Account, PMR, Token, EvidenceObligation, MessageIntent, Communications durable schedule, or Audit durable schedule. The new-account path and the duplicate path must have equal public response categories and wording in both locales. Timing and error mapping must not create an account-existence oracle.

## PMR allocation proposal

The Identity dossier leaves the exact PMR representation open under `ARQ-IAM-013`. The candidate for review is:

```text
PMR-<16 Base36 data characters><1 ISO/IEC 7064 MOD 37,2 check character>
```

- Data alphabet: `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`.
- Check alphabet: `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*`.
- Canonical form: uppercase. Compute the check character over `PMR` followed by the 16 data characters; exclude the presentation hyphen.
- Generate the 16 data characters from a cryptographically secure source with unbiased Base36 mapping. The checksum adds no entropy.
- Space size: `36^16 = 7,958,661,109,946,400,884,391,936`, or about 82.72 bits. The approximate raw birthday collision probability at 100 million allocations is `6.3e-10`, before database collision retry.
- Put a database uniqueness constraint over every allocated canonical PMR, including retired references. Retirement never permits reuse. Select the physical storage so that the anti-reuse rule survives the applicable Account closure/deletion contract. Do not add a PMR Resource unless current authority or the independent review finds that representation necessary.
- Identity retries only a PMR uniqueness collision, with a proposed limit of five generated candidates per allocation. Any other persistence failure aborts the acceptance transaction. Exhausting the bound aborts safely and returns a non-enumerating temporary failure. The implementation must verify a supported Ash/PostgreSQL retry mechanism rather than assume that a constraint error can be caught inside an aborted transaction.

Known check-character vector for the proposed mapping:

| Check input (hyphen excluded) | Displayed PMR | Expected check character |
|---|---|---|
| `PMR0123456789ABCDEF` | `PMR-0123456789ABCDEFA` | `A` |

ISO describes its check-character systems as detecting all single substitutions and all or nearly all local transpositions. This proposal is for transcription-error detection, not secrecy or authenticity. Before code, Identity must explicitly accept the prefix, alphabet, length, check mapping and known vector, transcription-error coverage, permanent non-reuse rule, and five-candidate retry bound. Independent review must verify the mapping and collision analysis. A different owner-approved choice requires revising this spec before implementation.

## Atomic acceptance and scheduling

A successful initial registration commits all PostgreSQL business consequences in one authoritative transaction or commits none. Credential validation, the required 18+ confirmation, and exact approved Terms and Privacy acceptances must pass before Account creation; invalid credentials, missing required fields, a failed age gate, absent acceptance, or an unapproved/missing locale or version reference leaves no Account or PMR. Account creation, activation of its password credential, and establishment of its password hash commit together in that same accepted Identity transition. No raw password is persisted. The private PostgreSQL protected-delivery envelope specified in the accepted WELL-46 decision must be durably established and bound to the Identity source and exact MessageIntent before the PostgreSQL transaction commits. If envelope establishment fails, no Account, PMR, Token, EvidenceObligation, MessageIntent, Communications durable schedule, Audit durable schedule, or delivery obligation may commit. The implementation must not establish the protected envelope outside the acceptance transaction as a fallback. Envelope-establishment failure rolls back the operation. If an orphan envelope is nevertheless discovered as an integrity fault, fail closed and reconcile or delete it. Orphan cleanup is recovery, not accepted transaction behaviour.

- one Identity Account with first name, surname, canonical email, and the selected locale stored as preferred language, plus successful 18+ confirmation;
- its Account-owned password credential marked active, with its hash established and committed in the same accepted transition as Account creation, through the approved Identity password representation and without creating a Session;
- accepted exact Terms/Privacy version references, locale, and acceptance time on the Account;
- one unique Account-owned canonical active PMR;
- one Identity verification Token, with no parallel SecurityChallenge store;
- the selected Account-plus-PMR E2 EvidenceObligation;
- one Communications MessageIntent bound to the exact approved content version, locale, destination provenance, and source operation;
- one Communications durable scheduling record inserted through the approved Oban/`ash_oban` boundary, whose only executor argument is `MessageIntent.id`;
- one Audit E2 durable scheduling record inserted through the approved Oban/`ash_oban` boundary, whose executor payload contains only the EvidenceObligation identifier or equivalent minimum owner-specific reference;
- the short-lived protected delivery envelope selected under WELL-46, bound to the source purpose and exact MessageIntent and recoverable only by the purpose-scoped delivery executor.

The Audit executor must not receive source payload, Account copy, PMR copy, bearer material, credentials, password/hash, rendered content, MessageIntent payload, or a prebuilt evidence envelope in its schedule arguments. It must reconstruct authoritative Audit state through Audit-owned interfaces. The Communications executor must reconstruct authoritative Communications state through Communications-owned interfaces.

Identity, Communications, and Audit mutations must go through their owning Ash interfaces. The orchestration must use the supported transaction mechanism verified against the actual locked dependency versions. No direct `Repo`, raw SQL, or parallel `Ecto.Multi` business-write path is allowed. Both required owner-specific durable schedules must be established inside the same authoritative PostgreSQL acceptance boundary where TB-001 requires them. Failure to establish either required schedule must prevent the authoritative acceptance result from committing. The provider and durable workers run only after commit, outside the acceptance transaction. Oban state and provider results never establish Account, PMR, verification, or Audit truth.

P8-05 must plan executable proof that:

1. a successful registration leaves both required durable schedules committed;
2. a failed acceptance leaves neither required durable schedule committed;
3. a deterministic failure between the two schedule insertions, regardless of which one implementation eventually inserts first, rolls back the full acceptance result;
4. a deterministic failure after both required schedules are established but before transaction commit rolls back the full acceptance result;
5. Communications executor arguments contain only `MessageIntent.id`;
6. Audit executor arguments contain only the approved EvidenceObligation identifier or equivalent minimum owner-specific reference;
7. no bearer, credential, source, or evidence payload leaks into either schedule's executor arguments;
8. neither Communications nor Audit durable workers execute as part of P8-05's acceptance proof.

The proof must also show successful protected-capability establishment for the accepted verification message and a fail-closed cut where capability establishment fails. In the failed case, no Account, PMR, password, Token, EvidenceObligation, MessageIntent, Communications durable schedule, Audit durable schedule, or delivery obligation is committed, and no orphaned capability remains recoverable. The success case must prove the capability is bound to exactly one source purpose and its MessageIntent without exposing the bearer through ordinary fields, schedule arguments, logs, telemetry, Audit, Analytics, or operator reads.

## Resend contract

The pending page exposes resend as a separate explicit action. The browser creates a resend operation ID for each click and reuses that ID only when retrying the same click.

For a valid new resend operation, Identity atomically supersedes the one active verification challenge and issues one replacement challenge. The same acceptance boundary creates exactly one MessageIntent and one Communications durable schedule whose only executor argument is `MessageIntent.id`. A retry with the same resend ID returns the prior result and creates no second challenge, intent, Communications schedule, EvidenceObligation, or Audit schedule. A later explicit click uses a new ID and may create one new replacement challenge, intent, and Communications schedule.

The accepted `WELL-47` decision is that an ordinary accepted resend is not selected as central E2. It creates no resend EvidenceObligation and no Audit durable schedule. The accepted resend boundary contains Identity's challenge replacement and resend audit, the new Communications MessageIntent and its durable schedule, and the protected delivery envelope specified above. Oban arguments remain MessageIntent-ID-only.

The response remains neutral for unknown, verified, expired, or otherwise ineligible accounts. Resend never creates a second Account or PMR. Identity owns the resend operation and its audit record; Communications owns the new MessageIntent and delivery schedule. This spec records the accepted `WELL-47` outcome but does not authorize implementation.

This slice does not consume the challenge, log in the participant, change the Account email, run delivery, or select rate limits. P8-07 owns scanner-safe consumption proof. OQ-035 continues to own abuse thresholds.

## Pre-implementation gates

The following Plane gates still govern implementation. They do not change WELL-6 from Planning.

| Gate | Plane item | Required outcome |
|---|---|---|
| Approved bilingual content | `WELL-45` | Approved, immutable Afrikaans and English locale-selection, launch, safety, registration, verification, pending/resend, Terms, and Privacy versions exist with owner, approval state, and exact locale/version references. No fallback or invented copy. |
| Protected delivery capability | `WELL-46` | Security/Architecture accepted the private PostgreSQL authenticated-encryption envelope recorded above. Before this revision merges and is independently verified, the gate remains `PASS PENDING CANONICAL RECORDING`. After merge and independent verification, reconcile WELL-46 in Plane. This decision does not authorize implementation. |

The accepted `WELL-47` decision recorded in this spec is that ordinary accepted resend is not selected as central E2 and creates no resend EvidenceObligation or Audit durable schedule. This decision is canonically settled only after this spec revision is merged to `main`; it does not authorize implementation. The content gate also covers exact approved Terms and Privacy version references. The current repository contains a Content & Media governance pack, but no dedicated approved registration-content pack was found. WELL-45 remains blocked on approved content and Legal/Privacy approval. WELL-46 no longer has an open mechanism-selection question, but implementation remains unauthorized until canonical recording and independent verification, plus all other required gates and authorization.

## Proposed implementation ticket decomposition

These are proposed coding tickets for review, not created Plane work items. Every ticket depends on independent planning review and resolution of `WELL-45` and `WELL-46`, because P8-05 includes the browser journey and protected delivery. The accepted `WELL-47` no-central-E2 resend outcome is a fixed scope constraint once this revision is merged to `main`; it is not an additional Audit implementation path. None may enter the execution frontier before the applicable conditions pass. After review, create them in Plane with explicit dependencies and keep them out of Ready until all applicable gates are resolved and implementation is authorized.

| Order | Proposed ticket | Depends on | Independent acceptance boundary |
|---|---|---|---|
| 1 | Identity registration, canonicalization, PMR, Token, and operation-idempotency primitives | Independent planning review; `WELL-45`; `WELL-46`; Identity/Product approval of canonicalizer; Identity approval of PMR and safe request-binding proposals | Identity-owned actions and focused tests require the complete DEC-027 field set: first name, surname, canonical email, password credential, preferred language, 18+ confirmation, and exact approved Terms/Privacy acceptance. The selected locale is stored as the Account's preferred language. Successful registration marks the Account-owned password credential active and establishes its hash in the same transition that creates the Account. Invalid credentials, any missing required field, a failed age gate, or missing/unapproved Terms/Privacy acceptance leaves no Account or PMR. Tests also enforce one Account-owned PMR, bounded collision retry, immutable operation binding, unverified state, and no Session. No raw password is persisted. Contracts expose what Tickets 2 and 3 require for atomic integration. No public path may commit a partial registration before integration. |
| 2 | Communications MessageIntent and Communications durable scheduling | Independent planning review; Ticket 1 contracts; `WELL-45`; `WELL-46` | Communications-only acceptance boundary: creates one version-bound MessageIntent; establishes its Communications durable schedule inside the source PostgreSQL acceptance transaction with `MessageIntent.id` as its only executor argument; establishes the protected-delivery envelope specified above; does not own Audit scheduling. Tests prove envelope failure leaves no MessageIntent, no Communications durable schedule, no recoverable orphan envelope, and invokes no Communications worker or provider. |
| 3 | Audit E2 obligation, minimum real materialisation seam, and Audit durable scheduling | Independent planning review; Ticket 1 Account/PMR transition contract (not Ticket 1 implementation completion); `WELL-45`; `WELL-46` | Establishes the selected initial Account-plus-PMR EvidenceObligation; implements the already-authorised EvidenceRecord representation/action boundary needed by the minimum real materialisation path; implements a real Audit executor entry point capable of reconstructing work from EvidenceObligation.id; establishes Audit durable scheduling for initial registration inside the source acceptance transaction; Audit schedule arguments contain only the minimum obligation identifier/reference. Ordinary accepted resends create no central EvidenceObligation and no Audit schedule. Does not claim P8-11 hardening completion. Does not add generic event bus, generic outbox Resource, AuditEvent, EvidenceAttempt, MaterialisationJob, generic dispatcher, or cross-Domain consequence worker. |
| 4 | Registration and resend acceptance orchestration | Independent planning review; Tickets 1–3; `WELL-45`; `WELL-46` | Initial registration composes Identity mutation, Communications mutation plus Communications schedule, the initial Account-plus-PMR Audit obligation plus Audit schedule, and the protected delivery envelope within the verified PostgreSQL acceptance boundary. An accepted resend composes Identity challenge replacement and resend audit with its Communications MessageIntent, durable schedule, and protected delivery envelope; it creates no central Audit obligation or Audit schedule. All consequences required for the respective operation commit or roll back together. An envelope failure during initial registration leaves no Account, PMR, password credential/hash, Token, EvidenceObligation, MessageIntent, Communications durable schedule, Audit durable schedule, or delivery obligation, and no recoverable orphan envelope. An envelope failure during resend rolls back challenge supersession/replacement, resend audit, the new MessageIntent and Communications schedule, and the delivery obligation; it preserves the previously committed Account, PMR, credential, Token, and active challenge, and leaves no recoverable orphan envelope. Retries and duplicate email preserve the selected public result and one-set cardinality. |
| 5 | Bilingual registration and verification-pending browser path | Independent planning review; Ticket 4; `WELL-45`; `WELL-46` | Exercise the complete browser journey separately in Afrikaans and English: locale selection, exact approved launch and safety content, required registration fields and gates, accepted registration, and the localized pending view with its explicit resend action. Use exact approved locale versions with no fallback. Resend is a separate explicit operation. No email correction, Session, login, proof consumption, silent fallback, or protected access. |
| 6 | P8-05 production-path proof and evidence artifact | Independent planning review; Tickets 1–5; `WELL-45`; `WELL-46`; P8-04 harness | Capture browser-level evidence of the complete registration journey in both Afrikaans and English, including locale-specific approved content, accepted registration, and the localized pending/resend view. Alongside that evidence, the real PostgreSQL/Ash path proves success with the complete DEC-027 field set, the selected locale stored as Account preferred language, and the Account-owned password credential active with its hash established in the same accepted transition; proves invalid credentials, any missing required field, failed age confirmation, or absent/unapproved Terms/Privacy acceptance leave no Account or PMR; proves no raw password is persisted; proves exact Terms/Privacy references, accepted locale, and acceptance time; proves successful protected-capability establishment; proves an initial-registration capability failure leaves no Account, PMR, password credential/hash, Token, EvidenceObligation, MessageIntent, Communications durable schedule, Audit durable schedule, delivery obligation, or recoverable orphan capability; proves a resend capability failure rolls back challenge supersession/replacement, resend audit, the new MessageIntent and Communications schedule, and delivery obligation while preserving the previously committed Account, PMR, credential, Token, and active challenge with no recoverable orphan capability; and proves duplicate email, same-ID replay, changed-input rejection, PMR collision bound, resend replay/supersession, initial Account-plus-PMR E2 selection and both initial owner-specific schedules, no resend EvidenceObligation or Audit schedule, the Communications-only resend schedule, rollback between initial registration schedule insertions, rollback after both initial schedules before commit, MessageIntent-ID-only Communications schedule arguments, EvidenceObligation-ID-only Audit schedule arguments, no duplicate schedules on replay/duplicate email, and no Communications/Audit worker or provider execution. Run targeted tests and applicable NewYou verification gates, including `mix check` and `mix check.deep` where required by the current verification contract. Run the P8-04 deterministic harness through its approved entrypoint. |

Tickets 1–3 may be developed in parallel after independent planning review, all pre-implementation gates, and their shared contracts are approved, where lawful. Ticket 3 depends on Ticket 1’s agreed Account/PMR transition contract, not its implementation completion; the Audit work can be built against that contract before integration. Ticket 4 cannot integrate until the minimum real Audit executor and scheduling seam from Ticket 3 exists. Ticket 4 is the first complete registration acceptance path. Ticket 5 follows that boundary. Ticket 6 closes the P8-05 proof outcome. P8-05’s Audit executor is the minimum valid production seam needed to make the E2 source schedule real, not a substitute for P8-11. P8-06 retains exhaustive rollback/replay/PMR concurrency proof; P8-07 retains scanner-safe proof-consumption proof; P8-10 retains provider ambiguity; P8-11 retains duplicate execution, crash/retry, restart/backlog, append-only/tamper resistance, and comprehensive E2 materialisation hardening and proof.

## Candidate code map

The current repository is a Phoenix/Ash starter. It has no application Identity, Communications, or Audit resources, no registration route or pending view, no Oban dependency/supervisor, and no business tables. The following paths are candidates for later implementation and must be verified against repository conventions and locked APIs before use:

- `lib/new_you/identity.ex` and `lib/new_you/identity/*` for Identity-owned Ash resources and interface;
- `lib/new_you/communications.ex` and `lib/new_you/communications/*` for MessageIntent and its owner interface;
- `lib/new_you/audit.ex` and `lib/new_you/audit/*` for EvidenceObligation, EvidenceRecord, owning actions/interfaces, and the minimum real E2 materialisation executor seam (candidate/JIT module names remain subject to repository conventions);
- `lib/new_you/application.ex` and `config/config.exs` for approved durable executor supervision/configuration;
- `lib/new_you_web/router.ex` and a new registration LiveView/component for the browser path;
- generated migrations under `priv/repo/migrations/`;
- focused Identity, acceptance-boundary, Communications/Audit, and browser tests under `test/`.

This is a file map, not a selection of final modules, APIs, migrations, or dependencies. Before implementation, follow `.agents/skills/project-implementation/SKILL.md`, load relevant Ash/Phoenix/Elixir skills, inspect exact dependency versions, verify package APIs against primary sources, and use Igniter first for supported structural changes. The transaction-aware Oban/Ash integration and collision retry semantics are stop-and-verify points. No tests or application changes are part of this planning task.

## Review checklist and implementation stop conditions

Independent planning review must assess the exact spec and decomposition against live authority and the WELL-6 Outcome Contract. It should return any contradiction or unsafe design before coding begins, with attention to:

- the PMR alphabet, format, checksum, collision analysis, and permanent non-reuse;
- email canonicalization and its local-part case tradeoff;
- safe immutable request binding, including credential comparison and key/retention behavior;
- transaction-aware Oban/`ash_oban` insertion of both owner-specific durable schedules through owning Ash interfaces;
- the capability needed to deliver protected verification material;
- the accepted resend classification: ordinary accepted resends create no central EvidenceObligation or Audit durable schedule;
- content-version gates and the sessionless, unverified browser boundary;
- whether the six proposed tickets are independently reviewable and correctly ordered;
- whether initial registration establishes both owner-specific schedules inside the required PostgreSQL acceptance boundary;
- whether Audit execution can be reconstructed solely from its minimum EvidenceObligation reference;
- whether the Audit schedule targets a real executable owner path rather than a placeholder;
- whether Communications and Audit durable execution remain independent owner boundaries;
- whether any generic dispatcher, event bus, or shared worker is introduced merely to avoid two schedules;
- whether P8-11 still owns duplicate/crash/restart/tamper hardening;
- whether the supported Ash/AshPostgres/AshOban mechanism can actually insert both required schedules transactionally.

Stop for an authority or owner decision if the approved content is missing, the implementation cannot satisfy the accepted WELL-46 envelope contract, the immutable operation binding needs an unapproved secret mechanism, or the PostgreSQL/Ash boundary cannot include all selected consequences for their respective operations without a parallel write path.

Stop if no supported mechanism can establish both required owner-specific durable schedules for initial registration in the source acceptance transaction while preserving owning Ash mutation boundaries.

Stop if the only proposed fix requires changing TB-001, changing Domain ownership, a third Audit Resource, generic event infrastructure, placeholder or dead executor jobs, or absorbing P8-11 wholesale into P8-05.

A passing planning review alone does not close any gate, certify TB-001 or Phase 8, authorize Phase 9, or authorize implementation. WELL-6 remains in Planning until the planning package passes review and the gates and execution authorization are handled under Plane and current authority.

## Source references

- `docs/00_platform/README.md` and `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` for current authority routing; `docs/00_platform/00_PLATFORM_v1.8.0.md` §21E.4 for the scoped approval matrix.
- `docs/00_platform/02_OPEN_WORK_v1.2.80.md` §12.36 for P8-04 completion and P8-05 planning route.
- `docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md` §§3–9 for the PostgreSQL acceptance boundary, `ash_oban`, E2, job-argument, and proof constraints.
- `docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md` §§D.1, F.2, J.1, J.1a, O, R, T, and V for Account/PMR/Token ownership, delivery, resend, idempotency, security, frontend response, and tests.
- `docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` §§4–8 for MessageIntent authority, exact content/locale binding, resend, durable execution, and protected delivery.
- `docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` §§5–6 for selected audit evidence and E2 boundaries.
- `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` §§5.2 and 7.2 for pending experience and approved bilingual content.
- `docs/00_platform/01_DECISIONS_v1.8.0.md` OQ-035 for unresolved abuse thresholds.
- [ISO/IEC 7064:2003, Check character systems](https://www.iso.org/standard/31531.html) for check-character error-detection properties.
- [RFC 5321 §2.4](https://www.rfc-editor.org/rfc/rfc5321.html) for mailbox local-part and domain comparison rules.
