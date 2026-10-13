# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.1.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.1.0`
- **Date:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** none — initial ledger
- **Purpose:** discover and pressure-test the consequential operational semantics required to run, support, correct, reconcile, measure, pause, resume and progressively release the real paid participant journey without staff, dashboards, providers or operating tooling becoming hidden business authority.
- **Primary downstream consumer:** FP-006 Controlled core operations and staged paid release, plus later Feature Packs that reuse the operational foundation.
- **Scope:** Product/domain semantics, operational authority boundaries, correction/reconciliation semantics, participant-support journeys, release/pilot semantics, evidence/proof routing, and cross-domain failure behaviour.
- **Explicit non-goals:** implementation; Ash Resource design; database/schema design; admin-dashboard design; support-ticketing product design; infrastructure selection; provider procurement; creation of an Operations/Support/Administration Domain; alteration of governed authority; opening a PR.
- **External evidence dates:** no new external/provider research performed in this version. Existing Paystack Pre-JIT working evidence is reused only where necessary; its empirical provider validation remains explicitly incomplete.
- **Current overall disposition:** `IN_PROGRESS / FIRST NORMAL-JOURNEY BATCH COMPLETE / NOT FROZEN`.

---

## 0. Append-only discipline

This ledger is historical reasoning evidence.

- `v0.1.0` is the initial authority extraction, ownership map, hypotheses, correction taxonomy seed and normal-journey pressure-test batch.
- Semantic additions or revisions require a MINOR successor and preservation of this file.
- PATCH successors may correct only non-semantic provenance, formatting, path, SHA or citation defects.
- If a conclusion is later wrong, preserve it and append an explicit correction rather than rewriting history.
- No conclusion in this ledger becomes Product, Architecture, Domain, Roadmap or JIT authority merely by being accepted here.

---

# 1. Exact repository baseline and authority route

## 1.1 Live repository resolution

The live `main` branch was independently resolved before discovery work.

```text
main = 086ade7b28c000de1c387acb9760e5eb08bb0413
```

The prompt-creation provenance SHA is therefore still current at the start of this stream; that was verified rather than assumed.

A dedicated branch was created from that exact baseline:

```text
prejit/operations-support-pilot
```

No write has been made to `main`.

## 1.2 Current routed authority

