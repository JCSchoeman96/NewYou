# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.6.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.6.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 5 — Entitlement vs enrolment / access lifecycle
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.5.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused Entitlement / current-access / Enrolment seam pass while preserving v0.1.0 through v0.5.0 unchanged.

> This is an append-only semantic successor. Read v0.1.0 → v0.2.0 → v0.3.0 → v0.4.0 → v0.5.0 → this pass. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work or Commerce/Entitlements authority.

> Nuwe Jy remains the first concrete programme acceptance test. Do not solve entitlement/access seams by duplicating Commerce/Entitlements state inside Programmes or by importing generic LMS licensing/enrolment machinery.

---

# 42. Accepted working-lock status entering Pass 5

The user accepted Pass 4 after review.

Therefore Passes 1–4 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, deferred items and future explicit refinements.

Pass 5 inherits, without reopening:

- Programme is stable conceptual/catalogue identity;
- ProgrammeVersion is the version-pinned participant-semantic contract;
- Edition is a governed delivery configuration where required, not Commerce Product/Offer or Entitlement;
- Cohort is a shared participant delivery context, not Community/access authority;
- Enrolment is the durable participant-specific programme attempt/history;
- Entitlement is the Entitlements-owned durable access right;
- Access is a current authorisation result, not a Programmes lifecycle/resource;
- Enrolment does not create Entitlement;
- historical Enrolment does not prove current access;
- restart creates a new linked Enrolment and cannot silently consume a new paid entitlement;
- Edition archive does not itself imply Entitlement expiry;
- Pass 5 may re-adjudicate `PRG-GAP-004`, but may not solve Pass 6 delivery/availability, Pass 8 completion, Pass 9 substitution/exemption or Pass 10 compassionate recovery.

---

# 43. Pass 5 — Entitlement vs enrolment / access lifecycle

## 43.1 Scope hard stop

This pass answers only:

1. how Entitlement, current access and Enrolment coexist without lifecycle collapse;
2. what happens semantically when access is valid, expires, suspends, revokes or restores while Enrolment history exists;
3. whether access loss should automatically pause/abandon/complete an Enrolment;
4. how once-off, membership, gift, sponsored and practitioner-assigned programme access differ at the authority boundary;
5. how commercial refund/dispute/reversal affects programme access without rewriting history;
6. what restart/repeat participation may and may not infer from existing paid rights;
7. whether Edition archive/completion/catch-up dates imply Entitlement validity;
8. how duplicate/multiple entitlement sources relate to a single participant's programme history;
9. what current-policy checking requires at protected programme operations; and
10. whether `PRG-GAP-004` still requires a generic upstream Product rule.

This pass deliberately does **not** decide:

- exact lesson/day availability/prerequisite/release mechanics — Pass 6;
- cross-Domain activity-evidence contracts — Pass 7;
- completion thresholds/adjudication — Pass 8;
- exemption/substitute rules — Pass 9;
- compassionate catch-up/recovery after access interruption — Pass 10;
- exact Commerce billing/refund amounts, Paystack retry algorithms or provider APIs;
- exact Entitlements Ash Resources/actions/schema/idempotency keys;
- Privacy full-deletion retention implementation;
- safety eligibility consequences;
- Nuwe Jy Edition cancellation/postponement policy already held in `PRG-UPD-001`.

---

## 43.2 Pass-5 authority evidence

