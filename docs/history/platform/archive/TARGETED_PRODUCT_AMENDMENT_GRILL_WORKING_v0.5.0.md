# Targeted Product Amendment Grill — Working Decision Record

**Document version:** v0.5.0  
**Status:** NON-AUTHORITATIVE / HISTORICAL WORKING EVIDENCE  
**SemVer note:** First tracked version. The earlier unversioned file is a bootstrap draft only and is not part of the SemVer history.  
**Purpose:** Capture the interactive Product Amendment Grill, accepted recommendations, unresolved questions, rejected scope, and downstream consequences before any Product Law amendment is drafted.  
**Repository authority:** None. Live GitHub remains canonical.  
**Mutation rule:** This document does not amend Product Law, create governed identifiers, assign Domains, create Feature Packs, or authorize implementation.

---

## 1. Scope of this Grill

This Grill is limited to four Product-level directions:

1. Research & Feedback
2. Voting / Balloting / Competitions
3. Interactive Educational Tools / Calculators / Decision Aids
4. Platform Member Reference

Explicitly outside this Product Grill:

- Errors & Diagnostics
- Observability refinement
- Native Compute / Rustler
- Engineering Quality

Those remain downstream Architecture / Engineering amendment inputs.

---

# Round A — Research & Feedback

## Q1 — Product role

### Product-owner intent

The platform should support:

- normal research and interaction questions on the site;
- lightweight questions to get to know users;
- opinion and engagement questions;
- structured feedback;
- structured research campaigns.

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The platform supports both:

### A. Lightweight Interaction / Feedback

Examples include:

- topic-preference questions;
- usefulness ratings;
- quick opinion questions;
- pulse questions;
- lightweight engagement polls;
- simple feedback prompts.

### B. Governed Research Campaigns

Examples include:

- structured questionnaires;
- user research;
- longitudinal surveys;
- product/market research;
- structured participant-feedback programmes;
- research polls;
- formally governed/versioned instruments.

The platform does **not** thereby become a general-purpose SurveyMonkey/Typeform-style survey-building platform.

Common implementation primitives may later be shared, but lightweight interaction and governed research may carry different governance burdens.

**Status:** APPROVED

---

## Q2 — Participation identity

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Each instrument or campaign explicitly declares its participation identity mode.

Supported Product-level modes may include:

- **Account-linked** — the platform knows which Account submitted the response.
- **Pseudonymous** — approved linkage is retained for the campaign purpose without ordinary research consumers necessarily seeing participant identity.
- **Anonymous** — the response is not linked to a platform Account as Research/Feedback truth.

Account-linked participation is preferred where identity, eligibility, longitudinal follow-up, or personalised context is materially required.

Pseudonymous or anonymous participation is permitted where the approved purpose justifies it.

**Identity mode and uniqueness guarantee are separate Product promises.**

In particular:

> Anonymous participation does not automatically imply one-person-one-response.

The platform must not secretly preserve Account linkage merely to enforce deduplication while presenting the response as genuinely anonymous.

**Status:** APPROVED

---

## Q3 — What Research & Feedback responses may change

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Research and feedback responses remain Research/Feedback truth.

They do **not** directly mutate authoritative truth in:

- Health Records;
- Safety & Eligibility;
- Plans;
- Temperament;
- Commerce;
- Entitlements.

A response may initiate, offer, or request a separately governed action in another owning capability, but that owning capability must independently establish its own authority before changing its truth.

Example:

```text
Research response:
"I have a peanut allergy"
        ↓
Research/Feedback truth

Optional separate action:
"Would you like to update your health information?"
        ↓
Governed Health Records action
        ↓
Health Records truth
```

Research participation therefore does not silently transfer write authority into other Domains.

**Status:** APPROVED

---

## Q4 — Instrument and response lifecycle

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Persisted Research/Feedback instruments preserve the exact question/instrument version against which a response was submitted.

Governed research campaigns use immutable published versions and explicit lifecycle semantics for matters such as:

- publication;
- correction;
- withdrawal;
- retention;
- closure.

Lightweight interaction may use a simpler lifecycle where its approved purpose does not justify full research governance.

Core invariant:

> A published persisted question must not be edited in place in a way that changes the meaning of responses already collected against that version.

A simple non-persisted engagement prompt does not automatically require the full governed research lifecycle.

**Status:** APPROVED

---

## Q5 — Anonymous responses and later withdrawal

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

For genuinely anonymous responses, the platform does not promise later individual withdrawal or deletion when it has no reliable way to identify which response belongs to the participant.

That limitation must be made clear before submission where relevant.

Account-linked or appropriately pseudonymous campaigns may support individual correction, withdrawal, or deletion where the approved purpose and applicable law/policy require it.

The exact technical mechanism remains deferred.

**Status:** APPROVED

---

## Q6 — Sensitive and health-related research questions

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Research instruments may ask health-related or other sensitive questions only under an explicitly approved purpose and stronger privacy/safety governance.

Those answers remain Research/Feedback truth unless a separate governed action explicitly establishes the information as authoritative truth in another owning capability.

Sensitive research is therefore permitted, but it does not bypass Health Records, Safety, Consent, or other owning authority.

**Status:** APPROVED

---

## Q7 — Participant visibility of submitted responses

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

For Account-linked structured research, participants should normally be able to see responses they submitted where reasonably appropriate.

Exceptions may exist where participant visibility would conflict with:

- the approved research design;
- safety;
- law;
- integrity;
- another explicit Product constraint.

This does **not** promise a universal permanent “My Surveys” experience for every lightweight interaction or feedback response.

**Status:** APPROVED

---

## Q8 — Research participation incentives

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The Product may support incentives for research participation, including future examples such as:

- points;
- vouchers;
- discounts;
- competition entries;
- programme rewards.

Incentives are permitted but never automatic.

Research/Feedback does not manufacture Commerce or Entitlement truth.

Any actual reward, discount, benefit, or entitlement must be granted through the owning capability under its own governance.

Legal, commercial, fairness, and abuse constraints remain downstream gates where applicable.

**Status:** APPROVED

---

## Q9 — Targeting and cohorts

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Research campaigns may target approved participant cohorts using existing platform truth where the campaign purpose permits it.

Examples may include cohorts based on:

- programme participation;
- product purchase;
- plan completion;
- temperament;
- other approved participant attributes.

Targeting does not transfer ownership of the source attribute to Research/Feedback.

Sensitive or health-derived targeting requires an explicitly justified privacy/safety basis and must not expose the targeting attribute to unauthorised research operators.

The Product does not thereby promise unrestricted “query anything about everybody” segmentation.

**Status:** APPROVED

---

## Q10 — Longitudinal and repeated research

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Governed research may be:

- cross-sectional; or
- longitudinal/repeated over time.

Examples may include:

- before/after programme research;
- periodic wellbeing pulses;
- 30/60/90-day follow-up;
- repeated product-satisfaction research;
- research cohorts.

Where participant-level longitudinal linkage is required, the approved identity mode must permit that linkage and the participant purpose/expectation must be clear.

Genuinely anonymous research cannot promise participant-level longitudinal linkage.

**Status:** APPROVED

---

## Q11 — Publication of findings

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Research findings may be published:

- internally;
- to participants;
- or publicly,

where explicitly approved.

Publication should use an appropriate aggregate or otherwise authorised form by default.

Collecting an identified response does not automatically authorise publication of the individual response or identity.

Individual testimonials, attributable quotations, or equivalent uses require their own applicable permission/authority.

**Status:** APPROVED

---

## Q12 — Follow-up and escalation

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

A Research/Feedback instrument may explicitly support:

- participant-requested follow-up;
- defined escalation pathways;
- other approved downstream actions.

The response remains Research/Feedback truth.

Any follow-up obligation or action is separately governed by the owning capability.

Example:

```text
Feedback response
        ↓
"I would like someone to contact me."
        ↓
separately governed follow-up intent
        ↓
owning Communications/support capability
```

Research responses do **not** create an implicit universal promise that all free-text or research responses are continuously monitored for safety or intervention.

If a campaign promises monitoring or escalation, that promise must be explicit and governed.

**Status:** APPROVED

---

# Round A — Current Consolidated Product Direction

Research & Feedback is currently shaping into a mature platform capability with two bounded modes:

1. lightweight interaction/feedback;
2. governed structured research campaigns.

Current accepted principles:

- identity mode is explicit;
- identity mode and uniqueness promise are separate;
- research responses remain Research/Feedback truth;
- cross-domain authoritative changes require separate owner-controlled actions;
- persisted instruments are version-bound;
- governed published versions are immutable;
- genuinely anonymous responses may not support later individual withdrawal;
- sensitive research is permitted under stronger purpose/privacy/safety governance;
- Account-linked structured research normally supports appropriate participant visibility;
- incentives are permitted but must flow through owning commercial/entitlement authority;
- approved cohort targeting is permitted without transferring source-data ownership;
- longitudinal research is supported where identity mode permits it;
- findings may be published in approved aggregate/authorised form;
- explicit follow-up/escalation pathways are supported;
- no universal monitoring promise exists by default;
- the capability is not a generic survey-platform commitment.

---

## Q13 — Correction and finality for identified/pseudonymous responses

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Account-linked or appropriately pseudonymous responses may be correctable where the campaign purpose permits it.

Each campaign or instrument must make clear whether a submitted response is:

- editable;
- replaceable through a governed correction;
- or final after submission / a defined cutoff.

Corrections must preserve appropriate history rather than silently overwriting the original meaning where historical integrity matters.

Universal editability is not promised.

**Status:** APPROVED

---

## Q14 — Withdrawal/deletion for identified or pseudonymous research

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Identifiable participants may request withdrawal or deletion where applicable, subject to:

- the approved campaign purpose;
- applicable law/policy;
- legitimate retention obligations;
- the integrity of already-published aggregate findings.

The Product may distinguish:

- withdrawal from future research use;
- removal or reduction of identity linkage;
- deletion of the participant response where applicable;
- retention of minimal compliance/evidence records;
- already-published aggregate findings that cannot practically be reconstructed as though the response had never contributed.

The exact downstream deletion/retention mechanism remains deferred.

**Status:** APPROVED

---

## Q15 — Account closure/deletion and research retention

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Closing an Account does not automatically destroy otherwise valid Research/Feedback truth.

Research/Feedback has its own governed retention lifecycle.

Where continued identity linkage is no longer justified, the platform should remove, reduce, or otherwise govern that linkage according to the approved privacy/deletion rules.

Account closure therefore does not automatically mean:

> erase every historical research response.

But identity linkage must not be retained longer than justified by the approved purpose, policy, or law.

The exact technical retention/anonymisation mechanism remains deferred.

**Status:** APPROVED

---

## Q16 — Staff annotations and review notes

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Authorised staff may add governed annotations, classifications, exclusions, or review notes where a campaign or feedback process requires them.

Staff-added information must remain distinguishable from participant-submitted truth.

The platform must not silently rewrite a participant response and later represent a staff interpretation as though the participant submitted it.

Examples of permitted distinct annotations may include:

- participant requested follow-up;
- response excluded under an approved rule;
- duplicate/invalid submission classification;
- governed research-review notes.

Exact permissions, audit treatment, and storage remain downstream decisions.

**Status:** APPROVED

---

# Round A — Closure Status

**ROUND A STATUS: COMPLETE / PRODUCT DIRECTION APPROVED**

Research & Feedback is sufficiently defined at Product level to proceed to later Product-amendment drafting after the full four-round Grill is complete.

No Domain ownership decision is made here.

No ARQ, ARC, Feature Pack, implementation, package, schema, or provider decision is made here.

Remaining details such as exact campaign closure mechanics, retention implementation, analytics projection, and technical anonymity mechanisms are downstream unless a later cross-capability pressure test exposes a genuine Product contradiction.

---

# Round B — Voting / Balloting / Competitions

**Status:** COMPLETE / PRODUCT DIRECTION APPROVED

## Q1 — Product role

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The mature platform supports three bounded participation modes:

1. **Lightweight opinion polls** — low-stakes interaction and preference gathering.
2. **Research polls** — governed under the Research & Feedback capability.
3. **Governed voting / balloting** — contextual voting where eligibility, limits, opening/closing, finality, abuse review or an official result matter.

Competition voting is a governed-voting use case, not a separate generic election-platform commitment.

The platform does not thereby become a general-purpose civic election or ballot platform.

**Status:** APPROVED

---

## Q2 — Eligibility, identity and public unauthenticated voting

### Product-owner clarification

For current Nuwe Jy competition voting, the public may vote without creating an Account. Legitimate voters may include husbands, friends, colleagues, adult children and other supporters.

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Each vote declares its eligibility and identity mode.

Governed voting may be:

- Account-linked where account identity or programme/event participation is part of eligibility;
- publicly accessible without an Account where the Product purpose is broad public participation;
- anonymous or otherwise low-identity only where the Product does not promise verified person-level uniqueness.

For public Nuwe Jy-style voting:

> No platform Account is required merely to cast a legitimate public vote.

Public unauthenticated participation is therefore an approved Product mode.

However:

> Public unauthenticated voting does not imply a cryptographically or identity-verified one-human-one-vote guarantee.

Duplicate suppression, rate limiting, abuse detection, invalidation rules and other integrity controls may improve vote quality, but they must not be represented as stronger identity assurance than the Product actually provides.

The exact technical duplicate-detection or anti-abuse mechanism remains deferred.

**Status:** APPROVED

---

## Q3 — Vote limits and changing a vote

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

A governed vote explicitly defines its participation rules, including where relevant:

- allowed selections;
- maximum votes/selections;
- whether a submitted vote may be changed;
- when voting opens;
- when voting closes;
- when the submitted ballot becomes final.

For identity-capable governed ballots, the normal Product default is one active ballot per eligible participant, changeable until close unless the approved vote says otherwise.

Public unauthenticated competition voting may use a different approved integrity model because person-level uniqueness cannot be guaranteed solely through Account identity.

The exact enforcement mechanism remains deferred.

**Status:** APPROVED

---

## Q4 — Tally versus official result

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

For governed voting, a tally and an official result are distinct concepts.

A tally represents counted/accepted voting activity at a point in time.

A governed competition or ballot may require a separately finalised official result after applicable:

- duplicate/abuse review;
- eligibility checks;
- invalidation;
- moderation;
- tie rules;
- cancellation rules;
- adjudication.

For low-stakes opinion polls, the displayed tally may itself be the final displayed outcome.

For a governed competition:

```text
submitted votes
→ integrity/eligibility treatment
→ accepted tally
→ finalisation
→ official result
```

The platform must not silently treat a raw count, cache, analytics projection or provider count as the authoritative official result when governed finalisation applies.

**Status:** APPROVED

---

## Nuwe Jy current-state Product note

Current Nuwe Jy voting is form-based:

- the public submits votes;
- an Account is not required;
- submissions are collected;
- duplicates are removed;
- the remaining votes are used to determine the winner.

The future governed system should preserve the legitimate broad-public participation model while making the rules explicit and auditable.

The Product goal is therefore not to introduce mandatory Account registration, but to improve:

- declared voting rules;
- duplicate/abuse handling;
- tally integrity;
- finalisation;
- winner determination;
- auditability;
- operator confidence.

Exact fraud detection, identity verification, cookies, device signals, email/phone requirements, rate limits or other technical controls are not decided here.

---

## Q5 — Vote/tally visibility

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Vote and tally visibility is configurable by the approved voting context.

Permitted Product-level modes may include:

- hidden while voting is open;
- approximate/non-ranking participation indicators;
- exact live counts or percentages;
- final results only.

For governed competitions, the normal default is to keep exact live tallies hidden until voting closes and applicable finalisation/integrity review completes, unless the competition explicitly approves live visibility.

For lightweight opinion polls, live percentages/counts may be appropriate.

The platform therefore supports both transparent live interaction and secret/unrevealed competition tallies according to the approved context.

**Status:** APPROVED

---

## Q6 — Duplicate, abuse and repeated-vote handling

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Governed public voting may reject, invalidate, throttle, hold for review, or otherwise constrain submissions under predeclared integrity rules.

The Product must distinguish, where materially relevant, between:

- submitted;
- accepted;
- rejected/invalidated;
- held/requires review.

Material operator invalidation must be explainable and auditable.

Public unauthenticated voting does not promise perfect person-level uniqueness or a fraud-proof result.

### Anti-abuse clarification

The Product **does require proportionate anti-abuse controls** capable of preventing or constraining obvious repeated-vote behaviour such as one person or automated process attempting to submit repeatedly at abusive volume.

This may include throttling/rate-limiting behaviour as an implementation mechanism.

However, Product Law does **not** set:

- exact request rates;
- exact time windows;
- IP/device/browser rules;
- CAPTCHA/challenge mechanisms;
- cookies;
- fingerprinting;
- email/phone verification requirements;
- provider choices;
- automatic invalidation thresholds.

Those mechanisms and thresholds are deferred to Architecture/JIT implementation and must remain proportionate to the voting context, privacy expectations, and abuse risk.

**Status:** APPROVED

---

## Q7 — Tie, cancellation, disqualification and material integrity failure

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Every governed competition or material ballot must have an approved finalisation policy covering, where applicable:

- ties;
- contestant/option disqualification;
- material integrity failures;
- material outage or voting disruption;
- cancellation;
- re-run or extension;
- adjudication.

A tie-breaking or exception rule must not be invented after the outcome is known merely to favour a preferred result.

Different competitions may use different preapproved rules, including:

- additional voting round;
- approved adjudication panel;
- predetermined secondary criterion;
- jointly recognised winners;
- cancellation/re-run.

**Status:** APPROVED

---

## Q8 — Official winner and reward fulfilment

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

For governed competitions:

```text
submitted votes
→ integrity/eligibility treatment
→ accepted tally
→ governed finalisation
→ official result / winner
→ separately governed reward or entitlement fulfilment
```

The largest raw or cached count does not automatically create the official winner.

Winner/result truth is distinct from prize/reward fulfilment.

Any prize, benefit, entitlement, discount, voucher, programme benefit, or other commercial outcome must be granted through the owning capability under its own governance.

This separation permits lawful handling of:

- invalidated votes;
- disqualification;
- ties;
- winner ineligibility;
- winner refusal;
- fulfilment failure;
- changed or cancelled rewards.

**Status:** APPROVED

---

## Q9 — Voter privacy and leaderboard visibility

### Product-owner clarification

Individual voter choices should not be public.

The platform may later support leaderboards or ranked aggregate views for certain voting contexts.

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Individual voter identity and individual ballot choice are private by default.

Public or participant-facing voting views should ordinarily expose aggregate outcome information rather than showing who voted for whom.

Authorised operators may receive limited access needed for integrity review or adjudication under later governance.

The Product may support a configurable leaderboard or ranked aggregate presentation for approved voting contexts.

A leaderboard may show, for example:

- ranked contestants/options;
- aggregate accepted vote counts;
- percentages;
- approved participation indicators.

A leaderboard does **not** imply public disclosure of individual voter identity or ballot choice.

Leaderboard visibility remains context-specific and is governed together with the vote/tally visibility rules approved in Q5.

**Status:** APPROVED

---

## Q10 — Campaigning and vote solicitation

### Product-owner clarification

Contestants may share and invite legitimate supporters to vote.

Automated voting, scripted repetition and other manipulation must not be allowed.

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Where a competition permits public participation, contestants may legitimately invite supporters to vote.

Examples of legitimate activity may include:

- sharing the approved voting link;
- asking friends, family, colleagues or followers to participate;
- promoting the competition through ordinary social or communication channels.

The platform must prohibit deliberate manipulation such as:

- bots;
- scripts;
- vote farms;
- fabricated submissions;
- deliberate circumvention of anti-abuse controls;
- other prohibited automated or deceptive voting activity.

A particular competition may adopt stricter campaigning rules where its approved purpose requires them.

Ordinary campaigning does not itself make a vote invalid.

**Status:** APPROVED

---

## Q11 — Provisional tally and finalisation review

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

A governed competition may use a defined post-close integrity and finalisation period.

During that period:

```text
VOTING CLOSED
→ PROVISIONAL / UNFINALISED TALLY
→ integrity / duplicate / eligibility review
→ FINAL RESULT
→ winner/result announcement
```

No official winner exists merely because the voting window has closed if the competition requires post-close review.

The duration and exact operational process remain downstream decisions.

**Status:** APPROVED

---

## Q12 — Governed operator adjudication

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Authorised operators may perform governed adjudication actions required by approved competition rules, including where applicable:

- invalidating duplicate/manipulated votes;
- resolving reviewed submissions;
- recording contestant/option disqualification;
- correcting a documented operational error;
- approving/finalising the official result.

Operators may not arbitrarily alter counts or choose a preferred winner outside approved rules.

Material manual intervention must have an approved reason and remain distinguishable from voter-generated activity.

Product principle:

> Human adjudication is permitted; invisible manipulation is not.

Exact permissions, audit records and implementation controls remain downstream decisions.

**Status:** APPROVED

---

# Round B — Closure Status

**ROUND B STATUS: COMPLETE / PRODUCT DIRECTION APPROVED**

Voting / Balloting / Competitions is sufficiently defined at Product level to proceed to later Product-amendment drafting after the full four-round Grill is complete.

Current accepted principles include:

- lightweight polls, research polls and contextual governed voting are distinct Product modes;
- public unauthenticated voting is a legitimate governed mode;
- no Account is required by default for Nuwe Jy-style public voting;
- public unauthenticated voting does not promise verified one-human-one-vote;
- vote rules, limits and correction/finality are explicit;
- tally and official result are distinct;
- exact live visibility is configurable;
- candidate/option leaderboards may be supported without exposing individual voter choices;
- proportionate anti-abuse controls are required;
- automated/manipulated voting is prohibited;
- tie, cancellation, disqualification and integrity-failure rules are predeclared;
- official result/winner truth is separate from reward/entitlement fulfilment;
- ordinary campaigning and legitimate vote solicitation may be permitted;
- provisional post-close review may precede finalisation;
- operator adjudication is allowed only under governed, explainable rules.

No Voting Domain is approved here.

No exact anti-abuse mechanism, rate limit, CAPTCHA, identity-verification mechanism, storage model, schema, package, provider or implementation detail is approved here.

---

# Round C — Interactive Tools / Calculators / Decision Aids

**Status:** COMPLETE / PRODUCT DIRECTION APPROVED

## Q1 — Product capability boundary

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The mature platform supports approved interactive educational tools, calculators, visualisations and decision aids.

These may include:

- public educational calculators;
- interactive articles;
- quizzes/self-assessments;
- decision aids;
- progress visualisations;
- interactive planning tools;
- Account-linked personalised tools;
- participant dashboards and similar interactive views.

This does **not** make the platform a general-purpose no-code or user-programmable calculation/execution platform.

The Product does not promise arbitrary administrator-authored executable formulas or unrestricted custom tool creation.

**Status:** APPROVED

---

## Q2 — Calculation versus authority

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Interactive-tool output is educational or advisory by default.

A calculated result does not automatically become authoritative truth in:

- Health Records;
- Safety & Eligibility;
- Plans;
- Temperament;
- Commerce;
- Entitlements.

If an interactive experience is intended to change authoritative truth, the owning capability must perform a separately governed action that establishes that truth.

Product principle:

> Calculation is not authority.

Ownership follows the durable truth affected, not the UI or calculation mechanism.

**Status:** APPROVED

---

## Q3 — Persistence of inputs/results

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Public or anonymous interactive-tool inputs and results are non-persistent by default.

The platform should not collect or retain data merely because a calculator or tool technically can.

Account-linked tools may persist approved inputs or results only where there is clear Product value and the participant expectation/purpose is explicit.

Legitimate persistence purposes may include:

- continuing later;
- comparison over time;
- reproducibility;
- approved progress/history;
- an authorised downstream workflow.

Persistence is therefore purpose-driven rather than automatic.

**Status:** APPROVED

---

## Q4 — Versioning and reproducibility

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Any persisted or materially consequential interactive result must remain associated with the approved tool/calculation version that produced it.

A material change to calculation meaning creates a new governed version rather than silently changing the interpretation of historical stored results.

Where consequential/persisted output exists, the platform should later be able to establish at least:

- which tool/calculation produced it;
- which version produced it;
- when it was produced;
- the approved input context required to understand/reproduce the result;
- the resulting output.

Low-stakes ephemeral tools do not automatically require the same level of historical governance.

**Status:** APPROVED

---

## Q5 — Health and safety-sensitive tools

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The platform may support interactive tools, calculators and decision aids involving health or safety-sensitive information.

Such tools may:

- educate;
- screen;
- guide;
- surface a need for further review;
- gather inputs for a separately governed authoritative action.

However, a tool does not acquire authority merely because its calculation concerns health or safety.

Any output that changes authoritative truth in Safety & Eligibility, Health Records, Plans or another owning capability must pass through that owning capability's governed action.

