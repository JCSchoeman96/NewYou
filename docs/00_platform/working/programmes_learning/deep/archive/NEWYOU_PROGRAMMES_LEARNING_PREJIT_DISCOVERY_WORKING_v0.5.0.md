# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.5.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.5.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 4 — Edition / Cohort semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.4.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused Edition / Cohort semantic pass while preserving v0.1.0 through v0.4.0 unchanged.

> This is an append-only semantic successor. Read v0.1.0 → v0.2.0 → v0.3.0 → v0.4.0 → this pass. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work or any owning Domain.

> Nuwe Jy remains the first concrete programme acceptance test. Edition/Cohort semantics must be derived from NewYou’s approved delivery outcomes, not from generic LMS/course-cohort convention.

---

# 33. Accepted working-lock status entering Pass 4

The user accepted Pass 3 after review.

Therefore Passes 1–3 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, deferred items and future explicit refinements.

Pass 4 inherits, without reopening, these accepted boundaries:

- Programme is the stable conceptual/catalogue identity;
- ProgrammeVersion is the version-pinned participant-semantic contract;
- Edition is not ProgrammeVersion and not Commerce Product/Offer;
- Cohort is not Community group;
- enrolment is the durable participant programme attempt/history;
- Edition-bound enrolment uses the Edition’s explicit source ProgrammeVersion;
- multiple Editions may reuse the same ProgrammeVersion;
- Content & Media remains content/version/translation/publication authority;
- exact delivered ContentVersion/locale provenance must remain explainable;
- active enrolment does not silently follow a “latest” ProgrammeVersion or “latest” content pointer;
- Pass 4 may re-adjudicate the earlier Edition/Cohort ambiguity and `PRG-UPD-001`, but may not solve Pass 5 access/entitlement policy or later completion/recovery semantics.

---

# 34. Pass 4 — Edition / Cohort semantics

## 34.1 Scope hard stop

This pass answers only:

1. whether Edition is universal or optional across reusable programmes;
2. what semantic responsibility belongs to Edition versus Cohort;
3. how `ChallengeEdition → one or more Cohorts` composes with Edition-owned release/calendar configuration;
4. what “shared cohort schedule” means for Nuwe Jy;
5. when a new delivery configuration should be a new Edition rather than a new ProgrammeVersion or Cohort override;
6. whether multiple Cohorts under one Edition may carry divergent schedules/timezones/support/community rules;
7. which capacity/facilitation/community/live allocation questions are already routed to `OQ-026` rather than missing Product Law;
8. what normal activation/conclusion/archive checkpoints are semantically required without inventing a generic Edition/Cohort state machine;
9. how late enrolment and catch-up preserve the shared schedule;
10. whether the bootstrap exceptional-lifecycle gap (`PRG-GAP-003` / `PRG-UPD-001`) is genuinely justified after dedicated pressure testing; and
11. which exceptional actions should be required versus explicitly deferred.

This pass deliberately does **not** decide:

- entitlement lapse/reacquisition/current access consequences — Pass 5;
- detailed availability/prerequisite/release mechanics — Pass 6;
- activity evidence ownership contracts — Pass 7;
- completion thresholds/adjudication — Pass 8;
- exemptions/substitutions — Pass 9;
- recovery/catch-up policy detail — Pass 10;
- live transport/recording provider mechanics;
- Community moderation mechanics;
- Communications retry/channel mechanics;
- exact Ash Resources, fields, indexes, transactions, Oban jobs, worker names or UI actions.

---

## 34.2 Pass-4 authority evidence

### PRG-EV-028 — Live authority baseline reconfirmed

Live `main` remains:

`086ade7b28c000de1c387acb9760e5eb08bb0413`

`docs/00_platform/README.md` still routes default authority to:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `00_PLATFORM_v1.6.0.md`
- `01_DECISIONS_v1.6.0.md`
- `02_OPEN_WORK_v1.2.59.md`
- `03_ARCHITECTURE_v1.1.1.md`
- `04_DOMAIN_MAP_v1.2.0.md`
- `05_ROADMAP_v1.2.0.md`
- `PLATFORM_OPERATING_MODEL_v1.0.1.md`

The current authority manifest confirms those versions. The working Programmes/Learning ledgers remain outside governing authority.

### PRG-EV-029 — Generic programme delivery modes do not require Cohort universally

Current Product Law §21F.3 and `DEC-149` support:

```text
evergreen_self_paced
scheduled_cohort
facilitated_cohort
```

The generic programme model therefore does not justify creating Cohort for every programme or every participant.

### PRG-EV-030 — Nuwe Jy explicitly introduces Edition between ProgrammeVersion and Cohort

Current Product Law §21H.2 locks the flagship path:

```text
Nuwe Jy Programme
→ approved ProgrammeVersion
→ ChallengeEdition
→ one or more Cohorts
```

`DEC-198` requires scheduled cohorts for the flagship mode and permits a later evergreen edition.

Edition and Cohort are therefore both real approved concepts for Nuwe Jy, but they are not synonyms.

### PRG-EV-031 — Edition is the authoritative Nuwe Jy delivery-configuration envelope

Product Law §21H.14 states that a ChallengeEdition defines:

- public name;
- edition code;
- source programme version;
- sales window;
- enrolment window;
- start date;
- all 60 release dates;
- timezone;
- facilitators;
- live sessions;
- community destination;
- capacity;
- entitlements;
- pricing product;
- completion deadline;
- catch-up window;
- archive date.

Before activation the Edition must validate required content/translations, release dates, live sessions, safety material, facilitator coverage, product/payment configuration, community configuration and communication templates.

