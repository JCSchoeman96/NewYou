# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.18.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.18.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 17 - operator correction / source-authority exception semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.17.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose:** append one focused operator-correction/source-authority pass while preserving Passes 1-16 and their accepted working-lock boundaries.

> This is an append-only semantic successor. It does not override Product, Architecture, Domain, Roadmap, current Open Work or approved Feature Pack/JIT authority.

> An operator, facilitator, moderator, support agent, developer or administrator may act through an owning Domain where policy permits. The role or UI surface does not itself become a new owner, and correction does not suspend the one-owner rule.

---

# 134. Accepted working-lock status entering Pass 17

The user explicitly accepted Pass 16 and instructed the stream to continue.

Therefore Passes 1-16 are:

`WORKING_LOCKED / NON-AUTHORITATIVE`

Pass 17 inherits without reopening:

- every durable business truth has exactly one authoritative owner;
- admin/support/operator screens are operating projections, not business Domains;
- Programmes owns Programme/Edition/Enrolment/completion truth;
- HJP owns habit/journal/progress source truth and staff may not silently rewrite participant history;
- Events owns attendance/check-in;
- Safety owns safety outcomes/restrictions/overrides;
- Entitlements owns access/grant/revocation;
- Content owns published content/version/translation correction and withdrawal;
- Communications owns message intent/preferences/delivery evidence;
- Audit may append evidence but never becomes source authority;
- source correction and Programme consequence are distinct;
- `PRG-GAP-002` remains the post-award consequence gap;
- `PRG-GAP-009` is the narrowed generic operator-correction question for this pass; and
- full duplicate/retry/reordering proof remains downstream.

---

# 135. Pass 17 - operator correction / source-authority exception semantics

## 135.1 Scope hard stop

This pass decides the semantic owner rules for operator correction, including direct versus additive/superseding correction, source-versus-derived correction, exemptions/substitutions versus generic override, Safety/Entitlement/Event/HJP/Content/Communications owner boundaries, audit provenance, participant dispute/review, downstream reconciliation and `PRG-GAP-009`.

It does **not** decide exact Ash actions/resources, role matrices, approval thresholds, optimistic locking, idempotency/retry/conflict implementation, Edition cancellation/transfer/refund policy, final post-award certificate policy, retention schedules, professional-record addendum mechanics, incident/support-ticket architecture, or a generic shared correction engine.

---

# 136. Pass-17 authority evidence

