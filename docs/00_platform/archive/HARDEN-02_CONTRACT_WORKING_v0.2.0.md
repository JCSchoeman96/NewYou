# HARDEN-02_CONTRACT_WORKING_v0.2.0.md

- **Contract ID:** `HARDEN-02`
- **Plan / contract version:** `v0.2.0`
- **Status:** OPEN / PENDING INDEPENDENT CERTIFICATION — contract drafting complete; HARDEN-02 execution **NOT AUTHORISED** by this artifact alone
- **Authority class:** WORKING GOVERNANCE CONTRACT — Phase-7 delivery-pipeline sequencing and structural-hardening obligations only
- **Authoritative for:** HARDEN-02 identity, objective, in/out scope, structural invariants, permitted/prohibited execution classes, proof obligations, exit criteria, STOP criteria, and post-HARDEN-02 resume order
- **Not authoritative for:** Product Law, Architecture Law, Domain Law, Roadmap Law, Operating Model freeze meaning, Feature Pack capability content, OQ resolution, Horizontal Hardening (`HH-nnn`), Store Blueprint / CER reuse, Commerce/Entitlements semantics, or implementation
- **Conflict rule:** Live Product / Architecture / Domain / Roadmap / Operating Model / current Open Work authority wins. This contract may not invent Product or Architecture law. Atlas remains derived navigation only and does not create HARDEN-02 law.
- **Baseline repository:** `https://github.com/JCSchoeman96/NewYou`
- **Contract drafting baseline SHA:** `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`
- **Routing-refinement baseline SHA:** `91c1e64f9a99ede8be77040287173d450c1043ff`
- **Accepted human scope decisions:** `H02-1`, `H02-2`, `H02-3` (2026-09-09), `H02-3R` (2026-09-23; routing refinement)
- **Last updated:** 2026-09-23

### Revision log

- `v0.1.0` — initial HARDEN-02 governance contract after independent analysis review and accepted human scope decisions H02-1 / H02-2 / H02-3; pre-merge correction removes unreproducible local HARDEN-01 plan SHAs, clarifies merge + post-merge execution entry, and clarifies that package/reuse taxonomy is not applicable.
- `v0.2.0` — routing-only successor. Preserves H02-1/H02-2 and historical H02-3, records accepted H02-3R, and inserts Engineering Standards Authority Promotion as the sole post-HARDEN-02 NEXT stage before FP-001 reconciliation. Does not execute HARDEN-02, promote standards, amend upstream law or authorise implementation.

---

## 1. Objective

HARDEN-02 exists to prove and harden Phase-7 delivery-pipeline governance integrity so that, after certified execution, the separately governed Engineering Standards Authority Promotion stage can run before narrow `FP001_RECONCILIATION_REQUIRED` work and ordinary Phase-7B continuation resume, without stale routing, false authority dependencies, bypassed Phase-7 gates, or premature implementation authorisation.

---

## 2. Authority basis

### CURRENT AUTHORITY

| Source | Use |
|---|---|
| `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md` | Unchanged MVP / Phase 7–8 boundary context |
| `00_PLATFORM_v1.3.0.md` | Product Law; not amended by HARDEN-02 |
| `01_DECISIONS_v1.3.0.md` | Decision / OQ register; HARDEN-02 is not an OQ |
| `02_OPEN_WORK` current successor | Programme routing and Development Entry Hard Stop |
| `03_ARCHITECTURE_v1.1.0.md` | Architecture synthesis; unchanged |
| `04_DOMAIN_MAP_v1.1.0.md` | Domain Law including PMR ownership and `FP001_RECONCILIATION_REQUIRED` consequence |
| `05_ROADMAP_v1.1.0.md` | Roadmap Law; PMR REQUIRED in FP-001; Feature Pack count 17 |
| `PLATFORM_OPERATING_MODEL_v1.0.0.md` | Phase 7 handoff: Skeleton + Gate Manifest → required JIT Domain Dossiers → Final Feature Pack Contract |
| `FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md` | Out of HARDEN-02 scope unless a later governance task requires frontend routing hygiene |

### CURRENT DERIVED EVIDENCE

| Source | Use |
|---|---|
| `working/DELIVERY_ATLAS_WORKING_v0.2.0.md` | Derived Phase-7 / proof / HH lifecycle navigation only; does not create HARDEN-02 law |
| `working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md` | Current FP-001 Phase 7A factual state (stale for PMR reconciliation; not amended here) |
| `working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` | Identity dossier complete/merged factual state (not amended here) |