`DEC-211` independently requires each Edition to be created from an approved ProgrammeVersion and validated across those dependencies before activation.

### PRG-EV-032 — Daily release is Edition-scheduled, while participant delivery is cohort-shared

`DEC-201` locks automatic daily release “by edition schedule” with timezone awareness, idempotency, observability and recovery.

Product §21H.5 requires all 60 days to be configured and the full release calendar validated before the Edition begins.

Product §21H.15 and `DEC-212` require an allowed late enrollee to join the cohort’s current day, receive guided catch-up for missed material and remain on the shared cohort schedule. NewYou must not silently create a private rolling 60-day schedule.

Therefore current law contains one shared scheduled-delivery truth for a Nuwe Jy Edition; Cohort does not need or receive an independent conflicting release calendar merely because it groups participants.

### PRG-EV-033 — Edition-level community and edition/cohort live references do not transfer authority

Product §21H.9 and `DEC-205` give each flagship Edition a governed cohort community, initially potentially a dedicated Facebook group.

Product §21H.10 and `DEC-206` link live sessions, registration, attendance and replays to the challenge Edition/Cohort.

Domain Law remains controlling:

- Programmes & Challenges owns Edition/Cohort and enrolment truth;
- Community owns community group/membership/posts/moderation;
- Events & Live owns live occurrence/registration/attendance truth.

External Facebook or live-provider state cannot become Cohort authority.

### PRG-EV-034 — Domain Law owns Edition/Cohort schedule and enrolment lifecycle

Current Domain Law §6.8 assigns Programmes & Challenges ownership of:

- programme lifecycle and delivery-mode configuration;
- edition/cohort schedule and enrolment lifecycle;
- progression/completion configuration/outcome;
- Nuwe Jy edition/day configuration and repeat-enrolment history.

Edition and Cohort are both named major concepts.

No new Domain is justified by their relationship.

### PRG-EV-035 — FP-008 needs one concrete scheduled cohort, not a generic multi-cohort engine

Current FP-008 outcome is “the first native Nuwe Jy edition” operating as an approved 60-calendar-day scheduled cohort.

Its validation objective is to drive only the reusable `programme/version/edition/cohort` primitives NewYou genuinely needs.

This proves:

- the initial Feature Pack must support a real Edition + scheduled Cohort;
- it does **not** require every permitted future multi-cohort variation to be implemented now;
- generic LMS cohort infrastructure remains unjustified.

### PRG-EV-036 — OQ-026 already owns unresolved operational allocation/capacity detail

Current `OQ-026 — Nuwe Jy edition operations` is an `OPERATIONS REVIEW` gate that must define:

- cohort capacity;
- facilitator coverage;
- moderator coverage;
- support ownership;
- live-session ownership;
- escalation;
- archive responsibilities.

Roadmap FP-008 classifies OQ-026 as blocking Edition activation/sale.

Therefore exact per-Cohort capacity, facilitator/moderator/support/live allocation and archive responsibility is **already an explicit governed gate**, not a reason for this pass to invent Product semantics.

### PRG-EV-037 — Current Product Law still lacks a scheduled-programme exceptional-lifecycle contract

Fresh searches of current authority found the explicit organiser-cancellation/postponement/transfer policy for Events, but no equivalent Nuwe Jy/Programme rule defining:

- Edition cancellation;
- Edition postponement;
- Cohort transfer;
- Edition transfer;
- Cohort merge;
- participant consequences of those actions.

The bootstrap concern in `PRG-GAP-003` / `PRG-UPD-001` is therefore not resolved by newer current authority.

This absence matters only where an exceptional action is genuinely required; it does not justify a generic lifecycle engine.

---

# 35. Pass-4 semantic model

These are working discovery semantics, not Resource/schema prescriptions.

## 35.1 Edition

**Working meaning:** a governed delivery configuration/envelope for one approved ProgrammeVersion where the concrete programme needs delivery configuration distinct from programme semantics.

For Nuwe Jy, the Edition owns the configured delivery contract that includes:

- explicit source ProgrammeVersion;
- public Edition identity/code;
- commercial/enrolment windows as references/configuration;
- the shared release calendar and timezone;
- completion/catch-up/archive dates;
- the Edition-level set/references for facilitation, live, community, capacity, entitlements/pricing and communications readiness.

Edition is **not**:

- the Programme itself;
- a ProgrammeVersion;
- a Cohort;
- a Commerce Product/Offer;
- a Community group;
- an Events occurrence;
- a generic LMS course run imported from another system.

## 35.2 Edition is not proven universal for every programme

Current generic programme law supports evergreen self-paced delivery and does not require an Edition layer in the universal `Programme → ProgrammeVersion → Module → Lesson → Activity` hierarchy.

Current authority **does** require Edition for Nuwe Jy and permits later evergreen Nuwe Jy Editions.

Therefore:

- do not make Edition mandatory for every future programme merely for consistency;
- use Edition where a concrete programme needs governed delivery configuration/run semantics;
- a simple evergreen programme may remain directly version/enrolment-oriented if no Edition-specific business truth exists.

This resolves the Pass-1 uncertainty without inventing a generic “course offering” abstraction.

## 35.3 Cohort

**Working meaning:** a Programmes-owned shared participant grouping/delivery context underneath a scheduled/facilitated Edition.

For Nuwe Jy flagship delivery:

- at least one Cohort exists;
- enrolments are associated with the applicable shared delivery context;
- “cohort current day” is the day reached by the Edition’s shared release calendar, not a second independently authoritative schedule;
- the Cohort may provide the grouping boundary needed for facilitation/live/community/operational assignment once OQ-026 defines those assignments.

Cohort is **not**:

