# NewYou Operations, Support & Paid Pilot Pre-JIT Contract — Working v0.1.0

> **STATUS:** COMPACT WORKING PACK CANDIDATE / NON-AUTHORITATIVE
> **AUTHORITY:** NONE
> **IMPLEMENTATION AUTHORITY:** NONE
> **IMPLEMENTATION:** NOT AUTHORISED
> **DEEP SOURCE:** `deep/NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.32.0.md`
> **DEEP-SOURCE SHA-256:** `9d7895b6db1b9b2eb12b3c7c0ff38c16f29915ea730967e2a7c514c8c40fb518`

Live governed NewYou authority always wins. This working contract does not amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Feature Pack contracts or JIT dossiers.

## 1. Scope and closure posture

This is the compact semantic contract for Operations, Support and staged paid-pilot preparation. Broad Pre-JIT discovery is closed unless new evidence, changed scope or higher authority creates a real contradiction. No `OPS-UPD-008`, Operations Domain, Support Domain, Admin Domain, Refund Domain, Timer/Choice Domain or new architecture mechanism is created.

Operations / Support means:

```text
workflow + attention + observation + governed command surface
!= source business authority
```

## 2. Owner-authority doctrine

```text
every durable business truth
→ exactly one owning Domain

operator/support screen
→ may compose multiple truths
→ owns none of them

cross-domain action
→ invokes owning Domain

work / queue
→ attention and responsibility
→ not business authority
```

Provider dashboard/state, Analytics, Audit evidence, support notes, cache, PubSub, UI state, worker/job state and message/provider state never silently become business authority.

A support/operator journey projection may compose Commerce, Entitlements, Temperament, Safety, Plans, Communications, Privacy and Audit/Analytics where permitted. The projection is never a synthetic writable business status.

```text
provider says paid != Commerce verified payment
Commerce paid != Entitlement active
Entitlement active != paid benefit fulfilled
email delivered != participant currently has access
support work closed != underlying business consequence completed
```

## 3. Operator authority and minimum-necessary context

Role labels alone are insufficient. Consequential action requires current actor assurance, role/capability, relationship, purpose, scope, unexpired authority, applicable approval and current owner-Domain guards.

- stale page/session/approval/role state cannot authorise a consequential mutation;
- no universal Super Admin exists;
- routine impersonation is prohibited;
- break-glass is scoped exceptional capability, not universal business power;
- bulk convenience still enforces owner invariants per target;
- accepted command is distinct from completed consequence;
- business idempotency is required for material repeatable commands.

Payer, sponsor, operator or support status does not itself grant recipient-private health, Safety, Assessment, Plan, professional or deletion information.

## 4. Correction / reconciliation vocabulary

These are semantic distinctions, not universal Resources:

| Term | Meaning |
|---|---|
| retry | repeat execution of the same still-authorised logical operation after known retryable failure |
| re-execution | another execution attempt for existing business intent; consequence remains repeat-safe |
| reconciliation | converge owner truth from durable platform state plus legitimate external/async evidence |
| correction | rectify/qualify owner truth under that record type's correction law |
| override | explicit exceptional owner-authorised transition with reason/scope/evidence |
| replacement | new immutable/superseding artefact/version; predecessor remains historical |
| refund | Commerce-owned monetary obligation/outcome |
| financial reversal | later economic truth reversing/correcting an earlier effect without making the earlier event fictional |
| entitlement revocation | Entitlements-owned end of a specific current right/source |
| entitlement restoration | Entitlements-owned recreation/restoration only from a valid governed source consequence |
| cancellation | owner-authorised termination of an open/future obligation/path |
| suspension | reversible restriction while history/contract may remain |
| withdrawal | owner-specific ending of permission/content/service authority |
| deletion | Privacy-orchestrated category-aware destruction/anonymisation/suppression lifecycle |
| support annotation | internal context only; not source business truth merely because staff wrote it |

