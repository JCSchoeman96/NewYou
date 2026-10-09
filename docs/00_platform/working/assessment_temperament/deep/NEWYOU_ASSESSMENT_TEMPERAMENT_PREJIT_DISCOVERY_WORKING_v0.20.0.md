# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.20.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.19.0`. Read those predecessors first for `AT-WD-001...019`, the final adversarial sweep, and accepted upstream correction contracts `AT-UPD-001`, `AT-UPD-002`, and `AT-UPD-004`.
>
> Nothing in this file itself amends Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.20.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.19.0.md`
- **Predecessor blob SHA:** `43922c71d53c2a8ee781f3bebf27514542b74592`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Live canonical `main` revalidation pin:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `UPSTREAM RECONCILIATION — AT-UPD-001/002/004/005 ACCEPTED; AT-UPD-006 NEXT`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `CHANGES REQUIRED UPSTREAM / NOT ELIGIBLE FOR PARK`

---

# 1. Accepted upstream correction contract

## AT-UPD-005 — Assessment-expiry reminder gate routing

**Accepted working correction direction:** `2026-10-08`

Roadmap `OQ-017` must include `FP-003` as its earliest protected consumer because current Product Law already requires advance warning before a 30-day unfinished Assessment Attempt expires.

The correction is a routing change, not a new Product rule and not permission to pull the mature reminder system into FP-003.

### AT-UPD-005A — Earliest protected use

Roadmap routing must recognise:

- `FP-003` requires the bounded assessment-expiry warning path;
- later reminder-heavy Feature Packs may reuse/extend the same Communications capability under their own contracts;
- OQ-017 must therefore be resolved to the depth necessary for FP-003 before FP-003 activates scheduled expiry-warning behaviour.

### AT-UPD-005B — Scope boundary

FP-003 resolves only what its Product outcome requires:

- assessment reminder scheduling;
- governed delivery channel(s);
- retries;
- deduplication;
- quiet-hour handling;
- observability;
- relevant rate limiting;
- suppression when the owning assessment truth says the reminder is no longer applicable.

This does **not** pull forward programme reminders, habit nudges, challenge notifications, membership campaigns, broad notification-preference systems, or unrelated scheduled-notification capability merely because later packs may reuse the same Communications mechanism.

### AT-UPD-005C — Ownership boundary

Temperament remains authoritative for:

- attempt start;
- fixed expiry deadline;
- current attempt state;
- authoritative submission/completion;
- whether an assessment-warning obligation remains applicable.

Communications remains authoritative for:

- scheduled delivery intent;
- channel/delivery execution;
- retry state;
- deduplication;
- quiet-hour handling;
- delivery/observability evidence.

Communications may not independently redefine assessment expiry or completion truth.

### AT-UPD-005D — Delivery outcome does not move expiry

Reminder delivery, bounce, open/read status, provider failure or participant engagement does not alter the fixed 30-day Temperament expiry boundary.

Material platform failure to establish required warning obligations may remain evidence in separately governed technical-recovery adjudication; it does not automatically extend the attempt or restore an entitlement.

### AT-UPD-005E — Launch cadence remains downstream configuration

The accepted `AT-WD-009` launch cadence remains FP-003/JIT/Communications configuration rather than Product Law:

1. start confirmation at first durable scored answer;
2. 14 days remaining;
3. 7 days;
4. 3 days;
5. 24 hours;
6. expiry outcome;
7. persistent in-app status/Continue path;
8. email as required proactive launch channel.

Product Law need only preserve the fixed 30-day expiry and advance-warning obligation unless Product authority intentionally standardises a more specific cadence later.

---

# 2. Pressure tests

## AT-PT-197 — FP-003 exists before programme reminder packs

**Scenario:** FP-003 is being contracted before any programme/habit/challenge reminder pack.

**Expected:** OQ-017 is still relevant because assessment expiry warning is already mandatory.

**Result:** `PASS` under AT-UPD-005.

## AT-PT-198 — Reminder races accepted final submission

**Scenario:** warning job wakes while authoritative final submission succeeds concurrently.

**Expected:** Communications rechecks Temperament owner truth and suppresses the stale unfinished-attempt reminder.

**Result:** `PASS` under AT-WD-007/009 + AT-UPD-005C.

## AT-PT-199 — 24-hour warning lands in quiet hours

**Scenario:** nominal warning time falls inside a governed quiet-hours interval.

**Expected:** Communications uses the resolved OQ-017 scheduling contract to move the delivery within the allowed warning window without changing assessment expiry.

**Result:** `PASS / MECHANISM DEFERRED` under AT-UPD-005.

## AT-PT-200 — Provider bounce or unopened message

**Scenario:** required warning is sent but bounces or is never opened.

**Expected:** preserve delivery evidence; fixed assessment expiry is unchanged.

**Result:** `PASS` under AT-UPD-005D.

## AT-PT-201 — Generic reminder expansion attempted inside FP-003

**Scenario:** implementation proposes programme, membership or challenge reminder framework merely because FP-003 needs expiry warning.

**Expected:** reject as unnecessary scope expansion; resolve only the bounded assessment path and legitimate reusable seam.

**Result:** `PASS` under AT-UPD-005B.

---

# 3. Status after this acceptance

Accepted upstream correction contracts now recorded:

- `AT-UPD-001` assessment-credit consumption authority;
- `AT-UPD-002` methodology-authority Domain wording;
- `AT-UPD-004` result correction/invalidation/supersession Product semantics;
- `AT-UPD-005` FP-003 / OQ-017 reminder routing.

Still requiring upstream/cross-domain reconciliation before parking:

- `AT-UPD-006` cross-domain identity reconciliation;
- `AT-UPD-007` ordinary annual reassessment interval anchor.

`AT-UPD-003` remains conditional and must be formalised before any subscription offer claiming one included successfully completed initial digital assessment is activated.

**Next:** pressure-test and resolve `AT-UPD-006`.

**Final Pre-JIT disposition remains:** `CHANGES REQUIRED UPSTREAM / DO NOT PARK`.