| ID | Evidence | Consequence |
|---|---|---|
| `PRG-EV-256` | **Live authority baseline reconfirmed** | Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413`. README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` continue to route Product Law v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and Platform Operating Model v1.0.1 as current authority. The Programmes/Learning ledgers remain working/non-authoritative. |
| `PRG-EV-257` | **Operating surfaces do not create business ownership** | Platform Operating Model v1.0.1 states that administration, support screens, dashboards and work queues are UI/operating projections, not Domains, and that cross-domain action invokes the owning Domain rather than turning the operating UI into a second business-write API. |
| `PRG-EV-258` | **Administration is explicitly not a Domain** | Domain Law says `Administration` is not a business Domain: admin/support screens invoke owning Domains under policy. Therefore an operator console cannot become a generic correction owner merely because it presents many domains on one screen. |
| `PRG-EV-259` | **Every durable truth still has exactly one command owner** | Domain Law requires one owner per durable business truth and says cross-domain writes invoke the owning Domain application interface. A correction does not create an exception to the single-owner rule. |
| `PRG-EV-260` | **Derived/provider/UI state never becomes correction authority** | Domain Law explicitly prevents projections, caches, Analytics, PubSub observations and external-provider state from becoming hidden business authority. An operator may observe such evidence, but correction must resolve through the true owner. |
| `PRG-EV-261` | **Record correction policy already distinguishes mutation modes** | `DEC-241` locks the rule: use direct updates only where appropriate and additive or superseding corrections for immutable, professional and financial records. There is no authority for universal destructive overwrite. |
| `PRG-EV-262` | **Audit evidence records sensitive actions but does not own source truth** | Domain Law assigns Audit & Evidence append-only audit/security evidence while preserving source-domain authority. Audit can prove that a correction happened; it cannot perform or reverse the underlying Programme, Safety, HJP, Entitlement, Event or Communications business transition. |
| `PRG-EV-263` | **HJP history may not be silently rewritten** | Product Law explicitly says staff may not alter participant habit-occurrence history silently. This establishes a strong correction invariant: where HJP history is corrected, correction provenance must remain distinguishable from the original participant/system history. |
| `PRG-EV-264` | **Safety override remains a Safety & Eligibility command** | Domain Law assigns `Safety case/restriction/override` to Safety & Eligibility as COMMAND owner. Programmes and Professional Care may consume or request consequences, but an admin/facilitator cannot manufacture a Safety override inside Programme state. |
| `PRG-EV-265` | **Professional Care requests owner transitions rather than acquiring them** | Domain Law keeps practitioner professional-review outcomes in Professional Care while downstream Safety override/clearance and Plan changes are requested through their respective owners. Professional authority does not collapse Domain ownership. |
| `PRG-EV-266` | **Published Content corrections preserve immutable version history** | Content & Media lifecycle keeps published governed versions immutable and advances them through supersession/withdrawal. An operator fixing Programme-visible content therefore invokes Content correction; Programmes does not edit the published body in place. |
| `PRG-EV-267` | **Communications correction remains Communications truth** | Message intent, delivery attempt and provider evidence remain Communications-owned. An operational dashboard may surface delivery ambiguity/failure, but Programmes cannot mark a provider attempt delivered or rewrite message history to repair participant state. |
| `PRG-EV-268` | **Entitlement/access correction remains Entitlements-owned** | Domain Law assigns entitlement/access grant, validity, expiry and revocation to Entitlements. Programme operators cannot grant or restore access by editing Enrolment or completion; they must request the Entitlements owner where a real access correction is authorised. |
| `PRG-EV-269` | **Attendance correction remains Events & Live-owned** | Domain Law assigns attendance/check-in to Events & Live, with Programmes as a reader. If attendance evidence is wrong, Events corrects its source truth and Programmes re-evaluates any requirement that consumes that attendance. |
| `PRG-EV-270` | **Programmes may correct only Programmes-owned truth** | Programme/challenge definition/version, Edition/Cohort/Enrolment and completion are Programmes & Challenges truths. A governed Programmes correction may therefore change those owner-owned records where the lifecycle permits it, but cannot fabricate foreign evidence or bypass owner rules. |
| `PRG-EV-271` | **Correction and downstream consequence are separate transitions** | Where a source owner corrects HJP occurrence, attendance, Safety, Content, Entitlement or Communications truth, Programmes must consume the corrected owner truth and re-evaluate its consequence. The safe mechanism is not a staff patch to both source and derived Programme state. |
| `PRG-EV-272` | **Roadmap treats correction/recovery as product capability, not admin magic** | Roadmap doctrine says support, correction, withdrawal, incident handling, audit, recovery and release controls are part of operational capability rather than optional extras. That obligation still composes through the owning Domains. |
| `PRG-EV-273` | **Operator groupings remain navigation projections** | Frontend/Operating contracts treat Command Centre/Work/People/Programmes/Communications/Audit groupings as navigation and operating projections. A combined operator workspace therefore does not imply combined write authority. |
| `PRG-EV-274` | **Sensitive operator access must remain scoped and auditable** | Current Product/Domain/Operating rules repeatedly restrict sensitive staff access and require audit/MFA for privileged operations. A correction path that exposes private journal, health, professional or delivery evidence merely for convenience is not justified. |
| `PRG-EV-275` | **Correction, exception, override and adjudication are not synonyms** | `DEC-241` covers record correction; Safety override has its own Safety-owned lifecycle; Programme exemptions/substitutions have Programme semantics; professional outcomes have Professional Care semantics. A generic `override=true` action would collapse distinct business meanings. |
| `PRG-EV-276` | **Current authority wins over stale operator forms/projections** | Because projections are not authority and every command goes through the owner, a correction request must validate against current owner state. A stale support page or cached row cannot overwrite a newer authoritative transition merely because it was opened first. |
| `PRG-EV-277` | **Historical corrections must not falsify time** | A later correction may have an earlier business-effective time where the owning Domain legitimately establishes that fact, but the correction itself has a later recorded/adjudicated time. Backdating the audit/correction act would destroy explainability. |
| `PRG-EV-278` | **Post-award consequence remains an existing separate gap** | Passes 8/14 already preserve `PRG-GAP-002` for what happens when corrected source/completion truth undermines an already-issued certificate/outcome. Pass 17 may define how corrections reach Programmes without pretending that post-award policy is now solved. |
| `PRG-EV-279` | **Privacy orchestration does not acquire record-level correction authority** | Domain doctrine says cross-cutting orchestration such as deletion may request owner transitions without owning the records. The same principle prevents a Privacy/support workflow from directly rewriting Programme/HJP/Content history outside the owner contract. |
| `PRG-EV-280` | **Existing authority is sufficient to resolve the generic operator seam** | Operating Model, Domain Law, `DEC-241`, HJP no-silent-history rules, owner-specific override/correction lifecycles and Audit separation already answer who may correct what. Exact roles, action names, policies, approvals, schemas and concurrency mechanics remain later JIT/proof rather than a new Product/Architecture/Domain gap. |

