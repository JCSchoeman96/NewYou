# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.2.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.2.0`
- **Date:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.1.0.md`
- **Purpose:** continue the append-only semantic discovery ledger with a focused correction + Commerce / Entitlements operational pressure-test batch.
- **Scope:** all v0.1.0 scope plus financial/reconciliation/operator correction seams.
- **Explicit non-goals:** unchanged from v0.1.0; no implementation, no authority amendment, no Operations/Support/Admin Domain, no PR.
- **External evidence dates:** no new external/provider research performed. Current Paystack Pre-JIT working contract is reused as non-authoritative evidence; provider empirical validation remains blocked/not executed.
- **Current overall disposition:** `IN_PROGRESS / NORMAL-JOURNEY + COMMERCE-CORRECTION BATCHES COMPLETE / NOT FROZEN`.

---

# 0. Append-only successor rule

This successor is the next append in one logical deep ledger.

**The entire substantive reasoning of v0.1.0 remains part of the current reasoning record and is not superseded.** The predecessor is preserved byte-for-byte on the same branch. Read:

```text
v0.1.0 §§0–13
→ then this v0.2.0 append
```

No v0.1.0 conclusion is silently rewritten here. Where v0.2.0 refines a prior gap, the refinement is explicit below.

### v0.2.0 semantic additions

- `OPS-PT-014...OPS-PT-027`
- `OPS-UPD-002...OPS-UPD-003`
- `OPS-GAP-007...OPS-GAP-009`
- explicit adjudication of v0.1.0 `OPS-GAP-002`
- correction-taxonomy refinement for unknown outcome, concurrency and compensation

The live `main` SHA was rechecked before this batch and remained exactly `086ade7b28c000de1c387acb9760e5eb08bb0413`.

---

# 14. Batch B objective — correction + Commerce / Entitlements

This batch attacks a common operational anti-pattern:

> “An operator sees that the system is wrong, so give the operator a field/button that makes the state look right.”

That is unsafe for NewYou.

The pressure test instead asks, for every correction:

1. What durable truth is wrong or unresolved?
2. Which Domain owns it?
3. Is this retry, reconciliation, correction, compensation, override, cancellation, suspension, revocation or restoration?
4. Who may request the action?
5. Who may approve/execute it?
6. What is the logical idempotency identity?
7. What happens if outcome is unknown?
8. What if the command is duplicated?
9. What if automation acts concurrently?
10. What historical evidence must remain?
11. What must never be edited directly?

The batch reuses current governed `DEC-299` and `DEC-300`, current Commerce/Entitlements Domain ownership, and the non-authoritative CER and Paystack working packs. Working evidence is not promoted into law here.

---

# 15. Correction taxonomy refinement — v0.2.0

## 15.1 Correction versus compensation

A later action is not automatically a correction of the earlier event.

Examples:

- a legitimate payment followed by a refund = two true commercial events, not “the payment was wrong”;
- a legitimate entitlement followed by source-scoped revocation = two true entitlement events;
- a legitimate Plan followed by a safety replacement = predecessor remains historically true and a new version/consequence follows;
- an operator note saying “fixed” changes no business truth.

**Working rule:** prefer `compensating consequence` when the earlier event remains historically true; reserve `correction` for an earlier assertion that was wrong/incomplete under the owning Domain's correction law.

## 15.2 Unknown outcome is a first-class operational condition

A timeout, lost response or ambiguous provider acknowledgement is not permission to choose whichever terminal state is convenient.

For consequential operations:

```text
known retryable failure
→ retry may be lawful

known success
→ do not repeat the business consequence