- a Community group;
- the Edition’s release-calendar authority;
- an entitlement/access group;
- a personal 60-day clock;
- a generic class/section entity required by every programme.

## 35.4 Edition owns the schedule contract; Cohort must not duplicate it

For current Nuwe Jy law, Edition owns:

- start date;
- all 60 release dates;
- timezone;
- completion deadline;
- catch-up window;
- archive date.

Multiple Cohorts may exist beneath one Edition, but current authority does not authorise each Cohort to override those values independently.

Therefore the safe working rule is:

> **One Edition has one participant-facing delivery schedule contract. Cohorts under that Edition share it.**

If a group needs a materially different release calendar/timezone or materially different delivery/support/community rules, current authority points toward a different Edition, not an ungoverned Cohort override.

## 35.5 Multiple Cohorts are permitted but divergent Cohort behaviour is not automatically permitted

The explicit `one or more Cohorts` cardinality is retained.

A multi-Cohort Edition can represent parallel participant groups under one Edition contract.

However current law does not yet justify a generic per-Cohort override system for:

- release dates;
- timezone;
- completion/catch-up windows;
- commercial terms;
- different ProgrammeVersion;
- different Edition-level support/community policy.

Exact cohort-level assignment of facilitator/moderator/support/live ownership and capacity remains `OQ-026`.

The first FP-008 acceptance test can remain one Edition + one Cohort.

## 35.6 Scheduled/facilitated modes need Cohort; evergreen self-paced does not automatically need one

For a scheduled/facilitated delivery where participants share timing/group context, Cohort is meaningful.

For `evergreen_self_paced`, creating a one-person or perpetual “cohort” solely to satisfy a data model is rejected.

Current authority does not justify manufacturing one-person or perpetual Cohorts merely to satisfy a model.

For the **future Nuwe Jy evergreen Edition specifically**, exact Edition→Cohort cardinality is not required by FP-008 and is not fully explicit enough to freeze now: §21H’s scheduled flagship path says `ChallengeEdition → one or more Cohorts`, while generic programme law separately supports `evergreen_self_paced`. The safe rule is therefore to defer that future-only cardinality question rather than invent fake Cohorts now.

If Product later wants a facilitated evergreen group, that is a concrete delivery-mode requirement to model then.

## 35.7 Edition source ProgrammeVersion is historical delivery provenance, not a floating selector

An Edition is created from an approved ProgrammeVersion.

After the Edition becomes participant-facing/committed, implementation must not silently rebind it to a newer ProgrammeVersion because “latest approved” changed.

For a materially different ProgrammeVersion:

- future delivery normally uses a separately governed Edition/configuration;
- existing enrolments remain on their governing version unless an approved migration/safety path applies.

Before participant commitment/activation, authoring may change configured inputs only subject to complete revalidation; exact draft/edit mechanics remain JIT.

## 35.8 Activation is a real checkpoint; a generic Edition lifecycle enum is not authorised

Current Product Law explicitly requires validation **before activation** and provides dated windows/start/completion/catch-up/archive milestones.

It does not define a generic Edition state machine such as:

```text
draft → scheduled → selling → active → completed → archived → cancelled
```

Do not invent that lifecycle merely because LMS/event systems often have one.

JIT may represent only the minimum states/checkpoints required to enforce approved behaviour.

Any cancellation/postponement/suspension semantics must come from explicit Product policy rather than an inferred enum.

## 35.9 Cohort conclusion, participant completion and archive are separate truths

Product Law explicitly permits the Cohort to formally conclude while individual approved catch-up remains open.

Therefore:

- cohort conclusion does not auto-complete enrolments;
- an enrolment may remain incomplete/catching-up after the shared run concludes;
- completion remains evaluated under Programme-owned rules;
- archive date does not erase Enrolment/Edition/Cohort history;
- archive date must not be treated as entitlement expiry without Entitlements policy.

The exact participant-facing access after archive belongs Pass 5 and concrete Edition policy.

## 35.10 External operational objects remain linked consequences, not Edition/Cohort authority

Edition/Cohort may reference:

- Commerce product/offer configuration;
- Entitlements scope;
- Community destination;
- Events/Live sessions;
- Communications templates/schedules.

Those owners remain authoritative.

A Community group, Facebook group, live-session occurrence or Commerce product cannot substitute for Cohort/Edition identity.

---

# 36. Pass-4 pressure tests

## PRG-PT-079 — Baseline scheduled Nuwe Jy Edition with one Cohort

**Scenario class:** minimum flagship model.

**Scenario:** approved Nuwe Jy ProgrammeVersion V1 → Edition E1 → Cohort C1. E1 defines the 60-day release calendar, timezone, windows and supporting configuration. Participants enrol into C1.

**Expected invariants:**

- E1 is explicitly bound to V1;
- C1 is distinct from E1;
- E1 owns the shared schedule contract;
- C1 groups participant delivery under that contract;
- enrolments retain their own lifecycle/history.

**Disposition:** `PASS`.

**FP-008 relevance:** this is sufficient as the first concrete acceptance-test topology.

---

## PRG-PT-080 — One Edition has two parallel Cohorts on the same release calendar

**Scenario class:** explicit cardinality.

**Scenario:** E1 has C1 and C2 for operational grouping, but both are intended to participate in the same 60-day Edition schedule.

**Expected invariants:**

- both Cohorts reference E1;
- neither creates a conflicting release calendar;
- participant “current day” resolves from the same Edition schedule;
- different cohort labels/assignments do not alter ProgrammeVersion or Edition schedule semantics.