---

# 137. Pass-17 semantic model

## 137.1 Owner-mediated correction

```text
operator / dispute / reconciliation signal
        |
        v
owning Domain validates actor + current state + correction semantics
        |
        +--> direct correction where mutable truth permits
        |
        +--> additive/superseding correction where history/immutability requires
        |
        v
owner-owned corrected truth
        |
        v
dependent Domains re-evaluate their own consequences
        |
        v
minimum Audit/projection consequence
```

The operator surface is never a new authority layer.

## 137.2 Distinguish the operation type

| Operation | Meaning | Rule |
|---|---|---|
| Observation/explanation | Read current/history/provenance for support | Scoped read only; no mutation authority follows |
| Record correction | Fix owner-owned fact that was wrong | Owning Domain chooses direct vs additive/superseding |
| Business exception | Exemption/substitution/reopen where actually authorised | Domain-specific action; never generic `override` |
| Adjudication/override | Safety/professional/governed outcome change | Outcome owner remains command owner |
| Downstream reconciliation | Recompute consequences after source correction | Dependent Domain updates only its own consequence |

## 137.3 Programmes correction boundary

Programmes may correct Programmes-owned Enrolment/Edition/completion truth through Programmes actions where lifecycle rules permit. It does not correct HJP occurrences/private journals, Event attendance, Safety restrictions/overrides, Entitlements, Content publication/translation, Communications provider evidence, canonical Identity or Commerce payment/refund truth.

A Programme page may expose an owner-routed action for those truths. That is orchestration, not ownership.

## 137.4 Provenance and time

Where material, preserve original participant/provider/system/professional assertion, later operator request, owner correction/adjudication and downstream Programme reconciliation as distinct facts. A corrected business fact may legitimately have an earlier effective time, but the later correction/adjudication time must not be falsified or backdated.

## 137.5 Reconciliation beats downstream patching

When a source owner corrects truth, Programmes reads the corrected source, re-evaluates ProgrammeVersion rules and records its own consequence. Do not manually patch both source and Programme completion.

## 137.6 Audit proves action; Audit does not authorise action

Sensitive correction may append minimum actor/reason/scope/result evidence where required. Audit still does not become owner of the corrected truth.

---

# 138. Pass-17 pressure tests

