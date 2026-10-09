# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.3.0.md

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY EVIDENCE
- **Document version:** v0.3.0
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.2.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Predecessor branch head:** `38cc76b1ba24b5eee2c5319c0a9ead4a560d0f82`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap amendment:** NONE
- **Semantic rule:** v0.1.0 and v0.2.0 remain preserved unchanged. This file is an append-only substantive continuation. Prior semantic conclusions are not silently rewritten.
- **Pass scope:** recording intent and raw capture boundary only.

---

# 19. Pass C scope correction and objective

The predecessor's §18 described a broad future Batch C covering recording, consent, sensitive capture, replay publication, correction/withdrawal, deletion/retention and safety correction. That broad **sequencing statement is superseded** by the approved focused-pass method; no v0.2.0 semantic finding is superseded.

This pass asks only:

> What must NewYou distinguish between an occurrence's governed recording intent, external-provider capture evidence, and a provider capture that is deliberately adopted into governed NewYou media handling?

The pass is deliberately limited to:

- recording intended versus not intended;
- provider capture starts successfully or fails to start;
- capture starts late or ends early;
- provider restart/replacement yields multiple raw capture segments;
- raw capture is corrupted, incomplete or technically unusable;
- provider creates capture despite NewYou not intending recording;
- provider capture-finalisation evidence is duplicated, delayed, reordered or ambiguous;
- the authority handoff from provider artifact/evidence to governed NewYou media identity.

This pass deliberately does **not** adjudicate:

- recording notice presentation or acknowledgement mechanics;
- participant/speaker consent sufficiency;
- late-join consent;
- guest/speaker/staff distinctions;
- sensitive audience-material remedies;
- consent withdrawal after capture;
- one participant withdrawing from a multi-person recording;
- retention periods;
- Full Deletion or external-processor deletion;
- replay entitlement;
- replay publication, expiry, correction, replacement or withdrawal;
- promotional clip approval;
- safety-content withdrawal/remediation;
- participant communications about failed/unavailable recording;
- exact Restream or Cloudflare API behaviour.

Those remain separate later passes or named open gates.

No `LIVE-EV-*` evidence item is added in this pass because no external provider research is performed.

---

# 20. Focused authority extraction

## 20.1 Product Law

Current Product Law §21G.15 requires a recorded session to have explicit recording notice, participant/speaker consent rules, attendee privacy controls, sensitive audience-material handling, governed editing, replay entitlement, replay expiry where applicable, content/version history, correction/withdrawal and separate promotional-clip approval.

The same section states that a recording is not automatically public merely because the live session occurred.

This pass uses that law only to establish a **fail-closed boundary**: provider capture existence cannot itself authorise replay/public use. It does not attempt to decide the deferred notice/consent/remediation rules.

Current Product Law §21E.15 also treats media as governed independently and requires protected recordings to use entitlement-checked access with bounded delivery capability. This reinforces that a provider-created object is not self-authorising platform media.

## 20.2 Decision Law

`DEC-188 — Recording governance` is LOCKED and requires explicit recording notice, participant controls, governed editing, replay entitlements, versioning, correction and clip approval.

`DEC-190 — Platform live-video path` keeps the preferred provider chain directional while leaving architecture/provider detail pending. A recorded provider object therefore cannot be treated as settled platform behaviour merely because the preferred chain exists.

## 20.3 Domain Law

Events & Live owns:

- live-session/event definitions, versions and occurrences;
- session/event recording notice/association.

Events & Live explicitly does **not** own replay/media publication or provider stream-delivery state as business truth.

Content & Media owns:

- governed editorial media identity;
- rights;
- derivatives;
- publication state;
- media bytes within the governed platform media boundary.

The existing ownership boundary is therefore sufficient for this pass: **recording intent/occurrence association remains Events & Live context; governed platform media remains Content & Media truth.** No new Domain is justified.

## 20.4 Architecture Law

Current Architecture §10.3 requires:

- platform-owned media identity independent of provider/object IDs;
- lineage across masters, recordings and derivatives;
- provider capture not to equal replay publication;
- full recording, approved replay and promotional clips to remain separate governed publication/rights states;
- external production/streaming/transcoding to remain behind replaceable adapters;
- provider callbacks/status to remain evidence rather than authority.

Generic provider-ingress law additionally requires authenticity verification, durable receipt/evidence, idempotent handling and reconciliation under duplicate/reordered callbacks. The exact capture API is still provider empirical evidence, not Architecture truth.

## 20.5 Open gates

The focused pass inherits two still-open blockers:

- `OQ-020` — Restream/Cloudflare live validation;
- `OQ-021` — recording/video consent/retention.

`OQ-020` must later establish actual capture/start/stop/finalisation/segment/provider-replacement behaviour.

`OQ-021` blocks any attempt to turn accidental or consent-ambiguous capture into a lawful retention/publication rule.

---

# 21. Focused semantic model

This section is a semantic decomposition, not a Resource/schema proposal.

## 21.1 Recording intent is not capture existence

A NewYou occurrence may have a governed recording intention/association. That intention is part of the occurrence's governed context and is not created by a provider starting to record.

Therefore:

- `recording intended` does not prove that bytes were captured;
- `provider captured bytes` does not prove that NewYou intended or lawfully authorised recording;
- changing a provider toggle does not by itself change NewYou recording policy;
- recording intent must remain historically explainable independently of provider success/failure.

This pass does not define the exact occurrence-policy representation or whether recording intent may change after participants begin joining; the latter is routed to the next notice/consent-focused pass.

## 21.2 Provider capture is external artifact/evidence

A provider may expose one or more recording objects, files, processing jobs or status events. Those identifiers/statuses are external evidence and operational artifacts.

They are not automatically:

- a NewYou media identity;
- a complete recording;
- an approved replay;
- an entitlement;
- proof that notice/consent requirements were satisfied;
- proof that the session itself completed successfully.

Provider capture and occurrence execution are related but independent. A session can complete with no recording. A provider can create a recording for an occurrence that NewYou later treats as cancelled, failed, terminated or not intended for recording.

## 21.3 Governed media adoption is a deliberate boundary

When NewYou deliberately accepts a provider capture into governed media handling, Content & Media must own a **platform media identity independent of the provider object ID**, with provenance/lineage back to the provider capture and occurrence association.

This does not imply a particular Resource, action, table, object-storage copy or import workflow.

The semantic invariant is:

```text
provider artifact/evidence
        !=
NewYou governed media identity
        !=
approved replay publication
```

The transition from external capture evidence to governed media handling must be explicit enough that retries, duplicated provider objects, provider replacement and later corrections cannot accidentally manufacture multiple canonical recordings or publication authority.

## 21.4 Capture completeness and usability are not binary existence

A provider recording can exist while being:

- late-starting;
- early-ending;
- split into multiple segments;
- missing audio;
- missing video;
- showing the wrong source/screen;
- corrupt;
- inaccessible while processing;
- permanently unretrievable.

NewYou must not collapse `provider object exists` into `usable full recording exists`.

Exact quality-review workflow, technical metadata and acceptance thresholds remain downstream Content & Media JIT/editorial concerns unless a later Product promise makes a specific threshold consequential.

## 21.5 Cardinality must remain open

This pass rejects an implicit one-occurrence-to-one-provider-recording assumption.

A single NewYou occurrence may lawfully have:

- zero provider captures;
- one provider capture;
- several capture segments from one provider;
- captures from old and replacement provider resources;
- redundant/duplicate provider artifacts that should not become multiple platform-authoritative recordings.

Conversely, NewYou must not automatically concatenate provider segments into one canonical master merely because they belong to one occurrence. Any composition/edit is governed Content & Media work with retained lineage.

---

# 22. Pressure tests — focused recording-intent/raw-capture pass