Resolved from live `docs/00_platform/README.md` and cross-checked against `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when frontend/operator interaction semantics are relevant.

Current supporting engineering authority is routed through:

- `reference/ENGINEERING_STANDARDS_v1.0.1.md`

Deep `reference/` and `archive/` material is not default authority and is loaded only when source-level tracing requires it.

## 1.3 Current programme state relevant to this stream

Current Open Work records:

- Product/targeted amendment and Foundation Evaluation Pass 2 as complete/closed;
- 20 approved Domains and 17 Feature Packs;
- HARDEN-02 complete/certified;
- Engineering Standards promotion complete/certified;
- FP-001 PMR reconciliation complete/certified;
- Identity & Access JIT dossier current;
- Communications JIT dossier current;
- Communications finalisation still blocked;
- Privacy & Consent, Content & Media and Audit & Evidence conditional/pending explicit adjudication for FP-001;
- Analytics not required for FP-001;
- Phase 7C blocked/not started;
- proof classification not finalised;
- executable development blocked until Phase 8 entry conditions pass.

This Pre-JIT stream does not alter that programme state.

---

# 2. FP-001 through FP-006 operational dependency extraction

The current Roadmap preserves the core sequence:

```text
FP-001 trusted bilingual entry + verified identity
→ FP-002 purchase → verified payment → entitlement
→ FP-003 temperament provenance → assessment → immutable report
→ FP-004 health intake → safety → eligibility
→ FP-005 safe plan → purchased library → feedback
→ FP-006 controlled operations → internal / paid pilot release
```

Operationally relevant consequences:

- **FP-001:** Support may resolve ordinary account-access problems, but Identity & Access remains authority for Account, session, recovery and PMR truth.
- **FP-002:** Commerce owns purchase/payment/refund/dispute truth; Entitlements owns current access/right truth; browser/provider state is evidence only.
- **FP-003:** Temperament owns attempts, answers, raw result and report history; immutable result history cannot be reset by Support convenience.
- **FP-004:** Health Records owns facts; Safety & Eligibility owns eligibility/restriction/override truth. Support/Commerce cannot create eligibility.
- **FP-005:** Plans & Nutrition owns Plan generation/version/provenance. A personalised-plan right is not fulfilled by General Wellness or mere generation; fulfilment requires governed successful delivery.
- **FP-006:** named operators must be able to run, support, observe, correct, withdraw, reconcile and safely stop the approved core journey. FP-006 is the release/evidence boundary, not a generic Administration layer.

---

# 3. Governing operational doctrine

The following rules are treated as upstream constraints, not new findings:

1. Every durable business truth has exactly one Domain owner.
2. `Administration` is explicitly **not** a Domain.
3. Support/admin screens, queues, dashboards and timelines are projections; they do not create write authority.
4. Cross-domain action invokes the owning Domain.
5. Provider dashboards, Analytics, caches, PubSub and UI state do not become business truth.
6. Work is attention, not authority.
7. Queue visibility does not grant command authority.
8. Support sees minimum permitted context; sensitive health/professional information requires explicit current authority.
9. Routine impersonation is prohibited; any true impersonation would require separate governed design.
10. There is no universal Super Admin bypass.
11. Staff/practitioner privileged access requires scoped current authority; staff/practitioner MFA is mandatory.
12. Support may not directly overwrite historical truth in the database.
13. Corrections are record-type specific: profile update/history, additive assessment correction/new attempt, superseding Plan versions, professional addenda, financial credit/refund/adjustment, moderation-aware content changes, recalculated/inactivated derived flags.
14. Graceful degradation may use read-only, limited-capability or maintenance modes, but must never guess health, entitlement or payment truth.
15. Release expansion authority is split across product/commercial, clinical/safety and technical/operations; one authority cannot waive another authority's blocker.

---

# 4. Ownership map for operations and support

| Operational concern | Durable truth owner | Operator/support role |
|---|---|---|
| Account identity, sessions, recovery, PMR, privilege grants | **Identity & Access** | inspect minimum context; invoke permitted Identity actions |
| Consent, Full Deletion, export/retention orchestration | **Privacy & Consent** | route/request governed privacy action; never directly delete cross-domain truth |
| Assessment attempt/result/current profile | **Temperament** | explain permitted status; request owner action; never edit raw result |
| Health/lifestyle facts | **Health Records** | minimum-necessary read only where authorised; correction through Health owner |
| Eligibility/restriction/safety override | **Safety & Eligibility** | route concern; only scoped safety authority may decide/override |
| Plan generation/version/delivery truth | **Plans & Nutrition** | inspect status; retry/reconcile only through governed Plan operation |
| Purchase/payment/refund/dispute | **Commerce** | Finance/support invoke permitted commercial action; provider state is evidence |
| Current access/right/credit | **Entitlements** | explain source/provenance; grant/revoke/restore only through Entitlements authority |
| Message intent/delivery attempt/provider evidence | **Communications** | resend/retry only under Communications/source-owner semantics |
| Derived metrics/dashboards | **Analytics** | observe/measure; never repair business truth from analytics |
| Cross-cutting evidence | **Audit & Evidence** | append/read under policy; never use Audit as business state |
| Release/incident evidence | **Audit & Evidence** as evidence; decision authority remains governed owner(s) | record decision/evidence; Audit does not itself authorise release |

**Rejected model:** a new `Operations`, `Support`, `Administration`, `Case Management` or `Reconciliation` Domain merely because staff need coordinated views/actions.

A later JIT may justify owner-specific work/case concepts. That does not transfer underlying truth ownership.

---

# 5. Initial evidence hierarchy for this stream

Use evidence in this order:

```text
current governed NewYou authority
→ current certified JIT/proof material where applicable
→ current working Pre-JIT evidence
→ external/provider evidence
→ inference in this ledger
```

Working packs consulted selectively in this first pass:

- Commerce / Entitlements / recurring membership compact contract;
- Paystack FP-002 compact contract;
- Privacy / Consent compact contract;
- Health / Safety / Plans compact contract;
- Audit & Evidence compact contract;
- current Communications JIT semantics where retry/resend distinction matters.

These are evidence only. Where they expose an upstream gap, this ledger records the gap instead of promoting the working conclusion into authority.

---

# 6. Initial hypotheses to attack

These are hypotheses, not conclusions.

- **H1:** Most ordinary support journeys can be handled by a composed operator projection plus owner-Domain commands; no Operations Domain is needed.
- **H2:** The biggest operational risk is not missing CRUD capability but confusing investigation evidence with mutation authority.
- **H3:** The correction vocabulary is currently semantically fragmented enough that FP-006 JIT could accidentally turn “fix it” into direct mutation unless correction classes are explicit.
- **H4:** Product Law now governs who counts in the first paid cohort and how metrics are defined, but the atomic pilot-admission boundary under concurrency/in-flight payment may still be unspecified.
- **H5:** Pausing new admissions can usually be narrower than pausing fulfilment already owed to paid participants.
- **H6:** Operator concurrency must be made safe by Domain invariants/current revalidation, not UI button disabling or case assignment alone.
- **H7:** Operational evidence must prove both business outcome and human intervention burden without making Analytics/Audit the business owner.

---

# 7. Correction taxonomy — seed v0.1.0

This taxonomy is deliberately semantic. It does not imply universal Resources/actions.

| Term | Working semantic distinction | Owner rule / historical effect |
|---|---|---|
| **retry** | repeat execution for the same still-authorised logical operation after known retryable failure | must not manufacture a new business obligation; owner revalidates current authority |
| **reconciliation** | converge owner truth from durable platform state plus legitimate external/async evidence where outcome is unresolved or inconsistent | owner decides current truth; dashboard/provider evidence cannot decide it directly |
| **correction** | rectify or qualify a business fact that was wrong/incomplete under that record type's correction law | owner-specific; history preserved where materially required |
| **override** | exceptional governed transition by the Domain authority empowered to decide despite ordinary automated result/rule | never means “Super Admin force”; explicit reason/scope/evidence required |
| **replacement** | issue a new immutable/superseding artifact/version rather than edit historical artifact in place | common for Plans/content; predecessor remains historical |
| **refund** | Commerce-owned obligation/outcome returning money under commercial rules | does not itself define entitlement truth; Entitlements receives governed consequence |
| **financial reversal** | later Commerce truth that reverses/corrects an earlier economic effect, often after provider/dispute evidence | earlier historical payment may remain true; reversal is a later truth |
| **entitlement revocation** | Entitlements-owned ending of a specific current right/source | must not erase delivery history or unrelated valid sources |
| **entitlement restoration** | Entitlements-owned restoration/recreation of current access only when a valid governed source consequence permits it | provider success/dashboard never restores access directly |
| **re-execution** | another execution attempt of work whose business intent already exists | attempt identity may be new; business consequence must remain repeat-safe |
| **cancellation** | owner-authorised termination of an open/future obligation or lifecycle path | not automatically refund, deletion, reversal or revocation unless governing law says so |
| **suspension** | reversible restriction of current capability/right while underlying history/contract may remain | source-scoped; restoration requires governed re-evaluation |
| **withdrawal** | revocation/ending of a permission, content availability or other owner-specific authority | object must be named; consent withdrawal, content withdrawal and service withdrawal are not one lifecycle |
| **deletion** | Privacy-orchestrated data-right lifecycle causing owner-specific deletion/anonymisation/suppression | not correction; cannot be reduced to deleting an Account row |
| **support annotation** | internal contextual note for permitted support/work purpose | never business truth, professional record or audit evidence merely because a staff member wrote it |

### 7.1 Immediate anti-patterns

Reject:

- `force_success` for a payment, assessment, safety decision or Plan;
- direct operator edit of provider status into Commerce truth;
- direct Finance grant of Entitlement because “payment looks fine”;
- direct Support edit of assessment result or safety outcome;
- generic `reset` that erases completed history;
- direct SQL repair as an ordinary business API;
- using a support note as the source of an entitlement/refund/safety decision;
- using Audit to reconstruct or overwrite source-domain current truth.

---

# 8. Pressure-test batch A — normal operational journeys

## OPS-PT-001 — Participant asks where she is in the purchase journey

**Scenario class:** normal / operator

**Why it matters**  
A participant-facing/support answer can easily collapse payment, entitlement and fulfilment into one vague “purchase status,” making the support screen hidden authority.

**Relevant current authority**  
`DEC-258`, `DEC-263`, `DEC-264`; `DEC-299...DEC-300`; Domain Map ownership matrix; Roadmap FP-002/FP-005/FP-006; Platform Operating Model §§2, 5, 8, 19.

**Owning Domain(s)**  
Commerce; Entitlements; then the relevant fulfilment owner (Temperament or Plans & Nutrition). Communications only for notification delivery state.

**Preconditions**  
A known Account/order exists; operator is authorised to see the participant's minimum necessary commercial context.

**Exact scenario / timeline**

```text
participant asks “Where is my purchase?”
→ Support looks up Account/order using governed identifier
→ composed projection reads current Commerce truth
→ reads current Entitlement truth
→ reads relevant fulfilment/delivery truth
→ explains what is known, pending, delivered or blocked
```

**Expected invariant(s)**

- one screen may compose multiple truths but owns none of them;
- provider/browser state cannot be presented as authoritative payment success;
- “paid” cannot be silently presented as “access granted” or “benefit delivered”;
- pending/unknown remains pending/unknown.

**Questions under test**

- Can Support answer accurately without a generic PurchaseJourney authority?
- Can the answer identify which owner is blocking progress?

**Adversarial variants**

- provider dashboard says success but Commerce unresolved;
- Commerce verified, Entitlement pending;
- Entitlement valid, Plan still open;
- email says delivered but participant has no current access.

**Analysis**  
Current authority is sufficient for the semantic split. The operator experience needs a curated journey projection, but that projection must cite/derive owner state and cannot expose an editable synthetic status.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
FP-006 JIT must define the minimum support projection and stale-state re-read behaviour; later proof must show it cannot fabricate success.

**Follow-up**  
Mutate with stale operator page and concurrent owner transition in the concurrency batch.

---

## OPS-PT-002 — Participant asks why access is missing after payment

**Scenario class:** normal / financial / operator / recovery

**Why it matters**  
The temptation is for Support or Finance to “just grant access,” collapsing Commerce and Entitlements.

**Relevant current authority**  
`DEC-258`, `DEC-299`, `DEC-300`; Roadmap FP-002 exit condition; Domain Map Commerce/Entitlements split; working CER/Paystack evidence.

**Owning Domain(s)**  
Commerce for payment truth; Entitlements for current right; downstream product owner for fulfilment if access exists but value not delivered.

**Preconditions**  
Participant claims to have paid; operator can identify the order/attempt safely.

**Exact scenario / timeline**

```text
claimed payment
→ inspect Commerce + provider evidence
→ if Commerce unresolved: reconcile through Commerce
→ if Commerce verified but right absent: invoke/recover durable Entitlements consequence
→ if right valid but product unavailable: inspect owning fulfilment Domain
```

**Expected invariant(s)**

- Finance does not grant Entitlements directly;
- Support does not mark payment successful;
- repeated recovery creates at most the intended component right;
- participant is not encouraged to pay again while truth is unresolved.

**Questions under test**  
Does current law permit a lawful repair path without direct mutation?

**Adversarial variants**

- duplicate callbacks;
- worker crashed after Commerce commit;
- entitlement consequence ran twice;
- participant starts another checkout while first is unresolved.

**Analysis**  
The semantic repair is already structurally clear: reconcile the owner truth, then re-run/converge the owner consequence. Exact work/action design remains JIT.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `PHASE8_EXECUTABLE` + `EMPIRICAL_PROVIDER`

**Upstream delta:** none.

**Evidence still required**  
`OQ-004` empirical provider evidence; executable crash/replay proof; operator permission mapping.

**Follow-up**  
Commerce/Entitlement adversarial batch.

---

## OPS-PT-003 — Finance investigates a legitimate payment

**Scenario class:** normal / financial / operator / privacy

**Why it matters**  
Finance needs enough evidence to resolve money without gaining unrelated participant-health authority or treating the provider dashboard as truth.

**Relevant current authority**  
Domain Map Commerce ownership; Platform Operating Model Finance role; `DEC-292`; `OQ-004`; Paystack working contract evidence-minimisation rules.

**Owning Domain(s)**  
Commerce. Audit & Evidence may retain governed evidence. Entitlements only when a commercial consequence is lawfully established.

**Preconditions**  
Known order/payment reference; Finance actor currently authorised.

**Exact scenario / timeline**

```text
Finance opens commercial case
→ reads accepted order snapshot + Commerce state
→ reads minimum provider evidence
→ reconciles through Commerce-owned operation
→ any access consequence goes to Entitlements
```

**Expected invariant(s)**

- no health/temperament/Plan content is required for ordinary payment investigation;
- provider dashboard/API is evidence only;
- Finance cannot edit assessment/safety/Plan/access truth;
- reconciliation outcome is durable and repeat-safe.

**Questions under test**  
Can Finance prove what happened using financial evidence alone?

**Adversarial variants**

- provider data includes tempting customer metadata;
- operator has Finance + another role;
- dispute asks for sensitive evidence.

**Analysis**  
Current ownership and privacy doctrine are sufficient. The exact Finance permission envelope and evidence views remain JIT/security proof.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE` + `EMPIRICAL_PROVIDER`

