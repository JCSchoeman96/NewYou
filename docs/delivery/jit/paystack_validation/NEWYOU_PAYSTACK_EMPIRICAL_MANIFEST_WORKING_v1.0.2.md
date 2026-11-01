# NewYou Paystack Empirical Manifest — Working v1.0.2

- **Status:** WORKING / NON-AUTHORITATIVE / OPERATIONAL EXECUTION ROUTING PROJECTION
- **Repository baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Execution status:** **NO STAGE EXECUTED** — zero empirical stage results are recorded as PASS/FAIL/INCONCLUSIVE.
- **Stage-result summary:** cases with any executed stage `0 / 59`; fully satisfied cases `0 / 59`; executed stage slots `0 / 85`.
- **Routing predecessor:** `NEWYOU_PAYSTACK_EMPIRICAL_MANIFEST_WORKING_v1.0.1.md`
- **Semantic contract:** `NEWYOU_PAYSTACK_PREJIT_CONTRACT_WORKING_v1.0.0.md` (unchanged by this stage-result recording patch)
- **Detailed case-definition source:** `deep/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.11.0.md`

## 1. Routing model: Wave ≠ Execution Stage ≠ Gate Effect

These are orthogonal dimensions:

- **Wave** is risk/dependency execution order. It says what to attack first, not where a proof belongs in governance.
- **Execution Stage** says which environment/lifecycle may truthfully execute the proof.
- **Gate Effect** says what the result may block. A release-only case does not become an internal Phase-8 blocker merely because it appears in an earlier risk wave.

Allowed execution-stage labels used here:

- `PRE_JIT_PROVIDER_SANDBOX` / `...IF_SUPPORTED` / `...IF_REPRODUCIBLE` — provider-mechanics learning that can be performed before the NewYou application exists.
- `PRE_JIT_HARNESS_SANITY` — proves the temporary fault/test harness itself does not manufacture the behavior being studied.
- `PHASE8_ACTUAL_HTTP_STACK` — must be rerun against the selected Elixir HTTP client, middleware and proxy configuration; a curl/Python harness cannot satisfy this stage.
- `PHASE8_NEWYOU_PROOF` — executable Commerce/Entitlements/NewYou behavior is required.
- `PHASE8_*` — executable NewYou proof in the named seam, including actual HTTP stack, adapter, configuration, reconciliation, Privacy/Audit, security and Finance contracts.
- `RELEASE_*` — controlled-live/account/runbook evidence required before paid release, but not a substitute for Phase-8 proof and not necessarily required before safe internal implementation/proof work.
- `FUTURE_RECURRING` — outside FP-002 and does not block its one-off outcome.

## 2. Exact case-definition locator rule

Before executing any case, load its exact `### PAYSTACK-EV-...` definition from `deep/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.11.0.md` **unless the full setup/PASS/FAIL definition has been promoted into this manifest**. Do not invent a setup from the one-line purpose.

Routing precedence for execution is:

1. current compact semantic contract (`v1.0.0`) for effective invariants;
2. this `v1.0.2` manifest for **Execution Stage / Gate Effect / stage-result recording / wave routing**;
3. deep `v0.11.0` ledger for the detailed case procedure and provenance.

If the deep case procedure conflicts with the current compact contract, or lacks enough detail to execute reproducibly, **STOP and patch the working proof artifact** rather than silently reinterpret it.

## 3. Stage-result recording contract

A case may have one or more execution stages. **Results are recorded per stage, never as one lossy case-level status.**

Allowed current stage dispositions are:

- `NOT_EXECUTED` — no qualifying execution evidence has been accepted for this stage;
- `PASS` — the stage-specific PASS contract is satisfied by recorded evidence;
- `FAIL` — accepted evidence demonstrates a stage-specific failure and the threatened gate remains unresolved;
- `INCONCLUSIVE` — the stage was attempted but the evidence cannot establish PASS or FAIL;
- `GOVERNED_NA` — an authorised governance decision establishes that this stage is not applicable to the selected scope. This value requires an explicit authority/evidence reference and must never be inferred for convenience.

The matrix stores the **current stage disposition**. It does not erase execution history: every individual run and superseding result must remain in the empirical evidence record/index. A later PASS after a prior FAIL changes the current stage disposition only when the underlying defect has been corrected and the stage PASS contract is rerun successfully; the earlier failed run remains historical evidence.

