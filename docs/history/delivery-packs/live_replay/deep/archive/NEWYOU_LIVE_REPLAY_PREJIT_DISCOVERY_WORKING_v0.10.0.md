# NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.10.0.md

- **Status:** WORKING / NON-AUTHORITATIVE DISCOVERY
- **Document version:** v0.10.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.9.0.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted register predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.7.1.md`
- **Accepted register commit:** `0eed5028af0f16209cacbcf595ae679b9ab6e180`
- **Pass:** J
- **Focused semantic class:** promotional clips derived from live/replay media
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE

---

# 1. Pass-J bounded question

This pass asks only:

> **What durable semantics govern promotional clips derived from live/replay media, especially separate approval, public/promotional purpose, participant/speaker rights, source-version lineage and correction/withdrawal propagation?**

This pass does **not** design:

- participant communication wording, timing, channels or templates;
- a marketing campaign system;
- a social-publishing product/domain;
- provider-specific social APIs;
- exact video-editing/redaction tooling;
- exact Ash Resource/schema/job topology;
- exact clip duration/aspect-ratio/branding rules;
- campaign analytics or attribution;
- paid advertising operations;
- exact legal release wording;
- final retention schedules;
- a new Roadmap Feature Pack.

The pass must not silently expand the FP-007 Roadmap exit condition.

---

# 2. Authority baseline

## 2.1 Product Law already makes clip approval separate

Current Product Law §21G.15 requires recording/replay governance including:

- recording notice;
- participant/speaker consent rules;
- attendee privacy controls;
- governed editing;
- replay entitlement;
- replay expiry where applicable;
- content/version history;
- correction and withdrawal;
- **separate approval for promotional clips**.

It also states that a recording does not become public merely because the live session occurred.

Therefore:

```text
live participation/capture authority
!= replay-publication authority
!= promotional-clip authority
```

A promotional clip is not simply a smaller replay.

## 2.2 DEC-188 already authorises clip governance

`DEC-188 — Recording governance` is LOCKED and requires explicit recording notice, participant controls, governed editing, replay entitlements, versioning, correction and clip approval.

Pass J therefore does not need to invent the existence of a clip-approval capability.

## 2.3 OQ-021 explicitly owns unresolved clip rules

`OQ-021 — Video consent and retention` remains LEGAL / OPERATIONS REVIEW and explicitly requires definition of:

```text
speaker
attendee
recording
editing
replay
clip
retention
withdrawal
rules
```

The exact legal/operational consequence of a participant/speaker allowing replay but not promotion, withdrawing promotional use, or appearing with others in a public clip therefore remains governed by OQ-021.

## 2.4 Consent/lawful basis is purpose-specific

Architecture states that consent/lawful-basis authority is purpose-specific and material revocation triggers dependent invalidation obligations.

Accordingly:

```text
recording participation purpose
replay-delivery purpose
promotional/public-use purpose
```

must not be collapsed merely because the same bytes are involved.

## 2.5 Content & Media owns clip media/publication truth

Domain Law assigns governed content/publication version and editorial media identity/derivatives/publication to Content & Media. Events and Communications are consumers where relevant; they do not gain media-publication authority.

Events & Live continues to own occurrence/registration/attendance and recording association, not clip publication.

## 2.6 C&M derivative permissions do not auto-inherit

The current working Content & Media contract is non-authoritative but highly relevant supporting evidence. It says:

- stable platform-owned media identity/version;
- durable derivatives retain exact source-version lineage;
- **derivative permissions do not automatically inherit from the source**;
- rights/provenance/risk/publication remain exact C&M authority;
- correction creates successor immutable truth;
- withdrawal removes current delivery authority without rewriting historical publication evidence.

The C&M upstream register already routes:

- `CM-UPD-005` → OQ-020 live/video provider validation;
- `CM-UPD-006` → OQ-021 recording/video consent and retention, including clip rights/withdrawal;
- `CM-UPD-011` → correction impact/severity and downstream remediation.

Pass J must reuse those seams rather than creating competing authority.

## 2.7 FP-007 does not require promotional clips for its Roadmap exit

The current Roadmap exit condition for FP-007 is:

> a governed session can be published, registered, joined, recorded/replayed under approved policy, reconciled after provider failure and audited; notification failure is visible; protected playback never leaks through stale access.

Promotional clips are not named as an FP-007 exit condition.

Therefore the working scope rule is:

> **Promotional clips are Product-authorised and governed if included, but they are not automatically required to complete FP-007.**

A future Final Feature Pack Contract may include or explicitly defer them only within Roadmap/Product authority; discovery must not silently convert optional/adjacent Product capability into a required FP-007 deliverable.

---

# 3. Semantic dimensions kept separate

Pass J keeps these facts independent:

1. source live occurrence truth;
2. source recording/media version truth;
3. replay publication/current-version truth;
4. clip derivative media identity/version truth;
5. clip source-version lineage;
6. clip approval truth;
7. participant/speaker promotional-purpose authority;
8. clip publication/audience truth;
9. replay entitlement/access truth;
10. clip correction/withdrawal truth;
11. provider/social-channel delivery evidence;
12. historical publication/audit evidence.

The following collapses are forbidden:

```text
replay approved => clip approved                 [false]
recorded => promotional use allowed              [false]
source publicly reachable => clip rights exist   [false]
clip approved => every derivative/use approved   [false]
provider post exists => NewYou publication truth [false]
replay withdrawn => clip always withdrawn        [not necessarily]
replay current => all old clips current           [false]
```

---

# 4. Working clip model

## 4.1 Clip is a governed derivative, not a pointer into a replay URL

A promotional clip should be treated conceptually as its own governed media derivative/version with:

- exact source MediaAssetVersion lineage;
- exact edited bytes/version;
- its own rights/purpose eligibility;
- its own approval evidence;
- its own publication/current-withdrawn truth;
- historical publication evidence.

This does **not** decide Ash topology.

## 4.2 Source replay publication is not a prerequisite

A clip may in principle derive from an exact governed recording/media source even if no replay is published, provided all independent clip requirements are satisfied.

The source provider artifact alone is insufficient. The source must have governed NewYou media identity/lineage before the derivative becomes authoritative C&M media.

## 4.3 Public/promotional audience differs from protected replay audience

A protected replay may require an entitlement while a separately approved promotional clip is public.

That does not leak the replay entitlement because the clip is its own bounded approved media publication.

Conversely, replay entitlement cannot authorise publication of a promotional excerpt.

## 4.4 Clip approval is exact-version approval

A clip approval applies to the exact governed clip version/subject and applicable purpose/audience.

Changing the clip materially creates a successor subject requiring the applicable review/approval path.

## 4.5 Source change requires impact evaluation, not mechanical invalidation or mechanical preservation

If source replay/recording V1 is corrected or withdrawn, an existing clip derived from V1 must be evaluated against why the source changed and whether the affected material/right/purpose reaches the clip.

Two equally unsafe shortcuts are forbidden:

```text
source changed => every clip automatically invalid
source changed => every approved clip automatically remains valid
```

The correction/withdrawal class and exact clip lineage determine the required consequence.

## 4.6 Current clip publication and historical clip publication are separate

Withdrawing or superseding a clip stops current NewYou-controlled publication/use but does not falsify that the older clip was historically approved/published or viewed while valid.

Retention/deletion remains separately governed.

---

# 5. Pressure tests

## LIVE-PT-098 — Clip bytes exist but no separate promotional-clip approval exists

### Scenario class
Separate clip approval.

### Why it matters
A team may assume that because the live session was lawfully recorded and replay V1 is approved, cutting a 30-second excerpt is merely an editing operation.

### Authority
Product §21G.15; DEC-188; OQ-021; Content & Media ownership.

### Owning domains
Content & Media; Privacy & Consent where promotional-purpose authority is required. Events & Live supplies source association only.

### Preconditions
- lawful governed source recording exists;
- replay may or may not already be approved;
- a clip derivative is rendered;
- no separate clip approval exists.

### Timeline
1. Source recording V1 is governed.
2. Clip C1 is rendered from V1.
3. Operator attempts public/promotional publication because replay V1 is already approved.

### Expected invariants
- C1 is not publishable merely because V1/replay is approved;
- rendering/provider completion is not approval;
- source permission does not auto-inherit to derivative purpose;
- no public clip is created by convenience/UI action alone.

### Questions
- Is separate clip approval truly mandatory? Yes, Product Law explicitly says so.
- Can approval be represented only by provider draft state? No.

### Adversarial variants
- clip is only five seconds;
- clip contains only the presenter;
- clip is intended for NewYou's own public site rather than social media;
- clip is generated automatically.

None removes the separate-approval requirement.

### Analysis
This scenario is already decided by Product Law at the capability level. JIT may decide exact workflow/evidence representation but cannot waive approval because the excerpt is short or technically harmless.

### Disposition
`PASS / FAIL_CLOSED_BY_EXISTING_PRODUCT_LAW`

### Proof route
`PRODUCT §21G.15 + DEC-188 → CONTENT_MEDIA_JIT → APPROVAL/PUBLICATION_EXECUTABLE_PROOF`

### UPD
None.

### Evidence needed
Show that a rendered derivative without current separate clip approval cannot become current publication.

---

## LIVE-PT-099 — Separately approved public clip is derived from an entitlement-protected replay

### Scenario class
Purpose/audience separation.

### Why it matters
The system must support a public promotional excerpt without turning a protected replay into public content.

### Authority
Product §21G.15; Architecture media lineage/protected delivery; Content & Media ownership; Entitlements ownership.

### Owning domains
Content & Media owns clip publication; Entitlements owns replay access; Privacy owns promotional-purpose authority where applicable.

### Preconditions
- replay R1 is protected by entitlement;
- clip C1 derives from exact source version V1;
- C1 has required promotional-purpose rights and separate approval;
- C1 is intended for public audience.

### Timeline
1. Participant without replay entitlement opens public page containing C1.
2. C1 is delivered as its own public media publication.
3. Participant attempts to follow/reuse C1 delivery path to obtain R1.

### Expected invariants
- valid C1 may be public independently of R1;
- C1 publication does not manufacture replay entitlement;
- C1 delivery must not expose a reusable replay capability;
- exact C1 lineage remains auditable.

### Questions
- Does protected-source status require the clip itself to be protected? Not automatically.
- Does public C1 make source R1 public? No.

### Adversarial variants
- C1 and R1 share underlying object bytes;
- same CDN/provider hosts both;
- clip route includes source media ID.

Storage/locator sharing cannot collapse publication/access truth.

### Analysis
Public audience and protected replay audience are separate publication/access facts. The safe design is an independently governed derivative, not exposing a time range on a reusable protected replay URL.

### Disposition
`PASS_WITH_REFINEMENT / CONTENT_MEDIA_JIT_AND_ACCESS_PROOF`

### Proof route
`CONTENT_MEDIA_JIT → ENTITLEMENTS/DELIVERY BOUNDARY → SECURITY/EXECUTABLE PROOF`

### UPD
None.

### Evidence needed
Prove public clip access does not permit protected-source playback beyond the approved derivative.

---

## LIVE-PT-100 — Replay participation/replay permission exists but promotional-purpose authority does not

### Scenario class
Purpose-specific consent/rights.

### Why it matters
Recording/replay participation is not equivalent to endorsement or public promotional use.

### Authority
Product §21G.15; Architecture purpose-specific consent; OQ-021; accepted `LIVE-UPD-006`.

### Owning domains
Privacy & Consent owns purpose authority; Content & Media owns clip publication; Events retains source session truth.

### Preconditions
- participant validly appeared in recording/replay;
- replay publication is currently valid;
- no valid promotional/public-use authority is established for that participant/context.

### Timeline
1. Editor selects participant's statement for C1.
2. C1 passes ordinary editorial review.
3. Publication attempts to treat replay permission as promotional permission.

### Expected invariants
- publication fails closed;
- replay remains unaffected solely by missing promotional authority;
- editor/provider state cannot manufacture purpose authority.

### Questions
- Does replay permission imply clip permission? No.
- Can OQ-021/legal authority later establish role-specific contractual alternatives? Yes; JIT cannot invent them.

### Adversarial variants
- participant is a planned guest;
- participant is a staff facilitator;
- participant is an attendee promoted to speaker;
- source clip contains only voice, not face.

Role/surface may affect the eventual rule but does not itself create clip authority.

### Analysis
This is the central clip/privacy boundary. Existing Product/Architecture/OQ authority already owns it.

### Disposition
`BLOCKED / OQ-021_PROMOTIONAL_PURPOSE_RULE_REQUIRED`

### Proof route
`OQ-021 + PRIVACY JIT → CONTENT_MEDIA JIT → PURPOSE/PUBLICATION PROOF`

### UPD
No new UPD; accepted `LIVE-UPD-006` already includes purpose-specific replay versus promotional-clip withdrawal/authority.

### Evidence needed
Approved OQ-021 rule and executable current-purpose enforcement.

---

## LIVE-PT-101 — Source replay receives a material correction outside the excerpt used by an approved clip

### Scenario class
Source correction propagation without over-invalidation.

### Why it matters
Naively withdrawing every derivative whenever the source changes creates needless churn; naively preserving every derivative is unsafe.

### Authority
Product correction classes; accepted Pass I; C&M exact source lineage; CM-UPD-011.

### Owning domains
Content & Media, with affected authority owner depending correction reason.

### Preconditions
- C1 is approved and published from source V1;
- replay V1 later receives material correction producing V2;
- corrected material is outside C1 and does not alter C1 rights/safety/context.

### Timeline
1. V1 and C1 are current.
2. V2 supersedes replay V1.
3. System evaluates C1.

### Expected invariants
- C1 retains lineage to V1; it is never relabelled as derived from V2;
- C1 is not automatically invalid solely because V2 exists;
- C1 current eligibility is explicitly re-evaluated against correction impact;
- audit can explain why C1 remained or was withdrawn.

### Questions
- Must C1 always be re-rendered? Not established and likely unnecessary when unaffected.
- May C1 silently claim V2 lineage? No.

### Adversarial variants
- transcript context changed elsewhere in V2;
- source title changed but excerpt meaning did not;
- V2 re-encodes entire recording without semantic changes to C1.

### Analysis
Exact lineage plus correction-impact evaluation is simpler and more truthful than global invalidation.

### Disposition
`PASS_WITH_REFINEMENT / CM-UPD-011_IMPACT_EVALUATION`

### Proof route
`PRODUCT CORRECTION CLASS → CM-UPD-011 / CONTENT_MEDIA_JIT → LINEAGE/IMPACT PROOF`

### UPD
None.

### Evidence needed
Show C1 retains exact V1 provenance and current eligibility is explicitly adjudicated.

---

## LIVE-PT-102 — Source material correction directly affects the excerpt used by an approved clip

### Scenario class
Stale clip after source correction.

### Why it matters
A clip can remain publicly misleading even after the replay itself is corrected.

### Authority
Product correction classes; DEC-188; Content & Media correction/supersession; CM-UPD-011.

### Owning domains
Content & Media plus the authority that requires the correction.

### Preconditions
- C1 publicly uses V1 segment S;
- material correction establishes S is wrong/misleading and V2 replaces it.

### Timeline
1. C1 is published.
2. Material correction activates V2.
3. C1 remains independently reachable unless remediated.

### Expected invariants
- C1 cannot remain current merely because it had earlier clip approval;
- current clip eligibility is re-evaluated against the correction;
- if affected, C1 is withdrawn or superseded by separately approved C2;
- historical C1 publication remains evidence.

### Questions
- Does source correction itself publish C2? No.
- Does prior clip approval transfer to C2? No automatic transfer for materially changed derivative.

### Adversarial variants
- correction changes one word in caption but not video audio;
- C1 is already embedded in multiple NewYou pages;
- C1 is scheduled for future campaign use.

### Analysis
Correction propagation must follow exact usage/lineage, not rely on operator memory.

### Disposition
`PASS_WITH_REFINEMENT / CLIP_REMEDIATION_REQUIRED`

### Proof route
`CM-UPD-011 → CONTENT_MEDIA_JIT → DERIVATIVE_USAGE/ATOMIC_WITHDRAWAL_OR_SUCCESSOR_PROOF`

### UPD
None.

### Evidence needed
Demonstrate stale affected C1 cannot survive current publication after the controlling correction activates.

---

## LIVE-PT-103 — Safety correction affects the clip excerpt

### Scenario class
Immediate safety withdrawal propagation.

### Why it matters
A short promotional clip can amplify unsafe guidance more broadly than the protected replay.

### Authority
Product safety-correction semantics; accepted Pass I; C&M withdrawal authority.

### Owning domains
Safety & Eligibility supplies/owns safety consequence as governed; Content & Media withdraws its publication truth.

### Preconditions
- C1 is public;
- safety authority invalidates guidance contained in C1;
- no corrected C2 is ready.

### Timeline
1. Safety correction becomes authoritative.
2. Replay affected use is withdrawn.
3. Clip C1 is still cached/embedded/published on NewYou-controlled surfaces.

### Expected invariants
- C1 current use is withdrawn immediately for controlled surfaces;
- lack of replacement cannot preserve C1;
- historical C1 evidence remains;
- provider/cache cleanup is consequence/proof, not authority.

### Questions
- Can clip remain because it is “only marketing”? No.
- Must a replacement clip exist before withdrawal? No.

### Adversarial variants
- C1 is the highest-performing acquisition asset;
- removal harms an active campaign;
- provider takedown is delayed.

Commercial inconvenience cannot override safety authority.

### Analysis
Safety propagation is stricter than ordinary material correction.

### Disposition
`PASS / IMMEDIATE_CLIP_WITHDRAWAL_REQUIRED`

### Proof route
`SAFETY AUTHORITY → CONTENT_MEDIA WITHDRAWAL → CONTROLLED_SURFACE/CACHE/PROVIDER PROOF`

### UPD
None.

### Evidence needed
Failure-injection proof that a known unsafe clip cannot remain authorised because purge/provider work is incomplete.

---

## LIVE-PT-104 — Replay expires or is withdrawn for a replay-only access/publication reason while clip remains independently valid

### Scenario class
Avoiding false inheritance in the other direction.

### Why it matters
Separate clip approval would be meaningless if every replay state change mechanically controlled the clip.

### Authority
Product §21G.15; Content & Media derivative lineage/independent permissions; Entitlements separation.

### Owning domains
Content & Media; Entitlements only for replay access.

### Preconditions
- C1 has independent current clip approval/right/purpose;
- source replay is withdrawn or expires for a reason confined to replay access/publication, not source safety/rights/consent affecting C1.

### Timeline
1. C1 and replay are current.
2. Replay entitlement/publication expires.
3. C1 remains separately eligible.

### Expected invariants
- replay expiry does not automatically withdraw C1;
- C1 remains traceably derived from its exact source version;
- any controlling rights/safety/consent change still propagates if applicable.

### Questions
- Is every replay withdrawal reason clip-relevant? No.
- Is every clip independent of source rights? Also no.

### Adversarial variants
- replay expiry is contractual access duration;
- replay withdrawn because programme cohort ended;
- replay route retired while media rights remain valid.

### Analysis
The controlling question is why the replay changed, not merely that its state changed.

### Disposition
`PASS_WITH_REFINEMENT / REASON_SCOPED_PROPAGATION`

### Proof route
`CONTENT_MEDIA_JIT + ENTITLEMENTS SEPARATION → IMPACT/ELIGIBILITY PROOF`

### UPD
None.

### Evidence needed
Show replay-only expiry does not destroy independently valid clip publication while rights-invalidating changes do propagate.

---

## LIVE-PT-105 — Promotional-purpose authority is withdrawn while replay-purpose authority remains

### Scenario class
Purpose-specific withdrawal.

### Why it matters
A participant may no longer permit public promotional use while replay use remains lawful/authorised.

### Authority
Architecture purpose-specific consent; OQ-021; accepted `LIVE-UPD-006`; accepted Pass F.

### Owning domains
Privacy & Consent; Content & Media executes clip publication consequence; replay C&M state is independently evaluated.

### Preconditions
- participant appears in C1 and replay R1;
- both purposes were valid;
- participant withdraws promotional-purpose authority only.

### Timeline
1. Withdrawal becomes current Privacy authority.
2. C1 is public.
3. R1 remains protected and otherwise valid.

### Expected invariants
- C1 current publication/use is invalidated for affected promotional purpose according to approved OQ-021 rule;
- R1 is not automatically withdrawn solely because promotional purpose ended;
- historical lawful C1 publication is not rewritten;
- dependent promotional derivatives/uses converge.

### Questions
- Exact remediation for multi-person C1? OQ-021/legal/ops.
- Does withdrawal require physical deletion? Separate retention/deletion question.

### Adversarial variants
- participant is only briefly visible;
- clip has already been republished in multiple controlled contexts;
- speaker contract may create another lawful basis.

### Analysis
This scenario is already anticipated by accepted `LIVE-UPD-006`; Pass J sharpens the clip consequence but does not create a new decision package.

### Disposition
`BLOCKED / OQ-021_PURPOSE_WITHDRAWAL_RULE`

### Proof route
`PRIVACY AUTHORITY → OQ-021 → CONTENT_MEDIA JIT → DEPENDENT_INVALIDATION PROOF`

### UPD
No new UPD; refine accepted `LIVE-UPD-006` evidence expectations only.

### Evidence needed
Approved purpose/role rule and propagation proof.

---

## LIVE-PT-106 — Speaker, guest, facilitator or attendee is selected for promotional clip use

### Scenario class
Role/context versus promotional rights.

### Why it matters
Provider `host`, `speaker` or `panelist` labels can tempt the system to infer promotional rights.

### Authority
Accepted Pass E; OQ-021; DEC-188; Domain ownership.

### Owning domains
Identity/Events supply role/context; Privacy supplies purpose authority; Content & Media owns clip publication.

### Preconditions
A captured person has one of several live-session roles.

### Timeline
1. Operator selects excerpt.
2. Provider reports role label.
3. Clip approval workflow evaluates source participant/context.

### Expected invariants
- provider role is evidence only;
- role may select an applicable policy but cannot itself create rights;
- staff/facilitator status is not blanket promotional permission;
- attendee-to-speaker transition does not retroactively authorise promotion.

### Questions
Exact role-specific contractual/lawful bases remain OQ-021/legal review.

### Adversarial variants
- founder/employee appears;
- practitioner participates;
- volunteer facilitator appears;
- attendee asks a question and is briefly on screen.

### Analysis
Role/context is an input to policy, not the policy outcome.

### Disposition
`BLOCKED / ROLE_SPECIFIC_OQ-021_RULE`

### Proof route
`OQ-021 + IDENTITY/EVENT CONTEXT → PRIVACY/C&M JIT → POLICY PROOF`

### UPD
None.

### Evidence needed
Role/context-aware clip approval without provider-role authority leakage.

---

## LIVE-PT-107 — Multi-person clip contains one person without valid promotional authority

### Scenario class
Mixed authority within one derivative.

### Why it matters
One valid speaker approval cannot manufacture authority over other visible/audible participants.

### Authority
Product attendee privacy/clip approval; OQ-021; accepted Pass E/F; C&M derivative rights.

### Owning domains
Privacy & Consent; Content & Media.

### Preconditions
- C1 contains several people;
- one or more have valid promotional authority;
- at least one affected person does not.

### Timeline
1. C1 is assembled.
2. Approval evaluates participants/surfaces.
3. Editor proposes cropping/muting/redaction to remove unauthorised contribution.

### Expected invariants
- C1 cannot publish in unauthorised form;
- others' permission cannot substitute;
- a modified C2 requires its own exact approval;
- technical separability is evidence, not authority to edit/use.

### Questions
- When is a person “affected” enough to require authority? OQ-021/legal/ops.
- Are incidental crowd/background appearances treated differently? Not decided here.

### Adversarial variants
- person is visible but inaudible;
- voice present but face absent;
- name appears in captions;
- third-party private information is visible on screen.

### Analysis
The pass cannot invent de minimis/legal thresholds. Fail closed where required authority cannot be established.

### Disposition
`BLOCKED / OQ-021_MULTI_PERSON_CLIP_RULE`

### Proof route
`OQ-021 → PRIVACY/C&M JIT → EXACT_SUBJECT/EDIT/APPROVAL PROOF`

### UPD
None.

### Evidence needed
Approved subject/surface rules and successor approval after edits.

---

## LIVE-PT-108 — Promotional clip derives directly from governed raw recording even though no replay is published

### Scenario class
Source lineage independent of replay publication.

### Why it matters
Forcing every clip to derive from a published replay would conflate media lineage with publication state and may create needless architecture.

### Authority
Architecture media lineage; Product separate clip approval; C&M media contract.

### Owning domains
Content & Media; Privacy/OQ-021 where rights apply.

### Preconditions
- governed recording MediaAssetVersion V1 exists;
- replay has not been published or may never be published;
- C1 is proposed from V1.

### Timeline
1. Provider/raw capture is adopted into governed NewYou media V1.
2. C1 derivative is created with V1 lineage.
3. C1 receives required purpose/right/content approval.
4. C1 is published independently.

### Expected invariants
- provider artifact alone is not sufficient source authority;
- replay publication is not required merely to establish clip lineage;
- C1 remains exact-version traceable;
- separate clip approval remains mandatory.

### Questions
Could Product/JIT later choose to require replay publication operationally? Possibly, but current law does not require it.

### Adversarial variants
- raw source contains long unapproved material;
- source recording is retained but replay is permanently withdrawn;
- clip is the only approved downstream use.

### Analysis
This preserves clean C&M semantics: derivative lineage follows media identity/version, not whichever publication happens to exist.

### Disposition
`PASS_WITH_REFINEMENT / CONTENT_MEDIA_JIT`

### Proof route
`C&M MEDIA LINEAGE → OQ-021/APPROVAL → PUBLICATION PROOF`

### UPD
None.

### Evidence needed
Exact governed source adoption and derivative lineage without replay-publication dependency.

---

## LIVE-PT-109 — Public promotional clip has been sent to an external social/provider channel when later correction or withdrawal occurs

### Scenario class
External/public distribution boundary.

### Why it matters
Once media is legitimately exposed publicly, provider copies, cached copies and user reshares may outlive NewYou's current publication state. The platform must not promise impossible universal recall or treat provider deletion as authoritative completion without evidence.

### Authority
Product correction/withdrawal and OQ-021; Architecture provider-evidence doctrine; C&M publication/withdrawal semantics; Pass G processor/reconciliation doctrine where a processor relationship applies.

### Owning domains
Content & Media owns NewYou clip publication truth; Privacy/Safety/legal authority may invalidate use; exact external-channel operational ownership is deferred to later authorised JIT/provider work.

### Preconditions
- C1 is lawfully published/promoted;
- an external platform/provider has a copy/post;
- later safety/legal/consent/material rule requires C1 withdrawal or correction.

### Timeline
1. NewYou current authority changes.
2. NewYou-controlled publication is withdrawn.
3. Takedown/update requests are sent where the external channel is controllable.
4. Provider outcome may be delayed, duplicated, ambiguous or incomplete.

### Expected invariants
- provider post existence never becomes NewYou current-publication authority;
- NewYou-controlled use stops according to the controlling correction/withdrawal class;
- provider acknowledgement is evidence, not automatic completion;
- unknown provider outcome remains unresolved where closure is required;
- no claim is made that NewYou can erase independent third-party reshares beyond its control;
- exact acceptable channel/takedown/recall obligations must come from approved legal/operations/provider policy.

### Questions
- Which social/provider channels are permitted for participant-containing clips? Not decided here.
- What evidence is legally/operationally sufficient after public dissemination? OQ-021/later provider JIT.
- Does FP-007 need this external distribution capability? No current Roadmap exit condition requires it.

### Adversarial variants
- provider API says deleted but public URL still resolves;
- user downloaded/reposted C1 independently;
- C1 was embedded by third-party sites;
- correction is safety-critical versus ordinary editorial.

### Analysis
This is a real operational boundary but not grounds for inventing a new FP-007 blocker today. Promotional clips are not required by the FP-007 Roadmap exit, and OQ-021 already explicitly owns clip/withdrawal rules. If a later Feature Pack or Final FP-007 Contract chooses external promotional distribution, the exact provider/takedown evidence contract must then be selected and proved.

### Disposition
`PASS_WITH_BOUNDARY / OPTIONAL_CAPABILITY_REQUIRES_LATER_CHANNEL_PROOF`

### Proof route
`OQ-021 + CONTENT_MEDIA JIT + APPLICABLE PROVIDER/CHANNEL JIT → RECONCILIATION PROOF`

### UPD
None.

### Evidence needed
Only if external promotional distribution is authorised: provider-specific update/takedown semantics, residual-publication checks, ambiguity/retry behaviour and truthful completion criteria.

---

# 6. Cross-test synthesis

## 6.1 Clip approval and source approval are deliberately independent

The safest semantic statement is:

```text
source recording/replay eligibility
+ exact derivative lineage
+ promotional-purpose/right authority
+ exact clip approval
+ clip publication eligibility
= current promotional clip publication
```

No single term can substitute for another.

## 6.2 Public audience is a purpose/risk expansion

Moving from protected replay to public promotional clip generally expands audience/purpose. That is why source replay permission cannot silently authorise the clip.

The system must not model public clip publication as merely “same replay, different route”.

## 6.3 Correction propagation is reason-scoped

A source version change requires explicit impact evaluation:

- ordinary unrelated correction may leave a clip valid;
- affected material correction may require clip successor/withdrawal;
- safety correction affecting the clip requires immediate current-use withdrawal;
- legal/consent/promotional-purpose invalidation routes through OQ-021 and Privacy authority;
- replay-only expiry/access change need not withdraw an independently approved public clip.

## 6.4 Clip lineage remains historical truth after source supersession

A clip created from V1 remains a V1 derivative even when V2 becomes current. It must not be relabelled to V2 to make provenance look current.

A corrected clip C2 should point to the exact source/version actually used for C2.

## 6.5 Clip edits create a new governed subject where materially changed

Cropping, muting, replacing captions, removing a participant or otherwise materially changing the governed clip creates successor media/version truth requiring applicable current approval. Editing is not an authority shortcut.

## 6.6 No new Domain is justified

Promotional clips do not justify a Marketing Domain or Clip Domain.

- Content & Media owns media derivative/publication truth;
- Privacy owns purpose authority;
- Events supplies source occurrence/participant context;
- Safety/legal/professional authority supplies corrections where applicable;
- Communications owns messages/preferences/delivery where a communication journey exists, not clip publication itself;
- provider/social state remains external evidence.

---

# 7. FP-007 scope adjudication

## 7.1 Promotional clips are not a Roadmap exit requirement

The current FP-007 exit condition names governed publish/register/join/record/replay, provider-failure reconciliation, audit, notification-failure visibility and stale-access safety.

It does not name promotional clips.

Therefore:

**Working classification:** `PRODUCT_AUTHORISED / FP007_EXIT_NOT_REQUIRED / GOVERNED_IF_INCLUDED`

This is not a new governed status vocabulary. It is a working scope statement for this discovery pack.

## 7.2 Consequence

A future FP-007 Final Feature Pack Contract must not accidentally pull promotional clips into the required scope simply because Product Law describes them.

If FP-007 excludes clips:

- the discovery seam remains reusable future evidence;
- OQ-021 clip rules need not be resolved solely for the stated FP-007 exit unless another included FP-007 behaviour depends on them;
- replay recording/consent rules under OQ-021 remain blocking as already established.

If FP-007 explicitly includes clips:

- OQ-021 clip-purpose/role/withdrawal rules become applicable to that included slice;
- separate C&M derivative approval/publication must be modelled;
- exact provider/channel proof applies only to selected publication channels.

This avoids both under-governance and scope creep.

---

# 8. UPD adjudication

## No LIVE-UPD-007

Pass J does not create a new upstream decision package.

Reasons:

1. Product §21G.15 already requires separate approval for promotional clips.
2. DEC-188 already includes clip approval in locked recording governance.
3. Architecture already makes consent/lawful basis purpose-specific.
4. OQ-021 explicitly owns speaker/attendee/recording/editing/replay/**clip**/retention/withdrawal rules.
5. Accepted `LIVE-UPD-006` already includes purpose-specific replay versus promotional-clip consequences after withdrawal.
6. Content & Media already owns derivative/publication/version truth and its working contract says derivative permissions do not auto-inherit.
7. Exact correction propagation belongs to existing Product correction classes plus C&M `CM-UPD-011`.
8. External distribution mechanics are optional/provider/JIT detail unless explicitly placed into an authorised Feature Pack.

Creating `LIVE-UPD-007` would duplicate existing authority rather than expose a missing Product decision.

---

# 9. Gap adjudication

## No LIVE-GAP-015

Pass J does not create a new gap identifier.

Existing routing is sufficient:

- `LIVE-GAP-003 — RECORDING_PRIVACY_GATE` already includes promotional-purpose/clip permission and withdrawal semantics under OQ-021;
- accepted `LIVE-UPD-006` owns post-capture purpose-withdrawal consequence framing;
- C&M `CM-UPD-006` already routes recording/edit/replay/clip rights/withdrawal to OQ-021;
- C&M `CM-UPD-011` owns correction impact/severity → downstream remediation mapping;
- C&M media JIT owns derivative identity/version/lineage/publication topology;
- `LIVE-GAP-014` remains processor deletion/non-resurrection and should not be overloaded with ordinary public clip takedown;
- exact external social/provider distribution is not required by FP-007 exit and should be opened only if a governed Feature Pack includes it.

A new gap would be identifier creep without a new owner/problem class.

---

# 10. Evidence register

No `LIVE-EV-*` item is added by Pass J.

Later executable evidence should cover, **only where the selected Feature Pack includes promotional clips**:

- no clip publication without separate exact-version approval;
- purpose-specific promotional authority independent of replay authority;
- public clip does not leak protected replay access;
- exact source MediaAssetVersion lineage;
- source-correction impact evaluation;
- immediate affected-clip withdrawal for safety/legal/consent classes;
- purpose-only withdrawal leaves unrelated replay truth intact where valid;
- mixed-participant fail-closed behaviour;
- clip successor approval after material edits;
- provider/channel reconciliation if external distribution is actually selected.

---

# 11. Proposed Pass-J working conclusions

1. **A promotional clip is not a shorter replay.** It is a separately governed derivative/publication subject.
2. **Separate clip approval is mandatory under existing Product Law.** Replay/source approval cannot substitute.
3. **Promotional/public-use authority is purpose-specific.** Recording or replay authority does not automatically permit promotion.
4. **Derivative permissions do not auto-inherit from source permissions.** Existing C&M working doctrine supports this boundary.
5. **A public clip may validly derive from a protected replay without exposing replay entitlement, provided the clip has independent current approval/rights and bounded media delivery.**
6. **Replay publication is not inherently a prerequisite for clip publication.** Governed exact media source lineage is the prerequisite; provider raw artifact alone is not.
7. **Source correction/withdrawal propagates by reason and exact affected lineage, not by blanket cascade or blanket immunity.**
8. **Affected safety correction withdraws the clip immediately; replacement readiness is irrelevant to continued unsafe use.**
9. **Promotional-purpose withdrawal can invalidate a clip while replay remains valid.** Exact remediation remains OQ-021-dependent.
10. **Replay-only expiry/withdrawal does not automatically invalidate an independently approved clip when the controlling source rights/safety/consent remain valid.**
11. **Role labels do not create promotional rights.** Speaker/guest/staff/attendee context selects policy; provider role remains evidence only.
12. **One participant's authority cannot manufacture another participant's clip authority.** Multi-person clip rules remain OQ-021-dependent.
13. **Historical clip lineage/publication is preserved when current clip use is withdrawn or superseded.**
14. **External public distribution has a real recall/reconciliation boundary, but exact channel obligations are later legal/operations/provider work, not a new FP-007 Product gap.**
15. **Promotional clips are not required by the current FP-007 Roadmap exit condition.** They are Product-authorised and governed if explicitly included, but discovery must not silently expand FP-007 scope.
16. **No `LIVE-UPD-007` is justified.**
17. **No `LIVE-GAP-015` is justified.**

---

# 12. Explicit non-decisions preserved

Pass J does **not** decide:

- whether promotional clips will be included in the eventual FP-007 Final Feature Pack Contract;
- which social/public channels are approved;
- paid versus organic campaign rules;
- exact speaker/attendee release language;
- exact threshold for incidental/background appearance;
- legal sufficiency of any clip consent/release model;
- exact clip duration/aspect-ratio/branding/watermark rules;
- exact editing/redaction technology;
- exact external-platform takedown SLA;
- whether provider/social channels act as processors/controllers under applicable law;
- participant communication wording/timing/channel;
- marketing attribution/analytics;
- exact Ash Resources/actions/workers/storage topology;
- exact retention/deletion schedules.

---

# 13. Pass-J proposed outcome

**Outcome:** `PASS`

The current authority stack is sufficient to constrain promotional clips without a new Product amendment or gap identifier. The main new planning result is a **scope correction**: clips are governed Product capability but are not required by the current FP-007 Roadmap exit condition.

Remaining uncertainty is correctly routed to:

- OQ-021 for role/purpose/clip/withdrawal rules;
- accepted `LIVE-UPD-006` for post-capture purpose withdrawal framing;
- Content & Media derivative/publication/version JIT;
- C&M `CM-UPD-011` for correction-impact remediation;
- selected provider/channel proof only if external promotional distribution is actually included.

---

# 14. Proposed next focused pass

Only after Pass J acceptance:

> **Participant communications around live/replay lifecycle events — registration/join changes, cancellation/reschedule, recording/replay availability, correction/withdrawal and delivery failure visibility — without reopening generic Communications architecture.**

The next pass should distinguish:

- authoritative event/replay fact versus Communications delivery evidence;
- which participant-facing journeys are Product promises versus optional operations;
- cancellation/reschedule and join-instruction change notifications;
- replay-ready/replay-withdrawn/corrected-replay notifications;
- recording/privacy-policy change communication;
- notification failure visibility and retry/reconciliation;
- duplicate/reordered message-provider callbacks;
- stale message content versus current occurrence/replay truth;
- opt-out/purpose rules where a message is operational rather than marketing.

It must reuse current Communications, Privacy and event-owner doctrine and must not let message delivery become event/replay authority.
