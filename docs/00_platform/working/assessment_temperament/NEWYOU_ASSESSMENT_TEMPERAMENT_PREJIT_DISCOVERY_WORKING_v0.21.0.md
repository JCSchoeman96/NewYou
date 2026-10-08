# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.21.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.20.0`. Read those predecessors first for `AT-WD-001...019`, the final adversarial sweep, and accepted upstream/cross-domain correction contracts `AT-UPD-001`, `AT-UPD-002`, `AT-UPD-004`, and `AT-UPD-005`.
>
> Nothing in this file itself amends Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.21.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.20.0.md`
- **Predecessor blob SHA:** `20f78d10b6a4ce70cded97e3593a5e2bff92cc73`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Live canonical `main` revalidation pin:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `UPSTREAM RECONCILIATION — AT-UPD-001/002/004/005/006 ACCEPTED; AT-UPD-007 NEXT`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `CHANGES REQUIRED UPSTREAM / NOT ELIGIBLE FOR PARK`

---

# 1. Accepted cross-domain correction contract

## AT-UPD-006 — Cross-domain identity reconciliation

**Accepted working correction direction:** `2026-10-08`

Identity & Access alone establishes authoritative duplicate-account reconciliation and the canonical surviving participant/account identity. That reconciliation does not itself rewrite or merge another Domain's durable business truth.

Each affected owner applies an explicit, idempotent owner-mediated reconciliation consequence under its own invariants.

### AT-UPD-006A — Identity establishes sameness, not foreign business truth

Identity & Access owns:

- authoritative duplicate-account reconciliation;
- canonical survivor/predecessor account relationship;
- PMR merge-survivor semantics;
- the authoritative reconciliation boundary/evidence.

Identity does **not** thereby:

- merge Temperament answers;
- choose a current Temperament profile;
- sum Entitlements;
- manufacture or restore an assessment right;
- decide Privacy deletion/retention scope;
- rewrite another Domain's historical evidence.

### AT-UPD-006B — Owner-mediated, idempotent convergence

After Identity commits the reconciliation, each affected owner must apply its own reconciliation consequence idempotently.

The system must preserve sufficient reconciliation identity/version and original provenance so duplicate/retried delivery converges rather than duplicating history, rights, reports, current-profile transitions or other durable consequences.

Correctness-sensitive actions that could violate owning-Domain invariants must fail closed until the required owner reconciliation has converged.

### AT-UPD-006C — Preserve original producing-account provenance

Canonical ownership may converge to the reconciled participant, but historical origin must not be falsified.

Temperament history must retain sufficient evidence to establish which predecessor identity/account context originally produced an attempt, declaration, result, selection or report and that Identity later reconciled the accounts.

Exact storage design remains JIT work.

### AT-UPD-006D — Temperament active-attempt collision

If exactly one predecessor has an active valid Assessment Attempt, that same attempt may continue under the reconciled participant without creating another attempt, resetting its deadline, changing its pinned methodology context or consuming another entitlement.

If reconciliation yields more than one active attempt:

- attempts and answers remain historically distinct;
- answers must never be merged across attempts;
- ordinary writes/finalisation fail closed until an explicit Temperament-owned reconciliation disposition leaves at most one active attempt or otherwise lawfully closes/remediates the collision;
- reconciliation itself does not manufacture a new assessment right.

### AT-UPD-006E — Completed history remains history

Otherwise-valid completed declarations, assessment results, reports and their provenance survive reconciliation.

Duplicate-account discovery alone is not proof that a completed result is fraudulent, invalid, defective or unauthorised. Separate evidence and the appropriate owning authority are required for any such disposition.

Future assessment eligibility must evaluate the participant's reconciled legitimate qualifying history rather than treating predecessor accounts as permanently independent people.

### AT-UPD-006F — Current-profile conflicts require participant confirmation

Where predecessor histories contain conflicting effective current-profile selections, reconciliation must not silently choose:

- the surviving account's selection;
- the latest database timestamp;
- a digital source over a declared source;
- any other inferred winner.

Preserve the historical selections, suspend effective current Temperament selection where needed, and require the participant to explicitly select one currently eligible source before Temperament-based current personalisation resumes.

### AT-UPD-006G — Entitlements reconciles commercial rights

Entitlements remains authoritative for assessment credits, access grants, Premium reassessment rights and other commercial access truth.

Duplicate-account reconciliation must not blindly add predecessor balances. Entitlements must reconcile underlying right identity, provenance, validity, consumption, revocation/refund state and scope, then expose the canonical current rights state.

Temperament consumes the resulting Entitlements truth; it does not calculate merged commercial balances.

### AT-UPD-006H — Purchaser remains distinct from participant

Payment/purchaser provenance does not transfer participant-private assessment ownership.

Identity reconciliation may not turn a purchaser into the owner of a recipient's private Temperament result/report merely because the purchaser funded the assessment or shares commercial evidence.

### AT-UPD-006I — Privacy state survives reconciliation

Identity establishes canonical sameness; Privacy & Consent determines deletion/retention consequences across the reconciled identity state.

Reconciliation may not:

- silently cancel or discard an existing privacy lifecycle;
- expose data merely because accounts were merged while privacy scope remains unresolved;
- resurrect data already irreversibly deleted/anonymised;
- reconstruct completed-deletion assessment history.

### AT-UPD-006J — Race/cutover semantics

Authoritative writes racing reconciliation must resolve current server-side identity and owning-Domain state.

A business write that authoritatively committed before the Identity reconciliation boundary remains historical and is reconciled afterward. A stale non-survivor action occurring after reconciliation must resolve through the canonical identity state and fail closed where required owner reconciliation is incomplete.

### AT-UPD-006K — Repairability

If Identity later corrects an erroneous reconciliation, each owning Domain must use preserved origin/reconciliation provenance to repair current associations without rewriting historical business meaning.

Irreversibly deleted data must not be reconstructed during repair.

---

# 2. Pressure tests

## AT-PT-202 — Same participant changes email

**Scenario:** participant changes verified primary email within the same canonical Account.

**Expected:** ordinary identity continuity; no duplicate-account business reconciliation and no Temperament recreation.

**Result:** `PASS` under existing Identity ownership + AT-UPD-006.

## AT-PT-203 — Suspected but unproven duplicate

**Scenario:** two Accounts look related but Identity has not authoritatively reconciled them.

**Expected:** no cross-account history exposure, merge or entitlement reconciliation.

**Result:** `PASS` under AT-UPD-006A.

## AT-PT-204 — One active attempt across verified duplicates

**Scenario:** Account A has one active attempt; Account B has none; Identity reconciles them.

**Expected:** the same attempt continues under the canonical participant with the same pinned context, answers, deadline and consumption history.

**Result:** `PASS` under AT-UPD-006D.

## AT-PT-205 — Two active attempts collide

**Scenario:** A and B each have an active assessment when reconciliation becomes authoritative.

**Expected:** preserve both histories; merge no answers; block ordinary conflicting progress until explicit Temperament disposition leaves at most one active attempt.

**Result:** `PASS` under AT-UPD-006D.

## AT-PT-206 — Two completed results

**Scenario:** A has R1 and B has R2.

**Expected:** preserve both otherwise-valid results; duplicate-account discovery does not invalidate either one by itself.

**Result:** `PASS` under AT-UPD-006E.

## AT-PT-207 — Conflicting current selections

**Scenario:** A current source is declared Yellow; B current source is digital Blue.

**Expected:** preserve historical selections; no silent winner; participant explicitly confirms one eligible current source before Temperament current personalisation resumes.

**Result:** `PASS` under AT-UPD-006F.

## AT-PT-208 — Two apparent unused credits

**Scenario:** both predecessors project one unused assessment right.

**Expected:** Entitlements reconciles right provenance/identity; Temperament does not sum balances.

**Result:** `PASS` under AT-UPD-006G.

## AT-PT-209 — Gift purchaser and recipient

**Scenario:** purchaser paid for a recipient's assessment and later appears in an Identity reconciliation/support case.

**Expected:** purchaser provenance does not transfer access to recipient-private Temperament history.

**Result:** `PASS` under AT-UPD-006H.

## AT-PT-210 — Privacy lifecycle on one predecessor

**Scenario:** one reconciled predecessor has a pending/full-deletion lifecycle.

**Expected:** Identity does not erase, override or broaden Privacy truth; Privacy & Consent resolves scope and completed deletion is not resurrected.

**Result:** `PASS` under AT-UPD-006I.

## AT-PT-211 — Stale non-survivor browser writes after merge

**Scenario:** a stale browser authenticated under the retired predecessor tries to save/finalise after reconciliation.

**Expected:** authoritative action re-resolves current server-side identity/owner state and fails closed where reconciliation is incomplete; stale client identity cannot preserve a competing participant authority.

**Result:** `PASS` under AT-UPD-006J.

## AT-PT-212 — Duplicate reconciliation consequence

**Scenario:** the same reconciliation consequence is retried/replayed.

**Expected:** owner state converges idempotently; no duplicate history, rights, reports or current-profile transitions.

**Result:** `PASS` under AT-UPD-006B.

## AT-PT-213 — Identity merge later corrected

**Scenario:** Identity authority later determines the reconciliation was erroneous.

**Expected:** preserved origin/reconciliation provenance supports owner-mediated repair; historical Temperament content is not rewritten and deleted data is not reconstructed.

**Result:** `PASS` under AT-UPD-006K.

---

# 3. Authority classification

`AT-UPD-006` is classified as:

**CROSS-DOMAIN DOMAIN/JIT CONTRACT FORMALISATION REQUIRED**

It is not a new Product capability. Current Product/Domain authority already establishes one active attempt, participant-controlled current-profile selection, immutable history, purchaser/recipient separation, Identity merge authority and one owner per durable truth.

The missing requirement is explicit owner-mediated composition after an authoritative Identity reconciliation.

---

# 4. Status after this acceptance

Accepted mandatory correction/formalisation contracts now recorded:

- `AT-UPD-001` assessment-credit consumption authority;
- `AT-UPD-002` methodology-authority Domain wording;
- `AT-UPD-004` result correction/invalidation/supersession Product semantics;
- `AT-UPD-005` FP-003 / OQ-017 reminder routing;
- `AT-UPD-006` cross-domain identity reconciliation.

Still requiring mandatory upstream correction before final revalidation:

- `AT-UPD-007` ordinary annual reassessment interval anchor and Premium interaction.

`AT-UPD-003` remains conditional and must be formalised before any subscription offer claiming one included successfully completed initial digital assessment is activated.

**Next:** resolve `AT-UPD-007`.

**Final Pre-JIT disposition remains:** `CHANGES REQUIRED UPSTREAM / DO NOT PARK`.
