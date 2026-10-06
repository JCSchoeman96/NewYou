# NewYou Communications Pre-JIT Discovery — Consolidated Working v0.10.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT CONSOLIDATION**
>
> This document is not Product Law, Architecture Law, Domain Law, Roadmap authority, a governed JIT Domain Dossier, a Final Feature Pack Contract, proof classification, Tracer Bullet, Vertical Slice or release evidence.
>
> It is the compact current working interpretation of the detailed Communications Pre-JIT discovery recorded in predecessor `NEWYOU_COMMUNICATIONS_PREJIT_DISCOVERY_WORKING_v0.9.0.md`.
>
> The predecessor remains the detailed evidence ledger. This v0.10.0 successor is the reviewer-facing consolidation and should be used as the navigation surface for the eventual governed Communications JIT work.
>
> If live GitHub authority changes, this consolidation must be revalidated before reuse.

- **Document version:** v0.10.0
- **Predecessor:** `NEWYOU_COMMUNICATIONS_PREJIT_DISCOVERY_WORKING_v0.9.0.md` — preserved unchanged
- **Predecessor SHA-256:** `cc770b81ba57bbb4d15df9ba544a97aebbfbad15e5b857cb4d59723c383d1817`
- **Canonical repository checked:** `JCSchoeman96/NewYou`
- **Authority pin for this consolidation:** `3f899e00ecfdfb9abc0794cffcb19eaff2726d58`
- **Broad-discovery status:** `PASS — PARK BROAD COMMUNICATIONS PRE-JIT DISCOVERY`
- **Governed Communications JIT final-certification status:** `BLOCKED / STOP`
- **Phase 7C freeze status:** `BLOCKED / STOP`
- **Blocking upstream working deltas:** `COMM-UPD-001`, `COMM-UPD-002`
- **Detailed discovery volume:** `COMM-WD-001...200`; `COMM-PT-001...340`
- **Stable local trace identifiers:** `COMM-WD-*`, `COMM-PT-*`, `COMM-UPD-*`

## Consolidation hygiene correction

Earlier detailed versions contain overlapping plain ordinal numbering in some **rejected-model** and **later-proof-obligation** lists, especially across the v0.6/v0.7 transition. Those ordinals were prose-list numbers, not governed identifiers, but treating them as stable IDs would now be ambiguous.

Therefore:

- this v0.10.0 consolidation **retires those old ordinals as identifiers**;
- detailed semantic evidence remains preserved in v0.9.0;
- the only stable discovery trace IDs remain `COMM-WD-*`, `COMM-PT-*`, `COMM-UPD-*`;
- the compact rejected/proof registers below use fresh `COMM-RJ-W*` and `COMM-PROOF-W*` labels that are explicitly **local / non-governed working labels**.

One earlier hypothesis is also now considered resolved by later discovery:

- `COMM-WD-012` was recorded as `OPEN_HYPOTHESIS` around whether provider acceptance discharges every delivery obligation.
- Later accepted rules establish the stable interpretation: provider acceptance is external evidence, not delivery/source truth; it prevents speculative duplicate failover where an operation exists, while final obligation resolution remains role/policy/evidence dependent.
- v0.10.0 therefore carries **no unresolved core working-design hypothesis** for the required FP-001 Communications path.

---

# 1. Accepted working-design register

This register compresses the 200 detailed `COMM-WD-*` entries into the stable design contract that survived the adversarial sweep.

