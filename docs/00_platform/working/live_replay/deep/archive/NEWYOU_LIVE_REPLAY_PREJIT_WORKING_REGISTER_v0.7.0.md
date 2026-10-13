# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.7.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PROPOSED REGISTER SUCCESSOR
- **Document version:** v0.7.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.6.1.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted predecessor commit:** `e9d42dcf082b173264e39e8648add359fb0531a1`
- **Pass I discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.9.0.md`
- **Pass I discovery commit:** `bd1d5986dd60021b1ae90130eba3c33f4e84cb1d`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic rule:** Passes A–H remain `ACCEPTED_WORKING_LOCK`. Pass-I additions below remain `PROPOSED / AWAITING_USER_ACCEPTANCE` until explicitly accepted.

---

# 1. Cumulative state

Accepted working lock currently covers:

- Pass A / discovery v0.1.0;
- Pass B / discovery v0.2.0;
- Pass C / discovery v0.3.0;
- Pass D / discovery v0.4.0;
- Pass E / discovery v0.5.0;
- Pass F / discovery v0.6.0;
- Pass G / discovery v0.7.0;
- Pass H / discovery v0.8.0;
- `LIVE-PT-001...LIVE-PT-086`;
- `LIVE-UPD-001...LIVE-UPD-006`, with no `LIVE-UPD-007`;
- `LIVE-GAP-001...LIVE-GAP-014`, with no `LIVE-GAP-015`;
- no `LIVE-EV-*` entries.

Pass I adds proposed post-publication replay correction/version-history findings only. It does not reopen accepted occurrence, attendance, consent-withdrawal, retention, processor-deletion or Full-Deletion conclusions.

---

# 2. Pass register addition

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| I | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.9.0.md` | `bd1d5986dd60021b1ae90130eba3c33f4e84cb1d` | replay correction, replacement, withdrawal and version history after publication | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

---

# 3. Proposed Pass-I working conclusions

1. **Replay correction is already an authorised Product capability.** DEC-188 and Product §21G.15 require replay versioning, correction and withdrawal.
2. **The existing Product correction classes are the controlling vocabulary:** `minor_editorial_correction`, `material_content_correction`, `safety_correction`, `legal_or_consent_correction`, `full_withdrawal`.
3. **Minor correction must preserve original history.** Exact implementation representation remains C&M JIT detail; destructive historical rewrite is not acceptable.
4. **Material correction creates an approved superseding version.** Provider/render completion is not publication authority.
5. **Safety correction withdraws affected current use immediately.** Lack of a ready replacement does not justify continued unsafe replay delivery.
6. **Legal/consent correction composes with current Privacy authority and accepted `LIVE-UPD-006`.** Technical editability cannot substitute for OQ-021/legal authority.
7. **Full withdrawal may legitimately leave no current replay.** A successor replacement is not mandatory.
8. **Current replay publication and historical publication evidence are separate.** Correction/withdrawal does not erase prior publication or prior lawful views.
9. **Derivative lineage must converge on the corrected/current replay.** Captions, transcripts, thumbnails and other derivatives cannot silently retain affected V1 meaning/rights.
10. **Correction failure semantics depend on correction class.** An otherwise eligible V1 may remain current during ordinary material remediation; an already-invalidated safety/legal/consent V1 must remain fail-closed if V2 processing fails.
11. **Stale delivery capabilities, edge/cache state or provider reachability cannot become current publication authority.** OQ-014/proof must enforce immediate classes correctly.
12. **Correction-of-correction uses successor/withdrawal semantics, not destructive rollback.**
13. **Replay correction never rewrites occurrence or attendance truth.** Historical delivery/version evidence remains attributable to what was actually delivered.
14. **No new Live Product decision package is justified by Pass I.** Existing Product correction classes, OQ-014, OQ-021, accepted `LIVE-UPD-006`, C&M `CM-UPD-011`, C&M JIT and executable/provider proof already own the remaining work.

These are proposed working conclusions only until accepted.

---

