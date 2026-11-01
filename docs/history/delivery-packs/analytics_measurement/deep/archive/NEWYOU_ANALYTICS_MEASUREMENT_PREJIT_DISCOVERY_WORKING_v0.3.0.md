# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.3.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 3 ONLY — FP-006 VALUE / RELEVANCE / PRICE-VALUE OWNERSHIP PRESSURE TEST
```

- **Prepared:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked for this pass:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Main drift since Pass 2:** NONE.
- **Pre-pass branch head:** `47d27edd6ba518ebf74271797ce80b2d7060c6fa`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.2.0.md` — preserved unchanged.
- **Purpose:** resolve only `ANL-EV-012`, the source-owner and sequencing semantics for the mandatory FP-006 value/relevance/price-value response.
- **Scope:** purpose/ownership/sequencing pressure test only. No metric formula, denominator implementation, survey vendor, Resource/schema design, event names, privacy/retention mechanics, dashboard, experiment design or implementation work.

---

## 1. Pass discipline

Pass 2 deliberately left one source-owner seam unresolved:

> `ANL-EV-012` — the durable participant response used for value, relevance and price-value evidence in FP-006.

This pass answers only:

1. what business meaning the mandatory FP-006 response has;
2. which Domain owns the durable participant-submitted truth;
3. whether current Roadmap sequencing permits that owner to be activated for FP-006;
4. whether an upstream working delta is required before downstream metric/JIT work can rely on the response.

This pass does **not** broaden Research & Feedback into a generic MVP capability and does **not** start a Research JIT Domain Dossier.

---

## 2. Current authority relevant to the seam

### 2.1 Product Law requires the evidence

Current Product Law §21T.5–§21T.7 requires the controlled paid pilot to collect and interpret participant-reported value/relevance evidence, including:

- a ≥70% positive value/relevance target;
- at least 70% survey response for controlled-pilot interpretation;
- visible non-response and counts alongside percentages;
- the separate question: `Considering what you paid, did the product provide good value?`;
- for discounted participants, a normal-list-price purchase-intent question whose stated intent is explicitly weaker evidence than an actual purchase.

This is therefore not optional future discovery. Some bounded feedback mechanism is required for FP-006 paid-pilot evidence.

### 2.2 Domain Law gives Research & Feedback a broad but purpose-bounded owner role

Current Domain Map §6.19 says Research & Feedback exists to own durable truth for **bounded lightweight feedback and governed Research activities**, including:

- campaign/study identity and declared purpose;
- participation identity/uniqueness contract;
- published instrument/question versions;
- participant submissions/responses;
- correction/withdrawal/de-link lifecycle;
- distinguishable staff annotation.

It is explicitly **not** a generic survey-builder, forms platform or shared evidence store. Its ownership is triggered by the approved purpose and durable meaning, not merely by rendering a survey widget.

### 2.3 Habits, Journals & Progress owns core-loop progress/self-tracking feedback where that meaning fits

Current Domain Map §6.9 owns participant behavioural/progress/self-tracking truth and lightweight programme check-in responses where that meaning genuinely belongs to the participant progress loop.

Roadmap FP-005 further makes an explicit classification guardrail: FP-005 `basic feedback` and daily/weekly progress entries are participant progress/self-tracking/usefulness evidence under Habits, Journals & Progress and do **not** activate Domain 19 Research & Feedback.

That guardrail is narrow. It does not turn Habits, Journals & Progress into a generic repository for any question labelled `feedback`.

### 2.4 Roadmap currently future-gates Domain 19

Current Roadmap §3A says Research & Feedback is:

```text
FUTURE-GATED / FEATURE-PACK-UNASSIGNED
```

and explicitly states that no Feature Pack may silently absorb the capability merely because a page, poll widget, challenge, **pilot survey** or tool surface could use it. It says Research & Feedback is not MVP, not FP-005 and not automatically FP-006.

The same Roadmap nevertheless requires the FP-006 paid-pilot survey evidence described above.

This is the seam under test.

---

## 3. Purpose classification test

The correct boundary is **purpose and durable meaning**, not wording or UI shape.

### 3.1 FP-005 core-loop feedback

Examples that remain naturally within Habits, Journals & Progress when captured as part of the participant's own core plan/progress loop include:

- `Was today's plan practical for you?`
- a bounded daily/weekly usefulness check tied to a participant progress entry;
- a lightweight reflection used as participant self-tracking rather than as a governed cohort study.

That meaning is participant progress/usefulness evidence. FP-005 already explicitly classifies it there.

### 3.2 FP-006 controlled-pilot value instrument

