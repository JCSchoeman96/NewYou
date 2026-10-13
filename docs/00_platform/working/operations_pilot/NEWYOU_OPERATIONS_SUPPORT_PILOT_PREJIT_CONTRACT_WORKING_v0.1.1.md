# NewYou Operations, Support & Paid Pilot Pre-JIT Contract — Working v0.1.1

> **STATUS:** FROZEN WORKING SEMANTIC PACK / NON-AUTHORITATIVE
> **AUTHORITY:** NONE
> **IMPLEMENTATION AUTHORITY:** NONE
> **IMPLEMENTATION:** NOT AUTHORISED
> **DEEP SOURCE:** `deep/NewYou_Operations_Support_Pilot_PreJIT_Working_Control_Document_v0.32.0.md`
> **DEEP-SOURCE SHA-256:** `9d7895b6db1b9b2eb12b3c7c0ff38c16f29915ea730967e2a7c514c8c40fb518`

Live governed NewYou authority always wins. This working contract does not amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Feature Pack contracts or JIT dossiers.

**Freeze meaning:** `FROZEN WORKING SEMANTIC PACK` means broad Operations Pre-JIT discovery is closed and these working semantics are the stable baseline unless new contradictory evidence, changed Product scope, higher-authority drift, provider/expert evidence, or a genuine JIT-discovered semantic contradiction requires reopening. It does **not** mean governed Product/Decision authority, implementation approval, or independent certification.

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

## 4A. Locked cross-cutting invariants retained by compression

These invariants remain current within this frozen working stream. They are not optional implementation commentary.

1. Unknown consequential outcomes are **reconciled from authoritative evidence**; do not blindly retry, guess success/failure, or manufacture a terminal state.
2. Keep independent dimensions separate:
   ```text
   work / queue state
   != command-attempt state
   != source-Domain business state
   != provider state
   != participant-communication state
   ```
3. The command verbs `request`, `approve`, `execute`, `retry`, `reconcile`, `correct`, `compensate`, `restrict`, `restore`, `override` and `bulk` are not synonyms and may carry different authority/guards.
4. Correction and compensation are distinct; a later true refund/revocation/replacement does not make an earlier legitimate historical event false.
5. Commerce owns money truth; Entitlements owns current right/access truth. Neither owner infers the other's transition from a provider callback or UI state.
6. Provider refund execution state is distinct from whether money is owed. Provider failure cannot erase a valid customer-money obligation.
7. Replayed provider evidence for one economic collection is not a second collection. Partial provider amount coincidence, current price or callback order does not establish component identity.
8. Assessment attempt state, credit availability/hold, result/report state, refundability and credit consumption remain separate.
9. Plan generation/request state, Plan entitlement state, Safety state and first-fulfilment state remain separate.
10. Safety-relevant new information routes through Health Records / Safety & Eligibility authority; ordinary preference intent cannot preserve or recreate stale Safety authority.
11. Full Deletion, export request validity, export generation, protected delivery capability, participant-held copy and retained-by-obligation financial/legal evidence remain separate lifecycle dimensions.
12. No stale worker, signed link, restored backup, queue item or projection may resurrect a deleted entitlement/account or an obsolete business decision.
13. Pilot release exposure, reservation capacity, sale/payment state, Entitlement access and paid-demand evidence remain separate.
14. Analytics/Audit evidence may measure or prove; it does not authorise admission, refund, Safety, Entitlement, release progression or mutation.
15. No working conclusion below higher authority may be promoted by implementation convention. Where formal Product/Decision promotion is still required, JIT fails closed rather than choosing the Product rule.

## 5. Pilot exposure, paid-demand evidence and release stages

Pilot release exposure and paid-demand evidence are different dimensions.

```text
historical cumulative real external participant exposure
+ protected reserved-but-not-counted capacity
<= effective cumulative admission ceiling
<= 50
```

### Counted-admission boundary

A real external person becomes a counted first-pilot participant only when NewYou durably establishes that person's **pilot-qualified production access to the protected core pilot journey**.

For the ordinary paid path:

```text
pending / ambiguous provider event
→ not counted admission

verified commercial path without usable participant access yet
→ preserve protected capacity while reconciling

lawful Commerce → Entitlements path reaches current usable pilot access
→ counted exactly once
```

For an explicitly approved sponsored/complimentary/goodwill external pilot path, the corresponding governed external access grant may establish the same real-participant exposure even with no positive price.

Invitation, waitlist and mere checkout start do not count.

### Reservation semantics

