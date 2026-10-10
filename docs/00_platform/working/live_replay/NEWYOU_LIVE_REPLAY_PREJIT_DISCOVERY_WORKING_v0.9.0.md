# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.9.0.md

- **Status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY
- **Document version:** v0.9.0
- **Date:** 2026-10-10
- **Pass:** I
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Repository authority baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted working predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.6.1.md`
- **Accepted predecessor commit:** `e9d42dcf082b173264e39e8648add359fb0531a1`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE

---

# 1. Focused-pass boundary

Pass I addresses only:

> **Replay correction, replacement, withdrawal and version history after publication — including ordinary editorial, material content, safety, legal/consent and full-withdrawal classes — while preserving occurrence/attendance truth and without yet addressing promotional clips or participant communications.**

The purpose is to determine whether current authority is semantically sufficient for FP-007 JIT planning, or whether a genuinely new live-specific upstream Product decision is required.

This pass deliberately does **not** reopen accepted Passes A–H.

## 1.1 Explicit deferrals

Pass I does **not** decide:

- promotional-clip creation, approval, audience or downstream clip-specific withdrawal;
- participant-facing notification wording, channel, timing, retry or acknowledgement;
- provider-specific editing/redaction APIs;
- exact video editor or media-processing implementation;
- exact Cloudflare/Restream object replacement mechanics;
- exact signed-link TTL, purge API, cache configuration or CDN topology;
- exact Ash Resource/action/schema/job names;
- exact correction-impact vocabulary beyond the Product-Law classes already present;
- legal sufficiency of consent/release terms;
- exact retention/deletion periods;
- whole-platform Full Deletion;
- event-commerce/ticket consequences;
- automated content/safety detection.

Promotional clips remain a separate future pass because Product Law expressly requires separate approval for clips. Communications remain separate because correction semantics must be stable before message promises are specified.

---

# 2. Current authority checked

Current routing was re-verified against live `main` through:

- `docs/00_platform/README.md`;
- `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`.

Current authority remains:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`
2. `00_PLATFORM_v1.6.0.md`
3. `01_DECISIONS_v1.6.0.md`
4. `02_OPEN_WORK_v1.2.59.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.2.0.md`
7. `05_ROADMAP_v1.2.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` only where frontend experience is in scope.

`working/` remains derived/non-authoritative planning evidence.

## 2.1 Product and Decision Law relevant to this pass

### `DEC-188 — Recording governance`

Locked Product direction requires:

- explicit recording notice;
- participant controls;
- governed editing;
- replay entitlements;
- versioning;
- correction;
- clip approval.

This means replay correction/version history is already Product capability, not a new capability invented by this pass.

### `00_PLATFORM_v1.6.0 §21G.15 — Recording and replay governance`

A recorded session requires, among other things:

- governed editing;
- replay entitlement;
- replay expiry where applicable;
- content/version history;
- correction and withdrawal;
- separate approval for promotional clips.

A replay does not become automatically public merely because the live session occurred.

### Existing Product-Law correction classes

Current Product Law uses:

```text
minor_editorial_correction
material_content_correction
safety_correction
legal_or_consent_correction
full_withdrawal
```

Current Product semantics further establish:

- minor corrections update current presentation while preserving/recording the original;
- material corrections create an approved superseding version;
- safety corrections withdraw affected use immediately, identify impact, replace where possible and create incident evidence;
- the remaining legal/consent and full-withdrawal classes remain distinct governed classes rather than aliases for ordinary editorial correction.

`PLATFORM_OPERATING_MODEL_v1.0.1` explicitly preserves these Product-Law correction classes in operational handling.

### `DEC-301 — Consent withdrawal and delivered access`

Accepted Pass F already established that purpose withdrawal invalidates dependent future processing without rewriting historical delivered truth. Pass I consumes that accepted seam only where `legal_or_consent_correction` affects a published replay.

## 2.2 Architecture Law relevant to this pass

`03_ARCHITECTURE_v1.1.1` requires:

- publication activates a specific approved version; `latest`, `approved` and `published` remain distinct;
- risk classification determines approval/correction/withdrawal requirements;
- platform-owned media identity is independent of provider/object IDs;
- masters, recordings and derivatives retain lineage;
- protected playback checks current platform authority before bounded delivery capability is issued;
- provider capture/status never becomes publication authority.

Architecture therefore already supports successor-version and withdrawal semantics without provider-object identity becoming truth.

## 2.3 Domain Law relevant to this pass

`04_DOMAIN_MAP_v1.2.0` keeps ownership separated:

- Events & Live owns occurrence/session truth, registration/attendance and occurrence recording notice/association;
- **media bytes/publication remain Content & Media**;
- Entitlements owns current general access/right validity;
- Privacy & Consent owns current purpose/consent/deletion/retention authority;
- Audit & Evidence owns evidence only;
- Analytics remains derived.

