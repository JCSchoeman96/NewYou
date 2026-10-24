# P8-05 registration JIT specification

**Status:** Candidate for independent planning review
**Plane:** WELL-6, currently in Planning
**Planning baseline:** `main@1ebfee0581815ea7ff21af6ad0733709fadd0696`
**Scope:** Specification and proposed ticket decomposition only. This file does not change governed authority or authorize implementation.

## Purpose and current boundary

P8-05 is the first production-path Phase 8 proof slice. Its bilingual browser path presents approved launch and safety content before registration and enforces the required 18+ and exact Terms/Privacy acceptance gates before Account creation. The TB-001 PostgreSQL acceptance transaction commits one Identity-owned Account with an active password credential and its hash, its canonical active PMR, a verification Token, the selected Audit EvidenceObligation, a Communications MessageIntent, and initial durable scheduling. Password validation, Account creation, credential activation, and password-hash establishment are one accepted Identity transition. Raw passwords are never persisted.

The Account remains unverified and has no Session. The participant sees a localized verification-pending page. P8-05 does not consume verification proof, log the participant in, invoke the worker, contact a provider, or certify the full TB-001 proof.

The current authority is Open Work v1.2.80, especially §12.36. WELL-5 / P8-04 is complete, and the harness is available to later authorized Phase 8 slices. The current TB-001 proof remains `INCOMPLETE / COVERAGE-INCOMPLETE`, ten required business/browser manifests remain unavailable, and Phase 8 is not certified. Phase 9 remains `NOT STARTED / NOT AUTHORISED`.

This spec follows the outcome contract in Plane WELL-6. Live GitHub authority controls if a Plane description or this planning artifact becomes stale. It does not change Product, Architecture, Domain, Roadmap, TB-001, or the JIT dossiers.

## Fixed design decisions

| Area | P8-05 boundary |
|---|---|
| Identity ownership | Identity owns Account, canonical email, PMR, verification Token, and registration/resend operation truth. PMR remains Account-owned truth, not a separate Resource, login name, secret, or authorization mechanism. |
| Required registration data | Collect the complete DEC-027 minimum set: first name, surname, email, authentication credential (password), preferred language, 18+ confirmation, and Terms/Privacy acceptance. The selected Afrikaans or English locale becomes the Account's preferred language. Phone and city remain optional under DEC-027 and are outside this proof path. Identity validates the credential, marks it active, and establishes its password hash in the same transition as Account creation; this does not create a Session or log the participant in. Raw passwords are never persisted. |
| Entry and account gates | The participant selects Afrikaans or English and sees the exact approved launch and safety content before registration. Identity enforces 18+ confirmation and acceptance of the exact approved Terms and Privacy versions before creating an Account. A failed or missing gate creates no Account or PMR. |
| Registration operation | The browser creates one opaque operation ID for each logical registration and reuses it across retries. Identity binds the ID to one immutable request. Reuse with changed input safely rejects; a corrected request uses a new ID. |
| Duplicate email | A distinct operation for an existing canonical email returns the same neutral public response as a newly accepted registration. It creates no second Account, PMR, Token, MessageIntent, or job. The response must not reveal whether the address exists. |
| Account and Session | Successful registration creates an unverified Account and no Session. Protected access stays blocked. Proof consumption and credential login are later slices. |
| Pending experience | Show a localized verification-pending view with an explicit resend action. Do not offer email correction in this slice. |
| Resend | Resend is a separate Identity operation. Replaying the same resend ID returns its prior result. A later explicit click uses a new ID. An accepted resend supersedes the old active challenge and creates one new MessageIntent and one Oban job whose arguments contain only that MessageIntent ID. |
| Terms and Privacy | Before Account creation, the participant accepts the exact approved Terms and Privacy versions for the selected locale. Identity records those exact version references, accepted locale, and acceptance time on the Account. The same selected locale is stored as the Account's preferred language. Purpose-specific consent remains separate. |
| Durable scheduling | Oban scheduling uses the `ash_oban` direction already fixed by TB-001. Insert the job in the same PostgreSQL acceptance transaction. Do not run the worker or provider in this proof. |
| Audit | Keep the selected E2 obligation for initial Account creation plus PMR assignment. Record resend through Identity audit and its Communications intent. The Audit owner must decide whether resend also needs a central EvidenceObligation before implementation. |
| Abuse thresholds | OQ-035 remains unresolved and release-only. P8-05 selects no numeric rate, retry, or abuse threshold. |

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

