# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.2.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.2.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 1 — normal participant journey and core semantic vocabulary
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.1.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused discovery pass to the v0.1.0 bootstrap ledger without reopening later semantic areas.

> This is an append-only semantic successor. v0.1.0 remains preserved unchanged and remains the bootstrap/orientation predecessor. Read v0.1.0 first, then this pass. Nothing in this working file overrides Product Law, Architecture Law, Domain Law, Roadmap or current Open Work.

> Nuwe Jy remains the first concrete programme acceptance test. Reusable abstractions must emerge from approved NewYou outcomes, not generic LMS convention.

---

# 10. Pass 1 — Normal participant journey and core semantic vocabulary

## 10.1 Scope hard stop

This pass answers only:

1. what `Programme`, `ProgrammeVersion`, `Edition`, `Cohort`, `Enrolment`, `Entitlement`, `Access` and `Participation` mean at the ordinary participant-journey level;
2. which Domain owns the durable truth for each concept;
3. which lifecycle dimensions must remain separate;
4. what the ordinary Nuwe Jy participant journey proves about those terms; and
5. which vocabulary assumptions must be rejected before later JIT work.

This pass deliberately does **not** decide:

- ProgrammeVersion change classification in detail — Pass 2;
- ContentVersion/translation binding — Pass 3;
- Edition/Cohort cardinality and exceptional lifecycle — Pass 4;
- entitlement lapse/reacquisition behaviour — Pass 5;
- sequencing/release mechanics — Pass 6;
- activity evidence contracts — Pass 7;
- completion thresholds/adjudication — Pass 8;
- exemptions/substitutions — Pass 9;
- recovery/catch-up policy detail — Pass 10;
- later live/community/safety/journal/communications/operator/concurrency/cancellation/analytics questions.

A later-pass issue noticed here is recorded only as a routing note unless it invalidates the vocabulary itself.

---

## 10.2 Pass-1 authority evidence

### PRG-EV-007 — Current authority baseline reconfirmed

At the start of this pass, live `main` remained:

`086ade7b28c000de1c387acb9760e5eb08bb0413`

The current README still routes default platform authority to:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `00_PLATFORM_v1.6.0.md`
- `01_DECISIONS_v1.6.0.md`
- `02_OPEN_WORK_v1.2.59.md`
- `03_ARCHITECTURE_v1.1.1.md`
- `04_DOMAIN_MAP_v1.2.0.md`
- `05_ROADMAP_v1.2.0.md`
- `PLATFORM_OPERATING_MODEL_v1.0.1.md`

The manifest confirms those routed versions. The working ledger remains non-authoritative.

### PRG-EV-008 — Product vocabulary is intentionally split across different lifecycle dimensions

Current Product Law locks:

- `DEC-147`: `Programme → ProgrammeVersion → Module → Lesson → Activity` as the reusable conceptual hierarchy;
- `DEC-148`: programme catalogue lifecycle `draft → internal → pilot → public → paused → retired`;
- `DEC-149`: `evergreen_self_paced`, `scheduled_cohort` and `facilitated_cohort` delivery modes;
- `DEC-150`: programme access follows explicit entitlements;
- `DEC-152`: enrolment attempts, pauses, restarts and completions are preserved;
- `DEC-156`: active enrolments stay on their ProgrammeVersion unless governed migration or safety correction applies.

These decisions do not describe one shared state machine. They describe separate truths that must not be flattened into a single programme/participant status.

### PRG-EV-009 — Enrolment has its own durable participation history

Platform §21F.6 states that a participant may:

`enrol → schedule → begin → pause → resume → complete / abandon → restart`

It further requires:

- every enrolment attempt to be preserved;
- restart to create a new linked enrolment rather than delete or overwrite old progress;
- duplicate simultaneous enrolments in the same ProgrammeVersion to be prevented unless explicitly allowed; and
- restart not to silently consume a new paid entitlement.

