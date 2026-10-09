# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.1.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Created from live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose:** discover the minimum programme, version, edition/cohort, access, participation, sequencing, completion, recovery and cross-domain semantics NewYou genuinely needs before FP-008 / later programme JIT.

> Nuwe Jy is the first concrete programme acceptance test. Reusable abstractions must emerge from approved NewYou outcomes, not from generic LMS convention.

---

## 1. Live authority bootstrap

The live repository was re-read before substantive discovery. The uploaded Project snapshots are older orientation material and are not used as current authority where live repository versions differ.

Current routed authority at the creation head includes:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
- `00_PLATFORM_v1.6.0.md`
- `01_DECISIONS_v1.6.0.md`
- `02_OPEN_WORK_v1.2.59.md`
- `03_ARCHITECTURE_v1.1.1.md`
- `04_DOMAIN_MAP_v1.2.0.md`
- `05_ROADMAP_v1.2.0.md`
- `PLATFORM_OPERATING_MODEL_v1.0.1.md`
- `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` where frontend experience is in scope.

The current Engineering Standards router is supporting authority beneath Product / Architecture / Domain / Roadmap and does not authorise implementation here.

### PRG-EV-001 — Creation-head verification

Live `main` equals the supplied creation-time SHA `086ade7b28c000de1c387acb9760e5eb08bb0413`.

### PRG-EV-002 — Programme hierarchy verification

`DEC-147` remains LOCKED:

`Programme → ProgrammeVersion → Module → Lesson → Activity`.

`DEC-148...DEC-157` additionally lock programme lifecycle, delivery modes, entitlement dependency, guided pacing, enrolment history, activity requirement classes, compassionate recovery, versioned completion rules, version pinning/migration and temperament boundaries.

### PRG-EV-003 — Domain ownership verification

Current Domain Law assigns `Programmes & Challenges` ownership of programme/version structure, edition/cohort/enrolment/progression/completion and Nuwe Jy edition/day configuration. It explicitly does not own content bodies, habit/journal occurrences, entitlement/payment, community moderation, live registration/attendance, or central Safety/Plans truth.

### PRG-EV-004 — Nuwe Jy acceptance-test verification

Current FP-008 says Nuwe Jy is the concrete acceptance test for only the reusable programme/version/edition/cohort primitives NewYou genuinely needs and explicitly defers a generic LMS/page builder and LearnDash importer/converter.

### PRG-EV-005 — Foundation second-lens verification

Current FP-014 follows FP-008 or equivalent programme proof, extends only evidence-backed programme capability, and explicitly defers generic LMS/page-builder scope.

### PRG-EV-006 — Open Product gates verification

`OQ-019` remains PRODUCT REVIEW: programme-specific minimum participation, final check-ins and completion thresholds must be defined before each programme is published.

`OQ-025` remains CLINICAL / PRODUCT REVIEW for Nuwe Jy-specific safety routing, milestone check-ins, required activities and completion rules.

---

## 2. Anti-LMS discovery rule

Every candidate capability is tested against an approved NewYou outcome.

If the only justification is “LMS platforms normally have it”, disposition defaults to `DEFER_YAGNI`.

Current authority already rejects a generic LMS as an FP-008 prerequisite. Therefore this stream does not assume SCORM, xAPI, a generic gradebook, unrestricted page builder, generic quiz builder, arbitrary prerequisite graph, course marketplace, instructor marketplace, generic import engine, arbitrary multi-tenant authoring, points or gamification infrastructure.

Approved bounded capabilities such as compassionate completion certificates, optional approved badges, explicit prerequisites and programme-specific activities do not justify generic engines for those concepts.

---

## 3. Working semantic synthesis

These are discovery conclusions, not implementation schemas or new Product Law.

1. **Programme** is the stable conceptual programme identity.
2. **ProgrammeVersion** is the versioned programme-semantic contract: structure, ordering where meaningful, activity requirement meaning, progression/completion policy references and other participant-facing semantics that must not silently rewrite historical participation.
3. **Edition** is the reusable delivery configuration of one approved ProgrammeVersion. Product Law already permits both scheduled flagship editions and later evergreen editions. An edition may therefore carry schedule/window/support/community/live/communications configuration without forcing all programmes into cohort semantics.
4. **Cohort** is a participant grouping/shared delivery context when the edition actually needs one. Nuwe Jy needs a scheduled cohort; an evergreen self-paced programme does not automatically need a cohort.
5. **Enrolment/participation** is Programme-owned participation history. It is not entitlement and is not payment.
6. **Entitlement** remains Entitlements-owned access authority. Loss of access must not erase programme history.
7. **Activity definition** belongs to Programmes only for programme meaning. The authoritative evidence that an activity happened remains with the owning Domain: journal/habit/progress, Events attendance, Community contribution, Safety outcome, Content version, etc.
8. **Completion outcome** is Programme-owned and must be evaluated under an explicit versioned rule set against accepted evidence. Analytics may derive completion metrics but never decide completion.
9. **Meaningful lifecycle dimensions stay separate.** Programme catalogue lifecycle, ProgrammeVersion identity, edition operation, enrolment/participation, entitlement/access, safety state and source-domain activity state must not be collapsed into one mega-status.
10. **Exact delivered provenance matters.** Years later NewYou must be able to identify programme/version, edition/cohort where applicable, completion rule version, accepted exceptions/corrections and the exact source-domain evidence/version provenance required to explain the outcome without duplicating full source payloads.

### Working content-binding boundary

- Content & Media owns conceptual content, immutable content versions, translations, publication, correction and withdrawal.
- Programmes consumes governed content references; it does not become a second CMS.
- Every actual delivery must retain exact ContentVersion/locale provenance.
- A controlled editorial correction that does not alter programme meaning should not automatically force a new ProgrammeVersion merely because a new ContentVersion exists; the original delivery remains traceable.
- A material change to programme meaning, requiredness, progression, sequencing or completion expectations requires a new ProgrammeVersion.
- A safety correction is the explicit exceptional path already recognised by Domain/Product law for active participation and must preserve before/after provenance.

