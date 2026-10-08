# NewYou Paystack Evidence Index — Working v1.0.2

- **Status:** CURRENT COMPACT INDEX / NON-AUTHORITATIVE / STAGE-RESULT ROUTING PATCH
- **Repository baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **External-source access date:** 2026-10-08
- **Empirically verified provider facts in this pack:** **NONE**

## 1. Current NewYou authority/evidence

| Source | Role |
|---|---|
| `docs/00_platform/README.md` | current authority/navigation route |
| `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` | current authority versions/routing |
| `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` | MVP/commercial boundary |
| `00_PLATFORM_v1.6.0.md` | Paystack launch gateway; commercial payment/refund/dispute/access law |
| `01_DECISIONS_v1.6.0.md` | DEC-292 and OQ-004 status; DEC-300 commercial reversal consequences |
| `02_OPEN_WORK_v1.2.59.md` | current open-work/gate state |
| `03_ARCHITECTURE_v1.1.1.md` | provider ingress, ambiguity, retry/restart, durable reconciliation |
| `04_DOMAIN_MAP_v1.2.0.md` | Commerce/Entitlements/Audit ownership |
| `05_ROADMAP_v1.2.0.md` | FP-002 outcome, OQ-004 gate, recurring deferral, release gates |
| `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` | pending/verifying UX; browser non-authority |
| `PLATFORM_OPERATING_MODEL_v1.0.1.md` | Finance/support work vs business authority |
| `reference/ENGINEERING_STANDARDS_v1.0.1.md` | high-risk financial/provider proof rules |
| FLOW-02 pressure test | end-to-end payment/reconciliation failure model |
| Commerce/Entitlements Pre-JIT | supporting non-authoritative lifecycle pressure evidence |
| Privacy Pre-JIT | provider-retention/disclosure minimisation seams |

## 2. Paystack primary/first-party evidence

All accessed 2026-10-08 unless noted.

| ID | Source | Supports |
|---|---|---|
| PS-001 | https://paystack.com/docs/api/transaction/ | Initialize/Verify, unique reference, amount/currency/status, channels, reusable authorization endpoints |
| PS-002 | https://paystack.com/docs/api/errors/transaction/ | duplicate reference, reference-not-found, payment-session timeout errors |
| PS-003 | https://paystack.com/docs/payments/verify-payments/ | server-side verification and payment status guidance |
| PS-004 | https://paystack.com/docs/payments/webhooks/ | HMAC-SHA512, 200 acknowledgement, live/test retry schedules, callback weakness |
| PS-005 | https://paystack.com/docs/api/webhook-events/ | event history, full payload/server response, cursor pagination, resend behavior |
| PS-006 | https://paystack.com/docs/api/refund/ | Create/List/Fetch/Retry refund, full/partial refund, list pagination |
| PS-007 | https://paystack.com/docs/payments/refunds/ | refund lifecycle and provider transaction/refund relationship |
| PS-008 | https://paystack.com/docs/api/errors/refund/ | insufficient-balance refund failure and other refund errors |
| PS-009 | https://paystack.com/docs/api/dispute/ | dispute listing/status/linkage; evidence fields; upload URL; partial `refund_amount` |
| PS-010 | https://paystack.com/docs/payments/manage-disputes/ | dispute workflow, background detection, receipt/evidence upload, resolution |
| PS-011 | https://paystack.com/docs/api/pagination/ | offset/cursor pagination and best practices; disputes cursor support |
| PS-012 | https://paystack.com/docs/api/rate-limits/ | 429 handling, reset headers, reconciliation batching advice |
| PS-013 | https://paystack.com/docs/api/authentication/ | test/live and secret-key boundary |
| PS-014 | https://paystack.com/docs/payments/metadata/ | metadata/provider visibility |
| PS-015 | https://paystack.com/docs/payments/payment-channels/ | channel capabilities / hosted path |
| PS-016 | https://paystack.com/docs/payments/charge-card/ | raw card API PCI boundary |
| PS-017 | https://paystack.com/docs/payments/test-payments/ | test-mode payment/refund scenarios |
| PS-018 | https://paystack.com/docs/payments/subscriptions/ | provider-managed subscriptions; future recurring only |
| PS-019 | https://paystack.com/docs/payments/recurring-charges/ | reusable authorization behavior; future recurring only |
| PS-020 | https://paystack.com/docs/changelog/api/ | provider API evolution; Sep-2026 Webhook Events addition |
| PS-021 | https://paystack.com/docs/api/settlement/ | settlement lifecycle and paginated settlement/transaction reads |
| PS-022 | https://paystack.com/za/pricing | South-African fee context; fees are not NewYou order truth |
| PS-023 | Paystack first-party SA support on duplicate webhook delivery | operational duplicate-delivery evidence |
| PS-024 | Paystack first-party SA dispute/chargeback support | release-only account/market operating evidence |

## 3. Evidence classification

- **DOCUMENTED FACT** — explicitly stated by current first-party Paystack material.
- **REASONABLE INTERPRETATION** — conservative NewYou integration consequence derived from authority + provider contract; not a provider guarantee.
- **ASSUMPTION** — unproven premise; cannot become implementation fact.
- **UNKNOWN** — current docs/evidence do not establish the behavior.
- **EMPIRICALLY VERIFIED** — observed in a controlled experiment with captured evidence. **None yet.**

## 4. Five final documentary-delta findings

| Finding | Nature | Disposition |
|---|---|---|
| Hidden HTTP/SDK/proxy retry can invalidate mutation ambiguity handling | NewYou threat model; not a Paystack documented guarantee | PAY-INV-024; EV-050/051 |
| Unknown future provider values must fail closed | NewYou forward-compatibility requirement; provider API demonstrably evolves | PAY-INV-025; EV-052 |
| Paystack can reject refund for insufficient balance | DOCUMENTED FACT | PAY-INV-026; EV-053 |
| Dispute evidence API accepts customer contact/service details and uploaded receipt/evidence | DOCUMENTED FACT | PAY-INV-027; EV-054 minimisation contract |
| Paystack reads are paginated/rate-limited and disputes support cursor pagination | DOCUMENTED FACT | PAY-INV-028; EV-055 |

## 5. Critical documentary unknowns that remain empirical

- read-after-write visibility boundary after ambiguous Initialize;
- exact safe replacement rule when old checkout may remain payable;
- duplicate/ambiguous Create Refund behavior;
- refund/dispute cross-correction behavior;
- controlled-live South-African account/channel/dispute/settlement behavior.

These are intentionally not resolved by additional generic reading.

## 6. Empirical routing provenance

The v1.0.2 stage-result recording patch adds no new Paystack documentary claim. It separates:

- **Wave** — risk/dependency execution order;
- **Execution Stage** — where the case can truthfully execute;
- **Gate Effect** — what the result can block.

`NEWYOU_PAYSTACK_EMPIRICAL_MANIFEST_WORKING_v1.0.2.md` is the current operational routing/result projection. It records current disposition per execution stage; it does not collapse multi-stage cases into one status. `deep/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.11.0.md` remains the detailed case-definition/provenance source. A provider-only harness result cannot satisfy an `PHASE8_*` or `RELEASE_*` stage.
