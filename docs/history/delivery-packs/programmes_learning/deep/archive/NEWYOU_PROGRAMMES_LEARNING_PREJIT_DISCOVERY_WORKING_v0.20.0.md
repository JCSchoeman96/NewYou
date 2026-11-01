# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.20.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.20.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 19 - cancellation / transfer semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.19.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose:** append one focused cancellation/transfer pass while preserving Passes 1-18 and their accepted working-lock boundaries.

> This is an append-only semantic successor. It does not override Product, Architecture, Domain, Roadmap, current Open Work or approved Feature Pack/JIT authority.

> Event-ticket cancellation/transfer policy is not generic Programme law. Where Product Law is silent for committed Programme Editions, this ledger records the gap rather than inventing a remedy.

---

# 151. Accepted working-lock status entering Pass 19

The user explicitly accepted Pass 18 and instructed the stream to continue with the next pass.

Therefore Passes 1-18 are now:

`WORKING_LOCKED / NON-AUTHORITATIVE`

Pass 19 inherits without reopening the accepted owner, provenance, correction and concurrency conclusions. In particular, `PRG-GAP-003` / `PRG-UPD-001` remain the existing exceptional Edition/Cohort lifecycle seam; Pass 18 mechanics may make an approved transition safe but may not author missing Product policy.

---

# 152. Pass 19 - cancellation / transfer semantics

## 152.1 Scope hard stop

This pass asks only:

1. what organiser Edition cancellation, postponement/reschedule and participant transfer would mean;
2. how those meanings differ from participant abandonment, Safety restriction, Event cancellation, refund, access revocation, Community closure and communication suppression;
3. which Domain owns each consequence;
4. what historical participation must survive; and
5. whether current authority is sufficient to permit the exceptional action.

It does **not** choose refund/credit amounts, notice windows, participant acceptance UX, Ash state names/actions, provider APIs, permissions matrices, retry settings, migration mechanics or a generic cancellation engine.

## 152.2 Authority finding

Current Product Law is precise for **Events**: DEC-193/DEC-194 define ticket transfer/cancellation/refund/credit/postponement/force-majeure semantics.

Current Product Law is **not equivalently precise for scheduled Programme Editions**. DEC-198...DEC-219 define cohort delivery, schedule, purchaser/participant separation, Edition creation, late enrolment, completion, communications and repeat history, but do not define the organiser's contractual rights/remedies after a participant or commercial commitment when an Edition is postponed, cancelled before start or terminated mid-run.

Therefore Event policy cannot be imported by analogy. `PRG-GAP-003` remains a real upstream Product-authority gap.

---

# 153. Pass-19 evidence register extension