**Analysis:** Product explicitly allows one or more Cohorts while placing release dates/timezone on ChallengeEdition.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Refinement:** exact facilitator/capacity/community/live allocation per Cohort remains OQ-026/JIT.

---

## PRG-PT-081 — Two Cohorts under one Edition use different release dates

**Scenario class:** competing schedule authority.

**Scenario:** C1 starts on 1 March; C2 starts on 15 March, but both remain under E1.

**Expected invariant:** one Edition cannot have two contradictory values for Edition-owned start/release dates.

**Analysis:** this would create a second Cohort schedule authority not present in Product Law.

**Disposition:** `REJECT_CURRENT_MODEL`.

**Working route:** use separate Editions for materially different release calendars unless Product Law is explicitly amended to introduce per-Cohort schedule overrides.

---

## PRG-PT-082 — Cohort overrides Edition timezone

**Scenario class:** schedule divergence.

**Scenario:** E1 is configured for Africa/Johannesburg, while C2 independently releases against Europe/London.

**Expected invariant:** Edition timezone remains the governed release-calendar basis.

**Disposition:** `REJECT_CURRENT_MODEL`.

**Working route:** a materially different timezone-driven schedule belongs a separate Edition under current authority.

---

## PRG-PT-083 — Same ProgrammeVersion, different scheduling/support/community rules

**Scenario class:** Edition identity boundary.

**Scenario:** V1 is delivered once as a scheduled, facilitated flagship experience and later as an evergreen/self-paced experience with different support/community rules.

**Expected invariants:**

- both deliveries may reuse V1 if programme semantics are unchanged;
- the different delivery configurations are distinct Editions/configurations;
- no new ProgrammeVersion is manufactured merely for delivery-operation differences.

**Analysis:** Product §21H.2 explicitly anticipates a later evergreen Edition reusing an approved ProgrammeVersion with different scheduling/support/community rules.

**Disposition:** `PASS`.

---

## PRG-PT-084 — Per-Cohort facilitator assignment under one Edition

**Scenario class:** operational allocation.

**Scenario:** E1 has two parallel Cohorts and different facilitators cover each group.

**Expected invariants:**

- Programmes remains Edition/Cohort owner;
- facilitator identity/assignment does not create a second schedule;
- saleable capacity/support coverage remains governed and validated;
- implementation must not invent allocation rules before OQ-026.

**Disposition:** `DEFER_TO_OQ_026 / JIT`.

**Gap promotion:** NONE; existing authority already routes this question.

---

## PRG-PT-085 — Edition capacity versus Cohort capacity

**Scenario class:** saleable capacity authority.

**Scenario:** ChallengeEdition defines `capacity`, while OQ-026 explicitly requires `cohort capacity`. Implementation must decide whether capacity is Edition-total, per-Cohort or both.

**Expected invariants:**

- capacity cannot be guessed;
- sale must fail closed against the finally approved capacity contract;
- capacity must not be derived from Community member count or payment provider data.

**Analysis:** current Product configuration and OQ-026 intentionally leave exact operational allocation for review.

**Disposition:** `DEFER_TO_OQ_026`.

**Gap promotion:** NONE.

---

## PRG-PT-086 — Scheduled flagship Edition with no Cohort

**Scenario class:** delivery-mode contradiction.

**Scenario:** E1 is configured as scheduled Nuwe Jy but enrolments attach directly to Edition with no Cohort concept.

**Expected invariants:** flagship scheduled delivery uses a shared Cohort context.

**Analysis:** `DEC-198`, §21H.2 and FP-008 all require scheduled-cohort delivery.

**Disposition:** `REJECT` for scheduled Nuwe Jy.

---

## PRG-PT-087 — Evergreen self-paced Edition creates a fake Cohort for every participant

**Scenario class:** YAGNI/model distortion.

**Scenario:** a future evergreen Edition gives every self-paced enrolment its own Cohort so the schema always has one.

**Expected invariants:**

- Cohort exists only where shared participant grouping/delivery context is meaningful;
- self-paced participant timing is not relabelled as a “cohort”.

**Disposition:** `REJECT / DEFER_YAGNI`.

---

## PRG-PT-088 — Simple evergreen programme forced to have Edition despite no Edition-specific truth

**Scenario class:** universal-abstraction pressure.

**Scenario:** a future reusable evergreen programme has one approved ProgrammeVersion, direct entitlement and self-paced enrolment, with no edition-specific windows/schedule/support/community configuration. Implementation creates an Edition solely because Nuwe Jy has one.

**Expected invariant:** do not create durable business concepts without distinct business truth.

**Analysis:** generic Product hierarchy does not universally require Edition.

**Disposition:** `DEFER_YAGNI` — Edition is not proven universal.

---

## PRG-PT-089 — Rebind an unlaunched Edition to another approved ProgrammeVersion before commitment

**Scenario class:** pre-activation configuration.

**Scenario:** E1 is still internal configuration, no sale/redemption/enrolment/participant commitment exists, and Product chooses V2 instead of V1 before activation.

**Expected invariants:**

- V2 must itself be approved;
- the Edition must be revalidated against V2;
- no historical participant record is rewritten because none exists;
- exact draft/config-edit mechanics remain JIT.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Boundary:** this does not authorise silent rebind after participant commitment/activation.

---

## PRG-PT-090 — Rebind an activated Edition to a newer ProgrammeVersion

**Scenario class:** historical version integrity.

**Scenario:** E1/V1 is active. V2 is approved. Operator edits E1.source_version to V2.

**Expected invariants:**

- active enrolments remain on V1 unless governed migration/safety correction applies;
- E1’s original source-version provenance remains explainable;
- future V2 delivery uses a governed successor Edition/configuration rather than destructive rebind.

