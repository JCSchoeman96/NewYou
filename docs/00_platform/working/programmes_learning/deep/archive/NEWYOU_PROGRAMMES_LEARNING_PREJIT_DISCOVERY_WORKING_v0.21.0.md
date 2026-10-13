# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.21.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.21.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 20 — historical reproducibility / replay-provenance semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch parent:** `8c59586e4e8edd4edda0a432f385034132ee9e6a`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.20.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose:** append one focused historical reproducibility/provenance pass while preserving Passes 1–19 and their accepted working-lock boundaries.

> This is an append-only semantic successor. It does not override Product, Architecture, Domain, Roadmap, current Open Work or approved Feature Pack/JIT authority.

> “Replay” in this pass means historical explanation/reconstruction from owner records unless explicitly stated otherwise. It does **not** authorise event sourcing, executable old-code replay, re-dispatch of side effects or a global event store.

---

# 160. Accepted working-lock status entering Pass 20

The user explicitly accepted Pass 19 and instructed the stream to continue.

Therefore Passes 1–19 are now:

`WORKING_LOCKED / NON-AUTHORITATIVE`

Pass 20 inherits without reopening the accepted ownership, versioning, delivery-provenance, correction, concurrency and exceptional-lifecycle boundaries.

---

# 161. Pass 20 — historical reproducibility / replay-provenance semantics

## 161.1 Scope hard stop

This pass asks only:

1. what minimum durable Programme/history provenance must survive to explain what a participant received and why;
2. how ProgrammeVersion, Edition/Cohort schedule, ContentVersion/locale, requirement/completion rule basis and foreign source-evidence references combine without shared-write ownership;
3. how retries, corrections, projections and current authority interact with historical explanation;
4. what lawful deletion/anonymisation may intentionally make non-reconstructible; and
5. whether a new replay/event-sourcing subsystem is justified.

It does **not** select exact Resources/columns/indexes, retention durations, event-store technology, snapshot cadence, old-code packaging, audit schema, projection framework or Analytics model.

## 161.2 Authority finding

Current Architecture and Domain Law already require immutable/versioned governed truth, exact delivered content/locale provenance, owner-specific correction/supersession and repeat-enrolment history. That is enough to define a Programme historical-explanation contract without adding a new authority layer.

The safe semantic target is:

`Programme attempt identity + exact governing versions/schedule/rule basis + minimum owner-source references + correction lineage`

not:

`replay every technical event until the current Programme state appears`.

Historical explanation and current decision authority are intentionally different operations.

---

# 162. Pass-20 evidence register extension

