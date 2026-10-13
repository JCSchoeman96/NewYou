# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.4.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.4.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 3 — ContentVersion / translation binding and correction semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.3.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused ContentVersion / locale / publication / correction pass while preserving v0.1.0 through v0.3.0 unchanged.

> This is an append-only semantic successor. Read v0.1.0, then v0.2.0, then v0.3.0, then this pass. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work or Content & Media authority.

> Nuwe Jy remains the first concrete programme acceptance test. Reusable abstractions must emerge from approved NewYou outcomes, not generic LMS convention.

---

# 25. Accepted working-lock status entering Pass 3

The user accepted Pass 2 after review.

Therefore Pass 1 and Pass 2 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, deferred items and future explicit refinements.

In particular, Pass 3 inherits these accepted boundaries:

- Programme is the stable conceptual/catalogue identity;
- ProgrammeVersion is the version-pinned participant-semantic contract;
- ProgrammeVersion is not a duplicate ContentVersion;
- material programme-semantic change requires a successor ProgrammeVersion;
- a non-semantic minor correction must not be forced into a new ProgrammeVersion merely because Content changed;
- active/completed participant history must remain explainable against the governing ProgrammeVersion;
- Edition/Cohort semantics remain Pass 4 and have not been pulled into this pass.

---

# 26. Pass 3 — ContentVersion / translation binding and correction semantics

## 26.1 Scope hard stop

This pass answers only:

1. what Content & Media owns versus what Programmes & Challenges owns when programme lessons/activities consume governed content;
2. what must be true about exact ContentVersion/locale provenance at delivery;
3. how Content correction/supersession can coexist with ProgrammeVersion immutability;
4. when a Content change does and does not require a successor ProgrammeVersion;
5. how independently governed Afrikaans/English locale versions compose with one ProgrammeVersion;
6. what happens at the authority boundary when content is approved, published, superseded or withdrawn;
7. what current authority already decides about missing translations and machine drafts;
8. which exact resource/index/reference mechanics remain OQ-013/JIT rather than Product semantics; and
9. whether any participant-facing programme consequence remains genuinely unresolved after the content boundary is respected.

This pass deliberately does **not** decide:

- Edition/Cohort cardinality, schedule ownership or exceptional lifecycle — Pass 4;
- entitlement lapse/reacquisition — Pass 5;
- programme release/unlock sequencing, scheduler/idempotency mechanics — Pass 6;
- activity evidence contracts — Pass 7;
- completion thresholds/adjudication — Pass 8;
- exemption/substitute semantics — Pass 9;
- compassionate catch-up detail — Pass 10;
- broad Content & Media Ash resource design, locale indexes, publication workers, cache invalidation or exact delivery-reference schema — OQ-013/OQ-016 and Content JIT.

If a content event changes progression/completion semantics, this pass identifies the ownership seam and routes the consequence rather than inventing the later-pass rule.

---

## 26.2 Pass-3 authority evidence

### PRG-EV-020 — Live governed state reconfirmed for Pass 3

At the start of Pass 3, live `main` remained:

`086ade7b28c000de1c387acb9760e5eb08bb0413`

The working branch entered the pass at:

`a7ca3b9960e467a79639709ec2b9484d26b8b02f`

No newer authoritative `main` state was observed before substantive Pass-3 work.

### PRG-EV-021 — Content & Media is sole authority for governed content/translation/publication versions

Current Domain Law assigns Content & Media ownership of:

- conceptual content identity and immutable content versions;
- locale branches/translations and approval/publication lifecycle;
- content risk classification, approvals, corrections/withdrawals and attribution;
- governed editorial media identity/version/publication state.

The ownership matrix says all delivery domains **READ exact version** while Content & Media remains COMMAND owner of governed content/translation/publication version.

Programmes & Challenges explicitly does **not** own lesson/content body versions.

### PRG-EV-022 — Product Law requires independently governed bilingual version lineage

Current Product/Decision authority establishes:

- content may originate in Afrikaans or English while recording source locale/version relationships;
- Afrikaans and English variants remain linked to one conceptual content item and are reviewed independently;
- paid/core/assessment/plan/clinical/safety/contractual/core-onboarding content requires the governed bilingual path;
- optional low-risk editorial content may have explicit single-language availability;
- translation lifecycle includes missing/draft/machine-draft/review/approval/publication/superseded/withdrawn semantics;
- machine translation creates draft material only and never bypasses required human/clinical review;
- shared conceptual content uses immutable content and translation versions rather than unrelated records or one translation blob.

### PRG-EV-023 — Content versions are immutable and corrections preserve historical trace

Product Law §21E.8 states:

- every material content edit creates a new immutable content version;
- version provenance includes parent content item, locale/version/source relationship, author, change summary, risk class, approvals, publication date, superseded version and correction/withdrawal reason;
- minor typographical corrections may use a controlled correction path;
- the original published version remains traceable.

Therefore a correction is not permission to overwrite the previously delivered content version.

### PRG-EV-024 — Architecture requires exact content/locale delivery provenance

Current Architecture Law synthesis states:

- governed runtime content has one conceptual identity with independently versioned locale branches;
- published/activated governed versions are immutable evidence;
- material edits create new versions and correction uses explicit supersession/withdrawal;
- paid, personalised or governed delivery retains exact content/locale provenance;
- locale approval is independent;
- `latest`, `approved` and `published` are distinct states;
- critical paid/safety/legal content cannot silently fall back to an unapproved or machine translation.

### PRG-EV-025 — Programme Law explicitly composes minor correction with version pinning

Product Law §21F.10 states:

- new enrolments normally use the latest approved ProgrammeVersion;
- active participants remain on their enrolled ProgrammeVersion unless a minor correction applies, an optional governed migration is accepted, or safety correction requires migration/withdrawal;
- material changes create a new ProgrammeVersion;
- completed history never changes silently.

This confirms that ContentVersion evolution and ProgrammeVersion evolution are related but are not a one-to-one lifecycle.

### PRG-EV-026 — Exact translation/delivery-reference implementation is already an open architecture gate

`OQ-013 — Translation resource design` remains ARCHITECTURE REVIEW and explicitly owns:

- exact Ash resource boundaries;
- approval relationships;
- locale/version indexes; and
- immutable delivery references.

`OQ-016 — Content publication operations` remains OPERATIONS / ARCHITECTURE REVIEW for scheduler reliability, retry policy, alert ownership, stale-approval checks and recovery.

Therefore Pass 3 must not invent concrete Resource topology, binding tables, publication workers or scheduler mechanics.

### PRG-EV-027 — FP-008 already has a concrete Nuwe Jy content readiness gate

`OQ-024 — Nuwe Jy source-content inventory` remains CONTENT REVIEW and requires inventory of current Nuwe Jy lessons, videos, downloads, live-session assets, rights, duplicated material, missing translations and outdated content.

FP-008 therefore cannot treat programme-content binding as abstract LMS content. It must bind to the governed Nuwe Jy content actually proven ready for the flagship.

---

# 27. Pass-3 accepted working conclusions

Subject to the explicit gap/deferred items below, these are candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance of Pass 3.

## 27.1 Content bodies and locale versions stay in Content & Media

Programmes owns the programme structure/meaning that says a lesson/activity contains or uses governed content.

Content & Media owns:

- the conceptual content identity;
- immutable content versions;
- locale/translation versions;
- review/approval/publication state;
- correction/supersession/withdrawal;
- governed media publication/rights truth.

Programmes must not copy the lesson body/translation payload into a parallel programme-owned CMS authority.

## 27.2 The programme-content relationship needs both intended identity and exact delivered provenance

Two facts must remain distinguishable:

1. **programme intent:** which governed content concept/role belongs in this ProgrammeVersion structure; and
2. **delivery provenance:** which exact eligible published ContentVersion + locale version the participant actually received.

Current authority does not require Pass 3 to choose whether implementation represents this through a conceptual content reference plus delivery receipt, an exact binding record, an exact Publication reference, or another OQ-013-compliant mechanism.

But any JIT design must make both facts explainable without making Programmes owner of Content truth.