A distinct operation that loses the canonical-email uniqueness race returns the same public response as a newly accepted registration and creates no second Account, PMR, Token, MessageIntent, or job. The new-account path and the duplicate path must have equal public response categories and wording in both locales. Timing and error mapping must not create an account-existence oracle.

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

A successful initial registration commits all PostgreSQL business consequences in one authoritative transaction or commits none. Credential validation, the required 18+ confirmation, and exact approved Terms and Privacy acceptances must pass before Account creation; invalid credentials, missing required fields, a failed age gate, absent acceptance, or an unapproved/missing locale or version reference leaves no Account or PMR. Account creation, activation of its password credential, and establishment of its password hash commit together in that same accepted Identity transition. No raw password is persisted. The approved protected delivery capability must be durably established through its approved mechanism and bound to the Identity source and exact MessageIntent before the PostgreSQL transaction commits. If capability establishment fails, no Account, PMR, Token, EvidenceObligation, MessageIntent, job, or delivery obligation may commit. If a failed handoff leaves a capability outside the transaction, it must be cleared or rendered irrecoverable before the operation is treated as failed.

- one Identity Account with first name, surname, canonical email, and the selected locale stored as preferred language, plus successful 18+ confirmation;
- its Account-owned password credential marked active, with its hash established and committed in the same accepted transition as Account creation, through the approved Identity password representation and without creating a Session;
- accepted exact Terms/Privacy version references, locale, and acceptance time on the Account;
- one unique Account-owned canonical active PMR;
- one Identity verification Token, with no parallel SecurityChallenge store;
- the selected Account-plus-PMR E2 EvidenceObligation;
- one Communications MessageIntent bound to the exact approved content version, locale, destination provenance, and source operation;
- one initial Oban scheduling row inserted through the approved `ash_oban` boundary, with only the MessageIntent ID in job arguments;
- the already approved short-lived protected delivery capability for the verification bearer, bound to the source purpose and exact MessageIntent and recoverable only by the purpose-scoped delivery executor.

Identity, Communications, and Audit mutations must go through their owning Ash interfaces. The orchestration must use the supported transaction mechanism verified against the actual locked dependency versions. No direct `Repo`, raw SQL, or parallel `Ecto.Multi` business-write path is allowed. The provider and worker run only after commit, outside the acceptance transaction. Oban state and provider results never establish Account, PMR, verification, or Audit truth.

The proof must show that the job exists after successful acceptance and is absent after failed acceptance, including a deterministic failure after job insertion but before commit. It must inspect the persisted job arguments and show that they contain only the MessageIntent ID. It must not execute the worker or call a provider.

The proof must also show successful protected-capability establishment for the accepted verification message and a fail-closed cut where capability establishment fails. In the failed case, no Account, PMR, password, Token, EvidenceObligation, MessageIntent, Oban job, or delivery obligation is committed, and no orphaned capability remains recoverable. The success case must prove the capability is bound to exactly one source purpose and its MessageIntent without exposing the bearer through ordinary fields, job arguments, logs, telemetry, Audit, Analytics, or operator reads.

## Resend contract

The pending page exposes resend as a separate explicit action. The browser creates a resend operation ID for each click and reuses that ID only when retrying the same click.

For a valid new resend operation, Identity atomically supersedes the one active verification challenge and issues one replacement challenge. The same acceptance boundary creates exactly one MessageIntent and one Oban job containing only that intent ID. A retry with the same resend ID returns the prior result and creates no second challenge, intent, or job. A later explicit click uses a new ID and may create one new replacement challenge, intent, and job.

The response remains neutral for unknown, verified, expired, or otherwise ineligible accounts. Resend never creates a second Account or PMR. Identity records the resend operation in its own audit trail. Communications owns the new MessageIntent. No central resend EvidenceObligation is added unless the Audit owner selects it through gate `WELL-47`; that decision must be reflected in the atomic boundary before implementation.

This slice does not consume the challenge, log in the participant, change the Account email, run delivery, or select rate limits. P8-07 owns scanner-safe consumption proof. OQ-035 continues to own abuse thresholds.

## Pre-implementation gates

The following Plane items block implementation. They do not change WELL-6 from Planning.

