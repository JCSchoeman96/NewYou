# NewYou Paystack / OQ-004 Provider Validation Pre-JIT — Append-Only Working Record v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE / EMPIRICAL VALIDATION OUTSTANDING
- **Document version:** `v0.1.0`
- **Created:** 2026-10-08
- **Repository baseline:** `JCSchoeman96/NewYou` `main` at `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Purpose:** single cumulative working record for the bounded Paystack / `OQ-004` Provider Validation Pre-JIT stream.
- **Authority:** NONE. Live governed NewYou Product / Architecture / Domain / Roadmap / Open Work and later approved Feature Pack/JIT authority always win.
- **Implementation:** NOT AUTHORISED.
- **Empirical status:** no Paystack sandbox/live validation case is claimed executed in this baseline.

## Append-only / SemVer operating rule

This stream uses immutable historical versions and append-only successors.

1. A published `_WORKING_vX.Y.Z.md` file is never rewritten to change prior reasoning.
2. A successor copies the entire predecessor byte-for-byte as its prefix, then appends a new SemVer pass section.
3. Corrections do not erase earlier claims. A later section names the prior statement, explains the correction, and marks its effective disposition.
4. `PATCH` adds provenance, evidence, wording hygiene or test detail without changing a working semantic conclusion.
5. `MINOR` adds/refines provider-validation semantics, pressure tests, lifecycle interpretation, candidate upstream deltas or closure obligations without claiming governed authority.
6. `MAJOR` is reserved for a deliberate working-model reset after an upstream governed authority change or a provider finding that invalidates the core validation model.
7. Provider documentation, interpretation, assumption, unknown and empirical result remain separately labelled.
8. No working finding creates Product Law, Architecture Law, Domain Law, Roadmap law, an OQ, a Feature Pack, an Ash Resource or implementation permission.

## v0.1.0 import manifest

The v0.1.0 cumulative baseline imports the six first-pass artifacts exactly as they existed after the first validation pass. Their original internal version labels are intentionally preserved as historical evidence.

| Imported artifact | Role | SHA-256 |
|---|---|---|
| `README.md` | First-pass pack README | `219465cdc548da808047adfea6d1f69a0f1266ef1cc23c1a3a86457f9a670250` |
| `NEWYOU_PAYSTACK_VALIDATION_CONTRACT_WORKING_v0.1.0.md` | Provider-independent invariant/validation contract | `5bccfdfc44ef9f6a49b90af402642c562ff9886cfa0e6f92452f2d82537bba1a` |
| `NEWYOU_PAYSTACK_SCENARIO_MATRIX_WORKING_v0.1.0.md` | Scenario matrix | `f69b1e10cad8a4b3ff15181ba6776d28a1f3afd61711746292ebf2e1f66aba10` |
| `NEWYOU_PAYSTACK_EMPIRICAL_VALIDATION_WORKING_v0.1.0.md` | Empirical validation plan | `027bce29ee154062f26285d4f66638e172e3af08f0cf3be720e12f03215e7822` |
| `NEWYOU_PAYSTACK_GAP_REGISTER_WORKING_v0.1.0.md` | Gap register | `1fb0b25da96316d456a8cb00e6a3076e55c1ba2db9fbed5ed468fcfd38c56af9` |
| `NEWYOU_PAYSTACK_EVIDENCE_INDEX_WORKING_v0.1.0.md` | Evidence index | `acef474c1b48f034527f60452a899063e0e620ca7fa80e86b2ec2470d9977c2a` |

## v0.1.0 disposition

`OQ-004 BLOCKED ON EMPIRICAL TESTS`.

Documentary evidence indicates that FP-002 one-off payment reconciliation is plausible behind NewYou-owned authority and reconciliation, but critical ambiguity cases are not yet empirically proven. The global OQ-004 wording is broader than FP-002 because it also names subscription/proration behaviour.

---

# Imported v0.1.0 first-pass artifacts



<!-- IMPORT START: README.md -->

# NewYou Paystack / OQ-004 Provider Validation Pre-JIT

- **Status:** WORKING / NON-AUTHORITATIVE / PROVIDER VALIDATION EVIDENCE
- **Repository baseline:** `JCSchoeman96/NewYou` `main` @ `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Evidence access date:** 2026-10-08
- **Implementation:** NOT AUTHORISED
- **Repository mutation:** NONE — this pack was produced outside the repository for review.

## Purpose

This pack answers one bounded question:

> Can current Paystack behaviour safely support the provider-independent NewYou payment invariants required by FP-002, without turning browser/provider state into NewYou commercial or access authority?

The required direction is:

```text
NewYou semantics
→ provider-independent invariant
→ Paystack documented / empirical evidence
→ safe integration mechanism
```

Never reverse this into `Paystack API shape → NewYou Product Law`.

## Authority boundary

Live NewYou authority wins over every statement in this pack. The current live route inspected at the pinned baseline is:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when UI/public experience is relevant
10. Current reference evidence, including `REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md` and certified `reference/ENGINEERING_STANDARDS_v1.0.1.md`.

Current Product Law locks Paystack as the first/launch gateway but leaves provider retry, subscription, webhook, proration, refund, dispute/chargeback and related provider behaviour gated. Commerce remains payment/refund/dispute authority; Entitlements remains access authority.

## Scope result

### FP-002 now

The documentary evidence supports the architecture **only with NewYou reconciliation**. Paystack provides:

- unique transaction references;
- server-side transaction verification by reference;
- amount/currency/status evidence;
- signed webhooks with retry behaviour;
- webhook event history/resend tooling;
- partial/full refunds and refund status APIs/events;
- dispute APIs/events;
- ZAR support.

However, two FP-002-critical ambiguous-operation cases remain unproven empirically:

1. **transaction initialization timeout** — duplicate initialization with the same reference is an error, not documented idempotent replay; exact visibility/consistency timing through Verify after an ambiguous initialize must be tested;
2. **refund creation timeout** — Create Refund exposes no documented idempotency key and duplicate-request semantics are not documented; reconciliation through List/Fetch Refunds must be proven before any retry policy is fixed.

### Future recurring only

Paystack-managed Subscriptions explicitly do not retry a failed charge in the same billing cycle. That mechanism therefore does not, by itself, implement NewYou's 72-hour provider-safe failed-payment retry lifecycle. Paystack reusable authorizations may provide a lower-level mechanism, but that future recurring architecture is deliberately not selected here.

## Current disposition

**OQ-004 BLOCKED ON EMPIRICAL TESTS.**

Documentary provider compatibility is promising for FP-002. No FP-002 provider mismatch has been proven. Critical sandbox experiments remain `NOT_EXECUTED` because no Paystack sandbox credentials/provider test harness were available in this validation session.

There is also a governance point: current OQ-004 wording is broader than FP-002 and includes subscription/proration behaviour, while current Roadmap explicitly defers recurring membership from FP-002. Do not mark the global OQ `COMPLETE` while those broader clauses remain unvalidated unless current authority explicitly splits/narrows the gate or records a scoped FP-002 disposition without silently changing the Decision Register meaning.

## Read order

1. `NEWYOU_PAYSTACK_VALIDATION_CONTRACT_WORKING_v0.1.0.md`
2. `NEWYOU_PAYSTACK_SCENARIO_MATRIX_WORKING_v0.1.0.md`
3. `NEWYOU_PAYSTACK_EMPIRICAL_VALIDATION_WORKING_v0.1.0.md`
4. `NEWYOU_PAYSTACK_GAP_REGISTER_WORKING_v0.1.0.md`
5. `NEWYOU_PAYSTACK_EVIDENCE_INDEX_WORKING_v0.1.0.md`


<!-- IMPORT END: README.md -->


<!-- IMPORT START: NEWYOU_PAYSTACK_VALIDATION_CONTRACT_WORKING_v0.1.0.md -->

# NewYou Paystack Validation Contract — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE
- **Purpose:** Provider-independent invariants → Paystack evidence → safe mechanism
- **Implementation:** NOT AUTHORISED

## 1. Current NewYou payment authority extracted before provider mapping

The following identifiers are local to this working validation pack only. They are **not governed NewYou identifiers** and must not be promoted into Product/Architecture/Domain authority without normal governance.

| ID | Provider-independent NewYou invariant | Current authority basis | Consequence if provider cannot support it | Provider evidence needed | Proof level | Classification |
|---|---|---|---|---|---|---|
| PAY-INV-001 | Commerce alone establishes payment/refund/dispute/reversal truth. Browser, webhook, provider dashboard and API responses are evidence only. | Product §21R; Domain Map Commerce; FLOW-02; Architecture provider ingress | Provider cannot be safely used if NewYou must accept provider state as business authority. | Server-verifiable current transaction/refund/dispute evidence. | Docs + sandbox | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-002 | Entitlements alone establishes current access. A provider success event must not directly grant access. | Domain Map Commerce→Entitlements; Roadmap FP-002; FLOW-02 | Duplicate or forged provider evidence could multiply access. | Stable transaction evidence sufficient to reconcile Commerce, then an independent idempotent access consequence. | Docs + NewYou proof | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-003 | One NewYou purchase intent/commercial obligation has NewYou-owned identity. A Paystack reference identifies a provider transaction attempt; it must not become NewYou commercial identity. | Architecture idempotency doctrine; CER Pre-JIT; FLOW-02 | Retry/second reference can accidentally create a second purchase or entitlement. | Ability to supply/persist a unique provider reference and later query it. | Docs + sandbox | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-004 | A transport timeout or ambiguous acknowledgement is `unknown/unresolved`, not failure and not success. No blind consequential retry. | Architecture §§8, provider failure doctrine; Engineering Standards; FLOW-02 | Duplicate charge or fabricated failure/success. | Deterministic lookup/reconciliation path after ambiguous request. | Sandbox REQUIRED | EMPIRICAL_VALIDATION_REQUIRED |
| PAY-INV-005 | Browser return/navigation never creates authoritative payment truth or entitlement. | Frontend §5.3; Product §21R; FLOW-02 | Forged/replayed URL or missing callback could create/lose access. | Callback/reference can be independently verified server-side; recovery does not require browser return. | Docs sufficient for provider capability; NewYou proof for enforcement | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-006 | Provider evidence must be authenticated where applicable and bound to a known NewYou provider attempt before it can affect Commerce. | Architecture provider ingress; Engineering Standards | Forged webhook/replay can create false payment evidence. | HMAC-signed webhook; transaction reference/id; server-side API authentication. | Docs + sandbox | SUPPORTED_BY_PROVIDER |
| PAY-INV-007 | Duplicate, retried, replayed or reordered provider evidence cannot create a second payment effect or second entitlement effect. | Product checkout-abuse rule; Architecture idempotency; FLOW-02 | Double fulfilment / financial inconsistency. | Provider explicitly allows/retries duplicate delivery; NewYou can verify current state by reference. | Docs + sandbox/NewYou proof | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-008 | NewYou must reconcile successful payment after browser loss, webhook loss, worker/node restart or DB/API interruption. | Architecture restart/recovery; FLOW-02; Roadmap FP-002 | Paid customer can remain permanently unpaid/unentitled or be charged twice. | Verify Transaction by stable reference; durable NewYou attempt identity. | Docs + sandbox + restart proof | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-009 | `success` is valid payment evidence only when the provider transaction matches the expected NewYou reference, accepted amount and currency; environment must be the intended one. | FP-002 exact price/entitlement contract; Product order snapshot; Architecture correctness-over-convenience | Amount/currency manipulation creates under/over-paid entitlement. | Verify/webhook fields: reference, amount, currency, status/domain. | Docs + negative test | SUPPORTED_BY_PROVIDER |
| PAY-INV-010 | Provider states are not copied directly into NewYou payment states. Inconclusive states remain pending/reconciliation-required; reversal evidence is a separate correction/reversal concern. | Domain Map; Engineering Standards independent lifecycle rule; Product §21R | Provider operational vocabulary becomes hidden Product Law. | Documented transaction/refund/dispute status vocabularies and lookup APIs. | Docs | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-011 | Refund truth is separate from original payment truth and from entitlement consequence. Full/partial refunds use the accepted NewYou order/component allocation snapshot, not current prices. | Product §21R; Roadmap FP-002 hardening contract | Refund could erase history or revoke unrelated rights. | Full/partial refund, refund status, transaction linkage, amount/currency, webhook/API reconciliation. | Docs + sandbox | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-012 | Refund initiation ambiguity cannot be resolved by blind duplicate POST. | Architecture ambiguity doctrine; financial HIGH proof | Duplicate/stacked partial refunds or unclear customer remedy. | Ability to discover refund records by transaction and inspect status after an ambiguous Create Refund call. | Sandbox REQUIRED | EMPIRICAL_VALIDATION_REQUIRED |
| PAY-INV-013 | Dispute/chargeback/reversal evidence is source-scoped and correctable; it must not imply account-wide fraud or erase historical fulfilment. | Product §21R; CER Pre-JIT | Provider dispute state could silently become Identity/access policy. | Dispute API/events linked to transaction; current transaction/reversal evidence. | Docs + later operational confirmation | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-014 | Paystack customer identity/email/customer_code is never NewYou Identity authority. | Domain Map IAM/Commerce boundary; Product purchaser/recipient separation | Email/customer merges or changes can mis-assign purchases. | NewYou-owned purchase binding must work without trusting provider customer as account authority. | Architecture/NewYou proof; provider docs informative | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-015 | NewYou stores amount in currency minor units and ZAR payment evidence must reconcile exactly to the accepted customer charge. Provider fees are not silently substituted for order price. | Product SA/ZAR launch; FP-002 authoritative-price exit condition | Rounding, fee or currency mismatch creates invalid payment truth. | ZAR subunit/minimum; amount/currency/fees fields. | Docs + sandbox | SUPPORTED_BY_PROVIDER |
| PAY-INV-016 | Secret keys remain server-side; raw card credentials should not transit NewYou systems unless separately justified/compliance-approved. Provider metadata is minimum necessary. | Architecture external-provider boundary; Privacy minimisation; Engineering Standards leakage rules | Secret/card-data exposure materially expands security/compliance risk. | Public/secret key roles; hosted Checkout/Inline capability; PCI warning on raw Card API. | Docs + security review | SUPPORTED_BY_PROVIDER |
| PAY-INV-017 | Webhook acknowledgement must not mean “business consequence completed.” NewYou must authenticate and durably accept evidence, then reconcile asynchronously/repeat-safely. | Architecture provider ingress; Oban/durability doctrine | 200-before-durable-receipt can lose evidence; doing long business work before 200 causes retries. | Signature verification and retry/ack behaviour. | Docs + sandbox/failure injection | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-018 | Provider/API unavailability degrades to pending/unresolved/refused, never fabricated success. Durable unresolved obligations survive restart and backlog. | Architecture degradation/restart doctrine; Engineering Standards | Outage creates duplicate charge or false entitlement. | Verify endpoint + webhook history/resend provide later recovery evidence; rate limits known. | Docs + failure/recovery proof | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| PAY-INV-019 | Provider evidence/audit retention must be sufficient for financial support/reconciliation but must not become a shadow identity/health store. | Privacy Pre-JIT; Audit & Evidence Domain | Over-retention leaks sensitive data or reconstructs deleted product authority. | Payload fields/metadata visibility known; exact retention remains NewYou Privacy/JIT policy. | Docs + Privacy JIT | NEWYOU_POLICY_DECISION |
| PAY-INV-020 | Recurring-payment mechanics must remain separate from FP-002 one-off payment unless the current Roadmap explicitly pulls them in. | Roadmap FP-002 deferred scope; CER Pre-JIT | Future subscription mechanics can contaminate first paid slice or force wrong architecture. | Documentary recurring evidence only for future CER; no implementation selection. | Docs only now | FUTURE_RECURRING_ONLY |

## 2. Paystack capability map after invariant extraction

| Capability | Current provider evidence | Safe NewYou mechanism | Status |
|---|---|---|---|
| Initialize transaction | Backend Initialize accepts amount/email/currency/reference; reference must be unique; duplicate reference errors. | Persist NewYou purchase + one provider-attempt reference before request. Treat timeout as unresolved; reconcile same reference before considering a distinct attempt. | EMPIRICAL_VALIDATION_REQUIRED |
| Browser callback | Redirect callback returns a transaction reference; callbacks may fail because client/network can disappear. | Browser return only asks NewYou to re-read/reconcile current purchase. Never grant access from query parameters. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Webhook authenticity | `x-paystack-signature` = HMAC-SHA512 over payload using secret key; documented source IPs are an additional control. | Verify signature before durable acceptance. IP allowlisting may supplement but must not replace signature. | SUPPORTED_BY_PROVIDER |
| Webhook delivery | No 200 → live retries; Webhook Events API records/resends; resend explicitly non-idempotent. | Treat at-least-once, unordered evidence as normal. Business consequence dedupes at Commerce/Entitlements boundary. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Verify transaction | Server-side Verify by reference returns transaction status, amount, currency, customer, authorization, fees/timestamps. | Primary reconciliation query after callback/webhook/timeout and periodic recovery. | SUPPORTED_BY_PROVIDER |
| No-webhook recovery | Verify works independently of browser/webhook; Webhook Events API additionally exposes delivery history. | Durable reconciliation worker can discover truth later from reference. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Refunds | Full/partial Create Refund; List by transaction; Fetch by refund ID; lifecycle statuses/events. | Separate Refund lifecycle linked to payment; reconcile API + webhook. Never conflate `processed` with entitlement policy. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Refund POST ambiguity | Create Refund has no documented idempotency key/operation reference and no documented duplicate semantics. | On timeout, query refunds for source transaction; do not re-POST until reconciled. Exact behavior requires sandbox proof. | EMPIRICAL_VALIDATION_REQUIRED |
| Disputes | List/fetch transaction disputes; dispute create/remind/resolve events; resolution workflow. | Commerce records dispute/reversal truth; Entitlements applies source-specific current-access policy. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| ZAR/minor units | ZAR cent, SA availability, R1 minimum documented. | Store/compare accepted amount in integer cents. | SUPPORTED_BY_PROVIDER |
| Customer identity | Provider exposes customer id/code/email, but no NewYou identity semantics. | Persist only provider identifiers needed for evidence/recurring seam; IAM remains canonical. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Hosted payment/security | Public key only for frontend Inline/Mobile; secret server-side; custom raw Card API only for PCI-DSS-compliant businesses. | Prefer provider-hosted/approved UI path for FP-002; keep PAN/CVV out of NewYou. Exact PCI scope requires separate compliance assessment. | SUPPORTED_BY_PROVIDER |
| Test mode | Separate test/live keys; test mode aims to mirror live but not all features; no settlements; some channels unavailable. | Run deterministic provider behavior tests in sandbox; production smoke/operational evidence remains separate. | RELEASE_ONLY for production equivalence |
| Provider-managed Subscriptions | Failed subscription charge is not retried in-cycle; Paystack tries again at next payment date. | Do not equate this mechanism with NewYou 72-hour retry lifecycle. Future recurring architecture must decide provider-managed vs NewYou-managed collection. | PROVIDER_LIMITATION / FUTURE_RECURRING_ONLY |
| Proration | No first-party proration primitive was found in current subscription documentation. | Do not assume provider-supported proration. Future recurring/commercial JIT must prove or explicitly design the adjustment mechanism. | DOCUMENTATION_AMBIGUOUS / FUTURE_RECURRING_ONLY |


## 2.1 Evidence identifiers to retain (conceptual, not schema design)

For FP-002 recovery, NewYou needs enough durable linkage to re-run reconciliation after restart without depending on browser state or a provider dashboard. At minimum the JIT design must be able to relate:

- the NewYou purchase/checkout obligation identity;
- the NewYou provider-attempt identity;
- the Paystack transaction `reference` supplied/accepted for that attempt;
- the Paystack numeric transaction `id` once known;
- expected accepted amount in integer minor units and currency;
- observed provider status and material timestamps/channel as evidence;
- refund id(s), source transaction id/reference, refund amount/currency/status when refunds exist;
- dispute id and source transaction linkage when disputes exist;
- provider webhook/event identifiers when available as delivery evidence, **without making event id the business idempotency identity**.

The exact Resource/field schema remains JIT. Authorization codes/payment-instrument details are **not required for FP-002 one-off payment** and belong to future recurring/payment-method design if later selected.

## 2.2 Transaction-initialization adversarial cases

| Pressure | Safe interpretation | Classification |
|---|---|---|
| Client retries checkout UI after a server timeout | Same NewYou purchase intent must re-read its current provider-attempt/reconciliation state rather than automatically create another Paystack transaction. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Server loses Initialize response after request may have reached Paystack | Provider-attempt outcome is unresolved; Verify same stored reference before any new attempt. | EMPIRICAL_VALIDATION_REQUIRED |
| Same Paystack reference submitted twice | Paystack documents duplicate-reference error; never treat second POST as a guaranteed idempotent replay response. | SUPPORTED_BY_PROVIDER |
| Different Paystack references created for the same unresolved NewYou purchase intent | Two payable provider attempts can exist; NewYou commercial admission must prevent two valid payment/access effects and should avoid creating the second until the first is lawfully resolved/abandoned. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Two concurrent NewYou checkout submissions for one ordinary purchase obligation | Provider idempotency cannot solve NewYou duplicate-purchase admission. Commerce must preserve one admitted commercial obligation or explicitly treat excess collection as remedy/refund, never as second entitlement. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |

## 2.3 Provider customer identity pressure

| Case | Safe NewYou rule | Classification |
|---|---|---|
| Same provider email appears in more than one historical/customer object | Do not use provider email/customer object as canonical Account identity. Bind transaction to the NewYou-owned purchase/provider attempt. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| NewYou Account email changes | Historical Paystack transaction/customer evidence remains historical provider evidence; it does not rename or split the NewYou identity. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Paystack creates/retains duplicate customer records | Operational duplication must not create duplicate NewYou Accounts, purchases or entitlements. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| NewYou identity reconciliation/merge occurs | Commerce follows current Identity & Access authority/lineage; provider customer codes are evidence references only. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Payer enters/uses a different payment email | Do not infer purchaser/recipient/participant identity from Paystack customer email. Whether such a payment is admitted is a NewYou checkout/JIT policy decision; successful money evidence still must bind to the intended NewYou purchase. | NEWYOU_POLICY_DECISION |
| Guest-like provider customer exists | Provider-side customer existence does not create a NewYou Account or entitlement. | SUPPORTED_WITH_NEWYOU_RECONCILIATION |

## 2.4 Amount / currency integrity details

- Paystack documents ZAR as cent-denominated and available in South Africa, with a R1.00 minimum.
- Current launch prices are well above that minimum.
- Paystack's transaction error documentation states a generic maximum of `10,000,000` for supported currencies, but the wording does not make the unit/market semantics clear enough to encode as a NewYou Product limit. Current FP-002 prices do not approach it; treat provider maximum as `DOCUMENTATION_AMBIGUOUS` until a concrete need arises.
- Discounts/promotions must be resolved into the **accepted NewYou order price snapshot before Initialize**. Paystack must be asked to collect that accepted amount; a later provider success for another amount/currency is invalid evidence for that purchase.
- Paystack fees/settlement amounts are separate provider/accounting evidence. They must not silently redefine the customer-facing accepted order amount. If NewYou ever passes provider fees to the customer, that final customer charge must be explicit NewYou commercial truth before provider initialization.

## 3. Paystack transaction evidence-state matrix

These are **NewYou interpretations of provider evidence**, not NewYou state names.

| Paystack evidence/status | Provider meaning | NewYou interpretation | Safe action |
|---|---|---|---|
| `success` | Transaction successfully processed. | Conclusive success evidence only after reference + amount + currency + expected environment match. | Reconcile Commerce paid once; enqueue/execute one idempotent Entitlements consequence. |
| `failed` | Transaction failed. | Failure evidence for this provider attempt; never entitlement. | Mark/reconcile attempt failed according to Commerce lifecycle; a new attempt is a separate governed action. |
| `abandoned` | Customer has not completed transaction. | No success; likely terminal/abandoned provider attempt, but do not use this to infer cancellation of NewYou purchase intent. | No entitlement; allow governed retry/new attempt only under Commerce rules. |
| `ongoing` | Customer action still underway. | Inconclusive. | Pending; re-query later. |
| `pending` | Transaction in progress. | Inconclusive. | Pending; re-query later. |
| `processing` | Pending-like for direct debit. | Inconclusive/provider operational. | Pending; re-query later. |
| `queued` | Queued for bulk charge processing. | Provider-only operational state; not FP-002 normal path. | Do not treat as payment. |
| `reversed` | Refunded or a chargeback was successfully logged. | Historical payment/reversal evidence; not “payment never existed.” Requires refund/dispute reconciliation. | Reconcile reversal/dispute dimension; apply source-scoped entitlement consequence only from Commerce policy. |
| unknown reference after ordinary known-nonexistent input | No transaction found. | Invalid/mismatched evidence. | Reject as payment evidence. |
| unknown reference immediately after ambiguous Initialize timeout | No transaction currently found. | **Still inconclusive until empirically proven safe recovery boundary.** | Keep unresolved; bounded verify/reconciliation; do not create a new reference blindly. |
| signed `charge.success` webhook | Authenticated provider event claiming successful charge. | Strong success evidence but still not NewYou payment truth. | Bind to known attempt and validate amount/currency/reference; optionally Verify current transaction state as reconciliation source before authoritative transition. |
| browser reference/query | Client-visible provider reference. | Untrusted trigger/evidence pointer only. | Look up known NewYou attempt and server-verify. |

## 4. Lifecycle pressure-test model

These are conceptual dimensions, **not proposed Ash enums/Resources**.

### 4.1 Purchase/order intent — Commerce-owned commercial intent

- Conceptual states: `created/open → payment_unresolved → commercially_resolved` or `cancelled/expired` only where existing Product/Commerce law permits.
- Guard: one logical purchase intent must not become two purchases merely because two transport attempts exist.
- Idempotency identity: NewYou purchase/checkout obligation, not Paystack reference.
- Retry: a new provider attempt is allowed only after Commerce decides it is safe; timeout is not that decision.
- Recovery: durable purchase survives restart and points to provider attempts/evidence.
- Terminality: commercial intent terminality is NewYou law, never inferred from a browser closing.

### 4.2 Provider attempt — evidence-generating external operation

- Conceptual states: `not_sent`, `initialization_unknown`, `initialized`, `customer_in_progress`, `provider_inconclusive`, `success_evidence`, `failure/abandonment_evidence`, `reversal_evidence`.
- Guards: reference unique; one attempt reference never reused for a distinct purchase; same commercial intent may have multiple attempts only under explicit Commerce admission.
- Side effects: external Paystack transaction/session only.
- Terminality: `success` is not globally terminal because later refund/dispute/reversal may occur; those are separate dimensions/evidence.
- Restart recovery: Verify by stored reference.

### 4.3 Provider evidence — not a business lifecycle

- Stages: `received → authenticity_checked → durably_accepted → semantically_validated → reconciled`.
- Invalid branches: forged signature, unknown reference, amount mismatch, currency mismatch, wrong environment.
- Replays/duplicates: valid evidence may repeat; it must not repeat the business consequence.
- ACK rule: signature/authenticity + durable receipt first, business reconciliation asynchronously; a 200 does not mean Commerce paid.

### 4.4 Reconciled payment truth — Commerce

- Conceptual states: `unresolved/pending`, `paid`, `failed/closed-for-that-attempt`; later refund/dispute/reversal exists as an independent commercial dimension/history.
- Transition to paid guard: known purchase/attempt, authenticated/current provider evidence, `success`, exact reference, amount, currency, intended environment; transition remains idempotent.
- Concurrency: callback, webhook, polling/reconciliation may race. Database/business invariant must converge to one paid consequence.
- Correction: later reversal/refund does not overwrite historical paid fact; it adds current commercial correction/reversal truth.

### 4.5 Entitlement — Entitlements

- Payment does not create access directly.
- Durable consequence from authoritative Commerce transition requests the source-specific entitlement target.
- Duplicate/reordered workers cannot produce a second valid grant.
- Restart: entitlement convergence derives current Commerce/source authority, not remembered worker completion.
- Ending/reversing one source must not revoke independent valid sources.

### 4.6 Refund — Commerce, independent of payment acquisition

- Provider lifecycle evidence: `pending → processing → needs-attention / failed / processed`.
- NewYou refund request/decision and provider refund attempt are distinct.
- `failed` refund does not undo original paid truth; `processed` supplies reversal/refund evidence.
- Partial/full amount is reconciled against the accepted NewYou component/order snapshot.
- Create Refund timeout remains unresolved until refund list/fetch evidence establishes whether Paystack created it.

### 4.7 Dispute / chargeback — Commerce, independent contested-state dimension

- Provider statuses/events are evidence (`charge.dispute.create/remind/resolve`, API status vocabulary).
- A pending dispute is not automatically fraud, account cancellation or historical erasure.
- NewYou access consequence follows current Product law: confirmed dispute may suspend source access; restored payment restores idempotently; final lost chargeback revokes current access while preserving history.
- Out-of-order arrival is interpreted against current/history, not event order.

## 5. Security boundary

1. Prefer Paystack-hosted/approved Checkout/Inline rather than raw card API for FP-002.
2. Never expose secret key to browser; use server-side API calls over verified TLS.
3. Verify webhook HMAC-SHA512 before accepting evidence; IP allowlisting is defence-in-depth, not business identity.
4. Treat browser parameters as attacker-controlled even when generated by Paystack.
5. Metadata is provider-visible and may surface in Dashboard; use opaque NewYou IDs only where necessary. Do not send health data, assessment results, private plan information or secrets.
6. Persist only provider identifiers/evidence needed for reconciliation/support/legal retention under Privacy authority.
7. Do not make an exact PCI-scope claim here. Paystack's custom card API requires PCI DSS compliance; hosted provider UI is the safer scope-minimising direction.

## 6. Availability / degraded-operation contract

| Failure | Safe NewYou behavior |
|---|---|
| Paystack Initialize unavailable | No payment success; keep purchase open/pending as law permits; no entitlement. |
| Initialize timeout | Persist unresolved provider attempt; Verify same reference; do not create a new provider transaction blindly. |
| Browser disappears | Reconciliation continues from durable reference + webhook/API. |
| Webhook endpoint outage | Paystack retries; NewYou later verifies and may inspect/resend event history. |
| Queue/worker outage | Durable evidence remains; backlog reconciliation after recovery; no access fabricated. |
| DB unavailable after provider success | Provider success remains external evidence; on DB recovery Verify same reference and reconcile once. |
| App restart | Recover purchase/provider attempt from PostgreSQL and Verify current provider state. |
| Temporary API inconsistency | Keep unresolved; bounded retries/reconciliation; never downgrade unknown to failed or paid. |
| Reconciliation backlog | Throughput/freshness may degrade; financial/entitlement invariants cannot. |

## 7. Sandbox vs production classification

| Behaviour | Test mode | Production confirmation |
|---|---|---|
| Initialize/Verify/reference uniqueness | Safe/required to validate in test mode. | Small live smoke before paid pilot. |
| Duplicate same-reference initialization | Safe/required in test mode. | Docs sufficient unless behavior differs during live smoke. |
| Browser callback ordering/loss | Safe in test harness. | No special production dependency. |
| HMAC verification / forged webhook rejection | Safe locally/test mode. | Live webhook smoke required before paid pilot. |
| Webhook duplicate/resend/replay | Webhook Events API/test mode suitable. | Live retry schedule is documented; production resilience still operationally observed. |
| Webhook 500/retry timing | Safe in test mode, but test and live retry schedules differ by docs. | Live behavior should not be deliberately abused; rely on documented live schedule + operational telemetry. |
| Verify eventual visibility after ambiguous initialization | **Critical test-mode experiment.** | Controlled live confirmation if test evidence cannot establish parity. |
| Full/partial refund lifecycle | Test cards explicitly support refund scenarios. | Controlled live refund smoke before general release where operationally acceptable. |
| Refund Create timeout/duplicate semantics | **Critical sandbox experiment with fault injection.** | Production confirmation only if sandbox behavior proves non-representative. |
| Dispute/chargeback lifecycle | API/event contract documented; sandbox may not reproduce real bank dispute lifecycle. | Controlled launch/operations confirmation; FP-006/release evidence. |
| Settlements | Not available in test mode. | RELEASE_ONLY; not FP-002 access authority. |
| Rate/load behavior | Test mode explicitly not for load testing. | Phase 8/HH using controlled provider-bound budgets; do not load-test Paystack irresponsibly. |
| Recurring subscriptions | Can test mechanics, but not an FP-002 requirement. | FUTURE_RECURRING_ONLY. |


<!-- IMPORT END: NEWYOU_PAYSTACK_VALIDATION_CONTRACT_WORKING_v0.1.0.md -->


<!-- IMPORT START: NEWYOU_PAYSTACK_SCENARIO_MATRIX_WORKING_v0.1.0.md -->

# NewYou Paystack Scenario Matrix — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE
- **Rule:** Browser/webhook/API are evidence. Commerce owns payment/refund/dispute truth. Entitlements owns access.

