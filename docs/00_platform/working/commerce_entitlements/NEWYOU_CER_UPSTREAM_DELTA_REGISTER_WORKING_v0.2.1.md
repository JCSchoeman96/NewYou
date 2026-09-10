# NewYou Commerce / Entitlements / Recurring Membership Upstream Delta Register — Working v0.2.1

- **Status:** FINAL COMPACT WORKING DELTA REGISTER / NON-AUTHORITATIVE
- **Supersedes:** `v0.2.0` — provenance/SHA PATCH only; accepted policy-direction bodies unchanged
- **Detailed source:** `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.3.md`
- **Detailed source SHA-256:** `2966502d50e593359809b0c14071db725b544670a8ab9788daab8418a12131f4`
- **Implementation:** NOT AUTHORISED
- **Authority:** NONE

This register preserves the exact accepted policy-direction sections for all thirteen CER-owned Pre-JIT upstream deltas.

# 1. Current delta index

| Delta | Origin | Likely later governance cluster |
|---|---|---|
| `CER-UPD-001` | CER-PT-005 | Renewal / cancellation / cadence |
| `CER-UPD-002` | CER-PT-010 | Disputes / reversal |
| `CER-UPD-003` | CER-PT-012 | Gift / add-on / package / multi-source |
| `CER-UPD-004` | CER-PT-013 | Manual EFT |
| `CER-UPD-005` | CER-PT-016 | Renewal / cancellation / cadence |
| `CER-UPD-006` | Candidate 3 / CER-PT-008 | Renewal / cancellation / cadence |
| `CER-UPD-007` | CER-PT-017 | Price / recurring offer terms |
| `CER-UPD-008` | CER-PT-018 | Price / recurring offer terms |
| `CER-UPD-009` | CER-PT-019 | Wrong / duplicate collection remedy |
| `CER-UPD-010` | Candidate 11 / CER-PT-011 | Gift / add-on / package / multi-source |
| `CER-UPD-011` | Candidate 12 / CER-PT-012 | Gift / add-on / package / multi-source |
| `CER-UPD-012` | CER-PT-020 | Premium continuity |
| `CER-UPD-013` | Candidate 15 / CER-PT-011,012,020 | Gift / add-on / package / multi-source |

# 2. Exact accepted policy directions

## CER-UPD-001 — Cancellation during failed-renewal grace and late-success precedence

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-005
- **Likely later cluster:** Renewal / cancellation / cadence

### Accepted policy direction — exact section body from deep source `v0.30.3`

The accepted recommended direction is:

> **Cancellation during a failed-renewal grace window is effective immediately because the preceding paid period has already ended. It withdraws authority for unresolved future renewal collection and ends membership-only grace access. If a renewal was already authoritatively verified-paid before cancellation, the resulting paid period remains and cancellation takes effect at its end. Otherwise, any provider collection reconciled after cancellation must not reactivate the membership and must enter full reversal/refund or governed commercial-remedy handling.**

This direction deliberately makes Commerce authoritative rather than provider/network timing.

---

## CER-UPD-002 — Dispute/chargeback access and commercial-right consequences

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-010
- **Likely later cluster:** Disputes / reversal

### Accepted policy direction — exact section body from deep source `v0.30.3`

The accepted recommended direction is:

> **A payment dispute is a contested Commerce state, not immediate proof that the original payment or customer right was invalid. Opening a verified dispute must not erase historical payment, fulfilment, entitlement consumption or retained records, and must not trigger account-wide punishment. While a dispute is unresolved, NewYou should place only new or continuing value that materially depends on the disputed payment into a reversible source-scoped hold, while preserving already-delivered historical artifacts and required professional/safety records. If the dispute resolves in NewYou's favour, the hold is removed and the original commercial right resumes without duplicate grant. If the dispute is accepted or finally lost and the funds are reversed, Commerce records a financial reversal; future rights whose sole commercial source was that payment end or become non-active, but historical consumption and retained records remain immutable. A dispute against an expired historical period must not invalidate later independently paid periods. A final reversal must not itself imply fraud, debt, account-wide suspension or permanent account ban without separate governed authority.**