| ID | Evidence | Finding |
|---|---|---|
| PRG-EV-326 | Live authority routing unchanged | README and CURRENT_AUTHORITY_MANIFEST still route current authority to Product v1.3.0, Platform/Decisions v1.6.0, Architecture v1.1.1, Domain Map/Roadmap v1.2.0 and Open Work v1.2.59. |
| PRG-EV-327 | Published/activated governed versions are immutable evidence | Architecture states that material edits create new versions, corrections use explicit supersession/withdrawal, and paid/personalised/governed delivery retains exact content/locale provenance. |
| PRG-EV-328 | Content delivery provenance is exact | Content & Media Domain Law requires every delivered governed version to retain exact content/locale provenance and preserves media lineage through correction/withdrawal. |
| PRG-EV-329 | Content material edits are traceable immutable versions | DEC-135 requires every material content edit to create a new immutable and traceable content version. |
| PRG-EV-330 | Published/current/latest are distinct states | Content publication authority is versioned; a historical delivery cannot be reconstructed by resolving whatever is current/latest today. |
| PRG-EV-331 | ProgrammeVersion is durable structural meaning | Programmes owns Programme/ProgrammeVersion structure, requirement/progression/completion configuration and links an active Enrolment to its ProgrammeVersion unless governed migration/safety correction applies. |
| PRG-EV-332 | Edition schedule is Programme-owned durable truth | Programmes owns Edition/Cohort schedule and Nuwe Jy day schedule/configuration; DEC-201 requires schedule-aware, idempotent, observable and recoverable daily release. |
| PRG-EV-333 | Repeat-enrolment history is explicitly preserved | DEC-219 requires preserving repeat-enrolment history rather than flattening later attempts into the current one. |
| PRG-EV-334 | Historical Programme history is not a current-access projection | Entitlements owns current access while Programmes owns Enrolment/progression/completion history; access loss cannot make a historical attempt disappear. |
| PRG-EV-335 | Corrections do not require destructive history rewrite | DEC-241 permits additive/superseding correction for immutable records; Pass 17 already fixed owner-mediated correction and dependent-domain reconciliation. |
| PRG-EV-336 | Post-award corrected outcome remains separately governed | PRG-GAP-002 remains the existing seam when corrected source truth invalidates an already-issued Programme outcome/certificate. |
| PRG-EV-337 | Historical content correction does not erase prior valid delivery | Pass 15 established that later approved translation/content corrections preserve exact historical delivered locale/version and do not automatically reset valid progress. |
| PRG-EV-338 | Participant evidence stays with source owners | HJP owns habit/journal/progress source truth; Events owns attendance; Community owns native participation/moderation; Programmes records only its governed requirement/progression/completion consequence. |
| PRG-EV-339 | Raw journal payload is not Programme provenance | PRG-GAP-007 prohibits Programmes from copying raw journal/reflection text or attachments; minimum lawful satisfaction provenance is separately retention-gated. |
| PRG-EV-340 | Safety history and current safety authority are distinct | Safety owns eligibility/restriction/override history and current authority; Programmes consumes the approved consequence without copying raw health facts. |
| PRG-EV-341 | Communication history is not Programme source truth | Communications may retain historical message/provider evidence, but delivery/open/click observations never become Programme completion or release authority. |
| PRG-EV-342 | Audit evidence never mutates source truth | Domain Law requires sensitive domains to append minimum audit/security evidence while Audit & Evidence never mutates or owns the originating business truth. |
| PRG-EV-343 | Analytics is derived, not historical authority | Domain/Roadmap doctrine keeps Analytics as a derived consumer; historical Programme reconstruction cannot depend on mutable dashboards or aggregate projections. |
| PRG-EV-344 | Current projections may be rebuilt | Architecture separates durable authority from projections/caches; historical explanation must resolve to durable owner records rather than a cached Today view, feed, search index or dashboard. |
| PRG-EV-345 | Retention/deletion may intentionally limit reconstructibility | Privacy/Data Lifecycle law permits deletion/anonymisation/restriction under governed retention; historical reproducibility cannot resurrect data that an owning Domain was required to delete. |
| PRG-EV-346 | Full deletion ends participant access without reconstructing from retained finance | DEC-225/231 separate retained financial evidence from participant product access; retained commercial history cannot recreate deleted Programme access/private journey. |
| PRG-EV-347 | Clean LearnDash cutover avoids technical-history migration | DEC-219 requires future-edition cutover rather than technical LearnDash migration; native history starts from governed NewYou attempts, not imported LMS internals. |
| PRG-EV-348 | Pass 18 already governs replay execution safety | Duplicate/retry/reordering semantics require current precondition revalidation and repeat-safe business effect; a historical replay operation must not redispatch old side effects. |
| PRG-EV-349 | Pass 19 preserves committed schedule/lifecycle provenance | Exceptional future reschedule/cancellation policy, when authorised, must preserve prior committed schedule/lifecycle history rather than silently rewrite it. |
| PRG-EV-350 | No authority requires event sourcing | Current Product/Architecture/Domain law requires immutable/versioned provenance and durable owner truth, but does not require a platform-wide event store, executable historical replay engine or retention of every derived projection. |

---

# 163. Pass-20 semantic model

## 163.1 Historical Programme explanation

A historically explainable Programme attempt should be able to resolve, where materially applicable:

- Enrolment/attempt identity;
- Programme + exact ProgrammeVersion;
- Edition/Cohort identity;
- materially relevant schedule/effective-time context;
- exact delivered ContentVersion/locale provenance;
- governed activity/requirement/completion rule basis;
- minimum references to authoritative source evidence actually consumed;
- resulting Programme satisfaction/progression/completion/certificate state;
- explicit correction/supersession/reconciliation lineage; and
- current-vs-historical distinction.

This does **not** imply duplicating every foreign source payload inside Programmes.

## 163.2 Replay meaning

Three operations must remain distinct:

1. **Historical explanation** — read-only reconstruction of what was authoritative/observed and why.
2. **Current reconciliation** — re-read current owner truth and explicitly update current dependent consequences when required.
3. **Operational retry/recovery** — repeat an incomplete command/job safely under current preconditions.

None of these is a licence to replay arbitrary old side effects.

---

# 164. Pass-20 pressure tests

| ID | Test | Disposition | Key conclusion / route |
|---|---|---|---|
| PRG-PT-817 | Participant opens a lesson today that was delivered six months ago and content has since changed | PASS | Historical view resolves the exact delivered ContentVersion/locale provenance; current content may be shown separately as current, never substituted into history. |
| PRG-PT-818 | Historical Programme attempt stores only ContentItem and looks up current translation | REJECT | A floating current lookup cannot explain what the participant actually received. |
| PRG-PT-819 | Historical attempt stores exact ProgrammeVersion but not exact delivered content versions | REJECT / INCOMPLETE PROVENANCE | Programme structural provenance and Content delivery provenance are separate required dimensions. |
| PRG-PT-820 | Historical attempt stores exact content versions but not ProgrammeVersion | REJECT / INCOMPLETE PROVENANCE | Content alone cannot reconstruct the structural/requirement/completion meaning applied. |
| PRG-PT-821 | Participant repeats the same ProgrammeVersion in a later Edition | PASS | Separate Enrolment/Edition identities preserve each attempt and schedule context without cloning ProgrammeVersion. |
| PRG-PT-822 | Participant repeats after a new ProgrammeVersion is published | PASS | Each Enrolment remains tied to its own ProgrammeVersion; history does not resolve old attempts against the new version. |
| PRG-PT-823 | Programme title is renamed and old history displays only current title | PASS_WITH_DISPLAY_REFINEMENT | Current label may be displayed, but historical identity/version must remain resolvable; label changes cannot alter attempt meaning. |
| PRG-PT-824 | An Edition schedule is corrected before any participant commitment | PASS | Current Edition history may retain an audit/correction trail as appropriate; no artificial event-sourcing requirement is created. |
| PRG-PT-825 | A future authorised committed Edition reschedule occurs | PASS_WITH_PRG-GAP-003 DEPENDENCY | If Product policy authorises it, prior committed schedule and successor decision provenance must remain distinguishable. |
| PRG-PT-826 | A release job is replayed after crash and historical 'released at' is overwritten with replay time | REJECT | Effective business occurrence and execution/retry observation must remain distinguishable. |
| PRG-PT-827 | Duplicate release jobs create two historical releases | REJECT | Pass-18 idempotency applies; retries may add operational evidence but not duplicate the logical Programme effect. |
| PRG-PT-828 | Rebuild of Today projection changes historical release truth | REJECT | Projection rebuild may change derived display only; durable Programme release/history remains authoritative. |
| PRG-PT-829 | A replay tool re-sends old participant notifications while rebuilding history | REJECT | Historical reconstruction must be side-effect free by default; Communications sends require current authorised intent. |
| PRG-PT-830 | A historical reconstruction calls current Safety rules and replaces the historical route | REJECT | Current Safety governs current action; historical explanation preserves the route/evaluation provenance that applied then plus later corrections. |
| PRG-PT-831 | Current Safety re-evaluation blocks future work after an old historically-safe route | PASS | Historical truth and current permission are distinct dimensions. |
| PRG-PT-832 | A source health fact is corrected and prior Programme consequence is silently rewritten | REJECT | Source owner records correction/supersession; Programmes explicitly reconciles consequence while preserving prior history. |
| PRG-PT-833 | Corrected source invalidates an already-issued certificate | ROUTE PRG-GAP-002 | Historical basis and correction are preserved; certificate revocation/reissue/display remains the existing post-award policy gap. |
| PRG-PT-834 | A later Content correction invalidates an old typo-only delivery | PASS | Preserve old delivered version and correction lineage; do not reset progress when Programme meaning was not invalidated. |
| PRG-PT-835 | A later Content correction materially changes a Programme obligation | PASS_WITH_OWNER_REVIEW | Content correction cannot hide Programme semantic change; ProgrammeVersion/migration/correction rules apply. |
| PRG-PT-836 | Withdrawn required content had been validly completed before withdrawal | PASS_WITH_EXISTING_GAPS | Historical completion basis remains visible; current/future consequence depends on material invalidation and PRG-GAP-002/011 as applicable. |
| PRG-PT-837 | Raw journal text is copied into Programme history so completion can be reconstructed forever | REJECT | Programmes stores minimum governed satisfaction/provenance only; raw private journal authority remains HJP/Privacy-gated. |
| PRG-PT-838 | Journal content is lawfully deleted but minimal permitted satisfaction provenance remains | PASS / PRG-GAP-007 BOUNDARY | Historical Programme meaning may remain explainable without retaining deleted private narrative. |
| PRG-PT-839 | Journal and all permitted linked provenance must be deleted under final policy | PASS_WITH_LIMITED_RECONSTRUCTIBILITY | Reproducibility yields to lawful deletion; system must not recreate deleted private source data from caches/audit. |
| PRG-PT-840 | Event attendance source is later corrected | PASS | Events owns corrected attendance; Programmes records explicit reconciliation/superseding consequence, not destructive rewrite. |
| PRG-PT-841 | Provider attendance telemetry is the only historical source kept | REJECT | Provider observation cannot replace Events authoritative attendance history. |
| PRG-PT-842 | Facebook engagement is imported years later to 'prove' old completion | REJECT | External engagement was never default Programme completion authority; history cannot retroactively promote it. |
| PRG-PT-843 | Historical notification-delivered status is used to prove participant completion | REJECT | Communications history is operational evidence, not Programme satisfaction evidence. |
| PRG-PT-844 | Historical entitlement was active at delivery but is revoked today | PASS | Historical access/delivery may remain true while current protected access fails. |
| PRG-PT-845 | Current entitlement cache says active and is used to infer historical access | REJECT | Current projection is neither historical entitlement evidence nor Programme history authority. |
| PRG-PT-846 | Participant account email changes and old communication history is rebound to new address | REJECT | Historical destination/provenance remains what was actually used; current identity/contact governs future actions. |
| PRG-PT-847 | Participant language preference changes and old delivered content is relabelled to new language | REJECT | Historical locale/version stays exact; future delivery may follow current eligible preference. |
| PRG-PT-848 | Programme rule wording changes without a new ProgrammeVersion and old completion is recalculated | REJECT | Material requirement/progression/completion semantics require governed versioning/correction, not mutable rule lookup. |
| PRG-PT-849 | Completion is recalculated historically using today's threshold | REJECT | Historical explanation uses the governed threshold/rule basis that applied to that attempt; current rule is a separate fact. |
| PRG-PT-850 | Operator asks 'why was this participant completed?' | PASS | Answer is reconstructed from ProgrammeVersion/rule basis plus minimum authoritative evidence references and explicit corrections, not from an admin note alone. |
| PRG-PT-851 | Operator edits an audit log entry to make history match current state | REJECT | Audit evidence is immutable/corrected additively as governed and does not own source truth. |
| PRG-PT-852 | Audit entry exists but source owner record is missing | INSUFFICIENT AS BUSINESS AUTHORITY | Audit may prove an action observation; it cannot silently become replacement Programme/Content/HJP/Event authority. |
| PRG-PT-853 | Analytics dashboard snapshot disagrees with owner history | OWNER HISTORY WINS | Analytics/projection is derived and must be rebuilt/reconciled. |
| PRG-PT-854 | Analytics is rebuilt after a correction and old dashboard numbers change | PASS | Derived metrics may change under defined measurement rules; Programme historical owner truth remains unchanged. Exact analytics semantics stay Pass 21. |
| PRG-PT-855 | System stores every Today-page render forever to guarantee reproducibility | REJECT / DEFER_YAGNI | Historical business explanation requires durable owner provenance, not retention of every derived screen render. |
| PRG-PT-856 | System stores every PubSub message forever as canonical history | REJECT / DEFER_YAGNI | PubSub is freshness/observation, not business authority. |
| PRG-PT-857 | System introduces a global append-only event store as the canonical source for all Domains | REJECT / DEFER_YAGNI | Current law already assigns durable authority to owner Domains; no evidence justifies a competing event-store authority. |
| PRG-PT-858 | System requires executable copies of every historical code release to reproduce Programme outcome | REJECT AS GENERIC REQUIREMENT | Preserve governed versioned business inputs/rules/outcomes/provenance; exact executable archival requirements are not established by current law. |
| PRG-PT-859 | System re-runs old business logic against current database to 'replay history' | REJECT | Current mutable state would contaminate historical interpretation and could trigger side effects. |
| PRG-PT-860 | Side-effect-free historical explanation uses immutable owner versions and recorded source references | PASS | This is the preferred semantic meaning of historical reproducibility at Pre-JIT scope. |
| PRG-PT-861 | A correction records only the new truth and deletes the superseded historical state | REJECT WHERE RECORD IS GOVERNED IMMUTABLE/SUPERSEDING | DEC-241 and owner lifecycle semantics preserve correction lineage where required. |
| PRG-PT-862 | A mutable participant preference is snapshotted on every activity even when it did not affect the action | REJECT / OVER-CAPTURE | Capture only provenance that materially determined governed delivery/decision; avoid speculative sensitive duplication. |
| PRG-PT-863 | Timezone used for a scheduled release is not retained and later timezone changes make the effective release instant ambiguous | PASS_WITH_JIT REFINEMENT | Where timezone materially determines schedule semantics, historical schedule/effective-time provenance must remain explainable; exact representation stays JIT. |
| PRG-PT-864 | A legacy LearnDash completion record is imported as native NewYou Programme history | REJECT | DEC-207/219 require clean future-edition cutover, not technical migration of LearnDash domain truth. |
| PRG-PT-865 | A native NewYou participant's second enrolment overwrites the first because ProgrammeVersion is identical | REJECT | Repeat-enrolment history is explicit Product Law; attempts remain distinct. |
| PRG-PT-866 | A historical reconstruction resurrects lawfully deleted health/journal payload from backups or analytics extracts | REJECT | Privacy/deletion/retention authority outranks reproducibility; derived/cached/external copies must not become a recovery path. |