### PRG-EV-038 — Live authority baseline reconfirmed

Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413`.

`docs/00_platform/README.md` still routes current authority to Product/North Star, Product Law v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and the Platform Operating Model v1.0.1. `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` confirms those versions.

The Programmes/Learning ledgers remain working/non-authoritative.

### PRG-EV-039 — Product Law separates programme access from programme participation

Product Law §21F.4 states that programme access follows an explicit entitlement and may be public, free-account, membership-included, add-on, once-off purchased, bundle-included, sponsored or practitioner-assigned.

The same section says:
- once-off purchased programmes **may** grant permanent access to the delivered version;
- membership-only access stops when membership ends while completed progress history remains visible; and
- purchasers cannot see another participant's progress.

`DEC-150` independently locks explicit entitlement-based programme access.

### PRG-EV-040 — Enrolment lifecycle is durable and does not silently consume access rights

Product Law §21F.6 gives Enrolment its own lifecycle: enrol, schedule, begin, pause, resume, complete, abandon and restart.

It requires:
- every enrolment attempt to be preserved;
- restart to create a new linked enrolment rather than overwrite old progress;
- duplicate simultaneous enrolments in the same ProgrammeVersion to be prevented unless explicitly allowed; and
- restart not to silently consume a new paid entitlement.

`DEC-152` repeats the preservation/non-consumption rule.

### PRG-EV-041 — Domain Law gives Entitlements current-access authority and Programmes participation authority

Current Domain Law assigns:
- Commerce: product/offer, payment, refund/dispute and membership/subscription commercial truth;
- Entitlements: entitlement identity, scope, source/provenance, validity/expiry/revocation, redemption/consumption and current access;
- Programmes & Challenges: Edition/Cohort/Enrolment/progression/completion.

Programmes explicitly does **not** own commercial entitlement or payment.

Entitlements must current-policy check access; stale caches cannot override revocation. Duplicate payment/job/callback/redeem execution cannot multiply access, and payment success alone is not an entitlement until the authoritative grant transition.

### PRG-EV-042 — Commercial reversal changes current access without rewriting historical business truth

`DEC-300` locks the owner boundary for commercial reversals:
- provider callbacks are evidence, not access authority;
- Commerce records refund/duplicate/dispute/restoration/final reversal;
- Entitlements applies component-level access consequences idempotently;
- a confirmed dispute may temporarily suspend affected access;
- restored payment restores access idempotently;
- final lost chargeback revokes affected current access; and
- post-delivery full reversal ends current access while preserving historical delivery/reversal records.

Commercial history and current access remain distinct.

### PRG-EV-043 — Membership cancellation and failed-payment timing are commercial/access concerns, not Enrolment state

`DEC-039` says ordinary membership cancellation takes effect at the end of the paid period.

`DEC-043` locks a 72-hour grace period, provider-safe retries and suspension after final failure, with exact retry details still provider-gated.

`DEC-041` preserves purchased/historical outputs while membership-only content/community/new adjustments end after cancellation.

Therefore Programmes must not infer current access from a pending commercial cancellation flag, failed payment attempt or provider callback. It consumes the authoritative access outcome.

### PRG-EV-044 — Gift/sponsor purchaser and programme participant are separate

`DEC-044` says a purchaser sees redemption status only; redeemed access is non-transferable.

`DEC-210` keeps purchaser, intended recipient, redeemed participant and enrolment separate.

Product §21H.13 makes the Nuwe Jy chain explicit:

`purchaser → purchased challenge entitlement → intended recipient → redeemed participant → enrolment`

The commercial actor therefore never becomes programme-participation authority merely because they paid.

### PRG-EV-045 — Edition configuration may reference entitlement policy but cannot own it

Nuwe Jy ChallengeEdition configuration includes `entitlements` and `pricing product`, while Pass 4 established that Edition remains a Programmes-owned delivery contract and Commerce/Entitlements retain their own authority.

Edition start/release/completion/catch-up/archive dates are therefore not entitlement validity dates unless the separately governed entitlement/offer explicitly says so.

Likewise, an Entitlement expiry/revocation date is not automatically an Edition or Enrolment lifecycle transition.

### PRG-EV-046 — Access must be evaluated from current authority at protected operations

Architecture requires current policy before delivery and says revocable permission is resolved from current server state when an authoritative action occurs. Long-lived LiveViews must re-evaluate current authority rather than treating mount-time access as permanent.

Combined with Domain Law's stale-cache rule, an old page/session/projection cannot extend expired or revoked programme access.

### PRG-EV-047 — Commerce/Entitlements Pre-JIT working evidence is compatible but remains non-authoritative

The current non-authoritative Commerce / Entitlements / Recurring Membership Pre-JIT compact contract reinforces, without overriding authority:
- Commerce interpretation and Entitlement consequence are separate layers;
- multi-source entitlement state is source/provenance aware;
- ending one source must not erase another valid source;
- permanent once-off access is non-expiring only while the qualifying purchase remains commercially valid;
- historical fulfilment can remain true after later reversal; and
- caches/projections cannot extend revoked/expired authority.

This is supporting cross-stream consistency evidence only, not Product/Domain authority.

---

# 44. Pass-5 semantic model

These are working discovery semantics, not Resource/schema prescriptions.

## 44.1 Three independent dimensions must remain separate

For a protected programme journey, NewYou must be able to represent all three independently:

| Dimension | Owner | Answers |
|---|---|---|
| **Entitlement/right** | Entitlements | What right exists, its scope/provenance/validity/expiry/revocation/consumption? |
| **Current access result** | Entitlements + applicable current gates | May this protected operation succeed **now**? |
| **Enrolment/participation history** | Programmes & Challenges | What programme attempt exists, under which ProgrammeVersion/Edition/Cohort, and what participation state/history occurred? |

A change in one dimension does not silently rewrite the others.

## 44.2 Access loss default

The generic, authority-safe default when the only qualifying programme right becomes invalid is:

```text
Entitlement/current access changes
        ↓
protected programme operation fails closed
        ↓
existing Enrolment/progress/history remains preserved
```

It is **not**:

```text
access ended
→ auto-pause Enrolment
→ auto-abandon Enrolment
→ delete progress
→ mark complete
```

Any additional participant-facing programme transition requires an explicit programme/offer policy.

## 44.3 Access restoration default

When authoritative access is restored:

```text
Entitlements restores current right/access
        ↓
existing Enrolment history remains the same
        ↓
