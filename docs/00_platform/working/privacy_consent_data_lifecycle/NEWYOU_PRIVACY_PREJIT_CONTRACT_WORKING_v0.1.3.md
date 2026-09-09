# Privacy / Consent / Participant Data Rights Pre-JIT Contract — Working v0.1.3

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT CONTRACT
- **v0.1.3 hygiene patch:** Standardises exact governed identifiers and terminology: all abbreviated OQ references are fully namespaced, the governed contract term is `Phase 7C Final Feature Pack Contract`, and the prior security/anti-abuse ownership clarification is preserved. No accepted doctrine, upstream-delta classification or authority status is changed.
- **Purpose:** Small implementation-facing planning contract for future Privacy & Consent JIT work.
- **Detailed provenance:** `PRIVACY_CONSENT_PREJIT_DISCOVERY_WORKING_v0.12.1.md`
- **Compression audit:** `NEWYOU_PRIVACY_PREJIT_COMPRESSION_AUDIT_WORKING_v0.1.3.md`
- **Delta register:** `NEWYOU_PRIVACY_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.3.md`
- **Evidence index:** `NEWYOU_PRIVACY_EVIDENCE_INDEX_WORKING_v0.1.3.md`
- **Live authority baseline:** `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`
- **Date:** 2026-09-09
- **Implementation:** NOT AUTHORISED.
- **Authority:** None. Product/Architecture/Domain/Roadmap/Open Work and approved Feature Pack/JIT authority always win.

# 1. Scope

This contract compresses working semantics for:

- purpose-specific consent/lawful-basis authority and withdrawal;
- Full Deletion request/cancellation/execution/completion;
- retention, restricted retained obligations and legal holds;
- pseudonymisation, irreversible anonymisation and aggregation;
- participant export;
- external processor deletion/export coordination;
- backup/restore non-resurrection;
- cross-Domain deletion/export contracts;
- interactions with Health/Safety/Plans/professional records;
- Commerce/Entitlements/recurring membership;
- Identity closure/re-registration/reconciliation;
- Community/moderation/Security evidence.

It is not:

- Product Law;
- Architecture Law;
- Domain Law;
- a JIT Domain Dossier;
- a Phase 7C Final Feature Pack Contract;
- legal advice;
- an implementation schema;
- permission to create Resources, migrations, queues or provider integrations.

# 2. Current authority anchors

Primary Product/Decision direction includes:

- `DEC-220...DEC-243` Privacy/data lifecycle decisions;
- `DEC-245` verified email required before export/deletion capabilities;
- `DEC-094` purpose-specific permissions/consent;
- current Identity/PMR decisions for closure, recovery, reconciliation and non-reuse;
- current Community and Security decisions for restricted moderation/security evidence.

Architecture requires:

- purpose-specific consent authority;
- durable idempotent cross-system deletion;
- owner-Domain deletion contracts;
- representation-complete deletion across authoritative, derived, cached and external paths;
- pseudonymisation distinct from irreversible anonymisation;
- isolated/minimised retained obligations;
- scoped legal holds;
- restore suppression/deletion replay before service promotion;
- governed export assembled from eligible owner-Domain records with current authority revalidation.

# 3. Ownership contract

| Durable truth | Authoritative owner |
|---|---|
| Canonical Account, closure/recovery, PMR, identity reconciliation lineage | Identity & Access |
| Consent grants/withdrawals/current purpose state; deletion/retention/hold/export orchestration | Privacy & Consent |
| Health/lifestyle facts | Health Records |
| Eligibility/restrictions/Safety Cases | Safety & Eligibility |
| Plan generation/versions/provenance/review-adjustment outcomes | Plans & Nutrition |
| Professional case/review/outcome records | Professional Care |
| Payment/refund/dispute/subscription commercial truth | Commerce |
| Current access/right validity/revocation/consumption | Entitlements |
| Community content/moderation/sanction truth | Community |
| Security/anti-abuse business facts | Existing semantic owner according to the fact — for example Identity & Access, Community, Commerce or another source Domain; **no standalone Security Domain is created** |
| Cross-cutting audit/security evidence | Audit & Evidence; evidence only, never source-domain business truth |

