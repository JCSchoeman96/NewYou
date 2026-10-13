# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.10.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.10.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch entering pass:** `b22edeb06ce409acbdf518e6686a772b8a058bf1`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_CONTROL_REGISTER_WORKING_v0.9.0.md`
- **Discovery source through:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.14.0.md`
- **Corrected OPS-UPD-004 candidate:** `NEWYOU_OPS_UPD_004_AUTHORITY_PROMOTION_CANDIDATE_WORKING_v0.2.0.md`
- **Formal build contract:** `NEWYOU_OPS_UPD_004_AUTHORITY_SUCCESSOR_BUILD_WORKING_v0.1.0.md`
- **Independent review:** `NEWYOU_OPS_UPD_004_AUTHORITY_SUCCESSOR_INDEPENDENT_REVIEW_WORKING_v0.1.0.md`
- **v0.10.0 bounded change:** formal `OPS-UPD-004` Product/Decision successor build contract + independent review only. No new pressure tests, no new UPD/GAP, no implementation, no current-authority routing change.
- **Compression rule:** all unchanged v0.9.0/v0.8.0 convergence state remains inherited. This successor records only the material authority-build/review delta.

---

# 1. Current identifier and authority state

```text
latest semantic discovery = v0.14.0
contiguous PT coverage = OPS-PT-001...210
new PTs in this pass = 0
current upstream deltas = OPS-UPD-001...007
current normalized gaps = OPS-GAP-001...025
new OPS-UPD = 0
new OPS-GAP = 0
current Product Law = 00_PLATFORM_v1.6.0.md
current Decision Register = 01_DECISIONS_v1.6.0.md
live OPS-UPD-004 = CONFLICT_STOP
live OPS-GAP-010 = OPEN / CONFLICT_STOP
```

Nothing in this working register overrides current authority.

---

# 2. Independent-review corrections to the v0.1.0 promotion candidate

The prior `NEWYOU_OPS_UPD_004_AUTHORITY_PROMOTION_CANDIDATE_WORKING_v0.1.0.md` is historical evidence but is **not suitable for direct promotion unchanged**.

The independent review found four corrections now locked in v0.2.0:

1. `DEC-034`, not `DEC-057`, is the annual retake rule; `DEC-057` is launch scoring.
2. Ownership must remain explicit: Temperament owns attempt/result/report truth; Entitlements owns current credit/right truth; Identity & Access governs access assurance.
3. Product §21B.3 must be corrected as well as adding §21R.6; otherwise Product v1.7.0 would retain an internal contradiction.
4. No Roadmap semantic successor is justified because current FP-003 already says the credit remains unused until successful digital assessment delivery. A later Roadmap routing/reference PATCH may be needed after Product/Decision promotion.

No new semantic class emerged, so no new PT/UPD/GAP is justified.

---

# 3. Corrected OPS-UPD-004 candidate semantics

Candidate lifecycle:

| Situation | Candidate consequence |
|---|---|
| valid ordinary paid credit; no first answer | `available_unused` |
| first answer saved; active/recoverable attempt | `held_unconsumed` |
| immutable result exists but paid report not durably participant-available | `held_unconsumed` |
| immutable result + paid report durably available to authorised participant | `consume_exactly_once` |
| attempt expires before first answer | `release_to_available_unused` |
| post-first-answer nontechnical expiry without live recovery | `close_unconsumed` |
| genuine technical failure | preserve same paid obligation / recover existing lineage where present |
| valid technical-failure refund | close affected right; not delivery/consumption |

Additional locks:

- notification/provider success/failure is not assessment-credit consumption authority;
- participant open/read/view telemetry is not consumption authority;
- assessment-completion metrics are not Entitlements authority;
- refundability remains governed separately by `DEC-045`;
- `DEC-034` retake interval remains separate and is not redefined by this repair;
- duplicate/retried submission, recovery, delivery or consumption converges on one logical credit/result/report lineage.

The material Product choice remains:

```text
post-first-answer nontechnical expiry
→ close_unconsumed
```

This establishes no legal sufficiency and must remain explicit in the formal authority review/promotion trail.

---

# 4. Formal deterministic successor build

The formal build contract pins exact live source blobs:

```text
00_PLATFORM_v1.6.0.md
blob = bb98081841b432a5a3d5e961929acf494ac9c8ba