### HISTORICAL AUTHORITY / WORKING EVIDENCE

| Source | Class | Recovered meaning |
|---|---|---|
| `archive/02_OPEN_WORK_v1.2.29.md` | HISTORICAL AUTHORITY | HARDEN-02 is governance sequencing, not an FP-001 dependency, Roadmap gate, Product requirement or blocking OQ; next FP-001 domain task after HARDEN-02 was Communications |
| PR #24 (`docs/resolve-oq034-and-sync-fp001-state`) | HISTORICAL COMPLETION EVIDENCE | HARDEN-01 / OQ-034 state sync complete on canonical GitHub; left HARDEN-02 as next governance / delivery-pipeline task without starting Communications, Phase 7C or implementation |
| `archive/02_OPEN_WORK_v1.2.30.md` … `v1.2.38.md` | HISTORICAL AUTHORITY | HARDEN-02 suspended through targeted amendment programme until Atlas reconciliation |
| `archive/02_OPEN_WORK_v1.2.39.md` | HISTORICAL AUTHORITY (this PR) | Post-Atlas routing: `HARDEN-02_CONTRACT_REQUIRED` |

Historical material recovers intended HARDEN-02 semantics. It does not override current Roadmap/Domain PMR reconciliation requirements or current Open Work routing.

Non-canonical / unreproducible local-only HARDEN-01 plan SHAs are intentionally **not** cited here. The current structural invariant suite I-01…I-13 does not depend on them.

---

## 3. Accepted human scope decisions

| ID | Decision | Status |
|---|---|---|
| `H02-1` | HARDEN-02 is bounded Phase-7 delivery-pipeline governance / structural hardening only | ACCEPTED |
| `H02-2` | Store Blueprint / CER is OUT OF SCOPE | ACCEPTED |
| `H02-3` | Historical accepted route: post-HARDEN-02 narrow FP-001 PMR reconciliation → Communications JIT → remaining Phase-7B/7C → proof classification → Phase 8 only when gates pass | SUPERSEDED IN PART by H02-3R only for the immediate post-HARDEN-02 NEXT stage |
| `H02-3R` | Post-HARDEN-02 resume order: Engineering Standards Authority Promotion → narrow FP-001 PMR reconciliation → Communications JIT → remaining Phase-7B/7C → proof classification → Phase 8 only when gates pass | ACCEPTED 2026-09-23 |

---

## 4. In scope

1. Prove one unambiguous current programme NEXT stage for HARDEN-02 execution after this contract is certified.
2. Prove completed stages cannot silently reopen and suspended/downstream work cannot masquerade as current.
3. Prove Phase 7A / 7B / 7C structural coherence for the current Feature Pack preparation state:
   - Phase 7A complete for FP-001;
   - required JIT dossiers cannot be silently skipped;
   - conditional dossiers require explicit disposition;
   - Phase 7C cannot be treated as ready while required dossier/gate state is unresolved;
   - proof classification occurs only after Final Feature Pack Contract.
4. Prove HARDEN-02 is not classified as Product Law, Architecture Law, Domain Law, Roadmap Law, Feature Pack capability, blocking OQ, or Horizontal Hardening.
5. Recognise current FP-001 factual state, including `FP001_RECONCILIATION_REQUIRED` caused by PMR, without performing that reconciliation inside HARDEN-02.
6. Prove executable development remains blocked until Phase 8 entry conditions pass.
7. Prove HARDEN-02 completion does not authorise TB / VS / HH / application implementation.
8. Establish machine-checkable governance/routing/structural tests sufficient for HARDEN-02 exit.
9. On successful certified HARDEN-02 execution, route NEXT exclusively to `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`; FP-001 reconciliation remains downstream until that promotion is complete / certified.

---

## 5. Explicitly out of scope

### Parallel streams (record only to prevent conflation)

- `working/commerce_entitlements/*` CER Pre-JIT / reuse discovery
- any Store Blueprint / Store Blueprint Hardening repository
- subscription-engine hardening, Paystack integration, OQ-004 provider validation as HARDEN-02 work

### Programme work not authorised by HARDEN-02