## 27.3 A floating `latest content` lookup is not historical truth

`latest`, `approved` and `published` are distinct.

A participant-facing programme delivery cannot later be reconstructed by asking “what ContentVersion is current now?”.

At delivery, an exact eligible governed content/locale version must be identified, and historical explanation must retain that exact provenance.

## 27.4 Content correction does not automatically create a ProgrammeVersion

A controlled Content correction may produce a new immutable ContentVersion while retaining the same ProgrammeVersion **only when programme semantics do not materially change**.

Examples include a genuine typographical correction, formatting correction or semantically equivalent wording correction that leaves:

- programme structure;
- participant obligation;
- requiredness;
- progression/prerequisite meaning;
- completion meaning; and
- approved safety meaning

unchanged.

Original delivered ContentVersion/locale provenance remains traceable.

## 27.5 Content cannot be used to smuggle a programme-semantic change through the correction path

If a content successor changes what the participant is required to do, changes progression, materially changes an activity instruction, changes completion meaning, or otherwise changes the participant-facing programme contract, Content publication alone cannot mutate the existing ProgrammeVersion.

The programme change must follow the Pass-2 version rule: successor ProgrammeVersion or the separately governed safety/migration path.

## 27.6 Locale correction does not imply duplicate ProgrammeVersions

Afrikaans and English are independently governed locale branches under shared conceptual content lineage.

A correction/review in one locale does not, by itself, justify separate Afrikaans and English ProgrammeVersions.

The ProgrammeVersion remains language-neutral programme meaning unless a locale change actually creates semantic divergence in programme obligations. If such divergence appears, it is a defect requiring correction/version review, not an accepted bilingual feature.

## 27.7 Exact locale delivered matters when a participant switches language

A participant may change language without changing ProgrammeVersion merely because of the language switch.

Each governed delivery still needs exact locale/version provenance.

Past Afrikaans delivery is not retroactively relabelled as English; future eligible delivery may use the approved English branch, and vice versa.

## 27.8 Required translation readiness fails closed

For content that Product Law requires bilingually before publication/delivery:

- a missing/unapproved required locale blocks the governed delivery path;
- machine draft is never a fallback participant version;
- Programmes cannot waive Content approval simply to keep a schedule moving.

Optional low-risk public editorial content may use the explicit Product-approved missing-translation fallback, but that rule must not be broadened to Nuwe Jy paid/core/safety content merely for convenience.

## 27.9 Approved is not published

Programmes may not infer current delivery eligibility merely from “approved”.

Content publication activates a specific approved locale/version. Any programme delivery must consume the current Content-owned publication/eligibility result appropriate to that delivery contract.

Exact selection/reference mechanics remain OQ-013/JIT.

## 27.10 Withdrawal removes current delivery authority without deleting history

When Content & Media withdraws a version, Programmes does not continue serving it merely because an edition/enrolment still references the programme structure.

Withdrawal does not erase:

- the fact that an earlier participant received that exact version;
- the ProgrammeVersion that governed the participant;
- historical publication/delivery provenance.

Content owns the withdrawal declaration. Programmes owns any resulting programme-side transition/consequence.

## 27.11 Safety correction is an exceptional cross-domain route, not ordinary editorial drift

Where a content/safety issue makes continued delivery unsafe:

- Content & Media owns withdrawal/corrected content publication;
- Safety & Eligibility owns current safety restriction/outcome;
- Programmes cannot override either owner;
- Product Law permits safety correction to require ProgrammeVersion migration or withdrawal;
- exact participant progression/completion/recovery consequence must follow the governed programme/safety route.

A “safety correction” label must not be used to bypass ordinary version/change governance for non-safety edits.

## 27.12 Historical programme explanation needs references, not duplicated payloads

Years later, NewYou must be able to explain:

- governing ProgrammeVersion;
- delivery context where applicable;
- conceptual lesson/activity relationship;
- exact ContentVersion and locale version actually delivered where relevant;
- supersession/correction/withdrawal lineage sufficient to explain later differences.

This does not require Programmes to retain duplicate lesson bodies or translation text.

