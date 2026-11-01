# NewYou Operations, Support & Paid Pilot Pre-JIT — Compressed Candidate v0.1.0

> **STATUS:** WORKING COMPRESSION CANDIDATE  
> **REVIEW BASIS:** v0.32.0 received **PASS WITH NON-BLOCKING CORRECTIONS — COMPRESSION-READY**  
> **SOURCE WORKING ARTIFACT:** `NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.32.0.md`  
> **SOURCE SHA-256:** `9d7895b6db1b9b2eb12b3c7c0ff38c16f29915ea730967e2a7c514c8c40fb518`  
> **PRESSURE-TEST EVIDENCE:** `OPS-PT-001...470` contiguous in the append-only working artifact  
> **GITHUB / PR / ACTIONS:** deliberately deferred until reviewed compression is accepted  
> **IMPLEMENTATION:** NOT AUTHORISED  
> **PURPOSE:** current-state semantic compression only; this file does not silently rewrite frozen Product Law or Decision history.

---

## 1. Authority and use

This document is the compressed current-state candidate produced from the independently reviewed append-only Pre-JIT.

It is intended to:

- remove superseded working states and historical contradictions;
- preserve only the final reviewed Product/Domain/lifecycle semantics;
- identify the formal Product Law / Decision Register amendments still required;
- provide the current input to repository/governance integration and later JIT work.

Authority hierarchy remains:

```text
Product Law
→ Architecture Law
→ Domain Law
→ Roadmap
→ supporting operating/frontend contracts
→ current Open Work
→ approved Feature Pack / JIT contracts
→ proof
→ implementation
```

This compression does **not** itself promote proposed amendments into frozen law.

---

## 2. Scope and global invariants

This Pre-JIT covers Operations, Support and first-paid-pilot semantics without creating an Operations, Support, Admin, Refund, Choice, Timer or Pilot business Domain.

Global invariants:

```text
every durable business truth
→ exactly one authoritative owner

cross-domain mutation
→ through the owning Domain

provider / worker / UI / Analytics / Audit / cache state
→ never silently becomes business authority

authority
≠ acceleration

ambiguous money / entitlement / Safety / deletion state
→ fail closed and reconcile

historical immutable evidence
→ preserved where law requires
→ never silently rewritten into current truth
```

The approved Domain set remains unchanged.

---

## 3. Current ownership map

### Commerce

Owns:

- commercial product / offer / price / discount truth;
- purchase/order and purchaser/payer/recipient commercial relationships;
- payment, refund, dispute, chargeback and settlement truth;
- authoritative refund amount and payment destination;
- bundle component refund allocation;
- restricted financial evidence surviving deletion where law permits;
- provider reconciliation.

Does not own recipient-private health/Safety/Plan truth or access entitlement.

### Entitlements

Owns:

- durable paid rights and component entitlements;
- assessment credit availability/hold/consumption/closure;
- Plan entitlement availability/consumption/closure;
- bundle decomposition;
- idempotent entitlement consequences.

Does not own money settlement.

### Safety & Eligibility

Owns:

- current eligibility/routing;
- `eligible_automated`;
- `general_wellness_only`;
- `professional_review_required`;
- `insufficient_information`;
- Safety restriction/clearance authority.

Does not own refunds or commercial entitlement.

### Plans & Nutrition

Owns:

- Plan generation/delivery lineage;
- immutable Plan snapshots;
- first successful Plan fulfilment;
- correction/replacement lineage.

### Temperament

Owns assessment methodology representation, assessment attempts/results and paid report delivery truth.

### Privacy & Consent

Owns Full Deletion/export orchestration and deletion-completion truth.

Deletion orchestration invokes other owners; it does not acquire their business authority.

### Identity & Access

Owns canonical identity/authentication/authority context used to verify consequential human commands.

### Audit & Evidence

Owns minimised evidence only.

Audit never substitutes for Commerce, Entitlements, Safety, Privacy or another owner transition.

---

# 4. OPS-UPD-001 — first-paid pilot admission and cap

## 4.1 Product progression