The exact binding representation and correction mechanism remain JIT/Content-dossier detail; this working boundary must be revalidated there.

---

# 4. Pressure tests

## PRG-PT-001 — Normal participant journey
**Scenario class:** baseline end-to-end participation.

**Relevant Product/Decision authority:** `DEC-147...DEC-157`, `DEC-196...DEC-219`, FP-008.

**Owning Domain(s):** Programmes & Challenges plus Entitlements, Content & Media, Safety & Eligibility, Habits/Journals/Progress, Events & Live, Communications, Community.

**Preconditions:** approved ProgrammeVersion; approved edition where needed; valid content/translation/safety configuration; current entitlement where protected.

**Scenario/timeline:** programme exists → version approved → edition configured → participant entitled → enrols → starts → releases become available → evidence accrues across owning Domains → participant misses work → catches up → edition concludes → completion evaluated → history remains explainable.

**Expected invariants:** enrolment never manufactures entitlement; source Domains retain activity truth; missed work does not erase progress; completion is not inferred from elapsed time/page views; historical version/provenance remains stable.

**Questions:** exact completion threshold and final-check-in requirements remain programme-specific.

**Cross-domain seams:** all listed owners; Audit/Analytics downstream.

**Adversarial variants:** entitlement ends mid-way; safety changes; duplicate release; missed live; language switch.

**Analysis:** current authority supports the journey but leaves exact completion policy deliberately gated.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** Product promotion for OQ-019/OQ-025; JIT; controlled programme; Phase 8 for scheduled/retry paths.

## PRG-PT-002 — ProgrammeVersion change boundary
**Scenario class:** identity/version/history.

**Relevant Product/Decision authority:** DEC-147, DEC-152, DEC-156; Domain Law 6.8.

**Owning Domain(s):** Programmes & Challenges.

**Preconditions:** V1 has active participants; V2 is prepared.

**Scenario/timeline:** typo; translation correction; material lesson rewrite; module reorder; required activity added/removed; completion rule changed; programme retired.

**Expected invariants:** existing participation cannot be silently rewritten; structural/requirement/completion meaning changes create a new ProgrammeVersion; retirement does not erase V1 history.

**Questions:** exact JIT fingerprint/change classifier.

**Cross-domain seams:** Content & Media for content-only corrections; Safety for emergency correction.

**Adversarial variants:** operator edits “current” config in place; new V2 published while V1 cohort active.

**Analysis:** Product/Domain law establishes the semantic boundary strongly enough; exact implementation mechanics remain JIT.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** documentary + JIT.

## PRG-PT-003 — Content correction without duplicate CMS
**Scenario class:** content binding/version provenance.

**Relevant Product/Decision authority:** Content correction/version law; DEC-142; DEC-156; Domain Law Content 6.7 and Programmes 6.8.

**Owning Domain(s):** Content & Media; Programmes & Challenges consumes references.

**Preconditions:** ProgrammeVersion references approved content; cohort has started.

**Scenario/timeline:** typo corrected; English translation corrected; Afrikaans corrected; video replaced; lesson meaning materially changes; content becomes unsafe.

**Expected invariants:** Content remains source authority; exact delivered version/locale remains reconstructible; ordinary editorial correction does not silently mutate historical delivery; material programme-semantic change uses a new ProgrammeVersion; safety correction may replace unsafe delivery under governed exception without erasing history.

**Questions:** exact binding indirection and delivery receipt are JIT; a Content/JIT review must distinguish content-only correction from programme-semantic change.

**Cross-domain seams:** Content publication/withdrawal, Programme delivery, Safety invalidation, Communications where notice is required.

**Adversarial variants:** “latest content” lookup rewrites old cohort experience; one locale changes meaning but the other does not.

**Analysis:** a mutable “always current content” pointer is unsafe; duplicating content payloads into Programmes is also wrong.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** JIT + Content/translation dossier + Phase 8 for safety replacement where material.

## PRG-PT-004 — Edition versus cohort necessity
**Scenario class:** delivery-model boundary.

**Relevant Product/Decision authority:** DEC-149, DEC-198, DEC-211, DEC-212; Platform §21H.

**Owning Domain(s):** Programmes & Challenges.

**Preconditions:** one approved ProgrammeVersion.

**Scenario/timeline:** scheduled Nuwe Jy edition; later evergreen edition; participant-specific start; concurrent scheduled cohorts.

**Expected invariants:** an edition binds delivery configuration to one source ProgrammeVersion; cohort exists only when a shared participant grouping/schedule is actually required; evergreen does not gain fake cohort machinery.

**Questions:** exact Edition↔Cohort cardinality remains JIT and must be derived from concrete programme needs rather than LMS convention.

**Cross-domain seams:** Community, Events, Communications, Entitlements.

**Adversarial variants:** creating a cohort for every individual self-paced participant; treating cohort as Community group.

**Analysis:** Product explicitly names a later evergreen *edition*, so Edition is broader than “cohort”. Cohort is optional delivery context, not universal programme identity.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** documentary + FP-008 JIT.

## PRG-PT-005 — Entitlement versus enrolment
**Scenario class:** access/participation authority.

**Relevant Product/Decision authority:** DEC-150, DEC-152, DEC-210; Domain Law Commerce/Entitlements/Programmes.

**Owning Domain(s):** Entitlements owns access; Programmes owns enrolment.

**Preconditions:** participant may be purchased, sponsored, gifted, membership-included or complimentary.

**Scenario/timeline:** entitlement exists but never enrols; participant enrols; repeat participation occurs; purchaser differs from participant.

**Expected invariants:** entitlement does not imply enrolment; enrolment does not create entitlement; purchaser has no private participation access; repeat enrolment is historical, not overwrite.

