# NewYou Commerce / Entitlements / Recurring Membership Pre-JIT Discovery — Working

- **Current version:** `v0.30.3`
- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY
- **Stream:** Commerce + Entitlements + recurring Membership/subscription commercial semantics
- **Implementation authority:** NONE
- **Repository authority:** NONE
- **Purpose:** Preserve accepted discovery findings, pressure-test outcomes, provider-independent invariants, Store Blueprint reuse evidence, working recommendations, unresolved seams and upstream deltas for later Feature Pack/JIT work.
- **Conflict rule:** Live governed NewYou authority always wins. If this discovery exposes an upstream contradiction, STOP at the correct authority level rather than repairing it here.
- **Preservation rule:** Accepted findings are never silently deleted. Later work may add, refine or explicitly supersede prior wording, but provenance and earlier meaning must remain recoverable.
- **Broad pressure-test status:** SECOND-PASS CLOSURE ROUND COMPLETE; Candidate 1 created `CER-PT-016`, Candidate 2 refined `CER-PT-016`/`CER-UPD-005`, Candidate 3 refined `CER-PT-008` and accepted `CER-UPD-006`, Candidate 4 confirmed existing coverage, Candidate 5 created `CER-PT-017`/`CER-UPD-007`, Candidate 6 created `CER-PT-018`/`CER-UPD-008`, Candidate 7 created `CER-PT-019`/`CER-UPD-009`, Candidate 8 confirmed coverage under existing PT-003/PT-004/PT-006/PT-015, Candidate 9 confirmed coverage under existing PT-003/PT-007/PT-008/PT-015, Candidate 10 materially refined `CER-PT-008`, Candidate 11 materially refined `CER-PT-011` and accepted `CER-UPD-010`, Candidate 12 materially refined `CER-PT-012` and accepted `CER-UPD-011`, Candidate 13 created `CER-PT-020` and accepted `CER-UPD-012`, Candidate 14 materially refined `CER-PT-001`, `CER-PT-011`, and `CER-PT-015`, Candidate 15 materially refined `CER-PT-011`, `CER-PT-012`, and `CER-PT-020` and accepted `CER-UPD-013`. Planned Candidates 1–15 are complete. Renewed semantic stabilisation/completeness audit `v0.2.0` already passed against exact deep source `v0.30.1`; `v0.30.2` was a four-reference hygiene PATCH. This `v0.30.3` PATCH changes current routing/protocol text only. Exact `v0.30.3` bytes require narrow mechanical recertification under the audit anti-drift rule, then final compact recompression and source↔compact verification.
- **Renewed semantic stabilisation/completeness audit:** `NEWYOU_CER_PREJIT_STABILISATION_AUDIT_WORKING_v0.2.0.md` — PASS against exact `v0.30.1`. Its semantic conclusions carry forward because `v0.30.2` and `v0.30.3` are hygiene-only PATCHes; exact current bytes still require mechanical recertification before final recompression.
- **Prior first-pass stabilisation audit:** `NEWYOU_CER_PREJIT_STABILISATION_AUDIT_WORKING_v0.1.0.md` — PASS WITH NON-BLOCKING CORRECTIONS.
- **Prior first-pass full double-check:** `NEWYOU_CER_FULL_DOUBLE_CHECK_WORKING_v0.1.0.md` — CER SEMANTICS PASS; v0.1.0 compact packaging required correction.
- **Current compact baseline before final reissue:** `v0.1.1` remains the prior provisional first-pass compression. The final compact pack must be regenerated only after exact `v0.30.3` passes narrow mechanical recertification; this deep source does not depend on or pre-certify a downstream compact artifact.
- **Current audited NewYou baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`; current Open Work `v1.2.40`.
- **Current audited Store baselines:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `54871ef3bdda42f067ed5dbd398305151610c060`. The movement from the earlier `575ffa1848ac69abe855bd018c7ae8eaf05d61e4` runtime-evidence baseline was governance/control-plane only; historical sections retain the exact SHAs they inspected.

---

## 0. Working-document protocol

This is the detailed cumulative discovery source for the Commerce + Entitlements + Recurring Membership Pre-JIT stream.

The first-pass pressure-test sequence (`CER-PT-001...015`) and first-pass stabilisation/compression are complete. The authorised **single bounded second-pass closure round** is also complete.

All fifteen second-pass scenarios were evaluated by coverage class rather than identifier quota. Five genuinely new semantic classes were admitted as `CER-PT-016...020`; the remaining candidates either refined existing PTs or confirmed existing coverage. No third broad pressure-test round is currently recommended.

This detailed discovery is the semantically stabilised cumulative source. Renewed semantic audit `v0.2.0` passed against exact `v0.30.1`; `v0.30.2` then repaired four stale prospective references without changing doctrine; `v0.30.3` repairs only current routing/protocol text. Under the audit anti-drift rule, these exact current bytes must now receive narrow mechanical recertification. After that, the final compact pack may be regenerated and source↔compact verified without reopening semantic discovery.

Until an explicit repository handoff is authorised, this artifact remains local working/non-authoritative evidence.

For eventual repository handoff:

1. mechanically recertify exact corrected deep source `v0.30.3` under semantic audit `v0.2.0` and its anti-drift rule;
2. preserve all accepted first-pass and second-pass PT/refinement/delta provenance unchanged;
3. regenerate the final compact pack from the mechanically recertified `v0.30.3` SHA without semantic recompression drift;
4. mechanically/content-verify compact output against that exact deep-source SHA;
5. preserve the final detailed artifact as historical/working deep evidence;
6. do not silently promote working doctrine into Product, Architecture or Domain authority;
7. explicitly supersede the accidental early CER v0.1.0 “current/living” routing while preserving it as historical provenance;
8. after CER is parked, adjudicate HSP + Privacy + CER upstream deltas together before proposing governed Product amendments.

### 0.1 SemVer policy

While this remains active pre-1.0 discovery:

- **MINOR (`v0.x.0`)** — each newly accepted substantive pressure-test result, accepted working doctrine, material recommendation/reuse conclusion, or newly admitted upstream delta.
- **PATCH (`v0.x.y`)** — evidence refresh, source-baseline correction, terminology/hygiene clarification, typo correction, or non-semantic wording improvement.
- **`v1.0.0`** — not automatic. Requires an explicit decision that the deep discovery is stable enough for final compression/handoff.

The stable filename remains:

`NEWYOU_CER_PREJIT_DISCOVERY_WORKING.md`

The current SemVer is recorded in the document header and changelog.

### 0.2 Update rule after each accepted test

After every accepted pressure test or substantive decision:

1. increment SemVer;
2. add or adjust the relevant section;
3. preserve all accepted earlier findings unless explicitly superseded;
4. record any supersession/refinement clearly;
5. refresh NewYou and Store evidence baselines when the conclusion depends materially on live repository state;
6. update the pressure-test register;
7. update the Store reuse ledger where relevant;
8. update unresolved gates/deltas;
9. record the change in the changelog.

---

## 1. Scope

This stream exists to pressure-test and clarify:

- purchase/payment correctness;
- recurring billing and renewal semantics;
- provider evidence and reconciliation;
- entitlement issuance, validity, expiry, revocation and consumption;
- cancellation, retries, grace and suspension;
- refunds, disputes and chargebacks;
- membership/subscription/add-on commercial contract semantics;
- Basic/add-on/Premium composition;
- purchaser/recipient/participant/account-holder separation;
- once-off versus recurring commercial rights;
- cross-seams with Plan/review rights and professional fulfilment;
- concurrency, idempotency, retries, duplicate events, reordering, restart and recovery;
- Store Blueprint reuse/hardening opportunities.

This stream is deliberately **not**:

- implementation;
- a Feature Pack JIT dossier;
- Product Law;
- Architecture Law;
- Domain Law;
- a Roadmap amendment;
- a repository mutation permission;
- permission to redesign NewYou around Paystack;
- permission to copy Store Blueprint domain decomposition;
- permission to package/refactor Store Blueprint prematurely.

This stream does not alter the governed programme routing.

---

## 2. Canonical sources and authority hierarchy

### 2.1 NewYou

Canonical repository:

`https://github.com/JCSchoeman96/NewYou`

When current state matters:

1. inspect live GitHub;
2. read `docs/00_platform/README.md`;
3. read the current authority manifest;
4. identify current authoritative files;
5. inspect relevant current Open Work, Feature Pack and JIT artifacts.

Authority hierarchy:

Product Law  
→ Architecture Law  
→ Domain Law  
→ Roadmap  
→ supporting operating/frontend contracts  
→ current Open Work  
→ approved Feature Pack/JIT contracts  
→ proof  
→ implementation

The Delivery Atlas is derived navigation only.

### 2.2 Store Blueprint Hardening

Potential reuse/evidence repository:

`https://github.com/JCSchoeman96/Store_Blueprint_Hardening`

Store Blueprint is a moving implementation/evidence source only.

It is **not** NewYou authority.

At each material Store inspection:

1. inspect default branch;
2. inspect active relevant branches/PRs;
3. record the exact branch/head SHA used;
4. distinguish merged from in-progress work;
5. distinguish GitHub evidence from user-reported local/unpushed work;
6. record the exact baseline supporting material conclusions.

A changed Store head invalidates prior Store implementation certification for the new head, but does not itself alter NewYou doctrine.

---

## 3. Core working method

### 3.1 Authority first

For every seam:

1. determine whether current NewYou authority already answers it;
2. distinguish:
   - JIT representation choice;
   - provider-validation question;
   - operating-policy question;
   - Product/commercial-right question;
   - Domain contradiction;
   - Architecture contradiction;
3. propose new working doctrine only if genuinely missing;
4. escalate actual Product/commercial gaps as upstream deltas;
5. STOP at the correct authority layer if authority conflicts.

### 3.2 Local working identifiers

Non-governed discovery identifiers may be used:

- `CER-WH-###` — working hypothesis
- `CER-WD-###` — accepted working doctrine
- `CER-PT-###` — pressure test
- `CER-UPD-###` — upstream delta

These are not governed DEC/ARC/ARQ/OQ/FP/TB/VS/HH identifiers.

### 3.3 Dual verdict rule

Whenever Store evidence is involved, every material pressure test must produce two distinct conclusions:

1. **NewYou semantic pressure-test verdict**
2. **Store Blueprint implementation/reuse verdict**

A semantic PASS must never be read as “Store passes”.

### 3.4 Recommendation duty

This discovery is not merely an audit.

Where a real choice exists:

1. state realistic options;
2. identify authority-incompatible options;
3. compare correctness, simplicity, maintainability, recovery, concurrency and future flexibility;
4. recommend the smallest safe option;
5. explain why;
6. state trade-offs;
7. state evidence that could change the recommendation;
8. classify the recommendation as one of:
   - already required by authority;
   - working Pre-JIT doctrine requiring explicit acceptance;
   - JIT implementation recommendation;
   - Store reuse/hardening recommendation;
   - upstream Product/commercial decision.

Recommendation is not authority.

### 3.5 Provider independence rule

Use:

`NewYou commercial truth → provider-independent invariant → provider validation → adapter/mechanism`

Never:

`provider behaviour → NewYou commercial truth`

Paystack is the launch gateway, but provider state is not NewYou business authority.

---

## 4. Current authoritative ownership relevant to this stream

Current Domain Law separates:

### Commerce

Owns:

- commercial product/offer/price truth;
- purchase/payment/refund/dispute truth;
- membership/subscription/add-on commercial contract truth.

### Entitlements

Owns:

- entitlement/access grant identity;
- scope;
- source/provenance;
- validity/expiry;
- revocation;
- consumable/redemption rights;
- idempotent consumption.

### Boundary

`commercial/payment/contract truth ≠ access/right truth`

Memberships is not a separate Domain.

Cross-domain mutations go through the owning Domain.

Provider state, queue state, cache, analytics, UI projection and PubSub never silently become business authority.

---

## 5. Relevant locked Product/Decision baseline

The following existing decisions materially constrain this stream:

- `DEC-020` — purchaser, recipient, participant and account holder are distinct.
- `DEC-035` — Premium annual reassessment entitlement after 12 continuous Premium months or annual renewal; non-accumulating; expires unused with membership.
- `DEC-037` — once-off delivered Plan access is permanent.
- `DEC-038` — later repersonalisation requires another purchase or qualifying membership/add-on.
- `DEC-039` — monthly + annual billing; no default free trial; cancellation at paid-period end.
- `DEC-040` — Basic base subscription; add-ons recurring entitlements; Premium is the named Basic + add-ons bundle.
- `DEC-041` — cancellation preserves bought assessments, once-off Plans and historical check-ins; membership content/community/new adjustments end.
- `DEC-042` — Premium monthly reviews require complete check-in and do not accumulate indefinitely.
- `DEC-043` — 72-hour failed-payment grace, communication, provider-safe retries, then suspension; exact retry calls provider-validation dependent.
- `DEC-044` — gift/sponsored purchaser visibility is redemption-status only; codes expire after 12 months by default; redeemed access is non-transferable.
- `DEC-045` — refund boundaries; no ordinary membership partial-period refund.
- `DEC-046` — upgrades immediate with provider-supported proration; downgrades at renewal.
- `DEC-049` — manual EFT does not imply auto-renewal; access only after verification.
- `DEC-055` — assessment entitlement consumed only when first answer is saved.
- `DEC-292` — Paystack launch gateway; durable payment truth provider-independent in PostgreSQL; exact retry/recurring/webhook/proration/refund/dispute/chargeback/settlement behaviour must pass provider validation before implementation details are frozen.
- `DEC-285` — complimentary/sponsored access requires explicit, scoped, reasoned and auditable authority, with elevated approval for high-value, long-duration or lifetime grants.
- `DEC-297` — Platform Member Reference may assist checkout/gifting/beneficiary association but is not membership/subscription/entitlement evidence and is not a disguised coupon.
- `00_PLATFORM_v1.3.0.md §21A.9` — before redemption, support may reassign recipient email through a controlled process; sponsored bulk access may use unique redemption codes; sponsors may see aggregate redemption counts but not participant health data.

Relevant Feature Pack direction:

- FP-002 — purchase → verified payment → entitlement correctness spine.
- FP-009 — Basic Membership.
- FP-010 — Adjustment / recurring review capability.
- FP-011 — Premium packages already-proven recurring components; should not invent a second entitlement mechanism.

---

## 6. Open provider gate

### OQ-004

Exact Paystack recurring billing, webhook, retry, proration, refund, dispute/chargeback and provider-ambiguity behaviour remains unresolved.

Important rule:

OQ-004 does **not** block defining provider-independent NewYou semantics.

Correct order:

`NewYou semantics first → Paystack validation second`

Terminology guard:

- **manual EFT** in CER means the `DEC-049` manual-payment path requiring NewYou verification/matching and creating no implicit automatic-renewal authority;
- **Paystack EFT/Ozow** is a provider-mediated South African Charge API channel and remains provider evidence/adapter detail under `OQ-004`; the shared label `EFT` must not collapse these into one commercial path.

---

# 7. Accepted pressure tests

---

## CER-PT-001 — Provider succeeds; crash before entitlement convergence

### Scenario

Provider reports genuine payment success.

NewYou durably records or begins recording commercial success, then crashes before the required entitlement consequence has safely converged.

Possible crash windows:

1. provider succeeded, Commerce has not yet durably reconciled;
2. Commerce success is durable, entitlement is absent;
3. entitlement was granted, but the executing process dies before acknowledging completion.

### Required invariant

Provider success is external evidence.

Safe flow:

`provider success evidence → Commerce reconciliation → durable authoritative commercial success → Entitlements-owned consequence → one logical entitlement`

Retries/crashes may duplicate technical execution, but must not:

- fabricate commercial success;
- lose the required entitlement permanently;
- create multiple logical entitlements for the same governed right.

### Commercial truth

A successful payment remains historical commercial truth even if a later refund, reversal, dispute or chargeback changes the current commercial situation.

### Entitlement truth

An entitlement is separate durable access/right truth.

The entitlement consequence must eventually converge to one logical right where the commercial contract requires it.

### Recovery rule

There is no acceptable terminal state where money is permanently taken and the required entitlement is silently lost because retries were exhausted.

Persistent mismatch must remain visible/reconcilable until corrected or a governed commercial remedy is applied.

### NewYou verdict

**PASS**

Existing authority is sufficient.

No:

- `CER-WH`;
- `CER-WD`;
- `CER-UPD`;
- Domain change;
- Resource decision.

### Store Blueprint verdict

**CHANGES REQUIRED**

Store has strong payment apply-once mechanisms, but the current payment → subscription → entitlement path can grant entitlements post-commit and count entitlement errors as skipped without an independently proven convergence/recovery path.

### Reuse classification

**REUSE AFTER HARDENING**

### Carry-forward principle

**Commercial success and entitlement convergence are separate truths.**

A durable commercial success must not become a silent orphan with no corresponding governed access consequence.

---

### Second-pass Candidate 14 refinement — source-specific target-set convergence

Candidate 14 refines this PT from “commercial truth exists but entitlement consequence is incomplete” into an exact convergence obligation.

Where a Commerce transition establishes a new membership/add-on composition, Entitlements must converge the relevant commercial source to the exact latest authoritative target component set rather than replaying assumed worker history or applying unrelated grant/revoke commands without a shared target identity.

Retries, duplicate delivery, reordering and stale workers must not produce an older/superseded entitlement set.

Where atomic presentation is not available, incomplete convergence must not grant rights outside the new target or remove rights common to both old and new sets.

Other independently valid entitlement sources remain untouched.

## CER-PT-002 — Duplicate/replayed success while evidence paths race

### Scenario

Provider genuinely succeeds.

NewYou may observe that success through multiple channels:

- browser-triggered verification;
- webhook;
- webhook replay;
- reconciliation;
- worker retry;
- support recovery.

Multiple processes may race.

### Core question

Can many evidence-delivery paths converge on one authoritative commercial success without any delivery channel becoming business authority?

### Required invariant

Safe flow:

`many evidence observations → provider evidence validation → Commerce reconciliation → one authoritative commercial fact → durable owner-mediated consequence → one logical entitlement`

Key distinction:

`delivery identity ≠ business-effect identity`

A webhook event ID identifies a delivery/event observation.

It does not necessarily identify the business effect.

### Rejected options

**Browser return marks paid**  
Rejected. Authority-incompatible.

**Only webhook can initiate reconciliation**  
Possible provider implementation, but unnecessarily channel-dependent unless provider validation proves it sufficient and recoverable.

**Separate browser-success/webhook-success/reconciliation business transition paths**  
Rejected. Competing routes could multiply or diverge durable business consequences.

### Recommended option

Multiple verified evidence paths feed one Commerce-owned reconciliation contract.

Provider adapters/evidence acquisition may vary.

Business reconciliation semantics do not.

### NewYou verdict

**PASS**

No new working doctrine is needed.

This is a JIT implementation/architecture recommendation beneath existing authority.

### Store Blueprint verdict

**CHANGES REQUIRED**

Strengths:

- browser return/cancel read-only;
- receipt-first verified webhook;
- controller does not directly mark paid;
- worker-based reconciliation;
- WebhookReceipt / ProviderEvent / PaymentAttempt replay boundaries;
- PaymentApplication apply-once boundary.

Limitations:

1. Store proves webhook replay better than independent-channel convergence because its return route is read-only.
2. PT-001 entitlement convergence defect remains.
3. Store's order-centric paid-apply key is implementation detail and must not become NewYou doctrine.

### Reuse classification

**REUSE AFTER HARDENING**

### Carry-forward principle

**Provider delivery mechanisms may multiply; business consequences may not.**

---

## CER-PT-003 — Missing, delayed, reordered and contradictory provider evidence

### Scenario

One payment attempt experiences evidence such as:

`pending/unknown → failure-looking evidence → delayed success evidence → replayed older failure → later reconciliation`

The network arrival order is deliberately hostile.

### Rejected model

`last event received → overwrite payment.status`

This incorrectly turns network delivery order into commercial truth.

### Required dimensions

Do not collapse:

1. provider observations/evidence;
2. provider-attempt interpretation;
3. authoritative Commerce purchase/payment truth;
4. later reversal/refund/dispute truth.

### Ambiguity rule

A transport or observation problem does not prove final commercial failure.

While evidence remains genuinely ambiguous:

- do not fabricate paid;
- do not fabricate definitive failure;
- fail closed;
- reconcile.

### Failed attempt vs failed purchase

`one failed provider attempt ≠ failed commercial purchase forever`

A purchase may require another payment attempt.

Likewise a retry must not automatically create a second purchase.

### Recommended rule

Arrival order never establishes finality.

Authoritative Commerce truth comes from verified, provider-contract-aware reconciliation of the relevant payment/commercial attempt.

Exact Paystack terminality/supersession rules remain under OQ-004.

### NewYou verdict

**PASS**

Existing authority already requires ambiguity/reordering-safe reconciliation.

### Store Blueprint verdict

**CHANGES REQUIRED**

Current Store `PaymentIntent` state machine allows:

- submitted → succeeded;
- submitted → failed;
- requires_action → succeeded;
- requires_action → failed;

but does not permit failed → succeeded.

Therefore an earlier processed failure can make a later verified success for the same provider attempt non-transitionable.

That makes durable Store outcome vulnerable to evidence arrival order.

### Reuse classification

**REUSE AFTER HARDENING**

### Carry-forward principles

**Provider event order is an observation property, not a business rule.**

**A failed payment attempt and a failed purchase are not automatically the same durable truth.**

---

## CER-PT-004 — Recurring renewal replay / idempotency

### Scenario

One recurring billing period becomes due.

Execution may produce:

- duplicate scheduler observations;
- concurrent workers;
- repeated jobs;
- provider timeout after successful charge;
- retry worker;
- webhook;
- webhook replay;
- reconciliation;
- original worker retry.

Economically, only one renewal occurrence became due.

### Core invariant

**One governed renewal occurrence may require multiple technical attempts, but it must not create multiple logical renewals, multiple successful charges for the same intended collection, or multiple period extensions.**

### Critical distinction

`renewal occurrence ≠ scheduler run ≠ job ≠ provider request ≠ provider event ≠ retry number`

The durable commercial identity is the intended renewal occurrence for the governed subscription/membership contract and billing period.

### Two levels of idempotency

#### Local logical idempotency

One renewal occurrence cannot create multiple independent NewYou renewal consequences.

#### Provider mutation idempotency

Retries of the same intended collection must not become separate external charges.

### Ambiguous outbound failure

A timeout after sending a charge request means:

`NewYou did not receive a reliable answer`

It does **not** mean:

`the provider definitely did not charge`

Therefore:

`same renewal occurrence → same provider-safe collection identity → retry/verify/reconcile → one eventual commercial renewal outcome`

### Rejected options

- every scheduler run may create a fresh charge;
- Oban uniqueness is treated as business correctness;
- local renewal idempotency only while provider retries receive new independent external identities.

### Recommended option

Use a stable business renewal identity and preserve its semantic continuity through:

- scheduler replay;
- worker retry;
- local payment intent;
- provider mutation;
- callback processing;
- reconciliation.

The literal key format remains JIT/provider implementation detail.

### NewYou verdict

**PASS**

Already required by Architecture + DEC-043.

No new doctrine required.

OQ-004 remains open for exact Paystack safe-retry behaviour.

### Store Blueprint verdict

**CHANGES REQUIRED FOR NEWYOU REUSE — WITH A STRONG REUSABLE CORE**

Store demonstrates strong recurring idempotency mechanisms:

- deterministic renewal key based on subscription + billing period;
- unique RenewalAttempt identity;
- create-or-reuse semantics;
- compare-and-swap-style claim;
- deterministic renewal payment-intent identity;
- Stripe idempotency-key propagation;
- apply-once payment consequence;
- absolute-period reconciliation rather than additive period extension;
- already-reconciled renewal no-op.

Limitations:

1. provider proof is Stripe-specific, not Paystack;
2. PT-003 reordered payment outcome defect remains;
3. PT-001 Commerce → Entitlements convergence defect remains.

### Reuse classification

**REUSE AFTER HARDENING / PROVIDER ADAPTATION REQUIRED**

### Carry-forward principles

**A billing retry is not a new renewal.**

**Retries may multiply execution attempts, but the logical collection identity must remain stable across NewYou and the provider boundary.**

---

# 8. Current Store Blueprint reuse ledger

This ledger is the current broad-discovery reuse summary. It remains subject to the renewed stabilisation/completeness audit and later Store implementation evidence, but no further broad CER pressure-test round is currently planned.

| Mechanism / area | Current classification | Notes |
|---|---|---|
| Webhook receipt persistence/dedupe | REUSE AFTER HARDENING | Strong evidence ingestion pattern. |
| ProviderEvent evidence | REUSE AFTER HARDENING | Useful separation of provider observation from business consequence. |
| PaymentAttempt evidence | REUSE AFTER HARDENING | Useful provider-attempt evidence concept; exact NewYou representation remains JIT. |
| PaymentApplication apply-once boundary | REUSE AFTER HARDENING | Strong local business-effect idempotency candidate. |
| Read-only browser return | REUSE AFTER HARDENING | Consistent with browser-not-authority rule. |
| Renewal scheduler period calculation | REUSE AFTER HARDENING / ADAPT | Strong mechanism, but exact billing semantics must match NewYou and Paystack. |
| Deterministic renewal occurrence key | REUSE AFTER HARDENING / ADAPT | Strong concept; exact key format not NewYou doctrine. |
| RenewalAttempt idempotency anchor | REUSE AFTER HARDENING | Strong recurring core. |
| Renewal compare-and-swap claim | REUSE AFTER HARDENING | Strong concurrency mechanism candidate. |
| Deterministic renewal PaymentIntent identity | REUSE AFTER HARDENING | Strong retry continuity mechanism. |
| Stripe provider idempotency propagation | ADAPTATION REQUIRED | Demonstrates pattern, not Paystack compatibility. |
| Absolute-period renewal reconciliation | REUSE AFTER HARDENING | Strong replay-safe design. |
| PaymentIntent terminal-state model | NOT REUSABLE AS-IS | Failed state can block later success under reordered evidence. |
| Commerce → Entitlements post-commit convergence | REUSE AFTER HARDENING | Current Store path lacks sufficient independently proven convergence. |
| Store Subscriptions Domain decomposition | NOT REUSABLE AS NEWYOU DOMAIN LAW | NewYou already assigns contract truth to Commerce and access truth to Entitlements. |
| Membership-specific Store assumptions | ADAPTATION REQUIRED | App-specific representation must not leak into NewYou doctrine. |
| Store Stripe recurring provider proof | OUT OF SCOPE AS PAYSTACK PROOF | Useful mechanism evidence only. |
| Cancellation during past-due/grace vs in-flight renewal | ADAPTATION REQUIRED / BLOCKED FOR CERTIFICATION | Store suppresses future retries via cancel-at-period-end but can still allow an already-running renewal to reconcile and reactivate/extend; conflicts with accepted CER-UPD-001 direction. |
| Grace expiry / suspension / late-success recovery | NOT REUSABLE AS-IS / ADAPTATION REQUIRED | Store maps grace expiry to terminal `expired`, revokes entitlements and lacks `expired → active`; NewYou requires suspension to remain recoverable when late verified payment proves the same still-authorised renewal succeeded. |
| Renewal boundary cancellation/downgrade races; pending-cancellation rescission | REUSE AFTER HARDENING / ADAPTATION REQUIRED | Store reuses useful pending plan/price machinery, but queued renewal workers do not re-check `cancel_at_period_end`, period-end cancellation closure is not proven, mutable pending terms can rewrite the contract applied during later reconciliation, and the inspected user/admin surfaces do not expose a governed undo/resume transition for a pending period-end cancellation. |
| Refund after entitlement issuance / partial benefit use | CHANGES REQUIRED / REUSE AFTER HARDENING | Store has a strong financial refund core, but generic refund eligibility cannot replace NewYou Product policy; generic digital revocation policy is not NewYou entitlement law; post-refund revocation convergence and Paystack refund-event adaptation require hardening. |
| Dispute/chargeback after benefit consumption | CHANGES REQUIRED / NOT REUSABLE FOR THIS SEMANTIC AS-IS | Store has reusable provider-event evidence/dedupe and some financial-reversal machinery, but no proven dispute/chargeback business lifecycle, source-scoped entitlement hold/restore, recurring-contract dispute handling or final chargeback-to-Entitlements convergence. |
| Basic + add-on → Premium composition / contract identity | CHANGES REQUIRED / ADAPTATION REQUIRED — STRONG ENTITLEMENT REUSE CORE | Store's source-aware EntitlementGrant/effective-set model is strongly reusable, but one SubscriptionPlan currently yields one entitlement and subscription creation is line-oriented; NewYou needs one authoritative membership composition with component rights and source→target delta transitions rather than competing Basic/add-on/Premium subscriptions. |
| Gift/sponsored purchaser/recipient/participant separation | CHANGES REQUIRED / ADAPTATION REQUIRED | Store's payer→subscription-user→grantee assumption is insufficient for NewYou gifts/sponsorship. Payment/idempotency/source-aware entitlement mechanisms remain reusable; dedicated redemption, purchaser≠grantee and recurring-sponsor semantics require adaptation. |
| Manual EFT verification / recurring-right boundaries | ADAPTATION REQUIRED / REUSE GENERIC PAYMENT CORE | Durable payment/application/idempotency mechanisms remain useful, but the inspected PaymentIntent/provider model is provider-oriented and does not prove manual bank evidence ingestion, human verification, unmatched/under/over/duplicate EFT reconciliation or NewYou's no-implicit-renewal semantics. |
| Entitlement expiry/revocation racing in-flight Plan/review fulfilment | ADAPTATION REQUIRED — GENERIC GRANT MECHANICS ONLY | Store has reusable grant identity, expiry, explicit revocation and idempotent issuance mechanics, but no proven Request-to-entitlement binding or durable already-admitted fulfilment obligation that survives ordinary expiry; generic `active/expired/revoked` grant state is insufficient for NewYou Plan/review semantics. |
| Queued plan/variant change | REUSE AFTER HARDENING FOR DOWNGRADES ONLY | Store's pending change mechanism aligns with renewal-boundary downgrade semantics, but not with NewYou's immediate prorated upgrades. |
| Renewal reconciliation against mutable `pending_*` contract fields | NOT REUSABLE AS-IS / CORRECTNESS DEFECT | A paid renewal can reconcile against plan/price values that changed after the renewal checkout was priced; the applied commercial contract must be bound to the terms actually authorised and charged. |
| Long-outage recovery / terminal Commerce→Entitlements convergence | CHANGES REQUIRED / REUSE AFTER HARDENING — STRONG RECOVERY CORE | Store has durable webhook evidence, stable renewal identity, paid-renewal reconciliation, paid-order ensure workers and pending-provider-setup recovery. Hardening is still required so lost post-commit enqueue, finite worker exhaustion and late failed→success evidence cannot leave a durable commercial obligation undiscoverable or terminally orphaned. |
| Monthly ↔ annual billing cadence transition | CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED | Store has cadence-aware SubscriptionPlan fields and pending target-plan/change-effective-at machinery, but current mutable pending-plan reconciliation cannot prove that the cadence/price applied at renewal is the immutable contract actually authorised and charged. Boundary-effective cadence change in either direction is conceptually reusable only after the PT-007/PT-008 immutable renewal-contract hardening. |
| Existing-member recurring price/version migration | CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED | Store has useful per-subscription renewal amount/currency snapshots and pending renewal amount/currency fields, but `SubscriptionPlan.amount_minor` remains mutable and current implementation does not prove explicit price-version migration, grandfathering provenance, advance effective-boundary eligibility or immutable per-renewal price contract. |
| Recurring promotional pricing lifecycle | CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED | Store has strong deterministic transaction-pricing primitives, persisted promotion provenance, eligibility windows and stacking/exclusivity rules, but does not prove first-N-paid-period recurring promotion consumption, remaining promotional scope, package/cadence applicability, post-termination treatment or immutable preservation of an accepted recurring promotional promise after public promotion mutation. |
| Concurrent duplicate ordinary membership purchase / excess collection | CHANGES REQUIRED / REUSE AFTER HARDENING | Store has a useful pre-purchase membership admission guard checking open memberships and pending membership orders, but inspected durable Subscription identities are source-order-line and provider-subscription based; concurrency-safe exclusion of two distinct ordinary membership purchases is not proven, nor is duplicate successful-charge remediation convergence. |
| Payment-method / reusable-authorisation replacement during renewal | CHANGES REQUIRED / REUSE AFTER HARDENING | Store has a strong stable RenewalAttempt identity and a dedicated subscription payment-method update flow, but existing PaymentIntent lifecycle still lacks failed→succeeded reconciliation and current evidence does not prove old/new instrument attempts cannot both succeed for one renewal. |
| Failed immediate-upgrade adjustment/payment | CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING | Store has current/pending contract fields and plan-target validation, but current inspected paths do not prove NewYou's success-gated current-period upgrade semantics, immutable proration/adjustment identity, stale-basis revalidation or late-success correction. |
| Multiple future membership changes before one renewal boundary | CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING | Store can compose pending plan/variant targets, but mutable pending fields plus separate cancellation state do not prove immutable supersession history, stale-action detection, concurrency-safe version ordering, cancellation supersession of old targets or rescission without hidden-target resurrection. |
| Ordinary membership add-on recurring lifecycle | CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING | Store has strong subscription billing/payment primitives and immutable SubscriptionItem order snapshots, but inspected evidence does not provide an authoritative current add-on component lifecycle, aligned add/remove semantics, success-gated mid-period addition, component-specific cancellation, or Premium composition without duplicate billing obligations. |
| Gift/sponsor overlap with already-active membership | CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING | Store's EntitlementGrant has useful source-aware identity and bounded validity, but the current source-kind enum is subscription-only and the reviewed branch does not prove gift/sponsor provenance, pre-redemption overlap evaluation, future-dated activation, funding-source substitution, no-double-billing, sponsorship fallback or exact overlap redemption concurrency. |
| Premium reassessment continuity / annual maturity | NEWYOU-SPECIFIC ADAPTATION REQUIRED; overall Store reuse remains CHANGES REQUIRED / REUSE AFTER HARDENING | Store exposes durable subscription renewal periods and source-aware entitlement grants, but does not and should not own NewYou-specific 12-month Premium qualification, anniversary maturity or reassessment nonaccumulation policy. Current Store head `54871ef3...` is governance-only over prior runtime baseline. |
| Partial Commerce→Entitlements convergence during composition change | CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING | Store has reusable source-aware grant primitives, but current orchestration issues/revokes grants individually, does not prove source-specific target-set convergence or stale-version rejection, and uses a cached entitlement snapshot whose correctness/invalidation semantics require proof before NewYou reuse. |
| Multiple legitimate paid/gift/sponsored/complimentary/lifetime entitlement sources | CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING | Store has reusable source-aware grant identity and union-style boolean access, but current source taxonomy is subscription-only and does not prove membership-coverage-vs-access-overlay semantics, multi-source limited-benefit multiplicity, additive grant rules, or general consumable-source reconciliation. NewYou-specific Premium/review policy must remain outside the reusable Store package. |

