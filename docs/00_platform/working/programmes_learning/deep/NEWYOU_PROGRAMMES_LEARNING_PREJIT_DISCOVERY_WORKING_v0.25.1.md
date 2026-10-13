# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.25.1

- **Status:** WORKING / NON-AUTHORITATIVE / CORRECTIVE FREEZE CANDIDATE
- **Version:** v0.25.1
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 24 corrective successor — lifecycle authority precision
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch entry head:** `89b68bc38ff0dcb4a5a2ced1de28409851b90527`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.25.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose:** correct lifecycle-policy overreach found in the committed v0.25.0 Pass-24 candidate while preserving its valid Product-routing corrections.

> This is an append-only corrective successor inside **Pass 24**, not a new broad discovery pass and not “Pass 25”.

> v0.25.0 remains historical working provenance. Its Product-first routing for `PRG-GAP-002`, `PRG-GAP-011` and the Edition-centred `PRG-UPD-001` is preserved. Its unsupported Enrolment terminality/ordering conclusions are superseded by this file.

---

# 207. Why v0.25.1 is required

A fresh exact-authority review of committed v0.25.0 found that the candidate fixed the original two review blockers in the right direction but then crossed the same authority boundary in several lifecycle cells.

The specific overreach was material:

1. v0.25.0 declared `completed` and `abandoned` to be normal same-attempt terminal outcomes;
2. it treated completion while paused as requiring resume/current participation first;
3. it treated concurrent completion/abandonment and pause/completion as first-valid-commit conflicts rather than leaving unresolved business ordering at Product;
4. it implied restart is specifically from completed/abandoned history; and
5. it gave more exact generic schedule/resume transition semantics than current Product Law actually defines.

Current authority permits lifecycle verbs and fixes several invariants, but it does **not** universally define those ordering/terminality semantics. Therefore those cells must fail closed as:

`NOT AUTHORISED / PRODUCT DECISION REQUIRED`

This successor does not weaken concurrency correctness. Architecture still requires authoritative current-state validation, idempotency where applicable and invariant-safe persistence. It simply prevents technical commit order, locking strategy or JIT representation from becoming accidental Product policy.

---

# 208. Fresh authority recheck

Current live routing remains:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `00_PLATFORM_v1.6.0.md`
- `01_DECISIONS_v1.6.0.md`
- `02_OPEN_WORK_v1.2.59.md`
- `03_ARCHITECTURE_v1.1.1.md`
- `04_DOMAIN_MAP_v1.2.0.md`
- `05_ROADMAP_v1.2.0.md`
- `PLATFORM_OPERATING_MODEL_v1.0.1.md`
- `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` only where frontend experience is material.

Working Programmes ledgers remain derived/non-authoritative and cannot override those sources.

## 208.1 Corrective evidence extension