| Scenario | Browser evidence | Webhook evidence | Verify/API evidence | NewYou safe interpretation | Required action | Classification |
|---|---|---|---|---|---|---|
| ordinary successful payment | May return reference | `charge.success` may arrive | Verify = `success`, expected reference/amount/currency | Strong provider success evidence; not yet entitlement | Reconcile Commerce paid once → one idempotent Entitlements consequence | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| browser never returns | None | May arrive | Verify can discover by stored reference | Browser absence says nothing about payment truth | Reconcile without browser | SUPPORTED_BY_PROVIDER |
| webhook delayed | May return first | Later success event | Verify may already say success | Arrival order is not authority | Verify/reconcile; later webhook becomes duplicate evidence | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| webhook duplicated | Irrelevant | Same event/resource delivered again; resend is explicitly non-idempotent | Same current transaction | Duplicate evidence only | No second payment transition or entitlement | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| webhook before browser | Later reference | Success first | Verify current state | Normal race | Reconcile once; browser later re-reads state | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| browser before webhook | Reference first | Success later | Verify current state | Browser is trigger only | Show VERIFYING until reconciliation | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| timeout during initialization | No usable URL | None yet | Same reference may verify or report not found | **Ambiguous external outcome** | Keep attempt unresolved; Verify same reference; do not mint new ref blindly | EMPIRICAL_VALIDATION_REQUIRED |
| same provider reference initialized twice | N/A | N/A | Duplicate-reference error + original Verify path | Second POST is not idempotent replay authority | Keep original attempt; Verify it; do not create second business effect | SUPPORTED_BY_PROVIDER |
| different provider references for same unresolved NewYou purchase | User may see two checkout URLs | Either/both could later succeed | Two provider transactions can independently exist | Provider reference does not solve NewYou purchase idempotency | Avoid second attempt while first unresolved; if both genuinely collect, one commercial admission + excess-collection remedy; never two entitlements | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| concurrent duplicate NewYou checkout submission | Multiple client intents | Multiple possible events | Multiple refs if NewYou admits both | NewYou duplicate-purchase problem, not provider dedupe problem | Commerce admission/idempotency must converge to one intended purchase consequence | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| ambiguous provider response after request accepted | Unknown | May later arrive | Verify same reference | Unknown ≠ failed | Reconcile; no duplicate create | EMPIRICAL_VALIDATION_REQUIRED |
| payment failed | May display provider failure/cancel | Transaction webhooks are success-focused | Verify = `failed` | No paid truth for attempt | No entitlement; allow governed new attempt if Commerce permits | SUPPORTED_BY_PROVIDER |
| payment abandoned/session timeout | User may leave | Usually no success webhook | Verify = `abandoned` or provider session timeout error | No success; purchase intent not automatically cancelled | No entitlement; a later new attempt needs distinct provider reference | SUPPORTED_BY_PROVIDER |
| provider `ongoing`/`pending` | Any | None/success later | Verify = ongoing/pending | Inconclusive | Keep pending; retry Verify under bounded policy | SUPPORTED_BY_PROVIDER |
| amount mismatch | Browser cannot be trusted | Signed payload might carry mismatching amount | Verify amount ≠ expected accepted cents | Invalid/mismatched success evidence | Do **not** establish valid paid truth; operator/reconciliation exception | SUPPORTED_BY_PROVIDER |
| currency mismatch | Same | Same | Verify currency ≠ expected ZAR | Invalid/mismatched success evidence | No entitlement; exception/reconcile | SUPPORTED_BY_PROVIDER |
| unknown reference from client | Forged/arbitrary | None | Verify not found | Invalid evidence | Reject; no purchase/payment mutation | SUPPORTED_BY_PROVIDER |
| browser forges “success” UI/query state | Attacker-controlled claim/reference | None required | Verify disagrees or reference/amount/currency mismatch | Browser claim has zero payment authority | Ignore claim; show current NewYou reconciliation state | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| unknown reference after init timeout | None | None yet | Verify not found initially | **Still unresolved until recovery boundary proven** | Continue bounded reconciliation; do not duplicate | EMPIRICAL_VALIDATION_REQUIRED |
| forged webhook | None | Invalid/missing HMAC | Verify may disagree/unknown | Counterfeit evidence | Reject before durable business processing | SUPPORTED_BY_PROVIDER |
| replayed authentic webhook | None | Valid signature but duplicate payload/resource | Verify same current state | Valid duplicate evidence | Idempotent no-op after reconciliation | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| webhook endpoint returns 500 | Irrelevant | Paystack retries | Verify independently available | Delivery failure, not payment failure | Durable recovery + later webhook/Verify; ensure no duplicate effect | SUPPORTED_BY_PROVIDER |
| endpoint accepts then worker crashes | Irrelevant | Provider may consider delivered after 200 | Verify independently available | Evidence must already be durable before 200 | Restart from durable inbox/attempt; reconcile | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| webhook success after refund already processed | Irrelevant | Old/resent `charge.success` can arrive after refund events | Verify may be `reversed`; Refund API processed | Event order not business precedence | Reconcile current transaction/refund state; do not re-grant access | EMPIRICAL_VALIDATION_REQUIRED |
| refund requested | Browser irrelevant | refund pending/processing/etc | Refund API record linked to txn | Separate refund lifecycle | Keep payment history; update refund truth; access follows Commerce policy | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| partial refund | Irrelevant | refund lifecycle events | Refund amount < original | Source/component correction, not whole-order rewrite | Compare with accepted allocation snapshot; affect only authorised source/component | SUPPORTED_BY_PROVIDER |
| refund create times out | Irrelevant | Event may appear later | List Refunds by transaction may reveal created refund | Ambiguous financial operation | Query before any re-POST; exact duplicate behavior must be proven | EMPIRICAL_VALIDATION_REQUIRED |
| refund `needs-attention` | Irrelevant | Event | Refund API status | Refund unresolved, payment still historical | Finance work/retry only under approved flow; no fabricated refund completion | SUPPORTED_BY_PROVIDER |
| refund failed | Irrelevant | `refund.failed` | Refund status failed; transaction returns success per docs | Refund did not complete | Preserve payment; determine NewYou remedy/work | SUPPORTED_BY_PROVIDER |
| full refund processed | Irrelevant | `refund.processed` | Refund processed; transaction reversed | Provider reversal evidence | Commerce records refund/reversal; Entitlements applies Product-law source consequence; preserve history | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| dispute opened | Irrelevant | `charge.dispute.create`/reminders | Dispute API links to transaction | Contested state, not fraud verdict | Commerce dispute lifecycle; reversible access policy per Product law | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| dispute resolved/lost chargeback | Irrelevant | `charge.dispute.resolve` | Dispute + transaction/reversal evidence | Commercial reversal/correction | Source-scoped idempotent access consequence; preserve fulfilment history | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| refund/dispute event ordering differs | Irrelevant | Events can be delayed/replayed | API current state is queryable | Never use arrival order as precedence | Reconcile current/historical state | EMPIRICAL_VALIDATION_REQUIRED |
| NewYou crash after provider success before DB paid transition | Maybe | Maybe | Verify success after restart | External success exists; internal truth incomplete | Recover durable purchase/reference, Verify, reconcile once | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| NewYou crash after Commerce paid before entitlement | Confirmation may be stale | Duplicate later | Verify still success | Payment truth exists; entitlement consequence incomplete | Durable/reconstructed idempotent Entitlements convergence | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| duplicate entitlement projection attempt | Any | Any | Same paid source | Repeat execution only | Unique business consequence/target-set convergence; one valid entitlement | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| Paystack API unavailable during reconciliation | Browser/webhook may exist | Maybe | Verify unavailable | Cannot establish/refresh provider evidence | PAYMENT_PENDING/VERIFYING; retry later, no access fabrication | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| DB unavailable after provider success | Browser/webhook maybe | Delivery may retry or get 500 | Provider truth exists externally | NewYou cannot commit authoritative truth | Fail closed; later Verify/reconcile after DB recovery | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| queue unavailable | Browser/webhook maybe | Evidence receipt may still be durable | Verify available later | Freshness degraded, not truth changed | Durable unresolved work; reconcile after recovery | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| provider customer/email differs from NewYou account expectation | Browser may show payer | Payload/API customer differs | Customer object differs | Provider customer is not IAM authority | Bind payment to NewYou purchase/provider attempt; surface mismatch only if current Commerce policy requires it | SUPPORTED_WITH_NEWYOU_RECONCILIATION |
| metadata contains sensitive participant data | N/A | Echoed evidence may contain it | API returns metadata | Privacy leakage risk | Never send health/assessment/plan/secrets; opaque/minimal IDs only | NEWYOU_POLICY_DECISION |
| provider-managed subscription cycle fails (future) | N/A | `invoice.payment_failed` | subscription `attention` | Paystack does not retry same cycle | Do not claim DEC-043 satisfied by provider-managed Subscriptions | PROVIDER_LIMITATION / FUTURE_RECURRING_ONLY |


<!-- IMPORT END: NEWYOU_PAYSTACK_SCENARIO_MATRIX_WORKING_v0.1.0.md -->


<!-- IMPORT START: NEWYOU_PAYSTACK_EMPIRICAL_VALIDATION_WORKING_v0.1.0.md -->

# NewYou Paystack Empirical Validation — Working v0.1.0

- **Status:** TEST PLAN / ALL PROVIDER CASES NOT_EXECUTED unless explicitly marked otherwise
- **Reason:** No Paystack sandbox credentials, configurable webhook endpoint or fault-injection harness were available in this validation session.
- **Rule:** Do not fabricate results. A documentary observation is not an empirical pass.

## Priority order

`P0` cases are required before FP-002 provider mechanics are frozen. `P1` should complete before FP-002 Phase 8/paid-pilot readiness as applicable. `FUTURE` is recurring-only and must not expand FP-002.

### PAYSTACK-EV-001 — Ambiguous Initialize timeout and Verify visibility

- **Priority:** P0 / highest-risk unknown
- **Question:** If NewYou sends Initialize with a known unique reference and loses the HTTP response, how quickly and reliably can Verify discover whether Paystack accepted/created the transaction?
- **Why it matters:** Duplicate initialization with the same reference is documented as an error, not idempotent replay. Minting a new reference after timeout could create a second payable attempt.
- **Setup:** Sandbox key; reverse proxy/fault injector that forwards the POST to Paystack but drops/delays the response to NewYou. Pre-persist a unique reference and expected amount/currency. Immediately call Verify on the same reference on a controlled backoff timeline; record every HTTP/status response. Also inspect transaction list/timeline where useful.
- **Expected safe outcomes:** (A) Verify reliably discovers the transaction; or (B) a bounded documented/observed period exists after which “not found” is stable enough to permit a governed new attempt. Any nonzero visibility lag must be captured.
- **Evidence:** Request timestamp, reference, proxy trace proving request forwarding, Paystack response visibility timeline, transaction id/status, webhook timing.
- **Failure interpretation:** If acceptance cannot be determined without risking duplicate charge and there is no safe provider reconciliation signal, FP-002 provider mismatch or stronger manual-reconciliation gate exists.
- **Credentials required:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-002 — Duplicate Initialize same reference

- **Priority:** P0
- **Question:** What exact sandbox response occurs if Initialize is repeated with the same reference after a successful initialization and after an ambiguous one?
- **Setup:** Initialize once; re-POST identical payload/reference; repeat after EV-001 dropped response.
- **Expected safe outcome:** Duplicate request is rejected and does not create a second provider transaction; Verify returns the original transaction.
- **Evidence:** HTTP code/body, transaction list count, Verify result, transaction id.
- **Failure interpretation:** More than one provider transaction for same reference is a critical mismatch; inconsistent error/visibility feeds EV-001 policy.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-003 — Browser return before/after webhook and browser loss

- **Priority:** P1
- **Question:** Can all three normal orderings occur without affecting recovery: callback first, webhook first, browser never returns?
- **Setup:** Sandbox payments through Redirect/Checkout; capture callback/webhook timestamps; close browser before redirect in one run.
- **Expected safe outcome:** Payment is discoverable/reconcilable by webhook/Verify regardless of browser return.
- **Evidence:** timestamps, reference, webhook event id/history, Verify status.
- **Failure interpretation:** Any provider dependency on browser return would contradict FP-002 architecture.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-004 — Webhook duplicate/resend

- **Priority:** P0
- **Question:** Can an identical provider event be delivered multiple times and does NewYou remain one-effect?
- **Setup:** Receive `charge.success`, then use Webhook Events resend twice for the same event id; optionally replay captured signed payload in controlled test.
- **Expected safe outcome:** Multiple deliveries observed; NewYou durable evidence may record delivery attempts but one Commerce transition / one Entitlement effect occurs.
- **Evidence:** Paystack event `_id`, trial count/resend responses, NewYou receipt ids, single business consequence proof.
- **Failure interpretation:** Duplicate business consequence is a blocker; provider duplicate itself is expected.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-005 — Webhook transient 500 / outage / acknowledgement boundary

- **Priority:** P0
- **Question:** Does Paystack retry after 500 as documented, and can NewYou ACK only after authenticated durable receipt without doing long business work synchronously?
- **Setup:** Test webhook endpoint returns 500 for first attempt(s), then accepts; record retry timing. Separate case: durably persist signed event then intentionally stop worker before reconciliation.
- **Expected safe outcome:** Retry occurs; after durable acceptance a 200 prevents provider dependence on business-work completion; restart later reconciles.
- **Evidence:** event delivery history, response codes, timestamps, durable receipt row/evidence, restart result.
- **Failure interpretation:** If durable receipt cannot be established within provider timeout/retry contract, adjust ingress mechanism; never 200 before durability solely for convenience.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-006 — Forged and replayed webhook

- **Priority:** P0
- **Question:** Are invalid signatures rejected and valid replays harmless?
- **Setup:** Send altered payload with original signature; send missing signature; replay authentic signed payload.
- **Expected safe outcome:** Forged/missing signature rejected before business processing; replay yields no duplicate effect.
- **Evidence:** HTTP/app logs with redaction, rejection reason, no Commerce/Entitlement change.
- **Credentials:** A captured sandbox payload for replay; synthetic invalid cases need no Paystack credentials once fixture exists.
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-007 — Success with no usable webhook

- **Priority:** P0
- **Question:** Can NewYou deterministically discover a successful payment using only the stored transaction reference and Verify?
- **Setup:** Disable/point webhook at failing endpoint; complete sandbox payment; do not use callback as authority; poll/reconcile Verify.
- **Expected safe outcome:** Verify returns success with reference/amount/currency and transaction id; NewYou can reconcile exactly once.
- **Evidence:** payment timestamp, webhook failure history, Verify result, one Commerce paid consequence.
- **Failure interpretation:** If success cannot be discovered without webhook/browser, provider mismatch for restart/reconciliation invariant.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-008 — Amount/currency/reference mismatch rejection

- **Priority:** P0
- **Question:** Does NewYou refuse successful provider evidence that does not match its accepted purchase snapshot?
- **Setup:** Create a NewYou test purchase expecting amount/currency A; associate/replay valid Paystack success evidence from a deliberately different amount/reference where the harness can safely do so.
- **Expected safe outcome:** Evidence quarantined/invalid for that purchase; no paid truth and no entitlement.
- **Evidence:** provider response + NewYou expected snapshot + rejection proof.
- **Failure interpretation:** Any grant on mismatch is a blocker.
- **Credentials:** YES for realistic provider fixture
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-009 — Provider status progression and session expiry

- **Priority:** P1
- **Question:** Which observed status transitions occur for abandoned/failed/pending/ongoing and after payment-session timeout?
- **Setup:** Use failed test cards, incomplete checkout, OTP waiting, and configured session timeout where supported; query Verify over time.
- **Expected safe outcome:** Inconclusive statuses remain non-success; terminal failure/abandonment never grants; new attempt uses new provider reference only after Commerce allows it.
- **Evidence:** status timeline, gateway responses, callback/webhook presence/absence.
- **Failure interpretation:** Unexpected later success after assumed terminal state means NewYou must treat that state more conservatively.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-010 — Refund Create timeout / duplicate request ambiguity

- **Priority:** P0
- **Question:** If Create Refund reaches Paystack but NewYou loses the response, can NewYou discover the created refund before deciding whether any retry is safe? What happens if the same refund request is repeated?
- **Setup:** Successful sandbox transaction; fault injector forwards Create Refund and drops response. Query List Refunds filtered by transaction id at controlled intervals. Fetch discovered refund. In a disposable test, repeat same Create Refund amount and record whether Paystack rejects, creates another partial refund, or otherwise constrains it.
- **Expected safe outcome:** Created refund is discoverable by transaction and duplicate behavior is bounded enough to define a no-double-refund rule. NewYou never relies on blind repeat POST.
- **Evidence:** source txn id/ref, refund list timeline, refund IDs/amounts/statuses, duplicate POST response, total refunded/deducted amount.
- **Failure interpretation:** If refund creation can duplicate silently and cannot be reliably reconciled, refund automation is blocked; require operator/manual provider reconciliation until safer mechanism exists.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-011 — Full and partial refund lifecycle

- **Priority:** P0
- **Question:** Do sandbox full/partial refunds expose the documented pending/processing/needs-attention/failed/processed states and correlate correctly with transaction state/webhooks?
- **Setup:** Use normal success card plus documented failed/needs-attention refund test cards. Run partial and full refunds; capture API/webhooks/Verify over time.
- **Expected safe outcome:** Refund amount/status can be reconciled independently; transaction may move to reversal-pending/reversed as documented; NewYou component policy remains separate.
- **Evidence:** refund IDs, source txn, status/event timeline, amounts/currency, final Verify transaction status.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-012 — Reordered old success after refund/reversal

- **Priority:** P0
- **Question:** Can an old `charge.success` event be resent after current provider state has become reversed, and does NewYou avoid re-establishing paid/access as if nothing happened?
- **Setup:** Complete payment; refund to processed/reversed; resend original success event via Webhook Events API.
- **Expected safe outcome:** Reconciliation reads current/historical provider evidence; old event cannot override later refund/reversal truth.
- **Evidence:** original event id/timestamp, refund status, current Verify result, no access re-grant beyond Product law.
- **Credentials:** YES
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-013 — Dispute event/API lifecycle

- **Priority:** P1 / FP-006 operational relevance
- **Question:** How do dispute create/remind/resolve events and transaction `reversed` state relate in practice, especially for South African live operations?
- **Setup:** Use any provider-supported sandbox dispute simulation if available; otherwise coordinate controlled live/provider support validation before paid pilot. Capture transaction/dispute API and webhook timing.
- **Expected safe outcome:** NewYou can identify the affected source transaction and reconcile contested/final state without relying on event order.
- **Evidence:** dispute id/status, transaction id/ref/status, event sequence, resolution outcome, operator deadline.
- **Failure interpretation:** If no machine-readable linkage/current-state query exists, finance operations/manual reconciliation requirements must be explicit before release.
- **Credentials:** YES; may require controlled live/provider support
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-014 — Restart after provider success before Commerce reconciliation

- **Priority:** P0 (provider + NewYou proof)
- **Question:** After Paystack succeeds and NewYou crashes before authoritative Commerce transition, can restart recover from durable purchase/reference and converge exactly once?
- **Setup:** Sandbox payment; inject crash at boundary after external success is observable but before/while NewYou commits paid transition; restart; run reconciliation.
- **Expected safe outcome:** Verify rediscovers success; one paid transition; one valid entitlement.
- **Evidence:** crash marker, durable pre-crash purchase/reference, Verify response, DB invariants, entitlement count/source.
- **Credentials:** YES + executable NewYou proof environment
- **Status:** NOT_EXECUTED

### PAYSTACK-EV-015 — Test/live boundary confirmation

- **Priority:** P1 / RELEASE_ONLY elements
- **Question:** Which critical sandbox assumptions need a production smoke check?
- **Setup:** Before paid pilot, low-value controlled live payment using configured launch channel(s); verify callback/webhook/API, ZAR amount, signature validation, refund path where commercially acceptable. Do not load-test provider.
- **Expected safe outcome:** Core one-off semantics match validated sandbox/docs. Any difference is captured as provider configuration/ops issue before expansion.
- **Credentials:** LIVE; release authority required
- **Status:** NOT_EXECUTED / RELEASE_ONLY

### PAYSTACK-EV-016 — Provider-managed subscription failed cycle (future)

- **Priority:** FUTURE_RECURRING_ONLY
- **Question:** Confirm documented no-retry behavior and event/status lifecycle for a failed subscription cycle.
- **Setup:** Future sandbox subscription with a failing charge instrument; capture invoice/subscription events/status.
- **Expected safe outcome:** Evidence confirms provider-managed Subscriptions do not implement NewYou 72-hour retries, forcing an explicit future architecture choice rather than accidental adoption.
- **Status:** NOT_EXECUTED / FUTURE

### PAYSTACK-EV-017 — Charge Authorization retry ambiguity (future)

- **Priority:** FUTURE_RECURRING_ONLY
- **Question:** If NewYou later manages recurring charges through reusable authorizations, what happens on timeout/retry with a stable reference?
- **Setup:** Same fault-injection pattern as EV-001 around Charge Authorization; verify same reference; duplicate request; challenge/failed-card paths.
- **Expected safe outcome:** A stable renewal/payment-attempt identity can be reconciled without duplicate charge.
- **Status:** NOT_EXECUTED / FUTURE

## OQ-004 closure checklist

### A. Authority/governance

- [x] Pin current `main` SHA and current authority route.
- [x] Extract provider-independent FP-002 invariants before provider mapping.
- [x] Confirm Commerce owns commercial truth and Entitlements owns access.
- [x] Confirm browser/provider state is evidence only.
- [ ] Resolve governance wording for **global** OQ-004 if FP-002 is to close only its one-off-payment subset while recurring/proration remains future. No silent partial `COMPLETE` status.

### B. Documentary provider capability

- [x] Unique transaction reference and server Initialize documented.
- [x] Verify Transaction by reference documented.
- [x] Transaction status vocabulary documented.
- [x] Amount/currency/reference evidence documented.
- [x] HMAC-SHA512 webhook authenticity documented.
- [x] Live webhook retry and duplicate-capable resend semantics documented.
- [x] Refund full/partial + status/API/webhook documented.
- [x] Dispute API/events documented.
- [x] ZAR minor-unit support documented.
- [x] Test/live separation and limitations documented.

### C. FP-002 critical empirical evidence

- [ ] EV-001 ambiguous Initialize timeout / Verify visibility PASS.
- [ ] EV-002 duplicate same-reference initialize PASS.
- [ ] EV-004 duplicate/resend webhook + one-effect PASS.
- [ ] EV-005 500/retry + durable ACK boundary PASS.
- [ ] EV-006 forged/replayed webhook PASS.
- [ ] EV-007 no-webhook success recovery via Verify PASS.
- [ ] EV-008 amount/currency/reference mismatch fails closed PASS.
- [ ] EV-010 ambiguous refund creation / duplicate behavior PASS or a safe manual-only compensation is formally adopted.
- [ ] EV-011 full/partial refund lifecycle PASS.
- [ ] EV-012 reordered success after reversal/refund PASS.
- [ ] EV-014 restart after provider success converges to one payment + one entitlement PASS at the appropriate proof stage.

### D. Operational/release evidence

- [ ] Finance/support can see unresolved payment/refund/dispute/reconciliation work without dashboards becoming authority.
- [ ] Secret-key storage/rotation and webhook-secret handling are approved at JIT/release scope.
- [ ] Metadata/log/provider-payload retention is reconciled with Privacy & Consent / Audit & Evidence requirements.
- [ ] Controlled live smoke evidence exists before paid pilot where required.
- [ ] Dispute/chargeback operating ownership and South Africa response timing are confirmed before paid pilot/FP-006 release.

### E. Future recurring — not an FP-002 implementation prerequisite

- [x] Provider-managed Subscription no-retry behavior documented and recorded as a future limitation.
- [ ] Future recurring architecture selects provider-managed vs NewYou-managed collection only when FP-009/JIT requires it.
- [ ] Proration mechanism is proven or explicitly designed; current documentation is insufficient.
- [ ] Charge Authorization ambiguity/retry semantics are validated if NewYou-managed recurrence is selected.

## Current closure disposition

**OQ-004 BLOCKED ON EMPIRICAL TESTS.**

The documentary provider evidence is sufficient to continue a provider-validation stream and to say there is **no demonstrated FP-002 provider mismatch yet**. It is not sufficient to freeze payment/refund retry mechanics or mark the global OQ complete.


<!-- IMPORT END: NEWYOU_PAYSTACK_EMPIRICAL_VALIDATION_WORKING_v0.1.0.md -->


<!-- IMPORT START: NEWYOU_PAYSTACK_GAP_REGISTER_WORKING_v0.1.0.md -->

# NewYou Paystack Gap Register — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE

| Gap | Scope | Classification | Why it matters | Safe current disposition |
|---|---|---|---|---|
| GAP-001 Initialize timeout visibility/consistency is undocumented. Duplicate same-reference init is an error. | FP-002 | EMPIRICAL_VALIDATION_REQUIRED | Wrong retry can create second payable attempt. | EV-001/002 before mechanics freeze; unresolved means no blind new reference. |
| GAP-002 Create Refund exposes no idempotency key and duplicate-request semantics are undocumented. | FP-002 | EMPIRICAL_VALIDATION_REQUIRED | Timeout/retry could duplicate financial reversal. | EV-010; reconcile List/Fetch Refunds before retry; manual exception if needed. |
| GAP-003 Webhook transaction success can be resent after later state changes; provider event order is not precedence. | FP-002 | EMPIRICAL_VALIDATION_REQUIRED | Stale success could re-grant access after refund/dispute. | Reconcile current/historical API state; EV-012. |
| GAP-004 Main Paystack docs document different test-mode retry schedule from some alternate docs versions. | Test harness only | DOCUMENTATION_AMBIGUOUS | Exact sandbox timing assertions may be brittle. | Use current main docs as baseline; test behavior observationally; do not make timing exactness a Product invariant. |
| GAP-005 Paystack Webhook guidance says return 200 quickly; NewYou Architecture requires durable evidence acceptance before ACK. | FP-002 | SUPPORTED_WITH_NEWYOU_RECONCILIATION | 200 before durability can lose sole event; long work before 200 creates duplicates. | Minimal signature verify + durable inbox/receipt commit + 200; async reconcile. Prove in EV-005. |
| GAP-006 Provider transaction `success` alone is insufficient if amount/currency/reference mismatch. | FP-002 | SUPPORTED_WITH_NEWYOU_RECONCILIATION | Underpayment/cross-purchase evidence can grant value. | Exact NewYou snapshot validation required. |
| GAP-007 Provider customer/email semantics are not NewYou IAM semantics. | FP-002/future recurring | SUPPORTED_WITH_NEWYOU_RECONCILIATION | Email changes/duplicates can misbind identity if trusted. | Bind by NewYou purchase + provider reference; provider customer remains evidence/operational ID. |
| GAP-008 Metadata is provider-visible/returned and custom fields may show in Dashboard. | FP-002 privacy | NEWYOU_POLICY_DECISION | Sensitive participant data could leak to external processor/operator surface. | Opaque/minimum identifiers only; exact retention/data mapping deferred to Privacy/JIT. |
| GAP-009 Exact PCI scope for NewYou is not established by Paystack documentation alone. | Security/release | RELEASE_ONLY | False scope claims can misstate compliance obligations. | Prefer hosted/approved Checkout; separate compliance assessment; do not use raw Card API absent PCI approval. |
| GAP-010 South African dispute response timing differs across Paystack generic developer guide vs current SA support article. | FP-006/release | DOCUMENTATION_AMBIGUOUS / RELEASE_ONLY | Missed chargeback deadlines have financial consequence. | Treat current SA first-party support guidance as operations input and confirm with Paystack account/support before launch; do not hard-code generic 16h. |
| GAP-011 Provider-managed Subscriptions do not retry a failed cycle. | Future recurring | PROVIDER_LIMITATION / FUTURE_RECURRING_ONLY | Does not directly implement NewYou 72h provider-safe retry lifecycle. | Do not adopt as NewYou recurring authority/mechanism without explicit future JIT decision. |
| GAP-012 No documented subscription proration primitive found in current first-party docs. | Future upgrade/proration | DOCUMENTATION_AMBIGUOUS / FUTURE_RECURRING_ONLY | DEC-046 says immediate upgrade with provider-supported proration. | Future provider/commercial JIT must prove mechanism or amend product/mechanism at correct authority; not FP-002. |
| GAP-013 Reusable authorization is bound to the original transaction email for future charges. | Future recurring | PROVIDER_LIMITATION / FUTURE_RECURRING_ONLY | NewYou profile email changes cannot simply replace provider token-binding email. | Store token-bound provider email as payment-method operational data; never make it IAM authority. |
| GAP-014 Test mode does not process settlements and some channels are unavailable. | Release | RELEASE_ONLY | Sandbox cannot prove all production economics/rail behavior. | Production smoke/ops evidence at controlled launch; settlement never access authority. |
| GAP-015 Global OQ-004 wording includes subscription/proration while Roadmap defers recurring from FP-002. | Governance | NEWYOU_POLICY_DECISION | Marking OQ-004 globally complete on one-off evidence would silently narrow higher authority; requiring all recurring evidence could unlawfully expand FP-002. | Explicitly split/narrow/scope gate through governance before changing OQ status, or keep OQ globally open while recording FP-002-specific validated disposition if authority permits. |
| GAP-016 Paystack generic transaction error documentation states a maximum `10,000,000` without sufficiently clear market/unit semantics for a NewYou rule. | FP-002 bounds | DOCUMENTATION_AMBIGUOUS | Encoding the wrong limit would turn provider documentation ambiguity into Product behavior. | Current launch prices are far below the stated number; do not encode a Product maximum from this wording. Revalidate only if a real offer approaches provider limits. |

## Highest-risk unknown

**GAP-001 / PAYSTACK-EV-001 — Initialize timeout recovery.**

Reason: it sits before money collection, duplicate reference replay is not documented idempotent, and a wrong decision can create either a duplicate payable attempt or a stuck paid customer. Verify-by-reference is the promising compensation, but its immediate visibility/consistency after an ambiguous initialization is not documented.

## Provider mismatch assessment

### FP-002

No documented hard mismatch yet. Current status is `SUPPORTED_WITH_NEWYOU_RECONCILIATION` subject to critical empirical proof.

### Future recurring

A mechanism-level mismatch exists **if** NewYou were to adopt Paystack-managed Subscriptions as the implementation of DEC-043 retries: failed subscription charges are not retried in the cycle. This does not prove Paystack as a gateway is unusable; it means future recurring architecture must not be selected by provider convenience.


<!-- IMPORT END: NEWYOU_PAYSTACK_GAP_REGISTER_WORKING_v0.1.0.md -->


<!-- IMPORT START: NEWYOU_PAYSTACK_EVIDENCE_INDEX_WORKING_v0.1.0.md -->