## LIVE-PT-031 — Recording intended and one complete provider capture succeeds

**Scenario class**

Recording intent / ordinary raw-capture path.

**Why it matters**

The normal path must prove that even a successful provider recording does not erase the provider/media ownership boundary.

**Authority**

Product §21G.15; `DEC-188`; Domain Law Events recording association versus Content & Media media identity; Architecture §10.3 provider capture boundary.

**Owning Domains**

Events & Live for occurrence recording intent/association; Content & Media once capture is deliberately adopted into governed media handling.

**Preconditions**

Occurrence exists; current governed policy says recording is intended; the provider path is configured to capture; later notice/consent requirements are assumed satisfied only for purposes of this narrow happy-path test and are not adjudicated here.

**Timeline**

Recording intent established → live occurrence starts → provider capture starts → occurrence completes → provider reports/finalises one recording object → NewYou receives/reconciles provider evidence → capture is deliberately adopted into governed media handling → platform media identity/provenance exists → no replay publication is implied.

**Expected invariants**

- occurrence identity remains Events & Live truth;
- recording intent predates and is independent of provider capture success;
- provider object ID is provenance/evidence, not platform media identity;
- governed media identity is Content & Media truth;
- occurrence association remains historically traceable;
- capture adoption does not publish replay;
- no entitlement is created by capture existence;
- duplicate provider evidence cannot duplicate canonical adoption accidentally.

**Questions**

What exact platform action constitutes deliberate media adoption? Which provider evidence proves a capture is stable enough to adopt? Must NewYou copy bytes before establishing media identity, or may identity precede durable binary ingestion? These are JIT/provider questions, not Product ownership questions.

**Adversarial variants**

Provider sends completion twice; provider changes its object identifier after processing; operator retries adoption; object is initially processing and later ready.

**Analysis**

The ownership semantics are already sufficient. The remaining uncertainty is implementation-grade handoff and provider behaviour, not a missing Product owner.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT + PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

OQ-020 provider finalisation/idempotency evidence; Content & Media JIT contract for explicit media adoption/provenance.

---

## LIVE-PT-032 — Recording intended but provider capture never starts

**Scenario class**

Capture failure / missing artifact.

**Why it matters**

A failed recording must not falsify occurrence history or manufacture a placeholder replay/media record that appears successful.

**Authority**

Architecture provider failure cannot rewrite platform truth; Roadmap FP-007 requires provider/delivery failure to be visible without becoming business authority.

**Owning Domains**

Events & Live retains occurrence/recording-intent context; Content & Media owns no successful media merely because capture was intended; operational evidence remains non-authoritative.

**Preconditions**

Recording was intended; live session executes; provider capture fails to start or no capture artifact is produced.

**Timeline**

Intent recorded → live starts → capture command/configuration attempted → provider fails/silently does nothing → occurrence continues/completes → later reconciliation confirms no usable capture.

**Expected invariants**

- occurrence can remain successfully executed even though recording failed;
- recording intent remains historically true;
- no governed recording/media identity is fabricated solely from intent;
- no replay publication is fabricated;
- operator-visible capture failure may be retained as evidence/status without becoming occurrence truth;
- later provider evidence may reconcile the capture outcome idempotently.

**Questions**

Does Content & Media need a durable failed-import/capture-candidate concept, or is that integration evidence outside the media lifecycle? What evidence is sufficient to conclude `no capture` versus `still processing/unknown`? Exact answer depends on provider behaviour.

**Adversarial variants**

Provider API says recording enabled but no object appears; object appears hours later; provider dashboard and callback disagree; recording starts only after a manual retry.

**Analysis**

The critical semantic point is that **intent, live execution and capture outcome are independent dimensions**. The exact failure/reconciliation representation belongs to JIT after OQ-020 evidence.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`PROVIDER_EMPIRICAL + JIT`

**UPD if any**

None.

**Evidence needed**

OQ-020 evidence for provider recording enablement, failure signalling, delayed artifact creation and reconciliation.