| Working design | Consolidated accepted conclusion | Trace |
|---|---|---|
| **Core Resource model** | Required FP-001 Communications durable business Resources are exactly `MessageIntent` and `DeliveryAttempt`. New nouns, projections, commands, provider configuration and execution machinery do not earn Resource status without independent durable business truth. | `COMM-WD-001..002`, `019`, `036`, `090`, `119`, `142`, `161`, `176`, `186`, `193`, `200` |
| **MessageIntent identity** | A `MessageIntent` is one logical communication obligation anchored to the source logical operation/challenge + communication role, not merely Account + purpose + destination. Distinct source challenges never collapse because they target the same address. | `COMM-WD-001`, `013..014`, `020..023`, `063`, `192` |
| **DeliveryAttempt identity** | A `DeliveryAttempt` is one real provider/channel submission operation and its evidence. Rendering failure, policy deferral, known outage or queue retry before provider I/O is not a DeliveryAttempt. | `COMM-WD-002`, `008..010`, `085..086`, `092..095`, `168..173` |
| **Atomic source handoff** | Where Identity issuance requires protected delivery, source issuance + durable MessageIntent + required protected-delivery capability must establish atomically/fail closed. No committed issuance may exist with a lost delivery obligation. | `COMM-WD-003..004`, `116` |
| **Durable execution/liveness** | A committed intent must remain discoverable/executable after crash/restart independently of one surviving queue job. Oban uniqueness/job state is acceleration/execution, not business correctness. | `COMM-WD-004`, `011`, `097`, `099..100`, `117` |
| **Attempt-admission cutover** | All current owner predicates are revalidated before a new provider operation. Provider I/O begins only after a concurrency-safe durable attempt admission/identity. Invalidations winning before admission prevent the call; a lawfully begun external operation may finish historically. | `COMM-WD-005`, `016..017`, `092`, `188`, `198` |
| **Unknown outcome** | `UNKNOWN` is a first-class unresolved provider outcome. It is never equivalent to retryable failure. Blind retry/failover is prohibited until reconciliation makes a safe new operation possible. | `COMM-WD-006`, `079`, `094`, `111`, `128`, `170` |
| **Provider evidence dimensions** | Submission/acceptance, delivery, bounce, open/click and source business outcome are distinct dimensions. Provider acceptance/delivery never verifies an email, consumes a proof, changes canonical email or establishes conversion. | `COMM-WD-008..010`, `024`, `093..094`, `147`, `181..183` |
| **Retry versus resend** | Infrastructure/provider retry stays under the same MessageIntent. A participant resend that causes Identity to issue/supersede a challenge creates a new source obligation and new MessageIntent. | `COMM-WD-007`, `014`, `020`, `115`, `189`, `192` |
| **Superseding source obligation versus old ambiguity** | Old provider ambiguity blocks retry/failover of that old intent, but does not block a genuinely new source obligation. The old operation stays reconcilable; its superseded proof remains unusable if it later arrives. | `COMM-WD-189..192` |
| **Source validity and delivery state are orthogonal** | Proof validity/consumption/revocation/supersession remains Identity authority. Delivery history remains Communications authority. Historical reconciliation may continue after source invalidation without restoring send authority. | `COMM-WD-015..017`, `081`, `098`, `190..191` |
| **Destination provenance** | Security intents carry immutable, minimised event-correct destination provenance. Workers do not silently re-resolve the current Account email. This does not create Communications ownership of canonical email or justify `SubscriberContact`. | `COMM-WD-018..019`, `021..024`, `027`, `052` |
| **Primary-email change split** | New-address confirmation and old-address notice are distinct logical obligations with different destinations/semantics. Later cancellation may invalidate the confirmation proof without making an already-established old-address security notice historically false. | `COMM-WD-021..023` |
| **Protected delivery capability** | Bearer material is protected delivery machinery, not business authority or an ordinary Resource. It is purpose-scoped, bounded by proof/obligation lifetime, excluded from ordinary fields/jobs/logs/Audit/Analytics, and has no independent retention right. | `COMM-WD-034`, `083..084`, `135`, `190` |
| **Closure / deletion distinction** | Recoverable Account closure is not full deletion. Source/privacy authority may `ALLOW`, `SUSPEND` or terminally `STOP` new dispatch. Reactivation does not automatically replay old messages. | `COMM-WD-028..031` |
| **Full deletion owner boundary** | Privacy & Consent owns deletion orchestration/completion. Communications applies an idempotent owner deletion/disposition contract over its own records and reports its sub-result; Privacy never shared-writes Communications rows. | `COMM-WD-032..038`, `043..046` |
| **Restore / non-resurrection** | Restored provider egress is fail-closed until current deletion/suppression/source/content/provider authority is recovered and stale jobs/capabilities reconciled. Backups cannot resurrect deleted participant authority or stale sends. | `COMM-WD-039`, `196` |
| **Merge/reconciliation** | Duplicate-account candidates do nothing until Identity applies reconciliation. Historical Communications records are not re-parented to the survivor, and stale proofs/messages do not acquire survivor authority. | `COMM-WD-040..041` |
| **Data lifecycle versus business lifecycle** | Delivery state and data-retention/deletion/legal-hold state are orthogonal. Historical evidence may be retained only under independent approved authority and never becomes resend/recovery authority. | `COMM-WD-033..045`, `152..153`, `194` |
| **Required FP-001 preferences scope** | Mandatory/source-authorised security/account communication does not require marketing permission or an FP-001 `NotificationPreference` Resource. Marketing permission, preference and delivery policy remain separate truths. | `COMM-WD-025`, `050..067` |
| **Conditional accountless mailing list** | Accountless mailing-list state is not required by the current FP-001 outcome. If explicitly activated, `SubscriberContact` + a durable Communications preference concept become material and Privacy & Consent must be pulled forward before Phase 7C. | `COMM-WD-047..049`, `052..058`, `065..066` |
| **Content ownership** | Content & Media owns governed message/template content versions and locale versions. Communications owns exact delivery binding/provenance and execution, not template/body authority. | `COMM-WD-068`, `088..091`; see `COMM-UPD-001` |
| **Locale/content binding** | MessageIntent carries semantic role + explicit intended locale. Before first provider submission it binds one exact currently eligible C&M content/locale version; retries never dereference arbitrary “latest”. | `COMM-WD-069..077` |
| **Content correction/rebind** | Bound content eligibility is revalidated before each new attempt. Explicit safe successor rebinding is allowed only when the old provider operation is definitively non-delivered and source authority remains valid. Unknown old outcome blocks rebind + new send. | `COMM-WD-076..081` |
| **Render-data boundary** | MessageIntent may hold only a bounded immutable non-secret render snapshot. Templates receive closed/typed allowed data. Bearer material is transiently injected by the protected executor; full secret-bearing rendered bodies need not be ordinary durable truth. | `COMM-WD-082..087` |
| **Retry horizon / outage** | Retry is bounded by the underlying delivery obligation/proof/capability, not by queue configuration. Shared outage uses coordinated degradation, provider-aware scheduling, bounded concurrency and fresh revalidation. | `COMM-WD-096..109`, `114..119` |
| **Operator recovery** | Manual retry/reconcile are distinct, current-authority owner commands. Operators cannot bypass source/content/privacy/deletion/ambiguity guards, edit historical provider facts, or routinely resend from provider dashboards. | `COMM-WD-110..112`, `123..132`, `195` |
| **Audit boundary** | Automated delivery evidence stays Communications-owned. Central Audit receives minimum privileged/security evidence where governed; required Audit establishment is fail-closed for privileged provider-mutating actions. Audit is not the delivery ledger. | `COMM-WD-121..124`, `154..157` |
| **Observability boundary** | Logs/traces/metrics/dashboards are non-authoritative, failure-isolated diagnostics. No bearer, full destination/body, credentials or high-cardinality participant/business IDs belong in normal telemetry. | `COMM-WD-125..156` |
| **Security engagement tracking** | Required FP-001 security email does not need open/click tracking. Protected URLs must not be provider-rewritten through tracking redirects. Scanner/prefetch-safe proof consumption remains an Identity seam. | `COMM-WD-147..150`; see `COMM-UPD-002` |
| **In-app scope** | Product's “email + in-app first” is channel-capability direction, not mandatory dual delivery. FP-001 required work/status can be reconstructed from Identity + Communications state; a durable `InAppNotification` inbox is not an FP-001 prerequisite. | `COMM-WD-158..162` |
| **Channel/provider boundary** | Source semantics may constrain channel; Communications selects provider inside that constraint. `Channel` is a bounded concept, not a Resource. Adapters are thin and typed rather than one universal untyped `send(map)`. | `COMM-WD-163..176` |
| **Cross-channel/future channels** | No generic automatic channel fallback exists. Email verification cannot be substituted by SMS/WhatsApp/in-app. Future phone recovery and optional multi-channel delivery require new source/permission/fulfilment semantics. | `COMM-WD-165..180` |
| **Provider failover/migration** | Same-channel provider change remains under one MessageIntent and creates new DeliveryAttempts only when safe. Unknown/accepted old provider operation blocks speculative failover. Migration never transfers or erases old-provider ambiguity. | `COMM-WD-168..174`, `197` |
| **Provider suppression / bounce** | Provider suppression/bounce is a physical delivery constraint/evidence, not Identity canonical-email truth, Privacy permission or Communications preference. Selected provider must preserve mandatory-security versus marketing separation. | `COMM-WD-181..183` |
| **Batching / backlog** | Batch/provider bulk APIs and outage recovery are execution optimisations only if per-intent/per-attempt truth remains independently reconstructible. They do not create a `CommunicationJourney`. | `COMM-WD-185..186` |
| **OQ-036 boundary** | Provider-independent JIT semantics may freeze before provider selection. `OQ-036` remains release-only and must later prove a valid launch email implementation satisfying the frozen contract. | `COMM-WD-187` |
| **Composite admission theorem** | New provider submission is permitted only when all applicable current source, capability, destination, purpose/preference, content, ambiguity, retry/manual-recovery and channel/provider predicates allow it. No combined orchestration authority is created. | `COMM-WD-188`, `193`, `195`, `198` |
| **Conditional dossiers** | Privacy & Consent, Content & Media, Audit & Evidence remain conditional/not pulled forward for the current required FP-001 path. Analytics remains no-dossier. | `COMM-WD-091`, `157`, `199` |
| **Discovery stabilisation** | Broad ordinary Communications Pre-JIT scenario expansion is parked. Reopen only on new authority/scope, blocker resolution that changes the seam, drafting contradiction, or implementation/proof evidence that falsifies the model. | `COMM-WD-200` |

