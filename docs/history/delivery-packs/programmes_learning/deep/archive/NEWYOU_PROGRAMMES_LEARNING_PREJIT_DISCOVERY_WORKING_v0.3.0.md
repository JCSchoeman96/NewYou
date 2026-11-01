# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.3.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.3.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 2 — Programme identity and ProgrammeVersion semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.2.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused Programme / ProgrammeVersion discovery pass while preserving v0.1.0 and v0.2.0 unchanged.

> This is an append-only semantic successor. Read v0.1.0, then v0.2.0, then this pass. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap or current Open Work.

> Nuwe Jy remains the first concrete programme acceptance test. Reusable abstractions must emerge from approved NewYou outcomes, not generic LMS convention.

---

# 17. Working-lock discipline introduced for the discovery stream

The user has approved the separated-pass method and requested a working document that tracks and locks down accepted decisions and pressure tests.

For this Pre-JIT stream, an accepted pass may therefore be marked:

`WORKING_LOCKED / NON-AUTHORITATIVE`

This means only:

- the conclusion is stable inside this Pre-JIT working stream after user acceptance;
- later passes must not silently rewrite it;
- if later evidence contradicts it, a successor ledger records an explicit refinement/supersession such as `PRG-REF-###`;
- open gaps remain open and are not disguised as locked conclusions;
- this working lock does **not** create Product Law, Architecture Law, Domain Law, Roadmap authority, implementation authority or a governance decision;
- authoritative promotion still follows the governed project process.

Pass 1 is therefore treated as `WORKING_LOCKED / NON-AUTHORITATIVE` subject to its explicit unresolved/deferred items.

---

# 18. Pass 2 — Programme identity and ProgrammeVersion semantics

## 18.1 Scope hard stop

This pass answers only:

1. what semantic responsibility belongs to `Programme` versus `ProgrammeVersion`;
2. what must be pinned when a participant enrols;
3. when an approved/delivered ProgrammeVersion may or may not change in place;
4. what “latest approved version” means and does **not** mean;
5. how Nuwe Jy Edition version binding constrains later implementation;
6. what kinds of proposed change clearly require a successor ProgrammeVersion;
7. which versioning assumptions are unsupported/YAGNI; and
8. whether current authority defines the boundary between “new ProgrammeVersion” and “new Programme identity” strongly enough for all future cases.

This pass deliberately does **not** decide:

- detailed ContentVersion / locale correction binding — Pass 3;
- Edition/Cohort cardinality, schedule ownership or exceptional edition lifecycle — Pass 4;
- entitlement lapse/reacquisition — Pass 5;
- release sequencing — Pass 6;
- source evidence contracts — Pass 7;
- completion thresholds/adjudication — Pass 8;
- exemption/substitution semantics — Pass 9;
- recovery/catch-up detail — Pass 10.

A content, edition or completion issue encountered here is routed to its later dedicated pass unless it invalidates ProgrammeVersion semantics themselves.

---

## 18.2 Pass-2 authority evidence

### PRG-EV-013 — Live main reconfirmed for Pass 2

At the start of this pass, live `main` remained:

`086ade7b28c000de1c387acb9760e5eb08bb0413`

No newer authoritative main state was observed before this pass.

### PRG-EV-014 — Programme and ProgrammeVersion are distinct governed concepts

`DEC-147` remains LOCKED and explicitly uses:

`Programme → ProgrammeVersion → Module → Lesson → Activity`.

Current Domain Law separately names Programme and Programme Version as major Programmes & Challenges concepts and assigns that Domain ownership of programme definitions/versions and participant enrolment/version history.

### PRG-EV-015 — Programme carries catalogue identity/lifecycle meaning

Current Product Law §21F.2 says each programme defines purpose, audience, eligibility, risk class, expected duration, structure, completion rules, approvals and entitlements, and gives the programme catalogue lifecycle:

`draft → internal → pilot → public → paused → retired`.

This establishes a stable conceptual/catalogue layer above an individual ProgrammeVersion, but it does not by itself assign every listed field to a specific database record or declare a separate ProgrammeVersion state machine.

### PRG-EV-016 — ProgrammeVersion is the pinned participant-semantic unit

Current Product Law §21F.10 establishes:

- new enrolments normally use the latest approved version;
- active participants remain on their enrolled version unless a minor correction applies, an optional governed migration is accepted, or a safety correction requires migration or withdrawal;
- material changes create a new programme version;
- progress mapping must be explicit when migration occurs;
- completed history never changes silently.