Therefore the durable programme participation attempt is the **Enrolment**. Nothing in current authority requires a second generic `ProgrammeParticipation` record merely because the word “participation” is used in Product language.

### PRG-EV-010 — Entitlement and current access are not enrolment

Platform §21F.4 and Domain Law §6.11 establish that Entitlements owns the durable access right, including its scope, provenance, validity, expiry and revocation, and answers current access checks.

Programmes & Challenges owns enrolment/participation history and explicitly does not own commercial entitlement or payment.

Therefore:

- an entitlement may exist before any enrolment exists;
- an enrolment must not manufacture an entitlement;
- historical enrolment/progress does not itself prove current protected access; and
- current access should be understood as a policy decision over authoritative entitlement and other applicable constraints, not as another Programme lifecycle state.

### PRG-EV-011 — Nuwe Jy gives a concrete Edition/Cohort path without making those terms interchangeable

Platform §21H locks the flagship path:

`Nuwe Jy Programme → approved ProgrammeVersion → ChallengeEdition → one or more Cohorts`

A `ChallengeEdition` is created from an approved ProgrammeVersion and carries delivery/operational configuration including edition code, sales/enrolment windows, start date, release dates, timezone, facilitators, live sessions, community destination, capacity, entitlements, pricing product, completion deadline, catch-up window and archive date.

The Cohort is the shared participant delivery context: Nuwe Jy has a shared 60-day schedule, and a permitted late enrollee joins the cohort's **current day** rather than receiving a silently-created personal 60-day schedule.

Edition and Cohort are therefore related but not synonyms.

### PRG-EV-012 — Domain Law confirms the authority boundaries

Current Domain Law assigns Programmes & Challenges ownership of:

- programme definitions/versions;
- programme lifecycle and delivery-mode configuration;
- edition/cohort schedule and enrolment lifecycle;
- progression/completion configuration and outcome;
- Nuwe Jy edition/day configuration and repeat-enrolment history.

It explicitly excludes commercial entitlement/payment, Content bodies, Community moderation/posts, Events registration/tickets, HJP occurrence truth and central Safety/Plans authority.

Entitlements separately owns durable access rights and current access checking.

No new Domain is justified by this vocabulary pass.

---

## 10.3 Refined semantic vocabulary

These are **working discovery meanings**, not proposed database tables, Ash Resources or new Product Law.

### 10.3.1 Programme

**Working meaning:** the stable conceptual/catalogue identity of a structured participation product.

It answers questions such as:

- what programme is this?;
- what is its approved purpose/audience/risk positioning?;
- what catalogue lifecycle is the programme in?; and
- what ProgrammeVersions belong to this programme?

The programme catalogue lifecycle is its own dimension:

`draft → internal → pilot → public → paused → retired`

**Do not infer:**

- `public` means every person has access;
- `paused` means every existing enrolment is paused;
- `retired` means historical enrolments disappear; or
- programme catalogue lifecycle is participant lifecycle.

### 10.3.2 ProgrammeVersion

**Working meaning for this pass:** the participant-history-pinnable version of programme semantics under which an enrolment proceeds.

The minimum conclusion needed here is narrow:

- an active enrolment is tied to its ProgrammeVersion;
- a new approved version does not silently rewrite that enrolment;
- governed migration/safety correction are exceptional paths; and
- historical participation must remain explainable against the version that governed it.

**Not decided in Pass 1:** the exact independent ProgrammeVersion lifecycle, change classifier, publish/approval state machine or content-binding fingerprint. Current authority does not justify inventing those here. Those belong in Pass 2 and Pass 3.

### 10.3.3 Edition

**Working meaning for this pass:** a Programmes-owned delivery configuration of an approved ProgrammeVersion where the concrete product/delivery mode needs such a configured delivery instance.

Nuwe Jy conclusively requires this concept. Its ChallengeEdition binds the approved programme version to the flagship delivery configuration.

**Important narrowing from v0.1.0:** current authority does **not yet prove in this pass** that every generic programme enrolment must belong to an Edition. Nuwe Jy does; the generic necessity/cardinality question is deferred to Pass 4.