| ID | Evidence | Finding |
|---|---|---|
| PRG-EV-451 | Product Law §21F.6 authorises Enrolment verbs | A participant may enrol, schedule, begin, pause, resume, complete, abandon and restart. The verb list does not itself define a universal persisted enum, exact from-state graph or terminality. |
| PRG-EV-452 | Product Law fixes attempt-preservation invariants | Every attempt is preserved; restart creates a new linked Enrolment; duplicate simultaneous same-ProgrammeVersion Enrolments are prevented unless explicitly allowed; restart must not silently consume a new paid entitlement. |
| PRG-EV-453 | Product Law §21F.9 / DEC-155 defines completion criteria/outcomes | Completion is versioned and compassionate; outcome vocabulary is not automatically an Enrolment lifecycle-state machine. |
| PRG-EV-454 | Current Product Law does not define universal completion/abandonment terminality | No current clause states that every `completed` or `abandoned` outcome can never later participate in an approved correction, continuation or other Product-defined consequence. Universal terminality must not be inferred. |
| PRG-EV-455 | Current Product Law does not define pause-versus-complete legality | The generic law does not say whether a paused attempt may complete, must first resume, or how a pause/complete race is resolved. |
| PRG-EV-456 | Current Product Law does not define completion-versus-abandonment precedence | Neither command wins generically. Arrival order, transaction order or lock acquisition must not silently become Product meaning. |
| PRG-EV-457 | Exact generic resume semantics are not fully defined | `resume` is an authorised verb, but generic source-state detail, schedule effect, catch-up consequence and downstream progression meaning are not exhaustively fixed. |
| PRG-EV-458 | Exact self-paced scheduling semantics are not fully defined | `schedule` is an authorised verb, while Nuwe Jy shared scheduling is separately Edition-governed. Generic self-paced scheduling checkpoints must not be invented merely to fill a state graph. |
| PRG-EV-459 | DEC-156 / §21F.10 fix version pinning and migration invariants | Active Enrolments stay pinned unless governed correction/migration/Safety applies; migration requires explicit progress mapping; completed history never changes silently. Same-Enrolment versus successor-Enrolment migration identity remains undefined generically. |
| PRG-EV-460 | DEC-211/212 define Nuwe Jy Edition checkpoints | Edition creation/activation and shared Cohort scheduling are explicit for Nuwe Jy, but no universal Edition/Cohort lifecycle or organiser cancellation/postponement/termination policy is created. |
| PRG-EV-461 | Architecture §7.2 makes concurrency mechanism subordinate to the invariant | Atomic mutation, uniqueness, optimistic checks, row locking and isolation are implementation mechanisms. They may preserve one authoritative truth; they may not answer unresolved business precedence. |
| PRG-EV-462 | Domain Law keeps ownership singular | Programmes & Challenges owns Programme/Version/Edition/Cohort/Enrolment/progression/completion truth; access, Safety, Content, Commerce, Communications and other source truths stay with their owners. |
| PRG-EV-463 | DEC-217 authorises certificates but not post-award invalidation policy | `PRG-GAP-002` remains conditional Product-first where corrected authority undermines an issued award/certificate. |
| PRG-EV-464 | Required Content withdrawal without approved replacement has no participant-remedy rule | `PRG-GAP-011` remains Product-first when triggered; JIT cannot choose substitute/waive/pause/migrate/change-eligibility/withdrawal policy. |
| PRG-EV-465 | `PRG-UPD-001` remains Edition-centred | Committed scheduled Edition cancellation/postponement/termination remains upstream Product work; generic participant transfer/Cohort merge/cancellation engines remain YAGNI. |

---

# 209. Corrected lifecycle handoff contract

## 209.1 Interpretation rule

This matrix records **business semantics and authority status**, not Ash Resource enums, database status values or a generic LMS state machine.

For each cell:

- `AUTHORISED` means current Product authority explicitly permits/fixes the semantic rule;
- `FIXED INVARIANT` means downstream representation may vary but may not violate the stated truth;
- `CONDITIONAL / PROGRAMME-SPECIFIC` means a concrete approved Programme contract must supply the missing policy before the behaviour is implemented; and
- `NOT AUTHORISED / PRODUCT DECISION REQUIRED` means JIT, lock order, UI assumptions, job order and “reasonable defaults” may not choose the business rule.

## 209.2 Enrolment lifecycle matrix