| ID | Evidence |
|---|---|
| PRG-EV-301 | Live README/authority manifest still route current Product, Decision, Architecture, Domain, Roadmap and Open Work authority to the same v1.3.0/v1.6.0/v1.1.1/v1.2.0/v1.2.59 baseline. |
| PRG-EV-302 | DEC-198 makes scheduled cohorts the flagship Nuwe Jy delivery mode; later evergreen is separate. |
| PRG-EV-303 | DEC-199 defines a 60-calendar-day guided rhythm with catch-up/recovery rather than punitive reset or false automatic completion. |
| PRG-EV-304 | DEC-201 binds the 60-day release rhythm to the Edition schedule with timezone-aware, idempotent, observable and recoverable release. |
| PRG-EV-305 | DEC-210 keeps purchaser, intended recipient, redeemed participant and Enrolment separate; purchaser status does not confer participant-journey authority. |
| PRG-EV-306 | DEC-211 requires each Edition to be created from an approved ProgrammeVersion and validates schedules, sessions, safety, facilitation, products, community and communications before activation. |
| PRG-EV-307 | DEC-212 makes late-enrolment policy Edition-specific while keeping participants on the shared cohort schedule. |
| PRG-EV-308 | DEC-217 owns compassionate versioned completion/certificate outcomes; cancellation is not stated as automatic completion or certification. |
| PRG-EV-309 | DEC-218 requires deduplicated Edition communications/operations but does not make Communications the author of Edition lifecycle truth. |
| PRG-EV-310 | DEC-219 requires repeat-enrolment history preservation, supporting non-destructive attempt/lifecycle provenance. |
| PRG-EV-311 | Programmes & Challenges Domain Law owns programme lifecycle, Edition/Cohort schedule, Enrolment lifecycle, completion outcome and repeat-enrolment history. |
| PRG-EV-312 | Programmes Domain Law does not own payment/refund, entitlement, community moderation, live registration/tickets or central safety truth. |
| PRG-EV-313 | Commerce Domain Law owns payment/refund/credit/dispute and commercial contract cancellation; it does not own the participant Programme journey. |
| PRG-EV-314 | Entitlements Domain Law owns access grant/revocation/expiry; payment or Programme lifecycle does not directly become entitlement truth. |
| PRG-EV-315 | Events & Live owns Event policy, occurrence/ticket transfer/cancellation and attendance, while Commerce separately owns refund authority. |
| PRG-EV-316 | DEC-193/DEC-194 explicitly define Event transfer/cancellation/refund/credit/postponement/force-majeure semantics, proving that those semantics are product-specific rather than a generic platform lifecycle. |
| PRG-EV-317 | Communications owns change-message intent/delivery and deduplication; the originating Edition/Event/Commerce business fact remains with its source owner. |
| PRG-EV-318 | Roadmap FP-008 requires a real scheduled Nuwe Jy Edition and names activation gates, but contains no approved Edition cancellation/postponement/termination contract. |
| PRG-EV-319 | Current Open Work names OQ-019/OQ-024/OQ-025/OQ-026/OQ-027/OQ-028 and inherited gates for Nuwe Jy, but no dedicated Programme Edition cancellation/postponement policy gate. |
| PRG-EV-320 | Existing PRG-GAP-003 already identifies the exceptional Edition/Cohort lifecycle seam as missing Product authority. |
| PRG-EV-321 | Existing PRG-UPD-001 already narrows the missing contract to committed pre-start cancellation, committed postponement/reschedule and mid-run cancellation/termination. |
| PRG-EV-322 | Pass-4 PT-093/PT-094/PT-095 already rejected inventing sold/enrolled Edition postponement or cancellation downstream. |
| PRG-EV-323 | Pass-4 PT-096/PT-097/PT-099 already defer participant Cohort/Edition transfer and Cohort merge as YAGNI absent a concrete requirement. |
| PRG-EV-324 | Pass 18 established that idempotency/retry/reordering mechanics can make an approved lifecycle transition safe but cannot decide whether that transition is allowed or what remedy it carries. |
| PRG-EV-325 | No current Product Law clause authorises generic transfer of an enrolled participant journey or specifies refund/credit/access/completion remedies for organiser cancellation of a scheduled Programme Edition. |

---

# 154. Pass-19 semantic model

- **Programme lifecycle truth:** Programmes owns Edition/Cohort/Enrolment state and history.
- **Commercial remedy truth:** Commerce owns refund/credit/payment consequences.
- **Access truth:** Entitlements owns current entitlement validity/revocation.
- **Event truth:** Events & Live owns linked occurrence/ticket cancellation and transfer.
- **Community truth:** Community owns participation/space consequences.
- **Communication truth:** Communications owns change-message intent/delivery/suppression.
- **Safety truth:** Safety owns participant restriction/withdrawal reason and authority.
- **Historical truth:** cancellation/postponement never silently deletes prior schedule, progress, evidence, completion or source provenance.

The seam is intentionally asymmetric:
- pre-commit schedule edits may be ordinary Programme configuration;
- post-commit exceptional changes require Product policy;
- execution safety is already covered by Pass 18 but cannot substitute for that policy.

---

# 155. Pass-19 pressure tests

