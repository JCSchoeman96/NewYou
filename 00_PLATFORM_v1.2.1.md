# 00_PLATFORM.md

- **Document status:** FROZEN PRODUCT BASELINE v1.2.1
- **Authoritative for:** Platform purpose, product direction, users, commercial model, personalisation principles, clinical boundaries, membership direction, community direction, ownership intent, and platform-wide non-negotiables
- **Not authoritative for:** Ash resources, database schemas, technical architecture, implementation sequencing, pricing implementation, or legal advice
- **Current operating entity:** Provisionally Voelgoed Media
- **Possible future structure:** A new dedicated company may be created
- **Initial market:** Adult women, 18+
- **Last updated:** 2026-08-16
- **Decision coverage:** GQ-001 through GQ-012 plus GQ-NY-001 + approved post-freeze DEC-292–DEC-293 amendments
- **Related documents:** `01_DECISIONS_v1.2.1.md`, `02_OPEN_WORK_v1.2.1.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md`

---

## v1.2.1 Patch Scope

This is a **non-semantic current-state reference hygiene patch**. It does not add, remove, reopen, weaken or supersede any Product Law decision. The v1.2 amendments remain authoritative and the v1.2 text is preserved as the immediately preceding version.

The patch only corrects stale current-state version/provider wording and related-document metadata so the active pack describes its own v1.2.1 state consistently. Historical v1.0/v1.1/v1.2 amendment text remains intentionally preserved where it describes earlier states.

## v1.2 Amendment Scope

This v1.2 amendment preserves the v1.1 Product Law baseline and records two deliberately approved post-freeze business/platform decisions discovered during AR-000:

1. **Paystack is locked as the first / launch payment gateway** for the initial South African/ZAR launch rather than remaining a provisional provider choice. Provider behaviour such as retries, subscriptions, webhooks, refunds, disputes and proration remains subject to the existing validation gate before implementation details are fixed.
2. **First-party A/B/n experimentation is a required platform capability** for governed page/web and eligible email/message experiments. The platform must preserve clean/canonical URLs, stable randomised assignment, governed exposure/metric/statistical evidence, privacy/deletion boundaries, protected Product Law invariants and durable historical experiment decisions.

This amendment does **not** change the ultimate participant outcome, clinical model, MVP product catalogue, safety boundaries, entitlement truth, accounting authority or the principle that Analytics is downstream of authoritative business state. It adds a governed optimisation/learning capability and promotes the already-selected launch payment provider from provisional to locked.

The v1.1 planning-governance and realtime-authority corrections remain in force.

### Preserved v1.1 amendment history

The v1.1 amendment aligned downstream architecture and delivery governance with the approved post-freeze planning method. Its governance changes remain effective and are not repeated as new v1.2 decisions.

## v1.1 Amendment Scope (preserved historical text)

This v1.1 amendment aligns downstream architecture and delivery governance with the approved post-freeze planning method.

It does **not** reopen or alter the product model, commercial model, clinical boundaries, participant journeys, MVP scope, launch sequence or DEC-001 through DEC-291.

The substantive governance changes are limited to:

- clarifying the two-depth performance/scaling review required by OQ-039;
- recognising a lightweight Domain Architecture Profile for every mapped domain before Roadmap sequencing;
- requiring implementation-grade Domain Dossiers just in time for the affected Feature Pack and implementation slices;
- aligning the implementation hard stop with Feature Pack, architectural-proof and slice planning;
- removing the preselected GenServer-before-durability ordering for high-velocity writes and replacing it with an explicit authority, confirmation-boundary and crash-safety invariant.

---

# 1. Platform Purpose

The platform exists to become the leading Christian, temperament-guided holistic health and wellness ecosystem, initially for women.

It will combine:

- evidence-informed nutrition and lifestyle guidance;
- the Four-Colour Temperament Model™;
- personalised self-guided eating and lifestyle plans;
- emotional and behavioural insight;
- practical habit formation;
- Christian faith and identity;
- recurring membership;
- community, challenges, live streams and events;
- and, later, professionally reviewed services involving qualified dietitians, doctors, psychologists and other appropriate professionals.

The platform must help each woman understand how she is naturally wired, recognise the physical, emotional, behavioural and spiritual factors affecting her health, and build a sustainable way of living around who she already is.

The central promise is:

> You do not need to become a different woman to become a healthier woman. You need to understand the woman you already are, work wisely with your strengths, and build support structures around your vulnerabilities.

The platform is not intended to become merely:

- a diet application;
- a calorie tracker;
- a meal-plan generator;
- a personality quiz;
- an AI health chatbot;
- a generic membership site;
- or an event platform.

Those may become supporting capabilities, but none of them defines the full product.

---

# 2. Ultimate End State

The long-term goal is a complete temperament-based lifestyle ecosystem and community that supports the full participant journey:

```text
Discover herself
→ understand her temperament and patterns
→ identify relevant health barriers
→ receive suitable guidance
→ follow a realistic eating and lifestyle plan
→ build sustainable habits
→ recover after setbacks
→ track meaningful progress
→ join challenges and community experiences
→ attend events and live sessions
→ receive professional support where required
→ maintain long-term health and consistency
```

The mature platform may include:

- free public educational content;
- paid digital temperament assessments;
- temperament reports and introductory guidance;
- repeatable seven-day eating plans;
- longer premium plans;
- multi-week foundation programmes;
- personalised member content feeds;
- monthly plan reviews and adjustments;
- live streams and group Q&A;
- moderated community;
- health and lifestyle challenges;
- event access and member benefits;
- practitioner-reviewed plans;
- professional referrals;
- a future practitioner network;
- and later, a separate product experience for men on the same technical platform.

The women-first product must remain coherent even if the technical foundation is later reused for other markets.

---

# 3. Source and Method Foundation

The platform is grounded in the book and its core message that health cannot be reduced to food or weight alone.

The source material treats sustainable health as an interaction between:

- physical health;
- nutrition;
- body composition and measurements;
- blood markers and possible physiological barriers;
- sleep;
- energy;
- stress;
- emotional hunger;
- trauma and emotional wounds;
- self-talk and limiting beliefs;
- faith, grace and identity;
- movement;
- habits;
- and temperament-specific strengths and vulnerabilities.

The Four-Colour Temperament Model™ must be treated as a reflective self-awareness and behaviour-guidance tool, not as a clinical personality assessment or medical diagnosis.

A participant may have a dominant and secondary temperament. The platform must support mixed profiles and must not reduce a person to a single rigid label.

The temperament model may influence:

- communication style;
- plan presentation;
- degree of structure;
- number of choices;
- reminder style;
- accountability strategy;
- lesson ordering;
- response to setbacks;
- challenge format;
- and the type of support most likely to help the participant remain consistent.

Temperament must never override medical safety, nutritional evidence or professional judgement.

---

# 4. Initial Audience and Future Expansion

## 4.1 Initial audience

The initial commercial audience is individual adult women reached through:

- the physical book;
- live events;
- existing media and social platforms;
- public educational content;
- referrals from readers and attendees;
- and later, the member community.

The platform will not initially target health professionals as its primary commercial customer.

## 4.2 Age

The initial platform is for adults aged 18 and older.

Parent-and-child or family participation may be explored in the future, but minors are explicitly excluded from the initial product and account model.

## 4.3 Account model

Only individual accounts will be supported initially.

Household accounts, parent-managed dependant profiles and shared family profiles are not part of the first product.

## 4.4 Future men’s product

The underlying platform may later support men, but through a separate product and content experience.

The initial brand, content, journeys and clinical assumptions remain women-first.

---

# 5. Product Positioning

The platform should be positioned as:

> A temperament-guided women’s health and lifestyle ecosystem that helps each woman understand herself, receive relevant guidance, and build sustainable habits around her real life.

The product must lead with:

- health;
- consistency;
- energy;
- sustainable change;
- a healthier relationship with food and body;
- emotional freedom;
- personal agency;
- and faith-centred identity.

Fat loss may be an appropriate outcome for some participants, but it is not the universal or sole outcome.

When measurements indicate that a participant should not lose weight, the platform must not provide a weight-loss plan.

The platform must not use shame, fear or perfectionism as its primary behaviour-change mechanism.

---

# 6. Faith Position

The platform will be openly Christian and available to everyone.

Faith-centred content is part of the product identity and will not be removed through a configurable faith-free version.

The platform may include:

- Scripture;
- prayer;
- devotional material;
- Christian identity and grace;
- stewardship of the body;
- faith-based live sessions;
- and church or faith-community experiences.

The Christian identity must be clear before a person purchases or joins a programme.

The platform must not claim that prayer replaces qualified medical, psychological or dietetic care.

---

# 7. Commercial Model

## 7.1 Commercial ladder

The current intended product ladder is:

```text
PUBLIC VISITOR
Free educational content
Book and event information
        ↓
REGISTERED FREE USER
Saved content
Preferences
Personalised public-content feed
        ↓
ASSESSMENT CUSTOMER
Paid digital temperament assessment
Temperament report
Introductory personalised guidance
        ↓
STANDARD PLAN CUSTOMER
Repeatable seven-day self-guided plan
Temperament-specific presentation
        ↓
BASIC MEMBER
Moderated community
Monthly member content
Monthly live stream
Group Q&A submission
        ↓
PREMIUM MEMBER
Longer plans
Monthly plan review and adjustment
Deeper personalisation
Foundation programme
        ↓
PRACTITIONER-REVIEWED CUSTOMER
Paid professional review
Clinically relevant adjustments
Complex health support
```

## 7.2 Public content

Generic educational content will be freely available.

A visitor should be able to read public articles without creating an account.

Public content may include:

- nutrition;
- sleep;
- movement;
- emotional eating;
- stress;
- self-talk;
- faith;
- health education;
- and temperament-informed general guidance.

## 7.3 Free account and multilingual entry

A person may create a free account without purchasing anything.

A person may also join the public mailing list without creating a full account.

Required registration information is:

- first name;
- surname;
- email address;
- authentication credential;
- preferred interface language;
- confirmation that the user is 18 or older;
- acceptance of the applicable terms and privacy notice.

Optional registration information is:

- phone number;
- city.

A preferred-name field is not required.

Full date of birth, life-stage information, health information and medical information are collected later only when required for a defined product, safety or personalisation purpose.

The platform supports Afrikaans and English from launch.

On first entry, the visitor is asked to choose Afrikaans or English. Before registration, this choice is stored locally. After registration or login, it is saved to the user profile. A language control in the header allows switching at any time.

Interface language and content language remain distinct. A user may use one interface language while deliberately opening content in the other language.

## 7.4 Digital temperament assessment

The digital assessment is a paid product.

It may be purchased without buying the physical book.

The assessment purchase includes:

- completion of the digital assessment;
- a temperament result report;
- primary and secondary temperament guidance;
- and introductory personalised guidance.

It does not automatically include the full standard seven-day plan unless sold through a specific bundle.

## 7.5 Physical book access

The standard physical book does not automatically grant digital access.

Different book or event bundles may provide different digital entitlements, such as:

- assessment access;
- plan access;
- limited membership;
- event-linked resources;
- or premium bundles.

Bundle access should be granted through unique entitlements or redemption codes.

## 7.6 Standard seven-day plan

The standard plan is:

- self-guided;
- repeatable weekly;
- temperament-specific in format and presentation;
- available as a once-off purchase;
- and potentially included in selected memberships or bundles.

The plan is not a once-off promise of transformation. It is an immediate practical starting point.

## 7.7 Premium membership

Premium membership may include:

- longer plans;
- more meal options or greater structure;
- different meal-frequency options;
- deeper personalisation;
- monthly plan review and adjustment;
- a structured multi-week foundation programme;
- additional premium content;
- and access to premium challenges or tools.

A monthly review may legitimately conclude that no plan change is needed.

Human review is not guaranteed merely because a person is a premium member.

## 7.8 Practitioner-reviewed service

Human clinical review is a separate paid service.

It may include:

- dietitian review;
- doctor involvement when medically necessary;
- complex allergy review;
- medication-related considerations;
- abnormal blood-result review;
- clinical supplementation guidance;
- and more complex personalised support.

The service will be introduced only after the automated plan has been validated.

It should initially be offered to a limited number of customers to protect professional capacity and validate the review workflow.

---

# 8. Membership Model

## 8.1 Basic membership guarantees

Basic membership will guarantee:

1. access to a moderated member community;
2. at least one new or expanded member content release per month;
3. at least one live stream per month;
4. the ability to submit questions for moderated group Q&A.

Additional benefits may include:

- challenges;
- priority event notifications;
- event discounts;
- selected VIP access;
- and member-only resources.

These additional benefits should not be marketed as guaranteed monthly benefits unless the platform can reliably deliver them.

## 8.2 Premium membership guarantees

Premium membership is intended to include:

- all basic membership benefits;
- deeper personalisation;
- longer or more detailed plans;
- a monthly plan review;
- approved automatic plan adjustments;
- and access to the future foundation programme.

The monthly review contract is now governed by the locked GQ-003 and GQ-006 rules:

- a complete check-in is required;
- reviews do not accumulate indefinitely;
- an unchanged plan counts as a completed review;
- approved minor changes may be automated;
- professional review remains a separate service;
- exact submission timing, grace periods and clinically approved adjustment thresholds remain expert/product gates.

## 8.3 Q&A scalability

Basic membership does not guarantee individual clinical answers from Venessa.

The scalable model is:

- members submit questions;
- questions are moderated and grouped;
- recurring questions are answered in live sessions;
- approved answers may become reusable content;
- and private individual advice requires a separate paid practitioner service.

---

# 9. Community Model

The community is a core long-term capability, but it will not be built into the platform immediately.

The launch sequence is:

```text
Initial community on Facebook
→ validate engagement and moderation requirements
→ build trained moderation capability
→ define migration criteria
→ later introduce first-party platform community
```

The Facebook group is a launch and validation channel, not the permanent source of truth.

Members must be warned not to post:

- laboratory reports;
- diagnoses;
- medication lists;
- detailed trauma histories;
- private consultation requests;
- or other highly sensitive personal health information.

The future platform community may include:

- private groups;
- challenges;
- moderated discussions;
- live sessions;
- shared wins;
- accountability;
- event groups;
- and temperament-informed community experiences.

It must not include:

- public weight rankings;
- competitive restriction;
- unmoderated medical advice;
- public trauma disclosure pressure;
- or uncontrolled health misinformation.

---

# 10. Personalisation Model

The platform will use approved participant information to prioritise and adapt relevant guidance.

Personalisation may consider:

- temperament profile;
- goals;
- preferences;
- life stage;
- health context;
- food preferences;
- current plan;
- completed check-ins;
- and approved health information.

## 10.1 Content prioritisation

Public content remains discoverable by everyone.

For members, relevant content may be prioritised in a personalised feed.

Example:

> A member who has indicated that iron health is relevant may see iron-related educational content more prominently.

A member must still be able to browse other content freely.

## 10.2 Personalised content composition

The preferred model is governed, composable content:

```text
Approved base article
+ approved temperament block
+ approved life-stage block
+ approved member-relevance block
+ approved plan-explanation block
= member presentation
```

The platform should not create unrestricted AI rewrites of health articles for each member.

Every personalised content block should be:

- versioned;
- reviewable;
- explainable;
- translatable;
- independently withdrawable;
- and auditable.

## 10.3 Explainability

The platform must be able to explain:

- why content was prioritised;
- why a plan component was selected;
- which information influenced the recommendation;
- which rule or approved protocol was used;
- and whether the result was automated or professionally reviewed.

---

# 11. Plan Personalisation by Temperament

The plan should change in more than colour or visual style.

## 11.1 Yellow

The Yellow experience may include:

- more choice;
- flexible alternatives;
- simple anchors;
- social accountability;
- enjoyable challenges;
- visual motivation;
- and support when enthusiasm fades.

## 11.2 Red

The Red experience may include:

- measurable goals;
- clear targets;
- structured progress;
- sustainable pacing;
- recovery rules;
- planned rest;
- and protection against all-or-nothing behaviour.

## 11.3 Green

The Green experience may include:

- smaller steps;
- predictable routines;
- gentle activation;
- fewer disruptive changes;
- support with boundaries;
- and emphasis on self-prioritisation.

## 11.4 Blue

The Blue experience may include:

- more structure;
- greater detail;
- fewer choices;
- exact quantities where appropriate;
- clear preparation guidance;
- and deliberate flexibility to prevent perfectionism.

## 11.5 Mixed profiles

The platform must support combinations rather than simply displaying two separate generic reports.

Mixed profiles may affect:

- tone;
- plan structure;
- degree of choice;
- reminder style;
- challenge format;
- explanation depth;
- and recovery support.

---

# 12. Clinical and Safety Boundaries

## 12.1 Core principle

The platform may educate, prioritise content, generate approved plans and support healthy behaviour.

It must not automatically diagnose illness or provide individual clinical treatment beyond approved self-guided boundaries.

## 12.2 Three service levels

### Automated self-guided plan

Suitable only for participants who pass approved eligibility and safety rules.

### Premium automated plan

Suitable for members wanting more detail or configuration without clinically complex conditions.

### Practitioner-reviewed plan

Required for clinically complex or high-risk circumstances.

## 12.3 Risk-based routing

```text
Participant completes health intake
        ↓
Eligibility and safety rules evaluate the answers
        ↓
LOW RISK
Automated standard or premium pathway

MODERATE RISK
General Wellness Starter Pathway
+ recommendation for professional review

HIGH RISK
No personalised eating or weight-loss plan
+ professional review required
```

## 12.4 General Wellness Starter Pathway

This may include:

