# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.25.0

- **Status:** WORKING / NON-AUTHORITATIVE / CORRECTIVE FREEZE CANDIDATE
- **Version:** v0.25.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 24 — lifecycle + residual Product-authority corrective closure
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch parent:** `3d20bbf2a01fd696b07fabae29e01f78fbbdb204`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.24.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose:** implement the two bounded material corrections identified by the independent brutal review, then rerun only the final broad-discovery freeze gate.

> This is **not** another broad exploratory pass. It reopens only the final handoff conclusions materially affected by independent review.

> The independent reviewer found the underlying architecture substantially sound but rejected freeze because the lifecycle guard contract was too implicit and `PRG-GAP-002` / `PRG-GAP-011` were routed too low. This successor independently rechecks those findings against live authority before changing the working handoff.

---

# 197. Corrective-pass entry state

The user accepted Pass 23, then commissioned an independent brutal review. That review returned `CHANGES REQUIRED`.

The review is new evidence and therefore a valid re-entry trigger under the Pass-23 resume rules. Passes 1–23 remain historical `WORKING_LOCKED / NON-AUTHORITATIVE` evidence, but the Pass-23 freeze-ready conclusion is superseded for current handoff purposes by this corrective successor until Pass 24 is accepted. No prior ledger is rewritten.

---

# 198. Independent-review adjudication

## 198.1 Blocker 1 — lifecycle handoff

**ADJUDICATION: ACCEPTED.**

Current Product Law authorises the lifecycle verbs and several invariants, but the prior cumulative register did not consolidate them into a sufficiently explicit downstream handoff. Statements such as “owner lifecycle guards decide” were safe architecture reasoning but too weak for a final semantic contract consumed by smaller agents.

The correction is **not** to invent a generic state machine. It is to record the minimum authority-backed transition/checkpoint semantics, fixed invariants, normal same-attempt terminal outcomes, conflict/idempotency rules, and every unsupported transition as `NOT AUTHORISED / PRODUCT DECISION REQUIRED`.

## 198.2 Blocker 2 — residual Product routing

**ADJUDICATION: ACCEPTED.**

`PRG-GAP-002` and `PRG-GAP-011` were discovered correctly but routed too permissively. Feature Pack/JIT may implement an approved consequence but may not invent the participant-facing Product consequence.

The previous claim that `PRG-UPD-001` is the only upstream Programme work is corrected to:

> `PRG-UPD-001` is the **only currently named PRG-UPD identifier**, but it is **not the only Product-first residual Programme work**.

No new upstream identifier is created here.

---

# 199. Corrective evidence register extension

