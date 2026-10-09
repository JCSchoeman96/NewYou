# NewYou Assessment / Temperament Pre-JIT Discovery — Working v0.13.0

> **WORKING / NON-AUTHORITATIVE PRE-JIT DISCOVERY — APPEND-ONLY SEMVER SUCCESSOR**
>
> This successor does not rewrite `v0.1.0` through `v0.12.0`. Read those predecessors first for the accepted attempt, entitlement, expiry, subscription, recovery, submission, concurrency, notification, replacement/retake, execution-provenance, result-correction, profile-source, reassessment, report-lifecycle and identity-reconciliation semantics. This file appends the accepted privacy / retention / deletion / legal-hold lifecycle contract and pressure tests.
>
> Nothing in this file creates Product Law, Architecture Law, Domain Law, Roadmap authority, JIT authority, proof classification or implementation authorisation.

- **Document version:** `v0.13.0`
- **Predecessor:** `NEWYOU_ASSESSMENT_TEMPERAMENT_PREJIT_DISCOVERY_WORKING_v0.12.0.md`
- **Predecessor blob SHA:** `f855bf382c097ae223f4e71146c3bb55007f50cc`
- **Date:** `2026-10-08`
- **Canonical repository:** `JCSchoeman96/NewYou`
- **Authority pin inherited for this pass:** `a9c9a8d176e8d62044ca069efeefa60b8f666c8d`
- **Working branch:** `docs/assessment-temperament-prejit-working`
- **Discovery status:** `IN PROGRESS`
- **Implementation authorisation:** `NONE`
- **Final Pre-JIT disposition:** `NOT YET ELIGIBLE FOR PARK`

---

# 1. Successor delta

## AT-WD-017 — Privacy lifecycle supremacy over retained assessment evidence

**Accepted:** `2026-10-08`

Assessment attempts, submitted answers, results, declaration/current-profile history and report snapshots are immutable while retained, but immutability does not create perpetual retention. Privacy & Consent authority governs whether retained assessment data remains active, becomes restricted/archived, is retained by obligation, is placed under legal hold, is deleted, or is irreversibly anonymised according to the applicable category-specific lifecycle.

### AT-WD-017A — Immutability means no historical rewrite while retained, not undeletability

A retained submitted answer/result/report may not be silently edited merely because later preferences, methodology, wording or product state changed.

Where governing Privacy & Consent authority later requires deletion or irreversible anonymisation, Temperament must apply that disposition. Deleting or irreversibly anonymising retained immutable evidence is not the same as rewriting the historical fact while it existed.

Temperament must not create an assessment-specific perpetual-retention exception merely from DEC-070 reproducibility semantics.

### AT-WD-017B — Account closure is distinct from irreversible deletion

Recoverable account closure does not itself delete, rewrite or reset retained assessment history, retake timing, entitlement consumption, result provenance or report lineage.

Where the account is lawfully recovered/reopened while the underlying assessment history remains retained, the same retained history remains authoritative.

Irreversible full deletion is a different Privacy lifecycle and may remove or irreversibly anonymise eligible Temperament data according to governing retention law.

### AT-WD-017C — Permanent report access does not override authoritative deletion

`AT-WD-015E` permanent report access means no ordinary commercial/subscription expiry of an earned report while the report remains lawfully retained.

It does not create a right to preserve identifiable report/result data against an authoritative deletion/anonymisation obligation.

If report/result data is lawfully deleted, a hidden copy may not be preserved merely to satisfy the commercial word "permanent". Retained-by-obligation material may likewise be isolated from ordinary participant-facing product use where governing Privacy authority requires it.

### AT-WD-017D — Legal hold and retained-by-obligation scope narrowly

A legal/professional/fraud/dispute or other governed hold pauses only the deletion it validly governs. It must not silently freeze the participant's entire Temperament history or broader account data where the hold scope is narrower.

Held/retained-by-obligation Temperament data must be minimised and isolated from ordinary personalisation/product use unless separate authority permits use.

When the hold/retention obligation ends, the pending applicable deletion lifecycle resumes rather than silently converting the hold into permanent product retention.

### AT-WD-017E — Pseudonymisation is not automatically irreversible anonymisation

