# NewYou Programmes & Learning Delivery Pre-JIT Discovery Working v0.16.0

- **Status:** WORKING / NON-AUTHORITATIVE / ACTIVE DISCOVERY
- **Version:** v0.16.0
- **Stream:** Programmes & Learning Delivery Pre-JIT
- **Pass:** Pass 15 — translation / version-localisation semantics
- **Created against live `main`:** `086ade7b28c000de1c387acb9760e5eb08bb0413`
- **Working branch:** `prejit/programmes-learning`
- **Direct predecessor:** `NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.15.0.md`
- **Implementation authority:** NONE
- **Authoritative-document amendment:** NONE
- **Purpose of this version:** append one focused Content & Media / Programme translation-version seam pass while preserving Passes 1–14 and their accepted working-lock boundaries.

> This is an append-only semantic successor. Nothing in this file overrides Product Law, Architecture Law, Domain Law, Roadmap, current Open Work, approved Feature Pack/JIT contracts, Content & Media authority, Programmes & Challenges authority, Safety authority, Communications authority or participant-language preferences.

> A Programme may reference governed content and require that approved content be available in the participant's chosen content language. It does not thereby own translation wording, locale-version lifecycle, language approval, fallback authority, publication state or source-language provenance.

---

# 118. Accepted working-lock status entering Pass 15

The user explicitly accepted Pass 14 and instructed the stream to continue with the next pass.

Therefore Passes 1–14 are now treated as:

`WORKING_LOCKED / NON-AUTHORITATIVE`

subject to their explicit gaps, named authority gates, deferred items and later explicit refinements.

Pass 15 inherits without reopening:

- Programme is stable conceptual/catalogue identity and ProgrammeVersion is the version-pinned participant-semantic contract;
- active Enrolments remain tied to their ProgrammeVersion unless governed migration or safety correction applies;
- Content & Media owns lesson/content body versions, locale branches/translations, approvals, publication, correction and withdrawal;
- Programmes owns lesson/activity structure references, requirement meaning, progression and completion, but not lesson/content body versions;
- source evidence and Programme satisfaction remain separate owner truths;
- Nuwe Jy Edition activation already requires validated content and translations;
- exact Programme/Nuwe Jy completion thresholds remain behind `OQ-019` / `OQ-025`;
- required-content withdrawal/unavailability with no approved replacement remains `PRG-GAP-011` and cannot be repaired through recovery or silent waiver;
- content-correction binding semantics are bounded while exact resource/index/reference mechanics remain `OQ-013` / `OQ-016` (`PRG-GAP-005`);
- post-award correction consequences remain `PRG-GAP-002` where a later governed correction invalidates the original award basis;
- interface language and content language are distinct Product concepts; and
- Pass 15 may refine translation/version-localisation semantics but may not design exact Ash resources, caches, queues, publication workers or communications journeys.

---

# 119. Pass 15 — translation / version-localisation semantics

## 119.1 Scope hard stop

This pass answers only:

1. how Programme/ProgrammeVersion references Content-owned conceptual items, immutable versions and locale variants without taking translation ownership;
2. how source locale, translation relationship, locale version and ProgrammeVersion remain separate version dimensions;
3. how Afrikaans-first and English-first content are treated symmetrically rather than assuming one universal master language;
4. how interface language, saved preferred language, selected content language and delivered content locale differ;
5. how explicit language switching during an active Enrolment affects delivery without creating a new Enrolment, ProgrammeVersion or progress history;
6. when explicit low-risk fallback is permitted and when paid/safety/core delivery must fail closed for missing translations;
7. how machine drafts, language review and clinical/safety review compose before Programme delivery;
8. how a source-version change makes dependent drafts/reviews stale and what Programmes may safely consume;
9. how Edition activation/revalidation composes with translation readiness without Programmes duplicating publication authority;
10. how content translation corrections differ from Programme semantic/version changes;
11. how material cross-language meaning drift is prevented from silently changing Programme requirement/completion meaning;
12. how historical participant delivery/progress remains explainable from exact locale/content provenance;
13. how translation withdrawal or unavailable required content composes with `PRG-GAP-011` rather than fabricating completion/substitution;
14. how post-completion translation/content corrections compose with `PRG-GAP-002` rather than silently rewriting awards;
15. how duplicate/reordered publication or invalidation observations reconcile from Content authority;
16. why locale-specific slugs, titles, presentation and content versions do not create separate Programme identity by default;
17. how reusable content blocks/media derivatives remain Content-owned while Programme structure remains stable;
18. how FP-008 and later FP-014 preserve the same translation authority seam without pulling a generic LMS/localisation engine into Programmes; and
19. whether any new Product, Architecture or Domain gap is required before later JIT.

This pass deliberately does **not** decide:

- exact Ash ContentItem/ContentVersion/Translation Resource boundaries, relationships, indexes or immutable-reference representation — `OQ-013`;
- exact scheduler, retry, stale-approval check, publication recovery or withdrawal fan-out — `OQ-016`;
- exact edge/cache purge implementation — `OQ-014`;
- exact Nuwe Jy source asset inventory, rights, duplicated material, missing translations or content remediation — `OQ-024`;
- exact Programme/Nuwe Jy completion metrics — `OQ-019` / `OQ-025`;
- exact Communications template/delivery orchestration — later dedicated pass / `OQ-027` / `OQ-036` as applicable;
- exact translation vendor/provider, machine-translation model or terminology tooling;
- exact translator staffing, SLAs or editorial workflow UI;
- legal adequacy of any translation;
- a universal language negotiation framework beyond the approved Afrikaans/English launch model;
- translation of private participant journal prose or participant-authored Community content;
- SEO implementation beyond acknowledging Content-owned locale metadata; or
- a generic cross-platform translation service or locale-specific LMS hierarchy.

---

## 119.2 Pass-15 authority evidence

### PRG-EV-206 — Live authority baseline reconfirmed