unknown / ambiguous
→ preserve unresolved obligation
→ reconcile/read authoritative evidence
→ only then choose a lawful next action
```

This is especially material for payment, refund, reversal, entitlement grant/revoke/restore and privacy deletion.

## 15.3 Manual action is not a second write path

“Manual correction” must mean an authorised human invokes an explicit owner-Domain business operation under current guards.

It must not mean:

- edit the persisted state directly;
- bypass the owning Domain;
- set provider/business state to the operator's preferred answer;
- skip concurrency/current-state validation;
- suppress historical evidence.

## 15.4 Operator command and work-state dimensions remain separate

A support/finance work item may be `IN_PROGRESS` while the underlying Commerce outcome is already resolved, or a Commerce outcome may remain unresolved after the staff handoff ends.

Do not collapse:

```text
work assignment/status
operator command admission/outcome
source-Domain lifecycle
provider attempt/evidence
participant communication status
```

No universal “case resolved = business resolved” invariant is authorised.

---

# 16. Pressure-test batch B

## OPS-PT-014 — Verified payment but Entitlement consequence is delayed

**Scenario class:** failure / recovery / financial

**Why it matters**  
A successful Commerce transition can leave an owed cross-domain consequence incomplete after crash, backlog or worker failure.

**Relevant current authority**  
`DEC-258`, `DEC-299`, `DEC-300`; Domain Map Commerce → Entitlements command edge; Roadmap FP-002; Architecture durable consequence doctrine.

**Owning Domain(s)**  
Commerce owns verified payment; Entitlements owns grant/right truth.

**Preconditions**  
Commerce has durably verified and accepted the payment under the order contract; intended entitlement consequence is known.

**Exact scenario / timeline**

```text
Commerce payment becomes verified
→ durable entitlement consequence exists/is owed
→ process crashes or consequence is delayed
→ participant sees no right
→ Support/Finance investigates
→ recovery replays/converges Entitlements consequence
```

**Expected invariant(s)**

- Commerce truth remains truthful during Entitlements delay;
- retry/recovery may not create duplicate rights;
- operator does not directly grant because “it should be there”;
- unresolved owed consequence remains discoverable across restart.

**Questions under test**  
Does support need a new authority to fix this?

**Adversarial variants**  
worker runs twice; operator triggers recovery while worker resumes; entitlement already exists but projection stale.

**Analysis**  
No new authority is required. This is owner-consequence recovery, not operator override.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Crash/restart, duplicate/reordered execution and entitlement convergence proof.

**Follow-up**  
Operator concurrency batch.

---

## OPS-PT-015 — Entitlement appears visible while Commerce is unresolved

**Scenario class:** failure / financial / recovery

**Why it matters**  
A projected “active” access flag can conceal either an invalid premature paid-source grant or a legitimate independent source.

**Relevant current authority**  
`DEC-299`, `DEC-300`; Domain Map Entitlement provenance; Product Law paid-demand/payment-before-access doctrine; working CER multi-source evidence.

**Owning Domain(s)**  
Entitlements owns each current right/source. Commerce owns commercial source truth.

**Preconditions**  
Operator observes access while the questioned payment source is unresolved.

**Exact scenario / timeline**

1. Read the Entitlement's source/provenance.
2. If it depends solely on the unresolved paid source, the paid-source grant is not justified by provider/browser evidence alone.
3. If another independent valid source exists, current access may legitimately remain active.
4. Reconcile only the questioned source; do not globally revoke access.

**Expected invariant(s)**

- effective access cannot be explained from a generic boolean alone;
- one unresolved payment source does not erase another valid source;
- provider success cannot retroactively justify an already-invalid direct grant without Commerce reconciliation.

**Questions under test**  
Can operators distinguish “bad paid-source grant” from “valid access via another source”?

**Adversarial variants**  
goodwill grant + unresolved purchase; stale cache; source revoked during investigation.

**Analysis**  
The provenance boundary is governed. Exact multi-source convergence representation is downstream, but source-specific reasoning is mandatory.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Source-specific convergence and projection-staleness proof.

**Follow-up**  
`OPS-PT-026`.

---

## OPS-PT-016 — Two genuine successful collections for one accepted purchase

**Scenario class:** financial / concurrency / recovery

**Why it matters**  
Provider/API idempotency cannot be assumed to eliminate every distinct successful collection. NewYou must not turn excess money into a duplicate right.

**Relevant current authority**  
`DEC-290` zero duplicate charges/entitlements integrity target; `DEC-300` duplicate-payment correction leaves one valid right; `DEC-307` classifies `duplicate_or_erroneous_payment`; Paystack Pre-JIT §8 explicitly marks its stronger duplicate-collection remedy as an accepted working Product clarification **not yet Product Law**.

**Owning Domain(s)**  
Commerce owns both collections and any make-whole/refund obligation; Entitlements owns the one lawful right consequence.

**Preconditions**  
One accepted order; two distinct provider collections both genuinely succeeded.

**Exact scenario / timeline**

```text
accepted order
→ collection A success
→ collection B also genuinely succeeds
→ Commerce records truthful financial history
→ exactly one purchase fulfilment/right may be satisfied
→ excess economic effect requires governed remedy
```

**Expected invariant(s)**

- no second entitlement/credit/paid period arises merely from excess collection;
- historical money movements remain truthful;
- operator/provider arrival order cannot choose which business right is “real” arbitrarily;
- participant remedy cannot disappear because automated refund execution fails.

**Questions under test**

1. Does current Product Law explicitly require return of the full excess customer collection?
2. Does an owed make-whole obligation remain open when provider refund execution cannot complete?
3. Which source/amount is corrected when two genuine provider operations exist?

**Adversarial variants**  
second success appears late; one refund call times out; one collection later disputes; provider refund capacity unavailable.

**Analysis**  
Current Product Law clearly prevents duplicate entitlement and recognises duplicate-payment correction, but the current Paystack working pack itself records the precise excess-collection/make-whole rule as **not yet Product Law**. FP-002/FP-006 JIT should not be forced to invent whether NewYou owes the full excess and what remains true if provider execution fails. Reuse the existing working clarification rather than create a different one.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-002`

**Evidence still required**  
Governed promotion of the existing Paystack working clarification; empirical refund ambiguity/failure evidence.

**Follow-up**  
Provider/refund operational batch.