A stage result never promotes another stage. In particular:

- `PRE_JIT_* = PASS` does not imply any `PHASE8_*` or `RELEASE_*` PASS;
- `PHASE8_* = PASS` does not imply `RELEASE_*` PASS;
- a multi-stage case is **fully satisfied** only when every stage applicable to the current declared scope/gate is `PASS` or explicitly `GOVERNED_NA`;
- gate evaluation is stage-aware. Do not mark a gate satisfied merely because another stage in the same case passed.

### Summary-counting rules

Do not report a multi-stage catalogue as simply “executed/not executed.” Report at minimum:

- **Cases with any executed stage** — a case counts when at least one stage is `PASS`, `FAIL`, or `INCONCLUSIVE`;
- **Fully satisfied cases** — a case counts only when every stage applicable to the declared scope is `PASS` or `GOVERNED_NA`;
- **Executed stage slots** — count stage dispositions of `PASS`, `FAIL`, or `INCONCLUSIVE` against the total defined stage slots;
- list any partially executed case by exact case ID + stage + disposition.

At this version: `0 / 59` cases have any executed stage; `0 / 59` cases are fully satisfied; `0 / 85` stage slots have an executed result.

## 3A. Evidence required for every executed stage

Every run must capture enough evidence to distinguish provider observation from NewYou truth:
- exact validation case ID;
- exact execution stage being evaluated;
- environment (`test` / controlled `live` where authorised);
- execution timestamp/window;
- NewYou Purchase Intent / Provider Attempt / Refund Intent identity as applicable;
- Paystack reference and transaction/refund/dispute/event IDs where available;
- exact request class and redacted request metadata;
- response status/body class and timing;
- induced fault and where it occurred;
- webhook/event delivery evidence when relevant;
- follow-up Verify/List/Fetch evidence;
- authoritative Commerce transition(s);
- Entitlements consequence(s);
- restart/checkpoint evidence where relevant;
- expected vs actual;
- stage result: `PASS`, `FAIL`, or `INCONCLUSIVE`;
- failure interpretation and threatened invariant/gate;
- redacted attachments/logs.

Secrets, PAN, CVV, reusable authorization codes and unnecessary sensitive participant data are never evidence artifacts.

## 4. Case routing matrix

