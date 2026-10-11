# NewYou Live & Replay Upstream Delta / Gap Register — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE
- **Implementation:** NOT AUTHORISED
- **Authority:** NONE
- **Accepted set:** `LIVE-UPD-001...006`, `LIVE-GAP-001...014`
- **Guard:** `LIVE-UPD-007` NOT WARRANTED; `LIVE-GAP-015` NOT WARRANTED
- **Deep source:** `deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.1.md`

This register is the primary compact home for unresolved consequential Live & Replay questions and their authority/proof routes. It does not resolve them.

## 1. Upstream working decision packages

### LIVE-UPD-001 — Stable occurrence identity and occurrence lifecycle semantics

- **Status:** OPEN / ACCEPTED_WORKING_CANDIDATE / NOT AUTHORITY.
- **Accepted working direction:** NewYou occurrence identity remains stable independently of provider room/input/resource identity. Product/Domain authority must define the minimal schedule/execution/correction/supersession boundary that distinguishes identity-preserving change from a replacement/duplicate occurrence.
- **Originating tranche:** Pass A `LIVE-PT-002...003`, reinforced by Pass B `LIVE-PT-012...019`, `LIVE-PT-029` and convergence cases.
- **Affected owner:** Events & Live principally; Communications/Content & Media/Audit consume consequences without taking ownership.
- **Why JIT cannot invent it:** occurrence identity determines registration continuity, attendance history, stale-link handling, replay association, schedule history and operator correction semantics.
- **Likely authority route:** Product Law / Events & Live Domain clarification → future FP-007 JIT.
- **Current blocker/consumer:** `LIVE-GAP-001`; future Phase 7A/7B/7C occurrence contract.

### LIVE-UPD-002 — Attendance meaning, assurance, correction and finality

- **Status:** OPEN / ACCEPTED_WORKING_CANDIDATE / NOT AUTHORITY.
- **Accepted working direction:** Events & Live owns a Product-defined attendance business fact independent of provider attendee rows. Product must determine required assurance/evidence/finality/correction semantics; no duration threshold is invented here.
- **Originating tranche:** Pass A `LIVE-PT-005...007`, reinforced by Pass B `LIVE-PT-025...027` and later deletion/analytics cases.
- **Affected owner:** Events & Live; Programmes & Challenges and Analytics consume; Identity & Access supplies canonical identity context; Audit records evidence only.
- **Why JIT cannot invent it:** the meaning affects programme participation, live-value evidence, support correction and analytics denominators.
- **Likely authority route:** Product Law → Events & Live Domain/JIT reconciliation.
- **Current blocker/consumer:** `LIVE-GAP-004`, `LIVE-GAP-010`; future FP-007 proof and later programme/membership evidence.

### LIVE-UPD-003 — Live-right versus replay-right Product semantics

- **Status:** OPEN / ACCEPTED_WORKING_CANDIDATE / NOT AUTHORITY.
- **Accepted working direction:** live access and replay access are separate rights whose source/scope/validity/expiry/revocation must be explicit by relevant product/access source. Registration or attendance never silently implies replay entitlement.
- **Originating tranche:** Pass A `LIVE-PT-009...011`, with later commercial/sponsored/public/access scenarios.
- **Affected owner:** Entitlements for current right; Events & Live/Programmes & Challenges/Content & Media as consumers/related owners; Commerce only for commercial source truth.
- **Why JIT cannot invent it:** membership cancellation, programme windows, missed sessions, sponsored/gift access and separate purchases are Product policy.
- **Likely authority route:** Product Law / entitlement semantics → FP-007 JIT.
- **Current blocker/consumer:** `LIVE-GAP-005`; replay access contract.

### LIVE-UPD-004 — In-progress live-access continuity/revocation

- **Status:** OPEN / ACCEPTED_WORKING_CANDIDATE / NOT AUTHORITY.
- **Accepted working direction:** initial admission and continued/reconnect authority are distinct. Product must decide whether an already-admitted participant is disconnected immediately on expiry/revocation or whether any narrowly governed occurrence-specific continuity/grace exists.
- **Originating tranche:** Pass B `LIVE-PT-022`, reinforced by stale capability/reconnect and Pass-L convergence tests.
- **Affected owner:** Entitlements for general right; Events & Live for occurrence context/admission rules.
- **Why JIT cannot invent it:** user access continuity is Product behavior, not a provider-session technical default.
- **Likely authority route:** Product Law / Entitlement + Events semantics → future JIT enforcement.
- **Current blocker/consumer:** `LIVE-GAP-008`; live join/reconnect proof.