Live `main` remains `086ade7b28c000de1c387acb9760e5eb08bb0413`. README and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` continue to route Product Law v1.6.0, Decisions v1.6.0, Open Work v1.2.59, Architecture v1.1.1, Domain Map v1.2.0, Roadmap v1.2.0 and Platform Operating Model v1.0.1 as current authority. The Programmes/Learning ledgers remain working/non-authoritative.

### PRG-EV-207 — Source language is symmetric across Afrikaans and English

Product §21E.1 / `DEC-123` allow content to originate in Afrikaans or English while recording source locale and version relationship.

There is therefore no authority for a universal English-master or Afrikaans-master assumption inside Programmes.

### PRG-EV-208 — Bilingual publication is risk/access based, not optional for paid/core protected content

Product §21E.1 / `DEC-124` require both languages before publication/delivery for paid, contractual, assessment, plan, clinical, safety and core-onboarding content. Optional low-risk public editorial content may temporarily exist in one language only when availability is explicit, the missing translation is tracked and no silent machine translation is shown.

### PRG-EV-209 — Translation lifecycle is independent and governed

Product §21E.2 / `DEC-125` use independently governed translation states including missing, draft, machine draft, review, approval, publication, superseded and withdrawn. Locale branches therefore do not become valid merely because their source item or sibling locale is published.

### PRG-EV-210 — Machine translation is draft evidence only

Product §21E.2 / `DEC-126` says machine translation may create drafts only. A machine draft is labelled, never publicly visible before approval, bound to its exact source version, requires human language review, requires clinical review where health/safety is affected, and becomes stale when the source changes.

### PRG-EV-211 — Content uses shared conceptual identity with separately versioned locale variants

Product §21E.3 / `DEC-127` defines a shared conceptual content item with immutable content/translation versions rather than unrelated per-language records or one translation JSON blob. Conceptually: `ContentItem → ContentVersion → ContentTranslationVersion`.

### PRG-EV-212 — Language approval and risk approval are separate responsibilities

Product §21E.4 / `DEC-129` / `DEC-130` make risk class determine required reviewers. Afrikaans and English quality have language-review authority, while health, personalised/clinical, safety-critical and legal/consent content require their applicable professional approvals as well.

Language fluency therefore does not grant clinical/safety approval authority.

### PRG-EV-213 — Fallback is explicit and narrow

Product §21E.7 / `DEC-134` permits explicit fallback only for optional low-risk public content: tell the participant the selected translation is unavailable, explicitly offer the available language and never switch silently.

For paid, consent, assessment, plan, clinical and safety content, publication/delivery is blocked until required approved translations exist; unapproved machine fallback is prohibited.

### PRG-EV-214 — Material content edits create immutable versions

Product §21E.8 / `DEC-135` requires every material edit to create a new immutable and traceable content version. Published content is not rewritten in place merely to keep a Programme reference convenient.

### PRG-EV-215 — Content & Media owns locale/version lifecycle

Domain Law §6.7 gives Content & Media ownership of conceptual content identity, immutable content versions, locale branches/translations, approvals, publication, corrections/withdrawals and exact content/media lineage. Locale branches may advance independently subject to risk rules.

### PRG-EV-216 — Programmes owns structure and meaning, not content bodies

Domain Law §6.8 gives Programmes ownership of Programme/ProgrammeVersion/module/lesson/activity structure references, progression and completion configuration while explicitly excluding lesson/content body versions.

Therefore a Programme may reference governed Content; it may not mutate or fork translation bodies as Programme-owned truth.

### PRG-EV-217 — Delivered governed content must retain exact locale provenance

Domain Law §6.7 requires every delivered governed version to retain exact content/locale provenance. Historical Programme explainability therefore cannot rely only on "current translation" or a mutable locale label.

### PRG-EV-218 — Interface language and content language are separate Product concepts

Product §7.3 allows a participant to use one interface language while deliberately opening content in the other language. A header control may change interface language; that does not itself redefine which governed content version was delivered or which ProgrammeVersion owns the Enrolment.

### PRG-EV-219 — Nuwe Jy onboarding captures language provenance

`DEC-208` / Product §21H.12 require preferred language among the bounded onboarding facts before participation. That preference is delivery context, not a separate Programme identity or Enrolment lifecycle.

### PRG-EV-220 — Nuwe Jy Edition activation validates translations

`DEC-211` requires each Edition to be created from an approved ProgrammeVersion and to validate content, translations, schedules, sessions, safety, facilitation, products, community and communications before activation.

Translation readiness is therefore an Edition activation condition without transferring Content publication authority to Programmes.

### PRG-EV-221 — Nuwe Jy source inventory explicitly includes missing translations

`OQ-024` requires inventory of current Nuwe Jy lessons, videos, downloads, live-session assets, rights, duplicated material, missing translations and outdated content. Roadmap classifies `OQ-024` as `BLOCKS_THIS_FP` for FP-008.

Pass 15 may define the seam but cannot invent the actual source inventory or remediation list.

### PRG-EV-222 — Exact translation Resource architecture is already an owned gate

`OQ-013` is an Architecture Review gate to define exact Ash Resource boundaries, approval relationships, locale/version indexes and immutable delivery references.

The semantic owner boundary can therefore be worked now without guessing implementation representation.

### PRG-EV-223 — Publication/recovery mechanics are already an owned gate

`OQ-016` owns scheduler reliability, retry policy, alert ownership, stale-approval checks and recovery for content publication. Pass 15 must not invent worker topology or publication retry semantics.

### PRG-EV-224 — ProgrammeVersion stability is independent of locale-version advancement

Product §21F.10 / `DEC-156` keeps active participants on their enrolled ProgrammeVersion unless minor correction, governed migration or safety correction applies. A locale version changing does not by itself prove that Programme semantics changed or that an Enrolment migrated.

### PRG-EV-225 — Programme completion is versioned Programme meaning

Product §21F.9 / `DEC-155` makes completion rules versioned Programme meaning. A translator or Content correction cannot silently change what counts as required-for-progression/completion by editing wording alone.

### PRG-EV-226 — Nuwe Jy shared programme truth outranks presentation variants

`DEC-203` preserves shared health, faith, safety and programme truth while temperament adapts behavioural delivery. The same owner doctrine applies across languages: localisation may adapt wording, but cannot silently create locale-specific clinical or Programme truth.

### PRG-EV-227 — Edition release is scheduled and must remain reproducible

`DEC-201` prepares the 60-day edition in advance and releases by Edition schedule with timezone awareness, idempotency, observability and recovery. Translation choice/version is therefore delivery content provenance layered onto the same shared Edition schedule, not a locale-specific schedule engine.

### PRG-EV-228 — Required unavailable content already has an explicit Programme gap

`PRG-GAP-011` already records the unresolved consequence when required Programme content is withdrawn/unavailable and no approved replacement exists. Recovery cannot auto-waive, auto-substitute, mark complete or recommend withdrawn content.

A missing/withdrawn required translation is one way that gap can be engaged; it does not justify a new translation-specific Programme gap.

### PRG-EV-229 — Content-correction binding is already narrowed to JIT mechanics

`PRG-GAP-005` records content-correction binding as semantically resolved, with only `OQ-013` exact Resource/index/immutable-reference design and `OQ-016` publication-operation mechanics open.

Pass 15 must preserve that adjudication rather than reopening it as new architecture law.

### PRG-EV-230 — Roadmap already sequences translation gates correctly

FP-008 inherits translation readiness through Edition/content gates and blocks activation on `OQ-024`; later FP-014 classifies `OQ-013` as `BLOCKS_RELEASE_ONLY` for required bilingual programme content. The Roadmap therefore already distinguishes semantic programme modelling from exact translation-resource implementation.

No new Feature Pack or Domain is required for localisation.

---

# 120. Pass-15 semantic model

These are working semantic conclusions, not Resource/schema prescriptions.

## 120.1 Keep four version dimensions separate

A programme delivery may involve at least four independent identifiers/versions:

```text
ProgrammeVersion
ContentItem / ContentVersion
ContentTranslationVersion (locale)
participant delivery/progress provenance
```

They must not be collapsed into one "course version" or one locale-labelled blob.

- ProgrammeVersion owns participant-semantic structure/requirements.
- ContentVersion owns governed content meaning/version lineage.
- ContentTranslationVersion owns approved wording/locale lifecycle for that content lineage.
- delivery/progress provenance records what approved locale/version was actually presented when that matters for explainability.

Exact foreign keys/indexes remain `OQ-013`.

## 120.2 Do not designate a universal master language

Content may originate in Afrikaans or English.

The safe semantic model is:

```text
conceptual content identity
      ↓
