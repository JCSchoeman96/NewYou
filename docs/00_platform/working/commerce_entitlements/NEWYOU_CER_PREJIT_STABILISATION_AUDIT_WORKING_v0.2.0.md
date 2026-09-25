# NewYou Commerce / Entitlements / Recurring Membership Pre-JIT — Renewed Stabilisation / Completeness Audit

- **Audit version:** `v0.2.0`
- **Date:** `2026-09-10`
- **Status:** COMPLETE
- **Audited deep source:** `NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.1.md`
- **Audited deep-source SHA-256:** `921f865d79456f4b507499c23e2e9920229f3d467c22a98296324f7d1fa9a29c`
- **Repository mutation:** NONE
- **Purpose:** Independently determine whether the corrected cumulative CER deep source is semantically stable and complete enough at broad Pre-JIT scope to become the source for final recompression, without opening a third broad pressure-test round.

---

# 1. Outcome

> **CER SEMANTIC DISCOVERY: PASS**
>
> **SECOND-PASS CLOSURE GRILL: PASS**
>
> **EXACT `v0.30.1` DEEP SOURCE: PASS — STABLE FOR FINAL RECOMPRESSION**
>
> **BROAD COMMERCE PRE-JIT DISCOVERY: STOP — NO THIRD BROAD PRESSURE-TEST ROUND**
>
> **CURRENT COMPACT `v0.1.1`: PROVISIONAL / NOT FINAL-CERTIFIED**
>
> **CER PARKING: NOT YET COMPLETE — RECOMPRESSION + INDEPENDENT COMPRESSION/SOURCE VERIFICATION REMAIN**

No blocking semantic contradiction, competing Domain authority, missing ordinary-lifecycle class, or new broad Product gap was found.

The thirteen CER upstream deltas remain accepted **working/non-authoritative** inputs. This audit does not promote them into Product Law.

---

# 2. Canonical evidence baseline

## NewYou

Independently rechecked live GitHub:

- repository: `JCSchoeman96/NewYou`
- `main`: `1c899f58c9d5fb61d15d0263ee0b6ec595f5f614`

The routed current authority remains:

1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`
2. `00_PLATFORM_v1.3.0.md`
3. `01_DECISIONS_v1.3.0.md`
4. `02_OPEN_WORK_v1.2.40.md`
5. `03_ARCHITECTURE_v1.1.1.md`
6. `04_DOMAIN_MAP_v1.1.1.md`
7. `05_ROADMAP_v1.1.0.md`
8. `PLATFORM_OPERATING_MODEL_v1.0.1.md`
9. `FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` when relevant.

The current authority manifest independently confirms those versions.

## Store Blueprint Hardening

Current reviewed baselines:

- `main`: `56f06d028ec38896f5a927f54dc7adfcb20034a3`
- `hardening/subscriptions`: `54871ef3bdda42f067ed5dbd398305151610c060`

The movement from the earlier `575ffa1848ac69abe855bd018c7ae8eaf05d61e4` runtime-evidence baseline came through Store PR #12 and was governance/control-plane only. It did not modify production subscription source, migrations or configuration. Therefore earlier runtime conclusions remain materially applicable, while `54871ef3...` is the current reviewed branch head.

Historical deep-source sections correctly retain the exact SHAs they originally inspected.

---

# 3. Provider evidence refresh

Current official Paystack documentation was rechecked.

The following current provider facts remain compatible with CER:

- subscription billing has explicit recurring billing cycles / next-payment dates;
- a failed Paystack subscription charge is not automatically retried for the same failed attempt; later provider charging behaviour remains distinct from NewYou's own governed dunning/reconciliation policy;
- subscription plan updates may be applied to existing subscriptions and then take effect on the next billing cycle;
- reusable payment authorisations can be stored and charged subsequently where marked reusable;
- transaction state can remain non-final and must be verified/reconciled rather than inferred from one callback;
- failed webhook delivery is retried for a finite provider window; recovery cannot depend on infinite webhook delivery.

Provider references checked:

- `https://paystack.com/docs/payments/subscriptions/`
- `https://paystack.com/docs/payments/recurring-charges/`
- `https://paystack.com/docs/payments/webhooks/`
- `https://paystack.com/docs/payments/verify-payments/`
- `https://paystack.com/docs/api/subscription/`
- `https://paystack.com/docs/api/plan/`

**Audit conclusion:** CER continues to use the correct ordering:

`NewYou semantics → provider-independent invariant → Paystack validation → mechanism`

`OQ-004` remains open and correctly prevents provider behaviour from becoming Product Law.

---

