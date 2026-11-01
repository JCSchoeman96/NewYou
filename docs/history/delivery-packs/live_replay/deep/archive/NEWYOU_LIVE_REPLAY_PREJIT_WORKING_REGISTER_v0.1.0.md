# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.1.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / ACCEPTED-DISCOVERY REGISTER
- **Document version:** v0.1.0
- **Date:** 2026-10-09
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Register baseline head:** `2d64f290a261826b70984cf3f0d61699db0ab631`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Purpose:** provide one cumulative working register for accepted Pre-JIT discovery conclusions, pressure tests, upstream-delta candidates, gaps, evidence and explicit deferrals without replacing the detailed versioned discovery ledgers or creating a shadow authority layer.

---

# 1. Governance role of this register

This file exists because the Live & Replay discovery is intentionally proceeding in small focused passes. The detailed pass ledgers preserve full reasoning; this register provides the stable cumulative index and working lock.

The governing distinction is:

> **accepted working conclusion != frozen Product/Architecture/Domain/Roadmap law**

A conclusion marked `ACCEPTED_WORKING_LOCK` means the discovery stream has reviewed and accepted it as the current working position. It should not be casually reopened or silently rewritten in later passes. It can still be superseded by:

1. newer higher-authority Product, Architecture, Domain or Roadmap law;
2. new empirical evidence that materially contradicts it;
3. a later focused pressure test that exposes a real contradiction;
4. explicit user-directed reconsideration.

If superseded, a successor register must say exactly what changed and why. Historical register versions remain preserved.

This register must **not**:

- create `DEC-*`, `ARC-*`, `ARQ-*`, Feature Pack law or Domain Law;
- convert a `LIVE-UPD-*` working candidate into authority;
- convert provider evidence into business truth;
- claim that an unresolved privacy/legal/provider gate has been resolved;
- authorise implementation.

The detailed discovery ledgers remain the reasoning source for each item:

- `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.1.0.md`
- `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.2.0.md`
- `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.3.0.md`

---

# 2. Accepted pass register

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| A | `...DISCOVERY_WORKING_v0.1.0.md` | `208b74de408a2a94b9b1942fc8d4e7dc44b54ad9` | authority baseline, truth separation, first ordinary lifecycle/adversarial cases | `ACCEPTED_WORKING_LOCK` |
| B | `...DISCOVERY_WORKING_v0.2.0.md` | `38cc76b1ba24b5eee2c5319c0a9ead4a560d0f82` | occurrence identity, schedule/version, execution outcome, registration/access/attendance seams | `ACCEPTED_WORKING_LOCK` |
| C | `...DISCOVERY_WORKING_v0.3.0.md` | `2d64f290a261826b70984cf3f0d61699db0ab631` | recording intent and raw capture boundary only | `ACCEPTED_WORKING_LOCK` |

The accepted passes are cumulative. A later pass does not erase an earlier accepted conclusion unless it names the supersession explicitly.

---

# 3. Accepted working conclusions

The following are locked as the current working semantic position for this discovery stream.

## 3.1 Authority and truth separation

1. NewYou occurrence truth remains Events & Live authority; provider meeting/stream objects and provider status do not become occurrence truth.
2. Registration, entitlement/access, issued join capability, live presence, authoritative attendance, recording/capture, replay publication, replay entitlement and replay consumption are independent facts.
3. Entitlements owns general current access; Events & Live owns occurrence registration/attendance and later event-specific ticket/admission truth where applicable.
4. Content & Media owns governed media identity, rights, lineage, derivatives and publication; Events & Live retains the occurrence recording notice/association context.
5. Privacy & Consent owns purpose-specific consent/current consent and deletion/retention orchestration; attendance or registration never silently substitutes for recording permission.
6. Communications owns message intent/delivery evidence, not occurrence/access truth.
7. Analytics is derived and rebuildable; it does not become attendance, entitlement or replay authority.
8. Audit & Evidence records restricted append-only evidence where required and never becomes a competing source-domain authority.

## 3.2 Occurrence and provider identity

9. A NewYou occurrence identity must remain independent of provider room/stream/resource identity.
10. Provider resource replacement, recreation or stream-key rotation does not by itself create a new NewYou occurrence.
11. Schedule/announcement version, actual execution outcome, provider binding, registration, attendance, recording association and replay publication must not be collapsed into one giant lifecycle/status.
12. Historical schedule meaning must remain explainable after reschedule or correction; participant-local rendering is derived presentation.
13. Provider duplicate resources after timeout/retry cannot multiply NewYou occurrence identity.
14. Genuine duplicate NewYou occurrences require explicit governed correction/supersession semantics; destructive row merge is not an acceptable default.