**Upstream delta:** none.

**Evidence still required**  
Provider validation; role/field-policy proof; disclosure minimisation for disputes.

**Follow-up**  
Privilege/abuse batch.

---

## OPS-PT-004 — Support retries or resends a permissible delivery

**Scenario class:** normal / communications / operator / recovery

**Why it matters**  
“Resend” can mean retrying a delivery attempt or creating a new source-owned challenge/intent. Collapsing the two breaks idempotency and security semantics.

**Relevant current authority**  
`DEC-261...DEC-264`; current Communications JIT dossier; current Identity dossier for verification/recovery source authority; `OQ-036` remains open for provider/channel policy.

**Owning Domain(s)**  
Communications owns MessageIntent/DeliveryAttempt state; source Domain owns the underlying business/security intent.

**Preconditions**  
The message is permitted and operator is authorised to request the action.

**Exact scenario / timeline**

- known non-delivery retry of the same business message: same MessageIntent, new DeliveryAttempt for a new provider operation;
- participant asks for a fresh verification/recovery challenge: source owner creates the new challenge; this is a new MessageIntent;
- repeated transmission of an already-identified provider operation is not casually relabelled as a new attempt unless provider contract proves the identity semantics.

**Expected invariant(s)**

- Support cannot manufacture a new security challenge inside Communications;
- infrastructure retry does not create new business intent;
- resend action revalidates current source authority and channel policy;
- delivery success is not business-success authority for the source event.