---

# 2. Pressure-test coverage register

The 340 detailed scenarios are preserved in v0.9.0. This table is the compact coverage index.

| Pressure-test range | Coverage | Stabilised result |
|---|---|---|
| **`COMM-PT-001...027`** | Atomic Identity→Communications handoff; crash before/after enqueue; duplicate workers; provider acceptance/timeout/unknown/rejection; duplicate/reordered callbacks; retry/dedup; proof expiry/consumption/supersession; email-change destinations; resend abuse/enumeration | Established the two-Resource model, source-obligation idempotency, durable cutover, explicit unknown outcome, destination snapshots and separation of provider evidence from Identity truth. |
| **`COMM-PT-028...052`** | Account closure; deletion pending/cancel/execute; legal hold; provider deletion evidence; late callbacks; restore; protected-capability destruction; duplicate-account merge; same-email re-registration | No deletion/merge Resource added. Privacy remains deletion authority; Communications owns owner-specific disposition and historical evidence. Restore/non-resurrection rules stabilised. |
| **`COMM-PT-053...084`** | Public mailing-list scope; duplicate accountless signup; cross-domain partial failure; marketing permission vs preference; unsubscribe; linking contact→Account; quiet hours/frequency caps; future channels | Current FP-001 still needs no SubscriberContact/NotificationPreference Resource. Explicit mailing-list activation would pull Privacy forward and justify SubscriberContact + preference concept. |
| **`COMM-PT-085...124`** | C&M ownership; bilingual/locale rules; content binding; correction/withdrawal/rebind; renderer failures; safe render inputs; bearer interpolation; provider-hosted templates; retention/restore | Exposed `COMM-UPD-001`. No C&M dossier pulled forward. Exact immutable content/locale provenance and safe rebind contract stabilised. |
| **`COMM-PT-125...185`** | Provider outage/backlog; bounded retry; proof expiry in queue; retry storms; throttling; priority/fairness; unknown at scale; operator pause/retry/reconcile; graceful degradation; OQ-036 boundary | No provider/outage/retry Resource added. DeliveryAttempt boundary and bounded provider-independent retry/reconciliation semantics stabilised. |
| **`COMM-PT-186...244`** | Audit/observability; operator evidence; masking/reveal; logs/metrics/traces; raw provider payloads; credentials; callback authentication; open/click; provider tracking; scanner prefetch; Analytics; incident linkage | Audit remains conditional. Exposed `COMM-UPD-002`. Security-message engagement tracking not required; provider click rewriting rejected. |
| **`COMM-PT-245...300`** | Email vs in-app; required-work visibility; provider replacement/failover/migration; suppression/bounce; future SMS/WhatsApp; multi-channel semantics; batching; adapter abstraction; OQ-036 | In-app inbox not required. `Channel` remains a concept, not Resource. One provider-independent email contract is sufficient; future channels stay deferred. |
| **`COMM-PT-301...340`** | Adversarial compositions across proof expiry, provider unknown, content withdrawal, resend, deletion, merge, restore, migration, Audit outage, operator recovery, batches, scanner prefetch and simultaneous owner invalidations | No third Resource, no new higher-law amendment, no conditional dossier pull-forward. Added the refinement that old ambiguity does not block a genuinely new superseding source obligation. Broad discovery passed stabilisation. |

