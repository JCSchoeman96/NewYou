# NewYou Assessment / Temperament Pre-JIT Contract — Working Consolidation v0.1.1

> **FINAL COMPACT WORKING CONTRACT / NON-AUTHORITATIVE — COMPRESSION-FIDELITY PATCH**
>
> **Implementation:** NOT AUTHORISED
>
> **Authority:** NONE

- **Pack version:** `v0.1.1`
- **Predecessor compact contract:** `NEWYOU_AT_PREJIT_CONTRACT_WORKING_v0.1.0.md` — Git blob `dabb549c2b768b9b94fb3123a946cffaa65baf03`
- **Patch scope:** restore durable guardrails that were preserved in deep discovery but compressed too aggressively in v0.1.0; no new Assessment / Temperament semantic decision is created here.
- **Deep discovery lineage:** `deep/NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.1.0.md` through `v0.23.1.md`
- **Latest deep classification source:** `v0.23.1` — Git blob `41da4e92f6bf61f73979303d394a9865d6d0158d`
- **Independent review result:** `PASS WITH NON-BLOCKING CORRECTIONS`
- **Live canonical authority pin used for consolidation:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Conflict rule:** live governed authority always wins; this contract never repairs an upstream contradiction silently.

## 1. Purpose and status vocabulary

This contract is the compact normal-context representation of the completed Assessment / Temperament documentary Pre-JIT. It preserves durable constraints needed for FP-003 planning without requiring routine loading of the full append-only discovery chain.

It intentionally distinguishes four classes of statement:

- **AUTHORITY-DERIVED / STABLE BOUNDARY** — supported by current Product/Decision/Architecture/Domain/Roadmap authority and safe to carry into JIT unless authority changes.
- **JIT / PROOF CONTRACT** — a downstream correctness invariant or owner-composition rule that may be represented in JIT without creating new Product policy.
- **CANDIDATE PRODUCT RESOLUTION** — coherent Pre-JIT recommendation that is not current Product Law and must be adjudicated upstream before JIT relies on it.
- **FUTURE-ONLY** — preserved design direction for a commercial/product promise not currently active.

A conceptual distinction below never implies a separate Ash Resource, table, worker, service, queue, cache or process.

## 2. Governing ownership

Every durable business truth retains exactly one authoritative owner.

| Truth | Owner | Boundary |
|---|---|---|
| Four-Colour methodology representation/version lifecycle | **Temperament** | Temperament stores/publishes approved method representation; substantive methodology authority comes from the governing IP agreement/delegation, not a platform role. |
| Assessment attempt, saved/submitted answers, producing execution context, raw score/result history | **Temperament** | Assessment truth is not entitlement truth. |
| Declared temperament profile and digital assessment result history | **Temperament** | Declared and digital sources remain distinct provenance classes. |
| Current selected eligible temperament source | **Temperament** | Selection is mutable participant choice; it does not mutate source history. |
| Commercial assessment right identity, validity, consumption/revocation/reconciliation | **Entitlements** | Temperament supplies lifecycle facts but does not restore, sum or mutate commercial rights directly. |
| Canonical participant identity / duplicate-account reconciliation | **Identity & Access** | Temperament consumes reconciliation outcomes; it does not identity-match. |
| Assessment reminder/delivery intent and provider evidence | **Communications** | Communications never becomes attempt-expiry or assessment-completion authority. |
| Governed report wording/content/translation artefacts | **Content & Media** where applicable | Content publication does not create methodology authority. |
| Purpose-specific consent, deletion/retention orchestration, full deletion | **Privacy & Consent** | Privacy lifecycle may remove retained immutable assessment evidence; orchestration does not acquire Temperament truth. |
| Cross-cutting evidence | **Audit & Evidence** where required | Evidence never becomes an alternate copy of source-domain business truth. |

Cross-domain writes route through the owning Domain. Projection, cache, provider, worker and UI state are never business authority.

## 3. Provenance pathways

### 3.1 Declared versus digital sources — AUTHORITY-DERIVED

The platform must preserve distinct source classes, including at least:

- participant self-report / declared profile;
- book-derived declaration where current Product permits it;
- digitally assessed result.

A declared profile:

- is not a digital assessment result;
- receives no fabricated exact digital score;
- receives no paid digital assessment report merely because the declared colour/profile is known;
- remains historical declaration provenance if a later digital assessment is completed.

A later digital assessment appends a distinct digital result. It does not upgrade, overwrite or relabel the declaration.