| Lifecycle / condition | Command / trigger | What current authority actually permits or fixes | Durable Programme consequence | Terminality / ordering | Side effects / owner boundary | Authority status |
|---|---|---|---|---|---|---|
| No attempt exists | `enrol` | Create a durable attempt against an approved/selectable ProgrammeVersion when current access/eligibility permits; duplicate simultaneous same-Version Enrolments are prevented unless explicitly allowed | Preserve a distinct version-pinned Enrolment attempt | Not defined as a universal persisted state graph | Entitlements/Safety remain current guards; purchaser truth remains separate | `AUTHORISED` + `FIXED INVARIANTS` |
| Existing attempt where scheduling applies | `schedule` | Product authorises the verb. Concrete delivery mode determines whether/what participant scheduling means. Nuwe Jy shared schedule remains Edition/Cohort governed | Record only the Programme-approved scheduling consequence | Exact generic self-paced scheduling checkpoint/from-state is not fixed | Communications may consume approved schedule truth; participant scheduling cannot rewrite shared Edition truth | `CONDITIONAL`; exact generic self-paced semantics: **NOT AUTHORISED / PRODUCT DECISION REQUIRED** |
| Existing authorised attempt | `begin` | Product authorises beginning participation; current access/Safety/prerequisite authority must still be valid | Record participation start/progression according to the approved Programme contract | Product Law does not require one universal predecessor such as `scheduled` for every delivery mode | Other owners remain guards/evidence sources | `AUTHORISED`; exact generic from-state graph is not frozen |
| Existing participating attempt | `pause` | Product authorises pause and recovery is non-punitive; accepted history/progress must not be silently destroyed | Preserve the same attempt/history with the approved paused participation consequence | Whether pause is legal from every conceivable pre/post checkpoint is not universally specified | Pause does not itself mutate Entitlement, Safety or Edition schedule truth | `AUTHORISED`; exact edge legality remains Programme/Product-specific |
| Paused/interruptible attempt | `resume` | Product authorises resume; current owner guards must be re-evaluated before protected action | Continue the preserved attempt only according to approved Programme semantics | Exact generic resume eligibility, clock/catch-up effect and progression semantics are not fully defined | No stale Entitlement/Safety authority may be fabricated; shared Edition schedule stays owner-governed | `AUTHORISED` verb; unresolved details are **PRODUCT DECISION REQUIRED** when material |
| Completion criteria evaluation | `complete` / governed evaluation | Version-pinned completion rules and approved Programme-specific thresholds/outcome mapping govern the result | Record the Programmes-owned versioned completion/outcome truth | **Whether completion is universally terminal is NOT AUTHORISED. Whether a paused attempt may complete or must resume first is NOT AUTHORISED.** | Certificate/Communications/Analytics consequences remain separately governed | `AUTHORISED` evaluation; terminality/order: **NOT AUTHORISED / PRODUCT DECISION REQUIRED** |
| Existing attempt | `abandon` | Product authorises abandonment as a participant Programme outcome/verb; inactivity or mere time passage must not be silently reinterpreted as an unsupported business transition | Preserve an explicit Programmes-owned abandonment outcome/history where the approved Programme contract applies it | **Universal abandonment terminality and exact legal-from ordering are NOT AUTHORISED** | Does not itself erase evidence or mutate Entitlement/Safety truth | `AUTHORISED` verb/outcome; terminality/order: **NOT AUTHORISED / PRODUCT DECISION REQUIRED** |
| Existing historical/current attempt | `restart` | Restart creates a **new linked Enrolment**; old progress/history is preserved; duplicate simultaneous same-Version Enrolments remain prohibited unless allowed; no silent new paid-entitlement consumption | Create one new linked attempt when the approved Programme/access contract permits restart | Product Law does **not** restrict restart generically to only `completed` or `abandoned` sources; exact permitted source conditions are Programme/Product-specific | Entitlements owns any access/consumption consequence | `AUTHORISED` + `FIXED INVARIANTS`; exact source conditions conditional |
| Active version-pinned attempt | optional ProgrammeVersion migration | Governed migration may occur; explicit progress mapping is mandatory | Apply only an approved migration consequence with provenance | Same-Enrolment mutation versus successor-Enrolment identity is not fixed | Source-owner/version truth remains authoritative | **NOT AUTHORISED / PRODUCT DECISION REQUIRED** for identity shape |
| Attempt affected by Safety authority | Safety migration / withdrawal consequence | Current Safety may require a Programme consequence; Safety owns restriction/reason, Programmes owns Programme consequence | Record approved Programme-side consequence with provenance | Same-attempt later return/reopen after Safety clearance is not fixed generically | No owner boundary transfer | Conditional; reopen semantics: **NOT AUTHORISED / PRODUCT DECISION REQUIRED** |
| Historical/current outcome affected by authoritative correction | correction / reconciliation | DEC-241 permits owner-mediated correction; completed history may not change silently | Preserve before/after provenance through lawful direct or superseding correction | Correction is **not automatically a lifecycle reopen** | Post-award participant consequence routes through `PRG-GAP-002` when triggered | `AUTHORISED` correction mechanism; reopen semantics **NOT AUTHORISED** |
| Edition/Cohort reaches conclusion or another time boundary | scheduled evaluation/checkpoint | Current generic authority does not define one automatic Enrolment transition caused by Edition conclusion | Perform only the evaluation/consequence explicitly authorised by the concrete Programme/Edition contract | Automatic complete/abandon/terminate/reopen is **NOT AUTHORISED** | Communications/Analytics consume owner truth only | **NOT AUTHORISED / PRODUCT DECISION REQUIRED** for any automatic lifecycle effect |