---

# 9. Cross-stream seams to preserve

## 9.1 Health / Safety / Plans

Do not duplicate or silently redefine existing HSP upstream seams.

Relevant known cross-seams are:

- `HSP-UPD-001` — a time-scoped membership Plan/review benefit is validly admitted before entitlement expiry but remains in flight afterwards;
- `HSP-UPD-005` — genuinely unfulfillable paid Plan and the customer remedy;
- `HSP-UPD-006` — bounded professional-review delay/capacity failure and resulting remedy;
- `HSP-UPD-007` — refund boundary where Plan generation precedes professional approval/delivery;
- `HSP-UPD-008` — participant materially changes intent after paid admission but before first fulfilment.

Where CER pressure tests touch these, preserve HSP ownership and refer back to the exact HSP seam rather than creating competing doctrine. `CER-PT-014` therefore remains `BLOCKED / STOP — EXISTING HSP-UPD-001` and creates no duplicate CER delta.

## 9.2 Privacy / Consent / Data Lifecycle

Do not duplicate or supersede the Privacy stream's full-deletion/recurring-commerce policy work.

Relevant cross-seam:

- `PRIV-WD-002` / `PRIV-UPD-002` — Full Deletion versus active recurring commercial collection and the surviving restricted financial/dispute evidence required to reconcile lawful Commerce truth.

CER preserves the following relationship:

- `CER-PT-004` supplies stable recurring logical-collection/idempotency semantics;
- `CER-PT-005` supplies cancellation/late-collection precedence for unresolved renewal authority;
- `CER-PT-015` supplies recovery/reconciliation doctrine for late or interrupted evidence;
- Privacy retains authority over deletion timing, deletion suppression, retention minimisation and which restricted financial/dispute evidence may lawfully survive deletion.

A late financial operation that must truthfully reconcile after Full Deletion must not silently recreate Entitlements or product access. Exact deletion policy remains owned by the Privacy stream.

---
# 10. Current unresolved gates and accepted upstream deltas

## Provider validation

### OQ-004

Still required for exact Paystack:

- recurring billing;
- retry semantics;
- idempotency support;
- webhook semantics;
- provider ambiguity;
- proration;
- refunds;
- disputes/chargebacks;
- settlement/reconciliation.

## Accepted upstream Product/commercial deltas

Thirteen accepted Pre-JIT upstream deltas are present. They remain **working/non-authoritative inputs** for later cross-stream adjudication; they must not be mechanically promoted as thirteen separate Decision entries.

| Delta | Current working subject | Likely later governance cluster |
|---|---|---|
| `CER-UPD-001` | Cancellation during failed-renewal grace; late-success precedence | Renewal / cancellation / cadence contract |
| `CER-UPD-002` | Dispute/chargeback commercial-right consequences | Disputes / reversal |
| `CER-UPD-003` | Gift/sponsored redemption transfer, post-redemption control, recurring sponsorship authority | Gift / add-on / package / multi-source coverage |
| `CER-UPD-004` | Manual-EFT paid-period commencement | Manual EFT |
| `CER-UPD-005` | Monthly ↔ annual cadence transition | Renewal / cancellation / cadence contract |
| `CER-UPD-006` | Rescission of pending period-end cancellation | Renewal / cancellation / cadence contract |
| `CER-UPD-007` | Existing-member recurring price migration / grandfathering boundary | Price / recurring offer terms |
| `CER-UPD-008` | Recurring promotional pricing lifecycle | Price / recurring offer terms |
| `CER-UPD-009` | Duplicate ordinary membership purchase and excess collection | Wrong / duplicate collection remedy |
| `CER-UPD-010` | Ordinary membership add-on recurring lifecycle | Gift / add-on / package / multi-source coverage |
| `CER-UPD-011` | Gift/sponsored membership overlap with existing membership | Gift / add-on / package / multi-source coverage |
| `CER-UPD-012` | Premium reassessment continuity, maturity and nonaccumulation | Premium continuity benefit |
| `CER-UPD-013` | Multi-source entitlement overlap and grant commercial effect | Gift / add-on / package / multi-source coverage |

Later governed Product work should reconcile overlapping deltas into the smallest coherent ruleset. In particular, `CER-UPD-011` and `CER-UPD-013` intentionally overlap and must not become competing authorities.

All thirteen detailed accepted directions are recorded in §12. No implementation may depend on them as Product Law until the applicable upstream adjudication/amendment is completed.

## Conditional downstream questions — not a third broad CER round

No additional broad Product delta is currently admitted.

Two conditional seams remain for later JIT/provider/upstream adjudication if the chosen mechanism makes them material:

- provider inability to automatically reverse a post-cancellation late collection is handled first through the accepted wrong-collection/reversal/remedy model (`CER-UPD-001` / `CER-UPD-009`) plus `OQ-004`; it does not currently justify another broad PT;
- **only if NewYou selects merchant-managed proration:** Product authority may need to lock the monetary proration basis (time basis, price-version basis, rounding and applicable tax treatment) rather than leaving customer-money semantics solely to implementation.

These are bounded downstream questions, not permission to begin `CER-PT-021` or a third broad discovery cycle.

---

# 11. Pressure-test register

| ID | Topic | Current consolidated NewYou verdict | Store verdict | Status |
|---|---|---|---|---|
| CER-PT-001 | Provider success + crash before entitlement convergence | PASS; Candidate 14 adds target-set convergence refinement | CHANGES REQUIRED | ACCEPTED / REFINED |
| CER-PT-002 | Duplicate/replayed success across racing evidence paths | PASS | CHANGES REQUIRED | ACCEPTED |
| CER-PT-003 | Missing/delayed/reordered/contradictory provider evidence | PASS | CHANGES REQUIRED | ACCEPTED |
| CER-PT-004 | Recurring renewal replay/idempotency | PASS; same renewal occurrence retains one governed billing-period identity | CHANGES REQUIRED FOR NEWYOU REUSE; strong reusable core | ACCEPTED / CLARIFIED |
| CER-PT-005 | Failed renewal + 72h grace + cancellation + late successful retry | BLOCKED / STOP — `CER-UPD-001` accepted | BLOCKED FOR REUSE CERTIFICATION / ADAPTATION REQUIRED | ACCEPTED |
| CER-PT-006 | Retry exhaustion / suspension / late provider success after suspension | PASS; related cancellation exception remains `CER-UPD-001`; no originating upstream delta | CHANGES REQUIRED / ADAPTATION REQUIRED | ACCEPTED / CLARIFIED |
| CER-PT-007 | Immediate upgrade + proration + concurrent renewal/change | PASS — provider validation still required | CHANGES REQUIRED / ADAPTATION REQUIRED | ACCEPTED |
| CER-PT-008 | Downgrade/cancel-at-period-end racing renewal; rescission of pending cancellation | Original boundary ordering PASS; rescission refinement BLOCKED / STOP — `CER-UPD-006` accepted | CHANGES REQUIRED / ADAPTATION REQUIRED | ACCEPTED / REFINED |
| CER-PT-009 | Refund after entitlement issuance / partial benefit use | PASS; cross-stream HSP remedy seams remain separately governed | CHANGES REQUIRED / REUSE AFTER HARDENING | ACCEPTED |
| CER-PT-010 | Chargeback/dispute after benefit consumption | BLOCKED / STOP — `CER-UPD-002` accepted | CHANGES REQUIRED / NOT REUSABLE FOR THIS SEMANTIC AS-IS | ACCEPTED |
| CER-PT-011 | Basic + add-on → Premium composition and contract identity | Original composition invariant PASS; later add-on/multi-source refinements BLOCKED / STOP — `CER-UPD-010` and `CER-UPD-013` accepted | CHANGES REQUIRED / ADAPTATION REQUIRED — strong entitlement reuse core | ACCEPTED / REFINED |
| CER-PT-012 | Gift/sponsored purchase: purchaser/recipient/participant separation | BLOCKED / STOP — originating `CER-UPD-003`; later overlap refinements `CER-UPD-011` and `CER-UPD-013` accepted | CHANGES REQUIRED / ADAPTATION REQUIRED | ACCEPTED / REFINED |
| CER-PT-013 | Manual EFT + verification + recurring-right boundaries | BLOCKED / STOP — `CER-UPD-004` accepted | ADAPTATION REQUIRED / REUSE GENERIC PAYMENT CORE | ACCEPTED |
| CER-PT-014 | Entitlement expiry/revocation racing in-flight Plan/review fulfilment | BLOCKED / STOP — existing `HSP-UPD-001`; no duplicate CER delta | ADAPTATION REQUIRED — generic grant mechanics only | ACCEPTED |
| CER-PT-015 | Recovery/reconciliation after long outage/backlog/reordered provider events | PASS; Candidate 14 adds latest-target recovery refinement | CHANGES REQUIRED / REUSE AFTER HARDENING — strong recovery core | ACCEPTED / REFINED |
| CER-PT-016 | Monthly ↔ annual billing cadence transition | BLOCKED / STOP — `CER-UPD-005` accepted and broadened bidirectionally | CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED | ACCEPTED / REFINED |
| CER-PT-017 | Existing-member recurring price/version migration | BLOCKED / STOP — `CER-UPD-007` accepted; legal/consumer-protection expert gate required | CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED | ACCEPTED |
| CER-PT-018 | Recurring promotional pricing lifecycle | BLOCKED / STOP — `CER-UPD-008` accepted | CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED | ACCEPTED |
| CER-PT-019 | Concurrent duplicate ordinary membership purchase / two genuine successful charges | BLOCKED / STOP — `CER-UPD-009` accepted | CHANGES REQUIRED / REUSE AFTER HARDENING | ACCEPTED |
| CER-PT-020 | Premium reassessment continuity and annual maturity | BLOCKED / STOP — originating `CER-UPD-012`; multi-source refinement `CER-UPD-013` accepted | NEWYOU-SPECIFIC ADAPTATION REQUIRED; overall Store reuse remains CHANGES REQUIRED / REUSE AFTER HARDENING | ACCEPTED / REFINED |

`CER-PT-001...020` are complete at the current broad-discovery scope. The authorised second-pass closure round is complete. Remaining CER work is stabilisation/completeness verification, final compression, compression verification and parking — not automatic creation of `CER-PT-021`.

---

# 12. Accepted upstream deltas

## CER-UPD-001 — Cancellation during failed-renewal grace and late-success precedence

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-005`.
- **Why upstream:** Current Product authority defines cancellation at the end of a paid period (`DEC-039`) and a 72-hour failed-payment grace/retry lifecycle (`DEC-043`) but does not define which commercial intent wins when cancellation occurs during grace while a renewal collection is unresolved or already in flight.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. A later governed Product amendment must carry the decision into authority before downstream implementation may rely on it.

### 12.1 Accepted policy direction

The accepted recommended direction is:

> **Cancellation during a failed-renewal grace window is effective immediately because the preceding paid period has already ended. It withdraws authority for unresolved future renewal collection and ends membership-only grace access. If a renewal was already authoritatively verified-paid before cancellation, the resulting paid period remains and cancellation takes effect at its end. Otherwise, any provider collection reconciled after cancellation must not reactivate the membership and must enter full reversal/refund or governed commercial-remedy handling.**

This direction deliberately makes Commerce authoritative rather than provider/network timing.

### 12.2 Consequences of the accepted direction

#### A. Grace is not an additional successfully paid period

The 72-hour grace period is a temporary recovery condition following failed renewal.

It does not become a new paid period merely because access continues temporarily.

#### B. Cancellation during grace is immediately effective

Once Commerce durably accepts cancellation during failed-renewal grace:

- membership continuation authority ends;
- membership-only grace access ends;
- no new renewal collection may be initiated;
- queued retries must not proceed as new collection authority;
- already-running/in-flight work must revalidate current commercial authority before applying a renewal consequence.

Permanent/purchased rights continue according to existing Product authority.

#### C. Verified-paid before cancellation

If Commerce had already authoritatively established the renewal as verified-paid before cancellation was durably accepted:

`renewal verified-paid → new paid period exists → cancellation applies at that paid-period end`

This remains ordinary cancellation-at-period-end semantics.

#### D. Cancellation before authoritative renewal success

If, at the moment cancellation is durably accepted, the renewal remains:

- pending;
- failed;
- ambiguous;
- provider-in-flight;
- observed-success-but-not-yet-authoritatively-reconciled;

then cancellation wins for **contract continuation**.

A later provider success may establish real money movement, but it must not silently recreate or reactivate the membership contract.

#### E. Late provider collection

A provider collection that is reconciled only after cancellation has already withdrawn renewal authority must:

1. remain durable commercial/payment evidence;
2. not reactivate the membership;
3. not extend the membership period as an ordinary successful renewal;
4. enter full reversal/refund where technically possible;
5. otherwise remain a visible governed commercial exception requiring reconciliation/support resolution.

This is not an ordinary partial-period refund request. It is correction/remedy for a collection that no longer had current renewal authority at the point NewYou accepted cancellation.

### 12.3 Concurrency rule

Do not make wall-clock/provider ordering alone decide the contract.

The relevant control boundary is the Commerce-owned authoritative transition:

`renewal commercially verified-paid`
versus
`cancellation durably accepted`

Provider timestamps, webhook order and worker timing are evidence used in reconciliation; they are not independent commercial authority.

### 12.4 Architecture/JIT implication

The accepted Product direction implies—but does not yet freeze implementation—that downstream recurring execution must re-read current commercial authority around irreversible collection/consequence boundaries.

It does **not** mandate:

- a particular Resource;
- a specific transaction shape;
- a specific lock;
- a specific queue;
- a specific Paystack API;
- a generic cancellation worker.

Those remain downstream Architecture/JIT/provider-validation choices.

---

## CER-UPD-002 — Dispute/chargeback access and commercial-right consequences

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-010`.
- **Why upstream:** Current authority assigns dispute/chargeback reconciliation to Commerce and leaves exact Paystack mechanics behind OQ-004, but it does not define participant access while a payment is contested, the effect of a final chargeback loss on future rights, or whether permanent once-off access survives reversal of the sole qualifying purchase.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. A later governed Product amendment must carry the decision into authority before downstream implementation may rely on it.

### 12.5 Accepted policy direction

The accepted recommended direction is:

> **A payment dispute is a contested Commerce state, not immediate proof that the original payment or customer right was invalid. Opening a verified dispute must not erase historical payment, fulfilment, entitlement consumption or retained records, and must not trigger account-wide punishment. While a dispute is unresolved, NewYou should place only new or continuing value that materially depends on the disputed payment into a reversible source-scoped hold, while preserving already-delivered historical artifacts and required professional/safety records. If the dispute resolves in NewYou's favour, the hold is removed and the original commercial right resumes without duplicate grant. If the dispute is accepted or finally lost and the funds are reversed, Commerce records a financial reversal; future rights whose sole commercial source was that payment end or become non-active, but historical consumption and retained records remain immutable. A dispute against an expired historical period must not invalidate later independently paid periods. A final reversal must not itself imply fraud, debt, account-wide suspension or permanent account ban without separate governed authority.**

For once-off purchased artifacts, the accepted working clarification is:

> **“Permanent access” means non-expiring access while the qualifying purchase remains commercially valid. A later final chargeback reversal may end future paid-origin platform access without deleting historical fulfilment, provenance, professional/safety records or other records that must remain retained.**

### 12.6 Consequences of the accepted direction

#### A. Dispute opened is not final reversal

A verified dispute creates contested commercial state. It does not make the original successful payment historically false.

#### B. Pending consequences are reversible and source-scoped

Only new or continuing value materially dependent on the disputed payment should be held while the dispute is unresolved. Unrelated purchases, later independently paid periods and account-wide access must not be silently affected.

#### C. Merchant-favour resolution

If the dispute resolves in NewYou's favour, the original commercial right continues and any held rights resume without repurchase or duplicate entitlement issuance.

#### D. Customer-favour/final-loss resolution

If the dispute is accepted or finally lost and funds are reversed:

- Commerce records both the historical successful payment and the later reversal;
- future rights whose sole commercial source was that payment end or become non-active;
- historical benefit consumption and fulfilment remain true;
- required retained/professional/safety records remain;
- no fraud finding, debt status, account-wide suspension or permanent ban follows automatically.

#### E. Historical recurring periods do not poison later valid periods

A chargeback against an old paid period must not invalidate later periods that have separate valid commercial authority.

### 12.7 JIT/provider implication

Downstream JIT must define the exact source-scoped hold/release/reversal mechanism and the recurring-contract materiality test. OQ-004 must still validate Paystack dispute event types, payloads, merchant response deadlines, evidence submission, partial dispute amounts, financial debit timing, finality and reconciliation after missed/reordered events.

No specific Resource, state enum, lock, worker or provider API shape is frozen here.

---

## CER-UPD-003 — Redemption transfer, post-redemption control and recurring sponsorship authority

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-012`.
- **Why upstream:** Current Product authority separates purchaser, recipient, participant and account holder; limits purchaser/sponsor visibility; and makes redeemed access non-transferable, but it does not define who may revoke/refund an already-redeemed gift or sponsored right, nor whether a gift purchase may create continuing recurring debit authority against a different payer.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. A later governed Product amendment must carry the decision into authority before downstream implementation may rely on it.

### 12.8 Accepted policy direction

The accepted recommended direction is:

> **Gift and sponsored purchase roles remain distinct across the full commercial lifecycle. Before redemption, the purchaser or sponsor controls only the unredeemed commercial allocation subject to applicable refund, reassignment, expiry and sponsorship terms. Redemption is an authoritative one-time transfer boundary: it binds the governed right to the resolved recipient/account holder, consumes the redemption authority and makes the resulting access non-transferable. After redemption, the purchaser or sponsor may see only the Product-authorised redemption/commercial status and may not ordinarily revoke the recipient's redeemed access or obtain participant health, assessment, Plan, check-in or activity data merely because they funded it. Participant-side refund or access decisions for an already-redeemed benefit belong to the recipient/participant under the applicable Product refund rules, while any resulting financial reversal is reconciled against the original purchase/payment source without exposing the participant's protected information to the purchaser. Payment corrections, fraud/security handling, disputes, chargebacks and other authoritative financial reversals remain governed separately and may affect the redeemed right according to their existing rules.**
>
> **Gifted membership is fixed-duration/prepaid by default and must not silently create recurring debit authority against the purchaser. Recurring sponsorship is allowed only through separate explicit payer consent. In an explicitly recurring sponsored relationship, the payer may stop future billing, but ordinary cancellation does not retroactively revoke the recipient's already-paid period. Sponsored grants already redeemed follow the validity/expiry terms fixed for that grant; sponsor changes normally affect future or unredeemed allocations unless Product Law or the pre-disclosed sponsored contract explicitly authorised earlier revocation. A recipient may decline or stop using sponsored access without granting the sponsor visibility into protected participant information.**

### 12.9 Consequences of the accepted direction

#### A. Purchase is not participant entitlement

Successful payment for a gift/sponsored allocation creates commercial/redemption authority, not a false temporary entitlement for the purchaser. Entitlements are issued to the resolved grantee only after authoritative redemption.

#### B. Redemption is durable and exactly-once

One redemption authority may create at most one authoritative redeemed grant. Technical retries may reproduce the same result, but may not allocate the same right to multiple grantees. Recipient-routing data such as an email address does not replace canonical grantee identity owned by Identity & Access.

#### C. Post-redemption payer control is limited

After redemption, ordinary purchaser/sponsor change-of-mind is not sufficient authority to revoke another person's redeemed access. Legitimate payment corrections, fraud/security handling, disputes and chargebacks remain separate Commerce lifecycles and may have access consequences under their own governed rules.

#### D. Refund authority and settlement destination are separate

A recipient/participant may hold the participant-side authority for an eligible refund after redemption, while the monetary settlement still reconciles against the original purchase/payment source. That financial relationship does not grant the purchaser access to protected participant facts.

#### E. Sponsor reporting remains aggregate/bounded

Sponsor payment authority does not create participant-data authority. Aggregate redemption status may be exposed where Product Law permits; participant health, assessment, Plan, activity or other protected data does not follow from funding.

#### F. Fixed validity is not discretionary revocation

A redeemed sponsored grant may expire at its pre-disclosed validity boundary. A later sponsor decision to revoke it early is a separate authority and must not be inferred from sponsorship alone.

#### G. Ordinary gifts do not silently become subscriptions

Gifted membership is fixed-duration/prepaid by default. Continuing recurring sponsorship requires separate explicit payer consent. In that explicit mode, the payer may stop future billing, while the recipient keeps the already-paid period under ordinary cancellation semantics.

#### H. Refund/cancellation versus redemption needs one ordering

If cancellation/refund of an unredeemed allocation becomes authoritative first, redemption fails closed. If redemption becomes authoritative first, the resulting recipient right is real and ordinary purchaser change-of-mind may not silently revoke it.

### 12.10 Domain/JIT implication

No Gift, Sponsor or Redemption Domain is justified. Durable truths remain with their existing owners:

- Commerce — purchase, payer, payment, refund and recurring financial contract;
- Entitlements — redemption authority, grant, grantee, validity, expiry and revocation;
- Identity & Access — canonical grantee identity;
- protected participant domains — participant data and activity.

Downstream JIT must define the exact redemption/admission concurrency mechanism, source/provenance representation, bulk sponsorship allocation handling and recurring-sponsored-payer representation without weakening these boundaries.

---

## CER-UPD-004 — Manual-EFT paid-period commencement

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-013`.
- **Why upstream:** `DEC-049` requires payment verification before access and prohibits automatic renewal from manual EFT, but current Product authority does not define whether an ordinary membership period is measured from bank transfer/receipt, later verification/activation, or some other boundary when those dates differ. That determines the participant's purchased access duration and therefore cannot be left to an incidental implementation timestamp.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. A later governed Product amendment must carry the decision into authority before downstream implementation may rely on it.

### Accepted policy direction

> **For an ordinary on-demand manual-EFT membership purchase, the paid access period begins when the payment is authoritatively verified and the membership can lawfully activate, rather than when the bank transfer was initiated or first received. A different commencement date may apply only where the purchased offer explicitly defines a fixed or scheduled service period before purchase. Delayed manual verification must not silently shorten the purchased access duration.**

### Consequences

For ordinary on-demand membership, verification/activation is the paid-period commencement boundary. NewYou's own verification latency therefore does not consume part of the purchased duration before access is available.

This rule does not erase or alter the actual bank transaction date; financial evidence and commercial access-period truth remain separate facts.

An explicitly scheduled product may retain its disclosed service/calendar boundary where that timing was part of the offer before purchase. The fixed-period exception must not become a backdoor for silently shortening an ordinary on-demand membership.

The accepted direction does not define accounting recognition, bank settlement, Finance SLAs, reconciliation data structures, payment-intent representation or UI. Those remain downstream.

### Related rules preserved

- Manual EFT still creates no automatic renewal authority.
- Access still requires authoritative verification.
- A later recurring method requires separate explicit payer authorisation.
- Duplicate/under/over/late bank evidence remains Commerce reconciliation truth and does not independently create entitlement.

---


## CER-UPD-005 — Membership billing-cadence transition

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-016`, refined by second-pass Candidate 2.
- **Why upstream:** Current Product authority supports monthly and annual billing (`DEC-039`) and separately governs upgrades/downgrades (`DEC-046`) but does not define how same-composition cadence changes in either direction affect the current paid period, renewal boundary, credit/refund/proration, target-period commencement or ordering against an already-committed renewal. Those choices determine customer money and purchased duration and therefore cannot be left to incidental implementation.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. A later governed Product amendment must carry the decision into authority before downstream implementation may rely on it. Existing-member price/version migration was subsequently resolved in this discovery by Candidate 5 / `CER-UPD-007`; Premium continuity/reassessment implications were subsequently resolved by Candidate 13 / `CER-PT-020` / `CER-UPD-012`.

### Accepted policy direction

> **A change between monthly and annual billing for the same membership composition is, by default, a future renewal instruction and does not create a second membership contract or revoke/regrant unchanged membership entitlements. The current paid period remains authoritative through its existing end regardless of whether that period is monthly or annual; ordinary cadence change does not truncate already-purchased time or create an implicit refund, credit or overlapping billing obligation. At the next not-yet-committed renewal boundary, exactly one renewal occurs under the newly selected cadence. If the previous-cadence renewal has already become authoritatively paid before the cadence-change instruction wins the boundary ordering, that resulting paid period remains truthful and the new cadence targets the following not-yet-committed boundary. Any Product option for early/immediate cadence conversion must separately define paid-time termination, refund/credit/proration, new-period commencement and failed/ambiguous adjustment treatment before implementation. Cadence change alone must not interrupt unchanged entitlement rights.**

### Consequences

#### A. Same membership composition remains one commercial relationship

Cadence change is not permission to create two parallel membership contracts for the same intended membership composition.

#### B. Current paid time is preserved in either direction

Monthly→annual preserves the current monthly paid period through its existing end.

Annual→monthly preserves the current annual paid period through its existing end.

Ordinary cadence change creates no implicit forfeiture, refund, credit or overlapping billing obligation.

#### C. Boundary-effective new cadence

If the cadence instruction becomes authoritative before the relevant renewal occurrence is commercially committed:

`current paid period ends → exactly one renewal under the newly selected cadence`

The new cadence's paid period begins at that effective boundary.

#### D. Renewal-ordering rule

Cadence selection and renewal require one Commerce-owned ordering.

If the new cadence wins before the previous-cadence renewal becomes authoritatively committed/paid, the stale previous-cadence renewal must not execute as the governing renewal.

If the previous-cadence renewal becomes authoritatively paid first, that resulting paid period remains truthful and the new cadence moves to the next not-yet-committed boundary.

Queued work, stale workers, mutable provider state and callback arrival order do not decide the commercial contract.

#### E. Entitlement continuity

Where membership composition is unchanged, cadence change alone must not revoke/reissue unchanged membership rights.

An already-earned entitlement whose validity depends on membership continuing does not expire merely because billing cadence changes, unless its own governing Product rule says otherwise.

Candidate 13 subsequently resolved `DEC-035` continuity/annual-renewal trigger semantics through `CER-PT-020` / `CER-UPD-012`.

#### F. Cancellation and supersession

A later authoritative cancellation-at-period-end instruction may supersede a pending future cadence renewal, subject to the existing PT-008 boundary-ordering doctrine.

More complex multiple-future-instruction supersession was subsequently resolved by Candidate 10 as a refinement of `CER-PT-008`.

#### G. Price/version question remains separate

This delta does not decide whether a target cadence price selected before the boundary is locked, migrated, grandfathered or subject to later notice/acceptance.

Candidate 5 subsequently resolved that Product/commercial seam through `CER-PT-017` / `CER-UPD-007`.

#### H. Early/immediate conversion remains a distinct Product option

A later Product decision may permit immediate monthly→annual or annual→monthly conversion.

If so, Product must first define, as applicable:

- treatment of remaining paid value;
- early termination of an annual period;
- refund versus credit;
- proration basis;
- target-period commencement;
- failed or ambiguous financial adjustment consequence.

Provider support is then validated under `OQ-004`; provider capability does not create the Product rule.

### Store/JIT implication

Store's cadence-aware plans, pending target-plan fields and boundary-effective change machinery remain useful reuse evidence in both directions.

However, NewYou must not reuse a flow where mutable pending plan/price/cadence state can rewrite the contract applied to a payment that was actually priced/authorised under older terms.

Downstream JIT must bind each renewal occurrence to an immutable priced/charged contract snapshot and revalidate the current future instruction before the irreversible renewal boundary.

No specific Resource, worker, lock, provider object or queue topology is frozen here.

---


## CER-UPD-006 — Rescission of pending membership cancellation

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** second-pass Candidate 3; refinement of `CER-PT-008`.
- **Why upstream:** Current Product Law (`DEC-039`) establishes period-end cancellation but does not state whether a pending cancellation is revocable before the membership actually terminates. That choice determines whether future renewal remains authorised and whether the participant will be charged again, so it is a customer-facing commercial promise rather than incidental implementation.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. A later governed Product amendment must carry the rule into authority before downstream implementation may rely on it. Post-termination re-subscription was subsequently coverage-confirmed by Candidate 4; generalized multiple-future-instruction supersession was subsequently resolved by Candidate 10 as a refinement of `CER-PT-008`.

### Accepted policy direction

> **A period-end membership cancellation is a revocable future non-renewal instruction until the membership has actually terminated or the relevant commercial boundary has otherwise become irreversibly resolved. While the existing paid membership remains live, an authenticated participant may rescind the pending cancellation and replace the future instruction with renew-unchanged. Rescission preserves the same membership relationship, current paid period and unchanged entitlement continuity; it does not create a new membership or paid period. Historical cancellation and rescission instructions remain auditable, but only the current authoritative future instruction governs renewal. Rescission is prospective: it must not retroactively authorize a collection that occurred after cancellation had already withdrawn renewal authority. If the membership has already terminated, continuation is a new re-subscription journey rather than cancellation rescission. Restoring membership renewal intent does not itself restore any separately revoked or invalid payment authority.**

### Consequences

#### A. Pending cancellation remains future intent, not present termination

While the paid membership remains live:

`cancel at period end`

means:

`future instruction = do not renew`

It does not itself end the current paid period or revoke current membership rights.

#### B. Rescission keeps the same membership relationship

Before effective termination:

`do not renew → renew unchanged`

updates the current future instruction.

It does not create a second membership, new paid period, new entitlement provenance or immediate payment.

Historical cancellation and rescission events remain auditable.

#### C. Rescission is prospective

A later keep-membership instruction cannot retroactively make an earlier unauthorized renewal charge valid.

If cancellation had already withdrawn renewal authority and a provider nevertheless collected money, that collection remains subject to reversal/refund/governed remedy under existing CER doctrine.

#### D. Termination is the hard boundary

Before actual termination:

`undo cancellation = same live membership`

After actual termination:

`continue membership = new re-subscription journey`

Candidate 4 subsequently confirmed the post-termination case was already covered and required no new PT or upstream delta.

#### E. Membership intent and payment authority remain separate

Restoring future renewal intent does not automatically restore a separately revoked, expired or invalid reusable payment mandate.

Commerce may therefore have:

`renewal intent = yes`

while:

`valid reusable collection authority = no`

and must obtain valid payment authority before collection.

Candidate 8 subsequently pressure-tested payment-method/authorisation replacement and confirmed coverage under existing renewal/reconciliation PTs; no new PT was required.

#### F. Stale execution must revalidate current instruction

A queued cancellation/renewal-suppression/provider action cannot remain authority after rescission.

Before crossing an irreversible commercial boundary, execution must re-read the current authoritative future instruction.

#### G. Duplicate rescission is idempotent at the business level

Repeated equivalent keep-membership requests must converge on one current future instruction:

`renew unchanged`

They must not create duplicate renewals, duplicate memberships or additional payment authority.

### Store/JIT implication

The inspected Store subscription path exposes period-end cancellation and suppresses due renewals when `cancel_at_period_end` is true, but does not expose a corresponding governed user/admin resume/undo-cancellation transition.

NewYou reuse therefore requires an explicit cancellation-rescission business action, auditable instruction supersession, idempotent duplicate rescission, stale worker/provider revalidation and a clear distinction between pre-termination rescission and post-termination re-subscription.

No specific Resource, boolean, queue, worker or provider object is frozen here.

---

## CER-UPD-007 — Existing-member recurring price migration

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-017`.
- **Why upstream:** Current Product authority permits ordinary pricing, discounts and promotional pricing, but does not define how a later recurring membership price change applies to an existing active member. The answer determines future amounts owed, paid-period integrity, notice/consent obligations, grandfathering and effective renewal boundaries and therefore cannot be left to mutable provider/configuration state or incidental implementation.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. A later governed Product amendment must carry the rule into authority before downstream implementation may rely on it. Recurring promotion lifecycle was subsequently resolved by Candidate 6 / `CER-PT-018` / `CER-UPD-008`; continuity-derived Premium rights were subsequently resolved by Candidate 13 / `CER-PT-020` / `CER-UPD-012`.
- **Expert gate:** Before exact Product Law freezes notice/renewal mechanics, obtain South African consumer-protection/legal review of the intended monthly and annual agreement structures, including applicability of fixed-term renewal rules, required notice form/timing, termination rights and circumstances requiring express acceptance of renewed or increased-price terms.

### Accepted policy direction

> **Publishing or activating a new membership list price does not retrospectively alter an existing member's current paid period and does not by itself rewrite that member's recurring commercial contract. For an existing active membership, a higher price may take effect only from an eligible future not-yet-committed renewal after NewYou has durably established the exact target price/currency/effective boundary, given the participant clear advance notice of the new price and effective boundary, and satisfied all applicable contractual and legal notice/consent requirements. If those requirements have not been satisfied before that renewal becomes commercially committed, the higher price must not be charged for that occurrence. An already-committed renewal remains governed by its immutable price snapshot. Grandfathering or price locking may be offered explicitly, but it is a deliberate commercial term attached to the qualifying membership occurrence/offer and must not arise accidentally from historic list price or provider configuration. A later post-termination re-subscription does not inherit an old price solely because the same participant held it previously. Provider price/configuration state is execution evidence only and must not redefine NewYou contract truth.**