- narrow FP-001 PMR reconciliation itself
- Communications JIT Domain Dossier creation
- remaining conditional Phase-7B dossier adjudication
- Phase 7C Final Feature Pack Contract
- proof classification finalisation
- Phase 8 Architectural Proof / TB / VS / HH execution
- Engineering Standards design/freeze/promotion execution (HARDEN-02 may route to that separate stage but may not execute or approve it)
- Research / Voting / Interactive Tools / Domain redesign / Roadmap redesign / Atlas redesign
- Product / Architecture / Domain / Roadmap amendments (unless execution discovers a real upstream contradiction and STOPS)
- application source code, Ash Resources, schemas/migrations, packages, provider configuration

---

## 6. Reuse classification

The preliminary package/reuse classification taxonomy is **not applicable** to the accepted HARDEN-02 scope. HARDEN-02 is governance hardening of existing NewYou Phase-7 controls and routing evidence; it is not cross-repository or application-package reuse hardening. No new governed classification identifier is created.

HARDEN-02 proves governance integrity. It does not build a new product capability and does not harden reusable commerce packages.

---

## 7. Recovered historical structural-test intent

### Reproducible historical sources

Canonical, independently retrievable evidence used for HARDEN-02 structural intent:

- `archive/02_OPEN_WORK_v1.2.29.md` — HARDEN-02 as Phase 7B pipeline-governance sequencing, not Product/Roadmap/OQ/FP dependency; Communications as the then-next FP-001 domain task after HARDEN-02;
- PR #24 completion state on canonical GitHub — HARDEN-01 / OQ-034 routing sync completed without starting Communications, Phase 7C, proof or implementation;
- `PLATFORM_OPERATING_MODEL_v1.0.0.md` — Phase 7 handoff shape: Skeleton + Gate Manifest → required JIT Domain Dossiers → Final Feature Pack Contract;
- current Open Work successor — Development Entry Hard Stop and post-amendment programme routing;
- accepted human decisions H02-1 / H02-2 / historical H02-3 / routing refinement H02-3R.

### Failure mode the governance hardening must prevent

After HARDEN-01 / Atlas reconciliation and the targeted amendment programme, the remaining unchecked governance risks include:

- Phase-7 preparation state, dossier requirements, gate dispositions and development-entry stops becoming incoherent;
- governance sequencing being mistaken for a Product/Roadmap/OQ dependency;
- later agents skipping gates, skipping FP-001 reconciliation, or treating governance completion as implementation authority.

### Current derivation rule

The current structural invariant suite I-01…I-13 is derived from **current** Operating Model / Open Work / post-amendment FP-001–PMR authority plus accepted H02-1 / H02-2 / historical H02-3 / H02-3R. Historical Open Work and PR #24 recover sequencing intent; H02-3R explicitly refines only the immediate post-HARDEN-02 route. None of these invent Product or Architecture law.

---

## 8. Current structural invariant suite

### I-01 — Single unambiguous NEXT

Exactly one current programme NEXT stage is declared for HARDEN-02-related routing. Contradictory CURRENT/NEXT markers are a fail.

### I-02 — Completed stages stay completed

Completed amendment-programme and FP-001 Phase 7A / Identity milestones are not reopened by HARDEN-02 routing text.

### I-03 — Downstream cannot masquerade as current

`ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`, `FP001_RECONCILIATION_REQUIRED`, Communications, Phase 7C, proof classification and executable development remain explicitly downstream / blocked during HARDEN-02 execution. Certified HARDEN-02 completion may advance only the Engineering Standards Authority Promotion stage.

### I-04 — Phase-7 progression coherence

Declared FP-001 preparation state must remain coherent with:

```text
Phase 7A Skeleton + Gate Manifest
→ required JIT Domain Dossiers
→ Final Feature Pack Contract
→ proof classification
→ Phase 8 only when Development Entry Hard Stop passes
```

### I-05 — Required dossiers cannot be skipped

Identity complete/merged is factual. Communications remains REQUIRED / NOT_STARTED. HARDEN-02 must not mark Communications complete or optional.

### I-06 — Conditional dossiers need explicit disposition

Privacy & Consent, Content & Media, and Audit & Evidence remain CONDITIONAL / PENDING EXPLICIT ADJUDICATION unless a later authorised task changes them. Analytics remains NOT REQUIRED.

### I-07 — Phase 7C readiness fail-closed

Phase 7C remains BLOCKED / NOT_STARTED while required Communications dossier and conditional dispositions remain unresolved.