# 4. Pressure-test additions

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-087` | Minor editorial correction to a published replay transcript/caption | v0.9.0 | `PASS_WITH_REFINEMENT / C&M_JIT` | `PRODUCT_CORRECTION_CLASS → CONTENT_MEDIA_JIT → VERSION/PROVENANCE_EXECUTABLE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-088` | Material factual/content correction after replay publication | v0.9.0 | `PASS_WITH_REFINEMENT / EXISTING_CORRECTION_CONTRACT` | `PRODUCT_CORRECTION_CLASS → CM-UPD-011 / CONTENT JIT → ATOMIC_PUBLICATION_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-089` | Safety correction after replay publication; replacement not ready | v0.9.0 | `PASS / IMMEDIATE_WITHDRAWAL_REQUIRED` | `SAFETY_AUTHORITY → CONTENT_WITHDRAWAL → OQ-014 → FAILURE/EDGE/DELIVERY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-090` | Legal or consent correction removes one participant segment after publication | v0.9.0 | `BLOCKED / OQ-021_AND_ACCEPTED_UPD-006` | `CURRENT_PRIVACY_AUTHORITY → OQ-021 → CONTENT/PRIVACY_JIT → EXECUTABLE_LINEAGE/DELIVERY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-091` | Full replay withdrawal with no successor replacement | v0.9.0 | `PASS_WITH_REFINEMENT / C&M_JIT_AND_OQ-014` | `CONTENT_WITHDRAWAL → OQ-014 / SEARCH-CACHE_RECONCILIATION → EXECUTABLE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-092` | Successor replay is current but old signed delivery capability still targets V1 | v0.9.0 | `PASS_WITH_REFINEMENT / OQ-014_EXECUTABLE_PROOF` | `CURRENT_PUBLICATION_AUTHORITY → PROTECTED_DELIVERY → OQ-014 → CONTROLLED_FAILURE/REVOCATION_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-093` | V2 video current but captions/transcript/thumbnail still come from V1 | v0.9.0 | `PASS_WITH_REFINEMENT / CONTENT_MEDIA_JIT` | `CONTENT_LINEAGE_CONTRACT → JIT → DERIVATIVE_COMPATIBILITY/NON-RESURRECTION_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-094` | Correction processing or successor render fails halfway | v0.9.0 | `PASS_WITH_REFINEMENT / CM-UPD-011_DEPENDENT` | `CORRECTION_CLASS → CM-UPD-011 / CONTENT_JIT → RETRY/FAILURE-INJECTION_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-095` | Viewer requests playback concurrently with correction activation | v0.9.0 | `PASS_WITH_REFINEMENT / CONCURRENCY_PROOF_REQUIRED` | `CONTENT_JIT → ATOMIC_PUBLICATION/CAPABILITY_CONCURRENCY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-096` | A correction itself is later found wrong | v0.9.0 | `PASS` | `CONTENT_VERSION_LINEAGE → JIT → CORRECTION_CHAIN_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-097` | Replay correction must not rewrite occurrence, attendance or historical delivery evidence | v0.9.0 | `PASS_WITH_REFINEMENT / JIT_EVIDENCE_CONTRACT` | `DOMAIN_OWNERSHIP → CONTENT/AUDIT/ANALYTICS_JIT → TRACEABILITY_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Detailed timelines, invariants, adversarial variants, questions and evidence needs remain in discovery v0.9.0.

---

# 5. UPD register adjudication

## No LIVE-UPD-007

Pass I creates no new upstream-decision identifier.

Rationale:

- Product Law already requires replay versioning, correction and withdrawal;
- Product Law already defines the five correction classes;
- material and safety correction consequences are already materially specified;
- legal/consent consequence already routes through OQ-021 and accepted `LIVE-UPD-006`;
- exact correction-impact/remediation mapping is already exposed by C&M working seam `CM-UPD-011` and belongs to the proper Product/Content/Safety/Privacy/JIT owners;
- stale protected-delivery invalidation is OQ-014/proof, not a missing Product capability.