## 27.13 Publication/correction timing is separate from programme release scheduling

Content may change state before a future programme release becomes available.

Pass 3 establishes only that the release cannot fabricate eligibility and must ultimately bind/deliver an exact eligible version with provenance.

The exact time at which a future programme release resolves/revalidates its content target, and its retry/idempotency mechanics, remain Pass 6 plus OQ-016/JIT.

## 27.14 Media follows the same authority principle

Where a lesson uses a video/download/media asset:

- Content & Media owns governed media version/rights/publication truth;
- Programmes owns the programme-side relationship and consequence;
- participant delivery cannot treat provider URL/current object as durable authority;
- exact governed version/provenance must remain explainable.

Pass 3 does not design the media storage/delivery schema.

---

# 28. Pass-3 pressure tests

## PRG-PT-057 — Copy lesson bodies into Programmes

**Scenario class:** duplicate authority / shadow CMS.

**Scenario:** ProgrammeVersion stores full lesson body and Afrikaans/English copies so programme rendering does not need Content & Media.

**Expected invariants:** Content & Media remains sole owner of conceptual content, immutable versions, translations and publication/correction truth; Programmes owns programme structure/meaning only.

**Analysis:** duplicated mutable/published content creates competing authority and breaks correction/withdrawal provenance.

**Disposition:** `PASS` — duplicate Programme-owned content payload authority rejected.

---

## PRG-PT-058 — Store only ContentItem identity and reconstruct historical delivery from current content

**Scenario class:** provenance loss.

**Scenario:** an enrolment records only the stable conceptual ContentItem. Years later support resolves that item to its current published translation and claims that was what the participant saw.

**Expected invariants:** historical delivery identifies the exact delivered content/locale version; current content cannot rewrite historical evidence.

**Analysis:** Architecture explicitly requires exact content/locale provenance for governed delivery.

**Disposition:** `PASS` — floating conceptual reference alone is insufficient historical evidence.

**Implementation boundary:** exact immutable delivery-reference representation remains OQ-013.

---

## PRG-PT-059 — Typographical correction under the same ProgrammeVersion

**Scenario class:** non-semantic content correction.

**Scenario:** one Nuwe Jy lesson contains a spelling/formatting error. Content creates a controlled successor ContentVersion with identical programme meaning.

**Expected invariants:**

- original ContentVersion remains traceable;
- corrected ContentVersion is independently governed/published;
- ProgrammeVersion does not need a new semantic version solely for the typo;
- historical participants are not falsely recorded as having seen the corrected version.

**Analysis:** Product Law explicitly permits controlled minor correction while preserving original trace.

**Disposition:** `PASS`.

---

## PRG-PT-060 — Corrected lesson changes participant obligation

**Scenario class:** semantic boundary attack.

**Scenario:** a “content correction” changes “try this if useful” into a required action needed to progress or complete.

**Expected invariants:** Content correction cannot silently mutate programme requirement semantics; the existing ProgrammeVersion remains what historical participants were promised.

**Analysis:** this is a material programme-semantic change regardless of the ContentVersion label.

**Disposition:** `PASS` — correction-path mutation rejected; successor ProgrammeVersion or governed safety/migration route required.

---

## PRG-PT-061 — Afrikaans typo correction only

**Scenario class:** independent locale versioning.

**Scenario:** Afrikaans contains a typo; English is correct; programme meaning is unchanged.

**Expected invariants:**

- Afrikaans gets the governed successor locale/content version as required by Content authority;
- English history remains unchanged;
- ProgrammeVersion does not split into language-specific variants merely because locale version lineage differs;
- exact delivery provenance identifies which locale/version each participant received.

**Disposition:** `PASS`.

---

## PRG-PT-062 — Translation creates different programme obligation

**Scenario class:** semantic divergence across locales.

**Scenario:** English says an activity is optional while Afrikaans wording makes it sound mandatory.

**Expected invariants:**

- both locales cannot be treated as semantically equivalent merely because they share a ProgrammeVersion;
- the divergent translation must not silently redefine programme semantics for one language;
- affected publication/delivery fails closed or is corrected through Content governance;
- if the intended programme obligation itself changes, ProgrammeVersion review is required.