- general healthy-plate education;
- hydration;
- sleep;
- gentle movement;
- routine-building;
- emotional-awareness exercises;
- faith and identity content;
- and questions to discuss with a healthcare professional.

It must not include:

- personalised calorie restriction;
- fasting protocols;
- supplementation dosage;
- medication-related recommendations;
- blood-result interpretation;
- weight-loss targets;
- or allergy-dependent menus.

## 12.5 Professional review triggers

Professional review may be required for:

- pregnancy or breastfeeding;
- active or previous eating disorders;
- significant food allergies;
- medications requiring dietary management;
- abnormal blood results;
- diabetes treated with medication;
- recurrent fainting or dizziness;
- significant kidney, liver or cardiac disease;
- medically important symptoms;
- and complex supplementation needs.

The final eligibility matrix must be professionally approved.

---

# 13. Health Data and Blood-Test Information

The long-term platform may accept blood-test information through:

- member-entered values;
- uploaded laboratory reports;
- practitioner entry or verification;
- and future laboratory integration.

Each result must record:

- test type;
- value;
- unit;
- reference range;
- test date;
- source;
- verification status;
- reviewer;
- and review date.

Possible verification states include:

```text
member_reported
document_uploaded
practitioner_verified
laboratory_verified
expired
superseded
```

Unverified information may prioritise educational content.

It must not automatically trigger an individual clinical recommendation.

The platform may explain why an already approved plan contains a certain food or strategy, but it must not independently interpret complex blood results and invent treatment.

---

# 14. Monthly Plan Review and Adjustment

Weight alone must never trigger an automatic plan change.

A monthly plan review may consider:

- weight and measurement trend;
- time since the previous measurement;
- adherence;
- hunger and satiety;
- energy;
- sleep;
- dizziness or weakness;
- medication changes;
- pregnancy status;
- new diagnoses;
- allergies or reactions;
- participant goal;
- and whether the current plan remains appropriate.

## 14.1 Automatic minor changes

Examples may include:

- approved food substitutions;
- portion changes within approved ranges;
- changing between three and four meals;
- preference changes;
- variety changes;
- and temperament presentation changes.

## 14.2 Monthly algorithmic review

The system may recommend:

- continue the current plan;
- simplify the plan;
- progress the plan;
- increase variety;
- or request professional review.

## 14.3 Professional escalation

Professional review is required when the system detects:

- concerning symptoms;
- rapid or unexpected changes;
- medication changes;
- abnormal blood information;
- allergy concerns;
- pregnancy or breastfeeding;
- eating-disorder risk;
- or repeated intolerance of the plan.

---

# 15. Users, Actors and Roles

## 15.1 Actor model

One human identity may hold several explicit roles.

Possible roles include:

- visitor;
- mailing-list subscriber;
- registered user;
- purchaser;
- recipient;
- participant;
- customer;
- member;
- event attendee;
- community participant;
- verified contributor;
- practitioner;
- staff member;
- and platform administrator.

Roles must be:

- explicit;
- assignable;
- removable;
- scoped;
- and auditable.

## 15.2 Purchaser and participant separation

The following concepts must remain distinct:

```text
Purchaser
Recipient
Participant
Account holder
```

Paying for another person does not grant access to that person’s health information, assessment results, plan, check-ins or journal entries.

## 15.3 Staff roles

The platform expects these staff categories:

- Support;
- Finance;
- Super Admin;
- Content;
- Moderator;
- Data Analyst;
- Event Admin;
- Developer.

One person may hold several roles.

Sensitive actions must require elevated authentication and tightly scoped access.

## 15.4 Super Admin

Super Admin must not become an everyday unrestricted working role.

It should later be treated as a break-glass role with:

- strong authentication;
- reason for access;
- full auditing;
- alerts;
- and restricted assignment.

## 15.5 Venessa

Venessa may initially hold several separate roles:

- health-content author;
- clinical approver;
- programme author;
- dietitian practitioner;
- practitioner-review provider;
- live-stream presenter;
- Q&A presenter;
- platform administrator;
- and final nutrition-safety authority.

These responsibilities must remain separate role assignments even when one person holds all of them.

## 15.6 Lynette

Lynette’s initial role is community-facing rather than operational.

She may have:

- a verified profile;
- a founder or contributor badge;
- event attribution;
- stream participation;
- and community participation.

She will not initially have:

- content-management access;
- general backend access;
- assessment-answer access;
- health-profile access;
- or practitioner access.

A limited role may be added later if a real operational need arises.

## 15.7 Practitioners

The platform may later support:

- platform-employed practitioners;
- contracted independent practitioners;
- and external referral partners.

These relationships must not be treated as identical.

---

# 16. Practitioner Access to Participant Data

A practitioner may access participant information only when:

1. the participant has explicitly consented;
2. an active care or review relationship exists;
3. the access has a defined scope and expiry;
4. all access is audited;
5. the participant can revoke future access.

Revocation may end future platform access but may not erase professional records that must legally or ethically be retained.

The exact legal and professional recordkeeping obligations require expert review.

---

# 17. Data Ownership and Control

The participant is the subject of and primary controller over her personal health journey.

The operating company stores and processes her information only for:

- defined purposes;
- consented purposes;
- contractual purposes;
- legal obligations;
- and safe operation of the service.

The participant should be able to:

- access her records;
- correct appropriate information;
- export records produced about her;
- manage consent;
- and request account deletion subject to legitimate retention obligations.

The platform retains intellectual-property rights in:

- the assessment methodology;
- scoring logic;
- algorithms;
- templates;
- educational content;
- programme designs;
- and generic recommendation frameworks.

Those rights do not permit disclosure or repurposing of identifiable participant data without an authorised basis.

---

# 18. Ownership and Operating Entity

## 18.1 Current operating intention

Voelgoed Media is the provisional operating entity because it will develop and operate most of the platform.

A new dedicated company may later be created.

The final operating entity must be decided before:

- accepting production subscription payments;
- processing sensitive health data at scale;
- contracting practitioners;
- or accepting outside investment.

## 18.2 Intellectual-property intent

The current understanding is:

- Lynette contributes the Four-Colour Temperament Model™ and related methodology;
- Venessa contributes most of the health, nutrition, programme and platform knowledge;
- Voelgoed Media will likely develop and operate the software platform;
- and a formal licence or ownership agreement must define the exact rights.

The legal structure must define:

- model ownership;
- assessment ownership;
- scoring implementation rights;
- book-content rights;
- software ownership;
- platform brand ownership;
- revenue rights;
- future men’s-product rights;
- translation rights;
- exit rights;
- and the effect of forming a new company.

This document records intent only and is not legal advice.

---

# 19. Revenue and Growth Targets

## 19.1 First meaningful recurring-revenue milestone

```text
500 paying members × R200 per month
= R100,000 gross monthly recurring revenue
```

## 19.2 Five-year scale target

```text
5,000 paying members × R200 per month
= R1,000,000 gross monthly recurring revenue
= R12,000,000 gross annual recurring revenue
```

These are gross figures before:

- VAT;
- payment fees;
- churn;
- discounts;
- failed payments;
- staffing;
- content production;
- professional services;
- hosting;
- moderation;
- events;
- and other operating costs.

## 19.3 Five-year non-financial success

Success should also include:

- a vibrant and active community;
- recurring events and meet-ups;
- consistent live streams;
- meaningful challenge participation;
- high assessment completion;
- strong programme activation;
- sustained member retention;
- measurable habit consistency;
- safe professional escalation;
- and members returning to healthy behaviours after setbacks.

---

# 20. North-Star Outcome

The platform’s strongest long-term outcome is not merely:

- number of downloads;
- number of assessments;
- kilograms lost;
- number of daily logins;
- or community size.

The preferred north-star is:

> The proportion of members who understand their personal patterns, adopt appropriate repeatable health behaviours, and return to those behaviours after setbacks.

A future measurable version may be:

> Women who complete a temperament-guided programme and maintain at least three personally appropriate health behaviours 90 days after programme completion.

---

# 21. Platform-Wide Non-Negotiables

1. Temperament is not a medical or psychological diagnosis.
2. Medical safety overrides temperament preferences.
3. The platform must not promise universal weight loss.
4. Weight loss must not be prescribed when it is inappropriate.
5. Complex health cases require risk-based routing.
6. High-risk members must not receive automated personalised weight-loss plans.
7. The platform must not use shame as a behaviour-change tool.
8. A missed day must not erase progress.
9. One person may hold several explicit roles.
10. Roles must not automatically grant unrelated data access.
11. Paying for another person does not grant access to her health information.
12. Practitioner access requires consent, scope, active relationship, expiry and audit.
13. Public content remains broadly accessible.
14. Personalised content must be explainable.
15. Personalised health guidance must use approved rules and content.
16. Unverified health information may not trigger clinical treatment recommendations.
17. AI may assist, but may not independently diagnose or prescribe.
18. Community must be moderated.
19. Private health information must not be pushed into public or semi-public community spaces.
20. The Christian identity must remain open and honest.
21. The women-first experience must not be weakened by future expansion.
22. Professional capacity must be protected from unlimited member expectations.
23. Founder and contributor access must follow role and data-boundary rules.
24. Personal data collection must be proportionate to a defined purpose.
25. Operating-entity and IP agreements must be resolved before commercial scale.

---


# 21A. Locked GQ-003 Commercial and Entitlement Rules

This section records the final GQ-003 decisions and overrides earlier general wording where a conflict exists.

## 21A.1 Incremental product delivery

The platform should be capable of supporting all approved long-term product categories, but they must be implemented incrementally through tracer bullets and vertical slices.

Do not build every future product before launch.

Products and major capabilities use this release lifecycle:

```text
draft
→ internal
→ pilot
→ public
→ paused
→ retired
```

- `draft`: being configured and unavailable;
- `internal`: available only to approved staff or test accounts;
- `pilot`: available to a controlled customer group;
- `public`: generally discoverable and purchasable;
- `paused`: existing access may remain, but new acquisition stops;
- `retired`: no longer sold, while historical entitlements remain governed.

Product availability is a business rule. Technical feature flags may assist rollout but do not replace the product lifecycle.

## 21A.2 Existing temperament and assessment credit

A qualifying plan purchase may include one digital assessment credit.

To reduce onboarding friction, a participant who already knows her temperament may declare:

- a self-reported primary temperament;
- an optional self-reported secondary temperament;
- or a result obtained from the physical book.

The platform must distinguish at least:

```text
self_reported
book_derived
digitally_assessed
```

The participant may continue onboarding and use the included online assessment later.

When a later digital result differs materially:

1. the new result is added to permanent history;
2. the earlier result is not silently deleted;
3. the participant is shown the meaningful difference;
4. she explicitly selects the current temperament profile;
5. future recommendations use the selected current profile.

When the plan purchase included the assessment credit, one complimentary regeneration of that plan is available when the digital reassessment is completed within 90 days of original plan generation.

## 21A.3 Assessment attempts and history

A paid digital assessment includes:

- one assessment attempt;
- permanent access to the completed report;
- permanent historical result retention;
- and one explicitly selected current temperament profile.

A valid reassessment entitlement may be used no more than once per year.

Premium membership may include one reassessment entitlement per year. It:

- becomes available after 12 continuous premium months or at annual premium renewal;
- does not accumulate;
- expires unused when the paid membership period ends;
- and does not affect permanent access to already completed assessments.

## 21A.4 Once-off plan access and adjustments

A once-off standard-plan customer retains permanent access to the delivered plan version.

Included after delivery:

- corrections;
- safety replacements;
- and access to the historical plan.

Not included after delivery:

- preference-based re-personalisation;
- progress-based re-personalisation;
- ongoing macro recalculation;
- or ongoing portion recalculation.

Ongoing check-in-driven macro or portion adjustments require:

- a new qualifying purchase;
- an active qualifying membership;
- or an active plan-adjustment add-on.

## 21A.5 Membership and add-ons

Basic membership is the base recurring subscription.

Optional add-ons grant additional recurring entitlements.

Premium is a customer-facing bundle made from basic membership plus named add-ons, rather than a separate entitlement system.

This structure should support future add-ons without creating a generic plugin marketplace.

## 21A.6 Billing and cancellation

Membership supports:

- monthly billing;
- annual billing;
- configured promotional discounts;
- no default free trial.

Cancellation takes effect at the end of the paid billing period.

After membership ends:

- public content remains available;
- purchased assessments remain available;
- purchased once-off plans remain available;
- completed personal check-ins remain visible;
- downloaded resources remain with the customer;
- membership-only content becomes unavailable;
- community access ends;
- the current premium plan remains visible as historical content;
- no new plan adjustment occurs;
- unused membership-derived reassessment entitlements expire.

## 21A.7 Premium monthly review

A complete check-in is required for a monthly premium review.

Rules:

- reviews do not accumulate indefinitely;
- “no change required” counts as a completed review;
- approved minor changes may be automated;
- professional review remains a separate paid service.

The exact monthly submission deadline and incomplete-check-in behaviour remain open.

## 21A.8 Failed payments

A failed recurring payment follows this product-level lifecycle:

```text
payment failure
→ immediate communication
→ controlled provider-safe retry attempts
→ opportunity to update payment details
→ final warning
→ recurring entitlements suspended after the grace period
```

The intended grace period is 72 hours.

A candidate retry sequence is approximately:

- one hour;
- five hours;
- one day;
- three days.

The exact Paystack charge-retry implementation remains provisional until provider behaviour and card-network safety are tested.

Access is restored only after verified payment confirmation.

## 21A.9 Gifts and sponsored access

The purchaser may see only whether a code is:

```text
unredeemed
redeemed
expired
cancelled
```

The purchaser may not see participant health, assessment, plan or check-in activity.

Default gift-code expiry is 12 months from purchase.

A redeemed entitlement is non-transferable.

Before redemption, support may reassign the recipient email through a controlled process.

Sponsored bulk access may use multiple unique redemption codes. Sponsors may receive aggregate redemption counts but no participant health data.

## 21A.10 Refund principles

Assessment:

- refundable before the first answer is submitted;
- ordinarily non-refundable after the first answer;
- refundable for verified technical failure where delivery could not be completed.

Plan:

- refundable before generation;
- ordinarily non-refundable once delivered.

Membership:

- no ordinary partial refund for the current billing period;
- duplicate or erroneous billing is refundable;
- applicable statutory consumer rights remain in force.

Event:

- each event has a versioned refund, transfer and future-credit policy published before checkout;
- cutoffs may differ per event;
- the event policy must state what happens to bundled digital entitlements.

## 21A.11 Upgrades and downgrades

- Upgrades take effect immediately with provider-supported proration.
- Downgrades take effect at the next renewal.
- Previously purchased or generated historical records remain visible.
- Add-ons may be activated or cancelled independently where the offer permits it.

## 21A.12 Payment provider, market and currency

Paystack is the **locked first / launch payment gateway** for the initial South African launch.

This provider choice is now Product Law. Exact Paystack retry, recurring-billing, webhook, proration, refund, dispute/chargeback, settlement and provider-failure behaviour remains subject to the existing validation gate before implementation details are fixed. Durable platform payment truth remains provider-independent and authoritative in PostgreSQL.

South Africa is the launch market.

South African rand is the launch billing currency.

International cards may be accepted when international payments are enabled for the merchant.

Foreign-card acceptance does not mean true multi-currency billing.

True multi-currency charging is a future requirement and must not be assumed to be available through the initial South African Paystack integration.

Automatic subscriptions initially use supported card billing.

Manual EFT or other manual payments may be supported separately, but they do not create automatic renewal. Entitlements are granted only after payment is verified.

## 21A.13 Discounts, codes and access grants

Pricing mechanisms may include:

- fixed-amount discounts;
- percentage discounts;
- event-linked discounts;
- limited-time promotional pricing.

Redemption codes may include:

- book-bundle codes;
- event-linked codes;
- gift codes.

Access grants may include:

- complimentary access;
- sponsored access;
- explicitly scoped lifetime access.

Lifetime access must always name the exact product, report, programme, membership scope or content entitlement. It must never mean unrestricted access to every future platform capability.



# 21B. Locked GQ-004 Temperament Assessment Rules

This section records the final assessment, scoring, interpretation and report rules.

## 21B.1 Methodology authority

Only Venessa and Super Admin, acting under the governing intellectual-property agreement, may exercise methodology authority.

This authority covers:

- assessment questions;
- answer options;
- scoring weights;
- tie-resolution rules;
- primary and secondary result rules;
- temperament interpretation methodology.

Super Admin authority is not automatic merely because the role has broad technical access. The person must be acting under the intellectual-property agreement, and every methodology action must be audited.

Ordinary administrators, content staff, developers and support staff may not alter methodology.

## 21B.2 Initial assessment version

The launch assessment is a faithful, versioned digital representation of the approved book assessment.

Future versions may introduce:

- revised wording;
- improved approved questions;
- differentiated scoring weights;
- approved tie-break questions;
- revised interpretation rules.

A material change creates a new methodology version and never silently changes completed results.

## 21B.3 Completion and attempt rules

- Every scored question is required.
- Submission is blocked while scored answers are missing.
- Optional feedback questions remain separate from scoring.
- Save and resume is supported.
- Only one active attempt is permitted per participant at a time.
- The entitlement is not consumed until the first answer is saved.
- Once the first answer is saved, the entitlement is marked used.
- An unfinished attempt remains active for 30 days.
- A warning is issued before expiry.
- Controlled support recovery is permitted for genuine technical failure.
- In-progress answers may be changed until submission.
- Submitted answers are immutable.

## 21B.4 Initial and future scoring

The launch version uses equal weighting. Each selected answer contributes one point to its assigned colour.

The methodology format must permit future versions to define:

- question weights;
- answer-option weights;
- multiple colour contributions;
- approved tie-break questions;
- score-distance thresholds.