source content/version with source locale
      ↓
separately governed locale variants
```

Do not encode `english_is_source = true`, `afrikaans_is_translation = true` or any equivalent permanent hierarchy in Programme truth.

## 120.3 Interface language, preference and content locale remain distinct

A participant can have:

- saved preferred interface language;
- current interface language;
- selected content language for a particular delivery/open action; and
- exact delivered ContentTranslationVersion locale.

Changing one dimension does not silently rewrite the others.

In particular, switching interface language does not:
- migrate ProgrammeVersion;
- create/restart Enrolment;
- reset progress;
- change completion state; or
- prove a different content locale was delivered.

## 120.4 Programme structure should be locale-neutral unless Product meaning truly differs

Ordinary bilingual delivery should use one Programme / ProgrammeVersion structure with Content-owned locale variants.

Separate ProgrammeVersions per language are unjustified unless Product authority intentionally defines materially different participant semantics rather than translation/localisation.

Localized titles, slugs, labels or wording do not create new Programme identity.

## 120.5 Translation readiness is Content truth consumed by Edition/Programme activation

Programmes may ask Content authority questions such as:

- is the required conceptual content/version approved?
- are the required locale variants approved/published for this risk/access class?
- is any required locale stale, superseded or withdrawn?
- what exact approved version/locale may be delivered?

Programmes may use those answers in Edition readiness/release decisions.

It must not duplicate Content lifecycle state and then treat the duplicate as publication authority.

## 120.6 Required paid/core content fails closed when required translation is unavailable

For required paid/core Nuwe Jy content, the safe default is:

```text
required locale readiness incomplete
        ↓
Edition/activity delivery cannot claim ready
        ↓