Replay correction therefore cannot rewrite Events occurrence/attendance truth and cannot make provider objects authoritative.

## 2.4 Supporting C&M working evidence — not authority

`NEWYOU_CM_PREJIT_CONTRACT_WORKING_v0.1.0.md` is non-authoritative but highly relevant supporting discovery. Its accepted working model says:

- Correction, supersession and Withdrawal are distinct;
- Content & Media owns exact content/publication truth;
- withdrawal removes current delivery authority without erasing historical Publication evidence;
- correction creates successor immutable truth rather than editing old published truth in place;
- durable media derivatives retain exact source-version lineage.

Its routing register already contains:

- `CM-UPD-002` → `OQ-014` for edge/cache/protected-delivery mechanics, including immediate safety-withdrawal invalidation;
- `CM-UPD-006` → `OQ-021` for recording/edit/replay/clip/retention/withdrawal rights;
- `CM-UPD-011` for correction impact/severity and downstream remediation mapping;
- JIT-only Publication/correction/withdrawal Resource topology.

These are working routing seams only. They do not override Product/Architecture/Domain law.

---

# 3. Semantic dimensions kept separate

Pass I treats the following as independent facts/dimensions:

1. **Occurrence truth** — what live occurrence existed and what happened.
2. **Attendance truth** — governed attendance meaning/evidence.
3. **Stable governed replay/media identity** — conceptual media identity where applicable.
4. **Exact replay/media version** — immutable governed version/bytes/provenance.
5. **Publication truth** — which exact replay version is or was published/current.
6. **Correction declaration/class** — why current media treatment changes.
7. **Current delivery eligibility** — whether playback may be issued now.
8. **Replay entitlement/access** — whether the participant otherwise has a current right.
9. **Privacy/consent authority** — whether the affected use remains permitted.
10. **Derivative lineage** — captions, transcripts, thumbnails, renditions and other dependent media.
11. **Historical delivery/evidence** — what exact version was previously delivered/published/viewed.
12. **Provider/object state** — external evidence/execution only.
13. **Derived Analytics** — projections, never current publication authority.

Critical invariant:

> `historically published version` != `currently eligible version` != `latest candidate version` != `provider object currently reachable`.

A correction must not collapse these dimensions.

---

# 4. Focused semantic synthesis before pressure tests

The current authority already supports this high-level model:

```text
published replay version V1
        │
        ├─ minor correction
        │    → preserve original
        │    → governed current presentation/correction history
        │
        ├─ material correction
        │    → approved successor V2
        │    → explicit publication transition
        │
        ├─ safety correction
        │    → affected current use withdrawn immediately
        │    → compliant successor may follow later
        │
        ├─ legal_or_consent_correction
        │    → current use determined by current legal/privacy authority
        │    → compliant successor or withdrawal may follow
        │
        └─ full_withdrawal
             → no current replay delivery
             → historical publication evidence remains governed separately
```

This diagram is a working synthesis, not a new state enum and not implementation authority.

The unresolved questions are mostly:

- exact impact/severity mapping for replay-specific corrections;
- when an existing version may remain current while a successor is prepared;
- how immediate withdrawal is enforced against stale delivery/caches;
- how derivative lineage converges on a successor version;
- how legal/consent remediation interacts with OQ-021;
- exact proof of atomic publication transition and non-resurrection.

These appear to route to existing Product classes, OQ-014/OQ-021 and C&M JIT rather than requiring a new Product decision.

---

# 5. Pressure tests

## LIVE-PT-087 — Minor editorial correction to a published replay transcript/caption

**Scenario class:** ordinary low-impact editorial correction after replay publication.

**Why this matters:** A typo, punctuation error or clearly non-material caption/transcript defect should be correctable without pretending the original never existed. The platform must avoid destructive history rewrite while also avoiding over-escalation into a full replay withdrawal when no meaning/safety/rights issue exists.

**Authority:** Product correction classes; DEC-188; §21G.15; Architecture version/publication separation; C&M supporting correction model.

**Owning Domains:** Content & Media primary; Audit & Evidence only if selected evidence is required; Events & Live remains source for occurrence/attendance only.

**Preconditions:**

- occurrence completed;
- replay V1 is published/current;
- participant entitlement/privacy authority is otherwise valid;
- defect is genuinely minor/editorial and does not alter substantive meaning, safety or consent scope.

**Timeline:**

```text
V1 published
→ minor caption/transcript defect identified
→ correction classified as minor_editorial_correction
→ corrected current presentation becomes eligible
→ original/correction history remains preserved
```

**Expected invariants:**

- original published representation/history is not silently overwritten out of existence;
- correction does not rewrite occurrence or attendance;
- correction does not imply that prior lawful V1 views never occurred;
- if the correction changes a governed immutable media derivative, its provenance/history remains explainable;
- provider state does not classify the correction.

