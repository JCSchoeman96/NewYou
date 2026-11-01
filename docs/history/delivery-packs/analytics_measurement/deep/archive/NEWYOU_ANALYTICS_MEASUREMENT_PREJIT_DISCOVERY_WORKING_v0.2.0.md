# NewYou Analytics & Measurement Pre-JIT Discovery — Working v0.2.0

```text
WORKING / NON-AUTHORITATIVE
IMPLEMENTATION NOT AUTHORISED
PASS 2 ONLY — MEASUREMENT-QUESTION / SOURCE-TRUTH MAP
```

- **Prepared:** 2026-10-09
- **Repository:** `JCSchoeman96/NewYou`
- **Branch:** `prejit/analytics-measurement`
- **Live-main baseline rechecked for this pass:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Main drift since Pass 1:** NONE.
- **Pre-pass branch head:** `84f654fc0b99f0cbcd36faa31f0c9708047f3eda`
- **Direct predecessor:** `NEWYOU_ANALYTICS_MEASUREMENT_PREJIT_DISCOVERY_WORKING_v0.1.0.md` — preserved unchanged.
- **Purpose:** establish which product/paid-pilot questions must be answered and identify the authoritative source truth, governed analytical fact, best-effort observation or external evidence behind each question.
- **Scope of this version:** source-truth classification only. No metric formula set, denominator implementation, event catalogue, schema, collection payload, attribution model, privacy/retention design, vendor selection, experimentation design, dashboard design or implementation work.

---

## 1. Pass discipline and source classes

This pass starts with measurement questions and authority, **not event names**.

`ANL-EV-*` in this file means **measurement evidence / source-truth record**. It is not an analytics event-name catalogue and does not authorise implementation.

The following source classes are used:

| Class | Meaning |
|---|---|
| `S1_SOURCE_DOMAIN_AUTHORITY` | Durable business truth owned by the relevant non-Analytics Domain. Analytics may consume/derive from it but may not replace it. |
| `S2_ANALYTICS_GOVERNED_FACT` | A permitted first-party analytical/acquisition/operational fact owned by Analytics because it is measurement evidence rather than business authority. |
| `S3_BEST_EFFORT_OBSERVATION` | Behavioural/client observation that may be missing, duplicated, delayed or reordered and must not manufacture business success. |
| `S4_EXTERNAL_EVIDENCE` | Provider/platform/offline evidence that may inform analysis or reconciliation but is not NewYou authoritative business truth by itself. |
| `S5_SOURCE_AUTHORITY_UNRESOLVED` | Current authority does not yet safely classify the durable source meaning. This must be resolved before Analytics can treat it as governed fact. |

A single measurement question may combine several classes. The correct answer is not to force all evidence into one Analytics event stream.

---

## 2. Governing ownership constraints carried forward from Pass 1

Current Domain Law remains controlling:

- **Commerce** owns purchase, payment, refund, dispute and settlement/reconciliation truth.
- **Entitlements** owns access grants, provenance, consumption, expiry and revocation.
- **Temperament** owns assessment attempts, saved/submitted answers, immutable result/report provenance and self/book/digital provenance.
- **Health Records** owns progressively collected health/lifestyle facts and provenance.
- **Safety & Eligibility** owns eligibility outcomes, safety restrictions and current pathway authority.
- **Plans & Nutrition** owns plan generation/delivery/version/provenance and plan lifecycle/activation state.
- **Habits, Journals & Progress** owns participant behavioural/progress/check-in truth that fits that Domain; private journal text is excluded from Analytics by default.
- **Communications** owns message intent/delivery attempt/provider evidence, but provider open/click observations do not establish business conversion.
- **Audit & Evidence** owns cross-cutting audit/security/incident evidence but never the underlying business transition.
- **Research & Feedback** owns governed Research/feedback campaign/instrument/participant-response truth when the purpose genuinely falls in that Domain.
- **Analytics** owns permitted analytical observations/facts, acquisition evidence, operational analytical facts, derived projections/aggregates and attribution interpretations while remaining downstream of source Domains.