no silent sibling-locale or machine fallback
```

If Product/Content law permits a different safe correction/replacement path, it must be explicit.

A participant's fluency in the sibling language does not by itself waive the bilingual publication rule for paid/core content.

## 120.7 Optional low-risk fallback is explicit participant choice

Where Product classifies content as optional low-risk public content, fallback may be offered only by saying the selected translation is unavailable and allowing the participant to choose the available language.

The fallback is not:
- automatic;
- silent;
- machine-generated;
- proof that the missing locale is approved; or
- a general exemption from a required Programme activity.

## 120.8 Locale branches advance independently, but shared Programme truth must remain coherent

Afrikaans and English variants may have different translation version numbers and approval dates.

They may not intentionally encode different:
- activity requirement type;
- completion threshold;
- safety rule;
- clinical instruction;
- entitlement promise; or
- Programme outcome

unless a higher Product/Programme authority explicitly creates such a difference.

If a translation review discovers that the shared Programme meaning itself is wrong or must change, that is no longer a translation-only correction.

## 120.9 Source changes stale dependent translation work

When the authoritative source content version changes:

- dependent machine drafts become stale;
- dependent unapproved translations must rebind/review as required;
- a previously approved sibling translation cannot be assumed valid for the new source version merely because its text still looks similar;
- Programmes must not release from stale local copies or old approval flags.

Exact stale-check automation remains `OQ-016`/`OQ-013`.

## 120.10 Content correction and ProgrammeVersion migration are different questions

A Content-owned correction may supersede a locale/content version while the participant remains on the same ProgrammeVersion when Programme structure/requirement meaning is unchanged and the correction rules allow it.

If a proposed "translation correction" changes what the participant is required to do, what evidence satisfies the activity, what safety meaning applies, or what completion consequence follows, it crosses into Programme/Product semantics and cannot be smuggled through Content publication alone.

## 120.11 Historical delivery/progress uses exact provenance, not current translation

When explanation or audit requires it, NewYou must be able to distinguish:

```text
what ProgrammeVersion governed
what Content/Translation version was delivered
what Programme evidence/outcome was recorded
what later correction/withdrawal occurred
```

A later translation edit does not rewrite the text that was historically delivered.

## 120.12 Language switching is presentation/delivery selection, not progress migration

An active participant may deliberately switch between approved Afrikaans and English content where Product permits it.

The same Programme activity/progress remains unless Product explicitly says otherwise. The platform should not create parallel per-locale progress records or require completion in both languages merely because both variants exist.

## 120.13 Translation withdrawal does not fabricate Programme consequence

If a required translation/content version is withdrawn or unavailable:

- Content owns withdrawn/unavailable truth;
- Programmes stops recommending/delivering the invalid content as appropriate;
- Programmes does not silently mark the activity complete, exempt, substituted or failed;
- `PRG-GAP-011` governs the unresolved consequence when no approved replacement exists.

## 120.14 Later correction does not silently erase historical completion

If a participant completed an activity using an approved version valid at the time, a later ordinary translation correction does not automatically reset progress or revoke completion.

If a governed correction proves the original satisfaction/award basis was materially invalid, Programme reconciliation is required and `PRG-GAP-002` remains the post-award unresolved seam.

## 120.15 Publication observations are triggers, not authority

Duplicate, delayed or reordered publication/invalidation events may trigger Programme/Edition re-evaluation, but they do not define current Content truth by arrival order.

Before a protected release/readiness decision, reconcile from current Content-owned version/publication/approval state. Exact event/job mechanisms remain JIT.

---

# 121. Pass-15 focused pressure tests

## PRG-PT-577 — English is hard-coded as the universal source language

**Scenario:** Programme/content integration assumes every Afrikaans item is translated from English.

**Expected invariants / analysis:** Reject. Product Law permits Afrikaans- or English-origin content and requires source-locale/version relationship. Programme truth must not hard-code a universal master locale.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-578 — Afrikaans-origin lesson has an approved English translation

**Scenario:** A lesson is authored in Afrikaans and later translated/approved in English.

**Expected invariants / analysis:** One conceptual Content identity may have separately versioned locale variants. Programme structure remains shared; source provenance records Afrikaans.

**Disposition:** `PASS`.

---

## PRG-PT-579 — One ProgrammeVersion is created per language

**Scenario:** Nuwe Jy English and Afrikaans are modelled as two ProgrammeVersions solely because wording differs.

**Expected invariants / analysis:** Reject by default. Content locale/version is Content-owned; ProgrammeVersion is participant-semantic structure. Separate ProgrammeVersions require a real semantic Product difference, not translation alone.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-580 — One Enrolment is created per language

**Scenario:** Participant switches from Afrikaans to English and the system creates a second Enrolment.

**Expected invariants / analysis:** Reject. Language selection does not create another programme attempt or duplicate progress.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-581 — Content-language switch resets progress

**Scenario:** Participant changes to the other approved language mid-Programme and prior completions disappear.

**Expected invariants / analysis:** Reject. Programme activity identity/progress remains shared unless explicit Product semantics say otherwise.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-582 — Interface-language switch silently switches content language

**Scenario:** Header UI is changed to English and the current Afrikaans governed lesson is silently replaced with English.

**Expected invariants / analysis:** Interface language and content language are distinct. Do not infer content-locale delivery without the governed selection/fallback rule.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-583 — Participant explicitly opens the sibling approved locale

**Scenario:** Afrikaans-interface participant deliberately chooses the approved English lesson variant.

**Expected invariants / analysis:** Permitted where Product access/risk rules allow it. Delivery provenance records the actual locale/version; Programme progress remains on the same activity.

**Disposition:** `PASS`.

---

## PRG-PT-584 — Participant alternates approved locales across days

**Scenario:** Participant reads Afrikaans one day and English the next within one active Enrolment.

**Expected invariants / analysis:** Locale is delivery context, not a parallel Programme lifecycle. No duplicate activities/progress solely because locale differs.

**Disposition:** `PASS`.

---

## PRG-PT-585 — Required paid lesson missing Afrikaans translation; English exists

**Scenario:** Afrikaans participant reaches required paid Nuwe Jy content with only English approved.

**Expected invariants / analysis:** Paid/core bilingual delivery cannot use sibling-locale availability as a silent waiver. Edition/activity readiness fails closed under Product translation rules; exact remedy stays Content/Product/OQ-024/OQ-016 governed.

**Disposition:** `PASS`.

---

## PRG-PT-586 — Optional low-risk public resource lacks selected translation

**Scenario:** Optional public editorial support link exists only in Afrikaans.

**Expected invariants / analysis:** Explicitly tell the participant the selected translation is unavailable and offer the available language. Never switch silently.

**Disposition:** `PASS`.

---

## PRG-PT-587 — Optional low-risk fallback occurs silently

**Scenario:** Missing English article automatically renders Afrikaans without notice.

**Expected invariants / analysis:** Reject. Product requires explicit fallback/choice even for allowed low-risk fallback.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-588 — Machine draft is displayed as a live Programme lesson

**Scenario:** Translation provider produced a fluent draft, so Programme delivers it before human approval.

**Expected invariants / analysis:** Reject. Machine output is draft-only and cannot become public/participant delivery merely because a Programme needs the locale.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-589 — Machine draft is visible only in governed editorial review

**Scenario:** Machine draft is created against an exact source version and remains inside staff review.

**Expected invariants / analysis:** Compatible with Product Law if labelled and routed through required language/clinical approvals before publication.

**Disposition:** `PASS`.

---

## PRG-PT-590 — Source changes while machine draft awaits review

**Scenario:** Source lesson changes materially after an English machine draft was generated.

**Expected invariants / analysis:** The draft is stale. It must not be approved/delivered as if bound to the new source without governed rework/review.

**Disposition:** `PASS`.

---

## PRG-PT-591 — Source changes after sibling translation approval but before release

**Scenario:** Afrikaans source gets a new version after English translation was approved for the prior source.

**Expected invariants / analysis:** Prior approval does not automatically attach to the new source version. Current readiness must reconcile exact source/translation provenance.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-592 — Locale versions have different version numbers

**Scenario:** Afrikaans is v7 while English is v5 because their review histories differ.

**Expected invariants / analysis:** Valid. Locale branches advance independently. Programme must not require cosmetic version-number equality; it needs approved compatibility/provenance.

**Disposition:** `PASS`.

---

## PRG-PT-593 — System requires translated text hashes to match

**Scenario:** A generic synchronisation rule declares translations invalid because locale text differs byte-for-byte.

**Expected invariants / analysis:** Reject. Translation equivalence is governed through source relationship and approval, not identical text/hash.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-594 — Language reviewer changes health meaning

**Scenario:** Translator alters a health instruction for readability and publishes after language review only.

**Expected invariants / analysis:** Reject. Language authority does not grant health/clinical approval. Risk-class approvals still apply.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-595 — Safety-critical translation has only language approval

**Scenario:** Safety warning is linguistically approved but lacks required clinical/safety approval.

**Expected invariants / analysis:** It is not delivery-ready. Required professional approval remains independent of language quality approval.

**Disposition:** `PASS`.

---

## PRG-PT-596 — Minor translation typo correction preserves Programme semantics

**Scenario:** Approved English wording has a spelling/punctuation correction that does not alter participant meaning or requirement.

**Expected invariants / analysis:** Content correction/versioning may proceed under Content rules without inventing a new ProgrammeVersion solely for the typo. Exact correction class/mechanics remain Content authority.

**Disposition:** `PASS`.

---

## PRG-PT-597 — Translation correction changes what participant must do

**Scenario:** Revised translation changes "read" into "submit" or alters the qualifying activity/evidence.

**Expected invariants / analysis:** This crosses Programme semantic authority. Content publication alone cannot silently change requirement/completion meaning; explicit Programme/Product review/version consequence is required.

**Disposition:** `PASS`.

---

## PRG-PT-598 — Safety withdrawal leaves stale locale content deliverable

**Scenario:** Content authority withdraws an unsafe translation but a Programme cache/reference still serves it.

**Expected invariants / analysis:** Reject stale delivery. Current Content withdrawal must be respected; exact invalidation/cache mechanics stay OQ-014/OQ-016/JIT.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-599 — One required paid locale is withdrawn while sibling locale remains approved

**Scenario:** English remains approved but Afrikaans is withdrawn during a paid edition.

**Expected invariants / analysis:** Do not silently continue as if bilingual readiness still holds. Product requires both languages for paid content; affected delivery/readiness must fail closed or use an explicitly approved correction path.

**Disposition:** `PASS`.

---

## PRG-PT-600 — Content correction occurs mid-Enrolment

**Scenario:** Participant has not yet reached a lesson when its approved translation is superseded by a correction.

**Expected invariants / analysis:** Future delivery uses the currently approved permissible version while the Enrolment remains on its ProgrammeVersion if Programme semantics are unchanged. Historical deliveries retain provenance.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-601 — Participant completed old approved translation before later correction

**Scenario:** A normal correction is published after the participant validly satisfied the activity.

**Expected invariants / analysis:** Do not reset completion automatically. Historical delivery/satisfaction remains truthful unless a governed correction proves the original basis invalid; post-award consequence then remains PRG-GAP-002.

**Disposition:** `PASS_WITH_EXISTING_GAP`.

---

## PRG-PT-602 — Participant resumes after translation correction

**Scenario:** Participant returns after a pause and the next lesson translation has been corrected.

**Expected invariants / analysis:** Serve the currently approved version for future delivery; preserve prior progress/history; do not create a restart or locale migration solely due to content correction.

**Disposition:** `PASS`.

---

## PRG-PT-603 — ProgrammeVersion references only "latest translation"

**Scenario:** Historical records know the ProgrammeVersion but cannot identify which ContentTranslationVersion was delivered.

**Expected invariants / analysis:** Reject for governed delivery where exact provenance matters. Current law requires exact content/locale provenance; exact reference representation stays OQ-013.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-604 — Programmes copies both locale bodies into its own record

**Scenario:** Programme snapshot duplicates Afrikaans/English lesson text to simplify rendering.

**Expected invariants / analysis:** Reject competing Content authority and correction/deletion complexity. Programmes should retain minimum immutable references/provenance, not become the content body owner.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-605 — Translation record owns activity requirement type

**Scenario:** English translation marks an activity optional while Afrikaans translation marks it required.

**Expected invariants / analysis:** Reject. Requirement type is ProgrammeVersion authority, not locale wording authority.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-606 — Translation wording reveals a Programme rule defect

**Scenario:** During translation, reviewers discover the source instruction conflicts with the Programme requirement.

**Expected invariants / analysis:** Stop at the owning authority. Fix Content and/or Programme through governed correction/versioning; do not let the translation team silently choose the Programme rule.

**Disposition:** `PASS`.

---

## PRG-PT-607 — Optional fallback is counted as required completion evidence

**Scenario:** Optional public article fallback is opened and Programmes marks a separate required activity complete.

**Expected invariants / analysis:** Reject unless the explicit ProgrammeVersion evidence rule says that exact optional resource is qualifying evidence. Fallback availability does not grant completion semantics.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-608 — Required content unavailable so activity is auto-completed

**Scenario:** Translation is missing/withdrawn and operator marks the activity complete to avoid blocking participants.

**Expected invariants / analysis:** Reject. PRG-GAP-011 remains the governed consequence seam; no automatic completion/waiver/substitution.

**Disposition:** `PASS_WITH_EXISTING_GAP`.

---

## PRG-PT-609 — Duplicate publication observations duplicate Programme release

**Scenario:** Same Content publication/invalidation signal is observed more than once.

**Expected invariants / analysis:** Programme/Edition consequences must be idempotent/reconcilable; duplicate observations cannot multiply release/progress effects.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-610 — Publication observations arrive out of order

**Scenario:** Older locale publication state arrives after a newer withdrawal/supersession.

**Expected invariants / analysis:** Do not regress by event arrival order. Re-read current Content authority before protected delivery/readiness decisions.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-611 — Source locale changes in a later Content version

**Scenario:** Editorial governance creates a legitimate new source version in the other language.

**Expected invariants / analysis:** Preserve historical source/translation lineage; do not rewrite earlier provenance to pretend the new source locale always existed.

**Disposition:** `PASS`.

---

## PRG-PT-612 — Translator removes source-version relationship

**Scenario:** Translation remains published but loses the exact source version it was reviewed against.

**Expected invariants / analysis:** Reject as governed provenance loss. Programme cannot safely treat it as current approved content.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-613 — Localised lesson title creates new Programme identity

**Scenario:** English and Afrikaans lesson titles differ, so system generates separate Programme/Lesson identities.

**Expected invariants / analysis:** Reject by default. Localised presentation labels belong to Content; Programme structure identity remains stable.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-614 — Locale-specific public slug becomes Programme activity identity

**Scenario:** Progress key is derived from `/af/...` or `/en/...` public URL slug.

**Expected invariants / analysis:** Reject. Locale/SEO URL is Content/public-delivery metadata, not durable Programme activity identity.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-615 — Reusable translated content block appears in several Programme lessons

**Scenario:** Same approved content block is referenced by multiple lessons.

**Expected invariants / analysis:** Content retains block/version/locale authority and exact lineage; Programmes retains its own structural references. Reuse does not duplicate content ownership.

**Disposition:** `PASS`.

---

## PRG-PT-616 — Reusable block correction affects several lessons

**Scenario:** Shared block is corrected/withdrawn after several Programme references exist.

**Expected invariants / analysis:** Content correction/withdrawal must propagate through governed current delivery without silently rewriting historical Programme evidence. Exact fan-out/revalidation mechanics remain OQ-016/JIT.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-617 — Localised protected download metadata is stale

**Scenario:** Programme points to an approved download whose selected-language metadata/asset version has been superseded.

**Expected invariants / analysis:** Protected delivery must use current approved Content/Media lineage; Programmes cannot bypass version/rights/publication state because the structural activity reference is still valid.

**Disposition:** `PASS`.

---

## PRG-PT-618 — Media translation inventory is assumed from text readiness

**Scenario:** Lesson text is bilingual, so edition readiness assumes linked videos/downloads/replay assets have complete translation/rights coverage.

**Expected invariants / analysis:** Reject. OQ-024 explicitly inventories lessons, videos, downloads, live-session assets, rights, missing translations and outdated content. Text readiness is not whole-asset readiness.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-619 — Nuwe Jy Edition activates with one required locale incomplete

**Scenario:** Core programme structure is ready but required Afrikaans content is incomplete.

**Expected invariants / analysis:** Edition activation fails the DEC-211/OQ-024 translation-readiness condition. Core composition may exist, but activation cannot claim ready.

**Disposition:** `PASS`.

---

## PRG-PT-620 — Missing translation is added after Edition activation should already have been blocked

**Scenario:** Team argues later completion retroactively proves the earlier activation was acceptable.

**Expected invariants / analysis:** Reject retroactive readiness. Later remediation supports future/re-entry state only; it cannot rewrite historical activation evidence.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-621 — Participant changes preferred language mid-Edition

**Scenario:** Participant changes saved preference from Afrikaans to English while staying in the same cohort.

**Expected invariants / analysis:** Future eligible delivery may select English under current approved content state; shared Edition schedule, ProgrammeVersion, Enrolment and progress remain unchanged.

**Disposition:** `PASS`.

---

## PRG-PT-622 — Language preference is used as completion truth

**Scenario:** Programme marks an activity incomplete because the participant consumed the other approved language instead of their saved preference.

**Expected invariants / analysis:** Reject unless Product explicitly requires a specific locale for that activity. Preference guides delivery; approved sibling-locale consumption does not inherently invalidate participation.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-623 — Browser locale silently overrides participant/content choice

**Scenario:** Request locale causes a different content translation to be served without explicit participant selection or governed fallback.

**Expected invariants / analysis:** Reject silent negotiation that obscures delivery provenance/choice. Interface/request locale may inform presentation but cannot bypass approved selection/fallback semantics.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-624 — Translation provider says "complete" and Programme treats that as approved

**Scenario:** External tool/vendor reports translation finished.

**Expected invariants / analysis:** Provider state is evidence only. Content-owned review/approval/publication lifecycle remains authoritative.

**Disposition:** `PASS_REJECTED_MODEL`.

---

## PRG-PT-625 — Content authority is unavailable during protected required delivery

**Scenario:** Programme cannot reliably determine whether the required locale/version is still approved/published.

**Expected invariants / analysis:** For protected/paid/safety-sensitive delivery, fail closed or use an explicitly bounded safe cached immutable authority path proven at JIT; never fall back to unapproved/stale content merely for availability.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

## PRG-PT-626 — Duplicate/reordered translation invalidations race with Programme release

**Scenario:** Publication, withdrawal and cache-refresh signals repeat or reorder around a scheduled release.

**Expected invariants / analysis:** Signals trigger re-evaluation; current Content authority decides deliverability. Programme release effects are idempotent and must not resurrect withdrawn content from stale order.

**Disposition:** `PASS_WITH_JIT_PROOF`.

---

# 122. Pass-15 gap adjudication

## `PRG-GAP-005` — semantic boundary remains resolved; implementation remains existing gates

Pass 15 confirms the existing adjudication rather than reopening it:

```text
Content & Media owns content/locale version + approval/publication/correction truth
        ↓