### I-08 — Proof classification timing

Proof classification remains NOT FINALISED and must not be treated as complete before Final Feature Pack Contract.

### I-09 — Authority separation

HARDEN-02 must not be described as Product requirement, Roadmap gate, blocking OQ, Feature Pack, Horizontal Hardening, Store hardening, or Commerce/Entitlements hardening.

### I-10 — FP-001 stale-PMR recognition without reconciliation

`FP001_RECONCILIATION_REQUIRED` remains true. HARDEN-02 recognises it and forbids performing the reconciliation inside HARDEN-02.

### I-11 — Implementation stop

Passing HARDEN-02 must not authorise application implementation, TB, VS, HH, package installs, migrations or provider changes.

### I-12 — Post-HARDEN-02 resume order

Certified HARDEN-02 completion routes NEXT only to `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`. That promotion must freeze the applicable supporting Engineering Standards and reconcile repository authority routing before `FP001_RECONCILIATION_REQUIRED` becomes NEXT. Communications remains after FP-001 reconciliation. Phase 7C / Phase 8 remain later.

### I-13 — Store/CER exclusion

No Store repository SHA, CER proof obligation, CER exit condition or Store/CER implementation path may appear in HARDEN-02 baseline, proof, exit criteria or execution scope.

---

## 9. Stale-state / restart pressure tests

| Pressure | Required fail-closed behaviour |
|---|---|
| Duplicate completion markers | Detect contradictory COMPLETE/NEXT for the same stage; fail |
| Contradictory CURRENT/NEXT routing | Fail unless one unambiguous NEXT remains |
| Obsolete artifact versions referenced as current | Fail when active Open Work/README/manifest disagree on current Open Work path/version |
| Completed predecessor still referenced as current | Fail if archived Open Work/Atlas predecessors are treated as active |
| Upstream amendment makes FP artifact stale | Recognise `FP001_RECONCILIATION_REQUIRED`; forbid skipping it to Communications |
| Restart from old agent handoff | Contract + current Open Work win; historical “HARDEN-02 → Communications” alone is insufficient after PMR amendment |
| Branch/head drift | Exact-head certification required before advancing to FP-001 reconciliation |
| Repeated task execution | Idempotent governance checks; no duplicate law amendments |
| Partial documentation update | README / Open Work / manifest disagreement fails integrity checks |
| Agent skips to Communications | Fail; Communications is after FP-001 reconciliation |
| Agent skips Engineering Standards promotion to FP-001 reconciliation | Fail; refined I-12 |
| Agent skips Engineering Standards promotion to Communications | Fail; refined I-12 |
| Agent treats HARDEN-02 completion as Engineering Standards freeze authority | Fail; HARDEN-02 only routes to the promotion stage |
| Agent skips FP-001 reconciliation after certified standards promotion | Fail; I-12 |
| Agent treats HARDEN-02 as implementation authority | Fail; I-11 |

---

## 10. Proof-obligation matrix

| Obligation | Classification | Notes |
|---|---|---|
| HARDEN-02 identity = Phase-7 governance/structural hardening | `ALREADY_PROVEN` by accepted H02-1 + provenance | Locked in this contract |
| Store/CER excluded | `ALREADY_PROVEN` by accepted H02-2 | Locked in this contract |
| Post-H02 resume order inserts Engineering Standards Authority Promotion before FP-001 reconciliation, with reconciliation still before Communications | `ALREADY_PROVEN` by accepted H02-3R plus historical H02-3 | Locked in this successor |
| Contract artifact exists with objective/boundaries | `PROOF_REQUIRED` (this PR) | Contract-stage tests |
| I-01…I-13 structural invariants machine-checkable | `PROOF_REQUIRED` / later `IMPLEMENTATION_AND_PROOF_REQUIRED` | Contract-stage proves contract text; execution stage adds/extends governance tests as needed |
| Open Work / README routing coherence for contract-created state | `PROOF_REQUIRED` (this PR) | Pre-certification wording |
| Manifest Open Work successor hash parity | `PROOF_REQUIRED` (this PR) | FIA |
| Upstream Product/Architecture/Domain/Roadmap hashes unchanged | `PROOF_REQUIRED` (this PR) | Contract-stage tests |
| HARDEN-02 execution substantive governance tests | `IMPLEMENTATION_AND_PROOF_REQUIRED` | Later execution PR only |
| FP-001 PMR reconciliation | `OUT_OF_SCOPE` | Downstream after certified Engineering Standards Authority Promotion |
| Communications dossier | `OUT_OF_SCOPE` | Downstream after reconciliation |
| Store/CER/subscriptions/Paystack/OQ-004 | `OUT_OF_SCOPE` | Parallel / later commercial work |
| Engineering Standards design/freeze | `OUT_OF_SCOPE_FOR_HARDEN_02` | Separate supporting-authority promotion stage; becomes NEXT only after certified HARDEN-02 execution |
| Application code / Ash / migrations | `OUT_OF_SCOPE` | Implementation stop |
| New Product/Architecture/Domain/Roadmap law | `OUT_OF_SCOPE` / escalate if contradiction found | STOP |