Programmes evaluates what participation/delivery action is currently allowed
```

Restoration does not itself create:
- a new Enrolment;
- a restart;
- a new personal schedule;
- an extension;
- a completion outcome; or
- catch-up entitlement.

Those later consequences remain Programme/Edition policy.

## 44.4 Once-off programme access must have explicit scope

Product Law permits, but does not universally require, permanent access to the delivered version.

Therefore each sellable programme/Edition offer must make the participant promise explicit:
- exact programme/version/edition scope where applicable;
- start/expiry or permanent/non-expiring condition;
- whether the right covers protected historical viewing only, active participation, restart/re-enrolment, or some combination;
- source/provenance and any governed revocation condition.

Do not infer `once_off_purchase == lifetime_everything`.

## 44.5 Membership programme access

Membership-included/add-on access is current-right dependent.

When qualifying membership ends:
- membership-only protected programme access ends;
- completed progress history remains visible where Product Law says so;
- Enrolment history remains durable;
- Programmes does not create a replacement right.

If membership later becomes valid again, current access can return without rewriting old Enrolment history. Delivery/recovery implications remain later passes.

## 44.6 Edition dates and entitlement dates are orthogonal by default

An Edition may have:
- enrolment window;
- start/release calendar;
- completion deadline;
- catch-up window;
- archive date.

An Entitlement may have:
- validity start;
- expiry;
- revocation/suspension;
- permanent/non-expiring scope.

These may intentionally align, but one does not become the other by inference.

## 44.7 Restart and repeat participation

Restart creates a new linked Enrolment.

It must:
1. preserve prior Enrolment/progress;
2. check current qualifying access;
3. not silently consume a new paid right; and
4. not infer that a permanent delivered-version viewing right automatically includes unlimited repeat facilitated participation.

The concrete offer determines whether an existing entitlement covers another attempt.

## 44.8 Multiple access sources

Programmes must not care how many payment/grant sources exist beyond the minimum access/provenance information it legitimately needs.

If Entitlements says current protected access succeeds, Programmes proceeds under programme rules. If one source ends, Programmes must not independently revoke another valid source.

Multiple rights/sources do not automatically create multiple Enrolments or additional programme attempts.

## 44.9 Current-policy enforcement

Protected programme commands must not rely on:
- browser state;
- LiveView mount-time access;
- cached entitlement projections;
- Commerce/provider state directly;
- prior successful access checks.

Where revocation/expiry matters, the authoritative operation must use current owner-managed access state.

---

# 45. Pass-5 focused pressure tests

## PRG-PT-116 — Valid entitlement exists but participant never enrols

**Scenario class:** access versus participation existence.

**Scenario:** Participant has an active programme entitlement but never completes enrolment/onboarding.

**Expected invariants:**

- Entitlements retains the access right according to its scope/validity.
- No Enrolment is fabricated merely because access exists.
- Programme participation/progress remains absent unless actual programme participation occurs.

**Analysis:** Entitlement and Enrolment are independently durable truths.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-117 — Historical Enrolment exists while current access is false

**Scenario class:** history versus current access.

**Scenario:** An Enrolment exists, but its qualifying entitlement has expired or been revoked.

**Expected invariants:**

- Programmes preserves Enrolment/version/history.
- Protected programme operations consult current Entitlements authority and fail closed when access is not permitted.
- Programmes does not recreate or extend access from historical participation.

**Analysis:** An Enrolment can remain historically valid while current protected access is denied.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-118 — Membership cancellation is scheduled but paid period has not ended

**Scenario class:** commercial timing versus access.

**Scenario:** A membership participant cancels; cancellation is effective only at the paid-period boundary.

**Expected invariants:**

- Programmes does not block access merely because Commerce records pending cancellation.
- Entitlements remains the current-access authority.
- The Enrolment lifecycle is unchanged solely by cancellation scheduling.

**Analysis:** `cancel_at_period_end`-style commercial state is not an Enrolment or access result by itself.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-119 — Membership-only access ends during an active Enrolment

**Scenario class:** entitlement lapse.

**Scenario:** Membership reaches its end while a programme Enrolment still exists.

**Expected invariants:**

- Membership-only protected access ends according to Entitlements.
- Completed progress/history is preserved; Product specifically keeps completed progress history visible.
- The Enrolment is not deleted.
- No automatic `pause`, `abandon` or `complete` transition is inferred merely from access loss.

**Analysis:** Current law supplies the safe default boundary: deny protected access, preserve programme history, do not invent a programme transition.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-120 — Failed payment remains inside the governed grace period

**Scenario class:** payment failure/grace.

**Scenario:** Membership payment fails, retries remain authorised and the grace period has not ended.

**Expected invariants:**

- Programmes does not interpret provider/payment-attempt state as access authority.
- Current access follows Entitlements' authoritative state.
- No Enrolment mutation occurs because a payment attempt failed.

**Analysis:** Grace/payment mechanics remain Commerce/Entitlements concerns. Programmes consumes only current access.

**Disposition:** `PASS`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-121 — Failed payment reaches final suspension

**Scenario class:** suspension.

**Scenario:** Retry/grace is exhausted and recurring entitlements are suspended.

**Expected invariants:**

- Protected access fails closed once Entitlements says access is suspended.
- Enrolment/history stays intact.
- Suspension does not become an Enrolment `pause` unless a separate programme policy explicitly commands such a transition.

**Analysis:** Using Enrolment pause as a mirror of entitlement suspension would create shared/duplicated state.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-122 — Suspended access is later restored

**Scenario class:** restoration.

**Scenario:** Authoritative commercial evidence restores a previously suspended qualifying right.

**Expected invariants:**

- Entitlements restores access idempotently.
- Restoration does not create a new Enrolment.
- Restoration does not automatically invoke Enrolment `resume`; the prior Enrolment remains the same durable attempt unless Programmes policy says otherwise.
- Schedule/availability consequences are deferred to Pass 6/10.

**Analysis:** Access restoration and participation resumption are distinct concepts.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-123 — Access is restored after the Edition/catch-up timing has moved on

**Scenario class:** restoration versus delivery window.

**Scenario:** Qualifying access returns after the scheduled cohort has concluded or a catch-up window may have elapsed.

**Expected invariants:**

- Entitlements can truthfully restore current access within its scope.
- Programmes must still apply its own current Edition/availability/recovery rules.
- Restored access alone cannot fabricate a new schedule, extension, completion or restart.

**Analysis:** This seam is coherent without deciding recovery policy here; Pass 6/10 owns what content/action remains available.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Programme/Edition JIT; detailed availability/recovery remains Pass 6/10.

---

## PRG-PT-124 — Once-off programme purchase explicitly grants permanent delivered-version access

**Scenario class:** once-off access scope.

**Scenario:** An approved offer says the once-off purchase grants permanent access to the delivered version.

**Expected invariants:**

- Entitlements carries that scope/validity.
- Programme catalogue/Edition archive does not silently terminate the right.
- Permanent access remains bounded to the promised delivered version/scope and does not rewrite ProgrammeVersion history.

**Analysis:** Product Law expressly permits this model.

**Disposition:** `PASS`.

**Route:** Concrete offer/Entitlement scope must be explicit before FP-008 sale/activation; JIT must not invent the commercial promise.

---

## PRG-PT-125 — Once-off purchase is assumed permanent without the offer saying so

**Scenario class:** commercial promise ambiguity.

**Scenario:** Implementation treats every once-off programme purchase as lifetime access because Product says it 'may' grant permanent access.

**Expected invariants:**

- `may` is permission, not a universal promise.
- The concrete offer/Edition entitlement scope must be explicit before sale.
- JIT cannot silently select permanent versus time-bounded access.

**Analysis:** Assuming lifetime access would invent a commercial promise.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Concrete offer/Entitlement scope must be explicit before FP-008 sale/activation; JIT must not invent the commercial promise.

---

## PRG-PT-126 — Edition archive date is used as entitlement expiry

**Scenario class:** delivery/access lifecycle collapse.

**Scenario:** Implementation revokes access automatically on the Edition's archive date.

**Expected invariants:**

- Edition archive remains Programmes delivery/history configuration.
- Entitlement expiry/revocation remains Entitlements truth.
- The two dates may coincide only if the governed entitlement/offer explicitly binds them.

**Analysis:** Pass 4 already separated archive from access; Pass 5 confirms the authority boundary.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-127 — Entitlement expiry is treated as programme completion

**Scenario class:** access/completion conflation.

**Scenario:** A time-bounded entitlement expires and implementation marks the Enrolment complete.

**Expected invariants:**

- Completion remains Programmes-owned and rule-based.
- Access expiry does not prove required participation.
- Historical progress remains what actually occurred.

**Analysis:** Commercial/access time cannot fabricate programme completion.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-128 — Programme completion automatically expires a still-valid entitlement

**Scenario class:** completion/access conflation.

**Scenario:** A participant completes the programme while her entitlement still promises historical/delivered-version access.

**Expected invariants:**

- Completion does not revoke or consume a separately valid right unless that exact entitlement is explicitly consumable-on-completion.
- Entitlements remains current-access authority.
- Completion history remains separate from right validity.

**Analysis:** Completion and access duration are separate dimensions.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-129 — Participant abandons an Enrolment while entitlement remains valid

**Scenario class:** participation ending versus access.

**Scenario:** A participant abandons an attempt but still owns a valid permanent or time-bounded access right.

**Expected invariants:**

- Programmes records abandonment.
- Entitlements is not revoked merely because participation ended.
- Future viewing or a later restart/re-enrol decision follows the right's scope plus programme policy.

**Analysis:** Enrolment abandonment cannot silently mutate foreign entitlement truth.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-130 — Entitlement is revoked while Enrolment is active

**Scenario class:** access ending versus participation.

**Scenario:** A sponsor, membership, commercial reversal or other authoritative cause revokes the only qualifying right.

**Expected invariants:**

- Entitlements ends current access.
- Programmes preserves the active/historical Enrolment record.
- No automatic abandonment/deletion/completion follows without explicit programme policy.

**Analysis:** The default safe consequence is access denial, not invented participation state.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-131 — Unused programme entitlement is refunded before Enrolment

**Scenario class:** refund before use.

**Scenario:** Commerce validates a refund for an unused programme right before any Enrolment exists.

**Expected invariants:**

- Commerce owns refund truth.
- Entitlements ends the affected right idempotently.
- Programmes has no Enrolment to mutate.
- Provider evidence cannot directly alter programme/access state.

**Analysis:** This is a clean owner-mediated path.

**Disposition:** `PASS`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-132 — Post-delivery full reversal occurs after participation began

**Scenario class:** commercial reversal after fulfilment.

**Scenario:** A full reversal is accepted after protected programme delivery/participation has occurred.

**Expected invariants:**

- Current affected access may end under DEC-300.
- Historical programme delivery/participation and reversal provenance are preserved.
- Programmes does not delete historical Enrolment/progress to make the refund look as though participation never happened.

**Analysis:** Historical fulfilment and current access can both be truthful after reversal.

**Disposition:** `PASS`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-133 — Chargeback temporarily suspends access and is later won/restored

**Scenario class:** reversible dispute.

**Scenario:** A confirmed dispute suspends access; later authoritative restoration occurs.

**Expected invariants:**

- Suspension/restoration is source-scoped and idempotent in Entitlements.
- Enrolment remains the same attempt.
- Programmes neither deletes progress on suspension nor creates a new attempt on restoration.

**Analysis:** DEC-300 directly supports the access consequence; programme history remains independent.

**Disposition:** `PASS`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-134 — Final lost chargeback revokes current access

**Scenario class:** final reversal.

**Scenario:** A previously disputed payment becomes a final lost chargeback.

**Expected invariants:**

- Entitlements revokes the affected current access.
- Historical enrolment/delivery/reversal records remain.
- Unrelated valid entitlements must not be revoked by Programmes.

**Analysis:** Final commercial invalidity affects the sourced right, not programme history globally.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-135 — Duplicate payment/callback attempts to multiply programme access

**Scenario class:** idempotency.

**Scenario:** Duplicate provider/payment/redeem execution arrives for one logical programme right.

**Expected invariants:**

- Payment evidence alone does not grant access.
- Entitlements converges idempotently and does not multiply the right.
- Duplicate access evidence does not create duplicate Enrolments.

**Analysis:** Domain Law already requires idempotent grant/redemption behaviour.

**Disposition:** `PASS`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-136 — Two legitimate qualifying access sources overlap and one ends

**Scenario class:** multi-source access.

**Scenario:** A participant has two independently valid qualifying sources for the same protected programme capability; one source expires/revokes.

**Expected invariants:**

- Programmes does not decide which source wins.
- Ending one source must not cause Programmes to revoke another valid source.
- Effective access remains an Entitlements decision over current valid grants.
- No duplicate programme history is created because access has multiple provenance paths.

**Analysis:** Current Domain ownership plus the non-authoritative CER working contract support source-scoped convergence; exact grant identity remains Entitlements JIT.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-137 — Multiple valid entitlement sources are treated as multiple enrolments

**Scenario class:** source-count versus participation-count.

**Scenario:** Implementation creates one Enrolment per purchase/grant source.

**Expected invariants:**

- Entitlement provenance count does not define Enrolment count.
- Duplicate simultaneous same-version Enrolments remain prevented unless explicitly allowed.
- Programme participation history follows actual attempts, not payment/grant multiplicity.

**Analysis:** Access-source multiplicity is not programme-attempt multiplicity.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-138 — Gift entitlement exists before redemption

**Scenario class:** gift purchaser/recipient boundary.

**Scenario:** A purchaser buys Nuwe Jy for another person; the entitlement has not yet been redeemed by the participant.

**Expected invariants:**

- No participant Enrolment is fabricated before the recipient/participant boundary is resolved.
- Purchaser may see only governed commercial/redemption state.
- Programme private history remains unavailable to purchaser.

**Analysis:** Product §21H.13 and DEC-210 are explicit.

**Disposition:** `PASS`.

**Route:** Entitlements/Commerce/Programmes owner interfaces; no new programme authority.

---

## PRG-PT-139 — Purchaser tries to transfer redeemed participant access

**Scenario class:** redeemed gift transfer.

**Scenario:** A purchaser asks support to move a redeemed Nuwe Jy right to someone else.

**Expected invariants:**

- Redeemed access is non-transferable under DEC-044.
- Purchaser payment status does not confer authority over participant Enrolment.
- Any exceptional remedy would require explicit owned policy rather than editing Programmes records.

**Analysis:** Participant/purchaser separation is already governed.

**Disposition:** `PASS`.

**Route:** Entitlements/Commerce/Programmes owner interfaces; no new programme authority.

---

## PRG-PT-140 — Sponsored or practitioner-assigned access is revoked mid-Enrolment

**Scenario class:** non-purchase grant revocation.

**Scenario:** A sponsored/practitioner-assigned qualifying right ends while participation history exists.

**Expected invariants:**

- Entitlements owns grant validity/revocation.
- Programmes denies protected access when the right is no longer valid.
- Enrolment/progress is retained.
- Programme does not infer commercial refund or practitioner relationship state.

**Analysis:** The source of access changes; authority separation does not.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Entitlements/Commerce/Programmes owner interfaces; no new programme authority.

---

## PRG-PT-141 — Restart when an existing entitlement still qualifies

**Scenario class:** restart/reuse.

**Scenario:** Participant restarts after abandon/completion and a still-valid entitlement may cover the new attempt.

**Expected invariants:**

- Restart creates a new linked Enrolment.
- Programmes rechecks current qualifying access.
- It does not consume/create another paid right merely because restart occurred.
- Whether the existing right covers a new participation attempt is determined by its governed scope.

**Analysis:** Product explicitly forbids silent new paid-entitlement consumption.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Concrete offer/Entitlement scope must be explicit before FP-008 sale/activation; JIT must not invent the commercial promise.

---

## PRG-PT-142 — Restart when no qualifying entitlement exists

**Scenario class:** restart without access.

**Scenario:** Participant requests restart after the prior access right expired/revoked.

**Expected invariants:**

- A new linked Enrolment must not be created as a back door to access unless the governed programme action is authorised.
- Programmes cannot manufacture a new entitlement.
- The participant may need a new/renewed qualifying right according to the concrete offer.

**Analysis:** Restart intent is not access authority.

**Disposition:** `PASS`.

**Route:** Concrete offer/Entitlement scope must be explicit before FP-008 sale/activation; JIT must not invent the commercial promise.

---

## PRG-PT-143 — Restart silently consumes a spare/new paid entitlement

**Scenario class:** entitlement consumption.

**Scenario:** Implementation sees an unused paid programme credit and consumes it automatically when restart is clicked.

**Expected invariants:**

- Product explicitly prohibits silent new paid-entitlement consumption.
- Any consumption must be an explicit Entitlements-owned governed action with correct scope/participant intent.
- The old and new Enrolments remain linked history.

**Analysis:** Silent credit consumption is directly rejected by Product Law.

**Disposition:** `PASS`.

**Route:** Concrete offer/Entitlement scope must be explicit before FP-008 sale/activation; JIT must not invent the commercial promise.

---

## PRG-PT-144 — Permanent delivered-version access is treated as unlimited free new participation attempts

**Scenario class:** scope expansion.

**Scenario:** A permanent content/access right is interpreted as unlimited repeat cohort enrolments/restarts.

**Expected invariants:**

- Permanent access to the delivered version does not, by wording alone, prove unlimited new participation attempts, cohort seats, facilitator service or new Edition access.
- Repeat Enrolment history can exist, but admission/right-to-reparticipate must be explicit.
- No generic unlimited-restart promise may be inferred.

**Analysis:** `access to delivered version` and `right to a new governed participation attempt` are different possible scopes.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Concrete offer/Entitlement scope must be explicit before FP-008 sale/activation; JIT must not invent the commercial promise.

---

## PRG-PT-145 — Entitlement to V1 is silently treated as access to V2

**Scenario class:** version scope.

**Scenario:** A participant owns access tied to a delivered V1; V2 becomes approved/current.

**Expected invariants:**

- Active Enrolment stays on V1 unless governed migration/safety correction.
- A permanent delivered-version right does not silently expand to V2.
- A broader programme-family entitlement may cover future versions only if its governed scope explicitly says so.

**Analysis:** Version entitlement scope must not float accidentally with `latest approved`.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Concrete offer/Entitlement scope must be explicit before FP-008 sale/activation; JIT must not invent the commercial promise.

---

## PRG-PT-146 — Stale browser/LiveView continues after revocation

**Scenario class:** current-policy enforcement.

**Scenario:** Participant opened protected programme UI while entitled; access is revoked before a later protected action.

**Expected invariants:**

- Authoritative operations re-evaluate current access.
- Mount-time/session/cache state cannot override revocation.
- Already committed historical evidence is not erased because a later action is refused.

**Analysis:** Architecture and Domain Law both require current-policy checks.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-147 — Payment provider says success before authoritative entitlement grant

**Scenario class:** provider evidence boundary.

**Scenario:** A browser return/webhook shows payment success but Entitlements has not yet committed the qualifying grant.

**Expected invariants:**

- Programmes does not grant access from provider state.
- Commerce first verifies/records commercial truth; Entitlements applies the access consequence.
- No Enrolment/access success is fabricated from provider evidence.

**Analysis:** Payment success is not entitlement authority.

**Disposition:** `PASS`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

## PRG-PT-148 — Programme operator manually toggles access

**Scenario class:** operator authority.

**Scenario:** Programme admin tries to fix an access issue by directly setting an Enrolment/access flag.

**Expected invariants:**

- Operator UI is not authority.
- Programmes cannot write Entitlements truth.
- The operator must invoke the owning Entitlements/Commerce workflow under policy; audit/history remains explicit.

**Analysis:** Direct programme-side access toggles would create a second entitlement authority.

**Disposition:** `PASS`.

**Route:** Documentary boundary + JIT enforcement.

---

## PRG-PT-149 — Programme is paused/retired or Edition concludes while entitlement remains valid

**Scenario class:** catalogue/delivery versus access.

**Scenario:** Programme catalogue or Edition delivery status changes while the participant retains a valid access right.

**Expected invariants:**

- Programme/Edition state and entitlement validity remain separate.
- A participant-facing access effect occurs only where Product/offer policy explicitly requires it.
- Historical rights and Enrolments are not silently rewritten by catalogue state.

**Analysis:** Catalogue/delivery lifecycle cannot substitute for Entitlements.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Programme/Edition JIT; detailed availability/recovery remains Pass 6/10.

---

## PRG-PT-150 — Entitlement changes concurrently with a protected programme command

**Scenario class:** race/current authority.

**Scenario:** An access revocation/restoration races a protected programme action.

**Expected invariants:**

- The authoritative operation must evaluate the applicable current access/transaction boundary rather than cached UI state.
- Duplicate/reordered consequences must be idempotent.
- No successful programme mutation may depend on PubSub/cache freshness as authority.

**Analysis:** Exact transaction/locking/idempotency mechanics are JIT/Phase 8, but the authority invariant is already fixed.

**Disposition:** `PASS_WITH_REFINEMENT`.

**Route:** Commerce/Entitlements JIT + programme JIT; Phase 8 where concurrency/recovery is material.

---

# 46. Pass-5 gap adjudication

## PRG-GAP-004 — Entitlement lapse during Enrolment — refined by Pass 5

**Prior bootstrap classification:** `ENTITLEMENT_SEAM_GAP`.

**Pass-5 finding:** the broad lifecycle ambiguity is now substantially resolved.

Current authority already establishes the generic behaviour:

1. Entitlements owns current programme access.
2. Programmes owns Enrolment/history.
3. When the only qualifying right ends, protected access stops/fails closed.
4. Enrolment/progress/history is preserved rather than deleted.
5. No current Product/Domain rule says entitlement lapse automatically means Enrolment `pause`, `abandon`, `complete`, restart or deletion.
6. Restoration of access likewise does not automatically create/resume/restart an Enrolment.
7. Membership-only Product Law specifically preserves completed progress history after membership access ends.

Therefore **a universal automatic Enrolment transition on entitlement lapse is rejected**, not left open.

### Remaining concrete requirement

Before a sellable FP-008 Nuwe Jy Edition is activated, the concrete offer/Edition configuration must explicitly state its entitlement promise, including enough scope/validity to answer at least:

- what programme/version/Edition access is granted;
- whether access is time-bounded or permanent to the delivered version;
- when access begins/ends;
- which participant receives it after redemption; and
- whether the same right permits restart/re-enrolment or only continued viewing/use of the delivered version.

That is a **concrete offer/Entitlements declaration requirement**, not evidence that NewYou needs a new universal Product lifecycle or a Programmes-owned access resource.

If Product later wants additional semantics on access loss — for example automatic Enrolment pause, protected catch-up extension, special withdrawal outcome or another commercial/participation promise — that specific behaviour must be promoted before JIT implements it.

**Revised status:** `NARROWED / GENERIC SEMANTIC BOUNDARY RESOLVED / CONCRETE OFFER DECLARATION REQUIRED`.

**New upstream delta:** NONE in Pass 5.

No new `PRG-GAP-###` or `PRG-UPD-###` is justified by this pass.

