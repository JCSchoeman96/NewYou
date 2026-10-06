from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.foundation_integrity_audit import _h02_lifecycle_state, refresh_manifest, run_audit


SMALL_COUNTS = {
    "decisions": 1,
    "open_questions": 1,
    "architecture_law": 1,
    "architecture_requirements": 1,
    "reference_flows": 1,
    "domains": 1,
    "ownership_rows": 1,
    "feature_packs": 0,
}

FAD72C1_FROZEN_HASHES = {
    "docs/00_platform/archive/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/archive/00_PLATFORM_v1.2.1.md": "56a2b9a5db42a81e287f0c61deae37d6bbce5b19f48f67732584160b455f935a",
    "docs/00_platform/archive/03_ARCHITECTURE_v1.0.0.md": "87dd7d21714d751069bdbe72547c3500fbcbc8ccd747c003faf350fa953c9d4b",
    "docs/00_platform/archive/04_DOMAIN_MAP_v1.0.0.md": "f31223f7159732d368667145522704bb7c584316af540fb1e5e048ddbc26e70a",
    "docs/00_platform/archive/05_ROADMAP_v1.0.0.md": "b883c7ae3afeebe969930bd8a5690bfae81429de53145e79233ebce59f172e20",
    "docs/00_platform/archive/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "cdf09ecced658635572a20e4f2feb04120b4f856e81762ef5af9ba179a11c40e",
    "docs/00_platform/archive/ARCHITECTURE_LAW_WORKING_v0.35.0.md": "a853f3fc117f2fc4d6d0071658c4fd97edc487c5e6cdffb068f355c190264639",
    "docs/00_platform/archive/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "f93c18ac442b33cf9197d6fbf0aabe6b7fd0cc4a67ceac35ab15edd6c6718c20",
}

IDENTITY_LIFECYCLE_START = "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_START -->"
IDENTITY_LIFECYCLE_END = "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_END -->"
IDENTITY_LIFECYCLE_STATE = {
    "artifact_version": "v0.1.4",
    "identity_lifecycle": "CERTIFIED / CURRENT",
    "pr_76_candidate_certification": "COMPLETE",
    "pr_76_post_merge_certification_evidence": "COMPLETE",
    "current_status_promotion": "PR #77 STATUS SUCCESSOR",
    "communications": "REQUIRED / NEXT / NOT_STARTED",
    "communications_finalisation": "BLOCKED / STOP",
    "phase_7c": "BLOCKED / NOT_STARTED",
    "proof_classification": "NOT FINALISED",
    "phase_8_application_implementation": "UNAUTHORISED",
}