| ID | Evidence | Finding |
|---|---|---|
| PRG-EV-426 | Independent brutal review is valid new evidence | Two bounded blockers were identified: lifecycle handoff ambiguity and under-routed Product policy for `PRG-GAP-002/011`. |
| PRG-EV-427 | Live authority and branch state reverified | Before this correction, live `main` remained `086ade7b...`; the Programme branch was `3d20bbf...`, 25 ahead / 0 behind, with only append-only working ledgers. |
| PRG-EV-428 | Product Law names Enrolment lifecycle verbs | §21F.6 permits enrol, schedule, begin, pause, resume, complete, abandon and restart. |
| PRG-EV-429 | Enrolment attempts are durable historical identities | Every attempt is preserved; restart creates a new linked Enrolment rather than deleting old progress. |
| PRG-EV-430 | Duplicate simultaneous attempts are constrained | Same-ProgrammeVersion simultaneous Enrolments are prevented unless explicitly allowed; restart may not silently consume a new paid entitlement. |
| PRG-EV-431 | Pacing/recovery are non-punitive | DEC-151/154 and §21F.5/8 preserve progress, catch-up/rescheduling/simplification and reject ordinary delay as failure. |
| PRG-EV-432 | Completion uses versioned Product rules | DEC-155/§21F.9 require versioned participation-based completion and reject weight loss, perfect adherence and uninterrupted streak as universal requirements. |
| PRG-EV-433 | Version pinning/migration are authoritative | DEC-156/§21F.10 keep active Enrolments on their ProgrammeVersion unless correction/migration/Safety rules apply; migration requires explicit progress mapping. |
| PRG-EV-434 | Programme catalogue lifecycle is not a ProgrammeVersion enum | DEC-148 gives Programme catalogue states; current authority does not require each ProgrammeVersion to mirror them. |
| PRG-EV-435 | Stable Programme identity remains part of the hierarchy | DEC-147 defines Programme, ProgrammeVersion, Module, Lesson and Activity; ProgrammeVersion + Enrolment is a semantic centre, not the whole schema. |
| PRG-EV-436 | Programmes owns the lifecycle | Domain Law assigns programme lifecycle/delivery mode, Edition/Cohort schedule, Enrolment lifecycle and progression/completion truth to Programmes & Challenges. |
| PRG-EV-437 | Concurrency mechanism follows the invariant | Architecture §7.2 permits atomic mutation, uniqueness, optimistic checks, locking or isolation as justified by the invariant. |
| PRG-EV-438 | Queue uniqueness is not business correctness | Oban is execution machinery; queue uniqueness does not replace business idempotency. |
| PRG-EV-439 | Prior handoff left lifecycle races too generic | Pass 18 routed pause-vs-completion and abandon-vs-completion to owner lifecycle guards without freezing the business-level guard contract. |
| PRG-EV-440 | Nuwe Jy Edition activation has Product checkpoints | DEC-211 creates each Edition from an approved ProgrammeVersion and validates configured content/translations/schedule/sessions/Safety/facilitation/products/Community/Communications before activation. |
| PRG-EV-441 | Nuwe Jy shared schedule is Edition-governed | DEC-212 keeps late Enrolments on the shared Cohort schedule with guided catch-up rather than participant-specific schedule rewriting. |
| PRG-EV-442 | Product Law does not define command precedence or same-attempt reopen | No current Product clause says completion beats abandonment, abandonment beats completion, paused attempts auto-complete, or terminal attempts reopen as the same Enrolment. |
| PRG-EV-443 | Correction law preserves explicit correction semantics | DEC-241 permits direct update where appropriate and additive/superseding correction where required; Programme correction remains explicit and provenance-preserving. |
| PRG-EV-444 | Certificates are authorised but post-award invalidation policy is absent | DEC-217 permits compassionate outcomes/certificates but does not decide revoke/supersede/reissue/display/appeal after later source correction. |
| PRG-EV-445 | No-replacement required-content consequence is Product meaning | Content owns withdrawal/replacement truth, but current Product Law does not choose substitute/waive/pause/migrate/change-eligibility/withdraw when no approved replacement exists. |
| PRG-EV-446 | OQ-019 is narrower than gaps 002/011 | OQ-019 is programme-specific completion metrics, not post-award invalidation or no-replacement content-remedy policy. |
| PRG-EV-447 | OQ-025 is Nuwe Jy-specific | It cannot silently become generic Programme withdrawal/remediation law. |
| PRG-EV-448 | `PRG-UPD-001` remains valid but should be Edition-centred | The missing exceptional lifecycle concerns a committed scheduled Programme Edition; Cohort/Enrolment experience owner-mediated consequences. |
| PRG-EV-449 | Roadmap gates remain intact | FP-014 still blocks on OQ-018 where journals are used and OQ-019 for programme rules; Roadmap remains implementation-stopped. |
| PRG-EV-450 | Broad freeze can coexist with explicit Product stops | Generic discovery may freeze when unsupported lifecycle transitions and conditional participant-consequence policies are explicit Product-first stops rather than JIT discretion. |

---

# 200. Lifecycle handoff contract

## 200.1 Interpretation rule

The following matrices are **semantic handoff contracts**, not mandated Ash Resource enums or database state machines. Where Product Law names an operation but does not settle a material participant-semantic guard, the matrix fails closed instead of delegating the business decision to JIT.

### Enrolment