---

# 47. Pass-5 refinements to earlier working synthesis

## PRG-REF-020 — Access lapse is not an Enrolment lifecycle transition

Entitlement expiry, revocation or suspension changes current access. It does **not** by itself mean Enrolment `pause`, `abandon`, `complete` or deletion.

If a programme wants one of those additional transitions, that participant consequence must be explicitly governed.

## PRG-REF-021 — Access restoration is not Enrolment restart/resume

Restored Entitlements access makes protected capability access possible again within its scope. It does not create a new Enrolment, restart an old one or automatically mark a paused Enrolment resumed.

Programmes applies its own participation/delivery rules after access succeeds.

## PRG-REF-022 — Edition/archive/completion dates are not entitlement validity by default

Edition start/release/completion/catch-up/archive dates remain Programmes truth. Entitlement start/expiry/revocation remains Entitlements truth.

They may intentionally align only through explicit governed configuration; one must never be derived silently from the other.

## PRG-REF-023 — Permanent delivered-version access is narrower than unlimited participation

A promise of permanent access to a delivered ProgrammeVersion does not automatically promise:
- unlimited new Enrolments;
- repeated facilitated cohort seats;
- future ProgrammeVersions;
- future Editions; or
- recurring staff/live/community service.

Those are separate possible scopes and must be explicit.