Privacy coordination never creates shared-write ownership.

# 4. Lifecycle separation

Never collapse these into one lifecycle:

```text
Account closure
Consent withdrawal
Full Deletion
Legal hold
Export
Business-record lifecycle
Retention/anonymisation lifecycle
Provider/commercial lifecycle
Identity reconciliation
```

Important current Product timing:

```text
recoverable Account closure
→ 30-day recovery window

Full Deletion Request
→ immediate normal-access revocation
→ 14-day cancellation window
→ irreversible deletion execution
→ verified completion
```

Completed Full Deletion has no Account/product reconstruction path.

# 5. Consent contract

## 5.1 Current authority

Consent/lawful-basis authority is purpose-specific.

Withdrawal:

- invalidates the affected purpose's current authority;
- triggers dependent invalidation obligations;
- does not automatically mean Full Deletion;
- does not automatically invalidate independent purposes/authorities;
- does not let stale workers/events/providers continue merely because work was previously admitted.

Where another lawful basis may permit continued processing, that is an explicit legal/privacy decision, not inferred implementation logic.

## 5.2 Execution rule

Before a protected consequence:

```text
read current owner authority
→ read current purpose/consent/lawful-basis authority
→ execute only if still valid
```

Event delivery order is not authority order.

# 6. Full Deletion contract

## 6.1 General invariant

Full Deletion is a durable, idempotent cross-system orchestration.

Deleting the Account row is not completion.

Every owner of an eligible identifiable representation must execute its own governed consequence.

Protected/stale work must converge on current deletion/suppression authority.

No central Privacy shared-write service may silently mutate every Domain.

## 6.2 Completion

Verified completion requires all applicable paths to reach an approved outcome:

- authoritative records;
- objects/attachments;
- previews/derivatives/extracted values;
- caches/search/read models;
- Analytics/derived representations;
- external processors;
- product/access paths.

A processor request/transport acknowledgement is not automatically processor-side completion.

Retry exhaustion is not privacy completion.

Required unresolved processor path ⇒ deletion remains unresolved.

## 6.3 Health / Safety / Plans / professional records

Use the existing `HSP-UPD-004` seam.

Core rule already fixed:

- self-guided eligible Health data follows delete/irreversibly-anonymise treatment;
- historical immutability is not indefinite identifiable-retention authority;
- practitioner involvement does not transfer record ownership;
- genuine formal professional records may remain only under independently approved professional retention and stay restricted/non-reconstructive;
- Generation Input Basis/provenance must not become a shadow Health store.

Exact category matrix remains JIT + `OQ-009`/`OQ-029`/`OQ-033` expert work.

## 6.4 Commerce / Entitlements / recurring

Historical commercial truth may survive only under approved restricted financial/dispute retention.

It cannot:

- authenticate a deleted participant;
- reactivate Account;
- restore membership;
- satisfy a current Entitlement check;
- reconstruct Plans/products.

Money/contract truth ≠ access truth.

For active recurring membership use accepted `PRIV-WD-002` and resolve `PRIV-UPD-002` before affected behaviour freezes.

## 6.5 Identity closure, re-registration and reconciliation

Closure recovery resumes the same Account/PMR.

Completed deletion permanently severs recovery and retires the old PMR.

A later admitted Account, even with matching email/phone, is new current authority and inherits no deleted Product authority automatically.

Duplicate-reconciliation rules:

- candidate/unresolved/conflicted match does not broaden destructive deletion into another Account;
- applied authoritative reconciliation cannot become a deletion escape hatch;
- stale reconciliation cannot recreate active linkage after suppression;
- contested cross-lineage destruction fails closed pending authoritative Identity resolution;
- compensating correction cannot resurrect validly deleted data or retired PMR.

Default resolution of detailed contested merge/delete mechanics belongs to Identity + Privacy JIT/proof; escalate Product only if participant rights change.

## 6.6 Community / moderation / Security

Keep separate:

- participant-authored Community content;
- independently authored context;
- moderation evidence;
- Security/Fraud evidence.

Participant-authored content follows content-sensitive delete/anonymise treatment.

Independently authored context may survive where governed without preserving deleted Account attribution.

Restricted moderation/security evidence may survive only under its own minimised purpose and cannot reconstruct/authenticate the deleted Account.

A later new Account does not automatically inherit a historical sanction from weak identifier/contact matching.

Human-level continuing exclusion requires explicit Product/Trust & Safety policy.

# 7. Export contract

Participant export is a governed data-rights release, not ordinary product access and not a raw database dump.

`stored ≠ export eligible`.

Each owner Domain determines currently eligible participant-release representation.

Privacy orchestrates and assembles.

Request-time authority is not permanent; revalidate during generation and delivery.

Do not reconstruct:

- already-deleted records;
- irreversibly anonymised records;
- deleted Account/product relationships through historical retained joins.

Owner outcome must distinguish sufficiently between:

- eligible payload;
- no eligible records;
- separate/restricted access path;
- unresolved failure.

Exact participant-facing exclusion wording remains category/legal/JIT detail.

Use `PRIV-WD-001` for export-vs-Full-Deletion sequencing until upstream policy is resolved.

# 8. Retention, legal hold, anonymisation and restore

## 8.1 Retained obligations

Retained evidence must be:

- independently authorised;
- minimised;
- restricted from ordinary product use;
- non-reconstructive;
- category/purpose-specific.

Provider preference does not create retention authority.

## 8.2 Legal hold

An effective hold:

- pauses only deletion within its verified scope;
- keeps held records restricted;
- does not restore Account/product/access authority;
- does not stop unrelated eligible deletion;
- overrides stale destructive permission if effective before destructive commit;
- on release, resumes previously deferred deletion without a new participant request.

One hold's release cannot destroy data still governed by another applicable hold.

## 8.3 Pseudonymisation and anonymisation

Distinct dispositions include, conceptually:

```text
identifiable/current
restricted identifiable
pseudonymous
irreversibly anonymised
irreversibly aggregated
deleted
```

This is not a demand for one universal enum.

A practical re-identification path means irreversible anonymisation has not been achieved.

Direct-identifier removal, hashing, encryption/tokenisation, hidden mapping or ACL restriction is insufficient by itself.

Anonymisation proof covers authoritative, derived, cached, exported and applicable processor representations.

Analytics follows the stronger participant-level removal + irreversible aggregate/suppression rule.

## 8.4 Backup/restore

Historical encrypted backups may age out under normal retention.

Restore does not reinstate the historical world as authority.

Before recovered service is promoted:

```text
restore
→ recover later deletion/suppression/withdrawal/hold authority
→ owner-Domain reconciliation
→ rebuild derived state safely
→ semantic verification
→ promote
```

If current suppression/deletion authority cannot be established, fail closed.

# 9. Current cross-stream seams

## HSP

Use:

`NEWYOU_HSP_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.3.md`

Most relevant seam:

`HSP-UPD-004` — category-specific full-deletion treatment for Plan/Safety/professional-derived records.

Classification: non-blocking JIT/expert detail; core direction already resolved.

## CER

Use:

`NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.1.0.md`

Relevant accepted findings:

- `CER-PT-001` — Commerce success and Entitlement issuance are separate owner-controlled truths;
- `CER-PT-004` — one logical recurring collection identity survives technical retries/replays.

Privacy does not amend CER.

# 10. Accepted working doctrine

These are **accepted non-authoritative Pre-JIT doctrine**, not Product Law.

## `PRIV-WD-001`

> A valid participant Export Request that predates a Full Deletion Request may continue only as a narrowly scoped privacy/data-rights operation during the governed deletion cancellation window, without restoring normal product access. Export generation and delivery remain subject to current verification, authority and scope revalidation. If deletion is cancelled, the export may continue under its normal lifecycle. If irreversible deletion execution begins before delivery completes, any undelivered export is cancelled and its platform-controlled temporary artefacts/delivery capability must be removed under the deletion contract. Completed full deletion may not coexist with a live participant export-delivery path.