**Questions:** none requiring new universal LMS semantics.

**Cross-domain seams:** Commerce, Entitlements, Identity & Access, Programmes.

**Adversarial variants:** duplicate grant plus duplicate enrol request; payer tries to inspect progress.

**Analysis:** boundary is already explicit and strong.

**Disposition:** PASS.

**Proof route:** documentary + JIT + Phase 8 idempotency proof.

## PRG-PT-006 — Entitlement ends during active participation
**Scenario class:** entitlement seam/recovery.

**Relevant Product/Decision authority:** DEC-150/152; Entitlements Domain current-access doctrine; commercial reversal/cancellation law.

**Owning Domain(s):** Entitlements owns current access; Programmes owns participation/history.

**Preconditions:** participant is enrolled and has started.

**Scenario/timeline:** membership ends, refund/reversal occurs, sponsored access revoked or finite access expires while enrolment remains historically valid.

**Expected invariants:** protected access follows current Entitlements truth; historical enrolment/progress is not erased; Programmes does not manufacture continuation access.

**Questions:** whether a specific programme pauses participation, allows a catch-up window, requires a new entitlement, or records withdrawal is product/edition-policy-specific and is not fully declared generically.

**Cross-domain seams:** Entitlements, Commerce, Programmes, Communications.

**Adversarial variants:** entitlement expires during an activity; stale browser submits after revocation; later access is restored.

**Analysis:** authority ownership is clear; the participant-facing continuation policy still needs explicit programme/offer configuration.

**Disposition:** NEEDS_WORKING_DELTA.

**Proof route:** FP-008 JIT and Product promotion only where the programme’s commercial/access promise is not already explicit.

## PRG-PT-007 — Sequencing and release modes
**Scenario class:** delivery sequencing.

**Relevant Product/Decision authority:** DEC-149, DEC-151, DEC-199...DEC-202, DEC-212.

**Owning Domain(s):** Programmes & Challenges.

**Preconditions:** programme/edition declares its mode.

**Scenario/timeline:** all-at-once; date drip; explicit prerequisite; facilitated release; mixed Nuwe Jy daily release; late enrolment/catch-up.

**Expected invariants:** no single universal unlock engine is required; mode is version/edition configuration; scheduled work is durable/idempotent; ordinary delay does not equal failure.

**Questions:** facilitator-release capability should be added only when a concrete programme needs it.

**Cross-domain seams:** Communications for notices; Safety for restrictions.

**Adversarial variants:** duplicate scheduler run; timezone change; reschedule after reminders queued.

**Analysis:** reusable semantics are availability rules plus explicit prerequisite/pacing meaning, not a generic prerequisite graph platform.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** JIT + Phase 8 scheduled-work proof.

## PRG-PT-008 — Activity evidence ownership
**Scenario class:** cross-domain activity evidence.

**Relevant Product/Decision authority:** DEC-153, Domain ownership matrix.

**Owning Domain(s):** source owner per activity; Programmes owns activity definition and completion interpretation.

**Preconditions:** read/watch/live/journal/habit/check-in/practical/community activities may appear.

**Scenario/timeline:** participant completes activity in source Domain; Programmes consumes minimally sufficient evidence.

**Expected invariants:** Content owns content; Events attendance; HJP journal/habit/progress; Community social participation; Safety decisions; Health facts. Programmes never becomes shadow authority for all of them.

**Questions:** exact evidence contract per activity class is JIT.

**Cross-domain seams:** source Domain interfaces and privacy minimisation.

**Adversarial variants:** source record corrected/deleted; duplicate event; stale completion evaluator.

**Analysis:** Programmes may retain its own accepted completion/evidence decision without duplicating raw source payloads.

**Disposition:** PASS.

**Proof route:** documentary + JIT.

## PRG-PT-009 — Completion framework
**Scenario class:** completion semantics.

**Relevant Product/Decision authority:** DEC-153, DEC-155, DEC-199, DEC-217; OQ-019/OQ-025.

**Owning Domain(s):** Programmes & Challenges.

**Preconditions:** ProgrammeVersion has declared completion rules.

**Scenario/timeline:** page opened; required activities completed; live attended; replay substitute; check-in submitted; facilitator evidence; elapsed edition end.

**Expected invariants:** completion is rule-based and versioned; page view/elapsed time alone cannot be silently treated as completion; weight loss, perfection and streaks are forbidden completion criteria; completion survives later programme retirement as history.

**Questions:** exact minimum participation, final check-ins, substitutions and thresholds are unresolved Product decisions.

**Cross-domain seams:** HJP, Events, Content, Safety, Analytics.

**Adversarial variants:** missing one required activity; duplicate evidence; late evidence after cohort end.

**Analysis:** framework shape is known; exact programme rules must not be invented by JIT.

**Disposition:** INSUFFICIENT_AUTHORITY.

**Proof route:** Product promotion through OQ-019/OQ-025, then JIT/controlled programme.

## PRG-PT-010 — Required, optional, conditional, exempt and skipped
**Scenario class:** requirement semantics/exceptions.

**Relevant Product/Decision authority:** DEC-153; HJP occurrence states; OQ-019/OQ-025.

**Owning Domain(s):** Programmes owns requirement/completion meaning; source Domain owns occurrence/evidence.

**Preconditions:** activity may be required-for-progression, required-for-completion, required-for-safety, recommended, optional or conditional.

**Scenario/timeline:** participant intentionally skips; safety blocks; joins late; facilitator proposes an exception; technical failure prevents evidence.

**Expected invariants:** “skipped”, “not applicable”, “safety blocked” and “exempted by authorised rule” are semantically different; safety-required work cannot be waived by ordinary programme admin; optional work must not silently enter denominator.

**Questions:** NewYou has not yet declared a universal exemption/adjudication contract or how each exception affects completion.

**Cross-domain seams:** Safety, HJP, Audit.