**Disposition:** `PASS` — in-place rebind rejected.

---

## PRG-PT-091 — “Latest approved ProgrammeVersion” changes during an Edition

**Scenario class:** floating pointer.

**Scenario:** E1 references V1. V2 becomes the latest approved version while E1 continues selling/enrolling within its configured window.

**Expected invariants:**

- E1 continues to use V1;
- a participant joining E1 gets V1;
- V2 does not silently change E1 merely because it is latest.

**Disposition:** `PASS`.

---

## PRG-PT-092 — Release calendar edited before activation with no participant commitment

**Scenario class:** normal configuration correction.

**Scenario:** an internal Edition has an incorrect start/release date before activation and before sale/redemption/enrolment.

**Expected invariants:**

- correction is allowed only inside the pre-commit configuration boundary;
- the full Edition readiness validation is rerun;
- scheduled communications/live/community dependencies are checked against corrected dates.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Implementation note:** exact edit/freeze mechanics remain JIT.

---

## PRG-PT-093 — Postpone a sold/enrolled Edition before start

**Scenario class:** exceptional scheduled-product lifecycle.

**Scenario:** participants have bought/redeemed/enrolled against E1, but a facilitator/venue/provider/safety/content problem requires moving the start date.

**Expected invariants:**

- no silent rewrite of the promised schedule;
- participant-facing effect is explicit;
- Edition/Enrolment history is retained;
- Commerce/Entitlements/Events/Community/Communications consequences remain owner-mediated;
- duplicate operator execution cannot multiply consequences.

**Analysis:** current Programme/Nuwe Jy Product Law does not define the participant/commercial/access consequence.

**Disposition:** `INSUFFICIENT_AUTHORITY`.

**Route:** confirms narrowed `PRG-GAP-003` / `PRG-UPD-001`.

---

## PRG-PT-094 — Cancel a sold Edition before start

**Scenario class:** exceptional scheduled-product lifecycle.

**Scenario:** E1 cannot run at all after sale/redemption/enrolment.

**Expected invariants:**

- Edition/Enrolment records are not deleted;
- Programmes does not invent refund/credit/access policy;
- participant outcome and future eligibility remain explicit;
- linked live/community/communications consequences are requested from owners.

**Disposition:** `INSUFFICIENT_AUTHORITY`.

**Route:** confirms narrowed `PRG-GAP-003` / `PRG-UPD-001`.

---

## PRG-PT-095 — Cancel an Edition mid-run

**Scenario class:** exceptional active lifecycle.

**Scenario:** E1 reaches day 23 and must stop because of safety/content/operational failure.

**Expected invariants:**

- prior participation/evidence remains historically valid;
- elapsed time does not fabricate completion;
- any substitute/waiver/completion/recovery outcome needs governed policy;
- access/commercial remedy remains separately owned.

**Disposition:** `INSUFFICIENT_AUTHORITY`.

**Route:** `PRG-UPD-001` plus later Pass 8/9/10 where participant-obligation consequences intersect.

---

## PRG-PT-096 — Participant transfers between Cohorts under the same Edition

**Scenario class:** optional transfer capability.

**Scenario:** E1 has C1/C2 on the same schedule; participant asks to move from C1 to C2.

**Expected invariants if ever supported:**

- source history remains;
- no duplicate enrolment/completion/access consequence;
- capacity/facilitation remains valid;
- transfer is explicit and auditable.

**Analysis:** no approved Product outcome currently requires this operator action for FP-008.

**Disposition:** `DEFER_YAGNI`.

**Rule:** do not build a generic Cohort-transfer action unless Product/operations explicitly requires it.

---

## PRG-PT-097 — Participant transfers to another Edition using the same ProgrammeVersion

**Scenario class:** optional Edition transfer.

**Scenario:** participant wants to move from E1/V1 to later E2/V1.

**Expected invariants if ever supported:** source Edition/Cohort history must remain; target schedule/deadline/capacity and commercial/access consequences must be explicit.

**Analysis:** this is not ordinary Enrolment editing and is not currently approved as a required FP-008 capability.

**Disposition:** `DEFER_YAGNI`.

---

## PRG-PT-098 — Participant transfers to another Edition using a different ProgrammeVersion

**Scenario class:** transfer plus version migration.

**Scenario:** participant moves from E1/V1 to E2/V2.

**Expected invariants:**

- this cannot be treated as a simple Cohort reassignment;
- ProgrammeVersion migration semantics and explicit progress mapping apply;
- transfer/access/commercial consequences also require policy.

**Disposition:** `INSUFFICIENT_AUTHORITY_IF_REQUIRED / OTHERWISE_DEFER_YAGNI`.

---

## PRG-PT-099 — Merge two Cohorts

**Scenario class:** speculative operator lifecycle.

**Scenario:** low enrolment causes C1/C2 to be merged.

**Expected invariants if ever supported:** participant grouping history, facilitation/community/live links and capacity consequences remain explainable.

**Analysis:** no current FP-008 outcome requires Cohort merge.

**Disposition:** `DEFER_YAGNI`.

---

## PRG-PT-100 — Late enrollee receives a personal day-1 schedule

**Scenario class:** schedule authority violation.

**Scenario:** participant enrols on Edition day 17; system starts a private day 1 because her Enrolment is new.

**Expected invariants:** participant joins current shared day; missed material uses guided catch-up; notification starts at enrolment; no private rolling 60-day schedule is fabricated.

**Disposition:** `PASS` — personal schedule rejected.

---

## PRG-PT-101 — Cohort formally concludes while participant catch-up remains open

**Scenario class:** lifecycle-dimension separation.