# NewYou Paystack Evidence Index — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE
- **Access date for external sources:** 2026-10-08
- **Repository baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`

## A. Repository authority/evidence inspected

| Source | Role in validation |
|---|---|
| `docs/00_platform/README.md` | Current authority route/current planning state. |
| `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` | Machine-readable current authority versions/hashes. |
| `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` | MVP/commercial validation boundary; SA/ZAR/Paystack launch direction. |
| `00_PLATFORM_v1.6.0.md` | Paystack locked launch gateway; provider behavior gate; §21R payment/refund/dispute/access rules; checkout abuse. |
| `01_DECISIONS_v1.6.0.md` | Exact OQ-004 wording/status and OQ-001/OQ-002/OQ-035/OQ-036. |
| `02_OPEN_WORK_v1.2.59.md` | OQ-004 remains open; current sequencing. |
| `03_ARCHITECTURE_v1.1.1.md` | Provider ingress, ambiguity, durable reconciliation, retry/restart and idempotency doctrine. |
| `04_DOMAIN_MAP_v1.2.0.md` | Commerce/Entitlements/Audit ownership and provider non-authority. |
| `05_ROADMAP_v1.2.0.md` | FP-002 exact outcome/gates/exit; recurring deferred; FP-006 operational/release needs. |
| `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` | PAYMENT_PENDING/VERIFYING and browser return non-authority. |
| `PLATFORM_OPERATING_MODEL_v1.0.1.md` | Finance/support reconciliation workflow, work-not-authority. |
| `reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md` FLOW-02 | End-to-end payment/provider/reconciliation pressure test. |
| `reference/ENGINEERING_STANDARDS_v1.0.1.md` | HIGH financial/provider-reconciliation proof rules; timeout/unknown no blind retry. |
| `working/commerce_entitlements/NEWYOU_CER_PREJIT_CONTRACT_WORKING_v0.2.1.md` | Non-authoritative recurring/provider evidence layering and duplicate/reversal pressure. |
| `working/privacy_consent_data_lifecycle/NEWYOU_PRIVACY_PREJIT_CONTRACT_WORKING_v0.1.3.md` | Non-authoritative privacy/provider-retention/deletion seam. |

## B. Current OQ/gate facts

| Gate | Current wording/classification relevant here |
|---|---|
| OQ-004 | `VALIDATION REQUIRED` — test failed-payment, subscription, webhook, proration, refund and chargeback behaviour before implementation is locked. Open Work summarizes Paystack recurring/webhook/retry/proration/refund/chargeback behavior. |
| OQ-001 | EXPERT REVIEW final operating entity; Roadmap marks release-only for FP-002. |
| OQ-002 | RESOLVED by current pricing decisions; Roadmap non-blocking for FP-002. |
| OQ-035 | SECURITY / OPERATIONS REVIEW abuse-control thresholds; Roadmap release-only for FP-002. |
| OQ-036 | VENDOR / OPERATIONS REVIEW notification provider/channel policy; Roadmap non-blocking for FP-002. |
| FP-002 gate classification | OQ-004 `BLOCKS_THIS_FP`; exact provider ambiguity/webhook/retry/refund/dispute behavior. Recurring membership is explicitly deferred from FP-002. |

## C. Paystack first-party primary sources

All accessed 2026-10-08.

| Evidence ID | URL | What it supports | Evidence class |
|---|---|---|---|
| PS-001 | https://paystack.com/docs/api/transaction/ | Initialize/Verify; unique reference; amount/currency/status/ids; Charge Authorization. | DOCUMENTED FACT |
| PS-002 | https://paystack.com/docs/api/errors/transaction/ | Duplicate reference error; transaction not found; session-timeout behavior. | DOCUMENTED FACT |
| PS-003 | https://paystack.com/docs/payments/verify-payments/ | Verify-by-reference; status vocabulary; callback reference; double-fulfilment warning. | DOCUMENTED FACT |
| PS-004 | https://paystack.com/docs/payments/webhooks/ | Callback unreliability; HMAC-SHA512 signature; live/test retries; supported events; 200 behavior. | DOCUMENTED FACT |
| PS-005 | https://paystack.com/docs/api/webhook-events/ | Delivery history, event IDs, payload/server response, resend; resend explicitly non-idempotent. | DOCUMENTED FACT |
| PS-006 | https://paystack.com/docs/api/refund/ | Create/List/Fetch/Retry Refund; full/partial; list by transaction. | DOCUMENTED FACT |
| PS-007 | https://paystack.com/docs/payments/refunds/ | Refund status lifecycle and transaction-status relationship; refund webhooks. | DOCUMENTED FACT |
| PS-008 | https://paystack.com/docs/api/dispute/ | Dispute list/fetch/transaction linkage/status/resolution. | DOCUMENTED FACT |
| PS-009 | https://paystack.com/docs/payments/manage-disputes/ | Dispute workflow and events. | DOCUMENTED FACT |
| PS-010 | https://paystack.com/docs/api/authentication/ | Public vs secret keys; test/live; test limitations; TLS/key/IP controls. | DOCUMENTED FACT |
| PS-011 | https://paystack.com/docs/api/rate-limits/ | Live/test quotas; Verify/Initialize extended live limits; test mode not load testing. | DOCUMENTED FACT |
| PS-012 | https://paystack.com/docs/api/ | ZAR cent/subunit, SA availability, R1 transaction minimum. | DOCUMENTED FACT |
| PS-013 | https://paystack.com/docs/payments/metadata/ | Metadata/custom fields provider visibility/API return. | DOCUMENTED FACT |
| PS-014 | https://paystack.com/docs/payments/payment-channels/ | Hosted/Popup/Redirect channels; avoid direct card details unless PCI compliant. | DOCUMENTED FACT |
| PS-015 | https://paystack.com/docs/payments/charge-card/ | Raw card API PCI-DSS requirement. | DOCUMENTED FACT |
| PS-016 | https://paystack.com/docs/payments/test-payments/ | Sandbox cards incl. failed/refund scenarios. | DOCUMENTED FACT |
| PS-017 | https://paystack.com/docs/payments/subscriptions/ | Provider-managed subscriptions; failed cycle not retried; subscription statuses/events. | DOCUMENTED FACT / FUTURE |
| PS-018 | https://paystack.com/docs/payments/recurring-charges/ | Reusable card authorizations, signature, original-email binding, server-managed recurring direction. | DOCUMENTED FACT / FUTURE |
| PS-019 | https://paystack.com/docs/changelog/api/ | Sep 2026 Webhook Events API; June 2026 rate limits/response codes. | DOCUMENTED FACT |
| PS-020 | https://paystack.com/za/pricing | Current SA fee model / ZAR settlement context. | DOCUMENTED FACT; commercial info |
| PS-021 | https://support.paystack.com/en/articles/10609026 | First-party operational confirmation that duplicate webhook delivery can occur; retry only if integration handles repeats safely. | FIRST-PARTY SUPPORT EVIDENCE |
| PS-022 | https://support.paystack.com/en/articles/2125378 | Current first-party South Africa chargeback response timing guidance. | FIRST-PARTY SUPPORT / RELEASE OPS |

## D. Evidence classification rules used

- **DOCUMENTED FACT:** explicitly stated in current first-party Paystack material.
- **REASONABLE INTERPRETATION:** conservative integration consequence directly derived from NewYou authority + documented provider contract; not a claimed provider guarantee.
- **ASSUMPTION:** unproven premise; must not become implementation fact.
- **UNKNOWN:** not established by current documentation/repository evidence.
- **EMPIRICALLY VERIFIED:** observed in a controlled provider experiment with captured evidence. **None yet in this pack.**

## E. Key documentary findings and confidence

| Finding | Evidence nature | Provider-validation classification | Confidence / action |
|---|---|---|---|
| Duplicate same-reference transaction initialization is not an idempotent replay contract; Paystack documents duplicate-reference errors. | DOCUMENTED FACT | EMPIRICAL_VALIDATION_REQUIRED | High; drives EV-001/002 because ambiguous timeout recovery still needs observation. |
| Verify by stored transaction reference is a provider-supported reconciliation query. | DOCUMENTED FACT | SUPPORTED_BY_PROVIDER | High. |
| Webhook delivery can repeat; explicit event resends are non-idempotent. | DOCUMENTED FACT | SUPPORTED_WITH_NEWYOU_RECONCILIATION | High; NewYou one-effect invariant mandatory. |
| Browser callback can be absent/unreliable. | DOCUMENTED FACT | SUPPORTED_WITH_NEWYOU_RECONCILIATION | High; browser cannot be payment authority. |
| Create Refund has no documented idempotency key and docs do not state duplicate POST semantics. | UNKNOWN (absence in current docs) | EMPIRICAL_VALIDATION_REQUIRED | Critical EV-010. |
| Verify visibility timing immediately after an ambiguously completed Initialize is not documented. | UNKNOWN | EMPIRICAL_VALIDATION_REQUIRED | Critical EV-001. |
| Paystack-managed Subscriptions do not retry a failed billing attempt in the same cycle. | DOCUMENTED FACT | PROVIDER_LIMITATION / FUTURE_RECURRING_ONLY | High; cannot be equated to DEC-043 retry semantics. |
| Current docs do not establish a Paystack subscription proration primitive. | UNKNOWN / documentation gap | DOCUMENTATION_AMBIGUOUS / FUTURE_RECURRING_ONLY | Future validation; do not infer impossible, but do not promise provider proration. |
| Sandbox proves production parity. | FALSE ASSUMPTION | RELEASE_ONLY | Paystack explicitly says not all features exist in test mode; production smoke/release evidence remains necessary. |


<!-- IMPORT END: NEWYOU_PAYSTACK_EVIDENCE_INDEX_WORKING_v0.1.0.md -->


---

# Pass 2 — Provider-Ambiguity Decomposition, Amount Integrity and Upstream Pressure

- **SemVer successor:** `v0.1.0 → v0.2.0`
- **Pass date:** 2026-10-08
- **Pass status:** COMPLETE FOR DOCUMENTARY PRESSURE / EMPIRICAL CASES STILL OUTSTANDING
- **Change class:** MINOR — adds/refines validation semantics and candidate upstream deltas; no governed authority is changed.
- **Predecessor prefix SHA-256:** `4b4acd5e573823be59f9388852fb6d21cac9b16b53c0b895da9df9b4f5640bbc`
- **Live repository baseline rechecked:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`

## P2.1 Objective

Pass 2 does not broaden into generic Paystack research. It attacks the failure positions most likely to cause duplicate collection, false success, stale re-grant or unrecoverable money state in FP-002, then identifies the smallest upstream questions exposed by those failures.

The pass asks repeatedly:

- What exact durable NewYou identity survives this failure?
- What external capability may still be usable by the participant after the failure?
- What provider evidence can be re-read after restart?
- Can a retry create a second independently payable provider transaction?
- Can stale success evidence arrive after a later refund/dispute/reversal?
- Does the provider amount actually charged equal NewYou's accepted order amount?
- Does current Product Law define the money remedy as well as the access remedy?

## P2.2 New/refined findings

### P2-F-001 — Initialization ambiguity is not one failure; it has three materially different cut points

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION` + `EMPIRICAL_VALIDATION_REQUIRED`

Paystack transaction initialization yields a unique provider reference and an `access_code`/authorization URL. Reusing the same transaction reference for a new initialization is documented as a duplicate-reference error, not an idempotent replay. Therefore the original `PAYSTACK-EV-001` must distinguish whether the payment capability ever became usable by the participant.

#### Failure cut A — provider may have accepted; NewYou never receives the initialization response

```text
NewYou durably creates Purchase Intent + Provider Attempt/reference
→ sends Initialize
→ Paystack may create transaction
→ response is lost before NewYou receives access_code/auth URL
```

Safe interpretation:

- payment outcome is unresolved at the provider-attempt layer;
- the original reference must be queried before deciding anything about that attempt;
- absent a delivered authorization capability, the participant ordinarily cannot complete that particular provider checkout through the NewYou journey;
- a later new attempt may be necessary, but it must be a distinct Provider Attempt under the same NewYou Purchase Intent and must not create a second commercial identity;
- the exact safe admission point for a new attempt remains an empirical/JIT contract question because provider visibility and session behaviour after the ambiguous request must be proven.

#### Failure cut B — NewYou receives and durably retains provider capability; browser response is lost

```text
Initialize returns
→ NewYou durably retains reference + access_code/auth URL
→ response to browser is lost
```

Safe interpretation:

- do not create another Provider Attempt merely because browser delivery failed;
- resume/re-present the same provider capability where the selected Paystack integration mode permits it;
- any new attempt is subordinate to a NewYou guard that prevents concurrent independently payable attempts unless current authority explicitly allows replacement.

#### Failure cut C — browser receives a payable provider capability; NewYou later loses presentation/ack state

```text
Initialize returns
→ browser receives access_code/auth URL
→ customer may still pay old provider transaction
→ NewYou crashes / reconnects / user opens another tab
```

This is the dangerous duplicate-collection seam. A second provider reference can become a second independently payable transaction while the first remains payable. `reference` uniqueness prevents replay of one Paystack transaction; it does **not** enforce one NewYou purchase intent across two references.

**Required NewYou invariant:** a Provider Attempt is never the Purchase Intent. New attempt admission must account for any older attempt whose payment capability may still be live/payable.

**Empirical consequence:** split `PAYSTACK-EV-001` into `PAYSTACK-EV-001A/B/C` below.

---

### P2-F-002 — `abandoned` is non-success evidence, but documentary evidence is insufficient to treat every `abandoned` observation as irrevocably terminal

**Classification:** `DOCUMENTATION_AMBIGUOUS` + `EMPIRICAL_VALIDATION_REQUIRED`

Paystack's verification vocabulary includes `abandoned`; Paystack separately documents payment-session timeout errors that require initialization of a new transaction after the timeout. Those are not the same documentary statement.

Correction to any v0.1.0 wording that implicitly treated `abandoned` as universally terminal:

> `abandoned` is sufficient to deny payment success. It is not, from documentation alone, sufficient to prove that the old provider payment capability can never subsequently become payable/successful before or around session expiry.

NewYou therefore must not use a bare `abandoned` observation as the only concurrency guard for creating a replacement Provider Attempt until sandbox behaviour is proven for the selected checkout mode and timeout configuration.

`session expired / transaction cannot be completed because timeout exceeded` is stronger provider evidence that a new provider transaction is required, but even then NewYou's one-Purchase-Intent and amount/entitlement invariants remain controlling.

---

### P2-F-003 — Verify `data.amount` is the money-integrity field; `requested_amount` has a distinct meaning for Partial Debit

**Classification:** `SUPPORTED_BY_PROVIDER`

Paystack documents Partial Debit as a special, request-only recurring/authorization capability. For Partial Debit transactions:

- `amount` = amount actually charged;
- `requested_amount` = amount the merchant intended to charge.

FP-002 ordinary hosted/one-off checkout must therefore compare the **actual charged `data.amount`** and `data.currency` with the immutable NewYou accepted order snapshot. `requested_amount` is useful diagnostic/evidence when present; it is not a substitute for actual charged amount.

**FP-002 constraint:** Partial Debit is not required by FP-002 and must not be silently activated as a workaround for failed one-off payment. If it ever enters a future recurring design, it requires its own Product/commercial semantics because partial collection cannot truthfully satisfy a fixed-price purchase by default.

---

### P2-F-004 — Paystack fees are not part of NewYou payment truth merely because Paystack charges merchant fees

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack's South African pricing documents merchant transaction fees. Those fees affect settlement economics, not the participant's NewYou Purchase Intent by themselves.

For FP-002 the safest current invariant is:

```text
NewYou accepted customer amount in ZAR minor units
== Paystack data.amount actually charged to customer
```

Provider fees/settlement deductions are a separate financial/economic dimension and must not cause NewYou to weaken amount comparison.

**Open configuration pressure:** if a Paystack account/configuration can be set to pass provider fees through to the customer, that cannot be enabled silently for FP-002 because it could make the charged amount differ from the Product-Law price/order snapshot. Customer-paid checkout surcharges would need explicit governed Product/offer disclosure semantics before the amount-integrity invariant could change.

Until such authority exists, the validation contract assumes provider fees are absorbed as merchant/payment-processing cost and the customer's actual Paystack charge equals NewYou's accepted order amount.

---

### P2-F-005 — Provider capability is channel-specific; `Paystack validated` cannot mean every enabled channel was validated

**Classification:** `EMPIRICAL_VALIDATION_REQUIRED`

Paystack documents South African card payments plus additional channels such as EFT/Ozow and Capitec Pay, with channel-specific flows and availability. Test mode also does not expose every live feature/channel.

FP-002 does not need a broad promise that every Paystack channel is usable. The safe mechanism is:

- maintain an explicit implementation-time allowlist of enabled payment channels;
- validate each enabled channel against the FP-002 invariant suite;
- leave unvalidated channels disabled even if Paystack Dashboard/account configuration could expose them;
- channel enablement is mechanism/configuration, not Product Law, unless Product explicitly promises a particular channel.

The minimum OQ-004/FP-002 provider proof may therefore close against a bounded channel set. A later channel addition reopens the applicable provider-proof subset, not Product payment semantics.

---

### P2-F-006 — Webhook signature verification input must be proven against real Paystack-signed events

**Classification:** `SUPPORTED_BY_PROVIDER` + `EMPIRICAL_VALIDATION_REQUIRED`

**Documented fact:** Paystack signs webhook event payloads with HMAC-SHA512 using the integration secret key and sends the result in `x-paystack-signature`.

**Implementation interpretation requiring proof:** NewYou must compute the HMAC over a payload representation that is demonstrably compatible with Paystack's signing behaviour. The current Paystack examples serialize the request body in application code; framework body parsing/normalisation can differ, so we must not guess that any semantically equivalent JSON representation will verify.

The executable proof therefore uses a captured Paystack-signed test event and proves the exact Phoenix/Plug ingress handling. Verification occurs before provider evidence is admitted to the durable reconciliation path.

After authenticity verification, the event is still only provider evidence. Authentication does not make its payment/refund/dispute claim NewYou business truth.

---

### P2-F-007 — Secret-key rotation creates a webhook-ingress availability seam

**Classification:** `RELEASE_ONLY` + `EMPIRICAL_VALIDATION_REQUIRED`

Paystack recommends key rotation. Webhook signatures use the secret key. Therefore a key change can overlap with events created/delivered/retried under a previous key assumption.

Before production release, NewYou needs an explicit rotation procedure proving that:

- API callers switch safely;
- webhook authentication does not discard legitimate in-flight/retried events during the approved overlap;
- old key authority ends deliberately;
- secrets never enter logs/evidence payloads;
- reconciliation can recover even if an event is rejected during rotation.

This does not block the core sandbox reconciliation proof but is required release-operational evidence.

---

### P2-F-008 — Persist both Paystack reference and provider transaction ID as evidence identifiers; neither becomes NewYou commercial identity

**Classification:** `SUPPORTED_BY_PROVIDER`

Paystack documents a unique transaction reference and separately warns that its numeric transaction ID should be represented as an unsigned 64-bit integer if stored. Some provider operations/evidence lookup use transaction ID rather than reference.

JIT implication, not Resource design:

- NewYou needs durable provider-evidence linkage sufficient to query/verify/reconcile the same Paystack transaction after restart;
- do not truncate provider transaction IDs into 32-bit storage;
- Paystack reference and transaction ID remain provider identifiers under a NewYou-owned Purchase Intent / Provider Attempt identity.

---

### P2-F-009 — Paystack `reversed` is not one NewYou lifecycle state

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack verification can report `reversed`; provider documentation associates reversal with refund/chargeback outcomes. NewYou already separates payment truth, refund truth, dispute truth and entitlement consequences.

Therefore:

> `verify.status == reversed` is conclusive evidence that the original successful charge is no longer an ordinary current-success state, but it is insufficient by itself to decide whether NewYou is observing a refund, dispute/chargeback loss, another provider reversal reason, or the exact component/access consequence.

Reconciliation must inspect the relevant refund/dispute/provider evidence and then let Commerce establish the correct commercial state. Entitlements follows the resulting authoritative Commerce consequence idempotently.

---

### P2-F-010 — Webhook absence is not negative payment truth

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack documents webhooks as the preferred success-notification mechanism, but browser return can be missing and webhook delivery can be delayed/retried. The transaction Verify API is therefore essential to restart/outage recovery.

NewYou must be able to settle this case without browser or webhook:

```text
provider payment succeeds
→ browser never returns
→ webhook unavailable/delayed/lost to local outage
→ NewYou restarts
→ durable Provider Attempt/reference remains
→ reconciliation verifies provider transaction
→ validates reference + actual amount + currency + expected purchase linkage
→ Commerce establishes payment truth once
→ Entitlements converges once
```

The browser is not a required recovery dependency.

---

### P2-F-011 — Current Product Law defines duplicate-payment access correction but not the exact money remedy for two genuinely successful one-off FP-002 collections

**Classification:** `NEWYOU_POLICY_DECISION`

Current governed Product Law states that Commerce records duplicate payment and that duplicate-payment correction leaves one valid right. That is sufficient to prevent duplicate Entitlements. It does **not** explicitly state whether an excess, genuinely successful second collection for the same one-off Purchase Intent must be automatically refunded in full, may enter another make-whole mechanism, or requires operator adjudication.

The CER working rule `CER-UPD-009` does specify full reversal/refund or governed make-whole handling, but its accepted scope is duplicate **ordinary recurring membership** purchase. It may not be silently generalized into FP-002 one-off Product Law.

This is the first Pass-2 candidate upstream Product delta. See `P2-UPSTREAM-CAND-001` and focused question `P2-Q-001`.

---

### P2-F-012 — The global OQ-004 wording and the FP-002 gate need explicit closure routing, not semantic hand-waving

**Classification:** `NEWYOU_POLICY_DECISION` / governance routing

Current `OQ-004` names failed-payment, subscription, webhook, proration, refund and chargeback behaviour. Current Roadmap makes `OQ-004` `BLOCKS_THIS_FP` for FP-002 while explicitly deferring recurring memberships from FP-002.

Consequences:

- FP-002 must prove the provider behaviours material to its one-off purchase/refund/dispute outcome;
- subscription/proration proof must not be pulled into FP-002 merely to satisfy the textual breadth of OQ-004;
- but the global governed `OQ-004` also must not be marked `RESOLVED` if subscription/proration remain unvalidated.

The smallest safe governance fix is likely to preserve OQ-004 history while explicitly recording a scoped FP-002 satisfaction/remaining-future subset, or to split/refine the gate through an authorised upstream amendment. This working document does not invent the governed identifier or amendment wording.

See `P2-UPSTREAM-CAND-002`.

## P2.3 Refined provider evidence-state matrix

| Paystack evidence | NewYou interpretation | May grant payment truth? | New Provider Attempt admission | Notes |
|---|---|---:|---|---|
| Initialize API success only | provider transaction/capability created | NO | normally NO while same capability remains usable | Needs later Verify before Commerce success |
| Initialize timeout/connection loss | unresolved provider-attempt creation | NO | CONDITIONAL / guarded | Resolve failure cut A/B/C; never equate timeout with failure |
| browser/callback `reference` | untrusted navigation evidence | NO | NO by itself | Can trigger reconciliation only |
| webhook `charge.success` with valid signature | authenticated success evidence | NO by itself | NO | Durably receive then reconcile |
| duplicate/resend of same event | duplicate evidence | NO new effect | NO | Expected normal condition |
| Verify `success`, exact ref/amount/currency match | strong provider success evidence | YES, through Commerce reconciliation only | NO | Still enforce purchase/admission/idempotency guards |
| Verify `success`, amount mismatch | invalid/mismatched evidence for purchase | NO | NO automatic replacement | Financial exception/reconciliation required |
| Verify `success`, currency mismatch | invalid/mismatched evidence for purchase | NO | NO automatic replacement | Never grant governed right |
| Verify `pending` / `processing` / `ongoing` | inconclusive | NO | normally NO | Reconcile later |
| Verify `failed` | failure evidence for that attempt | NO | MAYBE | New attempt requires NewYou guard/policy |
| Verify `abandoned` | non-success; terminality not proven generically | NO | CONDITIONAL | Refined by P2-F-002 |
| Paystack session-timeout terminal response | old provider session cannot complete under documented timeout rule | NO | YES subject to NewYou intent guard | Create distinct attempt, not new Purchase Intent |
| Verify `reversed` | original success reversed at provider layer; reason dimension needed | NO current-success | NO | Reconcile refund/dispute truth before access consequence |
| Refund `pending/processing/needs-attention` | refund truth unresolved | NO change inferred solely from provider state | N/A | Commerce owns refund lifecycle |
| Refund `processed` + transaction reversed | strong refund completion evidence | through Commerce refund transition | N/A | Component/order policy decides Entitlements consequence |
| dispute opened/awaiting feedback | contested provider evidence | not final reversal | N/A | Commerce state reversible/source-scoped per Product Law |
| final dispute lost + reversed | strong final reversal evidence | through Commerce final reversal | N/A | Current access consequence owner-mediated |

## P2.4 Lifecycle pressure — Purchase Intent vs Provider Attempt

Pass 2 makes the independent lifecycle dimensions explicit.

### A. NewYou Purchase Intent

Conceptual working states, not implementation enum:

```text
created
→ checkout_eligible
→ payment_unresolved
→ paid
→ commercially_closed_without_payment
→ reversal/refund correction as separate dimensions
```

Guards/invariants:

- NewYou identity is stable across browser retry/reconnect/provider attempts.
- A Purchase Intent owns the expected immutable order/amount/currency snapshot.
- More than one Provider Attempt may exist historically, but multiple attempts do not imply multiple purchases or multiple rights.
- `paid` requires reconciled matching provider evidence.
- `commercially_closed_without_payment` may be reached only when no still-authorised provider payment capability can later create an unhandled charge, or when any late money is explicitly governed by correction/reconciliation.

### B. Provider Attempt

Conceptual working states:

```text
prepared(reference fixed)
→ initialize_unknown | initialized
→ payment_capability_not_delivered | payment_capability_delivered
→ provider_nonfinal
→ provider_success_evidence | provider_failure_evidence | provider_session_expired
→ later refund/dispute/reversal evidence may append
```

Important rule:

`provider_session_expired` can permit a replacement Provider Attempt. It does not turn the expired reference into the NewYou Purchase identity, erase history, or automatically close a later financial correction if stale evidence arrives.

### C. Commerce payment truth

Provider events do not directly drive this lifecycle. Conceptually:

```text
unresolved
→ reconciled_paid
→ reconciled_failed/closed (when safe to conclude)
```

Refund/dispute/reversal are separate dimensions appended to historical payment truth rather than overwriting that a payment occurred.

### D. Entitlement consequence

```text
no grant
→ grant intent/transition from authoritative Commerce outcome
→ one current valid right
→ source-scoped end/suspension/revocation where governed
```

Duplicate provider evidence, duplicate jobs and duplicate Commerce→Entitlements handoffs converge on the same valid-right identity.

## P2.5 New adversarial scenarios

| Scenario | Failure being attacked | Safe NewYou result | Evidence/proof still needed |
|---|---|---|---|
| Initialize accepted; response lost before NewYou sees access code | unknown provider creation | same Purchase Intent remains unresolved; query old reference before replacement decision | `EV-001A` |
| access code durably stored; browser never gets response | delivery failure | resume same provider attempt; do not create second by default | `EV-001B` |
| browser got old payable URL; opens second tab / retries checkout | two live Paystack refs possible | only one Purchase Intent/right; avoid or govern simultaneous payable attempts | `EV-001C` |
| two distinct refs for same one-off purchase both succeed | excess money + duplicate access risk | exactly one right; extra collection enters governed remedy, currently Product decision gap | `EV-024` + `P2-Q-001` |
| Verify says abandoned before session timeout | false terminality risk | no access; do not assume old capability impossible without proof | `EV-009A` |
| session timeout conclusively prevents old checkout | replacement-attempt admission | create a new Provider Attempt under same Purchase Intent | `EV-009B` |
| provider `success`, charged amount < expected | partial/incorrect collection | no paid truth for governed fixed-price order | `EV-008` / `EV-018` |
| provider `success`, charged amount > expected | overcharge/misconfiguration | no ordinary paid truth; finance exception/remedy; no extra right | `EV-018` |
| `requested_amount` equals expected but `amount` differs | Partial Debit/money-integrity trap | validate actual `amount`; reject as ordinary FP-002 completion | `EV-018` |
| Paystack fee pass-through changes customer charge | Product-price mismatch | fail validation/configuration gate; do not silently weaken amount check | `EV-019` |
| Paystack dashboard enables unvalidated EFT/channel | unproved transport semantics | channel unavailable to participant until validated | `EV-020` |
| forged valid-shape webhook, wrong HMAC | ingress forgery | reject before durable provider evidence admission | `EV-006` / `EV-021` |
| same signed webhook delivered twice | replay/duplicate | two evidence receipts at most; one Commerce effect | `EV-004` |
| old `charge.success` resent after processed refund | stale success after correction | refund/reversal remains authoritative after reconciliation; no regrant | `EV-012` |
| Verify status `reversed` with refund evidence | state-collapse risk | reconcile refund lifecycle specifically | `EV-011` |
| Verify status `reversed` with chargeback evidence | state-collapse risk | reconcile dispute/final reversal specifically | `EV-013` |
| webhook signed around secret-key rotation | valid event rejected due key rollover | safe overlap/reconciliation procedure; no lost business truth | `EV-022` |
| NewYou DB commits payment, crashes before entitlement consequence | cross-domain partial failure | durable consequence resumes; one right | `EV-014` |
| NewYou crashes after provider success before any local success receipt | restart recovery | Verify from durable provider-attempt identity; one payment/right | `EV-014B` |

## P2.6 Empirical validation additions/refinements

### PAYSTACK-EV-001A — Initialize accepted / response lost before NewYou receives capability

- **Status:** `NOT_EXECUTED`
- **Question:** after an induced client/network timeout where Paystack may have accepted Initialize, how quickly/consistently does Verify by the predetermined reference expose the transaction and what status is returned?
- **Setup:** persist test Purchase Intent + fixed Paystack reference; proxy/fault-inject response loss after request send; never deliver returned capability to browser; poll Verify with bounded schedule.
- **Capture:** request timestamp, reference, proxy cut point, API transport outcome, every Verify response/status/timestamp, provider transaction ID if it appears.
- **Safe pass:** NewYou can deterministically identify the old provider attempt from its reference without issuing another blind Initialize.
- **Failure interpretation:** if transaction visibility is delayed/ambiguous, replacement-attempt admission needs a conservative bounded unresolved window/reconciliation policy; do not guess failure.
- **Credentials required:** Paystack test secret key + fault-injection proxy/harness.

### PAYSTACK-EV-001B — Initialize response retained / browser response lost

- **Status:** `NOT_EXECUTED`
- **Question:** can the same returned Paystack capability be safely re-presented/resumed after the participant-facing response is lost?
- **Setup:** complete Initialize; durably capture reference/access_code before suppressing the NewYou→browser response; reconnect and resume via selected checkout method.
- **Safe pass:** same provider transaction is resumed; no new reference/charge is created merely for presentation failure.
- **Failure interpretation:** chosen UI integration must use a different safe recovery path; do not automatically create a second payable attempt.

### PAYSTACK-EV-001C — Old payable capability remains live while participant retries checkout

- **Status:** `NOT_EXECUTED`
- **Question:** can two Paystack transactions with distinct references remain simultaneously payable when the first authorization URL/access code was already delivered?
- **Setup:** initialize attempt A, capture/deliver its capability; before paying A, create attempt B under same synthetic NewYou intent in the harness; attempt payments in both orders if test mode permits.
- **Safe outcome:** harness demonstrates why NewYou must guard attempt admission or demonstrates a provider property strong enough to remove the risk. If both can pay, Product remedy `P2-Q-001` is mandatory for residual race/error cases.
- **Capture:** both references/IDs, session expiry, completion results, webhook/API ordering.

### PAYSTACK-EV-009A — `abandoned` before/around session expiry

- **Status:** `NOT_EXECUTED`
- **Question:** can an attempt observed as `abandoned` later be resumed or become `success` before the configured payment-session timeout?
- **Setup:** create a checkout, cause abandonment at controlled points, Verify, then attempt resume/completion before and after timeout.
- **Safe pass:** exact selected-mode semantics are known and new-attempt admission can distinguish non-success from conclusively non-payable state.

### PAYSTACK-EV-009B — Documented payment-session timeout replacement

- **Status:** `NOT_EXECUTED`
- **Question:** once Paystack reports the documented session-timeout terminal condition, can the old capability still complete?
- **Safe pass:** old capability is unusable and a new Provider Attempt/reference is required; stale evidence still remains harmless to NewYou reconciliation.

### PAYSTACK-EV-018 — `amount` vs `requested_amount` integrity / Partial Debit exclusion

- **Status:** `NOT_EXECUTED`
- **Question:** does ordinary FP-002 checkout consistently return actual charged `amount == accepted order snapshot`, and is Partial Debit absent from the path/account configuration?
- **Safe pass:** all ordinary test transactions match actual amount/currency exactly; any differing `requested_amount` semantics are quarantined as out of scope; no right is granted from a partial charge.

### PAYSTACK-EV-019 — Customer fee pass-through configuration guard

- **Status:** `NOT_EXECUTED`
- **Question:** can any current Paystack account configuration used by NewYou increase the amount charged to the participant beyond the initialized/order amount?
- **Setup:** inspect account/support configuration and execute a representative live-like test where safe.
- **Safe pass for current Product Law:** actual participant charge remains exactly the NewYou accepted order amount. Merchant processing fees remain settlement/economic cost.
- **Failure interpretation:** STOP; either disable fee pass-through or obtain explicit upstream Product/offer disclosure authority before changing the invariant.

### PAYSTACK-EV-020 — Enabled-channel validation matrix

- **Status:** `NOT_EXECUTED`
- **Question:** for every channel NewYou proposes to enable at FP-002 release, do Initialize/checkout, success evidence, Verify, amount/currency integrity, duplicate/retry and refund/reconciliation satisfy the same invariants?
- **Rule:** a channel not covered by executed evidence remains disabled. Test-mode absence cannot be represented as production proof.

### PAYSTACK-EV-021 — Webhook signed-payload handling

- **Status:** `NOT_EXECUTED`
- **Question:** does ingress verify a known Paystack-signed payload exactly, reject altered bytes/invalid signature, and avoid admitting provider evidence before verification?
- **Setup:** capture test webhook body+signature; replay exact payload; mutate whitespace/key order/body bytes without recomputing signature; replay forged header.
- **Safe pass:** exact valid payload accepted once as evidence; mutations/forgeries rejected; duplicate exact valid event does not multiply business effect.

### PAYSTACK-EV-022 — Secret-key rotation with webhook retry overlap

- **Status:** `NOT_EXECUTED / RELEASE_ONLY`
- **Question:** what exact key-overlap procedure prevents legitimate webhook loss during key rotation, and can reconciliation recover any rejected event?
- **Safe pass:** rotation runbook proves no business truth depends on receiving one callback; old key authority ends deliberately; Verify/reconciliation repairs missed ingress.

### PAYSTACK-EV-024 — Two genuine successful Paystack refs for one one-off Purchase Intent

- **Status:** `NOT_EXECUTED / BLOCKED_ON_P2-Q-001_FOR_FINAL_REMEDY`
- **Question:** can two distinct references both settle successfully under test conditions when they originate from one synthetic NewYou purchase intent, and can NewYou deterministically admit one while identifying the other as excess collection?
- **Safe invariant regardless of policy answer:** exactly one valid governed right; neither callback arrival order nor provider customer identity selects the commercial winner.
- **Money remedy:** governed Product answer required by `P2-Q-001`.

## P2.7 Candidate upstream deltas — not governed decisions

### P2-UPSTREAM-CAND-001 — One-off excess collection remedy

**Authority level if accepted:** Product / Decision Register, because this changes the customer's commercial remedy rather than a provider mechanism.

Current authority already establishes:

- duplicate payment remains Commerce truth;
- duplicate-payment correction leaves one valid right;
- Entitlements must not multiply access.

Missing explicit rule:

- what NewYou owes the customer when two distinct successful provider collections correspond to one admissible one-off FP-002 Purchase Intent.

**Recommended direction for discussion, not authority:**

> Admit exactly one collection to satisfy the Purchase Intent under NewYou's deterministic commercial ordering. Every additional successful collection attributable to that same one-off intent is excess money, must never create another right, and should be refunded in full automatically where the provider path is safely available; if automatic refund is unavailable/ambiguous/failed, create visible Finance make-whole work until the customer is made whole. Preserve truthful history for both provider collections and the correction.

This mirrors the safety principle already accepted for duplicate recurring membership collection without silently claiming that recurring working doctrine governs FP-002.

### P2-UPSTREAM-CAND-002 — OQ-004 scoped closure routing

**Authority level if accepted:** governance/Open Work/Decision Register routing at the same level that owns OQ-004 status.

Need:

- define which Paystack evidence closes the FP-002 one-off subset;
- preserve subscription/proration/future recurring validation as open until its activating Feature Pack;
- prevent a misleading global `OQ-004 RESOLVED` declaration while future clauses remain untested;
- prevent future subscription/proration work from blocking the explicitly once-off FP-002 outcome contrary to Roadmap scope.

No new OQ identifier is invented here.

### P2-UPSTREAM-CAND-003 — Customer-paid payment-processing fee / surcharge policy

**Current disposition:** `NO_UPSTREAM_CHANGE_NEEDED_IF_DISABLED`.

If NewYou absorbs Paystack processing fees and the customer is charged the exact accepted Product price, current authority is coherent.

Only if Product wants a customer-visible processing surcharge/fee pass-through does an upstream offer/pricing/disclosure decision become necessary. Provider configuration cannot create that commercial promise by itself.

## P2.8 Focused Product question

### P2-Q-001 — Excess collection for a one-off FP-002 purchase

Current Product Law gives us the entitlement result but not a complete money-remedy rule.

**Question for Product authority:**

> If two distinct Paystack transactions both genuinely succeed for the same one-off NewYou FP-002 Purchase Intent, should the governed rule be: **exactly one collection satisfies the purchase; every additional successful collection is excess money and must be refunded in full automatically where safely possible, otherwise remain visible Finance make-whole work until resolved; it never creates a second entitlement/right**?

Recommended answer: **YES**. It is the simplest customer-safe rule, closes the ambiguity without letting callback order choose commercial truth, and composes with DEC-300's existing “one valid right” rule.

## P2.9 Pass-2 closure impact

Pass 2 does **not** change the current disposition:

`OQ-004 BLOCKED ON EMPIRICAL TESTS`.

It improves the closure definition:

1. `EV-001A/B/C` must prove safe initialization/presentation ambiguity handling.
2. `EV-004/005/006/021` must prove at-least-once authenticated webhook ingress without duplicate business effect.
3. `EV-007/014/014B` must prove browser/webhook-independent restart recovery.
4. `EV-008/018/019` must prove exact actual amount/currency integrity under current fee/configuration assumptions.
5. `EV-010/011/012/013` must prove refund/dispute/reversal reconciliation and stale-success resistance.
6. every enabled FP-002 payment channel must have executed applicable proof (`EV-020`), or remain disabled.
7. `P2-Q-001` must be governed if the current authority is judged insufficient for excess one-off collection remedy.
8. OQ-004 closure/status routing must distinguish the FP-002 subset from future recurring/proration validation without falsely closing the global gate.
9. production release additionally needs the key-rotation/live-mode evidence classified `RELEASE_ONLY`; test mode alone cannot prove settlement or unavailable live-only channel behaviour.

## P2.10 Next pass targets

Pass 3 should attack, in order:

1. refund ambiguity and double-refund prevention as a lifecycle independent of payment;
2. refund after partial/full entitlement consumption and exact DEC-300/§21R consequence mapping;
3. dispute-open → evidence → win/loss → stale success/reversal reordering;
4. provider Customer/email identity changes and purchaser/recipient separation;
5. metadata/data-minimisation and financial-evidence retention boundaries;
6. webhook event identity/deduplication strategy versus transaction/reference identity;
7. exact test-mode versus controlled-live evidence split;
8. whether any further genuine Product/Architecture upstream gap exists before sandbox execution.

Do not expand into recurring architecture beyond what is necessary to keep OQ-004 routing coherent.


## P2.11 Pass-2 primary-source evidence additions

**Access date for all entries below:** 2026-10-08.

| Evidence ID | First-party source | What it supports | Evidence class |
|---|---|---|---|
| `PS-P2-001` | https://paystack.com/docs/api/transaction/ | Transaction APIs, provider reference/transaction identifiers and server-side transaction operations. | DOCUMENTED FACT |
| `PS-P2-002` | https://paystack.com/docs/api/errors/transaction/ | Duplicate reference error; payment-session timeout requires a new transaction; provider transaction error vocabulary. | DOCUMENTED FACT |
| `PS-P2-003` | https://paystack.com/docs/payments/verify-payments/ | Verify response fields; transaction status is `data.status`; amount/currency/reference/customer/authorization/requested_amount evidence. | DOCUMENTED FACT |
| `PS-P2-004` | https://paystack.com/docs/payments/partial-debits/ | `amount` is actual amount charged and `requested_amount` is intended amount for Partial Debit; feature is request-only. | DOCUMENTED FACT |
| `PS-P2-005` | https://paystack.com/docs/payments/webhooks/ | HMAC-SHA512 webhook signature, acknowledgement/retry behaviour, supported events and webhook-vs-polling role. | DOCUMENTED FACT |
| `PS-P2-006` | https://paystack.com/docs/api/webhook-events/ | Event `_id`, underlying resource/transaction ID, event lookup and non-idempotent resend. | DOCUMENTED FACT |
| `PS-P2-007` | https://support.paystack.com/en/articles/10609026 | Duplicate webhook delivery is possible; safely handle repeated events before giving value. | DOCUMENTED FACT / FIRST-PARTY SUPPORT |
| `PS-P2-008` | https://paystack.com/docs/api/refund/ | Create/List/Fetch Refund shape; Create exposes no documented idempotency key; List can reconcile transaction refunds. | DOCUMENTED FACT + DOCUMENTATION SILENCE FOR IDEMPOTENCY |
| `PS-P2-009` | https://paystack.com/docs/api/dispute/ | Dispute API lifecycle vocabulary and transaction-ID filtering. | DOCUMENTED FACT |
| `PS-P2-010` | https://paystack.com/docs/payments/manage-disputes/ | First-party dispute operational/reconciliation guidance. | DOCUMENTED FACT |
| `PS-P2-011` | https://paystack.com/docs/api/authentication/ | Test/live separation, secret-key security, rotation guidance, test-mode limitations. | DOCUMENTED FACT |
| `PS-P2-012` | https://paystack.com/docs/payments/payment-channels/ | South African channel-specific flows including EFT and Capitec Pay; channel-specific validation pressure. | DOCUMENTED FACT |
| `PS-P2-013` | https://paystack.com/za/pricing | South African merchant transaction fees. | DOCUMENTED FACT |
| `PS-P2-014` | https://support.paystack.com/en/articles/2130306 | Paystack account option to pass transaction fees to customers; if enabled the fee is added to checkout total. | DOCUMENTED FACT / FIRST-PARTY SUPPORT |
| `PS-P2-015` | https://paystack.com/docs/payments/subscriptions/ | Provider-managed Subscriptions; failed subscription charge is not retried in the same cycle. | DOCUMENTED FACT / FUTURE_RECURRING_ONLY |
| `PS-P2-016` | https://paystack.com/docs/payments/recurring-charges/ | Reusable authorization, provider instrument signature, and original-email binding for later charges. | DOCUMENTED FACT / FUTURE_RECURRING_ONLY |
| `PS-P2-017` | https://paystack.com/docs/changelog/api/ | September 2026 Webhook Events API addition and current provider API-change context. | DOCUMENTED FACT |

### Evidence-discipline note

No item in this section is an empirical NewYou result. `DOCUMENTATION SILENCE` means the first-party contract inspected does not state the required behaviour; it is not proof that the provider lacks the behaviour. Any claim depending on such silence remains `EMPIRICAL_VALIDATION_REQUIRED` or `DOCUMENTATION_AMBIGUOUS` until tested/confirmed by Paystack.


---

# Pass 3 — Refund/Dispute Lifecycle, Provider Identity and Sensitive-Data Boundary

- **SemVer successor:** `v0.2.0 → v0.3.0`
- **Pass date:** 2026-10-08
- **Pass status:** COMPLETE FOR DOCUMENTARY PRESSURE / EMPIRICAL AND RELEASE CONFIRMATION OUTSTANDING
- **Change class:** MINOR — adds/refines validation semantics, empirical cases and operational/release obligations; no governed authority is changed.
- **Predecessor prefix SHA-256:** `0a2bbf6f203b66bb8b109976c292b5eeefc0ab1ce329cf0013b4d630e9e4d54a`
- **Live repository baseline:** unchanged from Pass 2 unless a later pass explicitly rechecks and records movement.

## P3.1 Objective

Pass 3 attacks correction paths after money has moved. These paths are more dangerous than ordinary failure because stale success evidence remains historically true while refund/dispute/reversal truth changes what Commerce and Entitlements may do now.

The pass keeps separate:

```text
successful payment occurred
refund was requested
refund was processed/failed
chargeback/dispute exists
chargeback/dispute resolved
current commercial validity
current Entitlement consequence
historical delivery/consumption
provider settlement/fee economics
```

None of those dimensions may be compressed into a single provider-derived `payment_status` state machine.

## P3.2 New/refined findings

### P3-F-001 — Refund is an independent NewYou lifecycle, not a mutation of historical payment truth

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack documents refund states `pending`, `processing`, `needs-attention`, `failed`, and `processed`. It also maps those states onto the original provider transaction as `Reversal Pending`, `Success`, or `Reversed`.

NewYou must not mirror that provider collapse.

Provider-independent model:

```text
historical payment: reconciled_paid   # remains true that money was collected
refund intent: requested
refund provider operation: unresolved | pending | processing | needs_attention | failed | processed
Commerce refund truth: unresolved | completed | failed/closed | correction_required
Entitlement consequence: separate owner-mediated transition
```

A failed refund restores the provider transaction to `success`; that does not mean the NewYou refund request never existed. A processed refund changes current commercial validity according to Product Law while preserving historical payment/delivery/refund evidence.

---

### P3-F-002 — A processed partial refund can make provider transaction status too lossy for component-level NewYou truth

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack supports partial refunds. Its refund documentation states that a processed refund moves the associated transaction to `reversed`. That transaction-level provider status does not encode NewYou's component allocation or which portion of a bundle remains commercially valid.

For FP-002 this is decisive:

- the immutable NewYou order allocation snapshot determines the intended component refund amount;
- Commerce records the refund against the specific NewYou commercial source/component semantics;
- Verify `reversed` is supporting evidence, not sufficient component-level truth;
- Entitlements changes only the affected component unless governed order-level rules say otherwise;
- a separately valid assessment/right must survive a plan-component refund when Product Law requires it.

Therefore **transaction status alone cannot drive post-refund Entitlements.**

---

### P3-F-003 — Refund creation is an irreversible-effect ambiguity seam because Create Refund exposes no documented idempotency key

**Classification:** `DOCUMENTATION_AMBIGUOUS` + `EMPIRICAL_VALIDATION_REQUIRED`

Current Create Refund accepts the source transaction and amount/currency but exposes no documented client idempotency key. Paystack provides List Refunds by transaction ID and Fetch Refund by refund ID, which creates a reconciliation path after the provider refund object exists.

Unsafe behaviour:

```text
POST Create Refund
→ connection drops
→ assume failure
→ POST Create Refund again
```

For a partial component refund, two accepted requests could refund more than NewYou intended even if the combined amount remains below the original charge.

NewYou needs one stable internal **Refund Intent** identity with immutable:

- source NewYou commercial operation/order/payment linkage;
- source provider transaction linkage;
- intended amount/currency in minor units;
- reason/component/remedy basis;
- current provider-operation evidence;
- terminal/needs-attention/reconciliation state.

This is lifecycle semantics only, not a Resource/table mandate.

---

### P3-F-004 — Paystack supports multiple partial refunds conceptually, so duplicate-refund safety cannot rely on “provider will only allow one refund”

**Classification:** `EMPIRICAL_VALIDATION_REQUIRED`

Current first-party developer documentation expressly supports partial and full refunds and exposes a list of refunds per source transaction. Historical first-party Paystack product material also describes multiple refunds against the same transaction until the remaining amount is exhausted, but current API documentation does not fully specify concurrent duplicate-request behaviour or cumulative enforcement semantics.

Safe conclusion:

> NewYou must own exact refund-intent admission/idempotency and must not rely on a one-refund-per-transaction provider invariant.

Empirical tests must attack simultaneous and timeout-retry duplicate partial refund requests.

---

### P3-F-005 — `needs-attention` is a real operational refund state and can require customer bank details

**Classification:** `SUPPORTED_BY_PROVIDER` + `RELEASE_ONLY`

Paystack documents that some refunds enter `needs-attention` when customer bank details are unavailable and must be retried with bank-account details. This is available for bank-transfer refunds in South Africa according to first-party support material.

NewYou consequence:

- `needs-attention` is not refund completion and must remain visible work;
- Entitlements must not infer completion merely because a refund was requested;
- exact customer communication and operator workflow belongs to FP-002/FP-006 JIT/operations;
- **data minimisation recommendation:** do not build NewYou bank-account-detail capture merely because Paystack exposes an API path if the provider Dashboard can safely complete this exceptional operation. If a NewYou-native flow is later justified, Privacy/Security/retention scope must be explicitly reviewed first.

Provider Dashboard action remains execution evidence; Commerce reconciles completion afterward.

---

### P3-F-006 — Dispute notification has a hard operational deadline and first-party Paystack sources are not perfectly consistent across markets

**Classification:** `DOCUMENTATION_AMBIGUOUS` + `RELEASE_ONLY`

Paystack's general developer dispute guide states that disputes should be handled within 16 hours and may be automatically accepted if the deadline elapses. More recent location-specific first-party South African support material states **48 hours** for chargeback resolution, with business-day/weekend handling, and Paystack's South African terms also reference a 48-hour chargeback period (with a separate fraud-dispute period).

This inconsistency is material operational evidence, not a reason to guess.

Before paid release NewYou must obtain/record the current South-African account-specific dispute SLA and configure operator alert/escalation to the stricter confirmed contract. A stale documentation number must not be frozen into Product Law.

Regardless of exact hours:

- dispute intake is time-sensitive mandatory work;
- missing a webhook cannot be the only detection path;
- periodic API/Dashboard reconciliation must surface awaiting-merchant-feedback disputes;
- automatic provider acceptance can move money even if NewYou did nothing, so restart/outage recovery is mandatory.

---

### P3-F-007 — Dispute provider state and NewYou commercial consequence are separate and reversible until final outcome

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack exposes dispute states including `awaiting-merchant-feedback`, `awaiting-bank-feedback`, `pending`, and `resolved`, plus create/remind/resolve webhooks. Paystack also documents that issuing banks/card schemes ultimately decide outcomes.

This composes with existing NewYou Product Law:

```text
dispute opened / confirmed
→ Commerce contested state
→ only source-scoped reversible access consequence where governed
→ dispute resolves in merchant favour => restore/remove hold idempotently
→ dispute finally lost / money reversed => Commerce final reversal
→ Entitlements applies source-scoped final consequence
```

A provider `resolved` label alone still needs resolution/outcome details; NewYou must not assume all `resolved` disputes are merchant losses.

---

### P3-F-008 — Stale `charge.success` evidence after a refund/dispute is historically valid but must not re-win current precedence

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

The Webhook Events API allows non-idempotent resend. Therefore a historical `charge.success` event can be deliberately or accidentally delivered after later refund/dispute evidence.

Correct rule:

> Event arrival time is never Commerce precedence. Reconciliation evaluates the provider transaction and applicable refund/dispute evidence against durable NewYou history/current commercial state.

A late success event may prove that the original charge happened; it cannot erase a later authoritative refund/final reversal or re-grant revoked access.

This is an essential `EV-012`/restart/concurrency proof, not an edge-case nicety.

---

### P3-F-009 — Paystack Customer/email is payment-provider evidence, never NewYou Identity authority

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack transactions/customers expose provider customer IDs/codes and email. The Customer API can fetch by email/customer code and the Paystack Dashboard groups customer transaction activity. These provider objects are useful for provider operations but cannot become canonical person/account/grantee identity.

NewYou invariants:

- provider `customer.id` / `customer_code` identifies a Paystack-side customer record only;
- provider email is payment/contact evidence for that provider operation, not proof of the current NewYou Account owner;
- same/matching email must not merge NewYou accounts or grant access;
- NewYou email change must not rewrite historical transaction identity;
- purchaser, recipient and participant remain separate concepts;
- the Purchase Intent/Order stores its NewYou purchaser/recipient relationship independently of Paystack Customer.

For future reusable authorizations, Paystack's original-email binding becomes a payment-instrument contract detail, not a reason to freeze NewYou canonical email or identity.

---

### P3-F-010 — Provider metadata is externally visible/retained integration data and must be minimised

**Classification:** `SUPPORTED_BY_PROVIDER` + NewYou privacy constraint

Paystack metadata is returned through API responses, and `custom_fields` can be visible in the Paystack Dashboard. It is not an appropriate carrier for health, temperament, plan, safety, assessment answers/results, or other unnecessary participant-sensitive data.

Safe FP-002 metadata rule:

- use only opaque/minimal commercial correlation values when needed;
- avoid raw health/safety/temperament/plan data entirely;
- avoid using PMR or canonical Account identity merely for convenience if an opaque purchase/provider-attempt correlation is sufficient;
- never put secrets, authorization tokens or privileged context into metadata;
- provider metadata remains evidence/convenience, not NewYou business authority.

This is consistent with Privacy Pre-JIT minimisation and provider-boundary doctrine.

---

### P3-F-011 — Hosted Paystack Checkout is the correct security direction; custom raw-card collection is unjustified for FP-002

**Classification:** `SUPPORTED_BY_PROVIDER` + `RELEASE_ONLY`

Paystack states that its custom Cards API is for PCI-DSS-compliant businesses and that non-PCI-certified businesses can use Paystack Checkout/Mobile SDKs for card payments. Paystack itself is a PCI DSS Level 1 service provider.

For FP-002 there is no authority-backed requirement for NewYou to collect raw card PAN/CVV.

Recommended bounded mechanism:

- use Paystack-hosted/Paystack UI payment collection;
- keep secret keys server-side;
- NewYou receives provider transaction/authorization evidence but not raw card credentials;
- do not enable the raw Cards API/custom card form without a separate justified security/compliance decision.

This **does not claim that NewYou has zero PCI obligations**. Exact merchant PCI scope/SAQ/compliance remains a release/legal/security confirmation, not a provider-document inference.

---

### P3-F-012 — Webhook event `_id` is useful evidence but cannot replace business idempotency and may not be present in the delivered event payload

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION` + `EMPIRICAL_VALIDATION_REQUIRED`

