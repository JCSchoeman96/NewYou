# NewYou Content & Media Pre-JIT Contract — Working Consolidation v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT CONTRACT
- **Purpose:** Compact planning contract for future Content & Media JIT/Feature Pack work without loading the full Beacon reuse-discovery chronology.
- **Authority:** NONE. Live NewYou Product, Architecture, Domain, Roadmap, Operating Model, Open Work and applicable Feature Pack/JIT authority always win.
- **Implementation:** NOT AUTHORISED.
- **Deep source:** `BEACON_REUSE_GRILL_AND_EXTRACTION_WORKING_v0.42.1.md`
- **Deep-source SHA-256:** `08823adec046ae7222aff83725ded76a0bed68f629a1b7466a18acdc8efc4291`
- **Source semantic audit:** `NEWYOU_CM_PREJIT_STABILISATION_AUDIT_WORKING_v0.1.0.md`
- **Source mechanical recertification:** `NEWYOU_CM_PREJIT_STABILISATION_MECHANICAL_RECERTIFICATION_v0.1.1.md`
- **Conflict rule:** If this contract conflicts with current higher authority, stop at the correct authority level. Do not repair Product/Architecture/Domain law here.

## Live authority baseline used for this consolidation

Verified against `JCSchoeman96/NewYou` default branch at:

`be6b9ea4bdfc5a638a24affa20e6c75cd9fc321f`

