# NewYou Programmes & Learning Compression Audit Working v0.1.0

- **Status:** COMPRESSION AUDIT / NON-AUTHORITATIVE
- **Authority:** NONE
- **Implementation authority:** NONE
- **Compression rule:** compress repetition, not semantic breadth.

# 1. Semantic-family preservation

| Semantic family | Disposition | Compact destination / note |
|---|---|---|
| Programme / ProgrammeVersion | PRESERVED_COMPRESSED | Contract §§1–2 |
| Enrolment / attempt | PRESERVED_COMPRESSED | Contract §3; fail-closed lifecycle boundaries retained |
| Delivery modes | PRESERVED_COMPRESSED | Contract §4 |
| Release / availability / sequencing | PRESERVED_COMPRESSED | Contract §4; visibility, release, access, availability and completion kept distinct |
| Edition / Cohort | PRESERVED_COMPRESSED | Contract §4; conditional composition |
| Entitlements / access | PRESERVED_COMPRESSED | Contract §5 |
| Content / localisation / versioning | PRESERVED_COMPRESSED | Contract §6 |
| Requirement classes | PRESERVED_COMPRESSED | Contract §7 |
| Evidence ownership | PRESERVED_COMPRESSED | Contract §7 |
| Completion / certificates | PRESERVED_COMPRESSED | Contract §8 |
| Exceptions / substitutions | PRESERVED_COMPRESSED | Contract §7.1 + completion/recovery gap routes; exemption/substitution/alternate evidence kept distinct |
| Recovery | PRESERVED_COMPRESSED | Contract §9 |
| Live / replay | PRESERVED_COMPRESSED | Contract §11 |
| Community | PRESERVED_COMPRESSED | Contract §12 |
| Safety / Professional boundary | PRESERVED_COMPRESSED | Contract §14 |
| HJP / private reflections | PRESERVED_COMPRESSED | Contract §10 |
| Communications | PRESERVED_COMPRESSED | Contract §13 |
| Operator correction | PRESERVED_COMPRESSED | Contract §15 |
| Concurrency / retry / reordering | PRESERVED_COMPRESSED | Contract §3.2 / §15 |
| Historical provenance | PRESERVED_COMPRESSED | Contract §§2, 6, 15; side-effect-free explanation + lawful-deletion limit retained |
| Analytics / measurement | PRESERVED_COMPRESSED | Contract §16 |
| FP-014 second-lens reuse | PRESERVED_COMPRESSED | Contract §17 |
| Gap routing | ROUTED_TO_GAP_REGISTER | Upstream Delta Register |
| Product-first fail-closed cells | PRESERVED + ROUTED_TO_GAP_REGISTER | Contract §§3.1, 19 + v0.25.1 |
| Anti-LMS / YAGNI | PRESERVED_COMPRESSED | Contract §20 |
| Evidence / pressure-test detail | ROUTED_TO_EVIDENCE_INDEX | Evidence Index + deep/archive |

# 2. Supersession discipline

- `v0.25.1` is the frozen semantic handoff.
- `v0.25.2` is acceptance/provenance/retrieval hygiene and does not semantically replace v0.25.1.
- `v0.25.0` lifecycle claims that declared completion/abandonment universally terminal, required resume before completion while paused, or let technical first-commit order choose Product meaning are **SUPERSEDED / HISTORICAL_ONLY**.
- Pass-23 current-state language superseded by Pass-24 routing is **HISTORICAL_ONLY**.
- Older evidence remains provenance; it is not competing current truth.

# 3. Ownership preservation

The compression preserves `one durable truth → one owner`. No compact sentence grants shared-write authority to UI, operator surfaces, Analytics, Audit, provider state, PubSub, caches or JIT.

# 4. Nuwe Jy / reusable Programme separation

The compact contract preserves the generic Programme centre while keeping Nuwe Jy-specific 60-day, Today, drip, Community, Live and operational composition non-universal. FP-014 remains the second-lens proof that Edition/Cohort and flagship composition are conditional.

# 5. Product uncertainty preservation

Unsupported lifecycle semantics remain explicit Product decisions. Compression does not fill those gaps with a state machine or technical precedence. Product-first stops are kept distinct from other authority gates: `PRG-GAP-002`, `PRG-GAP-011`, `PRG-GAP-003/PRG-UPD-001` and unsupported lifecycle cells route to Product; `PRG-GAP-007` remains an HJP/Privacy/retention gate when triggered rather than being mislabeled as generic Product work.

# 6. Historical preservation method

Historical ledgers remain append-only provenance and must not be rewritten for cleanliness. Repository-level byte/hash preservation is a mechanical commit-time check, separate from this semantic audit.

# 7. Scope audit

Compression creates no new Product, Architecture or Domain authority; no new gap/update identifier; no Feature Pack; no application code; no implementation authority; no generic LMS/workflow/saga/event-store design.
# 8. Second semantic re-audit promotions

A second source-to-compact review promoted several semantics that were previously only implicit or deep-history-only. These are now explicit in the root contract rather than relying on a smaller agent to infer them:

- governed structural hierarchy `Programme → ProgrammeVersion → Module → Lesson → Activity`, while `Day/Today` remains composition rather than a universal structural layer;
- compact verb-by-verb Enrolment lifecycle handoff preserving the authorised positive meaning of enrol/schedule/begin/pause/resume/complete/abandon/restart while leaving terminality/ordering/source-state questions fail-closed;
- `PRG-GAP-010` Programme-identity review for fundamental purpose/outcome/audience/risk changes;
- Edition→ProgrammeVersion pinning, multi-Cohort shared-schedule semantics, pre-commit edit vs post-commit exceptional lifecycle, and no implicit facilitator manual unlock;
- Entitlement does not create Enrolment, Enrolment does not create Entitlement, and historical participation does not prove current access;
- translation/version asymmetry, optional low-risk fallback limits, separate language vs clinical/Safety/legal approvals, and prohibition on localisation changing Programme/Safety/Entitlement meaning;
- Programme-native self-attestation boundary, multi-owner check-in composition, evidence-minimisation/no-overtracking, and fail-closed handling of unavailable source evidence;
- conditional-requirement predicate/timing/re-evaluation policy and explicit numerator/denominator treatment of exemption/not-applicable/substitution;
- derived next-smallest-useful recovery guidance rather than indiscriminate backlog dumping;
- HJP habit-source distinctions, occurrence-state meaning, timezone/window ownership, and journal-sharing scope;
- replay asset/session/access ownership and replay-correction/non-clinical group-Q&A boundaries;
- Communications template/content owner, purpose/preference/mandatory-message separation, stale-message revalidation, purchaser-recipient separation and sensitive-data minimisation;
- Safety progressive collection, safe-modification authority, multi-owner check-in routing and urgent-help non-monitoring boundary;
- read/explain ≠ mutation authority and no generic operator `mark complete` fabrication;
- exact historical rule/threshold and Edition/schedule provenance, current-permission-vs-historical-truth distinction, and clean LearnDash cutover;
- late analytical evidence, restatement-vs-definition-change, and anti-denominator-shopping;
- FP-014 access/package independence and non-universal certificates/Community/Live;
- participant abandonment vs organiser cancellation vs Safety withdrawal, Event cancellation ≠ Edition cancellation, and source cause ≠ lifecycle authority;
- idempotency-identity collision semantics and live-equivalent repair/backfill invariants; and
- additional anti-LMS/YAGNI rejections already present in frozen historical decisions.

These additions do not create new authority. They reduce compression ambiguity.
