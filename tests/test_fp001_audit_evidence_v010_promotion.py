import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

from tests.foundation_test_support import (
    current_document_path,
    git_changed_paths,
    current_working_path,
)


# PR #119 resulting main recorded by the Phase 7B baseline.
HISTORICAL_SCOPE_HEAD = "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd"

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
BASE_MAIN = "3566f1353ef34af58773aa13c6f5bd61d2613d96"
CERTIFIED_CANDIDATE = "68df8bfb2723c6d4bb414fffae63f20ba0744a6d"
AUDIT_CANDIDATE_SHA256 = "0b0a8fb64a3ac602ebb81a7ab957a9dd075412350c818e4c6e5f13f667f7daea"
AUDIT_CURRENT_PATH = DOCS / "working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
AUDIT_ARCHIVE_PATH = DOCS / "archive/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
PROMOTION_MARKER_START = "<!-- AUDIT_EVIDENCE_V010_CURRENT_LIFECYCLE_STATE_START -->"
PROMOTION_MARKER_END = "<!-- AUDIT_EVIDENCE_V010_CURRENT_LIFECYCLE_STATE_END -->"

PREDECESSORS = (
    (
        "docs/00_platform/02_OPEN_WORK_v1.2.64.md",
        "docs/00_platform/archive/02_OPEN_WORK_v1.2.64.md",
    ),
    (
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md",
        "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.8.md",
    ),
    (
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.6.md",
        "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.6.md",
    ),
    (
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.8.md",
        "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.8.md",
    ),
)

PROTECTED_PATHS = (
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
    "docs/00_platform/00_PLATFORM_v1.8.0.md",
    "docs/00_platform/01_DECISIONS_v1.8.0.md",
    "docs/00_platform/03_ARCHITECTURE_v1.1.1.md",
    "docs/00_platform/04_DOMAIN_MAP_v1.2.0.md",
    "docs/00_platform/archive/05_ROADMAP_v1.2.2.md",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md",
    "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
    "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
)