**Questions:**

1. Must every minor caption correction create a new `MediaAssetVersion`, or may a governed presentation/derivative correction preserve original history another way?
2. What exact boundary distinguishes minor editorial from material content correction for replay media?

**Adversarial variants:**

- typo changes dosage/quantity meaning and is therefore not actually minor;
- caption contains the wrong participant name and creates privacy impact;
- transcript typo changes a safety warning from negative to affirmative meaning.

**Analysis:**

Product Law already permits minor correction while preserving/recording the original. The C&M working contract strongly favours immutable successor truth rather than destructive edits, but exact representation is JIT detail. Pass I should not force every trivial presentation correction into one schema mechanism. The semantic requirement is preservation, classification and explainability.

**Disposition:** `PASS_WITH_REFINEMENT / C&M_JIT`

**Proof route:** `PRODUCT_CORRECTION_CLASS → CONTENT_MEDIA_JIT → VERSION/PROVENANCE_EXECUTABLE_PROOF`

**UPD:** none.

**Evidence needed:** exact original/current representation provenance; correction classification; proof that prior history remains explainable.

---

## LIVE-PT-088 — Material factual/content correction after replay publication

**Scenario class:** substantive replay correction requiring approved successor version.

**Why this matters:** A published session may contain a materially incorrect educational claim that is not immediately unsafe but must not remain the canonical current replay indefinitely.

**Authority:** Product correction classes; DEC-188 versioning/correction; §21G.15 content/version history; Architecture publication/version distinction.

**Owning Domains:** Content & Media owns correction/successor/publication; applicable content/safety authority supplies required approval; Events occurrence truth is unchanged.

**Preconditions:** V1 published/current; material defect confirmed; no separate safety/legal/consent condition requiring immediate withdrawal.

**Timeline:**

```text
V1 current
→ material defect confirmed
→ successor V2 prepared
→ required review/approval satisfied
→ V2 activated as current publication
→ V1 remains historical/superseded evidence
```

**Expected invariants:**

- V2 does not destructively rewrite V1;
- publication switches to one exact approved successor;
- prior V1 delivery remains historically true;
- occurrence and attendance remain unchanged;
- a draft/processing candidate cannot become current merely because provider processing completed.

**Questions:**

1. May V1 remain current while V2 is prepared if V1 remains safe/legally eligible?
2. Which material replay corrections require which reviewer/approval set?

**Adversarial variants:**

- V2 processing succeeds but approval is stale/revoked before activation;
- V2 corrects the main video but transcript still carries V1 meaning;
- editor marks defect “minor” to avoid required review.

**Analysis:**

Product Law directly says material corrections create an approved superseding version. No new Live Product rule is required to establish successor semantics. The exact bounded impact vocabulary and reviewer/remediation mapping remains existing C&M routing (`CM-UPD-011`) / JIT detail.

**Disposition:** `PASS_WITH_REFINEMENT / EXISTING_CORRECTION_CONTRACT`

**Proof route:** `PRODUCT_CORRECTION_CLASS → CM-UPD-011 / CONTENT JIT → ATOMIC_PUBLICATION_PROOF`

**UPD:** none.

**Evidence needed:** defect classification, exact V1/V2 lineage, required approvals, publication transition evidence.

---

## LIVE-PT-089 — Safety correction discovered after replay publication; replacement is not yet ready

**Scenario class:** immediate safety withdrawal followed by possible successor replacement.

**Why this matters:** A replay containing unsafe health guidance cannot remain playable merely because producing a corrected edit takes hours or days.

**Authority:** Product safety-correction semantics; DEC-188; §21G.15; Architecture current-authority-before-delivery; C&M protected delivery/withdrawal supporting model.

**Owning Domains:** Content & Media owns current media publication/withdrawal; Safety & Eligibility / approved health authority owns applicable safety truth; Entitlements does not override withdrawn media eligibility.

**Preconditions:** V1 published; safety defect confirmed by governing authority; no compliant V2 yet.

**Timeline:**

```text
V1 current
→ safety defect confirmed
→ V1 current use withdrawn immediately
→ no replay available while remediation unresolved
→ V2 prepared/reviewed/approved
→ V2 may later become current
```

**Expected invariants:**

- “replacement not ready” never means unsafe V1 stays current by convenience;
- current entitlement cannot make V1 playable once C&M/safety eligibility is withdrawn;
- historical V1 publication evidence remains truthful while retained;
- occurrence/attendance are untouched;
- stale edge/provider state cannot defeat the withdrawal.

**Questions:**

1. What delivery capability/cache invalidation proof is sufficient for Product’s “withdraw affected use immediately” requirement?
2. What incident/evidence obligations apply to the safety correction?

**Adversarial variants:**