| Gate | Plane item | Required outcome |
|---|---|---|
| Approved bilingual content | `WELL-45` | Approved, immutable Afrikaans and English locale-selection, launch, safety, registration, verification, pending/resend, Terms, and Privacy versions exist with owner, approval state, and exact locale/version references. No fallback or invented copy. |
| Protected delivery capability | `WELL-46` | Security/Architecture confirms that an existing approved mechanism can safely retain and retrieve the verification bearer for durable delivery, or separately approves a mechanism and its boundary. TOTP approval for AshCloak does not imply delivery approval. |
| Resend E2 classification | `WELL-47` | Audit owner decides whether resend challenge issuance requires a central EvidenceObligation in addition to Identity audit and Communications intent. If yes, record its evidence class, minimum payload, causal identity, and required atomic boundary. |

The content gate also covers exact approved Terms and Privacy version references. The current repository contains a Content & Media governance pack, but no dedicated approved registration-content pack was found. The protected-secret search found no approval extending AshCloak to bearer delivery. These are open blockers, not permission to choose replacement content or storage.

## Proposed implementation ticket decomposition

These are proposed coding tickets for review, not created Plane work items. Every ticket depends on independent planning review and resolution of `WELL-45`, `WELL-46`, and `WELL-47`, because P8-05 includes the browser journey, protected delivery, and resend. None may enter the execution frontier before those conditions pass. After review, create them in Plane with explicit dependencies and keep them out of Ready until all applicable gates are resolved and implementation is authorized.

| Order | Proposed ticket | Depends on | Independent acceptance boundary |
|---|---|---|---|
| 1 | Identity registration, canonicalization, PMR, Token, and operation-idempotency primitives | Independent planning review; `WELL-45`; `WELL-46`; `WELL-47`; Identity/Product approval of canonicalizer; Identity approval of PMR and safe request-binding proposals | Identity-owned actions and focused tests require the complete DEC-027 field set: first name, surname, canonical email, password credential, preferred language, 18+ confirmation, and exact approved Terms/Privacy acceptance. The selected locale is stored as the Account's preferred language. Successful registration marks the Account-owned password credential active and establishes its hash in the same transition that creates the Account. Invalid credentials, any missing required field, a failed age gate, or missing/unapproved Terms/Privacy acceptance leaves no Account or PMR. Tests also enforce one Account-owned PMR, bounded collision retry, immutable operation binding, unverified state, and no Session. No raw password is persisted. No public path may commit a partial registration before integration. |
| 2 | Communications MessageIntent and transactional Oban scheduling | Independent planning review; Ticket 1 contracts; `WELL-45`; `WELL-46`; `WELL-47` | Owner interface creates one version-bound MessageIntent and inserts the Oban job in the same PostgreSQL transaction with only its ID. It establishes the approved crash-safe protected delivery capability bound to the source and intent before that transaction commits. Tests prove capability failure leaves no Account, PMR, Token, EvidenceObligation, MessageIntent, job, or delivery obligation, leaves no recoverable orphan capability, and invokes no worker/provider. |
| 3 | Audit registration E2 and resend audit boundary | Independent planning review; Ticket 1 Account/PMR transition contract (not Ticket 1 implementation completion); `WELL-45`; `WELL-46`; `WELL-47` | Initial Account-plus-PMR E2 is present in the transaction. Resend records Identity audit and follows the Audit owner’s explicit central-evidence decision. |
| 4 | Registration and resend acceptance orchestration | Independent planning review; Tickets 1–3; `WELL-45`; `WELL-46`; `WELL-47` | One public application operation composes owner interfaces within the verified PostgreSQL acceptance boundary, including successful protected-capability establishment. Successful acceptance commits every required consequence; injected failure leaves none. Retries and duplicate email preserve the selected public result and one-set cardinality. |
| 5 | Bilingual registration and verification-pending browser path | Independent planning review; Ticket 4; `WELL-45`; `WELL-46`; `WELL-47` | Exercise the complete browser journey separately in Afrikaans and English: locale selection, exact approved launch and safety content, required registration fields and gates, accepted registration, and the localized pending view with its explicit resend action. Use exact approved locale versions with no fallback. Resend is a separate explicit operation. No email correction, Session, login, proof consumption, silent fallback, or protected access. |
| 6 | P8-05 production-path proof and evidence artifact | Independent planning review; Tickets 1–5; `WELL-45`; `WELL-46`; `WELL-47`; P8-04 harness | Capture browser-level evidence of the complete registration journey in both Afrikaans and English, including locale-specific approved content, accepted registration, and the localized pending/resend view. Alongside that evidence, the real PostgreSQL/Ash path proves success with the complete DEC-027 field set, the selected locale stored as Account preferred language, and the Account-owned password credential active with its hash established in the same accepted transition; proves invalid credentials, any missing required field, failed age confirmation, or absent/unapproved Terms/Privacy acceptance leave no Account or PMR; proves no raw password is persisted; proves exact Terms/Privacy references, accepted locale, and acceptance time; proves protected-capability establishment and a failure cut that leaves no Account, PMR, password credential/hash, Token, EvidenceObligation, MessageIntent, job, delivery obligation, or recoverable orphan capability; and proves duplicate email, same-ID replay, changed-input rejection, PMR collision bound, resend replay/supersession, E2 selection, atomic job presence/absence, ID-only job args, and no worker/provider execution. Run the P8-04 deterministic harness through its approved entrypoint. |