### Consequences

#### A. Current paid period is never repriced

A list-price change does not mutate an already-purchased paid period.

#### B. Public/list price is not existing-member contract authority

New price publication creates a new offer/price version.

Existing memberships remain governed by their current commercial contract until a valid future price migration becomes authoritative.

#### C. Future price migration must be explicit

The future commercial target must durably identify, at minimum:

- package/composition;
- cadence;
- price;
- currency;
- effective boundary;
- applicable offer/price version.

Representation remains JIT work.

#### D. Higher-price renewal fails closed if transition conditions are incomplete

If required notice/consent/legal conditions are not satisfied before the renewal commitment boundary, the higher amount must not be charged for that occurrence.

A later eligible renewal may apply the new price once the transition conditions are validly satisfied.

#### E. Already-committed renewal is immutable

A price change that becomes effective after a renewal is already commercially committed cannot rewrite that renewal.

Likewise, a stale old-price renewal cannot ignore an already-authoritative valid price migration if the migration won the ordering first.

#### F. Grandfathering is deliberate Product truth

A grandfathered/locked price may exist, but only when explicitly promised by the applicable membership occurrence/offer.

Historic list price alone does not create a lifetime personal pricing right.

By default, post-termination re-subscription is a new commercial occurrence and does not inherit an old price solely because the participant previously held it.

#### G. Provider mismatch is reconciliation evidence

If provider-charged amount differs from NewYou's authoritative renewal contract amount, Commerce must treat that as an explicit mismatch/reconciliation case.

Provider amount does not rewrite NewYou contract truth.

#### H. Cancellation before price increase

A participant may cancel before the higher-price renewal under ordinary cancellation doctrine.

If cancellation becomes effective before the new-price renewal, no higher-price renewal occurs.

#### I. Cadence transition must resolve one coherent future contract

Where cadence and price both change before the boundary, the future renewal must resolve one coherent target commercial contract rather than combining a fixed cadence with a later mutable price lookup.

### Store/JIT implication

Store's per-subscription `renewal_amount_minor` / `renewal_currency` and pending renewal amount/currency fields are useful reuse seams because they separate a subscription's renewal amount from the current public plan amount.

However, NewYou must not treat mutable `SubscriptionPlan.amount_minor` as authority for existing-member renewal pricing.

Downstream JIT must prove explicit price-version migration, effective-boundary eligibility, grandfathering provenance where applicable and immutable per-renewal priced/charged contract snapshots.

No specific PriceVersion Resource, migration table, worker or provider object is frozen here.

---