For once-off purchased artifacts, the accepted working clarification is:

> **“Permanent access” means non-expiring access while the qualifying purchase remains commercially valid. A later final chargeback reversal may end future paid-origin platform access without deleting historical fulfilment, provenance, professional/safety records or other records that must remain retained.**

---

## CER-UPD-003 — Redemption transfer, post-redemption control and recurring sponsorship authority

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-012
- **Likely later cluster:** Gift / add-on / package / multi-source

### Accepted policy direction — exact section body from deep source `v0.30.3`

The accepted recommended direction is:

> **Gift and sponsored purchase roles remain distinct across the full commercial lifecycle. Before redemption, the purchaser or sponsor controls only the unredeemed commercial allocation subject to applicable refund, reassignment, expiry and sponsorship terms. Redemption is an authoritative one-time transfer boundary: it binds the governed right to the resolved recipient/account holder, consumes the redemption authority and makes the resulting access non-transferable. After redemption, the purchaser or sponsor may see only the Product-authorised redemption/commercial status and may not ordinarily revoke the recipient's redeemed access or obtain participant health, assessment, Plan, check-in or activity data merely because they funded it. Participant-side refund or access decisions for an already-redeemed benefit belong to the recipient/participant under the applicable Product refund rules, while any resulting financial reversal is reconciled against the original purchase/payment source without exposing the participant's protected information to the purchaser. Payment corrections, fraud/security handling, disputes, chargebacks and other authoritative financial reversals remain governed separately and may affect the redeemed right according to their existing rules.**
>
> **Gifted membership is fixed-duration/prepaid by default and must not silently create recurring debit authority against the purchaser. Recurring sponsorship is allowed only through separate explicit payer consent. In an explicitly recurring sponsored relationship, the payer may stop future billing, but ordinary cancellation does not retroactively revoke the recipient's already-paid period. Sponsored grants already redeemed follow the validity/expiry terms fixed for that grant; sponsor changes normally affect future or unredeemed allocations unless Product Law or the pre-disclosed sponsored contract explicitly authorised earlier revocation. A recipient may decline or stop using sponsored access without granting the sponsor visibility into protected participant information.**

---

## CER-UPD-004 — Manual-EFT paid-period commencement

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-013
- **Likely later cluster:** Manual EFT

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **For an ordinary on-demand manual-EFT membership purchase, the paid access period begins when the payment is authoritatively verified and the membership can lawfully activate, rather than when the bank transfer was initiated or first received. A different commencement date may apply only where the purchased offer explicitly defines a fixed or scheduled service period before purchase. Delayed manual verification must not silently shorten the purchased access duration.**

---

## CER-UPD-005 — Membership billing-cadence transition

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-016
- **Likely later cluster:** Renewal / cancellation / cadence

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **A change between monthly and annual billing for the same membership composition is, by default, a future renewal instruction and does not create a second membership contract or revoke/regrant unchanged membership entitlements. The current paid period remains authoritative through its existing end regardless of whether that period is monthly or annual; ordinary cadence change does not truncate already-purchased time or create an implicit refund, credit or overlapping billing obligation. At the next not-yet-committed renewal boundary, exactly one renewal occurs under the newly selected cadence. If the previous-cadence renewal has already become authoritatively paid before the cadence-change instruction wins the boundary ordering, that resulting paid period remains truthful and the new cadence targets the following not-yet-committed boundary. Any Product option for early/immediate cadence conversion must separately define paid-time termination, refund/credit/proration, new-period commencement and failed/ambiguous adjustment treatment before implementation. Cadence change alone must not interrupt unchanged entitlement rights.**

---