Published versions remain immutable.

## 21B.5 Primary, secondary and score display

- The highest score becomes the primary temperament.
- The second-highest score becomes the secondary temperament.
- Exact colour scores are shown.
- Exact ties follow the approved tie-resolution workflow.
- Strong-dominance, balanced, close-result and mixed-distance labels are disabled until exact thresholds are approved.

## 21B.6 Tie-resolution workflow

```text
initial scored questions
→ exact tie detected
→ approved tie-break questions
→ approved high-value tie rules
→ equal mixed result when still unresolved
→ optional participant interpretive preference
→ exceptional methodology review where genuinely required
```

Rules:

- unresolved ties remain equal mixed results;
- participant preference is stored separately and never rewrites raw scores;
- manual review is exceptional;
- tie-break logic belongs to the assessment version.

## 21B.7 Immutable raw result and reviewed interpretation

These remain separate:

```text
raw scored result
≠
reviewed interpretation
≠
current profile selection
```

Raw submitted answers, calculated scores and assessment version are immutable.

An exceptional change creates a separate audited reviewed interpretation referencing the original result. It records reason, reviewer, approver, timestamp, notes and participant-notification status.

The original result is never erased or overwritten.

## 21B.8 Current profile

One eligible result is explicitly selected as current.

Eligible sources may include:

- self-reported;
- book-derived;
- digitally assessed;
- reviewed interpretation.

The participant may select among valid profiles.

Staff may assist only with participant consent and an audited reason.

The newest digital result never becomes current automatically.

## 21B.9 Self-reported result use

A self-reported or book-derived result may drive:

- presentation;
- tone;
- layout;
- reminder style;
- degree of choice;
- other low-risk temperament adjustments.

It must be clearly labelled and may not be represented as digitally assessed.

The participant should be encouraged to complete the digital assessment.

The existing 90-day complimentary plan-regeneration rule remains applicable where the plan purchase included the assessment credit.

## 21B.10 Assessment report

The paid assessment report provides a concise but meaningful overview of:

- primary temperament;
- secondary temperament;
- exact score breakdown;
- strengths;
- vulnerabilities;
- stress response;
- eating and health patterns;
- communication style;
- practical health strategies;
- faith reflection;
- next recommended product;
- limitations and disclaimer.

The report must provide real value and may not be reduced to a thin upsell page.

## 21B.11 Historical reports and versions

The participant retains:

- the original delivered report;
- the latest approved interpretation where wording improves.

Each report records assessment version, scoring version, language version, interpretation-content version, generation date and result provenance.

Completed results remain immutable.

A valid short-lived active attempt may finish on its original version.

Retired versions cannot start new attempts.

Material methodology changes may require a new assessment rather than silently rescoring old answers.

## 21B.12 Afrikaans and English parity

Afrikaans and English are separate language variants linked to one methodological version.

Each language variant is reviewed independently while preserving equivalent intent, answer meaning, scoring and tie behaviour.

Every attempt records the language used.

## 21B.13 Review and publication workflow

```text
draft
→ methodology approval
→ health review where affected
→ language review
→ admin publication
→ active
→ retired
```

Minor copy corrections may use a lighter language/editorial path when meaning and scoring do not change.

Material question, scoring or tie-rule changes require a new methodology version and methodology-authority approval.

## 21B.14 Submitted-answer retention and access

Submitted answers are retained immutably so every result can be reproduced.

- Participants may view their own answers.
- Ordinary support staff may not browse assessment answers.
- Methodology-review access requires a defined reason.
- Every staff access is audited.
- Retention and deletion now follow the locked GQ-010 rules in section 21I; exact statutory, financial and professional durations remain expert-owned.

## 21B.15 Cross-product reuse and analytics

The underlying temperament result may be reused across approved product families.

Each product family provides its own interpretation, recommendations, content and safety boundaries.

Privacy-controlled aggregated analytics may measure completion, drop-off, colour distribution, tie frequency, language differences and conversion.

Analytics must not expose identifiable participants without an authorised purpose.



# 21C. Locked GQ-005 Health Onboarding, Eligibility and Safety Rules

This section records the approved health intake, eligibility, monitoring, suspension and clinical-safety boundaries.

## 21C.1 Progressive health onboarding

Health information is collected progressively and only for a defined purpose.

```text
free account
→ identity, language and age confirmation only

temperament assessment
→ temperament information only

plan onboarding
→ health, lifestyle and safety information required for eligibility and generation

professional review
→ deeper medical, medication, laboratory and clinical information only when required
```

The platform must not require a full health intake for public content, free registration or the temperament assessment.

## 21C.2 Required plan-onboarding information

Before any automated personalised plan is generated, require a safety-focused structured intake containing:

- full date of birth;
- height;
- current weight;
- desired outcome;
- recent weight-change pattern;
- pregnancy status;
- breastfeeding status;
- allergies;
- intolerances;
- diagnosed conditions relevant to nutrition;
- current medications relevant to diet or safety;
- eating-disorder screening;
- current concerning symptoms;
- activity level;
- typical meal pattern;
- meal-frequency preferences;
- hunger baseline;
- energy baseline;
- sleep baseline.

Optional unless required for a selected product or safety pathway:

- waist and other measurements;
- supplements;
- detailed medical history;
- laboratory values;
- practitioner information;
- progress photographs.

## 21C.3 Full date of birth

Full date of birth is required during personalised-plan onboarding, not during ordinary account registration or assessment purchase.

It may support age-based safety rules, energy calculations, life-stage relevance and professional review.

## 21C.4 Health-information provenance

Health information records its source and verification state.

Supported provenance includes:

```text
member_reported
document_uploaded
practitioner_entered
practitioner_verified
laboratory_verified
```

Permitted non-value states may include:

```text
unknown
not_tested
prefer_not_to_answer
```

Safety-critical questions may not permit `prefer_not_to_answer`. Missing or unclear required information produces `insufficient_information`.

## 21C.5 Eligibility outcomes

Use four explicit outcomes:

```text
eligible_automated
general_wellness_only
professional_review_required
insufficient_information
```

- `eligible_automated`: a standard or qualifying premium automated plan is permitted;
- `general_wellness_only`: only the General Wellness Starter Pathway is permitted;
- `professional_review_required`: no personalised plan until professional approval;
- `insufficient_information`: generation is blocked until required information is completed or clarified.

An opaque numerical risk score must not be the primary participant-facing eligibility decision.

## 21C.6 High-risk blockers

Approved high-risk rules block automated personalised-plan generation.

Likely blocker categories include:

- active eating disorder;
- recent eating-disorder treatment;
- pregnancy or breastfeeding requiring professional review;
- diabetes treated with medication;
- significant kidney, liver or heart disease;
- recurrent fainting;
- severe unexplained dizziness or weakness;
- unexplained rapid weight loss;
- repeated vomiting;
- severe allergy complexity;
- medication requiring dietary management;
- abnormal laboratory findings requiring interpretation;
- current professional advice conflicting with platform guidance;
- participant younger than 18.

The final blocker matrix requires clinical approval before automated plans may launch.

## 21C.7 Moderate-risk routing

Approved moderate-risk cases use automated routing with manual escalation.

Examples may include:

- unverified abnormal laboratory information;
- incomplete allergy details;
- manageable food intolerance;
- stable medication without confirmed dietary implications;
- uncertain eating-disorder history;
- recent significant weight change without urgent symptoms;
- incomplete medical information.

The platform may provide the General Wellness Starter Pathway, request clarification, request professional review or escalate the case.

Venessa or an authorised practitioner may escalate moderate risk.

## 21C.8 Eating-disorder boundary

Active or recent eating-disorder cases block automated plans.

Older stable history requires professional review before deeper personalised planning.

While eating-disorder risk is unresolved, the platform must not provide:

- fasting protocols;
- aggressive energy restriction;
- weight-loss targets;
- punitive tracking;
- rapid-loss messaging;
- or other content likely to increase harm.

## 21C.9 Pregnancy and breastfeeding

Pregnancy and breastfeeding require professional review before any personalised eating plan.

While awaiting review, the participant may receive the General Wellness Starter Pathway.

That pathway may include hydration, sleep and rest, gentle routine support, emotional wellbeing, approved general healthy-eating education, and faith and identity content.

It excludes weight-loss targets, fasting, supplement dosage and individual clinical recommendations.

## 21C.10 Food-exclusion categories

The platform must distinguish:

```text
medical_allergy
food_intolerance
religious_exclusion
ethical_exclusion
dislike
preference
```

Allergies and ordinary preferences must never share one generic field.

Allergy information may also include reaction severity, anaphylaxis history, cross-contamination concern, practitioner confirmation, emergency medication and uncertainty requiring review.

Ordinary dislikes may permit automated substitution.

Severe allergy complexity may block automated generation.

## 21C.11 Medication boundary

Collect only the structured minimum medication information required for safety:

- medication name where known;
- general purpose or condition;
- relevant frequency or timing;
- whether food timing is involved;
- whether the participant is unsure of implications.

The platform must not perform unrestricted automated drug-interaction interpretation.

Only professionally approved medication-related safety rules may be automated.

Unclear or complex medication cases route to professional review.

## 21C.12 Supplement boundary

Supplements are handled separately from medication and ordinary food preferences.

The platform may record supplement name, approximate use and current-use status.

It may provide general educational content, approved low-risk guidance and plan awareness of current use.

Approved rules or professional review are required for dosage recommendations, deficiency correction, medication interactions, pregnancy-related supplementation, complex combinations and high-dose use.

Premium membership does not automatically include clinical supplementation advice.

## 21C.13 Laboratory-result validity

Laboratory results remain permanently visible as historical information, but their use for current decisions follows a clinically approved test-specific validity policy.

A laboratory result records:

- test type;
- value;
- unit;
- supplied reference range;
- collection date;
- source;
- verification state;
- valid-for-decision-until date;
- reviewer where applicable;
- superseding result where applicable.

Member-entered and uploaded results remain unverified until appropriately reviewed.

A newer result may supersede an older result for current decisions but never deletes it.

## 21C.14 Check-ins and measurements

Participants may enter approved progress information daily or weekly, including:

- weight;
- waist or selected measurements;
- hunger;
- energy;
- sleep;
- adherence;
- symptoms;
- adverse reactions.

Recording frequency and plan-adjustment frequency remain separate.

Rules:

- daily or weekly entries do not regenerate the plan immediately;
- ordinary plan adjustments occur monthly;
- adjustments use trends and progress across an approved review window;
- normal short-term fluctuations do not trigger recalculation;
- one isolated measurement does not drive an adjustment;
- concerning symptoms or reactions may trigger an immediate safety review;
- the interface must discourage compulsive weighing and punitive tracking;
- progress photographs are optional and require separate privacy controls.

## 21C.15 Automatic safety suspension

When an approved high-risk rule is triggered after a plan has been issued:

```text
active plan
→ safety_paused
→ new adjustments blocked
→ participant informed
→ General Wellness Starter Pathway shown where appropriate
→ clarification or professional review
→ cleared, replaced or restricted
```

The historical plan remains visible but is prominently marked unsuitable for continued use.

The plan and participant history are not deleted.

## 21C.16 Safety-flag lifecycle

Use the following structured lifecycle:

```text
detected
→ awaiting_information
→ participant_action_required
→ professional_review_required
→ under_professional_review
→ cleared
→ restricted
→ resolved
```

A case may move backward when new information is received.

Possible outcomes include:

- automated plan permitted;
- General Wellness Starter Pathway only;
- practitioner-reviewed plan permitted;
- no plan permitted;
- urgent external care recommended.

## 21C.17 Manual clinical override

Venessa or an authorised practitioner may create a separate scoped clinical override.

It records:

- original automated outcome;
- replacement outcome;
- exact scope;
- reason;
- reviewer;
- professional role;
- supporting notes;
- participant notification;
- effective date;
- review or expiry date;
- complete audit trail.

The original automated outcome remains unchanged.

When a high-risk case is lowered to automated eligibility, a second authorised clinical approval or an explicitly approved single-practitioner protocol is required.

## 21C.18 Practitioner-review outcomes

A practitioner review records a structured outcome plus professional notes.

Supported outcomes include:

```text
approved_as_proposed
approved_with_modifications
practitioner_authored_plan
restricted_pathway
follow_up_required
declined_no_plan
referred_externally
```

The review may also define:

- prohibited foods or actions;
- permitted substitutions;
- supplementation restrictions;
- follow-up date;
- review expiry;
- approved plan version;
- professional notes;
- participant-facing explanation.

## 21C.19 Consent and processing permissions

Use purpose-specific permissions and lawful-basis records.

Keep separate records for:

- account terms and service delivery;
- storing health information;
- using health information for personalisation;
- receiving automated recommendations;
- laboratory-document uploads;
- sharing information with a named practitioner or active care relationship;
- anonymised or aggregated analytics;
- marketing email, SMS or WhatsApp communication;
- community participation.

Required product processing must be clearly distinguished from optional processing.

Marketing permission remains separate.

Practitioner sharing is scoped and relationship-specific.

Every consent, withdrawal and applicable policy version is timestamped and retained.

Withdrawal affects future processing but may not erase records that must legitimately be retained.

## 21C.20 Emergency and urgent-safety boundary

The platform is not an emergency service and must not imply continuous clinical monitoring.

When an approved urgent rule triggers:

- stop personalised onboarding or adjustment;
- do not generate a new plan;
- display a clear instruction to seek appropriate immediate professional or emergency assistance;
- show country-appropriate support information where available;
- require acknowledgement of the message;
- record the exact message version shown;
- prevent community moderators from acting as clinicians;
- avoid promising live monitoring;
- perform internal escalation only where a defined and staffed professional workflow exists;
- do not automatically contact third parties unless a lawful approved emergency protocol applies.

Emergency wording and location-specific support information require professional and legal review before launch.



# 21D. Locked GQ-006 Plan Generation, Lifecycle and Adjustment Rules

## 21D.1 Deterministic plan generation

Automated plans are assembled by a deterministic, versioned rule engine using approved calculation protocols, eligibility results, meal templates, substitutions, temperament presentation rules, recipes and multilingual content.

AI may assist with drafting or operations but may not independently decide nutritional targets, meals, quantities, safety outcomes or clinical recommendations.

## 21D.2 Goal catalogue

Initial automated pathways:

```text
health_foundation
weight_reduction
weight_maintenance
```

The goal catalogue must allow future approved pathways without redesigning plan generation, including:

```text
weight_gain
weight_restoration
condition_specific
pregnancy_or_breastfeeding
clinical_performance
```

General weight gain and clinically governed weight restoration remain separate concepts.

## 21D.3 Calculation protocols and energy units

Energy and macro targets use approved, versioned protocols with explicit formulas, limits, rounding, allocation rules, exclusions and escalation triggers.

Kilojoules are the default participant-facing energy unit for South Africa.

Calories or kilocalories are supported from launch through a saved display toggle.

Both displays use one authoritative underlying energy value and deterministic conversion. Changing units never regenerates the plan.

## 21D.4 Numerical detail and weight-reduction boundaries

Exact targets remain available internally.

Participant-facing detail may use plate guidance, portions, ranges, exact kilojoules or Calories, and macro grams according to product and safety rules.

Temperament may influence presentation depth, but safety and eating-disorder rules override it.

Weight-reduction protocols use approved deficit ranges, minimum energy boundaries, rate guardrails, symptoms requiring suspension and trend windows before adjustment.

## 21D.5 Meal structures, composition and substitutions

Initial automated plans support approved three- or four-meal structures. Fasting is excluded from ordinary automated plans.

Seven-day plans use approved modular meal slots, portions, recipes, alternatives, preparation guidance and shopping support.

Substitutions use approved, versioned equivalence groups that enforce nutritional tolerance, meal context, allergies, intolerances, religious exclusions, ethical exclusions and preparation assumptions.

Temperament changes behavioural delivery and presentation, not nutritional truth.

## 21D.6 Immutable snapshots and explainability

Each generated plan is an immutable snapshot containing the participant-input snapshot, eligibility result, selected temperament profile, calculation protocol, template version, substitution rules, language-content versions, generation reason, date, entitlement and provenance.

Every adjustment creates a linked new version.

Participant-facing explanations cover the goal, pathway, meal frequency, major preferences, temperament presentation, important inclusions, rejected requests and whether the plan was automated or practitioner reviewed.

The internal trace retains exact inputs, rules and versions.

## 21D.7 Failure handling

Generation fails closed.

- Partial plans are never published.
- The entitlement remains available until successful delivery.
- Failures are recorded.
- Retries must be safe and idempotent.
- Duplicate plans, double charging and silent generic fallback are prohibited.
- Defined retry exhaustion creates an operational alert.

## 21D.8 Plan lifecycle and activation

Use:

```text
pending_generation
→ generated
→ awaiting_review
→ approved
→ scheduled
→ active
→ safety_paused
→ completed
→ superseded
→ withdrawn
```

Not every plan passes through every state.

A participant may start immediately, review first or choose an approved near-term date.

Plans scheduled too far ahead require eligibility reconfirmation. Only one ordinary plan may be active for the same goal and product scope.

## 21D.9 Monthly reviews

One formal adjustment review becomes available per qualifying entitlement period after an approved minimum plan-use period.

A complete check-in is required.

Missed or incomplete reviews do not generate changes, do not accumulate and expire after a defined grace period. The current safe plan continues unless safety requires suspension.

Approved review outcomes include:

```text
continue_unchanged
presentation_adjustment
approved_substitution_update
portion_adjustment
macro_adjustment
meal_frequency_adjustment
simplify_plan
increase_variety
safety_pause
professional_review_required
```