## 3.3 Registration, access and attendance

15. Registration is intent/occurrence relationship, not current entitlement and not attendance.
16. Current access must be checked from owning authority; stale provider/native links cannot restore a revoked/expired right.
17. Admission and ongoing in-session delivery continuity are separate Product questions; provider persistence or token TTL must not silently decide the latter.
18. Attendance requires a Product-defined assurance/evidence model rather than a provider-row boolean.
19. Multiple devices/reconnects must not create multiple participant attendance facts.
20. Missing provider evidence does not automatically prove `no_show`.
21. Weak-identity/public viewing cannot silently become named participant attendance.
22. Provider email/display identity is evidence, not canonical NewYou identity.
23. Manual attendance correction, if Product permits it, must be explicit, attributed, scoped and historically explainable.
24. Purchaser, beneficiary/recipient and participant identity remain distinct.
25. Commercial reversal may change current rights but does not erase historical attendance/delivery truth.
26. Ordinary FP-007 must not absorb scarce-event hold/ticket/refund/seat-transfer/flash-sale mechanics from later event commerce.

## 3.4 Recording and raw capture

27. Recording intent, provider capture outcome and media publication are three independent facts.
28. Provider capture existence cannot retroactively create NewYou recording intent or lawful publication authority.
29. A provider recording object remains external evidence/artifact until NewYou deliberately adopts it into governed media handling.
30. Provider object identity never becomes NewYou media identity by default.
31. One occurrence may have zero, one or many raw capture artifacts; a one-occurrence/one-provider-recording assumption is rejected.
32. Provider restart/resource replacement may yield multiple capture segments while the NewYou occurrence remains one.
33. Capture existence/provider `ready` or `completed` state does not prove semantic completeness, technical usability, editorial acceptance or replay publication.
34. Late-starting, early-ending, corrupt, missing-audio/video and wrong-source captures must remain distinguishable from a usable full recording.
35. Concatenating/composing multiple capture segments is governed Content & Media editing, not automatic ingestion truth.
36. Capture-finalisation callbacks/status may be duplicate, delayed or reordered; arrival order cannot manufacture media finality or duplicate platform media identity.
37. Accidental capture when NewYou recording intent is false fails closed. The bytes cannot be relabelled as an ordinary authorised recording merely for operational convenience.
38. The current Product/Domain/Architecture ownership boundary is sufficient for raw-capture ownership. Pass C therefore deliberately created **no `LIVE-UPD-005`**.

---

# 4. Pressure-test register