## CER-UPD-006 — Rescission of pending membership cancellation

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** Candidate 3 / CER-PT-008
- **Likely later cluster:** Renewal / cancellation / cadence

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **A period-end membership cancellation is a revocable future non-renewal instruction until the membership has actually terminated or the relevant commercial boundary has otherwise become irreversibly resolved. While the existing paid membership remains live, an authenticated participant may rescind the pending cancellation and replace the future instruction with renew-unchanged. Rescission preserves the same membership relationship, current paid period and unchanged entitlement continuity; it does not create a new membership or paid period. Historical cancellation and rescission instructions remain auditable, but only the current authoritative future instruction governs renewal. Rescission is prospective: it must not retroactively authorize a collection that occurred after cancellation had already withdrawn renewal authority. If the membership has already terminated, continuation is a new re-subscription journey rather than cancellation rescission. Restoring membership renewal intent does not itself restore any separately revoked or invalid payment authority.**

---

## CER-UPD-007 — Existing-member recurring price migration

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-017
- **Likely later cluster:** Price / recurring offer terms

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **Publishing or activating a new membership list price does not retrospectively alter an existing member's current paid period and does not by itself rewrite that member's recurring commercial contract. For an existing active membership, a higher price may take effect only from an eligible future not-yet-committed renewal after NewYou has durably established the exact target price/currency/effective boundary, given the participant clear advance notice of the new price and effective boundary, and satisfied all applicable contractual and legal notice/consent requirements. If those requirements have not been satisfied before that renewal becomes commercially committed, the higher price must not be charged for that occurrence. An already-committed renewal remains governed by its immutable price snapshot. Grandfathering or price locking may be offered explicitly, but it is a deliberate commercial term attached to the qualifying membership occurrence/offer and must not arise accidentally from historic list price or provider configuration. A later post-termination re-subscription does not inherit an old price solely because the same participant held it previously. Provider price/configuration state is execution evidence only and must not redefine NewYou contract truth.**

---

## CER-UPD-008 — Recurring promotional pricing lifecycle

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-018
- **Likely later cluster:** Price / recurring offer terms

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **A recurring membership promotion is a commercial pricing term attached to a qualifying membership occurrence/offer and does not create a separate entitlement right. Every recurring promotion must define its pricing effect, qualifying scope, duration/consumption basis, commencement, post-promotion pricing rule and applicability across package/cadence changes. For cycle-limited promotions, one promotional cycle is consumed by one successfully established qualifying paid membership period, not by payment attempts, retries or duplicate execution; a renewal that never establishes a paid period does not consume a promotional cycle. Unused promotional cycles do not become standalone/banked credits and do not carry into a later post-termination membership occurrence unless Product explicitly promises otherwise. Re-subscription evaluates promotion eligibility under the current applicable offer and must neither automatically inherit remaining historical promotion value nor automatically reset a once-only promotion. An accepted promotion may not be retroactively altered by later mutation/deactivation of the public promotion definition. Upgrade, downgrade or cadence transition must resolve the exact target commercial contract—including base price/version, promotion applicability, remaining promotional scope and resulting charge—before commercial commitment. Duplicate user/provider execution must not multiply promotional benefit. Provider or mutable promotion configuration is execution/evaluation evidence only and cannot redefine the accepted NewYou commercial promise.**

> **For percentage promotions, the percentage applies to the membership's authoritative applicable base-price contract unless the offer explicitly promises a fixed promotional price. Any underlying base-price migration remains separately governed by `CER-UPD-007`; expiry of a promotion does not itself constitute a new unilateral base-price increase where the post-promotion pricing rule was clearly part of the accepted offer.**

---

## CER-UPD-009 — Duplicate ordinary membership purchase and excess collection

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-019
- **Likely later cluster:** Wrong / duplicate collection remedy

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **A canonical grantee may have at most one ordinary recurring membership commercial relationship admitted at a time; package, cadence and add-on changes to that relationship must use the governed membership-transition flows rather than creating a second overlapping ordinary membership. This exclusion is based on the intended grantee/commercial relationship, not merely purchaser, browser session, provider customer or payment reference, and does not prohibit separately governed gift, sponsored, complimentary or other legitimate entitlement sources. Concurrent or repeated purchase attempts must converge on exactly one admitted ordinary membership occurrence. If a non-admitted conflicting purchase nevertheless produces a successful financial collection, that payment remains truthful financial evidence but must not create a second membership, second paid period, duplicate recurring obligation or duplicate entitlement; NewYou must initiate full reversal/refund or, where automated reversal is unavailable, governed make-whole handling. The valid membership remains bound to the purchase that won NewYou's authoritative commercial-admission ordering, not whichever provider callback arrived first. Duplicate-payment remediation must be source-scoped and must not revoke or alter the valid membership. Provider transaction idempotency is necessary for retries of one payment but is not sufficient to enforce NewYou's one-ordinary-membership invariant across genuinely distinct purchase/payment attempts.**

