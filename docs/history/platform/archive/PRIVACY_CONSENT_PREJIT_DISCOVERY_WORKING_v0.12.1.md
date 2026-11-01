# PRIVACY_CONSENT_PREJIT_DISCOVERY_WORKING_v0.12.1.md

- **Document status:** WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY
- **Document version:** v0.12.1
- **Date:** 2026-09-09
- **Canonical repository:** `https://github.com/JCSchoeman96/NewYou`
- **Live authority baseline verified against `main`:** `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`
- **Baseline reverified for compression audit:** 2026-09-09; live `main` remained at the same SHA.
- **Previous version:** `PRIVACY_CONSENT_PREJIT_DISCOVERY_WORKING_v0.12.0.md` — preserved historical working evidence.
- **Purpose:** Maintain the cumulative Privacy + Consent + Participant Data Rights + Full Deletion + Retention + Anonymisation/Pseudonymisation + Export + Legal Hold + External Processor Coordination + Backup/Restore Non-Resurrection Pre-JIT discovery record.
- **Authority boundary:** This document does **not** amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Delivery Atlas, Feature Packs, JIT Domain Dossiers, or implementation authority. It records pressure-test evidence, accepted working conclusions, downstream proof obligations, cross-stream seams, and true upstream gaps where discovered.
- **Implementation:** NOT AUTHORISED by this document.

---

# 1. Document operating rule

This is the cumulative working record for the Privacy Pre-JIT stream.

The maintenance rule is:

> **Never delete accepted discovery history. Add, refine, correct, supersede, or explicitly reclassify it.**

The following rules apply:

1. Accepted pressure-test records remain present in successor versions.
2. A later correction does not silently erase the earlier accepted position. Where meaning changes, the earlier position is marked `SUPERSEDED` or `CORRECTED BY <successor>` and the replacement is added explicitly.
3. Previously published SemVer files are historical working evidence and are not rewritten once superseded by a new version.
4. New accepted substantive discovery normally creates a new successor version of this whole working document.
5. Hygiene, citation, wording, or classification corrections that do not materially change discovery semantics use a patch release.
6. No local Pre-JIT conclusion becomes Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT, or implementation authority merely by appearing here.
7. If current GitHub authority conflicts with this document, live governed GitHub authority wins and this document must be explicitly corrected/superseded.
8. Archive/history is evidence, not authority.

---

# 2. SemVer policy

This working stream uses SemVer intentionally.

## 2.1 MAJOR

Increment `MAJOR` when the Pre-JIT working contract itself changes incompatibly, for example:

- a material restructuring changes how accepted records must be interpreted;
- a previously central working doctrine is invalidated in a way that requires broad reinterpretation;
- the stream is recomposed into a materially different contract rather than merely extended.

A major bump does **not** create governing authority.

## 2.2 MINOR

Increment `MINOR` for backward-compatible substantive discovery additions, normally including:

- a newly accepted `PRIV-PT-###` pressure test;
- a newly accepted `PRIV-WD-###` working doctrine after explicit approval;
- a new `PRIV-UPD-###` upstream delta;
- a material new cross-stream dependency;
- a substantive new legal/privacy expert gate or JIT proof obligation not already captured.

Default rule for this stream:

> **Each newly accepted substantive pressure-test result normally advances MINOR.**

## 2.3 PATCH

Increment `PATCH` for non-semantic maintenance, including:

- citation/source hygiene;
- wording clarification;
- typo/format correction;
- stricter classification without changing the underlying accepted semantic conclusion;
- correction of an overly broad seam where governing authority already answers the question;
- change-log or provenance improvements.

If a correction materially changes the accepted discovery meaning, use `MINOR` or `MAJOR` as appropriate rather than hiding it in a patch.

---

# 3. Canonical authority baseline

## 3.1 Live repository state used for v0.12.0

Verified `main` head:

`5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`

Current authority set at this baseline:

1. `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `docs/00_platform/00_PLATFORM_v1.3.0.md`
3. `docs/00_platform/01_DECISIONS_v1.3.0.md`
4. `docs/00_platform/02_OPEN_WORK_v1.2.39.md`
5. `docs/00_platform/03_ARCHITECTURE_v1.1.0.md`
6. `docs/00_platform/04_DOMAIN_MAP_v1.1.0.md`
7. `docs/00_platform/05_ROADMAP_v1.1.0.md`
8. `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md`
9. `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` when frontend/UI work is in scope.

Deep/reference architecture evidence includes:

- `docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.1.0.md`
- `docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.36.0.md`
- `docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.3.0.md`
- `docs/00_platform/reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md`

Machine-readable authority manifest:

- `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`

Baseline note for `v0.2.0`:

- `main` advanced from the `v0.1.0` baseline to `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`;
- the advancing commit added Commerce/Entitlements Pre-JIT working navigation and did not itself amend the governed Product/Architecture/Domain/Roadmap authority set used by this Privacy stream.

## 3.2 Programme position at this baseline

At the verified baseline:

- the Targeted Product Amendment authority-stage sequence is complete through Domain and Roadmap amendment and warranted Delivery Atlas reconciliation;
- current routing is `HARDEN-02_CONTRACT_REQUIRED` after independent certification of the Delivery Atlas reconciliation head;
- `FP001_RECONCILIATION_REQUIRED` remains downstream;
- executable platform development is not yet generally authorised by the current planning gates;
- the FP-001 Privacy & Consent JIT Domain Dossier remains conditional/pending explicit adjudication rather than automatically required.

This Pre-JIT stream does not change that routing.

---

# 4. Existing Privacy authority that this stream must not re-legislate

Current Product/Decision authority already includes a substantial Privacy lifecycle contract, especially `DEC-220...DEC-243`.

Key existing directions include:

- shared lifecycle vocabulary;
- account closure distinct from irreversible full deletion;
- destructive-action verification;
- verified email required before export and deletion capabilities (`DEC-245`);
- 30-day recoverable closure and 14-day full-deletion cancellation window;
- assessment deletion/anonymisation treatment;
- permanent loss of purchased product access after full deletion;
- Health record separation between self-guided and formal professional records;
- journal deletion treatment;
- deletion of originals, derivatives, previews, extracted values, indexes, cached links and temporary processing artefacts;
- professional record governance;
- Community deletion/anonymisation boundaries;
- restricted commercial retention that cannot reconstruct the participant account or product access;
- consent withdrawal consequences;
- minimised/restricted Audit and Security-event retention;
- participant-level Analytics deletion with only sufficiently irreversible aggregate retention;
- inactive-account lifecycle;
- deceased-participant process;
- narrow scoped legal holds;
- historical encrypted backup expiry plus deletion replay after restore;
- participant export;
- correction/supersession rules;
- minimised incident evidence;
- versioned retention governance and deletion-completion semantics.

This Pre-JIT stream therefore starts from the presumption:

> **Stress accepted law first. Do not invent a parallel Privacy quasi-authority.**

---

# 5. Privacy & Consent ownership boundary

Current Domain Law assigns Privacy & Consent ownership of the participant-data-rights/governance boundary, including:

- purpose-specific consent/lawful-basis grants and withdrawals;
- current purpose authority;
- purpose-specific consent/share authority used by scoped access;
- full-deletion request/cancellation/execution orchestration and deletion-completion state;
- retention policy assignments/versions;
- retained-by-obligation classification;
- legal holds;
- participant export requests/lifecycle;
- minimal deletion/suppression/replay truth required to prevent resurrection after restore.

Privacy & Consent does **not** own every underlying record.

It does not become canonical owner of:

- Account lifecycle;
- Health records;
- Plan records;
- journal records;
- commercial records;
- professional records;
- Community records;
- Research/Feedback records;
- Voting/Balloting records;
- Audit/Security evidence produced by other Domains;
- professional retention durations not approved by the relevant expert authority.

Cross-Domain deletion, withdrawal, retention, export, hold and restore consequences therefore preserve the one-owner rule:

> **Privacy owns the relevant governance/orchestration truth; each owning Domain applies the consequence to its own authoritative records.**

---

# 6. Methodology rules accepted for this stream

## 6.1 Pressure-test verdicts

Each material pressure test uses:

- `PASS`
- `PASS WITH NON-BLOCKING CORRECTIONS`
- `CHANGES REQUIRED`
- `BLOCKED / STOP`

Implementation/operational evidence is classified separately:

- `PASS`
- `PASS WITH NON-BLOCKING CORRECTIONS`
- `CHANGES REQUIRED`
- `NOT ASSESSED`

Strict verdict rule:

> If existing authority fully survives the scenario and no semantic/model correction is required, the semantic verdict is `PASS`.

A newly identified JIT/Architectural Proof obligation by itself does **not** downgrade a semantic `PASS`.

## 6.2 Required invariant versus JIT shape

Every recommendation that mixes semantics with possible implementation shape must separate:

### Required invariant

What current authority requires to remain true.

### Recommended JIT shape

A likely implementation/JIT contract that could satisfy the invariant without being silently frozen as Product or Architecture authority.

This prevents language such as “guard”, “worker”, “row”, “resource”, “event”, “lock”, or “policy” from accidentally becoming mandatory representation before JIT/Architectural Proof.

## 6.3 Full-deletion cancellation window correction

Normal participant access during the 14-day full-deletion cancellation window is already governed:

```text
full deletion request
→ immediate normal-access revocation
→ 14-day cancellation window
→ irreversible deletion execution
```

Therefore this stream must **not** reopen ordinary-access semantics during the cancellation window.

A narrower legitimate future pressure-test seam remains:

- what retained-obligation/non-normal processing may continue during that window;
- what deletion preparation/processor coordination may occur;
- what exactly cancellation restores before irreversible deletion execution begins.

## 6.4 Legal/privacy law rule

Do not guess privacy law.

Where a recommendation materially depends on current law or regulator guidance:

1. identify the jurisdiction;
2. inspect current primary legal/regulatory sources;
3. distinguish NewYou Product Law from actual law;
4. distinguish legal text from interpretation/expert recommendation;
5. classify any necessary unresolved matter as a `LEGAL / PRIVACY EXPERT GATE` rather than inventing a rule.

No GDPR or POPIA rule is imported by assumption.

---

# 7. Discovery map

The active bounded discovery tracks are:

1. consent authority;
2. deletion authority, concurrency and stale work;
3. backup restore and non-resurrection;
4. retention and legal hold;
5. participant export;
6. external processor reconciliation;
7. identity/data-right lifecycle;
8. de-identification/evidence boundaries.

Initial pressure-test sequence:

| PT | Scenario | Status |
|---|---|---|
| PRIV-PT-001 | Full deletion versus concurrent downstream writes | ACCEPTED — PASS |
| PRIV-PT-002 | Restore a backup from before completed deletion | ACCEPTED — PASS |
| PRIV-PT-003 | Purpose-specific consent withdrawal while downstream work is in flight | ACCEPTED — PASS |
| PRIV-PT-004 | Stale, duplicated or reordered async events after deletion/withdrawal | ACCEPTED — PASS |
| PRIV-PT-005 | Export races deletion and concurrent mutation | ACCEPTED — CHANGES REQUIRED / PRIV-WD-001 accepted / PRIV-UPD-001 recorded |
| PRIV-PT-006 | External processor unavailable/delayed during deletion | ACCEPTED — PASS |
| PRIV-PT-007 | Legal hold applied during deletion; narrow scope and release resumes deletion | ACCEPTED — PASS |
| PRIV-PT-008 | Self-guided Health/Safety/Plan data versus professional retention | ACCEPTED — PASS / HSP-UPD-004 seam |
| PRIV-PT-009 | Retained Commerce/Audit evidence cannot recreate Account/Entitlement/access | ACCEPTED — PASS / CER-PT-001 seam |
| PRIV-PT-010 | Pseudonymised data remains re-identifiable | ACCEPTED — PASS |
| PRIV-PT-011 | Closure → reopen → deletion → new Account using same email/phone | ACCEPTED — PASS |
| PRIV-PT-012 | Export of mixed active / retained / deleted categories | ACCEPTED — PASS |
| PRIV-PT-013 | Deletion with refund/dispute/chargeback or active recurring membership | ACCEPTED — CHANGES REQUIRED / PRIV-WD-002 accepted / PRIV-UPD-002 recorded / CER seam |
| PRIV-PT-014 | Identity merge/unmerge where one side enters deletion | ACCEPTED — CHANGES REQUIRED / PRIV-WD-003 accepted / PRIV-UPD-003 recorded |
| PRIV-PT-015 | Community/moderation/security evidence after deletion | ACCEPTED — CHANGES REQUIRED / PRIV-WD-004 accepted / PRIV-UPD-004 recorded |

The sequence may be refined when pressure testing exposes a higher-priority seam, but accepted PT records are not removed.

**v0.9.0 map correction:** older working versions contained a stale planning-map label assigning `PRIV-PT-012` to Community/moderation/security evidence, while the actual later planned test section and accepted test use `PRIV-PT-012` for mixed-category export. Because accepted identifiers are never repurposed, the Community/moderation/security scenario is prospectively moved to unused `PRIV-PT-015`. Earlier versioned files remain unchanged as historical evidence.

---

# 8. Accepted pressure-test record — PRIV-PT-001

## PRIV-PT-001 — Full deletion versus concurrent downstream writes

### Scenario

A participant has passed the 14-day cancellation window and durable full-deletion orchestration has begun. Before an owning Domain completes its deletion consequence, another request/job attempts to create new participant-identifiable ordinary product/current-use state.

### Governing semantic conclusion

Once effective deletion/suppression authority exists, an ordinary participant/current-use mutation may not create fresh active authority merely because its request or work started earlier.

A real race may still physically commit before observing suppression, but that state must converge through the owning Domain's governed deletion treatment before deletion completion can be asserted.

### Rejected models

**Global Privacy lock/shared-write transaction:** REJECTED.

Reason: Privacy would become shared-write owner across Domains, increasing coupling and violating canonical ownership.

**Allow writes freely and clean up eventually:** REJECTED as the primary correctness model.

Reason: reconciliation is necessary as a recovery/backstop mechanism, but cannot itself be the permission model for ordinary current-use writes.

### Required invariant

> Once effective deletion/suppression authority exists, Domain-owned ordinary participant/current-use mutations must not create fresh active authority; true races must converge into the Domain's governed deletion treatment before deletion completion can be asserted.

### Recommended JIT shape

> Enforce the invariant through an owner-boundary current-authority check/guard plus durable reconciliation for true races and failures.

This is not a frozen Ash policy/resource/locking representation.

### Retained-obligation exception

Financial dispute, Security investigation, Legal Hold, deletion evidence or processor-reconciliation state may continue only under separate category-specific authority. Such state must be minimised/restricted and cannot recreate Account, product, Entitlement or ordinary current-use authority.

### Verdict

- **NewYou semantic verdict:** PASS
- **Current implementation / operational evidence:** NOT ASSESSED
- **Recommendation class:** REQUIRED BY CURRENT AUTHORITY
- **JIT / Architectural Proof obligation:** REQUIRED
- **New working doctrine:** NONE
- **Upstream delta:** NONE
- **Cross-stream dependency:** `HSP-UPD-004` only for exact Health/Safety/Plans category treatment

### Later proof obligations

At minimum prove:

- write starts → deletion effective → write attempts commit;
- deletion starts → stale worker executes;
- owner deletion completes → stale duplicate command arrives;
- write commits immediately before suppression becomes visible → reconciliation discovers it;
- deletion process crashes/retries without restoring ordinary authority;
- retained-obligation record is written while Account/product access remains deleted.

---

# 9. Accepted pressure-test record — PRIV-PT-002

## PRIV-PT-002 — Restore a backup from before completed deletion

### Scenario

A backup is created while a participant is active. Later full deletion completes. A disaster then requires restoring the historical backup that predates deletion.

The restored bytes may legitimately contain the old Account, Entitlements, Health/Plan state, derived state and old async work.

### Governing semantic conclusion

Historical backup contents are not automatically current business authority.

A backup may contain deleted data until normal encrypted-backup expiry, but a historical restore must not recover a deleted Account or reinstate deleted current product/access authority.

The restored environment remains recovery-gated until later deletion/withdrawal truth is recovered, owner-controlled state is reconciled, derived state is rebuilt under current privacy rules, and semantic promotion checks pass.

### Rejected models

**Restore and immediately reopen service, then clean up:** REJECTED.

**Mutate every historical backup after every participant deletion:** REJECTED; current Architecture explicitly chooses normal backup ageing plus replay/reconciliation.

### Required invariant

> A historical restore must never make historically valid but subsequently deleted, withdrawn or otherwise invalid authority become present authority. Before normal service promotion, NewYou must recover and reapply later privacy/deletion truth, reconcile affected owner-controlled state and verify that deleted product/access authority has not been resurrected.

### Recommended JIT shape

```text
isolated/recovery-gated restore
→ recover post-restore-point deletion/suppression truth
→ owner-specific replay/reconciliation
→ privacy-safe derived rebuild
→ semantic verification
→ service promotion
```

Exact storage/replication/recovery representation remains downstream.

### Fail-closed recovery rule

If post-restore-point deletion/suppression truth cannot be established reliably, the restored environment must not be promoted to normal service.

### Verdict

- **NewYou semantic verdict:** PASS
- **Current implementation / operational evidence:** NOT ASSESSED
- **Recommendation class:** REQUIRED BY CURRENT AUTHORITY
- **JIT / Architectural Proof obligation:** REQUIRED
- **New working doctrine:** NONE
- **Upstream delta:** NONE
- **Cross-stream dependency:** `HSP-UPD-004` only for exact Health/Safety/Plans category disposition after restored records are rediscovered

### Existing unresolved gate preserved

`OQ-031` remains the explicit Architecture/Operations gate for backup expiry, restore isolation, deletion-ledger/suppression replay, verification and go-live criteria.

This is not duplicated as a `PRIV-UPD`.

### Later proof obligations

At minimum prove:

- restore from backup before deletion request;
- restore from backup during cancellation window;
- restore from backup after request but before irreversible execution completes;
- restore from backup before completed deletion;
- successful replay of completed deletion;
- duplicate replay/idempotency;
- crash during replay and safe resume;
- stale worker restored from historical queue state;
- physically restored Account/Entitlement never becomes servable;
- derived search/Analytics rebuild without participant resurrection;
- suppression source unavailable → promotion fails closed;
- external callback referring to deleted identity during/after recovery;
- the post-restore-point suppression source itself survives the relevant disaster class.

---

# 10. Accepted pressure-test record — PRIV-PT-003

## PRIV-PT-003 — Purpose-specific consent withdrawal while downstream work is in flight

### Scenario

Valid consent for purpose `P` authorises downstream work. The work starts. The participant then withdraws consent for `P` before the protected business consequence is completed.

### Governing semantic conclusion

Authority at job/request start does not permanently authorise the eventual protected consequence.

Current Decision authority requires consent withdrawal to stop affected processing, recalculate dependent access, and invalidate caches, permissions and derived signals.

### Important separation

Consent withdrawal is purpose-specific.

```text
withdraw purpose P
→ invalidate authority derived from P
```

It does **not** automatically mean:

```text
withdraw purpose P
→ delete every record about the participant
```

or:

```text
withdraw purpose P
→ stop every independently authorised purpose Q
```

Whether existing records must be deleted, retained, restricted, anonymised or handled under another lawful authority remains a separate category/lawful-basis question.

### Required invariant

> Purpose-specific withdrawal invalidates the withdrawn purpose as authority for future/current protected processing. Any still-pending consequence that depends on that authority must respect the current withdrawn state before becoming authoritative, and dependent active access, permissions, caches and derived signals must converge accordingly.

### Recommended JIT shape

```text
receive/execute work
→ re-read current purpose authority
→ apply owning-Domain preconditions
→ commit allowed consequence
OR
→ stop / invalidate / reconcile under governed terminal semantics
```

This does not freeze a Resource/action/event representation.

### Alternative lawful basis boundary

NewYou must not assume either that processing may continue under a different lawful basis or that it may never do so.

Where that conclusion depends on actual law, category or jurisdiction, it remains a `LEGAL / PRIVACY EXPERT GATE` unless current NewYou authority already declares the basis.

### Verdict

- **NewYou semantic verdict:** PASS
- **Current implementation / operational evidence:** NOT ASSESSED
- **Recommendation class:** REQUIRED BY CURRENT AUTHORITY
- **JIT / Architectural Proof obligation:** REQUIRED
- **New working doctrine:** NONE
- **Upstream delta:** NONE
- **Cross-stream dependency:** NONE

### Later proof obligations

At minimum prove:

- job starts → withdrawal commits → job attempts consequence;
- consequence commits immediately before withdrawal;
- duplicate withdrawal;
- withdrawal consequence crashes/retries safely;
- stale allowed cache;
- long-lived practitioner/participant session spans withdrawal;
- derived signal is invalidated from current use;
- two independent purposes where only one is withdrawn;
- late/duplicated/reordered withdrawal consequence;
- delayed Domain reconciliation cannot make stale state valid authority;
- restore predating withdrawal → withdrawal replay suppresses restored permission;
- external processor operation already in flight when withdrawal occurs.

---

# 11. Accepted pressure-test record — PRIV-PT-004

## PRIV-PT-004 — Stale, duplicated or reordered async events after deletion or consent withdrawal

### Scenario

A grant/use/create event is emitted while authority is valid. Later consent is withdrawn or deletion becomes effective. The invalidation/deletion consequence may be processed first, after which the older event is delayed, duplicated, retried or replayed.

### Governing semantic conclusion

> **Event delivery order is not authority order.**

An event may be valid evidence that something happened or that work was requested. It is not self-sufficient present permission.

A stale/duplicate/reordered event must not recreate withdrawn, deleted or otherwise invalid current-use authority.

### Rejected models

**Last delivered event wins:** REJECTED.

Transport ordering cannot become business authority.

**Globally perfect total event ordering:** REJECTED as unnecessary/disproportionate.

Even perfect ordering would not remove the need to verify current authority at protected consequence boundaries.

### Required invariant

> Delivery order, retry state or message freshness must never supersede current authoritative Privacy or owning-Domain state. Stale and duplicate work must converge without recreating withdrawn, deleted or otherwise invalid current-use authority.

### Recommended JIT shape

```text
receive durable work/evidence
→ establish operation identity / repeat safety
→ read relevant current owner + Privacy authority
→ determine whether requested consequence is still valid
→ apply once
OR
→ record superseded/no-op/reconciliation outcome
```

Exact operation IDs, sequence/version representation, worker/job structures and database concurrency mechanisms remain JIT/Architectural Proof details.

### Important distinction

Captured historical inputs may legitimately be immutable/reproducible.

Captured historical permission is **not automatically perpetual authority** for a later protected consequence.

### Verdict

- **NewYou semantic verdict:** PASS
- **Current implementation / operational evidence:** NOT ASSESSED
- **Recommendation class:** REQUIRED BY CURRENT AUTHORITY
- **JIT / Architectural Proof obligation:** REQUIRED
- **New working doctrine:** NONE
- **Upstream delta:** NONE
- **Cross-stream dependency:** NONE

### Later proof obligations

At minimum prove:

- grant event → withdrawal → delayed grant delivery;
- duplicate withdrawal/deletion event;
- grant and withdrawal delivered in reverse order;
- consumer outage → stale backlog;
- consequence commits → acknowledgement lost → retry after withdrawal;
- deletion completes → stale create/update event executes;
- restore resurrects queue → deletion replay → stale job executes;
- concurrent duplicate consumers;
- current-authority lookup unavailable → protected effect fails closed;
- old provider callback after deletion;
- stale cache disagrees with current authority;
- repeated reconciliation never recreates authority.

---

# 12. Accepted pressure-test record — PRIV-PT-005

## PRIV-PT-005 — Participant export races full deletion and concurrent mutation

### Scenario

A participant has a valid, verified asynchronous export request in progress and subsequently requests full deletion while export generation or delivery remains pending. Underlying Domain records may also mutate while export assembly is underway.

### Governing semantic conclusion

Current authority strongly governs export and full deletion independently but does not fully specify their interaction. Export is a governed data-release product whose authority/scope is revalidated at request, generation and delivery. Full deletion immediately revokes normal access and proceeds through the governed 14-day cancellation window before irreversible execution.

The unresolved interaction is whether an already-valid export request may continue after deletion is requested and, if so, where its authority terminates.

Accepted working resolution:

> A valid participant Export Request that predates a Full Deletion Request may continue only as a narrowly scoped privacy/data-rights operation during the governed deletion cancellation window, without restoring normal product access. If irreversible deletion execution begins before delivery completes, the undelivered export is cancelled and its platform-controlled temporary artefacts/delivery capability are removed under the deletion contract. Completed full deletion may not coexist with a live participant export-delivery path.

### Rejected models

Rejected as default:

1. **Immediate cancellation of every pending export at deletion request** — unnecessarily breaks the natural `export → delete` journey and conflates data-rights processing with normal product access.
2. **Pending export blocks deletion until completion** — allows an export job or processor failure to veto or indefinitely delay deletion.
3. **Unbounded parallel export and deletion lifecycles** — risks a live export artefact becoming a post-deletion access/recovery loophole.
4. **Global cross-Domain snapshot locking for export** — unnecessary unless a later explicit requirement proves a need for atomic platform-wide snapshot semantics.

### Required invariant

> Completed full deletion cannot coexist with a live NewYou-controlled export-delivery path containing the deleted participant's identifiable data.

Normal Account/product access remains revoked throughout the deletion cancellation window. A continuing export is a narrow data-rights operation, not restored product access.

### Accepted working doctrine

`PRIV-WD-001 — Pending export across full-deletion cancellation window`

> A valid participant Export Request that predates a Full Deletion Request may continue only as a narrowly scoped privacy/data-rights operation during the governed deletion cancellation window, without restoring normal product access. Export generation and delivery remain subject to current verification, authority and scope revalidation. If deletion is cancelled, the export may continue under its normal lifecycle. If irreversible deletion execution begins before delivery completes, any undelivered export is cancelled and its platform-controlled temporary artefacts/delivery capability must be removed under the deletion contract. Completed full deletion may not coexist with a live participant export-delivery path.

Status: **ACCEPTED WORKING PRE-JIT DOCTRINE / NON-AUTHORITATIVE**.

### Concurrent mutation / temporal-boundary conclusion

Export authority and export data freshness are separate concerns. NewYou must not misleadingly present a multi-Domain assembly as one coherent instantaneous snapshot unless it actually provides that consistency contract.

Exact JIT representation remains open. A later contract may use a generation cutoff, owner-specific record versions/as-of markers, or another proven temporal-boundary model. No global transaction/lock is implied.

### Recommended JIT shape

Likely later shape:

```text
verified export request
→ request-time authority/scope check
→ bounded asynchronous generation from eligible owner-controlled records
→ explicit truthful temporal boundary
→ generation-time revalidation
→ delivery-time revalidation
→ short-lived protected delivery
→ expiry/removal
```

When a later full-deletion request exists:

```text
normal product access revoked
→ export may continue only during deletion cancellation window
→ deletion cancelled: export may continue after revalidation
OR
→ irreversible deletion execution begins: undelivered export cancelled
→ export artefact/delivery capability removed
→ deletion completion only after no live export access path remains
```

Exact Resource/action/job/artefact representation remains JIT/Architectural Proof detail.

### Legal/privacy expert boundary

This working sequencing is not asserted as a POPIA, GDPR or other jurisdictional requirement. Before authoritative Product adoption, specialist legal/privacy review must validate any jurisdiction-specific access/export timelines, rights surviving deletion requests, verification rules, and restrictions on cancelling a pending access/export request.

### Verdict

- **NewYou semantic verdict:** `CHANGES REQUIRED`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `PRODUCT / POLICY DECISION` with later `LEGAL / PRIVACY EXPERT VALIDATION` and `OQ-032` operating/JIT detail
- **New working doctrine:** `PRIV-WD-001` — accepted from proposed `PRIV-WH-001`
- **Upstream delta:** `PRIV-UPD-001`
- **Cross-stream dependency:** `NONE` currently

### Upstream delta

`PRIV-UPD-001 — Pending participant export versus subsequent full deletion`

Current Product/Architecture authority should eventually clarify the authoritative interaction between an already-valid participant export request and a later full-deletion request/execution, including the deterministic boundary at irreversible deletion execution.

This working document does not itself amend upstream authority.

### Later proof obligations

Later proof must include at least:

- export requested → deletion requested immediately afterward;
- normal Account/product access remains revoked while the export continues;
- export delivered safely during the cancellation window;
- participant cancels deletion and export remains/re-enters a valid lifecycle after revalidation;
- irreversible deletion begins before export completes → export cancellation;
- export artefact generated but not delivered when irreversible deletion begins;
- delivery capability expiry/removal;
- deletion completion blocked while a live NewYou-controlled export access path remains;
- stale export worker retry after irreversible deletion;
- underlying Domain mutation during generation;
- export authority revoked between generation and delivery;
- delivery attempted after completed deletion;
- truthful temporal-boundary behaviour without unnecessary global snapshot locking.

---

# 13. Current working-doctrine register

## `PRIV-WD-001 — Pending export across full-deletion cancellation window`

**Status:** ACCEPTED WORKING PRE-JIT DOCTRINE / NON-AUTHORITATIVE  
**Origin:** `PRIV-PT-005`; accepted after explicit user approval.

Working doctrine:

> A valid participant Export Request that predates a Full Deletion Request may continue only as a narrowly scoped privacy/data-rights operation during the governed deletion cancellation window, without restoring normal product access. Export generation and delivery remain subject to current verification, authority and scope revalidation. If deletion is cancelled, the export may continue under its normal lifecycle. If irreversible deletion execution begins before delivery completes, any undelivered export is cancelled and its platform-controlled temporary artefacts/delivery capability must be removed under the deletion contract. Completed full deletion may not coexist with a live participant export-delivery path.

This doctrine remains working evidence only until any warranted upstream Product/Architecture/JIT authority change is separately governed and approved.

## `PRIV-WD-002 — Full deletion versus active recurring commercial collection`

**Status:** ACCEPTED WORKING PRE-JIT DOCTRINE / NON-AUTHORITATIVE  
**Origin:** `PRIV-PT-013`; accepted after explicit user approval.

Working doctrine:

> Once a Full Deletion Request becomes effective and normal product access is revoked, NewYou must not intentionally originate a new recurring membership collection for a service period beginning after that deletion request. Commerce must establish a deletion-driven stop-renewal consequence for the affected participant-linked recurring contract, with exact provider mechanics deferred.
>
> Financial operations already irreversibly in flight may reconcile to truthful Commerce outcomes, but they must not create or restore Entitlement or product access. A successful recurring collection that materialises after the deletion request because of an unavoidable in-flight race requires an explicit Commerce/customer-remediation outcome rather than being treated as an ordinary active-membership renewal.
>
> Completed full deletion may not coexist with participant-linked recurring provider authority that remains capable of automatically initiating future membership charges.
>
> Pending refunds, disputes and chargebacks may continue under approved restricted financial-retention authority and do not by themselves prevent unrelated deletion from proceeding.
>
> If full deletion is cancelled before irreversible execution, the exact membership/subscription restoration, reactivation and paid-period treatment requires explicit Product/Commerce policy plus provider validation.

This doctrine remains working evidence only until any warranted upstream Product/Commerce/JIT authority change is separately governed and approved.

## `PRIV-WD-003 — Full deletion across duplicate-identity reconciliation lineage`

**Status:** ACCEPTED WORKING PRE-JIT DOCTRINE / NON-AUTHORITATIVE  
**Origin:** `PRIV-PT-014`; accepted after explicit user approval.

Working doctrine:

> A candidate, unresolved, rejected or conflicted duplicate-identity reconciliation does not broaden one Account's destructive Full Deletion scope into another Account.
>
> Once an Identity & Access reconciliation is authoritatively applied and establishes one canonical participant identity, eligible participant-linked records from the reconciled Account lineages may not escape the canonical participant's Full Deletion merely because their provenance originated under the retired/non-surviving Account. Privacy deletion orchestration must use the authoritative reconciliation lineage sufficiently for each owning Domain to apply its own category-specific deletion/anonymisation/restriction contract.
>
> If Full Deletion/suppression becomes effective while merge consequences are still in flight, stale reconciliation work may not create fresh ordinary-use authority or participant linkage that bypasses deletion.
>
> If an applied reconciliation becomes actively disputed or correction/reversal-pending before irreversible cross-lineage deletion is complete, destructive propagation into the contested other lineage must fail closed pending authoritative Identity resolution rather than risk irreversible over-deletion.
>
> A later compensating reconciliation/correction may restore truthful identity provenance and current topology where possible, but it may not resurrect data validly deleted under then-effective authority, reuse a permanently retired PMR, or reconstruct completed-deletion Account/product authority.

This doctrine remains working evidence only until any warranted upstream Product/Identity/Privacy/JIT authority change is separately governed and approved.

## `PRIV-WD-004 — Moderation/security evidence after deletion and later re-registration`

**Status:** ACCEPTED WORKING PRE-JIT DOCTRINE / NON-AUTHORITATIVE  
**Origin:** `PRIV-PT-015`; accepted after explicit user approval.

Working doctrine:

> Full deletion removes ordinary Community/Account authority and applies the governed content-sensitive delete/anonymise treatment to participant-authored Community content while preserving independently authored context only as permitted by the Community deletion contract.
>
> Approved restricted moderation and security/fraud evidence may survive completed deletion under their respective retention authorities, but such evidence must remain minimised, restricted and non-reconstructive. It may not itself restore the deleted Account, PMR, Community profile, Entitlements or other product authority.
>
> A later new Account must not automatically inherit a historical moderation sanction merely because a retained identifier or weak contact match links it to the deleted Account. Where retained moderation/security evidence legitimately indicates possible sanction evasion or continuing abuse risk, it may inform a governed current Community/Security decision using sufficiently reliable identity/risk evidence, without reconstructing the deleted Account.
>
> Product/Trust & Safety policy must explicitly distinguish Account-scoped sanctions from any sanction intended to represent a human-level continuing exclusion. Implementation must not infer that scope from a generic ban/status field.

This doctrine remains working evidence only until any warranted upstream Product / Trust & Safety / Community / Security / Privacy authority change is separately governed and approved.

Future doctrine procedure remains:

1. propose `PRIV-WH-###`;
2. state the exact hole and realistic alternatives;
3. recommend one option with trade-offs;
4. STOP for explicit user acceptance;
5. only after explicit acceptance may it become `PRIV-WD-###` in a successor working document.