**Scenario:** shared 60-day run ends, but an approved catch-up window remains and participant has required work outstanding.

**Expected invariants:**

- Cohort conclusion does not auto-complete Enrolment;
- participant history remains active/incomplete/catch-up as governed;
- completion deadline/catch-up window remain Edition configuration;
- ordinary delay does not trigger punitive reset.

**Disposition:** `PASS`.

---

## PRG-PT-102 — Edition archive deletes old Cohort/Enrolment history

**Scenario class:** historical integrity.

**Scenario:** Edition reaches archive date and implementation deletes or rewrites Cohort/Enrolment records.

**Expected invariants:** archive is not deletion; historical participation/version/delivery provenance remains explainable subject to privacy/retention law.

**Disposition:** `PASS` — destructive archive rejected.

**Deferred:** current protected access after archive belongs Pass 5.

---

## PRG-PT-103 — Community/Facebook group is used as Cohort identity

**Scenario class:** cross-domain authority collapse.

**Scenario:** C1’s “ID” is effectively the Facebook group or future Community group.

**Expected invariants:** Programmes owns Cohort; Community owns group/membership/posts/moderation; external/community state cannot become programme schedule/enrolment authority.

**Disposition:** `PASS` — collapse rejected.

---

## PRG-PT-104 — Cohort community becomes unavailable

**Scenario class:** external/community failure.

**Scenario:** Facebook group is disabled or future Community space is unavailable while E1/C1 continues.

**Expected invariants:**

- Cohort/Edition still exist;
- programme schedule/history is not erased;
- Community/operations determine the approved community consequence;
- participant completion is not fabricated from provider state.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** OQ-023/OQ-026 where operational policy is needed.

---

## PRG-PT-105 — Live session occurrence becomes Cohort schedule authority

**Scenario class:** Events/Programme collapse.

**Scenario:** implementation derives Cohort day/state from live-session occurrence records.

**Expected invariants:** Events owns occurrences/registration/attendance; Edition owns the programme release schedule; live sessions are linked supporting events.

**Disposition:** `PASS` — authority inversion rejected.

---

## PRG-PT-106 — Edition is represented by the Commerce product record

**Scenario class:** commercial/delivery collapse.

**Scenario:** because E1 has pricing product, sales window and entitlements, Commerce product becomes the Edition identity.

**Expected invariants:** Commerce owns commercial product/offer/payment truth; Entitlements owns access; Programmes owns Edition.

**Disposition:** `PASS` — collapse rejected.

---

## PRG-PT-107 — Activate Edition with missing readiness dependency

**Scenario class:** activation fail-closed.

**Scenario:** release dates exist but required translation/facilitator/community/communication readiness fails validation.

**Expected invariant:** Edition activation must not fabricate readiness.

**Disposition:** `PASS` — fail closed until the applicable blocking gate is satisfied.

---

## PRG-PT-108 — Copy Programme catalogue lifecycle onto Edition/Cohort

**Scenario class:** lifecycle over-generalisation.

**Scenario:** implementation gives Edition and Cohort `draft → internal → pilot → public → paused → retired` because Programme uses those states.

**Expected invariant:** lifecycle dimensions remain separate; Product Law does not authorise identical Edition/Cohort state machines.

**Disposition:** `REJECT / DEFER_YAGNI`.

**JIT rule:** model only required checkpoints/actions evidenced by Edition/Cohort law.

---

## PRG-PT-109 — Cohort current day is days-since-enrolment

**Scenario class:** duplicate schedule authority.

**Scenario:** each Enrolment calculates cohort day from its own enrolment timestamp.

**Expected invariant:** Cohort day follows the shared Edition schedule.

**Disposition:** `PASS` — duplicate personal clock rejected.

---

## PRG-PT-110 — Add a second Cohort after Edition activation

**Scenario class:** capacity/operational mutation.

**Scenario:** E1 was activated with C1 and validated support/capacity. Operations later wants C2 under the same shared schedule.

**Expected invariants:**

- no schedule divergence;
- capacity/facilitator/moderator/support/live/community readiness must remain valid;
- the additional Cohort cannot bypass the original activation gate.

**Analysis:** Product permits one-or-more Cohorts, but exact late Cohort creation/capacity revalidation is not defined and belongs OQ-026/JIT if the concrete operation is required.

**Disposition:** `DEFER_TO_OQ_026 / JIT`.

**FP-008 rule:** the first acceptance test does not require this operation.

---

## PRG-PT-111 — Multiple Cohorts demand separate community rules under one Edition

**Scenario class:** policy divergence.

**Scenario:** C1/C2 need materially different community/support policies while remaining in E1.

**Expected invariant:** Edition is the delivery-policy envelope; per-Cohort operational assignment must not silently become a second Edition policy layer.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Working rule:** ordinary assignment differences may be resolved by OQ-026; materially different support/community rules should use a separate Edition or explicit Product review.

---

## PRG-PT-112 — Archive date automatically ends Entitlement

**Scenario class:** Edition/access lifecycle conflation.

**Scenario:** E1 reaches archive date and Programmes revokes entitlement.

**Expected invariants:** Programmes owns Edition lifecycle; Entitlements owns access expiry/revocation; archive date alone cannot mutate entitlement unless explicit entitlement policy says so.

**Disposition:** `PASS` for ownership boundary / `DEFER_TO_PASS_5` for participant access behaviour.

---

## PRG-PT-113 — Different Cohorts under one Edition use different ProgrammeVersions

**Scenario class:** version authority split.

**Scenario:** E1 is created from V1; C1 follows V1 but C2 under the same E1 is configured against V2.

**Expected invariants:**