| Semantic condition/checkpoint | Command / trigger | Minimum authorised guard | Durable Programme consequence | Cross-owner side effects / boundaries | Normal terminality | Retry / concurrency contract |
|---|---|---|---|---|---|---|
| No Enrolment attempt | `enrol` | Applicable Programme/ProgrammeVersion is selectable; required current access/eligibility passes; duplicate simultaneous same-Version attempt is not allowed unless explicitly configured | Create one durable attempt pinned to its ProgrammeVersion | Owner-mediated configured consequences only; purchaser/Entitlement/Safety truth remains with owners | Non-terminal | Same logical command is idempotent; duplicate race must not create two attempts |
| Existing enrolled attempt, before participation begins | `schedule` where the delivery mode supports it | Scheduling is part of the approved Programme mode; shared scheduled-cohort dates remain Edition authority | Record participant scheduling choice/reference without creating a new attempt | Communications may derive reminders; private scheduling cannot rewrite shared Edition truth | Non-terminal | Duplicate scheduling repeat-safe; unsupported post-begin/shared-schedule mutation is not inferred |
| Enrolled/scheduled attempt | `begin` | Current protected access plus applicable Safety/prerequisite guards pass; no normal terminal outcome exists | Mark participation begun/in progress on the same version-pinned attempt | Other Domains remain guards/evidence owners | Non-terminal | Revalidate current state; stale begin cannot reopen terminal history |
| Begun/in-progress attempt | `pause` | Existing non-terminal in-progress attempt | Same attempt becomes paused; accepted progress/version/history remain | Does not itself change Entitlement, Edition clock, Communications preference or Safety truth | Non-terminal | Duplicate pause idempotent; conflicts use current-state/revision checks |
| Paused attempt | `resume` | Current access/Safety/prerequisite authority is revalidated | Same attempt returns to active/in-progress participation | Does not restore stale pre-pause authority or shift shared Edition schedule | Non-terminal | Duplicate resume repeat-safe; stale resume cannot override newer owner state |
| Begun/resumed, current-valid participation | `complete` / governed completion evaluation | Versioned completion rules satisfied; Programme-specific threshold/outcome mapping approved | Record Programmes-owned completion outcome | Certificate/Communications/Analytics consequences remain separately governed | **Normal same-attempt terminal** | At most one conflicting transition from the same prior revision may commit; no type precedence or last-write-wins |
| Approved final evaluation yields a non-complete outcome such as `participated` / `partially_completed` where that vocabulary is enabled | governed outcome finalisation | Programme-specific Product contract defines the outcome and criteria | Record versioned Programmes-owned outcome without fabricating completion | Analytics/Communications consume owner outcome only | **NOT GENERICALLY DEFINED** — Product/Programme contract must define whether catch-up can later change it or it is final | JIT must not infer terminality/reopenability from the label |
| Existing non-terminal attempt | `abandon` | Explicit participant/governed owner intent; inactivity, time passage, access loss or Cohort conclusion alone is insufficient | Record durable abandonment while preserving prior progress/history | Does not itself revoke Entitlement or erase external evidence | **Normal same-attempt terminal** | Conflicting transition uses current-state/revision check; stale command fails/reloads |
| Completed or abandoned historical attempt | `restart` | Programme permits restart; current access/eligibility rechecked; no prohibited simultaneous attempt; no silent paid-entitlement consumption | Create a **new linked Enrolment**; prior attempt remains unchanged | Entitlements decides any access/consumption consequence | Old attempt remains terminal; new attempt non-terminal | Retry converges on one new logical attempt, not multiplied attempts |
| Active version-pinned attempt | optional governed ProgrammeVersion migration | Migration Product-authorised/accepted where required and progress mapping explicit | **Identity shape is not authorised generically:** same-Enrolment vs successor-Enrolment is Product decision when concrete migration is needed | Content/Safety/other owner references remain provenance, not copied authority | Not fixed generically | JIT must stop rather than pick a representation that changes participant-semantic identity |
| Active attempt affected by Safety correction | governed migration or withdrawal request | Current Safety authority requires the consequence | Programmes records approved Programme-side consequence with provenance | Safety owns reason/restriction; Programmes owns participation consequence | Return/reopen semantics not fixed generically | Automatic same-attempt return after later Safety clearance is **NOT AUTHORISED** without Product rule |
| Historical/current Programme outcome affected by authoritative correction | correction / reconciliation | Source-owner correction authoritative; Programmes applies approved correction rule | Preserve before/after provenance; direct or superseding correction as appropriate; correction is **not** normal lifecycle reopen | Post-award consequence routes through `PRG-GAP-002` where applicable | Original history preserved | Repeat correction/reconciliation idempotent and current-source aware |
| Edition/Cohort completion window or schedule boundary arrives | scheduled evaluation | Approved Programme/Edition rule says evaluation is due | Evaluate attempt; do **not** fabricate completion/abandonment merely because time passed | Communications/Analytics consume resulting owner truth | No automatic terminality | Repeated evaluation converges on same owner outcome |

### Conflict rule for Enrolment commands

For two commands targeting the same authoritative Enrolment revision/state:

1. both validate current owner truth;
2. at most one mutually exclusive transition may commit from that prior revision;
3. there is **no generic command-type precedence** such as `complete > abandon` or `abandon > complete`;
4. the stale loser fails/reloads current state rather than overwriting or blind-retrying;
5. automatic retry may repeat the same intended business effect but may not reinterpret it as another transition; and
6. if Product needs semantic precedence or same-attempt reopen behaviour, that rule must be explicit upstream before implementation.

This uses Architecture's invariant-specific concurrency controls without turning lock acquisition or arrival order into Product Law.

## 200.2 Programme / ProgrammeVersion checkpoints

| Checkpoint | Current-authority handoff |
|---|---|
| Stable identity | `Programme` remains the stable catalogue/product identity; `ProgrammeVersion` is the versioned participant-semantic configuration. |
| Catalogue lifecycle | `draft → internal → pilot → public → paused → retired` is Programme catalogue law (DEC-148). Do **not** automatically mirror it into a ProgrammeVersion enum. |
| Material meaning change | Material approved change creates a new ProgrammeVersion; do not mutate in-use/completed semantic meaning in place. |
| New Enrolment selection | New Enrolments normally use the latest approved ProgrammeVersion. |
| Active version pin | Active Enrolments remain on their enrolled ProgrammeVersion unless minor correction, governed migration or Safety correction applies. |
| Minor correction | Apply only within correction semantics authorised by Product/owner law; preserve exact historical delivered/content provenance where material. |
| Optional migration | Requires governed migration and explicit progress mapping. Product Law does **not** decide same-Enrolment vs successor-Enrolment identity; that question is Product-first if a concrete FP needs it. |
| Safety migration/withdrawal | May override ordinary version pinning when current Safety requires it; Programme consequence remains Programmes-owned and provenance-preserving. |
| Completed history | Completed history never changes silently; correction/supersession is explicit. |
| Version retirement/selectability mechanics | Exact ProgrammeVersion lifecycle enum/retirement mechanics are not fully defined by current Product Law; JIT may implement representation only after business meaning is clear. |