---

## OPS-PT-017 — Refund requested after Entitlement exists

**Scenario class:** financial / operator

**Why it matters**  
Refund eligibility is determined by Product/commercial law, while access consequence belongs to Entitlements. A single destructive “refund and delete access” operation can destroy history or unrelated sources.

**Relevant current authority**  
`DEC-045`, `DEC-299`, `DEC-300`, `DEC-308`; Domain Map; Roadmap FP-002/FP-006.

**Owning Domain(s)**  
Commerce for refund decision/outcome; Entitlements for current right; product owner for immutable delivered history.

**Preconditions**  
Payment and at least one entitlement component exist.

**Exact scenario / timeline**

```text
refund request
→ Commerce applies product-specific refund boundary
→ if allowed, Commerce establishes refund obligation/outcome
→ source-specific Entitlement consequence converges
→ prior payment/delivery/consumption history remains truthful
```

**Expected invariant(s)**

- refundability is not inferred from whether a UI “access” toggle is on;
- an unrelated valid entitlement source survives;
- no silent deletion of delivered report/Plan history where law preserves history;
- operator note is not the refund decision.

**Questions under test**  
Who can request/approve/execute the refund, and when is dual/elevated approval required?

**Adversarial variants**  
partial component use; bundle; purchaser differs from participant; refund request submitted twice.

**Analysis**  
Domain outcome semantics are clear. The actor/approval matrix is not yet sufficiently explicit for a real FP-006 operator workflow; that gap is confirmed across this and later tests.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` or supporting operating-policy promotion as appropriate, then `JIT`/`PHASE8_EXECUTABLE`.

**Upstream delta:** `OPS-UPD-003`

**Evidence still required**  
Consequential operator authority matrix; provider proof.

**Follow-up**  
Privilege/abuse batch.

---

## OPS-PT-018 — Refund completes while affected access still appears active

**Scenario class:** failure / financial / recovery / concurrency

**Why it matters**  
This is a cross-domain convergence failure, but blindly revoking all access may be worse than the original fault.

**Relevant current authority**  
`DEC-300`; Domain Map Commerce/Entitlements; CER source-specific evidence.

**Owning Domain(s)**  
Commerce owns verified refund; Entitlements owns source-specific current right.

**Preconditions**  
Commerce has a verified refund/reversal outcome; projection shows access.

**Exact scenario / timeline**

1. Read the refunded commercial component/source.
2. Read current Entitlement source set.
3. Apply/recover only the governed consequence for the affected source/component.
4. Preserve any independent valid source.
5. Refresh projections.

**Expected invariant(s)**

- refund completion is not itself an entitlement write;
- stale projection cannot extend invalid source authority;
- recovery is idempotent;
- independent sources are untouched.

**Questions under test**  
Can an operator safely repair access without a generic “revoke user” command?

**Adversarial variants**  
worker resumes concurrently; another valid source granted while refund runs; refund later found erroneous and reversed.

**Analysis**  
No Product gap. Correct repair is Entitlements convergence from current source-specific authority.

**Semantic disposition:** `PASS`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Deterministic source/component mapping and race proof.

**Follow-up**  
Multiple-source test.

---

## OPS-PT-019 — Dispute/chargeback arrives during Support/Finance investigation

**Scenario class:** financial / concurrency / operator / recovery

**Why it matters**  
A pending/contested external process should not erase history or trigger unrelated account-wide punishment.

**Relevant current authority**  
`DEC-300`; Domain Map; Paystack/CER working evidence.

**Owning Domain(s)**  
Commerce owns dispute/reversal truth; Entitlements owns any affected access consequence; Identity/Security own any separately proven abuse facts.

**Preconditions**  
Payment exists; investigation is already open; provider dispute evidence arrives.

**Exact scenario / timeline**

```text
human investigation active
+ provider dispute evidence arrives
→ Commerce interprets/reconciles current evidence
→ source-scoped reversible consequence where governed
→ later final outcome reconciles again
```

**Expected invariant(s)**

- dispute ≠ fraud finding;
- dispute ≠ account-wide ban;
- earlier historical payment/delivery remains historical truth;
- operator's stale investigation conclusion cannot overwrite later authoritative Commerce state;
- any entitlement effect is source/component-specific.

**Questions under test**  
Can manual and automated evidence processing converge without “last writer wins”?

**Adversarial variants**  
refund already requested; chargeback amount partial; operator simultaneously attempts correction.

**Analysis**  
Core semantics are adequate; exact provider states and race proof remain empirical/JIT.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `EMPIRICAL_PROVIDER` + `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Paystack dispute lifecycle validation and deterministic partial-attribution handling.

**Follow-up**  
Provider empirical proof, not more documentary guesswork.

---

## OPS-PT-020 — Browser/provider state disagrees with Commerce

**Scenario class:** failure / financial / operator

**Why it matters**  
Participants and staff naturally trust a provider receipt/dashboard, but NewYou cannot outsource its business truth.