ProgrammeVersion owns structural/requirement meaning and references governed Content
        ↓
participant delivery records exact approved locale/version provenance where required
        ↓
Programme owns progress/satisfaction consequence, not translation lifecycle
```

Exact Content/Translation Resource relationships, indexes and immutable delivery references remain `OQ-013`. Publication retry, stale-approval checks, revalidation and correction/withdrawal fan-out remain `OQ-016`.

No new `PRG-GAP-012` is justified for translation binding.

## `PRG-GAP-011` — missing/withdrawn required translation can engage the existing gap

When a required Programme activity has no approved deliverable translation/replacement:

- Content owns unavailable/withdrawn truth;
- Programmes must not auto-complete, waive, substitute or recommend invalid content;
- a later approved replacement may satisfy the governed Programme policy;
- where no approved replacement exists, `PRG-GAP-011` remains open.

Pass 15 does not create a second "missing translation" gap for the same consequence.

## `PRG-GAP-002` — post-award correction remains separate

A later ordinary translation correction does not automatically invalidate historical completion/certification. If a governed correction proves the original award basis materially invalid, reconciliation reaches the existing `PRG-GAP-002` post-award consequence seam.

## `PRG-GAP-010` — locale does not redefine Programme identity

Language/localisation alone does not trigger the Product-semantic question of new Programme versus successor ProgrammeVersion. `PRG-GAP-010` remains reserved for a fundamental purpose/outcome/audience/risk redefinition, not ordinary bilingual content delivery.

## No new Product / Architecture / Domain gap promoted

Current Product, Domain and Roadmap authority already establishes:

- bilingual/risk-based publication rules;
- separate Content and Programme owners;
- source/translation/version lineage;
- Edition translation readiness;
- exact translation architecture as `OQ-013`;
- publication recovery as `OQ-016`; and
- Nuwe Jy content inventory as `OQ-024`.

No new Domain, Product amendment, Architecture amendment, Feature Pack, `PRG-GAP-###` or `PRG-UPD-###` is justified.

