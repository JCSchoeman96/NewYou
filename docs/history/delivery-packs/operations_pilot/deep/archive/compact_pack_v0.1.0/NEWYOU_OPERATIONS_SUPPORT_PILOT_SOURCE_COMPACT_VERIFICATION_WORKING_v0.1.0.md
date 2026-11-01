# NewYou Operations, Support & Paid Pilot Source ↔ Compact Verification — Working v0.1.0

> **AUTHORITY:** NONE
> **IMPLEMENTATION:** NOT AUTHORISED
> **SCOPE:** normal-context compact root plus canonical deep-source identity; historical archive may contain superseded wording.

## 1. Identifier cardinality

Required mechanical assertions:

```text
OPS-UPD count = 7
IDs = OPS-UPD-001...007
OPS-UPD-008 absent

OPS-GAP count = 25
IDs = OPS-GAP-001...025
all accounted

OPS-PT evidence coverage = OPS-PT-001...470
no missing range
no OPS-PT-471
```

## 2. Positive semantic assertions required in root pack

- Operations/Support is not a business Domain.
- work = attention/responsibility, not authority.
- provider/UI/Analytics/Audit/support queue state is not business authority.
- support projection owns no business truth.
- minimum-necessary support/private-data boundary exists.
- pilot exposure is distinct from paid-demand evidence.
- current first-pilot numeric ceiling is monotonic non-decreasing.
- rollback closes admission gate rather than lowering the ceiling.
- duplicate genuine collection remediation / payer make-whole exists.
- purchaser/payer/recipient/participant are split.
- first Assessment answer holds/claims credit and does not consume it.
- complete paid Assessment delivery is the consumption boundary.
- Plan generation and first fulfilment are separate.
- failed-fulfilment working remedy exists and requires formal Product/Decision promotion.
- General Wellness is not paid Plan fulfilment and does not consume the Plan.
- current General Wellness timer = none.
- future conditional bounded-election clock invariant is retained.
- R249/R300 is labelled a working allocation pending governed promotion.
- deletion/refund commitment is distinct from provider settlement.
- `OPS-GAP-019`, `022`, `023`, `024` remain downstream evidence/measurement seams.

## 3. Negative semantic assertions

Normal-context root must not present as live law:

- `close_unconsumed` as current Assessment-credit state;
- a current General Wellness 14-day timer;
- provider acceptance/open/read/Analytics as Product clock authority;
- payer unilateral post-redemption revocation of recipient Plan;
- recipient as refund beneficiary merely because recipient controls entitlement;
- provider settlement as prerequisite to Full Deletion completion;
- cumulative numeric ceiling lowering as ordinary rollback;
- General Wellness as paid personalised Plan fulfilment;
- Analytics/Audit/support queue as business-state authority;
- universal Super Admin authority;
- R249/R300 as already-frozen Product Law;
- `OPS-UPD-008` or `OPS-PT-471`.

## 4. Provenance assertions

- deep v0.32 SHA-256 is exactly `9d7895b6db1b9b2eb12b3c7c0ff38c16f29915ea730967e2a7c514c8c40fb518`;
- v0.32 itself is described as an authoring candidate, not falsely as the source of a clean review verdict;
- early PT evidence is mapped to discovery v0.1...v0.14;
- later PT evidence is mapped to deep-control sections through v0.32;
- historical archive relocation reuses exact Git blob identities;
- old compressed candidate is preserved unchanged under `deep/archive/`.

## 5. JIT boundary

The compact pack defines semantics and gates only. Exact Resources, Ash actions, schema/locks/indexes/jobs/queues/UI/cache/provider APIs/retention-field/runbook/event representations remain downstream unless higher authority fixes them.

## 6. Verification outcome

This file is completed only after mechanical checks are run against the final root. `FINAL COMPACT WORKING PACK` status in README/manifest is permitted only when all checks above pass and the final tree/hash inventory is produced.

## 7. Repository-finalisation status

Local source/compact semantic and identifier checks pass, but repository-level finalisation is **BLOCKED** in this connector-only session on two explicit provenance mechanics:

1. the exact 442,866-byte v0.32 deep source is available locally and its SHA-256 is verified, but the available GitHub write actions accept text content rather than a mounted-file parameter, so the local source cannot be safely materialised into the repository without reserialising a very large artifact through the chat layer;
2. historical branch-root artifacts can be relocated byte-identically by reusing their existing Git blob SHA objects, but the connector does not provide raw-byte materialisation for redundant SHA-256 computation.

Therefore:
- no branch ref was advanced;
- no historical file was rewritten;
- no `FINAL COMPACT WORKING PACK` claim is made by the locally corrected pack;
- the remaining blocker is packaging/provenance mechanics, not a semantic Operations Pre-JIT gap.

A git-capable/local-files repository session can finish by copying the verified deep source, `git mv`-ing historical artifacts, computing redundant SHA-256 values, running `git diff --check`, validating the manifest, and committing one bounded documentation change.
