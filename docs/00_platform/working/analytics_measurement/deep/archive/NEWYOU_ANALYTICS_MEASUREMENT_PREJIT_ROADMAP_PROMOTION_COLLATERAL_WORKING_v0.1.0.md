# NewYou Analytics & Measurement Pre-JIT — Roadmap v1.3.0 Promotion Collateral Working v0.1.0

```text
WORKING / NON-AUTHORITATIVE
PROMOTION COLLATERAL CONTRACT ONLY
DO NOT TREAT AS CURRENT AUTHORITY ROUTING
IMPLEMENTATION NOT AUTHORISED
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Current live-main baseline during Pass 7:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Exact Roadmap candidate commit:** `25cef5c3eb6462292cb5c34fff2e4c59d3be2078`
- **Exact Roadmap candidate blob:** `ddff1c2fa34b3b9185bef8eb72e49f8513479887`
- **Exact archived predecessor blob:** `5432991071d4d1a7cbd9dc4c8fca48c823129f40`
- **Known predecessor SHA-256:** `601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0`
- **Candidate SHA-256:** `UNRESOLVED — MUST BE COMPUTED FROM EXACT ddff1c2... BYTES BEFORE ROUTING`
- **Source decision:** `ANL-UPD-001`
- **Source pressure tests:** `ANL-PT-013`–`ANL-PT-023`

---

## 1. Purpose

This file records the **exact routing/status collateral contract** that must accompany a later governed promotion of the already-reviewed Roadmap v1.3.0 candidate.

It exists to prevent promotion-time improvisation. It does not itself modify README, the authority manifest, Open Work, Delivery Atlas or `main`.

The promotion may proceed only when all required integrity values are real and independently checkable.

---

## 2. Roadmap authority payload already assembled

### 2.1 Candidate

```text
current candidate path:
  docs/00_platform/05_ROADMAP_v1.3.0.md

git blob:
  ddff1c2fa34b3b9185bef8eb72e49f8513479887

candidate commit:
  25cef5c3eb6462292cb5c34fff2e4c59d3be2078
```

Pass-7 semantic review: **PASS**.

Any byte change to this candidate creates a new candidate and requires a new exact diff review plus a newly computed SHA-256.

### 2.2 Preserved predecessor

```text
archive path:
  docs/00_platform/archive/05_ROADMAP_v1.2.0.md

git blob:
  5432991071d4d1a7cbd9dc4c8fca48c823129f40

known SHA-256:
  601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0
