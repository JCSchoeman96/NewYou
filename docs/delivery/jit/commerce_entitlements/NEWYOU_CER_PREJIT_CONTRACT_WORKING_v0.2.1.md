# NewYou Commerce / Entitlements / Recurring Membership Pre-JIT Contract — Working v0.2.1

- **Status:** FINAL COMPACT WORKING CONTRACT / NON-AUTHORITATIVE
- **Supersedes:** compact contract `v0.2.0` — provenance/SHA PATCH only; semantic body unchanged
- **Date:** 2026-09-10
- **Detailed source:** `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.3.md`
- **Detailed source SHA-256:** `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`
- **Semantic audit:** `NEWYOU_CER_PREJIT_STABILISATION_AUDIT_WORKING_v0.2.0.md`
- **Mechanical recertification:** `NEWYOU_CER_PREJIT_STABILISATION_MECHANICAL_RECERTIFICATION_v0.2.2.md`
- **Live NewYou baseline:** `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store `main`:** `56f06d028ec38896f5a927f54dc7adfcb20034a3`
- **Store `hardening/subscriptions`:** `54871ef3bdda42f067ed5dbd398305151610c060`
- **Implementation:** NOT AUTHORISED
- **Authority:** NONE

# 1. Use and authority

Use this after current governed NewYou authority. It compresses accepted Pre-JIT evidence only.

It does not amend authority, authorise implementation, promote Store/Paystack state into NewYou law, invent implementation structures, or duplicate HSP/Privacy seams.

# 2. Ownership

**Commerce** owns offer/price/promotion, purchase/payment/refund/dispute/chargeback/excess-collection truth, membership/subscription/add-on commercial lifecycle, future-contract ordering, and provider-evidence reconciliation.

**Entitlements** owns grant/right identity/scope/source/provenance, validity/expiry/revocation, component decomposition, gift/sponsored/complimentary/lifetime grants, redemption, limited-credit consumption, current access, and source-specific target-set convergence.

**Identity & Access** owns canonical Account/grantee identity.

Provider state, queues/workers, caches, PubSub, Analytics, search/UI projections are never business authority.

No separate Membership, Subscription, Gift, Sponsor, Pricing, Promotion, Redemption or Provider Domain is justified.

# 3. Truth layers and provider evidence

Keep distinct:

1. provider observation;
2. Commerce interpretation;
3. Entitlement consequence;
4. execution evidence.

Duplicate execution must not multiply one logical business effect. Event arrival order is not business precedence. Ambiguous external state remains unresolved until authoritative evidence exists. Historical payment plus later refund/reversal can both remain true.

# 4. Stable renewal identity and recovery

One intended renewal has one stable identity across scheduler, retries, provider calls, callbacks, browser return, reconciliation, restart and outage recovery.

**Billing retry is not a new renewal.**

Queued execution re-reads current Commerce authority before irreversible collection.

Recovery derives current target from durable truth, not presumed worker history.

Late verified success for the **same renewal occurrence** retains that occurrence's original scheduled paid-period boundaries; reconciliation time does not start a new full term.

# 5. Failed renewal, grace, suspension, cancellation

Grace is recovery condition, not a paid period. After retry exhaustion, blind automatic retry authority ends; suspension may occur; later success for the same still-authorised renewal may repair suspension.

`CER-UPD-001`: cancellation during failed-renewal grace is immediately effective because prior paid period ended; it withdraws unresolved future-renewal authority. Verified-paid renewal that became authoritative first remains valid; cancellation that became authoritative first prevents later collection from reactivating membership. Late money enters reversal/refund/remedy.

`CER-UPD-006`: pending period-end cancellation can be rescinded before actual termination. Rescission renews unchanged from current live contract and does not resurrect hidden prior future targets.

After actual termination, continuation is a new re-subscription occurrence.

# 6. Future contract ordering and cadence

One uncommitted renewal boundary has one current authoritative future commercial outcome.

Future changes form ordered superseding target-contract versions. Dimension-scoped actions preserve other valid dimensions; cancellation means **do not renew**. Once renewal commits, later actions target another boundary.

Monthly↔annual cadence change is a future renewal instruction by default: preserve current paid period; no automatic refund/credit/truncation/second membership; target the next uncommitted boundary. Immediate conversion requires separately governed money/period semantics.

# 7. Upgrade, downgrade and add-ons

Immediate upgrade is success-gated. Existing paid composition remains authoritative until required adjustment/payment succeeds and target contract remains applicable. Failed/ambiguous upgrade does not revoke/suspend the already-paid lower tier.

Late success revalidates membership, target, price/proration basis and intervening changes.

Downgrades take effect at renewal.

Ordinary add-ons default to one Basic membership composition:
- inherit Basic cadence/boundary unless Product explicitly defines independent billing;
- mid-period activation is success-gated;
- removal is renewal-effective by default;
- dependent add-ons do not outlive Basic;
- Premium is a named bundle over Basic + governed add-ons, not a second opaque entitlement system.

# 8. Price migration and recurring promotion

Public/list/provider price is not existing-member recurring contract.

Higher future price applies only at an eligible uncommitted renewal after exact target price/currency/boundary are durable and applicable notice/contract/legal conditions are satisfied. Already-committed renewal price is immutable.

Grandfathering is explicit offer/occurrence policy.

Recurring promotion defines effect, qualification, duration/consumption, commencement, post-promo price and behavior across package/cadence changes. Cycle-limited promotion consumes on successfully established qualifying paid periods, not attempts/retries. Unused cycles are not generic banked credit.

# 9. Duplicate purchase and excess collection

Provider idempotency handles retries of one occurrence, not two distinct successful purchases.

Concurrent repeated attempts for one canonical grantee's ordinary membership converge to one admitted membership occurrence.

If two genuine collections occur but one membership is admissible, excess money must not create another membership/period/recurring obligation/entitlement; it enters source-scoped reversal/refund/remedy.

Commercial-admission ordering, not callback arrival, determines the valid occurrence.

# 10. Gift, sponsorship and existing-coverage overlap

Purchaser, recipient, participant and canonical grantee remain distinct.

Redemption is a one-time transfer boundary. After redemption, right is bound to canonical grantee; purchaser/sponsor gets only Product-authorised commercial/redemption visibility, not protected participant data/control.

Gifted membership is fixed/prepaid by default. Recurring sponsorship requires explicit payer consent. Sponsor cancellation stops future funding, not an already-funded recipient period.

Duration-based gift/sponsor value does not silently burn concurrently with equivalent already-paid coverage. It begins at next eligible uncovered boundary unless offer explicitly defines fixed-window/immediate-start behavior.

Gift/sponsor-funded equivalent periods suppress overlapping self-paid collection. Open-ended sponsorship does not silently restart personal billing without explicit fallback consent. Gift/sponsor application does not silently rescind existing self-paid cancellation.

# 11. Multi-source Entitlements

Multiple legitimate sources retain independent identity, scope, validity, provenance, revocation and consumption history.

For boolean/scoped access:

`effective access = union of valid qualifying sources`.

Ending one source does not revoke another valid source.

Effective access similarity does **not** rewrite Commerce membership truth.

Distinguish:
- access-overlay grant;
- qualifying membership-coverage grant;
- explicit additive limited-benefit grant.

Only explicit membership-coverage grant may suppress redundant covered future self-billing. Partial grants affect only covered components.

Overlap alone does not multiply limited benefits, credits, continuity clocks or nonaccumulating entitlements. Additional units require explicit additive authority.

No global source hierarchy is authorised.

# 12. Premium continuity and recurring limited benefits

Premium reassessment maturity measures uninterrupted qualifying Premium coverage time for canonical grantee, not charge count, payment method, payer, provider object, cadence or one source.

Seamless qualifying cadence/funding-source transitions preserve continuity if no gap exists. Overlapping qualifying sources count time once and do not accelerate maturity.

Initial annual purchase or switching into annual is not an annual-renewal maturity trigger.

Grace access is provisional until Commerce proves paid Premium period existed.

Premium→Basic, Premium termination or genuine uncovered Premium interval resets continuity.

At most one unused reassessment entitlement exists; missed anniversaries do not bank hidden catch-up entitlements. Unused reassessment expires when qualifying Premium ends even if Basic continues.

Ordinary overlap does not automatically multiply monthly reviews or annual reassessments.

# 13. Refund, dispute and chargeback

Refundability follows Product irreversible-use boundaries. Refund amount is not entitlement authority.

Pending dispute is contested state, not final invalidity; consequences are reversible/source-scoped.

Final reversal may end future rights whose sole source was reversed payment while preserving historical payment/fulfilment/consumption and later independent sources/periods.

“Permanent” once-off access is non-expiring while qualifying purchase remains commercially valid.

No dispute/chargeback alone implies fraud, account-wide ban or unrelated revocation.

# 14. Manual EFT

`DEC-049` manual EFT is NewYou-verified manual payment, not Paystack EFT/Ozow provider channel.

No automatic renewal. Access only after verification.

Ordinary on-demand manual-EFT membership period begins at verification/lawful activation; bank initiation/receipt does not silently start access clock; delayed verification must not shorten purchased duration.

This differs from late reconciliation of an already-existing recurring renewal occurrence.

# 15. Entitlement target-set convergence

Each commercial membership/add-on source has one latest authoritative entitlement target set/version.

Do not depend on grant-before-revoke or revoke-before-grant ordering.

If transition cannot present atomically, incomplete convergence must:
- not grant outside new target;
- preserve rights common to old/new;
- cease removed rights no later than governed boundary;
- begin new rights only after target acceptance.

Duplicate/reordered/stale application cannot produce superseded source state. Recovery derives latest target from durable authority. Other valid sources remain untouched. Caches/projections cannot extend revoked/expired authority.

# 16. Cross-stream seams

Preserve HSP ownership of `HSP-UPD-001`, `HSP-UPD-005`, `HSP-UPD-006`, `HSP-UPD-007`, `HSP-UPD-008`.

Preserve Privacy ownership of `PRIV-WD-002` / `PRIV-UPD-002`.

Late unavoidable financial outcome after Full Deletion may reconcile to truthful Commerce history but must not restore product/Entitlement access.

# 17. Provider boundary

`OQ-004` remains open.

`NewYou semantics → provider-independent invariant → Paystack validation → mechanism`.

Provider facts are evidence only and must be revalidated when implementation depends on them.

# 18. Store reuse

> **REUSE AFTER HARDENING / ADAPTATION REQUIRED**

Strong reusable primitives: provider evidence/dedupe, stable RenewalAttempt identity, PaymentApplication/apply-once, reconciliation, immutable commercial snapshots, generic refund/payment core, source-aware EntitlementGrant identity/validity.

Material gaps: reordered outcomes, suspension/terminal recovery, immutable future-contract ordering, cadence, price migration, recurring promotion, concurrency-safe membership admission, payment-method race, success-gated upgrades, Basic/add-on/Premium composition, gift/sponsor/complimentary/lifetime taxonomy, target-set convergence, multi-source limited-benefit rules, cache/non-authority proof.

NewYou-specific `12 Premium months → reassessment` policy stays outside generic Store.

# 19. Accepted upstream deltas

Exactly `CER-UPD-001...013` are accepted working/non-authoritative inputs.

| Cluster | CER inputs |
|---|---|
| Renewal / cancellation / cadence | `001`, `005`, `006` |
| Price / recurring offer terms | `007`, `008` |
| Wrong / duplicate collection remedy | `009` + relevant part of `001` |
| Gift / add-on / package / multi-source | `003`, `010`, `011`, `013` |
| Disputes / reversal | `002` |
| Manual EFT | `004` |
| Premium continuity | `012` |

Do not mechanically create thirteen governed Decisions.

# 20. Pressure-test disposition

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

Five genuinely new second-pass semantic classes were `CER-PT-016...020`; all other second-pass scenarios refined existing PTs or confirmed coverage.

# 21. Closure

Broad CER semantic discovery is complete at `CER-PT-020`.

No third broad round is recommended.

Implementation details remain JIT/proof concerns unless new evidence exposes a genuine unresolved semantic class or upstream contradiction.