| ID | Test | Disposition |
|---|---|---|
| PRG-PT-767 | Internal Edition start date corrected before sale, redemption, enrolment or participant commitment | PASS / ORDINARY PROGRAMME EDIT |
| PRG-PT-768 | Sold/enrolled Edition is postponed two weeks before start | BLOCKED / PRG-GAP-003 |
| PRG-PT-769 | Sold/enrolled Edition is cancelled before start | BLOCKED / PRG-GAP-003 |
| PRG-PT-770 | Active Edition is terminated on Day 12 | BLOCKED / PRG-GAP-003 |
| PRG-PT-771 | Organiser postpones a committed Edition and automatically moves every participant to new dates | REJECT / PRODUCT POLICY MISSING |
| PRG-PT-772 | Organiser cancels a committed Edition and automatically refunds every purchase | REJECT / COMMERCE REMEDY NOT INFERABLE |
| PRG-PT-773 | Organiser cancels a committed Edition and automatically issues future credit | REJECT / COMMERCE REMEDY NOT INFERABLE |
| PRG-PT-774 | Organiser cancellation automatically revokes every related entitlement immediately | REJECT / ENTITLEMENT CONSEQUENCE NOT INFERABLE |
| PRG-PT-775 | Organiser cancellation automatically preserves all paid access forever | REJECT / ENTITLEMENT CONSEQUENCE NOT INFERABLE |
| PRG-PT-776 | Committed Edition reschedule proceeds with no participant remedy/choice because dates are 'operational' | REJECT / PRODUCT POLICY MISSING |
| PRG-PT-777 | Participant explicitly accepts a proposed reschedule | INSUFFICIENT TO DEFINE POLICY / PRODUCT CONTRACT STILL REQUIRED |
| PRG-PT-778 | Edition postponement erases already-recorded progress and evidence | REJECT |
| PRG-PT-779 | Edition cancellation marks all Enrolments abandoned | REJECT |
| PRG-PT-780 | Edition cancellation marks all Enrolments completed | REJECT |
| PRG-PT-781 | Edition cancellation issues certificates to all participants | REJECT |
| PRG-PT-782 | Mid-run cancellation converts every remaining required activity to exempt | REJECT / REQUIREMENT SEMANTICS NOT IMPLIED |
| PRG-PT-783 | Cancelled Edition/Cohort row/history is deleted | REJECT / PRESERVE HISTORY |
| PRG-PT-784 | Committed Edition is silently reused with materially different dates/terms as though nothing changed | REJECT / PRESERVE COMMITMENT PROVENANCE |
| PRG-PT-785 | Timezone/schedule change after commitment materially moves release instants | BLOCKED AS COMMITTED-SCHEDULE CHANGE / PRG-GAP-003 |
| PRG-PT-786 | Same schedule change occurs before any participant/commercial commitment | PASS / ORDINARY EDIT IF OTHER ACTIVATION RULES HOLD |
| PRG-PT-787 | Edition is postponed after purchase but before redemption/enrolment | BLOCKED / COMMERCIAL COMMITMENT STILL EXISTS |
| PRG-PT-788 | One linked live session is cancelled while Edition otherwise continues | PASS / EVENT TRUTH ONLY; PROGRAMME CONSEQUENCE SEPARATE |
| PRG-PT-789 | All live sessions fail because provider is unavailable | DOES NOT BY ITSELF CANCEL EDITION |
| PRG-PT-790 | Cohort Facebook/community operation is unavailable | DOES NOT BY ITSELF CANCEL EDITION |
| PRG-PT-791 | Communications provider outage prevents reminders | DOES NOT BY ITSELF CANCEL EDITION |
| PRG-PT-792 | Required Content is withdrawn mid-Edition | ROUTE PRG-GAP-011 / NOT ORGANISER CANCELLATION |
| PRG-PT-793 | One participant becomes Safety-restricted mid-Edition | SAFETY/PARTICIPANT OUTCOME; NOT EDITION CANCELLATION |
| PRG-PT-794 | One participant loses entitlement mid-Edition | ACCESS CONSEQUENCE; NOT EDITION CANCELLATION |
| PRG-PT-795 | Participant voluntarily abandons an active Enrolment | PASS / ENROLMENT OUTCOME; NOT ORGANISER CANCELLATION |
| PRG-PT-796 | Participant requests a refund and also stops participation | COMMERCE REFUND + PROGRAMME ENROLMENT SEMANTICS REMAIN SEPARATE |
| PRG-PT-797 | Refund succeeds and Programme history is deleted | REJECT |
| PRG-PT-798 | Edition cancellation is used as a proxy for full participant data deletion | REJECT / PRIVACY LIFECYCLE SEPARATE |
| PRG-PT-799 | Participant full deletion occurs while Edition is cancelled/postponed | PRIVACY LIFECYCLE REMAINS SEPARATE |
| PRG-PT-800 | Membership cancellation occurs while participant has a Nuwe Jy Enrolment | ACCESS/COMMERCIAL CONSEQUENCES DO NOT EQUAL EDITION CANCELLATION |
| PRG-PT-801 | Support moves a redeemed participant to another Cohort because it is operationally easier | REJECT / TRANSFER NOT AUTHORISED |
| PRG-PT-802 | Participant is moved between Cohorts of the same Edition for load balancing | DEFER_YAGNI / REQUIRE EXPLICIT PRODUCT NEED |
| PRG-PT-803 | Participant is moved to another Edition using the same ProgrammeVersion | DEFER_YAGNI / REQUIRE EXPLICIT PRODUCT NEED |
| PRG-PT-804 | Participant is moved to an Edition using a different ProgrammeVersion | REJECT AS SIMPLE TRANSFER / WOULD NEED GOVERNED MIGRATION OR NEW ENROLMENT CONTRACT |
| PRG-PT-805 | Purchaser transfers a redeemed participant's Programme journey to someone else | REJECT / DEC-210 SEPARATION |
| PRG-PT-806 | Two Cohorts are merged after activation | DEFER_YAGNI |
| PRG-PT-807 | A make-up Cohort is created automatically after Edition cancellation | DEFER_YAGNI / PRODUCT POLICY REQUIRED IF INTRODUCED |
| PRG-PT-808 | Edition cancellation leaves linked future Event occurrences active without reconciliation | REJECT STALE CONSEQUENCE; EVENTS OWNER MUST RECEIVE GOVERNED CONSEQUENCE IF POLICY REQUIRES |
| PRG-PT-809 | Edition cancellation directly deletes/cancels Event records from Programmes persistence | REJECT / CROSS-DOMAIN WRITE |
| PRG-PT-810 | Edition cancellation leaves stale future Programme reminders sending | REJECT / COMMUNICATIONS MUST RECONCILE AUTHORITATIVE CHANGE |
| PRG-PT-811 | Reschedule communication is sent before Programme lifecycle transition is authoritative | REJECT / MESSAGE CANNOT AUTHOR SOURCE TRUTH |
| PRG-PT-812 | Programme cancellation commits but Commerce refund is provider-ambiguous | PASS AS PARTIAL CROSS-DOMAIN STATE / COMMERCE RECONCILES; NO PAYMENT FICTION |
| PRG-PT-813 | Commerce refund completes but downstream Programme consequence temporarily fails | PASS AS RECOVERABLE PARTIAL CONSEQUENCE / NO SHARED-WRITE ROLLBACK |
| PRG-PT-814 | Duplicate organiser-cancellation command is submitted after policy is eventually approved | PASS 18 IDEMPOTENCY APPLIES; POLICY STILL DEFINES EFFECT |
| PRG-PT-815 | Cancel and reschedule commands race | OWNER LIFECYCLE GUARD + JIT CONCURRENCY; PRODUCT LAW MUST DEFINE ALLOWED TRANSITIONS |
| PRG-PT-816 | Edition is archived after normal completion and later operator tries to 'cancel' history | REJECT / GOVERNED CORRECTION ONLY; HISTORICAL COMPLETION PRESERVED |