- active viewer already has a signed playback capability;
- CDN copy remains directly reachable;
- operator prepares V2 but accidentally republishes V1 locator;
- safety classification later proves over-cautious.

**Analysis:**

This is already a strong Product rule. The unresolved mechanism is not Product semantics but protected-delivery invalidation/proof under OQ-014 / C&M JIT. A replay may legitimately have no current replacement for a period. Availability must not outrank safety.

**Disposition:** `PASS / IMMEDIATE_WITHDRAWAL_REQUIRED`

**Proof route:** `SAFETY_AUTHORITY → CONTENT_WITHDRAWAL → OQ-014 → FAILURE/EDGE/DELIVERY_PROOF`

**UPD:** none.

**Evidence needed:** correction authority/classification, withdrawal commit, bounded-delivery invalidation evidence, eventual replacement lineage if any.

---

## LIVE-PT-090 — Legal or consent correction requires removing one participant segment after publication

**Scenario class:** post-publication legal/consent remediation in multi-person media.

**Why this matters:** Accepted Pass F already established that purpose withdrawal after publication cannot be ignored and that separability is evidence rather than authority. Pass I must now connect that to correction/version history without re-deciding OQ-021.

**Authority:** Product `legal_or_consent_correction`; §21G.15; DEC-301; accepted `LIVE-UPD-006`; OQ-021; C&M ownership/version/withdrawal model.

**Owning Domains:** Privacy & Consent owns current purpose authority; Content & Media owns replay correction/publication; Events occurrence/attendance remains unchanged.

**Preconditions:** V1 published; one participant’s current replay-use authority is no longer valid for the affected contribution; compliant edit may be technically possible.

**Timeline:**

```text
V1 current
→ legal/consent authority changes
→ affected current use re-evaluated
→ V1 restricted/withdrawn as required
→ compliant V2 edited from governed source/lineage
→ V2 reviewed/approved
→ V2 may become current
```

**Expected invariants:**

- technical editability does not itself authorise V2;
- current privacy authority controls future use;
- V1 history is not rewritten;
- another participant’s continued authority does not cancel the withdrawing participant’s consequence;
- removing one participant does not rewrite occurrence/attendance truth;
- derivatives containing the affected contribution must be considered.

**Questions:**

1. When exactly must V1 cease current delivery pending V2?
2. Which participant roles/contracts may have independent lawful bases?
3. What derivatives count as dependent affected representations?

**Adversarial variants:**

- contribution is visually separable but transcript/thumbnail remains identifying;
- affected participant appears throughout most of the session;
- legal authority changes while a replacement render is already running;
- replacement accidentally includes an old unredacted caption track.

**Analysis:**

No new correction capability is missing. The unresolved legal/consent consequence is already routed through OQ-021 and accepted `LIVE-UPD-006`; exact C&M remediation uses successor/withdrawal semantics already present. Pass I must not invent the legal answer.

**Disposition:** `BLOCKED / OQ-021_AND_ACCEPTED_UPD-006`

**Proof route:** `CURRENT_PRIVACY_AUTHORITY → OQ-021 → CONTENT/PRIVACY_JIT → EXECUTABLE_LINEAGE/DELIVERY_PROOF`

**UPD:** none; reuse `LIVE-UPD-006`.

**Evidence needed:** current consent/lawful-basis authority, affected contribution/derivative lineage, V1 withdrawal/restriction evidence, V2 approvals.

---

## LIVE-PT-091 — Full replay withdrawal with no successor replacement

**Scenario class:** terminal current-publication withdrawal without replacement.

**Why this matters:** Correction handling must allow the correct answer to be “there is no current replay” rather than forcing a replacement or deleting occurrence history.

**Authority:** Product `full_withdrawal`; §21G.15 correction/withdrawal; Architecture current authority; C&M publication ownership.

**Owning Domains:** Content & Media primary; Privacy/Safety/legal authority may supply cause; Events remains occurrence/attendance owner.

**Preconditions:** V1 published/current; approved authority determines the replay must no longer be delivered; no successor is approved.

**Timeline:**

```text
V1 current
→ full withdrawal approved
→ current replay publication/delivery ends
→ historical publication/withdrawal evidence remains governed
→ no V2 required
```

**Expected invariants:**

- absence of successor is valid;
- withdrawn V1 is not returned merely because entitlement remains valid;
- historical publication/withdrawal remains explainable;
- event occurrence/attendance remains true;
- provider object existence is irrelevant to current publication authority.

**Questions:**

1. What exact operator/approval authority may perform `full_withdrawal` for a replay?
2. Which downstream projections/search/indexes must converge before release proof is satisfied?

**Adversarial variants:**

- old signed URL still works;
- provider dashboard still labels object active;
- a scheduled republish job targets V1 after withdrawal;
- cache/search still advertises the replay.