### LIVE-UPD-005 — Recording participation contract at admission/policy transition

- **Status:** ACCEPTED_WORKING_LOCK / CANDIDATE UPSTREAM DECISION PACKAGE / NOT AUTHORITY.
- **Accepted working direction:** current recording participation requirements must account for role/context, late join, refusal/decline outcome, material policy changes and provider-control mapping; registration does not freeze recording authority.
- **Originating tranche:** Pass D `LIVE-PT-040...047`, reinforced by Pass E role transition cases `LIVE-PT-048...056`.
- **Affected owner:** Privacy & Consent for purpose authority; Events & Live for occurrence notice/admission context; Content & Media for later governed use.
- **Why JIT cannot invent it:** refusal consequences, late-join treatment and materially changed capture scope are Product/privacy semantics.
- **Likely authority route:** `OQ-021` / Product-Privacy-Legal-Operations adjudication → provider empirical mapping → JIT.
- **Current blocker/consumer:** `LIVE-GAP-003`, `LIVE-GAP-013`; recording-aware admission.

### LIVE-UPD-006 — Post-capture recording-purpose withdrawal consequences

- **Status:** ACCEPTED_WORKING_LOCK / CANDIDATE UPSTREAM DECISION PACKAGE / NOT AUTHORITY.
- **Accepted working direction:** define current/future consequences of purpose withdrawal across live continuation, raw capture, pre-publication, published replay, multi-person separability/inseparability, role-specific bases and dependent derivatives while preserving historical truth.
- **Originating tranche:** Pass F `LIVE-PT-057...065`, reinforced by Passes G–H and replay/clip correction work.
- **Affected owner:** Privacy & Consent principally; Content & Media applies media consequences; Events retains occurrence/attendance truth.
- **Why JIT cannot invent it:** withdrawal scope, multi-person treatment and retained future use are Product/privacy/legal policy.
- **Likely authority route:** `OQ-021` plus applicable `OQ-029...032` → Privacy/C&M JIT after authority resolution.
- **Current blocker/consumer:** `LIVE-GAP-003`; replay/derivative/retention/deletion behavior.

## 2. Accepted gap register

### LIVE-GAP-001 — Complete occurrence lifecycle and schedule-version semantics

- **Classification:** `PRODUCT_AUTHORITY_GAP`.
- **Owner/gate:** Product / Events & Live; principally `LIVE-UPD-001`.
- **Status:** OPEN.
- **Blocks:** exact FP-007 occurrence lifecycle/schedule/supersession contract where a Product-significant distinction is required.
- **Does not block:** provider-independent occurrence identity invariant or ordinary JIT mechanics that do not decide the unresolved semantics.
- **Relevant UPD:** `LIVE-UPD-001`.
- **Proof route:** Product adjudication → Events JIT → executable lifecycle/concurrency proof.
- **Reopen trigger:** future JIT/7A needs an exact lifecycle answer or current authority changes.

### LIVE-GAP-002 — Provider/live path empirical validation

- **Classification:** `PROVIDER_EMPIRICAL_GATE`.
- **Owner/gate:** `OQ-020`.
- **Status:** OPEN; Pass M provides accepted documentation evidence only.
- **Blocks:** claiming the Restream/Cloudflare path is operationally proven/certified for FP-007.
- **Does not block:** semantic planning behind fail-closed provider interfaces.
- **Relevant UPD:** none; provider evidence may expose upstream issues but does not own Product meaning.
- **Proof route:** first-party documentation + provider/account confirmation + controlled live/failure-injection/retry/reorder/restart/operator-recovery proof.
- **Reopen trigger:** provider evidence drift or controlled proof falsifies an accepted invariant.

### LIVE-GAP-003 — Recording privacy/consent/retention/deletion semantics