---

# 156. Pass-19 gap / upstream-delta adjudication

## PRG-GAP-003

**Status remains:** `CONFIRMED / PRODUCT AUTHORITY GAP / IMPLEMENTATION BLOCKED`.

The missing semantics remain narrowly:

1. organiser cancellation of a committed scheduled Edition before start;
2. organiser postponement/reschedule after participant/commercial commitment;
3. organiser cancellation/termination after Edition start.

The gap now explicitly includes the **owner-boundary remedy questions that Product Law must answer or delegate**, such as:
- participant right/choice after a committed schedule materially changes;
- refund, credit or other commercial remedy eligibility;
- continued or ended Programme/Entitlement access;
- partial/mid-run treatment;
- effect on completion/certificate outcomes;
- treatment of linked future Events/Community/Communications; and
- whether a materially rescheduled delivery remains the same Edition or requires an explicit successor/migration construct.

This working ledger does not answer those questions.

## PRG-UPD-001

**Status remains:** `CONFIRMED / NARROWED / NON-AUTHORITATIVE`.

Smallest safe upstream promotion remains an explicit Product Law amendment for the three exceptional scheduled-Edition cases above plus participant-remedy/owner-boundary semantics. If promoted, current Roadmap/FP-008 planning must then explicitly consume/classify the new authority.

No governed DEC/OQ/FP identifier is invented here.

## Transfer adjudication

Generic participant transfer is **not** added to PRG-UPD-001.