No-change counts as a completed review.

## 21D.10 Trend-based recalculation and conflicting requests

Macro or portion changes require a due review, complete data, sufficient trends, movement beyond approved fluctuation tolerance, adherence context, no safety blocker and protocol-compliant targets.

Participant requests never override safety rules. The platform records and explains rejected requests, offers safe alternatives and escalates clinically significant disagreement.

## 21D.11 Practitioner-derived versions

Professional changes create a new immutable practitioner-derived plan version.

A practitioner may approve unchanged, approve with modifications, replace with a practitioner-authored plan, add restrictions or define follow-up requirements.

The version records its source, practitioner, review outcome and justification, and supersedes the prior active version when activated.

## 21D.12 Bilingual delivery and translation architecture

Calculations and plan logic are shared across languages.

Participant-facing content uses separately approved Afrikaans and English variants for meal names, recipes, preparation, warnings, explanations, behavioural guidance, shopping lists and reports.

Language switching does not recalculate the plan.

Each delivered plan records the exact language-content versions used.

The translation architecture is layered:

1. Gettext for interface labels, fixed application strings, pluralisation and translatable system or validation messages.
2. Explicit Ash-backed translation resources for runtime-managed governed content such as recipes, plans, warnings, products, articles and programmes.
3. Immutable delivery snapshots that reference the exact translation versions shown.

A single giant global string list is not the sole translation system.

Complex governed editorial content must not live only in compiled Gettext files.

Machine-assisted translation may create drafts, but health, safety and plan content requires the applicable language and professional approval before publication.

## 21D.13 Recipes, shopping lists, corrections and withdrawal

Plans may contain approved reusable recipes, serving data, substitution notes and consolidated shopping lists generated from the immutable plan snapshot.

Minor corrections preserve the original delivered version and record the correction.

Material corrections create replacement versions.

Safety issues pause or withdraw affected active plans, notify participants and generate safe replacements where possible without consuming a new entitlement.

## 21D.14 Analytics and performance

Plan analytics use governed events and precomputed aggregates.

Peak-time full-table scans are prohibited.

Unnecessary health detail is excluded, and analytics are pseudonymised or aggregated where possible.

Suitable real-time operational counters may use Redis. Durable plan and clinical truth remains in PostgreSQL. Analytics never becomes the source of eligibility or safety truth.



# 21E. Locked GQ-007 Content, Translation and Personalised Feed Rules

This section records the approved content-governance, translation, publication, discovery, media and caching model.

## 21E.1 Source languages and bilingual scope

Content may originate in Afrikaans or English.

Each version records:

- source locale;
- source version;
- author;
- translation relationship;
- approval state.

Afrikaans and English variants remain linked to one conceptual content item and are reviewed independently.

Both languages are mandatory before publication or delivery for:

- registration and authentication;
- checkout and subscriptions;
- terms, consent and privacy notices;
- assessments;
- paid reports;
- personalised plans;
- safety messages;
- clinical warnings;
- cancellation and refund communication;
- core onboarding.

Low-risk public editorial content may temporarily exist in one language when the available language is clearly identified, the missing translation is tracked, and no silent machine translation is shown.

## 21E.2 Translation lifecycle and machine assistance

Each translation uses an independently governed lifecycle:

```text
missing
→ draft
→ machine_draft
→ language_review
→ clinical_review_required
→ approved
→ published
→ superseded
→ withdrawn
```

Not every translation requires clinical review. Required approvals follow the content risk class.

Machine translation may create a draft only.

A machine draft:

- is marked as machine-generated;
- is never publicly visible before approval;
- records its exact source version;
- requires human language review;
- requires clinical review where health or safety is affected;
- becomes stale when its source changes.

## 21E.3 Content structure and types

Use a shared conceptual content item with separately versioned language variants.

Conceptually:

```text
ContentItem
→ ContentVersion
→ ContentTranslationVersion
```

The shared item defines identity, type, audience, risk class, ownership and relationships.

Each language version defines locale, wording, version, lifecycle state, reviewers, approvals and publication date.

Initial controlled content types include:

```text
article
lesson
devotional
recipe
plan_instruction
assessment_interpretation
safety_notice
faq
product_page
event_page
live_session
download
```

New types require an approved extension rather than arbitrary administrator-created names.

## 21E.4 Content risk and approvals

Use these governed risk classes:

```text
editorial_low_risk
health_education
personalisation_guidance
clinical_guidance
safety_critical
legal_or_consent
```

Risk class determines reviewers, clinical approval, language approval, publication authority, correction severity and withdrawal urgency.

Use a scoped approval matrix:

- editorial and platform copy: Content Approver;
- Afrikaans quality: Afrikaans Language Reviewer;
- English quality: English Language Reviewer;
- general health education: Health Content Approver;
- personalised or clinical guidance: Venessa or authorised clinical approver;
- safety-critical content: Venessa plus a second approval where the protocol requires it;
- legal and consent content: authorised legal or privacy approver;
- faith content: designated faith or editorial approver.

One person may hold several roles, but each approval remains separately recorded.

## 21E.5 Personalised feed ranking

Member-feed ranking is deterministic and explainable.

Approved ranking signals may include:

- selected content language;
- current temperament profile;
- active product entitlements;
- current programme stage;
- approved goals;
- broad health-relevance flags;
- content freshness;
- editorial priority;
- prior completion;
- saved or dismissed content.

Safety-required and professionally prescribed material may override ordinary ranking.

The feed prioritises relevant content but does not prevent broader browsing.

## 21E.6 Health-derived relevance and participant control

Feed ranking uses approved derived relevance flags rather than full diagnoses or detailed clinical records.

Examples include:

```text
iron_health_relevant
sleep_support_relevant
stress_support_relevant
general_wellness_only
```

Rules:

- feed infrastructure receives only the minimum signal;
- the underlying diagnosis is not copied into feed logs;
- the participant may see why content was prioritised;
- flags expire or withdraw when their source, validity or permission ends;
- feed analytics does not become a duplicate clinical record.

Participant controls include:

- why this is shown;
- save;
- dismiss;
- show less of a topic;
- follow or unfollow optional topics;
- browse all content;
- reset feed preferences.

Applicable safety-required content cannot be permanently hidden.

## 21E.7 Missing translation fallback

For optional low-risk public content:

- state clearly that the selected translation is unavailable;
- explicitly offer the available language;
- never switch language silently.

For paid, consent, assessment, plan, clinical and safety content:

- block publication or delivery until required approved translations exist;
- never use an unapproved machine fallback.

## 21E.8 Immutable content versions

Every material edit creates a new immutable content version.

Each version records:

- parent content item;
- locale;
- version number;
- author;
- source version;
- change summary;
- risk class;
- approvals;
- publication date;
- superseded version;
- correction or withdrawal reason.

Minor typographical corrections may use a controlled correction path, but the original published version remains traceable.

## 21E.9 Scheduling and automatic publication

Approved content may be scheduled to publish automatically on a future date so the editorial team can prepare content ahead of time.

A version may record:

```text
approved_at
publish_at
unpublish_at
embargo_until
```

Before automatic publication, the system rechecks:

- required approvals;
- required translations;
- access rules;
- product or event state;
- safety-withdrawal status;
- dependency availability.

A scheduled item must not publish when required approval has expired or a required translation has been withdrawn.

Scheduling must be reliable, idempotent and observable. Failed publication attempts create an operational alert and must not create duplicate publication events.

## 21E.10 Correction and withdrawal classes

Use:

```text
minor_editorial_correction
material_content_correction
safety_correction
legal_or_consent_correction
full_withdrawal
```

Minor corrections update current presentation while preserving and recording the original.

Material corrections create an approved superseding version and notify affected participants where appropriate.

Safety corrections withdraw affected use immediately, identify impacted plans, reports or programmes, notify participants, replace content where possible and create an incident record.

Legal or consent corrections require legal or privacy approval and may require renewed acknowledgement.

Full withdrawal removes future access while preserving audit history and applying product-specific handling to delivered content.

## 21E.11 Attribution

Internal responsibility records distinguish:

- original author;
- co-author;
- translator;
- language reviewer;
- health reviewer;
- clinical approver;
- legal or privacy approver;
- faith reviewer;
- publisher;
- correction approver.

Public presentation may show selected contributors, relevant credentials and the last-reviewed date without exposing all operational staff.

## 21E.12 Taxonomies and search

Use controlled, versioned taxonomy groups such as:

```text
topic
health_theme
temperament_relevance
programme_stage
life_stage
content_format
faith_theme
goal_relevance
audience
```

Aliases and redirects handle renamed terms. Arbitrary public tags require review. Diagnoses are not automatically exposed as public taxonomy labels.

Search uses layered deterministic ranking based on:

- full-text search;
- title and heading weights;
- exact phrases;
- approved synonyms;
- locale;
- taxonomy;
- freshness where appropriate;
- editorial priority;
- entitlement;
- publication state;
- secondary personalised relevance.

Withdrawn content never appears. Access policy is applied before returning results. Semantic search may later be added as a controlled secondary signal, not the sole authority.

## 21E.13 Bilingual SEO

Public content uses explicit locale-specific URLs, for example:

```text
/af/artikels/slaap
/en/articles/sleep
```

Each translation may define its own approved slug and metadata.

Rules:

- language variants link to one conceptual item;
- each language has its own canonical URL;
- language-alternate metadata is used only for real translations;
- slug changes create permanent redirects;
- private and paid content is excluded from ordinary indexing.

## 21E.14 Reusable content blocks

Approved reusable blocks may include:

```text
temperament_guidance
health_explanation
safety_warning
faith_reflection
preparation_instruction
programme_prompt
product_explanation
```

Each parent item selects an approved block version.

Historical delivered plans and reports retain the versions originally used. Updating a reusable block does not silently rewrite immutable deliveries.

Composition rules must prevent contradictory combinations.

## 21E.15 Media and protected delivery

Media assets are governed independently and record:

- type and version;
- owner;
- licence and usage rights;
- source and creator;
- alt text and captions;
- locale-specific text;
- accessibility transcript;
- risk class;
- publication state;
- checksum;
- storage location;
- replacement relationships.

Uploads are scanned before publication. Private media uses protected access. Public media may use CDN delivery.

Protected downloads, reports and recordings use entitlement-checked access and short-lived signed delivery links.

The platform distinguishes public, member-only, purchased and practitioner-shared assets.

## 21E.16 Analytics

Collect governed minimum events such as:

```text
content_impression
content_opened
content_completed
content_saved
content_dismissed
topic_followed
search_performed
download_requested
replay_started
required_content_acknowledged
```

Do not copy detailed health data into analytics events.

Use broad relevance reason codes, pseudonymous identifiers where appropriate, defined retention and aggregated dashboards.

Journal content is excluded unless separately approved.

## 21E.17 Cloudflare and layered caching direction

Cloudflare is the selected CDN and edge-caching direction for public static media and appropriately cacheable public content.

The architecture must combine:

```text
edge
→ Cloudflare CDN and safe edge caching

hot
→ ETS or Cachex for frequently accessed metadata and feed fragments

warm
→ Redis for published content, taxonomy results and suitable feed candidates

cold and durable
→ PostgreSQL for content versions, approvals and publication truth
```

Elixir, Ash and PostgreSQL query optimisation must be used deliberately, including correct indexes, bounded queries, pagination or streaming, preloading discipline and aggregate strategies.

“All optimisations” does not mean enabling every available cache indiscriminately.

Rules:

- private health, plan, entitlement and personalised content must not enter public CDN caches;
- cache keys include locale, access scope and published version where applicable;
- publication, correction, withdrawal and entitlement changes trigger invalidation;
- safety withdrawals bypass ordinary TTL and invalidate immediately;
- cache stampedes and thundering-herd behaviour must be prevented;
- PubSub may notify application nodes of publication changes;
- large result sets are paginated or streamed;
- dashboards use aggregates rather than peak-time scans;
- every optimisation must preserve correctness, privacy and immediate withdrawal behaviour.



# 21F. Locked GQ-008 Programme, Habit, Journal and Progress Rules

This section records the approved programme structure, participant progression, habits, reminders, journals, accountability and progress-recognition model.

## 21F.1 Reusable programme model

Use a reusable hierarchical programme structure:

```text
Programme
→ ProgrammeVersion
→ Module
→ Lesson
→ Activity
```

Activities may include reading, video, audio, reflection, journal prompts, habit actions, check-ins, acknowledgements, knowledge checks and downloads.

Each level may define ordering, requirements and approved temperament presentation.

## 21F.2 Programme catalogue and lifecycle

Use an approved extensible programme catalogue.

Possible categories include:

```text
health_foundation
sleep_foundation
stress_support
emotional_eating
self_talk
faith_and_identity
movement_foundation
weight_maintenance
```

Each programme defines purpose, audience, eligibility, risk class, expected duration, structure, completion rules, approvals and entitlements.

Programme release follows:

```text
draft
→ internal
→ pilot
→ public
→ paused
→ retired
```

## 21F.3 Delivery modes

Support:

```text
evergreen_self_paced
scheduled_cohort
facilitated_cohort
```

Launch primarily with evergreen self-paced delivery unless a specific pilot requires a cohort.

## 21F.4 Programme entitlements

Programme access follows an explicit entitlement and may be public, free-account, membership-included, add-on, once-off purchased, bundle-included, sponsored or practitioner-assigned.

Once-off purchased programmes may grant permanent access to the delivered version.

Membership-only access stops when membership ends, while completed progress history remains visible.

Purchasers cannot see another participant's progress.

## 21F.5 Progression and pacing

Use guided progression with explicit prerequisites.

A programme may define required sequential lessons, optional lessons, recommended ordering, milestone gates, safety acknowledgements and freely browsable support resources.

The participant must be told why a lesson is locked.

Programmes use recommended pacing with flexible completion. Missing a recommended date does not fail the programme.

## 21F.6 Enrolment lifecycle

A participant may enrol, schedule, begin, pause, resume, complete, abandon and restart.

Every enrolment attempt is preserved. Restarting creates a new linked enrolment rather than deleting old progress.

Duplicate simultaneous enrolments in the same programme version are prevented unless explicitly allowed.

A restart must not silently consume a new paid entitlement.

## 21F.7 Activity requirement types

Each activity has an explicit type:

```text
required_for_progression
required_for_completion
required_for_safety
recommended
optional
conditional
```

Participants must be able to see whether an activity is required and why.

## 21F.8 Missed days and recovery

Progress is never reset merely because time passed.

The programme may identify missed work, recommend the next smallest useful action, allow catch-up, reschedule unfinished activities, simplify upcoming workload, pause reminders and continue from the current position.

There is no punitive failure state for ordinary delay.

Required safety activities cannot be skipped silently.

Recovery messaging may be temperament-adapted.

## 21F.9 Completion rules

Programme completion uses versioned rules and may require all completion-required lessons, safety acknowledgements, required activities, a final check-in and minimum participation where appropriate.

Completion never requires weight loss, a specific measurement, perfect adherence or an uninterrupted streak.

Completion states may include:

```text
completed
completed_with_optional_items_remaining
partially_completed
```

## 21F.10 Programme version changes

New enrolments normally use the latest approved version.

Active participants remain on their enrolled version unless a minor correction applies, an optional governed migration is accepted, or a safety correction requires migration or withdrawal.

Material changes create a new programme version.

Progress mapping must be explicit when migration occurs.

Completed history never changes silently.

## 21F.11 Temperament influence

Temperament may influence framing, explanation depth, visible choice, lesson size, reminder tone, pacing suggestions, accountability style, reflection prompts, recovery messaging and optional activity recommendations.

It does not independently change clinical safety, factual health content, safety acknowledgements or professional restrictions.

## 21F.12 Habit catalogue

Use an approved habit catalogue plus participant-created low-risk habits.

Approved habits may be linked to programmes, plans, temperament guidance, health foundations or professional assignments.

Participant-created habits may not claim to diagnose, treat or replace professional recommendations.

Practitioner-assigned habits remain distinguishable from self-created habits.

## 21F.13 Habit schedules

Support controlled schedules:

```text
daily
selected_weekdays
times_per_week
weekly
specific_date
programme_relative
```

Schedules use the participant's timezone. Timezone changes must not duplicate completions. Completion windows must behave predictably around late-night entries.

Clinically relevant frequency follows approved limits. Missed occurrences remain historical.

## 21F.14 Habit occurrence states

Use:

```text
pending
completed
partially_completed
skipped_intentionally
missed
not_applicable
safety_blocked
```

Participants may add optional notes. Intentional skips do not equal failure. Safety-blocked occurrences reflect professional or platform restrictions.

Future occurrences are not marked missed before the completion window ends. Staff may not alter participant history silently.

## 21F.15 Compassionate consistency

Do not use fragile streaks that reset to zero after one missed day.

Use compassionate indicators such as seven- or thirty-day completion, personal consistency trend, recovery after a miss, current rhythm and optional longest rhythm.

One missed day does not erase progress. There are no shame-based warnings or public streak rankings. Participants may hide counters. Safety pauses do not count as failures.

## 21F.16 Reminder controls

Participants may control reminder time, channels, days, snooze, temporary pause and quiet hours within governed limits.

Reminders are timezone-aware, frequency-capped, stop after completion, use supportive missed-day language and remain separate from marketing.

Safety-required notices may override ordinary preferences where appropriate. Delivery failures are operationally recorded.

## 21F.17 Accountability sharing

Accountability sharing is optional, scoped and revocable.

A participant may share selected habits, programme milestones, completion summaries or participant-written updates with an approved accountability partner, authorised practitioner or future facilitator.

Journals, health data and assessment details are excluded by default.

Scope, expiry, revocation and access are audited. The recipient cannot alter participant history.

