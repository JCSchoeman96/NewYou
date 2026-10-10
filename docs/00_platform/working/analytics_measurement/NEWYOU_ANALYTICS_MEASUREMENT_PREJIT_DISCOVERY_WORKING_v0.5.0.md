# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.5.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 5 ONLY — ANL-UPD-001 AUTHORITY-PROMOTION HARDENING
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked for this pass:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Main drift since Pass 4:** NONE.
- **Pre-pass branch head:** `ccdf7dad19e9fc6185cba740ef99455ea33bd5ee`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.4.0.md` — preserved unchanged.
- **Accepted predecessor result:** Pass 4 / `ANL-PT-007`–`ANL-PT-012` accepted by human review.
- **Purpose:** harden the accepted `ANL-UPD-001` Roadmap amendment intent into a promotion-ready patch contract and identify the minimum governance collateral required for a later authority successor.
- **Scope:** authority-promotion semantics and anti-drift controls only. This pass does not modify current Roadmap authority, README routing, manifest routing, Open Work authority, Delivery Atlas, Product Law, Domain Law, Architecture or implementation.

---

## 1. Pass discipline

Pass 4 established that the semantic correction belongs at Roadmap level and that a bounded FP-006 Research & Feedback activation can resolve `ANL-GAP-001` without widening MVP into general Research capability.

Pass 5 asks only:

1. what must be preserved when a Roadmap v1.3.0 authority successor is eventually created;
2. what routing/status collateral is mandatory versus derived follow-up;
3. whether the promotion could accidentally alter the active FP-001 programme;
4. whether any remaining Roadmap sentence would contradict the bounded activation;
5. what exact stop conditions remain before authority promotion.

---

## 2. Pass-4 acceptance lock

Human acceptance of Pass 4 promotes these working conclusions to `WORKING_LOCKED` within this Pre-JIT stream:

- `ANL-PT-007`: semantic authority target is Roadmap; no Product/Domain/Architecture semantic amendment is justified.
- `ANL-PT-008`: a one-line domain addition is insufficient; internal Roadmap summaries must remain coherent.
- `ANL-PT-009`: bounded FP-006 activation must not generalise Research into an MVP platform capability.
- `ANL-PT-010`: no Research Feature Pack is justified.
- `ANL-PT-011`: no new OQ, forced full dossier, proof classification or implementation detail is invented by this Pre-JIT amendment.
- `ANL-PT-012`: semantic target is Roadmap only; normal authority-routing/status collateral remains required at promotion time.

These conclusions may be reopened only by changed authority, new contradictory evidence or an explicit human decision.

---

## 3. Pass-5 pressure-test register

### ANL-PT-013 — SemVer and predecessor preservation

**Question:** If `ANL-UPD-001` is promoted, what Roadmap lifecycle shape preserves governance history?

**Analysis:** The change is semantic sequencing, not a routing-only patch. Current Roadmap is `05_ROADMAP_v1.2.0.md`. The correct candidate shape is therefore a minor successor `05_ROADMAP_v1.3.0.md`, with the exact v1.2.0 bytes preserved under `archive/05_ROADMAP_v1.2.0.md`. Historical v1.1.x amendment wording remains historical provenance and must not be silently rewritten to make it read as though the bounded FP-006 activation existed earlier.

**Disposition:** `PASS`.

**Working conclusion:** expected semantic successor `v1.2.0 → v1.3.0`; preserve v1.2.0 byte-identically in archive.

---

### ANL-PT-014 — README and authority-manifest routing

**Question:** Can Roadmap v1.3.0 become current authority without changing README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json`?

**Analysis:** No. README and the manifest are the current routing pointers. Promotion must change the default-authority route from `05_ROADMAP_v1.2.0.md` to `05_ROADMAP_v1.3.0.md`. The manifest Roadmap record must set canonical filename/path/SemVer to v1.3.0, set `superseded_version` to `1.2.0`, and pin the SHA-256/provenance SHA-256 of the exact promoted bytes. The manifest hash cannot be guessed before exact candidate bytes are frozen.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Working conclusion:** README + manifest are mandatory promotion collateral, not optional documentation cleanup.

---

### ANL-PT-015 — Open Work status successor

**Question:** Must authority promotion advance the active programme or change FP-001 status?

**Analysis:** No. Current Open Work says the active programme remains FP-001/HARDEN-02 related and that Analytics is not required for that active FP-001 conditional-dossier programme. A Roadmap amendment for the future FP-006 survey seam must not silently alter that current programme state. A later Open Work successor should record only the new current Roadmap version and the resolution of the Roadmap-level `ANL-UPD-001` contradiction, while preserving all unrelated active-stage and STOP statuses unless independent evidence changes them.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Working conclusion:** promotion requires planning-status reconciliation, but **does not advance Phase 7C, FP-001, proof classification or implementation** and does not make Analytics or Research & Feedback required for the current FP-001 work.

---

### ANL-PT-016 — Delivery Atlas treatment

**Question:** Is the derived Delivery Atlas part of the authority promotion itself?