---

# 14. Current upstream-delta register

## `PRIV-UPD-001 — Pending participant export versus subsequent full deletion`

**Status:** OPEN WORKING UPSTREAM DELTA / NON-AUTHORITATIVE  
**Origin:** `PRIV-PT-005`  
**Likely owner:** Product Law / Privacy policy, with legal/privacy expert validation and downstream `OQ-032` operational/JIT detail.

Gap:

> Current authority governs export and full deletion independently but does not fully specify whether and for how long an already-valid participant export request survives a later full-deletion request, nor the deterministic termination boundary when irreversible deletion execution begins.

Recommended working resolution is `PRIV-WD-001`. Any actual upstream amendment must occur through normal governance and must preserve the existing immediate normal-access revocation rule.

## `PRIV-UPD-002 — Full deletion request versus recurring membership commercial contract`

**Status:** OPEN WORKING UPSTREAM DELTA / NON-AUTHORITATIVE  
**Origin:** `PRIV-PT-013`  
**Likely owner:** Product Law / Commerce policy, coordinated with Entitlements and Privacy; provider-specific execution remains under `OQ-004`.

Gap:

> Current authority does not fully specify how an effective Full Deletion Request interacts with an active recurring membership commercial contract during the 14-day cancellation window, including renewal suppression timing, deletion-cancellation restoration semantics, and customer remediation where an already-in-flight recurring charge succeeds after access has been revoked.

Accepted working resolution is `PRIV-WD-002`.

Any actual upstream amendment must settle, at minimum:

- when deletion-driven renewal suppression becomes effective;
- what cancellation of the Full Deletion Request restores commercially;
- how an already-in-flight late charge is remedied;
- how paid-period semantics behave if deletion is cancelled;
- how provider subscription termination/reactivation maps to NewYou commercial truth without turning provider state into authority.

This delta must be coordinated with the live CER Pre-JIT rather than resolved independently in Privacy.

## `PRIV-UPD-003 — Full-deletion scope across duplicate-account reconciliation`

**Status:** OPEN WORKING DELTA / NON-AUTHORITATIVE — **compression-audit classification narrowed**  
**Origin:** `PRIV-PT-014`  
**Default resolution layer after compression audit:** Identity & Access + Privacy JIT/governance with owner-Domain consequences. Escalate to Product Law only if the resolution changes participant rights, identity promises or deletion scope promised by Product.

**Historical provenance:** the accepted `PRIV-PT-014` record classified this as a Product/policy decision. That accepted record remains unchanged below. The compression audit narrows the *default escalation layer* because current Domain/Identity authority already establishes governed reconciliation, one canonical surviving identity and owner-controlled consequences.

Gap:

> Current authority does not explicitly settle the destructive Full Deletion scope across an authoritatively applied duplicate-account reconciliation lineage, especially where reconciliation is still in flight, becomes contested/correction-pending, or some owner-Domain consequences have already applied.

Accepted working resolution is `PRIV-WD-003`.

Any actual upstream amendment should settle, at minimum:

- whether an applied duplicate-account reconciliation establishes one full-deletion identity lineage across both origin Accounts;
- how deletion scope is derived from authoritative reconciliation provenance rather than current foreign keys alone;
- how merge/reconciliation and deletion races converge;
- what happens when an applied reconciliation becomes contested before irreversible cross-lineage deletion completes;
- how compensating correction behaves after data was already validly deleted;
- what minimal reconciliation/deletion provenance may survive without becoming Account/product reconstruction authority.

## `PRIV-UPD-004 — Sanction scope across full deletion and later Account creation`

**Status:** OPEN WORKING UPSTREAM DELTA / NON-AUTHORITATIVE  
**Origin:** `PRIV-PT-015`  
**Likely owner:** Product / Trust & Safety / Community / Security / Privacy governance.

Gap:

> Current authority permits restricted moderation and security/fraud evidence to survive deletion, but it does not explicitly define whether sanctions are content-scoped, Account-scoped or human-level across completed deletion and later Account creation, nor what evidence/confidence permits a later current restriction without reconstructing the deleted Account.

Accepted working resolution is `PRIV-WD-004`.

Any actual upstream amendment should settle, at minimum:

- which sanctions are content-scoped;
- which sanctions are Account-scoped;
- whether any sanctions legitimately represent a human-level continuing exclusion;
- what identity/risk evidence and confidence threshold permits applying retained evidence to a later Account;
- whether a later consequence is restoration of historical sanction state or a new current sanction based on retained evidence;
- review/appeal requirements;
- retention/minimisation boundaries;
- separation of Community moderation evidence from Security/Fraud evidence;
- external Facebook/channel implications under `OQ-023`.

This does not duplicate `OQ-023`; that gate remains the Facebook moderation/privacy operating-policy seam, whereas this delta is the provider-independent Product meaning of sanctions across deletion/re-registration.

Existing unresolved gates already cover several downstream details and must not be duplicated merely to make the Privacy Pre-JIT look more complete.

Important existing gates include:

- `OQ-004` — Paystack recurring/webhook/retry/proration/refund/chargeback validation;
- `OQ-009` — early retention categories;
- `OQ-018` — journal encryption/retention;
- `OQ-021` — video consent/retention;
- `OQ-023` — Facebook/community operating policy;
- `OQ-029` — retention schedule matrix;
- `OQ-030` — external processor deletion inventory;
- `OQ-031` — backup restore and deletion replay;
- `OQ-032` — export and deletion operations;
- `OQ-033` — professional record authority;
- `OQ-037` — RPO/RTO;
- `OQ-040` — experimentation proof including privacy/deletion handling.

A future `PRIV-UPD` is created only when a genuine upstream authority gap survives comparison against these existing gates and the full current authority set.

---

# 15. Cross-stream dependency register

## 15.1 HSP

The Health/Safety/Plans Pre-JIT stream remains a companion evidence source.

Most important current seam:

### `HSP-UPD-004`

Exact full-deletion treatment remains to be specified for categories including:

- Plan Versions;
- Generation Input Bases;
- Plan Result Provenance;
- Safety adjudications/cases;
- practitioner-derived variants.

This Privacy stream must **not duplicate** `HSP-UPD-004` as a new generic Privacy upstream delta.

Current Privacy direction is already clear:

- business-record immutability while retained is not indefinite retention;
- full deletion ends ordinary product access;
- self-guided Health data follows delete/anonymise treatment;
- formal professional records may remain subject to separately approved professional/legal retention;
- Privacy orchestrates while each owning Domain applies its record-specific treatment.

The exact category matrix remains downstream expert/JIT work.

## 15.2 CER / Commerce + Entitlements + Recurring

A separate Commerce/Entitlements/Recurring Pre-JIT stream now has a living non-authoritative repository artifact:

`working/commerce_entitlements/NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.1.0.md`

Its own README and discovery file explicitly state that it is WORKING / NON-AUTHORITATIVE PRE-JIT material and does not amend Product Law, Architecture Law, Domain Law, Roadmap, Open Work, Feature Pack contracts or JIT Domain Dossiers.

**Historical provenance note:** earlier Privacy working versions recorded that no repository CER artifact had yet been found. That statement was accurate at those earlier checkpoints and is superseded for current navigation by the artifact above; the prior versioned Privacy files remain preserved unchanged.

This Privacy stream may now use concrete accepted CER findings as cross-stream working evidence, while live governed NewYou authority still wins.

Current CER ownership boundary confirms:

- Commerce owns purchase/payment/refund/dispute and membership/subscription/add-on commercial contract truth;
- Entitlements owns entitlement/access grant identity, scope, validity, expiry, revocation and consumption;
- `money / commercial contract truth ≠ access / entitlement truth`;
- provider, browser, cache, worker and analytics state are not hidden business authority.

Privacy must still avoid inventing CER doctrine. Where a Privacy test depends on a CER conclusion, cite the smallest exact CER finding actually present.

Current Privacy/CER convergence now includes:

- `PRIV-PT-009` using the Commerce/Entitlements ownership-separation principle;
- `PRIV-PT-013` using accepted `CER-PT-004` recurring-renewal logical-collection/idempotency findings, while leaving CER cancellation/restoration/refund policy seams unresolved; PT-013 exposes `PRIV-UPD-002` / accepted `PRIV-WD-002`.

`PRIV-WD-002` is Privacy working doctrine only. It does not silently amend CER or Product Law. The exact recurring cancellation/restoration/remediation contract must converge through upstream Product/Commerce governance plus the CER stream and provider validation.

---

# 16. Accepted pressure-test record — PRIV-PT-006

## PRIV-PT-006 — External processor unavailable or delayed during deletion

### Scenario

A participant reaches irreversible full-deletion execution while one or more relevant external processors still hold participant-identifiable data. NewYou may have sent a deletion instruction, received only an acknowledgement, encountered timeout/unavailability, exhausted ordinary automated retry, or received a processor-side retention response.

### Governing semantic conclusion

Current authority already answers the central failure mode. `DEC-243` requires deletion completion to cover external paths and no recovery to remain. Privacy Domain Law requires external processors to participate through deletion/export contracts. FLOW-08 explicitly records external-processor unavailability as a durable pending/retry condition and forbids falsely marking deletion complete.

Processor/provider state remains external evidence, not NewYou deletion authority. A request sent, HTTP acknowledgement, provider request ID, exhausted retry or absence of an error is not equivalent to a sufficiently evidenced processor-side deletion/retention outcome.

### Required invariant

> NewYou must not assert full-deletion completion while any required external processor path remains unresolved. Each applicable processor path must reach an approved and sufficiently evidenced deletion or governed retained-obligation outcome before it can contribute to deletion completion.

Unknown, failed, unavailable or merely acknowledged processor outcomes remain unresolved.

### Valid convergence outcomes

A processor path may converge through:

1. sufficiently evidenced deletion under that processor's approved contract; or
2. an approved retained-obligation/restricted-retention outcome that is minimised, isolated from ordinary product use, non-reconstructive and governed by the applicable retention authority.

The following are not completion outcomes:

- request maybe sent;
- provider unavailable;
- automated retry exhausted;
- acknowledgement without completion semantics;
- provider silence;
- unsupported or unapproved retention justification.

### Rejected models

1. **Fire-and-forget deletion** — reject because transport success is not deletion truth.
2. **One synchronous global deletion request waiting on all processors** — reject because slow/unavailable providers make the privacy lifecycle brittle and unnecessarily synchronous.
3. **Assume completion after retry exhaustion** — reject because operational exhaustion cannot manufacture privacy completion.

### Recommended JIT shape

Later JIT should preserve a durable, processor-specific consequence/evidence model:

```text
Privacy deletion orchestration
→ determine applicable processor consequences
→ durably establish processor work
→ send / retry / reconcile
→ interpret evidence under processor-specific contract
→ satisfactory deletion / governed-retention outcome
OR
→ unresolved visible state + escalation / retry
→ aggregate completion only when all required paths satisfy contract
```

This does not freeze exact Resources, states, APIs, worker names, provider evidence mechanisms or retry schedules. Oban may execute durable follow-up under current Architecture, but it does not own deletion truth.

### Participant-facing truthfulness

Normal Account/product access may already be revoked while deletion orchestration remains externally unresolved. NewYou must not tell the participant that full deletion is complete while a required processor path remains pending/unknown. Exact participant-facing pending/failure language remains `OQ-032` operating/JIT work.

### Legal / privacy / vendor boundary

This Pre-JIT does not decide:

- statutory retention periods;
- processor/controller legal classification;
- whether a provider's independent obligations justify retention;
- jurisdiction-specific deletion deadlines;
- the exact evidence standard required by law for a given processor.

Those remain `OQ-029`, `OQ-030`, `OQ-032` and legal/privacy/vendor validation as applicable.

### Verdict

- **NewYou semantic verdict:** `PASS`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `REQUIRED BY CURRENT AUTHORITY` with `OQ-030`, `OQ-032` and processor/vendor/legal validation where applicable
- **New working doctrine:** `NONE`
- **Upstream delta:** `NONE`
- **Cross-stream dependency:** `NONE currently`

### Later proof obligations

Later JIT/Architectural Proof should deliberately test:

1. processor timeout during deletion;
2. repeated timeout and automated retry exhaustion;
3. crash after request sent but before local result persistence;
4. duplicate processor deletion request;
5. provider returns asynchronous acceptance only;
6. late success after NewYou previously recorded failure;
7. duplicated/reordered processor result;
8. manual reconciliation after extended outage;
9. one unresolved processor while all others complete;
10. approved retained-obligation response;
11. unsupported/unapproved provider-retention response;
12. attempted aggregate deletion completion while one processor remains unresolved;
13. restore/retry reissues the processor consequence safely;
14. retained processor-reconciliation evidence remains minimised and non-reconstructive.

---


# 17. Accepted pressure-test record — PRIV-PT-007

## PRIV-PT-007 — Legal hold applied during deletion; narrow scope; release resumes deferred deletion

### Scenario

Full-deletion execution is already underway when verified legal-hold authority becomes effective for only part of the participant estate.

Representative sequence:

```text
deletion becomes irreversible
→ some eligible owner-Domain records are already processed
→ scoped legal hold becomes effective for a defined subset
→ held deletion consequences defer
→ unrelated eligible deletion continues
→ hold remains restricted and reviewed
→ hold is released
→ previously deferred deletion resumes
```

The pressure test also covers stale/duplicate hold and release work, destructive races, and a newer hold becoming effective before an older release consequence executes.

### Governing semantic conclusion

Current authority already answers the core interaction:

- `DEC-238` requires holds to cover only necessary records, restrict ordinary use, be reviewed regularly, and resume deletion when the hold ends;
- Architecture requires legal holds to be narrowly scoped and to pause only the deletion they govern;
- Privacy & Consent owns legal-hold governance/orchestration, while underlying records remain owned by their respective Domains;
- current Domain lifecycle already includes `legal hold scoped → active/reviewed → released → deferred deletion resumes`.

Therefore a legal hold is not a participant-wide freeze and is not a mechanism for restoring deleted Account/product authority.

### Required invariant

> An effective legal hold pauses deletion only for records within its verified governed scope, keeps those records restricted from ordinary use, and does not restore Account, Entitlement, product, session or ordinary participant/staff authority. Unrelated eligible deletion continues. When the hold ends, already-deferred deletion resumes without requiring a new participant deletion request.

A stale destructive operation or stale release consequence may not bypass current hold authority.

### Important race rule

If destructive work began while no hold existed but an applicable hold becomes effective before the irreversible owner-Domain consequence commits, historical permission to delete is stale.

The owning Domain must converge on current hold authority before completing that destructive consequence.

The exact concurrency mechanism remains JIT/Architectural Proof detail.

### Already-deleted data

A later hold does not automatically reconstruct information that was validly and irreversibly deleted before the hold became effective.

NewYou must preserve truthful evidence about what actually occurred rather than manufacture historical participant data solely to make a later hold appear complete.

Any real-world requirement to recover still-available information from another lawful source is a legal/operational question, not inferred Pre-JIT doctrine.

### Hold scope

A hold may eventually use category, matter/case, date-range, evidence-linkage, record or processor selectors, but this Pre-JIT does not freeze a selector schema.

The invariant is narrower:

> Hold scope must be sufficiently specific that unrelated eligible deletion can continue.

### Release semantics

Hold release does not cancel the original full-deletion obligation.

The correct relationship is:

```text
held deletion consequence
→ hold released
→ current hold authority revalidated
→ deferred deletion resumes
```

If another applicable hold remains active, release of one hold does not authorise destruction.

### Rejected models

Reject:

1. **Participant-wide blanket freeze by default** — contradicts narrow-scope Product and Architecture authority.
2. **Hold restores ordinary Account/product access** — confuses retained data disposition with business authority.
3. **Hold release merely leaves records indefinitely retained until somebody notices** — contradicts `released → deferred deletion resumes`.
4. **Last hold/release event delivered wins** — event delivery order is not hold authority order.
5. **Later hold reconstructs already validly deleted data by default** — would invent authority and falsify history.

### Recommended JIT shape

Without freezing Resources, schemas or locking strategy:

```text
Privacy-owned current hold authority
→ owner-Domain destructive boundary checks whether applicable hold is effective
→ NO: continue governed deletion
→ YES: restrict/preserve only governed scope and defer destructive consequence
→ hold review/release
→ current authority revalidated
→ deferred deletion resumes repeat-safely
```

### Legal/privacy expert boundary

This Pre-JIT does not decide:

- who legally may issue or approve a hold;
- jurisdiction-specific preservation triggers;
- exact scope criteria;
- exact review cadence;
- statutory consequences of mistaken deletion;
- whether a particular dispute/regulatory process requires recovery from another still-lawful source.

Those remain explicit legal/privacy expert and operating-policy matters.

### Verdict