The Webhook Events API records an event `_id`, underlying resource/transaction ID, delivery status, trial count and endpoint response. Resending the same event `_id` is explicitly non-idempotent and can deliver it again.

The displayed delivered `event_payload` example contains the business event/payload rather than exposing `_id` as part of the event body. Therefore NewYou must not design ingress correctness around a provider event ID being available in every webhook POST without empirical confirmation.

Safe rule:

- exact provider-event IDs are useful operational evidence when available through provider event history;
- durable ingress may retain enough evidence to investigate duplicate delivery;
- reconciliation/business idempotency keys on stable NewYou/provider resource identity and current authority, not event-arrival identity alone;
- two distinct event records about one transaction must still converge on one business effect.

## P3.3 Refund lifecycle model

The meaningful lifecycle dimensions are explicit.

### Refund Intent — NewYou-owned commercial operation identity

Conceptual states:

```text
proposed
→ authorised_to_initiate
→ provider_submission_unresolved | provider_refund_identified
→ provider_pending | provider_processing | provider_needs_attention
→ provider_processed | provider_failed
→ Commerce completed | Commerce failed/closed | correction_required
```

#### Guards

- refundability and amount come from current Product Law and immutable order/payment allocation, not current list price;
- exact source payment/transaction must be reconciled first;
- intended cumulative refund must not exceed NewYou-authorised refundable amount;
- only one active execution for the same Refund Intent may originate a provider mutation at a time;
- timeout does not authorize blind second Create Refund;
- `needs_attention` requires current operator authority and safe handling of any bank details;
- a provider `processed` result is reconciled before Entitlements consequence;
- a provider `failed` result does not delete/reforge the Refund Intent history.

#### Idempotency identity

One NewYou Refund Intent retains one stable identity across API call, timeout, List/Fetch Refund reconciliation, webhook duplicates, operator intervention, restart and final Entitlement consequence.

#### Terminal states

`Commerce completed` and `Commerce failed/closed` are terminal for that Refund Intent, subject to explicit correction/reconciliation if later provider evidence proves the terminal classification wrong. A new separately authorised additional partial refund is a new Refund Intent, not a retry of the first.

## P3.4 Dispute lifecycle model

Conceptual independent dimensions:

```text
dispute discovered
→ awaiting NewYou response / provider investigation
→ responded/contested or merchant-accepted
→ provider/bank pending
→ resolved_merchant_favour | resolved_customer_favour/final_reversal
→ possible later provider reopening/pre-arbitration where applicable
```

Guards/invariants:

- webhook/email/dashboard/API are evidence/detection channels, not Commerce finality;
- current market/account deadline is an operational guard;
- NewYou must detect unresolved disputes even if webhook delivery fails;
- dispute evidence must contain only necessary transaction/delivery proof;
- a dispute does not automatically prove fraud or justify account-wide punishment;
- source-scoped access effects follow current Product Law;
- final loss/reversal cannot erase historical delivery/payment evidence;
- independently paid later rights remain independent;
- provider reopening/pre-arbitration means `resolved` cannot always be modelled as irreversible universal terminality without provider/account evidence.

## P3.5 Additional adversarial scenarios

| Scenario | Provider observation | NewYou pressure | Safe result |
|---|---|---|---|
| component refund Create returns timeout | unknown whether refund exists | duplicate partial refund risk | reconcile List Refunds/source transaction before another mutation |
| two refund workers race | two POSTs may be accepted | excess refund | one Refund Intent execution owner; empirical concurrency proof |
| first partial refund processed, second separately authorised later | provider transaction may already read `reversed` | provider transaction status loses remaining component semantics | NewYou refund ledger/allocation governs remaining refundable amount |
| refund pending then failed | transaction goes reversal-pending then success | don't prematurely end right if Product consequence requires completed refund | Commerce refund remains unresolved until final evidence; failure handled explicitly |
| refund needs attention | provider needs bank details | operational stall / sensitive-data expansion | visible Finance work; no fake completion; prefer provider-hosted exceptional handling |
| refund processed, old charge.success resent | stale event ordering | accidental re-grant | reconcile current refund/payment history; no regrant |
| chargeback created while entitlement active | contested payment | premature permanent revocation | source-scoped reversible consequence per Product Law |
| dispute webhook missed during outage | no local callback | deadline risk | scheduled/API/dashboard reconciliation surfaces it |
| dispute auto-accepted after missed deadline | provider reverses money without NewYou action | local state stale | reconciliation discovers final reversal; Entitlements converges; incident evidence |
| dispute resolved merchant-favour then old create/remind replayed | stale provider evidence | re-suspension | current Commerce dispute authority wins |
| dispute later reopened/pre-arbitration | earlier resolved observation exists | false terminality | append new dispute phase/evidence; do not erase prior result |
| Paystack customer code points to same email as another NewYou Account | provider grouping | identity takeover/cross-account access | provider customer never authorises NewYou identity/access |
| NewYou user changes email after old transaction | provider historical email differs | reconciliation mismatch | transaction tied to Purchase Intent/Account lineage, not current email equality |
| provider metadata contains health answer | privacy leakage | unnecessary processor exposure | prohibited by metadata-minimisation contract |
| custom Cards API accidentally enabled | raw card data touches NewYou | PCI/security scope expansion | STOP; use hosted Checkout unless separately authorised/compliant |

## P3.6 Empirical/release validation additions

### PAYSTACK-EV-025 — Refund Create timeout reconciliation

- **Status:** `NOT_EXECUTED`
- **Question:** when Create Refund is accepted but the HTTP response is lost, how soon can List Refunds by source transaction identify the created refund, and what fields distinguish it sufficiently to correlate to the NewYou Refund Intent?
- **Setup:** create known refundable test transaction; fault-inject response loss at refund creation; poll List Refunds and Fetch discovered refund.
- **Safe pass:** NewYou can reconcile before issuing another provider refund mutation.
- **Failure interpretation:** if provider visibility is delayed/ambiguous, NewYou must remain unresolved and require conservative/manual reconciliation rather than blind retry.

### PAYSTACK-EV-026 — Concurrent duplicate partial-refund creation

- **Status:** `NOT_EXECUTED`
- **Question:** what does Paystack do when two identical partial refund requests are submitted concurrently or near-concurrently for one transaction?
- **Capture:** HTTP outcomes, number of provider refund objects, amounts, cumulative refunded amount, webhook sequence, source transaction state.
- **Safe NewYou invariant:** only one provider mutation is admitted for one Refund Intent regardless of provider behaviour.

### PAYSTACK-EV-027 — Multiple authorised partial refunds and cumulative amount

- **Status:** `NOT_EXECUTED`
- **Question:** how does Paystack expose remaining refundable amount and source transaction state across sequential legitimate partial refunds?
- **Why:** FP-002 bundle component correction may be partial relative to original transaction; provider `reversed` cannot become component truth.

### PAYSTACK-EV-028 — Refund failed after pending/processing

- **Status:** `NOT_EXECUTED`
- **Question:** verify documented transition back to provider transaction `success`, webhook ordering, and NewYou ability to preserve failed Refund Intent without changing historical payment truth.

### PAYSTACK-EV-029 — Needs-attention refund in South African test/live-confirmable path

- **Status:** `NOT_EXECUTED / MAY_REQUIRE_CONTROLLED_LIVE_CONFIRMATION`
- **Question:** which FP-002 channel/refund paths can enter `needs-attention` for the NewYou South African account, and what exact operator data/action is required?
- **Safe result:** unresolved work is visible and no NewYou Entitlement consequence claims refund completion early.

### PAYSTACK-EV-030 — Dispute detection without webhook

- **Status:** `NOT_EXECUTED / RELEASE_ONLY`
- **Question:** can a scheduled List Disputes reconciliation reliably surface an awaiting-response dispute independently of webhook/email delivery?
- **Safe result:** no dispute SLA depends on one notification channel.

### PAYSTACK-EV-031 — South Africa dispute deadline contract confirmation

- **Status:** `NOT_EXECUTED / RELEASE_ONLY / PROVIDER_CONFIRMATION_REQUIRED`
- **Question:** what exact chargeback and fraud-dispute response deadlines apply to the activated NewYou South African Paystack business at launch, including weekend/public-holiday semantics?
- **Evidence:** current Paystack account terms/support confirmation plus controlled Dashboard/API timestamps if safely available.
- **Reason:** first-party general developer docs and South-African-specific support/terms are not perfectly aligned.

### PAYSTACK-EV-032 — Dispute create/remind/resolve duplicate/reorder

- **Status:** `NOT_EXECUTED`
- **Question:** prove duplicate/reminded/out-of-order dispute events converge on current API-reconciled Commerce state and cannot repeatedly suspend/revoke/restore one entitlement source.

### PAYSTACK-EV-033 — Old charge.success resend after refund/dispute finality

- **Status:** `NOT_EXECUTED`
- **Setup:** produce success; complete refund or controlled dispute-like terminal state where test support permits; use Webhook Events resend on historical success.
- **Safe pass:** historical success evidence is recorded/recognised but cannot overturn later Commerce correction or grant another Entitlement.

### PAYSTACK-EV-034 — Provider customer/email identity non-authority

- **Status:** `NOT_EXECUTED`
- **Question:** exercise transactions from changed/same provider emails/customer records in a harness and prove NewYou reconciliation always uses its Purchase Intent/Account/purchaser mapping rather than provider customer equality.

### PAYSTACK-EV-035 — Metadata minimisation

- **Status:** `NOT_EXECUTED`
- **Question:** inspect Paystack Dashboard/API/webhook surfaces for approved opaque metadata and prove no health, temperament, plan, assessment answer/result, PMR-by-default, secret or unnecessary Account data is sent.

### PAYSTACK-EV-036 — Hosted Checkout card-data boundary

- **Status:** `NOT_EXECUTED / RELEASE_SECURITY_PROOF`
- **Question:** prove the selected FP-002 browser flow sends raw card credentials directly to Paystack-controlled UI/endpoints and NewYou application/logging/telemetry never receives PAN/CVV.
- **Boundary:** exact PCI merchant obligations still require the applicable compliance/security process; this test proves architecture/data flow, not legal certification.

### PAYSTACK-EV-037 — Webhook event-ID availability and dedupe evidence

- **Status:** `NOT_EXECUTED`
- **Question:** determine whether delivered webhook requests expose the Webhook Events `_id` anywhere accessible to NewYou ingress; compare an original and provider-resend delivery.
- **Safe result:** business idempotency remains correct either way; event ID is treated as evidence optimization only.

## P3.7 Upstream/JIT disposition

### No new Product-law gap found in refund component consequence

Current Product Law already gives the critical FP-002 semantics:

- refundability/irreversible-use boundaries (`DEC-045`);
- immutable component allocation/refund basis (`DEC-299` / §21R.1);
- Commerce refund/dispute authority and one-valid-right correction (`DEC-300` / §21R.2);
- component-level Entitlement consequence and preserved history.

Provider refund states therefore belong in JIT/reconciliation proof, not upstream Product invention.

### No Product-law decision is needed to use hosted Paystack Checkout

Hosted/provider-owned card entry is the least-scope mechanism consistent with current security/privacy architecture. Raw Cards API use would require new evidence/justification; absence of that justification is sufficient to exclude it from FP-002 planning.

### Operational upstream still needed: P2-Q-001 and OQ-004 scoped closure routing

Pass 3 does not add another Product question. The outstanding upstream candidate remains one-off excess-collection remedy (`P2-Q-001`), plus governance routing for global OQ-004 versus the FP-002 subset.

## P3.8 Pass-3 primary-source evidence additions

**Access date:** 2026-10-08.

| Evidence ID | First-party source | Material evidence | Classification |
|---|---|---|---|
| `PS-P3-001` | https://paystack.com/docs/payments/refunds/ | Partial/full refund, refund statuses, transaction-status mapping, webhook events, needs-attention. | DOCUMENTED FACT |
| `PS-P3-002` | https://paystack.com/docs/api/refund/ | Create/List/Fetch/Retry Refund fields and provider refund identifiers. | DOCUMENTED FACT |
| `PS-P3-003` | https://paystack.com/docs/api/errors/refund/ | Fully-reversed and refund error evidence. | DOCUMENTED FACT |
| `PS-P3-004` | https://support.paystack.com/en/articles/2127106 | South Africa bank-transfer refund availability, needs-attention/dashboard retry, processing-fee non-refundability. | DOCUMENTED FACT / FIRST-PARTY SUPPORT |
| `PS-P3-005` | https://support.paystack.com/en/articles/2130434 | First-party refund/transaction status relationship. | DOCUMENTED FACT / FIRST-PARTY SUPPORT |
| `PS-P3-006` | https://paystack.com/docs/payments/manage-disputes/ | Dispute flow, automatic handling warning, evidence upload, create/remind/resolve events. | DOCUMENTED FACT |
| `PS-P3-007` | https://paystack.com/docs/api/dispute/ | Dispute statuses/API and transaction-ID correlation. | DOCUMENTED FACT |
| `PS-P3-008` | https://support.paystack.com/en/articles/2125378 | South Africa chargeback timing and weekend/business-day handling. | DOCUMENTED FACT / LOCATION-SPECIFIC FIRST-PARTY SUPPORT |
| `PS-P3-009` | https://paystack.com/za/terms | South African merchant dispute/compliance obligations; used only for release/provider-contract validation, not Product Law. | FIRST-PARTY CONTRACTUAL EVIDENCE |
| `PS-P3-010` | https://paystack.com/docs/api/customer/ | Provider customer code/email/transactions/authorizations and update surface. | DOCUMENTED FACT |
| `PS-P3-011` | https://paystack.com/docs/payments/metadata/ | Metadata/custom-fields visibility and API return behaviour. | DOCUMENTED FACT |
| `PS-P3-012` | https://paystack.com/docs/payments/payment-channels/ | Cards API PCI requirements and Paystack Checkout direction for non-certified businesses. | DOCUMENTED FACT |
| `PS-P3-013` | https://paystack.com/compliance | Paystack PCI DSS Level 1 / security-compliance claims. | FIRST-PARTY COMPLIANCE EVIDENCE |
| `PS-P3-014` | https://paystack.com/docs/api/webhook-events/ | Event `_id`, resource ID, trial count, response evidence, non-idempotent resend. | DOCUMENTED FACT |

## P3.9 Pass-3 disposition

`OQ-004 BLOCKED ON EMPIRICAL TESTS` remains unchanged.

Material advancement:

- refund lifecycle is now explicitly independent of payment history and Entitlement state;
- partial refund proves provider transaction status is too lossy for NewYou component semantics;
- refund timeout/double-refund risk has a precise empirical suite;
- dispute SLA/detection is identified as a release-operational obligation with a South-African documentation inconsistency requiring provider/account confirmation;
- stale success after refund/dispute is explicitly precedence-tested;
- Paystack Customer/email is formally non-authoritative for NewYou identity;
- metadata and raw-card-data boundaries are explicit;
- webhook event ID is evidence only, not idempotency authority.

## P3.10 Next pass targets

Pass 4 should attack:

1. settlement/reconciliation and what NewYou does when Verify/refund/dispute evidence disagree temporarily;
2. authorization/card evidence retained from once-off transactions and whether FP-002 should deliberately discard/not activate reusable-authorisation behaviour;
3. exact provider reference-generation constraints and entropy/guessability requirements versus NewYou opaque external identifiers;
4. support/Finance correction powers and audit boundary for manual reconciliation;
5. provider outage/backlog admission control and participant UX under degraded checkout;
6. test-mode evidence that is impossible to promote to production proof;
7. exact OQ-004 closure manifest split into `FP-002 required`, `release-only`, and `future-recurring-only` rows;
8. final upstream delta audit before moving to sandbox execution.

---

# Pass 4 — Settlement Independence, Once-Off Authorization Containment, Finance Correction and Degraded Operation

- **SemVer successor:** `v0.3.0 → v0.4.0`
- **Pass date:** 2026-10-08
- **Repository baseline rechecked:** `JCSchoeman96/NewYou` `main` remains `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`.
- **Authority effect:** NONE. This pass records provider-validation working evidence and candidate upstream direction only.
- **Empirical status:** no Paystack sandbox/live validation case is claimed executed by this pass.

## P4.1 Accepted working upstream direction from P2-Q-001

The user accepted the recommended direction for the previously identified one-off excess-collection gap.

### `P2-UPSTREAM-CAND-001` — one-off excess collection remedy

**Working status:** `ACCEPTED WORKING UPSTREAM DIRECTION / NOT PRODUCT LAW`

> For one governed one-off FP-002 Purchase Intent, exactly one successful collection may satisfy the purchase. If two or more distinct Paystack transactions genuinely settle/complete for that same Purchase Intent, every additional collection is excess money: it must not create another purchased right, paid period, entitlement, credit or commercial occurrence. Commerce must initiate a full source-scoped refund/reversal for each excess collection where that can be done safely and deterministically; where automatic provider correction is unavailable, ambiguous or fails, the excess collection remains visible Finance make-whole work until resolved. The valid purchase/right is determined by NewYou's authoritative commercial-admission ordering, not callback arrival order, browser timing, provider customer grouping or whichever transaction is easiest to refund.

This direction composes with current `DEC-300` rather than replacing it: `DEC-300` already requires duplicate-payment correction to leave one valid right. The accepted working direction closes the previously missing **money-remedy** side only.

No governed Product amendment has been made. A later authorised upstream amendment must decide whether to encode this direction explicitly and where.

## P4.2 Settlement/payout is not payment truth

### P4-F-001 — Paystack settlement is a separate provider lifecycle after customer payment

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack's first-party payout/settlement material distinguishes:

```text
customer payment
→ pending payout / Paystack balance movement
→ settlement/payout to merchant account
```

The Settlement API separately exposes settlement states such as `success`, `processing`, `pending` and `failed`, and can list the transactions included in one settlement. First-party support further describes payouts as the process of moving collected Paystack funds to the merchant's payout account; payout activity can include deductions for refunds and chargebacks.

NewYou consequence:

```text
verified customer payment success
≠ merchant payout/settlement completion
```

A Paystack settlement delay/failure is therefore not by itself evidence that the customer did not pay. It is a Finance/accounting reconciliation condition. Current payment/access may change only when Commerce has separate authoritative evidence of refund, dispute, final reversal, duplicate-payment correction or another governed commercial correction.

### P4-F-002 — entitlement must not wait for normal settlement

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