An Edition is not:

- the Programme itself;
- the ProgrammeVersion itself;
- a Commerce Product/Offer/Price;
- an Entitlement;
- a Community group; or
- a participant Enrolment.

### 10.3.4 Cohort

**Working meaning for this pass:** a Programmes-owned shared participant delivery context used when a delivery mode genuinely groups participants around shared schedule/facilitation context.

For Nuwe Jy:

- scheduled cohorts are the flagship mode;
- the cohort has a shared 60-calendar-day schedule;
- late enrolment joins the cohort's current day; and
- a later evergreen edition must not be silently forced into personal “cohorts” merely to reuse a schema.

A Cohort is not automatically:

- a Community Space;
- a Communications audience list;
- an Event occurrence;
- an Entitlement scope; or
- an Enrolment.

Those capabilities may reference the cohort while retaining their own authority.

**Deferred to Pass 4:** Product §21H states `ChallengeEdition → one or more Cohorts`, while ChallengeEdition itself carries start date, release dates, timezone, facilitators, community destination and capacity. The exact responsibility split and allowed variability between an Edition and its multiple Cohorts must be pressure-tested separately rather than guessed here.

### 10.3.5 Enrolment

**Working meaning:** the durable participant-specific programme participation attempt/history owned by Programmes & Challenges.

An enrolment:

- is tied to a ProgrammeVersion;
- may be scheduled/begun/paused/resumed/completed/abandoned under governed semantics;
- preserves its history;
- is not overwritten by restart;
- may link to a previous enrolment when restarted/repeated;
- does not silently consume or create commercial access rights; and
- for Nuwe Jy, is associated with the applicable ChallengeEdition/Cohort.

This is the strongest candidate for the durable programme-side answer to “this person is/was participating in this programme delivery.”

### 10.3.6 Participation

**Working meaning:** business/process language describing what occurs under an enrolment and, where relevant, source-domain activity evidence.

**Pass-1 correction:** do **not** infer a generic durable `ProgrammeParticipation` Resource from the noun alone.

Current authority explicitly names `Challenge Participation` for challenge semantics in Domain Law, but the ordinary programme lifecycle is already carried by Enrolment plus source evidence and Programme-owned outcomes. Creating another generic participation authority now would risk overlapping ownership and duplicate state.

Disposition for a generic ProgrammeParticipation resource: **DEFER_YAGNI** until a concrete requirement cannot be represented coherently by Enrolment plus owned source evidence.

### 10.3.7 Entitlement

**Working meaning:** the Entitlements-owned durable right to access an explicitly scoped capability/product, independent of how it was purchased or granted.

It answers:

- what right exists?;
- for whom?;
- from what provenance?;
- with what scope?;
- when is it valid?;
- has it expired/revoked/ended?; and
- may this current access check succeed under current entitlement policy?

Entitlement is not programme progress and not enrolment.

### 10.3.8 Access

**Working meaning for this pass:** the current authorised ability to use a protected capability after consulting the authoritative access/entitlement state and any other applicable gate.

Access is a **decision/result**, not evidence that NewYou needs a new generic Programmes-owned `Access` lifecycle/resource.

Examples:

- a purchased programme entitlement may permit protected programme access;
- membership-only programme access may end when membership ends while programme history remains;
- full deletion ends participant access even if restricted financial history remains.

The detailed consequences of access loss/restoration during an active enrolment are deliberately deferred to Pass 5.

---

## 10.4 Normal Nuwe Jy participant journey — authority-preserving view

The ordinary journey can be stated without merging Domain authorities:

```text
Nuwe Jy Programme exists in the approved catalogue
        |
        v
approved ProgrammeVersion exists
        |
        v
ChallengeEdition is configured and validated from that ProgrammeVersion
        |
        v
one or more scheduled Cohorts provide the shared delivery context

Commercial / grant path (separate authority):
Commerce purchase/grant reason
        |
        v
Entitlements creates/holds the participant's applicable access right
        |
        v
recipient is redeemed / participant identity is established

Participation path:
required account / age / consent / safety / language / temperament readiness
        |
        v
Enrolment is created under the applicable ProgrammeVersion + Nuwe Jy delivery context
        |
        v
participant begins
        |
        v
programme availability follows the shared edition/cohort schedule
        |
        v
source Domains accumulate their own authoritative activity evidence
        |
        v
Programmes records/derives its own progression and participation outcome from accepted evidence
        |
        v
pause / resume / ordinary missed work / guided catch-up may occur
        |
        v
cohort may formally conclude while an approved catch-up window remains open
        |
        v
completion/participation outcome is evaluated under the applicable versioned programme rules
        |
        v
historical enrolment/version/delivery provenance remains explainable
```

This diagram is conceptual only. It does **not** prescribe transactions, events, jobs, Resources, database foreign keys or orchestration implementation.

### Boundary assertions for the happy path

The journey must preserve all of these distinctions:

```text
programme public             != participant entitled
participant entitled         != participant enrolled
participant enrolled         != current protected access guaranteed forever
programme version approved   != active enrolment auto-migrated
edition                      != commerce product/offer
edition                      != cohort
cohort                       != community group
cohort membership/context    != community membership
cohort day                   != days since participant enrolled
restart                      != mutation of old enrolment
completion                   != entitlement expiry
purchaser                    != participant
programme participation      != source-domain activity authority
```

These are not implementation preferences. They follow from the current ownership and historical-preservation rules.

---

# 11. Pass-1 focused pressure tests

## PRG-PT-029 — Programme lifecycle is not participant lifecycle

**Scenario class:** vocabulary/lifecycle separation.

**Scenario:** Nuwe Jy Programme is public; one edition is active; one participant is enrolled and paused; another has completed; a third has an entitlement but has never enrolled.

**Pressure:** model all of this using a single `programme_status` or single participant `status` copied from programme state.

**Expected invariants:**

- programme catalogue lifecycle remains programme truth;
- enrolment lifecycle remains participant attempt truth;
- entitlement/access remains Entitlements truth;
- edition/cohort context remains separate;
- one dimension changing does not implicitly rewrite the others.

**Analysis:** a mega-status cannot express the approved scenario without conflating owners and destroying history.

**Disposition:** `PASS` — separate lifecycle dimensions are required.

**Rejected model:** one universal `status` enum spanning programme publication, entitlement, enrolment and cohort delivery.

---

## PRG-PT-030 — Entitled participant never enrols

**Scenario class:** access versus participation.

**Scenario:** a participant receives a valid Nuwe Jy entitlement but never completes enrolment/onboarding and never begins the programme.

**Expected invariants:**

- entitlement remains an Entitlements-owned right according to its policy;
- no completed/active enrolment is fabricated merely because the right exists;
- programme participation analytics cannot count entitlement as participation without a defined derived measurement rule.

**Analysis:** entitlement and enrolment have independent existence.

**Disposition:** `PASS`.

---

## PRG-PT-031 — Enrolment history exists without assuming current access

**Scenario class:** participation history versus current access.

**Scenario:** an enrolment exists historically, but current access is not assumed from that fact alone.

**Expected invariants:**

- Programmes preserves the enrolment/history;
- current access is answered through the owning access/entitlement policy;
- Programmes does not convert historical participation into a new entitlement.

**Analysis:** the vocabulary boundary is sufficiently governed. The participant-facing behaviour after entitlement lapse/reinstatement remains Pass 5.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Deferred:** exact pause/withdraw/catch-up/restoration consequences.

---

## PRG-PT-032 — Late Nuwe Jy enrollee joins current cohort day

**Scenario class:** scheduled delivery semantics.

**Scenario:** an edition permits late enrolment and a participant enrols after the cohort has started.

**Expected invariants:**