**Adversarial variants:** facilitator exempts a safety requirement; exception applied after completion; bulk exemption.

**Analysis:** exact exception semantics belong in OQ-019/OQ-025 for concrete programme rules, not a guessed enum.

**Disposition:** INSUFFICIENT_AUTHORITY.

**Proof route:** Product promotion + JIT.

## PRG-PT-011 — Compassionate recovery
**Scenario class:** recovery/catch-up.

**Relevant Product/Decision authority:** DEC-151, DEC-154, DEC-199, DEC-212; Platform 21F/21H.

**Owning Domain(s):** Programmes & Challenges; source activity owners remain unchanged.

**Preconditions:** participant falls behind due to ordinary life disruption.

**Scenario/timeline:** missed day/week/live → recovery view → catch-up/reschedule/simplification/substitute where approved → programme continues; cohort may conclude while approved individual catch-up remains open.

**Expected invariants:** no punitive reset; no zeroed progress; no false automatic completion at day 60; completion need not require perfect adherence.

**Questions:** exact catch-up window/substitute rules remain programme/edition-specific.

**Cross-domain seams:** Events replay, Communications reminders, Safety substitutions.

**Adversarial variants:** long absence; catch-up after edition end; replay delayed.

**Analysis:** recovery is a first-class programme semantic, not an exception bolted onto a punitive LMS.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** OQ-019/OQ-025 where threshold-affecting; JIT + controlled programme.

## PRG-PT-012 — Live attendance and replay substitution
**Scenario class:** Events/Programme seam.

**Relevant Product/Decision authority:** DEC-186...DEC-190, DEC-206; FP-007/FP-008.

**Owning Domain(s):** Events & Live owns occurrence/attendance; Programmes owns completion meaning.

**Preconditions:** ProgrammeVersion/edition references a live occurrence.

**Scenario/timeline:** scheduled → rescheduled/cancelled → participant attends or misses → replay may become available → Programme evaluates approved equivalent evidence.

**Expected invariants:** Programme never manufactures attendance; replay publication remains governed; “replay substitutes for attendance” is an explicit programme rule, not universal inference.

**Questions:** exact Nuwe Jy attendance/replay requirement belongs OQ-025/OQ-019.

**Cross-domain seams:** Events, Content media/replay, Communications.

**Adversarial variants:** attendance arrives late; session cancelled; extra facilitator session added.

**Analysis:** ownership is clear; equivalence policy remains versioned programme configuration.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** Product gate + JIT + FP-007 proof reuse/new proof as classified.

## PRG-PT-013 — Community contribution as required activity
**Scenario class:** Community/Programme seam.

**Relevant Product/Decision authority:** DEC-205; Community law; OQ-023; FP-008/FP-013.

**Owning Domain(s):** Community owns social participation; Programmes would own completion meaning.

**Preconditions:** Nuwe Jy initially uses governed Facebook; native Community is later.

**Scenario/timeline:** programme proposes “make a community post” as completion-required activity.

**Expected invariants:** external Facebook must not become hidden NewYou business authority; moderator/manual confirmation must not be invented merely to mimic an LMS discussion requirement.

**Questions:** no current Nuwe Jy outcome requires a social post to be completion-critical.

**Cross-domain seams:** Community, Privacy, Programmes.

**Adversarial variants:** participant leaves Facebook; moderation removes post; platform cannot reliably prove external post.

**Analysis:** optional community participation is valid; completion-critical external-post evidence is unjustified at current authority.

**Disposition:** DEFER_YAGNI.

**Proof route:** future Product promotion only if a concrete programme outcome genuinely requires it.

## PRG-PT-014 — Safety change during programme
**Scenario class:** safety/restriction.

**Relevant Product/Decision authority:** DEC-157, DEC-185, DEC-208/209; Safety Domain Law.

**Owning Domain(s):** Safety & Eligibility owns restriction; Programmes interprets impact under programme rules.

**Preconditions:** participant was eligible at start.

**Scenario/timeline:** new safety fact → Safety changes outcome/restriction → one activity or broader programme path may block → safe alternative/catch-up may apply.

**Expected invariants:** Programme cannot override Safety; raw health data need not be copied into Programmes; historical participation remains; a safe alternative must be governed and completion-equivalent only when approved.

**Questions:** Nuwe Jy-specific restriction/substitute/completion consequences belong OQ-025.

**Cross-domain seams:** Health Records, Safety, Plans, Programmes, Communications.

**Adversarial variants:** safety correction after prior completion; stale browser attempts unsafe action.

**Analysis:** keep safety state independent from enrolment lifecycle; derive permitted actions from current Safety authority.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** OQ-025 + JIT + safety/Phase 8 proof.

## PRG-PT-015 — Programme-assigned habit
**Scenario class:** HJP ownership.

**Relevant Product/Decision authority:** DEC-158...DEC-163; FP-014.

**Owning Domain(s):** HJP owns habit/schedule/occurrence; Programmes owns assignment intent/reference and completion interpretation where applicable.

**Preconditions:** programme asks participant to practice a habit.

**Scenario/timeline:** participant already has similar habit; programme suggests/assigns one; habit persists or ends after programme.

**Expected invariants:** no duplicate habit authority in Programmes; existing participant habit is not silently overwritten; programme end does not automatically delete a participant-owned continuing habit.

**Questions:** reuse/link vs create behaviour remains JIT and programme configuration.

**Cross-domain seams:** HJP, Programmes, Communications reminders.

**Adversarial variants:** duplicate assignment retry; programme version changes while habit persists.

**Analysis:** source ownership is clear.

**Disposition:** PASS.

**Proof route:** FP-014 JIT / future controlled programme.

## PRG-PT-016 — Private journal required for programme
**Scenario class:** privacy/journal completion.

**Relevant Product/Decision authority:** DEC-164...DEC-167; HJP Domain Law; OQ-018.

