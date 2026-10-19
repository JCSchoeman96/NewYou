from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import _markdown_h2_section, run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
BASELINE_MAIN_SHA = "f24786eec8ff4d60f6f8cdf9dbe7947556fe87c3"
PR_121_CANDIDATE_SHA = "b6f82218026f3372ccacc96ffdbb37430e8e503f"
MERGE_TREE_SHA = "98e553d45006136277e4b2aa629c97c31f7742e2"
ARCHIVED_CANDIDATE_SHA256 = "274306e73e2450806516a5b76ca96f1a768af7824ba823cca6c9371c58e65401"
POST_MERGE_ATTESTATION_URL = (
    "https://github.com/JCSchoeman96/NewYou/pull/121#issuecomment-6235345322"
)

ARCHIVED_CANDIDATE = (
    "docs/00_platform/archive/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
)
CURRENT_RECONCILIATION = (
    "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md"
)
LIFECYCLE_START = "<!-- HARDEN_02_LIFECYCLE_STATE_START -->"
LIFECYCLE_END = "<!-- HARDEN_02_LIFECYCLE_STATE_END -->"

ARCHIVE_PREDECESSORS = {
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.66.md": (
        "docs/00_platform/02_OPEN_WORK_v1.2.66.md",
        "96a61dd94098f3c9fbb4ba1a6c683e9a3484b62ee15306d8dd5d884ad84f2133",
    ),
    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.8.md": (
        "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.4.8.md",
        "e92f94d390cbf58173231daaedea00a0fac2a6d67fb69a0a7f6edab0e487af4e",
    ),
    "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md": (
        "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.10.md",
        "5d1332286bd8c9d7e86838f91b22edbf2e72afca1d8fb59edd28103e165c019b",
    ),
    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.10.md": (
        "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.10.md",
        "dad16d39906afede052e3cc94bb4c39568a1fe14215bb0b7b52e0e234b106f42",
    ),
}


