# NewYou Assessment / Temperament Upstream Delta Register — Working v0.1.0

> **NON-AUTHORITATIVE WORKING DELTA REGISTER**
>
> This file routes unresolved Assessment / Temperament findings to the correct authority/JIT/proof stage. It does not predetermine the governed answer.

- **Pack version:** `v0.1.0`
- **Source discovery:** `deep/NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.23.1.md`
- **Source blob:** `41da4e92f6bf61f73979303d394a9865d6d0158d`
- **Independent review:** `PASS WITH NON-BLOCKING CORRECTIONS`
- **Tracking issue:** GitHub Issue #89
- **Implementation:** NOT AUTHORISED

## 1. AT-UPD-001 — assessment-right consumption semantics

**Classification:** `PRODUCT_AUTHORITY_GAP / ENTITLEMENT_SEAM_GAP`

### Why this remains open

Current authority contains competing commercial signals:

- generic assessment-use / attempt-start wording points toward first-answer consumption;
- included assessment-credit Product/Roadmap wording points toward successful digital assessment delivery.

The working discovery originally selected a universal first-durably-accepted-scored-answer event. The independent review correctly reclassified that as a **candidate**, not current law.

### Required governed adjudication

Product must explicitly define the authoritative consumption/fulfilment event by applicable right type, including as relevant:

- ordinary standalone assessment right;
- included plan/bundle assessment credit;
- Premium annual reassessment right;
- technical/methodology remediation or replacement right.

### Invariants regardless of Product choice

- Entitlements owns commercial right identity/validity/consumption/revocation/reconciliation.
- Temperament owns attempt/result/report lifecycle facts.
- Retry/crash recovery must not double-consume or resurrect a right.
- Pre-attempt failure, post-attempt technical failure, canonical-result existence, report failure and refund/remedy must remain distinguishable.
- JIT may not solve the authority gap with an idempotency mechanism alone.

### Blocking stage

Product adjudication is required before affected FP-003 Phase 7C semantics can freeze.

---

## 2. AT-UPD-002 — methodology-authority Domain wording

**Classification:** `DOMAIN_OWNERSHIP_CORRECTION REQUIRED`

### Defect

Current Domain wording still associates Four-Colour methodology authority with Venessa / Super Admin status, while current `DEC-309` establishes that methodology authority comes from the governing IP agreement and scoped delegation; Super Admin alone is not methodology authority.

### Smallest safe correction

- Keep Temperament as owner of approved methodology representation/version lifecycle.
- Replace fixed-role authority wording with the governing IP agreement/delegation model.
- Preserve the distinction between methodology approval, rights, administrative publication, Product application and Health/Clinical safety authority.

### Blocking stage

Domain-law correction before FP-003 relies on the stale wording.

---

## 3. AT-UPD-003 — subscription promise of one successfully completed initial digital assessment

**Classification:** `FUTURE_ONLY`

Current authority does not presently guarantee one successfully completed initial digital assessment as a membership/subscription promise.

If Product later creates that promise, it must govern fulfilment/replacement semantics before implementation. The discovery's replacement-after-incomplete-expiry model remains future design input only.

**Current FP-003 blocker:** NO, unless the offer scope changes.

---

## 4. AT-UPD-004 — defective-result correction / invalidation / supersession

**Classification:** `PRODUCT_AUTHORITY_GAP`

### Already governed

- submitted answers / original calculated result / producing version remain immutable while retained;
- Reviewed Interpretation is a separate audited path rather than raw-score mutation.

### Still unresolved Product consequences

Product must decide the minimum required semantics for:

- proven platform computation defects;
- corrective-result successors, if permitted;
- material methodology invalidation/remediation;
- historical preservation versus active-use eligibility;
- current-profile consequences;
- report succession;
- participant notification/remediation;
- owner-mediated consequences for durable downstream outputs derived from a defective source result.

`AT-WD-012` is the parked candidate model, not current law.

### Blocking stage

Product promotion before FP-003 Phase 7C includes a governed defective-result path.

---

## 5. AT-UPD-005 — FP-003 / OQ-017 assessment expiry-warning routing