**Owning Domain(s):** HJP owns journal content/share state; Programmes owns requirement/completion meaning.

**Preconditions:** a future programme requires reflection.

**Scenario/timeline:** participant records private reflection; refuses to share content; later deletes entry; Programme needs to know only whether approved evidence was satisfied.

**Expected invariants:** journal is private by default; completion must not require content disclosure merely for programme convenience; Analytics gets no journal text by default; Programmes should consume minimal evidence rather than copy content.

**Questions:** whether deletion of source journal should preserve a minimal previously-accepted programme evidence receipt, and exact retention linkage, require Privacy/JIT resolution.

**Cross-domain seams:** HJP, Privacy & Consent, Programmes, Audit.

**Adversarial variants:** practitioner has separate scoped copy; full account deletion; completion already issued.

**Analysis:** a reflection activity can be completion-relevant without Programmes reading reflection content. Full journal capability belongs FP-014, not FP-008 by default.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** OQ-018/privacy review + FP-014 JIT.

## PRG-PT-017 — Translation and language switching
**Scenario class:** bilingual provenance.

**Relevant Product/Decision authority:** Content/translation law; DEC-211; Content Domain Law.

**Owning Domain(s):** Content & Media owns locale versions; Programmes owns programme semantics.

**Preconditions:** English/Afrikaans approved content bound to programme delivery.

**Scenario/timeline:** participant starts Afrikaans, switches English; one translation corrected; translated wording materially changes activity meaning.

**Expected invariants:** exact delivered locale/content version remains traceable; interface language is not automatically content language; paid/safety content cannot use unapproved fallback; semantic divergence that changes programme obligation triggers programme-version review.

**Questions:** exact locale-binding representation is OQ-013/JIT.

**Cross-domain seams:** Content, Programmes, Communications.

**Adversarial variants:** only one locale ready; stale cached translation; bilingual live session mismatch.

**Analysis:** translation lifecycle remains Content-owned; ProgrammeVersion must not duplicate translation payloads.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** OQ-013 + Content JIT + FP-008.

## PRG-PT-018 — Communications and stale reminders
**Scenario class:** programme/communications seam.

**Relevant Product/Decision authority:** DEC-162, DEC-218; Communications Domain Law; OQ-017/027/036.

**Owning Domain(s):** Programmes owns reason/schedule context; Communications owns durable delivery intent/attempt/provider evidence.

**Preconditions:** module/day/live reminder configured.

**Scenario/timeline:** release/reschedule creates message intent; schedule changes before send; worker retries; quiet hours/preferences apply.

**Expected invariants:** duplicate execution does not multiply logical message; send-time/current-policy checks prevent stale reminder where required; delivery success/failure never changes programme completion truth.

**Questions:** exact dedup identity/channel/caps remain OQ-017/027/036 and JIT.

**Cross-domain seams:** Communications, Programmes, Events, Content templates.

**Adversarial variants:** provider duplicate callback; reschedule races send; communication outage.

**Analysis:** durable intent is required for must-not-lose communication, but Programmes must not own provider delivery lifecycle.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** Communications JIT + FP-008 proof.

## PRG-PT-019 — Facilitator/operator actions
**Scenario class:** operator mutation authority.

**Relevant Product/Decision authority:** DEC-213; operating-model “work is attention, not authority”; Domain ownership.

**Owning Domain(s):** owning business Domain per action.

**Preconditions:** authorised staff role/relationship exists.

**Scenario/timeline:** enrol, withdraw, transfer, extend deadline, grant exception, correct completion, substitute content, pause edition, add live session.

**Expected invariants:** operator UI is not authority; each action invokes owner; policy/role/current state checked; history/audit retained; duplicate command safe; participant-visible consequence is explainable.

**Questions:** transfer, exception, completion-correction and edition pause/cancel policy are not all fully defined by Product Law.

**Cross-domain seams:** Programmes, Entitlements, Content, Events, Audit, Communications.

**Adversarial variants:** two staff act concurrently; stale operator page; bulk action with one invalid participant.

**Analysis:** generic admin CRUD would be unsafe. Concrete governed commands belong JIT after missing Product semantics resolve.

**Disposition:** NEEDS_WORKING_DELTA.

**Proof route:** Product promotion where required + JIT + Phase 8 for concurrency-sensitive actions.

## PRG-PT-020 — Duplicate/retry/restart
**Scenario class:** concurrency/idempotency/recovery.

**Relevant Product/Decision authority:** Architecture durability/idempotency doctrine; Engineering Standards where later applicable; FP-008 proof objective.

**Owning Domain(s):** Programmes plus each consequence owner.

**Preconditions:** scheduled release/enrol/completion action may repeat.

**Scenario/timeline:** duplicate enrol; duplicate release; completion evaluation repeats; worker crashes after commit; stale browser resubmits; cross-domain event duplicated/reordered.

**Expected invariants:** one logical obligation causes at most one authoritative consequence; restart does not lose committed participation; reordering is interpreted against current/historical authority; external side effects remain reconcilable.

**Questions:** exact idempotency keys/transactions/jobs are JIT, not Product Law.

**Cross-domain seams:** PostgreSQL authority; Oban durable work; Communications/Events/Entitlements downstream consequences.

**Adversarial variants:** completion correction races new evidence; entitlement ends during submission.

**Analysis:** Nuwe Jy scheduled release is a real tracer candidate because this path is materially consequential.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** JIT + Phase 8 Architectural Proof.

## PRG-PT-021 — Cohort/edition transfer
**Scenario class:** exceptional participation lifecycle.

**Relevant Product/Decision authority:** DEC-152, DEC-156, DEC-198/211/212; no matching generic programme-transfer contract found.

**Owning Domain(s):** Programmes & Challenges; Entitlements remains access owner.

**Preconditions:** participant is enrolled in an active scheduled edition.

**Scenario/timeline:** participant requests transfer to later/concurrent cohort; source and target may use same or different ProgrammeVersion; prior evidence exists.

