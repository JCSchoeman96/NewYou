# NewYou Commerce / Entitlements / Recurring Membership Pre-JIT Evidence Index — Working v0.2.1

- **Status:** FINAL COMPACT WORKING EVIDENCE INDEX / NON-AUTHORITATIVE
- **Supersedes:** `v0.2.0` — provenance/SHA PATCH only; evidence mappings unchanged
- **Detailed source:** `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.3.md`
- **Detailed source SHA-256:** `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`
- **Compact contract:** `NEWYOU_CER_PREJIT_CONTRACT_WORKING_v0.2.1.md`
- **Delta register:** `NEWYOU_CER_UPSTREAM_DELTA_REGISTER_WORKING_v0.2.1.md`
- **Live NewYou baseline:** `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`
- **Store `main`:** `56f06d028ec38896f5a927f54dc7adfcb20034a3`
- **Store `hardening/subscriptions`:** `54871ef3bdda42f067ed5dbd398305151610c060`
- **Implementation:** NOT AUTHORISED

# 1. Routing

`README → live NewYou authority → compact contract → delta register as required → evidence index → deep v0.30.3 for exact provenance`.

# 2. Current authority

`PROJECT_NORTH_STAR_AND_MVP_v1.2.1`
→ `00_PLATFORM_v1.3.0`
→ `01_DECISIONS_v1.3.0`
→ `02_OPEN_WORK_v1.2.40`
→ `03_ARCHITECTURE_v1.1.0`
→ `04_DOMAIN_MAP_v1.1.0`
→ `05_ROADMAP_v1.1.0`
→ `PLATFORM_OPERATING_MODEL_v1.0.0`
→ frontend system when relevant.

# 3. Pressure-test index

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

Exactly twenty PT headings are expected: `CER-PT-001...020`.

# 4. Second-pass candidate disposition

| Candidate | Disposition |
|---|---|
| 1 | NEW `CER-PT-016`; `CER-UPD-005` |
| 2 | refine PT-016 / UPD-005 |
| 3 | refine PT-008; `CER-UPD-006` |
| 4 | coverage confirmed; no new PT/UPD |
| 5 | NEW `CER-PT-017`; `CER-UPD-007` |
| 6 | NEW `CER-PT-018`; `CER-UPD-008` |
| 7 | NEW `CER-PT-019`; `CER-UPD-009` |
| 8 | coverage confirmed under PT-003/004/006/015 |
| 9 | coverage confirmed under PT-003/007/008/015 |
| 10 | refine PT-008 |
| 11 | refine PT-011; `CER-UPD-010` |
| 12 | refine PT-012; `CER-UPD-011` |
| 13 | NEW `CER-PT-020`; `CER-UPD-012` |
| 14 | refine PT-001/PT-011/PT-015 |
| 15 | refine PT-011/PT-012/PT-020; `CER-UPD-013` |

# 5. Upstream delta index

`CER-UPD-001...013`; exact accepted policy sections live in the Delta Register.

# 6. HSP / Privacy routes

HSP: `HSP-UPD-001`, `HSP-UPD-005`, `HSP-UPD-006`, `HSP-UPD-007`, `HSP-UPD-008`.

Privacy: `PRIV-WD-002` / `PRIV-UPD-002`.

# 7. Provider / OQ-004

Provider facts remain evidence only. `OQ-004` remains open for exact recurring/webhook/retry/proration/refund/dispute/chargeback/reconciliation behavior.

# 8. Store reuse evidence

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

A future Store runtime-head change requires targeted reuse re-review.

# 9. Certification chain

- semantic stabilisation audit `v0.2.0`: `05d6ac9cac911be98e69c9fd16c2465e04334e7d8dc5af8d983d0d6bcddeb9f7`
- mechanical recertification `v0.2.2`: `8c9e00ab3fb74b8739d1180cfe4b3ef9beb201d4b3c2f38bdb5509daea944af6`
- exact mechanically certified deep source `v0.30.3`: `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`

# 10. Closure

Broad CER is closed at `CER-PT-020`. Do not reopen merely because implementation representation remains undecided.
