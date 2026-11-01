# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.8.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PROPOSED REGISTER SUCCESSOR
- **Document version:** v0.8.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.7.1.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted predecessor commit:** `0eed5028af0f16209cacbcf595ae679b9ab6e180`
- **Pass J discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.10.0.md`
- **Pass J discovery commit:** `3884617930da5eba42505085a1b414ff1aca4748`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic rule:** Passes A–I remain `ACCEPTED_WORKING_LOCK`. Pass-J additions below remain `PROPOSED / AWAITING_USER_ACCEPTANCE` until explicitly accepted.

---

# 1. Cumulative state

Accepted working lock currently covers:

- Passes A–I / discovery v0.1.0 through v0.9.0;
- `LIVE-PT-001...LIVE-PT-097`;
- `LIVE-UPD-001...LIVE-UPD-006`, with no `LIVE-UPD-007`;
- `LIVE-GAP-001...LIVE-GAP-014`, with no `LIVE-GAP-015`;
- no `LIVE-EV-*` entries.

Pass J adds proposed promotional-clip semantics and one important FP-007 scope adjudication only. It does not reopen accepted replay correction, withdrawal, Full Deletion, provider deletion, occurrence or attendance conclusions.

---

# 2. Pass register addition

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| J | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.10.0.md` | `3884617930da5eba42505085a1b414ff1aca4748` | promotional clips: separate approval, public/promotional purpose, rights, source lineage, correction/withdrawal propagation | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

---

# 3. Proposed Pass-J working conclusions

1. **A promotional clip is not a shorter replay.** It is a separately governed derivative/publication subject.
2. **Separate clip approval is mandatory under existing Product Law.** Replay/source approval cannot substitute.
3. **Promotional/public-use authority is purpose-specific.** Recording or replay authority does not automatically permit promotion.
4. **Derivative permissions do not auto-inherit from source permissions.** Existing C&M working doctrine supports this boundary.
5. **A public clip may validly derive from a protected replay without exposing replay entitlement**, provided the clip has independent current approval/rights and bounded delivery.
6. **Replay publication is not inherently a prerequisite for clip publication.** Governed exact media source lineage is the prerequisite; provider raw artifact alone is not.
7. **Source correction/withdrawal propagates by reason and exact affected lineage, not by blanket cascade or blanket immunity.**
8. **Affected safety correction withdraws the clip immediately.** Replacement readiness is irrelevant to continued unsafe use.
9. **Promotional-purpose withdrawal can invalidate a clip while replay remains valid.** Exact remediation remains OQ-021-dependent.
10. **Replay-only expiry/withdrawal does not automatically invalidate an independently approved clip when controlling rights/safety/consent remain valid.**
11. **Role labels do not create promotional rights.** Speaker/guest/staff/attendee context selects policy; provider role remains evidence only.
12. **One participant's authority cannot manufacture another participant's clip authority.** Multi-person clip rules remain OQ-021-dependent.
13. **Historical clip lineage/publication is preserved when current clip use is withdrawn or superseded.**
14. **External public distribution has a real recall/reconciliation boundary**, but exact channel obligations are later legal/operations/provider work, not a new FP-007 Product gap.
15. **Promotional clips are not required by the current FP-007 Roadmap exit condition.** They are Product-authorised and governed if explicitly included, but discovery must not silently expand FP-007 scope.
16. **No `LIVE-UPD-007` is justified.**
17. **No `LIVE-GAP-015` is justified.**

These conclusions remain proposed until accepted.

---

# 4. Pressure-test additions

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-098` | Clip bytes exist but no separate promotional-clip approval | v0.10.0 | `PASS / FAIL_CLOSED_BY_EXISTING_PRODUCT_LAW` | `PRODUCT §21G.15 + DEC-188 → CONTENT_MEDIA_JIT → APPROVAL/PUBLICATION_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-099` | Separately approved public clip derived from entitlement-protected replay | v0.10.0 | `PASS_WITH_REFINEMENT / CONTENT_MEDIA_JIT_AND_ACCESS_PROOF` | `C&M JIT → ENTITLEMENTS/DELIVERY BOUNDARY → SECURITY PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-100` | Replay permission exists but promotional-purpose authority does not | v0.10.0 | `BLOCKED / OQ-021_PROMOTIONAL_PURPOSE_RULE_REQUIRED` | `OQ-021 + PRIVACY JIT → C&M JIT → PURPOSE/PUBLICATION PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-101` | Source replay material correction is outside clip excerpt | v0.10.0 | `PASS_WITH_REFINEMENT / CM-UPD-011_IMPACT_EVALUATION` | `PRODUCT CORRECTION CLASS → CM-UPD-011 / C&M JIT → LINEAGE/IMPACT PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-102` | Source material correction directly affects approved clip excerpt | v0.10.0 | `PASS_WITH_REFINEMENT / CLIP_REMEDIATION_REQUIRED` | `CM-UPD-011 → C&M JIT → DERIVATIVE_USAGE/ATOMIC_WITHDRAWAL_OR_SUCCESSOR_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-103` | Safety correction affects public clip excerpt | v0.10.0 | `PASS / IMMEDIATE_CLIP_WITHDRAWAL_REQUIRED` | `SAFETY AUTHORITY → C&M WITHDRAWAL → CONTROLLED_SURFACE/CACHE/PROVIDER PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-104` | Replay expires/withdraws for replay-only reason while clip remains independently valid | v0.10.0 | `PASS_WITH_REFINEMENT / REASON_SCOPED_PROPAGATION` | `C&M JIT + ENTITLEMENTS SEPARATION → IMPACT/ELIGIBILITY PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-105` | Promotional-purpose authority withdrawn while replay-purpose authority remains | v0.10.0 | `BLOCKED / OQ-021_PURPOSE_WITHDRAWAL_RULE` | `PRIVACY AUTHORITY → OQ-021 → C&M JIT → DEPENDENT_INVALIDATION PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-106` | Speaker/guest/facilitator/attendee selected for promotional clip use | v0.10.0 | `BLOCKED / ROLE_SPECIFIC_OQ-021_RULE` | `OQ-021 + IDENTITY/EVENT CONTEXT → PRIVACY/C&M JIT → POLICY PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-107` | Multi-person clip includes one person without valid promotional authority | v0.10.0 | `BLOCKED / OQ-021_MULTI_PERSON_CLIP_RULE` | `OQ-021 → PRIVACY/C&M JIT → EXACT_SUBJECT/EDIT/APPROVAL PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-108` | Clip derives directly from governed raw recording while no replay is published | v0.10.0 | `PASS_WITH_REFINEMENT / CONTENT_MEDIA_JIT` | `C&M MEDIA LINEAGE → OQ-021/APPROVAL → PUBLICATION PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-109` | Public clip exists on external channel when later correction/withdrawal occurs | v0.10.0 | `PASS_WITH_BOUNDARY / OPTIONAL_CAPABILITY_REQUIRES_LATER_CHANNEL_PROOF` | `OQ-021 + C&M JIT + APPLICABLE PROVIDER/CHANNEL JIT → RECONCILIATION PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Detailed timelines, invariants, adversarial variants, questions and evidence needs remain in discovery v0.10.0.