**Questions under test**  
Can Support safely “resend” without the UI hiding the semantic distinction?

**Adversarial variants**

- original challenge expired while support page is stale;
- participant changed primary email;
- first provider outcome is ambiguous;
- operator clicks resend twice.

**Analysis**  
The core distinction is already clear in current JIT material. FP-006 must preserve source-owner semantics rather than offering a generic universal resend button.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE` + `EMPIRICAL_PROVIDER`

**Upstream delta:** none.

**Evidence still required**  
`OQ-036` provider/channel policy and executable concurrency/provider-ambiguity proof.

**Follow-up**  
Communications recovery batch.

---

## OPS-PT-005 — Participant requests a correction

**Scenario class:** normal / operator / privacy

**Why it matters**  
A generic “edit participant” capability would violate multiple immutable histories and owner boundaries.

**Relevant current authority**  
Product Law §21I.22 Corrections; Domain Map; Platform Operating Model §§2, 8.

**Owning Domain(s)**  
Depends on the fact: Identity, Health Records, Temperament, Plans, Commerce, Community, Professional Care, etc.

**Preconditions**  
Participant identity/control and correction authority established to the level required for the specific record.

**Exact scenario / timeline**

```text
participant identifies disputed fact
→ Support classifies record type and requested correction
→ owner Domain applies its correction law
→ prior history/evidence preserved as required
→ derived projections recalculate/inactivate
```

**Expected invariant(s)**

- no universal correction API owns all facts;
- immutable assessment/Plan/financial history is not overwritten;
- Support annotation is not the correction itself;
- derived views follow corrected owner truth.

**Questions under test**  
Is “correction” sufficiently specified at Product level to stop JIT inventing destructive edits?

**Adversarial variants**

- participant says an assessment result is “wrong” versus an answer was incorrectly recorded;
- health fact was once true but changed later;
- operator selected wrong participant;
- automated recalculation races human correction.

**Analysis**  
Product Law already rejects one-size-fits-all correction. Detailed record-type actions belong to owner JIT. A later batch must decide which operator correction classes need explicit approval/separation-of-duties policy.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none yet.

**Evidence still required**  
Per-owner correction lifecycles, permission matrix, concurrency and evidence requirements.

**Follow-up**  
Dedicated correction taxonomy pressure-test batch.

---

## OPS-PT-006 — Participant requests refund or cancellation

**Scenario class:** normal / financial / operator

**Why it matters**  
Refund, cancellation, reversal and access revocation are different truths. A support workflow can easily collapse them into “cancel/refund.”

**Relevant current authority**  
`DEC-045`, `DEC-299`, `DEC-300`, `DEC-307...DEC-308`; Product Law §§21L, 21T; Domain Map Commerce/Entitlements split; Roadmap FP-002/FP-006.

**Owning Domain(s)**  
Commerce owns refund/cancellation commercial truth; Entitlements owns access consequence; Safety owns eligibility; Plans/Temperament own delivered-history truth.

**Preconditions**  
Known order/contract and participant/purchaser authority appropriate to the request.

**Exact scenario / timeline**

```text
request received
→ classify request: cancellation vs refund vs component refund vs correction
→ Commerce evaluates governing commercial rule
→ Commerce commits any money/contract consequence
→ Entitlements converges affected current right
→ delivered immutable history remains truthful
```

**Expected invariant(s)**

- refund does not erase the original payment/delivery history;
- cancellation does not automatically mean immediate refund;
- Entitlements does not infer access consequence from provider callback alone;
- General Wellness plan-component choice follows the governed 14-day retain/refund rule.

**Questions under test**  
Can Support initiate a request without acquiring Commerce authority?

**Adversarial variants**

- refund succeeds while entitlement still appears active;
- duplicate refund request;
- dispute arrives during refund investigation;
- participant is purchaser for someone else.

**Analysis**  
Core semantics are strong. Exact operator authority, dual-control thresholds and unknown-provider-outcome handling remain JIT/operations/security concerns.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE` + `EMPIRICAL_PROVIDER`