A meaningful later participant declaration appends declaration history rather than silently rewriting the earlier declaration. Declaration change remains distinct from a digital reassessment and does not itself consume a digital assessment right.

### 3.2 Current profile selection — AUTHORITY-DERIVED

The participant explicitly selects the current eligible profile source.

- A newly completed digital assessment never becomes current automatically.
- Changing current selection does not mutate source history or consume a reassessment right.
- If the currently selected source becomes invalid/ineligible/deleted, it becomes ineffective; the platform must not silently choose another source.
- Learned preferences or low-risk personalisation must never rewrite the provenance of the selected source.

### 3.3 Durable downstream provenance — JIT / PROOF CONTRACT

Where a durable materially personalised output depends on temperament in a way that matters to later explanation, correction or reproduction, the owning downstream contract must retain sufficient provenance to identify the eligible temperament source/current selection used when that output was produced.

A later declaration, assessment result or current-profile selection must not make an historical Plan, Programme or other durable output appear to have been produced from a different temperament source. This requirement does not make every transient page render a durable snapshot and does not transfer downstream business ownership to Temperament.

## 4. Attempt lifecycle

### 4.1 Attempt start — JIT / STABLE SEMANTIC

Opening the assessment, loading the shell or pressing a UI Start control does not itself create an authoritative Assessment Attempt.

The first **durably accepted scored answer** starts exactly one authoritative active attempt. That boundary:

- records the first accepted scored answer;
- pins the governed execution context;
- starts the fixed attempt lifetime;
- must converge under duplicate taps, retries and multi-device races;
- must leave at most one active attempt for the participant.

The **commercial right consequence** at this boundary is not universal current law; see §5 and `AT-UPD-001`.

### 4.2 Fixed expiry — AUTHORITY-DERIVED / JIT REFINEMENT

An unfinished active attempt has a fixed 30-day lifetime from the authoritative attempt-start boundary. The deadline does not slide when later answers are saved.

Expiry:

- closes ordinary work on that attempt;
- preserves retained attempt/answer history according to Privacy authority;
- does not itself invent a replacement right;
- does not depend on successful reminder delivery or participant engagement.

While an attempt is active, the participant-facing product must expose the exact authoritative expiry deadline and a persistent in-product route to resume/continue the authoritative attempt. Browser-local state is not proof of saved progress.

DEC-056 requires advance warning. Exact reminder cadence/channel is downstream Communications/JIT configuration subject to the Roadmap/OQ routing correction in `AT-UPD-005`.

### 4.3 One active attempt and recovery — AUTHORITY-DERIVED / JIT CONTRACT

Ordinary use permits at most one active attempt.

Failure classes must remain separate:

1. **Before authoritative attempt start:** no scored answer committed; no active attempt exists.
2. **Temporary failure during a still-valid attempt:** resume the same attempt under the same deadline and pinned context.
3. **Material genuine technical failure that makes the attempt unusable:** any successor/replacement/remediation must be explicit, preserve the original history and not merge answers into the successor.
4. **Ambiguous submit/outcome:** reconcile authoritative state before creating a replacement or assuming failure.
5. **Canonical result already exists:** recovery is result/report/delivery recovery only; never rescore merely because report delivery failed.
6. **Deletion completed:** technical recovery cannot resurrect deleted participant data.

The following are recovery guardrails, not a new commercial promise:

- a genuine technical failure is a demonstrated platform/system failure, corrupted or unrecoverable authoritative state, or material service failure that prevented normal completion; ordinary inactivity, change of mind, participant scheduling constraints, repeatedly closing the browser or loss of a personal device do not become technical failure merely because support is asked to reset the assessment;
- support may route or adjudicate only recovery/remedy paths authorised by the owning Product/Entitlements/Commerce authority and may not erase history or manufacture a reusable right directly;
- where governing authority establishes that a technical-recovery obligation already arose during an eligible started attempt, later ordinary subscription termination does not by itself erase that already-arisen obligation; the exact remedy remains owner-mediated;
- recovery/replacement and technical-failure refund are distinct remedies and are not automatically cumulative;
- a successor recovery attempt, where authorised, remains a distinct attempt with its own start, deadline and then-valid governed context; predecessor answers are not silently migrated across methodology/version boundaries.

Exact commercial remedy/refund consequences remain owner-mediated and must respect the governed right-type consumption rule.

## 5. Assessment-right consumption — CANDIDATE PRODUCT RESOLUTION / OPEN GAP

There is no safe universal consumption event yet.

Current authority contains competing signals:

- generic attempt-use wording points toward first-answer/attempt-start consumption;
- included plan/bundle credit wording points toward successful digital assessment delivery.

Therefore FP-003 JIT must not choose one event globally.

Product must adjudicate the authoritative consumption/fulfilment event by assessment-right type, including as applicable:

- ordinary standalone right;
- included plan/bundle assessment credit;
- Premium annual reassessment right;
- remediation/replacement right.

Whichever Product rule is selected:

- Entitlements remains the right owner;
- retries must be idempotent;
- crash windows must not double-consume or resurrect a right;
- Temperament records attempt/result/report lifecycle facts rather than directly restoring commercial credit.

`AT-WD-001` remains the working candidate for right types where Product adopts first-durable-scored-answer consumption. It is not universal current law.

## 6. Answer writes and concurrency — JIT / PROOF CONTRACT

Before accepted final submission, answers remain editable while the attempt is active and in deadline.

Concurrency invariants:

- different-question writes may converge independently;
- same-question stale conflicting writes must not silently overwrite a newer authoritative value;
- browser/local state is not authority;
- no exclusive device lock is required merely to obtain correctness;
- a stale UI must not final-submit a materially unseen authoritative state without server-side validation;
- a same-value retry may be treated as idempotent only when authoritative state already proves the same accepted value.

The exact locking/version/transaction mechanism is JIT/implementation detail and must be proven under concurrency.

## 7. Final submission and canonical result — AUTHORITY-DERIVED / JIT CONTRACT

A submit request is intent, not success.

Authoritative final-submission acceptance requires at minimum:

- the attempt is active and within its authoritative deadline;
- the exact server-side canonical attempt context is valid;
- all governed scored requirements are complete;
- any methodology-required ambiguity/tie inputs are complete or explicitly permitted unresolved;
- the exact final answer snapshot is durably accepted.

Rejected submission does not freeze the attempt.

Accepted final submission:

- freezes one exact answer snapshot;
- ends ordinary participant editing for that attempt;
- must be idempotent under duplicate/retried submits;
- must converge to exactly one canonical deterministic result under the pinned governed execution context;
- cannot be reopened merely because scoring/report generation later fails.

Participant-work completion, result production and report production are distinct lifecycle boundaries.

After final submission is accepted but before the canonical valid result has converged, the submitted attempt remains the participant's outstanding assessment lifecycle. A second ordinary assessment/reassessment must not start merely because backend result generation is delayed or retrying; recovery completes the same frozen submission/result path unless a separately governed remediation rule applies.

For any later Product timing rule that depends on a **qualifying completed assessment**, a frozen accepted submission alone is not silently treated as the qualifying valid result; apply the then-governed Product definition and `AT-UPD-007` adjudication.

## 8. Governed execution provenance and methodology

### 8.1 Execution provenance — AUTHORITY-DERIVED / JIT CONTRACT

The first accepted scored answer must pin sufficient governed context to reproduce the participant-facing assessment/result later without dereferencing mutable “current” configuration.

The pinned semantic bundle must cover every enabled methodology-sensitive input required for deterministic replay, including as applicable:

- methodology/instrument version;
- stable question and option identities;
- scored/required/conditional semantics;
- scoring mappings/weights/calculation/normalisation;
- score representation/classification/ranking;
- tie/near-tie/tie-break/unresolved ambiguity rules;
- mask behaviour where enabled;
- exact governed language variant used for each answered item.

A later successor methodology never silently mutates an already-started attempt.

Language switching during an attempt is permitted only where an approved counterpart belongs to the same governed methodological context and the answer trace preserves the exact variant presented.

### 8.2 Methodology Authority Input Contract — AUTHORITY-DERIVED GATE

Production-intended Four-Colour methodology behaviour may be encoded only from an identifiable, rights-backed, versioned methodology package approved by the authority established by the governing IP agreement/delegation.

Administrative capability, Super Admin status, Content role, clinical role, support role or developer access does not itself confer methodology authority.

The package must be complete enough for deterministic behaviour of every enabled methodology-sensitive capability. Missing, ambiguous or contradictory proprietary inputs fail closed; engineers/Product/Content/admin staff may not infer plausible scoring, tie, mask or interpretation rules to obtain implementation completeness.

Methodology approval, commercial/digital rights, operator publication, Product application and Health/Clinical safety authority remain distinct.

Additional fail-closed constraints preserved from discovery:

- a participant-facing scored English/Afrikaans counterpart requires the applicable translation/use rights, language governance and methodology-meaning compatibility; linguistic fluency alone cannot approve methodology-sensitive wording;
- the book/EPUB or an interesting rule found in source material is not an executable digital methodology specification and may not be mined to fill gaps absent the rights-backed approved digital methodology package;
- the methodology-sensitive interpretation basis for reports is narrower than the full book; Content may express approved methodology but may not invent it;
- publication is semantically atomic for the **enabled** methodology behaviour: required questions, scoring, tie/conditional behaviour, language counterparts and other enabled dependencies must be complete and mutually consistent before that methodology version is startable, while genuinely optional disabled capabilities need not block core publication;
- a published methodology version must retain auditable provenance sufficient to establish the exact governed input/version set, rights basis, approving authority/delegation scope, approval evidence/time, enabled optional capabilities and compatible governed language/content variants.

The optional score-distance/dominance labels remain independently gated where applicable. Mask capability remains disabled until its governed definition/process is complete.

## 9. Result immutability, interpretation and defects

### 9.1 Historical immutability — AUTHORITY-DERIVED

Submitted answers, original calculated result/scores and producing assessment/methodology version remain immutable historical evidence while retained.

Interpretation-only changes use the existing separate audited Reviewed Interpretation path; they do not overwrite raw answers/scores.

### 9.2 Corrective result / invalidation consequences — CANDIDATE PRODUCT RESOLUTION / OPEN GAP

Current Product Law does not fully govern:

- corrective-result creation for a proven platform computation defect;
- methodology invalidation/remediation;
- superseded-for-active-use versus historical state;
- current-profile consequences;
- report succession;
- participant notification/remediation.

`AT-WD-012` is the working candidate model: preserve original immutable evidence, append explicit correction/invalidation/supersession relationships, never treat participant regret as correction, and never silently run historical answers through a later materially different methodology unless authority explicitly permits a backwards-compatible correction.

JIT may not assume those consequential Product rules until `AT-UPD-004` is governed.

## 10. Report lifecycle

The paid digital report is a participant-facing snapshot derived from one canonical result plus the exact approved interpretation/content version and locale used for that snapshot.

Stable boundaries:

- report generation failure after result creation never reopens the attempt or triggers rescoring;
- retry must converge on the same result/provenance basis;
- original and later approved interpretation/report snapshots remain distinguishable;
- requested locale must have an approved governed counterpart; missing required locale fails closed rather than inventing translation;
- ordinary subscription termination does not by itself erase earned report history/access, subject always to Privacy/deletion authority;
- report ownership follows the canonical participant, not payer email or payment instrument.

The exact Product meaning of **successful delivery/fulfilment** remains important where a commercial included-credit rule depends on it and must be adjudicated with `AT-UPD-001`. Email sent/open/download is not automatically equivalent to report existence/availability.

## 11. Notifications and expiry warning

Temperament owns the authoritative attempt deadline and whether an unfinished-assessment warning is still applicable. Communications owns scheduled intent, channel execution, retries, quiet-hour handling, deduplication, observability and provider/delivery evidence.

A warning racing final submission must re-check authoritative attempt state and suppress stale communication where no longer applicable.

Reminder success/failure/opening never changes the fixed attempt deadline automatically. Material platform failure may become evidence in a separately governed recovery decision; it is not itself an automatic extension or restored right.

The participant-facing exact deadline and persistent in-product continuation path in §4.2 remain required working/JIT guardrails; the launch reminder cadence and proactive channel explored in discovery remain downstream configuration, not Product Law.

## 12. Identity continuity and reconciliation — JIT / PROOF PRIMARY

Assessment truth attaches to the canonical participant identity, not an email string, browser session or purchaser.

Ordinary identifier changes must not create a new assessment history.

Where Identity & Access authoritatively reconciles duplicate accounts:

- Temperament consumes that outcome rather than performing identity matching itself;
- retained completed assessment histories remain distinct historical results with original producing-account provenance;
- answers from two active attempts are never merged;
- if reconciliation leaves competing active attempts, ordinary progress must fail closed until an owner-mediated Temperament disposition leaves at most one active attempt;
- conflicting current-profile selections must not silently choose a winner;
- Entitlements separately reconciles underlying right identities/provenance rather than blindly summing balances;
- purchaser identity never gains recipient-private assessment access merely because of payment provenance;
- Privacy determines deletion/retention consequences and reconciliation may not resurrect deleted data;
- replay/retry of reconciliation consequences must converge idempotently;
- enough origin/reconciliation evidence must remain for governed repair if the Identity decision is later corrected, subject to deletion law.