---

# 5. FP-007 scope adjudication

## Promotional clips are not a current FP-007 Roadmap exit requirement

The authoritative FP-007 exit condition requires governed session publish/register/join/record/replay, provider-failure reconciliation, audit, notification-failure visibility and protected-playback stale-access safety.

It does not require promotional clips.

Working discovery classification:

`PRODUCT_AUTHORISED / FP007_EXIT_NOT_REQUIRED / GOVERNED_IF_INCLUDED`

This is a planning statement, not a new governed status vocabulary.

Consequences:

- do not silently add clips to FP-007 required scope;
- if the future Final Feature Pack Contract excludes clips, the clip discovery remains reusable future evidence and clip-specific OQ-021 resolution need not be pulled in solely for FP-007 completion;
- if clips are explicitly included, applicable OQ-021 clip rules, C&M derivative approval/publication and selected provider/channel proof become required for that included slice.

---

# 6. UPD register adjudication

## No LIVE-UPD-007

No new upstream decision package is proposed because Product §21G.15, DEC-188, purpose-specific consent Architecture, OQ-021, accepted `LIVE-UPD-006`, C&M derivative/publication doctrine and `CM-UPD-011` already own the semantic questions.

Creating a new Live UPD would duplicate existing authority/routing.

---

# 7. Gap-register adjudication

## No LIVE-GAP-015

No new gap identifier is proposed.

Existing routing remains sufficient:

- `LIVE-GAP-003 — RECORDING_PRIVACY_GATE` for clip-purpose/participant/withdrawal semantics under OQ-021;
- accepted `LIVE-UPD-006` for post-capture purpose-withdrawal framing;
- C&M `CM-UPD-006` for recording/edit/replay/clip rights/withdrawal;
- C&M `CM-UPD-011` for correction-impact remediation;
- C&M JIT for derivative identity/version/lineage/publication;
- selected provider/channel proof only if external promotional distribution is actually authorised.

`LIVE-GAP-014` remains processor deletion/non-resurrection and is not overloaded with ordinary clip takedown.

---

# 8. Evidence register

No `LIVE-EV-*` item is added by Pass J.

Later executable evidence is conditional on promotional clips actually being included in a governed Feature Pack slice.

---

# 9. Explicit non-decisions preserved

Pass J does not decide whether clips enter FP-007 Final Contract, approved social/public channels, paid/organic campaign rules, release wording, incidental/background-person thresholds, legal sufficiency, clip duration/format/branding, editing technology, external-platform takedown SLAs, processor/controller classification, participant communications, attribution analytics, retention schedules or implementation topology.

---

# 10. Pass-J proposed outcome

**Outcome:** `PASS`

Current authority is sufficient to constrain promotional clips without a new Product amendment or gap identifier. The important new planning result is the FP-007 scope correction: clips are governed Product capability but not a required Roadmap exit outcome.

---

# 11. Acceptance transition rule

If Pass J is accepted without semantic changes, create non-semantic status successor `v0.8.1` promoting:

- Pass J;
- `LIVE-PT-098...LIVE-PT-109`;
- the §3 Pass-J conclusions;
- the FP-007 scope adjudication;
- the decision that no `LIVE-UPD-007` is warranted;
- the decision that no `LIVE-GAP-015` is warranted;

to `ACCEPTED_WORKING_LOCK`.

If semantic changes are requested, create a substantive successor and preserve this v0.8.0 unchanged.

---

# 12. Proposed next focused pass

Only after Pass J acceptance:

> **Participant communications around live/replay lifecycle events — registration/join changes, cancellation/reschedule, recording/replay availability, correction/withdrawal and delivery failure visibility — without reopening generic Communications architecture.**

The next pass should keep source event/replay truth separate from Communications intent/delivery/provider evidence and determine which participant-facing journeys are actual Product promises versus optional operations.