---

# 123. Pass-15 refinements to the working synthesis

## PRG-REF-161 — Source language is not globally fixed

Afrikaans and English can each be source locale; preserve exact source/version lineage rather than hard-coding a master language.

## PRG-REF-162 — Content & Media owns locale branches and translation lifecycle

Programmes references approved governed Content and does not duplicate wording, approval or publication authority.

## PRG-REF-163 — ProgrammeVersion is locale-neutral by default

A language variant is not a separate ProgrammeVersion unless Product deliberately creates different participant semantics.

## PRG-REF-164 — Interface language, preference and delivered content locale are distinct

Do not infer one from another when recording governed delivery/progress.

## PRG-REF-165 — Explicit language switching does not reset Programme progress

Approved sibling-locale consumption remains the same Programme activity unless Product explicitly says otherwise.

## PRG-REF-166 — Paid/core required content requires bilingual readiness

Missing one required approved locale is a readiness failure, not permission for silent sibling-locale or machine fallback.

## PRG-REF-167 — Optional low-risk fallback is explicit only

Tell the participant the selected translation is unavailable and offer the available language; never switch silently.

## PRG-REF-168 — Machine translation never becomes delivery authority

Provider completion/draft state remains evidence; Content review/approval/publication owns deliverability.

## PRG-REF-169 — Every translation binds to an exact source version

