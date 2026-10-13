# NewYou Operations, Support & Pilot Evidence Pre-JIT — Working Control Register v0.9.0

> **WORKING / NON-AUTHORITATIVE**  
> **DERIVED CONTROL REGISTER — NOT A NEW AUTHORITY LAYER**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.9.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/operations-support-pilot`
- **Working branch predecessor head:** `129515d9641a6a78967a422c88fb86546707e194`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_CONTROL_REGISTER_WORKING_v0.8.0.md`
- **Discovery source through:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.14.0.md`
- **Convergence review source:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_UPSTREAM_PROMOTION_REVIEW_WORKING_v0.1.0.md`
- **OPS-UPD-004 promotion candidate:** `NEWYOU_OPS_UPD_004_AUTHORITY_PROMOTION_CANDIDATE_WORKING_v0.1.0.md`
- **v0.9.0 bounded change:** `OPS-UPD-004` authority-promotion candidate only. No new pressure tests, no new `OPS-UPD`, no new `OPS-GAP`, and no discovery `v0.15.0`.
- **Compression rule:** all unchanged v0.8.0 convergence classifications, normalized gap routing and working locks remain inherited. This successor records only the material `OPS-UPD-004` candidate delta plus enough current routing to prevent ambiguity.
- **Non-goals:** no current Product/Decision/Roadmap amendment, no Architecture/Domain change, no implementation design, no PR.

---

# 1. Register semantics and inheritance

`WORKING_LOCKED` remains a constraint **inside this Pre-JIT stream only**. It is not Product Law, a frozen DEC/ARC/ARQ, implementation authority or a JIT contract.

Read order:

```text
current NewYou authority
→ this v0.9.0 control register
→ v0.8.0 predecessor for unchanged convergence/gap/lock detail
→ exact discovery / PT / UPD / GAP evidence as needed
```

Conflict rule:

```text
current authority wins over this register;
exact deep evidence wins over an erroneous summary;
a working promotion candidate never becomes current authority by being listed here.
```

The v0.8.0 promotion sequence remains inherited. Only its first step is materially refined here.

---

# 2. Discovery and identifier state

Semantic discovery is unchanged:

```text
latest discovery = v0.14.0
contiguous PT coverage = OPS-PT-001...210
new PTs in this pass = 0
current upstream deltas = OPS-UPD-001...007
current normalized gaps = OPS-GAP-001...025
new OPS-UPD = 0
new OPS-GAP = 0
```

Do not create `OPS-UPD-008` merely to restate any part of the assessment-credit repair.

---

# 3. Current upstream-delta register

| ID | Current meaning | Current state | Route |
|---|---|---|---|
| `OPS-UPD-001` | pilot admission commitment / review boundaries / maximum / in-flight / historical cohort | `OPEN_UPSTREAM` | Product/release promotion |
| `OPS-UPD-002` | duplicate genuine collection / full-excess make-whole / no-manufactured partial attribution | `OPEN_UPSTREAM` | Product/commercial promotion; provider proof separate |
| `OPS-UPD-003` | minimum FP-006 consequential human command authority matrix | `OPEN_UPSTREAM`, principally operations-policy | bounded operations policy after relevant Product powers are governed |
| `OPS-UPD-004` | assessment-credit claim/hold vs consumption; `DEC-055` conflicts with successful-delivery rule | `PROMOTION_CANDIDATE_READY`; **live `CONFLICT_STOP` remains** | proposed `DEC-313` + Product §21R.6; formal authority successor required |
| `OPS-UPD-005` | material participant Plan change-of-intent before first fulfilment | `OPEN_UPSTREAM`, narrowed | Product / Commerce / Entitlements promotion |
| `OPS-UPD-006` | valid predating export across effective Full Deletion | `OPEN_UPSTREAM`, narrowed | Product/Privacy promotion after legal/privacy validation; `OQ-032` downstream |
| `OPS-UPD-007` | General Wellness single 14-day choice-window qualifying communication start | `OPEN_UPSTREAM`, narrowed | Product/customer-communication promotion; `OQ-017` / `OQ-036` downstream |

Only `OPS-UPD-004` changes working readiness in this successor.

---

# 4. Gap routing affected by this pass

The normalized `OPS-GAP-001...025` inventory remains inherited from v0.8.0 without reclassification, except for added candidate-readiness metadata on the existing conflict record:

| Gap | Current classification | Current route |
|---|---|---|
| `OPS-GAP-010` | `PRODUCT_AUTHORITY_GAP / CONFLICT_STOP`; promotion candidate ready | `OPS-UPD-004` → proposed `DEC-313` + Product §21R.6 → formal Product/Decision successor |

This does **not** close `OPS-GAP-010`. Closure requires the formal authority successor to become current.

---

# 5. New working locks from the OPS-UPD-004 promotion candidate

All v0.8.0 working locks remain inherited. Add these bounded candidate-level locks:

64. **First-answer save is claim/hold, not consumption, in the candidate.** It makes the existing credit unavailable for another ordinary sale/independent attempt while leaving it commercially unconsumed.
65. **Successful assessment delivery is a Product-availability boundary.** The candidate requires both the immutable governed digital result and the paid digital report permitted by Product Law to be durably available to the authorised participant through an approved participant-access path.
66. **Notification/open telemetry is non-controlling.** Provider acceptance, email delivery, result creation alone, report generation alone and open/read/view analytics do not independently establish assessment-credit consumption.
67. **Pre-first-answer expiry does not consume or close the credit.** The expired attempt ends and the credit remains/returns `available_unused`.
68. **Post-first-answer nontechnical expiry is proposed to close the credit unconsumed.** This is a new Product/customer-right choice introduced by the candidate, not a consequence already implied by `DEC-056`; it requires explicit formal approval and establishes no legal sufficiency.
69. **Genuine technical failure preserves one paid obligation.** Controlled recovery continues the same credit/result lineage, or the existing technical-failure refund path closes it; neither path may mint a duplicate credit/result/report/consumption.
70. **Qualifying delivery consumes exactly once.** Duplicate/retried submission, recovery, delivery or consumption signals converge on one logical credit/result lineage.

These are working candidate semantics only until promoted.

---

# 6. OPS-UPD-004 candidate adjudication

## 6.1 Exact live contradiction

Current authority still contains both:

```text
DEC-055:
first answer / attempt begins
→ consume / mark used
```

and:

```text
current Product Law + FP-003:
successful digital assessment delivery
→ consume
```

Therefore live current state remains:

```text
OPS-UPD-004 = CONFLICT_STOP
OPS-GAP-010 = OPEN / CONFLICT_STOP
```

JIT, operators and implementation may not choose between the texts.

## 6.2 Proposed minimal repair

The candidate allocates proposed:

```text
DEC-313 — Assessment-credit claim, closure and consumption
Product Law §21R.6 — Assessment-credit claim, delivery, closure and consumption
```

Candidate lifecycle:

| Situation | Candidate Product consequence |
|---|---|
| valid ordinary paid credit; no first answer | `available_unused` |
| first answer saved; active/recoverable attempt; no delivery | `held_unconsumed` |
| immutable result exists; paid report not yet participant-available | `held_unconsumed` |
| result + paid report durably participant-available through approved access path | `consume_exactly_once` |
| attempt expires before first answer | `release_to_available_unused` |
| attempt expires after first answer; no delivery; nontechnical; no live technical-recovery case | `close_unconsumed` |
| genuine technical failure | preserve same paid obligation for controlled recovery |
| valid technical-failure refund | close affected credit/right; do not call it delivery/consumption |

## 6.3 Highest-impact Product choice

The `post-first-answer nontechnical expiry → close_unconsumed` branch is **not derived from current `DEC-056`**. It is an explicit proposed Product choice needed to avoid leaving an expired post-answer credit indefinitely stranded while also preserving:

- successful-delivery-only consumption;
- `DEC-045` ordinary refund closure after the first answer; and
- the one-active-unused-credit purchase cap.

Material consequence:

> a participant who voluntarily abandons the assessment after answering and lets it expire receives neither successful assessment delivery nor an ordinary refund, and the credit ceases to be an active unused right.

The formal authority review must accept or reject that participant-right consequence explicitly. If rejected, **STOP** and choose another terminal rule; do not silently return the credit to availability or relabel expiry as consumption.

## 6.4 Existing authority explicitly preserved

The candidate does not reopen:

- `DEC-045` refund boundary;
- `DEC-054` one active attempt / save-resume / technical recovery;
- `DEC-056` 30-day attempt expiry itself;
- `DEC-057` annual retake interval;
- `DEC-061` immutable raw result;
- `DEC-066` historical delivered report;
- `DEC-067` version/result immutability;
- `DEC-303` unused-credit purchase limits;
- assessment methodology, scoring, tie/mask rules or clinical interpretation;
- current Temperament / Entitlements ownership split.

Proposed `DEC-313` supersedes `DEC-055` **only** for assessment-credit consumption timing/meaning and the associated terminal credit consequence.

---

# 7. Validation against focused evidence

The candidate supplies a deterministic Product-level answer to every `OPS-PT-163...174` case:

| PT | Candidate result |
|---|---|
| `163` first answer | hold unconsumed; second sale blocked |
| `164` abandon after answers | held while active; nontechnical expiry closes unconsumed |
| `165` technical failure before result | same-obligation recovery or technical refund; no duplicate credit |
| `166` result exists but delivery incomplete | hold unconsumed; recover existing result/report lineage |
| `167` in-product delivery qualifies; notification fails | notification does not alter consumption truth |
| `168` participant never opens | open/read telemetry does not control consumption |
| `169` second purchase during held credit | reject under current unused-credit cap |
| `170` 30-day expiry | pre-answer release; post-answer nontechnical close; technical branch recovers/refunds |
| `171` controlled recovery | same credit/result lineage; consume at most once |
| `172` ordinary refund after first answer | remains unavailable under `DEC-045`; refundability ≠ consumption |
| `173` duplicate completion/delivery | one result/right; one consumption |
| `174` operator manually marks consumed | prohibited; operator cannot substitute for Product delivery event |

No new pressure test or upstream class is required for this candidate.

---