**Relevant current authority**  
`DEC-292`, Architecture authority-before-projection doctrine, Domain Map, Paystack working contract.

**Owning Domain(s)**  
Commerce.

**Preconditions**  
Browser/provider shows one state; Commerce holds another or unresolved state.

**Exact scenario / timeline**

```text
observe provider/browser evidence
→ authenticate/bind evidence where applicable
→ reconcile through Commerce
→ Commerce establishes current platform truth
→ Entitlements follows only governed Commerce consequence
```

**Expected invariant(s)**

- no direct “copy provider status” action;
- browser return never grants access;
- unknown provider values fail closed into inconclusive evidence;
- participant communication distinguishes known platform truth from provider evidence still under reconciliation.

**Questions under test**  
Can Finance use a provider dashboard without making it authority?

**Adversarial variants**  
provider success then later reversal; stale dashboard; wrong environment/reference.

**Analysis**  
Current authority is explicit.

**Semantic disposition:** `PASS`

**Proof route:** `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`

**Upstream delta:** none.

**Evidence still required**  
Provider binding/authentication and mismatch proof.

**Follow-up**  
None beyond existing OQ-004 route.

---

## OPS-PT-021 — Late provider callback arrives after manual investigation

**Scenario class:** recovery / financial / concurrency

**Why it matters**  
A human conclusion cannot permanently suppress legitimate later evidence, but late arrival cannot blindly reverse a newer lawful state either.

**Relevant current authority**  
Architecture event-order doctrine; `DEC-300`; Paystack evidence rules.

**Owning Domain(s)**  
Commerce.

**Preconditions**  
Human investigation has recorded a conclusion/action; later provider evidence arrives.

**Exact scenario / timeline**

- late evidence is recorded as evidence;
- Commerce evaluates it against current/historical source state;
- arrival time is not business precedence;
- if the new evidence lawfully changes Commerce truth, a new transition/compensating consequence occurs;
- stale human notes/conclusions remain history but not current authority.

**Expected invariant(s)**

- old success event cannot override a later verified refund/reversal merely because it arrived late;
- a legitimate previously unknown success may correct an unresolved/incorrect failure conclusion;
- resulting Entitlement consequence is repeat-safe and current-state aware.

**Questions under test**  
What if participant was already told payment failed and paid again?

**Adversarial variants**  
late success after refund; late success after admission pause; second purchase succeeded meanwhile.

**Analysis**  
Commerce reconciliation can handle the business truth. Participant-remedy consequences may compose with duplicate-collection policy and pilot-admission policy; do not invent them in the callback handler.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-001` may apply if the late success crosses a pilot pause; `OPS-UPD-002` may apply if the participant paid twice.

**Evidence still required**  
Provider reorder proof and promoted Product seams.

**Follow-up**  
`OPS-PT-025`.

---

## OPS-PT-022 — Human correction races automated reconciliation

**Scenario class:** concurrency / operator / financial

**Why it matters**  
This is the core test of whether “manual correction” is a safe owner command or a second business-write API.

**Relevant current authority**  
Architecture current-authority and domain-write doctrine; Domain Map; Engineering Standards concurrency/idempotency rules; Product correction doctrine.

**Owning Domain(s)**  
The source Domain being corrected, here Commerce for illustration.

**Preconditions**  
An unresolved case exists; worker/reconciliation and operator action can overlap.

**Exact scenario / timeline**

```text
operator loads unresolved case at t0
worker obtains new evidence at t1
operator submits owner command at t2
```

**Expected invariant(s)**

- operator command revalidates current authoritative state at execution;
- stale UI snapshot is not permission;
- if worker already resolved the same logical obligation, duplicate human command cannot create a second consequence;
- if human command remains valid after new evidence, owner defines lawful transition/compensation;
- work-item state does not arbitrate the business race.

**Questions under test**  
Must the platform have a generic case lock?

**Adversarial variants**  
two operators act simultaneously; human refund races automatic payment success; operator sees timeout and retries.

**Analysis**  
No generic operator lock is required as Product law. The hard invariant belongs at the owning Domain/transaction boundary. UI locking may help usability but cannot be correctness authority.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-003` for who is authorised to issue each consequential command; no new concurrency Product rule.

**Evidence still required**  
Deterministic threatened-interleaving tests and stale-command rejection/re-evaluation behaviour.

**Follow-up**  
General operator-concurrency batch.

---

## OPS-PT-023 — Finance attempts to grant paid access directly

**Scenario class:** operator / abuse / financial

**Why it matters**  
A well-intentioned Finance shortcut is still a shared-write authority violation.

**Relevant current authority**  
Domain Map Commerce vs Entitlements; Platform Operating Model; Architecture cross-domain writes.

**Owning Domain(s)**  
Commerce for financial truth; Entitlements for access.

**Preconditions**  
Finance believes payment is legitimate and access is missing.

**Exact scenario / timeline**