- same-Edition Cohort movement;
- cross-Edition movement;
- cross-ProgrammeVersion movement/migration;
- Cohort merge/split; and
- make-up Cohorts

remain `DEFER_YAGNI` unless a concrete Product/operations requirement appears.

No new `PRG-GAP` or `PRG-UPD` is justified.

---

# 157. Pass-19 refinements

| ID | Refinement |
|---|---|
| PRG-REF-245 | Separate organiser Edition cancellation from participant Enrolment abandonment. |
| PRG-REF-246 | Separate committed Edition postponement/reschedule from ordinary pre-commit schedule editing. |
| PRG-REF-247 | Separate Programme cancellation truth from Commerce refund/credit truth. |
| PRG-REF-248 | Separate Programme cancellation truth from Entitlement revocation/persistence truth. |
| PRG-REF-249 | Separate Edition cancellation from linked Event occurrence/session cancellation. |
| PRG-REF-250 | Separate Edition cancellation from Community availability/closure and Communications suppression. |
| PRG-REF-251 | Cancellation never deletes or rewrites historical participation/progress/evidence by default. |
| PRG-REF-252 | Cancellation does not manufacture completed/participated/abandoned/exempt/certified outcomes. |
| PRG-REF-253 | Participant/commercial commitment is the boundary after which schedule change cannot be treated as an ordinary operational edit. |
| PRG-REF-254 | Cancellation reason source and Programme lifecycle transition owner remain distinct; Safety/Content/Event/provider failure may motivate but does not itself author Edition cancellation. |
| PRG-REF-255 | Refund, credit, choice, notice, continued access and mid-run remedy semantics must come from Product/commercial authority, not implementation convenience. |
| PRG-REF-256 | A reschedule must preserve the previous committed schedule/decision provenance rather than silently rewrite historical terms. |
| PRG-REF-257 | Programme participant transfer is not inferred from Event ticket transfer law. |
| PRG-REF-258 | Same-Edition Cohort move, cross-Edition move and cross-ProgrammeVersion migration are distinct possible operations, not one generic transfer. |
| PRG-REF-259 | Purchaser cannot transfer a redeemed participant journey merely because purchaser funded it. |
| PRG-REF-260 | Cohort merge/split/make-up Cohort remains DEFER_YAGNI until a real Product/operations requirement exists. |
| PRG-REF-261 | Pass-18 idempotency/retry semantics apply only after an authoritative cancellation/reschedule transition and consequence contract exists. |
| PRG-REF-262 | Cross-domain cancellation consequences are owner-mediated and independently recoverable; no global rollback owner is introduced. |
| PRG-REF-263 | PRG-GAP-003 remains a Product-authority gap and must not be reclassified as an implementation/JIT detail. |
| PRG-REF-264 | PRG-UPD-001 remains the smallest upstream delta: committed pre-start cancellation, committed postponement/reschedule and mid-run cancellation/termination plus participant remedy boundaries. |
| PRG-REF-265 | If Product Law promotes the exceptional lifecycle, FP-008 planning/gate classification must explicitly consume it rather than silently treating current OQ lists as sufficient. |
| PRG-REF-266 | No generic cancellation/transfer engine, cross-domain saga service or shared lifecycle Domain is justified. |

---

# 158. Pass-19 anti-cancellation-engine / YAGNI outcome

Rejected / deferred:

- generic Programme transfer capability;
- participant drag-and-drop between Cohorts;
- automatic cross-Edition migration;
- automatic cross-ProgrammeVersion migration;
- Cohort merge engine;
- Cohort split engine;
- automatic make-up Cohort;
- global cancellation engine shared by Programmes/Events/Commerce;
- generic refund-from-Programme action;
- generic entitlement-rewrite-from-Programme action;
- destructive cancellation that deletes historical participation;
- automatic certificate/completion award on organiser cancellation;
- automatic participant abandonment on organiser cancellation;
- purchaser-controlled transfer of a redeemed participant journey;
- reusing Event DEC-194 as Programme Edition law;
- hard-coded refund/credit/no-refund policy downstream;
- generic force-majeure workflow engine;
- cross-domain distributed transaction for cancellation;
- new Cancellation/Transfer Domain;
- Cancellation/Transfer Feature Pack;

The simplest correct model remains:

`approved Programme lifecycle transition → durable owner truth → owner-mediated cross-domain consequences → repeat-safe reconciliation`

with no exceptional transition implemented until Product policy authorises it.

