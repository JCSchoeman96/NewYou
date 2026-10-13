# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.8.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.8.0`
- **Date:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch head before this successor:** `877a83247b240028f551a1508508bdae286f6904`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.7.0.md`
- **Purpose:** perform one bounded pass on operator authority and consequential correction, with particular focus on `OPS-UPD-003`.
- **Scope:** request/approve/execute/reconcile/correct/compensate/override distinctions; Support/Finance/Super Admin/Developer authority boundaries; stale authority; human/automation races; bulk actions; break-glass; source-Domain command boundaries; operator evidence obligations.
- **Explicit non-goals:** no pilot-count/admission semantics, no Day-7/30/90 measurement semantics, no pause/resume product-policy redesign, no communications-policy pass, no privacy/deletion pass, no clinical-operational policy design, no new Operations/Support/Admin Domain, no implementation, no PR, no authority amendment.
- **External evidence dates:** none added. Current Audit & Evidence working contract is reused only as non-authoritative supporting evidence where explicitly labelled.
- **Current overall disposition:** `FOCUSED PASS CONVERGED / OPS-UPD-003 NARROWED / REMAINING EXACT HUMAN COMMAND ASSIGNMENTS REQUIRE FP-006 OPERATIONS POLICY / BROAD STREAM FREEZE STILL BLOCKED`.

---

# 0. Append-only successor rule

Reasoning chain:

```text
v0.1.0
→ v0.2.0
→ v0.3.0
→ v0.4.0
→ v0.5.0
→ v0.6.0
→ v0.7.0
→ this v0.8.0 focused operator-authority pass
```

All predecessors remain preserved. This successor does not erase the broader historical pressure testing. It intentionally adds only the material needed for this bounded pass.

This version adds:

- `OPS-PT-128...OPS-PT-139`;
- no new `OPS-UPD`;
- no new `OPS-GAP`;
- a material narrowing/adjudication of existing `OPS-UPD-003`.

---

# 69. Live baseline and bounded authority route

Immediately before this pass, live GitHub `main` was re-fetched and remained:

```text
086ade7b28c000de1c387acb9760e5eb08bb0413
```

The repository README still routes current authority through:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` where relevant.

For this bounded pass, the authority actually rechecked in depth was limited to:

- Product Law staff/privileged-access/correction rules in `00_PLATFORM_v1.6.0.md`, especially §§15, 21I and 21J;
- `DEC-291` in `01_DECISIONS_v1.6.0.md`;
- current-authority, owner-command and privileged-access doctrine in `03_ARCHITECTURE_v1.1.1.md`;
- Domain ownership in `04_DOMAIN_MAP_v1.2.0.md`;
- FP-006 operator outcome in `05_ROADMAP_v1.2.0.md`;
- role/work/approval/bulk/support doctrine in `PLATFORM_OPERATING_MODEL_v1.0.1.md`;
- certified/current Identity planning detail in `working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md` only where it refines the already-authorised Identity command boundary;
- `working/audit_evidence/NEWYOU_AUDIT_EVIDENCE_PREJIT_CONTRACT_WORKING_v0.1.3.md` only as non-authoritative supporting evidence, never as upstream law.

No archive document was used to override current authority.

---

# 70. Authority findings for this pass

## 70.1 Role labels are not business permissions

Current Product and Operating Model law names staff categories such as Support, Finance, Super Admin and Developer. Architecture Law is stronger than any convenient UI interpretation:

> authorisation composes role/capability with relationship, purpose, scope, expiry and current authoritative state.

Therefore:

```text
role name
≠ blanket capability
≠ relationship authority
≠ current permission
≠ source-Domain transition authority
```

A person may hold several roles, but each consequential action still has to prove the specific authority under which it is being performed.

## 70.2 Work is attention, not authority

The Operating Model explicitly says:

- queue visibility does not grant business-action authority;
- self-approval exists only where policy permits it;
- separation of duties applies where governing law requires it;
- bulk action is lawful only if every selected target independently passes its own policy and invariants.

Therefore assignment, claim, ownership of a case, or a visible button is not an authorisation primitive.

## 70.3 Human actions must still invoke the owner Domain