**Analysis:** No. The Atlas is explicitly derived/non-authoritative and currently routes to Roadmap v1.2.0. It should be reconciled after a successful authority promotion so navigation points to v1.3.0 and reflects bounded Domain-19 participation in FP-006, but stale Atlas navigation cannot be allowed to block or override the promoted Roadmap. The Atlas follow-up must not create new law, gates, dossier requirements or Feature Packs.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Working conclusion:** Atlas reconciliation is **derived follow-up**, not semantic authority promotion. It should occur promptly after promotion but cannot be used to redefine `ANL-UPD-001`.

---

### ANL-PT-017 — §3A no-present-blocker sentence

**Question:** Does the current §3A closing statement remain coherent after the bounded FP-006 activation?

**Current meaning under v1.2.0:** future-gated capability rows do not create present OQ blockers for FP-001–FP-017; sensitive Research gates are scheduled only when an activating Feature Pack is assigned.

**Analysis:** The sentence needs refinement once FP-006 becomes the activating pack for one bounded Research mode. The amendment must not invent an OQ, but it also cannot imply that the activated mode has no downstream JIT/gate obligations. The correct meaning is: the bounded activation creates no automatic new OQ by Roadmap fiat; normal FP-006 Phase 7 must adjudicate the minimum applicable Research/Privacy/JIT/proof obligations before implementation.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Working conclusion:** include this clarification inside the §3A amendment block. This refines Pass 4's edit surface without widening the semantic scope.

---

### ANL-PT-018 — Promotion hash/freeze discipline

**Question:** Can manifest pins or certification claims be prepared from the prose patch alone?

**Analysis:** No. The exact Roadmap v1.3.0 candidate bytes must first be assembled from the live v1.2.0 predecessor plus only the accepted patch. Only then may SHA-256, archive equality, manifest routing and exact-head review be claimed. A prose patch is sufficient to lock intent, but not sufficient to claim authority or byte-level certification.

**Disposition:** `PASS`.

**Working conclusion:** no guessed hash, no premature `CURRENT`, and no certification claim before exact candidate bytes exist and are independently reviewed.

---

## 4. Refined minimum promotion package

### 4.1 Semantic authority payload

One Roadmap successor only:

- `05_ROADMAP_v1.3.0.md` — semantic authority candidate.
- `archive/05_ROADMAP_v1.2.0.md` — exact preserved predecessor.

The v1.3.0 semantic changes remain bounded to:

1. version/header + v1.3.0 amendment-scope statement;
2. §2 Research & Feedback mature-capability summary;
3. §3.3 Domain/Feature-Pack challenge summary;
4. §3A activation rule, Research & Feedback row and no-automatic-OQ/JIT clarification;
5. FP-006 Affected Domains;
6. FP-006 bounded Research & Feedback activation paragraph;
7. FP-006 `Deferred From This FP` scope fence.

The §3A refinement is one semantic section even though it changes more than one sentence.

### 4.2 Mandatory promotion collateral

At the same governed promotion boundary:

- README current-authority route → Roadmap v1.3.0;
- authority-manifest Roadmap record → v1.3.0 exact path/SemVer/hash with `superseded_version: 1.2.0`;
- Open Work successor → record current Roadmap v1.3.0 and the resolved sequencing contradiction without advancing unrelated programme state;
- preserve direct predecessors according to existing governance conventions.

### 4.3 Derived follow-up

After successful authority promotion:

- reconcile Delivery Atlas current-source routing and FP-006 derived Domain participation;
- keep Atlas explicitly non-authoritative;
- do not let Atlas reconciliation reopen or broaden the accepted Roadmap semantics.

---

## 5. Promotion non-goals

The promotion package must not:

- amend Product Law, Decision Register, Domain Law or Architecture;
- create a Research Feature Pack;
- add Research & Feedback to FP-005;
- change FP-001 current dossier requirements or Analytics-not-required status for FP-001;
- activate Voting & Balloting;
- activate FP-016 experimentation;
- create a new OQ solely because the Domain participates;
- choose anonymous/account-linked identity mode, retention period, deletion mechanics, provider, Resource, schema or event name;
- classify proof before the normal FP-006 Phase 7 contract;
- authorise implementation.

---

## 6. ANL-UPD-001 state after Pass 5

```text
SEMANTIC INTENT: WORKING_LOCKED
PROMOTION PATCH CONTRACT: DRAFTED / PRESSURE-TESTED
EXACT ROADMAP v1.3.0 BYTES: NOT YET FROZEN
CURRENT AUTHORITY: STILL 05_ROADMAP_v1.2.0.md
ANL-GAP-001: UPSTREAM_ACTION_REQUIRED
FP-006 SURVEY JIT/IMPLEMENTATION: BLOCKED AT ROADMAP AUTHORITY
```

No authority file was modified by this pass.

---

## 7. Pass 5 disposition

**PASS — PROMOTION CONTRACT HARDENED; EXACT AUTHORITY SUCCESSOR STILL REQUIRES A SEPARATE FREEZE/PROMOTION PASS.**

The accepted Roadmap repair remains the smallest coherent upstream change. Pass 5 adds the required lifecycle/routing discipline and closes the risk that the amendment could accidentally change current FP-001 work, create a new OQ, or treat the Delivery Atlas as authority.

**Recommended next focused pass after human acceptance:** assemble and independently review the exact `05_ROADMAP_v1.3.0.md` authority-successor bytes plus routing/status successors, but do not merge to `main` until that exact candidate passes review.