# NewYou Operations, Support & Pilot Evidence Pre-JIT Discovery — Working v0.14.0

> **WORKING / NON-AUTHORITATIVE**  
> **IMPLEMENTATION NOT AUTHORISED**

- **Document version:** `v0.14.0`
- **Date:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Exact NewYou `main` baseline reverified:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch head before this successor:** `452a71f49224e94890cf6a0a3bc59ddcefaf0660`
- **Working branch:** `prejit/operations-support-pilot`
- **Predecessor:** `NEWYOU_OPERATIONS_SUPPORT_PILOT_PREJIT_DISCOVERY_WORKING_v0.13.0.md`
- **Successor form:** additive focused successor. Read v0.13.0 for `OPS-PT-001...198`; this file adds only the new bounded v0.14.0 reasoning so historical evidence is not duplicated or rewritten.
- **Purpose:** pressure-test only `OPS-UPD-007` — the exact Product-level start event for the General Wellness single 14-day retain-or-refund choice window.
- **Scope:** `general_wellness_only`; `held_unconsumed` plan-component right; decision/choice communication; initial handoff; queue/provider ambiguity; multi-channel delivery; open/read telemetry; malformed/wrong-destination communication; retries/reminders; explicit participant choice; no-response deadline and automatic refund obligation.
- **Non-goals:** no clinical-rule redesign; no Plan-generation semantics; no provider selection; no reminder-cadence design; no new Domain/Resource; no implementation/API/storage selection; no PR; no authority amendment.
- **Current overall disposition:** `FOCUSED PASS CONVERGED / OPS-UPD-007 CONFIRMED AND NARROWED / PRODUCT-LEVEL QUALIFYING-COMMUNICATION CLOCK-START RULE STILL REQUIRED / OQ-017 AND OQ-036 REMAIN DOWNSTREAM / BROAD STREAM FREEZE STILL BLOCKED`.

---

# 128. Live baseline and bounded authority route

Immediately before this pass:

```text
main = 086ade7b28c000de1c387acb9760e5eb08bb0413
working branch head = 452a71f49224e94890cf6a0a3bc59ddcefaf0660
```

Relevant authority/evidence rechecked:

- `00_PLATFORM_v1.6.0.md` §21T.4;
- `01_DECISIONS_v1.6.0.md` `DEC-308`;
- `04_DOMAIN_MAP_v1.2.0.md` owner boundaries for Safety & Eligibility, Commerce, Entitlements and Communications;
- certified `FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md` as lower-level delivery evidence/ownership guidance only;
- `02_OPEN_WORK_v1.2.59.md` for `OQ-017` reminder delivery and `OQ-036` notification provider/channel policy.

Current locked Product text establishes:

- `general_wellness_only` does not fulfil a purchased personalised Plan;
- the plan-component entitlement remains unconsumed while the participant chooses retain or refund;
- refund uses the original snapshotted plan-component allocation;
- the participant receives **one 14-day choice window when NewYou communicates the governed decision and the retain-or-refund choice**;
- reminders occur inside the same window;
- no recorded choice by the end creates automatic refund and component-entitlement closeout.

No archive document was used to override current authority.

---

# 129. What current authority already fixes

## 129.1 Outcome finalisation is not the clock start

`DEC-308` does not say the clock starts merely when Safety & Eligibility records `general_wellness_only`. It starts when NewYou communicates the governed decision **and** the retain-or-refund choice.

Therefore an internal eligibility transition alone is insufficient to infer clock start.

## 129.2 There is one window, not one per channel or attempt

Because Product Law promises one 14-day window, retries, second channels, provider replay and reminders cannot each create a new 14-day period.

## 129.3 Communications evidence does not silently become Product-right authority

Communications owns communication obligations, delivery attempts, provider observations and reconciliation. Provider/job/UI/telemetry state does not automatically define another Domain's business transition.

Therefore Product must define the semantic communication class first; `OQ-036`/JIT can then map channel-specific evidence to it.

## 129.4 Reminder/provider design is already routed

`OQ-017` remains reminder-delivery design. `OQ-036` remains notification-provider/channel policy. This pass does not select providers, channels, retries or reminder cadence.

---

# 130. Semantic dimensions that must not be collapsed

1. **Governed eligibility decision** — current authoritative `general_wellness_only` outcome.
2. **Retain-or-refund offer readiness** — correct participant choice over the snapshotted plan component.
3. **Communication obligation** — durable internal obligation; not itself participant communication.
4. **Delivery attempt/provider evidence** — accepted, failed, bounced, ambiguous, delivered, unknown.
5. **Qualifying participant-facing communication** — the unresolved Product-level clock-start concept.
6. **Open/read/view telemetry** — optional evidence; not automatically Product authority.
7. **Single choice-window lifecycle** — starts once, ends by explicit choice or no-choice expiry, no reset by retries/reminders.
8. **Refund obligation vs refund execution** — deadline consequence is distinct from later Commerce/provider execution.

