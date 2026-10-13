# NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.4.0.md

- **Status:** WORKING / NON-AUTHORITATIVE / PROPOSED REGISTER SUCCESSOR
- **Document version:** v0.4.0
- **Date:** 2026-10-09
- **Predecessor:** `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.3.1.md`
- **Repository baseline:** `main@086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/live-replay`
- **Accepted predecessor commit:** `860c5280d03219fb7bd510cf9658c416efc88b64`
- **Pass F discovery artifact:** `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.6.0.md`
- **Pass F discovery commit:** `e4acd293f143ea8152e676129783dffc637c7040`
- **Primary downstream target:** `FP-007 — Governed live sessions and replay`
- **Implementation authority:** NONE
- **Product / Architecture / Domain / Roadmap authority:** NONE
- **Semantic rule:** Passes A–E remain `ACCEPTED_WORKING_LOCK`. Pass-F additions below remain `PROPOSED / AWAITING_USER_ACCEPTANCE` until explicitly accepted.

---

# 1. Cumulative state

Accepted working lock currently covers:

- Pass A / discovery v0.1.0;
- Pass B / discovery v0.2.0;
- Pass C / discovery v0.3.0;
- Pass D / discovery v0.4.0;
- Pass E / discovery v0.5.0;
- `LIVE-PT-001...LIVE-PT-056`;
- `LIVE-UPD-001...LIVE-UPD-005`;
- `LIVE-GAP-001...LIVE-GAP-013`;
- no `LIVE-EV-*` entries.

Pass F adds proposed post-capture withdrawal findings only. It does not reopen an accepted predecessor conclusion.

---

# 2. Pass register addition

| Pass | Discovery artifact | Commit | Focus | Working acceptance |
|---|---|---|---|---|
| F | `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.6.0.md` | `e4acd293f143ea8152e676129783dffc637c7040` | post-capture recording-purpose withdrawal, including one participant withdrawing from a multi-person recording | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

---

# 3. Proposed Pass-F working conclusions

1. **Post-capture withdrawal changes current future-processing authority; it does not rewrite the historical fact that capture/attendance occurred.**
2. **Historical lawful capture does not grant indefinite future replay/publication authority.** Existing media bytes or an already-published replay cannot preserve stale permission.
3. **Withdrawal is purpose-specific and is not Full Deletion.** It must neither under-apply to dependent uses nor silently erase unrelated valid purposes/rights.
4. **A published replay must re-evaluate current Privacy/Content authority after withdrawal.** Replay entitlement cannot override an ineligible current publication.
5. **One participant's withdrawal from a multi-person recording cannot be ignored merely because others remain authorised; nor does this pass assume that participant automatically controls the whole recording.**
6. **Technical separability is an input, not authority.** Editing/removal/replacement versus whole-replay withdrawal requires an approved consequence rule.
7. **Material inseparability is a real adversarial case that JIT cannot resolve by convenience.** The platform needs a fail-closed policy when no compliant replacement is currently approved.
8. **Role/context may change the applicable withdrawal rule, especially for planned speakers/guests/staff, but provider role state does not decide it.**
9. **Dependent derivatives must converge on current purpose authority through governed lineage; blocking only the primary replay is insufficient.**

These are proposed working conclusions only until accepted.

---

# 4. Pressure-test additions

| ID | Title | Source | Semantic disposition | Proof / resolution route | Acceptance |
|---|---|---|---|---|---|
| `LIVE-PT-057` | Participant withdraws recording-purpose authority while the live session is still running after already speaking | v0.6.0 | `PASS_WITH_REFINEMENT / OQ-021_DEPENDENT` | `OQ-021 → PROVIDER_EMPIRICAL → JIT → CONTROLLED_LIVE_PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-058` | Participant withdraws after raw capture exists but before replay publication | v0.6.0 | `PASS_WITH_REFINEMENT / REMEDIATION_POLICY_OPEN` | `OQ-021 + CONTENT/PRIVACY JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-059` | Participant withdraws after replay is already published | v0.6.0 | `NEEDS_WORKING_DELTA` | `OQ-021 + PRODUCT/PRIVACY/CONTENT ADJUDICATION` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-060` | One participant withdraws from a multi-person recording and her contribution is cleanly separable | v0.6.0 | `NEEDS_WORKING_DELTA` | `OQ-021 + PRODUCT/PRIVACY/CONTENT ADJUDICATION → JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-061` | One participant withdraws from a multi-person recording and her contribution is materially inseparable | v0.6.0 | `NEEDS_WORKING_DELTA / BLOCKS_JIT_POLICY_CHOICE` | `OQ-021 + PRODUCT/PRIVACY/LEGAL/OPERATIONS ADJUDICATION` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-062` | Planned speaker or guest withdraws after capture | v0.6.0 | `BLOCKED / ROUTE_TO_RECORDING_PRIVACY_GATE` | `OQ-021 + LEGAL/OPERATIONS REVIEW` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-063` | Participant withdraws one downstream purpose but not all recording-related purposes | v0.6.0 | `PASS_WITH_REFINEMENT / OQ-021_DEPENDENT` | `OQ-021 + PRIVACY JIT` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-064` | Derivatives already exist when the participant withdraws | v0.6.0 | `PASS_WITH_REFINEMENT` | `OQ-021 → CONTENT/PRIVACY JIT → EXECUTABLE PROOF` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |
| `LIVE-PT-065` | Recording-purpose withdrawal must not rewrite occurrence, attendance or unrelated rights | v0.6.0 | `PASS` | `JIT + PHASE8_EXECUTABLE` | `PROPOSED / AWAITING_USER_ACCEPTANCE` |

