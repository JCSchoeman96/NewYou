# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.13.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.13.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch head before this successor:** `b320a277f8d56b06ae020f0c63a31d13dae6b198`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.12.0.md`
- **Purpose:** perform one bounded pass on `OPS-UPD-006` — interaction between an already-valid participant export and a later effective Full Deletion Request.
- **Scope:** valid export predating deletion; normal-access revocation versus exceptional data-right continuation; export generation and secure delivery during the 14-day deletion cancellation window; delivery/handoff completion boundary; irreversible deletion execution; deletion cancellation; stale/replayed export work; concurrent underlying-data change; external processor delay; participant-held copies after successful handoff.
- **Explicit non-goals:** no general Privacy redesign, no recurring-membership/deletion semantics, no duplicate-account deletion semantics, no Community/moderation sanction policy, no category-specific retention schedule, no legal interpretation of POPIA/GDPR, no new Domain/Resource, no implementation/API/storage selection, no PR, no authority amendment.
- **External legal research:** none added. Existing Privacy doctrine explicitly requires legal/privacy validation rather than guessed law; this pass narrows the Product/Privacy decision surface only.
- **Current overall disposition:** `FOCUSED PASS CONVERGED / OPS-UPD-006 CONFIRMED AND NARROWED / PRODUCT-PRIVACY EXPORT-HANDOFF RULE STILL REQUIRED / LEGAL-PRIVACY VALIDATION REMAINS / BROAD STREAM FREEZE STILL BLOCKED`.

---

# 0. Append-only successor rule

Reasoning chain:

```text
v0.1.0
→ v0.2.0
→ v0.3.0
→ v0.4.0
→ v0.5.0
→ v0.6.0
→ v0.7.0
→ v0.8.0
→ v0.9.0
→ v0.10.0
→ v0.11.0
→ v0.12.0
→ this v0.13.0 focused export / Full Deletion pass
```

All predecessors remain historical reasoning evidence.

This version adds:

- `OPS-PT-187...OPS-PT-198`;
- no new `OPS-UPD`;
- no new `OPS-GAP`;
- a material narrowing of existing `OPS-UPD-006` / `OPS-GAP-016` using `PRIV-UPD-001` and `PRIV-WD-001` as non-authoritative working evidence.

---

# 120. Live baseline and bounded authority route

Immediately before this pass:

```text
main = 086ade7b28c000de1c387acb9760e5eb08bb0413
working branch head = b320a277f8d56b06ae020f0c63a31d13dae6b198
```

Only authority/evidence relevant to this bounded seam was rechecked in depth:

- `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` Full Deletion lifecycle: immediate normal-access revocation → 14-day cancellation window → irreversible deletion execution;
- `01_DECISIONS_v1.6.0.md`:
  - `DEC-221` account closure versus irreversible Full Deletion;
  - `DEC-222` risk-based step-up verification for closure/deletion/sensitive export;
  - `DEC-223` 14-day Full Deletion cancellation window and no recovery/reconstruction after completed deletion;
  - `DEC-240` secure, verified, asynchronous human-readable + structured participant exports with expiring delivery;
  - `DEC-245` verified-email gate for export/deletion capabilities;
- `04_DOMAIN_MAP_v1.2.0.md` Privacy & Consent ownership of participant data-rights/lifecycle authority, Full Deletion and export orchestration;
- current Privacy Pre-JIT working evidence:
  - `NEWYOU_PRIVACY_PREJIT_CONTRACT_WORKING_v0.1.3.md`;
  - `NEWYOU_PRIVACY_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.3.md`;
  - archived `PRIV-PT-005` reasoning only as historical working evidence;
- `OQ-032` remains the existing export/deletion operational gate for verification levels, job deadlines, processor retries, pending states, participant notices, failure alerts and completion evidence.

No archive document was used to override current authority.

---

# 121. What current authority already fixes

## 121.1 Full Deletion immediately removes normal product access

The Full Deletion cancellation window is not ordinary continued Account access.

Current Product direction is:

```text
effective Full Deletion Request
→ immediate normal-access revocation
→ 14-day cancellation window
→ irreversible deletion execution
→ verified completion
```

Therefore an export that continues during the cancellation window cannot do so by restoring ordinary product access or treating the Account as normally active.

## 121.2 Export is a separate governed data-rights operation

`DEC-240` already establishes a secure, verified, asynchronous participant export with expiring delivery.

Privacy & Consent owns export orchestration, but each source Domain remains authoritative for its own records and release representation.