Creating `LIVE-UPD-007` would duplicate existing authority/routing.

---

# 6. Gap-register adjudication

## No LIVE-GAP-015

Pass I creates no new gap identifier.

Existing routing is sufficient:

- `LIVE-GAP-003 — RECORDING_PRIVACY_GATE` remains the seam for post-publication `legal_or_consent_correction` where recording/replay rights are affected under OQ-021;
- accepted `LIVE-UPD-006` remains the post-capture withdrawal-consequence package;
- OQ-014 / C&M `CM-UPD-002` owns protected-delivery/cache invalidation and immediate safety-withdrawal proof;
- C&M `CM-UPD-011` owns exact correction impact/severity → downstream remediation mapping;
- Content & Media JIT owns correction/withdrawal/version topology and derivative lineage representation;
- accepted `LIVE-GAP-014` remains processor deletion/non-resurrection, not ordinary correction publication.

`LIVE-GAP-005 — replay-right policy` is deliberately not overloaded with current media publication eligibility. Entitlement/right truth and C&M publication eligibility remain distinct.

---

# 7. Evidence register

No `LIVE-EV-*` item is added by Pass I.

Later proof should cover:

- exact V1→V2 lineage and publication history;
- atomic current-publication transition;
- safety/legal withdrawal fail-closed behaviour;
- stale delivery/cache/provider capability invalidation;
- derivative compatibility/replacement lineage;
- correction retry/failure recovery;
- correction-of-correction history;
- preservation of occurrence/attendance truth;
- delivered-version traceability where the eventual evidence contract selects it.

Provider-specific research remains deferred until the chosen media-provider path is ready for targeted proof.

---

# 8. Explicit non-decisions preserved

Pass I does **not** decide:

- exact thresholds distinguishing minor from material correction beyond current Product semantics;
- exact reviewer/approver matrix per replay risk class;
- exact legal/consent remedy under OQ-021;
- participant notification wording/channel/timing;
- promotional-clip correction/withdrawal propagation;
- exact signed-link TTL or purge mechanics;
- exact media editing/redaction technology;
- exact derivative compatibility algorithm;
- exact incident or Analytics event schema;
- provider-specific media object/versioning APIs;
- exact retention/deletion durations;
- exact Ash Resource/schema/job/storage implementation.

---

# 9. Pass-I proposed outcome

**Outcome:** `PASS`

Current authority is semantically sufficient to plan replay correction/version-history JIT work without a new Product amendment. Remaining uncertainty is correctly routed to existing Product correction classes, OQ-014, OQ-021, accepted `LIVE-UPD-006`, C&M `CM-UPD-011`, C&M JIT and executable/provider proof.

---

# 10. Acceptance transition rule

If Pass I is accepted without semantic changes, create non-semantic status successor `v0.7.1` that promotes:

- Pass I;
- `LIVE-PT-087...LIVE-PT-097`;
- the §3 Pass-I conclusions;
- the decision that no `LIVE-UPD-007` is warranted;
- the decision that no `LIVE-GAP-015` is warranted;
- the Pass-I routing/refinement of `LIVE-GAP-003`, OQ-014, OQ-021 and C&M `CM-UPD-011`;

to `ACCEPTED_WORKING_LOCK`.

If semantic changes are requested, create a substantive successor instead and preserve this v0.7.0 unchanged.

---

# 11. Proposed next focused pass

Only after Pass I acceptance:

> **Promotional clips derived from live/replay media — separate approval, purpose/audience, participant/speaker rights, correction/withdrawal propagation and lineage — while still deferring participant communications.**

That pass should pressure-test:

- clip approval is separate from replay publication approval;
- clip permission does not automatically inherit from recording/replay permission;
- exact source-version lineage after replay correction;
- source-replay correction/withdrawal versus an already-approved clip;
- consent withdrawal affecting clip purpose but not necessarily replay purpose;
- promotional/public audience versus protected replay audience;
- stale clip publication after source correction;
- speaker/guest versus attendee contribution in clips.

Participant-facing communication promises remain a later separate pass.