# NewYou Paystack Pre-JIT — Current Working Context v1.0.2

- **Status:** WORKING / NON-AUTHORITATIVE / DOCUMENTARY DISCOVERY FROZEN
- **Patch character:** STAGE-RESULT RECORDING / USABILITY ONLY — no new provider semantics, Product semantics, EV cases or Paystack research
- **Repository baseline:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Provider validation status:** `OQ-004 / FP-002 APPLICABLE SCOPE — BLOCKED ON EMPIRICAL TESTS`
- **Formal Product promotion:** outstanding
- **Empirical stage results recorded:** **NONE**
- **Execution summary:** cases with any executed stage `0 / 59`; fully satisfied cases `0 / 59`; executed stage slots `0 / 85`
- **Deep provenance ledger:** `deep/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.11.0.md`

## Start here

For ordinary FP-002 planning/JIT work, load these files in this order:

1. `NEWYOU_PAYSTACK_PREJIT_CONTRACT_WORKING_v1.0.0.md` — current effective semantics/invariants; unchanged by v1.0.2.
2. `NEWYOU_PAYSTACK_GAP_REGISTER_WORKING_v1.0.2.md` — actually-open blockers split by Product governance, provider mechanics, Phase 8 and release.
3. `NEWYOU_PAYSTACK_EMPIRICAL_MANIFEST_WORKING_v1.0.2.md` — current execution routing/result state: Wave + Execution Stage + Gate Effect + per-stage dispositions.
4. `NEWYOU_PAYSTACK_EVIDENCE_INDEX_WORKING_v1.0.2.md` — authority/provider evidence index.

### Mandatory empirical-case locator rule

Before executing any empirical case, load its exact `### PAYSTACK-EV-...` definition from the deep v0.11 ledger **unless the full setup/PASS/FAIL definition has been promoted into the empirical manifest**. The one-line purpose in the manifest is not sufficient to invent a test procedure.

Use the compact contract for current semantics, the v1.0.2 manifest for execution-stage/gate routing and stage-result disposition, and the deep ledger for exact detailed procedure/provenance. If those conflict, STOP and patch the working proof artifact rather than silently reconciling them.

## v1.0.2 stage-result recording correction

v1.0.1 correctly separated Wave, Execution Stage and Gate Effect but still exposed one lossy case-level `Status` field. v1.0.2 removes that field. Every case now records a disposition for each execution stage independently.

This means, for example, `EV-050` can truthfully record:

- `PRE_JIT_HARNESS_SANITY=PASS`;
- `PHASE8_ACTUAL_HTTP_STACK=NOT_EXECUTED`.

No derived case-level `PARTIALLY_EXECUTED` state is required. Summary reporting separately counts cases with any executed stage, fully satisfied cases, and executed stage slots. Individual run history remains evidence and must not be erased when a current stage disposition later changes after remediation/retest.

## v1.0.1 routing correction

The previous compact pack correctly ordered cases by risk wave but could make **Wave** look like the same thing as **proof stage/gate effect**. v1.0.1 separates them explicitly:

- `Wave` = dependency/risk execution order;
- `Execution Stage` = `PRE_JIT_*`, `PHASE8_*`, `RELEASE_*`, or `FUTURE_RECURRING`;
- `Gate Effect` = provider-mechanics freeze, Phase-8 proof, FP-002 outcome, channel admission, paid release, supporting evidence, or future-only.

Therefore release-only cases inside Waves 4/5/7 no longer appear to block safe internal Phase-8 proof merely because of wave number.

`EV-050` and `EV-051` now have an explicit two-stage requirement: a Pre-JIT harness-sanity result proves only the harness emits one mutation; the selected Elixir HTTP client/middleware/proxy stack must be re-proven in Phase 8 before the actual integration claim is satisfied.

## What remains frozen

The documentary/semantic discovery stream remains mature. Broad Paystack reading is stopped unless Paystack changes an affected contract, empirical evidence contradicts the model, FP-002 scope changes, live NewYou authority changes, or a new mandatory expert constraint appears.

The compact pack does **not** mean Paystack is validated. There are still zero empirical PASS results.

## Current decision boundary

Two Product semantics were discovered and accepted in working form but are not yet governed Product Law:

- duplicate/excess genuine collection -> exactly one valid right; full excess customer amount remains owed until made whole;
- partial final reversal/chargeback without deterministic component attribution -> record financial loss, but do not invent which component/right to revoke.

These should be promoted through normal Product governance before FP-002 Phase 7C relies on them. No repository mutation has been made by this compact stage-result recording patch.

## Recommended immediate empirical action

Start only the provider-only/harness-sanity portion of Wave 1: `EV-001/001A/001B/001C/002/009/009A/009B/041` plus `EV-050` stage A. Do **not** try to make Phase-8-only cases green before the actual NewYou proof environment exists.

The shortest safe provider scope remains **Paystack + South Africa + ZAR + card only** as a proof-scope recommendation, not permanent Product Law.

## Provenance integrity

The v1.0.1 compact pack remains preserved separately, and v1.0.0 remains preserved separately. Deep `v0.11.0` and its byte-prefix predecessor `v0.10.0` are copied unchanged into this v1.0.2 bundle.

## File hashes

| File | SHA-256 |
|---|---|
| `NEWYOU_PAYSTACK_PREJIT_CONTRACT_WORKING_v1.0.0.md` | `1ba714b884fd8952f0c3f92157ce9bc0ca9b353db2f33cf613bc75ef34e5e44e` |
| `NEWYOU_PAYSTACK_GAP_REGISTER_WORKING_v1.0.2.md` | `abfb419ad00fc848cb6c8f32166b1902a1a719110c2c1fb0e8e0164274c835f2` |
| `NEWYOU_PAYSTACK_EMPIRICAL_MANIFEST_WORKING_v1.0.2.md` | `efb9cec5b2875eea53bd6023ddeadba7f3e5fe5b46722a8e2695a6fd29192b96` |
| `NEWYOU_PAYSTACK_EVIDENCE_INDEX_WORKING_v1.0.2.md` | `6d25e419d6c20ea0aa8d2218def381ba679c2dbc1430b6441594ee1dae5b0764` |
| `deep/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.11.0.md` | `8399645c5c7f8ecb4e5d263b3c37379e7d710262ad9b7b388929bca3c54d0a6d` |
| `deep/archive/NEWYOU_PAYSTACK_VALIDATION_PREJIT_WORKING_v0.10.0.md` | `770a32bc3217443c2fbcbd47fe1919de027226fc078f83f2a556f79972814aaa` |