**Analysis:**

Current law already distinguishes withdrawal from correction/replacement. A successor is not mandatory. This case should fail closed on current delivery while preserving truthful history.

**Disposition:** `PASS_WITH_REFINEMENT / C&M_JIT_AND_OQ-014`

**Proof route:** `CONTENT_WITHDRAWAL → OQ-014 / SEARCH-CACHE_RECONCILIATION → EXECUTABLE_PROOF`

**UPD:** none.

**Evidence needed:** withdrawal authority/reason/class, current-publication transition, stale projection/capability proof, historical publication evidence.

---

## LIVE-PT-092 — Successor replay is current but an old signed delivery capability still targets V1

**Scenario class:** stale bounded-delivery capability after correction/replacement.

**Why this matters:** Version history is meaningless if an old capability can indefinitely bypass current correction/withdrawal authority.

**Authority:** Architecture current-authority-before-bounded-delivery; Product safety/withdrawal rules; C&M `CM-UPD-002` / OQ-014 supporting routing; accepted `LIVE-PT-011` stale replay access concern.

**Owning Domains:** Content & Media current publication; Entitlements current access; provider/CDN execution only.

**Preconditions:** V1 previously current; V2 now current or V1 withdrawn; a V1 delivery capability was issued earlier.

**Timeline:**

```text
V1 capability issued
→ correction/withdrawal commits
→ V2 current or no replay current
→ old V1 capability is presented
```

**Expected invariants:**

- a stale capability cannot become durable publication authority;
- safety/legal/consent withdrawal must not be defeated by capability lifetime;
- exact TTL/purge/revocation mechanism remains replaceable;
- ordinary material correction may have different urgency from safety/legal withdrawal, but the platform must implement the governing class correctly.

**Questions:**

1. Which correction classes require active invalidation versus sufficiently short bounded expiry?
2. How is the proof demonstrated for Cloudflare/other chosen media delivery?

**Adversarial variants:**

- capability cached in a browser;
- direct provider URL bypasses application route;
- capability spans the exact publication transition moment;
- V1 remains legally retainable but no longer deliverable.

**Analysis:**

This is an implementation/proof question already represented by OQ-014 and accepted stale-link pressure testing. It does not justify a new Product rule. Safety/legal immediacy constrains the eventual delivery design.

**Disposition:** `PASS_WITH_REFINEMENT / OQ-014_EXECUTABLE_PROOF`

**Proof route:** `CURRENT_PUBLICATION_AUTHORITY → PROTECTED_DELIVERY → OQ-014 → CONTROLLED_FAILURE/REVOCATION_PROOF`

**UPD:** none.

**Evidence needed:** correction class, exact publication transition, capability issue/expiry/revocation evidence, provider/CDN residual-access tests.

---

## LIVE-PT-093 — V2 video is current but captions/transcript/thumbnail still come from V1

**Scenario class:** derivative lineage mismatch after replay replacement.

**Why this matters:** A corrected video can still deliver incorrect, unsafe or identifying information through derivatives.

**Authority:** Architecture media lineage; Product version history/correction; C&M derivative lineage and non-auto-inherited permissions.

**Owning Domains:** Content & Media.

**Preconditions:** V1 published with derivative set D1; V2 approved/current; one or more D1 derivatives remain attached or discoverable.

**Timeline:**

```text
V1 + D1 current
→ correction produces V2
→ V2 activated
→ stale D1 transcript/caption/thumb still served
```

**Expected invariants:**

- exact derivative source/version lineage is known;
- a derivative is not assumed compatible merely because its file still exists;
- legal/consent/safety correction propagates to affected derivatives;
- old derivatives may remain historically retained only under their lawful/governed disposition, not current-use convenience.

**Questions:**

1. Which derivative classes can be deliberately reused across replay versions and under what explicit compatibility proof?
2. Does a minor caption-only correction create a successor derivative while video version remains the same conceptual current replay?

**Adversarial variants:**

- transcript includes removed participant name;
- thumbnail shows sensitive frame removed from V2;
- captions generated from V1 auto-attach to V2;
- translated subtitle track has not yet been corrected.

**Analysis:**

The semantic requirement is lineage-complete convergence, not a prescribed schema. Exact derivative/version representation belongs to C&M JIT. No new Domain or Product decision is needed.

**Disposition:** `PASS_WITH_REFINEMENT / CONTENT_MEDIA_JIT`

**Proof route:** `CONTENT_LINEAGE_CONTRACT → JIT → DERIVATIVE_COMPATIBILITY/NON-RESURRECTION_PROOF`

**UPD:** none.

**Evidence needed:** source-version lineage, derivative eligibility, compatibility/replacement evidence, stale derivative tests.

---

## LIVE-PT-094 — Correction processing or successor render fails halfway