Current Architecture and Operating Model law already forbid an operator UI from becoming a second business-write API.

Examples remain:

- Commerce owns payment/refund/dispute truth;
- Entitlements owns current right/source truth;
- Identity & Access owns account/recovery/reconciliation and identity-side grants;
- Temperament owns assessment result truth;
- Safety & Eligibility owns safety/eligibility restriction/override truth;
- Plans & Nutrition owns Plan truth;
- Privacy & Consent owns purpose permission and deletion/export rights;
- Audit & Evidence owns evidence truth only.

An operator may be the human cause of a lawful transition. The operator does not become owner of the resulting business truth.

## 70.4 Current authority is checked when the consequential action executes

Architecture Law requires revocable permission to be resolved from current server state when an authoritative action occurs. Long-lived UI state, a prior approval, a queue assignment or a stale operator page cannot become permanent authority.

This implies a minimum two-dimensional revalidation:

1. **actor authority is still valid now**; and
2. **the source-Domain transition is still lawful now**.

## 70.5 Super Admin and break-glass are not business override semantics

Product Law says Super Admin must not become an everyday unrestricted working role. Architecture Law says there is no universal Super Admin bypass.

Current Product Law further requires emergency/break-glass access to have a named identity, strong MFA, explicit reason, narrow scope where possible, short expiry, immediate audit event, designated-owner alert and post-access review.

That is an exceptional **access/elevation** path. It does not imply permission to manufacture payment truth, entitlement, assessment results, health facts, safety outcomes, Plans, consent or any other owner-Domain truth.

If a break-glass actor must also perform a business transition, that transition still requires an explicit lawful owner-Domain operation and the business authority applicable to that operation.

## 70.6 Direct database mutation is not an operator correction model

Product Law explicitly says Support may not overwrite historical truth directly in the database. Architecture Law makes direct Ecto/SQL a controlled read/infrastructure escape hatch, never a second ordinary business-write API.

Therefore “manual correction” continues to mean:

> an authorised human invokes an explicit owner-Domain operation under current guards.

It does not mean “edit the row until the screen looks correct.”

---

# 71. Minimum consequential-command vocabulary

This pass narrows `OPS-UPD-003` by defining the semantic verbs that FP-006 operations policy must not collapse.

| Verb | Meaning | What it does **not** mean |
|---|---|---|
| `observe` | read authorised minimum-necessary context | permission to mutate |
| `request` | create/raise a proposed action or investigation | approval or business effect |
| `approve` | policy decision that a proposed action may proceed | source-Domain success |
| `execute` | invoke an authoritative owner-Domain operation | direct persistence edit |
| `retry` | repeat an operation only after a known retryable failure under the same logical obligation | repeat after unknown outcome |
| `reconcile` | resolve ambiguous/conflicting evidence against owner rules and current truth | choose the operator-preferred answer |
| `correct` | fix an earlier wrong/incomplete authoritative assertion through the owner's correction semantics | erase true history |
| `compensate` | create a later lawful consequence while preserving the earlier true event | pretend the earlier event never happened |
| `restrict / revoke / stop` | narrow an authority/capability/right where a lawful owner transition permits it | universal operator emergency power |
| `restore / broaden / grant` | increase authority/capability/right through an explicit lawful owner transition | inverse of revocation by assumption |
| `override / exception` | exceptional transition only where upstream/owner law explicitly defines such a power | generic “force” button |
| `bulk` | operator convenience over multiple independent lawful commands | one aggregate bypass of per-target guards |

A UI may combine steps for usability only where governing law permits the same actor to hold the required powers. The semantic distinctions remain real even when the interface is compact.

---

# 72. Independent lifecycle dimensions

This pass rejects a universal `AdminAction` lifecycle as hidden authority. At least four dimensions must remain independently reasoned about.

## 72.1 Request / approval lifecycle

Conceptually, where approval is required:

```text
not_requested
→ submitted
→ approved | rejected | expired | superseded
```

Approval is an authorisation fact. It is not proof that the source transition executed.

Where the governing policy permits direct self-service operator execution, this lifecycle may be absent; do not manufacture approval bureaucracy for every low-risk action.

## 72.2 Execution-attempt lifecycle

Conceptually:

```text
not_started
→ dispatched
→ succeeded
   | rejected_by_current_guard
   | known_retryable_failure
   | known_final_failure
   | outcome_unknown
```

`outcome_unknown` may proceed to:

```text
outcome_unknown
→ reconciling
→ resolved_success | resolved_failure | still_unresolved
```

A retry is lawful only from an outcome that is known to be safe to retry under the owner contract.

## 72.3 Source-Domain business lifecycle

The source Domain's own states/transitions remain authoritative and do not collapse into operator-command state.

Examples:

- refund request approved but Commerce refund still unresolved;
- operator execution succeeded but Entitlements consequence still pending;
- operator request rejected because the underlying source state already changed;
- work item resolved after the source Domain has already converged automatically.

## 72.4 Work-item lifecycle

`UNASSIGNED / ASSIGNED / IN_PROGRESS / CHANGES_REQUESTED / RESOLVED` remains only an operating projection vocabulary. It does not certify business outcome.

A work item may close only according to the owning workflow's resolution criteria; where the case exists to achieve a business consequence, closure must not falsely represent an unresolved source obligation as resolved.

---

# 73. Minimum authority conjunction for a consequential command

The safe conceptual rule is:

```text
authenticated named actor + required assurance
AND active scoped grant/capability
AND valid relationship/purpose/context where applicable
AND workflow policy allows this actor to request/approve/execute this command class
AND required separation-of-duties condition is satisfied
AND source-Domain current-state guard permits the transition
AND required pre-effect evidence can be established where governing law requires it
→ command may be admitted
```

None of these substitutes for another.

The following are specifically **not** sufficient:

- staff role name alone;
- queue visibility;
- work assignment;
- a previously rendered button;
- a prior approval whose actor grant has since been revoked;
- provider dashboard state;
- Audit history;
- an Analytics projection;
- direct database access.

---

# 74. Role-boundary conclusions without inventing the final FP-006 matrix

## 74.1 Support

Current authority permits Support to work participant cases and permitted identity/access/entitlement/payment issues, while requiring minimum necessary context and prohibiting routine impersonation/direct historical overwrite.

Safe conclusion now:

- Support may observe/explain/triage within authorised scope;
- Support may raise/request/escalate consequential work;
- Support may execute a source-Domain command only when that exact capability is explicitly granted and current policy permits it;
- Support role alone is never a blanket refund/grant/reset/rewrite power.

The exact FP-006 Support command set remains unresolved operations policy.

## 74.2 Finance

The Operating Model centres Finance on payment/reconciliation exceptions, refunds/disputes and commercial indicators.

Safe conclusion now:

- Finance work may invoke Commerce operations where explicitly authorised;
- Finance cannot directly manufacture Entitlement truth because access is owned separately;
- a Commerce outcome may trigger/recover an Entitlements consequence through the owner boundary;
- exact request/approve/execute separation for refunds/reconciliation remains unresolved operations policy.

## 74.3 Super Admin

Safe conclusion now:

- not an everyday unrestricted working role;
- no universal cross-Domain bypass;
- break-glass elevation is explicit, scoped, short-lived and evidenced;
- possession of Super Admin/break-glass access does not itself create methodology, clinical, safety, financial, consent or other business authority.

## 74.4 Developer / Platform

Safe conclusion now:

- technical operational/release evidence does not imply unrelated business-data access;
- exceptional production access is separately governed;
- direct database access is exceptional infrastructure access, not an accepted operator correction API;
- after a technical intervention, business truth must still be established/reconciled by the owning Domain rather than declared correct because a developer changed storage.

## 74.5 Clinical / methodology / practitioner authority

These powers are granted through the relevant approved role/relationship/scope and cannot be inherited from Support, Finance or Super Admin.

This pass does **not** design those operational policies. It only confirms that FP-006 cannot bypass them through a generic operator role.

---

# 75. Focused pressure tests

## OPS-PT-128 — Support requests a refund but is not the refund executor

**Scenario class:** operator / financial / authority separation

**Why it matters**  
A participant-facing Support role may need to initiate resolution without becoming Commerce authority.

**Relevant current authority**  
Commerce ownership; Operating Model role/work boundaries; Product correction law; `OPS-UPD-003`.

