# Commerce / Entitlements / Recurring Membership Pre-JIT Discovery — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY
- **Stream:** Commerce + Entitlements + recurring Membership/subscription commercial semantics
- **Purpose:** Preserve accepted pre-JIT findings, pressure-test outcomes, working recommendations, Store reuse evidence and unresolved seams for later Feature Pack/JIT work.
- **Authority:** None. This document does not amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Feature Pack contracts or JIT Domain Dossiers.
- **Implementation:** NOT AUTHORISED BY THIS DOCUMENT.
- **Repository rule:** Live governed NewYou authority always wins. Store Blueprint is evidence only and never NewYou authority.
- **Conflict rule:** If downstream discovery exposes an upstream contradiction, stop at the correct authority level. Do not repair Product/Architecture/Domain law inside this document.
- **Preservation rule:** Accepted findings are never silently deleted. Later changes must add, refine, or explicitly supersede prior wording with provenance.

---

## 0. Versioning and preservation policy

This discovery remains pre-1.0 working material.

SemVer policy for this stream:

- **MINOR (`v0.x.0`)** — new accepted pressure-test result, accepted working doctrine, material reuse conclusion, material recommendation change, or newly admitted upstream delta.
- **PATCH (`v0.x.y`)** — evidence refresh, citation/source-baseline correction, terminology/hygiene clarification, typo correction, or non-semantic wording improvement.
- **`v1.0.0`** — not automatic. It requires an explicit decision that a stable compact contract or equivalent governed handoff artifact is ready. This working discovery document does not become authority merely by reaching `v1.0.0`.

For each version change:

1. preserve the previous versioned file;
2. create a successor versioned file rather than deleting the predecessor;
3. record the semantic/non-semantic change in the version history;
4. preserve accepted finding identifiers and mark any changed conclusion as refined/superseded rather than reusing an identifier for a different meaning;
5. refresh source baselines where a material conclusion depends on live repository state.

Git history is useful evidence but is not a substitute for the explicit versioned-successor rule above.

---

## 1. Scope and non-scope

This stream exists to pressure-test and clarify:

- purchase/payment correctness;
- recurring billing and renewal semantics;
- provider evidence and reconciliation;
- entitlement issuance, validity, expiry, revocation and consumption;
- cancellation, retries, grace and suspension;
- refunds, disputes and chargebacks;
- Basic/add-on/Premium composition;
- purchaser/recipient/participant separation;
- cross-seams with Plan/review rights and professional fulfilment;
- Store Blueprint reuse/hardening opportunities.

It is deliberately **not**:

- implementation;
- a Feature Pack JIT dossier;
- Product Law;
- Architecture Law;
- Domain Law;
- an authority amendment;
- permission to redesign NewYou around a payment provider;
- permission to package/refactor Store Blueprint prematurely.

The stream must not alter current governed programme routing.

---

## 2. Authority and evidence baselines

### 2.1 NewYou baseline used for v0.1.0

The accepted findings captured in this initial document were pressure-tested against live NewYou `main` at:

`e95712ab000977b8b8dab5dac62761c2d912b866`