## CER-UPD-008 — Recurring promotional pricing lifecycle

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-018`.
- **Why upstream:** Current Product authority permits discounts and promotional pricing, but does not define recurring promotion duration/consumption, attachment to a commercial occurrence, upgrade/downgrade/cadence treatment, failed-renewal consumption, post-termination treatment or repeat eligibility. Those choices change money owed and the duration of the customer-facing commercial promise.
- **Boundary:** This accepted Pre-JIT direction does not itself amend Product Law. Base-price migration remains governed separately by accepted `CER-UPD-007`. Genuinely duplicated purchases/charges were subsequently resolved by Candidate 7 / `CER-PT-019` / `CER-UPD-009`; continuity-dependent rights were subsequently resolved by Candidate 13 / `CER-PT-020` / `CER-UPD-012`.

### Accepted policy direction

> **A recurring membership promotion is a commercial pricing term attached to a qualifying membership occurrence/offer and does not create a separate entitlement right. Every recurring promotion must define its pricing effect, qualifying scope, duration/consumption basis, commencement, post-promotion pricing rule and applicability across package/cadence changes. For cycle-limited promotions, one promotional cycle is consumed by one successfully established qualifying paid membership period, not by payment attempts, retries or duplicate execution; a renewal that never establishes a paid period does not consume a promotional cycle. Unused promotional cycles do not become standalone/banked credits and do not carry into a later post-termination membership occurrence unless Product explicitly promises otherwise. Re-subscription evaluates promotion eligibility under the current applicable offer and must neither automatically inherit remaining historical promotion value nor automatically reset a once-only promotion. An accepted promotion may not be retroactively altered by later mutation/deactivation of the public promotion definition. Upgrade, downgrade or cadence transition must resolve the exact target commercial contract—including base price/version, promotion applicability, remaining promotional scope and resulting charge—before commercial commitment. Duplicate user/provider execution must not multiply promotional benefit. Provider or mutable promotion configuration is execution/evaluation evidence only and cannot redefine the accepted NewYou commercial promise.**

> **For percentage promotions, the percentage applies to the membership's authoritative applicable base-price contract unless the offer explicitly promises a fixed promotional price. Any underlying base-price migration remains separately governed by `CER-UPD-007`; expiry of a promotion does not itself constitute a new unilateral base-price increase where the post-promotion pricing rule was clearly part of the accepted offer.**

### Consequences

- Promotion is Commerce pricing truth, not entitlement identity.
- Base-price contract/version and promotional adjustment remain distinct.
- Cycle-limited promotion scope is consumed by successfully established qualifying paid periods, not attempts or retries.
- Unused promotional scope is not a portable/banked credit by default.
- Re-subscription does not automatically inherit unused promotion value or reset once-only eligibility.
- Public promotion mutation/deactivation cannot retroactively rewrite an already-accepted recurring promotional promise.
- Package/cadence changes must resolve exact promotion applicability and duration basis before commitment.
- Promotion expiry and ordinary base-price migration remain separate commercial events.

### Store/JIT implication

Store's deterministic Pricing primitives—promotion provenance, windows, eligibility, exclusivity/combinability, ordering and canonical pricing outputs—are valuable reuse seams.

NewYou still requires recurring-specific hardening/adaptation for first-N-paid-period consumption, membership-occurrence attachment, remaining promotional scope, package/cadence applicability, post-termination treatment, repeat eligibility and immutable accepted recurring promotion rules.

No Promotion Domain, PromotionRedemption Resource or generic promotions engine is authorised here.

---

## CER-UPD-009 — Duplicate ordinary membership purchase and excess collection

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** `CER-PT-019`.
- **Why upstream:** Current authority and existing CER doctrine prevent competing membership truth and duplicate logical entitlement consequence, but do not explicitly define the customer-facing financial outcome when two distinct ordinary membership purchase/payment attempts both genuinely succeed while only one ordinary recurring membership relationship should be admitted. That determines whether duplicate money is retained, stacked, refunded or otherwise remedied.
- **Boundary:** This delta addresses conflicting ordinary recurring membership contracts for the same canonical grantee/commercial relationship. It does not prohibit separately governed gift, sponsored, complimentary or other legitimate entitlement sources; that broader overlap case was subsequently resolved by Candidate 15 / `CER-UPD-013`.

### Accepted policy direction

> **A canonical grantee may have at most one ordinary recurring membership commercial relationship admitted at a time; package, cadence and add-on changes to that relationship must use the governed membership-transition flows rather than creating a second overlapping ordinary membership. This exclusion is based on the intended grantee/commercial relationship, not merely purchaser, browser session, provider customer or payment reference, and does not prohibit separately governed gift, sponsored, complimentary or other legitimate entitlement sources. Concurrent or repeated purchase attempts must converge on exactly one admitted ordinary membership occurrence. If a non-admitted conflicting purchase nevertheless produces a successful financial collection, that payment remains truthful financial evidence but must not create a second membership, second paid period, duplicate recurring obligation or duplicate entitlement; NewYou must initiate full reversal/refund or, where automated reversal is unavailable, governed make-whole handling. The valid membership remains bound to the purchase that won NewYou's authoritative commercial-admission ordering, not whichever provider callback arrived first. Duplicate-payment remediation must be source-scoped and must not revoke or alter the valid membership. Provider transaction idempotency is necessary for retries of one payment but is not sufficient to enforce NewYou's one-ordinary-membership invariant across genuinely distinct purchase/payment attempts.**

### Consequences

- Ordinary overlapping self/recipient recurring membership purchases for the same canonical grantee are conflicting commercial intents, not separate valid memberships by default.
- Same purchaser does not imply duplicate if recipients/grantees differ.
- Two genuine provider successes remain two real financial facts even when only one may establish membership authority.
- The purchase that wins NewYou's Commerce-owned admission ordering remains the valid membership source.
- Callback arrival order, provider reference order and provider idempotency keys do not decide membership authority.
- The losing successful payment is duplicate/excess collection truth and must enter full reversal/refund or governed make-whole handling.
- Duplicate/excess collection must not be converted into an unrequested future prepaid period by default.
- Erroneously emitted duplicate entitlement must not justify retaining the duplicate payment.
- Remediation is source-scoped and must not revoke the valid membership.
- Crash/restart/retry must preserve a repeat-safe route to one valid membership plus one resolved or durable outstanding duplicate-payment remedy.

### Store/JIT implication

Store already has useful pre-admission checks for open membership subscriptions and pending membership orders, and it correctly distinguishes initial subscription creation from renewal reconciliation.

However, current reviewed evidence does not prove an atomic/concurrency-safe invariant preventing two distinct membership purchases from both passing those read-before-write guards.

NewYou reuse therefore requires proof/hardening for:

- concurrency-safe ordinary membership admission/exclusion;
- two-tab/two-transaction races;
- two successful distinct charges;
- exactly one membership consequence;
- duplicate-payment reversal/refund/remedy convergence;
- prevention of duplicate recurring provider obligations.

No specific database uniqueness shape, lock, saga, worker or queue topology is frozen here.

---

## CER-UPD-010 — Ordinary membership add-on recurring lifecycle

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** Second-pass Candidate 11 / refinement of `CER-PT-011`.
- **Why upstream:** Product Law defines Basic as the base recurring subscription, add-ons as recurring entitlement components and Premium as Basic plus named add-ons, but does not yet define add-on commencement, cadence, renewal alignment, cancellation timing, dependency on Basic or independently billed behavior.
- **Boundary:** Gift/sponsor overlap was subsequently resolved by Candidate 12 / `CER-UPD-011`; broader overlapping entitlement sources were subsequently resolved by Candidate 15 / `CER-UPD-013`; exact provider proration/co-billing mechanics remain `OQ-004`.

### Accepted policy direction

> **An ordinary membership add-on is a recurring commercial component of the existing Basic membership relationship, not a second ordinary membership contract. Basic remains the prerequisite base subscription and the authoritative membership composition is Basic plus zero or more active add-on components. Unless an offer explicitly defines a separately billed add-on, an add-on inherits the base membership's billing cadence and renewal boundary. Adding an add-on to an active membership is a composition upgrade: it may become effective during the current paid period only after any required incremental/prorated commercial adjustment becomes authoritative, and failed or unresolved adjustment must leave the existing membership unchanged. Thereafter the add-on renews as part of the same membership composition. Removing an add-on is a composition downgrade and ordinarily takes effect at the next not-yet-committed membership renewal boundary, preserving already-paid add-on access through the current paid period and creating no ordinary partial-period refund. Removing one add-on does not cancel Basic or unrelated components. Cancelling the Basic membership schedules the ordinary membership composition, including dependent add-ons, to end at the governing paid-period boundary; a dependent ordinary add-on must not outlive the Basic membership source it augments. Entitlement consequences remain source/provenance-aware, so ending a membership/add-on commercial source must not remove an equivalent right that remains valid through another authoritative source. Premium remains a named commercial bundle over Basic plus governed add-on components, and transitions to/from Premium apply source→target component deltas without artificial revoke/regrant of unchanged rights or duplicate billing obligations. Any independently billed add-on with a cadence or paid period different from Basic requires an explicit Product offer defining its independent renewal, cancellation, failure and dependency semantics rather than arising by implementation accident.**

---

## CER-UPD-011 — Gift/sponsored membership overlap with existing membership

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial decision.
- **Origin:** Second-pass Candidate 12 / refinement of `CER-PT-012`.
- **Why upstream:** Existing Product/Domain Law governs purchaser/recipient separation, code redemption, sponsor privacy and source-specific entitlement ownership, but does not define how fixed/prepaid gift or sponsored membership value is consumed when equivalent or stronger coverage is already active, whether self-billing pauses, when gift coverage begins, or how personal billing may resume. These are customer-money and paid-duration semantics.
- **Boundary:** Candidate 15 generalises multiple legitimate overlapping entitlement sources. Exact provider pause/resume/defer mechanics remain `OQ-004`.

### Accepted policy direction

> **Gift and sponsored membership access remain distinct commercial/entitlement sources and do not merge into or overwrite a recipient's existing membership provenance. Before an irrevocable redemption is consumed, NewYou must evaluate the canonical grantee's relevant active or already-committed membership coverage and make any material overlap outcome clear to the recipient. For ordinary fixed/prepaid duration-based membership gifts or sponsorships, equivalent already-paid coverage must not cause the incoming value to be silently consumed concurrently by default. The incoming source instead begins at the next eligible not-yet-committed boundary after already-paid equivalent coverage, unless the governed offer explicitly defines a fixed calendar window or an immediate-start rule. For periods fully funded by the gift/sponsor source, NewYou must not also collect an overlapping ordinary self-paid renewal for the same covered membership composition. A fixed-duration gift may permit self-paid renewal to resume after gift coverage only where that resulting schedule is clearly disclosed and accepted and payment authority remains valid. Open-ended or uncertain-duration sponsorship must not automatically restart personal billing when sponsorship ends unless the participant explicitly opted into such fallback. Sponsor termination affects future funding only and does not revoke an already-funded recipient period. Applying a gift/sponsorship does not rewrite historical paid periods or silently rescind an existing membership cancellation. Different or narrower target compositions must be disclosed rather than silently upgrading or downgrading the recipient. Fixed-calendar sponsored offers may consume during overlapping coverage only when that bounded-window behavior is part of the accepted offer. Entitlement provenance remains source-specific throughout, and termination of one source must not revoke access independently sustained by another valid source.**

---

## CER-UPD-012 — Premium reassessment continuity, maturity and nonaccumulation

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/benefit-eligibility decision.
- **Origin:** Second-pass Candidate 13 / `CER-PT-020`.
- **Why upstream:** `DEC-035` defines the annual Premium reassessment benefit at a high level but does not define continuity across cadence/source changes, failed-payment grace, genuine gaps, downgrade/re-upgrade, overlapping Premium sources, annual-renewal interpretation, nonaccumulation mechanics or expiry when Premium ends but Basic continues.
- **Boundary:** This delta defines Product eligibility semantics only. Exact Commerce evidence/provenance representation and Entitlements issuance remain downstream JIT. Provider mechanics remain evidence inputs only.

### Accepted policy direction

> **The Premium annual reassessment benefit is earned from uninterrupted qualifying Premium coverage of the canonical grantee, not from payment-attempt count, payment method, billing cadence or funding-source identity. The first reassessment entitlement becomes available after twelve calendar months of uninterrupted qualifying Premium coverage; for an annual Premium membership, an authoritatively paid annual renewal at the first anniversary is the ordinary annual-billing expression of the same maturity rule and is not an additional or accelerating trigger. Initial annual purchase and a switch into annual billing do not themselves constitute annual renewal for this purpose. Monthly↔annual cadence changes, price or promotion changes, payment-method replacement and seamless transitions between qualifying self-paid, gift or sponsored Premium sources preserve continuity when there is no uncovered Premium interval. Overlapping qualifying sources count elapsed time once and do not accelerate eligibility. A source contributes to continuity only where its governed offer constitutes qualifying Premium membership coverage; partial Premium-like grants do not qualify by accidental entitlement equivalence. During unresolved failed-payment grace, continuity and any maturity dependent upon that boundary remain provisional until Commerce establishes the relevant paid Premium period; successful reconciliation covering the boundary preserves continuity, while an ultimately unpaid uncovered period breaks continuity at the prior paid-period end. Downgrade to Basic, termination of qualifying Premium or any genuine uncovered Premium interval breaks continuity, and a later Premium upgrade begins a new continuity interval. An unused Premium reassessment entitlement expires when qualifying Premium coverage ends, even where the broader Basic membership relationship continues. At each successive twelve-month qualifying anniversary no more than one unused reassessment entitlement may exist; where one is already unused, no additional or catch-up entitlement is banked, and after later consumption the next entitlement becomes available only at the next future qualifying anniversary.**

### Consequences

- Continuity is measured in qualifying Premium coverage time, not successful charge count.
- Cadence, price, promotion or payment-method changes do not reset continuity by themselves.
- Seamless self-paid↔gift↔sponsored Premium source hand-offs preserve continuity where each source is qualifying Premium.
- Overlapping Premium sources do not double-count time.
- Initial annual purchase and cadence switch into annual are not annual-renewal maturity triggers.
- Failed-payment grace is provisional until Commerce establishes whether the new Premium period actually existed.
- Genuine Premium coverage gaps and Premium→Basic downgrade reset the continuity interval.
- Later re-upgrade begins a new qualifying interval.
- Unused reassessment entitlement expires when qualifying Premium ends, even if Basic continues.
- Nonaccumulation means at most one unused entitlement exists; missed anniversaries are not banked or caught up later.
- After late consumption of an existing entitlement, the next benefit waits until the next future qualifying anniversary.
- A grant only contributes to the clock if Product explicitly classifies it as qualifying Premium membership coverage.

### Store/JIT implication

Store should provide generic, durable commercial-period and provenance evidence only.

NewYou-specific Premium-tenure accumulation and reassessment benefit policy should remain outside the reusable Store package.

No generic Store feature should encode `12 Premium months → reassessment`.

---

## CER-UPD-013 — Multi-source entitlement overlap and grant commercial effect

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Classification:** Upstream Product/commercial/benefit-effect decision.
- **Origin:** Second-pass Candidate 15 / refinement of `CER-PT-011`, `CER-PT-012`, and `CER-PT-020`.
- **Why upstream:** Domain Law already permits multiple source-specific entitlements and source-scoped consumption/revocation, but Product Law does not yet fully distinguish access-overlay grants from qualifying membership-coverage grants or define whether overlapping legitimate sources multiply standard recurring/limited benefits. Those choices affect billing, qualification, paid value and benefit quantity.
- **Boundary:** This delta does not create a global source priority, generic credit wallet, new Domain or new provider gate. Exact source-selection/consumption implementation remains JIT.

### Accepted policy direction

> **Multiple legitimate entitlement sources for the same canonical grantee may coexist and retain independent identity, scope, validity, provenance, revocation and consumption history. Effective non-consumable access is the union of currently valid qualifying sources; expiry, revocation, refund, dispute or termination of one source must not remove access independently sustained by another valid source. Effective access composition does not itself rewrite the participant's authoritative Commerce membership contract or create a synthetic membership tier. Every complimentary, sponsored, gift, lifetime or other governed grant must derive its commercial and benefit effect from its explicit offer/authority: an access-overlay grant affects only its stated scopes and does not alter membership billing or membership-tenure qualification unless explicitly authorised; a qualifying membership-coverage grant may fund/substitute the covered membership composition for its governed interval. Where qualifying membership-coverage grant value makes a future ordinary self-paid collection fully redundant for the same composition and interval, NewYou must suppress that overlapping collection at the next not-yet-committed boundary unless a separate explicit commercial basis authorises it; already-paid periods remain unchanged. Partial grants suppress or replace only the commercial components they explicitly cover and do not cancel unrelated base membership obligations. Overlapping sources do not by themselves multiply recurring limited benefits, credits, continuity clocks or nonaccumulating entitlements. Product-defined limits such as the ordinary monthly Premium review and annual reassessment remain participant/benefit limits across equivalent overlapping sources. Additional consumable units arise only where an explicit governed offer/grant promises additive value. Consumption must apply exactly once against an authoritative eligible benefit occurrence/source and preserve auditable provenance.**

### Consequences

- Multiple valid sources may coexist without merge or global winner.
- Boolean/scoped access uses union semantics across valid sources.
- Effective access does not become a synthetic commercial tier.
- Access-overlay grants affect only their explicit scopes.
- Membership-coverage grants may substitute the covered commercial composition/interval.
- Redundant future self-paid collection is suppressed only where the grant explicitly covers that membership composition/interval.
- Partial grants alter only the covered component.
- Already-paid historical periods remain unchanged.
- Overlap alone does not multiply standard monthly reviews, annual reassessments, continuity clocks or limited credits.
- Explicit additive offers/grants may create additional units.
- Consumption applies once to one authoritative eligible occurrence/source with preserved provenance.
- No global source precedence such as lifetime > sponsored > gift > paid is authorised.

### Store/JIT implication

Store's source-aware grant identity and union-style effective access are useful reusable primitives.

Store reuse must be broadened beyond subscription-only source taxonomy and must support generic source-specific grants/limited entitlements without embedding NewYou-specific Premium/review policy.

NewYou Product authority decides whether a grant is:
- access overlay;
- qualifying membership coverage;
- additive limited benefit;
- non-additive ordinary benefit.

No new Domain is authorised.

---

# 12A. Accepted pressure-test evidence — continuation

The detailed PT evidence below continues the earlier pressure-test material after the accepted-delta register. This heading is navigational only and creates no new authority layer.

## CER-PT-005 — Failed renewal + 72-hour grace + cancellation + late successful retry

### Scenario

`renewal fails → 72-hour grace begins → participant cancels during grace → previously scheduled/already-in-flight renewal succeeds later`

### Pressure-test finding

This scenario exposed a genuine Product/commercial-right gap rather than a provider or implementation detail.

Current authority defines both:

- cancellation at the end of the paid period;
- 72-hour failed-payment grace with provider-safe retries;

but does not define precedence when cancellation happens after the successfully paid period has ended and before an unresolved renewal has been authoritatively established as paid.

### Options considered

#### Option A — Grace ignores cancellation until retries finish

Rejected.

This could allow a participant to cancel and still be intentionally charged for a new period because retry machinery remained active.

#### Option B — Stop future retries, but allow an already-started retry to renew the membership

Rejected as the preferred NewYou policy.

It makes contract outcome depend on an invisible execution race and can result in an additional paid period after the participant has explicitly requested cancellation.

#### Option C — Cancellation during grace withdraws continuation authority

**ACCEPTED / RECOMMENDED UPSTREAM PRODUCT DIRECTION.**

Cancellation becomes immediately effective during grace because the preceding paid period has already ended.

An already authoritatively verified-paid renewal remains a valid new paid period; an unresolved or merely provider-observed success does not automatically outrank the later accepted cancellation.

### NewYou verdict

**BLOCKED / STOP — PRODUCT AUTHORITY GAP**

The missing rule belongs upstream in Product/commercial authority.

It must not be invented inside:

- Paystack integration;
- Architecture mechanism;
- Domain implementation;
- JIT dossier;
- Store reuse adaptation.

### Working result

`CER-UPD-001` accepted for later governed Product amendment.

No `CER-WD` is created to bypass the upstream gap.

### Store Blueprint verdict

**BLOCKED FOR REUSE CERTIFICATION / ADAPTATION REQUIRED**

At the inspected Store subscription-hardening baseline:

- `past_due` subscriptions may set `cancel_at_period_end`;
- this suppresses future due-query retries;
- an already-running renewal may still proceed to paid-renewal reconciliation;
- `past_due → active` period extension remains possible.

Store therefore embeds a policy broadly equivalent to Option B.

That mechanism cannot be reused as-is if NewYou adopts the accepted Option C direction.

### Store hardening implied by the accepted direction

Future adaptation will need to prove:

- cancellation during grace suppresses future renewal authority;
- in-flight renewal work revalidates current contract authority;
- late provider success does not silently reactivate the membership;
- any late collection enters reversal/refund/reconciliation handling;
- entitlement/grace access ends consistently with the accepted commercial transition;
- cancellation/renewal races are safe under concurrency and restart.

### Carry-forward principles

**Grace is not permission for retry machinery to outrank a later commercial instruction.**

**Cancellation, payment collection and entitlement consequences are separate durable truths; queue timing must not decide the customer's contract.**

**A provider collection can be financially real without being authorised to recreate a cancelled recurring contract.**

---

## CER-PT-006 — Retry exhaustion / suspension / late provider success after suspension

### Status

- **NewYou semantic verdict:** PASS
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Upstream delta:** NONE
- **Related exception:** `CER-UPD-001` applies where a later cancellation has already withdrawn unresolved renewal authority.
- **Provider gate:** OQ-004 remains open for exact Paystack mechanics.

### Scenario

`renewal due → failed attempts → 72-hour grace → retries exhausted → membership suspended → late verified success for the same renewal occurrence`

The late success may arise because:

- an already-authorised provider mutation completed later than expected;
- success evidence was delayed;
- reconciliation only later established the true provider outcome.

This must be distinguished from a brand-new collection initiated after suspension.

### Core semantic finding

Current NewYou authority is sufficient.

`DEC-043` requires:

`failed payment → 72-hour grace → provider-safe retries → suspension after final failure`

The Domain Map separately models:

`active → grace → suspended → ended`

and requires provider ambiguity to be reconciled rather than guessed.

Therefore:

> **Suspension is not cancellation, contract erasure or proof that later verified payment evidence must be ignored.**

### Meaning of "final failure"

The safe interpretation is:

> **The governed automatic retry lifecycle has reached its end based on the authoritative evidence then available, so access is suspended and NewYou must stop blindly initiating further retries under that dunning cycle.**

It does **not** mean that no later evidence may ever prove the already-authorised renewal succeeded.

### Required invariant

If later canonical evidence proves that the **same still-authorised renewal occurrence** was successfully paid:

`late verified success → Commerce reconciliation → suspended membership restored to active → Entitlements restored`

provided no separate commercial event has withdrawn continuation authority.

### Interaction with CER-UPD-001

If cancellation was durably accepted while the renewal was still unresolved:

`cancellation → renewal authority withdrawn`

A later provider success is still real money movement, but it must not reactivate the membership.

It must instead enter reversal/refund or governed commercial-remedy handling.

Therefore:

> **Late verified success may repair suspension only while current Commerce authority still permits that renewal.**

### New collection after suspension

Retry exhaustion ends the automatic dunning cycle.

It must not silently become permission for indefinite background charging.

A new post-suspension collection attempt requires a fresh governed recovery trigger or provider-safe recovery path. Exact Paystack mechanics remain under OQ-004.

### Entitlements consequence

When a suspended membership is legitimately restored after late verified payment:

- Commerce establishes the renewal as paid;
- the membership contract becomes active again;
- Entitlements restores exactly the governed membership/add-on rights;
- the consequence must converge repeat-safely.

PT-001 still applies: Commerce success must not become a silent entitlement-restoration orphan.

### Late-success renewal-period anchor clarification

Where canonical evidence later proves success for the **same renewal occurrence**, that success establishes the renewal period that was already scheduled for that occurrence. It does not create a fresh full paid term beginning at the later webhook, verification or reconciliation timestamp.

For example:

`renewal due 1 Sep for 1 Sep → 1 Oct`
`→ grace / suspension`
`→ same occurrence authoritatively reconciled paid on 6 Sep`

remains:

`paid renewal period = 1 Sep → 1 Oct`
`next ordinary renewal boundary = 1 Oct`

not:

`6 Sep → 6 Oct`.

This follows the stable renewal-occurrence/billing-period identity in `CER-PT-004` and the Product rule that recurring membership is monthly/annual against governed paid billing periods. Reconciliation timing is evidence timing, not a new subscription-period commencement event.

This clarification is specific to a recurring renewal occurrence. It does not alter `CER-UPD-004`, where an ordinary on-demand **initial manual-EFT** membership period begins at authoritative verification/lawful activation.

If NewYou or a provider wrongly withheld service after payment was already valid, a separate governed remedy/make-whole question may arise. Such remedy does not shift the recurring renewal boundary by default.

### Store Blueprint finding

At the inspected Store subscription-hardening baseline, Store does not model `suspended`.

Its subscription states are:

`pending / active / past_due / canceled / expired`

At grace expiry Store:

- transitions the subscription to `expired`;
- sets an ended condition;
- revokes subscription entitlements;
- clears further renewal timing;
- sends an access-ended communication.

Its state machine permits:

`past_due → active`

and:

`active → active`

through renewal period extension, but does not permit:

`expired → active`.

This means a late paid renewal can become unreconcilable after Store has already expired the subscription.

That is independent of the earlier PT-003 defect where `PaymentIntent.failed` can block a later success.

### Store reuse conclusion

Do not reuse:

`grace expiry → expired terminal contract`

as NewYou semantics.

Potentially reusable mechanisms remain:

- deterministic renewal identity;
- retry accounting;
- grace calculation;
- entitlement revoke/restore mechanisms;
- reconciliation worker shape.

But NewYou requires the commercial contract/access model to preserve:

`grace expiry → suspended`

with later recovery possible when the same still-authorised renewal is authoritatively proven paid.

### Recommendation classification

- **NewYou semantic rule:** already required by current authority.
- **Implementation direction:** JIT implementation recommendation.
- **Store conclusion:** reuse/hardening recommendation.
- **New Product policy:** not required for the core PT-006 invariant.

### Carry-forward principles

**Suspension is not cancellation and is not contract erasure.**

**Retry exhaustion ends automatic retry authority; it does not authorise NewYou to ignore later verified evidence from an already-authorised renewal.**

**Late payment may restore a suspended contract only if current Commerce authority still permits that renewal.**

---

## CER-PT-007 — Immediate upgrade + proration + concurrent renewal/change

### Status

- **NewYou semantic verdict:** PASS — PROVIDER VALIDATION STILL REQUIRED
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Upstream delta:** None at present
- **Conditional upstream seam:** exact monetary proration formula/basis if NewYou must calculate proration itself
- **Provider gate:** OQ-004 remains open and blocks final Paystack implementation choice.

### Scenario

An existing recurring member requests an upgrade while the current renewal may be due, already claimed, already priced, already dispatched to the provider, or awaiting reconciliation.

Representative race:

`renewal due → Basic renewal begins → participant requests Basic → Premium → one or both money movements may be in flight`

The test asks which commercial contract is authoritative, which amount was legitimately priced, when upgraded access becomes valid, and how stale concurrent work is prevented from applying the wrong contract.

### Product contract

Current Product authority is clear at the semantic level:

- upgrades are immediate with provider-supported proration;
- downgrades take effect at renewal;
- historical records remain accessible.

Therefore upgrade and downgrade are not the same lifecycle operation.

`upgrade ≠ queued future configuration`

for NewYou Product semantics.

### Meaning of immediate upgrade

"Immediate" does **not** mean optimistic access before money truth.

The safe interpretation is:

`upgrade requested → required commercial adjustment established → required prorated collection verified → Commerce upgrade authoritative → Entitlements change immediately`

If the provider requires authentication/challenge or the outcome is ambiguous, the upgrade remains unresolved until Commerce can reconcile authoritative payment evidence.

### Normal mid-period upgrade

For a mid-period upgrade, Commerce must reason from:

- the current successfully paid contract;
- the target contract/price;
- the remaining governed billing-period basis;
- the effective upgrade time;
- any other Product-authorised monetary rules.

The upgrade should charge only the governed incremental amount for the remaining period rather than silently charge a second full overlapping period.

After verified adjustment success:

`Commerce = upgraded contract now → Entitlements = upgraded/add-on rights now → next renewal = target recurring contract`

Premium/add-on access must still reuse the existing Entitlements mechanism rather than inventing a second access-authority path.

### Renewal/upgrade ordering

Economically conflicting mutations of the same recurring commercial contract require one authoritative ordering.

#### Case A — upgrade becomes authoritative before renewal collection is committed

The renewal path must re-read current Commerce truth and must not blindly charge a stale lower-tier contract.

At an exact period boundary, the correct result may be a target-tier renewal rather than an old-tier renewal plus a meaningless zero-duration proration.

#### Case B — old-tier renewal was already authoritatively committed first

The renewal must reconcile as the contract that was actually priced/charged.

The later upgrade then calculates an adjustment from that newly paid contract to the target contract for the remainder of the new period.

#### Case C — neither intent has yet won

Renewal and upgrade cannot independently snapshot stale state and later both commit incompatible commercial effects.

One authoritative Commerce ordering must win; the losing/stale operation must re-read and, where necessary, recompute before irreversible effect.

### Stale-pricing invariant

A prorated adjustment is only valid against the commercial basis it was calculated from.

Conceptually it must be bound to:

- source contract/price version;
- target contract/price version;
- billing-period basis;
- effective timing;
- logical collection identity.

If that basis changes before irreversible collection, the adjustment must be rejected, revalidated or recomputed.

This is an invariant, not a Pre-JIT mandate for a particular Resource, lock or version column.

### Retry/idempotency

PT-003 and PT-004 apply unchanged:

`timeout ≠ definitely unpaid`

and:

`upgrade-payment retry ≠ new upgrade`

Retries of the same adjustment must preserve one logical collection identity and must not multiply charges or entitlement changes.

### Commerce → Entitlements convergence

PT-001 also applies unchanged.

A verified paid upgrade cannot become a permanent state where Commerce says the member is upgraded but Entitlements never converges because a worker crashed or exhausted retries.

### Provider evidence — verified 2026-09-09

Primary Paystack documentation currently shows:

1. The public Subscriptions API exposes create/fetch/enable/disable and subscription-card-management operations, but does not document a per-subscription immediate plan-switch/proration endpoint.
2. Paystack's documented plan-update mechanism can update existing subscriptions, but the changes apply on the **next billing cycle**, so it is not by itself an implementation of NewYou's immediate individual upgrade promise.
3. The subscriptions guide states that failed subscription charges are **not retried** by Paystack, reinforcing the need to validate any NewYou grace/retry design rather than assuming provider-managed dunning.
4. Paystack documents charging reusable authorisations for a merchant-specified amount through `charge_authorization`, which is a plausible building block for merchant-managed adjustment collection if OQ-004 proves it safe and available for the launch contract/market.

Primary references:

- https://paystack.com/docs/payments/subscriptions/
- https://paystack.com/docs/api/subscription/
- https://paystack.com/docs/api/transaction/

These facts constrain implementation; they do not redefine NewYou Product semantics.

### Provider options

#### Option A — provider-native individual proration

Use only if OQ-004 proves Paystack exposes a safe, suitable facility matching NewYou's semantic contract.

Do not assume it from current public documentation.

#### Option B — NewYou-owned proration + provider adjustment collection

**Preferred fallback / likely direction if OQ-004 validates the mechanism.**

Conceptually:

`Commerce calculates governed adjustment → provider executes one provider-safe collection → Commerce reconciles → upgraded contract becomes authoritative → Entitlements converge`

This preserves NewYou as commercial authority and keeps the provider behind an adapter boundary.

#### Option C — queue all upgrades until renewal

Rejected as Product-incompatible.

That would silently turn upgrade semantics into downgrade semantics.

#### Option D — grant upgraded rights first, settle later

Rejected.

Verified-payment authority must remain intact.

### Conditional proration-formula seam

No `CER-UPD` is created yet.

If OQ-004 proves that Paystack provides an acceptable native proration contract, its exact provider behaviour can be validated against NewYou authority.

If NewYou must calculate proration itself, then before FP-009's final commercial contract is frozen we must decide whether current Product authority is sufficiently precise about customer-money rules such as:

- time basis;
- source and target price-version basis;
- rounding;
- tax treatment where applicable;
- exact boundary-time treatment.

If those rules materially determine customer rights/money and cannot be treated as a provider-defined validated contract, they may require a small upstream Product/commercial amendment.

Until that branch is selected, this remains a **conditional upstream seam** and has no `CER-UPD` identifier.

### Store Blueprint finding — Product mismatch

Store's current plan/variant change path is renewal-boundary oriented.

It stores pending target plan/variant and pending renewal amount/currency, then promotes those values during renewal.

That is a useful mechanism for:

`downgrade → effective next renewal`

but it does not implement:

`upgrade → immediate + prorated`

Therefore the Store abstraction must not be reused unchanged for both directions.

### Store Blueprint finding — stale-contract race

The more serious defect is reconciliation against mutable pending contract terms.

The inspected RenewalAttempt identity/snapshot carries the subscription, period and renewal key, while later paid-renewal reconciliation obtains the current Subscription and promotes current `pending_*` plan/price fields.

The shown payment-match guard proves the paid order belongs to the RenewalAttempt; it does not prove the paid amount/order was created for the **currently pending** target plan/price.

A credible race is therefore:

`T1 Basic renewal checkout priced → T2 Basic payment succeeds → T3 Premium is queued → T4 old paid renewal reconciles → current pending Premium gets promoted`

That can establish a higher commercial contract without proof that the higher contract was actually priced and collected.

For NewYou, a paid renewal must reconcile the immutable commercial contract that was actually authorised and charged, not whatever mutable pending target happens to exist later.

### Concurrency implication

PT-007 is the first test where the absence of an explicit contract-version/transition concurrency mechanism becomes materially dangerous.

The invariant is:

> **A conflicting recurring-contract mutation must prove it is acting on the commercial version it priced and authorised against, or it must re-read/recompute before irreversible effect.**

Possible downstream mechanisms include optimistic versioning, constrained transition ownership, a short row-level serialization step or another durable compare-and-set/claim model.

Pre-JIT does not choose the mechanism.

### Store reuse conclusion

**ADAPTATION REQUIRED.**

Potentially reusable:

- renewal occurrence identity;
- renewal checkout/order/payment spine;
- pricing-resolution machinery;
- provider charge/reconciliation patterns;
- queued pending change concept for renewal-boundary downgrades.

Not reusable as-is:

- one queued-change mechanism for both upgrades and downgrades;
- renewal reconciliation against mutable current pending plan/price values;
- any model where the contract applied after payment can diverge from the contract snapshot actually priced and charged.

### Recommendation classification

- **NewYou semantic rule:** already required by current authority.
- **Provider mechanism:** OQ-004 validation required.
- **Concurrency/representation direction:** JIT implementation recommendation.
- **Store conclusion:** reuse/hardening recommendation.
- **Product amendment:** not required now; conditional only if merchant-managed proration exposes unresolved customer-money formula semantics.

### Carry-forward principles

**An upgrade is a commercial adjustment, not merely a future subscription configuration change.**

**Immediate upgrade means immediate after verified commercial success, never optimistic access before payment truth.**

**Renewal and upgrade may race technically, but they must have one authoritative commercial ordering.**

**A paid renewal must reconcile the commercial contract that was actually priced and charged, not whatever pending target happens to exist later.**

**If a recurring contract changes after an adjustment was priced, stale pricing authority must be revalidated or recomputed before irreversible collection.**

**Provider-native proration is optional; provider-safe execution is mandatory.**

---

## CER-PT-008 — Downgrade / cancel-at-period-end racing renewal

### Status

- **Original PT-008 boundary-ordering verdict:** PASS
- **Second-pass cancellation-rescission refinement:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Accepted upstream delta:** `CER-UPD-006` — rescission of pending period-end cancellation

### Core distinction

Cancellation and downgrade are different boundary instructions against the same future renewal occurrence.

Cancellation means:

`do not create the next paid recurring period`

Downgrade means:

`if the next recurring period is created, create it under the lower commercial contract`

They must therefore be ordered against renewal authority rather than treated as ordinary mutable flags.

### Cancellation precedence

If cancellation is durably accepted before the next renewal becomes authoritative as verified-paid:

`cancellation wins → no new paid period`

Any later provider money movement remains real payment evidence but must not silently create a new membership period; it enters reversal/refund or governed remedy handling.

If the renewal is already authoritatively verified-paid before cancellation:

`new paid period exists → cancellation applies at that period end`

This preserves DEC-039 and the already-accepted CER-UPD-001 direction.

### Downgrade precedence

For downgrade, the relevant boundary is the renewal commercial-commitment point.

If downgrade becomes authoritative before the renewal is commercially committed:

`renew under downgraded contract`

If downgrade arrives after the renewal has already crossed that commitment boundary:

`current renewal keeps the contract it was authorised against → downgrade applies to the next not-yet-committed renewal`

### Required invariant

> **Each renewal occurrence must resolve exactly one boundary instruction against one immutable commercial contract snapshot.**

The instruction may be:

- renew unchanged;
- renew downgraded;
- do not renew.

A queued worker or mutable pending field is not authority for which instruction won.

### Renewal snapshot integrity

A renewal must apply the commercial contract actually priced and charged for that renewal.

Pending future contract state created afterward must not rewrite historical payment meaning.

### Store Blueprint findings

At the inspected Store subscription-hardening baseline:

1. the due-query path suppresses subscriptions with `cancel_at_period_end == true`;
2. however, a renewal job queued before cancellation may still run because worker-side `ensure_subscription_due` checks timing/status but does not re-check `cancel_at_period_end`;
3. deeper renewal chargeability checks validate provider/payment-method conditions but do not restore the missing cancellation guard;
4. period-end cancellation currently records a flag, but the inspected path does not prove a durable boundary transition that closes the subscription when the paid period actually ends;
5. pending plan/price fields are useful for uncomplicated downgrade-at-renewal behaviour;
6. however, paid-renewal reconciliation can still consume mutable current `pending_*` state, allowing later downgrade state to alter the contract applied to an earlier payment.

### Store reuse conclusion

**REUSE AFTER HARDENING / ADAPTATION REQUIRED**

Reusable:

- deterministic renewal identity;
- due scheduling;
- order/payment reconciliation spine;
- pending target plan/price mechanics for downgrade.

Not reusable as-is:

- cancellation guard placement;
- period-end cancellation completion;
- mutable pending state as reconciliation authority.

### Second-pass Candidate 3 refinement — rescind pending period-end cancellation

Candidate 3 confirmed that this is not a new lifecycle class.

`CER-PT-008` already owns the authoritative ordering between future renewal instructions and the renewal boundary. Candidate 3 adds one missing Product/commercial promise inside that class: whether a participant may replace an accepted future `do not renew` instruction with `renew unchanged` before termination.

Accepted direction is recorded as `CER-UPD-006`.

#### Refined invariant

Before actual termination:

`period-end cancellation`
=
`future instruction: do not renew`

A later authenticated keep-membership instruction may supersede it:

`future instruction: renew unchanged`

provided the rescission becomes authoritative before the relevant termination/renewal boundary has irreversibly resolved.

Historical intent is preserved; current future intent governs.

#### Boundary distinction

If rescission wins first:

`live membership → normal renewal may proceed`

If termination wins first:

`membership ended`

A later continuation request is no longer rescission and belongs to Candidate 4 re-subscription semantics.

#### Late-charge rule

A later keep-membership instruction is prospective and cannot retroactively authorize a charge that occurred after cancellation had already withdrawn renewal authority.

#### Entitlements

Scheduling cancellation and rescinding it before termination should not revoke/regrant unchanged rights. Entitlements remain continuous because the membership never ended.

#### Payment-authority separation

Renewal intent and reusable payment authority are distinct. Rescission does not resurrect a separately revoked/invalid payment mandate.

#### Store refinement

The inspected Store path exposes period-end cancellation and renewal suppression but no governed undo/resume action in the reviewed user/admin capability surface. Store therefore remains **CHANGES REQUIRED / ADAPTATION REQUIRED** for this journey.

### Recommendation classification

- **First-pass boundary-ordering rule:** supported by current Product/Architecture authority.
- **Second-pass Product/commercial gap:** pending-cancellation rescission requires `CER-UPD-006`.
- **JIT requirement:** define the renewal commercial-commitment boundary, future-instruction supersession and concurrency mechanism.
- **Store conclusion:** hardening/adaptation required.

### Carry-forward principles

**Cancellation is a negative renewal instruction; downgrade is a replacement renewal instruction.**

**A queued renewal does not outrank a later authoritative boundary instruction.**

**A renewal must apply the contract it actually priced and charged.**

**Pending future contract state may not rewrite the meaning of an already-created payment.**

**Recurring-contract boundary races require one authoritative ordering, not last-write-wins mutation.**

**A period-end cancellation remains a future non-renewal instruction until actual termination.**

**Under accepted `CER-UPD-006`, valid pre-termination rescission restores `renew unchanged` on the same membership relationship.**

**Cancellation rescission is prospective and cannot retroactively authorize an already-unauthorized collection.**

**Renewal intent and reusable payment authority are separate truths.**

---


### Second-pass refinement — multiple future-facing instructions before one renewal boundary

Candidate 10 materially refines this PT without creating a new semantic class.

A membership has at most one authoritative future renewal outcome for each not-yet-committed boundary.

Multiple accepted future-facing instructions form an ordered sequence of superseding future-contract versions rather than competing independent authorities.

An instruction that changes only a defined contract dimension transforms the currently authoritative future target while preserving other still-valid dimensions. A broader explicit target selection supersedes every dimension it defines.

Period-end cancellation is special: it replaces the future renewal outcome with `do not renew` and makes prior pending target contracts historical rather than latent.

Under accepted `CER-UPD-006`, cancellation rescission creates `renew unchanged` from the still-live current contract; it does not automatically resurrect a pre-cancellation downgrade, cadence, price or promotion target.

Once a renewal becomes commercially committed, later instructions cannot rewrite it and instead target the next not-yet-committed boundary.

Concurrent, duplicate or stale instructions must resolve under one Commerce-owned ordering. Stale work must not overwrite a newer authoritative future contract.

Representation remains JIT work; this refinement does not require a dedicated FutureInstruction Resource.

## CER-PT-009 — Refund after entitlement issuance / partial benefit use

### Status

- **NewYou semantic verdict:** PASS
- **Store Blueprint verdict:** CHANGES REQUIRED / REUSE AFTER HARDENING
- **Upstream delta:** None
- **Existing upstream seam preserved:** `HSP-UPD-007`

### Product-defined refund boundaries

Current Product Law already provides explicit irreversible-benefit boundaries rather than a generic percentage-used model:

- assessment refundability ends after the first saved answer, except technical failure;
- Plan refundability ends after generation, subject to the existing generated-vs-delivered ambiguity already preserved as `HSP-UPD-007`;
- membership has no ordinary partial-period refund.

Assessment entitlement consumption is aligned to the first saved-answer boundary.

### Required concurrency invariant

Refund commitment and new irreversible benefit consumption must not both succeed against the same refundable commercial right.

Conceptually:

`refund commercially committed`
**XOR**
`new irreversible benefit consumption becomes authoritative`

If refund commitment wins first, affected rights must no longer remain freely consumable while provider refund execution is in flight.

If irreversible benefit consumption wins first, the ordinary refund boundary must be evaluated against that authoritative fact before external refund mutation.

The exact representation of any hold, restriction, pending state, contract-version check or lock remains JIT.

### Refund failure

A refund request or provider-processing attempt must not permanently destroy a still-valid right merely because refund execution was attempted.

If the refund ultimately fails and the original payment remains authoritative, temporary refund-related access restriction may be released and the entitlement may remain or become usable again if otherwise valid.

### Successful refund after historical consumption

A successful refund may remove future rights but must not rewrite historical consumption.

Examples:

- an assessment consumed by a first saved answer remains historically consumed even if an exceptional technical-failure refund is later granted;
- a generated or delivered benefit cannot be made historically “unused” by refunding the payment;
- money-refunded truth and benefit-already-consumed truth may coexist.

Therefore:

> **Refund may revoke future rights; it may not erase historical consumption.**

### Refund amount is not entitlement authority

Refund value does not determine entitlement scope through a generic percentage algorithm.

Entitlement consequences follow Product-defined commercial provenance and scope.

Examples include:

- full refund of an unused assessment → revoke the assessment right;
- shipping-only refund → no digital/product entitlement consequence;
- refund of a separately purchased component → consequence must follow the governed source/component relationship, not merely the numeric refund amount.

### Plan seam

The core Plan race is:

- refund commitment first → generation must not subsequently consume the refunded commercial right;
- generation authoritative first → ordinary refundability ends under current Product Law.

The already-known generated-but-not-delivered ambiguity remains `HSP-UPD-007`.

CER does not duplicate or silently resolve that upstream seam.

### Membership boundary

Do not introduce generic partial-use refund calculations for memberships.

Current Product Law already rejects ordinary partial-period membership refunds.

Corrective refunds for unauthorised/wrongful collections remain separate from ordinary partial-period refund policy.

### Store Blueprint findings

Store's refund engine contains a strong reusable financial core:

- locked financial refund bounds;
- durable refund records;
- idempotency-key fingerprinting;
- partial/full refund scopes;
- provider event evidence;
- replay-safe refund attempts;
- successful-refund accounting.

However, generic Store refund eligibility checks financial and order-level conditions rather than NewYou Product conditions such as:

- first assessment answer saved;
- Plan generation reached;
- ordinary membership partial-period refund prohibition;
- Product-specific exception authority.

Therefore Store refund eligibility must sit beneath NewYou Commerce policy and may not become NewYou authority.

### Store digital revocation policy

Store supports generic refund-driven revocation policies such as line-scoped, order-scoped and threshold-based revocation.

Those are reasonable generic store mechanisms but are **not reusable as NewYou business semantics**.

NewYou entitlement consequences must be derived from Product/Commerce provenance and applied through the Entitlements owner.

### Post-refund convergence

Store does retry downstream digital revocation after successful refund, but the inspected worker has finite retry attempts and no independently proven terminal reconciler for refund-succeeded / revocation-missing orphan repair.

PT-001 therefore still applies.

### Paystack adaptation

The inspected Store refund webhook event assumptions do not match current Paystack refund event naming/shape.

This is provider adaptation under OQ-004, not a NewYou Product issue.

### Store reuse conclusion

**CHANGES REQUIRED / REUSE AFTER HARDENING**

Strong reusable core:

- refund amount bounds;
- durable refund identity;
- idempotency;
- provider evidence;
- partial/full execution;
- replay-safe refund processing.

Do not reuse as NewYou authority:

- generic refund eligibility;
- generic amount/line/order-driven digital revocation policy.

Hardening still required:

- Product-specific admission before refund execution;
- cross-domain entitlement consequence through Entitlements;
- durable post-refund convergence after retry exhaustion;
- Paystack refund-event adaptation.

### Recommendation classification

- **NewYou semantic rule:** already supported by Product/Domain/Architecture authority.
- **Existing upstream seam:** preserve `HSP-UPD-007`.
- **Store conclusion:** reuse after hardening.
- **New CER Product amendment:** not required.

### Carry-forward principles

**Refundability is determined by Product-defined irreversible benefit boundaries, not generic percentage-used logic.**

**Refund commitment and new irreversible benefit consumption must not both succeed against the same commercial right.**

**A refund may revoke future rights; it may not erase historical consumption.**

**Money refunded and benefit already consumed can both be true at the same time.**

**Refund amount is not entitlement authority.**

**Generic Store refund mechanics may be reused; generic Store revocation policy may not replace NewYou Product and Entitlements law.**

---

## CER-PT-010 — Chargeback/dispute after benefit consumption

### Status

- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Accepted upstream delta:** `CER-UPD-002`
- **Store Blueprint verdict:** CHANGES REQUIRED / NOT REUSABLE FOR THIS SEMANTIC AS-IS

### Evidence baseline

- NewYou `main`: `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`
- Store `main`: `56f06d028ec38896f5a927f54dc7adfcb20034a3` (governance/workstream-registry movement; not treated as subscription/dispute implementation proof)
- Store `hardening/subscriptions`: `77a272c3887a7ab46e84a7fed02163d964e37b9b`
- No relevant open Store dispute/chargeback PR was found during PT-010 inspection.

### Core distinction

A refund is an authorised NewYou commercial action. A dispute/chargeback is an externally initiated contested-payment lifecycle that may arise after valid payment and benefit delivery.

Therefore:

> **A dispute is contested payment truth, not final reversal truth.**

Opening a dispute must not make historical payment, fulfilment or entitlement consumption false.

### Pending-dispute models considered

Three models were pressure-tested:

1. **No access consequence until final loss** — coherent but permits continued irreversible value delivery against a materially contested source.
2. **Reversible source-scoped hold while pending** — **recommended and accepted**. It prevents new/continuing value that materially depends on the disputed payment while preserving delivered history and unrelated rights.
3. **Immediate global revocation/termination** — rejected because dispute opening is not proof of invalid payment, fraud or contract termination.

### Source-scoped consequence

A dispute against one commercial occurrence must not automatically revoke unrelated purchases or later independently funded membership periods.

For recurring contracts, an unresolved dispute may block further automatic continuation only where the disputed payment remains material authority for the current recurring contract. Exact materiality/continuation mechanics remain JIT.

### Resolution in NewYou's favour

If NewYou wins the dispute:

- original payment remains authoritative;
- any temporary source-scoped hold is removed;
- rights resume without repurchase;
- no duplicate entitlement may be created.

### Final customer-favour reversal

If a dispute is accepted or finally lost and funds are reversed:

- historical successful payment remains recorded;
- later financial reversal is separately recorded;
- future rights whose sole source was that payment end or become non-active;
- historical consumption/fulfilment remains immutable;
- unrelated later valid commercial occurrences remain valid;
- no fraud finding, debt status, account-wide suspension or permanent ban follows automatically.

### Once-off permanent-access gap

Current Product Law gives once-off Plan purchasers permanent access to the delivered Plan, but did not previously define whether that access survives final reversal of the sole qualifying purchase.

The accepted `CER-UPD-002` direction clarifies that permanent means non-expiring while the qualifying purchase remains commercially valid. Final chargeback reversal may end future paid-origin platform access while preserving delivered history, provenance and required professional/safety records.

### Paystack validation

OQ-004 remains responsible for exact provider mechanics including dispute event/payload semantics, merchant response/evidence deadlines, partial dispute amounts, financial debit timing, resolution finality, replay and reconciliation after missed/reordered provider events.

### Store Blueprint findings

The inspected Store subscription-hardening baseline does not prove a dedicated dispute/chargeback business lifecycle comparable to its refund engine.

Reusable pieces include:

- durable provider-event evidence;
- provider event identity/dedupe;
- some financial-reversal/refund mechanisms that may be shared below the business lifecycle.

Missing/not proven:

- dispute lifecycle and finality;
- Paystack dispute integration;
- source-scoped entitlement hold/release;
- recurring-contract dispute semantics;
- final chargeback → Entitlements convergence.

Refund and dispute reversal may share lower-level financial mechanisms but must remain separate business truths.

### Store reuse conclusion

**CHANGES REQUIRED / NOT REUSABLE FOR THIS SEMANTIC AS-IS**

### Carry-forward principles

**A dispute is contested payment truth, not final reversal truth.**

**Opening a dispute does not erase historical payment, fulfilment or consumption.**

**Pending dispute consequences must be reversible and source-scoped.**

**A final chargeback may end future rights without rewriting consumed history.**

**A dispute against one commercial occurrence does not invalidate unrelated later valid occurrences.**

**Financial reversal does not itself prove fraud.**

**Refund and chargeback may share financial machinery but are not the same business lifecycle.**

**Provider dispute state is evidence; NewYou Commerce owns the commercial interpretation.**

---

## CER-PT-011 — Basic + add-on → Premium composition and contract identity

### Status

- **Original PT-011 composition invariant:** PASS
- **Second-pass add-on lifecycle refinement:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Second-pass multi-source commercial/benefit-effect refinement:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED — STRONG ENTITLEMENT REUSE CORE
- **Accepted later upstream deltas:** `CER-UPD-010`, `CER-UPD-013`
- **Historical note:** the original PT-011 PASS remains valid for bundle/component identity; the later deltas govern additional lifecycle/effect questions rather than reversing that invariant.

### Authority basis

Current Product Law already defines Basic membership as the base subscription, add-ons as recurring entitlement-granting components, and Premium as a named bundle of Basic plus add-ons. Current Domain Law keeps Commerce packaging/contract truth separate from Entitlements right identity, scope, provenance, validity and revocation. The Roadmap explicitly anticipates component entitlements.

The remaining problem is JIT representation and transition semantics, not missing Product Law.

### Core distinction

> **Bundle identity is not entitlement identity.**

Premium is commercial packaging over a defined composition of Basic plus governed add-ons. It must not become an opaque replacement entitlement that erases the identity and provenance of its component rights.

### Recommended commercial model

The preferred JIT direction is one authoritative current membership commercial composition per participant:

`Membership composition = Basic base + zero-or-more governed add-on components`

A named package such as Premium may define a target composition and commercial price, but must not create a second competing membership truth alongside the pre-existing Basic/add-on obligations. This recommendation does not freeze Resource, table, aggregate or provider-object design.

### Upgrade example

Source: `{Basic, A}`

Target Premium: `{Basic, A, B}`

After verified commercial adjustment:

- Basic remains continuous;
- A remains continuous;
- B is newly granted;
- obsolete independent billing obligations that were replaced by the Premium package must not continue;
- the target commercial composition becomes authoritative.

The transition applies the source→target delta rather than revoking and recreating every included right.

### Downgrade example

Source Premium: `{Basic, A, B}`

Target: `{Basic, A}`

At the governing renewal boundary:

- Basic continues;
- A continues;
- B ends;
- unchanged rights do not undergo artificial revoke/regrant cycles.

PT-008 continues to govern downgrade-vs-renewal ordering.

### Multiple entitlement sources

The same effective entitlement scope may legitimately have more than one authoritative source. If `A` is supplied by Premium and also by an independent lifetime grant, ending the Premium source must not remove effective access while the independent source remains valid.

> **Revoking one commercial source must not revoke an entitlement scope that remains valid through another authoritative source.**

Refund, chargeback, cancellation and package-transition consequences must follow provenance.

### Billing and entitlement deltas are related but distinct

At a membership transition, Commerce resolves source composition, target composition and the commercial adjustment; Entitlements applies the effective-right delta after authoritative commercial success. A named bundle may change pricing/package identity without forcing unchanged component rights to become new entitlement identities.

### Provider boundary

Provider subscription/charge object structure does not determine NewYou membership truth. Even if Paystack later requires one or several provider-side objects, NewYou should preserve one authoritative membership composition and map provider execution beneath it.

### Store Blueprint — strong reusable entitlement core

Store's `EntitlementGrant` model is strongly aligned with NewYou because grant identity includes user, kind, scope, source kind and source id. Its effective entitlement set can combine multiple active sources for the same capability, and source-specific revocation can remove one source without requiring global scope revocation. This is a strong reuse candidate.

### Store Blueprint — composition gap

Store's current `SubscriptionPlan` carries one `entitlement_kind` and one `entitlement_scope_key`, and the subscription entitlement issuer issues one grant from that plan/source. That is insufficient for a NewYou Premium package whose commercial meaning is Basic plus multiple add-on component rights.

Store's subscription creation is also currently line-oriented: each paid subscription line can create its own `Subscription` plus immutable `SubscriptionItem`. Used directly for NewYou Basic/add-on/Premium semantics, that naturally trends toward multiple independently renewing lifecycle objects. NewYou should not import that as membership authority without evidence that multiple independent contracts are actually required.

### SubscriptionItem interpretation

Store's existing `SubscriptionItem` is useful historical commercial snapshot evidence. It should not be assumed to already represent the authoritative current membership-component lifecycle merely because of its name. Current component authority therefore requires adaptation.

### Duplicate-membership protection

Store's `membership_key` guard is useful for preventing duplicate open membership subscriptions for the same membership-access scope. However, it does not by itself establish one coherent Basic + add-on + Premium composition. It is reusable protection, not the complete NewYou membership model.

### Store reuse conclusion

**CHANGES REQUIRED / ADAPTATION REQUIRED — STRONG ENTITLEMENT REUSE CORE**

Strongly reusable:

- source/provenance-aware entitlement grants;
- multiple sources for one effective scope;
- effective-set deduplication;
- source-scoped revocation;
- immutable commercial snapshots;
- duplicate-membership protection patterns.

Adaptation required:

- one authoritative recurring membership composition;
- multi-component entitlement issuance from that composition;
- Premium package mapping to Basic + add-ons;
- source→target composition transitions;
- retirement of obsolete replaced component billing obligations;
- continuity of unchanged component rights.

Do not reuse as NewYou semantics:

- one subscription line = one independent membership contract by default;
- one SubscriptionPlan = one entitlement as the Premium model;
- coarse `premium_access` as a substitute for component rights.

### Recommendation classification

- **Product/Domain authority:** sufficient.
- **Pre-JIT doctrine:** bundle identity ≠ entitlement identity; one authoritative membership composition.
- **JIT recommendation:** model source→target component deltas without freezing representation yet.
- **Store conclusion:** adapt subscription composition; retain the strong entitlement provenance core.
- **New CER Product amendment:** not required.

### Carry-forward principles

**Bundle identity is not entitlement identity.**

**Premium is commercial packaging over Basic plus governed add-on components.**

**One participant should have one authoritative current membership composition, even if provider execution uses multiple objects.**

**Bundle transitions apply commercial and entitlement deltas rather than destroying and reconstructing unchanged rights.**

**An unchanged component right must remain continuous through package changes.**

**Revoking one source must not remove a right still supported by another valid source.**

**A package change must not leave obsolete component billing obligations running alongside their replacement bundle.**

**Provider structure must not define NewYou membership truth.**

---

### Second-pass refinement — ordinary add-on purchase/cancellation while Basic remains active

Candidate 11 materially refines this PT without creating a new semantic class.

The authoritative membership composition is Basic plus zero-or-more governed add-on components. An ordinary add-on is a commercial component of the existing Basic membership relationship, not a second ordinary membership contract.

Unless an offer explicitly defines independent billing, an add-on inherits the base membership cadence and renewal boundary. Adding an add-on during an active paid period is a composition upgrade and may become effective only after any required incremental/prorated adjustment becomes authoritative. Failed or ambiguous adjustment leaves the existing membership composition unchanged.

Removing an add-on is a composition downgrade and ordinarily takes effect at the next not-yet-committed membership renewal boundary, preserving already-paid add-on access through the current paid period and creating no ordinary partial-period refund.

Cancelling Basic ends the ordinary dependent add-on composition at the same governing paid-period boundary. A dependent ordinary add-on does not outlive the Basic membership source it augments.

Entitlement consequences remain provenance-aware: ending one membership/add-on source does not revoke an equivalent right that remains valid through another authoritative source.

Premium remains a customer-facing bundle over Basic plus named add-on components; transitions apply source→target component deltas without artificial revoke/regrant of unchanged rights or duplicate billing obligations.

Independently billed add-ons with their own cadence/paid period remain possible only as an explicit Product exception with separately governed renewal, cancellation, failure and dependency semantics.

### Second-pass Candidate 14 refinement — composition transition safety

Candidate 14 further refines component composition transitions.

A source→target membership composition delta is one entitlement-set transition for that source, not a sequence whose correctness depends on whether grants happen before revokes or revokes before grants.

Unchanged component rights remain continuously valid through the transition.

Removed component rights cease no later than their governed effective boundary.

Newly added rights become authoritative only after the target transition is durably accepted.

### Second-pass Candidate 15 refinement — multi-source capability resolution

Candidate 15 generalises membership-component composition into multi-source entitlement resolution.

Equivalent effective access may be sustained by multiple independently valid sources without collapsing those sources into one commercial membership or merged grant.

Access composition is capability-specific. Boolean/scoped access resolves as the union of currently valid qualifying sources, while limited/consumable benefits follow Product-defined multiplicity rather than naive source-count addition.

Overlap alone never creates additional standard recurring benefits.

## CER-PT-012 — Gift/sponsored purchaser/recipient/participant separation

### Status

- **Original PT-012 semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Originating upstream delta:** `CER-UPD-003`
- **Accepted later overlap refinements:** `CER-UPD-011`, `CER-UPD-013`
- **Historical note:** `CER-UPD-003` remains the originating payer/grantee/redemption-control gap; later deltas extend overlap and multi-source commercial effect.

### Authority basis

Current Product authority already separates purchaser, recipient, participant and account holder, limits the purchaser to redemption status, makes redeemed access non-transferable and restricts sponsored bulk reporting to aggregate redemption visibility rather than participant health data. Current Domain Law already assigns gift/sponsored/complimentary/lifetime grants and access redemption codes to Entitlements while Commerce owns payer/payment/refund truth and Identity & Access owns canonical grantee identity.

Therefore the identity, privacy and Domain ownership model is already sound. The unresolved issue was narrower: who controls an already-redeemed benefit when payer and grantee differ, and what recurring debit authority may exist for a gifted membership.

### Base lifecycle

The accepted semantic shape is:

`purchaser pays → unredeemed allocation/redemption authority → recipient redeems → canonical grantee resolved → redemption consumed exactly once → grantee entitlement issued`

Payment for another person does not temporarily grant the purchaser the participant entitlement.

### Redemption boundary

Redemption is not a cosmetic status flag. It converts an unredeemed allocation into a source-bound, non-transferable grantee right. One redemption authority may create at most one authoritative grant. Duplicate technical requests may converge on the same result but may not allocate the same right twice or to two different grantees.

Recipient-routing information such as an email address is not permanent entitlement authority. The grant follows the canonical grantee identity resolved through Identity & Access.

### Refund/cancellation versus redemption

The race:

`refund/cancel unredeemed allocation ↔ recipient redemption`

requires one authoritative ordering.

- refund/cancellation first → allocation invalidated → later redemption fails closed;
- redemption first → recipient right becomes authoritative → ordinary purchaser change-of-mind cannot silently revoke it.

Later true financial reversal, dispute or chargeback is handled under the separate PT-009/PT-010 rules rather than pretending redemption never occurred.

### Post-redemption control models considered

**Payer retains full control forever** was rejected because it undermines the Product-law purchaser/recipient separation and would let a funder silently withdraw another person's redeemed right.

**Redemption completely cuts the payer out of Commerce** was rejected because the payer remains the party charged and may still have legitimate payment-correction, chargeback and settlement relationships.

**Split financial ownership from redeemed-benefit control** was accepted: the purchaser retains payment/settlement and authorised future sponsorship control; the recipient/participant controls participant use, protected data and ordinary participant-side post-redemption decisions.

### Refund authority versus settlement destination

The request authority, financial settlement destination and entitlement consequence are separate truths. A participant may hold the right to invoke a qualifying post-redemption refund while Commerce settles against the original purchase/payment source. That does not expose the participant's protected health/assessment/Plan/activity details to the payer.

### Sponsored access

Sponsors may receive Product-authorised aggregate redemption information, not participant surveillance. Already-redeemed sponsored grants follow their pre-disclosed validity/expiry terms. Sponsor changes normally affect future or unredeemed allocations unless an explicitly governed sponsored contract authorised earlier revocation.

A recipient must also be able to decline or stop using sponsored access without granting the sponsor visibility into protected participant information.

### Recurring gifted membership

Current authority did not define whether purchasing membership for another person creates indefinite recurring debit authority against the purchaser. The accepted direction is:

- ordinary gifted membership is fixed-duration/prepaid by default;
- it must not silently create recurring debit authority;
- recurring sponsorship is allowed only through separate explicit payer consent;
- the payer may stop future recurring billing;
- ordinary cancellation does not retroactively revoke the recipient's already-paid period.

### Store Blueprint finding

At the inspected subscription-hardening baseline, Store's ordinary subscription path binds the subscription user to the order user and later grants the entitlement to that subscription user. This effectively assumes:

`order purchaser → subscription holder → entitlement grantee`

That works for self-purchase but does not satisfy NewYou's locked purchaser/recipient separation for gifts or sponsorship.

Store's strong reusable pieces remain:

- Orders/Payments and payer-side reconciliation;
- durable payment/business idempotency;
- source/provenance-aware entitlement grants;
- source-scoped revocation/effective entitlement evaluation.

Not proven in the inspected path:

- a dedicated gift/sponsorship redemption lifecycle;
- purchaser ≠ grantee subscription flow;
- exactly-once redemption;
- bulk sponsor allocation lifecycle;
- recurring-sponsored-payer semantics.

### Store reuse conclusion

**CHANGES REQUIRED / ADAPTATION REQUIRED**

The Store payment and entitlement mechanisms remain valuable, but the purchaser→subscription-user→grantee assumption cannot be reused as NewYou gift/sponsorship semantics.

### Recommendation classification

- **Existing Product/Domain authority:** sufficient for role separation, privacy boundaries and ownership.
- **Upstream Product gap:** post-redemption commercial control and recurring sponsored-payer authority.
- **Accepted upstream delta:** `CER-UPD-003`.
- **JIT:** exact redemption representation, concurrency control, source model and sponsored-recurring execution.
- **Store:** adaptation required; no new NewYou Domain justified.

### Carry-forward principles

**Purchaser, recipient, participant and account holder remain distinct even when one human occupies several roles.**

**Payment for another person does not make the payer the entitlement holder or participant.**

**An unredeemed allocation is not yet the recipient's participant entitlement.**

**Redemption is a durable, exactly-once transfer boundary.**

**Recipient-routing data is not canonical grantee identity.**

**After redemption, funding does not imply participant-data visibility or ordinary unilateral access revocation.**

**Refund-request authority, financial settlement destination and entitlement consequence are separate truths.**

**Sponsored aggregate reporting must not become participant surveillance.**

**Pre-disclosed grant expiry is not the same as discretionary sponsor revocation.**

**Gifted membership must not silently create recurring payer authority.**

**Explicit recurring sponsorship separates payer billing control from recipient participation/access rights.**

**Unredeemed cancellation/refund and redemption require one authoritative ordering.**

**Store's purchaser→subscription user→grantee assumption is not reusable as NewYou gift/sponsorship semantics.**

---

### Second-pass refinement — gift/sponsor overlap with an already-active membership

Candidate 12 materially refines this PT without creating a new semantic class.

Gift and sponsored membership access remain distinct commercial/entitlement sources and do not overwrite or merge provenance with the recipient's existing membership source.

Before irrevocable redemption is consumed, NewYou must evaluate the canonical grantee's relevant active or already-committed coverage and make any material overlap outcome clear.

For ordinary fixed/prepaid duration-based membership gifts or sponsorships, equivalent already-paid coverage must not cause the incoming value to be silently consumed concurrently by default. The incoming source begins at the next eligible not-yet-committed boundary after already-paid equivalent coverage unless the governed offer explicitly defines a fixed-calendar window or an immediate-start rule.

Periods fully funded by the gift/sponsor source must not also trigger overlapping ordinary self-paid collection for the same covered membership composition.

A fixed-duration gift may permit self-paid renewal to resume after gift coverage only where that resulting schedule is clearly disclosed/accepted and payment authority remains valid.

Open-ended or uncertain-duration sponsorship must not automatically restart personal billing when sponsorship ends unless the participant explicitly opted into such fallback.

Sponsor termination affects future funding only and does not revoke an already-funded recipient period.

Applying gift/sponsorship does not rewrite historical paid periods or silently rescind an existing membership cancellation.

Different or narrower target compositions must be disclosed rather than silently upgrading or downgrading the recipient.

Fixed-calendar sponsored offers may consume during overlapping coverage only when that bounded-window behavior is part of the accepted offer.

Entitlement provenance remains source-specific throughout; termination of one source must not revoke access independently sustained by another valid source.

### Second-pass Candidate 15 refinement — general overlap beyond gift/sponsor

Candidate 15 generalises gift/sponsor overlap to all legitimate sources including self-paid, complimentary and scoped lifetime grants.

Source identity, scope, validity, revocation and historical provenance remain independent.

A source ending must not revoke another independently valid source.

Commercial billing consequences arise only when a governed grant is explicitly a membership-coverage source for the relevant composition/interval; an access-overlay grant does not silently change billing or commercial membership status.

## CER-PT-013 — Manual EFT verification / recurring-right boundaries

- **Status:** ACCEPTED
- **NewYou verdict:** **BLOCKED / STOP — PRODUCT AUTHORITY GAP**
- **Store verdict:** **ADAPTATION REQUIRED / REUSE GENERIC PAYMENT CORE**
- **Accepted upstream delta:** `CER-UPD-004`
- **NewYou evidence baseline:** `main` at `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`

### Why this test matters

`DEC-049` already settles the most dangerous manual-payment rule: manual EFT may be supported separately, creates no automatic renewal authority and grants access only after payment verification. The pressure test therefore did not treat EFT as a degraded card/provider path. It tested whether the existing rule remains coherent under delayed verification, duplicate deposits, wrong references, under/over-payment, cancellation, late matching and later migration to an authorised recurring method.

### Existing authority is sufficient for most EFT semantics

A manual EFT proves only the commercial payment it is authoritatively verified and matched against. It does not create authority to debit, assume or fabricate payment for a future membership period. A following period therefore requires a new verified payment unless the payer separately establishes an authorised recurring-payment arrangement.

> **Manual payment evidence is not commercial payment truth until Commerce authoritatively verifies and matches it.**

The bank movement is evidence. NewYou must still determine that the money corresponds to the intended payer/order or commercial obligation, amount, currency and applicable commercial terms before access follows. A screenshot or customer assertion that payment was sent is likewise not sufficient payment authority.

### Missing EFT is not a failed automatic renewal

`DEC-043` defines a 72-hour failed-payment grace/retry lifecycle, but `DEC-049` explicitly says manual EFT does not create automatic renewal. Therefore the absence of another manual EFT at the end of a paid period is not itself a failed automatic collection. NewYou must not manufacture provider retry semantics where no automatic debit authority existed.

A newly initiated EFT renewal may remain pending while bank evidence is unresolved, but that is a manual-payment reconciliation condition, not an automatic-provider retry lifecycle.

> **Absence of a new EFT is not a failed automatic renewal.**

### Verification is the access boundary

If money has reached a bank account but NewYou has not yet authoritatively verified and matched it, membership access does not begin merely because external cash movement exists. Commerce first establishes the payment application; Entitlements then receives the resulting grant consequence.

This preserves the existing owner split:

`bank evidence → Commerce verification/application → Entitlements consequence`

### Duplicate verification and retries

Finance double-review, request retry, reconciliation replay, worker restart or post-commit consequence retry must not multiply the purchased result.

> **One verified EFT application may create the purchased commercial/entitlement consequence only once.**

This reuses the business-idempotency doctrine already established by PT-001, PT-002 and PT-004.

### Wrong reference / unidentified deposit

A real deposit with insufficient matching information is not permission to guess a beneficiary or order. The durable financial evidence may exist while its commercial application remains unresolved. The correct behavior is fail-closed reconciliation/manual adjudication rather than optimistic entitlement.

> **Money received ≠ right identified.**

Exact matching workflow, Finance UX and reconciliation representation remain JIT/operating concerns.

### Underpayment

If the required amount is greater than the verified deposit, partial financial satisfaction must not silently become full commercial satisfaction. The purchase may remain pending, require an additional payment, enter an explicitly authorised commercial remedy or be returned according to later governed operating/accounting rules.

> **Underpayment must not silently create full entitlement.**

### Overpayment and duplicate deposits

A payment greater than the price, or two similar deposits, does not automatically create extra membership periods. Commerce must determine whether the money represents separate legitimate purchases, a duplicate/mistaken transfer, an explicitly supported prepayment arrangement or an amount requiring refund/remedy.

> **Overpayment and duplicate money do not automatically create additional entitlement.**

Monetary amount by itself is not entitlement authority.

### Late EFT against expired or changed commercial intent

Late money movement may remain financially real even after the relevant offer, price or pending purchase has changed or ceased to be fulfilable. Commerce must reconcile the evidence against the original commercial intent/price version rather than silently applying the funds to whichever offer happens to be current. If the original obligation can no longer be validly fulfilled, the funds enter governed refund/remedy handling.

> **Late money may be financially real while no longer authorised to activate the original commercial right.**

### Cancellation / abandonment before late verification

Where a pending manual purchase is authoritatively withdrawn before unresolved money is commercially committed, later bank matching must not surprise-reactivate the withdrawn purchase. It may establish a real financial movement requiring refund/remedy, but financial reality does not itself recreate withdrawn commercial authority. Exact pending-order cancellation mechanics remain JIT.

### Moving from EFT to recurring billing

Prior manual-payment history is not consent to future debits. A participant or payer moving to card/another recurring method must establish fresh explicit recurring-payment authority. This remains true when purchaser and participant differ under PT-012.

> **A new recurring payment method requires fresh explicit payer authority.**

### The Product gap — paid-period commencement under delayed verification

Current Product authority says access begins only after payment verification but does not say what date an ordinary membership period is measured from when a bank transfer was initiated or received earlier than verification. That choice determines how much purchased access the customer actually receives and is therefore Product/commercial-right semantics, not an implementation timestamp.

Three models were considered.

**Bank-transfer/receipt date** was rejected as the ordinary default because administrative verification delay could consume purchased days during which access was forbidden.

**Verification/activation date** is the recommended ordinary on-demand model: the paid period begins when the payment becomes authoritatively verified and membership can lawfully activate, preserving the full purchased duration.

**Explicit fixed/scheduled service period** remains valid where the offer itself was sold against a known calendar/cohort/event/service period. In that case the disclosed schedule may govern even when verification occurs later.

This gap is accepted as `CER-UPD-004`.

### Store Blueprint findings

At the inspected subscription-hardening baseline, Store's `PaymentIntent` is provider-oriented: it requires a provider and carries provider payment/session/customer/payment-method references through a submitted/requires-action/succeeded/failed style lifecycle. The persisted provider enum contains Stripe, PayFast, Paystack, Yoco and Peach Payments; no manual/EFT/bank source was found in the inspected path.

That does not justify mechanically adding `:eft` to an enum. It proves only that the inspected provider-oriented PaymentIntent path is not a reusable NewYou manual-EFT workflow as-is.

No dedicated manual bank-evidence ingestion, human verification/audit flow, unmatched EFT reconciliation or under/over/duplicate adjudication path was proven in the inspected subscription branch. The generic durable payment/business-idempotency spine remains valuable.

### Store reuse conclusion

**ADAPTATION REQUIRED / REUSE GENERIC PAYMENT CORE**

Strong reuse candidates include durable commercial/payment identity, apply-once business consequences and replay/idempotency mechanisms. NewYou-specific manual verification should enter through an adapted manual-payment ingress rather than by pretending EFT is a synchronous payment provider. Exact Resource/action/ledger/UI design remains JIT.

### Recommendation classification

- **Existing Product authority:** sufficient for verification-before-access and no implicit automatic renewal.
- **Upstream Product gap:** paid-period commencement where verification is delayed.
- **Accepted upstream delta:** `CER-UPD-004`.
- **JIT/operating:** matching, evidence capture, Finance workflow, under/over/duplicate handling representation, reconciliation and audit mechanics.
- **Store:** generic payment core reusable; provider-oriented intent path requires adaptation.
- **Domain:** no new NewYou Domain justified.

### Carry-forward principles

**Manual payment evidence is not commercial payment truth until authoritatively verified and matched.**

**Manual EFT creates no implicit future debit or automatic-renewal authority.**

**Absence of another EFT is not a failed automatic renewal.**

**One verified EFT application may create the purchased consequence only once.**

**Underpayment must not silently create full entitlement.**

**Overpayment and duplicate money do not automatically create additional entitlement.**

**Late money may be financially real while no longer authorised to activate the original commercial right.**

**Delayed administrative verification must not silently consume paid access duration.**

**A new recurring payment method requires fresh explicit payer authority.**

**Store's generic payment spine is reusable; its provider-oriented PaymentIntent is not a manual-EFT model as-is.**

---


## CER-PT-014 — Entitlement expiry/revocation racing in-flight Plan/review fulfilment

### Status

- **NewYou semantic verdict:** BLOCKED / STOP — EXISTING `HSP-UPD-001`
- **Store Blueprint verdict:** ADAPTATION REQUIRED — GENERIC GRANT MECHANICS ONLY
- **New CER upstream delta:** None
- **Existing upstream identity preserved:** `HSP-UPD-001`

### Authority relationship

The live Health / Safety / Plans upstream-delta register already owns the exact gap:

> a time-scoped membership Plan/review benefit expires after a Request was validly admitted but before fulfilment; does admitted work retain a bounded completion right?

That question remains open at Product Law + Entitlements, with Commerce involved where membership contract meaning changes.

CER therefore must not create a duplicate `CER-UPD`.

### Recommended bounded-completion direction

A time-scoped membership Plan/review benefit that is validly exercised and authoritatively bound to an exact Request before ordinary entitlement or membership expiry should retain a bounded right to complete that same admitted Request.

Ordinary expiry prevents new exercise but should not retroactively invalidate already-admitted work.

This direction remains working Pre-JIT doctrine until upstream Product/Entitlements authority resolves `HSP-UPD-001`.

### Admission versus expiry

Admission and expiry require one authoritative Entitlements ordering.

If authoritative admission wins first:

- the exact admitted Request may continue;
- the source entitlement becomes unavailable for new admission when it later expires.

If expiry wins first:

- the new Request must fail admission.

Queue insertion, worker start time, browser click time or stale cached access cannot decide this ordering.

### Queue insertion is not admission

Infrastructure scheduling is downstream of the business decision.

The semantic order is:

`validate current right → authoritatively admit exact Request → persist obligation → schedule execution`

A queue job does not itself create entitlement authority.

### Bounded means exact, not banked

The completion right is bounded by:

- exact Request identity;
- exact source/provenance;
- exact benefit class;
- no material scope expansion;
- continued Safety validity;
- governed operational completion limits.

It is not:

- a reusable carried-forward credit;
- a membership extension;
- authority for another Request;
- authority for another participant;
- a way to consume a later membership period;
- a bypass around new Safety facts.

### Renewal interaction

An older admitted Request remains funded by the commercial/entitlement occurrence that admitted it.

A later renewal does not silently become its new source.

A later renewal may create a separate new benefit under its own rules.

### Ordinary expiry is not generic revocation

The bounded-completion recommendation applies to ordinary entitlement/membership expiry.

It does not create a blanket rule that admitted work survives every later source change.

Distinct causes remain distinct:

- refund commitment;
- pending dispute;
- final chargeback/reversal;
- Safety invalidation;
- content/dependency withdrawal;
- participant material change of intent;
- professional capacity/remedy failure.

Those continue to follow their own Product/HSP/CER rules.

### Cross-seam preservation

`HSP-UPD-005` remains the customer-remedy question for genuinely unfulfillable admitted Plan work.

`HSP-UPD-006` remains the bounded professional-review delay/capacity-failure and remedy question.

`HSP-UPD-007` remains the generated-but-not-delivered refund-boundary question.

`HSP-UPD-008` remains the pre-first-fulfilment material participant change-of-intent question.

PT-014 does not silently resolve any of them.

### Store Blueprint findings

Store's generic digital grant model provides useful mechanisms including:

- explicit expiry timestamp;
- explicit expire operation;
- explicit revoke operation;
- revocation reason;
- idempotent grant issuance.

Those are reusable mechanics.

However, the inspected Store path does not prove a separate durable concept equivalent to:

`right valid → exact work admitted → source later expires → exact admitted obligation may still complete`

A simple current `active/expired/revoked` grant check is therefore insufficient for NewYou Plan/review fulfilment semantics.

### Store reuse conclusion

**ADAPTATION REQUIRED — GENERIC GRANT MECHANICS ONLY**

Reusable:

- durable grant identity;
- expiry timestamp;
- explicit expiry;
- explicit revocation/reason;
- idempotent issue.

Not proven for this semantic:

- Request-to-entitlement binding;
- admitted fulfilment obligation surviving ordinary expiry;
- professional/Plan completion authority distinct from current access;
- refund/dispute/Safety-aware in-flight treatment.

### Recommendation classification

- **Existing upstream Product gap:** `HSP-UPD-001`.
- **CER action:** pressure-test and strengthen the recommended direction only.
- **New CER Product amendment:** not required.
- **JIT concern:** exact representation/concurrency mechanism after upstream policy is resolved.
- **Store conclusion:** reuse generic grant mechanics only after adaptation.

### Carry-forward principles

**Expiry for new use does not necessarily erase an already-admitted obligation.**

**Admission and expiry must have one authoritative Entitlements ordering.**

**Queue insertion is not entitlement admission.**

**A validly admitted exact Request may retain a bounded completion right after ordinary source expiry.**

**Bounded completion is not membership extension.**

**Bounded completion is not a carried-forward reusable credit.**

**The completion right stays bound to the exact Request, source and benefit class.**

**Technical retries may continue the same admitted obligation; they may not multiply it.**

**A new membership period must not silently become the source for an older admitted Request.**

**Ordinary expiry, refund, dispute, chargeback, Safety invalidation and withdrawal are distinct causes with potentially different in-flight consequences.**

**Current entitlement validity answers new admission; it does not alone determine previously admitted fulfilment authority.**

**Safety may invalidate or pause commercial completion authority where current safe fulfilment no longer exists.**

**`HSP-UPD-001` remains the single upstream identity for the ordinary-expiry completion-right gap.**

**Store's generic expiry/revocation mechanics are reusable, but generic active/expired access status is insufficient for NewYou in-flight Plan/review semantics.**

---

## CER-PT-015 — Recovery/reconciliation after long outage, backlog and reordered provider events

### Status

- **NewYou semantic verdict:** PASS
- **Store Blueprint verdict:** CHANGES REQUIRED / REUSE AFTER HARDENING — STRONG RECOVERY CORE
- **New CER upstream delta:** None
- **NewYou evidence baseline:** `main` at `764010e8d3896f4430cc56b59997b9cbf85cec6c`
- **Baseline movement:** NewYou advanced from `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2` by a Privacy Evidence Pre-JIT documentation commit. The inspected diff did not amend routed Product, Architecture, Domain or Roadmap authority relevant to CER.
- **Store evidence baseline:** `main` remained `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` remained `77a272c3887a7ab46e84a7fed02163d964e37b9b` for the implementation path inspected by this test.

### Why no new Product gap exists

Current authority already requires the necessary semantics:

- durable payment truth is provider-independent and authoritative in PostgreSQL;
- Commerce owns commercial/provider reconciliation independently of Entitlements;
- provider callbacks and responses are evidence rather than business authority;
- mandatory post-commit consequences must be durable;
- queue uniqueness is not business idempotency;
- duplicate, reordered and ambiguous evidence must be reconciled without arrival-order authority.

The remaining choices are recovery representation, bounded discovery/scanning strategy, operational exception handling and Paystack validation. They belong to JIT/provider proof rather than a new Product amendment.

### Long outage does not recreate a renewal

A long application outage may cause browser returns, webhooks and workers to be delayed or missed while the provider has already processed a charge.

Recovery must ask:

> **What is the authoritative truth of the existing logical commercial occurrence?**

It must not ask:

> Which old job should be replayed as though the commercial occurrence never existed?

The stable logical collection identity established by `CER-PT-004` must survive process restart, deployment, queue loss, worker replacement and delayed provider evidence.

> **Recovery is about rediscovering and converging business truth, not recreating execution.**

### Technical retry exhaustion is not business finality

Provider webhook retries and local worker retries are finite technical delivery/execution mechanisms.

Their exhaustion must not itself turn an unresolved commercial occurrence into terminal `failed`, `paid`, `refunded`, `reversed` or any other fabricated business truth.

If authoritative finality remains unknown, NewYou must retain an explicit durable unresolved/exception condition that remains eligible for reconciliation or governed support handling.

> **Finite technical retry exhaustion must never manufacture false terminal business truth.**

### Reordered evidence after recovery

A backlog may contain failure, success, duplicate success and older pending observations for the same logical occurrence.

Recovery must not use arrival time, queue order or "last event wins" semantics as business finality.

Commerce must reconcile the stable occurrence against:

- durable NewYou state;
- provider evidence that remains available;
- the provider contract validated under `OQ-004`;
- current governing commercial authority;
- the previously accepted lifecycle and idempotency rules in this stream.

Historical provider observations remain evidence even when reconciliation changes the current authoritative interpretation.

### Stale evidence must revalidate current commercial authority

Recovery may discover old evidence after later participant or system decisions have changed what consequences remain permitted.

Examples include:

- cancellation accepted during grace;
- refund commitment;
- pending or final dispute/chargeback;
- downgrade or package transition;
- entitlement revocation;
- Safety invalidation where the benefit cannot safely continue.

Recovery may establish that money moved while still being forbidden from recreating a membership or access right that current Commerce/Entitlements authority no longer permits.

`CER-UPD-001` remains controlling for cancellation-before-late-renewal-success:

- authoritative cancellation first → no membership recreation;
- late financial movement enters reversal/refund or governed commercial-remedy handling.

> **Recovery of stale evidence must revalidate current Commerce authority before producing a present-day consequence.**

### Queue loss may lose execution, not obligation

A crash may occur after authoritative Commerce truth commits but before the downstream Entitlements/fulfilment job is successfully inserted or completed.

The outstanding business obligation must therefore be discoverable from durable truth rather than existing only as a queue pointer.

A queue job is an executor. It is not the sole durable evidence that a consequence is still owed.

The recovery target is not merely "webhook processed". It is either:

- converged authoritative Commerce truth plus all required Entitlements consequences; or
- an explicit durable unresolved/exception state with visible repair/support obligation.

### Accepted recovery invariant

> **For every durable commercial occurrence capable of affecting participant access, there must be a repeat-safe path from any recoverable interruption to either converged authoritative Commerce + Entitlements truth or an explicit durable unresolved/exception state. A finite worker retry budget may not itself terminate that obligation.**

### Targeted recovery rather than replay-everything

The recommended JIT direction is bounded discovery of durable mismatches/obligations, for example:

- commercially unresolved occurrences beyond an expected age;
- paid occurrences missing a required Entitlements consequence;
- refund/reversal truth missing the corresponding source-scoped access consequence;
- provider evidence whose local commercial interpretation remains unresolved;
- downstream work whose execution pointer disappeared while the durable obligation remains open.

A giant job that blindly replays all historical provider events is not recommended.

Exact Resources, queries, workers, scheduling and operational thresholds remain JIT decisions. Pre-JIT does not require a new `ReconciliationCase` Resource or new Domain.

### Paystack validation — verified 2026-09-09

Current official Paystack documentation provides useful recovery evidence without defining NewYou semantics:

- live webhook deliveries that do not receive `200 OK` are retried every three minutes for the first four tries and then hourly for the next 72 hours;
- Paystack documents polling/verification as an alternative means to obtain final/current status when webhook delivery is unavailable;
- the Verify Transaction API confirms transaction status by reference;
- documented non-final/other statuses include `ongoing`, `pending`, `processing`, `queued` and `reversed` in addition to success/failure states.

Primary sources checked:

- `https://paystack.com/docs/payments/webhooks/`
- `https://paystack.com/docs/api/transaction/`
- `https://paystack.com/docs/payments/verify-payments/`

