# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.6.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PROPOSED REGISTER SUCCESSOR
- **Document version:** v0.6.0
- **Date:** 2026-10-10
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.5.1.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted predecessor commit:** `90389bef840477e7c03cab0b6c6a7ea9f94d30d9`
- **Pass H discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.8.0.md`
- **Pass H discovery commit:** `8642d0df2ee0d760c6b8fb783c8c3d83c65a9bef`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic rule:** Passes A–G remain `ACCEPTED_WORKING_LOCK`. Pass-H additions below remain `PROPOSED / AWAITING_USER_ACCEPTANCE` until explicitly accepted.

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
- `LIVE-PT-001...LIVE-PT-075`;
- `LIVE-UPD-001...LIVE-UPD-006`, with no `LIVE-UPD-007`;
- `LIVE-GAP-001...LIVE-GAP-014`;
- no `LIVE-EV-*` entries.

Pass H adds proposed FP-007-specific Full Deletion integration findings only. It does not reopen the whole-platform Privacy architecture or an accepted predecessor conclusion.

---

# 2. Pass register addition

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| H | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.8.0.md` | `8642d0df2ee0d760c6b8fb783c8c3d83c65a9bef` | FP-007 interaction with Full Deletion: registration/attendance, current access, shared recordings, processors, Audit and Analytics | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

---

# 3. Proposed Pass-H working conclusions

1. **Full Deletion orchestration does not transfer source ownership to Privacy.** Events, Content, Entitlements, Audit and Analytics execute their own governed consequences.
2. **Occurrence history and participant identifiability are separate questions.** Deleting a participant does not make the occurrence never have happened.
3. **A Full Deletion Request immediately removes ordinary live/replay access authority.** Provider transport persistence, stale tokens or cached links cannot preserve it.
4. **This Full-Deletion-specific immediate revocation does not resolve every general in-progress entitlement-revocation case.** `LIVE-UPD-004` remains independently scoped.
5. **Registration/attendance business meaning is separate from identifiable representation retention.** Exact Events record disposition belongs to OQ-029/Privacy JIT.
6. **Historical attendance must not be rewritten as `no_show` merely because participant linkage is later deleted/anonymised.**
7. **Shared multi-person media requires participant-level deletion consequence without assuming automatic whole-asset destruction or automatic preservation.**
8. **Technical separability/inseparability is evidence, not authority.** Exact lawful disposition remains OQ-021/OQ-029.
9. **Any speaker/guest/staff independent lawful or contractual basis must be explicit and scoped.** Account deletion and provider roles cannot manufacture or silently cancel it.
10. **Audit may retain independently authorised minimum non-reconstructive evidence when source references become non-resolvable.** Audit cannot become a shadow participant-history store.
11. **Participant-level live/replay Analytics is deleted/suppressed; only sufficiently irreversible aggregates may survive.**
12. **A required unresolved external processor path prevents verified Full Deletion completion.** Existing `LIVE-GAP-014` is reused rather than duplicated.
13. **Cancellation of Full Deletion does not let FP-007 self-restore access or resurrect disposed data.** Live/replay consumes current owner authority after the generic cancellation outcome.

These are proposed working conclusions only until accepted.

---