A bounded pre-admission reservation may temporarily consume capacity to prevent oversubscription. It is bound to one intended participant lineage, is idempotent under retries, and is **not** counted exposure.

```text
payment pending / ambiguous
→ participant not yet counted
→ protected reservation is not silently released/resold
→ reconcile authoritative outcome first
```

A reservation may be released only while the participant has not crossed the counted-admission boundary and the governing attempt has reached a lawful release outcome.

### Participant-centric exposure

```text
one real external participant
→ at most one counted first-pilot admission
```

Orders, products, attempts, callbacks or collections do not multiply the count. If purchaser and participant/recipient differ, the real admitted participant/recipient is the exposure identity, not merely the payer.

A counted participant remains historical exposure after refund, cancellation, inactivity, withdrawal, support remediation, Safety pause, entitlement revocation or Full Deletion. Those events do not mint replacement pilot capacity.

Paid-demand evidence is narrower:

```text
verified actual positive payment
→ may qualify as paid-demand evidence

free / staff / complimentary / 100%-discount / manual grant
→ does not become paid-demand evidence merely because it consumed pilot exposure
```

Genuine discounted positive payment may qualify when list price, promotion and actual amount paid remain distinct.

Current first-pilot progression:

```text
internal validation
→ first 10
→ review
→ expand toward an explicitly authorised ceiling <=25
→ review
→ expand toward an explicitly authorised ceiling <=50
```

Keep separate historical exposure, numeric cumulative ceiling, current admission-open/closed gate and protected pre-admission reservation capacity. The current numeric ceiling is monotonic non-decreasing. Rollback/pause closes the new-admission gate; it does not lower the cumulative ceiling or rewrite history. Re-entry is deliberate. Expansion is never automatic, and technical capacity never authorises expansion.

Stale dashboards, Analytics, spreadsheets, process memory or node-local counters cannot authorise the next admission.

## 6. OPS-UPD-001 — pilot admission / exposure / stage cap

The current working model is the §5 exposure/stage model above.

Core fail-closed invariants:

```text
counted participants
+ protected reserved-but-not-counted capacity
<= current exact authorised cumulative ceiling

one participant admission lineage
→ counted at most once

ambiguous payment / entitlement outcome
→ no admission from ambiguity
→ protected capacity not silently recycled

failed or unavailable capacity authority
→ no new protected admission
```

A stage stop prevents new admissions where it applies but does not silently revoke existing rights, erase counted history or open replacement places.

Formal Product/release-policy promotion remains required where current frozen authority does not yet contain these exact semantics.

JIT may choose the concrete PostgreSQL transaction/lock/reservation representation and expiry mechanics, but it may not choose the Product cap, counted-admission meaning, reservation business semantics, re-entry meaning or historical non-recycling rule.

For the current first-pilot ceiling of 50, the working evidence does **not** justify Redis, ETS, Cachex, GenServers or a generic scarce-inventory service as an admission authority/acceleration mechanism. Any future extra mechanism requires independent evidence and must preserve PostgreSQL/durable owner authority rather than create competing truth.

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

Commands execute through the owning Domain. No generic Operations/Admin write authority is created.

Consequential command lifecycle dimensions remain explicit:

```text
request
→ optional approval
→ owner acceptance/rejection
→ execution attempt(s)
→ reconciliation if outcome is unknown/ambiguous
→ terminal owner outcome
```

`request`, `approve`, `execute`, `retry`, `reconcile`, `correct`, `compensate`, `restrict`, `restore`, `override` and `bulk` are not interchangeable actions. A work item being assigned/closed, an Audit record being written or a provider operation being accepted does not imply the underlying business command completed.

Unknown outcomes reconcile current authoritative evidence; they are not blindly replayed. Retries/re-execution remain business-idempotent and revalidate current authority. Bulk convenience preserves per-target policy/invariants.

Exact role/action matrices, approval thresholds and work/case representation remain principally FP-006 JIT/operating-policy work. Formal Product/clinical/privacy/security promotion is required only where those powers themselves change; `OPS-UPD-003` does not by itself demand a broad Product amendment.

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

Keep these boundaries separate:

```text
generation work exists
!= first successful personalised Plan fulfilment

ordinary refund eligibility
!= Plan entitlement fulfilment/consumption
```

### Pre-first-fulfilment change of initial intent

Before first successful qualifying Plan delivery, a lawful change to the participant's intended initial Plan does **not** require a second Plan purchase merely because earlier onboarding choices were saved, an old generation request was queued, generation started, or an undelivered immutable candidate snapshot already exists.

