# NEWYOU_AUDIT_EVIDENCE_PREJIT_DISCOVERY_WORKING_v0.6.2.md

- **Document status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY LEDGER
- **Document version:** v0.6.2
- **Started:** 2026-10-08
- **Last updated:** 2026-10-08
- **Governance mode:** CUMULATIVE / APPEND-ONLY DISCOVERY EVIDENCE
- **Implementation:** NOT AUTHORISED
- **Phase 7C authority:** NONE
- **Repository mutation:** NONE — this artifact was materialised outside the canonical repository for review before any governed repository change
- **Canonical repository:** `https://github.com/JCSchoeman96/NewYou`
- **Live authority baseline used for this pass:** `main` at `a9c9a8d176e8d62044ca069efeefa60b8f666c8d` (verified 2026-10-08)
- **Authority rule:** Product Law → Architecture Law → Domain Law → Roadmap → supporting operating/frontend contracts → current Open Work → approved Feature Pack/JIT contracts → proof → implementation
- **Authority boundary:** This document records accepted working hypotheses, pressure-test outcomes, unresolved issues and future JIT questions. It does not amend Product, Architecture, Domain or Roadmap Law; it does not create a JIT Domain Dossier; it does not authorise Phase 7C or implementation.
- **Pre-JIT working adjudication:** `FP-001 Audit & Evidence JIT Domain Dossier = REQUIRED` under accepted `AE-WD-065`.
- **Live governed programme status at pinned baseline:** `AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION`; `PHASE 7C: BLOCKED / NOT_STARTED`.
- **Promotion boundary:** The Pre-JIT working adjudication does not itself change governed programme state. Only an explicit governed current-status adjudication/promotion may do so.
- **Upstream-scope boundary:** “No upstream gap” in this stream means **no unresolved Audit-specific Product or Architecture amendment prerequisite**. Separately governed upstream gaps in participating Domains remain binding and are not resolved by this Audit pack.
- **Supersession discipline:** Earlier accepted working decisions are not silently deleted. Later passes must append a new decision that explicitly refines, supersedes or rejects an earlier one.
- **SemVer discipline:** Minor version for substantive discovery additions/refinements; patch version for provenance, wording, formatting or mechanical corrections that do not change accepted meaning.

---

# 1. Purpose

This bounded discovery stream reduces uncertainty around **Audit & Evidence** before future Feature Pack JIT work—especially FP-001 and later commerce, safety, privacy and operations work—so downstream JIT does not invent Audit semantics.

The central doctrine under pressure is:

> **Business truth remains owned by the semantic Domain. Audit & Evidence records durable evidence about material actions and outcomes but must not become a second source of business truth.**

Refined working principle:

> **The semantic Domain owns the audited business truth. Audit & Evidence is authoritative only for the existence, provenance, integrity, relation, correction/supersession, access and governed retention state of its own evidence. An Audit record never authorises or reconstructs source-domain business state merely because it describes that state.**

This stream must pressure-test at least:

- business truth vs evidence truth;
- exactly-once illusion;
- failed attempts;
- correction/supersession;
- minimisation;
- access/operator controls;
- retention;
- cross-domain failure;
- security/abuse;
- disaster recovery;
- deletion/anonymisation;
- sensitive security evidence risk;
- provider contradiction;
- delayed evidence behind source truth.

---

# 2. Current authority anchors

Current live authority reviewed for this stream includes:

- `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `docs/00_platform/00_PLATFORM_v1.6.0.md`
- `docs/00_platform/01_DECISIONS_v1.6.0.md`
- `docs/00_platform/02_OPEN_WORK_v1.2.59.md`
- `docs/00_platform/03_ARCHITECTURE_v1.1.1.md`
- `docs/00_platform/04_DOMAIN_MAP_v1.2.0.md`
- `docs/00_platform/05_ROADMAP_v1.2.0.md`
- `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md`
- `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`
- `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`
- `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`
- `docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md`
- `docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md`
- `docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md`
- `docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md`

Relevant non-authoritative cross-stream working packs consulted:

- Privacy / Consent / Participant Data Lifecycle
- Content & Media
- Communications
- Commerce / Entitlements / Recurring Membership
- Health / Safety / Plans

The live repository remains authoritative over any snapshot, prior chat summary or this working file.

---

# 3. Existing Domain and Architecture constraints

## 3.1 Audit & Evidence Domain boundary

Current Domain Law establishes Audit & Evidence as owner of:

- append-only audit evidence for sensitive/domain-governed actions where central evidence is required;
- security/fraud event evidence under security-specific identifiers;
- break-glass/privilege-access evidence and review linkage;
- incident/evidence linkage and release/go-no-go decision evidence where centrally retained;
- audit query/access controls;
- evidence retention-class metadata.

Audit & Evidence does **not** own:

- the underlying business transition;
- generic logs, metrics or traces;
- the professional clinical record;
- payment/provider reconciliation truth except minimum audit linkage;
- Community moderation case business state;
- Research responses;
- official Voting results;
- PMR or Account business truth.

## 3.2 Evidence is not automatically Audit-owned

Examples already established upstream:

- Communications owns `MessageIntent`, `DeliveryAttempt`, provider/delivery evidence and reconciliation.
- Commerce owns payment attempt/transaction state, verified provider evidence and refund/dispute/settlement reconciliation.
- Health Records owns health facts/evidence/provenance.
- Safety & Eligibility owns eligibility outcome and risk-routing evidence/version applied.
- Content & Media owns scoped review/approval evidence where applicable.
- Voting & Balloting owns vote-submission/integrity/finalisation business truth.
- Audit receives only the minimum cross-cutting accountability/security/governance evidence required by law.

## 3.3 Architecture constraints

Current Architecture requires:

- PostgreSQL-first durable authority;
- business correctness reconstructible after process/node restart;
- Oban as durable async execution machinery, never business truth;
- queue uniqueness does not replace business idempotency;
- post-commit consequences must be durable where required;
- PubSub/caches/Analytics/telemetry never become business authority;
- audit/security evidence is a separate governed class from ordinary logs;
- sensitive payloads are minimised/redacted;
- privileged/break-glass actions are reasoned, scoped, expiring, evidenced, alerted and reviewable;
- current policy/authority must be revalidated at protected action boundaries;
- restore must recover later deletion/suppression/hold authority before service promotion.

---

# 4. Working evidence criticality model

These labels are **working semantic classes only**. They are not implementation enums, database values or governed identifiers.

## E1 — CAPTURE_REQUIRED_BEFORE_ACCEPTANCE

The protected action or protected data release cannot succeed unless the minimum required durable evidence is successfully accepted at the same protected boundary.

Typical current candidates:

- practitioner access to highly sensitive participant information;
- break-glass activation;
- exceptional privileged access;
- support-assisted privileged recovery or identity correction;
- human high-risk safety override.

## E2 — DURABLE_EVIDENCE_OBLIGATION

The source-domain action may commit independently of central Audit materialisation only when the same acceptance boundary establishes a lossless, durable, idempotent obligation to materialise the required evidence later.

Typical current candidates:

- authoritative payment transition after verified provider evidence;
- entitlement consequence after truthful commercial state;
- ordinary verification/recovery transitions where central Audit is required but is not itself the source authority.

## E3 — TELEMETRY_OR_OPTIONAL_EVIDENCE

Central Audit is not required for correctness. Source-domain evidence and/or governed telemetry is sufficient.

Typical current candidates:

- routine low-risk failed login;
- low-risk technical probes or denials;
- ordinary diagnostic telemetry.

No universal classification matrix is fixed here. Exact event/category classification remains downstream JIT work.

---

# 5. Accepted working decisions

All decisions below were explicitly accepted in the discovery conversation unless marked `CANDIDATE / NOT YET ACCEPTED`.

## AE-WD-001 — Required material evidence is not best-effort

**Status:** ACCEPTED

> Best-effort is not an acceptable semantic contract for evidence that governing law says is materially required.

If a governed event requires material evidence, “business succeeded and maybe we log later” is insufficient.

---

## AE-WD-002 — Fail-closed pre-disclosure evidence for E1 sensitive access

**Status:** ACCEPTED / REFINED

> Before the first protected payload is disclosed, minimum durable evidence of the authorised disclosure attempt must already exist.

This pre-disclosure evidence records the authorised attempt/commencement, **not fictional completion**.

For privileged/highly sensitive access, required evidence failure means protected access fails closed.

---

## AE-WD-003 — Truthful source transition may use durable evidence obligation

**Status:** ACCEPTED

> Where a source Domain must establish truthful business state independently of central Audit availability, the transition may commit only if required Audit evidence is durably accepted with it or a lossless, idempotent evidence obligation is established at the same acceptance boundary.

Volatile or best-effort emission is insufficient.

---

## AE-WD-004 — Sensitive disclosure has pre-disclosure and outcome evidence moments

**Status:** ACCEPTED

For E1 disclosure:

1. pre-disclosure evidence is mandatory and fail-closed;
2. it records authorised attempt/commencement, not completion;
3. outcome evidence is appended when outcome becomes knowable;
4. outcome evidence never rewrites the pre-disclosure record;
5. if outcome evidence cannot materialise synchronously after disclosure, a durable/recoverable obligation must survive restart/retry.

Working criticality:

- pre-disclosure = E1;
- post-disclosure outcome = E2.

---

## AE-WD-005 — Evidence states only what the platform can prove

**Status:** ACCEPTED

> Audit evidence must state only what the platform can actually prove. It must not upgrade technical observations into stronger semantic claims.

Keep distinct:

```text
access requested
≠ access authorised
≠ disclosure initiated
≠ disclosure completed
≠ recipient actually viewed/understood the data
```

---

## AE-WD-006 — No unaudited emergency or break-glass bypass

**Status:** ACCEPTED

> Under current Product Law there is no emergency/break-glass path that bypasses required E1 evidence. Required evidence failure means protected access fails closed.

Any future requirement to permit genuinely life-critical access without successful durable evidence is an **UPSTREAM_PRODUCT** change requiring explicit safety/legal/architecture treatment.

---

## AE-WD-007 — Exactly-once Audit is not the invariant

**Status:** ACCEPTED

> Audit & Evidence does not promise “exactly one record per business event.” It promises that material evidence is not lost, falsely multiplied semantically, silently overwritten, or incorrectly conflated across distinct attempts.

Important separations:

```text
business effect identity
≠ action/disclosure attempt identity
≠ audit evidence record identity
≠ worker/provider delivery attempt identity
```

---

## AE-WD-008 — Business idempotency does not erase material attempts

**Status:** ACCEPTED

> Business idempotency suppresses duplicate business effects; it does not automatically suppress evidence of materially distinct attempts.

A repeated privileged attempt may deserve separate evidence even when the source business effect is already complete.

---

## AE-WD-009 — Evidence materialisation retry is its own idempotency boundary

**Status:** ACCEPTED

> Retrying delivery/materialisation of the same evidence assertion must be idempotent. Retrying the underlying governed action is a separate question.

```text
retry evidence append
≠ retry protected action
```

---

## AE-WD-010 — Deduplicate only demonstrably identical evidence-materialisation retries

**Status:** ACCEPTED

> Evidence deduplication may collapse only demonstrably identical evidence-materialisation retries. It may not collapse distinct governed attempts merely because actor, target, action, source operation or time window match.

---

## AE-WD-011 — Correction/supersession is append-only

**Status:** ACCEPTED

> Append-only does not mean perpetuating known error as current interpretation. Corrections, retractions and supersessions are new immutable evidence linked to earlier evidence; they never destructively rewrite historical records.

The earlier record continues to prove what the platform recorded at the earlier time; later evidence proves the governed correction.

---

## AE-WD-012 — Evidence-authority principle

**Status:** ACCEPTED

> The semantic Domain owns the audited business truth. Audit & Evidence is authoritative only for the existence, provenance, integrity, relation, correction/supersession, access and governed retention state of its own evidence. An Audit record never authorises or reconstructs source-domain business state merely because it describes that state.

---

## AE-WD-013 — Audit stores an evidence envelope, not a source snapshot

**Status:** ACCEPTED

> A central Audit record stores the minimum semantic evidence envelope necessary for accountability, not a copy of the source Domain's business payload.

Typical evidence envelope dimensions:

- actor/executing authority;
- action/attempt;
- governed target/category;
- purpose/scope/authority;
- time;
- result class;
- source operation/causation/correlation;
- reason where required.

---

## AE-WD-014 — Prefer durable references and bounded categorical assertions

**Status:** ACCEPTED

> A central Audit record should prefer durable references and bounded categorical assertions over duplicated source-domain payloads. Copying a source value requires a specific accountability requirement that cannot be satisfied safely by reference or classification alone.

---

## AE-WD-015 — Limited change summary is not before/after snapshotting

**Status:** ACCEPTED

> “Limited change summary” means the minimum semantic description necessary to prove the governed action or outcome. It does not mean automatic before/after payload capture.

Examples:

- `primary_email_changed`
- `changed_fields = [primary_email]`

are conceptually safer than storing full old/new values.

---

## AE-WD-016 — Reason/purpose evidence must minimise free text

**Status:** ACCEPTED

> Where reason/purpose evidence is required, prefer controlled semantic codes plus only the minimum bounded human rationale needed for accountability. Operator free text is not a licence to duplicate sensitive source content into Audit.

---

## AE-WD-017 — Hashes/fingerprints do not automatically make sensitive data safe

**Status:** ACCEPTED

> Hashing/fingerprinting a sensitive business value does not automatically make that value safe Audit metadata or anonymised evidence. A fingerprint may be used only where its precise integrity/correlation purpose is justified and residual linking/re-identification risk is accepted by the applicable privacy/security contract.

---

## AE-WD-018 — Audit access is itself privileged

**Status:** ACCEPTED

> Audit evidence access is privileged, purpose-bound and minimum-necessary. Audit is not a convenient general operator-search database.

Query/access must respect evidence categories and scope.

---

## AE-WD-019 — Audit-of-audit has a semantic stopping rule

**Status:** ACCEPTED

> Material human/system-principal access to, export of, correction of or administrative action over Audit evidence is itself evidence-worthy, but the internal evidence-appending mechanism does not recursively generate evidence about its own normal append operation.

Exceptional direct database access, retention override, integrity repair or administrative export remains evidence-worthy.

---

## AE-WD-020 — Restricted historical accountability linkage may survive ordinary product deletion

**Status:** ACCEPTED

> Where independently authorised retention requires historical accountability, Audit may retain a restricted evidence-specific linkage sufficient for that accountability purpose after ordinary product identity linkage is removed, provided that linkage cannot authenticate, reactivate, reconstruct product authority, or become a general-purpose participant profile.

Exact categories, linkage form and durations remain **EXPERT_LEGAL_PRIVACY** + JIT work.

---

## AE-WD-021 — Immutability does not mean immortality

**Status:** ACCEPTED

> An Audit evidence record is immutable in historical meaning while retained, but remains subject to independently governed retention, legal-hold, deletion/anonymisation and lawful-disposition contracts. Append-only status creates no perpetual-retention authority.

---

## AE-WD-022 — Correction meaning and retention/disposition are orthogonal

**Status:** ACCEPTED

> Correction/supersession state and retention/disposition state are orthogonal. Legal hold, expiry, deletion or anonymisation must not silently change the historical semantic meaning of an evidence record.

---

## AE-WD-023 — Retention governance ownership split

**Status:** ACCEPTED

> Audit & Evidence applies its own evidence-retention contract as the owning Domain; Privacy & Consent supplies the governing retention/hold/deletion authority. Neither acquires the other Domain's durable truth.

---

## AE-WD-024 — Legal hold is scoped and temporary authority over disposition

**Status:** ACCEPTED

> A legal hold prevents otherwise-applicable evidence disposition only within its governed scope and duration. It does not reactivate deleted Account/product authority, broaden evidence access, change source-domain truth, or create permanent retention.

---

## AE-WD-025 — Preserve retention-class provenance

**Status:** ACCEPTED

> Evidence must retain sufficient provenance of its retention classification/basis to explain why it was retained or disposed, while applicability of later policy changes remains governed by the relevant legal/privacy contract rather than inferred automatically.

No exact retention duration is fixed here.

---

## AE-WD-026 — Disposition must be provable without an immortal shadow ledger

**Status:** ACCEPTED

> Evidence disposition must itself be provable at the minimum necessary level, but disposition proof must not reconstruct the expired evidence or create an immortal one-for-one shadow ledger of everything lawfully removed.

Exact representation remains JIT work.

---

## AE-WD-027 — Correction-chain disposition must remain truthful

**Status:** ACCEPTED

> Retention/disposition of linked evidence must preserve truthful interpretability while authorised and must not use correction/supersession relationships as a mechanism for indefinite retention.

Exact chain representation remains **DOMAIN_JIT**.

---

## AE-WD-028 — Do not collapse independent evidence lifecycle dimensions

**Status:** ACCEPTED

> Audit evidence meaning, correction lineage, access state, retention classification and legal-hold/disposition state are independent dimensions and must not be collapsed into one lifecycle merely for implementation convenience.

---

## AE-WD-029 — E2 delayed Audit cannot rewrite source truth

**Status:** ACCEPTED

> For E2 transitions, delayed Audit materialisation never delays, reverses or reinterprets an already-authoritative source-domain transition, provided the required lossless evidence obligation was established at the acceptance boundary.

---

## AE-WD-030 — Arrival order is not authority order

**Status:** ACCEPTED

> Arrival order of evidence is not authority order. Audit records governed observations/decisions relevant to accountability but may not use “latest evidence wins” to reinterpret another Domain's business truth.

---

## AE-WD-031 — Later source correction does not erase historical accountability

**Status:** ACCEPTED

> A later source-domain correction may supersede the current interpretation of a prior source fact without falsifying the historical fact that the platform possessed, evaluated or acted upon the earlier assertion at that time. Audit preserves that historical accountability without retaining authority for the superseded source truth.

---

## AE-WD-032 — Audit references may become non-resolvable

**Status:** ACCEPTED

> An Audit reference may lawfully become non-resolvable after source-domain disposition. Evidence retention does not create an obligation or authority to preserve or reconstruct the referenced source record.

---

## AE-WD-033 — Audit references do not extend source/provider retention

**Status:** ACCEPTED

> A central Audit reference does not impose indefinite retention on referenced source/provider evidence. Each owner applies its own lawful retention contract.

---

## AE-WD-034 — Audit corrects evidence, not source business truth

**Status:** ACCEPTED

> Audit & Evidence may authoritatively correct its own evidence metadata/provenance under a governed correction process. It may not independently correct the semantic Domain's business outcome; source-truth corrections require authoritative source-domain evidence/command first.

---

## AE-WD-035 — Reconstructed evidence must disclose recovery provenance

**Status:** ACCEPTED

> Audit recovery may reconcile missing evidence from surviving authorised source provenance, but reconstructed evidence must preserve its recovery provenance and may never masquerade as original contemporaneous capture.

---

## AE-WD-036 — Audit may trigger reconciliation but never restore source truth directly

**Status:** ACCEPTED

> Audit evidence may trigger source-owner reconciliation, but may never directly recreate or mutate missing source-domain business state after restore.

---

## AE-WD-037 — Historical gaps and current E1 viability are different questions

**Status:** ACCEPTED

> A bounded historical Audit gap does not automatically prohibit unrelated future E1 activity once current evidence integrity/durability is established. An unresolved condition that prevents trustworthy current evidence capture does prohibit E1 activity.

Exact RPO/RTO and disaster-loss envelopes remain separate DR/release governance.

---

# 6. Accepted mechanism-routing decision

## AE-MECH-001 — Ash Temporal Resources are a JIT-time candidate only

**Status:** ACCEPTED

> Ash Temporal Resources are a JIT-time implementation candidate only. Pre-JIT establishes temporal/evidence semantics without requiring Ash Temporal. Selection requires then-current stable ecosystem verification, proof that the mechanism fits the Audit lifecycle, and confirmation that its PostgreSQL/platform requirements do not silently amend Architecture.

Primary bucket: `DOMAIN_JIT`.

Conditional escalation: `UPSTREAM_ARCHITECTURE` if adoption requires an infrastructure/database/platform baseline change outside current authority.

Current working preference:

- **do not assume Temporal Resources for the core Audit evidence ledger;**
- the emerging model is multiple independently meaningful immutable assertions (`R1`, `R2`, `R3`) rather than versions of one logical row;
- plain append-only Resources may therefore be semantically simpler;
- Temporal Resources may still fit a concrete temporal concept if later JIT demonstrates an independent invariant requiring `as_of` semantics;
- the final decision belongs in the applicable Phase 7B Domain JIT, not this Pre-JIT.

Current ecosystem observations are **evidence snapshots, not pins or architecture law**, and must be re-verified at JIT time.

---

# 7. Accepted pressure-test results

## PT-001 — Evidence criticality / acceptance boundary

### Ordinary email verification succeeds; central Audit temporarily unavailable

Working result: **E2 likely**.

Identity owns verification truth. Central Audit does not become verification authority.

### Password reset/recovery completion

Working result: **E2 normally**, with exceptional manual/high-risk recovery potentially E1.

### Privileged grant/revoke

Working result: E1 or strong E2 depending on exact governed action. Needs JIT category classification.

### Break-glass activation

Working result: **E1 candidate / current preferred treatment**.

### Practitioner opens highly sensitive participant record

Working result: **E1**.

Required durable pre-disclosure evidence must exist before protected bytes leave the boundary.

### Support performs privileged recovery/identity correction

Working result: **E1 candidate**.

### Automated safety/eligibility decision

Working result: source-domain evidence required; central Audit may be E2/E3 depending on materiality. Safety remains decision/provenance authority.

### Human safety override

Working result: **E1 candidate**.

### Verified payment becomes authoritative

Working result: **E2**.

Commerce truthful state must not be denied merely because central Audit materialisation is delayed.

### Entitlement grant following truthful payment

Working result: **E2**.

Entitlements remains access authority.

### Routine failed login

Working result: **E3 normally**.

### High-risk credential-stuffing/security outcome

Working result: central governed evidence candidate, exact class deferred.

---

## PT-002 — Sensitive disclosure failure semantics

### Audit fails before protected bytes leave

Result: **deny access**.

### Audit succeeds; protected read fails before bytes leave

Result: preserve the pre-disclosure attempt; append failure/aborted outcome where knowable.

### Audit succeeds; partial stream leaves then process/network dies

Result: pre-disclosure record remains truthful; later outcome may be `partial`, `aborted` or `unknown` depending on provable facts.

### Full data returns; final outcome evidence initially fails

Result: disclosure cannot be undone; durable outcome-evidence obligation must survive restart/retry.

### Client retries uncertain request

Result: do not blindly collapse the next request into the first attempt. A second real disclosure may occur.

### Consent revoked during long-running stream/export

Result: requires explicit long-lived-access/revalidation contract; point-in-time semantics may be insufficient.

Primary bucket: `CROSS_DOMAIN_JIT`.

---

## PT-003 — Duplicate/retry/exactly-once illusion

### Two privileged reads of same record

Result: two genuine disclosures may lawfully produce two distinct attempts/evidence chains.

### Same evidence append retried after uncertain acknowledgement

Result: materialisation is idempotent; it must not fabricate a second governed action.

### Double-click on one business transition

Result: source-domain idempotency suppresses duplicate business effect; material attempts may still be evidenced if category requires.

### Two concurrent tabs

Result: two disclosures are possible; generic uniqueness such as `(actor, target, action, day)` is unsafe.

---

## PT-004 — Correction/supersession

### Wrong actor recorded

Result:

- original immutable evidence remains;
- governed correction appends a new linked assertion;
- current interpretation follows correction/supersession lineage;
- historical record is not destructively rewritten.

### Source business interpretation changes

Result: source Domain owns correction; Audit records that correction/reconciliation occurred but does not independently change source truth.

---

## PT-005 — Minimisation and shadow-store prevention

### Health/private payload

Result: central Audit normally stores reference/category + action/scope/result, not the underlying health payload.

### Communications delivery

Result: Communications keeps provider/delivery business evidence; central Audit gets minimum restricted accountability evidence only.

### Credentials/tokens/secret URLs

Result: never copy into central Audit.

### Before/after snapshots

Result: prohibited as a generic audit pattern. Use bounded semantic change summary unless a separately justified accountability requirement demands a value.

### Free-text operator reason

Result: prefer controlled codes and bounded rationale; do not create a sensitive-data dump channel.

### Hash/fingerprint

Result: not automatically anonymous or safe.

---

## PT-006 — Retention / expiry / lawful disposition

### Retention expires; no hold/obligation

Result: evidence becomes eligible for governed disposition despite append-only semantics.

### Full Deletion; separate evidence retention basis exists

Result: retained evidence may survive only under its independent basis, minimised/restricted/non-reconstructive.

### Full Deletion; no independent retention basis remains

Result: “append-only” does not justify indefinite identifiable retention.

### Legal hold before destructive commit

Result: applicable disposition pauses in scope.

### Hold after already-completed lawful disposition

Result: evidence is not reconstructed merely because a later hold appears.

### Wrong retention class

Result: correct/supersede retention metadata with provenance; do not rewrite audited event meaning.

### Restore from backup predating evidence disposal

Result: current suppression/disposition/hold authority must be recovered before promotion.

---

## PT-007 — Cross-domain contradiction / delayed evidence / disaster recovery

### Commerce commits truthful payment; Audit delayed

Result: payment remains Commerce truth; lossless evidence obligation must materialise later.

### Provider evidence arrives out of order

Result: arrival order is not authority order. Commerce reconciles; Audit does not interpret payment from latest arrival.

### Health/Safety source corrected later

Result: preserve historical fact that platform acted on earlier assertion while current Health/Safety authority follows the correction.

### Source record later deleted/anonymised

Result: retained Audit reference may become non-resolvable; Audit does not reconstruct source data.

### Audit restored behind source Domain

Result: source truth remains source truth; missing evidence becomes reconciliation/integrity issue. Any reconstructed evidence discloses recovery provenance.

### Audit restored ahead of source Domain

Result: Audit cannot replay source state. It may trigger source-owner reconciliation only.

### Bounded historical evidence gap

Result: does not necessarily stop unrelated future E1 activity after current capture integrity is re-established.

---

# 8. Working data-shape doctrine

This section is semantic only and does not authorise fields/schema.

A central evidence record may need to represent concepts such as:

- evidence-record identity;
- event/category;
- source Domain;
- source operation reference;
- attempt reference;
- actor/executing-authority reference;
- target reference/category;
- purpose/scope/reason code;
- outcome/result class;
- occurrence/acceptance time;
- causal/correlation references;
- correction/supersession relation;
- evidence capture/recovery provenance;
- retention-class/basis metadata;
- restricted access classification.

This is **not** a final Resource schema.

Prohibited generic payload behaviour includes:

- full source-domain snapshots;
- passwords;
- bearer tokens;
- raw secrets;
- rendered secret URLs;
- full communications bodies;
- raw provider payloads copied centrally by default;
- health/private payload duplication;
- generic before/after record serialization;
- unrestricted operator free-text dumping;
- deterministic sensitive fingerprints without justified purpose/risk review.

---

# 9. Unresolved issues and primary bucket

Exactly one primary bucket is assigned to each unresolved issue.

| Issue | Primary bucket | Current working position |
|---|---|---|
| Exact event/category matrix for E1/E2/E3 | `DOMAIN_JIT` | Pre-JIT defines classes; JIT maps concrete events. |
| Exact evidence Resource(s), field names, indexes, constraints | `DOMAIN_JIT` | Deferred. |
| Evidence assertion identity vs material attempt identity representation | `DOMAIN_JIT` | Semantics accepted; representation deferred. |
| Correction/supersession chain representation | `DOMAIN_JIT` | Must remain append-only and truthful. |
| Chain-coherent retention/disposition representation | `DOMAIN_JIT` | Must not create indefinite retention. |
| Audit query/access permission representation | `DOMAIN_JIT` | Must be purpose/scope/category restricted. |
| Cross-domain acceptance boundary for each material action | `CROSS_DOMAIN_JIT` | E1/E2/E3 model established; concrete mapping pending. |
| Long-running disclosure/export revalidation | `CROSS_DOMAIN_JIT` | Needs explicit contract. |
| Source-reference design per Domain | `CROSS_DOMAIN_JIT` | Prefer references/minimum categorical evidence. |
| Exact retention durations | `EXPERT_LEGAL_PRIVACY` | Do not invent in JIT. |
| Exact post-deletion historical linkage form | `EXPERT_LEGAL_PRIVACY` | Must remain non-reconstructive. |
| Retroactive effect of retention-policy changes | `EXPERT_LEGAL_PRIVACY` | Policy/legal decision. |
| Category-specific deletion/anonymisation treatment | `EXPERT_LEGAL_PRIVACY` | Align with Privacy + OQ-009/OQ-029/OQ-033. |
| Leakage/redaction/query-scope proof | `IMPLEMENTATION_PROOF` | Required later. |
| Evidence retry/concurrency proof | `IMPLEMENTATION_PROOF` | Required later. |
| Crash/restart/reconciliation proof | `IMPLEMENTATION_PROOF` | Required later. |
| Backup/restore evidence-gap proof | `IMPLEMENTATION_PROOF` | Required later. |
| Exact RPO/RTO / acceptable disaster-loss envelope | `RELEASE_ONLY` | Governed by DR/release readiness, not this Pre-JIT. |
| Incident operational ownership / OQ-038 | `RELEASE_ONLY` | Do not pull forward without new need. |
| Provider-specific empirical behaviour affecting source evidence | `PROVIDER_EMPIRICAL` | Owner Domain validates; Audit does not infer. |
| Future life-critical unaudited emergency access | `UPSTREAM_PRODUCT` | Not allowed under current law; requires explicit future amendment. |
| Ash Temporal Resources selection | `DOMAIN_JIT` | Candidate only. |
| Ash Temporal requiring architecture/platform baseline change | `UPSTREAM_ARCHITECTURE` | Escalate only if selection would amend current architecture. |

No confirmed `UPSTREAM_PRODUCT`, `UPSTREAM_ARCHITECTURE` or Domain-law contradiction has been found in the current discovery stream, except the **conditional future** emergency-access case and the **conditional** mechanism escalation noted above.

---

# 10. FP-001 Audit dossier adjudication — NOT YET FINAL

Current FP-001 state:

- Identity & Access dossier: COMPLETE / CERTIFIED / CURRENT.
- Communications dossier: COMPLETE / CERTIFIED / CURRENT.
- Communications finalisation remains BLOCKED / STOP pending applicable gates and conditional-dossier adjudication.
- Privacy & Consent: CONDITIONAL / pending explicit adjudication.
- Content & Media: CONDITIONAL / pending explicit adjudication.
- Audit & Evidence: CONDITIONAL / pending explicit adjudication.
- Analytics: NOT REQUIRED.
- Phase 7C: BLOCKED / NOT STARTED.
- Phase 8 application implementation: UNAUTHORISED.

Required eventual adjudication:

- `REQUIRED`
- `NOT_REQUIRED`
- `REQUIRED_ONLY_IF <condition>`

Final test:

> **Can Phase 7C state the complete implementation-grade FP-001 Audit/Evidence contract without inventing new Audit Domain semantics?**

This question remains open until the discovery grill is complete.

---

# 11. Pass 7 — Audit security, tamper resistance and operator abuse

**Status:** ACCEPTED 2026-10-08.

This pass pressure-tested the Audit system itself as a high-value target. It deliberately avoids prematurely selecting cryptographic, WORM or specialist infrastructure while fixing the semantic integrity and access boundaries that any later implementation must satisfy.

## `AE-WD-038` — Semantic immutability is not physical immobility

> **Audit evidence meaning is immutable while lawfully retained, but its physical storage representation may change through governed maintenance provided evidence identity, meaning, provenance, integrity and applicable retention constraints remain preserved.**

Examples of potentially legitimate physical change include encryption-key rotation, database migration, partition movement, storage-format migration, backup/restore and compression. These are not evidence correction when semantic meaning remains unchanged.

Primary bucket: `DOMAIN_JIT` / `IMPLEMENTATION_PROOF`.

## `AE-WD-039` — Tamper-resistant means no silent historical rewrite

> **Ordinary application, support, staff and administrative authority must not be able to silently edit or replace retained Audit history. Legitimate correction uses append-only correction/supersession; legitimate retention disposition uses the governed disposition path.**

Keep distinct:

```text
correction
≠ lawful disposition
≠ unauthorised tampering
```

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-040` — Audit administrator is not a universal super-admin

