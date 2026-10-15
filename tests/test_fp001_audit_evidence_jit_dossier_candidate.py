import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
BASELINE = "5f5a994e48d9458aaa6397044b3af4d72c5d5e81"
CANDIDATE_RELATIVE = (
    "docs/00_platform/working/"
    "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
)
CANDIDATE_PATH = ROOT / CANDIDATE_RELATIVE
AUDIT_STATUS = "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"

PROTECTED_PATHS = (
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
    "docs/00_platform/00_PLATFORM_v1.8.0.md",
    "docs/00_platform/01_DECISIONS_v1.8.0.md",
    "docs/00_platform/03_ARCHITECTURE_v1.1.1.md",
    "docs/00_platform/04_DOMAIN_MAP_v1.2.0.md",
    "docs/00_platform/05_ROADMAP_v1.2.2.md",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md",
    "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
    "docs/00_platform/README.md",
    "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json",
    "docs/00_platform/02_OPEN_WORK_v1.2.63.md",
    "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.7.md",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
    "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
)


def _git_show(path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{BASELINE}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def _section(text: str, start: str, end: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index + len(start))
    return text[start_index:end_index]


def _first_table(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    started = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            started = True
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            rows.append(cells)
        elif started:
            break
    return rows


def _row_containing(rows: list[list[str]], needle: str) -> list[str]:
    matches = [row for row in rows[1:] if needle.casefold() in row[0].casefold()]
    if len(matches) != 1:
        raise AssertionError(f"expected one table row containing {needle!r}, found {len(matches)}")
    return matches[0]


class Fp001AuditEvidenceJitDossierCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.candidate = (
            CANDIDATE_PATH.read_text(encoding="utf-8") if CANDIDATE_PATH.exists() else ""
        )
        cls.manifest_path = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        cls.manifest = json.loads(cls.manifest_path.read_text(encoding="utf-8"))
        cls.readme = (DOCS / "README.md").read_text(encoding="utf-8")
        cls.open_work = (DOCS / "02_OPEN_WORK_v1.2.63.md").read_text(encoding="utf-8")
        state_match = re.search(
            r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
            cls.open_work,
            re.DOTALL,
        )
        cls.lifecycle_state = json.loads(state_match.group(1)) if state_match else {}
        cls.skeleton = (
            DOCS / "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.7.md"
        ).read_text(encoding="utf-8")
        cls.domain_map = (DOCS / "04_DOMAIN_MAP_v1.2.0.md").read_text(encoding="utf-8")
        cls.roadmap = (DOCS / "05_ROADMAP_v1.2.2.md").read_text(encoding="utf-8")

    def test_candidate_is_present_at_the_review_path(self):
        self.assertTrue(CANDIDATE_PATH.is_file(), CANDIDATE_RELATIVE)
        self.assertIn("PROPOSED VERSION: v0.1.0", self.candidate)

    def test_candidate_lifecycle_does_not_claim_currentness_or_execution_authority(self):
        for marker in (
            f"PROPOSED PATH: {CANDIDATE_RELATIVE}",
            "PROPOSED VERSION: v0.1.0",
            "STATUS: CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT",
            "NON-EXECUTABLE",
            "NOT PHASE 7C DEVELOPMENT-ENTRY AUTHORITY",
            "DOES NOT AMEND PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW",
        ):
            self.assertIn(marker, self.candidate)

        manifest_text = json.dumps(self.manifest)
        for current_route in (manifest_text, self.readme, self.open_work, self.skeleton):
            self.assertNotIn(CANDIDATE_RELATIVE, current_route)

    def test_current_governance_status_and_downstream_stops_remain_unchanged(self):
        self.assertEqual(AUDIT_STATUS, self.lifecycle_state.get("audit_dossier"))
        self.assertEqual(AUDIT_STATUS, self.lifecycle_state.get("conditional_dossiers", {}).get("audit_evidence"))
        self.assertIn("IDENTITY & ACCESS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4", self.open_work)
        self.assertIn("COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0", self.open_work)
        self.assertIn("PHASE 7C: BLOCKED / NOT_STARTED", self.open_work)
        self.assertIn("PROOF CLASSIFICATION: NOT FINALISED", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: UNAUTHORISED", self.open_work)
        self.assertIn("phase 7c remains `blocked / not_started`", self.skeleton.casefold())
        self.assertIn("does not authorise or perform Phase 7B, Phase 7C", self.skeleton)

    def test_governing_and_current_fp001_sources_match_the_verified_baseline(self):
        for path in PROTECTED_PATHS:
            with self.subTest(path=path):
                self.assertEqual(_git_show(path), (ROOT / path).read_bytes(), path)

    def test_fp001_scope_keeps_six_domains_seven_capabilities_and_seventeen_packs(self):
        participation = _section(
            self.skeleton,
            "## 7. Domain participation",
            "## 8. Phase 7B dossier discovery",
        )
        domain_rows = [
            line for line in participation.splitlines() if line.startswith("| ") and " | `" in line
        ]
        self.assertEqual(6, len(domain_rows))
        for domain in (
            "Identity & Access",
            "Privacy & Consent",
            "Content & Media",
            "Communications",
            "Audit & Evidence",
            "Analytics",
        ):
            self.assertEqual(1, sum(domain in row for row in domain_rows))

        capabilities = _section(
            self.skeleton,
            "## 6. Material capability input",
            "## 7. Domain participation",
        )
        capability_ids = {
            match.group(1)
            for line in capabilities.splitlines()
            if line.startswith("| `CAP-")
            for match in [re.match(r"\| `(CAP-\d{3})` \|", line)]
            if match is not None
        }
        self.assertEqual(
            {"CAP-001", "CAP-002", "CAP-003", "CAP-005", "CAP-006", "CAP-017", "CAP-028"},
            capability_ids,
        )
        self.assertEqual(17, len(re.findall(r"(?m)^## FP-\d{3} —", self.roadmap)))

    def test_authority_delta_revalidation_separates_law_jit_and_downstream_items(self):
        review = _section(
            self.candidate,
            "## 3. Authority and delta revalidation",
            "## 4. Audit ownership contract",
        )
        for path in (
            "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
            "00_PLATFORM_v1.8.0.md",
            "01_DECISIONS_v1.8.0.md",
            "03_ARCHITECTURE_v1.1.1.md",
            "04_DOMAIN_MAP_v1.2.0.md",
            "05_ROADMAP_v1.2.2.md",
            "PLATFORM_OPERATING_MODEL_v1.0.1.md",
            "FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
            "02_OPEN_WORK_v1.2.63.md",
            "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.7.md",
            "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
            "FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        ):
            self.assertIn(path, review)

        for classification in (
            "DIRECT_AUTHORITY",
            "FP-001 JIT SEMANTIC DECISION",
            "IMPLEMENTATION_PROOF",
            "EXPERT_LEGAL_PRIVACY",
            "LATER FEATURE PACK",
            "STOP / ESCALATION",
        ):
            self.assertIn(classification, review)
        self.assertIn("no unresolved Audit-specific Product or Architecture amendment prerequisite", review)
        self.assertIn("AE-WD-* identifiers remain working discovery identifiers", review)

    def test_event_selection_precedes_criticality_and_keeps_routine_activity_out(self):
        selection = _section(
            self.candidate,
            "## 5. FP-001 event/evidence selection matrix",
            "## 6. Evidence acceptance contract",
        )
        rows = _first_table(selection)
        self.assertGreaterEqual(len(rows), 30)
        self.assertEqual(
            [
                "FP-001 event / source action",
                "Source owner",
                "Central Audit selection",
                "Criticality after selection",
                "Truth, duplicate and failure boundary",
            ],
            rows[0],
        )
        self.assertLess(selection.index("Central Audit selection"), selection.index("Criticality after selection"))
        self.assertIn("Selection happens before E1/E2/E3 classification", selection)

        expected = {
            "successful Account creation": ("YES", "E2"),
            "email verification proof successfully consumed": ("YES", "E2"),
            "ordinary sign-in success": ("NO", "E3"),
            "ordinary failed password attempt": ("NO", "E3"),
            "manual/exception recovery": ("YES", "E1"),
            "security hold placement": ("YES", "E2"),
            "security hold release": ("YES", "E1"),
            "privileged/manual MFA reset": ("YES", "E1"),
            "grant activation": ("YES", "E1"),
            "grant revocation or expiry": ("YES", "E2"),
            "break-glass activation": ("YES", "E1"),
            "ordinary verification/recovery delivery attempt": ("NO", "E3"),
            "provider accepted/delivered/failed callback": ("NO", "E3"),
            "bulk/high-sensitivity Audit query/export": ("YES", "E1"),
        }
        for event, (chosen, criticality) in expected.items():
            with self.subTest(event=event):
                row = _row_containing(rows, event)
                self.assertIn(chosen, row[2])
                self.assertIn(criticality, row[3])

    def test_e1_e2_and_e3_acceptance_contracts_remain_distinct(self):
        acceptance = _section(
            self.candidate,
            "## 6. Evidence acceptance contract",
            "## 7. Evidence identity, correlation and idempotency",
        )
        for invariant in (
            "E1",
            "before the protected effect",
            "admission/attempt",
            "does not claim completion",
            "linked outcome",
            "protected e1 effect fails closed",
            "E2",
            "same acceptance boundary",
            "lossless, replay-safe/idempotent obligation",
            "does not rewrite, delay or invalidate source truth",
            "E3",
            "central Audit is not required for correctness",
            "governed telemetry",
        ):
            self.assertIn(invariant.casefold(), acceptance.casefold())

    def test_evidence_identity_and_retry_rules_do_not_collapse_distinct_attempts(self):
        identity = _section(
            self.candidate,
            "## 7. Evidence identity, correlation and idempotency",
            "## 8. Minimum accountability envelope",
        )
        for invariant in (
            "Business-operation idempotency and evidence-materialisation idempotency are separate",
            "same evidence assertion/materialisation obligation",
            "genuinely distinct governed attempts remain distinct",
            "actor + target + action + similar timestamp is insufficient",
            "correlation is a relationship, not source concurrency authority",
            "arrival order does not redefine source truth",
            "Audit never repairs source-domain atomicity or concurrency",
        ):
            self.assertIn(invariant.casefold(), identity.casefold())

    def test_accountability_envelope_and_corrections_are_minimised_and_append_only(self):
        envelope = _section(
            self.candidate,
            "## 8. Minimum accountability envelope",
            "## 9. Correction, retraction and supersession",
        )
        for category in (
            "evidence identity and relationships",
            "restricted actor",
            "restricted target",
            "event/admission/outcome time",
            "purpose/scope/authority reference",
            "bounded reason",
            "safe result/outcome class",
            "causal/source-operation/correlation reference",
            "limited semantic change summary",
        ):
            self.assertIn(category.casefold(), envelope.casefold())
        for prohibited in (
            "credentials or bearer secrets",
            "full communication bodies",
            "raw provider payloads",
            "payment credentials",
            "full health/private source payloads",
            "generic before/after JSON",
            "diagnostic logs or stack traces",
        ):
            self.assertIn(prohibited.casefold(), envelope.casefold())
        self.assertIn("not a source snapshot", envelope.casefold())

        correction = _section(
            self.candidate,
            "## 9. Correction, retraction and supersession",
            "## 10. Privileged Audit access",
        )
        for invariant in (
            "append-only",
            "new linked evidence",
            "preserves the original historical assertion",
            "never silently overwrite",
            "Audit cannot correct source business truth",
            "compensation or reversal is a separate truthful business event",
            "correction/supersession is itself a high-risk privileged operation",
        ):
            self.assertIn(invariant.casefold(), correction.casefold())

    def test_audit_access_is_separately_scoped_and_stops_recursion(self):
        access = _section(
            self.candidate,
            "## 10. Privileged Audit access",
            "## 11. Retention, hold and disposition",
        )
        for capability in (
            "narrow read/lookup",
            "high-sensitivity lookup",
            "bulk query",
            "export",
            "correction/supersession",
            "retention/hold administration",
            "exceptional infrastructure access",
        ):
            self.assertIn(capability.casefold(), access.casefold())
        self.assertIn("support permission does not imply audit-reader authority", access.casefold())
        self.assertIn("bulk/cross-participant/high-sensitivity/export", access.casefold())
        self.assertIn("deliberate final trusted operational boundary", access.casefold())
        self.assertIn("normal internal evidence append does not recursively audit itself", access.casefold())

    def test_retention_and_source_deletion_keep_owner_separation(self):
        retention = _section(
            self.candidate,
            "## 11. Retention, hold and disposition",
            "## 12. Source deletion and non-resolvable references",
        )
        for invariant in (
            "Audit owns its evidence truth and evidence-retention-category metadata",
            "Privacy & Consent owns retention-policy assignment/version",
            "data-owning Domains own their own data contracts",
            "historical semantic meaning",
            "correction/supersession lineage",
            "evidence access state",
            "retention classification/basis",
            "hold/disposition state",
            "Immutability does not mean immortality",
            "exact lawful periods remain unresolved",
            "EXPERT_LEGAL_PRIVACY",
        ):
            self.assertIn(invariant.casefold(), retention.casefold())
        self.assertIsNone(re.search(r"\b\d+\s*(?:day|days|month|months|year|years)\b", retention, re.I))

        deletion = _section(
            self.candidate,
            "## 12. Source deletion and non-resolvable references",
            "## 13. Restore, recovery and integrity semantics",
        )
        self.assertIn("may become non-resolvable", deletion.casefold())
        for prohibition in (
            "must not authenticate",
            "must not reactivate an Account",
            "must not restore product authority",
            "must not reconstruct a deleted participant profile",
            "must not become a general participant directory",
        ):
            self.assertIn(prohibition.casefold(), deletion.casefold())

    def test_restore_semantics_preserve_source_truth_and_recovery_provenance(self):
        restore = _section(
            self.candidate,
            "## 13. Restore, recovery and integrity semantics",
            "## 14. Identity and Communications seams",
        )
        for invariant in (
            "Audit behind source is an integrity/reconciliation gap",
            "does not invalidate or rewrite source truth",
            "recovered evidence discloses recovery provenance",
            "Audit ahead of source cannot authorise replay of business mutations",
            "source owner reconciles its own business truth",
            "current required E1 capture integrity cannot be trusted",
            "selected e1 protected effects fail closed",
            "bounded historical gap",
            "does not permanently disable unrelated future E1",
            "lawful disposition and unauthorised tampering must remain distinguishable",
        ):
            self.assertIn(invariant.casefold(), restore.casefold())

    def test_identity_and_communications_seams_keep_source_ownership(self):
        seams = _section(
            self.candidate,
            "## 14. Identity and Communications seams",
            "## 15. Semantic pressure cases",
        )
        self.assertIn("Identity & Access remains the sole source of Account, PMR, proof, recovery, grant and security truth", seams)
        self.assertIn("Communications owns routine delivery attempts, retries and provider observations", seams)
        self.assertIn("no duplicate raw central delivery ledger", seams)
        self.assertIn("provider state is evidence, never source authority", seams.casefold())
        self.assertIn("communication ambiguity cannot establish identity success", seams.casefold())

    def test_pressure_case_matrix_covers_all_required_cases_and_dimensions(self):
        pressure = _section(
            self.candidate,
            "## 15. Semantic pressure cases",
            "## 16. Unresolved items and replaceable mechanisms",
        )
        rows = _first_table(pressure)
        self.assertEqual(
            [
                "#",
                "Pressure case",
                "Authoritative source owner",
                "Central selection / criticality",
                "Truthful evidence claim",
                "Duplicate/retry behaviour",
                "Failure/reconciliation outcome",
            ],
            rows[0],
        )
        cases = [row[1] for row in rows[1:]]
        self.assertEqual([f"{number:02d}" for number in range(1, 23)], [row[0] for row in rows[1:]])
        self.assertEqual(22, len(cases))
        self.assertEqual(len(cases), len(set(cases)))
        self.assertTrue(all(len(row) == 7 and all(cell for cell in row) for row in rows[1:]))

        required = (
            "same evidence-materialisation obligation replayed twice",
            "two genuinely distinct privileged attempts with near-identical actor/target/time",
            "business operation is idempotently suppressed but second human attempt is evidence-worthy",
            "E1 admission succeeds and the source protected action later fails",
            "required E1 durable admission cannot be established",
            "E2 source transition commits while central materialisation is delayed",
            "delayed E2 materialisation retries after recovery/restart",
            "security revocation/restriction during central Audit outage",
            "privileged grant/restoration during central Audit outage",
            "source owner later corrects business truth",
            "evidence correction/supersession attempt itself",
            "source record later lawfully disappears",
            "correction chain reaches lawful disposition",
            "Audit-behind restore",
            "Audit-ahead restore",
            "current integrity mechanism is compromised",
            "narrow authorised Audit lookup",
            "unauthorised or insufficiently scoped bulk/high-sensitivity Audit access",
            "Audit export creation/expiry without a permanent shadow",
            "routine Communications provider observations are duplicate/reordered",
            "successful Account plus PMR creation versus failed/ambiguous Account creation",
            "duplicate-account reconciliation with Identity as canonical-truth owner",
        )
        for index, expected in enumerate(required):
            self.assertIn(expected.casefold(), cases[index].casefold())

    def test_mechanisms_and_future_event_selection_remain_unfrozen(self):
        downstream = _section(
            self.candidate,
            "## 16. Unresolved items and replaceable mechanisms",
            "## 17. Current governance state and lifecycle",
        )
        for unresolved in (
            "EXPERT_LEGAL_PRIVACY",
            "IMPLEMENTATION_PROOF",
            "LATER FEATURE PACK",
            "PROVIDER_EMPIRICAL",
            "RELEASE_ONLY",
        ):
            self.assertIn(unresolved, downstream)
        for choice in (
            "Ash Temporal Resources",
            "Ash Resource layout",
            "database schemas/tables/indexes",
            "transaction implementation",
            "Oban job shape",
            "queue topology",
            "Redis/ETS/cache choices",
            "provider APIs",
            "exact idempotency key strings",
            "PostgreSQL extensions",
            "hash-chain/signature/Merkle/WORM design",
            "object-lock infrastructure",
            "key-management implementation",
            "exact RPO/RTO values",
            "object-storage topology",
            "infrastructure account/role implementation",
        ):
            self.assertIn(choice.casefold(), downstream.casefold())
        self.assertIn("later feature packs must perform their own event selection", downstream.casefold())

    def test_working_discovery_ids_are_not_promoted_to_product_or_decision_authority(self):
        self.assertIn("AE-WD-* identifiers remain working discovery identifiers", self.candidate)
        self.assertIsNone(re.search(r"AE-WD-\d{3}", self.candidate))
        for path in (
            "docs/00_platform/00_PLATFORM_v1.8.0.md",
            "docs/00_platform/01_DECISIONS_v1.8.0.md",
        ):
            self.assertNotRegex((ROOT / path).read_text(encoding="utf-8"), r"AE-WD-\d{3}")


if __name__ == "__main__":
    unittest.main()
