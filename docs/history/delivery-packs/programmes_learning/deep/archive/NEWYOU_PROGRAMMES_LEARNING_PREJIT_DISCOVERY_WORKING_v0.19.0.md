# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.19.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Pass:** Pass 18 — concurrency / retry / reordering semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.18.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE

> Passes 1–17 are accepted `WORKING_LOCKED / NON-AUTHORITATIVE`. Retry, duplicate execution and reordering do not suspend the one-owner rule.

## Scope
Semantic-only pass for duplicate/simultaneous commands, idempotency, conflicting transitions, crash/restart, durable consequence recovery, stale work, reordered source evidence and replay provenance. Exact locks/indexes/Ash actions/idempotency-key formats/Oban settings/outbox/provider mechanics and cancellation/transfer policy remain downstream.

## Authority evidence
| ID | Evidence |
|---|---|
| PRG-EV-281 | Live authority baseline reconfirmed |
| PRG-EV-282 | Architecture defines three consequence classes |
| PRG-EV-283 | Concurrency control is selected by the invariant |
| PRG-EV-284 | Transactions stay short and coherent |
| PRG-EV-285 | Authoritative actions must survive duplicate and concurrent execution |
| PRG-EV-286 | Important repeated external mutation needs durable business idempotency |
| PRG-EV-287 | Must-not-lose consequences use durable intent plus repeat-safe execution |
| PRG-EV-288 | Queue uniqueness is not business idempotency |
| PRG-EV-289 | Retries and backlog recovery are bounded operational concerns |
| PRG-EV-290 | Dynamic programme schedules remain business state |
| PRG-EV-291 | Provider duplicate/reordered delivery is normal evidence |
| PRG-EV-292 | PubSub/realtime observations may be missing, duplicated or reordered |
| PRG-EV-293 | Cross-domain writes remain owner-mediated under concurrency |
| PRG-EV-294 | Cross-domain durable consequences already use owner-specific handoff |
| PRG-EV-295 | Programmes and source evidence have distinct owners under races |
| PRG-EV-296 | Pass 17 established owner-mediated correction plus downstream reconciliation |
| PRG-EV-297 | Pass 14 already identified duplicate occurrence/check-in submission as correctness-sensitive |
| PRG-EV-298 | Pass 16 already identified duplicate source observations and provider retries |
| PRG-EV-299 | Historical/provenance truth must survive retries |
| PRG-EV-300 | Existing Architecture and Domain Law are sufficient for this seam |

## Locked semantic model
- Owning Domain controls the business command/effect; HTTP/jobs/provider attempts are execution only; source evidence remains with its source owner; PubSub/Analytics/cache/dashboard state is observation only.
- Business idempotency prevents duplicate durable semantic effects; transport exactly-once is not assumed.
- Current owner state/version/lifecycle/effective time determines ordering, never generic arrival order.
- Must-not-lose cross-domain consequences use durable intent plus repeat-safe owner-mediated reconciliation; no shared-write rollback.