Working consequence:

```text
stored data ≠ automatically exportable data
```

A raw database dump or reconstruction from retained/deleted joins is not the export contract.

## 121.3 Request-time authority is not perpetual authority

Current Privacy working doctrine is consistent with current architecture/domain principles:

- current verification and scope must be revalidated at protected consequences;
- stale worker/event timing does not become present authority;
- underlying records may change while asynchronous export work is in flight;
- deleted or irreversibly anonymised records must not be reconstructed merely because the export request started earlier.

This is downstream/JIT proof detail once the Product sequencing rule is explicit.

## 121.4 Completed Full Deletion cannot leave a platform-controlled live product reconstruction path

`DEC-223` prohibits recovery/reconstruction after completed deletion.

A live platform-controlled export-delivery path containing participant data would therefore be materially different from a participant-held copy that was already lawfully handed off before irreversible deletion execution.

That distinction is central to this pass.

## 121.5 Operational export/deletion mechanics already have an existing gate

`OQ-032` already owns operational detail such as verification levels, export/deletion job deadlines, retries and pending states, participant notices, failure alerts, and completion evidence.

This pass must not turn those mechanics into a new Product delta.

---

# 122. Semantic dimensions that must not be collapsed

The export/deletion race needs at least these distinct dimensions regardless of later implementation representation.

## 122.1 Export-request validity

Was a participant export request validly created under then-current export authority and verification?

The bounded `OPS-UPD-006` seam concerns an export that **predates** the later effective Full Deletion Request.

This pass does not decide whether a brand-new export may be requested after Full Deletion has already become effective.

## 122.2 Export-generation state

The platform may still be assembling eligible payload from owner-Domain records.

Generation is not the same thing as successful participant handoff.

## 122.3 Platform-controlled delivery capability

An export may be generated and held behind a secure expiring delivery capability.

The platform still controls that artefact/capability until a governed handoff boundary is crossed.

## 122.4 Successful participant handoff / export completion

This is the key unresolved Product/Privacy boundary.

Current authority does not explicitly say whether export delivery is complete at secure artefact creation, secure link creation, notice/link dispatch, successful authenticated retrieval/download, or another legally/operationally defined handoff event.

Implementation must not choose this merely because one event is easiest to observe.

## 122.5 Effective Full Deletion Request / cancellation window

This immediately revokes normal access but remains cancellable for 14 days.

A continuing predating export, if Product permits it, is an exceptional data-rights operation during this window rather than restored product use.

## 122.6 Irreversible deletion execution

Once this begins, an export that has not crossed the governed successful-handoff boundary cannot remain a live platform-controlled delivery path under the accepted working direction.

## 122.7 Verified deletion completion

Completion cannot be asserted while a required platform/external path still exposes a live delivery/reconstruction capability that current deletion authority requires removed.

## 122.8 Participant-held copy

After a lawful secure handoff, the participant may possess a copy outside NewYou's control.

Full Deletion can remove NewYou-controlled data and delivery artefacts; it cannot pretend the participant never received a copy that was already handed off.

---

# 123. Focused pressure tests

## OPS-PT-187 — Effective Full Deletion follows a valid export before export generation starts

**Scenario class:** privacy / data rights / lifecycle ordering

**Timeline**

```text
valid verified export request
→ export queued but generation not started
effective Full Deletion Request
→ normal product access revoked
→ 14-day cancellation window begins
```

**Expected invariants**

- normal Account/product access is not restored merely to service the export;
- the earlier export does not silently become invalid only because normal access is revoked;
- whether it may continue during the cancellation window is a Product/Privacy participant-right rule, not a worker convenience rule;
- irreversible deletion must still have a deterministic boundary against any undelivered export.

**Analysis**

Current law governs both lifecycles independently but not their composition. Existing `PRIV-WD-001` recommends that the predating export may continue narrowly during the cancellation window. That recommendation is coherent but not yet upstream authority.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-006` / `PRIV-UPD-001`.

**Proof route:** `PRODUCT_PRIVACY_PROMOTION` → `LEGAL_PRIVACY_VALIDATION` → `JIT/OQ-032`.

---

## OPS-PT-188 — Export generation continues during the 14-day cancellation window

**Scenario class:** privacy / authorization / degraded access

**Preconditions**

- export validly predates deletion;
- Full Deletion is effective but still cancellable;
- normal product access is already revoked.

**Expected invariants**

- export continuation, if permitted, is narrowly scoped and does not re-enable ordinary Account/product functions;
- current export verification/authority/scope are revalidated at protected stages;
- each owner Domain supplies only currently eligible export representation;
- stale request-time permission is not permanent authorization.

**Analysis**

No new upstream class is exposed. This is the operational consequence of the same Product/Privacy sequencing choice plus existing owner-authority doctrine.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-006` only for the continuation permission.