Before generation, permitted initial intent may change within the purchased Product scope. Safety-relevant factual changes are not mere preferences: Health/Safety truth updates and current eligibility must be re-evaluated.

After generation has started or an immutable candidate exists, but before successful first delivery:

1. the old generation lineage cannot later become the delivered/current Plan once a newer lawful intent is accepted;
2. already-generated stale snapshots remain immutable historical/internal evidence where required and are not destructively rewritten;
3. the **same still-unfulfilled purchased Plan right** may produce the one eventual qualifying first delivery from the latest lawful/current inputs;
4. no second charge or second Plan entitlement is created;
5. at most one participant-visible first fulfilment may consume that purchased initial-Plan right.

Conceptually:

```text
intent v1
→ superseded by lawful intent v2
→ superseded by lawful intent v3
→ one eventual first fulfilled Plan
```

Safe JIT outcomes may cancel/abort stale work, retain a stale immutable candidate as non-deliverable evidence, regenerate from the latest valid snapshot, or surface a current-state conflict. JIT may choose the mechanism; it may not deliver stale work merely because it completed later or because regeneration has technical cost.

Display-only changes such as approved energy-unit presentation, approved language presentation or use of alternatives already contained in a delivered Plan are not automatically re-personalisation.

A lawful selection of another valid current Temperament profile before first delivery uses that latest selected valid profile for the initial Plan under the same purchase. This is distinct from the specific post-delivery DEC-036 complimentary regeneration rule.

### Safety boundary

Current Safety always outranks participant preference. Material Health/Safety changes before delivery invalidate stale generation assumptions and require current Safety/Eligibility revalidation. The participant cannot preserve an unsafe prior eligibility result by asking the platform to use old answers.

### Participant pause / abandonment

The platform does not force generation merely to consume a Plan right. Before first fulfilment, an unfulfilled right may remain available for lawful later resume subject to current Entitlement law and revalidation of Safety/time-sensitive inputs. No new expiry is invented here.

### Post-delivery boundary

After first successful delivery:

```text
initial once-off Plan obligation = fulfilled
```

A later material preference/progress-based Plan change requires a new purchase or qualifying membership/add-on unless an explicit existing correction, Safety replacement or complimentary-regeneration rule applies. OPS-UPD-005 creates no generic post-delivery free-regeneration right.

### Ordinary refund

```text
before generation
→ ordinary Plan refund available under current law

after generation
→ ordinary change-of-mind refund closed

after generation but before first delivery
→ ordinary refund may be closed
AND purchased Plan obligation may still be unfulfilled
```

The post-generation/pre-first-delivery Safety-invalidated remedy is a **working Product amendment** and must not be described as already contained in historical DEC-045.

Where a paid Plan was generated, no first delivery succeeded, and current Safety blocks qualifying first fulfilment other than a still-actionable temporary `insufficient_information` state, an **accrued elective refund remedy** exists. Recipient may retain the unconsumed right or relinquish it through refund.

- `general_wellness_only`: retain right OR elect failed-fulfilment refund;
- `professional_review_required`: retain right OR refund; professional review remains separate;
- actionable `insufficient_information`: complete the current clarification path first;
- still `eligible_automated` but prior snapshot stale: safely regenerate under the same right; exceptional refund does not arise merely from regeneration.

If a refund becomes durably committed, competing first fulfilment is blocked until financial reconciliation reaches the governed outcome.

## 11. OPS-UPD-006 — export / Full Deletion composition

Export is a point-in-time governed release, not a live mirror, portable entitlement, recovery credential, account backup or reconstruction authority.

Keep the lifecycle dimensions separate:

```text
export request validity
!= export generation
!= protected delivery capability
!= participant-held copy
!= Full Deletion request/pending state
!= irreversible deletion execution/completion
!= retained-by-obligation financial/legal evidence
```

### Snapshot / provenance

A completed export is an as-of snapshot assembled from eligible authoritative records. It should preserve enough generation/data-as-of/category/version provenance to avoid implying the archive is always the participant's current account. The export payload never becomes source-Domain authority.

### Full Deletion request before execution

Full Deletion may revoke ordinary product/account access while a **narrow, strongly verified pre-execution export pathway** remains available where current Product/privacy law requires it.

That export path:

- does not reactivate ordinary account use;
- does not restore Entitlements;
- does not reopen optional processing;
- does not permit editing underlying business records;
- revalidates identity/authority appropriate to sensitive export.

### Ordering / terminality