```

The candidate commit preserves this predecessor using the exact current v1.2.0 blob.

---

## 3. README routing candidate

At the governed promotion boundary, and only after the manifest pin is real, README default-authority routing should change:

```text
7. 05_ROADMAP_v1.2.0.md
```

to:

```text
7. 05_ROADMAP_v1.3.0.md
```

If Open Work is promoted at the same boundary, README item 4 must route to the exact Open Work successor created by that promotion package (expected shape: `02_OPEN_WORK_v1.2.60.md`, subject to exact then-current baseline).

No other default-authority route is changed by `ANL-UPD-001`.

README narrative statements must continue to say:

- README + manifest are routing pointers;
- working artifacts remain non-authoritative;
- Delivery Atlas remains derived/non-authoritative;
- current Open Work owns active programme status;
- no Roadmap promotion by itself authorises implementation.

---

## 4. Manifest routing candidate

### 4.1 Current `ROADMAP` record after promotion

The manifest `governing_documents` Roadmap record must become equivalent to:

```json
{
  "document_id": "ROADMAP",
  "canonical_filename": "05_ROADMAP_v1.3.0.md",
  "semver": "1.3.0",
  "repository_path": "docs/00_platform/05_ROADMAP_v1.3.0.md",
  "authority_class": "ROADMAP",
  "sha256": "<EXACT_SHA256_OF_ddff1c2_BYTES>",
  "superseded_version": "1.2.0",
  "lifecycle": "current",
  "graph_policy": "frozen_provenance",
  "provenance_sha256": "<SAME_EXACT_SHA256>"
}
```

The placeholders above are **not acceptable in a promoted manifest**. They are documentation markers only.

### 4.2 Historical v1.2.0 registration

The manifest historical section must register the exact archived predecessor according to the existing Roadmap convention, equivalent to:

```json
{
  "document_id": "ROADMAP_V1_2_0",
  "canonical_filename": "05_ROADMAP_v1.2.0.md",
  "semver": "1.2.0",
  "repository_path": "docs/00_platform/archive/05_ROADMAP_v1.2.0.md",
  "authority_class": "ROADMAP_HISTORICAL",
  "sha256": "601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0",
  "superseded_version": "1.3.0",
  "lifecycle": "historical",
  "graph_policy": "frozen_provenance",
  "provenance_sha256": "601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0"
}
```

Do not alter historical v1.1.x Roadmap entries except where a repository integrity tool mechanically requires ordering/graph metadata that preserves their meaning.

### 4.3 Open Work manifest record

If Open Work v1.2.60 is created in the same promotion package, its exact SHA-256 must also be computed from final bytes before the manifest is frozen. Its current record must set:

```text
canonical_filename: 02_OPEN_WORK_v1.2.60.md
semver: 1.2.60
superseded_version: 1.2.59
lifecycle: current
```

and the exact v1.2.59 bytes must be preserved/registered historically according to repository convention.

No hash may be guessed.

---

## 5. Open Work successor contract

Expected semantic shape if the promotion occurs against current Open Work v1.2.59:

```text
02_OPEN_WORK_v1.2.59.md
→ 02_OPEN_WORK_v1.2.60.md
```

The successor must record only the governance status consequences of Roadmap v1.3.0 promotion.

### 5.1 Required current-state update

Update current authority prose so Roadmap current authority becomes v1.3.0.

Record that the bounded FP-006 Research & Feedback Roadmap sequencing contradiction identified by `ANL-GAP-001` has been resolved **at Roadmap authority level only**.

### 5.2 Required preserved programme status

Unless live evidence changes before promotion, preserve all of the following:

- Product v1.6.0, Decision v1.6.0, Domain v1.2.0 and North Star v1.3.0 remain current;
- Domain count remains 20;
- Feature Pack count remains 17;
- FP-001 PMR reconciliation remains COMPLETE / CERTIFIED;
- Identity dossier v0.1.4 remains CERTIFIED / CURRENT;
- Communications dossier v0.1.0 remains COMPLETE / CERTIFIED / CURRENT;
- Communications finalisation remains BLOCKED / STOP;
- Privacy & Consent, Content & Media and Audit & Evidence remain conditional / pending explicit FP-001 adjudication;
- Analytics remains NOT REQUIRED for the active FP-001 conditional-dossier programme;
- the newly bounded Research & Feedback FP-006 activation does not make Research or Analytics required for current FP-001 work;
- Phase 7C remains BLOCKED / NOT_STARTED;
- proof classification remains NOT FINALISED;
- executable development remains blocked until the existing development-entry conditions pass;
- Store/CER remains outside HARDEN-02 as already governed.

### 5.3 Explicit non-advancement

The Open Work successor must say that this Roadmap promotion does **not**:

- start FP-006;
- start a Research & Feedback JIT dossier;
- decide FP-006 gate-manifest detail;
- resolve participation identity/uniqueness, privacy, retention/deletion, provider, Resource/schema or proof classification;
- advance FP-001 or Phase 7C;
- authorise Phase 8 or implementation.

### 5.4 Archive discipline

Preserve exact current Open Work v1.2.59 bytes at the repository's normal historical path when the successor is frozen. Compute and register its exact hash according to the existing manifest convention.

---

## 6. Delivery Atlas treatment

Delivery Atlas reconciliation is **not part of semantic authority promotion**.

After successful Roadmap/Open Work promotion, the derived Atlas should be reconciled so that:

- its current Roadmap source route points to v1.3.0;
- its current Open Work route points to the promoted successor;
- FP-006 derived Domain participation includes the bounded Research & Feedback mode;
- FP-005 basic progress/usefulness remains HJP;
- broader Research remains future-gated;
- Atlas remains explicitly non-authoritative and creates no new gate, dossier, Feature Pack or law.

A stale Atlas must not override a successfully promoted Roadmap, but prompt reconciliation remains good navigation hygiene.

---

## 7. Foundation Integrity / exact-head gate

Before any PR/merge/current promotion claim, the **complete** candidate head must pass:

1. exact SHA-256 computation for every changed manifest-pinned file;
2. manifest-backed Foundation Integrity on the exact candidate head;
3. archive equality/integrity checks;
4. README/manifest/current-path coherence;
5. exact semantic review of changed authority/status files;
6. confirmation that no unrelated programme state advanced;
7. confirmation that the Roadmap candidate blob is still exactly `ddff1c2fa34b3b9185bef8eb72e49f8513479887` unless a new review explicitly supersedes it.

The repository already has an exact-head `workflow_dispatch` Foundation Integrity route. If used, it must be run on the exact candidate head and its result recorded; a different SHA does not certify the target head.

---

## 8. Current disposition

```text
ROADMAP v1.3.0 SEMANTIC CANDIDATE: PASS
ARCHIVED ROADMAP v1.2.0 BLOB IDENTITY: PASS
README ROUTING: SPECIFIED / NOT APPLIED
MANIFEST ROUTING: SPECIFIED / BLOCKED ON REAL CANDIDATE SHA-256
OPEN WORK SUCCESSOR: SPECIFIED / NOT FROZEN
DELIVERY ATLAS: DERIVED FOLLOW-UP / NOT STARTED
PR: NOT OPENED
MERGE: NOT PERFORMED
IMPLEMENTATION: NOT AUTHORISED
```

**Promotion status:** `BLOCKED / STOP` until exact digest + complete integrity package are proven.