`DEC-156` independently locks the active-enrolment rule: keep active enrolments on their version unless governed migration or safety correction applies.

### PRG-EV-017 — Nuwe Jy Editions bind an explicit source ProgrammeVersion

Nuwe Jy Product Law uses:

`Nuwe Jy Programme → approved ProgrammeVersion → ChallengeEdition → one or more Cohorts`.

A `ChallengeEdition` explicitly defines its `source programme version`, and edition activation validates the edition against its configured content, translations, schedule, sessions, safety, facilitation, products, community and communications.

Therefore an edition is not a floating reference to “whatever ProgrammeVersion is latest today”.

### PRG-EV-018 — Domain Law requires version stability for active enrolment

Current Programmes & Challenges Domain Law states that the version is immutable for active enrolment unless governed migration applies, and lists as an invariant that active enrolment remains tied to its programme/version unless governed migration/safety correction applies.

### PRG-EV-019 — FP-008 requires only evidence-backed programme/version primitives

Current FP-008 validation explicitly says the first concrete Nuwe Jy composition should drive only the reusable `programme/version/edition/cohort` primitives genuinely needed by the platform.

This is direct authority against speculative generic course-versioning infrastructure.

---

# 19. Pass-2 accepted working conclusions

Subject to the explicit gaps/deferred items below, the following are `WORKING_LOCKED / NON-AUTHORITATIVE` after acceptance of this pass.

## 19.1 Programme is the stable conceptual/catalogue identity

A Programme represents the durable conceptual programme the platform recognises across versions and deliveries.

It is the natural owner of catalogue-level identity/lifecycle such as whether that conceptual programme is draft/internal/pilot/public/paused/retired.

A Programme is **not**:

- a single delivered edition;
- a participant enrolment;
- an entitlement;
- a ContentVersion;
- a mutable container whose current child version silently rewrites old participant history.

## 19.2 ProgrammeVersion is the version-pinned participant-semantic contract

A ProgrammeVersion is the governed version of programme semantics that an enrolment/edition can point to.

At minimum, a version boundary matters when the participant-facing programme meaning changes materially, including changes to structure, ordering where required, progression/prerequisite meaning, activity requirement meaning, completion meaning or another programme obligation that would make historical participation mean something different.

This is a semantic conclusion, not a schema prescription.

## 19.3 Approved/in-use ProgrammeVersion semantics must not be mutated in place

Once a ProgrammeVersion is approved and is used as the source for an active edition/enrolment, implementation must not edit participant-facing programme semantics in place and pretend historical participants were always governed by the new meaning.

Material change creates a successor ProgrammeVersion.

Draft/pre-approval authoring mechanics remain JIT detail; this pass does not require a full ProgrammeVersion lifecycle enum.

## 19.4 “Latest approved version” is a selection rule, not a live pointer

For a new enrolment that is not otherwise pinned by an edition/configured delivery, Product Law says the participant normally enters the latest approved ProgrammeVersion.

The chosen version must then become explicit durable enrolment provenance.

An active enrolment must **not** continually resolve `programme.latest_version` and thereby auto-upgrade itself.

## 19.5 Edition source ProgrammeVersion overrides a generic “latest” lookup

When a participant enrols into a configured Edition, the Edition's explicit source ProgrammeVersion is the governing source.

If V2 becomes latest while an Edition is still configured against V1, that does not itself rebind the Edition or its participants to V2.

Any permitted Edition source-version change requires governed revalidation and must not silently rewrite existing enrolments. Exact pre-activation/active Edition rules remain Pass 4.

## 19.6 Completed history remains version-pinned

Completion, partial completion, participation history and historical explanation remain associated with the ProgrammeVersion under which they were evaluated.

Programme retirement, a newer ProgrammeVersion or later editorial changes do not silently restate old participation as though it occurred under the newer version.

## 19.7 Minor correction is not permission for semantic mutation

Product Law recognises a minor-correction path for active participants.

For Pass 2, the safe boundary is:

- a correction that does not change programme-semantic obligations may be handled through the governed correction mechanism;
- a correction that changes programme meaning/requirements/progression/completion must not be smuggled through as “minor”; it requires a successor ProgrammeVersion or explicit safety/migration route.

Exact ContentVersion/locale binding and correction representation is deliberately deferred to Pass 3.

## 19.8 ProgrammeVersion numbering format is not Product Law