```text
internal validation
→ first 10 real paid participants
→ review
→ expand toward 25
→ review
→ maximum 50 in first paid pilot
```

The current first-pilot cumulative admission ceiling is monotonic non-decreasing within that progression.

It never exceeds 50.

Intermediate exact ceilings may be authorised within the applicable reviewed band.

## 4.2 Independent dimensions

Keep separate:

```text
historical cumulative exposure
numeric cumulative admission ceiling
current new-admission gate
protected reservation capacity
```

Rollback/stop:

```text
closes new-admission gate
```

and does **not** lower the numeric ceiling or rewrite historical exposure.

## 4.3 Core invariants

```text
historical counted exposure
+ protected reserved-but-not-counted capacity
<= effective cumulative admission ceiling
<= applicable progression maximum
<= 50

one real participant lineage
→ counted at most once

refund / withdrawal / Safety pause / Full Deletion
→ does not recycle historical pilot exposure

stale projection
→ cannot authorise admission

ambiguous cap/admission authority
→ fail closed
```

Re-entry requires explicit governed re-entry authority; technical recovery alone does not reopen admissions.

---

# 5. OPS-UPD-002 — duplicate genuine collection / money reconciliation

Distinguish:

```text
duplicate evidence
≠ duplicate genuine collection

one commercial obligation + multiple genuine collections
→ retain only lawful amount
→ make payer whole for excess

two intended purchases
→ separate obligations
```

For amount due `D` and verified collected total `C`:

```text
if C > D:
  excess = C - D
```

Excess remediation is independent of ordinary Product refund cutoffs.

Core rules:

- one intended purchase creates at most one valid entitlement consequence;
- refund/reversal/chargeback/duplicate-remediation outcomes reconcile to one authoritative net economic result;
- provider state remains evidence until Commerce reconciles it;
- unresolved financial obligations survive deletion only through minimum lawful restricted Commerce evidence;
- payer, purchaser, recipient and participant remain distinct.

---

# 6. OPS-UPD-003 — consequential human commands

A consequential human command is authenticated human intent causing material durable or external effect.

Authority is not a role label.

Conceptually:

```text
actor
+ current assurance
+ role/capability
+ relationship
+ purpose
+ scope
+ unexpired authority
+ required approvals
+ current owning-Domain state/invariants
= command may be accepted
```

Rules:

- command executes through the owning Domain;
- no universal Super Admin / Support / Operations write authority;
- no automatic second approval for every command;
- no impersonation bypass;
- bulk actions enforce authority/invariants per affected item;
- break-glass enables bounded emergency capability, not specialist authority;
- accepted command does not imply completed consequence;
- material commands require business idempotency and auditable outcome;
- stale page/session/role state cannot authorise an irreversible mutation.

---

# 7. OPS-UPD-004 — paid Assessment credit lifecycle

Current working Product semantics:

```text
available_unused
→ held_unconsumed
→ consumed

or

→ closed_after_refund
```

First answer:

```text
claims / holds credit
≠ consumes credit
```

Consumption occurs only when the complete paid digital Assessment deliverable is durably available:

- immutable assessment result;
- paid report;
- primary/secondary guidance;
- introductory personalised guidance required by the paid deliverable.

If a started nontechnical attempt expires without complete paid delivery:

```text
same credit
→ returns to available_unused
```

Technical failure preserves the delivery obligation/recovery/refund path.

Annual retake timing starts from successful digital Assessment delivery, not merely attempt start.

No notification, read/open event, Analytics event or provider observation consumes the credit.

---

# 8. OPS-UPD-005 — Plan pre-first-fulfilment changes and refund boundaries

## 8.1 First fulfilment boundary

Before first successful qualifying personalised Plan delivery:

- latest lawful participant intent may change;
- current Safety authority outranks preferences;
- generated-but-undelivered snapshot does not fulfil the paid Plan;
- stale snapshots remain historical but cannot be delivered as current truth.

After first successful fulfilment, material re-personalisation follows existing DEC-038/new-purchase or qualifying-membership rules.

## 8.2 Ordinary Plan refund