# 4. Mechanical / document-consistency verification

The exact audited bytes passed the following checks:

| Check | Result |
|---|---|
| Deep source version is `v0.30.1` | PASS |
| `CER-PT` headings are exactly `001...020` | PASS |
| Pressure-test register contains exactly `001...020` | PASS |
| `CER-UPD` headings are exactly `001...013` | PASS |
| Section 10 indexes all thirteen current accepted deltas | PASS |
| Standing anti-drift principles are sequential `1...201` | PASS |
| No duplicate PT/UPD heading identifiers | PASS |
| No `CER-PT-021` heading | PASS |
| No `CER-UPD-014` heading | PASS |
| No stale “Candidates 2–15 remain pending” current-state text | PASS |
| No stale “second-pass round active” current-state text | PASS |
| No stale “all four accepted directions” summary | PASS |
| Current Store header baseline is `54871ef3...` | PASS |
| Historical Store SHAs remain preserved where historically inspected | PASS |
| PT-006 metadata restored to PASS / no originating `CER-UPD-006` | PASS |
| PT-008 distinguishes original PASS from Candidate-3 `CER-UPD-006` refinement | PASS |
| PT-011 later `CER-UPD-010` / `CER-UPD-013` cross-links present | PASS |
| PT-012 originating `CER-UPD-003` + later `011` / `013` cross-links present | PASS |
| PT-020 originating `CER-UPD-012` + later `013` cross-link present | PASS |
| Markdown parentage repaired before PT-005 via Section `12A` | PASS |
| Prospective Candidate references normalised retrospectively | PASS |
| No merge-conflict markers | PASS |

The accumulated changelog still contains historical statements that were true at those historical versions. Those are preserved provenance and are not current-state defects.

---

# 5. Domain / authority audit

## Commerce

The deep source consistently keeps Commerce authoritative for:

- commercial offer / price / promotion truth;
- purchase and payment truth;
- refund, dispute and excess-collection truth;
- membership/subscription/add-on commercial contract truth;
- renewal/cancellation/cadence/price-transition ordering;
- provider evidence verification and reconciliation.

## Entitlements

The deep source consistently keeps Entitlements authoritative for:

- grant/right identity and scope;
- source provenance;
- validity / expiry / revocation;
- bundle/component decomposition;
- gift/sponsored/complimentary/lifetime grants;
- limited-credit/benefit consumption;
- current access decisions;
- source-specific target-set convergence.

## Identity & Access

Canonical grantee identity remains outside Commerce/Entitlements and is resolved through Identity & Access.

## Non-authorities

The document continues to reject provider state, queue state, Cachex/ETS/PubSub, UI state and projections as business authority.

**Outcome: PASS.**

No Subscriptions, Membership, Gift, Sponsor, Pricing, Promotion, Redemption or Provider Domain is justified.

---

# 6. Semantic completeness audit by lifecycle cluster

## 6.1 Provider evidence / recurring identity

Covered by PT-001...004 and PT-015:

- provider success followed by local crash;
- duplicate/replayed callbacks;
- delayed/missing/reordered/contradictory evidence;
- stable renewal occurrence;
- provider-safe retry identity;
- long outage/backlog/reconciliation;
- source-target recovery rather than process-history replay.

**PASS.**

## 6.2 Failed renewal / cancellation / cadence

Covered by PT-005, PT-006, PT-008 and PT-016 plus `CER-UPD-001`, `005`, `006`:

- grace and suspension;
- cancellation during unresolved renewal;
- late success precedence;
- cancellation rescission before termination;
- post-termination re-subscription;
- monthly↔annual future-boundary cadence changes;
- multiple future instructions before one boundary.

**PASS as Pre-JIT discovery.**

The Product gaps are already captured; no new broad delta is needed.

## 6.3 Upgrade / downgrade / add-on composition

Covered by PT-007, PT-008, PT-011 plus Candidate 9, Candidate 10, Candidate 11 and Candidate 14:

- success-gated immediate upgrade;
- failed/ambiguous upgrade preserving the existing paid composition;
- renewal-effective downgrade;
- Basic + aligned add-ons as one membership composition by default;
- add-on add/remove lifecycle;
- stale-safe future-contract supersession;
- exact source-specific Entitlements target-set convergence.

**PASS.**

## 6.4 Price / grandfathering / recurring promotion

Covered by PT-017 / PT-018 and `CER-UPD-007` / `008`:

- public list price ≠ existing member contract;
- immutable already-committed renewal price;
- future price migration;
- deliberate grandfathering;
- finite recurring promotional lifecycle;
- promotion consumption on successfully established qualifying periods rather than attempts;
- interaction with package/cadence changes.

