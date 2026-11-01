# Privacy / Consent Upstream Delta Register — Working Consolidation v0.1.3

- **Status:** WORKING / NON-AUTHORITATIVE
- **v0.1.3 hygiene patch:** Standardises governed terminology to `Phase 7C Final Feature Pack Contract` and preserves exact namespaced identifiers throughout the register. No accepted doctrine, delta classification or resolution layer is changed.
- **Source:** `PRIV-UPD-001...004` from `PRIVACY_CONSENT_PREJIT_DISCOVERY_WORKING_v0.12.1.md`
- **Live authority baseline:** `5bd3e840d92cab8a0c159ef7156b6187e4a1e0b2`
- **Date:** 2026-09-09
- **Implementation:** NOT AUTHORISED.
- **Interpretation rule:** the `PRIV-UPD` prefix preserves discovery provenance; it does not mean every item requires Product Law.

## Classification summary

### Genuine upstream Product/policy work

- `PRIV-UPD-001` — pending export versus subsequent Full Deletion.
- `PRIV-UPD-002` — Full Deletion versus active recurring membership commercial contract.
- `PRIV-UPD-004` — sanction scope across Full Deletion and later Account creation.

### JIT/governance first; Product escalation conditional

- `PRIV-UPD-003` — Full-deletion scope across duplicate-account reconciliation.

Current Domain/Identity authority already supplies governed reconciliation, canonical-survivor semantics and owner-controlled consequences. Resolve the detailed merge/delete interaction at Identity + Privacy JIT/proof first; escalate Product only if the chosen resolution changes participant rights or the Product identity/deletion promise.

## Register

| ID | Issue | Default owner / layer | Classification | Resolution point | Related working doctrine / gates |
|---|---|---|---|---|---|
| `PRIV-UPD-001` | Does an already-valid participant export survive a later Full Deletion Request, and where is the deterministic termination boundary? | Product/Privacy policy + Legal/Privacy validation | **UPSTREAM POLICY** | Before an affected Phase 7C Final Feature Pack Contract freezes export/deletion participant behaviour. | `PRIV-WD-001`; `OQ-032`. |
| `PRIV-UPD-002` | How does effective Full Deletion interact with an active recurring membership during the 14-day cancellation window, including renewal suppression, cancellation restoration and late-charge remedy? | Product + Commerce, coordinated with Entitlements/Privacy and CER | **UPSTREAM COMMERCIAL POLICY** | Before any recurring-membership + Full Deletion contract is frozen or implemented. | `PRIV-WD-002`; `CER-PT-004`; `OQ-004`; `OQ-029`; processor gates where applicable. |
| `PRIV-UPD-003` | How does destructive deletion scope traverse applied duplicate-identity reconciliation lineage, especially when reconciliation is contested/in flight? | Identity + Privacy JIT/governance + owner Domains | **NON-BLOCKING / DEFER TO JIT BY DEFAULT** | Before a JIT/proof freezes merge/delete concurrency and reconciliation consequences. Escalate only if Product rights change. | `PRIV-WD-003`; Identity ReconciliationCase planning evidence; current PMR/canonical identity law. |
| `PRIV-UPD-004` | Are sanctions content-, Account- or human-scoped across deletion/re-registration, and what evidence permits a later current restriction? | Product / Trust & Safety / Community / Privacy plus security/anti-abuse operating responsibility (**not a separate Domain**) | **UPSTREAM POLICY** | Before NewYou carries or reapplies sanctions across a deleted/recreated Account identity. | `PRIV-WD-004`; `OQ-023` for Facebook operating policy; retention/security gates. |

## `PRIV-UPD-001`

### Current gap

Current authority strongly governs export and deletion independently but does not fully specify the lifecycle relationship when a valid export exists first and Full Deletion is requested later.

### Accepted working direction

Use `PRIV-WD-001` as non-authoritative planning input:

- export may continue as a narrowly scoped data-right operation during the deletion cancellation window without restoring normal product access;
- generation/delivery remain subject to current verification, authority and scope;
- once irreversible deletion execution begins, an undelivered export is cancelled and platform-controlled delivery capability/temporary artefacts are removed;
- completed deletion cannot coexist with a live participant export-delivery path.

### Upstream need

Set the participant promise and legal boundary explicitly; leave operational deadlines/retry/pending states to `OQ-032`.

## `PRIV-UPD-002`

### Current gap

Current law does not fully define recurring subscription behaviour after Full Deletion has revoked normal access but before irreversible deletion completes.

### Accepted working direction

Use `PRIV-WD-002`:

- do not intentionally originate a new future-service-period recurring collection after the deletion request is effective;
- already-in-flight money truth reconciles honestly;
- late success cannot restore Entitlement/access;
- completed deletion cannot leave participant-linked recurring provider authority capable of future automatic membership charges;
- deletion cancellation restoration/paid-period semantics remain explicit Product/Commerce policy.

### Upstream need

Product + Commerce must define renewal-suppression timing, deletion-cancellation restoration and late-charge remedy. Provider mechanics remain under `OQ-004`.

## `PRIV-UPD-003`

### Compression classification correction

The original accepted PT-014 classified this as Product/policy. Compression narrows the default escalation layer.

Current authority already establishes:

- governed duplicate-identity reconciliation rather than destructive row collapse;
- one canonical survivor/PMR semantics;
- owner-Domain consequences;
- Privacy-owned deletion orchestration.

Therefore the exact contested merge/delete concurrency contract normally belongs to Identity + Privacy JIT/Architectural Proof.

Escalate Product only if a proposed solution changes:

- whose data a Full Deletion promise covers;
- participant rights in a contested identity case;
- Product identity continuity semantics;
- a durable Product promise rather than implementation/governance mechanics.

The accepted `PRIV-WD-003` invariant remains unchanged.

## `PRIV-UPD-004`

### Current gap

Product law permits restricted moderation/security evidence to survive deletion, but does not fully specify sanction scope across a later genuinely new Account.

### Accepted working direction

Use `PRIV-WD-004`:

- retained evidence remains minimised/restricted/non-reconstructive;
- weak identifier/contact match never automatically resurrects sanction state;
- retained evidence may inform a governed current Community and applicable security/anti-abuse decision using sufficiently reliable identity/risk evidence;
- human-level continuing exclusion must be explicit policy, not inferred from a generic ban field.

### Upstream need

Trust & Safety/Product governance must define sanction scopes, evidence confidence, review/appeal and human-level exclusion semantics. `OQ-023` remains the separate Facebook operating-policy gate.

## Existing gates — do not duplicate

- `OQ-004` payment-provider recurring/refund/chargeback validation
- `OQ-009` Health/professional retention umbrella
- `OQ-018` journal encryption/retention
- `OQ-021` recording/video consent/retention
- `OQ-023` Facebook moderation/privacy operating policy
- `OQ-029` retention schedule matrix
- `OQ-030` external processor deletion/export inventory
- `OQ-031` backup restore/deletion replay
- `OQ-032` export/deletion operations
- `OQ-033` professional record authority
- `OQ-037` RPO/RTO
- `OQ-038` incident ownership
- `OQ-040` experimentation privacy/deletion proof

`HSP-UPD-004` remains the existing HSP category-specific deletion seam and is not duplicated here.

## Anti-drift conclusion

Escalate only genuine Product rights/policy.

Keep:

- retention periods with expert gates;
- provider mechanics with provider validation;
- concurrency/locking/resource representation with JIT/proof;
- owner-Domain record consequences with their owners.

No new authority layer is created.