These mechanics support, but do not create, the NewYou rule that webhook absence is not transaction absence and timeout is not authoritative failure.

Exact Paystack recurring-collection, dispute, refund and South African production reconciliation behaviour remains under `OQ-004`.

### Store Blueprint findings

Store contains a materially useful recovery core.

The inspected branch includes:

- durable receipt-first webhook evidence and duplicate identities;
- finite retrying webhook processing;
- a dedicated `ReconcilePaidSubscriptionRenewalWorker` rather than reissuing a new collection;
- reconciliation against an existing paid renewal order/attempt;
- entitlement synchronisation within the renewal reconciliation path;
- paid-order ensure workers for initial subscription and fulfilment consequences;
- an explicit `reconcile_pending_provider_setup` path;
- stable renewal/payment identities that support repeat-safe execution.

These are strong reusable mechanisms.

### Store terminal-convergence gap

The inspected path does not yet prove an independent durable repair loop that can rediscover every owed consequence after the execution pointer itself is lost.

The critical crash window is conceptually:

`payment application commits → downstream enqueue fails → later payment replay is already apply-once/no-op → required consequence may no longer be automatically rediscovered`

Likewise, finite webhook/ensure/reconciliation worker budgets do not by themselves prove that terminal job exhaustion leaves a separately discoverable business obligation.

This repeats the core PT-001 distinction at whole-system recovery level:

> **Retryability is not the same as recoverability.**

Store also retains the `CER-PT-003` defect where a local failed PaymentIntent lifecycle can block later verified success for the same provider attempt.

A recovery mechanism that can discover correct evidence but cannot represent the resulting correct local truth is not fully recoverable.

### Store reuse conclusion

**CHANGES REQUIRED / REUSE AFTER HARDENING — STRONG RECOVERY CORE**

Strongly reusable:

- webhook evidence/dedupe;
- stable renewal identity;
- paid-renewal reconciliation shape;
- paid-order ensure-worker shape;
- pending-provider-setup recovery;
- repeat-safe local business idempotency mechanisms.

Hardening required:

- rediscovery after post-commit enqueue loss;
- rediscovery after finite worker exhaustion;
- late failed→success provider truth (`CER-PT-003`);
- repair of Commerce→Entitlements mismatches without relying on the original queue job;
- current-authority revalidation before applying stale recovered consequences;
- Paystack-specific adapter/verification proof under `OQ-004`.

### Recommendation classification

- **Product amendment:** none.
- **Architecture/Domain requirement:** existing authority already requires durable convergence/reconciliation.
- **Pre-JIT doctrine:** recovery is a business capability, not merely retry configuration.
- **JIT:** exact durable obligation representation, discovery queries, workers, schedules, escalation thresholds and operational dashboards.
- **Provider validation:** exact Paystack reconciliation behaviour under `OQ-004`.
- **Store:** retain the existing recovery core and harden terminal convergence rather than redesigning the engine from scratch.

### Carry-forward principles

**Recovery is a business capability, not merely worker retry.**

**Technical retry exhaustion must not manufacture terminal business truth.**

**Reconciliation derives current commercial truth from stable logical identity, durable NewYou state, available provider evidence and current governing authority — not provider-event arrival order.**

**Restart, deployment, queue loss and webhook retry exhaustion may interrupt execution but may not erase an outstanding commercial obligation.**

**Recovery of stale evidence must revalidate current Commerce authority before producing current access or membership consequences.**

**Business idempotency must survive worker identity, queue identity and process lifetime.**

**Commerce-to-Entitlements convergence must remain independently repairable after the original consequence-delivery path fails.**

**Unresolved ambiguity must remain explicitly unresolved and visible; it must not be fabricated into success or failure.**

**Recovery should target durable unresolved or mismatched obligations rather than blindly replaying all historical events.**

**Historical provider observations remain evidence even when reconciliation changes the current authoritative interpretation.**

---

### Second-pass Candidate 14 refinement — recovery to latest target set

Recovery after partial Commerce→Entitlements convergence derives the latest authoritative source-specific entitlement target and reconciles toward it.

It does not infer correctness from the last worker step believed to have run.

A stale target/version must not overwrite a newer target after restart, backlog or out-of-order delivery.

## CER-PT-016 — Monthly ↔ annual billing cadence transition

### Status

- **Second-pass candidates:** Candidate 1 created this PT; Candidate 2 materially refined the same semantic class
- **Coverage assessment:** NEW SEMANTIC CLASS from Candidate 1; MATERIAL EXTENSION from Candidate 2
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING / ADAPTATION REQUIRED
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-005` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** None for cadence transition itself; Premium continuity effects remain reserved for second-pass Candidate 13.
- **Provider gate:** `OQ-004`
- **Disposition:** CREATE `CER-PT-016` from Candidate 1; REFINE EXISTING `CER-PT-016` for Candidate 2; no new PT
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `77a272c3887a7ab46e84a7fed02163d964e37b9b`
- **Store PR movement:** draft PR #11 targets `hardening/subscriptions` and promotes governance files while reporting no source/runtime change; it does not alter the inspected implementation baseline.

### Why this earned a new PT

Current Product authority supports both monthly and annual membership billing but does not define switching between them.

`DEC-046` defines upgrades as immediate with provider-supported proration and downgrades as renewal-effective, but current authority does not establish that a same-composition billing-cadence change is either an upgrade or downgrade.

Existing CER tests therefore do not determine:

- whether monthly→annual is immediate or boundary-effective;
- what happens to remaining paid monthly time;
- whether an implicit credit exists;
- when the annual paid period starts;
- which cadence wins if a monthly renewal is already queued/in flight.

These are customer-money and purchased-duration semantics, not incidental implementation choices.

### Durable truths

#### Commerce

Commerce owns:

- one current membership commercial relationship;
- current membership composition;
- current billing cadence;
- current paid-period boundaries;
- future cadence instruction;
- effective boundary;
- target commercial contract/price version;
- logical renewal occurrence;
- payment and reversal truth.

#### Entitlements

Where the membership composition itself is unchanged, monthly→annual cadence change should not create a second membership source or revoke/regrant unchanged effective rights.

The exact effect on continuity-derived annual Premium reassessment remains intentionally deferred to second-pass Candidate 13.

### Options considered

#### A. Immediate annual conversion with credit/proration

Possible in principle, but it requires Product to define unused monthly value, credit/proration basis, annual commencement, adjustment failure/ambiguity and related money rules.

Current Product authority does not define those promises.

#### B. Annual cadence takes effect at the next not-yet-committed renewal boundary

**Accepted recommendation.**

The current monthly paid period remains intact. At its boundary, one annual renewal occurs if the cadence instruction won the Commerce ordering before the monthly renewal became commercially committed.

This is the simplest model that preserves paid time, avoids implicit credits and composes with existing renewal-boundary doctrine.

#### C. Immediate annual conversion with no credit

Rejected.

It can silently destroy already-purchased monthly time.

#### D. Create a second annual membership alongside the monthly one

Rejected.

It would create competing membership authority and duplicate billing/access risk.

#### E. Treat cadence change automatically as a `DEC-046` upgrade

Rejected as an unsupported interpretation shortcut.

Commercial attractiveness to NewYou does not itself make cadence change a Product-defined membership upgrade.

### Boundary/concurrency rule

One authoritative Commerce ordering decides:

`future annual cadence instruction`
versus
`monthly renewal commercially committed/verified-paid`

If the cadence instruction wins first:

`monthly period ends → annual renewal`

If the monthly renewal wins first:

`new monthly paid period remains true → annual instruction moves to following renewal boundary`

A queued monthly job, mutable provider object or callback arrival order is not contract authority.

### Billing anchor

Under the accepted default, the annual paid period begins at the effective monthly-period boundary.

Example:

`1 Sep → 1 Oct monthly`
then
`1 Oct → 1 Oct next year annual`

No independent mid-period anchor is invented.

### Price-version boundary intentionally deferred

If annual price changes between customer selection and the effective boundary, Candidate 1 does not decide which price applies.

Second-pass Candidate 5 subsequently resolved existing-member price/version migration and grandfathering semantics through `CER-PT-017` / `CER-UPD-007`.

### Duplicate future-change commands

Multiple cadence/package/cancellation changes before the boundary still require one current authoritative future instruction and immutable history.

Second-pass Candidate 10 subsequently resolved supersession in detail as a material refinement of `CER-PT-008`.

### Recovery

Once accepted, a cadence-change instruction must survive crash/restart independently of queue insertion.

Existing PT-015 recovery doctrine applies.

### Store Blueprint findings

Store `SubscriptionPlan` models cadence through `interval_unit` and `interval_count`, with amount and anchor configuration.

Store `Subscription` also exposes pending target-plan, pending renewal amount/currency and `change_effective_at` fields with a queued-change action.

Those mechanisms are useful evidence for a boundary-effective cadence change.

However, existing PT-007/PT-008 findings remain blocking for reuse as-is: mutable pending target fields can be reconciled against a payment priced under older terms unless the renewal occurrence is bound to an immutable priced/charged contract snapshot.

A provider charge actually made under monthly terms must never be promoted into an annual paid period merely because the pending plan later says annual.

### Candidate 2 refinement — Annual → monthly

Candidate 2 confirmed that annual→monthly is not a distinct semantic class.

The annual paid period remains authoritative through its existing end. Starting monthly billing early would either duplicate payment for already-purchased access or require an explicit early-termination/refund/credit rule.

Therefore the accepted cadence invariant is bidirectional:

`same membership composition + cadence change → preserve current paid period → apply new cadence at next not-yet-committed renewal boundary`

This means:

- monthly→annual preserves the current monthly period and begins annual billing at the next boundary;
- annual→monthly preserves the current annual period and begins monthly billing at the next boundary;
- neither direction creates a second membership;
- neither direction creates an implicit refund/credit;
- neither direction is silently classified as a `DEC-046` upgrade/downgrade merely because cadence changes.

If the target-cadence renewal fails at the boundary, existing failed-renewal/grace/suspension doctrine applies to that new renewal occurrence. The old paid period does not silently extend.

A later cancellation-at-period-end instruction may supersede the pending cadence renewal under PT-008.

Already-earned membership-derived rights are not revoked merely because cadence changes; Premium continuity/reassessment-trigger semantics were subsequently resolved by Candidate 13 through `CER-PT-020` / `CER-UPD-012`.

### Why Candidate 2 did not earn a new PT

Both directions share one durable commercial class:

`same membership + current paid period + future cadence instruction + one renewal boundary`

The economic consequences are asymmetric, but the governing invariant is the same: do not truncate already-purchased time and do not create overlapping billing.

Creating another PT solely for reverse direction would fragment one semantic rule.

### Recommendation classification

- **Upstream Product/commercial decision:** monthly→annual default cadence-transition rule (`CER-UPD-005`).
- **JIT implementation recommendation:** one authoritative future instruction plus immutable renewal-contract snapshot.
- **Store reuse/hardening recommendation:** reuse cadence-aware plan/change mechanisms only after PT-007/PT-008 hardening.
- **Provider validation:** `OQ-004` validates execution capability after NewYou semantics are governed.

### Carry-forward principles

**Billing cadence is part of the commercial contract, not entitlement identity.**

**A same-composition cadence change must not create a second membership or revoke/regrant unchanged membership rights.**

**Under accepted `CER-UPD-005`, ordinary monthly↔annual cadence changes default to the next not-yet-committed renewal boundary.**

**The existing paid period remains authoritative through its existing end in either cadence direction; no implicit forfeiture, refund, credit or overlapping billing is created.**

**Cadence change and renewal require one Commerce-owned boundary ordering.**

**A mutable future cadence/plan must never rewrite the cadence/price actually authorised and charged for an already-committed renewal occurrence.**

**Candidate 5 / `CER-PT-017` / `CER-UPD-007` subsequently resolved the target price/version question for this discovery.**

---

---

## CER-PT-017 — Existing-member recurring price/version migration

### Status

- **Second-pass candidate:** 5 of 15
- **Coverage assessment:** NEW SEMANTIC CLASS
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING / ADAPTATION REQUIRED
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-007` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** Candidate 6 for promotions; Candidate 13 for continuity-derived rights
- **Provider gate:** `OQ-004`
- **Expert gate:** South African consumer-protection/legal review before final Product freeze
- **Disposition:** CREATE `CER-PT-017`
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`

### Why this earned a new PT

Existing CER already defines renewal identity, stale-evidence recovery, future contract instructions, cadence transitions and immutable paid occurrences.

It does not define which recurring price applies when NewYou changes the public/list price for an already-active member.

That is a separate customer-money lifecycle class.

### Durable Commerce truths

Commerce must distinguish:

`public/list offer`
≠
`member's current commercial contract`
≠
`future price-change instruction`
≠
`renewal occurrence`
≠
`amount actually charged`

