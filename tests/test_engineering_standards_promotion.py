from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from typing import Callable

from tools.foundation_integrity_audit import run_audit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_RELATIVE = Path("docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json")
CURRENT_STANDARDS_RELATIVE = Path("docs/00_platform/reference/ENGINEERING_STANDARDS_v1.0.1.md")
ARCHIVED_CANDIDATE_RELATIVE = Path("docs/00_platform/archive/ENGINEERING_STANDARDS_v1.0.0.md")
OPEN_WORK_RELATIVE = Path("docs/00_platform/02_OPEN_WORK_v1.2.54.md")
README_RELATIVE = Path("docs/00_platform/README.md")


Mutation = Callable[[Path, dict], None]


def _entry(manifest: dict, document_id: str) -> dict:
    for section in ("governing_documents", "reference_documents", "historical_documents"):
        for item in manifest.get(section, []):
            if item.get("document_id") == document_id:
                return item
    raise AssertionError(f"missing manifest entry {document_id}")


def _refresh_manifest_hash(root: Path, manifest: dict, document_id: str) -> None:
    entry = _entry(manifest, document_id)
    digest = hashlib.sha256((root / entry["repository_path"]).read_bytes()).hexdigest()
    entry["sha256"] = digest
    if "provenance_sha256" in entry:
        entry["provenance_sha256"] = digest


def _rewrite(path: Path, before: str, after: str) -> None:
    text = path.read_text(encoding="utf-8")
    if before not in text:
        raise AssertionError(f"mutation marker not found in {path}: {before}")
    path.write_text(text.replace(before, after, 1), encoding="utf-8")


def _rewrite_open_work(root: Path, before: str, after: str) -> None:
    path = root / OPEN_WORK_RELATIVE
    text = path.read_text(encoding="utf-8")
    start = text.find("# 9. Immediate Next Action")
    end = text.find("# 10. Minimal Tools", start + 1)
    if start < 0 or end < 0:
        raise AssertionError("Open Work current-state section is missing")
    active = text[start:end]
    if before not in active:
        raise AssertionError(f"mutation marker not found in current Open Work section: {before}")
    text = text[:start] + active.replace(before, after, 1) + text[end:]
    path.write_text(text, encoding="utf-8")