> **Administrative authority over Audit infrastructure does not confer source-domain business authority or unrestricted evidence access. Audit capabilities remain explicit, scoped and purpose-bound.**

Audit administration must not automatically grant Health, Commerce, Identity or unrestricted participant authority.

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-041` — Separate dangerous Audit capabilities

> **Read, bulk-query/export, correction/supersession, retention/hold administration and exceptional infrastructure access are distinct capabilities. Ordinary support/admin authority must not implicitly include them, and no ordinary role may suppress evidence of its own governed actions.**

Exact two-person approval or separation-of-duty requirements remain later category/security/operations decisions unless existing higher authority already mandates them.

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-042` — Material Audit access is itself an evidence boundary

> **Material human access to Audit evidence—especially bulk, cross-participant, high-sensitivity or export access—is itself a governed disclosure and must establish required evidence before the protected Audit payload is released.**

High-risk/bulk Audit access is an E1 candidate. Exact lower-risk query categories remain risk/JIT work rather than creating permanent audit for every trivial lookup.

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-043` — Audit exports are temporary protected derivatives

> **A material Audit export is a purpose-scoped protected derivative, not new evidence authority. Its creation, access, delivery, expiry and disposal must be governed, and it must not become an indefinite shadow copy of the Audit ledger.**

This is an Audit operational export, distinct from participant data-rights export owned/orchestrated under Privacy & Consent.

Primary bucket: `DOMAIN_JIT` / `IMPLEMENTATION_PROOF`.

## `AE-WD-044` — Exceptional bypass paths are part of the threat model

> **Tamper-resistance proof must cover authorised application paths and exceptional infrastructure/database administration paths. A control that protects only normal application actions is insufficient evidence that retained Audit history cannot be silently rewritten.**

Future proof must deliberately cover direct database/infrastructure privileges, exceptional maintenance authorisation, mutation detectability and the risk of one principal both altering evidence and suppressing all evidence of that alteration.

Primary bucket: `IMPLEMENTATION_PROOF`.

## `AE-WD-045` — No infinite meta-audit chain

> **Audit integrity requires a deliberate trust boundary and evidence against material tampering, but not recursively auditing each evidence system with another evidence system forever. The future design must identify the final trusted operational/infrastructure boundary explicitly.**

Primary bucket: `DOMAIN_JIT` / `IMPLEMENTATION_PROOF`.

## `AE-MECH-002` — Cryptographic/WORM integrity mechanisms remain JIT candidates

> **Hash chains, signatures, Merkle structures, WORM/object-lock storage, dedicated append-only services and similar mechanisms are implementation candidates only. None is required by Pre-JIT unless future threat analysis proves that simpler PostgreSQL/Ash controls cannot satisfy the tamper-resistance contract.**

Any selected mechanism must remain compatible with lawful retention/disposition, correction/supersession, backup/restore and disaster recovery. Specialist infrastructure is not introduced by fashion.

Primary bucket: `DOMAIN_JIT`, conditional `UPSTREAM_ARCHITECTURE` if selection introduces a new material infrastructure/platform requirement.

## `AE-WD-046` — Confidentiality and integrity are separate

> **Encryption/key protection does not by itself satisfy evidence integrity or tamper-resistance. Audit confidentiality, integrity, availability and provenance are distinct concerns and must not be collapsed into one mechanism.**

Key rotation/re-encryption may change bytes without changing evidence semantics.

Primary bucket: `DOMAIN_JIT` / `IMPLEMENTATION_PROOF`.

## `AE-WD-047` — Security incident does not rewrite evidence history

> **Compromise of an Audit protection mechanism changes security/integrity assurance and triggers governed incident/recovery consequences; it does not change the historical semantic meaning of the underlying evidence records.**

Exact KMS/HSM/provider mechanisms remain implementation/security work.

Primary bucket: `IMPLEMENTATION_PROOF` / `RELEASE_ONLY` where incident operations are the unresolved concern.

## `AE-WD-048` — Current integrity failure versus historical integrity incident

> **If current required evidence cannot be captured with sufficient integrity, E1 actions fail closed. A bounded historical integrity anomaly becomes an explicit incident/reconciliation problem and does not automatically halt unrelated future E1 operations once current capture integrity is established.**

Primary bucket: `DOMAIN_JIT` / `IMPLEMENTATION_PROOF`.

## `AE-WD-049` — Authorised disposition must be distinguishable from tampering

> **The integrity model must distinguish governed evidence disposition from unauthorised disappearance or mutation without retaining an immortal copy of every disposed record.**

This refines `AE-WD-026` rather than replacing it.

Primary bucket: `DOMAIN_JIT` / `IMPLEMENTATION_PROOF`.

## `AE-WD-050` — Evidence correction is itself a high-risk governed action

> **Correction/supersession of Audit evidence is itself a material privileged action with durable provenance. Correction authority may change the current interpretation of Audit-owned evidence metadata but cannot erase the original assertion or silently become source-domain correction authority.**

Working criticality: E1.

Primary bucket: `DOMAIN_JIT`.

## Pass 7 pressure-test outcomes

| Scenario | Accepted working outcome | Primary bucket |
|---|---|---|
| Support/admin tries to delete evidence of own action | Prohibited; ordinary role cannot suppress own governed evidence | `DOMAIN_JIT` |
| Audit reader requests bulk export | High-risk governed disclosure; E1 candidate | `DOMAIN_JIT` |
| Operator wants to fix original Audit row | Prohibited; append governed correction/supersession | `DOMAIN_JIT` |
| DBA/infrastructure path bypasses Ash | Must be inside integrity/threat model and proof | `IMPLEMENTATION_PROOF` |
| Encryption key rotates | Physical representation change, not evidence correction | `IMPLEMENTATION_PROOF` |
| Protection key compromised | Security incident/recovery; history meaning unchanged | `IMPLEMENTATION_PROOF` |
| Hash chain or WORM suggested | Candidate only; retention/deletion compatibility required | `DOMAIN_JIT` |
| Old bounded segment fails integrity verification | Incident/reconciliation; future E1 can resume once current capture proven trustworthy | `IMPLEMENTATION_PROOF` |
| Current Audit integrity/durability uncertain | E1 fails closed | `DOMAIN_JIT` |
| Governed retention disposes evidence | Valid disposition, not tampering | `DOMAIN_JIT` |
| Malicious or false correction appended | Original preserved; correction has its own provenance/review boundary | `DOMAIN_JIT` |

---

# 12. Next pressure-test queue

The next planned pass is:

## Pass 8 — FP-001 Audit/Evidence event matrix and dossier adjudication pressure

Build a concrete FP-001 matrix across the current Identity & Access and Communications contracts. For each candidate event determine:

- semantic owner;
- whether central Audit evidence is actually required;
- E1 / E2 / E3 working criticality where applicable;
- minimum evidence envelope;
- prohibited Audit payload;
- source-operation / attempt / evidence identity relationship;
- retention/access category questions;
- whether the contract can be stated without inventing new Audit Domain semantics.

At minimum pressure-test:

- registration and Account creation;
- email verification proof consumption;
- password authentication and material denial classes;
- password reset/recovery completion and exceptional/manual recovery;
- MFA enrol/reset where applicable;
- primary-email change requested/confirmed/applied/cancelled/superseded;
- session/device revocation and compromise response;
- role/grant creation/revocation/elevation;
- break-glass activation/use/review;
- support-assisted identity/recovery/reconciliation actions;
- duplicate-account reconciliation/conflict;
- Communications privileged delivery-side actions;
- provider/delivery evidence boundary;
- material Audit query/access where FP-001 operations require it.

Then re-run the FP-001 conditional dossier test:

> **Can Phase 7C state the complete implementation-grade FP-001 Audit/Evidence contract without inventing new Audit Domain semantics?**

Later passes still required if the FP-001 matrix exposes them:

- FLOW-01 / FLOW-08 cross-stream reconciliation;
- final unresolved-bucket audit;
- FP-001 dossier adjudication;
- final compact Pre-JIT working pack.

---

# 13. Change ledger

## v0.1.0 — 2026-10-08

Initial materialisation of the Audit & Evidence Pre-JIT discovery stream.

Captured:

- current authority baseline;
- Domain/Architecture boundary;
- E1/E2/E3 criticality model;
- accepted `AE-WD-001` through `AE-WD-037`;
- accepted `AE-MECH-001`;
- pressure-test results PT-001 through PT-007;
- unresolved issue routing;
- FP-001 dossier adjudication status;
- next pressure-test queue.

No Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority is amended by this file.

## v0.2.0 — 2026-10-08

Cumulative append-only successor. Preserves v0.1.0 semantics and adds accepted Pass 7 security/integrity doctrine.

Added:

- accepted `AE-WD-038` through `AE-WD-050`;
- accepted `AE-MECH-002`;
- explicit distinction between semantic immutability and physical storage changes;
- scoped Audit administration/access/export/correction boundaries;
- direct database/infrastructure paths inside tamper-resistance proof;
- no infinite meta-audit chain;
- encryption/confidentiality separated from integrity;
- current-integrity failure versus bounded historical incident distinction;
- authorised-disposition versus tampering distinction;
- Pass 8 FP-001 event-matrix queue.

No prior accepted discovery decision is silently removed or rewritten. No Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority is amended by this file.

---

# 14. Pass 8 — FP-001 event/evidence matrix

## Pass objective

Test the current Phase 7A conditional rule for Audit & Evidence:

> **Can Phase 7C state the complete implementation-grade FP-001 Audit/Evidence contract without inventing new Audit Domain semantics?**

Current Phase 7A keeps Audit & Evidence `CONDITIONAL` and says a dossier becomes necessary if exact FP-001 evidence-event, minimisation, access or retention contracts cannot be stated without invention.

## FP-001 working matrix

| FP-001 action / event | Source authority | Central Audit working requirement | Working criticality | Accepted working reasoning |
|---|---|---|---|---|
| Successful Account creation + canonical PMR assignment | Identity & Access | YES | E2 | Identity truth must commit truthfully; same acceptance boundary establishes required evidence or a lossless evidence obligation |
| Failed/aborted registration before Account exists | Identity & Access | Usually NO central Audit unless material security/abuse outcome | E3 | Do not permanently audit every validation failure |
| Email verification proof successfully consumed | Identity & Access | YES | E2 | Verification remains Identity truth; Audit records accountability only |
| Expired/invalid ordinary verification proof | Identity & Access | Usually source security evidence / telemetry | E3 | Routine denial does not justify permanent central evidence |
| High-risk/replay/abuse verification denial | Identity & Access | YES when material security outcome | E2/E3 category boundary | Risk-based central evidence |
| Ordinary sign-in success | Identity & Access | Not automatically permanent central Audit | E3 | Session/auth source evidence and telemetry normally suffice |
| Ordinary failed password attempt | Identity & Access | Not automatically permanent central Audit | E3 | Avoid turning Audit into authentication telemetry |
| High-risk authentication/security decision | Identity & Access | YES where material category requires | E2 | Material security evidence |
| Participant self-service password change | Identity & Access | YES | E2 | Security change remains Identity-owned |
| Ordinary automated recovery completion | Identity & Access | YES | E2 | Recovery truth remains Identity-owned; durable evidence consequence required |
| Manual/exception recovery approval/completion | Identity & Access | YES | E1 | Exceptional human authority must be evidenced before authority-changing action completes |
| Security hold placement / forced restriction | Identity & Access | YES | E2 | Security narrowing must not be blocked by Audit outage |
| Security hold release by privileged actor | Identity & Access | YES | E1 | Re-enables authority through exceptional human action |
| MFA enrol/disable/reset for ordinary participant where applicable | Identity & Access | YES for material transition | Usually E2 | Identity security truth remains source-owned |
| Privileged/manual MFA reset | Identity & Access | YES | E1 | Exceptional security authority |
| Primary-email-change requested | Identity & Access | YES | E2 | Historical operation evidence is Audit-owned; current operation remains Account truth |
| Primary-email-change confirmation | Identity & Access | YES | E2 | Proof consumption/source operation remains Identity authority |
| Primary-email-change applied | Identity & Access | YES | E2 | Security-sensitive transition; no raw old/new email duplication by default |
| Primary-email-change cancelled/expired/superseded | Identity & Access | YES | E2 | Historical lifecycle evidence preserved without rewrite |
| Individual/global session revocation | Identity & Access | YES when material security action | E2 | Revocation must remain possible during Audit disturbance |
| Device assurance revocation/security invalidation | Identity & Access | YES when material | E2 | Same security-narrowing rule |
| Scoped ordinary grant activation | Identity & Access | YES | E1 where it expands privileged human authority | Evidence before exceptional authority becomes usable |
| Grant revocation/expiry | Identity & Access | YES | E2 | Narrowing/removal cannot be held hostage by Audit |
| Privileged elevation | Identity & Access | YES | E1 | Exceptional human authority activation |
| Break-glass activation | Identity & Access | YES | E1 | No unaudited emergency path |
| Break-glass protected use | Source action + Identity authority | YES | E1 before protected consequence | Activation evidence alone is not proof of later protected use |
| Break-glass expiry/revocation | Identity & Access | YES | E2 | Restrictive transition |
| Break-glass review result | Identity/governance owner | YES | E2 | Historical review evidence; original use remains immutable history |
| Ordinary low-risk support lookup | Relevant source owner | Risk/category dependent | Normally E3 | No permanent audit solely because a benign operator screen was viewed |
| Support-assisted credential/security/recovery correction | Identity & Access | YES | E1 where privileged human authority changes identity/security | Named actor/reason before protected effect |
| Duplicate-account candidate identified | Identity & Access | Source evidence; central Audit only if material review/security event | E2/E3 | Candidate alone changes no canonical identity |
| Human-applied duplicate reconciliation | Identity & Access | YES | E1 | Material privileged canonical-lineage decision |
| Reconciliation rejected/conflicted/corrected | Identity + Audit evidence relation | YES where material | E2 | Preserve provenance; correction never overwrites |
| Ordinary verification/recovery delivery attempt | Communications | NO duplicate central delivery ledger | Source-owned / E3 centrally | Communications owns attempt/retry/provider evidence |
| Provider accepted/delivered/failed callback | Communications | NO raw duplicate in Audit by default | Source-owned | Provider observations remain Communications evidence |
| Privileged delivery-side action | Communications | YES where accountability required | E1 if protected delivery authority changes; otherwise category-specific E2 | Minimum actor/reason/result/safe correlation only |
| Narrow authorised Audit lookup | Audit & Evidence | Risk/category dependent | E2/E3 | Evidence access itself can be sensitive |
| Bulk/high-sensitivity Audit query/export | Audit & Evidence | YES | E1 | Protected Audit payload must not be released before required access evidence exists |

## `AE-WD-051` — FP-001 does not audit everything

> **FP-001 central Audit capture is event/risk-specific. Routine authentication attempts, ordinary validation failures, delivery attempts and provider observations do not become permanent central Audit evidence merely because they are operationally observable.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-052` — FP-001 source transition default