A qualifying communication must at least concern the current governed decision and the retain-or-refund choice, be directed through an authorised participant-facing route, and have a governed way for the participant to record either choice. Exact channel evidence remains downstream.

---

# 131. Focused pressure tests

## OPS-PT-199 — Outcome becomes authoritative but initial communication is delayed

`general_wellness_only` is recorded, but queue/provider outage delays participant-facing communication for two days.

**Invariant:** the participant must not silently lose two days from the Product-promised 14-day choice period merely because internal state changed earlier.

**Disposition:** `NEEDS_WORKING_DELTA` → `OPS-UPD-007`.

## OPS-PT-200 — Durable communication obligation exists but no dispatch occurs

A MessageIntent/outbox/job or equivalent durable obligation exists, but no participant-facing attempt occurs.

**Invariant:** internal durability is not participant communication and does not start the Product clock.

**Disposition:** `PASS_WITH_REFINEMENT`.

## OPS-PT-201 — Provider accepts initial message; final delivery unknown or later bounces

**Invariant:** raw provider acceptance is not automatically evidence that the Product-level communication obligation completed. A later bounce/unknown cannot be forced into “communicated” because acceptance is easy to observe.

**Disposition:** `NEEDS_WORKING_DELTA` → Product semantic class first, then `OQ-036` mapping.

## OPS-PT-202 — One channel qualifies; another follows later

Example: qualifying participant-surface communication at T0, email at T0+6h, or the reverse.

**Invariant:** first qualifying communication starts the one window; later channels do not reset or extend it.

**Disposition:** `NEEDS_WORKING_DELTA`.

## OPS-PT-203 — Notice is delivered but no governed retain/refund choice can be exercised

Examples include a notice omitting the choice, materially wrong choice terms, or no governed way to record either choice.

**Invariant:** technically delivered information is not automatically the `DEC-308` communication event. No-response expiry cannot rely on a clock that began before the governed choice could be exercised.

**Disposition:** `NEEDS_WORKING_DELTA`.

## OPS-PT-204 — Qualifying communication occurs but participant never opens/reads it

**Invariant:** open/read/view telemetry must not be required by implementation convention. Otherwise the window could remain open indefinitely because telemetry may be unavailable, blocked or participant-controlled.

**Disposition:** `PASS_WITH_REFINEMENT`.

## OPS-PT-205 — First attempt fails; later attempt is first qualifying communication

**Invariant:** a known failed/bounced attempt does not start the window; the later first qualifying communication does. Retry identity does not create multiple windows.

**Disposition:** `PASS_WITH_REFINEMENT`.

## OPS-PT-206 — Crash/retry replays initial communication after window start

**Invariant:** replay does not create a new period; the original start/deadline survive restart.

**Disposition:** `PASS` → JIT idempotency/crash proof.

## OPS-PT-207 — Wrong destination/participant or materially wrong governed content

**Invariant:** provider “delivered” cannot cure invalid destination, stale source outcome, wrong participant or materially wrong choice terms. Such delivery cannot start the participant's Product clock.

**Disposition:** `PASS_WITH_REFINEMENT`.

## OPS-PT-208 — Valid participant choice precedes later duplicate/secondary communication

**Invariant:** explicit retain/refund choice terminates the no-response window; later retries/reminders cannot reopen it.

**Disposition:** `PASS`.

## OPS-PT-209 — Reminder fails or occurs near the deadline

**Invariant:** reminders are inside the same existing window. Reminder failure does not reset the Product clock; cadence/provider behaviour remains `OQ-017`/`OQ-036`.

**Disposition:** `PASS`.

## OPS-PT-210 — No choice at deadline; refund execution delayed or ambiguous

**Invariant:** expiry creates the automatic refund/component-close obligation. Provider refund execution timing does not extend or reopen the expired choice window; Commerce reconciles later provider truth under its own authority.

**Disposition:** `PASS_WITH_REFINEMENT`.

---

# 132. Narrowed upstream decision surface

`OPS-UPD-007` / `OPS-GAP-020` is now limited to:

1. the exact participant-facing semantic event that means NewYou has communicated the governed decision and retain-or-refund choice;
2. whether qualifying communication requires both correct decision/choice content and a currently available governed way to record either choice;
3. the Product-level handoff/delivery class, without using internal intent creation, queue insertion or raw provider acceptance by convenience;
4. first-qualifying-channel semantics for multi-channel delivery while preserving one window;
5. explicit non-control by open/read/view telemetry;
6. confirmation that no-choice expiry fixes the refund/close obligation even if Commerce/provider execution occurs later.