- **NewYou semantic verdict:** `PASS`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `REQUIRED BY CURRENT AUTHORITY`
- **Required invariant:** effective scoped hold beats stale destructive work for governed records; unrelated deletion continues; release resumes deferred deletion.
- **Recommended JIT shape:** Privacy-owned durable hold authority plus owner-Domain current-authority revalidation and repeat-safe defer/resume consequences.
- **New working doctrine:** `NONE`
- **Upstream delta:** `NONE`
- **Cross-stream dependency:** `NONE`

### Later proof obligations

At minimum:

1. hold active before deletion starts;
2. hold becomes effective during destructive race;
3. unrelated records continue deleting;
4. held records remain unavailable for ordinary product use;
5. duplicate hold application;
6. duplicate release;
7. stale release after a newer hold becomes active;
8. crash/retry during hold application;
9. release resumes deferred deletion without a new participant request;
10. multiple holds where one releases and another remains;
11. invalid/ambiguous hold authority fails safely without silently creating a permanent blanket freeze;
12. restore from backup reconverges current hold and deletion authority correctly.

---


# 18. Accepted pressure-test record — PRIV-PT-008

## PRIV-PT-008 — Full deletion across self-guided Health/Safety/Plans versus professional retained records

### Scenario

A participant has accumulated participant-reported Health facts, Safety evaluations/cases, immutable Plan generation inputs, generated Plan Versions, result provenance, practitioner review, practitioner-derived Plan changes and Professional Care evidence before full deletion reaches irreversible execution.

The pressure test asks which representations are deleted, irreversibly anonymised or restricted under a separately approved retention obligation, while preserving one authoritative owner per durable truth.

### Governing semantic conclusion

Current authority already establishes the core rule:

- full deletion permanently ends access to reports, Plans, programmes, progress and Entitlements;
- retained financial/professional evidence cannot restore deleted product authority;
- self-guided Health records follow deletion or irreversible-anonymisation treatment;
- formal professional records may remain only where separately approved professional retention applies and must remain restricted;
- professional-record governance does not silently transfer ownership of Health, Safety or Plan truth into Professional Care;
- record immutability while legitimately retained is not authority for indefinite identifiable retention.

The exact category-level mapping is intentionally deferred beneath existing authority.

### Ownership boundary

Deletion does not reassign business ownership:

- **Health Records** owns participant Health/lifestyle facts;
- **Safety & Eligibility** owns eligibility evaluations, restrictions, governed overrides and Safety Cases;
- **Plans & Nutrition** owns Plan generation requests/inputs, Plan Versions, Plan review/adjustment outcomes and Plan provenance;
- **Professional Care** owns professional review/case/outcome evidence;
- **Privacy & Consent** owns deletion/retention orchestration and category disposition governance, not the underlying domain records.

Practitioner involvement does not by itself transform an owner-Domain record into a Professional Care record.

### Self-guided Health

For genuinely self-guided Health data:

```text
full deletion
→ delete
OR
→ irreversibly anonymise
```

The exact category choice remains downstream Privacy/legal/JIT work.

Pseudonymisation is not automatically irreversible anonymisation.

### Safety adjudications and cases

Safety records are not automatically Health Records and not automatically Professional Care records merely because they concern health or a practitioner participated.

If no separately approved post-deletion retention authority exists, historical immutability does not justify indefinite identifiable retention.

If a particular Safety representation genuinely forms part of an approved formal professional record, that classification and retention authority must be explicit.

### Generation Input Basis

A Generation Input Basis is minimum-necessary reproducibility/provenance evidence, not permission for Plans to retain a shadow copy of the entire Health/Safety estate.

Deletion of authoritative Health data must not be defeated by indefinite participant-identifiable duplication inside Plans.

Its exact full-deletion disposition remains category-specific.

### Plan Result Provenance

Historical provenance may remain valuable while lawfully retained, but provenance value is not itself authority for indefinite participant-identifiable retention.

Where possible and appropriate, methodological/version provenance can survive independently of reconstructive participant linkage; exact treatment remains JIT/category specific.

### Plan Versions

Full deletion conclusively ends participant access/recovery to Plan Versions.

Data-retention treatment remains separate from business lifecycle:

```text
immutable while retained
≠
retain forever
```

A historical Plan Version may later be deleted, irreversibly anonymised or restricted under an independently approved obligation.

### Practitioner-derived Plan Version

Professional review or modification does not automatically transfer the authoritative resulting Plan Version to Professional Care.

Professional Care owns the professional case/review/outcome evidence; Plans & Nutrition continues to own the resulting Plan truth.

If a specific Plan artifact itself must legally/professionally form part of a formal retained record, that must be an explicit category rule rather than an accidental consequence of practitioner involvement.

### Professional Care records

Genuine formal professional records may survive completed full deletion only under separately approved professional retention authority.

They remain restricted and may not operate as a hidden:

- Account;
- Health profile;
- Plan entitlement;
- active Plan;
- product-access path.

### Cross-links

A retained professional record may preserve only the linkage/provenance necessary for its approved professional-record purpose.

That linkage cannot become an ordinary Account, Entitlement, Health-profile or product reconstruction path.

Exact identifier/linkage treatment remains JIT/legal-professional detail.

### Anti-duplication rule

Do not copy a Domain-owned record wholesale into Professional Care merely to evade its deletion treatment.

If Professional Care needs its own professional case/outcome evidence, it owns that evidence.

If an exact foreign-domain artifact must be retained for an independently approved professional/legal reason, its category treatment must be explicitly governed rather than duplicated into a competing authority.

### In-flight professional review

If full deletion becomes irreversible while professional review is in flight:

- stale work cannot produce a new participant-facing Plan or entitlement consequence;
- any required minimal professional case-closure/recordkeeping consequence may continue only under approved professional-record authority;
- recordkeeping authority cannot be converted into product-fulfilment authority.

### Re-registration

A later newly created Account for the same human does not automatically inherit or reconstruct:

- the deleted Account;
- old Entitlements;
- old Plan access;
- old Health profile;
- old Safety state.

Any lawful professional continuity mechanism would require separately governed authority.

### Existing cross-stream delta reused

This exact category seam is already recorded as:

`HSP-UPD-004`

It covers full-deletion treatment for:

- Plan Versions;
- Generation Input Bases;
- Plan Result Provenance;
- Safety adjudications/cases;
- practitioner-derived variants.

The HSP stream already classifies the **core direction as resolved** while the category matrix remains gated for Privacy/JIT/legal-professional resolution.

Therefore this Privacy stream must not create a duplicate `PRIV-UPD`.

### Required invariant

> Full deletion permanently terminates participant product/access authority. Self-guided Health and other eligible identifiable Health/Safety/Plan representations follow their approved delete or irreversible-anonymisation contracts; genuine formal professional records may remain only under separately approved professional retention authority and remain restricted/non-reconstructive. Practitioner involvement does not itself transfer record ownership or create professional-retention authority. Immutability while retained never creates indefinite identifiable retention.

### Recommended JIT shape

Use one explicit category/disposition matrix spanning the affected authoritative owner Domains.

At minimum each category should identify:

- authoritative owner;
- durable record/category meaning;
- self-guided versus formal-professional classification where applicable;
- retention authority and purpose;
- full-deletion action;
- anonymisation requirement if used;
- restricted-retention treatment if applicable;
- cross-link treatment;
- external-processor treatment;
- final disposition;
- completion/proof obligation.

Privacy coordinates the data-right lifecycle; each owner executes its own deletion/anonymisation/restriction consequence.

Do not freeze Resources/tables or solve retention by duplicating authority across Domains.

### Verdict

- **NewYou semantic verdict:** `PASS`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `REQUIRED BY CURRENT AUTHORITY` for governing invariants; `LEGAL / PRIVACY / PROFESSIONAL EXPERT DECISION` plus `JIT IMPLEMENTATION RECOMMENDATION` for exact category disposition.
- **Required invariant:** full deletion ends product/access authority; historical immutability does not justify indefinite identifiable retention; genuine professional records survive only under approved professional retention and remain restricted/non-reconstructive.
- **Recommended JIT shape:** category-specific delete/anonymise/restrict matrix coordinated by Privacy and executed through each authoritative owner.
- **New working doctrine:** `NONE`
- **Upstream delta:** `NONE`
- **Cross-stream dependency:** `HSP-UPD-004`

### Later proof obligations

At minimum:

1. self-guided Health data follows delete/anonymise disposition;
2. Safety/Plan records cannot survive indefinitely merely because immutable;
3. professional record remains restricted after Account/product deletion;
4. practitioner-derived Plan remains Plans-owned;
5. retained professional evidence cannot restore Entitlement or product access;
6. in-flight professional review cannot create participant-facing fulfilment after irreversible deletion;
7. category/linkage treatment prevents retained professional evidence from reconstructing deleted Account/Health/Plan authority;
8. duplicate records are not created merely to escape deletion treatment;
9. restore/replay preserves deleted product authority while correctly retaining only approved professional records;
10. later re-registration does not automatically reconnect retained professional records to ordinary product authority.

---


# 19. Accepted pressure-test record — PRIV-PT-009

## PRIV-PT-009 — Retained Commerce/Audit evidence after deletion must not recreate Account, Entitlement, membership or product access

### Scenario

A participant has an Account, subscription/membership, payments, Entitlements, delivered paid products, invoices/refunds/dispute evidence and audit evidence before completing full deletion.

After deletion, restricted financial/dispute and audit records may still exist under approved retention obligations. Later events may include delayed provider callbacks, chargebacks, finance/support investigation, disaster recovery, or a newly created Account for the same human.

The pressure test asks whether retained evidence can ever become a reconstruction path for deleted Account, membership, Entitlement or product authority.

### Governing semantic conclusion

Current Product Law already answers the core question:

- full deletion permanently ends participant access to reports, Plans, programmes, progress and Entitlements;
- retained financial records cannot restore them;
- only required financial/dispute evidence may be retained;
- retained commercial evidence must be isolated from product use and unusable for Account reconstruction;
- Audit & Evidence retains minimised restricted evidence and does not become the source of business facts.

The Commerce/Entitlements ownership boundary reinforces this:

```text
money / commercial contract truth
≠
access / entitlement truth
```

Historical payment/subscription truth may remain valid without any current access authority remaining valid.

### Commerce truth after deletion

Commerce may retain approved financial/dispute truth sufficient to prove or reconcile:

- payment;
- invoice/tax evidence;
- refund;
- dispute;
- chargeback;
- provider transaction/subscription evidence;
- accounting consequence.

That evidence proves historical commercial events only.

It may not:

- recreate Account authority;
- authenticate a participant;
- reissue or reactivate Entitlements;
- restart membership access;
- restore Plans/programmes/reports;
- reconstruct deleted product state.

### Provider identifiers

Provider customer IDs, transaction IDs, subscription references or payment method/token references remain external/commercial evidence.

They may not silently become:

- canonical NewYou identity;
- Account-recovery credentials;
- current Entitlement authority;
- proof that membership access should be restored.

A delayed provider callback after completed deletion may still require Commerce reconciliation, refund/dispute handling or accounting treatment, but it cannot manufacture deleted product authority.

### Historical Entitlement evidence

Completed deletion means no current Entitlement authority remains.

If a later approved retention matrix allows minimal historical Entitlement evidence to survive for evidence/reconciliation purposes, that evidence must be incapable of satisfying a current access check or reconstructing a grant.

Retention must not be represented merely as "active but hidden from UI".

The authoritative access state itself must no longer grant current access.

### Audit & Evidence boundary

Audit & Evidence may prove actions such as:

- deletion request/completion;
- Entitlement grant/revocation history;
- financial/admin action;
- authorised access to retained evidence;
- refund/dispute processing.

It must remain:

- minimised;
- restricted;
- immutable where required;
- category-specific;
- non-authoritative for source-domain business truth.

Audit must not contain a full duplicate Account/profile/subscription/Entitlement/product estate merely to preserve evidence.

Historical audit evidence such as "Entitlement granted" cannot be interpreted as current Entitlement authority after later full deletion.

### Re-registration

If the same human later creates a new Account using the same or similar contact data, retained commercial/provider/audit evidence must not automatically:

- reconnect the deleted Account;
- restore old subscription state;
- restore old Entitlements;
- restore Plans or products.

Any new current authority must arise from the new governed lifecycle, not reconstruction from retained evidence.

### Finance/support tooling

Restricted Finance/support tooling may inspect retained evidence for approved accounting/dispute/reconciliation purposes.

It must not expose or enable actions that reconstruct deleted Account/product authority from retained evidence.

UI/admin grouping does not create cross-Domain mutation authority.

### Refund/chargeback after deletion

A post-deletion refund, chargeback or dispute may continue within Commerce's approved retained-obligation boundary.

Those commercial lifecycle consequences do not require re-creating participant-facing Account, membership, Entitlement or product state.

### Restore boundary

Disaster recovery may physically restore old Account/subscription/Entitlement rows from a historical backup, but retained financial evidence does not justify their semantic restoration.

Current deletion/suppression truth still wins.

### Required invariant

> After completed full deletion, retained Commerce, provider, Entitlement-history or Audit evidence may prove historical commercial/governance facts only within its approved retained purpose. It must not recreate, authenticate, reactivate or authorise an Account, membership, Entitlement, Plan, programme or other product access. Audit evidence must remain minimised and must not become a shadow copy of source-domain truth.

### Recommended JIT shape

Keep retained evidence and current authority structurally and semantically separate:

```text
Commerce
→ restricted retained financial/dispute truth where approved

Entitlements
→ no current access authority after completed deletion
→ only separately approved minimal historical evidence if required

Audit & Evidence
→ minimal immutable proof of governed actions
→ never source-domain business truth

Privacy
→ retention/deletion orchestration + non-resurrection truth
```

Exact identifiers, record categories, retention periods and storage shapes remain JIT / `OQ-029` / Finance-Legal-Privacy detail.

### Rejected models

Reject:

1. retaining the whole Account/customer/product graph because Finance may need it;
2. deleting all commercial/audit evidence regardless of approved obligations;
3. representing deleted Entitlements as still-active records hidden only by UI filtering;
4. using provider customer/subscription identifiers as recovery or access authority;
5. allowing Finance/support tooling to restore deleted product authority from retained evidence;
6. treating historical Audit events as current source-domain state.

### Verdict

- **NewYou semantic verdict:** `PASS`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `REQUIRED BY CURRENT AUTHORITY`
- **Required invariant:** retained evidence may prove historical truth but may never become current Account/access authority or a reconstruction source.
- **Recommended JIT shape:** restricted Commerce retention, no-current-access Entitlement treatment, minimal Audit evidence and Privacy-owned suppression/non-resurrection orchestration.
- **Legal/Finance/Privacy expert boundary:** exact retained categories, identifiers and durations remain under `OQ-029`.
- **New working doctrine:** `NONE`
- **Upstream delta:** `NONE`
- **Cross-stream dependency:** `CER-PT-001` — ownership separation only.

### Later proof obligations

At minimum:

1. retained successful payment cannot satisfy an access check;
2. delayed provider success after deletion cannot issue Entitlement;
3. delayed renewal callback cannot restart membership;
4. refund/chargeback can reconcile without Account recreation;
5. Finance can inspect permitted retained evidence without ordinary product access;
6. Audit grant-history event cannot reconstruct current Entitlement;
7. Audit does not contain full duplicated sensitive/product payload;
8. new Account with same contact detail does not inherit deleted Entitlements automatically;
9. provider customer/subscription ID cannot function as Account recovery authority;
10. restore of old Account/Entitlement is suppressed despite retained financial evidence;
11. restricted evidence remains usable for approved accounting/dispute purpose;
12. deletion completion proof remains possible without reconstructing the deleted participant estate.

---


# 20. Accepted pressure-test record — PRIV-PT-010

## PRIV-PT-010 — Pseudonymised participant data remains re-identifiable

### Scenario

A deletion/anonymisation path removes obvious direct identifiers and replaces them with a stable pseudonym, token, encrypted identifier or deterministic hash, while some practical route to re-identification may still exist through NewYou, processors, Analytics, Research, retained professional/commercial evidence, derived systems or quasi-identifiers.

The pressure test asks when such a representation can truthfully be called irreversibly anonymised.

### Governing semantic conclusion

Current authority already draws the decisive line:

> pseudonymisation is not irreversible anonymisation.

Removing or replacing direct identifiers is therefore insufficient where practical re-identification remains possible.

A legitimate pseudonymous dataset may remain pseudonymous under an approved purpose/contract. It must not be silently relabelled anonymous.

### Direct mapping/linkage

If any usable mapping such as:

```text
pseudonym → Account/person
```

remains available to NewYou or an applicable processor, the representation remains pseudonymous/identifiable for governance purposes.

Deleting only the primary Account foreign key does not satisfy irreversible anonymisation if another retained mapping still permits reconnection.

### Encryption/tokenisation

Encryption, reversible tokenisation or protected identifiers improve confidentiality but do not by themselves create irreversible anonymisation while a usable decryption/re-identification capability remains.

Such data may instead be correctly governed as restricted identifiable or pseudonymous data.

### Deterministic identifiers

Stable deterministic hashes or derivations from email/phone/other identifiers are not automatically anonymous.

If candidate identifiers can reasonably be recomputed and matched, or other retained datasets permit linkage, the re-identification route still exists.

