from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "00_platform"

PRODUCT_SOURCE = DOCS / "00_PLATFORM_v1.6.0.md"
PRODUCT_TARGET = DOCS / "working" / "operations_pilot" / "authority_candidates" / "00_PLATFORM_v1.7.0.md"
DECISIONS_SOURCE = DOCS / "01_DECISIONS_v1.6.0.md"
DECISIONS_TARGET = DOCS / "working" / "operations_pilot" / "authority_candidates" / "01_DECISIONS_v1.7.0.md"
README = DOCS / "README.md"
MANIFEST = DOCS / "CURRENT_AUTHORITY_MANIFEST_v1.0.0.json"

PRODUCT_SCOPE = """## v1.7.0 Amendment Scope

This substantive Product successor repairs the assessment-credit consumption contradiction exposed by OPS-UPD-004. It preserves prior Product Law except for the explicit assessment-credit claim/closure/consumption refinement: first-answer save claims/holds the existing ordinary paid assessment credit without consuming it; successful digital assessment delivery consumes exactly once when the immutable governed result and paid report are durably available to the authorised participant; pre-first-answer expiry leaves the credit available unused; post-first-answer nontechnical expiry closes the credit unconsumed; and genuine technical failure preserves the same paid obligation for controlled recovery or the existing technical-failure refund path. DEC-313 records the decision. The amendment changes no methodology, scoring, annual retake interval, Domain ownership, Architecture, provider/channel policy or legal-sufficiency finding.

"""

SECTION_21R6 = """## 21R.6 Assessment-credit claim, delivery, closure and consumption

Assessment attempt/result/report state and commercial credit state are separate. An ordinary paid assessment credit may be unavailable for another attempt or sale while still commercially unconsumed.

| Assessment-credit situation | Product consequence |
|---|---|
| valid ordinary paid credit; no first answer saved | `available_unused` |
| first answer saved; attempt active/recoverable; no successful delivery | `held_unconsumed` |
| immutable governed result exists but paid report is not yet durably participant-available | `held_unconsumed` |
| immutable governed result and paid report are both durably available to the authorised participant through the approved access path | `consume_exactly_once` |
| attempt expires before first answer | `release_to_available_unused` |
| attempt expires after first answer; no successful delivery; no live genuine technical-recovery case | `close_unconsumed` |
| genuine technical failure under controlled recovery | `preserve_same_paid_obligation; recover_existing_lineage_where_present` |
| valid technical-failure refund | `close_credit_after_refund; not_delivery_or_consumption` |
| notification/provider failure after qualifying in-product delivery | `no_change_to_consumption_truth` |
| participant never opens/views an otherwise qualifying result/report | `no_change_to_consumption_truth` |

Saving the first answer claims/holds the existing ordinary paid credit; it does not consume it. Successful digital assessment delivery is the durable availability of both the immutable governed digital result and the paid digital report to the authorised participant through the approved participant-access path. Temperament owns attempt, result and report truth; Entitlements owns current assessment-credit/right truth; Identity & Access governs access assurance. Notification/provider acceptance or delivery, result creation alone, report generation alone, and participant open/read/view telemetry do not independently establish consumption.

A qualifying delivery consumes the ordinary paid assessment credit exactly once. If the attempt expires before the first answer, the attempt ends and the credit remains available unused. If it expires after the first answer without successful delivery and no genuine technical-recovery case remains live, the attempt ends and the credit closes unconsumed. Closure is not delivery or consumption. Genuine technical failure preserves one paid obligation for controlled recovery of the same lineage where one exists, or follows the existing technical-failure refund path. A valid technical-failure refund closes the affected right and is not recorded as delivery or consumption.

Refundability remains governed separately by DEC-045. The annual retake interval in DEC-034 remains separate and unchanged; this amendment does not redefine its clock. The assessment-completion metric remains separate from commercial credit consumption and cannot become Entitlements authority. Duplicate/retried submission, recovery, report availability, delivery processing or consumption signals must converge on one logical credit/result/report lineage and may not create duplicate rights, immutable results/reports or consumption.

The lifecycle labels in this section are Product semantics, not mandated database enums, tables, Ash Resources or action names.
"""

DECISIONS_SCOPE = """## v1.7.0 Amendment Scope

This substantive successor preserves prior decision history, explicitly supersedes DEC-055 with DEC-313 for ordinary paid assessment-credit claim, closure and consumption semantics, and appends DEC-313. It changes no assessment methodology, scoring, annual retake interval, Architecture, Domain ownership, provider/channel policy or legal-sufficiency conclusion.

"""