Replacing a participant identifier with a random/pseudonymous key does not by itself satisfy deletion/anonymisation where the retained answer/result/report combination remains reasonably linkable or reconstructive under governing Privacy standards.

Temperament must not classify participant-level exact answers, scores, timestamps or rare result combinations as anonymous merely because the direct account id has been replaced.

### AT-WD-017F — Irreversibly anonymous aggregates may survive where permitted

Privacy-controlled assessment analytics may retain genuinely irreversible anonymous aggregates where governing Product/Privacy authority permits them.

Identifiable or re-linkable participant-level analytics rows, projections or derivative data must follow the applicable deletion/anonymisation disposition and may not become a hidden backup of Temperament authority.

### AT-WD-017G — Deletion spans authoritative and derivative identifiable representations

A Temperament deletion/anonymisation obligation is not complete merely because one PostgreSQL source row is hidden or removed.

Applicable identifiable representations include, where present and in scope:

- authoritative attempts/answers/results/profile-selection state;
- generated report objects/snapshots;
- search/read-model projections;
- caches;
- participant-level analytics/derived projections;
- exports/derivative files under platform control;
- relevant external-processor copies; and
- any other reconstructive identifiable representation governed by the deletion contract.

Exact processor/storage mechanics remain JIT/Privacy work, but Temperament may not treat derivative copies as outside the deletion obligation merely because they are not business authority.

### AT-WD-017H — Irreversible deletion becomes a write/finalisation guard

Once irreversible deletion execution becomes authoritative for the participant/data in scope, stale browser writes, autosaves, final-submit requests, scoring jobs, report-generation work, identity-reconciliation replay or technical-recovery work may not recreate the deleted Temperament data.

If a final submission became authoritative before the irreversible-deletion boundary, the resulting retained history follows the applicable deletion lifecycle. If irreversible deletion authority wins the race first, the late mutation/finalisation must fail closed.

Exact transaction/reconciliation mechanics are deferred to JIT Architecture work.

### AT-WD-017I — Technical recovery does not defeat participant deletion

A pending technical-recovery obligation or replacement right does not authorise Temperament to retain/reconstruct answers/results after authoritative irreversible deletion.

Commercial/refund/entitlement consequences may remain for their owning Domains, but Temperament personal data follows Privacy authority and may not be resurrected to satisfy a future recovery path.

### AT-WD-017J — Deleted current-profile source does not cause silent fallback

Where the effective current-profile source is deleted or irreversibly anonymised such that it is no longer an eligible participant-specific source, the platform must not silently select another declared/digital profile.

Any remaining eligible source requires explicit participant selection under `AT-WD-013` where a participant-facing account still lawfully exists.

### AT-WD-017K — Minimal non-reconstructive suppression evidence may survive only under governing authority

Where lawful and necessary to prove deletion, prevent backup/restore resurrection or suppress replay, a minimal non-reconstructive deletion/suppression marker may survive.

Such evidence must not preserve enough participant Temperament data to reconstruct the deleted assessment history or quietly continue product personalisation/report access.

---

# 2. Retention-gate position

No new retention duration or category schedule is invented in this pass.

Current `OQ-009` / `OQ-029` remain the governing open retention-matrix dependencies. FP-003/JIT must consume their resolved category-specific dispositions rather than treating this working document as retention authority.

The semantic contract frozen here is limited to the interaction between Temperament immutability/reproducibility and the existing platform Privacy lifecycle.

---

# 3. Pressure-test additions — v0.13.0

## AT-PT-124 — Recoverable account closure only

**Scenario:** participant closes the account under a recoverable account-closure lifecycle; no irreversible deletion is yet authoritative.

**Expected:** retained assessment history is not silently deleted, rewritten or reset merely because ordinary account access is closed. If lawful recovery occurs while data remains retained, the same history remains.

**Result:** `PASS` under AT-WD-017B.

## AT-PT-125 — Full deletion reaches eligible submitted answers/results

**Scenario:** governing Privacy authority determines submitted answers, result and report are eligible for irreversible deletion/anonymisation.

**Expected:** DEC-070 immutability does not create a perpetual-retention exception. Eligible identifiable data is deleted or irreversibly anonymised according to the governed lifecycle rather than edited in place or retained forever.

**Result:** `PASS` under AT-WD-017A/C.