## 200.3 Edition / Cohort checkpoints

| Checkpoint | Current-authority handoff |
|---|---|
| Applicability | Edition/Cohort is delivery-mode-specific; do not require it for every evergreen/self-paced Programme. |
| Nuwe Jy Edition creation | Create from an approved ProgrammeVersion. |
| Activation | Validate configured Nuwe Jy Content, translations, schedule, sessions, Safety, facilitation, products, Community and Communications before activation. This is not a universal all-Programme checklist. |
| Schedule authority | Nuwe Jy shared schedule is Edition-governed; Cohorts/Enrolments do not create competing release calendars. |
| Late Enrolment | Follow Edition-specific late-enrolment policy and guided catch-up while remaining on shared Cohort schedule. |
| Enrolment pause/resume | Does not shift shared Edition clock by itself. |
| Cohort/Edition conclusion | Triggers governed evaluation/catch-up handling; does not itself fabricate participant completion or abandonment. |
| Committed pre-start cancellation | **NOT AUTHORISED / PRODUCT DECISION REQUIRED — `PRG-UPD-001`.** |
| Material post-commit reschedule/postponement | **NOT AUTHORISED / PRODUCT DECISION REQUIRED — `PRG-UPD-001`.** |
| Mid-run organiser termination | **NOT AUTHORISED / PRODUCT DECISION REQUIRED — `PRG-UPD-001`.** |
| Generic Edition/Cohort lifecycle enum | Not defined by current Product Law; do not invent one merely for symmetry. |

## 200.4 Completion / correction checkpoints

| Trigger | Current-authority consequence |
|---|---|
| Completion criteria satisfied under the attempt's ProgrammeVersion | Programmes records approved versioned outcome; exact thresholds remain Product-gated (`OQ-019`, plus Nuwe Jy-specific gates where applicable). |
| Source evidence corrected before any award consequence | Programmes explicitly reconciles its own outcome from current authoritative source truth while preserving correction history/provenance. |
| Source correction undermines an already-issued certificate/award | **`PRG-GAP-002 — CONDITIONAL PRODUCT-FIRST`.** Product must define revoke/supersede/reissue/display/appeal/review/notification meaning before implementation chooses a consequence. |
| Required governed Content withdrawn and an approved replacement/substitution exists | Content owns version/withdrawal/replacement truth; Programmes follows the already-approved Programme consequence. |
| Required governed Content withdrawn with **no** approved replacement/substitution | **`PRG-GAP-011 — PRODUCT-FIRST WHEN TRIGGERED`.** Product must decide substitute/waive/pause/migrate/eligibility/withdrawal or another participant consequence before JIT implements it. |
| Lawful deletion removes private source payload/provenance | Privacy/HJP retention authority controls what may remain; Programmes must not resurrect deleted private truth from Analytics/Audit/cache/backups. |

---

# 201. Corrected residual Product-authority routing

## 201.1 PRG-GAP-002

**New current working classification:**

`OPEN / CONDITIONAL PRODUCT-FIRST / AWARD-USE BLOCKER WHEN TRIGGERED`

Product authority must decide participant-facing policy when corrected authoritative evidence undermines an already-issued completion award/certificate. Possible dimensions include, without deciding them here: invalidate/preserve-as-historical/supersede; revoke/reissue; participant-visible display/history; notification obligation; review/appeal; effective date and historical provenance.

Programmes remains owner of completion/certificate outcome. Other Domains retain their source/correction/delivery/audit truth. **JIT may not choose the policy.**

## 201.2 PRG-GAP-011

**New current working classification:**

`OPEN / PRODUCT-FIRST WHEN TRIGGERED / BLOCKS AFFECTED FP OR RELEASE`

When required governed Content is withdrawn and there is no approved replacement/substitution, Product authority must decide the participant Programme consequence before implementation. Possible dimensions include, without deciding them here: substitute another requirement; waive it; pause affected progression/delivery; migrate to another governed version/path; change completion eligibility; withdraw/terminate affected delivery; participant remedy/communication expectations where applicable.

Content remains owner of withdrawal/replacement truth. Programmes implements only an approved Programme consequence. `OQ-019` is not authority for this decision.

## 201.3 PRG-UPD-001

**Corrected title:**

`PRG-UPD-001 — Committed scheduled Programme Edition exceptional lifecycle contract`