Source change stales dependent draft/review assumptions; current compatibility must be governed, not inferred from similar text.

## PRG-REF-170 — Language approval and risk approval remain independent

A translator cannot self-authorise health, clinical, safety or legal meaning merely by approving linguistic quality.

## PRG-REF-171 — Translation version and ProgrammeVersion advance independently

A content/locale correction does not automatically migrate Enrolment or create a new ProgrammeVersion.

## PRG-REF-172 — Content correction and Programme semantic change require different owner actions

If requirement/evidence/completion meaning changes, stop treating the change as translation-only and route it through Programme/Product authority.

## PRG-REF-173 — Cross-locale meaning must preserve shared Programme truth

Locale variants cannot independently redefine requirement type, safety truth, entitlement promise or completion outcome.

## PRG-REF-174 — Historical delivery retains exact content/locale provenance

Do not explain old participation from whatever translation is current today.

## PRG-REF-175 — Historical progress is not duplicated per locale

The same Programme activity/progress persists when the participant deliberately uses another approved language.

## PRG-REF-176 — Withdrawal constrains future delivery without fabricating Programme outcome

Missing/withdrawn required translation reaches `PRG-GAP-011` if no approved replacement exists; it is not auto-completed/waived/substituted/failed.

## PRG-REF-177 — Later correction does not silently rewrite historical awards

Ordinary corrections preserve valid history; material invalidation reaches explicit Programme reconciliation and `PRG-GAP-002` where post-award consequence remains unresolved.

## PRG-REF-178 — Edition activation consumes Content translation readiness

Programmes validates readiness from Content authority but does not own or duplicate Content publication state.

## PRG-REF-179 — Duplicate/reordered publication signals reconcile from current Content authority

Events/jobs/invalidations are triggers, not current truth; exact idempotency mechanics remain JIT proof.

## PRG-REF-180 — Locale presentation identifiers never become Programme identity

Titles, slugs, URLs and translation IDs are not durable Programme/Activity identity keys.

## PRG-REF-181 — OQ-013 remains the exact implementation boundary

Do not preselect a JSON blob, generic translation table, per-locale Programme graph or custom localisation service in this Pre-JIT pass.

## PRG-REF-182 — No new translation Domain or Feature Pack is justified