def _git_show(commit: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _lifecycle_state(text: str) -> dict:
    pattern = (
        re.escape(LIFECYCLE_START)
        + r"\s*```json\s*(.*?)\s*```\s*"
        + re.escape(LIFECYCLE_END)
    )
    match = re.search(pattern, text, re.DOTALL)
    return json.loads(match.group(1)) if match else {}


def _section(text: str, start: str, end: str) -> str:
    return text[text.index(start) : text.index(end, text.index(start) + len(start))]


class FP001Phase7BReconciliationCertificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = _read_json(MANIFEST_PATH)
        cls.integrity_rules = cls.manifest["integrity_rules"]
        cls.candidate_rules = cls.integrity_rules["fp001_phase7b_reconciliation_candidate"]
        cls.current_path = ROOT / CURRENT_RECONCILIATION
        cls.archive_path = ROOT / ARCHIVED_CANDIDATE
        cls.current_text = cls.current_path.read_text(encoding="utf-8") if cls.current_path.exists() else ""
        cls.archive_bytes = cls.archive_path.read_bytes() if cls.archive_path.exists() else b""
        cls.archive_text = cls.archive_bytes.decode("utf-8")
        entries = {
            entry.get("document_id"): entry
            for group in ("governing_documents", "reference_documents")
            for entry in cls.manifest[group]
        }
        entries.update(
            {entry.get("document_id"): entry for entry in cls.manifest["historical_documents"]}
        )
        cls.entries = entries

    def test_archived_candidate_is_the_exact_pr_121_artifact(self):
        self.assertTrue(self.archive_path.is_file())
        self.assertEqual(
            ARCHIVED_CANDIDATE_SHA256,
            hashlib.sha256(self.archive_bytes).hexdigest(),
        )
        self.assertEqual(
            self.archive_bytes,
            _git_show(
                PR_121_CANDIDATE_SHA,
                "docs/00_platform/working/FP-001_PHASE_7B_RECONCILIATION_WORKING_v0.1.0.md",
            ),
        )
        archive_rules = self.integrity_rules.get(
            "fp001_phase7b_reconciliation_certification_archives", {}
        )
        self.assertEqual(
            ARCHIVED_CANDIDATE_SHA256,
            archive_rules.get(ARCHIVED_CANDIDATE),
        )

    def test_current_reconciliation_is_a_status_only_v010_successor(self):
        self.assertTrue(self.current_path.is_file())
        for token in (
            "FP-001 PHASE 7B RECONCILIATION\nCOMPLETE\nCERTIFIED\nCURRENT",
            "NON-IMPLEMENTATION",
            "NOT PHASE 7C",
            "NOT DEVELOPMENT-ENTRY AUTHORITY",
            "**Artifact version:** v0.1.0",
            "PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT",
            "RECONCILIATION v0.1.0: CERTIFIED / CURRENT",
            "PHASE 7C: NEXT / NOT_STARTED",
            "PROOF CLASSIFICATION: NOT FINALISED",
            "PHASE 8 / APPLICATION IMPLEMENTATION: UNAUTHORISED",
        ):
            with self.subTest(token=token):
                self.assertIn(token, self.current_text)

        self.assertEqual(
            _section(
                self.archive_text,
                "## 3. Reconciliation method and terms",
                "## 8. Candidate result and certification boundary",
            ),
            _section(
                self.current_text,
                "## 3. Reconciliation method and terms",
                "## 8. Candidate result and certification boundary",
            ),
        )
        rows = re.findall(r"(?m)^\| S-\d{2} \|", self.current_text)
        self.assertEqual(15, len(rows))
        self.assertIn("BLOCKING_AUTHORITY_GAP: NONE", self.current_text)
        self.assertIn("BLOCKING_DOSSIER_CONTRADICTION: NONE", self.current_text)

        for evidence in (
            PR_121_CANDIDATE_SHA,
            "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd",
            BASELINE_MAIN_SHA,
            MERGE_TREE_SHA,
            ARCHIVED_CANDIDATE_SHA256,
            "39035622705",
            "39041010709",
            "397 PASS",
            "646 assertions / PASS / 0 findings",
            "PR #121 comment 6235094794",
            POST_MERGE_ATTESTATION_URL,
            "Fresh independent post-merge review: PASS",
        ):
            with self.subTest(evidence=evidence):
                self.assertIn(evidence, self.current_text)
        self.assertRegex(
            self.current_text,
            r"(?m)^\| Exact-head run \| .*39035622705.*— PASS \|$",
        )
        self.assertRegex(
            self.current_text,
            r"(?m)^\| Resulting-main run \| .*39041010709.*— PASS \|$",
        )

    def test_current_readme_does_not_project_phase7c_as_blocked(self):
        readme = (DOCS / "README.md").read_text(encoding="utf-8")
        current_state = _markdown_h2_section(readme, "Current State")
        self.assertIsNotNone(current_state)
        current_state = current_state or ""
        self.assertIn("- PHASE 7B RECONCILIATION: COMPLETE / CERTIFIED / CURRENT", current_state)
        self.assertIn(
            "- PHASE 7C: COMPLETE / CERTIFIED / CURRENT",
            current_state,
        )
        self.assertIn("- PHASE 7C EXECUTION/CONTROL TRACKER #124: CLOSED / COMPLETED", current_state)
        self.assertIn("FP-001 FINAL FEATURE PACK CONTRACT v0.1.0: COMPLETE / CERTIFIED / CURRENT", current_state)
        self.assertIn("NEXT GOVERNANCE ACTION: NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION", current_state)
        self.assertIn("ARCHITECTURAL PROOF CLASSIFICATION: COMPLETE / FINALISED", current_state)
        self.assertIn("PROOF CLASSIFICATION: NEW_TRACER_BULLET", current_state)
        self.assertIn("DEVELOPMENT ENTRY HARD STOP: PASS / ALL 10 CONDITIONS SATISFIED", current_state)
        self.assertIn("PHASE 8: AUTHORISED (ARCHITECTURAL PROOF ONLY)", current_state)
        self.assertNotRegex(
            current_state,
            r"(?i)\bphase\s+7c\b[^\n.!?]{0,100}\b(?:remains|is|still|currently)\s+blocked\s*/\s*not\s+started\b",
            "the current README cannot give Phase 7C both NEXT and BLOCKED status",
        )

    def test_lifecycle_manifest_and_scope_are_current_and_unchanged(self):
        state = _lifecycle_state(
            (ROOT / self.entries["OPEN_WORK"]["repository_path"]).read_text(encoding="utf-8")
        )
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", state.get("phase_7b_reconciliation"))
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", state.get("phase_7c"))
        self.assertEqual("NEW_TRACER_BULLET PROOF CONTRACT / TASK DEFINITION", state.get("next_stage"))
        self.assertEqual("NEW_TRACER_BULLET", state.get("proof_classification"))
        self.assertEqual("AUTHORISED", state.get("application_implementation"))
        self.assertEqual("AUTHORISED", state.get("phase8"))
        self.assertEqual(
            "CERTIFIED / CURRENT",
            state.get("phase_7b_reconciliation_candidate", {}).get("lifecycle"),
        )
        certification = state.get("phase_7b_reconciliation_certification", {})
        self.assertEqual(PR_121_CANDIDATE_SHA, certification.get("candidate_head"))
        self.assertEqual(BASELINE_MAIN_SHA, certification.get("resulting_main"))
        self.assertEqual(MERGE_TREE_SHA, certification.get("candidate_resulting_main_tree"))
        self.assertEqual(POST_MERGE_ATTESTATION_URL, certification.get("post_merge_attestation_url"))
        self.assertEqual("PASS", certification.get("post_merge_independent_review"))
        phase7c_contract = state.get("phase_7c_final_feature_pack_contract", {})
        self.assertEqual("COMPLETE / CERTIFIED / CURRENT", phase7c_contract.get("lifecycle"))
        self.assertEqual("bb7bc67fd2d9aa49ed9a6e7f49f09fc5eba5d6a5", phase7c_contract.get("candidate_head_sha"))
        self.assertEqual("cfc63a7a77299cd59c98d88b57a88bb5b4ac29e5", phase7c_contract.get("merge_sha"))
        self.assertEqual("NEW_TRACER_BULLET", phase7c_contract.get("proof_classification"))
        self.assertEqual("AUTHORISED", phase7c_contract.get("phase8"))

        current_open_work = self.entries["OPEN_WORK"]
        self.assertEqual("02_OPEN_WORK_v1.2.74.md", current_open_work["canonical_filename"])
        self.assertEqual("1.2.74", current_open_work["semver"])
        self.assertEqual(
            "docs/00_platform/02_OPEN_WORK_v1.2.74.md",
            current_open_work["repository_path"],
        )
        self.assertEqual("1.2.73", current_open_work["superseded_version"])
        self.assertEqual("current", current_open_work["lifecycle"])

        immediate_predecessor = self.entries.get("OPEN_WORK_V1_2_73", {})
        self.assertEqual("02_OPEN_WORK_v1.2.73.md", immediate_predecessor.get("canonical_filename"))
        self.assertEqual("1.2.73", immediate_predecessor.get("semver"))
        self.assertEqual("docs/00_platform/archive/02_OPEN_WORK_v1.2.73.md", immediate_predecessor.get("repository_path"))
        self.assertEqual("1.2.72", immediate_predecessor.get("superseded_version"))
        self.assertEqual("historical", immediate_predecessor.get("lifecycle"))

        direct_predecessor = self.entries.get("OPEN_WORK_V1_2_69", {})
        self.assertEqual("02_OPEN_WORK_v1.2.69.md", direct_predecessor.get("canonical_filename"))
        self.assertEqual("1.2.69", direct_predecessor.get("semver"))
        self.assertEqual(
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.69.md",
            direct_predecessor.get("repository_path"),
        )
        self.assertEqual("1.2.70", direct_predecessor.get("superseded_version"))
        self.assertEqual("historical", direct_predecessor.get("lifecycle"))
        self.assertEqual("fea721b924defc93365b17fbe67086c4a8681061896bc6ea15fbaf29917c1c0f", direct_predecessor.get("sha256"))
        self.assertEqual(direct_predecessor.get("sha256"), direct_predecessor.get("provenance_sha256"))

        predecessor = self.entries.get("OPEN_WORK_V1_2_66", {})
        self.assertEqual("02_OPEN_WORK_v1.2.66.md", predecessor.get("canonical_filename"))
        self.assertEqual("1.2.66", predecessor.get("semver"))
        self.assertEqual(
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.66.md",
            predecessor.get("repository_path"),
        )
        self.assertEqual("PLANNING_TRACKER_HISTORICAL", predecessor.get("authority_class"))
        self.assertEqual("1.2.67", predecessor.get("superseded_version"))
        self.assertEqual("historical", predecessor.get("lifecycle"))
        self.assertEqual(predecessor.get("sha256"), predecessor.get("provenance_sha256"))
        self.assertEqual(
            "96a61dd94098f3c9fbb4ba1a6c683e9a3484b62ee15306d8dd5d884ad84f2133",
            predecessor.get("sha256"),
        )

        candidate = self.candidate_rules
        self.assertEqual(
            [
                "Identity & Access",
                "Privacy & Consent",
                "Content & Media",
                "Communications",
                "Audit & Evidence",
                "Analytics",
            ],
            candidate["six_affected_domains"],
        )
        self.assertEqual(
            ["CAP-001", "CAP-002", "CAP-003", "CAP-005", "CAP-006", "CAP-017", "CAP-028"],
            candidate["seven_material_capabilities"],
        )
        for domain, status in candidate["required_dossiers"].items():
            self.assertIn(domain, self.current_text)
            self.assertIn(status, self.current_text)
        for domain in ("Privacy & Consent", "Content & Media", "Analytics"):
            self.assertEqual("NOT_REQUIRED", candidate["required_dossiers"][domain])

    def test_all_direct_predecessor_archives_match_the_baseline_bytes(self):
        configured = self.integrity_rules.get(
            "fp001_phase7b_reconciliation_certification_archives", {}
        )
        expected = {ARCHIVED_CANDIDATE: ARCHIVED_CANDIDATE_SHA256}
        expected.update(
            {archive: details[1] for archive, details in ARCHIVE_PREDECESSORS.items()}
        )
        self.assertEqual(expected, configured)
        for archive, (source, expected_hash) in ARCHIVE_PREDECESSORS.items():
            with self.subTest(archive=archive):
                archive_bytes = (ROOT / archive).read_bytes()
                self.assertEqual(expected_hash, hashlib.sha256(archive_bytes).hexdigest())
                self.assertEqual(archive_bytes, _git_show(BASELINE_MAIN_SHA, source))

    def test_foundation_integrity_rejects_unarchived_predecessors_and_allows_archives(self):
        names = [
            "02_OPEN_WORK_v1.2.70.md",
            "DELIVERY_ATLAS_WORKING_v0.4.12.md",
            "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.14.md",
            "HARDEN-02_CONTRACT_WORKING_v0.5.14.md",
        ]
        readme_path = DOCS / "README.md"
        original_readme = readme_path.read_text(encoding="utf-8")
        current_start = original_readme.index("## Current State")
        current_end = original_readme.find("\n## ", current_start + 1)
        current_end = current_end if current_end >= 0 else len(original_readme)
        current = original_readme[current_start:current_end]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(DOCS, fixture_docs)
            fixture_readme = fixture_docs / "README.md"
            fixture_readme.write_text(
                original_readme[:current_end]
                + "\nUnarchived routes: " + ", ".join(names) + "\n"
                + original_readme[current_end:],
                encoding="utf-8",
            )
            rejected = run_audit(root, fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
            route_check = next(item for item in rejected["checks"] if item["name"] == "fp001_phase7c_final_contract_current_promotion")
            self.assertEqual("FAIL", route_check["status"], route_check["message"])
            for name in names:
                self.assertIn(name, route_check["message"])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(DOCS, fixture_docs)
            fixture_readme = fixture_docs / "README.md"
            fixture_readme.write_text(
                original_readme[:current_end]
                + "\nHistorical archives: " + ", ".join(f"archive/{name}" for name in names) + "\n"
                + original_readme[current_end:],
                encoding="utf-8",
            )
            accepted = run_audit(root, fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
            route_check = next(item for item in accepted["checks"] if item["name"] == "fp001_phase7c_final_contract_current_promotion")
            self.assertEqual("PASS", route_check["status"], route_check["message"])

    def test_successor_does_not_change_upstream_authority_or_application_source(self):
        tracked_changed = subprocess.run(
            ["git", "diff", "--name-only", BASELINE_MAIN_SHA],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        untracked = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        changed = sorted(set(tracked_changed + untracked))
        protected = (
            "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_",
            "docs/00_platform/00_PLATFORM_",
            "docs/00_platform/01_DECISIONS_",
            "docs/00_platform/03_ARCHITECTURE_",
            "docs/00_platform/04_DOMAIN_MAP_",
            "app/",
            "assets/",
            "lib/",
            "src/",
            "web/",
        )
        self.assertFalse(
            [path for path in changed if path.startswith(protected)],
            changed,
        )


if __name__ == "__main__":
    unittest.main()