- enrolment is created at the actual enrolment time;
- participant joins the cohort's current day;
- daily release remains tied to the cohort schedule;
- missed material routes to guided catch-up;
- NewYou does not create a hidden personal 60-day cohort/schedule for the late enrollee.

**Analysis:** current Product Law is explicit.

**Disposition:** `PASS`.

**Important vocabulary consequence:** `cohort day` is not `enrolment age`.

---

## PRG-PT-033 — One Edition to multiple Cohorts

**Scenario class:** Edition/Cohort responsibility boundary.

**Scenario:** Product §21H permits a ChallengeEdition to lead to one or more Cohorts, while the ChallengeEdition itself declares schedule-oriented configuration such as start date, release dates, timezone, facilitators, community destination and capacity.

**Pressure:** decide now whether Cohort duplicates, overrides, partitions or merely groups the Edition configuration.

**Expected invariant:** no duplicated/conflicting schedule authority may be invented.

**Analysis:** current Product Law proves both concepts exist and are not synonymous, but Pass 1 does not have enough basis to freeze the detailed responsibility split or cardinality constraints.

**Disposition:** `INSUFFICIENT_AUTHORITY_FOR_DETAIL / DEFER_TO_PASS_4`.

**Gap promotion:** NONE in this pass. First exhaust the dedicated Edition/Cohort pass before deciding whether Product authority is genuinely missing.

---

## PRG-PT-034 — Cohort modelled as Community group

**Scenario class:** cross-domain boundary.

**Scenario:** because each flagship edition has a cohort community, implementation proposes using the Community group as the cohort identity/source of truth.

**Expected invariants:**

- Programmes owns Cohort;
- Community owns community space/membership/posts/moderation;
- the community space may reference a cohort but cannot become programme enrolment/schedule authority;
- external Facebook cannot become durable programme truth.

**Analysis:** current Domain Law already rejects the collapse.

**Disposition:** `PASS` — boundary clear; proposed collapse rejected.

---

## PRG-PT-035 — Introduce generic ProgrammeParticipation resource

**Scenario class:** YAGNI/domain duplication.

**Scenario:** implementation proposes `ProgrammeParticipation` alongside `Enrolment` because Product language sometimes says “participation”.

**Expected invariants:** one authoritative owner/record for each durable business truth; no second resource without distinct business lifecycle/meaning.

**Analysis:** ordinary programme participation attempt/history is already represented conceptually by Enrolment. Source Domains own activity occurrence evidence. Domain Law separately names Challenge Participation where challenge semantics require it. No current approved outcome demonstrates a distinct generic ProgrammeParticipation lifecycle.

**Disposition:** `DEFER_YAGNI`.

**Promotion condition:** only revisit if a later concrete programme requirement demonstrates durable participation truth that is neither Enrolment nor source-domain evidence nor Challenge Participation.

---

## PRG-PT-036 — Restart mutates the existing enrolment

**Scenario class:** historical integrity.

**Scenario:** participant abandons or completes an attempt and later restarts; implementation resets the old Enrolment to “active” and clears/reuses its progress.

**Expected invariants:** restart creates a new linked Enrolment; old progress/history remains preserved; new participation does not silently consume a new paid entitlement.

**Analysis:** Product Law is explicit.

**Disposition:** `PASS` — mutation model rejected.

---

## PRG-PT-037 — Enrolment creates entitlement

**Scenario class:** authority inversion.

**Scenario:** an enrol action inserts/grants programme access because the enrolment “needs access”.

**Expected invariants:** Programmes cannot manufacture commercial/access authority; Entitlements owns grants/revocation/expiry and current access.

**Analysis:** cross-domain ownership is explicit.

**Disposition:** `PASS` — direct entitlement manufacture by Programmes rejected.

---

## PRG-PT-038 — New ProgrammeVersion auto-upgrades active enrolments

**Scenario class:** version pinning/history.

**Scenario:** V2 is approved while a V1 participant is active; “current programme version” lookup silently switches the enrolment to V2.