The semantic test is practical re-identifiability, not whether the stored value visually resembles personal data.

### Quasi-identifiers and sparse cohorts

A dataset may remain re-identifiable without any explicit mapping key.

Risk may arise from combinations such as:

- precise timestamps;
- location;
- age;
- rare Health attributes;
- unusual professional pathways;
- sparse cohorts;
- uncommon product combinations;
- longitudinal event sequences.

Therefore "drop direct identifiers" is not a sufficient anonymisation algorithm.

### Analytics boundary

Current Product Law requires removal of identifiable participant-level Analytics and permits only irreversibly aggregated statistics with suppression controls.

This is stronger than retaining stable participant-level pseudonyms indefinitely.

Small-group/sparse-cohort protection is therefore part of the Analytics privacy boundary.

### Research/Voting distinction

Pseudonymisation is not itself defective.

Where Research/Voting law permits a declared pseudonymous participation mode, purpose-scoped longitudinal linkage may remain as explicitly governed pseudonymous linkage.

The error would be to call such data genuinely anonymous while linkage still exists.

This pressure test does not reopen current Research/Voting deletion semantics.

### Retained professional/commercial evidence

Where approved professional, financial, dispute, security or legal-obligation records legitimately remain identifiable, they should remain truthfully classified as restricted retained identifiable records.

They need not be relabelled "anonymous" merely because ordinary product Account authority was deleted.

### External processors

If a category's deletion contract requires irreversible anonymisation and an applicable processor still possesses a usable pseudonym-to-person mapping, the processor path has not satisfied that anonymisation outcome.

Local deletion of the NewYou-side mapping alone is insufficient.

### Backups

Historical encrypted backup retention remains governed by the existing backup-expiry/deletion-replay model.

This pressure test does not require rewriting every historical backup.

The relevant requirement is that restore/replay cannot re-establish a current re-identification/reconstruction path that later privacy authority has removed.

### Derived representations

Anonymisation/deletion proof must cover applicable:

- authoritative stores;
- search/read models;
- Analytics representations;
- exports;
- caches;
- derived recommendation/projection data;
- processor copies.

A source row becoming anonymous is insufficient if a derived representation still contains a practical participant linkage.

### Access restriction is not anonymisation

A policy saying "nobody should use the linkage" or an ACL that hides it from ordinary users does not transform pseudonymous/identifiable data into irreversibly anonymous data.

Restriction and anonymisation are distinct dispositions.

### Required invariant

> A representation may be treated as irreversibly anonymised only when the governed anonymisation outcome has removed or rendered unusable the relevant practical re-identification paths across NewYou-controlled and applicable external representations. Merely replacing direct identifiers, hiding a mapping, encrypting/tokenising identifiers, hashing identifiers or restricting access does not by itself convert pseudonymous or identifiable data into irreversible anonymous data.

And:

> A legitimately pseudonymous dataset remains labelled and governed as pseudonymous; it must not be silently upgraded to an anonymity claim.

### Recommended JIT shape

Category-specific privacy disposition must distinguish the actual semantics of states such as:

```text
identifiable/current
restricted identifiable
pseudonymous
irreversibly anonymised
irreversibly aggregated
deleted
```

This is a conceptual distinction, not a demand for one universal status enum.

For a category claiming irreversible anonymisation, JIT/proof should document the actual re-identification analysis across applicable representations and processors.

Exact algorithms and acceptable re-identification thresholds remain downstream expert/JIT decisions.

### Rejected models

Reject:

1. removing direct identifiers and automatically calling the result anonymous;
2. stable pseudonym plus retained linkage map being called anonymous;
3. encrypted/tokenised identifiers with usable keys being called anonymous;
4. deterministic hashes being assumed anonymous without linkage analysis;
5. access-control policy alone being treated as anonymisation;
6. preserving participant-level pseudonymous Analytics where current Product Law requires irreversible aggregation;
7. calling restricted professional/commercial retained records anonymous when they remain intentionally identifiable.

### Verdict

- **NewYou semantic verdict:** `PASS`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `REQUIRED BY CURRENT AUTHORITY`
- **Required invariant:** any meaningful retained re-identification route means the representation has not satisfied an irreversible-anonymisation contract.
- **Recommended JIT shape:** category-specific re-identification analysis across authoritative, derived, cached and processor representations without freezing one universal anonymisation algorithm.
- **Legal / Privacy expert boundary:** exact anonymisation standards, acceptable re-identification-risk thresholds and jurisdiction-specific legal meaning require current expert review when material.
- **New working doctrine:** `NONE`
- **Upstream delta:** `NONE`
- **Cross-stream dependency:** `NONE`

### Later proof obligations

At minimum:

1. direct identifiers removed but mapping retained must not pass anonymisation proof;
2. encrypted identifier with accessible key must not pass;
3. deterministic email/phone-derived identifier is tested for recomputable linkage;
4. processor-held pseudonym-to-person mapping is included in anonymisation completion;
5. sparse cohort/quasi-identifier re-identification pressure;
6. precise timestamp/location/rare-Health combinations;
7. joinability to Finance/Audit/professional data;
8. source mapping removed while search/derived representation retains stable participant key;
9. Analytics small-group suppression prevents singleton/sparse disclosure;
10. Research pseudonymous mode remains labelled pseudonymous;
11. genuine anonymous participation has no hidden Account linkage;
12. restore/replay does not reactivate removed/suppressed linkage;
13. retained professional records remain truthfully classified as restricted identifiable rather than anonymous;
14. repeated anonymisation processing remains idempotent.

---


# 21. Accepted pressure-test record — PRIV-PT-011

## PRIV-PT-011 — Closure → reopen → deletion → new Account using same email/phone

### Scenario

Representative sequence:

```text
Account active
→ participant closes Account
→ 30-day recoverable closure
→ participant reopens same Account
→ later requests full deletion
→ 14-day deletion cancellation window
→ irreversible deletion completes
→ same human later presents the same email and/or phone during registration
```

The test separates:

1. identity continuity across recoverable closure;
2. identity severance across completed full deletion;
3. contact-identifier reuse/admission after deletion.

### Governing semantic conclusion

Current authority distinguishes recoverable closure from full deletion:

- recoverable closure preserves one Account identity and allows legitimate reopening;
- full deletion is irreversible after completion and has no Account/product reconstruction path;
- Identity & Access owns Account closure/recovery;
- Privacy & Consent owns full-deletion orchestration;
- legitimate Account reactivation preserves the same PMR;
- final deletion permanently retires that PMR and it cannot be reused.

Therefore:

```text
closure → reopen
= same Account identity
```

while:

```text
completed full deletion
→ later admitted registration
= new Account authority
```

even when contact details happen to match.

### Closure and recovery

During the governed closure-recovery window, a same-email registration attempt must not create a second parallel canonical Account merely because the original Account is closed/recoverable.

The governed path remains recovery/reopening of the existing Account.

Identity recovery restores control over the existing Account identity. It does not independently manufacture unrelated business authority; each owner Domain still determines its current valid state.

### Full deletion

Once full deletion completes:

- old recovery tokens cannot reopen the Account;
- old login/session/verification material cannot reopen the Account;
- retained payment/provider evidence cannot reopen the Account;
- old PMR cannot be reused;
- deleted Entitlement, membership, consent, Health, Plan or programme authority cannot be reconstructed.

Historical work that was valid before deletion may not cross the completed-deletion boundary and resurrect old Account authority.

### Same email / same phone after deletion

Contact equality is not identity-continuity authority.

A later Account admitted using a previously used email/phone must begin a new current identity lifecycle:

- new Account identity;
- new creation/verification lifecycle;
- new credentials/sessions;
- new PMR;
- no automatic inherited Entitlements;
- no automatic inherited membership;
- no old consent authority;
- no old Health/Plan/product authority.

The same email or phone may be evidence relevant to an Identity process, but it does not itself prove continuity with a deleted Account.

### PMR

The PMR boundary is absolute:

```text
recoverable closure → reopen
→ same PMR
```

but:

```text
completed deletion
→ old PMR permanently retired
→ later new Account receives a different PMR
```

No same-contact match may override PMR non-reuse.

### Retained evidence

Restricted Privacy, Security, Commerce, Audit, Professional or provider evidence may continue under its approved purpose.

Matching such retained evidence to a new Account does not automatically:

- recover the deleted Account;
- restore historical Account ID;
- restore old membership/subscription access;
- restore old Entitlements;
- restore old Plans/Health/product state.

Any later separately lawful professional/commercial association must be governed independently.

### Duplicate-identity reconciliation

Duplicate-identity reconciliation remains a governed Identity process.

It must not become a resurrection mechanism where a completed-deletion Account is reconstructed merely to be merged into a later Account.

Retained deletion evidence may prevent resurrection; it must not recreate the deleted identity graph.

### Contact-admission mechanics

Current Product Law does not explicitly guarantee:

> immediate reuse of the exact same email/phone after completed deletion.

Therefore this Pre-JIT does not freeze a permanent or immediate contact-release policy.

The durable semantic rule is narrower:

> If current registration/contact-admission policy admits a post-deletion registration using a previously used contact identifier, it creates new Account authority and does not recover the deleted Account.

Exact uniqueness/suppression/release mechanics remain JIT/Privacy/Identity detail.

### Registration racing deletion

A registration attempt with the same canonical contact while deletion is still in progress cannot bypass current old-Account/deletion authority and create ambiguous parallel identity.

After deletion has completed, a subsequent registration can be evaluated under current contact-admission policy.

Exact transaction/suppression coordination remains later proof work.

### Required invariant

> Recoverable Account closure preserves one canonical Account identity and legitimate reopening resumes that same identity. Completed full deletion permanently severs recovery of that Account. Any later registration admitted under current registration/contact rules creates new Account authority—even when email, phone or other human details match—and must not automatically reconnect the deleted Account, PMR, Entitlements, consent, membership, Health, Plans or other product authority.

And:

> A stale recovery, login, verification, merge or registration operation may not cross the completed-deletion boundary and resurrect old Account authority.

### Recommended JIT shape

Keep separate:

```text
Account lifecycle authority
→ Identity & Access

full-deletion/suppression authority
→ Privacy & Consent

contact uniqueness/admission mechanics
→ Identity & Access under Privacy/retention constraints

historical retained evidence
→ its owning Domain
```

Do not encode "same email means same historical Account".

### Rejected models

Reject:

1. closure always returning through a brand-new Account;
2. completed deletion becoming reversible when the same email returns;
3. same email/phone automatically implying continuity with the deleted Account;
4. old PMR reuse after final deletion;
5. retained Commerce/Audit/Professional/provider evidence automatically re-linking a new Account to deleted authority;
6. stale recovery/merge/verification work overriding completed deletion.

Do not freeze a permanent same-email block either; that is a separate contact-admission/retention question.

### Verdict

- **NewYou semantic verdict:** `PASS`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `REQUIRED BY CURRENT AUTHORITY` for identity continuity/non-reconstruction; `JIT IMPLEMENTATION RECOMMENDATION` for post-deletion contact-admission mechanics.
- **Required invariant:** recoverable closure preserves identity continuity; completed deletion permanently terminates that Account's recovery; any later admitted Account is new authority and inherits nothing automatically.
- **Recommended JIT shape:** Identity-owned canonical Account/contact lifecycle, Privacy-owned deletion/suppression, current-authority checks at recovery/registration boundaries and a new PMR for every genuinely new Account.
- **New working doctrine:** `NONE`
- **Upstream delta:** `NONE`
- **Cross-stream dependency:** `NONE`

### Later proof obligations

At minimum:

1. same-email attempt during recoverable closure does not create a second Account;
2. closure reopening resumes the same Account/PMR;
3. old recovery token after deletion request cannot restore normal access;
4. old recovery/login/verification work after completed deletion cannot reopen the Account;
5. same-email registration during deletion execution does not create ambiguous parallel identity;
6. post-deletion admitted registration creates new Account identity and new PMR;
7. retained Commerce/Audit/Professional/Security/provider evidence does not auto-relink the new Account;
8. old Entitlements/membership/consent/Health/Plans are not inherited;
9. old PMR collision/reuse is impossible;
10. duplicate-identity reconciliation cannot reconstruct a completed-deletion Account;
11. restore/replay cannot turn historical closure/recovery evidence into post-deletion Account recovery;
12. contact-admission implementation remains non-enumerating and privacy-safe.

---


# 22. Accepted pressure-test record — PRIV-PT-012

## PRIV-PT-012 — Export of mixed active / retained / deleted categories

### Scenario

A participant export request is assembled while the participant estate contains a mixture of:

- active participant records;
- historical participant-accessible records;
- restricted professional records;
- retained financial/dispute evidence;
- legal-hold records;
- minimal Audit/security evidence;
- irreversibly anonymised representations;
- already-deleted records.

The pressure test asks whether physical existence or historical linkage is enough to make a representation export-eligible.

### Governing semantic conclusion

Current Architecture defines export as a governed data-release product assembled from **eligible Domain-owned records**, with authority and scope revalidated through request, generation and delivery.

Therefore:

```text
record exists
≠
record is export eligible
```

Export eligibility follows current Domain/category/access authority.

Privacy orchestrates the export lifecycle but does not become the owner or semantic interpreter of every foreign Domain record.

### Active and historical participant records

Ordinary current or historical participant records may be exportable where the owning Domain's current participant-release contract says they are eligible.

Each owner Domain supplies the governed participant-release representation.

Privacy assembles those owner outputs rather than querying persistence indiscriminately.

### Already-deleted records

A record validly and irreversibly deleted before a later export must not be reconstructed from:

- backups;
- retained Finance evidence;
- Audit history;
- derived stores;
- processor evidence;

merely to make an export appear "complete".

Completed governed deletion is not an export failure.

### Irreversibly anonymised records

If a representation is genuinely irreversibly anonymised, a later export must not recreate participant linkage.

If NewYou can reliably re-link it merely to export it, the earlier anonymisation claim must be re-examined.

### Restricted professional records

Current Product Law preserves a participant-access principle for professional records, while `OQ-033` deliberately leaves the exact participant-access/export boundary to Clinical/Legal review.

Therefore professional retention does not imply automatic exclusion, but neither does participant accessibility mean every professional artifact belongs unchanged in every generic export.

Exact representation/scope remains expert/JIT work.

### Retained financial/dispute evidence

Required financial/dispute evidence may remain under approved retention.

Physical retention alone does not make every retained commercial record export-eligible.

Some participant-facing commercial records may be eligible; other provider, dispute, accounting, fraud or reconciliation evidence may not be.

Exact access/export treatment remains category-specific under Finance/Legal/Privacy review.

### Legal-hold records

A legal hold changes retention/disposition authority for scoped records.

It does not by itself settle whether a participant data-rights export must include or exclude those records.

Reject blanket rules of:

```text
legal hold → always include
```

and:

```text
legal hold → always exclude
```

The governing legal/category access rule decides the participant-release consequence.

### Audit and security evidence

Audit & Evidence is not source-domain truth.

A participant export must not simply dump internal:

- security detections;
- abuse evidence;
- privileged investigations;
- internal Audit payloads;

merely because those records mention the participant.

Any participant-access obligation for such categories must be explicitly governed.

### No reconstruction through mixed joins

Export assembly must not use retained professional, commercial, security or Audit relationships to reconstruct a deleted Account or deleted product relationships.

Current eligible relationships govern the export; technical joinability does not create export authority.

### Eligibility changes while export runs

Request-time eligibility is not permanent authority.

Where category/access/privacy state changes during generation, current authority must be revalidated.

Likewise a generated export artifact is not automatically deliverable after its authority changes; `PRIV-WD-001` already governs the export-versus-full-deletion boundary.

### Truthful completeness

NewYou should not describe the export as "everything NewYou has ever had about you" unless that is literally and legally true.

The semantic product is a governed export of records currently eligible for participant release.

Exact participant-facing wording remains JIT/legal review.

### Deleted versus withheld versus no records

Internally, owner export contracts must distinguish enough meaning to avoid conflating:

- no records ever existed;
- eligible records were deleted;
- records are no longer participant-linked after anonymisation;
- retained records exist but are not currently export-eligible;
- owner export processing failed/unresolved.

Exact status vocabulary remains JIT detail.

### Required invariant

> Participant export includes only records and representations currently eligible for participant release under their authoritative Domain/category contract. Physical retention, legal hold, professional retention, Audit presence or historical linkage does not by itself create export eligibility. Records already deleted or irreversibly anonymised must not be reconstructed merely to satisfy an export. Export assembly must not become a path for reconstructing deleted Account/product relationships.

And:

> Owner-Domain export eligibility must be revalidated under current authority during generation and delivery, not frozen permanently when the Export Request was created.

### Recommended JIT shape

Each owner Domain should expose a governed export consequence capable, conceptually, of distinguishing:

```text
eligible participant-release payload

no eligible participant records

separate/restricted access path

unresolved failure
```

Privacy assembles owner outputs and manages protected delivery.

Do not create a central Privacy persistence query layer that reimplements all Domain retention/access semantics.

### Rejected models

Reject:

1. export every record physically linked to the participant;
2. export only currently active product records;
3. reconstruct deleted or anonymised records for export completeness;
4. generic export of all retained professional/financial/security/Audit evidence;
5. blanket legal-hold include/exclude policy;
6. treating zero returned rows as automatically equivalent to a successful no-record condition;
7. allowing historical joins to reconstruct deleted Account/product relationships.

### Verdict

- **NewYou semantic verdict:** `PASS`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `REQUIRED BY CURRENT AUTHORITY`, with `LEGAL / PRIVACY / PROFESSIONAL / FINANCE EXPERT DECISION` for specific retained-category participant-access boundaries.
- **Required invariant:** `stored ≠ export eligible`; `deleted/anonymised ≠ reconstruct for export`.
- **Recommended JIT shape:** owner-Domain export contracts returning currently eligible participant-release representations or explicit governed non-release/failure outcomes, assembled by Privacy.
- **New working doctrine:** `NONE`
- **Upstream delta:** `NONE`
- **Cross-stream dependency:** `NONE`

### Later proof obligations

At minimum:

1. active eligible record exports correctly;
2. historical but still participant-accessible record exports correctly;
3. deleted record is not reconstructed;
4. irreversibly anonymised record is not re-linked;
5. retained professional record follows the approved participant-access/export contract;
6. retained financial evidence does not automatically become exportable merely because stored;
7. legal-hold record follows category/legal access authority rather than blanket include/exclude;
8. Audit/security evidence is not dumped as source-domain data;
9. zero eligible records is distinguished from owner-contract failure;
10. eligibility changes during generation;
11. deletion starts after artifact generation but before delivery;
12. mixed retained records cannot reconstruct deleted Account/Entitlement/product relationships;
13. one owner Domain fails/times out while others complete and export does not falsely claim completion;
14. participant-facing exclusion explanation does not leak restricted security/legal information.

---


# 23. Accepted pressure-test record — PRIV-PT-013

## PRIV-PT-013 — Deletion with refund/dispute/chargeback or active recurring membership

### Scenario

A participant has an active recurring membership and may also have a pending refund, dispute or chargeback when a Full Deletion Request becomes effective.

Representative race:

```text
active recurring membership
→ participant requests full deletion
→ normal product access revoked immediately
→ 14-day deletion cancellation window
→ next renewal falls inside the window
→ provider/Commerce evidence may be delayed, duplicated or already in flight
```

The pressure test separates:

1. pending financial/dispute obligations;
2. recurring collection that has not yet begun;
3. recurring collection already irreversibly in flight;
4. provider recurring authority that could continue creating future charges;
5. deletion cancellation and commercial restoration semantics.

### What current authority already settles

Current Product/Domain authority already establishes:

- full deletion immediately revokes normal product access before irreversible execution;
- completed deletion permanently ends reports, Plans, programmes, progress and Entitlements;
- required financial/dispute evidence may survive only under restricted retained authority and cannot reconstruct Account/product authority;
- Commerce owns payment/refund/dispute and subscription/membership contract truth;
- Entitlements owns access truth;
- provider state is evidence/execution state, not NewYou business authority.

Therefore pending refunds, disputes and chargebacks may continue under approved restricted Finance/Commerce authority without keeping the participant Account or Entitlements alive.

Unrelated eligible deletion continues.

### The recurring-membership gap

Current authority does not fully specify what happens when the next recurring collection would occur during the 14-day Full Deletion cancellation window after normal product access has already been revoked.

Continuing normal recurring billing throughout that window would risk intentionally charging for a new service period while ordinary membership access is unavailable.

Privacy directly owning/cancelling provider subscriptions would violate Commerce ownership.

The accepted working direction is therefore:

```text
effective Full Deletion Request
→ normal access revoked
→ Commerce receives deletion-driven stop-renewal consequence
→ no intentional new recurring collection for a future service period
```

with provider-specific mechanics deferred.

### Already-in-flight recurring collection

A recurring collection that was already irreversibly in flight before or across the deletion boundary cannot be wished away.

Provider timeout or delayed evidence does not prove that no charge occurred.

Commerce must reconcile the truthful commercial outcome using the stable logical recurring-collection identity.

If a late success materialises:

```text
Commerce reconciles money truth
→ Entitlements remain non-authorising
→ customer remediation follows explicit commercial policy
```

The late payment must not restore membership access merely because payment succeeded.

### Customer remedy remains upstream policy

Ordinary membership cancellation/no-partial-period-refund semantics do not clearly answer a recurring charge that succeeds after deletion has already revoked access.

Exact remediation may include refund/credit/other governed treatment, but this Pre-JIT does not invent the final policy.

That is part of `PRIV-UPD-002` and the CER/Product seam.

### Deletion completion

By verified full-deletion completion, participant-linked recurring provider authority must no longer remain capable of automatically initiating future membership charges.

A provider subscription still capable of creating future charges is an unresolved external/commercial path, not merely retained historical evidence.

Commerce owns the stop-renewal/provider consequence; Privacy owns aggregate deletion orchestration/completion.

### Deletion cancellation

If the participant cancels full deletion before irreversible execution, the exact commercial restoration semantics remain genuinely unresolved.

Possible outcomes differ materially:

- restore prior provider subscription where possible;
- resume/recreate subscription without duplicating paid-period value;
- require a fresh subscription;
- other governed paid-period treatment.

This choice belongs to Product/Commerce governance plus provider validation.

It must not be hidden in adapter code.

### Pending refund/dispute/chargeback

Pending financial operations do not by themselves prevent unrelated deletion.

They may continue using approved restricted commercial evidence.

They cannot:

- restore Account authority;
- recreate Entitlements;
- reactivate membership access;
- prevent deletion of unrelated eligible records.

### Required invariant

> Once a Full Deletion Request has revoked normal product access, NewYou must not intentionally create a new recurring charge for a future membership service period dependent on that revoked access. Already-in-flight financial truth must be reconciled honestly but cannot create new Entitlement/access authority. By verified deletion completion, the affected recurring provider contract must no longer be capable of initiating future participant-linked membership charges.

Pending refund/dispute/chargeback work may continue under restricted retained financial authority without rebuilding the deleted product relationship.

### Accepted working doctrine

`PRIV-WD-002 — Full deletion versus active recurring commercial collection`

This is accepted non-authoritative Pre-JIT doctrine, not Product Law.

### Upstream delta

`PRIV-UPD-002 — Full deletion request versus recurring membership commercial contract`

The upstream Product/Commerce contract still needs to govern:

- renewal-suppression effective point;
- deletion-cancellation restoration/reactivation;
- late in-flight charge remedy;
- paid-period treatment;
- exact provider subscription mapping.

### Recommended JIT shape

Preserve ownership:

```text
Privacy
→ authoritative deletion lifecycle/orchestration

Commerce
→ recurring contract/payment/refund/dispute truth
→ stop-renewal/provider reconciliation/remediation

Entitlements
→ current access authority

Provider
→ external execution/evidence
```

Deletion supplies a governed consequence to Commerce.

Commerce performs provider-specific work.

Entitlements do not infer access from late payment evidence.

### Rejected models

Reject:

1. intentionally continuing normal future-period recurring billing throughout the deletion cancellation window;
2. Privacy directly taking ownership of Commerce/provider subscription mutation;
3. treating a late successful charge as permission to restore Entitlement;
4. declaring deletion complete while the participant-linked recurring provider contract can still automatically create future charges;
5. treating pending refund/dispute/chargeback work as a reason to retain/reconstruct ordinary Account/product authority;
6. burying deletion-cancellation commercial restoration policy solely inside provider integration code.

### Verdict

- **NewYou semantic verdict:** `CHANGES REQUIRED`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `PRODUCT/POLICY DECISION`, coordinated with CER, followed by provider validation under `OQ-004`.
- **Required invariant:** no intentional new future-period recurring collection after deletion has revoked normal access; in-flight money truth reconciles without restoring access; completed deletion leaves no future-charge-capable recurring membership authority.
- **Recommended JIT shape:** Privacy deletion consequence → Commerce-owned stop-renewal/reconciliation → Entitlements remain non-authorising → provider-specific implementation beneath that contract.
- **New working doctrine:** `PRIV-WD-002 — ACCEPTED`
- **Upstream delta:** `PRIV-UPD-002 — OPEN WORKING UPSTREAM DELTA`
- **Cross-stream dependency:** CER recurring logical-collection/idempotency findings plus unresolved CER renewal/cancellation/refund policy seams.

### Later proof obligations

At minimum:

1. deletion request becomes effective before a scheduled future renewal;
2. future renewal is suppressed without Privacy owning Commerce persistence/provider mechanics;
3. provider mutation/reconciliation retries are idempotent;
4. renewal already irreversibly in flight when deletion request becomes effective;
5. provider success arrives after access revocation;
6. late success reconciles Commerce truth but cannot issue/restore Entitlement;
7. customer-remediation consequence is explicit and repeat-safe;
8. deletion cancellation before irreversible execution follows governed commercial restoration semantics;
9. provider subscription remains unavailable/ambiguous and deletion completion fails closed until required external consequence resolves;
10. completed deletion leaves no provider recurring authority capable of creating future charges;
11. pending refund/dispute/chargeback continues under restricted evidence without Account recreation;
12. duplicate/reordered renewal/refund/dispute evidence does not create duplicate commercial or access consequences;
13. restore/replay does not reactivate a deleted recurring membership;
14. Finance/support tooling cannot manually reconstruct deleted access from retained commercial evidence.

---


# 24. Accepted pressure-test record — PRIV-PT-014

## PRIV-PT-014 — Identity merge/unmerge where one side enters deletion

### Scenario

Two Accounts are suspected or confirmed duplicates and participate in governed Identity reconciliation. Before, during or after reconciliation, one side enters full deletion.

The pressure test distinguishes:

- candidate/unresolved reconciliation;
- authoritatively applied reconciliation;
- in-flight owner-Domain merge consequences;
- later correction/compensating reconciliation;
- stale merge/deletion work.

### Governing semantic conclusion

Current architecture already establishes that duplicate-identity merge is governed reconciliation rather than destructive row collapse, and that owner Domains preserve their own business-record authority/provenance.

The missing semantic is the exact Full Deletion scope across an applied reconciliation lineage.

### Candidate / unresolved reconciliation

A candidate, unresolved, rejected or conflicted duplicate case does not prove that two Accounts are the same participant.

Therefore deletion for Account A must not automatically destroy Account B's estate merely because a duplicate candidate exists.

Unproven identity similarity cannot broaden irreversible destructive authority.

### Authoritatively applied reconciliation

Once Identity & Access has authoritatively applied reconciliation and established one canonical participant identity, records from the retired/non-surviving Account lineage must not escape deletion merely because their provenance originated under the earlier Account.

Deletion scope therefore cannot be implemented as only:

```text
records where current account_id = canonical_account_id
```

where authoritative reconciliation provenance says additional records remain participant-linked to the same canonical identity.

### Ownership

Privacy does not centrally rewrite all foreign Domain records.

Identity & Access owns reconciliation lineage/provenance.

Privacy owns deletion/suppression orchestration.

Each owning Domain applies its own record consequence:

- delete;
- irreversibly anonymise;
- restrict/retain where independently approved.

### Merge racing deletion

If deletion/suppression becomes effective while reconciliation consequences are still in flight, stale reconciliation work cannot create fresh ordinary-use participant linkage or active authority that bypasses deletion.

Current Privacy authority must be revalidated before a consequence that would re-establish active participant linkage.

### Stale source deletion

The opposite error is also dangerous.

After A has been reconciled into canonical B, a stale old instruction that says "delete Account A" cannot blindly destroy everything currently associated with B.

The operation must resolve current authoritative identity/deletion scope.

This pressure test therefore protects against both:

```text
merge hides data from deletion
```

and:

```text
stale source deletion over-deletes the surviving identity
```

### Correction / compensating reconciliation

A later correction does not erase historical reconciliation provenance.

It creates compensating truth.

If data was legitimately and irreversibly deleted under then-effective authority, later correction cannot reconstruct that data merely to restore the previous topology.

Likewise a permanently retired PMR cannot be resurrected.

### Contested applied reconciliation

The hardest case is an applied reconciliation that becomes actively disputed/correction-pending before irreversible cross-lineage deletion is complete.

Automatically continuing destructive propagation into the contested other lineage risks unrecoverable over-deletion.

The accepted working rule is to fail closed on cross-lineage destructive propagation pending authoritative Identity resolution.

This does not necessarily halt unrelated deletion outside the contested scope.

### Required invariant

> Duplicate-account reconciliation may neither become a deletion escape hatch nor an over-deletion mechanism. An authoritatively applied identity reconciliation must preserve enough lineage for eligible records from the reconciled participant estate to receive their proper deletion treatment, while unresolved/conflicted identity candidates cannot broaden irreversible deletion into another Account. Stale merge/correction work may not resurrect suppressed or completed-deletion authority.

### Accepted working doctrine

`PRIV-WD-003 — Full deletion across duplicate-identity reconciliation lineage`

### Upstream delta

`PRIV-UPD-003 — Full-deletion scope across duplicate-account reconciliation`

### Recommended JIT shape

Conceptually:

```text
Identity & Access
→ authoritative reconciliation case/lineage/status/provenance

Privacy
→ deletion/suppression authority

each owning Domain
→ evaluates its own records/provenance
→ applies governed delete/anonymise/restrict consequence

Audit
→ minimal reconciliation/deletion evidence
```

Do not use a universal shared-write Account-FK migration or let Privacy become foreign-record owner.

### Rejected models

Reject:

1. deletion based only on current canonical Account foreign key;
2. any suspected duplicate automatically broadening deletion to both Accounts;
3. Privacy centrally migrating/deleting all foreign Domain records;
4. stale merge work recreating active linkage after deletion suppression;
5. stale source deletion blindly destroying canonical-survivor data;
6. compensating reconciliation resurrecting validly deleted data or retired PMR;
7. continuing irreversible cross-lineage deletion while the authoritative reconciliation itself is actively contested.

### Verdict

- **NewYou semantic verdict:** `CHANGES REQUIRED`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `PRODUCT/POLICY DECISION`, with downstream `Identity + Privacy JIT / Architectural Proof`.
- **Required invariant:** merge cannot hide participant data from deletion; unproven/contested merge cannot expose another Account to irreversible deletion.
- **Recommended JIT shape:** Identity-owned reconciliation provenance + Privacy-owned deletion lifecycle + owner-Domain consequences.
- **New working doctrine:** `PRIV-WD-003 — ACCEPTED`
- **Upstream delta:** `PRIV-UPD-003 — OPEN WORKING UPSTREAM DELTA`
- **Cross-stream dependency:** `NONE`

### Later proof obligations

At minimum:

1. A/B candidate merge + A deletion does not delete B;
2. applied A→B reconciliation + B deletion includes eligible A-origin records;
3. applied reconciliation retains immutable source provenance;
4. merge worker races deletion suppression;
5. stale merge worker cannot attach active A authority under B after suppression;
6. stale source-A deletion after A→B cannot blindly over-delete B;
7. source PMR remains permanently retired;
8. reconciliation correction uses compensating provenance rather than history erasure;
9. correction after valid deletion cannot resurrect deleted data;
10. applied reconciliation becomes disputed before cross-lineage deletion commits and destructive propagation fails closed;
11. each owner Domain independently applies its record consequence;
12. retained professional/commercial evidence still follows its own retention authority;
13. duplicate/reordered merge/deletion commands converge;
14. restore/replay preserves both reconciliation lineage and later deletion suppression without resurrection;
15. minimal reconciliation evidence cannot become a hidden reconstruction graph.

---


# 25. Accepted pressure-test record — PRIV-PT-015

## PRIV-PT-015 — Community/moderation/security evidence after deletion

### Scenario

A participant has Community-authored content, other participants' replies/context, moderation reports/actions/sanctions/appeals and Security/Fraud evidence before completing full deletion.

Later, the same human may create a genuinely new Account.

The pressure test separates:

- participant-authored Community content;
- independently authored context;
- Community moderation evidence;
- Security/Fraud evidence;
- current sanction authority on a later Account.

### Governing semantic conclusion

Current Product Law already establishes:

- content-sensitive deletion/anonymisation for Community;
- preservation of independently authored context where appropriate;
- restricted moderation evidence retention;
- minimised security/fraud evidence under security-specific identifiers for an approved period.

These categories must not be collapsed into one deletion rule.

The remaining gap is the Product/Trust & Safety meaning of sanctions/evidence after completed deletion and later Account creation.

### Participant-authored content

Participant-authored posts/comments/replies may be deleted or anonymised according to the Community deletion contract.

The treatment must be content-sensitive rather than a blanket "delete every related row" rule.

### Independently authored context

Another participant's independently authored reply/context may survive where appropriate.

Preserving that context does not authorise preservation of the deleted participant's ordinary Account identity.

Quotes, mentions, embeds, previews, attachments and attribution require explicit Community JIT treatment so surviving context does not accidentally defeat deletion/anonymisation.

### Deleted-participant attribution

Ordinary Community surfaces must not preserve a hidden reconstructive path to the deleted Account, PMR or profile.

A surviving conversation may use an anonymised/deleted-author representation where the Community contract permits it, but preserving context does not preserve product identity authority.

### Moderation evidence

A moderation report, investigation, sanction, appeal or decision does not need to disappear merely because the participant deletes the Account.

