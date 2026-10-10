# NewYou Analytics & Measurement Pre-JIT — ANL-UPD-001 Roadmap Promotion Candidate Working v0.3.0

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
- **Exact current Roadmap git blob:** `5432991071d4d1a7cbd9dc4c8fca48c823129f40`
- **Current manifest Roadmap SHA-256:** `601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0`
- **Expected semantic successor if later frozen/promoted:** `05_ROADMAP_v1.3.0.md`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_ROADMAP_DELTA_CANDIDATE_WORKING_v0.2.0.md` — preserved unchanged.
- **Source pressure tests:** Pass 4 and Pass 5 accepted; Pass 6 recorded in `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.6.0.md`.
- **Related records:** `ANL-EV-012`, `ANL-PT-005`, `ANL-PT-007`–`ANL-PT-021`, `ANL-GAP-001`, `ANL-UPD-001`.

---

## 1. Candidate purpose and supersession rule

This v0.3.0 successor preserves the accepted semantic intent of v0.2.0 and **supersedes only its incomplete exact edit-surface definition**.

The new evidence is full-text inspection of the exact current Roadmap predecessor. Two inherited whole-Domain statements in FP-005 and FP-017 would become false after the bounded FP-006 Research & Feedback activation unless narrowly refined.

Therefore:

```text
v0.2.0 semantic intent = PRESERVED / WORKING_LOCKED
v0.2.0 seven-location edit surface = SUPERSEDED
v0.3.0 nine-location edit surface = CURRENT WORKING CANDIDATE / PENDING HUMAN ACCEPTANCE
```

This file is not Roadmap authority and does not authorise implementation.

---

## 2. Exact predecessor discipline

The eventual v1.3.0 candidate must be assembled from the **current live** `05_ROADMAP_v1.2.0.md` bytes, not from an older PR-introduction blob bearing the same semantic version.

Current exact source lock:

```text
live main: 086ade7b28c000de1c387acb9760e5eb08bb0413
Roadmap path: docs/00_platform/05_ROADMAP_v1.2.0.md
git blob: 5432991071d4d1a7cbd9dc4c8fca48c823129f40
manifest SHA-256: 601172754e78f23df7d6b59e7c4eceb0aefa0b9e5bb65045dafeacd78b9d0fb0
```

The exact v1.2.0 current bytes must later be preserved byte-identically at `archive/05_ROADMAP_v1.2.0.md` when a governed successor is actually frozen.

---

## 3. Complete nine-location semantic patch contract

### 3.1 Header / successor lifecycle

If later frozen, create `05_ROADMAP_v1.3.0.md` with lifecycle metadata equivalent to:

```text
Document status: FROZEN / AMENDED ROADMAP v1.3.0
Document version: v1.3.0
Predecessor frozen version: archive/05_ROADMAP_v1.2.0.md
SemVer transition: v1.2.0 → v1.3.0
Last updated: 2026-10-10 (or actual promotion date if later)
```

Do not rewrite historical v1.1.x/v1.2.0 amendment-scope text. Add a new v1.3.0 amendment-scope section with meaning equivalent to:

> This semantic Roadmap successor explicitly activates one bounded Research & Feedback mode inside FP-006: the mandatory controlled-pilot value/relevance/price-value feedback instrument already required by Product Law. Research & Feedback owns the governed instrument/question version and participant-response lifecycle for that bounded mode; Analytics remains downstream measurement authority. FP-005 basic participant progress/usefulness feedback remains Habits, Journals & Progress truth where that purpose fits. Broader Research campaigns, studies, arbitrary instruments and generic survey capability remain future-gated / Feature-Pack-unassigned. No new Feature Pack, Product Law, Domain Law or Architecture decision is created. Implementation remains unauthorised.

### 3.2 §2 mature-capability Research & Feedback row

Replace only the current Research & Feedback row meaning with:

| Mature capability family | Approved outcome represented in this Roadmap |
|---|---|
| Research & Feedback | Bounded lightweight Research/Feedback and governed Research campaigns owned by Domain 19. The Product-Law-required FP-006 controlled-pilot value/relevance/price-value instrument is explicitly activated as a narrow MVP evidence mode. Its governed instrument/question version and participant response are Research & Feedback truth; Analytics owns downstream measurement only. FP-005 basic progress/usefulness feedback remains Habits, Journals & Progress truth where that purpose fits. All broader Research campaigns, studies, arbitrary instruments and generic survey capability remain **FUTURE-GATED / FEATURE-PACK-UNASSIGNED** and are not automatically assigned to FP-008, FP-009 or another pack. |

Voting & Balloting and all other rows remain unchanged.

### 3.3 §3.3 Domain/Feature-Pack challenge row

Replace only the `New Domains 19/20 require new Feature Packs` decision meaning with:

| Assumption challenged | Roadmap decision |
|---|---|
| New Domains 19/20 require new Feature Packs | Rejected. A Domain is not a Feature Pack. Research & Feedback is explicitly activated inside existing FP-006 only for the mandatory controlled-pilot value/relevance/price-value instrument; all broader Research capability remains future-gated / Feature-Pack-unassigned. Voting & Balloting remains fully future-gated / Feature-Pack-unassigned until a later governed Roadmap decision assigns an activating outcome. |

### 3.4 §3A future-gated capability block

Keep the general anti-silent-activation rule. Add the bounded exception:

> **Bounded FP-006 Research & Feedback activation:** Roadmap v1.3.0 is the governed activating decision for one narrow Domain-19 mode only: the Product-Law-required controlled-pilot value/relevance/price-value feedback instrument inside FP-006. This exception does not activate general Research campaigns, studies, arbitrary instruments, generic survey tooling or other Research modes.

Replace the Research & Feedback row meaning with:

| Capability | Domain / ownership | Status | Explicit boundary |
|---|---|---|---|
| Research & Feedback | Domain 19 — Research & Feedback | Bounded FP-006 activation; otherwise `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` | FP-006 activation is limited to the mandatory controlled-pilot value/relevance/price-value instrument. Not FP-005. Broader Research campaigns/studies/arbitrary instruments remain future-gated. No Research Feature Pack is created. |

Voting & Balloting remains unchanged.

Replace the current absolute no-present-blocker closing meaning with:

> Future-gated capability rows do not create automatic OQ blockers merely because the capability exists. The bounded FP-006 Research & Feedback activation creates no new OQ by Roadmap fiat; normal FP-006 Phase 7 gate-manifest/JIT adjudication must identify the minimum applicable Domain, Privacy, retention/deletion, proof and operational obligations before that instrument can be implemented. Future Voting and broader Research modes remain gated only when explicitly activated.

### 3.5 FP-005 feedback-classification guardrail — Pass-6 refinement

Replace the current whole-Domain future-gated sentence while preserving the HJP ownership guardrail. Use meaning equivalent to:

> **Feedback classification guardrail:** FP-005 “basic feedback” and daily/weekly progress entries are participant progress / self-tracking / usefulness evidence under `Habits, Journals & Progress` for the core plan loop. They do **not** activate Domain 19 Research & Feedback and are not reclassified by the bounded FP-006 Research activation. The only MVP Research & Feedback activation is the separately bounded FP-006 controlled-pilot value/relevance/price-value instrument; all broader Research capability remains `FUTURE-GATED / FEATURE-PACK-UNASSIGNED`. Plan/protocol calculations required by this outcome remain Plans & Nutrition authority (`calculation != authority` for Interactive Tools elsewhere).

No FP-005 Affected Domain, ownership or outcome changes.

### 3.6 FP-006 Affected Domains

Add `Research & Feedback` while preserving all current participants:

> **Affected Domains:** `Identity & Access`; `Privacy & Consent`; `Commerce`; `Entitlements`; `Temperament`; `Health Records`; `Safety & Eligibility`; `Plans & Nutrition`; `Content & Media`; `Communications`; `Research & Feedback`; `Analytics`; `Audit & Evidence`.

### 3.7 FP-006 bounded activation paragraph

Add after the paid-pilot evidence contract and before `Deferred From This FP`:

> **Bounded Research & Feedback activation:** FP-006 explicitly activates Research & Feedback only for the controlled-pilot value/relevance/price-value feedback instrument required by Product Law §§21T.5–21T.9. The governed instrument/question version and participant-submitted response lifecycle are Research & Feedback truth. Analytics may consume permitted projections and derive response rate, positive-value/relevance distributions, cohort comparisons and release evidence, but does not become participant-response authority. FP-005 basic daily/weekly progress/usefulness feedback remains Habits, Journals & Progress truth where its primary purpose is participant self-tracking/progress. This activation does not admit general Research campaigns/studies, arbitrary survey-builder capability or unrelated feedback modes into MVP. Exact participation identity/uniqueness mode, correction/withdrawal/de-link behaviour, privacy/retention requirements, provider choice, Resource/schema design and required JIT/proof work remain for normal FP-006 Phase 7 adjudication under current authority.

### 3.8 FP-006 deferred scope

Extend the existing deferral to include:

> broader Research campaigns/studies, arbitrary instruments and generic survey-builder capability beyond the mandatory bounded FP-006 pilot-feedback instrument

All current FP-006 deferrals remain intact.

### 3.9 FP-017 future-gated capability boundary — Pass-6 refinement

Replace the whole-Domain Feature-Pack-unassigned wording while preserving the FP-017 non-ownership guardrail. Use meaning equivalent to:

> **Future-gated capability boundary:** FP-017 does not automatically own Research & Feedback or Voting & Balloting. The bounded FP-006 Research & Feedback activation does not extend to FP-017. Broader Research capability and all Voting & Balloting remain Feature-Pack-unassigned unless a concrete approved product-space/market direction explicitly requires them and a later governed Roadmap decision assigns the required bounded mode.

No FP-017 Affected Domain, dependency, gate or release change.

---

## 4. Explicit non-changes

The refined patch contract leaves unchanged:

- Product-Law survey thresholds, denominator rules and fixed question wording;
- Decision Register semantics;
- Domain 19 ownership law;
- Architecture;
- FP-005 HJP ownership and Affected Domains;
- all 17 Feature Pack identifiers and dependency graph;
- Voting & Balloting fully future-gated status;
- FP-016 experimentation sequencing;
- FP-017 outcome/dependencies/Affected Domains;
- current FP-001 programme status and dossier requirements;
- identity/uniqueness/privacy/retention/provider/resource/event implementation details;
- proof classification until normal FP-006 Phase 7 adjudication;
- historical amendment summaries and archived authority evidence.

---

## 5. Authority-routing collateral contract — unchanged from v0.2.0

If and only if the exact Roadmap successor later passes freeze review, the governed promotion package must also:

1. route README from Roadmap v1.2.0 to v1.3.0;
2. route the manifest `ROADMAP` record to exact v1.3.0 path/SemVer/SHA-256 with `superseded_version: 1.2.0` and register the v1.2.0 historical archive according to repository convention;
3. create the then-current Open Work successor recording the Roadmap-level resolution without advancing FP-001, Phase 7C, proof classification or implementation;
4. preserve the then-current Open Work predecessor in archive;
5. reconcile the Delivery Atlas only as later derived/non-authoritative navigation.

Hashes must never be guessed before exact candidate bytes exist.

---

## 6. Freeze gate

Before `ANL-UPD-001` can be marked Roadmap-resolved:

1. human accepts the Pass-6 two-refinement correction;
2. recheck live `main` and the current authority route;
3. assemble exact v1.3.0 bytes from current v1.2.0 blob `5432991071d4d1a7cbd9dc4c8fca48c823129f40` plus only this nine-location patch;
4. preserve the exact current v1.2.0 predecessor byte-identically in archive;
5. compute real SHA-256 pins;
6. assemble matching README/manifest/Open Work candidate collateral against the then-current baseline;
7. verify the exact candidate diff contains no unrelated semantic drift;
8. obtain an independent exact-head review before PR/merge/promotion.

Until then:

```text
ANL-GAP-001 = UPSTREAM_ACTION_REQUIRED
ANL-UPD-001 = REFINED_PROMOTION_PATCH_CONTRACT_DRAFTED / PENDING HUMAN ACCEPTANCE
CURRENT ROADMAP = 05_ROADMAP_v1.2.0.md
FP-006 SURVEY JIT/IMPLEMENTATION = BLOCKED AT ROADMAP AUTHORITY
```