Detailed timelines, invariants, adversarial variants, questions and evidence needs remain in discovery v0.6.0.

---

# 5. Proposed upstream-delta addition

## LIVE-UPD-006 — Define post-capture recording-purpose withdrawal consequences

**Status:** `PROPOSED / AWAITING_USER_ACCEPTANCE / NOT AUTHORITY`

**Origin:** `LIVE-PT-057...LIVE-PT-065`, especially PT-059, PT-060, PT-061 and PT-062.

**Decision package to be resolved through existing OQ-021/Product/Privacy/legal/operations authority:**

1. the recording-related purposes/scopes that may be granted/withdrawn, including the relationship among capture participation, replay publication/use and separately approved promotional clips;
2. the effective boundary for withdrawal while a live recorded occurrence is still running;
3. the consequence when withdrawal occurs after capture but before replay publication;
4. the consequence when withdrawal occurs after replay publication;
5. the consequence when one participant withdraws from a multi-person recording and the affected material is technically/editorially separable;
6. the consequence when the affected material is materially inseparable;
7. any role/context-specific withdrawal rules for planned speakers, guests, facilitators or staff, including any separately approved contractual/lawful basis;
8. the fail-closed rule while a compliant remediation/replacement outcome is unresolved;
9. how current replay publication/access changes without rewriting historical occurrence, attendance, prior publication or prior lawful views;
10. how dependent media derivatives/uses are identified and re-evaluated under current authority;
11. the rule that withdrawal alone is not Full Deletion and does not silently revoke unrelated product/commercial rights;
12. that any alternative lawful basis for continued processing must be explicit Privacy/legal authority and may not be invented by JIT.

**Owner/gate:** existing `OQ-021 — Video consent and retention` plus Product/Privacy/legal/operations governance. This candidate refines the decision package; it does not create a parallel legal gate.

---

# 6. Gap-register adjudication

## LIVE-GAP-003 refinement — post-capture withdrawal consequence

**Existing classification:** `RECORDING_PRIVACY_GATE`

Proposed Pass F refinement adds:

- withdrawal while the live session continues after prior capture;
- withdrawal after capture but before replay publication;
- withdrawal after replay publication;
- one participant withdrawing from a multi-person recording;
- separable versus materially inseparable contribution;
- speaker/guest/facilitator/staff withdrawal distinctions;
- purpose-specific withdrawal across replay versus separately approved promotional clips;
- derivative dependency after withdrawal;
- the distinction between withdrawal and Full Deletion;
- the distinction between recording-purpose withdrawal and occurrence/attendance/general entitlement truth.

This remains one OQ-021 recording/privacy gate.

## No LIVE-GAP-014

No new gap identifier is proposed.

OQ-021 already explicitly includes withdrawal rules; `LIVE-UPD-006` captures the missing consequence package; exact propagation/orchestration/lineage representation remains downstream JIT/proof; and retention/processor deletion remain separate existing governance work.

---

# 7. Evidence register

No `LIVE-EV-*` item is added by Pass F.

Provider research remains deliberately deferred. The pass defines what provider enforcement/deletion evidence will eventually need to prove without allowing provider behaviour to define the Product rule.

---

# 8. Explicit non-decisions preserved

Pass F does **not** decide:

- statutory, contractual or policy retention durations;
- whether already-captured bytes must be immediately destroyed, temporarily restricted or retained under another lawful basis;
- Full Deletion request/cancellation/execution/completion;
- external provider/processor deletion deadlines, APIs or completion evidence;
- exact video-editing/redaction technology;
- final communications wording/channel;
- provider-specific recording/deletion controls;
- final replay correction taxonomy beyond the withdrawal consequence seam;
- legal sufficiency of any consent/release mechanism;
- Ash Resource/schema/job/storage representation.

---

# 9. Acceptance transition rule

If Pass F is accepted without semantic changes, create non-semantic status successor `v0.4.1` that promotes:

- Pass F;
- `LIVE-PT-057...LIVE-PT-065`;
- the §3 Pass-F conclusions;
- `LIVE-UPD-006`;
- the refinements to `LIVE-GAP-003`;

to `ACCEPTED_WORKING_LOCK`.

If semantic changes are requested, create a substantive successor instead and preserve this v0.4.0 unchanged.

---

# 10. Proposed next focused pass

Only after Pass F acceptance:

> **Retention and processor-deletion boundary for live recordings/replays after withdrawal, while keeping Full Deletion itself for the following separate pass.**

That pass should focus only on retained-but-not-usable media, provider/processor copies, deletion/reconciliation evidence, retry/partial failure/non-completion, recording-media non-resurrection and the effect of legal hold or another independently approved lawful retention basis.

It must still defer the whole-platform Full Deletion lifecycle and avoid inventing statutory durations not supplied by the expert retention matrix.
