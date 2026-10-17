# FP-001 Audit & Evidence JIT Domain Dossier

```text
PHASE 7B JIT DOMAIN DOSSIER
FEATURE PACK: FP-001
DOMAIN: AUDIT & EVIDENCE
IMPLEMENTATION-GRADE PLANNING LAW
NON-EXECUTABLE
NOT PHASE 7C DEVELOPMENT-ENTRY AUTHORITY
DOES NOT OVERRIDE PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW
```

**Artifact version:** v0.1.0 narrow status successor. The exact PR #118 candidate bytes remain at `archive/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` (SHA-256 `0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea`).

**Status:** `CERTIFIED / CURRENT`. PR #118 candidate certification is `COMPLETE`; PR #118 post-merge certification evidence is `COMPLETE`; current-status promotion is `PR #<promotion-pr> STATUS SUCCESSOR`. PR #118 certified and merged the reviewed candidate unchanged. This separate status successor records v0.1.0 as current. Phase 7B reconciliation is `NEXT / NOT_STARTED`. Phase 7C remains `BLOCKED / NOT_STARTED` until successful Phase 7B reconciliation. Proof classification remains `NOT FINALISED`. Phase 8/application implementation remains `UNAUTHORISED`.

<!-- AUDIT_EVIDENCE_V010_CURRENT_LIFECYCLE_STATE_START -->
```json
{
  "artifact_version": "v0.1.0",
  "audit_lifecycle": "CERTIFIED / CURRENT",
  "pr_118_candidate_certification": "COMPLETE",
  "pr_118_post_merge_certification_evidence": "COMPLETE",
  "current_status_promotion": "PR #<promotion-pr> STATUS SUCCESSOR",
  "phase_7b_reconciliation": "NEXT / NOT_STARTED",
  "phase_7c": "BLOCKED / NOT_STARTED",
  "proof_classification": "NOT FINALISED",
  "phase_8_application_implementation": "UNAUTHORISED"
}
```
<!-- AUDIT_EVIDENCE_V010_CURRENT_LIFECYCLE_STATE_END -->

The unchanged semantic body from section 1 onward preserves the exact PR #118 candidate, including source-at-certification references. Current routing comes from the README, manifest and current Open Work successor.

### Inherited PR #118 certification evidence