**Upstream delta:** none.

**Evidence still required**  
Operator permissions; provider empirical refund/dispute evidence; concurrency proof.

**Follow-up**  
Commerce/Entitlements batch.

---

## OPS-PT-007 — Participant has paid but cannot see purchased benefit

**Scenario class:** normal / financial / recovery / operator

**Why it matters**  
“Access” and “fulfilment” can fail at different boundaries. Repair must preserve an owed paid right rather than falsely closing it.

**Relevant current authority**  
`DEC-299...DEC-300`; Product §21T.4; Roadmap FP-002/FP-005; HSP working evidence for generated vs fulfilled Plan distinction.

**Owning Domain(s)**  
Commerce → Entitlements → relevant fulfilment owner (Temperament or Plans & Nutrition).

**Preconditions**  
Commerce has verified successful payment or an accepted manual-payment truth; entitlement/product expectation is known.

**Exact scenario / timeline**

1. Verify Commerce truth.
2. Verify relevant Entitlement source and current validity.
3. Verify downstream fulfilment/delivery state.
4. Reconcile/retry only the missing owner consequence.
5. Keep paid right held where governing law says fulfilment has not succeeded.

**Expected invariant(s)**

- no double entitlement or double Plan/report;
- a technical delivery failure does not consume/close the paid right improperly;
- successful communication delivery is not product fulfilment;
- repair can survive worker/node restart.

**Questions under test**  
Where exactly is the owed service boundary, and which owner repairs it?

**Adversarial variants**

- Plan generated but final delivery failed;
- report delivered but email failed;
- entitlement valid but content version withdrawn;
- safety authority changes while fulfilment is in flight.

**Analysis**  
Owner boundaries are sufficient. Exact owner-specific recovery work remains JIT. FP-006 must expose durable unresolved obligations so support does not rely on inboxes or memory.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Owner-specific fulfilment terminal boundaries, recovery/reconciliation proof and operator visibility.

**Follow-up**  
Assessment + HSP operational batches.

---

## OPS-PT-008 — Participant has access; Support must explain its source

**Scenario class:** normal / operator / financial

**Why it matters**  
Access may come from purchase, bundle, grant, gift/sponsorship or later multiple valid sources. Support must explain provenance without inventing a source hierarchy.

**Relevant current authority**  
Domain Map Entitlements source/provenance ownership; `DEC-285`, `DEC-300`; Product §21L.18; working CER multi-source evidence.

**Owning Domain(s)**  
Entitlements owns current right and provenance; Commerce owns commercial source truth where applicable.

**Preconditions**  
Support is allowed to see the source class and minimum commercial context.

**Exact scenario / timeline**

```text
read current Entitlement
→ read its source/provenance
→ if commercial, reference Commerce source truth
→ explain current access without treating one source as global winner
```

**Expected invariant(s)**

- access explanation comes from Entitlements provenance, not provider/dashboard inference;
- ending one source must not remove another independently valid right;
- purchaser/sponsor visibility must not expose participant private health journey;
- a manual grant must carry governed reason/issuer/approval where required.

**Questions under test**  
Does a single “active because payment X” explanation remain truthful when multiple sources exist?

**Adversarial variants**

- purchase plus support_resolution grant;
- sponsored source revoked while purchased source remains;
- duplicate economic payment correction but one valid right survives.

**Analysis**  
Domain Law already gives Entitlements provenance authority. Multi-source exact convergence needs JIT/proof; the operator projection must never collapse provenance into one guessed source.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Multi-source source-specific revocation/restoration proof; minimum disclosure policy.

**Follow-up**  
Commerce/Entitlements source-race batch.

---

## OPS-PT-009 — Support escalates a legitimate payment issue to Finance

**Scenario class:** normal / operator / financial

**Why it matters**  
Escalation/work assignment can be mistaken for transfer of business authority.

**Relevant current authority**  
Platform Operating Model §§5–8; Domain Map; Commerce ownership.

**Owning Domain(s)**  
Commerce owns payment truth. The support/work projection may assign responsibility without owning the payment.

**Preconditions**  
Support has enough minimum context to identify that Finance/Commerce authority is required.

**Exact scenario / timeline**

```text
Support investigates
→ identifies financial authority needed
→ creates/updates governed work context or handoff projection
→ Finance acts through Commerce-authorised operation
→ result flows back to shared timeline/projection
```

**Expected invariant(s)**

- assignment changes responsibility, not truth ownership;
- internal note does not become Commerce state;
- Finance re-reads current Commerce state before acting;
- participant-facing explanation is separated from internal note/evidence.

**Questions under test**  
Can two roles collaborate without a generic case becoming business authority?

**Adversarial variants**

- Support continues acting while Finance begins;
- case reassigned twice;
- participant action changes state during escalation.

**Analysis**  
The Operating Model already treats Work as attention. Detailed handoff/work structures are JIT-only unless later pressure tests expose a missing policy rule.

**Semantic disposition:** `PASS`

**Proof route:** `JIT`

**Upstream delta:** none.

**Evidence still required**  
Work projection/current-state revalidation, permissions and concurrency proof.

**Follow-up**  
Operator concurrency batch.

---

## OPS-PT-010 — Participant requires safety or clinical escalation