Current routed authority at that baseline included:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.39.md`
5. `03_ARCHITECTURE_v1.1.0.md`
6. `04_DOMAIN_MAP_v1.1.0.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.0.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` where frontend/experience semantics are materially relevant.

The Delivery Atlas remains derived navigation only and does not create authority.

### 2.2 Store Blueprint evidence baseline used for v0.1.0

Store evidence is moving implementation evidence, not NewYou authority.

Initial material checkpoint:

- Store default branch `main`: `486a1c74f5b738d488fdd54118002e90ec67bd49`
- Store `hardening/subscriptions`: `77a272c3887a7ab46e84a7fed02163d964e37b9b`
- no open PR whose head is `hardening/subscriptions` at the checkpoint;
- other active PRs were inspected where relevant and were not treated as subscription-semantic authority merely because they existed.

At each later material Store inspection:

1. inspect default branch;
2. inspect relevant active branches/PRs;
3. record the exact branch/head SHA used;
4. distinguish merged from in-progress work;
5. distinguish GitHub evidence from user-reported local/unpushed work;
6. invalidate prior implementation certification for a changed Store head without treating that Store change as a NewYou doctrine change.

Store differences must be classified as one of:

- implementation improvement consistent with NewYou;
- implementation defect;
- reusable mechanism improvement;
- new evidence exposing a working seam;
- genuine NewYou upstream question.

Only the last two can materially change this Pre-JIT stream, and genuine upstream questions must resolve through NewYou authority.

---

## 3. Governing ownership already established by current authority

The current Domain Map keeps **Commerce** and **Entitlements** deliberately separate.

### Commerce owns

- commercial product/offer/price truth;
- purchase/payment/refund/dispute truth;
- membership/subscription/add-on commercial contract truth.

### Entitlements owns

- entitlement/access grants;
- entitlement identity and scope;
- source/provenance;
- validity and expiry;
- revocation;
- consumable/redemption rights and idempotent consumption.

`Memberships` is **not** a separate NewYou Domain.

Core boundary:

`money / commercial contract truth ≠ access / entitlement truth`

Provider state, browser returns, caches, Analytics, PubSub and worker state cannot become hidden business authority.

---

## 4. Working method for this stream

### 4.1 Authority-first rule

For each scenario:

1. determine whether current authority already answers it;
2. distinguish Product/commercial policy from Architecture mechanism, Domain ownership, JIT representation, provider validation and operating policy;
3. create no new working doctrine when existing authority is sufficient;
4. create no provider-specific rule where provider-independent semantics can be established first;
5. if Product Law is genuinely missing, record an upstream delta rather than inventing a local answer;
6. if authority contradicts itself, stop at the correct upstream layer.

### 4.2 Dual-verdict rule

Whenever Store evidence is materially involved, every pressure test reports two distinct verdicts:

**NewYou semantics**
- PASS
- PASS WITH NON-BLOCKING CORRECTIONS
- CHANGES REQUIRED
- BLOCKED / STOP

**Store Blueprint evidence/reuse**
- PASS
- PASS WITH NON-BLOCKING CORRECTIONS
- CHANGES REQUIRED
- BLOCKED / STOP

Then report a separate reuse classification where applicable:

- SAFE TO REUSE AS-IS
- REUSE AFTER HARDENING
- ADAPTATION REQUIRED
- NOT REUSABLE FOR THIS SEMANTIC
- OUT OF CURRENT SCOPE

A NewYou semantic PASS must never be read as certification that Store implementation also passes.

### 4.3 Recommendation duty

This Pre-JIT is not only an audit.

When a genuine design choice, Product-policy option, implementation direction or reuse decision exists:

1. state the realistic options;
2. identify options incompatible with current authority;
3. compare correctness, simplicity, maintainability, recovery, concurrency and future flexibility;
4. recommend the smallest safe option;
5. explain why it is preferred;
6. identify trade-offs;
7. identify evidence that could change the recommendation;
8. classify the recommendation as one of:
   - already required by authority;
   - working Pre-JIT doctrine requiring explicit user acceptance;
   - JIT implementation recommendation;
   - Store reuse/hardening recommendation;
   - upstream Product/commercial decision.

A recommendation is not automatically authority.

If genuinely new working doctrine is required, propose `CER-WH-###` and wait for explicit acceptance before treating it as `CER-WD-###`.

### 4.4 Local working identifiers

Permitted non-governed identifiers:

- `CER-WH-###` — proposed working hypothesis;
- `CER-WD-###` — explicitly accepted working doctrine;
- `CER-PT-###` — pressure test;
- `CER-UPD-###` — upstream delta.

These identifiers are working navigation only. They do not create governed DEC/ARC/ARQ/OQ/FP/TB/VS/HH authority.

---

## 5. Provider-independent governing principle

A core accepted method principle for this stream is:

> Define NewYou's commercial truth first → validate whether the launch provider can implement it → adapt the provider boundary where possible → escalate only genuine incompatibilities.

Do **not** model NewYou around whatever a provider happens to expose.

`OQ-004` therefore does not prevent provider-independent NewYou semantics from being defined. It gates exact webhook, recurring billing, retry, proration, refund, dispute/chargeback and provider-ambiguity behaviour where provider proof is materially required.

---

# 6. Accepted pressure-test findings

## CER-PT-001 — Provider succeeds; crash before entitlement convergence

### Scenario

The provider successfully takes payment, but NewYou crashes at one of the boundaries before the required Entitlements consequence has fully converged.

### Accepted NewYou invariant

For one qualifying authoritative commercial success, exactly one intended logical entitlement consequence must eventually exist per purchased right.

Multiple technical paths — provider evidence, browser return, webhook replay, provider verification, reconciliation, worker retry, restart or support recovery — do not create new purchases or new logical rights.

Commercial success and entitlement issuance are separate owner-controlled truths. A crash after Commerce commits cannot erase the commercial fact; a crash after an Entitlements grant but before acknowledgement cannot justify issuing another independent logical right.