FP-002 cannot make merchant bank payout a prerequisite for entitlement grant without contradicting the existing payment architecture. Paystack's ordinary settlement occurs after payment and may be delayed independently. The authoritative gate remains NewYou's reconciled payment evidence: exact Purchase Intent/provider-attempt linkage, exact reference, actual amount, currency and a conclusive provider success observation.

Safe interpretation:

| Provider situation | Commerce interpretation | Entitlement effect |
|---|---|---|
| Verify success; settlement pending | paid, subject to ordinary later correction lifecycles | grant once if all other guards pass |
| Verify success; payout delayed/failed | paid + Finance settlement exception | no automatic revoke |
| Verify success; later refund/dispute/final reversal | historical payment remains true; correction lifecycle changes current commercial validity | source-scoped governed consequence |
| payout deduction for refund/chargeback | accounting/settlement evidence of separate correction | never infer access solely from payout row |
| settlement record missing transaction expected by Finance | reconciliation exception | no automatic participant-facing payment rewrite |

### P4-F-003 — settlement proof is production evidence, not test-mode evidence

**Classification:** `RELEASE_ONLY`

Paystack explicitly separates test and live environments: test transactions/API calls involve no real money; live transactions and settlements are real. Test mode can prove parsing and adapter behaviour, but cannot prove South African real payout timing, payout-bank configuration, actual settlement membership, deductions or merchant-funding behaviour.

Controlled production confirmation is therefore release evidence rather than an FP-002 sandbox blocker.

## P4.3 Cross-endpoint disagreement and evidence precedence

### P4-F-004 — provider endpoints can report different dimensions without one being 'wrong'

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Examples:

- Verify may preserve that a charge succeeded while Refund says a refund is pending/processed.
- Dispute may be open while the original transaction object still contains historical success fields.
- Settlement may include or later deduct amounts independently of the original customer-charge result.
- An old success webhook may be resent after a later refund/dispute/reversal.

Therefore NewYou must not define a universal rule of "latest Paystack payload wins" or "transaction.status is the whole commercial state".

The working evidence model remains multi-dimensional:

```text
Payment collection history
Refund lifecycle
Dispute/chargeback lifecycle
Settlement/payout lifecycle
Entitlement consequence
```

Provider event time and arrival time are evidence attributes, not NewYou precedence.

### P4-F-005 — disagreement must become reconciliation work, not arbitrary selection

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

When provider evidence materially disagrees or is temporarily incomplete:

1. preserve each received observation with source, provider IDs/references and observed timestamps;
2. query the provider endpoints appropriate to each dimension;
3. validate exact NewYou Purchase Intent/provider-attempt/refund/dispute linkage;
4. derive current Commerce interpretation under NewYou law;
5. emit only the idempotent Entitlements consequence warranted by that interpretation;
6. keep unresolved contradictions visible rather than forcing a terminal state.

A participant browser payload, provider Dashboard screenshot, old webhook, settlement line, refund row or dispute row does not individually outrank NewYou's reconciliation contract.

## P4.4 Once-off transaction authorizations must not silently become recurring debit authority

### P4-F-006 — successful card payments can expose reusable authorizations

**Classification:** `SUPPORTED_BY_PROVIDER / FUTURE_RECURRING_ONLY`

Paystack documents that a successful card payment can return an `authorization` object with an `authorization_code`, card signature, masked card details and a `reusable` flag. When reusable, the authorization code plus the matching email can be used later with Charge Authorization. Paystack also exposes an API for deactivating an authorization.

This capability is useful evidence for future recurring architecture but is **not** required for one-off FP-002.

### P4-F-007 — `reusable=true` is provider capability, not NewYou payer consent or renewal authority

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

The provider creating a reusable authorization after a normal card payment cannot silently create:

- a NewYou recurring membership contract;
- stored-payment-method Product semantics;
- future collection authority;
- payer consent for recurring sponsorship;
- Entitlement or Account identity authority.

For FP-002 the safe direction is:

- do not call Charge Authorization;
- do not expose "saved card" or recurring semantics;
- do not treat provider customer/authorization identity as canonical NewYou identity;
- do not persist `authorization_code` in ordinary durable Commerce truth merely because Paystack returned it;
- retain only the minimum provider evidence actually required for one-off payment/refund/dispute/reconciliation and approved support/accounting purposes.

The `authorization_code` is not raw PAN/CVV, but it is a payment credential capable of future charging when reusable. It should therefore be treated as sensitive provider capability material rather than harmless transaction metadata.

Exact future recurring retention/consent/deactivation semantics remain `FUTURE_RECURRING_ONLY` and must be designed under the CER contract plus OQ-004 provider validation.

## P4.5 Provider reference contract

### P4-F-008 — reference is attempt identity at the provider boundary, not NewYou purchase identity

**Classification:** `SUPPORTED_BY_PROVIDER`

Paystack documents transaction `reference` as unique and case-sensitive, with only alphanumeric characters plus `-`, `.`, and `=` permitted. Duplicate transaction references are rejected; if NewYou omits the reference, Paystack may generate one.

NewYou should provide the reference itself because restart/ambiguous-initialize recovery depends on knowing it **before** the provider call.

Safe conceptual identity hierarchy:

```text
Purchase Intent / Order identity      — NewYou business identity
Provider Attempt identity             — NewYou attempt/reconciliation identity
Paystack transaction reference        — provider correlation key for one Provider Attempt
Paystack numeric transaction ID       — provider evidence identifier
Webhook event ID                      — provider-delivery evidence identifier where available
```

None may substitute for the layer above it.

### P4-F-009 — provider reference should be opaque/non-semantic

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

The reference may surface in browser navigation, Dashboard/provider evidence and support flows. It therefore should not encode email, PMR, health state, temperament, purchased health-product details or other sensitive/business-semantic data.

A high-entropy opaque NewYou-generated reference is the preferred JIT direction. It improves collision resistance and avoids leaking internal identifiers; it is still not an authentication secret or bearer credential.

The reviewed Paystack transaction documentation does not establish a maximum reference length. The exact chosen representation therefore requires a small compatibility test rather than relying on an undocumented length assumption.

## P4.6 Manual Finance/reconciliation powers

### P4-F-010 — operator work may trigger/reconcile Commerce; it must not become a parallel payment authority

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Current NewYou authority already provides the necessary boundary:

- Commerce owns payment/refund/dispute truth;
- Audit & Evidence records cross-cutting audit/security evidence but never mutates Commerce truth;
- operator Work is attention, not authority;
- provider Dashboard/callback state is evidence, not commercial truth.

Therefore a future Finance/operator surface may safely support actions such as:

- request/force a fresh provider reconciliation;
- review unresolved provider evidence;
- initiate an already-authorised Commerce refund/correction;
- attach minimum necessary evidence/reason to an exception;
- retry a failed execution where current Commerce authority still permits it;
- close a visible exception only after the authoritative Commerce outcome is established.

It may **not** provide an unguarded "mark paid", "grant access", "ignore amount mismatch", "overwrite provider reference", "delete financial history" or direct database-write escape hatch.

### P4-F-011 — manual correction requires evidence-bearing additive history

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

A consequential manual correction should record, at minimum conceptually:

- actor/current authority;
- affected Commerce identity;
- correction type/reason;
- evidence basis/provider references;
- prior interpreted state;
- resulting authoritative state;
- downstream consequence identity/status;
- timestamp/correlation sufficient for incident/support reconstruction.

The exact Ash action names, schemas, separation-of-duties policy and role thresholds remain FP-002/JIT detail. This pass does **not** invent a universal dual-approval rule.

## P4.7 Degraded operation and provider outage

### P4-F-012 — provider unavailability before a payment attempt is safely admitted

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

If checkout cannot reach Paystack before a provider mutation may have crossed the boundary:

- keep the Purchase Intent valid but unpaid;
- show checkout temporarily unavailable/retry-later rather than payment failed;
- do not grant Entitlement;
- do not invent a provider transaction;
- allow a later attempt under the same Purchase Intent when current Commerce guards still permit it.

### P4-F-013 — once an Initialize request may have crossed the provider boundary, outage means unresolved

**Classification:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION`

After a provider mutation may have been transmitted:

```text
network/API failure or timeout
→ provider acceptance unknown
→ preserve same Provider Attempt/reference
→ Verify/reconcile when provider is reachable
→ only then decide whether a replacement attempt may be admitted
```

Blindly minting a new Paystack reference during an outage reopens the double-collection hazard already covered by `EV-001A/001C/024`.

### P4-F-014 — existing provider checkout may outlive NewYou/API disruption

**Classification:** `EMPIRICAL_VALIDATION_REQUIRED`

A participant may already possess a Paystack checkout capability when NewYou, the Paystack API or webhook path becomes temporarily unavailable. NewYou must assume the customer can potentially complete that provider attempt until session expiry or provider evidence proves otherwise.

Consequences:

- participant UI remains `PAYMENT_PENDING` / `VERIFYING` when local truth is unresolved;
- recovery does not depend on browser return;
- restart/reconciliation searches durable unresolved Provider Attempts;
- replacement checkout is guarded against still-live prior capability.

Exact cross-component outage behaviour belongs in sandbox/fault-injection proof.

### P4-F-015 — webhook/queue/database outage acknowledgement remains fail-safe

**Classification:** `SUPPORTED_BY_PROVIDER / SUPPORTED_WITH_NEWYOU_RECONCILIATION`

Paystack retries webhook events if it does not receive successful acknowledgement. NewYou Architecture already requires:

```text
verify authenticity
→ durably receive provider evidence
→ commit
→ acknowledge provider
→ reconcile asynchronously
```

Therefore:

- if NewYou cannot durably record the evidence, it must not claim durable receipt merely to silence retries;
- if queue execution is unavailable after durable ingress, acknowledgement can still succeed because durable evidence/intention permits later processing;
- duplicate retries are normal and must converge;
- provider retries supplement but do not replace periodic reconciliation.

### P4-F-016 — rate limiting is a retry/reconciliation condition, never payment failure

**Classification:** `SUPPORTED_BY_PROVIDER`

Paystack documents HTTP/API rate limits, including materially different test/live quotas and higher live limits for critical endpoints such as Verify Transaction and Initialize Transaction. Test mode is explicitly not intended for load testing.

A rate-limit response therefore means:

- back off/jitter and preserve the same unresolved business obligation;
- do not reinterpret payment as failed;
- do not cause a herd of duplicate initialization attempts;
- reconcile later under bounded worker concurrency.

## P4.8 Test-mode versus production-proof boundary

### Safe to validate in Paystack test mode

- successful/failed card transaction flows;
- reference uniqueness/duplicate-reference rejection;
- amount/currency/reference validation;
- browser-loss independence;
- signed webhook parsing and duplicate ingress;
- test-mode retry behaviour as **test-mode behaviour**;
- refund `failed` and `needs-attention` simulations using documented test instruments;
- refund lifecycle parsing and one-Refund-Intent idempotency;
- restart/reconciliation logic;
- metadata minimisation;
- hosted-checkout card-data boundary;
- operator/JIT state-transition and concurrency proofs that do not depend on real banking rails.

### Documentation + controlled live confirmation required

- actual South African enabled channels/account configuration;
- live webhook retry cadence and operational event history;
- real settlement/payout mapping and deductions;
- South African chargeback deadlines/account terms;
- real dispute/chargeback lifecycle availability;
- real `needs-attention`/bank-detail exceptional behaviour where test simulation cannot prove the account-specific path;
- production authorization/channel behaviour materially dependent on banks/acquirers;
- Paystack account activation/compliance/payout readiness;
- production fee/pass-through settings;
- secret-key rotation procedure on the real account.

### Not a load-test environment

Paystack explicitly states that test mode is for development/integration testing, not load testing. Provider-capacity proof should therefore use bounded mocks/fakes for application load and a controlled provider-call budget; do not use Paystack test endpoints as a stress target.

## P4.9 Adversarial scenario additions

| Scenario | Failure attacked | Safe NewYou interpretation/action |
|---|---|---|
| Verify success; settlement pending for T+2 | settlement confused with payment | payment may become authoritative; settlement is Finance follow-up |
| Verify success; settlement payout fails | payout failure revokes access | keep payment/access; raise settlement exception unless separate correction evidence exists |
| refund deducted from payout but stale success webhook arrives | payout/event ordering | preserve historical success + refund truth; no regrant |
| chargeback deduction appears in payout before local dispute worker processes webhook | financial evidence arrives out of order | reconcile dispute/API; payout deduction is evidence, not direct access command |
| provider transaction success plus refund processed | one status overwrites the other | record successful payment history and completed refund independently |
| provider says transaction reversed but refund API temporarily pending | cross-endpoint lag | remain reconciliation-required; no guessed terminal interpretation |
| successful one-off card returns reusable authorization | accidental recurring authority | do not store/use charging credential for FP-002 recurrence |
| participant later changes NewYou email | authorization tied to old provider email | irrelevant to FP-002; future recurring must store provider charging identity separately from Account email |
| operator sees Dashboard success while Verify API is down | manual mark-paid temptation | keep unresolved; operator triggers/records reconciliation evidence, no raw state override |
| Finance refund API call times out | blind manual retry | preserve Refund Intent; List/Fetch reconcile before another mutation |
| API returns 429 during verification backlog | retry storm | bounded backoff; same obligation, no new Provider Attempt |
| Paystack API unavailable but customer still has checkout URL | hidden in-flight success | keep pending; reconcile same reference after recovery |
| NewYou DB unavailable when webhook arrives | evidence loss | non-success acknowledgement / provider retry; later API reconciliation remains backstop |
| queue unavailable after durable webhook receipt | duplicate provider retries unnecessary | acknowledge after durable receipt; process later from durable obligation |
| guessed/semantic reference contains email/PMR | data leakage/correlation | use opaque provider reference; reference is not authority |

## P4.10 Empirical validation additions

### PAYSTACK-EV-038 — Settlement independence from payment/access

- **Status:** `NOT_EXECUTED / CONTROLLED_LIVE_CONFIRMATION_REQUIRED`
- **Question:** confirm on the activated South African Paystack account that a successfully verified transaction enters a later payout/settlement lifecycle and that settlement timing/status is independent of NewYou's customer-payment confirmation boundary.
- **Capture:** transaction reference/ID, Verify result/time, settlement ID/status/time, payout bank evidence, fees/deductions.
- **Safe pass:** NewYou can treat settlement as Finance/accounting reconciliation and never as the entitlement-grant predicate.

### PAYSTACK-EV-039 — Settlement transaction membership and correction deductions

- **Status:** `NOT_EXECUTED / RELEASE_ONLY`
- **Question:** confirm List Settlement Transactions can correlate one live transaction and that refund/chargeback deductions are visible without implying a new customer payment state.
- **Failure interpretation:** if settlement evidence is incomplete or delayed, Finance requires its own reconciliation path; participant access still follows Commerce payment/refund/dispute authority.

### PAYSTACK-EV-040 — FP-002 reusable-authorization containment

- **Status:** `NOT_EXECUTED`
- **Question:** after a successful one-off test card payment returning a reusable authorization, prove the NewYou adapter persists no future-charge credential and exposes no recurrence/saved-card path.
- **Capture:** application DB, logs, telemetry, provider-evidence representation and redaction output.
- **Safe pass:** no `authorization_code` becomes ordinary durable FP-002 business state; masked minimum evidence only where justified.

### PAYSTACK-EV-041 — Provider reference compatibility and opacity

- **Status:** `NOT_EXECUTED`
- **Question:** prove the selected JIT reference format is accepted by Initialize/Verify, unique under concurrency, survives restart and contains no semantic/sensitive identifiers.
- **Boundary:** exact format/length is JIT detail; this experiment validates the selected representation rather than inventing Product meaning.

### PAYSTACK-EV-042 — Manual Finance correction cannot bypass Commerce

- **Status:** `NOT_EXECUTED / ARCHITECTURAL_PROOF`
- **Question:** prove operator actions can trigger reconciliation/refund/correction only through guarded Commerce actions, append required evidence/audit and cannot directly grant Entitlements or mutate a payment row into success.
- **Attack:** stale operator page, duplicate submit, concurrent reconciliation, revoked role, mismatched amount, raw provider Dashboard claim without reconciled evidence.

### PAYSTACK-EV-043 — Provider outage with in-flight checkout

- **Status:** `NOT_EXECUTED`
- **Setup:** initialize and expose checkout; interrupt NewYou API/webhook/reconciliation paths at controlled points while allowing provider payment where test tooling permits.
- **Safe pass:** unresolved UI, no duplicate replacement attempt by default, eventual same-reference reconciliation, exactly one payment/right.

### PAYSTACK-EV-044 — Verification rate limit/backlog

- **Status:** `NOT_EXECUTED`
- **Setup:** simulate provider 429/rate-limit responses and large unresolved-attempt backlog without load-testing Paystack itself.
- **Safe pass:** bounded jitter/backoff, no duplicate Provider Attempts, business obligations survive restart, payment truth never fabricated.

### PAYSTACK-EV-045 — Test/live evidence boundary audit

- **Status:** `NOT_EXECUTED / RELEASE_ONLY`
- **Question:** before production pilot, verify every closure claim is labelled `TEST_EXECUTED`, `LIVE_CONFIRMED`, `DOCUMENTATION_ONLY`, or `NOT_APPLICABLE` and that no test-mode evidence is being used to claim real settlement/dispute/acquirer behaviour.

## P4.11 OQ-004 closure manifest — first explicit scope split

This is a working validation manifest, **not** an amendment to the governed OQ.

### A. FP-002 Phase 7 / Phase 8 provider-validation blockers

These must be satisfied before Paystack integration mechanics for the one-off paid slice are frozen/executed:

| Obligation | Main validation cases | Minimum closure evidence |
|---|---|---|
| Initialize ambiguity/replacement safety | `EV-001`, `001A`, `001B`, `001C`, `002`, `009A`, `009B` | executed sandbox/fault-injection proof; one Purchase Intent cannot accidentally fan out into unbounded payable attempts |
| Browser non-authority | `EV-003`, `007` | browser loss/forgery cannot grant payment/access; API reconciliation recovers |
| Webhook authenticity/duplicate/retry | `EV-004`, `005`, `006`, `021`, `037` | signed ingress; duplicate/replay/reorder safe; durable-receive-before-ack proof |
| Restart/reconciliation | `EV-007`, `014`, `043`, `044` | durable unresolved attempts converge after crash/outage/backlog |
| Exact money integrity | `EV-008`, `018`, `019` | actual amount + currency + reference + Purchase Intent must match; fee pass-through configuration guarded |
| Enabled-channel scope | `EV-020` | each enabled launch channel proves applicable invariants or remains disabled |
| Duplicate genuine collections | `EV-024` | accepted P2-Q-001 direction governed upstream as required; one right + excess-money remedy |
| Refund lifecycle/idempotency | `EV-010`, `011`, `025`, `026`, `027`, `028`, `029` | one Refund Intent cannot double-refund; partial/full/failed/needs-attention are reconcilable |
| Stale success / refund/dispute precedence | `EV-012`, `013`, `032`, `033` | historical success cannot overwrite later correction; dispute remains separate dimension |
| Identity/data/security boundary | `EV-034`, `035`, `036`, `040`, `041` | provider customer/auth/metadata/card data cannot become NewYou identity or leak sensitive data |
| Manual correction boundary | `EV-042` | operator cannot bypass Commerce/Entitlements authority |

### B. Production-release-only provider evidence

These do not need to manufacture sandbox proof that cannot exist, but must be complete before real paid pilot release:

- `EV-015` exact test/live boundary;
- `EV-022` real key-rotation/overlap runbook confirmation;
- `EV-029` any account-specific live needs-attention behavior not reproducible in test mode;
- `EV-030` dispute reconciliation backstop;
- `EV-031` South African dispute deadline/account confirmation;
- `EV-036` production hosted-checkout/data-flow security confirmation;
- `EV-038`/`039` real settlement/payout evidence;
- `EV-045` final evidence-class audit;
- actual enabled South African payment channels/account settings;
- provider compliance/activation and payout-account readiness.

### C. Future recurring-only OQ-004 evidence

These must **not** block FP-002 one-off implementation merely because the global OQ text also names subscription/proration:

- `EV-016` provider-managed Subscription failed cycle;
- `EV-017` Charge Authorization retry ambiguity;
- authorization retention/deactivation/payment-method lifecycle;
- exact provider-managed versus NewYou-managed recurrence selection;
- 72-hour failed-renewal retry implementation;
- recurring payment-method update;
- subscription cancellation/re-enable behavior;
- upgrade/proration provider mechanics;
- cadence/price/promotion/provider synchronization;
- recurring sponsorship/payment authority.

### D. Governance consequence

The global `OQ-004` must not be marked fully `RESOLVED` while its named future subscription/proration behavior remains unvalidated.

At the same time, current Roadmap explicitly defers recurring memberships from FP-002. The smallest safe upstream routing is therefore:

```text
OQ-004 remains the umbrella provider-validation gate
        ↓
record explicit FP-002 one-off subset = SATISFIED when Section A passes
        ↓
FP-002 may proceed subject to its other gates
        ↓
release-only rows must pass before real paid pilot
        ↓
future recurring subset remains OPEN until its Feature Pack/JIT entry
```

If current governance machinery cannot represent a scoped satisfied subset without falsely changing OQ status, an authorised Open Work/Roadmap/Decision routing clarification is required before FP-002 Phase 7C. No new OQ identifier is invented here.

## P4.12 Pass-4 upstream delta audit

### Existing upstream candidate — accepted working direction

- `P2-UPSTREAM-CAND-001`: one-off excess-collection remedy — **ACCEPTED WORKING DIRECTION / GOVERNED AMENDMENT STILL REQUIRED IF CURRENT AUTHORITY IS JUDGED INSUFFICIENT**.

### Existing governance-routing candidate

- `P2-UPSTREAM-CAND-002`: global OQ-004 versus FP-002 scoped closure — **STILL REQUIRED BEFORE FP-002 FINALISATION IF CURRENT STATUS machinery cannot express the subset cleanly**.

### No new Product-law delta from settlement

No new Product policy is needed to distinguish settlement from payment. This follows existing Commerce/provider-evidence authority and Paystack's documented payout separation.

### No new Product-law delta from once-off reusable authorization

FP-002 is a once-off paid slice. Excluding future-charge use is a scope/security consequence, not a new commercial promise. Recurring authorization semantics belong to the future CER/OQ-004 recurring stream.

### No new Domain/Architecture gap from Finance correction

Existing Commerce ownership + Audit & Evidence + workflow-first operator doctrine are sufficient. Exact correction actions/guards/evidence are JIT/proof detail.

## P4.13 Pass-4 primary-source evidence additions

**Access date:** 2026-10-08.

| Evidence ID | First-party source | Material evidence | Classification |
|---|---|---|---|
| `PS-P4-001` | https://paystack.com/docs/api/settlement/ | Separate settlement lifecycle and settlement-transaction listing. | DOCUMENTED FACT |
| `PS-P4-002` | https://support.paystack.com/en/articles/2125314 | Payment enters pending payout; payout/settlement moves merchant funds; payout activity includes refunds/chargeback deductions. | DOCUMENTED FACT / FIRST-PARTY SUPPORT |
| `PS-P4-003` | https://support.paystack.com/en/articles/2131074 | South Africa payout timing/configuration including T+2 and manual-payout availability. | DOCUMENTED FACT / FIRST-PARTY SUPPORT / RELEASE CONTEXT |
| `PS-P4-004` | https://paystack.com/docs/payments/recurring-charges/ | Successful payment authorization object, reusable flag, authorization code/email requirements, card signature. | DOCUMENTED FACT / FUTURE_RECURRING_ONLY |
| `PS-P4-005` | https://paystack.com/docs/api/customer/ | Customer authorization inventory and authorization deactivation endpoint. | DOCUMENTED FACT / FUTURE_RECURRING_ONLY |
| `PS-P4-006` | https://paystack.com/docs/api/transaction/ | Unique transaction reference; allowed character set; Verify by reference. | DOCUMENTED FACT |
| `PS-P4-007` | https://paystack.com/docs/api/errors/transaction/ | Duplicate reference rejection and payment-session timeout behavior. | DOCUMENTED FACT |
| `PS-P4-008` | https://paystack.com/docs/api/rate-limits/ | Test/live API limits; higher live endpoint limits; test mode not for load testing. | DOCUMENTED FACT |
| `PS-P4-009` | https://paystack.com/docs/api/authentication/ | Test/live separation; real transactions/settlements only live; HTTPS/secret-key guidance. | DOCUMENTED FACT |
| `PS-P4-010` | https://paystack.com/docs/payments/test-payments/ | Test instruments for success/failure and refund failed/needs-attention behavior. | DOCUMENTED FACT |
| `PS-P4-011` | https://paystack.com/docs/payments/webhooks/ | Live/test webhook retry differences and acknowledgement behavior. | DOCUMENTED FACT |
| `PS-P4-012` | https://support.paystack.com/en/articles/2130434 | Refund status changes and associated transaction-status mapping/deductions. | DOCUMENTED FACT / FIRST-PARTY SUPPORT |

## P4.14 Pass-4 disposition

`OQ-004 BLOCKED ON EMPIRICAL TESTS` remains the correct global disposition.

The **documentary FP-002 architecture question is now substantially answered**:

> Paystack can support one-off FP-002 safely only when NewYou owns Purchase Intent, Provider Attempt, Payment, Refund/Dispute interpretation and Entitlement consequence; when transaction reference is attempt correlation rather than commercial identity; when browser/webhook/settlement/customer/authorization objects remain evidence; and when ambiguous mutations reconcile before any replacement or repeated irreversible effect.

No provider mismatch has been found for the one-off architecture.

The remaining FP-002 blockers are proof execution plus the two upstream-routing matters already identified; they are not unexplored generic Paystack API questions.

## P4.15 Next pass targets

Pass 5 should now stop broad provider research and perform a **completeness/adversarial audit**:

1. map every investigation domain requested by the stream to resolved/documented/empirical/upstream status;
2. audit every meaningful lifecycle for states, transitions, guards, side effects, idempotency, concurrency, terminality and recovery;
3. audit the scenario matrix for missing failure combinations rather than adding provider features;
4. classify every outstanding gap as FP-002 blocker, release-only or future recurring-only;
5. test whether any genuine Product/Architecture/Domain contradiction remains;
6. produce the documentary freeze point and the exact next executable sandbox sequence.


---

# Pass 5 — Completeness, Cross-Lifecycle Collision and Documentary Freeze Audit

- **SemVer:** `v0.4.0 → v0.5.0`
- **Change class:** MINOR — adds cross-lifecycle financial-correction invariants, complete investigation-domain coverage audit, lifecycle/recovery audit, scenario-combination audit, new empirical cases and a documentary-freeze decision. No prior pass is edited.
- **Repository authority pin:** live `main` rechecked at `a9c9a8d176e8d62044ca069efeefa60b8f666c8d` on 2026-10-08.
- **Provider evidence access date:** 2026-10-08 unless a row states otherwise.
- **Implementation:** NOT AUTHORISED.
- **Authority:** NONE. This remains working provider-validation evidence subordinate to current NewYou authority.

## P5.1 Accepted working upstream direction carried forward

The user accepted `P2-Q-001`. The following is therefore **accepted working upstream direction, not Product Law**:

> For one governed one-off FP-002 Purchase Intent, exactly one successful collection may satisfy the purchase. Any additional successful collection for that same Purchase Intent is excess money: it cannot create another entitlement, another purchased right, another paid period or an unrequested credit. Commerce should initiate a full source-scoped refund/reversal where that can be done safely and deterministically. If automatic correction is unavailable, ambiguous or fails, the excess collection remains visible Finance make-whole work until resolved. The valid purchase is determined by NewYou commercial-admission ordering, not callback arrival, browser timing, provider customer identity or whichever provider reference reports success first.

This closes the *working* money-remedy gap discovered in Pass 2. Later governed encoding is still required if the authorised Product/Roadmap/Open Work process judges current `DEC-300` insufficiently explicit for FP-002 finalisation.

## P5.2 New provider-independent cross-lifecycle invariants

These are working `PAY-INV-*` identifiers inside this non-authoritative validation stream only.

### PAY-INV-021 — One financial correction cannot be applied twice through different provider paths

**Authority basis:** Commerce owns payment/refund/dispute truth; provider events are evidence; duplicate/reordered evidence cannot multiply business effect.

**Meaning:** refund, dispute/chargeback, settlement deduction and stale transaction-status changes for one provider transaction may describe overlapping financial correction. NewYou must reconcile them to durable correction identities and must not intentionally return or write off the same commercial amount twice merely because two provider APIs/events expose it.

**Provider evidence required:** refund IDs/status/amount, dispute ID/status/refund amount, transaction ID/reference, settlement deductions where available, chronology and provider linkage.

**Proof:** documentation is insufficient for refund/dispute collision behavior; sandbox/live empirical proof is required.

### PAY-INV-022 — Merchant settlement is not participant payment truth

**Authority basis:** Commerce provider-evidence boundary and payment/entitlement separation.

**Meaning:** movement of merchant funds into a Paystack settlement/payout, or failure/delay of that payout, is a Finance/accounting lifecycle. It cannot retroactively manufacture or remove a participant payment/entitlement without separate verified correction evidence such as refund/dispute/reversal.

**Provider evidence required:** transaction success evidence plus settlement/payout lifecycle and deductions.

**Proof:** documentary separation is strong; controlled live confirmation remains release evidence.

### PAY-INV-023 — A provider amount does not invent component identity

**Authority basis:** accepted order allocation snapshots; component-level entitlement consequences; Commerce owns correction interpretation.

**Meaning:** a partial provider refund/dispute amount may be evidence of money movement but does not by itself identify which Assessment/Plan/bundle component is commercially affected. Component consequence requires an existing NewYou allocation/reason/evidence basis. No arbitrary ordering such as "plan first" or "assessment first" may be invented in provider integration.

**Consequence if unsupported:** a partial provider correction could silently revoke the wrong paid right.

**Proof:** current provider docs establish amount-scoped dispute/refund mechanics but do not establish NewYou component identity. `P5-Q-001` remains the working upstream policy question for genuinely unallocated final partial chargeback loss.

## P5.3 Fourteen-domain investigation coverage audit

| Requested investigation domain | Documentary position | Empirical / release proof | Current classification | FP-002 completeness |
|---|---|---|---|---|
| 1. Transaction initialization | unique provider reference; duplicate reference rejected; initialize returns checkout capability; reference supplied by NewYou | `EV-001/001A/001B/001C/002/009A/009B/041` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` + `EMPIRICAL_VALIDATION_REQUIRED` | DOCUMENTARILY COMPLETE; proof outstanding |
| 2. Browser return/callback | browser can disappear; browser return is not verification; NewYou UI remains pending until reconciliation | `EV-003/007` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` | COMPLETE MODEL; proof outstanding |
| 3. Webhooks | signature/HMAC; retry on non-200; duplicate/replay/resend possible; supported event classes documented | `EV-004/005/006/021/037` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` | COMPLETE MODEL; proof outstanding |
| 4. Verify/reconciliation API | Verify by reference gives provider transaction status/amount/currency/reference; independent API recovery exists | `EV-001/007/014/043/044` | `SUPPORTED_BY_PROVIDER` + `SUPPORTED_WITH_NEWYOU_RECONCILIATION` | COMPLETE MODEL; consistency timing outstanding |
| 5. Provider state machine | documented statuses include abandoned/failed/ongoing/pending/processing/queued/success/reversed; refund lifecycle separately mutates transaction status | `EV-009/009A/009B/048` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` | COMPLETE; provider state deliberately not copied |
| 6. Timeout / ambiguous outcome | duplicate reference is not idempotent replay; timeout therefore remains unresolved and must Verify/reconcile before replacement | `EV-001/001A/001B/001C` | `EMPIRICAL_VALIDATION_REQUIRED` | HIGHEST-RISK MODEL COMPLETE; proof outstanding |
| 7. Refunds | full/partial supported; async statuses; failed/needs-attention; List/Fetch reconciliation; no documented Create idempotency key | `EV-010/011/025/026/027/028/029/046/048` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` + `DOCUMENTATION_AMBIGUOUS` | COMPLETE MODEL; mutation ambiguity proof outstanding |
| 8. Chargebacks/disputes/reversals | transaction-linked dispute lifecycle/API/webhooks; amount-scoped resolve; SA deadline evidence conflict; failed-card-debit bank reversals are not payment success | `EV-013/030/031/032/046/047/049` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` + `RELEASE_ONLY` | COMPLETE except `P5-Q-001` policy edge |
| 9. Recurring/subscriptions | provider-managed subscriptions and reusable authorization exist; provider-managed failed cycle does not implement NewYou 72h retry as-is | `EV-016/017` + future CER cases | `PROVIDER_LIMITATION` + `FUTURE_RECURRING_ONLY` | CORRECTLY DEFERRED FROM FP-002 |
| 10. Customer identity | provider Customer/email/authorization identity is provider-side evidence only | `EV-034` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` | COMPLETE |
| 11. Amount/currency integrity | amount in currency subunits; Verify exposes amount/currency; actual amount matters; fee pass-through/partial debit constrained | `EV-008/018/019` | `SUPPORTED_BY_PROVIDER` + NewYou exact-match guard | COMPLETE MODEL; proof outstanding |
| 12. Security | hosted/provider checkout direction; secret-key backend; webhook signature; metadata minimisation; future-charge credential containment | `EV-021/022/035/036/040/041` | `SUPPORTED_BY_PROVIDER` + `RELEASE_ONLY` | COMPLETE MODEL; PCI scope not overclaimed |
| 13. Availability/degraded operation | durable attempt/reference/reconciliation supports restart/outage; rate limits documented; webhook retries provide backstop | `EV-005/014/043/044` | `SUPPORTED_WITH_NEWYOU_RECONCILIATION` | COMPLETE MODEL; proof outstanding |
| 14. Sandbox vs production | test/live separated; test has synthetic instruments; settlement/acquirer/account behavior requires live confirmation; test not for load | `EV-015/031/038/039/045` | `RELEASE_ONLY` | COMPLETE EVIDENCE BOUNDARY |

**Coverage result:** all fourteen requested provider investigation domains have an explicit disposition. No unbounded generic Paystack research category remains.

## P5.4 Lifecycle completeness audit

The following are **logical dimensions**, not a requirement for one universal enum or exact future Ash Resource names.

