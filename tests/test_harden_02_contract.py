from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.3.0.md"
CONTRACT_PREDECESSOR = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.2.0.md"
CONTRACT_OLDER_PREDECESSOR = DOCS / "archive" / "HARDEN-02_CONTRACT_WORKING_v0.1.0.md"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.42.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.41.md"
OPEN_WORK_OLDER_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.40.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

EXPECTED_BASE_SHA = "2599638334b761ddef8e5568d0a38c3207eef722"
EXPECTED_CONTRACT_V0_2_SHA256 = "9fab2f79b1e5720378a6852bcda9c81aafe8564cd0866a0ea38c1242e7b34f5f"
EXPECTED_OPEN_WORK_V1_2_41_SHA256 = "85dd9946cf5684b0907f49e973ef75b59541c0f265ac46d44465d1527535da62"
EXPECTED_ATLAS_V0_2_SHA256 = "c122c0f4a903c9679529e0e65a794999dcdaf957a66fcff00df990a0644bbb7f"

PROTECTED_UPSTREAM_HASHES = {
    "docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.2.1.md": "5bf5a8582d5ada7c7c39d937a6730e29d219c11b688a31fb763e439047d89a20",
    "docs/00_platform/00_PLATFORM_v1.3.0.md": "4694f841cfa92c2a802b50a1db7dcf3a5043e8a62a2a5250d6dfe819e5388445",
    "docs/00_platform/01_DECISIONS_v1.3.0.md": "43ecce4423cd90afbf97fa3c447a54a591e0d34acb7e6a5250a8b91c7b650a96",
    "docs/00_platform/03_ARCHITECTURE_v1.1.0.md": "d44615f0db3f5f0b38bb68a2904db6066d23e1f82c55da134745c4f6d70b6852",
    "docs/00_platform/04_DOMAIN_MAP_v1.1.0.md": "2c66142e624ccd626727ae36511121fcb64333ca774986ab97ce31eebe5c5ef2",
    "docs/00_platform/05_ROADMAP_v1.1.0.md": "eaeaf6031e47653777caf5885ad9eb0ceba58783c99d7d6d255acfbca53fa613",
    "docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.0.md": "884a7231a86b438a220f057e03ba9c06357820b43629e018d50c92cc773b2811",
    "docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.0.md": "caadd2dfc3c7ed872fda5806efdba467d753b9662e1ff47af16b6303d90b9fa3",
    "docs/00_platform/working/FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md": "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be",
    "docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md": "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.39.md": "5af9c6965d214bb0dd46cd3215a2e23ed1a17d546ef53ccd4de31be346d11e21",
    "docs/00_platform/archive/02_OPEN_WORK_v1.2.40.md": "e53d416efe2b859053e4d2167b36065383f4f67603db56d833f20247d5120b3e",
    "docs/00_platform/archive/HARDEN-02_CONTRACT_WORKING_v0.1.0.md": "71615d3363a91a7e6002d907c6edd474fbd87f77bdfc6a38f5b11afd240a5626",
    "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.2.0.md": EXPECTED_ATLAS_V0_2_SHA256,
    ".github/workflows/foundation-integrity.yml": "2c718457456c71ad8d7fc416a6e0a646792271b9341e4a14fedda6ddb02bcdb8",
}

PROHIBITED_PRESENT_PATHS = (
    "docs/00_platform/02_OPEN_WORK_v1.2.39.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.40.md",
    "docs/00_platform/02_OPEN_WORK_v1.2.41.md",
    "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.1.0.md",
    "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.2.0.md",
    "docs/00_platform/ENGINEERING_STANDARDS_v1.0.0.md",
    "docs/00_platform/reference/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    "docs/00_platform/working/ENGINEERING_STANDARDS_WORKING_v0.1.0.md",
    "mix.exs",
)