Publishing a new list price does not rewrite the member's current paid period or an already-committed renewal.

The relevant durable question is:

`which exact price/version was authoritative for this membership occurrence at this renewal boundary?`

### Durable Entitlements truth

A same-package price change is Commerce truth.

Entitlement identity does not change merely because the recurring price changes.

Entitlements consume the resulting authoritative membership-period validity/provenance; they do not own list-price or price-migration truth.

### Options considered

#### A. Grandfather every existing member forever

Rejected as the default because it would create a large accidental commercial promise.

Explicit grandfathering remains permitted when Product deliberately promises it.

#### B. Apply the increase immediately to an already-paid period

Rejected.

Already-purchased time cannot be retrospectively repriced.

#### C. Let every future collection use whatever public/provider price is current at execution time

Strongly rejected.

Mutable configuration would become the commercial contract and could change the amount of replayed or queued renewal work.

#### D. Explicit future-boundary price migration

**Accepted recommendation.**

A new public price creates a new offer/price version.

For an existing active membership, a higher price may apply only to an eligible future not-yet-committed renewal after exact target terms and all required notice/consent/legal conditions are satisfied.

### Monthly-member consequence

An existing monthly member may move to the new price only from an eligible future renewal.

If transition requirements are incomplete at the next renewal, NewYou must not surprise-charge the higher amount for that occurrence.

### Annual-member consequence

An already-paid annual period remains unchanged.

Only a later renewal can be governed by the new annual price.

Exact statutory/contractual treatment of the annual agreement/renewal structure requires the legal expert gate.

### Consumer-protection/legal gate

CER does not make a legal conclusion about whether every NewYou monthly or annual membership agreement is a statutory fixed-term agreement, nor does it invent a universal affirmative-consent requirement.

Before final Product authority freezes price-change and renewal mechanics, legal review must determine the minimum applicable consumer-law constraints for the intended contract structures.

Product may then choose a stronger customer-friendly promise above that legal floor.

### Recommended Product promise above the legal floor

1. Never reprice an already-paid period.
2. Never let a list-price edit itself rewrite an existing member's contract.
3. Give clear advance notice before the first higher-price renewal.
4. Do not charge the higher amount where required transition conditions are incomplete.
5. Make grandfathering/price locking explicit rather than accidental.

### Grandfathering attachment

Default recommendation:

`explicit qualifying membership occurrence / offer`

not:

`person/account forever`

and never:

`provider plan identifier`

Candidate 4's post-termination rule therefore remains intact: a later new membership occurrence does not inherit an old price solely because the same participant previously held it.

### Price-change / renewal race

One Commerce-owned ordering decides whether the old or new price version is authoritative for a renewal.

If renewal commits first, its price snapshot remains immutable.

If a valid new price migration becomes authoritative first, the renewal must use that new exact price/version.

### Provider amount mismatch

Provider-charged amount is financial evidence, not contract authority.

A mismatch between expected and charged amount must enter explicit Commerce reconciliation/exception handling.

### Cancellation before effective increase

If the participant validly cancels before the higher-price renewal, the current paid period completes and the higher-price renewal does not occur.

`CER-UPD-006` rescission can later restore renewal intent before termination, but the restored renewal must use the currently applicable valid contract terms, not automatically the historical price.

### Cadence + price transition

Candidate 1/2 intentionally deferred the target-price question here.

Where cadence and price both change, the future renewal must resolve one coherent commercial contract:

- package;
- cadence;
- price;
- currency;
- effective boundary;
- applicable offer/version.

A fixed target cadence must not be combined with a later mutable price lookup.

### Store Blueprint findings

Store's current `SubscriptionPlan` has mutable `amount_minor` and currency.

That row must not become existing-member renewal authority.

Store's Subscription separately carries `renewal_amount_minor` / `renewal_currency` plus pending renewal amount/currency fields, which is a useful reuse seam because it already distinguishes subscription renewal terms from current public plan configuration.

Store still needs hardening/adaptation for:

- explicit price-version migration;
- grandfathering/price-lock provenance;
- advance effective boundary;
- legal/notice eligibility;
- immutable renewal price snapshot;
- price-change/renewal race ordering;
- provider amount mismatch handling.

### Recommendation classification

- **Upstream Product/commercial decision:** `CER-UPD-007`
- **Legal / consumer-protection expert gate:** required before Product freeze
- **JIT implementation recommendation:** immutable effective price/version per renewal occurrence
- **Store reuse/hardening recommendation:** preserve subscription-level renewal snapshots; do not use mutable plan price as authority
- **Provider validation:** `OQ-004`

### Carry-forward principles

**Public/list price is not existing-member contract authority.**

**A price change never reprices an already-paid period or already-committed renewal.**

**Existing-member price migration requires an explicit future effective contract, not a mutable lookup at collection time.**

**A higher-price renewal must fail closed against the increase if required transition conditions are incomplete.**

**Grandfathering/price locking is deliberate Product truth, not an accidental historical-list-price property.**

**A post-termination re-subscription does not inherit an old price solely because the same participant previously held it.**

**Provider amount/configuration is evidence only and cannot redefine NewYou price-contract truth.**

---

## CER-PT-018 — Recurring promotional pricing lifecycle

### Status

- **Second-pass candidate:** 6 of 15
- **Coverage assessment:** NEW SEMANTIC CLASS
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING / ADAPTATION REQUIRED
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-008` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** `CER-UPD-007` for base-price migration; Candidate 13 only where continuity becomes a promotion condition
- **Provider gate:** NONE inherently; `OQ-004` only for provider-specific execution mechanics
- **Disposition:** CREATE `CER-PT-018`
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`

### Why this earned a new PT

Finite recurring promotion has its own lifecycle: `qualify → bind promotional rule → discounted paid occurrences → consume finite scope → expire → ordinary pricing`. Existing price-migration doctrine does not define that lifecycle.

### Durable truths

Commerce distinguishes base-price contract/version, promotional rule, promotion eligibility, renewal/payment attempt and successfully established paid-period occurrence. Entitlements do not own promotion identity.

### Accepted semantics

For ordinary cycle-limited recurring promotions, promotional scope is consumed by successful qualifying paid periods unless the offer explicitly defines a calendar/time-window basis. Failed attempts and retries do not consume extra cycles; a renewal that never establishes a paid period consumes none.

Unused promotional cycles are not standalone/banked credits. After genuine termination, a new membership occurrence evaluates current eligibility and neither automatically inherits unused historical promotion value nor automatically resets a once-only promotion.

An accepted recurring promotion is immutable against later public Promotion definition mutation/deactivation for its promised scope.

Upgrade, downgrade and cadence transitions must resolve the exact target contract, including base price/version, promotion applicability, remaining promotional scope and duration basis.

Promotion expiry is not itself a unilateral base-price increase where the higher post-promotion amount was part of the accepted staged offer. Underlying base-price migration remains separately governed by `CER-UPD-007`.

### Store Blueprint findings

Store has strong deterministic transaction-pricing primitives, persisted promotion provenance, eligibility windows and stacking/exclusivity rules. It does not yet prove recurring first-N-paid-period consumption, remaining promotional scope, recurring occurrence attachment, package/cadence applicability, post-termination handling, once-only repeat eligibility or immutable preservation of an accepted recurring promise after public promotion mutation.

### Carry-forward principles

**Recurring promotion is Commerce pricing truth, not entitlement identity.**

**Base price and promotional adjustment are distinct commercial truths.**

**Cycle-limited promotional scope is consumed by successful qualifying paid periods, not attempts or retries.**

**Unused promotional cycles are not standalone/banked credits by default.**

**Post-termination re-subscription neither automatically inherits remaining promotion value nor automatically resets once-only eligibility.**

**Public promotion mutation cannot retroactively rewrite an accepted recurring promotion promise.**

**Package/cadence changes must resolve exact target promotion applicability and semantic duration basis before commitment.**

**Promotion expiry and ordinary base-price migration are separate events.**

---

## CER-PT-019 — Concurrent duplicate ordinary membership purchase

### Status

- **Second-pass candidate:** 7 of 15
- **Coverage assessment:** NEW SEMANTIC CLASS
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-009` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** Candidate 15 for legitimate overlapping paid/gift/sponsored/complimentary sources
- **Provider gate:** `OQ-004` for reversal/refund mechanics and provider idempotency capability only
- **Disposition:** CREATE `CER-PT-019`
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`

### Why this earned a new PT

PT-002 covers replay/duplication of evidence for one commercial occurrence.

Candidate 7 covers two distinct purchase/payment occurrences that both genuinely succeed while only one ordinary membership relationship should exist.

Provider transaction idempotency cannot solve this class by itself.

### Durable truths

Commerce distinguishes customer action, purchase intent, commercial admission, payment attempt, successful financial collection and membership contract.

Two distinct provider successes do not imply two valid ordinary memberships.

Entitlements follow Commerce's commercial resolution and must not multiply access merely because two payments exist.

### Grantee boundary

Duplicate exclusion applies to the intended canonical grantee/commercial membership relationship, not merely purchaser identity.

A purchaser may legitimately buy for herself and another recipient.

Gift/sponsored/complimentary overlap was subsequently resolved by Candidate 15 / `CER-UPD-013`.

### Accepted resolution

Exactly one ordinary membership purchase may be authoritatively admitted.

If another conflicting purchase also succeeds financially:

`one valid membership`
+
`one duplicate/excess collection requiring reversal/refund/remedy`

The duplicate payment must not create a second paid period, recurring obligation or entitlement.

### Winner ordering

The valid membership source is the purchase that wins NewYou's authoritative Commerce admission ordering.

Not:

- first provider callback;
- first provider success timestamp;
- lexicographically first provider reference;
- whichever payment is easier to refund.

### Different-package concurrent purchases

If concurrent purchase attempts target materially different packages/cadences, NewYou must still admit at most one ordinary membership relationship.

The non-admitted purchase cannot silently become a second membership.

The participant may later use governed upgrade/cadence-change flows to change the admitted relationship.

### Duplicate-payment remedy

Recommended default is full reversal/refund of the non-admitted successful collection.

No second valid membership benefit was legitimately admitted from it.

An accidentally emitted duplicate entitlement is an implementation defect and does not justify retaining duplicate money.

### Provider idempotency boundary

Provider idempotency remains necessary for retries of one intended payment.

It is insufficient across two genuinely distinct NewYou purchase/payment attempts with separate provider references or keys.

Business duplicate prevention therefore remains a NewYou Commerce responsibility.

### Recovery

If the system crashes after both payments succeed but before duplicate classification/remedy, PT-015 applies.

Recovery must preserve a discoverable path to:

`one valid membership`
+
`duplicate-payment remedy pending/completed`

Finite worker exhaustion cannot orphan the duplicate financial obligation.

### Store Blueprint findings

Store has a useful `ensure_membership_purchase_allowed_for_system` admission guard checking both open memberships and pending membership orders before allowing another membership purchase.

Store also correctly separates renewal orders from initial subscription creation.

However, the inspected Subscription identities are source-order-line and provider-subscription based rather than a proved durable uniqueness invariant over the open ordinary membership relationship.

Therefore current evidence does not prove the two-tab concurrency race is impossible.

Required Store proof/hardening includes:

- atomic/concurrency-safe exclusion;
- two simultaneous initial membership purchases;
- two distinct successful provider charges;
- one membership consequence;
- source-scoped duplicate refund/remedy;
- no duplicate recurring provider subscription.

### Carry-forward principles

**Provider replay duplication and genuinely duplicated customer purchase attempts are different failure classes.**

**At most one ordinary recurring membership commercial relationship may be admitted for the same canonical grantee at a time.**

**Two real successful payments do not automatically create two valid memberships or two paid periods.**

**NewYou's Commerce admission ordering, not provider callback order, decides which conflicting purchase is authoritative.**

**A successful non-admitted duplicate collection requires full reversal/refund or governed make-whole handling by default.**

**Provider transaction idempotency is necessary but insufficient for business-level duplicate membership prevention.**

**Duplicate-payment remediation must be source-scoped and must not damage the valid membership.**

---

## CER-PT-020 — Premium reassessment continuity and annual maturity

### Status

- **Classification:** NEW SEMANTIC CLASS
- **Originating NewYou verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Originating upstream delta:** `CER-UPD-012`
- **Accepted later multi-source refinement:** `CER-UPD-013`
- **Store verdict:** NEWYOU-SPECIFIC ADAPTATION REQUIRED; overall Store reuse remains CHANGES REQUIRED / REUSE AFTER HARDENING
- **Provider boundary:** no new semantic provider gate; provider evidence only supports Commerce truth
- **Disposition:** accepted second-pass PT / later refined by Candidate 15

### Scenario

A Premium member approaches or crosses the annual reassessment maturity boundary while any of the following may occur:

- monthly↔annual cadence change;
- price/promotion/payment-method change;
- failed renewal and 72-hour grace;
- seamless self-paid↔gift↔sponsored Premium source substitution;
- overlapping Premium sources;
- Premium→Basic downgrade and later re-upgrade;
- genuine or apparent coverage gap;
- annual renewal;
- an already-unused reassessment entitlement existing at a later anniversary.

### Core invariant

`12 continuous Premium months` means twelve calendar months of uninterrupted authoritative qualifying Premium coverage for the canonical grantee.

It is not equivalent to twelve successful charges, one provider authorization, one payer, one subscription row, one cadence or one funding source.

### Annual renewal interpretation

Annual renewal is the annual-billing expression of the same anniversary maturity rule.

Initial annual purchase and switching into annual billing do not accelerate or independently trigger the benefit.

### Continuity-preserving changes

The following do not reset continuity where qualifying Premium coverage remains uninterrupted:

- monthly↔annual cadence changes;
- price changes;
- promotion changes;
- payment-method replacement;
- seamless transition between qualifying self-paid, gift and sponsored Premium sources.

### Grace / failed renewal

Grace access itself is not qualifying paid Premium tenure.

If reconciliation proves a Premium period existed continuously from the boundary, continuity is preserved.

If the renewal remains unpaid and the Premium period never authoritatively existed, continuity breaks at the prior paid-period end.

### Continuity-breaking events

- downgrade to Basic;
- qualifying Premium termination;
- any genuine uncovered Premium interval.

A later Premium upgrade begins a new continuity interval.

### Overlapping sources

Multiple simultaneous qualifying Premium sources count calendar time once.

They do not accelerate anniversary maturity.

### Nonaccumulation

At most one unused reassessment entitlement may exist.

If one is already unused at a later qualifying anniversary, no second/catch-up entitlement is banked.

After later consumption, the next entitlement becomes available only at the next future qualifying anniversary.

### Expiry

An unused Premium reassessment entitlement expires when qualifying Premium coverage ends, even if the broader membership relationship continues as Basic.

Completed assessment history remains separately governed and is not destroyed by Premium ending.

### Store boundary

This is NewYou Product logic, not generic Store commerce policy.

Store should preserve the commercial-period/provenance evidence NewYou needs to evaluate continuity; it should not embed this 12-month benefit rule.

---

### Second-pass Candidate 15 refinement — overlapping sources and benefit multiplicity

Candidate 15 confirms that overlapping qualifying Premium sources do not multiply continuity clocks, annual reassessment maturity or standard recurring limited benefits.

Ordinary overlap preserves one participant-level Premium continuity timeline and one Product-defined ordinary monthly/annual benefit cadence.

Additional consumable units may exist only where an explicit governed offer/grant promises additive value.

## Second-pass Candidate 15 — Multiple legitimate overlapping entitlement sources

### Status

- **Coverage assessment:** MATERIAL EXTENSION OF `CER-PT-011`, `CER-PT-012`, `CER-PT-020`, plus Candidate-14 convergence doctrine
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT CLARIFICATION REQUIRED
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-013` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** NONE NEW
- **Provider gate:** NONE NEW
- **Disposition:** MATERIAL EXTENSION — NO NEW CER-PT REQUIRED
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `hardening/subscriptions` at `54871ef3bdda42f067ed5dbd398305151610c060`

### Accepted general model

Many legitimate sources may coexist for one canonical grantee.

Each source retains independent provenance, validity and revocation.

Effective access is resolved by capability, not by choosing one global source winner.

### Boolean/scoped access

A capability is available when at least one valid qualifying source grants it.

Duplicate sources do not produce “double access”.

Revoking one source leaves equivalent access intact where another source remains valid.

### Commercial membership is not inferred from effective access

A participant can have Basic membership plus enough access-overlay grants to resemble Premium capability-wise without Commerce becoming Premium.

Entitlement equivalence does not imply commercial-contract equivalence.

### Grant classes

An access-overlay grant changes only its governed scopes.

A qualifying membership-coverage grant may substitute the covered membership composition for its governed interval and may suppress redundant future self-paid collection.

Partial grants affect only the covered component.

### Limited/consumable benefits

Overlap alone does not multiply ordinary recurring benefits.

Two qualifying Premium sources do not automatically create two monthly reviews, two annual reassessment clocks or doubled nonaccumulating credits.

Additional units arise only where an explicit governed offer/grant promises additive value.

### Consumption

One fulfilment consumes exactly one authoritative eligible benefit occurrence/source according to deterministic, auditable Product/JIT rules.

Consumption must not debit every matching source.

### No global source priority

No hierarchy such as `lifetime > sponsored > gift > paid` is authorised.

Mixed sources may cover different capabilities and periods.

### Store Blueprint findings

Store's source-aware EntitlementGrant identity and any-valid-grant access check are strong reusable primitives.

Current Store source taxonomy remains subscription-only and does not provide:
- gift/sponsor/complimentary/lifetime source classes;
- access-overlay versus membership-coverage semantics;
- additive/non-additive limited benefits;
- general consumable-source selection/reconciliation.

NewYou-specific Premium/review rules must remain outside the generic Store engine.

### Carry-forward principles

**Multiple legitimate entitlement sources may coexist without merge or global winner.**

**Boolean/scoped effective access is the union of valid qualifying sources.**

**Effective access equivalence does not rewrite Commerce membership truth.**

**Access-overlay grants do not alter billing or membership-tenure qualification unless explicitly authorised.**

**Qualifying membership-coverage grants may substitute covered future commercial intervals and suppress only redundant covered billing.**

**Overlap alone does not multiply recurring limited benefits or continuity clocks.**

**Additional consumable units require explicit additive Product/grant authority.**

**Consumption applies once to one authoritative eligible occurrence/source with preserved provenance.**

**No global source-priority hierarchy is authorised.**

---

## Second-pass Candidate 14 — Partial Commerce→Entitlements convergence during composition change

### Status

- **Coverage assessment:** MATERIAL EXTENSION OF `CER-PT-001`, `CER-PT-011`, AND `CER-PT-015`
- **NewYou semantic verdict:** PASS
- **Store Blueprint verdict:** CHANGES REQUIRED
- **Reuse classification:** ADAPTATION REQUIRED / REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** NONE
- **Cross-stream dependency:** Candidate 15 for general multi-source entitlement composition
- **Provider gate:** NONE NEW
- **Disposition:** MATERIAL EXTENSION — NO NEW CER-PT REQUIRED
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `hardening/subscriptions` at `54871ef3bdda42f067ed5dbd398305151610c060`

### Accepted convergence model

Each commercial membership/add-on source has one latest authoritative entitlement target set/version.

Entitlements converges the source to that exact target.

The transition is not defined as “grant these things, then revoke those things” or the reverse.

### Transitional safety

If final target presentation cannot be atomic, effective access during incomplete convergence must:

- not exceed the new target set; and
- preserve rights common to old and new sets.

Conceptually, the safe interim floor/ceiling is constrained by `OLD ∩ NEW`.

### Upgrade

For `Basic → Premium`, Basic remains valid while newly added Premium rights wait for authoritative target acceptance.

### Downgrade

For `Premium → Basic`, Premium-only rights must not remain beyond their valid boundary, while Basic must remain intact.

### Component swap

For `{Basic, A} → {Basic, B}`, Basic remains continuous, A ceases on time, and B appears only when the target transition is authoritative.

### Crash/retry/reordering

Recovery derives the latest authoritative target from durable truth and reconciles toward it.

A stale V2 worker must not overwrite a newer V3 target.

Duplicate delivery of the same target is idempotent.

### Source isolation

Membership-source changes operate only on that source's grants.

Equivalent rights provided by gift, sponsor, complimentary, lifetime or other valid sources remain untouched.

### Cache/projection boundary

Caches and projections do not become access authority and must not extend revoked or expired access.

Any acceleration layer requires correctness proof and is not imported from Store by default.

### Store Blueprint findings

Store's current entitlement orchestration uses source-aware individual grants but issues/revokes at individual-grant/source level rather than proving an exact source-specific target-set transition.

The current subscription reconciliation path issues the current plan entitlement, while source-wide revocation is used for cancellation/grace expiry.

This does not prove safe component migration such as `{Basic, A, B} → {Basic, A}`.

Store also maintains a Cachex-backed entitlement-set snapshot, which is useful only if stale-cache behavior cannot extend authority.

### Carry-forward principles

**Each commercial source has one latest authoritative entitlement target set/version.**

**Composition transitions converge to the target set, not to a guessed sequence of grant/revoke steps.**

**Incomplete convergence must not overgrant beyond the new target or remove rights common to old and new sets.**

**Unchanged component rights remain continuous.**

**Stale, duplicate and reordered target application must not produce superseded entitlement truth.**

**Recovery derives the current target from durable authority, not worker history.**

**Other independently valid entitlement sources remain untouched.**

**Caches/projections cannot extend entitlement authority.**

---

## Second-pass Candidate 13 — 12 continuous Premium months / annual reassessment maturity

### Status

- **Coverage assessment:** NEW SEMANTIC CLASS
- **New PT:** `CER-PT-020`
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** NEWYOU-SPECIFIC ADAPTATION REQUIRED; overall Store reuse remains CHANGES REQUIRED / REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-012` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** Candidate 15 only for general overlapping-source composition; no new HSP/Privacy delta
- **Provider gate:** none new; provider evidence remains an input to Commerce reconciliation
- **Disposition:** NEW SEMANTIC CLASS → `CER-PT-020`
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `hardening/subscriptions` at `54871ef3bdda42f067ed5dbd398305151610c060`; PR #12 is governance-only and changed no production source/migrations/configuration

### Accepted continuity model

Qualifying time is measured by uninterrupted authoritative Premium coverage of the canonical grantee.

It is not measured by:

- number of successful charges;
- one payment method;
- one payer;
- one provider customer/authorization;
- one subscription record;
- one billing cadence.

### Annual renewal

The first authoritatively paid annual renewal at the first anniversary is the annual-billing expression of the same twelve-month maturity boundary.

Initial annual purchase and switching into annual billing do not independently trigger the benefit.

### Seamless source transitions

Self-paid, gift-funded and sponsored Premium periods preserve continuity when:

- each offer is governed as qualifying Premium membership coverage; and
- no uncovered Premium interval exists.

Partial Premium-like grants do not qualify merely because they expose equivalent rights.

### Grace

Grace access does not itself add qualifying Premium tenure.

Continuity at a failed-renewal boundary remains provisional until Commerce establishes whether the new Premium paid period actually existed.

### Downgrade / gap / re-upgrade

Premium→Basic or any genuine uncovered Premium interval breaks continuity.

A later Premium transition begins a new continuity interval.

### Overlap

Two qualifying Premium sources overlapping for one month still equal one month of elapsed Premium continuity.

Source overlap never accelerates maturity.

### Expiry and nonaccumulation

An unused reassessment entitlement expires when qualifying Premium ends, even if Basic continues.

At most one unused reassessment entitlement may exist.

If it remains unused across a later anniversary, no additional/catch-up entitlement is banked.

After later consumption, the next benefit waits until the next future qualifying anniversary.

### Store baseline movement

Store `hardening/subscriptions` advanced to `54871ef3...` through governance-only PR #12. Runtime findings therefore remain materially applicable, but this new SHA is the evidence baseline for Candidate 13.

The NewYou-specific 12-month benefit must not be pushed into the reusable Store package.

---

## Second-pass Candidate 12 — Gift/sponsor overlaps an already-active membership

### Status

- **Coverage assessment:** MATERIAL EXTENSION OF `CER-PT-012`
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-011` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** Candidate 15 for general overlapping entitlement-source composition
- **Provider gate:** `OQ-004` for exact self-billing pause/defer/resume mechanics only
- **Disposition:** MATERIAL EXTENSION OF `CER-PT-012` — NO NEW CER-PT

### Accepted default model

Prepaid gift/sponsor value remains a distinct source and does not overwrite existing membership provenance.

Equivalent already-paid coverage must not silently consume the incoming duration in parallel by default.

For ordinary duration-based coverage:

`existing paid coverage`
→
`gift/sponsor coverage at next eligible uncovered boundary`
→
`optional self-paid resumption only under governed authority`

### Pre-redemption overlap evaluation

Before code redemption becomes irrevocable, NewYou must identify the canonical grantee, evaluate relevant active/already-committed coverage, disclose any material timing/composition consequence, and only then consume redemption exactly once.

### No double billing

A fully gift/sponsor-funded period must not also collect overlapping ordinary self-paid renewal for the same composition.

### Fixed-duration gift

Self-paid renewal after gift expiry may resume only when the resulting schedule was clearly disclosed/accepted and payment authority remains valid.

### Recurring/open-ended sponsorship

Personal billing must not unexpectedly restart when uncertain-duration sponsorship ends unless the participant explicitly opted into that fallback.

Sponsor termination stops future funding only; already-funded current coverage remains valid.

### Existing cancellation

Applying gift/sponsorship does not silently rescind a self-paid membership cancellation.

A gift may establish future gift-funded coverage while the old self-paid recurring relationship remains scheduled not to renew.

### Composition mismatch

A Premium recipient receiving Basic gift, or a Basic recipient receiving Premium gift, must be shown the resulting future composition rather than being silently downgraded/upgraded.

### Fixed-calendar sponsored offer

A governed sponsor offer may intentionally cover a fixed calendar window. Such an offer may overlap existing coverage without extending beyond the fixed end date, but only when this behavior is explicit in the offer.

### Entitlements

Effective access may be sustained by one or more valid sources, but provenance stays separate. Ending one source must not revoke another valid source.

### Store Blueprint findings

Store's EntitlementGrant identity is source-aware and supports validity windows, which is a strong reusable primitive.

However, current Store entitlement source kinds are subscription-only. The current branch does not prove gift/sponsor provenance, future-dated activation, overlap evaluation, no-double-billing, sponsorship fallback or exact overlap redemption behavior.

---

## Second-pass Candidate 11 — Add-on purchase/cancel while Basic remains active

### Status

- **Coverage assessment:** MATERIAL EXTENSION OF `CER-PT-011`
- **NewYou semantic verdict:** BLOCKED / STOP — PRODUCT AUTHORITY GAP
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** `CER-UPD-010` — ACCEPTED PRE-JIT / NOT YET GOVERNED PRODUCT LAW
- **Cross-stream dependency:** Candidate 12 for gift/sponsor overlap; Candidate 15 for broader overlapping entitlement sources
- **Provider gate:** `OQ-004` for exact proration/co-billing execution only
- **Disposition:** MATERIAL EXTENSION OF `CER-PT-011` — NO NEW CER-PT

### Accepted model

`Basic + aligned add-ons = one recurring membership composition`.

Ordinary add-ons inherit Basic cadence and renewal boundary by default. Mid-period addition is success-gated on any required incremental/prorated adjustment. Removal is renewal-effective by default and preserves already-paid access through the current paid period. Removing one add-on does not cancel Basic or unrelated components. Cancelling Basic ends dependent ordinary add-ons at the governing paid-period boundary.

Premium remains Basic plus named add-on components, with source→target deltas and no duplicate billing obligations. Independently billed add-ons require explicit Product authority.

### Store Blueprint finding

Store's `SubscriptionItem` is an immutable paid-order snapshot rather than a proved authoritative current add-on lifecycle. NewYou therefore requires explicit component-composition adaptation/hardening.

---

## Second-pass Candidate 10 — Multiple changes before the renewal boundary

### Status

- **Coverage assessment:** MATERIAL EXTENSION OF `CER-PT-008`
- **NewYou semantic verdict:** BLOCKED / STOP — EXISTING ACCEPTED UPSTREAM DELTAS ONLY; NO NEW GAP
- **Store Blueprint verdict:** CHANGES REQUIRED / ADAPTATION REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** NONE NEW; existing `CER-UPD-005/006` and where relevant `CER-UPD-007/008` are sufficient
- **Cross-stream dependency:** Candidate 11 for detailed add-on lifecycle
- **Provider gate:** no new semantic gate; `OQ-004` remains execution validation only
- **Disposition:** MATERIAL EXTENSION OF `CER-PT-008` — NO NEW CER-PT REQUIRED
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`

### Accepted refinement

A membership has at most one authoritative future renewal outcome for each not-yet-committed boundary.

Multiple future-facing actions do not remain as independent latent authorities. They resolve as ordered future-contract versions.

A dimension-specific action transforms the current future target while preserving other still-valid dimensions.

Examples:

`Premium monthly → downgrade Basic → change cadence annual`
becomes
`Basic annual`

whereas:

`Premium monthly → downgrade Basic → cancel`
becomes
`do not renew`

and under accepted `CER-UPD-006`:

`do not renew → rescind cancellation`
becomes
`renew unchanged = Premium monthly`

not
`silently restore Basic monthly`.

A later cadence-only change after that rescission may then produce:

`Premium annual`.

### Cancellation supersession rule

Cancellation is not merely a boolean layered over still-live hidden package/cadence targets.

Once cancellation becomes authoritative for the boundary, earlier pending renewal targets become historical superseded intent.

Rescission therefore restores ordinary renewal of the current still-live membership rather than reviving hidden prior targets.

### Partial versus broad target changes

A cadence-only instruction changes cadence while preserving other still-valid target dimensions.

A package-only instruction changes package while preserving other still-valid target dimensions.

A broader explicit target selection may intentionally replace multiple dimensions at once.

Supersession therefore follows semantic scope, not timestamp alone.

### Boundary commitment

Once the renewal becomes commercially committed, later actions cannot rewrite it.

They target the next not-yet-committed boundary.

### Concurrent/stale instructions

Concurrent customer actions require one Commerce-owned ordering.

A stale instruction based on an older future-contract version must not overwrite a newer authoritative future target.

Exact version/CAS/transaction representation remains JIT work.

### Price/promotion composition

Where price migration or recurring promotion also participates, the final future target must resolve one coherent package/cadence/price/promotion contract before commitment.

Mutable current configuration is not authority.

### Store Blueprint findings

Store can preserve an already-pending variant while queueing a plan change and vice versa, which is a useful target-composition seam.

However, current evidence still relies on mutable pending plan/variant/amount/currency fields plus a separate cancellation flag.

That does not prove:

- immutable supersession history;
- stale-action detection;
- atomic ordering of concurrent future changes;
- cancellation superseding old pending targets;
- rescission without hidden target resurrection;
- renewal work bound to an exact expected future-contract version.

### Carry-forward principles

**One not-yet-committed renewal boundary has one current authoritative future commercial outcome.**

**Multiple future-facing instructions form an ordered supersession history, not competing latent authorities.**

**A dimension-specific change transforms only its semantic scope while preserving other still-valid future dimensions.**

**Period-end cancellation replaces the future renewal outcome with `do not renew` and makes prior pending targets historical.**

**Cancellation rescission restores `renew unchanged` from the current live contract and does not automatically resurrect pre-cancellation targets.**

**Committed renewal truth is immutable; later instructions target the next boundary.**

**Stale or concurrent instructions must not overwrite newer authoritative future-contract truth.**

---

## Second-pass Candidate 9 — Failed upgrade payment

### Status