**Scenario class:** normal / safety / privacy / operator

**Why it matters**  
Support must route urgent/safety concerns without becoming a clinical decision-maker or seeing unnecessary health detail.

**Relevant current authority**  
`DEC-012`, `DEC-073...DEC-095`, `DEC-255`, `DEC-288`, `DEC-291`; Product §21J privileged access, §21L.21/24; Domain Map Health/Safety/Professional split; HSP working contract.

**Owning Domain(s)**  
Health Records owns facts; Safety & Eligibility owns safety/eligibility/restriction/override; Professional Care owns an actual professional case/review when activated.

**Preconditions**  
Support receives a concern through an authorised channel.

**Exact scenario / timeline**

```text
Support recognises safety/clinical routing condition
→ records only minimum permitted support context
→ invokes governed Safety escalation/routing
→ scoped authorised clinical/safety actor sees required detail
→ owner decides restriction/override/referral
→ dependent Plans/actions revalidate current Safety authority
```

**Expected invariant(s)**

- Support does not diagnose or override Safety;
- Support role alone does not grant health-record access;
- Super Admin cannot bypass clinical authority;
- safety narrowing/stop remains possible even if unrelated operating tooling is degraded.

**Questions under test**  
Can Support safely route the issue while remaining outside clinical authority?

**Adversarial variants**

- Support agent also holds another role;
- urgent wording gate unresolved;
- safety restriction conflicts with active Plan;
- operator proposes break-glass for convenience.

**Analysis**  
Owner boundary is clear. `OQ-005`/`OQ-008` remain real clinical gates. Exact triage wording and escalation path must not be invented by FP-006 JIT.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `EXPERT_REVIEW` + `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Clinical matrix/urgent wording, scoped access proof, safety consequence proof.

**Follow-up**  
HSP and staff-misuse batches.

---

## OPS-PT-011 — Operator reviews first-pilot cohort status

**Scenario class:** normal / pilot / release / operator / concurrency

**Why it matters**  
FP-006 expansion depends on a trustworthy cohort boundary. A dashboard count must not become admission authority, and concurrent/late payments must not silently overrun the governed stage.

**Relevant current authority**  
`DEC-280`, `DEC-281`, `DEC-288...DEC-291`, `DEC-307...DEC-312`; Product §§21L.13–21L.24, 21T.5–21T.9; Roadmap FP-006; Domain Map Analytics/Audit non-authority rules.

**Owning Domain(s)**  
No Operations Domain. Commerce owns qualifying payment truth; relevant product/Entitlement owners own delivered rights; Analytics derives cohort evidence; Audit may record release decisions. The authority that admits/expands the pilot must remain explicitly governed by Product/release law.

**Preconditions**  
Pilot stage is open; some participants may be paid, pending, failed, refunded or otherwise excluded from paid-demand evidence.

**Exact scenario / timeline**

```text
operator sees “9 qualifying paid participants”
→ two legitimate checkouts/payment paths race
→ one/both provider outcomes may initially be ambiguous
→ stage boundary should remain governed
→ dashboard may lag
```

**Expected invariant(s)**

- only qualifying paid participation counts under Product Law;
- grants/staff/sponsored/100%-discount/manual entitlement do not count as paid demand;
- Analytics/dashboard count is derived evidence, not permission to admit another participant;
- provider success event itself is not release/admission authority;
- the 10→25→50 boundary cannot rely on staff memory or UI disable alone.

**Questions under test**

1. What exact event makes a person consume a pilot admission place?
2. Is admission tied to accepted checkout, verified payment, first paid benefit activation, or another governed point?
3. What happens when the boundary participant's payment is ambiguous and later reconciles?
4. What happens when the 11th purchase races the 10th?
5. What happens to an in-flight checkout when new admissions are paused?

**Adversarial variants**

- participant 10 and 11 pay simultaneously;
- 10 initially ambiguous, 11 verified first;
- 10 later reconciles successful after stage pause;
- qualifying participant later refunds/withdraws;
- same participant buys multiple qualifying products.

**Analysis**  
Current Product Law is now strong about **qualifying paid-demand evidence** and metric denominators, but this review has not found an explicit atomic **pilot admission-slot lifecycle** or an explicit rule for late/in-flight payment across a stage cap. JIT cannot safely choose this because it affects whether NewYou accepts a real commercial participant while a stage is capped/paused. A derived count alone is insufficient.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` then `JIT`/`PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-001`

**Evidence still required**  
Product/release decision on admission/count boundary; concurrency and payment-ambiguity proof after promotion.

**Follow-up**  
Dedicated pilot-count/admission batch.

---

## OPS-PT-012 — Release operator reviews unresolved problems before cohort expansion

**Scenario class:** normal / pilot / release / operator

**Why it matters**  
A green dashboard must not override mandatory blockers, and a red metric must not automatically force a Product conclusion beyond current law.

**Relevant current authority**  
`DEC-288...DEC-291`, `DEC-307...DEC-312`; Product §§21L.21–21L.24 and 21T; Roadmap FP-006.

**Owning Domain(s)**  
Each owner retains its truth. Product/commercial, clinical/safety and technical/operations authorities make their governed release decisions. Audit & Evidence may record decision evidence; Analytics supplies derived measurement.

**Preconditions**  
Current cohort has evidence; some issues may remain open.

**Exact scenario / timeline**

```text
assemble current owner facts + metric evidence + open critical work
→ each responsible authority assesses its blockers
→ no authority waives another authority's blocker
→ decision = proceed / iterate / repeat_pilot / pause / rollback as applicable
→ decision + evidence + reason + re-entry criteria recorded
```

**Expected invariant(s)**