01_DECISIONS_v1.6.0.md
blob = 85402cb169e095771f03482981d0691e08efb021
```

Target semantic successors:

```text
00_PLATFORM_v1.7.0.md
01_DECISIONS_v1.7.0.md
```

Both are MINOR successors because the repair adds/changes Product semantics.

## Product transformation only

- version/header/amendment-scope metadata;
- replace the two conflicting §21B.3 first-answer consumption bullets;
- add §21R.6 assessment-credit claim/delivery/closure/consumption rule;
- update §24 internal current-version sentence;
- no other Product semantic change.

## Decision transformation only

- version/header/amendment-scope metadata;
- preserve historical DEC-055 wording but mark `SUPERSEDED BY DEC-313`;
- append `DEC-313`;
- no other DEC/OQ semantic change.

## Explicit non-changes

- no North Star semantic successor;
- no Roadmap semantic successor;
- no Architecture amendment;
- no Domain Map amendment;
- no provider/channel choice;
- no operator permission rule;
- no implementation representation.

---

# 5. Independent review outcome

The corrected candidate and deterministic build contract were reviewed independently against `OPS-PT-163...174` and adjacent authority.

| Review area | Outcome |
|---|---|
| Product authority level | PASS |
| DEC-055 explicit supersession | PASS |
| Product §21B.3 internal conflict removal | PASS |
| §21R.6 lifecycle | PASS |
| Domain ownership | PASS |
| DEC-045 refund separation | PASS |
| DEC-054/056 recovery/expiry composition | PASS |
| DEC-061/066/067 immutable result/report lineage | PASS |
| DEC-303 purchase-cap composition | PASS |
| DEC-034 non-expansion | PASS WITH BOUNDED NON-EXPANSION |
| North Star metric vs commercial consumption | PASS WITH EXPLICIT SEPARATION |
| OPS-PT-163...174 | PASS, 12/12 |
| Roadmap semantic change | NOT JUSTIFIED |
| Architecture/Domain change | NOT JUSTIFIED |

The review certifies the **deterministic build contract**, not cumulative v1.7.0 bytes and not current authority.

---

# 6. Materialisation hard gate

Before `OPS-UPD-004` can close, a separate exact materialisation/promotion pass must:

1. generate cumulative `00_PLATFORM_v1.7.0.md` from the pinned Product blob;
2. generate cumulative `01_DECISIONS_v1.7.0.md` from the pinned Decisions blob;
3. prove the exact diffs match the build contract and nothing else;
4. archive predecessor authority byte-identically;
5. update/add Foundation Integrity assertions for DEC-055 supersession, DEC-313, §21B.3 and §21R.6;
6. prove a negative check prevents first-answer consumption from remaining current authority;
7. run exact-head CI;
8. independently review the materialised head;
9. only then update README/manifest/current routing and any required routing-only downstream PATCH successors;
10. reverify resulting-main after any eventual merge before claiming current-status closure.

Until that pass completes:

```text
OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
implementation = NOT AUTHORISED to choose a rule
```

---

# 7. Other upstream deltas remain unchanged

No other upstream delta is reopened or promoted in this pass:

- `OPS-UPD-001` pilot admission/cap — unchanged / open;
- `OPS-UPD-002` duplicate collection/make-whole — unchanged / open;
- `OPS-UPD-003` consequential command authority — unchanged / principally operations-policy;
- `OPS-UPD-005` pre-first-fulfilment Plan change — unchanged / open;
- `OPS-UPD-006` export + Full Deletion — unchanged / open, legal/privacy validation still required;
- `OPS-UPD-007` General Wellness clock start — unchanged / open.

Do not begin `OPS-UPD-001` until `OPS-UPD-004` materialisation/promotion has completed or the user explicitly changes the serial order.

---

# 8. v0.10.0 disposition

```text
SEMANTIC PRESSURE TESTS ADDED: NONE
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
DISCOVERY SUCCESSOR: NONE (v0.14.0 REMAINS LATEST)
OPS-UPD-004 V0.1.0 CANDIDATE: SUPERSEDED FOR PROMOTION PURPOSES
OPS-UPD-004 V0.2.0 CORRECTED CANDIDATE: PASS
FORMAL AUTHORITY-SUCCESSOR BUILD CONTRACT: PASS
INDEPENDENT REVIEW: PASS
12/12 OPS-PT-163...174: PASS UNDER CORRECTED CANDIDATE
TARGET PRODUCT SUCCESSOR: v1.7.0
TARGET DECISION SUCCESSOR: v1.7.0 / DEC-313
ROADMAP SEMANTIC SUCCESSOR: NOT JUSTIFIED
ARCHITECTURE AMENDMENT: NOT JUSTIFIED
DOMAIN MAP AMENDMENT: NOT JUSTIFIED
CURRENT AUTHORITY MODIFICATION: NONE
LIVE OPS-UPD-004 CONFLICT_STOP: REMAINS
MATERIALISED CUMULATIVE v1.7.0 BYTES: REQUIRED NEXT
IMPLEMENTATION: NOT AUTHORISED
PR: NONE
AUTHORITY BUILD/REVIEW PASS: PASS / CONVERGED
BROAD PRE-JIT FREEZE: NOT READY
NEXT PASS: OPS-UPD-004 EXACT CUMULATIVE v1.7.0 MATERIALISATION + DIFF/INTEGRITY REVIEW ONLY
```