The Platform Operating Model additionally establishes that operator **Work is attention, not authority**: there is no universal `Task` Resource or universal support-work lifecycle. Support/admin presentation cannot silently create a new owner.

---

## 3. FP-006 measurement-question / source-truth register

### ANL-EV-001 — Paid-pilot cohort qualification and context

**Measurement question:** Are the first-10 / toward-25 / maximum-50 participants the intended genuine paid pilot cohort, and what context is known about that cohort without claiming representativeness?

**Required source truth/evidence:**

- verified actual payment, product, accepted/list price, promotion and amount paid → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- current eligibility outcome → **Safety & Eligibility** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- temperament provenance/current eligible profile where applicable → **Temperament** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- adult/account qualification and language/profile source where captured under the current identity/account contract → **Identity & Access** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- acquisition source, book exposure, prior Lynette/NewYou familiarity and other pilot-recruitment context → **Analytics acquisition evidence** when explicitly captured as measurement evidence — `S2_ANALYTICS_GOVERNED_FACT`;
- offline recruiter notes, event/media records or third-party source evidence not yet represented as first-party governed evidence → `S4_EXTERNAL_EVIDENCE` until deliberately admitted under a governed analytical contract.

**Boundary:** The Product Law criterion that the pilot consists of real adult women in the approved audience does not justify turning sex/gender, book exposure or familiarity into permanent Identity business truth merely for segmentation. Where such attributes are needed only to evidence the bounded pilot cohort, they may be analytical cohort evidence subject to the later privacy/minimisation pass. Collection basis and retention are deliberately not decided here.

**Pass-2 result:** `SOURCE ROUTE RESOLVED` at the authority-class level. No new Domain is justified.

---

### ANL-EV-002 — Acquisition, invitation/exposure and channel path

**Measurement question:** How did a participant encounter the offer, and which acquisition path ultimately led to an authoritative purchase?

**Required source truth/evidence:**

- page views, referrers, UTM-like campaign observations, client-side clicks and anonymous browsing → `S3_BEST_EFFORT_OBSERVATION` unless a stronger first-party fact exists;
- platform-created invitation/message intent and delivery attempt → **Communications** — `S1_SOURCE_DOMAIN_AUTHORITY` for communication delivery state only;
- provider open/click reports → `S4_EXTERNAL_EVIDENCE` and never purchase/conversion authority;
- book/event/media/offline recruitment provenance explicitly collected for pilot analysis → **Analytics acquisition evidence** — `S2_ANALYTICS_GOVERNED_FACT`;
- purchase/payment outcome → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- attribution interpretation joining acquisition evidence to later purchase → **Analytics** — `S2_ANALYTICS_GOVERNED_FACT` / derived analytical interpretation.

**Boundary:** Attribution is interpretation, not causal proof. Client/provider telemetry may support acquisition analysis but cannot create payment or entitlement truth.

**Pilot/public distinction:** Deliberately invited first-pilot conversion is not ordinary visitor-to-purchase conversion. Ordinary funnel/channel economics begin at limited-public release under Product/Roadmap law.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-003 — Checkout, payment attempt and verified paid state

**Measurement question:** Did an eligible participant begin the commercial path, attempt payment and reach verified paid truth?

**Required source truth/evidence:**

- purchase/order/checkout intent where represented as a durable commercial transition → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- payment attempt/transaction state → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- verified paid/refunded/disputed/reconciled state → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- gateway/browser return/webhook/provider state before Commerce reconciliation → `S4_EXTERNAL_EVIDENCE`;
- UI-only checkout-button clicks with no durable commercial state → `S3_BEST_EFFORT_OBSERVATION`.

**Boundary:** A browser or provider assertion cannot be promoted directly into paid-demand evidence. Analytics derives commercial funnel facts from Commerce state where authoritative state exists.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-004 — Entitlement fulfilment and access consequence

**Measurement question:** Did a verified commercial consequence result in exactly the correct current access right?