The mandatory FP-006 evidence has materially different meaning:

- it is interpreted at controlled-cohort level;
- the response rate itself is a release/evidence criterion;
- non-response must remain visible;
- the question meaning must remain stable enough for cohort comparison;
- price-value is explicitly separated from generic usefulness;
- discounted participants receive a distinct normal-list-price purchase-intent question;
- the responses inform proceed/iterate/repeat/pause decisions for the paid pilot.

This is not merely a participant's progress state. It is a bounded, version-sensitive feedback instrument used to learn from a defined cohort.

That purpose fits Domain 19's frozen definition of **bounded lightweight feedback** more directly than it fits Habits, Journals & Progress.

### 3.3 Conclusion

The mandatory FP-006 controlled-pilot value/relevance/price-value instrument should be treated as **Research & Feedback source truth**, while Analytics remains downstream and derives response-rate/value aggregates.

This does **not** reclassify ordinary FP-005 progress/basic-feedback records. The two meanings remain distinct.

---

## 4. Pressure-test records

### ANL-PT-001 — Put the whole FP-006 survey under Habits, Journals & Progress

**Measurement question:** Can the required FP-006 value/relevance/price-value survey simply reuse the FP-005 basic-feedback ownership rule?

**Authority/source Domains:** Product Law §21T; Domain Map §§6.9 and 6.19; Roadmap §3A, FP-005, FP-006.

**Scenario:** A participant is asked a versioned controlled-pilot set of value/relevance questions after paid use, including the required price-value question and, when discounted, normal-list-price purchase intent.

**Invariants:**

- every durable business truth has one owner;
- purpose determines ownership;
- HJP must not become a generic feedback bucket;
- Domain 19's bounded-feedback ownership cannot be bypassed by naming a survey a progress check-in.

**Measurement failure:** Treating all responses as HJP would stretch participant progress/self-tracking authority into commercial/product-learning feedback whose primary meaning is cohort evidence.

**Privacy:** This route would not remove privacy obligations; it would only obscure the true purpose classification.

**Adversarial variants:** Price-value and hypothetical full-price purchase intent are especially weak fits for participant progress truth.

**Analysis:** FP-005's explicit basic-feedback carve-out is real but narrow. It protects the core participant loop. It cannot safely carry the entire FP-006 controlled-pilot instrument merely because both contain questions.

**Disposition:** `CONFLICT`.

**Proof route:** Authority interpretation only; no implementation proof can repair an ownership mismatch.

---

### ANL-PT-002 — Let Analytics own the participant survey response

**Measurement question:** Can Analytics persist the response as its own governed analytical fact and thereby avoid Domain 19 activation?

**Authority/source Domains:** Analytics §6.17; Research & Feedback §6.19.

**Scenario:** Analytics stores `useful=yes`, `good_value=yes`, and `would_buy_full_price=no` as analytical event facts and treats those rows as the canonical survey response.

**Invariants:**

- Analytics does not become hidden business authority;
- participant Research/feedback responses are explicitly excluded from Analytics ownership;
- analytical projections must remain downstream/rebuildable.

**Measurement failure:** Analytics becomes the only durable source for participant-submitted feedback truth and therefore a shadow Research owner.

**Privacy:** Consolidating participant feedback into Analytics also increases linkage/disclosure risk without solving lifecycle ownership.

**Analysis:** Analytics may ingest a permitted projection or minimum fact for measurement, but it may not own the canonical participant response.

**Disposition:** `CONFLICT`.

**Proof route:** Not applicable; prohibited ownership shape.

---

### ANL-PT-003 — Treat an external survey/provider as source authority

**Measurement question:** Could a survey SaaS, email provider or spreadsheet be the source of truth for the pilot responses?

**Authority/source Domains:** Research & Feedback; Analytics; external-provider evidence doctrine.

**Scenario:** A third-party survey link collects answers and the exported CSV is used directly to decide whether the pilot passed.

**Invariants:**

- provider state is evidence, not platform business authority;
- cohort membership, response meaning/version and correction/deletion handling remain governed;
- external reports cannot silently define NewYou business truth.

**Measurement failure:** Provider-specific rows become the ungoverned canonical response, making reproducibility, correction, deletion and cohort interpretation dependent on external state.

**Privacy:** Processor/deletion/export obligations would still need explicit treatment in the later privacy pass.

**Analysis:** A provider can collect or transmit evidence behind an adapter/contract. It does not replace the owning Domain.

**Disposition:** `CONFLICT`.

**Proof route:** Later provider proof may show reliable collection, never business ownership.

---

### ANL-PT-004 — Split the same pilot survey across HJP and Research by question