**Owning Domain(s)**  
Commerce owns refund decision/outcome; Support owns no payment truth.

**Preconditions**  
A participant asks Support for a refund that appears potentially eligible under current Product Law.

**Timeline**

```text
Support observes minimum permitted context
→ Support records/raises refund request with reason and evidence reference
→ no business effect yet
→ authorised Commerce/Finance path evaluates current eligibility/state
→ approved executor invokes Commerce operation
→ Commerce outcome becomes authoritative
→ downstream Entitlement consequence converges if applicable
```

**Expected invariant(s)**

- Support request is not a refund;
- ticket/work resolution is not refund success;
- exact actor executing Commerce must hold current capability;
- duplicate Support requests cannot create duplicate refunds.

**Questions under test**  
Must Support always be request-only? Must Finance approve and execute? Is dual approval required?

**Analysis**  
Current authority does not answer those exact assignments. It answers the owner boundary. The exact FP-006 mapping remains `OPS-UPD-003` operations policy.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `OPERATIONS_POLICY` → `JIT` → `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-003`.

**Evidence still required**  
Exact command-role mapping, approval rule and duplicate-command proof.

**Follow-up**  
None in this pass.

---

## OPS-PT-129 — Finance reconciles payment and attempts to grant access directly

**Scenario class:** operator / financial / cross-domain authority

**Why it matters**  
Finance may legitimately establish Commerce truth but still not own the participant's current right.

**Relevant current authority**  
Commerce/Entitlements ownership; Architecture owner-command doctrine; FP-002/FP-006 outcome.

**Owning Domain(s)**  
Commerce for payment; Entitlements for access.

**Preconditions**  
Finance reconciles previously ambiguous provider evidence to verified paid success.

**Expected invariant(s)**

- Finance may not write an `active` access flag directly;
- verified Commerce truth creates/requires the governed Entitlements consequence;
- recovery of a missing consequence invokes Entitlements convergence/idempotent owner action;
- any other valid Entitlement source remains independently intact.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-003` only for who may trigger which recovery command.

**Evidence still required**  
Negative direct-write proof and cross-domain convergence proof.

---

## OPS-PT-130 — One human holds Support and Finance roles

**Scenario class:** operator / separation of duties

**Why it matters**  
The platform explicitly permits one identity to hold multiple roles. That must not silently erase required approval separation.

**Relevant current authority**  
Product/Operating Model multi-role rule; self-approval only where policy permits; separation of duties where governing law requires.

**Owning Domain(s)**  
Identity & Access owns grants; affected owner Domain owns business transition.

**Preconditions**  
One employee holds both Support and Finance grants.

**Expected invariant(s)**

- each action records/evaluates the actual capability/scope under which it is performed;
- merely holding both roles does not imply that an action requiring independent approval may be self-approved;
- where current policy allows one actor to perform both steps, the separate request/approval semantics may still be evidenced without manufacturing a second person;
- exact separation rule is per command class, not global.

**Questions under test**  
Which FP-006 commands require a distinct approver identity rather than merely a distinct capability?

**Analysis**  
Current law gives the rule shape but not the command-specific answer. That is a bounded operations-policy remainder.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `OPERATIONS_POLICY` then `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-003`.

**Evidence still required**  
Command-specific self-approval/separation policy.

---

## OPS-PT-131 — Approval exists but actor authority is revoked before execution

**Scenario class:** operator / stale authority / security

**Why it matters**  
A durable approval must not become an eternal bearer token after employment/role/scope changes.

**Relevant current authority**  
Architecture current-state authorisation; Product prompt revocation; Identity scoped expiring/revocable grants.

**Owning Domain(s)**  
Identity & Access for actor grant; source Domain for business transition.

**Timeline**

```text
request approved at t0
→ executor grant/scope revoked at t1
→ executor attempts action at t2
```

**Expected invariant(s)**

- current actor authority is revalidated at t2;
- prior approval does not revive a revoked executor grant;
- another currently authorised executor may act if the approval itself remains valid under policy;
- source state is also revalidated at execution.

**Semantic disposition:** `PASS`

**Proof route:** `PHASE8_EXECUTABLE`.

**Upstream delta:** none beyond exact `OPS-UPD-003` command policy.

**Evidence still required**  
Grant-revocation interleaving proof.

---

## OPS-PT-132 — Operator sees timeout and retries a consequential command

**Scenario class:** operator / recovery / idempotency

**Why it matters**  
A timeout is ambiguous; treating it as failure can create duplicate money/access/effects.

**Relevant current authority**  
v0.2.0 unknown-outcome doctrine; Architecture durable/idempotent consequence law; source ownership.

**Owning Domain(s)**  
The command's source owner.

**Preconditions**  
Operator submitted a refund/recovery/revocation/restoration command; response was lost or timed out.

**Expected invariant(s)**

- timeout does not equal failure;
- operator cannot simply repeat the business effect with a new identity;
- same logical command is queried/reconciled/idempotently resumed;
- a known retryable failure may be retried under the same logical obligation;
- distinct human attempts remain separately evidenced even when business effect deduplicates.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`; provider empirical evidence where external effect exists.

