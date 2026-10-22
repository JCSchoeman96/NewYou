from __future__ import annotations

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path


from tests.foundation_test_support import git_changed_paths

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
STARTING_MAIN = "332d51f19d77430fe4e95911920fe0c87cab524a"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"


def read_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def current_open_work() -> str:
    manifest = read_manifest()
    entry = next(item for item in manifest["governing_documents"] if item["document_id"] == "OPEN_WORK")
    return (ROOT / entry["repository_path"]).read_text(encoding="utf-8")


def git_show(path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{STARTING_MAIN}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


class FP001ConditionalDossierAdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skeleton = git_show("docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.6.md").decode("utf-8")
        cls.open_work = git_show("docs/00_platform/02_OPEN_WORK_v1.2.62.md").decode("utf-8")
        cls.readme = git_show("docs/00_platform/README.md").decode("utf-8")
        cls.domain_map = (DOCS / "04_DOMAIN_MAP_v1.2.0.md").read_text(encoding="utf-8")
        cls.roadmap = (DOCS / "05_ROADMAP_v1.2.3.md").read_text(encoding="utf-8")

    def test_exactly_the_three_conditional_dossiers_have_terminal_dispositions(self) -> None:
        table = self.skeleton.split("## 7. Domain participation", 1)[1].split("## 8.", 1)[0]
        rows = {
            cells[0]: cells
            for line in table.splitlines()
            if line.startswith("|")
            for cells in [[cell.strip().strip("`") for cell in line.strip("|").split("|")]]
            if len(cells) >= 5 and cells[0] not in {"Domain", "---"}
        }
        expected = {
            "Privacy & Consent": "NOT_REQUIRED",
            "Content & Media": "NOT_REQUIRED",
            "Audit & Evidence": "REQUIRED",
        }
        self.assertEqual(expected.keys(), rows.keys() & expected.keys())
        for domain, disposition in expected.items():
            self.assertEqual(disposition, rows[domain][3])
            self.assertEqual(1, len(re.findall(rf"(?m)^\| {re.escape(domain)} \|", table)))
        self.assertNotIn("CONDITIONAL / PENDING EXPLICIT ADJUDICATION", table)
        for document in (self.skeleton, self.open_work, self.readme):
            self.assertIn("Privacy & Consent", document)
            self.assertIn("Content & Media", document)
            self.assertIn("Audit & Evidence", document)

    def test_required_dossiers_analytics_and_current_routes_agree(self) -> None:
        expected_routes = (
            "IDENTITY & ACCESS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4",
            "COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "PRIVACY & CONSENT: NOT_REQUIRED",
            "CONTENT & MEDIA: NOT_REQUIRED",
            "AUDIT & EVIDENCE: REQUIRED / NEXT / NOT_STARTED",
            "ANALYTICS: NOT_REQUIRED",
        )
        for route in expected_routes:
            self.assertIn(route, self.open_work)
        for status in (
            "| Identity & Access | `PRIMARY` | `YES` | `REQUIRED` |",
            "| Communications | `SUPPORTING` | `YES` | `REQUIRED` |",
            "| Privacy & Consent | `SUPPORTING` | `YES` | `NOT_REQUIRED` |",
            "| Content & Media | `SUPPORTING` | `YES` | `NOT_REQUIRED` |",
            "| Audit & Evidence | `SUPPORTING` | `YES` | `REQUIRED` |",
            "| Analytics | `CONSUMER` | `NO` | `NOT_REQUIRED` |",
        ):
            self.assertIn(status, self.skeleton)
        for status in (
            "- IDENTITY & ACCESS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.4",
            "- COMMUNICATIONS: REQUIRED / COMPLETE / CERTIFIED / CURRENT v0.1.0",
            "- PRIVACY & CONSENT: NOT_REQUIRED",
            "- CONTENT & MEDIA: NOT_REQUIRED",
            "- AUDIT & EVIDENCE: REQUIRED / NEXT / NOT_STARTED",
            "- ANALYTICS: NOT_REQUIRED",
        ):
            self.assertIn(status, self.open_work)
        for status in (
            "- PRIVACY & CONSENT DOSSIER: NOT_REQUIRED",
            "- CONTENT & MEDIA DOSSIER: NOT_REQUIRED",
            "- AUDIT & EVIDENCE DOSSIER: REQUIRED / NEXT / NOT_STARTED",
            "- ANALYTICS DOSSIER: NOT_REQUIRED",
        ):
            self.assertIn(status, self.readme)
        self.assertIn("Identity & Access dossier v0.1.4 and Communications dossier v0.1.0 remain `REQUIRED / COMPLETE / CERTIFIED / CURRENT`", self.skeleton)

    def test_required_audit_dossier_keeps_phase_7c_blocked(self) -> None:
        block = "Audit & Evidence dossier must be COMPLETE / CERTIFIED / CURRENT and subsequent Phase 7B reconciliation must succeed"
        self.assertIn("NEXT STAGE: FP-001 AUDIT & EVIDENCE JIT DOMAIN DOSSIER", self.open_work)
        self.assertIn("PHASE 7C: BLOCKED / NOT_STARTED UNTIL AUDIT DOSSIER COMPLETE / CERTIFIED / CURRENT AND PHASE 7B RECONCILIATION SUCCEEDS", self.open_work)
        self.assertIn("Phase 7C remains `BLOCKED / NOT_STARTED` until the Audit dossier is complete, certified/current, and subsequent Phase 7B reconciliation succeeds", self.skeleton)
        self.assertIn(block, self.open_work)
        self.assertIn("The proof is not complete and classification is not finalised", self.skeleton)
        self.assertIn("PROOF CLASSIFICATION: NOT FINALISED", self.open_work)
        self.assertIn("This skeleton does not authorise or perform Phase 7B, Phase 7C, proof execution or implementation", self.skeleton)
        self.assertIn('"application_implementation": "UNAUTHORISED / BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS"', self.open_work)

    def test_not_required_domains_remain_in_the_approved_scope_and_keep_ownership(self) -> None:
        affected = {
            "Identity & Access",
            "Privacy & Consent",
            "Content & Media",
            "Communications",
            "Audit & Evidence",
            "Analytics",
        }
        table = self.skeleton.split("## 7. Domain participation", 1)[1].split("## 8.", 1)[0]
        rows = [line for line in table.splitlines() if line.startswith("| ") and " | `" in line]
        self.assertEqual(6, len(rows))
        for domain in affected:
            self.assertEqual(1, sum(domain in line for line in rows))
        self.assertNotIn("| Commerce |", table)
        privacy_section = self.domain_map.split("### 6.2 — Privacy & Consent", 1)[1].split("### 6.3", 1)[0]
        content_section = self.domain_map.split("### 6.7 — Content & Media", 1)[1].split("### 6.8", 1)[0]
        self.assertIn("Own purpose-specific consent", privacy_section)
        self.assertIn("purpose-specific consent/lawful-basis grants, withdrawals and current consent state", privacy_section)
        self.assertIn("Own governed runtime content, translations, taxonomy, publication", content_section)
        self.assertIn("| Purpose-specific consent/current consent, including marketing-purpose permission | **Privacy & Consent**", self.domain_map)
        self.assertIn("| Governed content/translation/publication version | **Content & Media**", self.domain_map)
        self.assertIn("Content & Media owns content versions, locale branches, approval and publication", self.skeleton)
        self.assertIn("Audit & Evidence owns restricted append-only evidence; source Domains retain business truth", self.skeleton)
        self.assertIn("never owns identity, consent, communications or another source Domain's truth", self.skeleton)
        self.assertIn("retention-category dependencies", self.skeleton)
        self.assertNotRegex(self.skeleton, r"(?i)retention period\s*(?:is|=|:)\s*\d+")

    def test_capability_scope_domain_count_and_pack_count_are_unchanged(self) -> None:
        expected_caps = {"CAP-001", "CAP-002", "CAP-003", "CAP-005", "CAP-006", "CAP-017", "CAP-028"}
        table = self.skeleton.split("## 6. Material capability input", 1)[1].split("## 7.", 1)[0]
        capability_ids = {
            match.group(1)
            for line in table.splitlines()
            if line.startswith("| `CAP-")
            for match in [re.match(r"\| `(CAP-\d{3})` \|", line)]
            if match is not None
        }
        self.assertEqual(expected_caps, capability_ids)
        self.assertEqual(20, len(re.findall(r"(?m)^\| \d+ \| \*\*[^|]+\*\* \|", self.domain_map)))
        self.assertEqual(17, len(re.findall(r"(?m)^## FP-\d{3} —", self.roadmap)))
        self.assertIn("Commerce is deliberately absent", self.skeleton)
        self.assertIn("| Analytics | `CONSUMER` | `NO` | `NOT_REQUIRED` |", self.skeleton)

    def test_predecessors_are_archived_byte_identically_and_pinned(self) -> None:
        predecessors = {
            "docs/00_platform/archive/02_OPEN_WORK_v1.2.61.md": DOCS / "archive/02_OPEN_WORK_v1.2.61.md",
            "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.4.3.md": DOCS / "archive/DELIVERY_ATLAS_WORKING_v0.4.3.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md": DOCS / "archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.5.md",
            "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.5.md": DOCS / "archive/HARDEN-02_CONTRACT_WORKING_v0.5.5.md",
        }
        manifest = read_manifest()
        pins = manifest["integrity_rules"]["fp001_conditional_dossier_predecessor_archives"]
        for source_path, archive in predecessors.items():
            archived_bytes = archive.read_bytes()
            self.assertEqual(git_show(source_path), archived_bytes, source_path)
            self.assertEqual(hashlib.sha256(archived_bytes).hexdigest(), pins[str(archive.relative_to(ROOT))])

    def test_upstream_semantic_authorities_are_unchanged_from_starting_main(self) -> None:
        authority_paths = (
            "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
            "docs/00_platform/00_PLATFORM_v1.8.0.md",
            "docs/00_platform/01_DECISIONS_v1.8.0.md",
            "docs/00_platform/03_ARCHITECTURE_v1.1.1.md",
            "docs/00_platform/04_DOMAIN_MAP_v1.2.0.md",
        )
        for path in authority_paths:
            self.assertEqual(git_show(path), (ROOT / path).read_bytes(), path)
        roadmap_predecessor = DOCS / "archive/05_ROADMAP_v1.2.2.md"
        self.assertEqual(
            git_show("docs/00_platform/05_ROADMAP_v1.2.2.md"),
            roadmap_predecessor.read_bytes(),
        )

    def test_only_authorized_audit_candidate_and_no_implementation_artifacts_were_introduced(self) -> None:
        # This cumulative scope includes the authorised Audit candidate and its
        # PR #119 promotion, whose resulting main is the pinned Phase 7B base.
        paths = git_changed_paths(ROOT, STARTING_MAIN, "5d282ecca4e13b621c7f96c05c47d6fac43ec1bd")
        allowed = lambda path: (
            path.startswith("docs/00_platform/")
            or path == "tools/foundation_integrity_audit.py"
            or path in {
                "tools/foundation_integrity_routing.py",
                "tools/foundation_integrity_smoke.py",
                "docs/development/foundation-integrity-ci.md",
                "docs/development/github-branch-governance.md",
            }
            or path.startswith("tests/")
            or path == ".github/workflows/foundation-integrity.yml"
        )
        self.assertTrue(all(allowed(path) for path in paths), paths)
        audit_dossiers = [
            path for path in paths
            if "JIT_DOMAIN_DOSSIER" in path and "AUDIT" in path.upper()
        ]
        self.assertEqual(
            [
                "docs/00_platform/archive/"
                "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
                "docs/00_platform/working/"
                "FP-001_AUDIT_EVIDENCE_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            ],
            audit_dossiers,
        )
        self.assertFalse(
            any(
                "JIT_DOMAIN_DOSSIER" in path
                and any(domain in path.upper() for domain in ("PRIVACY", "CONTENT"))
                for path in paths
            )
        )
        self.assertFalse(any(path.startswith(("lib/", "config/", "priv/", "test/", "resources/", "services/", "jobs/", "routes/", "schema/", "migrations/")) for path in paths))


if __name__ == "__main__":
    unittest.main()
