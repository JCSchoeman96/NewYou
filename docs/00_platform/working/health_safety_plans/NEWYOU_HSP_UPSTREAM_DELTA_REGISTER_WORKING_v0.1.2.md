# Health / Safety / Plans Upstream Authority Delta Register — Working Consolidation v0.1.2

- **Status:** WORKING / NON-AUTHORITATIVE
- **Source:** `HSP-UPD-001...008` from `HEALTH_SAFETY_PLAN_PREJIT_DISCOVERY_WORKING_v0.42.0.md`
- **Purpose:** Identify what truly requires upstream authority versus what can remain JIT/governance detail.
- **Implementation:** NOT AUTHORISED.
- **v0.1.2 hygiene patch:** Retains the narrowed FP-005 blocker semantics and standardises the canonical `Phase 7C Final Feature Pack Contract` terminology; chat-specific “uploaded” source wording is replaced with durable source-artifact wording.

## Live authority baseline used for this consolidation

Verified against the live `JCSchoeman96/NewYou` default branch at commit:

`c4ed5ce95b151c060c104bbec6b25edefb271814`

Current routed authority:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.39.md`
5. `03_ARCHITECTURE_v1.1.0.md`
6. `04_DOMAIN_MAP_v1.1.0.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.0.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` only when frontend/experience planning is in scope.

The current `v1.3.0` Product amendment and `v1.1.0` Architecture/Domain/Roadmap amendments are additive for Research & Feedback, Voting & Balloting, Interactive Tools and Platform Member Reference. They do not alter the Health → Safety → Plans authority model or FP-004/FP-005 sequencing used here.

The source `HEALTH_SAFETY_PLAN_PREJIT_DISCOVERY_WORKING_v0.42.0.md` remains working evidence only.


## Classification summary

There is **no HSP-UPD blocker before FP-004 JIT**.

For FP-005, the blocker classification below is deliberately **not** a blanket prohibition on beginning all Phase 7B investigation. The live governed sequence is Phase 7A Skeleton + preliminary Gate Manifest → Phase 7B required JIT Domain Dossiers → Phase 7C Final Feature Pack Contract. The two commercial deltas identified here must be resolved before Phase 7C freezes the affected participant/commercial semantics; Phase 7B may investigate and surface their consequences without deciding them.

FP-004 still has its existing Roadmap blockers, notably `OQ-005` and `OQ-008`; they are not HSP-UPD items.

Two HSP deltas are genuine blockers before FP-005 can freeze the affected commercial semantics in its Phase 7C Final Feature Pack Contract:

- `HSP-UPD-005`
- `HSP-UPD-008`

Three belong to later recurring/professional/commercial work:

- `HSP-UPD-001`
- `HSP-UPD-006`
- `HSP-UPD-007`

Three are better treated as non-blocking JIT/governance detail rather than broad upstream Product blockers:

- `HSP-UPD-002`
- `HSP-UPD-003`
- `HSP-UPD-004` (core direction already upstream; category detail remains gated)

No item is fully resolved by current authority at the exact question asked.

## Register

| ID | Issue | Authoritative owner / responsibility | Classification | Current authority status | Required resolution point | Governed amendment? | Recommendation |
|---|---|---|---|---|---|---|---|
| `HSP-UPD-001` | A time-scoped membership Plan/review benefit expires after a Request was validly admitted but before fulfilment. Does admitted work retain a bounded completion right? | Product Law + Entitlements; Commerce where membership contract meaning is affected. | **BLOCKER BEFORE LATER PROFESSIONAL/COMMERCIAL WORK** | **OPEN.** DEC-041 governs what ends after membership, and Entitlements owns validity/expiry, but current law does not settle already-admitted in-flight work. | Before FP-010/FP-011 or any JIT contract that allows membership-derived Plan work to remain in flight across entitlement-period expiry. Also before a later professional review uses that entitlement class. | **Yes**, if the completion right changes the Product entitlement promise. | Preserve the discovery preference only as provenance, not law: a bounded completion right is coherent, but Product/Entitlements must explicitly decide it. Do not pull this into FP-004/FP-005 once-off MVP. |
| `HSP-UPD-002` | A dependency is ordinarily superseded, not withdrawn, while generation is in flight. May admitted work finish on the predecessor, or must it restart on successor? | Content & Media + Plans & Nutrition governance; Product only if participant/commercial promise changes. | **NON-BLOCKING / DEFER TO JIT** | **OPEN at generic policy level.** Current authority clearly distinguishes superseded from withdrawn but does not prescribe one universal in-flight rule. | FP-005 JIT per dependency class, before proof/release for any class where supersession can occur during generation. | **Usually no Product amendment.** Use governed JIT/content policy unless the choice alters promised product behaviour. | Do not invent a platform-wide rule. Define the smallest dependency-specific revalidation policy. Historical provenance remains exact either way. |
| `HSP-UPD-003` | A delivered Plan dependency is withdrawn. What exact affected-Plan consequence applies: correction/replacement, Safety pause, withdrawal, warning, Safety adjudication? | Withdrawal-declaring owner + Plans + Safety according to reason/scope; Content governance where content is the dependency. | **NON-BLOCKING / DEFER TO JIT** | **Partially governed.** Product Law already requires governed corrections/replacements/safety withdrawals and history preservation. Exact affected-delivery mapping is not universal. | Before FP-005 release/correction/withdrawal operations for the relevant dependency class. Roadmap already treats publication/correction operations as release-gated. | **Not normally.** Escalate upstream only if the consequence changes Product rights or clinical policy. | Make withdrawal declarations carry affected-delivery semantics. Plans/UI must not infer severity from “withdrawn” alone. |
| `HSP-UPD-004` | Exact full-deletion treatment for Plan Versions, Generation Input Bases, Plan Result Provenance, Safety adjudications/cases and practitioner-derived variants. | Privacy & Consent orchestration + each owning Domain’s deletion contract; professional/legal authority for formal records. | **NON-BLOCKING / DEFER TO JIT / EXPERT GATES** | **Core direction resolved, category mapping open.** DEC-225/226/229 and Architecture §11 already establish deletion/access/retention separation. OQ-009/OQ-029/OQ-033 and deletion/export gates remain. | Before applicable Privacy/Health/Plans JIT freeze and certainly before pilot/release of affected retained categories. FP-004 Roadmap treats retention as release-only rather than a blocker to all planning. | **Only if expert review changes Product/Domain meaning.** Exact mapping normally belongs to governed Privacy JIT beneath current law. | Do not keep this labelled as a generic Product-policy gap. Preserve “immutable while retained” and specify category-specific delete/anonymise/restrict/retain under the existing retention gates. |
| `HSP-UPD-005` | A paid/consumable Plan Request is validly admitted, but mandatory hard constraints make the current approved Plans capability `unfulfillable`. What customer remedy is owed? | Product + Commerce + Entitlements. Plans supplies the truthful `unfulfillable` outcome but does not choose remedy. | **BLOCKER BEFORE FP-005 FINAL CONTRACT / AFFECTED SEMANTICS FREEZE** | **OPEN.** DEC-109 requires fail-closed generation and entitlement preservation; current authority does not define refund/credit/alternate/retry/expiry remedy for this business outcome. | Before FP-005 Phase 7C Final Feature Pack Contract freezes participant/commercial behaviour. It may be discussed earlier but must not be guessed in implementation. | **Yes.** This is a Product/commercial right. | Resolve minimally: define the permitted customer remedy set and who initiates it. Do not “solve” it by weakening hard constraints, misclassifying Safety or auto-routing to professional review. |
| `HSP-UPD-006` | Required professional review cannot be completed due reviewer/capacity/provider failure. What maximum pending/resolution promise and customer remedy apply? | Product + Professional Care + Commerce + Entitlements; operating policy may own exact internal timers beneath the promise. | **BLOCKER BEFORE LATER PROFESSIONAL/COMMERCIAL WORK** | **OPEN.** Current Roadmap already requires capacity control and expected turnaround for FP-012, but no complete timeout/remedy contract exists. | Before FP-012 or another sold review-gated professional service is frozen/marketed. Also before any recurring product promises human review under a bounded SLA. | **Yes** for customer promise/remedy; **no** for subordinate operational timer mechanics if they remain within the approved promise. | Set saleable capacity before admission, then define bounded pending, reassignment, cancellation and refund/credit/alternate-review semantics. Reviewer loss must not consume another Plan entitlement. |
| `HSP-UPD-007` | Locked DEC-045 says Plan refunds end after generation, while review-gated work may be generated before approved delivery. What counts as qualifying “generation” for refund purposes? | Product + Commerce + Entitlements, informed by Plans/Professional Care workflow. | **BLOCKER BEFORE LATER PROFESSIONAL/COMMERCIAL WORK** | **OPEN/UNDER-SPECIFIED.** DEC-045 says generation; current Platform refund prose says “refundable before generation” and “ordinarily non-refundable once delivered.” The generated-but-not-delivered interval is not explicitly resolved for review-gated cases. | Before a pathway is sold/frozen where generation can materially precede mandatory approval/delivery (not required for the plain automated FP-005 path unless JIT introduces such a gate). | **Yes.** Locked Product refund semantics need clarification/amendment if an exception is intended. | Keep refund boundary separate from Plan fulfilment/Entitlements consumption. Do not let stale worker completion manufacture commercial forfeiture after authoritative cancellation. |
| `HSP-UPD-008` | Participant deliberately changes material Plan intent after paid admission but before first fulfilment, especially after generation began. Does the same unconsumed right fund replacement work? | Product + Commerce + Entitlements. Plans owns basis invalidation/new Request, not pricing/right treatment. | **BLOCKER BEFORE FP-005 FINAL CONTRACT / AFFECTED SEMANTICS FREEZE** | **OPEN.** DEC-038 governs later preference/progress re-personalisation after a valid Plan; it does not settle pre-first-fulfilment change-of-intent. DEC-045 may interact once generation has occurred. | Before FP-005 Phase 7C Final Feature Pack Contract freezes how material in-flight participant input edits are handled. | **Yes.** This is a Product/commercial entitlement rule. | Decide whether the original unconsumed right may be rebound/released to a replacement Request, whether any point incurs a new right/fee, and how DEC-045 applies. Do not mutate the original Generation Basis. |

## Category view

### BLOCKER BEFORE FP-004 JIT

None from `HSP-UPD-001...008`.

Existing Roadmap blockers remain `OQ-005` and `OQ-008`.

### BLOCKER BEFORE FP-005 FINAL CONTRACT / AFFECTED SEMANTICS FREEZE

- `HSP-UPD-005` — customer remedy for `unfulfillable`.
- `HSP-UPD-008` — commercial/entitlement consequence of pre-fulfilment participant change-of-intent.

### BLOCKER BEFORE LATER PROFESSIONAL / COMMERCIAL WORK

- `HSP-UPD-001` — admitted membership-derived work across entitlement expiry.
- `HSP-UPD-006` — required professional-review delay/capacity failure and remedy.
- `HSP-UPD-007` — DEC-045 meaning for generated-but-not-delivered review-gated Plans.

### NON-BLOCKING / DEFER TO JIT

- `HSP-UPD-002` — ordinary supersession in-flight policy, per dependency class.
- `HSP-UPD-003` — affected-delivery mapping for withdrawal, under withdrawal reason/scope.
- `HSP-UPD-004` — category-specific deletion mapping beneath current deletion/retention law and expert gates.

### RESOLVED BY CURRENT AUTHORITY

None fully at the exact issue level.

`HSP-UPD-004` is the closest: its **principle** is already resolved (business lifecycle ≠ data lifecycle; no blanket indefinite retention; full deletion ends product access), but the requested category matrix remains intentionally unresolved.

## Anti-drift conclusion

The discovery artifact’s “UPD” prefix should not be interpreted to mean every item requires Product Law.

The compressed classification removes that ambiguity:

- Product/commercial rights are escalated upstream.
- Domain/content/privacy mechanics remain JIT/governance where current authority already supplies the rule.
- Clinical thresholds remain in the existing OQ gates.
- No new authority layer is created.