“Implementation” for HARDEN-02 means governance tooling/tests/document-routing mechanisms only.

---

## 11. Lifecycle obligations

| State | Meaning |
|---|---|
| `HARDEN-02_CONTRACT_REQUIRED` | Pre-contract historical routing (closed by creating this contract) |
| `HARDEN-02 CONTRACT: OPEN / PENDING CERTIFICATION` | This PR / pre-merge exact-head review state |
| `HARDEN-02 CONTRACT: COMPLETE / CERTIFIED` | Independent pre-merge review + exact-head CI + merge of the certified head unchanged + independent post-merge certification of the resulting `main` |
| `HARDEN-02 EXECUTION: NOT STARTED` | Remains until the contract reaches COMPLETE / CERTIFIED under the row above |
| `HARDEN-02 EXECUTION: NEXT / AUTHORISED` | Allowed only after the certified contract head is merged unchanged and the resulting `main` merge state is independently post-merge certified |
| `HARDEN-02 EXECUTION: COMPLETE / CERTIFIED` | All I-01…I-13 proofs pass; NEXT = `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED` |
| Terminal failure | STOP and escalate to owning authority; do not invent law |

The later external state `ENGINEERING STANDARDS PROMOTION: COMPLETE / CERTIFIED → NEXT = FP001_RECONCILIATION_REQUIRED` is owned by current Open Work and the later separately governed promotion stage, not by HARDEN-02.

**Execution entry rule:** pre-merge exact-head certification of this PR is **not** sufficient to start HARDEN-02 execution. HARDEN-02 execution becomes NEXT / authorised only after the certified contract head is merged unchanged and the resulting `main` is independently post-merge certified.

HARDEN-02 remains governance sequencing. It is not an FP-001 dependency, Roadmap gate, Product requirement or blocking OQ.

---

## 12. Concurrency / idempotency / retry obligations

- Governance checks must be deterministic and repeatable on the same head.
- Re-running HARDEN-02 checks must not create duplicate Open Work successors or contradictory markers.
- Partial updates that leave README, Open Work and manifest disagreeing are failures, not soft warnings.
- Exact-head certification is required; stale local branches are not completion evidence.

---

## 13. Failure / recovery / STOP criteria

STOP and escalate upstream when HARDEN-02 execution or contract review discovers:

1. contradiction with Product / Architecture / Domain / Roadmap / Operating Model authority;
2. attempt to absorb Store/CER/commerce/subscription work into HARDEN-02;
3. attempt to execute or freeze Engineering Standards Authority Promotion, perform FP-001 reconciliation, or perform Communications dossier work inside HARDEN-02;
4. attempt to authorise Phase 8 / TB / VS / HH / application implementation from HARDEN-02 alone;
5. inability to express I-01…I-13 as machine-checkable evidence without inventing new Product/Architecture law;
6. branch/head drift that invalidates the certified baseline without re-certification.

Recovery is re-baseline + amend this contract or the correct upstream authority — never silent scope expansion.

---

## 14. Domain-authority boundaries

HARDEN-02 owns no business Domain truth.

| Concern | Owner |
|---|---|
| Programme routing / Open Work sequencing | Open Work planner authority |
| Phase-7 workflow shape | Operating Model + Open Work |
| FP-001 outcome / PMR sequencing meaning | Roadmap / Domain / Product as already locked |
| Identity / PMR Account truth | Identity & Access |
| Commerce / Entitlements / subscriptions | Commerce and Entitlements Domains (out of HARDEN-02) |
| Store package mechanism | External evidence only; never NewYou authority |