**Scenario class:** correction failure/recovery semantics.

**Why this matters:** Failure must not accidentally publish an incomplete replacement or restore a version that the governing correction class says must remain withdrawn.

**Authority:** Product correction classes; Architecture degradation/correct refusal; C&M immutable-version/publication model.

**Owning Domains:** Content & Media; Safety/Privacy/legal authority where applicable.

**Preconditions:** correction initiated; V2 candidate processing begins; render/processing/upload fails or produces unusable output.

**Timeline A — ordinary material correction:**

```text
V1 remains eligible/current
→ V2 candidate processing fails
→ V2 not published
→ V1 remains current unless separately withdrawn
```

**Timeline B — safety/legal/consent correction requiring immediate withdrawal:**

```text
V1 withdrawn/restricted
→ V2 candidate processing fails
→ no current replay
→ V1 must not return by fallback
```

**Expected invariants:**

- processing success/failure is not publication truth;
- no partial V2 becomes current;
- correction class controls whether V1 may remain current;
- safety/legal fail-closed withdrawal survives worker/provider failure;
- retry creates no duplicate current publication identities.

**Questions:**

1. What exact correction-impact mapping determines whether V1 may remain current during remediation?
2. How is retry/reconciliation keyed so one logical successor is not multiplied?

**Adversarial variants:**

- render succeeds but upload finalisation is ambiguous;
- approval happens before processing fails;
- retry produces two candidate objects;
- worker restarts from stale pre-withdrawal state.

**Analysis:**

This is exactly where `CM-UPD-011` matters: current Product classes exist, but exact impact-to-remediation mapping must be explicit in JIT. There is no evidence of a missing live-specific Product class.

**Disposition:** `PASS_WITH_REFINEMENT / CM-UPD-011_DEPENDENT`

**Proof route:** `CORRECTION_CLASS → CM-UPD-011 / CONTENT_JIT → RETRY/FAILURE-INJECTION_PROOF`

**UPD:** none.

**Evidence needed:** correction classification, current-publication state before/after failure, retry identity, stale-worker tests.

---

## LIVE-PT-095 — Viewer requests playback concurrently with correction activation

**Scenario class:** concurrency at publication transition.

**Why this matters:** A viewer must receive one coherent exact eligible replay version, not a mixed or authority-racing result.

**Authority:** Architecture exact version/current authority doctrine; Product correction/withdrawal; C&M publication model.

**Owning Domains:** Content & Media publication; Entitlements/access check; Privacy current authority where relevant.

**Preconditions:** V1 current; V2 approved and activation begins; viewer initiates playback during the transition.

**Timeline:**

```text
viewer request R
↘
 V1 current → atomic governed activation → V2 current
↗
playback capability decision
```

**Expected invariants:**

- capability resolves against one coherent committed publication state;
- no mixed V1 video/V2 metadata result where exact-version integrity is required;
- no capability is issued from uncommitted candidate state;
- safety/legal withdrawal takes precedence over availability;
- PubSub/UI freshness is not authority.

**Questions:**

1. What atomicity boundary is required between current Publication and the exact MediaAssetVersion/derivative set?
2. If R races the transition, is serving V1 still valid for ordinary material correction but invalid for a safety withdrawal?

**Adversarial variants:**

- two application instances observe transition at different moments later in scale;
- cache points to V1 while DB current is V2;
- V2 activation commits but capability signing times out ambiguously.

**Analysis:**

Architecture already requires authority before delivery and exact approved version publication. The exact transaction/capability mechanism belongs to C&M JIT/proof. Correction class still controls urgency/eligibility.

**Disposition:** `PASS_WITH_REFINEMENT / CONCURRENCY_PROOF_REQUIRED`

**Proof route:** `CONTENT_JIT → ATOMIC_PUBLICATION/CAPABILITY_CONCURRENCY_PROOF`

**UPD:** none.

**Evidence needed:** exact publication/version transition proof, capability issuance correlation, race/failure tests.

---

## LIVE-PT-096 — A correction itself is later found wrong

**Scenario class:** correction-of-correction / successor supersession.

**Why this matters:** A version-history model must remain truthful under human error. “Rollback” must not mean destructive history rewrite.

**Authority:** Product version history/correction; C&M successor immutable truth; Audit append-only correction doctrine where selected evidence applies.

**Owning Domains:** Content & Media.

**Preconditions:** V1 published; V2 superseded V1; V2 later found wrong or incomplete.

**Timeline:**

```text
V1 historical
→ V2 current
→ V2 defect confirmed
→ V3 successor or current withdrawal
→ V1/V2 remain historical according to retention rules
```

**Expected invariants:**

- V2 is not edited in place to masquerade as never wrong;
- a return to V1 content, if appropriate, is a new governed current decision rather than erasing V2 history;
- current publication points to one exact eligible version;
- provider object reuse does not collapse semantic version history.