A safety-critical interactive experience may be the UI through which an authoritative Safety action is invoked, but the authority remains with the owning capability.

**Status:** APPROVED

---

## Q6 — Use of existing participant data

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Personalised tools may use information already held by the platform where:

- the tool's approved purpose justifies it;
- the participant context/expectation permits it;
- privacy and consent requirements are satisfied;
- only the minimum necessary information is used.

Possible source information may include, where appropriately governed:

- temperament;
- programme participation;
- plan information;
- habit/progress history;
- health information;
- other approved participant data.

Using source data does not transfer ownership of that durable truth to the interactive tool.

Sensitive or health-derived information carries a higher privacy/safety bar.

**Status:** APPROVED

---

## Q7 — Public, Account-gated and entitlement-gated tools

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Interactive tools may use different approved access models, including:

- **public** — acquisition, education or engagement;
- **Account-gated** — personalised, saved or participant-specific experience;
- **entitlement-gated / paid** — included in a purchased product, programme, membership or premium capability.

The tool itself does not establish entitlement merely because access is commercial.

Entitlements remains authoritative for whether the participant may access an entitlement-gated tool.

**Status:** APPROVED

---

## Q8 — Downstream workflow initiation

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

An interactive tool may initiate, offer or request an approved downstream action.

The tool's output or user interaction does not itself perform the authoritative transition unless the owning capability is explicitly being invoked through its governed action.

Examples:

```text
interactive tool
→ "request plan adjustment"
→ Plans validates and performs governed action
→ Plan truth changes
```

or:

```text
interactive decision aid
→ "requires safety review"
→ Safety & Eligibility action
→ authoritative eligibility decision
```

The owning capability remains responsible for validating and establishing its own truth.

**Status:** APPROVED

---

## Q9 — Explainability

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Interactive results should be explainable in proportion to their consequence.

Low-risk tools may provide a simple explanation.

Consequential, personalised, health-sensitive or safety-sensitive tools must provide enough understandable context for the participant or operator to understand:

- what materially influenced the result;
- relevant limitations;
- the appropriate next step where applicable.

Explainability does not require exposing source code, proprietary formulas or unsafe internal implementation detail.

**Status:** APPROVED

---

## Q10 — Dashboards and visualisations

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Dashboards and visualisations are legitimate interactive Product experiences.

They may combine and present truth from multiple owning capabilities.

A dashboard, chart or visualisation does not become authoritative merely because it aggregates or presents data.

Derived presentation metrics must not silently become new business authority.

This Product capability therefore does not imply a new Dashboard Domain.

**Status:** APPROVED

---

## Q11 — Administrator-configurable tools and formulas

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Authorised staff may configure approved interactive-tool types and governed content/parameters, including where appropriate:

- titles;
- descriptions;
- questions;
- answer options;
- educational copy;
- media;
- approved thresholds or parameters;
- publication/version selection.

The Product does **not** promise arbitrary executable formulas, unrestricted scripts, JavaScript, or arbitrary code authored through a CMS/admin experience.

Material calculation behaviour remains governed, versioned and testable application logic unless a later requirement proves the need for a safer bounded configuration/rules mechanism.

**Status:** APPROVED

---

## Q12 — Correction and recalculation

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Interactive tools support correction and recalculation appropriate to their purpose.

For ephemeral tools, a corrected input may simply replace the currently displayed result.

For persisted or consequential tools, recalculation must not silently falsify historical meaning.

A later result remains distinguishable from the earlier result and from the inputs/version that produced it where historical integrity matters.

The Product does not require indefinite visibility of every superseded result; exact retention/history presentation remains purpose-dependent and downstream.

**Status:** APPROVED

---

# Round C — Closure Status

**ROUND C STATUS: COMPLETE / PRODUCT DIRECTION APPROVED**

Interactive Tools / Calculators / Decision Aids is sufficiently defined at Product level to proceed to later Product-amendment drafting after the full four-round Grill is complete.

Current accepted principles include:

- approved public and personalised interactive tools are a mature Product capability;
- the platform is not a generic no-code execution environment;
- calculation does not itself create authority;
- authoritative changes remain with the owning capability;
- public/anonymous inputs are ephemeral by default;
- persistence requires Product value and clear purpose;
- persisted/consequential outputs are version-bound;
- health/safety-sensitive tools are permitted under stronger boundaries;
- personalised tools may consume existing platform truth without taking ownership of it;
- public, Account-gated and entitlement-gated access models are legitimate;
- tools may initiate downstream workflows without owning the resulting truth;
- explainability is proportionate to consequence;
- dashboards/visualisations are projections, not authority;
- staff may configure approved bounded tools/content, not arbitrary executable code;
- correction/recalculation is supported without falsifying historical meaning.

No Interactive Tools Domain is approved here.

No exact schema, Resource, package, formula engine, scripting engine, cache, provider or execution architecture is approved here.

---

# Round D — Platform Member Reference

**Status:** COMPLETE / PRODUCT DIRECTION APPROVED

## Q1 — Who receives a Platform Member Reference?

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Every successfully created individual platform Account receives a Platform Member Reference.

This includes free Account holders as well as purchasers, participants, recipients or subscribers who hold an actual Account.

The following do not automatically receive a Platform Member Reference merely by appearing elsewhere in platform data:

- anonymous visitors;
- anonymous voters;
- anonymous research respondents;
- mailing-list/newsletter contacts with no Account;
- recipient email addresses that have not yet become Accounts.

The reference is created because an Account exists, not because the person has purchased or subscribed.

**Status:** APPROVED

---

## Q2 — What the reference means

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The Platform Member Reference is a stable human-facing identifier for an individual Account.

It does not itself represent:

- paid membership;
- subscription state;
- entitlement;
- authentication;
- authorisation;
- identity-verification assurance;
- database identity.

It may be used in human-facing platform interactions such as:

- customer support;
- participant communication;
- authorised staff lookup;
- offline/event interaction;
- checkout or gifting workflows;
- identifying an intended recipient/beneficiary Account.

Possession of the reference does not confer rights belonging to the referenced Account.

**Status:** APPROVED

---

## Q3 — Secrecy and exposure

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The Platform Member Reference is non-secret but private-by-default.

It may appear in appropriate participant-facing, staff-facing and transactional contexts.

Knowledge or possession of the reference must provide no authentication or authorisation power.

The Product does not promise that member references are publicly enumerable or suitable for unrestricted bulk exposure.

**Status:** APPROVED

---

## Q4 — Immutability and reuse

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Once assigned, a Platform Member Reference is:

- unique;
- immutable for that Account;
- never reassigned to another Account.

Normal Account changes such as email, name, password, products, membership or entitlements do not change it.

Account closure does not make the reference reusable.

Legitimate reactivation of the same Account retains its existing reference.

Exceptional merge/deletion/re-registration semantics remain to be resolved in the remaining Round D lifecycle questions.

**Status:** APPROVED

---

## Checkout / gifting / mixed-benefit clarification

### Product-owner intent

A purchaser may buy for herself and/or other people, including a mixture of subscribers and non-subscribers.

The Platform Member Reference should be usable as a human-facing code in checkout or related flows to identify an existing Account.

### Accepted boundary

**APPROVED PRODUCT DIRECTION**

A purchaser may enter or select a Platform Member Reference to identify an intended Account/recipient/beneficiary where an approved checkout or gifting workflow permits it.

The reference is a lookup/association key only.

It does **not** itself prove:

- that the purchaser controls the referenced Account;
- that the referenced person consents to a sensitive action;
- that a subscription is active;
- that a discount is valid;
- that an entitlement may be transferred or redeemed.

Any subscriber benefit, discount, entitlement or eligibility must be resolved authoritatively by the owning Commerce/Entitlements/Membership capability under the applicable Product rules.

The checkout experience must reveal no more information about the referenced Account than the approved purpose requires.

### Still-open Product question

The Product must still decide whether a benefit attached to the recipient/subscriber Account is:

- personal/non-transferable;
- usable when another purchaser buys specifically for that beneficiary;
- transferable under explicit gifting rules;
- or context-specific.

The member reference itself cannot answer that commercial policy question.

---

## Candidate implementation-format note — NOT PRODUCT LAW

The Product owner proposed the following candidate human-facing representation:

```text
VG-K7M-4P9-X
```

Candidate characteristics:

- six payload characters;
- one check character;
- human-safe alphabet excluding `0`, `1`, `I`, `L`, `O`, `U`;
- 30-symbol payload alphabet;
- payload space of `30^6 = 729,000,000` combinations;
- grouped presentation intended to be easy to read/type.

This is captured as a **deferred implementation candidate only**.

No exact prefix, alphabet, payload length, check-character algorithm, generation algorithm, database representation or collision strategy is approved by Product Law in this Grill.

### Brand-coupling warning

The literal `VG` prefix appears brand-specific.

Because the platform's public brand/domain may change, a permanent Account identifier should not be coupled to the current brand unless there is a deliberate requirement to retain that prefix forever.

Later Architecture/JIT work should therefore consider either:

- no semantic brand prefix;
- a stable brand-independent platform prefix;
- or a presentation layer that does not make the mutable public brand part of the immutable canonical reference.

---

## Q5 — Beneficiary-linked subscriber benefits when another person pays

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

A purchaser may pay for products or services intended for multiple beneficiaries, including a mixture of subscribers and non-subscribers.

Where an approved benefit belongs to a beneficiary Account, the platform may honour that benefit when another purchaser is paying specifically for that beneficiary.

Example:

```text
Purchaser: Jane

Jane   → Jane's Account/reference   → Jane's eligibility
Sarah  → Sarah's Account/reference  → Sarah's subscriber benefit
Megan  → Megan's Account/reference  → Megan's eligibility
```

The benefit is attached to the eligible beneficiary/context, not borrowed merely because the purchaser knows another person's member reference.

A beneficiary-linked benefit may not be applied to unrelated recipients or purchases unless that benefit's Product rules explicitly permit transferability.

The member reference itself does not establish that the benefit is valid.

Commerce/Entitlements or the applicable owning capability resolves the authoritative eligibility and discount/benefit.

**Status:** APPROVED

---

## Q6 — Minimum disclosure during member-reference lookup

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Entering or selecting a Platform Member Reference in checkout or another approved workflow may reveal only the minimum information necessary to:

- confirm the intended Account/beneficiary;
- prevent a material recipient-selection error;
- complete the authorised workflow.

The lookup must not expose unrelated Account information such as:

- full private identity information without need;
- email address without need;
- health information;
- purchase history;
- detailed membership history;
- unrelated entitlements;
- other sensitive/private Account data.

An approved workflow may internally evaluate benefit/eligibility without disclosing unnecessary source detail to the purchaser.

Exact UI confirmation and masking remain downstream decisions.

**Status:** APPROVED

---

## Q7 — Full Account deletion and later re-registration

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The Platform Member Reference is Account-scoped rather than a permanent lifelong identifier for the human person.

For the same Account:

```text
Account created
→ reference assigned

Account closed
→ reference remains reserved

same Account legitimately restored/reactivated
→ same reference retained
```

If an Account undergoes genuine final deletion and the person later creates a genuinely new Account, the new Account receives a new Platform Member Reference.

The old reference remains permanently non-reusable.

The Product does not require hidden cross-deletion linkage merely to recover the prior member reference.

Exact deletion/reconciliation mechanics remain downstream.

**Status:** APPROVED

---

## Q8 — Duplicate Account merge

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Where two Accounts are later established under governed rules to represent a duplicate Account situation and are merged/reconciled:

- exactly one Account/reference becomes the surviving canonical active Account identity;
- the non-surviving member reference is retired;
- a retired reference is never reassigned to another Account;
- historical/reconciliation evidence may preserve the relationship where justified;
- the retired reference must not continue behaving as a second equal active member identity.

The choice of surviving Account/reference must follow later governed merge/reconciliation rules rather than arbitrary operator preference.

A retired reference may remain internally resolvable for support/reconciliation where justified without regaining active authority.

**Status:** APPROVED

---

## Q9 — Staff lookup and support use

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

Authorised staff may search for an Account by Platform Member Reference for legitimate support, operations, commerce, event and reconciliation workflows.

The member reference is only a lookup key and does not bypass or expand normal staff authorisation.

**Status:** APPROVED

---

## Q10 — Participant-facing display and use

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The Platform Member Reference may be displayed or used where it materially assists with human-facing Account identification.

Appropriate contexts may include:

- Account/profile;
- support correspondence;
- order/gifting flows;
- selected emails;
- event/check-in interactions;
- participant-facing reports/documents where useful;
- telephone support or other human-assisted workflows.

The Product does not require the reference to appear on every public, transactional or participant-facing surface.

Use remains purpose-driven and private-by-default.

**Status:** APPROVED

---

## Q11 — Exceptional retirement/replacement

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

A Platform Member Reference is immutable under the normal Account lifecycle.

Governed exceptional retirement/replacement may be permitted only where a real security, privacy, integrity, reconciliation, or equivalent operational-correctness reason justifies replacement.

Routine vanity changes are not a Product requirement.

When replacement occurs:

- the old reference is permanently retired;
- it is never reassigned;
- the replacement relationship is preserved where governance requires it;
- only the new canonical reference remains active.

This is a narrow exception to normal immutability, not a general edit capability.

**Status:** APPROVED

---

## Q12 — Product-level format requirements

### Accepted recommendation

**APPROVED PRODUCT DIRECTION**

The Platform Member Reference must be suitable for routine human use.

Product-level requirements are:

- human-readable;
- reasonably short;
- practical to type, dictate, copy and display;
- resistant to common transcription mistakes;
- unambiguous for ordinary human entry;
- non-semantic;
- contains no encoded date of birth, gender, health state, geography, paid status or similar business meaning;
- non-secret;
- not obviously sequential in a way that unnecessarily exposes Account growth or materially simplifies enumeration;
- compatible with an error-detection/check mechanism;
- stable across ordinary Account changes;
- supported by a namespace large enough for realistic platform growth.

The exact representation remains an implementation decision.

### Preferred implementation candidate retained for later validation

```text
VG-K7M-4P9-X
```

Candidate characteristics:

- six payload characters;
- one check character;
- human-safe alphabet excluding `0`, `1`, `I`, `L`, `O`, `U`;
- 30-symbol payload alphabet;
- payload space of `30^6 = 729,000,000`;
- grouped presentation.

The exact prefix, alphabet, payload length, grouping, check algorithm, generation algorithm, collision strategy and database representation remain deferred.

The `VG` prefix is specifically **not** approved as durable Product Law because of potential coupling to a mutable public brand.

**Status:** APPROVED

---

# Round D — Closure Status

**ROUND D STATUS: COMPLETE / PRODUCT DIRECTION APPROVED**

Platform Member Reference is sufficiently defined at Product level to proceed to later Product-amendment drafting after the cross-capability pressure test is complete.

Current accepted principles include:

- every successfully created individual Account receives a human-facing Platform Member Reference;
- the reference identifies the Account, not paid membership or entitlement;
- the reference is non-secret but private-by-default;
- it provides no authentication or authorisation power;
- it is unique, normally immutable and never reused;
- it may identify beneficiaries in checkout/gifting workflows;
- beneficiary-linked benefits may be honoured when another purchaser pays, subject to authoritative eligibility;
- lookup reveals only the minimum information necessary;
- final deletion followed by genuinely new registration yields a new reference;
- duplicate Account merge leaves one active canonical reference and retires the other;
- authorised staff may use it as a lookup key without bypassing permissions;
- display/use is purpose-driven;
- exceptional replacement is permitted only through a governed narrow process;
- Product Law specifies human usability and non-semantic requirements, not the exact encoding;
- `VG-K7M-4P9-X` remains a preferred implementation candidate for later validation, not frozen Product Law.

No exact field name, schema, Ash Resource, prefix, alphabet, check algorithm, generator or persistence implementation is approved here.

---

# Cross-Capability Pressure Test

**Status:** IN PROGRESS

## P1 — Research poll versus governed vote

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Classification follows approved purpose and consequence, not the UI widget.

A poll whose purpose is to learn participant opinion remains Research/Feedback truth.

A vote whose result participates in an official governed business outcome follows the applicable Voting/business-process rules.

A reusable poll/voting UI component does not create shared business authority.

**Status:** APPROVED

---

## P2 — Anonymous participation versus duplicate prevention

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

The platform must not claim a stronger uniqueness guarantee than the approved identity mode can support.

Anonymous/public participation may use proportionate duplicate and abuse controls.

Those controls do not create a verified one-person-one-response or one-human-one-vote guarantee unless the identity model genuinely supports that promise.

This applies consistently across Research/Feedback and Voting.

**Status:** APPROVED