**Analysis:** bilingual branches may differ linguistically, not in governed programme obligation.

**Disposition:** `PASS_WITH_REFINEMENT` — Content review/correction first; ProgrammeVersion changes only if intended programme meaning changes.

---

## PRG-PT-063 — Required Nuwe Jy translation missing at delivery

**Scenario class:** bilingual fail-closed.

**Scenario:** the English version is approved/published but required Afrikaans Nuwe Jy lesson translation is missing or unapproved.

**Expected invariants:**

- required bilingual delivery readiness is not satisfied;
- machine draft is not served;
- Programmes cannot fabricate approval or silently show an unintended language merely to keep the cohort schedule.

**Analysis:** Product Law explicitly fails closed for required paid/core/clinical/safety content translations.

**Disposition:** `PASS`.

**Route:** OQ-024 content inventory/readiness; exact resource checks OQ-013; operational failure OQ-016 where applicable.

---

## PRG-PT-064 — Optional low-risk editorial item exists in one language

**Scenario class:** permitted fallback boundary.

**Scenario:** a non-core optional low-risk editorial link associated with a programme is available only in English.

**Expected invariants:**

- selected translation unavailability is explicit;
- available language is offered explicitly where Product Law permits;
- no silent machine fallback;
- this exception does not weaken required bilingual Nuwe Jy/core content readiness.

**Disposition:** `PASS`.

---

## PRG-PT-065 — Participant switches language mid-programme

**Scenario class:** locale/provenance continuity.

**Scenario:** participant consumed days 1–10 in Afrikaans and changes preferred content language to English for later days.

**Expected invariants:**

- ProgrammeVersion does not change merely because language changes;
- previously delivered Afrikaans content remains historically identified as Afrikaans + exact version;
- later delivery may use the exact eligible English locale version;
- interface language does not retroactively rewrite content-language provenance.

**Disposition:** `PASS`.

---

## PRG-PT-066 — Approved but unpublished translation is used by Programmes

**Scenario class:** publication authority bypass.

**Scenario:** Programme renderer finds an approved newer translation and uses it even though Content has not made that locale/version current/published for delivery.

**Expected invariants:** `approved != published`; Programmes reads Content publication authority and does not invent activation.

**Disposition:** `PASS` — bypass rejected.

---

## PRG-PT-067 — Withdrawn content remains servable because it is cached or referenced by the Edition

**Scenario class:** current-use withdrawal.

**Scenario:** Content withdraws a lesson version; a programme projection/cache/edition reference still points to it.

**Expected invariants:**

- current Content withdrawal wins over stale projection/cache/reference;
- withdrawn content is not treated as current delivery authority;
- historical delivery evidence remains intact;
- Programmes handles its own consequence rather than mutating Content state.

**Disposition:** `PASS` for ownership/current-delivery boundary.

**Deferred:** required-content participant consequence is PRG-GAP-011 / later completion-substitution-recovery passes.

---

## PRG-PT-068 — Required lesson is withdrawn and no approved replacement exists

**Scenario class:** cross-domain programme consequence gap.

**Scenario:** a lesson required for Nuwe Jy progression/completion is withdrawn after Edition activation; no equivalent approved content is currently available.

**Expected invariants:**

- withdrawn content is not served;
- Content cannot decide programme completion/progression;
- Programmes cannot fabricate a substitute/waiver/completion result;
- historical participants retain their actual delivery/progress evidence;
- participant-facing consequence must be explicit and compassionate.

**Analysis:** current authority defines owner boundaries and safety/migration principles but does not fully specify the non-safety required-content consequence when no replacement exists.

**Disposition:** `INSUFFICIENT_AUTHORITY_FOR_PROGRAMME_CONSEQUENCE`.

**Promotion:** PRG-GAP-011. No upstream delta yet; later Pass 8/9/10 and existing OQ gates must adjudicate concrete consequence before JIT invents one.

---

## PRG-PT-069 — Safety-critical content correction during active enrolment

**Scenario class:** exceptional safety correction.

