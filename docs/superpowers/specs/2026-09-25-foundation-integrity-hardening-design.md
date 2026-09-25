# Foundation Integrity hardening design

## Goal

Make a passing Foundation Integrity Audit (FIA) prove that current authority routing agrees across README and manifest, active lifecycle routing is coherent, blocked Development Entry has no executable application roots, and registered Phase 7 gates have not been bypassed. Add a separate live GitHub evidence verifier for certification actions.

The work stays within FIA tooling, governance tests, CI, and narrowly scoped routing or lifecycle metadata. It does not start application implementation, advance HARDEN-02, or change Product, Architecture, Domain, or Roadmap meaning.

## Existing project context

`main` and `origin/main` both resolve to `352f304139b9d4f8ee3ba205cde9e34d0ad8437f`, the reviewed baseline. The baseline suite passes 142 tests with `python3 -m unittest discover -s tests -v`. The baseline FIA reports 280 passing checks and no findings.

Open Work v1.2.43 already has a marked JSON state object with current and next stage, conditional dossier dispositions, Phase 7C, proof classification, and `application_implementation`. The current state says application implementation is blocked. The manifest records governing, reference, and historical documents, but the README check searches for filenames across the whole file and does not enforce array, lifecycle, or path agreement. The workflow filters out application source paths. The Atlas currently routes to archived Open Work v1.2.39 in its current-source table and FP-001 anchors.

The approved Architecture direction is one Elixir/Phoenix/Ash application. The repository has no application source roots today. The physical boundary check will use explicit Phoenix project roots and exclude `tools/`, `tests/`, documentation, and CI.

## Approaches considered

1. Extend the existing Open Work JSON record and verify its relationships. This reuses the established lifecycle source and keeps the changes small. This is the selected approach.
2. Add a second governance state file. This would create another active status source and require extra routing rules.
3. Add tests around current prose without changing FIA. This would leave the routine audit unable to enforce the new invariants.

## Design

### Development Entry and CI

Run Foundation Integrity on every pull request and every push to `main`, with no partial path filter. FIA reads `application_implementation` from the marked canonical Open Work JSON. If the state is `BLOCKED`, the audit fails if any of these repository roots exist: `mix.exs`, `lib/`, `config/`, `priv/`, or `assets/`. The state `AUTHORISED` permits them. Unknown or missing state fails closed. Tests use temporary repositories.

### Authority routing

Add a machine-readable routing table inside README's designated Current Authority section. Each row identifies the document ID, authority class, current context mode, canonical filename, repository path, and SemVer. The verifier parses only this marked section and compares its current governing entries with `governing_documents` in the manifest.

Manifest entries must carry a valid `lifecycle`. Governing, reference, and historical array placement must agree with lifecycle and normalized path class. Resolved paths must remain inside the repository. Current singular authority classes must have exactly one current artifact. Where a current artifact declares a predecessor, the predecessor must be represented as historical and must not also be current.

### Active lifecycle and Phase 7

The Open Work JSON remains the canonical active state. README gets a reserved, machine-readable mirror for current stage, next stage, Phase 7C, proof classification, and application implementation. FIA compares the mirror with Open Work and rejects duplicate or conflicting declarations inside that reserved block. Historical statements explicitly marked `source-at-freeze` remain outside the active mirror.

Add a small formal-artifact registry to the existing active state object. It records artifact identity, formal type, and path for lifecycle artifacts. Gate checks use this registry rather than scanning `working/`. Required implications include:

- required Communications work must be complete before Phase 7C becomes ready, starts, or completes;
- every conditional dossier must be explicitly adjudicated, and any adjudicated-required dossier must be complete before Phase 7C;
- proof classification cannot become final before an approved Final Feature Pack Contract is registered;
- a Pre-JIT artifact cannot satisfy a formal JIT dossier requirement by title or status alone;
- application implementation stays blocked until the required formal Phase 7 and Phase 8 entry state is present.

The current state remains blocked. The patch adds test fixtures for future states without changing current HARDEN-02 or Phase 7 status.

### Delivery Atlas

Create a versioned Atlas successor for the routing correction and preserve v0.2.0 as historical evidence. Replace current Open Work references with the current route from the manifest. Mark any retained old route as `source-at-freeze`. Atlas tests resolve expected Open Work from the manifest and parse rows designated as current sources.

### Live certification verifier

Add a separate command and module that verifies GitHub PR metadata, review or attestation records, Actions runs, merge SHA relationships, and post-merge evidence. The verifier uses a read-only GitHub API client that can be replaced by fixtures in tests. It emits JSON and exits nonzero if evidence is missing, stale, contradictory, or unavailable. Routine FIA and existing contract unit tests remain offline. The verifier reports evidence only and never edits Open Work or advances HARDEN-02.

The verifier checks repository-visible identities and commit relationships. Human reviewers remain responsible for the substance of a review and for decisions that GitHub cannot prove.

### Preservation and reporting

Versioned governance documents get successors where repository conventions require them. Predecessors remain byte-identical in the archive. Roadmap handoff and dossier state are labelled with their applicable freeze or handoff time. Historical-stage tests stop pinning unrelated present-day Open Work routes; current routing checks live in FIA.

The implementation report will record the baseline SHA, branch, changed paths, artifact transitions, new invariants, mutation outcomes, full test results, FIA status, remaining semantic-review boundaries, and deferred work.

## Validation

Every new invariant gets a negative mutation test that fails for the targeted invalid state. The final checks are the full unittest suite, the manifest-backed FIA command, static workflow trigger inspection, certification verifier fixtures, and a check that no application implementation roots were added.

## Stop boundaries

Do not change approved business or architecture meaning to make a check pass. Do not transition the current HARDEN-02 lifecycle. If live evidence requirements cannot be verified from the existing v0.4.0 contract without adding new certification rules, keep that ambiguity explicit and stop that portion of the patch.
