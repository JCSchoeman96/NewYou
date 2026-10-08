# NewYou Paystack Gap Register — Working v1.0.2

- **Status:** OPEN ITEMS ONLY / NON-AUTHORITATIVE / STAGE-RESULT ROUTING PATCH
- **Repository baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Documentary research:** frozen; this is not a list of settled findings.
- **Routing authority for empirical execution:** `NEWYOU_PAYSTACK_EMPIRICAL_MANIFEST_WORKING_v1.0.2.md`

## Blocking now

| Gap | Class | Blocks | Closure evidence |
|---|---|---|---|
| Formal promotion of accepted duplicate-collection + partial-reversal Product clarification | `UPSTREAM_PRODUCT_GOVERNANCE` | FP-002 Phase 7C reliance on those semantics | reviewed/merged governed Product + Decision successor, routing/integrity evidence |
| Initialize ambiguity / safe attempt replacement | `PRE_JIT_PROVIDER_EMPIRICAL` | provider-mechanics freeze for the one-off checkout path | provider-only Wave-1 cases `EV-001/001A/001B/001C/002/009/009A/009B/041` PASS plus `EV-050` **stage A** harness sanity |
| Actual NewYou mutation transport cannot hide retries | `PHASE8_ACTUAL_STACK_PROOF` | actual integration proof | `EV-050` **stage B** and, for refunds, `EV-051` stage B against selected Elixir HTTP client/middleware/proxy stack |
| Applicable one-off NewYou integration/reconciliation programme | `PHASE8_EXECUTABLE_PROOF` | FP-002 stated outcome / applicable OQ-004 scope | all manifest cases whose Gate Effect includes `BLOCKS_PHASE8_*` or `BLOCKS_FP002_OUTCOME` PASS/explicitly governed N/A; release-only cases are excluded from this internal-proof closure |

## Open architecture/JIT proof

| Gap | Class | Closure evidence |
|---|---|---|
| Unknown provider status/event/schema handling | `ARCHITECTURAL_PROOF_REQUIRED` | `EV-052` Phase-8 synthetic adapter contract tests + fail-closed observability |
| Durable exactly-once business consequence under duplicate/reordered evidence/restart | `ARCHITECTURAL_PROOF_REQUIRED` | Commerce/Entitlements executable proof under the applicable Phase-8 cases |
| Reconciliation scan pagination/overlap/checkpoint/429 completeness | `ARCHITECTURAL_PROOF_REQUIRED` | `EV-055` Phase-8 reconciliation proof |
| Refund mutation hidden retry / timeout dedupe | `EMPIRICAL + ARCHITECTURAL_PROOF` | provider mechanics `EV-010/025` plus `EV-051` actual-stack stage and `EV-026` concurrency proof |
| Dispute evidence minimisation and sensitive-data escalation | `PRIVACY/AUDIT/LEGAL_JIT` | `EV-054` + governed Privacy/Audit/Operations contract |
| Operator/Finance correction cannot bypass Commerce | `ARCHITECTURAL/OPERATIONS_PROOF` | `EV-042` + scoped audit proof |

## Open release actions/evidence

These items block paid release/readiness as specified; they do **not** become internal Phase-8 blockers merely because they are placed in an earlier risk wave.

| Item | Class | Release impact |
|---|---|---|
| Exact FP-002 launch Paystack channel allowlist | `FEATURE_PACK / PROOF-SCOPE ACTION` | each enabled channel must pass applicable `EV-020`; recommended first candidate is card-only |
| South-African account dispute deadline/operating behavior | `RELEASE_ONLY` | `EV-031` plus applicable controlled-live dispute evidence before paid release |
| Dispute detection backstop without webhook | `RELEASE_ONLY` | `EV-030`; proves live operational detection, not internal Commerce correctness |
| Settlement/payout reconciliation | `RELEASE_ONLY / FINANCE` | `EV-038/039`; confirm live settlement mapping and Finance exception handling |
| Insufficient Paystack balance on owed refund | `PHASE8 + RELEASE / FINANCE` | `EV-053`; synthetic obligation-continuity proof in Phase 8 plus top-up/escalation runbook evidence before paid release |
| Production webhook/secret rotation/recovery runbook | `RELEASE_ONLY` | exercise controlled production path (`EV-022` and related runbook evidence) |
| Hosted Checkout card-data boundary / applicable security confirmation | `PHASE8_SECURITY + RELEASE` | `EV-036`; architecture/data-flow proof plus applicable release/compliance confirmation |
| Test/live evidence classification audit | `RELEASE_ONLY` | `EV-045`; prevents sandbox evidence from being promoted into live claims |
| OQ-035 abuse thresholds | `SEPARATE RELEASE GATE` | blocks paid pilot/public release, not documentary Paystack design |

## Open outside FP-002

These do not block the one-off FP-002 path but keep global OQ-004 open as applicable:

- `EV-016` recurring/subscription failed-payment behavior;
- `EV-017` reusable Charge Authorization retry ambiguity;
- proration;
- future channels, markets and currencies.

## Execution rule

Wave number is **not** sufficient to decide whether a case may execute or what it blocks. Before running a case:

1. read its `Execution stage` and `Gate effect` in the v1.0.2 empirical manifest;
2. load its exact case definition from the deep v0.11 ledger unless the full definition is present in the manifest;
3. execute only in an environment capable of satisfying that stage;
4. never mark a multi-stage case fully PASS from an earlier harness-only stage.

## Stage-result recording rule

The empirical manifest records result state **per execution stage**, not once per case. For a multi-stage case, a completed earlier stage must be recorded without changing outstanding later stages. Gate evaluation consumes only the stage(s) applicable to that gate.

Do not use case-level `PASS`, `NOT_EXECUTED`, `INCONCLUSIVE` or a synthetic `PARTIALLY_EXECUTED` value as a substitute for the stage dispositions in the manifest. Summary reporting must distinguish cases with any executed stage, fully satisfied cases and executed stage slots.

## Closed as documentary questions

Do **not** reopen without new evidence: Commerce/Entitlements/provider authority separation; browser non-authority; webhook signature/retry model; unique reference contract; amount/currency/reference integrity; refund/dispute lifecycle separation; settlement non-authority; reusable authorization containment; metadata/privacy direction; test/live boundary; recurring exclusion from FP-002.