**Scenario:** current guidance becomes unsafe for a subset or all participants and Content publishes a corrected/safer successor while old content is withdrawn.

**Expected invariants:**

- Safety remains authoritative for restrictions/outcomes;
- Content remains authoritative for corrected/withdrawn content;
- Programmes cannot keep serving unsafe content because the enrolment is version-pinned;
- Product Law permits safety correction to require migration or withdrawal;
- history preserves before/after provenance.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Deferred:** exact Nuwe Jy safety route and completion consequence remain OQ-025 / later Safety and completion passes.

---

## PRG-PT-070 — Content superseded after Edition validation but before scheduled release

**Scenario class:** timing/revalidation boundary.

**Scenario:** Edition validation referenced eligible content. Before day 20 is released, Content supersedes or withdraws the previously eligible version.

**Expected invariants:**

- scheduled programme delivery cannot blindly trust stale validation;
- current Content publication/eligibility is rechecked at the appropriate governed boundary;
- delivery records the exact version actually released;
- no `latest` lookup may erase the original configured intent/history.

**Analysis:** semantic requirement is clear; exact release-time resolution, scheduler/retry/idempotency mechanism belongs Pass 6/OQ-016/JIT.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-071 — Correction occurs after participant already consumed the lesson

**Scenario class:** historical delivery integrity.

**Scenario:** participant viewed ContentVersion C1; later Content publishes corrected C2 under the same ProgrammeVersion.

**Expected invariants:**

- participant history does not claim C2 was delivered earlier;
- future re-open behaviour may show a corrected/current version only under explicit governed delivery semantics;
- the historical fact that C1 was previously delivered remains explainable;
- completed programme meaning is not silently rewritten.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Implementation boundary:** whether UI exposes “current corrected copy” alongside historical provenance is delivery/JIT detail; history must not be falsified.

---

## PRG-PT-072 — Correction is published before participant's first delivery under the same ProgrammeVersion

**Scenario class:** correction before first consumption.

**Scenario:** Edition uses ProgrammeVersion V1. Content C1 was originally prepared, then semantically equivalent corrected C2 becomes the eligible published version before this participant reaches the lesson.

**Expected invariants:**

- same ProgrammeVersion may remain valid because programme semantics did not change;
- delivery must identify C2 exactly;
- no claim is made that C1 was delivered to that participant;
- exact binding/resolution implementation remains OQ-013.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

## PRG-PT-073 — Machine translation becomes stale after source change

**Scenario class:** translation provenance.

**Scenario:** an Afrikaans source ContentVersion changes while an English machine draft was generated from the prior source.

**Expected invariants:**

- machine draft records exact source version;
- source change makes the draft stale;
- stale/unapproved machine translation never becomes participant delivery merely to meet programme schedule;
- replacement translation follows normal review/approval/publication.

**Disposition:** `PASS`.

---

## PRG-PT-074 — Every ContentVersion change forces a new ProgrammeVersion

**Scenario class:** false one-to-one version coupling.

**Scenario:** implementation fingerprints all referenced ContentVersion IDs and creates V2 whenever any referenced content version changes.

**Expected invariants:** ProgrammeVersion changes track programme semantics, not every editorial version event; genuine minor correction can remain within the same ProgrammeVersion.

**Disposition:** `PASS` — automatic one-to-one version coupling rejected.

---

## PRG-PT-075 — Separate Afrikaans and English ProgrammeVersions

**Scenario class:** duplicate programme semantics.

**Scenario:** implementation creates Nuwe Jy V1-AF and V1-EN solely because locale versions are independently governed.

**Expected invariants:** one ProgrammeVersion carries the programme semantics; Content owns independent locale version lineages; language-specific ProgrammeVersion duplication requires a genuinely different programme contract, not ordinary translation governance.

**Disposition:** `PASS` — duplicate ProgrammeVersion-by-locale rejected.

---

## PRG-PT-076 — Media asset replaced underneath a lesson reference

**Scenario class:** Content/Media authority boundary.

**Scenario:** a lesson video is replaced because rights expire or the media is corrected.

**Expected invariants:**