## `PRIV-WD-002`

> Once a Full Deletion Request becomes effective and normal product access is revoked, NewYou must not intentionally originate a new recurring membership collection for a service period beginning after that deletion request. Commerce must establish a deletion-driven stop-renewal consequence for the affected participant-linked recurring contract, with exact provider mechanics deferred.
>
> Financial operations already irreversibly in flight may reconcile to truthful Commerce outcomes, but they must not create or restore Entitlement or product access. A successful recurring collection that materialises after the deletion request because of an unavoidable in-flight race requires an explicit Commerce/customer-remediation outcome rather than being treated as an ordinary active-membership renewal.
>
> Completed full deletion may not coexist with participant-linked recurring provider authority that remains capable of automatically initiating future membership charges.
>
> Pending refunds, disputes and chargebacks may continue under approved restricted financial-retention authority and do not by themselves prevent unrelated deletion from proceeding.
>
> If full deletion is cancelled before irreversible execution, the exact membership/subscription restoration, reactivation and paid-period treatment requires explicit Product/Commerce policy plus provider validation.

## `PRIV-WD-003`

> A candidate, unresolved, rejected or conflicted duplicate-identity reconciliation does not broaden one Account's destructive Full Deletion scope into another Account.
>
> Once an Identity & Access reconciliation is authoritatively applied and establishes one canonical participant identity, eligible participant-linked records from the reconciled Account lineages may not escape the canonical participant's Full Deletion merely because their provenance originated under the retired/non-surviving Account. Privacy deletion orchestration must use the authoritative reconciliation lineage sufficiently for each owning Domain to apply its own category-specific deletion/anonymisation/restriction contract.
>
> If Full Deletion/suppression becomes effective while merge consequences are still in flight, stale reconciliation work may not create fresh ordinary-use authority or participant linkage that bypasses deletion.
>
> If an applied reconciliation becomes actively disputed or correction/reversal-pending before irreversible cross-lineage deletion is complete, destructive propagation into the contested other lineage must fail closed pending authoritative Identity resolution rather than risk irreversible over-deletion.
>
> A later compensating reconciliation/correction may restore truthful identity provenance and current topology where possible, but it may not resurrect data validly deleted under then-effective authority, reuse a permanently retired PMR, or reconstruct completed-deletion Account/product authority.

## `PRIV-WD-004`

> Full deletion removes ordinary Community/Account authority and applies the governed content-sensitive delete/anonymise treatment to participant-authored Community content while preserving independently authored context only as permitted by the Community deletion contract.
>
> Approved restricted moderation and security/fraud evidence may survive completed deletion under their respective retention authorities, but such evidence must remain minimised, restricted and non-reconstructive. It may not itself restore the deleted Account, PMR, Community profile, Entitlements or other product authority.
>
> A later new Account must not automatically inherit a historical moderation sanction merely because a retained identifier or weak contact match links it to the deleted Account. Where retained moderation/security evidence legitimately indicates possible sanction evasion or continuing abuse risk, it may inform a governed current Community and applicable security/anti-abuse decision using sufficiently reliable identity/risk evidence, without reconstructing the deleted Account.
>
> Product/Trust & Safety policy must explicitly distinguish Account-scoped sanctions from any sanction intended to represent a human-level continuing exclusion. Implementation must not infer that scope from a generic ban/status field.

# 11. Delta and gate routing

Use `NEWYOU_PRIVACY_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.3.md`.

Summary:

- `PRIV-UPD-001` — upstream Product/Privacy export-vs-deletion policy;
- `PRIV-UPD-002` — upstream Product/Commerce recurring/deletion policy + CER/provider validation;
- `PRIV-UPD-003` — JIT/governance first; Product escalation conditional;
- `PRIV-UPD-004` — upstream Product/Trust & Safety sanction-scope policy.

Existing gates, not new Privacy deltas:

