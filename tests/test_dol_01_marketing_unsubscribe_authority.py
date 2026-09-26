from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

PREDECESSOR_SHA256 = {
    "00_PLATFORM_v1.4.1.md": "868b6a6ca81df7d4322dd534cb4387c051748cd49cdc3834e53626b49040c8ec",
    "01_DECISIONS_v1.4.1.md": "e92564c16c9ad15e8b7558ff76a509efad4310aa786c697b09b0ce2723ec4701",
    "02_OPEN_WORK_v1.2.45.md": "9bc1b0f882125153a9db9668db8f0fee1ed9b1f20f6ba8422882707a4d203087",
    "02_OPEN_WORK_v1.2.46.md": "d19ba98b486478ff8fea36b74a72b4102e8fe192a797af919318a1fc31c8c870",
    "04_DOMAIN_MAP_v1.1.1.md": "ae1b6e44e0e5da2060bcbfda46b8c280a6c7aa0e596b8feb8198cea22aa4bb42",
    "DELIVERY_ATLAS_WORKING_v0.2.1.md": "b4c27c8a314d2a9e227acd53bd69dfce0e01a2cc743535e49a45a848f135cc59",
    "DELIVERY_ATLAS_WORKING_v0.2.2.md": "2a9553cd9076333665d340c6d787a8de8bfa0f78509e6cc8b2cfb874730ab02e",
}