## 209.3 Race / concurrency rule

Architecture fixes **correctness mechanics**, not unresolved Product precedence.

For duplicate/retry/concurrent Enrolment commands:

1. the authoritative Programmes owner must validate current state and applicable current owner guards;
2. duplicate execution of one logical obligation must not multiply the authoritative consequence where idempotency applies;
3. lost updates / blind stale overwrite are prohibited;
4. technical mechanisms may use uniqueness, optimistic concurrency, locking, isolation or another proven PostgreSQL mechanism as appropriate;
5. **lock acquisition, arrival order, transaction commit order or queue order may not be documented as Product precedence unless Product authority actually defines that precedence**; and
6. where two otherwise plausible commands create materially different participant outcomes and current Product Law does not define their ordering, the semantic case is:

`NOT AUTHORISED / PRODUCT DECISION REQUIRED`

Therefore:

- `pause` versus `complete` race: **NOT AUTHORISED / PRODUCT DECISION REQUIRED**;
- `complete` versus `abandon` race: **NOT AUTHORISED / PRODUCT DECISION REQUIRED**;
- “completion always wins”: **NOT AUTHORISED**;
- “abandonment always wins”: **NOT AUTHORISED**; and
- “first commit wins as business policy”: **NOT AUTHORISED**.

JIT may prove an implementation can detect/prevent lost updates; it may not decide the missing participant-semantic winner.

## 209.4 Programme / ProgrammeVersion checkpoints

| Checkpoint | Current-authority handoff | Authority status |
|---|---|---|
| Stable identity | `Programme` is the stable catalogue identity; `ProgrammeVersion` carries versioned participant-semantic configuration | `AUTHORISED` |
| Programme catalogue lifecycle | `draft → internal → pilot → public → paused → retired` belongs to Programme catalogue law | `AUTHORISED`; do not mirror automatically into ProgrammeVersion |
| Material meaning change | Material approved change creates a new ProgrammeVersion | `FIXED INVARIANT` |
| New Enrolment selection | New Enrolments normally use the latest approved ProgrammeVersion, subject to separately approved deliberate pinning | `AUTHORISED NORMAL RULE` |
| Active version pin | Active Enrolments remain on their ProgrammeVersion unless governed correction/migration/Safety applies | `FIXED INVARIANT` |
| Migration | Explicit progress mapping is mandatory | `FIXED INVARIANT`; same-vs-successor Enrolment identity unresolved |
| Safety migration/withdrawal | Safety may force a governed Programme consequence | `AUTHORISED OWNER INTERACTION`; exact return/reopen policy conditional |
| Completed history | Completed history never changes silently; correction/supersession remains explicit | `FIXED INVARIANT`; this does **not** establish universal Enrolment terminality |
| ProgrammeVersion lifecycle enum/retirement mechanics | Current Product Law does not define a universal mirrored Version lifecycle | **NOT AUTHORISED** to invent for symmetry |

## 209.5 Edition / Cohort checkpoints

