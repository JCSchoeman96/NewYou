# NewYou Analytics & Measurement — Source ↔ Compact Verification Working v0.1.1

```text
FINAL COMPACT WORKING PACK / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
AUTHORITY: NONE
MECHANICAL CONSISTENCY CHECK
```

## 1. Metric cardinality and exact sets

Expected and verified:

```text
6 total named core metrics
4 Product gate metrics
2 operational targets

Product:
001, 002, 003, 004

Operational:
005, 006
```

Expected target/aim sequence:

```text
001 ≥80%
002 ≥80%
003 ≥70%
004 ≥60%
005 ≥95% operational aim
006 ≥95% operational aim
```

The compact contract must not call 005/006 Product paid-entry gate metrics.

## 2. Exact gap states

```text
ANL-GAP-001
UPSTREAM_ACTION_REQUIRED

ANL-GAP-002
SUPERSEDED / RECLASSIFIED

ANL-GAP-003
OPEN / FP-006 JIT REQUIRED
```

No `ANL-GAP-004` is created.

## 3. Research state

Compact documents must preserve:

```text
CURRENT ROADMAP RESEARCH ACTIVATION
= NOT CURRENT

Research & Feedback
= FUTURE-GATED / FEATURE-PACK-UNASSIGNED
  under current Roadmap v1.2.0
```

The historical v1.3.0 candidate remains non-current evidence.

## 4. Phase 7 ordering

Compact documents must preserve:

```text
7A
→ 7B where required
→ ordinary reconciliation
→ 7C
→ proof execution
→ implementation/hardening
→ release readiness
```

And:

```text
7C owns final REUSE_EXISTING_PROOF / NEW_TRACER_BULLET classification.
```

There is no fourth pre-7C stage.

The Pre-JIT pack does not select proof classification.

A conditional dossier that could materially change the final 7C decision must be explicitly adjudicated before 7C approval.

Post-7C proof must retain, where material:

- authoritative correlation and failure behaviour;
- proof that Analytics does not become shadow business authority;
- concurrency/retry/idempotency boundaries;
- metric-definition, cohort and source-version provenance;
- required fail-closed behaviour;
- upstream stop if proof exposes a higher-authority contradiction.

## 5. Authority

The compact contract must preserve:

- source Domains own durable business truth;
- Analytics owns derived/rebuildable analytical representation only;
- provider/UI/cache/PubSub/dashboard/analytical-arrival state cannot replace authoritative source truth;
- cross-domain metric composition does not create shared-write ownership;
- source correction remains source-owned;
- Plans & Nutrition retains immutable delivered plan snapshot ownership;
- HJP retains habit definition/schedule/occurrence and behavioural/progress/adherence entry ownership;
- Entitlements retains source provenance and expiry within its entitlement lifecycle truth.

## 6. Research/value-evidence precision

Verify the compact contract retains:

- ≥70% positive value/relevance among respondents;
- ≥70% controlled-pilot survey response;
- visible non-response and count + percentage reporting;
- the separate price-value question: “Considering what you paid, did the product provide good value?”;
- discounted purchase intent remains weaker evidence than actual purchase.

## 7. Shared metric invariants

Verify compact pack retains:

- prospective definition/version;
- no retroactive rewrite to make an observed cohort pass;
- count + percentage for small cohorts;
- no denominator shopping;
- missing data does not automatically imply success/failure/removal;
- authoritative business occurrence ≠ analytical arrival ≠ source correction;
- source correction may restate derived output only under governed policy;
- lifecycle machinery applies where materially relevant.

## 8. Implementation, hardening and stop state

Root semantic/routing artifacts preserve `IMPLEMENTATION NOT AUTHORISED`. Hardening may strengthen recovery, reconciliation, observability, resilience and performance only where business meaning remains unchanged.

Expected closure:

```text
HANDOFF-READY / STOP AT JIT BOUNDARY
NO DEFAULT PASS 15
```

The pack does not claim paid-pilot, Phase 7, proof, implementation or release readiness.

## 9. Historical byte preservation

There are 29 historical Analytics working sources before deep v0.1.2: the original 28 plus deep v0.1.1, which becomes a byte-preserved predecessor.

Relocation rule:

```text
old root path blob SHA
==
deep/archive path blob SHA
```

and byte count is unchanged.

Because the final Git tree references the exact existing blob object for each relocated historical file, archive relocation is byte-identical by construction. SHA-256 values independently materialised during packaging are recorded in the Evidence Index/manifest; all other archive identities are deterministically pinned by Git blob SHA + byte count, which also proves unchanged bytes.

## 10. Routing checks

Final expected root:

```text
README.md
NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_CONTRACT_WORKING_v0.1.1.md
NEWYOU_ANALYTICS_MEASUREMENT_UPSTREAM_DELTA_REGISTER_WORKING_v0.1.1.md
NEWYOU_ANALYTICS_MEASUREMENT_EVIDENCE_INDEX_WORKING_v0.1.1.md
NEWYOU_ANALYTICS_MEASUREMENT_COMPRESSION_AUDIT_WORKING_v0.1.1.md
NEWYOU_ANALYTICS_MEASUREMENT_SOURCE_COMPACT_VERIFICATION_WORKING_v0.1.1.md
PACK_MANIFEST_v0.1.1.json
deep/
```

Expected deep source:

`deep/NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_UNIFIED_HANDOFF_WORKING_v0.1.2.md`

Expected archive count: 29.

README, Evidence Index and manifest paths must resolve after commit.

## 11. Authority-contamination check

Final branch diff against main must not modify any current governed authority file:

- Product/North Star;
- Platform;
- Decisions;
- Open Work;
- Architecture;
- Domain Map;
- Roadmap;
- Operating Model;
- FES;
- current authority manifest.

All final packaging changes must be confined to:

`docs/00_platform/working/analytics_measurement/**`

The old Roadmap v1.3.0 candidate must not be installed at the canonical current Roadmap location.

## 12. Verification disposition

This document records the required mechanical assertions. A v0.1.1 compression-preservation PASS requires every semantic assertion above to be present in the compact artifacts plus the final committed tree, paths, blobs, JSON and branch diff to be checked against these expectations.
