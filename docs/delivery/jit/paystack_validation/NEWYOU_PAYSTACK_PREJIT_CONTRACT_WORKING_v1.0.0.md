# NewYou Paystack Pre-JIT Contract — Working v1.0.0

- **Status:** CURRENT WORKING PROJECTION / NON-AUTHORITATIVE
- **Derived from:** `NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.11.0.md`
- **Repository baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Documentary status:** `PASS / STABILISED / FREEZE`
- **Provider validation:** `BLOCKED / NOT EXECUTED EMPIRICALLY`
- **Purpose:** current effective provider-independent contract for FP-002 planning/JIT; excludes superseded pass history.

## 1. Scope

This contract covers FP-002's one-off South African/ZAR Paystack path: checkout, verified payment evidence, Commerce reconciliation, Entitlements consequence, refunds, disputes/chargebacks, restart/recovery, operator correction boundaries and release evidence.

It deliberately excludes future recurring memberships, subscription retry/proration design, future reusable-authorisation charging, additional gateways, international/multi-currency activation and event-ticket commerce except where documentary evidence is recorded for future use.

## 2. Authority and ownership

The live GitHub repository remains canonical. This working projection never overrides Product Law, Architecture Law, Domain Law, Roadmap, current Feature Pack authority or proof.

Durable ownership remains:

| Truth | Authoritative owner |
|---|---|
| purchase, payment, refund, dispute, reversal and provider reconciliation | Commerce |
| current access/right/credit consequence | Entitlements |
| canonical person/account identity | Identity & Access |
| privacy permission/disclosure constraints | Privacy & Consent / applicable legal authority |
| append-only/minimised cross-cutting evidence | Audit & Evidence |
| Paystack callback/API/dashboard/browser state | external evidence only |

Provider evidence can inform Commerce. It never directly grants/revokes Entitlements.

## 3. Required lifecycle separation

Do not collapse these dimensions into one enum or provider status:

- Purchase Intent / accepted order;
- Provider Attempt;
- Provider evidence observation;
- Commerce payment truth;
- Entitlement/right;
- Refund Intent + refund execution state;
- Dispute/chargeback state;
- merchant settlement/payout state;
- operator/reconciliation work state.

Historical successful payment may coexist with later refund/dispute/reversal evidence. Settlement failure does not by itself undo customer payment truth.

## 4. Effective provider-independent invariants