Every accepted pre-execution export that could otherwise disclose participant data later must reach a governed terminal outcome before deletion can be declared complete. Deletion cannot be marked complete while an old worker, signed URL, delivery token, object-store artefact or external processor capability can later expose the deleted participant estate.

Exact legal deadline and whether a particular valid export request delays deletion execution remain routed to the existing legal/privacy/operations gates.

Platform-controlled export artefacts/capabilities are themselves deletion/expiry targets. A database status of deleted is insufficient while a live delivery capability still works.

A lawfully downloaded participant-held copy may remain outside platform control. That copy does not restore account, Entitlements, Plan/report access, health authority or identity relationship.

### Concurrency / restore

Concurrent owner-record changes require deterministic as-of/inclusion semantics; worker timing may not accidentally decide authoritative export scope.

After backup restore:

```text
replay current deletion/suppression truth
→ reapply export expiry/deletion truth
→ revoke resurrected delivery capability
→ prevent deleted identity/entitlement resurrection
```

### Money lifecycle composition

Business and data lifecycle remain separate. An accrued/committed valid refund obligation survives Full Deletion through minimum restricted Commerce evidence without reconstructing account, Plan, health record or entitlement.

```text
remedy qualification
!= refund request
!= refund commitment
!= provider settlement
!= terminal net financial outcome
```

At irreversible deletion execution, a still-valid accrued elective remedy whose retain-the-Plan branch is being destroyed converts into a durable Commerce refund obligation before entitlement destruction.

**Durable refund commitment before entitlement destruction does not mean external provider settlement is required before deletion completion.** Once the obligation is durably preserved, the entitlement irreversibly closed and other deletion requirements pass, Privacy may complete deletion; Commerce continues provider reconciliation afterward.

Provider failure never resurrects the deleted account/right. Chargeback, reversal and refund reconcile to one authoritative net customer-money result.

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

Graceful degradation may use read-only, limited-capability or maintenance modes. Never guess payment, entitlement, health or Safety truth. New admissions may be stopped more narrowly than obligations already owed to existing participants. Safety containment must not depend on a non-authoritative dashboard/Analytics feed being healthy.

Capability-specific degradation behaviour belongs to JIT/proof, but the implementation must preserve owner truth, fail closed for protected consequential actions when required evidence/authority cannot be established, and keep incident/work state distinct from the underlying Domain lifecycle. Operator recovery never bypasses owner authority. Historical incidents remain evidence after remediation; correction does not rewrite incident history.

## 17. Operational measurement and evidence boundaries

Analytics may measure support contact burden, manual intervention, release/pilot metrics, refunds/incidents and progression evidence. Analytics does not authorise admission, refund, entitlement, Safety or release progression. Audit preserves selected governed evidence but does not authorise release merely by containing a record.

Measurement definitions are prospective contracts. They must not retroactively rewrite historical business truth, silently change denominators, or turn read/open/provider telemetry into Product authority. Pilot progression counts real participants, not orders, attempts, collections or dashboard rows.

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

Downstream JIT/proof may choose exact Resource/table names, Ash actions, Ecto schemas, transactions, database constraints/locks/indexes, reservation expiry mechanics, Oban jobs, queue structures, operator UI composition, support-case representation, duplicate-account algorithms, provider refund APIs, exact retention fields/durations, degradation runbooks and metric event schemas.

Acceleration/state mechanisms such as Redis, ETS, Cachex or GenServers are **not** free JIT choices merely because they are technically available. Current evidence does not justify them for the first-pilot admission ceiling. If future evidence justifies an accelerator/service, Architecture Law still requires durable PostgreSQL/owner authority, restart-safe reconstruction, and no competing business truth.

JIT may not redefine Product money/refund/entitlement/Safety/deletion semantics, choose a missing Product rule, create shared-write ownership, turn projections/providers/work queues into authority, weaken historical/immutable evidence, or invent the missing formal authority promotions.

## 20. Closure / freeze rule

This v0.1.1 contract is the **frozen working semantic baseline** for the Operations / Support / first-paid-pilot Pre-JIT stream.

Do not create `OPS-PT-471`, `OPS-UPD-008` or another broad Operations Pre-JIT pass merely because packaging, cross-references, repository installation, provider mechanics or implementation representation remain unresolved.

Reopen substantive semantics only for:
- new contradictory evidence;
- changed Product scope;
- higher-authority amendment/drift;
- provider/expert evidence that falsifies a working assumption; or
- a genuine JIT-discovered semantic contradiction that cannot be resolved within existing authority.

Formal Product/Decision promotion, JIT, proof and release-readiness work remain downstream and do not unfreeze broad discovery by themselves.