def _git_show(commit: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def _lifecycle_state(text: str) -> dict:
    pattern = re.escape(PROMOTION_MARKER_START) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(PROMOTION_MARKER_END)
    match = re.search(pattern, text, re.DOTALL)
    if match is None:
        return {}
    return json.loads(match.group(1))


def _section(text: str, start: str, end: str) -> str:
    return text[text.index(start) : text.index(end, text.index(start) + len(start))]


class Fp001AuditEvidenceV010PromotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit_current = AUDIT_CURRENT_PATH.read_text(encoding="utf-8") if AUDIT_CURRENT_PATH.exists() else ""
        cls.audit_archive = AUDIT_ARCHIVE_PATH.read_bytes() if AUDIT_ARCHIVE_PATH.exists() else b""
        cls.audit_candidate = cls.audit_archive.decode("utf-8")
        cls.lifecycle = _lifecycle_state(cls.audit_current) if cls.audit_current else {}
        cls.manifest = json.loads((DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json").read_text(encoding="utf-8"))
        cls.readme = (DOCS / "README.md").read_text(encoding="utf-8")
        cls.open_work_path = DOCS / "archive/02_OPEN_WORK_v1.2.65.md"
        cls.open_work = cls.open_work_path.read_text(encoding="utf-8") if cls.open_work_path.exists() else ""
        cls.atlas_path = DOCS / "archive/DELIVERY_ATLAS_WORKING_v0.4.7.md"
        cls.atlas = cls.atlas_path.read_text(encoding="utf-8") if cls.atlas_path.exists() else ""
        cls.skeleton_path = DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.9.md"
        cls.skeleton = cls.skeleton_path.read_text(encoding="utf-8") if cls.skeleton_path.exists() else ""
        cls.harden_path = DOCS / "archive/HARDEN-02_CONTRACT_WORKING_v0.5.9.md"
        cls.harden = cls.harden_path.read_text(encoding="utf-8") if cls.harden_path.exists() else ""

    def test_certified_candidate_archive_has_the_exact_sha256(self):
        self.assertTrue(AUDIT_ARCHIVE_PATH.is_file())
        self.assertEqual(AUDIT_CANDIDATE_SHA256, hashlib.sha256(self.audit_archive).hexdigest())
        self.assertEqual(
            self.audit_archive,
            _git_show(CERTIFIED_CANDIDATE, "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"),
        )

    def test_current_dossier_is_a_narrow_v010_status_successor(self):
        for marker in (
            "Artifact version:** v0.1.0 narrow status successor",
            "PHASE 7B JIT DOMAIN DOSSIER",
            "IMPLEMENTATION-GRADE PLANNING LAW",
            "NON-EXECUTABLE",
            "NOT PHASE 7C DEVELOPMENT-ENTRY AUTHORITY",
            "DOES NOT OVERRIDE PRODUCT / ARCHITECTURE / DOMAIN / ROADMAP LAW",
        ):
            self.assertIn(marker, self.audit_current)
        self.assertIn("PR #118", self.audit_current)
        self.assertIn("68df8bfb2723c6d4bb414fffae63f20ba0744a6d", self.audit_current)
        self.assertIn("5f5a994e48d9458aaa6397044b3af4d72c5d5e81", self.audit_current)
        self.assertIn("acd04f523997a0ae8a7ae3edbbfb9280bd4de1ca", self.audit_current)
        self.assertIn("3566f1353ef34af58773aa13c6f5bd61d2613d96", self.audit_current)
        self.assertIn("38698409603", self.audit_current)
        self.assertIn("38704942507", self.audit_current)
        self.assertIn("Independent exact-head review | PASS", self.audit_current)
        self.assertIn("Candidate/resulting-main tree identity | PASS", self.audit_current)

    def test_certified_candidate_semantic_body_is_preserved_byte_for_byte(self):
        body_start = "## 1. Baseline, purpose and scope"
        self.assertIn(body_start, self.audit_candidate)
        self.assertIn(body_start, self.audit_current)
        self.assertEqual(
            self.audit_archive[self.audit_archive.index(body_start.encode("utf-8")) :],
            AUDIT_CURRENT_PATH.read_bytes()[AUDIT_CURRENT_PATH.read_bytes().index(body_start.encode("utf-8")) :],
        )

    def test_current_lifecycle_and_downstream_stops_are_exact(self):
        self.assertEqual(1, self.audit_current.count(PROMOTION_MARKER_START))
        self.assertEqual(1, self.audit_current.count(PROMOTION_MARKER_END))
        expected = {
            "artifact_version": "v0.1.0",
            "audit_lifecycle": "CERTIFIED / CURRENT",
            "pr_118_candidate_certification": "COMPLETE",
            "pr_118_post_merge_certification_evidence": "COMPLETE",
            "phase_7b_reconciliation": "NEXT / NOT_STARTED",
            "phase_7c": "BLOCKED / NOT_STARTED",
            "proof_classification": "NOT FINALISED",
            "phase_8_application_implementation": "UNAUTHORISED",
        }
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertEqual(value, self.lifecycle.get(key))
        self.assertEqual("PR #119 STATUS SUCCESSOR", self.lifecycle.get("current_status_promotion"))
        self.assertIn("Phase 7C remains `BLOCKED / NOT_STARTED` until successful Phase 7B reconciliation", self.audit_current)
        self.assertIn("Proof classification remains `NOT FINALISED`", self.audit_current)
        self.assertIn("Phase 8/application implementation remains `UNAUTHORISED`", self.audit_current)

    def test_current_open_work_records_complete_dossier_set_and_next_reconciliation(self):
        for required in (
            "AUDIT & EVIDENCE DOSSIER: REQUIRED / COMPLETE / CERTIFIED / CURRENT",
            "IDENTITY & ACCESS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4",
            "COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "PRIVACY & CONSENT: NOT_REQUIRED",
            "CONTENT & MEDIA: NOT_REQUIRED",
            "ANALYTICS: NOT_REQUIRED",
            "NEXT STAGE: FP-001 PHASE 7B RECONCILIATION",
            "PHASE 7C: BLOCKED / NOT_STARTED",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "EXECUTABLE DEVELOPMENT: UNAUTHORISED",
        ):
            self.assertIn(required, self.open_work)
        self.assertNotIn("AUDIT & EVIDENCE DOSSIER: REQUIRED / IN PROGRESS / NOT COMPLETE", self.open_work)
        self.assertNotIn("PHASE 7B RECONCILIATION: COMPLETE", self.open_work)

    def test_routing_successors_and_manifest_agree(self):
        current_routes = (
            current_working_path(ROOT, "DELIVERY_ATLAS_WORKING_"),
            current_working_path(ROOT, "FP-001_FEATURE_PACK_SKELETON_WORKING_"),
            current_working_path(ROOT, "HARDEN-02_CONTRACT_WORKING_"),
            current_working_path(ROOT, "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_"),
            current_working_path(ROOT, "FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_"),
        )
        current_open_work = current_document_path(ROOT, "OPEN_WORK")
        self.assertIn(current_open_work.relative_to(ROOT / "docs/00_platform").as_posix(), self.readme)
        for route in current_routes:
            with self.subTest(route=route):
                path = route.relative_to(ROOT / "docs/00_platform").as_posix()
                self.assertIn(path, self.readme)
        self.assertIn("FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", self.readme)
        audit_route = "working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        for artifact in (self.atlas, self.skeleton, self.harden):
            with self.subTest(artifact=artifact[:40]):
                self.assertIn(audit_route, artifact)
        open_work = next(row for row in self.manifest["governing_documents"] if row["document_id"] == "OPEN_WORK")
        current_open_work = current_document_path(ROOT, "OPEN_WORK")
        self.assertEqual(current_open_work.name, open_work["canonical_filename"])
        self.assertEqual(current_open_work.relative_to(ROOT).as_posix(), open_work["repository_path"])
        navigation = self.manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]
        for path in [route.relative_to(ROOT).as_posix() for route in current_routes] + [
            "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        ]:
            self.assertIn(path, navigation)
        historical = json.dumps(self.manifest["historical_documents"])
        self.assertIn("FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", historical)
        self.assertNotIn("FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", json.dumps(self.manifest["governing_documents"]))

    def test_manifest_distinguishes_candidate_pr_from_current_status_promotion(self):
        guard_note = self.manifest["integrity_rules"]["graph_rules"]["stale_predecessor_current_path_guard_note"]
        self.assertIn("The separate PR #119 Audit v0.1.0 current-status promotion", guard_note)
        self.assertNotIn("The separate PR #118 Audit v0.1.0 current-status promotion", guard_note)
        self.assertIn("the exact PR #118 candidate is pinned as historical certification evidence", guard_note)

    def test_current_skeleton_records_status_promotion_and_reconciliation_boundary(self):
        self.assertIn("Audit & Evidence v0.1.0 are `REQUIRED / COMPLETE / CERTIFIED / CURRENT`", self.skeleton)
        self.assertIn("records the Audit v0.1.0 current-status promotion", self.skeleton)
        self.assertIn("Phase 7B reconciliation is `NEXT / NOT_STARTED`", self.skeleton)
        self.assertNotIn("records the work start for the already-adjudicated required FP-001 Audit & Evidence JIT Domain Dossier", self.skeleton)
        for preserved in (
            "preserves accepted PMR reconciliation semantics",
            "all seven material capability relationships",
            "the six affected Domains",
            "the existing stage gates",
            "does not perform Phase 7B reconciliation",
            "does not authorise Phase 7C",
            "does not finalise proof classification",
            "does not authorise Phase 8/application implementation",
        ):
            with self.subTest(preserved=preserved):
                self.assertIn(preserved, self.skeleton)

    def test_atlas_historical_candidate_review_route_uses_open_work_v1264(self):
        historical = _section(
            self.atlas,
            "## v0.4.6 Patch Scope (historical predecessor record)",
            "## v0.4.4 Patch Scope",
        )
        current_header = self.atlas.split("## v0.4.6 Patch Scope", 1)[0]
        self.assertIn("Open Work v1.2.64", historical)
        self.assertNotIn("Open Work v1.2.65", historical)
        self.assertIn("review-ready in PR #118", historical)
        self.assertIn("NOT CERTIFIED / NOT CURRENT", historical)
        self.assertIn("Open Work v1.2.65", current_header)
        self.assertIn("separate current-status promotion PR #119", current_header)

    def test_harden_v059_preserves_v058_predecessor_provenance(self):
        header = self.harden.split("### Revision log", 1)[0]
        self.assertEqual(1, header.count("v0.5.9 current-status successor base main SHA"))
        self.assertIn(
            "v0.5.9 current-status successor base main SHA:** `3566f1353ef34af58773aa13c6f5bd61d2613d96`",
            header,
        )
        self.assertEqual(1, header.count("v0.5.8 routing-successor base main SHA"))
        self.assertIn(
            "v0.5.8 routing-successor base main SHA:** `5f5a994e48d9458aaa6397044b3af4d72c5d5e81`",
            header,
        )
        self.assertIn("v0.5.7 routing-successor base main SHA", header)
        self.assertNotIn("v0.5.9 routing-successor base main SHA", self.harden)

    def test_current_skeleton_keeps_fp001_scope_and_dossier_dispositions(self):
        self.assertIn("REQUIRED / COMPLETE / CERTIFIED / CURRENT", self.skeleton)
        for disposition in ("Identity & Access", "Privacy & Consent", "Content & Media", "Communications", "Audit & Evidence", "Analytics"):
            self.assertIn(disposition, self.skeleton)
        capabilities = re.findall(r"(?m)^\| `(CAP-\d{3})` \| `I` \|", self.skeleton)
        self.assertEqual(["CAP-001", "CAP-002", "CAP-003", "CAP-005", "CAP-006", "CAP-017", "CAP-028"], capabilities)
        domain_section = _section(self.skeleton, "## 7. Domain participation", "## 8. Phase 7B dossier discovery")
        domains = re.findall(
            r"(?m)^\| (Identity & Access|Privacy & Consent|Content & Media|Communications|Audit & Evidence|Analytics) \|",
            domain_section,
        )
        self.assertEqual(
            ["Identity & Access", "Privacy & Consent", "Content & Media", "Communications", "Audit & Evidence", "Analytics"],
            domains,
        )

    def test_all_immediate_predecessors_are_archived_byte_identically(self):
        for source, archived in PREDECESSORS:
            with self.subTest(archived=archived):
                self.assertEqual(_git_show(BASE_MAIN, source), (ROOT / archived).read_bytes())

    def test_no_upstream_authority_or_application_source_changed(self):
        for path in PROTECTED_PATHS:
            with self.subTest(path=path):
                baseline_path = (
                    "docs/00_platform/05_ROADMAP_v1.2.2.md"
                    if path == "docs/00_platform/archive/05_ROADMAP_v1.2.2.md"
                    else path
                )
                workspace_path = path
                if path == "docs/00_platform/00_PLATFORM_v1.8.0.md":
                    workspace_path = "docs/00_platform/archive/00_PLATFORM_v1.8.0.md"
                elif path == "docs/00_platform/01_DECISIONS_v1.8.0.md":
                    workspace_path = "docs/00_platform/archive/01_DECISIONS_v1.8.0.md"
                elif path == "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md":
                    workspace_path = "docs/00_platform/archive/PLATFORM_OPERATING_MODEL_v1.0.1.md"
                elif path.endswith("FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"):
                    workspace_path = "docs/00_platform/archive/identity_promotions/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                self.assertEqual(_git_show(BASE_MAIN, baseline_path), (ROOT / workspace_path).read_bytes())
        changed = git_changed_paths(ROOT, BASE_MAIN, HISTORICAL_SCOPE_HEAD)
        application_prefixes = ("app/", "apps/", "backend/", "frontend/", "lib/", "src/")
        self.assertEqual([], [path for path in changed if path.startswith(application_prefixes)])


if __name__ == "__main__":
    unittest.main()