> **Where an FP-001 source-domain transition must remain truthful independently of central Audit availability, required central evidence uses E2: the source transition may commit only when the same acceptance boundary establishes either the required evidence or a lossless idempotent evidence obligation.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-053` — Security narrowing cannot be blocked

> **A security-narrowing action such as session revocation, grant revocation, device invalidation or security-hold placement must not be prevented merely because central Audit materialisation is unavailable. Its acceptance boundary must instead establish a lossless E2 evidence obligation.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-054` — Privilege broadening is asymmetric

> **Activation or restoration of exceptional human authority is E1; narrowing or revoking that authority is E2.**

Working examples:

```text
grant/elevation activation       -> E1
break-glass activation           -> E1
manual privileged recovery       -> E1
security-hold release            -> E1

grant revocation                 -> E2
break-glass revocation/expiry    -> E2
session revocation               -> E2
security-hold placement          -> E2
```

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-055` — Routine authentication is not an immortal Audit stream

> **Ordinary successful logins and routine failed authentication attempts are not automatically permanent central Audit events. Material security outcomes, privileged/high-risk authentication events and governed abuse decisions may require central evidence according to the risk matrix.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-056` — Primary-email-change evidence

> **FP-001 primary-email-change requested, confirmed, applied, cancelled and superseded outcomes require linked historical Audit evidence, while current email-change truth remains Identity-owned. Audit normally records change category, operation/reference, actor/authority, result and correlation rather than copying old/new email addresses.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-057` — Duplicate reconciliation distinction

> **A duplicate-account candidate or conflict is not equivalent to an applied reconciliation. Material human application/correction of canonical identity reconciliation is an E1 privileged action; the canonical reconciliation truth and PMR consequences remain Identity-owned.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-058` — Communications evidence boundary