**Proof route:** `JIT` + `OQ-032` after promotion.

---

## OPS-PT-189 — Export artefact is ready, but handoff is not complete when deletion becomes effective

**Scenario class:** privacy / delivery / lifecycle

**Timeline**

```text
export generated
→ platform-controlled secure artefact exists
→ no governed successful handoff yet
effective Full Deletion Request
→ cancellation window
→ irreversible deletion execution later begins
```

**Expected invariants**

- generated ≠ delivered merely because bytes exist;
- platform-controlled temporary artefact remains subject to current deletion authority;
- if irreversible deletion begins before the governed handoff boundary, the undelivered export cannot survive indefinitely as a delivery path.

**Analysis**

The exact successful-handoff boundary remains Product/Privacy + legal-validation work.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-006`.

---

## OPS-PT-190 — Secure delivery notice/link was issued but the participant has not retrieved the export when irreversible deletion begins

**Scenario class:** privacy / customer promise / delivery semantics

**Why it matters**

A provider/email acknowledgement or link-dispatch event is easy to observe but may not equal participant possession. Conversely, requiring a participant download forever could let inactivity block deletion indefinitely.

**Expected invariants**

- implementation does not invent “delivery complete” from the easiest technical event;
- the Product/Privacy rule chooses a deterministic successful-handoff boundary;
- once irreversible deletion execution begins, any still-platform-controlled live delivery capability is handled according to that rule rather than UI/email timing.

**Semantic disposition:** `NEEDS_WORKING_DELTA`

**Upstream delta:** `OPS-UPD-006`.

**Proof route:** `PRODUCT_PRIVACY_PROMOTION` + `LEGAL_PRIVACY_VALIDATION` + `JIT`.

---

## OPS-PT-191 — Participant securely retrieves the export before irreversible deletion execution

**Scenario class:** privacy / completed handoff / deletion

**Timeline**

```text
valid export
→ secure governed handoff completes
→ participant now possesses copy
effective Full Deletion Request / window
→ irreversible deletion execution
```

**Expected invariants**

- NewYou does not rewrite history and pretend the participant never received the export;
- Full Deletion proceeds against NewYou-controlled eligible data/artefacts;
- hosted temporary export artefacts/delivery capability still expire or are removed under the deletion/retention contract;
- participant-held external copy is not a live NewYou reconstruction path.

**Analysis**

This is compatible with the working recommendation, but the exact handoff event must first be governed.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-006` only for exact handoff semantics.

---

## OPS-PT-192 — Participant cancels Full Deletion during the 14-day window while the predating export is pending

**Scenario class:** privacy / cancellation / recovery

**Expected invariants**