## AT-PT-126 — Earned permanent report versus full deletion

**Scenario:** participant earned permanent report access but later completes an authoritative full-deletion lifecycle covering that report/result.

**Expected:** ordinary subscription/commercial expiry remains irrelevant, but deletion authority prevails. No hidden identifiable report copy is preserved merely to maintain the access promise.

**Result:** `PASS` under AT-WD-017C.

## AT-PT-127 — Narrow legal hold during broader deletion

**Scenario:** a dispute hold lawfully covers one assessment transaction while other participant Temperament data is deletion-eligible.

**Expected:** only scoped held material is retained; unrelated deletion proceeds. Held material is minimised/isolated and does not automatically remain active current-profile or personalisation authority.

**Result:** `PASS` under AT-WD-017D.

## AT-PT-128 — Random identifier with reconstructive exact answer set

**Scenario:** account id is removed but complete answers, exact scores and timestamps remain under a random identifier that can still reasonably be linked/reconstructed.

**Expected:** do not claim irreversible anonymisation merely because the direct identifier was replaced.

**Result:** `PASS` under AT-WD-017E.

## AT-PT-129 — Genuine irreversible aggregate survives

**Scenario:** participant-level identifiable assessment history is deleted, while a genuinely irreversible aggregate statistic remains under governing privacy policy.

**Expected:** aggregate may remain where permitted; it cannot be used to recreate participant-specific Temperament truth.

**Result:** `PASS` under AT-WD-017F.

## AT-PT-130 — Cached/search/report derivative survives source-row deletion

**Scenario:** authoritative result row is deleted but an identifiable report object, cache or search/read projection remains usable.

**Expected:** deletion is incomplete; applicable derivative representations must follow the deletion/anonymisation lifecycle.

**Result:** `PASS` under AT-WD-017G.

## AT-PT-131 — Stale browser submits after irreversible deletion boundary

**Scenario:** browser retains an old active assessment state and submits after irreversible deletion execution has become authoritative.

**Expected:** fail closed. No new answer/submission/result is recreated from stale client state.

**Result:** `PASS` under AT-WD-017H.

## AT-PT-132 — Report/scoring worker runs after deletion

**Scenario:** queued deterministic scoring or report generation wakes after irreversible deletion authority already governs the relevant data.

**Expected:** job must reconcile current Privacy state and may not regenerate deleted assessment/report state.

**Result:** `PASS` under AT-WD-017H.

## AT-PT-133 — Backup/restore reintroduces deleted assessment material

**Scenario:** a restore reintroduces stale deleted Temperament data.

**Expected:** governing deletion/suppression/reconciliation truth prevents the restored data from regaining participant-visible/business authority and removes/re-anonymises it as required.

**Result:** `PASS` under AT-WD-017G/K.

## AT-PT-134 — Technical recovery exists when participant completes deletion

**Scenario:** genuine technical-recovery right exists, but participant completes authoritative full deletion before using it.

**Expected:** Temperament answers/results are not retained or reconstructed solely to honour recovery. Owning commercial Domains handle any remaining remedy without data resurrection.

**Result:** `PASS` under AT-WD-017I.

## AT-PT-135 — Current-profile source deleted

**Scenario:** participant's selected current digital result is deleted under governing Privacy authority while another eligible retained profile source exists.

**Expected:** no automatic fallback to the other source. Current-profile state requires explicit participant choice if/when participant-facing operation remains lawful.

**Result:** `PASS` under AT-WD-017J + AT-WD-013.

---

# 4. Open-question queue after v0.13.0

The Privacy/retention/deletion/legal-hold interaction is now materially constrained by `AT-WD-017` and `AT-PT-124...135`, while exact category durations/dispositions remain gated by existing `OQ-009`/`OQ-029` authority.

Next unresolved cluster:

- **Research & Feedback / Interactive Tools isolation:** prevent research responses, optional feedback, quizzes/calculators or anonymous/public interactive outputs from silently becoming Temperament assessment authority, current-profile truth, digital score provenance or entitlement consumption. Define the narrow explicit path, if any, by which separately governed participant input may intentionally create/update a declared profile or preference.

Later passes still include Methodology Authority Input Contract and the final adversarial sweep.