Current routed authority:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.40.md`
5. `03_ARCHITECTURE_v1.1.0.md`
6. `04_DOMAIN_MAP_v1.1.0.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.0.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` when frontend/public publishing is in scope.

The deep source remains working evidence only. This compact contract is likewise working/non-authoritative.

## 1. Scope and stop boundary

This contract preserves the durable conclusions needed to plan NewYou Content & Media without repeatedly loading the full 593 KB discovery source.

It covers:

- governed block/composition contracts;
- editorial templates and template versions;
- mutable authoring versus immutable content versions;
- locale/translation authoring and immutable locale versions;
- Review, Approval, Publication, scheduling, correction and withdrawal boundaries;
- governed media identity/version/ingest/rights/publication/delivery/deletion/reference semantics;
- public locale addresses, canonical/redirect history and discovery projections;
- Beacon/LiveAdmin reuse/adapt/reimplement/reject boundaries.

It does **not** decide exact Ash modules, fields, tables, indexes, actions, workers, queues, cache keys, route-prefix syntax, Unicode normalisation algorithm, search ranking weights, Cloudflare configuration, storage provider, UI component implementation or deployment sequence.

Broad Beacon/C&M semantic discovery is parked after GRILL-41. Reopen only for new evidence, changed scope, higher-authority contradiction or a genuine JIT-discovered semantic gap.

## 2. Authority and ownership

Every durable truth has one owner.

| Truth | Working owner/boundary |
|---|---|
| Conceptual content identity/type/audience/risk/relationships | Content & Media |
| Mutable editorial working state | Content & Media authoring boundary |
| Immutable shared content versions | Content & Media |
| Immutable locale/translation versions | Content & Media |
| Review evidence and scoped Approval evidence | Content & Media where C&M approval is the applicable owner; required external approvers remain separate authority |
| Publication/correction/withdrawal truth | Content & Media |
| Governed media identity/version/rights/publication state | Content & Media |
| Application route namespace/mechanism | Phoenix/application code |
| Durable public-content address claim/history inside the permitted namespace | Content & Media |
| Access/entitlement | Identity & Access / Entitlements as governed |
| Consent/privacy purpose and deletion orchestration | Privacy & Consent |
| Safety consequences | Safety & Eligibility / affected owner as governed |
| Search/sitemap/cache/ETS/generated-route/crawler state | Derived projection only |
| Object-store/provider state | Bytes/locator/provider evidence only, not business authority |
| Experiment assignment/decision | Experimentation, not CMS/PageVariant |

Cross-domain mutation goes through the owning Domain. Rechecking an invariant in another layer does not transfer ownership.

## 3. Beacon/LiveAdmin donor boundary

Pinned donor baselines:

- Beacon CMS stable `v0.5.1`, tagged commit `97024750c88d7ccce34e21e802d8936c8e83c573`, MIT;
- Beacon LiveAdmin stable `v0.4.3`, MIT.

Beacon is **reference/donor evidence**, not NewYou authority and not an approved runtime dependency.

Use these classifications:

- **ADAPT:** concept is useful but implemented through NewYou Ash/Phoenix/domain boundaries;
- **REIMPLEMENT:** donor proves a mechanism/problem, but source/runtime coupling is unsuitable;
- **REJECT:** mechanism would create competing authority, unsafe runtime extensibility or unjustified coupling;
- **SELECTIVE REUSE CANDIDATE:** only for small isolated UI/helper code after exact JIT provenance/licence review;
- **DEFER:** no current need/evidence.

No source copy is authorised by this pack.

## 4. Governed block and composition contract

### 4.1 Block catalogue

The primitive block catalogue is code-authoritative. Editors do not create or mutate primitive block types in PostgreSQL.

Code owns:

- stable block type identifier;
- field/value contract;
- allowed options;
- renderer behaviour;
- schema-version interpretation;
- bounded slot contracts where needed.

Database content stores occurrences of approved block contracts, not mutable block definitions.

### 4.2 Ordinary block occurrence

An ordinary block occurrence is subordinate to its containing governed composition. It has no independent publication, approval, risk, entitlement or cross-content authority.

Minimum semantic envelope:

```text
occurrence_key
block_type
schema_version
typed payload
```

The occurrence key provides stable local continuity/addressability for editing, diffs, review references and provenance. It is not an independent business identity.

Order belongs to the containing sequence. Do not create a second canonical `position` authority.

Unknown/unsupported `(block_type, schema_version)` combinations fail closed.

### 4.3 Persistence/evolution

Ordinary occurrences are initially structured/embedded version-owned values, not independently persisted child Resources. Separate relational Resources require evidence of a real independent relational requirement.

A schema version changes when persisted interpretation would otherwise change. Historical published representations are not destructively rewritten to newer schemas.

Reader support precedes writer support for a new schema. Older schemas may become non-authorable while remaining readable as long as retained authoritative content requires them.

### 4.4 Slots, sections, components and patterns

A composition slot exists only where a block/template genuinely needs child composition. Slots are stable named bounded contract regions, not independent business entities.

Sections and “components” are catalogue/composition roles over approved contracts unless a later requirement proves independent durable identity.

Composed patterns are copy-on-instantiation authoring recipes. Once instantiated, resulting content is governed by the normal draft/version model; the pattern is not live runtime authority over already-created content.

## 5. Editorial template contract

### 5.1 Template identity and versioning

Editorial templates are authoring scaffolds, not deliverable/published content authority.

The working model justifies dedicated conceptual `ContentTemplate` and immutable `ContentTemplateVersion` identities rather than reusing deliverable `ContentItem`/`ContentVersion` as template authority.

Each template is bound to one governed content type. Its version owns typed declarative scaffold structure interpreted through code-defined contracts.

### 5.2 Template state dimensions

Keep separate:

- Template Version approval/governance;
- which exact approved Template Version is current/selectable for new authoring;
- template retirement/availability;
- historical drafts/content already bound to older versions.

A maturity/current marker must not replace required Approval evidence.

### 5.3 Structural slots

Template structural slots are non-recursive ordered authoring regions with explicit cardinality and versioned allow-lists/constraints.

Drafts bound to a template retain exact Template Version provenance and deterministic structural-slot membership.

Template changes do not silently rewrite existing drafts or governed versions.

### 5.4 Migration

Automatic template migration is permitted only for deterministic stable-key structural rebinding that preserves authored content exactly and satisfies the target contract.

A migration plan is validated against the exact source draft revision. Ambiguity, content transformation/deletion/invention, unsatisfied required regions, unsupported schemas or cardinality violations require explicit human resolution.

No partial mutation occurs on conflict. Composition, membership, target Template Version and migration provenance commit coherently only after the full plan passes.

## 6. Mutable authoring and immutable version contract

### 6.1 ContentItem, ContentDraft and ContentVersion

`ContentItem` is stable conceptual identity and high-level content authority.

A dedicated mutable `ContentDraft` authoring boundary is justified by autosave, concurrency, exact review snapshotting, template binding/membership and migration provenance. It is authoritative **working state**, not historical published truth.

`ContentVersion` is immutable governed shared-version truth. It is never the mutable autosave workspace.

A new ContentVersion is cut when exact authored content first crosses into an independently addressable governance boundary, normally formal review submission and otherwise before Approval, scheduling or Publication.

Draft autosave itself does not create a ContentVersion.

Snapshot/version cut binds to one exact draft revision so mixed/stale authoring state cannot become a governed version.

### 6.2 Concurrency

Initially permit one active authoritative mutable shared draft per governed authoring branch. Parallel merge-heavy editorial branches require evidence before introduction.

Draft mutations/version cuts must protect exact-revision expectations and be idempotent where retries can occur. Exact Ash/PostgreSQL locking/optimistic concurrency mechanisms remain JIT.

## 7. Locale and translation contract

### 7.1 Shared versus locale truth

One immutable `ContentVersion` owns shared language-neutral composition and locale-invariant governed values.

Each locale has an independent immutable `ContentTranslationVersion` lineage holding localisable governed truth against that exact shared structure.

Do not duplicate independent EN/AF block trees merely to represent translation.

The serving/delivery target is exact shared version + exact eligible locale version, never “latest”.

### 7.2 Mutable locale authoring and TranslationWork

Mutable locale authoring is separate from immutable locale version truth. The working model justifies subordinate mutable locale-draft semantics and durable translation-work/provenance concepts without deciding final Ash topology.

Initially one active mutable locale draft exists per governed shared-draft/locale branch. Abandonment is explicit; superseded mutable work does not become historical published truth.

### 7.3 Translation provenance and staleness

Translation alignment/staleness derives from exact source/shared-version provenance, not a manually authoritative “stale” flag.

Carry-forward into a successor locale draft may be allowed only as draft authoring assistance where content remains semantically reusable. It never transfers prior Approval.

Machine-generated content never self-publishes where human approval is required.

Required bilingual content follows current Product Law; missing required approved translation blocks publication/delivery rather than silently falling back.

## 8. Content Type, Review and Approval contract

### 8.1 Content Type contract

Content types are code-authoritative stable type keys with explicit immutable contract revisions.

Template Versions, drafts and governed ContentVersions retain exact Content Type contract revision provenance where required for historical interpretation.

Historical approval is evaluated against the exact revision used at the time. Current selectability/authoring compatibility is a separate question evaluated by explicit directional code-defined compatibility.

Different revisions fail closed for new authoring unless compatibility is explicitly allowed.

No administrator-authored runtime Content Type compatibility DSL is introduced initially.

### 8.2 Review, Approval and readiness

Review, Approval and “ready to publish” are separate concerns.

Approval is durable scoped evidence against an exact immutable subject/version and an applicable requirement basis. One person may fulfil multiple roles but required approvals remain separately recorded where Product Law requires that distinction.

Approval does not create Publication. Publication does not create Approval.

Later content changes create a successor immutable subject requiring the applicable new review/approval path.

## 9. Publication, scheduling, correction and withdrawal contract

### 9.1 Publication

Publication activates one exact currently eligible locale version belonging to one exact immutable shared ContentVersion.

“Latest”, “approved” and “published/current” are distinct.

Publication must revalidate current eligibility, including required approvals/translations/access/safety/dependencies as governed.

### 9.2 Scheduled publication

A schedule pins exact intent/target. It does not dereference “current draft” or “latest version”.

Execution revalidates current eligibility at activation. Schedule creation does not reserve a public route unless later explicit authority creates a reservation capability.

Reliability/retry/alerts/recovery remain OQ-016.

### 9.3 Correction, supersession and withdrawal

Keep distinct:

- successor/superseding content;
- material correction;
- immediate withdrawal/current-use suppression;
- downstream owner consequences/remediation.

Content & Media owns the content declaration and exact content/publication truth. Affected Domains own their own durable consequences; C&M does not mutate foreign authority directly.

Withdrawal removes current delivery authority without erasing historical Publication evidence.

A correction creates successor immutable truth rather than editing the old published version in place.

Exact correction severity/impact vocabulary and owner-specific remediation implementation remain downstream.

## 10. Governed media contract

### 10.1 Identity/version/storage

Use a stable platform-owned `MediaAsset` conceptual identity and immutable `MediaAssetVersion` truth.

Publication, provenance and governed consumer references pin the exact version, not merely the stable asset identity.

A MediaAssetVersion records/derives exact bytes/checksum/storage provenance and applicable governed metadata/rights/risk/accessibility state.

Object-store/provider identity is not business identity. PostgreSQL/Ash remains business authority; external S3-compatible storage owns bytes/locators.

Durable derivatives are governed media assets/versions with exact source-version lineage. Derivative permissions do not automatically inherit from the source.

### 10.2 Ingest and async processing

Pre-authority upload/staging is restricted and not usable public/business media truth.

After required checks, NewYou may durably accept ingest intent and exact platform identity before permanent object-store finalisation, but storage-pending media is not usable as successfully ingested media.

Workers/providers are execution evidence only. Required finalisation is verified and retry/idempotency safe; restart/reordering cannot fabricate completion.

Optional derivative completion does not redefine source-version identity.

### 10.3 Rights/publication/protected delivery

Rights, provenance, risk and publication remain exact C&M authority.

Protected delivery composes current C&M media eligibility with current access/entitlement/consent authority and emits only a bounded short-lived delivery capability. A provider URL/credential never becomes durable entitlement.

### 10.4 Withdrawal and deletion

Withdrawal immediately removes delivery authority.

Physical deletion/disposition is separate durable work and must be idempotent, verifiable and non-resurrecting across exact governed subjects, derivatives, object storage, processors and recovery.

Disposition scope must distinguish:

- exact `MediaAssetVersion` terminality;
- whole stable `MediaAsset` terminality;
- byte-level destruction obligations.

Shared immutable bytes may remain only while another lawfully retained version still requires them. Byte sharing never evades a deletion obligation.

Deleted stable identities/versions never resurrect; later identical bytes enter under new governed identity where applicable.

### 10.5 References and reverse usage

Consuming Domains own exact forward references to the exact governed media version they use.

Reverse usage indexing is derived/rebuildable acceleration. An empty/stale reverse index cannot prove that destructive deletion is safe.

Replacement is owner-mediated against the exact expected reference so concurrent/stale replacement cannot silently rewrite unrelated or already-changed consumers.

## 11. Public addressability and discovery contract

### 11.1 Draft slug versus public address truth

Locale slug/path values originate in governed locale authoring/version truth.

Before first public Publication they do not create historical public-route obligations.

First eligible public Publication creates a durable locale-specific public address claim inside the permitted application-defined public-content namespace.

### 11.2 Exact route target and atomic activation

A public route resolves to:

```text
normalised effective public route
→ exact Publication
→ exact ContentTranslationVersion
→ exact ContentVersion
```

If activation creates/changes public address truth, the following are one coherent PostgreSQL authoritative transition:

```text
exact Publication activation
+ canonical route claim
+ required superseded-address redirect/history relation
```

Do not permit a current Publication without its required route claim or an orphaned claim from failed activation.

### 11.3 Canonical changes and redirect history

Same-address successor Publication changes the exact target without creating a new external address identity.

New-address successor Publication establishes the new canonical address and retains governed historical aliases/redirects for previously exposed addresses.

Historical aliases resolve to the current eligible canonical Publication and must not form avoidable chains/loops.

A previous address may become canonical again for the same conceptual content/locale only through a governed Publication transition that leaves loop-free convergent history.

Previously exposed addresses are not silently reassigned to unrelated content while their historical obligation remains active. Expiry/reuse policy remains downstream.

### 11.4 Normalised uniqueness and namespace

Uniqueness is over one normalised effective public-route identity, not merely raw submitted text. Equivalent addresses cannot become competing claims.

Exact Unicode/case/percent-encoding/trailing-slash/canonical-string algorithm remains JIT.

Application/system routes remain Phoenix/application authority. Editorial content cannot shadow them. Arbitrary administrator-authored parameterised/catch-all routes are not introduced initially.

### 11.5 Locale alternates, canonical metadata and discovery

Language switching/alternates resolve through the same conceptual ContentItem plus currently eligible sibling locale Publications. Do not blindly rewrite `/af/` to `/en/` or silently substitute a missing translation.

Canonical URL and alternate-language metadata derive from authoritative route-claim + exact Publication truth.

Public deliverability, access eligibility and ordinary search-engine indexability are distinct.

The following are derived/rebuildable outputs only:

- canonical/hreflang tags;
- sitemap rows;
- robots/noindex rendering;
- structured data;
- native-search indexes;
- generated route modules;
- ETS/router/cache state;
- external crawler/search-engine state.

Their lag/failure cannot create or preserve Publication/access/address authority after current C&M truth changes.

No separate SEO Domain, generic Route Domain, Indexability lifecycle or Sitemap business Resource is justified by current evidence.

## 12. Operator/admin boundary

NewYou's operator model remains the governed Library + Work Queue + Editorial Calendar + exact-target preview model.

Beacon LiveAdmin may inform small generic table/search/filter/sort/pagination/editor interaction mechanics, but LiveAdmin is not adopted as a second operator application or authority layer.

Do not introduce arbitrary executable editor content, arbitrary JS hooks, arbitrary stylesheets, stored executable helpers or a second frontend/runtime model merely because Beacon supports them.

## 13. Derived state and failure doctrine

The following can accelerate or project current truth but never become correctness authority:

- ETS;
- caches;
- generated route lookup state;
- PubSub;
- sitemap/search indexes;
- reverse media-usage indexes;
- workers/queues;
- provider callbacks/status;
- browser/LiveView state.

On restart/recovery, reconstruct them from durable current authority. Stale projections must fail safe for protected/withdrawn content and must not extend revoked access.

## 14. JIT-only exact design still required

The future authorised C&M JIT must choose/prove the smallest implementation preserving this contract, including as applicable:

- exact Ash Resource decomposition/names/fields/relationships;
- block union/typed-structure representation;
- draft optimistic concurrency and idempotency implementation;
- Template scaffold/slot/migration persistence shape;
- exact Review/Approval relations/actions;
- exact TranslationWork and locale-draft persistence;
- Content Type catalogue/revision/compatibility API;
- Publication/schedule intent/correction/withdrawal topology;
- media version/reference/shared-byte accounting;
- route/address claim representation and database constraints;
- normalisation/redirect HTTP mechanics;
- indexes/query patterns;
- Oban jobs/retries/reconciliation;
- cache/search/sitemap/robots/structured-data implementation;
- operator UI component choice.

Representation may use fewer Resources than the conceptual distinctions where one representation safely preserves all invariants. Do not create a Resource merely because a noun exists in this contract.

## 15. Open governed/downstream gates

This compact contract does not close:

- `OQ-013` translation resource design;
- `OQ-014` edge/cache design;
- `OQ-015` search configuration;
- `OQ-016` publication operations;
- `OQ-020` live/video validation;
- `OQ-021` recording/video consent/retention;
- `OQ-024` source-content/media inventory;
- `OQ-029` retention schedule matrix;
- `OQ-030` external processor deletion inventory;
- `OQ-031` backup restore/deletion replay;
- `OQ-032` export/deletion operations;
- IP/licence/contributor-rights review;
- historical-address obligation expiry/unrelated reuse policy;
- exact correction impact/remediation policy.

Use `NEWYOU_CM_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.0.md` for routing.

## 16. Accepted decision coverage register

| Decisions | Compressed meaning |
|---|---|
| GRILL-01...06 | Code-authoritative bounded block contracts, subordinate occurrences, structured version-owned storage, minimal envelope, explicit schema evolution, bounded slots. |
| GRILL-07...09 | Sections/components remain composition roles; patterns copy into authoring rather than becoming runtime authority. |
| GRILL-10...19 | Dedicated governed editorial Template identity/version semantics, lifecycle dimensions, content-type binding, typed scaffold/slots, draft provenance, safe migration; template branch closed. |
| GRILL-20...25 | Mutable shared/locale authoring separated from immutable shared/locale version truth; exact version cut, translation provenance/staleness and concurrency. |
| GRILL-26...30 | Review/Approval/Content-Type revision/Publication/Scheduling/Correction/Withdrawal semantics; content-governance branch closed. |
| GRILL-31...38 | Platform-owned media identity/version, ingest, rights, protected delivery, withdrawal, deletion, reference/reverse-index semantics; media branch closed with GRILL-36/37 refinements controlling. |
| GRILL-39...41 | Durable public route claims/history, exact atomic activation, normalised uniqueness, schedule non-reservation, loop-free reversion, derived discovery projections; addressability branch closed. |

All exact GRILL text and pressure-test chronology remains in the deep source/evidence index.

## 17. Closure / anti-drift rule

The stable C&M pre-JIT model is:

```text
code-governed content contracts
→ durable mutable authoring
→ exact immutable shared + locale versions
→ scoped Review/Approval
→ exact Publication / correction / withdrawal
→ exact media/version authority where referenced
→ exact public route claim where public
→ derived delivery/discovery projections
```

Broad Beacon reuse discovery is complete enough for JIT handoff.

Do not reopen it for ordinary implementation questions. Do not infer implementation authority from this pack. If JIT discovers a real contradiction, stop at the correct higher authority or reopen only the smallest affected working seam.