## 21F.18 Journal types

Support:

```text
free_reflection
guided_prompt
programme_reflection
gratitude_entry
faith_reflection
food_or_hunger_reflection
setback_reflection
practitioner_shared_note
```

Entries may contain text, prompt references, simple reflection markers, approved attachments, programme relationships and sharing state.

Structured health check-ins remain separate from private journals.

## 21F.19 Journal privacy

Journal entries are private by default.

Ordinary support, content, moderator and administrator roles cannot browse journals.

The participant may explicitly share selected entries with an authorised practitioner. Sharing records recipient, scope, purpose and expiry. Practitioner access is audited.

Revocation ends future platform access, subject to professional retention obligations where an entry has entered a professional record.

Journal excerpts are not copied into support tickets or analytics.

## 21F.20 Journal safety boundary

The platform does not promise continuous monitoring of free-text journals.

Journals display a non-monitoring notice. Structured check-ins and explicit help actions may trigger safety workflows. High-risk structured answers may pause plans or request review. Urgent user actions display approved help information.

Free-text AI monitoring is excluded from the MVP.

Any later assistive detection requires disclosure, expert approval, tested escalation capacity and a staffed response process.

## 21F.21 AI journal assistance

Future AI assistance may be participant-initiated and tightly scoped.

The participant may select entries and request a summary or discussion themes.

It is disabled by default, outside the MVP, non-diagnostic, never automatically shared, labelled, discardable and subject to approved privacy, retention and provider boundaries.

## 21F.22 Progress recognition

Use private, health-aligned recognition.

Possible milestones include first lesson, module completion, returning after a setback, maintaining a chosen routine, completing reflections, finishing a programme and reaching a personal non-weight goal.

The platform may offer private milestone messages, optional badges, completion certificates and participant-controlled sharing.

There are no public weight rankings, shame-based consequences or rewards that encourage restriction or overexercise.

## 21F.23 Programme and habit analytics

Collect governed behavioural events and aggregates such as programme enrolment, lesson completion, activity completion, pause, resume, programme completion, habit scheduling, habit completion, intentional skip, recovery actions, reflection creation and milestones.

Journal text is excluded. Health detail is not duplicated.

Dashboards use cached or materialised aggregates. Peak-time full-table scans are prohibited. High-volume occurrence data is paginated or streamed.

Suitable real-time counters may use Redis. Durable progress truth remains in PostgreSQL. Analytics never changes completion or safety truth.



# 21G. Locked GQ-009 Community, Challenges, Live Sessions and Event Rules

This section records the approved community, challenge, live-session, recording and event model.

## 21G.1 Community rollout

Community follows a staged validation path:

```text
governed Facebook community
→ migration-readiness evidence
→ first-party community pilot
→ controlled migration
```

Facebook is an initial operating channel, not the permanent source of platform truth.

Migration readiness must be based on observed moderation, privacy, identity, engagement, programme and operational needs rather than dissatisfaction alone.

## 21G.2 Community entitlement

Community access requires an explicit qualifying entitlement.

Possible sources include:

- membership;
- bundle;
- programme or challenge;
- event;
- sponsored access;
- pilot access;
- staff/facilitator access;
- practitioner participation where explicitly appropriate.

Community access never grants unrelated health, journal, plan or professional-record access.

When a qualifying entitlement ends, new community access ends subject to the product policy. Historical contributions follow the deletion/anonymisation rules rather than being silently erased.

## 21G.3 Identity and profile privacy

The platform retains verified private account identity where required while allowing a controlled participant-selected public display name.

Possible public community fields are participant-selected and may include:

- display name;
- profile image;
- limited bio;
- approved interests;
- selected programme or community badges.

The following remain private by default:

- assessment answers;
- health profile;
- diagnoses and medication;
- weight and measurements;
- plans;
- journals;
- practitioner relationships;
- purchases;
- private support cases.

Verified staff, practitioner and facilitator badges are controlled platform assertions, not user-editable labels.

## 21G.4 Group participation policies

A community group may use one of several governed participation modes:

```text
read_only
staff_posts_members_comment
member_posts_moderated
member_posts_immediate
facilitated_discussion
```

The group configuration determines whether members may post, comment or react.

Moderation capability and safety rules exist regardless of whether publication is pre- or post-moderated.

## 21G.5 Sensitive information boundary

General wellbeing discussion and personal experience are allowed.

Members must be warned or redirected when attempting to publish highly sensitive material such as:

- laboratory reports;
- identity documents;
- detailed diagnoses;
- medication lists;
- detailed trauma histories;
- private practitioner correspondence;
- detailed consultation requests;
- another person's private health information.

The platform may request editing, hide or remove unsafe disclosures and retain restricted moderation evidence where required.

No participant is pressured to disclose trauma or private medical history publicly.

## 21G.6 Peer health-advice boundary

Members may describe personal experience.

Community participants may not present themselves as providing platform-approved individual medical treatment unless separately authorised.

Prohibited examples include:

- diagnosing another participant;
- telling another participant to start, stop or change medication;
- prescribing medication or supplement doses;
- promoting dangerous restriction, purging or unsafe fasting;
- contradicting an active safety restriction;
- guaranteeing treatment or weight-loss outcomes;
- presenting unverified claims as official Voelgoed guidance.

Moderators are not converted into clinicians merely because a post is health-related.

## 21G.7 Moderation lifecycle

Use an explicit moderation case lifecycle:

```text
reported
→ triaged
→ under_review
→ action_required
→ action_taken
→ appealed
→ appeal_review
→ upheld_or_reversed
→ closed
```

Not every case uses every state.

Moderation records must preserve:

- report category;
- reporter protection;
- content/evidence reference;
- severity;
- reviewer;
- reason;
- action;
- timestamps;
- appeal history.

Evidence is restricted and is not copied into ordinary analytics.

## 21G.8 Reports, sanctions and appeals

Report categories may include:

```text
harassment
spam
health_misinformation
dangerous_advice
privacy
impersonation
inappropriate_content
crisis_or_urgent_risk
fraud
other
```

Available actions may include:

```text
no_action
education_or_warning
request_edit
hide
remove
posting_restriction
temporary_suspension
ban
urgent_redirect
```

Severe privacy, safety, fraud or harassment cases may receive immediate restriction.

A ban applies to the governed identity, not merely one display profile.

Eligible moderation decisions permit one governed appeal. Independent review is preferred where operationally possible.

## 21G.9 Direct messaging

Unrestricted member-to-member direct messaging is excluded initially.

Any future first-party messaging requires:

- mutual-consent or otherwise explicit initiation rules;
- blocking;
- reporting;
- rate limits;
- abuse controls;
- retention rules;
- moderator/evidence access boundaries;
- clinical-advice boundaries.

Do not create DMs merely to reproduce a generic social network.

## 21G.10 Community data after membership ends

When community entitlement ends:

- the participant cannot create new entitled activity;
- previous posts may remain where discussion integrity requires it;
- deletion or anonymisation may be available under GQ-010;
- moderation evidence may remain restricted under its retention policy;
- private health data is never retained merely to preserve community context.

## 21G.11 Challenge modes

The challenge model supports governed reusable modes such as:

```text
individual_private
group_private
community_group
programme_linked
event_linked
sponsored
facilitated
```

Every challenge defines:

- eligibility;
- entitlement;
- privacy;
- duration;
- activities;
- safe metrics;
- completion rules;
- facilitator rules;
- safety behaviour;
- version.

Challenges must reuse central habits, programme, safety, content and entitlement concepts rather than inventing parallel systems.

## 21G.12 Challenge metrics and recognition

Suitable challenge measures may include:

- participation;
- completed activities;
- consistency;
- recovery;
- milestones;
- non-weight wellbeing outcomes.

Do not use public competitive rankings for:

- body weight;
- body measurements;
- calorie restriction;
- fastest weight loss.

Recognition may celebrate participation and consistency without implying medical success.

## 21G.13 Challenge safety

A relevant safety change may:

- pause an affected challenge activity;
- restrict an unsafe activity;
- present a private explanation;
- offer an approved safe alternative;
- route to professional review where required;
- allow the participant to leave without penalty.

A safety block is not treated as failure.

## 21G.14 Live-session access and Q&A

Live sessions use explicit access modes such as:

```text
public
free_account
member
programme
premium
ticketed
practitioner
invite_only
```

Registration may include capacity, waiting-list and entitlement checks.

Joining instructions are protected.

Attendance records avoid exposing private participant identity unnecessarily.

Group Q&A is moderated and may classify questions as:

```text
general_education
temperament
programme
faith
community
product_support
clinical_private_redirect
not_appropriate_for_group
```

Group Q&A does not provide private diagnosis, prescription or treatment.

## 21G.15 Recording and replay governance

A recorded session requires:

- explicit recording notice;
- participant/speaker consent rules;
- attendee privacy controls;
- handling of sensitive audience material;
- governed editing;
- replay entitlement;
- replay expiry where applicable;
- content/version history;
- correction and withdrawal;
- separate approval for promotional clips.

A recording is not automatically public merely because the live session occurred.

## 21G.16 Restream and Cloudflare direction

Restream is the provisional production/multistream tool, subject to operational and plan validation.

The preferred platform path is:

```text
presenter / production tool
→ Restream
→ social destinations
→ custom RTMPS output
→ Cloudflare Stream
→ entitlement-controlled platform player
→ recorded asset
→ governed replay
```

Phoenix/Ash own:

- session metadata;
- registrations;
- entitlements;
- policy decisions;
- replay publication;
- captions/transcript metadata;
- consent/audit;
- analytics.

Do not build a self-hosted RTMP/transcoding service for the first release.

## 21G.17 Event model

Use the conceptual structure:

```text
Event
→ EventVersion
→ EventOccurrence
→ TicketType
→ TicketEntitlement
```

An occurrence defines at least:

- date/time/timezone;
- venue or delivery mode;
- capacity;
- sales window;
- ticket configuration;
- refund/transfer policy version;
- linked digital entitlements;
- attendance rules.

Reserved seating is a later capability unless a release explicitly requires it.

## 21G.18 Capacity and checkout reservations

For general-admission capacity:

```text
available capacity
→ short checkout reservation
→ verified payment confirmation
→ issued entitlement/ticket

or

reservation expiry
→ capacity released
```

Rules:

- confirmed capacity must never oversell;
- all allocations count against authoritative capacity;
- reservation and payment handling are idempotent;
- waiting lists may allocate released capacity through governed rules;
- displayed availability may be cached;
- final confirmation uses authoritative concurrency-safe truth.

Flash-sale implementation details remain an architecture/performance gate.

## 21G.19 Purchaser, ticket holder and attendee

Keep separate:

```text
purchaser
ticket_holder
attendee
```

Paying for a ticket does not automatically grant access to another attendee's private account or health information.

Transfers follow the event policy.

## 21G.20 Ticket lifecycle and check-in

Ticket state may include:

```text
reserved
pending_payment
issued
transferred
checked_in
cancelled
refunded
credited
expired
voided
```

A valid ticket cannot be successfully checked in twice.

Manual recovery must be auditable.

Future offline check-in must reconcile safely rather than creating duplicate attendance.

## 21G.21 Event policy

Every event has a versioned policy accepted before checkout.

It may define:

- cancellation;
- refunds;
- transfers;
- future credit;
- no-show;
- organiser cancellation;
- postponement;
- delivery-format change;
- force majeure;
- bundled digital entitlements;
- partial consumption.

Bulk event actions such as cancellation communications, refunds and entitlement changes must be idempotent.

## 21G.22 Community, live and event analytics

Collect the minimum events needed for:

- access;
- engagement;
- moderation load;
- live attendance;
- replay usage;
- sales;
- reservation conversion;
- check-in;
- refund/transfer behaviour.

Do not copy post bodies, journals or detailed health data into general analytics.

Operational dashboards should use cached/materialised aggregates and suitable Redis counters.

PostgreSQL remains durable truth for moderation cases, issued tickets and entitlements.



# 21H. Locked GQ-NY-001 Nuwe Jy Flagship Product Rules

This section records the approved product model for **Nuwe Jy – 60 Dag Uitdaging**.

Nuwe Jy is not a LearnDash course migration.

It is a first-class, cohort-led, temperament-guided transformation programme delivered through a structured 60-day challenge experience.

## 21H.1 Strategic position

Nuwe Jy is the first flagship vertical expansion after the core account, assessment, safety, payment, entitlement and plan foundation.

Its requirements influence architecture from the beginning, but the full 60-day product does not belong inside the absolute smallest MVP.

It must act as an architecture acceptance test for the reusable Programme, Content, Safety, Plans, Entitlements, Notifications, Community, Live and Analytics domains.

## 21H.2 Delivery model

Flagship delivery uses scheduled cohorts.

A later evergreen edition may reuse an approved programme version with different scheduling, support and community rules.

Use:

```text
Nuwe Jy Programme
→ approved ProgrammeVersion
→ ChallengeEdition
→ one or more Cohorts
```

## 21H.3 Meaning of 60 days

Nuwe Jy uses a guided 60-calendar-day rhythm.

Rules:

- the cohort has a shared 60-day schedule;
- missed days do not reset progress;
- participants may recover and catch up;
- required work remains visible;
- the system recommends the next smallest useful action;
- the cohort may formally conclude while approved individual catch-up remains open;
- completion does not require perfect adherence.

## 21H.4 Today experience

The participant receives a dedicated Today view containing the relevant combination of:

```text
today_focus
lesson
practical_action
habit
reflection
check_in
live_session
community_prompt
progress
recovery_action
```

The participant may also:

- resume where she stopped;
- enter guided catch-up;
- view upcoming items;
- view completed history;
- browse permitted programme structure.

## 21H.5 Preconfigured daily drip

All 60 days are configured and approved before the edition begins.

Daily releases are:

- timezone-aware;
- idempotent;
- observable;
- recoverable;
- protected against duplicate release;
- independent of daily administrator action.

Every edition validates its full release calendar before activation.

## 21H.6 Composable day structure

A day may contain controlled components such as:

```text
teaching
video_or_audio
scripture_or_devotional
practical_action
habit
meal_or_lifestyle_guidance
reflection
check_in
download
community_prompt
live_session
rest_or_recovery_day
```

Not every day requires every component.

Do not turn the programme into an unrestricted page builder.

## 21H.7 Temperament adaptation

Temperament may adapt:

- framing;
- visible detail;
- amount of choice;
- action wording;
- reminder tone;
- accountability suggestions;
- reflection prompts;
- recovery messaging;
- optional recommendations.

Temperament does not change:

- health truth;
- faith truth;
- safety rules;
- core programme requirements.

No dynamic AI rewrite replaces approved content.

## 21H.8 Progress

Use private multi-dimensional progress including appropriate combinations of:

- content completed;
- actions attempted;
- habits followed;
- reflections completed;
- check-ins completed;
- milestones reached;
- recovery after interruption;
- participant-selected non-weight outcomes.

No public weight, calorie-restriction or fastest-completion leaderboard is permitted.

## 21H.9 Cohort community

Each flagship edition has a governed cohort community.

Initially this may use a dedicated Facebook group.

Later the first-party platform may support:

- edition-linked groups;
- facilitator posts;
- daily prompts;
- moderated member posts;
- milestones;
- optional accountability;
- announcements;
- safe discussion boundaries.

Participant progress is never automatically shared.

## 21H.10 Live sessions and replays

Live sessions link directly to the edition/cohort.

The programme may expose:

- next session;
- registration;
- joining instructions;
- reminders;
- attendance;
- replay;
- related lesson/discussion.

Use the shared live-video architecture rather than a Nuwe Jy-specific streaming system.

## 21H.11 Build-from-scratch rule

Do not build:

- a LearnDash importer;
- a LearnDash converter;
- a LearnDash compatibility layer.

LearnDash is only:

- source-content reference;
- media inventory;
- evidence of the existing participant experience;
- evidence of current limitations.

Do not preserve LearnDash identifiers, course hierarchy, completion states, shortcodes, drip implementation, quiz assumptions or plugin architecture as new domain truth.

Existing content is deliberately reviewed, restructured and entered into the new model.

Any exceptional legacy participant recognition is a bounded business process, not a reusable migration subsystem.

## 21H.12 Progressive onboarding and safety

Every participant completes:

- account;
- age confirmation;
- terms/privacy;
- challenge consent/boundaries;
- essential safety screen;
- preferred language;
- temperament provenance.

Temperament may be self-reported, book-derived or digitally assessed.

The deeper personalised-plan health intake remains separate.

Challenge outcomes may include:

```text
eligible_for_full_challenge
eligible_with_safe_modifications
general_wellness_components_only
professional_review_required
insufficient_information
```

Approved education, faith, community and General Wellness may remain available where personalised nutrition is blocked if safety permits.

## 21H.13 Purchaser, recipient and participant

Use:

```text
purchaser
→ purchased challenge entitlement
→ intended recipient
→ redeemed participant
→ enrolment
```

The purchaser sees commercial/redemption state only.

The purchaser cannot see:

- health;
- assessment answers;
- progress;
- journals;
- community activity;
- practitioner information.

Before redemption, reassignment may follow policy. Redeemed access is normally non-transferable.

## 21H.14 Edition configuration

A ChallengeEdition defines:

- public name;
- edition code;
- source programme version;
- sales window;
- enrolment window;
- start date;
- all 60 release dates;
- timezone;
- facilitators;
- live sessions;
- community destination;
- capacity;
- entitlements;
- pricing product;
- completion deadline;
- catch-up window;
- archive date.

Before activation validate:

- all required 60-day content;
- required translations;
- release dates;
- live sessions;
- safety material;
- facilitator coverage;
- product/payment configuration;
- community configuration;
- communication templates.

