# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.12.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.11.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification, replacement/retake, execution-provenance, result-correction, profile-source, reassessment and report-lifecycle semantics. This file appends the accepted participant identity-continuity / reconciliation contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.12.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.11.0.md`
- **Predecessor blob SHA:** `09c3497c535b0f1f4f2b5d508cfa88084d04446c`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-016 — Participant identity continuity and authoritative reconciliation

**Accepted:** `2026-10-08`

Assessment attempts, declarations, immutable digital results, current-profile history and report ownership attach to the canonical participant identity established by Identity & Access, not to a transient login identifier, browser session, email string, purchaser identity or payment instrument.

Temperament consumes authoritative identity/reconciliation outcomes; it does not independently prove that two accounts belong to the same human.

### AT-WD-016A — Identifier or credential change preserves the same participant history

Verified email change, password recovery, authentication-provider change or other Identity & Access operation that preserves the same canonical participant must preserve access to the same Temperament history.

Temperament must not copy/recreate assessment rows merely because the participant's login identifier changes.

### AT-WD-016B — Suspected duplicate accounts fail closed until Identity & Access reconciles them

Names, payment instruments, IP/device signals, similar emails or support intuition are not sufficient Temperament authority to merge participant histories.

Cross-account consolidation may occur only after authoritative Identity & Access reconciliation. Candidate, uncertain or conflicted matches must not broaden access or ownership.

### AT-WD-016C — Reconciliation unifies participant ownership without falsifying historical origin

Where Identity & Access authoritatively establishes that Account A and Account B represent the same canonical participant, Temperament may make both legitimate histories available to the reconciled participant, but must preserve sufficient provenance to show which historical account/context originally produced each attempt, declaration, result, selection and report.

A reconciliation must not destructively rewrite history as though only one account ever existed.

### AT-WD-016D — Dual active attempts may not be merged or silently continued in parallel

If reconciled accounts each contain an active Assessment Attempt, reconciliation may not combine answers across attempts or allow both ordinary attempts to continue as though the one-active-attempt invariant did not exist.

Both attempts remain historically distinct. Further ordinary progress must fail closed until an explicit governed resolution leaves at most one attempt eligible to continue or lawfully closes them. Exact resolution UX/mechanics remain JIT work.

### AT-WD-016E — Completed histories from both reconciled accounts remain immutable

If reconciled accounts contain completed valid historical results, those results remain separate immutable history. Reconciliation does not delete, merge or rewrite results merely to make prior timing appear compliant.

Future reassessment eligibility must evaluate the reconciled participant's valid completion history as a whole. Absent separate invalidation, the most recent qualifying valid completion anchors the ordinary future rolling interval.

Duplicate-account discovery alone is not proof of fraud.

### AT-WD-016F — Conflicting current-profile selections require participant confirmation

If reconciled accounts each carry a different effective current-profile selection, the historical selections remain preserved, but the reconciled participant may not continue with two effective current profiles.

The platform must require participant selection/confirmation of one currently eligible source rather than silently choosing the newest, the digital result, or an arbitrary winner.

### AT-WD-016G — Entitlement reconciliation remains owned by Entitlements

Identity reconciliation must not cause Temperament to add together apparent assessment credits/rights.

Entitlements owns whether apparently separate rights are duplicate projections of one commercial fact, distinct legitimate purchases, subscription inclusion, Premium reassessment, consumed rights or revoked/invalid rights.

Temperament consumes only the reconciled entitlement truth needed to start/continue an assessment.

### AT-WD-016H — Purchaser identity never becomes recipient-result ownership

Where one person purchases or sponsors an assessment for another, purchaser/payment provenance does not grant access to the redeemed participant's private answers, results, profile or report.

Identity recovery/reconciliation may not transfer recipient-private assessment history to the purchaser merely because the purchaser funded the right.

### AT-WD-016I — Reconciliation must remain reversible/auditable enough for governed repair

If a previous identity reconciliation is later proven erroneous, historical origin/provenance must be sufficient to support governed repair without relying on destructive rewrites that erased where each business fact originated.

Exact Identity & Access reversal mechanics remain outside Temperament ownership.

### AT-WD-016J — Privacy/deletion consequences remain separately authoritative

Identity reconciliation does not override Privacy & Consent authority. It must not recreate lawfully deleted/anonymised Temperament data, broaden a deletion request from one unresolved account into another person's data, or preserve processing merely because a historical alias can be found.

Privacy/retention/legal-hold consequences are the next dedicated Pre-JIT pass.

---

# 2. Upstream / cross-domain contract addition

## AT-UPD-006 — Cross-domain identity-reconciliation contract required before FP-003 finalisation

**Status:** `REQUIRED BEFORE GOVERNED FP-003 CONTRACT COMPLETION`