Recovery must be possible from durable authority/evidence after restart. Process memory, LiveView, PubSub, provider dashboard state, cache state and operator memory are insufficient correctness mechanisms.

There is no acceptable terminal condition in which money is durably taken and a required entitlement is silently lost merely because retries exhausted.

### NewYou semantics verdict

**PASS**

Existing authority is sufficient.

- No `CER-WH`.
- No `CER-UPD`.
- No Domain change.
- No Resource decision.
- No implementation mechanism frozen.

### Store Blueprint evidence verdict

**CHANGES REQUIRED**

Strong mechanism candidate:

- Commerce-side `apply_payment_success_once` / durable payment-application apply-once handling.

Current defect against the NewYou requirement:

- subscription creation can commit before entitlement issuance;
- entitlement issuance occurs after that transaction;
- entitlement failures can be counted/skipped;
- no independent must-not-lose entitlement convergence mechanism was identified in the inspected path.

### Reuse classification

**REUSE AFTER HARDENING**

---

## CER-PT-002 — Duplicate/replayed success while browser verification and webhook processing race

### Scenario

Several independent evidence paths may concurrently describe the same successful commercial occurrence: browser-triggered verification, webhook processing, webhook replay, reconciliation and retry.

### Accepted NewYou invariants

- Browser/client/provider return is evidence, not payment authority.
- Evidence channels are interchangeable inputs to Commerce reconciliation, not independent payment authorities.
- Delivery identity is not business-effect identity.
- Ten successful observations of one provider payment still represent one qualifying commercial success.
- Logical entitlement issuance follows the commercial occurrence, not the number of delivery observations.
- Concurrency must be defeated at a durable business invariant, not by check-then-act process logic.

Accepted principle:

> Provider delivery mechanisms may multiply; business consequences may not.

### Recommendation

**Recommended direction:** allow multiple trusted evidence-acquisition paths, but make them converge through one Commerce-owned reconciliation contract.

Rejected:

- browser return directly marks paid;
- webhook-only business authority;
- separate browser-success/webhook-success/reconciliation success transitions that can each manufacture the same business consequence.

Classification: **JIT implementation/architecture recommendation beneath existing authority**.

### NewYou semantics verdict

**PASS**

Existing authority is sufficient.

- No `CER-WH`.
- No `CER-UPD`.
- No new Domain.
- No Resource decision.

### Store Blueprint evidence verdict

**CHANGES REQUIRED**

Useful Store evidence:

- return/cancel path is read-only rather than payment-authoritative;
- verified webhook receipt is persisted before domain transition;
- provider-event/payment-attempt evidence provides replay boundaries;
- `PaymentApplication` uses a durable apply-once key with database conflict protection.

Limitations:

- Store does not currently prove the harder independent-channel race where browser-triggered server verification and webhook reconciliation both compete;
- PT-001's downstream entitlement-convergence defect remains;
- Store's order-centric payment-application key is implementation evidence, not NewYou doctrine.

### Reuse classification

**REUSE AFTER HARDENING**

---

## CER-PT-003 — Missing, delayed and reordered provider evidence

### Scenario

For the same payment attempt, NewYou may receive pending/ambiguous/failure-looking evidence first, then delayed success, then replayed older evidence. Network arrival order may disagree with commercial finality.

### Accepted NewYou invariants

- Provider event arrival order is an observation property, not a business rule.
- Last event received cannot define authoritative commercial state.
- First terminal-looking event cannot universally define finality.
- “Success always wins” is also not a safe universal rule without provider-contract evidence.
- Contradictory provider evidence must be reconciled according to the verified provider contract, independent of arrival order.
- Genuine ambiguity must fail closed: do not fabricate paid truth, but also do not fabricate irreversible failure where provider finality remains unresolved.
- A failed provider attempt and a failed commercial purchase are not automatically the same durable truth.

Accepted principles:

> Provider event order is an observation property, not a business rule.

> A failed payment attempt and a failed purchase are not automatically the same durable truth.

### Recommendation

**Recommended direction:** preserve provider observations/evidence separately from authoritative Commerce interpretation; reconcile contradictory observations before final commercial consequence.

Do not model Commerce as `last provider event → overwrite payment.status`.

Classification: **implementation/reuse hardening recommendation beneath existing authority**.

Exact Paystack finality/supersession rules remain under `OQ-004` provider validation.

### NewYou semantics verdict

**PASS**

Existing authority is sufficient at provider-independent semantic level.

