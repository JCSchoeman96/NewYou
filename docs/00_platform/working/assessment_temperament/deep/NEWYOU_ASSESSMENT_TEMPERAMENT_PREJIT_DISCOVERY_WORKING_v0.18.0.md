# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.18.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.17.0`. Read those predecessors first for `AT-WD-001...019`, the final adversarial sweep, the upstream-delta register, and the accepted `AT-UPD-001` assessment-credit consumption correction contract.
>
> Nothing in this file itself amends Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.18.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.17.0.md`
- **Predecessor blob SHA:** `b6e7a2dbeb6e93d4811bc2ee0e7075f2cb2b1515`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Live canonical `main` revalidation pin:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `UPSTREAM RECONCILIATION — AT-UPD-001/002 ACCEPTED; AT-UPD-004 NEXT`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `CHANGES REQUIRED UPSTREAM / NOT ELIGIBLE FOR PARK`

---

# 1. Accepted upstream correction contract

## AT-UPD-002 — Align Temperament methodology-authority wording to DEC-309

**Accepted working correction direction:** `2026-10-08`

Temperament remains the authoritative Domain owner for platform representation and lifecycle of approved Four-Colour methodology versions, scoring configuration, assessment attempts/results and participant-selected current temperament profile. No Domain ownership move is required.

The stale detailed Domain policy that restricts methodology authority to `Venessa/Super Admin under IP agreement` must be replaced with the current Product-law authority model:

> **Methodology authority is established by current Product Law, DEC-309 and the governing IP agreement. A platform role does not itself create methodology authority.**

Material Four-Colour methodology changes therefore require Lynette Beer or another authority explicitly delegated by the governing IP agreement, within that delegation's scope. Super Admin, Content, Support, clinical, developer or other technical/operational roles do not independently confer methodology authority.

### AT-UPD-002A — Ownership versus approval authority

Temperament owns durable methodology representation and lifecycle state. It does not originate substantive methodology authority.

The owning Domain may record and publish an approved methodology version only after the required authority, rights and approval evidence exists. Administrative publication executes an already-authorised decision; publication does not create methodology approval.

### AT-UPD-002B — Product-law basis hygiene

The Temperament Domain profile must explicitly reflect current DEC-309 authority and must not rely on historical DEC-051's former fixed-role assignment as the current approval rule.

DEC-051 remains historical evidence where required, but DEC-309 governs current methodology-authority meaning.

### AT-UPD-002C — Approved-state integrity

An `approved` or equivalent methodology lifecycle state cannot manufacture authority merely because an administrator can write that state.

The state is valid only when backed by the required methodology-authority and rights evidence. Exact evidence representation, signatures, workflows and storage remain downstream JIT/governance design.

### AT-UPD-002D — Authority dimensions remain separate

Methodology authority, Product application authority, Content/translation publication authority, Health/Clinical authority and technical/administrative capability remain distinct.

Consequences:

- valid methodology approval does not bypass missing commercial/digital/translation rights;
- Health/Clinical may block or require correction of unsafe health/safety-sensitive content without thereby acquiring Four-Colour scoring authority;
- Product may version permitted low-risk behavioural application rules without methodology approval where DEC-309 allows, provided methodology itself is not redefined;
- Content/language approval does not authorise scoring changes;
- technical access does not grant methodology authority.

### AT-UPD-002E — Delegation provenance

Published methodology versions must retain enough immutable provenance to establish which authority approved the version, the authority basis/delegation scope applicable at the time, and the rights basis under which production use was allowed.

Later changes to delegates or platform roles do not rewrite historical approval provenance.

---

# 2. Domain Law correction target

The future authoritative Domain Map successor should preserve the existing Temperament purpose/ownership while correcting the detailed policy approximately as follows:

> **Key methodology-authority policy:** Temperament owns the platform representation and lifecycle of approved methodology versions. Approval or material alteration authority is determined by DEC-309 and the governing IP agreement; platform roles, including Super Admin, do not independently confer methodology authority. Only methodology versions backed by valid authority/rights evidence may enter approved/publishable production states.

`publish approved methodology versions` remains a valid Domain capability, but **approved** must mean approved by the governing authority rather than merely flagged by an operator.

No new Domain, generic approval Domain, workflow engine or methodology service is justified by this correction.

---

# 3. Pressure tests

## AT-PT-197 — Super Admin changes scoring without methodology delegation

**Scenario:** Super Admin has technical access and attempts to approve changed weights/questions without authority delegated under the governing IP agreement.

**Expected:** reject as methodology approval. Technical/admin capability does not create substantive methodology authority.

**Result:** `PASS` under AT-UPD-002.

## AT-PT-198 — Valid methodology authority approves, operator publishes

**Scenario:** valid methodology authority approves M2 within rights scope; an authorised platform operator performs publication.

**Expected:** allow publication subject to all other Product/content/health/language gates. Operator publication is not the source of methodology authority.

**Result:** `PASS`.

## AT-PT-199 — Methodology approval exists but production rights do not

**Scenario:** authorised methodology approver signs off M2, but the governing agreement does not grant required digital/commercial use rights.

**Expected:** production encoding/publication remains blocked. Methodology approval and use rights are independent gates.

**Result:** `PASS` under DEC-309 + AT-WD-019.

## AT-PT-200 — Clinical reviewer rejects unsafe report claim

**Scenario:** methodology is valid, but Health/Clinical authority rejects an unsafe health-pattern claim in participant-facing report content.

**Expected:** affected publication fails closed/requires correction. Clinical authority does not thereby rewrite Four-Colour scoring methodology.

**Result:** `PASS`.

## AT-PT-201 — Delegated methodology authority changes later

**Scenario:** M1 was validly approved by delegate D1; later the governing agreement delegates future approvals to D2.

**Expected:** M1 retains immutable historical approval provenance to D1. New M2 approval follows the current valid authority chain. No retroactive rewriting.

**Result:** `PASS`.

## AT-PT-202 — Administrator flips approved flag without evidence

**Scenario:** an operator directly sets a methodology version's lifecycle state to approved without valid approval/rights evidence.

**Expected:** the state transition is invalid/fails closed; a writable field cannot manufacture substantive authority.

**Result:** `PASS`.

## AT-PT-203 — Low-risk Product application changes

**Scenario:** Product changes a permitted low-risk temperament-informed presentation rule without altering questions, scoring, classification or methodology meaning.

**Expected:** follow Product application authority rather than unnecessarily treating every application rule as a methodology successor, provided DEC-309 and safety limits are respected.

**Result:** `PASS`.

## AT-PT-204 — Methodology approver is also Super Admin

**Scenario:** a person has both valid methodology delegation and Super Admin role.

**Expected:** methodology approval is valid only by virtue of the governing delegation; removal of Super Admin alone would not remove methodology authority, and removal of methodology delegation would remove approval authority even if Super Admin remains.

**Result:** `PASS`.

---

# 4. Upstream reconciliation status

Accepted correction directions now recorded:

- `AT-UPD-001` — assessment-credit consumption authority;
- `AT-UPD-002` — methodology-authority Domain wording.

Still requiring accepted correction/formalisation before parking:

- `AT-UPD-004` — Product result correction/invalidation/supersession semantics;
- `AT-UPD-005` — FP-003 routing for OQ-017 reminder design;
- `AT-UPD-006` — cross-domain identity-reconciliation contract;
- `AT-UPD-007` — Product definition of the annual reassessment interval anchor.

`AT-UPD-003` remains conditional on activation of a subscription offer promising one successfully completed included initial digital assessment.

**Current disposition:** `CHANGES REQUIRED UPSTREAM / DO NOT PARK.`
