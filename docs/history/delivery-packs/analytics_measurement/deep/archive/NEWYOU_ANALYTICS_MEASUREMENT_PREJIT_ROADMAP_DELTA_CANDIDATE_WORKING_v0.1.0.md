# NewYou Analytics & Measurement Pre-JIT — ANL-UPD-001 Roadmap Delta Candidate Working v0.1.0

```text
WORKING / NON-AUTHORITATIVE
ROADMAP AMENDMENT CANDIDATE ONLY
DO NOT TREAT AS CURRENT ROADMAP
IMPLEMENTATION NOT AUTHORISED
```

- **Prepared:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Current Roadmap authority under review:** `05_ROADMAP_v1.2.0.md`
- **Live-main baseline:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Source pressure test:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.4.0.md`
- **Related records:** `ANL-EV-012`, `ANL-PT-005`, `ANL-PT-007`–`ANL-PT-012`, `ANL-GAP-001`, `ANL-UPD-001`.

---

## 1. Candidate intent

Resolve the current Roadmap sequencing conflict by explicitly activating **Research & Feedback** inside existing `FP-006` only for the Product-Law-required controlled-pilot value/relevance/price-value feedback instrument.

This candidate does not change the requirement, ownership or architecture. It only makes Roadmap sequencing agree with existing Product and Domain Law.

If accepted and promoted, the semantic change should be a minor Roadmap successor (expected `v1.3.0`). Exact promotion metadata/date/routing must be produced by the governed authority-promotion step, not by this candidate.

---

## 2. Proposed amendment scope text

Add a successor amendment-scope section with meaning equivalent to:

> This semantic Roadmap successor explicitly activates one bounded Research & Feedback mode inside FP-006: the mandatory controlled-pilot value/relevance/price-value feedback instrument already required by Product Law. Research & Feedback owns the governed instrument/question version and participant response lifecycle for that bounded mode; Analytics remains downstream measurement authority. FP-005 basic participant progress/usefulness feedback remains Habits, Journals & Progress truth where that purpose fits. Broader Research campaigns, studies, arbitrary instruments and generic survey capability remain future-gated / Feature-Pack-unassigned. No new Feature Pack is created. Product Law, Architecture Law and Domain Law are unchanged. Implementation remains unauthorised.

---

## 3. Proposed §2 mature-capability row replacement

Replace the current Research & Feedback row meaning with:

| Mature capability family | Approved outcome represented in this Roadmap |
|---|---|
| Research & Feedback | Bounded lightweight Research/Feedback and governed Research campaigns owned by Domain 19. The Product-Law-required FP-006 controlled-pilot value/relevance/price-value instrument is explicitly activated as a narrow MVP evidence mode. Its governed instrument/question version and participant response are Research & Feedback truth; Analytics owns only downstream measurement. FP-005 basic progress/usefulness feedback remains Habits, Journals & Progress truth where that purpose fits. All broader Research campaigns/studies/arbitrary survey capability remain **FUTURE-GATED / FEATURE-PACK-UNASSIGNED** and are not automatically assigned to FP-008, FP-009 or any other pack. |

Rationale: the current absolute “Not MVP / not automatically FP-006” wording would contradict the explicit bounded activation.

---

## 4. Proposed §3.3 dependency-challenge row replacement

Replace the current `New Domains 19/20 require new Feature Packs` decision meaning with:

| Assumption challenged | Roadmap decision |
|---|---|
| New Domains 19/20 require new Feature Packs | Rejected. A Domain is not a Feature Pack. Research & Feedback is explicitly activated only inside FP-006 for the mandatory controlled-pilot value/relevance/price-value instrument; all broader Research capability remains future-gated / Feature-Pack-unassigned. Voting & Balloting remains fully future-gated / Feature-Pack-unassigned until a later governed Roadmap decision assigns an activating outcome. |

---

## 5. Proposed §3A future-gated rule refinement

Preserve the general activation rule, then add a narrow exception statement equivalent to:

> **Bounded FP-006 Research & Feedback activation:** This Roadmap successor is the governed activating decision for one narrow Domain-19 mode only: the Product-Law-required controlled-pilot value/relevance/price-value feedback instrument inside FP-006. This exception does not activate general Research campaigns/studies, arbitrary survey tooling or other Research modes.

Replace the Research & Feedback table row meaning with:

| Capability | Domain / ownership | Status | Explicit boundary |
|---|---|---|---|
| Research & Feedback | Domain 19 — Research & Feedback | `BOUNDED FP-006 ACTIVATION; OTHERWISE FUTURE-GATED / FEATURE-PACK-UNASSIGNED` | FP-006 activation is limited to the mandatory controlled-pilot value/relevance/price-value instrument. Not FP-005. Broader Research campaigns/studies/arbitrary instruments remain future-gated. No Research Feature Pack is created. |

Voting & Balloting remains unchanged.

The literal status label above is candidate wording, not a pre-existing governed identifier; the final authority review may choose equivalent prose if preferred.

---

## 6. Proposed FP-006 Affected Domains refinement

Change the FP-006 Affected Domains list to add `Research & Feedback` while preserving all current Domains:

> **Affected Domains:** `Identity & Access`; `Privacy & Consent`; `Commerce`; `Entitlements`; `Temperament`; `Health Records`; `Safety & Eligibility`; `Plans & Nutrition`; `Content & Media`; `Communications`; `Research & Feedback`; `Analytics`; `Audit & Evidence`.

No Domain ownership changes are implied; this only sequences the already-owning Domain into the pack.

---

## 7. Proposed FP-006 bounded activation paragraph

Add immediately after the paid-pilot evidence contract, before `Deferred From This FP`, wording equivalent to:

> **Bounded Research & Feedback activation:** FP-006 explicitly activates Research & Feedback only for the controlled-pilot value/relevance/price-value feedback instrument required by Product Law §§21T.5–21T.9. The governed instrument/question version and participant-submitted response lifecycle are Research & Feedback truth. Analytics may consume permitted projections and derive response rate, positive-value/relevance distributions, cohort comparisons and release evidence, but does not become response authority. FP-005 basic daily/weekly progress/usefulness feedback remains Habits, Journals & Progress truth where its primary purpose is participant self-tracking/progress. This activation does not admit general Research campaigns/studies, arbitrary survey-builder capability or unrelated feedback modes into MVP. Exact participation identity/uniqueness mode, correction/withdrawal/de-link behaviour, privacy/retention requirements, provider choice, Resource/schema design and required JIT/proof work remain for normal FP-006 Phase 7 adjudication under current authority.

---

## 8. Proposed FP-006 deferred-scope refinement

Extend `Deferred From This FP` so it explicitly includes:

> ... broader Research campaigns/studies, arbitrary instruments and generic survey-builder capability beyond the mandatory bounded FP-006 pilot-feedback instrument ...

This prevents the bounded exception from being interpreted as a general Domain-19 MVP activation.

---

## 9. Explicit non-changes

The candidate leaves unchanged:

- Product-Law survey thresholds, meanings and question wording;
- Domain 19 ownership law;
- FP-005 HJP basic-feedback guardrail;
- the 17 Feature Pack identifiers and dependency graph;
- Voting & Balloting future-gated status;
- FP-016 experimentation sequencing;
- all implementation/resource/provider choices;
- all privacy/retention/identity-mode details not already fixed upstream;
- proof classification until normal Phase 7 adjudication.

---

## 10. Promotion boundary

This file is **not** the Roadmap amendment.

If later accepted for authority promotion, the semantic successor must be created through normal governance and must also update normal current-authority routing/status artifacts as required at that time (for example README/authority manifest routing and current programme bookkeeping). Those collateral updates route the new Roadmap authority; they do not create additional Product or Domain semantics.

Until that governed promotion occurs:

```text
ANL-GAP-001 = OPEN / UPSTREAM_ACTION_REQUIRED
ANL-UPD-001 = CANDIDATE_DRAFTED / UPSTREAM_ACTION_REQUIRED
FP-006 SURVEY JIT/IMPLEMENTATION = BLOCKED AT ROADMAP AUTHORITY
```