> **Ordinary Communications delivery attempts, retries, provider observations and reconciliation remain Communications-owned evidence and do not create a duplicate central Audit ledger. Central Audit captures only the minimum accountability evidence required for material privileged/security delivery actions.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-059` — FP-001 Audit access boundary

> **FP-001 operator access to Audit evidence is separately governed from the underlying support permission. Bulk/high-sensitivity evidence access is E1; narrow evidence lookup remains category/risk-specific and grants no source-domain business authority.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WH-001` — Provisional FP-001 dossier adjudication hypothesis

Current working hypothesis after the event/evidence matrix:

> **FP-001 Audit & Evidence JIT Domain Dossier -> REQUIRED.**

Reason:

- FP-001 creates Audit-owned durable evidence truth with its own event-selection semantics;
- E1 versus E2 acceptance behaviour is not owned completely by Identity or Communications;
- privilege-broadening versus security-narrowing asymmetry must be explicit;
- Audit-owned minimisation, access, correction/supersession, evidence-materialisation idempotency and retention-class binding remain required;
- Phase 7C would otherwise have to invent those Domain semantics.

This remains a hypothesis until the FLOW-01 end-to-end failure/race attack is completed.

Primary bucket: `DOMAIN_JIT`.

---

# 15. Next pressure-test queue