# 8. Formal authority-successor footprint proposed by the candidate

This pass does **not** execute the following changes. It identifies the smallest formal package for the next approved authority-build/review pass:

| Authority/artifact | Proposed formal action |
|---|---|
| `01_DECISIONS_v1.6.0.md` | proposed `v1.7.0`; append `DEC-313` and explicit limited supersession of `DEC-055` |
| `00_PLATFORM_v1.6.0.md` | proposed `v1.7.0`; add §21R.6 |
| `05_ROADMAP_v1.2.0.md` | proposed `v1.3.0`; synchronize FP-003 exit condition only |
| `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` | no semantic amendment expected |
| `03_ARCHITECTURE_v1.1.1.md` | no amendment expected |
| `04_DOMAIN_MAP_v1.2.0.md` | no amendment expected |
| `02_OPEN_WORK_v1.2.59.md` | patch successor only after actual promotion/status change |
| README + authority manifest | route/hash updates only when new authority is made current |
| predecessor authority files | preserve byte-identically in archive |
| Foundation Integrity/tests | assert new rule, limited supersession, routing and negative regression against attempt-start consumption |

The proposed SemVer values and `DEC-313` identifier are candidate planning values, not current authority.

---

# 9. Formal-promotion proof requirements

Before the candidate may become current authority, prove at minimum:

1. current predecessor authority bytes are preserved;
2. `DEC-313` explicitly limits its supersession of `DEC-055`;
3. Product §21R.6 and `DEC-313` agree on claim, delivery, expiry closure and technical-failure branches;
4. FP-003 synchronizes rather than legislates competing Product semantics;
5. North Star, Architecture and Domain ownership are unchanged unless a real contradiction is found;
6. Foundation Integrity asserts the new lifecycle and current ownership;
7. a negative regression test rejects reintroduction of attempt-start consumption as current law without later explicit supersession;
8. README/manifest route exactly one current Platform, Decisions and Roadmap successor;
9. archive paths/hashes are correct;
10. exact-head CI passes;
11. fresh independent exact-head semantic review passes;
12. after merge, resulting-main tree/routing and Foundation Integrity are reverified before current-status certification.

No application code, Ash Resource, schema, migration or provider integration belongs in that authority package.

---

# 10. Current STOP / non-inference rules

Until the formal successor is approved and current:

- do not treat proposed `DEC-313` or §21R.6 as current Product Law;
- do not let JIT choose attempt-start versus successful-delivery consumption;
- do not infer `close_unconsumed` from `DEC-056` alone;
- do not equate ordinary refundability with consumption;
- do not equate result creation, report generation, notification delivery or open/read analytics with successful Product delivery;
- do not mint a replacement credit/result for technical recovery;
- do not let Support/Finance manually resolve the conflict;
- do not amend Architecture or Domain Law merely to represent the lifecycle;
- do not start implementation from this candidate.

---

# 11. Promotion sequence after this pass

The v0.8.0 convergence sequence remains:

```text
1. formal OPS-UPD-004 Product/Decision successor + independent review
2. OPS-UPD-001 promotion
3. OPS-UPD-002 promotion
4. OPS-UPD-005 promotion
5. OPS-UPD-007 promotion
6. OPS-UPD-006 after legal/privacy validation
7. bounded OPS-UPD-003 FP-006 operations-policy freeze
8. final convergence / Pre-JIT freeze audit
```

Do not move to item 2 merely because this working candidate exists. Item 1 is complete only when the formal authority successor has passed review and current-status governance.

---

# 12. v0.9.0 disposition

```text
SEMANTIC PRESSURE TESTS ADDED: NONE
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
DISCOVERY SUCCESSOR: NONE (v0.14.0 REMAINS LATEST)
OPS-UPD-004 PROMOTION CANDIDATE: READY FOR FORMAL AUTHORITY-SUCCESSOR BUILD / INDEPENDENT REVIEW
LIVE OPS-UPD-004 CONFLICT_STOP: REMAINS
OPS-GAP-010: OPEN / CONFLICT_STOP; CANDIDATE READY
PROPOSED DEC-313 / PRODUCT §21R.6: WORKING CANDIDATE ONLY
PROPOSED CUSTOMER-RIGHT CHOICE: POST-FIRST-ANSWER NONTECHNICAL EXPIRY → CLOSE_UNCONSUMED; EXPLICIT FORMAL PRODUCT APPROVAL REQUIRED
ARCHITECTURE AMENDMENT: NOT JUSTIFIED
DOMAIN MAP AMENDMENT: NOT JUSTIFIED
NEW DOMAIN: NOT JUSTIFIED
NEW OPS-UPD-008: NOT JUSTIFIED
IMPLEMENTATION: NOT AUTHORISED
CURRENT AUTHORITY MODIFICATION: NONE
PR: NONE
AUTHORITY-PROMOTION CANDIDATE PASS: PASS / CONVERGED
BROAD PRE-JIT FREEZE: NOT READY
NEXT PASS: FORMAL OPS-UPD-004 PRODUCT/DECISION AUTHORITY-SUCCESSOR BUILD + INDEPENDENT REVIEW ONLY
```
