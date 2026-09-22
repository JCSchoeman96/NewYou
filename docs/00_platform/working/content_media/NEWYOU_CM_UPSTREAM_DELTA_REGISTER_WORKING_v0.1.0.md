# NewYou Content & Media Pre-JIT Delta / Deferred-Detail Register — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE ROUTING REGISTER
- **Purpose:** Preserve unresolved governed gates and JIT-only details exposed by the Content & Media / Beacon discovery without letting the compact contract silently decide them.
- **Implementation:** NOT AUTHORISED.
- **Deep source:** `BEACON_REUSE_GRILL_AND_EXTRACTION_WORKING_v0.42.1.md`
- **Deep-source SHA-256:** `08823adec046ae7222aff83725ded76a0bed68f629a1b7466a18acdc8efc4291`

## 1. How to use this register

These local `CM-UPD-*` keys are **working routing labels only**. They are not Product `DEC`, Architecture `ARC/ARQ`, Open Question `OQ`, Feature Pack or other governed identifiers.

Do not “resolve” an item here if its owner is Product/Architecture/Privacy/Operations/Legal or another governed process. This file only records where the compact C&M contract stops.

## 2. Governed/open deltas

### CM-UPD-001 — OQ-013 exact translation resource design

**Owner/gate:** `OQ-013` Architecture Review.  
**Current working constraints:** GRILL-22...27 already constrain the semantics: shared ContentVersion truth, independent locale versions, mutable locale authoring/TranslationWork distinction, exact source provenance, scoped Approval and version-addressable Content Type contracts.  
**Still unresolved:** exact Ash Resource boundaries/relationships, locale/version identities/indexes, Approval relationship implementation and immutable delivery-reference shape.  
**Must not happen:** use OQ-013 as permission to collapse shared/locale truth or treat “latest translation” as delivery authority.

### CM-UPD-002 — OQ-014 edge/cache/protected-delivery mechanics

**Owner/gate:** `OQ-014` Architecture Review.  
**Current working constraints:** edge/cache/CDN state is non-authoritative; protected media delivery rechecks current C&M + access/consent authority; withdrawal must not be defeated by stale edge state.  
**Still unresolved:** cache eligibility, Cloudflare rules, signed delivery, TTL/purge behaviour, security controls, immediate safety-withdrawal invalidation and proof.  
**Must not happen:** provider cache state becomes Publication/access truth.

### CM-UPD-003 — OQ-015 native-search configuration

**Owner/gate:** `OQ-015` Architecture Review.  
**Current working constraints:** search is derived, access-first, publication-aware and rebuildable; withdrawn/ineligible content cannot be returned because an index is stale.  
**Still unresolved:** PostgreSQL FTS details, synonyms, ranking weights, indexes, pagination and future semantic-search boundary.  
**Must not happen:** search ranking/index state becomes publication or access authority.

### CM-UPD-004 — OQ-016 publication operations

**Owner/gate:** `OQ-016` Operations / Architecture Review.  
**Current working constraints:** schedule intent pins an exact immutable target; schedule creation does not reserve a route; execution revalidates current eligibility and route availability; Publication/address activation is atomic where address truth changes.  
**Still unresolved:** scheduler reliability, retries, alert ownership, approved-window semantics, stale-approval checks, failed/refused attempt evidence and recovery/reconciliation.  
**Must not happen:** queue/worker success becomes Publication truth or schedule creation preclaims authority not granted by Product Law.

### CM-UPD-005 — OQ-020 live/video provider validation

**Owner/gate:** `OQ-020` Vendor / Architecture Review.  
**Current working constraints:** provider capture/status is evidence only; recordings/replays/clips require governed C&M media identity/version/publication/rights semantics.  
**Still unresolved:** Restream/Cloudflare Stream plan/features, live-input/recording limits, failure handling and integration proof.

### CM-UPD-006 — OQ-021 recording/video consent and retention

**Owner/gate:** `OQ-021` Legal / Operations Review.  
**Current working constraints:** C&M media rights/publication do not override consent/privacy authority; derivative permissions do not auto-inherit.  
**Still unresolved:** speaker/attendee consent, recording/edit/replay/clip rights, retention and withdrawal rules.

### CM-UPD-007 — OQ-024 source-content/media inventory

**Owner/gate:** `OQ-024` Content Review.  
**Current working constraints:** imported/migrated content/media must enter governed identity/version/rights/translation/publication truth rather than importing legacy platform state as authority.  
**Still unresolved:** actual Nuwe Jy lesson/video/download inventory, rights, duplication, missing translations and outdated material.

### CM-UPD-008 — OQ-029 retention schedule matrix

**Owner/gate:** `OQ-029` Legal / Finance / Professional Review.  
**Current working constraints:** immutability while retained is not indefinite retention; media version/asset disposition must respect lawful retention and deletion scope.  
**Still unresolved:** category-specific retention/archive/deletion durations and exceptions.