---

## CER-UPD-010 — Ordinary membership add-on recurring lifecycle

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** Candidate 11 / CER-PT-011
- **Likely later cluster:** Gift / add-on / package / multi-source

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **An ordinary membership add-on is a recurring commercial component of the existing Basic membership relationship, not a second ordinary membership contract. Basic remains the prerequisite base subscription and the authoritative membership composition is Basic plus zero or more active add-on components. Unless an offer explicitly defines a separately billed add-on, an add-on inherits the base membership's billing cadence and renewal boundary. Adding an add-on to an active membership is a composition upgrade: it may become effective during the current paid period only after any required incremental/prorated commercial adjustment becomes authoritative, and failed or unresolved adjustment must leave the existing membership unchanged. Thereafter the add-on renews as part of the same membership composition. Removing an add-on is a composition downgrade and ordinarily takes effect at the next not-yet-committed membership renewal boundary, preserving already-paid add-on access through the current paid period and creating no ordinary partial-period refund. Removing one add-on does not cancel Basic or unrelated components. Cancelling the Basic membership schedules the ordinary membership composition, including dependent add-ons, to end at the governing paid-period boundary; a dependent ordinary add-on must not outlive the Basic membership source it augments. Entitlement consequences remain source/provenance-aware, so ending a membership/add-on commercial source must not remove an equivalent right that remains valid through another authoritative source. Premium remains a named commercial bundle over Basic plus governed add-on components, and transitions to/from Premium apply source→target component deltas without artificial revoke/regrant of unchanged rights or duplicate billing obligations. Any independently billed add-on with a cadence or paid period different from Basic requires an explicit Product offer defining its independent renewal, cancellation, failure and dependency semantics rather than arising by implementation accident.**

---

---

## CER-UPD-011 — Gift/sponsored membership overlap with existing membership

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** Candidate 12 / CER-PT-012
- **Likely later cluster:** Gift / add-on / package / multi-source

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **Gift and sponsored membership access remain distinct commercial/entitlement sources and do not merge into or overwrite a recipient's existing membership provenance. Before an irrevocable redemption is consumed, NewYou must evaluate the canonical grantee's relevant active or already-committed membership coverage and make any material overlap outcome clear to the recipient. For ordinary fixed/prepaid duration-based membership gifts or sponsorships, equivalent already-paid coverage must not cause the incoming value to be silently consumed concurrently by default. The incoming source instead begins at the next eligible not-yet-committed boundary after already-paid equivalent coverage, unless the governed offer explicitly defines a fixed calendar window or an immediate-start rule. For periods fully funded by the gift/sponsor source, NewYou must not also collect an overlapping ordinary self-paid renewal for the same covered membership composition. A fixed-duration gift may permit self-paid renewal to resume after gift coverage only where that resulting schedule is clearly disclosed and accepted and payment authority remains valid. Open-ended or uncertain-duration sponsorship must not automatically restart personal billing when sponsorship ends unless the participant explicitly opted into such fallback. Sponsor termination affects future funding only and does not revoke an already-funded recipient period. Applying a gift/sponsorship does not rewrite historical paid periods or silently rescind an existing membership cancellation. Different or narrower target compositions must be disclosed rather than silently upgrading or downgrading the recipient. Fixed-calendar sponsored offers may consume during overlapping coverage only when that bounded-window behavior is part of the accepted offer. Entitlement provenance remains source-specific throughout, and termination of one source must not revoke access independently sustained by another valid source.**

---

---