Status remains:

`CONFIRMED / NARROWED / NON-AUTHORITATIVE / IMPLEMENTATION BLOCKED AT PRODUCT AUTHORITY WHEN APPLICABLE`

The missing Product semantics remain:

1. organiser cancellation of a committed scheduled Edition before start;
2. material postponement/reschedule after participant or commercial commitment;
3. organiser termination/cancellation after the Edition starts;
4. command guards/commitment boundary;
5. same-Edition reschedule versus governed successor/migration meaning;
6. participant choice/right-to-exit where applicable;
7. preservation of Enrolment/progress/history;
8. commercial-remedy eligibility while Commerce retains remedy authority;
9. current-access consequence while Entitlements retains access authority;
10. completion/certificate consequence; and
11. linked owner-mediated Events/Community/Communications consequences.

**Cohort and Enrolment are affected Programmes-owned truths; they are not co-equal cancellation-policy owners.** No participant-transfer/Cohort-merge/generic cancellation engine is added.

## 201.4 Product-first residual statement

The current handoff must no longer say that `PRG-UPD-001` is the only upstream Programme authority work.

The correct statement is:

> `PRG-UPD-001` is the sole currently named `PRG-UPD` identifier. Product-first residual work also exists conditionally under `PRG-GAP-002`, `PRG-GAP-011`, and any lifecycle-matrix cell explicitly marked `PRODUCT DECISION REQUIRED` when a concrete Feature Pack needs that behaviour.

---

# 202. Corrective pressure tests