**Measurement question:** Could usefulness/relevance answers belong to HJP while price-value answers belong to Research & Feedback inside one governed pilot instrument?

**Authority/source Domains:** HJP §6.9; Research & Feedback §6.19.

**Scenario:** One participant submits one survey screen. Some answers are persisted as progress truth and others as Research responses solely to avoid activating Domain 19 for the whole instrument.

**Invariants:**

- ownership follows genuine independent business meaning;
- UI composition does not create or merge authority;
- avoid shared-write or fragmented lifecycle for one logical record without evidence.

**Measurement failure:** One instrument gains two correction/withdrawal/version lifecycles and ambiguous response completeness. A retry could partially succeed across owners and manufacture inconsistent survey state.

**Privacy:** Split ownership also complicates deletion/export and response withdrawal for no current benefit.

**Analysis:** Separate feedback mechanisms may legitimately have different owners when their purposes are independently real. But splitting a single FP-006 controlled-pilot instrument by question purely to route around Roadmap activation is unjustified complexity.

**Disposition:** `PASS_WITH_REFINEMENT` only for **genuinely separate mechanisms/purposes**; `CONFLICT` as a workaround for the mandatory FP-006 instrument.

**Proof route:** Purpose classification at JIT; no generic mixed-owner survey primitive.

---

### ANL-PT-005 — Explicitly activate a bounded Research & Feedback mode inside FP-006

**Measurement question:** Can current law support the mandatory pilot feedback cleanly if Roadmap explicitly activates only the required Domain 19 slice in FP-006?

**Authority/source Domains:** Product Law §21T; Domain Map §6.19; Roadmap §3A and FP-006.

**Scenario:** FP-006 activates only the minimum participant-feedback capability necessary to collect/version the required controlled-pilot value/relevance/price-value responses. Broader Research campaigns/studies remain future-gated.

**Invariants:**

- no new Feature Pack merely because a Domain exists;
- Product Law's mandatory pilot evidence is implemented by its rightful owner;
- Research & Feedback owns response/instrument truth;
- Analytics derives measurement only;
- broader Research capability remains out of MVP.

**Measurement failure:** None inherent. The material current defect is sequencing authority, not Domain ownership.

**Privacy:** Exact identity mode, deletion/withdrawal and retention remain later dedicated work; this pressure test does not guess them.

**Analysis:** This is the smallest coherent correction. Domain Law already supplies the owner and Product Law already supplies the requirement. Only the Roadmap's activation statement prevents the required owner from participating in FP-006.

**Disposition:** `NEEDS_WORKING_DELTA`.

**Proof route:** Roadmap amendment first; later FP-006 Phase 7 determines exact JIT dossier/gate/proof obligations. This pass does not start them.

---

### ANL-PT-006 — Pull general Research capability into MVP because FP-006 needs one survey

**Measurement question:** Does resolving the FP-006 survey require activating generic Research campaigns/studies across the MVP?

**Authority/source Domains:** Roadmap §3A; Research & Feedback §6.19.

**Scenario:** The platform builds a reusable survey/research subsystem, campaign administration, arbitrary instruments and general study workflows before the first paid pilot.

**Invariants:**

- solve only the approved outcome;
- Domain existence does not justify generic infrastructure;
- future capability remains future-gated unless required;
- authority ≠ acceleration.

**Measurement failure:** Scope inflation delays the paid pilot and creates unrequired product/operational surface.

**Privacy:** Broader research modes introduce additional identity/retention/anonymity obligations prematurely.

**Analysis:** The required correction is a **bounded FP-006 activation**, not a generic Research product.

**Disposition:** `CONFLICT`.

**Proof route:** None; explicitly defer broader capability.

---

## 5. Gap and smallest safe upstream delta

### ANL-GAP-001 — FP-006 requires feedback whose rightful Domain is Roadmap-future-gated

**Classification:** `ROADMAP SEQUENCING / ACTIVATION GAP`.

**Conflict:**

1. Product Law requires a controlled-pilot value/relevance survey, response-rate evidence and price-value question before/through FP-006.
2. Domain Law assigns bounded lightweight feedback campaign/instrument/participant-response truth to Research & Feedback when that is the response's purpose.
3. The mandatory FP-006 controlled-pilot instrument has that purpose; the price-value/full-price-intent questions cannot honestly be treated as participant progress truth.
4. Roadmap §3A keeps Research & Feedback future-gated, Feature-Pack-unassigned and not automatically FP-006, while expressly warning against silent activation merely because a pilot survey exists.