| ID | Current effective invariant | Proof/evidence class |
|---|---|---|
| PAY-INV-001 | Commerce alone establishes payment/refund/dispute/reversal truth; provider/browser state is evidence. | NewYou architecture + provider evidence |
| PAY-INV-002 | Entitlements alone establishes current access; provider success never grants access directly. | NewYou proof |
| PAY-INV-003 | Purchase Intent identity is NewYou-owned; Paystack reference identifies a provider attempt, not the purchase itself. | Docs + proof |
| PAY-INV-004 | Transport timeout/ambiguous acknowledgement is unresolved, not success/failure; no blind consequential retry. | **Empirical required** |
| PAY-INV-005 | Browser return/navigation is never payment or entitlement authority. | Docs + enforcement proof |
| PAY-INV-006 | Provider evidence is authenticated where applicable and bound to a known Provider Attempt before Commerce consequence. | Docs + sandbox |
| PAY-INV-007 | Duplicate/replayed/reordered provider evidence cannot create a second payment or entitlement effect. | Docs + proof |
| PAY-INV-008 | Browser/webhook loss, worker/node restart and API interruption remain reconcilable from durable NewYou identity + provider reads. | Docs + restart proof |
| PAY-INV-009 | Success evidence is eligible only when expected reference, amount, currency and environment match. | Docs + negative proof |
| PAY-INV-010 | Provider state vocabulary is evidence; it is not copied directly into NewYou business lifecycle states. | Contract proof |
| PAY-INV-011 | Refund truth is distinct from original payment and entitlement consequence; component refund uses accepted order allocation snapshot. | Docs + proof |
| PAY-INV-012 | Ambiguous refund creation cannot be resolved by blind duplicate POST. | **Empirical required** |
| PAY-INV-013 | Dispute/reversal evidence is source-scoped/correctable and does not erase historical fulfilment or imply account-wide fraud. | Docs + proof |
| PAY-INV-014 | Paystack customer/email/customer_code is never NewYou Identity authority. | Contract proof |
| PAY-INV-015 | Money is reconciled in currency minor units; ZAR amount/currency must equal accepted customer charge; provider fees do not redefine order price. | Docs + proof |
| PAY-INV-016 | Secret keys remain server-side; raw card credentials do not transit NewYou absent separate justification/compliance approval; metadata is minimised. | Security proof |
| PAY-INV-017 | Webhook 200 means durable evidence acceptance, not completion of business consequence; consequence is async/repeat-safe. | Docs + failure injection |
| PAY-INV-018 | Provider/API outage degrades to unresolved/refused/backlog; never fabricated success. | Failure/recovery proof |
| PAY-INV-019 | Provider/audit evidence is sufficient for support/reconciliation but never a shadow identity/health store. | Privacy JIT |
| PAY-INV-020 | Recurring-payment mechanics remain outside FP-002 unless Roadmap scope changes. | Scope guard |
| PAY-INV-021 | The same financial correction cannot be applied twice through refund/dispute/other provider paths. | Empirical + Commerce proof |
| PAY-INV-022 | Merchant settlement/payout state is not participant payment truth. | Docs + release proof |
| PAY-INV-023 | Provider amount does not manufacture NewYou component/right identity. | Product clarification + proof |
| PAY-INV-024 | No HTTP client/SDK/proxy/resilience layer may transparently repeat an ambiguous irreversible Paystack mutation; retry control returns to NewYou reconciliation. | **Architecture + fault proof** |
| PAY-INV-025 | Unknown provider status/event/enum/schema values fail closed into unrecognised/inconclusive evidence; no guessed business transition or crash. | **Architecture contract proof** |
| PAY-INV-026 | Once a refund/make-whole amount is owed, provider execution failure—including insufficient Paystack balance—does not erase the obligation. | Docs + Ops proof |
| PAY-INV-027 | Chargeback/dispute evidence submitted externally is purpose-minimised; sensitive health/temperament/plan/support data is prohibited by default and needs governed escalation. | Privacy/Audit/Legal proof |
| PAY-INV-028 | Reconciliation scans are restart-safe, overlapping/idempotent, pagination-complete and rate-limit-aware; scan interruption cannot permanently hide provider cases. | Architecture proof |

## 5. Evidence interpretation

| Provider observation | NewYou interpretation |
|---|---|
| browser callback/reference | untrusted reconciliation trigger only |
| signed `charge.success` | strong provider evidence; still must match known attempt/reference/amount/currency/env and reconcile through Commerce |
| Verify `success` | strong server-read evidence; still not entitlement authority |
| `pending` / `processing` / `ongoing` / unknown status | inconclusive; reconcile |
| `failed` / `abandoned` | no success at observation time; do not infer purchase cancellation unless NewYou's attempt contract proves terminality |
| transaction `reversed` | reversal/refund concern; does not erase historical payment or identify component consequence |
| refund `pending`/`processing`/`needs-attention` | independent refund lifecycle; not refund completion |
| refund `processed` | provider refund completion evidence; Commerce reconciles exact source/amount |
| dispute created/pending | contested payment state; source-scoped reversible consequence only under Product Law |
| final lost chargeback | Commerce records verified final loss; Entitlements applies only deterministically affected current right |
| settlement pending/failed | Finance/payout reconciliation; no automatic participant-access consequence |
| unknown event/status/value | unrecognised evidence -> observe/reconcile; no guessed transition |

## 6. Attempt and mutation rules

1. Persist NewYou Purchase Intent/Provider Attempt identity and chosen Paystack reference before Initialize leaves the platform.
2. A Paystack reference is unique per provider transaction attempt.
3. Do not mint a replacement reference while the prior checkout may still be payable.
4. Browser retry/reload reuses a valid checkout capability where safe.
5. A second attempt is admitted only under a deterministic NewYou replacement guard.
6. Initialize/Refund/dispute mutation timeouts remain unresolved until provider reads/reconciliation establish a safe next step.
7. Automatic client/proxy retry of ambiguous mutation POSTs is prohibited.
8. Read-path polling/reconciliation may retry with bounded rate-limit-aware control because reads do not create the irreversible financial effect.

## 7. Money integrity