Current ordinary rule:

```text
before generation
→ ordinary Plan refund available

after generation
→ ordinary change-of-mind refund closed
```

Generation and successful first fulfilment are separate facts.

## 8.3 Safety-invalidated failed fulfilment — formal Product amendment required

The final reviewed candidate requires explicit amendment/supersession of historical DEC-045.

Where:

```text
valid paid Plan component exists
AND Plan was generated
AND no qualifying first delivery succeeded
AND current Safety no longer permits qualifying personalised first fulfilment
AND the block is not merely a still-actionable temporary insufficient-information state
```

then an **accrued elective refund remedy** exists.

The participant/recipient may:

```text
retain still-unconsumed Plan right
OR
relinquish it through failed-fulfilment refund path
```

General Wellness and professional review do not fulfil or consume the paid personalised Plan.

### Outcome-specific scope

`general_wellness_only`:

```text
retain right OR elect failed-fulfilment refund
```

`professional_review_required`:

```text
retain right OR elect failed-fulfilment refund
professional review remains separate
```

Actionable `insufficient_information`:

```text
complete current participant clarification first
exception not yet active solely from that transient actionable state
```

If all requested clarification is completed and no included participant action can produce lawful first fulfilment:

```text
retain right OR elect failed-fulfilment refund
```

Still `eligible_automated`, but prior snapshot stale:

```text
regenerate safely under same right
no exceptional refund merely because regeneration is required
```

---

# 9. OPS-UPD-007 — General Wellness and the paid Plan entitlement

General Wellness is non-substitutive:

```text
General Wellness
≠ paid 7-Day Personalised Plan fulfilment

General Wellness use
≠ Plan entitlement consumption
```

If the current route is `general_wellness_only` before Plan generation:

```text
personalised generation blocked
Plan right remains active/unfulfilled
ordinary pre-generation refund remains available
```

No current MVP General-Wellness choice timer exists.

Do not invent:

- countdown;
- inactivity expiry;
- automatic credit;
- automatic professional-review conversion;
- Timer/Choice Domain.

If later eligibility becomes `eligible_automated`, the same still-valid unfulfilled right may fund exactly one qualifying first Plan unless it was refunded/deleted/otherwise closed.

---

# 10. R549 Assessment + Plan Bundle commercial allocation

Current launch offer:

```text
Assessment list price   = R249
Plan list price         = R399
Separate list total     = R648

Bundle price            = R549
Bundle saving           = R99
```

Authoritative current launch component allocation:

```text
Assessment component = R249
Plan component       = R300
Total                = R549
```

The R99 discount is allocated entirely to the Plan component.

Consequences:

```text
Assessment fulfilled + Plan refundable
→ refund R300

Plan retained/fulfilled + Assessment independently refundable
→ refund R249
→ retained Plan is not repriced to R399

both components refundable
→ total <= R549 after reconciliation
```

Refund uses the accepted historical offer-version allocation, never current standalone list price.

Every future paid bundle/sponsored offer requiring partial refunds must define its own deterministic component allocation before activation.

---

# 11. Split purchaser / payer / recipient / participant semantics

Keep distinct:

```text
purchaser
payer
recipient
participant
account holder
```

Paying for another person grants no access to that person's:

- health;
- Safety outcome;
- Assessment result;
- Plan;
- progress;
- deletion reason.

## 11.1 Money versus entitlement

After redemption:

```text
recipient
→ controls redeemed entitlement retain/relinquish decisions

authoritative payer/payment relationship
→ receives any monetary refund
```

Recipient cannot redirect another person's refund value merely because she controls the entitlement.

Payer cannot unilaterally terminate another person's redeemed health-related Plan through the optional refund paths merely because the payer funded it.

---

# 12. Ordinary pre-generation refund for third-party paid Plans

## 12.1 Before redemption

Use the reviewed precision:

```text
refund / cancellation authority
→ authorised purchaser / sponsor / commercial-order actor
  under the accepted offer

refund destination
→ authoritative payer/payment relationship
```