DEC313 = """## DEC-313 — Assessment-credit claim, closure and consumption
**Status:** LOCKED
An ordinary paid digital-assessment credit is not consumed when an assessment attempt is admitted or when the first answer is saved. Saving the first answer claims/holds the existing credit for the active or recoverable attempt. A claimed credit remains commercially unconsumed but is unavailable for another ordinary assessment purchase or independent attempt.

Successful digital assessment delivery occurs when the participant's immutable governed digital result and the paid digital report permitted by current Product Law have both been durably made available to the authorised participant through an approved participant-access path. Temperament owns attempt, result and report truth; Entitlements owns the assessment-credit/right state; Identity & Access governs access assurance. Participant open/read/view behaviour is not required. Notification-provider acceptance, notification delivery, result creation alone and report generation alone do not independently establish this consumption event.

The ordinary paid assessment credit is consumed exactly once at successful digital assessment delivery. If an attempt expires under DEC-056 before the first answer has been saved, the attempt ends and the credit remains available and unused. If an attempt expires after the first answer has been saved without successful delivery and the case is not still governed as a genuine technical-failure recovery, the attempt ends and the credit closes unconsumed. Closure is neither successful delivery nor consumption; ordinary refundability remains governed separately by DEC-045.

A genuine technical failure resolves through controlled recovery of the same paid obligation and existing result/report lineage where one exists, or through the existing technical-failure refund path. Recovery must not mint a duplicate credit, immutable result, report or consumption. A valid technical-failure refund closes the affected credit/right and is not recorded as delivery or consumption. Duplicate or retried submission, result/report recovery, delivery processing and consumption signals must converge on one logical paid credit/result/report lineage and may consume at most once.

DEC-034, DEC-045, DEC-054, DEC-056, DEC-057, DEC-061, DEC-066, DEC-067 and DEC-303 otherwise remain unchanged. DEC-313 supersedes DEC-055 for assessment-credit claim, closure and consumption semantics only.
"""


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise AssertionError(f"expected one occurrence of {old[:80]!r}, found {text.count(old)}")
    return text.replace(old, new, 1)