| ID | Test | Disposition | Key conclusion / route |
|---|---|---|---|
| PRG-PT-1017 | Duplicate `enrol` commands create two attempts | REJECT | Same logical effect is idempotent and duplicate simultaneous same-Version Enrolments remain prohibited unless explicitly allowed. |
| PRG-PT-1018 | Participant begins without current protected access | REJECT | Current Entitlements/eligibility guards are revalidated; history does not grant present permission. |
| PRG-PT-1019 | Participant schedule command shifts shared Edition calendar | REJECT | Shared scheduled-cohort calendar remains Edition authority. |
| PRG-PT-1020 | Pause deletes progress or creates replacement Enrolment | REJECT | Pause preserves the same attempt, version and accepted progress. |
| PRG-PT-1021 | Pause automatically extends a scheduled Edition deadline | REJECT | Pause does not rewrite Edition time; extension/catch-up requires approved Programme/Edition policy. |
| PRG-PT-1022 | Resume restores stale pre-pause access/Safety | REJECT | Resume revalidates current owner authority. |
| PRG-PT-1023 | Completion submitted while paused | NOT AUTHORISED BY GENERIC PRODUCT LAW | Do not invent auto-completion-while-paused; absent an explicit Product rule, resume/current valid participation is required first. |
| PRG-PT-1024 | Completion and abandonment race from same revision | CONFLICT / NO TYPE PRECEDENCE | At most one owner transition commits; stale command fails/reloads; no last-write-wins or command priority. |
| PRG-PT-1025 | Pause and completion race | CONFLICT / NO TYPE PRECEDENCE | At most one transition commits from expected current state; loser re-reads and cannot blind-retry into another outcome. |
| PRG-PT-1026 | Inactivity or deadline infers abandonment | REJECT | Ordinary delay, cohort conclusion, deadline or inactivity does not fabricate abandonment. |
| PRG-PT-1027 | Explicit abandon preserves history | PASS | Abandonment is Programmes-owned durable outcome and does not erase prior evidence. |
| PRG-PT-1028 | Completed Enrolment resumes as same attempt | NOT AUTHORISED | Normal `completed` outcome is same-attempt terminal; non-complete final-outcome terminality must be explicitly defined by Product contract. |
| PRG-PT-1029 | Abandoned Enrolment resumes as same attempt | NOT AUTHORISED | Restart, not destructive reopening, is the authorised fresh-participation path. |
| PRG-PT-1030 | Restart mutates terminal attempt back to active | REJECT | Restart creates a new linked Enrolment and preserves old history. |
| PRG-PT-1031 | Restart silently consumes paid entitlement | REJECT | Product Law expressly forbids silent consumption. |
| PRG-PT-1032 | Restart creates second simultaneous same-Version active attempt | NOT AUTHORISED BY DEFAULT | Duplicate simultaneous Enrolments are prohibited unless explicitly allowed. |
| PRG-PT-1033 | Active Enrolment floats to newer ProgrammeVersion | REJECT | Active attempts remain version-pinned absent governed correction/migration. |
| PRG-PT-1034 | Migration occurs with no progress mapping | REJECT | Explicit mapping is a Product requirement. |
| PRG-PT-1035 | JIT decides migration mutates same Enrolment | NOT AUTHORISED / PRODUCT DECISION REQUIRED | Current Product Law does not define same-vs-successor Enrolment identity semantics. |
| PRG-PT-1036 | JIT decides migration always creates new Enrolment | NOT AUTHORISED / PRODUCT DECISION REQUIRED | The opposite representation is equally unsupported. |
| PRG-PT-1037 | Safety correction requires migration/withdrawal | PASS WITH OWNER AUTHORITY | Safety owns reason/restriction; Programmes owns the approved Programme consequence and provenance. |
| PRG-PT-1038 | Safety later clears and JIT auto-reopens same Enrolment | NOT AUTHORISED / PRODUCT DECISION REQUIRED | Same-attempt return after Safety withdrawal is undefined. |
| PRG-PT-1039 | Programme catalogue lifecycle is copied as ProgrammeVersion enum | REJECT | DEC-148 is catalogue lifecycle law, not a mirrored ProgrammeVersion lifecycle. |
| PRG-PT-1040 | Material Programme meaning edited in place | REJECT | Material changes require a new ProgrammeVersion; historical meaning remains pinned. |
| PRG-PT-1041 | New Enrolments normally select latest approved ProgrammeVersion | PASS AS NORMAL RULE | Matches §21F.10, subject to any separately authorised deliberate version pin. |
| PRG-PT-1042 | Completed history recalculated under latest ProgrammeVersion | REJECT | Completed history does not change silently. |
| PRG-PT-1043 | Nuwe Jy Edition activates without required validation | REJECT | DEC-211 activation checkpoint is explicit. |
| PRG-PT-1044 | Cohort invents release calendar independent of Edition | REJECT | Shared schedule is Edition-governed. |
| PRG-PT-1045 | Cohort conclusion auto-completes every Enrolment | REJECT | Time boundaries trigger evaluation/recovery, not fabricated outcome. |
| PRG-PT-1046 | Committed scheduled Edition materially rescheduled by JIT policy | BLOCKED / PRG-UPD-001 | Product authority must first define exceptional lifecycle/remedies. |
| PRG-PT-1047 | `PRG-UPD-001` described as Cohort cancellation policy | CORRECT TERMINOLOGY | Upstream Product question is Edition-level committed scheduled delivery; Cohort/Enrolment are affected truths. |
| PRG-PT-1048 | Source correction invalidates completion before certificate | PASS WITH PROGRAMMES RECONCILIATION | Programmes reconciles own outcome with correction provenance under approved Programme rules. |
| PRG-PT-1049 | Source correction undermines issued certificate and JIT auto-revokes | BLOCKED / PRG-GAP-002 PRODUCT-FIRST | Revocation/supersession/reissue/display/appeal is Product meaning. |
| PRG-PT-1050 | JIT preserves invalidated certificate forever as valid | BLOCKED / PRG-GAP-002 PRODUCT-FIRST | The opposite policy is also not authorised. |
| PRG-PT-1051 | Required Content withdrawn with approved replacement | PASS WITH OWNER-MEDIATED CONSEQUENCE | Content owns replacement/version truth; Programmes follows approved consequence. |
| PRG-PT-1052 | No-replacement Content case and JIT waives requirement | BLOCKED / PRG-GAP-011 PRODUCT-FIRST | Waiver changes participant Programme contract. |
| PRG-PT-1053 | No-replacement case and JIT pauses all participants | BLOCKED / PRG-GAP-011 PRODUCT-FIRST | Pause may be a future remedy but is not currently Product-authorised. |
| PRG-PT-1054 | No-replacement case and JIT migrates participants | BLOCKED / PRG-GAP-011 PRODUCT-FIRST | Migration is not an implementation default. |
| PRG-PT-1055 | No-replacement case and Programmes fabricates completion | REJECT | Missing/withdrawn Content cannot become false evidence. |
| PRG-PT-1056 | OQ-019 used as certificate invalidation authority | REJECT | OQ-019 is programme-specific completion metrics. |
| PRG-PT-1057 | OQ-019 used as withdrawn-content remediation authority | REJECT | It does not define required-content remedies. |
| PRG-PT-1058 | OQ-025 used as generic Foundation content-withdrawal policy | REJECT | OQ-025 is Nuwe Jy-specific. |
| PRG-PT-1059 | Handoff says `PRG-UPD-001` is the only Product-first Programme work | REJECT / CORRECTED | It remains the sole named `PRG-UPD`, not the sole Product-first residual. |
| PRG-PT-1060 | Smaller agent chooses a “reasonable” policy for unsupported transition | REJECT / FAIL CLOSED | `NOT AUTHORISED / PRODUCT DECISION REQUIRED` is a hard semantic stop. |
| PRG-PT-1061 | Feature Pack narrows optional Product capability without contradiction | PASS | An FP may choose a supported subset/mode; it may not invent broader participant semantics. |
| PRG-PT-1062 | Feature Pack needs migration identity semantics marked unsupported | STOP AT PRODUCT | Resolve Product semantics first, then return to JIT representation. |
| PRG-PT-1063 | Broad Pre-JIT remains open merely because conditional Product stops exist | REJECT | Known, correctly routed Product stops do not require further generic discovery. |
| PRG-PT-1064 | Broad Pre-JIT freezes while Product stops remain hidden in JIT notes | REJECT | Freeze is safe only because the matrix/gap map expose them and fail closed. |
| PRG-PT-1065 | Correction adds a new Domain/architecture mechanism | REJECT / NOT NEEDED | Corrective pass changes semantic handoff/routing only. |
| PRG-PT-1066 | Final freeze gate after lifecycle/routing corrections | PASS / FREEZE-READY CANDIDATE | The two review blockers are corrected without reopening broad architecture; residual Product stops are explicit. |