Bare payer status does **not** automatically equal cancellation authority where purchaser, payer and intended recipient are different actors.

## 12.2 After redemption

Redemption is the entitlement-authority transfer boundary.

For:

```text
A pays
→ B redeems
→ no Plan generated
→ ordinary refund still open
```

a payer/purchaser may request refund review, but Commerce may not commit the optional ordinary refund until the redeemed recipient explicitly relinquishes the Plan right.

If recipient relinquishes:

```text
Entitlements closes/revokes redeemed Plan right
Commerce commits refund to authoritative payer/payment relationship
```

If payer wants refund but recipient wants to retain Plan:

```text
recipient keeps Plan
optional ordinary refund does not commit
```

If recipient wants to relinquish but payer prefers continued use:

```text
recipient may relinquish
refund still returns payer-side
```

Never allow:

```text
committed refund
+ live corresponding redeemed Plan entitlement
```

and never revoke the entitlement merely because a payer submitted a request.

## 12.3 Generation race

If generation commits first:

```text
ordinary pre-generation refund closes
```

If refund commitment/entitlement closure wins first:

```text
stale generation cannot fulfil closed right
```

Onboarding/preferences alone do not close the ordinary refund window.

---

# 13. Failed-fulfilment remedy when payer ≠ recipient

For a redeemed third-party paid Plan:

```text
recipient
→ controls retain/relinquish election

authoritative payer/payment relationship
→ monetary refund beneficiary
```

Payer may not independently invoke the Safety-dependent exception after redemption to terminate the recipient's right.

If recipient relinquishes:

```text
recipient Plan closes through governed refund transition
payer/payment relationship receives refund
```

Payer receives minimum commercial information only:

- order/product/component;
- amount;
- refund status/reference;
- generic policy-based reason.

Do not disclose recipient Safety class, health facts, Plan data, Assessment data, progress or deletion reason.

Paid sponsorship follows the same principle.

Zero-price complimentary/sponsored rights create no invented cash refund.

---

# 14. Full Deletion × refund composition

## 14.1 General deletion law

Full Deletion permanently ends:

- account recovery;
- Plan/Assessment access;
- account-linked entitlements;
- Plan reconstruction.

Restricted financial/refund/dispute evidence may remain only as required and may never reconstruct the deleted account.

## 14.2 Accrued elective failed-fulfilment remedy

Qualification:

```text
failed-fulfilment Product conditions satisfied
→ accrued elective refund remedy exists
```

Keep separate:

```text
qualification
≠ refund request
≠ refund commitment
≠ provider settlement
≠ terminal net financial outcome
```

During the 14-day deletion cancellation window:

```text
deletion request alone
→ does not force refund commitment
```

At irreversible deletion execution, if an accrued failed-fulfilment remedy remains unresolved:

```text
deletion terminates retain-the-Plan branch
→ Commerce durably commits refund obligation
→ Entitlements may terminate Plan right
```

Requested/committed/settlement-pending refund survives deletion.

## 14.3 Ordinary pre-generation third-party refund + deletion

If a redeemed paid third-party Plan is:

```text
not yet generated
AND still ordinarily refundable
AND recipient reaches irreversible Full Deletion
```

then deletion is final recipient relinquishment.

Before the Plan entitlement is destroyed:

```text
Commerce must durably commit the still-valid ordinary refund
to the authoritative payer/payment relationship
```

### Critical settlement boundary

```text
durable refund commitment before entitlement destruction
≠
external provider settlement before deletion completion
```

Privacy must **not** wait for Paystack/provider settlement once:

- the Commerce obligation is durably preserved;
- the entitlement is irreversibly closed;
- all other deletion-completion requirements are satisfied.

Provider settlement/reconciliation may continue afterward using minimum restricted financial evidence.

Provider failure does not restore the deleted Plan entitlement.

Chargeback/reversal/refund interactions reconcile to one net authoritative customer-money outcome.

---

# 15. Payer deletion and recipient entitlement

Payer/account-holder deletion does not destroy another person's already-redeemed Plan.

If the recipient later validly relinquishes/refunds:

```text
Commerce uses minimum lawfully retained commercial/payment evidence
→ settles against authoritative payer/payment relationship
→ does not reconstruct payer account
```

Recipient does not become refund beneficiary by default.

---

# 16. Complimentary and sponsored access

## 16.1 Zero-price

```text
attributable paid Plan amount = R0
→ no cash failed-fulfilment refund
→ no cash ordinary Plan refund is invented
```

## 16.2 Positive-price sponsored / third-party access

Recipient controls redeemed entitlement relinquishment.

Sponsor/payer receives money.

Sponsor/payer receives no recipient-private health/Safety reason.

Paid bulk offers must define deterministic per-recipient/per-Plan refund allocation before activation where refunds may arise.

Missing allocation:

```text
affected offer activation = NO-GO
```

---

# 17. OPS-UPD-006 — export then Full Deletion

Export is:

```text
point-in-time governed release
```

not:

- live mirror;
- recovery credential;
- reconstruction authority;
- continuing entitlement.

A downloaded lawful participant-held copy may remain outside platform control.

Platform-controlled export artefacts must expire/delete/revoke according to policy.

If an accepted pre-deletion export could still disclose after deletion:

```text
export must reach governed terminal outcome
before deletion can be declared complete
```

Full Deletion cannot be reversed by old exports, transaction records, backups or retained evidence.

Existing legal/privacy/processor/restore gates remain required.

---

# 18. Cross-domain concurrency and failure rules

Across payment/refund/entitlement/Safety/deletion:

- authoritative current state must be re-read before irreversible consequence;
- stale workers cannot override later refund/deletion/Safety truth;
- provider ambiguity reconciles before irreversible duplicate consequence;
- every durable monetary/entitlement transition is idempotent;
- duplicate workers cannot create duplicate refund or duplicate fulfilment;
- refund commitment blocks competing first fulfilment;
- deletion replay prevents entitlement resurrection after backup restore;
- financial reconciliation survives deletion without account reconstruction;
- detailed health records are not retained merely to prove refund qualification.

Exact locks, transactions, Ash actions, Oban workers and schemas remain JIT.

---

# 19. Release / NO-GO conditions retained

The following remain release gates rather than invented implementation detail:

- formal promotion of the reviewed DEC-045 failed-fulfilment amendment/supersession;
- formal preservation of split payer/recipient refund semantics in Product/Decision authority;
- R249/R300 launch-bundle allocation in governed offer data;
- deterministic allocations for any future paid bundle/sponsored offers that need partial refund;
- payment/refund/provider validation;
- duplicate collection/refund/chargeback reconciliation proof;
- Safety eligibility matrix and applicable clinical gates;
- legal/privacy/retention approval;
- export/deletion/restore proof;
- first-paid operational/support/incident readiness;
- pilot progression sign-offs.

Any unresolved required release gate:

```text
affected stage = NO-GO
```

---

# 20. Formal Product / Decision promotions required before implementation

The reviewed compression requires explicit governed promotion rather than silent historical rewrite.

## 20.1 DEC-045 bounded failed-fulfilment amendment

Formal successor/amendment must state that:

- ordinary Plan refund ends at generation;
- bounded post-generation/pre-first-delivery Safety invalidation can create an accrued elective refund remedy;
- `general_wellness_only` and `professional_review_required` qualify as defined;
- actionable temporary `insufficient_information` must first follow its clarification path;
- General Wellness/professional review do not substitute for the paid Plan;
- successful refund closes the Plan right;
- qualified/committed monetary remedy composes with Full Deletion as defined here.

## 20.2 Gift / payer / recipient ordinary refund composition

Formal Product/Decision authority must preserve:

- before-redemption cancellation authority = authorised commercial-order actor under accepted offer;
- refund destination = authoritative payer/payment relationship;
- after-redemption optional ordinary refund requires recipient relinquishment;
- payer cannot unilaterally revoke redeemed access through that path;
- recipient may relinquish but does not become monetary beneficiary by default;
- deletion can act as final relinquishment where a valid refund path remains.

## 20.3 Historical decisions remain historical