---

# 165. Pass-20 gap adjudication

No new gap is justified.

- `PRG-GAP-002` remains the post-award corrected-outcome/certificate consequence seam.
- `PRG-GAP-003 / PRG-UPD-001` remains the exceptional committed Edition lifecycle Product seam; any later authorised transition must preserve predecessor provenance.
- `PRG-GAP-005` remains semantically resolved for Content/translation binding, with exact representation mechanics deferred to OQ-013/OQ-016/JIT.
- `PRG-GAP-007` remains the minimum-lawful journal-derived satisfaction provenance / deletion-retention seam.
- `PRG-GAP-009` remains semantically resolved for owner-mediated correction; Pass 20 consumes its correction lineage.
- `PRG-GAP-011` remains the required-content-withdrawal/no-replacement consequence seam.

Historical reproducibility does not create a second copy of those gaps and does not turn Audit/Analytics into Programme authority.

---

# 166. Pass-20 refinements

| ID | Refinement | Effect |
|---|---|---|
| PRG-REF-267 | Define historical reproducibility as owner-record explanation, not executable event replay. | Keeps the pass aligned with current authority and avoids event-sourcing overreach. |
| PRG-REF-268 | Preserve ProgrammeVersion identity/basis for every Enrolment attempt. | Prevents current Programme semantics from rewriting historical attempts. |
| PRG-REF-269 | Preserve Edition/Cohort and materially relevant schedule/effective-time provenance. | Allows explanation of what was available/released when without storing every scheduler execution. |
| PRG-REF-270 | Preserve exact delivered ContentVersion/locale provenance separately from ProgrammeVersion. | Maintains Content/Programme ownership separation. |
| PRG-REF-271 | Preserve the governed requirement/completion rule basis used for an outcome. | Prevents historical recalculation against today's thresholds/rules. |
| PRG-REF-272 | Reference minimum source-owner evidence rather than copy foreign raw payloads. | Supports explanation while preserving Domain ownership/privacy. |
| PRG-REF-273 | Distinguish effective business time from worker/job/provider observation time. | Retries/replays must not move the historical occurrence. |
| PRG-REF-274 | Distinguish historical truth from current permission/current authority. | Old valid delivery or route may remain historical while current access/Safety blocks future action. |
| PRG-REF-275 | Treat correction/supersession as new linked truth, not destructive historical rewrite. | Aligns with DEC-241 and immutable-version doctrine. |
| PRG-REF-276 | Keep post-award invalidation consequences under PRG-GAP-002. | Pass 20 preserves provenance but does not invent certificate revocation/reissue policy. |
| PRG-REF-277 | Keep private-journal retention/reconstructibility under PRG-GAP-007 and Privacy/HJP gates. | Reproducibility must not expand sensitive retention. |
| PRG-REF-278 | Keep withdrawn-required-content consequences under PRG-GAP-011. | Historical provenance does not decide replacement/waiver/migration consequences. |
| PRG-REF-279 | Keep exceptional Edition lifecycle history compatible with PRG-GAP-003/PRG-UPD-001. | Any later reschedule/cancellation policy must preserve predecessor schedule/lifecycle provenance. |
| PRG-REF-280 | Audit evidence supplements owner records but never substitutes for missing owner authority. | Prevents a competing audit source of truth. |
| PRG-REF-281 | Analytics and operational projections are rebuildable consumers, not historical authority. | Prepares a clean handoff to Pass 21. |
| PRG-REF-282 | Historical reconstruction is side-effect free by default. | Prevents replay from sending messages, issuing access, changing progress or re-running provider calls. |
| PRG-REF-283 | Current-state reconciliation and historical explanation are separate operations. | Reconciliation may change current consequences; historical explanation preserves what occurred and subsequent corrections. |
| PRG-REF-284 | Do not require retention of every UI render, PubSub message, job attempt or provider callback. | Keep only owner truth and evidence required by business/operational policy. |
| PRG-REF-285 | Do not require a global event store or platform-wide event sourcing. | PostgreSQL owner records plus governed versions/provenance remain the default. |
| PRG-REF-286 | Do not require archived executable code for every historical Programme decision absent explicit authority. | Versioned business basis and outcomes are the current requirement. |
| PRG-REF-287 | Lawful deletion/anonymisation may intentionally reduce historical reconstructibility. | Never resurrect deleted payload from analytics, cache, backup or audit. |
| PRG-REF-288 | Repeat enrolments are distinct historical attempts even when ProgrammeVersion is identical. | Preserves DEC-219 repeat-enrolment history. |