class FoundationIntegrityAuditTests(unittest.TestCase):
    def _ensure_identity_lifecycle_block(self, dossier_path: Path) -> str:
        dossier = dossier_path.read_text(encoding="utf-8")
        if IDENTITY_LIFECYCLE_START in dossier or IDENTITY_LIFECYCLE_END in dossier:
            return dossier
        status_start = dossier.index("**Status:**")
        status_end = dossier.index("\n", status_start)
        block = (
            f"{IDENTITY_LIFECYCLE_START}\n"
            "This structured block is the machine-authoritative lifecycle projection for this artifact. "
            "Historical narrative and explanatory prose do not independently redefine current lifecycle state.\n"
            "```json\n"
            f"{json.dumps(IDENTITY_LIFECYCLE_STATE, indent=2)}\n"
            "```\n"
            f"{IDENTITY_LIFECYCLE_END}\n"
        )
        return dossier[: status_end + 1] + "\n" + block + dossier[status_end + 1 :]

    def _rewrite_identity_lifecycle_payload(self, dossier: str, mutate) -> str:
        start = dossier.index(IDENTITY_LIFECYCLE_START)
        payload_start = dossier.index("```json\n", start) + len("```json\n")
        payload_end = dossier.index("\n```", payload_start)
        payload = json.loads(dossier[payload_start:payload_end])
        mutate(payload)
        return dossier[:payload_start] + json.dumps(payload, indent=2) + dossier[payload_end:]

    def test_clean_fixture_returns_pass_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertEqual([], report["findings"])

    def test_pending_post_merge_lifecycle_state_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            open_work_entry = next(
                entry for entry in manifest["governing_documents"]
                if entry["document_id"] == "OPEN_WORK"
            )
            open_work_path = root / open_work_entry["repository_path"]
            open_work = open_work_path.read_text(encoding="utf-8")
            replacements = (
                (
                    "| POST_MERGE_INDEPENDENT_REVIEW | PASS |",
                    "| POST_MERGE_INDEPENDENT_REVIEW | PENDING |",
                ),
                (
                    "| POST_MERGE_ATTESTATION | COMPLETE |",
                    "| POST_MERGE_ATTESTATION | PENDING |",
                ),
                (
                    "| EXECUTION | COMPLETE_CERTIFIED |",
                    "| EXECUTION | IN_PROGRESS_NOT_COMPLETE_CERTIFICATION_PENDING |",
                ),
            )
            for current, stale in replacements:
                self.assertEqual(1, open_work.count(current), current)
                open_work = open_work.replace(current, stale)
            open_work_path.write_text(open_work, encoding="utf-8")

            readme_path = fixture_docs / "README.md"
            readme = readme_path.read_text(encoding="utf-8")
            for current, stale in (
                ("CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION", "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING"),
                ("NEXT STAGE: COMMUNICATIONS JIT DOMAIN DOSSIER", "NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED"),
                (
                    "HARDEN-02 EXECUTION: COMPLETE / CERTIFIED",
                    "HARDEN-02 EXECUTION: IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
                ),
            ):
                self.assertEqual(1, readme.count(current), current)
                readme = readme.replace(current, stale)
            readme_path.write_text(readme, encoding="utf-8")

            refresh_manifest(root, manifest_path)
            report = run_audit(root, manifest_path)
            lifecycle_check = next(
                check for check in report["checks"]
                if check["name"] == "harden_02_lifecycle_state"
            )

            self.assertEqual("FAIL", lifecycle_check["status"])

    def test_fp001_pmr_certified_successors_pass_production_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))

            report = run_audit(root, manifest_path)

            check = next(
                check for check in report["checks"] if check["name"] == "fp001_pmr_reconciliation"
            )
            self.assertEqual("PASS", check["status"], check["message"])

    def test_fp001_identity_v013_archives_and_durable_delivery_section_are_preserved(self):
        tick = chr(96)
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        active = source_docs / "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
        old_active = source_docs / "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
        predecessor = source_docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md"
        candidate = source_docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
        snapshot = source_docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
        stale_candidate = source_docs / "working/candidates/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"

        self.assertTrue(active.is_file(), "certified v0.1.4 must be the active Identity dossier")
        self.assertFalse(old_active.exists(), "the superseded v0.1.3 file must no longer be an active route")
        self.assertTrue(predecessor.is_file(), "v0.1.2 must be preserved in the archive")
        self.assertTrue(candidate.is_file(), "the exact PR #70 candidate must be preserved in the archive")
        self.assertTrue(snapshot.is_file(), "the promoted/current v0.1.3 snapshot must be separately preserved")
        self.assertFalse(stale_candidate.exists(), "the promoted candidate path must be retired")
        self.assertEqual(
            "28dfe34dce0e9c48c737f666b112aeb89ccf45c0dfa10d2cfb81877def2538db",
            hashlib.sha256(predecessor.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            "52fe67fcf6335bc0f2675c772a15a5ccdf75150f2ac4d92c98d61a9c48369285",
            hashlib.sha256(candidate.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            "a88f993d92ea9ff0dc5652c284ccf4e2c17f4bb16b31759fb3417044d7f8e254",
            hashlib.sha256(snapshot.read_bytes()).hexdigest(),
        )
        self.assertNotEqual(candidate.read_bytes(), snapshot.read_bytes())
        active_text = active.read_text(encoding="utf-8")
        candidate_text = candidate.read_text(encoding="utf-8")
        snapshot_text = snapshot.read_text(encoding="utf-8")
        self.assertIn("**Status:** " + tick + "CERTIFIED / CURRENT" + tick, active_text)
        section = "### J.1 Narrow Identity/Communications durable-delivery correction"
        next_heading = "### J.1a Automated retrieval / scanner-safe proof consumption"
        end_heading = "### J.2 Technical evidence and certification boundary"
        active_j1 = active_text.split(section, 1)[1].split(next_heading, 1)[0]
        candidate_j1 = candidate_text.split(section, 1)[1].split(end_heading, 1)[0]
        snapshot_j1 = snapshot_text.split(section, 1)[1].split(end_heading, 1)[0]
        self.assertEqual(candidate_j1, snapshot_j1, "v0.1.3 candidate and promoted snapshot must retain distinct files but same J.1")
        self.assertEqual(candidate_j1, active_j1, "v0.1.4 must preserve the certified J.1 section byte-for-byte")

    def test_fp001_identity_v014_promotion_is_current_and_pins_distinct_same_version_archives(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("PASS", promotion_check["status"], promotion_check["message"])

            docs = root / "docs/00_platform"
            active = docs / "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            pr70_candidate = docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            superseded_v013_current = docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
            pr76_candidate = docs / "archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            stale_candidate = docs / "working/candidates/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"

            self.assertTrue(active.is_file())
            self.assertFalse(stale_candidate.exists())
            self.assertEqual("CERTIFIED / CURRENT", active.read_text(encoding="utf-8").split("**Status:** `", 1)[1].split("`", 1)[0])
            self.assertEqual(
                "52fe67fcf6335bc0f2675c772a15a5ccdf75150f2ac4d92c98d61a9c48369285",
                hashlib.sha256(pr70_candidate.read_bytes()).hexdigest(),
            )
            self.assertEqual(
                "a88f993d92ea9ff0dc5652c284ccf4e2c17f4bb16b31759fb3417044d7f8e254",
                hashlib.sha256(superseded_v013_current.read_bytes()).hexdigest(),
            )
            self.assertEqual(
                "1557a4bded20b94fc363d96dd5a601213de105e0daccfa1970b869a0e38f362f",
                hashlib.sha256(pr76_candidate.read_bytes()).hexdigest(),
            )
            self.assertNotEqual(pr70_candidate.read_bytes(), superseded_v013_current.read_bytes())

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            pinned_archives = manifest["integrity_rules"]["identity_v014_promotion_archives"]
            self.assertEqual(
                {
                    "docs/00_platform/archive/02_OPEN_WORK_v1.2.56.md",
                    "docs/00_platform/archive/DELIVERY_ATLAS_WORKING_v0.3.8.md",
                    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.5.0.md",
                    "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md",
                    "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
                },
                set(pinned_archives),
            )

    def test_fp001_identity_v014_structured_lifecycle_rejects_invalid_state_and_mirrors(self):
        def remove_block(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start) + len(IDENTITY_LIFECYCLE_END)
            return dossier[:start] + dossier[end:]

        def duplicate_block(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start) + len(IDENTITY_LIFECYCLE_END)
            block = dossier[start:end]
            history = dossier.index("### Inherited v0.1.3 certification evidence")
            return dossier[:history] + block + "\n\n" + dossier[history:]

        def malformed_marker(dossier: str) -> str:
            return dossier.replace(IDENTITY_LIFECYCLE_START, "<!-- IDENTITY_V014_CURRENT_LIFECYCLE_STATE_BEGIN -->", 1)

        def relocate_block(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start) + len(IDENTITY_LIFECYCLE_END)
            block = dossier[start:end]
            remaining = dossier[:start] + dossier[end:]
            history = remaining.index("### Inherited v0.1.3 certification evidence")
            return remaining.replace(
                "### Inherited v0.1.3 certification evidence",
                "### Inherited v0.1.3 certification evidence\n\n" + block,
                1,
            )

        def reverse_markers(dossier: str) -> str:
            start = dossier.index(IDENTITY_LIFECYCLE_START)
            end = dossier.index(IDENTITY_LIFECYCLE_END, start)
            return (
                dossier[:start]
                + dossier[end : end + len(IDENTITY_LIFECYCLE_END)]
                + dossier[start + len(IDENTITY_LIFECYCLE_START) : end]
                + IDENTITY_LIFECYCLE_START
                + dossier[end + len(IDENTITY_LIFECYCLE_END) :]
            )

        def malformed_payload(dossier: str) -> str:
            return self._rewrite_identity_lifecycle_payload(dossier, lambda _payload: None).replace(
                '"artifact_version": "v0.1.4"',
                '"artifact_version": v0.1.4',
                1,
            )

        def duplicate_json_key(dossier: str) -> str:
            return dossier.replace(
                '"artifact_version": "v0.1.4",',
                '"artifact_version": "v0.1.4",\n  "artifact_version": "v0.1.4",',
                1,
            )

        def missing_field(dossier: str) -> str:
            return self._rewrite_identity_lifecycle_payload(
                dossier, lambda payload: payload.pop("communications_finalisation")
            )

        def wrong_payload(field: str, value: str):
            return lambda dossier: self._rewrite_identity_lifecycle_payload(
                dossier, lambda payload: payload.update({field: value})
            )

        def wrong_header_status(dossier: str) -> str:
            return dossier.replace(
                "**Status:** `CERTIFIED / CURRENT`",
                "**Status:** `NOT CURRENT`.",
                1,
            )

        def wrong_phase7c_mirror(dossier: str) -> str:
            return dossier.replace(
                "Identity v0.1.4 is `CERTIFIED / CURRENT`",
                "Identity v0.1.4 is `NOT CURRENT`",
                1,
            )

        def wrong_header_provenance(dossier: str) -> str:
            status_start = dossier.index("**Status:**")
            status_end = dossier.index("\n", status_start)
            status_line = dossier[status_start:status_end]
            if "current-status promotion is `PR #77 STATUS SUCCESSOR`" in status_line:
                changed = status_line.replace(
                    "PR #77 STATUS SUCCESSOR", "PR #76 CERTIFICATION/PROMOTION", 1
                )
            else:
                changed = status_line.replace(
                    "PR #76 certified and merged this v0.1.4 dossier unchanged.",
                    "PR #76 certified and merged this v0.1.4 dossier unchanged and made it current.",
                    1,
                )
            return dossier[:status_start] + changed + dossier[status_end:]

        def pr76_claims_phase7c_promotion(dossier: str) -> str:
            current_promotion = "* Current-status promotion is recorded by `PR #77 STATUS SUCCESSOR`."
            if current_promotion in dossier:
                return dossier.replace(
                    current_promotion,
                    "* Current-status promotion is recorded by `PR #76`;",
                    1,
                )
            communications = "* Communications remains `REQUIRED / NEXT / NOT_STARTED`;"
            self.assertEqual(1, dossier.count(communications))
            return dossier.replace(
                communications,
                "* Current-status promotion is recorded by `PR #76`;\n" + communications,
                1,
            )

        def remove_state_field(field: str):
            return lambda dossier: self._rewrite_identity_lifecycle_payload(
                dossier, lambda payload: payload.pop(field, None)
            )

        mutations = (
            ("missing block", remove_block),
            ("duplicate block", duplicate_block),
            ("malformed marker", malformed_marker),
            ("block outside current-state region", relocate_block),
            ("out-of-order markers", reverse_markers),
            ("malformed JSON", malformed_payload),
            ("duplicate JSON key", duplicate_json_key),
            ("missing required field", missing_field),
            ("wrong Identity lifecycle", wrong_payload("identity_lifecycle", "NOT CURRENT")),
            ("wrong dossier version", wrong_payload("artifact_version", "v0.1.3")),
            ("Communications advanced", wrong_payload("communications", "COMPLETE / FINALISED")),
            ("Phase 7C advanced", wrong_payload("phase_7c", "READY / STARTED")),
            ("proof classification finalised", wrong_payload("proof_classification", "FINALISED")),
            ("unexpected canonical JSON field", wrong_payload("unexpected_state", "UNEXPECTED")),
            (
                "PR #76 cannot collapse certification and promotion",
                wrong_payload("pr_76_certification_promotion", "COMPLETE"),
            ),
            ("PR #76 candidate certification missing", remove_state_field("pr_76_candidate_certification")),
            (
                "PR #76 candidate certification wrong",
                wrong_payload("pr_76_candidate_certification", "PENDING"),
            ),
            (
                "PR #76 post-merge certification evidence missing",
                remove_state_field("pr_76_post_merge_certification_evidence"),
            ),
            (
                "PR #76 post-merge certification evidence wrong",
                wrong_payload("pr_76_post_merge_certification_evidence", "PENDING"),
            ),
            (
                "current-status promotion source missing",
                remove_state_field("current_status_promotion"),
            ),
            (
                "current-status promotion source wrong",
                wrong_payload("current_status_promotion", "PR #76"),
            ),
            (
                "Phase 8 authorised",
                wrong_payload("phase_8_application_implementation", "AUTHORISED"),
            ),
            ("header Status conflicts", wrong_header_status),
            ("BLOCKS_PHASE7C mirror conflicts", wrong_phase7c_mirror),
            ("header Status provenance conflicts", wrong_header_provenance),
            ("BLOCKS_PHASE7C attributes promotion to PR #76", pr76_claims_phase7c_promotion),
        )
        for name, mutate in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                dossier_path = root / "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                dossier = self._ensure_identity_lifecycle_block(dossier_path)
                dossier_path.write_text(mutate(dossier), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("Identity current lifecycle", promotion_check["message"])

    def test_fp001_identity_v014_historical_candidate_certification_evidence_is_exempt(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            dossier_path = root / "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            dossier = self._ensure_identity_lifecycle_block(dossier_path)
            historical_heading = "### Inherited v0.1.3 certification evidence\n"
            historical_claim = (
                "Historical PR #76 evidence: the exact v0.1.4 candidate was not current and its "
                "certification was pending before promotion.\n\n"
            )
            self.assertEqual(1, dossier.count(historical_heading))
            dossier_path.write_text(
                dossier.replace(historical_heading, historical_heading + "\n" + historical_claim, 1),
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("PASS", promotion_check["status"], promotion_check["message"])

    def test_fp001_identity_v014_open_work_separates_pr76_certification_from_pr77_promotion(self):
        canonical_provenance = (
            "PR #76 certified the v0.1.4 candidate and supplied completed post-merge certification evidence. "
            "It did not make v0.1.4 current. This separate PR #77 status successor records the current-status "
            "promotion; the resulting Identity state is CERTIFIED / CURRENT."
        )
        collapsed_provenance = "PR #76 certification/promotion is COMPLETE / CERTIFIED / CURRENT."
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            open_work_path = root / "docs/00_platform/02_OPEN_WORK_v1.2.57.md"
            open_work = open_work_path.read_text(encoding="utf-8")
            section_start = open_work.index("## 12.14 —")
            section_end = open_work.find("\n## ", section_start + 1)
            if section_end < 0:
                section_end = len(open_work)
            section = open_work[section_start:section_end]
            if canonical_provenance in section:
                section = section.replace(canonical_provenance, collapsed_provenance, 1)
                open_work = open_work[:section_start] + section + open_work[section_end:]
            else:
                open_work = open_work[:section_end] + "\n\n" + collapsed_provenance + open_work[section_end:]
            open_work_path.write_text(open_work, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn("Open Work §12.14", promotion_check["message"])

    def test_fp001_identity_v014_lifecycle_evidence_boundaries_fail_closed(self):
        mutations = (
            ("missing evidence boundary", "### Inherited v0.1.3 certification evidence\n", ""),
            (
                "duplicate evidence boundary",
                "## A. Baseline and scope\n",
                "### Inherited v0.1.3 certification evidence\n\n## A. Baseline and scope\n",
            ),
            (
                "malformed evidence boundary",
                "## A. Baseline and scope\n",
                "### A. Baseline and scope\n",
            ),
        )
        for name, anchor, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                dossier_path = root / "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                dossier = self._ensure_identity_lifecycle_block(dossier_path)
                self.assertIn(anchor, dossier)
                dossier_path.write_text(dossier.replace(anchor, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("active Identity lifecycle evidence boundaries", promotion_check["message"])

    def test_fp001_pmr_validates_atlas_artifact_lineage_independently_of_open_work(self):
        mutations = (
            (
                "wrong direct predecessor",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md`",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.7.md`",
            ),
            (
                "wrong semver transition",
                "- **SemVer transition:** `v0.3.8 → v0.3.9`",
                "- **SemVer transition:** `v0.3.7 → v0.3.9`",
            ),
            (
                "missing predecessor metadata",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md` (routing predecessor; preserved byte-identically). Earlier v0.2.0, v0.2.1, v0.2.2, v0.2.3, v0.3.1 and v0.3.2 predecessors remain preserved.\n",
                "",
            ),
            (
                "duplicate predecessor metadata",
                "- **SemVer transition:** `v0.3.8 → v0.3.9`",
                "- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md` (duplicate)\n"
                "- **SemVer transition:** `v0.3.8 → v0.3.9`",
            ),
        )
        for name, anchor, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                atlas_path = root / "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.9.md"
                original_open_work = (root / "docs/00_platform/02_OPEN_WORK_v1.2.57.md").read_bytes()
                atlas = atlas_path.read_text(encoding="utf-8")
                self.assertIn(anchor, atlas)
                atlas_path.write_text(atlas.replace(anchor, replacement, 1), encoding="utf-8")
                self.assertEqual(original_open_work, (root / "docs/00_platform/02_OPEN_WORK_v1.2.57.md").read_bytes())
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("current Atlas artifact lineage", promotion_check["message"])

    def test_fp001_pmr_rejects_atlas_metadata_declarations_outside_header(self):
        mutations = (
            (
                "later predecessor declaration",
                "\n- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.7.md` (contradictory later declaration)\n",
            ),
            (
                "later transition declaration",
                "\n- **SemVer transition:** `v0.3.7 → v0.3.9` (contradictory later declaration)\n",
            ),
        )
        for name, declaration in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                atlas_path = root / "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.9.md"
                atlas = atlas_path.read_text(encoding="utf-8")
                header = atlas.split("## v0.3.9 Patch Scope", 1)[0]
                self.assertIn("- **Predecessor:** `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md`", header)
                self.assertIn("- **SemVer transition:** `v0.3.8 → v0.3.9`", header)
                atlas_path.write_text(atlas + declaration, encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("Atlas metadata declaration", promotion_check["message"])

    def test_fp001_pmr_allows_historical_lineage_prose_without_metadata_declarations(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            atlas_path = root / "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.3.9.md"
            atlas_path.write_text(
                atlas_path.read_text(encoding="utf-8")
                + "\nHistorical prose: Atlas v0.3.7 preceded the direct v0.3.8 predecessor, and the current transition is v0.3.8 to v0.3.9.\n",
                encoding="utf-8",
            )
            harden_path = root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md"
            harden_path.write_text(
                harden_path.read_text(encoding="utf-8")
                + "\nHistorical prose: v0.4.9 came before the current v0.5.0 predecessor; the certified semantics originate in v0.4.0.\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("PASS", promotion_check["status"], promotion_check["message"])

    def test_fp001_pmr_validates_harden_v051_successor_metadata(self):
        predecessor = "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.5.0.md` — byte-identical prior current-status snapshot\n"
        mutations = (
            (
                "multiple current predecessors",
                predecessor,
                predecessor + "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md`\n",
            ),
            (
                "wrong current predecessor",
                predecessor,
                "- **Current predecessor:** `archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md` — wrong direct predecessor\n",
            ),
            (
                "wrong certified successor version",
                "this v0.5.1 successor preserves them",
                "this v0.5.0 successor preserves them",
            ),
            (
                "missing successor base SHA",
                "- **v0.5.1 status-successor base main SHA:** `90f96ba3452c95112bf6ec4ce5bb897676adbed4`\n",
                "",
            ),
            (
                "incorrect successor base SHA",
                "- **v0.5.1 status-successor base main SHA:** `90f96ba3452c95112bf6ec4ce5bb897676adbed4`",
                "- **v0.5.1 status-successor base main SHA:** `0000000000000000000000000000000000000000`",
            ),
        )
        for name, anchor, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                harden_path = root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md"
                harden = harden_path.read_text(encoding="utf-8")
                self.assertIn(anchor, harden)
                harden_path.write_text(harden.replace(anchor, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("current HARDEN-02 v0.5.1 successor metadata", promotion_check["message"])

    def test_fp001_pmr_rejects_harden_metadata_declarations_outside_header(self):
        declarations = (
            ("Plan / contract version", "v0.5.0"),
            ("Current predecessor", "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md`"),
            ("Earlier historical status predecessor", "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.8.md`"),
            (
                "Certified contract semantics",
                "`archive/HARDEN-02_CONTRACT_WORKING_v0.4.9.md` — this v0.4.9 successor changes status",
            ),
            ("v0.5.0 status-successor base main SHA", "`0000000000000000000000000000000000000000`"),
            ("v0.5.1 status-successor base main SHA", "`0000000000000000000000000000000000000000`"),
        )
        for field, value in declarations:
            declaration = f"\n- **{field}:** {value}\n"
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                harden_path = root / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md"
                harden = harden_path.read_text(encoding="utf-8")
                self.assertIn("- **Plan / contract version:** `v0.5.1`", harden.split("### Revision log", 1)[0])
                harden_path.write_text(harden + declaration, encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
                self.assertIn("HARDEN-02 v0.5.1 successor metadata declaration", promotion_check["message"])

    def test_fp001_identity_v014_promotion_rejects_non_immediate_atlas_predecessor(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            open_work_path = root / "docs/00_platform/02_OPEN_WORK_v1.2.57.md"
            open_work = open_work_path.read_text(encoding="utf-8")
            current_predecessor = "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.8.md`"
            stale_predecessor = "immediate routing predecessor `archive/DELIVERY_ATLAS_WORKING_v0.3.7.md`"
            if current_predecessor in open_work:
                open_work = open_work.replace(current_predecessor, stale_predecessor, 1)
            elif stale_predecessor not in open_work:
                self.fail("Open Work Atlas predecessor mutation anchor is missing")
            open_work_path.write_text(open_work, encoding="utf-8")
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)
            promotion_check = next(
                check for check in report["checks"]
                if check["name"] == "fp001_pmr_reconciliation"
            )

            self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])
            self.assertIn(
                "Open Work v1.2.57 Atlas route must name archived Atlas v0.3.8 as its immediate routing predecessor",
                promotion_check["message"],
            )

    def test_fp001_identity_v014_promotion_rejects_lineage_route_and_gate_mutations(self):
        def rewrite_current_open_work_state(root: Path, mutate) -> None:
            manifest_path = root / "docs/00_platform/CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            current = next(
                entry for entry in manifest["governing_documents"]
                if entry["document_id"] == "OPEN_WORK" and entry.get("lifecycle") != "historical"
            )
            open_work_path = root / current["repository_path"]
            open_work = open_work_path.read_text(encoding="utf-8")
            start = open_work.index("<!-- HARDEN_02_LIFECYCLE_STATE_START -->")
            json_start = open_work.index("{", start)
            json_end = open_work.index("\n```", json_start)
            state = json.loads(open_work[json_start:json_end])
            mutate(state)
            open_work_path.write_text(
                open_work[:json_start] + json.dumps(state, indent=2) + open_work[json_end:],
                encoding="utf-8",
            )

        def replace_once(root: Path, relative: str, old: str, new: str) -> None:
            path = root / "docs/00_platform" / relative
            text = path.read_text(encoding="utf-8")
            if old not in text:
                raise AssertionError(f"mutation anchor missing from {relative}: {old}")
            path.write_text(text.replace(old, new, 1), encoding="utf-8")

        def restore_candidate_route(root: Path) -> None:
            candidate = (
                root / "docs/00_platform/working/candidates/"
                "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            )
            candidate.parent.mkdir(parents=True, exist_ok=True)
            candidate.write_bytes(
                (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").read_bytes()
            )

        mutations = (
            (
                "wrong current dossier version",
                lambda root: replace_once(
                    root,
                    "working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
                    "**Artifact version:** v0.1.4",
                    "**Artifact version:** v0.1.3",
                ),
            ),
            (
                "candidate remains on active route",
                restore_candidate_route,
            ),
            (
                "missing exact PR #76 candidate archive",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                ).unlink(),
            ),
            (
                "altered exact PR #76 candidate archive",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
                ).write_bytes(
                    (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md").read_bytes()
                    + b"\nALTERED CANDIDATE\n"
                ),
            ),
            (
                "missing superseded promoted-current v0.1.3 snapshot",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
                ).unlink(),
            ),
            (
                "altered superseded promoted-current v0.1.3 snapshot",
                lambda root: (
                    root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md"
                ).write_bytes(
                    (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md").read_bytes()
                    + b"\nALTERED CURRENT SNAPSHOT\n"
                ),
            ),
            (
                "PR #70 candidate confused with promoted-current snapshot",
                lambda root: (
                    (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md").write_bytes(
                        (root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3_SUPERSEDED_PROMOTED_CURRENT.md").read_bytes()
                    ),
                ),
            ),
            (
                "wrong PR #76 post-merge attestation URL",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state["identity_v014_promotion_certification"].update(
                        {"post_merge_attestation_url": "https://github.com/JCSchoeman96/NewYou/pull/76"}
                    ),
                ),
            ),
            (
                "missing PR #76 post-merge attestation URL",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state["identity_v014_promotion_certification"].pop(
                        "post_merge_attestation_url", None
                    ),
                ),
            ),
            (
                "post-merge reviewer falsely attributed to poster",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state["identity_v014_promotion_certification"].update(
                        {"post_merge_independent_review_actor": "JCSchoeman96"}
                    ),
                ),
            ),
            (
                "stale Open Work Identity lifecycle route",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"identity_dossier": "CERTIFIED / CURRENT v0.1.3"})
                ),
            ),
            (
                "stale README Identity route",
                lambda root: replace_once(
                    root,
                    "README.md",
                    "- IDENTITY v0.1.4: CERTIFIED / CURRENT under the separate PR #77 status successor; PR #76 candidate and post-merge certification evidence are COMPLETE",
                    "- IDENTITY v0.1.3: CERTIFIED / CURRENT under PR #70",
                ),
            ),
            (
                "stale Delivery Atlas Identity route",
                lambda root: replace_once(
                    root,
                    "working/DELIVERY_ATLAS_WORKING_v0.3.9.md",
                    "Identity dossier v0.1.4 is CERTIFIED / CURRENT",
                    "Identity dossier v0.1.3 is CERTIFIED / CURRENT",
                ),
            ),
            (
                "stale HARDEN-02 Identity route",
                lambda root: replace_once(
                    root,
                    "working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md",
                    "Identity dossier v0.1.4 are COMPLETE / CERTIFIED",
                    "Identity dossier v0.1.3 are COMPLETE / CERTIFIED",
                ),
            ),
            (
                "Communications started or finalised",
                lambda root: rewrite_current_open_work_state(
                    root,
                    lambda state: state.update(
                        {
                            "communications": "COMPLETE / FINALISED",
                            "communications_finalisation": "COMPLETE / FINALISED",
                        }
                    ),
                ),
            ),
            (
                "Phase 7C prematurely advanced",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"phase_7c": "READY / STARTED"})
                ),
            ),
            (
                "proof classification prematurely finalised",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"proof_classification": "FINALISED"})
                ),
            ),
            (
                "Phase 8 or implementation prematurely authorised",
                lambda root: rewrite_current_open_work_state(
                    root, lambda state: state.update({"application_implementation": "AUTHORISED"})
                ),
            ),
        )

        for name, mutate in mutations:
            with self.subTest(mutation=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                mutate(root)
                if name not in {
                    "missing exact PR #76 candidate archive",
                    "altered exact PR #76 candidate archive",
                    "missing superseded promoted-current v0.1.3 snapshot",
                    "altered superseded promoted-current v0.1.3 snapshot",
                    "PR #70 candidate confused with promoted-current snapshot",
                }:
                    refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                promotion_check = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )
                self.assertEqual("FAIL", promotion_check["status"], promotion_check["message"])

    def test_fp001_durable_delivery_attestation_requires_bound_post_merge_comment(self):
        mutations = (
            ("missing_url", lambda evidence: evidence.pop("post_merge_attestation_url", None)),
            (
                "self_assertion_used_as_url",
                lambda evidence: evidence.update(
                    {
                        "post_merge_attestation": "COMPLETE",
                        "post_merge_attestation_url": (
                            "COMPLETE / preserved in this status successor and Identity dossier v0.1.3"
                        ),
                    }
                ),
            ),
        )
        for name, mutate in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                open_work_path = root / "docs/00_platform/02_OPEN_WORK_v1.2.57.md"
                open_work = open_work_path.read_text(encoding="utf-8")
                lifecycle_start = open_work.index("<!-- HARDEN_02_LIFECYCLE_STATE_START -->")
                json_start = open_work.index("{", lifecycle_start)
                json_end = open_work.index("\n```", json_start)
                lifecycle_state = json.loads(open_work[json_start:json_end])
                mutate(lifecycle_state["identity_durable_delivery_certification"])
                open_work = (
                    open_work[:json_start]
                    + json.dumps(lifecycle_state, indent=2)
                    + open_work[json_end:]
                )
                open_work_path.write_text(open_work, encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)
                reconciliation = next(
                    check for check in report["checks"]
                    if check["name"] == "fp001_pmr_reconciliation"
                )

                self.assertEqual("FAIL", reconciliation["status"], reconciliation["message"])

    def test_fp001_pmr_rejects_unarchived_predecessor_route_in_current_atlas(self):
        mutations = (
            ("working/DELIVERY_ATLAS_WORKING_v0.3.9.md", "02_OPEN_WORK_v1.2.54.md"),
            ("working/DELIVERY_ATLAS_WORKING_v0.3.9.md", "DELIVERY_ATLAS_WORKING_v0.3.6.md"),
            ("working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md", "HARDEN-02_CONTRACT_WORKING_v0.4.8.md"),
            (
                "working/DELIVERY_ATLAS_WORKING_v0.3.9.md",
                "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
            ),
        )
        for route_path, predecessor in mutations:
            with self.subTest(predecessor=predecessor), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                current_route = root / "docs/00_platform" / route_path
                current_route.write_text(
                    current_route.read_text(encoding="utf-8")
                    + f"\nCurrent route pointer: {predecessor}\n",
                    encoding="utf-8",
                )
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] == "fp001_pmr_reconciliation"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )
                self.assertTrue(
                    any(
                        finding["check"] == "active_document_graph"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_fp001_pmr_rejects_multiple_active_skeleton_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            working = root / "docs/00_platform/working"
            active = working / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md"
            duplicate = working / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.4.md"
            duplicate.write_bytes(active.read_bytes())

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_rejects_multiple_active_identity_dossier_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            working = root / "docs/00_platform/working"
            active = working / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md"
            duplicate = working / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            duplicate.write_bytes(active.read_bytes())

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_mutation_matrix_fails_closed(self):
        mutations = (
            ("skeleton_pre_pmr_outcome", "skeleton", "A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, receive that Account's required human-facing Platform Member Reference (PMR), verify email, recover access and use a controlled support/admin path without exposing unfinished product spaces.", "A public visitor can choose Afrikaans or English, understand the launch-facing product and safety boundaries, create an individual 18+ account, verify email, recover access and use a controlled support/admin path without exposing unfinished product spaces."),
            ("identity_dossier_omits_pmr", "dossier", "The PMR is stable and human-facing.", "The PMR is opaque and non-human-facing."),
            ("pmr_before_account_success", "dossier", "only after successful individual Account creation", "before successful individual Account creation"),
            ("failed_partial_ambiguous_creation_exposes_pmr", "dossier", "A failed, partial or ambiguous Account creation does not assign an externally usable PMR", "A failed, partial or ambiguous Account creation assigns an externally usable PMR"),
            ("retry_does_not_converge", "dossier", "retries converge on the one committed Account/reference result", "retries create a new PMR on each attempt"),
            ("reference_not_stable_human_facing", "dossier", "The PMR is stable and human-facing.", "The PMR is unstable and opaque."),
            ("pmr_other_domain_owner", "dossier", "The Platform Member Reference is Identity & Access Account truth", "The Platform Member Reference is Communications Account truth"),
            ("pmr_is_authentication", "dossier", "it is not authentication", "it is authentication"),
            ("pmr_is_authorisation", "dossier", "it is not authorisation", "it is authorisation"),
            ("pmr_is_database_identity", "dossier", "It is not database identity", "It is database identity"),
            ("pmr_is_verification_assurance", "dossier", "it is not verification assurance", "it is verification assurance"),
            ("pmr_is_membership", "dossier", "it is not paid Membership", "it is paid Membership"),
            ("pmr_is_subscription", "dossier", "it is not subscription state", "it is subscription state"),
            ("pmr_is_entitlement", "dossier", "it is not entitlement", "it is entitlement"),
            ("pmr_is_payment_authority", "dossier", "it is not payment authority", "it is payment authority"),
            ("pmr_is_voucher_coupon_discount_authority", "dossier", "it is not a voucher/coupon/discount authority", "it is a voucher/coupon/discount authority"),
            ("pmr_is_bearer_credential", "dossier", "it is not a bearer credential", "it is a bearer credential"),
            ("multiple_active_pmrs", "dossier", "one canonical active PMR per canonical individual Account", "multiple canonical active PMRs per canonical individual Account"),
            ("ordinary_pmr_mutable", "dossier", "Ordinary PMR values are immutable.", "Ordinary PMR values are mutable."),
            ("reactivation_loses_reference", "dossier", "Legitimate reactivation retains the correct reference.", "Legitimate reactivation issues a new reference."),
            ("retired_reuse", "dossier", "never reassign or reuse it", "may reassign or reuse it"),
            ("duplicate_survivor_semantics_changed", "dossier", "one canonical active Account/reference and permanently retires the non-surviving reference", "two canonical active Accounts/references are retained"),
            ("allocation_collision_safety_lost", "dossier", "collision-safe, concurrency-correct and idempotent", "collision-prone, concurrency-unsafe and non-idempotent"),
            ("lookup_not_purpose_scoped", "dossier", "purpose-scoped, minimum-disclosure and non-authoritative", "unscoped, full-disclosure and authoritative"),
            ("lifecycle_dimensions_collapsed", "dossier", "orthogonal account, verification and security dimensions", "one collapsed Account status for account, verification and security"),
            ("representation_frozen", "skeleton", "Exact PMR representation remains unfrozen under `ARQ-IAM-013`", "The PMR prefix is VG and the alphabet is fixed"),
            ("arq_iam_013_resolved", "skeleton", "Exact PMR representation remains unfrozen under `ARQ-IAM-013`", "Exact PMR representation is resolved under `ARQ-IAM-013`"),
            ("oq034_proof_complete", "skeleton", "The approved authentication architecture is selected; executable proof is not complete and proof classification is not finalised.", "The approved authentication architecture is selected; executable proof is complete and proof classification is final.") ,
            ("oq035_resolved", "skeleton", "| `OQ-035` | `BLOCKS_RELEASE_ONLY` |", "| `OQ-035` | `RESOLVED` |"),
            ("oq036_resolved", "skeleton", "| `OQ-036` | `BLOCKS_RELEASE_ONLY` |", "| `OQ-036` | `RESOLVED` |"),
            ("communications_completed", "open_work", "COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED", "COMMUNICATIONS: COMPLETE / CERTIFIED"),
            ("communications_route_still_downstream", "open_work", "NEXT STAGE: COMMUNICATIONS JIT DOMAIN DOSSIER", "NEXT STAGE: FP001_RECONCILIATION_REQUIRED"),
            ("reconciliation_still_not_performed", "open_work", "FP001_RECONCILIATION_REQUIRED: COMPLETE / CERTIFIED\nIDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT", "FP001_RECONCILIATION_REQUIRED: REQUIRED / NEXT / NOT PERFORMED\nIDENTITY v0.1.4 PROMOTION: COMPLETE / CERTIFIED / CURRENT"),
            ("communications_dossier_started", "dossier", "COMMUNICATIONS DOSSIER STARTED: NO", "COMMUNICATIONS DOSSIER STARTED: YES"),
            ("conditional_dossiers_adjudicated", "open_work", "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE CONDITIONAL / PENDING EXPLICIT ADJUDICATION; ANALYTICS NOT REQUIRED", "CONDITIONAL DOSSIERS: PRIVACY & CONSENT, CONTENT & MEDIA, AUDIT & EVIDENCE COMPLETE; ANALYTICS NOT REQUIRED"),
            ("phase_7c_unblocked", "open_work", "PHASE 7C: BLOCKED / NOT_STARTED PENDING COMMUNICATIONS AND CONDITIONAL-DOSSIER DISPOSITIONS", "PHASE 7C: READY / NOT_BLOCKED"),
            ("proof_finalised", "open_work", "PROOF CLASSIFICATION: NOT FINALISED", "PROOF CLASSIFICATION: FINAL"),
            ("phase_8_authorised", "open_work", "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS", "EXECUTABLE DEVELOPMENT: AUTHORISED"),
            ("candidate_status_promoted_without_pr67_evidence", "skeleton", "79d0540c66f0224ece0330181e61dfef8ab4b458", "0000000000000000000000000000000000000000"),
            ("skeleton_remains_candidate", "skeleton", "**Lifecycle status:** `CERTIFIED / CURRENT`", "**Lifecycle status:** `RECONCILIATION CANDIDATE / NOT CERTIFIED`"),
            ("identity_dossier_remains_candidate", "dossier", "**Status:** `CERTIFIED / CURRENT`", "**Status:** `RECONCILIATION CANDIDATE / NOT CERTIFIED`"),
            ("communication_started", "open_work", "COMMUNICATIONS: REQUIRED / NEXT / NOT_STARTED", "COMMUNICATIONS: STARTED"),
            ('second_lifecycle_stage_advanced', 'open_work', '    "FP-001 IDENTITY v0.1.4 GOVERNANCE-CORRECTION PATCH PROMOTION"\n  ],\n  "engineering_standards_authority_promotion"', '    "FP-001 IDENTITY v0.1.4 GOVERNANCE-CORRECTION PATCH PROMOTION",\n    "COMMUNICATIONS JIT DOMAIN DOSSIER"\n  ],\n  "engineering_standards_authority_promotion"'),
            ("oq038_changed", "skeleton", "| `OQ-038` | `FUTURE_ONLY` |", "| `OQ-038` | `BLOCKS_RELEASE_ONLY` |"),
            ("store_cer_included", "open_work", "STORE / CER: EXCLUDED FROM HARDEN-02", "STORE / CER: INCLUDED IN SCOPE"),
        )
        source_root = Path(__file__).resolve().parents[1]
        for name, target, current, replacement in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                relative = {
                    "skeleton": "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md",
                    "dossier": "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.4.md",
                    "open_work": "docs/00_platform/02_OPEN_WORK_v1.2.57.md",
                }[target]
                path = root / relative
                text = path.read_text(encoding="utf-8")
                self.assertIn(current, text, f"mutation anchor missing: {name}")
                path.write_text(text.replace(current, replacement, 1), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] == "fp001_pmr_reconciliation"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_fp001_pmr_successor_requires_archived_predecessors_and_current_routes(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            predecessor_paths = (
                root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
                root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
                root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md",
            )
            for predecessor in predecessor_paths:
                predecessor.unlink()

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_rejects_stale_candidate_path_alongside_certified_successor(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            working = root / "docs/00_platform/working"
            stale = working / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"
            certified = working / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.3.md"
            stale.write_bytes(certified.read_bytes())

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_rejects_created_communications_dossier(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            communications = root / "docs/00_platform/working/FP-001_COMMUNICATIONS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            communications.write_text("status-only PR mutation\n", encoding="utf-8")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_archive_hash_contract_mutations_fail_closed(self):
        archive_paths = {
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md",
            "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.1.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.2.md",
            "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md",
        }
        for mutation in ("missing", "malformed", "wrong", "path_substitution"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root, manifest_path = self._copy_production_fixture(Path(directory))
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                hashes = manifest["integrity_rules"]["fp001_pmr_predecessor_archives"]
                if mutation == "missing":
                    hashes.pop("docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md")
                elif mutation == "malformed":
                    hashes["docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"] = "not-a-sha256"
                elif mutation == "wrong":
                    hashes["docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"] = "0" * 64
                else:
                    hashes.pop("docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md")
                    hashes["docs/00_platform/archive/UNEXPECTED_SUBSTITUTE.md"] = "a09bf07b189cbf3384cfe803d2ef1f32c3eaa6556333141fde1e323b6174b207"
                manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] == "fp001_pmr_reconciliation"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_fp001_pmr_candidate_archive_missing_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            (root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md").unlink()

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_corrupted_skeleton_archive_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_corrupted_identity_archive_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_pmr_corrupted_candidate_archive_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.2.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_identity_v013_candidate_archive_corruption_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            archive = root / "docs/00_platform/archive/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            archive.write_bytes(archive.read_bytes() + b"\nARCHIVE CORRUPTION\n")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_fp001_identity_v013_candidate_path_is_retired_after_promotion(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest_path = self._copy_production_fixture(Path(directory))
            stale_candidate = root / "docs/00_platform/working/candidates/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.3.md"
            stale_candidate.parent.mkdir(parents=True, exist_ok=True)
            stale_candidate.write_text("unpromoted candidate route\n", encoding="utf-8")

            report = run_audit(root, manifest_path)

            self.assertTrue(
                any(
                    finding["check"] == "fp001_pmr_reconciliation"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def _copy_production_fixture(self, root: Path) -> tuple[Path, Path]:
        source_root = Path(__file__).resolve().parents[1]
        fixture_docs = root / "docs" / "00_platform"
        shutil.copytree(source_root / "docs" / "00_platform", fixture_docs)
        manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        refresh_manifest(root, manifest_path)
        return root, manifest_path

    def test_harden_execution_state_machine_fixtures(self):
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        candidate_open_work = (source_docs / "02_OPEN_WORK_v1.2.57.md").read_text(encoding="utf-8")
        current_readme = (source_docs / "README.md").read_text(encoding="utf-8")
        contract = (source_docs / "working" / "HARDEN-02_CONTRACT_WORKING_v0.5.1.md").read_text(encoding="utf-8")
        expected = (True, "HARDEN-02 execution completion and downstream route are coherent")
        self.assertEqual(expected, _h02_lifecycle_state(candidate_open_work, current_readme, contract))

        incomplete = candidate_open_work.replace(
            '"harden_02_execution": "COMPLETE / CERTIFIED"',
            '"harden_02_execution": "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING"',
            1,
        )
        self.assertFalse(_h02_lifecycle_state(incomplete, current_readme, contract)[0])

        old_route = candidate_open_work.replace(
            "CURRENT AUTHORITY-STAGE PROGRAMME: CERTIFIED FP-001 IDENTITY v0.1.4 PATCH PROMOTION",
            "CURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION / STRUCTURAL HARDENING",
            1,
        ).replace(
            "NEXT STAGE: COMMUNICATIONS JIT DOMAIN DOSSIER",
            "NEXT STAGE: HARDEN-02_EXECUTION_REQUIRED",
            1,
        )
        self.assertFalse(_h02_lifecycle_state(old_route, current_readme, contract)[0])

        premature_standards = candidate_open_work.replace(
            '"engineering_standards_authority_promotion": "COMPLETE / CERTIFIED"',
            '"engineering_standards_authority_promotion": "NEXT / AUTHORISED / NOT STARTED"',
            1,
        )
        self.assertFalse(_h02_lifecycle_state(premature_standards, current_readme, contract)[0])

    def test_production_audit_uses_manifest_expectations(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["integrity_rules"]["expected_counts"]["decisions"] = 2
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            decision_count_check = next(
                check for check in report["checks"] if check["name"] == "definition_count_dec"
            )
            self.assertEqual("DEC definition count is 1, expected 2", decision_count_check["message"])

    def test_completed_stage_3a1_readiness_wording_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            readme.write_text(
                "\n".join(
                    [f"`{entry['canonical_filename']}`" for entry in manifest["governing_documents"]]
                    + [
                        "PLANNING FOUNDATION: READY",
                        "STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS: COMPLETE",
                        "STAGE 3A.2 — GOVERNED AR-000 AMENDMENT (NOT_STARTED / NEXT)",
                        "EXECUTABLE DEVELOPMENT: BLOCKED UNTIL PHASE 8 ENTRY CONDITIONS PASS",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json")

            readiness_check = next(
                check for check in report["checks"] if check["name"] == "readiness_wording"
            )
            self.assertEqual("PASS", readiness_check["status"])

    def test_source_at_freeze_references_are_not_stale(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            source_at_freeze = root / "docs" / "00_platform" / "reference" / "ARCHITECTURE_LAW_WORKING_v0.35.0.md"
            source_at_freeze.write_text(
                source_at_freeze.read_text(encoding="utf-8")
                + "\nSource tracker at freeze: 02_OPEN_WORK_v1.2.23.md\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)02_OPEN_WORK_v1\.2\.(?:[0-9]|1[0-9]|2[0-6])\.md"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = ["ROADMAP"]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_non_navigation_document_is_not_scanned_for_stale_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            current_navigation = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            current_navigation.write_text(
                current_navigation.read_text(encoding="utf-8") + "\nOLD_TRACKER_MARKER\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"OLD_TRACKER_MARKER"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = []
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertFalse(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_declared_current_navigation_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            current_navigation = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            current_navigation.write_text(
                current_navigation.read_text(encoding="utf-8") + "\nOLD_TRACKER_MARKER\n",
                encoding="utf-8",
            )
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"OLD_TRACKER_MARKER"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = ["ROADMAP"]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            self.assertTrue(
                any(finding["check"] == "active_document_graph" for finding in report["findings"])
            )

    def test_current_authorities_reject_unarchived_historical_open_work(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            pattern = r"(?<!archive/)02_OPEN_WORK_v1\.2\.44\.md"
            self.assertIn(pattern, manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"])
            self.assertIn(
                "routing guard only",
                manifest["integrity_rules"]["graph_rules"]["stale_open_work_v1_2_44_guard_note"],
            )

            authority_ids = (
                "PROJECT_NORTH_STAR_AND_MVP",
                "PLATFORM_BASELINE",
                "DECISION_REGISTER",
                "ROADMAP",
            )
            for document_id in authority_ids:
                entry = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == document_id
                )
                path = root / entry["repository_path"]
                path.write_text(
                    path.read_text(encoding="utf-8") + "\nStale route: 02_OPEN_WORK_v1.2.44.md\n",
                    encoding="utf-8",
                )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"])
            for document_id in authority_ids:
                entry = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == document_id
                )
                self.assertIn(entry["repository_path"], graph_check["message"])

    def test_archived_open_work_reference_is_allowed_in_current_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            product_entry = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8") + "\nHistorical source: archive/02_OPEN_WORK_v1.2.44.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("PASS", graph_check["status"], graph_check["message"])

    def test_stale_reference_route_rejects_former_integrity_audit_reference_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            product_entry = next(
                item for item in json.loads(manifest_path.read_text(encoding="utf-8"))["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\nStale route: reference/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"], graph_check["message"])
            self.assertIn(product_entry["repository_path"], graph_check["message"])
            self.assertIn("FOUNDATION_INTEGRITY_AUDIT", graph_check["message"])

    def test_archived_integrity_audit_reference_is_allowed_in_current_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            fixture_docs = root / "docs" / "00_platform"
            shutil.copytree(source_docs, fixture_docs)
            manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            product_entry = next(
                item for item in json.loads(manifest_path.read_text(encoding="utf-8"))["governing_documents"]
                if item["document_id"] == "PLATFORM_BASELINE"
            )
            path = root / product_entry["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\nHistorical evidence: archive/FOUNDATION_INTEGRITY_AUDIT_v1.0.0.md\n",
                encoding="utf-8",
            )
            refresh_manifest(root, manifest_path)

            report = run_audit(root, manifest_path)

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("PASS", graph_check["status"], graph_check["message"])

    def test_declared_working_navigation_path_is_scanned_for_stale_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            relative = "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.1.md"
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("See STALE_MOVED_SOURCE.md for the source.\n", encoding="utf-8")
            manifest["integrity_rules"]["graph_rules"]["stale_reference_patterns"] = [
                r"(?<!archive/)STALE_MOVED_SOURCE\.md"
            ]
            manifest["integrity_rules"]["graph_rules"]["navigation_document_ids"] = []
            manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"] = [relative]
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json")

            graph_check = next(check for check in report["checks"] if check["name"] == "active_document_graph")
            self.assertEqual("FAIL", graph_check["status"])
            self.assertIn(relative, graph_check["message"])

    def test_readme_current_authority_order_uses_positions_from_the_readme(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            readme.write_text(
                "\n".join(
                    f"{index}. `{entry['canonical_filename']}`"
                    for index, entry in enumerate(reversed(manifest["governing_documents"]), start=1)
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json")

            order_check = next(
                check for check in report["checks"] if check["name"] == "readme_current_authority_order"
            )
            self.assertEqual("FAIL", order_check["status"])

    def test_frozen_provenance_hash_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            manifest["governing_documents"][0]["provenance_sha256"] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
            path.write_text(path.read_text(encoding="utf-8") + "\nChanged after freeze.\n", encoding="utf-8")
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "frozen_provenance_hash" for finding in report["findings"])
            )

    def test_fad72c1_frozen_artifacts_match_accepted_hashes(self):
        root = Path(__file__).resolve().parents[1]

        for relative, expected_hash in FAD72C1_FROZEN_HASHES.items():
            with self.subTest(path=relative):
                actual_hash = hashlib.sha256((root / relative).read_bytes()).hexdigest()
                self.assertEqual(expected_hash, actual_hash)

    def test_hash_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["sha256"] = "0" * 64
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(finding["check"] == "manifest_hash_parity" for finding in report["findings"])
            )

    def test_unresolved_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nSee OQ-999.\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(finding["check"] == "identifier_resolution" for finding in report["findings"])
            )

    def test_duplicate_definition_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "## DEC-001 — Duplicate\n",
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "duplicate_definitions_dec" for finding in report["findings"])
            )

    def test_missing_roadmap_gate_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace("| OQ-001 |", "| Gate omitted |"),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "roadmap_gate_coverage" for finding in report["findings"])
            )

    def test_duplicate_roadmap_gate_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "05_ROADMAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "## 14.1", "| OQ-001 | Duplicate |\n## 14.1"
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "roadmap_gate_coverage" for finding in report["findings"])
            )

    def test_multiple_domain_owners_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "04_DOMAIN_MAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "| Truth | **Example Domain** |",
                    "| Truth | **Example Domain** and **Other Domain** |",
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "domain_ownership_uniqueness" for finding in report["findings"])
            )

    def test_duplicate_domain_name_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "04_DOMAIN_MAP_v1.0.0.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "## 4. Platform-wide",
                    "| 2 | **Example Domain** | Duplicate |\n## 4. Platform-wide",
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "duplicate_domain_names" for finding in report["findings"])
            )

    def test_missing_current_version_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_clean_fixture(root)
            manifest["governing_documents"][0]["semver"] = "9.9.9"
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "manifest_version_parity" for finding in report["findings"])
            )

    def test_document_version_metadata_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "**Document version:** v1.2.1", "**Document version:** v9.9.9"
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(finding["check"] == "document_version_parity" for finding in report["findings"])
            )

    def test_current_north_star_and_product_self_versions_match_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)

            for document_id, old_version, new_version in (
                ("PROJECT_NORTH_STAR_AND_MVP", "1.2.3", "9.9.9"),
                ("PLATFORM_BASELINE", "1.5.0", "9.9.9"),
            ):
                with self.subTest(document_id=document_id):
                    entry = next(
                        item for item in manifest["governing_documents"]
                        if item["document_id"] == document_id
                    )
                    path = root / entry["repository_path"]
                    path.write_text(
                        path.read_text(encoding="utf-8").replace(
                            f"**Document version:** v{old_version}",
                            f"**Document version:** v{new_version}",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, root / "manifest.json")

                    report = run_audit(
                        root,
                        root / "manifest.json",
                        expected_counts=SMALL_COUNTS,
                    )

                    self.assertTrue(
                        any(
                            finding["check"] == "current_authority_self_version"
                            and finding["path"] == entry["repository_path"]
                            for finding in report["findings"]
                        )
                    )

                    path.write_text(
                        path.read_text(encoding="utf-8").replace(
                            f"**Document version:** v{new_version}",
                            f"**Document version:** v{old_version}",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    refresh_manifest(root, root / "manifest.json")

    def test_north_star_governance_self_state_matches_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            north_star = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PROJECT_NORTH_STAR_AND_MVP"
            )
            path = root / north_star["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "governance-alignment condition: MET (v1.2.3)",
                    "governance-alignment condition: MET (v1.2.2)",
                    1,
                ),
                encoding="utf-8",
            )
            refresh_manifest(root, root / "manifest.json")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_self_version"
                    and finding["path"] == north_star["repository_path"]
                    for finding in report["findings"]
                )
            )

    def test_product_current_programme_lifecycle_mirror_is_rejected(self):
        for lifecycle in (
            "NEXT / AUTHORISED / NOT STARTED",
            "IN PROGRESS / NOT COMPLETE / CERTIFICATION PENDING",
            "COMPLETE / CERTIFIED",
        ):
            with self.subTest(lifecycle=lifecycle), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = self._write_current_authority_fixture(root)
                product = next(
                    item for item in manifest["governing_documents"]
                    if item["document_id"] == "PLATFORM_BASELINE"
                )
                path = root / product["repository_path"]
                with path.open("a", encoding="utf-8") as file:
                    file.write(f"HARDEN-02 execution is {lifecycle}.\n")
                refresh_manifest(root, root / "manifest.json")

                report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

                self.assertTrue(
                    any(
                        finding["check"] == "current_authority_delegated_routing"
                        and finding["path"] == product["repository_path"]
                        for finding in report["findings"]
                    )
                )

    def test_current_authority_fixture_passes_self_state_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_current_authority_fixture(root)

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertEqual("PASS", report["status"])
            self.assertEqual(
                {
                    "current_authority_self_version",
                    "current_authority_route_resolution",
                    "current_authority_delegated_routing",
                },
                {
                    check["name"]
                    for check in report["checks"]
                    if check["name"].startswith("current_authority_")
                },
            )

    def test_current_routing_field_must_resolve_to_manifest_routes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            north_star = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "PROJECT_NORTH_STAR_AND_MVP"
            )
            path = root / north_star["repository_path"]
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "CURRENT_AUTHORITY_MANIFEST",
                    "00_PLATFORM_v1.4.1.md",
                    1,
                ),
                encoding="utf-8",
            )
            refresh_manifest(root, root / "manifest.json")

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_route_resolution"
                    and finding["path"] == north_star["repository_path"]
                    for finding in report["findings"]
                )
            )

    def test_unregistered_governing_root_authority_document_fails_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
            shutil.copytree(source_docs, root / "docs" / "00_platform")
            manifest_path = root / "docs" / "00_platform" / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
            stale_copy = root / "docs" / "00_platform" / "00_PLATFORM_v1.4.1.md"
            archive_copy = root / "docs" / "00_platform" / "archive" / "00_PLATFORM_v1.4.1.md"
            shutil.copyfile(archive_copy, stale_copy)

            report = run_audit(root, manifest_path)

            self.assertEqual("FAIL", report["status"])
            self.assertTrue(
                any(
                    finding["check"] == "governing_root_exclusivity"
                    for finding in report["findings"]
                ),
                report["findings"],
            )

    def test_explicit_current_routes_in_roadmap_atlas_and_harden_resolve_relationally(self):
        source_docs = Path(__file__).resolve().parents[1] / "docs" / "00_platform"
        mutations = (
            (
                "05_ROADMAP_v1.2.0.md",
                "PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md",
                "PROJECT_NORTH_STAR_AND_MVP_v1.2.4.md",
            ),
            (
                "working/DELIVERY_ATLAS_WORKING_v0.3.9.md",
                "00_PLATFORM_v1.6.0.md",
                "00_PLATFORM_v1.5.1.md",
            ),
            (
                "working/HARDEN-02_CONTRACT_WORKING_v0.5.1.md",
                "02_OPEN_WORK_v1.2.57.md",
                "02_OPEN_WORK_v1.2.50.md",
            ),
            (
                "02_OPEN_WORK_v1.2.57.md",
                "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.9.md`",
                "ATLAS RECONCILIATION: COMPLETE — current Atlas `working/DELIVERY_ATLAS_WORKING_v0.3.2.md`",
            ),
        )
        for relative, current_route, stale_route in mutations:
            with self.subTest(path=relative), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                fixture_docs = root / "docs" / "00_platform"
                shutil.copytree(source_docs, fixture_docs)
                manifest_path = fixture_docs / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                path = fixture_docs / relative
                text = path.read_text(encoding="utf-8")
                self.assertIn(current_route, text)
                path.write_text(text.replace(current_route, stale_route, 1), encoding="utf-8")
                governing_entry = next(
                    entry
                    for entry in manifest["governing_documents"]
                    if entry["repository_path"] == f"docs/00_platform/{relative}"
                ) if not relative.startswith("working/") else None
                if governing_entry is not None and "provenance_sha256" in governing_entry:
                    governing_entry["provenance_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
                    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
                refresh_manifest(root, manifest_path)

                report = run_audit(root, manifest_path)

                self.assertTrue(
                    any(
                        finding["check"] == "current_authority_route_resolution"
                        for finding in report["findings"]
                    ),
                    report["findings"],
                )

    def test_current_state_delegated_routing_must_match_readme_and_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self._write_current_authority_fixture(root)
            readme = root / "docs" / "00_platform" / "README.md"
            current_open_work = next(
                item for item in manifest["governing_documents"]
                if item["document_id"] == "OPEN_WORK"
            )["canonical_filename"]
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    current_open_work,
                    "02_OPEN_WORK_v1.2.48.md",
                    1,
                ),
                encoding="utf-8",
            )

            report = run_audit(root, root / "manifest.json", expected_counts=SMALL_COUNTS)

            self.assertTrue(
                any(
                    finding["check"] == "current_authority_delegated_routing"
                    for finding in report["findings"]
                )
            )

    def test_refresh_manifest_updates_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_clean_fixture(root)
            path = root / "docs" / "00_platform" / "01_DECISIONS_v1.2.1.md"
            path.write_text("## DEC-001 — Changed\n## OQ-001 — Example\n", encoding="utf-8")

            refresh_manifest(root, root / "manifest.json")
            manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
            expected_hash = hashlib.sha256(path.read_bytes()).hexdigest()

            self.assertEqual(expected_hash, manifest["governing_documents"][0]["sha256"])

    def _write_clean_fixture(self, root: Path) -> dict:
        files = {
            "docs/00_platform/01_DECISIONS_v1.2.1.md": (
                "- **Document version:** v1.2.1\n"
                "## DEC-001 — Example\n"
                "## OQ-001 — Example\n"
            ),
            "docs/00_platform/05_ROADMAP_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "# 14. Gate schedule\n"
                "| OQ-001 | Example |\n"
                "## 14.1 Non-OQ expert/vendor gates\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_LAW_WORKING_v0.35.0.md": (
                "- **Document version:** v0.35.0\n"
                "## ARC-001 — Example\n"
            ),
            "docs/00_platform/reference/ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "### ARQ-TEST-001 — Example\n"
            ),
            "docs/00_platform/reference/REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": (
                "- **Document version:** v0.2.0\n"
                "# 3. FLOW-01 — Example\n"
            ),
            "docs/00_platform/04_DOMAIN_MAP_v1.0.0.md": (
                "- **Document version:** v1.0.0\n"
                "## 3. Approved domain set\n"
                "| 1 | **Example Domain** | Example |\n"
                "## 4. Platform-wide business-truth ownership matrix\n"
                "| Business truth | Authoritative domain | Dependents | Rule |\n"
                "| Truth | **Example Domain** | None | READ |\n"
                "### 4.1 Ownership interpretation\n"
            ),
        }

        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        manifest = {
            "governing_documents": [],
            "reference_documents": [],
            "historical_documents": [],
            "integrity_rules": {
                "document_roots": {
                    "governing": "docs/00_platform",
                    "reference": "docs/00_platform/reference",
                    "historical": "docs/00_platform/archive",
                    "context_index": "docs/00_platform/README.md",
                },
                "expected_counts": SMALL_COUNTS,
                "contiguous_ranges": {
                    "DEC": {"prefix": "DEC", "start": 1, "end": 1, "width": 3},
                    "OQ": {"prefix": "OQ", "start": 1, "end": 1, "width": 3},
                    "ARC": {"prefix": "ARC", "start": 1, "end": 1, "width": 3},
                    "FLOW": {"prefix": "FLOW", "start": 1, "end": 1, "width": 2},
                },
                "definition_sources": {
                    "decisions": "DECISION_REGISTER",
                    "architecture_law": "ARCHITECTURE_LAW_EVIDENCE",
                    "architecture_requirements": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
                    "reference_flows": "REFERENCE_FLOW_EVIDENCE",
                    "roadmap": "ROADMAP",
                    "domain_map": "DOMAIN_LAW",
                },
                "graph_rules": {
                    "stale_reference_patterns": [],
                    "reference_header_lines": 35,
                    "frozen_provenance_policy": "frozen_provenance",
                    "navigation_document_ids": ["ROADMAP"],
                },
            },
        }
        authority_classes = {
            "01_DECISIONS_v1.2.1.md": "DECISION_REGISTER",
            "05_ROADMAP_v1.0.0.md": "ROADMAP",
            "ARCHITECTURE_LAW_WORKING_v0.35.0.md": "ARCHITECTURE_LAW_EVIDENCE",
            "ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "REFERENCE_FLOW_EVIDENCE",
            "04_DOMAIN_MAP_v1.0.0.md": "DOMAIN_LAW",
        }
        document_ids = {
            "01_DECISIONS_v1.2.1.md": "DECISION_REGISTER",
            "05_ROADMAP_v1.0.0.md": "ROADMAP",
            "ARCHITECTURE_LAW_WORKING_v0.35.0.md": "ARCHITECTURE_LAW_EVIDENCE",
            "ARCHITECTURE_REQUIREMENTS_WORKING_v1.0.0.md": "ARCHITECTURE_REQUIREMENTS_EVIDENCE",
            "REFERENCE_FLOW_PRESSURE_TESTS_WORKING_v0.2.0.md": "REFERENCE_FLOW_EVIDENCE",
            "04_DOMAIN_MAP_v1.0.0.md": "DOMAIN_LAW",
        }
        for relative in files:
            path = root / relative
            manifest["governing_documents"].append(
                {
                    "document_id": document_ids[path.name],
                    "canonical_filename": path.name,
                    "semver": path.name.split("_v", 1)[1][:-3],
                    "repository_path": relative,
                    "authority_class": authority_classes[path.name],
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                }
            )

        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest

    def _write_current_authority_fixture(self, root: Path) -> dict:
        manifest = self._write_clean_fixture(root)
        files = {
            "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": (
                "# PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md\n"
                "- **Document version:** v1.2.3\n"
                "# 23. Current Planning Position\n"
                "Current Product/Decision/Roadmap authority is routed by README and CURRENT_AUTHORITY_MANIFEST. README and current Open Work own the active programme stage and NEXT route.\n"
                "# 24. Document Stop Condition\n"
                "**Current Product Law / governance-alignment condition: MET (v1.2.3).**\n"
                "**Implementation STOP:** planning gates remain mandatory.\n"
            ),
            "docs/00_platform/00_PLATFORM_v1.5.0.md": (
                "# 00_PLATFORM_v1.5.0.md\n"
                "- **Document version:** v1.5.0\n"
                "# 24. Current Planning Stop Condition\n"
                "Current Product Law is v1.5.0. This Product Law does not execute HARDEN-02 or authorise implementation. README and current Open Work own current programme routing and lifecycle status.\n"
            ),
            "docs/00_platform/02_OPEN_WORK_v1.0.0.md": (
                "# 02_OPEN_WORK_v1.0.0.md\n"
                "- **Document version:** v1.0.0\n"
            ),
            "docs/00_platform/README.md": (
                "## Default Agent Context\n"
                "1. `PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md`\n"
                "2. `00_PLATFORM_v1.5.0.md`\n"
                "3. `01_DECISIONS_v1.2.1.md`\n"
                "4. `02_OPEN_WORK_v1.0.0.md`\n"
                "5. `05_ROADMAP_v1.0.0.md`\n"
                "\n## Active Working Artifacts\n"
            ),
        }
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        authority_classes = {
            "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": "PRODUCT_NORTH_STAR",
            "00_PLATFORM_v1.5.0.md": "PLATFORM_PRODUCT_LAW",
            "02_OPEN_WORK_v1.0.0.md": "PLANNING_TRACKER",
        }
        document_ids = {
            "PROJECT_NORTH_STAR_AND_MVP_v1.2.3.md": "PROJECT_NORTH_STAR_AND_MVP",
            "00_PLATFORM_v1.5.0.md": "PLATFORM_BASELINE",
            "02_OPEN_WORK_v1.0.0.md": "OPEN_WORK",
        }
        for relative in files:
            path = root / relative
            if path.name == "README.md":
                continue
            manifest["governing_documents"].append(
                {
                    "document_id": document_ids[path.name],
                    "canonical_filename": path.name,
                    "semver": path.name.split("_v", 1)[1][:-3],
                    "repository_path": relative,
                    "authority_class": authority_classes[path.name],
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "superseded_version": None,
                }
            )
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest


if __name__ == "__main__":
    unittest.main()