Nothing in current Product/Domain authority requires ProgrammeVersion identifiers to use SemVer, integer versions, dates, release names or LMS-style revision numbers.

The implementation needs stable identity and historical ordering/provenance sufficient for governed behaviour, but a generic semantic-versioning engine for programmes is `DEFER_YAGNI` unless a concrete business requirement appears.

## 19.9 Programme catalogue lifecycle must not be copied automatically onto ProgrammeVersion

`draft/internal/pilot/public/paused/retired` is explicitly the Programme catalogue/release lifecycle in current Product Law.

Pass 2 finds no authority for blindly giving ProgrammeVersion an identical independent state machine.

The implementation will need a governed way to distinguish an approved/selectable version from unfinished authoring, because Product Law uses “latest approved version”, but the exact representation/state vocabulary remains JIT detail unless a Product contradiction appears.

## 19.10 One ProgrammeVersion may support multiple Editions

Nuwe Jy Product Law explicitly allows a later evergreen edition to reuse an approved ProgrammeVersion with different scheduling, support and community rules.

Therefore “new Edition” does **not** imply “new ProgrammeVersion”.

Creating one ProgrammeVersion per Edition merely to hold scheduling/operations configuration is rejected.

## 19.11 ProgrammeVersion is not a duplicate ContentVersion

ProgrammeVersion captures programme semantics; Content & Media owns immutable content/locale versions.

A programme version may bind/reference content, but it must not become a second CMS or duplicate content payload/version authority.

Exact binding/correction semantics remain Pass 3.

## 19.12 New Programme identity versus new ProgrammeVersion is not fully governed for extreme redefinition

Current authority proves that material programme changes create a new ProgrammeVersion, and it also says a Programme defines purpose, audience, eligibility, risk class and other catalogue semantics.

It does **not** explicitly define the threshold at which a proposed change is so fundamental that it should become a new Programme identity rather than another ProgrammeVersion of the existing Programme.

Pass 2 therefore adopts a conservative escalation rule:

- normal evolution of the same approved programme concept may use a successor ProgrammeVersion;
- a change that fundamentally changes the participant promise/outcome/purpose/audience/risk identity must not be classified by implementation alone;
- when such a concrete change is proposed, Product review must decide whether it is still the same Programme.

This is an explicit gap trigger, not permission to invent a generic classifier now.

---

# 20. Pass-2 pressure tests

## PRG-PT-041 — V2 approved while V1 participant is active

**Scenario class:** version pinning.

**Scenario:** Nuwe Jy V1 has active enrolments. V2 is approved.

**Expected invariants:**

- existing V1 enrolments remain V1;
- “latest approved” changes the default selection for applicable future enrolments only;
- V1 history is not rewritten;
- migration requires an explicit governed path.

**Analysis:** Product and Domain Law are explicit.

**Disposition:** `PASS`.

---

## PRG-PT-042 — New direct enrolment after V2 approval

**Scenario class:** version selection.

**Scenario:** a programme allows direct/evergreen enrolment and V2 is the latest approved version.

**Expected invariants:**

- the enrolment normally resolves V2 at creation;
- exact V2 identity is persisted with the enrolment;
- later V3 approval does not mutate that enrolment.

**Analysis:** this is the safe interpretation of “new enrolments normally use the latest approved version”.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Refinement:** edition-bound enrolment is handled by the edition's explicit source version rather than generic latest-version selection.

---

## PRG-PT-043 — New enrolment into a V1 Edition after V2 becomes latest

**Scenario class:** Edition/version binding.

**Scenario:** an approved Nuwe Jy Edition was created from V1. Before its enrolment window closes, V2 becomes the newest approved ProgrammeVersion.

**Expected invariants:**

- the Edition remains bound to V1 unless explicitly governed/revalidated otherwise;
- participants entering that Edition receive V1 semantics;
- “latest approved” does not silently override the Edition source version.

**Analysis:** ChallengeEdition explicitly stores its source ProgrammeVersion; treating that as a floating latest pointer would make the field meaningless and violate historical version stability.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Deferred:** exact Edition source-version amendment rules belong Pass 4.

---

## PRG-PT-044 — Change a required activity in approved V1 in place

**Scenario class:** material semantic mutation.

**Scenario:** an operator changes an activity from optional/recommended to required-for-completion on an approved V1 that already has participants.

**Expected invariants:**