- integrity blockers remain non-waivable by unrelated authority;
- non-integrity target miss does not automatically equal abandonment;
- counts and percentages remain visible; denominator definitions cannot be rewritten retroactively;
- dashboard freshness/error cannot be mistaken for zero/no blockers.

**Questions under test**  
Is current authority enough to prevent “founder says proceed” from overriding a clinical/security blocker?

**Adversarial variants**

- value target missed but all integrity criteria pass;
- unresolved security blocker with strong sales;
- dashboard stale during review;
- Day-90 evidence not yet mature.

**Analysis**  
Current Product Law is strong. Exact release evidence packet, query/projection and sign-off workflow belong to FP-006 JIT, not new Product Law.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `CONTROLLED_LIVE` + `RELEASE_ONLY`

**Upstream delta:** none.

**Evidence still required**  
Exact FP-006 release evidence map and later controlled-live evidence.

**Follow-up**  
Release/pause/resume batch.

---

## OPS-PT-013 — New admissions pause while existing paid participants continue owed service

**Scenario class:** normal / release / recovery / financial / safety

**Why it matters**  
“Pause the platform” is too broad. Stopping new sales should not automatically abandon an already-paid participant's lawful owed benefit, while some safety/technical incidents may require narrowing fulfilment too.

**Relevant current authority**  
`DEC-264`, `DEC-291`, Product §21L.24 rollback modes; `DEC-299...DEC-300`; Roadmap FP-006; Architecture degradation doctrine.

**Owning Domain(s)**  
Release authority controls stage/capability activation; Commerce owns accepted commercial obligations; Entitlements owns rights; each fulfilment owner decides current lawful fulfilment under its own guards; Safety may pause affected Plans.

**Preconditions**  
Some participants already have accepted/verified purchases or held paid rights; release operator decides to stop further admission.

**Exact scenario / timeline**

```text
release decision: stop new admission/sales
→ new purchase path closes at governed boundary
→ already-accepted obligations remain visible
→ each owed fulfilment continues if still lawful/safe
→ unsafe/failing capability may be separately paused
→ re-entry requires recorded criteria
```

**Expected invariant(s)**

- “stop new sales” is distinct from `read_only`, `stop_new_plan_generation`, safety pause and full maintenance;
- existing paid obligations are not silently cancelled by an admission pause;
- safety/current-authority revalidation still applies before fulfilment;
- in-flight/ambiguous checkout is not guessed into success/failure.

**Questions under test**

- At what boundary is an in-flight participant considered already admitted/owed service?
- Which modes permit continued fulfilment?
- Can a payment reconcile successfully after admission is paused, and what obligation follows?

**Adversarial variants**

- checkout initiated before pause, payment verifies after pause;
- provider returns unknown then succeeds later;
- Plan generation is unsafe but report delivery is safe;
- support load causes admission pause with no underlying integrity incident.