**Expected invariants:** active enrolment stays on V1 unless governed migration or safety correction applies; completed history never silently changes.

**Analysis:** Product and Domain Law are explicit.

**Disposition:** `PASS` — auto-upgrade rejected.

**Deferred:** exact change/migration semantics belong Pass 2.

---

## PRG-PT-039 — Edition treated as Commerce Product/Offer

**Scenario class:** commercial/delivery boundary.

**Scenario:** because the Nuwe Jy ChallengeEdition references pricing product, entitlements and sales window, implementation proposes making the Commerce product record the Edition authority.

**Expected invariants:**

- Programmes owns Edition and its delivery configuration;
- Commerce owns product/offer/pricing/purchase/payment;
- Entitlements owns access rights;
- references between them do not transfer authority.

**Analysis:** `pricing product` and `entitlements` are fields/relationships in the edition configuration precisely because those concepts remain separately owned.

**Disposition:** `PASS` — authority collapse rejected.

---

## PRG-PT-040 — Nuwe Jy day derived from participant enrolment age

**Scenario class:** scheduled cohort semantics.

**Scenario:** participant joins on cohort day 12; implementation calculates the participant's “programme day” as `today - enrolment_started_at`, showing day 1.

**Expected invariants:** for the flagship scheduled-cohort delivery, the shared cohort schedule is authoritative for the current cohort day; late participant joins current day and receives guided catch-up for missed work.

**Analysis:** Product Law explicitly prohibits silently converting a late cohort entrant to a separate personal 60-day schedule.

**Disposition:** `PASS` — enrolment-age clock rejected for the scheduled flagship.

**Deferred:** evergreen/personal schedule semantics belong later delivery-mode passes.

---

# 12. Pass-1 semantic model — minimum safe distinctions

The minimum vocabulary model NewYou can safely carry into later discovery is:

```text
Programme
  stable conceptual/catalogue identity
  owns catalogue lifecycle

ProgrammeVersion
  version-pinned programme semantics for enrolment/history
  exact version lifecycle/change rules -> Pass 2

Edition
  configured delivery of an approved ProgrammeVersion where needed
  Nuwe Jy definitely requires it
  universal necessity/cardinality -> Pass 4

Cohort
  shared participant delivery context where the mode needs grouping/schedule
  Nuwe Jy definitely requires it
  Edition/Cohort responsibility split -> Pass 4

Enrolment
  durable participant-specific programme attempt/history
  restart/repeat => new linked enrolment

Participation
  business/process term under an Enrolment
  NOT a new generic durable Resource without evidence

Entitlement
  durable right to access, owned by Entitlements

Access
  current authorisation result/policy decision
  NOT a Programmes lifecycle state
```

### Lifecycle separation table

| Dimension | Authoritative owner | What it answers | Must not be collapsed into |
|---|---|---|---|
| Programme catalogue lifecycle | Programmes & Challenges | Is the conceptual programme draft/internal/pilot/public/paused/retired? | Enrolment, Entitlement, Edition operation |
| ProgrammeVersion identity/pinning | Programmes & Challenges | Which programme semantics govern this enrolment/history? | “latest version” lookup, ContentVersion |
| Edition delivery configuration | Programmes & Challenges | Which approved delivery configuration is being operated? | Commerce Product, Cohort, Entitlement |
| Cohort shared context | Programmes & Challenges | Which shared delivery grouping/schedule context applies? | Community group, Event, Enrolment |
| Enrolment lifecycle/history | Programmes & Challenges | What happened in this participant's programme attempt? | Entitlement/access, Programme catalogue state |
| Entitlement right/current access | Entitlements | What scoped access right exists and is it currently usable? | Enrolment/progress |
| Safety state | Safety & Eligibility | What pathway/activity is currently safe/permitted? | Enrolment status |
| Source activity evidence | Owning source Domain | Did the relevant habit/journal/event/etc. fact occur? | Programme-owned shadow evidence store |