| Checkpoint | Current-authority handoff | Authority status |
|---|---|---|
| Applicability | Edition/Cohort is delivery-mode-specific; it is not mandatory for evergreen/self-paced Programmes | `AUTHORISED BOUNDARY` |
| Nuwe Jy Edition creation | Create from an approved ProgrammeVersion | `AUTHORISED` |
| Nuwe Jy activation | Validate configured Content/translations/schedule/sessions/Safety/facilitation/products/Community/Communications before activation | `AUTHORISED` for Nuwe Jy; not universalised |
| Shared schedule | Late Enrolments use guided catch-up while remaining on the shared Cohort schedule | `AUTHORISED` |
| Participant pause/resume | Must not silently rewrite Edition-owned shared schedule | `FIXED OWNER BOUNDARY`; exact participant catch-up/resume semantics remain concrete-Programme policy |
| Edition/Cohort conclusion | No generic automatic Enrolment transition is currently authorised | **NOT AUTHORISED / PRODUCT DECISION REQUIRED** if a concrete Product needs one |
| Committed pre-start organiser cancellation | Current Product Law does not define it | **NOT AUTHORISED / PRODUCT DECISION REQUIRED — `PRG-UPD-001`** |
| Material post-commit postponement/reschedule | Current Product Law does not define it | **NOT AUTHORISED / PRODUCT DECISION REQUIRED — `PRG-UPD-001`** |
| Mid-run organiser termination/cancellation | Current Product Law does not define it | **NOT AUTHORISED / PRODUCT DECISION REQUIRED — `PRG-UPD-001`** |
| Generic Edition/Cohort lifecycle enum | No universal enum is defined | **NOT AUTHORISED** to invent |

## 209.6 Completion / correction / content-withdrawal checkpoints

| Trigger | Current-authority consequence | Authority status |
|---|---|---|
| Completion criteria satisfied under the Enrolment's pinned ProgrammeVersion | Programmes records the approved versioned outcome; exact programme thresholds remain under `OQ-019` plus applicable programme-specific authority | `AUTHORISED` framework / Product-gated values |
| Source evidence corrected before any award consequence | Programmes reconciles its own outcome from authoritative current source truth while preserving correction provenance | `AUTHORISED` correction boundary |
| Corrected source truth undermines an already-issued award/certificate | Product must decide participant-facing invalidate/revoke/supersede/reissue/display/notify/review/appeal meaning before implementation | **`PRG-GAP-002 — CONDITIONAL PRODUCT-FIRST`** |
| Required governed Content withdrawn and approved replacement/substitution already exists | Content owns withdrawal/replacement truth; Programmes follows only the already-approved Programme consequence | `OWNER-MEDIATED` |
| Required governed Content withdrawn with no approved replacement/substitution | Product must decide substitute/waive/pause/migrate/change-eligibility/withdraw/other participant consequence | **`PRG-GAP-011 — PRODUCT-FIRST WHEN TRIGGERED`** |
| Lawful deletion removes private source payload/provenance | Privacy/HJP retention authority controls what may lawfully remain; Programmes must not recreate deleted private truth from projections | `FIXED OWNER BOUNDARY` |

---

# 210. Residual Product-authority routing preserved from v0.25.0

## 210.1 `PRG-GAP-002`

`OPEN / CONDITIONAL PRODUCT-FIRST / AWARD-USE BLOCKER WHEN TRIGGERED`

Product authority must define participant-facing policy if corrected authoritative evidence undermines an already-issued completion award/certificate. Programmes may implement only the approved consequence. No certificate invalidation policy is invented here.

## 210.2 `PRG-GAP-011`

`OPEN / PRODUCT-FIRST WHEN TRIGGERED / BLOCKS AFFECTED FP OR RELEASE`

When required governed Content is withdrawn and no approved replacement/substitution exists, Product authority must define the participant Programme consequence before JIT. Content owns withdrawal/replacement truth; Programmes owns its approved participant consequence. `OQ-019` is not authority for this decision.

## 210.3 `PRG-UPD-001`

`PRG-UPD-001 — Committed scheduled Programme Edition exceptional lifecycle contract`

Status:

`CONFIRMED / NARROWED / NON-AUTHORITATIVE / IMPLEMENTATION BLOCKED AT PRODUCT AUTHORITY WHEN APPLICABLE`

The missing Product semantics remain limited to:

1. organiser cancellation of a committed scheduled Edition before start;
2. material postponement/reschedule after participant or commercial commitment;
3. organiser termination/cancellation after Edition start;
4. action guards / commitment boundary;
5. same-Edition material reschedule versus governed successor/migration meaning;
6. participant choice/right-to-exit where applicable;
7. preservation of Enrolment/progress/history;
8. financial-remedy eligibility while Commerce remains financial authority;
9. current-access consequence while Entitlements remains access authority;
10. completion/certificate consequence; and
11. linked owner-mediated Events/Community/Communications consequences.