Do not rewrite the original locked text in place.

Use explicit amendment/supersession with normal version history.

No new DEC identifier is assigned by this compressed Pre-JIT.

---

# 21. Evidence summary

The append-only predecessor contains contiguous authoring pressure tests:

```text
OPS-PT-001...470
```

Latest focused ranges cover:

- pilot ceiling / rollback correction;
- post-generation Safety invalidation;
- R249/R300 bundle allocation;
- failed-fulfilment refund survival through deletion;
- payer ≠ recipient failed-fulfilment;
- redeemed third-party ordinary pre-generation refund;
- gift/sponsor/zero-price distinctions;
- duplicate payment/refund reconciliation;
- stale worker / restore / deletion races.

The final independent review disposition is:

```text
PASS WITH NON-BLOCKING CORRECTIONS
COMPRESSION-READY
BLOCKING FINDINGS = 0
```

### Compression correction applied: pre-redemption authority

Historical shorthand such as:

```text
payer/purchaser controls pre-redemption cancellation
```

is **not** current compressed law.

Current compressed rule:

```text
authorised purchaser / sponsor / commercial-order actor
→ controls cancellation under accepted offer

authoritative payer/payment relationship
→ receives settlement/refund
```

### Compression correction applied: deletion/provider settlement

Current compressed rule explicitly proves:

```text
recipient Full Deletion before generation
→ valid ordinary refund durably committed
→ entitlement destroyed
→ deletion may complete
→ provider settlement may remain pending/fail/reconcile afterward
→ account/entitlement never restored
```

This is an unnumbered compression proof case, not a new governed `OPS-PT` identifier.

---

# 22. Superseded working semantics intentionally excluded

The following are historical only and must not be reintroduced as current law:

- `CONFLICT_STOP` / `DO NOT START` statuses from earlier passes;
- GitHub-first sequencing during substantive Pre-JIT;
- current-MVP General Wellness choice timer/countdown;
- `close_unconsumed` Assessment-credit interpretation;
- rollback represented as lowering numeric pilot ceiling below historical exposure;
- immediate exceptional refund solely from actionable `insufficient_information`;
- post-generation failed-fulfilment refund described as if already contained in historical DEC-045;
- refund survival beginning only at Commerce acceptance;
- participant implicitly treated as monetary beneficiary in split-party purchases;
- payer implicitly treated as post-redemption entitlement authority;
- bare payment source treated as pre-redemption cancellation authority;
- external provider settlement treated as prerequisite to deletion completion.

---

# 23. Pre-JIT completion disposition

```text
SUBSTANTIVE PRE-JIT DISCOVERY / ADJUDICATION =
  COMPLETE

INDEPENDENT HOSTILE REVIEW =
  PASS WITH NON-BLOCKING CORRECTIONS

NON-BLOCKING CORRECTIONS =
  APPLIED IN THIS COMPRESSION

BLOCKING PRODUCT / DOMAIN / ARCHITECTURE GAPS =
  0 FOUND AT COMPRESSION ENTRY

CURRENT COMPRESSED CANDIDATE =
  READY FOR GOVERNANCE / REPOSITORY INTEGRATION REVIEW

FORMAL PRODUCT / DECISION PROMOTION =
  REQUIRED BEFORE IMPLEMENTATION

JIT / FEATURE PACK IMPLEMENTATION =
  NOT YET AUTHORISED

GITHUB / PR / ACTIONS =
  NEXT WORKSTREAM ONLY AFTER THIS COMPRESSION IS ACCEPTED
```

---

## 24. Next governed sequence

```text
1. accept/review this compressed current-state candidate
2. restore repository/GitHub canonical-state inspection
3. identify exact authoritative amendment targets and versions
4. promote Product Law / Decision amendments explicitly
5. update affected governed Open Work / operating artifacts
6. re-check authority manifest / repository consistency
7. only then proceed into applicable Feature Pack / JIT entry workflow
```

Do not re-open substantive Pre-JIT discovery without new contradictory evidence, changed Product scope or a failed upstream governance integration.
