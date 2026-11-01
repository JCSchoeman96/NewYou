# Foundation Integrity merge gate

This is the current operational CI contract. The workflows define executable behaviour; this document explains their lane boundaries.

## Required gate

The repository ruleset requires the **Foundation Integrity** status context. Every pull request and push to `main` runs Foundation Smoke. Application CI runs when the change contains application or engineering paths. Foundation Full is separate, non-blocking evidence and is not part of the required aggregate.

The aggregate requires successful routing and Smoke, plus successful Application CI when selected. It does not wait for Foundation Full.

## Semantic path ownership

The repository path communicates the normal CI route:

| Paths | Route |
| --- | --- |
| `docs/governance/**` | Smoke + Foundation Full |
| `docs/history/**` | Smoke + Foundation Full |
| Foundation Full/provenance machinery | Smoke + Foundation Full |
| `docs/delivery/**` | Smoke + applicable Application CI |
| `docs/development/**` | Smoke + applicable engineering CI |
| application source, migrations and tests | Smoke + Application CI |
| `.agents/**`, `AGENTS.md` and normal engineering files | Smoke + applicable engineering CI |
| unknown or unclassifiable paths | fail closed to Foundation Full |

Classification is explicit. Python files under `tests/` do not select Foundation Full by language or location alone. Foundation Full tests and tooling are named directly in the classifier; ordinary application, routing and Smoke tests stay on the Application CI route.

Delivery state such as Ready, blockers, dependencies, PR review and Done remains in Plane project `WELL`; it is not mirrored into repository documents.

## Foundation Smoke

Smoke validates both current routers:

- `docs/governance/CURRENT_GOVERNANCE_ROUTER.json` routes current durable law and genuine supporting authority only.
- `docs/delivery/CURRENT_DELIVERY_ROUTER.json` routes current Feature, JIT, proof, execution and content-evidence contracts beneath governance.

Smoke runs the path-classification regression tests and checks router identity, route containment, target existence, hashes, required authority inventories, the `docs/README.md` entrypoint, required historical files and merge-gate topology. Governance cannot route into delivery or history; delivery cannot route into governance or history. No current route may resolve into an archive.

## Foundation Full

Full runs for governance and frozen-history changes, Foundation Full/provenance machinery, and unknown paths that cannot safely be classified. It validates the frozen `docs/history/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` and historical certification suite. The frozen `docs/history/02_OPEN_WORK_v1.2.90.md` remains evidence only; it is not live execution authority.

Full is also available for nightly and exact-SHA certification. A Full failure remains evidence and must be investigated when the changed PR affects that lane, even though Full does not block the required aggregate.

## Application CI

Application CI runs the canonical `mix check` gate for routed application and engineering changes. The slower `mix check.deep` Dialyzer lane runs when application source, migrations or the dependency/toolchain definition changes. Documentation-only delivery/development changes, agent guidance and test-only changes skip the deep lane. The classifier never selects Full solely because a change is under `docs/delivery/**`, `docs/development/**`, `.agents/**` or `tests/**`.

The historical pre-migration suite and audit use temporary compatibility views inside Foundation Full. They rebuild pinned baseline files at frozen paths, then overlay `docs/history/` evidence so provenance mutations remain visible. The temporary views do not add a legacy documentation root to the repository or either current router. Foundation Smoke validates current governance and delivery routing directly.

See [Foundation Integrity CI](foundation-integrity-ci.md) for certification history and command details.