**Upstream delta:** none.

**Evidence still required**  
Unknown-outcome/reconciliation and duplicate-attempt proof.

---

## OPS-PT-133 — Manual operator recovery races automated recovery

**Scenario class:** operator / automation / concurrency

**Why it matters**  
The platform must not require operators to disable automation merely to prevent duplicate consequences.

**Relevant current authority**  
Architecture owner-Domain/current-state/idempotency doctrine; v0.2.0 manual-action doctrine.

**Owning Domain(s)**  
Source owner.

**Timeline**

```text
durable obligation exists
→ worker begins recovery
→ operator independently triggers authorised recovery
→ both converge on same logical source obligation
```

**Expected invariant(s)**

- only one lawful business consequence occurs;
- both attempts may remain visible as distinct operational/evidence attempts;
- operator work state does not become the mutex protecting business correctness;
- a stale human command may return already-satisfied/no-op rather than overwrite truth.

**Semantic disposition:** `PASS`

**Proof route:** `PHASE8_EXECUTABLE`.

**Upstream delta:** none.

**Evidence still required**  
Deterministic worker/human interleaving proof.

---

## OPS-PT-134 — Operator closes work while source obligation remains unresolved

**Scenario class:** operator / projection / evidence

**Why it matters**  
A tidy queue must not hide an unresolved customer obligation.

**Relevant current authority**  
Operating Model: work is attention, not authority; work resolves only when owning workflow outcome/criteria are satisfied.

**Owning Domain(s)**  
Source Domain owns obligation; operating projection owns no business truth.

**Preconditions**  
Operator has completed their investigation/handoff but payment/refund/entitlement/recovery outcome remains unresolved.

**Expected invariant(s)**

