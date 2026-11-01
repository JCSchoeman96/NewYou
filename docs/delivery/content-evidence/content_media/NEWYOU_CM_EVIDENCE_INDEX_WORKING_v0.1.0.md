# NewYou Content & Media Compressed Evidence Index — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE TRACEABILITY
- **Purpose:** Trace the compact Content & Media contract back to all accepted GRILL decisions, current NewYou authority and relevant Beacon/LiveAdmin donor evidence without loading the full deep source by default.
- **Implementation:** NOT AUTHORISED.
- **Deep source:** `BEACON_REUSE_GRILL_AND_EXTRACTION_WORKING_v0.42.1.md`
- **Deep-source SHA-256:** `08823adec046ae7222aff83725ded76a0bed68f629a1b7466a18acdc8efc4291`
- **Beacon baseline:** stable `v0.5.1`, tagged commit `97024750c88d7ccce34e21e802d8936c8e83c573`.
- **Beacon LiveAdmin baseline:** stable `v0.4.3`.

## 1. Authority baseline

Current NewYou baseline checked for compression:

`main = be6b9ea4bdfc5a638a24affa20e6c75cd9fc321f`

Primary C&M anchors:

- `00_PLATFORM_v1.3.0.md` §21E content/translation/media law;
- `03_ARCHITECTURE_v1.1.1.md` §10 content/search/media/provider boundaries and §11 deletion/recovery;
- `04_DOMAIN_MAP_v1.1.1.md` §6.7 Content & Media;
- `05_ROADMAP_v1.1.0.md` affected Feature Packs/gates;
- `PLATFORM_OPERATING_MODEL_v1.0.1.md` Content Library / Work Queue / Editorial Calendar operating model;
- `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` public publishing, editor and SEO/search contracts where relevant;
- `02_OPEN_WORK_v1.2.40.md` current OQ/development sequencing.

## 2. GRILL-to-contract traceability

