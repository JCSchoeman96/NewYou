# NewYou Audit & Evidence Grill — Working v0.1.3

```text
WORKING / NON-AUTHORITATIVE
FULL RE-REVIEW + PRESSURE-TEST / COMPRESSION AUDIT
SUPERSEDES COMPACT v0.1.2
```

- **Re-reviewed:** 2026-10-08
- **Live baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Discovery ledger:** `NEWYOU_AUDIT_EVIDENCE_PREJIT_DISCOVERY_WORKING_v0.6.2.md`

## 1. Review correction

The earlier compact v0.1.0 compression verdict was too strong.

Full re-review found:
- several accepted semantics were omitted or weakened in the compact contract;
- the Evidence Index had an incorrect Engineering Standards path;
- historical Pass 7 routing displayed multiple “primary” buckets;
- the discovery ledger needed an explicit current-status pointer for the earlier provisional FP-001 adjudication;
- `AE-WD-006` overstated the source of the exact fail-closed outage-timing rule.

These are compression/provenance/routing defects, not failures of the accepted Audit doctrine.

**v0.1.0 compact-pack review outcome: `CHANGES REQUIRED`.**

The corrected v0.1.2 pack restores the accepted meaning.

## 2. Authority recheck

Live repository head remained:

`a9c9a8d176e8d62044ca069efeefa60b8f666c8d`

Current manifest/README routing remained:
- North Star v1.3.0
- Platform v1.6.0
- Decisions v1.6.0
- Open Work v1.2.59
- Architecture v1.1.1
- Domain Map v1.2.0
- Roadmap v1.2.0
- Operating Model v1.0.1
- Frontend Experience System v1.0.1
- Architecture Requirements v1.1.0
- Architecture Law v0.36.0
- Reference Flows v0.3.0
- Engineering Standards v1.0.1 under `reference/`

No live authority drift invalidated the discovery.

## 2A. Programme-status precedence check

At live baseline `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`:

- **Pre-JIT working adjudication:** `FP-001 Audit & Evidence JIT Domain Dossier = REQUIRED`.
- **Governed programme state:** `AUDIT & EVIDENCE DOSSIER: CONDITIONAL / PENDING EXPLICIT ADJUDICATION`.
- **Phase 7C:** `BLOCKED / NOT_STARTED`.

Result: **PASS after v0.1.2 routing patch**. The compact pack no longer permits a reasonable small-context reading that working doctrine has already promoted governed programme state.

## 2B. Upstream-scope check

Effective conclusion:

> **No unresolved Audit-specific Product or Architecture amendment prerequisite has been identified.**

Separately owned upstream gaps in participating Domains remain binding and are outside this pack's authority.

Result: **PASS after v0.1.2 routing patch**.

## 3. Required pressure categories

| Category | Result |
|---|---|
| Business truth vs evidence truth | PASS |
| Exactly-once illusion | PASS |
| Failed attempts | PASS |
| Correction/supersession | PASS |
| Minimisation | PASS |
| Access/operator | PASS |
| Retention | PASS |
| Cross-domain | PASS |
| Security/abuse | PASS |
| Disaster recovery | PASS |

## 4. Mandatory high-risk scenarios

| Scenario | Result |
|---|---|
| Account verification evidence failure | PASS — Identity truth remains source-owned; selected central evidence is E2 |
| Payment authoritative but Audit delayed | PASS — Commerce remains source authority |
| Dangerous health eligibility evidence failure | PASS — Health/Safety remain source authority; central evidence selection is separate |
| Privileged op with incomplete actor/evidence | PASS — E1 fails closed before protected effect |
| Source truth correction | PASS — source owner corrects truth; Audit appends evidence correction only |
| Retries/concurrency | PASS — business effect, material attempt and evidence assertion identities stay separate |
| Provider contradiction | PASS — provider evidence informs owner reconciliation only |
| Lawful expiry | PASS — append-only is not immortal |
| Deletion/anonymisation | PASS — any retained evidence linkage is independently authorised/minimised/non-reconstructive |
| Sensitive security evidence | PASS — access is governed and structured categories may themselves be sensitive |

## 5. FLOW-01 attack

Registration → Account/PMR → verification delivery → proof consumption → login/session → recovery → controlled support survived:
- source commit with delayed Audit only via a lossless E2 obligation;
- duplicate requests without duplicate business effect;
- evidence replay safety;
- proof replay without second verification effect;
- concurrent recovery/security changes resolved by Identity;
- security revocation during Audit materialisation outage;
- E1 privilege activation failing closed when required evidence cannot be established;
- E1 admission surviving later source failure;
- Audit-behind/ahead restore divergence without promotion of Audit to source authority.

Result: **PASS**.

## 6. Cross-domain generalisation

Commerce/provider disorder and Health/Safety correction did not break the model.

Two durable refinements were confirmed:
1. central evidence selection happens before E1/E2 classification;
2. later compensating business events are not automatically evidence corrections.

Result: **PASS**.

## 7. Retention/integrity attack

Confirmed:
- immutability ≠ immortality;
- semantic immutability ≠ byte immobility;
- correction lineage ≠ retention state;
- legal hold ≠ permanent retention;
- lawful disposition must be distinguishable from tampering;
- correction itself is a privileged E1 action;
- key/protection compromise changes assurance, not past semantic meaning;
- direct DBA/infrastructure paths belong in tamper-resistance proof.

Result: **PASS**.

## 8. 74-decision compression coverage

Corrected contract v0.1.2 contains all 74 accepted decision IDs and explicit current meaning.

| Decision range | Covered in contract |
|---|---|
| `001..006` | YES |
| `007..012` | YES |
| `013..020` | YES |
| `021..028` | YES |
| `029..037` | YES |
| `038..050` | YES |
| `051..059` | YES |
| `060..065` | YES |
| `066..069` | YES |
| `070..074` | YES |

Also retained:
- `AE-MECH-001`
- `AE-MECH-002`
- `AE-WH-001` only as historical/superseded provenance

## 9. FP-001 adjudication

The exact conditional test remains:

> Can Phase 7C state the complete implementation-grade FP-001 Audit/Evidence contract without inventing new Audit-owned Domain semantics?

Answer after the full review: **NO**.

Current **Pre-JIT working adjudication**:

> **FP-001 Audit & Evidence JIT Domain Dossier = REQUIRED**

Current **governed programme status** remains `CONDITIONAL / PENDING EXPLICIT ADJUDICATION`; Phase 7C remains `BLOCKED / NOT_STARTED` until explicit authorised adjudication/promotion.

The full review did not uncover an **Audit-specific** Product/Architecture amendment prerequisite. Separately governed upstream gaps in participating Domains remain binding.

## 10. Corrected compression verdict

`PASS — v0.1.2 COMPACT PACK PRESERVES CURRENT ACCEPTED PRE-JIT MEANING AND PROGRAMME-STATUS PRECEDENCE`

The park verdict applies only to discovery v0.6.2 + compact v0.1.3, not to the superseded compact v0.1.0.