**Why this is material:** Without correction, downstream work must either violate Domain ownership, violate Roadmap sequencing, or leave a mandatory Product-Law pilot criterion without a lawful source owner.

**Disposition:** `CONFLICT`.

**Implementation effect:** **STOP** for implementation/JIT specification of the FP-006 controlled-pilot value instrument until the Roadmap activation seam is explicitly resolved. Other unrelated Analytics Pre-JIT questions are not declared invalid, but this stream should not pretend the survey contract is implementation-ready.

---

### ANL-UPD-001 — Proposed minimal Roadmap amendment for bounded FP-006 Research & Feedback activation

**Target authority level:** Roadmap only.

**No Product Law amendment required:** Product Law already requires the evidence.

**No Domain Law amendment required:** Domain Law already provides the correct owner and boundary.

**Proposed Roadmap change intent:**

1. Amend §3A so Research & Feedback remains generally `FUTURE-GATED / FEATURE-PACK-UNASSIGNED`, **except** for an explicit bounded FP-006 activation limited to the mandatory controlled-pilot value/relevance/price-value feedback instrument required by Product Law §21T.
2. Add **Research & Feedback** to FP-006 Affected Domains for that bounded mode.
3. Clarify inside FP-006 that:
   - the governed instrument/question version and participant response are Research & Feedback truth;
   - Analytics owns only derived response-rate/distribution/release measurement;
   - FP-005 basic progress/usefulness feedback remains Habits, Journals & Progress truth and is not reclassified wholesale;
   - broader Research studies/campaigns, arbitrary survey-builder capability and general-purpose Research activation remain future-gated.
4. Do not create a new Feature Pack merely for this activation.
5. Let normal FP-006 Phase 7 gate-manifest/JIT adjudication decide the exact minimum Research dossier/proof work before implementation; this Pre-JIT pass does not decide Resource/schema/provider mechanics.

**Disposition:** `NEEDS_WORKING_DELTA`.

**Required before:** final implementation-authorising FP-006 contract for the controlled-pilot survey path and first paid participation relying on that evidence.

**Not authorised by this record:** editing Roadmap authority, starting the Research JIT Domain Dossier, choosing a survey vendor or implementing collection.

---

## 6. Resolution of ANL-EV-012

`ANL-EV-012` is refined as follows:

**Measurement question:** What did the participant report about usefulness/relevance and the value received for what they paid?

**Source owner for the mandatory FP-006 controlled-pilot instrument:** **Research & Feedback** — `S1_SOURCE_DOMAIN_AUTHORITY`, once the bounded FP-006 Roadmap activation is explicitly authorised.

**Analytics role:** Derived response-rate, positive-value/relevance distributions, cohort comparisons and release evidence only.

**HJP boundary:** FP-005 daily/weekly/basic progress feedback remains Habits, Journals & Progress when its primary meaning is participant self-tracking/progress/usefulness in the core loop. It does not become Research merely because it contains a question.

**Current readiness:** `SOURCE OWNER RESOLVED / ROADMAP ACTIVATION BLOCKED`.

The Pass-2 `S5_SOURCE_AUTHORITY_UNRESOLVED` status is therefore superseded by this more precise state; the predecessor remains preserved as provenance.

---

## 7. Explicit non-decisions

Pass 3 does not define:

- exact survey questions beyond wording already fixed by Product Law;
- response scales;
- numerator/denominator formulas;
- measurement windows;
- anonymous versus Account-linked response identity mode;
- uniqueness/deduplication contract;
- correction/withdrawal UX;
- retention or deletion durations;
- small-cohort disclosure/suppression;
- survey delivery channel/vendor;
- Resources/tables/Ash actions;
- event names/payloads;
- dashboards;
- experimentation.

Those remain downstream and may not be inferred from this ownership result.

---

## 8. Pass 3 disposition

**NEEDS_WORKING_DELTA — SOURCE OWNERSHIP RESOLVED; ROADMAP ACTIVATION CONFLICT IDENTIFIED.**

The durable source owner for the mandatory FP-006 controlled-pilot value/relevance/price-value instrument is Research & Feedback, not Analytics and not a stretched generic HJP feedback bucket. Current Product Law and Domain Law are coherent on requirement and ownership, but current Roadmap sequencing does not explicitly activate that owner for FP-006 and explicitly forbids silent activation.

The smallest safe repair is `ANL-UPD-001`: a narrow Roadmap amendment that activates only the mandatory FP-006 pilot-feedback mode while leaving broader Research & Feedback future-gated.

Per governance doctrine, this Pre-JIT stream stops at that authority boundary. It does not rewrite Roadmap law inside a downstream Analytics artifact.