# 4. Pressure-test additions

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-076` | Full Deletion Request while participant is actively viewing live | v0.8.0 | `PASS_WITH_REFINEMENT / EXECUTABLE_ENFORCEMENT_REQUIRED` | `PRIVACY/ENTITLEMENTS JIT + OQ-020 → PHASE8/CONTROLLED_LIVE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-077` | Full Deletion Request after registration but before occurrence starts | v0.8.0 | `PASS_WITH_REFINEMENT / RETENTION_MATRIX_DEPENDENT` | `PRIVACY + EVENTS JIT + applicable OQ-029/OQ-032 → EXECUTABLE PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-078` | Full Deletion after attendance but before replay publication | v0.8.0 | `PASS_WITH_REFINEMENT / CATEGORY_DISPOSITION_DEPENDENT` | `OQ-021 + OQ-029 + EVENTS/CONTENT/PRIVACY JIT → EXECUTABLE PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-079` | Full Deletion after replay publication and current replay access | v0.8.0 | `PASS_WITH_REFINEMENT / MEDIA_DISPOSITION_DEPENDENT` | `PRIVACY + ENTITLEMENTS + CONTENT JIT + OQ-021/OQ-029 → EXECUTABLE PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-080` | Deleted participant in multi-person recording; contribution cleanly separable | v0.8.0 | `PASS_WITH_REFINEMENT / OQ-021_OQ-029_DEPENDENT` | `CONTENT/PRIVACY JIT + OQ-021/OQ-029/OQ-030 → EXECUTABLE PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-081` | Deleted participant in multi-person recording; contribution materially inseparable | v0.8.0 | `BLOCKED / ROUTE_TO_EXISTING_PRIVACY_RETENTION_GATES` | `OQ-021 + OQ-029 + LEGAL/PRIVACY/CONTENT ADJUDICATION` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-082` | Speaker/guest/facilitator/staff Full Deletion with possible independent basis | v0.8.0 | `BLOCKED / LEGAL_PRIVACY_CATEGORY_REVIEW` | `OQ-021 + OQ-029 + LEGAL/OPERATIONS/PRIVACY → CONTENT JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-083` | Minimum Audit evidence survives while source live records are disposed | v0.8.0 | `PASS / REUSE_EXISTING_AUDIT_DOCTRINE` | `AUDIT JIT EVENT_SELECTION + PRIVACY RETENTION CONTRACT → EXECUTABLE PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-084` | Participant-level Analytics deleted while irreversible aggregates survive | v0.8.0 | `PASS_WITH_REFINEMENT / ANONYMISATION_PROOF_REQUIRED` | `PRIVACY + ANALYTICS JIT → PHASE8/RELEASE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-085` | Required external recording processor path unresolved during Full Deletion | v0.8.0 | `PASS / EXISTING_PROVIDER_GATE_REUSED` | `OQ-030/OQ-032 + LIVE-GAP-014 → PROVIDER_EMPIRICAL + FAILURE-INJECTION/RECONCILIATION PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-086` | Full Deletion cancelled during 14-day window after access revocation | v0.8.0 | `PASS_WITH_REFINEMENT / GENERIC_RESTORATION_AUTHORITY_DEPENDENT` | `PRIVACY/IDENTITY/ENTITLEMENTS JIT → EVENTS/CONTENT CURRENT-AUTHORITY INTEGRATION PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Detailed timelines, invariants, adversarial variants, questions and evidence needs remain in discovery v0.8.0.

---

# 5. UPD register adjudication

No `LIVE-UPD-007` is created.

Pass H found no genuinely missing live-specific Product decision package because:

- current Product/North-Star law already defines the Full Deletion lifecycle and immediate normal-access revocation;
- Architecture already requires owner-specific, representation-complete, idempotent deletion;
- Domain Law already assigns Privacy orchestration without shared writes;
- OQ-029 owns category-specific registration/attendance/media/evidence disposition;
- OQ-021 owns live-video retention/privacy rules;
- OQ-030/OQ-031/OQ-032 own processor, restore and operational completion detail.

`LIVE-UPD-006` remains specifically about post-capture purpose withdrawal and is not expanded into Full Deletion.

---

# 6. Gap-register adjudication

## No LIVE-GAP-015

No new gap identifier is proposed.

Existing seams are sufficient:

- `LIVE-GAP-003 — RECORDING_PRIVACY_GATE` is proposed to be refined to include Full-Deletion participant representation inside shared recordings and the separable/inseparable consequence;
- `LIVE-GAP-014 — PROVIDER_EMPIRICAL_GATE` is reused for processor-complete Full Deletion and non-resurrection proof;
- OQ-029 owns category-specific registration/attendance/media/evidence disposition;
- generic deletion-cancellation restoration remains Privacy/Identity/Entitlements authority.

`LIVE-GAP-004 — Attendance business meaning` is deliberately **not** overloaded with retention/deletion policy. Attendance meaning and identifiable record disposition remain separate questions.

---

# 7. Evidence register

No `LIVE-EV-*` item is added by Pass H.

Provider research remains deferred. Accepted `LIVE-GAP-014` already defines the later video/storage processor deletion evidence contract.

---

# 8. Explicit non-decisions preserved

Pass H does **not** decide:

- exact registration/attendance/media/Audit retention periods;
- the full OQ-029 category matrix;
- generic Account/Entitlement restoration semantics after deletion cancellation;
- whole-platform Full Deletion Resource/orchestration implementation;
- deletion/export operational deadlines;
- provider/API selection or retry timings;
- unrelated Domain deletion contracts;
- exact media redaction/editing technology;
- participant communication wording;
- event-commerce/ticket retention;
- legal sufficiency of speaker/participant contracts;
- database/schema/worker/queue/storage implementation.

---

# 9. Acceptance transition rule

If Pass H is accepted without semantic changes, create non-semantic status successor `v0.6.1` that promotes:

- Pass H;
- `LIVE-PT-076...LIVE-PT-086`;
- the §3 Pass-H conclusions;
- the decision that no `LIVE-UPD-007` is warranted;
- the decision that no `LIVE-GAP-015` is warranted;
- the refinements/reuse of `LIVE-GAP-003` and `LIVE-GAP-014`;

to `ACCEPTED_WORKING_LOCK`.

If semantic changes are requested, create a substantive successor instead and preserve this v0.6.0 unchanged.

---

# 10. Proposed next focused pass

Only after Pass H acceptance:

> **Replay correction, replacement, withdrawal and version history after publication — including safety/legal/consent correction classes — without yet addressing promotional clips or participant communications.**

That pass should pressure-test ordinary editorial correction, safety correction, legal/consent correction, successor replay replacement, immediate withdrawal, historical publication evidence, captions/transcripts/derivatives and stale/bounded delivery capabilities while preserving source occurrence/attendance truth.