---

# 159. Pass-19 disposition

**Discovery outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

**Implementation status for committed Edition cancellation/postponement/termination: BLOCKED / STOP pending Product authority.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Passes 1–18 remain accepted/working-locked and Pass 19 does not reopen them.
2. Programmes owns Edition/Cohort/Enrolment lifecycle truth; organiser Edition cancellation/postponement cannot be authored by Commerce, Events, Communications, Entitlements or an operator UI.
3. Participant Enrolment abandonment, organiser Edition cancellation and participant Safety withdrawal are distinct lifecycle meanings.
4. Commerce owns refund/credit/payment consequences; Programme cancellation does not itself establish a refund or credit.
5. Entitlements owns current access/revocation; Programme cancellation does not itself define when access ends or persists.
6. Events & Live owns linked Event/session occurrence/ticket cancellation. Event cancellation does not equal Edition cancellation, and DEC-194 does not author Programme transfer/cancellation law.
7. Communications owns change-notice intent/delivery and stale-send suppression; message delivery cannot author the Edition lifecycle transition.
8. Community closure/availability is a separate owner consequence and cannot silently become Edition cancellation truth.
9. Ordinary pre-commit schedule correction may remain a Programme edit; after participant/commercial commitment, a material schedule change is an exceptional lifecycle decision requiring approved Product semantics.
10. Current Product Law does not define the participant/commercial contract for committed Edition postponement/reschedule, pre-start organiser cancellation or mid-run organiser termination.
11. Current authority therefore does not permit this Pre-JIT stream to choose refund-versus-credit, continued-access, notice/acceptance/right-to-exit, partial remedy or completion/certificate consequences.
12. Historical Edition/Cohort/Enrolment/progress/evidence remains preserved through exceptional lifecycle changes; cancellation is not deletion.
13. Organiser cancellation does not automatically mark participants completed, participated, abandoned, exempt or failed and does not automatically issue/revoke certificates.
14. A reason originating in Safety, Content, Events, provider operations or force majeure may motivate a Programme lifecycle decision but does not transfer cancellation authority to that source Domain.
15. PRG-GAP-003 remains CONFIRMED / PRODUCT AUTHORITY GAP and blocks implementation/sale of the missing exceptional Edition actions until upstream Product Law is approved.
16. PRG-UPD-001 remains CONFIRMED / NARROWED and is sharpened—not expanded—to the three exceptional cases plus their cross-owner participant-remedy boundaries.
17. Programme participant transfer remains DEFER_YAGNI; Event ticket transfer law must not be reused as authority for Enrolment transfer.
18. If transfer is later required, same-Edition Cohort move, cross-Edition move and cross-ProgrammeVersion migration/new-attempt semantics must be governed separately with preserved provenance.
19. Purchaser status never authorises transfer of a redeemed participant’s private Programme journey.
20. Cohort merge/split/make-up-Cohort capability remains DEFER_YAGNI.
21. Once an upstream cancellation/reschedule contract exists, Pass-18 idempotency/concurrency rules govern duplicate/racing execution; those mechanics cannot choose the business policy.
22. Cross-domain consequences after an authorised exceptional transition reconcile through each owner; partial success does not justify shared-write rollback.
23. No new Product/Architecture/Domain gap identifier is needed: the existing PRG-GAP-003 / PRG-UPD-001 pair accurately contains the missing authority.
24. The smallest safe upstream action is an explicit Product Law amendment defining committed scheduled-Programme exceptional lifecycle and participant remedy semantics; no governed DEC identifier is invented here.
25. After Product promotion, Roadmap/FP-008 planning must explicitly consume/classify that authority before implementing sellable cancellation/reschedule actions.
26. No generic cancellation/transfer engine, global saga service, shared lifecycle store or new Domain/Feature Pack is justified.
27. Pass 19 discovery can pass while the exceptional Edition implementation seam remains BLOCKED / STOP at Product authority.
28. Exact state names, Ash actions, permissions, optimistic locking, jobs, idempotency keys and provider/refund mechanics remain downstream JIT/proof after Product policy exists.
29. No main/authority mutation is authorised by this pass.
30. Broad discovery remains unfrozen; historical reproducibility/replay-provenance is the next isolated pass.

**Pass hard stop:** Pass 20 - historical reproducibility / replay-provenance semantics - has not started.

**Broad discovery remains unfrozen.**