---

## P3 — Research response versus health/safety duty

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Research/Feedback does not acquire Health Records or Safety & Eligibility authority merely because a response concerns health or safety.

An instrument may explicitly define a governed safety/follow-up/escalation pathway.

When such a pathway exists, the owning Health/Safety capability independently evaluates and establishes authoritative truth.

Where no monitoring/escalation promise exists, the platform must not imply that general research or free-text feedback is continuously clinically monitored.

**Status:** APPROVED

---

## P4 — Interactive-tool result versus research response

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Interactive-tool inputs/results and Research/Feedback responses remain distinct truth according to their approved purpose.

Data does not become research evidence merely because an interactive tool collected a similar field.

Likewise, Research/Feedback responses do not automatically become interactive-tool or authoritative operational inputs.

Cross-purpose reuse requires an explicit governed basis.

**Status:** APPROVED

---

## P5 — Platform Member Reference in public voting/research

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

A Platform Member Reference must not be required merely to participate in an approved anonymous/public voting or research activity unless the specific Product purpose genuinely requires Account-linked participation.

Public Nuwe Jy-style voting therefore remains possible without Account creation or a member reference.

Where a member reference is used, it identifies an Account; it does not itself authenticate the voter or respondent.

**Status:** APPROVED

---

## P6 — Platform Member Reference and subscriber benefits at checkout

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

In an approved checkout/gifting flow:

```text
member reference
→ identifies intended beneficiary

authoritative membership/entitlement capability
→ determines current benefit eligibility

Commerce
→ applies the valid commercial effect
```

Knowing another person's Platform Member Reference does not transfer that person's benefits to the purchaser outside the benefit's Product rules.

The reference must never become a pseudo-coupon or entitlement credential.

**Status:** APPROVED

---

## P7 — Account deletion versus retained research/votes

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Account closure or deletion does not automatically invalidate historically legitimate Research/Feedback responses or votes.

Retention, de-identification, withdrawal and deletion follow the rules of the originating capability together with applicable Privacy/Consent requirements.

A valid historical competition result does not change merely because a voter later closes or deletes an Account.

Identity linkage must not survive longer than its approved purpose, policy or law justifies.

**Status:** APPROVED

---

## P8 — Analytics, dashboards, leaderboards and reports remain derived

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Analytics, dashboards, leaderboards, reports and projections may derive and present information from authoritative sources, but do not become the authoritative owner of the underlying business truth.

Examples:

```text
accepted votes → governed voting/result authority
leaderboard → derived presentation
```

```text
research responses → Research/Feedback authority
research dashboard → derived presentation
```

```text
membership/entitlement truth → owning capability
checkout eligibility display → derived presentation
```

If a projection is incorrect, the projection is corrected. Source business truth is not silently rewritten merely to match a derived view.

**Status:** APPROVED

---

## P9 — Incentives, prizes and rewards do not move authority

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Research/Feedback or Voting/Competition may establish that an approved participation or result condition occurred.

They do not directly manufacture authoritative:

- payment;
- voucher;
- discount;
- entitlement;
- commercial reward;
- prize-fulfilment

truth.

The owning Commerce/Entitlements or other applicable capability performs the separately governed commercial/benefit action.

This allows reward fulfilment to fail, retry or reconcile without changing the underlying research participation or official competition result.

**Status:** APPROVED

---

## P10 — Existing wellness/competition safety restrictions remain controlling

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

The new governed Voting / Balloting / Competitions capability does not supersede or weaken existing wellness and safety Product restrictions.

Governed voting mechanics do not silently authorise unsafe or prohibited competition models.

Existing restrictions on unsafe public weight, calorie-restriction, body-measurement, weight-led or otherwise prohibited competitive comparison remain controlling unless separately amended at the proper Product authority level.

The voting system governs how an already-permitted competition operates; it does not decide whether the underlying competition is Product-safe.

**Status:** APPROVED

---

## P11 — Public interactive tools do not weaken privacy/safety requirements

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Public availability is an access mode, not a weaker privacy or safety mode.

A public interactive tool must:

- minimise sensitive inputs;
- make its purpose appropriately clear;
- avoid persistence by default;
- preserve the same authority boundaries as Account-linked tools.

Where identity, longitudinal history, sensitive authoritative action or stronger governance is genuinely required, an Account-linked/governed experience should be used instead.

**Status:** APPROVED

---

## P12 — Shared interaction primitives do not create universal Engagement authority

### Accepted recommendation

**APPROVED CROSS-CAPABILITY RULE**

Shared forms, questions, polls, voting components, calculators, dashboards or other interaction primitives do not imply shared business ownership.

Authority follows the durable truth, lifecycle and Product purpose.

A reusable UI or implementation primitive may serve multiple owning capabilities without becoming an authoritative cross-platform "Engagement" owner.

No Engagement Domain is approved by this Grill.

**Status:** APPROVED

---

# Cross-Capability Pressure Test — Closure Status

**STATUS: COMPLETE / PASS**

The pressure test found no blocking Product contradiction across the four approved amendment areas and existing Product boundaries.

The following are explicitly reconciled:

- Research polls versus governed voting;
- anonymity versus uniqueness guarantees;
- Research/Feedback versus Health/Safety authority;
- Interactive Tools versus Research purpose;
- public voting/research versus Account/member-reference requirements;
- member reference versus subscriber/discount authority;
- Account deletion versus historical research/voting truth;
- Analytics/dashboard/leaderboard projection versus authority;
- incentives/prizes versus commercial/entitlement authority;
- governed competitions versus existing wellness-safety restrictions;
- public tools versus sensitive-data minimisation;
- reusable interaction primitives versus Domain ownership.

Remaining questions are downstream classification, Domain ownership, sequencing, Architecture, JIT or implementation decisions rather than blockers to drafting the Product amendment.

---

# Final Product Amendment Decision Set

**Status:** COMPLETE / APPROVED WORKING DECISION SET  
**Authority:** NON-AUTHORITATIVE WORKING INPUT ONLY  
**Baseline reviewed:** live `main` at `ad71191b17b297ac9dc683c18141e1c546fa9850`

No governed identifiers are created by this working document.

## A. Existing Product Law Preserved

The targeted amendment does not reopen or weaken existing Product Law outside the approved scope.

Preserved boundaries include:

- current MVP scope and launch sequencing remain unchanged unless later Roadmap work explicitly amends sequencing;
- purchaser, recipient, participant and Account-holder remain distinct concepts;
- existing Health Records, Safety & Eligibility, Plans, Temperament, Commerce and Entitlements retain their authoritative business-truth boundaries;
- Analytics remains derived rather than authoritative;
- privacy/safety obligations continue to apply to sensitive data regardless of UI/access mode;
- existing wellness and competition-safety restrictions remain controlling;
- public interaction does not automatically require an Account;
- provider/UI/cache/projection state does not become business authority merely because it displays or computes something.

## B. Newly Approved Product Decisions

### B1. Research & Feedback

The mature platform supports two bounded modes:

1. lightweight interaction/feedback;
2. governed structured research campaigns.

Approved principles include:

- Research/Feedback is not a generic survey-platform commitment;
- identity mode is explicit per instrument/campaign: Account-linked, pseudonymous or anonymous where appropriate;
- identity mode and uniqueness guarantee are separate Product promises;
- Research/Feedback responses remain Research/Feedback truth;
- responses do not directly mutate Health Records, Safety & Eligibility, Plans, Temperament, Commerce or Entitlements;
- downstream authoritative actions must be separately governed by the owning capability;
- persisted instrument/question versions remain tied to submitted responses;
- published governed instrument versions are immutable in meaning;
- anonymous responses cannot promise later individual withdrawal where no identifying linkage exists;
- sensitive/health-related research is permitted only under an approved purpose and stronger privacy/safety boundary;
- Account-linked structured research normally supports appropriate participant visibility;
- incentives are permitted but fulfilled through owning commercial/entitlement authority;
- purpose-limited cohort targeting is permitted without transferring source-data ownership;
- longitudinal research is supported where the identity mode permits it;
- approved aggregate/authorised publication of findings is permitted;
- explicit follow-up/escalation pathways may exist without creating a universal monitoring promise;
- correction/finality rules are campaign-specific and preserve history where needed;
- withdrawal/deletion may distinguish future use, identity linkage, retained evidence and already-published aggregates;
- Account closure does not automatically erase otherwise valid research truth;
- staff annotations/review notes remain distinguishable from participant-submitted truth.