## Pass 9 — FLOW-01 end-to-end failure/race attack

Pressure-test:

```text
registration
-> Account creation / PMR assignment
-> verification intent and delivery
-> proof consumption
-> login/session
-> recovery
-> controlled support/admin action
```

Across at least:

- Audit unavailable before E1;
- Audit materialisation delayed after E2;
- process crash after source commit but before materialised evidence;
- process crash after evidence admission but before source commit;
- duplicate HTTP requests;
- duplicate evidence materialisation retry;
- duplicated/reordered Communications provider callbacks;
- proof replay;
- concurrent recovery and email/security changes;
- security revocation while Audit materialisation is delayed;
- privilege activation while Audit unavailable;
- source correction after evidence capture;
- Audit restore behind source authority;
- Audit restore ahead of source authority.

Pass 9 must decide whether `AE-WH-001` survives.

---

# 16. Change ledger addition

## v0.3.0 — 2026-10-08

Cumulative append-only successor. Preserves v0.2.0 semantics and adds accepted Pass 8 FP-001 event/evidence doctrine.

Added:

- FP-001 event/evidence matrix;
- accepted `AE-WD-051` through `AE-WD-059`;
- explicit E1/E2 asymmetry for privilege broadening versus security narrowing;
- explicit Communications non-duplication boundary;
- explicit primary-email-change and duplicate-reconciliation Audit boundaries;
- provisional `AE-WH-001`: FP-001 Audit & Evidence JIT Domain Dossier `REQUIRED`;
- Pass 9 FLOW-01 failure/race attack queue.

No prior accepted discovery decision is silently removed or rewritten. No Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority is amended by this file.

---

# 17. Pass 9 — FLOW-01 end-to-end failure/race attack

## Pass objective

Attack the FP-001 Audit/Evidence contract through the full trusted-entry path:

```text
registration
-> Account creation / PMR assignment
-> verification intent and delivery
-> proof consumption
-> login/session
-> recovery
-> controlled support/admin action
```

Pressure includes crashes, retries, duplicate requests, provider reorder, replay, concurrency, Audit outages and restore divergence.

## `AE-WD-060` — E2 acceptance atomicity

> **An E2 source transition and the durable obligation that guarantees its required Audit evidence form one acceptance boundary: either the source transition plus evidence obligation become durable together, or the governed transition does not commit. Materialisation of the Audit record may occur later.**

This rule does not prescribe an outbox Resource or implementation pattern.

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-061` — E1 pre-effect evidence must not claim completion

> **For an E1 state-changing action, the evidence required before the protected effect records the authorised attempt/admission and its actor, authority, scope/reason and causal identity. It must not claim the business effect completed before the owning Domain commits that effect.**

Linked outcome evidence follows when the source result is known.

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-062` — Failed E1 attempts remain truthful history

> **Once an E1 privileged attempt/admission has been durably evidenced, later source-domain failure, guard rejection or rollback does not erase that evidence. A linked outcome records failure/abort/unknown as actually established.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-063` — Audit never repairs broken source atomicity

> **Audit evidence requirements do not compensate for a source Domain whose own authoritative transition is non-atomic or internally inconsistent. Proof consumption, verification state, recovery completion and similar owner-local invariants remain the owning Domain's responsibility.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-064` — Audit ordering is not source concurrency ordering

> **Evidence insertion order, event timestamp order and worker-delivery order do not resolve source-domain concurrency. The owning Domain determines the authoritative outcome; Audit records the resulting attempt/outcome relationships and causal provenance.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## FLOW-01 pressure outcomes

| Scenario | Accepted working result |
|---|---|
| Account/PMR source commit + Audit materialisation delayed | Safe only if required E2 evidence obligation is durably established in same acceptance boundary |
| Source commits + only volatile Audit emission exists | Rejected; evidence-loss window is semantically invalid |
| E1 admission durable + source action later fails | Admission remains truthful; append linked failure/abort/unknown outcome |
| Duplicate registration HTTP request | Source business idempotency suppresses duplicate Account/PMR effect; same evidence assertion materialisation remains replay-safe |
| Audit insert commits but acknowledgement is lost | Retrying same evidence assertion must be idempotent |
| Duplicate/reordered provider delivery callbacks | Communications reconciles them; central Audit does not mirror provider ledger |
| Verification proof replay | Identity prevents second effect; ordinary denial is not necessarily permanent central Audit |
| Crash during Identity proof consumption/verification transition | Identity must maintain its own atomicity; Audit does not repair it |
| Concurrent recovery and email/security change | Identity resolves concurrency; Audit arrival/insertion order never decides source truth |
| Security revocation while Audit materialisation delayed | Revocation commits with E2 obligation; security narrowing is not blocked |
| Privilege activation while Audit unavailable | E1 cannot be established; activation fails closed |
| E1 admission exists, process crashes before source effect | Admission remains; recovery reconciles source outcome and appends outcome evidence |
| Ordinary login while central Audit materialisation is unavailable | Central Audit outage does not universally block ordinary login |
| Source correction after evidence capture | Source Domain corrects source truth; Audit appends linked evidence correction where required |
| Audit restored behind source authority | Source remains authoritative; reconcile evidence gap with explicit recovery provenance where possible |
| Audit restored ahead of source authority | Audit triggers source-owner reconciliation only; never recreates source truth |
| Communications and Identity restore differently | Communications/provider state cannot manufacture Identity verification state |

## `AE-WD-065` — FP-001 Audit dossier adjudication

> **FP-001 requires an Audit & Evidence JIT Domain Dossier. The dossier is required because Phase 7C cannot state the complete implementation-grade FP-001 evidence-event selection, E1/E2 acceptance semantics, minimisation, evidence identity/idempotency, privileged access, correction/supersession and retention-class contract without introducing Audit-owned Domain semantics that are not fully specified by the existing Identity & Access and Communications dossiers.**

### Locked Pre-JIT adjudication

`FP-001 Audit & Evidence JIT Domain Dossier: REQUIRED`

This does not imply every later Feature Pack automatically requires another Audit dossier. Each Feature Pack must undergo its own JIT-necessity test.

Primary bucket: `DOMAIN_JIT`.

---

# 18. Next pressure-test queue

## Pass 10 — Cross-domain generalisation attack

Pressure-test `AE-WD-001..065` against:

### Commerce / provider disorder

- provider success arrives after a failure-looking observation;
- app crashes after provider success before Commerce records interpretation;
- Commerce becomes authoritative before central Audit materialisation;
- refund/dispute/reversal corrects or supersedes prior commercial interpretation;
- provider payload is later unavailable;
- duplicate/reordered provider evidence races with Audit evidence materialisation;
- retained Audit evidence must not reconstruct deleted participant access.

### Health / Safety correction

- Health fact later corrected/retracted;
- Safety previously acted on then-valid Health assertion;
- human override or exceptional safety decision;
- automated eligibility result with delayed central Audit;
- sensitive health content must not be duplicated into Audit;
- source Health record lawfully disposed while independently authorised Audit evidence survives;
- restore divergence across Health, Safety and Audit.

Pass 10 must decide whether the current doctrine is Identity-overfit, needs refinement, or generalises unchanged.

---

# 19. Change ledger addition

## v0.4.0 — 2026-10-08

Cumulative append-only successor. Preserves v0.3.0 semantics and adds accepted Pass 9 FLOW-01 doctrine.

Added:

- accepted `AE-WD-060` through `AE-WD-065`;
- FLOW-01 end-to-end crash/retry/replay/concurrency/restore pressure outcomes;
- explicit E2 source-transition/evidence-obligation acceptance-boundary rule;
- explicit E1 admission-vs-outcome semantics;
- explicit rule that Audit never repairs source atomicity or resolves source concurrency;
- locked FP-001 Audit & Evidence dossier adjudication: `REQUIRED`;
- Pass 10 cross-domain generalisation queue.

No prior accepted discovery decision is silently removed or rewritten. No Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority is amended by this file.

---

# 20. Pass 10 — Cross-domain generalisation attack

## Pass objective

Test whether `AE-WD-001..065` are Identity-overfit by applying them to Commerce/provider disorder, refund/reversal/dispute semantics, Health/Safety corrections, privileged Safety overrides, sensitive categorical evidence and cross-domain restore divergence.

## `AE-WD-066` — Evidence selection precedes E1/E2 classification

> **E1/E2/E3 classifies the acceptance semantics of an evidence obligation; it does not itself decide that central Audit evidence is required. The Domain/risk contract first determines whether the semantic event requires central Audit evidence at all. Only selected central evidence is then classified E1 or E2; otherwise source-owned evidence and/or telemetry remains sufficient.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-067` — Compensating source outcomes are not evidence corrections

> **A later legitimate compensating business outcome—such as refund, reversal, revocation or safety restriction—does not automatically mean earlier Audit evidence was erroneous. Where both source-domain facts are historically true, Audit preserves them as distinct governed events rather than treating the later event as a correction of the earlier evidence.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-068` — Safety/authority broadening versus narrowing

> **Where central evidence is required, an exceptional human action that broadens or restores sensitive/safety authority is E1; an action that narrows, pauses or withdraws authority is E2 so that making the platform safer is not blocked by central Audit availability.**