- Accepted order amount/currency is NewYou authority.
- Provider `data.amount`/currency/reference/environment must match exactly before eligible payment effect.
- Paystack `requested_amount`/Partial Debit semantics do not redefine FP-002 payment success.
- Customer fee pass-through remains disabled unless separately governed/disclosed; provider fees do not substitute for accepted amount.
- Bundle component refunds use immutable accepted checkout allocation snapshots, not current catalogue prices.
- Duplicate genuine collections do not create duplicate rights.

## 8. Accepted working Product clarification — not yet Product Law

**Duplicate collection correction and partial reversal attribution**

For one accepted Purchase Intent/order, exactly one genuine successful collection may satisfy the purchase. Any additional genuine successful collection remains truthful financial history but creates no second entitlement, credit, paid period or right. The full customer-collected excess amount remains owed and must be returned through safe source-scoped correction where reliable; if correction is ambiguous or cannot complete, the exact amount remains a visible Commerce-owned make-whole obligation until reconciled.

A partial provider dispute/chargeback/final reversal can establish a financial loss amount without establishing which NewYou component/right that amount represents. Commerce records the financial correction independently from access. Entitlements may permanently affect only a right deterministically identified by governed NewYou commercial evidence. Amount coincidence, provider aggregate status, callback ordering, current prices, arbitrary ordering or proportional allocation cannot manufacture component identity. Unattributable partial loss remains visible Finance/Commerce adjudication work, not an arbitrary entitlement mutation.

**Promotion state:** accepted in working form; formal governed Product/Decision successor still required unless authoritative review finds equivalent semantics already explicit.

## 9. Refund execution failure

If Paystack cannot execute an owed refund, including insufficient merchant balance:

```text
customer obligation remains open
+ Refund Intent remains unresolved/failed-needs-remedy
+ valid unrelated right remains unchanged
+ Finance/support work is durable and visible
+ no blind retry storm
+ restart preserves the exact owed amount and source
```

Provider execution capacity never decides whether NewYou owes the money.

## 10. Dispute Evidence Minimisation Contract

### Allowed by default when necessary

- order/provider transaction identity;
- accepted amount/currency/order snapshot;
- generic fulfilment/delivery/access timestamps;
- minimum receipt/value-delivery proof;
- provider-required customer contact fields to minimum necessary scope.

### Prohibited by default

- health/safety answers or screening detail;
- temperament questions/raw answers/result detail;
- personalised-plan contents;
- journals/private support or clinical notes;
- unrelated account history;
- credentials/tokens/secrets.

Sensitive participant evidence requires explicit Privacy/Legal/Operations escalation; Audit records minimum disclosure evidence without becoming business authority.

## 11. Reconciliation completeness

Reconciliation must tolerate:

- offset/cursor pagination;
- duplicated observations across overlapping windows;
- late provider objects;
- crash before/after checkpoint;
- `429`/provider outage;
- repeated pages/cursors;
- scan restart.

A page failure does not advance the durable completeness boundary. Completion is a bounded replayable watermark/window, not merely "last page fetched".

## 12. Launch channel scope

Current NewYou authority locks Paystack/South Africa/ZAR but not the exact FP-002 Paystack channel allowlist.

**Recommended first proof target:** `card` only.

This is a proof-scope recommendation, not permanent Product Law. Enable additional channels only after explicit admission and applicable `EV-020` proof.

## 13. Test/live boundary

Sandbox/test mode may prove protocol/invariant behavior that Paystack exposes there, but cannot certify production account/channel activation, settlement/payout, South-African dispute timing/account policy, production secret rotation, or all live operational behavior.

No test-mode result is silently promoted to live parity.

## 14. Development-entry boundary

This contract does not authorise implementation. Before FP-002 development entry, the normal Phase 7 sequence and applicable gates still apply. JIT may choose Resources/actions/indexes/jobs/adapter functions only to implement—never redefine—the authority above.

## 15. Current disposition

- Documentary/provider research: **PASS / STABILISED / FROZEN**.
- Provider-independent contract: **PASS / STABILISED**.
- Accepted Product clarification: **working-complete; formal promotion outstanding**.
- OQ-004 FP-002 provider proof: **BLOCKED / NOT EXECUTED**.
- Production operational evidence: **NOT DONE**.