---

## 15. Permitted later HARDEN-02 execution change classes

Only the minimum classes required to prove I-01…I-13:

1. governance / structural unit tests under `tests/`;
2. narrowly necessary extensions to `tools/foundation_integrity_audit.py` if existing checks cannot express a required invariant;
3. Open Work / README routing updates that mark HARDEN-02 execution progress truthfully;
4. authority-manifest refresh for Open Work / README-linked planning-tracker paths only;
5. narrowly necessary working governance documentation that does not create Product/Architecture/Domain/Roadmap law.

No category is permitted merely because it is convenient.

---

## 16. Prohibited later HARDEN-02 execution changes

1. application source code;
2. Ash Resources / actions / policies;
3. schemas / migrations / indexes;
4. package installs for product implementation;
5. Commerce / Entitlements implementation;
6. Store repository changes;
7. subscription / Paystack / provider implementation;
8. PMR encoding/implementation;
9. Communications JIT Domain Dossier creation;
10. FP-001 Skeleton / Gate Manifest / Identity dossier PMR reconciliation;
11. Engineering Standards creation;
12. Product / Architecture / Domain / Roadmap amendments except STOP + upstream escalation;
13. Atlas law invention;
14. CER completion as an H02 exit condition.

---

## 17. Required proof (exit shape)

### Contract stage (this PR)

- this contract artifact present with objective, boundaries, exclusions and resume order;
- focused contract tests PASS;
- full unit tests PASS;
- Foundation Integrity audit PASS;
- upstream protected authority hashes unchanged;
- no application code changed;
- PR OPEN / unmerged pending independent review.

### Execution stage (later, separately authorised)

- machine-checkable proofs for I-01…I-13 PASS;
- governance tests PASS on the exact execution head;
- current authority/routing graph coherent after execution updates;
- no new Product/Architecture/Domain/Roadmap law;
- no FP-001 reconciliation performed;
- no Communications dossier started;
- no implementation authorisation created;
- Open Work NEXT after certified HARDEN-02 execution = `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED`;
- FP-001 reconciliation remains downstream until the standards promotion is complete / certified;
- Communications remains after reconciliation;
- independent exact-head review/CI before merge;
- post-merge certification before beginning Engineering Standards Authority Promotion.

---

## 18. Downstream consequence

Certified HARDEN-02 **execution** completion authorises only the next governed planning stage:

```text
NEXT = ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED
```

HARDEN-02 completion does **not** itself freeze or approve Engineering Standards. The separate promotion stage must complete and be independently certified under then-current authority.

It does **not** directly authorise:

- FP-001 reconciliation;
- Communications JIT Domain Dossier;
- Phase 7C;
- Phase 8;
- implementation.

After independently certified Engineering Standards Authority Promotion, the next planning task is:

```text
NEXT = FP001_RECONCILIATION_REQUIRED
```

After independently certified narrow FP-001 PMR reconciliation, the expected next ordinary FP-001 Phase-7B task is:

```text
Communications JIT Domain Dossier
```

subject to then-current authority, then remaining required/conditional Phase-7B work, then Phase 7C, then proof classification, then Phase 8 only when Development Entry Hard Stop conditions pass.

Historical H02-3 evidence remains historically true for the earlier programme state. Accepted H02-3R refines only the immediate post-HARDEN-02 route by inserting the Engineering Standards supporting-authority promotion stage before FP-001 reconciliation.

---

## 19. Explicit exclusion confirmations

- Store Blueprint / CER: **EXCLUDED**
- Commerce / Entitlements hardening: **EXCLUDED**
- Subscriptions / Paystack / OQ-004: **EXCLUDED**
- FP-001 reconciliation: **NOT PERFORMED by HARDEN-02**
- Communications dossier: **NOT STARTED by HARDEN-02**
- Engineering Standards: **NOT STARTED by HARDEN-02**
- Engineering Standards Authority Promotion: **NOT EXECUTED by HARDEN-02**
- Application code: **UNCHANGED by this contract stage**

---

## 20. Contract-stage STOP

This artifact drafts the HARDEN-02 contract only.

Do not:

- merge without independent certification;
- execute HARDEN-02;
- start FP-001 reconciliation;
- start Communications;
- execute Engineering Standards Authority Promotion or freeze Engineering Standards;
- implement application behaviour.