```text
correction != compensation
provider evidence != reconciliation authority
later refund/reversal/revocation != historical earlier event never occurred
```

Never use direct database editing as the ordinary correction API.

## 5. Pilot exposure, paid-demand evidence and release stages

Pilot release exposure and paid-demand evidence are different dimensions.

```text
historical cumulative real external participant exposure
+ protected reservation capacity
<= effective cumulative admission ceiling
<= 50
```

A real external sponsored/complimentary participant who receives genuine pilot-qualified production access may consume release exposure because the cap protects real external exposure. Once counted, refund, withdrawal, Safety pause, inactivity, entitlement revocation or Full Deletion does not recycle the historical slot.

Paid-demand evidence is narrower:

```text
verified actual positive payment
→ may qualify as paid-demand evidence

free / staff / complimentary / 100%-discount / manual grant
→ does not become paid-demand evidence merely because it consumed pilot exposure
```

Current first-pilot progression:

```text
internal validation
→ first 10
→ review
→ expand toward <=25
→ review
→ expand toward <=50
```

Keep separate historical exposure, numeric cumulative ceiling, current admission-open/closed gate and pre-admission reservation capacity. The current numeric ceiling is monotonic non-decreasing. Rollback/pause closes the new-admission gate; it does not lower the cumulative ceiling or rewrite history. Re-entry is deliberate. Expansion is never automatic, and technical capacity never authorises expansion.

## 6. OPS-UPD-001 — pilot admission / exposure / stage cap

The current working model is the §5 exposure/stage model above. Concurrency-safe admission must preserve counted + protected reservation capacity within the current exact ceiling; stale dashboards/Analytics cannot admit. Refund/deletion cannot recycle exposure. Formal Product/release-policy promotion remains required where current frozen authority does not yet contain these exact semantics. JIT may choose transaction/lock/reservation representation; it may not choose the Product cap or count/re-entry meaning.

## 7. OPS-UPD-002 — duplicate genuine collection / payer make-whole

```text
duplicate evidence != duplicate genuine collection
one obligation + multiple genuine collections → retain lawful amount; make payer whole for excess
two intended purchases → separate obligations
```

Commerce owns the net economic result. Provider state is evidence until reconciled. One intended purchase yields at most one valid entitlement consequence. Refund/reversal/chargeback/duplicate-remediation are reconciled so the payer is made whole exactly once for each valid monetary claim.

## 8. OPS-UPD-003 — consequential human command authority

```text
actor + current assurance + role/capability + relationship + purpose + scope
+ unexpired authority + required approvals + current owner state/invariants
= may accept command
```

Commands execute through the owning Domain. No generic Operations/Admin write authority is created. Exact role/action matrices, approval thresholds and work/case representation remain JIT/policy detail unless they change Product/clinical/privacy/security powers.

## 9. OPS-UPD-004 — paid Assessment credit lifecycle

Current working Product direction:

```text
available_unused → held_unconsumed → consumed
                              ↘ closed_after_refund
```

First answer claims/holds the credit; it does **not** consume it. Consumption requires complete paid digital Assessment delivery: immutable governed result, paid report, required primary/secondary guidance, required introductory personalised guidance, and durable authorised-participant availability.

Post-first-answer nontechnical expiry without successful delivery:

```text
attempt = terminal
same paid credit → available_unused
no refund created merely by expiry
no consumption
no duplicate credit
```

Annual-retake reference event is prior successful digital Assessment delivery. Notification/open/read/provider/Analytics state is not consumption authority. Historical `close_unconsumed` is superseded. Formal Product/Decision promotion remains required before implementation.

## 10. OPS-UPD-005 — Plan pre-first-fulfilment intent / failed fulfilment / refund boundary

Before first qualifying personalised Plan delivery, latest lawful participant intent may change; current Safety outranks stale preference; a stale generated snapshot cannot be delivered as current truth. Generation and first successful fulfilment are separate facts.

Ordinary refund:

```text
before generation → ordinary Plan refund available
after generation → ordinary change-of-mind refund closed
```

The post-generation/pre-first-delivery Safety-invalidated remedy is a **working Product amendment** and must not be described as already contained in historical DEC-045.

Where a paid Plan was generated, no first delivery succeeded, and current Safety blocks qualifying first fulfilment (other than a still-actionable temporary `insufficient_information` state), an **accrued elective refund remedy** exists. Recipient may retain the unconsumed right or relinquish it through refund.

- `general_wellness_only`: retain right OR elect failed-fulfilment refund;
- `professional_review_required`: retain right OR refund; professional review remains separate;
- actionable `insufficient_information`: complete the current clarification path first;
- still `eligible_automated` but prior snapshot stale: safely regenerate under the same right; exceptional refund does not arise merely from regeneration.

## 11. OPS-UPD-006 — export / Full Deletion composition

Export is a point-in-time governed release, not a live mirror, recovery credential or reconstruction authority. A lawfully downloaded participant-held copy may remain outside platform control; platform-controlled export artefacts/capabilities must terminate according to deletion policy. If an accepted pre-deletion export could still disclose after deletion, it must reach a governed terminal outcome before deletion can be declared complete.

Business and data lifecycle remain separate. An accrued/committed valid refund obligation survives Full Deletion through minimum restricted Commerce evidence without reconstructing account, Plan, health record or entitlement.

```text
remedy qualification != refund request != refund commitment != provider settlement != terminal net outcome
```

At irreversible deletion execution, a still-valid accrued elective remedy whose retain-the-Plan branch is being destroyed converts into a durable Commerce refund obligation before entitlement destruction. **Durable refund commitment before entitlement destruction does not mean external provider settlement is required before deletion completion.** Once the obligation is durably preserved, the entitlement irreversibly closed and other deletion requirements pass, Privacy may complete deletion; Commerce continues provider reconciliation afterward. Provider failure never resurrects the deleted account/right.

## 12. OPS-UPD-007 — General Wellness / paid Plan disposition

```text
General Wellness != paid personalised Plan fulfilment
General Wellness use != Plan-entitlement consumption
```

Before generation, `general_wellness_only` blocks personalised generation but leaves the paid Plan right active/unfulfilled and ordinary pre-generation refund available. If later `eligible_automated`, the same still-valid unfulfilled right may fund exactly one first qualifying Plan unless refunded/deleted/otherwise closed.

**Current MVP:** no bounded General Wellness participant election/timer is authorised.

**Future conditional invariant:** IF later Product authority explicitly creates a bounded participant election, its clock starts only when the complete current governed choice is durably available and actually exercisable. It does not start merely from internal eligibility timestamp, provider state, notification acceptance, read/open telemetry, Analytics, stale UI or operator queue state. This is not current MVP behaviour.

## 13. Accepted Pre-JIT working R549 bundle allocation candidate

This is **not frozen Product Law**. It is the accepted Pre-JIT working Product/Commercial allocation proposed for explicit governed promotion:

```text
Assessment = R249
Plan       = R300
Total      = R549
R99 discount allocated to Plan component
```

The accepted historical offer-version allocation controls later component refund; retained component is not repriced after purchase. Future paid offers need their own deterministic allocation before activation where component refunds may arise.

## 14. Purchaser / payer / recipient / participant separation

Keep distinct:

```text
purchaser
payer
recipient
participant
account holder
```

After redemption:

```text
recipient → controls redeemed entitlement retain/relinquish decision
authoritative payer/payment relationship → receives monetary refund
```

Payer funding creates neither entitlement-control power nor recipient-private visibility.

### 14.1 Before redemption

```text
refund/cancellation authority
→ authorised purchaser / sponsor / commercial-order actor under accepted offer

refund destination
→ authoritative payer/payment relationship
```

Bare payer status does not automatically equal cancellation authority.

### 14.2 Redeemed third-party ordinary pre-generation refund

