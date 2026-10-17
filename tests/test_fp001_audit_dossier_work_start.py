import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
AUDIT_STATUS = "REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"
AUDIT_CANDIDATE_STATUS = "CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT"
NEXT_ACTION = "FRESH INDEPENDENT EXACT-HEAD CANDIDATE REVIEW/CERTIFICATION"

SEMANTIC_AUTHORITY_SHA256 = {
    "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md": "249f5985ff1e8971e1ac4437e4bbebd5a3db9254ab25a2238e135cb7a7ae5f4b",
    "00_PLATFORM_v1.8.0.md": "cb93abfee9a6337a7f2a23c16f35413b8b2ea84608974fcf5a0033822578905e",
    "01_DECISIONS_v1.8.0.md": "123d3a622f89c22e364df565b87117c22244378c5c51b10d621597909b569140",
    "03_ARCHITECTURE_v1.1.1.md": "342d02a7946f99aca9e6683647fc3a2505901b3d0cc2d13c21d807442025f0b3",
    "04_DOMAIN_MAP_v1.2.0.md": "e09e14ee0a773c5855257c48685cf3a75d413c983a98d22a56b42af57dc2c078",
    "05_ROADMAP_v1.2.2.md": "4225fad688589d3c66733527303cbda39ef3c8bf52b78c4cc372c0736d202cdc",
    "PLATFORM_OPERATING_MODEL_v1.0.1.md": "7cb725adcdb796ba112d39c4be6fd09c90026b49e772b61f0867db62828b9d12",
    "FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md": "58c733e8e0cc73c72b102b623cb756b60cbadb084f8cc710051be42d0877fdb4",
}


def _navigation_path(manifest: dict, filename_prefix: str) -> Path:
    paths = manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]
    relative = next(Path(path) for path in paths if Path(path).name.startswith(filename_prefix))
    return ROOT / relative


def _section(text: str, start: str, end: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index + len(start))
    return text[start_index:end_index]