- historical V1 obligations do not change in place;
- a material requirement change uses a successor ProgrammeVersion;
- active V1 participants stay on V1 unless a governed migration/safety route applies.

**Analysis:** requirement/completion meaning is exactly the class of programme semantics that version pinning protects.

**Disposition:** `PASS` — in-place mutation rejected.

---

## PRG-PT-045 — Reorder required progression in approved V1

**Scenario class:** material structural/progression mutation.

**Scenario:** modules/lessons are reordered so a previously available activity now depends on another prerequisite.

**Expected invariants:**

- active historical semantics cannot be silently changed;
- materially changed progression belongs to a successor ProgrammeVersion;
- any migration requires explicit mapping.

**Analysis:** Product Law explicitly allows ordering/prerequisite meaning and requires explicit progress mapping on migration.

**Disposition:** `PASS`.

---

## PRG-PT-046 — Change completion threshold in place

**Scenario class:** completion/version boundary.

**Scenario:** a ProgrammeVersion changes the percentage/minimum participation/final check-in rule after participants started.

**Expected invariants:**

- completion rule meaning is versioned;
- old enrolments remain evaluated under their governing version unless an approved correction/migration rule says otherwise;
- JIT cannot “fix” the threshold by editing V1.

**Analysis:** versioned completion rules are locked; exact threshold is still OQ-019/OQ-025.

**Disposition:** `PASS` for version-boundary semantics / `DEFER_TO_PASS_8` for the actual threshold.

---

## PRG-PT-047 — Create a new ProgrammeVersion solely because the Edition dates changed

**Scenario class:** ProgrammeVersion/Edition separation.

**Scenario:** the same programme semantics are delivered in a later cohort with different start date, release dates, facilitators, community destination or support schedule.

**Expected invariants:**

- delivery/operations changes do not automatically manufacture a new ProgrammeVersion;
- the later Edition may reuse the approved ProgrammeVersion when underlying programme semantics are unchanged.

**Analysis:** Product Law explicitly anticipates an evergreen Edition reusing an approved ProgrammeVersion with different scheduling/support/community rules.

**Disposition:** `PASS` — automatic version-per-edition model rejected.

**Deferred:** exact Edition configuration rules belong Pass 4.

---

## PRG-PT-048 — Create a new ProgrammeVersion for every content typo correction

**Scenario class:** ProgrammeVersion/ContentVersion separation.

**Scenario:** one lesson text receives a typographical correction without changing the programme obligation or meaning.

**Expected invariants:**

- ProgrammeVersion must not become a duplicate ContentVersion history;
- a non-semantic correction should not automatically create a new ProgrammeVersion solely because Content created a new traceable version/correction;
- original delivery remains explainable.

**Analysis:** the high-level boundary is clear, but exact correction binding belongs the Content pass.

**Disposition:** `PASS_WITH_REFINEMENT / DEFER_TO_PASS_3`.

---

## PRG-PT-049 — Treat a material content rewrite as “same ProgrammeVersion” because only Content changed

**Scenario class:** semantic boundary across Domains.

**Scenario:** Content publishes a replacement that materially changes what the participant is required to understand/do, but Programmes keeps the same ProgrammeVersion because the content body lives elsewhere.

**Expected invariants:**

- Domain ownership does not permit semantic evasion;
- if the content change changes programme obligations/requirements/progression/completion meaning, ProgrammeVersion review is required;
- Content remains the body/version owner.

**Analysis:** ProgrammeVersion semantics are determined by business meaning, not which table/file was edited.

**Disposition:** `PASS_WITH_REFINEMENT / DEFER_TO_PASS_3` for exact binding.

---

## PRG-PT-050 — Safety correction edits historical ProgrammeVersion semantics in place

**Scenario class:** exceptional safety correction.

**Scenario:** a previously approved activity becomes unsafe for some/all participants and an operator overwrites V1 so the old activity appears never to have existed.

**Expected invariants:**

- safety outranks convenience;
- unsafe future delivery can be blocked/replaced through governed safety correction;
- original ProgrammeVersion/history/provenance is not erased;
- active enrolment may require governed migration/withdrawal/restriction.

**Analysis:** Product Law explicitly recognises safety correction as exceptional, not as permission to rewrite history.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Deferred:** Content replacement mechanics to Pass 3; participant safety consequences to the later Safety pass.

---

## PRG-PT-051 — Give ProgrammeVersion the same draft/internal/pilot/public/paused/retired state machine as Programme

**Scenario class:** speculative lifecycle duplication.

