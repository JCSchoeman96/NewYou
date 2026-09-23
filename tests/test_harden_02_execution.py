from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
OPEN_WORK = DOCS / "02_OPEN_WORK_v1.2.42.md"
OPEN_WORK_PREDECESSOR = DOCS / "archive" / "02_OPEN_WORK_v1.2.41.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"
CONTRACT = DOCS / "working" / "HARDEN-02_CONTRACT_WORKING_v0.2.0.md"
ATLAS = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
ATLAS_PREDECESSOR = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.0.md"
FP001 = DOCS / "working" / "FP-001_FEATURE_PACK_SKELETON_WORKING_v0.1.0.md"
IDENTITY = DOCS / "working" / "FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.1.0.md"

CONTRACT_SHA256 = "9fab2f79b1e5720378a6852bcda9c81aafe8564cd0866a0ea38c1242e7b34f5f"
OPEN_WORK_PREDECESSOR_SHA256 = "85dd9946cf5684b0907f49e973ef75b59541c0f265ac46d44465d1527535da62"
ATLAS_PREDECESSOR_SHA256 = "c122c0f4a903c9679529e0e65a794999dcdaf957a66fcff00df990a0644bbb7f"
FP001_SHA256 = "8719971d92f70fc2a485e5fb9b23b9d2bc897313bc697025b91bd86802ee23be"
IDENTITY_SHA256 = "f96dcbbf26cdee35ac9aded273dbfc33346bb559fd88525f41112e85c23d798b"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(text: str, start: str, end: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index)
    return text[start_index:end_index]


def _fenced_text(section: str) -> str:
    match = re.search(r"```text\n(.*?)\n```", section, re.DOTALL)
    if match is None:
        raise AssertionError("expected fenced text block")
    return match.group(1)


def _state_lines(text: str) -> list[str]:
    section = _section(text, "# 9. Immediate Next Action", "# 10. Minimal Tools")
    return [line.strip() for line in _fenced_text(section).splitlines() if line.strip()]


def _one_prefixed(lines: list[str], prefix: str) -> str:
    matches = [line for line in lines if line.startswith(prefix)]
    if len(matches) != 1:
        raise AssertionError(f"expected exactly one {prefix!r} line, found {len(matches)}: {matches}")
    return matches[0]