**Required source truth/evidence:**

- entitlement grant/scope/source/provenance/consumption/revocation → **Entitlements** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- payment state that caused a grant/revoke intent → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- Analytics fulfilment/duplicate-rate measurements → derived from those source facts.

**Boundary:** Payment success is not entitlement truth. Analytics must preserve this distinction rather than infer access directly from payment telemetry.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-005 — Assessment start, submission and governed result

**Measurement question:** Did a participant genuinely start and complete the governed assessment?

**Required source truth/evidence:**

- attempt lifecycle, first persisted/submitted answer, saved/resumed state and submitted answers → **Temperament** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- valid calculated result/report provenance → **Temperament** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- page-load/button-click telemetry → `S3_BEST_EFFORT_OBSERVATION` and not required where the authoritative attempt state exists.

**Boundary:** Product Law already defines the starter as the first answer persisted/submitted and completion as valid submission plus governed result. Analytics should derive the metric from Temperament authority rather than invent an independent completion event.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-006 — Health onboarding and sufficient facts for deterministic eligibility

**Measurement question:** Did a paid personalised-plan-pathway participant reach required onboarding and provide sufficient facts for deterministic eligibility?

**Required source truth/evidence:**

- progressively collected health/lifestyle intake facts and provenance → **Health Records** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- current deterministic eligibility outcome → **Safety & Eligibility** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- paid/personalised-plan commercial/access context used to identify the applicable population → **Commerce / Entitlements** — `S1_SOURCE_DOMAIN_AUTHORITY` as applicable;
- Analytics completion/coverage readout → derived analytical fact.