Current authority establishes Identity & Access ownership of canonical participant identity and preserves purchaser/recipient separation, but FP-003/JIT still needs an explicit cross-domain reconciliation contract for Temperament consequences.

That contract must at minimum govern:

1. canonical participant reconciliation input from Identity & Access;
2. preservation of historical producing-account provenance;
3. dual-active-attempt resolution without answer merging;
4. conflicting current-profile selections;
5. reconciled completed-result history and reassessment timing;
6. Entitlements-owned right reconciliation;
7. purchaser/recipient privacy separation; and
8. interaction with deletion/retention and erroneous-reconciliation repair.

Temperament must not become an independent identity-matching authority.

---

# 3. Pressure-test additions — v0.12.0

## AT-PT-114 — Login email changes after report delivery

**Scenario:** participant changes verified login email after completing an assessment and receiving permanent report access.

**Expected:** same canonical participant retains the same attempts/results/reports. No copy/recreation or ownership transfer occurs.

**Result:** `PASS` under AT-WD-016A.

## AT-PT-115 — Password/account recovery

**Scenario:** legitimate participant completes governed account recovery after losing credentials.

**Expected:** recovery restores access to existing participant-owned Temperament history rather than creating duplicate result/report ownership.

**Result:** `PASS` under AT-WD-016A.

## AT-PT-116 — Suspected duplicate accounts without authoritative proof

**Scenario:** two accounts share a name/device/payment signal but Identity & Access has not authoritatively reconciled them.

**Expected:** no Temperament merge, no broadened report access and no combined current-profile/result history.

**Result:** `PASS` under AT-WD-016B.

## AT-PT-117 — Reconciled accounts each have one active attempt

**Scenario:** A and B are authoritatively reconciled as one participant while A1 and B1 are both active.

**Expected:** answers are never merged; two ordinary attempts may not continue in parallel; fail closed pending explicit resolution leaving at most one continuable attempt.

**Result:** `PASS` under AT-WD-016D.

## AT-PT-118 — Reconciled accounts contain historical R1 and R2

**Scenario:** A owns valid completed R1 and B owns valid completed R2 before authoritative reconciliation.

**Expected:** preserve R1 and R2 as distinct immutable history with original provenance. Future reassessment timing considers the reconciled completion history rather than deleting one result.

**Result:** `PASS` under AT-WD-016C/E.

## AT-PT-119 — Two reconciled results occurred inside 12 months

**Scenario:** duplicate accounts previously bypassed ordinary annual timing and each produced a valid result within 12 months.

**Expected:** preserve factual history; do not retroactively edit/invalidate merely to make timing appear compliant. Future ordinary interval uses the most recent qualifying valid completion absent separate authority. Fraud/security consequences require their own evidence/authority.

**Result:** `PASS` under AT-WD-016E + AT-WD-014.

## AT-PT-120 — Reconciled accounts have different current-profile selections

**Scenario:** A selected declared Yellow; B selected digital Blue.

**Expected:** preserve historical selections but require one participant confirmation among currently eligible sources; no silent digital/newest winner.

**Result:** `PASS` under AT-WD-016F + AT-WD-013.

## AT-PT-121 — Duplicate apparent unused assessment rights

**Scenario:** after reconciliation A and B each appear to expose an unused assessment right.

**Expected:** Temperament does not sum them. Entitlements reconciles commercial right identity/provenance/consumption and supplies the usable-right truth.

**Result:** `PASS` under AT-WD-016G.

## AT-PT-122 — Gift purchaser requests recipient report

**Scenario:** purchaser funded the assessment and asks for the redeemed participant's report after account recovery/reconciliation.

**Expected:** funding provenance does not grant participant-private assessment/report access. Recipient ownership remains distinct.

**Result:** `PASS` under AT-WD-016H.

## AT-PT-123 — Erroneous reconciliation later discovered

**Scenario:** A and B were previously reconciled but later authoritative evidence shows they are different humans.

**Expected:** historical producing-account provenance was not destroyed, allowing Identity & Access and owning Domains to perform governed repair. Temperament must not have irreversibly flattened origin.

**Result:** `PASS AS REQUIRED INVARIANT` under AT-WD-016C/I; exact reversal mechanics remain Identity & Access/JIT work.

---

# 4. Open-question queue after v0.12.0

The identity continuity/reconciliation cluster is now materially constrained by `AT-WD-016`, `AT-UPD-006` and `AT-PT-114...123`, subject to later Identity & Access/Entitlements JIT integration and privacy authority.

Next unresolved cluster:

- **Privacy / retention / deletion / legal hold:** reconcile immutable assessment evidence and permanent report access with data-minimisation, participant deletion, account closure, retention obligations, legal holds, anonymisation, analytics and non-resurrection requirements. Resolve OQ-009/OQ-029 dependencies without inventing the final retention matrix.

Later passes still include Research/Interactive isolation; Methodology Authority Input Contract; and final adversarial sweep.