Tickets 1–3 may be developed in parallel after independent planning review, all pre-implementation gates, and their shared contracts are approved. Ticket 3 depends on Ticket 1’s agreed Account/PMR transition contract, not its implementation completion; the Audit work can be built against that contract and integrated after Tickets 1–3 are complete. Ticket 4 is the first complete registration acceptance path. Ticket 5 follows that boundary. Ticket 6 closes the P8-05 proof outcome. P8-06 retains exhaustive rollback/replay/PMR concurrency proof; P8-07 retains scanner-safe proof-consumption proof; P8-10 retains provider ambiguity; P8-11 retains E2 materialization/restart recovery.

## Candidate code map

The current repository is a Phoenix/Ash starter. It has no application Identity, Communications, or Audit resources, no registration route or pending view, no Oban dependency/supervisor, and no business tables. The following paths are candidates for later implementation and must be verified against repository conventions and locked APIs before use:

- `lib/new_you/identity.ex` and `lib/new_you/identity/*` for Identity-owned Ash resources and interface;
- `lib/new_you/communications.ex` and `lib/new_you/communications/*` for MessageIntent and its owner interface;
- `lib/new_you/audit.ex` and `lib/new_you/audit/*` for EvidenceObligation and its owner interface;
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
- transaction-aware `ash_oban` insertion through owning Ash interfaces;
- the capability needed to deliver protected verification material;
- the Audit owner’s resend E2 decision;
- content-version gates and the sessionless, unverified browser boundary;
- whether the six proposed tickets are independently reviewable and correctly ordered.

Stop for an authority or owner decision if the approved content is missing, no approved protected delivery mechanism fits, Audit has not decided resend evidence, the immutable operation binding needs an unapproved secret mechanism, or the PostgreSQL/Ash boundary cannot include all selected consequences without a parallel write path.

A passing planning review alone does not close any gate, certify TB-001 or Phase 8, authorize Phase 9, or authorize implementation. WELL-6 remains in Planning until the planning package passes review and the gates and execution authorization are handled under Plane and current authority.

## Source references

- `docs/00_platform/README.md` and `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` for current authority routing.
- `docs/00_platform/02_OPEN_WORK_v1.2.80.md` §12.36 for P8-04 completion and P8-05 planning route.
- `docs/00_platform/working/FP-001_TRACER_BULLET_CONTRACT_WORKING_v0.1.2.md` §§3–9 for the PostgreSQL acceptance boundary, `ash_oban`, E2, job-argument, and proof constraints.
- `docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md` §§D.1, F.2, J.1, J.1a, O, R, T, and V for Account/PMR/Token ownership, delivery, resend, idempotency, security, frontend response, and tests.
- `docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` §§4–8 for MessageIntent authority, exact content/locale binding, resend, durable execution, and protected delivery.
- `docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` §§5–6 for selected audit evidence and E2 boundaries.
- `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` §§5.2 and 7.2 for pending experience and approved bilingual content.
- `docs/00_platform/01_DECISIONS_v1.8.0.md` OQ-035 for unresolved abuse thresholds.
- [ISO/IEC 7064:2003, Check character systems](https://www.iso.org/standard/31531.html) for check-character error-detection properties.
- [RFC 5321 §2.4](https://www.rfc-editor.org/rfc/rfc5321.html) for mailbox local-part and domain comparison rules.