**Boundary:** Assessment-only customers are excluded by Product Law. Analytics does not create a second notion of health completeness independent of the governed Health/Safety pathway.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`; exact metric contract remains a later pass.

---

### ANL-EV-007 — Safety/eligibility pathway outcome

**Measurement question:** Which governed pathway did the participant receive, and how should that pathway appear in pilot evidence?

**Required source truth/evidence:**

- `eligible_automated`, `general_wellness_only`, `professional_review_required` and `insufficient_information` outcome → **Safety & Eligibility** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- supporting health facts → **Health Records** — `S1_SOURCE_DOMAIN_AUTHORITY` but not copied wholesale into Analytics;
- analytical cohort/pathway counts → **Analytics** derived from the current/historical governed outcome facts required by the metric contract.

**Boundary:** A correct `general_wellness_only` outcome is not a failed personalised-plan activation. Analytics must preserve the Product Law pathway distinction rather than flatten all non-personalised outcomes into failure.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-008 — Plan generation, successful delivery and paid-plan fulfilment

**Measurement question:** Was the governed plan outcome generated/delivered correctly and reproducibly, and did the paid right transition correctly?

**Required source truth/evidence:**

- generation request/outcome, immutable delivered plan/version/provenance and reproducibility context → **Plans & Nutrition** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- current paid-plan entitlement/consumption state → **Entitlements** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- refund/closeout where delivery cannot lawfully fulfil the commercial component → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- notification that a plan is ready → **Communications** source truth for delivery state only, not plan-delivery success.

**Boundary:** Generation, notification and entitlement are distinct facts. Analytics may correlate them but may not collapse them into one synthetic authority.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-009 — Plan activation

**Measurement question:** Did a participant take a genuine qualifying action after successful personalised-plan delivery?

**Required source truth/evidence:**

- plan lifecycle/activation state → **Plans & Nutrition** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- participant progress/action evidence used by the owning workflow where appropriate → **Habits, Journals & Progress** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- simple plan-open/read observation, if separately collected → `S3_BEST_EFFORT_OBSERVATION` unless the owning Domain deliberately records it as a durable business fact.

**Boundary:** Product Law says generation, notification or a single plan open alone does not establish activation. Since Domain Law already assigns plan activation state to Plans, Analytics should consume the governed activation truth rather than invent its own activation state from clicks.

**Pass-2 result:** `SOURCE ROUTE RESOLVED` at ownership level. The exact qualifying-action contract belongs to the later metric/JIT pass.

---

### ANL-EV-010 — Meaningful seven-day use

**Measurement question:** Is there evidence of meaningful engagement on the required distinct days after delivery?

**Required source truth/evidence:**

- durable participant habit/progress/check-in/adherence facts that fit the core plan loop → **Habits, Journals & Progress** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- successful plan delivery/date anchor → **Plans & Nutrition** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- content/read/open interactions that are not business state → `S3_BEST_EFFORT_OBSERVATION` where permitted;
- distinct-day usage result → **Analytics** derived analytical fact.

**Boundary:** Product Law fixes the three-distinct-days / first-seven-days / at-least-one-after-Day-1 meaning, but this pass does **not** define the complete qualifying-action set. Raw journal text must not be required for usage measurement.

**Pass-2 result:** `SOURCE ROUTE PARTIALLY RESOLVED`; owner classes are clear, qualifying engagement semantics remain for the metric-contract pass.

---

### ANL-EV-011 — Purchased library availability versus actual use

**Measurement question:** Could the participant correctly access purchased report/plan artifacts, and did they actually use/view them?

**Required source truth/evidence:**

- current right to access → **Entitlements** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- assessment report artifact/provenance → **Temperament** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- delivered plan artifact/provenance → **Plans & Nutrition** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- governed content version where applicable → **Content & Media** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- actual read/open/navigation observations → ordinarily `S3_BEST_EFFORT_OBSERVATION` unless a specific owning Domain defines a durable business transition.

**Boundary:** “Access was correctly available” and “participant viewed/used it” are different questions. The first can be proved from business authority; the second may depend on fallible behavioural observation.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-012 — Value, relevance and price-value response

**Measurement question:** What did the participant report about usefulness/relevance and the value received for what they paid?

**Current authority collision/seam:**

- FP-005 explicitly classifies its **basic feedback** and daily/weekly progress entries as **Habits, Journals & Progress** truth and explicitly says this does not activate Domain 19 Research & Feedback;
- Domain Law says a persisted response belongs to **Research & Feedback** when its purpose genuinely classifies it as Research/feedback campaign/instrument truth;
- the Roadmap says Research & Feedback is `FUTURE-GATED / FEATURE-PACK-UNASSIGNED` and no Feature Pack may silently absorb it merely because a **pilot survey** exists;
- FP-006 nevertheless requires value/relevance survey evidence, a minimum response rate for controlled-pilot interpretation and a specific price-value question.

**Boundary:** Analytics may derive response rates and value distributions, but **Analytics must not own the participant-submitted response merely to avoid the ownership question**.

**Pass-2 result:** `S5_SOURCE_AUTHORITY_UNRESOLVED` for the durable participant value-response record. This pass does not decide whether the required FP-006 response is:

1. bounded FP-005/product-loop basic feedback owned by Habits, Journals & Progress; or
2. a governed Research & Feedback instrument requiring explicit Roadmap activation/amendment.

This remains the only material source-owner seam identified by this pass. It is not yet promoted to `ANL-GAP-*` because it requires its own focused purpose/ownership pressure test.

---

### ANL-EV-013 — Refund truth and dissatisfaction classification

**Measurement question:** How many refunds occurred, why did they occur, and which categories are commercial-dissatisfaction signals versus safety/technical corrections?

**Required source truth/evidence:**

- refund/payment/dispute state → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- Product-Law refund reason classification recorded with the refund/closeout → **Commerce** as commercial refund truth, with references to source evidence where needed;
- safety/eligibility reason evidence → **Safety & Eligibility** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- technical/payment correction evidence → relevant source Domain plus Audit/operational evidence as applicable;
- dissatisfaction/refund aggregates → **Analytics** derived analytical facts.

**Boundary:** Refund reason categories must not be inferred solely from free-text/support notes when an authoritative commercial reason can be captured. Safety/eligibility and technical/payment refunds remain analytically separate from product-value dissatisfaction.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

### ANL-EV-014 — Support burden and manual intervention

**Measurement question:** How much support did the pilot require, what kind of support was needed, and how much manual/developer/expert intervention was required?

**Required source truth/evidence:**

- the underlying business issue and any corrective transition remain owned by the affected Domain: e.g. Commerce for payment correction, Entitlements for access correction, Temperament for assessment state, Safety for eligibility, Plans for plan correction;
- sensitive operator actions may additionally generate **Audit & Evidence** records, but Audit does not become the business owner;
- support contact occurrence, support minutes, issue category and intervention level may be represented as permitted **Analytics operational analytical facts** — `S2_ANALYTICS_GOVERNED_FACT` — when their only durable purpose is pilot/support measurement;
- external helpdesk/email-provider records, if any, are `S4_EXTERNAL_EVIDENCE` until admitted under a governed analytical/source contract.

**Boundary:** No universal Support Domain, universal `Task` Resource or shadow case-authority layer is justified for FP-006 measurement. If a future support product requires a durable case lifecycle with its own independent business meaning, that would require separate Product/Domain analysis; Analytics measurement does not authorise it.

**Pass-2 result:** `SOURCE ROUTE RESOLVED` for the current pilot-measurement need. The Pass-1 “support operational truth” candidate seam does **not** require a new upstream Domain based on current evidence.

---

### ANL-EV-015 — Pilot economics and limited-public acquisition economics

**Measurement question:** What did the pilot actually cost to serve and what commercial/economic signal exists without pretending the pilot proves mature CAC/LTV/margin economics?

**Required source truth/evidence:**

- product/price/promotion/actual paid/refund/settlement truth → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- provider-reported fees before reconciliation → `S4_EXTERNAL_EVIDENCE`; reconciled commercial fee/settlement evidence may become Commerce source truth where the Commerce contract owns it;
- founder/staff support effort → **Analytics operational facts** from `ANL-EV-014` — `S2_ANALYTICS_GOVERNED_FACT`;
- channel spend, fulfilment/vendor cost or other externally sourced cost evidence without an approved platform business owner → `S4_EXTERNAL_EVIDENCE` admitted as bounded analytical cost evidence, not accounting authority;
- attributed purchasers, CAC-like calculations and contribution analyses → **Analytics** derived facts/interpretations.

**Boundary:** Early first-10/25/50 evidence has no invented CAC/LTV/margin threshold. At limited public, acquisition economics may be calculated, but analytical labels must not silently claim accounting authority. “Revenue” must be defined from its Commerce source basis rather than used as an ambiguous catch-all.

**Pass-2 result:** `SOURCE ROUTE RESOLVED` with explicit non-accounting limitation.

---

### ANL-EV-016 — Release-integrity and no-go evidence

**Measurement question:** Did any of the Product-Law zero-tolerance/core-readiness failures occur, and are the operational targets backed by authoritative evidence?

**Required source truth/evidence:**

- duplicate charge/payment effect → **Commerce** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- duplicate entitlement effect → **Entitlements** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- unreproducible plan or plan-generation truth → **Plans & Nutrition** — `S1_SOURCE_DOMAIN_AUTHORITY`;
- critical safety failure / incorrect pathway authority → **Safety & Eligibility** with relevant **Audit & Evidence** incident evidence;
- unauthorised sensitive-data exposure → relevant source/privacy/access facts plus **Audit & Evidence** security/incident evidence;
- plan-generation success → **Plans & Nutrition**;
- entitlement fulfilment success → **Entitlements**;
- incident/release decision evidence → **Audit & Evidence**;
- counts/rates/dashboard readouts → **Analytics** derived facts.

**Boundary:** Missing telemetry cannot be interpreted as “zero incidents.” The source systems/incident evidence must support the zero claim; Analytics only presents the evidence-backed aggregate.

**Pass-2 result:** `SOURCE ROUTE RESOLVED`.

---

## 4. Consolidated source-owner routing

The FP-006 core measurement path can therefore be routed without creating a shadow Analytics authority:

```text
Commerce -------------------- payment / refund / commercial amount ----------┐
Entitlements ---------------- access / grant / consumption ------------------┤
Temperament ----------------- assessment / result / provenance --------------┤
Health Records -------------- health-intake facts ---------------------------┤
Safety & Eligibility -------- pathway / eligibility / safety ----------------┤
Plans & Nutrition ----------- generation / delivery / activation ------------┤
Habits, Journals & Progress - governed progress/check-in evidence -----------┤
Communications -------------- message intent/delivery context ---------------┤
Audit & Evidence ------------ incident/security/release evidence ------------┤
                                                                             ▼
                                                              Analytics measurements
                                                     (facts / projections / aggregates)