### Coverage verdict

The sweep covers all scenario classes required by the initial Grill-Me mandate, including:

- concurrency / retries / reordering / restart;
- duplicate execution and business idempotency;
- provider ambiguity;
- source proof races;
- email-change old/new destinations;
- closure/deletion/merge/restore;
- accountless contacts / permission / preferences;
- content/locale/version provenance;
- sensitive-data and protected-bearer minimisation;
- Audit/Analytics/observability boundaries;
- provider outage / retry storms / terminal recovery;
- channel/provider independence and future SMS/WhatsApp seams;
- composed adversarial combinations.

No further ordinary broad scenario round is justified on current evidence.

---

# 3. Upstream-delta register

## `COMM-UPD-001` — REQUIRED

**Owner:** certified FP-001 Identity & Access JIT dossier governance.

**Issue:** Identity v0.1.3 says Communications owns “message body/template”. Current higher authority assigns governed message/template content versions to Content & Media; Communications owns delivery intent/execution/evidence and exact content/locale delivery provenance.

**Required smallest correction:** narrow Identity PATCH successor/explicit certified correction preserving the already-certified protected-delivery seam.

**Higher-law amendment:** `NO`.

**Effect:**

```text
Communications Pre-JIT consolidation
→ may continue / complete

Governed Communications JIT final certification
→ BLOCKED / STOP

Phase 7C freeze
→ BLOCKED / STOP
```

## `COMM-UPD-002` — REQUIRED

**Owner:** Identity & Access protected-link proof-consumption semantics.

**Issue:** current certified lifecycle does not explicitly freeze the interaction boundary preventing email providers, corporate gateways, anti-phishing/security scanners, browser preview systems or other automated fetchers from becoming the effective consumer of verification/reset/recovery/email-change bearer links.

**Required invariant:**

```text
automated link retrieval / HEAD / GET / prefetch
≠ sufficient authority by itself to complete
verification / reset / recovery / email-change transition
```

**Required smallest correction:** narrow Identity successor/clarification, or an explicitly governed Identity executable proof contract that freezes scanner/prefetch-safe protected-link consumption before final cross-domain freeze/implementation.

**Higher-law amendment:** `NO`.

**Effect:**

```text
Communications discovery/consolidation
→ complete enough to park

Final cross-domain freeze / implementation entry
→ BLOCKED / STOP until resolved or explicitly governed
```

## No third upstream delta

The final adversarial sweep exposed no additional Product, Architecture, Domain or Roadmap contradiction.

---

# 4. Unresolved-gate register

| Matter | Current disposition |
|---|---|
| `COMM-UPD-001` | **Blocks Communications final JIT certification / Phase 7C freeze.** |
| `COMM-UPD-002` | **Blocks final cross-domain freeze / implementation unless explicitly resolved/routed.** |
| `OQ-035` | Security/operations abuse thresholds remain release-only. Does not block provider-independent Communications semantics. |
| `OQ-036` | Launch email/in-app implementation/provider/channel operations proof remains release-only. Communications JIT must remain provider-independent. |
| `OQ-029` | Exact retention/deletion periods for Communications/provider/Audit/telemetry evidence remain later policy/expert gate. |
| `OQ-030...032` | Processor deletion/export, restore replay and deletion-operation exact mechanics remain later data-lifecycle/provider gates. |
| `OQ-013` | Exact Content & Media translation/version Resource topology remains C&M concern; Communications consumes opaque exact version/locale + current eligibility. |
| `OQ-038` | Named incident ownership/process remains future-only for FP-001 planning. Does not justify Incident Resource now. |
| Exact Ash Resources/attributes/actions/indexes | Communications JIT detail. |
| Exact PostgreSQL uniqueness/locking/conditional-write mechanics | JIT + executable proof detail. |
| Exact Oban queue names/uniqueness/backoff/retry counts | JIT / OQ-036 / proof detail. |
| Exact provider SDK/API/callback fields | OQ-036 + implementation proof. |
| Exact protected-capability storage/encryption implementation | Identity/Communications JIT/proof; no package selected here. |
| Exact central Audit event schema | Audit implementation detail; semantic minimum contract is sufficient. |
| Exact support/operator UI controls | FES/Identity/Communications implementation detail under the stable policy boundaries. |

---

# 5. Cross-stream dependency register