It does **not** authorise a generic participant-transfer engine, Cohort merge/split policy, generic cancellation engine or generic transfer engine.

## 210.4 Correct upstream-work statement

> `PRG-UPD-001` is the sole currently named `PRG-UPD` identifier. Product-first residual work also exists conditionally under `PRG-GAP-002`, `PRG-GAP-011`, and any lifecycle cell explicitly marked `NOT AUTHORISED / PRODUCT DECISION REQUIRED` when a concrete Feature Pack needs that behaviour.

No new upstream identifier is invented by this corrective successor.

---

# 211. Pressure-test correction extension

v0.25.0 pressure tests remain provenance except where explicitly superseded below.

| ID | Test | Disposition | Correct conclusion |
|---|---|---|---|
| PRG-PT-1067 | v0.25.0 says `completed` is a normal universal same-attempt terminal outcome | REJECT / SUPERSEDED | Current Product Law does not define universal completion terminality. **PRODUCT DECISION REQUIRED** when a concrete behaviour depends on it. |
| PRG-PT-1068 | v0.25.0 says `abandoned` is a normal universal same-attempt terminal outcome | REJECT / SUPERSEDED | Current Product Law does not define universal abandonment terminality. **PRODUCT DECISION REQUIRED** when material. |
| PRG-PT-1069 | Completion submitted while paused | **NOT AUTHORISED / PRODUCT DECISION REQUIRED** | Generic Product Law does not decide “complete while paused” versus “must resume first”. JIT must not choose. |
| PRG-PT-1070 | Completion and abandonment race | **NOT AUTHORISED / PRODUCT DECISION REQUIRED** | No generic precedence, first-commit-wins policy or last-write-wins policy is authorised. Concurrency must preserve correctness without inventing a semantic winner. |
| PRG-PT-1071 | Pause and completion race | **NOT AUTHORISED / PRODUCT DECISION REQUIRED** | No generic winner/order is authorised. |
| PRG-PT-1072 | Exact generic resume behaviour inferred from the verb | REJECT | Revalidation of current owner authority is mandatory for protected action, but precise catch-up/clock/progression consequence remains Programme/Product-specific. |
| PRG-PT-1073 | Generic self-paced `schedule` checkpoint/state invented | REJECT | Product authorises the verb but does not define one universal self-paced scheduling state graph. |
| PRG-PT-1074 | Restart allowed only from completed/abandoned attempts | REJECT AS GENERIC RULE | Restart invariants are explicit; exact source conditions are not universally limited to those two outcomes. |
| PRG-PT-1075 | Edition conclusion automatically completes/abandons/terminates active Enrolments | **NOT AUTHORISED / PRODUCT DECISION REQUIRED** | No generic automatic Edition-end lifecycle consequence exists. |
| PRG-PT-1076 | Technical lock/commit order used as Product transition precedence | REJECT | Architecture mechanism cannot launder unresolved Product meaning. |
| PRG-PT-1077 | Post-award correction policy delegated to JIT | BLOCKED / `PRG-GAP-002` | Product-first when award/certificate invalidation is triggered. |
| PRG-PT-1078 | Required Content withdrawn without replacement and JIT chooses remedy | BLOCKED / `PRG-GAP-011` | Product-first when triggered. |
| PRG-PT-1079 | Committed scheduled Edition cancellation/postponement/termination handled as ordinary JIT lifecycle | BLOCKED / `PRG-UPD-001` | Product authority must define exceptional Edition lifecycle first. |
| PRG-PT-1080 | Corrected lifecycle matrix leaves unsupported legality to “owner guards” | REJECT | Unsupported participant semantics are named explicitly and fail closed at Product. |
| PRG-PT-1081 | Corrected Pass 24 introduces a new Domain/LMS engine/new PRG gap | REJECT / NOT NEEDED | No new owner, generic abstraction or gap identifier is justified. |
| PRG-PT-1082 | Freeze gate after v0.25.1 correction | PASS / FREEZE-READY CANDIDATE | The lifecycle handoff is explicit without inventing terminality/ordering; Product-first residuals are routed correctly. |