No new upstream delta is justified.

---

# 133. Recommended minimum promotion shape — not authority

> The single 14-day General Wellness retain-or-refund window starts exactly once when the current governed `general_wellness_only` decision and the correct retain-or-refund choice first cross a **qualifying participant-facing communication boundary**. A communication qualifies only when the decision/choice are correct for that participant, directed through an authorised participant-facing channel or surface, and a governed path exists to record either choice. Internal eligibility finalisation, communication-intent/outbox/job creation, queue insertion, raw provider acceptance, known failed/bounced attempts, and open/read/view telemetry do not by themselves start the Product clock. For multiple channels, the first qualifying communication starts the single window; later channels, retries and reminders do not reset or extend it. Channel-specific evidence satisfying the qualifying handoff boundary is defined downstream under Communications JIT / `OQ-036`; reminder execution remains `OQ-017`. A valid participant choice terminates the window. If no choice is recorded by the deadline, the automatic refund and component-entitlement-close obligation becomes due at that deadline; later provider refund execution/reconciliation does not reopen the choice window.

This recommendation does not require email, in-app or any specific provider status and does not change the 14-day duration.

---

# 134. Working locks added by this pass

1. `general_wellness_only` outcome finalisation and choice-window start are distinct.
2. Internal communication obligation creation/queueing is not participant communication.
3. Raw provider acceptance is not automatically the Product-level clock-start event.
4. Known failed/bounced communication does not start the window.
5. Open/read/view telemetry is non-controlling by default and must not become Product authority by implementation convention.
6. The governed decision and retain-or-refund choice must be part of the qualifying communication.
7. A governed way to record either choice must exist when the communication qualifies.
8. First qualifying communication starts the one window; second channel, retries and reminders do not reset/extend it.
9. A valid participant choice terminates the no-response window; stale communications cannot reopen it.
10. Reminder failure does not reset the Product clock.
11. No-choice expiry creates the refund/close obligation independently of provider refund execution timing.
12. `OQ-017` and `OQ-036` remain downstream.

---

# 135. Downstream only after `OPS-UPD-007` is resolved

JIT/proof may then choose the smallest mechanism for:

- authoritative start instant/deadline representation;
- owner-Domain choice transition and current-state guards;
- Communications handoff evidence mapping per authorised channel;
- retry/replay/multi-channel idempotency;
- wrong-destination/content suppression;
- stale reminder suppression after choice;
- reminder cadence/failure under `OQ-017`;
- provider/channel semantics under `OQ-036`;
- crash/restart recovery and exact-deadline concurrency proof;
- Commerce automatic-refund command/reconciliation;
- Entitlements component closeout;
- participant-facing status projection.

Do not create a new General Wellness, Timer, Reminder or Operations Domain merely to hold the clock.

---

# 136. Pass convergence

```text
SEMANTIC PRESSURE TESTS ADDED: OPS-PT-199...210
CUMULATIVE PRESSURE TESTS: 210
NEW OPS-UPD: 0
NEW OPS-GAP: 0
OPS-UPD-007: CONFIRMED + NARROWED
OPS-GAP-020: OPEN / SAME SEMANTIC CLASS
DEC-308 / PRODUCT §21T.4: REUSED, NOT REWRITTEN
OUTCOME FINALISATION VS WINDOW START: SEPARATED
INTERNAL INTENT / QUEUE / PROVIDER ACCEPTANCE VS QUALIFYING COMMUNICATION: SEPARATED
OPEN/READ TELEMETRY: NON-CONTROLLING BY DEFAULT
MULTI-CHANNEL / RETRY / REMINDER: ONE WINDOW / NO RESET
NO-CHOICE DEADLINE VS REFUND EXECUTION: SEPARATED
OQ-017: PRESERVED AS DOWNSTREAM REMINDER DESIGN
OQ-036: PRESERVED AS DOWNSTREAM PROVIDER/CHANNEL POLICY
IMPLEMENTATION: NOT AUTHORISED
AUTHORITY MODIFICATION: NONE
PR: NONE
FOCUSED PASS: CONVERGED
BROAD PRE-JIT FREEZE: STILL BLOCKED BY EXISTING UPSTREAM DELTAS + REQUIRED REVIEW/PROMOTION
```

This completes focused semantic pressure-testing of the current seven `OPS-UPD-001...007` classes. Do not automatically create `OPS-UPD-008` or continue scenario expansion. The next approved step should be a separate convergence/upstream-promotion review over `OPS-UPD-001...007`, unless new evidence, contradiction or scope change reopens discovery.