**Questions:**

1. Can exact prior bytes be reused as a new governed successor/current version while preserving correction provenance?
2. What bounded evidence is necessary to explain V2 → V3 correction without duplicating full media payload into Audit?

**Adversarial variants:**

- operator selects historical V1 provider object directly;
- V2 was safety correction but reintroduced another safety issue;
- V3 is byte-identical to V1 but approved under new current authority.

**Analysis:**

Current version/correction doctrine is sufficient. Reverting semantic content does not justify destructive history rewind. Exact media identity/version representation is JIT detail.

**Disposition:** `PASS`

**Proof route:** `CONTENT_VERSION_LINEAGE → JIT → CORRECTION_CHAIN_PROOF`

**UPD:** none.

**Evidence needed:** correction lineage, current-publication history, exact version/object provenance.

---

## LIVE-PT-097 — Replay correction must not rewrite occurrence, attendance or historical delivery evidence

**Scenario class:** cross-domain historical truth preservation.

**Why this matters:** Media correction can otherwise leak into unrelated authority: changing attendance, pretending old viewers saw V2, or relabelling provider/history events as if corrected content had always existed.

**Authority:** Domain Law ownership; Product correction/version history; Architecture authority separation; accepted Passes A/B/H.

**Owning Domains:** Events & Live for occurrence/attendance; Content & Media for replay version/publication; Audit & Evidence for selected evidence; Analytics derived only.

**Preconditions:** V1 was published and viewed by some participants; V2 later becomes current or V1 is withdrawn.

**Timeline:**

```text
occurrence O completed
attendance facts A committed
V1 published / replay_started events occur
→ later correction/withdrawal
→ V2 current or no replay
```

**Expected invariants:**

- O and A are not rewritten by media correction;
- prior replay-start/delivery evidence refers to the version/publication actually delivered at that time where the evidence contract requires version specificity;
- historical views are not relabelled as V2 views;
- derived Analytics may recompute current dashboards but cannot rewrite source history;
- correction/withdrawal evidence does not become occurrence authority.

**Questions:**

1. What exact minimum replay-version/publication reference must delivery/Audit/Analytics evidence carry?
2. Which historical analytics may be recomputed versus which event-level evidence remains fixed?

**Adversarial variants:**

- correction removes a participant segment but historical attendance remains named under its lawful retention contract;
- current dashboard reports only corrected V2 views and accidentally erases V1 history;
- Audit source reference later becomes non-resolvable under deletion.

**Analysis:**

Ownership law already answers the primary semantic question: media correction cannot mutate Events truth. Exact evidence-envelope/version-reference design is JIT/proof detail. Analytics remains derived.

**Disposition:** `PASS_WITH_REFINEMENT / JIT_EVIDENCE_CONTRACT`

**Proof route:** `DOMAIN_OWNERSHIP → CONTENT/AUDIT/ANALYTICS_JIT → TRACEABILITY_PROOF`

**UPD:** none.

**Evidence needed:** occurrence/attendance invariance, publication/version history, exact delivered-version traceability where selected, derived-state rebuild tests.

---

# 6. Pass-I synthesis

The focused pressure tests support these proposed working conclusions:

1. **Replay correction is already an authorised Product capability.** DEC-188 and §21G.15 require replay versioning/correction/withdrawal.
2. **The existing Product correction classes apply as the controlling correction vocabulary.** Pass I must not invent replay-only severity classes merely for implementation convenience.
3. **Minor correction still requires preserved original history.** Exact representation may be a governed presentation/derivative correction or successor media truth; destructive in-place historical rewrite is not acceptable.
4. **Material correction creates an approved superseding version.** Candidate processing/provider completion is not publication authority.
5. **Safety correction withdraws affected current use immediately.** Lack of a ready replacement is not permission to keep unsafe replay current.
6. **Legal/consent correction composes with current Privacy authority and accepted `LIVE-UPD-006`.** Technical editability cannot substitute for OQ-021/legal authority.
7. **Full withdrawal may legitimately leave no current replay.** A successor is not mandatory.
8. **Current replay publication and historical publication evidence are separate.** Withdrawal/correction does not make historical publication or prior lawful views disappear.
9. **Derivative lineage must converge on the corrected/current replay.** Old captions/transcripts/thumbnails cannot silently remain current when their meaning/rights are affected.
10. **Correction failure semantics depend on the correction class.** Ordinary material correction may leave an otherwise eligible V1 current until V2 activation; safety/legal/consent withdrawal that already invalidates V1 must remain fail-closed when V2 processing fails.
11. **Stale delivery capability/cache/provider reachability cannot become current publication authority.** OQ-014/proof must make safety/legal withdrawal enforceable.
12. **Correction-of-correction uses successor/withdrawal semantics, not destructive rollback.**
13. **Replay correction never rewrites occurrence or attendance truth.** Cross-domain historical meaning remains owner-controlled.
14. **No new Live Product decision package is currently justified.** Existing Product classes, OQ-014/OQ-021 and C&M JIT/CM-UPD-011 already own the remaining work.