| ID | Scenario | Expected invariant / adjudication | Disposition |
|---|---|---|---|
| `PRG-PT-677` | Facilitator clicks `mark complete` for a habit-based activity | A facilitator cannot manufacture HJP occurrence evidence. If Programmes later permits operator-attested Programme satisfaction, that must be an explicit Programmes-owned evidence type and remain distinct from HJP history. | `REJECT GENERIC MARK-COMPLETE` |
| `PRG-PT-678` | Support changes a missed habit occurrence to completed | HJP owns occurrence truth and Product Law forbids silent staff history rewriting. Any legitimate HJP correction must go through HJP with provenance/reason, not support-side overwrite. | `REJECT` |
| `PRG-PT-679` | HJP corrects a duplicate participant occurrence | An owner-defined HJP correction may remove/supersede the duplicate effect while preserving correction provenance. Programmes then re-evaluates consumed evidence if material. | `PASS / OWNER CORRECTION` |
| `PRG-PT-680` | Programme admin patches completion after HJP source correction | Do not patch derived completion independently. Programmes should re-evaluate from corrected HJP evidence under ProgrammeVersion rules and record its own resulting transition. | `REJECT DERIVED PATCH` |
| `PRG-PT-681` | Admin removes a Safety restriction from a Programme screen | Safety restriction/override is Safety & Eligibility COMMAND truth. The Programme surface may request/read the result but cannot mutate it. | `REJECT` |
| `PRG-PT-682` | Authorised practitioner requests Safety clearance | Professional Care may supply a professional outcome/request, but Safety & Eligibility performs the actual override/clearance transition and Programmes consumes current Safety authority. | `PASS / OWNER-MEDIATED` |
| `PRG-PT-683` | Support extends entitlement because an enrolment looks wrong | Entitlements owns access validity. Correct the owning Entitlement if authorised; do not simulate access by changing Enrolment/completion. | `REJECT CROSS-OWNER WRITE` |
| `PRG-PT-684` | Programme operator corrects an imported Enrolment start date | If the date is genuinely Programmes-owned and the lifecycle permits correction, an owner action with actor/reason/provenance may correct it. Downstream schedules are reconciled separately. | `PASS / OWNER CORRECTION` |
| `PRG-PT-685` | Support engineer fixes state with direct SQL | Operating UI/support is not a second business-write API. Direct persistence mutation bypasses owner invariants/audit and is not an accepted operational correction mechanism. | `REJECT` |
| `PRG-PT-686` | Operator console invokes a Programmes correction action | A single UI may invoke the owner boundary. The action remains Programmes-owned, policy-checked and audited; the console itself gains no Domain authority. | `PASS` |
| `PRG-PT-687` | Operator edits an active historical ProgrammeVersion in place | Version-pinned participant semantics cannot be silently rewritten. Material governed structure/rule change requires the appropriate version/supersession path, not in-place history mutation. | `REJECT` |
| `PRG-PT-688` | Operator fixes non-semantic Programme display metadata | A direct update can be acceptable where the owning Domain classifies the field as mutable and participant-semantic/history invariants are unaffected, consistent with DEC-241. | `PASS IF OWNER POLICY ALLOWS` |
| `PRG-PT-689` | Content editor fixes a typo in already-published lesson body | Published Content versions are immutable. Correct by Content-owned superseding/withdrawal/versioning semantics and preserve historical delivered provenance. | `PASS VIA CONTENT OWNER` |
| `PRG-PT-690` | Programme admin marks a failed provider delivery as delivered | Delivery attempt/provider evidence is Communications truth. Programme cannot rewrite it; Communications may reconcile ambiguous provider evidence under its owner contract. | `REJECT` |
| `PRG-PT-691` | Communications operator corrects an ambiguous provider attempt | A Communications-owned reconciliation/correction may change Communications delivery disposition while preserving provider/correction evidence; it cannot create Programme progress. | `PASS / OWNER CORRECTION` |
| `PRG-PT-692` | Event attendance was recorded against the wrong participant | Events & Live corrects attendance/check-in truth with provenance. Programmes re-evaluates any attendance-based requirement; Programme admin does not rewrite attendance. | `PASS / OWNER CORRECTION` |
| `PRG-PT-693` | Programme operator uses a Community moderator note as completion evidence | A moderator note is not automatically Programme evidence. Only an explicitly approved source/evidence contract can satisfy the requirement. | `REJECT` |
| `PRG-PT-694` | Source evidence is later deleted under governed privacy lifecycle | The owner/deletion contract governs source deletion. Programmes must not retain hidden raw copies to defeat deletion; minimum historical satisfaction provenance remains bounded by existing lifecycle/retention gates. | `PASS WITH EXISTING GATES` |
| `PRG-PT-695` | Participant disputes a completion record | The dispute may start an owner-defined review/correction flow. It does not itself overwrite source or completion truth before adjudication. | `PASS / REVIEW NOT OVERWRITE` |
| `PRG-PT-696` | Operator double-submits the same correction | One logical correction must not create duplicate business effects or duplicate downstream awards. Exact idempotency/concurrency proof is reserved for Pass 18/JIT. | `PASS / JIT PROOF` |
| `PRG-PT-697` | Two authorised operators submit conflicting corrections | The owning Domain must resolve current authority deterministically and preserve both attempts/evidence as appropriate; last UI submit cannot be assumed authoritative by arrival order. | `PASS / PASS-18 PROOF` |
| `PRG-PT-698` | Operator submits a stale correction after a newer source transition | The owner action must validate current state/version/guards and fail or reconcile safely. A stale form cannot overwrite newer authority. | `REJECT STALE OVERWRITE` |
| `PRG-PT-699` | Attendance correction is entered after certificate issuance | Events corrects source truth; Programmes re-evaluates. Any consequence for an already-issued award remains `PRG-GAP-002`, not a support-side delete/reissue shortcut. | `PASS / GAP-002` |
| `PRG-PT-700` | Support revokes a certificate because a reminder email failed | Communications failure is not Programme completion authority. No certificate consequence follows from delivery failure alone. | `REJECT` |
| `PRG-PT-701` | Operator grants an exemption because a participant asks nicely | Compassion is not generic override authority. Exemption must exist in Programme rules, actor policy and recorded reason/evidence; otherwise the action is unauthorised. | `REJECT` |
| `PRG-PT-702` | Programmes executes an explicitly authorised exemption action | Where ProgrammeVersion/policy permits an exemption and the actor is authorised, Programmes may record the exemption as its own durable truth with reason/provenance; it does not rewrite source evidence. | `PASS` |
| `PRG-PT-703` | Staff substitutes one activity for another ad hoc | Substitution requires explicit Programme semantics/accepted substitute policy. Operator discretion cannot invent equivalent evidence by label similarity. | `REJECT` |
| `PRG-PT-704` | Staff changes `required` to `optional` for one active participant | Do not mutate ProgrammeVersion requirement semantics per participant. Use an authorised exemption/substitution/waiver-style Programme action only if Product/Programme rules actually permit it. | `REJECT RULE MUTATION` |
| `PRG-PT-705` | Facilitator edits the Edition release date from Communications dashboard | Edition schedule is Programmes truth. Communications/dashboard may request a Programmes change but cannot alter schedule authority. | `REJECT` |
| `PRG-PT-706` | Authorised Programme operator postpones an Edition | If the owning Edition lifecycle permits postponement, Programmes records it and downstream Communications/Events/etc reconcile. Exact cancellation/transfer consequences remain later. | `PASS / OWNER ACTION` |
| `PRG-PT-707` | One admin button cancels Edition and refunds all purchases | A composite workflow may orchestrate multiple owner commands, but Programmes cannot write Commerce refund truth. Partial failure/retry semantics are Pass 18/later cancellation work. | `PASS ONLY AS ORCHESTRATION` |
| `PRG-PT-708` | Support fixes purchaser/participant mismatch by changing participant identity | Identity, Commerce and Programmes truths must be corrected through their respective owners. A generic support reassignment cannot rewrite all three stores. | `REJECT SHARED WRITE` |
| `PRG-PT-709` | Programme operator changes canonical account email | Canonical identity/email is Identity & Access truth. Programme UI may deep-link/request the owner flow but cannot update it. | `REJECT` |
| `PRG-PT-710` | Operator edits participant language and rewrites historical delivered locale | Current preference may be changed only by its owning profile/identity contract; historical content/message delivery provenance must remain what actually occurred. | `REJECT HISTORY REWRITE` |
| `PRG-PT-711` | Correction note copies private journal prose into Programme admin history | Private journal content remains HJP/private data. Correction records use minimum necessary references/reasons, not copied prose. | `REJECT` |
| `PRG-PT-712` | Facilitator reads private journal text to decide exemption | Private journal access is not implied by Programme role. Unless an entry was lawfully shared and Programme rules explicitly require approved evidence, do not expose/browse it. | `REJECT` |
| `PRG-PT-713` | Zoom/provider CSV says attendee was present | Provider evidence does not directly complete Programme activity. Events & Live reconciles attendance truth first; Programmes reads that authoritative result. | `PASS VIA EVENTS` |
| `PRG-PT-714` | Programme admin manually sets attendance=true | Attendance is Events & Live truth. Even if the control appears on a Programme page, it must invoke an authorised Events correction, not write Programme-local attendance. | `REJECT LOCAL COPY` |
| `PRG-PT-715` | Support clears Safety block because participant signs disclaimer | Participant acknowledgement does not grant support staff Safety override authority. Safety owner/professional policy remains controlling. | `REJECT` |
| `PRG-PT-716` | Governed professional clearance changes Safety outcome | Safety & Eligibility records the new/overridden outcome; Programmes re-evaluates availability/requirements as a consequence. Historical restricted state remains explainable. | `PASS` |
| `PRG-PT-717` | Programme screen changes reminder preference | Reminder/channel/category preference belongs Communications. A Programme screen may invoke Communications owner action with correct scope; no duplicate Programme preference truth is created. | `PASS VIA OWNER` |
| `PRG-PT-718` | Operator clicks `unsubscribe all marketing` but only flips one channel flag | Participant-visible scope matters. A purpose-level withdrawal must route to Privacy & Consent; changing only a Communications preference would not implement the represented action. | `REJECT SEMANTIC MISMATCH` |
| `PRG-PT-719` | Programme admin republishes a withdrawn translation | Content publication/translation is Content & Media authority. Programmes cannot resurrect withdrawn content to make an activity available. | `REJECT` |
| `PRG-PT-720` | Support deletes completion row so participant can retry | Do not repair lifecycle by deleting authoritative history. Use Programmes owner correction/reopen/recovery semantics if such an action exists and preserve provenance. | `REJECT` |
| `PRG-PT-721` | Sensitive correction is recorded with actor/reason and minimum audit evidence | This matches owner-mediated correction plus Audit evidence. Audit proves the action but does not become source truth. | `PASS` |
| `PRG-PT-722` | Audit service writes a new completion state during incident recovery | Audit & Evidence cannot mutate source truth. Recovery must invoke Programmes or the relevant owner; Audit records the evidence. | `REJECT` |
| `PRG-PT-723` | Analytics dashboard backfills completion to match a KPI | Analytics is derived. A metric discrepancy cannot author Programme truth; investigate/correct the source owner and rebuild projections. | `REJECT` |
| `PRG-PT-724` | Search/cache still shows old completion after correction | The stale projection should be invalidated/rebuilt from current authority. Do not change source truth again merely to make the projection agree. | `PASS / PROJECTION REPAIR` |
| `PRG-PT-725` | Programme correction succeeds but downstream Entitlement consequence fails | Do not fake a shared cross-domain transaction by rewriting one owner. Preserve source transition and reconcile the failed consequence idempotently; full concurrency/retry proof is Pass 18. | `PASS / PASS-18 PROOF` |
| `PRG-PT-726` | Operator retries a correction command after timeout | The owner must prevent duplicate durable effects and return/reconstruct the current result where possible. Exact idempotency key/transaction/retry mechanics remain Pass 18/JIT. | `PASS / PASS-18 PROOF` |