## PRG-REF-024 — Restart must check entitlement scope without silent consumption

Restart always creates a new linked Enrolment. Before protected participation, current access is re-evaluated.

The restart action must neither manufacture a grant nor silently consume a new paid entitlement. Whether an existing right covers restart is an Entitlements/offer-scope question.

## PRG-REF-025 — Multiple access sources do not multiply programme participation

Entitlements may have source/provenance complexity. Programmes must not translate grant count, payment count or funding-source count into Enrolment count.

Effective current access remains an Entitlements decision; Enrolment count follows actual governed participation attempts.

## PRG-REF-026 — Protected programme operations require current access, not remembered access

A prior successful access check, LiveView mount, browser page, cache entry or PubSub observation cannot guarantee later protected access.

The authoritative operation re-checks the current owner-managed state where revocation/expiry matters.

## PRG-REF-027 — PRG-GAP-004 is narrowed from lifecycle ambiguity to concrete-offer declaration

The broad bootstrap uncertainty is resolved: current access loss itself does not require a generic Enrolment transition. The safe generic consequence is fail-closed protected access plus preserved programme history.

What remains programme-specific is the commercial/access promise and any *additional* participant consequence. Before sale/activation, the concrete Nuwe Jy offer/Edition must explicitly declare entitlement scope/validity (including whether once-off access is permanent or time-bounded). If Product wants automatic pause, abandonment, extension, transfer or similar behaviour on access loss, that rule must be promoted explicitly rather than invented in JIT.