- Content & Media owns exact media version/rights/publication state;
- provider URL/object identity is not programme authority;
- historical delivery/reference remains explainable;
- Programmes does not overwrite foreign media truth;
- if replacement changes programme semantics, ProgrammeVersion review applies.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** OQ-024 proves Nuwe Jy source media/rights readiness; exact media binding stays Content JIT.

---

## PRG-PT-077 — Renderer chooses “latest approved” instead of published current version

**Scenario class:** lifecycle conflation.

**Scenario:** Content C3 is approved for future publication; C2 is current published. Programme renderer chooses C3 because it is “latest approved”.

**Expected invariants:** latest, approved and published/current are distinct; Programmes cannot activate C3 by reading it.

**Disposition:** `PASS` — lifecycle conflation rejected.

---

## PRG-PT-078 — Historical explanation years later

**Scenario class:** long-term provenance.

**Scenario:** support/audit needs to explain what a participant received when programme V1, content and translations have since changed several times.

**Expected invariants:** NewYou can identify the governing ProgrammeVersion and exact relevant delivered ContentVersion/locale provenance without copying all content payloads into Programmes or resolving through today's current version.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** OQ-013/JIT defines exact reference representation; privacy/retention law constrains retained personal linkage where applicable.

---

# 29. Pass-3 gap adjudication

## PRG-GAP-005 — Content-correction binding mechanics — refined by Pass 3

Existing classification: `CONTENT_TRANSLATION_GAP / JIT_ONLY`.

Pass 3 materially narrows this earlier bootstrap gap:

- **now semantically resolved:** Content owns conceptual/version/locale/publication/correction truth; Programmes owns programme semantic structure/consequence; exact governed delivery provenance is mandatory; minor non-semantic Content correction need not create ProgrammeVersion; material programme meaning change does;
- **still open by explicit authority:** exact Ash resource topology, locale/version indexes, approval relationships and immutable delivery-reference representation — `OQ-013`;
- **operationally open:** publication scheduling/retry/stale-approval/recovery — `OQ-016`;
- **action:** do not create a new duplicate gap for resource design. Consume OQ-013/OQ-016 at JIT.

`PRG-GAP-005` remains open only for those already-governed implementation details and is no longer a broad semantic uncertainty.

## PRG-GAP-011 — Required programme content withdrawn/unavailable with no approved replacement

- **Classification:** PROGRAMME_CONTENT_CONSEQUENCE_GAP / LATER-PASS ADJUDICATION
- **Origin:** PRG-PT-068.
- **Authority already clear:** Content owns withdrawal/current delivery eligibility; Programmes owns progression/completion; Safety owns safety restrictions; active enrolment/history remains version-pinned/explainable.
- **Exact missing semantic:** if a content item that is required for progression/completion becomes unavailable after programme activation and no approved equivalent exists, current Product Law does not fully specify whether that programme obligation pauses, is substituted, becomes temporarily unavailable, receives an authorised exception, extends recovery, triggers migration/withdrawal, or has another participant-visible consequence.
- **Why JIT cannot invent it:** the choice changes participant obligations, completion fairness and potentially the commercial programme promise.
- **Why Pass 3 does not decide it:** substitute/exemption/completion/recovery consequence belongs the dedicated Pass 8/9/10 pressure tests; safety-caused cases additionally route through OQ-025.
- **FP-008 relevance:** before the flagship can activate, OQ-024 must prove content/media/rights/translation readiness. If a required-content withdrawal contingency is part of the actual operating model, the concrete programme consequence must be explicit before JIT/operator tooling implements it.
- **Upstream delta now:** NONE. Existing OQ-019/OQ-024/OQ-025 and later dedicated passes should be exhausted first. Promote only if they cannot express the necessary Product rule.
- **Status:** OPEN / NON-BLOCKING FOR PASS-3 SEMANTIC FREEZE, potentially blocking for a concrete required-content failure path if unresolved at FP-008 activation.

No other new Product/Architecture/Domain gap is promoted in Pass 3.

---

# 30. Pass-3 refinements to earlier working synthesis