This table is semantic only. It does not prescribe separate database tables for every row.

---

# 13. Corrections/refinements to v0.1.0 produced by Pass 1

v0.1.0 remains immutable as the bootstrap record. Pass 1 refines three shorthand statements rather than rewriting them.

## PRG-REF-001 — `Enrolment/participation` shorthand is too loose

v0.1.0 used “Enrolment/participation” together.

**Refinement:** Enrolment is the durable participant-specific programme attempt/history established by Product and Domain Law. `Participation` remains business/process language unless a later concrete requirement proves a distinct durable lifecycle. Do not pre-create a generic ProgrammeParticipation authority.

## PRG-REF-002 — Edition should not yet be mandatory for every programme

v0.1.0 described Edition as reusable delivery configuration.

**Refinement:** this is proven for Nuwe Jy and Edition is a valid Programmes concept generally, but Pass 1 does not prove that every evergreen/self-paced enrolment requires an Edition instance. The dedicated Edition/Cohort pass must establish the minimum generic rule.

## PRG-REF-003 — Edition/Cohort exact responsibility remains deliberately open

v0.1.0 correctly separated Edition from Cohort.

**Refinement:** do not freeze exact Edition↔Cohort cardinality or schedule-field ownership yet. Nuwe Jy Product Law says `ChallengeEdition → one or more Cohorts` while ChallengeEdition itself carries significant schedule/operations configuration. This is a concrete Pass-4 pressure-test target, not permission for JIT to choose arbitrarily.

These refinements do not require an authoritative amendment at this stage.

---

# 14. Pass-1 gap and upstream-delta adjudication

## New Product/Architecture/Domain gap promotion

**NONE.**

Pass 1 found one later-pass ambiguity — the precise Edition/Cohort responsibility split — but it has not yet been subjected to the dedicated Pass-4 pressure tests. Promoting it now would violate the agreed focused-pass method.

## Existing gaps touched but not adjudicated here

- `PRG-GAP-004` entitlement lapse during enrolment remains for Pass 5.
- existing completion gaps remain for Pass 8/9 and OQ-019/OQ-025.
- `PRG-UPD-001` exceptional scheduled-edition/cohort lifecycle remains untouched for the later dedicated pass.

No new `PRG-UPD-###` is created in Pass 1.

---

# 15. Pass-1 anti-LMS/YAGNI outcome

Pass 1 adds one explicit YAGNI rejection:

- generic `ProgrammeParticipation` resource/state machine merely to mirror LMS terminology — `DEFER_YAGNI`.

No evidence in this pass justifies:

- generic course enrolment engines beyond the NewYou enrolment semantics already required;
- tenant/instructor/course abstractions;
- generic LMS access models;
- generic cohort/community coupling;
- generic “course status” mega-state.

The correct pressure is the opposite: keep each durable truth with its owner and require a concrete second use case before broadening the model.

---

# 16. Pass-1 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

The normal participant journey and core vocabulary are coherent enough to proceed to the next discovery pass **later**, with these constraints carried forward:

1. Programme catalogue lifecycle is not participant lifecycle.
2. ProgrammeVersion pins the semantics governing an enrolment; do not silently follow “latest”.
3. Edition and Cohort are real Programmes concepts, but their generic necessity/cardinality/responsibility split is not frozen by this pass.
4. Enrolment is the durable programme participation attempt/history.
5. `Participation` does not justify a duplicate generic resource.
6. Entitlement is the durable access right and belongs to Entitlements.
7. Access is a current authorisation result, not a Programmes-owned lifecycle state.
8. Nuwe Jy's scheduled cohort day is not participant enrolment age.
9. Community group, Commerce product, Event occurrence and Cohort remain separate authorities/concepts even when composed.
10. No new Domain, Product gap or upstream delta is justified by Pass 1.

**Pass hard stop:** Pass 2 has not started. Programme identity/ProgrammeVersion semantics beyond the minimum pinning rule above remain deliberately unexamined in this version.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.