Analytics ------------------- acquisition/support analytical evidence --------┘
External/client evidence ---- admitted only with explicit evidence class
```

The required value-response source remains deliberately outside this resolved diagram until `ANL-EV-012` is pressure-tested.

---

## 5. What changed from the Pass-1 candidate seams

### 5.1 Support operational truth — narrowed and resolved for current scope

The current authority is sufficient for FP-006 support-burden measurement without inventing a Support Domain:

- business corrections remain source-Domain truth;
- operator Work remains a projection over Domain-owned obligations;
- support effort/contact/category/intervention level may be Analytics-owned operational analytical facts when their purpose is measurement only;
- Audit records sensitive operator evidence where required without becoming support/business authority.

No upstream amendment is justified by this measurement need alone.

### 5.2 Pilot value-survey truth — still unresolved by design

`ANL-EV-012` remains the only source-owner seam that cannot safely be classified in this pass. A dedicated purpose/ownership pressure test must decide whether the required FP-006 value response is bounded product-loop feedback or genuine Research & Feedback capability.

No `ANL-GAP-*` or `ANL-UPD-*` is created yet.

### 5.3 Anonymous acquisition continuity — not tested in this pass

Pass 2 classifies anonymous behavioural observations and acquisition evidence but does **not** decide how anonymous observations may be joined to known Accounts/purchasers. Existing FES/privacy constraints remain unchanged. This belongs to the later privacy/attribution pass.

### 5.4 Small-cohort disclosure — not tested in this pass

Pass 2 identifies source truth only. Suppression, rare-segment disclosure, minimum cohort sizes and dashboard visibility belong to the dedicated privacy/small-cohort pass.

---

## 6. Explicit non-decisions

This pass does **not** define:

- event names or event payloads;
- database tables/Resources;
- numerator or denominator implementations;
- qualifying-action lists beyond meanings already fixed by Product Law;
- deduplication keys or late-event correction rules;
- attribution windows/models;
- anonymous-to-known stitching;
- cookies/device identifiers;
- retention periods or deletion mechanics;
- small-cohort suppression thresholds;
- survey tooling or Research activation;
- analytics vendors, warehouses, queues, Redis/ETS or specialised stores;
- dashboards or reporting UI;
- A/B/n assignment, exposure, significance or stopping rules.

---

## 7. Pass 2 disposition

**PASS — SOURCE-TRUTH MAP COMPLETE FOR THE FP-006 CORE JOURNEY, WITH ONE DELIBERATE SOURCE-OWNERSHIP DEFERMENT.**

The core paid journey can be measured without making Analytics a shadow owner. Payment, access, assessment, health, safety, plan, progress, refund and incident truth remain with their owning Domains. Acquisition/support analytical evidence can live in Analytics when it does not imply business authority. External/client observations remain explicitly weaker evidence.

`ANL-EV-012` — the durable value/relevance/price-value response — remains intentionally unresolved and requires a separate focused authority/purpose pressure test before its metric contract is frozen.

No authority amendment is proposed in this pass. No implementation is authorised.

**Recommended next pass:** resolve only `ANL-EV-012` — FP-006 required value/relevance/price-value response ownership and purpose classification — before moving into metric-contract formulas/denominators.