Administrators must eventually be able to configure a new approved edition without developer intervention.

Do not implement edition creation by database-record cloning.

## 21H.15 Late enrolment

Each edition defines:

```text
closed_at_start
open_for_defined_window
manual_exception_only
rolling_start_not_allowed
```

Where late enrolment is allowed:

- the participant joins the cohort's current day;
- missed content is handled through guided catch-up;
- she is not expected to complete every missed item immediately;
- required safety/foundation items may still gate progression;
- daily release remains tied to the cohort;
- notification delivery begins from enrolment;
- completion/catch-up windows remain explicit.

Do not silently convert a cohort entrant into an unrelated personal 60-day schedule.

## 21H.16 Roles

Use scoped roles such as:

```text
challenge_owner
programme_admin
cohort_manager
facilitator
community_moderator
live_session_host
support_agent
clinical_reviewer
data_analyst
```

Facilitators may receive only appropriate non-clinical information such as:

- participant display names/roster;
- enrolment state;
- broad participation state;
- milestones;
- participant-submitted facilitator questions;
- moderation tools where separately assigned.

Facilitators do not automatically see:

- diagnoses;
- medication;
- assessment answers;
- plans;
- journals;
- weight;
- laboratory data;
- professional records.

Clinical access is a separate consented role.

## 21H.17 Daily and milestone check-ins

Lightweight daily interaction may capture:

- whether the day's focus was viewed/completed;
- whether the practical action was attempted;
- manageability;
- approved optional energy/hunger/mood/sleep marker;
- request for catch-up help;
- optional private reflection.

Deeper milestone check-ins may occur at versioned points such as:

```text
baseline
day_7
day_14
day_30
day_45
day_60
```

The exact schedule remains programme-versioned and clinically/product reviewed.

Journals remain separate and private.

## 21H.18 Support routing

Use deterministic outcomes such as:

```text
continue_normally
show_recovery_path
simplify_upcoming_actions
pause_nonessential_reminders
offer_general_support_content
suggest_group_QA
recommend_professional_review
safety_pause
urgent_help_information
```

Ordinary difficulty triggers self-service recovery first.

Facilitators receive only appropriate non-clinical signals.

Clinical concerns use the Safety domain.

The programme does not imply unlimited coaching or guaranteed clinical follow-up.

## 21H.19 Plan integration

A Nuwe Jy package may include:

- assessment;
- personalised seven-day plan;
- General Wellness pathway;
- challenge;
- programme;
- community;
- live sessions.

Eligibility determines the plan pathway.

Nuwe Jy references the current authoritative approved plan and does not copy mutable plan data into challenge progress.

Plan correction, withdrawal or safety pause immediately changes dependent guidance.

There is no separate Nuwe Jy nutrition engine.

## 21H.20 Completion and certificate

Versioned completion criteria may require:

- safety acknowledgements;
- required foundation lessons;
- approved proportion of required activities;
- milestone check-ins;
- final reflection/check-in;
- no unresolved completion-blocking requirement.

Possible outcomes:

```text
completed
completed_with_optional_items_remaining
participated
partially_completed
withdrawn_for_safety
abandoned
```

Approved catch-up may allow completion after cohort day 60.

Certificates indicate participation/completion only and never claim medical competence, guaranteed transformation or weight loss.

## 21H.21 Communication journey

An edition may preconfigure:

- purchase confirmation;
- redemption reminder;
- incomplete-onboarding reminder;
- preparation;
- start welcome;
- daily release;
- live-session reminder;
- recovery support;
- milestone message;
- midpoint;
- day-60 conclusion;
- catch-up;
- certificate;
- replay;
- archive notice.

Messages obey:

- participant language;
- timezone;
- quiet hours where applicable;
- completion suppression;
- separation of operational/safety from marketing;
- idempotency;
- deduplication;
- bounded retry;
- constrained facilitator bulk-send authority.

## 21H.22 Operational dashboards

Role-scoped dashboards may cover:

**Commercial**
- sold;
- pending payment;
- redemption;
- refund;
- sponsored places.

**Onboarding**
- account;
- consent;
- safety;
- assessment;
- enrolment readiness.

**Programme**
- started;
- current cohort day;
- release state;
- engagement;
- milestones;
- recovery;
- completion outlook.

**Operations**
- notification failures;
- release failures;
- video/replay state;
- support load;
- moderation load;
- capacity.

**Safety**
- aggregate routing;
- authorised professional case queues only.

Journals and full clinical records are not exposed on general programme dashboards.

## 21H.23 Analytics and repeat participation

Measure appropriate events such as:

- purchase/redemption;
- onboarding;
- start;
- daily/weekly participation;
- milestones;
- recovery;
- live/replay use;
- community participation;
- completion;
- usefulness;
- non-weight outcomes;
- safety routing;
- support/moderation demand;
- repeat enrolment;
- membership conversion.

Repeat participation creates a new enrolment while preserving earlier history.

## 21H.24 Legacy cutover

Use a clean product cutover:

- complete current LearnDash obligations under existing promises;
- use old content only as source/media reference;
- launch a named future Nuwe Jy edition entirely on the new platform;
- do not split one cohort across the old and new systems;
- preserve required historical business evidence outside the new programme domain;
- manually handle exceptional legacy recognition where justified;
- retire LearnDash after contractual, support and retention obligations are satisfied.

Do not map LearnDash completion percentages into the new progress model as if they were equivalent.



# 21I. Locked GQ-010 Privacy, Records and Data-Lifecycle Rules

This section records the approved closure, deletion, consent, retention, export, correction, backup and incident model.

Exact legal, financial and professional retention durations remain expert-owned.

## 21I.1 Shared lifecycle vocabulary

Use shared category-aware states where applicable:

```text
active
archived
access_restricted
deletion_requested
deletion_pending
anonymised
deleted
retained_by_obligation
legal_hold
```

Lifecycle state is separate from a record's business state.

Transitions record reason, authority, timestamp and applicable policy version.

Deletion processing must be idempotent.

## 21I.2 Account closure

Account closure is distinct from full deletion.

Closure:

- revokes active sessions;
- disables login;
- stops optional processing and communication;
- applies subscription cancellation rules;
- preserves eligible records/purchased access during a recovery window.

The recoverable closure period is:

```text
30 days
```

Recovery requires strong verification.

Subscriptions do not restart automatically.

## 21I.3 Full deletion

Full deletion is deliberately irreversible after execution.

Process:

```text
full deletion requested
→ normal access revoked
→ optional processing stopped
→ 14-day cancellation window
→ category-specific deletion/anonymisation/restricted retention
→ deletion completion
```

Before execution, explain consequences and permit a secure export.

After completed deletion:

```text
no account recovery
no entitlement restoration
no personalised-plan reconstruction
no journal recovery
no health-profile restoration
no reconstruction from transactions, backups or retained records
```

A returning person may create a new account, but it is a new identity relationship.

## 21I.4 Verification for destructive actions and export

Use risk-based step-up verification.

Controls may include:

- recent authenticated session;
- credential re-entry;
- MFA where configured;
- verified-email confirmation;
- stronger verification for sensitive export/deletion;
- governed manual recovery if normal authentication is unavailable.

Do not collect identity documents for routine actions unless proportionate verification cannot otherwise be achieved.

## 21I.5 Assessment records under deletion

Assessment immutability applies while records exist; it does not require indefinite identifiable retention.

For approved full deletion:

- eligible submitted answers, scores and reports are deleted or irreversibly anonymised;
- raw historical values are never silently rewritten;
- irreversibly anonymous aggregate statistics may remain;
- legal/professional/fraud/dispute holds may delay specific destruction;
- product report access ends.

## 21I.6 Plans, programmes and entitlements

Full deletion ends future access to:

- assessment reports;
- personalised plans;
- programmes;
- participant progress;
- account-linked entitlements.

Eligible private snapshots are deleted/anonymised according to policy.

Minimum commercial evidence may remain separately restricted.

Generic platform IP/content remains platform property.

Earlier "permanent access" decisions mean durable purchased access while the account relationship exists; they do not override an explicit completed full deletion.

## 21I.7 Self-guided health records

For full deletion:

- delete or irreversibly anonymise eligible self-guided health/check-in data;
- remove it from personalisation;
- invalidate derived relevance flags;
- remove search/index/cache copies;
- stop future processing.

## 21I.8 Professional records

Formal professional records follow their approved professional retention obligations.

While retained:

- remove them from ordinary platform use;
- restrict access to authorised recordkeeping/professional functions;
- exclude them from marketing, feeds and ordinary analytics;
- preserve participant access where applicable;
- use addenda for corrections rather than destructive rewriting;
- delete when the approved obligation ends.

## 21I.9 Journals

Private journals receive strong deletion treatment.

For full deletion:

- delete eligible entries;
- delete eligible attachments;
- invalidate caches/indexes;
- delete future embeddings or AI-derived summaries if ever created;
- exclude journal text from analytics.

If a journal excerpt was explicitly incorporated into a professional record, the professional copy follows that separate record policy.

## 21I.10 Uploaded files and laboratory assets

Complete deletion covers:

- original object;
- derivatives;
- thumbnails/previews;
- extracted structured values;
- search indexes;
- cached links;
- signed-link capability;
- superseded files;
- worker temporary files.

Deleting only a database row is insufficient.

## 21I.11 Community contributions

Use content-sensitive deletion/anonymisation.

Possible actions:

- delete standalone content;
- anonymise content required for discussion continuity;
- remove profile links/public identifiers;
- retain restricted moderation evidence;
- preserve independently authored third-party context;
- delete uploaded media separately where eligible.

## 21I.12 Commercial records

Retain only records required for tax, accounting, payment, refund, chargeback, dispute or legal purposes.

Rules:

- isolate them from the active participant profile;
- minimise identity fields;
- restrict access;
- exclude them from marketing/personalisation;
- never use them to reconstruct the deleted account;
- delete/anonymise when the approved retention period ends.

## 21I.13 Consent withdrawal

Consent withdrawal stops the affected processing and recalculates dependent capability.

Examples:

- marketing withdrawal stops marketing;
- feed-personalisation withdrawal removes affected ranking signals;
- practitioner-sharing withdrawal ends future practitioner access;
- research withdrawal stops future research inclusion;
- optional AI consent withdrawal disables that feature;
- withdrawal of required programme consent may pause/end that capability.

Withdrawal is timestamped and audited.

Dependent caches, flags and active permissions are invalidated.

Prior lawful processing is not rewritten.

## 21I.14 Audit logs

Use immutable, minimised and category-specific audit retention.

An audit entry may record:

- actor;
- action;
- target category;
- timestamp;
- access reason;
- outcome;
- policy result;
- correlation identifier;
- limited change summary.

Do not duplicate full sensitive health payloads inside audit logs.

Ordinary administrators cannot rewrite audit history.

Evidence proving deletion/consent withdrawal may remain under its approved retention rule.

## 21I.15 Security events

Retain minimised security evidence for an approved period.

Examples:

- failed-login patterns;
- account takeover;
- MFA change/reset;
- suspicious recovery;
- abuse-prevention outcomes;
- confirmed fraud;
- deletion verification.

Use security-specific or pseudonymous identifiers where possible.

Do not use security records for marketing/personalisation.

## 21I.16 Analytics after deletion

Remove identifiable event-level analytics and preserve only irreversibly aggregated statistics where re-identification is not reasonably possible.

Rules:

- delete/anonymise participant identifiers;
- stop future collection;
- use small-group suppression where appropriate;
- do not rebuild analytics identity from finance/security records;
- send required deletion instructions to external processors.

Journals and detailed health data must not enter general analytics in the first place.

## 21I.17 Inactive accounts

Use staged inactivity management such as:

```text
active
→ inactive_warning
→ dormant
→ restricted_archive
→ eligible_for_deletion_or_anonymisation
```

Periods vary by record/entitlement type.

Notify participants before material action where possible.

Dormancy stops unnecessary processing/notifications.

Professional, dispute, financial and legal-hold records follow separate obligations.

Dormant-account recovery never reconstructs a fully deleted account.

## 21I.18 Deceased participants

Use a verified deceased-participant process.

Possible actions:

- freeze account access;
- stop subscriptions/optional communication;
- verify lawful authority;
- provide only legally permitted information;
- apply professional/financial/legal retention;
- close/delete remaining records under verified instruction;
- prevent impersonation/reactivation.

A relative does not automatically receive journals, health records or practitioner notes.

## 21I.19 Legal holds

Use scoped legal holds.

A hold defines:

- exact records;
- purpose;
- authority;
- owner;
- start date;
- review date;
- release condition.

Hold only what is necessary.

Allow unrelated deletion where possible.

Held data is not used for marketing, feeds or ordinary analytics.

Resume the deletion process after the hold ends.

## 21I.20 Backups

Backups are for disaster recovery, not participant recovery.

Deleted records may remain in encrypted backups only until normal backup expiry.

Rules:

- backup access is restricted;
- no ordinary retrieval of deleted accounts;
- restore into controlled recovery process;
- replay completed deletion and consent-withdrawal events before normal service resumes;
- verify deleted identities do not reappear;
- securely expire backups according to policy;
- never restore one participant's deleted account on request.

## 21I.21 Participant export

Provide a human-readable package plus structured data.

Formats may include:

```text
PDF
JSON
CSV
original_uploaded_files
```

Eligible categories may include:

- profile;
- consent history;
- assessments;
- health profile;
- plan history;
- programme/habit progress;
- journals;
- appropriate practitioner-shared records;
- purchases/entitlements;
- community contributions;
- uploads;
- access/sharing history where applicable.

Use strong verification, asynchronous generation for large exports, secure short-lived delivery, redaction where required and audit.

## 21I.22 Corrections

Use record-specific correction:

- profile fields may update with history where necessary;
- submitted assessments use additive correction/new permitted attempt;
- plans use superseding versions;
- professional records use addenda;
- financial records use credit/refund/adjustment records;
- community content follows moderation-aware editing;
- derived flags are recalculated/inactivated.

Support may not overwrite historical truth directly in the database.

## 21I.23 Incident records

Maintain a minimised restricted incident record with:

- incident type;
- discovery/containment/closure times;
- affected categories;
- necessary identifiers;
- system/provider impact;
- actions;
- notifications;
- legal/regulatory decisions;
- remediation;
- evidence references;
- post-incident review.

Link to evidence rather than copying full health records.

## 21I.24 Versioned retention policy and deletion completion

Every record category defines:

- purpose;
- lawful/operational basis;
- owner;
- active period;
- archive period;
- deletion/anonymisation action;
- exceptions;
- legal-hold behaviour;
- backup expiry;
- external processor handling;
- approval authority;
- policy version/effective date.

A full deletion is complete only when:

- live access is revoked;
- eligible DB records are deleted/anonymised;
- files/derivatives are processed;
- caches/indexes are invalidated;
- derived flags are removed;
- external processors receive required requests;
- retained finance/professional/security/legal records are isolated;
- the 14-day cancellation window has passed;
- no account recovery or reconstruction path remains;
- completion is auditable.



# 21J. Locked GQ-011 Identity, Security, Notifications and Operational Resilience Rules

This section records the approved authentication, privileged-access, abuse-prevention, notification, resilience, incident and observability model.

## 21J.1 Participant authentication

Launch supports:

- email and password;
- secure password reset;
- optional email magic-link sign-in;
- verified email for sensitive capability;
- future passkeys where justified.

Social login is deferred until a proven acquisition/usability need exists.

## 21J.2 Email verification gates

An unverified user may:

- select language;
- complete basic profile setup;
- browse permitted public/free content;
- request another verification message.

Verified email is required before:

- paid purchase;
- paid entitlement redemption;
- temperament assessment;
- health-data entry;
- personalised plan;
- member community;
- sensitive export;
- account deletion.

## 21J.3 Participant MFA

Participant MFA is optional.

Step-up authentication is required for high-risk actions such as:

- primary-email change;
- disabling MFA;
- sensitive export;
- full deletion;
- unusually sensitive professional-record access;
- sign-out-all-devices;
- security-setting changes following suspicious activity.

## 21J.4 Staff and practitioner MFA

MFA is mandatory for all staff and practitioners.

Rules:

- no privileged access without MFA;
- stronger authenticators are preferred for higher-risk roles;
- MFA reset is governed/audited;
- privileged users cannot approve their own privileged recovery;
- shared accounts are prohibited.

## 21J.5 Sessions

Use role- and risk-based session policy.

Participants:

- reasonable persistent sessions;
- inactivity expiry;
- absolute expiry;
- step-up for sensitive actions.

Staff/practitioners:

- shorter inactivity;
- shorter absolute duration;
- reauthentication for sensitive records.

All users may view active sessions, revoke individual sessions and sign out all devices.

## 21J.6 Trusted devices

Trusted devices are:

- participant-consented where applicable;
- expiring;
- revocable;
- nameable;
- invalidated by suspicious access or key credential/security changes.

Trusted status never bypasses required high-risk step-up authentication.

Privileged users use stricter device policy.

## 21J.7 Account recovery

Use graduated recovery.

Normal recovery may use:

- verified email;
- expiring single-use links;
- MFA;
- recovery codes;
- sensitive-session invalidation;
- verified-channel notification.

When ordinary recovery is unavailable:

- use governed manual verification;
- apply a temporary security hold;
- block immediate email/MFA/export/deletion changes;
- require second-person approval for privileged accounts;
- audit the full recovery.

## 21J.8 Primary-email change

Use:

```text
reauthenticate
→ confirm new email
→ notify old email
→ risk-based security delay
→ session review/revocation
→ audit
```

If the old email is unavailable, use governed recovery rather than an informal support override.