---

# 203. Corrective refinements

| ID | Refinement | Effect |
|---|---|---|
| PRG-REF-355 | Add one compact lifecycle handoff contract rather than a generic LMS state machine. | Explicit business semantics with representation freedom. |
| PRG-REF-356 | Treat Enrolment lifecycle checkpoints as semantic conditions unless Product defines a persisted enum. | Avoid accidental schema law. |
| PRG-REF-357 | Treat completed and abandoned as normal same-attempt terminal outcomes; correction remains separate. | Prevent casual resume/reopen of history. |
| PRG-REF-358 | Restart creates a new linked Enrolment and preserves the old attempt. | Reinforces Product Law. |
| PRG-REF-359 | Conflicting Enrolment commands use expected-current-state/revision semantics with no command-type precedence. | Prevent last-write-wins and hidden priority. |
| PRG-REF-360 | Unsupported migration identity semantics fail closed at Product. | JIT cannot decide same-vs-successor Enrolment meaning. |
| PRG-REF-361 | Do not mirror Programme catalogue lifecycle into ProgrammeVersion lifecycle. | Preserve correct distinction. |
| PRG-REF-362 | ProgrammeVersion + Enrolment is a semantic centre, not the whole schema. | Preserve stable Programme identity and owner references. |
| PRG-REF-363 | Edition/Cohort checkpoints remain configuration-specific; no universal state machine. | Avoid invented generic lifecycle. |
| PRG-REF-364 | Rename `PRG-UPD-001` around committed scheduled Programme Edition exceptional lifecycle. | Keep Product amendment at real shared-delivery boundary. |
| PRG-REF-365 | Cohort/Enrolment are affected truths under `PRG-UPD-001`, not co-equal policy owners. | Preserve Edition-centred semantics. |
| PRG-REF-366 | Reclassify `PRG-GAP-002` as conditional Product-first. | Product decides post-award invalidation meaning. |
| PRG-REF-367 | Reclassify `PRG-GAP-011` as Product-first when required Content lacks replacement. | Participant remedy cannot be invented downstream. |
| PRG-REF-368 | OQ-019 does not close gaps 002/011. | Prevent authority laundering. |
| PRG-REF-369 | `PRG-UPD-001` is sole named upstream-delta identifier, not sole Product-first residual work. | Correct convergence overclaim without new IDs. |
| PRG-REF-370 | Unsupported transitions say `NOT AUTHORISED / PRODUCT DECISION REQUIRED`. | Safe handoff for smaller agents. |
| PRG-REF-371 | Corrections/supersessions remain separate from normal lifecycle reopening. | Preserve history/provenance. |
| PRG-REF-372 | Edition conclusion/time boundaries trigger evaluation, not participant outcomes. | Prevent fabricated completion/abandonment. |
| PRG-REF-373 | Entitlement/Safety authority are guards, not Enrolment state dimensions. | Keep lifecycles independent. |
| PRG-REF-374 | No new `PRG-GAP` or `PRG-UPD` IDs in this corrective pass. | Review exposed routing/closure defects, not a new owner family. |
| PRG-REF-375 | Rerun only freeze gate after bounded corrections. | Avoid reopening successful broad discovery. |
| PRG-REF-376 | Freeze corrected successor rather than silently edit v0.24.0. | Preserve append-only provenance. |

---

# 204. Freeze-gate rerun

The reviewer did **not** identify a new Domain owner, a broken ProgrammeVersion/Enrolment abstraction, a failed FP-014 second lens, or a need for new infrastructure.

After applying the two blocking corrections:

- lifecycle commands/checkpoints no longer delegate material business semantics vaguely to JIT;
- unsupported transition semantics fail closed at Product;
- `PRG-GAP-002` and `PRG-GAP-011` are Product-first when triggered;
- `PRG-UPD-001` is Edition-centred and no longer described as the sole Product-first residual work; and
- no new gap/update identifier, Domain or mechanism is required.

**Corrective review disposition: PASS.**

**Corrected broad-discovery disposition: FREEZE-READY / STOP GENERIC PRE-JIT DISCOVERY — CANDIDATE PENDING USER ACCEPTANCE.**