### CM-UPD-009 — OQ-030 / OQ-031 / OQ-032 deletion and recovery operations

**Owners/gates:** Privacy / Architecture / Security / Operations.  
**Current working constraints:** media deletion is durable, idempotent, verified and non-resurrecting; shared bytes may survive only for lawful retained dependants; caches/search/provider state must reconcile; restored environments cannot resurrect deleted identities.  
**Still unresolved:** processor inventory/verification, backup expiry/replay, restore isolation/go-live gates, deletion job operations/deadlines/retries/completion evidence and export/deletion orchestration.

### CM-UPD-010 — Historical public-address obligation expiry / unrelated reuse

**Owner/gate:** downstream Product/SEO/legal/JIT policy as applicable; no current governed answer.  
**Current working constraints:** previously exposed addresses cannot be silently reassigned while the historical redirect obligation remains; same-content/locale reversion must remain loop-free.  
**Still unresolved:** whether the obligation can ever expire, what policy permits expiry, and whether/when unrelated content may reuse a formerly public address.  
**Must not happen:** JIT invents a reuse timeout because a database uniqueness constraint is inconvenient.

### CM-UPD-011 — Correction impact/severity and downstream remediation contract

**Owner/gate:** Product/Content/Safety/Privacy/affected Domain JIT as applicable.  
**Current working constraints:** Correction, supersession and Withdrawal are distinct; C&M owns the content declaration, affected Domains own their own consequences.  
**Still unresolved:** exact bounded correction-impact vocabulary, which severities trigger which downstream durable consequences, and owner-specific remediation contracts/proofs.  
**Must not happen:** one generic C&M worker directly mutates foreign Domain authority.

### CM-UPD-012 — Direct Beacon/LiveAdmin source-copy policy and IP/provenance

**Owner/gate:** legal/IP/contributor-rights + authorised JIT/code review.  
**Current working constraints:** this pack authorises no direct source copy. Beacon/LiveAdmin are MIT donor/reference evidence; clean reimplementation is preferred where simpler.  
**Still unresolved:** whether any specific helper/UI fragment is worth copying, exact destination, provenance notice placement and legal/code-review acceptance.  
**If later proposed:** pin repository, stable tag/commit, exact path/blob SHA, licence/copyright, modifications, reason for copy and proof.

### CM-UPD-013 — FP-001 Content & Media dossier adjudication

**Owner/gate:** governed FP-001 reconciliation / Phase 7 process.  
**Current working constraints:** the pre-JIT reuse evidence may strengthen the case for a C&M dossier because FP-001 uses bilingual public content/publication/address semantics.  
**Still unresolved:** the governed `CONDITIONAL` dossier disposition must be adjudicated at the proper FP-001 reconciliation step.  
**Must not happen:** this pack silently flips the Feature Pack disposition or authorises implementation.

## 3. JIT-only deferred details — not upstream deltas

The following should normally be decided inside an authorised C&M JIT/proof task and should **not** be escalated merely because they are absent from this compact contract:

- exact Ash module/Resource/action names;
- exact table/field/identity/index/constraint names;
- block representation choice (`Ash.Type.Union`, typed struct, embedded Resource, etc.);
- draft concurrency/optimistic lock implementation;
- Template scaffold/slot/migration persistence representation;
- localisable Template default/initial-content capability representation;
- exact TranslationWork lifecycle vocabulary and retention;
- exact Review/Approval Resource topology;
- Content Type catalogue module/API and compatibility-function code shape;
- Publication/schedule-intent/correction/withdrawal Resource topology;
- exact idempotency-key storage/reconciliation mechanism;
- media storage-reference/shared-byte accounting representation;
- derived reverse-usage projection schema/rebuild implementation;
- object-store provider selection/configuration;
- route/address Resource topology;
- route prefix, slug generator, Unicode/case/percent-encoding/trailing-slash normalisation algorithm;
- redirect HTTP status/response mechanics;
- canonical/hreflang/schema/robots/sitemap rendering implementation;
- exact search indexes/ranking/pagination under OQ-015;
- exact cache/TTL/purge mechanics under OQ-014;
- exact Oban jobs/queues/retry schedules under OQ-016 and media processing;
- PubSub topics/freshness messages;
- LiveAdmin table/editor primitive reuse versus clean reimplementation;
- operator UI components/forms/routes.

## 4. Closed seams that should not be reopened casually

| Closed seam | Controlling decisions |
|---|---|
| Editorial Template semantics | GRILL-10...19 |
| Mutable/immutable content + locale + Review/Approval/Publication/Correction | GRILL-20...30 |
| Media identity/version/ingest/rights/delivery/deletion/references | GRILL-31...38, with GRILL-36/37 refinements |
| Public addressability/canonical/redirect/indexability/discovery projection | GRILL-39...41, with GRILL-40 refinement |

Reopen only for new evidence, changed scope, a higher-authority contradiction or a genuine JIT-discovered semantic gap.