- `OQ-004`, `OQ-009`, `OQ-018`, `OQ-021`, `OQ-023`, `OQ-029`, `OQ-030`, `OQ-031`, `OQ-032`, `OQ-033`, `OQ-037`, `OQ-038`, `OQ-040`;
- `OQ-035` only where adjacent abuse-control threshold proof becomes relevant.

# 12. Mandatory JIT / Architectural Proof

The future JIT/proof must deliberately cover at least these classes.

## 12.1 Current-authority races

- deletion vs downstream writes;
- consent withdrawal vs in-flight work;
- stale/duplicate/reordered jobs/events;
- current-authority revalidation at owner boundary;
- true-race reconciliation;
- idempotent consequence handling.

## 12.2 Processor and deletion completion

- timeout/unavailability;
- crash after request before result persistence;
- duplicate requests;
- late/reordered provider evidence;
- retry exhaustion without false completion;
- approved retained-obligation outcome;
- aggregate completion blocked by unresolved path.

## 12.3 Restore

- old backup before deletion;
- later suppression/hold/withdrawal replay;
- recovery-gated promotion;
- derived/cache rebuild;
- no Account/product resurrection.

## 12.4 Export

- export/deletion cancellation-window race;
- authority changes during generation/delivery;
- undelivered artifact cancellation at irreversible deletion;
- mixed active/historical/restricted/deleted categories;
- zero eligible records vs owner failure;
- no cross-retained reconstruction.

## 12.5 Legal hold

- hold/delete race;
- unrelated deletion continues;
- multiple holds;
- stale/duplicate release;
- release resumes deferred deletion;
- restore preserves current hold authority.

## 12.6 Anonymisation

- mapping retained;
- reversible encryption/tokenisation;
- deterministic identifier;
- quasi-identifiers/sparse cohort;
- processor mapping;
- derived/search/export linkage;
- aggregate suppression.

## 12.7 Health/professional

- HSP category matrix;
- self-guided delete/anonymise;
- formal professional restricted retention;
- professional-review/deletion race;
- retained evidence non-reconstructive.

## 12.8 Commerce/recurring

- retained payment cannot satisfy access;
- delayed renewal/payment after deletion;
- stop-renewal consequence;
- late-charge remediation;
- provider recurring authority gone by completion;
- refund/dispute/chargeback without Account reconstruction.

## 12.9 Identity reconciliation/re-registration

- same-contact closure recovery;
- post-deletion new PMR;
- stale recovery/merge;
- candidate vs applied duplicate;
- contested cross-lineage delete fail-closed;
- compensating correction without resurrection.

## 12.10 Community/Security

- content-sensitive deletion/anonymisation;
- independently authored context;
- restricted moderation evidence;
- Security-specific identifiers;
- weak-match new Account does not inherit sanction;
- governed strong-evidence current decision;
- sanction-scope policy;
- Facebook channel separately validated under `OQ-023`.

# 13. Anti-overdesign contract

Do not assume JIT requires:

- a new Domain;
- a Resource per lifecycle concept;
- a universal status enum;
- Redis/ETS/Cachex/GenServer authority;
- distributed locks;
- a central shared-write privacy database;
- one atomic transaction across Domains;
- a universal event bus/outbox;
- a universal anonymisation primitive;
- provider state as business authority.

Prefer:

Elixir/BEAM + Phoenix + Ash + PostgreSQL first, with durable owner-controlled actions and evidence-led additions only.

# 14. Readiness and routing

Broad Privacy Pre-JIT discovery is complete through `PRIV-PT-015`.

This compact contract is fit as **working input** to future applicable Privacy & Consent JIT planning after the normal governed entry conditions are satisfied.

It does not authorise:

- FP-001 conditional Privacy dossier work unless explicitly adjudicated/authorised;
- CAP-004 / FP-006 JIT merely because this contract exists;
- Phase 7C;
- Architectural Proof;
- implementation.

Current live programme routing remains controlled by `02_OPEN_WORK_v1.2.39.md` and the README.

No new pressure-test programme should start without:

- changed authority;
- new evidence;
- contradiction;
- scope expansion;
- or a JIT question that genuinely cannot be answered from this contract and its detailed provenance.