## Pressure tests
| ID | Test | Disposition |
|---|---|---|
| PRG-PT-727 | Duplicate completion command arrives twice | PASS / JIT PROOF |
| PRG-PT-728 | Two nodes submit completion simultaneously | PASS / JIT PROOF |
| PRG-PT-729 | Same idempotency identity is reused with different payload | REJECT SILENT COLLAPSE |
| PRG-PT-730 | Two different command identities request the same already-reached target state | PASS / OWNER SEMANTICS |
| PRG-PT-731 | Completion commit succeeds but response is lost and client retries | PASS / JIT PROOF |
| PRG-PT-732 | Process crashes before authoritative commit | PASS |
| PRG-PT-733 | Process crashes after authoritative commit but before mandatory downstream consequence | PASS / JIT PROOF |
| PRG-PT-734 | Downstream owner commits consequence, acknowledgement is lost, and caller retries | PASS / JIT PROOF |
| PRG-PT-735 | Programme release event is observed twice by worker infrastructure | PASS / JIT PROOF |
| PRG-PT-736 | Old release job executes after Edition postponement | PASS |
| PRG-PT-737 | Release job executes before effective release due to scheduler race | REJECT EARLY EFFECT |
| PRG-PT-738 | Release transition becomes effective while worker is delayed | PASS / JIT |
| PRG-PT-739 | Safety restriction and Programme release race | PASS / JIT PROOF |
| PRG-PT-740 | Entitlement revocation races Enrolment activation | PASS |
| PRG-PT-741 | Enrolment pause and completion submission race | PASS / JIT PROOF |
| PRG-PT-742 | Abandon and complete commands race | PASS / JIT PROOF |
| PRG-PT-743 | Operator correction races participant submission | PASS / JIT PROOF |
| PRG-PT-744 | HJP occurrence arrives after Programme already evaluated window as missed | PASS |
| PRG-PT-745 | Duplicate HJP occurrence submission is consumed twice by Programmes | REJECT DUPLICATE EFFECT |
| PRG-PT-746 | HJP correction invalidates evidence while Programme reconciliation job is retried | PASS / JIT PROOF |
| PRG-PT-747 | Event attendance arrives before Programme link projection is refreshed | PASS |
| PRG-PT-748 | Event attendance correction and Programme completion race | PASS / GAP-002 |
| PRG-PT-749 | Content withdrawal races lesson delivery/release | PASS / PRG-GAP-011 BOUNDARY |
| PRG-PT-750 | Translation correction arrives after locale-specific delivery job was queued | PASS |
| PRG-PT-751 | Communication provider retries the same Programme reminder multiple times | PASS |
| PRG-PT-752 | Provider callbacks arrive out of order | PASS |
| PRG-PT-753 | PubSub signal is lost after authoritative completion commit | PASS |
| PRG-PT-754 | PubSub sends duplicate completion signal | PASS |
| PRG-PT-755 | Analytics sees event B before event A | PASS |
| PRG-PT-756 | Bulk backfill/reconciliation worker crashes halfway | PASS / JIT PROOF |
| PRG-PT-757 | Two reconciliation workers pick the same stale item | PASS / JIT PROOF |
| PRG-PT-758 | Retry storm follows shared provider outage | PASS / ARCHITECTURE |
| PRG-PT-759 | A stale operator form submits after a newer owner transition | PASS |
| PRG-PT-760 | Old correction replay arrives after a newer correction | PASS / JIT PROOF |
| PRG-PT-761 | Same historical source event is replayed during disaster recovery | PASS / JIT PROOF |
| PRG-PT-762 | Retry changes the effective timestamp to “now” | REJECT |
| PRG-PT-763 | Certificate issuance job retries after certificate already exists | PASS / GAP-002 |
| PRG-PT-764 | Concurrent language change and scheduled message render | PASS / JIT |
| PRG-PT-765 | Concurrent deletion/de-link request and Programme evidence reconciliation | PASS / PRG-GAP-007 BOUNDARY |
| PRG-PT-766 | System proposes a global distributed lock/event bus to make all Programme operations “exactly once” | REJECT / DEFER_YAGNI |

## Gap adjudication
- `PRG-GAP-002` remains open for post-award certificate/outcome consequence.
- `PRG-GAP-003` remains separate; cancellation/transfer/refund is Pass 19.
- `PRG-GAP-007` remains separate; retry/reconciliation cannot decide retention/de-link policy.
- `PRG-GAP-009` remains semantically resolved; exact conflict/idempotency representation remains JIT.
- `PRG-GAP-011` remains separate; stale-work suppression cannot decide withdrawn-content replacement.
- No new Product, Architecture, Domain, `PRG-GAP` or `PRG-UPD` is justified.

## Refinements
| ID | Refinement |
|---|---|
| PRG-REF-227 | Separate logical command, execution attempt and observation identity |
| PRG-REF-228 | Define idempotency by business effect |
| PRG-REF-229 | Duplicate identical command converges on existing/current owner truth |
| PRG-REF-230 | Same idempotency identity with materially different intent is a conflict |
| PRG-REF-231 | Concurrency protection belongs at the owner boundary |
| PRG-REF-232 | Arrival order is never generic business ordering |
| PRG-REF-233 | Retries re-read current preconditions |
| PRG-REF-234 | Mandatory cross-domain consequence requires durable recoverable intent where it must not be lost |
| PRG-REF-235 | Each owner makes its own effect idempotent |
| PRG-REF-236 | Partial cross-domain success is reconciled, not destructively rolled back across owners |
| PRG-REF-237 | Crash/restart convergence is derived from durable truth |
| PRG-REF-238 | Terminal owner states reject stale reopening unless lifecycle explicitly permits it |
| PRG-REF-239 | Correction races use Pass-17 owner-mediated semantics |
| PRG-REF-240 | Source-evidence reconciliation into Programme meaning is repeat-safe |
| PRG-REF-241 | Downstream communication/certificate/projection retries cannot multiply Programme truth |
| PRG-REF-242 | Backfills and repair jobs obey the same invariants as live paths |
| PRG-REF-243 | Observability is required but not authority |
| PRG-REF-244 | Exact locks, constraints, idempotency keys, Oban uniqueness/backoff and worker topology remain JIT/proof |

