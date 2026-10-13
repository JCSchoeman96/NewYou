# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.4.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 4 ONLY — ANL-UPD-001 ROADMAP DELTA CANDIDATE PRESSURE TEST
```

- **Prepared:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked for this pass:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Main drift since Pass 3:** NONE.
- **Pre-pass branch head:** `c975c4b92793d28794f540d8fd907a671f2e62f3`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.3.0.md` — preserved unchanged.
- **Purpose:** pressure-test and draft the smallest internally coherent Roadmap amendment candidate for `ANL-UPD-001`.
- **Scope:** Roadmap sequencing/activation wording only. No Product Law amendment, Domain Law amendment, Architecture amendment, Feature Pack implementation, Research JIT dossier, metric formula, privacy/retention design, provider choice or code.

---

## 1. Pass discipline

Pass 3 resolved the durable source owner for the mandatory FP-006 controlled-pilot value/relevance/price-value instrument to **Research & Feedback**, but found that the current Roadmap keeps that capability future-gated and not automatically assigned to FP-006.

This pass asks only:

1. whether Roadmap is the correct authority layer for the repair;
2. which current Roadmap statements must change together to avoid a new internal contradiction;
3. how narrowly the FP-006 activation can be stated;
4. which areas must remain explicitly unchanged;
5. what promotion collateral would be required if the candidate were later accepted as authority.

The pass does **not** amend `05_ROADMAP_v1.2.0.md`.

---

## 2. Current Roadmap facts under test

Current Roadmap law simultaneously says:

- mature Research & Feedback is generally `FUTURE-GATED / FEATURE-PACK-UNASSIGNED`, “Not MVP” and not automatically assigned to FP-006;
- §3A requires a later governed Roadmap amendment to name an activating Feature Pack and bounded mode;
- no Feature Pack may silently absorb future-gated capability merely because a pilot survey exists;
- FP-006 is the controlled paid-evidence/release boundary;
- FP-006 already requires the Product-Law value/relevance survey, response-rate threshold, price-value question and discounted-participant normal-list-price purchase-intent evidence;
- FP-006 currently omits Research & Feedback from Affected Domains.

Domain Law independently assigns durable truth for bounded lightweight feedback instruments and participant responses to Research & Feedback. Product Law independently requires the FP-006 evidence. The missing authority is therefore sequencing/activation, not requirement or ownership.

---

## 3. Pass-4 pressure-test register

### ANL-PT-007 — Is Roadmap the correct authority level?

**Question:** Does resolving the FP-006 activation seam require Product Law, Domain Law or Architecture Law to change?

**Analysis:** No. Product Law already requires the evidence; Domain Law already supplies the owner and boundaries; Architecture does not need a new mechanism merely to sequence the owning Domain into an existing Feature Pack. Roadmap explicitly says it may activate approved future-gated capability when a concrete Product outcome requires it.

**Disposition:** `PASS`.

**Working conclusion:** `ANL-UPD-001` is semantically a Roadmap amendment. No Product, Domain or Architecture semantic amendment is justified by this seam.

---

### ANL-PT-008 — Is changing only §3A and FP-006 Affected Domains sufficient?

**Question:** Can the smallest correction touch only the future-gated table and FP-006 Affected Domains?

**Analysis:** No. That would leave the same Roadmap internally contradictory because §2 still says Research & Feedback is “Not MVP” and not automatically assigned to FP-006, while §3.3 still says the Domain remains future-gated until a later Roadmap decision assigns an activating outcome. Once this candidate is the activating decision, those summaries must acknowledge the bounded exception.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Minimum coherent semantic edit surface:**

1. successor amendment scope/header;
2. §2 mature-capability Research & Feedback row;
3. §3.3 Domain/Feature-Pack challenge row;
4. §3A future-gated rule + Research & Feedback row;
5. FP-006 Affected Domains + explicit bounded activation paragraph;
6. FP-006 Deferred From This FP scope fence.

No other Roadmap section currently requires semantic change for this activation.

---

### ANL-PT-009 — Does bounded FP-006 activation make general Research an MVP capability?

**Question:** Would activating Domain 19 for the mandatory FP-006 instrument implicitly pull campaigns, studies, arbitrary surveys or a generic Research product into MVP?

**Analysis:** It must not. The amendment must distinguish **one Product-Law-required controlled-pilot feedback instrument** from the broader mature Research capability. The owner participates because the required durable meaning belongs there, not because a general survey system is now an MVP goal.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Required fence:** broader Research campaigns/studies, arbitrary instruments, general survey-builder capability and unrelated feedback modes remain future-gated / Feature-Pack-unassigned.

---

### ANL-PT-010 — Is a new Research Feature Pack required?

**Question:** Does Domain 19 participation require a new Feature Pack?

**Analysis:** No. Roadmap doctrine explicitly rejects Feature Packs per Domain. The concrete outcome already exists in FP-006; adding a new pack would split one paid-pilot evidence outcome and add sequencing overhead without a new independent Product outcome.

