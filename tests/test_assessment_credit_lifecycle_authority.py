from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"
MANIFEST_PATH = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def section(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def feature_pack_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^## (FP-\d{3})\b", text))
    result = {}
    for index, match in enumerate(matches):
        finish = matches[index + 1].start() if index + 1 < len(matches) else text.index("# 7. ", match.end())
        result[match.group(1)] = text[match.start():finish]
    return result


class AssessmentCreditLifecycleAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(read(MANIFEST_PATH))
        cls.current = {
            entry["document_id"]: entry
            for entry in cls.manifest["governing_documents"]
        }
        cls.history = {
            entry["document_id"]: entry
            for entry in cls.manifest["historical_documents"]
        }
        cls.product = read(DOCS / cls.current["PLATFORM_BASELINE"]["canonical_filename"])
        cls.decisions = read(DOCS / cls.current["DECISION_REGISTER"]["canonical_filename"])
        cls.roadmap = read(DOCS / cls.current["ROADMAP"]["canonical_filename"])
        cls.previous_roadmap = read(DOCS / "archive" / "05_ROADMAP_v1.2.1.md")
        cls.domain_map = read(DOCS / cls.current["DOMAIN_MAP"]["canonical_filename"])
        cls.open_work = read(DOCS / cls.current["OPEN_WORK"]["canonical_filename"])

    def test_first_answer_holds_the_same_credit_without_consuming_it(self):
        attempt_rules = section(
            self.product,
            "## 21B.3 Completion and attempt rules",
            "## 21B.4 Initial and future scoring",
        )
        self.assertIn("first valid answer saved", attempt_rules)
        self.assertIn("claims and holds the existing paid Assessment credit in `held_unconsumed`", attempt_rules)
        self.assertIn("It does not consume or create a credit", attempt_rules)

        lifecycle = section(
            self.product,
            "## 21R.6 Assessment-credit claim, delivery and release",
            "# 21S.",
        )
        self.assertIn("available_unused\n    ↓ valid first-answer claim\nheld_unconsumed", lifecycle)
        self.assertIn("held_unconsumed\n    ↓ successful complete paid digital Assessment delivery\nconsumed", lifecycle)
        self.assertIn("The first valid saved answer", lifecycle)
        self.assertIn("does not consume the credit or create another one", lifecycle)

    def test_only_complete_paid_delivery_with_durable_availability_consumes(self):
        lifecycle = section(
            self.product,
            "## 21R.6 Assessment-credit claim, delivery and release",
            "# 21S.",
        )
        for required in (
            "successful complete paid digital Assessment delivery",
            "durable authorised availability",
            "immutable governed result",
            "complete paid output required by §7.4 and §§21B.5–21B.11",
            "primary/secondary temperament guidance",
            "introductory personalised guidance",
            "applicable language variant under §21B.12",
        ):
            self.assertIn(required, lifecycle)
        for non_authority in (
            "computed score",
            "generated result",
            "queued delivery",
            "internal job completion",
            "Communications intent",
            "provider acceptance",
            "callback",
            "message delivery",
            "open/read/view telemetry",
            "Analytics event/state",
            "UI rendering alone",
        ):
            self.assertIn(non_authority, lifecycle)
        self.assertIn("Attempt state, result state, report state", lifecycle)
        self.assertIn("entitlement/right state, refundability and Analytics measurement remain distinct", lifecycle)

    def test_nontechnical_expiry_releases_the_same_credit_without_refund_or_replacement(self):
        lifecycle = section(
            self.product,
            "## 21R.6 Assessment-credit claim, delivery and release",
            "# 21S.",
        )
        expiry = lifecycle.split("If an attempt expires terminally", 1)[1].split("A genuine technical failure", 1)[0]
        for required in (
            "before successful complete paid delivery",
            "releases the same paid credit to `available_unused`",
            "one semantic release of the original right",
            "does not consume the credit",
            "create an automatic refund",
            "replacement/duplicate credit",
            "create a new commercial right",
            "does not close as `close_unconsumed`",
        ):
            self.assertIn(required, expiry)

        decision = section(
            self.decisions,
            "## DEC-313 — Assessment-credit claim, hold, delivery and release",
            "# Open Gates",
        )
        self.assertIn("releases the same credit to `available_unused`", decision)
        self.assertIn("no consumption, expiry-only refund, duplicate/replacement credit or `close_unconsumed` outcome", decision)

    def test_technical_failure_and_annual_retake_event_remain_distinct(self):
        lifecycle = section(
            self.product,
            "## 21R.6 Assessment-credit claim, delivery and release",
            "# 21S.",
        )
        technical = lifecycle.split("A genuine technical failure", 1)[1].split("For DEC-034", 1)[0]
        self.assertIn("separate from ordinary nontechnical expiry", technical)
        self.assertIn("paid obligation and held credit survive", technical)
        self.assertIn("recovery or reconciliation remains possible", technical)
        self.assertIn("Commerce owns the refund truth", technical)
        self.assertIn("A refund is not Assessment delivery or consumption", technical)
        self.assertIn("adds no refund-eligibility rule", technical)

        retake = lifecycle.split("For DEC-034", 1)[1].split("Temperament owns", 1)[0]
        self.assertIn("prior successful digital Assessment delivery", retake)
        for rejected_event in (
            "First answer",
            "attempt creation",
            "result generation alone",
            "notification",
            "provider activity",
            "open/read/view telemetry",
            "Analytics completion",
        ):
            self.assertIn(rejected_event, retake)
        decision = section(self.decisions, "## DEC-034 — Retake interval", "## DEC-035 — Premium reassessment")
        self.assertIn("no more than one assessment retake per year", decision)

    def test_decision_register_preserves_and_narrows_dec055_history(self):
        dec055 = section(self.decisions, "## DEC-055 — Entitlement consumption", "## DEC-056 — Attempt expiry")
        self.assertIn("**Status:** SUPERSEDED IN PART BY DEC-313", dec055)
        self.assertIn("Historical DEC-055 wording:", dec055)
        self.assertIn("DEC-313 supersedes this first-answer consumption meaning", dec055)
        self.assertIn("Other right types remain governed by their applicable current Product authority", dec055)
        self.assertEqual("current", self.current["DECISION_REGISTER"]["lifecycle"])
        self.assertTrue(self.current["DECISION_REGISTER"]["canonical_filename"].endswith("v1.8.0.md"))

        archived = self.history["DECISION_REGISTER_V1_6_0"]
        self.assertEqual("historical", archived["lifecycle"])
        archived_path = ROOT / archived["repository_path"]
        self.assertEqual(archived["sha256"], sha256(archived_path))
        self.assertIn("first answer is saved", read(archived_path))
        self.assertIn("## DEC-313 — Assessment-credit claim, hold, delivery and release", self.decisions)

    def test_domain_ownership_and_current_route_are_preserved(self):
        lifecycle = section(
            self.product,
            "## 21R.6 Assessment-credit claim, delivery and release",
            "# 21S.",
        )
        for owner_statement in (
            "Temperament owns attempt, answer, scoring/result, report and methodology/version-provenance truth",
            "Entitlements owns Assessment-credit/right state and lawful release of that same right",
            "Identity & Access owns participant identity/access assurance",
            "Commerce owns applicable payment/refund truth",
            "Communications may deliver messages but does not decide consumption",
            "Analytics and Audit may derive, measure or prove evidence but do not own Assessment-credit authority",
        ):
            self.assertIn(owner_statement, lifecycle)

        ownership = section(self.domain_map, "## 4. Platform-wide business-truth ownership matrix", "## 5.")
        self.assertRegex(ownership, r"(?m)^\| Assessment attempt/answers/raw scores/result \| \*\*Temperament\*\*")
        self.assertRegex(ownership, r"(?m)^\| Access redemption code/consumable credit \| \*\*Entitlements\*\*")
        self.assertRegex(ownership, r"(?m)^\| Purchase/payment/refund/dispute truth \| \*\*Commerce\*\*")

        self.assertEqual("1.8.0", self.current["PLATFORM_BASELINE"]["semver"])
        self.assertEqual("1.8.0", self.current["DECISION_REGISTER"]["semver"])
        self.assertIn("00_PLATFORM_v1.8.0.md", self.open_work)
        self.assertIn("01_DECISIONS_v1.8.0.md", self.open_work)
        archived_open_work = read(ROOT / "docs/00_platform/archive/02_OPEN_WORK_v1.2.65.md")
        self.assertIn("PR #113 completed OPS-UPD-002 / issue #98 and issue #98 is closed", archived_open_work)
        self.assertIn("#98 is closed", self.open_work)
        self.assertIn("#99", self.open_work)
        self.assertIn("Issue #89 remains separate", self.open_work)
        self.assertIn("Issue #89 remains separate and is not wholesale resolved", self.open_work)

    def test_roadmap_patch_changes_only_current_authority_routing(self):
        old_packs = feature_pack_sections(self.previous_roadmap)
        new_packs = feature_pack_sections(self.roadmap)
        self.assertEqual({f"FP-{index:03d}" for index in range(1, 18)}, set(new_packs))
        self.assertEqual(set(old_packs), set(new_packs))
        changed = new_packs["FP-002"].replace(
            "`PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md §§11–13`; `00_PLATFORM_v1.8.0.md §§21L.4–21L.6, 21L.13–21L.18, 21R.1–21R.2, 21R.5`; `DEC-029...DEC-050`, `DEC-258`, `DEC-268...DEC-285`, `DEC-292`, `DEC-299`, `DEC-300`, `DEC-303`, `DEC-314`.",
            "`PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md §§11–13`; `00_PLATFORM_v1.6.0.md §§21L.4–21L.6, 21L.13–21L.18, 21R.1–21R.2, 21R.5`; `DEC-029...DEC-050`, `DEC-258`, `DEC-268...DEC-285`, `DEC-292`, `DEC-299`, `DEC-300`, `DEC-303`.",
        )
        self.assertEqual(old_packs["FP-002"], changed)
        self.assertEqual(
            old_packs["FP-003"],
            new_packs["FP-003"].replace("00_PLATFORM_v1.8.0.md", "00_PLATFORM_v1.7.0.md", 1),
        )
        expected_fp001 = old_packs["FP-001"].replace(
            "**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET` — the first real authentication/session/recovery path materially exercises the accepted identity boundary; Phase 7 decides whether one proof can cover the complete path.",
            "**Anticipated Architectural Proof:** `PROBABLY_NEW_TRACER_BULLET`. This direction is provisional. Phase 7C freezes the architectural proof requirement and applicable obligations. The separate architectural proof classification gate after Phase 7C and before Phase 8 selects the final proof vehicle.",
            1,
        )
        self.assertEqual(expected_fp001, new_packs["FP-001"])
        for pack_id in old_packs.keys() - {"FP-001", "FP-002", "FP-003"}:
            self.assertEqual(old_packs[pack_id], new_packs[pack_id], pack_id)
        self.assertIn("remains unused until successful digital Assessment delivery", self.roadmap)
        self.assertEqual(17, self.manifest["integrity_rules"]["expected_counts"]["feature_packs"])

    def test_north_star_architecture_domain_and_feature_pack_count_stay_at_current_baseline(self):
        expected = {
            "PROJECT_NORTH_STAR_AND_MVP": ("1.3.0", "249f5985ff1e8971e1ac4437e4bbebd5a3db9254ab25a2238e135cb7a7ae5f4b"),
            "ARCHITECTURE_SYNTHESIS": ("1.1.1", "342d02a7946f99aca9e6683647fc3a2505901b3d0cc2d13c21d807442025f0b3"),
            "DOMAIN_MAP": ("1.2.0", "e09e14ee0a773c5855257c48685cf3a75d413c983a98d22a56b42af57dc2c078"),
        }
        for document_id, (version, digest) in expected.items():
            entry = self.current[document_id]
            self.assertEqual(version, entry["semver"])
            self.assertEqual(digest, entry["sha256"])
            self.assertEqual(digest, sha256(ROOT / entry["repository_path"]))
        self.assertEqual(17, self.manifest["integrity_rules"]["expected_counts"]["feature_packs"])


if __name__ == "__main__":
    unittest.main()