| GRILL | Compact contract | Deep source | NewYou authority anchor | Beacon/LiveAdmin evidence posture |
|---|---|---|---|---|
| 01 | §4.1 | §6.7 | Domain §6.7; Product reusable blocks | `component.ex` / component contract — **ADAPT**, code authority retained by NewYou |
| 02 | §4.2 | §6.10 | immutable version/provenance law | component/page composition evidence — **ADAPT**, occurrence not independent entity |
| 03 | §4.3 | §6.13 | Postgres/Ash-first; immutable Content Version authority | Beacon persisted component/page patterns — **REIMPLEMENT/ADAPT**, not child-resource default |
| 04 | §4.2 | §6.17 | immutable exact version provenance | component attrs/slots — **ADAPT** into typed minimal envelope |
| 05 | §4.3 | §6.20 | compatible state evolution; immutable history | no direct Beacon schema-governance authority — **REIMPLEMENT** |
| 06 | §4.4 | §6.23 | bounded governed composition | `component_slot.ex`, `component_slot_attr.ex` — **ADAPT** |
| 07 | §4.4 | §6.26 | no Domain/Resource merely for UI grouping | Beacon editor/layout concepts — **REFERENCE**, no separate Section authority |
| 08 | §4.4 | §6.29 | one owner per durable truth | Beacon component terminology — **ADAPT as role**, reject entity inflation |
| 09 | §4.4 | §6.32 | immutable published content, no live hidden authority | reusable composition idea — **ADAPT copy-on-instantiation** |
| 10 | §5.1 | §6.35 | governed reusable content authoring | Beacon layouts/templates/pages — **ADAPT concept**, not runtime published authority |
| 11 | §5.1 | §6.38 | C&M owns governed runtime content; code interprets contracts | Beacon data-driven content — **ADAPT**, NewYou contract-controlled |
| 12 | §5.1 | §6.41 | durable truth separation | no direct donor for NewYou template identity/version split — **REIMPLEMENT** |
| 13 | §5.2 | §6.44 | approval evidence distinct from lifecycle/current state | Beacon simple state insufficient — **REIMPLEMENT** |
| 14 | §5.1/§8.1 | §6.47 | governed content type / content ownership | Beacon type/page concepts only — **ADAPT boundary** |
| 15 | §5.1/§5.3 | §6.50 | validated governed composition | component attributes/slots — **ADAPT scaffold concept** |
| 16 | §5.3 | §6.53 | bounded composability | Beacon slots — **ADAPT**, NewYou semantics stronger |
| 17 | §5.3 | §6.56 | exact provenance / mutable draft boundary | no direct donor for binding/membership provenance — **REIMPLEMENT** |
| 18 | §5.4 | §6.59 | safe explicit migration/evolution | no direct donor — **REIMPLEMENT** |
| 19 | §1/§5 | §6.62 | JIT deferral / no speculative implementation | branch closure evidence only |
| 20 | §6.1 | §6.65 | Product immutability; Domain C&M ownership | `page.ex` mutable state + snapshot principle — **ADAPT**, direct authority rejected |
| 21 | §6.1 | §6.68 | Product §21E.8; exact governance versions | `page_event.ex`, `page_snapshot.ex` — separation idea **ADAPT**, snapshot model **REJECT/REIMPLEMENT** |
| 22 | §7.1 | §6.71 | Product conceptual item/version/translation structure; bilingual law | no adequate Beacon translation donor — **REIMPLEMENT from NewYou law** |
| 23 | §7.3 | §6.74 | exact source/translation provenance; no silent machine fallback | no direct donor — **REIMPLEMENT** |
| 24 | §7.2 | §6.77 | C&M locale branches/translations | no direct donor — **REIMPLEMENT**, OQ-013 retained |
| 25 | §6.2/§7.2 | §6.80 | concurrency/idempotency/retry doctrine | Beacon editing evidence only — **REIMPLEMENT** authoritative concurrency |
| 26 | §8.2 | §6.83 | Product §21E.4 approvals; separate approvals | Beacon lifecycle insufficient — **REIMPLEMENT** scoped Approval evidence |
| 27 | §8.1 | §6.86 | code-governed contracts + historical interpretation | no direct donor for revision compatibility — **REIMPLEMENT** |
| 28 | §9.1/§9.2 | §6.89 | Product §21E.9; Architecture exact publication target | `page_event.ex` publish event as reference — **ADAPT concept**, lifecycle authority rejected |
| 29 | §9.3 | §6.92 | Product §21E.10 correction/withdrawal | Beacon publish/unpublish too weak — **REIMPLEMENT** |
| 30 | §1/§9 | §6.95 | branch semantic closure / JIT boundary | closure evidence only |
| 31 | §10.1 | §6.98 | Product §21E.15; Architecture §10.3 media identity/provider boundary | `media_library/asset.ex`, `provider.ex` — **ADAPT HIGH VALUE** |
| 32 | §10.2 | §6.101 | durable async/idempotency/recovery doctrine | `upload_metadata.ex`, provider/processors — **ADAPT/REIMPLEMENT**; worker not authority |
| 33 | §10.3 | §6.104 | media rights/publication + protected access | media provider/URL patterns — **REIMPLEMENT** bounded delivery; derivative permission non-inheritance is NewYou law/working semantics |
| 34 | §10.4 | §6.107 | Product/Architecture deletion/withdrawal separation | stable S3 delete/provider behaviour insufficient — **REIMPLEMENT**, direct semantics rejected |
| 35 | §10.5 | §6.110 | one owner per reference truth; projections rebuildable | media library relationships as reference — **ADAPT** forward refs; reverse index derived |
| 36 | §10.1/§10.5 | §6.113 | exact version provenance/immutable media | Beacon asset model lacks NewYou version hierarchy — **REIMPLEMENT**; supersedes narrow GRILL-31 assumption |
| 37 | §10.4 | §6.117 | deletion/retention/recovery architecture | no donor for version/asset/byte scoped disposition — **REIMPLEMENT** |
| 38 | §1/§10 | §6.121 | branch semantic closure / downstream privacy/vendor gates | closure evidence only |
| 39 | §11.1/§11.3/§11.5 | §6.125 | Product §21E.13; FES §12; Domain discovery metadata | `page.ex`, `router.ex`, `router_server.ex`, `loader/routes.ex`, sitemap — bounded concepts **ADAPT**, CMS/ETS authority **REJECT** |
| 40 | §11.2/§11.4 | §6.129 | PostgreSQL correctness/concurrency; scheduled revalidation | no direct donor for atomic exact route claim/history — **REIMPLEMENT** |
| 41 | §1/§11 | §6.134 | Product/FES/Architecture discovery projection boundaries | sitemap/robots/router concepts retained as **derived reference only** |

## 3. Key Beacon stable source references