The required South African consumer-protection/legal expert gate remains explicit before exact Product-law freeze.

**PASS.**

## 6.5 Duplicate purchase / excess collection

PT-019 correctly distinguishes:

- duplicate evidence for one payment occurrence; from
- two distinct purchase/payment attempts that both genuinely succeed.

One ordinary membership relationship may result; excess financial collection remains truthful and must be reversed/refunded/remedied without creating a second membership or entitlement period.

**PASS.**

## 6.6 Gift / sponsor / complimentary / lifetime / multi-source

Covered by PT-012, Candidates 12/15 and `CER-UPD-003`, `011`, `013`:

- purchaser ≠ recipient ≠ canonical grantee;
- fixed/prepaid gift as default;
- explicit recurring sponsorship authority;
- redemption boundary;
- overlap with existing membership;
- future coverage without silent duplicate self-billing;
- access-overlay versus qualifying membership-coverage grants;
- independent source provenance;
- capability-specific effective access;
- no global source hierarchy;
- no automatic multiplicative recurring benefits.

**PASS.**

The later upstream adjudication should reconcile `003`, `010`, `011`, `013` into a coherent Product-law cluster rather than mechanically creating separate competing Decisions.

## 6.7 Premium 12-month continuity / reassessment

PT-020 and `CER-UPD-012` / `013` provide a coherent model:

- qualifying Premium coverage time, not charge count;
- cadence/payment-method/funding-source changes do not inherently reset continuity;
- seamless qualifying source hand-off preserves continuity;
- overlap does not accelerate the clock;
- genuine Premium gap/downgrade resets continuity;
- grace remains provisional until Commerce proves the paid period;
- initial annual purchase is not annual renewal;
- at most one unused reassessment entitlement;
- no hidden catch-up accumulation;
- unused benefit ends when qualifying Premium ends.

**PASS.**

## 6.8 Refund / dispute / chargeback / manual EFT

PT-009 / PT-010 / PT-013 plus `CER-UPD-002` / `004` preserve:

- truthful historical fulfilment;
- source-scoped reversal consequences;
- pending dispute distinct from final loss;
- no silent destruction of historical evidence;
- manual-EFT access only after authoritative verification;
- ordinary on-demand manual-EFT period commencement at lawful verification/activation.

**PASS.**

---

# 7. Late-renewal-period anchor adjudication

The final bounded question was:

`renewal due 1 Sep`
`→ grace / suspension`
`→ same renewal occurrence reconciled paid on 6 Sep`

Does the period become `1 Sep → 1 Oct` or `6 Sep → 6 Oct`?

## Conclusion

> **COVERAGE CONFIRMED — NO NEW CER-PT / NO NEW CER-UPD.**

For a late success reconciled as the **same renewal occurrence**, the paid period retains the original scheduled renewal boundaries.

Therefore:

`1 Sep → 1 Oct`

is the default commercial period.

The later provider/webhook/reconciliation timestamp is evidence timing; it does not create a fresh renewal occurrence or rebase the subscription calendar.

This conclusion follows the existing combination of:

- PT-004 stable renewal identity tied to one governed billing period;
- PT-006 late success explicitly constrained to the same still-authorised renewal occurrence;
- monthly/annual paid-period Product semantics;
- prohibition on multiple period extensions for one renewal occurrence.

Starting a new full term on the reconciliation date would silently transform the same renewal into a new commercial occurrence and move the next renewal boundary.

## Important distinctions

This does **not** override `CER-UPD-004`: an ordinary on-demand **initial manual-EFT** membership has a different commencement rule because no recurring renewal period already existed.

If valid payment existed but NewYou/provider failure wrongly denied access, a separate customer remedy/make-whole may be required. That remedy does not shift the recurring renewal boundary by default.

**Audit result: PASS / clarification only.**

---

# 8. Cross-stream audit

## HSP

CER correctly defers admitted-before-expiry Plan/review completion to existing `HSP-UPD-001` and preserves HSP ownership of paid-fulfilment/remedy seams.

Current HSP working evidence still contains `HSP-UPD-001` as the bounded completion-right question.

No duplicate CER delta is justified.

## Privacy

CER correctly preserves the Privacy rule that unavoidable late financial operations may reconcile to truthful Commerce outcomes after Full Deletion but must not recreate product/Entitlement access.

Current Privacy working evidence remains compatible with CER's stable renewal and late-reconciliation rules.

**Outcome: PASS.**

No cross-stream contradiction was found.

---

# 9. Store reuse audit