- if the work item exists specifically to achieve the unresolved outcome, `RESOLVED` must fail its closure guard;
- if responsibility legitimately transfers elsewhere, the original work may close only with a separately durable unresolved obligation/work route still discoverable;
- participant/business status is derived from source truth, not queue closure.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`.

**Upstream delta:** none.

**Evidence still required**  
Workflow-specific closure criteria and unresolved-obligation visibility proof.

---

## OPS-PT-135 — Bulk refund/revoke/recovery action contains mixed-authority targets

**Scenario class:** operator / bulk / policy

**Why it matters**  
Batch convenience can silently turn one permitted target into authority over every selected record.

**Relevant current authority**  
Operating Model bulk guard.

**Owning Domain(s)**  
Each target's relevant source owner.

**Preconditions**  
Operator selects many records; some are eligible, some are stale, restricted or independently sourced.

**Expected invariant(s)**

- each target independently passes actor authority and source guards;
- one valid target cannot authorise an invalid target;
- partial success is explicit, not hidden as one aggregate “success”;
- retries preserve per-target logical identities/outcomes;
- source-specific rights are not globally revoked merely for bulk convenience.

**Semantic disposition:** `PASS`

**Proof route:** `PHASE8_EXECUTABLE`.

**Upstream delta:** none beyond `OPS-UPD-003` if the bulk command class itself is not yet assigned.

**Evidence still required**  
Mixed-target and partial-failure proof.

---

## OPS-PT-136 — Break-glass actor attempts a business override

**Scenario class:** operator / privileged access / abuse

**Why it matters**  
Emergency access is dangerous if interpreted as “can make any business state true.”

**Relevant current authority**  
Product §§15.4 and 21J.12; Architecture §6.3; Domain ownership.

**Owning Domain(s)**  
Identity & Access owns elevation/grant; affected source Domain owns business truth.

**Preconditions**  
Actor receives valid scoped break-glass access to investigate a production incident.

**Expected invariant(s)**

- break-glass access is named, strongly authenticated, reasoned, scoped/expiring, audited, alerted and reviewed;
- elevation does not bypass source-Domain invariants;
- actor cannot convert provider evidence into payment truth, grant paid access, rewrite assessment results, clear Safety restriction or alter consent merely because break-glass is active;
- any lawful consequential transition must still use an explicit owner operation and required business authority.

**Semantic disposition:** `PASS`

**Proof route:** `SECURITY_REVIEW` + `JIT` + `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-003` only for exact break-glass operational issuance/approver route in FP-006.

**Evidence still required**  
Negative cross-Domain bypass proof; expiry/revocation/evidence proof.

---

## OPS-PT-137 — Required privileged-access evidence cannot be established

**Scenario class:** operator / audit / fail-closed

**Why it matters**  
Current Product Law requires an immediate audit event for break-glass. A silent “audit later” path would weaken the governed access contract.

**Relevant current authority**  
Product §21J.12; Architecture governed privileged-access evidence. Non-authoritative Audit Pre-JIT working contract classifies exceptional authority broadening/restoration as E1 and therefore fail-closed when required central evidence cannot be durably established.

**Owning Domain(s)**  
Identity & Access owns elevation; Audit & Evidence owns central evidence if selected by its JIT contract.

**Preconditions**  
Operator requests exceptional authority broadening; required evidence path is unavailable or cannot prove durable capture.

**Expected invariant(s)**

- no unaudited universal bypass is inferred;
- where immediate durable evidence is a precondition of the selected governed path, the broadening fails closed;
- failed broadening remains distinguishable from an already-active grant revocation/narrowing;
- exact Audit E1/E2 implementation remains Audit JIT, not invented here.

**Analysis**  
This does not promote the Audit working E1/E2 labels into Product Law. It records that the working rule is aligned with higher authority's requirement for immediate audited privileged access and no explicit unaudited escape hatch.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** Audit JIT + security proof.

**Upstream delta:** none unless a future Product requirement explicitly wants unaudited emergency broadening.

**Evidence still required**  
Selected Audit capture/failure semantics.

---

## OPS-PT-138 — Immediate safety/technical stop is mistaken for generic operator revoke authority

**Scenario class:** operator / release authority

**Why it matters**  
`DEC-291` deliberately permits immediate scoped safety or technical stop actions. That asymmetry must not become a universal right to revoke arbitrary participant business truth.

**Relevant current authority**  
`DEC-291`; Product narrowest-safe rollback doctrine.

**Owning Domain(s)**  
Release-control authority for stage/capability stop; source Domains retain underlying business truth.

**Expected invariant(s)**

- an authorised immediate stop can narrow the affected release/capability scope without waiting for unrelated expansion approval;
- it does not erase already-committed Commerce/Entitlement/assessment/Plan history;
- it does not imply Support/Finance/Super Admin may revoke arbitrary source truth;
- resume/re-entry requires current evidence and the governed separate product/commercial, clinical/safety and technical/operations authority structure for stage expansion.

**Questions under test**  
Which named people may exercise each FP-006 stop/resume command?

**Analysis**  
The authority classes are Product Law. Exact named-human/capability mapping remains `OPS-UPD-003` operations policy.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `OPERATIONS_POLICY` + `RELEASE_ONLY` + `PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-003`.

**Evidence still required**  
Named/scoped stop and re-entry command mapping.

---

## OPS-PT-139 — Developer performs a direct database “hotfix” to business state

**Scenario class:** operator / technical / correction / abuse

**Why it matters**  
An incident can create pressure to treat database access as the fastest authority path.

**Relevant current authority**  
Product direct-database correction prohibition; Architecture controlled escape-hatch doctrine; Developer minimum-access doctrine.

**Owning Domain(s)**  
Affected source Domain owns business truth; Developer/Platform owns no participant business truth merely by technical access.

**Preconditions**  
Production data appears inconsistent and a developer has exceptional database access.

**Expected invariant(s)**

- direct SQL/Ecto is not the normal business correction path;
- infrastructure repair that changes storage cannot silently redefine business semantics;
- where emergency technical intervention is unavoidable under a separately governed incident path, owner-Domain reconciliation/evidence must establish the resulting business truth;
- the existence of a database credential does not constitute Support/Finance/clinical/privacy authority.

**Semantic disposition:** `PASS`

**Proof route:** `SECURITY_REVIEW` + `JIT` + `PHASE8_EXECUTABLE`.

**Upstream delta:** none.

**Evidence still required**  
Negative ordinary-write-path proof and incident/reconciliation runbook proof.

---

# 76. `OPS-UPD-003` focused adjudication

## 76.1 Prior broad statement

`OPS-UPD-003` was previously framed as the missing consequential FP-006 human command authority matrix.

That remains real, but this pass narrows what is actually missing.

## 76.2 What is already governed and must not be re-decided

The following are already sufficiently governed upstream:

1. business truth remains with the owning Domain;
2. operator UIs/queues/work items do not become authority;
3. roles do not grant unrelated blanket permissions;
4. current scoped authority is checked at execution;
5. one identity may hold multiple roles, but separation of duties still applies where policy/law requires it;
6. there is no universal Super Admin bypass;
7. break-glass is named, strongly authenticated, reasoned, scoped/expiring, audited/alerted and reviewed;
8. bulk actions do not weaken per-target invariants;
9. direct database writes are not the normal business correction path;
10. clinical/methodology/practitioner authority is separately granted;
11. release expansion authority is split across product/commercial, clinical/safety and technical/operations; immediate scoped safety/technical stop is allowed.

FP-006 JIT must consume those constraints, not restate them as optional policy.

## 76.3 What remains a genuine FP-006 operations-policy gate

Before FP-006 Final Feature Pack Contract / development entry, the minimum consequential command set actually exercised by FP-006 must define, for each command class:

- semantic command name and owner Domain;
- whether the human role may `observe`, `request`, `approve`, `execute`, `reconcile`, or only escalate;
- required actor capability/grant/scope;
- whether self-approval is allowed;
- whether a distinct approver identity is required;
- any already-governed assurance/step-up requirement;
- source-state/current-authority guards;
- idempotency/logical obligation identity;
- unknown-outcome/reconciliation path;
- bulk allowance or prohibition;
- evidence requirements;
- work-resolution criteria;
- participant-notification responsibility where already governed.

This is **not** a mandate for a mature-platform permission catalogue. Only the consequential command set needed for FP-006 should be frozen.

## 76.4 Promotion boundary: when operations policy must STOP upstream

The operations-policy matrix may assign actors to **existing lawful actions**. It may not create new business powers.

STOP and promote to the correct authority if the proposed matrix would introduce or redefine any of the following, for example:

- a new complimentary/goodwill/support-resolution Entitlement source or economic cap;
- a discretionary refund/remedy outside current Product commercial law;
- a new ability to rewrite/replace an assessment result rather than use existing technical recovery/review law;
- a new safety/clinical override or professional authority;
- a new Plan replacement/withdrawal right not already authorised by Product/Domain law;
- a privacy/consent/deletion/export override;
- a universal admin/business bypass;
- a new release-stage expansion or customer-admission rule;
- a new unaudited privileged-access exception.

Those are not “permissions configuration.” They change Product, Domain, clinical, privacy/security or release law.

## 76.5 Current disposition

`OPS-UPD-003` becomes:

```text
CONFIRMED
→ GENERIC COMMAND-AUTHORITY SEMANTICS NOW DERIVED FROM CURRENT LAW
→ EXACT FP-006 COMMAND/ROLE/APPROVAL ASSIGNMENTS STILL OPEN
→ CLASSIFICATION: OPERATIONS_POLICY_GAP
→ UPSTREAM PROMOTION ONLY FOR NEW/CHANGED BUSINESS POWERS
```

This is a narrowing, not closure.

---

# 77. Minimum FP-006 command-matrix rows now known to be required

This table intentionally does **not** assign final people/roles where current law is silent.

| Consequential seam | Owner | Already-governed boundary | Still required before FP-006 final contract |
|---|---|---|---|
| payment reconciliation / refund / dispute handling | Commerce | provider evidence is not Commerce truth; owner action required | exact request/approve/execute/reconcile actor mapping and any command-specific separation rule |
| missing/incorrect access consequence | Entitlements | source-specific owner convergence; no direct Finance/Support access toggle | who may trigger recovery/reconciliation and any permitted non-paid grant sources |
| identity recovery/reconciliation / exceptional access | Identity & Access | scoped grant, reason, current authority, no manufactured external business truth | exact request/approver/executor routes for FP-006 |
| assessment technical recovery | Temperament | immutable assessment truth; methodology authority remains separate | exact technical-recovery actor mapping only; no methodology power inferred |
| safety/Plan operational intervention | Safety / Plans respectively | source ownership and professional/safety authority remain separate | only the exact FP-006 operator actions already authorised upstream; otherwise STOP upstream |
| release stop / resume / expansion | governed release authority | `DEC-291` authority split and immediate scoped safety/technical stop | named/scoped command mapping, evidence and re-entry execution route |
| privileged/break-glass production access | Identity/Security + evidence | named/MFA/reason/scope/expiry/audit/alert/review; no Super Admin bypass | exact issuance/approval/revocation/expiry operational route |

---

# 78. Evidence obligations for consequential operator activity

Without choosing an Audit schema, FP-006 must be capable of proving, as applicable:

- named human actor;
- effective role/capability/grant and relevant scope at action time;
- authentication/step-up assurance where required;
- purpose/reason code and bounded human-entered explanation where justified;
- request identity and requester;
- approver/approval identity when approval is required;
- executor identity;
- owner-Domain command/action class;
- target/source reference without copying unnecessary sensitive payload into generic evidence;
- expected/current source context needed to prove stale-action handling;
- logical obligation/idempotency identity;
- distinct execution-attempt identities;
- outcome classification: success, rejected, known failure, unknown, reconciled result;
- correction/compensation/supersession linkage where applicable;
- policy/definition/version references where material;
- privilege grant/expiry/revocation and post-access review for break-glass;
- participant communication status where the governing workflow requires participant notification.

Audit evidence does not make an unauthorised action lawful. The source Domain's transition remains the business authority.

---

# 79. Gap and delta result for this bounded pass

## New upstream deltas

**None.**

No genuinely new Product/Architecture/Domain policy class was discovered in this pass. Creating `OPS-UPD-008` would duplicate or overstate `OPS-UPD-003`.

## New gaps

**None.**

The unresolved human-command assignment work is the already-known `OPS-UPD-003` operations-policy gap. The pass made it substantially more precise.

## Existing delta changed materially

`OPS-UPD-003` is narrowed from “we need a broad authority matrix” to:

> Freeze only the minimum FP-006 consequential command matrix over existing lawful actions, preserving request/approve/execute/reconcile distinctions and owner-Domain authority; promote upstream only where an intended command would create a new business power or alter participant rights/safety/privacy/release semantics.

---

# 80. Focused convergence result

This bounded pass **converged**.

The pass found no new semantic class after pressure-testing:

- role labels versus capabilities;
- request versus approval versus execution;
- owner-Domain command boundaries;
- multi-role/separation-of-duties semantics;
- stale/revoked authority;
- unknown outcomes and retry;
- automation/manual races;
- work-state versus source-state closure;
- bulk actions;
- break-glass versus business override;
- evidence failure for exceptional broadening;
- immediate stop asymmetry;
- direct-database hotfix pressure.

The remaining blocker is concrete rather than exploratory:

> `OPS-UPD-003` requires the minimum FP-006 command/role/approval assignment policy over the lawful action set before FP-006 can safely finalise its operator contract.

That is **not** implementation work and **not** permission to create an Operations Domain.

Broad stream freeze remains blocked by the already-recorded upstream deltas and the still-required independent review. No PR is opened by this pass.