---

## LIVE-PT-033 — Provider capture starts late or stops early

**Scenario class**

Partial capture / completeness.

**Why it matters**

The platform must not label a partial artifact as the full session merely because a provider says `recording completed`.

**Authority**

Architecture requires provider evidence to remain non-authoritative and media lineage to be platform-owned; Product requires governed editing/version history before replay publication.

**Owning Domains**

Events & Live for occurrence actual execution context; Content & Media for adopted capture/media lineage and later editorial disposition.

**Preconditions**

Recording intended; occurrence has an actual live interval; provider captures only part of it.

**Timeline**

Live begins at T1 → provider recording begins T2 > T1, or recording ends T3 < actual live end T4 → provider finalises artifact → NewYou reconciles known capture interval/defect → optional later governed edit/publication remains out of scope.

**Expected invariants**

- occurrence actual start/end are not rewritten to match captured interval;
- provider `completed` status does not mean complete semantic coverage;
- adopted media preserves enough provenance to explain known partiality;
- partial capture is not silently promoted as a complete replay;
- later editorial remediation cannot erase original lineage.

**Questions**

Which completeness facts are provider-derived versus operator/editor-confirmed? Does Product ever promise a `full recording`, or is completeness only editorial metadata? What capture timing precision is available from the provider?

**Adversarial variants**

First ten minutes missing; final Q&A missing; provider timestamp clock skew; stream started early with holding screen but recording began only when presenter spoke.

**Analysis**

Current law is sufficient to forbid the dangerous collapse. Exact completeness metadata/quality thresholds can remain JIT/editorial unless later Product promises make them upstream semantics.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT + PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

Provider capture timestamps/segment metadata; Content & Media JIT quality/provenance contract.

---

## LIVE-PT-034 — Provider restart creates multiple raw capture segments

**Scenario class**

Segmented capture / lineage.

**Why it matters**

A transient provider/production restart must not force one NewYou occurrence into multiple business occurrences or create an accidental one-recording-per-occurrence assumption.

**Authority**

`LIVE-UPD-001` working direction keeps occurrence identity independent of provider resource; Architecture requires platform media identity and lineage independent of provider object IDs.

**Owning Domains**

Events & Live for one occurrence; Content & Media for each adopted media artifact/lineage and any later governed composition.

**Preconditions**

One occurrence; recording intended; provider/production restarts during live execution.

**Timeline**

Occurrence starts → capture segment A created → provider/production restart → capture segment B created → occurrence completes → A/B provider artifacts reconcile → NewYou may adopt zero, one or both into governed media handling → later editing/composition is separate.

**Expected invariants**

- multiple provider artifacts do not create multiple NewYou occurrences;
- one occurrence does not require exactly one governed raw media artifact;
- segment ordering/coverage is preserved as provenance rather than guessed from callback order;
- retries cannot duplicate adopted segments;
- concatenation/composition is governed editing, not automatic ingestion behaviour;
- replay publication remains separate.

**Questions**

How does the selected provider identify recording segments and their temporal ordering? Can a provider replace a segment object after processing? Does NewYou need an explicit recording-set/group concept, or can ordinary media relationships express the lineage? Do not invent a new Resource before JIT proves need.

**Adversarial variants**

A and B overlap; a restart produces A/B/C with gaps; provider reuses names; callbacks arrive B then A; A later becomes unavailable.

**Analysis**

The domain/architecture model supports one occurrence to multiple raw captures. The remaining shape is JIT/provider work. A dedicated `RecordingSet`-style Resource is not justified by this evidence alone.

**Semantic disposition**

`PASS`

**Proof route**