| Case | Purpose | Wave | Execution stage | Gate effect | Stage results |
|---|---|---:|---|---|---|
| `PAYSTACK-EV-001` | Ambiguous Initialize timeout and Verify visibility | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-001A` | Initialize accepted / response lost before NewYou receives capability | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-001B` | Initialize response retained / browser response lost | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-001C` | Old payable capability remains live while participant retries checkout | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-002` | Duplicate Initialize same reference | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-009` | Provider status progression and session expiry | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-009A` | `abandoned` before/around session expiry | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-009B` | Documented payment-session timeout replacement | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-041` | Provider reference compatibility and opacity | `1` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-050` | Hidden automatic retry of Initialize | `1` | `PRE_JIT_HARNESS_SANITY + PHASE8_ACTUAL_HTTP_STACK` | `BLOCKS_PREJIT_HARNESS_TRUST + BLOCKS_PHASE8_ACTUAL_INTEGRATION_PROOF` | `PRE_JIT_HARNESS_SANITY=NOT_EXECUTED`<br>`PHASE8_ACTUAL_HTTP_STACK=NOT_EXECUTED` |
| `PAYSTACK-EV-003` | Browser return before/after webhook and browser loss | `2` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_FP002_OUTCOME` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-004` | Webhook duplicate/resend | `2` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_FP002_OUTCOME` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-005` | Webhook transient 500 / outage / acknowledgement boundary | `2` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_FP002_OUTCOME` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-006` | Forged and replayed webhook | `2` | `PHASE8_NEWYOU_PROOF` | `BLOCKS_PHASE8_PROOF` | `PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-021` | Webhook signed-payload handling | `2` | `PHASE8_ACTUAL_HTTP_STACK` | `BLOCKS_PHASE8_PROOF` | `PHASE8_ACTUAL_HTTP_STACK=NOT_EXECUTED` |
| `PAYSTACK-EV-037` | Webhook event-ID availability and dedupe evidence | `2` | `PRE_JIT_PROVIDER_SANDBOX` | `SUPPORTING_EVIDENCE_NOT_INDEPENDENT_BLOCKER` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-007` | Success with no usable webhook | `2` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_RECONCILIATION_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_FP002_OUTCOME` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_RECONCILIATION_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-014` | Restart after provider success before Commerce reconciliation | `2` | `PHASE8_NEWYOU_PROOF` | `BLOCKS_FP002_OUTCOME` | `PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-008` | Amount/currency/reference mismatch rejection | `3` | `PHASE8_NEWYOU_PROOF` | `BLOCKS_PHASE8_PROOF` | `PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-018` | `amount` vs `requested_amount` integrity / Partial Debit exclusion | `3` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_ADAPTER_CONTRACT` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_PHASE8_PROOF` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_ADAPTER_CONTRACT=NOT_EXECUTED` |
| `PAYSTACK-EV-019` | Customer fee pass-through configuration guard | `3` | `PHASE8_CONFIGURATION_PROOF + RELEASE_CONFIRMATION` | `BLOCKS_PHASE8_PROOF + BLOCKS_PAID_RELEASE` | `PHASE8_CONFIGURATION_PROOF=NOT_EXECUTED`<br>`RELEASE_CONFIRMATION=NOT_EXECUTED` |
| `PAYSTACK-EV-020` | Enabled-channel validation matrix | `3` | `PRE_JIT_PROVIDER_SANDBOX_PER_CHANNEL + RELEASE_CONFIRMATION` | `BLOCKS_CHANNEL_ADMISSION` | `PRE_JIT_PROVIDER_SANDBOX_PER_CHANNEL=NOT_EXECUTED`<br>`RELEASE_CONFIRMATION=NOT_EXECUTED` |
| `PAYSTACK-EV-024` | Two genuine successful Paystack refs for one one-off Purchase Intent | `3` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_FP002_OUTCOME` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-010` | Refund Create timeout / duplicate request ambiguity | `4` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-025` | Refund Create timeout reconciliation | `4` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_RECONCILIATION_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_FP002_OUTCOME` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_RECONCILIATION_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-051` | Hidden automatic retry of Create Refund | `4` | `PRE_JIT_HARNESS_SANITY + PHASE8_ACTUAL_HTTP_STACK` | `BLOCKS_PREJIT_HARNESS_TRUST + BLOCKS_PHASE8_ACTUAL_INTEGRATION_PROOF` | `PRE_JIT_HARNESS_SANITY=NOT_EXECUTED`<br>`PHASE8_ACTUAL_HTTP_STACK=NOT_EXECUTED` |
| `PAYSTACK-EV-011` | Full and partial refund lifecycle | `4` | `PRE_JIT_PROVIDER_SANDBOX` | `BLOCKS_PROVIDER_MECHANICS_FREEZE` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED` |
| `PAYSTACK-EV-026` | Concurrent duplicate partial-refund creation | `4` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_PHASE8_PROOF` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-027` | Multiple authorised partial refunds and cumulative amount | `4` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_PHASE8_PROOF` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-028` | Refund failed after pending/processing | `4` | `PRE_JIT_PROVIDER_SANDBOX_IF_REPRODUCIBLE + RELEASE_CONTROLLED_LIVE_IF_REQUIRED` | `BLOCKS_REFUND_PATH_ADMISSION_OR_RELEASE` | `PRE_JIT_PROVIDER_SANDBOX_IF_REPRODUCIBLE=NOT_EXECUTED`<br>`RELEASE_CONTROLLED_LIVE_IF_REQUIRED=NOT_EXECUTED` |
| `PAYSTACK-EV-048` | Partial refund + transaction `reversed` status | `4` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_ADAPTER_CONTRACT` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_PHASE8_PROOF` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_ADAPTER_CONTRACT=NOT_EXECUTED` |
| `PAYSTACK-EV-029` | Needs-attention refund in South African test/live-confirmable path | `4` | `PRE_JIT_PROVIDER_SANDBOX_IF_AVAILABLE + RELEASE_CONTROLLED_LIVE_IF_REQUIRED` | `BLOCKS_PAID_RELEASE_FOR_AFFECTED_PATH` | `PRE_JIT_PROVIDER_SANDBOX_IF_AVAILABLE=NOT_EXECUTED`<br>`RELEASE_CONTROLLED_LIVE_IF_REQUIRED=NOT_EXECUTED` |
| `PAYSTACK-EV-053` | Insufficient Paystack balance on owed refund | `4` | `PHASE8_FINANCE_CONTRACT + RELEASE_OPERATIONS_FINANCE` | `BLOCKS_PHASE8_CORRECTION_PROOF + BLOCKS_PAID_RELEASE` | `PHASE8_FINANCE_CONTRACT=NOT_EXECUTED`<br>`RELEASE_OPERATIONS_FINANCE=NOT_EXECUTED` |
| `PAYSTACK-EV-013` | Dispute event/API lifecycle | `5` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED + RELEASE_CONTROLLED_LIVE_IF_REQUIRED` | `BLOCKS_DISPUTE_PATH_ADMISSION_OR_RELEASE` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED=NOT_EXECUTED`<br>`RELEASE_CONTROLLED_LIVE_IF_REQUIRED=NOT_EXECUTED` |
| `PAYSTACK-EV-030` | Dispute detection without webhook | `5` | `RELEASE_ONLY` | `BLOCKS_PAID_RELEASE_NOT_INTERNAL_PROOF` | `RELEASE_ONLY=NOT_EXECUTED` |
| `PAYSTACK-EV-032` | Dispute create/remind/resolve duplicate/reorder | `5` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED + PHASE8_NEWYOU_PROOF` | `BLOCKS_PHASE8_PROOF` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-033` | Old charge.success resend after refund/dispute finality | `5` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_FP002_OUTCOME` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-012` | Reordered old success after refund/reversal | `5` | `PHASE8_NEWYOU_PROOF` | `BLOCKS_FP002_OUTCOME` | `PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-046` | Refund/dispute collision | `5` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED + PHASE8_NEWYOU_PROOF` | `BLOCKS_PROVIDER_MECHANICS_FREEZE + BLOCKS_PHASE8_PROOF` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-049` | Partial final dispute / component non-identity | `5` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED + PHASE8_NEWYOU_PROOF + RELEASE_CONFIRMATION_IF_REQUIRED` | `BLOCKS_PHASE8_PROOF + BLOCKS_PAID_RELEASE_IF_LIVE_CONFIRMATION_REQUIRED` | `PRE_JIT_PROVIDER_SANDBOX_IF_SUPPORTED=NOT_EXECUTED`<br>`PHASE8_NEWYOU_PROOF=NOT_EXECUTED`<br>`RELEASE_CONFIRMATION_IF_REQUIRED=NOT_EXECUTED` |
| `PAYSTACK-EV-054` | Dispute evidence minimisation | `5` | `PHASE8_PRIVACY_AUDIT_CONTRACT` | `BLOCKS_PRIVACY_AUDIT_READINESS` | `PHASE8_PRIVACY_AUDIT_CONTRACT=NOT_EXECUTED` |
| `PAYSTACK-EV-043` | Provider outage with in-flight checkout | `6` | `PHASE8_NEWYOU_PROOF` | `BLOCKS_FP002_OUTCOME` | `PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-044` | Verification rate limit/backlog | `6` | `PHASE8_RECONCILIATION_PROOF` | `BLOCKS_FP002_OUTCOME` | `PHASE8_RECONCILIATION_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-042` | Manual Finance correction cannot bypass Commerce | `6` | `PHASE8_NEWYOU_PROOF` | `BLOCKS_PHASE8_PROOF` | `PHASE8_NEWYOU_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-055` | Reconciliation scan completeness under pagination/restart/429 | `6` | `PHASE8_RECONCILIATION_PROOF` | `BLOCKS_FP002_OUTCOME` | `PHASE8_RECONCILIATION_PROOF=NOT_EXECUTED` |
| `PAYSTACK-EV-052` | Unknown provider vocabulary/schema evolution | `6` | `PHASE8_ADAPTER_CONTRACT` | `BLOCKS_PHASE8_ROBUST_INTEGRATION_PROOF` | `PHASE8_ADAPTER_CONTRACT=NOT_EXECUTED` |
| `PAYSTACK-EV-015` | Test/live boundary confirmation | `7` | `RELEASE_CONTROLLED_LIVE` | `BLOCKS_PAID_RELEASE` | `RELEASE_CONTROLLED_LIVE=NOT_EXECUTED` |
| `PAYSTACK-EV-022` | Secret-key rotation with webhook retry overlap | `7` | `RELEASE_CONTROLLED_LIVE` | `BLOCKS_PAID_RELEASE` | `RELEASE_CONTROLLED_LIVE=NOT_EXECUTED` |
| `PAYSTACK-EV-031` | South Africa dispute deadline contract confirmation | `7` | `RELEASE_ONLY` | `BLOCKS_PAID_RELEASE` | `RELEASE_ONLY=NOT_EXECUTED` |
| `PAYSTACK-EV-036` | Hosted Checkout card-data boundary | `7` | `PHASE8_SECURITY_PROOF + RELEASE_CONFIRMATION` | `BLOCKS_PAID_RELEASE` | `PHASE8_SECURITY_PROOF=NOT_EXECUTED`<br>`RELEASE_CONFIRMATION=NOT_EXECUTED` |
| `PAYSTACK-EV-038` | Settlement independence from payment/access | `7` | `RELEASE_CONTROLLED_LIVE` | `BLOCKS_PAID_RELEASE` | `RELEASE_CONTROLLED_LIVE=NOT_EXECUTED` |
| `PAYSTACK-EV-039` | Settlement transaction membership and correction deductions | `7` | `RELEASE_OPERATIONS_FINANCE` | `BLOCKS_PAID_RELEASE` | `RELEASE_OPERATIONS_FINANCE=NOT_EXECUTED` |
| `PAYSTACK-EV-045` | Test/live evidence boundary audit | `7` | `RELEASE_ONLY` | `BLOCKS_PAID_RELEASE` | `RELEASE_ONLY=NOT_EXECUTED` |
| `PAYSTACK-EV-047` | Failed-but-debited customer evidence / bank reversal boundary | `7` | `RELEASE_SUPPORT_RUNBOOK` | `BLOCKS_PAID_RELEASE` | `RELEASE_SUPPORT_RUNBOOK=NOT_EXECUTED` |
| `PAYSTACK-EV-034` | Provider customer/email identity non-authority | `X` | `PHASE8_ADAPTER_CONTRACT` | `BLOCKS_PHASE8_PROOF` | `PHASE8_ADAPTER_CONTRACT=NOT_EXECUTED` |
| `PAYSTACK-EV-035` | Metadata minimisation | `X` | `PHASE8_PRIVACY_ADAPTER_CONTRACT + RELEASE_CONFIGURATION_CONFIRMATION` | `BLOCKS_PHASE8_PROOF + BLOCKS_PAID_RELEASE` | `PHASE8_PRIVACY_ADAPTER_CONTRACT=NOT_EXECUTED`<br>`RELEASE_CONFIGURATION_CONFIRMATION=NOT_EXECUTED` |
| `PAYSTACK-EV-040` | FP-002 reusable-authorization containment | `X` | `PRE_JIT_PROVIDER_SANDBOX + PHASE8_ADAPTER_CONTRACT` | `BLOCKS_PHASE8_PROOF` | `PRE_JIT_PROVIDER_SANDBOX=NOT_EXECUTED`<br>`PHASE8_ADAPTER_CONTRACT=NOT_EXECUTED` |
| `PAYSTACK-EV-016` | Provider-managed subscription failed cycle (future) | `FUTURE` | `FUTURE_RECURRING` | `FUTURE_ONLY_DOES_NOT_BLOCK_FP002` | `FUTURE_RECURRING=NOT_EXECUTED` |
| `PAYSTACK-EV-017` | Charge Authorization retry ambiguity (future) | `FUTURE` | `FUTURE_RECURRING` | `FUTURE_ONLY_DOES_NOT_BLOCK_FP002` | `FUTURE_RECURRING=NOT_EXECUTED` |

## 5. Wave-1 dependency gate

Wave 1 executes first because Initialize ambiguity can invalidate all later conclusions about one-off payment safety. A Wave-1 ambiguity failure is `BLOCKED / STOP`; do not accumulate green later-wave evidence to compensate.

### Wave-1 exact PASS contract

1. Provider reference/attempt identity is durable before Initialize leaves NewYou.
2. Lost Initialize response never becomes automatic failure.
3. Immediate Verify `reference not found` after ambiguous Initialize is not prematurely conclusive.
4. Same-reference repetition cannot silently create a second transaction.
5. Browser retry/reload reuses a still-valid checkout attempt.
6. Replacement reference is admitted only when the prior attempt is proven no longer payable under the accepted contract.
7. Concurrent retries cannot both win Provider Attempt admission.
8. Restart preserves reconciliation identity.
9. No provider/browser observation grants entitlement.
10. The temporary Pre-JIT fault harness emits no hidden second Initialize POST (`EV-050` harness-sanity stage).
11. Phase 8 later re-proves the same property against the actual selected Elixir HTTP client/middleware/proxy stack (`EV-050` actual-stack stage).
12. Evidence establishes a bounded safe rule for replacing an ambiguously initialised attempt.

### Wave-1 STOP conditions

- provider may have accepted Initialize yet NewYou cannot deterministically recover within an operationally safe boundary;
- NewYou must create another reference while the first may remain payable;
- ordinary retry can admit two live payable attempts;
- the Pre-JIT harness itself auto-retries an ambiguous Initialize mutation;
- the selected Phase-8 HTTP/client/proxy stack auto-retries an ambiguous Initialize mutation;
- restart loses the only reconciliation identity;
- observed Paystack behavior contradicts the documented duplicate-reference model in a way that changes safe retry semantics.

## 6. EV-050 / EV-051 two-stage PASS requirement

`EV-050` and `EV-051` are intentionally **two-stage cases**:

- **A — Pre-JIT harness sanity:** the temporary runner/fault injector must emit exactly one mutation request when the response is lost. This prevents the test harness from fabricating a retry.
- **B — Phase-8 actual-stack proof:** the selected Elixir HTTP client + middleware + proxy/infrastructure configuration must independently prove that ambiguous mutation outcomes are returned to the owning NewYou reconciliation lifecycle and are not transparently repeated.

A PASS from stage A alone **must not** be reported as proof about the eventual Phoenix/Elixir stack. `EV-050/051` are fully satisfied only when every stage applicable to the current delivery gate has passed. After stage A passes and stage B remains outstanding, record the case explicitly as `PRE_JIT_HARNESS_SANITY=PASS; PHASE8_ACTUAL_HTTP_STACK=NOT_EXECUTED`; do not collapse it to case-level `PASS`, `NOT_EXECUTED`, or `INCONCLUSIVE`.

## 7. Gate interpretation

- `BLOCKS_PROVIDER_MECHANICS_FREEZE` — the related Paystack mechanism must remain unfrozen until this provider-only evidence is satisfactory.
- `BLOCKS_PREJIT_HARNESS_TRUST` — the temporary fault harness cannot be trusted for that mutation until stage A proves it emits one request only.
- `BLOCKS_PHASE8_*` / `BLOCKS_FP002_OUTCOME` — requires executable NewYou proof and cannot be satisfied by a provider-only harness.
- `BLOCKS_CHANNEL_ADMISSION` — only channels that satisfy applicable proof may be enabled; this does not force validation of every Paystack channel.
- `BLOCKS_PAID_RELEASE*` / `RELEASE_*` — blocks paid release/readiness, **not safe internal Phase-8 proof by itself**.
- `SUPPORTING_EVIDENCE_NOT_INDEPENDENT_BLOCKER` — useful forensic evidence but business correctness must not depend on it.
- `FUTURE_ONLY_DOES_NOT_BLOCK_FP002` — preserved under global OQ-004 future scope, but does not block the one-off FP-002 path.

## 8. Closure states

Before provider mechanics + applicable Phase-8 proof are complete:

`OQ-004 / FP-002 APPLICABLE SCOPE — BLOCKED ON EMPIRICAL TESTS`

After documentary + applicable provider-mechanics + architectural/Phase-8 proof, while release-only evidence remains:

`OQ-004 / FP-002 APPLICABLE SCOPE — READY TO CLOSE FOR PHASE 7/8; RELEASE EVIDENCE REMAINS`

After applicable controlled-live/release evidence:

`OQ-004 / FP-002 APPLICABLE SCOPE — SATISFIED`

Global OQ-004 may remain open for recurring/proration scope.

## 9. Immediate execution order

Start only the **provider-only / harness-sanity portion of Wave 1** now: `EV-001/001A/001B/001C/002/009/009A/009B/041` plus `EV-050` stage A. After each run, update only the exact stage disposition supported by the evidence and leave all other stage dispositions unchanged. Do not claim the `EV-050` actual-stack stage until the selected NewYou Elixir HTTP stack exists. Do not paste Paystack secret keys into chat or evidence files; inject them through a secret/environment mechanism.