- **Coverage assessment:** COVERED BY EXISTING PT
- **Relevant existing CER:** `CER-PT-003`, `CER-PT-007`, `CER-PT-008`, `CER-PT-015`
- **NewYou semantic verdict:** PASS
- **Store Blueprint verdict:** CHANGES REQUIRED
- **Reuse classification:** ADAPTATION REQUIRED / REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** NONE
- **Cross-stream dependency:** NONE
- **Provider gate:** `OQ-004`
- **Disposition:** COVERAGE CONFIRMED — NO NEW CER-PT REQUIRED
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`

### Coverage conclusion

Candidate 9 confirms that PT-003 + PT-007 already provide the correct failed-upgrade model.

The accepted invariant is:

`existing valid membership remains authoritative`
until
`required upgrade adjustment/payment becomes authoritative and the target contract remains currently applicable`

A requested upgrade is therefore a conditional commercial transition, not immediate authority to replace the current paid membership.

### Durable Commerce truths

Commerce distinguishes:

`current paid membership`
≠
`requested target membership`
≠
`upgrade adjustment`
≠
`provider attempt/evidence`

A failed or ambiguous upgrade payment does not invalidate the already-paid current membership.

### Durable Entitlements truth

While an upgrade adjustment remains failed or unresolved:

- existing membership rights remain valid;
- target/Premium-only rights remain unavailable;
- no downgrade/suspension occurs merely because the customer failed to buy more.

### Definitive upgrade-payment failure

If the incremental upgrade adjustment definitively fails, the existing membership remains unchanged and the upgrade does not complete.

### Ambiguous upgrade payment

If provider state is unresolved, the current membership remains authoritative and the upgrade remains pending/unresolved.

NewYou must reconcile the original adjustment identity rather than optimistically activating the target or inventing permanent failure.

### Late success

If previously failed/ambiguous provider evidence later proves successful, Commerce must first revalidate:

- upgrade instruction still authorised;
- membership still live;
- target package still applicable;
- pricing/proration basis still valid;
- no intervening renewal/change invalidated the old basis.

Only then may the target membership become authoritative.

If the old successful financial event can no longer lawfully satisfy the current target contract, it enters reconciliation/reversal/remedy rather than silently changing membership.

### Renewal races

If renewal becomes authoritative before a late upgrade success, the old proration basis cannot simply be reused.

The upgrade must be re-evaluated against the new current period/contract.

A stale old amount must not be reinterpreted as though it were a valid new-period adjustment.

### Period-end cancellation while upgrade remains unresolved

Period-end membership cancellation and current-period upgrade instruction are independent dimensions.

Scheduling cancellation does not automatically withdraw an already-authorised unresolved current-period upgrade.

If the upgrade later succeeds while the membership remains live and its authority is still valid, Premium may apply for the remaining current period while cancellation still ends the membership at period end.

### Explicit upgrade withdrawal

If the participant explicitly withdraws the unresolved upgrade before its commercial commitment boundary, the upgrade authority ends.

A later provider success remains financial truth but cannot activate the target membership; it requires reconciliation/reversal/remedy.

### Membership ends before late upgrade success

A late upgrade success after genuine membership termination cannot reactivate membership, create a new Premium period or attach itself to a later re-subscription.

It becomes financial-remedy truth only.

### Retry identity

Retries of the same still-valid upgrade adjustment remain attempts of one logical upgrade instruction.

They do not create multiple upgrades.

Before each retry, current contract and adjustment authority must be revalidated.

### Duplicate upgrade-charge success

If two adjustment attempts both genuinely succeed:

`one upgrade`
+
`one required adjustment`
+
`one excess collection remedy`

No second upgrade or future membership credit is created.

### Store Blueprint findings

Store exposes current and pending plan/variant/renewal amount fields and queue-change actions. Those are useful seams for future-effective contract changes.

The current inspected flow does not prove NewYou's required success-gated immediate current-period upgrade/proration path.

Existing PT-007 concerns therefore remain:

- mutable pending target state;
- stale target/proration basis;
- lack of explicit current-period upgrade-adjustment identity;
- need for success-gated target activation;
- need for failed/ambiguous/late-success reconciliation;
- no target entitlement before authoritative adjustment.

### Carry-forward principles

**A requested immediate upgrade is a conditional commercial transition, not immediate replacement of the current paid membership.**

**Failed or ambiguous upgrade adjustment never revokes existing paid membership rights.**

**Target/Premium rights begin only after the required adjustment becomes authoritative and current Commerce truth still supports the target.**

**Late upgrade success must revalidate current instruction, membership state and pricing/proration basis before changing membership.**

**A stale or no-longer-authorized successful adjustment becomes reconciliation/remedy truth rather than membership authority.**

**Membership cancellation and unresolved current-period upgrade instruction are independent future/current commercial dimensions unless Product explicitly couples them.**

**Retries or duplicate provider success cannot multiply upgrade consequence.**

---

## Second-pass Candidate 8 — Payment method / reusable authorisation replacement during renewal

### Status

- **Coverage assessment:** COVERED BY EXISTING PT
- **Relevant existing CER:** `CER-PT-003`, `CER-PT-004`, `CER-PT-006`, `CER-PT-015`; `CER-UPD-009` reinforces excess-collection remedy but is not the originating semantic
- **NewYou semantic verdict:** PASS
- **Store Blueprint verdict:** CHANGES REQUIRED
- **Reuse classification:** REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** NONE
- **Cross-stream dependency:** NONE
- **Provider gate:** `OQ-004`
- **Disposition:** COVERAGE CONFIRMED — NO NEW CER-PT REQUIRED
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`

### Coverage conclusion

Changing payment method does not create a new renewal occurrence.

The accepted invariant is:

`one logical renewal occurrence`
→
`potentially multiple instrument-specific payment attempts`
→
`at most one successful collection consequence`
→
`one paid period`
→
`one entitlement consequence`

This is already established by PT-004 and strengthened by PT-003/PT-006/PT-015.

### Durable Commerce truths

Payment method/reusable authorisation is an execution dimension inside the renewal contract.

Commerce must distinguish:

`membership/renewal authority`
≠
`reusable payment authority`
≠
`payment attempt`
≠
`provider success evidence`

Changing the preferred/current instrument affects how a still-authorised renewal may be attempted; it does not create a new renewal key, paid period or membership.

### Durable Entitlements truth

Entitlements do not care which valid payment instrument paid the renewal.

They care only whether the logical renewal became authoritatively paid.

### Old attempt definitely failed

If the old-instrument attempt is authoritatively failed, a new-instrument attempt may execute for the same logical renewal.

If the new attempt succeeds, exactly one paid period is established.

### Old attempt still ambiguous

NewYou must not blindly start a second independently successful charge while the first can still settle.

Safe execution requires either:

- sufficient business/provider evidence that the old attempt can no longer succeed; or
- provider mechanics that make the old/new attempts mutually safe.

Exact execution remains `OQ-004`.

### Old attempt succeeds late after payment-method replacement

Changing the stored/default instrument is prospective.

If the old attempt was legitimately submitted while the old authority remained valid and later becomes authoritatively successful, that success satisfies the same renewal occurrence.

The replacement instrument then governs later safe attempts/future renewals.

### Both attempts succeed

If both old and new instrument attempts genuinely succeed:

`one renewal`
+
`two real financial collections`

must converge to:

`one governing successful collection`
+
`one duplicate/excess collection requiring source-scoped reversal/refund/remedy`

No second paid period or entitlement may be created.

### Revocation nuance

Explicitly revoking an old reusable payment authority prevents new future attempts under that authority once effective, but does not rewrite already-submitted attempt history.

Whether an already-submitted provider charge can still settle or can be neutralised is provider-specific and remains under `OQ-004`.

### Store Blueprint findings

Store's `RenewalAttempt` is a stable idempotency anchor on `(subscription_id, renewal_key)`.

Store's `PaymentIntent` separately carries provider/payment-method identity and purpose.

Store also has a dedicated payment-method update flow that can update the subscription billing reference and trigger retry for relevant past-due payment-method failures.

Those are strong reuse seams.

However, the existing PaymentIntent lifecycle still lacks failed→succeeded reconciliation, which remains a PT-003 hardening defect. That matters directly where an old instrument is locally marked failed but later provider evidence proves success.

Current evidence also does not prove old/new instrument attempts cannot both succeed for one renewal without explicit reconciliation/remediation.

### Carry-forward principles

**Payment-method replacement changes execution authority for the same logical renewal; it does not create a new renewal occurrence.**

**One renewal may have multiple payment attempts but at most one successful collection consequence and one paid period.**

**A later payment-method update does not retroactively invalidate a legitimately submitted earlier attempt unless governing authority/provider mechanics establish otherwise.**

**An unresolved old attempt must be reconciled or safely neutralised before NewYou knowingly risks another independent successful collection.**

**If two instrument-specific attempts both succeed, the second financial fact is excess collection/remedy truth, not another membership period.**

**Reusable payment authority and membership renewal authority are separate truths.**

---

## Second-pass Candidate 4 — Re-subscribe after membership has genuinely ended

### Status

- **Coverage assessment:** COVERED BY EXISTING PT / EXISTING ACCEPTED DELTA
- **NewYou semantic verdict:** BLOCKED / STOP — EXISTING `CER-UPD-006`; NO NEW PRODUCT GAP
- **Store Blueprint verdict:** PASS for the narrow post-termination occurrence model
- **Reuse classification:** REUSE AFTER HARDENING
- **New working doctrine:** NONE
- **Upstream delta:** NONE NEW; existing `CER-UPD-006` is sufficient
- **Cross-stream dependency:** Candidate 13 for Premium continuity/reassessment only
- **Provider gate:** `OQ-004` only for provider-side reusable-authorisation mechanics
- **Disposition:** COVERAGE CONFIRMED — NO NEW CER-PT REQUIRED
- **NewYou evidence baseline:** `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store evidence baseline:** `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3`; `hardening/subscriptions` at `575ffa1848ac69abe855bd018c7ae8eaf05d61e4`
- **Store baseline movement:** PR #11 merged into `hardening/subscriptions`; the merge promoted governance/hardening-loop material and did not change the inspected subscription source/runtime implementation. Prior code conclusions remain applicable, but the evidence SHA advances.

### Coverage conclusion

Candidate 4 pressure-tests the post-termination half of the boundary established by `CER-UPD-006`:

`before actual termination → cancellation rescission on the same live membership`

versus

`after actual termination → new re-subscription journey`

No additional Product/commercial rule is required beyond that accepted boundary.

### Durable Commerce truth

Once a membership has genuinely terminated, a later purchase is a **new commercial membership occurrence**.

The earlier occurrence remains immutable historical truth:

`old membership occurrence A → ended`

A later authoritative purchase creates:

`new membership occurrence B → current`

The same participant/account may be associated with both, but same customer identity does not make them the same commercial occurrence.

The old occurrence must not be reopened merely because the customer returns.

### Durable Entitlements truth

Membership-derived rights sourced from the ended occurrence stop according to Product authority.

Historical/once-off rights that Product Law preserves after cancellation remain historically true.

A later membership purchase produces a new current entitlement source/provenance.

Therefore:

`old membership source A → historical/ended`

and

`new membership source B → current/active`

must remain distinct for later cancellation, refund, dispute, chargeback and provenance reasoning.

### Fresh intent and payment authority

Re-subscription requires fresh current customer commercial intent.

A still-valid reusable payment credential or provider authorisation may potentially be used as the payment mechanism, subject to `OQ-004`, but it is not itself authority to restart membership.

Required ordering remains:

`fresh purchase intent → current valid offer/contract → valid payment authority → verified payment → new membership occurrence`

Provider-side reusable authorisation must never silently recreate a terminated membership.

### Stale old evidence after the new membership starts

If provider evidence relating to the old terminated occurrence arrives after the new membership has begun, it must reconcile against the old occurrence identity.

It must not:

- reactivate the old membership;
- extend the new membership;
- rewrite the new package/cadence;
- become current entitlement authority merely because the participant or provider customer reference is the same.

Existing PT-005/PT-015 reversal/remedy and recovery doctrine remains authoritative.

### Pricing, promotion and continuity boundaries

Candidate 4 does not decide:

- whether a returning customer receives a historical/grandfathered price — Candidate 5;
- whether an old promotion may be reused — Candidate 6;
- whether a gap resets or preserves a continuity-derived Premium right — Candidate 13.

It establishes only that those later rules, if any, must operate over distinct historical and current commercial occurrences rather than mutating the old membership back into the current one.

### Store Blueprint findings

At the refreshed Store subscription evidence head, `canceled` and `expired` remain terminal in the inspected Subscription state machine; there is no canceled/expired→active transition.

Store's paid-order subscription creation is idempotent around the **source order-line identity**. A genuinely new paid order therefore creates a new subscription occurrence rather than finding and reactivating an old canceled/expired subscription.

That is a strong fit for NewYou's Candidate 4 invariant.

This narrow result does not certify the whole Store subscription engine as safe-as-is. Existing PT-003/PT-005/PT-007/PT-008/PT-015 hardening gaps remain, and Candidates 7/15 still need to test unintended concurrent active membership sources.

### Carry-forward principles

**Actual membership termination is a hard commercial-history boundary.**

**A later re-subscription creates a new commercial occurrence; it does not reopen the old terminated occurrence.**

**Same participant/account identity does not collapse distinct membership occurrences.**

**Late provider evidence remains bound to the commercial occurrence it concerns and may not mutate a later re-subscription.**

**Fresh purchase intent is required to create a new membership; stored/reusable provider payment authority is not itself re-subscription intent.**

**Historical retained rights and new current membership rights may coexist with distinct source provenance.**

---

---

# 13. Version history

## v0.30.3 — 2026-09-10

- Current-routing / certification-chain hygiene PATCH over `v0.30.2`; no Commerce, Entitlements, Product, Store, provider, PT, UPD or cross-stream semantic conclusion changed.
- Updated the current header/protocol to record that renewed semantic stabilisation audit `v0.2.0` already passed against exact `v0.30.1`.
- Recorded `v0.30.2` as the prior four-reference hygiene PATCH and `v0.30.3` as current-routing/protocol hygiene only.
- Replaced stale current-state routing that incorrectly said renewed semantic audit remained the next step.
- Updated eventual-handoff routing so exact `v0.30.3` must first receive narrow mechanical recertification, then final compact recompression and source↔compact verification.
- Preserved all historical changelog entries unchanged.
- No governed NewYou or Store repository mutation performed.


## v0.30.2 — 2026-09-10

- Exact-byte hygiene PATCH over `v0.30.1`; no semantic discovery, PT, UPD, provider, Store or cross-stream conclusion changed.
- Replaced four stale prospective second-pass references inside substantive material with retrospective references to completed Candidates 8, 10 and 13.
- Preserved all historical changelog statements, evidence SHAs, PT/UPD identifiers, accepted recommendations and authority classifications.
- Requires mechanical recertification because `v0.30.1` exact-byte certification does not automatically carry forward under the audit anti-drift rule.
- No governed NewYou or Store repository mutation performed.


## v0.30.1 — 2026-09-10

- Non-semantic stabilisation-preparation PATCH over accepted `v0.30.0` discovery; no third broad pressure-test round opened.
- Corrected protocol and handoff checklist to record second-pass Candidates 1–15 as complete.
- Updated current Store header baseline to `54871ef3bdda42f067ed5dbd398305151610c060` while preserving historical inspected SHAs.
- Replaced stale four-delta summary with a complete current index of `CER-UPD-001...013` plus later-governance clustering guidance.
- Rebuilt the pressure-test register through `CER-PT-020` with original-vs-later-refinement verdicts.
- Corrected PT-006 metadata; corrected PT-008 layered verdict metadata; added later-delta cross-references to PT-011/PT-012/PT-020.
- Added navigational H1 `# 12A. Accepted pressure-test evidence — continuation` before PT-005.
- Clarified that late verified success for the same renewal occurrence retains the original scheduled renewal period/boundary; no `CER-UPD-014` created.
- Reclassified remaining provider-reversal/proration seams as conditional downstream questions, not a third broad CER cycle.
- Normalised prospective second-pass cross-references in earlier sections into retrospective links now that Candidates 1–15 are complete; historical conclusions and original evidence SHAs remain unchanged.
- Normalised the Store-ledger and Section-10 navigation labels to post-closure current-state wording.
- Compact v0.1.1 remains provisional pending renewed stabilisation/completeness audit and final recompression.
- No governed NewYou or Store repository mutation performed.


## v0.30.0 — 2026-09-10

- Accepted second-pass Candidate 15 as a **material refinement of `CER-PT-011`, `CER-PT-012`, and `CER-PT-020`**, with no new PT.
- Added accepted `CER-UPD-013 — Multi-source entitlement overlap and grant commercial effect`.
- Accepted independent provenance for multiple simultaneous paid/gift/sponsored/complimentary/lifetime sources.
- Accepted union semantics for boolean/scoped access without synthetic membership-tier rewriting.
- Distinguished access-overlay grants from qualifying membership-coverage grants.
- Accepted suppression of redundant future self-paid collection only where a governed membership-coverage grant explicitly covers the same composition/interval.
- Accepted component-scoped effect for partial grants.
- Accepted non-multiplication of ordinary recurring limited benefits, Premium continuity clocks and nonaccumulating entitlements merely because equivalent sources overlap.
- Accepted explicit additive Product/grant authority as the only basis for additional consumable units.
- Accepted exactly-once, auditable source/occurrence consumption semantics.
- Rejected a global source-priority hierarchy.
- Recorded Store verdict: **CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING**; reusable source-aware grant/union-access primitives remain, but source taxonomy and limited-benefit semantics need adaptation.
- Confirmed NewYou-specific Premium/review policy must remain outside the generic Store package.
- Planned second-pass Candidates 1–15 are COMPLETE.
- Compact CER v0.1.1 remains provisional pending renewed stabilisation/completeness audit and final recompression.
- No governed NewYou or Store repository mutation performed.

## v0.29.0 — 2026-09-10

- Accepted second-pass Candidate 14 as a **material refinement of `CER-PT-001`, `CER-PT-011`, and `CER-PT-015`**, with no new PT.
- Accepted one latest authoritative entitlement target set/version per commercial membership/add-on source.
- Rejected correctness models that depend only on grant-before-revoke or revoke-before-grant ordering.
- Accepted safe incomplete-transition semantics: no rights outside the new target and preservation of rights common to old and new sets.
- Accepted continuous preservation of unchanged component rights across upgrades, downgrades and component swaps.
- Accepted source-specific, idempotent, stale-resistant target convergence under crash, retry, backlog and reordering.
- Accepted recovery from current durable target authority rather than replay of presumed worker history.
- Preserved unrelated entitlement-source provenance during membership-source changes.
- Preserved cache/projection non-authority and rejected importing Store's Cachex layer into NewYou without evidence-backed correctness need.
- Recorded Store verdict: **CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING**.
- No new upstream delta, working doctrine, Domain or Resource created.
- Compact CER v0.1.1 remains provisional pending Candidate 15, renewed stabilisation/completeness audit and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.28.0 — 2026-09-10

- Accepted second-pass Candidate 13 as **NEW SEMANTIC CLASS → `CER-PT-020`**.
- Added accepted `CER-UPD-012 — Premium reassessment continuity, maturity and nonaccumulation`.
- Defined twelve continuous Premium months as uninterrupted authoritative qualifying Premium coverage time for the canonical grantee.
- Accepted cadence/price/promotion/payment-method changes and seamless qualifying self-pay↔gift↔sponsor source hand-offs as continuity-preserving when no Premium gap exists.
- Accepted overlapping qualifying Premium sources as non-accelerating; elapsed time counts once.
- Clarified annual renewal as the annual-billing expression of the same anniversary maturity rule; initial annual purchase and cadence switch into annual do not trigger the benefit.
- Accepted grace as provisional for tenure until Commerce proves the new paid Premium period.
- Accepted Premium→Basic downgrade, qualifying Premium termination and genuine uncovered Premium interval as continuity-breaking.
- Accepted expiry of unused reassessment when qualifying Premium ends even if Basic continues.
- Defined nonaccumulation as at most one unused entitlement, with no hidden/catch-up issuance at missed anniversaries.
- Updated Store evidence baseline to `54871ef3bdda42f067ed5dbd398305151610c060`; PR #12 is governance-only, so prior runtime findings remain materially applicable.
- Classified this 12-month benefit as NewYou-specific Product logic that must not be embedded in the generic Store package.
- Compact CER v0.1.1 remains provisional pending Candidates 14–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.27.0 — 2026-09-10

- Accepted Candidate 12 as a material refinement of `CER-PT-012`, with no new PT.
- Added accepted `CER-UPD-011 — Gift/sponsored membership overlap with existing membership`.
- Accepted source-specific gift/sponsor provenance without rewriting existing membership history.
- Accepted overlap-safe duration handling, next-uncovered-boundary activation by default, and no overlapping self-paid collection for equivalent gift/sponsor-funded periods.
- Accepted clear authority for self-paid resumption after fixed-duration gift coverage and no automatic personal-billing restart after uncertain/open-ended sponsorship without explicit fallback consent.
- Preserved already-funded recipient periods when sponsors stop future funding.
- Preserved existing self-paid cancellation rather than treating gift/sponsor application as cancellation rescission.
- Accepted explicit bounded behavior for fixed-calendar sponsored offers and explicit disclosure for composition mismatch.
- Store remains **CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING**.
- Compact CER v0.1.1 remains provisional pending Candidates 13–15, renewed stabilisation and recompression.
- No governed repository mutation performed.

## v0.26.0 — 2026-09-10

- Accepted Candidate 11 as a material refinement of `CER-PT-011`, with no new PT.
- Added accepted `CER-UPD-010 — Ordinary membership add-on recurring lifecycle`.
- Accepted the default one-composition model: Basic plus aligned ordinary add-ons within one recurring membership relationship.
- Accepted inherited Basic cadence/renewal boundary by default, success-gated mid-period addition, renewal-effective removal, dependent termination with Basic, provenance-aware Entitlements and Premium source→target component deltas.
- Classified independently billed add-ons as explicit Product exceptions.
- Store remains **CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING**.
- Compact CER v0.1.1 remains provisional pending Candidates 12–15, renewed stabilisation and recompression.
- No governed repository mutation performed.

## v0.25.0 — 2026-09-10

- Accepted second-pass Candidate 10 as a **material refinement of `CER-PT-008`**, with no new PT.
- Accepted one authoritative future renewal outcome per not-yet-committed boundary.
- Rejected both whole-contract naïve last-write-wins and indefinitely independent latent pending flags.
- Accepted semantic-scope transformation: dimension-specific changes preserve other still-valid future dimensions; broader explicit targets supersede the dimensions they define.
- Accepted period-end cancellation as a full `do not renew` future instruction that makes earlier pending targets historical rather than latent.
- Preserved `CER-UPD-006`: rescission returns to `renew unchanged` from the current live contract and does not automatically resurrect pre-cancellation downgrade/cadence/price/promotion targets.
- Accepted immutable boundary commitment and one Commerce-owned ordering for concurrent/stale instructions.
- Preserved `CER-UPD-005/007/008` as applicable existing deltas for cadence, price and recurring promotion composition.
- Recorded Store verdict: **CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING**; target-composition seams are useful but mutable pending fields plus separate cancellation state do not yet prove authoritative supersession/concurrency semantics.
- No new upstream delta, working doctrine, Domain or Resource created.
- Compact CER v0.1.1 remains provisional pending Candidates 11–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.24.0 — 2026-09-10

- Accepted second-pass Candidate 9 as **COVERAGE CONFIRMED — NO NEW CER-PT REQUIRED**.
- Confirmed that failed/ambiguous immediate-upgrade payment is already governed by PT-003/PT-007/PT-008/PT-015.
- Preserved the current paid membership as authoritative until the required upgrade adjustment becomes authoritative and remains commercially applicable.
- Accepted that failed or ambiguous upgrade payment does not revoke or suspend already-purchased membership rights.
- Accepted that target/Premium rights must not be granted before authoritative adjustment success.
- Accepted stale-basis revalidation for late success, including membership state, target contract, price/proration basis and intervening renewal/change.
- Preserved the distinction between period-end cancellation and current-period upgrade instruction; one does not automatically cancel the other.
- Accepted explicit upgrade withdrawal as a separate authority change, with later stale financial success going to reconciliation/reversal/remedy rather than target activation.
- Accepted one logical upgrade consequence across retries/duplicate provider success.
- Store verdict remains **CHANGES REQUIRED / ADAPTATION REQUIRED / REUSE AFTER HARDENING**; current/pending fields are reusable seams but success-gated immediate-upgrade semantics are not proven.
- No new upstream delta, working doctrine, Domain or Resource created.
- Compact CER v0.1.1 remains provisional pending Candidates 10–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.23.0 — 2026-09-10

- Accepted second-pass Candidate 8 as **COVERAGE CONFIRMED — NO NEW CER-PT REQUIRED**.
- Confirmed that payment-method/reusable-authorisation replacement is already governed by PT-003/PT-004/PT-006/PT-015.
- Preserved one renewal occurrence across old/new instrument attempts and prohibited duplicate paid-period/entitlement consequence.
- Accepted that changing the stored/default payment method is prospective and does not automatically invalidate an already-submitted valid attempt.
- Accepted that an unresolved old attempt must be reconciled or safely neutralised before knowingly risking another independent successful collection.
- Accepted source-scoped reversal/refund/remedy if two instrument-specific attempts both genuinely succeed for one renewal.
- Preserved separation between reusable payment authority and membership renewal authority.
- Recorded `OQ-004` provider-validation obligations for authorization update, already-submitted attempt behavior, safe retry and neutralisation/cancellation capability.
- Store verdict remains **CHANGES REQUIRED / REUSE AFTER HARDENING**; stable RenewalAttempt identity and payment-method update flow are strong reuse seams, while failed→succeeded reconciliation and old/new double-success proof remain hardening requirements.
- No new upstream delta, working doctrine, Domain or Resource created.
- Compact CER v0.1.1 remains provisional pending Candidates 9–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.22.0 — 2026-09-10

- Accepted second-pass Candidate 7 as genuinely new `CER-PT-019 — Concurrent duplicate ordinary membership purchase`.
- Added accepted `CER-UPD-009 — Duplicate ordinary membership purchase and excess collection`.
- Distinguished one-occurrence provider replay (`CER-PT-002`) from two genuinely distinct purchase/payment attempts.
- Accepted at-most-one ordinary recurring membership relationship for the same canonical grantee/commercial relationship.
- Accepted that two genuine successful payments remain real financial evidence but do not automatically create two memberships, two paid periods, two recurring obligations or duplicate entitlement.
- Accepted NewYou Commerce admission ordering as authority over callback/provider timing.
- Accepted full reversal/refund or governed make-whole handling for the non-admitted successful duplicate collection by default.
- Explicitly rejected accidental future-period stacking as the default remedy.
- Preserved Candidate 15 for legitimate overlapping gift/sponsored/complimentary/other entitlement sources.
- Recorded Store verdict: **CHANGES REQUIRED / REUSE AFTER HARDENING**; current pre-purchase guards are useful but concurrency-safe exclusion is not yet proven by inspected durable identities.
- Compact CER v0.1.1 remains provisional pending Candidates 8–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.21.0 — 2026-09-10

- Accepted second-pass Candidate 6 as genuinely new `CER-PT-018 — Recurring promotional pricing lifecycle`.
- Added accepted `CER-UPD-008 — Recurring promotional pricing lifecycle`.
- Accepted Commerce ownership, paid-period-count consumption semantics by default, no banked unused cycles, no automatic re-subscription inheritance/reset, immutability against public promotion mutation, explicit package/cadence scope, and separation from `CER-UPD-007` base-price migration.
- Store verdict remains **CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED**: deterministic Pricing primitives are reusable, recurring promotion lifecycle semantics are not yet proven.
- Compact CER v0.1.1 remains provisional pending Candidates 7–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.20.0 — 2026-09-09

- Accepted second-pass Candidate 5 as genuinely new `CER-PT-017 — Existing-member recurring price/version migration`.
- Recorded NewYou verdict: **BLOCKED / STOP — PRODUCT AUTHORITY GAP**.
- Added accepted `CER-UPD-007 — Existing-member recurring price migration` as working/non-authoritative upstream Product/commercial direction.
- Accepted that public/list price changes do not rewrite an existing member's current paid period or already-committed renewal.
- Accepted explicit future-boundary price migration with durable target price/currency/effective boundary and required notice/consent/legal eligibility before a higher-price renewal.
- Accepted fail-closed behavior against a higher amount when transition conditions are incomplete for that renewal occurrence.
- Accepted that grandfathering/price locking must be a deliberate commercial promise attached to a qualifying membership occurrence/offer, not an accidental historical-list-price property.
- Preserved Candidate 4's rule that post-termination re-subscription does not inherit an old price solely because the same participant held it previously.
- Preserved Candidate 6 as the owner of promotional/discount lifecycle and Candidate 13 as the owner of continuity-derived rights.
- Added an explicit **South African consumer-protection/legal expert gate** before final Product authority freezes monthly/annual price-change and renewal mechanics; CER does not invent the final legal answer.
- Recorded Store verdict: **CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED**; subscription-level renewal snapshots are useful, but mutable plan pricing cannot become NewYou authority.
- Compact CER v0.1.1 remains provisional pending Candidates 6–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.19.0 — 2026-09-09

- Accepted second-pass Candidate 4 as **COVERAGE CONFIRMED — NO NEW CER-PT REQUIRED**.
- Confirmed that the post-termination re-subscription case is already resolved by the termination boundary in accepted `CER-UPD-006` plus existing PT-005/PT-008/PT-015 doctrine.
- Recorded the durable rule that a genuinely terminated membership remains historical truth and a later successful re-subscription creates a new commercial occurrence rather than reactivating the old one.
- Preserved distinct old/new entitlement provenance and required stale provider evidence to remain bound to the old occurrence it concerns.
- Preserved the distinction between fresh customer re-subscription intent and reusable provider payment authority.
- Deferred historical/grandfathered price treatment to Candidate 5, promotion reuse to Candidate 6 and Premium continuity consequences to Candidate 13.
- Refreshed Store `hardening/subscriptions` evidence baseline from `77a272c3887a7ab46e84a7fed02163d964e37b9b` to `575ffa1848ac69abe855bd018c7ae8eaf05d61e4` after PR #11 merged governance/hardening-loop material.
- Verified that the Store merge did not change the inspected subscription source/runtime implementation; prior code conclusions remain applicable at the new branch evidence SHA.
- Recorded narrow Store Candidate 4 verdict: **PASS for post-termination occurrence model / REUSE AFTER HARDENING**.
- No new upstream delta, working doctrine, Domain or Resource created.
- Compact CER v0.1.1 remains provisional pending Candidates 5–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.18.0 — 2026-09-09

- Accepted second-pass Candidate 3 as a **MATERIAL EXTENSION** of existing `CER-PT-008`; no new PT created.
- Added accepted `CER-UPD-006 — Rescission of pending membership cancellation` as working/non-authoritative upstream Product/commercial direction.
- Refined PT-008 to distinguish period-end cancellation as a revocable future non-renewal instruction from actual membership termination.
- Accepted that an authenticated participant may rescind a pending period-end cancellation before termination and restore `renew unchanged` as the current future instruction.
- Preserved the same membership relationship, current paid period and entitlement continuity across valid pre-termination rescission.
- Preserved historical cancellation/rescission intent while making only the current future instruction authoritative for renewal.
- Explicitly prohibited retroactive authorization of a late charge by a later keep-membership instruction.
- Preserved separation between membership renewal intent and reusable payment authority.
- Preserved Candidate 4 as the owner of post-termination re-subscription and Candidate 10 as the owner of generalized multiple-future-instruction supersession.
- Refined Store evidence: inspected Store path exposes period-end cancellation and suppression but no governed undo/resume action; Store remains **CHANGES REQUIRED / ADAPTATION REQUIRED**.
- Compact CER v0.1.1 remains provisional pending Candidates 4–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.17.0 — 2026-09-09

- Accepted second-pass Candidate 2 as a **MATERIAL EXTENSION** of existing `CER-PT-016`; no new PT created.
- Broadened `CER-PT-016` from monthly→annual to **monthly↔annual billing cadence transition**.
- Refined accepted `CER-UPD-005` into a bidirectional default: preserve the current paid period in either direction and apply the new cadence at the next not-yet-committed renewal boundary.
- Explicitly rejected automatic classification of cadence direction as `DEC-046` upgrade/downgrade.
- Explicitly rejected overlapping monthly billing during an already-paid annual period absent a separately governed early-termination/refund/credit rule.
- Preserved one authoritative membership relationship and unchanged entitlement continuity across same-composition cadence change.
- Preserved Candidate 5 as the owner of target price/version migration and Candidate 13 as the owner of Premium continuity/reassessment-trigger semantics.
- Preserved PT-008 cancellation/supersession and PT-005/PT-006 failed-renewal behavior for the new target-cadence renewal occurrence.
- Store verdict unchanged: **CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED**.
- Compact CER v0.1.1 remains provisional pending Candidates 3–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.16.0 — 2026-09-09

- Reopened CER once and narrowly for the authorised 15-scenario second-pass closure grill; the scenario count is not a quota of new PT identifiers.
- Accepted second-pass Candidate 1 as genuinely new `CER-PT-016 — Monthly → annual billing cadence transition`.
- Recorded NewYou verdict: **BLOCKED / STOP — PRODUCT AUTHORITY GAP**.
- Created and accepted `CER-UPD-005 — Membership billing-cadence transition` as working/non-authoritative upstream Product/commercial direction.
- Accepted the default monthly→annual rule: preserve the current paid monthly period and apply annual cadence at the next not-yet-committed renewal boundary.
- Preserved one authoritative membership relationship and unchanged entitlement continuity across same-composition cadence change.
- Preserved the PT-008/PT-015 rule that queue/provider timing is not contract authority and that one Commerce-owned ordering governs cadence instruction versus renewal commitment.
- Preserved Candidate 5 as the owner of target price/version migration and Candidate 13 as the owner of Premium continuity/reassessment implications.
- Recorded Store verdict: **CHANGES REQUIRED / REUSE AFTER HARDENING / ADAPTATION REQUIRED**; cadence-aware plan/change mechanisms are useful, but immutable priced/charged renewal-contract hardening remains required.
- Rechecked NewYou `main` at `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`.
- Rechecked Store `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3` and `hardening/subscriptions` at `77a272c3887a7ab46e84a7fed02163d964e37b9b`.
- Noted draft Store PR #11 as in-progress governance evidence reporting no source/runtime change; prior Store implementation conclusions remain applicable to the unchanged branch head.
- Marked compact CER v0.1.1 as provisional pending completion of Candidates 2–15, renewed stabilisation and recompression.
- No governed NewYou or Store repository mutation performed.

## v0.15.2 — 2026-09-09