---

# 7. UPD adjudication

## No LIVE-UPD-007

Pass I creates no new `LIVE-UPD-*` identifier.

Reasons:

1. Product Law already requires replay versioning, correction and withdrawal.
2. Product Law already defines the five correction classes.
3. Material and safety correction consequences are already materially specified.
4. Legal/consent consequence already routes through OQ-021 and accepted `LIVE-UPD-006`.
5. Exact correction-impact/remediation mapping is already exposed by Content & Media working seam `CM-UPD-011` and belongs to the proper Product/Content/Safety/Privacy/JIT owners.
6. Stale delivery invalidation is already OQ-014 / protected-delivery proof, not a missing Product capability.

Creating `LIVE-UPD-007` would duplicate current authority/routing rather than expose a missing decision.

---

# 8. Gap-register adjudication

## No LIVE-GAP-015

Pass I creates no new `LIVE-GAP-*` identifier.

Existing routing is sufficient:

- `LIVE-GAP-003 — RECORDING_PRIVACY_GATE` remains the correct seam for post-publication `legal_or_consent_correction` where recording/replay rights are affected under OQ-021;
- accepted `LIVE-UPD-006` remains the missing post-capture withdrawal consequence package;
- OQ-014 / C&M `CM-UPD-002` owns protected-delivery/cache invalidation and immediate safety-withdrawal proof;
- C&M `CM-UPD-011` owns exact correction impact/severity → downstream remediation mapping;
- Content & Media JIT owns exact replay correction/withdrawal/version Resource topology and derivative lineage representation;
- accepted `LIVE-GAP-014` remains processor deletion/non-resurrection, not ordinary correction publication.

`LIVE-GAP-005 — replay-right policy` is not expanded into correction/publication eligibility. Entitlement/right truth and media publication eligibility remain separate.

---

# 9. Evidence register

No `LIVE-EV-*` item is added by Pass I.

Pass I does, however, refine later proof expectations:

- exact V1→V2 publication/version lineage;
- atomic current-publication transition;
- safety/legal withdrawal fail-closed behaviour;
- stale delivery/cache/provider capability invalidation;
- derivative compatibility/replacement lineage;
- correction retry/failure recovery;
- correction-of-correction history;
- preservation of occurrence/attendance truth;
- delivered-version traceability where the eventual evidence contract selects it.

Provider-specific empirical research remains deferred until correction semantics and the selected media provider path are ready for targeted proof.

---

# 10. Explicit non-decisions preserved

Pass I does **not** decide:

- exact thresholds distinguishing minor from material correction beyond current Product semantics;
- exact reviewer/approver matrix per replay risk class;
- exact legal/consent remedy under OQ-021;
- exact participant notification requirements;
- promotional clip correction/withdrawal propagation;
- exact signed-link TTL or purge mechanics;
- exact media editing/redaction technology;
- exact derivative compatibility algorithm;
- exact incident schema;
- exact Analytics event schema;
- provider-specific media object/versioning APIs;
- exact retention/deletion durations;
- exact Ash Resource/schema/job/storage implementation.

---

# 11. Pass-I proposed status

**Outcome:** `PASS`

**Reason:** Current authority is semantically sufficient to plan replay correction/version-history JIT work without a new Product amendment. Remaining uncertainty is correctly routed to existing Product correction classes, OQ-014, OQ-021, accepted `LIVE-UPD-006`, C&M `CM-UPD-011`, C&M JIT and executable/provider proof.

**New proposed identifiers:**

- Pressure tests: `LIVE-PT-087...LIVE-PT-097`
- New UPDs: none
- New gaps: none
- New evidence IDs: none

All Pass-I findings remain `PROPOSED / AWAITING_USER_ACCEPTANCE` until explicitly accepted.

---

# 12. Proposed next focused pass

Only after Pass I acceptance:

> **Promotional clips derived from live/replay media — separate approval, purpose/audience, participant/speaker rights, correction/withdrawal propagation and lineage — while still deferring participant communications.**

That pass should specifically test:

- clip approval is separate from replay publication approval;
- a clip may not inherit recording/replay permission automatically;
- clip source-version lineage after replay correction;
- correction/withdrawal of source replay versus already-approved clip;
- consent withdrawal that affects clip purpose but not necessarily replay purpose;
- promotional/public audience versus protected replay audience;
- stale clip delivery/publication after source correction;
- speaker/guest versus attendee contribution in clips.

Participant-facing communication promises should remain a later separate pass so notification semantics are based on accepted correction/clip consequences rather than guesses.