- **Classification:** `RECORDING_PRIVACY_GATE`.
- **Primary owner/gate:** `OQ-021`.
- **Status:** OPEN.
- **Scope:** recording consent/permission; role/capture scope; sensitive audience material; post-capture withdrawal; replay/clip purpose; multi-person media; recording retention/deletion; Full-Deletion participant representation.
- **Composes as applicable with:** `OQ-029` category retention/disposition; `OQ-030` external processor deletion; `OQ-031` restore/non-resurrection; `OQ-032` deletion/export operations; `LIVE-GAP-014` provider proof.
- **Blocks:** exact lawful/Product recording/replay/withdrawal policy and any provider path that cannot enforce the approved rule.
- **Does not block:** owner separation, fail-closed behavior, or historical-truth invariants already established.
- **Relevant UPDs:** `LIVE-UPD-005`, `LIVE-UPD-006`.
- **Proof route:** Product/Privacy/Legal/Operations authority → Privacy/C&M/Events JIT → controlled proof.
- **Reopen trigger:** OQ resolution changes/falsifies current assumptions.

### LIVE-GAP-004 — Attendance business meaning

- **Classification:** `PRODUCT_AUTHORITY_GAP`.
- **Owner/gate:** Product / Events & Live.
- **Status:** OPEN.
- **Blocks:** exact `attended`/`no_show`/pending/finality/correction policy.
- **Does not block:** provider-evidence-not-authority invariant or derived Analytics ownership.
- **Relevant UPD:** `LIVE-UPD-002`.
- **Proof route:** Product adjudication → Events JIT → provider correlation/correction proof.
- **Reopen trigger:** FP-007/FP-008/FP-009 needs exact attendance semantics.

### LIVE-GAP-005 — Replay-right policy across product/access sources

- **Classification:** `PRODUCT_AUTHORITY_GAP`.
- **Owner/gate:** Product / Entitlements.
- **Status:** OPEN.
- **Blocks:** exact replay-right matrix by membership/programme/sponsored/public/once-off source.
- **Does not block:** current-entitlement-before-protected-delivery invariant.
- **Relevant UPD:** `LIVE-UPD-003`.
- **Proof route:** Product entitlement semantics → Entitlements/C&M JIT → protected-playback proof.
- **Reopen trigger:** selected FP-007 product family needs an exact replay-right answer.

### LIVE-GAP-006 — Promised live communications

- **Classification:** `COMMUNICATIONS_GATE`.
- **Owner/gate:** Communications; `OQ-036` for promised/required live journeys; `OQ-017` additionally where reminders are promised.
- **Status:** OPEN / scope-dependent.
- **Blocks:** only included/promised journeys requiring unresolved channel/provider policy.
- **Does not block:** lifecycle facts when no outbound promise exists; Communications never owns source truth.
- **Relevant UPD:** none.
- **Proof route:** future FP-007 journey inventory → applicable gate → Communications JIT → durable delivery/failure proof.
- **Reopen trigger:** Final Contract includes a previously optional journey or authority changes notification requirements.

### LIVE-GAP-007 — Scarce event commerce

- **Classification:** `FUTURE_EVENT_COMMERCE`.
- **Owner/gate:** future FP-015 / Event Commerce scope.
- **Status:** DEFERRED BY DESIGN.
- **Blocks:** nothing in ordinary FP-007 governed live/replay.
- **Does not block:** non-scarce registration/access/attendance.
- **Relevant UPD:** none.
- **Proof route:** future FP-015 governance.
- **Reopen trigger:** FP-007 scope is materially amended to include scarce/paid ticket mechanics.

### LIVE-GAP-008 — In-progress access continuity

- **Classification:** `PRODUCT_AUTHORITY_GAP`.
- **Owner/gate:** Product / Entitlements + Events context.
- **Status:** OPEN.
- **Blocks:** exact disconnect/grace/continuity behavior after right changes during an active session.
- **Does not block:** initial current-access admission check or stale-capability fail-closed rule.
- **Relevant UPD:** `LIVE-UPD-004`.
- **Proof route:** Product adjudication → JIT enforcement → active-session/reconnect proof.
- **Reopen trigger:** future Final Contract requires exact ongoing-access behavior.

### LIVE-GAP-009 — Registration requirement and cancellation semantics

- **Classification:** `PRODUCT_AUTHORITY_GAP`.
- **Owner/gate:** Product / Events & Live.
- **Status:** OPEN.
- **Blocks:** exact required/optional/absent registration matrix and cancellation behavior if cancellation is included.
- **Does not block:** omitting unnecessary cancellation from FP-007 or separating registration from entitlement/attendance.
- **Relevant UPD:** related to occurrence/access policy; no new UPD required.
- **Proof route:** FP-007 scope adjudication → if included, Product authority → Events JIT → proof.
- **Reopen trigger:** selected FP-007 scope includes cancellation or requires exact registration mode.