Primary bucket: `CROSS_DOMAIN_JIT`.

## `AE-WD-069` — Structured/categorical evidence may itself be sensitive

> **Minimisation applies to semantic classifications as well as raw payloads. A result code, restriction category, reason code or derived outcome may itself reveal sensitive health, identity, security or financial information and must not be treated as harmless merely because it is structured rather than free text.**

Primary bucket: `DOMAIN_JIT`.

## Commerce/provider pressure outcomes

| Scenario | Accepted working result |
|---|---|
| Failure-looking provider observation followed by delayed success | Commerce interprets provider evidence; Audit arrival order does not decide truth |
| Provider may have succeeded but app crashed before Commerce interpretation | Commerce reconciles first; Audit cannot invent payment success |
| Commerce becomes authoritative before central Audit materialises | If selected for central Audit, use E2 acceptance with lossless evidence obligation |
| Refund/reversal after prior successful payment | Both source facts may remain historically true; later compensation is not automatically an Audit correction |
| Dispute/chargeback | Does not itself become fraud/security truth |
| Provider payload later expires | Audit reference does not force indefinite source/provider evidence retention |
| Audit materialisation races duplicate/reordered provider evidence | Source owner resolves; Audit records only selected accountability evidence |

## Health/Safety pressure outcomes

| Scenario | Accepted working result |
|---|---|
| Health assertion later corrected/retracted | Health owns correction; prior Audit evidence may still truthfully show what the platform possessed/acted on at the time |
| Genuine later health-state change | Not an evidence correction merely because the value/result differs |
| Automated eligibility result | Safety-owned; central Audit only if independently selected by current Domain/risk contract |
| Human override broadens sensitive/safety authority | E1 where central evidence is required |
| Restriction/pause/withdrawal narrows authority | E2 where central evidence is required |
| Detailed clinical rationale exists | Keep clinically complete rationale with proper owner; Audit receives minimum accountability envelope |
| Structured result/reason code itself reveals sensitive information | Treat as sensitive; use minimum necessary granularity |
| Source Health record later lawfully disposed | Surviving Audit reference may become non-resolvable; Audit must not reconstruct source truth |
| Health/Safety/Audit restore points diverge | Source owners reconcile their own truth; Audit never recreates source state |

## Pass 10 verdict

`PASS — doctrine generalises across Identity, Commerce/provider disorder, and Health/Safety correction without changing the core Domain ownership model.`

No new `UPSTREAM_PRODUCT` or `UPSTREAM_ARCHITECTURE` contradiction was found.

---

# 21. Pass 11 queue — unresolved-bucket and semantic-completeness audit

Objectives:

1. enumerate every remaining unresolved Audit/Evidence issue;
2. assign exactly one primary bucket from the mandatory taxonomy;
3. attack whether any item classified as JIT is actually an upstream Product or Architecture gap;
4. distinguish legal/privacy inputs from implementation proof and provider empirical work;
5. identify any unresolved issue that blocks the Pre-JIT itself;
6. decide whether broad discovery is complete enough to compress into the final five-file pack.

Mandatory primary buckets:

- `UPSTREAM_PRODUCT`
- `UPSTREAM_ARCHITECTURE`
- `DOMAIN_JIT`
- `CROSS_DOMAIN_JIT`
- `EXPERT_LEGAL_PRIVACY`
- `IMPLEMENTATION_PROOF`
- `PROVIDER_EMPIRICAL`
- `RELEASE_ONLY`
- `FUTURE_ONLY`

---

# 22. Change ledger addition

## v0.5.0 — 2026-10-08

Cumulative append-only successor. Preserves v0.4.0 semantics and adds accepted Pass 10 cross-domain generalisation doctrine.

Added:

- accepted `AE-WD-066` through `AE-WD-069`;
- explicit rule that evidence selection precedes E1/E2 classification;
- explicit distinction between compensating source events and Audit corrections;
- generalised broadening-vs-narrowing asymmetry into Safety/sensitive authority;
- explicit sensitivity of derived/categorical evidence;
- Commerce/provider and Health/Safety pressure outcomes;
- Pass 10 generalisation verdict;
- Pass 11 unresolved-bucket/completeness queue.

No prior accepted discovery decision is silently removed or rewritten. No Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority is amended by this file.

---

# 23. Pass 11 — Unresolved-bucket and semantic-completeness audit

## Pass objective

Prove that remaining incompleteness is correctly downstream and that no unresolved Product or Architecture contradiction is being hidden as “JIT detail”.

## Remaining unresolved register

Each unresolved issue has exactly one primary bucket.

| Remaining issue | Primary bucket |
|---|---|
| Exact Audit Resource(s), field names, schema, actions, indexes and relationships | `DOMAIN_JIT` |
| Exact per-Feature-Pack central evidence event/category matrix | `DOMAIN_JIT` |
| Exact evidence envelope by category, including allowed result/reason granularity | `DOMAIN_JIT` |
| Evidence assertion identity / materialisation dedupe representation | `DOMAIN_JIT` |
| Correction/supersession relation representation and derived current interpretation | `DOMAIN_JIT` |
| Audit reader/query/export/correction/disposition capability matrix | `DOMAIN_JIT` |
| Exact evidence-retention disposition representation, including correction-chain coherence | `DOMAIN_JIT` |
| Ash Temporal Resources versus ordinary append-only Ash Resources | `DOMAIN_JIT` |
| Cryptographic chaining, WORM, signatures, Merkle structures and similar integrity mechanisms | `DOMAIN_JIT` |
| E1/E2 owner-to-Audit acceptance contract for each cross-domain event | `CROSS_DOMAIN_JIT` |
| Durable source-reference / causal / correlation contract per participating Domain | `CROSS_DOMAIN_JIT` |
| Source correction -> Audit correction/supersession handshake | `CROSS_DOMAIN_JIT` |
| Long-lived disclosure/export revalidation when authority changes mid-operation | `CROSS_DOMAIN_JIT` |
| Exact retention periods for Audit categories | `EXPERT_LEGAL_PRIVACY` |
| Which evidence categories may retain restricted post-deletion linkage and for how long | `EXPERT_LEGAL_PRIVACY` |
| Legal-hold scope, policy-change retroactivity and overlapping-hold specifics | `EXPERT_LEGAL_PRIVACY` |
| Exact anonymisation threshold where evidence linkage is retained/transformed | `EXPERT_LEGAL_PRIVACY` |
| E1 fail-closed behaviour under crashes/outages | `IMPLEMENTATION_PROOF` |
| E2 transaction/evidence-obligation crash atomicity | `IMPLEMENTATION_PROOF` |
| Evidence-materialisation retry/idempotency/concurrency | `IMPLEMENTATION_PROOF` |
| Sensitive-data leakage/redaction and query-scope enforcement | `IMPLEMENTATION_PROOF` |
| Tamper-resistance including exceptional DBA/infrastructure paths | `IMPLEMENTATION_PROOF` |
| Backup/restore, expired-evidence replay and reconciliation | `IMPLEMENTATION_PROOF` |
| Detection/reconciliation of Audit-behind or Audit-ahead restore divergence | `IMPLEMENTATION_PROOF` |
| Evidence disposition versus malicious disappearance distinguishability | `IMPLEMENTATION_PROOF` |
| Third-party delivery/payment provider behaviour | `PROVIDER_EMPIRICAL` |
| Selected external WORM/KMS/evidence provider behaviour, if ever chosen | `PROVIDER_EMPIRICAL` |
| Exact class-specific RPO/RTO | `RELEASE_ONLY` |
| Production incident ownership/escalation operating model | `RELEASE_ONLY` |
| Multi-region/external evidence service or specialist infrastructure absent demonstrated need | `FUTURE_ONLY` |
| More elaborate cryptographic evidence infrastructure absent threat/proof need | `FUTURE_ONLY` |

Current unresolved `UPSTREAM_PRODUCT`: **NONE**.

Current unresolved `UPSTREAM_ARCHITECTURE`: **NONE**.

Conditional escalation remains mandatory if a downstream mechanism would silently amend upstream law or platform constraints.

## Required semantic-category completeness audit

| Required category | Status |
|---|---|
| Business truth vs evidence truth | `COVERED` |
| Exactly-once illusion | `COVERED` |
| Failed attempts | `COVERED` |
| Correction / supersession | `COVERED` |
| Minimisation | `COVERED` |
| Access / operator | `COVERED` |
| Retention | `COVERED` |
| Cross-domain semantics | `COVERED` |
| Security / abuse | `COVERED` |
| Disaster recovery | `COVERED` |

## `AE-WD-070` — Downstream incompleteness is not upstream ambiguity

> **The Pre-JIT need not settle Resource representation, exact retention periods, infrastructure mechanisms, provider behaviour, RPO/RTO or executable proof where current higher authority already defines the semantic invariant and explicitly leaves those matters downstream.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-071` — No current Product/Architecture amendment is required

> **The completed Audit & Evidence pressure tests have identified no unresolved current requirement that requires amendment of Product Law or Architecture Law before an Audit & Evidence JIT Domain Dossier can be written.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-072` — Later Feature Packs still require event-selection adjudication