The current Content & Media + Programmes composition already owns the required durable truths; localisation remains a cross-domain delivery seam.

---

# 124. Pass-15 anti-localisation-engine / YAGNI outcome

Pass 15 explicitly rejects:

- hard-coding English as the universal source language;
- hard-coding Afrikaans as the universal source language;
- separate Programme identities solely for language;
- separate ProgrammeVersions solely for language;
- separate Enrolments/progress histories solely for language;
- locale-specific completion rules by default;
- using a locale slug/URL as durable Programme or Activity identity;
- copying Afrikaans/English content bodies into Programmes;
- one giant Programme-owned translation JSON blob;
- a generic translation microservice merely because two languages exist;
- a generic LMS localisation layer detached from Content authority;
- silent sibling-language fallback;
- unapproved machine fallback;
- translation-provider completion as publication authority;
- language-review authority as clinical/safety approval authority;
- automatic ProgrammeVersion migration for every content typo/correction;
- hiding Programme requirement changes inside translation edits;
- treating same translation version number across locales as a correctness requirement;
- byte/hash equality across languages as translation equivalence;
- browser locale as implicit participant consent to a different content language;
- duplicated per-locale day/release schedules for Nuwe Jy;
- auto-completing required activities because a translation is unavailable;
- retaining stale withdrawn translations for availability;
- treating text translation readiness as proof that all media/download assets are ready;
- a new Translation Domain; and
- a new Translation Feature Pack.

The simplest correct model remains Content-owned immutable locale/version lineage consumed by a shared ProgrammeVersion/Edition, with explicit risk-based readiness and exact delivery provenance where required.

---

# 125. Pass-15 disposition

**Outcome: PASS WITH NON-BLOCKING REFINEMENTS.**

Candidate `WORKING_LOCKED / NON-AUTHORITATIVE` conclusions pending user acceptance:

1. Passes 1–14 remain accepted/working-locked and Pass 15 does not reopen them.
2. Content & Media owns conceptual content, immutable body versions, locale branches/translations, approvals, publication, corrections and withdrawals; Programmes owns structural/requirement/completion meaning and references Content.
3. Afrikaans and English are symmetric source-language possibilities; no universal master language is authorised.
4. ProgrammeVersion, ContentVersion, ContentTranslationVersion and participant delivery/progress provenance are separate version dimensions.
5. ProgrammeVersion is locale-neutral by default; translation/localisation alone does not justify a separate ProgrammeVersion, Programme or Enrolment.
6. Interface language, saved preference, selected content language and exact delivered locale/version are distinct and must not be silently collapsed.
7. Explicit participant language switching between approved sibling variants does not reset or duplicate Programme progress.
8. Paid/core/safety-sensitive required content fails readiness when required approved translations are unavailable; sibling-locale or machine fallback is not silently substituted.
9. Optional low-risk public fallback is permitted only when explicitly disclosed/offered under Product rules.
10. Machine translations are drafts only; provider completion never becomes Content publication or Programme delivery authority.
11. Every translation remains bound to exact source-version provenance and becomes stale/review-sensitive when its source changes.
12. Locale branches may advance at different version numbers/times; equality of version numbers/text hashes is not a correctness invariant.
13. Language review and health/clinical/safety/legal approval remain separate scoped authorities.
14. Translation wording cannot independently change Programme requirement type, qualifying evidence, completion rule, safety truth or entitlement promise.
15. Content corrections and Programme semantic/version changes are separate owner decisions; material requirement changes cannot be disguised as localisation edits.
16. Active Enrolment need not migrate merely because a ContentTranslationVersion advances when Programme semantics remain unchanged.
17. Governed delivery/history must retain exact content/locale provenance where required rather than resolving historical participation against today's translation.
18. Later ordinary translation corrections do not automatically erase historical progress/completion; material invalidation reaches explicit reconciliation and existing `PRG-GAP-002` where post-award consequence remains open.
19. Missing/withdrawn required translation does not fabricate complete/exempt/substitute/fail outcomes; `PRG-GAP-011` remains the consequence seam where no approved replacement exists.
20. `PRG-GAP-005` remains semantically resolved; exact immutable-reference/resource/index mechanics stay `OQ-013` and publication/revalidation/recovery mechanics stay `OQ-016`.
21. Nuwe Jy Edition activation consumes translation readiness from Content authority under `DEC-211`/`OQ-024` rather than duplicating Content lifecycle inside Programmes.
22. Translation readiness for text does not prove linked video/download/media readiness; `OQ-024` inventory remains broader than lesson text.
23. Duplicate/reordered publication/withdrawal signals trigger reconciliation from current Content authority and cannot resurrect stale content by arrival order.
24. Locale-specific titles/slugs/URLs/presentation remain Content metadata and do not become Programme identity.
25. FP-014 can reuse the same shared Programme/Content translation seam established through FP-008 proof; it does not require a generic LMS/localisation engine.
26. `OQ-013`, `OQ-016`, `OQ-019`, `OQ-024`, `OQ-025` and applicable `OQ-014` remain the correct existing gates for this seam; this is not a claim that they are the complete gate set for FP-008 or FP-014.
27. No new Product, Architecture or Domain amendment is justified by this pass.
28. No new `PRG-GAP` or `PRG-UPD` is justified by this pass.
29. A generic translation Domain, translation Feature Pack, locale-specific Programme graph or Programme-owned translation store remains `DEFER_YAGNI` / rejected.
30. The exact Ash translation-resource representation remains intentionally deferred to `OQ-013` and later JIT/architecture work.

**Pass hard stop:** Pass 16 — communications orchestration / delivery-consequence semantics — has not started. Do not pull channel/provider/template retry/deduplication/quiet-hours/notification-failure detail into this Pass-15 candidate beyond the existing owner boundary.

**Broad discovery remains unfrozen.** Later operator correction, concurrency/retry, cancellation/transfer, historical reproducibility, analytics, FP-014 second-lens and final adversarial-convergence passes remain separate.