---

# 139. Pass-17 gap adjudication

## `PRG-GAP-009` - SEMANTICALLY RESOLVED / REPRESENTATION DEFERRED

There is **no universal administrator `mark complete` / `override` / `fix state` authority**.

The controlling contract is owner-defined correction/action + scoped actor policy + current-state guard + appropriate correction semantics + explicit dependent-domain reconciliation + minimum audit evidence.

Therefore:

- Programmes corrects only Programmes-owned truth;
- HJP correction remains HJP-owned and cannot silently rewrite participant history;
- attendance correction remains Events-owned;
- Safety override remains Safety-owned;
- access correction remains Entitlements-owned;
- content correction remains Content-owned;
- delivery correction remains Communications-owned;
- Audit records but does not perform business correction;
- a role-scoped UI may orchestrate owner actions without becoming a shared-write Domain.

Exact action names, role matrices, approvals, optimistic locking, idempotency and conflict handling remain JIT/Pass 18 proof.

## `PRG-GAP-002` - remains open

A corrected source/completion may undermine an already-issued certificate/outcome. Pass 17 defines how corrected truth reaches Programmes but does not decide revocation, reissue, participant notice, appeal or historical display.

## `PRG-GAP-003` - remains separate

Edition cancellation/transfer/refund policy is not replaced by generic operator correction. Composite workflows still invoke each owner.