## Disposition
**PASS WITH NON-BLOCKING REFINEMENTS.**

1. Passes 1-17 remain accepted/working-locked and Pass 18 does not reopen them.
2. Programmes concurrency semantics are governed by current Architecture and existing owner boundaries; no new event model or authority layer is introduced.
3. Critical owner invariants must survive duplicate, simultaneous, reordered, retried and partially failed execution.
4. Business idempotency is defined by durable effect, not by transport/job exactly-once delivery.
5. Logical business command/effect identity is distinct from job/provider attempt identity and from PubSub/Analytics observation identity.
6. Repeating the same logical command after uncertain acknowledgement must converge on durable owner truth without multiplying semantic effects.
7. Reusing one idempotency identity for materially different intent must be rejected or explicitly conflicted, not silently coalesced.
8. Concurrency control is selected per owning invariant; no universal lock/optimistic scheme is frozen by this pass.
9. Owner-side lifecycle/state guards determine the winner of conflicting transitions; last arrival/last UI response is not a generic business rule.
10. Arrival order of jobs, provider callbacks, PubSub signals or Analytics events never becomes durable Programme ordering authority.
11. Must-not-lose asynchronous consequences require durable recoverable intent and repeat-safe execution with current precondition revalidation.
12. Oban/job uniqueness may suppress duplicate execution but cannot replace owner-level business idempotency.
13. Stale queued work cannot outrank current Programme, Content, Safety, Entitlement, HJP, Events or Communications authority.
14. Partial cross-domain success is recovered through owner-mediated retry/reconciliation, not shared-write rollback across Domains.
15. Each authoritative Domain protects its own durable effect; cross-domain orchestration does not create a global transaction owner.
16. Crash/restart recovery derives required work from durable truth/intent, not process memory or best-effort observations.
17. PubSub is observation only; lost/duplicate/reordered PubSub cannot create or destroy Programme truth.
18. Repeated source-evidence reconciliation from HJP/Events/Safety/Content/Entitlements/Communications must converge without duplicate Programme consequences.
19. Correction races retain Pass-17 owner-mediated correction/provenance semantics; stale operator forms do not bypass current owner checks.
20. Historical effective time/source/version/actor provenance is preserved across retries and replay; retry does not rewrite history to “now”.
21. Certificate/message/projection retries cannot multiply Programme completion or participant action. Post-award reversal/reissue remains PRG-GAP-002.
22. PRG-GAP-003, PRG-GAP-007 and PRG-GAP-011 remain separate business/lifecycle seams; Pass 18 does not resolve them through concurrency mechanics.
23. PRG-GAP-009 remains semantically resolved; concurrency implementation for owner actions is representation/JIT proof, not a reopened admin-authority gap.
24. Exact indexes/constraints/locks/idempotency keys/Oban options/retry budgets/worker topology remain downstream JIT/proof.
25. No new Product, Architecture, Domain, PRG-GAP or PRG-UPD is justified; generic event-sourcing/saga/distributed-lock/concurrency platforms remain DEFER_YAGNI.

**YAGNI:** no global event store/event-sourcing mandate, exactly-once transport layer, distributed lock, generic saga/workflow engine, generic outbox by fashion, Redis/GenServer authority, shared cross-domain transaction or new concurrency Domain/Feature Pack.

**Pass hard stop:** Pass 19 — cancellation / transfer semantics — has not started. Later historical reproducibility, analytics, FP-014 second-lens and final adversarial convergence remain separate.