## 21J.9 Duplicate accounts and merge

Never merge by name or demographics alone.

Verify control of both identities where practical.

Review domain records separately:

- purchases;
- entitlements;
- assessments;
- health profiles;
- plans;
- journals;
- community identity;
- professional records.

Preserve immutable histories and original finance/professional provenance.

Resolve conflicting current-profile choices explicitly.

High-risk merges require staff review.

## 21J.10 Compromised account

Possible containment actions:

- revoke all sessions;
- remove trusted devices;
- suspend sensitive actions;
- require credential reset;
- review MFA;
- freeze email changes, exports, sharing and deletion;
- notify verified channels;
- preserve minimised incident evidence;
- review recent sensitive access;
- restore only after verified recovery.

Privileged compromise escalates immediately.

## 21J.11 Privileged-role grants

Every grant records:

- subject;
- role;
- scope;
- reason;
- approver;
- start date;
- expiry or review date;
- organisation/practitioner relationship;
- revocation history.

Apply least privilege and time-limited elevation where practical.

Technical administration never grants clinical authority.

Sensitive roles cannot be self-approved.

Employment/practitioner termination triggers prompt revocation.

## 21J.12 Break-glass and production access

Emergency access requires:

- named identity;
- strong MFA;
- explicit reason;
- narrow scope where possible;
- short expiry;
- immediate audit event;
- alert to designated owners;
- post-access review.

No shared credentials.

Developers do not have routine health-record access.

Support uses reason-coded, impersonation-safe tooling.

Direct database access is exceptional.

Production participant data is not copied into local development.

Emergency access never grants clinical authority.

## 21J.13 Registration, login and recovery abuse

Use layered protection:

```text
Cloudflare edge controls
→ application rate limits
→ Redis-backed velocity counters
→ account/device/network risk signals
→ temporary challenge_or_lockout
```

Protect:

- registration;
- login;
- password reset;
- magic-link requests;
- MFA verification;
- email changes;
- account recovery.

Rate limits work across nodes.

Do not use PostgreSQL as the immediate high-velocity counter store.

Lockouts are temporary/recoverable and privileged accounts receive stricter response.

## 21J.14 Redemption abuse

Use:

- high-entropy codes;
- Redis-backed attempt limits;
- account/device/network throttling;
- single-use or explicit usage counts;
- expiry;
- entitlement-level idempotency;
- audit;
- fraud escalation.

Failure responses must not reveal whether a guessed code was otherwise real.

## 21J.15 Payment and checkout abuse

Use provider verification plus platform controls against:

- duplicate submissions;
- repeated failures;
- promotion abuse;
- refund abuse;
- webhook replay;
- duplicate entitlement granting;
- suspicious account/payment mismatch.

Provider webhooks are verified and idempotent.

Entitlements grant once.

Durable payment truth remains in PostgreSQL.

Hot velocity counters may use Redis.

## 21J.16 File-upload security

Every upload follows:

```text
temporary_restricted_upload
→ size/type validation
→ MIME/content inspection
→ malware scan
→ metadata sanitisation where appropriate
→ durable storage
→ governed access/publication
```

Private files are never public by default.

Signed URLs expire.

Unsafe formats and failed scans never publish.

Heavy processing is asynchronous.

## 21J.17 Scraping and bot protection

Use:

- Cloudflare bot/rate controls;
- endpoint-specific limits;
- pagination;
- bounded search;
- public CDN caching where safe;
- authenticated download limits;
- signed protected media;
- extraction anomaly detection.

Intended public SEO remains crawlable.

Private health, plan and paid data cannot be bulk-exported through ordinary endpoints.

## 21J.18 Notification channels

Architecture supports:

```text
email
in_app
sms
whatsapp
push_future
```

Launch direction is email and in-app first.

SMS/WhatsApp may activate later after provider, cost and consent validation.

Native push is deferred until native/mobile use warrants it.

## 21J.19 Notification preferences and quiet hours

Use category-, purpose- and channel-aware preferences.

Categories may include:

```text
security
transactional
programme
habit_reminder
community
event
membership
marketing
professional
safety
```

Rules:

- essential security/transactional messages remain mandatory where necessary;
- marketing has separate consent;
- quiet hours apply to non-urgent communication;
- timezone is respected;
- frequency caps prevent overload;
- completed actions suppress obsolete reminders;
- safety overrides are separately governed.

## 21J.20 Notification delivery

Use durable asynchronous delivery:

```text
domain_event
→ durable_notification_intent
→ Oban job
→ provider
→ delivery_status
→ bounded_retry_or_terminal_failure
```

Require:

- idempotency;
- deduplication;
- exponential/provider-aware backoff;
- terminal-failure visibility;
- template/version tracking;
- correlation IDs;
- no duplicate message after retry.

PubSub may update operational dashboards.

## 21J.21 Graceful degradation and maintenance

Use explicit modes:

```text
read_only
limited_capability
full_maintenance
```

Examples:

- approved public cached content may remain available during some outages;
- checkout stops if payment verification is unavailable;
- plan generation stops if safety truth cannot be verified;
- community may become read-only;
- notifications may queue safely.

Never guess health, entitlement or payment truth.

## 21J.22 Backup/recovery tiers

Use criticality-based recovery classes.

**Tier 1**
- payments;
- entitlements;
- health;
- safety;
- plans.

**Tier 2**
- programmes;
- community;
- content operations.

**Tier 3**
- rebuildable caches;
- derived analytics.

Architecture later defines exact RPO/RTO.

Require:

- frequent/continuous PostgreSQL backup capability;
- point-in-time recovery where supported;
- encrypted off-site copies;
- object-storage durability;
- configuration/secrets recovery;
- backup expiry;
- regular restore tests;
- GQ-010 deletion-ledger replay after restore.

## 21J.23 Incident severity

Use:

```text
SEV-1 critical
SEV-2 major
SEV-3 degraded
SEV-4 minor
```

SEV-1 may include:

- health/safety integrity failure;
- major privacy breach;
- authentication compromise;
- widespread duplicate charging/entitlement corruption;
- widespread outage.

Every material incident has:

- named owner;
- timeline;
- containment;
- communication;
- remediation;
- post-incident review.

## 21J.24 Observability, queues and provider outages

Observe:

**Infrastructure**
- CPU;
- memory;
- BEAM schedulers;
- DB connections;
- Redis health;
- storage;
- network.

**Application**
- request latency;
- LiveView disconnects;
- Ash action failures;
- Oban depth/job age;
- PubSub health;
- cache hit/miss;
- external-provider latency.

**Domain**
- checkout success;
- entitlement grant;
- assessment completion;
- plan-generation failure;
- Nuwe Jy drip-release failure;
- live/replay state;
- notification delivery;
- event oversell prevention;
- safety-routing failure.

Heavy work uses Oban.

Queues use priority classes.

Safety/payment/entitlement work outranks low-priority analytics.

Backlogs alert.

Jobs are idempotent and retries are bounded.

Provider outages use explicit degraded behaviour instead of uncontrolled retry storms.

Dashboards use cached/Redis-backed aggregates rather than peak-time PostgreSQL scans.



# 21K. Mandatory Performance and Scaling Architecture Constraints

This section records project-level performance constraints that every later architecture artifact, Domain Architecture Profile, implementation-grade Domain Dossier and TOON implementation task must honour.

It does not pre-select exact module names, Redis keys, database indexes or TTLs. Platform-wide mechanisms are established during architecture; domain-level baseline implications are recorded before Roadmap sequencing; exact implementation choices are completed just in time before affected implementation slices.

## 21K.1 Data-temperature layers

Use the appropriate layer:

```text
hot
→ ETS / GenServer / Cachex
→ approximately 10 seconds to 5 minutes where appropriate

warm
→ Redis
→ approximately 30 minutes to 24 hours where appropriate

cold / durable
→ PostgreSQL

browser-local
→ localStorage / IndexedDB for explicitly safe client-side state

public static/media
→ object storage + Cloudflare CDN
```

Private health, plan, entitlement and security data must never be exposed through public cache paths.

TTL is selected per data purpose and invalidation risk rather than copied universally.

## 21K.2 Redis high-velocity structures

Where the domain requires high-velocity distributed state, prefer Redis-native structures.

Examples:

- hashes for hot shared maps/snapshots;
- sets for membership/uniqueness where appropriate;
- bitmaps for dense seat/occupancy flags if reserved seating is introduced;
- sorted sets for rate limits, expiring holds, check-in queues and time-ordered registries;
- lists/streams where an activity feed or append workflow is appropriate;
- HyperLogLog for approximate unique visitor metrics;
- cached pricing/occupancy/read models where safe.

General-admission and future reserved-seat inventory must use an explicit hold registry with expiration during high-demand sales.

## 21K.3 High-concurrency writes

Critical paths require:

- idempotency;
- optimistic or transactional locking as appropriate;
- explicit uniqueness/invariant constraints;
- DB indexes on critical query paths;
- PgBouncer in transaction mode when deployed at production scale;
- safe retries;
- no duplicate entitlement grant;
- no confirmed event oversell.

Read replicas are expected for analytics/dashboard read load when scale warrants them.

## 21K.4 Real-time operations

Use:

- Phoenix PubSub for cross-node broadcasts;
- LiveView push updates rather than client polling;
- GenServers for designated hot state aggregation;
- Redis as distributed warm/read mirror where required;
- Oban for heavy/async work.

GenServers and Redis are coordination/acceleration mechanisms, not automatic write authorities. For designated high-velocity state, architecture must explicitly define the authoritative confirmation boundary, crash/restart behaviour, reconstruction, multi-node consistency and failure semantics before choosing a coordination path.

Node-local or cache state must not become unprotected durable business truth. A process, node, cache or coordination-layer failure must not cause the platform to treat uncommitted entitlement, payment verification, confirmed capacity, safety state or other durable business state as successfully committed truth.

PostgreSQL remains durable authority for durable business state. Temporary reservation or coordination state may use another approved mechanism only where its lifecycle, expiry, reconciliation and correctness contract are explicit. Peak real-time reads should not repeatedly hit PostgreSQL when a safe hot/warm representation is justified.

## 21K.5 Flash-sale readiness

Any high-demand event/product release must design for:

- queue/admission control where needed;
- distributed rate limiting;
- expiring hold workers;
- idempotent payment/entitlement processing;
- anti-thundering-herd behaviour;
- cache-stampede protection;
- bounded retries;
- degraded-mode protection when providers fail.

## 21K.6 Analytics

Use:

- materialised views;
- precomputed/cached aggregates;
- Redis real-time counters where appropriate;
- read replicas when justified;
- streaming/pagination instead of loading large sets into memory.

Do not run large peak-time scans against primary PostgreSQL tables.

Analytics never becomes operational safety or entitlement truth.

## 21K.6A First-party experimentation

The platform must include a governed first-party **A/B/n experimentation capability** for approved web/page experiences and eligible email/message experiences.

Product-level rules:

- an experiment has one control and one or more treatment variants;
- authorised editors may create a page experiment from an eligible published experience, duplicate the control into variant drafts, and manually change approved presentation/content elements before activation;
- the normal public URL remains clean, semantic and canonical wherever technically feasible; normal treatment assignment must not depend on exposing experiment or variant identifiers in user-facing URLs;
- eligible experimental units receive stable, randomised/sticky treatment assignment according to governed allocation rules;
- actual exposure, governed primary/guardrail metrics and authoritative downstream outcomes such as verified sales/income may be compared;
- decision-bearing experiments require an approved statistical/readout design sufficient to prevent casual underpowered or opportunistic winner selection;
- experiment configuration, methodology, final aggregate result, conclusion and decision remain durable auditable institutional evidence; identifiable participant-level assignment/exposure evidence remains subject to consent, retention, deletion and anonymisation law;
- experiment results are analytical decision support and never create payment, entitlement, safety, clinical, consent or accounting truth;
- experiments may not weaken mandatory safety messages, legal/consent notices, accessibility obligations, security controls, payment verification, entitlement correctness, clinical/safety rules or other hard Product Law invariants;
- implementation libraries and exact assignment/cache/statistical mechanisms remain Architecture decisions behind platform-owned boundaries.

Experiment delivery must preserve SEO and cache correctness. Architecture must prevent a shared cache from serving one assigned treatment as another treatment merely because variants share the same canonical URL. Campaign-attribution parameters, authorised preview/debug parameters or temporary alternate test URLs may exist under separate governed rules, but they are not the normal treatment-assignment contract.

## 21K.7 Performance review required for every domain/action

Performance/scaling review occurs at two depths. This changes planning timing and granularity, not the performance or scaling obligation.

### Platform-wide baseline before Roadmap

Every mapped domain must have a Domain Architecture Profile sufficient to establish:

1. the authoritative state/data layer and broad hot/warm/cold classification;
2. whether the domain contains materially high-concurrency or latency-sensitive paths;
3. whether PostgreSQL alone is expected to satisfy the known envelope or whether an acceleration mechanism may be required;
4. major multi-node, provider-failure, queueing, streaming/pagination or rebuildability concerns;
5. obvious cross-domain performance dependencies and architectural proof needs.

This baseline must be sufficient to sequence Feature Packs without pretending that exact implementation details are already known.

### Implementation-grade review before an affected slice

Before an implementation slice is issued for an affected domain/action, its approved implementation-grade Domain Dossier and Feature Pack contract must answer, where applicable:

1. Which authoritative layer owns the durable truth?
2. Is the path safe at the required concurrency envelope, including 100,000 concurrent users where relevant?
3. Does it create avoidable database calls?
4. Is Redis required? If yes, what representation is appropriate; if not, record `NONE`.
5. Is ETS, Cachex or GenServer ownership required? If not, record `NONE`.
6. Can the result be streamed or paginated instead of loaded fully into memory?
7. What indexes are required?
8. What cache and TTL apply, or `NONE`?
9. What invalidates the cache, or `NONE`?
10. What PubSub behaviour is required, or `NONE`?
11. What Oban behaviour or priority is required, or `NONE`?
12. What happens under provider failure, retry, backlog and horizontal multi-node execution?

Acceleration must be earned by a concrete latency, concurrency or access-pattern requirement. PostgreSQL-only is a valid result where it safely satisfies the requirement. No domain is required to use Redis, ETS, Cachex, GenServer, PubSub or Oban merely because those mechanisms exist.

## 21K.8 Targets

Architecture aims for:

- sub-100 ms API latency on suitable hot/common paths;
- checkout p99 under 5 seconds where provider latency permits;
- zero confirmed overselling;
- zero duplicate entitlement grants;
- safe horizontal scaling across nodes;
- no polling for genuine real-time UI;
- bounded resource usage under backlog/load.

Correctness, clinical safety, privacy and financial integrity take priority over a latency target.


# 21L. Locked GQ-012 Launch Scope, Product Spaces, Pilot, Pricing and Release Gates

This section closes the final product Grill-Me round.

It defines the operating product-space model, first commercial release, staged rollout, launch pricing, Nuwe Jy position, membership/premium sequence, practitioner pilot, launch-readiness gates, pilot success criteria and release/rollback authority.

## 21L.1 Operating platform and controlled product spaces

Build one operating platform with controlled product spaces.

Conceptually:

```text
Voelgoed Platform
│
├── Women’s Health & Lifestyle
│   ├── Assessment
│   ├── Plans
│   ├── Nuwe Jy
│   ├── Membership
│   └── future women’s programmes
│
├── Future Men’s Product
│
└── Future Specialist Product Spaces
```

Shared platform capabilities may include:

- identity;
- authentication;
- payments;
- entitlement infrastructure;
- temperament methodology;
- content infrastructure;
- notifications;
- event/live infrastructure;
- analytics;
- audit and operations.

A product space may independently define:

- brand;
- audience;
- onboarding;
- navigation;
- products;
- programmes;
- content;
- eligibility;
- participant journeys.

This is not unrestricted generic multi-tenancy.

Sponsors, churches, employers, practitioners and event partners do not automatically become platform tenants.

Tenant-style isolation must not be introduced unless a future approved product genuinely requires it.

## 21L.2 Launch-facing product space

Only the women’s health and lifestyle product is customer-facing at first public launch.

Do not expose unfinished navigation or empty areas for:

- men;
- professional products;
- corporate products;
- partner products;
- future specialist spaces.

Nuwe Jy is a flagship product within the women’s ecosystem, not the entire platform identity.

## 21L.3 Geographic launch

South Africa is the first activated market.

Initial defaults:

```text
market
→ South Africa

currency
→ ZAR

default timezone
→ Africa/Johannesburg

launch languages
→ Afrikaans + English

payment configuration
→ South Africa first
```

Reusable platform domains must avoid unnecessary South Africa-specific hard-coding.

A future country/market requires explicit activation and review of:

- currency;
- payment support;
- tax;
- legal/consumer requirements;
- privacy;
- health/safety rules;
- emergency/urgent-support resources;
- language;
- support capability.

A successful foreign-card payment does not by itself authorise market launch.

## 21L.4 Exact core MVP product loop

The first commercially usable platform proves the full:

```text
public bilingual website
→ individual account
→ checkout
→ temperament onboarding / assessment
→ report
→ safety-focused health onboarding
→ deterministic eligibility routing
→ personalised 7-day plan
   OR
   General Wellness pathway
→ purchased-access library
→ lightweight progress / feedback
→ support and admin operations
```

The MVP is not merely an assessment product and is not a content-only launch.

It proves the central paid proposition: safe temperament-guided understanding plus useful health/lifestyle guidance.

## 21L.5 MVP temperament entry paths

Support all approved provenance paths:

```text
self_reported
book_derived
digitally_assessed
```

Provenance is always visible and retained.

The paid digital assessment remains the authoritative platform assessment experience.

