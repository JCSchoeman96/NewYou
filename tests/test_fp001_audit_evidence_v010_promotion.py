import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path


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
    "docs/00_platform/05_ROADMAP_v1.2.2.md",
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
        cls.open_work_path = DOCS / "02_OPEN_WORK_v1.2.65.md"
        cls.open_work = cls.open_work_path.read_text(encoding="utf-8") if cls.open_work_path.exists() else ""
        cls.atlas_path = DOCS / "working/DELIVERY_ATLAS_WORKING_v0.4.7.md"
        cls.atlas = cls.atlas_path.read_text(encoding="utf-8") if cls.atlas_path.exists() else ""
        cls.skeleton_path = DOCS / "working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.9.md"
        cls.skeleton = cls.skeleton_path.read_text(encoding="utf-8") if cls.skeleton_path.exists() else ""
        cls.harden_path = DOCS / "working/HARDEN-02_CONTRACT_WORKING_v0.5.9.md"
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
        for version in ("v1.2.65", "v0.4.7", "v0.1.9", "v0.5.9", "v0.1.4", "v0.1.0"):
            with self.subTest(version=version):
                self.assertIn(version, self.readme)
        self.assertIn("FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", self.readme)
        audit_route = "working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
        for artifact in (self.atlas, self.skeleton, self.harden):
            with self.subTest(artifact=artifact[:40]):
                self.assertIn(audit_route, artifact)
        open_work = next(row for row in self.manifest["governing_documents"] if row["document_id"] == "OPEN_WORK")
        self.assertEqual("1.2.65", open_work["semver"])
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.65.md", open_work["repository_path"])
        navigation = self.manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"]
        for path in (
            "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.7.md",
            "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.9.md",
            "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.9.md",
            "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
            "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
            "docs/00_platform/working/FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
        ):
            self.assertIn(path, navigation)
        historical = json.dumps(self.manifest["historical_documents"])
        self.assertIn("FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", historical)
        self.assertNotIn("FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md", json.dumps(self.manifest["governing_documents"]))

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
                self.assertEqual(_git_show(BASE_MAIN, path), (ROOT / path).read_bytes())
        changed = subprocess.run(
            ["git", "diff", "--name-only", BASE_MAIN],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        application_prefixes = ("app/", "apps/", "backend/", "frontend/", "lib/", "src/")
        self.assertEqual([], [path for path in changed if path.startswith(application_prefixes)])


if __name__ == "__main__":
    unittest.main()