Approved moderation evidence may survive in restricted form.

It must not become a shadow Account/profile containing unnecessary Health, Plan, Commerce or other product data.

### Security/Fraud evidence

Security/Fraud evidence is a separate category.

It may survive under approved retention using security-specific identifiers.

A security identifier is not an Account, PMR, entitlement or product identity.

Security evidence cannot itself authenticate or reactivate the deleted Account.

### Ban state versus retained ban evidence

While an Account exists, Community may own a current participation restriction/ban.

After completed deletion there is no ordinary Community participation authority for that Account.

What may survive is restricted evidence that the sanction/event occurred.

That distinction matters if a later genuinely new Account is created.

### Later re-registration gap

Current authority does not clearly establish whether a historical sanction is:

- content-scoped;
- Account-scoped;
- human-level across future Accounts;
- or merely evidence that may trigger a new governed current review/restriction.

Automatic sanction inheritance based on weak identifier/contact matching is unsafe and can make retained evidence into hidden identity authority.

Deleting all moderation/security evidence is also unsafe because deletion could become a trivial sanction-evasion mechanism.

### Accepted working direction

The safe provider-independent model is:

```text
old Account deleted
→ no Account reconstruction

approved moderation/security evidence retained
→ restricted purpose only

later new Account
→ retained evidence may inform a governed current Community/Security decision
→ sufficiently reliable identity/risk evidence required
→ no automatic restoration of deleted Account state
```

Any human-level continuing exclusion must be explicit Product/Trust & Safety policy rather than inferred from a generic ban field.

### External Facebook launch channel

External Facebook/community-provider mechanics remain separate operating/provider questions.

`OQ-023` continues to own Facebook moderation/privacy operating policy.

This Pre-JIT does not invent Meta-specific deletion, ban or identity semantics.

### Required invariant

> Full deletion may not erase independently authorised restricted moderation/security evidence merely to permit sanction evasion, but retained evidence may not become a hidden reconstruction of the deleted Account. Participant-authored Community content, independently authored context, moderation evidence and security/fraud evidence remain distinct governed categories. Any later consequence for a newly created Account must arise from current Community/Security authority rather than automatic resurrection of deleted Account state.

### Accepted working doctrine

`PRIV-WD-004 — Moderation/security evidence after deletion and later re-registration`

### Upstream delta

`PRIV-UPD-004 — Sanction scope across full deletion and later Account creation`

### Recommended JIT shape

Conceptually:

```text
Community
→ participant-authored content
→ moderation case/evidence
→ current Community sanctions

Security
→ minimised security/fraud evidence
→ security-specific identifiers

Privacy
→ deletion/retention orchestration

Identity
→ current Account identity only

later Account risk path
→ retained evidence may be consulted under governed policy
→ current decision
→ no old Account reconstruction
```

Do not centralise all of this in Privacy.

### Rejected models

Reject:

1. deleting every independently authored reply/context solely because the original author deleted their Account;
2. retaining full participant identity/profile merely to preserve Community context;
3. deleting all moderation/security evidence and allowing deletion to become a sanction-evasion mechanism;
4. treating retained moderation/security evidence as an active Account;
5. automatically imposing a historical sanction on a later Account from weak contact/identifier matching;
6. inferring human-level permanent exclusion from a generic `ban = true`;
7. using ordinary Account IDs/PMRs indefinitely as the retained Security identity model.

### Verdict

- **NewYou semantic verdict:** `CHANGES REQUIRED`
- **Current implementation / operational evidence:** `NOT ASSESSED`
- **Recommendation class:** `PRODUCT / TRUST & SAFETY / PRIVACY POLICY DECISION`, followed by Community/Security JIT and `OQ-023` validation for the Facebook launch channel.
- **Required invariant:** retained moderation/security evidence may support legitimate anti-abuse purposes without reconstructing deleted Account authority; a later Account consequence must arise from governed current authority.
- **Recommended JIT shape:** Community-owned moderation truth + Security-specific retained evidence + Privacy orchestration + Identity-owned current Account, with governed evidence-based re-evaluation rather than automatic sanction resurrection.
- **New working doctrine:** `PRIV-WD-004 — ACCEPTED`
- **Upstream delta:** `PRIV-UPD-004 — OPEN WORKING UPSTREAM DELTA`
- **Cross-stream dependency:** `NONE`

### Later proof obligations

At minimum:

1. deleted participant-authored content follows content-sensitive delete/anonymise treatment;
2. independently authored reply survives where appropriate without deleted Account attribution;
3. quote/mention/embed handling does not accidentally defeat deletion;
4. restricted moderation case survives without ordinary Community visibility;
5. moderation evidence does not retain unnecessary Health/Plan/purchase/profile data;
6. Security evidence uses approved security-specific identifiers;
7. Security evidence cannot authenticate/reactivate deleted Account;
8. old PMR cannot be recreated from retained moderation/security evidence;
9. later Account weakly matching deleted Account does not automatically inherit sanction;
10. strong governed anti-abuse evidence may trigger the eventually approved current review/restriction path;
11. Account-scoped versus human-level sanction semantics are explicit;
12. appeal/review works where applicable without Account reconstruction;
13. moderation/security retention expires under the approved schedule;
14. restore/replay cannot re-expose deleted participant identity in ordinary Community surfaces;
15. external Facebook behaviour is validated independently under `OQ-023`.

---

# 26. Current consolidated invariants discovered/confirmed through PRIV-PT-015

These are not new Product Law; they are the cumulative semantic consequences already required by current authority and confirmed under pressure.

1. **Privacy orchestration does not create shared-write Domain ownership.**
2. **Deletion/withdrawal current authority overrides stale ordinary current-use work.**
3. **True races may require reconciliation, but reconciliation is not the primary permission model.**
4. **Historical backup bytes are not automatically present authority.**
5. **Restored service remains recovery-gated until later privacy truth is replayed/reconciled and semantic authority is verified.**
6. **A backup restore cannot recover a completed-deletion Account or product access.**
7. **Purpose-specific consent withdrawal invalidates that purpose's current authority without automatically becoming full deletion.**
8. **Independent purpose/lawful-basis dimensions must not be silently collapsed into one global consent boolean.**
9. **Async event delivery order is not business-authority order.**
10. **Jobs/events/providers carry evidence or historical intent, not perpetual permission.**
11. **Protected consequences re-evaluate current authority at the owning boundary.**
12. **Caches/projections/derived state may accelerate or represent current state but cannot supersede durable authority.**
13. **Retained-obligation evidence may survive only under its own minimised/restricted authority and cannot reconstruct ordinary Account/product/Entitlement authority.**
14. **Where law determines whether processing may continue after consent withdrawal or how retained categories are treated, the answer remains an explicit legal/privacy expert matter rather than guessed Pre-JIT doctrine.**
15. **Participant export is a governed data-rights operation, not ordinary product access.**
16. **A pending export may not indefinitely block full deletion.**
17. **Completed full deletion cannot coexist with a live NewYou-controlled export-delivery path for the deleted participant.**
18. **Export authority/scope and export data-freshness/temporal-boundary semantics are separate concerns.**
19. **A multi-Domain export must not claim atomic snapshot consistency unless NewYou actually provides that contract.**
20. **A required external processor path that is unresolved, unavailable, failed or of unknown outcome prevents verified full-deletion completion.**
21. **Processor request/transport acknowledgement is evidence of delivery, not automatically evidence of processor-side deletion completion.**
22. **Retry exhaustion is an operational state, not a privacy completion state.**
23. **A processor-side retained-obligation outcome is acceptable only when independently approved and governed; provider preference alone does not create retention authority.**
24. **A legal hold pauses only deletion within its verified governed scope; unrelated eligible deletion continues.**
25. **Held records remain restricted and do not restore Account, Entitlement, product, session or ordinary-use authority.**
26. **A hold that becomes effective before a destructive owner-Domain consequence commits overrides stale prior permission to delete.**
27. **Hold release resumes the already-deferred deletion obligation; it does not require a new participant deletion request.**
28. **Release of one hold cannot destroy data still governed by another current applicable hold.**
29. **A later hold does not by default reconstruct information validly and irreversibly deleted before the hold became effective.**
30. **Immutability while retained is not authority for indefinite participant-identifiable retention.**
31. **Practitioner involvement does not itself transfer ownership of Health, Safety or Plan truth into Professional Care.**
32. **A Generation Input Basis or provenance record may not become a shadow participant-data store that defeats the governing owner's deletion treatment.**
33. **Formal professional retention may preserve only approved professional-record purpose and cannot restore deleted Account, Entitlement, Health-profile, Plan or product authority.**
34. **Do not duplicate owner-Domain records into Professional Care merely to evade deletion treatment.**
35. **A stale in-flight professional workflow after irreversible deletion cannot create new participant-facing Plan/product fulfilment; any surviving recordkeeping consequence needs independent professional authority.**
36. **Retained Commerce/provider evidence may prove historical commercial truth but cannot recreate current Account, membership, Entitlement or product authority.**
37. **Any historical Entitlement evidence that survives retention must be incapable of satisfying a current access check or reconstructing a grant.**
38. **Audit & Evidence may prove governed actions but must not become a shadow copy of source-domain business truth.**
39. **Provider customer/subscription/transaction identifiers are evidence identifiers, not identity-recovery or entitlement-authority keys.**
40. **A later new Account for the same human does not inherit deleted commercial/product authority merely because retained evidence can be linked to the person.**
41. **Pseudonymisation, access restriction, encryption/tokenisation and irreversible anonymisation are distinct privacy dispositions.**
42. **A retained practical re-identification path prevents a representation from satisfying an irreversible-anonymisation contract.**
43. **A legitimately pseudonymous dataset must remain truthfully governed as pseudonymous and cannot be silently relabelled anonymous.**
44. **Anonymisation proof follows applicable authoritative, derived, cached, exported and external-processor representations, not only the source row.**
45. **Analytics participant-level retention must not bypass the stronger existing irreversible-aggregation and small-group-suppression requirement.**
46. **Recoverable closure preserves one canonical Account identity; reopening resumes that same identity rather than creating a replacement Account.**
47. **Completed full deletion permanently severs recovery of the old Account and permanently retires its PMR.**
48. **Same email/phone after completed deletion is not automatic identity-continuity authority.**
49. **Any later admitted Account after completed deletion begins new current authority and inherits no deleted Account, Entitlement, membership, consent, Health, Plan or product authority automatically.**
50. **Stale recovery/login/verification/merge/registration work cannot cross the completed-deletion boundary and resurrect old Account authority.**
51. **Physical retention or historical linkage does not itself create participant-export eligibility.**
52. **Already-deleted or irreversibly anonymised records must not be reconstructed or re-linked merely to satisfy an export.**
53. **Export assembly must follow owner-Domain current eligibility and must not become a reconstruction path through retained cross-domain joins.**
54. **Request-time export eligibility is not permanent; current authority/scope is revalidated during generation and delivery.**
55. **Owner export processing must distinguish governed no-eligible-record outcomes from unresolved failure strongly enough to avoid false export completion.**
56. **Once full deletion has revoked normal access, NewYou must not intentionally originate a new recurring membership collection for a future service period dependent on that revoked access.**
57. **Already-in-flight recurring financial truth is reconciled by Commerce but cannot create or restore Entitlement/access authority after deletion has revoked normal access.**
58. **Verified full-deletion completion cannot coexist with participant-linked recurring provider authority still capable of automatically initiating future membership charges.**
59. **Pending refund/dispute/chargeback work may continue under approved restricted financial authority without rebuilding ordinary Account/product authority.**
60. **Deletion-cancellation commercial restoration/reactivation and late-charge remediation remain explicit Product/Commerce policy rather than provider-adapter invention.**
61. **Unresolved/rejected/conflicted duplicate-identity reconciliation does not broaden one Account's irreversible deletion scope into another Account.**
62. **An authoritatively applied identity reconciliation must preserve enough lineage that eligible source-lineage records cannot evade canonical participant deletion merely because provenance predates the surviving Account.**
63. **Stale reconciliation work cannot recreate ordinary-use participant linkage or active authority after deletion/suppression becomes effective.**
64. **Stale deletion scoped to a retired source Account cannot blindly over-delete surviving canonical Account data.**
65. **If applied identity reconciliation becomes actively contested before irreversible cross-lineage deletion completes, destructive propagation into the contested lineage fails closed pending authoritative Identity resolution.**
66. **Compensating reconciliation may correct provenance/topology but cannot resurrect validly deleted data, completed-deletion Account authority or a permanently retired PMR.**
67. **Participant-authored Community content, independently authored context, moderation evidence and Security/Fraud evidence are distinct deletion/retention categories.**
68. **Retained moderation/security evidence must remain minimised, restricted and non-reconstructive; it cannot itself authenticate or restore deleted Account/product authority.**
69. **A later new Account must not automatically inherit historical sanctions from weak identifier/contact matching.**
70. **Retained moderation/security evidence may inform a later current Community/Security decision only under governed identity/risk authority.**
71. **Any human-level sanction intended to survive Account deletion must be explicit Product/Trust & Safety policy rather than inferred from a generic Account ban field.**

---

# 27. Current JIT / Architectural Proof obligations

`PRIV-PT-001...004` and `PRIV-PT-006...012` passed semantically. `PRIV-PT-005` identified a working gap resolved locally through accepted `PRIV-WD-001` with `PRIV-UPD-001`; `PRIV-PT-013` identified a recurring-commercial policy gap resolved locally through accepted `PRIV-WD-002` with `PRIV-UPD-002`; `PRIV-PT-014` identified a duplicate-identity deletion-scope gap resolved locally through accepted `PRIV-WD-003` with `PRIV-UPD-003`; `PRIV-PT-015` identified a sanction-scope/re-registration gap resolved locally through accepted `PRIV-WD-004` with `PRIV-UPD-004`. Executable proof remains absent.

Cross-cutting later proof must include:

- deletion/write races;
- stale workers;
- duplicate/reordered async work;
- current-authority revalidation;
- idempotent consequence handling;
- reconciliation after a true race or partial failure;
- old-backup restore;
- post-restore-point privacy suppression survival;
- replay after restore;
- recovery-gated promotion;
- safe derived-model rebuilding;
- cache invalidation;
- long-lived session/access revalidation;
- purpose-specific withdrawal fan-out;
- processor/provider late evidence;
- fail-closed behaviour when current authority cannot be established;
- export/deletion cancellation-window race;
- irreversible deletion cancelling undelivered export;
- deletion completion requiring removal of live NewYou-controlled export access paths;
- delivery-time export authority/scope revalidation;
- export temporal-boundary truthfulness under concurrent Domain mutation;
- processor timeout/unavailability during deletion;
- retry exhaustion without false completion;
- duplicate/reordered provider deletion evidence;
- processor-specific completion/retention evidence interpretation;
- aggregate deletion completion blocked by any unresolved required processor path.
- legal-hold/delete race with current-authority revalidation;
- proof that unrelated eligible deletion continues while held scope remains restricted;
- duplicate/reordered hold and release consequences;
- multiple overlapping holds;
- hold release automatically/resumably continuing deferred deletion;
- restore/replay preserving current hold plus deletion semantics.
- self-guided Health delete/anonymise versus formal professional restricted-retention paths;
- explicit category mapping for Plan Versions, Generation Input Bases, Plan Result Provenance, Safety cases/adjudications and practitioner-derived variants under `HSP-UPD-004`;
- retained professional record cannot reactivate or reconstruct Account, Entitlement, Health-profile or Plan authority;
- professional-review/delete race prevents stale participant-facing fulfilment;
- retained professional linkage remains minimum-necessary and non-reconstructive;
- later re-registration does not automatically reconnect deleted product authority.
- retained Commerce/payment evidence cannot satisfy current access checks;
- delayed provider success/renewal evidence after deletion cannot reissue Entitlements or membership access;
- post-deletion refund/dispute/chargeback processing operates without Account/product reconstruction;
- retained historical Entitlement evidence, if approved, is non-authorising;
- Audit evidence remains minimised and cannot reconstruct source-domain payload/state;
- Finance/support tooling cannot restore deleted product authority from retained evidence.
- pseudonym-to-person mapping retained after direct-identifier removal fails anonymisation proof;
- reversible encryption/tokenisation with usable key fails anonymisation proof;
- deterministic identifiers and quasi-identifiers are pressure-tested for practical re-identification;
- external processor mappings are included in anonymisation completion;
- source/derived/search/export representations cannot retain hidden stable linkage;
- Analytics aggregation/suppression proves no participant-level re-identification path survives under the aggregate contract.
- closure recovery resumes the same Account/PMR rather than creating a parallel identity;
- same-contact registration during recoverable closure cannot create a duplicate canonical Account;
- old recovery/login/verification work cannot reopen an Account after completed deletion;
- post-deletion admitted registration receives new Account identity and new PMR;
- retained evidence matching a new Account cannot restore deleted product authority;
- duplicate-identity reconciliation cannot reconstruct a completed-deletion Account.
- mixed active/historical/restricted/retained/deleted categories follow owner-specific export eligibility;
- deleted/anonymised records are not reconstructed or re-linked for export;
- legal-hold/professional/financial/security categories follow explicit access contracts rather than storage presence;
- zero eligible records is distinguished from owner export failure;
- mixed retained records cannot reconstruct deleted Account/Entitlement/product relationships;
- current authority changes during generation/delivery are respected.
- deletion-driven future-renewal suppression occurs through Commerce ownership;
- already-in-flight recurring collection reconciles truthfully without Entitlement restoration;
- late provider success after deletion access revocation triggers governed remediation rather than access;
- completed deletion cannot leave a future-charge-capable provider recurring contract;
- pending refund/dispute/chargeback survives only under restricted commercial authority;
- deletion cancellation exercises the eventually governed restoration/paid-period contract repeat-safely.
- unresolved duplicate candidate does not broaden deletion into another Account;
- applied reconciliation lineage cannot hide eligible source-origin records from canonical deletion;
- stale reconciliation work cannot recreate active linkage after suppression;
- stale source deletion cannot over-delete canonical-survivor data;
- contested applied reconciliation fails closed before irreversible cross-lineage destruction;
- compensating reconciliation cannot resurrect deleted records or retired PMR.
- Community content-sensitive delete/anonymise preserves eligible independently authored context without deleted Account attribution;
- moderation/security retained evidence remains restricted/minimised and cannot recreate Account/PMR/product authority;
- later Account weak-match does not automatically inherit historical sanction;
- governed strong-evidence anti-abuse path creates a current consequence rather than resurrecting deleted Account state;
- sanction scope (content/Account/human-level) follows explicit upstream policy;
- external Facebook/community-provider behaviour remains separately validated under `OQ-023`.