- Edition has one explicit source ProgrammeVersion;
- Cohort cannot override that source version;
- participants in the same Edition must not receive contradictory ProgrammeVersion semantics through Cohort configuration.

**Disposition:** `REJECT_CURRENT_MODEL`.

**Working route:** a different ProgrammeVersion requires a separately governed Edition/configuration or explicit migration path.

---

## PRG-PT-114 — Cohort overrides Edition late-enrolment policy

**Scenario class:** policy authority split.

**Scenario:** E1 declares `closed_at_start`, but C2 independently allows late enrolment.

**Expected invariants:**

- late-enrolment policy is Edition-specific under Product §21H.15 / DEC-212;
- Cohort cannot silently override the Edition contract;
- any different policy is a different Edition policy or explicit future Product amendment.

**Disposition:** `PASS` — Cohort override rejected.

---

## PRG-PT-115 — Cohort independently extends completion/catch-up/archive dates

**Scenario class:** deadline authority split.

**Scenario:** E1 defines completion deadline, catch-up window and archive date, but C2 independently extends those dates for the whole Cohort.

**Expected invariants:**

- Edition remains the configured deadline/window authority;
- participant-specific exception/recovery semantics cannot be smuggled in as a Cohort-wide override;
- an Edition-wide postponement/extension after participant commitment is an exceptional lifecycle change, not ordinary Cohort configuration.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Deferred:** participant-specific exemptions/substitutions/recovery remain Pass 9/10; Edition-wide reschedule/cancellation remains `PRG-UPD-001`.

# 37. Pass-4 gap adjudication

## PRG-GAP-003 — Exceptional Edition/Cohort lifecycle — confirmed and narrowed by Pass 4

Bootstrap classification: `PRODUCT_AUTHORITY_GAP`.

Pass 4 dedicated pressure testing confirms the gap is real, but the earlier scope was too broad.

### Confirmed minimum missing Product semantic

For a **sellable scheduled Edition**, Product authority must define the participant-facing outcome when the Edition:

- must be postponed after participants have committed; or
- must be cancelled before start or mid-run.

At minimum the governed policy must decide:

- whether the Edition is rescheduled, terminated or replaced;
- what happens to existing Enrolment history;
- whether participants remain associated with the original Edition/Cohort for history;
- how completion/catch-up deadlines are treated at the programme level;
- what owner-mediated requests go to Commerce, Entitlements, Events, Community and Communications;
- what participant communication/visibility is required;
- how repeated/retried operator execution remains one logical transition.

The policy must **not** let Programmes invent refund/credit/access truth owned elsewhere.

### Explicitly not justified as mandatory initial capability

The following bootstrap items are now narrowed to `DEFER_YAGNI` unless a concrete Product/operations requirement appears:

- participant transfer between Cohorts;
- participant transfer between Editions;
- automatic Cohort merge;
- generic bulk reallocation;
- a generic Edition/Cohort lifecycle engine covering every hypothetical exceptional state.

If a transfer to a different ProgrammeVersion is later required, it additionally invokes the already-governed ProgrammeVersion migration boundary.

### Why this is FP-008 relevant

A scheduled paid cohort can encounter real pre-start or mid-run inability to deliver because of safety/content/operational failure. “Never happens” is not a safe Product contract.

Roadmap already blocks Edition activation/sale on operational readiness (`OQ-026`) but does not define cancellation/postponement consequences.

Therefore the **minimum cancellation/postponement policy** remains an upstream Product concern before a sellable FP-008 Edition relies on those operator actions.

### Status

`OPEN / CONFIRMED / NARROWED`

No new `PRG-GAP-###` is created in Pass 4.

## Edition/Cohort responsibility ambiguity from PRG-PT-033 — resolved without a new gap

Pass 1 deferred the question because Product placed schedule-oriented configuration on ChallengeEdition while also allowing one-or-more Cohorts.

Pass 4 resolves the semantic split conservatively:

- Edition owns the participant-facing delivery schedule/configuration contract;
- Cohort is the participant grouping/shared context under that Edition;
- multiple Cohorts share the Edition schedule unless future Product Law explicitly authorises cohort-level schedule override;
- exact operational allocation of capacity/facilitators/moderation/support/live/archive responsibility remains OQ-026.

No upstream Product delta is required for the first one-Edition/one-Cohort FP-008 acceptance test.

---

# 38. Pass-4 upstream delta adjudication

## PRG-UPD-001 — Scheduled programme Edition/Cohort exceptional lifecycle contract — CONFIRMED / NARROWED

Earlier bootstrap wording bundled cancellation/postponement with transfer/merge.

Pass 4 replaces that broad working direction with this narrower requirement:

### Product delta that is genuinely justified

Before a sellable scheduled FP-008 Edition implements exceptional operator actions, Product authority must define **minimum cancellation/postponement semantics** for:

1. cancellation before start after participant commitment;
2. postponement/reschedule after participant commitment;
3. cancellation/termination after the Edition has started.

The Product rule should state participant/programme consequences while preserving Domain ownership:

- Programmes: Edition/Cohort/Enrolment historical transition;
- Commerce: refund/credit/commercial remedy;
- Entitlements: access consequence;
- Events & Live: session/occurrence consequences;
- Community: community-space consequence;
- Communications: participant notices/delivery;
- Safety/Content: source reason/authority where applicable.

### Product delta not justified now

Do **not** promote a generic rule for:

- transfers;
- merges;
- arbitrary Cohort reassignment;
- generic make-up cohorts;
- generic cancellation workflow across all programmes.

Those remain deferred until an approved outcome needs them.

### Status