EXPECTED_RECOVERY_STATE = {
    "baseline_main_sha": EXPECTED_BASE_SHA,
    "current_stage": "HARDEN-02_CONTRACT_RECOVERY_REQUIRED",
    "next_stage": "HARDEN-02_CONTRACT_RECOVERY_REQUIRED",
    "contract_version": "0.3.0",
    "contract_status": "OPEN / PENDING INDEPENDENT PRE-MERGE CERTIFICATION",
    "pre_merge_certification": "PENDING",
    "exact_head_ci": "PENDING",
    "certified_head_merge": "PENDING",
    "post_merge_certification": "PENDING",
    "harden_02_execution": "NOT STARTED / NOT AUTHORISED",
    "harden_02_scope": "PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY",
    "store_cer": "EXCLUDED",
    "completed_milestones": [
        "TARGETED PRODUCT AMENDMENT PROGRAMME",
        "FP-001 PHASE 7A",
        "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
    ],
    "engineering_standards_authority_promotion": "DOWNSTREAM / NOT STARTED",
    "fp001_reconciliation": "REQUIRED / DOWNSTREAM / NOT PERFORMED",
    "communications": "REQUIRED / NOT_STARTED",
    "conditional_dossiers": {
        "privacy_consent": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "content_media": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "audit_evidence": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
        "analytics": "NOT REQUIRED",
    },
    "phase_7c": "BLOCKED / NOT_STARTED",
    "proof_classification": "NOT FINALISED",
    "application_implementation": "BLOCKED",
    "pr_38": "BLOCKED / NOT AUTHORITY",
    "downstream_route": [
        "CERTIFIED HARDEN-02 EXECUTION",
        "ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED",
        "CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION",
        "FP001_RECONCILIATION_REQUIRED",
        "COMMUNICATIONS JIT DOMAIN DOSSIER",
        "REMAINING REQUIRED / CONDITIONAL PHASE 7B",
        "PHASE 7C",
        "PROOF CLASSIFICATION",
        "PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
    ],
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(text: str, heading: str, next_heading: str) -> str:
    start = text.index(heading)
    end = text.index(next_heading, start)
    return text[start:end]


def _reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise AssertionError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _marked_json(text: str, start_marker: str, end_marker: str) -> dict[str, object]:
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise AssertionError("expected one marked JSON record")
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    region = text[start:end]
    match = re.search(r"```json\s*(\{.*?\})\s*```", region, re.DOTALL)
    if match is None:
        raise AssertionError("marked JSON record is missing")
    return json.loads(match.group(1), object_pairs_hook=_reject_duplicate_json_keys)


def _route_declaration(text: str, label: str) -> str:
    declarations = re.findall(
        rf"^\s*(?:-\s*)?{re.escape(label)}:\s*(.+)$",
        text,
        re.MULTILINE,
    )
    if len(declarations) != 1:
        raise AssertionError(f"expected one {label} declaration, found {len(declarations)}")
    return declarations[0].strip()


def _assert_no_current_execution_authority(text: str) -> None:
    if re.search(
        r"^\s*(?:-\s*)?HARDEN-02 EXECUTION:\s*NEXT\s*/\s*AUTHORISED\s*$",
        text,
        re.MULTILINE,
    ):
        raise AssertionError("recovery text grants execution authority")
    if re.search(r"^HARDEN-02_EXECUTION_REQUIRED\s*$", text, re.MULTILINE):
        raise AssertionError("legacy execution route appears as current")


def _valid_sha(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value) is not None


def _valid_pr_record_url(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(
        r"https://github\.com/JCSchoeman96/NewYou/pull/\d+#(?:pullrequestreview|issuecomment)-\d+",
        value,
    ) is not None


def _valid_actions_url(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(
        r"https://github\.com/JCSchoeman96/NewYou/actions/runs/\d+",
        value,
    ) is not None


def _record_has_fields(record: object, required_fields: object) -> bool:
    return (
        isinstance(record, dict)
        and isinstance(required_fields, list)
        and all(isinstance(field, str) and field in record for field in required_fields)
    )


def _execution_entry_passes(
    expected_head_sha: str,
    pr_author: str,
    evidence: object,
    evidence_spec: dict[str, object],
) -> bool:
    if not _valid_sha(expected_head_sha) or not isinstance(evidence, dict):
        return False

    keys = (
        "pre_merge_review",
        "pre_merge_ci",
        "merge",
        "post_merge_ci",
        "post_merge_certification",
    )
    if not all(_record_has_fields(evidence.get(key), evidence_spec.get(key)) for key in keys):
        return False

    review = evidence["pre_merge_review"]
    pre_ci = evidence["pre_merge_ci"]
    merge = evidence["merge"]
    post_ci = evidence["post_merge_ci"]
    post_cert = evidence["post_merge_certification"]
    if not all(isinstance(record, dict) for record in (review, pre_ci, merge, post_ci, post_cert)):
        return False

    reviewer = review["independent_reviewer"]
    post_reviewer = post_cert["independent_reviewer"]
    main_sha = merge["resulting_main_sha"]
    return all(
        (
            review["reviewed_head_sha"] == expected_head_sha,
            review["reviewed_head_is_certified_head"] is True,
            review["outcome"] == "PASS",
            isinstance(reviewer, str) and reviewer and reviewer != pr_author,
            _valid_pr_record_url(review["record_url"]),
            pre_ci["head_sha"] == expected_head_sha,
            pre_ci["conclusion"] == "PASS",
            pre_ci["workflow"] == "Foundation Integrity",
            _valid_actions_url(pre_ci["run_url"]),
            merge["certified_head_sha"] == expected_head_sha,
            merge["merged_head_sha"] == expected_head_sha,
            _valid_sha(main_sha),
            post_ci["head_sha"] == main_sha,
            post_ci["conclusion"] == "PASS",
            post_ci["workflow"] == "Foundation Integrity",
            _valid_actions_url(post_ci["run_url"]),
            post_cert["resulting_main_sha"] == main_sha,
            post_cert["certified_head_sha"] == expected_head_sha,
            post_cert["ci_head_sha"] == main_sha,
            post_cert["ci_conclusion"] == "PASS",
            post_cert["ci_run_url"] == post_ci["run_url"],
            post_cert["outcome"] == "PASS",
            isinstance(post_reviewer, str) and post_reviewer and post_reviewer != pr_author,
            _valid_pr_record_url(post_cert["record_url"]),
        )
    )


class Harden02ContractRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = CONTRACT.read_text(encoding="utf-8")
        cls.contract_predecessor = CONTRACT_PREDECESSOR.read_text(encoding="utf-8")
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.recovery_state = _marked_json(
            cls.open_work,
            "<!-- HARDEN_02_RECOVERY_STATE_START -->",
            "<!-- HARDEN_02_RECOVERY_STATE_END -->",
        )
        cls.evidence_spec = _marked_json(
            cls.contract,
            "<!-- HARDEN_02_CERTIFICATION_EVIDENCE_SPEC_START -->",
            "<!-- HARDEN_02_CERTIFICATION_EVIDENCE_SPEC_END -->",
        )

    def test_v0_3_is_the_active_working_successor_and_rebased_on_expected_main(self):
        self.assertTrue(CONTRACT.is_file())
        self.assertIn("Plan / contract version:** `v0.3.0`", self.contract)
        self.assertIn("OPEN / PENDING INDEPENDENT PRE-MERGE CERTIFICATION", self.contract)
        self.assertIn("execution **NOT STARTED / NOT AUTHORISED**", self.contract)
        self.assertIn(f"Re-baseline main SHA:** `{EXPECTED_BASE_SHA}`", self.contract)
        self.assertEqual(EXPECTED_BASE_SHA, self.recovery_state["baseline_main_sha"])
        self.assertIn("WORKING GOVERNANCE CONTRACT", self.contract)
        self.assertNotIn("REUSE_HARDENING", self.contract)

    def test_v0_2_is_archived_byte_identically_and_not_retroactively_certified(self):
        self.assertTrue(CONTRACT_PREDECESSOR.is_file())
        self.assertEqual(EXPECTED_CONTRACT_V0_2_SHA256, _sha256(CONTRACT_PREDECESSOR))
        self.assertFalse((DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.2.0.md").exists())
        for statement in (
            "historical evidence of the previous contract attempt",
            "CI facts remain valid historical facts",
            "COMPLETE / CERTIFIED lifecycle was never repository-verifiably established",
            "does not retroactively repair or certify v0.2.0",
            "This recovery follows v0.2.0 §13: re-baseline and amend the contract rather than silently expanding scope.",
        ):
            self.assertIn(statement, self.contract)
        self.assertIn("PR #37", self.contract)
        self.assertIn("b1b0431152481006bbc1eff33cc9844a1b8c1ad5", self.contract)
        self.assertIn("35859522372", self.contract)
        self.assertIn("35875423226", self.contract)

    def test_open_work_v1_2_41_is_archived_byte_identically(self):
        self.assertTrue(OPEN_WORK_PREDECESSOR.is_file())
        self.assertEqual(EXPECTED_OPEN_WORK_V1_2_41_SHA256, _sha256(OPEN_WORK_PREDECESSOR))
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.41.md").exists())
        self.assertIn("v1.2.41 → v1.2.42", self.open_work)

    def test_harden_02_scope_invariants_are_preserved_from_v0_2(self):
        for start, end in (
            ("## 3. Accepted human scope decisions", "## 4. In scope"),
            ("## 8. Current structural invariant suite", "## 9. Stale-state / restart pressure tests"),
        ):
            predecessor_section = _section(self.contract_predecessor, start, end)
            successor_section = _section(self.contract, start, end)
            if start.startswith("## 3."):
                for scope_id in ("H02-1", "H02-2", "H02-3", "H02-3R"):
                    predecessor_row = next(
                        line for line in predecessor_section.splitlines()
                        if line.startswith(f"| `{scope_id}` |")
                    )
                    successor_row = next(
                        line for line in successor_section.splitlines()
                        if line.startswith(f"| `{scope_id}` |")
                    )
                    self.assertEqual(predecessor_row, successor_row, scope_id)
            else:
                self.assertEqual(predecessor_section, successor_section)

    def test_recovery_stays_the_single_current_stage_and_rejects_appended_routes(self):
        expected_label = "HARDEN-02 CONTRACT RECOVERY / RE-CERTIFICATION REQUIRED"
        expected_next = "HARDEN-02_CONTRACT_RECOVERY_REQUIRED"
        self.assertEqual(
            expected_label,
            _route_declaration(self.open_work, "CURRENT AUTHORITY-STAGE PROGRAMME"),
        )
        self.assertEqual(expected_next, _route_declaration(self.open_work, "NEXT STAGE"))
        self.assertEqual(
            expected_label,
            _route_declaration(self.readme, "CURRENT AUTHORITY-STAGE PROGRAMME"),
        )
        self.assertEqual(expected_next, _route_declaration(self.readme, "NEXT STAGE"))
        self.assertEqual(EXPECTED_RECOVERY_STATE, self.recovery_state)
        _assert_no_current_execution_authority(self.open_work)
        _assert_no_current_execution_authority(self.readme)

        conflicting_text = (
            self.open_work
            + "\nCURRENT AUTHORITY-STAGE PROGRAMME: HARDEN-02 EXECUTION\n"
            + "NEXT STAGE: ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED\n"
        )
        with self.assertRaises(AssertionError):
            _route_declaration(conflicting_text, "CURRENT AUTHORITY-STAGE PROGRAMME")
        with self.assertRaises(AssertionError):
            _route_declaration(conflicting_text, "NEXT STAGE")
        with self.assertRaises(AssertionError):
            _assert_no_current_execution_authority(
                self.open_work + "\nHARDEN-02 EXECUTION: NEXT / AUTHORISED\n"
            )

    def test_missing_certification_and_head_drift_fail_closed(self):
        head_sha = "a" * 40
        self.assertFalse(
            _execution_entry_passes(
                head_sha,
                "pr-author",
                {},
                self.evidence_spec,
            )
        )

        evidence = self._complete_evidence(head_sha)
        self.assertTrue(_execution_entry_passes(head_sha, "pr-author", evidence, self.evidence_spec))

        drifted_review = self._complete_evidence(head_sha)
        drifted_review["pre_merge_review"]["reviewed_head_sha"] = "b" * 40
        self.assertFalse(
            _execution_entry_passes(head_sha, "pr-author", drifted_review, self.evidence_spec)
        )

        drifted_merge = self._complete_evidence(head_sha)
        drifted_merge["merge"]["merged_head_sha"] = "b" * 40
        self.assertFalse(
            _execution_entry_passes(head_sha, "pr-author", drifted_merge, self.evidence_spec)
        )

        changed_head = "c" * 40
        self.assertFalse(
            _execution_entry_passes(changed_head, "pr-author", evidence, self.evidence_spec)
        )

    def test_certification_schema_requires_durable_exact_sha_records(self):
        self.assertEqual(
            {
                "pre_merge_review": [
                    "reviewed_head_sha",
                    "outcome",
                    "reviewed_head_is_certified_head",
                    "independent_reviewer",
                    "record_url",
                ],
                "pre_merge_ci": ["head_sha", "conclusion", "workflow", "run_url"],
                "merge": ["certified_head_sha", "merged_head_sha", "resulting_main_sha"],
                "post_merge_ci": ["head_sha", "conclusion", "workflow", "run_url"],
                "post_merge_certification": [
                    "resulting_main_sha",
                    "certified_head_sha",
                    "ci_head_sha",
                    "ci_conclusion",
                    "ci_run_url",
                    "outcome",
                    "independent_reviewer",
                    "record_url",
                ],
            },
            self.evidence_spec,
        )
        for requirement in (
            "submitted GitHub PR review",
            "clearly identified PR review comment",
            "independent reviewer certifies the exact immutable PR head with outcome PASS",
            "exact reviewed head SHA",
            "the previous certification and CI evidence do not cover the new head",
            "the exact PR head is the head being certified",
            "independent reviewer must leave a repository-verifiable post-merge certification record on GitHub with outcome PASS",
            "repository-verifiable",
        ):
            self.assertIn(requirement, self.contract)

    def test_execution_remains_not_started_and_downstream_gates_remain_blocked(self):
        self.assertEqual("NOT STARTED / NOT AUTHORISED", self.recovery_state["harden_02_execution"])
        self.assertIn("HARDEN-02 execution remains NOT STARTED / NOT AUTHORISED throughout this recovery PR", self.contract)
        self.assertEqual("DOWNSTREAM / NOT STARTED", self.recovery_state["engineering_standards_authority_promotion"])
        self.assertEqual("REQUIRED / DOWNSTREAM / NOT PERFORMED", self.recovery_state["fp001_reconciliation"])
        self.assertEqual("REQUIRED / NOT_STARTED", self.recovery_state["communications"])
        self.assertEqual("BLOCKED / NOT_STARTED", self.recovery_state["phase_7c"])
        self.assertEqual("NOT FINALISED", self.recovery_state["proof_classification"])
        self.assertEqual("BLOCKED", self.recovery_state["application_implementation"])
        self.assertEqual("BLOCKED / NOT AUTHORITY", self.recovery_state["pr_38"])
        self.assertIn("PR #38 is not authority and remains blocked until this recovery is complete", self.open_work)

    def test_full_h02_3r_route_is_explicit_and_ordered(self):
        expected_route = EXPECTED_RECOVERY_STATE["downstream_route"]
        self.assertEqual(expected_route, self.recovery_state["downstream_route"])
        for stage in expected_route:
            self.assertIn(stage, self.contract)
            self.assertIn(stage, self.open_work)
        self.assertIn("H02-3R", self.contract)
        self.assertIn("H02-3R", self.open_work)

    def test_completed_milestones_and_conditional_dossier_dispositions_remain_explicit(self):
        self.assertEqual(
            [
                "TARGETED PRODUCT AMENDMENT PROGRAMME",
                "FP-001 PHASE 7A",
                "IDENTITY & ACCESS JIT DOMAIN DOSSIER",
            ],
            self.recovery_state["completed_milestones"],
        )
        self.assertEqual("CONDITIONAL / PENDING EXPLICIT ADJUDICATION", self.recovery_state["conditional_dossiers"]["privacy_consent"])
        self.assertEqual("CONDITIONAL / PENDING EXPLICIT ADJUDICATION", self.recovery_state["conditional_dossiers"]["content_media"])
        self.assertEqual("CONDITIONAL / PENDING EXPLICIT ADJUDICATION", self.recovery_state["conditional_dossiers"]["audit_evidence"])
        self.assertEqual("NOT REQUIRED", self.recovery_state["conditional_dossiers"]["analytics"])
        self.assertIn("Domain count is **20**", self.open_work)
        self.assertIn("Feature Pack count remains **17**", self.open_work)
        self.assertIn("IDENTITY & ACCESS: COMPLETE / MERGED", self.open_work)
        self.assertIn("COMMUNICATIONS: REQUIRED / NOT_STARTED", self.open_work)

    def test_harden_02_is_not_authority_for_product_or_implementation(self):
        self.assertEqual("PHASE-7 GOVERNANCE / STRUCTURAL HARDENING ONLY", self.recovery_state["harden_02_scope"])
        self.assertEqual("EXCLUDED", self.recovery_state["store_cer"])
        for forbidden in (
            "Product Law",
            "Architecture Law",
            "Domain Law",
            "Roadmap Law",
            "blocking OQ",
            "Feature Pack capability",
            "Horizontal Hardening",
            "Store Blueprint / CER reuse",
            "not authority",
            "No application implementation is authorised",
        ):
            self.assertIn(forbidden, self.contract)
        for path in PROHIBITED_PRESENT_PATHS:
            self.assertFalse((ROOT / path).exists(), path)

    def test_readme_open_work_and_manifest_route_current_successor(self):
        self.assertTrue(OPEN_WORK.is_file())
        self.assertTrue(OPEN_WORK_PREDECESSOR.is_file())
        self.assertTrue(CONTRACT_PREDECESSOR.is_file())
        self.assertTrue(CONTRACT_OLDER_PREDECESSOR.is_file())
        self.assertFalse((DOCS / "02_OPEN_WORK_v1.2.40.md").exists())
        self.assertFalse((DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.1.0.md").exists())
        self.assertIn("02_OPEN_WORK_v1.2.42.md", self.readme)
        self.assertIn("HARDEN-02_CONTRACT_WORKING_v0.3.0.md", self.readme)
        self.assertIn("archive/02_OPEN_WORK_v1.2.41.md", self.readme)
        self.assertIn("archive/HARDEN-02_CONTRACT_WORKING_v0.2.0.md", self.readme)
        self.assertIn("DELIVERY_ATLAS_WORKING_v0.2.0.md", self.readme)
        self.assertIn("HARDEN-02_CONTRACT_RECOVERY_REQUIRED", self.readme)

        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertEqual("1.2.42", current["OPEN_WORK"]["semver"])
        self.assertEqual("docs/00_platform/02_OPEN_WORK_v1.2.42.md", current["OPEN_WORK"]["repository_path"])
        self.assertEqual(_sha256(OPEN_WORK), current["OPEN_WORK"]["sha256"])
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_41"]["lifecycle"])
        self.assertEqual(EXPECTED_OPEN_WORK_V1_2_41_SHA256, historical["OPEN_WORK_V1_2_41"]["sha256"])

    def test_protected_authority_atlas_and_workflow_hashes_are_unchanged(self):
        for relative_path, expected_hash in PROTECTED_UPSTREAM_HASHES.items():
            self.assertEqual(expected_hash, _sha256(ROOT / relative_path), relative_path)
        self.assertEqual(EXPECTED_ATLAS_V0_2_SHA256, _sha256(DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.0.md"))

    def test_harden_02_contract_is_not_listed_in_authority_manifest(self):
        paths = [
            entry.get("repository_path", "")
            for section in ("governing_documents", "reference_documents", "historical_documents")
            for entry in self.manifest[section]
        ]
        self.assertTrue(all("HARDEN-02" not in path for path in paths))

    @staticmethod
    def _complete_evidence(head_sha: str) -> dict[str, object]:
        main_sha = "d" * 40
        pre_ci_url = "https://github.com/JCSchoeman96/NewYou/actions/runs/1001"
        post_ci_url = "https://github.com/JCSchoeman96/NewYou/actions/runs/1002"
        return {
            "pre_merge_review": {
                "reviewed_head_sha": head_sha,
                "outcome": "PASS",
                "reviewed_head_is_certified_head": True,
                "independent_reviewer": "reviewer",
                "record_url": "https://github.com/JCSchoeman96/NewYou/pull/999#pullrequestreview-1",
            },
            "pre_merge_ci": {
                "head_sha": head_sha,
                "conclusion": "PASS",
                "workflow": "Foundation Integrity",
                "run_url": pre_ci_url,
            },
            "merge": {
                "certified_head_sha": head_sha,
                "merged_head_sha": head_sha,
                "resulting_main_sha": main_sha,
            },
            "post_merge_ci": {
                "head_sha": main_sha,
                "conclusion": "PASS",
                "workflow": "Foundation Integrity",
                "run_url": post_ci_url,
            },
            "post_merge_certification": {
                "resulting_main_sha": main_sha,
                "certified_head_sha": head_sha,
                "ci_head_sha": main_sha,
                "ci_conclusion": "PASS",
                "ci_run_url": post_ci_url,
                "outcome": "PASS",
                "independent_reviewer": "reviewer",
                "record_url": "https://github.com/JCSchoeman96/NewYou/pull/999#issuecomment-2",
            },
        }


if __name__ == "__main__":
    unittest.main()