| Owner / stream | Communications dependency and boundary |
|---|---|
| **Identity & Access** | Owns Account email, source challenges/proofs, verification/recovery/email-change truth, source validity/consumption/supersession, resend issuance, Account closure/merge effects and operator grants. Communications consumes a non-secret current source-validity/dispatch contract and never becomes second Identity authority. |
| **Privacy & Consent** | Owns purpose permission, deletion orchestration/completion, retention policy, legal hold and suppression authority. Communications owns its contact/preference state where introduced and applies owner-specific deletion/disposition through its own interface. |
| **Content & Media** | Owns governed message/template content versions, locale versions, publication/correction/withdrawal and current delivery eligibility. Communications owns exact binding/provenance and delivery execution. |
| **Audit & Evidence** | Owns minimum append-only privileged/security evidence and governed evidence access. Communications owns delivery/provider evidence. Audit never becomes a second delivery ledger. |
| **Analytics** | Consumer-only derived measurement. No authority over delivery, verification, permission, provider truth or communication content. Raw security payload/bearer/contact data is not required. |
| **FES / Operating Model** | Required work/status remains source-owned and reconstructible; email/toast/inbox projection is not the only place required work exists. In-app notification centre is not an FP-001 prerequisite. |
| **Engineering Standards** | HIGH-risk concurrency/idempotency/provider-reconciliation/sensitive-data proof expectations apply. Telemetry remains bounded, backend-neutral and non-authoritative. |
| **PostgreSQL / Ash** | Default authoritative persistence/transaction boundary. Exact actions/constraints/locking belong JIT/proof. Cross-Domain owner interfaces must preserve one-writer ownership. |
| **Oban** | Durable executor/scheduler, not business truth. Job uniqueness/retry counts never replace MessageIntent idempotency, current source checks or DeliveryAttempt evidence. |
| **Selected email provider / `OQ-036`** | Must satisfy frozen provider-independent callback/authentication, ambiguity/reconciliation, suppression, protected-link, delivery-evidence and operations requirements. Provider capability does not redefine platform law. |
| **Future SMS / WhatsApp / push** | Deferred seams. Activation requires explicit source/channel/permission/content/provider semantics; no premature Resources/abstractions are introduced in FP-001. |

---

# 6. Conditional-dossier adjudication

## Privacy & Consent

**Current disposition:** `CONDITIONAL / NOT PULLED FORWARD`.

The required FP-001 security/account-delivery path can be implementation-grade from current Privacy authority without inventing new Privacy lifecycle.

**Explicit pull-forward trigger:**

```text
IF FP-001 activates public/accountless mailing-list acquisition
→ accountless purpose grant / withdrawal / regrant / link-to-Account semantics become implementation-grade
→ Privacy & Consent dossier becomes REQUIRED before Phase 7C
```

Future optional SMS/WhatsApp/marketing activation may create a similar trigger.

## Content & Media

**Current disposition:** `CONDITIONAL / NOT PULLED FORWARD`.

Communications can depend on a stable owner contract:

```text
role + intended locale
→ exact eligible C&M content version
→ exact locale version
→ current eligibility / explicit successor relation
```

No C&M internal Resource topology needs to be invented by Communications.

**Pull-forward trigger:** materially new FP-001 message-content/publication semantics or implementation evidence that the exact-version/current-eligibility contract cannot be supplied from existing C&M authority.

## Audit & Evidence

**Current disposition:** `CONDITIONAL / NOT PULLED FORWARD`.

Current law is sufficient to freeze:

- Communications-owned delivery evidence;
- central minimum privileged/security evidence;
- fail-closed privileged mutation when required Audit cannot be established;
- restricted evidence access;
- no bearer/body/provider-secret leakage.

**Pull-forward trigger:** Phase 7C requires a materially new central Audit-owned event/access/retention lifecycle that cannot be stated from current authority.

## Analytics

**Current disposition:** `NO DOSSIER`.

Analytics is not required for Communications correctness, delivery, proof consumption or FP-001 entry-flow completion.

---

# 7. Consolidated rejected-model register

The labels below are **local / non-governed** and replace ambiguous legacy rejected-list ordinals for review purposes.