---

# 167. Pass-20 anti-replay-engine / YAGNI outcome

Rejected / deferred:

- global event-sourcing architecture for Programmes;
- platform-wide canonical event store;
- replaying every Domain event to reconstruct Programme state;
- retaining every Today-page render;
- retaining every LiveView/PubSub message as business history;
- retaining every worker execution forever;
- retaining every provider callback as canonical Programme truth;
- full raw journal copies inside Programmes for historical proof;
- raw health snapshots inside Programmes for replay;
- current-content lookup as historical delivery reconstruction;
- current-rule lookup as historical completion reconstruction;
- automatic historical recomputation whenever thresholds change;
- executable archive of every old application release as a generic requirement;
- re-running old side effects during historical replay;
- Analytics warehouse as Programme history authority;
- Audit log as replacement business source of truth;
- LearnDash completion-history importer;
- generic replay debugger as a Product capability;
- historical reconstruction that bypasses deletion/retention rules;
- new Historical Replay / Provenance Domain;

The simplest correct model remains durable PostgreSQL owner truth plus immutable/versioned provenance and explicit correction/reconciliation.

---

# 168. Pass-20 disposition

**Discovery outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Passes 1–19 remain accepted/working-locked and Pass 20 does not reopen them.
2. Historical reproducibility means being able to explain a Programme attempt/outcome from durable owner records and exact governed provenance; it does not require executable event replay.
3. Every Enrolment history must remain tied to the ProgrammeVersion whose structural/requirement/completion meaning applied to that attempt.
4. Edition/Cohort identity and materially relevant schedule/effective-time provenance remain distinct from ProgrammeVersion and must be sufficient to explain scheduled availability/release context.
5. Exact delivered ContentVersion/locale provenance remains Content-owned and is required separately from Programme structural provenance.
6. A floating lookup of current/latest Programme rules or Content cannot reconstruct historical delivery or completion meaning.
7. Programme outcome explanation preserves the governed rule/threshold basis that applied at the time; later rule changes do not silently recalculate history.
8. Participant source evidence remains owned by HJP, Events, Community, Safety and other source Domains; Programmes stores/references only the minimum governed provenance necessary for its consequence.
9. Programmes must not copy raw journal narrative, health payloads or other foreign sensitive source truth merely to make history easier to reconstruct.
10. Historical business occurrence/effective time is distinct from retry/job/provider observation time.
11. Retry/replay may add operational evidence but cannot create a second logical historical Programme effect.
12. Historical reconstruction is side-effect free by default and cannot resend communications, regrant access, call providers or mutate Programme state.
13. Current authority and historical truth are distinct: a delivery/access/Safety route may have been valid then while current policy blocks future action now.
14. Corrections and supersessions remain explicit linked history where governed; they do not destructively rewrite the earlier state.
15. PRG-GAP-002 remains the post-award consequence seam when corrected truth invalidates a certificate/completion outcome.
16. PRG-GAP-007 remains the retention/deletion seam for minimum journal-derived satisfaction provenance; Pass 20 does not expand raw-data retention.
17. PRG-GAP-011 remains the required-content unavailability/replacement consequence seam; historical provenance alone does not decide waiver/substitute/migration.
18. PRG-GAP-003/PRG-UPD-001 remain compatible with Pass 20: any later authorised committed Edition reschedule/cancellation must preserve predecessor schedule/lifecycle provenance.
19. Audit & Evidence may prove actor/action/context evidence but never becomes replacement Programme, Content, HJP, Events or Safety authority.
20. Analytics, dashboards, caches, search indexes, Today views and other projections are derived/rebuildable and cannot become historical Programme authority.
21. Repeat Enrolments remain distinct attempts even when they share the same ProgrammeVersion.
22. DEC-219 clean LearnDash cutover means legacy LMS internal completion history is not imported as native NewYou Programme truth.
23. Lawful privacy deletion/anonymisation/restriction can intentionally reduce reconstructibility; the platform must not resurrect deleted payloads from caches, analytics, audit or backups.
24. Historical reproducibility should retain only provenance that materially determined a governed delivery/decision, avoiding speculative sensitive snapshots.
25. No current authority requires retaining every UI render, PubSub message, worker execution or provider callback forever.
26. No current authority requires a global event store, event-sourcing architecture, generic replay engine or Historical Replay Domain.
27. No current authority requires archived executable copies of every application version merely to explain Programme history.
28. Exact Ash resources, provenance columns/references, immutable indexes, retention representation and projection-rebuild mechanics remain JIT/proof detail.
29. No new Product, Architecture, Domain, PRG-GAP or PRG-UPD is justified by Pass 20.
30. Broad discovery remains unfrozen; analytics / measurement semantics is the next isolated pass.

**Pass hard stop:** Pass 21 — analytics / measurement semantics — has not started.

**Broad discovery remains unfrozen.**