EXPECTED_CURRENT = {
    "PLATFORM_BASELINE": ("00_PLATFORM_v1.5.0.md", "1.5.0"),
    "DECISION_REGISTER": ("01_DECISIONS_v1.5.0.md", "1.5.0"),
    "OPEN_WORK": ("02_OPEN_WORK_v1.2.47.md", "1.2.47"),
    "DOMAIN_MAP": ("04_DOMAIN_MAP_v1.2.0.md", "1.2.0"),
    "ROADMAP": ("05_ROADMAP_v1.1.3.md", "1.1.3"),
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _table_rows(text: str, start: str, end: str) -> list[dict[str, str]]:
    if text.count(start) != 1 or text.count(end) != 1:
        raise AssertionError(f"expected one table bounded by {start} and {end}")
    section = text.split(start, 1)[1].split(end, 1)[0]
    lines = [line for line in section.splitlines() if line.strip().startswith("|")]
    cells = lambda line: [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
    headers = cells(lines[0])
    rows = []
    for line in lines[2:]:
        values = cells(line)
        if len(values) != len(headers):
            raise AssertionError(f"malformed table row: {line}")
        rows.append(dict(zip(headers, values)))
    return rows


def _current_document(manifest: dict, document_id: str) -> tuple[dict, str]:
    entry = next(row for row in manifest["governing_documents"] if row["document_id"] == document_id)
    return entry, _read(ROOT / entry["repository_path"])


def _gate_lines(text: str) -> list[str]:
    prefixes = (
        "HARDEN-02 EXECUTION:",
        "ENGINEERING STANDARDS AUTHORITY PROMOTION:",
        "FP001_RECONCILIATION_REQUIRED:",
        "COMMUNICATIONS:",
        "CONDITIONAL DOSSIERS:",
        "PHASE 7C:",
        "PROOF CLASSIFICATION:",
        "EXECUTABLE DEVELOPMENT:",
        "→ PHASE 8 ONLY AFTER DEVELOPMENT ENTRY HARD STOP PASSES",
    )
    return [line for line in text.splitlines() if line.startswith(prefixes)]


class MarketingUnsubscribeAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.product_entry, cls.product = _current_document(cls.manifest, "PLATFORM_BASELINE")
        cls.decision_entry, cls.decisions = _current_document(cls.manifest, "DECISION_REGISTER")
        cls.open_work_entry, cls.open_work = _current_document(cls.manifest, "OPEN_WORK")
        cls.domain_entry, cls.domain = _current_document(cls.manifest, "DOMAIN_MAP")
        cls.readme = _read(DOCS / "README.md")
        atlas_path = cls.manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"][0]
        cls.atlas = _read(ROOT / atlas_path)

    def test_product_actions_change_only_their_own_permission_dimension(self):
        rows = _table_rows(
            self.product,
            "<!-- NEWYOU:PRODUCT-MATRIX:MARKETING-UNSUBSCRIBE:START -->",
            "<!-- NEWYOU:PRODUCT-MATRIX:MARKETING-UNSUBSCRIBE:END -->",
        )
        actions = {row["action"]: row for row in rows}
        self.assertEqual(
            {
                "scoped_channel_category_opt_out",
                "purpose_level_marketing_withdrawal",
                "manage_communication_preferences",
                "manage_preferences_after_withdrawal",
                "explicit_marketing_permission_regrant",
                "link_accountless_contact_to_account",
                "provider_unsubscribe_evidence",
                "ambiguous_unscoped_generic_unsubscribe",
            },
            set(actions),
        )

        scoped = actions["scoped_channel_category_opt_out"]
        self.assertEqual("selected_channel_category_only", scoped["communications_preference_effect"])
        self.assertEqual("unchanged", scoped["purpose_permission_effect"])
        self.assertEqual("suppress_selected_optional_marketing_channel", scoped["optional_marketing_effect"])

        withdrawn = actions["purpose_level_marketing_withdrawal"]
        self.assertEqual("unchanged", withdrawn["communications_preference_effect"])
        self.assertEqual("withdraw_through_privacy_consent", withdrawn["purpose_permission_effect"])
        self.assertEqual("suppress_all_optional_marketing_across_channels", withdrawn["optional_marketing_effect"])
        self.assertEqual("new_explicit_privacy_consent_grant_only", withdrawn["restoration_effect"])

        preference_change = actions["manage_preferences_after_withdrawal"]
        self.assertEqual("selected_preferences_only", preference_change["communications_preference_effect"])
        self.assertEqual("remain_withdrawn", preference_change["purpose_permission_effect"])
        self.assertEqual("remain_suppressed_all_channels", preference_change["optional_marketing_effect"])
        self.assertEqual("not_a_permission_grant", preference_change["restoration_effect"])

        regrant = actions["explicit_marketing_permission_regrant"]
        self.assertEqual("unchanged", regrant["communications_preference_effect"])
        self.assertEqual("new_explicit_participant_grant_through_privacy_consent", regrant["purpose_permission_effect"])

        account_link = actions["link_accountless_contact_to_account"]
        self.assertEqual("communications_contact_and_preference_link_only", account_link["communications_preference_effect"])
        self.assertEqual("unchanged_no_create_transfer_broaden_or_restore", account_link["purpose_permission_effect"])

        provider = actions["provider_unsubscribe_evidence"]
        self.assertEqual("external_evidence_only", provider["purpose_permission_effect"])
        self.assertEqual("no_platform_permission_change", provider["optional_marketing_effect"])

        ambiguous = actions["ambiguous_unscoped_generic_unsubscribe"]
        self.assertEqual("not_permitted_without_clear_scope", ambiguous["communications_preference_effect"])
        self.assertEqual("not_permitted_without_clear_scope", ambiguous["purpose_permission_effect"])

    def test_product_decision_and_domain_map_share_one_owner_per_truth(self):
        ownership = _table_rows(
            self.domain,
            "## 4. Platform-wide business-truth ownership matrix",
            "### 4.1 Ownership interpretation",
        )
        purpose_rows = [row for row in ownership if "marketing-purpose permission" in row["Business truth"].lower()]
        preference_rows = [row for row in ownership if "marketing channel/category preference" in row["Business truth"].lower()]
        self.assertEqual(1, len(purpose_rows))
        self.assertEqual(1, len(preference_rows))
        self.assertEqual(["Privacy & Consent"], re.findall(r"\*\*(.+?)\*\*", purpose_rows[0]["Authoritative domain"]))
        self.assertEqual(["Communications"], re.findall(r"\*\*(.+?)\*\*", preference_rows[0]["Authoritative domain"]))

        actions = {
            row["action"]: row
            for row in _table_rows(
                self.product,
                "<!-- NEWYOU:PRODUCT-MATRIX:MARKETING-UNSUBSCRIBE:START -->",
                "<!-- NEWYOU:PRODUCT-MATRIX:MARKETING-UNSUBSCRIBE:END -->",
            )
        }
        self.assertEqual("Privacy & Consent", actions["purpose_level_marketing_withdrawal"]["purpose_permission_owner"])
        self.assertEqual("Communications", actions["scoped_channel_category_opt_out"]["communications_preference_owner"])

        edges = _table_rows(
            self.domain,
            "## 5. Cross-domain command/dependency doctrine",
            "## 6. Domain laws and lightweight Architecture Profiles",
        )
        comm_to_privacy = [
            row for row in edges
            if row.get("From") == "Communications" and row.get("To") == "Privacy & Consent"
        ]
        privacy_to_comm = [
            row for row in edges
            if row.get("From") == "Privacy & Consent" and row.get("To") == "Communications"
        ]
        self.assertEqual(1, len(comm_to_privacy))
        self.assertEqual(1, len(privacy_to_comm))
        self.assertIn("withdrawal request", comm_to_privacy[0]["Contract / dependency"].lower())
        self.assertIn("delivery re-checks current marketing-purpose permission", privacy_to_comm[0]["Contract / dependency"].lower())
        self.assertIn("Communications may not directly mutate Privacy & Consent persistence", self.domain)

    def test_decision_register_records_the_next_decision_without_rewriting_prior_decisions(self):
        identifiers = re.findall(r"^## DEC-(\d{3}) — ", self.decisions, re.MULTILINE)
        self.assertEqual([f"{number:03d}" for number in range(1, 305)], identifiers)
        self.assertEqual(1, self.decisions.count("## DEC-304 — Marketing unsubscribe scope and consent ownership"))
        decision = self.decisions.split("## DEC-304 —", 1)[1]
        self.assertTrue(decision.startswith(" Marketing unsubscribe scope and consent ownership"))
        self.assertIn("DEC-094", decision)
        self.assertIn("DEC-232", decision)
        self.assertIn("DEC-262", decision)
        self.assertIn("DEC-301", decision)
        self.assertIn("does not establish legal sufficiency", decision.lower())

    def test_communication_lifecycle_keeps_contact_preferences_and_permission_separate(self):
        communications = self.domain.split("### 6.15 — Communications", 1)[1].split("### 6.16 —", 1)[0]
        self.assertNotIn("mailing subscriber active/unsubscribed according to consent/state", communications)
        self.assertIn("Communications may not directly mutate Privacy & Consent persistence", communications)
        self.assertIn("provider evidence", communications.lower())
        self.assertIn("marketing consent/lawful basis", communications)

    def test_domain_dol01_provenance_routes_to_current_product_and_decision_authority(self):
        current_inputs = next(
            line.split(":", 1)[1]
            for line in self.domain.splitlines()
            if line.startswith("- **Primary inputs — current semantic authority for the v1.2.0 DOL-01 amendment:**")
        )
        self.assertEqual("1.2.0", self.domain_entry["semver"])
        self.assertIn(self.product_entry["canonical_filename"], current_inputs)
        self.assertIn("§21S", current_inputs)
        self.assertIn(self.decision_entry["canonical_filename"], current_inputs)
        self.assertIn("DEC-304", current_inputs)
        self.assertIn("# 21S. Marketing Permission and Communication Preferences", self.product)
        self.assertIn("## DEC-304 — Marketing unsubscribe scope and consent ownership", self.decisions)

        privacy = self.domain.split("### 6.2 — Privacy & Consent", 1)[1].split("### 6.3 —", 1)[0]
        privacy_basis = next(line for line in privacy.splitlines() if line.startswith("**Product Law basis:**"))
        self.assertIn("DEC-301", privacy_basis)
        self.assertIn("DEC-304", privacy_basis)

        communications = self.domain.split("### 6.15 — Communications", 1)[1].split("### 6.16 —", 1)[0]
        communications_basis = next(
            line for line in communications.splitlines() if line.startswith("**Product Law basis:**")
        )
        self.assertIn("DEC-304", communications_basis)

    def test_manifest_routes_successors_and_archives_each_predecessor_byte_identically(self):
        governing = {entry["document_id"]: entry for entry in self.manifest["governing_documents"]}
        historical = {entry["document_id"]: entry for entry in self.manifest["historical_documents"]}
        for document_id, (filename, version) in EXPECTED_CURRENT.items():
            entry = governing[document_id]
            self.assertEqual(filename, entry["canonical_filename"])
            self.assertEqual(version, entry["semver"])
            self.assertEqual(f"docs/00_platform/{filename}", entry["repository_path"])
            self.assertEqual(_sha256(ROOT / entry["repository_path"]), entry["sha256"])

        all_entries = (
            self.manifest["governing_documents"]
            + self.manifest["reference_documents"]
            + self.manifest["historical_documents"]
        )
        for filename, _version in EXPECTED_CURRENT.values():
            self.assertEqual(1, sum(entry["canonical_filename"] == filename for entry in all_entries), filename)

        for filename, expected_hash in PREDECESSOR_SHA256.items():
            archive = DOCS / "archive" / filename
            self.assertEqual(expected_hash, _sha256(archive), filename)

        for document_id, filename in (
            ("PLATFORM_BASELINE_V1_4_1", "00_PLATFORM_v1.4.1.md"),
            ("DECISION_REGISTER_V1_4_1", "01_DECISIONS_v1.4.1.md"),
            ("OPEN_WORK_V1_2_45", "02_OPEN_WORK_v1.2.45.md"),
            ("OPEN_WORK_V1_2_46", "02_OPEN_WORK_v1.2.46.md"),
            ("DOMAIN_MAP_V1_1_1", "04_DOMAIN_MAP_v1.1.1.md"),
        ):
            entry = historical[document_id]
            self.assertEqual("historical", entry["lifecycle"])
            self.assertEqual(f"docs/00_platform/archive/{filename}", entry["repository_path"])
            self.assertEqual(PREDECESSOR_SHA256[filename], entry["sha256"])

        self.assertEqual(304, self.manifest["integrity_rules"]["expected_counts"]["decisions"])
        self.assertEqual(304, self.manifest["integrity_rules"]["contiguous_ranges"]["DEC"]["end"])
        self.assertEqual(61, self.manifest["integrity_rules"]["expected_counts"]["ownership_rows"])
        self.assertEqual(17, self.manifest["integrity_rules"]["expected_counts"]["feature_packs"])

    def test_current_routes_are_current_and_old_paths_remain_archived(self):
        atlas_path = "docs/00_platform/working/DELIVERY_ATLAS_WORKING_v0.2.3.md"
        self.assertEqual(
            atlas_path,
            self.manifest["integrity_rules"]["graph_rules"]["navigation_document_paths"][0],
        )
        self.assertTrue((ROOT / atlas_path).is_file())
        archived_atlas = DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        pinned_atlas = DOCS / "working" / "DELIVERY_ATLAS_WORKING_v0.2.1.md"
        self.assertEqual(PREDECESSOR_SHA256["DELIVERY_ATLAS_WORKING_v0.2.1.md"], _sha256(archived_atlas))
        self.assertEqual(_sha256(archived_atlas), _sha256(pinned_atlas))
        self.assertEqual(
            PREDECESSOR_SHA256["DELIVERY_ATLAS_WORKING_v0.2.2.md"],
            _sha256(DOCS / "archive" / "DELIVERY_ATLAS_WORKING_v0.2.2.md"),
        )
        current_section = self.readme.split("## Default Agent Context", 1)[1].split("## Active Working Artifacts", 1)[0]
        for filename, _version in EXPECTED_CURRENT.values():
            self.assertIn(filename, current_section)

        for stale_name in (
            "00_PLATFORM_v1.4.1.md",
            "01_DECISIONS_v1.4.1.md",
            "02_OPEN_WORK_v1.2.45.md",
            "04_DOMAIN_MAP_v1.1.1.md",
        ):
            self.assertNotIn(stale_name, current_section)
        immediate_next_action = self.open_work.split("# 9. Immediate Next Action", 1)[1].split("```text", 1)[0]
        for current_name in (
            "00_PLATFORM_v1.5.0.md",
            "01_DECISIONS_v1.5.0.md",
            "04_DOMAIN_MAP_v1.2.0.md",
            "DELIVERY_ATLAS_WORKING_v0.2.3.md",
        ):
            self.assertIn(current_name, immediate_next_action)
        for stale_name in (
            "00_PLATFORM_v1.4.1.md",
            "01_DECISIONS_v1.4.1.md",
            "02_OPEN_WORK_v1.2.45.md",
            "04_DOMAIN_MAP_v1.1.1.md",
            "DELIVERY_ATLAS_WORKING_v0.2.1.md",
        ):
            self.assertNotIn(stale_name, immediate_next_action)
        for filename in PREDECESSOR_SHA256:
            self.assertIn(f"archive/{filename}", self.readme)

        source_table = self.atlas.split("## 1.1 Authority hierarchy", 1)[1].split("## 1.2 Purpose", 1)[0]
        for document_id in ("PLATFORM_BASELINE", "DECISION_REGISTER", "OPEN_WORK", "DOMAIN_MAP"):
            self.assertIn(Path(self.manifest["governing_documents"][
                next(i for i, entry in enumerate(self.manifest["governing_documents"]) if entry["document_id"] == document_id)
            ]["repository_path"]).name, source_table)
        for stale_name in (
            "00_PLATFORM_v1.4.1.md",
            "01_DECISIONS_v1.4.1.md",
            "02_OPEN_WORK_v1.2.45.md",
            "04_DOMAIN_MAP_v1.1.1.md",
        ):
            self.assertNotIn(stale_name, source_table)
        atlas_completion = self.atlas.split("## 26.18 ATLAS reconciliation", 1)[1]
        for stale_version in ("Product `v1.4.1`", "Decisions `v1.4.1`", "Domain Map `v1.1.1`", "Open Work `v1.2.45`"):
            self.assertNotIn(stale_version, atlas_completion)

    def test_downstream_gate_lines_match_the_preserved_open_work_predecessor(self):
        predecessor_path = DOCS / "archive" / "02_OPEN_WORK_v1.2.46.md"
        if not predecessor_path.is_file():
            self.fail(f"missing archived Open Work predecessor: {predecessor_path}")
        predecessor = _read(predecessor_path)
        self.assertEqual(_gate_lines(predecessor), _gate_lines(self.open_work))
        self.assertIn("DOL-01", self.open_work)
        self.assertIn("REQUIRED / DOWNSTREAM AFTER CERTIFIED ENGINEERING STANDARDS AUTHORITY PROMOTION / NOT PERFORMED", self.open_work)
        self.assertIn("HARDEN-02 EXECUTION: NEXT / AUTHORISED / NOT STARTED", self.open_work)


if __name__ == "__main__":
    unittest.main()