Earlier ledgers remain immutable. These successor refinements now govern the working stream once Pass 3 is accepted.

## PRG-REF-008 — ProgrammeVersion/content binding must preserve two different truths

Earlier shorthand that ProgrammeVersion “references content” is refined.

The implementation must distinguish:

- intended governed content identity/role in the programme structure; and
- exact ContentVersion/locale version actually delivered.

Do not collapse these into a mutable `current_content_id` lookup or duplicate content payload.

## PRG-REF-009 — Non-semantic ContentVersion correction may remain within one ProgrammeVersion

A successor ContentVersion does not automatically mean a successor ProgrammeVersion.

ProgrammeVersion changes only when programme semantics change materially or an exceptional governed safety/migration path applies.

## PRG-REF-010 — Locale versions are not ProgrammeVersions

Afrikaans/English independently governed translation versions remain Content & Media truth. The programme semantic version remains shared unless the underlying programme contract itself differs.

## PRG-REF-011 — Historical delivery is exact-version truth, not “whatever is published now”

Any support/audit/progress explanation that matters must not reconstruct past delivery by resolving the current ContentVersion/locale version.

Exact delivered provenance must survive content evolution subject to privacy/retention law.

## PRG-REF-012 — Content withdrawal and programme consequence are separate authoritative transitions

Content withdrawal removes Content-owned current delivery authority. It does not itself decide programme completion/progression.

Programmes must apply only a governed programme-side consequence; if that consequence is undefined, JIT stops rather than inventing it.

---

# 31. Pass-3 anti-LMS/YAGNI outcome

Pass 3 explicitly rejects:

- copying lesson bodies/translations into ProgrammeVersion as a shadow CMS;
- separate Afrikaans/English ProgrammeVersions merely to represent locale versions;
- automatic ProgrammeVersion creation for every ContentVersion event;
- a floating “latest content” renderer as historical provenance;
- using approved-but-unpublished content because it is newer;
- serving machine translation as programme fallback where governed approval is required;
- a generic LMS content-package/version-import mechanism as a prerequisite for Nuwe Jy;
- a generic compatibility layer that treats ContentVersion IDs as SCORM/xAPI-like course-package revisions.

Absent a concrete approved outcome, all generic LMS content-package/import interoperability remains `DEFER_YAGNI`.

---

# 32. Pass-3 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Content & Media remains sole authority for content bodies, immutable versions, locale/translation versions, publication, correction, withdrawal and governed media state.
2. Programmes owns the programme structural/semantic relationship and programme-side consequence; it does not become a second CMS.
3. Programme-content binding must preserve both intended content identity/role and exact delivered ContentVersion/locale provenance.
4. A floating `latest`/`current` content lookup cannot explain historical delivery.
5. A genuine non-semantic Content correction may produce a successor ContentVersion without a successor ProgrammeVersion.
6. Content changes that materially alter programme obligations/structure/progression/completion require ProgrammeVersion governance, not Content-only publication.
7. Afrikaans/English locale versions are independently governed Content truth, not separate ProgrammeVersions by default.
8. Required bilingual content fails closed when a required approved translation is unavailable; machine draft is never a participant fallback.
9. `approved`, `published/current` and `latest` are distinct; Programmes does not invent publication authority.
10. Content withdrawal stops current delivery authority but preserves historical provenance; Programmes owns the resulting programme-side consequence.
11. Safety correction is exceptional and may require governed migration/withdrawal; ordinary editorial change cannot use that label as a bypass.
12. Exact OQ-013 resource/index/delivery-reference design and OQ-016 publication-operation mechanics remain deliberately open for JIT.
13. `PRG-GAP-005` is narrowed to explicit OQ-013/OQ-016 implementation detail rather than broad semantic uncertainty.
14. `PRG-GAP-011` records the unresolved required-content-withdrawal programme consequence and is routed to later completion/substitution/recovery adjudication before any implementation invents a rule.
15. No new Domain and no new upstream `PRG-UPD-###` is justified by Pass 3.

**Pass hard stop:** Pass 4 has not started. Edition/Cohort semantics remain deliberately unexamined beyond references necessary to test content binding.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.