### B2. Voting / Balloting / Competitions

The mature platform supports:

1. lightweight opinion polls;
2. Research-governed polls;
3. contextual governed voting/balloting, including competition voting.

Approved principles include:

- the platform is not a general-purpose civic election system;
- public unauthenticated voting is a legitimate governed mode;
- Nuwe Jy-style public supporters do not require Accounts merely to vote;
- public unauthenticated voting does not promise verified one-human-one-vote;
- vote eligibility, identity mode, limits, correction/finality and open/close rules are explicit;
- exact tally visibility is configurable;
- leaderboards/ranked aggregate views may be configured without exposing individual voter choices;
- proportionate anti-abuse controls are required;
- automated voting, bots, scripts, vote farms, fabricated submissions and deliberate circumvention are prohibited;
- submitted, accepted, rejected/invalidated and review-required concepts may be distinguished;
- a tally is distinct from the official governed result where finalisation applies;
- governed competitions define tie, disqualification, outage/integrity-failure, cancellation/re-run and adjudication rules before finalisation;
- legitimate campaigning/inviting supporters is permitted where competition rules allow it;
- provisional post-close review may precede final result;
- operator adjudication is permitted only under governed, explainable rules;
- winner/result truth is separate from reward/entitlement fulfilment.

### B3. Interactive Tools / Calculators / Decision Aids

The mature platform supports approved:

- educational calculators;
- interactive articles;
- quizzes/self-assessments;
- decision aids;
- progress visualisations;
- interactive planning tools;
- personalised Account-linked tools;
- dashboards and related interactive views.

Approved principles include:

- the platform is not a general-purpose arbitrary no-code execution environment;
- calculation is not authority;
- authoritative changes remain with the owning capability;
- public/anonymous tool inputs/results are ephemeral by default;
- persistence requires clear Product value and participant purpose/expectation;
- persisted or materially consequential results are version-bound;
- health/safety-sensitive tools are permitted under stronger governance while preserving owning-capability authority;
- personalised tools may consume existing platform truth under minimisation/purpose limits without taking ownership;
- public, Account-gated and entitlement-gated tools are all legitimate access modes;
- tools may initiate approved downstream workflows without owning the resulting authoritative truth;
- explainability is proportionate to consequence;
- dashboards/visualisations remain derived presentations;
- staff may configure approved bounded tool types/content/parameters;
- arbitrary executable CMS formulas/scripts are not a Product promise;
- correction/recalculation is supported without falsifying historical meaning.

### B4. Platform Member Reference

Every successfully created individual Account receives a stable human-facing Platform Member Reference.

Approved principles include:

- mere newsletter contacts, anonymous visitors/voters/respondents and uncreated recipient identities do not receive one merely by appearing in platform data;
- the reference identifies an Account for human-facing use;
- it does not represent paid membership, subscription, entitlement, authentication, authorisation, identity-verification level or database identity;
- it is non-secret but private-by-default;
- possession of the reference confers no Account authority;
- it is unique, normally immutable and never reused;
- legitimate reactivation of the same Account retains its reference;
- final deletion followed by genuinely new Account creation yields a new reference;
- duplicate Account reconciliation leaves one canonical active reference and permanently retires the other;
- authorised staff may search by member reference without bypassing permissions;
- the reference may be used in appropriate support, communication, event, checkout/gifting and beneficiary-identification workflows;
- checkout lookup exposes only the minimum information required;
- beneficiary-linked subscriber benefits may be honoured when another purchaser pays specifically for that beneficiary;
- the reference itself never proves benefit/discount/entitlement eligibility and must not become a pseudo-coupon;
- exceptional replacement is allowed only through a governed security/privacy/integrity/reconciliation process;
- Product-level format requirements emphasise human readability, shortness, transcription resistance, non-semantic content, non-obvious sequentiality, error detection and adequate namespace size.

Preferred implementation candidate retained for later validation only:

```text
VG-K7M-4P9-X
```

The literal `VG` prefix is not approved as durable Product Law because of brand-coupling risk.

## C. Explicit Deferrals

The following are intentionally deferred:

- whether Research & Feedback merits a new Domain;
- exact Voting ownership by context;
- exact Interactive Tool ownership by durable truth affected;
- detailed Platform Member Reference lifecycle implementation;
- exact research retention periods;
- exact anonymity/pseudonymisation mechanisms;
- exact voting identity assurance mechanisms;
- exact anti-abuse thresholds and controls;
- exact competition review windows;
- exact leaderboard presentation;
- exact calculator/tool execution architecture;
- exact tool/configuration model;
- exact member-reference format and generation algorithm;
- exact commercial terms of future benefits beyond the approved beneficiary-linked principle;
- exact Roadmap sequencing of mature capabilities.

## D. Rejected / Out-of-Scope Product Commitments

This Grill explicitly rejects or does not approve:

- a general-purpose SurveyMonkey/Typeform-style survey platform;
- a general-purpose civic election/ballot platform;
- a generic arbitrary no-code/script/formula execution environment;
- an automatic new Voting Domain;
- an automatic new Interactive Tools Domain;
- a universal Engagement Domain merely because UI primitives are shared;
- mandatory Account creation for approved public Nuwe Jy-style voting;
- claims of verified one-human-one-vote for public unauthenticated voting;
- silently treating Research responses as Health/Safety/Plan/Temperament truth;
- silently treating calculator output as authoritative business truth;
- using the Platform Member Reference as authentication, authorisation, entitlement or discount credential;
- encoding PII, health state, geography, paid status or other business semantics into the member reference;
- routine vanity replacement of member references;
- public disclosure of individual voter choices by default;
- unsafe competition mechanics prohibited by existing Product Law;
- arbitrary executable administrator code/formulas merely for configurability.

## E. Still-Open Product Decisions

**No Product decision currently remains open that blocks Stage 2 drafting.**

Context-specific policies may still be set by future Product work when a concrete campaign, competition, benefit or tool requires them.

Those contextual choices do not prevent the bounded Product-law amendment from being drafted now.

## F. Candidate Downstream AR-000 Product-Law Consequences

These are candidate Product-derived Architecture requirement areas only. No ARQ identifiers are created here.

Potential downstream requirement areas include:

- explicit participation identity modes and truthful uniqueness guarantees;
- versioned/immutable published research instruments with response provenance;
- preservation of Research/Feedback authority boundaries;
- explicit cross-domain mutation boundaries for research/tool-triggered actions;
- governed public unauthenticated voting with proportional integrity controls;
- distinction between submitted/accepted voting activity, tally and official result;
- governed finalisation and operator-adjudication evidence;
- configurable tally/leaderboard visibility without voter-level disclosure;
- separation of official competition result from commercial reward fulfilment;
- version-bound consequential interactive-tool results;
- privacy-minimising public interactive tools;
- authoritative-owner enforcement for health/safety/plan-affecting interactive actions;
- Platform Member Reference uniqueness, normal immutability, non-reuse, minimum disclosure and non-authority properties;
- governed retirement/reconciliation of duplicate member references;
- beneficiary identification at checkout without transferring entitlement authority.

Errors & Diagnostics, Observability, Native Compute/Rustler and Engineering Quality remain separate Stage 3B inputs and are not Product-derived AR-000 material merely because this amendment programme exists.

## G. Domain Questions for Later Stage 7

The later Domain pressure test must independently determine:

- whether Research & Feedback has sufficiently distinct durable truth/lifecycle/invariants to justify an independent Domain;
- whether Voting/Competition truth belongs contextually to Programmes, Community, Events, Research or another owner rather than a universal Voting Domain;
- which owning Domain controls consequential Interactive Tool results/actions;
- whether Platform Member Reference is fully owned by Identity & Access as currently expected or exposes a contradiction requiring upstream resolution;
- how staff annotations, competition finalisation and reconciliation evidence map to owning Domains/Audit without shared-write ownership.

This working document does not decide those questions.

## H. Roadmap Questions for Later Stage 8

The later Roadmap Sequencing Grill should decide:

- when lightweight Research/Feedback becomes valuable enough to schedule;
- when governed research campaigns are warranted;
- when structured public voting should replace the current Nuwe Jy form-based process;
- whether voting mechanics should arrive with the Product context that first requires them;
- when public/personalised interactive tools become product priorities;
- which interactive-tool types are justified first;
- how the Platform Member Reference should be reconciled into FP-001 because Account creation is already in that Feature Pack;
- whether any mature capabilities belong in existing later Feature Packs versus a future roadmap amendment.