```text
Finance command: “grant access”
→ must be rejected unless it is an explicitly authorised Entitlements operation under valid source authority
→ normal repair: resolve Commerce → trigger/recover Entitlements consequence
```

**Expected invariant(s)**

- Finance role does not imply Entitlements mutation authority;
- payment investigation does not become access grant;
- exceptional goodwill grant, if permitted, is a separately governed Entitlements source with its own authority/reason, not fake payment fulfilment.

**Questions under test**  
Could Super Admin do it anyway?

**Adversarial variants**  
Finance+Super Admin actor; friend/favour grant; “temporary” grant to unblock complaint.

**Analysis**  
Current owner law clearly rejects direct cross-domain mutation. Exact exceptional-grant role/caps are an operator-policy question and feed `OPS-UPD-003`.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-003`

**Evidence still required**  
Negative authorisation proof; governed goodwill grant policy/cap/approval.

**Follow-up**  
Privilege/abuse batch.

---

## OPS-PT-024 — Support attempts to mark payment successful

**Scenario class:** operator / abuse / financial

**Why it matters**  
Support pressure to resolve a complaint can turn a support screen into a payment ledger.

**Relevant current authority**  
Domain Map; Platform Operating Model; `DEC-292` provider evidence boundary.

**Owning Domain(s)**  
Commerce only.

**Preconditions**  
Participant presents receipt/screenshot/provider reference; Support wants to help.

**Exact scenario / timeline**

- Support may record/route the evidence under permitted minimum scope;
- Support may invoke or request Commerce reconciliation if authorised;
- Support cannot set `paid = true` or equivalent;
- Commerce independently establishes truth.

**Expected invariant(s)**

- receipt/screenshot is evidence, not payment truth;
- Support note is not payment truth;
- escalation to Finance changes responsibility, not authority owner.

**Questions under test**  
Does current role law explicitly say which Support command can initiate reconciliation versus only request Finance review?

**Adversarial variants**  
Support has Finance role too; fake receipt; duplicate support request.

**Analysis**  
The prohibited direct mutation is clear. The exact Support-vs-Finance command capability remains ungoverned enough to matter operationally.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Proof route:** `PRODUCT_DECISION_PROMOTION` or supporting operating-policy promotion, then `JIT`.

**Upstream delta:** `OPS-UPD-003`

**Evidence still required**  
Role/capability matrix with owner-command boundaries.

**Follow-up**  
Privilege matrix batch.

---

## OPS-PT-025 — Late payment success after participant was told payment failed

**Scenario class:** recovery / financial / communications / operator

**Why it matters**  
The platform may have communicated a statement that becomes wrong as later authoritative evidence arrives. Participant remedy and business truth must both remain coherent.

**Relevant current authority**  
Commerce reconciliation doctrine; Communications source-vs-delivery separation; `DEC-300`; Paystack ambiguity working rules.

**Owning Domain(s)**  
Commerce owns payment truth; Communications owns delivery evidence; source Domain owns the business statement/intent.

**Preconditions**  
Earlier evidence justified or appeared to justify a failure message; later strong evidence establishes genuine success.

**Exact scenario / timeline**

```text
payment believed failed/unresolved
→ participant told failure / invited to retry
→ later Commerce reconciliation proves original success
→ Commerce records current/historical truth
→ Entitlements applies lawful consequence
→ participant receives correction/explanation
→ if participant paid twice, duplicate-collection remedy applies
```

**Expected invariant(s)**

- earlier communication remains historical evidence; it is not silently edited;
- late success is not ignored to preserve staff narrative;
- duplicate second payment does not create duplicate right;
- participant-facing correction is separate from business-state repair.

**Questions under test**  
If stage admission is paused before the late success, is the participant admitted/owed service?

**Adversarial variants**  
second payment already succeeded; first success appears after refund; pilot cap crossed.

**Analysis**  
Core reconciliation is clear. Two Product seams may be invoked: duplicate-collection remedy and pilot admission boundary.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `EMPIRICAL_PROVIDER` + applicable `PRODUCT_DECISION_PROMOTION`

**Upstream delta:** `OPS-UPD-001`, `OPS-UPD-002` when their conditions apply.

**Evidence still required**  
Promoted seams and communications recovery proof.

**Follow-up**  
Pilot boundary batch later.

---

## OPS-PT-026 — Multiple valid Entitlement sources; one source is revoked

**Scenario class:** concurrency / financial / recovery

**Why it matters**  
A generic revoke can remove access still lawfully supported by another source, while a generic “active” projection can conceal source-specific invalidity.

**Relevant current authority**  
Domain Map Entitlement source/provenance/validity/revocation; `DEC-285`, `DEC-300`; CER working multi-source model.

**Owning Domain(s)**  
Entitlements owns source-specific rights/effective access; Commerce owns relevant commercial source truth.

**Preconditions**  
At least two independently valid sources support overlapping access.

**Exact scenario / timeline**

```text
source A + source B valid
→ A revoked/ends
→ A-specific consequence applied
→ B remains valid
→ effective access remains only to extent B independently supports it
```

**Expected invariant(s)**

- revocation is source-specific;
- historical provenance remains;
- no global source hierarchy is invented by operator tooling;
- limited credits/benefits are not automatically multiplied merely because sources overlap.

**Questions under test**  
Is the union/convergence rule sufficiently governed for exact JIT design?

**Adversarial variants**  
A revoke and B grant race; B expires simultaneously; same scope but different component semantics.

**Analysis**  
Domain Law requires source/provenance ownership but does not itself encode every multi-source effective-access rule. The CER working pack supplies a strong non-authoritative candidate model. Exact domain lifecycle/convergence belongs in Entitlements JIT unless Product benefit semantics require escalation.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** none at this point.

**Evidence still required**  
Entitlements JIT must explicitly model source-specific convergence, benefit accumulation/non-accumulation and races; escalate Product only where benefit semantics are not already governed.

**Follow-up**  
Track as `OPS-GAP-008` JIT-only unless later cases expose a Product ambiguity.

---

## OPS-PT-027 — Correction taxonomy under duplicate, timeout and concurrent automation

**Scenario class:** concurrency / recovery / operator

**Why it matters**  
The taxonomy is only useful if each class behaves differently under repeated/ambiguous execution.

**Relevant current authority**  
Architecture + Engineering Standards idempotency/reconciliation doctrine; Product correction law; Domain ownership.

**Owning Domain(s)**  
Always the owner of the durable truth being acted on; there is no generic Correction owner.

**Preconditions**  
A consequential operator action is available.

**Exact scenario / timeline**  
For each class below, submit twice, time out after submission, and race an automated owner transition:

| Operation class | Repeat-safe semantic target |
|---|---|
| retry | same logical obligation; new attempt only where execution semantics require |
| reconciliation | converge to same lawful result under unchanged evidence |
| correction | one intended corrected meaning/history, not repeated mutations |
| override | one scoped exceptional transition; repeated request cannot broaden scope |
| replacement | one intended successor/version per authorised replacement request |
| refund | one owed financial consequence; repeated command cannot refund twice |
| reversal | source-specific commercial consequence; no unrelated effect |
| revocation | same source/right ends once; repeat is no-op/reconciled |
| restoration | only if current source authority permits; no stale resurrection |
| cancellation | same open/future obligation cannot be cancelled into unrelated states repeatedly |
| suspension | current restriction converges; repeat does not extend/change scope accidentally |
| withdrawal | same named permission/content authority converges to withdrawn state where applicable |
| deletion | destructive orchestration repeat-safe; no resurrection |
| support annotation | duplicate note may be duplicate evidence/noise but never duplicate business consequence |

**Expected invariant(s)**

- transport/request identity is not automatically business idempotency identity;
- unknown outcome does not authorise blind repeat of irreversible consequence;
- owner state/current guards decide stale/concurrent command outcome;
- audit evidence may record distinct attempts without multiplying business effect.

**Questions under test**  
Can JIT implement one generic “operator action” retry policy?

**Adversarial variants**  
all rows above.

**Analysis**  
A universal retry policy is unsafe. The required durable invariant is owner- and consequence-specific. The remaining cross-cutting missing rule is **who may invoke which consequential commands and with which approval**, not a universal lifecycle implementation.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Proof route:** `JIT` + `PHASE8_EXECUTABLE`

**Upstream delta:** `OPS-UPD-003`

**Evidence still required**  
Action-specific idempotency/unknown-outcome mapping and operator capability matrix.

**Follow-up**  
Operator privilege/abuse + concurrency batch.

---

# 17. Upstream delta additions / refinements

## OPS-UPD-002 — Promote the already-accepted duplicate-collection / make-whole Product clarification

> **WORKING / NON-AUTHORITATIVE**

**Originating PT:** `OPS-PT-016`, with consequences in `OPS-PT-021` and `OPS-PT-025`.

**Exact missing authority**  
Current Product Law clearly prevents duplicate rights and recognises duplicate-payment correction, but the current Paystack Pre-JIT contract explicitly records the stronger rule as an **accepted working Product clarification — not yet Product Law**:

- one accepted order may be satisfied by only one genuine collection;
- additional genuine collection is truthful financial history but no second right;
- full customer-collected excess remains owed through safe source-scoped remedy;
- provider execution failure/ambiguity does not erase the owed amount;
- partial reversal amount cannot manufacture component identity.

**Candidate working direction**  
Do not invent new wording here. Reuse/promote the existing accepted Paystack working clarification after upstream review, unless current authority is amended by a different explicit rule.

**Affected authority**  
Product Law/Decision Register commercial correction rules; FP-002/FP-006 Roadmap semantics only as needed for routing.

**Affected Domains**  
Commerce; Entitlements for deterministic consequence only.

**Rejected alternatives**

- keep excess money because one entitlement was already granted;
- create a second right for the second collection;
- treat provider refund failure as ending NewYou's obligation;
- infer component identity from amount coincidence/current catalogue price;
- let operator choose an arbitrary component to revoke.

**Reason JIT cannot safely decide it**  
It is a customer-money obligation and correction policy. Implementation cannot decide what NewYou owes.

**Likely promotion destination**  
Product Law / Decision Register, preferably by promoting the already-reviewed Paystack clarification rather than duplicating policy language.

**Provider/expert dependency**  
Provider empirical evidence is still needed for mechanism/unknown-outcome handling; legal/consumer review may be appropriate. Provider mechanics do not decide the obligation.

**Downstream Feature Pack impact**  
FP-002 and FP-006.

---

## OPS-UPD-003 — Consequential operator command authority matrix

> **WORKING / NON-AUTHORITATIVE**

**Originating PTs:** `OPS-PT-017`, `OPS-PT-022`, `OPS-PT-023`, `OPS-PT-024`, `OPS-PT-027`; refines v0.1.0 `OPS-GAP-002`.

**Exact missing authority**  
Current authority defines staff role categories, Domain owners, least privilege, no universal Super Admin bypass, some specialised grants and release authority. It does **not yet provide a sufficiently complete FP-006 operating contract stating which human roles/scopes may request, approve and execute each consequential core-journey command**, including at minimum:

- payment reconciliation initiation/adjudication;
- refund/component-refund request and approval;
- governed goodwill/complimentary entitlement grant within any allowed cap;
- entitlement revoke/restore/correction request;
- assessment technical recovery versus completed-result correction/review;
- identity merge/recovery/privileged access;
- health-fact correction routing;
- safety restriction/override/clearance;
- Plan withdrawal/replacement/regeneration where human authority is involved;
- high-risk evidence/export/access actions;
- pilot pause/resume/release sign-off actions.

The missing rule is **not** a universal admin role matrix for the mature platform. It is the minimum consequential command authority needed by FP-006's real operators.

**Candidate working direction**

For every consequential FP-006 operator action define:

```text
source Domain owner
requesting capability/role/scope
executing/approving authority
current-state guard
separation-of-duties rule where required
reason/evidence requirement
reversibility
idempotency / unknown-outcome rule
participant-visible consequence
```

Support/Finance may initiate or request owner operations where explicitly authorised, but never acquire owner truth. Super Admin remains bounded and cannot bypass clinical/methodology/privacy/business authority merely by role name.

**Affected authority**  
Likely Platform Operating Model and/or Product/Decision operating policy; specific owner Domain/JIT contracts may specialise action-level checks after the human authority rule is governed.

**Affected Domains**  
Cross-cutting across FP-001...FP-006 owner Domains. No new Domain.

**Rejected alternatives**

- `Super Admin = can do everything`;
- infer permission from page visibility;
- let JIT assign consequential powers ad hoc;
- universal “Support can fix participant state” capability;
- direct database/provider-dashboard corrections;
- requiring two-person approval for every low-risk action without evidence.

**Reason JIT cannot safely decide it**  
Who may refund, restore access, override safety, correct identity or pause release is operational/business authority. A coding/JIT agent should not invent human power boundaries.

**Likely promotion destination**  
Supporting operating authority (Platform Operating Model successor) for cross-role doctrine plus Product/Decision authority where a command changes commercial/safety/customer promise; owner JIT dossiers then encode the governed capability precisely.

**Provider/expert dependency**  
Security/privacy/clinical/legal review where the action class requires it.

**Downstream Feature Pack impact**  
FP-006 primary; reused by later Feature Packs with action-specific additions rather than a universal admin system.

---

# 18. Gap register changes — v0.2.0

## OPS-GAP-002 — Consequential operator permission/approval matrix

**Prior state in v0.1.0:** `OPERATIONS_POLICY_GAP / OPEN / NOT YET PROVEN UPSTREAM`.

**v0.2.0 refinement:** pressure tests now demonstrate that leaving the **human authority boundary** entirely to JIT would require JIT to invent consequential operating policy.

- **Classification remains:** `OPERATIONS_POLICY_GAP`
- **Status:** CONFIRMED.
- **Route:** `OPS-UPD-003`.

No v0.1.0 text is erased.

## OPS-GAP-007 — Duplicate collection / make-whole clarification not yet governed

- **Classification:** `PRODUCT_AUTHORITY_GAP`
- **Origin:** `OPS-PT-016`.
- **Evidence:** Paystack Pre-JIT current compact explicitly says the candidate clarification is accepted working direction but not Product Law.
- **Route:** `OPS-UPD-002`; do not independently redesign it here.
- **Status:** OPEN.

## OPS-GAP-008 — Exact multi-source Entitlement convergence

- **Classification:** `JIT_ONLY`
- **Origin:** `OPS-PT-015`, `OPS-PT-018`, `OPS-PT-026`.
- **Current direction:** Domain Law fixes source/provenance ownership; CER working evidence provides a strong source-union/convergence model. Exact Entitlements lifecycle/constraints/proof belong in Entitlements JIT unless a concrete benefit-accumulation case exposes a Product ambiguity.
- **Status:** DEFERRED CORRECTLY.

## OPS-GAP-009 — Partial reversal component attribution

- **Classification:** `PRODUCT_AUTHORITY_GAP`
- **Origin:** `OPS-PT-019` and existing Paystack working clarification.
- **Current direction:** a financial loss amount alone must not manufacture which entitlement component/right to revoke; the Paystack working pack already records this as part of the not-yet-governed clarification.
- **Route:** included in `OPS-UPD-002` rather than creating another delta.
- **Status:** OPEN.

---

# 19. Correction taxonomy disposition after Batch B

The v0.1.0 taxonomy survives, with these refinements:

1. **Compensation must be explicit.** Refund/reversal/revocation may be later true events, not corrections of the earlier event.
2. **Manual = human-triggered owner command, never alternate persistence write.**
3. **Unknown outcome blocks blind repeat for irreversible consequences.**
4. **Reconciliation converges; it does not “pick the latest event.”**
5. **Business idempotency and evidence-attempt history are separate.** Repeated attempts may be auditable while the business consequence remains one.
6. **Source-specificity is mandatory for Commerce→Entitlement correction.** A financial event cannot justify account-wide access mutation without a governed mapping.
7. **Operator work lifecycle is independent of source lifecycle.** Closing a case cannot certify that the business outcome is correct.

---

# 20. Batch B findings

## 20.1 Strong conclusions

- No generic `manual fix` operation is semantically safe.
- Finance is not Entitlements authority.
- Support is not Commerce authority.
- Cross-domain recovery should repair/converge the owner consequence, not mutate a synthetic support state.
- Domain invariants/current-state guards, not staff assignment or UI disabling, must settle races.
- Current Product Law is already strong enough to reject duplicate entitlement and provider-as-authority behaviour.

## 20.2 New real gaps

Two consequential gaps are now justified:

- `OPS-UPD-002` — reuse/promote the existing duplicate-collection/make-whole and partial-attribution working clarification;
- `OPS-UPD-003` — govern the minimum FP-006 consequential operator command authority matrix before JIT makes up staff powers.

Neither gap justifies an Operations Domain.

## 20.3 What is *not* a gap

Do not promote these merely because implementation is not yet designed:

- support case table/schema;
- generic case lifecycle;
- generic reconciliation Resource;
- exact source-set storage model;
- UI buttons/locks;
- worker names/queues;
- database locking mechanism;
- exact provider retry implementation.

These are JIT/proof/mechanism concerns after semantics are governed.

---

# 21. Current cumulative PT / UPD inventory

### Pressure tests

```text
OPS-PT-001...013  v0.1.0 normal operational journeys
OPS-PT-014...027  v0.2.0 correction + Commerce/Entitlements
```

Total executed: **27**.

### Candidate upstream deltas

- `OPS-UPD-001` — pilot admission boundary and concurrent/in-flight stage-cap semantics.
- `OPS-UPD-002` — promote existing duplicate-collection/make-whole + partial-attribution clarification.
- `OPS-UPD-003` — consequential operator command authority matrix.

All remain **WORKING / NON-AUTHORITATIVE**.

---

# 22. Next highest-value batch

Next MINOR successor should attack **Assessment + Health/Safety/Plans operations** because these are the places where support convenience can most dangerously rewrite immutable or clinically governed truth.

Execute at minimum:

### Assessment

1. credit exists but attempt cannot start;
2. attempt exists but result delivery stuck;
3. result exists but credit appears unused;
4. credit consumed but delivery failed;
5. duplicate submission;
6. timeout after submit;
7. Support wants to “reset” completed assessment;
8. participant disputes result;
9. staff wants to change digital result manually;
10. declared temperament + unused digital right;
11. later digital completion.

### Health / Safety / Plans

12. health intake submitted but eligibility unresolved;
13. eligibility changes after Plan generation;
14. Plan generated from stale facts;
15. unsafe content found after delivery;
16. participant reports adverse symptoms;
17. Support routes concern without unnecessary health detail;
18. professional review required;
19. Plan regeneration owed;
20. entitlement ends during already-admitted fulfilment;
21. Support tries to bypass Safety;
22. clinical authority corrects/withdraws content or Plan.

The batch should explicitly separate operational retry from Product correction, safety override, clinical decision and immutable replacement.

---

# 23. v0.2.0 disposition

```text
NORMAL JOURNEYS: 13 PTs
CORRECTION + COMMERCE/ENTITLEMENTS: 14 PTs
CUMULATIVE: 27 PTs
UPSTREAM DELTAS: OPS-UPD-001...003
NEW GAPS THIS VERSION: OPS-GAP-007...009
OPS-GAP-002: CONFIRMED → OPS-UPD-003
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
BROAD PRE-JIT FREEZE: NOT READY
NEXT: ASSESSMENT + HEALTH/SAFETY/PLANS OPERATIONS
```