**Expected invariants:** no silent version migration; prior history preserved; transfer cannot duplicate completion/access consequences; target rules and schedule are explicit.

**Questions:** transfer eligibility, evidence carry-forward, version mismatch, deadlines and participant-visible consequences are not currently governed generically.

**Cross-domain seams:** Entitlements, Communications, Community, Events.

**Adversarial variants:** two concurrent transfers; target full/cancelled; entitlement expiry during transfer.

**Analysis:** JIT cannot safely invent this if FP-008 operators are expected to perform transfer.

**Disposition:** INSUFFICIENT_AUTHORITY.

**Proof route:** Product promotion via PRG-UPD-001 if transfer is in FP-008 scope; otherwise defer the action.

## PRG-PT-022 — Programme edition cancellation/postponement
**Scenario class:** exceptional edition lifecycle.

**Relevant Product/Decision authority:** programme lifecycle + Nuwe Jy edition rules; no programme-equivalent of the explicit event cancellation/transfer policy was found.

**Owning Domain(s):** Programmes owns edition/participation truth; Commerce/Entitlements own money/access; Events owns linked occurrence changes.

**Preconditions:** edition exists before start or is active.

**Scenario/timeline:** postponed, cancelled before start, cancelled mid-way, facilitator unavailable, safety/content failure, business withdrawal.

**Expected invariants:** never delete edition/history; no automatic refund/access mutation by Programmes; downstream owners receive explicit governed commands; participant outcome/catch-up/completion remains explainable.

**Questions:** cancellation/postponement/merge consequences for enrolment, access, catch-up, completion and commercial remedy are not currently specified for programmes.

**Cross-domain seams:** Commerce, Entitlements, Events, Community, Communications, Content, Safety.

**Adversarial variants:** cancellation races scheduled release/payment/refund; restart during bulk consequences.

**Analysis:** this is a material Product semantic gap for a sellable scheduled Nuwe Jy edition if those operator actions are required.

**Disposition:** INSUFFICIENT_AUTHORITY.

**Proof route:** Product promotion PRG-UPD-001 before FP-008 JIT authorises such actions.

## PRG-PT-023 — Historical reproducibility
**Scenario class:** provenance/history.

**Relevant Product/Decision authority:** DEC-152/155/156/211/217/219; Content immutable delivery provenance; Domain Law.

**Owning Domain(s):** Programmes owns programme outcome; source Domains own evidence payloads.

**Preconditions:** participation completed years earlier.

**Scenario/timeline:** support/audit asks what participant received and why completion outcome occurred.

**Expected invariants:** Programme, ProgrammeVersion, edition/cohort if applicable, completion rule version, exceptions/corrections and exact evidence/content provenance can be identified; no need to copy all source payloads indefinitely.

**Questions:** retention/deletion may constrain how long personal evidence links remain; full deletion has separate law.

**Cross-domain seams:** Content, HJP, Events, Privacy, Audit.

**Adversarial variants:** source content withdrawn; journal deleted; programme retired.

**Analysis:** retain enough Programme-owned decision provenance to explain its own historical truth without becoming a shadow journal/content/event store.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** JIT + privacy/retention gates.

## PRG-PT-024 — Analytics denominator
**Scenario class:** derived metrics.

**Relevant Product/Decision authority:** DEC-169/219; Analytics Domain Law.

**Owning Domain(s):** Programmes owns enrolment/outcome; Analytics derives metrics.

**Preconditions:** enrolments include late joins, withdrawals, transfers, repeats and potentially cancelled editions.

**Scenario/timeline:** calculate completion/dropout/engagement rate.

**Expected invariants:** Analytics never decides completion; denominator definition is versioned measurement logic based on authoritative participation states; repeat enrolments are not silently deduplicated into one journey.

**Questions:** exact denominator exclusions for transfer/withdrawal/cancelled edition should be defined with the controlled programme measurement contract once underlying Product semantics exist.

**Cross-domain seams:** Analytics reads Programme outcomes, not vice versa.

**Adversarial variants:** retroactive metric-definition change; missing events; duplicated analytics event.

**Analysis:** this is measurement-contract work, not a reason to add new programme authority.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** controlled programme + Analytics JIT/Phase 8 as applicable.

## PRG-PT-025 — Generic LMS capability challenge
**Scenario class:** anti-overengineering/YAGNI.

**Relevant Product/Decision authority:** Roadmap FP-008/FP-014; DEC-196/202/207.

**Owning Domain(s):** none unless a concrete capability is separately approved.

**Preconditions:** proposal for SCORM/xAPI, gradebook, generic quiz builder, unrestricted page builder, arbitrary prerequisite graph, course marketplace, instructor marketplace, import engine, arbitrary multi-tenant authoring, points.

**Scenario/timeline:** proposal cites LMS convention rather than an approved NewYou outcome.

**Expected invariants:** no capability enters architecture merely because competitors have it; bounded approved prerequisites/certificates/badges do not imply generic engines.

**Questions:** which concrete Nuwe Jy or later approved programme outcome requires it?

**Cross-domain seams:** avoid inventing them.

**Adversarial variants:** “future proofing”, “industry standard”, “we might migrate courses later”.

**Analysis:** no current authority requires these generic capabilities.

**Disposition:** DEFER_YAGNI.

**Proof route:** future-only Product promotion if real evidence appears.

## PRG-PT-026 — Nuwe Jy as first acceptance test
**Scenario class:** scope validation.

**Relevant Product/Decision authority:** DEC-196...DEC-219; FP-008.

**Owning Domain(s):** Programmes & Challenges composed with existing owners.

**Preconditions:** core MVP and FP-007 dependencies eventually satisfied.

**Scenario/timeline:** configure one real 60-day scheduled edition and discover only the semantics it actually exercises.