class Harden02ExecutionIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.open_work = OPEN_WORK.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.contract = CONTRACT.read_text(encoding="utf-8")
        cls.atlas = ATLAS.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_execution_entry_fails_closed_without_verifiable_independent_certification(self):
        self.assertEqual(CONTRACT_SHA256, _sha256(CONTRACT))
        lifecycle = _section(
            self.contract,
            "## 11. Lifecycle obligations",
            "## 12. Concurrency / idempotency / retry obligations",
        )
        self.assertIn("HARDEN-02 CONTRACT: OPEN / PENDING CERTIFICATION", lifecycle)
        self.assertIn("Independent pre-merge review", lifecycle)
        self.assertIn("independent post-merge certification", lifecycle)
        state = _state_lines(self.open_work)
        contract_state = _one_prefixed(state, "HARDEN-02 CONTRACT:")
        execution_state = _one_prefixed(state, "HARDEN-02 EXECUTION:")
        self.assertIn("OPEN / PENDING INDEPENDENT CERTIFICATION", contract_state)
        self.assertIn("not repository-verifiable", contract_state)
        self.assertIn("NOT STARTED / NOT AUTHORISED", execution_state)
        self.assertNotIn("HARDEN-02_EXECUTION_REQUIRED", state)
        self.assertNotIn("COMPLETE / CERTIFIED FOR EXECUTION ENTRY", "\n".join(state))
        self.assertNotIn("CANDIDATE COMPLETE", "\n".join(state))
        self.assertIn("b1b0431152481006bbc1eff33cc9844a1b8c1ad5", contract_state)
        self.assertIn("2599638334b761ddef8e5568d0a38c3207eef722", contract_state)
        self.assertIn("35875423226", contract_state)
    def test_i01_single_current_stage(self):
        state = _state_lines(self.open_work)
        contract_state = _one_prefixed(state, "HARDEN-02 CONTRACT:")
        execution_state = _one_prefixed(state, "HARDEN-02 EXECUTION:")
        self.assertIn("OPEN / PENDING INDEPENDENT CERTIFICATION", contract_state)
        self.assertIn("NOT STARTED / NOT AUTHORISED", execution_state)
        self.assertNotIn("HARDEN-02_EXECUTION_REQUIRED", state)
        for prefix in (
            "ENGINEERING STANDARDS AUTHORITY PROMOTION:",
            "FP001_RECONCILIATION_REQUIRED",
            "COMMUNICATIONS JIT DOMAIN DOSSIER",
        ):
            line = _one_prefixed(state, prefix)
            self.assertNotRegex(line, r"\b(?:CURRENT|NEXT)\b", line)
    def test_i02_completed_stages_stay_completed(self):
        state = _state_lines(self.open_work)
        for prefix in (
            "STAGE 1 — TARGETED PRODUCT AMENDMENT GRILL:",
            "STAGE 2 — GOVERNED PRODUCT LAW AMENDMENT:",
            "STAGE 3A.1 — PRODUCT-LAW AR-000 DELTA ANALYSIS:",
            "STAGE 3A.2 — GOVERNED AR-000 AMENDMENT:",
            "STAGE 3B — INDEPENDENT ARCHITECTURE/ENGINEERING CLASSIFICATION:",
            "ARCHITECTURE GRILL:",
            "ENGINEERING-POLICY GRILL:",
            "ARCHITECTURE AMENDMENT:",
            "DOMAIN PRESSURE TEST:",
            "DOMAIN AMENDMENT:",
            "ROADMAP SEQUENCING GRILL:",
            "ROADMAP AMENDMENT:",
            "ATLAS RECONCILIATION:",
        ):
            line = _one_prefixed(state, prefix)
            self.assertIn("COMPLETE", line)
            self.assertNotRegex(line, r"\b(?:NOT_STARTED|BLOCKED|IN_PROGRESS)\b", line)
        milestone = _one_prefixed(state, "LAST APPROVED FP-001 MILESTONE:")
        self.assertIn("PHASE 7A COMPLETE", milestone)
        self.assertIn("IDENTITY & ACCESS JIT DOMAIN DOSSIER COMPLETE / MERGED", milestone)
    def test_i03_downstream_cannot_masquerade_as_current(self):
        state = _state_lines(self.open_work)
        expectations = {
            "ENGINEERING STANDARDS AUTHORITY PROMOTION:": ("DOWNSTREAM", "NOT STARTED"),
            "FP001_RECONCILIATION_REQUIRED": ("DOWNSTREAM",),
            "COMMUNICATIONS JIT DOMAIN DOSSIER": ("DOWNSTREAM",),
            "PHASE 7C:": ("BLOCKED / NOT_STARTED",),
            "PROOF CLASSIFICATION:": ("NOT FINALISED",),
            "EXECUTABLE DEVELOPMENT:": ("BLOCKED",),
        }
        for prefix, required in expectations.items():
            line = _one_prefixed(state, prefix)
            for marker in required:
                self.assertIn(marker, line)
            self.assertNotRegex(line, r"\b(?:CURRENT|NEXT|COMPLETE / CERTIFIED)\b", line)
    def test_i04_phase7_progression_coherence(self):
        invariant = _section(self.contract, "### I-04 — Phase-7 progression coherence", "### I-05")
        sequence = [line.strip() for line in _fenced_text(invariant).splitlines() if line.strip()]
        self.assertEqual(
            [
                "Phase 7A Skeleton + Gate Manifest",
                "→ required JIT Domain Dossiers",
                "→ Final Feature Pack Contract",
                "→ proof classification",
                "→ Phase 8 only when Development Entry Hard Stop passes",
            ],
            sequence,
        )
        state = _state_lines(self.open_work)
        self.assertEqual("- COMMUNICATIONS: REQUIRED / NOT_STARTED", _one_prefixed(state, "- COMMUNICATIONS:"))
        self.assertIn("BLOCKED / NOT_STARTED", _one_prefixed(state, "PHASE 7C:"))
        self.assertEqual("PROOF CLASSIFICATION: NOT FINALISED.", _one_prefixed(state, "PROOF CLASSIFICATION:"))
        self.assertIn("BLOCKED", _one_prefixed(state, "EXECUTABLE DEVELOPMENT:"))
    def test_i05_required_communications_cannot_be_skipped(self):
        state = _state_lines(self.open_work)
        dossier = _one_prefixed(state, "- COMMUNICATIONS:")
        self.assertEqual("- COMMUNICATIONS: REQUIRED / NOT_STARTED", dossier)
        active = [
            line for line in state
            if "COMMUNICATIONS" in line.upper()
            and re.search(r"\b(?:COMPLETE|OPTIONAL|NOT REQUIRED)\b", line)
        ]
        self.assertEqual([], active)
    def test_i06_conditional_dossiers_keep_explicit_dispositions(self):
        state = _state_lines(self.open_work)
        expected = {
            "- PRIVACY & CONSENT:": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "- CONTENT & MEDIA:": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "- AUDIT & EVIDENCE:": "CONDITIONAL / PENDING EXPLICIT ADJUDICATION",
            "- ANALYTICS:": "NOT REQUIRED",
        }
        for prefix, disposition in expected.items():
            self.assertEqual(f"{prefix} {disposition}", _one_prefixed(state, prefix))
    def test_i07_phase7c_fails_closed(self):
        state = _state_lines(self.open_work)
        unresolved_required = "REQUIRED / NOT_STARTED" in _one_prefixed(state, "- COMMUNICATIONS:")
        unresolved_conditional = any(
            "PENDING EXPLICIT ADJUDICATION" in _one_prefixed(state, prefix)
            for prefix in ("- PRIVACY & CONSENT:", "- CONTENT & MEDIA:", "- AUDIT & EVIDENCE:")
        )
        self.assertTrue(unresolved_required or unresolved_conditional)
        phase7c = _one_prefixed(state, "PHASE 7C:")
        self.assertIn("BLOCKED / NOT_STARTED", phase7c)
        self.assertNotRegex(phase7c, r"\b(?:READY|COMPLETE|AUTHORISED)\b")
    def test_i08_proof_classification_is_not_finalised(self):
        state = _state_lines(self.open_work)
        self.assertIn("BLOCKED / NOT_STARTED", _one_prefixed(state, "PHASE 7C:"))
        proof = _one_prefixed(state, "PROOF CLASSIFICATION:")
        self.assertEqual("PROOF CLASSIFICATION: NOT FINALISED.", proof)
        self.assertNotRegex(proof, r"\b(?:COMPLETE|APPROVED)\b")
    def test_i09_authority_separation(self):
        state = _state_lines(self.open_work)
        active_harden = [
            _one_prefixed(state, "HARDEN-02 CONTRACT:"),
            _one_prefixed(state, "HARDEN-02 EXECUTION:"),
        ]
        for line in active_harden:
            for forbidden in (
                "Product requirement",
                "Roadmap gate",
                "blocking OQ",
                "Feature Pack",
                "Horizontal Hardening",
                "Store hardening",
                "Commerce/Entitlements hardening",
            ):
                self.assertNotIn(forbidden, line)
        self.assertIn(
            "HARDEN-02 remains governance sequencing. It is not an FP-001 dependency, Roadmap gate, Product requirement or blocking OQ.",
            self.contract,
        )
    def test_i10_pmr_reconciliation_remains_required_and_unperformed(self):
        self.assertEqual(FP001_SHA256, _sha256(FP001))
        self.assertEqual(IDENTITY_SHA256, _sha256(IDENTITY))
        state = _state_lines(self.open_work)
        fp001 = _one_prefixed(state, "FP001_RECONCILIATION_REQUIRED")
        self.assertIn("DOWNSTREAM", fp001)
        self.assertNotRegex(fp001, r"\b(?:CURRENT|NEXT|COMPLETE)\b")
        self.assertIn("FP-001 reconciliation: **NOT PERFORMED by HARDEN-02**", self.contract)
    def test_i11_implementation_stop_remains_closed(self):
        state = _state_lines(self.open_work)
        executable = _one_prefixed(state, "EXECUTABLE DEVELOPMENT:")
        self.assertIn("BLOCKED", executable)
        self.assertNotRegex(executable, r"\b(?:READY|AUTHORISED|ENABLED)\b")
        hard_stop = _section(self.open_work, "## Development Entry Hard Stop", "# 9. Immediate Next Action")
        self.assertIn(
            "Implementation remains stopped unless every Development Entry Hard Stop condition above is satisfied.",
            hard_stop,
        )
    def test_i12_full_post_harden02_route_is_ordered(self):
        section = self.contract.split("## 18. Downstream consequence", 1)[1].split("---", 1)[0]
        standards = section.index("NEXT = ENGINEERING_STANDARDS_AUTHORITY_PROMOTION_REQUIRED")
        fp001 = section.index("NEXT = FP001_RECONCILIATION_REQUIRED")
        communications = section.index("Communications JIT Domain Dossier", fp001)
        self.assertLess(standards, fp001)
        self.assertLess(fp001, communications)
        tail = section[section.index("subject to then-current authority") :]
        ordered = [
            "remaining required/conditional Phase-7B work",
            "Phase 7C",
            "proof classification",
            "Phase 8 only when Development Entry Hard Stop conditions pass",
        ]
        positions = [tail.index(marker) for marker in ordered]
        self.assertEqual(sorted(positions), positions)
        state = _state_lines(self.open_work)
        for prefix in (
            "ENGINEERING STANDARDS AUTHORITY PROMOTION:",
            "FP001_RECONCILIATION_REQUIRED",
            "COMMUNICATIONS JIT DOMAIN DOSSIER",
        ):
            self.assertNotRegex(_one_prefixed(state, prefix), r"\b(?:CURRENT|NEXT)\b")
    def test_i13_store_cer_remains_excluded(self):
        state = _state_lines(self.open_work)
        store_lines = [line for line in state if "STORE/CER" in line.upper()]
        self.assertGreaterEqual(len(store_lines), 1)
        for line in store_lines:
            self.assertRegex(line, r"(?i)(excluded|separate|H02-2)")
            self.assertNotRegex(line, r"(?i)(CURRENT|NEXT|implementation path|proof obligation|exit condition)")
        self.assertIn("Store Blueprint / CER: **EXCLUDED**", self.contract)
    def test_versioned_execution_successors_and_manifest_are_coherent(self):
        self.assertEqual(OPEN_WORK_PREDECESSOR_SHA256, _sha256(OPEN_WORK_PREDECESSOR))
        self.assertEqual(ATLAS_PREDECESSOR_SHA256, _sha256(ATLAS_PREDECESSOR))
        self.assertIn("v1.2.41 → v1.2.42", self.open_work)
        self.assertIn("v0.2.0 → v0.2.1", self.atlas)
        self.assertIn("02_OPEN_WORK_v1.2.42.md", self.readme)
        self.assertIn("DELIVERY_ATLAS_WORKING_v0.2.1.md", self.readme)

        current = {
            entry["document_id"]: entry
            for section in ("governing_documents", "reference_documents")
            for entry in self.manifest[section]
        }
        self.assertEqual("1.2.42", current["OPEN_WORK"]["semver"])
        self.assertEqual(
            "docs/00_platform/02_OPEN_WORK_v1.2.42.md",
            current["OPEN_WORK"]["repository_path"],
        )
        self.assertEqual(_sha256(OPEN_WORK), current["OPEN_WORK"]["sha256"])

        historical = {
            entry["document_id"]: entry for entry in self.manifest["historical_documents"]
        }
        self.assertEqual("historical", historical["OPEN_WORK_V1_2_41"]["lifecycle"])
        self.assertEqual(
            _sha256(OPEN_WORK_PREDECESSOR),
            historical["OPEN_WORK_V1_2_41"]["sha256"],
        )

    def test_atlas_current_source_is_not_archived_open_work(self):
        current_refs = []
        ambiguous = []
        for line_number, line in enumerate(self.atlas.splitlines(), start=1):
            refs = re.findall(r"(?:archive/)?02_OPEN_WORK_v(\d+\.\d+\.\d+)\.md", line)
            for version in refs:
                if version == "1.2.42":
                    current_refs.append((line_number, line))
                    continue
                if re.search(r"\bcurrent\b", line, re.IGNORECASE):
                    ambiguous.append((line_number, line))
                if "historical-at-freeze" not in line and "archive/02_OPEN_WORK_" not in line:
                    ambiguous.append((line_number, line))
        self.assertTrue(current_refs)
        self.assertEqual([], ambiguous)
        self.assertNotIn("current gate definitions in `02_OPEN_WORK_v1.2.28.md", self.atlas)
        self.assertNotIn("current unresolved-work context in `02_OPEN_WORK_v1.2.28.md", self.atlas)

if __name__ == "__main__":
    unittest.main()