No new Feature Pack identifier is created here.

## I. Implementation Decisions Explicitly Deferred

Deferred implementation detail includes:

- Ash Resources/actions;
- schemas/tables/columns;
- indexes and constraints;
- API shapes;
- exact states/enums;
- exact retention jobs;
- identity/pseudonymisation/anonymisation technology;
- rate-limit numbers/windows;
- IP/device/cookie/CAPTCHA/fingerprinting strategy;
- fraud-scoring mechanisms;
- leaderboard caches/projections;
- calculation engines;
- package/provider choices;
- admin configuration representation;
- member-reference field name;
- `VG` or other prefix;
- alphabet;
- payload length;
- check-character algorithm;
- generation/randomness algorithm;
- collision handling;
- database identifier relationship;
- UI components.

## J. Likely Product-Law Artifact Impact

Subject to Stage 2 authority review, the amendment will likely require successor Product-law evidence primarily in:

- `docs/00_platform/00_PLATFORM_*` for mature capability law and cross-cutting Product invariants;
- `docs/00_platform/01_DECISIONS_*` where the existing governance requires accepted Product decisions to be recorded;
- `docs/00_platform/02_OPEN_WORK_*` to truthfully record the amendment trigger/programme state and downstream sequencing.

`PROJECT_NORTH_STAR_AND_MVP_*` should be amended only if Stage 2 proves that an accepted rule changes North Star/MVP law rather than merely adding mature-platform capability.

The current Platform Member Reference affects FP-001 later, but does not by itself authorise editing FP-001 during Stage 2.

Exact successor filenames/versions must follow current repository SemVer/governance rather than being invented by this working record.

## K. Final Readiness Verdict

**PASS**

The targeted Product Amendment Grill is complete.

The accepted Product decisions are sufficiently specific to draft a bounded Stage 2 Product Law amendment without requiring Architecture, Domain Map, Roadmap or implementation to invent missing Product semantics.

No blocking Product contradiction remains.

### Mandatory next boundary

Stage 2 may draft the Product amendment.

Stage 2 must not:

- create ARQs;
- perform AR-000 delta analysis;
- classify independent Architecture/Engineering inputs;
- amend Architecture;
- assign new Domain ownership;
- amend Roadmap;
- modify FP-001 implementation artifacts;
- run HARDEN-02;
- implement any capability.

Human/review approval of the Stage 2 Product amendment remains mandatory before Stage 3A.1.

---

# Working Document Changelog

## v0.5.0

Minor version: Targeted Product Amendment Grill completed.

Includes:

- approved cross-capability pressure-test rules P7–P12;
- cross-capability pressure-test closure as `COMPLETE / PASS`;
- consolidated Final Product Amendment Decision Set;
- explicit preserved law, approved decisions, deferrals, rejected scope and downstream questions;
- candidate Product-derived AR-000 consequence areas without governed ARQ identifiers;
- final Stage 1 readiness verdict: `PASS`;
- Stage 2 boundary and mandatory stop conditions.

This remains a non-authoritative working input until a governed Product Law amendment is approved and merged.

## v0.4.1

Patch update during the cross-capability pressure test.

Includes approved pressure-test rules P1–P6 covering:

- research polls versus governed voting;
- anonymity versus uniqueness guarantees;
- research versus health/safety authority;
- interactive tools versus research purpose;
- public voting/research versus Platform Member Reference requirements;
- Platform Member Reference versus subscriber benefit/discount authority.

Cross-capability pressure testing remains in progress.

## v0.4.0

Minor version: Round D completed.

Includes:

- Platform Member Reference Q1–Q12 fully approved;
- staff lookup without permission bypass;
- purpose-driven participant-facing display/use;
- governed exceptional retirement/replacement;
- Product-level human usability, non-semantic and anti-enumeration requirements;
- preferred `VG-K7M-4P9-X` representation retained as an implementation candidate only;
- Round D closure as `COMPLETE / PRODUCT DIRECTION APPROVED`.

All four main Product Grill rounds are now complete. Cross-capability pressure testing remains before final Grill closure.

## v0.3.2

Patch update during Round D.

Includes:

- approved Platform Member Reference Q5–Q8;
- beneficiary-linked subscriber benefits when another purchaser pays;
- minimum-disclosure rule for member-reference lookup;
- Account-scoped continuity across closure/reactivation, without hidden lifelong-person identity across final deletion/re-registration;
- duplicate-Account merge semantics with one surviving canonical reference and permanent retirement of the other.

Round D remains in progress.

## v0.3.1

Patch update during Round D.

Includes:

- approved Platform Member Reference Q1–Q4;
- explicit checkout/gifting use as a human-facing Account lookup/reference;
- authority boundary: member reference does not itself establish subscription, discount, entitlement, authentication or authorisation;
- open commercial-policy question for use of recipient/subscriber benefits by another purchaser;
- proposed `VG-K7M-4P9-X` format captured as a deferred implementation candidate only;
- brand-coupling warning for a permanent `VG` prefix.

Round D remains in progress.

## v0.3.0

Minor version: Round C completed.

Includes:

- Interactive Tools / Calculators / Decision Aids Q1–Q12 fully approved;
- proportionate explainability requirements;
- dashboard/visualisation projection boundary;
- bounded administrator configuration without arbitrary executable code;
- correction/recalculation semantics without falsifying historical results;
- Round C closure as `COMPLETE / PRODUCT DIRECTION APPROVED`.

Round D — Platform Member Reference remains not started.

## v0.2.2

Patch update during Round C.

Includes:

- approved Interactive Tools / Calculators / Decision Aids Q5–Q8;
- support for health/safety-sensitive tools while preserving owning-domain authority;
- purpose-limited use of existing participant data with minimisation;
- public, Account-gated and entitlement-gated access modes;
- downstream workflow initiation without transferring authoritative write ownership to the tool.

Round C remains in progress.

## v0.2.1

Patch update during Round C.

Includes:

- approved Interactive Tools / Calculators / Decision Aids Q1–Q4;
- bounded interactive-tool capability without general-purpose no-code execution scope;
- explicit `calculation != authority` Product rule;
- ephemeral-by-default input/result handling;
- purpose-driven persistence for Account-linked tools;
- version-binding and reproducibility for persisted or consequential results.

Round C remains in progress.

## v0.2.0

Minor version: Round B completed.

Includes:

- Voting / Balloting / Competitions Q1–Q12 fully approved;
- configurable public/hidden aggregate visibility;
- optional contestant/option leaderboards without exposing individual voter choices;
- legitimate public campaigning and supporter invitations;
- explicit prohibition of bots, scripts, vote farms and deliberate circumvention;
- provisional post-close integrity review before final result where applicable;
- governed operator adjudication with explainable reasons;
- Round B closure as `COMPLETE / PRODUCT DIRECTION APPROVED`.

Round C — Interactive Tools / Calculators / Decision Aids remains not started.

## v0.1.2

Patch update during Round B.

Includes:

- approved Voting / Balloting / Competitions Q5–Q8;
- configurable tally/result visibility, including hidden competition tallies and optional live poll visibility;
- Product requirement for proportionate anti-abuse controls while deferring exact rate-limit thresholds/mechanisms to Architecture/JIT;
- governed invalidation/review concepts;
- predeclared tie, cancellation, disqualification and integrity-failure treatment;
- explicit separation of official competition result from reward/entitlement fulfilment.

No Round B closure is declared yet.

## v0.1.1

Patch update during Round B.

Includes:

- approved Voting / Balloting / Competitions Q1–Q4;
- explicit approval of public unauthenticated Nuwe Jy-style voting;
- distinction between integrity controls and verified one-human-one-vote identity;
- distinction between raw/accepted tally and governed official result;
- current Nuwe Jy form-based voting context and future governance objective.

No Round B closure is declared yet.

## v0.1.0

First SemVer-tracked working version.

Includes:

- Stage-1 scope and non-authoritative boundary;
- Research & Feedback Q1–Q16;
- all accepted Product recommendations through Round A;
- Round A closure as `COMPLETE / PRODUCT DIRECTION APPROVED`;
- placeholders for Voting / Balloting / Competitions;
- Interactive Tools / Calculators / Decision Aids;
- Platform Member Reference;
- cross-capability pressure test;
- final Product Amendment Decision Set.

The prior unversioned file is treated as a bootstrap draft only and is not part of the SemVer history.