class OpsUpd004AuthorityMaterializationTests(unittest.TestCase):
    def test_pinned_sources_are_exact(self):
        self.assertEqual("bb98081841b432a5a3d5e961929acf494ac9c8ba", git_blob_sha(PRODUCT_SOURCE))
        self.assertEqual("85402cb169e095771f03482981d0691e08efb021", git_blob_sha(DECISIONS_SOURCE))

    def test_product_candidate_is_only_the_authorised_delta(self):
        source = PRODUCT_SOURCE.read_text(encoding="utf-8")
        candidate = PRODUCT_TARGET.read_text(encoding="utf-8")
        reversed_text = candidate
        for old, new in [
            ("# 00_PLATFORM_v1.6.0.md", "# 00_PLATFORM_v1.7.0.md"),
            ("- **Document status:** FROZEN PRODUCT BASELINE v1.6.0", "- **Document status:** FROZEN PRODUCT BASELINE v1.7.0"),
            ("- **Document version:** v1.6.0", "- **Document version:** v1.7.0"),
            ("- **Predecessor:** `archive/00_PLATFORM_v1.5.1.md`", "- **Predecessor:** `archive/00_PLATFORM_v1.6.0.md`"),
            ("- **SemVer transition:** `v1.5.1 → v1.6.0`", "- **SemVer transition:** `v1.6.0 → v1.7.0`"),
            ("- **Last updated:** 2026-09-30", "- **Last updated:** 2026-10-10"),
            ("- **Decision coverage:** GQ-001 through GQ-012 plus GQ-NY-001 and approved post-freeze DEC-292–DEC-312 amendments", "- **Decision coverage:** GQ-001 through GQ-012 plus GQ-NY-001 and approved post-freeze DEC-292–DEC-313 amendments"),
            ("- **Related documents:** `01_DECISIONS_v1.6.0.md`, `02_OPEN_WORK_v1.2.51.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`", "- **Related documents:** `01_DECISIONS_v1.7.0.md`, `02_OPEN_WORK_v1.2.59.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`"),
        ]:
            reversed_text = replace_once(reversed_text, new, old)
        reversed_text = replace_once(reversed_text, PRODUCT_SCOPE + "## v1.6.0 Amendment Scope\n", "## v1.6.0 Amendment Scope\n")
        reversed_text = replace_once(
            reversed_text,
            "- Saving the first answer claims/holds the existing ordinary paid assessment credit for that active or recoverable attempt; it does not consume the credit.\n- Assessment-credit availability, closure and consumption follow §21R.6 and DEC-313.",
            "- The entitlement is not consumed until the first answer is saved.\n- Once the first answer is saved, the entitlement is marked used.",
        )
        reversed_text = replace_once(reversed_text, "\n" + SECTION_21R6 + "\n# 21S. Marketing Permission and Communication Preferences\n", "\n# 21S. Marketing Permission and Communication Preferences\n")
        reversed_text = replace_once(reversed_text, "Current Product Law is v1.7.0.", "Current Product Law is v1.6.0.")
        self.assertEqual(source, reversed_text)
        self.assertNotIn("- The entitlement is not consumed until the first answer is saved.\n- Once the first answer is saved, the entitlement is marked used.", candidate)
        self.assertEqual(1, candidate.count("## 21R.6 Assessment-credit claim, delivery, closure and consumption"))

    def test_decision_candidate_is_only_the_authorised_delta(self):
        source = DECISIONS_SOURCE.read_text(encoding="utf-8")
        candidate = DECISIONS_TARGET.read_text(encoding="utf-8")
        reversed_text = candidate
        for old, new in [
            ("# 01_DECISIONS_v1.6.0.md", "# 01_DECISIONS_v1.7.0.md"),
            ("- **Document status:** FROZEN PRODUCT DECISION REGISTER v1.6.0", "- **Document status:** FROZEN PRODUCT DECISION REGISTER v1.7.0"),
            ("- **Document version:** v1.6.0", "- **Document version:** v1.7.0"),
            ("- **Predecessor:** `archive/01_DECISIONS_v1.5.0.md`", "- **Predecessor:** `archive/01_DECISIONS_v1.6.0.md`"),
            ("- **SemVer transition:** `v1.5.0 → v1.6.0`", "- **SemVer transition:** `v1.6.0 → v1.7.0`"),
            ("- **Decision coverage:** GQ-001 through GQ-012 plus GQ-NY-001 and approved post-freeze DEC-292–DEC-312 amendments", "- **Decision coverage:** GQ-001 through GQ-012 plus GQ-NY-001 and approved post-freeze DEC-292–DEC-313 amendments"),
            ("- **Last updated:** 2026-09-30", "- **Last updated:** 2026-10-10"),
            ("- **Related documents:** `00_PLATFORM_v1.6.0.md`, `02_OPEN_WORK_v1.2.51.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`", "- **Related documents:** `00_PLATFORM_v1.7.0.md`, `02_OPEN_WORK_v1.2.59.md`, `PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md`"),
        ]:
            reversed_text = replace_once(reversed_text, new, old)
        reversed_text = replace_once(reversed_text, DECISIONS_SCOPE + "## v1.6.0 Amendment Scope\n", "## v1.6.0 Amendment Scope\n")
        reversed_text = replace_once(
            reversed_text,
            "## DEC-055 — Entitlement consumption\n**Status:** SUPERSEDED BY DEC-313\nHistorical DEC-055 wording: “Do not consume the entitlement until the first answer is saved. Mark it used once the attempt begins.” Current assessment-credit claim, closure and consumption semantics follow DEC-313 and Product Law §21R.6.\n",
            "## DEC-055 — Entitlement consumption\n**Status:** LOCKED\nDo not consume the entitlement until the first answer is saved. Mark it used once the attempt begins.\n",
        )
        reversed_text = replace_once(reversed_text, "\n" + DEC313 + "\n# Open Gates\n", "\n# Open Gates\n")
        self.assertEqual(source, reversed_text)
        self.assertEqual(1, candidate.count("## DEC-313 — Assessment-credit claim, closure and consumption"))
        self.assertIn("**Status:** SUPERSEDED BY DEC-313", candidate)
        self.assertNotIn("## DEC-055 — Entitlement consumption\n**Status:** LOCKED", candidate)

    def test_candidate_preserves_owner_and_lifecycle_boundaries(self):
        product = PRODUCT_TARGET.read_text(encoding="utf-8")
        decisions = DECISIONS_TARGET.read_text(encoding="utf-8")
        for text in (product, decisions):
            self.assertIn("Temperament owns attempt, result and report truth", text)
            self.assertIn("Entitlements owns", text)
            self.assertIn("Identity & Access governs access assurance", text)
            self.assertIn("DEC-034", text)
        self.assertIn("close_unconsumed", product)
        self.assertIn("Closure is neither successful delivery nor consumption", decisions)

    def test_current_routing_remains_v1_6_until_promotion(self):
        readme = README.read_text(encoding="utf-8")
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        platform = next(item for item in manifest["governing_documents"] if item["document_id"] == "PLATFORM_BASELINE")
        decisions = next(item for item in manifest["governing_documents"] if item["document_id"] == "DECISION_REGISTER")
        self.assertEqual("00_PLATFORM_v1.6.0.md", platform["canonical_filename"])
        self.assertEqual("01_DECISIONS_v1.6.0.md", decisions["canonical_filename"])
        self.assertIn("2. `00_PLATFORM_v1.6.0.md`", readme)
        self.assertIn("3. `01_DECISIONS_v1.6.0.md`", readme)

    def test_decision_identifiers_are_contiguous_through_313_in_candidate(self):
        candidate = DECISIONS_TARGET.read_text(encoding="utf-8")
        ids = [int(value) for value in re.findall(r"^## DEC-(\d{3})\b", candidate, re.MULTILINE)]
        self.assertEqual(list(range(1, 314)), ids)


if __name__ == "__main__":
    unittest.main()