If accepted:

```text
PROGRAMMES / LEARNING BROAD PRE-JIT DISCOVERY
=> WORKING_FROZEN / NON-AUTHORITATIVE / HANDOFF-READY

FINAL CORRECTIVE PASS
=> v0.25.0 / PASS 24

NO DEFAULT BROAD PASS 25

IMPLEMENTATION
=> NOT AUTHORISED
```

The Product-first cells/gaps remain hard stops when their trigger enters actual scope. Freeze means the missing decisions are **known and correctly routed**, not silently solved.

---

# 205. Candidate corrected final conclusions

Pending explicit user acceptance:

1. Passes 1–23 remain historical working evidence; Pass 23's freeze-ready conclusion was legitimately reopened by independent review without reopening unaffected semantics.
2. The independent reviewer was correct that the lifecycle handoff was not explicit enough for smaller downstream agents.
3. The independent reviewer was also correct that `PRG-GAP-002` and `PRG-GAP-011` were routed too low in the final residual map.
4. ProgrammeVersion + Enrolment/attempt remains the reusable semantic centre, but stable Programme identity and owner-version/source references remain required surrounding truth.
5. Enrolment lifecycle is now handed off as explicit semantic checkpoints/commands/guards/consequences rather than a vague “owner lifecycle guards decide” instruction.
6. The lifecycle matrix is not a mandated persisted enum or schema.
7. Enrol creates a durable version-pinned attempt and duplicate simultaneous same-Version attempts remain prohibited unless explicitly allowed.
8. Pause/resume remain the same attempt; pause preserves progress/version and does not shift Edition time or Entitlement truth; resume revalidates current authority.
9. Completed and abandoned are normal same-attempt terminal outcomes for participant-driven lifecycle; restart creates a new linked attempt rather than reopening them.
10. Current Product Law does not authorise automatic completion while paused, same-attempt reopen, simultaneous active restart, or migration identity shape; those cases fail closed as Product decisions when needed.
11. Conflicting Enrolment commands use authoritative current-state/revision checks with no generic command-type precedence and no blind stale retry.
12. Programme catalogue lifecycle states must not be copied into a ProgrammeVersion lifecycle enum.
13. Material Programme meaning creates a new ProgrammeVersion; active attempts remain pinned unless governed correction/migration applies; completed history never changes silently.
14. Governed migration requires explicit progress mapping, but current Product Law does not decide same-Enrolment versus successor-Enrolment identity; JIT must not invent it.
15. Nuwe Jy Edition activation and shared schedule checkpoints remain explicit while a universal Edition/Cohort state machine remains unjustified.
16. Edition/Cohort conclusion or time boundaries do not automatically complete, abandon or reopen Enrolments.
17. `PRG-UPD-001` remains necessary but is renamed/scoped to the committed scheduled Programme Edition exceptional lifecycle.
18. Cohort and Enrolment are affected Programme truths under `PRG-UPD-001`; they are not co-equal cancellation-policy owners.
19. `PRG-GAP-002` is now `OPEN / CONDITIONAL PRODUCT-FIRST`: award/certificate invalidation policy must be decided by Product before implementation when triggered.
20. `PRG-GAP-011` is now `OPEN / PRODUCT-FIRST WHEN TRIGGERED`: no-replacement required-content consequences must be decided by Product before implementation.
21. OQ-019 does not decide post-award invalidation or required-content remediation.
22. `PRG-UPD-001` is the sole currently named PRG-UPD identifier, but it is not the sole Product-first residual Programme work.
23. No new upstream identifier is invented by this corrective pass.
24. Correction/supersession remains separate from normal lifecycle reopening and preserves historical provenance.
25. Current Entitlement/Safety/Consent authority remains a guard on current actions rather than being collapsed into Enrolment lifecycle state.
26. The corrective changes require no new Domain, Resource family, service, event store, saga, workflow engine or Analytics authority.
27. The two independent-review blockers are materially corrected.
28. Known Product-first stops may remain unresolved while broad generic discovery freezes because their scope, owner and fail-closed behaviour are now explicit.
29. Corrected broad Programmes/Learning Pre-JIT is again freeze-ready as a non-authoritative handoff candidate, pending explicit user acceptance.
30. There is no default broad Pass 25; later re-entry still requires a concrete authority/proof/Feature-Pack contradiction or explicit Product-resolution trigger.

---

# 206. Hard stop

There is **NO DEFAULT BROAD PASS 25**.

If this corrective candidate is accepted, use the corrected v0.25.0 cumulative handoff as working navigation and retain all focused ledgers as append-only provenance.

Any Product-first lifecycle cell, `PRG-GAP-002`, `PRG-GAP-003/PRG-UPD-001`, `PRG-GAP-007`, `PRG-GAP-011` or other named authority gate remains active and must fail closed when its trigger is in scope.