---

# 212. Corrective refinements extension

| ID | Refinement | Effect |
|---|---|---|
| PRG-REF-377 | Supersede v0.25.0's universal completion/abandonment terminality claim. | Outcome labels no longer become invented lifecycle law. |
| PRG-REF-378 | Supersede “resume first” as the generic answer to completion-while-paused. | Pause/completion legality fails closed at Product. |
| PRG-REF-379 | Supersede technical first-committer-wins as generic completion/abandonment or pause/completion policy. | Concurrency mechanism cannot choose participant meaning. |
| PRG-REF-380 | Keep restart's explicit new-linked-attempt/history/duplicate/entitlement invariants while leaving exact source conditions Programme/Product-specific. | Preserve law without inventing a transition graph. |
| PRG-REF-381 | Treat exact generic resume and self-paced schedule semantics as unresolved where current authority is silent. | Smaller agents cannot infer a generic LMS state machine. |
| PRG-REF-382 | Mark Edition-conclusion automatic lifecycle effects Product-required instead of asserting a generic no-op transition. | Fail closed on unsupported scheduled-delivery semantics. |
| PRG-REF-383 | Preserve v0.25.0's Product-first routing for `PRG-GAP-002` and `PRG-GAP-011`. | Correct original authority-routing blocker. |
| PRG-REF-384 | Preserve Edition-centred `PRG-UPD-001` scope. | Correct original exceptional-lifecycle routing blocker without generic engines. |
| PRG-REF-385 | Keep lifecycle dimensions independent from access, Safety, Content, Commerce and provider/projection state. | One durable owner per truth. |
| PRG-REF-386 | Use v0.25.1 as the current Pass-24 handoff and retain v0.25.0 as superseded working provenance. | Append-only correction; no silent historical rewrite. |

---

# 213. Pass-24 freeze-gate rerun

The freeze gate is rerun only for the bounded defects reopened by the independent review and the additional v0.25.0 authority-overreach found during exact verification.

## Gate results

| Gate | Result | Reason |
|---|---|---|
| Current live authority freshly verified | PASS | README/manifest route the current v1.3.0 / v1.6.0 / v1.6.0 / v1.2.59 / v1.1.1 / v1.2.0 / v1.2.0 / v1.0.1 authority set. |
| Durable owner ambiguity | PASS | Programmes remains sole owner of Programme/Version/Edition/Cohort/Enrolment/progression/completion truth; no new shared-write model is introduced. |
| Explicit lifecycle handoff | PASS | Verbs, fixed invariants, conditional semantics and unsupported legality are separated explicitly. |
| Unsupported transition legality fails closed | PASS | Universal terminality, pause/complete, complete/abandon precedence, exact resume, exact self-paced schedule, migration identity and Edition-end automatic effect are Product-required where authority is silent. |
| `PRG-GAP-002` authority routing | PASS | Conditional Product-first when issued award/certificate consequence is triggered. |
| `PRG-GAP-011` authority routing | PASS | Product-first when required Content is withdrawn without approved replacement/substitution. |
| `PRG-UPD-001` scope | PASS | Limited to committed scheduled Programme Edition exceptional lifecycle and owner-mediated consequences. |
| Generic LMS/state-machine abstraction | PASS | None added. |
| New Domain / shared-write authority | PASS | None added. |
| Identifier continuity | PASS CANDIDATE | This successor continues evidence from `451`, pressure tests from `1067`, refinements from `377`; it creates no new `PRG-GAP` or `PRG-UPD` ID. Mechanical branch validation must still confirm the committed bytes. |
| Implementation authority | PASS | None created. |

## Verdict

# `PASS`

**Broad Programmes/Learning Pre-JIT disposition:**

`FREEZE-READY / STOP GENERIC PRE-JIT DISCOVERY — CANDIDATE PENDING USER ACCEPTANCE`