> **This Pre-JIT establishes reusable Audit/Evidence doctrine but does not pre-classify every later Feature Pack event. Each Feature Pack/JIT must determine which of its semantic events require central Audit evidence before applying E1/E2 acceptance classification.**

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-073` — Mechanism choices remain replaceable

> **Ash Temporal Resources, ordinary append-only Ash Resources, cryptographic integrity structures, WORM storage and similar mechanisms remain replaceable JIT candidates. None acquires architectural status merely because it is useful for historical evidence.**

If a candidate's requirements exceed current Architecture, the JIT must stop and escalate.

Primary bucket: `DOMAIN_JIT`.

## `AE-WD-074` — Pre-JIT semantic discovery completeness

> **The Audit & Evidence Pre-JIT has established enough Domain semantics to prevent Phase 7C or implementation from inventing Audit ownership, evidence criticality, acceptance boundaries, idempotency/correction semantics, minimisation, access, retention doctrine, cross-domain authority or restore behaviour. Remaining issues are correctly routed downstream.**

Primary bucket: `DOMAIN_JIT`.

## Pass 11 verdict

`PASS — NO HIDDEN UPSTREAM AUDIT/EVIDENCE GAP FOUND`

`PASS — BROAD DISCOVERY IS COMPLETE ENOUGH FOR COMPRESSION`

---

# 24. Change ledger addition

## v0.6.0 — 2026-10-08

Cumulative append-only successor. Preserves v0.5.0 semantics and adds accepted Pass 11 completeness doctrine.

Added:

- accepted `AE-WD-070` through `AE-WD-074`;
- complete unresolved-bucket routing with exactly one primary bucket per item;
- explicit finding of no current `UPSTREAM_PRODUCT` or `UPSTREAM_ARCHITECTURE` blocker;
- required semantic-category completeness audit;
- broad-discovery-complete verdict;
- readiness to run compression/staleness audit and produce the compact Pre-JIT pack.

No prior accepted discovery decision is silently removed or rewritten. No Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority is amended by this file.

---

# 25. v0.6.1 full-review patch corrections

```text
PATCH / PROVENANCE + ROUTING + SOURCE-ATTRIBUTION CORRECTION
NO ACCEPTED SEMANTIC DECISION IS REMOVED
IMPLEMENTATION REMAINS UNAUTHORISED
```

This patch follows a full re-review of the cumulative discovery ledger and the first compact compression pack against live repository authority at:

`a9c9a8d176e8d62044ca069efeefa60b8f666c8d`

The earlier accepted discovery doctrine remains current. This patch corrects routing presentation, source attribution and current-status navigation only.

## 25.1 Current effective status

Historical sections retain the state that was true at the time of each pass.

The following later accepted decision is the current effective FP-001 adjudication:

> **`AE-WD-065`: FP-001 Audit & Evidence JIT Domain Dossier = REQUIRED.**

Therefore:

- the earlier section headed `FP-001 Audit dossier adjudication — NOT YET FINAL` is historical pass-state only;
- `AE-WH-001` is a historical working hypothesis;
- `AE-WD-065` supersedes that hypothesis and is current working doctrine.

No Phase 7C, proof classification or implementation authority is created by this discovery artifact.

## 25.2 Authority/provenance correction

The live source check for this stream includes the machine-readable:

`docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`

The manifest is an authority inventory/routing artifact and does not create a new authority layer.

Current supporting Engineering Standards path is:

`docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md`

not a root-level `docs/00_platform/ENGINEERING_STANDARDS_v1.0.1.md` path.

## 25.3 Effective single-primary routing corrections

Some Pass 7 entries historically displayed two slash-separated routing labels. The semantic decisions remain accepted, but the effective routing must obey the stream rule that each unresolved issue has exactly one primary bucket.

| Decision | Effective primary bucket | Downstream/conditional route |
|---|---|---|
| `AE-WD-038` semantic immutability vs physical representation | `DOMAIN_JIT` | executable migration/integrity behaviour → `IMPLEMENTATION_PROOF` |
| `AE-WD-043` Audit export derivative governance | `DOMAIN_JIT` | export expiry/disposal enforcement → `IMPLEMENTATION_PROOF` |
| `AE-WD-045` final trusted integrity boundary | `DOMAIN_JIT` | control effectiveness → `IMPLEMENTATION_PROOF` |
| `AE-WD-046` confidentiality vs integrity separation | `DOMAIN_JIT` | encryption/integrity control proof → `IMPLEMENTATION_PROOF` |
| `AE-WD-047` protection-mechanism compromise consequences | `IMPLEMENTATION_PROOF` | production incident ownership/escalation remains independently `RELEASE_ONLY` |
| `AE-WD-048` current-integrity fail-closed vs bounded historical anomaly | `DOMAIN_JIT` | integrity/recovery demonstration → `IMPLEMENTATION_PROOF` |
| `AE-WD-049` lawful disposition vs tampering distinction | `DOMAIN_JIT` | detectability/enforcement demonstration → `IMPLEMENTATION_PROOF` |

These effective primary routes supersede only the historical slash-separated routing presentation. They do not change the accepted semantic decision bodies.

`AE-MECH-001` and `AE-MECH-002` retain `DOMAIN_JIT` as their single primary bucket. Any stated `UPSTREAM_ARCHITECTURE` route is a conditional escalation trigger if a chosen mechanism would exceed current Architecture authority, not a second primary bucket.

## 25.4 `AE-WD-006` source-attribution clarification

The accepted fail-closed doctrine remains current, but its historical wording overstated the exact source of the outage-timing rule.

Current higher authority requires governed, named, strongly authenticated, scoped/time-bounded, alerted/post-reviewed emergency or privileged access and requires auditing for governed sensitive access. It defines no explicit unaudited bypass.

The current effective reading of `AE-WD-006` is therefore:

> **Current Product/Architecture/Domain authority requires governed audited emergency/privileged access and defines no explicit unaudited bypass. This Pre-JIT adopts fail-closed E1 semantics when required pre-effect evidence cannot be durably established. Any future Product requirement to permit protected emergency/privileged access despite failure to establish required E1 evidence is an `UPSTREAM_PRODUCT` change requiring explicit safety/legal/architecture treatment.**

This clarification preserves the accepted safety posture while distinguishing higher-authority requirements from the Pre-JIT's exact acceptance-timing semantic.

## 25.5 Ash Temporal Resources evidence snapshot

The mechanism routing remains unchanged:

- Ash Temporal Resources are **not** selected by this Pre-JIT;
- the core Audit ledger should not assume a temporal-resource model because the accepted evidence model is multiple independently meaningful immutable assertions rather than versions of one logical row;
- final selection belongs to the applicable Domain JIT.

As of the 2026-10-08 recheck against official HexDocs, Temporal Resources remain experimental; production AshPostgres support requires PostgreSQL 18+, and the then-current package/API compatibility must be reverified again at JIT.

This is ecosystem evidence only, not an Architecture pin.

## 25.6 Compact-pack review correction

The first compact `v0.1.0` compression pack did not fully preserve every accepted semantic decision. Its prior compression-PASS statement is therefore superseded.

The cumulative discovery ledger itself remains the accepted historical evidence source.

A corrected compact successor must:

- restore every accepted `AE-WD-001..074` semantic;
- preserve the full FP-001 event/evidence matrix rather than weakening selected `YES` central-Audit rows;
- preserve `AE-MECH-001..002` as mechanism candidates only;
- record `AE-WH-001` as superseded by `AE-WD-065`;
- use the corrected current supporting-authority paths;
- retain exactly one primary unresolved bucket per issue.

---

# 26. v0.6.1 change ledger addition

## v0.6.1 — 2026-10-08

Patch successor to v0.6.0 after full certification-style re-review.

Corrected:

- current-status navigation for historical `NOT YET FINAL` / `AE-WH-001` text;
- Authority Manifest and Engineering Standards provenance/path;
- seven historical dual-primary routing presentations into one effective primary route each;
- `AE-WD-006` source attribution without weakening fail-closed E1 doctrine;
- Ash Temporal Resources evidence snapshot and non-selection posture;
- prior compact-pack compression verdict, which is superseded pending corrected compact v0.1.1.

No accepted `AE-WD-001..074` semantic decision is removed. No Product, Architecture, Domain, Roadmap, Feature Pack or implementation authority is amended.

---

# 27. v0.6.2 targeted programme-status / upstream-scope routing patch

```text
PATCH / DOCUMENTARY ROUTING ONLY
NO NEW AUDIT SEMANTICS
NO GOVERNED PROGRAMME-STATE PROMOTION
IMPLEMENTATION REMAINS UNAUTHORISED
```

A full independent review confirmed that broad Audit & Evidence discovery is complete enough to stop, but identified two documentary hazards for small-context downstream agents.

## 27.1 Working adjudication versus governed programme state

Current accepted Pre-JIT working adjudication:

> **`AE-WD-065`: FP-001 Audit & Evidence JIT Domain Dossier = REQUIRED.**

Current live governed programme state at pinned baseline:

> **AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION.**

> **PHASE 7C: BLOCKED / NOT_STARTED.**

These statements are intentionally different.

The working Pre-JIT conclusion does **not** promote itself into governed Open Work / programme state. Only an explicit authorised adjudication/current-status promotion may change the governed status.

Any later agent or artifact must preserve the distinction:

```text
working Pre-JIT adjudication
≠
governed programme-state promotion
```

## 27.2 Audit-specific scope of “no upstream gap”

The effective completeness claim is:

> **No unresolved Audit-specific Product or Architecture amendment prerequisite has been identified.**

This is not a platform-wide statement that all Product/Privacy/Commerce/Safety/Trust & Safety policy questions are closed.

Separately governed upstream gaps in participating Domains remain binding whenever a Feature Pack exercises those behaviours. This Audit Pre-JIT does not resolve, absorb or supersede them.

## 27.3 Freeze effect

This patch changes documentary routing/precedence only.

It does not alter:

- `AE-WD-001..074`;
- `AE-MECH-001..002`;
- the E1/E2/E3 model;
- ownership boundaries;
- the working FP-001 `REQUIRED` adjudication;
- downstream proof/defer routing.

After this patch, the documentary Pre-JIT may be frozen while the governed programme status remains conditional until explicitly adjudicated/promoted.

---

# 28. v0.6.2 change ledger addition

## v0.6.2 — 2026-10-08

Patch successor to v0.6.1 after independent freeze-readiness review.

Corrected:

- made the distinction between working `REQUIRED` adjudication and live governed `CONDITIONAL / PENDING EXPLICIT ADJUDICATION` impossible to miss;
- made explicit that Phase 7C remains `BLOCKED / NOT_STARTED`;
- scoped “no upstream Product/Architecture gap” to **Audit-specific amendment prerequisites**;
- stated that independently governed upstream gaps in participating Domains remain binding.

No accepted Audit semantic decision changed. No repository programme-state promotion is performed by this file.