| Local label | Rejected model | Why rejected / trace |
|---|---|---|
| `COMM-RJ-W01` | Communications owns Identity proof/account-email truth | Violates Domain ownership; provider evidence cannot establish Identity state. `COMM-WD-015..024`. |
| `COMM-RJ-W02` | Communications owns governed message/template versions | Competes with C&M; upstream wording defect is `COMM-UPD-001`. `COMM-WD-068`, `088..091`. |
| `COMM-RJ-W03` | One giant MessageIntent status encodes proof validity + delivery + privacy + content + provider state | Collapses independent authorities/lifecycles and creates a shadow orchestrator. `COMM-WD-015`, `028`, `033`, `188`, `193`. |
| `COMM-RJ-W04` | Provider/Oban state is business authority | Queue uniqueness, retry count, provider dashboard/status are execution/evidence only. `COMM-WD-011`, `097..100`, `120`, `132`. |
| `COMM-RJ-W05` | Deduplicate on Account/email + purpose | Incorrectly collapses distinct challenges/resends/roles. `COMM-WD-013..014`, `020..023`, `063`. |
| `COMM-RJ-W06` | Infrastructure retry creates a new MessageIntent | Same source obligation remains one logical intent. `COMM-WD-007`, `168`. |
| `COMM-RJ-W07` | Participant resend is merely another DeliveryAttempt | Resend is source re-issuance when Identity creates a new challenge. `COMM-WD-014`, `192`. |
| `COMM-RJ-W08` | `UNKNOWN` provider outcome may be blindly retried/failovered | Can duplicate a possibly accepted operation. `COMM-WD-006`, `079`, `094`, `170`. |
| `COMM-RJ-W09` | Provider acceptance/delivery means email verified/proof consumed | External evidence never establishes source truth. `COMM-WD-008`, `147`, `183`. |
| `COMM-RJ-W10` | Worker resolves current Account email at send time | Breaks event-correct destination semantics and old/new email-change notices. `COMM-WD-018..024`. |
| `COMM-RJ-W11` | Add SubscriberContact/NotificationPreference because the mature Domain names them | No current FP-001 durable truth justifies them. Conditional mailing-list branch is explicit. `COMM-WD-019`, `025`, `047..049`. |
| `COMM-RJ-W12` | Treat Account closure as full deletion or blanket no-email state | Product/Architecture distinguish recoverable closure, required recovery/security and full deletion. `COMM-WD-028..032`. |
| `COMM-RJ-W13` | Privacy shared-writes/deletes Communications rows | Violates one-owner rule. Privacy orchestrates; Communications applies owner contract. `COMM-WD-032`, `045`. |
| `COMM-RJ-W14` | Restore starts workers/provider egress immediately | Can resurrect deleted/suppressed participant work and stale protected data. `COMM-WD-039`, `196`. |
| `COMM-RJ-W15` | Retry dereferences latest template / silently changes locale | Destroys exact provenance and logical-message stability. `COMM-WD-069..079`. |
| `COMM-RJ-W16` | Persist bearer token or full secret-bearing rendered body in ordinary fields/jobs/logs | Violates protected-delivery minimisation. `COMM-WD-083..087`, `135`. |
| `COMM-RJ-W17` | Automatic provider failover/router is required for replaceability | Replaceable adapter does not justify active-active routing. `COMM-WD-118`, `169..175`. |
| `COMM-RJ-W18` | Generic automatic cross-channel fallback | Can change proof meaning/permission/content semantics. `COMM-WD-165..180`. |
| `COMM-RJ-W19` | In-app notification centre is required because required work must not exist only in email | Required work remains source-owned; FES says inbox is not FP-001 prerequisite. `COMM-WD-158..162`. |
| `COMM-RJ-W20` | Add mutable `Channel`/`Provider` Resources for configuration vocabulary | No independent FP-001 business lifecycle. `COMM-WD-174..176`. |
| `COMM-RJ-W21` | One universal untyped `send(channel, map)` abstraction | Erases channel-specific destination/content/permission/evidence contracts. `COMM-WD-175`. |
| `COMM-RJ-W22` | One DeliveryAttempt for a provider batch / batch-level retry | Loses per-recipient external-operation truth and ambiguity. `COMM-WD-185..186`. |
| `COMM-RJ-W23` | Central Audit/logs are the delivery ledger | Duplicates Communications authority and makes observability retention correctness-critical. `COMM-WD-121..139`. |
| `COMM-RJ-W24` | Operator may `mark delivered`, bypass source checks or resend directly from provider portal | Fabricates evidence/bypasses owner invariants and Audit. `COMM-WD-128..132`, `195`. |
| `COMM-RJ-W25` | Raw provider payloads/destinations/IDs/secrets belong in telemetry/Analytics | Violates minimisation/cardinality and creates duplicate sensitive stores. `COMM-WD-133..156`. |
| `COMM-RJ-W26` | Security open/click tracking is necessary for FP-001 | Not required for product correctness and increases privacy/link risk. `COMM-WD-147..150`. |
| `COMM-RJ-W27` | Disabling provider click tracking alone makes protected links scanner-safe | Independent mail/security scanners may still fetch direct links; Identity fix remains required. `COMM-UPD-002`. |
| `COMM-RJ-W28` | Continue broad discovery because more scenarios can always be imagined | After adversarial convergence, further ordinary scenarios add speculation more than confidence. `COMM-WD-200`. |

---

# 8. Consolidated later proof-obligation register

These labels are **local / non-governed**. They consolidate the detailed proof obligations from v0.9.0 and deliberately do not reuse the ambiguous legacy ordinals.