`CONFIRMED / NARROWED / NOT YET PROMOTED TO AUTHORITATIVE PRODUCT LAW`

Pass 4 creates no new `PRG-UPD-###`.

---

# 39. Pass-4 refinements to earlier working synthesis

Earlier ledgers remain immutable. Once Pass 4 is accepted, these successor refinements govern the working stream.

## PRG-REF-013 — Edition is not universal programme structure

Edition is required for Nuwe Jy and any future programme with genuine Edition-specific delivery truth.

It is not automatically required for every simple evergreen programme.

## PRG-REF-014 — Edition is the Nuwe Jy schedule authority; Cohort is shared participant context

For current Nuwe Jy law, start/release dates/timezone/completion/catch-up/archive schedule belong to Edition configuration.

Cohort must not introduce a competing participant-facing calendar.

## PRG-REF-015 — One Edition may have multiple Cohorts only under the shared Edition contract

The Product cardinality `one or more Cohorts` is preserved.

Multiple Cohorts may represent parallel participant groupings under one Edition schedule.

Materially different schedule/timezone/support/community rules require a separate Edition or explicit Product amendment, not an ad hoc Cohort override.

## PRG-REF-016 — Evergreen self-paced delivery must not manufacture fake Cohorts

Cohort is required by shared scheduled/facilitated delivery context, not by schema convenience.

A later evergreen Edition/programme need not create one-person or perpetual Cohorts without evidence.

## PRG-REF-017 — Edition/Cohort lifecycle must not copy Programme catalogue states

Current authority provides activation validation and dated operational milestones but no general Edition/Cohort lifecycle enum.

Do not import `draft/internal/pilot/public/paused/retired` or an LMS run-state machine without a real requirement.

## PRG-REF-018 — Cohort conclusion/archive do not decide Enrolment completion or Entitlement

A Cohort may conclude while catch-up remains open.

Edition archive does not erase participation and does not itself revoke access.

Completion remains Programme-owned; current access remains Entitlements-owned.

## PRG-REF-019 — PRG-UPD-001 is narrower than the bootstrap version

Cancellation/postponement for a sellable scheduled Edition remains a genuine Product-policy gap.

Transfer/merge/reallocation are not mandatory initial capabilities and are now explicitly `DEFER_YAGNI` unless a concrete requirement appears.

---

# 40. Pass-4 anti-LMS / YAGNI outcome

Pass 4 explicitly rejects:

- a mandatory Cohort for every programme;
- one Cohort per self-paced participant merely to satisfy a schema;
- per-Cohort duplicate release calendars under one Edition;
- arbitrary per-Cohort timezone/schedule overrides without Product authority;
- copying Programme catalogue lifecycle states onto Edition/Cohort;
- using Community/Facebook group identity as Cohort truth;
- using Events occurrence state as Cohort schedule truth;
- using Commerce Product/Offer as Edition identity;
- a generic Cohort transfer/merge engine before a concrete approved need;
- a generic “course run / class section / semester” LMS abstraction beyond NewYou’s approved Edition/Cohort semantics.

Generic LMS cohort/term/class-section infrastructure remains `DEFER_YAGNI`.

---

# 41. Pass-4 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Edition is a governed delivery configuration/envelope over one approved ProgrammeVersion; it is not ProgrammeVersion, Cohort, Commerce Product, Community group or Event.
2. Edition is required for Nuwe Jy but is not proven mandatory for every reusable programme.
3. Cohort is a Programmes-owned shared participant grouping/delivery context for scheduled/facilitated delivery; it is not universal.
4. Nuwe Jy Edition owns the shared start/release-date/timezone/completion/catch-up/archive schedule contract.
5. Cohorts under one Edition share that Edition schedule; Cohort does not gain a second release-calendar authority.
6. Product’s `one or more Cohorts` cardinality is retained; the first FP-008 acceptance test needs only one.
7. Multiple parallel Cohorts may exist under one Edition, but per-Cohort capacity/facilitator/moderator/support/live/archive allocation remains OQ-026.
8. Materially different release calendar/timezone or delivery/support/community policy should be a separate Edition or explicit Product amendment, not an ungoverned Cohort override.
9. Evergreen self-paced delivery must not manufacture fake Cohorts.
10. Edition source ProgrammeVersion does not float to the latest approved version after participant-facing commitment/activation.
11. Normal pre-activation configuration changes require full revalidation; participant-impacting post-commit schedule change is exceptional, not ordinary editing.
12. Current authority does not justify a generic Edition/Cohort state machine; model only evidenced checkpoints/actions.
13. Cohort conclusion does not auto-complete participants; approved catch-up may remain open.
14. Edition archive does not erase history and does not itself revoke Entitlement.
15. Community/Events/Commerce/Entitlements remain separate owners linked to Edition/Cohort; their records cannot become programme authority.
16. `PRG-GAP-003` is confirmed but narrowed to minimum sellable-Edition cancellation/postponement semantics.
17. `PRG-UPD-001` is confirmed/narrowed and remains non-authoritative until governed Product promotion.
18. Cohort/Edition transfer and Cohort merge are not required initial capabilities; they are `DEFER_YAGNI` unless Product/operations explicitly requires them.
19. The earlier Edition/Cohort responsibility ambiguity is resolved enough for the first one-Edition/one-Cohort FP-008 acceptance test without a new Product/Architecture/Domain gap.
20. No new Domain, `PRG-GAP-###` or `PRG-UPD-###` is justified by Pass 4.

**Pass hard stop:** Pass 5 has not started. Entitlement versus enrolment/access lifecycle remains deliberately unexamined beyond ownership boundaries necessary to prevent Edition/Cohort authority leakage.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.