- deletion cancellation before irreversible execution follows the governed deletion-cancellation path;
- export may return to its normal lifecycle only after current authority/verification is revalidated;
- no duplicate export obligation is manufactured merely because work was paused/retried;
- cancellation does not rewrite prior period of revoked normal access.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-006` for the export-survival promise; exact resume/retry mechanics are `OQ-032`/JIT.

---

## OPS-PT-193 — Purported deletion request fails required verification and never becomes effective

**Scenario class:** privacy / authorization / false trigger

**Expected invariants**

- an invalid/unverified destructive request cannot acquire Full Deletion authority;
- the valid export is not cancelled merely because someone attempted deletion;
- security/audit evidence may record the failed request without changing data-rights lifecycle truth.

**Semantic disposition:** `PASS`

**Upstream delta:** none beyond `OPS-UPD-006` general policy context.

---

## OPS-PT-194 — Export re-verification fails during the deletion cancellation window

**Scenario class:** privacy / verification / secure release

**Preconditions**

The export request was valid earlier, but current release verification/authority can no longer be satisfied at delivery.

**Expected invariants**

- earlier validity does not force current release;
- export delivery fails closed rather than bypassing verification because deletion is pending;
- normal product access remains revoked;
- whether the export is cancelled, remains pending, or may be reverified later within the window is operational policy beneath the upstream sequencing rule.

**Semantic disposition:** `PASS`

**Proof route:** `OQ-032` / Identity + Privacy JIT.

---

## OPS-PT-195 — Owner-Domain records change while export generation is in progress

**Scenario class:** privacy / concurrency / snapshot semantics

**Examples**

- participant corrects a record;
- an owner Domain lawfully deletes/anonymises an eligible record;
- a retained-obligation classification changes release eligibility;
- a concurrent write lands after export assembly began.

**Expected invariants**

- export needs a deterministic inclusion/cut rule rather than an accidental mix caused by worker timing;
- delivery-time/current-authority checks prevent reconstruction of records no longer release-eligible;
- exact snapshot/cut representation remains JIT/`OQ-032` unless Product explicitly promises a particular temporal snapshot.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** no new delta; `OPS-UPD-006` only if the Product participant promise needs a specific temporal meaning.

---

## OPS-PT-196 — External processor or owner Domain is still producing export material when irreversible deletion starts

**Scenario class:** privacy / processor / failure / deletion completion

**Expected invariants**

- an undelivered export does not hold Full Deletion in a permanent “waiting for participant export” state merely because an external processor is slow;
- under the accepted working direction, irreversible deletion start terminates the undelivered export path;
- processor-side export artefacts/capabilities that are deletion-eligible must be cancelled/removed/reconciled under the owner/processor deletion contract;
- verified deletion completion cannot be claimed merely from a transport acknowledgement when a required external path remains live.

**Semantic disposition:** `PASS_WITH_REFINEMENT`

**Upstream delta:** `OPS-UPD-006` for termination boundary only.

**Proof route:** `OQ-030` + `OQ-032` + deletion proof.

---

## OPS-PT-197 — Crash/restart replays stale export work after irreversible deletion execution begins

**Scenario class:** privacy / recovery / stale work

**Expected invariants**

- current deletion authority wins over stale queued/export state;
- restarted workers cannot regenerate or re-enable a delivery path from historical request validity;
- idempotent cancellation/removal and current-authority revalidation survive restart/reordering.

**Semantic disposition:** `PASS`

**Proof route:** JIT + architectural proof.

---

## OPS-PT-198 — Duplicate retry/reissue arrives after completed Full Deletion

**Scenario class:** privacy / terminal state / replay

**Expected invariants**

- completed deletion has no Account/product/export-delivery reconstruction path;
- duplicate export retry, stale notification or reissue command cannot create fresh delivery capability;
- minimum deletion/suppression evidence may prevent resurrection without reconstructing participant product authority.

**Semantic disposition:** `PASS`

**Proof route:** JIT + deletion/replay proof.

---

# 124. Results and narrowing of `OPS-UPD-006`

## 124.1 What this pass does not reopen

The following remain fixed by current authority or previously accepted doctrine:

- Full Deletion immediately revokes normal participant product access;
- the Full Deletion cancellation window is 14 days;
- completed deletion has no recovery/reconstruction path;
- participant export is secure, verified, asynchronous and expiring;
- verified email is required before export/deletion capabilities;
- Privacy & Consent owns export/deletion orchestration, not every source record;
- source Domains retain ownership of their own records/export representations;
- stored data is not automatically export eligible;
- request-time authority is not permanent;
- `OQ-032` remains the operations/JIT gate for deadlines, retries, notices, pending state and completion evidence;
- retention/legal-hold/category-specific release rules are separate from this sequencing question.

## 124.2 Exact remaining upstream decision surface

`OPS-UPD-006` / `PRIV-UPD-001` is now narrowed to these Product/Privacy policy questions:

1. **Predating export survival:** does an already-valid export continue as a narrow data-rights obligation during the 14-day Full Deletion cancellation window even though normal product access is revoked?
2. **Successful handoff:** what exact governed event means export delivery/handoff is complete for this lifecycle interaction?
3. **Irreversible boundary:** if that handoff has not completed when irreversible deletion execution begins, is the export cancelled and all platform-controlled delivery capability/temporary artefacts removed?
4. **Already-completed handoff:** after lawful handoff, does deletion proceed without attempting to revoke the participant-held copy while still removing NewYou-controlled temporary artefacts/capabilities?
5. **Deletion cancellation:** if deletion is cancelled before irreversible execution, may the predating export resume under its ordinary lifecycle after revalidation?
6. **Legal/privacy validation:** does the chosen participant promise satisfy the applicable data-rights obligations? This must be validated by appropriate legal/privacy authority, not guessed here.

No additional upstream delta is justified.

## 124.3 Recommended minimum promotion shape — not authority

The least contradictory current working shape is:

> A valid, verified participant export request created before an effective Full Deletion Request may continue during the 14-day deletion cancellation window only as a narrowly scoped participant data-rights operation and must not restore ordinary Account or product access. Export generation and delivery remain subject to current verification, authority and scope revalidation. If deletion is cancelled before irreversible execution, the export may return to its normal lifecycle after revalidation. If irreversible deletion execution begins before the governed successful participant handoff has completed, the undelivered export is cancelled and NewYou-controlled temporary export artefacts and delivery capability are removed under the deletion contract; stale retries/reissues may not recreate them. If lawful secure handoff completed before irreversible execution, subsequent Full Deletion does not pretend the participant-held copy never existed, while NewYou still removes its own temporary delivery artefacts/capabilities according to the deletion/retention contract. Product/Privacy authority must define the exact successful-handoff event, and legal/privacy validation remains required.

Important: this recommendation does **not** decide whether a brand-new export may be requested after an effective Full Deletion Request. That is outside this bounded `OPS-UPD-006` pass and should not be inferred from the predating-export exception.

---

# 125. Working locks added by this pass

Unless reopened by the stream's normal reopen conditions:

1. Full Deletion normal-access revocation and a narrowly scoped predating export operation are distinct dimensions; servicing export must not restore normal product access.
2. Export request validity, export generation, platform-controlled delivery capability and successful participant handoff are distinct states/concepts.
3. Generated export bytes are not automatically equivalent to successful participant delivery.
4. Email/provider/link dispatch timing does not automatically define Product-level successful handoff.
5. Request-time export authority does not permanently outrank later deletion, retention, legal-hold or owner-Domain release authority.
6. Completed Full Deletion cannot coexist with a live NewYou-controlled participant export-delivery/reconstruction path.
7. A participant-held copy that was lawfully handed off before irreversible deletion is not itself a NewYou-controlled reconstruction path; deletion still removes NewYou-controlled eligible artefacts/capabilities.
8. Stale/replayed export work after irreversible deletion begins must fail closed against current deletion authority.
9. Concurrent owner-record changes require deterministic export inclusion semantics; worker timing cannot decide truth accidentally.
10. `OQ-032` remains the downstream operational gate and must not be duplicated as Product policy.
11. Legal/privacy sufficiency is not established by this Pre-JIT pass.

---

# 126. Downstream only after `OPS-UPD-006` is resolved

JIT / proof may then choose and prove the smallest mechanism for:

- export-request lifecycle representation;
- secure expiring delivery capability;
- step-up/reverification and identity reconstruction while normal access is revoked;
- owner-Domain export snapshot/cut semantics;
- cancellation/restart idempotency;
- stale worker/retry suppression;
- processor/export artefact deletion coordination;
- secure handoff evidence;
- deletion-completion evidence;
- participant notices/failure alerts;
- crash/restart/reordering proof.

Do not create a new Export Domain or central Privacy shared-write authority merely for this lifecycle interaction.

---

# 127. Pass convergence

This focused pass is converged.

```text
SEMANTIC PRESSURE TESTS ADDED: OPS-PT-187...198
CUMULATIVE PRESSURE TESTS: 198
NEW OPS-UPD: 0
NEW OPS-GAP: 0
OPS-UPD-006: CONFIRMED + NARROWED
OPS-GAP-016: OPEN / SAME SEMANTIC CLASS
PRIV-UPD-001: REUSED, NOT DUPLICATED
PRIV-WD-001: REUSED AS NON-AUTHORITATIVE WORKING DIRECTION
NORMAL ACCESS VS DATA-RIGHTS EXPORT: SEPARATED
EXPORT VALIDITY / GENERATION / DELIVERY CAPABILITY / HANDOFF: SEPARATED
IRREVERSIBLE DELETION VS UNDELIVERED EXPORT: PRODUCT-PRIVACY RULE REQUIRED
SUCCESSFUL HANDOFF EVENT: OPEN UPSTREAM + LEGAL/PRIVACY VALIDATION
PARTICIPANT-HELD COPY VS PLATFORM-CONTROLLED ARTEFACT: SEPARATED
OQ-032: PRESERVED AS DOWNSTREAM OPERATIONS/JIT GATE
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED BY EXISTING UPSTREAM DELTAS + REQUIRED REVIEW/PROMOTION
```

Next semantic pass, only after user approval, should address `OPS-UPD-007` unless authority changes or an explicit upstream promotion pass is chosen first.