- Applied the accepted full-double-check packaging corrections; no accepted PT, `CER-UPD`, HSP/Privacy seam or Store reuse conclusion changed meaning.
- Updated deep-source routing to record that broad discovery, stabilisation and compact compression are complete.
- Declared compact CER v0.1.1 as the normal default context and retained this detailed artifact as deep evidence.
- Preserved audited NewYou and Store evidence baselines.
- Recorded that compact v0.1.0 was semantically sound but failed final packaging certification because the Evidence Index retained unresolved Store SHA placeholders.
- No new pressure test, upstream delta, Product rule, Domain, Resource or implementation authority was created.
- No governed NewYou repository mutation was performed.

## v0.15.1 — 2026-09-09

- Applied the accepted stabilisation/completeness audit corrections `C-01...C-08`; no accepted PT, CER-UPD or Store reuse conclusion changed meaning.
- Refreshed the current audited NewYou baseline to `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614` and current Open Work to `v1.2.40`; Product, Decision, Architecture, Domain and Roadmap authority relevant to CER remained unchanged.
- Added the missing PT-014 Store reuse-ledger row.
- Added PT-014 carry-forward principles to the consolidated anti-drift list and mechanically renumbered the list.
- Added exact gift/sponsorship authority anchors `DEC-044`, `DEC-285` and the relevant `00_PLATFORM_v1.3.0 §21A.9` details used by PT-012.
- Replaced prose-only HSP cross-seams with exact `HSP-UPD-001`, `005`, `006`, `007`, `008` routing.
- Added the Privacy `PRIV-WD-002` / `PRIV-UPD-002` cross-stream preservation note.
- Clarified `DEC-049` manual EFT versus Paystack's provider-mediated South African EFT/Ozow channel.
- Recorded the stale accidental CER v0.1.0 repository routing as explicit later-handoff cleanup rather than mutating the repository during stabilisation.
- Broad discovery remains closed at PT-015; compression is the next default activity.
- No governed NewYou repository mutation performed for this patch.

## v0.15.0 — 2026-09-09

- Accepted `CER-PT-015`.
- Recorded NewYou semantic verdict: **PASS**.
- Recorded Store Blueprint verdict: **CHANGES REQUIRED / REUSE AFTER HARDENING — STRONG RECOVERY CORE**.
- Created no new CER upstream delta.
- Refreshed the NewYou evidence baseline to `764010e8d3896f4430cc56b59997b9cbf85cec6c`; the intervening commit added Privacy Evidence Pre-JIT documentation and did not amend the routed CER Product/Architecture/Domain/Roadmap authority inspected for this test.
- Preserved Store `main` at `56f06d028ec38896f5a927f54dc7adfcb20034a3` and `hardening/subscriptions` at `77a272c3887a7ab46e84a7fed02163d964e37b9b` as the inspected Store evidence baseline.
- Accepted the distinction that recovery is a business capability rather than merely finite worker/provider retry.
- Required stable logical commercial identity and current-authority reconciliation across restart, queue loss, webhook exhaustion and reordered evidence.
- Required independently repairable Commerce→Entitlements convergence or an explicit durable unresolved/exception state; finite retry exhaustion may not silently terminate the obligation.
- Required recovered stale evidence to revalidate current Commerce authority before recreating access, including previously accepted cancellation/refund/dispute/revocation rules.
- Recorded Store's webhook evidence, paid-renewal reconciliation, paid-order ensure workers and pending-provider-setup recovery as a strong reusable recovery core.
- Recorded terminal-convergence hardening needs around lost post-commit enqueue, finite worker exhaustion and `CER-PT-003` late failed→success reconciliation.
- Verified current official Paystack webhook retry and transaction-verification evidence; exact provider semantics remain under `OQ-004`.
- Marked the broad CER pressure-test sequence complete through `CER-PT-015`; stabilisation/completeness audit and later compression are next by default rather than `CER-PT-016`.
- No governed NewYou repository mutation performed for this version.

## v0.14.0 — 2026-09-09

- Accepted `CER-PT-014`.
- Recorded NewYou verdict: **BLOCKED / STOP — EXISTING `HSP-UPD-001`**.
- Recorded Store Blueprint verdict: **ADAPTATION REQUIRED — GENERIC GRANT MECHANICS ONLY**.
- Created no new CER upstream delta; preserved `HSP-UPD-001` as the single upstream identity for admitted membership-derived Plan/review work that crosses ordinary entitlement expiry.
- Strengthened the bounded-completion recommendation: ordinary expiry may block new exercise without retroactively invalidating an already-authoritatively admitted exact Request.
- Added the admission-vs-expiry authoritative ordering invariant.
- Clarified that queue insertion is execution infrastructure, not entitlement admission.
- Clarified that bounded completion is neither membership extension nor a banked reusable credit.
- Preserved separate treatment for refund, dispute, chargeback, Safety invalidation, withdrawal and other HSP seams.
- Recorded Store grant expiry/revocation/idempotent issuance as reusable mechanics while rejecting generic active/expired status as sufficient for NewYou in-flight Plan/review semantics.
- Advanced `CER-PT-015` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.13.0 — 2026-09-09

- Accepted `CER-PT-013`.
- Recorded NewYou verdict: **BLOCKED / STOP — PRODUCT AUTHORITY GAP**.
- Created and accepted `CER-UPD-004 — Manual-EFT paid-period commencement`.
- Preserved `DEC-049` semantics that manual EFT grants access only after verification and creates no automatic renewal authority.
- Clarified that absence of another EFT is not a failed automatic renewal and must not fabricate the `DEC-043` provider retry lifecycle.
- Established fail-closed treatment for unmatched bank evidence and apply-once treatment for duplicate verification/reconciliation.
- Clarified that underpayment, overpayment, duplicate deposits and late money movement do not independently define entitlement.
- Accepted verification/activation as the ordinary on-demand membership paid-period start, with an exception only for offers explicitly sold against fixed/scheduled service periods.
- Required fresh explicit payer authority when moving from manual EFT to a recurring payment method.
- Recorded Store's generic payment/application/idempotency spine as reusable while its provider-oriented PaymentIntent path is not a manual-EFT workflow as-is.
- Backfilled the Store reuse ledger and standing principles with accepted PT-012 gift/sponsorship conclusions that were recorded in v0.12.0 but not yet duplicated into those navigation sections.
- Advanced `CER-PT-014` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.12.0 — 2026-09-09

- Accepted `CER-PT-012`.
- Recorded NewYou verdict: **BLOCKED / STOP — PRODUCT AUTHORITY GAP**.
- Created and accepted `CER-UPD-003 — Redemption transfer, post-redemption control and recurring sponsorship authority`.
- Preserved locked purchaser/recipient/participant/account-holder separation and sponsor privacy boundaries.
- Established redemption as a durable exactly-once transfer boundary rather than a cosmetic code-status update.
- Clarified that unredeemed commercial allocation and redeemed participant entitlement are different truths.
- Accepted split post-redemption control: payer retains payment/settlement and explicitly authorised future sponsorship control; recipient/participant controls the redeemed participant right and protected participant information.
- Clarified that refund-request authority, financial settlement destination and entitlement consequence may belong to different roles.
- Accepted fixed-duration/prepaid gifted membership as the default and prohibited silent recurring debit authority.
- Accepted explicit recurring sponsorship only through separate payer consent, with future-billing cancellation not retroactively revoking the already-paid recipient period.
- Recorded Store's purchaser→subscription-user→grantee assumption as insufficient for NewYou gift/sponsorship semantics while preserving Store payment/idempotency/source-aware-entitlement mechanisms as reuse candidates.
- Advanced `CER-PT-013` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.11.0 — 2026-09-09

- Accepted `CER-PT-011`.
- Recorded NewYou verdict: **PASS**.
- Recorded Store Blueprint verdict: **CHANGES REQUIRED / ADAPTATION REQUIRED — STRONG ENTITLEMENT REUSE CORE**.
- Confirmed that current Product/Domain authority is sufficient; no new CER upstream delta is required.
- Clarified that Premium is commercial packaging over Basic plus governed add-on components rather than a new opaque entitlement identity.
- Recommended one authoritative current membership composition rather than competing Basic/add-on/Premium recurring contracts.
- Added source→target composition-delta semantics for upgrades/downgrades while preserving continuity of unchanged rights.
- Clarified that revoking one commercial source must not remove a right still supported by another valid source.
- Recorded Store's source/provenance-aware EntitlementGrant model as a strong reuse candidate.
- Recorded Store's one-plan/one-entitlement and line-oriented subscription creation as insufficient for NewYou Premium composition without adaptation.
- Removed the previously anticipated add-on/Premium contract-identity question from the unresolved-candidate list because PT-011 resolved it at the Pre-JIT doctrine level.
- Advanced `CER-PT-012` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.10.0 — 2026-09-09

- Accepted `CER-PT-010`.
- Recorded NewYou verdict: **BLOCKED / STOP — PRODUCT AUTHORITY GAP**.
- Created and accepted `CER-UPD-002 — Dispute/chargeback access and commercial-right consequences`.
- Accepted a reversible, source-scoped pending-dispute hold rather than no-op or immediate global revocation.
- Clarified that dispute opening is contested commercial state, not final reversal, fraud proof or account-wide punishment authority.
- Clarified merchant-favour restoration without repurchase/duplicate entitlement and customer-favour final reversal without erasing historical consumption.
- Clarified that historical disputed periods must not invalidate later independently paid recurring periods.
- Accepted the working clarification that permanent once-off access remains non-expiring only while the qualifying purchase remains commercially valid; final chargeback reversal may end future paid-origin platform access while retained history/professional/safety records remain.
- Recorded Store Blueprint verdict: **CHANGES REQUIRED / NOT REUSABLE FOR THIS SEMANTIC AS-IS**.
- Recorded Store provider-event dedupe as reusable mechanism evidence while dispute lifecycle, source-scoped hold/restore, recurring-contract dispute handling and chargeback-to-Entitlements convergence remain unproven.
- Advanced `CER-PT-011` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.9.0 — 2026-09-09

- Accepted `CER-PT-009`.
- Recorded NewYou semantic verdict: **PASS**.
- Recorded Store Blueprint verdict: **CHANGES REQUIRED / REUSE AFTER HARDENING**.
- Preserved `HSP-UPD-007` as the existing generated-vs-delivered Plan refund seam; no duplicate CER upstream delta created.
- Clarified that Product-defined irreversible-benefit boundaries govern refundability.
- Added the refund-commitment vs irreversible-consumption concurrency invariant.
- Clarified that successful refunds may revoke future rights but cannot erase historical consumption.
- Clarified that refund amount alone is not entitlement authority.
- Recorded Store's generic refund eligibility and generic digital revocation policy as insufficient for NewYou business semantics.
- Recorded Store post-refund convergence and Paystack refund-event adaptation as hardening requirements.
- Advanced `CER-PT-010` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.8.0 — 2026-09-09

- Accepted `CER-PT-008`.
- Recorded NewYou semantic verdict: **PASS**.
- Recorded Store Blueprint verdict: **CHANGES REQUIRED / ADAPTATION REQUIRED**.
- Clarified cancellation as a negative renewal instruction and downgrade as a replacement renewal instruction.
- Established precedence for cancellation vs verified-paid renewal.
- Established a JIT-level commercial-commitment boundary for downgrade-vs-renewal races.
- Clarified that a renewal must reconcile the immutable commercial contract it actually priced and charged.
- Recorded Store defects: queued renewal does not re-check `cancel_at_period_end`, period-end terminal closure is not proven, and mutable `pending_*` terms can rewrite later reconciliation.
- Advanced `CER-PT-009` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.7.0 — 2026-09-09

- Accepted `CER-PT-007`.
- Recorded NewYou semantic verdict: **PASS — PROVIDER VALIDATION STILL REQUIRED**.
- Recorded Store Blueprint verdict: **CHANGES REQUIRED / ADAPTATION REQUIRED**.
- Preserved locked Product semantics: upgrades are immediate with proration; downgrades take effect at renewal.
- Clarified that "immediate" means immediately after authoritative commercial success, not optimistic entitlement before payment verification.
- Added the renewal-vs-upgrade ordering invariant and stale-pricing revalidation requirement.
- Recorded current Paystack primary-source evidence: public Subscription APIs do not show an individual immediate plan-switch/proration endpoint; existing-plan updates apply next billing cycle; Paystack subscriptions are not automatically retried; reusable authorisations can be charged for a merchant-specified amount.
- Kept OQ-004 open for final Paystack mechanism validation.
- Recorded the exact merchant-managed proration formula as a **conditional upstream seam**, not a new `CER-UPD`.
- Recorded Store's queued change mechanism as reusable only for renewal-boundary change semantics such as downgrades.
- Recorded Store's mutable-pending-term paid-renewal reconciliation as a commercial-integrity defect for NewYou reuse.
- Advanced `CER-PT-008` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.6.0 — 2026-09-09

- Accepted `CER-PT-006`.
- Recorded NewYou semantic verdict: **PASS**.
- Recorded Store Blueprint verdict: **CHANGES REQUIRED / ADAPTATION REQUIRED**.
- Clarified that retry exhaustion produces **suspension**, not commercial-contract erasure.
- Clarified that late verified success for the same still-authorised renewal must reconcile and may restore the suspended membership and Entitlements.
- Preserved `CER-UPD-001`: if cancellation already withdrew renewal authority, late provider success must not reactivate the membership.
- Clarified that retry exhaustion ends automatic dunning authority and does not permit indefinite blind charging.
- Recorded Store's `grace expired → expired` terminal model as not reusable as-is for NewYou.
- Advanced `CER-PT-007` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.5.0 — 2026-09-08

- Accepted `CER-PT-005`.
- Recorded NewYou verdict: **BLOCKED / STOP — PRODUCT AUTHORITY GAP**.
- Created and accepted `CER-UPD-001 — Cancellation during failed-renewal grace and late-success precedence`.
- Accepted Option C: cancellation during failed-renewal grace is immediately effective, withdraws unresolved renewal authority and ends membership-only grace access.
- Clarified that a renewal already authoritatively verified-paid before cancellation remains a valid paid period and cancels at its end.
- Clarified that provider success reconciled only after cancellation must not reactivate the membership and must enter reversal/refund or governed commercial-remedy handling.
- Recorded Store Blueprint as blocked for reuse certification on this semantic because its current implementation suppresses future retries but may still allow an already-running renewal to reconcile after cancellation.
- Advanced `CER-PT-006` to NEXT.
- No governed NewYou repository mutation performed for this version.

## v0.4.0 — 2026-09-08

- Established the living local deep-discovery artifact.
- Backfilled accepted CER-PT-001 through CER-PT-004.
- Preserved the dual-verdict and recommendation-duty working method.
- Added current Store reuse ledger.
- Added HSP cross-seam preservation rule.
- Added pressure-test register and identified CER-PT-005 as next.
- Defined stable-filename + internal-SemVer update protocol.
- Clarified that active discovery remains outside the governed repository until later compression/handoff.

### Historical note

An initial CER working directory/files were prematurely written to the NewYou repository during this chat before the desired workflow was clarified. They are not treated by this living artifact as authority or as the preferred active-discovery source. No further repository mutation for this stream is authorised unless explicitly requested by the user.

### Later repository-handoff cleanup

The repository still contains the accidental `working/commerce_entitlements/NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.1.0.md` and its README, which still describe v0.1.0 as current/living. Do not rewrite them during active local stabilisation. When the compressed CER pack is explicitly approved for repository handoff, supersede that routing explicitly, preserve the old file as historical provenance, refresh affected Privacy→CER cross-references, and keep all CER artifacts non-authoritative unless a separate governed amendment promotes specific conclusions.

---

# 14. Standing anti-drift principles

1. **Authority ≠ acceleration.**
2. **Provider state is evidence, not NewYou business authority.**
3. **Commerce money/contract truth ≠ Entitlements access/right truth.**
4. **Delivery identity ≠ business-effect identity.**
5. **Provider event order is an observation property, not a business rule.**
6. **A failed payment attempt ≠ failed purchase forever.**
7. **A billing retry is not a new renewal.**
8. **Retries may multiply execution; logical business consequence must not multiply.**
9. **Commercial success must not become a silent entitlement orphan.**
10. **Store Blueprint mechanisms may be reused; Store Blueprint domain law may not.**
11. **Exact Paystack behaviour must validate against NewYou semantics, not define them.**
12. **Do not create a new Domain merely because a recurring engine, worker, page or provider integration exists.**
13. **Do not freeze Resource/table/worker representations during Pre-JIT unless authority genuinely requires them.**
14. **If downstream work exposes an upstream contradiction, STOP at the correct authority level.**
15. **During failed-renewal grace, a later accepted cancellation may withdraw future continuation authority; provider/in-flight execution must not silently outrank that commercial instruction.**
16. **Suspension after retry exhaustion is recoverable contract/access state, not proof that the recurring contract ceased to exist.**
17. **Late verified payment may restore a suspended membership only when the same renewal remains commercially authorised.**
18. **An upgrade is a commercial adjustment, not merely a queued future subscription configuration.**
19. **Immediate upgraded access follows verified commercial success, not provider-request dispatch.**
20. **Renewal and upgrade may race technically, but must have one authoritative commercial ordering.**
21. **Paid renewal reconciliation must apply the contract that was actually priced and charged.**
22. **Stale proration/upgrade pricing must be revalidated or recomputed before irreversible collection.**
23. **Provider-native proration is optional; provider-safe execution consistent with NewYou authority is mandatory.**
24. **Cancellation is a negative renewal instruction; downgrade is a replacement renewal instruction.**
25. **A queued renewal does not outrank a later authoritative boundary instruction.**
26. **A renewal must apply the immutable commercial contract it actually priced and charged.**
27. **Pending future contract state may not rewrite the meaning of an already-created payment.**
28. **Recurring-contract boundary races require one authoritative ordering, not last-write-wins mutation.**
29. **Refundability follows Product-defined irreversible benefit boundaries, not generic percentage-used logic.**
30. **Refund commitment and new irreversible benefit consumption must not both succeed against the same commercial right.**
31. **A refund may revoke future rights but may not erase historical consumption.**
32. **Money refunded and benefit already consumed can both be true at the same time.**
33. **Refund amount is not entitlement authority.**
34. **Generic Store refund mechanics may be reused; generic Store revocation policy may not replace NewYou Product and Entitlements law.**
35. **A dispute is contested payment truth, not final reversal truth.**
36. **Opening a dispute does not erase historical payment, fulfilment or consumption.**
37. **Pending dispute consequences must be reversible and source-scoped.**
38. **A final chargeback may end future rights without rewriting consumed history.**
39. **A dispute against one commercial occurrence does not invalidate unrelated later valid occurrences.**
40. **Financial reversal does not itself prove fraud.**
41. **Refund and chargeback may share financial machinery but are not the same business lifecycle.**
42. **Provider dispute state is evidence; NewYou Commerce owns the commercial interpretation.**
43. **Bundle identity is not entitlement identity.**
44. **Premium is commercial packaging over Basic plus governed add-on components.**
45. **One participant should have one authoritative current membership composition, even if provider execution uses multiple objects.**
46. **Bundle transitions apply commercial and entitlement deltas rather than destroying and reconstructing unchanged rights.**
47. **An unchanged component right must remain continuous through package changes.**
48. **Revoking one source must not remove a right still supported by another valid source.**
49. **A package change must not leave obsolete component billing obligations running alongside their replacement bundle.**
50. **Provider structure must not define NewYou membership truth.**
51. **Purchaser, recipient, participant and account holder remain distinct even when one human occupies several roles.**
52. **Payment for another person does not make the payer the entitlement holder or participant.**
53. **An unredeemed allocation is not yet the recipient's participant entitlement.**
54. **Redemption is a durable, exactly-once transfer boundary.**
55. **Recipient-routing data is not canonical grantee identity.**
56. **After redemption, funding does not imply participant-data visibility or ordinary unilateral access revocation.**
57. **Refund-request authority, financial settlement destination and entitlement consequence are separate truths.**
58. **Sponsored aggregate reporting must not become participant surveillance.**
59. **Pre-disclosed grant expiry is not the same as discretionary sponsor revocation.**
60. **Gifted membership must not silently create recurring payer authority.**
61. **Explicit recurring sponsorship separates payer billing control from recipient participation/access rights.**
62. **Unredeemed cancellation/refund and redemption require one authoritative ordering.**
63. **Store's purchaser→subscription user→grantee assumption is not reusable as NewYou gift/sponsorship semantics.**
64. **Manual payment evidence is not commercial payment truth until authoritatively verified and matched.**
65. **Manual EFT creates no implicit future debit or automatic-renewal authority.**
66. **Absence of another EFT is not a failed automatic renewal.**
67. **One verified EFT application may create the purchased consequence only once.**
68. **Underpayment must not silently create full entitlement.**
69. **Overpayment and duplicate money do not automatically create additional entitlement.**
70. **Late money may be financially real while no longer authorised to activate the original commercial right.**
71. **Delayed administrative verification must not silently consume paid access duration.**
72. **A new recurring payment method requires fresh explicit payer authority.**
73. **Store's generic payment spine is reusable; its provider-oriented PaymentIntent is not a manual-EFT model as-is.**
74. **Expiry for new use does not necessarily erase an already-admitted obligation.**
75. **Admission and expiry must have one authoritative Entitlements ordering.**
76. **Queue insertion is not entitlement admission.**
77. **Bounded completion is not membership extension or a carried-forward reusable credit.**
78. **The completion right remains bound to the exact Request, source and benefit class.**
79. **A later membership period must not silently become the source for an older admitted Request.**
80. **Current entitlement validity governs new admission; it does not alone decide previously admitted fulfilment authority.**
81. **Ordinary expiry must remain distinct from refund, dispute, chargeback, Safety invalidation and withdrawal.**
82. **`HSP-UPD-001` remains the single upstream identity for the ordinary-expiry completion-right gap.**
83. **Recovery is a business capability, not merely worker retry.**
84. **Technical retry exhaustion must not manufacture terminal business truth.**
85. **Reconciliation derives current commercial truth from stable logical identity, durable NewYou state, available provider evidence and current governing authority — not provider-event arrival order.**
86. **Restart, deployment, queue loss and webhook retry exhaustion may interrupt execution but may not erase an outstanding commercial obligation.**
87. **Recovery of stale evidence must revalidate current Commerce authority before producing current access or membership consequences.**
88. **Business idempotency must survive worker identity, queue identity and process lifetime.**
89. **Commerce-to-Entitlements convergence must remain independently repairable after the original consequence-delivery path fails.**
90. **Unresolved ambiguity must remain explicitly unresolved and visible; it must not be fabricated into success or failure.**
91. **Recovery should target durable unresolved or mismatched obligations rather than blindly replaying all historical events.**
92. **Historical provider observations remain evidence even when reconciliation changes the current authoritative interpretation.**
93. **Billing cadence is part of the commercial contract, not entitlement identity.**
94. **A same-composition cadence change must not create a second membership or revoke/regrant unchanged membership rights.**
95. **Under accepted `CER-UPD-005`, ordinary monthly↔annual cadence changes default to the next not-yet-committed renewal boundary.**
96. **The existing paid period remains authoritative through its existing end in either cadence direction; cadence change creates no implicit forfeiture, refund, credit or overlapping billing.**
97. **Cadence change and renewal require one Commerce-owned boundary ordering.**
98. **A mutable future cadence/plan must never rewrite the cadence/price actually authorised and charged for an already-committed renewal occurrence.**
99. **Cadence-transition policy does not itself decide future target price/version migration or Premium-continuity semantics; those remain separate second-pass seams.**
100. **Annual→monthly is not a separate commercial class from monthly→annual; both preserve the current paid period and change only the next not-yet-committed renewal cadence by default.**
101. **A period-end cancellation is a future non-renewal instruction, not present termination.**
102. **Before actual termination, a participant may replace a pending `do not renew` instruction with `renew unchanged` under accepted `CER-UPD-006`.**
103. **Cancellation rescission preserves the same membership relationship, current paid period and unchanged entitlement continuity; it does not create a new membership or paid period.**
104. **Cancellation rescission is prospective and cannot retroactively authorize a collection that occurred after renewal authority had already been withdrawn.**
105. **Undo cancellation before termination and re-subscribe after termination are different commercial journeys.**
106. **Restoring membership renewal intent does not itself restore separately revoked or invalid reusable payment authority.**
107. **Execution that would terminate or suppress renewal must revalidate the current future instruction before crossing an irreversible commercial boundary.**
108. **Actual membership termination is a hard commercial-history boundary.**
109. **A later re-subscription creates a new commercial occurrence rather than reopening the terminated occurrence.**
110. **Same participant/account identity does not collapse distinct membership commercial occurrences.**
111. **Late provider evidence remains bound to the occurrence it concerns and cannot silently mutate a later re-subscription.**
112. **Fresh customer purchase intent is required for re-subscription; reusable payment authority is not itself authority to restart membership.**
113. **Historical retained rights and a new current membership may coexist with distinct entitlement provenance.**
114. **Public/list price is not existing-member contract authority.**
115. **A recurring price change never reprices an already-paid period or already-committed renewal.**
116. **Existing-member price migration requires an explicit future effective contract and one Commerce-owned ordering against renewal commitment.**
117. **A higher-price renewal must fail closed against the increase where required notice/consent/legal transition conditions are incomplete.**
118. **Grandfathering or price locking is deliberate Product truth attached to a qualifying offer/membership occurrence, not an accidental historical-list-price property.**
119. **A post-termination re-subscription does not inherit an old price solely because the same participant previously held it.**
120. **Provider amount/configuration is financial/execution evidence only and cannot redefine NewYou price-contract truth.**
121. **Recurring promotion is Commerce pricing truth, not entitlement identity.**
122. **Base-price contract/version and promotional adjustment are separate commercial truths.**
123. **Cycle-limited recurring promotion scope is consumed by successful qualifying paid periods, not payment attempts, retries or duplicate execution.**
124. **Unused promotional scope is not a standalone/banked credit and does not survive termination by default.**
125. **Post-termination re-subscription neither automatically inherits remaining promotion value nor automatically resets once-only eligibility.**
126. **An accepted recurring promotional promise cannot be retroactively rewritten by later public promotion mutation/deactivation.**
127. **Promotion duration must preserve its semantic unit/basis across package or cadence changes; raw remaining-count state is insufficient.**
128. **Promotion expiry and underlying ordinary base-price migration are separate commercial events.**
129. **Provider replay duplication and genuinely duplicated customer purchase attempts are distinct failure classes.**
130. **At most one ordinary recurring membership commercial relationship may be admitted for the same canonical grantee at a time.**
131. **Two successful financial collections do not automatically create two valid memberships or two paid periods.**
132. **Commerce admission ordering, not provider callback arrival, decides which conflicting ordinary membership purchase is authoritative.**
133. **A successful non-admitted duplicate collection requires full reversal/refund or governed make-whole handling by default.**
134. **Provider transaction idempotency is necessary but insufficient for business-level duplicate membership prevention.**
135. **Duplicate-payment remediation is source-scoped and must not revoke or alter the valid membership.**
136. **Payment-method replacement changes execution authority for the same logical renewal; it does not create a new renewal occurrence.**
137. **One renewal may have multiple instrument-specific attempts but at most one successful collection consequence and one paid period.**
138. **Changing the stored/default payment method is prospective and does not by itself retroactively invalidate a legitimately submitted earlier attempt.**
139. **An unresolved old attempt must be reconciled or safely neutralised before NewYou knowingly risks another independent successful collection.**
140. **If old and new instrument attempts both succeed for one renewal, the excess financial collection requires source-scoped reversal/refund/remedy rather than another membership period.**
141. **Reusable payment authority and membership renewal authority are separate durable truths.**
142. **A requested immediate upgrade is a conditional commercial transition, not immediate replacement of the current paid membership.**
143. **Failed or ambiguous upgrade adjustment does not revoke existing valid membership rights.**
144. **Target membership rights begin only after the required adjustment becomes authoritative and the target remains commercially applicable.**
145. **Late upgrade success must revalidate current instruction, membership state and pricing/proration basis before changing membership.**
146. **A stale or no-longer-authorized successful upgrade adjustment is reconciliation/remedy truth rather than membership authority.**
147. **Period-end cancellation and an unresolved current-period upgrade instruction are independent commercial dimensions unless Product explicitly couples them.**
148. **Retries or duplicate successful adjustment attempts cannot multiply the logical upgrade consequence.**
149. **One not-yet-committed renewal boundary has one current authoritative future commercial outcome.**
150. **Multiple future-facing instructions form an ordered supersession history rather than competing latent authorities.**
151. **A dimension-specific change transforms only its semantic scope while preserving other still-valid future dimensions.**
152. **Period-end cancellation replaces the future renewal outcome with `do not renew` and makes prior pending targets historical rather than latent.**
153. **Cancellation rescission restores `renew unchanged` from the current live contract and does not automatically resurrect pre-cancellation targets.**
154. **Once renewal is commercially committed, later instructions cannot rewrite it and target the next not-yet-committed boundary instead.**
155. **Stale or concurrent future instructions must not overwrite newer authoritative future-contract truth.**
156. **Ordinary add-ons are recurring commercial components of the existing Basic membership relationship, not separate ordinary memberships.**
157. **Ordinary add-ons inherit the Basic cadence and renewal boundary by default unless Product explicitly defines independent billing.**
158. **Mid-period add-on activation is success-gated on any required incremental/prorated adjustment and failure leaves the existing composition unchanged.**
159. **Ordinary add-on removal is a composition downgrade effective at the next not-yet-committed renewal boundary by default.**
160. **Removing one add-on does not cancel Basic or unrelated add-on components.**
161. **A dependent ordinary add-on does not outlive the Basic membership source it augments.**
162. **Premium is a named commercial bundle over Basic plus governed add-on components and transitions apply source→target component deltas without duplicate billing obligations.**
163. **Independently billed add-ons require explicit Product authority for their own cadence, paid period, cancellation, failure and dependency semantics.**
164. **Gift/sponsor value remains source-specific and does not overwrite existing membership provenance.**
165. **Equivalent already-paid coverage does not silently consume duration-based gift/sponsor value in parallel by default.**
166. **Duration-based gift/sponsor coverage begins at the next eligible uncovered not-yet-committed boundary unless the governed offer explicitly defines another clock.**
167. **Gift/sponsor-funded periods suppress overlapping ordinary self-paid collection for the same covered composition.**
168. **Open-ended or uncertain-duration sponsorship does not automatically restart personal billing without explicit participant fallback consent.**
169. **Sponsor termination affects future funding only and does not revoke an already-funded recipient period.**
170. **Applying gift/sponsorship does not silently rescind an existing self-paid membership cancellation.**
171. **Fixed-calendar sponsored offers may legitimately overlap existing coverage only when that bounded-window behavior is explicit in the offer.**
172. **Termination of one entitlement source must not revoke access independently sustained by another valid source.**
173. **Premium reassessment maturity is based on uninterrupted qualifying Premium coverage time for the canonical grantee, not charge count, payment method, cadence or funding-source identity.**
174. **Annual Premium renewal is the annual-billing expression of the same twelve-month maturity boundary; initial annual purchase or cadence switch into annual does not accelerate eligibility.**
175. **Seamless transitions among qualifying self-paid, gift and sponsored Premium sources preserve continuity when no uncovered Premium interval exists.**
176. **Overlapping qualifying Premium sources count elapsed calendar time once and never accelerate reassessment maturity.**
177. **Grace access alone is not qualifying paid Premium tenure; continuity remains provisional until Commerce establishes whether the Premium period actually existed.**
178. **Premium→Basic downgrade, qualifying Premium termination or any genuine uncovered Premium interval breaks continuity; later Premium begins a new interval.**
179. **An unused Premium reassessment entitlement expires when qualifying Premium coverage ends even if Basic membership continues.**
180. **Nonaccumulation means at most one unused Premium reassessment entitlement exists and missed anniversaries do not create hidden or catch-up entitlements.**
181. **After later consumption of an existing reassessment entitlement, the next entitlement becomes available only at the next future qualifying anniversary.**
182. **NewYou-specific Premium-tenure and reassessment policy belongs outside the reusable Store package; Store should supply generic commercial-period/provenance evidence only.**
183. **Each commercial membership/add-on source has one latest authoritative entitlement target set/version.**
184. **Composition changes converge a source to its target set rather than depending on unsafe grant-before-revoke or revoke-before-grant ordering.**
185. **Where transition presentation is incomplete, effective access must not exceed the new target and must preserve rights common to old and new sets.**
186. **Unchanged component rights remain continuously valid across composition transitions.**
187. **Removed rights cease no later than their governed effective boundary, while newly added rights begin only after authoritative target acceptance.**
188. **Duplicate, reordered or stale entitlement target application must not produce a superseded source state.**
189. **Recovery derives the latest source-specific target from durable authority rather than replaying presumed worker history.**
190. **A source-specific composition change must not revoke equivalent rights independently sustained by another valid entitlement source.**
191. **Caches and projections do not become entitlement authority and must not extend revoked or expired access.**
192. **Multiple legitimate entitlement sources may coexist for one canonical grantee without being merged or reduced to one global winner.**
193. **Boolean/scoped effective access is the union of currently valid qualifying sources.**
194. **Effective access equivalence does not rewrite authoritative Commerce membership truth or create a synthetic membership tier.**
195. **An access-overlay grant changes only its explicit governed scopes and does not alter billing or Premium-tenure qualification unless Product explicitly says so.**
196. **A qualifying membership-coverage grant may substitute the covered future commercial composition/interval and suppress only redundant covered self-paid collection.**
197. **Partial grants affect only their covered commercial/access components and do not cancel unrelated base obligations.**
198. **Overlapping sources do not by themselves multiply ordinary recurring limited benefits, continuity clocks or nonaccumulating entitlements.**
199. **Additional limited-benefit units arise only from explicit governed additive Product/grant authority.**
200. **Consumption applies exactly once against an authoritative eligible benefit occurrence/source and preserves auditable provenance.**
201. **No global source-precedence hierarchy is authorised; capability-specific resolution is required.**
