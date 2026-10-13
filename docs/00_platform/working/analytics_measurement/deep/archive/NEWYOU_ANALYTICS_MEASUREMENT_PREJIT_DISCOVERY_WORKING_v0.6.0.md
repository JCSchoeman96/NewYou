# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.6.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 6 ONLY — EXACT ROADMAP FREEZE PRE-AUDIT / PATCH-CONTRACT CORRECTION
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked for this pass:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Pre-pass branch head:** `eb1e264665fb42ea557c288ce8b1f2150fde447d`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.5.0.md` — preserved unchanged.
- **Accepted predecessor result:** Pass 5 / `ANL-PT-013`–`ANL-PT-018` accepted by human review.
- **Purpose:** perform the exact-source pre-freeze audit required before assembling `05_ROADMAP_v1.3.0.md`, and stop if the accepted promotion patch contract would produce an internally contradictory Roadmap successor.
- **Scope:** exact predecessor/source audit and bounded anti-contradiction refinement only. No Roadmap authority successor, README route, manifest route, Open Work successor, Delivery Atlas reconciliation, Feature Pack/JIT work, metric contract, provider choice or implementation is created in this pass.

---

## 1. Pass discipline and execution ruling

Pass 5 authorised the next focused step to assemble exact Roadmap v1.3.0 candidate bytes from the current v1.2.0 predecessor plus only the accepted `ANL-UPD-001` patch contract.

During exact full-text inspection of the current Roadmap predecessor, two inherited statements outside the Pass-5 patch surface were found that would become false if the accepted bounded FP-006 Research & Feedback activation were applied without refinement:

1. FP-005 says Research & Feedback remains wholly `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` until a later Roadmap decision.
2. FP-017 says Research & Feedback and Voting & Balloting both remain Feature-Pack-unassigned until a later product-space/market activation decision.

The bounded FP-006 activation would make both whole-Domain statements inaccurate even though their intended local guardrails remain valid.

**Ruling:** do not freeze or route Roadmap v1.3.0 from an incomplete patch contract. Record the two smallest anti-contradiction refinements, preserve all accepted ownership/scope fences, and stop for human review before exact authority bytes are assembled.

This is a correction to the **working promotion patch surface**, not a reopening of the accepted source-owner decision or a new Product/Domain/Architecture decision.

---

## 2. Exact predecessor lock

The exact current Roadmap predecessor on both live `main` and `prejit/analytics-measurement` is:

```text
path: docs/00_platform/05_ROADMAP_v1.2.0.md
git blob SHA: 5432991071d4d1a7cbd9dc4c8fca48c823129f40
current manifest SHA-256: 601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0
```

A historical blob from the PR that first introduced v1.2.0 is not sufficient as a freeze predecessor if later same-filename routing/governance corrections changed the bytes. The live current authority bytes must be the sole source for an exact v1.3.0 successor and archived v1.2.0 predecessor.

---

## 3. Pass-6 pressure-test register

### ANL-PT-019 — FP-005 whole-Domain future-gated wording after bounded FP-006 activation

**Question:** Can the current FP-005 feedback-classification guardrail remain byte-for-byte unchanged if Roadmap v1.3.0 explicitly activates Research & Feedback inside FP-006?

**Current relevant meaning:** FP-005 basic feedback is HJP truth, does not activate Domain 19, and the same paragraph then says Research & Feedback remains `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` until a later Roadmap decision.

**Analysis:** The first sentence remains correct and must be preserved. The second is stated at whole-Domain level and would become false after v1.3.0 itself becomes the later governed decision activating one bounded FP-006 mode. Leaving it unchanged would create an internal contradiction and could mislead later agents into treating the bounded FP-006 instrument as unauthorised despite the new §3A/FP-006 activation.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Required refinement:** FP-005 must continue to state that its basic daily/weekly progress/usefulness feedback remains HJP truth and does not activate/reclassify Research. It must additionally acknowledge that the **only MVP Research exception is the separately bounded FP-006 controlled-pilot instrument**; all broader Research remains future-gated / Feature-Pack-unassigned.

**Non-change:** no FP-005 Affected Domain changes, no Research truth moves into FP-005, and no survey-builder capability is admitted.

---

### ANL-PT-020 — FP-017 whole-Domain Feature-Pack-unassigned wording after bounded FP-006 activation

**Question:** Can FP-017 continue to say Research & Feedback and Voting & Balloting both remain Feature-Pack-unassigned after v1.3.0 assigns one bounded Research mode to FP-006?

**Analysis:** No. The local FP-017 guardrail remains correct — FP-017 must not automatically acquire Research or Voting merely because it is a future product/market pack. But the whole-Domain statement that Research remains Feature-Pack-unassigned becomes inaccurate once the bounded FP-006 mode is assigned. Voting remains fully Feature-Pack-unassigned; broader Research remains future-gated/unassigned outside the bounded FP-006 exception.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Required refinement:** state that FP-017 does not automatically own Research or Voting; the bounded FP-006 Research activation does not extend to FP-017; broader Research capability and all Voting/Balloting remain future-gated / Feature-Pack-unassigned unless a later governed Roadmap decision activates them for a concrete approved outcome.

**Non-change:** FP-017 gains no new Domain, dependency, capability or gate.

---

### ANL-PT-021 — Which v1.2.0 bytes are the lawful exact predecessor?

**Question:** May the v1.3.0 freeze be assembled from an older PR-introduction blob for the same `05_ROADMAP_v1.2.0.md` filename?

**Analysis:** No. The canonical source-of-truth rule requires the exact bytes currently routed on live `main`. Full current-path reads on `main` and the Analytics working branch resolve the current Roadmap to git blob `5432991071d4d1a7cbd9dc4c8fca48c823129f40`. Historical PR blobs remain provenance only and must not silently replace later current bytes.

**Disposition:** `PASS`.

**Working lock:** exact v1.3.0 assembly and archive preservation must start from the current live v1.2.0 bytes, not an earlier same-version historical blob. The manifest SHA-256 remains the integrity pin for those current authority bytes until promotion.

---

## 4. Refined exact semantic edit surface for ANL-UPD-001

Pass 5's accepted semantic intent is preserved. The exact Roadmap successor must now change these **nine logical locations together**:

1. successor header + new v1.3.0 amendment-scope section;
2. §2 Research & Feedback mature-capability row;
3. §3.3 `New Domains 19/20 require new Feature Packs` decision row;
4. §3A activation rule, Research & Feedback row and no-automatic-OQ/JIT closing clarification;
5. **FP-005 feedback-classification guardrail — local anti-contradiction refinement only**;
6. FP-006 Affected Domains — add Research & Feedback;
7. FP-006 bounded Research & Feedback activation paragraph;
8. FP-006 `Deferred From This FP` — preserve broader Research deferral;
9. **FP-017 future-gated capability boundary — local anti-contradiction refinement only**.

Historical v1.1.x/v1.2.0 amendment summaries/verdicts remain historical provenance and are not rewritten to pretend this bounded activation existed earlier.

---

## 5. Exact candidate wording additions

### 5.1 FP-005 guardrail replacement meaning

Use meaning equivalent to:

> **Feedback classification guardrail:** FP-005 “basic feedback” and daily/weekly progress entries are participant progress / self-tracking / usefulness evidence under `Habits, Journals & Progress` for the core plan loop. They do **not** activate Domain 19 Research & Feedback and are not reclassified by the bounded FP-006 Research activation. The only MVP Research & Feedback activation is the separately bounded FP-006 controlled-pilot value/relevance/price-value instrument; all broader Research capability remains `FUTURE-GATED / FEATURE-PACK-UNASSIGNED`. Plan/protocol calculations required by this outcome remain Plans & Nutrition authority (`calculation != authority` for Interactive Tools elsewhere).

### 5.2 FP-017 boundary replacement meaning

Use meaning equivalent to:

> **Future-gated capability boundary:** FP-017 does not automatically own Research & Feedback or Voting & Balloting. The bounded FP-006 Research & Feedback activation does not extend to FP-017. Broader Research capability and all Voting & Balloting remain Feature-Pack-unassigned unless a concrete approved product-space/market direction explicitly requires them and a later governed Roadmap decision assigns the required bounded mode.

These additions are consistency repairs only; they do not broaden `ANL-UPD-001`.

---

## 6. ANL-UPD-001 state after Pass 6

```text
SEMANTIC INTENT: WORKING_LOCKED
PASS-5 PROMOTION CONTRACT: SUPERSEDED IN PART BY PASS-6 CONSISTENCY REFINEMENT
REFINED PROMOTION CONTRACT: DRAFTED / PRESSURE-TESTED / PENDING HUMAN ACCEPTANCE
EXACT ROADMAP v1.3.0 BYTES: NOT FROZEN
CURRENT AUTHORITY: STILL 05_ROADMAP_v1.2.0.md
ANL-GAP-001: UPSTREAM_ACTION_REQUIRED
FP-006 SURVEY JIT/IMPLEMENTATION: BLOCKED AT ROADMAP AUTHORITY
```

No authority document was modified by this pass.

---

## 7. Pass 6 disposition

**CHANGES REQUIRED — EXACT FREEZE STOPPED BEFORE AUTHORITY MUTATION; PROMOTION PATCH CONTRACT NEEDS TWO NARROW CONSISTENCY REFINEMENTS.**

The accepted owner, activation boundary and governance route remain valid. The failure is narrower: exact full-text review proved that the Pass-5 edit surface omitted two inherited whole-Domain statements that would contradict the intended v1.3.0 state.

Freezing the candidate anyway would violate the project's anti-drift and authority-coherence rules. The smallest safe response is to accept the two refinements above and then perform exact v1.3.0 byte assembly in the next focused pass.

**Recommended next focused pass after human acceptance:** assemble exact `05_ROADMAP_v1.3.0.md` bytes from current live v1.2.0 blob `5432991071d4d1a7cbd9dc4c8fca48c823129f40` plus only the accepted nine-location patch; preserve exact v1.2.0 in archive; compute real SHA-256 pins; prepare matching README/manifest/Open Work candidate collateral; independently review the exact candidate; still do not open a PR or merge to `main` until that exact head passes.