**Classification:** `ROADMAP / DOCUMENTARY ROUTING CORRECTION`

DEC-056 already requires advance warning before an unfinished 30-day Assessment Attempt expires. OQ-017 governs reminder-delivery design, but current routing points only to later reminder-heavy packs.

### Smallest safe correction

Add FP-003 as the earliest relevant OQ-017 consumer **only for the bounded assessment-expiry-warning obligation**.

Do not pull generic programme, habit, membership, challenge or campaign reminder scope into FP-003.

Ownership remains:

- Temperament — attempt status/deadline/applicability;
- Communications — schedule/channel/retry/quiet-hours/deduplication/observability/delivery evidence.

Exact reminder cadence remains downstream configuration.

---

## 6. AT-UPD-006 — cross-domain identity reconciliation

**Classification:** `FP-003 / IDENTITY / ENTITLEMENTS JIT + PHASE-8 PROOF PRIMARY`

The earlier working stream over-classified this as a likely upstream Product correction. Current ownership already gives:

- Identity & Access — authoritative duplicate-account reconciliation;
- Temperament — assessment truth;
- Entitlements — commercial-right truth;
- Privacy & Consent — deletion/retention truth.

### Normal JIT contract still required

- authoritative reconciliation input/version;
- original producing-account provenance;
- idempotent owner-specific replay/convergence;
- two active attempts never merge answers;
- conflicting active attempts fail closed until Temperament resolves them;
- conflicting current-profile selections do not silently choose a winner;
- Entitlements reconciles underlying rights rather than summing balances;
- purchaser/recipient separation survives reconciliation;
- Privacy scope/deletion cannot be dropped or bypassed;
- completed deletion cannot be resurrected;
- sufficient retained provenance supports repair if Identity later corrects an erroneous reconciliation.

### Product escalation rule

Escalate upstream only if JIT exposes a participant-facing policy choice that current authority genuinely cannot answer.

---

## 7. AT-UPD-007 — authoritative annual reassessment timing

**Classification:** `PRODUCT_AUTHORITY_GAP`

### Why this remains open

Current law says no more than one assessment retake per year with a valid entitlement and separately recognises assessment completion, annual-use interval, purchase eligibility and Premium credit, but it does not fully define the temporal anchor/semantics.

### Parked candidate

`AT-WD-020` proposes a rolling dual guard:

1. at least 12 calendar months after the latest qualifying valid digital completion; and
2. at least 12 calendar months after the latest ordinary reassessment start/first-answer commitment, where one exists.

This closes the repeated-abandoned-retake loophole, but it is **not current Product Law** merely because it is coherent.

### Required governed adjudication

Product must explicitly select, refine or supersede the annual timing rule and reconcile it with:

- valid-entitlement gating;
- Premium annual entitlement;
- abandoned/expired attempts;
- same-assessment correction;
- technical/methodology remediation.

FP-003 JIT must not implement the dual-clock candidate automatically.

---

## 8. Existing external gates — not new AT-UPD items

The compacting exercise does not convert existing governed gates into new Pre-JIT defects. They remain independently binding at their current scopes, including:

- governing IP/methodology rights (`DEC-016` / `DEC-309` as applicable);
- approved proprietary questions/options/scoring/tie/mask/interpretation package;
- methodology-sensitive language equivalence / `OQ-013` routing;
- release retention/deletion categories under `OQ-009` / `OQ-029`;
- optional score-distance/dominance thresholds under `OQ-006` only if activated.

## 9. Required sequencing

The normal sequence remains:

1. adjudicate/promote the Product/Domain/Roadmap items at the correct authority layer;
2. revalidate against then-current canonical `main`;
3. perform FP-003 Phase 7A Skeleton + Gate Manifest;
4. complete required/conditional Phase 7B JIT Domain Dossiers;
5. resolve required gates;
6. produce the Phase 7C Final Feature Pack Contract;
7. classify proof explicitly;
8. enter implementation only after the normal Development Entry Hard Stop.

No downstream artifact may silently absorb a different answer to one of these deltas without explicit review.