The Store reuse analysis remains appropriately conservative.

## Strong reusable primitives

- stable renewal identity / RenewalAttempt concepts;
- provider/payment evidence ingestion;
- apply-once payment consequences;
- payment reconciliation;
- immutable commercial snapshots;
- source-aware EntitlementGrant identity;
- bounded entitlement validity;
- refund/payment infrastructure.

## Material NewYou reuse gaps remain

- Paystack adaptation;
- reordered outcome hardening;
- subscription terminal/suspension recovery;
- immutable future contract/version ordering;
- cadence changes;
- existing-member price migration;
- recurring promotion lifecycle;
- duplicate membership admission under concurrency;
- payment-method race handling;
- success-gated immediate upgrades;
- Basic/add-on/Premium composition;
- gift/sponsor/complimentary/lifetime source taxonomy;
- source-specific target entitlement-set convergence;
- multi-source limited-benefit rules;
- cache/non-authority correctness proof.

## Important scope boundary

NewYou-specific Product rules such as:

`12 qualifying Premium months → reassessment`

must **not** be pushed into the reusable Store package.

Store should provide generic commercial-period, payment and entitlement-provenance primitives.

**Store reuse analysis outcome: PASS.**

**Actual engine classification remains: REUSE AFTER HARDENING / ADAPTATION REQUIRED.**

---

# 10. Upstream-delta audit

Exactly thirteen accepted CER deltas remain.

They are credible, but they are not thirteen automatic future Decision amendments.

Recommended later adjudication clusters:

| Cluster | CER inputs |
|---|---|
| Renewal / cancellation / cadence contract | `001`, `005`, `006` |
| Price / recurring offer terms | `007`, `008` |
| Wrong / duplicate collection remedy | `009` + relevant part of `001` |
| Gift / add-on / package / multi-source coverage | `003`, `010`, `011`, `013` |
| Disputes / reversal | `002` |
| Manual EFT | `004` |
| Premium continuity benefit | `012` |

Cross-stream Product adjudication should then reconcile overlapping HSP / Privacy / CER deltas into the smallest coherent governed amendment set.

**PASS.**

---

# 11. Third-round decision

A third broad CER pressure-test round is **not recommended**.

The second pass demonstrated composability: several additional scenarios reduced to existing renewal, ordering, entitlement, provenance and recovery rules rather than earning new PT identifiers.

Further ordinary cases such as duplicate cancel clicks, stale UI, checkout abandonment, support retry or upgrade-during-grace should now be handled in:

- Feature Pack/JIT lifecycle design;
- Architectural Proof;
- tracer/vertical-slice proof;
- implementation tests;

unless a downstream exercise exposes a genuine upstream contradiction.

Continuing broad Pre-JIT discovery now would increase speculation more than confidence.

**Decision: STOP broad discovery.**

---

# 12. Blocking and non-blocking findings

## Blockers

**NONE against `v0.30.1` as the final deep source for recompression.**

The accepted `CER-UPD-*`, HSP/Privacy seams and `OQ-004` remain deliberate upstream/provider gates; they are not defects in the Pre-JIT artifact.

## Non-blocking corrections

**NONE required before recompression.**

Any later wording-only polish must either preserve the exact audited SHA or trigger a mechanical recertification of the changed deep source before compression.

---

# 13. Final certification

The exact deep-source bytes:

`NEWYOU_CER_PREJIT_DISCOVERY_WORKING_v0.30.1.md`

SHA-256:

`921f865d79456f4b507499c23e2e9920229f3d467c22a98296324f7d1fa9a29c`

are certified:

> **PASS — STABLE FOR FINAL RECOMPRESSION**

This is **not yet `PASS — PARK CER`**, because the compact representation has not yet been regenerated and independently verified against this exact source.

The required next sequence is:

`audited v0.30.1`
`→ rebuild compact CER pack`
`→ independent compression audit`
`→ mechanical/content source↔compact verification`
`→ PASS — PARK CER`
`→ HSP + Privacy + CER cross-stream upstream-delta adjudication`

No third broad CER grill is authorised by this audit.

---

# 14. Audit anti-drift rule

If the deep source changes after SHA `921f865d79456f4b507499c23e2e9920229f3d467c22a98296324f7d1fa9a29c`, this audit does not automatically certify the changed bytes.

If NewYou current Product/Architecture/Domain authority changes materially before compression, recheck only the affected CER conclusions rather than reopening broad discovery by default.

If Store `hardening/subscriptions` moves through runtime implementation changes before reuse certification, Store-specific conclusions must be reviewed against the new head.