**Scenario:** implementation copies the Programme catalogue lifecycle enum onto every ProgrammeVersion because it looks convenient.

**Expected invariants:**

- Product Law's Programme lifecycle is not silently redefined as a ProgrammeVersion lifecycle;
- implementation still needs a way to identify approved/selectable versions;
- no extra version states are invented without a concrete semantic need.

**Analysis:** current authority names a Programme catalogue lifecycle and separately speaks of an “approved” ProgrammeVersion, but does not lock a matching Version lifecycle.

**Disposition:** `DEFER_YAGNI` for a mirrored lifecycle; `JIT_ONLY` for the minimum approval/selectability representation.

---

## PRG-PT-052 — Use SemVer ordering as Programme business meaning

**Scenario class:** unsupported convention.

**Scenario:** implementation assumes ProgrammeVersion `2.0.0` is a breaking programme change, `1.1.0` adds optional material, and `1.0.1` is a minor correction.

**Expected invariants:**

- documentation SemVer conventions do not become programme business semantics by analogy;
- materiality is determined by governed programme meaning, not numeric version formatting;
- exact version label format may remain simple.

**Analysis:** no Product authority defines SemVer semantics for participant programmes.

**Disposition:** `DEFER_YAGNI`.

---

## PRG-PT-053 — Delete old ProgrammeVersion after all active participants finish

**Scenario class:** historical integrity.

**Scenario:** no one is currently active on V1, so implementation deletes V1 after V2 is public.

**Expected invariants:**

- completed/repeat enrolment history remains explainable;
- old version identity remains available for historical provenance subject to privacy/deletion law;
- programme retirement/supersession is not equivalent to erasing ProgrammeVersion history.

**Analysis:** completed history never changes silently and repeat enrolment history is preserved.

**Disposition:** `PASS` — destructive version deletion as ordinary lifecycle rejected.

---

## PRG-PT-054 — Create one ProgrammeVersion per Edition to simplify joins

**Scenario class:** data-model convenience versus business truth.

**Scenario:** every new cohort/edition clones the same programme semantics into a new ProgrammeVersion to avoid Edition→Version references.

**Expected invariants:**

- version identity tracks semantic change, not operational convenience;
- multiple Editions can reuse one ProgrammeVersion;
- history should not falsely imply programme meaning changed when only delivery configuration changed.

**Analysis:** this would create false semantic versions and undermine FP-008's evidence-led reuse model.

**Disposition:** `PASS` — clone-per-edition model rejected.

---

## PRG-PT-055 — Fundamentally repurpose an existing Programme and call it V2

**Scenario class:** Programme identity boundary.

**Scenario:** an existing programme's purpose, target audience, risk profile and promised outcome are substantially changed, while implementation retains the same Programme identity and merely creates V2.

**Expected invariants:**

- Programme identity remains meaningful across versions;
- a fundamental redefinition cannot be classified solely for implementation convenience;
- enrolment/history/catalogue analytics must not misleadingly conflate genuinely different participant products.

**Analysis:** authority says material changes create a new ProgrammeVersion, but also assigns purpose/audience/eligibility/risk identity to Programme. It does not give a precise threshold for when a redefinition becomes a new Programme rather than a new version.

**Disposition:** `INSUFFICIENT_AUTHORITY_FOR_EXTREME_IDENTITY_CHANGE`.

**Promotion:** `PRG-GAP-010`.

---

## PRG-PT-056 — Programme paused/retired while historical versions exist

**Scenario class:** catalogue lifecycle versus historical version truth.

**Scenario:** Programme is paused or retired after several ProgrammeVersions have been delivered.

**Expected invariants:**

- catalogue state does not erase historical ProgrammeVersions/enrolments;
- old completion/provenance remains tied to the delivered version;
- “retired” does not mean rewrite/delete participant history.

**Analysis:** catalogue lifecycle and historical enrolment/version truth are separate dimensions.

**Disposition:** `PASS`.

**Deferred:** exact current access/new-enrolment consequences belong later entitlement/delivery passes.

---

# 21. Pass-2 gap adjudication

## PRG-GAP-010 — Programme identity boundary under fundamental redefinition