The deep source contains exact blob SHAs where reviewed. Compact JIT planning normally needs only the pinned tag plus path unless direct copying is proposed.

### Composition/content

- `lib/beacon/content/component.ex`
- `lib/beacon/content/component_attr.ex`
- `lib/beacon/content/component_slot.ex`
- `lib/beacon/content/component_slot_attr.ex`
- `lib/beacon/content/page_field.ex`
- `lib/beacon/content/page.ex`
- `lib/beacon/content/page_event.ex`
- `lib/beacon/content/page_snapshot.ex`
- `lib/beacon/content/page_variant.ex`
- `lib/beacon/lifecycle.ex`

### Routing/public publishing

- `lib/beacon/router.ex`
- `lib/beacon/router_server.ex`
- `lib/beacon/loader/routes.ex`
- `lib/beacon/web/controllers/sitemap_controller.ex`
- `lib/beacon/web/robots_txt.ex`
- `lib/beacon/web/robots/robots.txt.eex`

### Media

- `lib/beacon/media_library/asset.ex`
- `lib/beacon/media_library/asset_field.ex`
- `lib/beacon/media_library/provider.ex`
- `lib/beacon/media_library/provider/s3.ex`
- `lib/beacon/media_library/provider/s3/signed.ex`
- `lib/beacon/media_library/provider/s3/unsigned.ex`
- `lib/beacon/media_library/processors/image.ex`
- `lib/beacon/media_library/upload_metadata.ex`

### LiveAdmin

Use stable `v0.4.3` only as UI/reference evidence for generic operator table/search/filter/sort/pagination/editor interaction primitives. Do not import LiveAdmin as NewYou's operator authority.

## 4. Explicit rejection trace

The compact contract intentionally preserves the deep source's rejection posture:

| Rejected mechanism | Reason |
|---|---|
| Beacon as authoritative NewYou CMS dependency | competing C&M authority and pre-1.0 coupling |
| Beacon fork as NewYou CMS | long-term fork/runtime burden; authority mismatch |
| mutable Beacon `Page` as published authority | conflicts with exact immutable shared/locale version truth |
| Beacon `PageEvent` as full lifecycle authority | insufficient Review/Approval/Correction/Withdrawal model |
| serialised PageSnapshot as NewYou business version model | insufficient first-class governed version semantics |
| Beacon `PageVariant` as experimentation authority | Experimentation owns assignment/decision truth |
| broad CMS catch-all/editor-authored dynamic routes | can shadow application/system routing authority |
| ETS/RouterServer as route/publication correctness | process-local state cannot be business authority |
| arbitrary stored HEEx/helpers/JavaScript/styles | shadow deployment/runtime injection mechanism |
| Beacon multisite as NewYou product-space model | product spaces are not generic CMS tenants |
| LiveAdmin as second operator application | duplicates NewYou Work/Command Centre authority/UX model |

## 5. Open-gate trace

| Compact delta | Governed/open source |
|---|---|
| CM-UPD-001 | OQ-013 translation resource design |
| CM-UPD-002 | OQ-014 edge/cache design |
| CM-UPD-003 | OQ-015 search configuration |
| CM-UPD-004 | OQ-016 publication operations |
| CM-UPD-005 | OQ-020 live/video validation |
| CM-UPD-006 | OQ-021 recording/video consent/retention |
| CM-UPD-007 | OQ-024 source-content/media inventory |
| CM-UPD-008 | OQ-029 retention matrix |
| CM-UPD-009 | OQ-030/OQ-031/OQ-032 deletion/recovery/export operations |
| CM-UPD-010 | historical-address expiry/unrelated reuse policy — no current governed answer |
| CM-UPD-011 | exact correction impact/remediation policy |
| CM-UPD-012 | direct source-copy/IP/provenance acceptance |
| CM-UPD-013 | FP-001 conditional C&M dossier adjudication at governed reconciliation |

## 6. Closure trace

- Template branch: GRILL-19 — CLOSED / PASS for JIT handoff.
- Content version/translation/review/approval/publication/correction branch: GRILL-30 — CLOSED / PASS.
- Media branch: GRILL-38 — CLOSED / PASS after GRILL-36/37 refinements.
- Public addressability/discovery-projection branch: GRILL-41 — CLOSED / PASS after GRILL-40 refinement.

No further broad Beacon/C&M scenario expansion is recommended absent new evidence, changed scope or a JIT-discovered semantic contradiction.