**Expected invariants:** no parallel Nuwe Jy engine; central Safety/Plans/Entitlements/Events/Community/Communications reused; generic LMS not prerequisite; programme abstractions justified by actual edition needs.

**Questions:** OQ-019/OQ-024...OQ-028 remain activation gates.

**Cross-domain seams:** all FP-008 affected Domains.

**Adversarial variants:** building a generic course builder first; copying LearnDash model; treating Nuwe Jy as its own Domain.

**Analysis:** current Roadmap explicitly requires this evidence-led path.

**Disposition:** PASS.

**Proof route:** FP-008 JIT → Product gates → Phase 8/controlled programme.

## PRG-PT-027 — FP-014 as second lens
**Scenario class:** future reuse.

**Relevant Product/Decision authority:** FP-014; DEC-158...DEC-169 and programme decisions.

**Owning Domain(s):** Programmes & Challenges; HJP; Content; Safety; Communications; Privacy.

**Preconditions:** Nuwe Jy or equivalent programme proof exists.

**Scenario/timeline:** broader foundation programme adds persistent habits, private reflections/journals, richer progress/recovery.

**Expected invariants:** reuse FP-008 programme/edition mechanism where genuinely the same; introduce journal/habit semantics only through HJP; do not pull FP-014 privacy complexity into FP-008 without a concrete requirement.

**Questions:** OQ-018 and OQ-019 block relevant programme/journal publication.

**Cross-domain seams:** HJP/Privacy particularly.

**Adversarial variants:** using FP-014 as excuse to implement every future programme capability now.

**Analysis:** FP-014 is a validation lens for seams, not scope authority for FP-008.

**Disposition:** PASS.

**Proof route:** FUTURE_FP014 / reuse existing proof unless materially new mechanism.

## PRG-PT-028 — Deduplicated adversarial second pass
**Scenario class:** second-pass semantic-class check.

**Relevant Product/Decision authority:** all authorities above.

**Owning Domain(s):** varies.

**Preconditions:** PT-001...027 completed.

**Scenario/timeline:** re-run classes for version change, content replacement, translation, transfer, entitlement end, safety change, missed activity, catch-up, completion correction, cancellation, duplicates/restart, privacy/deletion, live/replay, journal ownership and analytics denominator.

**Expected invariants:** only genuinely new semantic classes produce new PT/GAP/UPD IDs.

**Questions:** completion correction/exemption and exceptional edition lifecycle remain the material unresolved classes; no new Domain is justified.

**Cross-domain seams:** already enumerated.

**Adversarial variants:** confirmation bias toward an LMS abstraction or toward declaring convergence too early.

**Analysis:** second pass does not reveal a justification for generic LMS scope. It does confirm that exceptional edition/participation actions and exact completion adjudication cannot be left to implementation invention.

**Disposition:** PASS_WITH_REFINEMENT.

**Proof route:** documentary now; Product/JIT routes for named gaps.

---

# 5. Gap register

## PRG-GAP-001 — Programme-specific completion thresholds
- **Classification:** PRODUCT_AUTHORITY_GAP
- **Origin:** PRG-PT-009
- **Existing authority route:** OQ-019; OQ-025 for Nuwe Jy.
- **Finding:** framework is locked, exact thresholds are deliberately unresolved.
- **Action:** do not create a duplicate UPD; consume the existing Product gates.

## PRG-GAP-002 — Completion exceptions/corrections
- **Classification:** PROGRAMME_SEMANTIC_GAP
- **Origin:** PRG-PT-010, PRG-PT-019, PRG-PT-028
- **Finding:** required/optional/conditional classes exist, but authorised exemption, substitute, correction, supersession and possible revocation consequences are not fully specified.
- **Action:** require OQ-019/OQ-025 resolution to state the applicable exception/adjudication rules for the programme. JIT may implement but must not invent them.

## PRG-GAP-003 — Exceptional edition/cohort lifecycle
- **Classification:** PRODUCT_AUTHORITY_GAP
- **Origin:** PRG-PT-021, PRG-PT-022
- **Finding:** normal/late participation is governed, but scheduled-programme transfer, postponement, cancellation, merge and their participant consequences lack an explicit programme policy contract.
- **Action:** PRG-UPD-001.

## PRG-GAP-004 — Entitlement lapse during enrolment
- **Classification:** ENTITLEMENT_SEAM_GAP
- **Origin:** PRG-PT-006
- **Finding:** ownership is clear; protected access ends according to Entitlements, but programme-specific continuation/pause/catch-up/withdrawal consequences must be declared by the concrete offer/edition.
- **Action:** FP-008 JIT may consume existing offer policy if explicit; otherwise Product promotion is required before promising a behaviour.

## PRG-GAP-005 — Content-correction binding mechanics
- **Classification:** CONTENT_TRANSLATION_GAP / JIT_ONLY
- **Origin:** PRG-PT-003, PRG-PT-017
- **Finding:** authority supports immutable content history, controlled corrections and safety correction, but exact ProgrammeVersion↔ContentVersion binding/correction mechanics are deliberately not implementation law.
- **Action:** Content + Programmes JIT must preserve exact delivery provenance and the ProgrammeVersion semantic boundary; no new Product rule unless a concrete correction policy contradiction appears.

## PRG-GAP-006 — External community as completion evidence
- **Classification:** DOMAIN_BOUNDARY_GAP / DEFER_YAGNI
- **Origin:** PRG-PT-013
- **Finding:** Facebook-first community cannot silently become authoritative programme evidence.
- **Action:** keep community participation non-completion-critical unless a future approved programme defines an explicit governed evidence route.

## PRG-GAP-007 — Journal evidence after deletion/correction
- **Classification:** PRIVACY_JOURNAL_GATE / FUTURE_FP014
- **Origin:** PRG-PT-016
- **Finding:** Programmes needs minimal accepted evidence, not journal content; exact retention/linkage after journal deletion requires OQ-018/privacy/JIT design.
- **Action:** do not pull full journal capability into FP-008 without a concrete requirement.