| Lifecycle / truth dimension | Stable identity | Conceptual states / facts | Transition guards | Idempotency / concurrency | Terminality / correction | Restart recovery source |
|---|---|---|---|---|---|---|
| Purchase / Order Intent | NewYou Purchase Intent identity | open/intended; commercially satisfied once; closed/cancelled only where Product/JIT permits | current order snapshot, purchaser/grantee/offer admissibility | one commercial satisfaction; concurrent attempts cannot multiply right | extra settled money is correction work, not second purchase | PostgreSQL Commerce authority |
| Provider Attempt | NewYou Provider Attempt + Paystack reference | reference allocated; initialize not sent / sent-unresolved; checkout capability known; provider observations; expired/non-payable where proven | stable reference persisted before provider call; replacement only after reconciliation/expiry rule | one reference per attempt; duplicate same-reference Initialize is not replay safety | success/failure/expiry evidence does not rewrite Purchase identity | durable attempt/reference + Verify |
| Provider Evidence Receipt | provider event/API observation identity where available + normalized evidence fingerprint | received; authenticity accepted/rejected; durably recorded; reconciled | signature/authentication and minimum schema checks | duplicates/replays/reordering tolerated; event ID is acceleration, not sole dedupe | evidence remains historical; later evidence can correct interpretation | durable evidence + provider query |
| NewYou Payment Truth | NewYou payment/application identity bound to Purchase Intent | unresolved; verified successful collection; verified non-success; historical success plus separate corrections | reference + exact actual amount + currency + expected Purchase Intent; current Commerce admissibility | one successful application of one collection to purchase; duplicate evidence repeat-safe | historical success is not erased by refund/dispute; current commercial validity is separate | PostgreSQL Commerce truth + evidence |
| Refund | NewYou Refund Intent + provider refund ID when accepted | requested/admitted; provider-creation unresolved; pending; processing; needs-attention; processed; failed; exception/reconciliation | refund policy/amount/source snapshot; no blind retry after ambiguous mutation | one Refund Intent; provider List/Fetch before repeated mutation | processed/failed are provider terminal observations; NewYou exception may remain until money/accounting reconciles | durable Refund Intent + List/Fetch Refund |
| Dispute / Chargeback | NewYou dispute case + Paystack dispute ID | opened/contested; awaiting feedback/bank; accepted/declined/resolved; restoration/correction where provider evidence supports | verified provider dispute + current Commerce interpretation; deadline/account rules | webhook/query duplicates converge on one case | final provider resolution does not erase historical purchase; component consequence still needs NewYou meaning | durable dispute case + List/Fetch Dispute + provider events |
| Merchant Settlement / Payout | provider settlement ID + NewYou Finance reconciliation record | pending/processing/success/failed and deduction observations | provider settlement evidence only | repeated payout observations update Finance reconciliation, not participant truth | payout failure remains Finance exception unless separate correction exists | settlement API/export + Commerce/Finance records |
| Entitlement | Entitlements-owned grant/source identity | granted/active; consumed where applicable; suspended/revoked/expired/ended per governed source lifecycle | authoritative Commerce consequence + current grantee/source/scope policy | source-specific grant/revoke repeat-safe; duplicate Commerce consequence cannot multiply access | historical provenance remains; current access can change independently | Entitlements PostgreSQL authority |
| Future recurring authorization | provider authorization identity, only if future Product/CER authorizes use | received; reusable/non-reusable; retained/active/deactivated only in future recurring scope | explicit future recurring/payment-authority semantics; NOT one-off FP-002 success | separate recurring occurrence identity needed | authorization deactivation/payment-method replacement future-only | future Commerce/CER durable authority |

### Lifecycle anti-collapse rules

Never collapse:

```text
Purchase Intent
≠ Provider Attempt
≠ Provider Evidence
≠ historical successful collection
≠ current commercial validity
≠ Refund
≠ Dispute/Chargeback
≠ merchant Settlement/Payout
≠ Entitlement
≠ future reusable Authorization
```

This separation is now sufficient to explain every required FP-002 failure path without provider state becoming NewYou authority.

## P5.5 Provider-state evidence interpretation audit

| Paystack observation | Safe NewYou interpretation |
|---|---|
| `success` with exact reference/actual amount/currency and admissible Purchase Intent | conclusive provider success evidence; Commerce may establish paid truth idempotently |
| `success` but amount/currency/reference mismatch | invalid/mismatched evidence; never paid truth for that Purchase Intent |
| `pending` / `ongoing` / `processing` | inconclusive; reconcile later |
| `abandoned` | non-success at observation time; do not grant; do not assume permanent non-payability until expiry/session evidence supports replacement |
| `failed` | conclusive provider non-success observation for that attempt; customer-side debit alert does not convert it to NewYou success |
| `reversed` | provider correction/reversal observation; **not sufficient by itself to infer full NewYou entitlement invalidity**, because refund/dispute amount and component meaning remain separate |
| transaction `reversal pending` | refund/correction in progress; reconciliation-required |
| refund `pending/processing/needs-attention` | correction unresolved; no repeated refund mutation without same Refund Intent reconciliation |
| refund `processed` | conclusive provider refund completion evidence for documented amount; component consequence still NewYou-owned |
| refund `failed` | refund did not complete; historical payment remains; Commerce determines retry/alternate remedy |
| dispute opened | contested commercial evidence; current Product Law allows reversible source-scoped access consequence after Commerce confirmation |
| dispute resolved/lost | conclusive provider dispute outcome evidence; Commerce records correction; exact component effect follows NewYou authority, not provider amount alone |
| settlement pending/failed | merchant payout operational evidence only; no automatic participant payment/access reversal |

## P5.6 Cross-lifecycle collision finding — refund + dispute

### Documented facts

Paystack documents ordinary Refund creation independently from Dispute resolution. An accepted dispute carries a `refund_amount`, while the Refund API independently permits full or partial refunds. Refund objects also expose a nullable `dispute` field. No first-party source found in this pass states a cross-API idempotency guarantee or guarantees that an in-flight ordinary Refund and a later Dispute cannot both produce financial correction against the same transaction.

### Safe interpretation

`PAY-INV-021` applies:

> The existence of two provider correction paths cannot mean NewYou may initiate or accept two business corrections for one eligible amount without reconciliation.

Before initiating a new ordinary Refund on a transaction with a known open dispute, or accepting a dispute while an ordinary Refund is unresolved, Commerce must re-read all known correction state and avoid duplicate economic effect. Exact provider capabilities are empirically validated rather than guessed.

### Classification

`DOCUMENTATION_AMBIGUOUS` + `EMPIRICAL_VALIDATION_REQUIRED`.

This is **not** presently a Product-law contradiction. Product already separates Commerce correction truth from Entitlement effect. The missing provider coordination is implementation/JIT/proof unless empirical results expose an unavoidable business choice.

## P5.7 Partial final chargeback — candidate upstream policy edge

Paystack's Dispute API permits amount-scoped resolution. Current NewYou `DEC-300` says a final lost chargeback revokes the *affected* current access, but current authority inspected in this pass does not specify how an unallocated partial chargeback amount against a multi-component bundle determines which component is "affected".

**Working status:** `NEWYOU_POLICY_DECISION / P5-Q-001 PENDING USER ANSWER`.

Recommended direction already posed to the user:

> Do not invent an amount-to-component ordering. If actual dispute evidence identifies the affected snapshotted component, affect only that component. If a final partial loss cannot be mapped to a component from governed evidence, keep the case as a visible Commerce/Finance adjudication exception rather than allowing a raw provider amount to choose which entitlement survives.

Until accepted/governed, FP-002 JIT must not invent `assessment_first`, `plan_first`, proportional, or other allocation for unallocated partial chargeback.

## P5.8 Scenario-combination audit additions

| Scenario | Browser | Webhook | Verify / API | Safe NewYou action |
|---|---|---|---|---|
| ordinary refund already processing, then dispute opens | irrelevant | refund/dispute events may reorder | Refund + Dispute APIs both show correction paths | freeze new correction mutation; reconcile aggregate correction; no double return |
| dispute open, participant requests ordinary refund | irrelevant | dispute event may be delayed | dispute query shows contested transaction | do not blindly create separate refund; route through Commerce policy/correction guard |
| partial refund processed, Verify reports transaction `reversed` | irrelevant | refund.processed | transaction status may be `reversed`; refund amount is partial | preserve historical payment + partial refund amount; do not infer complete entitlement loss from transaction status |
| failed transaction but participant shows debit alert | browser/customer evidence only | no success expected | Verify `failed` | no entitlement; customer/bank reversal/support process is evidence/support, not success |
| refund processed and stale `charge.success` replay arrives | none | stale success duplicate | Refund API processed | historical success remains, refund precedence unaffected; no regrant |
| duplicate successful collections and one refund is ambiguous | any | multiple success/refund events | two Verify successes + unresolved Refund | one purchase/right; excess collection remains make-whole exception until its Refund Intent reconciles |
| final partial chargeback on bundle with no component identity | none | dispute.resolve | dispute amount known, component unknown | `P5-Q-001`; no arbitrary entitlement mapping |
| settlement fails after valid payment | none | may have normal success | Verify success; settlement failed | payment/access unchanged; Finance settlement exception |
| NewYou restart with refund + dispute both unresolved | none | may replay both | List/Fetch Refund + Dispute | rebuild correction state from durable intents + provider queries; no duplicate correction |

## P5.9 Empirical validation additions

### PAYSTACK-EV-046 — Refund/dispute collision

- **Status:** `NOT_EXECUTED / CRITICAL`
- **Question:** what happens when an ordinary refund and a dispute/chargeback overlap on one Paystack transaction?
- **Test setup:** create successful sandbox transaction; initiate a partial refund and hold it in a non-terminal state where test instruments permit; introduce a dispute if supported in test tooling, and also test the reverse ordering.
- **Capture:** transaction ID/reference, all refund IDs/status/amounts, dispute ID/status/refund amount, webhook chronology, Verify status, balance/settlement evidence available in the environment.
- **Safe pass:** NewYou can discover all correction facts and its guard prevents duplicate economic correction; provider behavior does not require "latest event wins".
- **Failure interpretation:** if Paystack permits two independent corrections without sufficient correlation, NewYou needs stronger mutation admission/reconciliation; this is a provider limitation but not automatically a blocker if safely compensable.

### PAYSTACK-EV-047 — Failed-but-debited customer evidence / bank reversal boundary

- **Status:** `NOT_EXECUTED / RELEASE_SUPPORT_CONFIRMATION`
- **Question:** confirm support/runbook handling when Paystack Verify says `failed` but a participant reports a bank debit.
- **Safe outcome:** participant evidence opens support/reconciliation work only; NewYou does not grant access from a bank alert/screenshot; provider/bank reversal or later authoritative provider correction resolves the money issue.
- **Note:** this need not manufacture a failed debit in production; documentary/provider support procedure plus controlled support runbook evidence can satisfy the release obligation.

### PAYSTACK-EV-048 — Partial refund + transaction `reversed` status

- **Status:** `NOT_EXECUTED / CRITICAL`
- **Question:** after a partial refund reaches `processed`, what does Verify/Fetch Transaction report, and can NewYou still recover the exact partial amount from Refund APIs?
- **Safe pass:** adapter never maps transaction `reversed` directly to "entire Purchase invalid"; refund amount/identity remains available for component-aware reconciliation.

### PAYSTACK-EV-049 — Partial final dispute / component non-identity

- **Status:** `NOT_EXECUTED / POLICY-BOUND`
- **Question:** confirm Paystack exposes disputed/refunded amount but no NewYou component identity, and capture exact fields/events for a partial dispute resolution.
- **Pass condition:** provider evidence can be bound to transaction + amount + dispute identity without pretending it identifies Assessment vs Plan.
- **Policy dependency:** final NewYou component consequence requires resolution of `P5-Q-001` where evidence does not identify a component.

## P5.10 Upstream and adjacent-gate audit

### OQ-004

Current Roadmap explicitly classifies for FP-002:

- `OQ-004 — BLOCKS_THIS_FP`: exact webhook, retry, refund, dispute and provider-ambiguity behavior is material to verified payment;
- `OQ-035 — BLOCKS_RELEASE_ONLY`: payment boundary can be prepared/tested internally, but paid pilot/public release needs approved abuse thresholds/recovery.

The provider stream therefore **must not absorb OQ-035**. OQ-004 provider validation and OQ-035 abuse threshold policy are separate gates.

### OQ-001

Operating-entity readiness is not a Paystack semantic. It remains its own expert/commercial/legal gate at the stage current Product/Roadmap requires. OQ-004 evidence cannot close it.

### OQ-002

MVP list pricing is resolved. Provider validation uses the **accepted order snapshot**, not hard-coded list prices, because discounts/bundle allocations remain versioned commercial configuration.

### OQ-035

Exact abuse thresholds/recovery are release-only for FP-002 according to current Roadmap. The payment adapter must expose enough bounded signals/guards for later threshold proof, but this stream does not invent the threshold.

### OQ-036

OQ-036 governs notification providers/channel policy, not Paystack payment authority. Payment/refund communications may create Communications consequences later, but provider-delivery choices must not be confused with OQ-004 payment reconciliation.

### Settlement

`DEC-292` includes settlement among provider behaviors requiring validation. Pass 4 therefore correctly added settlement evidence without making merchant payout a prerequisite for participant entitlement.

## P5.11 Authority contradiction audit

### Product vs Architecture

**No contradiction found.** Product establishes Paystack choice and Commerce/Entitlements consequences. Architecture establishes provider evidence, unresolved ambiguity, durable reconciliation and idempotent consequences. Paystack's documented behavior fits that separation.

### Product vs Domain Law

**No contradiction found.** Commerce remains payment/refund/dispute owner; Entitlements remains access owner; provider Customer/reference/authorization/settlement do not create competing ownership.

### Architecture vs provider behavior

**No unmitigable contradiction found.** Paystack's duplicate-reference rejection, retrying webhooks, mutable transaction status after refunds, and separate settlement lifecycle all make the NewYou reconciliation architecture necessary rather than invalid.

### Roadmap vs global OQ wording

**Routing ambiguity remains, not semantic contradiction.** The global OQ names recurring/proration; FP-002 defers recurring while Roadmap makes the provider behavior relevant to its one-off slice `BLOCKS_THIS_FP`. `P2-UPSTREAM-CAND-002` remains the smallest required governance clarification if existing status machinery cannot record a scoped satisfied subset.

### New policy edge

`P5-Q-001` is a genuine Product/commercial edge only for an **unallocated partial final chargeback on a multi-component purchase**. It does not reopen ordinary full chargeback, refund, duplicate-payment or component-refund policy.

## P5.12 Outstanding-gap classification after completeness audit

| Gap | Class | FP-002 Phase 7/8 | Paid release | Future recurring |
|---|---|---:|---:|---:|
| Initialize response ambiguity / safe replacement | `EMPIRICAL_VALIDATION_REQUIRED` | BLOCKS | BLOCKS | relevant later |
| duplicate reference exact behavior | `EMPIRICAL_VALIDATION_REQUIRED` | BLOCKS | BLOCKS | relevant later |
| webhook duplicate/retry/signature/durable ack | `EMPIRICAL_VALIDATION_REQUIRED` | BLOCKS | BLOCKS | relevant later |
| no-webhook recovery + restart | `EMPIRICAL_VALIDATION_REQUIRED` | BLOCKS | BLOCKS | relevant later |
| amount/currency/reference integrity | `EMPIRICAL_VALIDATION_REQUIRED` | BLOCKS | BLOCKS | relevant later |
| duplicate genuine collections | accepted working Product direction + proof | BLOCKS until governed as needed + `EV-024` | BLOCKS | n/a |
| refund mutation timeout/deduplication | `DOCUMENTATION_AMBIGUOUS` + empirical | BLOCKS | BLOCKS | relevant later |
| refund/dispute collision | `DOCUMENTATION_AMBIGUOUS` + empirical | BLOCKS where correction path is in FP scope | BLOCKS | relevant later |
| partial transaction `reversed` interpretation | empirical adapter proof | BLOCKS | BLOCKS | relevant later |
| unallocated partial final chargeback | `NEWYOU_POLICY_DECISION` (`P5-Q-001`) | BLOCKS final contract if partial dispute handling is in stated scope | BLOCKS | n/a |
| SA dispute deadline exact account rule | `RELEASE_ONLY` provider/account confirmation | NO | BLOCKS | relevant later |
| settlement mapping/payout behavior | `RELEASE_ONLY` | NO for entitlement mechanics | BLOCKS Finance readiness | relevant later |
| actual enabled payment channels | `RELEASE_ONLY` per-channel activation/proof | selected channels can be planned | BLOCKS each enabled channel | future channels later |
| abuse thresholds | OQ-035 | NO | BLOCKS | later as applicable |
| provider-managed subscription failure model | `PROVIDER_LIMITATION / FUTURE_RECURRING_ONLY` | NO | NO FP-002 | BLOCKS future recurring selection |
| proration | `DOCUMENTATION_AMBIGUOUS / FUTURE_RECURRING_ONLY` | NO | NO FP-002 | BLOCKS future upgrade implementation |

## P5.13 Exact executable validation order after credentials are available

Do **not** execute all cases randomly. Attack the irreversible ambiguity seams first:

```text
Wave 1 — mutation ambiguity and identity
EV-001 / 001A / 001B / 001C
EV-002
EV-041

Wave 2 — evidence ingress and recovery
EV-003
EV-004 / 005 / 006 / 021 / 037
EV-007
EV-014

Wave 3 — money integrity and duplicate collection
EV-008 / 018 / 019
EV-020 for each intended launch channel
EV-024

Wave 4 — refund mutation and state collapse
EV-010 / 025
EV-026 / 027 / 028
EV-048
EV-029 where test tooling supports it

Wave 5 — dispute/correction interaction
EV-013 / 030 / 032 / 033
EV-046
EV-049 after `P5-Q-001` is resolved sufficiently to define safe NewYou expectation

Wave 6 — outage/backlog/operator recovery
EV-043 / 044
EV-042 architectural proof

Wave 7 — controlled live/release confirmation
EV-015 / 022 / 031 / 036 / 038 / 039 / 045 / 047
```

Every wave captures request/response timestamps, stable NewYou identities, provider references/IDs, relevant webhook/event IDs, provider query results, NewYou authoritative transitions and Entitlement consequences. Secrets/PAN/CVV are never evidence artifacts.

## P5.14 Documentary freeze test

The documentary/provider-research stream can stop broad discovery when all of these are true:

1. every requested provider investigation domain has an explicit disposition — **YES**;
2. every FP-002 invariant maps to provider evidence/reconciliation — **YES**;
3. browser/webhook/query/settlement/customer/authorization evidence roles are separate — **YES**;
4. timeout/duplicate/reorder/restart behavior has a safe model — **YES, proof outstanding**;
5. amount/currency/reference integrity is explicit — **YES**;
6. refund/dispute/chargeback/settlement are independent dimensions — **YES**;
7. test/live evidence limits are explicit — **YES**;
8. future recurring is separated — **YES**;
9. no provider feature is being allowed to rewrite Product Law — **YES**;
10. remaining unknowns are named empirical tests or focused upstream policy/routing questions rather than generic research — **YES**.

### Documentary freeze verdict

**PASS WITH OPEN EMPIRICAL / UPSTREAM GATES.**

Broad Paystack documentation research is now **PARKED**. New research should be opened only by:

- a failing/ambiguous empirical case;
- Paystack documentation/account behavior that contradicts this evidence baseline;
- a new enabled payment channel;
- future recurring Feature Pack/JIT entry;
- or an upstream Product/Architecture amendment that changes the invariant.

This is not OQ-004 closure. It is the point where more generic reading has lower value than executing the defined proof.

## P5.15 Pass-5 evidence additions

| Evidence ID | First-party source | Finding | Classification |
|---|---|---|---|
| `PS-P5-001` | https://paystack.com/docs/payments/manage-disputes/ | Disputes include duplicate billing/refund-not-received scenarios; merchant-accepted resolution may specify refund amount; unresolved disputes may be auto-accepted after provider deadline. | DOCUMENTED FACT |
| `PS-P5-002` | https://paystack.com/docs/api/dispute/ | Dispute is transaction-linked; statuses/query endpoints; Resolve Dispute accepts `refund_amount`. | DOCUMENTED FACT |
| `PS-P5-003` | https://paystack.com/docs/api/refund/ | Ordinary Refund is independently created and managed; full/partial supported; Refund record exposes transaction and nullable dispute/settlement fields. | DOCUMENTED FACT |
| `PS-P5-004` | https://paystack.com/docs/payments/refunds/ | Refund statuses and linked transaction status; needs-attention requires explicit retry endpoint only after corresponding event. | DOCUMENTED FACT |
| `PS-P5-005` | https://paystack.com/docs/payments/verify-payments/ | Transaction statuses include abandoned, failed, ongoing, pending, processing, queued and reversed. | DOCUMENTED FACT |
| `PS-P5-006` | https://support.paystack.com/en/articles/2127938 | Customer may be debited despite failed payment; bank reversal/support handling does not turn failed provider status into merchant payment success. | DOCUMENTED FACT / FIRST-PARTY SUPPORT |
| `PS-P5-007` | https://paystack.com/docs/api/errors/refund/ | Fully reversed transaction cannot be refunded again via ordinary refund; insufficient merchant balance can block refund. | DOCUMENTED FACT |

## P5.16 Pass-5 disposition

Global disposition remains:

**`OQ-004 BLOCKED ON EMPIRICAL TESTS`**.

The **documentary Pre-JIT provider model is now at a defensible freeze point**. No further generic Paystack capability research is justified for FP-002. The remaining blockers are:

1. execute the defined empirical waves;
2. govern the accepted P2 excess-collection direction if required by upstream review;
3. answer/govern `P5-Q-001` for unallocated partial final chargebacks;
4. record a scoped FP-002 OQ-004 satisfaction without falsely closing future recurring/proration;
5. satisfy release-only provider/account evidence and independent OQ-035 before real paid release.


---

# Pass 6 — Adversarial Stabilisation Audit and Gate-Routing Correction

- **SemVer:** `v0.5.0 → v0.6.0`
- **Change class:** MINOR — append-only governance correction plus final documentary/stabilisation audit. No predecessor text is rewritten.
- **Repository authority pin:** `main` remained `a9c9a8d176e8d62044ca069efeefa60b8f666c8d` when this pass began.
- **Implementation:** NOT AUTHORISED.
- **Authority:** NONE.

## P6.1 Why this pass exists

Pass 5 concluded that broad provider research can stop. Pass 6 attacks the *working pack itself*:

- did it cover every required scenario and investigation domain?
- did any documentary statement accidentally become claimed empirical proof?
- did it create unnecessary upstream work?
- did it collapse independent lifecycles?
- can OQ-004's FP-002 gate be represented without falsely changing the global OQ?
- is every remaining blocker either a named proof case or a genuine Product decision?

## P6.2 Mechanical coverage audit

A local mechanical audit of the cumulative v0.5.0 predecessor confirmed:

- all required baseline scenario labels are present;
- `PAY-INV-001...PAY-INV-023` are represented;
- 53 distinct empirical validation identifiers are represented through `PAYSTACK-EV-049`, including lettered subcases;
- every required classification vocabulary appears where relevant: `SUPPORTED_BY_PROVIDER`, `SUPPORTED_WITH_NEWYOU_RECONCILIATION`, `DOCUMENTATION_AMBIGUOUS`, `EMPIRICAL_VALIDATION_REQUIRED`, `PROVIDER_LIMITATION`, `NEWYOU_POLICY_DECISION`, `RELEASE_ONLY`, `FUTURE_RECURRING_ONLY`;
- no case is marked `TEST_EXECUTED / PASS` or `LIVE_CONFIRMED / PASS`;
- the phrase `EMPIRICALLY VERIFIED` appears only in the evidence-class definition stating that **none yet exist in this pack**;
- no sandbox result has been fabricated.

**Audit result:** PASS.

## P6.3 Correction to `P2-UPSTREAM-CAND-002` — scoped OQ-004 gate handling

Earlier passes treated the global OQ-004 / FP-002 scope split as potentially requiring an upstream routing amendment. Current governance evidence supports a simpler interpretation.

Current Open Work requires:

```text
Phase 7A Feature Pack Skeleton + preliminary Gate Manifest
→ Phase 7B required JIT Domain Dossiers
→ Phase 7C Final Feature Pack Contract
```

and explicitly says the Skeleton/Gate Manifest identifies the affected gates. Current Roadmap separately classifies `OQ-004 — BLOCKS_THIS_FP` for FP-002 because exact webhook/retry/refund/dispute/provider-ambiguity behavior is material to the one-off verified-payment outcome, while recurring membership remains deferred from FP-002.

### Corrected working conclusion

**No upstream Product/Decision/Open Work amendment is currently required merely to represent FP-002-scoped satisfaction of OQ-004.**

The safe representation is:

```text
upstream OQ-004 status = VALIDATION REQUIRED
(global named provider-validation question remains open)

FP-002 Gate Manifest:
OQ-004 / FP-002 applicable scope
= SATISFIED BY <exact evidence set>

future recurring/proration OQ-004 scope
= NOT IN FP-002 / remains open upstream
```

The Feature Pack contract must not write `OQ-004 RESOLVED` globally. It records only whether the gate **as applicable to FP-002's approved outcome** has sufficient evidence.

### Revised candidate disposition

`P2-UPSTREAM-CAND-002` → **CLOSED / NO UPSTREAM AMENDMENT CURRENTLY JUSTIFIED**.

Reopen only if the actual FP-002 Phase 7A/7C governance machinery proves unable to express scoped gate evidence without mutating the global OQ status. Do not amend upstream pre-emptively.

## P6.4 Upstream change ledger after correction

| Working item | Current disposition | Why |
|---|---|---|
| `P2-Q-001` one-off duplicate genuine collections / excess-money remedy | **ACCEPTED WORKING UPSTREAM DIRECTION** | Current law guarantees one valid right but does not explicitly define excess-money make-whole treatment. This is a commercial remedy, so later Product encoding is justified if FP-002 finalisation needs exact customer promise. |
| former `P2-UPSTREAM-CAND-002` global OQ vs FP-002 scoped closure | **CLOSED / NO AMENDMENT** | Existing Roadmap + Gate Manifest mechanism can preserve global OQ while recording FP-specific evidence. |
| `P5-Q-001` unallocated partial final chargeback on multi-component order | **PENDING USER DECISION** | Provider can expose partial disputed amount without NewYou component identity; no arbitrary mapping is authorised. |
| settlement/payment separation | **NO UPSTREAM CHANGE** | Existing provider-evidence and Commerce ownership law sufficient. |
| reusable authorization containment for FP-002 | **NO UPSTREAM CHANGE** | Once-off FP scope + provider/card-secret boundary already sufficient; recurring use is future policy. |
| Finance manual correction boundary | **NO UPSTREAM CHANGE** | Commerce + Audit & Evidence + operator-work doctrine sufficient; exact actions/guards are JIT. |
| refund/dispute collision | **NO PRODUCT CHANGE YET** | Provider coordination unknown is empirical/JIT first. Escalate only if observed provider behavior forces a business choice. |

This is a materially smaller upstream burden than the earlier working posture.

## P6.5 Adversarial lifecycle audit result

Each meaningful lifecycle now has:

- an authoritative owner or explicit provider-evidence classification;
- a stable logical identity;
- non-authoritative provider observations separated from NewYou truth;
- retry and duplicate rules;
- concurrency interpretation;
- restart recovery source;
- correction/reconciliation path;
- explicit terminality limits.

### Remaining lifecycle uncertainty is intentional

The pack does **not** freeze exact future implementation enum labels for:

- Purchase Intent closure/cancellation;
- Provider Attempt internal technical states;
- Finance exception/work states;
- exact Payment Resource status representation;
- exact Refund/Dispute Resource layout;
- operator queue/workflow states;
- recurring authorization/payment-method lifecycle.

Those are JIT representation choices constrained by the semantic dimensions already frozen above. This is not incompleteness.

## P6.6 Cross-lifecycle economic-integrity rule

The refund/dispute collision review sharpens one non-negotiable provider-independent rule:

```text
one original collection
+ zero or more legitimate correction facts
≠ permission to return the same eligible amount twice
```

Commerce must reconcile aggregate corrections by durable source/correction identity. Provider API separation is not business separation.

This rule applies to:

- ordinary Refund + accepted Dispute;
- duplicate ordinary Refund attempts;
- stale refund failure after another correction succeeds;
- settlement deduction observations;
- duplicate genuine collection remediation;
- later provider events that replay historical success.

It does **not** mean the customer's legitimate total remedy is always capped mechanically at the original transaction amount for every conceivable legal/customer-remedy case. Any separate goodwill, damages, fee reimbursement or other payment would require its own explicit commercial authority and identity. The payment-provider adapter may not invent such authority.

## P6.7 Partial chargeback remains the sole newly discovered Product edge

`P5-Q-001` is deliberately narrow:

```text
one multi-component one-off Purchase Intent
→ one provider transaction
→ final partial chargeback / dispute loss
→ provider supplies transaction + amount
→ provider does not supply NewYou component identity
```

The question is **not** whether Commerce records the money loss: it does.

The question is **which current paid-origin component access is "affected" under DEC-300** when provider evidence does not answer that semantic question.

Until answered:

- no provider adapter may choose a component;
- no proportional split is implied;
- no first/last component ordering is implied;
- no full-bundle revocation is implied merely because that is easier;
- already-delivered historical records remain distinct from current access;
- the case remains a visible commercial exception under Commerce authority.

## P6.8 Evidence-class audit

Every current Paystack claim falls into one of these buckets:

### Documentation sufficient for integration constraint

Examples:

- unique reference and duplicate-reference rejection;
- Verify API exists by reference;
- amount/currency/status are provider evidence fields;
- webhook signature and retry contract;
- Refund/List/Fetch/Dispute/Settlement APIs exist;
- reusable authorization can be returned;
- test/live environments differ;
- transaction and refund provider statuses documented.

### Sandbox/fault-injection proof required before FP-002 gate satisfaction

Examples:

- ambiguous Initialize visibility timing;
- two-live-attempt prevention;
- webhook duplicate/reorder/ack behavior through NewYou durability boundary;
- crash/restart convergence;
- exact amount/currency mismatch rejection;
- duplicate genuine collection remedy;
- refund timeout/deduplication;
- partial refund status handling;
- refund/dispute collision;
- stale success after correction.

### Architectural Proof/JIT evidence rather than Paystack sandbox fact

Examples:

- manual Finance cannot bypass Commerce;
- one entitlement consequence under concurrent duplicate evidence;
- durable receipt before webhook acknowledgement;
- sensitive metadata/log redaction;
- no one-off authorization credential persistence.

### Controlled live/release confirmation

Examples:

- real South African dispute deadline/account configuration;
- real settlement/payout mapping;
- actual enabled channels/acquirer behavior;
- provider compliance/activation/payout readiness;
- real secret-key rotation runbook;
- production hosted-checkout/card-data boundary confirmation.

### Future recurring only

Examples:

- provider-managed Subscription retry semantics;
- Charge Authorization retry ambiguity;
- saved payment method lifecycle;
- 72-hour renewal recovery;
- proration/cadence/provider synchronization.

**Audit result:** evidence classes are not being conflated.

## P6.9 FP-002 OQ-004 gate satisfaction contract — freeze candidate

When the required evidence exists, the future FP-002 Gate Manifest should be able to state a result semantically equivalent to:

> **OQ-004 — FP-002 APPLICABLE SCOPE SATISFIED.** The one-off South African/ZAR Paystack path has evidence for Initialize ambiguity, reference correlation, browser non-authority, webhook authenticity/duplicate/retry handling, Verify-based recovery, exact amount/currency/reference validation, duplicate collection remediation, refund/dispute reconciliation, restart recovery and enabled launch-channel behavior. This does not change upstream OQ-004's global `VALIDATION REQUIRED` status for deferred recurring billing, retry and proration behavior.

The exact wording/location belongs to the governed FP-002 artifact when Phase 7A/7C begins; this Pre-JIT pack does not create that authority.

## P6.10 Phase 7 / Phase 8 / Release boundary

### Before FP-002 Phase 7C finalisation

Must have:

- resolved `P2-Q-001` governance/encoding as applicable;
- resolved `P5-Q-001` if partial dispute/chargeback handling is required by the stated FP-002 contract;
- executed critical provider empirical cases sufficiently to freeze the adapter/reconciliation contract;
- defined exact JIT lifecycles/guards/identities from these semantic dimensions;
- classified Architectural Proof (`REUSE_EXISTING_PROOF` or `NEW_TRACER_BULLET`) under normal governance.

### Phase 8 / executable proof

Must attack:

- concurrency/idempotency at Commerce and Entitlements boundaries;
- durable webhook receipt/ack/recovery;
- provider timeout and restart;
- duplicate/reordered/stale evidence;
- money mismatch rejection;
- correction/reconciliation recovery;
- operator boundary and redaction/security where classified applicable.

### Before real paid pilot/release

Additionally require:

- OQ-035 release gate;
- Paystack live account activation/configuration/channel evidence;
- controlled live settlement/dispute confirmation;
- support/Finance runbooks and ownership;
- observability/alerting for unresolved financial obligations;
- no unresolved critical provider behavior masked by sandbox assumptions.

## P6.11 STOP conditions for future work

This Pre-JIT stream should **not** continue researching generic provider features now.

Re-open documentary research only if one of the following occurs:

1. an empirical validation case fails or contradicts the model;
2. `P5-Q-001` is answered and exposes another commercial implication;
3. an enabled launch channel has materially different semantics;
4. Paystack changes relevant documentation/API behavior;
5. FP-002 JIT uncovers a representation choice that cannot satisfy an invariant;
6. future recurring Feature Pack/JIT entry begins;
7. a live-account/release behavior contradicts test-mode evidence.

Otherwise the next work is evidence execution, not more reading.

## P6.12 Stabilisation verdict

### Pre-JIT documentary/provider architecture

**PASS WITH OPEN EMPIRICAL / ONE PENDING PRODUCT EDGE.**

### Upstream semantic consistency

**PASS EXCEPT `P5-Q-001` PENDING.** No Product/Architecture/Domain contradiction has been found. One accepted commercial-remedy direction (`P2-Q-001`) needs normal governed encoding if current law is judged insufficiently explicit; one partial-chargeback component-allocation decision remains pending.

### OQ-004

**OQ-004 BLOCKED ON EMPIRICAL TESTS.**

This is now a precise statement: broad research is not the blocker. The blocker is the defined evidence programme plus the one pending Product edge.