**Corrected PT-028 route:** cancellation optional in FP-007 scope → if included → `LIVE-GAP-009` / Product authority resolves meaning → Events JIT implements it. JIT does not invent the rule.

### LIVE-GAP-010 — Weak-identity/public live attendance

- **Classification:** `PRODUCT_AUTHORITY_GAP`.
- **Owner/gate:** Product / Events & Live with Identity assurance context.
- **Status:** OPEN.
- **Blocks:** claiming named participant attendance where delivery mode lacks sufficient identity assurance.
- **Does not block:** aggregate permitted live-engagement measurement or public viewing where person-level attendance is not promised.
- **Relevant UPD:** `LIVE-UPD-002`.
- **Proof route:** Product assurance requirement → provider capability evidence → Events JIT.
- **Reopen trigger:** public/free access mode requires person-level attendance.

### LIVE-GAP-011 — Provider capture lifecycle/finalisation

- **Classification:** `PROVIDER_EMPIRICAL_GATE`.
- **Owner/gate:** `OQ-020`.
- **Status:** OPEN; Pass M adds recording multiplicity/segmentation/readiness evidence.
- **Blocks:** trusting provider readiness/finality/callbacks as sufficient capture evidence.
- **Does not block:** raw-capture-not-governed-media invariant.
- **Relevant UPD:** none.
- **Proof route:** provider docs/account confirmation → controlled capture failure/segment/reorder tests → C&M/Events JIT.
- **Reopen trigger:** provider behavior materially differs in controlled proof.

### LIVE-GAP-012 — External capture → governed-media adoption mechanism

- **Classification:** `JIT_ONLY`.
- **Owner/gate:** Content & Media JIT after semantics/provider evidence.
- **Status:** OPEN / DOWNSTREAM.
- **Blocks:** exact adoption Resource/action/operator mechanism only.
- **Does not block:** Product semantics or need a new Domain.
- **Relevant UPD:** none.
- **Proof route:** C&M JIT → operator/concurrency/idempotency proof.
- **Reopen trigger:** JIT exposes an upstream contradiction rather than a representation choice.

### LIVE-GAP-013 — Recording-aware provider enforcement

- **Classification:** `PROVIDER_EMPIRICAL_GATE`.
- **Owner/gate:** `OQ-020`, dependent on approved OQ-021 semantics.
- **Status:** OPEN.
- **Blocks:** claiming selected provider path can enforce approved notice/role/capture/no-recording behavior.
- **Does not block:** fail-closed semantics.
- **Relevant UPD:** `LIVE-UPD-005` where policy meaning remains unresolved.
- **Proof route:** OQ-021 rule → provider account/capability validation → controlled admission/capture proof.
- **Reopen trigger:** provider cannot enforce approved rule or introduces unavoidable capture.

### LIVE-GAP-014 — Recording-media processor deletion and non-resurrection evidence

- **Classification:** `PROVIDER_EMPIRICAL_GATE`.
- **Owner/gate:** `OQ-030` plus `OQ-031`; composes with OQ-021/OQ-029/OQ-032 as applicable.
- **Status:** ACCEPTED_WORKING_LOCK / OPEN.
- **Blocks:** declaring processor-complete deletion/non-resurrection for the selected path.
- **Does not block:** current-use withdrawal or local owner truth when processor deletion is still pending; it prevents false completion.
- **Relevant UPD:** `LIVE-UPD-006` only for purpose-withdrawal semantics; no new Product delta.
- **Proof route:** complete processor representation inventory → delete/reconcile/verify → restore/non-resurrection proof.
- **Reopen trigger:** selected provider/storage path changes or controlled deletion proof fails.

## 3. Guard decisions

```text
LIVE-UPD-007 = NOT CREATED / NOT WARRANTED
LIVE-GAP-015 = NOT CREATED / NOT WARRANTED
```

Remaining work is already owned by the six UPDs, fourteen gaps, current OQ routes, future JIT representation choices or executable proof. Packaging questions do not justify new governed-looking identifiers.