**Disposition:** `CONFLICT` for creating a new Feature Pack.

**Working conclusion:** Research & Feedback participates in existing `FP-006` only for the bounded mode.

---

### ANL-PT-011 — Should this amendment invent a new OQ, dossier mandate or proof classification?

**Question:** Must Roadmap now define a new gate identifier, force a full Research dossier or choose proof/resource/provider detail?

**Analysis:** No. The amendment should sequence the Domain and state the boundary. Normal FP-006 Phase 7 gate-manifest/JIT adjudication must decide the minimum dossier/gate/proof work required by the activated mode. Inventing those details in this Pre-JIT pass would bypass the governed workflow.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Working conclusion:** do not invent a new OQ or implementation contract here. The eventual FP-006 Phase 7 process owns that adjudication.

---

### ANL-PT-012 — Is “Roadmap-only amendment” sufficient as a promotion description?

**Question:** If the candidate is later adopted, can only the Roadmap file change?

**Analysis:** Semantically, yes: the authority correction belongs only to Roadmap. Operationally, no: a promoted Roadmap successor must also be routed as current authority through the normal README/manifest mechanism and reflected in the then-current programme status bookkeeping as required. Those are routing/status consequences, not new Product or Domain semantics.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Working conclusion:** distinguish **semantic authority target = Roadmap only** from **promotion collateral = normal authority routing/status updates**.

---

## 4. ANL-UPD-001 candidate amendment shape

### 4.1 SemVer recommendation if promoted

Because this is a semantic Roadmap sequencing change rather than a routing-only patch, the candidate should be treated as a **minor Roadmap successor** (expected shape: `v1.2.0 → v1.3.0`) if governance accepts it. This pass does not create or promote that authority file.

### 4.2 Required semantic edits

The candidate must do all of the following together:

1. state that the successor explicitly activates one bounded FP-006 Research & Feedback mode required by existing Product Law;
2. preserve all 17 Feature Pack identifiers and create no Research Feature Pack;
3. revise the §2 Research & Feedback summary so “Not MVP” applies to broader Research capability, not the mandatory bounded FP-006 instrument;
4. revise §3.3 so the “later governed Roadmap decision” requirement is recorded as satisfied only for this bounded mode;
5. revise §3A so Research & Feedback remains generally future-gated but has an explicit bounded FP-006 exception;
6. add `Research & Feedback` to FP-006 Affected Domains;
7. add an FP-006 activation boundary stating:
   - instrument/question version + participant response are Research & Feedback truth;
   - Analytics owns derived response-rate/value distributions/release measurement only;
   - FP-005 basic participant progress/usefulness feedback remains HJP truth when that purpose fits;
   - broader Research remains out of scope;
   - exact identity/uniqueness/correction/withdrawal/privacy/retention/provider/JIT detail remains downstream;
8. extend FP-006 `Deferred From This FP` to explicitly defer broader Research campaigns/studies/general survey capability beyond the mandatory instrument.

### 4.3 Explicit non-edits

The candidate must **not**:

- alter Product Law survey thresholds or question wording;
- alter Domain ownership;
- change FP-005 basic-feedback classification;
- activate Voting & Balloting;
- activate FP-016 experimentation;
- create a generic survey-builder, Research administration product or cross-domain evidence store;
- select anonymous versus Account-linked response mode;
- define retention/deletion periods;
- choose provider, table/Resource, schema, event names or implementation mechanism;
- classify Architectural Proof or start implementation.

---

## 5. Candidate internal-consistency result

The smallest safe amendment is **not** a one-line FP-006 domain addition. It is a tightly bounded Roadmap consistency amendment across the six semantic locations listed in `ANL-PT-008`.

That is still the smallest safe upstream repair because every changed statement already speaks directly to Research activation/sequencing; no unrelated Feature Pack or authority area needs modification.

`ANL-GAP-001` remains real until an authority successor is explicitly reviewed and promoted.

`ANL-UPD-001` status after this pass:

```text
CANDIDATE_DRAFTED
UPSTREAM_ACTION_REQUIRED
NOT AUTHORITY
NOT IMPLEMENTATION AUTHORISATION
```

---

## 6. Pass 4 disposition

**PASS — ROADMAP DELTA CANDIDATE PRESSURE-TESTED; UPSTREAM ACTION STILL REQUIRED.**

The candidate can resolve the Pass-3 contradiction without changing Product Law, Domain Law or Architecture and without activating general Research capability. The key refinement is that internal Roadmap summaries must change together; editing only §3A and FP-006 would be incomplete.

No authority document was modified in this pass. No JIT dossier, metric formula, provider selection or implementation is authorised.

**Recommended next step after human acceptance of this pass:** treat the exact Roadmap delta candidate as approved working intent, then decide whether to perform the governed upstream Roadmap amendment/promotion now or leave `ANL-UPD-001` explicitly blocked while continuing only Analytics work that does not depend on the survey instrument.