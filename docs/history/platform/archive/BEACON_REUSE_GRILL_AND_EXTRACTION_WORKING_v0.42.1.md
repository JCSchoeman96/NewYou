# BEACON REUSE GRILL AND EXTRACTION — WORKING v0.42.1

- **Status:** WORKING / NON-AUTHORITATIVE / PRE-JIT REUSE DISCOVERY
- **Document version:** v0.42.1
- **Date:** 2026-09-21
- **Project:** NewYou / Wellness Platform
- **Purpose:** Evidence-backed extraction and grill dossier for selective reuse of Beacon CMS / Beacon LiveAdmin ideas and source in an Ash-native NewYou Content & Media implementation.
- **Authority:** None. This document does not amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Feature Pack contracts or JIT Domain Dossiers.
- **Implementation:** NOT AUTHORISED.
- **Conflict rule:** Live NewYou authority wins over every recommendation in this dossier.
- **Reuse rule:** No Beacon mechanism becomes NewYou authority merely because it is mature, convenient or already implemented.
- **v0.42.1 PATCH:** No GRILL or architecture semantics changed. This patch repairs stale historical/current-sequence statements found by the whole-source stabilisation audit after `GRILL-41`: the GRILL-28-era “next seam” wording is historically qualified; the pre-GRILL-41 Block 5A closure/next-action text is explicitly historical; and the current grill sequence now includes GRILL-40 and GRILL-41 with Block 5A CLOSED. Accepted `GRILL-01` through `GRILL-41` remain unchanged. Executable implementation remains unauthorised.

---

## 1. Purpose

This dossier exists to answer one bounded question:

> Which exact Beacon CMS / Beacon LiveAdmin mechanisms can NewYou reuse, adapt, reimplement or reject so that future Content & Media delivery is accelerated without importing competing authority, unsafe runtime extensibility, unnecessary dependencies or pre-1.0 architectural coupling?

The intended output is not a proposal to "use Beacon" as NewYou's CMS.

The intended output is a traceable extraction map:

```text
Beacon evidence
→ identify mechanism
→ compare against NewYou authority
→ pressure-test lifecycle / authority / failure / security / maintenance
→ classify REUSE / ADAPT / REIMPLEMENT / REJECT
→ define permitted NewYou seam
→ preserve provenance/licence where source is copied
```

This is a working discovery artifact intended to improve later JIT planning. It cannot authorise implementation.

---

## 2. NewYou live authority basis

The live GitHub repository is canonical. At this dossier's creation, `docs/00_platform/README.md` routes current authority to:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.40.md`
5. `03_ARCHITECTURE_v1.1.0.md`
6. `04_DOMAIN_MAP_v1.1.0.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.0.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` when frontend/content experience is in scope.

Canonical repository:

`https://github.com/JCSchoeman96/NewYou`

### 2.1 Governing NewYou constraints relevant to Beacon reuse

Current authority requires, among other things:

- one modular Elixir/Phoenix/Ash application initially;
- Ash 3.x actions/code interfaces as the normal authoritative application-operation boundary;
- PostgreSQL as default durable structured business authority;
- S3-compatible object storage for durable binary objects, with PostgreSQL governing business metadata/control;
- Oban for durable asynchronous work where justified;
- PubSub for observation/freshness, never durable truth;
- no hard business invariant may depend on process-local state, LiveView state, ETS, PubSub delivery or permanent single-node locality;
- Content & Media owns conceptual content identity, immutable content versions, locale branches/translations, approval/publication lifecycle, taxonomy, governed editorial media identity/derivatives/publication state, and message/template content versions;
- governed runtime content is Ash-backed;
- published governed versions are immutable; corrections supersede or withdraw rather than silently overwrite;
- paid/safety/clinical/core-onboarding content requires approved bilingual variants;
- editors may compose approved blocks/components but may not inject arbitrary HTML, scripts, styles, ungoverned components or arbitrary embeds;
- content operations use the Library + Work Queue + Editorial Calendar model;
- scheduled publication must be durable, idempotent, observable and reconciled;
- Content & Media Domain Architecture Profile lists `GenServer: NONE initially`, `Oban: APPLICABLE`, and PubSub only for freshness;
- Search/discovery remains a derived projection, not publication or access authority;
- Experimentation owns experiment configuration/assignment/decision authority; Analytics owns derived evidence;
- current unresolved gates include OQ-013 translation resource model, OQ-014 edge/cache design, OQ-015 search configuration and OQ-016 scheduled publication operations.

These rules are constraints on reuse. Beacon code that conflicts with them is evidence to study, not code to transplant.

---

## 3. Beacon evidence baseline

### 3.1 Beacon CMS stable baseline

- **Repository:** `https://github.com/BeaconCMS/beacon`
- **Latest Beacon CMS stable release at review:** `v0.5.1`
- **Release date:** 2025-04-01
- **Annotated tag object SHA:** `565587625714465643888a64f62a62f553daab9e`
- **Tagged commit SHA:** `97024750c88d7ccce34e21e802d8936c8e83c573`
- **Hex package:** `beacon 0.5.1`
- **Licence:** MIT, Copyright © 2021 DockYard, Inc.
- **Project status stated by upstream:** incomplete features and breaking changes are expected before a stable v1.0.

Stable Beacon 0.5.1 depends at runtime on Phoenix, LiveView, Ecto SQL, Postgrex, ExAws/S3, Image/Vix, PubSub, Markdown tooling and other CMS/runtime support libraries. This dependency surface is one reason NewYou should not adopt the entire package merely to obtain a few content mechanisms.

### 3.2 Beacon LiveAdmin stable baseline

- **Repository:** `https://github.com/BeaconCMS/beacon_live_admin`
- **Latest stable release at review:** `v0.4.3`
- **Release date:** 2025-03-31
- **Annotated tag object SHA:** `17ee8a75c2ebb461a4d6f6585d3078275b93a596`
- **Tagged commit SHA:** `0ba64699ad76407e31d962fddda16bad6275a027`
- **Licence:** MIT
- **Notable dependency direction:** Beacon LiveAdmin depends on Beacon and also introduces LiveSvelte and editor/admin infrastructure.

### 3.3 Unreleased `main`

Beacon `main` contains material evolution beyond stable v0.5.1, including a redesigned runtime renderer and other changes. Unreleased `main` may be studied as forward evidence but must be labelled `UNRELEASED / NON-STABLE` and must not be treated as a stable dependency contract.

Direct-copy decisions in this dossier must pin an exact stable tag/blob or an explicitly reviewed commit SHA.

---

## 4. Classification vocabulary

### `REUSE`

Small, isolated source or behaviour is suitable for direct or near-direct reuse under MIT, subject to licence/provenance and NewYou integration review.

### `ADAPT`

Beacon contains a strong concept, algorithm, data relationship or UI pattern, but NewYou should implement it through its own Ash/Phoenix/application boundaries.

### `REIMPLEMENT`

Beacon proves the problem and provides useful implementation evidence, but its actual implementation is materially coupled to Beacon's Ecto/runtime architecture or is insufficient for NewYou's invariants. Use it as reference/test evidence, not source.

### `REJECT`

The mechanism conflicts with NewYou authority, creates a competing source of truth, weakens security/governance, or introduces unjustified dependency/runtime complexity.

### `DEFER`

Potentially useful, but current authority or evidence does not justify deciding it yet.

---

## 5. Executive extraction map — research baseline

| Beacon subsystem | Stable source | Baseline classification | NewYou use |
|---|---|---|---|
| Component definition | `lib/beacon/content/component.ex` | ADAPT — HIGH VALUE | Inform a governed block/component catalogue |
| Component attributes | `lib/beacon/content/component_attr.ex` | ADAPT — HIGH VALUE | Typed attributes, required/default/allowed-value/editor metadata concepts |
| Component slots | `lib/beacon/content/component_slot.ex` | ADAPT — HIGH VALUE | Governed composition/slot model |
| Slot attributes | `lib/beacon/content/component_slot_attr.ex` | ADAPT — HIGH VALUE | Typed slot configuration concepts |
| Page custom fields | `lib/beacon/content/page_field.ex` | ADAPT CAREFULLY | Extension-point pattern only; important NewYou truth stays first-class |
| Page model | `lib/beacon/content/page.ex` | ADAPT MUTABLE-WORKING-STATE SEPARATION / REJECT DIRECT AUTHORITY | Supports the mutable-authoring concept now owned by NewYou `ContentDraft`; Beacon Ecto Page is not reused as business authority |
| Page event | `lib/beacon/content/page_event.ex` | REFERENCE ONLY / REJECT AS NEWYOU LIFECYCLE AUTHORITY | Useful evidence that publication is an event/consequence; Beacon's simple event lifecycle is insufficient for NewYou review/approval/publication/correction separation |
| Page snapshot | `lib/beacon/content/page_snapshot.ex` | ADAPT CONCEPT / REJECT SERIALISED-STRUCT APPROACH | Informs exact `ContentDraft` revision → immutable `ContentVersion` snapshot boundary; NewYou owns first-class version truth |
| Page variants | `lib/beacon/content/page_variant.ex` | REJECT FOR EXPERIMENT AUTHORITY | Rendering reference only; NewYou Experimentation remains authority |
| Layout + layout snapshots | `lib/beacon/content/layout*.ex` | ADAPT NARROWLY | Reusable composed presentation patterns, not mutable runtime layout authority |
| Beacon lifecycle hooks | `lib/beacon/lifecycle.ex` | REIMPLEMENT NARROWLY | Prefer explicit domain consequences, not open-ended CMS lifecycle injection |
| Beacon router / router server | `lib/beacon/router.ex`, `lib/beacon/router_server.ex`, `lib/beacon/loader/routes.ex` | ADAPT BOUNDED ROUTING CONCEPT / REJECT AS CONTENT AUTHORITY | Reuse path uniqueness/URL-generation/mounting ideas only; C&M owns durable published route claims while Phoenix/ETS remain delivery/projection mechanisms |
| Runtime content loading / ETS | stable loader/runtime mechanisms | REJECT INITIALLY | No correctness dependency on process/ETS; future acceleration evidence-gated |
| HEEx runtime template compilation | template modules | REJECT FOR EDITORS | Compiled NewYou renderers + governed data instead |
| Markdown template support | template modules | DEFER / POSSIBLE PACKAGE-LEVEL REUSE | Allow only where a content type genuinely benefits |
| Stylesheets as CMS content | `Content.Stylesheet` | REJECT | NewYou design tokens/application styles remain code/design-system authority |
| Custom JS hooks as CMS content | `Content.JSHook` | REJECT | JavaScript remains application code |
| Custom executable helpers | Page helpers/runtime code | REJECT | No shadow deployment mechanism in content DB |
| Media asset/source relationship | `media_library/asset.ex` | ADAPT — HIGH VALUE | Master/derivative lineage model |
| Media custom fields | `media_library/asset_field.ex` | ADAPT CAREFULLY | Optional extension metadata only |
| Media provider abstraction | `media_library/provider.ex` | ADAPT — HIGH VALUE | Platform-owned replaceable object-storage capability boundary |
| S3 provider | `provider/s3.ex` + signed/unsigned wrappers | REIMPLEMENT | Interface/reference only; stable delete semantics are insufficient |
| Image processor | `processors/image.ex` | REIMPLEMENT | Processing pipeline shape, not hard-coded variants |
| Upload metadata pipeline | `upload_metadata.ex` | ADAPT | Upload/validation/processing context pattern |
| LiveAdmin PageBuilder.Table | `page_builder/table.ex` | SELECTIVE REUSE CANDIDATE | Pagination/filter/sort state and navigation helpers |
| LiveAdmin AdminComponents | `components/admin_components.ex` | SELECTIVE REUSE / ADAPT | Generic table/search/sort/pagination/editor UX patterns |
| LiveAdmin PageBuilder | `page_builder.ex` | REIMPLEMENT / REFERENCE | Operator-shell extension concept only; NewYou owns Command Centre/Work UX |
| LiveSvelte visual editor stack | LiveAdmin dependency/editor | REJECT INITIALLY | Do not add second frontend model without evidence |
| Beacon multisite abstraction | site config/types | REJECT | NewYou product spaces are not generic CMS tenants |

This table is a research baseline, not an approved design. **A baseline classification is promoted, narrowed, replaced or rejected only where a later numbered GRILL explicitly decides that seam. The accepted GRILL register and the latest conclusion control over stale baseline wording in this table.**

`GRILL-22` adds a current interpretation relevant to the earlier block-storage baseline:

```text
GRILL-03 Content-Version-owned structured block storage
→ remains valid for shared language-neutral composition

GRILL-22
→ localisable block values are governed by exact ContentTranslationVersion truth
→ locale versions do not own duplicate independent block trees
```

Beacon supplies no direct translation/version donor for this split; it is reimplemented from NewYou Product/Architecture/Domain law.


`GRILL-37` adds a current interpretation relevant to the media deletion baseline:

```text
MediaAssetVersion-scoped disposition
→ permanently suppresses that exact version
→ does not require destruction of shared immutable bytes while another lawfully retained version still requires them

whole MediaAsset terminal disposition
→ retires the stable asset identity
→ later identical bytes must enter under a new stable MediaAsset identity

byte-level destruction requirement
→ expands impact to every version that depends on those bytes
→ byte sharing never evades deletion policy
```

Beacon supplies no direct donor for this subject-scoped deletion/share accounting model. Exact storage-reference accounting remains JIT rather than a reason to create a `MediaBlob` business Resource now.

`GRILL-39` adds a current interpretation relevant to the earlier router baseline:

```text
pre-publication locale slug/path wording
→ governed locale authoring/version truth
→ no historical public-address obligation yet

first eligible public Publication
→ claims a durable locale-specific public address

successor Publication at same address
→ address remains stable; exact published target changes

successor Publication at a new address
→ new canonical address
→ prior exposed address becomes governed historical redirect

Phoenix router / generated route module / ETS / sitemap / search index / cache
→ delivery/projection/acceleration only
→ rebuildable from C&M route-claim + Publication truth
```

Beacon's stable `Page.path`, URL generation, Phoenix mounting and published-page sitemap patterns remain useful reference evidence, but mutable `Page.path`, arbitrary CMS catch-all route authority and process-local route tables are not adopted as NewYou business authority.

---

## 6. Block 1A — where an allowed NewYou block definition lives

### 6.1 Scope boundary

This revision resolves one question only:

> Where is the authoritative definition of an allowed NewYou content block?

It does **not** decide:

- how a block instance is persisted;
- whether instances are child Ash Resources, embedded Resources, unions, structured values or another representation;
- composition/container modelling;
- publication/version Resources;
- translation representation;
- editor implementation;
- media, SEO, scheduling or caching;
- the general direct-source-copy policy.

Those remain separate grills.

### 6.2 Governing NewYou constraints

Current authority requires an extensible, approved catalogue of blocks, sections, content components and composed patterns. The catalogue grows from real content needs and review and is explicitly not an unrestricted page builder. Editors may compose approved building blocks but may not inject arbitrary HTML, scripts, styles, ungoverned components or arbitrary embeds.

Current authority also requires governed runtime content to be Ash-backed and published governed versions to remain immutable.

These constraints mean NewYou needs editor flexibility **inside** approved capabilities, not runtime authority to invent new executable capabilities.

### 6.3 Beacon stable evidence inspected

Beacon `v0.5.1`:

- `lib/beacon/content/component.ex` — blob `154e77cf5ece5cae100f1bf4285e22f321b49f4d`
- `lib/beacon/content/component_attr.ex` — blob `82714f2d8271908a82e44d2e408dfd8039d8c971`
- `lib/beacon/content/component_slot.ex` — blob `6c76dc4778b9de263b4dcdc60fec0772abaca81e`
- `lib/beacon/content/component_slot_attr.ex` — blob `4a56b537af9922f39ac43cca009cc647d97a48f7`

Beacon usefully models typed attributes, required/default semantics, accepted values/examples, named slots, slot attributes, categories and editor-facing description/example metadata.

Beacon also persists the component definition itself, including template-oriented material, and persists some options using Beacon binary-term storage. Those persistence/runtime choices are not automatically reusable merely because the component vocabulary is useful.

### 6.4 Models pressure-tested

#### Model A — code-authoritative block catalogue

The definition of what a block **is** lives in versioned application code. Governed database content stores uses/instances of approved block types and their values.

Conceptually:

```text
compiled/versioned block contract
    ├─ stable block type key
    ├─ accepted fields / slots
    ├─ types / constraints
    ├─ allowed values / defaults
    ├─ validation behaviour
    └─ compiled renderer behaviour
             ↓
governed content stores block instances
```

Pressure-test result:

- aligns with the approved-catalogue / no-arbitrary-code rule;
- keeps executable rendering inside the application deployment boundary;
- avoids runtime races over mutable schema definitions;
- fits Ash's static Resource/type/action model and its introspection capabilities;
- does not require a second schema interpreter in PostgreSQL;
- still permits data-driven templates/composed patterns later, provided they only compose approved block capabilities;
- requires explicit representation/schema version provenance so later releases cannot silently reinterpret immutable published content.

#### Model B — PostgreSQL/Ash `BlockDefinition` as runtime authority

A durable record defines fields, slots, defaults, validation and potentially renderer/template information.

Pressure-test result:

- introduces mutable runtime schema authority that NewYou does not currently require;
- risks reducing the Ash model to a generic `type + data map` wrapper whose real validation contract is interpreted elsewhere;
- creates additional lifecycle/version/compatibility/deprecation/rollback concerns for block definitions themselves;
- creates a new concurrency problem when drafts were created under one definition and save/publish under another;
- becomes especially dangerous if renderer/template behaviour is persisted as executable content.

No current higher authority requires this runtime flexibility.

**Disposition: REJECT initially.**

#### Model C — hybrid split authority

Code defines a block while PostgreSQL also defines material field/default/constraint semantics.

Pressure-test result:

A broad hybrid can make both code and database records answer “what is this block?”. Even apparently harmless mutable defaults can silently change future rendering or require published versions to capture them anyway.

The useful part of “hybrid” is therefore narrowed: **content values and later templates/composed patterns may be data-driven; primitive block capability definitions are not split across code and mutable DB schema authority.**

**Disposition: reject broad split-authority hybrid for the initial design.**

### 6.5 Ash-specific conclusion

The accepted direction deliberately does not invent a final Ash Resource model yet.

Ash makes a code-authoritative catalogue viable because static Resources/types/actions/validations are introspectable. That provides a path for editor-generation and server validation without introducing a mutable `BlockDefinition` business Resource solely to describe the schema.

**Historical at GRILL-01 acceptance:** instance persistence was deferred to Block 1B. `GRILL-03` subsequently fixes the structured/embedded Content-Version-owned baseline, while the exact Ash union/typed representation remains JIT.

### 6.6 Beacon extraction decision for this seam

| Beacon element | v0.2.0 decision |
|---|---|
| Attribute concept | **ADAPT** |
| Attribute typing | **ADAPT** |
| Required/default semantics | **ADAPT** |
| Allowed-value validation | **ADAPT** |
| Slot concept | **ADAPT** |
| Slot attributes | **ADAPT** |
| Editor description/help/example metadata | **ADAPT** |
| Persisted Beacon `Component` as NewYou block-definition authority | **REJECT** |
| Persisted executable component template | **REJECT** |
| Binary-term option persistence | **REJECT** |
| Runtime editor-created primitive block types | **REJECT initially** |

These decisions apply only to the **definition-authority seam**. They do not yet approve a specific persistence model for block instances.

### 6.7 ACCEPTED GRILL DECISION

#### `GRILL-01 — Code-authoritative Block Catalogue`

**Status:** ACCEPTED / WORKING DOSSIER DECISION / NON-AUTHORITATIVE

> The NewYou approved block catalogue is code-authoritative. There is initially no mutable PostgreSQL/Ash `BlockDefinition` business Resource.
>
> Block capabilities, field contracts, allowed options and renderer behaviour are versioned application code.
>
> Governed database content stores **instances of approved block types**, not definitions of new primitive block types.
>
> Templates/composed patterns may later be data-driven, but may only compose already-approved block capabilities.
>
> Published block representations must carry sufficient schema/version provenance to prevent later code changes from silently changing historical meaning.
>
> Editors cannot create or alter primitive block types themselves.

### 6.8 Important consequences now fixed for later grills

Later design must respect these constraints:

1. A content editor may change block **content/configuration values** that the approved contract permits, but may not change the executable definition of the block.
2. A new primitive block capability requires an application change/release rather than an editorial DB mutation.
3. An application release must not silently reinterpret already-published content. Block representation/schema evolution therefore requires explicit compatibility/version semantics.
4. Database-driven templates or composed patterns, if later accepted, cannot become an indirect way to introduce arbitrary executable components.
5. No later implementation should create `BlockDefinition` merely because Beacon has a persisted `Component` schema; a real NewYou requirement would have to justify reopening this decision.

### 6.9 Block 1B.1 — block occurrence identity and lifecycle

This revision resolves one additional question only:

> Does an ordinary block occurrence own independent durable business identity/lifecycle, or is it subordinate to the governed content composition/version in which it occurs?

It does **not** decide how that occurrence is physically persisted or represented in Ash.

#### 6.9.1 Governing distinction: business identity vs addressability

A block occurrence needs a stable way to be targeted by editor operations, reordering, diffs, review references, provenance and later translation correspondence. That does not by itself justify a first-class business entity with independent lifecycle, publication, approval, ownership or authority.

The accepted model distinguishes:

```text
business identity / authority
        !=
stable local occurrence address
```

An ordinary block occurrence is therefore subordinate to its content/version context but carries a stable local occurrence key.

#### 6.9.2 Reordering pressure test

Array position is too weak as identity because moving a block would change its apparent identity. A stable local occurrence key survives reorder operations and supports editor targeting without creating a separate business entity.

#### 6.9.3 Successor-version pressure test

If the same logical occurrence survives from one content version to the next, the local occurrence key may be carried forward for diff/correspondence purposes. Historical truth remains version-bound:

```text
Content v7 + locale + occurrence d4 != Content v8 + locale + occurrence d4
```

The occurrence key alone never identifies what was published. Exact provenance remains bound to the content identity, locale, exact content version, block type/schema version and occurrence.

#### 6.9.4 Removal/correction pressure test

Removing an occurrence from a successor composition does not destroy the historical occurrence in an immutable prior version. Removal is a change in successor composition/version, not destructive deletion of an independently authoritative Block entity.

#### 6.9.5 Review/comment pressure test

Review evidence can target the content/version-under-review plus the occurrence key. This preserves the exact historical review target even if the occurrence is later edited or removed. No independent Block lifecycle is required merely to support comments/review targeting.

#### 6.9.6 Translation pressure test

Current NewYou authority requires separately governed locale branches, while exact translation Resource design remains downstream under OQ-013. GRILL-02 therefore requires enough stable occurrence addressability to support future correspondence, but does not assert that English and Afrikaans occurrences share one database identity.

Translation correspondence remains a separate later decision.

#### 6.9.7 Analytics/provenance pressure test

A future interaction event can identify the delivered object using content identity, published version, locale, occurrence key and block type. Analytics therefore does not require an independently mutable Block entity and must not become content authority.

#### 6.9.8 Reuse pressure test

A genuinely reusable, independently approved/versioned fragment may eventually justify its own governed concept and lifecycle. That requirement must create a separate explicit concept such as a governed reusable fragment rather than turning every ordinary paragraph/image/callout occurrence into shared mutable authority.

#### 6.9.9 Media counterexample

Media demonstrates the boundary clearly. A Media Asset has independent durable truths such as rights, attribution, source/master lineage, derivatives, replacement and withdrawal/deletion semantics. An Image block occurrence may reference a Media Asset; the block occurrence does not thereby inherit Media Asset business identity.

#### 6.9.10 Concurrency pressure test

Giving every block independent mutable authority would force publication to prove which set of independently changing block rows constitutes the exact version being published. The accepted semantic boundary is instead that review/publication captures one exact governed composition/version. Physical persistence remains undecided and may still use rows if later justified; rows do not imply independent authority.

#### 6.9.11 Ash-specific consequence

Ash Resources provide entity-level actions, identity, validation and policy semantics. GRILL-02 therefore prevents choosing a persisted child Resource merely because it is convenient technically. A child Resource is still possible later as an implementation mechanism, but it must remain subordinate in authority/lifecycle unless a later requirement explicitly justifies promotion.

### 6.10 ACCEPTED GRILL DECISION

#### `GRILL-02 — Block Occurrences Are Subordinate, Not Independent Business Entities`

**Status:** ACCEPTED / WORKING DOSSIER DECISION / NON-AUTHORITATIVE

> An ordinary content-block occurrence does not initially own an independent durable business lifecycle or authority.
>
> It exists as part of a governed content composition/version context.
>
> Each occurrence has a stable **local occurrence key** — working terminology only — sufficient to support editor targeting, reordering, diffs, review references, provenance and future translation correspondence.
>
> The occurrence key may be carried forward across successor versions where the same logical occurrence survives, but the key alone never identifies historical published truth. Exact provenance remains bound to the content identity, locale, exact content version, block type/schema version and occurrence.
>
> Removing or replacing a block creates a changed successor composition/version; it does not destroy historical occurrences in immutable versions.
>
> A block occurrence has no independent publication state, approval state, ownership, entitlement or cross-content authority.
>
> If future requirements reveal independently reusable/versioned/approved content fragments, those must be modelled as a separate governed concept rather than turning ordinary block occurrences into shared mutable entities.
>
> This decision **does not decide** whether block occurrences are ultimately represented by embedded Ash Resources, child persisted Resources, typed values, JSON structures or another mechanism.

### 6.11 Consequences fixed for later grills

1. Block occurrence addressability must remain stable across reorder operations.
2. Historical identity is composite/version-bound; an occurrence key must never be treated as sufficient publication provenance.
3. Removal from a successor version must not erase historical occurrence evidence.
4. Review/comments may target an occurrence without promoting it to independent business authority.
5. Translation correspondence must be possible but is not yet specified.
6. Reusable independently governed content, if later required, must be a distinct governed concept.
7. A future persisted child Resource, if selected, would be an implementation shape rather than automatic proof of independent domain authority.

### 6.12 Block 1B.2 — Ash persistence/value shape

This revision resolves one additional question only:

> What persistence/value shape best implements GRILL-01 and GRILL-02 for ordinary block occurrences?

It does **not** settle the exact block envelope, draft concurrency strategy, translation correspondence, media-reference indexing, publication action, or renderer migration contract.

#### 6.12.1 Candidate A — separately persisted child Ash Resource

A relational child shape can provide granular row updates, joins, indexes and foreign-key enforcement. Those capabilities are real, but they are not currently required strongly enough to justify promoting every ordinary block occurrence into a separately persisted row.

The main cost is architectural, not merely storage overhead: the design must then prove which ordered set of independently mutable child rows constitutes the exact version being reviewed or published. It also introduces ordering/update mechanics and more relational lifecycle surface for a concept already accepted as subordinate.

**Working conclusion:** do not introduce persisted child block Resources by default. Reopen only if a demonstrated relational requirement cannot be met cleanly otherwise.

#### 6.12.2 Candidate B — raw JSON / untyped map

A generic `map`/JSON representation is easy to persist but weakens the reason NewYou is using Ash for governed structured content. It would push type discrimination, casting, validation and compatibility rules into a parallel interpreter layer.

**Working conclusion:** reject arbitrary untyped maps as the normal block representation.

#### 6.12.3 Candidate C — typed/embedded value owned by Content Version

The strongest semantic fit is an ordered structured value owned by the exact Content Version:

```text
ContentVersion
└── ordered block occurrences
    ├── stable local occurrence key
    ├── explicit block representation/type
    ├── explicit schema/representation version
    └── validated typed payload
```

This preserves the Content Version as the authoritative snapshot, avoids a second ordering authority, and keeps historical published meaning self-contained rather than reconstructing it from mutable shared block rows.

Ash can support this family of implementation using typed structures, union/discriminator types, new types and/or embedded Resources. The exact member mechanism should be chosen according to demonstrated validation complexity rather than assuming every block type must be a full Resource.

#### 6.12.4 Ordering pressure test

With separately persisted rows, order requires an additional field/index/ordering contract and concurrent reorder semantics. With one ordered structured composition, list order itself is authoritative for the version snapshot.

This does not solve collaborative draft editing; it merely prevents published composition from acquiring a second independent ordering authority.

#### 6.12.5 Immutable-version pressure test

A published Content Version should contain the exact block composition that was approved/published. It must not depend on mutable block rows whose later updates could reinterpret historical publication.

The accepted baseline therefore favours self-contained version-owned structured values.

#### 6.12.6 Ash atomicity pressure test

Ash union and some embedded-resource shapes have limitations around fully atomic casting/update paths. That is material for highly contested mutable state, but less decisive for the intended publication boundary where a validated draft composition is captured into a new immutable Content Version rather than patched inside an already-published version.

Draft concurrency remains deliberately deferred; GRILL-03 must not be misread as permission to overwrite concurrent draft edits blindly.

#### 6.12.7 Queryability pressure test

Persisted child rows are superior when the product genuinely requires frequent independent block-level relational queries, indexes or database-enforced relationships. Current authority does not establish that requirement for ordinary blocks.

Where dependency discovery or projection is needed later, that requirement should be pressure-tested directly rather than pre-emptively relationalising every paragraph, heading and callout.

#### 6.12.8 Schema-evolution pressure test

Version-owned values must carry sufficient explicit representation/version information so that historical values remain interpretable after later code releases. A later block representation may coexist with older representations; old published values are not silently rewritten merely because application code changes.

The exact persisted envelope and compatibility policy remain Block 1B.3 and later work.

#### 6.12.9 Large-document pressure test

Version-owned structured composition may rewrite more data per draft save than row-granular mutation. That is an acknowledged trade-off. There is currently no evidence that ordinary NewYou article/lesson/recipe compositions require pre-emptive row-per-block optimisation.

If measured draft/editor behaviour later proves otherwise, the mutable draft representation may be reconsidered without weakening the rule that the immutable governed Content Version owns the exact published composition.

### 6.13 ACCEPTED GRILL DECISION

#### `GRILL-03 — Content-Version-Owned Structured Block Storage`

**Status:** ACCEPTED / WORKING DOSSIER DECISION / NON-AUTHORITATIVE

> Ordinary block occurrences are persisted as an ordered, structured part of the owning Content Version rather than as independently PostgreSQL-backed block Resources by default.
>
> The Ash baseline is a code-defined structured/embedded value model. A block occurrence carries its stable local occurrence key and sufficient explicit representation/version information to identify the block contract used to interpret it.
>
> The occurrence key is an ordinary value, not an Ash primary key, Ash identity or independent business identifier.
>
> Heterogeneous block payloads must remain explicitly typed/discriminated and validated; arbitrary untyped maps are not the normal representation.
>
> `Ash.Type.Union`, `Ash.TypedStruct`, `Ash.Type.NewType` and/or embedded Ash Resources may implement that structured contract according to demonstrated validation needs. Full embedded Resources are not required merely because Ash provides them.
>
> Published Content Versions capture the exact ordered block composition and are not later reconstructed from mutable shared block rows.
>
> Separate persisted child block Resources are **not introduced initially**. They require evidence of a relational requirement such as necessary independent querying, relational integrity or granular mutation that cannot be satisfied cleanly while preserving the Content Version as authority.
>
> This decision does not yet settle the exact union/tag/wrapper representation, draft concurrency strategy, media-reference indexing, translation correspondence or publication action.

### 6.14 Consequences fixed for later grills

1. The owning Content Version remains the authoritative container for the exact ordered block composition.
2. The ordinary block occurrence is a structured subordinate value, not a separate PostgreSQL business authority by default.
3. Raw arbitrary JSON/map storage is not the normal contract; block representations must be explicitly typed/discriminated and validated.
4. The stable occurrence key remains data, not an Ash primary key or Ash identity.
5. Historical block representations require explicit schema/representation versioning and continued interpretation support.
6. Separate relational block rows may be reconsidered only against a concrete requirement and evidence, not convenience.
7. **Historical at GRILL-03 acceptance:** draft concurrency, translation correspondence, media-reference indexing and publication actions were unresolved. `GRILL-22`/`GRILL-23` subsequently resolve the shared/locale translation ownership and lineage/staleness semantics; `GRILL-35`/`GRILL-36` subsequently resolve authoritative forward media references, version-exact references and derived/rebuildable reverse usage semantics; exact translation persistence, draft concurrency, reverse-usage projection/reconciliation mechanics and publication action implementation remain JIT/deferred.

### 6.15 Block 1B.3 — minimal persisted block envelope

This revision resolves one additional question only:

> What exact common persisted envelope must every ordinary block occurrence carry, and what must deliberately not be stored there?

The accepted baseline is intentionally small:

```text
BlockOccurrence
├── occurrence_key
├── block_type
├── schema_version
└── payload
```

The four fields have distinct responsibilities.

#### 6.15.1 `occurrence_key`

`occurrence_key` is an opaque, system-managed local continuity/addressability value. It supports editor targeting, reorder continuity, diffs, review references and future translation correspondence. It is not independently sufficient historical provenance and must not become an Ash primary key, Ash identity, public semantic identifier or independent business identifier merely for framework convenience.

The exact encoding remains an implementation/JIT detail unless a later requirement makes it architectural.

#### 6.15.2 `block_type`

`block_type` is the stable code-catalogue capability identifier such as `paragraph`, `image`, `callout` or another approved internal key. It must remain independent of Elixir module names, renderer-module names and editor-facing labels so implementation refactors do not require rewriting historical content.

The mapping is conceptually:

```text
persisted block_type
        ↓
code-authoritative catalogue
        ↓
known validator / decoder / renderer
```

#### 6.15.3 `schema_version`

`schema_version` identifies the exact persisted representation contract for that `block_type`. It is distinct from Content Version numbering and from the block capability identity itself.

A later code release may support `callout` representation versions 1 and 2 concurrently. Historical content carrying version 1 must remain interpretable as version 1; application changes must not silently reinterpret it as version 2.

The working baseline favours a simple positive discrete version rather than SemVer for the persisted representation. Exact encoding remains implementation detail.

#### 6.15.4 `payload`

`payload` contains the exact occurrence-specific values permitted by `block_type + schema_version`. It is not an arbitrary JSON escape hatch. Casting, constraints and validation are defined by the code-authoritative block contract. Approved bounded presentation choices may be payload values where they are part of that contract.

### 6.16 Envelope pressure-test conclusions

1. **Ordering:** list/composition order is authoritative; do not duplicate it through a canonical per-block `position` field.
2. **Parent provenance:** content identity, locale, Content Version, risk, approval and publication state belong to the owning governed Content Version and are not repeated in every block.
3. **Generic extension bags:** no common canonical `metadata`, `extra`, `options` or equivalent open-ended map is introduced initially. New durable meaning must enter through an explicit typed contract.
4. **References:** no canonical generic `refs` array duplicates references already carried by a typed payload. Dependency/search projections may be derived separately if later justified.
5. **Media:** block payloads may carry an explicit typed Media reference where required, but Media-owned rights, versions, checksums, publication state and other authority are not copied into the block envelope.
6. **Executable/runtime definition:** renderer modules, HEEx/templates, arbitrary HTML, JavaScript, CSS, function names or equivalent executable/editor-controlled definitions are not persisted as block-envelope content.
7. **Editor metadata:** current labels, icons, help text and editor-component choices belong to the code catalogue, not historical Content Versions.
8. **Timestamps:** no generic block-level `created_at` / `updated_at` is required by the common envelope; audit/editor activity is a separate concern.
9. **Lifecycle:** ordinary blocks do not receive independent draft/approved/published state.
10. **Template provenance:** template origin/slot lineage is not added to every block by default; template provenance will be pressure-tested at the appropriate composition/template seam.
11. **Unknown representation:** unsupported `(block_type, schema_version)` pairs must fail closed rather than being silently coerced to a newer/other representation.

### 6.17 ACCEPTED GRILL DECISION

#### `GRILL-04 — Minimal Versioned Block Envelope`

**Status:** ACCEPTED / WORKING DOSSIER DECISION / NON-AUTHORITATIVE

> Every ordinary block occurrence is persisted under a minimal common semantic envelope containing:
>
> `occurrence_key` — opaque, system-managed local continuity/addressability;
>
> `block_type` — stable code-catalogue capability identifier independent of implementation module names and editor-facing labels;
>
> `schema_version` — explicit positive representation version identifying the persisted block contract;
>
> `payload` — the exact typed and validated occurrence-specific values defined by that `block_type + schema_version`.
>
> Block ordering is owned by the containing composition and is not duplicated through a canonical `position` field.
>
> Parent content identity, locale, version, risk, approval and publication truth are inherited from the owning governed Content Version and are not duplicated into every block occurrence.
>
> The common block envelope has no generic `metadata`, `extra`, `options` or canonical generic `refs` escape hatch.
>
> Executable/rendering implementation—Elixir modules, HEEx/templates, arbitrary HTML, JavaScript and CSS—is never content-owned envelope data.
>
> Approved bounded presentation choices may be persisted inside a block's typed payload where they are part of that block's code-defined contract.
>
> Domain references such as Media references occur explicitly in the relevant typed payload; their authoritative external metadata is not copied into the block.
>
> Unknown or unsupported `(block_type, schema_version)` representations must not be silently reinterpreted as another version.
>
> Exact `occurrence_key` encoding and exact Ash DSL/storage mechanics remain implementation/JIT details unless a later requirement makes them architectural.

### 6.18 Consequences fixed for later grills

1. The common persisted envelope is exactly four semantic concerns: local occurrence address, block capability identity, representation version and typed occurrence payload.
2. Block order belongs to the containing composition.
3. Content/locale/publication provenance is not duplicated per block.
4. The code catalogue remains renderer/editor-definition authority; historical content stores bounded data, not executable implementation.
5. Open-ended extension bags are rejected initially; new durable semantics require an explicit contract.
6. Domain-owned referenced entities keep their own authority; block payloads hold references, not copied authority.
7. Unsupported historical representation versions fail closed.
8. **Historical at GRILL-04 acceptance:** schema evolution/version-bump rules were unresolved; `GRILL-05` subsequently resolves the compatible block-schema evolution contract.

### 6.19 Block 1B.4 pressure test — schema evolution

`schema_version` identifies the persisted interpretation contract for one `block_type`. It is not an application release, Ash version, editor version, Content Version number, or presentation release.

The version-bump test is:

> If newly persisted data cannot be safely and equivalently interpreted under the previous contract, or if an existing persisted value/default would otherwise acquire a different meaning, the block requires a new `schema_version`.

Pressure-test conclusions:

1. **Newly persisted fields/options unknown to old readers:** new schema version before those values may be written.
2. **Field rename or incompatible type change:** new schema version. Historical payloads remain in their original representation.
3. **Changed persisted defaults:** new schema version where omission would otherwise acquire a new meaning. Old missing-field semantics remain fixed forever for that old version.
4. **Authoring-policy change only:** not automatically a schema bump where historical payload meaning and renderability remain unchanged. A value may become non-authorable while remaining readable.
5. **Pure code/refactor change:** no schema bump where persisted meaning remains equivalent.
6. **Security/accessibility repair:** no schema bump merely because implementation changes, provided the intended persisted meaning is preserved. Historical fidelity does not require retaining vulnerable behaviour.
7. **Material semantic reinterpretation:** new schema version even when the stored shape looks superficially similar.
8. **Historical published values:** are not destructively rewritten merely to conform to the latest schema.
9. **Read adaptation:** deterministic old-version decoders/adapters may map historical payloads into a safe current internal rendering model without altering the persisted source or meaning.
10. **Mixed representation versions:** are valid. `latest` is not synonymous with `valid`.
11. **Reader-before-writer:** read support for a new version must be deployed before that version becomes authorable/persistable.
12. **Rollback:** once new-version payloads exist, rollback must not cross to application code that cannot read them.
13. **Writer retirement and reader retirement are distinct:** an old version may stop being authorable long before its reader can safely be removed.
14. **Reader retirement:** requires proof that no retained authoritative content still needs that version, or a separately approved preservation/migration strategy that preserves equivalent historical interpretation.
15. **Unsupported versions:** fail closed; do not guess, coerce to latest, strip unknown semantics, or render generically.
16. **Unexpected canonical payload fields:** should be rejected by the persisted contract rather than silently becoming extension metadata.

This model deliberately prefers retaining cheap historical decoders over rewriting immutable governed history.

### 6.20 ACCEPTED GRILL DECISION

#### `GRILL-05 — Explicit Compatible Block-Schema Evolution`

**Status:** ACCEPTED / WORKING DOSSIER DECISION / NON-AUTHORITATIVE

> `schema_version` identifies the persisted interpretation contract for one `block_type`; it is not a software, editor, Content Version or presentation release number.
>
> A new schema version is required whenever newly persisted payloads cannot be safely and equivalently interpreted under the previous contract, or when the meaning of existing persisted values/defaults would otherwise change.
>
> Structural changes such as field renames, incompatible type changes, newly persisted fields/options unknown to old readers, changed persisted defaults, or materially changed representation semantics require a new schema version.
>
> Pure implementation refactors, security/accessibility fixes that preserve persisted meaning, and authoring-policy changes that do not change historical interpretation do not automatically require a schema bump.
>
> Existing published Content Versions are not automatically or destructively rewritten to newer block schemas. Historical representations remain authoritative as originally persisted.
>
> Older representations may be deterministically adapted on read into safe internal rendering models, provided their persisted source and semantics remain preserved.
>
> New schema versions follow a **reader-before-writer** deployment rule: compatible read support must exist before new-version payloads may be authored/persisted. Once newer payloads exist, rollback must not cross to application code that cannot read them.
>
> Old schema versions may become non-authorable while remaining readable. Read support is retained while authoritative retained content still requires it, unless a separately approved preservation/migration strategy proves equivalent historical interpretation.
>
> Unknown `(block_type, schema_version)` combinations must fail closed rather than silently falling back to another version. Canonical persisted payload validation should likewise reject unexplained fields rather than treating unknown data as harmless extension metadata.
>
> Schema-version evolution is a NewYou content contract independent of Ash package versions and independent of Beacon's internal component evolution.

### 6.21 Consequences fixed for later grills

1. `schema_version` is a durable interpretation-contract marker, not a generic software version.
2. Version changes are driven by persisted compatibility/meaning, not every implementation change.
3. Historical published block payloads are preserved in the representation actually persisted.
4. New code carries the burden of understanding supported old representations; old content does not chase new code.
5. Reader-before-writer compatibility is a release requirement for introducing a new block representation.
6. Old versions may become read-only/non-authorable without forcing data migration.
7. Reader retirement needs explicit proof; writer retirement alone is insufficient.
8. Unsupported or unexplained persisted representations fail closed.
9. This decision does not yet define exact Ash decoder modules, migrations, release automation, draft concurrency, translation correspondence or template semantics.

### 6.22 Block 1C.1 pressure test — slot semantics

Three different concepts can be called a `slot` and must not be conflated:

1. a Phoenix function-component rendering slot;
2. Beacon's persisted CMS representation of Phoenix slots;
3. a NewYou content-composition region.

Beacon stable `v0.5.1` explicitly models `ComponentSlot` as a persisted representation of Phoenix slots, including a name, serialised options and persisted slot attributes. That is useful evidence for requiredness, known-slot validation, documentation and bounded child contracts, but NewYou's accepted `GRILL-01` prevents the database from becoming a second mutable authority for block/slot definitions.

Pressure-test conclusions:

1. **Leaf blocks remain simple.** Paragraph, image, heading and similar leaf blocks do not gain slot machinery merely for uniformity.
2. **Composition slots exist only where child composition is real.** Examples may include bounded regions such as a two-column left/right composition or a hero content/actions region.
3. **Slot definitions are code-authoritative.** Stable slot keys, requiredness, cardinality, permitted child block/content types and editor help belong to the versioned parent block contract, not mutable CMS rows.
4. **Slot content is governed data.** The exact child composition assigned to an approved slot is persisted as part of the parent block/content-version representation.
5. **Slots are not independent entities.** A slot has no independent identity, approval, publication, risk, ownership or lifecycle state.
6. **Stable keys are contract identifiers.** Slot keys are not locale labels, database IDs or Phoenix module/function names. A persisted key rename is a representation-schema concern under `GRILL-05`.
7. **Ordering has one authority.** Ordered multi-child slots derive order from their child sequence rather than an additional canonical `position` field.
8. **Strict validation applies.** Unknown slots, missing required slots, invalid cardinality and disallowed child types fail validation instead of being silently ignored.
9. **No generic slot-attribute bag initially.** Semantically meaningful configuration belongs in explicit typed fields/contracts rather than a Beacon-style open-ended slot-attribute mechanism.
10. **No unrestricted recursion.** Allowed child types are explicit. Self-recursive or indirectly recursive composition requires demonstrated need and a separate pressure test.
11. **Implementation sharing is not assumed.** Block slots and future template slots may share a concept without being forced into the same Ash implementation type.

Beacon reuse for this seam is therefore conceptual:

- **ADAPT:** named-slot concept, requiredness, known-slot validation, documentation/help, bounded typed constraints;
- **REINTERPRET:** Phoenix/Beacon rendering slots into NewYou bounded composition slots;
- **REJECT initially:** database-authoritative `ComponentSlot`/`ComponentSlotAttr` rows, serialised slot `opts`, runtime editor-created slots, generic slot-attribute bags and 1:1 coupling between persisted NewYou composition and `Phoenix.Component.slot/3`.

### 6.23 ACCEPTED GRILL DECISION

#### `GRILL-06 — Code-Defined Bounded Composition Slots`

**Status:** ACCEPTED / WORKING DOSSIER DECISION / NON-AUTHORITATIVE

> NewYou supports a slot concept only where an approved block or template genuinely requires child composition.
>
> A NewYou composition slot is a stable, named, code-defined and bounded content region; it is not itself a business entity, independently persisted lifecycle, or direct runtime copy of `Phoenix.Component.slot/3`.
>
> Leaf blocks remain simple typed blocks and do not acquire slot machinery merely for consistency.
>
> Slot definitions belong to the same code-authoritative versioned contract as their parent block. They may declare requiredness, cardinality, permitted child content/block types and editor-facing documentation or equivalent constraints where justified.
>
> Persisted content stores the exact child composition assigned to approved slots as part of the owning parent block/content-version representation; slot definitions themselves are not mutable CMS data.
>
> Slot names/keys are stable internal contract identifiers and are not locale labels or implementation-module names.
>
> A slot has no separate publication, approval, risk, ownership or lifecycle state.
>
> Ordered multi-child slots derive order from their canonical child sequence rather than duplicating order through an independent position authority.
>
> Unknown slots, missing required slots, invalid cardinality and disallowed child types fail validation rather than being silently ignored.
>
> Generic Beacon-style slot attribute bags are not introduced initially. Any necessary semantic configuration is represented through explicit typed fields/contracts.
>
> Unrestricted recursive composition is not the default. Permitted child types are explicitly bounded by code; self-recursive or indirectly recursive composition requires demonstrated need and separate pressure testing.
>
> The shared conceptual slot model does not yet require block slots and future template slots to use the same Ash implementation.
>
> Beacon's slot semantics are therefore **ADAPTED conceptually**, while Beacon's persisted `ComponentSlot` / `ComponentSlotAttr` authority model is **REJECTED** for NewYou.

### 6.24 Consequences fixed for later grills

1. A slot is a bounded composition contract, not a persisted business entity.
2. Slot definitions are versioned code contract; slot contents are governed content data.
3. Leaf blocks remain slot-free unless actual child composition is required.
4. Slot structure participates in the parent block's `schema_version` contract.
5. Generic slot attributes and unrestricted recursion are rejected initially.
6. Child occurrences inside slots remain governed by `GRILL-02` through `GRILL-05`.
7. Phoenix slots may implement rendering later, but NewYou persisted semantics do not depend on a 1:1 Phoenix-slot mapping.

### 6.25 Block 1C.2 pressure test — section semantics

Current NewYou operating/frontend authority uses the vocabulary `blocks`, `sections`, `content components` and `composed patterns`, but does not establish four separate durable entity types.

The pressure test therefore distinguished editor/catalogue vocabulary from durable business/content identity.

#### Separate persisted `Section` Resource

Rejected initially.

A separate `Section`, `SectionDefinition` or `SectionVersion` Resource would immediately create lifecycle and ownership questions with no demonstrated requirement: independent identity, approval, publication, translation, correction, removal and successor-version semantics.

Visual size or editor grouping is not evidence of independent durable authority.

#### Separate section envelope

Rejected initially.

Creating a parallel persisted envelope for sections alongside the already accepted block envelope would duplicate identity, versioning, ordering, validation, diffing and schema-evolution mechanics without evidence that those semantics differ.

#### Section as a code-defined catalogue/composition role

Accepted.

A substantial composed or visually bounded region may be represented by an ordinary approved block contract whose code-authoritative catalogue metadata classifies it as a section for editor discovery, organisation, documentation and tooling.

A section-classified block may use bounded composition slots under `GRILL-06` when its actual structure requires them, but `section` does not automatically imply containment, slots, recursion, shared identity or independent lifecycle.

Examples may eventually include Hero, Feature Grid, Two Column, FAQ Section or CTA Section, but each remains governed by its own explicit `block_type + schema_version` contract.

#### Classification is not structural authorisation

A catalogue category such as `section` must not silently grant every current or future member of that category access to every composition position.

Composition contracts remain explicitly bounded.

Adding a new section-classified block to the code catalogue must not automatically make it legal inside every template/content type that currently permits some sections.

#### Reuse does not come from the word `section`

If a future requirement needs independently reusable/versioned/approved content across many Content Versions, that is evidence for a separately justified governed reusable-content concept, not evidence that every section should become a shared mutable entity.

#### Beacon and LiveFrames comparison

Beacon stable `v0.5.1` classifies Components with an Ecto enum including `:section`; the useful idea is the category itself, not database-authoritative component/category definitions.

LiveFrames likewise uses `Section` as UI-library taxonomy for larger styled compositions. Under accepted `LF-01`, that presentation taxonomy may supply rendering implementations but does not define NewYou's persisted content hierarchy.

### 6.26 ACCEPTED GRILL DECISION

#### `GRILL-07 — Sections Are Catalogue/Composition Roles, Not Separate Content Entities`

**Status:** ACCEPTED by the human project owner on 2026-09-19.

> NewYou does not initially introduce a separate persisted `Section`, `SectionDefinition`, `SectionVersion` or Section Ash Resource merely because current experience language distinguishes blocks, sections, components and patterns.
>
> An ordinary NewYou section is an approved code-defined block contract classified for editorial/catalogue purposes as a substantial composed or visually bounded region.
>
> Section-classified occurrences use the same `BlockOccurrence` semantics and minimal versioned envelope established by `GRILL-02` through `GRILL-05`.
>
> A section may use bounded composition slots under `GRILL-06` where its actual structure requires them, but being a section does not automatically imply containment, slots, recursion or independent lifecycle.
>
> Section classification is code-authoritative catalogue metadata and is not redundantly persisted into every block occurrence.
>
> Catalogue classifications primarily support editor discovery, organisation, documentation and tooling. They do not automatically grant structural authorisation to every current or future member of a category; composition contracts remain explicitly bounded.
>
> Sections have no independent approval, publication, risk, ownership, translation or withdrawal lifecycle merely because they are sections.
>
> Independently reusable/versioned governed content must justify its own explicit concept from its reuse/governance requirements rather than being modelled as a shared mutable Section.
>
> Beacon's `:section` component-category idea is **ADAPTED** as catalogue vocabulary, while a database-authoritative category is not adopted.
>
> LiveFrames' `Section` taxonomy may provide presentation implementations, but it does not define NewYou persisted content hierarchy.

### 6.27 Consequences fixed for later grills

1. `section` is not a new Ash Resource or persistence envelope.
2. Section-classified occurrences remain ordinary subordinate block occurrences.
3. Section classification belongs to the code-authoritative catalogue.
4. Classification is primarily editorial/tooling metadata, not blanket composition permission.
5. Slot support remains an independent characteristic of a block contract.
6. Independent reusable governed content must be justified from actual reuse/lifecycle semantics rather than visual category.
7. LiveFrames UI taxonomy remains presentation-side and cannot redefine NewYou content persistence.

### 6.28 Block 1C.3 pressure test — content-component semantics

Current NewYou authority names `content components` in the approved composition catalogue, but does not assign them separate durable identity, lifecycle, persistence, ownership or publication authority.

The pressure test therefore distinguished content/editorial catalogue vocabulary from UI/framework component terminology and from durable content entities.

#### Separate persisted `ContentComponent` Resource

Rejected initially.

Creating `ContentComponent`, `ContentComponentDefinition` or `ContentComponentVersion` Resources would introduce identity, lifecycle, translation, publication, reuse and relationship semantics not required by current authority.

A named reusable editor concept is not sufficient evidence for a new Ash Resource.

#### Separate component occurrence envelope

Rejected initially.

An ordinary structured content component needs the same persisted facts already established for an ordinary block occurrence:

```text
occurrence_key
block_type
schema_version
payload
```

A second `ComponentOccurrence` envelope would duplicate identity, schema evolution, ordering, validation and historical interpretation mechanics without a demonstrated semantic distinction.

#### Content component as a code-defined catalogue/editorial role

Accepted.

The canonical persisted composition unit remains `BlockOccurrence`.

A `content component` is a code-authoritative catalogue/editorial classification for an approved block contract that is typically more structured and semantically cohesive than a low-level basic content block.

Possible future examples include `key_takeaways`, `author_bio`, `nutrition_summary`, `testimonial`, `product_card` or `download_card`, but each persists through the ordinary block contract/envelope.

The classification supports authoring-palette organisation, documentation, preview tooling, template guidance and other editorial ergonomics without creating a second persistence hierarchy.

#### Contract reuse is not shared occurrence reuse

A content-component contract may be reused across many Content Versions while each inserted occurrence remains independently owned by its containing Content Version.

For example, two articles may both use the `key_takeaways` contract while retaining independent occurrence keys and independent payload values.

Classification as a content component does not mean that two Content Versions point to one mutable shared content object.

If future requirements establish genuinely shared governed content with independent identity, versioning, approval, dependency and withdrawal semantics, that requirement must justify a separately named governed reusable-content concept.

#### Slots and category are independent

A content-component-classified block does not automatically own composition slots.

Some components may be structured leaf blocks; others may use bounded slots under `GRILL-06`.

Likewise a section-classified block and a content-component-classified block may overlap in editor vocabulary without requiring an inheritance hierarchy.

Exact catalogue taxonomy/tagging remains downstream.

#### Catalogue role does not grant placement authority

A content type or slot must not implicitly allow every current and future block merely because each is classified as `content component`.

Actual placement/composition permission remains explicitly bounded by the owning content-type or slot contract.

This prevents future catalogue growth from silently expanding existing authoring capabilities.

#### Beacon comparison

Beacon stable `v0.5.1` uses persisted `Beacon.Content.Component` records that own runtime component definition data such as name, body, template, attrs, slots and category.

The useful ideas are the reusable named contract, typed inputs, bounded options and editor-facing documentation.

The database-authoritative runtime component-definition model remains rejected under `GRILL-01`.

#### LiveFrames/Phoenix terminology boundary

Under accepted `LF-01`, three meanings remain distinct:

```text
NewYou content component
    = editorial/catalogue role over a NewYou content block contract

LiveFrames UI component
    = reusable presentation implementation

Phoenix component
    = framework rendering construct
```

A NewYou content-component-classified block may render through one LiveFrames component, several LiveFrames primitives/components, or NewYou-specific presentation code. That mapping is not persisted content identity.

### 6.29 ACCEPTED GRILL DECISION

#### `GRILL-08 — Content Components Are Catalogue Roles Over Block Contracts, Not Separate Durable Entities`

**Status:** ACCEPTED by the human project owner on 2026-09-19.

> NewYou does not initially introduce a separate persisted `ContentComponent`, `ContentComponentDefinition`, `ContentComponentVersion` or ContentComponent Ash Resource merely because current experience authority distinguishes content components in the approved composition catalogue.
>
> The canonical persisted composition unit remains the ordinary versioned `BlockOccurrence`.
>
> A NewYou `content component` is a code-authoritative catalogue/editorial classification for an approved, typically more structured and semantically coherent content block contract.
>
> Content-component-classified occurrences use the same identity, storage, versioning and historical semantics already accepted for ordinary block occurrences.
>
> Classification as a content component does not automatically imply composition slots, independent identity, independent reuse-by-reference, approval/publication lifecycle, translation lifecycle, or shared mutable content.
>
> Reuse applies initially to the **code-defined contract**, not automatically to the occurrence's content values.
>
> Where genuinely shared governed content later requires independent identity, versioning, approval, dependency and withdrawal semantics, that requirement must justify a separately named governed reusable-content concept rather than promoting every content component into a shared entity.
>
> Content-component classification is code-authoritative catalogue metadata and is not redundantly persisted into every occurrence.
>
> Catalogue classification does not itself grant placement authority. Content-type and composition contracts remain explicitly bounded so future catalogue growth cannot silently expand existing authoring permissions.
>
> Beacon's reusable component-contract ideas are **ADAPTED**, while Beacon's database-authoritative `Component` definition model remains rejected.
>
> A NewYou content component is explicitly distinct from a LiveFrames UI component and a Phoenix framework component. Presentation implementations may map 1:1, many:1 or 1:many without changing NewYou persisted content semantics.
>
> Exact catalogue taxonomy/tagging mechanics remain downstream and must not become an unnecessary inheritance hierarchy.

### 6.30 Consequences fixed for later grills

1. `ContentComponent` is not a new Ash Resource or persistence envelope by default.
2. The persisted composition unit remains `BlockOccurrence`.
3. `content component` is code-authoritative catalogue/editorial metadata over a block contract.
4. Component classification does not imply slots, lifecycle or shared mutable occurrence content.
5. Reuse initially means reuse of the code-defined contract, not shared content-instance identity.
6. Placement authority remains explicit and does not derive automatically from catalogue role.
7. Beacon's database-defined runtime component authority remains rejected.
8. LiveFrames/Phoenix UI components remain presentation-side concepts distinct from NewYou content semantics.
9. Exact catalogue taxonomy mechanics remain downstream.

### 6.31 Block 1C.4 pressure test — composed-pattern semantics

Unlike `section` and `content component`, a composed pattern may carry genuine authoring behaviour because it can describe a reusable multi-block composition.

The pressure test therefore distinguished a reusable **authoring recipe** from a live runtime content dependency.

#### Runtime `PatternOccurrence`

Rejected initially.

Persisting a live pattern reference whose definition expands at render time would make mutable shared authoring definitions capable of changing already-authored content.

That conflicts with NewYou's immutable-version and historical-provenance requirements.

Published content must not depend on a mutable pattern lookup to determine its exact block composition.

#### Copy-on-instantiation composition recipe

Accepted.

A composed pattern is an approved, initially code-authoritative recipe that materialises a finite composition of approved NewYou block contracts into the target draft.

Conceptually:

```text
Pattern definition
        ↓ apply
concrete BlockOccurrences
        ↓
owning draft / Content Version
```

Each application creates fresh subordinate occurrence keys and concrete payload values.

The resulting occurrences are ordinary content owned by the target draft/Content Version; they do not remain live-linked to the pattern.

#### Defaults become owned draft values

Pattern-provided defaults are copied into the instantiated draft values.

They are not dynamically inherited.

Changing a pattern default later does not rewrite prior instantiations.

#### Editors edit the instantiated content, not the pattern

After expansion, editors may modify the resulting block values or composition subject to the target content type, block schemas, slot constraints and governed workflow.

Editing one instantiation does not mutate the reusable pattern.

#### Pattern changes/deprecation do not rewrite existing content

A later recipe change affects new instantiations only unless an editor explicitly creates an updated successor Content Version.

Pattern deprecation/removal therefore does not make historical published content unreadable, because published truth contains the concrete block composition.

#### Placement and validation remain explicit

Pattern catalogue approval is not placement authority.

The fully expanded result must satisfy the target content-type and slot contracts.

Pattern application is semantically one coherent draft mutation: an invalid expansion must not leave a partially inserted composition. Exact transaction/concurrency mechanics remain deferred.

#### Authoring provenance is not content authority

Where useful, an authoring/audit record may later capture which pattern definition/revision was applied.

Such provenance does not belong in the common `BlockOccurrence` envelope and rendering/publication must not depend on it.

#### No arbitrary-runtime escape hatch

Patterns compose only approved NewYou block contracts.

They do not introduce arbitrary HTML, HEEx, scripts, styling, unknown block types or arbitrary LiveFrames/Phoenix implementation references.

Runtime recursive pattern expansion and shared mutable PatternOccurrence references are not introduced initially.

#### Pattern versus template

A composed pattern is narrower than a content template.

Working distinction:

```text
pattern
= reusable partial composition recipe

template
= broader content-authoring scaffold
```

Current NewYou authority permits templates to predefine expected sections, ordering, default blocks/components, required structural slots, recommended metadata, CTA placements and presentation defaults.

This grill does not decide exact template storage, instantiation, versioning or dynamic-link semantics.

#### Ash

No Pattern Ash Resource is justified initially.

A Pattern Resource would require future evidence that pattern definitions themselves need independently mutable/versioned/approved/permissioned governed lifecycle beyond code-authoritative catalogue governance.

#### Beacon

Stable Beacon `v0.5.1` has no first-class persisted Pattern entity to import.

Adjacent Page/Layout/Component/template/snapshot mechanisms are reference material only for this seam.

#### LiveFrames

A NewYou composed pattern is an authoring composition recipe.

A LiveFrames `Pattern` is presentation/UI-library taxonomy.

Under accepted `LF-01`, they remain separate concepts even where a LiveFrames pattern later implements the UI for an instantiated NewYou composition.

### 6.32 ACCEPTED GRILL DECISION

#### `GRILL-09 — Composed Patterns Are Copy-on-Instantiation Authoring Recipes, Not Runtime Content Entities`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> A NewYou composed pattern is an approved, initially code-authoritative reusable recipe for producing a bounded composition of approved content block contracts.
>
> Applying a pattern materialises concrete ordinary `BlockOccurrence` values into the owning draft/content composition. Each instantiation receives its own occurrence keys and content values.
>
> Once instantiated, the resulting content is owned by the containing draft/Content Version and does not retain a live semantic dependency on the pattern definition.
>
> Pattern changes, deprecation or removal do not silently alter previously instantiated drafts or immutable published Content Versions.
>
> Published content renders from its exact materialised block composition and must not require runtime pattern expansion or lookup.
>
> Pattern defaults become ordinary draft values at instantiation rather than dynamically inherited values.
>
> Editors may modify instantiated content subject to the owning content-type, block-schema, slot, review and publication constraints; this does not modify the reusable pattern definition.
>
> Pattern catalogue approval does not grant placement authority. The fully expanded composition must satisfy the target content-type and slot contracts.
>
> Pattern application is one coherent draft mutation: an invalid expansion must not leave a partially inserted composition. Exact Ash/PostgreSQL concurrency/transaction mechanics remain deferred.
>
> Pattern provenance, where useful, belongs to authoring/audit evidence rather than the common persisted block envelope, and publication/rendering must not depend on it.
>
> Patterns do not introduce arbitrary HTML, HEEx, scripts, styling, unknown blocks or ungoverned UI implementations; they compose only approved NewYou content contracts.
>
> Runtime pattern recursion and shared mutable PatternOccurrence references are not introduced initially. Pattern expansion resolves to finite concrete content composition.
>
> A pattern is narrower than a content template: patterns provide reusable partial composition recipes, while templates may govern broader authoring scaffolds such as expected structure, required slots, metadata guidance and CTA placement under existing NewYou authority.
>
> Pattern application never overrides content type, translation, risk, review, accessibility, approval or publication rules.
>
> No Pattern Ash Resource is introduced initially. Independently editable/versioned/governed pattern definitions would require separate future evidence and pressure testing.
>
> Beacon stable `v0.5.1` provides no first-class Pattern entity to import and is **REFERENCE ONLY** for this seam.
>
> NewYou composed patterns remain distinct from LiveFrames UI patterns under `LF-01`.

### 6.33 Consequences fixed for later grills

1. Composed patterns are authoring recipes, not persisted runtime content entities.
2. Pattern application materialises ordinary `BlockOccurrence` values.
3. Instantiated occurrences receive fresh local occurrence keys.
4. Pattern defaults become ordinary owned draft values rather than live inherited values.
5. Pattern changes/deprecation/removal cannot silently mutate prior instantiations.
6. Published rendering never depends on runtime pattern expansion or lookup.
7. Pattern provenance, if later retained, is authoring/audit evidence rather than canonical block-envelope authority.
8. Pattern application must validate atomically as one coherent draft mutation; implementation mechanics remain deferred.
9. Patterns compose only approved NewYou contracts and do not create arbitrary runtime UI/code extension.
10. Pattern and template semantics remain distinct; exact template semantics are still undecided.
11. No Pattern Ash Resource is introduced initially.
12. LiveFrames UI patterns remain presentation-side concepts distinct from NewYou composed patterns.

### 6.34 Block 2A.1 pressure test — pattern versus governed content template

Current NewYou authority already gives content templates stronger responsibilities than composed patterns.

Reusable templates may precompose approved structures, slots and defaults, while template changes must not silently rewrite immutable published versions. Working experience provenance further describes template concerns such as expected sections, ordering, default blocks/components, required structural slots, recommended metadata, CTA placements and presentation defaults.

The pressure test therefore distinguished a bounded local insertion recipe from a broader authoring scaffold.

#### Pattern

A composed pattern remains the `GRILL-09` concept:

```text
partial/local reusable authoring recipe
        ↓
insert
        ↓
concrete ordinary BlockOccurrences
        ↓
live pattern relationship ends
```

Patterns provide local composition convenience.

#### Template

A content template is a broader governed authoring scaffold for a substantial portion or whole governed content item.

Conceptually:

```text
content type authority
        ↓
selected template revision
        ↓
draft scaffold
        ↓
resolved concrete composition/content values
        ↓
immutable/versioned Content Version
```

A template may organise or narrow authoring choices within the upstream content-type/Domain contract, but may not create competing content authority.

#### Content type remains upstream

A template cannot:

- permit a block forbidden by the selected content type;
- remove required review or translation;
- weaken accessibility/publication requirements;
- alter Domain-owned workflow;
- create a separate publishability truth.

Universal business/publishability invariants belong to content-type/Domain authority rather than being duplicated only inside particular templates.

#### Hard constraints versus defaults/recommendations

Template declarations must preserve the semantic difference between:

- hard structural constraints;
- defaults;
- recommendations/guidance.

For example, a required body region is not equivalent to a suggested closing CTA.

Exact DSL/storage representation remains deferred.

#### Revision-addressable authoring semantics

Templates may evolve over time.

Because a template revision can affect required structure, ordering or defaults, an instantiated draft must be governed by an exact stable template identity/revision or equivalent immutable provenance.

A later template revision must not silently replace the scaffold of an existing draft.

Moving a draft/content lineage to a newer template revision must be an explicit governed operation. Exact migration UX, merge semantics and concurrency handling remain deferred.

#### Materialisation into draft/content truth

Like patterns, templates do not remain hidden runtime body authority.

Applying a template materialises or resolves ordinary NewYou content composition into the target draft.

Resulting block occurrences:

- receive ordinary local occurrence keys;
- are owned by the draft/content lineage;
- follow normal block schema/version semantics;
- ultimately become exact Content Version truth.

Anything materially affecting the published representation must resolve to stable Content Version data rather than remain dependent on the current template definition at render time.

#### Template provenance is stronger than pattern provenance

Pattern provenance is optional authoring evidence.

Template provenance is materially useful because an exact revision may have governed required structure/defaults for the draft.

Therefore the content/draft-level authoring record should be capable of retaining conceptually:

```text
template identity
template revision used
```

without duplicating template provenance into every block occurrence.

This is provenance, not runtime content authority.

#### Template updates do not rewrite drafts or published versions

Current frozen authority explicitly protects historical published content from silent template rewrite.

The working design extends the same safety to already-instantiated drafts: template changes must not silently mutate their scaffold.

Existing drafts remain governed by the revision they were instantiated/applied under until an explicit upgrade/reapplication operation occurs.

#### Deprecation

A template revision may become unavailable for new selection without invalidating previously resolved drafts or historical published Content Versions.

Historical rendering must not require the deprecated template definition because published content is materialised.

#### Dynamic-template exception

Working experience provenance preserves the possibility that a relationship might be explicitly designed as dynamic.

This grill does **not** authorise dynamic editorial content templates.

Ordinary content-template semantics are snapshot/materialisation based.

Any future dynamic template relationship requires separate pressure testing and explicit authority for:

- ownership;
- versioning;
- publication semantics;
- invalidation;
- rollback;
- provenance;
- failure behaviour.

The exception must not become a loophole for mutable shared article/body truth.

#### Translation

Template identity does not replace locale/content-version governance.

Textual defaults instantiated from a template become ordinary governed content values and enter the relevant translation/review lifecycle.

#### Personalised runtime composition is separate

Product-Law personalised composition of independently governed approved blocks is a separate runtime composition problem.

It is not ordinary CMS template inheritance.

#### Ash/storage

This decision establishes semantics only.

It does not yet decide whether content-template definitions are:

- code-authoritative;
- Ash/PostgreSQL-backed;
- split between code and governed data;
- represented through another mechanism.

That question is intentionally deferred.

#### Beacon

Stable Beacon `v0.5.1` provides mutable `Page`/`Layout` structures plus `PageSnapshot`/`LayoutSnapshot` historical snapshots.

Useful lesson:

- reusable mutable structures combined with publication need explicit version/snapshot thinking.

Not adopted:

- Beacon `Layout` as the NewYou content-template entity;
- runtime HEEx template authority;
- Beacon page/layout persistence as the direct NewYou model.

Classification:

```text
snapshot/versioning concept → ADAPT
Beacon Page/Layout model     → REFERENCE ONLY
runtime HEEx authority       → REJECT
```

#### LiveFrames

A LiveFrames template is presentation/design-system tooling.

A NewYou content template is governed authoring scaffolding.

Under `LF-01`, those identities remain separate even where LiveFrames supplies presentation implementation.

### 6.35 ACCEPTED GRILL DECISION

#### `GRILL-10 — Content Templates Are Revision-Addressable Authoring Scaffolds, Not Live Published-Content Authority`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> A NewYou content template is a broader governed authoring scaffold than a composed pattern. A pattern inserts a bounded local composition; a template scaffolds a substantial portion or whole governed content item within the authority of its selected content type.
>
> Templates may precompose or guide approved structure, ordering, default blocks/components, structural slots, metadata, CTA placement and bounded presentation defaults where permitted by current NewYou authority.
>
> Content-type and Domain rules remain upstream of templates. A template may narrow or organise permitted authoring but cannot expand forbidden composition, weaken workflow/review/translation/accessibility/publication requirements, or become a competing content authority.
>
> Universal publishability/business invariants belong to the content-type/Domain contract rather than existing only inside one template.
>
> Template declarations must distinguish hard structural constraints from defaults/recommendations; exact DSL representation remains deferred.
>
> Applying a template materialises/resolves ordinary NewYou content composition into the owning draft. Resulting block occurrences receive ordinary local occurrence keys and are owned by that draft/content lineage.
>
> Anything from the template that materially affects the eventual published representation must resolve to stable Content Version truth rather than remain implicitly inherited from whichever template definition is current at render time.
>
> Because template structure may govern authoring over time, an instantiated draft must be associated with an exact stable template identity/revision or equivalent immutable provenance. A later template revision must not silently replace the scaffold governing an existing draft.
>
> Template changes do not silently rewrite instantiated drafts or immutable published Content Versions. Moving an existing draft/content lineage to a newer template revision must be an explicit governed operation; exact migration UX and concurrency semantics remain deferred.
>
> Published Content Versions do not ordinarily retain a live semantic/rendering dependency on the current template. Exact template revision provenance may be retained at the content/version level without being duplicated into each block occurrence.
>
> Template deprecation may prevent new selection without invalidating already-resolved historical content.
>
> Ordinary content templates use snapshot/materialisation semantics by default. The authority-preserved possibility of an explicitly dynamic template relationship is **not authorised by this decision**; any such relationship requires a separate future pressure test defining its ownership, versioning, publication, invalidation, rollback and provenance semantics.
>
> Templates do not bypass ordinary locale/translation governance. Textual/default content instantiated from a template becomes governed content values subject to normal review and translation requirements.
>
> Runtime personalised composition of independently governed content is a separate concern and is not modelled as ordinary content-template inheritance.
>
> This decision does **not** yet decide whether template definitions are code-authoritative, Ash/PostgreSQL-backed, or represented through another governed mechanism. It establishes the required semantics first.
>
> Beacon's snapshot/versioning concepts are **ADAPTED conceptually**, while Beacon `Page`/`Layout` and runtime HEEx template authority remain **REFERENCE ONLY / REJECTED as a direct NewYou content-template model**.
>
> NewYou content templates remain distinct from LiveFrames presentation templates under `LF-01`.

### 6.36 Consequences fixed for later grills

1. A pattern is a bounded local insertion recipe; a template is a broader authoring scaffold.
2. Content-type/Domain authority remains upstream of template authority.
3. Universal publishability invariants do not live only in templates.
4. Template contracts distinguish hard constraints from defaults/recommendations.
5. An instantiated draft must be associated with an exact stable template revision or equivalent immutable provenance.
6. Template revision changes do not silently rewrite existing drafts.
7. Applying a template materialises/resolves ordinary content owned by the draft/content lineage.
8. Material published meaning does not depend on the current template definition at runtime.
9. Template provenance belongs at content/draft level rather than every block occurrence.
10. Published Content Versions ordinarily have no live semantic dependency on the template.
11. Dynamic content-template relationships are not authorised by this decision and require separate future architecture.
12. Translation/content governance remains independent of template identity.
13. Runtime personalised composition is separate from ordinary CMS template semantics.
14. Exact template storage/Resource design remains undecided.
15. Beacon snapshot concepts are reference material; Beacon Page/Layout runtime template authority is not adopted.
16. LiveFrames presentation templates remain distinct from NewYou content templates.

### 6.37 Block 2A.2 pressure test — template definition authority and storage

Current Content & Media Domain Law explicitly lists `Template Version` among its major concepts/entities and establishes PostgreSQL as the Domain's durable content/media metadata authority.

Current operating/frontend authority also requires reusable governed content templates, exact revision-safe evolution and historical protection from silent template rewrites.

The pressure test therefore compared code-only, database-only and responsibility-split models.

#### Code-only template authority

Rejected as the long-term template authority.

Application code is appropriate for stable capability definitions and validation semantics, but making every individual editorial template revision an Elixir/module/release concept would unnecessarily couple editorial evolution to software deployment and application-version identity.

Code may seed/bootstrap initial templates, but seed definitions must not remain a competing ongoing authority after governed revisions exist in Content & Media storage.

#### Unrestricted database-defined template behaviour

Rejected.

Persisting arbitrary HEEx, Elixir, JavaScript, CSS, renderer modules, LiveFrames component identifiers or unrestricted expression languages would recreate a dynamic executable CMS/page-builder authority and violate the already accepted code-authoritative capability boundary.

Template data must remain declarative and bounded.

#### Governed template data through a code-defined contract

Accepted.

The clean authority split is:

```text
CODE
  owns:
  - legal template-definition constructs;
  - interpretation semantics;
  - validation rules;
  - approved block/schema capabilities;
  - bounded presentation/configuration vocabulary;
  - materialisation logic.

CONTENT & MEDIA DATA
  owns:
  - which template identities exist;
  - which exact template revisions exist;
  - each revision's exact declarative scaffold/configuration;
  - the revision associated with a governed draft/content lineage.
```

This is not shared-write authority because the two sides own different truths.

Code defines **what a template is allowed to mean**.

Content & Media data defines **which governed templates/revisions exist and their exact approved values**.

#### No duplicated individual template definition

Once an individual template is represented as governed Content & Media data, the same template's semantic definition must not also exist independently as a second application-code authority.

Code-defined bootstrap/import representations may create governed records explicitly, but later code changes do not silently mutate existing persisted revisions.

#### Explicit versioned capability references

A stable Template Version must not depend on ambiguous concepts such as `latest` block schema.

Where template meaning depends on a persisted block contract, it must identify an explicit supported `block_type + schema_version` or equivalent immutable interpretation.

Unknown template constructs, unknown block types or unsupported required schema versions fail closed.

#### Immutable template-revision meaning

Once a template revision has governed an instantiated draft or is retained as historical provenance, its semantic definition must not mutate in place.

Template evolution creates a successor revision or equivalent immutable successor representation.

Exact revision-numbering, approval states and transition mechanics remain deferred.

#### Persisted template does not imply editor mutation permission

The fact that template definitions are database-backed does not establish that ordinary editors may create, edit or approve templates.

Current evidence establishes that editors may **start from** approved reusable templates, not that every editor may define global template authority.

Template authoring permissions, review and approval remain downstream decisions.

#### Historical independence

A Content Version retains materialised content and remains renderable independently of the referenced Template Version.

Template identity/revision may remain useful authoring provenance, but it is not runtime published-body authority.

A referenced historical template revision should therefore remain referentially meaningful even if retired/deprecated from new authoring.

#### Durable concept versus exact Resource design

This grill establishes durable PostgreSQL-backed Content & Media template-version truth.

It does **not** yet decide that the implementation must use exactly:

```text
ContentTemplate
ContentTemplateVersion
```

Ash Resources.

Current authority justifies the durable concept `Template Version`; the exact Resource decomposition still needs to be tested against lifecycle, reuse, relationships and existing Content Item/Version machinery.

#### Beacon

Beacon's persisted reusable-definition and snapshot ideas remain useful reference material.

Adapt:

- persistent reusable-definition identity;
- historical/version awareness;
- admin discoverability.

Reject:

- database-owned executable HEEx;
- runtime helper code;
- mutable persisted renderer/component authority.

#### LiveFrames

LiveFrames remains presentation-side under accepted `LF-01`.

NewYou persists semantic template identity/revision and approved declarative content scaffolding, never LiveFrames module/template identity as Content & Media authority.

### 6.38 ACCEPTED GRILL DECISION

#### `GRILL-11 — Template Revisions Are Content & Media–Owned Governed Data Interpreted Through a Code-Defined Contract`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou content-template definitions are not solely application-code authority.
>
> Individual template identities and exact revisions are durable Content & Media business truth and are persisted under Content & Media's PostgreSQL-backed authority so that template evolution, draft provenance and historical references survive deployments, restarts and application-version changes.
>
> Application code remains authoritative for the bounded template-definition language, interpretation semantics, validation rules, approved block/schema capabilities and other legal constructs through which template data may express a scaffold.
>
> This is a division of responsibility, not shared business authority: code defines **what a valid template may mean**, while governed Content & Media data defines **which templates/revisions exist and the exact declarative scaffold of each revision**.
>
> Individual template definitions must not be duplicated as competing semantic authorities in both code and PostgreSQL.
>
> Template data is declarative and may compose/reference only approved NewYou capabilities. It does not contain arbitrary HEEx, Elixir, JavaScript, CSS, implementation module names, LiveFrames component identities or unrestricted executable expressions.
>
> Unknown or unsupported template constructs, block types or required block-schema versions fail closed rather than falling back to a current/latest interpretation.
>
> Where a Template Version's meaning depends on a block representation, it must bind to an explicit supported versioned block contract or equivalent immutable interpretation rather than implicitly using whatever block schema is latest.
>
> Once a template revision is used as the stable scaffold/provenance of a draft, its semantic definition must not mutate in place. Template evolution creates a successor revision or equivalent immutable successor representation. Exact template authoring lifecycle and revision-transition rules remain deferred.
>
> Persisting templates does not imply that ordinary editors may create or modify them. Template-definition permissions, review and approval remain separate downstream decisions.
>
> Source-controlled seed/bootstrap definitions may create initial governed template records, but after creation they are not a competing ongoing business authority over the persisted revisions.
>
> Historical Content Versions remain renderable from their materialised content without requiring the referenced Template Version at runtime; template identity/revision is provenance and authoring history, not published-body authority.
>
> Template revisions referenced by governed history must remain referentially meaningful even when no longer selectable for new authoring; exact deprecation/retention lifecycle is deferred.
>
> Current authority justifies durable `Template Version` truth but does not yet force a particular Ash Resource decomposition. Whether this becomes dedicated `ContentTemplate` + `ContentTemplateVersion` Resources, reuses appropriate Content Item/Version machinery, or uses another narrow Content & Media representation is a JIT Resource-design decision.
>
> Beacon's persisted reusable-definition and snapshot concepts are **ADAPTED conceptually**, while database-owned executable HEEx/template code and runtime component authority remain **REJECTED**.
>
> LiveFrames remains presentation-side under `LF-01` and does not own NewYou template identity or revisions.

### 6.39 Consequences fixed for later grills

1. Individual template identity/revision is durable Content & Media truth.
2. Template revision truth is PostgreSQL-backed, not solely application-code authority.
3. Code owns the bounded template language, interpreter, validation and legal capability vocabulary.
4. Persisted data owns which templates/revisions exist and each revision's exact declarative scaffold.
5. No individual template definition may have competing semantic authorities in both code and data.
6. Template data is declarative and cannot carry arbitrary executable UI/code.
7. Unknown constructs and unsupported required block-schema versions fail closed.
8. Template revisions bind to explicit supported interpretation contracts rather than `latest`.
9. Used/referenced template revisions do not mutate in place.
10. Database persistence does not imply ordinary-editor definition authority.
11. Bootstrap/seed code may create governed templates but does not remain business authority afterward.
12. Historical Content Versions remain independently renderable from materialised content.
13. Historical template revisions remain referentially meaningful when retired from new authoring.
14. Durable Template Version truth is established; exact Ash Resource decomposition remains undecided.
15. Beacon executable database-template authority remains rejected.
16. LiveFrames remains presentation-side.

### 6.40 Block 2A.3 pressure test — dedicated template Resources versus Content Item/Version reuse

The pressure test compared semantic reuse of `Content Item / Content Version` against a dedicated editorial-template identity/version pair.

Current operating authority gives ordinary content items a delivery-oriented lifecycle:

```text
authorised idea/draft
→ governed content type
→ responsible editor
→ risk classification
→ scoped approvals
→ preview
→ publish/schedule
→ correct/supersede/withdraw
```

Editorial templates instead govern authoring scaffolds and revision provenance.

The overlap is versioning mechanics, not business meaning.

#### Reuse `Content Item / Content Version`

Rejected.

Doing so would either require inventing a hidden/template content type outside the approved catalogue or turning the ordinary content model into a polymorphic hierarchy with many template-specific exceptions.

Ordinary content semantics include:

- governed content type;
- content-risk classification;
- locale/translation branches;
- participant/publication state;
- correction/withdrawal;
- delivery provenance;
- discovery/search concerns.

Those semantics do not automatically apply to editorial authoring templates.

#### Translation mismatch

Template structure may be language-neutral.

Textual/default values instantiated from a template become governed content values and enter ordinary locale/translation workflow after materialisation.

That does not justify forcing the template itself into the full `Locale Version` model.

#### Publication mismatch

A template becoming available for editorial use is not the same business event as participant-facing content publication.

Likewise retiring a template from future authoring is not automatically equivalent to withdrawing delivered content.

These lifecycle differences argue against shared Resources.

#### Dedicated stable identity and immutable/successor versions

Accepted conceptual baseline:

```text
ContentTemplate
    ↓
ContentTemplateVersion
```

`ContentTemplate` represents stable lineage/identity.

`ContentTemplateVersion` represents the exact immutable/successor declarative scaffold revision.

Version-sensitive structure, constraints, defaults and interpretation-bound values belong on the version rather than mutable template identity state.

#### Relationship to ordinary content

A template version may scaffold a governed draft/content lineage:

```text
ContentTemplateVersion
        ↓ scaffold
Content Item / draft
        ↓
Content Version
```

The resulting content owns its own block occurrences, locale governance, approvals and publication lifecycle.

The template-version relationship is authoring provenance, not runtime rendering authority.

#### Separate concept does not prohibit implementation reuse

Shared implementation helpers may later support:

- immutable successor creation;
- optimistic concurrency;
- revision sequencing;
- provenance/audit;
- historical lookup.

Implementation reuse does not collapse the Resources.

#### Avoid one universal Template hierarchy

Current Domain Law's generic `Template Version` terminology does not prove that editorial content templates, communication/message templates, generated-plan templates and every other use of the word `template` share one lifecycle or Resource.

This grill concerns specifically editorial content-authoring templates.

Other template concepts require separate compatibility proof before sharing the same Resources.

#### Ash scope

This decision establishes the conceptual Resource pair only.

It does not yet freeze:

- exact primary keys;
- attributes;
- Ash identities;
- revision-number implementation;
- relationships;
- state machine;
- actions;
- permissions;
- approval Resources;
- content-type association cardinality;
- archive/deprecation fields.

Those remain JIT details.

#### Beacon

Beacon's separate Page/Layout/Component/Snapshot concepts reinforce the general lesson that semantically different durable structures should not be forced into one content entity.

Its concrete schemas remain reference only and are not adopted.

#### LiveFrames

LiveFrames template/component identity remains presentation-side under `LF-01`.

A NewYou `ContentTemplate` is Content & Media business identity, not a LiveFrames design/template identity.

### 6.41 ACCEPTED GRILL DECISION

#### `GRILL-12 — Editorial Content Templates Use Dedicated Template Identity/Version Resources Rather Than Reusing Deliverable Content Item/Version`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou editorial content-authoring templates are distinct durable Content & Media concepts from ordinary deliverable `Content Item` / `Content Version`.
>
> The working JIT baseline should therefore model the editorial template lineage as dedicated conceptual Resources:
>
> `ContentTemplate` — stable template identity/lineage; and  
> `ContentTemplateVersion` — exact immutable/successor scaffold revision.
>
> This decision establishes the Resource boundary but does not yet freeze exact Ash attributes, identities, relationships, actions, state-machine implementation or database schema.
>
> `Content Item / Content Version` are not reused as the template persistence model merely to share generic versioning mechanics. Ordinary content carries content-type, risk, locale/translation, publication, correction/withdrawal and delivery semantics that do not automatically apply to authoring templates.
>
> Editorial template availability/retirement is not equated with participant-facing content publication/withdrawal.
>
> Template structure may be language-neutral; textual/default values materialised into authored content enter normal governed content/locale review without forcing the template itself into the ordinary `Locale Version` model.
>
> `ContentTemplate` should remain a thin stable identity. Version-dependent scaffold, constraints, defaults and interpretation-sensitive values belong to immutable/successor `ContentTemplateVersion` records rather than mutable identity state.
>
> A governed draft/content lineage may retain an exact `ContentTemplateVersion` reference or equivalent immutable provenance to identify the scaffold used. This is authoring provenance, not a runtime rendering dependency.
>
> Historical Content Versions remain independently renderable from their materialised content even if the originating template version is later deprecated or unavailable for new authoring.
>
> Shared implementation helpers for version lineage, concurrency, provenance or audit may be reused where semantics align, but implementation reuse does not collapse the business Resources.
>
> The generic term `Template Version` in current Domain Law does not by itself authorise one universal Template Resource for editorial templates, communication templates, plan-generation templates or other structurally different template concepts. This decision concerns specifically **editorial content-authoring templates**.
>
> Other template categories must separately demonstrate compatible ownership, lifecycle and invariants before sharing these Resources.
>
> Beacon's concrete Page/Layout/Component persistence models remain **REFERENCE ONLY**, with no direct Resource reuse.
>
> LiveFrames template/component identity remains presentation-side under `LF-01` and is not NewYou `ContentTemplate` identity.

### 6.42 Consequences fixed for later grills

1. Editorial templates are dedicated durable Content & Media concepts.
2. The conceptual Resource pair is `ContentTemplate` + `ContentTemplateVersion`.
3. `Content Item / Content Version` are not reused for editorial template persistence.
4. `ContentTemplate` is thin stable identity/lineage.
5. Version-dependent scaffold/constraints/defaults belong on `ContentTemplateVersion`.
6. Template availability/retirement is not ordinary content publication/withdrawal.
7. Template structure does not inherit the ordinary Locale Version model by default.
8. Instantiated textual/default values become ordinary governed content values.
9. Content/draft lineage may retain exact template-version provenance.
10. Historical Content Versions remain independently renderable.
11. Shared implementation helpers may be reused without collapsing Resource semantics.
12. No universal Template hierarchy is assumed across editorial, communications, plan-generation or other template concepts.
13. Exact Ash fields, identities, relationships, actions and lifecycle remain undecided.
14. Beacon Resource schemas remain reference only.
15. LiveFrames identity remains presentation-side.

### 6.43 Block 2A.4 pressure test — minimum template lifecycle

Current authority requires that editors use **approved reusable templates**, but it does not define a dedicated template `review`, `published`, `scheduled`, `withdrawn` or similar lifecycle.

A working experience sequence `DRAFT → REVIEW → APPROVED → ACTIVE → SUPERSEDED / RETIRED` was verified to belong to **canonical metric definitions**, not editorial templates, and is therefore not imported into Content Template lifecycle.

The pressure test instead separated three independent questions:

1. Has this exact Template Version passed governance?
2. Which approved revision is current for new authoring?
3. Is the Template identity available for new authoring at all?

Collapsing those into one enum would lose historical truth.

#### Template Version maturity

Accepted minimum lifecycle:

```text
DRAFT
  ↓ approve
APPROVED
```

A draft Template Version is mutable authoring work and is not available for ordinary content creation.

Approval is the semantic freeze boundary. Once approved, the exact scaffold revision is immutable.

Further semantic change requires a successor draft/version.

#### No dedicated review state initially

Review workflow may exist operationally through reviewer assignment, comments, change requests, work queues or approval evidence without creating a durable `REVIEW` Template Version state.

A dedicated review state requires later evidence that it represents independent durable business truth.

#### Approval is not current selection

An approved Template Version remains historically approved even after another revision becomes the current choice for new authoring.

Therefore `APPROVED` does not mean `current`.

Current new-authoring selection is a separate `ContentTemplate`-level relationship.

Conceptually:

```text
ContentTemplate
  current_version → one exact APPROVED ContentTemplateVersion
```

#### Separate approval and selection actions

Approving a revision establishes that the exact scaffold is valid and immutable.

Selecting a revision as current establishes that new content created through that Template identity should use that approved revision.

These may be combined in UI convenience later, but remain distinct authoritative actions.

This permits approval/preview before rollout and controlled rollback of new-authoring selection without rewriting version history.

#### No `SUPERSEDED` Template Version state initially

When current selection changes from revision 7 to revision 8, revision 7 remains historically `APPROVED`.

Its non-current status is derived from current-selection/lineage facts rather than rewriting approval history to `SUPERSEDED`.

#### Template availability/retirement is identity-level state

Availability for new authoring belongs to `ContentTemplate`, not each Template Version.

Accepted minimum identity lifecycle:

```text
AVAILABLE
   ↓ retire
RETIRED
```

Retirement blocks new authoring from that Template identity while preserving all historical versions and content provenance.

Retirement does not withdraw or mutate Content Versions previously scaffolded from the template.

Retirement is treated as terminal initially; temporary suspension/reactivation requires separate future evidence.

#### Selectability is derived

A Template Version is usable for ordinary new authoring only when all applicable conditions hold, conceptually:

```text
template identity is AVAILABLE
AND
version == template.current_version
AND
version is APPROVED
AND
version is compatible with running code
AND
target content type permits it
AND
actor is authorised
```

No redundant persisted `selectable` business flag is introduced initially.

#### Exactly zero or one current revision per Template identity

A `ContentTemplate` has zero or one current Template Version.

Zero is valid during initial creation or after retirement.

One is the normal available state.

Multiple concurrently current revisions of one identity are not introduced; genuinely distinct simultaneously offered variants should normally be separate Template identities rather than overloading revision history.

#### Approval invariants

Approval must fail closed unless the exact Template Version is valid under the running code-defined template contract, including supported constructs, supported block/schema versions, internal structure and required/default value validation.

Exact approver roles and Approval Resource relationships remain deferred.

#### Current-selection invariants and concurrency

Changing current selection is an authoritative Content & Media transition.

It must revalidate that the target revision:

- belongs to the same ContentTemplate;
- is approved;
- is supported by the running contract;
- is eligible under applicable Template identity/content-type rules.

Concurrent current-version changes must not silently overwrite each other.

An expected-current version or equivalent optimistic/transactional guard is required conceptually; exact Ash/PostgreSQL implementation remains deferred.

#### Existing drafts remain pinned

Selecting a newer current Template Version affects new authoring only.

Existing drafts remain associated with their exact originating Template Version unless a separate explicit migration/reapplication operation is performed.

#### Defective approved revision

An approved revision is never edited in place.

Recovery uses one of:

- select an older still-valid approved revision as current;
- create/approve/select a successor revision;
- retire the Template identity;
- use ordinary content correction/withdrawal processes for already-materialised content where independently required.

A template defect does not automatically prove all derived Content Versions are invalid.

#### States explicitly not introduced

Without further evidence, `ContentTemplateVersion` does not gain:

- `review`;
- `active`;
- `superseded`;
- `retired`;
- `published`;
- `scheduled`;
- `withdrawn`;
- `rejected`.

These names may correspond to workflow or derived conditions but are not currently justified as independent durable Template Version state.

#### Beacon

Beacon stable `v0.5.1` Page lifecycle uses `created`, `published` and `unpublished` events with snapshots.

That lifecycle belongs to runtime published Pages and is not copied to NewYou editorial authoring templates.

The snapshot/history discipline remains useful reference material only.

### 6.44 ACCEPTED GRILL DECISION

#### `GRILL-13 — Template-Version Approval, Current Selection and Template Retirement Are Separate State Dimensions`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou does not copy the ordinary content publication lifecycle onto editorial `ContentTemplateVersion`.
>
> The minimum `ContentTemplateVersion` maturity lifecycle is:
>
> `DRAFT → APPROVED`.
>
> A draft template version may be edited and is never available for ordinary content creation. Approval is the semantic freeze boundary: once approved, the exact scaffold revision is immutable and later changes require a successor draft/version.
>
> No separate durable `REVIEW` state is introduced initially. Review workflow, reviewer assignments, change requests and approval evidence may exist without becoming Template Version lifecycle states; a dedicated review state requires future evidence.
>
> `APPROVED` means the exact version passed template governance. It does not mean the version is necessarily the revision currently offered for new authoring.
>
> Current new-authoring selection is an independent `ContentTemplate`-level relationship to exactly zero or one approved `ContentTemplateVersion`.
>
> Selecting a current version is an authoritative Content & Media action separate from version approval. Only an approved version belonging to that template identity and valid under the running contract may become current.
>
> Replacing the current revision does not mutate the predecessor's historical approval state. `SUPERSEDED` is therefore not introduced as a Template Version lifecycle status initially; successor/current-selection relationships carry that meaning.
>
> Template availability/retirement is likewise an independent `ContentTemplate` concern rather than a Template Version state. An available template may be retired from future authoring while all historical versions and content provenance remain intact.
>
> Template retirement does not withdraw, mutate or invalidate Content Versions previously scaffolded from its revisions.
>
> Ordinary new authoring may use a template revision only when the template identity is available, the revision is the current approved revision, the revision remains compatible with running code, the target content type permits it and the actor is authorised.
>
> Existing drafts remain associated with the exact Template Version under which they were instantiated when a newer current revision is selected.
>
> Current-version replacement requires concurrency-safe authoritative mutation so concurrent operators cannot silently overwrite each other's selection. Exact Ash/PostgreSQL mechanism remains deferred.
>
> A defective approved revision is never edited in place. Recovery uses an explicit change of current selection, a new successor revision, template retirement, or the appropriate separate content-correction process for already-materialised content.
>
> No `published`, `scheduled`, `withdrawn`, `active`, `superseded`, `retired` or `rejected` Template Version statuses are introduced without evidence that they represent independent durable version state.
>
> Beacon's Page `created/published/unpublished` event lifecycle is **REFERENCE ONLY** and is not adopted as the NewYou editorial-template lifecycle.

### 6.45 Consequences fixed for later grills

1. Template Version maturity is only `DRAFT → APPROVED` initially.
2. Approval freezes Template Version semantic content.
3. Later semantic change creates a successor version.
4. Review workflow does not automatically create a `REVIEW` version state.
5. Approval and current new-authoring selection are separate authoritative facts/actions.
6. `ContentTemplate` has zero or one current approved version.
7. Old approved revisions remain historically approved when no longer current.
8. `SUPERSEDED` is not a Template Version state initially.
9. Template identity availability is `AVAILABLE → RETIRED`.
10. Retirement is identity-level, blocks new use and preserves history.
11. Retirement does not withdraw previously materialised Content Versions.
12. Selectability is derived rather than stored as a redundant flag.
13. Current-version replacement requires concurrency-safe mutation.
14. Existing drafts remain pinned to their originating Template Version.
15. Defective approved versions are never edited in place.
16. Ordinary content publication lifecycle states are not copied into Template Version.
17. Beacon Page publication lifecycle remains reference only.

### 6.45A Owner-review clarification — `AVAILABLE` requires a current revision after first selection

**Recorded in:** v0.15.1 PATCH consistency repair.  
**Nature:** clarification of accepted `GRILL-13`; no new GRILL identifier and no rewrite of the original accepted decision text.

The permissive phrase “zero or one current Template Version” is tightened to avoid creating an unnamed temporary-unavailability state.

For a `ContentTemplate` identity:

```text
before first current-version selection:
    AVAILABLE + current_version = nil
    → permitted as incomplete setup
    → not selectable for ordinary authoring

after first current-version selection:
    AVAILABLE
    → MUST reference exactly one current APPROVED ContentTemplateVersion

to stop all new authoring:
    retire the ContentTemplate identity
    → do not clear current_version while remaining AVAILABLE
```

Consequences:

1. `AVAILABLE + current_version = nil` is permitted only before the first successful current-version selection.
2. Once a Template identity has had a current revision, remaining `AVAILABLE` requires exactly one current approved revision.
3. Clearing current selection is not a temporary-suspension mechanism.
4. The initial model has no unnamed “temporarily unavailable but AVAILABLE” condition.
5. Retirement is the explicit mechanism for stopping new authoring from the Template identity.
6. Retirement does not require erasing historical current-version provenance; exact retention of the pointer is an implementation detail, but history must remain interpretable.
7. A future requirement for temporary suspension/reactivation must justify a separately named state/dimension rather than weakening this invariant.

This clarification preserves the `GRILL-13` separation of approval, current selection and retirement while closing the ambiguity identified during owner review.

### 6.46 Block 2A.5 pressure test — content-type binding cardinality

Current NewYou authority requires the creator to select a governed content type before composing. The content type controls structure, metadata and applicable workflow. Reusable templates are subordinate authoring scaffolds and may not bypass content-type authority.

The pressure test compared one stable content-type binding per Template identity against multi-type compatibility.

#### Multi-content-type Template identity

Rejected initially.

A Template identity compatible with multiple content types would become a compatibility policy spanning multiple upstream contracts.

That would require cross-type validation of permitted block structures, required metadata, workflow assumptions, structural constraints and template eligibility.

If one content-type contract changed incompatibly while another remained valid, a previously approved Template Version could become only partially eligible. That would force per-type compatibility/approval/selectability state and substantially complicate the minimal lifecycle accepted in `GRILL-13`.

No current requirement justifies that machinery.

#### One stable governed content-type binding

Accepted.

Each `ContentTemplate` is associated with exactly one governed content type.

The association belongs to the stable Template identity and is inherited by all `ContentTemplateVersion` revisions.

Conceptually:

```text
article
  ├── Standard Article
  │     ├── r1
  │     └── r2
  └── Feature Article
        └── r1

lesson
  └── Standard Lesson
        └── r1
```

A Template identity does not move from `article` to `lesson` through an ordinary revision.

Changing target content type requires a distinct Template identity.

#### One content type may have many templates

The inverse cardinality is intentionally flexible.

A governed content type may have no Template, one Template or many Templates.

This supports different approved scaffolds for the same upstream content type without allowing Template identity to become cross-type authority.

#### Template requirement remains upstream

Whether a content type requires a Template is a content-type/domain contract rule.

It is not a property of one particular `ContentTemplate`.

This avoids contradictions such as one Template claiming to be mandatory while another Template for the same content type is optional.

#### Authoring order remains governed

Authoring follows:

```text
1. select governed content type
2. resolve eligible Templates for that type
3. choose Template when required/desired
4. instantiate exact current approved Template Version
5. compose governed content
```

A Template does not choose or redefine the content type.

#### Reuse across content types occurs below Template level

Shared structure across different content types should initially reuse code-authoritative block contracts, composed patterns, bounded slots and catalogue roles already accepted.

Slight declarative duplication between two type-specific Templates is preferred over introducing cross-type compatibility state without evidence.

#### Approval and later content-type change

Template Version approval validates the exact revision against its one bound content-type contract plus the code-defined template/block contracts.

If that upstream content-type contract later changes incompatibly, the Template Version remains historically `APPROVED`.

However, derived new-authoring eligibility must revalidate current compatibility.

Thus historical approval truth is preserved without implying permanent selectability.

#### Content-type retirement/unavailability

If a governed content type later becomes unavailable for new authoring, associated Templates stop being eligible through upstream rules.

Historical Template identities, versions and provenance remain intact.

Automatic destructive Template retirement/cascade is not introduced.

#### Immutable binding

The content-type association of a `ContentTemplate` is conceptually immutable.

A semantic move to another content type creates another Template identity rather than mutating lineage meaning.

#### Persistence representation

This decision establishes semantic cardinality only.

It does not yet choose whether the binding is represented through an Ash relationship, a stable governed content-type identifier or another implementation mechanism.

That remains JIT Resource design.

#### Beacon

Pinned stable Beacon `v0.5.1` has no equivalent stable Template Type mechanism to adopt.

A current Beacon `main` search exposes unreleased `template-types-design.md` work describing generic Template Types and an “everything is a page” direction, but that file does not exist in the pinned stable release.

It is **FUTURE REFERENCE ONLY**, not stable donor evidence and not NewYou authority.

#### LiveFrames

LiveFrames presentation/template reuse may span UI contexts.

That does not imply a NewYou governed content-authoring Template may span multiple content types.

Presentation reuse remains separate under `LF-01`.

### 6.47 ACCEPTED GRILL DECISION

#### `GRILL-14 — Each Editorial Content Template Has One Immutable Governed Content-Type Binding`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> Every NewYou editorial `ContentTemplate` is associated with exactly one governed content type.
>
> The content-type association belongs to the stable `ContentTemplate` identity and does not vary between `ContentTemplateVersion` revisions.
>
> Changing the target content type is not an ordinary template revision; it requires a distinct `ContentTemplate` identity.
>
> A governed content type may have zero, one or many `ContentTemplate` identities.
>
> Whether template use is optional or required belongs to the upstream content-type contract, not to an individual Template or Template Version.
>
> Authoring selects the governed content type first and then resolves only eligible templates belonging to that type, preserving current NewYou authority that content type controls structure, metadata and applicable workflow.
>
> Multi-content-type compatibility lists are not introduced initially. They would require cross-type validation, partial compatibility, per-type approval/eligibility and invalidation semantics without a current requirement.
>
> Template Version approval validates the exact revision against its one bound content-type contract and the code-defined template/block contracts.
>
> Historical `APPROVED` status remains immutable even if a later content-type contract change makes that Template Version unsuitable for new authoring. New-authoring selectability revalidates current content-type compatibility rather than rewriting historical approval.
>
> Content-type retirement or unavailability prevents new eligible use but does not erase Template identities, Template Versions or historical provenance.
>
> Structural reuse across different content types should initially occur through approved lower-level block contracts, composed patterns and other already-established reuse seams rather than through a shared multi-type Template identity.
>
> Slight duplication of declarative template scaffolds across content types is preferred over introducing a cross-type compatibility subsystem without evidence.
>
> This decision establishes semantic cardinality only. It does not yet decide whether the content-type association is represented as an Ash relationship, stable identifier field or another implementation mechanism.
>
> Beacon stable `v0.5.1` provides no equivalent stable Template Type mechanism to adopt. Beacon `main` contains unreleased Template Type design work, which remains **FUTURE REFERENCE ONLY** and does not alter this NewYou decision.
>
> LiveFrames presentation templates remain outside this Content & Media identity relationship under `LF-01`.

### 6.48 Consequences fixed for later grills

1. Every editorial `ContentTemplate` has exactly one governed content-type binding.
2. The binding belongs to stable Template identity and does not vary by Template Version.
3. Changing target content type requires a distinct Template identity.
4. A content type may have zero, one or many Templates.
5. Whether a Template is required belongs to the content-type contract.
6. Content type is selected before Template resolution.
7. Multi-type compatibility collections are not introduced initially.
8. Template Version approval validates against one upstream content-type contract.
9. Historical approval remains unchanged if later upstream changes make a version unsuitable for new authoring.
10. New-authoring eligibility revalidates current content-type compatibility.
11. Content-type unavailability does not erase historical Template lineage/provenance.
12. Cross-type reuse occurs through lower-level blocks/patterns rather than multi-type Template identity.
13. Content-type persistence representation remains undecided.
14. Beacon `main` Template Type design is future reference only; stable Beacon provides no mechanism to adopt.
15. LiveFrames presentation reuse remains outside this binding.

### 6.49 Block 2A.6 pressure test — Template Version scaffold representation

Block 2A.6 was evaluated under the v0.15.1 ten-question Ash-design hard stop.

Four candidate models were pressure-tested:

| Candidate | Result |
|---|---|
| Store ordinary concrete `BlockOccurrence`s | **REJECT** — wrong identity/ownership and turns Template Version into shadow content |
| Store only abstract slot/schema declarations | **REJECT** — too weak for approved defaults, ordered precomposition, initial content and placement semantics |
| Store ordinary blocks plus Template flags throughout | **REJECT** — contaminates the block-occurrence model and duplicates Template semantics |
| Store a typed declarative scaffold that materialises ordinary occurrences | **ACCEPTED BASELINE** |

The accepted direction is therefore a bounded declarative scaffold specification owned by the exact immutable `ContentTemplateVersion`.

#### Template scaffold is not Content Version composition

A Template Version does not own ordinary `BlockOccurrence` identities.

Ordinary block occurrences belong to concrete governed draft/Content Version composition.

Template scaffold elements instead use subordinate template-local keys for editing, diffing, validation errors, preview, provenance and successor-revision comparison.

Conceptually:

```text
template scaffold key
        ↓ materialise
fresh draft block occurrence_key
```

The scaffold key is not reused as the content occurrence key, is not a business identity and is not a public anchor.

#### No second block language

The Template scaffold may reference existing code-authoritative block contracts only through explicit supported:

```text
block_type + schema_version
```

or an equivalent immutable version-safe block-contract reference.

The Template layer does not redefine block fields, block payload schemas or renderer behaviour.

No Template-local schema such as:

```text
template component:
  heading: string
  image: media
```

may independently redefine what a referenced NewYou block contract means.

#### Block prototypes

Concrete Template scaffold block declarations are **block prototypes**, not content occurrences.

A prototype identifies an approved versioned block contract plus bounded initial/default authoring values where the contract permits them.

Instantiation creates fresh ordinary draft-owned `BlockOccurrence`s.

#### Explicit scaffold semantic classes

A scaffold declaration must express its semantics rather than relying on presence alone.

The architectural semantic classes are:

```text
REQUIRED STRUCTURE
BOUNDED CHOICE
DEFAULT
RECOMMENDATION
INITIAL CONTENT
PLACEMENT CONSTRAINT
```

These are semantic categories, not yet frozen Ash enums or persistence fields.

Their meanings are:

- **REQUIRED STRUCTURE** — must be satisfied at applicable governed transition boundaries;
- **BOUNDED CHOICE** — editor chooses only within an explicitly permitted bounded set;
- **DEFAULT** — initial state copied/materialised into the draft but changeable/removable where upstream rules permit;
- **RECOMMENDATION** — editor guidance only and never itself a validity invariant;
- **INITIAL CONTENT** — typed value copied into the draft and thereafter governed as ordinary content;
- **PLACEMENT CONSTRAINT** — narrows where specified approved contracts may occur.

Mere presence in a Template does not imply requiredness.

#### Template structural slots

Template-level structural slots are allowed as bounded authoring regions inside a Template Version.

They are distinct from `GRILL-06` code-defined block slots.

```text
block slot
→ local nested-composition contract inside one block type

Template structural slot
→ Template Version-level bounded authoring region
```

Template structural slots remain subordinate Template Version data and do not gain independent lifecycle, approval or publication authority.

**Historical at this point in the dossier:** their exact constraint vocabulary was deferred to Block 2A.7; `GRILL-16` subsequently resolves the initial structural-slot cardinality/allow-list vocabulary.

#### Constraint direction

Template constraints may only narrow upstream authority.

Conceptually:

```text
effective authoring permission
=
Content Type permissions
∩
Template Version constraints
∩
applicable Block / Block-slot constraints
```

Template authority never expands Content Type or block-contract permission.

#### Catalogue roles are not hard placement authority

Editorial/catalogue classifications such as `section`, `content component` or similar roles do not automatically become hard Template placement predicates.

Otherwise adding a new catalogue member could silently expand the semantics of an already approved Template Version.

Hard constraints therefore require stable version-safe approved contract semantics.

Catalogue roles may still support editor discovery/tooling.

#### Pattern expansion resolves before Template approval

Composed patterns may assist Template authoring.

However, an approved Template Version must preserve the resolved scaffold semantics rather than depend on whichever pattern definition exists at future instantiation time.

Conceptually:

```text
pattern
  ↓ resolve during Template authoring
scaffold declarations
  ↓ approve/freeze
ContentTemplateVersion
```

Pattern provenance may be retained as audit/editorial evidence if useful, but live pattern lookup does not define an approved Template Version's meaning.

#### Metadata, CTA and presentation defaults

Recommended metadata and bounded presentation defaults may be represented as Template Version declarative configuration only within the upstream Content Type and code-defined Template contract.

Universal required metadata remains Content Type authority.

Where structural placement such as a standard CTA can be represented directly by scaffold topology, the scaffold itself is preferred over a parallel duplicate placement field.

Presentation defaults remain bounded semantic values and may not contain raw CSS, HEEx, JS, renderer modules or LiveFrames identities.

#### Template-definition representation version

Template business revision and persisted scaffold-definition representation version are distinct dimensions.

Conceptually:

```text
ContentTemplateVersion business revision = 7
scaffold-definition schema version = 2
```

The latter identifies how application code interprets the persisted declarative scaffold.

Unknown scaffold-definition representation versions fail closed.

Exact field naming is deferred.

#### Subordinate structured data

Scaffold nodes, structural slots, defaults and recommendations have no independent business lifecycle, ownership, approval, publication or reuse identity.

Separate child Ash Resources are therefore not introduced initially.

The Template Version owns the scaffold as bounded structured data.

The exact Ash representation remains deferred.

#### Draft-time conformance

Hard Template Version constraints are not checked only at instantiation.

A draft that originated from an exact Template Version remains associated with that revision and continues to be evaluated against its hard scaffold constraints during authoring.

Working/autosaved drafts may temporarily be incomplete during editing.

This does not create another lifecycle state.

Applicable governed review/approval/publication transitions fail closed while hard Template constraints are unsatisfied.

#### Materialisation and publication

Instantiation materialises concrete block prototypes/default values into draft-owned truth.

Template-local scaffold identities, Template structural slot markers and recommendation markers do not become published content blocks.

At governed publication, the `ContentVersion` contains resolved ordinary content composition.

Published rendering does not require runtime Template expansion or lookup.

#### Unsupported referenced block schema

If an approved Template Version references a block schema that later becomes unsupported:

- the historical Template Version remains historically `APPROVED`;
- it fails closed for new instantiation/current eligibility;
- existing drafts must not silently reinterpret the reference;
- recovery requires restored reader support or explicit governed migration to a compatible successor;
- already published historical content follows the accepted block-schema evolution/correction rules rather than Template-driven silent rewrite.

#### Ten hard-stop answers

The Block 2A.6 hard-stop questions are resolved at architecture level as follows:

1. **Authoritative scaffold data** — exact immutable ordered scaffold topology, hard structural constraints, bounded choices, explicit versioned block-prototype references, Template structural slots, placement narrowing and declared defaults/guidance owned by the exact Template Version.
2. **Default/recommendation semantics** — defaults initialise draft state; recommendations are guidance only; initial substantive content becomes ordinary governed content when copied; only explicit hard declarations are conformance invariants.
3. **Block references** — explicit supported `block_type + schema_version` or equivalent immutable version-safe contract reference; never `latest` and never a Template-local block schema.
4. **Materialisation** — block prototypes produce fresh draft-owned BlockOccurrences and permitted defaults/initial values are copied into draft-owned authoring state; Template slot/recommendation markers do not become published blocks.
5. **Post-materialisation relationship** — draft retains exact Template Version provenance and hard authoring constraints; later Template revisions do not silently replace it; published rendering uses resolved Content Version truth.
6. **Required/optional validation** — Content Type owns global requirements; Template Version owns explicit narrower hard scaffold constraints; defaults/recommendations do not become required by presence.
7. **Nested composition** — bounded by code-defined block slots plus finite Template structural slots with explicit permitted contracts/cardinality; unrestricted recursion and live recursive pattern dependency are not introduced.
8. **Unsupported block schema** — historical approval remains true but new instantiation fails closed; drafts require supported interpretation or explicit migration; no silent reinterpretation.
9. **Conformance timing** — hard conformance continues during draft authoring; temporary incomplete autosaved drafts may exist, but governed review/approval/publication transitions fail closed.
10. **Invariant ownership** — Content Type owns global content rules; Template Version owns narrower scaffold rules; block contracts own local representation; block slots own local nested composition; Pattern owns correct expansion only while applied; Draft/Content Version owns exact materialised truth; publication revalidates/orchestrates without redefining these rules.

This satisfies the v0.15.1 Block-2A.6 Ash-design hard stop at architecture level. It does **not** authorise exact Ash fields/actions yet.

#### Beacon

Pinned stable Beacon `v0.5.1` provides useful primitive ideas around named slots, required/default semantics and typed component attributes.

Adapt conceptually:

- named bounded slots;
- typed/default concepts;
- explicit requiredness.

Reject as the NewYou Template model:

- persisted executable Component/template bodies;
- Phoenix-specific Component/slot persistence as business authority;
- arbitrary/binary option bags;
- renderer/runtime implementation references.

No direct stable Beacon code donor is accepted for the Template scaffold representation.

### 6.50 ACCEPTED GRILL DECISION

#### `GRILL-15 — Content Template Versions Own Typed Declarative Scaffolds That Materialise Governed Draft Composition`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> A NewYou `ContentTemplateVersion` owns an immutable bounded declarative scaffold specification used to initialise, guide and constrain content authoring for its one governed content type.
>
> The scaffold is not a `ContentVersion`, does not contain ordinary `BlockOccurrence` identities and does not create a second block/schema language.
>
> Scaffold declarations reference existing code-authoritative block contracts using explicit supported `block_type + schema_version` semantics or an equivalent immutable version-safe contract reference.
>
> Concrete scaffold block declarations are **block prototypes**. On instantiation they produce fresh ordinary `BlockOccurrence`s owned by the resulting draft; template-local scaffold keys are never reused as content occurrence keys.
>
> Scaffold declarations must have explicit semantics rather than relying on mere presence. The supported semantic categories are conceptually: **required structure, bounded choice, default, recommendation, initial content and placement constraint**. Exact persisted representation remains deferred.
>
> Hard Template Version rules may only narrow upstream Content Type and block/slot permissions. They may never expand them.
>
> Defaults are copied/materialised initial state and are changeable where upstream rules allow. Recommendations are guidance only. Initial substantive content becomes ordinary governed draft content when materialised and thereafter follows normal locale, risk, review and publication governance.
>
> Template structural slots are bounded authoring regions subordinate to `ContentTemplateVersion`; they are distinct from code-defined block slots and are not independently governed Resources.
>
> Hard placement/choice constraints use stable version-safe block contract semantics rather than mutable catalogue-role membership such as “any section”.
>
> Composed patterns may assist Template Version authoring, but an approved Template Version stores/resolves their resulting scaffold semantics and does not depend on future live pattern expansion.
>
> The Template Version representation carries an explicit scaffold-definition representation/schema version, or equivalent immutable interpretation discriminator, distinct from the Template's business revision. Unknown scaffold representation versions fail closed.
>
> Instantiation materialises concrete block prototypes/default values into draft-owned truth while retaining the exact Template Version reference as authoring provenance and constraint authority.
>
> Hard template conformance continues during draft authoring; it is not checked only at instantiation. The authoring experience may permit temporarily incomplete working/autosaved drafts, but applicable governed review/approval/publication transitions fail closed while hard template constraints remain unsatisfied.
>
> Published `ContentVersion` composition contains resolved ordinary content truth and no unresolved Template structural slots, template-local scaffold identities or runtime template expansion dependency.
>
> An approved Template Version referencing a block schema that later becomes unsupported remains historical approved truth but becomes ineligible for new instantiation until compatibility is restored or a compatible successor is selected. Existing drafts require explicit supported interpretation or governed migration rather than silent reinterpretation.
>
> Template scaffold nodes, structural slots, defaults and recommendations remain subordinate structured data owned by `ContentTemplateVersion`; separate child Ash Resources are not introduced without later evidence of independent relational/lifecycle requirements.
>
> Invariant ownership remains directional: Content Type owns global content requirements; Template Version owns narrower scaffold conformance; block and block-slot contracts own local representation/composition; the draft/Content Version owns exact materialised truth; publication revalidates those authorities rather than duplicating them.
>
> Arbitrary HTML, HEEx, Elixir, JavaScript, CSS, renderer/module identities, LiveFrames identities, arbitrary untyped maps and unrestricted expression languages are excluded from Template Version authority.
>
> Beacon stable named-slot/default/required concepts are **ADAPTED conceptually**; Beacon's persisted executable Component/template authority remains **REJECTED**.

### 6.51 Consequences fixed for later grills

1. `ContentTemplateVersion` owns a typed declarative scaffold, not ordinary content composition.
2. Template scaffold nodes use Template-local subordinate keys, never content occurrence keys.
3. Concrete Template blocks are prototypes that mint fresh draft BlockOccurrences.
4. Template scaffold references existing versioned block contracts and cannot redefine their schemas.
5. Semantic classes are explicitly distinguished: required structure, bounded choice, default, recommendation, initial content and placement constraint.
6. Mere Template presence does not imply requiredness.
7. Hard Template constraints only narrow upstream permission.
8. Template structural slots are distinct from block slots and remain subordinate data.
9. Catalogue roles do not silently become hard placement authority.
10. Pattern semantics are resolved into approved Template scaffold meaning rather than live-expanded later.
11. Template business revision and scaffold-definition representation version are distinct.
12. Unknown scaffold representation versions fail closed.
13. Hard Template conformance continues during draft authoring.
14. Temporarily incomplete autosaved drafts may exist; governed transitions fail closed when hard constraints fail.
15. Published Content Versions contain resolved content only and do not depend on runtime Template expansion.
16. Unsupported referenced block schemas block new Template instantiation without rewriting historical approval.
17. Separate scaffold-node/slot Ash Resources are not introduced initially.
18. Exact Ash scaffold representation remains undecided.
19. **Historical at GRILL-15 acceptance:** exact Template structural-slot/placement-constraint vocabulary remained undecided; `GRILL-16` subsequently resolves that seam.
20. Exact multilingual policy for literal Template initial/default content remains deferred.

### 6.52 Block 2A.7 pressure test — Template structural-slot and placement semantics

Current NewYou authority establishes that governed Templates may predefine required structural slots and ordering while remaining subordinate to the selected governed content type and approved block catalogue.

Current authority does not prescribe a slot cardinality DSL, nesting depth, editor mutation semantics or placement-expression language.

The pressure test therefore sought the smallest durable constraint vocabulary that satisfies Template authoring without creating a generic page/layout engine.

#### Structural-slot semantic core

A Template structural slot is a named Template-local authoring region subordinate to one immutable `ContentTemplateVersion`.

Its hard semantics are limited to:

- position in the ordered Template scaffold;
- cardinality;
- an explicit finite allow-list of supported version-safe block contracts.

This is sufficient to express required/optional singletons, repeated content regions and bounded choices without introducing another expression language.

#### Requiredness derives from minimum cardinality

Requiredness is not introduced as an independent fact that may contradict cardinality.

Conceptually:

```text
min = 0
→ optional

min >= 1
→ required
```

This prevents states such as:

```text
required = false
min = 1
```

Exact persisted representation remains deferred.

#### Cardinality

The semantic model supports:

```text
0..1
1..1
0..many
1..many
```

and justified bounded ranges such as:

```text
2..4
```

where real content semantics require them.

A finite business maximum is not invented merely to satisfy the word “bounded”.

Operational anti-abuse/size caps are separate from editorial business cardinality.

#### Explicit versioned contract allow-lists

Hard slot permission references exact supported version-safe block contracts, conceptually:

```text
paragraph/v1
heading/v2
image/v1
callout/v3
```

rather than mutable catalogue roles such as `section` or “whatever the content type currently permits”.

This ensures an approved historical Template Version does not silently expand when catalogue membership or upstream content-type definitions evolve.

Effective permission remains an intersection:

```text
Content Type permission
∩
Template structural-slot allow-list
∩
applicable block / block-slot constraints
```

Template slots never grant authority beyond upstream contracts.

#### Bounded choice

`BOUNDED CHOICE` from `GRILL-15` is expressed through cardinality plus the explicit allowed-contract set.

For example:

```text
LeadVisual
  cardinality: 1..1
  allowed:
    hero_image/v2
    hero_video/v1
```

means exactly one approved choice from that set.

A separate Boolean/choice-expression DSL is not introduced.

#### Required structure versus defaults

Hard structural requirement and initial materialisation remain separate concepts.

For example:

```text
HeroSlot
  cardinality: 1..1
  allowed:
    hero/v2

default prototype:
  hero/v2
```

The slot defines what must exist.

The prototype defines what is initially materialised.

Removing the default prototype from a working draft does not remove the slot requirement; the draft becomes incomplete until another permitted occurrence satisfies it.

#### Template-level ordering

Template scaffold-region order is authoritative Template structure.

Editors do not reorder Template structural slots inside an instantiated draft.

Changing:

```text
Hero
Body
CTA
```

to:

```text
Hero
CTA
Body
```

requires a successor Template Version or an explicit governed migration of an existing draft.

Generic `before`, `after`, `between` or arbitrary placement predicate languages are not introduced initially.

#### Ordering within a multi-item slot

Occurrences inside a multi-item structural slot retain ordinary content order.

Editors may reorder those occurrences unless a narrower upstream or block-level contract prohibits it.

If fixed child positions become materially required, the preferred model is separate ordered structural regions rather than a general ordering-expression language.

#### Working-draft incompleteness versus illegal mutation

Template conformance distinguishes temporary incompleteness from intrinsically illegal placement.

A working/autosaved draft may temporarily fall below a required slot minimum while an editor is replacing/restructuring content.

Such a draft is explicitly non-conformant and cannot cross applicable governed review/approval/publication boundaries.

By contrast, mutations that:

- insert a block contract outside the slot allow-list;
- use an unsupported schema version;
- place a block in a forbidden region;
- exceed a hard maximum;

fail immediately rather than persisting intentionally illegal structure.

#### Replace semantics

Replacement is permitted only if the resulting occurrence satisfies the target structural slot plus all upstream Content Type and applicable block/slot contracts.

Whether ordinary block-occurrence continuity preserves or mints an `occurrence_key` remains ordinary draft/occurrence design and is not redefined by Template slots.

#### Move semantics

Moving an occurrence between structural slots is permitted only when:

- the target slot allows the exact block contract;
- the target cardinality remains valid with respect to the hard maximum;
- upstream Content Type permission still holds;
- applicable block-level composition rules hold.

The source slot may temporarily fall below its minimum during editing and become non-conformant until repaired.

#### Deterministic slot membership

Template conformance may require knowing which Template structural slot owns a concrete portion of draft composition.

Where slot membership cannot be unambiguously derived from composition/order alone, the draft must retain enough explicit subordinate authoring-location information to resolve membership deterministically.

This authoring-location information:

- is not independent business identity;
- is not automatically part of the common `BlockOccurrence` envelope;
- exists to preserve exact Template Version conformance/provenance during authoring.

**Historical at this point in the dossier:** semantic ownership/addressability was deferred to Block 2A.8; `GRILL-17` subsequently resolves the draft Template-binding/slot-membership semantics, while exact Ash persistence remains JIT.

#### Publication boundary

Template structural-slot machinery is authoring infrastructure.

If a region matters after authoring because it changes semantic meaning, accessibility, presentation or runtime rendering independently of its children, that meaning must materialise into an approved published content/block/presentation concept.

Hidden Template-slot authority must not survive as an unresolved runtime dependency.

#### No recursive Template structural slots

Template structural slots do not recursively contain other Template structural slots initially.

Nested content composition occurs through approved code-defined block slots.

Conceptually:

```text
Template structural slot
        ↓
block occurrence
        ↓
code-defined block slot
        ↓
nested block occurrences
```

not:

```text
Template slot
  ↓
Template slot
  ↓
Template slot
```

Template-provided nested block prototypes may populate legitimate code-defined block slots, subject to those contracts.

#### No arbitrary global depth number

No global maximum nesting depth such as `5` is invented without evidence.

The architectural constraints are instead:

- Template structural slots themselves are non-recursive;
- nested content uses code-defined block slots;
- approved Template expansion must be finite and acyclic;
- individual block contracts may impose narrower nesting rules;
- runtime recursive Template/Pattern references are prohibited.

Operational depth/safety caps may be introduced later if measured evidence requires them.

#### Template approval validation

A draft Template Version cannot become `APPROVED` when its structural-slot specification is incoherent.

Approval fails closed for conditions including:

- `min > max`;
- a required slot with no permitted contract;
- unsupported block/schema references;
- slot permissions that exceed the bound Content Type;
- nested default composition violating a block-slot contract;
- cyclic or unbounded scaffold expansion.

#### Instantiation failure

Template instantiation validates the complete exact scaffold before committing materialisation.

It revalidates:

- Template identity availability;
- exact current Template Version approval/eligibility;
- Content Type compatibility;
- scaffold-definition representation support;
- referenced block-schema support;
- structural-slot integrity;
- default/prototype materialisability.

If the complete operation cannot be validated, no partial Template composition is inserted into the destination draft.

Exact transaction/action implementation remains deferred.

#### Beacon

Pinned stable Beacon `v0.5.1` `ComponentSlot` provides only a narrow conceptual donor:

- named slots;
- requiredness concepts;
- slot attribute validation.

It does not provide the NewYou semantics for Content Type narrowing, versioned allowed child contracts, business cardinality, Template-region ordering, working-draft incompleteness or publication materialisation.

Therefore:

```text
Beacon named-slot / requiredness idea
→ ADAPT conceptually

Beacon ComponentSlot persistence/schema
→ REFERENCE ONLY / REJECT as direct NewYou model
```

No direct Beacon code donor is accepted for this seam.

### 6.53 ACCEPTED GRILL DECISION

#### `GRILL-16 — Template Structural Slots Are Non-Recursive Ordered Authoring Regions with Explicit Cardinality and Versioned Contract Allow-Lists`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> A NewYou Template structural slot is a named Template-local authoring region subordinate to one immutable `ContentTemplateVersion`.
>
> Template structural slots define hard authoring/conformance structure through: their position in the ordered Template scaffold; cardinality semantics; and an explicit finite allow-list of supported version-safe block contract references.
>
> Requiredness is semantically derived from minimum cardinality greater than zero rather than treated as an independent contradictory fact. Cardinality may express optional/required singleton, repeated regions, or justified bounded ranges. A business maximum is not invented where the semantic requirement is simply “many”; operational safety limits remain separate.
>
> Hard slot allow-lists reference explicit supported `block_type + schema_version` contracts or equivalent immutable version-safe references. Mutable catalogue roles and “whatever the Content Type currently allows” are not accepted as historical Template Version placement authority.
>
> `BOUNDED CHOICE` is expressed through slot cardinality plus its explicit allowed-contract set rather than through a separate expression language.
>
> Hard required structure should preferentially be represented through slot cardinality/allowed-contract semantics. Default block prototypes are initial materialisation values within those structural regions and do not themselves create requiredness.
>
> The ordered sequence of Template structural regions defines Template-level placement/order. Editors do not reorder Template slots in an instantiated draft; changing the scaffold-region order requires a successor Template Version or an explicit governed draft migration.
>
> Occurrences within a multi-item slot retain ordinary content order and are editor-reorderable unless a narrower upstream/block constraint applies. Generic `before/after/between` predicate languages are not introduced initially.
>
> Editors may remove an occurrence even when doing so temporarily causes a working/autosaved draft to fall below a slot's minimum cardinality; the draft is then explicitly non-conformant and cannot cross applicable governed review/approval/publication boundaries until repaired.
>
> Mutations that introduce a forbidden block contract, forbidden placement, unsupported schema version or exceed a hard maximum fail immediately rather than being stored as intentionally illegal draft structure.
>
> Replacement or movement is permitted only when the resulting target placement satisfies the exact Template slot, Content Type and applicable block/slot contracts. Moving from a source slot may leave that source temporarily incomplete during editing.
>
> During Template-governed authoring, draft state must preserve enough explicit subordinate authoring-location information to determine Template structural-slot membership unambiguously where membership cannot be derived from composition alone. This information is authoring addressability, not independent business identity, and is not added to the common `BlockOccurrence` envelope by this decision.
>
> Template structural-slot machinery is authoring infrastructure. If a structural region has meaning that must survive publication or affect runtime rendering independently of its child ordering/content, that meaning must materialise into an approved published content/block/presentation concept rather than remain hidden Template-slot authority.
>
> Template structural slots do not recursively contain other Template structural slots initially. Nested content composition occurs through approved code-defined block slots. Template-provided nested block prototypes may use those block slots but must satisfy their contracts.
>
> No arbitrary global nesting-depth number is introduced without evidence. Approved Template expansion must nevertheless be finite and acyclic, and unrestricted recursive Template/Pattern dependency is prohibited.
>
> A Template Version cannot become `APPROVED` with incoherent slot semantics, including impossible cardinality, missing required choices, unsupported references, constraints that exceed Content Type authority, invalid nested defaults or cyclic/unbounded expansion.
>
> Template instantiation validates the complete exact scaffold before committing materialisation; failure leaves no partially instantiated Template composition.
>
> Beacon stable named-slot/requiredness ideas are **ADAPTED conceptually**, but Beacon `ComponentSlot` persistence and Phoenix-specific slot semantics remain **REJECTED as the NewYou Template structural-slot model**.

### 6.54 Consequences fixed for later grills

1. Template structural slots are named Template-local ordered authoring regions.
2. Requiredness derives from minimum cardinality.
3. Cardinality supports optional/required singleton, repeated and justified bounded ranges.
4. “Many” need not receive an invented business maximum.
5. Slot permissions use explicit version-safe block-contract allow-lists.
6. Mutable catalogue roles are not hard historical placement authority.
7. Bounded choice uses cardinality + explicit allowed-contract set.
8. Slot requirement and default block prototype are separate concepts.
9. Template slot order is fixed by the Template Version.
10. Multi-item slot occurrence order remains ordinary editor-controlled content order unless narrowed elsewhere.
11. Generic ordering predicate languages are not introduced.
12. Temporary below-minimum working drafts may exist but are non-conformant.
13. Forbidden placements/contracts/unsupported schemas/over-maximum mutations fail immediately.
14. Move/replace operations revalidate the target Template slot and upstream contracts.
15. Draft authoring state must preserve deterministic slot membership when order alone is ambiguous.
16. Slot-membership state is authoring addressability, not ordinary BlockOccurrence identity.
17. Runtime-significant region meaning must materialise into published content truth rather than hidden Template-slot state.
18. Template structural slots are non-recursive.
19. Nested content uses code-defined block slots.
20. No arbitrary global depth number is introduced initially.
21. Approved Template expansion must be finite and acyclic.
22. Template approval fails closed for incoherent slot/scaffold semantics.
23. Instantiation is all-or-nothing at the semantic operation level.
24. Exact slot-membership/draft-provenance persistence shape remains undecided.
25. Exact Ash representation remains undecided.

### 6.55 Block 2A.8 pressure test — draft↔TemplateVersion provenance and deterministic structural-slot membership

Block 2A.8 pressure-tested the distinction between:

- active Template authoring authority;
- mutable authoring-only Template structural-slot membership;
- ordinary block occurrence identity;
- explicit Template migration;
- immutable Content Version provenance;
- runtime rendering authority.

Current NewYou authority requires immutable/traceable content versions and prevents later Template changes from silently rewriting historical published content.

The accepted GRILL chain also requires exact Template Version pinning, continuing draft-time Template conformance and deterministic slot membership where flat order alone is ambiguous.

#### One exact active Template Version binding

A Template-governed draft retains one exact active `ContentTemplateVersion` binding for ongoing authoring conformance.

For content types where Templates are optional, a draft may have no Template binding.

Once Template-governed authoring is instantiated, the binding is pinned to that exact version.

Later changes to:

- `ContentTemplate.current_version`;
- Template retirement;
- creation of successor Template Versions;

do not silently change the draft's active Template Version.

There is no live “follow current Template” relationship.

#### Retirement does not rewrite existing drafts

Retiring a `ContentTemplate` prevents new authoring through that Template identity but does not erase or rewrite an existing draft's exact Template Version provenance.

Existing drafts may continue under their pinned version while that version remains safely interpretable.

Business retirement and technical compatibility remain separate concerns.

#### Explicit deterministic Template structural-slot membership

Where Template structural-slot membership cannot be reconstructed unambiguously from concrete composition/order, the draft preserves explicit subordinate authoring-location membership.

Conceptually:

```text
Template Version r7

HeroSlot
  → occurrence A

BodySlot
  → occurrences B, C, D
```

This membership is authoritative for Template-conformance authoring state.

It is not independent business identity.

It is not added to the universal `BlockOccurrence` envelope.

#### Membership applies at the Template structural level only

Template membership applies only at the scaffold level governed by Template structural slots.

Nested composition inside a block remains governed by that block's code-defined slot contract.

This avoids duplicate recursive Template membership.

Conceptually:

```text
Template structural slot
  ↓
Section occurrence
  ↓
Section block slot
  ↓
nested block occurrences
```

#### Active binding and slot membership are different facts

The active Template Version is pinned unless an explicit migration occurs.

Template slot membership is mutable under ordinary guarded draft editing.

Moves/replacements may change membership while the Template Version remains the same.

#### Coherent move/replace mutation

Concrete draft composition and Template structural-slot membership must not commit in contradictory states.

A move/replacement operation that changes both must preserve the invariant atomically at the business-operation boundary.

Exact Ash transaction/concurrency implementation remains deferred.

#### Template migration is explicit governance

Changing an existing draft from one Template Version to another is an explicit governed Template migration.

It is not:

- a direct foreign-key/reference edit;
- automatic adoption of the Template identity's current revision;
- a background update;
- live inheritance.

Migration evaluates the source draft composition/membership against the target exact approved Template Version and produces a new coherent target authoring state or no committed migration.

#### Same Template identity only initially

The initial migration seam is limited to successor/version migration within the same `ContentTemplate` identity.

Generic migration/retemplating between unrelated Template identities is not introduced without separate evidence and pressure-testing.

#### Migration is all-or-nothing

A Template migration validates/transforms the complete affected authoring structure before committing:

```text
source Template Version
+
current draft composition
+
source slot membership
        ↓
target Template Version migration
        ↓
target composition
+
target slot membership
```

Failure/conflict leaves the source draft state intact.

#### Authored content must not silently disappear or be overwritten

Migration must not silently:

- discard authored occurrences;
- overwrite editor-authored payload values with new Template defaults;
- reinterpret incompatible block contracts;
- drop excess occurrences because a target slot has a smaller maximum;
- arbitrarily reclassify ambiguous content between target structural slots.

Where a deterministic safe correspondence does not exist, migration requires explicit conflict resolution.

#### Template defaults are not replay semantics

Template defaults initialise authoring.

They are not automatically reapplied when:

- reopening a draft;
- validating a draft;
- selecting a newer Template Version;
- performing migration.

A migration may introduce target-required material only through explicit migration semantics that preserve authored truth and surface conflicts.

#### Active binding versus historical migration provenance

The draft's active Template Version and its historical Template application/migration provenance are distinct.

Conceptually:

```text
active authoring authority:
  r7

historical provenance:
  originated r4
  migrated r4 → r6
  migrated r6 → r7
```

Later migration does not erase origin/migration history.

Exact audit-history persistence remains deferred.

No new audit/history Resource is introduced by this decision.

#### Immutable Content Version retains effective Template Version provenance

When an immutable `ContentVersion` is created from a Template-governed draft, it retains the exact effective `ContentTemplateVersion` against which that snapshot was governed.

This is historical provenance, not runtime Template inheritance.

For content created without a Template where the Content Type permits that, the effective Template Version is absent.

#### Authoring-only slot membership does not survive as runtime authority

Mutable Template structural-slot membership is authoring infrastructure.

It does not survive into `ContentVersion` as live Template authority by default.

If a region has semantic/presentation meaning that must survive publication, that meaning must materialise into explicit governed Content Version structure/presentation rather than hidden Template-slot membership.

#### Publication validates before authoring-only state becomes unnecessary

Before immutable snapshot creation, publication validates:

- the exact active Template Version;
- current concrete draft composition;
- deterministic Template slot membership;
- all hard Template constraints.

Only after successful validation does the immutable Content Version become authoritative for resolved content.

#### Successor drafts from historical Content Versions

A successor draft created from an immutable Content Version begins with that Content Version's exact effective Template Version provenance rather than silently adopting whatever Template Version is currently selected for new authoring.

If that historical Template Version is no longer safely authorable/interpretable, the system requires restored compatibility or an explicit governed migration.

#### Retirement versus unsupported interpretation

Template retirement alone does not invalidate existing pinned drafts or historical Content Versions.

If application code can no longer safely interpret the pinned Template scaffold or referenced block schemas, governed transitions fail closed.

The remedy is restored support or explicit migration, not silent reassignment.

#### Coherent conformance boundary

For mutations that affect Template-governed authoring, these facts form one coherent conformance boundary:

```text
active exact Template Version
+
concrete draft composition
+
Template structural-slot membership
```

Exact optimistic locking, transactional implementation and Ash action design remain deferred.

#### Beacon

Beacon stable snapshot/history concepts reinforce the principle of preserving historical state/provenance.

Beacon does not provide a direct model for NewYou's exact Template Version pinning, deterministic Template structural-slot membership or governed Template migration provenance.

Therefore:

```text
Beacon snapshot/history principle
→ ADAPT conceptually

Beacon persistence as donor for this seam
→ NO DIRECT DONOR
```

### 6.56 ACCEPTED GRILL DECISION

#### `GRILL-17 — Template-Governed Drafts Are Pinned to One Exact Active Template Version with Explicit Subordinate Slot Membership and Durable Migration Provenance`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> A NewYou draft whose authoring was instantiated from a governed editorial Template retains an exact active `ContentTemplateVersion` binding for ongoing Template conformance.
>
> The active binding is pinned. Later changes to `ContentTemplate.current_version`, Template retirement or creation of successor Template Versions do not silently alter an existing draft's binding.
>
> Template-governed draft composition preserves explicit deterministic Template structural-slot membership for the occurrences whose Template conformance depends on those regions. Slot membership is subordinate mutable authoring state, not independent business identity and not part of the universal `BlockOccurrence` envelope.
>
> Template structural-slot membership applies at the Template scaffold level. Nested child composition inside a block remains governed by that block's code-defined slot contract rather than duplicating Template membership recursively.
>
> Content movement/replacement and its Template-slot membership change form one coherent authoring mutation and must not commit in contradictory states.
>
> Changing an existing draft's active Template Version is an explicit governed **Template migration**, not a direct reference edit and not automatic adoption of the Template identity's current revision.
>
> The initial migration seam supports successor/version migration within the same `ContentTemplate` identity. Generic migration between unrelated Template identities is not introduced without separate evidence.
>
> Template migration validates/transforms the complete affected draft composition and Template membership against the target approved Template Version before committing. Migration is all-or-nothing at the business-operation level.
>
> Migration must not silently discard authored content, overwrite authored payloads with Template defaults, reclassify incompatible content or partially migrate a draft. Non-deterministic incompatibilities become explicit conflicts requiring governed resolution.
>
> Template defaults are initialisation semantics and are not automatically replayed whenever a draft is opened, validated or migrated.
>
> The draft's currently active Template Version and its historical Template-application/migration provenance are separate facts. Explicit migrations preserve an append-only/interpretable from→to history; later binding does not erase origin/migration provenance.
>
> When an immutable `ContentVersion` is created from a Template-governed draft, it retains the exact **effective `ContentTemplateVersion` provenance** against which the snapshot was governed. This reference is provenance only and is not runtime rendering/inheritance authority.
>
> Mutable Template structural-slot membership is authoring infrastructure and does not survive into `ContentVersion` as live Template authority by default. If a structural distinction matters after publication, it must materialise into approved Content Version content/presentation truth.
>
> Before a Template-governed draft is cut into an immutable `ContentVersion`, the exact draft composition and Template structural-slot membership are validated against its pinned `ContentTemplateVersion`. Subsequent review, approval, scheduling and publication operate on that exact immutable Content Version and do not dereference mutable draft truth. Only resolved governed content becomes rendering authority.
>
> A successor draft created from an immutable Content Version begins from that Content Version's exact effective Template Version provenance rather than silently adopting the Template identity's then-current version. Unsupported historical Template interpretation requires restored support or explicit migration.
>
> Template identity retirement does not invalidate existing pinned drafts or historical Content Versions. Technical inability to interpret a referenced Template/block schema is a separate fail-closed compatibility condition.
>
> Draft composition, active Template binding and structural-slot membership constitute one coherent conformance boundary for mutations that affect them. Exact Ash concurrency/transaction implementation remains deferred.
>
> Exact storage for active binding, slot membership and migration history remains undecided; this decision does not introduce a `TemplateBinding`, `TemplateMembership` or migration-history Ash Resource by itself.
>
> Beacon's snapshot/history principle remains **ADAPTED conceptually**, but Beacon supplies no direct persistence model for this NewYou provenance seam.

### 6.57 Consequences fixed for later grills

1. Template-governed drafts retain one exact active Template Version binding.
2. That binding is pinned and never follows current Template selection automatically.
3. Existing draft bindings survive Template retirement while safely interpretable.
4. Deterministic Template structural-slot membership is explicit authoring state when inference would be ambiguous.
5. Slot membership is not added to the universal BlockOccurrence envelope.
6. Template membership applies only at Template structural level.
7. Nested child placement remains block-slot contract truth.
8. Active Template binding and slot membership are separate state dimensions.
9. Moves/replacements update composition and membership coherently.
10. Template Version change is explicit governed migration.
11. Initial migration supports versions within the same Template identity only.
12. Migration is all-or-nothing.
13. Migration cannot silently discard or overwrite authored content.
14. Ambiguous/incompatible target correspondence becomes an explicit conflict.
15. Template defaults are not replayed automatically.
16. Active Template Version and historical migration provenance are separate facts.
17. Migration provenance is append-only/interpretable.
18. Immutable Content Versions retain effective Template Version provenance.
19. Effective Template Version provenance is not runtime inheritance.
20. Mutable Template slot-membership authoring state does not survive into Content Version as live authority by default.
21. Publication validates pinned Template Version + composition + membership before immutable snapshot creation.
22. Successor drafts from historical Content Versions begin from that exact effective Template Version provenance.
23. Unsupported historical interpretation requires restored support or explicit migration.
24. Template retirement and technical incompatibility remain distinct.
25. Exact storage/Ash/concurrency mechanics remain undecided.
26. **Historical at GRILL-17 acceptance:** Template migration correspondence rules were not yet decided; `GRILL-18` subsequently resolves the safe stable-key structural-rebinding boundary.

### 6.58 Block 2A.9 pressure test — automatic Template migration correspondence versus human resolution

Block 2A.9 pressure-tested the safe boundary between deterministic Template migration and content transformation.

Stable Template structural-slot keys carry logical continuity across successor Template Versions. Reusing the same key asserts the same logical authoring region; labels may change without changing the key. Semantically different regions require different keys.

Automatic Template migration is restricted to deterministic structural rebinding. It may preserve existing authored occurrences, payloads, occurrence keys and order within repeated slots; rebind same-key structural slots; apply target scaffold-region ordering; and accept target constraints where the actual existing content already conforms.

It may not delete or invent authored content, replay defaults silently, substitute block types, rewrite payloads, guess correspondence, truncate repeated content, split/merge populated regions heuristically or implement block-schema migration.

Widened target constraints are automatically compatible with already-valid content. Narrowed constraints are automatic only when the actual existing draft already satisfies them.

A removed source slot may disappear automatically only when empty. A populated unmapped source slot creates a conflict.

A new optional target slot may remain empty. A new required target slot not already satisfied by safely preserved content creates a conflict even if the target Template supplies a default prototype; applying such a default is an explicit resolution.

Slot-key replacement, populated split and populated merge are not inferred automatically. No general migration-mapping DSL or predecessor-alias system is introduced initially.

Template migration does not implement block-schema migration. If the exact existing block contract/schema is not valid under the target slot, migration conflicts unless separately governed block-schema evolution has already produced a valid occurrence.

Unchanged logical occurrences preserve their `occurrence_key`. Moving the same occurrence to another explicitly resolved valid slot does not itself mint a new key. Replacement content receives a new key under ordinary occurrence semantics.

Template block-prototype keys do not become hidden permanent lineage for materialised draft BlockOccurrences. Structural-slot membership is the migration anchor.

Migration conflict semantics include: populated unmapped source region; unsatisfied required target region; disallowed occurrence contract; target maximum exceeded; ambiguous split/merge/key correspondence; unsupported contract/schema; and required content transformation.

Migration first derives and validates a complete proposed plan from the exact source draft state. Unresolved conflicts leave the source draft unchanged and bound to its source Template Version. Only a completely resolved/revalidated plan commits composition, slot membership, active target Template Version and migration provenance together.

A migration plan is valid only for the exact source draft state against which it was derived; concurrent source changes invalidate/recompute the plan.

Pinned stable Beacon provides no direct donor for these migration semantics.

### 6.59 ACCEPTED GRILL DECISION

#### `GRILL-18 — Automatic Template Migration Is Limited to Stable-Key Structural Rebinding That Preserves Authored Content Exactly`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> Stable Template structural-slot keys carry logical continuity across successor `ContentTemplateVersion`s. Reusing the same key asserts that the successor slot represents the same logical authoring region; presentation labels may change without changing the key. A semantically different region requires a different key.
>
> NewYou does not infer Template migration correspondence from display labels, catalogue roles, structural similarity, block type heuristics or relative position.
>
> Automatic Template migration is restricted to deterministic **structural rebinding**. Existing authored occurrences, payloads and ordinary occurrence keys are preserved unchanged when their same-key target structural slot still permits the exact block contract and the target cardinality remains satisfied.
>
> Target Template scaffold-region reordering may apply automatically when stable slot keys preserve logical region correspondence. Existing occurrence order within each repeated slot remains unchanged.
>
> Widened target allow-lists/cardinality migrate automatically. Narrowed constraints migrate automatically only when the actual existing draft composition already satisfies the target rules.
>
> A removed source structural slot may disappear automatically only when it contains no authored occurrences. A populated source slot without a same-key target creates an explicit migration conflict.
>
> A new optional target structural slot may remain empty automatically. A new required target slot not satisfied by safely mapped existing content creates an explicit conflict, even when the target Template provides a default prototype. Applying such a target default is an explicit resolution, not silent migration behaviour.
>
> Slot-key changes, populated slot splits and populated slot merges are not inferred automatically. They require explicit human correspondence/resolution initially.
>
> No general Template migration-mapping DSL, predecessor-key alias system or transformation expression language is introduced without later evidence that repeated real migrations justify one.
>
> Template migration does not implement block-schema migration. If a target slot no longer permits the exact source block contract/schema, that is a conflict unless a separately governed block-schema migration has already produced a target-valid occurrence.
>
> An unchanged authored occurrence preserves its `occurrence_key` across Template migration. Moving that same occurrence to another explicitly chosen valid target slot does not by itself require a new occurrence key. Replacing an occurrence with newly created content creates a new key according to ordinary block-occurrence semantics.
>
> Template block-prototype keys do not automatically correspond to materialised draft BlockOccurrences. Structural-slot membership, not original prototype identity, is the migration anchor.
>
> Automatic migration requires every populated source slot to map by stable key, every mapped occurrence to remain target-valid, all target cardinalities to be satisfied, every target required slot to be satisfied from preserved existing content, all required schemas to remain supported, and no authored content transformation/deletion/invention to be necessary.
>
> Migration conflicts include conceptually: populated unmapped source region, unsatisfied required target region, disallowed occurrence contract, target maximum exceeded, ambiguous split/merge/key correspondence, unsupported contract/schema and required content transformation. Exact conflict persistence/type representation remains deferred.
>
> Conflict discovery does not partially mutate the draft. Migration first derives and validates a complete proposed plan; unresolved conflicts leave the source draft bound to the source Template Version. Only a completely resolved and revalidated plan commits composition, slot membership, active Template Version and migration provenance together.
>
> Migration applies only to the exact source draft state against which the plan was validated; concurrent source changes invalidate/recompute the plan. Exact concurrency mechanism remains deferred.
>
> Beacon provides **NO DIRECT DONOR** for these migration semantics.

### 6.60 Consequences fixed for later grills

1. Stable Template structural-slot keys carry logical continuity across Template revisions.
2. Human-facing label changes do not require key changes when semantics remain the same.
3. Semantically different regions require different stable keys.
4. NewYou does not infer migration correspondence heuristically.
5. Automatic migration is structural rebinding only.
6. Automatic migration preserves authored occurrences, payloads and ordinary occurrence keys.
7. Target scaffold-region movement/order changes may apply automatically where stable-key identity is preserved.
8. Widened constraints are automatically compatible with already-valid content.
9. Narrowed constraints are automatic only when existing content already satisfies them.
10. Populated removed/unmapped source regions create conflicts.
11. New optional target regions may remain empty.
12. New required unsatisfied target regions create conflicts even if target defaults exist.
13. Target defaults are explicit resolution options, not automatic migration replay.
14. Slot-key replacement is not inferred as rename.
15. Populated split/merge requires explicit resolution.
16. No generic migration-mapping DSL is introduced initially.
17. Block-schema migration remains separate authority.
18. Unchanged logical occurrences preserve occurrence keys.
19. Moving the same occurrence does not by itself create a new occurrence.
20. Newly created replacement content receives new occurrence identity.
21. Template prototype keys are not hidden draft-occurrence lineage.
22. Migration conflict categories are defined semantically but not yet persisted.
23. Migration planning does not partially mutate the source draft.
24. A completely resolved plan commits composition, membership, target binding and provenance together.
25. Migration plans are valid only for the exact source draft state they evaluated.
26. Exact concurrency and Ash action mechanics remain deferred.
27. Block 2A.10 must determine whether another architecture question still blocks JIT Resource/action design.

### 6.61 Block 2A.10 closure audit — editorial Content Template reuse discovery

Block 2A.10 performed an adversarial closure audit rather than assuming that accumulated detail implied readiness.

The result distinguishes Template-specific semantic closure from downstream JIT dependency gates.

#### Closure outcome

```text
BEACON TEMPLATE REUSE DISCOVERY
→ PASS / CLOSED

CONTENT & MEDIA JIT HANDOFF
→ PASS

CORE ContentTemplate / ContentTemplateVersion RESOURCE JUSTIFICATION
→ PASS

EXECUTABLE IMPLEMENTATION
→ NOT AUTHORISED
```

The accepted Template-specific semantics are sufficiently closed for handoff to Content & Media JIT.

Further Beacon-specific Template grilling would now risk crossing from reuse discovery into speculative implementation design.

#### Resource justification is closed

Dedicated C&M-owned concepts remain justified:

```text
ContentTemplate
→ stable Template identity / lineage / content-type binding / availability

ContentTemplateVersion
→ exact immutable governed scaffold revision / maturity / successor semantics
```

These concepts are sufficiently justified for exact Resource design to be undertaken inside an authorised Content & Media JIT dossier.

This working Beacon dossier does not itself freeze Ash Resources or authorise implementation.

#### Draft-binding/membership is a scoped JIT gate, not a Template-closure blocker

Current authority requires working drafts/autosave and immutable/traceable Content Versions, but does not yet freeze the durable mutable-working-draft Resource model.

Therefore exact placement of:

```text
active ContentTemplateVersion
Template structural-slot membership
Template migration source-state guard
```

remains gated by the broader C&M mutable-draft ownership decision.

The Template branch must not invent a `ContentDraft` Resource merely to host Template state.

This gate does not invalidate `ContentTemplate` / `ContentTemplateVersion` Resource justification.

#### Template Approval evidence semantics — subsequently resolved by GRILL-26

At GRILL-19 closure, exact Template Version approval design remained a scoped JIT gate because applicable approvals had to remain separately recorded.

`GRILL-26` subsequently resolves the semantic authority: `ContentTemplateVersion` uses the same bounded C&M Approval semantics as other governed immutable C&M subjects, and Template maturity `DRAFT → APPROVED` is not itself Approval evidence.

Exact typed relationships/actions remain JIT. Current Template selectability still depends on `EXPOSED-01`.

#### EXPOSED-01 is a scoped approval/selectability compatibility gate

`GRILL-14` binds each Template identity to one governed Content Type.

Historical Template approval and current authoring selectability are distinct.

Before exact approval/selectability compatibility mechanics are frozen, JIT must establish a stable/version-addressable interpretation of the governing Content Type contract, or an equivalent explicit compatibility mechanism sufficient to answer:

- what Content Type semantics were validated when a Template Version was approved;
- whether those historical approval semantics remain interpretable;
- whether the exact Template Version remains eligible for new authoring now.

`EXPOSED-01` is therefore a hard subgraph/JIT gate, not a reason to continue Beacon Template reuse discovery.

#### Localisable INITIAL CONTENT is capability-gated

The Template scaffold may contain locale-neutral structural/default configuration.

Substantive/localisable Template `INITIAL CONTENT` remains unsupported until C&M translation/locale semantics determine how such values are governed.

Until then:

```text
locale-neutral structural/default values
→ may be designed

substantive localisable Template defaults
→ unsupported / fail closed
```

Template approval must never substitute for normal locale/content review and publication governance.

#### What may remain implementation/JIT detail after dependencies close

The following do not require another Beacon Template architecture GRILL:

- Ash embedded Resource versus typed struct/union choice;
- exact PostgreSQL constraints/index names;
- optimistic concurrency mechanism;
- transaction implementation;
- exact action names;
- migration-plan persistence versus ephemeral derivation;
- editor migration-conflict workflow;
- exact policy DSL syntax.

These remain downstream implementation decisions once their semantic owners/gates are resolved.

#### Correct stopping point

The Template branch now stops.

**Historical status at GRILL-19 acceptance:** the correct next broader seam was not another Template-specific implementation detail but the Content & Media mutable-authoring boundary, Block 3A.1.

`GRILL-20` subsequently resolves Block 3A.1; `GRILL-21` through `GRILL-23` then resolve the version-cut, shared/locale split and translation-lineage seams. Block 3A.5 was subsequently resolved by `GRILL-24`; Block 3A.6 was subsequently resolved by `GRILL-25`; Block 3A.7 was subsequently resolved by `GRILL-26`; Block 3A.8 was subsequently resolved by `GRILL-27`; Block 3A.9 was subsequently resolved by `GRILL-28`; Block 3A.10 was subsequently resolved by `GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

This broader seam is required before exact draft-binding/membership persistence can be frozen.

### 6.62 ACCEPTED GRILL DECISION

#### `GRILL-19 — Editorial Content Template Reuse Discovery Is Semantically Closed and Ready for Content & Media JIT Handoff`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> `GRILL-10` through `GRILL-18` provide sufficient Template-specific semantic closure for the Beacon reuse-discovery phase.
>
> The existence and responsibility of dedicated C&M-owned `ContentTemplate` and `ContentTemplateVersion` concepts are sufficiently justified for exact Resource design to be undertaken **inside the authorised Content & Media JIT dossier**. This working Beacon dossier does not itself authorise or freeze Ash Resources.
>
> No further Beacon-specific Template architecture GRILL is required before JIT. Additional Template-detail decisions made here would risk crossing from reuse discovery into speculative implementation design.
>
> The Content & Media JIT may rely on the accepted Template constraints without reopening them absent new evidence, contradiction or changed scope.
>
> Exact draft-binding, Template structural-slot membership and Template-migration persistence/actions remain gated by the broader C&M mutable-working-draft ownership model. The Template dossier must not invent a draft Resource merely to host Template state.
>
> Exact Template Version approval actions/evidence must compose with the platform requirement that applicable approvals remain separately recorded. A maturity marker may not silently replace required durable Approval evidence.
>
> Template approval/selectability compatibility remains gated by `EXPOSED-01`: JIT must establish a stable/version-addressable interpretation of the governing Content Type contract, or an equivalent explicit compatibility mechanism, before freezing how historical approval and current authoring eligibility are evaluated.
>
> Substantive/localisable Template `INITIAL CONTENT` remains capability-gated until C&M translation/locale semantics determine how such values are governed. Locale-neutral structural/default configuration may proceed independently; unsupported localisable defaults fail closed rather than forcing speculative multilingual Template storage.
>
> These are **JIT dependency gates**, not unresolved Beacon Template-reuse questions.
>
> Exact Ash representation choices such as embedded Resources, typed structures/unions, PostgreSQL constraints, optimistic concurrency, transaction mechanics and migration-plan persistence remain downstream implementation decisions once their owning semantic dependencies are resolved.
>
> The editorial Template branch of this Beacon reuse dossier is therefore **CLOSED / PASS for JIT handoff**, while executable implementation remains governed by the normal Feature Pack/JIT entry gates.

### 6.63 Consequences fixed for handoff

1. Beacon editorial Template reuse discovery is CLOSED / PASS.
2. No additional Template-specific GRILL is required before C&M JIT.
3. `ContentTemplate` Resource justification is sufficient for JIT design.
4. `ContentTemplateVersion` Resource justification is sufficient for JIT design.
5. The Beacon dossier does not freeze exact Ash schemas/actions.
6. Accepted `GRILL-10` through `GRILL-18` are handoff constraints for JIT.
7. At v0.20.0 exact draft-binding/membership persistence waited for mutable-working-draft ownership; `GRILL-20` now resolves that owner as dedicated subordinate `ContentDraft` authority.
8. The eventual `ContentDraft` is justified by broader durable C&M authoring requirements, not invented merely to host Template state.
9. Template Version approval maturity remains `DRAFT → APPROVED`.
10. Durable/separately recorded Approval evidence must not be replaced silently by maturity state.
11. `EXPOSED-01` remains a hard JIT gate for exact approval/selectability compatibility.
12. Substantive/localisable Template initial content remains capability-gated.
13. Locale-neutral Template structure/default configuration may proceed independently.
14. Unsupported localisable Template defaults fail closed.
15. Exact Ash representation/concurrency/transaction mechanics remain downstream implementation detail.
16. `GRILL-20` subsequently resolved Block 3A.1; `GRILL-21` then resolved Block 3A.2, `GRILL-22` resolved Block 3A.3, and `GRILL-23` resolved Block 3A.4. Block 3A.5 was subsequently resolved by `GRILL-24`; Block 3A.6 was subsequently resolved by `GRILL-25`; Block 3A.7 was subsequently resolved by `GRILL-26`; Block 3A.8 was subsequently resolved by `GRILL-27`; Block 3A.9 was subsequently resolved by `GRILL-28`; Block 3A.10 was subsequently resolved by `GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.64 Block 3A.1 pressure test — mutable working-draft authority versus immutable Content Version truth

Current NewYou authority requires all of the following simultaneously:

- substantial editors/forms use safe autosave and clear saved-state indication;
- autosave does not imply approval or publication;
- working drafts may evolve during editing;
- meaningful review/publication boundaries create immutable/versioned snapshots;
- every material edit creates a new immutable and traceable content version at governed version boundaries;
- published governed versions are immutable;
- material historical truth is preserved through immutable/versioned or superseding records rather than destructive overwrite.

These requirements make mutable authoring truth and immutable governed-version truth distinct authority classes.

#### Candidate model: mutate `ContentVersion` while it is “draft”

**REJECT.**

Using the same `ContentVersion` record as an autosaved mutable workspace would blur the boundary between:

```text
working mutable truth
```

and:

```text
immutable governed historical truth
```

It would also make approval/review provenance vulnerable to later mutation unless a second freeze mechanism recreated the distinction elsewhere.

#### Candidate model: store mutable draft composition directly on `ContentItem`

**REJECT.**

Current Product Law assigns the shared conceptual item stable identity/type/audience/risk/ownership/relationship semantics.

Mutable wording/composition, Template binding, slot membership and autosave revisions are different concerns and would contaminate the stable conceptual identity boundary.

Independent locale branches further weaken the case for putting mutable authored wording/composition directly on `ContentItem`.

#### Candidate model: browser / LiveView state only

**REJECT.**

A browser or LiveView process cannot be durable business authority for:

- safe autosave;
- crash/restart recovery;
- concurrent editing protection;
- exact Template Version binding;
- Template slot membership;
- draft-addressed review comments;
- governed snapshot creation.

Frontend state remains projection, not business truth.

#### Candidate model: immutable `ContentVersion` on every autosave

**REJECT.**

Current frontend authority explicitly distinguishes mutable autosave from meaningful immutable/versioned snapshot boundaries.

Creating a governed immutable version for every keystroke/autosave would produce version spam and conflate operational authoring revisions with business content versions.

#### Candidate model: event-source every authoring mutation

**REJECT initially.**

No current requirement justifies an event-sourced keystroke/autosave history as primary content authority.

Durable audit evidence may record significant actions where required, but that does not justify event sourcing the entire editor.

#### Accepted candidate: dedicated durable subordinate mutable authoring aggregate

A dedicated conceptual `ContentDraft` is justified by independent durable requirements rather than UI convenience.

It owns mutable working-authoring state such as:

- evolving composition;
- mutable authoring metadata that is not stable `ContentItem` identity;
- safe autosave state;
- authoring revision/concurrency state;
- exact active `ContentTemplateVersion` binding where applicable;
- deterministic Template structural-slot membership where applicable;
- exact source/base Content Version provenance where applicable;
- durable addressability for contextual draft work.

Exact Ash module/field representation remains JIT.

#### `ContentDraft` is not a second governed version lineage

Draft autosave/revision identity is operational authoring addressability and concurrency state.

It is not equivalent to a governed immutable `ContentVersion` identity or number.

Conceptually:

```text
ContentDraft revision 184
≠
ContentVersion V184
```

#### Snapshot boundary

A governed version boundary validates and snapshots one exact draft revision into a new immutable `ContentVersion`.

Conceptually:

```text
ContentDraft D @ revision 184
        ↓ validate + snapshot
ContentVersion V12
```

Later authoring mutations produce later draft revisions and cannot mutate V12.

The draft record is not “promoted” by changing its row type/status into a Content Version; mutable and immutable records retain different invariants.

#### Review / approval / publication target exact immutable truth

Formal approval and publication must reference exact immutable governed content rather than a moving draft.

A safe conceptual flow is:

```text
mutable ContentDraft
      ↓ governed version cut
immutable ContentVersion
      ↓ exact applicable approvals
approved exact version
      ↓
publication / schedule
```

Contextual editorial review comments may target the relevant draft or exact version where the experience contract permits, but approval truth must not become detached from the exact content that was approved.

#### Template authoring state now has a legitimate owner

The draft-level Template facts accepted in `GRILL-17` belong naturally to the mutable authoring aggregate:

```text
ContentDraft
  ├── composition
  ├── active exact ContentTemplateVersion
  └── Template structural-slot membership
```

At governed snapshot creation, immutable `ContentVersion` retains resolved content and accepted effective Template Version provenance, not live Template-slot authoring machinery.

#### Base/source version provenance

A draft derived from prior governed content retains the exact source/base `ContentVersion` it started from.

This is provenance and concurrency/reconciliation context, not dynamic inheritance.

The draft owns its current mutable truth.

#### Exact source revision guard

Snapshot creation must operate against one exact source draft revision or equivalent concurrency condition.

If the source draft changes after validation begins, the operation must fail/revalidate rather than create an immutable version from a stale or mixed authoring state.

Exact optimistic-lock/transaction implementation remains JIT.

#### One active mutable draft per governed authoring branch initially

NewYou does not initially introduce parallel Git-like editorial draft branches and merge semantics.

There is one active authoritative mutable working draft per governed authoring branch unless later evidence requires otherwise.

**Historical at GRILL-20 acceptance:** exact uniqueness scope across locale/translation branches remained deferred. `GRILL-24` subsequently introduced dedicated subordinate locale-draft authority, and `GRILL-25` fixed at most one active `ContentLocaleDraft` per exact `ContentVersion` + locale.

#### Draft lifecycle restraint

A Resource does not require a rich lifecycle merely because it exists.

No speculative `new / paused / cancelled / archived / abandoned` state machine is introduced here.

Exact abandonment, retention and cleanup semantics remain JIT and must follow audit/retention requirements.

#### Remaining version-cut ambiguity

This decision deliberately does not decide exactly which event creates a new immutable `ContentVersion`.

Current authority gives both:

```text
working drafts evolve with autosave
```

and:

```text
material edits create immutable/traceable content versions
meaningful review/publication boundaries create immutable/versioned snapshots
```

The exact reconciliation belongs to Block 3A.2.

Autosave itself is not sufficient to imply a governed version cut.

#### Translation boundary — historical at GRILL-20 acceptance; subsequently resolved

Current Product Law conceptually defines:

```text
ContentItem
→ ContentVersion
→ ContentTranslationVersion
```

and locale branches advance independently.

Therefore this decision establishes `ContentDraft` as the mutable authoring aggregate/root without yet freezing exact locale-specific subordinate draft representation.

The shared-versus-locale authority split is subsequently resolved by `GRILL-22`; exact Translation Resource persistence remains a separate JIT/OQ-013 seam.

#### Beacon reuse classification

Beacon's separation between mutable Page editing state and publication snapshots is useful evidence for the authority split.

NewYou adapts that separation concept but rejects Beacon's Ecto Page/PageSnapshot business model as direct authority.

```text
Beacon mutable Page ↔ snapshot separation
→ ADAPT conceptually

Beacon Page / serialised PageSnapshot persistence
→ REJECT as direct NewYou authority
```

### 6.65 ACCEPTED GRILL DECISION

#### `GRILL-20 — Mutable Content Authoring Uses Dedicated Durable ContentDraft Authority Separate from Immutable ContentVersion Truth`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou Content & Media distinguishes mutable working-authoring truth from immutable governed content-version truth.
>
> A dedicated subordinate `ContentDraft` authoring aggregate is justified by durable requirements including safe autosave, concurrent editing protection, Template Version pinning, Template structural-slot membership, draft/version review addressability and exact snapshot creation. It is not introduced merely because an editor UI exists.
>
> `ContentDraft` is mutable authoritative **working state**, not a governed historical `ContentVersion`, publication unit or second immutable version lineage.
>
> `ContentItem` remains stable conceptual content identity/type/audience/risk/ownership/relationship authority and does not absorb mutable draft composition merely to avoid a draft Resource.
>
> `ContentVersion` is not used as the mutable autosave workspace. Mutable authoring does not destructively alter an existing immutable governed Content Version.
>
> Draft autosave/revision identity is operational authoring concurrency/addressability and is distinct from governed Content Version numbering/identity.
>
> A governed version boundary creates a new immutable `ContentVersion` by validating and snapshotting one exact `ContentDraft` revision. Later draft edits cannot modify that previously created Content Version.
>
> Formal approval and publication apply to exact immutable governed versions, not to a moving working draft. Review comments may remain contextually linked to either the relevant draft or exact version as permitted by frontend law.
>
> Publication and scheduled publication never dereference “the current draft”; they act on an exact approved immutable version.
>
> Template-governed authoring state accepted in `GRILL-17`—the active exact `ContentTemplateVersion` binding and deterministic Template structural-slot membership—belongs to the mutable draft authoring boundary. Immutable Content Versions retain resolved content plus effective Template Version provenance, not live Template-slot authoring machinery.
>
> A draft derived from existing governed content retains exact source/base Content Version provenance, but does not dynamically inherit mutable truth from that version.
>
> Snapshot creation must bind to an exact source draft revision or equivalent concurrency condition so a governed Content Version cannot accidentally capture a stale or mixed authoring state. Exact Ash/PostgreSQL concurrency implementation remains JIT.
>
> NewYou initially permits only one active authoritative mutable working draft per governed authoring branch. Parallel mutable editorial branches and merge semantics are not introduced without evidence.
>
> **Historical at GRILL-20 acceptance:** exact locale/translation uniqueness and child-Resource shape remained deferred. `GRILL-24` subsequently justified subordinate `ContentLocaleDraft` and `TranslationWork` concepts, and `GRILL-25` fixed the initial active-locale-draft uniqueness invariant.
>
> `ContentDraft` does not initially receive a rich independent business lifecycle merely because it is a Resource. Exact abandonment/retention mechanics remain JIT.
>
> **Historical status at GRILL-20 acceptance:** the exact trigger constituting a governed **Content Version cut** was unresolved and became the next seam; autosave itself was already excluded as sufficient cause. **Subsequently resolved by GRILL-21:** the governed version cut occurs at the first exact-content governance boundary, normally formal review submission and otherwise before approval, scheduling or publication.
>
> Beacon's separation between mutable page state and snapshots is **ADAPTED conceptually**, while Beacon `Page` / `PageSnapshot` persistence and runtime authority are **REJECTED as the direct NewYou model**.

### 6.66 Consequences fixed for later grills

1. A dedicated conceptual `ContentDraft` is now justified as C&M-owned durable mutable authoring authority.
2. `ContentDraft` is subordinate working truth, not a second governed historical version lineage.
3. `ContentItem` does not own mutable draft composition.
4. `ContentVersion` is not the mutable autosave workspace.
5. Browser/LiveView state cannot be durable draft authority.
6. Autosave revisions are distinct from governed Content Version identity.
7. Governed version creation snapshots one exact draft revision into a new immutable Content Version.
8. Later draft changes cannot mutate an already-created Content Version.
9. Formal approval/publication targets exact immutable versions, not moving drafts.
10. Template Version binding and Template slot membership belong to the mutable draft boundary.
11. Immutable Content Versions retain resolved content plus effective Template Version provenance, not live Template membership state.
12. Successor/correction drafts retain exact source/base Content Version provenance where applicable.
13. Snapshot creation requires an exact source draft revision/concurrency condition.
14. Only one active authoritative mutable draft per governed authoring branch is supported initially.
15. **Historical at GRILL-20 acceptance:** locale/translation uniqueness scope was deferred; `GRILL-24`/`GRILL-25` subsequently resolved the semantic Resource/active-uniqueness boundary.
16. No speculative rich `ContentDraft` lifecycle is introduced.
17. Exact draft abandonment/retention mechanics remain JIT.
18. **Historical at GRILL-20 acceptance:** exact Content Version-cut semantics remained unresolved; `GRILL-21` subsequently resolved that boundary.
19. Autosave alone is not a governed version cut.
20. `GRILL-21` subsequently resolved Block 3A.2; `GRILL-22` then resolved Block 3A.3 and `GRILL-23` resolved Block 3A.4. Block 3A.5 was subsequently resolved by `GRILL-24`; Block 3A.6 was subsequently resolved by `GRILL-25`; Block 3A.7 was subsequently resolved by `GRILL-26`; Block 3A.8 was subsequently resolved by `GRILL-27`; Block 3A.9 was subsequently resolved by `GRILL-28`; Block 3A.10 was subsequently resolved by `GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.67 Block 3A.2 pressure test — exact Content Version cut and lifecycle placement

Current NewYou authority requires all of the following:

- `DEC-135`: every material edit creates a new immutable and traceable content version;
- working drafts may evolve through safe autosave;
- autosave does not imply approval or publication;
- meaningful review/publication boundaries create immutable/versioned snapshots;
- approvals are separately recorded;
- scheduled publication revalidates approval/current policy;
- published governed versions are immutable;
- corrections supersede/withdraw rather than rewrite published truth;
- the Domain Map summarises the aggregate content lifecycle as `draft / machine-draft / review / approved / published → superseded / withdrawn`.

The architecture must reconcile these statements without creating immutable versions for every keystroke and without turning one mutable `ContentVersion.status` field into authority for several independent business facts.

#### Version cut at the first exact-content governance boundary

The governing rule is:

> A new immutable governed `ContentVersion` is cut when mutable authored content must become an exact, independently addressable governance subject.

Normally that boundary is formal review submission.

Where formal review is legitimately absent under policy, an immutable version must still exist before approval, scheduling or publication.

Ordinary authoring remains mutable:

```text
ContentDraft rev 41
→ autosave
ContentDraft rev 42
→ autosave
ContentDraft rev 43
```

Then:

```text
ContentDraft @ exact rev 43
        ↓ validate / governed version cut
ContentVersion V7
        ↓
formal review / approval / publication facts reference V7
```

Autosave itself is not a governed version cut.

#### DEC-135 interpretation

`DEC-135` does not require one immutable version for every draft mutation.

Instead:

> A material edit is never applied to an existing governed Content Version. It is authored in mutable draft truth and must become a successor immutable version before those changed semantics can become reviewed, approved, scheduled or published governed truth.

This preserves both durable working authoring and immutable historical content truth.

#### `draft` / `machine_draft` stay on the mutable-authoring side

`draft` and `machine_draft` describe mutable authoring state/origin.

They do not make an immutable `ContentVersion` mutable.

Exact Ash representation of those authoring distinctions remains JIT.

#### Formal review operates on an immutable candidate

Formal review requires exact stable content.

Conceptually:

```text
ContentDraft rev 43
        ↓ submit for formal review
ContentVersion V7
        ↓
review V7
```

Later autosaves to the draft cannot alter V7.

If review requests changes, those changes happen in mutable draft truth and a successor immutable version is cut before renewed formal review:

```text
V7
→ changes requested

ContentDraft
→ rev 51
→ governed cut
→ V8
→ renewed review
```

V7 remains immutable evidence of what was actually reviewed.

#### Approval does not create a duplicate content version

If V8 passes review and no content changes:

```text
V8
→ Approval evidence
```

Approval is evidence about V8.

No V9 is created merely because approval occurred.

This preserves the platform rule that approvals remain separately recorded and prevents approval state from becoming content identity.

#### Publication does not create a duplicate content version

Likewise:

```text
V8
→ approved
→ scheduled
→ published
```

remains V8 when content is unchanged.

Publication establishes separate publication truth about that exact immutable version.

A publication schedule therefore references the exact approved immutable version and never dereferences “whatever the draft contains at execution time”.

#### Aggregate lifecycle, not one overloaded enum

The Domain-Law lifecycle:

```text
draft / machine-draft / review / approved / published
→ superseded / withdrawn
```

is interpreted as the aggregate governed-content lifecycle across multiple authoritative concepts.

It does not require one `ContentVersion.status` field to own every phase.

Semantically:

```text
draft / machine_draft
→ ContentDraft authoring truth

review
→ governed workflow against exact immutable ContentVersion

approved
→ separately recorded Approval evidence for exact version

published / scheduled
→ Publication truth referencing exact version

superseded
→ effective version/publication lineage consequence

withdrawn
→ Correction / Withdrawal truth
```

A derived lifecycle label may later be projected for operator UX, but it cannot become competing authority.

#### Independent state dimensions are required

A version may be:

- reviewed but never approved;
- approved but not published;
- approved and scheduled;
- published and later withdrawn;
- historical and superseded.

Those are not safely representable as one mutually exclusive lifecycle dimension without losing information or creating artificial transitions.

#### Review rejection / changes requested

A rejected or changes-requested immutable review candidate is not edited in place.

Revisions occur through `ContentDraft`, then a new immutable successor candidate is created before renewed governed review.

Exact retention policy for unsuccessful historical candidates remains JIT/audit policy, but they must not be overwritten while required evidence.

#### Editing after approval

Editing after approval does not mutate the approved version and does not retroactively erase the fact that the old version was approved.

Instead:

```text
V8 approved

ContentDraft based on V8
→ changed
→ future V9
```

V9 does not inherit V8's approval.

Applicable approval evidence must be established for V9 independently.

#### Editing while an approved version is scheduled

A publication schedule remains pinned to its exact approved version.

Later draft changes or creation of V9 do not silently redirect the schedule.

Switching a schedule to a successor version requires an explicit governed schedule change after that successor satisfies applicable approval policy.

#### Corrections after publication

Published content is not edited in place.

A changed delivered-content meaning becomes replacement immutable version truth.

A controlled minor correction may use a lighter governance path, but it does not destroy traceability of the original published version.

Conceptually:

```text
V8 published
   ↓ correction authoring
ContentDraft
   ↓ governed cut
V9
   ↓ applicable correction governance
publish V9
```

For urgent safety/legal correction, V8 may be withdrawn before V9 is ready.

Withdrawal and replacement are independent governed actions.

#### Successor lineage versus effective supersession

Creating V9 as a candidate does not by itself supersede currently effective V8.

The system must distinguish:

```text
derived_from / predecessor lineage
```

from:

```text
effective supersession
```

Normally effective supersession occurs when the successor becomes replacement publication truth.

A separate withdrawal can remove the earlier version first when policy requires.

#### Low-risk/direct flows

Where policy permits a direct/self-approved low-risk flow, the UX may compress:

```text
snapshot
→ permitted approval
→ publication
```

into one coherent higher-level operation.

The semantic boundaries remain: an exact immutable version exists before approval/publication authority is established.

#### No speculative manual governed-version checkpoints

No generic “save governed version” action is introduced initially.

Ordinary authoring checkpoints remain draft-level concerns unless a later collaboration/audit requirement justifies additional governed snapshot types.

#### Translation boundary — historical at GRILL-21 acceptance; subsequently resolved

Current Product Law conceptually defines:

```text
ContentItem
→ ContentVersion
→ ContentTranslationVersion
```

and locale branches advance independently.

Therefore these version-cut semantics apply to the relevant exact governed content/locale snapshot, but this decision does not yet decide which exact payload/state belongs to `ContentVersion` versus `ContentTranslationVersion`.

That payload/authority split was subsequently resolved by `GRILL-22`; `GRILL-23` subsequently resolved translation lineage, staleness and safe carry-forward semantics.

#### Beacon reuse classification

Beacon's mutable-state-to-snapshot separation remains useful.

Beacon's simple `created / published / unpublished` PageEvent model does not capture NewYou's independent review, approval, publication, correction, withdrawal, locale and supersession authorities.

Therefore:

```text
Beacon mutable state → snapshot boundary
→ ADAPT conceptually

Beacon PageEvent lifecycle
→ REFERENCE ONLY

Beacon Page/PageSnapshot/PageEvent as direct NewYou authority
→ REJECT
```

### 6.68 ACCEPTED GRILL DECISION

#### `GRILL-21 — Immutable Content Versions Are Cut at Exact Governance Boundaries; Approval, Publication and Correction Remain Separate Authorities`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou mutable authoring remains in `ContentDraft`. Draft autosaves, previews and ordinary editing do not independently create governed `ContentVersion` records.
>
> A new immutable governed `ContentVersion` is created when the exact authored content must cross from mutable working truth into an independently addressable governance boundary, normally formal review submission and, where formal review is legitimately absent, before approval, scheduling or publication.
>
> This reconciles `DEC-135` with safe autosave: material changes are never applied to an existing governed Content Version. They are authored in mutable draft truth and must become a new immutable version before those changed semantics can become reviewed, approved, scheduled or published governed truth.
>
> `draft` and `machine_draft` describe mutable authoring state/origin and belong to the `ContentDraft` side of the boundary rather than making `ContentVersion` mutable.
>
> Formal review operates against an exact immutable Content Version snapshot. Later draft edits do not alter the reviewed version. Changes requested during review are made in mutable draft truth and require a successor immutable version before renewed formal review/approval.
>
> Approval does not create a new Content Version when content is unchanged. Applicable separately recorded Approval evidence references the exact immutable version being approved.
>
> Publication and scheduled publication likewise reference an exact approved immutable version and do not create a new Content Version merely because publication occurs.
>
> The Domain-Law lifecycle `draft / machine-draft / review / approved / published → superseded / withdrawn` is an aggregate governed-content lifecycle across authoritative concepts, not a mandate for one mutable `ContentVersion.status` field.
>
> Review workflow state, Approval evidence, Publication truth and Correction/Withdrawal truth remain semantically distinct dimensions around an immutable version. A derived lifecycle label may be projected for operator UX but must not become a competing authority.
>
> A rejected or changes-requested immutable review candidate is not edited in place. Revised content is authored through `ContentDraft` and cut as a successor immutable version before renewed governed review.
>
> Approval of one version does not transfer to a later changed version. A successor immutable version must establish its own applicable approval evidence.
>
> A publication schedule remains pinned to the exact approved version originally scheduled and does not silently follow subsequent draft edits or newly created versions.
>
> Published Content Versions are never edited in place. Any delivered-content change, including a controlled minor correction, produces replacement immutable version truth; the correction class may alter required workflow intensity but does not destroy traceability of the original published version.
>
> Creating a successor candidate does not itself supersede the currently effective published version. Effective supersession occurs only when the successor becomes replacement publication truth, unless the earlier version is separately withdrawn first under a governed correction/withdrawal action.
>
> Direct/self-approved low-risk flows may compress snapshot, permitted approval and publication into one coherent user operation, but an exact immutable version must still exist before approval/publication authority is established.
>
> No generic manual “save governed version” mechanism is introduced without a demonstrated workflow need. Non-governed authoring checkpoints remain draft-level concerns.
>
> Version predecessor/derivation lineage is distinct from effective supersession.
>
> **Historical status at GRILL-21 acceptance:** exact allocation between `ContentVersion` and `ContentTranslationVersion` remained deferred. **Subsequently resolved semantically by GRILL-22:** `ContentVersion` owns shared language-neutral composition/invariant truth and `ContentTranslationVersion` owns one locale's localisable governed truth; exact Ash persistence remains JIT/OQ-013.
>
> Beacon's mutable-state-to-snapshot boundary is **ADAPTED conceptually**. Beacon's simple PageEvent lifecycle remains **REFERENCE ONLY / REJECTED as NewYou lifecycle authority**.

### 6.69 Consequences fixed for later grills

1. Autosave, preview and ordinary editing remain `ContentDraft` concerns.
2. A governed immutable version is cut at the first exact-content governance boundary.
3. Formal review submission normally causes that cut.
4. Where formal review is legitimately absent, an immutable version must still exist before approval, scheduling or publication.
5. `DEC-135` prohibits applying material changes to an existing governed version; it does not require version-per-keystroke.
6. `draft` / `machine_draft` remain on the mutable-authoring side.
7. Formal review targets exact immutable version truth.
8. Changes requested during review produce later draft edits and a successor immutable candidate.
9. Approval evidence attaches to the exact immutable version and does not create a duplicate version.
10. Publication/scheduling attach to the exact immutable version and do not create duplicate versions.
11. The Domain-Map lifecycle is aggregate across authoritative concepts, not a single `ContentVersion.status` contract.
12. Review, Approval, Publication and Correction/Withdrawal remain independent state/evidence dimensions.
13. Approval never transfers automatically to a changed successor version.
14. Publication schedules never silently follow draft edits or newer versions.
15. Published content is never edited in place.
16. Minor corrections may use lighter governance but still preserve original published-version traceability.
17. Candidate predecessor lineage is distinct from effective supersession.
18. Effective supersession normally occurs when successor publication becomes replacement truth.
19. Governed withdrawal may precede replacement where policy requires.
20. Low-risk/direct UX may compress several operations but not collapse the semantic boundaries.
21. No speculative generic “save governed version” action is introduced.
22. Exact `ContentVersion` versus `ContentTranslationVersion` payload/authority allocation was subsequently resolved by `GRILL-22` at semantic level.
23. **Historical after GRILL-22:** Block 3A.4 became the next broader seam; `GRILL-23` subsequently resolves translation lineage/staleness/carry-forward semantics. Block 3A.5 was subsequently resolved by `GRILL-24`; Block 3A.6 was subsequently resolved by `GRILL-25`; Block 3A.7 was subsequently resolved by `GRILL-26`; Block 3A.8 was subsequently resolved by `GRILL-27`; Block 3A.9 was subsequently resolved by `GRILL-28`; Block 3A.10 was subsequently resolved by `GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.70 Block 3A.3 pressure test — shared Content Version versus independently governed locale versions

Current NewYou authority provides a strong conceptual hierarchy:

```text
ContentItem
→ ContentVersion
→ ContentTranslationVersion
```

The shared item owns conceptual identity/type/audience/risk/ownership/relationships.

Each language version owns locale, wording, version, lifecycle state, reviewers, approvals and publication date.

Locale branches advance independently.

The architecture therefore must preserve one content/version lineage without creating competing locale-specific composition authorities.

#### Accepted ownership split

`ContentVersion` owns one immutable language-neutral governed composition.

That includes:

- ordered BlockOccurrence structure;
- shared occurrence identity;
- exact `block_type`;
- exact `schema_version`;
- locale-invariant payload/configuration values;
- resolved Template structure/provenance where applicable;
- other shared governed values whose business meaning does not vary by locale.

A `ContentTranslationVersion` owns one locale's immutable localisable values against exactly one shared `ContentVersion`, together with the locale-specific lifecycle/review/approval/publication provenance required by Product/Architecture law.

Conceptually:

```text
ContentVersion C7
  ├── shared structure / occurrence identity / invariant values
  ├── EN locale version(s)
  └── AF locale version(s)
```

#### GRILL-03 refinement, not reversal

`GRILL-03` remains valid:

> Ordinary block occurrences are structured part of the owning Content Version.

`GRILL-22` refines that statement:

```text
BlockOccurrence structure / identity / invariant values
→ ContentVersion

localisable values for those occurrences
→ ContentTranslationVersion
```

The common block architecture is not duplicated per locale.

#### Block contracts classify invariant versus localisable values

Each code-authoritative block contract must make explicit which governed values are:

```text
locale-invariant
```

and which are:

```text
localisable
```

For example, conceptually:

```text
callout/v2

shared:
  severity
  icon/media reference
  presentation variant

localisable:
  heading
  body
  action label
```

Exact Ash representation remains deferred.

NewYou does not use an untyped arbitrary “translation overrides” bag as a substitute for block-contract semantics.

Unknown or unsupported localisation semantics fail closed.

#### Shared occurrence key provides locale addressability

Stable `occurrence_key` values in the shared Content Version provide deterministic addressability for locale-specific values.

Conceptually:

```text
ContentVersion C7:
  hero-1
  paragraph-4
  cta-2

EN locale version:
  hero-1.heading
  paragraph-4.body
  cta-2.label

AF locale version:
  hero-1.heading
  paragraph-4.body
  cta-2.label
```

Locale versions do not mint a second independent occurrence identity merely to hold translated wording.

#### No locale-specific structural divergence initially

All locale variants of one shared `ContentVersion` initially use the same:

- occurrence set;
- occurrence order;
- `block_type`;
- `schema_version`;
- locale-invariant values.

A locale version may not independently add/remove/reorder an occurrence or change the block contract/schema.

Such changes are shared composition changes and require a successor `ContentVersion`.

A genuine later requirement for structurally different locale variants requires a separate architecture pressure test.

#### Wording-only changes remain locale-version changes

If shared structure C7 does not change but Afrikaans wording changes:

```text
C7 / AF4
→
C7 / AF5
```

No successor shared Content Version is created solely because localisable wording changed.

`DEC-135` therefore applies at the relevant immutable authority layer:

```text
shared/invariant material change
→ new ContentVersion

locale-localisable material change
→ new ContentTranslationVersion for that locale
```

No governed immutable record is edited in place.

#### Shared structural change creates a successor Content Version

If structure/order/contract/schema or another locale-invariant governed value changes:

```text
C7
→
C8
```

Existing locale versions remain immutable historical variants of C7.

They are never silently rebound to C8.

C8 must establish locale-version truth explicitly before locale-specific review/approval/publication requirements can be satisfied.

#### Carry-forward into a new shared version is draft material only

Where stable occurrence keys/contracts permit deterministic correspondence, later JIT tooling may seed a new locale draft for C8 from compatible locale values under C7.

That carry-forward:

- creates/updates mutable draft material only;
- never mutates prior locale versions;
- never transfers approval/publication authority;
- requires renewed applicable governance against C8.

Exact carry-forward/staleness semantics remain Block 3A.4.

#### Required bilingual alignment becomes exact

Where policy requires approved bilingual variants, the required locale versions must belong to the same exact shared `ContentVersion`.

This does not satisfy bilingual alignment:

```text
EN approved against C8
AF approved against C7
```

This does:

```text
C8
  ├── approved EN locale version
  └── approved AF locale version
```

This prevents a newer structure from being delivered with an older translation that does not correspond to it.

#### Locale branches still advance independently

Sharing one structural Content Version does not mean locale workflows move in lockstep.

For the same C8:

```text
EN
→ review → approved → published

AF
→ machine draft → language review → approved
```

Delivery eligibility then follows the applicable bilingual/fallback/risk policy.

Shared structure and independent locale governance are distinct dimensions.

#### Publication resolves an exact pair

Architecture Law distinguishes latest, approved and published locale/version state.

Therefore delivery/publication must resolve an exact immutable pair:

```text
ContentVersion C8
+
ContentTranslationVersion AF6 belonging to C8
```

Runtime must not load C8 and dynamically combine it with “whatever Afrikaans version is latest”.

Exact persisted Publication relationships remain JIT.

#### Translation source provenance is more specific than the shared parent

Every locale version belongs to one exact shared `ContentVersion`.

Where a target locale is produced through translation from another locale, its translation provenance must additionally identify the exact source locale version whose wording was translated.

Conceptually:

```text
C8
  ├── EN4
  └── AF draft/version
        translated_from = EN4
```

This satisfies the requirement that translation work records its source version.

No permanent English-as-canonical rule is introduced; source locale/version is contextual to the translation operation.

#### Two different stale/mismatch conditions

A target translation can be stale because its exact source locale version has been superseded by newer wording while the shared Content Version remains the same.

That is:

```text
source-wording staleness
```

A different condition exists when shared structure changes:

```text
C8 → C9
```

A locale version attached to C8 remains valid historical C8 truth but cannot be treated as a C9 locale variant.

That is:

```text
shared-version mismatch
```

These conditions must not be collapsed.

Exact staleness/carry-forward rules are Block 3A.4.

#### Locale-varying metadata follows locale authority

Where business meaning varies by locale, the value belongs to the locale-governed layer.

Examples may include:

- title;
- slug;
- meta title;
- meta description;
- human-facing labels/copy.

Genuinely shared business truth remains at the shared Content Version / Content Item boundary according to its ownership semantics.

Exact field placement remains content-type/JIT detail.

#### ContentDraft now has shared and locale authoring dimensions

`GRILL-20` remains the mutable authoring root.

Conceptually it now contains:

```text
ContentDraft
  ├── shared mutable authoring state
  │     structure / order / occurrence identity
  │     locale-invariant values
  │     Template binding/membership
  │
  ├── EN locale authoring branch
  │     localisable values / translation work
  │
  └── AF locale authoring branch
        localisable values / translation work
```

This does not yet introduce a `ContentLocaleDraft` Resource.

Exact translation/draft persistence remains JIT/OQ-013.

#### Concurrency implication

Shared structural edits affect every locale branch.

A pure locale wording edit does not need to mutate another locale's wording.

Later JIT concurrency therefore needs to distinguish shared authoring revisions from locale-specific authoring revisions or provide an equivalent correctness mechanism.

Exact locks/revision counters are deferred.

The invariant is that any immutable locale snapshot must reference the exact shared Content Version/structure it governs.

#### Template initial content boundary

Template structure and locale-neutral defaults materialise into shared draft state.

Substantive localisable Template defaults, if supported later, belong to locale-specific mutable authoring state.

They never imply locale review/approval.

`GRILL-19`'s capability gate remains: substantive localisable Template defaults stay unsupported until their governed locale-source semantics are explicitly designed.

#### Rendering/delivery boundary

Rendering/delivery combines:

```text
exact immutable ContentVersion
+
exact immutable selected ContentTranslationVersion
+
code-authoritative block contract
```

It does not use mutable drafts or “current/latest” translation inheritance.

#### Beacon

Beacon provides no direct donor for NewYou's translation/version authority split.

NewYou's exact source-version provenance, independent locale lifecycle, bilingual gating, language review and immutable locale publication requirements are materially stronger than Beacon's generic page/variant mechanisms.

Therefore:

```text
Beacon translation/version donor
→ NONE

NewYou model
→ REIMPLEMENT from NewYou law
```

### 6.71 ACCEPTED GRILL DECISION

#### `GRILL-22 — ContentVersion Owns Shared Language-Neutral Composition; Locale Versions Own Independently Governed Localisable Content Against That Exact Structure`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou's conceptual `ContentItem → ContentVersion → ContentTranslationVersion` model is interpreted as one shared governed structural version with independently governed locale versions.
>
> `ContentVersion` owns language-neutral governed composition: ordered BlockOccurrence structure, occurrence identity, exact block contracts/schema versions, Template-derived resolved structure/provenance and other values whose business meaning is invariant across locales.
>
> A locale `ContentTranslationVersion` owns the exact localisable values for one locale against exactly one `ContentVersion`, together with that locale version's independent lifecycle/review/approval/publication provenance as required by current Product/Architecture law.
>
> Block contracts must define which governed values are locale-invariant versus localisable. The exact Ash representation is deferred; NewYou does not use arbitrary untyped translation override bags.
>
> Stable `occurrence_key` values from the shared `ContentVersion` provide deterministic addressability for locale-specific values. Locale versions do not create an independent duplicate BlockOccurrence tree merely to hold translations.
>
> All locale variants of one `ContentVersion` initially share the same occurrence structure, ordering, `block_type`, `schema_version` and locale-invariant values. A locale may not independently add, remove, reorder or change the contract of BlockOccurrences.
>
> A genuine future requirement for locale-specific structural divergence requires a separate architecture pressure test; it is not introduced speculatively.
>
> A material change to shared structure or another locale-invariant governed value creates a successor `ContentVersion`. Existing locale versions remain immutable historical variants of their original Content Version and are never silently rebound to the successor.
>
> A material change limited to one locale's localisable content creates a successor locale/translation version for that locale under the same shared `ContentVersion`; it does not create a new shared Content Version solely because wording changed.
>
> Compatible locale values from an earlier shared Content Version may later be copied into draft authoring for a successor shared version using deterministic occurrence/contract correspondence, but copied values are draft material and do not inherit approval/publication authority.
>
> Where policy requires bilingual or multi-locale approved variants, the required approved locale versions must belong to the same exact shared `ContentVersion`. An approved locale version for an older shared structure cannot satisfy the requirement for a newer Content Version.
>
> Locale branches advance independently in workflow state. Sharing one structural Content Version does not imply lockstep locale review, approval or publication.
>
> Publication/delivery resolves an exact locale version belonging to an exact shared Content Version. Runtime must not dynamically combine a shared version with whatever translation is merely “latest”.
>
> Every locale version references its exact shared `ContentVersion`. Where a locale artifact is produced through translation from another locale, its translation provenance additionally identifies the exact source locale version; no permanent English-as-canonical assumption is introduced.
>
> Translation staleness is derivable from exact source-version provenance. A target translation based on an older source locale version can be stale relative to a newer intended source version without mutating or falsifying its historical provenance.
>
> A change to the shared `ContentVersion` is distinct from source-wording staleness: locale versions attached to the predecessor remain historical truth for that predecessor but cannot be treated as locale variants of the successor shared Content Version.
>
> Locale-varying public metadata such as human-facing wording and locale-specific URLs belongs to the locale-governed layer; genuinely locale-invariant business truth remains shared. Exact field allocation remains JIT/content-type-specific.
>
> `ContentDraft` is refined semantically as one mutable authoring aggregate containing shared authoring state plus independently evolving locale-authoring branches. This decision does not yet introduce a `ContentLocaleDraft` Resource or otherwise resolve OQ-013's exact translation Resource design.
>
> Template structure and locale-neutral defaults materialise into shared draft state. Substantive localisable Template defaults, if later supported, must populate locale-specific authoring truth and cannot imply locale approval. Their exact governed storage remains capability-gated.
>
> Renderer/delivery logic combines an exact immutable shared Content Version with an exact immutable approved/published locale version through the code-authoritative block contract; neither side dynamically inherits from “current/latest” mutable state.
>
> Beacon provides **NO DIRECT DONOR** for this translation/version authority model.

### 6.72 Consequences fixed for later grills

1. `ContentVersion` owns one shared language-neutral governed composition.
2. `ContentTranslationVersion` owns one locale's localisable governed values against one exact shared Content Version.
3. `GRILL-03` remains valid for shared composition and is refined rather than reversed.
4. Block contracts classify locale-invariant versus localisable governed values.
5. Arbitrary untyped translation-override bags are not the default model.
6. Shared `occurrence_key` values address locale-specific values deterministically.
7. Locale versions do not create duplicate independent BlockOccurrence trees.
8. Locale-specific add/remove/reorder/contract changes are unsupported initially.
9. Shared structural/invariant material change creates a successor `ContentVersion`.
10. Locale-only wording change creates a successor locale/translation version under the same Content Version.
11. Historical locale versions are never silently rebound to a successor shared Content Version.
12. Carry-forward into a successor shared version is draft material and does not inherit approval/publication authority.
13. Required bilingual locale variants must align to the same exact shared Content Version.
14. Locale workflows remain independent even when structure is shared.
15. Publication/delivery resolves an exact shared-version + locale-version pair.
16. Runtime does not combine a shared version with merely “latest” translation.
17. Translation provenance may additionally reference the exact source locale version.
18. No permanent English-as-canonical source rule is introduced.
19. Source-wording staleness is distinct from shared-version mismatch.
20. Locale-varying metadata belongs to locale authority where business meaning varies by locale.
21. `ContentDraft` has conceptual shared and locale authoring dimensions.
22. No `ContentLocaleDraft` Resource is introduced by this decision.
23. Shared structural edits and pure locale edits have distinct concurrency implications.
24. Template locale-neutral defaults belong to shared draft state.
25. Substantive localisable Template defaults belong to locale authoring state if/when supported and never imply approval.
26. Beacon supplies no direct donor for this translation/version model.
27. Block 3A.4 was subsequently resolved by `GRILL-23`; Blocks 3A.5–3A.10 were subsequently resolved by `GRILL-24`–`GRILL-29`, and Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.73 Block 3A.4 pressure test — translation lineage, staleness and safe carry-forward

Current NewYou authority requires translation work to:

- record an exact source version;
- create draft material only when machine-assisted;
- become stale when the source changes;
- preserve independent locale lifecycle/governance;
- retain immutable references to delivered translation versions;
- distinguish latest, approved and published state;
- preserve exact content/locale provenance in governed delivery.

These requirements imply that translation staleness cannot be implemented by mutating immutable historical translation truth.

#### Staleness is derived current alignment, not historical mutation

Suppose:

```text
ContentVersion C8

EN4
  ↓ translated/reconciled into
AF6
```

and later editorial intent advances to:

```text
EN5
```

AF6 remains immutable historical truth:

```text
AF6 translated/reconciled against EN4
AF6 may have been approved
AF6 may have been published
```

Those facts remain true.

What changes is the current alignment relationship:

```text
AF6 source provenance = EN4
current designated translation source = EN5
→ AF6 is not current-aligned to EN5
```

Therefore:

> `stale` is a derived relationship between exact source provenance and current translation/release intent, not a destructive lifecycle state on immutable `ContentTranslationVersion`.

#### Do not compare against merely “latest”

Architecture Law distinguishes latest, approved and published.

Therefore NewYou does not define staleness as:

```text
target.source_version != latest(source locale)
```

A newer source candidate may exist but may never become the intended source of target translation/release work.

Staleness is evaluated against the exact source locale version explicitly designated for the relevant translation/release intent.

Exact persistence of that designation remains JIT.

#### Open translation work never silently retargets

If an Afrikaans draft/work item is based on EN4 and the intended source moves to EN5, the system does not silently rewrite:

```text
source = EN4
→
source = EN5
```

That would falsify provenance.

Instead existing work is recognised as stale relative to EN5 until explicit reconciliation/rebase/successor work establishes newer source provenance.

Exact work/assignment Resource mechanics remain deferred.

#### Same shared ContentVersion enables deterministic field diff

Where source locale versions EN4 and EN5 both belong to the same shared ContentVersion C8, `GRILL-22` guarantees:

- same occurrence structure;
- same occurrence keys;
- same block contracts;
- code-defined localisable field identities.

Therefore source changes may be compared deterministically by:

```text
occurrence_key
+
localisable field identity
```

#### Unchanged source field → target draft value may carry forward

Where an exact source localisable field is unchanged between source versions:

```text
same ContentVersion
same occurrence
same localisable field
same source value
```

the corresponding target draft value may be retained/carried forward automatically as draft authoring material.

This reduces needless retranslation without changing governance authority.

#### Changed source field → explicit reconciliation

Where the source localisable value changed, the existing target value cannot automatically be considered current.

The system does not infer semantic equivalence from:

- unchanged target text;
- string similarity;
- same block type;
- same field name;
- machine/LLM judgement.

Explicit translation/reconciliation is required.

A qualified human may deliberately retain identical target wording after reviewing the changed source.

#### Same target text can still create a successor locale version

A successor locale version may legitimately contain text identical to its predecessor while carrying newer source provenance:

```text
AF6
  values = X
  source = EN4

AF7
  values = X
  source = EN5
```

These are distinct governed claims because the target was reconciled against different exact source truth.

#### Carry-forward never transfers approval/publication authority

This is absolute:

```text
copy target wording
≠
copy language approval

copy target wording
≠
copy clinical/specialist approval

copy target wording
≠
copy publication state
```

Every successor immutable locale version must establish its own applicable governance in its exact shared-version and source-provenance context.

#### Carry-forward does not automatically waive review

Even unchanged carried-forward text may require renewed language/specialist/clinical review because surrounding invariant/structural context may have changed.

For example:

```text
shared severity:
info → safety_critical
```

while translated wording remains identical.

Therefore carry-forward may reduce authoring work but never automatically weakens governing review/approval requirements.

A later explicit policy may define a differential-review path where justified.

#### Shared-version mismatch is stronger than ordinary source-wording staleness

When shared structure/invariant truth changes:

```text
C8 → C9
```

locale versions under C8 remain immutable historical C8 variants.

They cannot be treated as locale variants of C9.

This is a **shared-version mismatch**, distinct from same-C8 source-wording staleness.

#### Safe carry-forward C8 → C9 is draft-only

A new locale draft for C9 may be seeded from a C8 locale version only where correspondence is deterministic.

Minimum safe correspondence:

```text
same stable occurrence_key
AND compatible block contract
AND same/compatible localisable field semantics
```

The simplest safe case is:

```text
same occurrence_key
same block_type
same schema_version
same localisable field identity
```

Copied values remain draft material only.

#### Block schema evolution remains GRILL-05 authority

Translation carry-forward does not introduce a separate schema migration language.

If a block changes:

```text
callout/v2 → callout/v3
```

automatic translation carry-forward is permitted only where the code-authoritative block evolution contract defines an explicit compatible mapping for the relevant localisable fields.

Otherwise carry-forward fails closed.

#### New / removed occurrence or field

A new occurrence/field has no inherited target value.

A removed occurrence/field remains historical predecessor content and is not heuristically remapped elsewhere.

No translation rule guesses split/merge/replacement correspondence.

#### Reordering with preserved identity

If occurrences are reordered but retain stable occurrence identity/contracts, locale values may seed the successor locale draft.

The resulting successor locale still requires applicable governance because changed surrounding order may change interpretation.

#### Machine translation after source change

Machine assistance may generate replacement draft values for changed source fields.

It must:

- record the exact newer source version;
- remain draft/machine-draft material;
- never self-establish approval/publication where human/specialist review is required.

#### Published historical target is not automatically withdrawn

A newer source version does not itself mutate a published older target locale version to withdrawn.

Withdrawal/correction remains separate governed authority.

Where a source change is safety/legally material, existing correction/withdrawal policy may require urgent action, but that action is explicit and independently evidenced.

#### Aligned bilingual release gate

For content requiring aligned approved bilingual/multi-locale variants, a target locale version based on an older designated source cannot satisfy the aligned release gate for a newer designated source until reconciliation establishes current source alignment.

That does not erase or falsify the target version's historical approval/publication.

Optional low-risk fallback continues to follow existing Product Law rather than a new automatic withdrawal rule.

#### No permanent source language hierarchy

The model does not encode English as permanently canonical.

A translation relationship may identify any exact locale version as source.

Independently authored locale variants do not fabricate a translation-source relationship merely to fit persistence.

#### Translation assignment/work source history is preserved

Translation is explicit assignable work with source version, target locale, assignee, state and required review.

When source intent changes, existing source history is preserved.

The system may later model reconciliation as mutation with audit or successor work records, but it cannot silently overwrite source provenance.

Exact Resource choice remains Block 3A.5/JIT.

#### `stale` is derived, not editor-controlled truth

An editor does not arbitrarily toggle `stale`.

Conceptually:

```text
target source provenance = EN4
current designated source = EN5
→ stale
```

After explicit reconciliation establishes newer source provenance:

```text
successor target source provenance = EN5
→ current-aligned
```

Exact query/calculation mechanism remains JIT.

#### Historical validity versus current alignment

The architecture distinguishes:

```text
historical validity
→ immutable record accurately describes what happened

current alignment
→ whether that record/work satisfies current source/release intent
```

An old translation may therefore be historically valid and no longer current-aligned without contradiction.

#### Retranslation preserves both target and source lineage

Successor locale versions retain:

- predecessor locale-version lineage; and
- exact source-locale-version provenance.

Conceptually:

```text
AF6
  predecessor = AF5
  source = EN4

AF7
  predecessor = AF6
  source = EN5
```

Exact relationship names remain deferred.

#### Beacon

Beacon provides no direct donor for these translation-lineage/staleness semantics.

NewYou must implement them from Product/Architecture/Domain law.

### 6.74 ACCEPTED GRILL DECISION

#### `GRILL-23 — Translation Staleness Is Derived from Exact Source Provenance; Carry-Forward Is Draft-Only and Never Transfers Approval`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> A NewYou translation/locale lineage preserves the exact immutable source locale version used for translation or reconciliation where a translation relationship exists. The platform does not assume a permanent canonical source language.
>
> Translation staleness is a **derived current-alignment condition**, not a destructive lifecycle transition on an immutable historical `ContentTranslationVersion`.
>
> An approved or published historical locale version remains exact evidence of the wording, provenance, approvals and publication that actually occurred. A later source change does not rewrite those historical facts.
>
> Staleness is evaluated against the exact source locale version designated for the current translation/release intent, not against whatever locale version is merely “latest”. The existence of a newer candidate alone does not silently retarget translation work.
>
> Open translation work based on an older source version does not silently have its source reference changed. When the intended source advances, the work becomes stale until explicit reconciliation/rebase/successor work establishes the newer exact source provenance.
>
> Within the same shared `ContentVersion`, source-version comparison uses deterministic shared occurrence identity and code-defined localisable-field identity. Target draft values whose corresponding source values are unchanged may be retained automatically as draft material.
>
> Where a corresponding source localisable value changed, the existing target value cannot automatically be considered current. Explicit translation/reconciliation is required even if the target wording happens to remain textually identical.
>
> A qualified human may explicitly retain unchanged target wording after reviewing a changed source. Establishing alignment to the newer source may therefore create a successor immutable locale version whose textual values are identical but whose source provenance and governance evidence differ.
>
> Carry-forward never transfers Approval evidence, publication state or review authority. Any successor locale version establishes its own applicable governance against its exact shared Content Version and source provenance.
>
> Carry-forward also does not automatically waive required language, specialist or clinical review. Any reduced/differential review path must be explicitly justified by governing policy rather than inferred from unchanged copied values.
>
> A successor shared `ContentVersion` creates a **shared-version mismatch**, not merely ordinary source-wording staleness. Locale versions attached to the predecessor remain historical truth but cannot satisfy locale requirements for the successor shared version.
>
> Locale values may be seeded into draft authoring for a successor shared Content Version only where correspondence is deterministic: preserved occurrence identity plus an exact compatible localisable field contract, or an explicitly governed code-defined schema compatibility mapping.
>
> Translation carry-forward does not introduce a separate block-schema migration language. Block-schema evolution remains owned by `GRILL-05`; unsupported block/field mappings fail closed.
>
> New/removed occurrences or localisable fields are not heuristically matched. Removed values remain historical; new required values require new locale content.
>
> Reordered occurrences with preserved identity/contracts may carry their locale values forward as draft material, but changed structural/invariant context still requires renewed applicable governance before the successor locale version can be approved/published.
>
> Machine translation after a source change may generate replacement draft material for affected values but never establishes approval and must record the exact newer source version.
>
> A source change does not automatically withdraw a previously published target locale version. Withdrawal/correction remains separately governed according to risk and correction policy.
>
> For content requiring aligned approved bilingual/multi-locale variants, a target version whose translation provenance is stale relative to the designated source for the intended release cannot satisfy the aligned release gate until reconciled. This does not erase its historical approval/publication.
>
> Optional low-risk handling remains governed by the existing explicit fallback policy; this decision does not invent automatic withdrawal of an older locale publication.
>
> Source-based staleness applies only where an actual translation/source relationship exists. Independently authored locale variants do not receive fabricated source provenance merely to fit the model.
>
> Translation assignments/work preserve source-version history when the designated source changes; exact assignment Resource/lifecycle representation remains deferred.
>
> `stale` is derived from exact lineage/current-source intent and is not an arbitrary editor-controlled truth flag.
>
> Successor locale versions preserve both their locale-version predecessor lineage and their exact source-version provenance so retranslation history remains reproducible.
>
> Beacon provides **NO DIRECT DONOR** for these translation-lineage/staleness rules.

### 6.75 Consequences fixed for later grills

1. Translation source provenance references exact immutable source locale versions where a translation relationship exists.
2. No permanent canonical source language is introduced.
3. Staleness is derived current-alignment state, not destructive historical mutation.
4. Historical approval/publication facts remain immutable.
5. Staleness is relative to explicitly designated source intent, not merely “latest”.
6. Open work never silently retargets its source version.
7. Same-shared-version source changes can be diffed by occurrence key + localisable field identity.
8. Unchanged source fields may preserve target draft values automatically.
9. Changed source fields require explicit reconciliation.
10. Identical target text may still require a successor locale version because source provenance changed.
11. Carry-forward never transfers Approval evidence.
12. Carry-forward never transfers publication state.
13. Carry-forward never automatically waives required review.
14. Shared-version mismatch is distinct from source-wording staleness.
15. Cross-shared-version carry-forward is draft-only.
16. Cross-version carry-forward requires deterministic occurrence/field compatibility.
17. Block-schema compatibility remains GRILL-05 authority.
18. New/removed fields/occurrences are not heuristically matched.
19. Reordered preserved occurrences may seed successor drafts.
20. Machine translation remains draft-only and records exact source.
21. Source advancement does not automatically withdraw older published target truth.
22. Aligned bilingual release gates require current source alignment.
23. Optional low-risk fallback remains governed by existing Product Law.
24. Independently authored locale variants do not fabricate source provenance.
25. Translation work preserves source-history across source changes.
26. `stale` is not an arbitrary manually controlled truth flag.
27. Historical validity and current alignment are separate concepts.
28. Locale predecessor lineage and source provenance are both retained.
29. Block 3A.5 was subsequently resolved by `GRILL-24`; Blocks 3A.6–3A.10 were subsequently resolved by `GRILL-25`–`GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.76 Block 3A.5 pressure test — durable Resource boundaries for locale authoring, translation work and immutable locale truth

Current Product/Frontend/Architecture authority now requires three materially different durable concerns:

```text
mutable locale wording
translation assignment/work
immutable delivered locale-version truth
```

They have different identity, mutability, lifecycle, concurrency and governance responsibilities.

The Resource decision must therefore follow durable business truth rather than UI shape.

#### `ContentTranslationVersion` — dedicated immutable Resource justified

Product Law explicitly defines:

```text
ContentItem
→ ContentVersion
→ ContentTranslationVersion
```

and DEC-119 requires Ash-backed governed runtime content with immutable references to delivered translation versions.

`ContentTranslationVersion` therefore has independently addressable immutable business truth:

- exact shared `ContentVersion`;
- exact locale;
- immutable localisable values;
- locale predecessor lineage;
- exact source locale-version provenance where a translation relationship exists;
- exact governance target for review/approval/publication/correction.

It is not an embedded UI convenience object.

A dedicated immutable C&M Resource is justified.

#### Mutable locale authoring — dedicated subordinate Resource justified

`GRILL-22` and `GRILL-23` expose durable requirements for locale-specific mutable authoring:

- one exact target locale;
- mutable localisable values;
- independent autosave/revision/concurrency;
- exact shared `ContentVersion` context once shared structure has been cut;
- stable targeting by translation work;
- independent progress while other locales or future shared drafts advance.

Those requirements are relational and concurrency-bearing.

A dedicated subordinate mutable locale-authoring Resource is therefore justified conceptually.

The working conceptual name is:

```text
ContentLocaleDraft
```

but the exact Ash module/name remains JIT.

Its responsibility is:

> mutable locale-specific authoring truth for one locale against one exact shared Content Version context.

#### Why locale drafts cannot remain only embedded in the shared `ContentDraft`

Once shared C8 exists, locale work for C8 may continue while authors begin future shared work toward C9.

If all locale mutable state exists only inside the evolving shared `ContentDraft`, NewYou would have to either:

- make old-locale work accidentally follow future shared changes;
- freeze shared authoring until every locale finishes;
- or build hidden baseline/version pointers inside one increasingly overloaded aggregate.

A subordinate locale draft pinned to exact C8 avoids those competing-authority problems.

#### Pre-shared-version provisional locale authoring

Before a shared `ContentVersion` has been cut, provisional locale values may remain subordinate to the broader `ContentDraft` aggregate.

At the shared version-cut boundary, locale authoring that continues independently becomes pinned to the new exact shared `ContentVersion`.

Conceptually:

```text
ContentDraft exact revision
        ↓ shared version cut
ContentVersion C8
        ├── mutable locale authoring [en]
        └── mutable locale authoring [af]
```

Exact copy/create orchestration remains JIT.

#### One active locale draft per exact shared version + locale initially

NewYou initially supports at most one active authoritative mutable locale draft for:

```text
(ContentVersion, locale)
```

Parallel locale branches and merge semantics are not introduced without evidence.

Exact database uniqueness and lifecycle enforcement remain JIT.

#### Locale draft is not locale history

`ContentLocaleDraft` is mutable working truth.

It is not:

- `ContentTranslationVersion`;
- Review evidence;
- Approval evidence;
- Publication truth;
- Correction/Withdrawal truth.

Locale draft revision identity is likewise not locale-version identity.

#### Locale version cut

An immutable `ContentTranslationVersion` is cut from one exact locale-draft revision when localisable content crosses an exact locale-governance boundary.

Conceptually:

```text
ContentLocaleDraft @ revision 31
        ↓ locale version cut
ContentTranslationVersion AF7
```

Later locale-draft edits cannot mutate AF7.

Formal locale review/approval/publication then target exact immutable AF7.

Exact action/transaction implementation remains JIT.

#### `TranslationWork` — dedicated Resource justified

Current frontend authority explicitly says translation is assignable work with:

- exact source version;
- target locale;
- assignee;
- state;
- required review.

`GRILL-23` adds:

- source history must remain interpretable;
- source advancement cannot silently rewrite provenance;
- work may become stale relative to newer source intent;
- translation/reconciliation may be reassigned/repeated;
- history matters independently of target wording.

This is sufficient durable operational identity to justify a dedicated C&M TranslationWork Resource.

#### TranslationWork coordinates work but does not own translated wording

Authority separation is:

```text
TranslationWork
→ source / target / assignee / operational progress

ContentLocaleDraft
→ mutable target localisable values

ContentTranslationVersion
→ immutable target localisable truth
```

TranslationWork must not become a content-payload dumping ground.

#### One TranslationWork has one immutable exact source version

A TranslationWork record binds one exact immutable source locale version.

If source intent advances materially:

```text
W1 source EN4
→ historical/superseded work

W2 source EN5
→ successor/current work
```

NewYou does not rewrite W1's source reference to EN5 because that would falsify the work actually assigned/performed.

Exact work-state vocabulary remains JIT.

#### No permanent source-language hierarchy

TranslationWork source is an exact `ContentTranslationVersion`, not an English-specific concept.

Either locale may be a source when that reflects real authoring provenance.

Independently authored locale content requires no fabricated TranslationWork/source relationship.

#### TranslationWork targets mutable locale authoring

Conceptually:

```text
TranslationWork W2
  source = EN5
  target = mutable AF locale draft for C8
```

This gives translation operations a stable mutable target without making TranslationWork content authority.

Exact relationship normalization remains JIT.

#### One active source-designating TranslationWork per target locale draft initially

NewYou does not initially allow two simultaneously authoritative source assignments for the same target locale draft.

When source intent advances, existing work is completed/superseded/cancelled according to later lifecycle design and successor work becomes current.

Exact operational state names remain undecided.

#### TranslationWork is not one-to-one with immutable locale versions

One TranslationWork may yield zero, one or multiple immutable `ContentTranslationVersion` candidates.

Example:

```text
W1 source EN4
→ AF6 candidate
→ review requests changes
→ same mutable locale draft changes
→ AF7 candidate
```

if the exact source/reconciliation assignment remains EN4.

No artificial 1:1 constraint is introduced.

#### Immutable locale version retains source provenance independently

Where translation lineage exists, `ContentTranslationVersion` itself retains exact source locale-version provenance.

A relationship such as “produced from TranslationWork” may later supplement provenance, but work identity cannot replace exact source-version provenance.

Independently authored locale versions legitimately have no translation source.

#### Required-review routing is not Review/Approval evidence

`TranslationWork.required_review` or equivalent expresses operational routing/governance expectation.

It does not prove that Review/Approval occurred.

Actual Review/Approval evidence remains separate and references the exact immutable `ContentTranslationVersion`.

#### Machine/human translation mutate only mutable locale truth

Machine generation and human reconciliation modify `ContentLocaleDraft` through guarded/idempotent operations.

They do not:

- mutate an existing immutable locale version;
- create Approval evidence;
- publish content;
- overwrite newer human edits unconditionally.

#### No `TranslationStaleness` Resource

`GRILL-23` remains controlling.

Staleness is derived from exact source provenance plus current source/release intent.

No manually authoritative stale Boolean or dedicated staleness table is introduced.

#### No row-per-field `TranslationUnit` Resource initially

Localisable values remain bounded structured data addressed by:

```text
occurrence_key
+
block-contract localisable field identity
```

No row-per-field TranslationUnit model is justified yet.

A future cross-content translation-memory/reuse requirement may create new evidence, but no such relational need currently exists.

#### No provider-attempt business Resource initially

Machine provider calls/jobs do not automatically justify:

```text
TranslationAttempt
MachineTranslationRun
TranslationProviderJob
```

as business Resources.

Durable async execution may use Oban and audit/provider telemetry.

Promotion to a business Resource requires later evidence such as legally significant provider provenance, billing reconciliation or independent provider-attempt lifecycle.

#### Work Queue remains projection

TranslationWork may appear in Work Queue views.

The queue does not become generic Task authority.

TranslationWork is justified by translation-domain facts, not because a queue exists.

#### Retention and interpretability

Completed/superseded TranslationWork needed for governed provenance/audit must remain interpretable.

It must not be destructively deleted in a way that breaks historical evidence.

Exact retention duration/category remains governed elsewhere.

#### Concurrency boundary

Three distinct mutable concurrency seams now exist conceptually:

```text
ContentDraft revision
→ shared mutable structure

ContentLocaleDraft revision
→ mutable locale values

TranslationWork state/source
→ translation coordination
```

A machine/human write must be valid against the exact work/source and locale-draft revision it evaluated.

Stale asynchronous results must not blindly overwrite newer human/machine edits.

Exact PostgreSQL/Ash optimistic-concurrency implementation remains JIT.

No GenServer becomes durable correctness authority.

#### Idempotency boundary

Translation generation/reconciliation actions require an idempotent logical-operation boundary tied to exact work/source/draft assumptions.

This requirement does not itself justify another business Resource.

#### OQ-013 consequence

This decision materially answers the Resource-boundary portion of OQ-013 for later authoritative C&M JIT/Architecture Review:

```text
mutable locale authoring
→ dedicated subordinate Resource

translation assignment/work
→ dedicated operational Resource

immutable locale truth
→ dedicated ContentTranslationVersion Resource
```

The working Beacon dossier does not itself close OQ-013, amend authoritative Architecture Law, or authorise implementation.

Exact Ash relationships/identities/indexes, Approval integration, immutable delivery references and action mechanics remain downstream.

#### Beacon

Beacon provides no direct donor for this Resource topology.

NewYou must implement it from its own Product/Architecture/Domain authority.

### 6.77 ACCEPTED GRILL DECISION

#### `GRILL-24 — Mutable Locale Authoring, Translation Work, and Immutable Locale Versions Are Separate Durable C&M Concerns`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou uses three distinct durable ownership boundaries for governed locale content: a subordinate mutable locale-authoring draft, durable translation-work coordination where a translation relationship exists, and immutable `ContentTranslationVersion` truth.
>
> A dedicated conceptual `ContentLocaleDraft` Resource is justified by durable requirements rather than UI convenience. It owns mutable localisable authoring values for one locale against one exact shared Content Version context, together with its authoring revision/concurrency boundary. The exact Ash module/name remains JIT.
>
> Before a shared Content Version exists, provisional locale values may remain subordinate to the broader `ContentDraft` authoring aggregate. Once an exact shared `ContentVersion` has been cut, independently advancing locale work for that version is pinned to that exact shared version rather than following future shared-draft changes.
>
> NewYou initially permits at most one active authoritative mutable locale draft per exact shared `ContentVersion` + locale. Parallel locale-authoring branches and merge semantics are not introduced without evidence.
>
> `ContentLocaleDraft` is mutable working truth, not historical locale-version truth, not Approval evidence and not Publication authority.
>
> A new immutable `ContentTranslationVersion` is cut from one exact locale-draft revision when localisable content crosses its exact locale-governance boundary. Later locale-draft edits cannot mutate that immutable version.
>
> A dedicated C&M `TranslationWork` Resource is justified because translation is durable assignable work with exact source version, target locale/draft, assignee, operational state, required-review routing and source/work history.
>
> `TranslationWork` coordinates authoring but does not own translated wording. Mutable target wording remains `ContentLocaleDraft` truth; immutable governed wording remains `ContentTranslationVersion` truth.
>
> One TranslationWork has one exact immutable source locale version. A material change in designated source does not rewrite that source reference; it creates successor translation work or an equivalent explicitly historical successor operation. Exact operational state values remain JIT.
>
> No permanent source-language hierarchy is introduced. Independently authored locale content requires no fabricated `TranslationWork` or source-version provenance.
>
> NewYou initially permits only one active source-designating TranslationWork for a target locale draft. Competing simultaneous translation-source authorities are not introduced.
>
> TranslationWork is not 1:1 with `ContentTranslationVersion`. One work item may yield zero, one or multiple immutable locale-version candidates while the same source/reconciliation assignment remains active.
>
> Immutable `ContentTranslationVersion` retains its exact source locale-version provenance where a translation relationship exists independently of TranslationWork persistence. A produced-from-work relationship may supplement but never replace exact source provenance.
>
> `ContentTranslationVersion` is a dedicated immutable C&M Resource as required by the accepted Product/Architecture hierarchy. It owns exact locale, localisable values, shared `ContentVersion` parent and immutable locale-lineage/provenance facts. Approval, Publication and Correction/Withdrawal remain separate authorities around it.
>
> TranslationWork `required review` expresses routing/required governance intent but does not itself constitute Review or Approval evidence.
>
> Machine translation and human translation/reconciliation mutate only mutable locale-authoring truth through guarded/idempotent operations. They never mutate an existing immutable `ContentTranslationVersion` or directly establish Approval/Publication.
>
> No separate `TranslationStaleness` Resource or manually authoritative stale flag is introduced; staleness remains derived under `GRILL-23`.
>
> No row-per-field `TranslationUnit` Resource is introduced initially. Localisable values remain bounded structured data addressed by shared occurrence key + block-contract field semantics unless a future translation-memory/reuse requirement demonstrates a relational need.
>
> No `TranslationAttempt` / provider-run business Resource is introduced initially merely for asynchronous execution. Durable jobs/audit/provider telemetry remain implementation/evidence mechanisms unless later business/legal requirements justify promotion.
>
> Work Queue/UI surfaces derive from domain work and do not create a generic universal Task authority.
>
> TranslationWork and locale-draft mutations must be concurrency-safe against the exact work/source assumptions and exact locale-draft revision they evaluated. Stale asynchronous results must not overwrite newer human or machine edits. Exact optimistic-concurrency/idempotency mechanisms remain JIT.
>
> Completed/superseded TranslationWork required for governed provenance/audit remains interpretable and is not destructively deleted in a way that breaks historical evidence. Exact retention periods remain governed elsewhere.
>
> This decision materially answers the Resource-boundary portion of OQ-013 for later C&M JIT adoption, but does not itself close the governed OQ-013 authority item or authorise Ash implementation.
>
> Beacon provides **NO DIRECT DONOR** for this Resource topology.

### 6.78 Consequences fixed for later grills

1. Dedicated immutable `ContentTranslationVersion` Resource is justified.
2. Dedicated subordinate mutable locale-authoring Resource is justified conceptually (`ContentLocaleDraft` working name only).
3. Dedicated C&M TranslationWork Resource is justified.
4. Locale draft is pinned to one exact shared `ContentVersion` after shared version cut.
5. At most one active authoritative locale draft exists per exact ContentVersion + locale initially.
6. Parallel locale draft branches/merge semantics remain unsupported without evidence.
7. Locale draft is mutable working truth, not immutable locale history.
8. Locale version cut snapshots one exact locale-draft revision.
9. Later locale-draft edits cannot mutate an existing ContentTranslationVersion.
10. TranslationWork owns operational coordination, not wording.
11. One TranslationWork has one exact immutable source locale version.
12. Source changes do not silently rewrite existing TranslationWork provenance.
13. No permanent source-language hierarchy is introduced.
14. At most one active source-designating TranslationWork per target locale draft initially.
15. TranslationWork is not constrained 1:1 to immutable locale versions.
16. Immutable locale versions retain exact source provenance independently of work records.
17. TranslationWork review requirements are routing/expectation, not Review/Approval evidence.
18. Machine/human translation mutate only mutable locale authoring.
19. No TranslationStaleness Resource/manual truth flag.
20. No row-per-field TranslationUnit Resource initially.
21. No provider-attempt business Resource initially absent new evidence.
22. Work Queue remains projection, not universal Task authority.
23. TranslationWork required for provenance/audit remains interpretable.
24. Locale-draft/work writes require stale-write protection against exact assumptions/revision.
25. Translation actions require idempotency; this does not itself justify another Resource.
26. The Resource-boundary portion of OQ-013 is materially answered for later authoritative adoption, but OQ-013 remains governed/open until the proper Architecture Review/JIT closes it.
27. Block 3A.6 was subsequently resolved by `GRILL-25`; exact locking/constraint mechanics remain JIT, and Block 3A.7 was subsequently resolved by `GRILL-26`; Block 3A.8 was subsequently resolved by `GRILL-27`; Block 3A.9 was subsequently resolved by `GRILL-28`; Block 3A.10 was subsequently resolved by `GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.79 Block 3A.6 pressure test — shared/locale draft lifecycle and concurrency

Current NewYou authority requires safe autosave with durable business authority, immutable governed snapshot boundaries, PostgreSQL-backed authoritative state, concurrency control selected by the invariant, short coherent transactions and durable idempotency evidence where crash recovery/reconciliation depends on it. PubSub/process/browser state remains freshness/UX only.

#### Version cuts do not retire mutable drafts

Creating an immutable `ContentVersion` from an exact `ContentDraft` revision does not automatically close, replace or retire that draft.

```text
ContentDraft D @ rev 43
        ↓ governed version cut
ContentVersion C8

ContentDraft D
→ remains active mutable authoring workspace
```

The same applies to `ContentLocaleDraft`.

This supports review/change-request loops without needless draft-record churn.

#### Minimal lifecycle

The initial semantic lifecycle is only:

```text
ACTIVE
→ ABANDONED
```

Exact enum names remain JIT.

`ACTIVE` means authoritative mutable workspace, not “currently open in UI”.

`ABANDONED` means non-authoritative: no further authored mutation and no further version cuts.

#### Abandonment is initially terminal

Restore-in-place is not introduced initially. If future editing is needed, a new active draft is created from an explicitly selected governed source.

Abandonment is not hard deletion; retention/deletion remains governed by audit/privacy/provenance requirements.

#### Active-authority uniqueness

Initially:

```text
ContentItem
→ at most one ACTIVE ContentDraft

(ContentVersion, locale)
→ at most one ACTIVE ContentLocaleDraft
```

Database-backed enforcement is required. Parallel branch/merge semantics are not introduced without evidence.

#### Shared-version advancement does not rebind predecessor locale drafts

A locale draft pinned to C8 remains C8 work after C9 exists.

A separate C9 locale draft may exist for the same locale.

GRILL-23 governs any safe carry-forward into that successor draft.

#### Locale-draft abandonment must coordinate with TranslationWork

A locale draft cannot be abandoned while leaving active/current TranslationWork as writable authority against it.

Abandonment must either find no active TranslationWork or coherently transition affected work in the same governed operation. Exact work states remain JIT.

#### Exact durable revisions

Every mutable shared/locale draft has a monotonically changing authoritative revision or equivalent concurrency token.

A mutation is valid only against the exact expected revision/state it evaluated.

Stale writes fail closed.

Generic last-write-wins and automatic collaborative merge are rejected initially.

#### Revisions track authored truth only

Revisions advance for authoritative authoring changes, not for PubSub, preview generation, viewing, cache refresh or downstream publication effects.

#### Exact-revision version cuts

Shared and locale version cuts bind to one exact draft revision. Concurrent later edits cannot leak into the immutable snapshot.

#### Idempotent version cuts

Repeating the same semantic cut for the same exact draft revision cannot mint duplicate immutable versions.

```text
D @ rev 43
→ C8

retry same semantic cut
→ C8
```

One active draft may nevertheless produce multiple successive versions from different revisions.

#### Draft origin vs immutable predecessor lineage

A draft's original base/source provenance is distinct from later immutable predecessor/version lineage.

Those meanings must not be collapsed into one mutable pointer.

#### Review feedback does not roll drafts backward automatically

If a reviewed immutable candidate captured rev43 while the active draft has advanced to rev50, review rejection/changes-requested does not reset the draft to rev43.

Applying feedback to current mutable authoring is deliberate.

#### Async work carries exact assumptions

Machine translation, Template migration and other asynchronous/multi-step mutations carry the exact draft/work/source assumptions they evaluated.

If required assumptions changed before commit, stale output does not overwrite current truth.

#### Small atomic authority transaction

A version cut conceptually:

```text
verify ACTIVE draft
verify expected revision
validate governed state
create immutable version + provenance/lineage
establish durable idempotency
COMMIT
```

External providers, notifications, CDN/cache effects and PubSub stay outside the authoritative transaction.

#### Failure/retry semantics

Failure before commit leaves no half-created immutable truth.

If commit succeeds but acknowledgement is lost, retry/reconciliation resolves the committed result rather than creating duplicate truth.

#### No process-local correctness authority

LiveView/browser state, GenServer, ETS and PubSub may improve UX/freshness but never establish active-draft uniqueness, valid revision, idempotency or business truth.

### 6.80 ACCEPTED GRILL DECISION

#### `GRILL-25 — Shared and Locale Drafts Are Single-Active Durable Workspaces with Explicit Abandonment, Exact-Revision Concurrency and Idempotent Version Cuts`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> `ContentDraft` and the conceptual `ContentLocaleDraft` are durable mutable authoring workspaces. Their lifecycle is independent from immutable version creation, review, approval and publication.
>
> Creating an immutable `ContentVersion` or `ContentTranslationVersion` does not automatically close, retire or replace the mutable draft from which it was cut. The draft remains the active authoring workspace until it is explicitly abandoned/replaced under its own lifecycle.
>
> One active shared `ContentDraft` is permitted per `ContentItem` initially. One active `ContentLocaleDraft` is permitted per exact `ContentVersion` + locale initially. Database-backed enforcement is required; parallel mutable authorities and merge semantics are not introduced without evidence.
>
> The initial draft lifecycle needs only the semantic distinction between **active authoritative workspace** and **explicitly abandoned/non-authoritative workspace**. Exact enum names remain JIT. Version cuts, review, approval, publication and immutable-version supersession do not themselves imply draft abandonment.
>
> Abandonment is explicit and initially terminal for that draft identity. An abandoned draft cannot receive further authoring mutations or produce new immutable versions. Restore-in-place is not introduced without evidence; future editing creates a new authoritative draft from an explicitly selected governed source under later action design.
>
> Abandonment does not itself imply hard deletion. Draft retention/deletion follows audit/privacy/provenance requirements, and drafts required to interpret governed evidence must not be destructively removed while that requirement exists.
>
> For shared authoring, a new active draft cannot be created concurrently when another active draft already owns the `ContentItem`. For locale authoring, a second active draft cannot be created for the same exact `ContentVersion` + locale. Exact constraint/index implementation remains JIT.
>
> A shared Content Version change does not silently rebind or abandon locale drafts pinned to its predecessor. Locale work for C8 remains C8 work even after C9 exists. A distinct C9 locale draft may be created using the accepted GRILL-23 carry-forward rules.
>
> A locale draft with active/current TranslationWork cannot be abandoned while leaving that work as a writable/current authority. Draft abandonment must either require no active TranslationWork or coherently transition affected work in the same governed operation. Exact TranslationWork lifecycle states remain JIT.
>
> Every mutable shared/locale draft has an authoritative monotonically changing authoring revision or equivalent concurrency token. A mutation is valid only against the exact expected revision/state it evaluated.
>
> A stale write fails closed rather than silently overwriting newer authored truth. Generic last-write-wins and automatic collaborative merge semantics are not introduced initially.
>
> PubSub, LiveView/browser state and process-local coordination may improve freshness/UX but never establish write validity. PostgreSQL-backed authoritative state/concurrency remains controlling.
>
> Draft revisions track authoritative authoring changes, not derived/UI/freshness events.
>
> Shared version cuts and locale version cuts bind to one exact expected draft revision. The immutable snapshot must contain exactly that revision's governed truth and provenance; concurrent later edits cannot leak into the snapshot.
>
> Repeating the same semantic version-cut operation for the same exact source draft revision is idempotent and must not mint duplicate immutable versions merely because of retry, timeout or duplicate submission.
>
> One active draft may produce multiple successive immutable versions over time from different exact draft revisions. A single exact draft revision does not produce duplicate equivalent immutable snapshots.
>
> Draft origin/base provenance is distinct from successor immutable-version lineage.
>
> Review rejection/changes-requested does not roll an advanced active draft backward automatically.
>
> Machine translation, Template migration and other asynchronous or multi-step mutations carry the exact draft/work/source assumptions they evaluated. If required assumptions changed, stale output does not overwrite current truth.
>
> Version-cut and other coherent authoritative transitions use the smallest short transaction that verifies expected state, validates invariants, writes the immutable result/provenance and establishes required durable idempotency. External/provider/realtime consequences are not part of that authority transaction.
>
> Transaction failure leaves no half-created immutable version or partially advanced draft authority. If authoritative commit succeeds but confirmation is lost, retry/reconciliation resolves the already-created result.
>
> Exact optimistic-lock fields, Ash actions, PostgreSQL constraints/indexes, idempotency-key representation, Oban mechanics, deletion windows and UI conflict-resolution flows remain downstream JIT choices.
>
> No GenServer, ETS, PubSub or browser state becomes authoritative draft/concurrency truth.
>
> Beacon provides **NO DIRECT DONOR** for these lifecycle/concurrency semantics.

### 6.81 Consequences fixed for later grills

1. Version cuts do not retire shared or locale drafts.
2. Draft lifecycle is independent from Review/Approval/Publication.
3. Initial draft lifecycle is semantically ACTIVE → ABANDONED.
4. Abandonment is explicit and terminal for that draft identity initially.
5. Restore-in-place is unsupported initially.
6. Abandonment does not imply hard deletion.
7. One active ContentDraft per ContentItem initially.
8. One active ContentLocaleDraft per exact ContentVersion + locale initially.
9. Active-authority uniqueness requires durable/database-backed enforcement.
10. Shared-version advancement does not silently rebind predecessor locale drafts.
11. Different shared ContentVersions may each have a locale draft for the same locale.
12. Locale-draft abandonment must coherently handle active/current TranslationWork.
13. Every mutable draft has an authoritative revision/concurrency token.
14. Stale writes fail closed.
15. Generic last-write-wins is rejected.
16. Generic automatic collaborative merge is rejected initially.
17. Revisions track authored truth, not freshness/derived events.
18. Version cuts bind to one exact draft revision.
19. Equivalent retry cuts are idempotent.
20. One draft may yield successive immutable versions from different revisions.
21. One exact revision does not mint duplicate equivalent versions.
22. Draft origin provenance is distinct from immutable predecessor lineage.
23. Review rejection does not automatically roll back an advanced draft.
24. Async/multi-step operations carry and verify exact source assumptions.
25. Template migration commit is invalidated by relevant concurrent draft changes.
26. Authority transactions remain small and short.
27. Failed transactions leave no partial immutable truth.
28. Successful-but-unacknowledged transactions reconcile to the committed result.
29. Process-local/frontend state never becomes concurrency authority.
30. Block 3A.7 was subsequently resolved by `GRILL-26`; Blocks 3A.8–3A.10 were subsequently resolved by `GRILL-27`–`GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.82 Block 3A.7 pressure test — Review/Approval authority without lifecycle collapse

Current Product/Operating/Domain authority requires approval authority to vary by content risk, language and professional scope, while each applicable approval remains separately recorded even where one person may satisfy several roles. `GRILL-21` already separates immutable content truth, Review, Approval, Publication and Correction/Withdrawal.

The architecture therefore needs durable scoped evidence around exact immutable subjects rather than one overloaded `approved` field/status.

#### Approval is a genuine durable C&M concept

`Approval` is already a major Content & Media concept in the Domain Map.

An Approval represents one affirmative governance fact about:

```text
one exact immutable governed subject
+
one explicit bounded approval scope
+
one exact authorised approver/context
```

Exact Ash fields/relationships remain JIT.

Approval is durable evidence. It is not merely a UI state.

#### Review and Approval are distinct

Formal Review is durable workflow/evaluation evidence around an exact immutable candidate.

It may record:

- exact immutable subject;
- reviewer/context/role;
- outcome;
- reason/comment;
- time.

Review can result in changes requested/rejection without creating negative Approval records.

Conceptually:

```text
Review
→ evaluation/workflow evidence

Approval
→ affirmative scoped governance evidence
```

Exact Review Resource topology remains JIT.

#### Changes requested never mutate immutable candidates

A reviewed immutable candidate remains immutable.

Changes requested are applied through the appropriate active draft and produce a successor immutable candidate before renewed governance.

Historical review context remains interpretable.

#### Approval attaches at the narrowest complete immutable subject

For delivered localised content, language and wording/meaning-sensitive professional, clinical, legal/privacy, faith/editorial or safety approvals normally attach to exact `ContentTranslationVersion` because that is the immutable delivered locale wording in the exact shared `ContentVersion` context.

An Approval attaches directly to `ContentVersion` only when governing policy explicitly requires approval of shared/locale-invariant truth.

NewYou does not duplicate every locale approval onto both shared and locale subjects.

#### Locale approval is independent

Approval of one locale never implies approval of another locale.

Approval of a shared `ContentVersion` never substitutes for wording-sensitive Approval of a locale version where policy requires that locale-specific approval.

#### Approval scope is explicit and bounded

Each required approval is separately recorded.

One person may satisfy several scopes, but each scoped Approval remains distinct.

The approval-scope vocabulary is governed/bounded rather than arbitrary administrator-defined strings or runtime policy code.

Exact enum/catalogue representation remains JIT.

#### Approval requirements need historical basis

The platform must retain enough provenance to explain:

- which approval scopes were required for the exact subject;
- what governed type/risk/locale/professional context caused those requirements;
- which policy/compatibility basis was evaluated at that governance point.

This does not yet justify a dedicated `ApprovalRequirementSet` Resource.

The persistence shape remains JIT.

#### Historical Approval vs current eligibility

Historical Approval evidence remains true even if later policy/compatibility changes mean the subject is no longer eligible for a future publication/republication/new-authoring decision.

Therefore:

```text
historical Approval evidence
≠
current approval/readiness eligibility
```

Current readiness is derived from:

- exact immutable subject;
- applicable required approval scopes;
- separately recorded Approval evidence;
- current governing policy/compatibility checks.

Derived operator labels such as `approved` or `ready_to_publish` are projections, not new authority.

#### No generic expiry/revocation lifecycle invented here

Current content law does not establish a generic Approval expiry/revocation lifecycle.

This seam does not invent one.

If future policy requires expiry/retraction/revocation, historical evidence must remain interpretable and invalidation must be explicit rather than destructive overwrite.

#### OQ-016 stale approval remains eligibility logic

OQ-016 stale-approval checks operate around preserved historical Approval evidence.

A manually authoritative `approval.stale` flag is not introduced here.

`GRILL-28` subsequently resolves the semantic publication eligibility/revalidation boundary. Exact OQ-016 scheduler reliability, retry, alert ownership, approved-window and recovery mechanics remain JIT/Operations review.

#### Publication consumes eligible Approval evidence

Publication/scheduling evaluate the exact immutable subject and current eligibility of all required Approval evidence.

Publication does not manufacture Approval.

Approval does not manufacture Publication.

`GRILL-28` subsequently fixes the revalidation rule: scheduled execution re-evaluates current eligibility for the exact pinned immutable target. Exact OQ-016 operational mechanics remain open.

#### Template Version uses the same bounded C&M Approval semantics

`ContentTemplateVersion` does not create a competing `TemplateApproval` authority.

Required Template approval is recorded through the same bounded C&M Approval semantics against exact `ContentTemplateVersion`.

Template maturity:

```text
DRAFT → APPROVED
```

remains a useful workflow/selectability marker that can only be established when required Approval evidence exists.

The maturity marker is not itself the evidence.

#### Template approval never transfers to content

Approval of `ContentTemplateVersion T7` does not approve any `ContentVersion` / `ContentTranslationVersion` instantiated from T7.

Likewise content approval does not substitute for Template approval.

#### One semantic Approval authority does not require polymorphic storage

This decision requires one coherent C&M Approval meaning.

It does not require one polymorphic database table/foreign key.

JIT may choose typed subject relationships/resources to preserve PostgreSQL referential integrity.

#### EXPOSED-01 current-selectability gate — subsequently resolved semantically by GRILL-27

Historical Template Approval remains distinct from current Template selectability.

Current selectability additionally requires current Content Type compatibility/version-addressable interpretation. `GRILL-27` subsequently resolves that semantic dependency through code-authoritative, explicitly revision-addressable Content Type contracts with fail-closed directional compatibility.

#### Multi-scope UX may be efficient without collapsing evidence

One authorised person may complete several required scopes in one UX interaction.

The persistence/evidence result remains separate scoped Approval facts.

#### No universal cross-platform Approval engine

This is a bounded C&M Approval authority.

It does not imply a generic Approval engine across unrelated NewYou Domains.

#### Beacon

Beacon provides no direct donor for NewYou's scoped Review/Approval authority semantics.

### 6.83 ACCEPTED GRILL DECISION

#### `GRILL-26 — Approval Is Separate Scoped Evidence Against Exact Immutable C&M Subjects; Review and Readiness Remain Distinct`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> Content & Media uses one bounded Approval semantic authority for its governed immutable subjects. Approval evidence is distinct from Review workflow, immutable content/version truth, Publication truth and derived current readiness.
>
> Each Approval represents one affirmative governance fact for one exact immutable governed subject and one explicit bounded approval scope. Approval is not represented solely by a mutable `approved` Boolean or an overloaded subject lifecycle status.
>
> Approval authority follows governing content risk, language and professional scope. Each required approval is recorded separately, including when one person is authorised to satisfy multiple scopes.
>
> Approval-scope vocabulary is governed/bounded rather than arbitrary runtime strings or administrator-authored workflow policy. Exact catalogue/enum representation remains JIT.
>
> For delivered localised content, language and other wording/meaning-sensitive professional, clinical, legal/privacy, faith/editorial or safety approvals attach to the exact `ContentTranslationVersion`, which already identifies the exact parent `ContentVersion`. Approval of one locale never implies approval of another locale.
>
> An Approval attaches directly to `ContentVersion` only where governing policy explicitly requires independent approval of shared/locale-invariant truth. NewYou does not duplicate every locale approval onto both shared and locale versions.
>
> Approval attaches at the narrowest immutable governed subject containing all truth actually being approved.
>
> Formal Review is durable workflow/evaluation evidence around an exact immutable candidate but is not itself Approval authority. Changes-requested/rejected review evidence is not modelled merely as a negative Approval.
>
> Review history preserves sufficient exact subject, reviewer/context, outcome, reason/comment and time evidence for later interpretation. Exact Review Resource topology remains JIT.
>
> Changes requested or rejection never mutates the reviewed immutable subject. Revised work occurs through the appropriate mutable draft and creates a successor immutable candidate before renewed formal governance.
>
> Approval of one immutable version does not transfer to a changed successor version. Approval also does not transfer between locale variants.
>
> Existing Approval evidence for one scope is not destructively removed merely because another required scope requests changes; readiness fails because the complete required Approval set is absent. A changed successor subject establishes all applicable approvals independently.
>
> The set of approvals required for an exact subject is derived from its governed type/risk/locale/professional context. NewYou retains sufficient immutable requirement-basis provenance to explain why particular approvals were required when the governance decision occurred. Exact persistence shape remains JIT; no `ApprovalRequirementSet` Resource is introduced without relational evidence.
>
> Historical Approval evidence and current approval eligibility are separate concepts. Later policy/compatibility changes do not rewrite the fact that an Approval occurred.
>
> Current readiness/eligibility is derived from the exact immutable subject, the applicable approval requirements, the separately recorded Approval evidence and current governing compatibility/policy checks. A derived UI label such as “approved” or “ready to publish” is not independent authority.
>
> Current Product Law does not establish a generic Approval expiry/revocation lifecycle. NewYou does not invent one in this seam. If later policy requires revocation, expiry or retraction, historical Approval evidence must remain interpretable and any invalidation must be explicit rather than destructive mutation.
>
> OQ-016 stale-approval checks operate on current eligibility around preserved historical Approval evidence; `stale` is not introduced here as a manually authoritative Approval flag.
>
> Publication and scheduling consume exact eligible Approval evidence for the exact immutable subject. Publication does not create Approval, and Approval does not create Publication. Scheduled publication must later re-evaluate current eligibility according to the OQ-016 contract.
>
> `ContentTemplateVersion` uses the same bounded C&M Approval semantic authority rather than a competing `TemplateApproval` meaning. Template maturity `DRAFT → APPROVED` remains a workflow/selectability marker that may only be established when the required Approval evidence for that exact Template Version exists; the maturity state is not itself the Approval evidence.
>
> Template approval never transfers to content instantiated from the Template, and content approval never substitutes for Template approval.
>
> Exact persistence may use typed subject relationships/resources if needed for PostgreSQL referential integrity; this decision does not require a polymorphic database foreign-key design. It requires one coherent C&M Approval semantics.
>
> Historical Template Approval remains distinct from current Template selectability. Current selectability additionally depends on the unresolved `EXPOSED-01` Content Type compatibility/version-addressability seam.
>
> Review/Approval UX may let one authorised person complete several scopes efficiently, but each required Approval remains separately durable.
>
> Content & Media Approval does not become a universal cross-platform Approval engine for unrelated Domains.
>
> Beacon provides **NO DIRECT DONOR** for this Review/Approval authority model.

### 6.84 Consequences fixed for later grills

1. C&M Approval is a durable bounded semantic authority.
2. Approval is separate from Review, Publication and immutable subject truth.
3. Approval is separately recorded per exact subject + bounded scope.
4. One approver may satisfy several scopes, but each Approval remains separate.
5. Approval-scope vocabulary is governed/bounded.
6. Delivered locale wording/meaning-sensitive approvals normally attach to exact ContentTranslationVersion.
7. ContentVersion receives direct Approval only where policy explicitly requires shared/invariant approval.
8. Locale approval never transfers across locales.
9. Approval attaches at the narrowest immutable subject containing the truth being approved.
10. Formal Review is durable workflow/evaluation evidence, not negative/positive Approval authority.
11. Review rejection/changes requested never mutate immutable candidates.
12. Approval never transfers to changed successor versions.
13. Existing Approval in one scope is not deleted merely because another scope requests changes.
14. Approval requirement provenance must remain explainable.
15. No ApprovalRequirementSet Resource is introduced by this decision.
16. Historical Approval evidence is distinct from current eligibility/readiness.
17. Readiness is derived and not an independent authoritative Boolean/status.
18. No generic Approval expiry/revocation lifecycle is invented here.
19. OQ-016 stale approval remains current-eligibility logic around preserved historical evidence.
20. Publication/scheduling consume eligible Approval evidence but remain separate authority.
21. ContentTemplateVersion uses the same bounded C&M Approval semantics.
22. Template maturity APPROVED is not itself Approval evidence.
23. Template approval never transfers to instantiated content.
24. One semantic Approval authority does not require polymorphic persistence.
25. `EXPOSED-01` was subsequently resolved semantically by `GRILL-27`; exact catalogue/compatibility implementation remains JIT.
26. Multi-scope UX may be combined while evidence stays separate.
27. C&M Approval does not become a universal platform Approval engine.
28. Block 3A.8 was subsequently resolved by `GRILL-27`; Blocks 3A.9–3A.10 were subsequently resolved by `GRILL-28`–`GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.85 Block 3A.8 pressure test — governed Content Type contract revision/addressability

Current NewYou authority requires a controlled, approved, extensible catalogue of Content Types. The creator selects one governed type before composing, and that type controls structure, metadata and applicable workflow.

No current authority requires operators to create or mutate Content Type contracts dynamically in PostgreSQL.

The problem exposed by `GRILL-14` / `EXPOSED-01` is historical interpretation and current compatibility, not runtime administration.

#### Mutable ContentType rows are insufficient

A mutable current `ContentType` record cannot explain which exact contract semantics governed an older Template Version approval after the row changes.

Historical Template Approval and immutable Content Version interpretation therefore require explicit version-addressable contract identity.

#### No dedicated ContentType / ContentTypeVersion Resources initially

A data-versioned ContentType/ContentTypeVersion hierarchy could solve addressability, but it would also introduce another governed lifecycle, current pointer, approval path and runtime configuration authority.

No current requirement justifies that complexity.

The initial authority remains code-defined.

#### Code-authoritative catalogue with explicit contract revisions

Each governed Content Type has:

```text
stable type key
+
explicit immutable contract revision
+
code-defined bounded semantics
```

Application release/Git SHA is not the Content Type contract identity.

A contract revision changes only when governed Content Type semantics change.

#### Contract ownership boundary

The Content Type contract owns only type-level semantics such as:

- permitted structural/block capabilities;
- required/allowed metadata semantics;
- shared/localisable metadata classification where type-owned;
- type-specific invariants/validation;
- Template compatibility envelope;
- type-owned workflow/risk capability classification.

It does not duplicate block implementation/contracts, Template-specific narrowing, Approval evidence, Publication truth, Translation lifecycle or arbitrary runtime workflow policy.

#### Content Type is the broad envelope; Template narrows it

Effective authoring validity remains directional:

```text
Content Type contract
∩ ContentTemplateVersion contract
∩ block / block-slot contracts
```

A Template may narrow its Content Type contract but never expand it.

#### Template Version approval retains exact Content Type contract basis

Each `ContentTemplateVersion` records the exact stable type key + contract revision used for validation/approval.

Historical Approval remains evidence about that exact Template Version under that exact Content Type contract basis.

A later current contract revision does not rewrite that history.

#### Immutable ContentVersion retains exact type-contract provenance

Each immutable `ContentVersion` records the exact Content Type contract revision against which its shared governed content was validated.

Historical interpretation never depends on whatever the current application now means by the type key alone.

#### Active ContentDraft pins one exact type-contract revision

An active shared `ContentDraft` is governed against one exact Content Type contract revision.

A newly deployed/current contract revision does not silently reinterpret or migrate the draft.

Adoption of a newer contract revision requires an explicit validated migration/rebase operation; exact mechanics remain JIT.

#### Locale resources derive type provenance through ContentVersion

`ContentLocaleDraft` and `ContentTranslationVersion` do not create a second Content Type authority.

Their exact parent `ContentVersion` carries the relevant type-contract provenance.

#### Any governed semantic change gets a new revision

If a Content Type semantic changes in a way that may affect validation, interpretation, metadata, Template compatibility or type-contributed workflow/risk behavior, a new contract revision is created even if the change is backwards compatible.

Contract provenance and compatibility are separate questions.

#### Compatibility is explicit and directional

Historical Template approval under revision A may or may not remain selectable under current revision B.

The question is explicit:

```text
is Template contract approved under type@A
still valid for new authoring under current type@B?
```

Compatibility is directional and deterministic.

#### Compatibility defaults fail closed

Initial rule:

```text
same exact revision
→ compatible

different revision
→ incompatible unless explicit code-defined compatibility says otherwise
```

Compatibility is not inferred from names, apparent structural similarity, additive-looking changes or runtime data shape.

#### Compatibility remains code-defined

No runtime compatibility table, migration expression language or admin-authored Content Type DSL is introduced initially.

Bounded code defines compatibility semantics.

#### Historical Approval vs current selectability

A Template Version may remain historically correctly approved while becoming unselectable for new authoring because its approved Content Type contract is incompatible with the current contract.

Historical Approval is never rewritten merely to express current incompatibility.

A successor Template Version is approved under an appropriate newer contract where required.

#### Old contract readers remain interpretable

Historical records may continue referencing old contract revisions after new authoring has moved on.

Old revision interpreters/descriptions must remain available while governed history requires interpretation.

Old revisions may be disallowed for new authoring without becoming unreadable history.

#### Unsupported old revisions fail closed

If an operation requires interpreting a historical Content Type contract revision and the running code cannot interpret it, NewYou fails closed rather than substituting the current revision.

Stored immutable evidence remains untouched.

#### Revision versus new Content Type identity

A revision evolves the same conceptual business Content Type.

If the business meaning becomes materially different, a new stable governed type key is required rather than hiding a new concept behind an old identity.

#### Extensible means governed code extension, not arbitrary editor creation

`DEC-128` extensibility initially means demonstrated content need can add a new governed code-defined Content Type contract through normal review/deployment.

It does not imply runtime editor-created arbitrary types.

#### No ContentType database authority initially

Current requirements are satisfied by:

```text
code-authoritative catalogue
+
stable type keys
+
explicit contract revisions
+
explicit compatibility semantics
+
exact provenance on governed records
```

No `ContentType`, `ContentTypeVersion` or `ContentTypeApproval` Resource is introduced initially.

#### Approval policy remains separate

`GRILL-26` remains controlling.

Content Type contracts may contribute classification facts used by approval-policy derivation but do not become a free-form Approval policy engine.

#### Template-governed draft pins both contracts

A Template-governed active shared draft therefore has exact governance pins to:

```text
Content Type contract revision
+
ContentTemplateVersion
+
code-authoritative block contracts
```

Current catalogue changes cannot silently alter that in-progress draft.

#### Beacon

Beacon provides no direct donor for this governed Content Type contract model.

### 6.86 ACCEPTED GRILL DECISION

#### `GRILL-27 — Governed Content Types Are Code-Authoritative, Explicitly Revision-Addressable Contracts; Historical Approval and Current Compatibility Are Separate`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> NewYou initially implements its `DEC-128` controlled/extensible Content Type catalogue as code-authoritative governed contracts rather than mutable runtime ContentType/ContentTypeVersion database authority.
>
> Each Content Type has a stable governed type key and an explicit immutable contract revision identifier. Application release/Git SHA is not the Content Type contract identity.
>
> A Content Type contract contains only the bounded governed semantics contributed by that type, such as permitted structural/block capabilities, required/allowed metadata semantics, type-specific validation/invariants, Template compatibility boundaries and type-owned workflow/risk capability classification. It does not duplicate block implementation, Approval evidence, Publication truth, Translation lifecycle or Template-specific constraints.
>
> Content Type contracts provide the broad permitted content envelope. Template Versions may narrow that envelope but may not expand it. Effective validity remains the intersection of Content Type, Template and code-authoritative block/block-slot contracts.
>
> Each `ContentTemplateVersion` retains the exact Content Type key + contract revision that formed its approval/validation basis. Historical Template Approval remains attached to that exact immutable Template Version and is never rewritten merely because the Content Type contract later advances.
>
> Each immutable `ContentVersion` likewise retains the exact Content Type contract revision against which its governed shared content was validated, so historical content interpretation does not depend on mutable/current type semantics.
>
> Active shared `ContentDraft` authoring is pinned to one exact Content Type contract revision. A new catalogue-current revision does not silently reinterpret or migrate an active draft. Adoption of a newer contract revision requires an explicit validated migration/rebase operation; exact mechanics remain JIT.
>
> `ContentLocaleDraft` and `ContentTranslationVersion` do not introduce an independent Content Type contract authority; their exact shared `ContentVersion` parent provides the relevant Content Type contract provenance.
>
> Any change to governed Content Type semantics that may affect validation, interpretation, Template compatibility, metadata requirements or type-contributed workflow behaviour creates a new contract revision even when the change is backward-compatible. Contract identity/provenance and compatibility are separate questions.
>
> Current Template selectability evaluates the exact contract revision used for Template approval against the current contract revision for the same stable Content Type key.
>
> Compatibility defaults fail closed: exact revision equality is compatible; differing revisions are incompatible unless an explicit deterministic code-defined compatibility rule states that the historical approved contract remains valid for new authoring under the current contract.
>
> Content Type compatibility is directional and is not inferred from names, structural similarity, apparent additive change or runtime data shape.
>
> Content Type compatibility rules remain bounded code-defined semantics. NewYou does not introduce a runtime ContentType migration/compatibility DSL or administrator-authored compatibility table without future evidence.
>
> Historical Approval and current selectability are separate. A Template Version may remain historically correctly approved while becoming currently unselectable because its approved Content Type contract is incompatible with the current contract.
>
> Where a Template Version is no longer compatible, NewYou does not mutate its historical Approval. A successor Template Version is validated/reviewed/approved against an appropriate newer Content Type contract.
>
> Old Content Type contract revisions remain interpretable for historical governed records while those records require interpretation, following a reader-before-writer/support principle. Old revisions may be unavailable for new authoring while remaining readable as history.
>
> Unknown or unsupported historical Content Type contract revisions fail closed for operations requiring interpretation and are never silently substituted with the current revision.
>
> Content Type contract revisions evolve one conceptual type. A materially different business content class requires a distinct governed Content Type key rather than hiding a new concept behind a revision number.
>
> The `DEC-128` catalogue remains extensible through governed code changes driven by demonstrated content needs. “Extensible” does not imply runtime editor-created arbitrary Content Types.
>
> No dedicated `ContentType`, `ContentTypeVersion` or `ContentTypeApproval` Resource is introduced initially because current requirements do not establish independent mutable/data-owned business truth that justifies them.
>
> `GRILL-26` Approval requirements remain independently governed. Content Type contracts may contribute type/risk/workflow classification facts but do not become a free-form Approval-policy engine.
>
> Template-governed draft validation uses the exact pinned Content Type contract revision, exact pinned `ContentTemplateVersion` and applicable block contracts together. Current catalogue changes cannot silently alter an in-progress governed draft.
>
> This decision resolves the semantic `EXPOSED-01` compatibility boundary for later C&M JIT adoption, but exact catalogue API/module design, contract representation, compatibility function shape and draft migration actions remain implementation/JIT details.
>
> Beacon provides **NO DIRECT DONOR** for this governed Content Type contract model.

### 6.87 Consequences fixed for later grills

1. Content Type catalogue is code-authoritative initially.
2. Each Content Type has stable key + explicit immutable contract revision.
3. Application release/Git SHA is not the contract identity.
4. Content Type contract owns bounded type-level semantics only.
5. Content Type is the broad envelope; Template may narrow but not expand it.
6. Template Versions retain exact type key + contract revision approval basis.
7. Immutable ContentVersions retain exact type-contract provenance.
8. Active ContentDrafts pin one exact type-contract revision.
9. Current type revision changes do not silently migrate active drafts.
10. Locale draft/version type provenance derives through exact shared ContentVersion.
11. Any governed semantic change creates a new contract revision.
12. Revision identity and compatibility are separate.
13. Current Template selectability compares historical approved revision to current revision.
14. Compatibility is explicit, deterministic and directional.
15. Exact revision equality is compatible.
16. Different revisions fail closed unless code explicitly permits compatibility.
17. No runtime/admin Content Type compatibility DSL/table initially.
18. Historical Approval remains true even if current selectability becomes false.
19. Incompatible historical Templates require successor Template Version for current authoring rather than Approval mutation.
20. Old contract revisions remain interpretable while governed history requires them.
21. Unsupported historical revisions fail closed rather than substituting current semantics.
22. Materially different business type meaning requires a new stable type key.
23. DEC-128 extensibility means governed code extension initially, not arbitrary editor-created types.
24. No ContentType/ContentTypeVersion/ContentTypeApproval Resource initially.
25. Content Type contract does not become an Approval-policy engine.
26. Template-governed drafts pin exact Content Type + Template + block contract semantics.
27. `EXPOSED-01` is semantically resolved for later authoritative C&M JIT adoption.
28. Block 3A.9 was subsequently resolved by `GRILL-28`; Block 3A.10 was subsequently resolved by `GRILL-29`; Block 3A.11 subsequently closed the branch under `GRILL-30`.

### 6.88 Block 3A.9 pressure test — Publication/Scheduling eligibility, activation and revalidation

Current NewYou authority establishes that:

- Content & Media owns publication truth;
- PostgreSQL is the durable authority for content versions, approvals and publication truth;
- publication activates a **specific approved locale/version**;
- latest, approved and published are distinct states;
- required high-risk/bilingual content is blocked from publication/delivery until its required approved locale variants exist;
- scheduled publication revalidates approval/current policy before publication;
- scheduled publication is durable, idempotent, observable and recoverable;
- a scheduler attempt never proves that content was published;
- published governed versions are immutable and later corrections use explicit supersession/withdrawal.

These constraints require Publication truth to be separate from both mutable drafts and operational scheduler attempts.

#### Publication activates one exact immutable locale version

For localised governed content, the publication target is one exact immutable `ContentTranslationVersion`, which already identifies its exact parent `ContentVersion`.

Conceptually:

```text
Publication
→ exact ContentTranslationVersion AF7
→ exact parent ContentVersion C8
```

Publication never dereferences:

- `ContentDraft`;
- `ContentLocaleDraft`;
- latest locale version;
- latest shared version;
- current Template Version.

A durable C&M Publication concept/Resource is justified by existing Domain/Platform authority. Exact Ash fields/topology remain JIT.

#### Publication is locale-specific truth

Publication activates the exact locale version users may receive for that publication/delivery scope.

Approval of or publication of another locale does not make the target locale published.

The language-version publication date is derived from/anchored by durable Publication truth rather than an independently mutable field that can contradict publication history.

Exact first-publication/re-publication date representation remains JIT.

#### Current-effective uniqueness

NewYou initially permits at most one current effective Publication for a given conceptual content identity + locale + equivalent publication scope.

A successor Publication may atomically become current and supersede the previously effective Publication for that scope.

The predecessor Publication remains historical evidence.

Exact publication-scope dimensions and persistence constraints remain JIT; this decision does not invent additional delivery channels/surfaces.

#### Publication eligibility is current, not historical-only

Immediate publication requires current eligibility at the authoritative transition.

At minimum that means:

- the exact immutable target is interpretable;
- all required scoped Approval evidence for that exact subject exists and is currently eligible under `GRILL-26`;
- any required sibling locale variants exist against the same exact shared `ContentVersion`;
- required translation/source alignment under `GRILL-23` is current;
- current Product/Domain policy permits publication/delivery;
- no current Correction/Withdrawal truth blocks the target;
- other explicit risk/access/content gates applicable to that target pass.

Historical Approval evidence is not rewritten when current eligibility fails.

#### Content Type and Template checks at publication

The target `ContentVersion` must remain interpretable under its exact pinned Content Type contract revision from `GRILL-27`.

However, **current Template selectability is not a publication gate**.

Templates are authoring scaffolds/provenance and have no live runtime inheritance after immutable content materialisation.

Likewise a newer current Content Type contract does not automatically invalidate an already-governed ContentVersion merely because the revision differs. Any current-policy prohibition must be explicit rather than inferred from Template/current-type drift.

#### Required bilingual / multi-locale gate

Where Product Law requires approved Afrikaans and English (or other required locales) before publication/delivery, the exact target may not publish unless the required sibling locale versions:

- belong to the same exact shared `ContentVersion`;
- have all required Approval evidence;
- satisfy required translation/source alignment.

The locale Publications themselves remain separate durable truths; this decision does not require simultaneous multi-locale activation unless later policy explicitly requires it.

For optional low-risk editorial content, the existing explicit fallback rule remains controlling: the selected locale may be unavailable only if the experience states that fact and explicitly offers an available approved language. Silent locale substitution remains prohibited.

#### Scheduling is durable intent, not Publication truth

A schedule records durable intent to attempt publication of one exact immutable target at an approved time/window.

Conceptually:

```text
Schedule intent
→ exact ContentTranslationVersion AF7
→ intended publication time/window

≠ Publication(AF7)
```

Scheduling never points to “latest”, “current draft” or “whatever is approved at execution time”.

The exact Resource representation of durable schedule intent remains OQ-016/JIT.

#### Scheduling requires eligibility before it is accepted

The current Operating Model orders risk/approvals before “published now or scheduled”.

Therefore NewYou does not use scheduling as a placeholder for unfinished/unapproved content.

At schedule creation, the exact target must satisfy the current publication-eligibility rules applicable at that time.

This does not waive later revalidation.

#### Execution-time revalidation is mandatory

When scheduled execution occurs, NewYou re-evaluates current eligibility for the same exact pinned target.

The schedule does not snapshot permanent permission to publish.

A previously valid scheduled target may therefore become ineligible because of:

- changed current policy/risk requirements;
- stale/ineligible Approval evidence under OQ-016/`GRILL-26`;
- required translation/source misalignment;
- Correction/Withdrawal;
- lost interpretability/support of required governed contract;
- another explicit current publication gate.

If revalidation fails, publication fails closed.

Historical Approval/schedule evidence remains intact.

#### Scheduler attempts never prove Publication

Execution of an Oban job, scheduler callback or retry is operational evidence only.

Publication exists only when the authoritative C&M Publication transition commits.

Therefore:

```text
scheduler attempt succeeded technically
≠
Publication truth exists
```

unless the authoritative publication transaction actually committed.

#### Durable failure/recovery and no silent rescheduling

Scheduled publication uses durable retry/reconciliation.

If it cannot complete within its approved publication window, the platform surfaces a visible operator exception/work item.

NewYou does not silently move editorial publication to a different future time.

Retries/reconciliation within the approved window may occur according to the later OQ-016 operational policy.

Explicit operator rescheduling is a new durable intent, not hidden mutation of history.

Exact retry limits, window semantics, alerts and ownership remain OQ-016.

#### Publication activation is idempotent

Retry, duplicate submission or lost acknowledgement cannot create duplicate logical Publication truth for the same semantic activation.

If the authoritative publication commit succeeds but confirmation is lost:

```text
retry/reconcile
→ resolve the already-committed Publication
```

rather than publish again.

Exact idempotency key/constraint design remains JIT.

#### Concurrent competing Publications fail closed

Two concurrent attempts to establish different current publications for the same content/locale/publication scope cannot both become authoritative current truth.

The authoritative transition must verify the expected current publication/state and serialize or conflict deterministically.

Generic last-write-wins is rejected.

If two attempts target the same semantic activation, idempotency resolves them to one logical result.

#### Successor publication creates effective supersession

Creating a successor content/locale candidate does not supersede the currently published version.

Approval of that successor also does not supersede current Publication.

Effective supersession occurs when the successor Publication becomes authoritative/current for the same publication scope.

Conceptually:

```text
AF6 currently published

AF7 exists
→ AF6 still current

AF7 approved
→ AF6 still current

Publication(AF7) commits
→ AF7 current
→ AF6 Publication becomes historically superseded
```

The historical AF6 Publication remains evidence.

#### Withdrawal is distinct from supersession

Withdrawal is explicit governed truth that removes affected published content from current delivery eligibility without erasing the original Publication.

A withdrawn Publication/version remains historically published-and-withdrawn.

If an urgent correction requires stopping unsafe content before a replacement is ready, withdrawal can remove current delivery authority before successor Publication exists.

A later successor Publication does not rewrite the old withdrawal.

#### Correction creates successor immutable truth

A material correction follows the existing immutable-version rules.

It produces successor immutable shared/locale truth as applicable, obtains required Approval, and is published explicitly.

The old published version is never edited in place.

Where the corrected successor becomes current Publication, the predecessor is superseded unless it was already separately withdrawn.

**Historical at GRILL-28 acceptance:** exact correction classification/reason/impact propagation was the next seam. `GRILL-29` subsequently resolved the durable Correction/Withdrawal declaration and downstream-ownership boundary; exact classification vocabulary and impact-propagation implementation remain JIT/downstream detail.

#### No automatic unwithdrawal / re-publication semantics invented

This decision does not assume that a previously withdrawn exact locale version can simply become current again.

If future requirements permit re-publication of withdrawn content, the exact governance/evidence rules must be explicit.

#### Failed/refused attempts require evidence but not another business authority

A blocked or technically failed scheduled attempt must leave enough durable operational/audit evidence to explain non-publication and support recovery.

It does not itself create Publication truth.

This decision does not yet justify a separate `PublicationAttempt` business Resource.

Exact scheduler/attempt evidence shape remains OQ-016/JIT.

#### Publication transaction stays small

The authoritative publication transition should coherently:

```text
verify exact target
revalidate current eligibility
verify expected current Publication
establish new Publication truth
establish effective supersession where applicable
establish idempotency
COMMIT
```

External notifications, search indexing, cache invalidation, CDN work and other fan-out are durable downstream consequences, not proof of Publication.

Derived system failure cannot invent or erase C&M Publication truth.

#### Delivery respects current authoritative Publication/Withdrawal truth

Search indexes, caches, generated routes and other projections do not become publication authority.

Where a projection is stale or invalidation is delayed, current authoritative Publication/Withdrawal policy must still prevent unsafe new delivery where required by the platform's delivery/access design.

Exact shared edge/cache mechanics remain `OQ-014` rather than being invented here.

#### OQ-016 status after this seam

This decision materially resolves the **semantic eligibility/revalidation/publication-authority boundary** needed by OQ-016.

It does not close OQ-016 itself.

Still open for the authoritative Operations/Architecture Review are:

- scheduler reliability mechanism;
- retry policy;
- approved-window mechanics;
- alert/operator ownership;
- exact durable failure/recovery evidence;
- reconciliation implementation;
- exact Ash/Oban Resource/action topology.

#### Beacon

Beacon's page-event/snapshot distinction remains useful conceptual evidence that editable working state is not published state.

Beacon's event/snapshot persistence and simple publish/unpublish lifecycle are not sufficient NewYou authority and remain rejected for direct reuse.

### 6.89 ACCEPTED GRILL DECISION

#### `GRILL-28 — Publication Activates One Exact Eligible Locale Version; Scheduling Pins Exact Intent and Revalidates Before Activation`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> Content & Media owns durable Publication truth. Publication activates one exact immutable `ContentTranslationVersion` in the context of its exact parent `ContentVersion`; it never dereferences mutable drafts, `latest`, current Template state or other moving pointers.
>
> Publication is locale-specific durable truth. Approval/publication of one locale never makes another locale published.
>
> NewYou initially permits at most one current effective Publication for a conceptual content identity + locale + equivalent publication scope. Successor publication establishes a new current Publication and effective supersession while preserving predecessor Publication history. Exact scope dimensions remain JIT.
>
> Immediate publication requires current eligibility at the authoritative transition: exact subject interpretability, complete currently eligible scoped Approval evidence, required same-ContentVersion sibling locale approvals/alignment, current translation/source alignment, applicable current policy/risk gates, and absence of blocking Correction/Withdrawal truth.
>
> Current Template selectability is not a publication gate because Templates are authoring scaffolds/provenance rather than live runtime publication authority. The exact pinned Content Type contract must remain interpretable, but mere existence of a newer Content Type revision does not itself invalidate historical governed content.
>
> Required bilingual/multi-locale content cannot publish until all policy-required locale variants against the same exact shared ContentVersion satisfy their applicable Approval/alignment gates. Locale Publication truth remains independent unless later policy explicitly requires atomic simultaneous activation.
>
> Optional low-risk fallback remains limited to the existing explicit rule: state that the selected translation is unavailable and explicitly offer an available approved language. Silent fallback remains prohibited.
>
> Scheduling is durable publication intent, not Publication truth. A schedule pins one exact immutable locale version and approved execution time/window and never follows latest/current.
>
> Schedule creation requires the exact target to be currently publication-eligible. Scheduling is not a mechanism for reserving publication of unfinished/unapproved content.
>
> Scheduled execution revalidates current eligibility for the same exact pinned target. Scheduling does not snapshot permanent permission to publish.
>
> If execution-time approval/policy/translation/withdrawal/interpretability checks fail, publication fails closed; historical Approval and schedule evidence are not rewritten.
>
> Scheduler/job execution never proves Publication. Only successful authoritative C&M publication commit establishes Publication truth.
>
> Scheduled publication uses durable retry/reconciliation and is observable. If publication cannot complete within its approved window, a visible operator exception/work item is required. NewYou does not silently reschedule editorial work.
>
> Publication activation is idempotent. Retry, duplicate submission and lost acknowledgement cannot multiply logical Publication truth.
>
> Concurrent attempts to establish competing current Publications for the same scope cannot both succeed. Generic last-write-wins is rejected; expected-state/concurrency protection is required.
>
> A successor candidate or Approval does not supersede existing Publication. Effective supersession occurs only when successor Publication becomes authoritative/current.
>
> Withdrawal is separate explicit governed truth that removes affected publication/delivery eligibility without erasing the historical fact that the content was published.
>
> Material corrections create successor immutable governed content. When the corrected successor is published it supersedes the predecessor Publication unless the predecessor was already separately withdrawn. The predecessor is never edited in place.
>
> This decision does not invent automatic re-publication/unwithdrawal of a previously withdrawn exact locale version.
>
> Failed/refused scheduler attempts require durable operational/audit evidence sufficient for diagnosis/recovery but do not create Publication truth and do not yet justify a dedicated `PublicationAttempt` business Resource.
>
> The authoritative Publication transaction remains small: revalidate exact target/current eligibility, verify expected current publication state, establish Publication/supersession/idempotency atomically, then trigger durable downstream consequences outside that authority transaction.
>
> Search/cache/CDN/PubSub/UI projections never become Publication authority.
>
> This decision materially resolves OQ-016's semantic publication eligibility/revalidation boundary for later authoritative adoption but does not itself close OQ-016 or specify scheduler reliability/retry/alert/recovery implementation.
>
> Beacon provides conceptual snapshot/publication-boundary evidence only and **NO DIRECT DONOR** for NewYou's Publication/Scheduling authority model.

### 6.90 Consequences fixed for later grills

1. Publication is durable C&M authority separate from drafts, Approval and scheduler attempts.
2. Publication targets one exact ContentTranslationVersion + exact parent ContentVersion.
3. Publication never follows latest/current/mutable draft pointers.
4. Publication truth is locale-specific.
5. One current effective Publication per content identity + locale + equivalent publication scope initially.
6. Successor current Publication preserves predecessor Publication history.
7. Immediate publication revalidates complete current eligibility.
8. Current Template selectability is not a publish-time gate.
9. Pinned Content Type contract interpretability is required; current revision drift alone is not invalidation.
10. Required sibling locales must belong to the same shared ContentVersion.
11. Required locale variants must satisfy Approval and translation/source-alignment gates.
12. Locale publication remains independent unless future policy explicitly requires atomic activation.
13. Optional low-risk fallback remains explicit/non-silent only.
14. Schedule intent pins one exact immutable target.
15. Schedule creation requires current eligibility.
16. Scheduled execution revalidates current eligibility.
17. Schedule intent never proves Publication.
18. Failed execution fails closed.
19. Scheduled publication uses durable retry/reconciliation and observable failure handling.
20. Missed approved window requires visible operator exception; no silent reschedule.
21. Publication is idempotent under retry/duplicate/lost acknowledgement.
22. Competing current Publications require durable concurrency protection; no last-write-wins.
23. Successor candidate/Approval does not supersede existing Publication.
24. Successor Publication establishes effective supersession.
25. Withdrawal preserves historical Publication while removing current delivery eligibility.
26. Material correction creates successor immutable truth, never in-place edit.
27. No automatic unwithdrawal/re-publication semantics are introduced.
28. Failed/refused attempts need durable evidence but no PublicationAttempt Resource is justified yet.
29. Publication transaction is short/coherent; external fan-out follows after commit.
30. Derived caches/search/CDN/PubSub/UI never become Publication authority.
31. OQ-016 semantic eligibility/revalidation boundary is materially answered but governed OQ-016 remains open.
32. Block 3A.10 was subsequently resolved by `GRILL-29`; Block 3A.11 must now decide whether the full version/translation/review/approval/publication/correction branch is semantically closed for JIT handoff.

### 6.91 Block 3A.10 pressure test — Correction/Withdrawal declaration and downstream impact ownership

Current NewYou authority defines `FLOW-11` as:

```text
safety-critical correction/withdrawal
→ dependency discovery
→ invalidation
→ operational/participant response
→ audit
```

Reference-flow pressure tests further require safety-critical withdrawal to remain effective when caches/search lag, downstream providers fail, dependency fan-out partially completes or concurrent requests still reference older content.

This requires a hard separation between authoritative C&M correction/withdrawal truth and downstream owner-mediated consequences.

#### Correction, Withdrawal and supersession are distinct facts

A **Correction** records that one exact immutable governed subject contains a defect requiring explicit corrective treatment.

A **Withdrawal** records that one exact immutable governed subject is no longer eligible for continuing/new governed delivery according to its affected scope.

**Supersession** records that a successor Publication has become effective/current for the same publication scope.

These concepts are related but not interchangeable.

#### Correction may exist without immediate withdrawal

A low-impact defect may be corrected through a successor version while the predecessor remains temporarily deliverable where governing policy permits.

A safety-critical defect may require immediate Withdrawal before a successor exists.

Therefore Correction cannot be represented only as a successor relationship, and Withdrawal cannot be inferred merely from the existence of a Correction.

#### Narrowest exact immutable subject owns defect scope

Correction/Withdrawal attaches at the narrowest exact immutable subject that contains the defective truth.

Examples:

```text
shared/invariant defect
→ exact ContentVersion

locale wording defect
→ exact ContentTranslationVersion
```

This avoids both under-withdrawal and false sibling defects.

#### Shared-version withdrawal affects all children

Withdrawal of an exact shared `ContentVersion` makes every locale version under that shared version ineligible for new Publication/delivery.

Those child locale versions are not individually rewritten; their current eligibility derives from the withdrawn shared parent.

#### Locale withdrawal remains locale-local as defect truth

Withdrawal of one exact `ContentTranslationVersion` does not claim sibling locale versions contain the same defect.

However, a required bilingual/multi-locale release policy may make an otherwise valid sibling temporarily undeliverable because the aligned required release set is incomplete.

That is derived release eligibility, not fabricated sibling Withdrawal truth.

#### Immutable governed content is never corrected in place

Corrections flow through mutable draft authoring and successor immutable version creation.

The defective predecessor remains exact historical evidence of what existed and may have been delivered.

#### Correction may precede the successor

Urgent incident handling may require:

```text
defect discovered
→ Correction declared
→ optional/immediate Withdrawal
→ corrected draft/version created later
```

Therefore Correction is a durable fact independent of successor availability.

When a corrective successor exists, explicit corrective lineage distinguishes it from ordinary editorial predecessor lineage.

#### Corrective successor does not bypass governance

A successor that corrects prior content still undergoes the applicable Review, Approval and Publication path.

A reduced minor-correction path may exist only where governing policy explicitly authorises it.

#### Withdrawal history is not erased

Withdrawal remains historical truth and is not “unwithdrawn in place”.

Any later lawful availability requires a new explicit governed publication decision under later policy/JIT rules.

This seam does not decide whether exact same-version re-publication is ever permitted.

#### Machine-readable impact classification is required

Downstream automation must not parse free-form human rationale to decide whether Plans, Communications or Safety actions are required.

Correction/Withdrawal therefore carries a bounded machine-interpretable impact/severity classification or equivalent governed routing facts, plus human rationale/evidence.

Exact vocabulary remains JIT/authority work.

#### Defect impact differs from baseline content risk

A normally low-risk Content Item may have a severe safety defect.

A generally high-risk item may have a trivial typo.

Therefore correction impact/severity is not inferred solely from baseline Content Item risk classification.

#### Withdrawal becomes authoritative before fan-out completes

Once an authoritative Withdrawal commits, the affected exact content is no longer eligible for governed new/continuing delivery according to that scope.

Search removal, cache/CDN purge, provider callbacks, dependency scans and participant communications may complete afterward.

Derived-system delay or failure cannot keep withdrawn content authorised.

#### Stale projection state cannot re-authorise content

Search indexes, caches, CDN state, PubSub and UI projections never become Correction/Withdrawal authority.

A stale index/cache that still references withdrawn content cannot establish delivery permission.

Current authoritative Publication/Withdrawal/access rules remain controlling.

#### Dependency discovery uses governed provenance/relationships

Downstream durable records that materially depend on governed content preserve sufficient exact content/version provenance to make the dependency reproducible.

Dependency discovery must not rely on textual search, search-index matches or guessed relationships.

A reverse dependency index may accelerate discovery but cannot become the only authority proving that another Domain's durable record depends on content.

#### Content does not own downstream business truth

Content & Media owns:

```text
Correction / Withdrawal truth
exact affected subject
effective time
bounded impact classification
explanatory evidence
```

It does not directly own:

- Plan validity/adjustment;
- participant safety state;
- communication delivery;
- entitlement validity;
- payment/refund state;
- professional-care case state;
- programme/challenge state.

Cross-domain mutation invokes the owning Domain.

#### Downstream owners decide their consequences

The exact Correction/Withdrawal fact plus bounded impact context is handed to the affected owning Domain.

That Domain applies its own approved policy and records its own durable remediation/invalidation truth.

Content & Media does not directly write another Domain's state.

#### Historical downstream records are not rewritten

A Plan/report/message previously created from now-withdrawn content remains historical truth.

Its owning Domain decides whether it becomes invalid for future use, needs a successor, requires participant warning, or needs some other response.

Content withdrawal never silently rewrites historical downstream business records.

#### Safety-critical delivery fails closed during fan-out lag

For safety-critical dependencies, local projection lag must not allow unsafe new governed delivery.

The owning delivery path must have an authoritative correctness path or bypass sufficient to observe current withdrawal/eligibility state until durable local remediation catches up.

Exact mechanism remains JIT.

#### Offline/external delivery cannot be physically erased

Withdrawal stops future governed eligibility but cannot magically retract content already present in sent email, downloaded PDFs, printed material or external provider payloads.

Where response is required, affected-use discovery and owner-mediated operational/participant remediation are explicit downstream consequences.

#### Communications / Safety / Plans retain ownership

A withdrawal may trigger:

```text
Communications
→ owns message intent / send / delivery / retry truth

Safety & Eligibility
→ owns participant safety decisions

Plans & Nutrition
→ owns plan validity / successor / adjustment
```

The C&M fact is input/provenance, not their authority.

#### Fan-out must be durable and resumable where must-not-lose

Safety-critical/high-impact correction/withdrawal cannot rely on fire-and-forget PubSub.

Must-not-lose consequences require durable, idempotent, resumable and reconcilable orchestration/evidence.

This seam does not require a generic global `ContentImpactTask` or workflow engine.

Exact representation remains AR-005/JIT.

#### Cross-domain handoffs are idempotent

The exact Correction/Withdrawal identity accompanies downstream handoffs.

Retries must not multiply logical remediation effects.

Each owner handles the same exact source fact idempotently.

#### Transport ordering is not business ordering

Downstream consumers cannot trust arrival order of:

```text
Withdrawal(old)
Publication(successor)
```

or other related messages.

Where current state matters, consumers reconcile against exact source/owner state rather than deriving authority solely from transport order.

#### Correction/Withdrawal evidence remains interpretable

Durable evidence preserves conceptually:

- exact affected immutable subject;
- disposition type;
- effective time;
- authorised actor/authority;
- bounded impact/severity classification;
- human rationale/evidence;
- later corrective/replacement lineage where established.

Exact fields/resources remain JIT.

#### Audit & Evidence remains evidence, not source authority

Audit & Evidence may preserve cross-cutting evidence around the flow.

It does not replace C&M Correction/Withdrawal truth or another Domain's remediation truth.

#### Beacon

Beacon `unpublished` PageEvent semantics are insufficient for this model.

They do not model defect scope, correction versus withdrawal versus supersession, impact/severity, dependency discovery, owner-mediated consequences or durable partial-fan-out recovery.

There is no direct donor.

### 6.92 ACCEPTED GRILL DECISION

#### `GRILL-29 — Correction, Withdrawal and Supersession Are Distinct Durable Truths; Content Owns the Declaration While Dependent Domains Own Their Consequences`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> Content & Media distinguishes Correction, Withdrawal and effective supersession rather than collapsing them into one mutable lifecycle field.
>
> A **Correction** is durable evidence that one exact immutable governed content subject contains a defect or error requiring explicit corrective treatment. Correction does not by itself necessarily remove current delivery eligibility.
>
> A **Withdrawal** is durable authoritative truth that one exact immutable governed content subject is no longer eligible for new/continuing governed publication or delivery according to its affected scope. Withdrawal can become effective before a corrected successor exists.
>
> **Supersession** is the effective relationship created when a successor Publication becomes current for the same publication scope. A successor candidate, Correction declaration or Approval does not itself establish supersession.
>
> Correction/Withdrawal attaches at the narrowest exact immutable subject containing the affected truth. A shared/invariant defect may target exact `ContentVersion`; a locale-wording defect may target exact `ContentTranslationVersion`.
>
> Withdrawal of an exact shared `ContentVersion` makes all locale versions under that shared version ineligible for new Publication/delivery. Withdrawal of one locale version does not falsely mark sibling locale versions as defective.
>
> Governing release policy may nevertheless make an otherwise-valid sibling locale currently undeliverable when a required aligned locale is withdrawn. That is derived release eligibility, not fabricated sibling Withdrawal truth.
>
> Published or otherwise immutable governed content is never edited in place to perform a correction. Corrective authored changes produce successor immutable shared/locale versions through the existing draft/version-cut/governance path.
>
> Correction may be declared before a corrective successor exists. When a successor is later established, corrective lineage is explicit and distinguishable from ordinary predecessor/editorial evolution.
>
> A corrective successor does not bypass applicable Review, Approval or Publication. Any controlled reduced correction path must remain explicitly authorised by governing policy.
>
> Withdrawal truth is historical and is never destructively erased or “unwithdrawn in place”. Any later lawful availability must be established through a new explicit governed publication decision; exact same-version re-publication permissibility remains downstream policy/JIT.
>
> Correction/Withdrawal retains bounded machine-interpretable impact/severity classification sufficient for safe routing plus human rationale/evidence. Downstream automation does not infer criticality or required response solely from free-form reason strings.
>
> Correction impact/severity is distinct from the content item's baseline risk classification. The defect itself may have materially different urgency from the content's normal risk category.
>
> Authoritative Withdrawal becomes effective independently of completion of cache/search invalidation, dependency fan-out, provider operations or participant communications. Derived-system failure cannot keep withdrawn content authorised.
>
> Search indexes, caches, CDN state, PubSub and other projections never become Correction/Withdrawal authority. Stale projection state cannot authorise new delivery of withdrawn content.
>
> Durable business records in other Domains that materially depend on governed content retain sufficient exact content/version provenance to identify that dependency. Dependency discovery is based on governed relationships/provenance, not search-index heuristics or textual matching.
>
> Content & Media does not become a universal owner of downstream dependency truth. The dependent Domain owns its own durable records and their exact content references. A derived reverse dependency index may accelerate discovery but cannot become the sole authority for the relationship.
>
> Content & Media owns the exact Correction/Withdrawal fact and a bounded machine-readable impact handoff. It does not directly mutate Plans, Safety & Eligibility, Communications, Commerce, Entitlements, Professional Care or other downstream business truth.
>
> Cross-domain consequences invoke the owning Domain. Each owner evaluates the exact content impact plus its own governing policy and establishes its own durable remediation/invalidation truth.
>
> Content & Media correction/withdrawal does not rewrite historical downstream records. Already-generated/delivered Plans, reports, communications or other records remain historical truth; their owning Domains determine any successor, invalidation, pause, warning or remediation.
>
> For safety-critical dependencies, derived-state lag must not permit unsafe new governed delivery. Owning delivery paths must be able to fail closed against current authoritative withdrawal/eligibility state even while local projections/fan-out catch up. Exact implementation mechanism remains JIT.
>
> Withdrawal cannot physically retract already-delivered offline/external content. Where participant or operator remediation is required, affected-use discovery and owner-mediated response occur as explicit durable consequences.
>
> Communications owns message intent/delivery; Safety & Eligibility owns participant safety truth; Plans owns plan validity/adjustment; other Domains retain equivalent ownership. A content withdrawal may trigger those workflows but never silently becomes their business authority.
>
> Safety-critical/high-impact Correction/Withdrawal consequence propagation is durable, idempotent, resumable and reconcilable. PubSub/fire-and-forget delivery is insufficient where must-not-lose downstream action is required.
>
> Exact Correction/Withdrawal identity is carried through downstream handoffs so retries cannot multiply logical remediation effects.
>
> Downstream consumers do not infer final business state from event arrival order alone. Where current state matters they reconcile against exact authoritative source/owner state.
>
> Correction/Withdrawal preserves exact target, effective time, authority/actor, bounded impact classification, explanatory evidence and any later corrective/replacement lineage required for interpretation. Exact Resource/field representation remains JIT.
>
> Audit & Evidence may retain cross-cutting evidence, but it does not replace Content & Media's Correction/Withdrawal truth or another Domain's remediation truth.
>
> Beacon `unpublished` PageEvent semantics are **REJECTED** as NewYou Correction/Withdrawal authority and provide **NO DIRECT DONOR** for this cross-domain safety model.

### 6.93 Consequences fixed for later grills

1. Correction, Withdrawal and supersession are separate durable facts.
2. Correction does not automatically imply Withdrawal.
3. Withdrawal may precede a corrected successor.
4. Supersession occurs only when successor Publication becomes current.
5. Defect scope attaches at the narrowest exact immutable subject.
6. Shared ContentVersion Withdrawal invalidates new delivery for all child locale versions.
7. Locale Withdrawal does not fabricate sibling defects.
8. Release policy may derive sibling delivery ineligibility without sibling Withdrawal.
9. Corrective edits always use successor immutable versions.
10. Correction can exist before replacement content.
11. Corrective lineage is distinct from ordinary predecessor lineage.
12. Corrective successors still require applicable governance.
13. Withdrawal history is never destructively erased.
14. No automatic unwithdraw-in-place semantics are introduced.
15. Machine routing uses bounded impact/severity classification, not free-form reason parsing.
16. Defect impact/severity is separate from baseline content risk.
17. Withdrawal authority becomes effective before downstream fan-out completes.
18. Cache/search/CDN/PubSub lag cannot re-authorise withdrawn content.
19. Dependency discovery uses exact governed provenance/relationships.
20. Reverse dependency indexes may accelerate but never become sole authority.
21. Content & Media owns impact declaration, not downstream business truth.
22. Cross-domain consequences invoke each owning Domain.
23. Historical downstream records are not silently rewritten.
24. Safety-critical delivery must fail closed despite derived-state lag.
25. Offline/external copies require remediation rather than imaginary physical retraction.
26. Communications/Safety/Plans and other Domains retain their own authority.
27. Must-not-lose fan-out is durable, idempotent, resumable and reconcilable.
28. PubSub/fire-and-forget alone is insufficient for critical consequences.
29. Exact Correction/Withdrawal identity supports idempotent downstream handoffs.
30. Event arrival order is not business authority.
31. Correction/Withdrawal evidence remains interpretable with target/time/authority/impact/rationale/lineage.
32. Audit & Evidence does not replace source-domain truth.
33. No generic ContentDependency / ContentImpactTask / universal workflow authority is introduced by this decision.
34. Block 3A.11 must assess whether the Content Version / Translation / Review / Approval / Publication / Correction branch is semantically closed for JIT handoff.

### 6.94 Block 3A.11 closure pressure test — semantic readiness for C&M JIT handoff

This seam re-evaluates `GRILL-20` through `GRILL-29` as one coherent authority/lifecycle chain rather than asking for another automatic architecture expansion.

#### Closure chain

The accepted branch now establishes:

```text
ContentItem
│
├── ContentDraft
│      mutable shared authoring authority
│      exact revision / single-active / explicit abandonment
│
├── ContentVersion
│      immutable shared governed truth
│
│      └── ContentLocaleDraft
│              mutable locale authoring authority
│              │
│              ├── TranslationWork
│              │      durable translation coordination / source intent
│              │
│              └── ContentTranslationVersion
│                     immutable locale governed truth
│                     │
│                     ├── Review evidence
│                     ├── scoped Approval evidence
│                     └── Publication truth
│
└── Correction / Withdrawal
       exact immutable affected subject
       │
       └── owner-mediated downstream consequences

effective successor Publication
→ supersession
```

No accepted concept in that chain requires another concept to become its competing authority.

#### Mutable versus immutable boundaries are closed

`GRILL-20`, `GRILL-21` and `GRILL-25` establish:

- mutable drafts versus immutable governed versions;
- exact version-cut boundary;
- exact-revision concurrency;
- idempotent version cuts;
- single-active mutable authority;
- explicit abandonment;
- no process-local correctness authority.

Exact Ash locking/index/action syntax can change implementation without changing those ownership semantics.

#### Shared versus locale authority is closed

`GRILL-22` through `GRILL-24` establish:

- shared structural/invariant authority in `ContentVersion`;
- locale-localisable immutable truth in `ContentTranslationVersion`;
- mutable locale authoring as a subordinate durable concern;
- exact source provenance where translation exists;
- derived translation staleness;
- durable `TranslationWork` coordination without making work records own wording.

No remaining translation question requires a new semantic owner before JIT.

#### Review / Approval / readiness is closed

`GRILL-26` establishes:

- Review as durable workflow/evaluation evidence;
- Approval as separately durable scoped affirmative evidence;
- current readiness/eligibility as derived;
- no overloaded version `status = approved` authority;
- shared versus locale approval attachment at the narrowest complete immutable subject.

Exact Review/Approval Resource/table decomposition remains implementation design, provided these semantics survive.

#### Content Type compatibility is closed semantically

`GRILL-27` establishes:

- code-authoritative Content Type contracts;
- stable keys + explicit immutable revisions;
- exact historical contract provenance;
- directional fail-closed compatibility;
- historical Approval distinct from current selectability.

`EXPOSED-01` is therefore semantically resolved. Exact catalogue/API implementation remains JIT.

#### Publication / Scheduling is closed semantically

`GRILL-28` establishes:

- Publication as durable locale-specific activation truth;
- exact immutable publication target;
- durable schedule intent separate from Publication;
- eligibility at schedule creation and execution-time revalidation;
- idempotent/concurrency-safe activation;
- historical Publication distinct from supersession/withdrawal;
- scheduler/job attempts are not business publication authority.

`OQ-016` remains open only for the governed operational/implementation concerns it actually owns.

#### Correction / Withdrawal / downstream ownership is closed semantically

`GRILL-29` establishes:

- Correction, Withdrawal and supersession as distinct durable facts;
- narrowest exact defect scope;
- withdrawal correctness independent of projection/fan-out lag;
- bounded machine-readable impact facts rather than free-form automation;
- exact provenance-based dependency discovery;
- owning downstream Domains establish their own remediation truth;
- durable/idempotent/reconcilable safety-critical fan-out.

`FLOW-11` still requires proof. That proof does not require inventing another C&M owner before JIT.

#### No architecture contradiction found

The closure audit found no unresolved semantic contradiction requiring another GRILL across:

- `ContentDraft`;
- `ContentLocaleDraft`;
- `ContentVersion`;
- `ContentTranslationVersion`;
- `TranslationWork`;
- Review;
- Approval;
- Publication;
- Correction;
- Withdrawal;
- supersession.

Remaining questions can be answered without changing the accepted owner of durable truth.

#### Remaining OQs/proof remain open at the correct authority level

The dossier must not claim closure of governed work it does not own.

In particular:

- `OQ-013` remains Architecture Review for exact Ash translation-resource boundaries, approval relationships, locale/version indexes and immutable delivery references;
- `OQ-016` remains Operations / Architecture Review for scheduler reliability, retry policy, alert ownership, stale-approval operations and recovery;
- `FLOW-11` remains a cross-domain safety-critical proof obligation;
- `EXPOSED-02` remains JIT formalisation of the already accepted validation-ownership baseline.

The dossier supplies architecture-discovery evidence to those gates; it does not close them.

#### Remaining choices are JIT / policy / operations, not new branch semantics

Examples include:

- exact Ash module/resource names;
- exact Resource decomposition for Review, Approval, schedule intent, Correction and Withdrawal;
- attributes/relationships/indexes/constraints;
- transaction/action/code-interface syntax;
- optimistic locking/idempotency-key representation;
- TranslationWork operational state vocabulary;
- Approval-requirement persistence;
- correction impact/severity vocabulary;
- exact publication-scope persistence dimensions;
- same-version re-publication after withdrawal policy;
- retention windows;
- Oban scheduler/retry/backoff/alert/reconciliation mechanics;
- reverse-dependency acceleration;
- cross-domain durable handoff/outbox/orchestration representation;
- FLOW-11 owner-specific remediation proof.

These can alter implementation shape but not the accepted source-of-truth boundaries.

#### No speculative Resources are justified merely for implementation mechanics

This branch does not justify introducing merely for convenience:

- `TranslationStaleness`;
- row-per-field `TranslationUnit`;
- provider-attempt business Resource;
- generic universal Task;
- generic `ContentDependency`;
- generic `ContentImpactTask`;
- global workflow engine;
- mutable runtime `ContentType` / `ContentTypeVersion` authority.

Search/cache/CDN projections, reverse indexes, Work Queue projections and PubSub remain derived mechanisms.

#### Capability-gated Template localisable defaults remain bounded

Substantive/localisable Template initial/default content remains capability-gated.

If unsupported, it fails closed.

If later supported, `GRILL-22`–`GRILL-24` already determine its shared-versus-locale ownership, so this does not require another branch-level architecture GRILL.

#### Documentation-integrity findings

The closure audit found several historical progression statements that still described now-resolved seams as currently `next`, `open` or `deferred`.

Those are documentation-integrity defects rather than architecture defects.

`v0.31.0` repairs them using the existing temporal convention:

```text
Historical at GRILL-X acceptance
→ subsequently resolved by GRILL-Y
```

No accepted architecture is changed by those repairs.

#### Closure outcome

Pre-repair review outcome:

**PASS WITH NON-BLOCKING CORRECTIONS**

After the consistency repairs in this revision:

**CLOSED / PASS FOR CONTENT & MEDIA JIT HANDOFF**

This means semantic discovery readiness only.

It does not authorise implementation, close OQ-013/OQ-016/FLOW-11, or bypass normal Feature Pack/JIT entry gates.

### 6.95 ACCEPTED GRILL DECISION

#### `GRILL-30 — The Content Version / Translation / Review / Approval / Publication / Correction Branch Is Semantically Closed for Content & Media JIT Handoff`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

> `GRILL-20` through `GRILL-29` provide sufficient semantic closure for the Content & Media mutable-authoring, immutable-version, locale/translation, Review/Approval, Publication/Scheduling and Correction/Withdrawal branch.
>
> The accepted chain establishes durable ownership for shared mutable authoring, immutable shared versions, mutable locale authoring, immutable locale versions, translation work, Review evidence, scoped Approval evidence, Publication truth and Correction/Withdrawal truth without collapsing independent lifecycle dimensions.
>
> No further architecture-discovery GRILL is required for this branch before Content & Media JIT unless new authoritative evidence, contradiction or materially changed scope appears.
>
> Exact Ash Resource decomposition, module names, fields, relationships, indexes, actions, transaction implementation and constraint syntax remain JIT decisions provided they preserve the accepted ownership and invariants.
>
> Exact representation may choose one or several Resources for durable concepts such as Review, Approval, schedule intent, Correction and Withdrawal where PostgreSQL referential integrity and bounded lifecycle design justify it. That representation choice may not redefine their accepted semantic ownership.
>
> `OQ-013` remains a governed Architecture Review gate. This dossier materially answers its Resource-boundary semantics but does not itself close the OQ, choose final Ash relationships/indexes or authorise implementation.
>
> `OQ-016` remains a governed Operations / Architecture Review gate. `GRILL-28` fixes Publication/Scheduling semantics but does not decide scheduler reliability technology, retry/backoff, approved-window handling, alert ownership, reconciliation or operational recovery.
>
> `FLOW-11` remains a proof obligation. `GRILL-29` fixes Content & Media declaration ownership and owner-mediated downstream consequence boundaries but does not prove each downstream Domain's remediation path or durable fan-out implementation.
>
> `EXPOSED-02` remains JIT formalisation of the already accepted validation-ownership baseline rather than an unresolved architecture branch.
>
> Exact Correction impact/severity vocabulary, TranslationWork operational states, Approval-requirement representation, publication-scope persistence dimensions, retention windows and same-version re-publication-after-withdrawal policy remain bounded JIT/policy decisions. Their conservative default is fail-closed; none currently changes the accepted authority owners.
>
> Substantive/localisable Template initial-content support remains capability-gated. If unsupported, it fails closed; if later supported, its ownership is already fixed by the shared/locale model and therefore does not require another branch-level architecture GRILL.
>
> No `TranslationStaleness`, per-field `TranslationUnit`, provider-attempt business Resource, generic Task, generic ContentDependency, ContentImpactTask, mutable ContentType authority or global workflow engine is justified merely to complete the implementation.
>
> Search/cache/CDN projections, reverse dependency indexes, Work Queue projections and PubSub remain derived acceleration/observation mechanisms and never become business authority.
>
> The current dossier repairs stale historical “next / open / deferred” statements during this closure revision so historical context remains explicit without contradicting subsequent accepted GRILLs.
>
> After those consistency repairs, this branch is **CLOSED / PASS FOR C&M JIT HANDOFF**. This status is semantic readiness only; it does not authorise implementation or close the platform's normal Feature Pack/JIT entry gates.
>
> Beacon provides no further branch-level semantic decision required here; subsequent work moves to the next distinct reuse area rather than continuing to elaborate this lifecycle.

### 6.96 Consequences fixed for later work

1. The entire Block 3A content-governance branch is CLOSED / PASS for semantic C&M JIT handoff.
2. No additional 3A GRILL is required absent new evidence, contradiction or materially changed scope.
3. GRILL-20–29 accepted owner/lifecycle/invariant semantics remain controlling inputs to JIT.
4. Exact Ash Resource decomposition may vary without changing semantic ownership.
5. Review/Approval/schedule/Correction/Withdrawal persistence topology is JIT, not another architecture-discovery branch.
6. OQ-013 remains governed/open until Architecture Review/JIT closes it.
7. OQ-016 remains governed/open until Operations/Architecture Review closes operational publication concerns.
8. FLOW-11 remains a proof obligation despite semantic C&M boundary closure.
9. EXPOSED-02 remains JIT formalisation rather than an unresolved branch semantic.
10. Exact locking/index/idempotency implementation remains JIT.
11. TranslationWork operational state vocabulary remains JIT.
12. Correction impact/severity vocabulary remains governed JIT/policy work.
13. Same-version re-publication after Withdrawal is not decided here and defaults fail closed.
14. Retention/deletion windows remain governed elsewhere.
15. Reverse dependency acceleration may be added without becoming dependency authority.
16. Durable cross-domain handoff/orchestration representation remains JIT.
17. No speculative generic workflow/dependency/task Resource is authorised by branch closure.
18. Substantive/localisable Template defaults remain capability-gated under already accepted ownership.
19. Historical stale progression wording is repaired without changing accepted architecture.
20. Subsequent Beacon reuse discovery moves to media lineage/storage rather than continuing Block 3A.

### 6.97 Block 4A.1 pressure test — authoritative media identity, derivative lineage and storage-provider boundary

Current NewYou authority is explicit:

- Content & Media owns governed editorial media identity, rights, derivatives and publication state;
- media identity is platform-owned and independent of provider/object IDs;
- masters, recordings and derivatives retain lineage;
- protected playback checks current platform authority before bounded delivery capability is issued;
- the governed Media Library preserves source/provenance, metadata, rights/attribution where applicable, derivatives, usage references and replacement/version semantics;
- material replacements preserve lineage and update references according to usage semantics.

This is sufficient to establish a dedicated durable media identity boundary without inventing provider-owned business truth.

#### Dedicated C&M media identity is justified

A durable governed media object needs an identity that survives provider/object-key changes, storage migration, CDN changes, derivative generation, rights/provenance changes, replacement, publication/withdrawal and usage/reference history.

The conceptual working name is `MediaAsset`; exact Ash module/name remains JIT.

```text
MediaAsset.id
≠ object key
≠ bucket + key
≠ CDN URL
≠ provider asset ID
```

#### PostgreSQL/Ash owns media authority; object storage owns bytes

```text
PostgreSQL / Ash
→ MediaAsset identity
→ provenance / rights / attribution
→ source / derivative lineage
→ publication / protected-delivery classification
→ replacement lineage
→ material governed metadata

external S3-compatible object storage
→ durable binary bytes
→ provider/object locator
```

The storage provider is a capability, not a Domain and not media authority.

#### Project-owner deployment direction: external S3-compatible storage

At `GRILL-31` acceptance, the project owner reiterated the intended deployment direction: NewYou will eventually offload media bytes to external S3-compatible object storage such as Wasabi to reduce application-server disk usage, server load and binary-storage burden.

This working dossier records that as a deployment-direction constraint while keeping the architecture provider-independent:

```text
required seam
→ external S3-compatible object storage

current likely provider direction
→ Wasabi or equivalent

business authority
→ NewYou PostgreSQL/Ash
```

A future provider change therefore does not require changing media business identity.

This note is project-owner direction captured in this non-authoritative discovery artifact; canonical governed implementation remains subject to normal JIT/Architecture adoption.

#### Storage locator is subordinate infrastructure state

A media asset may retain a provider/object locator sufficient to find its bytes. Exact representation may be an attribute, embedded structure or subordinate storage record.

Changing physical location during migration does not create a new `MediaAsset` identity unless the media itself is materially replaced.

#### Beacon provider-key map is not NewYou authority

Beacon's stable `Asset.keys` provider map is useful implementation inspiration only.

NewYou does not make an open provider-key map the source of media identity, publication, rights or delivery truth.

Nor does Beacon's support for multiple providers create a NewYou requirement for multi-provider replication.

#### Durable derivatives receive exact platform media identities

A derivative that may be independently referenced, governed, delivered, withdrawn, replaced or audited receives its own exact media identity.

```text
MediaAsset M1
role = master/source

├── MediaAsset M2
│   derivative_of = M1
│   role = thumbnail/responsive/etc
│
└── MediaAsset M3
    derivative_of = M1
    role = governed derivative
```

#### Source and derivative use one semantic media-asset concept initially

No separate `MediaDerivative` Resource is introduced solely because an asset is derived.

Both master/source and derivative are durable governed media objects.

A dedicated derivative Resource would require later evidence of materially different lifecycle/invariants.

#### Derivative lineage pins exact source

A derivative references the exact source `MediaAsset` that produced it.

It never means “derived from whichever asset is current now”.

Replacing M1 with M4 does not silently change historical lineage:

```text
M2 derivative_of M1
```

remains true.

New derivatives for M4 receive new identities.

#### Derivation does not automatically transfer governance

`derived_from` establishes provenance only.

It does not automatically grant rights, attribution sufficiency, publication, Approval or protected-delivery permission.

Those facts are evaluated according to the derivative's applicable policy.

This is especially important for full recordings, approved replays, promotional clips, captions and transcripts.

#### Captions/transcripts fit the lineage model where applicable

Architecture Law explicitly treats captions/transcripts as governed derivatives.

The same exact-source-lineage model can represent them without implying that every derivative class has identical processing or lifecycle semantics.

Exact derivative taxonomy remains later JIT work.

#### Material replacement creates a new media identity

An already-governed/referenceable media asset is not materially replaced by overwriting bytes behind the same identity.

Instead:

```text
M17
↓ replaced by
M22
```

M17 remains historical truth.

M22 becomes a distinct exact platform media identity.

#### No MediaItem → MediaAssetVersion hierarchy initially

**Historical at GRILL-31 acceptance; explicitly superseded by GRILL-36.** The text below is preserved as the accepted-at-the-time conclusion and is not current architecture-discovery guidance.


A separate stable parent/version hierarchy is not introduced merely because media can be replaced.

Exact asset-to-asset replacement lineage is sufficient initially.

If future relational/business requirements demonstrate a need for a stable media-family identity, that can be revisited at JIT/Architecture Review.

#### Usage references preserve exact historical truth

Immutable governed consumers reference exact `MediaAsset` identities and never silently follow replacement.

Mutable authoring may explicitly adopt a successor/replacement asset according to its own action semantics.

```text
published ContentVersion references M17
→ remains M17 historically

mutable ContentDraft
→ may explicitly replace M17 with M22
```

#### No shared-write usage authority

The consuming resource/Domain owns its own durable reference to the media asset.

Content & Media may maintain a derived reverse usage/dependency projection for editorial discovery, replacement and withdrawal operations.

That projection does not become the only authority proving the reference.

#### Material governance facts are first-class

Rights, attribution, provenance, publication, protected-delivery classification and withdrawal semantics are first-class governed facts where applicable.

They are not hidden in an unrestricted `extra` map.

Optional low-significance editorial metadata may later use a bounded extension mechanism if it does not create competing authority.

#### Storage/process success does not equal publication

Durable bytes uploaded successfully:

```text
≠ media approved
≠ media published
≠ media deliverable
```

Likewise provider capture or derivative-generation success does not create publication authority.

#### Protected delivery checks platform authority

For protected media:

```text
request exact MediaAsset
→ current media publication/withdrawal checks
→ Entitlement/sharing/consent checks where applicable
→ bounded delivery capability
```

Provider/object existence is never enough to authorise delivery.

Exact signed-URL/edge-token mechanics remain later JIT/OQ work.

#### Deletion remains distinct from storage-object removal

Media withdrawal/deletion business truth and provider-object deletion completion are separate facts.

Beacon's stable S3 `soft_delete/1` is incomplete and demonstrates why provider lifecycle cannot be imported as business lifecycle.

Full storage/processor/backup deletion and restore reconciliation remain governed by platform deletion architecture and open OQ-030/OQ-031 work.

#### Beacon reuse classification

| Beacon mechanism | NewYou classification |
|---|---|
| durable Asset identity | ADAPT |
| self-referencing source lineage | ADAPT — HIGH VALUE |
| named derivative usage/role | ADAPT CONCEPTUALLY |
| provider abstraction | ADAPT — HIGH VALUE |
| provider-specific locator | ADAPT CONCEPTUALLY |
| DB `file_body` binary storage as default | REJECT |
| open provider-key map as business authority | REJECT AS AUTHORITY |
| unrestricted `extra` map for material governance | REJECT |
| S3 `soft_delete/1` | REJECT / REIMPLEMENT |
| stable image processor | REIMPLEMENT, not source donor |
| multiple providers as default architecture | DO NOT PULL FORWARD WITHOUT EVIDENCE |

### 6.98 ACCEPTED GRILL DECISION

#### `GRILL-31 — Governed Media Uses Platform-Owned Exact Asset Identities; Durable Derivatives Are Assets with Exact Source Lineage, While Storage Providers Own Bytes/Locators Only`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

**Current-status note (v0.37.0):** GRILL-36 explicitly supersedes only GRILL-31's no-`MediaAssetVersion` conclusion and refines material replacement into stable-asset versus immutable-version semantics. GRILL-31's provider-independence, stable media identity, derivative identity and storage-authority conclusions remain accepted.

> Content & Media owns a dedicated durable governed media-asset identity independent of S3 keys, buckets, URLs, CDN paths, provider IDs or other external storage identifiers. Exact Ash module naming remains JIT; `MediaAsset` is the conceptual working name.
>
> PostgreSQL/Ash owns authoritative media identity, provenance, rights/attribution, lineage, publication/protected-delivery classification, replacement relationships and other material business metadata. S3-compatible object storage owns durable binary bytes.
>
> A storage provider/object locator is subordinate infrastructure state for an exact `MediaAsset`; it is never the asset's business identity or publication/delivery authority.
>
> Provider/object migration may change the storage locator without changing the platform media identity. Exact migration/replication mechanics remain JIT.
>
> NewYou does not pull Beacon's multi-provider semantics forward as a requirement. Additional storage copies/providers require an evidenced storage/recovery need and never create competing media authority.
>
> Each durable master/source, recording or derivative that can be independently referenced, governed, delivered, withdrawn, replaced or audited receives its own exact platform media identity.
>
> Source/master and derivative initially use the same `MediaAsset` semantic concept rather than introducing a separate `MediaDerivative` Resource solely because the object is derived.
>
> Every derivative records exact source lineage against the concrete source `MediaAsset` from which it was produced. Derivatives never reference a moving “current media” pointer.
>
> Creating or replacing a source asset does not silently rebind historical derivatives. New derivatives are generated against the replacement asset when required.
>
> Derivative lineage provides provenance but does not automatically transfer rights, publication state, approval or delivery permission. Those facts remain governed according to the derivative's own applicable policy.
>
> Captions, transcripts, approved replays, promotional clips, responsive images, thumbnails and other durable generated artifacts may participate in this exact derivative-lineage model where applicable; exact bounded derivative taxonomy remains JIT.
>
> Material replacement does not overwrite the binary behind an already-governed/referenceable `MediaAsset` identity. It creates a new exact media asset with explicit replacement/successor lineage. Historical references to the predecessor remain historically accurate.
>
> NewYou does not introduce a separate `MediaItem → MediaAssetVersion` hierarchy initially. Exact asset-to-asset replacement lineage is sufficient unless later relational/business requirements justify an additional stable parent identity.
>
> Immutable governed consumers reference exact `MediaAsset` identities and never silently follow replacements. Mutable authoring may explicitly adopt a replacement according to its own action semantics.
>
> Consuming Domains/resources remain authoritative for their own media-reference relationships. Content & Media may maintain a derived reverse usage/dependency projection for discovery, replacement and withdrawal operations, but that projection never becomes sole relationship authority.
>
> Material rights, attribution, provenance, publication, protected-delivery and withdrawal semantics are first-class governed facts where applicable and are not hidden inside an unrestricted `extra` metadata map.
>
> Optional low-significance editorial/presentation metadata may use a bounded extension mechanism only where it does not create competing business authority; exact extension design remains a later seam.
>
> Durable byte storage success, derivative processing success and provider capture do not imply media Approval, Publication or delivery permission.
>
> Protected media delivery checks current platform authority before issuing bounded delivery capability. Object/provider existence does not authorise delivery.
>
> Media Withdrawal/deletion business truth remains distinct from physical object deletion completion. Full storage/processor/backup deletion and restore reconciliation remain governed by the platform's deletion architecture and open OQ-030/OQ-031 work.
>
> Beacon's self-referencing Asset lineage and provider abstraction are **ADAPTED conceptually**. Beacon's database-binary default, unrestricted provider-key/extra maps as business authority, incomplete S3 deletion and stable image-processing implementation are **REJECTED as direct NewYou authority/source donors**.
>
> No direct Beacon runtime dependency is introduced by this decision.

**Project-owner deployment-direction note captured at acceptance:** eventual media-byte storage is intended to use external S3-compatible object storage such as Wasabi (or equivalent) so media is offloaded from the application server, reducing server disk footprint and binary-serving/storage load. This does not change the accepted provider-independent authority boundary and does not make Wasabi/provider identifiers business truth.

### 6.99 Consequences fixed for later grills

1. Dedicated durable C&M media identity is justified.
2. Conceptual working name is `MediaAsset`; exact module/name remains JIT.
3. Media identity is independent of provider/object IDs.
4. PostgreSQL/Ash owns material media business truth.
5. External S3-compatible object storage owns binary bytes/provider locators.
6. Project deployment direction expects off-server S3-compatible storage such as Wasabi or equivalent.
7. Exact provider remains replaceable without changing media business identity.
8. Provider/object locator is subordinate infrastructure state.
9. Multi-provider replication is not pulled forward without evidence.
10. Masters/sources and durable derivatives share the same media-asset semantic concept initially.
11. Every durable derivative has its own exact media identity.
12. Derivative lineage pins exact source asset.
13. Replacing a source does not rebind historical derivatives.
14. Derivation does not automatically transfer rights/publication/approval/delivery permission.
15. Captions/transcripts/replays/clips/responsive images may use the same lineage model where applicable.
16. Material replacement creates successor asset identity rather than overwriting governed bytes in place.
17. No MediaItem→MediaAssetVersion hierarchy initially.
18. Immutable consumers retain exact asset references.
19. Mutable authoring may explicitly adopt replacement assets.
20. Consumers remain authority for their own reference relationships.
21. Reverse usage/dependency lookup may be derived but not authoritative.
22. Material rights/attribution/provenance/publication/protected-delivery/withdrawal facts are first-class.
23. Open generic metadata maps do not own material governance.
24. Storage/processing success does not create media Publication.
25. Protected delivery checks current platform authority.
26. Provider/object existence never authorises delivery.
27. Business withdrawal/deletion is distinct from provider-object deletion completion.
28. Full deletion/processor/backup reconciliation remains OQ-030/OQ-031/downstream work.
29. Beacon Asset lineage/provider seams are adapted conceptually; stable storage/processing implementations are not direct donors.
30. **Historical at GRILL-31 acceptance:** Block 4A.2 was the next seam; it was resolved by GRILL-32 in v0.33.0 without making worker/provider state authoritative.

### 6.100 Block 4A.2 pressure test — media ingest, durable async processing and object-store reconciliation

Current NewYou authority requires:

```text
temporary_restricted_upload
→ size/type validation
→ MIME/content inspection
→ malware scan
→ metadata sanitisation where appropriate
→ durable storage
→ governed access/publication
```

It also fixes:

- S3-compatible object storage for durable binary objects, with PostgreSQL governing metadata/control;
- heavy processing as asynchronous;
- PostgreSQL-backed durable execution intent / Oban for durable async work;
- queue runtime state as operational only;
- short authoritative transactions;
- durable idempotency evidence where crash recovery/reconciliation depends on it.

Beacon stable `v0.5.1` provides useful processor/provider separation, but its upload orchestration writes to external providers before local database persistence and therefore cannot be imported as NewYou's correctness model.

#### Beacon stable write ordering is rejected

Beacon's stable upload path is effectively:

```text
process
→ provider write
→ database Asset insert
→ asset lifecycle / derivative side effects
```

If provider write succeeds but database persistence fails, external bytes exist without NewYou authoritative media truth.

External S3-compatible writes are not part of a PostgreSQL transaction and cannot be rolled back by database failure.

NewYou therefore rejects any design that treats object storage + PostgreSQL as one atomic transaction.

#### Temporary upload is pre-authority restricted state

Uploaded bytes initially exist only inside a restricted, non-deliverable staging boundary.

A temporary upload:

- is not a `MediaAsset`;
- is not published;
- is not referenceable by governed content;
- is not deliverable;
- does not establish rights/provenance authority.

Direct-to-S3-compatible staging may be used for large media so Phoenix does not need to retain/proxy the complete payload.

Completion of a temporary upload proves only that temporary bytes arrived.

#### Mandatory inspection occurs before accepted ingest

Before accepted durable ingest, the media passes the required:

- size/type validation;
- MIME/content inspection;
- malware scanning;
- metadata sanitisation where applicable.

Unsafe content fails closed.

Ambiguous/infrastructure-failed scanning does not become acceptance merely because bytes exist.

Client filename, extension and declared MIME are input/provenance only, not authoritative media type.

#### Accepted ingest intent precedes permanent external write

After the required pre-ingest checks pass, NewYou may allocate the exact `MediaAsset` identity and durable accepted-ingest intent before permanent provider writes.

Conceptually:

```text
validated / accepted source bytes
        ↓
short PostgreSQL transition
        ↓
reserve MediaAsset M17
storage not yet available
exact ingest assumptions recorded
        ↓ COMMIT

external durable-object write
```

This creates durable platform authority against which retry/reconciliation can operate.

A separate `MediaIngest` business Resource is not justified initially merely to coordinate upload mechanics.

#### Object-store write and DB finalisation are separate transitions

Permanent provider/object writes occur outside the database transaction.

After write success, NewYou verifies the resulting object against expected integrity facts and performs a second short authoritative transition:

```text
provider write succeeds
→ verify expected object / size / checksum
→ short PostgreSQL transition
→ exact locator + integrity facts
→ storage available
```

Exact Ash action/transaction representation remains JIT.

#### MediaAsset existence does not equal usable media

A reserved MediaAsset with pending/unverified storage is not usable/referenceable as successfully ingested media.

Only verified storage finalisation makes the asset storage-ready.

Storage readiness remains distinct from:

- rights completeness;
- Approval;
- Publication;
- protected delivery permission.

#### Platform checksum belongs to exact represented bytes

Each storage-ready MediaAsset retains platform-controlled integrity evidence, including checksum and size, for the exact durable bytes represented by that identity.

Exact checksum algorithm remains JIT.

Provider IDs/ETags/object metadata do not automatically substitute for NewYou's platform integrity evidence.

Checksum equality does not merge business identities; automatic content-addressed deduplication is not introduced without evidence.

#### Accepted source is the sanitised/approved durable representation

The source MediaAsset represents the bytes that passed the governed ingest pipeline.

Temporary raw/pre-sanitisation material is not retained indefinitely by default.

Any requirement to retain raw pre-sanitisation bytes requires explicit governed retention/provenance justification.

#### Ready media bytes are not silently overwritten

Once an exact MediaAsset is storage-ready, materially different bytes do not replace its object in place.

Material change creates a new MediaAsset under `GRILL-31`.

If retry encounters an already-existing object whose integrity matches the expected operation, NewYou may reconcile the same logical result.

If the existing object differs from expected integrity, the operation fails closed rather than silently overwriting/adopting the conflicting bytes.

#### Crash recovery is deterministic

If accepted-ingest intent commits but object storage fails:

```text
M17 pending
object absent
→ retry same M17 operation
```

If object storage succeeds but final DB confirmation is lost/fails:

```text
M17 pending
expected object exists
→ verify
→ reconcile/finalise M17
```

No duplicate MediaAsset is created merely because the worker/caller lost confirmation.

Temporary restricted objects that never reach accepted-ingest intent are staging orphans, not MediaAssets, and are cleaned/reconciled under bounded staging policy.

#### Heavy processing is durable async

Media processing that is expensive or non-immediate uses durable async execution.

Conceptually:

```text
authoritative processing intent
→ PostgreSQL-backed durable execution / Oban
→ processing worker
→ provider/object write
→ verify
→ authoritative MediaAsset finalisation
```

Queue/worker runtime state never becomes media business authority.

#### Derivative work pins exact source and exact processing intent

A derivative operation binds to:

```text
exact source MediaAsset
+
exact source integrity/provenance assumptions
+
bounded derivative/processing intent
```

It does not process a moving “current media” pointer.

The exact derivative-contract/version representation remains JIT.

#### Derivative MediaAsset can be reserved before external work

A durable derivative MediaAsset may be reserved with exact source lineage and non-ready storage state before processing/provider side effects.

Equivalent retries target the same logical derivative identity.

A materially different transform/processing contract produces a distinct derivative result rather than silently overwriting an already-ready derivative.

#### Source readiness and derivative readiness are independent

A source may become storage-ready while optional derivatives are still processing.

Whether specific derivatives are mandatory for Publication or delivery is a later policy/governance seam.

The existence of pending optional derivatives does not redefine source identity.

#### Processing attempts remain operational evidence

Worker retries, provider HTTP failures, processing exceptions and execution duration remain operational evidence.

They do not justify a `MediaProcessingAttempt` business Resource initially.

Future legal/billing/provider-accountability requirements may justify stronger attempt evidence later.

#### Processing failure does not erase media identity

If a reserved derivative repeatedly fails processing, its identity can remain non-ready/failed/abandoned under later lifecycle design.

Retries do not require minting a new identity each time.

Exact terminal-state vocabulary remains JIT.

#### Missing/corrupt durable object is a storage incident, not identity erasure

If PostgreSQL contains authoritative MediaAsset history but the expected S3-compatible object later disappears or fails integrity checks:

```text
MediaAsset history remains
→ delivery fails closed
→ storage incident/recovery/reconciliation
```

NewYou does not pretend that the MediaAsset never existed.

Backup/restore/non-resurrection details remain under OQ-031 and downstream architecture.

#### No long DB transactions across external work

NewYou explicitly rejects:

```text
BEGIN DB transaction
→ upload large media to Wasabi/S3
→ transcode
→ upload derivatives
→ COMMIT
```

Correct shape:

```text
short authoritative DB transition
→ external durable async work
→ short authoritative reconciliation/finalisation transition
```

#### Wasabi remains behind the provider seam

The accepted deployment direction composes as:

```text
Phoenix / Ash
→ metadata + authority + ingest intent

Oban / processors
→ durable external work

Wasabi or equivalent S3-compatible storage
→ restricted staging + durable bytes

delivery/CDN layer
→ later bounded delivery
```

Wasabi/provider state remains infrastructure, not media authority.

#### Beacon reuse classification for Block 4A.2

| Beacon mechanism | NewYou classification |
|---|---|
| `UploadMetadata` as processing context | ADAPT CONCEPTUALLY |
| processor abstraction | ADAPT CONCEPTUALLY |
| provider abstraction | ADAPT |
| validation-hook concept | ADAPT CONCEPTUALLY |
| `process → provider upload → DB insert` ordering | REJECT |
| external provider calls around DB lifecycle work | REJECT |
| filename-derived MIME as authority | REJECT |
| synchronous whole-file BEAM-memory processing as general media model | REJECT |
| synchronous derivative creation in upload lifecycle | REJECT / REIMPLEMENT AS DURABLE ASYNC |
| provider success as completion authority | REJECT |
| no explicit external-write reconciliation | REIMPLEMENT |

### 6.101 ACCEPTED GRILL DECISION

#### `GRILL-32 — Media Ingest Uses Restricted Pre-Authority Staging, Durable Accepted-Ingest Intent and Verified Idempotent Object-Store Finalisation; Processing Workers Never Become Media Authority`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

**Current-status note (v0.38.0):** GRILL-36 refines GRILL-32 so checksum, byte size, storage locator, accepted-ingest/finalisation target and processing provenance are exact `MediaAssetVersion` facts. Any GRILL-32 wording that delegates materially changed bytes to GRILL-31's historical “new MediaAsset” rule is likewise read through GRILL-36: a revision of the same conceptual object creates a successor `MediaAssetVersion`; a genuinely distinct media object creates a distinct stable `MediaAsset`. The ingest ordering, idempotency and provider/worker authority conclusions remain accepted.

> Uploaded bytes first enter a temporary restricted, non-deliverable staging boundary. A temporary upload is not itself a `MediaAsset`, Publication or delivery authority.
>
> Before durable Media Library acceptance, the upload undergoes the platform-required size/type validation, MIME/content inspection, malware scanning and metadata sanitisation applicable to the media class. Unsafe or unresolved inputs fail closed and cannot become usable governed media.
>
> Client-provided filename, extension and MIME declarations are input/provenance metadata only; authoritative media type is established through the accepted inspection pipeline.
>
> NewYou may use direct-to-external-S3-compatible restricted upload for large media so the application server is not required to persist or proxy full media payloads. Exact signed-upload/staging mechanics remain JIT. Completion of such an upload proves only that temporary bytes arrived.
>
> Once required pre-ingest checks succeed, NewYou may allocate the exact platform `MediaAsset` identity in a non-usable storage-pending state and durably record the accepted ingest intent **before** performing the permanent external-object-store write.
>
> NewYou does not introduce a dedicated `MediaIngest` business Resource initially merely to coordinate external upload mechanics. Exact temporary-upload/session representation remains implementation/JIT detail.
>
> Permanent provider/object writes occur outside PostgreSQL transactions. NewYou never holds a database transaction open across S3-compatible upload, transcoding or derivative-processing calls and never treats PostgreSQL plus object storage as one atomic transaction.
>
> After external storage succeeds, NewYou verifies the exact durable object against platform integrity expectations and performs a separate short authoritative transition recording the storage locator, exact-byte checksum/size and storage availability for the reserved `MediaAsset`.
>
> A `MediaAsset` is not usable/referenceable as successfully ingested media until its durable object has been verified and its authoritative storage-availability transition has committed.
>
> Storage availability remains independent from rights, Approval, Publication and actor delivery authorisation. A successfully stored asset is not automatically published or deliverable.
>
> Each durable `MediaAsset` retains a platform-controlled checksum/integrity value for the exact durable bytes represented by that identity. Exact checksum algorithm remains JIT. Provider/object identifiers do not replace platform integrity evidence.
>
> Checksum equality does not merge media identities. Identical bytes may carry different provenance, rights or lifecycle history. Automatic content-addressed deduplication is not introduced without evidence.
>
> The durable source asset represents the accepted bytes that passed the governed ingest pipeline. Temporary pre-sanitisation upload bytes are not retained indefinitely by default; any requirement to preserve them must be explicitly governed.
>
> Permanent bytes behind a storage-ready `MediaAsset` are not silently overwritten. Materially different bytes require a new MediaAsset identity under `GRILL-31` replacement semantics.
>
> Retry against an existing object that matches the expected integrity may reconcile the same operation. An existing object with mismatching integrity fails closed rather than being silently overwritten/adopted.
>
> If PostgreSQL accepted-ingest intent commits but the provider write fails, the same non-ready MediaAsset remains the reconciliation/retry target rather than minting another identity.
>
> If the provider write succeeds but final PostgreSQL confirmation is lost/fails, reconciliation verifies the already-written object and completes the same MediaAsset rather than creating duplicate business truth.
>
> Temporary restricted objects that never reach accepted-ingest intent are staging orphans, not MediaAssets, and are removed/reconciled under bounded temporary-storage policy.
>
> Heavy media processing is durable asynchronous work. PostgreSQL-backed durable intent/Oban is the default execution model where async processing is required; queue runtime/worker state is operational only.
>
> Derivative processing binds to one exact immutable source MediaAsset plus the exact bounded derivative/processing intent it evaluated. It never processes a moving “current media” pointer.
>
> A durable derivative MediaAsset may be reserved with exact source lineage and non-ready storage state before its external processing/storage work. Equivalent retries target the same logical derivative identity rather than minting duplicate MediaAssets.
>
> A materially different derivative transformation/processing contract creates a distinct derivative result rather than silently overwriting an already-ready derivative identity. Exact derivative-contract/version representation remains JIT.
>
> Source storage readiness and derivative readiness are independent. Optional derivative work may continue asynchronously after the source becomes storage-ready. Whether specific derivatives are mandatory for Publication/delivery remains a later policy seam.
>
> Individual provider/worker retries, exceptions and execution attempts are operational evidence and do not justify a `MediaProcessingAttempt` business Resource initially.
>
> If an object expected by an already-authoritative MediaAsset becomes unavailable or corrupt, the MediaAsset's historical identity is not erased. Delivery fails closed and storage recovery/reconciliation operates against the authoritative PostgreSQL media record.
>
> External S3-compatible storage such as the project-directed Wasabi-or-equivalent provider remains behind the `GRILL-31` storage seam and never becomes media business authority.
>
> Beacon's processing-context, processor and provider separations are **ADAPTED conceptually**. Beacon's stable synchronous orchestration, external-write-before-database ordering, filename-derived type assumptions, transaction-adjacent provider work and whole-file synchronous processing are **REJECTED / REIMPLEMENTED** for NewYou.
>
> No direct Beacon runtime dependency is introduced by this decision.

### 6.102 Consequences fixed for later grills

1. Temporary uploads remain restricted and non-authoritative.
2. Mandatory inspection/scan/sanitisation precedes accepted ingest.
3. Filename/extension/client MIME are not authoritative type.
4. Direct-to-S3-compatible restricted staging is permitted to offload large media from Phoenix.
5. Temporary-upload completion proves bytes arrived only.
6. Exact MediaAsset identity and durable accepted-ingest intent precede permanent provider write.
7. No dedicated MediaIngest business Resource initially.
8. Permanent provider writes occur outside PostgreSQL transactions.
9. Object-store + PostgreSQL is never treated as one atomic transaction.
10. Storage-ready finalisation occurs only after object integrity verification.
11. Non-ready MediaAssets are not usable/referenceable as successful media.
12. Storage readiness is independent from rights/Approval/Publication/delivery.
13. Each ready MediaAsset retains platform checksum/size integrity evidence.
14. Checksum equality does not merge media identities.
15. No automatic content-addressed deduplication initially.
16. Accepted durable source represents post-validation/sanitisation bytes.
17. Raw temporary bytes are not retained indefinitely by default.
18. Ready MediaAsset bytes are effectively immutable under that identity.
19. Integrity-matching retries reconcile the same operation.
20. Integrity mismatch fails closed.
21. DB-intent/provider-write failure retries the same MediaAsset.
22. Provider-success/DB-finalisation failure reconciles the same MediaAsset.
23. Staging orphans are not MediaAssets and are cleaned separately.
24. Heavy processing uses durable async execution.
25. Queue/worker state remains operational only.
26. Derivative jobs pin exact source + exact processing intent.
27. Durable derivative identity may be reserved before external work.
28. Equivalent retries do not mint duplicate derivatives.
29. Materially different derivative processing yields distinct derivative result.
30. Source readiness and derivative readiness are independent.
31. No MediaProcessingAttempt business Resource initially.
32. Missing/corrupt durable object is storage incident/recovery, not identity erasure.
33. No long PostgreSQL transaction spans S3/Wasabi/transcoding work.
34. Wasabi-or-equivalent remains behind the provider seam.
35. Beacon processor/provider separation is conceptual inspiration; orchestration is reimplemented.
36. **Historical at GRILL-32 acceptance:** Block 4A.3 was the next seam; it was resolved by GRILL-33 in v0.34.0 without creating shared authority.

### 6.103 Block 4A.3 pressure test — rights, provenance, publication and protected delivery

Current authority requires Content & Media to own governed media identity/derivatives/publication while protected playback checks current platform authority before issuing bounded delivery capability. Entitlements retains product/access authority, Events & Live retains event admission, Identity & Access retains actor/session authority and Privacy & Consent retains consent truth.

The semantic split is:

```text
May this exact media asset be used/published at all?
→ Content & Media

Does this actor currently have access?
→ Entitlements / owning admission authority

Does current consent permit this use?
→ Privacy & Consent
```

Rights/provenance evidence and current rights eligibility are separate. Historical evidence remains interpretable even when later expiry, policy or legal facts make the asset currently ineligible.

Source/derivative lineage establishes provenance only. Permissions do not broaden automatically through derivation.

Full recordings, approved replays, promotional clips, captions and transcripts remain separately governable exact MediaAssets.

Media Publication is durable activation truth for one exact MediaAsset and remains distinct from asset identity/storage state. Source and derivative publication are independent.

Protected delivery composes current C&M eligibility with current owning-domain access/consent truth. It does not copy those foreign truths into MediaAsset state.

The result of a successful protected-delivery decision is a short-lived/bounded technical capability, not a durable entitlement or stable provider credential.

Provider/CDN/object-store success, object existence or direct provider URLs never establish Publication or access authority.

Beacon's provider abstraction remains useful. Beacon's direct URL construction is unsuitable as protected-delivery authorisation.

### 6.104 ACCEPTED GRILL DECISION

#### `GRILL-33 — Media Rights and Publication Remain Exact C&M Authority; Derivative Permissions Do Not Auto-Inherit, and Protected Delivery Composes Current C&M, Access and Consent Truth into a Bounded Capability`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

**Current-status note (v0.37.0):** GRILL-36 refines media Publication to activate an exact `MediaAssetVersion`. GRILL-33's C&M/access/consent ownership boundaries and bounded protected-delivery semantics remain accepted.

> Content & Media owns the governed media provenance, applicable rights/attribution facts, exact media Publication/Withdrawal truth and permitted delivery/exposure classification for each exact `MediaAsset`.
>
> Content & Media records rights/provenance facts sufficient to govern platform media usage but does not invent legal ownership/licence authority. Exact IP/licence terms remain subject to the existing Product/Expert Review and legal-rights gates.
>
> Rights/provenance evidence and current rights eligibility are separate. Historical rights/provenance evidence remains interpretable even when expiry, policy or later legal facts make an asset currently ineligible for publication/delivery.
>
> Exact rights persistence may use bounded attributes or subordinate Resources where relational multiplicity/lifecycle justifies them. No dedicated `MediaRightsGrant` Resource is introduced by this decision without that evidence.
>
> Rights eligibility, storage readiness, Publication and delivery authorisation are independent dimensions. Successful ingest/storage does not establish rights, Publication or access.
>
> Exact source→derivative lineage establishes provenance but does not automatically grant the derivative the source's rights, Publication, Approval or delivery permission.
>
> Constraints arising from source provenance/rights may restrict derivatives, but derivative permissions never broaden implicitly. Any broader/different permitted use requires an explicit governed rights basis.
>
> Full recordings, approved replays, promotional clips, captions, transcripts and other derivatives remain separately governable exact MediaAssets. Provider capture of a recording does not create an approved replay; replay approval/publication does not automatically publish or authorise promotional derivatives.
>
> Material attribution requirements are governed C&M media facts where applicable. Defaults copied from a source may assist authoring but do not establish that derivative obligations are legally identical.
>
> Media Publication is durable C&M activation truth against one exact `MediaAsset`, separate from MediaAsset identity/storage state. The dossier requires one coherent C&M Publication semantic meaning but does not require content and media Publication to share one polymorphic persistence table.
>
> Publishing a derivative does not publish its source or sibling derivatives. A source/master may remain restricted/unpublished while an approved replay or promotional derivative has its own independent Publication.
>
> Media Publication may define an approved exposure/delivery class or equivalent bounded scope. That class establishes how C&M permits the media to be exposed; it does not establish whether a particular actor owns the required entitlement/admission.
>
> A consuming context may further restrict media use but may not broaden use beyond C&M's current rights/publication rules.
>
> Entitlements remains authoritative for general product/access rights. Events & Live remains authoritative for event-specific ticket/admission truth where applicable. Identity & Access remains authoritative for actor/session authority. Privacy & Consent remains authoritative for consent truth.
>
> Content & Media does not copy those current foreign-domain truths into `MediaAsset` state and does not introduce a general `MediaAccessGrant` merely to mirror them.
>
> Media Publication or delivery operations may retain exact decision-basis references/evidence showing which external authority facts were evaluated historically, but those references never become the current authority for entitlement, event admission or consent.
>
> Protected media delivery is an authoritative operation that rechecks current C&M media eligibility and all applicable current owning-domain access/consent gates before issuing a bounded technical delivery capability.
>
> A protected-delivery capability is short-lived/bounded and scoped to the permitted delivery operation/asset rather than being a permanent business entitlement or stable provider credential. Exact token/signed-URL/edge mechanism remains OQ-014/JIT.
>
> Entitlement cancellation, access revocation, consent withdrawal or media Withdrawal prevents issuance of new protected-delivery capabilities as soon as the relevant authoritative state is effective.
>
> Exact revocation/purge behavior for already-issued capabilities and cached content remains governed by `OQ-014`; high-risk immediate-withdrawal requirements must be proven there rather than assumed from ordinary object-storage URLs.
>
> Public media delivery does not require per-actor entitlement merely because it is media, but it still requires current C&M public-publication/rights/withdrawal eligibility.
>
> Provider/CDN/object-store availability never creates Publication or access authority. Provider delivery success/failure is operational evidence only.
>
> Stable provider/object URLs are not a protected-delivery authorisation model. Protected Wasabi/S3 objects are accessed only through the governed bounded-delivery path chosen downstream.
>
> Media rights/publication changes do not rewrite or erase historical MediaAsset bytes/identity. Withdrawal and physical deletion remain separate governed concerns.
>
> Where changed source-rights/consent facts affect derivatives, affected derivative Publication/delivery eligibility is reevaluated through the governed rights/consent model; derivative identities and lineage are not rewritten.
>
> Beacon's provider abstraction and basic public-URL mechanics may provide low-level reference for explicitly public media. Beacon's direct `url_for` pattern, provider-object existence, `extra` metadata and soft-delete semantics are **REJECTED** as NewYou protected-rights/publication/access authority.
>
> No direct Beacon runtime dependency is introduced by this decision.

### 6.105 Consequences fixed for later grills

1. Rights/provenance, storage readiness, Publication and delivery authorisation are separate dimensions.
2. C&M owns exact media rights/provenance/publication/withdrawal truth.
3. Legal ownership/licence authority remains subject to existing legal/expert gates.
4. Derivative permissions never broaden implicitly from source lineage.
5. Recording capture does not create approved replay truth.
6. Source and derivative publication are independent.
7. Entitlements/Event admission/Identity/Consent remain foreign current authorities.
8. C&M does not copy those truths into MediaAsset state.
9. Protected delivery rechecks current owners at request time.
10. Successful protected delivery yields a bounded technical capability only.
11. Provider/CDN/object existence is never access authority.
12. Exact token/signed-URL/edge mechanics remain OQ-014/JIT.
13. Media Withdrawal blocks new capability issuance when effective.
14. Public media still requires current C&M public-publication/rights/withdrawal eligibility.
15. No generic MediaAccessGrant Resource is introduced.
16. **Historical at GRILL-33 acceptance:** Block 4A.4 was the next seam; it was resolved by GRILL-34 in v0.35.0 and later deletion terminality was narrowly refined by GRILL-37.

### 6.106 Block 4A.4 pressure test — withdrawal, physical deletion and non-resurrection

Current Architecture Law defines full deletion as a durable, idempotent cross-system orchestration. Deleting a database row is not completion. Eligible identifiable representations must be disposed and verified across authoritative state, object/derivative storage, caches/search/read models and relevant external processors.

`FLOW-08` is:

```text
Full deletion
→ storage / processors
→ backup boundary
```

`OQ-030` remains the external-processor deletion inventory gate. `OQ-031` remains the backup restore/deletion replay gate. `OQ-032` remains the export/deletion operations gate.

Withdrawal and physical deletion are distinct:

```text
Withdrawal
→ remove current/future delivery authority

Physical deletion
→ governed disposition of eligible bytes/representations
```

Deletion/suppression must become authoritative before asynchronous destructive work, so cleanup failure cannot preserve delivery authority.

Source/derivative lineage identifies the candidate deletion-impact set, but ancestry alone does not dictate disposition; policy determines which descendants are actually in scope.

Database cascade deletion and provider soft-delete cannot prove object/processor/cache/backup disposition and are therefore rejected as business deletion semantics.

Restore from a point preceding deletion remains recovery-isolated until later deletion/suppression truth is replayed/reconciled and resurrected state is removed or suppressed.

### 6.107 ACCEPTED GRILL DECISION

#### `GRILL-34 — Media Withdrawal Immediately Removes Delivery Authority; Physical Deletion Is a Separate Durable, Idempotent and Non-Resurrecting Disposition Workflow Across Exact Assets, Derivatives, Storage and Processors`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

**Current-status note (v0.38.0):** GRILL-37 refines only GRILL-34's pre-version terminality/object-reuse wording so disposition is scoped to the exact `MediaAssetVersion` or broader stable `MediaAsset` subject and legitimately shared same-asset bytes are not destroyed while another lawfully retained version still requires them. GRILL-34's Withdrawal separation, fail-closed suppression, durable/idempotent cleanup, derivative-impact policy, provider verification, cross-system reconciliation and backup non-resurrection semantics remain accepted.

> Content & Media keeps media Withdrawal and physical deletion semantically separate. Withdrawal removes current/future delivery eligibility for an exact governed MediaAsset according to scope; it does not by itself mean the physical binary must be destroyed.
>
> Physical deletion occurs only when an applicable privacy, rights, retention, legal or other governed disposition requires eligible media representations to cease existing. Ordinary editorial withdrawal does not silently imply physical deletion.
>
> Once an exact media deletion/suppression obligation becomes effective, the affected MediaAsset becomes non-deliverable before asynchronous physical cleanup completes. Provider, cache, processor or cleanup failure cannot preserve delivery authority.
>
> New governed references, Publication and derivative creation against a deletion-suppressed MediaAsset fail closed.
>
> Already-running derivative work must revalidate the exact source's current deletion/suppression eligibility before authoritative derivative finalisation. Work whose source has become deletion-suppressed cannot create a ready derivative; produced external bytes are cleaned/reconciled.
>
> NewYou does not delete/minimise the authoritative PostgreSQL media facts needed for external deletion reconciliation before in-scope provider/processor cleanup is verified.
>
> After lawful deletion completion, authoritative media records may themselves be deleted, irreversibly anonymised or reduced to minimal non-reconstructive suppression/deletion evidence according to the applicable retention/privacy policy.
>
> Physical deletion of the exact MediaAsset bytes is terminal for that exact media identity. Later upload of identical bytes creates a new MediaAsset identity rather than resurrecting the deleted identity.
>
> Exact source/derivative lineage is used to discover the deletion-impact candidate set. Deletion does not use an unconditional relational cascade merely because an asset is descended from a source.
>
> Each descendant's required disposition is established by the governing deletion/rights/privacy policy. Derivatives containing the same eligible identifiable/deletion-subject material are included where required; independently lawful/unaffected derivatives are not falsely deleted merely by ancestry.
>
> Withdrawal or deletion of one asset never rewrites derivative identities or historical lineage.
>
> Beacon's Ecto `on_delete: :delete_all` derivative cascade is **REJECTED** as NewYou business deletion semantics because database-row cascade cannot prove provider-object, processor, cache or backup disposition.
>
> Beacon's stable provider `soft_delete` implementation is **REJECTED** as NewYou physical-deletion authority; setting `deleted_at` while an S3 object remains does not satisfy deletion completion.
>
> Current governed content/publications that depend on a media asset being deletion-suppressed must fail closed and be corrected, replaced or withdrawn according to C&M policy rather than continuing to present the asset as available. Immutable historical references remain historically accurate.
>
> Media physical deletion is durable, idempotent, retryable, observable and reconcilable. Retry after partial success converges on the same exact deletion obligation rather than manufacturing new asset or deletion identities.
>
> Individual provider/worker delete attempts remain operational evidence and do not justify a `MediaDeletionAttempt` business Resource initially.
>
> Provider deletion success alone does not prove platform deletion completion. Completion requires verification against the actual configured storage/processor contract, including applicable object versions, replicas, derivatives, caches/search representations and external processors.
>
> Provider object/versioning/retention/replication behavior is proof/JIT configuration under OQ-030; NewYou does not assume that one S3-compatible `DELETE` call removes every historical provider-held representation.
>
> A provider object locator that has represented one exact MediaAsset is not reused for a different media identity. Exact key-generation mechanics remain JIT.
>
> Full participant/data deletion remains a platform-wide durable cross-system orchestration. Content & Media participates through its own deletion contract and retains ownership of C&M media semantics; it does not become a global deletion authority.
>
> The platform-wide deletion workflow may coordinate C&M deletion work but does not directly redefine MediaAsset business truth.
>
> Lawfully retained or legally held media is minimised and isolated from ordinary access. A narrow hold pauses only the exact deletion it governs and never restores ordinary delivery eligibility.
>
> C&M reports its deletion sub-obligation complete only when all eligible C&M representations in scope are deleted/irreversibly anonymised or otherwise lawfully disposed and verified. Completion is not inferred merely from an Oban job finishing.
>
> Historical encrypted backups are not rewritten for every deletion by default. Required suppression/deletion evidence survives beyond selected restore points.
>
> Any restore from a point preceding a completed deletion remains recovery-isolated until later deletion/suppression truth is replayed/reconciled and resurrected media/database/provider state has been removed or suppressed.
>
> A restored database row, object-store object or provider representation does not regain current authority merely because it existed in the historical backup.
>
> OQ-031 retains authority over backup expiry, restore isolation, deletion-ledger replay, verification and go-live gates. This decision fixes the media non-resurrection semantic requirement but does not close OQ-031.
>
> OQ-030 retains authority over the concrete external storage/video/processor deletion inventory and provider-specific verification semantics. This decision does not close OQ-030.
>
> OQ-032 and the platform's full deletion capability retain authority over operational deletion requests, completion evidence and cross-domain orchestration.
>
> No direct Beacon runtime dependency is introduced by this decision.

### 6.108 Consequences fixed for later grills

**Current-status note (v0.38.0):** consequence 7 and the locator/identity implications are refined by GRILL-37. Version-scoped disposition does not force destruction of bytes still lawfully required by another version of the same stable asset; whole-asset terminal disposition still prevents stable-identity resurrection; a policy requiring destruction of the bytes themselves expands to every dependent version.

1. Media Withdrawal and physical deletion are distinct.
2. Withdrawal does not imply binary destruction.
3. Deletion suppression blocks delivery before cleanup finishes.
4. New references/Publications/derivatives against deletion-suppressed media fail closed.
5. Running derivative work revalidates before finalisation.
6. Reconciliation authority is retained until external cleanup is verified.
7. Exact deleted bytes never resurrect under the same MediaAsset identity.
8. Lineage drives candidate impact discovery, not blind cascade.
9. Beacon database cascade is rejected as deletion semantics.
10. Beacon provider soft-delete is rejected as deletion completion.
11. Deletion is durable, idempotent, retryable, observable and reconcilable.
12. Provider DELETE success alone is insufficient completion evidence.
13. Provider object/versioning semantics remain OQ-030/proof work.
14. Provider locators are not reused across media identities.
15. C&M participates in platform full deletion without becoming global deletion authority.
16. Legal holds are narrow and never restore ordinary delivery.
17. Completion requires verified disposition of all in-scope C&M representations.
18. Backup deletion truth must survive restore points.
19. Restore remains isolated until deletion/suppression replay and reconciliation complete.
20. OQ-030/OQ-031/OQ-032 remain open.
21. No MediaDeletionAttempt business Resource is introduced.
22. **Historical at GRILL-34 acceptance:** Block 4A.5 was the next seam; it was resolved by GRILL-35 in v0.36.0 without making reverse indexes authoritative.

### 6.109 Block 4A.5 pressure test — authoritative forward media references, derived reverse usage indexing and owner-mediated replacement

Current frontend/operating contracts require the governed Media Library to preserve:

- usage references;
- replacement/version semantics;
- material replacement lineage;
- reference updates according to usage semantics rather than blind overwrite.

`GRILL-31` already establishes exact platform-owned MediaAsset identity and replacement lineage.

`GRILL-34` already establishes that dependency discovery must not rely on a stale derived index as sole authority for destructive disposition.

The remaining question is which side owns the actual media-reference relationship and how replacement/dependency discovery can be fast without becoming shared-write authority.

#### Forward references are authoritative

If an owning record uses exact MediaAsset `M4`, the owner contains or otherwise owns the exact relationship:

```text
ContentVersion C17
→ exact MediaAsset M4
```

The forward reference is business truth.

File names, URLs, storage keys, successor pointers and reverse-index rows do not substitute for the exact MediaAsset relationship.

#### The consumer owns its own relationship

The Domain/resource containing the consuming record remains authoritative for the media reference.

Content & Media owns the referenced MediaAsset.

It does not gain shared-write ownership of every foreign record merely because those records refer to C&M media.

#### Immutable consumers do not silently follow replacement

If:

```text
C17 → M4
```

and `M4` is replaced by `M9`, historical immutable truth remains:

```text
C17 → M4
```

A current immutable/published Content Version that must adopt `M9` does so through the existing successor Content Version / Review / Approval / Publication path.

Replacement lineage never rewrites historical governed references.

#### Mutable consumers may explicitly adopt replacement

Mutable authoring/consumer state may replace an exact old reference with a successor through the owning Domain/resource action.

The existence of:

```text
M4 replaced_by M9
```

is not itself a mutation command.

#### No generic runtime latest-media pointer

Ordinary governed references do not resolve through a moving “current/latest replacement” pointer.

If a future bounded capability genuinely requires current-media resolution, it needs explicit separate semantics rather than becoming the default reference model.

#### Reverse usage index is derived

Editors/operators need an efficient:

```text
Where is M4 used?
```

surface.

A derived reverse usage/dependency projection may answer that question.

Conceptually it can contain enough locator/context data to return to the authoritative owner:

```text
M4
→ owner/domain kind
→ exact consumer identity
→ reference location/role
→ lifecycle/currentness context
```

Exact schema remains JIT.

The reverse projection never becomes sole authority for whether the relationship exists.

#### Derived usage indexing is rebuildable

Loss/corruption of the projection may reduce operator convenience/performance.

It must not erase the underlying relationships.

Conceptually:

```text
drop / corrupt projection
→ scan/replay authoritative forward references
→ rebuild projection
```

#### No synchronous cross-domain dual-write requirement

An owning Domain does not need to synchronously write both:

```text
its own authoritative record
+
a shared C&M MediaUsage business table
```

inside one transaction merely to preserve correctness.

Projection maintenance may be asynchronous/reconcilable because the forward owner remains authority.

#### Reverse index never authorises mutation

A reverse-index row only identifies a candidate owner/reference.

Replacement must:

```text
derived usage candidate
→ invoke owner
→ owner revalidates current exact reference
→ owner validates replacement
→ owner applies or refuses
```

C&M does not directly update foreign Domain tables from usage-index rows.

#### Expected-old-reference protection

Owner-mediated replacement revalidates that the target still references the exact predecessor asset.

Conceptually:

```text
replace_media(
  expected_old_asset: M4,
  new_asset: M9
)
```

If the authoritative owner already changed to `M6`, the stale replacement attempt reports conflict/already-changed rather than overwriting `M6`.

Exact optimistic-lock/action syntax remains JIT.

#### Successor compatibility belongs to the consumer

The successor asset must satisfy the owning consumer's own constraints.

Examples may include:

- expected media type;
- bounded block/field role;
- rights/exposure compatibility;
- derivative availability;
- consumer-specific invariants.

Content & Media does not create one universal cross-domain `compatible_replacement?/2` business oracle.

#### Replacement semantics depend on consumer lifecycle

At minimum:

```text
mutable draft
→ explicit owner mutation may be allowed

immutable historical version
→ never mutate

current immutable/published version
→ successor governed version/publication

foreign Domain mutable record
→ owner-specific action

foreign Domain immutable record
→ owner-specific successor/correction semantics
```

There is no valid global SQL-style “replace everywhere” mutation.

#### Bulk replacement is orchestration, not authority

Editors may request a broad replacement.

The semantic flow is:

```text
discover candidate usages
→ group/classify by owner/lifecycle
→ invoke each owner
→ owner revalidates old ref + successor compatibility
→ update / refuse / require successor / retry
→ collect durable result
```

Where partial completion matters, that orchestration is durable, idempotent, resumable and reconcilable.

It does not justify a generic workflow engine or shared-write media relationship authority.

#### No platform-wide atomic replacement transaction

Cross-domain replacement does not require one database transaction spanning unrelated owners.

Each owner establishes its own valid transition.

Partial progress remains explicit and recoverable.

A coordinated all-at-once release boundary requires separate product/domain evidence and is not assumed globally.

#### Semantic completion differs from worker completion

A bulk operation cannot claim replacement complete merely because a worker ended.

Conceptual result classes include:

- updated;
- already no longer referenced;
- incompatible;
- requires governed successor;
- retry pending;
- failed.

Exact operational representation remains JIT.

#### Bounded lag is acceptable for ordinary editorial discovery

Ordinary “where used?” screens may tolerate bounded derived-index lag if represented appropriately.

That does not weaken authoritative replacement/revalidation semantics.

#### Empty reverse index is not safety proof

For destructive deletion, high-impact replacement or withdrawal:

```text
usage_index.count(M4) == 0
```

does not prove there are no authoritative dependencies.

Likewise, missing search results do not prove absence.

#### Every media-reference owner needs deterministic dependency reconciliation

Any Domain/resource class permitted to retain governed MediaAsset references must expose an owner-mediated way for safety/deletion/replacement orchestration to discover/reconcile those references.

Exact API/query/action mechanics remain JIT.

This does not require a new Resource per Domain.

#### Projection lag/reordering cannot create authority

Projection updates may be delayed, duplicated or reordered.

Projection state reconciles against authoritative owner identity/revision/state rather than treating event arrival order as business truth.

#### Projection repair follows authority

If:

```text
index says D7 → M4
actual D7 → M9
```

repair means:

```text
fix projection
```

not:

```text
change D7 back to M4
```

#### Unified cross-domain usage view remains projection only

An operator may see one aggregated usage view across Content & Media, Events & Live, Commerce, Communications and other owners.

That unified experience does not transfer ownership of the underlying references into C&M.

#### Current versus historical usage stays distinguishable

Operator usage views should distinguish, where derivable from owners:

- current mutable use;
- current delivered/published use;
- historical immutable use.

The projection displays/derives those facts; it does not create them.

#### Replacement lineage is advisory to consumers

A successor relation can power:

- suggested replacement;
- impact analysis;
- editorial warning.

It does not cause runtime auto-resolution or automatic mutation.

Replacement existence does not imply Withdrawal.

Withdrawal does not require a replacement to exist.

#### Beacon stable has no direct donor

Beacon stable `v0.5.1` built-in image rendering uses filename-based lookup through `beacon_media_url(@name)` / `url_for_asset(file_name)`.

That is convenient CMS rendering but does not provide:

- exact durable consumer→MediaAsset reference authority;
- usage-reference provenance;
- reverse dependency discovery;
- immutable-versus-mutable replacement semantics;
- owner-mediated replacement orchestration.

Beacon's `source_id` / `usage_tag` indexes address derivative lineage only.

Block 4A.5 therefore has **NO DIRECT BEACON DONOR** beyond general media-library/editorial convenience inspiration.

### 6.110 ACCEPTED GRILL DECISION

#### `GRILL-35 — Media Consumers Own Exact Forward Asset References; Reverse Usage Indexing Is Derived/Rebuildable, and Replacement Is Owner-Mediated Against the Exact Expected Reference`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

**Current-status note (v0.37.0):** GRILL-36 refines governed forward references from exact stable `MediaAsset` identity to exact `MediaAssetVersion`; owner authority, expected-old-reference protection and derived/rebuildable reverse indexing remain accepted.

> Every governed media consumer stores or otherwise owns an exact forward reference to the concrete `MediaAsset` identity it uses. File names, storage keys, URLs, replacement pointers and reverse-index rows do not substitute for that relationship.
>
> The Domain/resource containing the consumer record remains authoritative for the media-reference relationship. Content & Media does not become a shared-write owner merely because it owns the referenced MediaAsset.
>
> Immutable governed consumers retain their exact historical MediaAsset references forever unless their own governing deletion/privacy policy requires otherwise. Media replacement does not silently rewrite immutable Content Versions, Plans, messages, Event records or other historical truth.
>
> Mutable authoring/consumer state may explicitly adopt a replacement asset through the owning Domain/resource action.
>
> NewYou does not introduce a generic runtime “follow current/latest media replacement” pointer for ordinary governed references. Material media replacement lineage is advisory/provenance for consumers; it does not dynamically rewrite resolution.
>
> Content & Media may maintain a derived reverse usage/dependency projection so editors/operators can discover where an exact MediaAsset appears.
>
> The reverse projection may include sufficient non-authoritative locator/context data to return to the owner—such as owner/domain kind, exact consumer identity, reference location/role and lifecycle context—but its exact schema remains JIT.
>
> The reverse usage projection is rebuildable from authoritative forward references and is never sole authority for whether a relationship exists.
>
> Loss, lag, corruption or rebuild of the reverse projection may degrade editorial convenience but cannot erase, create or redefine the underlying forward references.
>
> Projection maintenance does not require every owning Domain to synchronously dual-write into a shared C&M business table as part of its authoritative transaction.
>
> Replacement operations discovered through the reverse projection invoke the owning Domain/resource rather than directly mutating foreign persistence.
>
> Each owner revalidates that the targeted record still references the exact expected predecessor MediaAsset before replacement. Stale replacement attempts fail/return conflict rather than using last-write-wins semantics.
>
> Each owner validates the successor MediaAsset against its own bounded reference contract, lifecycle, rights/exposure requirements and other applicable invariants. Content & Media does not create a universal cross-domain compatibility oracle.
>
> Mutable references, immutable references, current published references and foreign-domain references may have different replacement semantics. There is no single cross-platform SQL-style “replace everywhere” mutation.
>
> A current immutable/published Content Version that must adopt a replacement media asset does so through the existing draft/successor-version/Review/Approval/Publication path rather than in-place mutation.
>
> Bulk replacement may exist as durable orchestration over owner-mediated operations. It is idempotent, resumable and reconcilable where partial completion matters, but it does not become a shared-write authority or generic workflow engine.
>
> Cross-domain bulk replacement does not require one global atomic database transaction. Each owner establishes its own valid transition; partial results remain visible and recoverable.
>
> A bulk-replacement operation cannot report semantic completion merely because its worker finishes. Updated, stale/no-longer-referenced, incompatible, requires-successor, retry-pending and failed outcomes remain distinguishable conceptually; exact operational representation remains JIT.
>
> Ordinary editorial “where used?” views may tolerate bounded derived-index lag.
>
> High-impact replacement, Withdrawal and especially physical deletion do not treat an empty/stale reverse index as proof of no authoritative usage.
>
> Every Domain/resource class permitted to retain governed MediaAsset references must expose a deterministic owner-mediated dependency-discovery/reconciliation path sufficient for safety/deletion workflows. Exact interface/query mechanics remain JIT.
>
> The reverse projection accelerates that discovery but does not replace those owner contracts.
>
> Projection updates may arrive late, duplicate or reorder. Projection state reconciles against current authoritative owner state/revision rather than inferring truth from transport order.
>
> Projection reconciliation repairs the projection when it disagrees with an authoritative owner; it never mutates the owner merely to make the index agree.
>
> A unified operator usage view may aggregate references across Domains without transferring ownership of those references to Content & Media.
>
> Current mutable/delivered usage should remain distinguishable from immutable historical usage for operator interpretation, but the projection does not invent those lifecycle facts.
>
> Media replacement/successor lineage may power operator suggestions and impact analysis but never causes references to resolve automatically to the successor.
>
> Replacement existence does not imply Withdrawal, and Withdrawal does not require that a replacement already exist.
>
> Beacon stable `v0.5.1` filename-based `beacon_media_url(@name)` / `url_for_asset(file_name)` resolution is **REJECTED** as NewYou governed media-reference authority. Beacon's derivative `source_id`/`usage_tag` indexes do not provide the required consumer usage/dependency model.
>
> Block 4A.5 therefore has **NO DIRECT BEACON DONOR** beyond general Media Library/editorial convenience inspiration.
>
> No direct Beacon runtime dependency is introduced by this decision.

### 6.111 Consequences fixed for later grills

1. Governed consumers own exact forward MediaAsset references.
2. File names, URLs, storage keys, successor pointers and reverse indexes are not relationship authority.
3. C&M owns the MediaAsset, not every foreign relationship to it.
4. Immutable consumers never silently follow replacement.
5. Mutable consumers may explicitly adopt replacement through owner actions.
6. No generic runtime latest-media pointer is introduced.
7. Reverse usage/dependency indexing is derived and rebuildable.
8. Reverse index loss/lag/corruption cannot erase or create business relationships.
9. Synchronous cross-domain dual-write into a shared C&M usage authority is not required.
10. Reverse-index rows identify candidates only; they never authorise mutation.
11. Owner-mediated replacement revalidates the exact expected old reference.
12. Stale replacement fails/conflicts rather than overwriting a newer owner state.
13. Successor compatibility belongs to the consuming owner.
14. No universal cross-domain replacement compatibility oracle is introduced.
15. Immutable/current-published references use successor-version/correction semantics rather than in-place mutation.
16. Bulk replacement may be durable orchestration but never shared-write authority.
17. No global atomic transaction is required across Domains.
18. Partial replacement outcomes remain explicit/recoverable.
19. Worker completion does not prove semantic bulk-replacement completion.
20. Ordinary editorial where-used views may tolerate bounded index lag.
21. Empty/stale reverse index is never proof of no dependency for high-impact/destructive operations.
22. Media-reference-bearing owners expose deterministic dependency discovery/reconciliation.
23. Projection events may lag/duplicate/reorder and reconcile from owner truth.
24. Projection repair never mutates owners to make the index agree.
25. Unified cross-domain usage view remains projection only.
26. Current/delivered/historical usage remains distinguishable for operator context.
27. Replacement lineage is advisory/provenance, never automatic mutation.
28. Replacement and Withdrawal remain independent.
29. Beacon filename-based media resolution is rejected as governed reference authority.
30. Block 4A.5 has no direct Beacon donor.
31. **Historical at GRILL-35 acceptance:** Block 4A.6 performed the first media-branch closure audit and BLOCKED/STOPPED on the media-version gap later resolved by GRILL-36.

### 6.112 Block 4A.6 closure audit — BLOCKED / STOP pending media version semantics

The first Block 4A closure audit re-evaluated `GRILL-31` through `GRILL-35` against current live NewYou authority.

The chain is coherent across:

- platform-owned media identity;
- provider-independent storage;
- restricted ingest and verified object-store finalisation;
- exact source/derivative lineage;
- rights/provenance;
- media Publication and protected delivery;
- Withdrawal versus physical deletion;
- owner-owned forward references;
- derived reverse usage indexing and owner-mediated replacement.

However, higher authority exposes one unresolved semantic contradiction.

Platform Law requires governed media assets to record:

```text
type and version
owner
licence and usage rights
source and creator
alt text and captions
locale-specific text
accessibility transcript
risk class
publication state
checksum
storage location
replacement relationships
```

Domain Law also assigns Content & Media ownership of editorial/media version lineage.

The current GRILL-31→35 model has stable exact `MediaAsset` identity but no immutable media-version authority. That creates unsafe choices for changes such as corrected locale-specific alt text or accessibility metadata:

```text
mutate MediaAsset in place
→ destroys historical version provenance

mint unrelated MediaAsset identity
→ overstates conceptual replacement and may duplicate storage unnecessarily

leave metadata unversioned
→ contradicts higher-authority media version lineage
```

Therefore Block 4A cannot close safely without separating stable conceptual media identity from exact immutable media-version truth.

The audit outcome before GRILL-36 is:

```text
Block 4A
→ BLOCKED / STOP for semantic closure
```

This is a deliberate correction from the earlier tentative closure direction and is required by higher authority.

The same audit also confirmed that OQ-014, OQ-020, OQ-021, OQ-024, OQ-029, OQ-030, OQ-031, OQ-032 and IP/licence/contributor-rights gates remain downstream authority/proof/policy work and must not be silently solved inside this dossier.

### 6.113 ACCEPTED GRILL DECISION

#### `GRILL-36 — Governed Media Separates Stable MediaAsset Identity from Immutable MediaAssetVersion Truth; Publication, Provenance and Governed Consumer References Pin the Exact Version`

**Status:** ACCEPTED by the human project owner on 2026-09-20.

**Current-status note (v0.38.0):** GRILL-37 resolves the deletion/shared-byte ambiguity exposed by this version model. GRILL-36's stable identity, immutable version, exact Publication/provenance/reference and same-asset byte-sharing semantics remain accepted.

> `MediaAsset` is the stable conceptual Content & Media identity for one governed media object. `MediaAssetVersion` is the immutable governed revision containing the exact media-version truth used for provenance, publication and governed delivery.
>
> A dedicated MediaAsset/MediaAssetVersion identity-version separation is now justified by Platform Law requiring media `type and version`, Domain Law requiring editorial/media version lineage, and the requirement to preserve media/version provenance without forcing metadata-only corrections to mint unrelated conceptual asset identities or destructively overwrite history.
>
> This decision explicitly supersedes only the `GRILL-31` conclusion that no separate MediaAssetVersion hierarchy is initially required. All other GRILL-31 provider-independence, storage-authority and derivative-identity conclusions remain accepted.
>
> A genuinely distinct governed media object—such as a source recording, approved replay, promotional clip, responsive derivative, caption-track asset or other independently governed derivative—retains its own stable MediaAsset identity.
>
> Revisions of that same conceptual media object create immutable successor MediaAssetVersions rather than silently replacing prior governed state.
>
> A new binary, materially changed governed media metadata, or another change that must preserve historical version provenance creates successor MediaAssetVersion truth according to bounded policy. Exact version-cut rules remain JIT.
>
> A metadata-only successor version may retain the same exact immutable binary/storage object when the bytes and checksum are unchanged. NewYou does not duplicate binary bytes merely to version governed metadata.
>
> A materially changed binary creates a successor MediaAssetVersion with exact new checksum/storage provenance.
>
> No dedicated `MediaBlob` business Resource is introduced initially. Exact immutable byte identity remains represented through version storage/checksum provenance unless later evidence justifies a separate blob abstraction.
>
> Every durable derivative version records provenance to the exact source MediaAssetVersion from which it was produced. Stable asset-level derivative relationships may exist for navigation/grouping but never replace exact source-version provenance.
>
> A later source version never rewrites an already-created derivative version's source provenance.
>
> Governed immutable consumers pin the exact MediaAssetVersion they use. Stable MediaAsset identity, replacement relationships, filenames, URLs or “current version” pointers never substitute for exact historical version references.
>
> This refines `GRILL-35`: its owner-owned forward-reference and derived reverse-index principles remain accepted, but governed references are version-exact.
>
> Mutable authoring may explicitly adopt a different MediaAssetVersion or a version of a replacement MediaAsset through the owning action. No generic runtime “follow latest media version” rule is introduced.
>
> Media Publication activates one exact MediaAssetVersion. Creating a successor version does not automatically republish or supersede the previously published version.
>
> This refines `GRILL-33` without changing its ownership boundary: C&M still owns media Publication; Entitlements, Events & Live, Identity & Access and Privacy & Consent retain their own current authority.
>
> Storage ingest/finalisation under `GRILL-32` applies to the exact MediaAssetVersion being created. Checksum, byte size, storage locator and processing provenance are version-exact facts.
>
> Short localisable accessibility/editorial metadata—including alt text, display captions and locale-specific descriptive text—belongs to governed media-version truth and must remain immutable/version-addressable per applicable locale rather than being destructively edited on a published historical version.
>
> Exact persistence for locale-specific media metadata remains JIT. A dedicated locale-metadata Resource is justified only if its independent lifecycle/approval/query invariants require it; an unrestricted generic metadata map is not accepted as the governance boundary.
>
> Durable caption tracks, transcript files and other independently deliverable/access-controlled accessibility artefacts may remain derivative MediaAssets with their own MediaAssetVersions. This avoids making the same durable artefact both free-form metadata and independent media authority.
>
> Historical media-version rights/provenance/risk evidence remains distinguishable from current rights/consent/publication eligibility.
>
> Withdrawal, correction and physical deletion may target the narrowest governed media subject required by policy—an exact MediaAssetVersion or a broader stable MediaAsset scope—without rewriting version lineage.
>
> Physical deletion of one version does not erase the historical identity/version lineage required for lawful minimal non-reconstructive evidence, subject to the existing privacy/deletion rules.
>
> Provider object locators remain infrastructure state. Where multiple versions of the same stable MediaAsset legitimately share identical immutable bytes, carrying forward the exact same stored object/checksum does not constitute cross-asset locator reuse.
>
> A provider locator is still never reassigned to a different stable MediaAsset or materially different byte identity.
>
> Exact version numbering, successor constraints, current-editorial-version selection, concurrency/indexes, locale-metadata Resource topology and Ash actions remain JIT provided they preserve these semantics.
>
> Beacon provides **NO DIRECT DONOR** for this version model. Its stable Asset identity and source lineage remain conceptual inspiration only.
>
> No direct Beacon runtime dependency is introduced by this decision.

### 6.114 Supersession and refinement map

`GRILL-36` does not silently rewrite historical accepted decisions.

It explicitly changes only these narrow current semantics:

```text
GRILL-31 historical conclusion:
no MediaAssetVersion hierarchy initially
→ SUPERSEDED by GRILL-36

GRILL-31 historical replacement wording:
material replacement always creates a new MediaAsset identity
→ REFINED:
   distinct conceptual media object/replacement may create a new MediaAsset;
   revision of the same conceptual media object creates a new MediaAssetVersion

GRILL-35 historical governed forward-reference wording:
consumer → exact MediaAsset
→ REFINED:
   governed consumer → exact MediaAssetVersion
   stable MediaAsset remains conceptual grouping/identity

GRILL-33 historical Publication wording:
Publication → exact MediaAsset
→ REFINED:
   Publication → exact MediaAssetVersion

GRILL-32 storage/provenance wording:
MediaAsset checksum/storage facts
→ REFINED:
   checksum / byte size / storage locator / processing provenance are exact MediaAssetVersion facts
```

Unchanged accepted semantics include:

- Content & Media owns stable platform media identity;
- S3-compatible providers own bytes/locators only, never business identity;
- Wasabi-or-equivalent remains a replaceable deployment direction;
- masters/sources and separately governed derivatives each have stable MediaAsset identity;
- no separate `MediaDerivative` Resource is required merely because an asset is derived;
- source/derivative provenance is exact and immutable;
- restricted staging and durable accepted-ingest intent remain required;
- storage/provider calls remain outside PostgreSQL transactions;
- workers/providers remain non-authoritative;
- rights, Publication, Entitlements, Events admission, Identity and Consent authorities remain separate;
- Withdrawal and physical deletion remain separate;
- deletion remains durable/reconcilable/non-resurrecting;
- consumers remain authority for their own media references;
- reverse usage indexes remain derived/rebuildable;
- replacement remains owner-mediated;
- no generic Task, MediaProcessingAttempt, MediaDeletionAttempt, MediaAccessGrant or MediaBlob business Resource is justified.

### 6.115 Consequences fixed for later grills

**Current-status note (v0.38.0):** consequences 24–26 are refined by GRILL-37 so version/asset disposition scope and shared-byte destruction are explicit; all other GRILL-36 consequences remain current.

1. `MediaAsset` is stable conceptual media identity.
2. `MediaAssetVersion` is immutable governed media revision truth.
3. The narrow no-version-hierarchy conclusion in GRILL-31 is explicitly superseded.
4. Distinct governed media objects/derivatives retain distinct stable MediaAsset identities.
5. Revisions of one conceptual media object create successor MediaAssetVersions.
6. Metadata-only versions may share the same immutable stored bytes when checksum is unchanged.
7. Material binary change produces a new MediaAssetVersion with new exact byte/storage provenance.
8. No MediaBlob business Resource is introduced initially.
9. Derivative provenance pins exact source MediaAssetVersion.
10. Stable asset-level derivative grouping never replaces exact version provenance.
11. Governed immutable consumers pin exact MediaAssetVersion.
12. GRILL-35's owner/reverse-index model remains accepted but is version-exact.
13. Mutable authoring may explicitly adopt another version; no follow-latest rule exists.
14. Media Publication activates exact MediaAssetVersion.
15. Successor version creation never automatically republishes.
16. GRILL-33 ownership boundaries remain unchanged.
17. GRILL-32 ingest/storage reconciliation applies to exact MediaAssetVersion.
18. Checksum, byte size, storage locator and processing provenance are version-exact.
19. Localisable alt text/display captions/descriptive text are governed immutable/version-addressable media-version truth.
20. Exact locale metadata Resource topology remains JIT.
21. No unrestricted generic metadata map may own governed locale/accessibility truth.
22. Durable caption tracks/transcript files may be derivative MediaAssets with their own versions.
23. Historical rights/provenance/risk evidence remains separate from current eligibility.
24. Withdrawal/correction/deletion may target exact version or broader asset scope according to policy.
25. Same immutable bytes may be carried across versions of the same stable MediaAsset without object duplication.
26. Provider locators remain infrastructure state and are never reassigned across different stable assets/material byte identities.
27. Exact version numbering/current-editorial selection/indexes/actions remain JIT.
28. Beacon has no direct donor for the version model.
29. **Historical at GRILL-36 acceptance:** Block 4A.7 re-ran semantic closure and BLOCKED/STOPPED only on the deletion subject/shared-byte ambiguity later resolved by GRILL-37.
30. OQ-014/OQ-020/OQ-021/OQ-024/OQ-029/OQ-030/OQ-031/OQ-032 and IP/licence/contributor-rights gates remain open at their proper authority levels.

### 6.116 Block 4A.7 corrected closure audit — BLOCKED / STOP on deletion subject/byte-sharing semantics only

Block 4A.7 re-evaluated `GRILL-31` through `GRILL-36` as one coherent media model against the current live NewYou authority generation.

The corrected identity/version model passes the following semantic seams:

- stable `MediaAsset` conceptual identity;
- immutable `MediaAssetVersion` truth;
- exact source/derivative version lineage;
- restricted ingest and verified storage finalisation;
- version-exact rights/provenance and Publication;
- current-authority protected delivery;
- locale/accessibility metadata ownership;
- exact governed consumer forward references;
- derived/rebuildable reverse usage indexing;
- owner-mediated replacement;
- cross-domain ownership boundaries.

One genuine contradiction remains between GRILL-34 and GRILL-36.

GRILL-34 predates `MediaAssetVersion` and states that physical deletion of exact MediaAsset bytes is terminal for that exact media identity and that a later upload of identical bytes creates a new `MediaAsset`.

GRILL-36 later permits both:

```text
version-scoped deletion
```

and:

```text
MediaAsset M1/v1
MediaAsset M1/v2
→ same immutable object/checksum when bytes are unchanged
```

That creates an unresolved case:

```text
M1/v1 ─┐
       ├── immutable object O / checksum X
M1/v2 ─┘

policy requires deletion/disposition of M1/v1 only
```

Destroying object `O` would wrongly destroy bytes still lawfully required by `M1/v2`.

Keeping object `O` is safe only if the dossier explicitly states that continued physical byte existence does not preserve delivery, Publication, reference or derivative authority for the deleted/suppressed `M1/v1`.

The model must also distinguish:

```text
exact version terminality
≠ stable asset terminality
≠ physical byte destruction
```

and must prevent byte sharing from becoming a loophole when policy requires the bytes themselves to cease existing.

This is semantic architecture, not OQ-030 provider detail. OQ-030 may decide how object versions/processors are deleted and verified; it cannot decide which governed identity is terminal or whether another still-lawful version may keep shared bytes.

The audit result is therefore:

```text
Block 4A.7
→ BLOCKED / STOP
→ one narrow deletion-scope refinement required
```

No other GRILL-31→36 seam is reopened.

### 6.117 ACCEPTED GRILL DECISION

#### `GRILL-37 — Media Deletion Is Scoped to the Governed Version or Stable Asset Subject; Shared Immutable Bytes Survive Only While Another Lawfully Retained Version Requires Them, and Deleted Identities Never Resurrect`

**Status:** ACCEPTED by the human project owner on 2026-09-21.

> A media deletion/disposition obligation identifies its governed subject explicitly: an exact `MediaAssetVersion`, an entire stable `MediaAsset`, or another policy-derived set of exact versions. Physical byte cleanup follows that governed subject/impact determination; object-store identity does not define the business scope.
>
> Version-scoped deletion/suppression permanently makes that exact `MediaAssetVersion` unavailable for new Publication, new governed references, protected/public delivery and authoritative derivative finalisation as soon as the obligation becomes effective, before asynchronous physical cleanup completes.
>
> Version-scoped deletion does not erase historical version identity/lineage that may lawfully remain as minimal non-reconstructive evidence under the existing privacy/retention rules.
>
> Where another lawfully retained `MediaAssetVersion` of the same stable `MediaAsset` legitimately depends on the exact same immutable stored bytes/checksum, continued existence of those shared bytes does not preserve any Publication, reference, delivery or derivative-finalisation authority for the deleted/suppressed version.
>
> Shared physical bytes are destroyed only when the governing disposition scope requires their destruction and no lawfully retained in-scope version may continue to depend on that representation.
>
> If the governing privacy, rights, legal, retention or other disposition policy requires the bytes themselves to cease existing, the impact set expands to every `MediaAssetVersion` that depends on those exact bytes. Byte sharing may never be used to evade a deletion obligation.
>
> A `MediaAssetVersion` whose governed identity has been terminally deleted/retired/suppressed is never resurrected. Any later lawful revision is a new `MediaAssetVersion` with new version provenance even when its bytes/checksum are identical to historical bytes.
>
> Whole-asset terminal deletion/retirement is stronger than version-scoped disposition. Once the stable `MediaAsset` identity itself is terminally disposed, later reintroduction of identical bytes creates a new stable `MediaAsset` identity rather than resurrecting the old asset.
>
> A successor version may reuse immutable bytes already lawfully retained by another surviving version of the same stable `MediaAsset`. If those bytes were actually destroyed, a later re-upload creates new storage provenance even if the resulting checksum is identical.
>
> Exact source/derivative and consumer-dependency discovery for destructive disposition is version-exact and must account for shared-object dependencies before provider deletion. A stale/empty derived reverse-usage projection is never proof that deletion is safe.
>
> C&M or the platform deletion orchestrator must fail closed when it cannot establish whether a supposedly deletable object is still required by another lawfully retained version in the governed impact set.
>
> No `MediaBlob`, reference-count, storage-object business Resource or generic deletion-attempt Resource is introduced by this decision. Exact database constraints, storage-reference accounting, provider object/version handling, locking, reconciliation queries and deletion-worker mechanics remain JIT/proof detail provided they preserve these semantics.
>
> GRILL-34's Withdrawal-versus-deletion separation, immediate fail-closed suppression, durable/idempotent/retryable deletion workflow, derivative-impact policy, external-provider verification, full-deletion orchestration and backup non-resurrection semantics remain accepted.
>
> GRILL-36's stable `MediaAsset` / immutable `MediaAssetVersion` model, exact version provenance, metadata-only byte sharing and no-`MediaBlob` conclusion remain accepted.
>
> OQ-030 retains provider/processor deletion-inventory and verification authority; OQ-031 retains restore/deletion replay authority; OQ-032 retains platform deletion/export operations authority. This decision closes none of those gates.
>
> No direct Beacon runtime dependency is introduced by this decision.

### 6.118 Supersession and refinement map

`GRILL-37` does not silently rewrite historical accepted decisions.

It explicitly refines only the deletion/non-resurrection portions affected by the identity/version split:

```text
GRILL-34 historical terminality wording:
physical deletion of exact MediaAsset bytes
→ terminal for that exact media identity
→ identical later bytes require new MediaAsset

REFINED by GRILL-37:
version-scoped terminal disposition
→ exact MediaAssetVersion never resurrects
→ shared bytes may remain while another lawfully retained version requires them

whole-asset terminal disposition
→ stable MediaAsset never resurrects
→ identical later bytes require new stable MediaAsset

byte-destruction obligation
→ applies to every version depending on those bytes
```

GRILL-36 historical deletion wording:

```text
withdrawal/correction/deletion may target exact MediaAssetVersion or broader MediaAsset
+
multiple same-asset versions may share exact immutable bytes
```

is retained and completed by GRILL-37's explicit subject/byte-sharing disposition rules.

Unchanged accepted semantics include:

- stable `MediaAsset` conceptual identity;
- immutable `MediaAssetVersion` truth;
- exact source-version derivative provenance;
- exact governed consumer references;
- exact Media Publication target;
- restricted staging and verified storage finalisation;
- providers/workers remain non-authoritative;
- rights/current eligibility separation;
- bounded protected delivery;
- Withdrawal remains separate from physical deletion;
- consumers own their own forward references;
- reverse usage indexes remain derived/rebuildable;
- replacement remains owner-mediated;
- deletion remains durable/idempotent/retryable/observable/reconcilable;
- restore never resurrects current authority;
- no generic Task, `MediaBlob`, `MediaProcessingAttempt`, `MediaDeletionAttempt`, `MediaAccessGrant` or storage-reference business Resource is justified.

### 6.119 Consequences fixed for later grills

1. Every deletion/disposition obligation identifies exact governed version/asset scope.
2. Version-scoped suppression immediately blocks new Publication, references, delivery and derivative finalisation.
3. Physical byte existence never preserves authority for a suppressed/deleted version.
4. Shared same-asset bytes may survive only while another lawfully retained version requires them.
5. Byte-level destruction expands to every version dependent on those bytes.
6. Byte sharing never evades privacy/rights/legal/retention deletion policy.
7. A terminally disposed `MediaAssetVersion` never resurrects.
8. A later revision is a new MediaAssetVersion even when checksum/bytes match historical material.
9. Whole-asset terminal disposition permanently retires that stable MediaAsset identity.
10. Identical later bytes after whole-asset terminal disposition require a new stable MediaAsset.
11. Re-upload after actual byte destruction creates new storage provenance even if checksum matches.
12. Destructive dependency discovery is version-exact and accounts for shared-object dependencies.
13. Empty/stale reverse usage projection is never proof of safe deletion.
14. Uncertain shared-byte dependency fails closed.
15. No MediaBlob/reference-count/storage-object business Resource is introduced initially.
16. Exact storage-reference accounting/locking/index/query/worker mechanics remain JIT/proof detail.
17. GRILL-34 remains accepted except for the explicitly refined terminality/object-sharing wording.
18. GRILL-36 remains accepted and is completed by the subject-scoped deletion rules.
19. OQ-030/OQ-031/OQ-032 remain open at their proper authority levels.
20. **Historical at GRILL-37 acceptance:** Block 4A.8 was required as the final corrected semantic closure audit; it subsequently PASSED and closed Block 4A through GRILL-38 in v0.39.0.

### 6.120 Block 4A.8 final corrected closure audit — PASS / semantic closure justified

Block 4A.8 re-evaluated `GRILL-31` through `GRILL-37` as one coherent media model with both the GRILL-36 and GRILL-37 supersession/refinement maps applied.

The audit finds no remaining semantic contradiction across the required closure surface:

| Semantic seam | Result | Closure finding |
|---|---|---|
| stable media identity | PASS | `MediaAsset` remains the stable conceptual identity independent of provider/object identifiers. |
| immutable media versions | PASS | `MediaAssetVersion` owns exact immutable revision truth and historical provenance. |
| source/derivative version lineage | PASS | derivatives pin exact source versions; later versions cannot rewrite provenance. |
| ingest/storage authority | PASS | restricted staging, durable accepted intent, verified object-store finalisation and reconciliation preserve platform/PostgreSQL authority. |
| rights/provenance | PASS | historical evidence, current rights eligibility and Publication remain separate governed dimensions. |
| locale/accessibility metadata | PASS | exact version-addressable metadata is governed without requiring a generic locale Resource. |
| Publication | PASS | Publication targets an exact eligible `MediaAssetVersion`; successor creation does not auto-publish. |
| protected delivery | PASS | current C&M eligibility composes with current owning-domain access/consent authority before bounded delivery capability is issued. |
| Withdrawal | PASS | delivery authority can be removed immediately without pretending physical deletion has completed. |
| physical deletion / non-resurrection | PASS | GRILL-37 now distinguishes exact-version terminality, whole-asset terminality and physical byte destruction, including lawful same-asset byte sharing. |
| exact forward references | PASS | governed consumers own exact `MediaAssetVersion` references. |
| reverse usage indexing | PASS | reverse usage remains derived/rebuildable and never becomes write authority. |
| replacement | PASS | same conceptual object creates successor version; genuinely distinct object creates distinct stable asset; owner-mediated replacement never means implicit follow-latest. |
| dependency discovery | PASS | destructive operations are version-exact, shared-byte aware and fail closed when derived dependency evidence is uncertain. |
| cross-domain ownership | PASS | Content & Media retains media authority while Entitlements, Events/Live, IAM, Privacy/Consent and other owners retain their own current business truth. |

The remaining open work is downstream rather than another pre-JIT semantic gap. In particular, the audit does **not** resolve or absorb:

- OQ-014 edge/cache/signed-delivery design;
- OQ-020 live/video vendor validation;
- OQ-021 recording/video consent and retention;
- OQ-024 source-content/media inventory;
- OQ-029 retention schedule matrix;
- OQ-030 external-processor deletion inventory;
- OQ-031 backup restore/deletion replay;
- OQ-032 deletion/export operations;
- IP/licence/model/book/translation/contributor-rights review;
- exact Ash Resource/action/relationship design;
- exact fields, constraints, identities and indexes;
- exact storage-reference/shared-object accounting implementation;
- provider object/version APIs and object-key mechanics;
- Oban jobs/queues/retry settings;
- media processor/transcoder contracts;
- signed-delivery token shape and CDN/cache topology;
- operational thresholds, alerts and reconciliation implementation.

Those details remain JIT/proof/policy/vendor work unless later evidence changes authoritative ownership or lifecycle semantics.

The Block 4A.8 result is therefore:

```text
Block 4A media branch
→ CLOSED / PASS FOR CONTENT & MEDIA JIT HANDOFF
→ semantic reuse-discovery complete at current scope
→ implementation NOT AUTHORISED
```

No further media GRILL is justified merely because downstream implementation detail remains undecided.

### 6.121 ACCEPTED GRILL DECISION

#### `GRILL-38 — The Media Identity / Version / Ingest / Rights / Publication / Delivery / Withdrawal / Deletion / Usage-Reference Branch Is Semantically Closed for Content & Media JIT Handoff`

**Status:** ACCEPTED by the human project owner on 2026-09-21.

> Block 4A is **CLOSED / PASS FOR CONTENT & MEDIA JIT HANDOFF** at the reuse-discovery and semantic-architecture level.
>
> `GRILL-31` through `GRILL-37`, interpreted through the explicit GRILL-36 and GRILL-37 supersession/refinement maps, form one coherent media model.
>
> `MediaAsset` owns stable conceptual media identity. `MediaAssetVersion` owns immutable exact revision truth. Governed consumers, Publication and derivative provenance pin exact versions.
>
> Restricted ingest, durable accepted intent, external storage work, verification and authoritative finalisation preserve PostgreSQL/platform authority while S3-compatible providers remain byte/storage infrastructure only.
>
> Rights/provenance evidence, current eligibility, Publication and actor delivery authority remain separate dimensions. Protected delivery composes current owning-domain authority into a bounded technical capability.
>
> Withdrawal and physical disposition remain distinct. Version-scoped disposition permanently suppresses the exact version; whole-asset terminal disposition permanently retires the stable asset identity; shared immutable bytes survive only while another lawfully retained version requires them; byte-destruction obligations expand to every dependent version.
>
> Owner Domains retain authoritative exact forward `MediaAssetVersion` references. Reverse usage/dependency indexing remains derived and rebuildable. Replacement and destructive disposition are owner-mediated and fail closed against stale or uncertain dependency information.
>
> No semantic requirement justifies a generic `MediaBlob`, storage-reference, `MediaProcessingAttempt`, `MediaDeletionAttempt`, `MediaAccessGrant`, Task or workflow business Resource.
>
> Exact Ash Resources/actions/relationships, database fields/indexes/constraints, version numbering, storage-reference accounting, provider APIs, object-key generation, Oban jobs/queues, processing contracts, signed-delivery mechanisms, cache topology, retention settings and operational thresholds remain JIT/proof details unless later evidence changes authoritative ownership or lifecycle semantics.
>
> Existing OQ, legal/IP, vendor, retention, privacy, deletion/recovery and proof gates remain in force. This closure does not resolve them.
>
> Beacon remains a selective concept/source donor only. No Beacon or LiveAdmin runtime authority/dependency is introduced.
>
> Reopen Block 4A only for new higher-authority contradiction, materially changed scope, or new evidence exposing an actual semantic inconsistency—not because downstream implementation detail remains undecided.
>
> This closure does **not** authorise implementation. Normal Feature Pack/JIT/development-entry gates remain controlling.

### 6.122 Closure consequences fixed for JIT handoff

1. Block 4A is semantically CLOSED / PASS at current reuse-discovery scope.
2. Stable `MediaAsset` identity and immutable `MediaAssetVersion` truth remain separate.
3. Publication, derivative provenance and governed consumer references pin exact versions.
4. Ingest/storage providers and async workers remain infrastructure/execution, never media authority.
5. Rights/provenance evidence, current eligibility, Publication and delivery authority remain distinct.
6. Protected delivery revalidates current owning-domain authority before issuing bounded capability.
7. Withdrawal remains distinct from physical deletion.
8. Version-scoped disposition permanently suppresses the exact version identity.
9. Whole-asset terminal disposition permanently retires the stable asset identity.
10. Same-asset immutable bytes may remain shared only while another lawfully retained version requires them.
11. Byte-destruction policy expands to every dependent version and cannot be bypassed by sharing.
12. Owner Domains retain authoritative exact forward references.
13. Reverse usage/dependency indexes remain derived/rebuildable acceleration only.
14. Replacement and destructive disposition remain owner-mediated and expected-reference/version exact.
15. Destructive dependency discovery fails closed on stale, empty or uncertain derived evidence.
16. No generic `MediaBlob`, storage-reference, Task, workflow, processing-attempt, deletion-attempt or access-grant business Resource is justified by current evidence.
17. OQ-014/OQ-020/OQ-021/OQ-024/OQ-029/OQ-030/OQ-031/OQ-032 and legal/IP/vendor/proof gates remain open at their proper authority levels.
18. Exact implementation topology remains JIT/proof work.
19. Beacon/LiveAdmin remain selective donors, not runtime authority/dependency.
20. Block 4A may be reopened only by higher-authority contradiction, materially changed scope or genuinely new semantic evidence.
21. This closure authorises no executable development.

### 6.123 Post-media seam selection

Block 4A media reuse discovery remains closed. The next Beacon seam is selected from an actual FP-001 Content & Media pressure rather than dossier-completeness pressure.

FP-001 requires a genuinely useful bilingual public boundary. Current Product Law gives each real translation its own approved slug/metadata and canonical URL, requires real translation alternates, and requires permanent redirects after slug changes. The frozen Frontend Experience System additionally requires clean stable human-readable canonical URLs, governed redirects without loops/chains or silent historical-route destruction, language/locale alternate relationships and first-slice SEO correctness.

The previously accepted Content/Publication decisions establish exact locale versions and exact Publication targets but do not yet settle what happens to an address after it has been publicly exposed. That makes public bilingual addressability the first justified post-media seam.

### 6.124 Block 5A.1 pressure test — locale public addressability and redirect history

#### Governing semantic distinction

A locale slug/path begins as governed editorial/version data. Before public exposure, changing it is ordinary authoring/version evolution.

Once an eligible Publication exposes that address publicly, the address gains durable external meaning because search engines, inbound links, bookmarks, analytics evidence and previously emitted links may depend on it. It can no longer be treated as merely mutable renderer configuration.

The required split is therefore:

```text
locale authoring/version truth
→ desired slug/path wording

Publication
→ activates one exact eligible locale version

public route claim/history
→ records which public address is canonical now
→ preserves previously exposed addresses as historical aliases/redirects where applicable

Phoenix routing / ETS / generated routes / sitemap / search index / cache
→ delivery/projection/acceleration only
```

#### Stable Beacon evidence inspected

The current non-retired Beacon CMS package line remains `v0.5.1`. Hex also exposes retired `1.0.0` and `1.1.0` versions from an unrelated older project; those do not supersede the Beacon CMS `0.5.1` line.

Stable `v0.5.1` source inspected for this seam:

- `lib/beacon/content/page.ex` — mutable `path`, title/description/meta fields; `{path, site}` uniqueness;
- `lib/beacon/content.ex` — publishing creates a snapshot of the current Page and lists currently published page snapshots;
- `lib/beacon/router.ex` — mounts a broad catch-all LiveView route and exposes URL helpers;
- `lib/beacon/router_server.ex` — keeps current published path→page lookup in ETS;
- `lib/beacon/loader/routes.ex` — generates public page URLs from site prefix + Page path;
- `lib/beacon/web/controllers/sitemap_controller.ex` — derives sitemap rows from currently published pages.

Useful Beacon donor ideas:

- one unique effective path per site;
- a central public URL-generation boundary;
- explicit Phoenix mounting/prefix semantics;
- published content as sitemap input;
- runtime route lookup as a performance mechanism.

Direct authority reuse is rejected because Beacon's mutable `Page.path` + current published snapshot + ETS route lookup does not preserve NewYou's immutable locale-version/publication/address-history invariants.

#### Lifecycle and failure pressure

1. **Draft/pre-publication:** changing a never-published locale slug does not create historical redirect obligation.
2. **First Publication:** the effective locale address is claimed durably for the published content identity/scope.
3. **Same-address successor:** a new eligible locale Publication may replace the exact published target while keeping the external canonical address stable.
4. **Changed-address successor:** the new address becomes canonical and the previously exposed address remains a governed historical alias/redirect for the same conceptual content/locale.
5. **Repeated changes:** historical aliases should resolve directly to the current canonical eligible address rather than accumulate avoidable redirect chains.
6. **Concurrent activation:** two Publications cannot successfully claim the same effective public address. Scheduled activation must revalidate address availability atomically.
7. **Withdrawal/ineligibility:** an old alias cannot route around Withdrawal, access restriction or other current Publication ineligibility. Current eligibility is rechecked before redirect/delivery.
8. **Cross-route safety:** content-owned route claims may not shadow authentication, account, support, operator, API, asset or other application/system routes.
9. **Locale alternates:** language switching/alternate metadata resolves through the same conceptual ContentItem and currently eligible locale Publications; it is not a blind string rewrite between `/af/` and `/en/`.
10. **Restart/cache loss:** ETS/cache/generated route state may disappear and rebuild without losing address history or changing canonical truth.

The semantic requirement is real, but exact Ash Resource/table/index/normalisation/HTTP details remain JIT. No generic router Domain is justified.

### 6.125 ACCEPTED GRILL DECISION

#### `GRILL-39 — Published Locale Addresses Become Durable Content & Media Route Claims; Canonical URLs and Permanent Redirects Follow Exact Publication Truth While Phoenix Routing and Caches Remain Non-Authoritative`

**Status:** ACCEPTED by the human project owner on 2026-09-21.

> Locale-specific slug/path values originate in governed locale authoring and immutable locale-version truth. Before first public Publication they create no historical public-route obligation.
>
> Activation of an eligible public Publication claims its effective public address under Content & Media authority. A public address that has been exposed therefore has durable historical meaning distinct from mutable draft wording.
>
> A successor Publication using the same address changes the exact published target without creating a new external address identity.
>
> A successor Publication using a different address establishes the successor address as canonical and preserves previously published addresses as governed historical aliases/redirects for the same conceptual content and locale. Historical addresses are not silently reassigned to unrelated content while their redirect obligation remains.
>
> Historical aliases resolve to the current eligible canonical Publication rather than forming avoidable redirect chains. Withdrawal, access restriction, deletion/disposition where applicable, or other current ineligibility cannot be bypassed through an older alias.
>
> Public-address claims are unique within their governed routing scope. Competing concurrent Publications fail closed rather than allowing ambiguous routing. Scheduled Publication revalidates route availability at activation.
>
> Content & Media may claim only explicitly permitted public-content routing space. Application/system routes remain Phoenix/application authority and may not be shadowed by editorial content.
>
> Arbitrary administrator-authored dynamic, parameterised or catch-all routes are not introduced initially. A future requirement for governed parameterised content routing requires separate pressure testing.
>
> Locale switching and alternate-language relationships resolve through the same conceptual `ContentItem` and currently eligible locale Publications; they do not blindly transform URL strings or silently substitute a missing language.
>
> Canonical URL and alternate-language metadata derive from authoritative address/Publication truth. Locale-specific editorial metadata remains governed locale-version content according to its own semantics.
>
> Sitemap/search-index/cache/generated-route state is derived and rebuildable. None becomes Publication, address or access authority.
>
> Process-local/ETS routing state is acceleration only and cannot be required for correctness or reconstruction after restart.
>
> Beacon's stable Page path uniqueness, URL generation, Phoenix mounting and published-page sitemap concepts are useful reference patterns. Beacon's mutable `Page.path`, broad catch-all CMS authority, arbitrary dynamic editorial paths and ETS `RouterServer` correctness model are rejected for direct NewYou authority.
>
> Exact route-prefix syntax, slug-generation algorithm, Unicode/case/trailing-slash normalisation, redirect HTTP status, Ash Resource name, fields, indexes/constraints, lookup implementation, cache design and sitemap implementation remain JIT detail.

### 6.126 Fixed consequences of GRILL-39

1. Published public address history is durable Content & Media truth; pre-publication slug wording alone is not.
2. Exact eligible Publication remains the delivery target; an address is not Publication authority.
3. A stable canonical address can point to a newer exact eligible locale Publication without changing the external address.
4. A changed published address preserves governed historical redirect semantics for the same conceptual content/locale.
5. Previously exposed addresses are not silently reassigned to unrelated content while their redirect obligation remains.
6. Historical aliases cannot bypass Withdrawal/access/current-eligibility checks.
7. Route-claim uniqueness is a correctness invariant at activation/scheduled activation.
8. C&M route claims are confined to explicitly permitted public-content routing space.
9. Arbitrary editor-authored parameterised/catch-all routes remain rejected initially.
10. Locale alternates resolve from conceptual-content + eligible-locale-Publication truth, not string rewriting.
11. Canonical/alternate metadata derives from route-claim/Publication truth; locale editorial metadata remains versioned content.
12. Sitemap, search-index, generated routes, ETS and caches remain derived/rebuildable.
13. Phoenix/application routing remains the code-defined application boundary; it does not become C&M business truth.
14. Exact Resource/schema/index/normalisation/status/cache/sitemap mechanics remain JIT.
15. Beacon remains a donor/reference only; no Beacon runtime authority/dependency is introduced.

### 6.127 Block 5A continuation boundary — historical post-GRILL-39 state

**Historical post-GRILL-39 state:** Block 5A was OPEN with Block 5A.1 accepted. This did not reopen Block 3A or Block 4A. `GRILL-40` and `GRILL-41` subsequently refined and closed Block 5A.

At that point, the next tightly related pressure test was limited to **public discovery projections**: canonical/alternate metadata, sitemap participation, robots/noindex/indexability and the distinction between public deliverability and search-engine discoverability. That test subsequently concluded that current Product/FES + GRILL-28/29/39/40 already derived the required semantic boundary, and GRILL-41 closed the branch without creating another discovery-state Resource.

Generic search ranking/configuration remains under OQ-015; edge/cache design remains under OQ-014. Neither is pulled forward merely because route claims now exist.

Exact implementation remains unauthorised until the relevant C&M JIT / Feature Pack entry gates are satisfied.

### 6.128 Block 5A.2 corrected route-activation pressure test — transaction coherence, exact target, normalised identity and reversion

Independent review of GRILL-39 found no contradiction in its authority direction, but identified four semantics that were too implicit to leave solely to JIT implementation:

1. route-claim mutation and exact Publication activation require one coherent authoritative transition;
2. the public address must resolve to the exact Publication / exact locale-version target rather than merely to a stable ContentItem;
3. uniqueness is a semantic invariant over one normalised effective route identity even though the exact normalisation algorithm remains JIT; and
4. future scheduling must not accidentally become advance address reservation.

A fifth edge case — canonical slug reversion — is needed to prove that historical address lineage cannot create redirect loops.

#### Crash-consistency pressure

The following states are semantically invalid:

```text
BAD A
Publication becomes current
→ process/database failure
→ required canonical route claim never commits

BAD B
canonical route claim commits
→ Publication activation fails
→ orphaned route claim blocks later valid activation
```

For an activation that creates or changes public-address truth, the authoritative PostgreSQL boundary must therefore commit coherently:

```text
exact Publication activation
+
canonical effective route claim
+
required superseded-address redirect/history relation
=
one authoritative transition
```

This requirement says nothing yet about whether the eventual Ash design uses one Resource, multiple Resources, one action or a transaction wrapper. It fixes the semantic commit boundary only.

Router/ETS/cache invalidation, sitemap/search projection work and external crawler effects remain outside that transaction. Their failure must be retryable/reconcilable without changing the committed Publication/address truth.

#### Exact-target pressure

A public route is not satisfied by resolving only to stable conceptual content identity. Delivery must remain exact:

```text
normalised public address
→ exact effective Publication
→ exact ContentTranslationVersion
→ exact parent ContentVersion
```

The stable `ContentItem` + locale relationship explains lineage and alternate-language membership; it does not replace the exact served target.

#### Effective-route normalisation pressure

Two syntactically equivalent public addresses must not become distinct competing claims merely because raw input strings differ.

The invariant is therefore:

```text
raw authoring path/slug
→ JIT-defined canonical normalisation
→ one effective route identity
→ uniqueness / claim arbitration
```

The exact Unicode normalisation, case policy, percent-encoding treatment, trailing-slash rule and canonical-string algorithm remain JIT. Deferring those mechanics does not defer the single-effective-identity correctness invariant.

#### Scheduling pressure

Creating or approving a scheduled Publication may preflight whether an address appears available, but does not reserve or own it by default:

```text
schedule creation
→ optional availability preflight
→ NO durable address reservation

scheduled execution
→ revalidate current Publication eligibility
→ revalidate/claim normalised effective address atomically
→ activate or fail closed
```

Advance reservation would be a new product/operating capability and must not appear accidentally through scheduling implementation.

#### Historical slug-reversion pressure

A same-content/locale address may legitimately be desired again after an intervening canonical address:

```text
/a canonical
→ /b canonical, /a historical
→ later /a canonical again
```

The accepted semantics must not yield:

```text
/a → /b → /a
```

or any equivalent redirect cycle/chain. Reversion, if permitted by the current Publication transition, rewrites the active canonical/history relation so retained historical addresses converge directly or equivalently to the current eligible canonical Publication.

This does not decide whether historical addresses may ever be reused by unrelated content. While a historical redirect obligation exists they remain unavailable to unrelated content under GRILL-39. Whether that obligation can expire, and the legal/SEO/retention rules for any later unrelated reuse, remain downstream governed policy/JIT work.

### 6.129 ACCEPTED GRILL DECISION

#### `GRILL-40 — Public Route Activation Is Atomic with Exact Publication; Effective Route Identity Is Normalised, Scheduling Does Not Reserve Addresses, and Historical Slug Reversion Must Preserve Loop-Free Address History`

**Status:** ACCEPTED by the human project owner on 2026-09-21.

> A governed public route claim resolves to one exact effective Publication, and therefore transitively to one exact `ContentTranslationVersion` and its exact parent `ContentVersion`. Stable `ContentItem` and locale identity explain lineage but are insufficient as the served route target.
>
> Establishing or changing the canonical public address is part of Publication activation semantics. For an activation that introduces or changes public address truth, the authoritative PostgreSQL transition must coherently establish exact Publication activation, the canonical effective route claim and any required superseded-address redirect/history relation as one authoritative transition.
>
> The system must not permit a committed current Publication whose required route claim was not committed, nor an orphaned route claim created by a failed Publication activation.
>
> Cache invalidation, ETS/router refresh, sitemap regeneration, search projection updates and other external/derived consequences occur after the authoritative commit and may be retried/reconciled independently. Their failure does not roll back or redefine authoritative Publication/address truth.
>
> Route uniqueness applies to the normalised effective public-route identity, not merely raw submitted slug/path text. Two syntactically equivalent addresses must not become competing claims. Exact Unicode normalisation, case policy, percent-encoding policy, trailing-slash policy and canonical string-generation algorithm remain JIT implementation detail, but they must implement this single-identity invariant.
>
> Creating or approving a future Publication schedule may preflight route availability but does not reserve the address unless later Product Law explicitly introduces an advance-reservation capability. Scheduled execution must revalidate and atomically acquire/update the effective route claim when Publication activates.
>
> A historical address previously used by the same conceptual content and locale may later become canonical again only through a governed Publication transition that preserves coherent, loop-free address history. Reversion must not create redirect cycles or avoidable historical chains; retained historical aliases converge directly or equivalently to the current eligible canonical Publication.
>
> Previously exposed addresses are not silently reassigned to unrelated content while their historical-address obligation remains active. Whether that obligation can ever expire, and under what retention/SEO/legal policy an unrelated item could later reuse the address, remains a downstream governed policy/JIT question.
>
> Withdrawal, access restriction, deletion/disposition or other current Publication ineligibility continues to outrank all canonical and historical-route mappings. Historical address state cannot resurrect or bypass an ineligible Publication.
>
> GRILL-39 otherwise remains accepted: Content & Media owns durable claims inside its permitted public-content namespace; Phoenix owns application routing mechanisms/namespaces; runtime route tables, caches, sitemaps and search indexes remain rebuildable projections.

### 6.130 GRILL-40 refinement map and fixed consequences

GRILL-40 does **not** replace GRILL-39. It refines only semantics that GRILL-39 left too implicit for safe JIT handoff.

1. GRILL-39's “activation claims the effective address” is refined to require one coherent authoritative PostgreSQL transition for exact Publication activation + canonical claim + required redirect/history relation.
2. GRILL-39's “exact eligible Publication remains the target” is made explicit as address → exact Publication → exact ContentTranslationVersion → exact ContentVersion.
3. GRILL-39's route uniqueness is refined to uniqueness of a single **normalised effective route identity**; the normalisation algorithm remains JIT.
4. Scheduled Publication may preflight but does not reserve the address absent later explicit authority; execution performs the current atomic claim/revalidation.
5. Same-content/locale historical slug reversion is permitted only through a governed Publication transition that leaves loop-free, convergent route history.
6. Historical-address reuse by unrelated content remains prohibited while the redirect obligation exists; expiry/reuse policy remains downstream rather than guessed here.
7. Runtime/router/cache/sitemap/search consequences remain post-commit, derived, retryable and reconcilable.
8. No `ContentRoute`, `RouteClaim`, reservation Resource, redirect worker, cache or search Resource is created merely by this refinement; exact Ash topology remains JIT.
9. All GRILL-39 namespace, eligibility, alternate-language, non-authoritative-projection and Beacon-rejection conclusions remain accepted.

### 6.131 Block 5A corrected closure audit — PASS / historical pre-GRILL-41 state

The Block 5A branch was re-audited after GRILL-40 rather than closing on the earlier under-specified route model.

| Closure question | Result after GRILL-39 + GRILL-40 |
|---|---|
| Does first public exposure create durable address/history truth? | **YES** — GRILL-39. |
| Is the canonical served target exact rather than “latest content”? | **YES** — exact Publication → exact locale/content versions; GRILL-40. |
| Can Publication and address truth diverge under crash/failure? | **NO by contract** — coherent authoritative transition required; GRILL-40. |
| Can equivalent raw paths become competing public claims? | **NO by contract** — uniqueness is over one normalised effective route identity; exact algorithm JIT. |
| Does schedule creation reserve a public address? | **NO initially** — optional preflight only; execution reclaims/revalidates atomically. |
| Can slug reversion create redirect cycles? | **NO by contract** — retained history must converge to current canonical target. |
| Can an historical alias bypass Withdrawal/access/ineligibility? | **NO** — current Publication/access eligibility outranks aliases; GRILL-39/40. |
| Can editorial content shadow application/system routes? | **NO** — code/application namespace remains authoritative; GRILL-39. |
| Are canonical/alternate-language relationships independent authority? | **NO** — derived from current route claim + exact eligible sibling Publications. |
| Is public deliverability equivalent to search-engine indexability? | **NO** — C&M owns discovery metadata, but indexability is a separate eligibility/projection concern. |
| Do sitemap, robots/noindex, native-search indexes or external crawler state create Publication/access truth? | **NO** — derived projection only. |
| Is a new SEO/indexability/sitemap business Resource required now? | **NO evidence** — current Product/Domain/FES semantics are sufficient; exact shape remains JIT. |
| Are OQ-014 edge/cache or OQ-015 native-search configuration resolved? | **NO** — correctly remain downstream gates. |

The discovery-projection pressure test therefore does **not** justify an additional discovery-state lifecycle or business Resource. Current law plus GRILL-28/29/39/40 is sufficient to state the semantic boundary:

```text
exact eligible Publication
+
current C&M public/private discovery metadata
+
current access/publication eligibility
→ current public-delivery / discovery eligibility

canonical + alternate tags
sitemap rows
robots/noindex rendering
native-search projection
external search-engine observation
→ derived outputs only
```

A page being deliverable does not imply it must be indexable. A `noindex` or robots directive does not secure content. Sitemap omission does not withdraw Publication. Search-engine cache/crawl lag cannot preserve authority after current C&M truth makes a Publication ineligible.

No semantic blocker remains inside the bounded public-addressability/discovery-projection branch. Formal branch closure is not auto-recorded here because closure is itself a human-accepted working decision. A separate closure decision should be proposed next.

### 6.132 Block 5A next action

> Historical sequencing note: this subsection records the state immediately before GRILL-41 acceptance. Current Block 5A status is stated in Section 6.135 and the active conclusion.

**Historical pre-GRILL-41 state:** Block 5A remained **OPEN pending one explicit closure decision**. `GRILL-41` subsequently closed Block 5A. No additional mechanism-level addressability/SEO GRILL is justified merely for dossier completeness.

The next decision should only certify the already-pressure-tested branch as semantically closed for Content & Media JIT handoff. It must preserve OQ-014/OQ-015, exact SEO/schema/sitemap/robots/cache implementation, historical-address expiry/reuse policy and normal Feature Pack/JIT/development-entry gates as downstream work.

Exact implementation remains unauthorised.

### 6.133 Block 5A.3 final adversarial closure audit — PASS

After GRILL-40, Block 5A was deliberately pressure-tested one more time against the live NewYou authority rather than being closed from momentum.

The live canonical repository remained at `be6b9ea4bdfc5a638a24affa20e6c75cd9fc321f` during this audit. The current Product, Architecture, Domain and Frontend authority remained consistent with the GRILL-39/40 model.

The final escape-hatch checks were:

1. **Scheduled publication / OQ-016:** OQ-016 remains unresolved and correctly owns scheduler reliability, retry policy, alert ownership, stale-approval checks and recovery. GRILL-40 fixes only the business-correctness boundary: schedule creation does not reserve a route; scheduled execution revalidates current eligibility and atomically claims/updates the effective route as Publication activates.
2. **Correction and Withdrawal:** historical aliases cannot create a second delivery authority. Current Publication/access eligibility outranks every canonical or historical mapping.
3. **Deletion and recovery:** search/read/sitemap/cache projections must rebuild through current privacy/deletion and Publication rules. Projection lag cannot resurrect authority.
4. **Indexability:** public delivery, protected access and ordinary search-engine indexability remain separate concerns. `robots.txt`, `noindex` or sitemap omission cannot secure or withdraw content.
5. **Canonical and bilingual alternates:** canonical and alternate-language outputs derive from the current route claim plus exact eligible sibling locale Publications; no independent canonical/hreflang business lifecycle is justified.
6. **Routing namespace:** Phoenix/application code retains the permitted route namespace/mechanism. C&M claims only bounded editorial public-content addresses inside that namespace.
7. **Historical-address reuse:** while a historical-address obligation remains, unrelated content cannot silently take the address. Whether such an obligation may expire is a later governed policy decision, not a missing ownership model.
8. **Native search and edge caching:** OQ-015 and OQ-014 remain unresolved implementation/architecture gates. Their existence does not create search/cache authority over Publication or address truth.

The audit therefore finds **no hidden durable address/discovery lifecycle** requiring another Domain, Resource or pre-JIT mechanism decision.

### 6.134 ACCEPTED GRILL DECISION

#### `GRILL-41 — The Public Addressability / Canonical / Redirect / Indexability / Discovery-Projection Branch Is Semantically Closed for Content & Media JIT Handoff`

**Status:** ACCEPTED by the human project owner on 2026-09-21.

> Block 5A is **CLOSED / PASS FOR CONTENT & MEDIA JIT HANDOFF** at semantic reuse-discovery level.
>
> GRILL-39 and GRILL-40 together form the controlling public-address model. Publicly exposed locale addresses are durable Content & Media truth; address changes preserve governed historical route semantics; and any activation that creates or changes address truth coherently commits the exact Publication, canonical effective route claim and required historical redirect relationship.
>
> A public route resolves to an exact effective Publication and therefore to its exact `ContentTranslationVersion` and exact parent `ContentVersion`. Stable conceptual content identity explains lineage but does not replace the exact served target.
>
> Route uniqueness applies to one normalised effective route identity. Exact Unicode, case, encoding, trailing-slash and canonical-string mechanics remain JIT.
>
> Schedule creation may preflight route availability but does not reserve an address unless a later explicit authority creates such a capability. Scheduled execution revalidates and claims the address atomically.
>
> Historical slug reversion must preserve loop-free, convergent address history. Previously exposed addresses are not silently reassigned to unrelated content while their historical-address obligation remains. Any expiry/reuse policy remains downstream.
>
> Phoenix/application code owns the permitted routing namespace and mechanism. Content & Media owns durable public-content route claims only inside that allowed namespace. Editorial content cannot shadow application/system routes.
>
> Public deliverability, access eligibility and ordinary search-engine indexability are distinct. Being published or deliverable does not imply indexability, and robots/noindex behaviour does not provide access control.
>
> Canonical and alternate-language metadata derive from current authoritative route-claim and exact eligible Publication truth. Alternate-language relationships require actual eligible sibling locale Publications of the same conceptual content; they are not URL-string substitutions.
>
> Sitemap participation, robots/noindex rendering, structured-data output, native-search indexes, external crawler/search-engine state, generated route modules, ETS and caches are **derived/rebuildable projections**. None establishes Publication, access, canonical-address or Withdrawal truth.
>
> Historical aliases and stale search/sitemap/cache/crawler state cannot bypass current Withdrawal, restriction or other Publication ineligibility. External propagation delay is operational lag, not retained business authority.
>
> Current evidence does not justify a separate SEO Domain, Indexability business lifecycle, sitemap business Resource, generic route Domain or search-engine authority.
>
> Beacon's unique-path, public-URL helper, Phoenix-mount and published-page sitemap concepts remain useful donor/reference ideas only. Beacon's mutable `Page.path`, broad dynamic CMS routing and ETS correctness model remain rejected as NewYou authority.
>
> OQ-014 edge/cache design, OQ-015 native-search configuration and OQ-016 content-publication operations remain unresolved at their proper downstream authority. GRILL-39/40 constrain those implementations only by requiring them to preserve exact Publication/address authority, current eligibility and rebuildable projection semantics.
>
> Exact route Resource topology, normalisation algorithm, redirect HTTP mechanics, historical-address expiry/reuse policy, scheduling/retry mechanisms, canonical/hreflang/schema rendering, sitemap/robots implementation, indexes, caches and workers remain JIT/proof detail.
>
> This closure does not itself adjudicate FP-001's currently conditional Content & Media JIT dossier disposition. The reuse evidence may inform that later governed reconciliation but cannot change it.
>
> Reopen Block 5A only for a higher-authority contradiction, materially changed scope or new evidence exposing a genuine semantic inconsistency — not for ordinary implementation choices.
>
> Block 5A closure authorises no executable development.

### 6.135 Fixed consequences of GRILL-41 / Block 5A closure

1. Block 5A is formally **CLOSED / PASS FOR C&M JIT HANDOFF** at semantic reuse-discovery level.
2. GRILL-39 remains the ownership/address-history decision; GRILL-40 remains its atomicity/exactness/normalisation/scheduling/reversion refinement; GRILL-41 closes the bounded branch rather than replacing either decision.
3. No additional SEO, indexability, sitemap, generic-route or search-engine business authority is introduced.
4. `OQ-014`, `OQ-015` and `OQ-016` remain unresolved at their proper downstream authority.
5. Historical-address expiry/reuse policy remains deliberately unresolved; closure does not invent a retention duration or unrelated-content reuse rule.
6. Exact Ash Resource topology, constraints, normalisation algorithm, redirect status/mechanics, scheduler/retry implementation, sitemap/robots/canonical/hreflang/schema rendering, search indexes, caches and workers remain JIT/proof detail.
7. FP-001's conditional Content & Media dossier disposition is not changed by this working artifact.
8. Block 5A may be reopened only by higher-authority contradiction, materially changed scope or genuinely new semantic evidence.
9. No executable implementation is authorised.

---

## 7. High-value extraction candidate B — publication boundary and immutable versions

### 7.1 Exact Beacon source

Stable `v0.5.1`:

- `lib/beacon/content/page_event.ex`
  - blob SHA `175b195baa90c2dd4adee5e1c6253c0654a3cdeb`
- `lib/beacon/content/page_snapshot.ex`
  - blob SHA `92f20dd8941383339c12682b3470bcf3fbe032f4`
- related page model: `lib/beacon/content/page.ex`
  - blob SHA `ba1998848bce2bdfe906ca99e9c49ad1c6896fb7`

### 7.2 Useful Beacon idea

Beacon separates mutable page editing from published representation by creating publication events and snapshots.

The reusable lesson is:

> editable working state is not the same thing as delivered/published state.

### 7.3 Why direct reuse is wrong

Beacon's stable snapshot stores a serialised representation of the page struct. NewYou already requires immutable, versioned business truth with independent locale lineages and exact provenance.

NewYou's content lifecycle is materially richer than Beacon's simple `created / published / unpublished` event model.

NewYou must preserve states and distinctions including:

```text
missing
→ draft
→ machine_draft
→ language_review
→ clinical_review_required where applicable
→ approved
→ published
→ superseded / withdrawn
```

Each locale advances independently under governed risk rules.

### 7.4 Proposed NewYou adaptation

Use Beacon's separation principle, but implement first-class NewYou mutable-authoring, immutable-version and independent governance truth:

```text
ContentItem
   │
   ├── ContentDraft
   │      mutable working truth
   │      safe autosave / exact draft revision
   │      Template binding/membership where applicable
   │
   │      ↓ first exact-content governance boundary
   │        normally formal review submission
   │
   └── ContentVersion
          immutable governed snapshot
          exact provenance
          exact formal-review subject
             │
             ├── Approval evidence
             ├── Publication / schedule
             └── Correction / withdrawal consequences
```

Approval or publication does not mint another Content Version when the content is unchanged.

Later material edits return through `ContentDraft` and require a successor immutable version before those changed semantics can become reviewed/approved/published truth.

`GRILL-22` now refines locale/translation lineage:

```text
ContentVersion
→ shared immutable occurrence structure + locale-invariant values

ContentTranslationVersion
→ exact localisable values for one locale against that ContentVersion
```

Publication/rendering therefore resolves an exact immutable pair rather than “latest translation”:

```text
exact ContentVersion
+
exact approved/published ContentTranslationVersion belonging to it
```

Publication:

```text
→ references one exact approved immutable shared-version / locale-version pair
→ carries separate publication provenance/state/time
→ never dereferences or mutates the current draft
→ never silently follows a successor shared or locale version
```

### 7.5 Baseline decision

**ADAPT CONCEPT; REIMPLEMENT DATA MODEL.**

---

## 8. High-value extraction candidate C — media lineage and storage boundary

### 8.1 Exact Beacon source

Stable `v0.5.1`:

- `lib/beacon/media_library/asset.ex`
  - blob SHA `d0a21ad2205a35fa17e414f3c7a66e36a86e8e11`
- `lib/beacon/media_library/provider.ex`
  - blob SHA `a02338b753f3739f11e0b10723b900cb4c270a23`
- `lib/beacon/media_library/provider/s3.ex`
  - blob SHA `844bb47a9d0ea3f09544c52caa0018580d5eae8e`
- `lib/beacon/media_library/processors/image.ex`
  - blob SHA `61100a356e368fab67f8aec0989ac090149a398c`
- `lib/beacon/media_library/upload_metadata.ex`
  - blob SHA `268c506e651268c8e8462527c32c6abb3cebdc71`
- `lib/beacon/media_library/asset_field.ex`
  - blob SHA `4169b803cc0d15a65b7932656e91c0d5923c2238`

### 8.2 Useful Beacon ideas

Beacon cleanly demonstrates:

- media identity in application/database state;
- source → derivative relationships;
- named derivative usage such as thumbnails;
- a processing pipeline separated from storage providers;
- replaceable providers;
- upload metadata travelling through validation/processing/storage;
- custom optional asset metadata.

These map well to NewYou's requirement that Content & Media own governed media identity, rights, derivatives and publication state while object storage owns durable bytes.

### 8.3 Problems that prevent direct reuse

The stable Beacon S3 provider has incomplete deletion semantics: `soft_delete/1` does not remove the object from S3.

The stable image processor also hard-codes behaviour and contains evidence of unfinished semantics. For example, the `variant_480w!` path computes toward 400px rather than 480px.

NewYou additionally requires:

- rights / attribution;
- provenance/source;
- replacement/version lineage;
- usage references;
- deletion and withdrawal propagation;
- protected delivery where applicable;
- privacy/restore reconciliation;
- durable async processing where appropriate.

### 8.4 NewYou adaptation — resolved by GRILL-31

`GRILL-31` accepts the seam:

```text
PostgreSQL/Ash MediaAsset authority
        ↓
provider-independent storage capability
        ↓
external S3-compatible object storage
        ↓
current deployment direction: Wasabi or equivalent

master/source MediaAsset
        ↓
durable derivative processing
        ↓
derivative MediaAsset retains exact source lineage
```

The project-owner explicitly reiterated at GRILL-31 acceptance that media bytes are intended to be offloaded to external S3-compatible storage such as Wasabi to reduce application-server disk/load. The exact vendor remains replaceable and never becomes media business authority.

Beacon's S3 lifecycle implementation is not the authoritative deletion design.

### 8.5 Baseline decision — refined by GRILL-32, GRILL-36 and GRILL-37

- Stable conceptual Asset identity: **ADAPT — HIGH VALUE**
- Exact immutable MediaAssetVersion truth: **NEWYOU-OWNED; NO DIRECT BEACON DONOR**
- Exact source-version derivative lineage: **ADAPT CONCEPTUALLY / NEWYOU-OWNED VERSION SEMANTICS**
- Provider abstraction: **ADAPT — HIGH VALUE**
- Processing-context / validation-hook separation: **ADAPT CONCEPTUALLY**
- Stable upload orchestration ordering: **REJECT / REIMPLEMENT**
- Stable S3 provider source: **REIMPLEMENT**
- Stable synchronous image processor source: **REIMPLEMENT**
- Durable async ingest/derivative orchestration: **NEWYOU-OWNED**
- External-write reconciliation/idempotency: **NEWYOU-OWNED**
- Asset custom-field extension idea: **ADAPT CAREFULLY; NOT FOR GOVERNED VERSION/LOCALE/ACCESSIBILITY TRUTH**

`GRILL-32` fixes that accepted ingest intent precedes permanent provider writes, that object-store writes occur outside database transactions, and that verified storage finalisation/reconciliation—not worker/provider success—establishes storage readiness.

`GRILL-36` fixes that the target of those ingest/storage facts is the exact immutable `MediaAssetVersion`; governed consumers, Publication and derivative provenance are version-exact while `MediaAsset` remains stable conceptual identity.

`GRILL-37` fixes the remaining deletion/share seam: version-scoped disposition permanently suppresses the exact version without destroying bytes still lawfully required by another same-asset version; whole-asset terminal disposition prevents stable-identity resurrection; byte-destruction policy expands to every dependent version.

---

## 9. Selective extraction candidate D — LiveAdmin table/editor primitives

### 9.1 Exact stable source

Beacon LiveAdmin `v0.4.3`:

- `lib/beacon/live_admin/page_builder/table.ex`
  - blob SHA `449080450ac4ac8e0b36493b31df091d401f33bc`
- `lib/beacon/live_admin/components/admin_components.ex`
  - blob SHA `80cb75e0d4263e4d2c960800dd8ac6a2bf86e785`
- `lib/beacon/live_admin/page_builder.ex`
  - blob SHA `e205b92ff9f88a4996b42b6a6c69d8466473aaec`

### 9.2 Potentially reusable small mechanics

`PageBuilder.Table` is intentionally small and encapsulates:

- page size;
- current page;
- page count;
- sort selection;
- query string;
- URL/query-param construction;
- previous/next/goto navigation;
- pagination navigation-window calculation.

`AdminComponents` contains ordinary Phoenix component patterns for:

- tables;
- table search;
- sort controls;
- pagination;
- thumbnails;
- forms;
- flash/error presentation;
- content-resource sub-navigation.

### 9.3 Why LiveAdmin itself should not be adopted

NewYou already has an operator interaction doctrine and Content operations model. Installing LiveAdmin as a second admin application risks:

- a competing navigation/interaction authority;
- Ecto/Beacon write paths alongside Ash business actions;
- a second styling/design-system surface;
- LiveSvelte/editor dependencies without proven need;
- content operators acting through a CMS-specific shell instead of NewYou's governed Work model.

### 9.4 Proposed NewYou use

Review small, generic algorithms/components individually. Where copying source produces a clear benefit over Phoenix-generated/core components or a tiny clean-room rewrite, preserve MIT attribution.

Do not import the whole LiveAdmin package merely to obtain pagination or table components.

### 9.5 Baseline decision

**SELECTIVE REUSE CANDIDATE**, file-by-file only.

---

## 10. Candidate E — custom page/asset field extension points

Beacon provides `PageField` and `AssetField` behaviours allowing extension fields to define a name, type, default, form rendering and validation behaviour.

This is a useful extensibility concept, but NewYou must distinguish:

```text
material lifecycle/policy/invariant field
→ first-class governed domain concept

optional editorial presentation metadata
→ extensible metadata may be acceptable
```

NewYou must not bury rights, provenance, safety classification, publication authority or other business-significant fields inside generic `extra` maps merely because Beacon does so.

**Baseline classification:** ADAPT CAREFULLY.

---

## 11. Candidate F — Beacon lifecycle hooks

Beacon's lifecycle system exists specifically to let users inject/override steps inside page/template/media processing.

That flexibility is useful for a general-purpose CMS, but NewYou should be sceptical of an open-ended callback system around authoritative content transitions.

NewYou already has stronger architectural mechanisms:

- authoritative Ash actions;
- explicit cross-domain commands;
- durable consequences;
- Oban where work may be delayed/retried;
- PubSub for observation/freshness only;
- Audit & Evidence for appropriate evidence.

The likely reusable lesson is not "copy Lifecycle" but:

> identify extension seams explicitly and keep them narrow, typed and owned.

**Baseline classification:** REIMPLEMENT NARROWLY / REJECT OPEN-ENDED AUTHORITY HOOKS.

---

## 12. Explicit rejection register — v0.1.0

The following Beacon patterns should be presumed rejected unless later evidence overturns the presumption:

### 12.1 Beacon as the authoritative NewYou CMS dependency

Reason: creates Ecto/Beacon authority beside Ash Content & Media authority and imports pre-1.0 coupling.

### 12.2 Beacon fork as NewYou's CMS

Reason: turns NewYou into maintainer of a divergent CMS framework and makes upstream evolution expensive to consume.

### 12.3 Stored executable HEEx/Elixir helpers as normal editorial content

Reason: creates a shadow code-deployment mechanism in the content database.

### 12.4 Stored arbitrary JavaScript hooks as editorial capability

Reason: violates the governed component catalogue and expands security/review surface.

### 12.5 Stored arbitrary stylesheets as editorial capability

Reason: bypasses NewYou design tokens and design-system authority.

### 12.6 Beacon PageVariant as NewYou experimentation authority

Reason: NewYou already has a dedicated Experimentation Domain with deterministic sticky assignment, exposure evidence and governed decision semantics.

### 12.7 Per-site GenServer as publication correctness authority

Reason: NewYou requires horizontally correct authority and Content & Media explicitly has `GenServer: NONE initially`.

### 12.8 ETS/runtime loader state as publication truth

Reason: authority ≠ acceleration. Empty-cache correctness is mandatory.

### 12.9 Beacon multisite abstraction as NewYou product-space model

Reason: NewYou product spaces are governed logical experience/activation boundaries, not generic CMS tenants.

### 12.10 Beacon LiveAdmin as a second operator application

Reason: risks competing admin/business-write paths and duplicates NewYou's Command Centre / Work / design-system contracts.

---

## 13. Proposed NewYou seams influenced by Beacon

These are planning seams only, not final Resources/modules.

### 13.1 Governed composition contract

Accepted `GRILL-01` through `GRILL-06` now establish the baseline composition contract:

```text
code-authoritative/versioned block contract
        ↑
stable block_type + representation/schema_version
        ↑
minimal subordinate block occurrence
        ↑
ordered structured/embedded version-owned composition
        ↑
Content Version authority
```

`GRILL-03` resolved the persistence baseline: ordinary block occurrences are owned as structured/embedded values by the containing draft/Content Version rather than as independently persisted child block Resources by default.

`GRILL-04` fixes the minimal occurrence envelope as:

```text
occurrence_key
block_type
schema_version
typed payload
```

`GRILL-05` requires explicit compatible schema evolution, and `GRILL-06` keeps bounded block slots subordinate to code-defined block contracts rather than promoting them into independent content entities.

Still deferred are the exact Ash DSL/type implementation (`Ash.Type.Union`, embedded Resource, typed struct/NewType or another bounded Ash-native representation), draft mutation/concurrency mechanics and later indexing needs. Those implementation choices may refine mechanism but may not reopen the accepted ownership/persistence semantics without new evidence.

### 13.2 Publication/version contract

```text
ContentItem
    ↓
immutable ContentVersion
shared structure + locale-invariant governed values
    │
    ├── immutable EN ContentTranslationVersion lineage
    └── immutable AF ContentTranslationVersion lineage

exact ContentVersion
+
exact currently eligible approved ContentTranslationVersion belonging to it
        ↓
publish authoritative transition
        ↓
durable locale-specific Publication truth
        ↓
effective supersession / downstream durable consequences
```

`GRILL-22` establishes one shared structural authority rather than independent locale block trees. `GRILL-21` establishes that approval/publication operate around exact immutable version truth rather than minting duplicate Content Versions when content is unchanged. `GRILL-23` distinguishes immutable historical locale provenance from derived current translation alignment. `GRILL-28` establishes that Publication activates the exact currently eligible locale version, while scheduling pins exact intent and revalidates before activation.

### 13.3 Media contract

```text
stable MediaAsset identity
        ↓
immutable MediaAssetVersion
→ exact bytes/checksum/storage provenance
→ exact governed locale/accessibility metadata
→ exact rights/risk/provenance evidence
        ↓
exact source-version derivative lineage
        ↓
exact-version Publication
        ↓
current-authority bounded delivery

Withdrawal
→ immediate delivery/reference/finalisation suppression

version-scoped disposition
→ exact MediaAssetVersion terminality
→ shared bytes may remain only for another lawfully retained version

whole-asset terminal disposition
→ stable MediaAsset identity never resurrects
```

Reverse media usage remains a derived/rebuildable projection over owner-authoritative exact forward `MediaAssetVersion` references. Destructive disposition must reconcile authoritative dependencies and shared-byte consumers rather than trusting an empty reverse index or provider object identity.

### 13.4 Operator contract

```text
Library
+
Work Queue
+
Editorial Calendar
+
exact target preview
```

Beacon/LiveAdmin may inform generic UI mechanics, but NewYou owns the operating model.

---

## 14. Direct source-copy policy — proposed, not yet approved

Where a Beacon/LiveAdmin source fragment is directly copied or substantially derived, NewYou should preserve an internal provenance record containing at least:

- upstream repository;
- upstream stable tag or exact commit;
- exact source path;
- blob SHA;
- licence;
- copyright notice where required;
- NewYou destination path once known;
- summary of modifications;
- reason for copy instead of clean reimplementation;
- test/proof covering the adapted semantics.

The Beacon MIT notice must be retained in all copies or substantial portions as required by the licence.

No copy should be accepted merely because the code is small. A tiny clean implementation may have lower lifetime cost than carrying upstream provenance and assumptions.

---

## 14A. Exposed dependencies / downstream architecture questions

Accepted GRILL decisions may expose requirements that belong to another authority or later JIT dossier. Recording them here prevents silent loss without authorising this Beacon reuse dossier to solve them prematurely.

### EXPOSED-01 — Governed content-type contract evolution

**Exposed by:** `GRILL-14`.  
**Status:** SEMANTIC ARCHITECTURE BOUNDARY RESOLVED BY `GRILL-27`; AUTHORITATIVE JIT ADOPTION / EXACT IMPLEMENTATION STILL REQUIRED.

`GRILL-27` resolves the compatibility model:

```text
Content Type
→ code-authoritative stable type key
→ explicit immutable contract revisions
→ exact revision provenance on Template Versions, ContentDrafts and ContentVersions
→ explicit directional code-defined compatibility for current selectability
```

Historical Template Approval remains true against the exact Content Type contract revision used for approval.

Current Template selectability separately evaluates that historical revision against the current revision.

Different revisions fail closed unless explicit code-defined compatibility permits continued new authoring.

No mutable runtime `ContentType` / `ContentTypeVersion` authority or administrator-authored compatibility DSL is introduced initially.

Exact catalogue module/API design, contract representation, compatibility functions and migration actions remain C&M JIT work. This working dossier still does not itself amend authoritative Domain/Architecture law or authorise implementation.

### EXPOSED-02 — Validation ownership matrix

**Exposed by:** accumulated `GRILL-01` through `GRILL-15`, sharpened by owner review before Block 2A.6.  
**Status:** ARCHITECTURE-LEVEL BASELINE RESOLVED BY `GRILL-15`; JIT FORMALISATION STILL REQUIRED.  

Several layers will legitimately validate different truths:

```text
Content Type
Template Version
Block contract
Block slot contract
Pattern expansion
Draft / Content Version
Publication gate
```

Before implementation design, later work must state the authoritative owner of each invariant so the same business rule is not independently redefined across several layers.

The intended directional baseline is:

```text
Content Type     → global structure/business requirements
Template Version → narrower scaffold conformance
Block schema     → local block representation
Block slot       → local nested-composition constraints
Content Version  → exact governed snapshot truth
Publication      → cross-cutting publishability revalidation/orchestration
```

Invocation/rechecking of an invariant by another layer does not transfer ownership of that invariant.

`GRILL-15` now fixes this directional ownership baseline for the Template-scaffold seam. The eventual Content & Media JIT dossier must still turn the baseline into an explicit implementation/proof matrix and verify that no validation rule has competing semantic owners.

---

## 15. Grill strategy — revised in v0.2.0

The v0.1.0 sequence was too broad. From v0.2.0 onward the dossier proceeds through **small explicit seams**. One seam is pressure-tested, decided and incorporated before the next begins.

For each seam:

1. identify the exact NewYou requirement and owning authority;
2. inspect exact stable Beacon/LiveAdmin source relevant to that seam;
3. pressure-test against Ash 3.x rather than translating Ecto patterns mechanically;
4. pressure-test authority, lifecycle, concurrency, retries/reordering/restart/failure where relevant;
5. ask whether reuse reduces lifetime complexity or merely imports Beacon assumptions;
6. classify only the mechanism under review;
7. record the accepted decision in the next MINOR SemVer revision;
8. explicitly list what remains deferred/exposed to another authority;
9. run a **whole-document consistency sweep in the same revision** before handoff.

There is no universal assumption that all Beacon material must share one reuse posture. One small helper may justify direct source reuse while an adjacent persistence mechanism may require clean reimplementation or rejection.

### Current component/composition/template sequence

```text
Block 1A    Where does a block definition live?
            → ACCEPTED as GRILL-01 in v0.2.0

Block 1B.1  Does a block occurrence own independent business identity/lifecycle?
            → ACCEPTED as GRILL-02 in v0.3.0

Block 1B.2  What persistence/value shape implements those semantics in Ash?
            → ACCEPTED as GRILL-03 in v0.4.0

Block 1B.3  What exact persisted block envelope must every occurrence carry?
            → ACCEPTED as GRILL-04 in v0.5.0

Block 1B.4  When must block schema_version change, and how is compatibility governed?
            → ACCEPTED as GRILL-05 in v0.6.0

Block 1C.1  What is a slot in NewYou, and do we need Beacon-style named slots?
            → ACCEPTED as GRILL-06 in v0.7.0

Block 1C.2  Are sections separate persisted content entities?
            → ACCEPTED as GRILL-07 in v0.8.0

Block 1C.3  Are content components separate durable entities?
            → ACCEPTED as GRILL-08 in v0.9.0

Block 1C.4  What are composed patterns and how do they instantiate?
            → ACCEPTED as GRILL-09 in v0.10.0

Block 2A.1  Pattern versus governed content-template boundary?
            → ACCEPTED as GRILL-10 in v0.11.0

Block 2A.2  Where does template definition authority live?
            → ACCEPTED as GRILL-11 in v0.12.0

Block 2A.3  Dedicated ContentTemplate/ContentTemplateVersion Resources or Content Item/Version reuse?
            → ACCEPTED as GRILL-12 in v0.13.0

Block 2A.4  Minimum ContentTemplateVersion lifecycle?
            → ACCEPTED as GRILL-13 in v0.14.0

Block 2A.5  One content type per ContentTemplate or multi-type compatibility?
            → ACCEPTED as GRILL-14 in v0.15.0

Block 2A.6  What exactly belongs inside ContentTemplateVersion?
            → ACCEPTED as GRILL-15 in v0.16.0

Block 2A.7  What exact semantics do Template structural slots and placement constraints need?
            → ACCEPTED as GRILL-16 in v0.17.0

Block 2A.8  What draft↔ContentTemplateVersion provenance and deterministic slot-membership state must persist?
            → ACCEPTED as GRILL-17 in v0.18.0

Block 2A.9  What Template migration correspondence may be automatic, and what requires explicit human resolution?
            → ACCEPTED as GRILL-18 in v0.19.0

Block 2A.10 Does the editorial Template architecture have sufficient semantic closure for exact Ash Resource/action design?
            → ACCEPTED as GRILL-19 in v0.20.0; TEMPLATE BRANCH CLOSED / PASS

Block 3A.1   What owns mutable working-draft truth, and how does mutable authoring state cross into immutable ContentVersion truth?
            → ACCEPTED as GRILL-20 in v0.21.0

Block 3A.2   What event creates a new immutable ContentVersion, and where do lifecycle states live around that snapshot?
            → ACCEPTED as GRILL-21 in v0.22.0

Block 3A.3   What relationship exists between shared ContentVersion and independently governed locale/translation versions?
            → ACCEPTED as GRILL-22 in v0.23.0

Block 3A.4   What translation lineage/staleness and safe carry-forward rules apply across source/shared-version changes?
            → ACCEPTED as GRILL-23 in v0.24.0

Block 3A.5   What durable Resource boundaries are required for mutable locale authoring, translation work and immutable translation versions?
            → ACCEPTED as GRILL-24 in v0.25.0

Block 3A.6   What lifecycle and concurrency rules govern ContentDraft and ContentLocaleDraft?
            → ACCEPTED as GRILL-25 in v0.26.0

Block 3A.7   What exact Review/Approval authority model applies across shared, locale and Template immutable subjects?
            → ACCEPTED as GRILL-26 in v0.27.0

Block 3A.8   How is the governed Content Type contract made stable/version-addressable for historical approval vs current selectability?
            → ACCEPTED as GRILL-27 in v0.28.0

Block 3A.9   What Publication/Scheduling eligibility and revalidation model consumes immutable truth and current eligibility under OQ-016?
            → ACCEPTED as GRILL-28 in v0.29.0

Block 3A.10  What Correction/Withdrawal declaration and downstream impact semantics are required?
            → ACCEPTED as GRILL-29 in v0.30.0

Block 3A.11  Is the version/translation/review/approval/publication/correction branch semantically closed for C&M JIT handoff?
            → ACCEPTED as GRILL-30 in v0.31.0; BLOCK 3A BRANCH CLOSED / PASS FOR JIT HANDOFF

Block 4A.1   What is the authoritative media identity, source/derivative lineage and storage-provider boundary?
            → ACCEPTED as GRILL-31 in v0.32.0

Block 4A.2   What durable ingest/processing lifecycle, idempotency and reconciliation model governs media storage/derivatives?
            → ACCEPTED as GRILL-32 in v0.33.0

Block 4A.3   What rights/provenance/publication/protected-delivery lifecycle applies to source assets and derivatives?
            → ACCEPTED as GRILL-33 in v0.34.0

Block 4A.4   What withdrawal/physical-deletion/derivative/non-resurrection contract governs MediaAssets?
            → ACCEPTED as GRILL-34 in v0.35.0

Block 4A.5   What usage/reference indexing, replacement propagation and dependency-discovery model governs media?
            → ACCEPTED as GRILL-35 in v0.36.0

Block 4A.6   Is the media identity/ingest/rights/delivery/deletion/reference branch semantically closed for C&M JIT handoff?
            → BLOCKED / STOP; media-version gap resolved by GRILL-36 in v0.37.0

Block 4A.7   Is the corrected MediaAsset/MediaAssetVersion branch semantically closed for C&M JIT handoff?
            → BLOCKED / STOP; deletion subject/shared-byte ambiguity resolved by GRILL-37 in v0.38.0

Block 4A.8   Is the fully corrected media branch semantically closed for C&M JIT handoff?
            → ACCEPTED as GRILL-38 in v0.39.0; BLOCK 4A BRANCH CLOSED / PASS FOR C&M JIT HANDOFF

Block 5A.1   What durable authority and lifecycle governs locale-specific public addresses, canonical URLs and redirects after publication?
            → ACCEPTED as GRILL-39 in v0.40.0; BLOCK 5A remained OPEN at that point

Block 5A.2   What transaction/exact-target/normalised-route/reversion semantics refine public route activation?
            → ACCEPTED as GRILL-40 in v0.41.0; closure audit PASS but formal closure still pending at that point

Block 5A.3   Does the fully corrected public-addressability/discovery-projection branch have semantic closure for C&M JIT handoff?
            → ACCEPTED as GRILL-41 in v0.42.0; BLOCK 5A CLOSED / PASS FOR C&M JIT HANDOFF
```

Later/deferred C&M/JIT seams from the CLOSED Block 3A branch include:
- exact Correction/Withdrawal Ash Resource/action/relationship topology after GRILL-29;
- exact bounded correction-impact/severity classification vocabulary/policy;
- exact reverse-dependency acceleration and cross-domain durable handoff/orchestration representation;
- FLOW-11 safety-critical proof and owner-specific remediation contracts;
- OQ-016 scheduler reliability/retry/approved-window/alert/recovery implementation after GRILL-28;
- exact Publication / durable schedule-intent Ash Resource/action topology;
- exact failed/refused scheduler-attempt evidence representation;
- exact Content Type catalogue API/module/contract representation and compatibility-function implementation after GRILL-27;
- explicit ContentDraft Content Type contract migration/rebase action design;
- exact Review/Approval Ash Resource/relationship/action topology after GRILL-26;
- exact Approval requirement-basis persistence and OQ-016 current-eligibility mechanics;
- exact Ash optimistic-lock fields/actions and PostgreSQL uniqueness/index strategy for GRILL-25;
- exact idempotency-key persistence/reconciliation mechanics;
- exact Ash module names, fields/actions/identities/indexes for the accepted translation Resource topology;
- authoritative OQ-013 Approval relationships and immutable delivery-reference implementation;
- TranslationWork operational lifecycle/state vocabulary and retention details;
- exact draft↔TemplateVersion provenance and slot-membership Ash representation;
- exact Template migration action/conflict implementation;
- exact Ash representation of the accepted Template Version scaffold;
- substantive/localisable Template default semantics;
- exact derived media reverse-usage projection schema, rebuild/reconciliation mechanics and shared-object dependency accounting after GRILL-35/GRILL-37;
- JIT formalisation/proof of the validation ownership baseline (`EXPOSED-02`);
- editor/form-generation implications inside the authorised JIT.

These are downstream implementation/operational/proof gates, not reasons to reopen Block 3A absent new evidence or contradiction.

Translation authority/resource/lifecycle semantics are now covered by `GRILL-22`–`GRILL-26`. Public locale address/canonical/redirect semantics are now covered by `GRILL-39`. Generic search configuration, broader SEO projection detail, publication execution/correction detail, scheduling, caching and LiveAdmin reuse remain downstream until a real active-slice need warrants them.

### Mandatory consistency-sweep rule

Every accepted GRILL must update or verify, in the same dossier revision:

1. the executive extraction map;
2. proposed NewYou seams;
3. the current grill sequence;
4. deferred/exposed-question registers;
5. accepted-decision register;
6. SemVer progression;
7. latest conclusion;
8. any earlier statement that still presents a now-decided seam as currently “deferred”, “next”, “unresolved” or “not yet decided”;
9. publication/snapshot wording that could contradict the current mutable-draft → immutable-version governance boundary;
10. summary diagrams/contracts that could imply a superseded ownership model.

Historical accepted-decision text may preserve what was genuinely open **at the time** only when it is explicitly temporally qualified (for example, “Historical at GRILL-X acceptance”) and identifies the later resolving GRILL/current status where material. An unqualified stale historical statement is a dossier-integrity defect.

A stale earlier statement does not reopen a later accepted GRILL, but it must be repaired before continuing materially.

### Editorial Template closure and scoped JIT gates

`GRILL-19` closes the Beacon editorial Template branch for JIT handoff.

`GRILL-20` subsequently resolves the broader mutable-working-draft ownership dependency: dedicated subordinate `ContentDraft` authority now owns mutable authoring truth, including draft-local Template binding/membership where applicable.

Core `ContentTemplate` / `ContentTemplateVersion` Resource justification remains closed.

The following exact subgraphs remain gated inside Content & Media JIT:

1. **draft binding / Template slot membership / Template migration persistence shape** — semantic owners/version-cut/concurrency boundaries are now resolved through `GRILL-20`–`GRILL-25`; exact fields/actions remain JIT;
2. **Template Review/Approval persistence/actions** — `GRILL-26` resolves the semantic authority; exact typed relationships/action mechanics remain JIT;
3. **historical approval versus current selectability compatibility** — semantic model resolved by `GRILL-27`; exact catalogue/compatibility implementation remains JIT;
4. **substantive/localisable Template initial-content representation** — translation ownership is resolved by `GRILL-22`–`GRILL-24`; exact Template-localisable-default capability/persistence remains JIT-gated.

These scoped gates must not be bypassed through speculative fields, child Resources or duplicated authority.

Exact Ash representation choices that do not cross these gates may be explored only inside an authorised Content & Media JIT dossier.

This working Beacon dossier itself still does not authorise executable implementation.

---

## 16. Accepted working decisions

### GRILL-01 — Code-authoritative Block Catalogue

**Accepted:** 2026-09-19  
**First recorded in:** v0.2.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Section 6 for the full pressure test and exact decision text.

### GRILL-02 — Block Occurrences Are Subordinate, Not Independent Business Entities

**Accepted:** 2026-09-19  
**First recorded in:** v0.3.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.9–6.11 for the full pressure test and exact decision text.

### GRILL-03 — Content-Version-Owned Structured Block Storage

**Accepted:** 2026-09-19  
**First recorded in:** v0.4.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.12–6.14 for the full pressure test and exact decision text.

### GRILL-04 — Minimal Versioned Block Envelope

**Accepted:** 2026-09-19  
**First recorded in:** v0.5.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.15–6.18 for the full pressure test and exact decision text.

### GRILL-05 — Explicit Compatible Block-Schema Evolution

**Accepted:** 2026-09-19  
**First recorded in:** v0.6.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.19–6.21 for the full pressure test and exact decision text.

### GRILL-06 — Code-Defined Bounded Composition Slots

**Accepted:** 2026-09-19  
**First recorded in:** v0.7.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.22–6.24 for the full pressure test and exact decision text.

### GRILL-07 — Sections Are Catalogue/Composition Roles, Not Separate Content Entities

**Accepted:** 2026-09-19  
**First recorded in:** v0.8.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.25–6.27 for the full pressure test and exact decision text.

### GRILL-08 — Content Components Are Catalogue Roles Over Block Contracts, Not Separate Durable Entities

**Accepted:** 2026-09-19  
**First recorded in:** v0.9.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.28–6.30 for the full pressure test and exact decision text.

### GRILL-09 — Composed Patterns Are Copy-on-Instantiation Authoring Recipes, Not Runtime Content Entities

**Accepted:** 2026-09-20  
**First recorded in:** v0.10.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.31–6.33 for the full pressure test and exact decision text.

### GRILL-10 — Content Templates Are Revision-Addressable Authoring Scaffolds, Not Live Published-Content Authority

**Accepted:** 2026-09-20  
**First recorded in:** v0.11.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.34–6.36 for the full pressure test and exact decision text.

### GRILL-11 — Template Revisions Are Content & Media–Owned Governed Data Interpreted Through a Code-Defined Contract

**Accepted:** 2026-09-20  
**First recorded in:** v0.12.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.37–6.39 for the full pressure test and exact decision text.

### GRILL-12 — Editorial Content Templates Use Dedicated Template Identity/Version Resources Rather Than Reusing Deliverable Content Item/Version

**Accepted:** 2026-09-20  
**First recorded in:** v0.13.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.40–6.42 for the full pressure test and exact decision text.

### GRILL-13 — Template-Version Approval, Current Selection and Template Retirement Are Separate State Dimensions

**Accepted:** 2026-09-20  
**First recorded in:** v0.14.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.43–6.45 for the full pressure test and exact decision text.

### GRILL-14 — Each Editorial Content Template Has One Immutable Governed Content-Type Binding

**Accepted:** 2026-09-20  
**First recorded in:** v0.15.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.46–6.48 for the full pressure test and exact decision text.

### GRILL-15 — Content Template Versions Own Typed Declarative Scaffolds That Materialise Governed Draft Composition

**Accepted:** 2026-09-20  
**First recorded in:** v0.16.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.49–6.51 for the full pressure test and exact decision text.

### GRILL-16 — Template Structural Slots Are Non-Recursive Ordered Authoring Regions with Explicit Cardinality and Versioned Contract Allow-Lists

**Accepted:** 2026-09-20  
**First recorded in:** v0.17.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.52–6.54 for the full pressure test and exact decision text.

### GRILL-17 — Template-Governed Drafts Are Pinned to One Exact Active Template Version with Explicit Subordinate Slot Membership and Durable Migration Provenance

**Accepted:** 2026-09-20  
**First recorded in:** v0.18.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.55–6.57 for the full pressure test and exact decision text.

### GRILL-18 — Automatic Template Migration Is Limited to Stable-Key Structural Rebinding That Preserves Authored Content Exactly

**Accepted:** 2026-09-20  
**First recorded in:** v0.19.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.58–6.60 for the full pressure test and exact decision text.

### GRILL-19 — Editorial Content Template Reuse Discovery Is Semantically Closed and Ready for Content & Media JIT Handoff

**Accepted:** 2026-09-20  
**First recorded in:** v0.20.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.61–6.63 for the closure audit, accepted decision and handoff consequences.

### GRILL-20 — Mutable Content Authoring Uses Dedicated Durable ContentDraft Authority Separate from Immutable ContentVersion Truth

**Accepted:** 2026-09-20  
**First recorded in:** v0.21.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.64–6.66 for the full pressure test, exact decision and fixed consequences.

### GRILL-21 — Immutable Content Versions Are Cut at Exact Governance Boundaries; Approval, Publication and Correction Remain Separate Authorities

**Accepted:** 2026-09-20  
**First recorded in:** v0.22.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.67–6.69 for the full pressure test, exact decision and fixed consequences.

### GRILL-22 — ContentVersion Owns Shared Language-Neutral Composition; Locale Versions Own Independently Governed Localisable Content Against That Exact Structure

**Accepted:** 2026-09-20  
**First recorded in:** v0.23.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.70–6.72 for the full pressure test, exact decision and fixed consequences.

### GRILL-23 — Translation Staleness Is Derived from Exact Source Provenance; Carry-Forward Is Draft-Only and Never Transfers Approval

**Accepted:** 2026-09-20  
**First recorded in:** v0.24.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.73–6.75 for the full pressure test, exact decision and fixed consequences.

### GRILL-24 — Mutable Locale Authoring, Translation Work, and Immutable Locale Versions Are Separate Durable C&M Concerns

**Accepted:** 2026-09-20  
**First recorded in:** v0.25.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.76–6.78 for the full pressure test, exact decision and fixed consequences.

### GRILL-25 — Shared and Locale Drafts Are Single-Active Durable Workspaces with Explicit Abandonment, Exact-Revision Concurrency and Idempotent Version Cuts

**Accepted:** 2026-09-20  
**First recorded in:** v0.26.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.79–6.81 for the full pressure test, exact decision and fixed consequences.

### GRILL-26 — Approval Is Separate Scoped Evidence Against Exact Immutable C&M Subjects; Review and Readiness Remain Distinct

**Accepted:** 2026-09-20  
**First recorded in:** v0.27.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.82–6.84 for the full pressure test, exact decision and fixed consequences.

### GRILL-27 — Governed Content Types Are Code-Authoritative, Explicitly Revision-Addressable Contracts; Historical Approval and Current Compatibility Are Separate

**Accepted:** 2026-09-20  
**First recorded in:** v0.28.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.85–6.87 for the full pressure test, exact decision and fixed consequences.

### GRILL-28 — Publication Activates One Exact Eligible Locale Version; Scheduling Pins Exact Intent and Revalidates Before Activation

**Accepted:** 2026-09-20  
**First recorded in:** v0.29.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.88–6.90 for the full pressure test, exact decision and fixed consequences.

### GRILL-29 — Correction, Withdrawal and Supersession Are Distinct Durable Truths; Content Owns the Declaration While Dependent Domains Own Their Consequences

**Accepted:** 2026-09-20  
**First recorded in:** v0.30.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.91–6.93 for the full pressure test, exact decision and fixed consequences.

### GRILL-30 — The Content Version / Translation / Review / Approval / Publication / Correction Branch Is Semantically Closed for Content & Media JIT Handoff

**Accepted:** 2026-09-20  
**First recorded in:** v0.31.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.94–6.96 for the full closure pressure test, exact decision and fixed consequences.

**Branch outcome:** CLOSED / PASS FOR C&M JIT HANDOFF at semantic discovery level only.

### GRILL-31 — Governed Media Uses Platform-Owned Exact Asset Identities; Durable Derivatives Are Assets with Exact Source Lineage, While Storage Providers Own Bytes/Locators Only

**Accepted:** 2026-09-20  
**First recorded in:** v0.32.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.97–6.99 for the full pressure test, exact decision and fixed consequences.

**Current status after GRILL-36/GRILL-37:** provider-independence, stable asset identity and derivative identity remain accepted; the no-version-hierarchy conclusion is explicitly superseded by GRILL-36, replacement semantics are refined by GRILL-36, and deletion terminality is scoped by GRILL-37.

**Project-owner deployment direction recorded:** external S3-compatible media storage such as Wasabi (or equivalent) is intended to offload media bytes from the application server; exact provider remains implementation-replaceable and non-authoritative.

### GRILL-32 — Media Ingest Uses Restricted Pre-Authority Staging, Durable Accepted-Ingest Intent and Verified Idempotent Object-Store Finalisation; Processing Workers Never Become Media Authority

**Accepted:** 2026-09-20  
**First recorded in:** v0.33.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.100–6.102 for the full pressure test, exact decision and fixed consequences.

### GRILL-33 — Media Rights and Publication Remain Exact C&M Authority; Derivative Permissions Do Not Auto-Inherit, and Protected Delivery Composes Current C&M, Access and Consent Truth into a Bounded Capability

**Accepted:** 2026-09-20  
**First recorded in:** v0.34.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.103–6.105 for the full pressure test, exact decision and fixed consequences.

### GRILL-34 — Media Withdrawal Immediately Removes Delivery Authority; Physical Deletion Is a Separate Durable, Idempotent and Non-Resurrecting Disposition Workflow Across Exact Assets, Derivatives, Storage and Processors

**Accepted:** 2026-09-20  
**First recorded in:** v0.35.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.106–6.108 for the full pressure test, exact decision and fixed consequences.

**Current status after GRILL-37:** Withdrawal/deletion separation and durable deletion semantics remain accepted; the pre-version terminality/shared-object wording is refined by GRILL-37.

### GRILL-35 — Media Consumers Own Exact Forward Asset References; Reverse Usage Indexing Is Derived/Rebuildable, and Replacement Is Owner-Mediated Against the Exact Expected Reference

**Accepted:** 2026-09-20  
**First recorded in:** v0.36.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.109–6.111 for the full pressure test, exact decision and fixed consequences.

**Current status after GRILL-36/GRILL-37:** owner/reverse-index semantics remain accepted; governed references are exact `MediaAssetVersion`, and destructive dependency discovery must account for shared-object/version dependencies before provider deletion.

### GRILL-36 — Governed Media Separates Stable MediaAsset Identity from Immutable MediaAssetVersion Truth; Publication, Provenance and Governed Consumer References Pin the Exact Version

**Accepted:** 2026-09-20  
**First recorded in:** v0.37.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.112–6.115 for the closure audit, exact decision, supersession/refinement map and fixed consequences.

**Supersession scope:** explicitly supersedes only GRILL-31's no-version-hierarchy conclusion; refines GRILL-31 replacement semantics, GRILL-35 governed references, GRILL-33 Publication target and GRILL-32 storage/provenance target as described in Section 6.114.

No other grill decision is accepted in v0.37.0.

### GRILL-37 — Media Deletion Is Scoped to the Governed Version or Stable Asset Subject; Shared Immutable Bytes Survive Only While Another Lawfully Retained Version Requires Them, and Deleted Identities Never Resurrect

**Accepted:** 2026-09-21  
**First recorded in:** v0.38.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.116–6.119 for the Block 4A.7 audit, exact decision, refinement map and fixed consequences.

**Refinement scope:** refines only GRILL-34's pre-version terminality/object-sharing wording and completes GRILL-36's version-scoped deletion + same-asset byte-sharing semantics. All other GRILL-31→36 ownership, lifecycle, failure and provenance conclusions remain accepted.

No other grill decision is accepted in v0.38.0.

### GRILL-38 — The Media Identity / Version / Ingest / Rights / Publication / Delivery / Withdrawal / Deletion / Usage-Reference Branch Is Semantically Closed for Content & Media JIT Handoff

**Accepted:** 2026-09-21  
**First recorded in:** v0.39.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.120–6.122 for the final corrected Block 4A closure audit, exact closure decision and fixed JIT-handoff consequences.

**Branch outcome:** CLOSED / PASS FOR C&M JIT HANDOFF at semantic reuse-discovery level only.

**Closure scope:** GRILL-31→37 remain controlling through the GRILL-36 and GRILL-37 refinement maps. Remaining OQ/legal/IP/vendor/retention/privacy/deletion-recovery/proof and exact implementation details remain downstream and are not resolved by this closure.

No other grill decision is accepted in v0.39.0.

### GRILL-39 — Published Locale Addresses Become Durable Content & Media Route Claims; Canonical URLs and Permanent Redirects Follow Exact Publication Truth While Phoenix Routing and Caches Remain Non-Authoritative

**Accepted:** 2026-09-21  
**First recorded in:** v0.40.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.124–6.126 for the Block 5A.1 pressure test, exact decision and fixed consequences.

**Current effect:** first public Publication turns the effective locale address into durable C&M route-claim/history truth; exact Publication remains the target authority; historical aliases cannot bypass current eligibility; Phoenix/ETS/sitemap/search/cache remain derived delivery/projection mechanisms.

**Beacon extraction effect:** path uniqueness, central URL generation, explicit Phoenix mount boundaries and published-page sitemap derivation are useful concepts; mutable `Page.path`, broad CMS catch-all route authority, arbitrary editor-authored dynamic paths and ETS correctness authority are rejected.

No other grill decision is accepted in v0.40.0.

### GRILL-40 — Public Route Activation Is Atomic with Exact Publication; Effective Route Identity Is Normalised, Scheduling Does Not Reserve Addresses, and Historical Slug Reversion Must Preserve Loop-Free Address History

**Accepted:** 2026-09-21  
**First recorded in:** v0.41.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.128–6.131 for the corrected Block 5A route-activation pressure test, exact refinement decision, refinement map and corrected closure audit.

**Refinement scope:** refines GRILL-39 only by making the activation/address commit boundary atomic, binding routes explicitly to exact Publication/locale/content versions, defining uniqueness over a normalised effective route identity, prohibiting implicit schedule-time reservations and requiring loop-free slug reversion. GRILL-39's ownership/namespace/projection conclusions otherwise remain accepted.

**Branch status after this decision:** Block 5A semantic closure audit now passes, but formal branch closure remains pending a separate human-accepted closure decision.

No other grill decision is accepted in v0.41.0.


### GRILL-41 — The Public Addressability / Canonical / Redirect / Indexability / Discovery-Projection Branch Is Semantically Closed for Content & Media JIT Handoff

**Accepted:** 2026-09-21  
**First recorded in:** v0.42.0  
**Authority level:** working reuse-discovery decision only; non-authoritative.

See Sections 6.133–6.135 for the final adversarial closure audit, exact closure decision and fixed consequences.

**Closure effect:** Block 5A is CLOSED / PASS for C&M JIT handoff at semantic reuse-discovery level. GRILL-39/40 remain controlling for public-address ownership/history and atomic exact activation. Discovery/indexing/sitemap/router/cache state remains derived/rebuildable; OQ-014/OQ-015/OQ-016 and all exact implementation topology remain downstream.

No other grill decision is accepted in v0.42.0.

---

## 17. SemVer policy for this working dossier

This document uses SemVer for the discovery artifact itself.

- **PATCH** — editorial/source-reference correction that changes no reuse conclusion or grill decision.
- **MINOR** — new grill decisions, new subsystem extraction, or materially refined reuse/adaptation conclusions while the dossier remains working/non-authoritative.
- **MAJOR** — only if the completed evidence pack is deliberately frozen as a stable handoff, or if a future incompatible restructuring of the dossier contract is required.

Likely progression:

```text
v0.1.0  broad research/extraction orientation baseline
v0.2.0  GRILL-01 accepted: code-authoritative block catalogue
v0.3.0  GRILL-02 accepted: subordinate block occurrences
v0.4.0  GRILL-03 accepted: Content-Version-owned structured block storage
v0.5.0  GRILL-04 accepted: minimal versioned block envelope
v0.6.0  GRILL-05 accepted: explicit compatible block-schema evolution
v0.7.0  GRILL-06 accepted: code-defined bounded composition slots
v0.8.0  GRILL-07 accepted: sections are catalogue/composition roles, not separate content entities
v0.9.0  GRILL-08 accepted: content components are catalogue roles over block contracts, not separate durable entities
v0.10.0 GRILL-09 accepted: composed patterns are copy-on-instantiation authoring recipes, not runtime content entities
v0.11.0 GRILL-10 accepted: content templates are revision-addressable authoring scaffolds, not live published-content authority
v0.12.0 GRILL-11 accepted: template revisions are Content & Media-owned governed data interpreted through a code-defined contract
v0.13.0 GRILL-12 accepted: editorial content templates use dedicated template identity/version Resources rather than reusing deliverable Content Item/Version
v0.14.0 GRILL-13 accepted: template-version approval, current selection and template retirement are separate state dimensions
v0.15.0 GRILL-14 accepted: each editorial ContentTemplate has one immutable governed content-type binding
v0.15.1 PATCH: whole-document consistency repair; no new GRILL; adds owner-review lifecycle clarification, exposed dependencies and Block-2A.6/Ash-design hard stop
v0.16.0 GRILL-15 accepted: Content Template Versions own typed declarative scaffolds that materialise governed draft composition
v0.17.0 GRILL-16 accepted: Template structural slots are non-recursive ordered authoring regions with explicit cardinality and versioned contract allow-lists
v0.18.0 GRILL-17 accepted: Template-governed drafts are pinned to one exact active Template Version with explicit subordinate slot membership and durable migration provenance
v0.19.0 GRILL-18 accepted: automatic Template migration is limited to stable-key structural rebinding that preserves authored content exactly
v0.20.0 GRILL-19 accepted: editorial Content Template reuse discovery is semantically closed and ready for Content & Media JIT handoff
v0.21.0 GRILL-20 accepted: mutable content authoring uses dedicated durable ContentDraft authority separate from immutable ContentVersion truth
v0.22.0 GRILL-21 accepted: immutable Content Versions are cut at exact governance boundaries; Approval, Publication and Correction remain separate authorities
v0.23.0 GRILL-22 accepted: ContentVersion owns shared language-neutral composition; locale versions own independently governed localisable content against that exact structure
v0.24.0 GRILL-23 accepted: translation staleness is derived from exact source provenance; carry-forward is draft-only and never transfers approval
v0.24.1 PATCH: whole-document consistency repair only; no GRILL/architecture change
v0.25.0 GRILL-24 accepted: mutable locale authoring, TranslationWork and immutable locale versions are separate durable C&M concerns
v0.26.0 GRILL-25 accepted: shared and locale drafts are single-active durable workspaces with explicit abandonment, exact-revision concurrency and idempotent version cuts
v0.27.0 GRILL-26 accepted: Approval is separate scoped evidence against exact immutable C&M subjects; Review and readiness remain distinct
v0.28.0 GRILL-27 accepted: governed Content Types are code-authoritative explicitly revision-addressable contracts; historical Approval and current compatibility are separate
v0.29.0 GRILL-28 accepted: Publication activates one exact eligible locale version; scheduling pins exact intent and revalidates before activation
v0.30.0 GRILL-29 accepted: Correction, Withdrawal and supersession are distinct durable truths; Content owns the declaration while dependent Domains own their consequences
v0.31.0 GRILL-30 accepted: Block 3A content-governance branch semantically CLOSED / PASS for C&M JIT handoff; stale historical progression wording repaired
v0.32.0 GRILL-31 accepted: platform-owned exact MediaAsset identities, exact derivative lineage and provider-independent external S3-compatible byte storage; Wasabi-or-equivalent deployment direction recorded
v0.33.0 GRILL-32 accepted: restricted pre-authority staging, durable accepted-ingest intent, verified idempotent object-store finalisation and non-authoritative async workers/providers
v0.34.0 GRILL-33 accepted: exact C&M media rights/publication authority with non-inherited derivative permissions and current cross-domain protected-delivery composition
v0.35.0 GRILL-34 accepted: immediate media withdrawal plus separate durable verified physical deletion/non-resurrection across assets, derivatives, storage, processors and restore
v0.36.0 GRILL-35 accepted: exact owner-owned forward MediaAsset references, derived/rebuildable reverse usage indexing and owner-mediated expected-reference replacement
v0.37.0 GRILL-36 accepted: stable MediaAsset identity separated from immutable MediaAssetVersion truth; exact-version Publication/provenance/consumer references; narrow GRILL-31/35 supersession/refinement
v0.38.0 GRILL-37 accepted: deletion/disposition scoped to exact version or stable asset; same-asset shared bytes retained only while lawfully required; byte-destruction impact expansion and non-resurrection refined
v0.39.0 GRILL-38 accepted: Block 4A media branch semantically CLOSED / PASS for C&M JIT handoff; final corrected closure audit passed
v0.40.0 GRILL-39 accepted: published locale addresses become durable C&M route claims; canonical/redirect history follows exact Publication truth; router/ETS/sitemap/search/cache remain non-authoritative
v0.41.0 GRILL-40 accepted: exact Publication + canonical claim + redirect/history commit atomically; normalised effective route uniqueness; no schedule-time reservation; loop-free historical slug reversion
v0.42.0 GRILL-41 accepted: Block 5A public-addressability/canonical/redirect/indexability/discovery-projection branch semantically CLOSED / PASS for C&M JIT handoff; OQ-014/OQ-015/OQ-016 preserved downstream
v0.42.1 PATCH: whole-source stabilisation consistency repair only; no GRILL/architecture change
...
v0.x.0  cumulative working discovery
v1.0.0  optional completed/frozen evidence handoff after explicit review
```

A `v1.0.0` freeze would make the dossier stable evidence only. It would still not become Product Law, Architecture Law, Domain Law, Roadmap Law or implementation authority.

---

## 18. v0.42.1 conclusion

The dossier now contains forty-one accepted narrow reuse/architecture-discovery decisions: `GRILL-01` through `GRILL-41`.

Block 3A remains **CLOSED / PASS FOR C&M JIT HANDOFF**.

Block 4A remains **CLOSED / PASS FOR C&M JIT HANDOFF** at semantic reuse-discovery level.

Block 5A is now **CLOSED / PASS FOR C&M JIT HANDOFF** at semantic reuse-discovery level.

GRILL-39 remains the controlling ownership/address-history decision. GRILL-40 refines the exact activation boundary:

```text
normalised effective public route
→ exact Publication
→ exact ContentTranslationVersion
→ exact ContentVersion

activation that creates/changes public address truth
=
exact Publication activation
+ canonical route claim
+ required superseded-address history
committed as one authoritative PostgreSQL transition
```

GRILL-41 closes the bounded branch after a final adversarial audit found no additional durable SEO/indexability/sitemap/search-engine lifecycle requiring another Domain or business Resource.

Public deliverability, access eligibility and ordinary search-engine indexability remain distinct. Canonical/alternate tags, sitemap rows, robots/noindex output, structured-data output, native-search projections, generated route modules, ETS/cache state and external crawler/search-engine state are derived/rebuildable outputs. None can create or preserve Publication, access, canonical-address or Withdrawal authority.

Downstream authority remains deliberately intact:

- `OQ-014` still governs edge/cache design;
- `OQ-015` still governs native-search configuration;
- `OQ-016` still governs publication scheduler reliability, retries, alerts, stale-approval checks and recovery;
- historical-address obligation expiry / possible unrelated-content reuse policy remains unresolved;
- exact Ash route/address Resource topology, fields, indexes, constraints and actions remain JIT;
- exact Unicode/case/percent-encoding/trailing-slash normalisation remains JIT;
- redirect HTTP status and response mechanics remain JIT;
- exact scheduling/retry implementation, canonical/hreflang/structured-data/robots/sitemap rendering, indexes, caches and workers remain JIT/proof detail;
- FP-001's conditional Content & Media JIT dossier disposition remains unchanged by this working artifact.

Beacon CMS `v0.5.1` remains reference/donor evidence only. No Beacon runtime authority or required dependency is introduced.

**Next-action rule:** do not reopen Block 5A or invent another public-addressability/SEO/search GRILL for dossier completeness. Select the next subsystem/seam only from an actual Content & Media JIT need or a newly exposed authority gap. If later evidence contradicts GRILL-39/40/41, reopen at the smallest correct authority/reuse-discovery level.

Implementation remains unauthorised by this working reuse-discovery dossier.