- No `CER-WH`.
- No `CER-WD`.
- No `CER-UPD`.
- No Domain amendment.
- No Resource decision.

### Store Blueprint evidence verdict

**CHANGES REQUIRED**

Material defect at the inspected Store subscription head:

- `PaymentIntent.failed` is effectively terminal for ordinary payment success;
- success is transitionable from submitted/requires-action but not from failed;
- therefore late verified success for the same provider attempt may be rejected purely because a failure observation was processed first.

Store renewal reconciliation is more tolerant downstream, but it cannot repair an upstream paid-order/payment success that was blocked by the terminal PaymentIntent lifecycle.

### Reuse classification

**REUSE AFTER HARDENING**

---

## CER-PT-004 — Recurring renewal replay / idempotency

### Scenario

One billing period becomes due while multiple scheduler runs, workers, retries, provider calls, webhook deliveries and reconciliation executions overlap. A provider may successfully charge while NewYou loses the response and retries.

### Accepted NewYou invariants

- One governed renewal occurrence may require multiple technical attempts but must not become multiple logical renewals.
- Scheduler run, worker job, provider HTTP request, webhook, retry number and provider message identity are execution/evidence concepts, not the renewal's business identity.
- Local idempotency alone is insufficient if the provider may see retries as separate charges.
- A transport timeout proves only that NewYou lacks a reliable answer; it does not prove the provider did not charge.
- The logical recurring collection identity must remain stable across local replay, provider-safe retry and later reconciliation.

Accepted principles:

> A billing retry is not a new renewal.

> Retries may multiply execution attempts, but the logical collection identity must remain stable across NewYou and the payment-provider boundary.

### Recommendation

**Recommended direction:** define one durable logical identity for each intended recurring collection and preserve its semantic continuity through scheduler replay, worker retry, provider mutation retry, callback processing and reconciliation.

Rejected:

- each scheduler run may create a fresh collection;
- Oban uniqueness as the business correctness mechanism;
- local-only renewal idempotency while provider retries use unrelated mutation identities.

Classification: **already required by current Architecture + DEC-043; implementation/provider adaptation remains downstream**.

Exact Paystack support/equivalent safe-retry behaviour remains `OQ-004` work.

### NewYou semantics verdict

**PASS**

Existing authority is sufficient.

- No `CER-WH`.
- No `CER-WD`.
- No `CER-UPD`.
- No Domain amendment.
- No Resource decision.

### Store Blueprint evidence verdict

**CHANGES REQUIRED FOR NEWYOU REUSE — STRONG REUSABLE CORE**

Strong reusable Store mechanisms at the inspected subscription head:

- deterministic renewal occurrence key derived from subscription + period boundary;
- one `RenewalAttempt` identity per subscription + renewal key;
- create-or-reuse/upsert semantics;
- compare-and-swap style claim preventing concurrent workers from both owning the same attempt generation;
- deterministic renewal payment-intent identity;
- provider idempotency propagation in the operational Stripe path;
- absolute-period reconciliation rather than additive `+ 1 period` replay;
- already-succeeded paid-renewal reconciliation no-op.

Reasons whole-path reuse is not yet safe as-is:

1. provider proof is Stripe-specific and does not satisfy NewYou's Paystack gate;
2. PT-003's reordered outcome defect remains;
3. PT-001's Commerce → Entitlements convergence defect remains.

The exact Store key format is implementation evidence, not NewYou doctrine.

### Reuse classification

**REUSE AFTER HARDENING / PROVIDER ADAPTATION REQUIRED**

---

# 7. Current Store reuse ledger

This ledger is provisional and must be refreshed at material Store checkpoints.

| Store mechanism / semantic | Current classification | Reason |
|---|---|---|
| Payment apply-once / durable payment application boundary | **REUSE AFTER HARDENING** | Strong commercial idempotency candidate; downstream entitlement convergence remains incomplete. |
| Receipt-first webhook evidence and provider-event dedupe | **REUSE AFTER HARDENING** | Good evidence boundary; must fit NewYou provider-independent reconciliation contract. |
| Read-only browser return | **ADAPTATION REQUIRED** | Safe pattern, but does not by itself prove independent verification-channel convergence. |
| Store `PaymentIntent` lifecycle | **NOT REUSABLE AS-IS FOR THIS SEMANTIC** | Terminal failed state conflicts with reorder/ambiguity-safe reconciliation required by NewYou. |
| Renewal scheduler / renewal occurrence identity | **REUSE AFTER HARDENING** | Strong deterministic identity pattern; exact key format remains JIT implementation. |
| `RenewalAttempt` create-or-reuse + claim | **REUSE AFTER HARDENING** | Strong replay/concurrency mechanism candidate. |
| Stripe renewal idempotency propagation | **ADAPTATION REQUIRED** | Valuable provider-boundary pattern, but launch provider is Paystack and requires independent proof. |
| Absolute-period paid-renewal reconciliation | **REUSE AFTER HARDENING** | Repeat-safe direction; cross-intent concurrency still needs later testing. |
| Subscription → entitlement issuance after initial paid order | **NOT REUSABLE AS-IS FOR THIS SEMANTIC** | Must-not-lose entitlement convergence not currently proved. |
| Store Domain decomposition (`Subscriptions` as Domain, etc.) | **NOT REUSABLE FOR NEWYOU DOMAIN LAW** | Store implementation organization cannot override NewYou's Commerce/Entitlements ownership model. |