| Local label | Later executable proof obligation | Key discovery trace |
|---|---|---|
| `COMM-PROOF-W01` | Prove source issuance + MessageIntent + required protected capability fail atomically; failed establishment leaves no committed lost delivery obligation. | `PT-001`; `WD-003..004` |
| `COMM-PROOF-W02` | Crash after intent commit/before worker and restart/reconciliation must eventually execute or terminalise eligible work without source re-issuance. | `PT-002`; `WD-004`, `100` |
| `COMM-PROOF-W03` | Cross-node duplicate workers cannot create duplicate provider submissions for one attempt-admission path. | `PT-003`; `WD-005`, `092` |
| `COMM-PROOF-W04` | Timeout/ambiguous provider acknowledgement remains `UNKNOWN`; no blind same-intent retry/failover occurs. | `PT-004...006`, `256`; `WD-006`, `094`, `170` |
| `COMM-PROOF-W05` | Source invalidation/consumption/revocation/supersession racing attempt admission satisfies the cutover rule in both orderings. | `PT-012...016`, `332`; `WD-016..017`, `198` |
| `COMM-PROOF-W06` | Participant resend creates a new source-bound MessageIntent; old superseded intent/job cannot send, and coarse Oban/business dedupe cannot collapse the new challenge. | `PT-018...020`, `304`, `329..330`; `WD-014`, `192` |
| `COMM-PROOF-W07` | Old unknown provider operation may reconcile after resend, while late old proof remains unusable and does not block new source obligation. | `PT-304`, `326`; `WD-189..191` |
| `COMM-PROOF-W08` | New-address confirmation and old-address notice preserve distinct event-correct destination/role semantics under cancellation/apply/retry/outage races. | `PT-021...024`, `305..306`; `WD-021..023` |
| `COMM-PROOF-W09` | Protected bearer is absent from ordinary DB fields, jobs, logs, traces, Audit, Analytics, previews and support surfaces; capability becomes unusable at obligation/proof terminality. | `PT-106`, `117`, `202`, `207`; `WD-034`, `083..084`, `135` |
| `COMM-PROOF-W10` | Account closure suspends/permits only source-authorised work; reopening never blindly replays stale intents. | `PT-028...031`; `WD-028..031` |
| `COMM-PROOF-W11` | Full deletion racing queued/in-flight/unknown delivery prevents new egress, destroys active capability authority and cannot be reversed by late provider evidence. | `PT-032...040`, `307`; `WD-032..038`, `043..045` |
| `COMM-PROOF-W12` | Backup restore from pre-deletion/pre-withdrawal/pre-migration state produces zero provider egress until current suppression/source/content/provider truth is re-established. | `PT-042..043`, `124`, `311`; `WD-039`, `196` |
| `COMM-PROOF-W13` | Duplicate-account merge/candidate/rejection cannot re-parent stale communications or transfer proof authority; late callbacks stay historical. | `PT-044...047`, `309..310`; `WD-040..041` |
| `COMM-PROOF-W14` | If accountless mailing-list branch is activated: duplicate signup, cross-domain partial failure, withdrawal/regrant and contact→Account linking preserve separate Privacy permission and Communications preference/contact truths. | `PT-054...084`; `WD-048..067` |
| `COMM-PROOF-W15` | Exact C&M binding is concurrency-safe across nodes; critical missing/withdrawn locale/version fails closed before provider I/O. | `PT-086...095`; `WD-069..076` |
| `COMM-PROOF-W16` | Definitive non-delivery + explicit C&M successor can safely rebind same intent; unknown old outcome blocks rebind/new send. | `PT-096...101`, `315..316`; `WD-077..081` |
| `COMM-PROOF-W17` | Rendering contract rejects missing/unknown placeholders, arbitrary cross-Domain access and injection; renderer failure before provider I/O creates no fake DeliveryAttempt. | `PT-102...108`; `WD-082..087` |
| `COMM-PROOF-W18` | Provider-hosted template/config drift cannot silently alter governed NewYou content or erase exact platform version/locale provenance. | `PT-109..110`; `WD-088` |
| `COMM-PROOF-W19` | Long outage/backlog with proof/capability expiry suppresses stale protected sends; recovery uses current per-intent admission rather than blind FIFO drain. | `PT-125...145`, `312`, `328`; `WD-096..105` |
| `COMM-PROOF-W20` | Retry storm/provider throttling/fairness across nodes remains bounded; provider rate-control state never becomes business authority. | `PT-146...166`; `WD-101..108` |
| `COMM-PROOF-W21` | Automated terminal failure and manual recovery obey bounded retry/manual-recovery rules; participant-visible recovery remains available in owning journey. | `PT-167...185`, `327`, `338`; `WD-109..117` |
| `COMM-PROOF-W22` | Manual retry/reconcile/pause is idempotent, stale-command-safe, current-authority checked and appropriately audited; required Audit outage blocks privileged provider mutation. | `PT-190...198`, `324..325`; `WD-123..130`, `195` |
| `COMM-PROOF-W23` | Valid callbacks commit Communications evidence even when Audit/telemetry is unavailable; invalid callbacks cause zero business mutation and flood safely. | `PT-188...189`, `213...215`, `242`, `321`; `WD-125`, `145..146`, `154` |
| `COMM-PROOF-W24` | Metrics/logs/traces contain no participant identifiers as labels, raw destination/body/bearer/provider credentials or unsafe SDK exception data. | `PT-199...204`; `WD-133..139` |
| `COMM-PROOF-W25` | Provider engagement events never create Identity/business conversion truth; security tracking pixels/click rewriting remain absent for protected FP-001 links. | `PT-220...223`; `WD-147..149` |
| `COMM-PROOF-W26` | After `COMM-UPD-002`, automated scanner/prefetch and scanner-vs-user races cannot alone consume verification/reset/recovery/email-change proofs. | `PT-224...225`, `334..336`; `COMM-UPD-002` |
| `COMM-PROOF-W27` | FP-001 works without a durable in-app inbox: signed-out recovery, verification-pending status, terminal delivery recovery and old-address notice remain correct. | `PT-245...252`, `287..289`; `WD-158..162` |
| `COMM-PROOF-W28` | Provider selection/failover/migration preserves MessageIntent identity, creates per-provider DeliveryAttempts only when safe, and never fails over while old outcome is ambiguous/accepted. | `PT-253...268`, `313..317`; `WD-168..174`, `197` |
| `COMM-PROOF-W29` | Selected provider proves marketing unsubscribe/suppression cannot silently redefine mandatory-security application policy; hard bounce never mutates canonical Account email. | `PT-269...273`, `337`; `WD-181..183` |
| `COMM-PROOF-W30` | No automatic SMS/WhatsApp/in-app substitution for email verification or recovery exists without explicit future source/channel/permission policy. | `PT-274...281`; `WD-165..180` |
| `COMM-PROOF-W31` | Any future provider batch preserves independent per-recipient operation identity/outcome/ambiguity and cannot be blindly retried as one unit. | `PT-292...295`; `WD-185..186` |
| `COMM-PROOF-W32` | Two-node correction/rebind + provider failover creates at most one new DeliveryAttempt and preserves historical attempt provenance. | `PT-331`; `WD-071`, `078`, `169`, `198` |
| `COMM-PROOF-W33` | Simultaneous Identity invalidation + C&M withdrawal + provider-attempt admission exhaustively satisfies the current-authority cutover theorem. | `PT-332`; `WD-188`, `198` |
| `COMM-PROOF-W34` | Crash after durable intent followed by content/provider changes resumes the same logical obligation under current admissible execution truth without replaying source issuance. | `PT-340`; `WD-004`, `076`, `196` |
| `COMM-PROOF-W35` | Before release, `OQ-036` provider/channel proof demonstrates callback authentication, ambiguity/reconciliation support, protected-link non-rewrite, suppression semantics, retry/rate behaviour and operational recovery satisfy the frozen provider-independent contract. | `PT-300`; `WD-187` |