## CER-UPD-012 — Premium reassessment continuity, maturity and nonaccumulation

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** CER-PT-020
- **Likely later cluster:** Premium continuity

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **The Premium annual reassessment benefit is earned from uninterrupted qualifying Premium coverage of the canonical grantee, not from payment-attempt count, payment method, billing cadence or funding-source identity. The first reassessment entitlement becomes available after twelve calendar months of uninterrupted qualifying Premium coverage; for an annual Premium membership, an authoritatively paid annual renewal at the first anniversary is the ordinary annual-billing expression of the same maturity rule and is not an additional or accelerating trigger. Initial annual purchase and a switch into annual billing do not themselves constitute annual renewal for this purpose. Monthly↔annual cadence changes, price or promotion changes, payment-method replacement and seamless transitions between qualifying self-paid, gift or sponsored Premium sources preserve continuity when there is no uncovered Premium interval. Overlapping qualifying sources count elapsed time once and do not accelerate eligibility. A source contributes to continuity only where its governed offer constitutes qualifying Premium membership coverage; partial Premium-like grants do not qualify by accidental entitlement equivalence. During unresolved failed-payment grace, continuity and any maturity dependent upon that boundary remain provisional until Commerce establishes the relevant paid Premium period; successful reconciliation covering the boundary preserves continuity, while an ultimately unpaid uncovered period breaks continuity at the prior paid-period end. Downgrade to Basic, termination of qualifying Premium or any genuine uncovered Premium interval breaks continuity, and a later Premium upgrade begins a new continuity interval. An unused Premium reassessment entitlement expires when qualifying Premium coverage ends, even where the broader Basic membership relationship continues. At each successive twelve-month qualifying anniversary no more than one unused reassessment entitlement may exist; where one is already unused, no additional or catch-up entitlement is banked, and after later consumption the next entitlement becomes available only at the next future qualifying anniversary.**

---

## CER-UPD-013 — Multi-source entitlement overlap and grant commercial effect

- **Status:** ACCEPTED PRE-JIT UPSTREAM DELTA / NOT YET GOVERNED PRODUCT LAW
- **Origin:** Candidate 15 / CER-PT-011,012,020
- **Likely later cluster:** Gift / add-on / package / multi-source

### Accepted policy direction — exact section body from deep source `v0.30.3`

> **Multiple legitimate entitlement sources for the same canonical grantee may coexist and retain independent identity, scope, validity, provenance, revocation and consumption history. Effective non-consumable access is the union of currently valid qualifying sources; expiry, revocation, refund, dispute or termination of one source must not remove access independently sustained by another valid source. Effective access composition does not itself rewrite the participant's authoritative Commerce membership contract or create a synthetic membership tier. Every complimentary, sponsored, gift, lifetime or other governed grant must derive its commercial and benefit effect from its explicit offer/authority: an access-overlay grant affects only its stated scopes and does not alter membership billing or membership-tenure qualification unless explicitly authorised; a qualifying membership-coverage grant may fund/substitute the covered membership composition for its governed interval. Where qualifying membership-coverage grant value makes a future ordinary self-paid collection fully redundant for the same composition and interval, NewYou must suppress that overlapping collection at the next not-yet-committed boundary unless a separate explicit commercial basis authorises it; already-paid periods remain unchanged. Partial grants suppress or replace only the commercial components they explicitly cover and do not cancel unrelated base membership obligations. Overlapping sources do not by themselves multiply recurring limited benefits, credits, continuity clocks or nonaccumulating entitlements. Product-defined limits such as the ordinary monthly Premium review and annual reassessment remain participant/benefit limits across equivalent overlapping sources. Additional consumable units arise only where an explicit governed offer/grant promises additive value. Consumption must apply exactly once against an authoritative eligible benefit occurrence/source and preserve auditable provenance.**

---

# 3. Cross-stream boundaries

Preserve HSP ownership of `HSP-UPD-001`, `005`, `006`, `007`, `008`.

Preserve Privacy ownership of `PRIV-WD-002` / `PRIV-UPD-002`.

# 4. Governance rule

These thirteen deltas remain working/non-authoritative. Reconcile overlapping CER/HSP/Privacy inputs into the smallest coherent governed Product rules before downstream implementation depends on them.