This means generic discovery may stop because remaining Product questions are now explicit, bounded and fail closed. It does **not** mean those Product decisions are resolved, and it does not authorise implementation.

If accepted by the user:

```text
PROGRAMMES / LEARNING BROAD PRE-JIT DISCOVERY
=> WORKING_FROZEN / NON-AUTHORITATIVE / HANDOFF-READY

CURRENT PASS-24 FOCUSED HANDOFF
=> v0.25.1

v0.25.0
=> SUPERSEDED WORKING CANDIDATE / PROVENANCE RETAINED

NO DEFAULT BROAD PASS 25

IMPLEMENTATION
=> NOT AUTHORISED
```

---

# 214. Final corrected conclusions

1. Product Law authorises Enrolment verbs but does not define a universal Enrolment enum or complete transition graph.
2. Every Enrolment attempt is preserved; restart creates a new linked attempt; duplicate simultaneous same-Version attempts are prevented unless explicitly allowed; restart does not silently consume paid entitlement.
3. Completion remains versioned and programme-specific; `OQ-019` owns unresolved programme-specific completion metrics, not unrelated lifecycle/remedy policy.
4. `completed` is **not** declared universally terminal by this working handoff.
5. `abandoned` is **not** declared universally terminal by this working handoff.
6. Completion while paused is **NOT AUTHORISED / PRODUCT DECISION REQUIRED** at generic scope; this handoff does not invent “resume first” as Product law.
7. Completion-versus-abandonment and pause-versus-completion precedence are **NOT AUTHORISED / PRODUCT DECISION REQUIRED**; technical ordering does not decide Product meaning.
8. Exact generic resume and self-paced scheduling semantics remain Product/Programme-specific where current authority is silent.
9. Restart's fixed new-linked-attempt/history/duplicate/entitlement invariants remain authoritative without inventing an exhaustive source-state list.
10. Active Enrolments remain pinned to their ProgrammeVersion unless governed correction/migration/Safety applies; migration requires explicit progress mapping.
11. Same-Enrolment versus successor-Enrolment migration identity remains Product-first if a concrete Feature Pack needs it.
12. Correction/supersession preserves provenance and does not automatically reopen the original Enrolment.
13. Programme catalogue lifecycle must not be mirrored automatically into a ProgrammeVersion lifecycle.
14. Edition/Cohort remains delivery-mode-specific and must not become universal Programme structure.
15. Nuwe Jy Edition creation/activation/shared-schedule rules remain explicit and do not create a generic Edition state machine.
16. Edition/Cohort conclusion has no generic automatic Enrolment lifecycle effect; a concrete effect requires Product authority.
17. `PRG-UPD-001` remains the sole named `PRG-UPD` identifier and is correctly limited to committed scheduled Edition cancellation/postponement/termination semantics and consequences.
18. `PRG-GAP-002` is conditional Product-first when corrected authoritative truth undermines an issued award/certificate.
19. `PRG-GAP-011` is Product-first when required Content is withdrawn without an approved replacement/substitution.
20. `PRG-UPD-001` is not the only Product-first residual Programme work.
21. No new `PRG-GAP`, `PRG-UPD`, Domain, Resource family, event store, saga, workflow engine or generic LMS abstraction is justified.
22. Architecture concurrency/idempotency mechanisms preserve correctness but never create missing Product transition precedence.
23. Broad generic Programmes/Learning discovery is freeze-ready only because unsupported semantics are explicit hard stops rather than hidden JIT discretion.
24. There is no default broad Pass 25.
25. Implementation remains unauthorised.

---

# 215. Hard stop

Do not restart broad Programmes/Learning discovery after user acceptance unless a concrete trigger appears:

- higher authority changes a locked conclusion;
- Product resolves or changes a named Product-first seam;
- a Feature Pack/JIT contract exposes a real upstream contradiction;
- proof invalidates a material invariant; or
- the user explicitly reopens scope.

Until then, unsupported lifecycle cells, `PRG-GAP-002`, `PRG-GAP-003` / `PRG-UPD-001`, `PRG-GAP-007`, `PRG-GAP-011` and other named gates remain explicit fail-closed stops when their trigger enters scope.
