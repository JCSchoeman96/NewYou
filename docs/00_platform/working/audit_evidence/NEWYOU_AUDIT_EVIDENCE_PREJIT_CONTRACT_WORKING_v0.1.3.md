# NewYou Audit & Evidence Pre-JIT Contract — Working v0.1.3

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PRE-JIT SEMANTIC CONTRACT
SUPERSEDES COMPACT v0.1.2
```

- **Prepared / full re-review:** 2026-10-08
- **Live repository baseline checked:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Discovery basis:** `NEWYOU_AUDIT_EVIDENCE_PREJIT_DISCOVERY_WORKING_v0.6.2.md`
- **Discovery SHA-256:** `6a82725d71a8b861d8be88711bba209a3ad390739c195f69fc0560c1d95bfc91`

## 1. Purpose and authority boundary

This compact contract preserves the current accepted meaning of the Audit & Evidence Pre-JIT discovery stream. It is not Product Law, Architecture Law, Domain Law, a JIT Domain Dossier, Phase 7C authority or implementation permission.

The live governed repository remains canonical. Higher authority wins if it later conflicts with this working contract.

### Programme-status boundary

> **Pre-JIT working adjudication:** `FP-001 Audit & Evidence JIT Domain Dossier = REQUIRED`.
>
> **Live governed programme status at baseline `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`:** `AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION`.
>
> **Phase 7C:** `BLOCKED / NOT_STARTED`.

This contract does not promote the working adjudication into governed programme state. Only an explicit authorised current-status adjudication/promotion may do that.

### Upstream-scope boundary

The statement that no upstream amendment is required means:

> **No unresolved Audit-specific Product or Architecture amendment prerequisite has been identified.**

Separately governed upstream gaps in participating Domains remain binding when a Feature Pack exercises those behaviours. This Audit contract neither resolves nor supersedes them.

Core doctrine:

> **Business truth remains owned by the semantic Domain. Audit & Evidence owns only its own governed evidence truth and must never become a second source of the business truth being audited.**

## 2. Evidence selection and criticality model

Central Audit selection happens before E1/E2 classification.

- **E1 — capture required before protected effect:** required durable admission/attempt evidence must exist before the protected disclosure or exceptional authority-changing effect proceeds.
- **E2 — durable evidence obligation:** a source transition may commit only when the same acceptance boundary durably establishes either the required evidence or a lossless idempotent obligation to materialise it.
- **E3 — central Audit not required for correctness:** source-owned evidence and/or governed telemetry is sufficient.

Where central evidence is selected:

- exceptional human authority **broadening/restoration** is E1;
- authority **narrowing/revocation/restriction** is E2 so safer action is not blocked by central Audit materialisation outage.

Current higher authority requires governed audited emergency/privileged access and defines no explicit unaudited bypass. This Pre-JIT therefore adopts fail-closed E1 semantics when required pre-effect evidence cannot be durably established. A future requirement to permit such protected access despite E1 evidence failure is `UPSTREAM_PRODUCT`.

## 3. Accepted semantic decision register

The entries below preserve all accepted `AE-WD-001..074` decisions. The cumulative ledger remains the provenance/history source.

### Evidence criticality and truthfulness

- **AE-WD-001 — Required material evidence is not best-effort.** If governing law requires material evidence, “business succeeded and maybe we log later” is invalid.
- **AE-WD-002 — Fail-closed pre-disclosure E1.** Before the first protected payload is disclosed, minimum durable evidence of the authorised disclosure attempt must exist; it must not claim completion.
- **AE-WD-003 — Truthful source transition may use a durable obligation.** Source truth may commit independently of central materialisation only when required Audit evidence is durably accepted with it or a lossless idempotent obligation is established at the same acceptance boundary.
- **AE-WD-004 — Disclosure has two evidence moments.** Pre-disclosure admission is E1; actual completion/partial/failure/unknown outcome is appended later and, if not synchronous, survives as a durable E2 obligation.
- **AE-WD-005 — State only what can be proved.** Requested ≠ authorised ≠ initiated ≠ completed ≠ actually viewed/understood; Audit must not upgrade observations into stronger claims.
- **AE-WD-006 — No unaudited privileged bypass under the current working contract.** Current authority requires governed audited privileged/emergency access and defines no explicit unaudited bypass; this Pre-JIT applies fail-closed E1 timing.

### Identity, retries, exactly-once and correction

- **AE-WD-007 — Exactly-once Audit is not the invariant.** The invariant is no material evidence loss, no false semantic multiplication, no silent overwrite and no conflation of distinct attempts.
- **AE-WD-008 — Business idempotency does not erase material attempts.** Suppressing a duplicate business effect does not automatically suppress evidence of genuinely distinct governed attempts.
- **AE-WD-009 — Evidence-materialisation retry is a separate idempotency boundary.** Retrying the same evidence assertion must be replay-safe; retrying the underlying governed action is a different decision.
- **AE-WD-010 — Deduplicate only demonstrably identical evidence-materialisation retries.** Similar actor/target/action/time is insufficient proof that two governed attempts are the same assertion.
- **AE-WD-011 — Correction/supersession is append-only.** Corrections, retractions and supersessions are new immutable linked evidence, never destructive rewrite.
- **AE-WD-012 — Evidence-authority principle.** Audit is authoritative for its own evidence existence, provenance, integrity, relationships, corrections, access and governed retention state; it never authorises or reconstructs source business truth.

### Evidence envelope and minimisation

- **AE-WD-013 — Evidence envelope, not source snapshot.** Capture the minimum semantic accountability envelope, not duplicated business payload.
- **AE-WD-014 — Prefer durable references and bounded categorical assertions.** Copy source values only when a specific accountability requirement cannot safely be met by reference/classification.
- **AE-WD-015 — Limited change summary is not before/after snapshotting.** A semantic change class such as `primary_email_changed` is preferred over copying old/new sensitive values.
- **AE-WD-016 — Minimise reason/purpose free text.** Prefer governed codes plus only bounded rationale actually needed for accountability.
- **AE-WD-017 — Hash/fingerprint is not automatic safety/anonymity.** Use only for a justified integrity/correlation purpose with residual linking risk governed.
- **AE-WD-018 — Audit access is privileged.** Access is purpose-bound, minimum-necessary and category/scope-aware; Audit is not a general operator-search database.
- **AE-WD-019 — Audit-of-audit has a stopping rule.** Material human/system-principal access/admin action can be evidence-worthy, but normal internal evidence append does not recurse forever.
- **AE-WD-020 — Restricted historical accountability linkage may survive ordinary product deletion only when independently authorised.** Such linkage cannot authenticate, reactivate, reconstruct product authority or become a general participant profile.

### Retention, hold and disposition

- **AE-WD-021 — Immutability is not immortality.** Evidence remains subject to independently governed retention, legal hold, deletion/anonymisation and lawful disposition.
- **AE-WD-022 — Meaning and disposition are orthogonal.** Retention/hold/expiry must not silently rewrite historical semantic meaning.
- **AE-WD-023 — Retention ownership split.** Audit applies its own evidence-retention contract; Privacy & Consent supplies governing retention/hold/deletion authority; neither acquires the other's truth.
- **AE-WD-024 — Legal hold is scoped and temporary.** It pauses applicable disposition only in scope/duration; it does not reactivate product authority, broaden access or create permanent retention.
- **AE-WD-025 — Preserve retention-class provenance.** Evidence must explain why it was retained/disposed; later policy applicability is governed by the relevant legal/privacy contract, not inferred retroactively.
- **AE-WD-026 — Disposition must be provable without an immortal shadow ledger.** Disposition proof must not reconstruct expired evidence or retain one-for-one tombstones forever.
- **AE-WD-027 — Correction-chain disposition remains truthful.** Linked-evidence disposition must preserve truthful interpretability while authorised without using links to force indefinite retention.
- **AE-WD-028 — Do not collapse lifecycle dimensions.** Evidence meaning, correction lineage, access state, retention classification and legal-hold/disposition state are independent dimensions.

### Source truth, provider contradiction and recovery

- **AE-WD-029 — E2 delay cannot rewrite source truth.** Once the source transition and lossless obligation are accepted, delayed materialisation does not delay, reverse or reinterpret source authority.
- **AE-WD-030 — Arrival order is not authority order.** Audit may not use “latest evidence wins” to reinterpret another Domain's business truth.
- **AE-WD-031 — Later source correction does not erase historical accountability.** Audit may preserve that the platform possessed/relied on an earlier assertion even after the source owner later corrects it.
- **AE-WD-032 — Audit references may become non-resolvable.** Source disposition does not create an obligation to preserve/reconstruct the referenced source record.
- **AE-WD-033 — Audit references do not extend source/provider retention.** Each owner applies its own lawful retention contract.
- **AE-WD-034 — Audit corrects evidence, not source business truth.** Source truth corrections require source-owner authority; Audit may govern only its own evidence metadata/provenance correction.
- **AE-WD-035 — Reconstructed evidence discloses recovery provenance.** Recovery material must never masquerade as original contemporaneous capture.
- **AE-WD-036 — Audit may trigger reconciliation but never restore source truth directly.** Source-owner reconciliation decides current business truth.
- **AE-WD-037 — Historical gaps and current E1 viability differ.** A bounded historical gap does not permanently halt future E1 once current capture is trustworthy; inability to trust current capture does halt E1.

### Integrity, operator power and tamper resistance

- **AE-WD-038 — Semantic immutability is not physical immobility.** Governed key rotation, migration, partition movement, storage-format change, backup/restore or compression may change bytes while preserving evidence identity, meaning, provenance, integrity and retention constraints. Primary route: `DOMAIN_JIT`.
- **AE-WD-039 — Tamper-resistant means no silent historical rewrite.** Ordinary application/support/staff/admin authority cannot silently edit/replace retained history; correction and lawful disposition use their governed paths.
- **AE-WD-040 — Audit administrator is not universal super-admin.** Audit infrastructure authority grants neither source-domain business authority nor unrestricted evidence access.
- **AE-WD-041 — Separate dangerous capabilities.** Read, bulk query/export, correction/supersession, retention/hold administration and exceptional infrastructure access are distinct capabilities; ordinary roles cannot suppress evidence of their own governed actions.
- **AE-WD-042 — Material Audit access is an evidence boundary.** Bulk/cross-participant/high-sensitivity/export access requires pre-disclosure evidence; bulk/high-risk access is E1, while lower-risk lookup remains category-specific.
- **AE-WD-043 — Audit exports are temporary protected derivatives.** Govern creation, access, delivery, expiry and disposal; exports must not become an indefinite shadow ledger. Primary route: `DOMAIN_JIT`.
- **AE-WD-044 — Exceptional bypass paths are part of the threat model.** Tamper proof must cover direct database/infrastructure paths, not only normal Ash/application actions.
- **AE-WD-045 — No infinite meta-audit chain.** Define a deliberate final trusted operational/infrastructure boundary; do not recursively create evidence systems forever. Primary route: `DOMAIN_JIT`.
- **AE-WD-046 — Confidentiality and integrity are separate.** Encryption/key protection alone does not establish evidence integrity/tamper resistance; confidentiality, integrity, availability and provenance remain separate concerns. Primary route: `DOMAIN_JIT`.
- **AE-WD-047 — Protection-mechanism compromise does not rewrite evidence history.** It changes assurance and triggers governed incident/recovery consequences while historical semantic meaning remains unchanged. Primary route: `IMPLEMENTATION_PROOF`.
- **AE-WD-048 — Current integrity failure differs from bounded historical anomaly.** Current inability to capture trustworthy required evidence fails E1 closed; a bounded historical anomaly becomes incident/reconciliation work and does not halt unrelated future E1 after current integrity is restored. Primary route: `DOMAIN_JIT`.
- **AE-WD-049 — Lawful disposition must be distinguishable from tampering.** The integrity model must distinguish governed disappearance from unauthorised disappearance/mutation without immortal copies. Primary route: `DOMAIN_JIT`.
- **AE-WD-050 — Evidence correction is itself high-risk privileged action.** Correction/supersession has durable provenance, cannot erase the original, cannot become source correction authority, and is E1.

### FP-001 selection and criticality

- **AE-WD-051 — FP-001 does not audit everything.** Routine authentication, validation, delivery attempts and provider observations do not become permanent central Audit merely because observable.
- **AE-WD-052 — FP-001 source-transition default.** When selected central evidence is required but source truth must remain truthful independently of materialisation availability, use E2.
- **AE-WD-053 — Security narrowing cannot be blocked.** Session/grant/device revocation and security-hold placement use lossless E2 semantics rather than being held hostage by central materialisation outage.
- **AE-WD-054 — Privilege broadening is asymmetric.** Exceptional human authority activation/restoration is E1; narrowing/revoking is E2.
- **AE-WD-055 — Routine authentication is not an immortal Audit stream.** Ordinary successes/failures are not automatically permanent central evidence; material high-risk/security outcomes may be.
- **AE-WD-056 — Primary-email-change evidence.** Requested/confirmed/applied/cancelled/superseded outcomes require linked historical Audit evidence while current operation truth remains Identity-owned; do not copy old/new addresses by default.
- **AE-WD-057 — Duplicate reconciliation distinction.** A candidate/conflict is not an applied reconciliation; material human application/correction is E1 while canonical identity/PMR consequences remain Identity-owned.
- **AE-WD-058 — Communications boundary.** Delivery attempts/retries/provider observations/reconciliation remain Communications-owned; central Audit receives only minimum accountability evidence for material privileged/security delivery actions.
- **AE-WD-059 — FP-001 Audit access boundary.** Underlying support permission does not imply Audit-reader authority; bulk/high-sensitivity evidence access is E1, narrow lookup risk/category-specific.

### Crash/race semantics and dossier adjudication

- **AE-WD-060 — E2 acceptance atomicity.** Source transition plus its guaranteed durable evidence obligation are one acceptance boundary; materialisation may happen later.
- **AE-WD-061 — E1 pre-effect evidence must not claim completion.** It records authorised admission/attempt and actor/authority/scope/reason/causal identity; linked outcome follows source result.
- **AE-WD-062 — Failed E1 attempts remain truthful history.** Later failure/guard rejection/rollback does not erase admission; append failure/abort/unknown as actually established.
- **AE-WD-063 — Audit never repairs broken source atomicity.** Owner-local proof consumption/state/recovery invariants remain the source Domain's responsibility.
- **AE-WD-064 — Audit ordering is not source concurrency ordering.** The owning Domain determines authoritative concurrency outcomes; Audit records causal relationships only.
- **AE-WD-065 — FP-001 Audit dossier is REQUIRED.** Phase 7C cannot complete the implementation-grade FP-001 Audit contract without Audit-owned Domain semantics for selection, E1/E2, minimisation, identity/idempotency, access, correction/supersession and retention class.

### Cross-domain generalisation and completeness

- **AE-WD-066 — Evidence selection precedes E1/E2.** E1/E2 classifies a selected central evidence obligation; it does not decide that central Audit is required.
- **AE-WD-067 — Compensation is not automatically correction.** Refund/reversal/revocation/restriction may be a later true business event while the earlier event remains historically true.
- **AE-WD-068 — Safety/authority broadening vs narrowing follows the same asymmetry.** When central evidence is selected, exceptional human broadening/restoration is E1; narrowing/pause/withdrawal is E2.
- **AE-WD-069 — Structured/categorical evidence may itself be sensitive.** Result/restriction/reason codes may reveal health, identity, security or financial information and require minimisation.
- **AE-WD-070 — Downstream incompleteness is not upstream ambiguity.** Resource representation, exact retention periods, mechanisms, provider behaviour, RPO/RTO and executable proof remain downstream where higher authority already fixes the semantic invariant.
- **AE-WD-071 — No current Product/Architecture amendment is required.** The Audit JIT dossier can be written under current authority.
- **AE-WD-072 — Later Feature Packs still require event-selection adjudication.** This Pre-JIT does not pre-classify all future events; each Feature Pack/JIT decides which semantic events require central Audit before E1/E2.
- **AE-WD-073 — Mechanisms remain replaceable.** Temporal/plain Ash Resources, cryptographic structures, WORM and similar mechanisms do not become architecture merely because useful.
- **AE-WD-074 — Pre-JIT semantic discovery is complete enough for JIT.** Ownership, criticality, acceptance, idempotency/correction, minimisation, access, retention, cross-domain authority and recovery semantics are sufficiently defined to prevent downstream invention.

## 4. FP-001 event/evidence matrix

This matrix preserves the accepted Pass 8 result rather than weakening `YES` central-evidence selections.

| FP-001 action/event | Source authority | Central Audit | Criticality / rule |
|---|---|---|---|
| Successful Account creation + canonical PMR assignment | Identity & Access | **YES** | **E2** |
| Failed/aborted registration before Account exists | Identity & Access | Usually NO unless material security/abuse | E3 centrally |
| Email verification proof successfully consumed | Identity & Access | **YES** | **E2** |
| Expired/invalid ordinary verification proof | Identity & Access | Usually NO permanent central | E3 centrally |
| High-risk/replay/abuse verification denial | Identity & Access | YES when material security outcome | category-specific E2/E3 |
| Ordinary sign-in success | Identity & Access | Not automatically | E3 centrally |
| Ordinary failed password attempt | Identity & Access | Not automatically | E3 centrally |
| High-risk authentication/security decision | Identity & Access | YES where material category requires | E2 |
| Participant self-service password change | Identity & Access | **YES** | E2 |
| Ordinary automated recovery completion | Identity & Access | **YES** | E2 |
| Manual/exception recovery approval/completion | Identity & Access | **YES** | E1 admission + linked outcome |
| Security hold placement / forced restriction | Identity & Access | **YES** | E2 |
| Security hold release by privileged actor | Identity & Access | **YES** | E1 |
| Participant MFA enrol/disable/reset where material | Identity & Access | **YES** | usually E2 |
| Privileged/manual MFA reset | Identity & Access | **YES** | E1 |
| Primary-email-change requested | Identity & Access | **YES** | E2 historical evidence |
| Primary-email-change confirmation | Identity & Access | **YES** | E2 |
| Primary-email-change applied | Identity & Access | **YES** | E2 |
| Primary-email-change cancelled/expired/superseded | Identity & Access | **YES** | E2 linked history |
| Individual/global session revocation | Identity & Access | YES when material security action | E2 |
| Device assurance revocation/security invalidation | Identity & Access | YES when material | E2 |
| Scoped grant activation expanding privileged human authority | Identity & Access | **YES** | E1 |
| Grant revocation/expiry | Identity & Access | **YES** | E2 |
| Privileged elevation | Identity & Access | **YES** | E1 |
| Break-glass activation | Identity & Access | **YES** | E1 |
| Break-glass protected use | Source action + Identity authority | **YES** | E1 before protected consequence |
| Break-glass expiry/revocation | Identity & Access | **YES** | E2 |
| Break-glass review result | Identity/governance owner | **YES** | E2 |
| Ordinary low-risk support lookup | relevant source owner | risk/category dependent | normally E3 |
| Support-assisted credential/security/recovery correction | Identity & Access | **YES** when privileged human authority changes identity/security | E1 |
| Duplicate-account candidate identified | Identity & Access | source evidence; central only if material review/security event | E2/E3 by selected category |
| Human-applied duplicate reconciliation | Identity & Access | **YES** | E1 |
| Reconciliation rejected/conflicted/corrected | Identity + Audit evidence relation | YES where material | E2 |
| Ordinary verification/recovery delivery attempt | Communications | no duplicate central delivery ledger | source-owned / E3 centrally |
| Provider accepted/delivered/failed callback | Communications | no raw duplicate central ledger | source-owned |
| Privileged delivery-side action | Communications | YES where accountability required | E1 if protected delivery authority changes; otherwise selected E2 |
| Narrow authorised Audit lookup | Audit & Evidence | risk/category dependent | E2/E3 |
| Bulk/high-sensitivity Audit query/export | Audit & Evidence | **YES** | E1 |

## 5. Evidence envelope and prohibited shadow authority

A central evidence envelope may contain only the minimum required accountability data, typically:

- evidence identity/relationships;
- action or attempt class;
- restricted actor/executing-authority reference;
- restricted target/category reference;
- time;
- purpose/scope/authority reference where required;
- reason code and bounded rationale where required;
- minimum safe result class;
- causal/source-operation/correlation reference;
- limited semantic change summary.

Do not centrally duplicate by default:

- credentials, passwords, bearer secrets;
- full communication bodies or rendered secret URLs;
- raw provider payloads;
- payment credentials;
- full health/private business payloads;
- generic before/after JSON;
- diagnostic logs/stacks;
- sensitive categorical detail that is not required for accountability.

## 6. Retention and lifecycle dimensions

Audit owns its evidence and evidence-retention-class metadata. Privacy & Consent owns retention-policy assignments/versions, retained-by-obligation classification, legal holds and deletion orchestration. Each data-owning Domain executes its own retention/export/deletion contract.

The model must keep separate:

1. historical evidence meaning;
2. correction/supersession lineage;
3. evidence access state;
4. retention classification/basis;
5. legal-hold/disposition state.

No one lifecycle enum may collapse those dimensions merely for implementation convenience.

Exact lawful periods, post-deletion linkage categories, hold retroactivity and anonymisation thresholds remain `EXPERT_LEGAL_PRIVACY`.

## 7. Integrity and privileged evidence operations

Ordinary roles cannot silently rewrite retained evidence or suppress evidence of their own governed actions.

Evidence correction/supersession is itself a high-risk privileged **E1** action with durable provenance.

Lawful disposition must be distinguishable from unauthorised disappearance/mutation without keeping immortal full-content tombstones.

A security/key/integrity incident changes assurance and triggers recovery/incident consequences; it does not retroactively change the semantic meaning of retained evidence.

Tamper-resistance proof must include direct database/infrastructure paths and identify the final trusted control boundary.

## 8. Restore/reconciliation

Audit-behind restore does not invalidate source truth. Missing evidence becomes an integrity/reconciliation gap; reconstructed evidence must disclose recovery provenance.

Audit-ahead restore never authorises replay of business mutations into the source Domain. The source owner reconciles its own truth.

Current inability to establish trustworthy required E1 evidence fails E1 closed. A bounded historical gap does not indefinitely disable unrelated future E1 once current capture integrity is proven.

## 9. Mechanism routing

### AE-MECH-001 — Ash Temporal Resources

Ash Temporal Resources remain a JIT-time candidate only.

Current working preference is **not** to assume Temporal Resources for the core Audit evidence ledger because the accepted model is multiple independently meaningful immutable assertions, not version-history of one logical row. Plain append-only Resources may therefore be semantically simpler.

At JIT, reverify then-current Ash/AshPostgres stability and compatibility. If a selected mechanism would require an unapproved PostgreSQL/platform/architecture change, STOP and escalate to `UPSTREAM_ARCHITECTURE`.

### AE-MECH-002 — Cryptographic/WORM mechanisms

Hash chains, signatures, Merkle structures, WORM/object-lock storage and dedicated append-only services are replaceable JIT candidates only. They must remain compatible with lawful disposition, correction/supersession and DR. Do not add specialist infrastructure without demonstrated need.

## 10. FP-001 dossier adjudication

> **FP-001 Audit & Evidence JIT Domain Dossier: REQUIRED**

This is current working doctrine under `AE-WD-065`.

Phase 7C remains blocked from inventing the implementation-grade Audit contract.

## 11. Pre-JIT completion boundary

Current unresolved **Audit-specific** `UPSTREAM_PRODUCT` amendment prerequisite: **none**.

Current unresolved **Audit-specific** `UPSTREAM_ARCHITECTURE` amendment prerequisite: **none**.

Separately governed upstream gaps in participating Domains remain binding; this Audit Pre-JIT does not close them.

Remaining work is correctly downstream in `DOMAIN_JIT`, `CROSS_DOMAIN_JIT`, `EXPERT_LEGAL_PRIVACY`, `IMPLEMENTATION_PROOF`, `PROVIDER_EMPIRICAL`, `RELEASE_ONLY` or `FUTURE_ONLY`.

This conclusion must be rechecked if the live repository head/authority changes materially before use.