`JIT + PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

OQ-020 segment/finalisation behaviour and executable idempotency/reordering tests.

---

## LIVE-PT-035 — Provider produces a corrupt or technically unusable capture

**Scenario class**

Raw-media quality failure.

**Why it matters**

Object existence must not be confused with a usable recording or approved replay.

**Authority**

Content & Media owns governed media identity/rights/derivatives/publication; Product requires governed editing/versioning; provider state remains evidence only.

**Owning Domains**

Content & Media once artifact is deliberately adopted; Events & Live remains occurrence/association owner.

**Preconditions**

Recording intended; provider produces an artifact that is corrupt, has no audio, wrong source, severe truncation or another technical defect.

**Timeline**

Provider finalises artifact → NewYou receives evidence/object → defect discovered automatically or by authorised review → artifact remains historical/provenance evidence as appropriate → no replay publication follows merely from capture existence.

**Expected invariants**

- provider `ready/completed` cannot equal editorial/technical acceptance;
- unusable capture does not become approved replay;
- original provider/artifact lineage is not silently rewritten if a repaired/replacement media item is later created;
- occurrence/attendance/entitlement truth remains unaffected by media-quality failure;
- exact technical rejection thresholds remain Content/JIT concerns unless Product specifies a promise.

**Questions**

Should unusable bytes be adopted at all, or only recorded as provider evidence until technical acceptance? Which checks belong automatic ingestion versus human editorial review? What quality fields must survive into later correction/replacement provenance?

**Adversarial variants**

Audio missing only in first segment; wrong screen captured but correct audio exists; provider later regenerates a fixed file under same provider ID; file checksum changes after provider post-processing.

**Analysis**

The semantic rule is clear: capture existence and provider readiness are insufficient for governed replay. Exact acceptance mechanics remain JIT/editorial and may depend on provider evidence.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT + PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

Provider post-processing/mutability facts; Content & Media technical acceptance/provenance contract.

---

## LIVE-PT-036 — Provider records despite NewYou recording intent being false

**Scenario class**

Accidental/unauthorised capture boundary.

**Why it matters**

External provider behaviour must not manufacture lawful recording authority. This is the strongest negative case for separating intent from capture.

**Authority**

Product §21G.15 requires recording notice/consent/privacy controls; Events & Live owns recording notice/association; provider state is not business authority; Privacy & Consent owns purpose permission and deletion/retention orchestration.

**Owning Domains**

Events & Live for occurrence recording-intent/association truth; Privacy & Consent for later permission/remediation/retention/deletion adjudication; Content & Media only for any governed media handling that is lawfully permitted after those rules are resolved.

**Preconditions**

NewYou occurrence policy says recording is not intended, but provider auto-record/default/operator error creates capture anyway.

**Timeline**

Occurrence starts with no recording intent → provider begins capture unexpectedly → artifact exists → NewYou learns of artifact during or after session → artifact is **not** treated as authorised replay/media publication → downstream retention/deletion/remediation route is deferred to OQ-021/later privacy pass.

**Expected invariants**

- provider capture cannot retroactively create recording intent;
- artifact cannot be published merely because it exists;
- accidental capture cannot be relabelled as an ordinary successful recording to simplify operations;
- occurrence history must remain truthful about intended policy and discovered provider behaviour;
- any handling of the accidental bytes must fail closed pending privacy/retention authority;
- Audit evidence, if required, must not become the media or privacy authority.

**Questions**

Must accidental bytes be immediately deleted, temporarily restricted for incident handling, or retained under a lawful basis? Who may inspect them? What participant notification/remediation is required? These are intentionally **not answered here**.

**Adversarial variants**

Provider account has auto-record enabled globally; host clicks record accidentally; recording begins for only 30 seconds; provider creates hidden backup/cloud copy; operator discovers it days later.

**Analysis**

This scenario proves the separation, but its byte-handling remedy is blocked by the recording/privacy gate. The pass must stop rather than invent retention or deletion rules.

**Semantic disposition**

`BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE`

**Proof route**

`OQ-021 + LATER_FOCUSED_PRIVACY_PASS`

**UPD if any**

None in this pass; this refines the scope of existing `LIVE-GAP-003`.

**Evidence needed**

Recording notice/consent/retention/deletion authority plus provider evidence about auto-record/defaults and processor deletion behaviour in the later provider/privacy passes.

---

## LIVE-PT-037 — Capture-finalisation callbacks are duplicated, delayed or reordered

**Scenario class**

Provider evidence ordering / idempotency.

**Why it matters**

Provider event order must not manufacture duplicate media identities or premature finality.

**Authority**

Architecture provider-ingress doctrine: authenticate, durably receive evidence, commit/ack safely, process idempotently and reconcile duplicate/reordered evidence; provider status is not authority.

**Owning Domains**

No new owner. Content & Media owns any governed media identity; integration/provider evidence remains supporting evidence; Events retains occurrence association context.

**Preconditions**

A provider capture exists or is processing; provider emits lifecycle/status callbacks or NewYou polls provider state.

**Timeline**

Example: `recording_started` → `recording_completed` callback arrives → duplicate `completed` arrives → older `processing` callback arrives late → provider API later exposes final stable object.

**Expected invariants**

- callback arrival order does not define media lifecycle authority;
- repeated evidence is idempotent;
- stale/reordered evidence cannot regress a platform-owned media conclusion blindly;
- ambiguous finalisation remains unresolved/reconciling rather than fabricated success;
- one provider artifact must not create duplicate platform media identities through retries;
- an irreversible or publication consequence waits for the governed platform decision, not a callback alone.

**Questions**

Which events does the selected provider actually send? Are object IDs stable across processing? Can callbacks omit events? Is polling required for reconciliation? These are empirical questions.

**Adversarial variants**

Completion arrives before start; duplicate objects have same content; object ID changes; callback received after provider deletion; network retry repeats webhook delivery for hours.

**Analysis**

Architecture already supplies the correctness rule. The remaining blocker is provider-specific evidence mapping and executable proof.

**Semantic disposition**

`PASS`

**Proof route**

`PROVIDER_EMPIRICAL + CONTROLLED_LIVE_PROOF`

**UPD if any**

None.

**Evidence needed**

OQ-020 first-party provider documentation plus controlled duplicate/reorder/finalisation tests.

---

## LIVE-PT-038 — Provider resource replacement yields recordings from both old and new resources

**Scenario class**

Provider replacement / multi-source capture lineage.

**Why it matters**

`LIVE-PT-018` established that provider-resource replacement need not replace the NewYou occurrence. This pass must prove that recording lineage remains correct when both provider resources create artifacts.

**Authority**

`LIVE-UPD-001` working direction; Architecture platform-owned media identity and provider independence; Domain ownership boundary between Events and Content & Media.

**Owning Domains**

Events & Live for one NewYou occurrence/current provider association history; Content & Media for adopted raw captures and any later governed edit/composition.

**Preconditions**

One occurrence; recording intended; provider resource A fails or is replaced by B while live; A and B both produce capture artifacts.

**Timeline**

Occurrence bound to A → A records segment → operator switches to B → B records continuation/overlap → provider evidence from both arrives → occurrence remains one unless Product meaning actually changed → each adopted capture retains source provenance → later composition remains governed editing.

**Expected invariants**

- provider replacement does not merge or overwrite capture provenance;
- A/B recording objects cannot become occurrence identities;
- duplicate/overlapping content is not silently de-duplicated as business truth;
- each adopted capture can be traced to provider/source/time evidence;
- later edited master/replay remains a separate governed media/version outcome;
- stale provider A cannot become current join authority merely because its recording object still exists.

**Questions**

How much source-binding history must Events expose to Content for provenance? Is exact provider resource association needed per raw capture? Can provider B ingest A's stream or copy recording internally, creating ambiguous lineage?

**Adversarial variants**

A and B overlap for five minutes; A continues recording after participants move; B fails but A recording remains complete; provider migration changes object IDs while copying bytes.

**Analysis**

No new Product rule is required. JIT must preserve cross-provider provenance without creating shared-write ownership or assuming provider identity is stable.

**Semantic disposition**

`PASS_WITH_REFINEMENT`

**Proof route**

`JIT + PROVIDER_EMPIRICAL`

**UPD if any**

None.

**Evidence needed**

OQ-020 provider replacement/capture behaviour plus Content & Media lineage contract.

---

## LIVE-PT-039 — Recording intent changes immediately before or during live execution

**Scenario class**

Recording-policy version / boundary to notice and consent.

**Why it matters**

The pass must identify where recording intent itself stops being a simple operational toggle and becomes a participant-facing privacy decision.

**Authority**

Events & Live owns recording notice/association; Product §21G.15 requires explicit notice and participant/speaker consent rules; Privacy & Consent owns purpose permission.

**Owning Domains**

Events & Live for occurrence policy/association; Privacy & Consent for permission semantics; provider remains delivery/capture machinery.

**Preconditions**

Occurrence was configured as recording intended or not intended; authorised operator seeks to change that intention near or after live start.

**Timeline**

A. `recording intended` is changed to `not intended` before capture. B. `not intended` is changed to `intended` after some participants have joined. C. recording starts and operator later turns it off.

**Expected invariants**

- provider toggle state cannot be the sole authority for NewYou recording intent;
- historical policy/version must remain explainable;
- a mid-session change cannot silently bypass notice/consent requirements;
- capture that occurred before/after the change must retain truthful provenance;
- exact permission/remediation effect is not invented in this pass.

**Questions**

May recording intent change after registration? After participant admission? After live execution starts? Must participants re-acknowledge? What about late joiners? What is the effect on already-captured bytes? These are the next focused pass questions.

**Adversarial variants**

Host decides to record spontaneously; staff disables recording but provider takes seconds to stop; late joiner arrives after recording begins; recording is re-enabled after a pause.

**Analysis**

This case reaches the boundary of the current pass. The platform must version/explain intent separately from provider state, but Product/privacy authority is required before defining allowed transitions or participant effects.

**Semantic disposition**

`BLOCKED / DEFER_TO_NOTICE_AND_CONSENT_PASS`

**Proof route**

`OQ-021 + PRODUCT/PRIVACY ADJUDICATION`

**UPD if any**

None yet. Do not create an upstream delta until the focused notice/consent pass establishes whether current Product Law is insufficient.

**Evidence needed**

Focused recording-notice/consent pressure tests, followed later by provider enforcement evidence.

---

# 23. Gap register additions and refinements

## LIVE-GAP-003 refinement — accidental capture and intent changes remain inside the recording/privacy gate

**Classification:** `RECORDING_PRIVACY_GATE`

This pass does not create a second privacy gap. It refines existing `LIVE-GAP-003` with two concrete cases that OQ-021/later focused privacy work must answer:

1. provider creates capture when NewYou recording intent was false;
2. recording intent changes after participants may already have joined or after capture may already have begun.

The current pass establishes only the fail-closed rule: provider capture cannot retroactively authorise recording or replay use.

## LIVE-GAP-011 — Provider capture lifecycle/finalisation semantics are unverified

**Classification:** `PROVIDER_EMPIRICAL_GATE`

Current Architecture defines how provider evidence must be treated, but `OQ-020` still needs first-party/controlled evidence for the selected path concerning:

- recording enable/start/stop semantics;
- delayed or missing capture;
- segmentation on restart;
- finalisation/processing states;
- object-ID stability;
- duplicate/reordered callback behaviour;
- post-processing mutation/replacement;
- provider-resource replacement with recordings on both resources.

No implementation contract should assume those facts before evidence exists.

## LIVE-GAP-012 — Exact external-capture → governed-media adoption mechanism

**Classification:** `JIT_ONLY`

Authority already gives the ownership rule, so this is **not** an upstream Product/Domain gap.

JIT must define a minimal, idempotent handoff that preserves:

- provider/source provenance;
- occurrence association;
- segment/multi-artifact lineage;
- duplicate/retry safety;
- known completeness/quality state where relevant;
- independence between media adoption and replay publication.

The handoff must not create a generic integration/media orchestration platform or a speculative new Resource without evidence.

---

# 24. Upstream-delta decision for this pass

**No new `LIVE-UPD-*` is justified by Pass C.**

That is a deliberate result, not a missing step.

Current Product, Domain and Architecture Law already establish the critical authority boundary strongly enough:

1. Events & Live owns occurrence recording notice/association context.
2. Provider capture/status is evidence and operational artifact, not business/media authority.
3. Content & Media owns governed platform media identity/bytes/lineage/publication.
4. Provider capture is not replay publication.
5. Privacy/consent rules remain a separate authority and open gate.

The remaining unresolved issues in this focused pass are either:

- provider empirical facts (`LIVE-GAP-011` / OQ-020);
- implementation-grade handoff representation (`LIVE-GAP-012`);
- or explicitly deferred recording/privacy semantics under existing `LIVE-GAP-003` / OQ-021.

Creating a new upstream Product rule now would over-legislate an already coherent ownership boundary.

---

# 25. Pass-C semantic synthesis

This pass adds six durable working conclusions:

1. **Recording intent, capture outcome and media publication are three different facts.** None may be inferred automatically from another.
2. **A provider recording object is external evidence/artifact until NewYou deliberately adopts it into governed media handling.** Provider object identity never becomes platform media identity by default.
3. **One occurrence may have zero, one or many raw capture artifacts.** Segmentation/provider replacement does not justify creating duplicate occurrences or a one-to-one recording model.
4. **Capture existence does not prove completeness or usability.** Late/early/corrupt/wrong-source capture must remain distinguishable from a usable full recording.
5. **Accidental capture fails closed.** Provider behaviour cannot retroactively create recording authority; remediation/retention/deletion is deliberately deferred to the recording/privacy gate.
6. **No new upstream semantic delta is warranted yet.** Existing authority is sufficient for the raw-capture ownership boundary; the next uncertainty is privacy semantics, not Domain ownership.

No Resource, schema, state enum, storage workflow, provider API, background job, object-storage copy strategy, quality threshold or retention period is selected.

---

# 26. Current register after Pass C

## 26.1 Existing upstream candidates remain unchanged

- `LIVE-UPD-001` — stable NewYou occurrence identity + schedule/execution/correction/supersession semantics independent of provider resource.
- `LIVE-UPD-002` — Product-defined attendance meaning, assurance, correction/finality and provider-evidence relationship.
- `LIVE-UPD-003` — explicit live-right versus replay-right semantics by access/product source.
- `LIVE-UPD-004` — in-progress access continuity/revocation semantics independent of initial admission.

No `LIVE-UPD-005` is created.

## 26.2 New focused gaps

- `LIVE-GAP-011 — PROVIDER_EMPIRICAL_GATE` — provider capture lifecycle/finalisation semantics.
- `LIVE-GAP-012 — JIT_ONLY` — exact external-capture → governed-media adoption mechanism.

Existing `LIVE-GAP-003 — RECORDING_PRIVACY_GATE` is refined, not duplicated.

## 26.3 Evidence register

No `LIVE-EV-*` entries are created in this pass because provider research was intentionally withheld until NewYou semantic invariants were explicit.

---

# 27. Stop point and next-pass boundary

**Pass C stops here.**

The next approved focused pass should be only:

> **Recording notice and consent at admission/join, including late join, without yet addressing withdrawal/deletion/retention.**

That next pass may ask when notice is presented, what acknowledgement/permission is required, how a late joiner is handled, and whether recording-intent changes after admission are allowed.

It should still defer:

- consent withdrawal after capture;
- one participant withdrawing from a multi-person recording;
- Full Deletion;
- processor retention/deletion;
- replay publication/correction/withdrawal;
- communications;
- safety-content correction.

Do not proceed to those topics merely because a pressure test touches their seam.