**Analysis**  
The narrow-rollback doctrine is already governed, but the in-flight admission boundary remains the same unresolved Product seam exposed by `OPS-PT-011`. FP-006 must not invent it.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` then `JIT`/`CONTROLLED_LIVE`

**Upstream delta:** `OPS-UPD-001`

**Evidence still required**  
Atomic admission/in-flight rule; capability-specific pause/resume matrix.

**Follow-up**  
Pause/resume and admission concurrency batch.

---

# 9. Candidate upstream deltas

## OPS-UPD-001 — Pilot admission boundary and concurrent/in-flight stage-cap semantics

> **WORKING / NON-AUTHORITATIVE**

**Originating PTs:** `OPS-PT-011`, `OPS-PT-013`

**Exact missing authority**  
Current Product Law defines the staged release, first-pilot maximum, qualifying paid-demand evidence, first-10 cohort composition and metric contracts. This pass has not found an explicit rule defining the durable **pilot-admission boundary** under:

- concurrent checkout/payment at the 10/25/50 stage edge;
- provider/payment ambiguity;
- late reconciliation;
- a pause beginning while checkout is in flight;
- later refund/withdrawal after lawful admission;
- multiple purchases by the same participant.

The missing rule is not “how to implement a counter.” It is which business event consumes/relinquishes a governed pilot place and what NewYou owes when payment/admission events cross a pause/cap boundary.

**Candidate working direction**  
Treat pilot stage admission as a separately governed release/commercial decision derived from authoritative Commerce/participant state, not a dashboard/provider count. Define an explicit concurrency-safe stage-cap invariant and an explicit in-flight rule. The final direction must state whether accepted purchase, verified payment or another event creates admission and whether a later refund removes historical cohort membership versus only current active participation.

**Affected authority**

- `00_PLATFORM_v1.6.0.md` §§21L.13–21L.14, 21L.21–21L.24, 21T.5–21T.9;
- `DEC-280`, `DEC-281`, `DEC-288...DEC-291`, `DEC-307...DEC-312`;
- Roadmap FP-002 / FP-006.

**Affected Domains**  
Commerce; Entitlements; Identity & Access for canonical participant identity; Analytics for derived cohort evidence; Audit & Evidence for release-decision evidence. **No Operations Domain.**

**Rejected alternatives**

- dashboard count as authority;
- Paystack/provider success count as authority;
- “first 10 callbacks win”;
- checkout-start reservation invented by JIT without Product authority;
- allowing Support/Finance to manually edit cohort count;
- removing a historical participant from cohort evidence merely because she later refunds, unless Product explicitly says so.

**Reason JIT cannot safely decide it**  
The choice determines when NewYou accepts a real paid participant into a capped stage and what contractual/operational obligations exist when a cap/pause is crossed. That is consequential Product/release policy, not implementation detail.

**Likely promotion destination**  
Product Law / Decision Register, with corresponding Roadmap FP-006 clarification if sequencing/exit semantics need it.

**Provider/expert dependency**  
Provider mechanics may influence implementability but must not decide Product semantics. Legal/commercial review may be required if the chosen boundary changes sale acceptance/participant obligations.

**Downstream Feature Pack impact**  
FP-006 primary; FP-002 checkout/reconciliation seam; later event/scarce-capacity work should not be assumed equivalent.

---

# 10. Unresolved gap register — v0.1.0

## OPS-GAP-001 — Pilot admission/count concurrency boundary

- **Classification:** `PRODUCT_AUTHORITY_GAP`
- **Origin:** `OPS-PT-011`, `OPS-PT-013`
- **Route:** `OPS-UPD-001` → governed promotion before FP-006 JIT freezes the affected semantics.
- **Status:** OPEN.

## OPS-GAP-002 — Consequential operator permission/approval matrix

- **Classification:** `OPERATIONS_POLICY_GAP`
- **Origin:** cross-cutting observation from `OPS-PT-002...010`.
- **Current evidence:** owner boundaries are governed, but the complete Support/Finance/Super Admin/clinical operator command matrix, separation-of-duties points and approval thresholds are not yet pressure-tested.
- **Route:** dedicated correction/privilege batch. Do **not** create an upstream delta until that batch proves a real semantic omission rather than JIT policy detail.
- **Status:** OPEN / NOT YET PROVEN UPSTREAM.

## OPS-GAP-003 — Exact support/work representation

- **Classification:** `JIT_ONLY`
- **Origin:** normal journeys.
- **Current evidence:** Operating Model already says Work is a projection, not universal Task authority.
- **Route:** FP-006 JIT only if/when the concrete workflow requires it.
- **Status:** DEFERRED CORRECTLY.

## OPS-GAP-004 — Paystack one-off operational empirical proof

- **Classification:** `PROVIDER_EMPIRICAL_GAP`
- **Origin:** `OPS-PT-002`, `003`, `006`.
- **Current evidence:** Paystack Pre-JIT documentary/provider-independent contract is stabilised, but empirical provider validation remains not executed. `OQ-004` remains open.
- **Route:** existing Paystack empirical plan / FP-002 proof. No duplicate provider research is created here.
- **Status:** OPEN / REUSED EXISTING GATE.

## OPS-GAP-005 — Retention/deletion/restore release gates

- **Classification:** `EXPERT_GATE`
- **Origin:** FP-006 current gate manifest, relevant to participant support and recovery.
- **Current evidence:** `OQ-009`, `OQ-029...OQ-032` remain current. Privacy Pre-JIT evidence clarifies semantics but does not resolve legal/operations gates.
- **Route:** existing expert/Privacy/Architecture/Operations gates.
- **Status:** OPEN / REUSED EXISTING GATES.

## OPS-GAP-006 — Notification provider/channel release policy

- **Classification:** `PROVIDER_EMPIRICAL_GAP`
- **Origin:** `OPS-PT-004` and FP-006 release readiness.
- **Current evidence:** Communications dossier is current, but `OQ-036` remains open for launch provider/channel policy.
- **Route:** existing `OQ-036`; no new provider decision here.
- **Status:** OPEN / REUSED EXISTING GATE.

---

# 11. Batch A conclusions

## 11.1 What held up

The ordinary support journeys strongly support **H1**: NewYou does not need an Operations/Support Domain to operate the core journey. A composed operating surface can remain a projection while commands go to Identity, Commerce, Entitlements, Temperament, Health, Safety, Plans, Communications and Privacy owners.

The current authority is also materially stronger than the old orientation snapshots on:

- first-cohort composition;
- metric definitions;
- paid-demand exclusions;
- refund reason classification;
- Day-7/30/90 evidence maturity;
- economics evidence;
- cross-functional release authority;
- narrow rollback modes.

These are **not** gaps and must not be re-invented downstream.

## 11.2 What did not hold up

**H4 is provisionally confirmed:** qualifying participant evidence is governed, but the atomic pilot-admission boundary under concurrency/in-flight payment has not yet been found in current authority. This is consequential enough to justify `OPS-UPD-001` rather than a JIT guess.

## 11.3 What remains deliberately unresolved

This first batch does **not** yet claim that:

- the operator permission matrix is sufficient;
- correction/override semantics are complete;
- cross-domain manual-vs-automation races are safe;
- pilot pause/resume modes are complete;
- degradation classifications are complete;
- staff misuse is sufficiently constrained;
- second-pass adversarial coverage is complete.

---

# 12. Next highest-value pressure-test batch

Next MINOR successor should attack **correction + Commerce/Entitlements operational seams**, including:

1. verified payment but entitlement delayed;
2. entitlement visible while Commerce unresolved;
3. duplicate successful collection;
4. refund after entitlement;
5. refund completed while access still active;
6. dispute/chargeback during support investigation;
7. provider/browser disagreement with Commerce;
8. late callback after manual investigation;
9. manual operator correction racing reconciliation;
10. Finance attempting direct access grant;
11. Support attempting to mark payment successful;
12. late reconciliation after participant was told payment failed;
13. multiple entitlement sources with one source revoked;
14. each correction-taxonomy class against duplicate/retry/unknown-outcome semantics.

The objective is to determine whether `OPS-GAP-002` is truly Product/operations policy, Domain/JIT detail, or not a real gap.

---

# 13. v0.1.0 disposition

```text
NORMAL JOURNEY SEMANTIC COVERAGE: STARTED / 13 PRESSURE TESTS
NEW UPSTREAM DELTAS: OPS-UPD-001
OPEN GAPS: OPS-GAP-001...006
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
BROAD PRE-JIT FREEZE: NOT READY
```