class EngineeringStandardsPromotionAuditMutationTests(unittest.TestCase):
    def test_candidate_and_certified_normative_body_are_identical(self):
        current = (ROOT / CURRENT_STANDARDS_RELATIVE).read_text(encoding="utf-8")
        archived = (ROOT / ARCHIVED_CANDIDATE_RELATIVE).read_text(encoding="utf-8")
        start_marker = "## Risk classification\n"
        end_marker = "## Deferred choices and closed alternatives\n"
        current_body = current.split(start_marker, 1)[1].split(end_marker, 1)[0]
        archived_body = archived.split(start_marker, 1)[1].split(end_marker, 1)[0]
        self.assertEqual(archived_body, current_body)

    def _mutations(self) -> list[tuple[str, Mutation]]:
        def manifest_still_candidate(root: Path, manifest: dict) -> None:
            _entry(manifest, "ENGINEERING_STANDARDS")["lifecycle"] = "candidate"

        def document_still_not_certified(root: Path, manifest: dict) -> None:
            path = root / CURRENT_STANDARDS_RELATIVE
            _rewrite(path, "- **Status:** CERTIFIED / CURRENT", "- **Status:** PROMOTION CANDIDATE / NOT CERTIFIED")
            _refresh_manifest_hash(root, manifest, "ENGINEERING_STANDARDS")

        def missing_pr65_evidence(root: Path, manifest: dict) -> None:
            path = root / CURRENT_STANDARDS_RELATIVE
            _rewrite(path, "Fresh independent post-merge review | PASS", "Fresh independent post-merge review | PENDING")
            _refresh_manifest_hash(root, manifest, "ENGINEERING_STANDARDS")

        def altered_normative_body(root: Path, manifest: dict) -> None:
            path = root / CURRENT_STANDARDS_RELATIVE
            _rewrite(path, "- `LOW`\n- `STANDARD`\n- `HIGH`", "- `LOW`\n- `HIGH`")
            _refresh_manifest_hash(root, manifest, "ENGINEERING_STANDARDS")

        def wrong_stage4b_source(root: Path, manifest: dict) -> None:
            path = root / CURRENT_STANDARDS_RELATIVE
            _rewrite(
                path,
                "27bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017",
                "00bc75f1e17ca88922005374cc6643e0896ec40d477b87ac8b5e6b3c08ba2017",
            )
            _refresh_manifest_hash(root, manifest, "ENGINEERING_STANDARDS")

        def wrong_stage4b_source_route(root: Path, manifest: dict) -> None:
            path = root / CURRENT_STANDARDS_RELATIVE
            _rewrite(
                path,
                "working/TARGETED_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md",
                "working/OTHER_ENGINEERING_POLICY_GRILL_WORKING_v0.1.0.md",
            )
            _refresh_manifest_hash(root, manifest, "ENGINEERING_STANDARDS")

        def standards_still_routes_its_own_promotion(root: Path, manifest: dict) -> None:
            path = root / CURRENT_STANDARDS_RELATIVE
            _rewrite(
                path,
                "CERTIFIED HARDEN-02 EXECUTION\n→ CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
                "CERTIFIED HARDEN-02 EXECUTION\n→ ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED\n→ CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
            )
            _refresh_manifest_hash(root, manifest, "ENGINEERING_STANDARDS")

        def duplicate_current_registration(root: Path, manifest: dict) -> None:
            duplicate = dict(_entry(manifest, "ENGINEERING_STANDARDS"))
            duplicate["document_id"] = "ENGINEERING_STANDARDS_DUPLICATE"
            manifest["reference_documents"].append(duplicate)

        def parallel_active_candidate(root: Path, manifest: dict) -> None:
            candidate = dict(_entry(manifest, "ENGINEERING_STANDARDS_CANDIDATE_V1_0_0"))
            candidate["lifecycle"] = "candidate"
            manifest["reference_documents"].append(candidate)

        def governing_root_registration(root: Path, manifest: dict) -> None:
            active = _entry(manifest, "ENGINEERING_STANDARDS")
            manifest["reference_documents"].remove(active)
            manifest["governing_documents"].append(active)

        def programme_still_says_promotion_next(root: Path, manifest: dict) -> None:
            _rewrite_open_work(
                root,
                "ENGINEERING STANDARDS AUTHORITY PROMOTION: COMPLETE / CERTIFIED",
                "ENGINEERING STANDARDS AUTHORITY PROMOTION: NEXT / AUTHORISED / NOT STARTED",
            )
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def current_open_work_status_section_still_says_promotion_next(root: Path, manifest: dict) -> None:
            path = root / OPEN_WORK_RELATIVE
            _rewrite(
                path,
                "Engineering Standards Authority Promotion is COMPLETE / CERTIFIED under `reference/ENGINEERING_STANDARDS_v1.0.1.md`",
                "Engineering Standards Authority Promotion is NEXT / AUTHORISED / NOT STARTED",
            )
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def historical_promotion_status_is_not_marked_historical(root: Path, manifest: dict) -> None:
            path = root / OPEN_WORK_RELATIVE
            _rewrite(
                path,
                "**Historical pre-PR #65 status as recorded in Open Work v1.2.53:**",
                "Pre-PR #65 status:",
            )
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def next_token_still_names_standards(root: Path, manifest: dict) -> None:
            _rewrite_open_work(root, "NEXT STAGE: FP001_RECONCILIATION_REQUIRED", "NEXT STAGE: ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED")
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def fp001_already_performed(root: Path, manifest: dict) -> None:
            _rewrite_open_work(
                root,
                "FP001_RECONCILIATION_REQUIRED: REQUIRED / NEXT / NOT PERFORMED",
                "FP001_RECONCILIATION_REQUIRED: COMPLETE / PERFORMED",
            )
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def communications_started(root: Path, manifest: dict) -> None:
            _rewrite_open_work(
                root,
                "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION",
                "COMMUNICATIONS: REQUIRED / STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION",
            )
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def phase_7c_unblocked(root: Path, manifest: dict) -> None:
            _rewrite_open_work(root, "PHASE 7C: BLOCKED / NOT_STARTED", "PHASE 7C: UNBLOCKED / NEXT")
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def proof_finalised(root: Path, manifest: dict) -> None:
            _rewrite_open_work(root, "PROOF CLASSIFICATION: NOT FINALISED", "PROOF CLASSIFICATION: FINALISED")
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def implementation_authorised(root: Path, manifest: dict) -> None:
            _rewrite_open_work(
                root,
                "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
                "EXECUTABLE DEVELOPMENT: AUTHORISED",
            )
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def store_cer_included(root: Path, manifest: dict) -> None:
            _rewrite_open_work(root, "STORE / CER: EXCLUDED FROM HARDEN-02", "STORE / CER: IN SCOPE")
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        def readme_candidate_only(root: Path, manifest: dict) -> None:
            path = root / README_RELATIVE
            _rewrite(path, "## Certified Engineering Standards supporting authority", "## Engineering Standards promotion candidate")
            _rewrite(path, "reference/ENGINEERING_STANDARDS_v1.0.1.md", "reference/ENGINEERING_STANDARDS_v1.0.0.md")

        def archive_provenance_missing(root: Path, manifest: dict) -> None:
            (root / ARCHIVED_CANDIDATE_RELATIVE).unlink()
            manifest["historical_documents"] = [
                item for item in manifest["historical_documents"]
                if item.get("document_id") != "ENGINEERING_STANDARDS_CANDIDATE_V1_0_0"
            ]

        def artifact_hash_mismatch(root: Path, manifest: dict) -> None:
            path = root / CURRENT_STANDARDS_RELATIVE
            path.write_bytes(path.read_bytes() + b"\n")

        def manifest_hash_mismatch(root: Path, manifest: dict) -> None:
            _entry(manifest, "ENGINEERING_STANDARDS")["sha256"] = "0" * 64

        def multiple_stages_advanced(root: Path, manifest: dict) -> None:
            _rewrite_open_work(
                root,
                "FP001_RECONCILIATION_REQUIRED: REQUIRED / NEXT / NOT PERFORMED",
                "FP001_RECONCILIATION_REQUIRED: COMPLETE / PERFORMED",
            )
            _rewrite_open_work(
                root,
                "COMMUNICATIONS: REQUIRED / NOT_STARTED / DOWNSTREAM AFTER FP-001 RECONCILIATION",
                "COMMUNICATIONS: CURRENT / NEXT",
            )
            _rewrite_open_work(root, "NEXT STAGE: FP001_RECONCILIATION_REQUIRED", "NEXT STAGE: COMMUNICATIONS")
            _refresh_manifest_hash(root, manifest, "OPEN_WORK")

        return [
            ("certified document with candidate manifest lifecycle", manifest_still_candidate),
            ("certified manifest with NOT CERTIFIED document", document_still_not_certified),
            ("missing PR #65 lifecycle evidence", missing_pr65_evidence),
            ("altered EP-Q normative body", altered_normative_body),
            ("different Stage 4B source hash", wrong_stage4b_source),
            ("different Stage 4B source route", wrong_stage4b_source_route),
            ("certified Standards still routes its own promotion as NEXT", standards_still_routes_its_own_promotion),
            ("multiple current Standards registrations", duplicate_current_registration),
            ("parallel active candidate and certified authority", parallel_active_candidate),
            ("certified Standards registered as governing authority", governing_root_registration),
            ("programme still says Standards promotion is NEXT", programme_still_says_promotion_next),
            ("current Open Work status section still says Standards promotion is NEXT", current_open_work_status_section_still_says_promotion_next),
            ("superseded pre-PR #65 promotion status is not marked historical", historical_promotion_status_is_not_marked_historical),
            ("NEXT token remains Standards promotion", next_token_still_names_standards),
            ("FP-001 reconciliation already performed", fp001_already_performed),
            ("Communications started", communications_started),
            ("Phase 7C unblocked", phase_7c_unblocked),
            ("proof classification finalised", proof_finalised),
            ("Phase 8 implementation authorised", implementation_authorised),
            ("Store/CER included", store_cer_included),
            ("stale candidate-only README route", readme_candidate_only),
            ("missing candidate archive and provenance registration", archive_provenance_missing),
            ("artifact hash mismatch", artifact_hash_mismatch),
            ("manifest hash mismatch", manifest_hash_mismatch),
            ("successor advances more than one programme stage", multiple_stages_advanced),
        ]

    def test_fail_closed_mutations_use_production_run_audit(self):
        for label, mutate in self._mutations():
            with self.subTest(mutation=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                shutil.copytree(ROOT / "docs", root / "docs")
                manifest_path = root / MANIFEST_RELATIVE
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                mutate(root, manifest)
                manifest_path.write_text(
                    json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )

                report = run_audit(root, manifest_path)

                self.assertEqual("FAIL", report["status"], report.get("findings"))
                self.assertGreater(report["assertion_count"], 0)


if __name__ == "__main__":
    unittest.main()