class Fp001AuditDossierWorkStartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        current_open_work_entry = next(
            row
            for row in cls.manifest["governing_documents"]
            if row["document_id"] == "OPEN_WORK"
        )
        open_work_entry = next(
            row
            for row in cls.manifest["historical_documents"]
            if row["document_id"] == "OPEN_WORK_V1_2_64"
        )
        cls.open_work_entry = open_work_entry
        cls.current_open_work_entry = current_open_work_entry
        cls.open_work_path = ROOT / open_work_entry["repository_path"]
        cls.open_work = cls.open_work_path.read_text(encoding="utf-8")
        cls.atlas_path = DOCS / "archive/DELIVERY_ATLAS_WORKING_v0.4.6.md"
        cls.skeleton_path = DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md"
        cls.harden_path = DOCS / "archive/HARDEN-02_CONTRACT_WORKING_v0.5.8.md"
        cls.atlas = cls.atlas_path.read_text(encoding="utf-8")
        cls.skeleton = cls.skeleton_path.read_text(encoding="utf-8")
        cls.harden = cls.harden_path.read_text(encoding="utf-8")
        cls.readme = subprocess.check_output(
            ["git", "show", "3566f1353ef34af58773aa13c6f5bd61d2613d96:docs/00_platform/README.md"],
            cwd=ROOT,
        ).decode("utf-8")
        state_match = re.search(
            r"<!-- HARDEN_02_LIFECYCLE_STATE_START -->\s*```json\s*(.*?)\s*```\s*<!-- HARDEN_02_LIFECYCLE_STATE_END -->",
            cls.open_work,
            re.DOTALL,
        )
        cls.lifecycle_state = json.loads(state_match.group(1)) if state_match else {}

    def test_candidate_review_successors_are_preserved_as_archived_predecessors(self):
        self.assertEqual("02_OPEN_WORK_v1.2.64.md", self.open_work_path.name)
        self.assertEqual("DELIVERY_ATLAS_WORKING_v0.4.6.md", self.atlas_path.name)
        self.assertEqual("FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md", self.skeleton_path.name)
        self.assertEqual("HARDEN-02_CONTRACT_WORKING_v0.5.8.md", self.harden_path.name)
        self.assertEqual("1.2.65", self.current_open_work_entry["semver"])

    def test_open_work_manifest_lineage_registers_its_immediate_predecessor(self):
        current = self.current_open_work_entry
        self.assertEqual("1.2.65", current["semver"])
        self.assertEqual("1.2.64", current["superseded_version"])

        historical = self.open_work_entry
        self.assertEqual("02_OPEN_WORK_v1.2.64.md", historical["canonical_filename"])
        self.assertEqual("1.2.64", historical["semver"])
        self.assertEqual(
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.64.md",
            historical["repository_path"],
        )
        self.assertEqual("PLANNING_TRACKER_HISTORICAL", historical["authority_class"])
        self.assertEqual("1.2.65", historical["superseded_version"])
        self.assertEqual("historical", historical["lifecycle"])
        self.assertEqual(
            "1a96a3720de79432255e6ad2c947221900233b6928ef1e64150d1fa08a54a494",
            historical["sha256"],
        )
        self.assertEqual(historical["sha256"], historical["provenance_sha256"])
        archive_path = ROOT / historical["repository_path"]
        self.assertEqual(historical["sha256"], hashlib.sha256(archive_path.read_bytes()).hexdigest())

    def test_immediate_predecessor_paths_are_rejected_unless_archive_qualified(self):
        retired_predecessors = (
            ("(?<!archive/)02_OPEN_WORK_v1\\.2\\.64\\.md", "02_OPEN_WORK_v1.2.64.md"),
            ("(?<!archive/)DELIVERY_ATLAS_WORKING_v0\\.4\\.6\\.md", "DELIVERY_ATLAS_WORKING_v0.4.6.md"),
            (
                "(?<!archive/)FP-001_FEATURE_PACK_SKELETON_WORKING_v0\\.1\\.8\\.md",
                "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md",
            ),
            ("(?<!archive/)HARDEN-02_CONTRACT_WORKING_v0\\.5\\.8\\.md", "HARDEN-02_CONTRACT_WORKING_v0.5.8.md"),
        )
        configured = self.manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"]
        for pattern, filename in retired_predecessors:
            with self.subTest(filename=filename):
                self.assertIn(pattern, configured)
                self.assertIsNotNone(re.search(pattern, filename))
                self.assertIsNone(re.search(pattern, f"archive/{filename}"))

        guard_note = self.manifest["integrity_rules"]["graph_rules"]["stale_predecessor_current_path_guard_note"]
        for current in ("v1.2.65", "v0.4.7", "v0.1.9", "v0.5.9"):
            self.assertIn(current, guard_note)
        for predecessor in ("v1.2.64", "v0.4.6", "v0.1.8", "v0.5.8"):
            self.assertIn(predecessor, guard_note)

    def test_status_successors_preserve_their_direct_predecessors_byte_for_byte(self):
        predecessors = (
            ("docs/00_platform/02_OPEN_WORK_v1.2.64.md", "docs/00_platform/archive/02_OPEN_WORK_v1.2.64.md"),
            ("docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md", "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md"),
            ("docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.6.md", "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.6.md"),
            ("docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.8.md", "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.8.md"),
        )
        for source, archived in predecessors:
            with self.subTest(path=archived):
                expected = subprocess.check_output(["git", "show", f"3566f1353ef34af58773aa13c6f5bd61d2613d96:{source}"], cwd=ROOT)
                self.assertEqual(expected, (ROOT / archived).read_bytes())

    def test_audit_is_in_progress_and_certification_is_pending(self):
        state = self.lifecycle_state
        self.assertEqual(AUDIT_STATUS, state.get("audit_dossier"))
        self.assertEqual(AUDIT_STATUS, state.get("conditional_dossiers", {}).get("audit_evidence"))
        self.assertEqual("FP-001 PHASE 7B AUDIT & EVIDENCE JIT DOMAIN DOSSIER CANDIDATE REVIEW", state.get("current_stage"))
        self.assertEqual(NEXT_ACTION, state.get("next_stage"))
        self.assertEqual(116, state.get("audit_dossier_execution_tracker_issue"))
        self.assertEqual(118, state.get("audit_dossier_candidate_pr"))
        self.assertEqual("332d51f19d77430fe4e95911920fe0c87cab524a", state.get("audit_dossier_work_start_baseline_main_sha"))
        self.assertNotEqual("COMPLETE / CERTIFIED / CURRENT", state.get("audit_dossier"))
        self.assertNotIn("CERTIFIED", state.get("audit_dossier", ""))
        self.assertNotIn("CURRENT", state.get("audit_dossier", ""))
        self.assertIn(f"AUDIT & EVIDENCE DOSSIER: {AUDIT_STATUS}", self.open_work)

    def test_audit_dossier_candidate_is_present_but_remains_non_current(self):
        active_dossiers = [
            path
            for path in DOCS.rglob("*.md")
            if path.name.startswith("FP-001")
            and "AUDIT" in path.name.upper()
            and "DOSSIER" in path.name.upper()
            and "archive" not in path.parts
        ]
        current = DOCS / "working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        candidate = DOCS / "archive/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        self.assertEqual([current], active_dossiers)
        self.assertTrue(candidate.is_file())
        self.assertIn(AUDIT_CANDIDATE_STATUS, candidate.read_text(encoding="utf-8"))
        self.assertEqual(AUDIT_STATUS, self.lifecycle_state.get("audit_dossier"))
        self.assertEqual(
            AUDIT_CANDIDATE_STATUS,
            self.lifecycle_state.get("audit_dossier_candidate"),
        )
        self.assertIn("CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT", self.open_work)
        self.assertIn("AUDIT DOSSIER CANDIDATE PR: #118", self.open_work)
        self.assertNotIn("CERTIFIED", self.lifecycle_state.get("audit_dossier", ""))
        self.assertNotIn("CURRENT", self.lifecycle_state.get("audit_dossier", ""))

    def test_other_fp001_dossier_dispositions_are_unchanged(self):
        state = self.lifecycle_state
        self.assertEqual("NOT_REQUIRED", state["conditional_dossiers"]["privacy_consent"])
        self.assertEqual("NOT_REQUIRED", state["conditional_dossiers"]["content_media"])
        self.assertEqual("NOT_REQUIRED", state["conditional_dossiers"]["analytics"])
        self.assertIn("IDENTITY & ACCESS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4", self.open_work)
        self.assertIn("COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0", self.open_work)
        self.assertIn("PRIVACY & CONSENT: NOT_REQUIRED", self.open_work)
        self.assertIn("CONTENT & MEDIA: NOT_REQUIRED", self.open_work)
        self.assertIn("ANALYTICS: NOT_REQUIRED", self.open_work)

    def test_phase_7c_proof_and_implementation_stops_remain(self):
        state = self.lifecycle_state
        self.assertEqual("BLOCKED / NOT_STARTED", state.get("phase_7c"))
        self.assertEqual("NOT FINALISED", state.get("proof_classification"))
        self.assertEqual(
            "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
            state.get("application_implementation"),
        )
        self.assertIn("PHASE 7C: BLOCKED / NOT_STARTED", self.open_work)
        self.assertIn("PROOF CLASSIFICATION: NOT FINALISED", self.open_work)
        self.assertIn("EXECUTABLE DEVELOPMENT: UNAUTHORISED", self.open_work)

    def test_next_route_is_fresh_independent_candidate_review_and_certification(self):
        current_state = self.open_work.split("# 9. Immediate Next Action", 1)[1].split("# 10. Minimal Tools", 1)[0]
        next_routes = re.findall(r"(?m)^NEXT STAGE:\s*(.*?)\s*$", current_state)
        self.assertEqual([NEXT_ACTION], next_routes)
        self.assertIn("candidate v0.1.0 is authored and review-ready in pr #118", self.skeleton.casefold())
        self.assertIn("NOT CERTIFIED / NOT CURRENT", self.skeleton)
        self.assertNotIn("NEXT STAGE: FP-001 PHASE 7C", self.open_work)
        self.assertNotIn("NEXT STAGE: FP-001 PHASE 7B RECONCILIATION", self.open_work)

    def test_current_harden_route_keeps_audit_uncertified_and_phase_8_unauthorised(self):
        harden_route = self.harden.split("## 21. Current execution certification and next stage", 1)[1]
        self.assertIn(
            "AUDIT DOSSIER CANDIDATE: CANDIDATE / REVIEW-READY / NOT CERTIFIED / NOT CURRENT",
            harden_route,
        )
        self.assertIn(
            "EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
            harden_route,
        )
        readme = self.readme
        self.assertIn(
            "- EXECUTABLE DEVELOPMENT: UNAUTHORISED; PHASE 8 ENTRY CONDITIONS HAVE NOT PASSED",
            readme.split("## Current State", 1)[1],
        )
        open_work_harden_status = self.open_work.split(
            "## 12.9 — HARDEN-02 contract lifecycle completion", 1
        )[1].split("## 12.10", 1)[0]
        self.assertIn("candidate v0.1.0 is authored and review-ready in pr #118", open_work_harden_status.casefold())

    def test_audit_prejit_hypotheses_remain_non_authoritative(self):
        for required in (
            "WORKING / NON-AUTHORITATIVE PRE-JIT EVIDENCE",
            "central evidence selection precedes E1/E2 classification",
            "E1 concerns selected evidence required before a protected effect",
            "E2 permits source truth to commit only when the same acceptance boundary establishes a durable, lossless, replay-safe evidence obligation",
            "Source Domains remain authoritative for their business truth",
            "Audit does not repair or reinterpret source concurrency",
            "corrections and supersessions are append-only",
            "minimum accountability envelopes are preferred over source-data snapshots",
            "privileged Audit access is independently governed",
            "retention meaning is distinct from semantic meaning",
            "central Audit must not become a duplicate permanent stream for every routine authentication or provider observation",
            "No unresolved Audit-specific Product or Architecture amendment prerequisite was identified",
            "AE-WD-* identifiers are not promoted into Product Law or Decision Register entries",
        ):
            self.assertIn(required, self.open_work)

    def test_approved_scope_and_roadmap_contract_match_the_archived_skeleton(self):
        predecessor = DOCS / "archive" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.6.md"
        self.assertTrue(predecessor.is_file(), "direct Skeleton predecessor must be archived byte-identically")
        prior = predecessor.read_text(encoding="utf-8")
        stable_sections = (
            ("## 1. Identity", "## 2. Outcome"),
            ("## 2. Outcome", "## 3. Validation objective"),
            ("## 3. Validation objective", "## 4. Validation objective type"),
            ("## 5. Scope", "## 6. Material capability input"),
            ("## 6. Material capability input", "## 7. Domain participation"),
        )
        for start, end in stable_sections:
            self.assertEqual(_section(prior, start, end), _section(self.skeleton, start, end), start)
        domain_section = _section(self.skeleton, "## 7. Domain participation", "## 8. Phase 7B dossier discovery")
        self.assertEqual(
            ["Identity & Access", "Privacy & Consent", "Content & Media", "Communications", "Audit & Evidence", "Analytics"],
            re.findall(r"(?m)^\| (Identity & Access|Privacy & Consent|Content & Media|Communications|Audit & Evidence|Analytics) \|", domain_section),
        )
        capability_section = _section(self.skeleton, "## 6. Material capability input", "## 7. Domain participation")
        self.assertEqual(["001", "002", "003", "005", "006", "017", "028"], re.findall(r"(?m)^\| `CAP-(\d+)` \| `I` \|", capability_section))
        self.assertIn(
            "APPROVED AFFECTED DOMAINS: IDENTITY & ACCESS; PRIVACY & CONSENT; CONTENT & MEDIA; COMMUNICATIONS; AUDIT & EVIDENCE; ANALYTICS",
            self.open_work,
        )
        self.assertIn(
            "MATERIAL CAPABILITY RELATIONSHIPS: CAP-001, CAP-002, CAP-003, CAP-005, CAP-006, CAP-017, CAP-028 (seven; unchanged)",
            self.open_work,
        )

    def test_current_routes_and_audit_prejit_boundary_are_explicit(self):
        self.assertIn("#116", self.open_work)
        self.assertIn("#114", self.open_work)
        self.assertIn("#111", self.open_work)
        self.assertIn("Audit & Evidence owns its own evidence truth only. Source Domains remain authoritative for their business truth", self.open_work)
        self.assertIn("Audit Pre-JIT pack is WORKING / NON-AUTHORITATIVE PRE-JIT EVIDENCE", self.open_work)
        self.assertIn("Phase 7C would otherwise have to invent the FP-001 Audit event-selection, evidence-acceptance, correlation/idempotency, minimisation, privileged-access, append-only correction/supersession and retention-category contracts", self.open_work)
        self.assertIn("- AUDIT & EVIDENCE DOSSIER: REQUIRED / IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING", self.readme)

    def test_semantic_authorities_match_the_verified_main_baseline(self):
        for filename, expected_hash in SEMANTIC_AUTHORITY_SHA256.items():
            actual_hash = hashlib.sha256((DOCS / filename).read_bytes()).hexdigest()
            self.assertEqual(expected_hash, actual_hash, filename)


if __name__ == "__main__":
    unittest.main()
