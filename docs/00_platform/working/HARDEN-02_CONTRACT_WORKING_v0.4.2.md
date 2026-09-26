# HARDEN-02_CONTRACT_WORKING_v0.4.2.md

- **Contract ID:** `HARDEN-02`
- **Plan / contract version:** `v0.4.2`
- **Status:** Original v0.4.0 contract lifecycle **COMPLETE / CERTIFIED** — HARDEN-02 execution **NEXT / AUTHORISED / NOT STARTED**
- **Authority class:** WORKING GOVERNANCE CONTRACT — Phase-7 delivery-pipeline sequencing and structural-hardening obligations only
- **Authoritative for:** HARDEN-02 identity, objective, in/out scope, structural invariants, permitted/prohibited execution classes, proof obligations, exit criteria, STOP criteria, and post-HARDEN-02 resume order
- **Not authoritative for:** Product Law, Architecture Law, Domain Law, Roadmap Law, Operating Model freeze meaning, Feature Pack capability content, OQ resolution, Horizontal Hardening (`HH-nnn`), Store Blueprint / CER reuse, Commerce/Entitlements semantics, or implementation
- **Conflict rule:** Live Product / Architecture / Domain / Roadmap / Operating Model / current Open Work authority wins. This contract may not invent Product or Architecture law. Atlas remains derived navigation only and does not create HARDEN-02 law.
- **Baseline repository:** `https://github.com/JCSchoeman96/NewYou`
- **Status-successor base main SHA:** `9411b34b646d7752d2942afca1363830d3b25f10`
- **Certified contract PR:** [#40](https://github.com/JCSchoeman96/NewYou/pull/40), exact head `cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4`, merged unchanged as `352f304139b9d4f8ee3ba205cde9e34d0ad8437f`
- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.1.md` — preserved byte-identically as the pending-post-merge status snapshot
- **Certified contract semantics:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.0.md` — the original v0.4.0 semantics are certified; this v0.4.2 successor records lifecycle completion against current repository routing and does not amend that contract
- **Historical predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.3.0.md` — merged through PR #39; v0.3.0 GitHub-identity independence mechanism not satisfied for solo-maintainer workflow; not retroactively certified
- **Earlier historical predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.2.0.md` — previous contract attempt; not certified
- **Accepted human scope decisions:** `H02-1`, `H02-2`, `H02-3` (2026-09-09), `H02-3R` (2026-09-23; routing refinement)
- **Last updated:** 2026-09-25

### Revision log

- `v0.1.0` — initial HARDEN-02 governance contract after independent analysis review and accepted human scope decisions H02-1 / H02-2 / H02-3; pre-merge correction removes unreproducible local HARDEN-01 plan SHAs, clarifies merge + post-merge execution entry, and clarifies that package/reuse taxonomy is not applicable.
- `v0.2.0` — routing-only successor. Preserves H02-1/H02-2 and historical H02-3, records accepted H02-3R, and inserts Engineering Standards Authority Promotion as the sole post-HARDEN-02 NEXT stage before FP-001 reconciliation. Does not execute HARDEN-02, promote standards, amend upstream law or authorise implementation.
- `v0.3.0` — recovery and re-baseline after repository-verifiable independent pre-merge certification for v0.2.0 could not be established. Preserves v0.2.0 as historical evidence, adds exact-SHA GitHub-visible pre-merge and post-merge certification requirements, and keeps HARDEN-02 execution NOT STARTED / NOT AUTHORISED until the full new lifecycle passes.
- `v0.4.0` — solo-maintainer certification-mechanism amendment. Preserves v0.3.0 byte-identically as historical evidence. Replaces GitHub-account independence with independent **review actor** versus **attestation poster** attribution. Records PR #39 merge facts without retroactively certifying the v0.3.0 lifecycle. Establishes the usable certification mechanism prospectively from this amendment PR. Pre-merge independent exact-head review PASS and exact-head Foundation Integrity PASS are both required and may complete in either order; durable GitHub attestation binds both only after both exist. Does not execute HARDEN-02, promote Engineering Standards, or authorise implementation.
- `v0.4.1` — historical status-only lifecycle snapshot. At that point, the fresh post-merge independent inspection and durable post-merge attestation were pending, and HARDEN-02 execution remained NOT STARTED / NOT AUTHORISED. The original v0.4.0 lifecycle is now COMPLETE / CERTIFIED, as recorded by this v0.4.2 status successor. No contract scope, invariant, proof boundary or downstream route is changed.
- `v0.4.2` — status-only successor. Records completion of the original v0.4.0 lifecycle using status-successor base main SHA `9411b34b646d7752d2942afca1363830d3b25f10`: exact-head certification and CI PASS, unchanged certified-head merge, resulting-main CI PASS, fresh independent post-merge review PASS and durable post-merge attestation COMPLETE. HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED. No v0.4.0 scope, invariant, proof boundary or downstream route is changed.

---

## 1. Objective

HARDEN-02 exists to prove and harden Phase-7 delivery-pipeline governance integrity so that, after certified execution, the separately governed Engineering Standards Authority Promotion stage can run before narrow `FP001_RECONCILIATION_REQUIRED` work and ordinary Phase-7B continuation resume, without stale routing, false authority dependencies, bypassed Phase-7 gates, or premature implementation authorisation.

---

## 2. Authority basis

### CURRENT AUTHORITY

| Source | Use |
|---|---|
| `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md` | MVP / Phase 7–8 boundary context |
| `00_PLATFORM_v1.4.1.md` | Product Law; not amended by HARDEN-02 |
| `01_DECISIONS_v1.4.1.md` | Decision / OQ register; HARDEN-02 is not an OQ |
| `02_OPEN_WORK_v1.2.45.md` | Programme routing and Development Entry Hard Stop |
| `03_ARCHITECTURE_v1.1.1.md` | Architecture synthesis; unchanged |
| `04_DOMAIN_MAP_v1.1.1.md` | Domain Law including PMR ownership and `FP001_RECONCILIATION_REQUIRED` consequence |
| `05_ROADMAP_v1.1.2.md` | Roadmap Law; PMR REQUIRED in FP-001; Feature Pack count 17 |
| `PLATFORM_OPERATING_MODEL_v1.0.1.md` | Phase 7 handoff: Skeleton + Gate Manifest → required JIT Domain Dossiers → Final Feature Pack Contract |
| `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` | Out of HARDEN-02 scope unless a later governance task requires frontend routing hygiene |

### CURRENT DERIVED EVIDENCE

| Source | Use |
|---|---|
| `working/DELIVERY_ATLAS_WORKING_v0.2.1.md` | Derived Phase-7 / proof / HH lifecycle navigation only; does not create HARDEN-02 law |
| `working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md` | Current FP-001 Phase 7A factual state (not reconciled for PMR; not amended by HARDEN-02) |
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
- `PLATFORM_OPERATING_MODEL_v1.0.1.md` — Phase 7 handoff shape: Skeleton + Gate Manifest → required JIT Domain Dossiers → Final Feature Pack Contract;
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

### 11.1 Contract recovery record

Contract v0.2.0 is historical evidence of the previous contract attempt. [PR #37](https://github.com/JCSchoeman96/NewYou/pull/37) merged head `b1b0431152481006bbc1eff33cc9844a1b8c1ad5` into base `91c1e64f9a99ede8be77040287173d450c1043ff`, producing merge commit `2599638334b761ddef8e5568d0a38c3207eef722`. Its exact-head Foundation Integrity run [35859522372](https://github.com/JCSchoeman96/NewYou/actions/runs/35859522372) passed on the PR head. The post-merge Foundation Integrity run [35875423226](https://github.com/JCSchoeman96/NewYou/actions/runs/35875423226) passed on resulting `main` SHA `2599638334b761ddef8e5568d0a38c3207eef722`. These merge and CI facts remain valid historical facts.

The GitHub record for PR #37 contains no submitted review or review comment that certifies its exact head. The missing independent pre-merge certification means v0.2.0's COMPLETE / CERTIFIED lifecycle was never repository-verifiably established. v0.3.0 does not retroactively repair or certify v0.2.0. Its lifecycle was re-baselined from then-current `main` commit `2599638334b761ddef8e5568d0a38c3207eef722`.

The historical v0.3.0 recovery followed v0.2.0 §13: re-baseline and amend the contract rather than silently expanding scope.

Under that historical v0.3.0 recovery PR, HARDEN-02 execution remained NOT STARTED / NOT AUTHORISED. No merge or CI fact from v0.2.0 authorised execution under the v0.3.0 successor. That historical gate is superseded by the completed v0.4.0 lifecycle recorded in §11.5; current HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED.

### 11.1.1 PR #39 / v0.3.0 historical record (not retroactive certification)

[PR #39](https://github.com/JCSchoeman96/NewYou/pull/39) merged contract recovery v0.3.0. Certified candidate head: `887230fee605f34d4aef36d044737c1cfe257c49`. Merge commit on `main`: `6f9ce049616881805b1086d19ce747358de3c067`. Post-merge Foundation Integrity run [35969382003](https://github.com/JCSchoeman96/NewYou/actions/runs/35969382003) passed on resulting `main`. These merge and CI facts remain valid historical evidence.

Substantive independent review of that exact candidate head was performed by ChatGPT and received outcome PASS before merge. The durable GitHub attestation was posted through maintainer identity `JCSchoeman96` (PR author). Audit comment [5809723449](https://github.com/JCSchoeman96/NewYou/issues/comments/5809723449) explicitly records that the GitHub posting identity was **not** independently owned and does **not** satisfy v0.3.0's GitHub-account independence rule.

Therefore:

- do **not** retroactively call the v0.3.0 certification lifecycle satisfied;
- do **not** treat PR #39 as establishing HARDEN-02 execution authority;
- treat v0.4.0 as the prospective certification mechanism from this amendment PR forward.

### 11.2 Review actor versus attestation poster

**Review actor** — the entity that performs substantive independent review of the exact candidate head. In a solo-maintainer AI-assisted workflow, an acceptable independent review actor may be an external reasoning/review system such as `ChatGPT / GPT-5.6 Sol`, provided that actor:

- did not author or modify the exact candidate head being certified;
- independently inspects the live repository state and actual exact-head diff;
- checks relevant authority, tests, CI and scope rather than accepting a handoff summary;
- reports a governed review outcome;
- identifies the exact SHA reviewed;
- repeats review if that SHA changes.

**Attestation poster** — the GitHub identity that durably records the review result on the recovery PR. In a solo-maintainer repository the attestation poster may be the PR author / repository owner. Poster identity equality with the PR author does **not** by itself invalidate otherwise independent review.

The durable attestation must truthfully disclose:

- independent review actor;
- GitHub posting identity (attestation poster);
- whether posting identity equals PR author;
- exact reviewed SHA;
- review outcome;
- applicable CI run;
- whether the review actor authored or modified the reviewed candidate;
- that the substantive reviewer is the review actor, not misidentified as the GitHub poster when that is false.

Prohibited: describing the GitHub poster as the independent substantive reviewer when the review actor is a separate system or person. Prohibited: self-certification disguised as AI review (the maintainer cannot name themselves as the review actor while only repeating their own handoff without independent inspection).

### 11.3 Independence invariant (review work, not account ownership)

Review independence **fails** when:

- the claimed review actor authored or modified the candidate being reviewed;
- the review merely repeats an agent handoff without independently inspecting GitHub;
- reviewed SHA is missing or does not equal the candidate head;
- the candidate head changes after review;
- the review outcome is missing or not PASS;
- the durable attestation misrepresents who performed the review;
- CI evidence is missing or refers to a different SHA;
- attestation poster equals PR author but that fact is not truthfully disclosed;
- posting identity is missing from the attestation.

A solo maintainer posting an independent AI review to GitHub is acceptable when attribution is explicit and truthful.

### 11.4 v0.4.0 certification lifecycle requirements

The v0.4.0 lifecycle is fail-closed. Pre-merge and post-merge stages have required evidence, but pre-merge review and pre-merge CI are **not** required to occur in a fixed chronological order.

```text
candidate exact head
→ independent exact-head review PASS
  AND
→ Foundation Integrity PASS on same exact head
  (either may happen first)
→ durable GitHub attestation binds review + CI + exact head
→ immediate pre-merge head verification
→ merge unchanged certified head
→ Foundation Integrity PASS on resulting main
→ fresh independent post-merge review
→ durable post-merge attestation
→ only then HARDEN-02 execution may become NEXT / AUTHORISED
```

**Pre-merge required inputs (either order):**

1. An independent review actor inspects the exact immutable PR head, without having authored or modified that head, and reports outcome PASS for that exact SHA.
2. Foundation Integrity CI must PASS on that same exact PR head SHA.

**Pre-merge attestation (only after both inputs exist):**

3. The attestation poster leaves a repository-verifiable record on that same PR (submitted PR review or clearly identified PR review comment) that binds, for the same exact head SHA:
   - independent review actor;
   - review outcome PASS;
   - attestation poster identity and truthful poster-equals-author disclosure;
   - whether the review actor authored or modified the candidate;
   - the applicable exact-head Foundation Integrity run;
   - CI conclusion PASS.

**Merge gate:**

4. Immediately before merge, verify the live PR head still equals the reviewed head and the CI-covered head. Head drift invalidates prior review and CI evidence; repeat review and CI for the new SHA.
5. Merge only that verified unchanged head.

**Post-merge:**

6. Foundation Integrity CI must PASS on the resulting `main` SHA.
7. An independent review actor performs a fresh post-merge inspection (not a handoff replay) and reports PASS.
8. The attestation poster leaves durable post-merge attestation binding resulting `main` SHA, certified PR head relationship, post-merge CI run/result and PASS.
9. Only then may HARDEN-02 execution become NEXT / AUTHORISED.

Before merge, post-merge evidence cannot exist and is not a merge prerequisite. After merge, execution remains NOT STARTED / NOT AUTHORISED until resulting-main CI PASS, fresh post-merge review and post-merge attestation are present.

Independent exact-head review and exact-head CI may complete in either order. The contract does **not** require `review → attestation → CI` as a strict chronological sequence. It requires that the durable pre-merge attestation be created only after both the independent review PASS and the exact-head Foundation Integrity PASS exist, and that the attestation truthfully binds both to the same immutable head SHA.

Passing contract-stage unit tests or fixture syntax alone does **not** establish certification. Certification requires repository-verifiable GitHub attestation and CI on the governing SHAs.

The smallest required attestation field groups are:

<!-- HARDEN_02_CERTIFICATION_EVIDENCE_SPEC_START -->
```json
{
  "pre_merge_review": [
    "reviewed_head_sha",
    "outcome",
    "reviewed_head_is_certified_head",
    "independent_review_actor",
    "attestation_poster_github_identity",
    "poster_equals_pr_author_disclosed",
    "poster_equals_pr_author",
    "review_actor_authored_or_modified_candidate",
    "substantive_reviewer_is_review_actor_not_poster",
    "ci_head_sha",
    "ci_workflow",
    "ci_conclusion",
    "ci_run_url",
    "record_url"
  ],
  "pre_merge_ci": ["head_sha", "conclusion", "workflow", "run_url"],
  "merge": ["certified_head_sha", "head_sha_verified_before_merge", "merged_head_sha", "resulting_main_sha"],
  "post_merge_ci": ["head_sha", "conclusion", "workflow", "run_url"],
  "post_merge_certification": [
    "resulting_main_sha",
    "certified_head_sha",
    "ci_head_sha",
    "ci_conclusion",
    "ci_run_url",
    "outcome",
    "independent_review_actor",
    "attestation_poster_github_identity",
    "poster_equals_pr_author_disclosed",
    "poster_equals_pr_author",
    "review_actor_authored_or_modified_candidate",
    "substantive_reviewer_is_review_actor_not_poster",
    "record_url"
  ]
}
```
<!-- HARDEN_02_CERTIFICATION_EVIDENCE_SPEC_END -->

The `record_url` values must link to a GitHub-visible PR review or identified PR review comment on the same expected recovery PR. Evidence validation receives the expected recovery PR number and rejects records bound to a different PR. Merge evidence must record `head_sha_verified_before_merge` as the exact certified head SHA.

The `pre_merge_review` CI binding fields must exactly match the independently verifiable `pre_merge_ci` record for the same exact head: `ci_head_sha` equals the reviewed/certified head and `pre_merge_ci.head_sha`; `ci_workflow` is `Foundation Integrity` and equals `pre_merge_ci.workflow`; `ci_conclusion` is `PASS` and equals `pre_merge_ci.conclusion`; `ci_run_url` equals `pre_merge_ci.run_url` and is a valid repository Actions run URL. The durable attestation referenced by `pre_merge_review.record_url` is not valid if these bindings disagree with `pre_merge_ci`.

| State | Meaning |
|---|---|
| `v0.2.0: HISTORICAL / NOT REPOSITORY-VERIFIABLY CERTIFIED` | Prior contract attempt; merge/CI facts remain evidence; missing pre-merge certification blocks COMPLETE / CERTIFIED |
| `v0.3.0: MERGED / NOT RETROACTIVELY CERTIFIED` | Merged via PR #39; substantive ChatGPT PASS on candidate head; v0.3.0 GitHub-identity rule not met; lifecycle not satisfied retroactively |
| `HARDEN-02 CONTRACT v0.4.0: COMPLETE / CERTIFIED` | Independent review-actor exact-head PASS and exact-head CI PASS (either order) + pre-merge attestation binding both + unchanged-head merge + post-merge CI PASS + fresh post-merge review + post-merge attestation |
| `HARDEN-02_EXECUTION_REQUIRED` | Current NEXT stage after the original v0.4.0 contract lifecycle is complete |
| `HARDEN-02 EXECUTION: NEXT / AUTHORISED / NOT STARTED` | Current state; lifecycle completion permits execution to be NEXT / AUTHORISED, but this status record does not begin execution |
| `HARDEN-02 EXECUTION: COMPLETE / CERTIFIED` | All I-01…I-13 proofs pass; NEXT = `ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED` |
| Terminal failure | STOP and escalate; do not invent law |

The later external state `ENGINEERING STANDARDS PROMOTION: COMPLETE / CERTIFIED → NEXT = FP001_RECONCILIATION_REQUIRED` is owned by current Open Work and the later promotion stage, not by HARDEN-02.

**Execution entry rule:** pre-merge attestation alone is not sufficient to start HARDEN-02 execution. Execution becomes NEXT / AUTHORISED only after independent exact-head review PASS and exact-head Foundation Integrity PASS both exist, a pre-merge attestation truthfully binds both to the same head, that head is merged unchanged, resulting `main` passes CI, and fresh post-merge review plus post-merge attestation are repository-verifiably present.

### 11.5 PR #40 lifecycle evidence and current state

[PR #40](https://github.com/JCSchoeman96/NewYou/pull/40) certified exact head `cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4`. The repository-visible [pre-merge attestation](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5827553565) records independent review outcome PASS, exact-head binding and CI. Exact-head [Foundation Integrity run 36091130615](https://github.com/JCSchoeman96/NewYou/actions/runs/36091130615) passed with 142 tests, 280 FIA checks and no findings.

The certified PR head merged unchanged as `352f304139b9d4f8ee3ba205cde9e34d0ad8437f` at `2026-09-25T06:03:58Z`. The merge commit has first parent `6f9ce049616881805b1086d19ce747358de3c067`, second parent the certified head, and the same tree as that head. Resulting-main [Foundation Integrity run 36101210535](https://github.com/JCSchoeman96/NewYou/actions/runs/36101210535) passed on that SHA with 142 tests, 280 FIA checks and no findings.

The pre-merge attestation records review actor `ChatGPT / GPT-5.6 Sol`, poster `JCSchoeman96`, poster equals PR author, review actor authored or modified candidate `false`, and substantive reviewer is the review actor rather than the poster. The post-merge [attestation](https://github.com/JCSchoeman96/NewYou/pull/40#issuecomment-5830618876) records review actor `Codex / GPT-6`, poster `JCSchoeman96`, poster equals PR author, review actor authored or modified candidate `false`, and substantive reviewer is the review actor rather than the poster. That record reports fresh post-merge review outcome PASS and binds resulting main SHA, certified head, resulting-main CI run and PASS.

The v0.4.0 contract lifecycle is COMPLETE / CERTIFIED. The verified status-successor base main SHA is `9411b34b646d7752d2942afca1363830d3b25f10`, after PR #42 updated the authority and routing. This v0.4.2 artifact records lifecycle completion against that base; it does not claim that SHA remains the repository tip after this status successor merges. It does not revise or recertify v0.4.0 semantics. HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED.

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

### Contract stage (PR #40, v0.4.0)

- this contract artifact present with objective, boundaries, exclusions and resume order;
- focused contract tests PASS;
- full unit tests PASS;
- Foundation Integrity audit PASS;
- upstream protected authority hashes unchanged;
- no application code changed;
- exact-head certification and CI PASS on `cb710860f4db65ce4ef2f2ad50a4d4a967c0b9f4`;
- certified head merged unchanged as `352f304139b9d4f8ee3ba205cde9e34d0ad8437f`;
- resulting-main CI PASS on that SHA;
- post-merge independent inspection PASS and durable post-merge attestation COMPLETE; the original v0.4.0 contract lifecycle is COMPLETE / CERTIFIED.

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

subject to then-current authority. The complete H02-3R route remains:

```text
CERTIFIED HARDEN-02 EXECUTION
→ ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED
→ CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION
→ FP001_RECONCILIATION_REQUIRED
→ COMMUNICATIONS JIT DOMAIN DOSSIER
→ REMAINING REQUIRED / CONDITIONAL PHASE 7B
→ PHASE 7C
→ PROOF CLASSIFICATION
→ PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES
```

This route does not authorise work on a downstream stage early. The separately certified Engineering Standards Authority Promotion must finish before FP-001 reconciliation becomes NEXT. Communications follows FP-001 reconciliation. Remaining required and conditional Phase-7B work must pass before Phase 7C; proof classification follows Phase 7C; Phase 8 remains gated by the Development Entry Hard Stop.

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

This artifact records the HARDEN-02 contract lifecycle status only. HARDEN-02 is not authority for Product, Architecture, Domain or Roadmap law, Engineering Standards promotion, FP-001 reconciliation, Communications or implementation. No application implementation is authorised.

This status-sync artifact itself does not execute HARDEN-02. The original v0.4.0 contract lifecycle remains COMPLETE / CERTIFIED on its recorded evidence. Do not reopen it or describe its evidence as missing without new contradictory repository evidence that challenges a recorded lifecycle requirement. If such evidence appears, STOP and resolve it through the applicable governed review. This status successor does not alter the certified v0.4.0 semantics.

Current HARDEN-02 execution is NEXT / AUTHORISED / NOT STARTED. This authorises a separately governed HARDEN-02 execution task to begin; it does not mean execution has begun. Execution remains NOT STARTED until that separate task explicitly begins. Do not mark HARDEN-02 execution COMPLETE / CERTIFIED until all required I-01…I-13 execution proofs PASS and the applicable execution certification lifecycle is complete.

Preserve the fail-closed downstream gates:

- do not begin Engineering Standards Authority Promotion before HARDEN-02 execution is COMPLETE / CERTIFIED;
- do not begin FP-001 reconciliation before Engineering Standards Authority Promotion is COMPLETE / CERTIFIED;
- begin Communications only after FP-001 reconciliation is complete;
- keep Phase 7C blocked until required and conditional Phase-7B work passes its applicable gates;
- do not finalise proof classification before Phase 7C is complete;
- keep Phase 8 blocked until the Development Entry Hard Stop passes;
- this lifecycle-status synchronization does not authorise application implementation.