`Acceptance` below means the pressure-test conclusion is accepted as working discovery evidence. It does not mean every unresolved question in the test is resolved.

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-001` | Ordinary live-to-replay journey | v0.1.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-002` | Provider creates exactly one room for one NewYou occurrence | v0.1.0 | `PASS_WITH_REFINEMENT` | `JIT` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-003` | Duplicate provider rooms after ambiguous create | v0.1.0 | `PASS_WITH_REFINEMENT` | `PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-004` | Registered participant whose entitlement expires before join | v0.1.0 | `PASS_WITH_REFINEMENT` | `PHASE8_EXECUTABLE` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-005` | Registered no-show versus joined participant | v0.1.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-006` | Five-second join, reconnects and two devices | v0.1.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-007` | Provider reports attendance late, then corrects it | v0.1.0 | `NEEDS_WORKING_DELTA` | `JIT` after Product meaning | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-008` | Recording exists but replay is not yet governed | v0.1.0 | `PASS_WITH_REFINEMENT` | `JIT` + OQ-020/OQ-021 | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-009` | Participant never saw recording notice | v0.1.0 | `INSUFFICIENT_AUTHORITY` | `LEGAL_PRIVACY_REVIEW` / OQ-021 | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-010` | Live right ends but replay right may differ | v0.1.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-011` | Leaked replay URL after entitlement revocation | v0.1.0 | `PASS_WITH_REFINEMENT` | `PROVIDER_EMPIRICAL` + executable proof | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-012` | Reschedule after registration and sent join details | v0.1.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-013` | Draft → scheduled → published → started → completed ordinary occurrence | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-014` | Published occurrence is rescheduled after registration | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-015` | Timezone and daylight-saving rendering | v0.2.0 | `PASS_WITH_REFINEMENT` | `JIT` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-016` | Delayed start, overrun and early end | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-017` | Cancelled before start, cancelled after start, abandoned and emergency termination | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-018` | Provider room replacement without occurrence replacement | v0.2.0 | `PASS_WITH_REFINEMENT` | `JIT` + OQ-020 | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-019` | Stream key rotates, provider room stays the same | v0.2.0 | `PASS` | `PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-020` | Entitled participant when registration is required but missing | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-021` | Joined but not registered through a forwarded provider link | v0.2.0 | `PASS_WITH_REFINEMENT` | `PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-022` | Entitlement expires or is revoked during the live session | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-023` | Refund/reversal before live versus after attendance | v0.2.0 | `PASS` | `JIT` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-024` | Purchaser is not participant | v0.2.0 | `PASS` | `JIT` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-025` | Free/public occurrence with weak participant identity | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-026` | Provider email does not match NewYou account email | v0.2.0 | `PASS_WITH_REFINEMENT` | `PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-027` | Facilitator manually confirms attendance when provider evidence is missing | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-028` | Registration cancelled before a non-scarce live session | v0.2.0 | `DEFER_NOT_PREJIT` | Feature Pack/JIT scope | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-029` | Staff accidentally creates two NewYou occurrences for one intended session | v0.2.0 | `NEEDS_WORKING_DELTA` | `PRODUCT_DECISION_PROMOTION` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-030` | Historical session remains true after replay withdrawal | v0.2.0 | `PASS_WITH_REFINEMENT` | `JIT` + applicable privacy/processor gates | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-031` | Recording intended and one complete provider capture succeeds | v0.3.0 | `PASS_WITH_REFINEMENT` | `JIT + PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-032` | Recording intended but provider capture never starts | v0.3.0 | `PASS_WITH_REFINEMENT` | `PROVIDER_EMPIRICAL + JIT` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-033` | Provider capture starts late or stops early | v0.3.0 | `PASS_WITH_REFINEMENT` | `JIT + PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-034` | Provider restart creates multiple raw capture segments | v0.3.0 | `PASS` | `JIT + PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-035` | Provider produces a corrupt or technically unusable capture | v0.3.0 | `PASS_WITH_REFINEMENT` | `JIT + PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-036` | Provider records despite NewYou recording intent being false | v0.3.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 + LATER_FOCUSED_PRIVACY_PASS` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-037` | Capture-finalisation callbacks are duplicated, delayed or reordered | v0.3.0 | `PASS` | `PROVIDER_EMPIRICAL + CONTROLLED_LIVE_PROOF` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-038` | Provider resource replacement yields recordings from both old and new resources | v0.3.0 | `PASS_WITH_REFINEMENT` | `JIT + PROVIDER_EMPIRICAL` | `ACCEPTED_WORKING_LOCK` |
| `LIVE-PT-039` | Recording intent changes immediately before or during live execution | v0.3.0 | `BLOCKED / DEFER_TO_NOTICE_AND_CONSENT_PASS` | `OQ-021 + PRODUCT/PRIVACY_ADJUDICATION` | `ACCEPTED_WORKING_LOCK` |

---

# 5. Upstream-delta candidate register

These are **working candidates only**. They identify semantic decisions JIT must not invent. They are not current Product or Domain authority.

| ID | Working candidate | Origin / reinforcement | Current status |
|---|---|---|---|
| `LIVE-UPD-001` | Stable NewYou occurrence identity plus schedule/execution/correction/supersession semantics independent of provider resources | PT-002/003; strongly reinforced by PT-012–018 and PT-029 | `OPEN / ACCEPTED_WORKING_CANDIDATE` |
| `LIVE-UPD-002` | Product-defined attendance meaning, assurance, correction/finality and provider-evidence relationship | PT-005/006/007; reinforced by PT-025–027 | `OPEN / ACCEPTED_WORKING_CANDIDATE` |
| `LIVE-UPD-003` | Explicit live-right versus replay-right semantics by product/access source | PT-010; related PT-004/011/023/030 | `OPEN / ACCEPTED_WORKING_CANDIDATE` |
| `LIVE-UPD-004` | In-progress live-access continuity/revocation semantics independent of initial admission | PT-022 | `OPEN / ACCEPTED_WORKING_CANDIDATE` |

**Reserved fact:** no `LIVE-UPD-005` exists as of accepted Pass C. Pass C explicitly found that no new upstream ownership rule was justified for the raw-capture boundary.

---

# 6. Gap register

| ID | Gap | Classification | Current routing/status |
|---|---|---|---|
| `LIVE-GAP-001` | Complete occurrence lifecycle and schedule-version semantics | `PRODUCT_AUTHORITY_GAP` | open; principally represented by `LIVE-UPD-001` |
| `LIVE-GAP-002` | Provider/live path empirical validation | `PROVIDER_EMPIRICAL_GATE` | open under `OQ-020` |
| `LIVE-GAP-003` | Recording consent/retention/deletion rules | `RECORDING_PRIVACY_GATE` | open under `OQ-021`; refined by PT-036/PT-039, not duplicated |
| `LIVE-GAP-004` | Attendance business meaning | `PRODUCT_AUTHORITY_GAP` | open; principally represented by `LIVE-UPD-002` |
| `LIVE-GAP-005` | Replay-right policy across product/access sources | `PRODUCT_AUTHORITY_GAP` | open; principally represented by `LIVE-UPD-003` |
| `LIVE-GAP-006` | Promised live communications | `COMMUNICATIONS_GATE` | open where promised journey depends on `OQ-036` |
| `LIVE-GAP-007` | Scarce event commerce | `FUTURE_EVENT_COMMERCE` | intentionally outside FP-007 / later FP-015 |
| `LIVE-GAP-008` | In-progress access continuity | `PRODUCT_AUTHORITY_GAP` | open; represented by `LIVE-UPD-004` |
| `LIVE-GAP-009` | Registration requirement and cancellation semantics | `PRODUCT_AUTHORITY_GAP` | open; do not import ticket mechanics |
| `LIVE-GAP-010` | Weak-identity/public live attendance | `PRODUCT_AUTHORITY_GAP` | open; part of attendance-assurance decision |
| `LIVE-GAP-011` | Provider capture lifecycle/finalisation semantics are unverified | `PROVIDER_EMPIRICAL_GATE` | open under `OQ-020` |
| `LIVE-GAP-012` | Exact external-capture → governed-media adoption mechanism | `JIT_ONLY` | downstream after semantics/provider evidence; no new Domain implied |

---

# 7. Evidence register

No `LIVE-EV-*` entries exist yet.

That is intentional. Provider research has been withheld until NewYou semantic invariants are explicit enough to test provider capabilities against them rather than allowing provider behaviour to define Product meaning.

When provider research begins, every material external fact must be recorded as `LIVE-EV-###` with:

- source/provider;
- first-party URL/document;
- access/retrieval date;
- exact factual claim;
- whether documentation or controlled observation supports it;
- affected PT/gap;
- confidence/limits;
- whether the fact is capability evidence only or a blocker to the proposed provider path.

Provider evidence can close empirical uncertainty. It cannot promote itself into Product/Domain authority.

---

# 8. Explicitly deferred / out of current lock

The following are **not decided** by accepted Passes A–C:

- exact occurrence state enum/resource/schema;
- exact attendance threshold/duration rule;
- exact manual attendance-evidence hierarchy;
- exact registration-required/optional/absent matrix;
- in-progress revocation/grace rule;
- live-versus-replay entitlement matrix;
- recording notice/acknowledgement/consent-at-join model;
- late-join recording permission model;
- presenter/speaker/guest/staff recording permission distinctions;
- consent withdrawal after capture;
- one participant withdrawing from a multi-person recording;
- retention durations;
- Full Deletion and external-processor deletion;
- replay publication/replacement/correction/withdrawal semantics beyond already-frozen general media law;
- promotional clip approval mechanism;
- exact Restream/Cloudflare APIs/callbacks/configuration;
- live notification provider/channel policy;
- scarce event-commerce mechanics;
- any Ash Resource/table/index/job/provider-adapter design.

---

# 9. Register update rule

For each later focused pass:

1. write the append-only detailed discovery successor first;
2. record new PTs/gaps/UPDs/evidence in a **new register successor**;
3. mark the new pass `PROPOSED / AWAITING_USER_ACCEPTANCE` until the user accepts it;
4. on acceptance, use a non-semantic status patch if semantics are unchanged, or a substantive register successor if the user requests changes;
5. never rewrite this v0.1.0 register in place.

The register SemVer convention is:

- `v0.N.0` — new substantive discovery/pass information added;
- `v0.N.P` — status/provenance/non-semantic correction only;
- predecessors remain preserved.

---

# 10. Current stop point

Accepted discovery is locked through **Pass C / v0.3.0**.

The next focused pass is:

> **Recording notice and consent at admission/join, including late join, without yet addressing withdrawal/deletion/retention.**

That pass may refine `LIVE-GAP-003` and may create a new `LIVE-UPD-*` only if the pressure tests demonstrate a consequential semantic decision that current Product/Privacy authority and OQ-021 framing do not already resolve.