---

# Pass 7 — Accepted Partial-Chargeback Direction and Documentary Closure Hardening

- **SemVer:** `v0.6.0 → v0.7.0`
- **Change class:** MINOR — append-only acceptance of `P5-Q-001`, provider-configuration hardening and documentary closure refinements. No predecessor text is rewritten.
- **Repository authority pin:** live `main` rechecked at `a9c9a8d176e8d62044ca069efeefa60b8f666c8d` on 2026-10-08.
- **Implementation:** NOT AUTHORISED.
- **Authority:** NONE.
- **Provider evidence access date:** 2026-10-08.

## P7.1 Accepted working upstream direction from `P5-Q-001`

The user accepted `P5-Q-001`. The following is therefore **accepted working upstream direction, not Product Law**:

> **A final partial dispute/chargeback loss against a multi-component one-off purchase must not be mapped to a NewYou component merely from provider amount or transaction-level status. If actual dispute/commercial evidence deterministically identifies the affected snapshotted component, Commerce may apply the governed component consequence. If it does not, NewYou must not invent a first-component, last-component, proportional, cheapest-first, most-expensive-first or full-bundle rule. The unresolved component consequence remains a visible Commerce/Finance adjudication exception until governed evidence or Product authority resolves it. Historical delivery/provenance remains distinct from current access.**

This direction composes with current `DEC-300`; it does not rewrite it. `DEC-300` already makes Commerce authoritative for verified financial correction and Entitlements authoritative for the resulting access consequence. The accepted direction only prevents provider amount from silently manufacturing NewYou component semantics.

### Consequence for `PAYSTACK-EV-049`

`EV-049` now has a safe expected outcome:

- if provider/dispute evidence identifies a component under an already-governed commercial allocation, only that component may be affected;
- if component identity is absent, record the financial loss and commercial exception but do not make an arbitrary entitlement mutation;
- duplicate/reordered dispute/refund evidence remains idempotent and source-scoped;
- later adjudication must be additive/auditable rather than rewriting provider history.

`P5-Q-001` is therefore **ACCEPTED WORKING UPSTREAM DIRECTION** and no longer an unanswered Pre-JIT question.

## P7.2 Payment-session timeout is a controlled integration-wide safety parameter

### Documented fact

Paystack exposes `GET /integration/payment_session_timeout` and `PUT /integration/payment_session_timeout`. The timeout is an **integration-level setting**, expressed in seconds. A value of `0` disables session timeout. Paystack's transaction errors separately state that after session timeout a transaction cannot be completed and a new transaction must be initialized.

Primary sources:

- https://paystack.com/docs/api/integration/
- https://paystack.com/docs/api/errors/transaction/

### NewYou interpretation

This materially sharpens the two-live-attempt model:

```text
Purchase Intent
→ Provider Attempt A initialised
→ checkout capability A remains payable until provider session expires
→ participant retries
```

NewYou must not equate **user retry** with permission to mint Provider Attempt B while A is still a valid payable capability.

Safe working mechanism:

1. persist the stable NewYou Purchase Intent and Provider Attempt reference before Initialize;
2. if Initialize returns a usable checkout capability, persist it durably;
3. while that capability is still valid, participant retry/reload re-presents/reuses the same attempt rather than creating another reference;
4. a replacement Provider Attempt may be admitted only after the prior attempt is demonstrably no longer payable, or where the prior Initialize is proven not to have created a usable attempt;
5. provider `abandoned` observation alone is not sufficient proof of permanent non-payability;
6. the Paystack integration timeout must not be silently configured to `0` for the FP-002 launch path;
7. the exact non-zero timeout value is a JIT/release configuration decision informed by UX and provider proof, not Product Law invented here.

### Classification

`SUPPORTED_WITH_NEWYOU_RECONCILIATION` + `EMPIRICAL_VALIDATION_REQUIRED` + `RELEASE_ONLY` configuration confirmation.

### Existing proof coverage

No new empirical identifier is required. This is already covered by:

- `EV-001A/B/C` — ambiguous Initialize and live capability overlap;
- `EV-009A/B` — abandonment and documented timeout replacement;
- `EV-041` — concurrent attempt admission/locking.

Execution must additionally capture the integration timeout value used for the test and prove that replacement occurs only after the old capability is no longer payable.

## P7.3 Reusable authorization returned by one-off payment is capability, not permission

### Documented fact

Paystack's recurring-charge documentation states that a successful card payment can return an `authorization` object containing an `authorization_code`, `signature`, `reusable` flag and card metadata. To perform later recurring charges, Paystack instructs merchants to store the authorization and the email used for the transaction; the authorization code plus that email can be used for subsequent charges.

Primary source:

- https://paystack.com/docs/payments/recurring-charges/

### NewYou interpretation

For FP-002 one-off purchases:

- a returned reusable authorization is **provider capability evidence only**;
- it does not create customer consent or NewYou commercial authority for future charging;
- ordinary FP-002 persistence must not retain a chargeable `authorization_code` merely because Paystack returns it;
- NewYou may retain only the minimum non-sensitive/non-chargeable provider evidence justified for reconciliation/support (for example transaction/reference/channel and, if justified, masked display facts), subject to Privacy/Audit rules;
- any future saved-payment-method or recurring flow must enter through separately governed recurring/payment-authority semantics.

This is stronger than simply saying "do not use the token yet": **the once-off path should avoid acquiring durable charge capability it does not need.**

### Classification

`SUPPORTED_WITH_NEWYOU_RECONCILIATION` / `FUTURE_RECURRING_ONLY` for reuse.

No upstream Product change is required. Existing provider-boundary and one-off scope authority is sufficient.

## P7.4 Paystack transaction ID and webhook event ID have operational value but no business identity

### Documented facts

Paystack Verify returns a numeric transaction `id` in addition to the merchant reference. Paystack's Webhook Events API can list/fetch delivery attempts and look up an event by **transaction id or event id**, not by the transaction reference. It exposes delivery status, attempt count, response code and the payload that was sent.

Primary sources:

- https://paystack.com/docs/api/transaction/
- https://paystack.com/docs/api/webhook-events/

### Safe NewYou mechanism

Persist, when observed and justified:

- NewYou Purchase Intent identity — **commercial correlation authority**;
- NewYou Provider Attempt identity — **NewYou attempt authority**;
- merchant-generated Paystack reference — **stable provider reconciliation key**;
- Paystack numeric transaction id — **provider operational correlation**;
- Paystack webhook event id(s) — **delivery/evidence correlation only** where retained.

Neither provider id becomes NewYou purchase/payment identity.

Webhook Events history is useful for:

- proving whether Paystack attempted delivery;
- diagnosing endpoint failures;
- controlled event resend testing;
- correlating stale/replayed evidence.

It is **not** a replacement for Verify-based payment reconciliation and is never Commerce truth.

### Classification

`SUPPORTED_WITH_NEWYOU_RECONCILIATION`.

Existing `EV-004/005/012/021/037` cover this; evidence capture should include provider transaction id and webhook event id where available.

## P7.5 Test/live webhook timing cannot be promoted across environments

### Documented fact

Paystack documents different retry behaviour by environment:

- live: every 3 minutes for the first four failed attempts, then hourly for up to 72 hours;
- test: hourly for up to 10 hours, with a 30-second request timeout.

Primary source:

- https://paystack.com/docs/payments/webhooks/

### Consequence

Sandbox can validate:

- signature verification;
- duplicate/replay idempotency;
- durable receipt before acknowledgement;
- recovery after local worker/database failure;
- event-history/resend tooling.

Sandbox **cannot prove the production retry schedule or production delivery latency**. Those remain documented/release-confirmed behaviour. NewYou correctness must not depend on either schedule anyway, because Verify/reconciliation is the recovery path.

`EV-005` therefore proves NewYou semantics under retry, not "the live 72-hour schedule exists exactly as simulated in test".

## P7.6 Provider rate limits strengthen the bounded-reconciliation requirement

### Documented fact

Paystack publishes per-integration API rate limits, with separate test/live quotas and higher live limits for foundational endpoints such as Verify and Initialize. Paystack explicitly states that test mode is for development/integration testing, **not load testing**.

Primary source:

- https://paystack.com/docs/api/rate-limits/

### Safe NewYou interpretation

Reconciliation must be:

- durable;
- bounded;
- backoff-aware;
- retryable after restart;
- resistant to duplicate storms;
- able to surface backlog/age without turning API unavailability into failure truth.

Do not attempt to prove correctness by load-testing Paystack test mode. Performance proof should exercise NewYou's own queue/backpressure/concurrency boundaries with provider calls stubbed/fault-injected where appropriate, plus a small controlled provider smoke.

This is Architecture/Engineering proof detail, not a new Product decision.

## P7.7 Settlement/payout is confirmed as a separate Finance lifecycle

### Documented facts

Paystack's Settlement API exposes payout/settlement records with states including `success`, `processing`, `pending` and `failed`. South African Paystack terms describe a normal domestic payout schedule of T+2 business days, while explicitly allowing settlement delay/withholding for reasons including disputes, refunds, reversals, risk and legal requirements.

Primary sources:

- https://paystack.com/docs/api/settlement/
- https://paystack.com/za/terms

### NewYou consequence

A provider-verified successful customer payment and a merchant settlement/payout are **different facts**.

Therefore:

```text
customer payment verified success
+ settlement pending/failed/delayed/withheld
≠ unpaid customer
≠ revoke entitlement
```

Settlement mismatch creates Finance/reconciliation work. Only a separately verified refund, dispute/final reversal or other governed Commerce correction may change payment/access consequences.

This confirms the Pass-4 working direction; no new upstream law is required.

## P7.8 Launch payment channels require an explicit allowlist

Current NewYou authority locks **Paystack + South Africa + ZAR**, but the live repository search found no governed selection of specific Paystack payment channels for FP-002.

### Working rule

Before empirical sign-off / Phase 7C:

1. name the intended launch channel allowlist;
2. validate the applicable evidence/reconciliation behaviour for every enabled channel;
3. configure only those channels;
4. treat account/provider availability of any additional channel as **disabled until deliberately admitted and proved**;
5. adding a materially different channel later reopens only the channel-specific validation needed by its semantics, not the whole provider model.

This does not require a new Product Law decision merely to choose an implementation launch allowlist, unless channel availability is turned into a customer-facing commercial promise that belongs in Product authority.

Existing `EV-020` and `EV-015` remain the proof vehicles.

## P7.9 "Reference not found" after ambiguous Initialize is not immediate failure truth

### Documented fact

Paystack documents `Transaction reference not found` / `Transaction not found` as meaning no transaction could be found for that reference on the integration.

Primary source:

- https://paystack.com/docs/api/errors/transaction/

### Important limitation

The documentation does **not** establish a formal immediate-read-after-write consistency guarantee for the failure window:

```text
Initialize request may have reached Paystack
→ NewYou loses response
→ immediate Verify(reference) says not found
```

Therefore an immediate single `not found` observation after an ambiguous mutation cannot safely be promoted to conclusive "Paystack definitely did not accept Initialize" without empirical timing evidence.

Safe provisional interpretation:

- after an ambiguous Initialize, `not found` is **inconclusive until the bounded reconciliation policy is satisfied**;
- do not mint a replacement reference merely because the first immediate Verify is negative;
- `EV-001/001A` must determine the practical visibility window and safe replacement rule.

This is the highest-risk remaining provider uncertainty and remains first in the empirical programme.

## P7.10 Upstream sufficiency audit after both accepted questions

After acceptance of `P2-Q-001` and `P5-Q-001`, no further unresolved Product question has been found in the documentary stream.

| Candidate issue | Current working disposition |
|---|---|
| duplicate genuine one-off collection money remedy | `P2-Q-001` ACCEPTED WORKING DIRECTION; govern upstream if FP-002 final contract requires explicit Product wording |
| unallocated partial final chargeback | `P5-Q-001` ACCEPTED WORKING DIRECTION; govern upstream if FP-002 final contract requires explicit Product wording |
| provider attempt replacement/timeout | JIT/reconciliation mechanism; no Product change |
| payment-channel allowlist | FP-002/JIT/release configuration unless made a Product promise |
| webhook delivery/retry | provider proof + JIT; no Product change |
| settlement delay/withholding | Finance/reconciliation; no Product change |
| manual Finance correction | Commerce-owned command + Audit evidence; exact roles/guards JIT |
| reusable authorization containment | one-off security/privacy/JIT rule; future recurring authority separate |
| refund/dispute collision | empirical/JIT guard; no new Product policy unless observed provider behaviour forces one |
| global OQ-004 versus FP-002 subset | handled by FP Gate Manifest; no upstream amendment required |

### Result

**UPSTREAM SEMANTIC PRESSURE TEST: PASS WITH TWO ACCEPTED WORKING DIRECTIONS AWAITING NORMAL GOVERNED ENCODING IF REQUIRED.**

No Architecture Law contradiction, Domain ownership contradiction or new Domain requirement was found.

## P7.11 Documentary Pre-JIT closure test

The documentary stream is now considered **STABILISED / READY FOR EMPIRICAL EXECUTION** when read with the following precise meaning:

- provider-independent semantics are sufficiently explicit to prevent JIT from inventing payment truth;
- all material Paystack mechanisms required by FP-002 have a documented mapping or named empirical test;
- browser return, webhook delivery, Verify query, transaction status, refund, dispute, settlement, customer and reusable authorization remain distinct evidence classes;
- restart recovery is based on durable NewYou identities/reference plus reconciliation, not browser survival;
- duplicate/reordered/replayed evidence cannot multiply authoritative payment or entitlement effect;
- exact amount/currency/reference matching is mandatory;
- two genuine collections have an accepted excess-money remedy direction;
- unallocated partial chargeback has an accepted non-arbitrary adjudication direction;
- launch channel scope must be explicit and proven;
- release-only provider/account behaviour remains clearly separated from sandbox proof;
- future recurring remains outside FP-002.

### Documentary disposition

**`PRE-JIT DOCUMENTARY MODEL: PASS / STABILISED FOR EMPIRICAL EXECUTION`**

This is **not** OQ-004 closure and does not authorise Phase 7C or implementation.

Global disposition remains:

**`OQ-004 BLOCKED ON EMPIRICAL TESTS`**.

## P7.12 Evidence additions

| Evidence ID | First-party source | Finding | Classification |
|---|---|---|---|
| `PS-P7-001` | https://paystack.com/docs/api/integration/ | Payment-session timeout is integration-level; `0` disables timeout. | DOCUMENTED FACT |
| `PS-P7-002` | https://paystack.com/docs/api/errors/transaction/ | Expired session requires a new transaction; duplicate reference is rejected; transaction/reference-not-found errors are documented. | DOCUMENTED FACT |
| `PS-P7-003` | https://paystack.com/docs/payments/recurring-charges/ | Successful card payment can return reusable authorization; later charge uses authorization code + email. | DOCUMENTED FACT |
| `PS-P7-004` | https://paystack.com/docs/api/webhook-events/ | Webhook delivery events have event ids and transaction/resource ids and expose delivery response/attempt evidence. | DOCUMENTED FACT |
| `PS-P7-005` | https://paystack.com/docs/payments/webhooks/ | Test/live webhook retry schedules differ; signature is HMAC SHA512 over payload with secret key. | DOCUMENTED FACT |
| `PS-P7-006` | https://paystack.com/docs/api/rate-limits/ | Test/live rate limits differ; test mode is not for load testing. | DOCUMENTED FACT |
| `PS-P7-007` | https://paystack.com/docs/api/settlement/ | Settlement has its own provider lifecycle/status and payout evidence. | DOCUMENTED FACT |
| `PS-P7-008` | https://paystack.com/za/terms | South African payout schedule/withholding conditions confirm settlement can diverge from transaction timing. | DOCUMENTED FACT / TERMS |

## P7.13 Pass-7 verdict

No further generic Paystack documentation research is justified before empirical execution.

The next valid work is:

```text
Wave 1 empirical proof
→ mutation ambiguity / reference visibility / active-capability replacement
→ only then Wave 2 evidence ingress/recovery
→ then money-integrity / correction waves
```

Reopen documentary research only on contradiction, provider change, failed empirical case, newly admitted channel or future recurring entry.


---

# Pass 8 — Upstream Product-Law Delta Candidate and Empirical Entry Contract

- **SemVer:** `v0.7.0 → v0.8.0`
- **Change class:** MINOR — append-only upstream governance candidate plus executable empirical-entry contract. No predecessor text is rewritten.
- **Repository authority pin:** `main` remains `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`.
- **Implementation:** NOT AUTHORISED.
- **Authority:** NONE.

## P8.1 Why a Product-law delta is now justified

Passes 2 and 5 discovered two genuine commercial semantics that are not safely left to provider/JIT interpretation:

1. **two distinct successful collections for one one-off Purchase Intent** — current law protects one valid right, but does not explicitly state the customer money remedy for the excess collection;
2. **final partial chargeback/dispute loss on a multi-component purchase without provider component identity** — current law says a final lost chargeback revokes affected current access, but provider evidence may not identify which NewYou component is affected.

The user accepted both working directions.

These are not Paystack implementation details. They answer customer-money and customer-right questions. Therefore a future FP-002 Final Feature Pack Contract must not be the first authoritative artifact to invent them.

### Governance consequence

**STOP at Product authority before Phase 7C finalisation if current Product authority has not incorporated equivalent semantics.**

The smallest safe move is an **additive Product/Decision amendment refining DEC-300**, with normal SemVer/history preservation. Do not rewrite the historical `DEC-300` text in place. Do not assign a governed DEC identifier inside this Pre-JIT record.

## P8.2 Minimal upstream Product amendment candidate — no governed identifier assigned

The following is candidate amendment language only:

> **Duplicate/excess one-off collection correction.** Where more than one genuinely successful financial collection is reconciled to the same one-off NewYou Purchase Intent, exactly one eligible collection satisfies the purchase. Additional successful collections remain truthful financial history but create no additional paid right, entitlement, fulfilment credit or duplicate commercial obligation. Commerce must return each excess collection in full where a safe provider reversal/refund path is available; otherwise it must retain a visible source-scoped make-whole obligation until resolved. Duplicate-payment remediation must not revoke or alter the valid purchase/right that won NewYou's authoritative purchase ordering.
>
> **Partial final reversal attribution.** A final partial dispute, chargeback or other provider reversal against a multi-component purchase affects NewYou component access only where the affected component can be determined from governed NewYou commercial allocation plus actual verified correction evidence. Provider transaction amount, provider status or provider callback ordering does not itself choose a component. Where the final partial loss cannot be deterministically attributed to a component, Commerce records the financial loss and a visible adjudication exception, while Entitlements makes no arbitrary component revocation until governed authority/evidence resolves the affected right. Historical fulfilment, provenance and lawfully retained records remain distinct from current access.

### Explicit non-goals of the amendment

It must not:

- turn Paystack reference/status into NewYou commercial identity;
- create automatic goodwill/damages/fee-compensation policy;
- define staff roles or operator UI;
- choose refund API mechanics;
- choose a component ordering when evidence is absent;
- rewrite already-delivered historical truth;
- create recurring-membership semantics;
- change ordinary Product refund boundaries under DEC-045/DEC-299/DEC-308;
- make Audit & Evidence or Entitlements the payment owner.

### Expected authority effects

- **Product/Decision Law:** additive clarification/refinement required.
- **Platform Law:** update only if its commercial narrative would otherwise contradict the new locked decision; do not duplicate law unnecessarily.
- **Architecture Law:** no new architecture decision currently required.
- **Domain Law:** no new Domain or ownership change required; Commerce/Entitlements/Audit boundaries already fit.
- **Roadmap:** no Feature Pack scope expansion required.
- **Open Work:** status/routing update only after governed Product promotion, not before.

## P8.3 Upstream closure test

For this Pre-JIT stream, **upstream semantics are considered fully pressure-tested** when:

1. the two accepted directions above are promoted through normal Product governance or current Product authority is formally judged already sufficient in an authoritative review;
2. no lower-level artifact silently substitutes its own commercial remedy;
3. Commerce remains payment/refund/dispute authority;
4. Entitlements receives only governed source-scoped consequences;
5. Audit & Evidence records minimum evidence but does not own correction truth;
6. provider/customer/settlement state remains evidence;
7. no new Domain/Resource is created merely because provider mechanics are complicated.

Current working assessment:

**UPSTREAM DESIGN: SATISFIED IN SUBSTANCE / FORMAL PRODUCT PROMOTION STILL REQUIRED BEFORE PHASE 7C IF THE CURRENT LAW IS NOT AUTHORITATIVELY DEEMED SUFFICIENT.**

## P8.4 Empirical programme prerequisites

The documentary phase is now deliberately blocked from further broad research. Empirical execution requires a controlled environment with:

- Paystack **test** integration credentials injected through environment/secret management, never pasted into this record;
- a public HTTPS webhook endpoint under test control;
- ability to persist raw request bytes long enough to validate webhook HMAC without logging secrets/sensitive payload indiscriminately;
- a fault-injection proxy capable of forwarding a provider mutation and then dropping/delaying the provider response to NewYou;
- controllable application/database/worker restart points;
- a durable test datastore where Purchase Intent, Provider Attempt, provider reference/id, evidence receipt and Commerce/Entitlement outcomes can be inspected;
- clock/timestamp capture sufficient to reconstruct ordering;
- provider Dashboard/API access sufficient to inspect test transactions/refunds/webhook events;
- evidence redaction that excludes secret keys, PAN, CVV, OTP and reusable authorization codes;
- a known Paystack integration payment-session-timeout configuration recorded for the run;
- a named launch-channel candidate set for channel-specific proof.

Absence of any of these does not justify weakening the test; mark the affected case `NOT_EXECUTED`.

## P8.5 Evidence record required for every empirical case

Every executed case must capture, at minimum:

| Field | Requirement |
|---|---|
| Validation case | Exact `PAYSTACK-EV-*` id |
| Environment | Paystack test or controlled live |
| Date/time | UTC plus relevant Africa/Johannesburg interpretation where operationally useful |
| NewYou purchase identity | Opaque test identifier |
| NewYou provider-attempt identity | Opaque test identifier |
| Paystack reference | Allowed evidence field |
| Paystack transaction id | Capture when returned/observed |
| Webhook event id | Capture when applicable |
| Expected amount/currency | NewYou accepted snapshot |
| Provider observed amount/currency/status | Exact API evidence |
| Fault injected | Exact drop/delay/restart/replay condition |
| Request/response ordering | Timestamped sequence |
| NewYou Commerce result | Exact authoritative transition/effect |
| Entitlements result | Exact consequence count/state |
| Retry/reconciliation actions | Exact attempts and backoff points |
| Secrets/sensitive data | MUST NOT be included |
| Result | `PASS`, `FAIL`, `INCONCLUSIVE`, `NOT_EXECUTED` |
| Failure interpretation | Which invariant/gate is threatened |
| Evidence attachments | Redacted logs/API captures/screenshots where permitted |

A provider "success" screenshot without NewYou authoritative-state evidence is insufficient proof.

## P8.6 Wave-1 exact pass/fail contract

Wave 1 remains the highest-risk gate and must be executed first.

### Cases

- `EV-001`
- `EV-001A`
- `EV-001B`
- `EV-001C`
- `EV-002`
- `EV-009A`
- `EV-009B`
- `EV-041`

### Required PASS properties

Wave 1 passes only if all of the following hold:

1. a provider reference is durable before Initialize leaves NewYou;
2. lost Initialize response never becomes automatic "payment failed";
3. immediate `reference not found` after ambiguous Initialize is not treated as conclusive without the proved reconciliation window;
4. repeating Initialize with the same reference cannot create a second transaction silently;
5. participant retry/reload while a valid checkout capability exists reuses that attempt rather than minting a new payable attempt;
6. a second reference is admitted only when the first attempt is proven no longer payable under the accepted attempt-replacement contract;
7. two concurrent retries cannot both win Provider Attempt admission;
8. restart preserves enough durable state to continue reconciliation;
9. no provider/browser observation grants entitlement;
10. the test produces a bounded rule for when an ambiguously initialised reference can be replaced safely.

### Wave-1 fail conditions

Any of these is a **BLOCKED / STOP** for FP-002 provider contract finalisation:

- Paystack can accept an Initialize yet the transaction remains undiscoverable beyond any operationally safe bounded reconciliation window, with no other deterministic recovery path;
- NewYou must mint another reference while the first capability may still be payable;
- the same logical Purchase Intent can produce two live payable attempts under ordinary retry without a deterministic NewYou admission guard;
- provider test behaviour contradicts the documented duplicate-reference model in a way that changes safe retry semantics;
- restart loses the only identity required to reconcile an external success.

Do not proceed to later waves merely to accumulate green evidence around a failed Wave 1.

## P8.7 Wave-2 through Wave-7 gate semantics

The existing Pass-5 ordering remains controlling. Additional interpretation:

### Wave 2 — ingress/recovery

Proves provider evidence can enter durably, authenticate, duplicate/replay safely and recover without browser/webhook dependence.

### Wave 3 — money integrity

Proves only exact expected reference + amount + currency can establish the eligible Commerce payment effect; duplicate genuine collections follow the accepted make-whole direction; every intended launch channel obeys the same invariant.

### Wave 4 — refunds

Proves refund mutation ambiguity does not create double refund, provider refund state does not erase historical payment truth, and partial refund preserves unrelated valid components.

### Wave 5 — dispute/correction collision

Proves stale/reordered evidence cannot restore invalidated access; ordinary refund plus dispute cannot double-correct the same eligible amount; partial final loss follows the accepted non-arbitrary attribution direction.

### Wave 6 — outage/operator recovery

Proves queue/API/database outages produce visible unresolved work, not guessed payment state; manual operator actions are Commerce-owned, scoped, auditable and idempotent.

### Wave 7 — controlled live/release

Confirms only behaviours that test mode cannot establish: live account/channel activation, real webhook configuration, settlement/payout mapping, dispute timing/account policy, key rotation/runbook and controlled low-value end-to-end path.

## P8.8 OQ-004 FP-002 closure evidence manifest — freeze candidate

FP-002's applicable OQ-004 scope is ready to be marked satisfied only when a governed Feature Pack Gate Manifest can point to all of the following:

### A. Documentary/provider evidence

- current Paystack primary-source evidence index with access dates;
- provider-independent invariant map;
- scenario matrix;
- lifecycle/evidence-state matrix;
- explicit test/live boundary;
- accepted launch-channel allowlist;
- no unresolved FP-002 Product semantics.

### B. Empirical provider evidence

- Wave 1 PASS;
- Wave 2 PASS;
- Wave 3 PASS for every enabled launch channel;
- Wave 4 PASS;
- Wave 5 PASS for applicable dispute/correction cases, or explicit provider-supported inability plus safe compensating mechanism proof;
- Wave 6 PASS where NewYou architecture/operator mechanics are material;
- no unresolved critical `INCONCLUSIVE` case.

### C. Architectural proof

- exactly one authoritative Commerce payment effect per governed operation/purchase identity;
- exactly one valid Entitlements consequence despite duplicates/reordering/restart;
- durable webhook receipt/ack/recovery boundary;
- restart/reconciliation proof;
- mismatch rejection proof;
- redaction/security evidence;
- manual correction guard/audit proof where operator path exists.

### D. Release-only evidence

Required before paid pilot/release but not all necessarily before Phase 7C:

- Paystack business live/activated for intended South African/ZAR path;
- configured production webhook endpoint/signature path;
- intended live channel(s) enabled and smoke-tested;
- real integration payment-session timeout confirmed non-zero and intentional;
- dispute deadline/account behavior confirmed for the South African account;
- settlement/payout/accounting reconciliation confirmed;
- Finance/support ownership and unresolved-obligation runbook;
- secret-key rotation/recovery runbook exercised at appropriate boundary;
- OQ-035 independently satisfied for paid public/pilot release.

### Closure status vocabulary

Before A+B+C are satisfied:

**`OQ-004 / FP-002 APPLICABLE SCOPE — BLOCKED ON EMPIRICAL TESTS`**

After A+B+C are satisfied, while D may remain release-only:

**`OQ-004 / FP-002 APPLICABLE SCOPE — READY TO CLOSE FOR PHASE 7/8; RELEASE EVIDENCE REMAINS`**

After applicable D is satisfied:

**`OQ-004 / FP-002 APPLICABLE SCOPE — SATISFIED`**

Global upstream `OQ-004` may remain `VALIDATION REQUIRED` for future recurring/proration semantics.

## P8.9 Final documentary red-team result

The cumulative record was rechecked for the following failure modes:

- Paystack API shape dictating Product Law — **NOT FOUND**;
- browser return becoming payment truth — **NOT FOUND**;
- webhook becoming payment truth — **NOT FOUND**;
- provider Customer becoming Identity truth — **NOT FOUND**;
- settlement becoming customer payment truth — **NOT FOUND**;
- reusable authorization becoming implicit future charge authority — **NOT FOUND** after Pass 7 refinement;
- exactly-once webhook assumption — **NOT FOUND**;
- event-order assumption — **NOT FOUND**;
- timeout treated as financial failure — **NOT FOUND**;
- amount/currency mismatch granting access — **NOT FOUND**;
- duplicate successful collections multiplying entitlement — **NOT FOUND**;
- refund/dispute treated as one lifecycle — **NOT FOUND**;
- partial provider reversal automatically choosing a NewYou component — **NOT FOUND** after accepted P5 direction;
- future recurring expanding FP-002 — **NOT FOUND**;
- sandbox evidence promoted to production certainty — **NOT FOUND**;
- fabricated empirical result — **NOT FOUND**;
- unnecessary new Domain/authority — **NOT FOUND**.

### Pass-8 verdict

**DOCUMENTARY PRE-JIT: PASS / STABILISED.**

**UPSTREAM PRESSURE TEST: PASS IN SUBSTANCE; FORMAL PRODUCT GOVERNANCE OF THE TWO ACCEPTED COMMERCIAL DIRECTIONS IS THE ONLY REMAINING UPSTREAM PROMOTION STEP IF CURRENT LOCKED LAW IS NOT AUTHORITATIVELY DEEMED SUFFICIENT.**

**PROVIDER VALIDATION: BLOCKED ON THE DEFINED EMPIRICAL PROGRAMME, BEGINNING WITH WAVE 1.**

No additional generic provider research is authorised by this working model unless empirical evidence creates a contradiction or scope changes.


---

# Pass 8.1 — Closure Marker / Audit Hygiene Patch

- **SemVer:** `v0.8.0 → v0.8.1`
- **Change class:** PATCH — machine-checkable closure marker only; no working semantic conclusion changes.
- **Authority:** NONE.
- **Implementation:** NOT AUTHORISED.

## P8.1.1 Canonical browser non-authority marker

For audit/search purposes, the controlling provider-independent invariant is repeated here verbatim from the cumulative invariant table:

> **Browser return/navigation never creates authoritative payment truth or entitlement.**

This patch exists because the mechanical closure script initially searched for a different literal phrase even though the invariant was already present at `PAY-INV-005`. No semantic gap existed.

## P8.1.2 Final patch audit

Machine-checkable conditions on this successor:

- predecessor `v0.8.0` is preserved byte-for-byte as the prefix;
- `PAY-INV-005` browser non-authority marker is present;
- `P2-Q-001` and `P5-Q-001` are both accepted working directions;
- no empirical test is claimed passed;
- global disposition remains `OQ-004 BLOCKED ON EMPIRICAL TESTS`;
- documentary disposition remains `PASS / STABILISED`;
- next work remains Wave 1 empirical execution, not generic provider research.


---

# Pass 9 — Upstream Product-Law Closure Candidate

- **SemVer:** `v0.8.1 → v0.9.0`
- **Change class:** MINOR — appends the accepted working Product directions as one exact, unnumbered upstream amendment candidate and pressure-tests that candidate against current authority.
- **Authority:** NONE. This working record does not amend Product Law, assign a DEC identifier, close OQ-004 or authorise implementation.
- **Canonical repository basis rechecked:** `main` at `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`.
- **Implementation:** NOT AUTHORISED.

## P9.1 Authority recheck

Current Product authority already establishes all of the following:

1. Commerce determines payment, refund, dispute and reversal truth from verified evidence; Entitlements applies access consequences.
2. Provider callbacks are evidence and do not directly grant, remove or restore access.
3. Duplicate-payment correction leaves one valid right.
4. A confirmed disputed chargeback may temporarily suspend affected access; restored payment restores access idempotently; a final lost chargeback revokes affected current access.
5. Bundle component amounts are selected before sale, disclosed and immutably snapshotted; component refunds use the accepted snapshot rather than current prices.
6. Commercial history and current access remain distinct.

Relevant current anchors include `00_PLATFORM_v1.6.0.md §21R`, `01_DECISIONS_v1.6.0.md DEC-299/DEC-300`, `04_DOMAIN_MAP_v1.2.0.md` Commerce/Entitlements ownership, and `05_ROADMAP_v1.2.0.md FP-002`.

The accepted directions from P2-Q-001 and P5-Q-001 do not contradict these rules. They close two under-specified customer/commercial edge cases inside the same ownership model.

## P9.2 Why one upstream clarification is sufficient

The two accepted directions share one Product question:

> When provider-side financial correction produces money truth that is not one-to-one with a NewYou right, what may Commerce and Entitlements conclude without inventing authority from provider timing or amount shape?

A new Domain is not justified. A new Resource is not justified at Product level. A new Architecture decision is not justified. Roadmap scope does not change. The smallest safe upstream action is one additive Product-law clarification in the next governed Product/Decision successor.

This candidate deliberately does **not** assign the eventual governed DEC identifier.

## P9.3 Unnumbered Product-law amendment candidate — exact working wording

### Candidate title

**Duplicate collection correction and partial reversal attribution**

### Candidate body