| Evidence | Result |
|---|---|
| PR #118 | [Merged](https://github.com/JCSchoeman96/NewYou/pull/118) |
| Certified candidate head | `68df8bfb2723c6d4bb414fffae63f20ba0744a6d` |
| PR #118 merge base | `5f5a994e48d9458aaa6397044b3af4d72c5d5e81` |
| Candidate / resulting-main tree | `acd04f523997a0ae8a7ae3edbbfb9280bd4de1ca` |
| Resulting main | `3566f1353ef34af58773aa13c6f5bd61d2613d96` |
| Exact-head Foundation Integrity | [Run 38698409603](https://github.com/JCSchoeman96/NewYou/actions/runs/38698409603), SUCCESS |
| Resulting-main Foundation Integrity | [Run 38704942507](https://github.com/JCSchoeman96/NewYou/actions/runs/38704942507), SUCCESS |
| Independent exact-head review | PASS |
| Candidate/resulting-main tree identity | PASS |
| Exact certified candidate archive SHA-256 | `0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea` |

## 1. Baseline, purpose and scope

This candidate was authored from the verified resulting-main baseline `5f5a994e48d9458aaa6397044b3af4d72c5d5e81`. PR #117 is merged at that SHA with tree `925f794b644efa876b48b8658586ca71c36e393b` and parents `332d51f19d77430fe4e95911920fe0c87cab524a` and `872be31e92d28dbbf2c375c709d52a1405de1941`. Resulting-main Foundation Integrity run [38680269541](https://github.com/JCSchoeman96/NewYou/actions/runs/38680269541) completed successfully for the verified main SHA. Its resulting-main workflow skipped the exact-head-dispatch guard; unit tests and Foundation Integrity succeeded.

This dossier freezes the Audit & Evidence semantics needed by the selected FP-001 outcome, **Trusted bilingual entry and verified identity**. It defines which FP-001 actions require central Audit evidence, the truthful acceptance boundary for selected evidence, the minimum evidence identity and accountability envelope, correction and access rules, and retention/recovery boundaries.

FP-001 still has six affected Domains: Identity & Access, Privacy & Consent, Content & Media, Communications, Audit & Evidence and Analytics. Its seven material capability relationships, outcome, validation objective, dependency position and selected scope remain those in the current Skeleton and Roadmap. This dossier adds no Domain, capability, Feature Pack, shared-write owner or upstream rule.

This is FP-001-specific JIT planning. It does not classify every event for future Feature Packs. It does not begin Phase 7B reconciliation, Phase 7C, proof classification, Phase 8 or application implementation.

## 2. Authority boundary

Audit & Evidence owns the truth of its own evidence only: whether an assertion exists, its provenance and relationships, its integrity and correction history, its access evidence and its governed retention-category metadata. The semantic/source Domain remains authoritative for the business fact or transition being evidenced.

Evidence can prove or account for an action. It cannot authorise, duplicate, repair or redefine that action. Audit does not become:

- a second source of Identity, Communications or any other Domain's business truth;
- a second concurrency authority;
- a repair path that replays or restores source business mutations;
- a general operator or participant database;
- a raw provider-event warehouse; or
- a permanent duplicate of every observable platform event.

There are no shared writes. A source Domain establishes its own business transition through its owning boundary. A central evidence relationship does not grant Audit mutation authority over that source.

## 3. Authority and delta revalidation

The Audit Pre-JIT pack was prepared against `a9c9a8d176e8d62044ca069efeefa60b8f666c8d` and cited older Product, Decision, Roadmap, Open Work and Skeleton versions. Those documents are working evidence, not authority. The following live sources were read at the verified baseline, and every adopted working rule was checked against them.

| Live source at baseline | Current authority relevant to this candidate | Delta revalidation result |
|---|---|---|
| `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` | Sets the current MVP and journey boundary. It does not assign Audit a source-business role or authorise implementation. | No change to the FP-001 outcome or Audit ownership boundary. |
| `00_PLATFORM_v1.8.0.md` | §§15.3–15.4 and 21J.4, 21J.7–21J.12 govern staff authority, MFA, recovery, email changes, duplicate accounts, security holds, scoped grants and break-glass access. v1.8.0's narrow commercial amendment concerns duplicate provider evidence and one intended collection obligation. | The current Product rules support selected security and privileged evidence. The v1.8.0 amendment does not change FP-001 event selection or permit Audit to own source truth. |
| `01_DECISIONS_v1.8.0.md` | DEC-233 requires immutable, minimised, restricted and category-specific audit retention. DEC-234 governs security-event retention. DEC-254 and DEC-255 govern privileged grants and break-glass access. | These decisions constrain minimisation, access and evidence categories. They do not specify exact FP-001 events, retention periods, storage layout or an integrity mechanism. |
| `03_ARCHITECTURE_v1.1.1.md` | §§5–6 require one owner per durable business truth and owner-mediated changes. §8 distinguishes authoritative work, durable obligations and ephemeral observation. §§11–12 and 14 govern retention/deletion, restore, exports, observability and security boundaries. | Supports the source/evidence split and durable E1/E2 semantics below. It leaves exact FP-001 selection and implementation proof to the relevant downstream work. |
| `04_DOMAIN_MAP_v1.2.0.md` | §6.18 assigns restricted, append-only evidence to Audit & Evidence; excludes underlying business transitions and generic logs; assigns retention/deletion exceptions to Privacy & Consent. Its Phase-5 profile names PostgreSQL as durable append-only evidence authority and Redis as non-authoritative for evidence. | Direct authority confirms the Domain boundary, restricted access, append-only correction and PostgreSQL authority. This candidate does not reopen that baseline or select schemas, Resources or an integrity mechanism. |
| `05_ROADMAP_v1.2.2.md` | FP-001 remains the trusted bilingual entry and verified identity outcome with the six affected Domains. OQ-029, OQ-031–OQ-038 and their current stage boundaries remain in force. The Roadmap still has 17 Feature Packs. | No change to FP-001 scope or sequence. Exact retention periods, restore/release targets, incident ownership and executable authentication proof remain downstream at their existing gates. |
| `PLATFORM_OPERATING_MODEL_v1.0.1.md` and `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` | Support receives minimum permitted context. Operator groupings and timelines are projections. Append-only Audit evidence remains separate from internal notes and communication. Sensitive export is a separate governed permission. | These rules prevent an operator screen, note or timeline from becoming Audit truth or granting access. They add no Audit Domain or implementation choice. |
| `README.md`, `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` and `02_OPEN_WORK_v1.2.63.md` | Route the current source versions and current FP-001 lifecycle. #114 adjudicated Audit `REQUIRED`; #116 is the open dossier execution record; #111 is the programme router. | The current lifecycle is `REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING`. Phase 7C remains blocked. This candidate is not added to current routing or the manifest. |
| FP-001 Skeleton v0.1.7 (`FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.7.md`), Identity dossier v0.1.4 (`FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md`) and Communications dossier v0.1.0 (`FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md`) | The Skeleton holds FP-001's six Domains and seven material capability relationships. The certified/current source dossiers define Identity and Communications truth and their cross-domain seams. | No source ownership changes. Identity remains `REQUIRED / COMPLETE / CERTIFIED / CURRENT`; Communications remains `REQUIRED / COMPLETE / CERTIFIED / CURRENT`. Their contracts support the selected rows below. |

Revalidation finds no unresolved Audit-specific Product or Architecture amendment prerequisite. The 2026-10-08 Pre-JIT conclusion was rechecked against current authority; it is not adopted just because it appears in the pack. The current #114 adjudication, not the Pre-JIT's earlier conditional status, makes this dossier authorised work under #116.

AE-WD-* identifiers remain working discovery identifiers. They are not Product Law or Decision Register authority and are not used as this dossier's decision identifiers.

This candidate uses the following routing distinctions:

| Classification | Meaning in this candidate |
|---|---|
| `DIRECT_AUTHORITY` | A rule already required by current Product, Decision, Architecture, Domain or Roadmap authority. This dossier preserves it. |
| `FP-001 JIT SEMANTIC DECISION` | An FP-001 event-selection, evidence-acceptance, identity, minimisation, access or correction rule resolved here within current authority. |
| `IMPLEMENTATION_PROOF` | Executable proof of the selected design, including tamper resistance, direct database/infrastructure bypass resistance, restore/recovery and selected mechanism fault behaviour. |
| `EXPERT_LEGAL_PRIVACY` | Exact retention schedules, legal-hold applicability or retroactivity, permitted post-deletion linkage and anonymisation thresholds. |
| `LATER FEATURE PACK` | Event selection for a future Feature Pack when its governed scope is activated. |
| `STOP / ESCALATION` | A genuine contradiction with current authority, a required shared write, new source ownership or a selected mechanism that requires an unapproved platform/Architecture change. |

The `IMPLEMENTATION_PROOF`, `EXPERT_LEGAL_PRIVACY` and `LATER FEATURE PACK` items do not block authorship of this FP-001 candidate. A genuine `STOP / ESCALATION` finding would prevent the affected contract from being frozen; no such current contradiction was found in this revalidation.

## 4. Audit ownership contract

`DIRECT_AUTHORITY` from Domain Map §6.18: Audit owns its append-only evidence truth and restricted evidence operations. Each source Domain owns its business truth, its concurrency and its own correction of that truth. Communications owns delivery attempts and provider observations. Privacy & Consent governs retention and deletion exceptions. Evidence links may describe cause and provenance, but they do not transfer ownership or permit a cross-domain write.

`FP-001 JIT SEMANTIC DECISION`: central evidence is an accountability record, not a copy of a source object. It cannot restore a missing Account, grant, session, proof-consumption result or message delivery. It cannot settle which concurrent source mutation won. It records the source owner's asserted result and causal reference with the assurance that the evidence process can support.

## 5. FP-001 event/evidence selection matrix

Selection happens before E1/E2/E3 classification. `E1`, `E2` and `E3` describe the acceptance semantics only after a central-evidence selection has been made. A conditional row selects central evidence only for its named material outcome. Observability alone does not make an event a permanent Audit record.

| FP-001 event / source action | Source owner | Central Audit selection | Criticality after selection | Truth, duplicate and failure boundary |
|---|---|---|---|---|
| Successful Account creation + canonical PMR assignment | Identity & Access | YES | E2 | Evidence follows Identity's successful Account/PMR transition. It never creates or assigns the Account or PMR. |
| Failed/aborted registration before Account exists | Identity & Access | NO for routine failure; YES only for a selected material security/abuse outcome | E3 for routine activity; classify a selected security result by its source transition | Identity owns the failure. Do not claim an Account or PMR exists. |
| Email verification proof successfully consumed | Identity & Access | YES | E2 | Evidence records Identity's established proof-consumption result. Delivery or token parsing alone is not consumption. |
| Expired/invalid ordinary verification proof | Identity & Access | NO for routine activity | E3 | Identity owns expiry/invalidity. Do not create a permanent central stream of ordinary invalid attempts. |
| High-risk, replay or abuse verification denial | Identity & Access | YES when the security outcome is material | E2 when selected; otherwise E3 source evidence/telemetry | Record the bounded security result only when selected. It does not imply successful verification. |
| Ordinary sign-in success | Identity & Access | NO by default | E3 | Identity session/authentication state remains authoritative. Routine success is not an immortal Audit event. |
| Ordinary failed password attempt | Identity & Access | NO by default | E3 | Identity owns the failed attempt. Governed abuse telemetry may observe it without creating permanent central evidence. |
| High-risk authentication/security decision | Identity & Access | YES when a material security category requires it | E2 when selected; otherwise source-owned evidence/telemetry | Evidence states the bounded decision and result. It does not infer an authenticated session from a risk observation. |
| Participant self-service password change | Identity & Access | YES | E2 | Identity owns the credential change. Evidence excludes credentials, hashes and secret material. |
| Ordinary automated recovery completion | Identity & Access | YES | E2 | Evidence records the completed Identity recovery transition, not merely a sent message or provider receipt. |
| Manual/exception recovery approval or completion | Identity & Access | YES | E1 admission plus linked source outcome | Evidence admission precedes the exceptional human authority effect. Identity remains the recovery authority. |
| Security hold placement / forced restriction | Identity & Access | YES | E2 | Identity owns the restriction. A central materialisation outage does not preserve unsafe authority when the durable evidence obligation is established at the same acceptance boundary. |
| Security hold release by a privileged actor | Identity & Access | YES | E1 | Required admission evidence precedes release. It records the authorised release attempt, not completed release, until Identity establishes the result. |
| Participant MFA enrolment/disable/reset where material | Identity & Access | YES for material security outcomes | E2 | Identity owns factor state. Only minimum safe outcome and relationship evidence are central. |
| Privileged/manual MFA reset | Identity & Access | YES | E1 | Admission evidence precedes the privileged reset effect; the later result is separately linked. |
| Primary-email change requested | Identity & Access | YES | E2 | Record the request as a distinct historical assertion. Do not copy old or new email addresses by default. |
| Primary-email change confirmed | Identity & Access | YES | E2 | Identity owns participant confirmation and proof consumption. Communication delivery cannot establish it. |
| Primary-email change applied | Identity & Access | YES | E2 | Record the applied source transition and bounded change class without duplicating address values. |
| Primary-email change cancelled, expired or superseded | Identity & Access | YES | E2 | Append the distinct lifecycle result and link it to the request. Do not overwrite earlier evidence. |
| Individual/global session revocation | Identity & Access | YES when the security action is material | E2 | Identity revocation is authoritative. Selected evidence records the revocation result; it does not issue or preserve a session. |
| Device-assurance revocation/security invalidation | Identity & Access | YES when material | E2 | Identity owns device assurance and invalidation. Evidence cannot restore trusted-device authority. |
| Scoped grant activation expanding privileged human authority | Identity & Access | YES | E1 | Admission precedes activation. The grant's scope and approver remain Identity-owned and the evidence cannot grant the role. |
| Grant revocation or expiry | Identity & Access | YES | E2 | Narrowing is not held for central materialisation when the same boundary establishes a durable obligation. Expiry does not become Audit policy. |
| Privileged elevation | Identity & Access | YES | E1 | Record authorised admission before elevated protected work. The evidence cannot broaden its own scope. |
| Break-glass activation | Identity & Access | YES | E1 | Named, reasoned, scoped and time-bounded admission evidence precedes activation. Product's alert and review requirements remain. |
| Break-glass protected use | Source action plus Identity & Access authority | YES | E1 before the protected consequence | Evidence identifies the admitted use and causal source operation. It does not claim the protected consequence succeeded before the source says so. |
| Break-glass expiry or revocation | Identity & Access | YES | E2 | Evidence records the source-owned narrowing result. It is not blocked solely by a central materialisation outage when the obligation is durable. |
| Material break-glass review result | Identity & Access and the named governance owner | YES when it records a material review outcome | E2 | Evidence records a governed review result and its source. Routine review workflow is not copied wholesale into Audit. |
| Ordinary low-risk support lookup | Relevant source owner | No by default; risk/category-dependent | E3 unless a material central record is selected | Support remains scoped to the source. A lookup is not authority to alter source truth. |
| Support-assisted credential/security/recovery correction | Identity & Access | YES when privileged human authority changes Identity/security state | E1 before exceptional authority broadening; E2 for selected narrowing | Evidence proves the governed attempt/outcome. Identity owns the corrected business state. |
| Duplicate-account candidate identified | Identity & Access | Source evidence; YES centrally only for a material review/security outcome | E2 or E3 after event selection | A candidate/conflict is not an applied reconciliation. Identity owns canonical identity and PMR truth. |
| Human-applied duplicate reconciliation | Identity & Access | YES | E1 | Admission precedes the privileged application. Identity decides canonical mapping and preserves source provenance. |
| Material reconciliation rejected, conflicted or corrected | Identity & Access | YES when the result is material | E2 | Append the bounded result and relation to the case/action. Do not create a central event for every candidate observation. |
| Ordinary verification/recovery delivery attempt | Communications | NO central duplicate delivery ledger | E3 for central Audit | Communications owns intent, attempt, delivery state and provider evidence. Identity success is not inferred. |
| Provider accepted/delivered/failed callback | Communications | NO raw central duplicate ledger | E3 for central Audit | Communications authenticates and reconciles provider observations. Duplicate/reordered callbacks remain Communications facts. |
| Material privileged delivery-side action | Communications | YES when accountability requires it | E1 if protected delivery authority changes; otherwise selected E2 | Evidence is a minimum restricted link to Communications' action. It does not copy payloads or grant Identity success. |
| Narrow authorised Audit lookup | Audit & Evidence | Risk/category-dependent; select only when the lookup warrants central evidence | E2 or E3 by selected category | Audit records a human access assertion when required. The query result remains access-controlled evidence, not an operator-wide directory. |
| Bulk/high-sensitivity Audit query/export | Audit & Evidence | YES | E1 before protected disclosure | Record authorised admission before releasing the result. Export access and expiry remain separately governed. |

This matrix is the FP-001 selection decision. Future Feature Packs must perform their own event selection before classifying any selected evidence as E1/E2/E3.

## 6. Evidence acceptance contract

### Selection boundary

Selection happens before E1/E2/E3 classification. A category absent from the central-selection matrix does not become centrally required merely because source telemetry exists. E1/E2/E3 cannot be used to infer that central Audit is required.

### E1 — required before protected effect

For a selected E1 event, minimum truthful durable evidence of the authorised admission or attempt must exist before the protected disclosure or exceptional authority-broadening, restoration or activation effect occurs.

The admission/attempt says that a governed actor/authority attempted or was admitted to act within a stated scope before the protected effect. It does not claim completion or that the source action completed. When the source outcome becomes known, a linked outcome records success, rejection, failure, rollback or unresolved status as the source owner established it. An E1 admission remains truthful history if the later source action fails.

If current required E1 capture integrity cannot be trusted, the protected E1 effect fails closed. A retry can proceed only after current capture integrity is demonstrably restored and the attempt is freshly authorised. A historical gap alone does not create that same failure condition.

### E2 — durable evidence obligation

For a selected E2 source transition, the same acceptance boundary must durably establish either the required central evidence or a lossless, replay-safe/idempotent obligation to materialise it. The logical obligation is part of the truth contract; this dossier does not choose its storage or job implementation.

Once that boundary accepts the source transition and obligation, central materialisation may be delayed. That delay does not rewrite, delay or invalidate source truth. A retry materialises the same assertion safely. It does not create a second source transition or make Audit the authority for the source result.

Authority narrowing, restriction, revocation and security-hold placement use this E2 contract when central evidence is selected. Central materialisation outage alone must not block the safer source transition, provided its durable evidence obligation is established correctly. If the source cannot establish the required obligation, record an integrity/reconciliation failure and escalate through the source owner; do not falsely claim the evidence exists.

### E3 — no central Audit required for correctness

E3 means central Audit is not required for correctness. Source-owned evidence and/or governed telemetry are sufficient. Routine authentication attempts, ordinary delivery observations and generic operational events do not become permanent central evidence because they can be logged.

These E1/E2/E3 labels are dossier-local acceptance terms. They do not amend Product Law, Architecture Law or the Decision Register.

## 7. Evidence identity, correlation and idempotency

Business-operation idempotency and evidence-materialisation idempotency are separate identities.

- Every governed source attempt that is independently evidence-worthy has a distinct logical attempt/assertion identity and restricted provenance reference. A source business operation may be idempotently suppressed while the separate human attempt still deserves evidence.
- Replay of the same evidence assertion/materialisation obligation must be safe and must not create false semantic multiplication.
- Genuinely distinct governed attempts remain distinct evidence, even when actor, target, action and time are similar or the source business effect was suppressed.
- Actor + target + action + similar timestamp is insufficient to prove that two attempts are the same. Deduplicate only when the source evidence identity proves that the replay is the same assertion/obligation.
- Correlation is a relationship, not source concurrency authority. Causal references connect source actions and evidence without establishing source ordering or permission to repair a source transition.
- Arrival order does not redefine source truth. Audit never repairs source-domain atomicity or concurrency.

The minimum logical provenance distinguishes the source Domain and source operation, the governed attempt/assertion, the evidence assertion/materialisation obligation, the actor and executing authority where relevant, causal/correlation relationships, and admission, source-event and outcome times where known. Exact IDs, key formats, database keys and physical correlation schemes remain unfrozen.

## 8. Minimum accountability envelope

Central evidence is a minimum-necessary semantic envelope, not a source snapshot. Include only the categories needed to explain or prove the selected action:

- evidence identity and relationships;
- action or attempt class;
- restricted actor/executing-authority reference;
- restricted target/category reference;
- event/admission/outcome time, when known;
- purpose/scope/authority reference where needed;
- bounded reason code and rationale where needed;
- minimum safe result/outcome class;
- causal/source-operation/correlation reference; and
- limited semantic change summary.

Do not duplicate by default credentials or bearer secrets, full communication bodies, rendered secret URLs, raw provider payloads, payment credentials, full health/private source payloads, generic before/after JSON, diagnostic logs or stack traces, or sensitive categories that do not help accountability. A hash or fingerprint is not automatically anonymised or safe. Structured categorical evidence may itself reveal sensitive information and remains purpose- and access-controlled.

Copy a source value only when a named accountability need cannot be met safely by a restricted reference or bounded classification. The envelope does not become an independent business profile, delivery ledger or source-state snapshot.

## 9. Correction, retraction and supersession

Evidence correction is append-only. A correction, retraction or supersession adds new linked evidence and preserves the original historical assertion while it is lawfully retained. It states who or what made the correction, its authority, reason class, time and relationship to the prior assertion. It must never silently overwrite historical evidence.

Audit can correct or supersede its own evidence assertion and provenance. Audit cannot correct source business truth. A source owner that changes its current business truth supplies its own correction and the evidence relationship; the prior assertion that the platform possessed or relied on remains historically truthful while lawfully retained.

A compensation or reversal is a separate truthful business event. A revocation or restriction may also be a later source event. None is automatically an Audit correction. Evidence correction/supersession is itself a high-risk privileged operation and uses its own selected E1 admission boundary and linked outcome. An unauthorised or unprovable correction fails closed and enters incident/reconciliation handling.

Correction chains must remain truthfully interpretable while retained. They do not force indefinite retention, a permanent full-content shadow or a one-for-one tombstone after lawful disposition.

## 10. Privileged Audit access

Support permission does not imply Audit-reader authority. Audit access is independently authorised, purpose-bound, minimum-necessary, category-aware and scoped to the relevant evidence. A granted role is not a universal Audit super-admin.

| Capability | Boundary |
|---|---|
| Narrow read/lookup | Independently authorised for a source, purpose and category. Record the access assertion centrally when its risk/category requires it. |
| High-sensitivity lookup | Requires explicit high-sensitivity scope and stronger admission evidence before disclosure where selected. |
| Bulk query | Separate capability with cross-participant scope, limits and pre-disclosure evidence. |
| Export | Separate from query/read. Govern creation, access, delivery, expiry and disposition; do not retain an indefinite shadow copy. |
| Correction/supersession | Separate high-risk privilege with E1 admission and linked result. |
| Retention/hold administration | Separate authority. Apply only a valid Privacy & Consent policy/hold basis within its governed scope. |
| Exceptional infrastructure access | Separate emergency control and incident evidence. It grants no source-domain business authority or unrestricted evidence-use permission. |

Bulk/cross-participant/high-sensitivity/export access requires stronger evidence/admission before protected disclosure. Access evidence proves an access attempt or result; it does not broaden the requester's authority.

Normal internal evidence append does not recursively audit itself. A human or system-principal access, correction or administration action may produce one governed evidence assertion when selected. The append terminates at a deliberate final trusted operational boundary covered by security, change-control and implementation-proof controls. It does not create an infinite audit-of-audit chain.

## 11. Retention, hold and disposition

Audit owns its evidence truth and evidence-retention-category metadata. Privacy & Consent owns retention-policy assignment/version, retained-by-obligation classification, legal holds and deletion/privacy governance. Data-owning Domains own their own data contracts. The existing Domain Map §6.18 PostgreSQL authority is preserved.

Keep these lifecycle dimensions separate:

1. historical semantic meaning;
2. correction/supersession lineage;
3. evidence access state;
4. retention classification/basis; and
5. hold/disposition state.

Immutability does not mean immortality. A lawful retention or disposition decision does not silently rewrite historical meaning. A legal hold applies only to its authorised scope and duration. It does not reactivate participant/product authority, broaden evidence access or become universal/permanent retention.

This dossier sets no exact lawful retention period. Exact lawful periods remain unresolved. Exact schedules, legal-hold applicability and retroactivity, policy-version effect, post-deletion linkage and anonymisation thresholds remain `EXPERT_LEGAL_PRIVACY` work. Correction chains must remain interpretable while lawfully retained without making every linked assertion immortal.

Disposition must be provable without retaining an immortal full-content shadow ledger or permanent one-for-one tombstone capable of reconstructing expired evidence. The semantic/proof model must distinguish lawful disposition from unauthorised tampering without retaining expired payloads. Exact proof mechanisms remain `IMPLEMENTATION_PROOF` work.

## 12. Source deletion and non-resolvable references

An Audit evidence reference may become non-resolvable when its owning Domain lawfully disposes of the source record. Audit does not force a source Domain to retain that record forever.

Restricted historical accountability linkage may survive only when independently authorised by the applicable legal/privacy boundary. Such a link:

- must not authenticate someone;
- must not reactivate an Account;
- must not restore product authority;
- must not reconstruct a deleted participant profile; and
- must not become a general participant directory.

This dossier invents no lawful categories or duration for retained linkage; those remain `EXPERT_LEGAL_PRIVACY` decisions.

## 13. Restore, recovery and integrity semantics

### Audit behind source after restore

Audit behind source is an integrity/reconciliation gap. It does not invalidate or rewrite source truth. Recovered evidence discloses recovery provenance. Reconstructed evidence never claims original contemporaneous capture. The source owner reconciles its own business truth.

### Audit ahead of source after restore

Audit ahead of source cannot authorise replay of business mutations into a source Domain. The source owner reconciles its own business truth. Arrival order and the restored Audit copy do not change which source transition occurred.

### Current integrity failure and historical gap

If current required E1 capture integrity cannot be trusted, selected E1 protected effects fail closed. A bounded historical gap becomes incident/reconciliation work. It does not permanently disable unrelated future E1 activity once current capture integrity is demonstrably restored.

A compromised current integrity mechanism reduces assurance in the mechanism and triggers controlled incident/recovery work. It does not make retained historical assertions semantically meaningless or rewrite them. Lawful disposition and unauthorised tampering must remain distinguishable at the semantic/proof level.

## 14. Identity and Communications seams

Identity & Access remains the sole source of Account, PMR, proof, recovery, grant and security truth. Identity also owns verification, session, device, email-change and current Account authority. Central evidence may account for the selected creation/PMR outcome, proof consumption, material credential/security changes, automated and manual recovery, holds/releases, material MFA, email-change lifecycle, session/device revocation, grant/elevation/break-glass, privileged support actions and material duplicate-account reconciliation. Audit never creates an Account, consumes a proof, grants access, restores a session or selects a duplicate-account winner.

Communications owns routine delivery attempts, retries and provider observations, plus their reconciliation. Ordinary delivery and provider state stay in Communications, with no duplicate raw central delivery ledger. Audit receives only selected minimum accountability evidence for material privileged/security delivery actions. Provider state is evidence, never source authority. Communication ambiguity cannot establish Identity success.

The existing Communications source contract remains unchanged: provider outcomes are distinct from Identity proof consumption, and a callback or delivery receipt cannot establish verified identity. The central evidence envelope excludes bearer data, rendered secret URLs, full message bodies and raw provider payloads.

## 15. Semantic pressure cases

The table records the owner, central selection/criticality, truthful claim, retry identity and failure consequence for the required FP-001 cases.

| # | Pressure case | Authoritative source owner | Central selection / criticality | Truthful evidence claim | Duplicate/retry behaviour | Failure/reconciliation outcome |
|---|---|---|---|---|---|---|
| 01 | Same evidence-materialisation obligation replayed twice | Audit for evidence assertion; originating Domain for source event | Selected assertion retains its selected E1/E2 class | One logical evidence assertion exists; replay is not a second event | Replay the same obligation safely without semantic multiplication | If replay integrity is uncertain, reconcile the obligation and preserve the source truth; do not claim a second event |
| 02 | Two genuinely distinct privileged attempts with near-identical actor/target/time | Identity & Access for authority; Audit for evidence | YES when the governed attempt is selected; E1 for broadening | Each distinct admitted attempt is its own historical assertion | Similar actor/target/action/time does not merge attempts; only a proven replay of one obligation deduplicates | Preserve both attempts; source owner resolves any business concurrency result |
| 03 | Business operation is idempotently suppressed but second human attempt is evidence-worthy | Identity & Access | YES for the independently evidence-worthy attempt; E1 or E2 by effect | The second attempt occurred even if its business effect was suppressed | Business idempotency does not suppress distinct attempt evidence | Record the source's suppressed/no-second-effect result; do not claim the second effect happened |
| 04 | E1 admission succeeds and the source protected action later fails | Identity & Access or the source Domain for the protected action | YES, E1 admission followed by linked outcome | Admission proves an authorised attempt, not completion; the later failure is separately asserted | The admission retry refers to the same assertion; outcome is appended once established | Keep admission as truthful history and reconcile the source outcome without rewriting it |
| 05 | Required E1 durable admission cannot be established | Source owner plus Audit integrity boundary | YES, E1 required before effect | No protected effect or completion is claimed | Retry only after current E1 integrity is trusted and fresh authority checks pass | Fail closed before effect; create incident/reconciliation work for the capture failure |
| 06 | E2 source transition commits while central materialisation is delayed | Source Domain | YES, E2 with same-boundary durable obligation | Source transition and obligation were accepted; central materialisation may still be pending | Later materialisation retries the same evidence obligation | Keep source truth valid; reconcile delayed materialisation without rollback or reinterpretation |
| 07 | Delayed E2 materialisation retries after recovery/restart | Source Domain for transition; Audit for materialisation | YES, E2 | Recovered record discloses its actual materialisation/recovery provenance | Retry is idempotent for the same obligation and does not create another assertion | Reconcile any gap; never label reconstructed evidence as original capture |
| 08 | Security revocation/restriction during central Audit outage | Identity & Access | YES when selected, E2 | Evidence obligation accompanies the source-owned narrowing; central copy may lag | Materialise the same obligation later without repeating revocation | Do not block narrowing solely for central outage when the obligation is durable; escalate if the obligation itself cannot be established |
| 09 | Privileged grant/restoration during central Audit outage | Identity & Access | YES, E1 | Admission evidence exists before authority broadening; it does not claim later work completed | Fresh admission is required for a new attempt; retry of one admission does not create a second grant | Fail closed if current required E1 capture is unavailable or untrusted |
| 10 | Source owner later corrects business truth | The source Domain | YES only for the selected source correction | Audit preserves what was previously asserted/relied upon and links the source correction | A source correction is a new source event; prior evidence is not overwritten | Source owner establishes current truth and supplies the relationship; Audit does not correct the source |
| 11 | Evidence correction/supersession attempt itself | Audit & Evidence | YES, E1 privileged admission and linked result | The record states a governed evidence correction attempt, not a source business correction | Same correction obligation is replay-safe; a distinct correction remains distinct | Reject unauthorised/unprovable correction, preserve original, and escalate as incident/reconciliation work |
| 12 | Source record later lawfully disappears | Source Domain and Privacy & Consent | Existing selected evidence remains under its own lawful class | A restricted reference may be non-resolvable after source disposition | No retry may reconstruct or resurrect the source record | Apply source disposition; retain linkage only if independently authorised |
| 13 | Correction chain reaches lawful disposition | Audit and Privacy & Consent under their separate authority | Selected corrections remain linked while lawful; disposition by category | The chain is interpretable for as long as retained, then lawfully disposed | Disposition retry is safe and does not retain a permanent full-content shadow | Prove disposition without an immortal one-for-one tombstone; legal/privacy rules decide linkage |
| 14 | Audit-behind restore | Source Domain for business truth; Audit for evidence | Selected missing evidence is a reconciliation gap | Source truth remains authoritative; reconstructed evidence says it was recovered | Restore/replay deduplicates the same obligation and records recovery provenance | Source owner reconciles truth; current E1 capture must be restored before new protected effects |
| 15 | Audit-ahead restore | Source Domain for business truth; Audit for its evidence | Existing evidence remains evidence, not mutation authority | Audit can show a prior assertion but cannot prove a missing source mutation occurred | Do not replay source changes from Audit | Source owner reconciles current state; unresolved mismatch is an incident/reconciliation item |
| 16 | Current integrity mechanism is compromised | Audit/security operations; source owner for business truth | Selected history remains; current E1 fails closed until trust returns | Historical meaning remains, with reduced assurance about the compromised mechanism | Do not rewrite or duplicate old assertions to simulate integrity | Contain and investigate; disclose assurance limits; restore current capture integrity and distinguish tampering from lawful disposition |
| 17 | Narrow authorised Audit lookup | Audit & Evidence | Risk/category-dependent E2 or E3 | Access evidence states the admitted/read outcome it can prove, not broader authority | Same access-evidence obligation is replay-safe; a distinct lookup can remain distinct | Insufficient scope denies disclosure and routes to the Audit access owner |
| 18 | Unauthorised or insufficiently scoped bulk/high-sensitivity Audit access | Audit & Evidence | YES, E1 before any selected protected disclosure | Admission evidence records the attempt and denial; it does not claim data was disclosed | Retry requires new current authorisation; repeated transport of one assertion does not multiply it | Deny before disclosure, preserve selected denial evidence, and alert/escalate under the access incident path |
| 19 | Audit export creation/expiry without a permanent shadow | Audit & Evidence; Privacy & Consent for applicable disposition | YES, E1 before protected export disclosure | Evidence records export admission and bounded lifecycle facts, not an immortal export copy | A retry of one export obligation is safe; a genuinely new export remains distinct | Expire/dispose the derivative under its lawful class and retain only permissible disposition proof |
| 20 | Routine Communications provider observations are duplicate/reordered | Communications | NO central raw delivery ledger; selected privileged action only | Communications records provider observations and its reconciliation; provider state is not Identity success | Communications deduplicates/reconciles callbacks under its own source contract | Communications resolves ambiguity; central Audit cannot infer delivery or verification |
| 21 | Successful Account plus PMR creation versus failed/ambiguous Account creation | Identity & Access | YES/E2 after successful creation; routine failure is E3, material security result is conditional | Only a successful Identity transition proves Account/PMR creation; failure or ambiguity proves neither | Same source operation is idempotent; a genuinely new attempt remains separately evidence-worthy if selected | Identity resolves ambiguity and canonical PMR truth; Audit records only the established result |
| 22 | Duplicate-account reconciliation with Identity as canonical-truth owner | Identity & Access | YES/E1 for human-applied reconciliation; material conflict/rejection is selected E2 | Evidence proves the governed reconciliation attempt/result, not which account is canonical | Replaying one evidence obligation is safe; distinct human decisions remain distinct | Identity preserves provenance and decides the canonical result; unresolved conflicts remain with Identity |

## 16. Unresolved items and replaceable mechanisms

### `EXPERT_LEGAL_PRIVACY`

- Exact category-specific retention schedules and legal bases.
- Legal-hold applicability, duration, overlap and retroactivity.
- Permitted post-deletion historical linkage and its lawful scope.
- Anonymisation thresholds and when a transformed reference remains identifying.

### `IMPLEMENTATION_PROOF`

- Effectiveness of the selected tamper-resistance mechanism, including direct database and infrastructure bypass resistance.
- Restore/recovery proof, including Audit-behind/ahead divergence and lawful disposition versus unauthorised disappearance.
- E1 fail-closed behaviour, E2 source/obligation atomicity, retry/idempotency/concurrency and the selected mechanism's fault behaviour.
- Query scope, redaction, export expiry/disposition and privileged correction enforcement.

### `LATER FEATURE PACK`

Later Feature Packs must perform their own event selection before classifying selected records as E1, E2 or E3. This dossier does not pre-classify the platform's future event catalogue or create a generic Audit architecture.

### `PROVIDER_EMPIRICAL` and `RELEASE_ONLY`

Provider behaviour remains a provider-specific evidence gate only when a later selected flow depends on it. Exact class-specific RPO/RTO, production incident ownership and release readiness remain at their current Roadmap/Open Work gates.

### Replaceable mechanisms

The frozen Domain Map baseline names PostgreSQL as the durable append-only Audit evidence authority and excludes Redis as evidence authority. Within that boundary, this dossier does not select or freeze:

- Ash Temporal Resources or a plain Ash Resource layout;
- database schemas/tables/indexes;
- transaction implementation;
- Oban job shape or queue topology;
- Redis/ETS/cache choices;
- provider APIs;
- exact idempotency key strings;
- PostgreSQL extensions;
- hash-chain/signature/Merkle/WORM design;
- object-lock infrastructure;
- key-management implementation;
- exact RPO/RTO values;
- object-storage topology; or
- infrastructure account/role implementation.

The Pre-JIT mechanism discussion is candidate material for later implementation and proof evaluation. It is not authority. If a concrete choice requires a change to current Architecture or the frozen PostgreSQL baseline, stop and escalate before selecting it.

## 17. Current governance state and lifecycle

This candidate does not advance current governance state:

| Work item | Current state preserved |
|---|---|
| Identity & Access | `REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4` |
| Communications | `REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0` |
| Privacy & Consent | `NOT_REQUIRED` |
| Content & Media | `NOT_REQUIRED` |
| Audit & Evidence | `REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING` |
| Analytics | `NOT_REQUIRED` |
| Phase 7C | `BLOCKED / NOT_STARTED` |
| Proof classification | `NOT FINALISED` |
| Phase 8/application implementation | `UNAUTHORISED` |

The lifecycle remains candidate → independent exact-head review/certification → merge unchanged → resulting-main verification → separate current-status promotion. Issue #116 remains open through candidate authoring and review. Current Open Work, Skeleton, README, Delivery Atlas, HARDEN-02 and authority manifest are not amended here.

## 18. STOP conditions and review handoff

Stop and return to the appropriate authority if fresh review or later work finds:

- a contradiction with current Product, Decision, Architecture, Domain or Roadmap authority;
- an unowned source business truth or a required shared write;
- an Audit action that would authorise or repair Identity, Communications or another source Domain's truth;
- a need to allow a protected E1 effect without trustworthy required pre-effect evidence;
- a requirement to invent exact legal/privacy categories or retention periods here;
- a mechanism that requires an unapproved database, platform or Architecture change; or
- a need to classify future Feature Pack events before their scope is activated.

This candidate is submitted for fresh independent exact-head review. It claims no independent certification. Its scope is the FP-001 selection matrix and the JIT semantics required to keep Audit evidence accountable, minimised, owner-separated, correctable under a governed append-only model, access-controlled and subject to lawful disposition.

## 19. Provenance trail

### Current authority read and revalidated

- `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `docs/00_platform/00_PLATFORM_v1.8.0.md`
- `docs/00_platform/01_DECISIONS_v1.8.0.md`
- `docs/00_platform/03_ARCHITECTURE_v1.1.1.md`
- `docs/00_platform/04_DOMAIN_MAP_v1.2.0.md`
- `docs/00_platform/05_ROADMAP_v1.2.2.md`
- `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md`
- `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md`
- `docs/00_platform/README.md`
- `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`
- `docs/00_platform/02_OPEN_WORK_v1.2.63.md`

### Current FP-001 contracts read and revalidated

- `docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.7.md`
- `docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md`
- `docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md`

### Non-authoritative Audit evidence read

- `docs/00_platform/working/audit_evidence/NEWYOU_AUDIT_EVIDENCE_PREJIT_CONTRACT_WORKING_v0.1.3.md`
- `docs/00_platform/working/audit_evidence/NEWYOU_AUDIT_EVIDENCE_EVIDENCE_INDEX_WORKING_v0.1.3.md`
- `docs/00_platform/working/audit_evidence/NEWYOU_AUDIT_EVIDENCE_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.3.md`
- `docs/00_platform/working/audit_evidence/NEWYOU_AUDIT_EVIDENCE_GRILL_WORKING_v0.1.3.md`
- `docs/00_platform/working/audit_evidence/deep/NEWYOU_AUDIT_EVIDENCE_PREJIT_DISCOVERY_WORKING_v0.6.2.md`, consulted as supporting discovery history where the compact matrix/source trail required it.

The Pre-JIT sources remain working, non-authoritative evidence at an older repository baseline. Their working labels and mechanism proposals are not Product Law, Decision Register entries or current implementation selections.

### Governance records

- GitHub issue #114 adjudicates the FP-001 conditional dossier dispositions.
- GitHub issue #116 tracks this required Audit dossier candidate and its independent exact-head review/certification lifecycle.
- GitHub issue #111 routes programme-level Pre-JIT reconciliation; it is not this dossier's execution authority.

### Candidate final state

```text
PROPOSED PATH: docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md
PROPOSED VERSION: v0.1.0
STATUS: CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT
AUDIT & EVIDENCE: REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING
PHASE 7C: BLOCKED / NOT_STARTED
PROOF CLASSIFICATION: NOT FINALISED
PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED
```
