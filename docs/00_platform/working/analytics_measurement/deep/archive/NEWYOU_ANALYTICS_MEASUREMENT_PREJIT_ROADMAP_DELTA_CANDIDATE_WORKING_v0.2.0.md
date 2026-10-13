# NewYou Analytics & Measurement Pre-JIT — ANL-UPD-001 Roadmap Promotion Candidate Working v0.2.0

```text
WORKING / NON-AUTHORITATIVE
ROADMAP AUTHORITY-PROMOTION PATCH CONTRACT
DO NOT TREAT AS CURRENT ROADMAP
IMPLEMENTATION NOT AUTHORISED
```

- **Prepared:** 2026-10-10
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Current Roadmap authority:** `05_ROADMAP_v1.2.0.md`
- **Expected semantic successor if promoted:** `05_ROADMAP_v1.3.0.md`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_ROADMAP_DELTA_CANDIDATE_WORKING_v0.1.0.md` — preserved unchanged.
- **Source pressure tests:** Pass 4 accepted; Pass 5 recorded in `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.5.0.md`.
- **Related records:** `ANL-EV-012`, `ANL-PT-005`, `ANL-PT-007`–`ANL-PT-018`, `ANL-GAP-001`, `ANL-UPD-001`.

---

## 1. Candidate purpose

This document fixes the **promotion patch contract** for `ANL-UPD-001`. It is deliberately not the full Roadmap successor and cannot become authority by itself.

The eventual Roadmap v1.3.0 candidate must be assembled from the exact current v1.2.0 bytes plus only the semantic edits below, then independently reviewed as one exact candidate before any merge or authority claim.

---

## 2. Header / successor lifecycle patch

If promoted, create `05_ROADMAP_v1.3.0.md` with lifecycle metadata equivalent to:

```text
Document status: FROZEN / AMENDED ROADMAP v1.3.0
Document version: v1.3.0
Predecessor frozen version: archive/05_ROADMAP_v1.2.0.md
SemVer transition: v1.2.0 → v1.3.0
Last updated: promotion date
```

Preserve the exact current `05_ROADMAP_v1.2.0.md` bytes at `archive/05_ROADMAP_v1.2.0.md`.

Do **not** rewrite historical v1.1.x or v1.2.0 amendment-scope text. Add a new v1.3.0 amendment-scope section.

### Proposed v1.3.0 amendment-scope meaning

> This semantic Roadmap successor explicitly activates one bounded Research & Feedback mode inside FP-006: the mandatory controlled-pilot value/relevance/price-value feedback instrument already required by Product Law. Research & Feedback owns the governed instrument/question version and participant-response lifecycle for that bounded mode; Analytics remains downstream measurement authority. FP-005 basic participant progress/usefulness feedback remains Habits, Journals & Progress truth where that purpose fits. Broader Research campaigns, studies, arbitrary instruments and generic survey capability remain future-gated / Feature-Pack-unassigned. No new Feature Pack, Product Law, Domain Law or Architecture decision is created. Implementation remains unauthorised.

---

## 3. §2 mature-capability replacement

Replace only the current Research & Feedback row meaning with:

| Mature capability family | Approved outcome represented in this Roadmap |
|---|---|
| Research & Feedback | Bounded lightweight Research/Feedback and governed Research campaigns owned by Domain 19. The Product-Law-required FP-006 controlled-pilot value/relevance/price-value instrument is explicitly activated as a narrow MVP evidence mode. Its governed instrument/question version and participant response are Research & Feedback truth; Analytics owns downstream measurement only. FP-005 basic progress/usefulness feedback remains Habits, Journals & Progress truth where that purpose fits. All broader Research campaigns, studies, arbitrary instruments and generic survey capability remain **FUTURE-GATED / FEATURE-PACK-UNASSIGNED** and are not automatically assigned to FP-008, FP-009 or another pack. |

Voting & Balloting and all other rows remain unchanged.

---

## 4. §3.3 Domain/Feature-Pack challenge replacement

Replace only the `New Domains 19/20 require new Feature Packs` decision meaning with:

| Assumption challenged | Roadmap decision |
|---|---|
| New Domains 19/20 require new Feature Packs | Rejected. A Domain is not a Feature Pack. Research & Feedback is explicitly activated inside existing FP-006 only for the mandatory controlled-pilot value/relevance/price-value instrument; all broader Research capability remains future-gated / Feature-Pack-unassigned. Voting & Balloting remains fully future-gated / Feature-Pack-unassigned until a later governed Roadmap decision assigns an activating outcome. |

---

## 5. §3A future-gated capability refinement

Keep the general anti-silent-activation rule. Add an explicit bounded exception:

> **Bounded FP-006 Research & Feedback activation:** Roadmap v1.3.0 is the governed activating decision for one narrow Domain-19 mode only: the Product-Law-required controlled-pilot value/relevance/price-value feedback instrument inside FP-006. This exception does not activate general Research campaigns, studies, arbitrary instruments, generic survey tooling or other Research modes.

Replace the Research & Feedback row meaning with prose/table content equivalent to:

| Capability | Domain / ownership | Status | Explicit boundary |
|---|---|---|---|
| Research & Feedback | Domain 19 — Research & Feedback | Bounded FP-006 activation; otherwise `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` | FP-006 activation is limited to the mandatory controlled-pilot value/relevance/price-value instrument. Not FP-005. Broader Research campaigns/studies/arbitrary instruments remain future-gated. No Research Feature Pack is created. |

The final authority file should prefer ordinary prose over inventing a new governed lifecycle/status identifier if that keeps the Roadmap vocabulary cleaner.

### §3A closing-paragraph refinement

Replace the absolute no-present-blocker meaning with:

> Future-gated capability rows do not create automatic OQ blockers merely because the capability exists. The bounded FP-006 Research & Feedback activation creates no new OQ by Roadmap fiat; normal FP-006 Phase 7 gate-manifest/JIT adjudication must identify the minimum applicable Domain, Privacy, retention/deletion, proof and operational obligations before that instrument can be implemented. Future Voting and broader Research modes remain gated only when explicitly activated.

This prevents two opposite errors: inventing a new OQ prematurely, or pretending an activated source Domain has no downstream JIT obligations.

---

## 6. FP-006 Affected Domains patch

Use:

> **Affected Domains:** `Identity & Access`; `Privacy & Consent`; `Commerce`; `Entitlements`; `Temperament`; `Health Records`; `Safety & Eligibility`; `Plans & Nutrition`; `Content & Media`; `Communications`; `Research & Feedback`; `Analytics`; `Audit & Evidence`.

No ownership is reassigned. Research & Feedback is listed because its already-owned truth is now sequenced into this outcome.

---

## 7. FP-006 bounded activation paragraph

Add immediately after the paid-pilot evidence contract and before `Deferred From This FP`:

> **Bounded Research & Feedback activation:** FP-006 explicitly activates Research & Feedback only for the controlled-pilot value/relevance/price-value feedback instrument required by Product Law §§21T.5–21T.9. The governed instrument/question version and participant-submitted response lifecycle are Research & Feedback truth. Analytics may consume permitted projections and derive response rate, positive-value/relevance distributions, cohort comparisons and release evidence, but does not become participant-response authority. FP-005 basic daily/weekly progress/usefulness feedback remains Habits, Journals & Progress truth where its primary purpose is participant self-tracking/progress. This activation does not admit general Research campaigns/studies, arbitrary survey-builder capability or unrelated feedback modes into MVP. Exact participation identity/uniqueness mode, correction/withdrawal/de-link behaviour, privacy/retention requirements, provider choice, Resource/schema design and required JIT/proof work remain for normal FP-006 Phase 7 adjudication under current authority.

---

## 8. FP-006 deferred-scope patch

Extend `Deferred From This FP` to include:

> broader Research campaigns/studies, arbitrary instruments and generic survey-builder capability beyond the mandatory bounded FP-006 pilot-feedback instrument

All existing deferrals remain intact.

---

## 9. Authority-routing collateral contract

These are **promotion collateral**, not extra semantic amendments.

### README

Change the current-authority route from:

```text
7. 05_ROADMAP_v1.2.0.md
```

to:

```text
7. 05_ROADMAP_v1.3.0.md
```

Any nearby prose that explicitly calls v1.2.0 current must be updated consistently. Historical source-at-freeze references remain historical.

### Current authority manifest

The `ROADMAP` governing-document record must become:

```text
canonical_filename: 05_ROADMAP_v1.3.0.md
semver: 1.3.0
repository_path: docs/00_platform/05_ROADMAP_v1.3.0.md
authority_class: ROADMAP
sha256: <exact SHA-256 of frozen v1.3.0 candidate bytes>
superseded_version: 1.2.0
lifecycle: current
graph_policy: frozen_provenance
provenance_sha256: <same exact v1.3.0 SHA-256>
```

Do not fill the hash until exact candidate bytes exist.

The manifest should also preserve/register the v1.2.0 archive predecessor according to the repository's current historical-document conventions.

### Open Work

Create the next planning-state successor from whatever Open Work version is current **at promotion time**. On the currently verified baseline that would be expected to succeed v1.2.59, but the exact version must be rechecked immediately before promotion.

Its semantic scope must be limited to:

- recording Roadmap v1.3.0 as current;
- recording that the FP-006 bounded Research & Feedback Roadmap sequencing contradiction is resolved at Roadmap level;
- preserving the active FP-001/HARDEN-02/Communications programme state and STOP conditions unless independently changed;
- preserving the current fact that Analytics is not required for the active FP-001 conditional-dossier programme;
- not starting FP-006 Phase 7, a Research JIT dossier, proof work or implementation.

---

## 10. Derived Delivery Atlas follow-up

The current Atlas is derived/non-authoritative and currently routes Roadmap v1.2.0. After successful authority promotion, create a later Atlas routing/reconciliation successor that:

- routes current Roadmap to v1.3.0;
- derives bounded Research & Feedback participation for FP-006;
- preserves FP-005 HJP basic-feedback distinction;
- creates no new gate, Feature Pack, Domain or implementation authority.

Atlas reconciliation is not part of Roadmap law and must not delay or redefine an otherwise valid authority promotion.

---

## 11. Explicit non-changes

The promotion candidate must leave unchanged:

- Product-Law survey thresholds, meanings and fixed question wording;
- Decision Register semantics;
- Domain 19 ownership law;
- Architecture;
- FP-005 HJP basic-feedback guardrail;
- all 17 Feature Pack identifiers and the dependency graph;
- Voting & Balloting future-gated status;
- FP-016 experimentation sequencing;
- current FP-001 programme status and dossier requirements;
- exact identity/uniqueness/privacy/retention/provider/resource/event implementation details;
- proof classification until normal FP-006 Phase 7 adjudication.

---

## 12. Freeze and certification gate

Before `ANL-UPD-001` can be marked resolved:

1. assemble exact `05_ROADMAP_v1.3.0.md` bytes from current v1.2.0 plus only this accepted patch;
2. preserve v1.2.0 byte-identically in archive;
3. compute exact SHA-256 pins;
4. produce README/manifest/Open Work candidate collateral against the then-current baseline;
5. compare the exact candidate against current authority and verify no unrelated semantic drift;
6. independently review the exact head;
7. only then consider PR/merge/promotion under normal governance.

Until then:

```text
ANL-GAP-001 = UPSTREAM_ACTION_REQUIRED
ANL-UPD-001 = PROMOTION_PATCH_CONTRACT_DRAFTED
CURRENT ROADMAP = 05_ROADMAP_v1.2.0.md
FP-006 SURVEY JIT/IMPLEMENTATION = BLOCKED AT ROADMAP AUTHORITY
```