---

# 8. Cross-stream Health / Safety / Plans seams already known

Do not create duplicate CER doctrine where the HSP working stream already records a cross-seam.

Relevant existing HSP deltas include:

- membership-derived Plan/review admitted before entitlement expiry but still in flight after expiry;
- genuinely unfulfillable paid Plan;
- meaning of refund boundary where professional approval follows generation;
- participant materially changes intent after paid admission but before first fulfilment.

These must be cross-referenced when later CER pressure tests reach Plan/review fulfilment, rather than independently reinvented.

---

# 9. Current unresolved/provider gates

### OQ-004 — primary provider gate for this stream

Exact Paystack behaviour remains to be validated for material implementation decisions including:

- recurring billing;
- webhook delivery/verification;
- retry semantics and safe retry identity;
- provider ambiguity/finality;
- proration;
- refunds;
- disputes/chargebacks;
- settlement behaviour where relevant.

This gate does **not** allow Paystack to define NewYou commercial truth.

### Other later cross-seams

Additional known questions may become material for:

- monthly review timing/contracts;
- release commercial/legal readiness;
- security/operations/vendor readiness.

They should only be pulled into this stream when a pressure test materially depends on them.

---

# 10. Planned pressure-test map

Accepted/complete:

1. `CER-PT-001` — provider succeeds; crash before entitlement convergence — **COMPLETE**
2. `CER-PT-002` — duplicate/replayed success + concurrent evidence paths — **COMPLETE**
3. `CER-PT-003` — missing/delayed/reordered contradictory provider evidence — **COMPLETE**
4. `CER-PT-004` — recurring renewal replay/idempotency — **COMPLETE**

Next/high-value sequence:

5. `CER-PT-005` — failed renewal + 72-hour grace + late successful retry, including cancellation race
6. cancellation intent racing renewal
7. exact paid-period boundary semantics
8. Basic/add-on/Premium upgrade/downgrade/proration
9. refund before entitlement consumption
10. refund/chargeback after benefit consumption
11. in-flight membership benefit across expiry — cross-reference HSP
12. Plan unfulfillable/change-intent/refund-boundary — cross-reference HSP
13. purchaser ≠ beneficiary + PMR minimum disclosure
14. provider-side subscription identity replacement/recreation
15. manual reconciliation racing delayed provider evidence/provider outage

The list is bounded. Stop earlier if the model becomes stable enough that further tests are low-value repetition.

---

# 11. Accepted decision / doctrine register

No `CER-WD-###` doctrine has been created as of v0.1.0.

That is intentional: PT-001 through PT-004 were fully answerable from existing authority at the provider-independent semantic level.

Accepted outcomes captured here are working findings and recommendations beneath current authority; they do not manufacture a new authority layer.

If a future test requires genuinely new working doctrine, the sequence is:

`CER-WH-### proposed → explicit user acceptance → CER-WD-### recorded in successor version`

If it instead exposes missing Product/commercial policy:

`CER-UPD-###`

If it exposes an upstream contradiction:

**STOP at the correct authority level.**

---

# 12. Version history

## v0.1.0 — 2026-09-08

Initial living Commerce / Entitlements / Recurring Membership Pre-JIT discovery artifact.

Captured:

- authority and Store evidence baselines;
- moving Store evidence rule;
- dual-verdict method;
- recommendation duty;
- provider-independent-contract-first principle;
- accepted `CER-PT-001` through `CER-PT-004` findings;
- provisional Store reuse ledger;
- HSP cross-stream seams;
- current OQ-004 provider gate;
- bounded next pressure-test map;
- explicit statement that no `CER-WD` has yet been required.

This version does not authorise implementation or amend governed authority.