The normal case belongs to FP-003 / Identity / Entitlements JIT and Phase-8 proof. Escalate to Product only if JIT exposes a participant-facing policy choice current law genuinely cannot answer.

## 13. Privacy lifecycle — AUTHORITY-DERIVED

Immutable while retained does not mean perpetual retention.

Account closure, full deletion, retention, anonymisation/pseudonymisation and legal hold remain governed by Privacy authority.

Key constraints:

- full deletion can end ordinary purchased report/assessment access;
- eligible answers/scores/reports must be removed/anonymised according to governing policy;
- legal hold must be narrow, justified and minimised;
- pseudonymised data is not automatically anonymous;
- stale jobs/writes/recovery may not resurrect data after irreversible deletion;
- technical recovery never overrides completed deletion;
- an invalid/deleted current profile source does not trigger silent fallback selection;
- only truly irreversible anonymous aggregates may survive where governing Privacy rules permit.

Exact retention durations remain separately gated and are not invented here.

## 14. Research / Feedback / Interactive Tool isolation — AUTHORITY-DERIVED / DOMAIN CONTRACT

Research/Feedback responses, optional non-scoring assessment feedback and Interactive Tool outputs do not directly create or mutate authoritative digital assessment truth.

In particular:

- a Research response is not an Assessment Answer even if wording overlaps;
- optional assessment feedback does not affect score/completeness/result;
- quiz/calculator/visual outputs are non-authoritative by default;
- anonymous tool output cannot later be retro-attached as digital assessment evidence;
- an explicit Temperament-owned declaration action may use tool context, but the resulting source remains **declared**, never digitally assessed merely because a tool suggested it;
- staff/research interpretation cannot promote tool/research output into assessment truth.

The general owner boundary is **response does not equal command**: a Research/Feedback response does not silently become a Communications preference, Temperament declaration, entitlement change or other Domain command. Any permitted follow-on durable change uses an explicit action owned by that Domain.

Where a governed Research incentive grants assessment-related access, Research may establish only the authorised grant/access intent; Entitlements owns creation/reconciliation of the actual commercial right, and no Assessment Attempt starts until the governed Temperament start boundary is crossed.

## 15. Reassessment and Premium — PRODUCT TIMING GAP

Current authority establishes that valid entitlement and annual reassessment limits are distinct concerns, and Premium annual entitlement is a separate commercial right.

The exact authoritative meaning of `one retake per year` remains unresolved Product policy.

`AT-WD-020` is the working candidate dual-clock model because it closes the repeated-abandoned-retake loophole, but it is not current Product Law. FP-003 JIT must wait for `AT-UPD-007` adjudication rather than implementing the candidate automatically.

Stable surrounding constraints:

- an applicable valid right is independently required;
- Premium entitlement availability does not by itself erase the ordinary timing restriction Product ultimately selects;
- same-assessment interpretation/corrective processing must not be silently treated as a participant-requested ordinary retake;
- technical/methodology remediation remains conceptually distinct from an ordinary reassessment and requires its own governed authority.

## 16. Subscription-included completed assessment — FUTURE-ONLY

Current authority does not guarantee one successfully completed initial digital assessment as a membership/subscription promise.

The discovery model for replacement after incomplete expiry remains useful only if Product later creates that promise. FP-003 and Entitlements must not invent it.

## 17. Phase-7 / proof defer boundary

This compact Pre-JIT contract does not select:

- exact Ash Resources/actions;
- schemas/tables/indexes/constraints;
- locking/transaction/idempotency-key mechanism;
- worker/queue topology;
- cache/PubSub/GenServer infrastructure;
- renderer/storage mechanism;
- UI route/component design;
- provider/package choices.

Before implementation, the normal governed sequence still applies: upstream adjudication where required → FP-003 Phase 7A → required/conditional JIT dossiers → gate resolution → Phase 7C Final Feature Pack Contract → explicit proof classification → Development Entry Hard Stop.

Executable proof should cover at least concurrent first-answer/start convergence, stale answer writes, duplicate/two-device final submit, scoring crash windows, result/report crash boundaries, entitlement-transition retry once Product defines it, version retirement mid-attempt, deletion races, identity reconciliation conflicts and privacy-safe fail-closed recovery.

## 18. Freeze rule

Broad documentary discovery is frozen.

Reopen only for changed governing authority/evidence, a materially different upstream adjudication, a genuine JIT semantic contradiction, methodology/IP evidence that changes the model, or executable proof that falsifies an invariant.

Do not create another generic Assessment research round merely because implementation representation remains undecided.