---

# 48. Pass-5 anti-LMS / YAGNI outcome

Pass 5 explicitly rejects:

- a Programmes-owned duplicate `Access` resource/lifecycle;
- copying Entitlement expiry/revocation state onto Enrolment as authority;
- automatically pausing/abandoning/completing Enrolment whenever access changes;
- automatically restoring/resuming/restarting Enrolment when access returns;
- treating Edition archive/completion dates as entitlement expiry without explicit policy;
- treating entitlement expiry as programme completion;
- treating programme completion/abandonment as entitlement revocation;
- treating permanent delivered-version access as unlimited repeat cohort/service entitlement;
- one Enrolment per payment/grant source;
- one participation attempt per entitlement row;
- a generic LMS seat/licence pool as programme authority;
- generic token/credit consumption merely because LMS products often consume “seats” on enrolment;
- allowing browser/cache/provider state to extend protected access after authoritative revocation.

Generic LMS licensing/seat/registration engines remain `DEFER_YAGNI`.

---

# 49. Pass-5 disposition

**Outcome: PASS WITH NON-BLOCKING CORRECTIONS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Entitlement/right, current access result and Enrolment/history are separate lifecycle dimensions with separate authority.
2. Entitlements owns programme access scope, provenance, validity, expiry, revocation, consumption and current access.
3. Programmes owns Enrolment/participation history and must not duplicate Entitlements truth.
4. Current access loss does not automatically pause, abandon, complete or delete an Enrolment.
5. Current access restoration does not automatically resume, restart or create an Enrolment.
6. Protected programme operations fail closed when current access is not authorised; stale UI/cache/provider state cannot extend access.
7. Programme history/progress is preserved across access suspension/revocation unless separate Privacy/deletion law requires otherwise.
8. Membership-only programme access ends with qualifying membership, while completed progress history remains visible as Product Law specifies.
9. Once-off programme purchases may be permanent to the delivered version only when the concrete offer says so; permanent access is not universal.
10. Permanent delivered-version access does not automatically include unlimited repeat Enrolments, future ProgrammeVersions, future Editions, facilitated seats or ongoing services.
11. Edition start/completion/catch-up/archive dates are not Entitlement validity dates by default.
12. Entitlement expiry is not programme completion; completion/abandonment is not entitlement revocation.
13. Restart creates a new linked Enrolment, re-checks current access, and may not silently consume a new paid entitlement.
14. Multiple entitlement/payment/grant sources do not multiply Enrolments; Programmes consumes the authoritative current-access result.
15. Commercial reversal can end current access while historical programme delivery/participation remains truthful and preserved.
16. Purchaser/recipient/participant/Enrolment remain separate; purchaser sees no private programme journey.
17. Provider success/failure is evidence, not direct programme-access authority.
18. `PRG-GAP-004` is narrowed: the generic seam is resolved; the concrete FP-008 offer must declare access scope/validity and any special lapse consequence before sale/activation.
19. No new Domain, `PRG-GAP-###` or `PRG-UPD-###` is justified by Pass 5.
20. Exact Commerce/Entitlements mechanics remain in their owning JIT/validation streams and must not be reimplemented inside Programmes.

**Pass hard stop:** Pass 6 has not started. Delivery, availability and sequencing semantics remain deliberately unexamined beyond the minimum references needed to show that access success does not itself decide what lesson/day/action is currently available.

**Broad discovery remains unfrozen.** The final convergence/freeze sentence must not be used on the strength of this pass.