This proof belongs to later applicable JIT/Architectural Proof/Horizontal Hardening/Recovery exercises. It is not implementation authorisation here.

---

# 28. Current implementation / operational evidence posture

At the compression-audit baseline, the canonical NewYou repository root was reverified and contains `.github`, `.gitignore`, `docs`, `tests` and `tools`, with no root `mix.exs`. The repository therefore remains governance/planning/test/tooling material rather than a visible executable Elixir application at this SHA.

Therefore:

> `PRIV-PT-001...015` are semantic/governance pressure-test results. Executable privacy implementation and recovery evidence remain `NOT ASSESSED`.

This statement must be re-verified from live GitHub before any future implementation-complete, release-ready, certification or proof claim.

---

# 29. Planned pressure-test boundary reached

The planned Privacy Pre-JIT pressure-test grill is complete through `PRIV-PT-015`.

No `PRIV-PT-016` is created merely to keep numbering moving.

The next legitimate activity, if this stream continues, is a **stabilisation / compression / completeness audit** that should:

- verify every accepted `PRIV-PT-001...015` is represented once and only once;
- verify `PRIV-WD-001...004` and `PRIV-UPD-001...004` provenance and acceptance state;
- verify cross-stream HSP/CER dependencies remain accurate and non-duplicative;
- verify current authority references/gates have not drifted;
- distinguish current locked authority, accepted working doctrine, open upstream deltas, expert gates and JIT proof obligations;
- identify any contradiction or omitted high-risk seam before compression;
- only then produce a smaller implementation-facing Pre-JIT contract/index if warranted;
- preserve this cumulative working artifact and all prior SemVer versions as historical evidence.

A compression artifact must not silently upgrade working doctrine into Product/Architecture/Domain authority.

---

# 30. Change log

## v0.12.1 — 2026-09-09

Non-semantic compression-audit hygiene/evidence patch.

Changed:

- corrected the stale top-level document date from `2026-09-08` to `2026-09-09`;
- reverified live `main` at `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`;
- added the locked `DEC-245` verified-email gate to the current Privacy authority summary because it directly gates export/deletion capabilities;
- added `OQ-004` to the consolidated existing-gate list because accepted `PRIV-WD-002` / `PRIV-UPD-002` materially depend on recurring/refund/chargeback provider validation;
- sharpened the PT-013 CER dependency to accepted `CER-PT-004` for recurring logical-collection/idempotency semantics;
- narrowed `PRIV-UPD-003` classification to **Identity/Privacy JIT-governance first**, with Product escalation only if the resolution changes participant rights or Product identity/deletion promises; the accepted historical `PRIV-PT-014` record remains unchanged as provenance;
- reverified the repository-root implementation posture and confirmed no root `mix.exs` at the audited SHA.

No accepted `PRIV-PT`, `PRIV-WD` or substantive invariant was removed or semantically weakened.
No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.12.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-015 — Community/moderation/security evidence after deletion`;
- semantic verdict `CHANGES REQUIRED`;
- promoted proposed `PRIV-WH-004` to accepted `PRIV-WD-004 — Moderation/security evidence after deletion and later re-registration`;
- recorded `PRIV-UPD-004 — Sanction scope across full deletion and later Account creation`;
- confirmed participant-authored Community content, independently authored context, moderation evidence and Security/Fraud evidence remain distinct governed categories;
- confirmed restricted moderation/security evidence may survive deletion only as minimised non-reconstructive evidence;
- confirmed a later Account may not automatically inherit historical sanction state from weak identifier/contact matching;
- confirmed retained evidence may inform a governed current Community/Security decision without reconstructing deleted Account authority;
- preserved explicit Product/Trust & Safety policy work for content-scoped, Account-scoped and any human-level sanctions;
- marked the planned Privacy Pre-JIT pressure-test grill complete through `PRIV-PT-015`;
- deliberately did not invent `PRIV-PT-016`;
- routed the next legitimate activity to stabilisation/compression/completeness audit.

Preserved:

- all accepted `PRIV-PT-001...014` history;
- accepted `PRIV-WD-001...003`;
- `PRIV-UPD-001...003`;
- HSP/CER cross-stream registers;
- v0.9.0 discovery-map correction;
- methodology, SemVer, authority, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.11.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-014 — Identity merge/unmerge where one side enters deletion`;
- semantic verdict `CHANGES REQUIRED`;
- promoted proposed `PRIV-WH-003` to accepted `PRIV-WD-003 — Full deletion across duplicate-identity reconciliation lineage`;
- recorded `PRIV-UPD-003 — Full-deletion scope across duplicate-account reconciliation`;
- confirmed unresolved/rejected/conflicted duplicate reconciliation cannot broaden irreversible deletion into another Account;
- confirmed applied authoritative reconciliation must preserve enough lineage that eligible source-origin records cannot escape canonical participant deletion;
- confirmed stale merge work cannot recreate ordinary-use linkage after deletion suppression;
- confirmed stale source deletion cannot blindly over-delete the surviving canonical identity;
- confirmed contested applied reconciliation fails closed before irreversible cross-lineage deletion;
- confirmed compensating reconciliation cannot resurrect validly deleted data, completed-deletion authority or a retired PMR;
- advanced next test to `PRIV-PT-015 — Community/moderation/security evidence after deletion`.

Preserved:

- all accepted `PRIV-PT-001...013` history;
- accepted `PRIV-WD-001` and `PRIV-WD-002`;
- `PRIV-UPD-001` and `PRIV-UPD-002`;
- HSP/CER cross-stream registers;
- v0.9.0 discovery-map correction;
- methodology, SemVer, authority, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.10.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-013 — Deletion with refund/dispute/chargeback or active recurring membership`;
- semantic verdict `CHANGES REQUIRED`;
- promoted proposed `PRIV-WH-002` to accepted `PRIV-WD-002 — Full deletion versus active recurring commercial collection`;
- recorded `PRIV-UPD-002 — Full deletion request versus recurring membership commercial contract`;
- confirmed deletion-driven future-renewal suppression must occur through Commerce ownership rather than Privacy taking over provider/commercial state;
- confirmed already-in-flight financial truth must reconcile without restoring Entitlement/access;
- confirmed verified deletion completion cannot coexist with recurring provider authority still capable of initiating future participant-linked membership charges;
- confirmed pending refund/dispute/chargeback work may continue under restricted financial authority without rebuilding Account/product authority;
- preserved deletion-cancellation commercial restoration/reactivation and late-charge remediation as explicit upstream Product/Commerce + CER/provider-validation work;
- advanced next test to `PRIV-PT-014 — Identity merge/unmerge where one side enters deletion`.

Preserved:

- all accepted `PRIV-PT-001...012` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- HSP/CER cross-stream registers;
- v0.9.0 discovery-map correction and `PRIV-PT-015` prospective Community/moderation/security slot;
- methodology, SemVer, authority, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.9.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-012 — Export of mixed active / retained / deleted categories`;
- semantic verdict `PASS`;
- confirmed `stored ≠ export eligible`;
- confirmed deleted/irreversibly anonymised records are not reconstructed or re-linked merely for export;
- confirmed export assembly follows current owner-Domain eligibility and may not reconstruct deleted relationships through historical joins;
- confirmed export authority/scope remains revalidated during generation and delivery;
- confirmed owner export contracts must distinguish governed no-eligible-record outcomes from unresolved failures;
- corrected the **current** discovery map so accepted `PRIV-PT-012` matches its actual accepted mixed-category-export meaning;
- preserved historical prior-version map text and prospectively moved the displaced Community/moderation/security scenario to unused `PRIV-PT-015`, avoiding accepted-ID reuse;
- advanced next test to `PRIV-PT-013 — Deletion with refund/dispute/chargeback or active recurring membership`.

Preserved:

- all accepted `PRIV-PT-001...011` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- HSP/CER cross-stream registers;
- methodology, SemVer, authority, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.8.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-011 — Closure → reopen → deletion → new Account using same email/phone`;
- semantic verdict `PASS`;
- confirmed closure recovery resumes the same canonical Account identity and PMR;
- confirmed completed full deletion permanently severs Account recovery and permanently retires the old PMR;
- confirmed same email/phone after deletion does not itself create identity continuity;
- confirmed any later admitted Account starts new current authority and inherits no deleted product/business authority automatically;
- confirmed stale recovery/login/verification/merge/registration work cannot cross completed deletion and resurrect old Account authority;
- deliberately did not freeze immediate/permanent same-contact reuse policy because that remains contact-admission/retention JIT detail;
- refreshed discovery-map status through `PRIV-PT-011`;
- advanced next test to `PRIV-PT-012 — Export of mixed active / retained / deleted categories`.

Preserved:

- all accepted `PRIV-PT-001...010` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- HSP/CER cross-stream registers;
- methodology, SemVer, authority, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.7.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-010 — Pseudonymised participant data remains re-identifiable`;
- semantic verdict `PASS`;
- confirmed pseudonymisation, restricted identifiable retention, encryption/tokenisation, irreversible anonymisation and irreversible aggregation are distinct dispositions;
- confirmed that retained practical re-identification paths prevent satisfaction of an irreversible-anonymisation contract;
- confirmed legitimate pseudonymous datasets must remain truthfully classified as pseudonymous;
- confirmed anonymisation proof spans applicable authoritative, derived, cached, exported and processor representations;
- confirmed Analytics remains subject to the stronger participant-level removal plus irreversible aggregation/suppression rule;
- refreshed the discovery map statuses through `PRIV-PT-010`;
- advanced next test to `PRIV-PT-011 — Closure → reopen → deletion → new Account using same email/phone`.

Preserved:

- all accepted `PRIV-PT-001...009` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- `HSP-UPD-004` and `CER-PT-001` cross-stream seams;
- methodology, SemVer, authority, cross-stream, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.6.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-009 — Retained Commerce/Audit evidence after deletion must not recreate Account, Entitlement, membership or product access`;
- semantic verdict `PASS`;
- confirmed that retained financial/dispute/provider evidence may prove historical commercial truth but cannot restore current Account, membership, Entitlement or product authority;
- confirmed that any historical Entitlement evidence retained for an approved purpose must be non-authorising;
- confirmed that Audit & Evidence must remain minimised and cannot become a shadow source-domain recovery store;
- confirmed provider customer/subscription/transaction references are evidence identifiers, not recovery/access authority;
- confirmed later re-registration does not inherit deleted product authority from retained evidence;
- recorded `CER-PT-001` as the narrow cross-stream ownership-separation dependency;
- advanced next test to `PRIV-PT-010 — Pseudonymised participant data remains re-identifiable`.

Preserved:

- all accepted `PRIV-PT-001...008` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- `HSP-UPD-004` cross-stream reuse;
- methodology, SemVer, authority, cross-stream, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.5.0 — 2026-09-09

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-008 — Full deletion across self-guided Health/Safety/Plans versus professional retained records`;
- semantic verdict `PASS`;
- confirmed that full deletion permanently ends participant product/access authority while exact data disposition remains category-specific;
- confirmed that immutability while retained is not authority for indefinite identifiable retention;
- confirmed that practitioner involvement does not automatically transfer Health/Safety/Plan ownership into Professional Care;
- confirmed that Generation Input Bases and provenance must not become shadow stores that defeat owner-Domain deletion treatment;
- confirmed that genuine formal professional records may remain only under separately approved professional retention and remain restricted/non-reconstructive;
- explicitly reused `HSP-UPD-004` as the existing cross-stream category-disposition seam and created no duplicate `PRIV-UPD`;
- refreshed the CER cross-stream register to record the now-present `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.1.0.md` artifact while preserving historical prior-version provenance;
- advanced next test to `PRIV-PT-009 — Retained Commerce/Audit evidence after deletion must not recreate Account, Entitlement, membership or product access`.

Preserved:

- all accepted `PRIV-PT-001...007` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- methodology, SemVer, authority, cross-stream, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.4.0 — 2026-09-08

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-007 — Legal hold applied during deletion; narrow scope; release resumes deferred deletion`;
- semantic verdict `PASS`;
- confirmed that a legal hold pauses only deletion within its verified governed scope and does not freeze unrelated eligible deletion;
- confirmed that held records remain restricted and cannot restore Account, Entitlement, product, session or ordinary-use authority;
- confirmed that a hold becoming effective before destructive commit overrides stale prior deletion permission;
- confirmed that hold release resumes the already-deferred deletion obligation without a new participant deletion request;
- confirmed duplicate/reordered/overlapping hold and release work must converge on current hold authority;
- preserved actual legal authority, scope criteria, review cadence and jurisdiction-specific preservation duties as legal/privacy expert and operating-policy gates;
- advanced next test to `PRIV-PT-008 — Full deletion across self-guided Health/Safety/Plans versus professional retained records`.

Preserved:

- all accepted `PRIV-PT-001...006` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- methodology, SemVer, cross-stream, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.3.0 — 2026-09-08

Backward-compatible substantive discovery release.

Added/changed:

- accepted `PRIV-PT-006 — External processor unavailable or delayed during deletion`;
- semantic verdict `PASS`;
- confirmed that unresolved required processor paths block verified deletion completion;
- confirmed transport acknowledgement, retry exhaustion and provider silence do not manufacture deletion completion;
- confirmed approved retained-obligation processor outcomes may satisfy the processor contract only under independently governed retention authority;
- added processor timeout/retry/evidence/reconciliation proof obligations;
- preserved `OQ-029`, `OQ-030` and `OQ-032` as the exact retention, processor-inventory and operating/evidence gates;
- advanced next test to `PRIV-PT-007 — Legal hold applied during deletion; narrow scope; release resumes deferred deletion`.

Preserved:

- all accepted `PRIV-PT-001...005` history;
- accepted `PRIV-WD-001`;
- `PRIV-UPD-001`;
- methodology, SemVer, cross-stream, invariant and proof registers.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.2.0 — 2026-09-08

Backward-compatible substantive discovery release.

Added/changed:

- live baseline advanced to `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`;
- accepted `PRIV-PT-005 — Participant export races full deletion and concurrent mutation`;
- semantic verdict `CHANGES REQUIRED` for the under-specified export/deletion interaction;
- promoted proposed `PRIV-WH-001` to accepted non-authoritative `PRIV-WD-001`;
- added `PRIV-UPD-001 — Pending participant export versus subsequent full deletion`;
- added the invariant that completed deletion cannot coexist with a live NewYou-controlled export-delivery path;
- separated export authority/scope revalidation from export temporal-boundary/freshness semantics;
- added export/deletion and temporal-boundary JIT/Architectural Proof obligations;
- advanced next test to `PRIV-PT-006 — External processor unavailable or delayed during deletion`.

Preserved:

- all accepted `PRIV-PT-001...004` history;
- methodology corrections and strict verdict taxonomy;
- existing HSP/CER cross-stream seams;
- all prior consolidated invariants and proof obligations.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.

## v0.1.0 — 2026-09-08

Initial cumulative Privacy Pre-JIT working artifact.

Included:

- document maintenance and non-deletion rule;
- SemVer policy;
- live canonical authority baseline at `e95712ab000977b8b8dab5dac62761c2d912b866`;
- ownership and authority boundary;
- methodology corrections accepted after `PRIV-PT-001`;
- accepted `PRIV-PT-001` with corrected semantic verdict `PASS`;
- accepted `PRIV-PT-002`;
- accepted `PRIV-PT-003`;
- accepted `PRIV-PT-004`;
- current working-doctrine register (`NONE`);
- current upstream-delta register (`NONE`);
- HSP/CER cross-stream register;
- consolidated invariant register;
- consolidated JIT/Architectural Proof obligations;
- next test set to `PRIV-PT-005`.

No Product, Architecture, Domain, Roadmap, Open Work, Feature Pack, JIT or implementation authority changed.