Payer/purchaser may request review, but after redemption recipient relinquishment is required before optional ordinary pre-generation refund commits. If recipient wants to retain Plan, optional refund does not commit. If recipient relinquishes, Entitlements closes the corresponding right and Commerce commits refund payer-side.

Never allow committed refund + live corresponding redeemed Plan entitlement. Never revoke merely because payer requested refund.

### 14.3 Split-party failed fulfilment

The redeemed recipient controls retain/relinquish. Money returns to the authoritative payer/payment relationship. Payer-facing information is minimum commercial status only; no recipient Safety/health/Assessment/Plan/progress/deletion reason is disclosed.

Payer deletion does not destroy another person's redeemed entitlement. Zero-price complimentary/sponsored rights create no invented cash refund. Positive-price sponsored/bulk offers need deterministic attributable refund allocation before activation where refunds may arise.

## 15. Full Deletion × ordinary third-party pre-generation refund

If a redeemed paid third-party Plan remains ungenerated and ordinarily refundable when the recipient reaches irreversible Full Deletion, deletion acts as final recipient relinquishment. Commerce must durably commit the valid refund to the authoritative payer/payment relationship before entitlement destruction.

```text
refund commitment before entitlement destruction
!= provider settlement before deletion completion
```

Provider outage/failure cannot block privacy deletion indefinitely once the obligation is durably preserved, or resurrect account/entitlement afterward.

## 16. Support projections, incidents and safe-stop doctrine

Support can compose owner truths for a participant journey but never edits a synthetic journey status. Minimum necessary visibility applies throughout.

Graceful degradation may use read-only, limited-capability or maintenance modes. Never guess payment, entitlement, health or Safety truth. New admissions may be stopped more narrowly than obligations already owed to existing participants. Capability-specific degradation behaviour belongs to JIT/proof. Operator recovery never bypasses owner authority. Historical incidents remain evidence after remediation; correction does not rewrite incident history.

## 17. Operational measurement and evidence boundaries

Analytics may measure support contact burden, manual intervention, release/pilot metrics, refunds/incidents and progression evidence. Analytics does not authorise admission, refund, entitlement, Safety or release progression. Audit preserves selected governed evidence but does not authorise release merely by containing a record.

Downstream definitions intentionally retained:

- support-interaction measurement unit → prospective JIT definition;
- per-product Day-7/30/90 anchors → prospective JIT definition;
- capability-specific degradation runbooks → JIT/proof;
- Audit degraded-mode classification → Audit JIT/proof.

## 18. Release / NO-GO gates

At minimum retain:

- formal Product/Decision promotion of accepted working commercial amendments;
- pilot stage sign-offs;
- payment/refund provider validation;
- duplicate collection/refund/chargeback reconciliation proof;
- Safety/clinical gates;
- legal/privacy/retention gates;
- export/deletion/restore proof;
- communications/provider gates where applicable;
- first-paid operations/support/incident readiness;
- operational measurement definitions;
- degradation/runbook proof.

```text
unresolved required gate → affected stage = NO-GO
```

This does not mean unrelated platform truth has failed.

## 19. JIT boundary

Downstream JIT/proof may choose exact Resource/table names, Ash actions, Ecto schemas, transactions, DB locks, indexes, reservation expiry, Oban jobs, queue structures, operator UI composition, Redis/ETS/GenServer use, support-case representation, duplicate-account algorithm, provider refund APIs, exact retention fields/durations, degradation runbooks and metric event schemas.

JIT may not redefine Product money/refund/entitlement/Safety/deletion semantics, create shared-write ownership, turn projections/providers into authority, or invent the missing formal authority promotions.

## 20. Closure rule

Do not create `OPS-PT-471` merely because packaging, cross-references or implementation mechanisms remain unresolved. Reopen broad Operations Pre-JIT only for new contradictory evidence, changed Product scope, higher-authority drift or a genuine JIT-discovered semantic gap.
