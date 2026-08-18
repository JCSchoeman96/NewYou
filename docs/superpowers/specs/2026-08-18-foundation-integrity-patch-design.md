# Foundation Integrity Patch v1.0.0 Design

## Goal

Repair the known planning-foundation integrity defects, make the audit reproducible, reduce routine context load, and hand the repository cleanly to Phase 7 / FP-001 preparation without changing Product Law, Architecture Law, Domain Law, or Roadmap meaning.

## Scope

The patch has six bounded outcomes:

1. Add the already-consumed `OQ-040` definition to the authoritative Decision Register, tied to `DEC-293` and the first-party experimentation proof. Existing `DEC-*` and `OQ-001...OQ-039` identifiers remain unchanged.
2. Repair active document-graph references so canonical current, `reference/`, and `archive/` paths are explicit. Historical archive prose remains historical evidence and is not rewritten merely to modernise its contemporaneous filenames.
3. Add `docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` containing document ID, canonical filename, SemVer, repository path, authority class, SHA-256, and superseded version metadata for the seven current authority documents and the four current deep-reference evidence documents.
4. Add a dependency-free deterministic audit runner and tests. It will check file existence, manifest/hash parity, current versions and authority paths, duplicate definitions, identifier resolution for `DEC`, `OQ`, `ARC`, `ARQ`, `FLOW`, and `FP`, Roadmap OQ gate coverage, and unique ownership of the approved domain matrix.
5. Replace ambiguous readiness wording with `PLANNING FOUNDATION: READY`, `NEXT: PHASE 7 / FP-001 PREPARATION`, and `EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS`.
6. Move the accumulated historical `02_OPEN_WORK` changelog into a clearly marked archive artifact, leaving the current tracker body focused on current status, gates, sequence, and stop conditions.

The patch explicitly excludes architecture reopening, domain redesign, schema-per-tenant work, Redis/GenServer mandates, untouched-domain cache design, FP-015, experimentation implementation, clinical gate resolution, the full operating model, the Pilot Decision Contract, product-market-fit work, and all executable development.

## Approaches considered

### Manual manifest and shell checks

This would minimize code but make identifier parsing, duplicate detection, ownership checks, and structured failure reporting fragile and hard to test. It is rejected.

### Python standard-library audit runner — selected

`tools/foundation_integrity_audit.py` will read the checked-in manifest and Markdown files using only the Python standard library. It will expose a callable `run_audit(root, manifest_path)` function for tests and a CLI for repeatable repository checks. The CLI will print a concise human summary and can emit deterministic JSON for machine consumers. No package installation or application scaffolding is required.

### General Markdown parser dependency

A parser package could provide richer syntax handling, but the audit only needs bounded headings, tables, metadata, and identifier references. Adding a dependency would increase setup and execution friction without improving the governance checks enough to justify it. It is rejected.

## Design

### Authority manifest

The manifest is an explicit, reviewable inventory. `governing_documents` contains the seven files listed by the platform README as current authority. `reference_documents` contains the four current deep evidence files. Each entry has this shape:

```json
{
  "document_id": "DECISION_REGISTER",
  "canonical_filename": "01_DECISIONS_v1.2.1.md",
  "semver": "1.2.1",
  "repository_path": "docs/00_platform/01_DECISIONS_v1.2.1.md",
  "authority_class": "DECISION_REGISTER",
  "sha256": "<64 lowercase hexadecimal characters>",
  "superseded_version": null
}
```

The manifest contains no timestamps or generated-at fields, so identical repository content produces identical manifest content. The manifest itself is not included as a document entry and therefore does not create a self-hash cycle.

### Audit runner

The runner will use focused checks with explicit names and structured findings:

- manifest schema, duplicate document IDs, canonical filename/path agreement, path existence, and archive/reference authority placement;
- SHA-256 parity between manifest entries and repository files;
- SemVer parity between manifest entries, versioned filenames, and available document metadata;
- duplicate definitions and unresolved references for `DEC-*`, `OQ-*`, `ARC-*`, `ARQ-<family>-*`, `FLOW-*`, and `FP-*`;
- contiguous current Decision Register coverage through `DEC-293` and `OQ-040`, Architecture Law coverage through `ARC-327`, twelve Reference Flows, seventeen Feature Packs, and the frozen ARQ definition count;
- Roadmap gate-table coverage for every current `OQ-*` definition;
- the approved 18-domain set and 48 durable-truth rows, requiring exactly one valid bold owner per row;
- active authority graph references, including the canonical current Open Work path and explicit `reference/` or `archive/` prefixes where those files were moved.

The runner exits non-zero on any finding and emits a stable JSON object when requested. Historical archive files are excluded from active-graph path checks but remain filesystem-visible and preserved.

### Human-readable evidence

`FOUNDATION_READINESS_AUDIT_v1.0.0.md` will be updated as the human-readable result for this patch. It will record the audit command, current authority baseline, machine-derived counts, individual check results, the corrected readiness language, and the explicit closure statement:

> FOUNDATION INTEGRITY PATCH COMPLETE. NO FURTHER FOUNDATION EXPANSION WITHOUT AN UPSTREAM CONTRADICTION.

The report will not become a new authority layer. The manifest and runner provide machine evidence; the Markdown report explains the result for human readers.

### Context hygiene

`archive/02_OPEN_WORK_CHANGELOG_v1.0.0.md` will preserve the removed historical changelog verbatim with an archival status header. `02_OPEN_WORK_v1.2.27.md` will retain a short pointer to that artifact and its current tracker sections will carry only current planning state and the new readiness wording.

### Error handling

The runner will report every failed check in one invocation rather than stopping at the first error. Each finding will include a check name, repository-relative path where applicable, identifier or row context where applicable, and a concise expected/actual value. A clean run returns exit code `0`; any finding returns exit code `1`; malformed CLI input returns the standard argument-parser error code.

### Testing

Tests will use `unittest` and temporary directories. They will cover a passing repository-shaped fixture and isolated failures for missing manifest files, hash mismatch, duplicate definitions, unresolved references, incomplete Roadmap gate coverage, and multiple domain owners. The real repository audit will then run as an integration check after the document corrections and manifest hashes are finalized.

## Handoff boundary

When the audit is green, this patch closes foundation work. The next permitted planning action is Phase 7 / FP-001 preparation in the legislated order: FP-001 Skeleton, Preliminary Gate Manifest, affected JIT dossiers, blocking-gate resolution, Final FP-001 Contract, Architectural Proof decision, then Phase 8. No FP-001 implementation is included in this patch.