## `PRG-GAP-007` - remains lifecycle-gated

Correction history must not retain hidden raw journal/health/content payloads. Minimum provenance surviving deletion/de-linking remains subject to existing retention/deletion/professional-record gates.

## `PRG-GAP-011` - remains separate

An operator cannot resurrect/replace withdrawn required content inside Programmes to manufacture completion.

**No new Product, Architecture, Domain, `PRG-GAP` or `PRG-UPD` is promoted.**

---

# 140. Pass-17 refinements

| ID | Refinement | Working conclusion |
|---|---|---|
| `PRG-REF-205` | **Admin/support UI remains a projection, never a correction owner** | A combined operator surface may expose actions from many Domains but cannot become an alternate write boundary. |
| `PRG-REF-206` | **Every correction command enters through the owning Domain** | Cross-domain operators request owner transitions; they do not write foreign persistence or shadow truth. |
| `PRG-REF-207` | **Correction mode follows record semantics** | Use direct update only where owner policy permits; use additive/superseding correction where immutability, professional/financial history or reproducibility requires it. |
| `PRG-REF-208` | **Original assertion and later correction remain distinguishable where history matters** | Do not erase whether the original value came from participant, provider, system, practitioner or operator when the distinction is material. |
| `PRG-REF-209` | **Programmes corrects only Programme-owned truth** | Enrolment, Edition and Programme completion can have owner-defined corrections; HJP occurrence, attendance, Safety, Entitlement, Content and Communications truth stay with their owners. |
| `PRG-REF-210` | **Foreign source corrections trigger explicit Programme re-evaluation** | When an authoritative input changes, Programmes recomputes/reconciles its own consequence instead of accepting a staff patch to both layers. |
| `PRG-REF-211` | **No generic `mark complete` may fabricate source evidence** | Any operator-attested Programme evidence must be an explicitly authorised Programme evidence type, not a disguised HJP/Event/Community/Communication fact. |
| `PRG-REF-212` | **Safety override remains Safety-owned** | Programme/support/practitioner surfaces may request or display Safety outcomes but never directly toggle Safety authority. |
| `PRG-REF-213` | **Entitlement correction remains Entitlements-owned** | Access is not repaired by Enrolment/completion edits. |
| `PRG-REF-214` | **Attendance correction remains Events-owned** | Programmes consumes corrected attendance as an input; it does not own the attendance record. |
| `PRG-REF-215` | **HJP correction must never be silent** | Staff-originated correction is distinguishable and preserves the participant-history invariant. |
| `PRG-REF-216` | **Published Content correction uses supersession/withdrawal rather than mutation** | Historical delivery remains tied to the actual immutable content/locale version. |
| `PRG-REF-217` | **Communications correction changes delivery truth only** | Provider reconciliation cannot manufacture Programme progress or participant action. |
| `PRG-REF-218` | **Read/explain authority is not mutation authority** | Seeing a value in a role-scoped dashboard does not imply permission to correct it. |
| `PRG-REF-219` | **Sensitive correction uses least privilege and minimum evidence** | Correction workflows must not broaden access to private journal, Health, professional or provider data beyond what the action needs. |
| `PRG-REF-220` | **Correction time and business-effective time are separate when needed** | Never falsify the fact that an operator correction was recorded later merely because it establishes an earlier effective fact. |
| `PRG-REF-221` | **Correction cannot invent exemption/substitution/waiver semantics** | Those are Programme business meanings with explicit rules, not generic operator escape hatches. |
| `PRG-REF-222` | **Participant dispute starts review, not automatic overwrite** | Dispute, review, correction and final owner truth remain distinct lifecycle concepts. |
| `PRG-REF-223` | **Post-award correction routes to existing `PRG-GAP-002`** | Pass 17 defines source-to-Programme reconciliation but does not decide certificate revocation/reissue/notice policy. |
| `PRG-REF-224` | **Audit evidence proves the correction without owning it** | Actor, reason, scope and outcome evidence may be appended centrally where required; source Domain remains authoritative. |
| `PRG-REF-225` | **Resolve `PRG-GAP-009` semantically** | There is no generic admin override/mark-complete authority. The safe contract is owner-defined correction/action + scoped actor policy + provenance/audit + downstream reconciliation. |
| `PRG-REF-226` | **Exact role matrices and duplicate/conflict mechanics remain downstream** | Ash action names, permission matrices, approval thresholds, optimistic locking, idempotency keys and retry/reordering proof remain JIT and Pass 18 rather than new Product/Domain law. |