## PRG-GAP-008 — Programme analytics denominator rules
- **Classification:** CONTROLLED_PROGRAMME_PROOF
- **Origin:** PRG-PT-024
- **Finding:** Analytics ownership is clear; exact measurement denominator follows authoritative participation/exception semantics and should be versioned with the controlled-programme measurement contract.
- **Action:** no new Domain/Product rule unless a published KPI promise requires it.

## PRG-GAP-009 — Operator exception authority
- **Classification:** JIT_ONLY with Product prerequisite where consequence is undefined
- **Origin:** PRG-PT-019
- **Finding:** roles are named, but each exception command needs owner, guard, audit, reversibility/terminal behaviour and participant visibility.
- **Action:** JIT after Product semantics; no generic “admin override”.

---

# 6. Upstream delta register

## PRG-UPD-001 — Scheduled programme edition/cohort exceptional lifecycle contract

- **Originating PT:** PRG-PT-021, PRG-PT-022.
- **Exact missing semantic:** For a scheduled programme edition/cohort, Product authority does not yet explicitly define transfer, postponement, cancellation or merge semantics and the consequences for enrolment history, version pinning, catch-up/completion, participant visibility, entitlement/access and commercial remedy.
- **Accepted working direction:**
  - never model correction/cancellation as deleting the edition or enrolment;
  - preserve source and target ProgrammeVersion provenance;
  - Programmes owns the participation/edition transition only;
  - Commerce owns any refund/credit decision and Entitlements owns access consequences;
  - Events/Community/Communications remain owners of their linked consequences;
  - one logical operator action must be idempotent and auditable;
  - participant-facing effect must be explicit and historically explainable;
  - where the action is not required for FP-008, defer it rather than build a generic lifecycle engine.
- **Affected authority:** Product Law / Product Review for FP-008 scheduled-edition policy; may later become a named OQ or DEC only through governance.
- **Affected Domains:** Programmes & Challenges, Entitlements, Commerce, Events & Live, Community, Communications; Safety/Content where cancellation is caused by safety/content failure.
- **Why JIT cannot invent it:** transfer/cancellation changes customer-visible participation, access and potentially money/completion promises; these are Product semantics, not Resource/action details.
- **Downstream Feature Packs:** FP-008; FP-014 if it later uses scheduled/facilitated editions.
- **Privacy/expert gate:** commercial/legal/operations review when refund/credit or contractual access promises are involved; clinical/content review where safety/content failure triggers the action.
- **Rejected alternatives:** copy Event policy blindly; delete enrolment/edition; treat entitlement state as programme lifecycle; let operator UI define the rule; build a generic LMS cohort-state machine.
- **Authority status:** NON-AUTHORITATIVE WORKING DELTA until separately governed.

---

# 7. Reusable semantics versus Nuwe Jy configuration

## Reusable now

- Programme / ProgrammeVersion hierarchy.
- Edition as version-bound delivery configuration.
- Optional cohort/shared schedule context.
- Enrolment/participation history distinct from entitlement.
- Explicit availability/prerequisite/pacing rules.
- Activity requirement classes already locked by Product.
- Source-domain evidence consumption.
- Versioned completion-rule framework.
- Compassionate recovery/catch-up as a first-class concept.
- Explicit correction/migration provenance.
- Idempotent durable scheduled release where a programme uses scheduling.

## Nuwe Jy-specific configuration/authority

- 60-calendar-day shared rhythm.
- Today composition and daily drip.
- exact milestone check-ins and completion thresholds.
- exact late-enrolment/catch-up policy.
- Nuwe Jy safety route/required activities.
- cohort operational capacity/facilitation.
- current community/live/communications configuration.
- source content/media inventory and LearnDash retirement obligations.

## Wait for a second concrete use case / FP-014

- full private journal participation semantics.
- richer persistent habit assignment/reuse rules.
- any materially different programme-delivery mode not exercised by Nuwe Jy.
- broad facilitator-release tooling.
- generalized programme templates/builders beyond controlled composition.

---

# 8. Explicit generic-LMS rejection register

Current disposition unless new Product authority appears:

- SCORM — `DEFER_YAGNI`.
- xAPI — `DEFER_YAGNI`.
- unrestricted page builder — `DEFER_YAGNI`.
- generic quiz builder — `DEFER_YAGNI`.
- gradebook — `DEFER_YAGNI`.
- generic certificate engine — `DEFER_YAGNI`; bounded programme completion/participation certificate remains approved.
- generic badge/points/gamification engine — `DEFER_YAGNI`; bounded optional approved recognition is not a platform-wide points system.
- arbitrary prerequisites graph — `DEFER_YAGNI`; explicit programme prerequisites are already approved.
- course marketplace — `DEFER_YAGNI`.
- instructor marketplace — `DEFER_YAGNI`.
- LMS import/compatibility engine — `DEFER_YAGNI`; LearnDash clean future-edition cutover is already locked.
- arbitrary multi-tenant course authoring — `DEFER_YAGNI`.

---

# 9. Current convergence assessment

**Broad documentary discovery is not yet frozen.**

The reusable programme boundary is coherent enough to avoid generic LMS invention, and no new Domain is justified. However, freeze would be premature while:

1. OQ-019/OQ-025 still own the exact completion/required-activity/exception semantics for Nuwe Jy;
2. PRG-UPD-001 has not been separately adjudicated if FP-008 requires transfer/postpone/cancel/merge actions;
3. Content-binding correction detail still needs the affected JIT dossiers to prove that exact delivery provenance is preserved without making Programmes a duplicate CMS;
4. journal evidence/deletion remains a later FP-014/privacy gate rather than an FP-008 assumption;
5. no fresh independent reviewer has yet certified this stream’s convergence.

Until those conditions are satisfied, do not state the final freeze sentence and do not implement programme Resources/actions/schemas from this working ledger.