- **Classification:** PRODUCT_SEMANTIC_GAP / CONCRETE-CHANGE TRIGGERED
- **Origin:** PRG-PT-055.
- **Authority already present:** Programme and ProgrammeVersion are distinct; material changes create new ProgrammeVersion; Programme defines purpose/audience/eligibility/risk class and catalogue lifecycle.
- **Missing semantic:** no explicit threshold states when a proposed change ceases to be evolution of the same Programme and instead constitutes a different Programme identity.
- **Why it matters:** silently treating fundamentally different products as one Programme can corrupt participant expectations, repeat-enrolment meaning, catalogue history, analytics and future entitlement/offer semantics.
- **Why it is not an FP-008 initial blocker:** the first Nuwe Jy Programme/ProgrammeVersion does not require classifying a future fundamental redefinition in order to model the initial version correctly.
- **Working action:** do not build a generic automatic classifier. When a concrete future change materially alters the participant promise/outcome/purpose/audience/risk identity, stop and route that concrete change to Product review before deciding Programme versus ProgrammeVersion.
- **Upstream delta now:** NONE. A hypothetical future identity rewrite is not sufficient reason to manufacture a new Product decision/OQ today.
- **Status:** OPEN / NON-BLOCKING FOR INITIAL FP-008 JIT, but implementation must preserve the seam.

No other new Product/Architecture/Domain gap is promoted in Pass 2.

---

# 22. Pass-2 refinements to earlier working synthesis

Earlier files remain immutable. The following explicit refinements now govern this working stream.

## PRG-REF-004 — ProgrammeVersion semantic contract is now narrower and stronger

The v0.1 wording “versioned programme-semantic contract” is confirmed, with an important constraint: it is not a snapshot of every surrounding delivery/configuration fact.

ProgrammeVersion tracks programme meaning. Edition schedule/support/community configuration and ContentVersion bodies remain separate governed truths.

## PRG-REF-005 — “Latest approved” applies at selection time, not continuously

A new applicable enrolment may select the latest approved ProgrammeVersion, but once selected the enrolment carries the exact version. Edition-bound enrolments use the Edition source ProgrammeVersion.

## PRG-REF-006 — Do not manufacture semantic versions for operational Editions

Multiple Editions may reuse one ProgrammeVersion. A new Edition is not evidence of a new ProgrammeVersion.

## PRG-REF-007 — ProgrammeVersion lifecycle enum remains intentionally unfrozen

Current authority requires approved/selectable version semantics but does not lock a ProgrammeVersion lifecycle mirroring Programme catalogue states. JIT must implement only the minimum governed representation required by the Feature Pack rather than inventing an LMS publishing workflow.

---

# 23. Pass-2 anti-LMS/YAGNI outcome

Pass 2 explicitly rejects:

- ProgrammeVersion SemVer business semantics without a Product need — `DEFER_YAGNI`;
- one ProgrammeVersion per Edition/cohort — rejected as false semantic history;
- mutable “current ProgrammeVersion” that rewrites active/completed enrolments — rejected;
- a copied generic LMS course-version publishing state machine — `DEFER_YAGNI` beyond the minimum approval/selectability semantics genuinely required;
- duplicate ProgrammeVersion copies used as delivery configuration containers — rejected.

No generic LMS versioning/import/compatibility feature is justified.

---

# 24. Pass-2 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

The following are now `WORKING_LOCKED / NON-AUTHORITATIVE` for this stream once this pass is accepted:

1. Programme is the stable conceptual/catalogue identity across versions.
2. ProgrammeVersion is the version-pinned participant-semantic contract, not a generic content snapshot or Edition instance.
3. Approved/in-use ProgrammeVersion semantics cannot be materially mutated in place.
4. New applicable enrolments normally select the latest approved version once; active enrolments do not follow a live latest pointer.
5. Edition-bound enrolments use the Edition's explicit source ProgrammeVersion.
6. Multiple Editions may reuse the same ProgrammeVersion.
7. Material programme semantic changes require a successor ProgrammeVersion.
8. Minor correction cannot be used to hide a material semantic change.
9. Completed history stays explainable against its original ProgrammeVersion.
10. Programme catalogue lifecycle and ProgrammeVersion approval/selectability are separate concerns; no mirrored version lifecycle is authorised by current Product Law.
11. Programme version labels/ordering are implementation detail; SemVer business meaning is not required.
12. A future fundamental change to programme purpose/outcome/audience/risk identity triggers Product review for `Programme` versus `ProgrammeVersion`; no automatic classifier is authorised.

**Pass hard stop:** Pass 3 has not started. ContentVersion/locale binding and correction mechanics remain deliberately unexamined beyond the semantic boundary necessary for Pass 2.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.