> **For one accepted Purchase Intent/order, exactly one genuine successful collection may satisfy the purchase. Any additional genuine successful collection verified for that same Purchase Intent/order remains truthful financial history but is an excess collection: it creates no second entitlement, credit, paid period or other purchased right. NewYou must return the full customer-collected excess amount through a safe source-scoped refund/reversal where that can be done reliably. If the correction cannot be completed automatically, or its provider result is ambiguous, the full unresolved amount remains a visible Commerce-owned make-whole obligation with Finance/support ownership until reconciled. The valid purchased right remains singular. Provider/browser arrival order must not decide which collection becomes authoritative purchase satisfaction, and retry of the financial correction must not create a second correction effect.**
>
> **A partial provider dispute, chargeback or final reversal may establish a financial loss amount without establishing which NewYou component/right that amount represents. Commerce records the verified financial correction truth independently from component access. Entitlements may suspend, end or revoke only a right that governed NewYou commercial evidence deterministically establishes as affected. Numeric amount coincidence, provider transaction status, callback ordering, current catalogue price, arbitrary component ordering or proportional allocation must not silently manufacture component identity. Where the accepted order snapshot plus actual dispute/commercial evidence establishes one affected component unambiguously, only that component consequence applies. Where no deterministic attribution exists, the financial loss remains a visible Commerce/Finance adjudication exception and no arbitrary component right is permanently ended merely to force the books and entitlement model to align. Historical payment, delivery, entitlement-consumption and correction evidence remain preserved.**

## P9.4 Candidate interpretation boundaries

The candidate means:

- **full excess amount** means the participant/customer should not bear the cost of NewYou/provider duplicate execution; provider fees or internal correction costs do not reduce the customer make-whole amount;
- one valid right remains even if two or more provider references settle successfully;
- excess-collection correction is source-scoped and must not refund or revoke the valid collection/right by mistake;
- NewYou's authoritative payment admission/commit semantics, not provider callback race order, select the satisfying payment effect;
- a partial reversal amount does not itself name Assessment, Plan or another component;
- equality between a reversal amount and one snapshotted component amount is evidence to inspect, not automatic authority, unless the complete governed evidence makes the attribution unique and unambiguous;
- if two components have the same snapshotted amount, amount-only attribution is necessarily insufficient;
- discounts/promotions do not justify reconstructing an attribution from current list prices;
- unresolved partial-loss attribution is exceptional commercial work, not a reason to collapse the order into an invented full reversal;
- existing full-reversal and confirmed-dispute rules remain unchanged.

The candidate does not specify database schema, transaction-locking mechanism, operator UI, refund API retry algorithm or accounting journal design.

## P9.5 Adversarial Product pressure tests

| Scenario | Required Product consequence | Candidate result |
|---|---|---|
| Attempt A and Attempt B both settle for one Purchase Intent | one right; one satisfying collection; other full amount becomes excess correction obligation | PASS |
| B webhook arrives before A although A was earlier NewYou attempt | callback ordering cannot choose commercial authority | PASS |
| excess-refund POST times out | customer make-whole obligation remains unresolved; no blind second correction effect | PASS — JIT/provider reconciliation required |
| excess refund fails permanently | obligation remains visible until governed Finance/support resolution | PASS |
| satisfying payment later receives final full chargeback after excess was already refunded | existing final-reversal law applies to the singular valid right; refunded excess is not resurrected as a hidden replacement payment | PASS |
| partial chargeback equals Plan allocation exactly but provider evidence is transaction-only | numeric equality alone does not silently revoke Plan | PASS |
| partial chargeback plus external dispute evidence explicitly identifies the Plan component and matches immutable order snapshot | Plan may be the affected component; unrelated Assessment right remains independent | PASS |
| Assessment and Plan happen to have equal component allocations | amount-only mapping is ambiguous and cannot choose either | PASS |
| partial chargeback amount spans discount or multiple components | no proportional or arbitrary component revocation | PASS |
| ordinary component refund is already processing when dispute arrives | Commerce must reconcile correction overlap before admitting another financial correction effect | PASS — execution guard belongs downstream |
| provider marks whole transaction `reversed` after a partial correction | provider aggregate status cannot erase NewYou component/history distinctions | PASS |
| operator wants to 'fix' entitlement to match an accounting loss | operator cannot manufacture component identity without governed evidence | PASS |

## P9.6 Cross-authority contradiction check

### Product Law

No contradiction found. The candidate narrows existing terms `duplicate-payment correction`, `affected access`, `component-level access consequence` and `commercial history/current access` without changing ownership.

### Architecture Law

No amendment required. Existing doctrine already requires provider evidence to remain non-authoritative, ambiguous irreversible outcomes to remain unresolved/reconcilable, and external effects to be idempotent/restart-safe.

### Domain Law

No amendment required. Commerce already owns payment/refund/dispute/reversal/reconciliation truth; Entitlements already owns current access. Audit & Evidence remains evidence only.

### Roadmap

No scope expansion required. FP-002 already requires duplicate payment to preserve one valid right and exact refund/dispute/provider-ambiguity behaviour to pass OQ-004.

### CER working pack

The candidate is compatible with the earlier recurring-membership make-whole direction but does not import recurring membership semantics into FP-002.

## P9.7 Upstream governance routing

The correct future promotion route is:

1. preserve current Product/Decision authority unchanged;
2. create the next governed Product/Decision successor through the project's ordinary amendment process;
3. append one governed clarification with the substance in P9.3;
4. assign its identifier only in that governance step;
5. update related version/authority routing and integrity tests as required by repository governance;
6. preserve prior authority versions in archive;
7. then let FP-002 Phase 7A/7B/7C cite the promoted authority.

This Paystack Pre-JIT must not itself edit or pretend to supersede `DEC-300`.

## P9.8 Can FP-002 JIT still be forced to invent Product semantics after this candidate?

Pressure test result: **NO additional known Product semantic gap remains inside the current FP-002 provider-validation scope.**

After promotion of the P9.3 substance, remaining unresolved items classify as:

- provider empirical behaviour;
- provider-account/live configuration;
- JIT lifecycle/mechanism detail constrained by existing Product/Architecture/Domain law;
- release-only operational evidence;
- separately governed OQ-035 abuse thresholds;
- future recurring/proration scope outside FP-002.

None of those justify another Product decision merely to begin the defined OQ-004 empirical programme.

## P9.9 Pass-9 verdict

**UPSTREAM PRODUCT MODEL: SEMANTICALLY COMPLETE FOR THE KNOWN FP-002 PAYSTACK EDGE CASES, SUBJECT TO FORMAL PROMOTION OF THE P9.3 CLARIFICATION.**

**DOCUMENTARY PAYSTACK PRE-JIT: PASS / STABILISED.**

**FORMAL UPSTREAM GOVERNANCE: NOT YET SATISFIED because the accepted clarification remains working/non-authoritative.**

**OQ-004 / FP-002 APPLICABLE SCOPE: BLOCKED ON EMPIRICAL TESTS after upstream promotion, beginning with Wave 1.**

Do not perform additional generic provider research unless empirical evidence creates a contradiction, Paystack changes material documentation/API behaviour, or FP-002 scope changes.


---

# Pass 10 — Promotion Impact, JIT Non-Invention Check and Pre-JIT Exit

- **SemVer:** `v0.9.0 → v0.10.0`
- **Change class:** MINOR — appends the governance promotion map, final semantic non-invention audit and explicit Pre-JIT exit classification.
- **Authority:** NONE.
- **Implementation:** NOT AUTHORISED.
- **Canonical repository basis:** `main` at `a9c9a8d176e8d62044ca069efeefa60b8f666c8d` during this pass.

## P10.1 Candidate wording red-team

The P9.3 candidate was attacked for overreach in five directions.

### A. Does it create accounting law?

**NO.**

It establishes the customer/commercial obligation that excess collection must be made whole and that financial correction truth remains Commerce-owned. It does not define general-ledger entries, revenue recognition, tax treatment, fee accounting, settlement accounting or statutory retention.

### B. Does it create operator authority?

**NO.**

It permits no operator to manufacture payment or component identity. Any manual resolution remains subject to the existing scoped, auditable owner boundary. The candidate states a Product result, not which role/action/UI may execute it.

### C. Does it create a new entitlement allocation algorithm?

**NO.**

It explicitly forbids amount coincidence, proportional allocation, current prices or arbitrary ordering from becoming entitlement identity. Existing accepted order/component snapshots remain the only relevant commercial allocation basis.

### D. Does it broaden FP-002 into recurring billing?

**NO.**

The duplicate-collection rule applies to one accepted Purchase Intent/order and does not define subscription renewal identity, cadence, grace, retry or proration.

### E. Does it weaken existing full-reversal/dispute law?

**NO.**

Existing full reversal, confirmed dispute suspension and restoration rules remain controlling. The clarification applies only where duplicate collection creates excess money or a partial correction lacks deterministic component attribution.

**Red-team result:** `PASS`.

## P10.2 Why Platform + Decision authority should move together on promotion

The current repository's prior narrow Product amendment pattern demonstrates that a substantive Product clarification is represented in both the Platform Product Law and Decision Register rather than leaving one layer semantically stale. The v1.5.0 marketing-unsubscribe amendment, for example, updated both `00_PLATFORM` and `01_DECISIONS`; the later Pass-2 Product amendment likewise moved the Product pack and related routing/integrity evidence together.

Therefore the safest promotion model for P9.3 is:

- append the governed decision in the next Decision Register successor;
- add the corresponding Product-law clarification to the commercial reversal/payment consequence section in the next Platform successor;
- preserve every predecessor unchanged in archive;
- update exact downstream authority references/routing so FP-002 cites the new governed clarification rather than this Pre-JIT working file.

This is an amendment/supersession workflow, not permission to edit the frozen meaning of `DEC-300` in place.

## P10.3 Future upstream promotion pack — bounded impact map

The exact filenames/versions must be resolved from live `main` at promotion time. Do not copy these current versions blindly if `main` has moved.

### Required semantic authority changes

| Authority | Expected change | Reason |
|---|---|---|
| Product Platform (`00_PLATFORM`) | additive clarification in the existing commerce/payment/reversal law; version successor | keeps Product Law explicit rather than relying on Decision Register inference |
| Product Decision Register (`01_DECISIONS`) | append one new governed decision; preserve prior DEC history exactly | gives the accepted direction an explicit governed identifier/status |
| Roadmap (`05_ROADMAP`) | routing/reference update for FP-002 if its exact Product Authority list remains explicit | prevents FP-002 Phase 7 from citing stale authority set |

### Required governance/routing updates if current repository conventions still require them

| Artifact | Expected role |
|---|---|
| `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` | route current Product/Decision/Roadmap successors |
| `README.md` | current-state/current-authority navigation |
| `02_OPEN_WORK` | record amendment lifecycle, current gate state and next authorised work |
| `PROJECT_NORTH_STAR_AND_MVP` | update Product decision coverage/routing only if the current integrity contract requires it; do not change North Star substance without a separate reason |
| archive predecessors | preserve exact former current versions |
| integrity/product-law tests and `foundation_integrity_audit.py` | prove append-only decision history, authority routing, FP-002 authority anchors and no accidental OQ/Domain/Architecture change |

### Explicitly **not** justified by this amendment

- no new Domain;
- no Domain Map semantic amendment;
- no Architecture Law amendment;
- no Architecture Requirement amendment;
- no new OQ identifier;
- no new Feature Pack;
- no change to FP-002 outcome/scope/order;
- no recurring-subscription implementation choice;
- no Paystack API/schema/mechanism selection;
- no Delivery Atlas law creation.

The Delivery Atlas may need derived-navigation reconciliation only if repository integrity/routing conventions require it after the authority successors move. It must not become the reason for the amendment.

## P10.4 Exact promotion acceptance tests — semantic

A future upstream promotion is semantically acceptable only if all of the following are true:

1. prior Product/Decision authority remains preserved and historical versions are archived rather than rewritten;
2. exactly one new governed Product clarification captures both accepted directions without changing unrelated Product Law;
3. duplicate genuine collection still leaves exactly one valid purchased right;
4. the customer is owed the complete excess collected amount, independent of NewYou/provider correction cost;
5. unresolved refund mutation cannot silently create a second refund/correction effect;
6. partial provider correction does not manufacture a NewYou component from amount alone;
7. deterministic component evidence can still produce a source/component-scoped consequence;
8. unattributable partial final loss remains a visible Commerce/Finance exception rather than an arbitrary entitlement mutation;
9. full reversal/dispute restoration semantics remain unchanged;
10. OQ-004 remains `VALIDATION REQUIRED` globally until its applicable empirical scopes are actually proven;
11. FP-002 still treats OQ-004 as the provider-behaviour gate and OQ-035 as release-only;
12. no implementation, schema, package, queue, worker or provider SDK shape is frozen by the Product amendment.

## P10.5 Exact promotion acceptance tests — repository/governance

At promotion time, independent review must verify against the actual candidate head:

- base/head SHA and changed paths;
- exact diff for all Product-law/routing files;
- predecessor archive byte identity where required;
- decision identifier sequence/uniqueness;
- current manifest routes to the new successors;
- README/Open Work current-state routing matches manifest;
- Product/North-Star/Roadmap self-version and related-document references remain internally consistent;
- FP-002 authority anchors include the promoted clarification if exact anchor lists are retained;
- Product hardening/integrity tests pass;
- no unrelated semantic changes are bundled into the amendment.

Previous certification cannot be reused if the candidate head changes.

## P10.6 Final JIT non-invention audit

Question:

> After the P9.3 clarification is formally promoted, can FP-002 JIT/Phase 7C still be forced to invent Product, Domain or Architecture authority in order to specify the Paystack path?

Result: **NO KNOWN UPSTREAM AUTHORITY GAP.**

The remaining design work is legitimately downstream because current authority already determines:

- who owns purchase/payment/refund/dispute truth;
- who owns entitlement/access truth;
- provider/browser evidence non-authority;
- duplicate/reordered/replayed delivery safety;
- timeout/ambiguity semantics;
- amount/currency/reference integrity;
- bundle allocation/refund source;
- duplicate-payment singular-right outcome plus, after P9.3 promotion, excess-money remedy;
- dispute/full-reversal access semantics plus, after P9.3 promotion, partial-unattributable correction handling;
- durable/restart-safe reconciliation doctrine;
- webhook durable receipt/ack/reconcile doctrine;
- audit/evidence non-authority;
- provider-independent payment truth;
- Paystack as launch gateway;
- ZAR/South-Africa launch market;
- FP-002 OQ-004 gate and release-only OQ-035 separation.

Downstream JIT may still choose exact lifecycle state names, Resources, constraints, actions, indexes, Oban jobs, provider adapter functions, timeouts and reconciliation algorithms **only where those choices implement—not redefine—the above authority**.

## P10.7 Pre-JIT exit classification

### Documentary/provider research

`PASS / STABILISED`

No known documentary question remains whose answer is required before empirical execution. Generic Paystack research should remain stopped unless evidence changes.

### Provider-independent invariant extraction

`PASS / STABILISED`

The cumulative invariant set is sufficient to judge Paystack behaviour without adopting Paystack as business authority.

### Upstream semantic discovery

`PASS / COMPLETE IN WORKING FORM`

Two genuine Product gaps were found, pressure-tested and accepted by the Product owner/user. They are consolidated in one amendment candidate.

### Formal upstream governance

`BLOCKED / NOT YET PROMOTED`

The clarification is still non-authoritative. This working file cannot promote itself and repository state has not been mutated.

### OQ-004 empirical provider validation

`BLOCKED / NOT EXECUTED`

The defined empirical programme remains required. Wave 1 is first and fail-closed.

### FP-002 development entry

`NOT AUTHORISED BY THIS ARTIFACT`

This Pre-JIT remains evidence/preparation. It neither substitutes for the Phase 7 Feature Pack sequence nor authorises implementation.

## P10.8 What would constitute improper continuation

The following would now be churn rather than useful Pre-JIT work:

- reading more generic Paystack pages without a specific unresolved invariant;
- designing Ash Resources before the applicable JIT dossier/Final Feature Pack Contract;
- inventing exact lifecycle enum names as Product Law;
- writing Paystack adapter code before empirical ambiguity behaviour is proven;
- treating sandbox assumptions as production evidence;
- introducing Redis/GenServers/services for hypothetical payment load;
- creating a new payment/reconciliation Domain;
- creating a new OQ merely to track a subset already governed by OQ-004;
- changing the Roadmap outcome to accommodate provider quirks.

## P10.9 Next legitimate actions

There are now only two legitimate continuation streams:

### Stream A — upstream governance promotion

Promote the P9.3 clarification through the governed Product amendment process, with independent diff/CI/authority review before certification.

### Stream B — empirical provider proof preparation/execution

After or alongside the governance amendment where the test does not depend on the new commercial edge semantics, prepare the controlled Paystack test environment and execute Wave 1 using secret injection and the frozen evidence schema. No secret key belongs in this working artifact or chat.

If Wave 1 contradicts a documentary assumption or exposes a new Product contradiction, STOP at the appropriate authority level and append a new SemVer pass rather than silently repairing the model downstream.

## P10.10 Pass-10 verdict

**PRE-JIT DISCOVERY/RESEARCH: SATISFIED.**

**UPSTREAM SEMANTIC MODEL: SATISFIED IN WORKING FORM; FORMAL PRODUCT-LAW PROMOTION REMAINS REQUIRED.**

**FORMAL GOVERNANCE: BLOCKED UNTIL A SEPARATE AUTHORISED REPOSITORY AMENDMENT IS REVIEWED AND PROMOTED.**

**OQ-004: BLOCKED ON EMPIRICAL TESTS.**

No further documentary/semantic pass is justified without new evidence, changed scope, authority drift or a failed empirical case.

---

# Pass 11 — Bounded gap-closing delta and documentary freeze

- **Pass status:** COMPLETE / BOUNDED DELTA ONLY
- **Purpose:** close five targeted integration/proof gaps raised by independent review without reopening settled Product/provider research.
- **Authority:** non-authoritative working evidence. This pass does not amend Product Law, Architecture Law, Domain Law, Roadmap or OQ status.
- **Repository baseline rechecked:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d` on 2026-10-08; no authority drift.
- **External-source access date:** 2026-10-08.

This pass does **not** restart generic Paystack research. It addresses only:

1. hidden/automatic mutation retries below the Commerce reconciliation layer;
2. unknown future provider statuses/events/fields;
3. insufficient Paystack balance when NewYou already owes a refund;
4. dispute-evidence minimisation;
5. restart-safe/pagination-safe reconciliation scans.

## P11.1 New provider-independent invariants

The following identifiers remain local to this non-authoritative validation stream.

### PAY-INV-024 — Irreversible Paystack mutation retry ownership

No infrastructure layer, generic resilience wrapper, HTTP client, SDK, reverse proxy or middleware may transparently repeat a Paystack mutation whose outcome can be ambiguous after transmission. Mutation retry authority returns to the owning NewYou reconciliation lifecycle.

At minimum this applies to:

- `POST /transaction/initialize`;
- `POST /refund`;
- dispute/correction mutations;
- future `Charge Authorization` / reusable-authorisation mutations if ever activated.

A retry caused by a known pre-send failure may be safe only when the integration can prove the original request did not cross the provider boundary. A timeout, connection reset after write, lost response, ambiguous 5xx or unknown acknowledgement is not such proof.

**Why:** Paystack documents unique transaction references and duplicate-reference errors, while Create Refund exposes no documented idempotency key. Therefore a hidden transport-level repeat must not be treated as equivalent to a NewYou-governed retry.

**Class:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION / ARCHITECTURAL_PROOF_REQUIRED`.

### PAY-INV-025 — Unknown provider vocabulary fails closed

An unknown Paystack transaction/refund/dispute status, webhook event type, enum value or newly introduced provider field must never be guessed into NewYou success, failure, refund completion, reversal or access state.

Required boundary behaviour:

```text
parse safely
→ retain minimum provider evidence where structurally possible
→ classify as unrecognised/inconclusive provider evidence
→ emit observable reconciliation work
→ query/reconcile through supported current provider reads
→ no authoritative Commerce or Entitlements transition until recognised evidence is sufficient
```

Known events with additional fields must remain forward-compatible where those fields are optional to NewYou semantics. Missing/changed fields that are required for a safety-critical match (reference, amount, currency, environment, linked operation identity) fail closed rather than defaulting.

**Evidence nature:** NewYou fail-closed architecture rule, not a claimed Paystack guarantee. Paystack maintains an API changelog and added the Webhook Events API in September 2026, demonstrating that provider surface evolution is normal.

**Class:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION / ARCHITECTURAL_PROOF_REQUIRED`.

### PAY-INV-026 — Customer make-whole survives refund execution failure

Once Commerce establishes that NewYou owes a customer a refund/correction amount, provider execution failure does not erase the obligation.

If Paystack refuses or cannot execute an authorised refund — including because the merchant Paystack balance is insufficient — then:

- the original valid purchased right remains governed by its own payment/entitlement truth;
- the owed refund amount remains authoritative Commerce correction truth;
- the Refund Intent remains unresolved/failed-needs-remedy rather than `processed`;
- Finance/support work becomes visible and durable;
- no blind retry storm is permitted;
- no second entitlement is created;
- the make-whole obligation survives restart until reconciled.

Paystack currently documents the refund error `Insufficient balance to fulfill this refund. Please top up.` This is an execution constraint, not permission to reduce or forget the customer obligation.

**Class:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION / OPERATIONAL_PROOF_REQUIRED`.

### PAY-INV-027 — Dispute evidence is purpose-minimised external disclosure

Submitting evidence to Paystack, an issuing bank or card scheme is a disclosure to an external financial dispute process. Commerce does not obtain unilateral authority to export unrelated NewYou participant information merely because a payment is disputed.

**Allowed by default where necessary and proportionate:** 

- order/purchase identity and provider transaction evidence;
- accepted price/currency/order snapshot;
- generic fulfilment/delivery/access timestamps;
- receipt or minimum proof that the purchased service/value was made available;
- customer contact fields required by the provider only to the minimum necessary extent.

**Prohibited by default:**

- health/intake answers;
- safety-screening detail;
- temperament questions, raw answers or result detail;
- personalised-plan contents;
- private journals or unrelated content usage;
- private support/clinical notes;
- unnecessary account history;
- credentials, tokens, secrets or security evidence not required for the dispute.

Sensitive participant information may be disclosed for a dispute only through a separately governed Privacy/Legal/Operations escalation that establishes necessity, scope, minimisation and evidence handling. Audit records the disclosure decision/evidence linkage without becoming payment truth.

Paystack's Disputes API currently accepts customer email/name/phone and `service_details`, and its dispute process supports uploaded receipt/evidence files. Those provider capabilities do not broaden NewYou's disclosure authority.

**Class:** `NEWYOU_PRIVACY_JIT / AUDIT_OPERATIONS_PROOF`.

### PAY-INV-028 — Reconciliation scans are complete under pagination, overlap and restart

Periodic provider reconciliation is a recovery/backstop mechanism, not a best-effort report. A scan must not permanently miss a transaction/refund/dispute/settlement case because the provider dataset is paginated, changes while scanning, rate-limits a page, or the NewYou process crashes mid-run.

Required properties:

- bounded date/time windows with deliberate overlap where provider objects may arrive late;
- idempotent re-reading of already-seen provider objects;
- durable scan checkpoint/progress evidence that can restart safely;
- page/cursor exhaustion is verified rather than assumed;
- a failed/429 page does not advance the durable completeness boundary;
- results duplicated between runs are harmless;
- newly appearing objects near the boundary are caught by overlap/backfill;
- scan completion is observable and stale/incomplete scans alert operators;
- provider rate limits produce controlled backoff/retry of the **read** path, not guessed business state.

Paystack documents offset pagination broadly, cursor pagination for disputes and selected endpoints, and endpoint rate limits/429 handling. The exact NewYou scan algorithm remains downstream Architecture/JIT proof.

**Class:** `SUPPORTED_WITH_NEWYOU_RECONCILIATION / ARCHITECTURAL_PROOF_REQUIRED`.

## P11.2 New validation/proof cases

No case below is executed by this document.

### PAYSTACK-EV-050 — Hidden automatic retry of Initialize

**Wave:** 1 — mutation ambiguity and identity.

Fault sequence:

```text
NewYou sends Initialize once
→ request bytes cross transport boundary
→ provider may accept
→ response is lost/reset/times out
→ generic HTTP/resilience layer observes transient failure
```

**PASS only if:** the underlying client/proxy/SDK stack does not transparently emit a second Initialize POST. Control returns to the Provider Attempt reconciliation lifecycle, which verifies/reconciles the existing reference.

**FAIL / STOP:** packet/API evidence shows a second mutation request was emitted without an explicit NewYou reconciliation decision.

### PAYSTACK-EV-051 — Hidden automatic retry of Create Refund

**Wave:** 4 — refunds.

Repeat EV-050's transport fault against `POST /refund`.

**PASS only if:** one application-level refund mutation request is emitted; timeout/ambiguous response returns to the stable Refund Intent; discovery via List/Fetch Refund precedes any later mutation decision.

**FAIL / STOP:** the HTTP/infrastructure layer transparently issues a second Create Refund request.

### PAYSTACK-EV-052 — Unknown provider vocabulary/schema evolution

**Proof class:** Phase-8 adapter/contract proof; synthetic provider fixture, not a claim about a current Paystack value.

Inject independently:

- unknown transaction status;
- unknown refund status;
- unknown dispute status;
- unknown webhook event type;
- known event with extra fields;
- known object with optional field newly null/missing;
- safety-critical match field missing or malformed.

**PASS:** unknown/insufficient evidence is retained minimally, surfaced and reconciled without authoritative business transition or process crash; harmless additive fields are tolerated.

### PAYSTACK-EV-053 — Insufficient Paystack balance on owed refund

**Wave:** 4 plus Finance/Operations proof.

Scenario:

```text
duplicate/excess collection or other governed refund obligation established
→ Commerce authorises exact source-scoped refund
→ Paystack returns insufficient-balance refusal
```

**PASS:** original valid right is unaffected; exact owed amount remains durable; refund is not marked complete; Finance work is visible; restart preserves obligation; retries are bounded/owner-controlled; customer make-whole remains open until actual provider/other governed correction completes.

### PAYSTACK-EV-054 — Dispute evidence minimisation

**Proof class:** Privacy + Audit/Operations JIT/Phase-8 contract test, with provider schema evidence.

For representative dispute reasons, prove the evidence builder/operator path emits only approved minimum fields/files. Attempt to attach health, safety, temperament, plan or private-support information and prove it is blocked or requires the explicit governed escalation path.

### PAYSTACK-EV-055 — Reconciliation scan completeness under pagination/restart/429

**Wave:** 6 — outage/backlog/operator recovery.

Inject:

- multi-page disputes/refunds/settlements;
- duplicate objects across overlapping windows;
- process crash after page N before checkpoint commit;
- process crash after checkpoint commit;
- `429` during an intermediate page;
- provider object appearing near the previous window boundary after an earlier scan;
- cursor/page replay;
- empty terminal page / absent `next` cursor.

**PASS:** every eligible synthetic/provider case is eventually observed exactly-once in business consequence despite at-least-once scan observation; no skipped page advances completion; restart resumes safely; 429 pauses reads without inventing business state.

## P11.3 Wave ordering amendment

The effective empirical order is now:

```text
Wave 1 — mutation ambiguity and attempt admission
EV-001 / 001A / 001B / 001C
EV-002
EV-009A / 009B
EV-041
EV-050   # transport/client must not auto-repeat Initialize

Wave 2 — ingress and recovery
EV-003
EV-004 / 005 / 006 / 021 / 037
EV-007
EV-014

Wave 3 — money integrity and duplicate collection
EV-008 / 018 / 019
EV-020 for every intended launch channel
EV-024

Wave 4 — refund mutation and correction execution
EV-010 / 025
EV-051   # transport/client must not auto-repeat Create Refund
EV-026 / 027 / 028
EV-048
EV-029 where environment permits
EV-053   # insufficient merchant balance keeps make-whole open

Wave 5 — dispute/correction interaction
EV-013 / 030 / 032 / 033
EV-046
EV-049
EV-054   # privacy/minimisation proof is adjacent, not provider-state authority

Wave 6 — outage/backlog/operator/reconciliation recovery
EV-043 / 044
EV-042 architectural proof
EV-055   # pagination/overlap/checkpoint/429 completeness
EV-052   # unknown-provider-vocabulary adapter contract may execute in Phase 8

Wave 7 — controlled live/release confirmation
EV-015 / 022 / 031 / 036 / 038 / 039 / 045 / 047
```

**Ordering rule:** EV-050 is part of Wave-1 entry, because a hidden second POST would invalidate the entire ambiguous-initialization model. EV-051 is the corresponding refund-path guard in Wave 4.

## P11.4 Unknown-provider evolution classification

This gap is intentionally **not** labelled `EMPIRICAL_VALIDATION_REQUIRED` against Paystack because there is no specific current unknown status to observe.

It is instead a NewYou contract requirement:

- current provider values are documented facts;
- provider evolution is expected over time;
- forward-compatible parsing and fail-closed business interpretation are Architecture/JIT obligations;
- the proof uses synthetic fixtures plus future regression tests whenever Paystack adds/changing documented values.

A newly documented provider status/event after this freeze reopens only the affected mapping/evidence case, not the entire Pre-JIT.

## P11.5 Insufficient-refund-balance classification

Paystack documentation establishes the provider execution failure mode. It does **not** create a Product gap because P9.3 already preserves the full make-whole obligation when provider correction cannot complete.

Therefore:

- provider fact: `DOCUMENTED`;
- Product consequence: already covered by accepted working Product candidate;
- exact retry/top-up/operator mechanism: downstream Commerce/Finance JIT;
- proof: EV-053;
- paid-release runbook: Finance/support readiness.

## P11.6 Dispute Evidence Minimisation Contract — routing

This contract does not grant Commerce a new privacy role.

Ownership/routing remains:

- Commerce owns dispute/payment/correction truth and requests the evidence purpose;
- source Domains remain authoritative for their own data;
- Privacy & Consent / applicable legal governance constrains disclosure purpose and scope;
- Audit & Evidence records minimum evidence of the disclosure decision/action and does not become dispute truth;
- Operations may execute a governed workflow but is not business authority.

**Release STOP condition:** if the production dispute process requires routine disclosure of health/safety/temperament/plan detail to defend ordinary chargebacks, STOP for explicit Privacy/Legal review rather than normalising that disclosure inside Commerce.

## P11.7 Reconciliation scan completeness — design boundary

Do not freeze an algorithm here. The later JIT/Phase-8 design must choose provider-appropriate reads and checkpointing while satisfying PAY-INV-028.

The important distinction is:

```text
scan execution identity ≠ provider object identity ≠ Commerce operation identity
```

Re-reading the same provider object is normal. A scan run completing is not evidence that a provider object can never appear later. Durable completeness must therefore be expressed as a bounded, replayable reconciliation boundary rather than a one-shot "last page seen" flag.

## P11.8 Launch-channel action — not a Product-law gap

Current Paystack Initialize allows an explicit `channels` array. NewYou has not yet frozen the exact FP-002 launch allowlist in Product Law.

**Recommended shortest empirical target:**

```text
Paystack
South Africa
ZAR
card only
```

This is a **proof-scope recommendation**, not a permanent Product decision. It should be accepted/rejected in the FP-002 Feature Pack/Gate Manifest or other correct governed planning boundary. If card-only is selected for the first proof, `EV-020` runs against card first; EFT/Capitec Pay/other channels remain disabled until separately admitted and validated.

Do not equate "enabled on the Paystack account" with "approved by NewYou for launch".

## P11.9 Updated open-gap classification

### Blocks Product/Phase-7 finalisation

- formal promotion of the accepted P9.3 Product clarification, unless authoritative review concludes equivalent semantics are already explicit upstream;
- Wave-1 provider ambiguity proof, including EV-050 hidden-retry guard;
- remaining FP-002 OQ-004 empirical cases required by the Gate Manifest.

### Phase-8 architecture/JIT proof

- unknown provider vocabulary/schema fail-closed handling (EV-052);
- durable webhook ingress and exactly-once business consequence;
- restart/reconciliation convergence;
- operator correction authority/audit;
- reconciliation scan completeness (EV-055);
- dispute-evidence minimisation enforcement (EV-054) at the owning Privacy/Audit/Operations boundary.

### Paid-release-only evidence

- intended live channel allowlist activated/smoke-tested;
- South African account dispute deadline/operating behavior confirmed;
- settlement/payout reconciliation;
- insufficient-balance refund operational runbook/ownership;
- key rotation and production webhook runbook;
- OQ-035 abuse thresholds.

### Outside FP-002 / global OQ-004 remains open

- recurring/subscription retry mechanism;
- proration;
- future Charge Authorization/reusable-authorisation use;
- future additional markets/currencies/channels.

## P11.10 Documentary freeze decision

After this bounded delta:

- no known generic Paystack documentary research gap remains for FP-002;
- no new Product-law question was discovered;
- the two accepted Product directions remain the only upstream semantic amendment candidate;
- the five review gaps are now expressed as explicit invariants and executable proof obligations;
- no empirical result has been fabricated;
- provider validation is still **not complete**.

Therefore:

**DOCUMENTARY / SEMANTIC DISCOVERY — PASS / STABILISED / FREEZE.**

**PAYSTACK PROVIDER VALIDATION — BLOCKED / NOT EXECUTED EMPIRICALLY.**

Future documentary work should reopen only when one of these occurs:

1. Paystack documentation/changelog materially changes an affected contract;
2. an empirical case contradicts the current model;
3. FP-002 scope/channel selection changes;
4. live repository authority changes the governing semantics;
5. a Privacy/Legal/Finance review introduces a new mandatory constraint.

## P11.11 Compact-context projection

The 4k+ line cumulative file remains the provenance ledger. It is no longer the recommended default JIT context.

A compact current projection is created alongside this pass with:

- `README.md` — routing and status;
- `NEWYOU_PAYSTACK_PREJIT_CONTRACT_WORKING_v1.0.0.md` — current effective invariants only;
- `NEWYOU_PAYSTACK_EMPIRICAL_MANIFEST_WORKING_v1.0.0.md` — waves/cases/evidence/status;
- `NEWYOU_PAYSTACK_GAP_REGISTER_WORKING_v1.0.0.md` — open items only;
- `NEWYOU_PAYSTACK_EVIDENCE_INDEX_WORKING_v1.0.0.md` — current source index and evidence classes;
- `deep/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.11.0.md` — full append-only provenance ledger;
- `deep/archive/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.10.0.md` — explicit immediate predecessor snapshot.

The compact projection is **derived working context**, not authority. Where it conflicts with the deep ledger, live governed GitHub or newer provider evidence, the stronger/current source wins.

## P11.12 Pass-11 verdict

**PASS / BOUNDED GAP-CLOSING COMPLETE.**

No Pass 12 documentary grill is authorised by the current evidence. The next materially useful work is upstream Product promotion and Wave-1 empirical execution.