### Proof classification note

This register is **not** the governed FP-001 proof classification and does not choose `REUSE_EXISTING_PROOF` versus `NEW_TRACER_BULLET`.

It is the Pre-JIT inventory of executable proof obligations that the later governed process must classify.

---

# 9. Completeness / stabilisation assessment

## Discovery outcome

**PASS — PARK BROAD COMMUNICATIONS PRE-JIT DISCOVERY.**

The detailed evidence ledger now contains:

```text
200 working designs
340 pressure tests
2 upstream working deltas
8 major pressure-test clusters
1 final combined adversarial sweep
```

The final sweep found:

- no third required Communications business Resource;
- no additional higher-authority amendment;
- no conditional dossier that must be pulled forward for the current required FP-001 path;
- no provider choice required to state the business contract;
- no reason to continue ordinary broad scenario invention.

## Stable Resource conclusion

For current required FP-001 Communications:

```text
DURABLE BUSINESS RESOURCES
→ MessageIntent
→ DeliveryAttempt
```

Required non-Resource concepts/mechanisms include:

```text
protected delivery capability where required
bounded channel vocabulary
typed thin channel/provider adapter
exact content/locale binding
current owner revalidation
retry/reconciliation machinery
operator/support projections
bounded Audit linkage
observability
```

Not currently justified as FP-001 Communications Resources:

```text
SubscriberContact
NotificationPreference
InAppNotification
CommunicationJourney
Channel
Provider
ProviderRoute / ProviderFailoverPolicy
ChannelDelivery
ContentBinding
RenderedMessage / RenderSnapshot
DeliveryReconciliationCase
OperatorAction
SupportCase
Incident
ProviderWebhookEvent
ProviderRawPayload
RetryBudget
ProviderOutage
RecoveryWorkflow / DeliveryCase
```

## Governed JIT readiness

**BLOCKED / STOP.**

Do not draft/final-certify the governed Communications JIT dossier as if all upstream seams were clean.

Resolve/routinely govern first:

```text
COMM-UPD-001
COMM-UPD-002
```

After those are resolved, re-check live GitHub authority and verify that their successors do not invalidate this compact register.

## Reopen rule

Reopen broad Communications discovery only for:

1. changed live authority;
2. changed FP-001 scope;
3. `COMM-UPD-001` or `COMM-UPD-002` resolution that materially changes the seam;
4. contradiction discovered while drafting the governed dossier;
5. implementation/proof evidence that falsifies an accepted design;
6. activation of a conditional branch such as accountless marketing or SMS/WhatsApp.

Otherwise, additional broad Grill-Me rounds are now more likely to create speculative complexity than materially improve confidence.

## Recommended next governed action

The next work should be **upstream correction resolution**, not Communications dossier drafting:

1. prepare the smallest safe Identity v0.1.3 successor/correction for `COMM-UPD-001`;
2. prepare/freeze the Identity scanner/prefetch-safe proof-consumption contract for `COMM-UPD-002`;
3. independently review those changes against current Product/Architecture/Domain/FP-001 authority;
4. once accepted/current, revalidate this v0.10.0 consolidation against the new live `main`;
5. only then decide whether the Communications governed JIT dossier can move from `BLOCKED / STOP` to drafting/finalisation.

---

# Appendix A — Traceability by discovery pass

| Detailed pass | Working-design range | Pressure-test range | Main subject |
|---|---:|---:|---|
| foundational / v0.2 | `COMM-WD-001...027` | `COMM-PT-001...027` | durable handoff, intent/attempt, ambiguity, proof races, email-change, resend/idempotency |
| v0.3 | `COMM-WD-028...046` | `COMM-PT-028...052` | closure, deletion, retention, restore, merge |
| v0.4 | `COMM-WD-047...067` | `COMM-PT-053...084` | accountless contacts, consent, preference, quiet hours/frequency caps |
| v0.5 | `COMM-WD-068...091` | `COMM-PT-085...124` | content, locale, rendering, protected interpolation |
| v0.6 | `COMM-WD-092...120` | `COMM-PT-125...185` | provider outage, backlog, retry, operator recovery |
| v0.7 | `COMM-WD-121...157` | `COMM-PT-186...244` | Audit, observability, operator evidence, scanner/prefetch |
| v0.8 | `COMM-WD-158...187` | `COMM-PT-245...300` | channel/provider-independent architecture, in-app exclusion, future channels |
| v0.9 | `COMM-WD-188...200` | `COMM-PT-301...340` | combined adversarial falsification and stabilisation |

# Appendix B — Current working status

```text
LIVE AUTHORITY PIN
3f899e00ecfdfb9abc0794cffcb19eaff2726d58

COMMUNICATIONS PRE-JIT BROAD DISCOVERY
PASS / PARKED

COMMUNICATIONS COMPACT WORKING REGISTER
v0.10.0

REQUIRED DURABLE FP-001 COMMUNICATIONS RESOURCES
MessageIntent
DeliveryAttempt

PRIVACY & CONSENT DOSSIER
CONDITIONAL / NOT PULLED FORWARD

CONTENT & MEDIA DOSSIER
CONDITIONAL / NOT PULLED FORWARD

AUDIT & EVIDENCE DOSSIER
CONDITIONAL / NOT PULLED FORWARD

ANALYTICS DOSSIER
NO

COMM-UPD-001
REQUIRED

COMM-UPD-002
REQUIRED

GOVERNED COMMUNICATIONS JIT FINAL CERTIFICATION
BLOCKED / STOP

PHASE 7C
BLOCKED / STOP
```