---

# 141. Pass-17 anti-admin-engine / YAGNI outcome

Pass 17 rejects:

- a new Administration Domain;
- a generic `admin_override` authority/table;
- universal `mark_complete`, `force_pass` or `force_eligible`;
- generic cross-domain `correct_record(resource, id, attrs)` business APIs;
- support direct database writes as normal correction;
- shared-write operator transactions across Domain tables;
- duplicated HJP/Event/Safety/Entitlement/Communications truth inside Programmes;
- copied private journal/Health payloads in correction notes;
- Audit as rollback/source-of-truth;
- Analytics as authority to backfill source records;
- destructive overwrite of immutable published/professional/financial history;
- backdating correction acts;
- operator notes automatically equalling participant/provider evidence;
- ad hoc exemptions/substitutions without Programme rules;
- resurrecting withdrawn content through Programme admin controls;
- certificate consequence from downstream communication failure;
- cross-domain ownership transfer because controls share one page;
- a generic correction microservice/workflow engine detached from owners;
- solving Pass-18 concurrency/retry mechanics prematurely.

The simplest correct model is owner-mediated correction + explicit downstream reconciliation + minimum audit evidence.

---

# 142. Pass-17 disposition

**Outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Passes 1-16 remain accepted/working-locked and Pass 17 does not reopen them.
2. Operator/admin/support/facilitator/moderator UI is a projection and never becomes a business Domain or alternate write API.
3. Every correction changing durable truth is executed by the Domain owning that truth.
4. Cross-domain correction is orchestration of owner actions, not shared-write mutation.
5. `DEC-241` governs correction shape: direct update only where appropriate; additive/superseding correction where history/immutability requires it.
6. Original participant/provider/system/professional assertions and later correction provenance remain distinguishable where material.
7. Correction/adjudication time is not silently backdated even when an owner establishes an earlier effective business time.
8. Programmes may correct only Programmes-owned Enrolment/Edition/completion truth through Programmes lifecycle/actions.
9. Programmes cannot correct HJP, Events attendance, Safety override, Entitlements, Content publication/translation, Communications provider evidence or canonical Identity truth.
10. A Programme page may invoke another owner's correction action without acquiring its authority.
11. HJP corrections must never be silent; staff correction provenance remains distinguishable.
12. Attendance correction remains Events-owned; Programmes re-evaluates attendance-based requirements afterward.
13. Safety restriction/override remains Safety-owned even when requested by a practitioner or displayed in Programme operations.
14. Entitlement/access correction remains Entitlements-owned and cannot be simulated by Enrolment/completion edits.
15. Published Content correction remains Content-owned and uses governed supersession/withdrawal/versioning.
16. Communications delivery correction remains Communications-owned and never becomes Programme progress evidence.
17. Audit may append correction evidence but cannot perform/reverse/author the source business transition.
18. Read/explain access in an operator dashboard does not imply mutation authority.
19. Generic `mark complete`, `override`, `force pass` and `fix state` actions are rejected.
20. Operator-attested Programme evidence is permissible only if explicitly authorised and remains distinct from foreign source truth.
21. Programme exemption/substitution/recovery actions are business semantics, not generic operator escape hatches.
22. Participant dispute starts review/adjudication; it does not immediately overwrite authoritative history.
23. Source corrections propagate by owner correction followed by dependent-domain reconciliation.
24. Stale projections/forms cannot outrank newer owner truth; owner actions validate current state.
25. `PRG-GAP-009` is `SEMANTICALLY RESOLVED / REPRESENTATION DEFERRED`.
26. `PRG-GAP-002` remains open for post-award certificate/outcome consequence after corrected truth.
27. `PRG-GAP-003`, `PRG-GAP-007` and `PRG-GAP-011` remain separate seams and are not solved by admin override.
28. No new Product, Architecture, Domain, `PRG-GAP` or `PRG-UPD` is justified by this pass.
29. Exact role matrices, approvals, Ash actions, optimistic locking, idempotency and duplicate/conflict handling remain downstream JIT/proof.
30. Generic admin/correction engines, shared-write operator stores and cross-domain direct persistence mutation remain `DEFER_YAGNI` / rejected.

**Pass hard stop:** Pass 18 - concurrency / retry / reordering semantics - has not started. Do not pull full duplicate-command, conflicting-update, event reordering, crash/restart or cross-domain retry proof into this Pass-17 candidate beyond the minimum correction invariants stated here.

**Broad discovery remains unfrozen.** Later cancellation/transfer, historical reproducibility, analytics, FP-014 second-lens and final adversarial-convergence passes remain separate.