A qualifying bundle may allow fast onboarding from a known temperament while preserving the included digital assessment entitlement for later use.

External/social-media quizzes do not become trusted methodology inputs.

## 21L.6 Initial commercial catalogue

The first launch catalogue contains only:

### Product 1 — Digital Temperament Assessment

Includes:

- one assessment attempt;
- durable access to the delivered report while the account relationship exists;
- applicable correction and interpretation history.

Completed full deletion ends access/recovery according to GQ-010.

### Product 2 — 7-Day Personalised Plan

Available only when:

- temperament provenance is sufficient;
- required health/safety onboarding is complete;
- the participant is eligible for the relevant automated pathway.

The General Wellness pathway remains available where product/safety rules permit it.

### Product 3 — Assessment + Plan Bundle

This is expected to be the main advertised paid offer.

Do not launch a large catalogue before the core product loop is stable.

## 21L.7 Nuwe Jy release position

Nuwe Jy is the first major native vertical expansion after the paid core MVP is proven.

Sequence:

```text
platform foundation
→ assessment
→ safety
→ plan
→ paid MVP pilot
→ harden core
→ first native Nuwe Jy edition
```

Core architecture must already support reusable programme/version/edition/cohort, scheduling, entitlement, notification, progress, community/live and recovery concepts needed by Nuwe Jy.

Do not build an abstract generic LMS before the concrete Nuwe Jy acceptance test drives the reusable programme model.

## 21L.8 Basic Membership launch gate

Do not sell Basic Membership until minimum recurring value is genuinely operational.

Minimum promised value includes:

- moderated community;
- at least one approved new/expanded member-content release per month;
- at least one live session per month;
- group Q&A submission;
- correct entitlement lifecycle;
- correct cancellation lifecycle.

Nuwe Jy may launch before or alongside early membership depending on operational readiness.

Do not sell a recurring membership on the promise that benefits will be built later.

## 21L.9 Premium and adjustment sequence

Prove the underlying recurring-adjustment capability before packaging Premium.

Sequence:

```text
stable once-off plan
→ useful progress/check-in data
→ recurring review/adjustment capability
→ plan-adjustment add-on
→ Premium bundle
```

Premium remains a named bundle of working capabilities rather than a separate parallel entitlement architecture.

Premium never means unlimited practitioner access.

## 21L.10 Practitioner-reviewed service release

Introduce practitioner review through a limited controlled pilot after automated plan delivery is stable.

Pilot rules:

- small capacity;
- explicitly authorised practitioner(s);
- separate price;
- explicit expected turnaround;
- consented active case;
- scoped health-record access;
- structured review outcome;
- no unlimited messaging;
- clear external-referral boundary.

Before wider rollout evaluate:

- demand;
- case complexity;
- median and p95 turnaround;
- professional capacity;
- follow-up demand;
- safety events;
- economics;
- support burden.

Do not create an open practitioner marketplace before the professional-service model is proven.

## 21L.11 Community release sequence

Use:

```text
core MVP
→ governed Facebook communities for Nuwe Jy / Membership
→ collect evidence
→ first-party community pilot
→ controlled migration
```

Build first-party community because evidence shows what the platform specifically needs.

Do not build a generic Facebook clone merely because external community has limitations.

## 21L.12 Live sessions and event-commerce sequence

Integrate governed live experiences early.

Early capabilities may include:

- session/event information page;
- registration;
- entitlement check;
- Nuwe Jy live-session integration;
- Restream production/distribution;
- Cloudflare Stream platform playback;
- governed replay access.

Full event commerce follows later.

Later capability may include:

- paid event catalogue;
- ticket types;
- transactional capacity reservations;
- waiting lists;
- transfers;
- check-in;
- refunds/credits;
- event bundles;
- reserved seating when an approved event requires it.

Do not force the complete ticketing platform into the initial MVP.

## 21L.13 Staged paid rollout

Use a controlled paid release progression:

```text
internal validation
→ controlled paid pilot
→ expanded paid pilot
→ limited public release
→ general public release
```

Every expansion is gated.

Feature flags may assist rollout, but they do not replace the governed product lifecycle.

Do not move to the next stage merely because technical capacity exists.

## 21L.14 First paid-pilot capacity

The first real paid pilot has a maximum of 50 participants.

Progression:

```text
internal/test accounts
→ first 10 real participants
→ review
→ expand toward 25
→ review
→ maximum 50 in first pilot
```

Expansion requires:

- no unresolved critical safety failure;
- no payment/entitlement corruption;
- reproducible plan generation;
- manageable support load;
- useful participant feedback;
- no unresolved security/privacy blocker.

After successful completion, the next controlled cohort may expand toward approximately 100–250 participants.

This is an operating release gate, not a database capacity limit.

## 21L.15 MVP launch list prices

Lock the first South African list prices as versioned business configuration:

```text
Digital Temperament Assessment
R249

7-Day Personalised Plan
R399

Assessment + Plan Bundle
R549
```

Separate list value:

```text
R249 + R399
= R648
```

Bundle saving:

```text
R99
≈ 15%
```

Rules:

- prices are configuration/data, never source-code constants;
- every price has an effective/version history;
- past orders preserve accepted price;
- product pages and checkout resolve one authoritative active price;
- promotions/discounts are separate records/rules;
- a paid pilot may use a clearly identified pilot promotion without rewriting list price.

Customer-specific AI/dynamic pricing is excluded.

## 21L.16 Basic Membership commercial planning anchor

The provisional future commercial anchor is:

```text
Basic Monthly
R199 / month

Basic Annual
R1,990 / year
```

This is approximately two months free annually:

```text
10 × R199
= R1,990
```

This is a commercial planning anchor, not a current public launch promise.

The final Basic Membership public price may be changed from evidence before that product launches.

Price changes remain versioned business configuration.

## 21L.17 Bundle strategy

Keep bundle count intentionally small.

MVP bundle model:

```text
Assessment
Plan
Assessment + Plan
```

Potential future named bundles may include:

- Nuwe Jy + Assessment;
- Nuwe Jy + Plan;
- Nuwe Jy + Assessment + Plan;
- event-linked packages;
- book-linked packages.

Each bundle grants explicit underlying component entitlements.

Do not create a parallel bundle-entitlement architecture.

Discounts should normally remain modest unless a governed campaign states otherwise.

## 21L.18 Complimentary and sponsored access

Use governed scoped access grants.

Possible grant reasons include:

```text
support_resolution
staff_testing
professional_review
marketing_campaign
founder_authorised
sponsored
competition_or_event
goodwill
```

Each grant records:

- recipient;
- exact entitlement/product;
- reason;
- issuer;
- approver where required;
- start;
- expiry where applicable;
- sponsor/campaign reference;
- audit history.

Rules:

- Support may receive tightly capped goodwill authority;
- high-value, long-duration or lifetime grants require elevated commercial approval;
- clinical authority does not automatically grant commercial authority;
- sponsors see only permitted aggregate redemption information;
- lifetime access must always name the exact scope.

Do not use one uncontrolled shared coupon as the general free-access mechanism.

## 21L.19 Native Nuwe Jy edition launch gate

A native Nuwe Jy edition may activate only after all applicable gates pass.

### Core platform

- accounts stable;
- payments/entitlements stable;
- temperament integration stable;
- safety routing stable;
- central plan integration stable.

### Programme

- approved ProgrammeVersion;
- all 60 days configured;
- all required releases scheduled;
- required translations approved;
- completion/recovery rules approved.

### Operations

- cohort manager assigned;
- facilitator coverage assigned;
- moderation coverage assigned;
- support owner assigned;
- live-session owner assigned;
- communications configured and tested.

### Safety

- Nuwe Jy screen approved;
- safe-modification rules approved;
- professional escalation available;
- urgent-help wording approved.

### Live/community

- governed cohort community ready;
- live/replay flow validated.

### Technical

- drip release tested;
- duplicate release prevented;
- notification failure visible;
- operational dashboard working;
- restore/recovery behaviour tested.

A working set of screens is not sufficient for activation.

## 21L.20 Practitioner service capacity gate

Saleable professional-review capacity is explicitly modelled:

```text
authorised practitioners
×
safe cases per practitioner per week
=
saleable capacity
```

Track:

- median turnaround;
- p95 turnaround;
- complexity distribution;
- follow-up demand;
- professional workload;
- escalations;
- safety events;
- cancellations/refunds.

Rules:

- stop selling new review places before capacity is exceeded;
- waiting lists are permitted;
- expected turnaround is visible before purchase;
- do not promise unlimited practitioner messaging;
- automation may never silently replace a purchased promised human review.

## 21L.21 Paid-pilot production readiness

The first paid pilot is a NO-GO until all required owners sign off their area.

### Product

- purchase → assessment → safety → plan journey works;
- General Wellness pathway works;
- correction and withdrawal work.

### Clinical

- assessment version approved;
- eligibility matrix approved;
- calculation protocol approved;
- safety blockers approved;
- urgent-support wording approved.

### Content

- required Afrikaans and English paid content approved;
- safety content approved;
- plan content approved.

### Commerce

- products/prices active;
- refund behaviour defined;
- payment verification tested;
- webhook idempotency tested;
- duplicate entitlement grant prevented.

### Legal/privacy

- operating authority sufficient;
- IP authority sufficient;
- terms/privacy approved;
- consent wording approved;
- retention categories sufficiently approved for pilot.

### Security

- email verification;
- staff/practitioner MFA;
- access policies;
- distributed abuse/rate protection;
- upload protection where relevant;
- audit;
- incident handling.

### Operations

- support owner assigned;
- incident owner assigned;
- backup configured;
- restore tested;
- deletion/recovery process tested;
- alerts operational;
- queue visibility operational.

Any unresolved required item is a NO-GO for the affected stage.

## 21L.22 Progressive performance and load gates

Do not require 100,000-user load to admit the first 10 participants.

Do require architecture that does not force a later redesign of authoritative domain truth.

Before the first 50-person pilot:

- critical query paths have appropriate indexes;
- no known core-journey N+1 database path remains;
- checkout/entitlement delivery is idempotent;
- generation jobs are bounded;
- required distributed Redis/rate controls operate across nodes;
- failure/retry behaviour is tested;
- no unsafe database polling exists;
- plan generation and checkout are observable.

Before broader public growth:

- load tests exceed expected near-term traffic;
- checkout p99 target remains under 5 seconds where provider latency permits;
- suitable common server/API actions target sub-100 ms;
- duplicate entitlement grants remain zero;
- event flows prove zero confirmed oversell when introduced;
- queue backlogs recover safely;
- cache stampede/thundering-herd controls are tested;
- horizontal multi-node behaviour is tested.

Architecture continues to review relevant paths against 100k concurrent-user assumptions.

## 21L.23 First paid-pilot success criteria

Use balanced commercial, product, safety, operational and behavioural evidence.

### Must-pass integrity criteria

```text
0 critical safety failures caused by platform logic
0 duplicate charges
0 duplicate entitlements
0 unreproducible delivered plans
0 unauthorised sensitive-data exposures
```

### Operational targets

Aim for:

```text
≥ 95% successful plan generation
≥ 95% successful verified entitlement fulfilment
```

All critical failures must be observable and owned.

### Product targets

Aim for:

```text
≥ 80% assessment completion among starters
≥ 80% health-onboarding completion among eligible purchasers
≥ 70% plan activation among delivered plans
≥ 60% meaningful usage during the first 7 days
```

### Value target

Aim for:

```text
≥ 70% of surveyed participants
reporting the result/plan as useful,
clear or personally relevant
```

These are pilot decision thresholds, not medical efficacy claims.

A missed non-integrity target triggers a deliberate:

```text
proceed
iterate
repeat_pilot
pause
```

decision rather than automatic abandonment or automatic expansion.

## 21L.24 Go/No-Go and rollback authority

Stage expansion requires responsible sign-off for:

```text
product / commercial
clinical / safety
technical / operations
```

No owner may waive a blocker outside that owner’s authority.

Examples:

- Technical cannot waive a clinical blocker.
- Clinical cannot declare payment integrity proven.
- Commercial cannot waive security/privacy blockers.

A designated authorised clinical/safety owner may issue an immediate safety stop.

A technical/operations owner may immediately disable a failing capability to protect:

- payment integrity;
- entitlement integrity;
- security;
- privacy;
- data integrity.

Rollback modes may include:

```text
stop_new_sales
stop_new_plan_generation
safety_pause_affected_plans
disable_specific_product
read_only
limited_capability
full_maintenance
```

Prefer the narrowest safe rollback.

Every launch/rollback decision records:

- decision;
- responsible owner;
- evidence;
- timestamp;
- reason;
- remediation;
- re-entry criteria.


# 22. Explicitly Not Yet Decided

Product Grill-Me is complete.

No unresolved **product-policy** question may now be silently invented during architecture or implementation.

Remaining work is explicitly expert-, vendor-, architecture- or operations-gated.

## 22.1 Legal, ownership and commercial expert gates

- final operating entity;
- dedicated-company decision if pursued;
- IP/licence agreement;
- temperament-model rights;
- book/content/translation/contributor rights;
- final product/platform name and branding where not architecture-critical;
- terms/privacy/consumer wording;
- practitioner agreements;
- sponsor/partner agreements;
- LearnDash retirement obligations;
- statutory/professional retention durations.

## 22.2 Clinical and methodology expert gates

- final low/moderate/high eligibility matrix;
- exact formula values, minimums, deficit ranges and macro rules;
- trend/adjustment thresholds;
- exact review timing/grace period;
- eating-disorder time boundaries where not professionally fixed;
- pregnancy/breastfeeding protocols;
- medication/supplement approved rules;
- laboratory validity matrix;
- emergency/urgent-support wording;
- score-distance/dominance/mixed thresholds;
- final Nuwe Jy safety/completion thresholds.

## 22.3 Architecture, vendor and operations gates

- final Ash domain/resource/module names;
- database schemas and migrations;
- exact indexes;
- Redis structures and key formats;
- ETS/Cachex/GenServer ownership;
- exact TTL/invalidation strategy;
- Oban queues/workers;
- PubSub topics/broadcast rules;
- API/LiveView structure;
- translation-resource implementation;
- search configuration;
- Cloudflare edge/cache rules;
- publication scheduler implementation;
- notification providers;
- Restream/Cloudflare live validation;
- recording/video consent/retention implementation;
- event reservation/flash-sale implementation;
- Facebook operating procedures;
- Nuwe Jy source inventory and operational staffing;
- external processor inventory/deletion behaviour;
- backup restore/deletion replay;
- export/deletion operations;
- authentication package/implementation;
- exact abuse thresholds;
- exact RPO/RTO;
- incident-response roster;
- per-domain hot/warm/cold mapping.

These gates are allowed to remain after the product freeze because they no longer require the architecture team to invent the product model.

If an implementation slice requires one of these unresolved values, the coding agent must STOP and raise the named gate.
# 23. Document Boundary

This document answers:

- What are we building?
- Who are we building it for?
- What value will it provide?
- What is free and what is paid?
- How will personalisation work in principle?
- Where are the clinical boundaries?
- Who may participate and in which roles?
- What does the platform refuse to become?
- What are the long-term goals?

This document does not answer:

- How Ash resources are implemented;
- which database tables exist;
- how policies are coded;
- how Redis or caching is used;
- which vertical slice is built first;
- or how deployment works.

Those matters belong in future architecture, domain and implementation documents.

---

# 24. Current Planning Stop Condition

The product Grill-Me stop condition has been met.

```text
GQ-001 through GQ-012
+ GQ-NY-001
= CLOSED
```

The current Product Law / Gate Register pack is aligned at v1.2.1. Product Grill-Me remains closed; the product model is not reopened. Historical v1.1 governance-amendment text remains preserved above.

The next allowed planning and delivery sequence is:

```text
AR-000 — Architecture Requirement Extraction
→ architecture decision workstreams
→ reference-flow pressure testing
→ 03_ARCHITECTURE.md approval
→ 04_DOMAIN_MAP.md approval
→ lightweight Domain Architecture Profile for every mapped domain
→ 05_ROADMAP.md
→ next Feature Pack skeleton + preliminary Gate Manifest
→ JIT implementation-grade Domain Dossiers for affected domains/actions
→ final Feature Pack contract
→ architectural proof: reuse existing evidence OR execute a new tracer bullet
→ vertical slices
→ evidence-driven horizontal hardening
→ release/readiness gate
```

Architecture must work backward from the ultimate platform and preserve the exact MVP as the smallest viable slice of that final system.

Planning is complete for a Feature Pack only when its upstream law, affected domain detail, blockers and proof requirements are sufficient to issue self-contained implementation tasks without invention.

**Implementation hard stop:** do not begin executable architectural proof, coding-agent vertical slices, Ash resource implementation, migrations or production infrastructure for a Feature Pack until:

1. `03_ARCHITECTURE.md` is approved;
2. the complete `04_DOMAIN_MAP.md` is approved;
3. every mapped domain has the required lightweight Domain Architecture Profile baseline;
4. `05_ROADMAP.md` identifies the Feature Pack and its dependencies;
5. the current Feature Pack contract and Gate Manifest are approved;
6. every implementation-grade Domain Dossier required by the affected domain/actions is complete;
7. every expert/vendor/clinical/legal gate required by the task is resolved, or the approved Feature Pack explicitly excludes the blocked capability;
8. the architectural-proof requirement is explicit; and
9. the current TB/VS/HH task has testable acceptance criteria and STOP conditions.

A planning or coding agent must route an insufficiency to the correct upstream authority and STOP rather than invent policy, architecture, ownership, clinical thresholds, retention durations, provider behaviour, security exceptions or missing implementation semantics.
