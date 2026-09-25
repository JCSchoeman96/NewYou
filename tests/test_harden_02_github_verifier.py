from __future__ import annotations

import unittest
from pathlib import Path
from urllib.parse import urlsplit

from tools.harden_02_github_verifier import (
    DEFAULT_CONTRACT,
    _parse_contract_spec,
    verify_live_metadata,
)


REPOSITORY = "JCSchoeman96/NewYou"
PULL_REQUEST = 73
HEAD_SHA = "a" * 40
MAIN_SHA = "d" * 40


class FakeGitHubAPI:
    def __init__(self, responses):
        self.responses = responses
        self.requests = []

    def get_json(self, url_or_path):
        parsed = urlsplit(url_or_path)
        path = parsed.path
        self.requests.append(path)
        try:
            return self.responses[path], {}
        except KeyError as exc:
            raise AssertionError(f"unexpected GitHub API GET: {path}") from exc


def _fixture():
    pre_run = f"https://github.com/{REPOSITORY}/actions/runs/501"
    post_run = f"https://github.com/{REPOSITORY}/actions/runs/502"
    pre_record = f"https://github.com/{REPOSITORY}/pull/{PULL_REQUEST}#pullrequestreview-601"
    post_record = f"https://github.com/{REPOSITORY}/pull/{PULL_REQUEST}#issuecomment-602"
    evidence = {
        "pre_merge_review": {
            "reviewed_head_sha": HEAD_SHA,
            "outcome": "PASS",
            "reviewed_head_is_certified_head": True,
            "independent_review_actor": "ChatGPT / GPT-5.6 Sol",
            "attestation_poster_github_identity": "JCSchoeman96",
            "poster_equals_pr_author_disclosed": True,
            "poster_equals_pr_author": True,
            "review_actor_authored_or_modified_candidate": False,
            "substantive_reviewer_is_review_actor_not_poster": True,
            "ci_head_sha": HEAD_SHA,
            "ci_workflow": "Foundation Integrity",
            "ci_conclusion": "PASS",
            "ci_run_url": pre_run,
            "record_url": pre_record,
        },
        "pre_merge_ci": {
            "head_sha": HEAD_SHA,
            "conclusion": "PASS",
            "workflow": "Foundation Integrity",
            "run_url": pre_run,
        },
        "merge": {
            "certified_head_sha": HEAD_SHA,
            "head_sha_verified_before_merge": HEAD_SHA,
            "merged_head_sha": HEAD_SHA,
            "resulting_main_sha": MAIN_SHA,
        },
        "post_merge_ci": {
            "head_sha": MAIN_SHA,
            "conclusion": "PASS",
            "workflow": "Foundation Integrity",
            "run_url": post_run,
        },
        "post_merge_certification": {
            "resulting_main_sha": MAIN_SHA,
            "certified_head_sha": HEAD_SHA,
            "ci_head_sha": MAIN_SHA,
            "ci_conclusion": "PASS",
            "ci_run_url": post_run,
            "outcome": "PASS",
            "independent_review_actor": "ChatGPT / GPT-5.6 Sol",
            "attestation_poster_github_identity": "JCSchoeman96",
            "poster_equals_pr_author_disclosed": True,
            "poster_equals_pr_author": True,
            "review_actor_authored_or_modified_candidate": False,
            "substantive_reviewer_is_review_actor_not_poster": True,
            "record_url": post_record,
        },
    }
    responses = {
        f"/repos/{REPOSITORY}/pulls/{PULL_REQUEST}": {
            "number": PULL_REQUEST,
            "user": {"login": "JCSchoeman96"},
            "head": {"sha": HEAD_SHA},
            "base": {"ref": "main"},
            "merged": True,
            "merged_at": "2026-01-01T11:00:00Z",
            "merge_commit_sha": MAIN_SHA,
        },
        f"/repos/{REPOSITORY}/pulls/{PULL_REQUEST}/reviews": [
            {
                "id": 601,
                "user": {"login": "JCSchoeman96"},
                "commit_id": HEAD_SHA,
                "submitted_at": "2026-01-01T10:00:00Z",
                "state": "COMMENTED",
                "body": f"Review actor: ChatGPT / GPT-5.6 Sol. Outcome PASS. Candidate {HEAD_SHA}.",
            }
        ],
        f"/repos/{REPOSITORY}/issues/{PULL_REQUEST}/comments": [
            {
                "id": 602,
                "user": {"login": "JCSchoeman96"},
                "created_at": "2026-01-01T13:00:00Z",
                "body": f"Review actor: ChatGPT / GPT-5.6 Sol. Outcome PASS. Candidate {HEAD_SHA}; main {MAIN_SHA}.",
            }
        ],
        f"/repos/{REPOSITORY}/actions/runs/501": {
            "head_sha": HEAD_SHA,
            "name": "Foundation Integrity",
            "status": "completed",
            "conclusion": "success",
            "html_url": f"https://github.com/{REPOSITORY}/actions/runs/501",
            "completed_at": "2026-01-01T09:00:00Z",
        },
        f"/repos/{REPOSITORY}/actions/runs/502": {
            "head_sha": MAIN_SHA,
            "name": "Foundation Integrity",
            "status": "completed",
            "conclusion": "success",
            "html_url": f"https://github.com/{REPOSITORY}/actions/runs/502",
            "completed_at": "2026-01-01T12:00:00Z",
        },
        f"/repos/{REPOSITORY}/git/ref/heads/main": {"object": {"sha": MAIN_SHA}},
        f"/repos/{REPOSITORY}/compare/{HEAD_SHA}...{MAIN_SHA}": {"status": "ahead"},
    }
    return evidence, responses


class Harden02GitHubVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evidence_spec = _parse_contract_spec(DEFAULT_CONTRACT)

    def verify(self, evidence=None, responses=None):
        fixture_evidence, fixture_responses = _fixture()
        api = FakeGitHubAPI(responses or fixture_responses)
        result = verify_live_metadata(
            REPOSITORY,
            PULL_REQUEST,
            evidence or fixture_evidence,
            self.evidence_spec,
            api,
        )
        return result, api

    def test_live_metadata_matches_without_claiming_contract_certification(self):
        result, api = self.verify()
        self.assertEqual("LIVE_GITHUB_METADATA_RETRIEVED", result["result"])
        self.assertEqual("MATCH", result["metadata_consistency"])
        self.assertEqual("NOT_DETERMINED_BY_THIS_TOOL", result["contract_certification"])
        self.assertEqual("NONE", result["hardening_state_mutation"])
        checks = {check["name"]: check for check in result["checks"]}
        self.assertEqual("PASS", checks["candidate_head_is_ancestor_of_resulting_main"]["status"])
        self.assertEqual("PASS", checks["pre_merge_ci_run_matches_claimed_sha_workflow"]["status"])
        self.assertEqual("UNVERIFIED", checks["pre_merge_ci_github_conclusion_unmapped"]["status"])
        self.assertIn("no mapping", checks["pre_merge_ci_github_conclusion_unmapped"]["detail"])
        self.assertTrue(all(path for path in api.requests))
        self.assertTrue(all("POST" not in path for path in api.requests))

    def test_live_head_drift_fails_closed(self):
        _, responses = _fixture()
        responses[f"/repos/{REPOSITORY}/pulls/{PULL_REQUEST}"]["head"]["sha"] = "b" * 40
        result, _ = self.verify(responses=responses)
        checks = {check["name"]: check for check in result["checks"]}
        self.assertEqual("LIVE_GITHUB_METADATA_MISMATCH", result["result"])
        self.assertEqual("FAIL", checks["pull_request_identity_and_live_head"]["status"])

    def test_does_not_treat_github_review_state_as_contract_pass(self):
        _, responses = _fixture()
        responses[f"/repos/{REPOSITORY}/pulls/{PULL_REQUEST}/reviews"][0]["state"] = "APPROVED"
        result, _ = self.verify(responses=responses)
        checks = {check["name"]: check for check in result["checks"]}
        self.assertEqual("INFO", checks["pre_merge_attestation_review_state_not_interpreted_as_pass"]["status"])
        self.assertIn("does not map it to contract PASS", checks["pre_merge_attestation_review_state_not_interpreted_as_pass"]["detail"])
        self.assertEqual("NOT_DETERMINED_BY_THIS_TOOL", result["contract_certification"])

    def test_actions_conclusion_is_reported_without_mapping_to_contract_pass(self):
        _, responses = _fixture()
        responses[f"/repos/{REPOSITORY}/actions/runs/501"]["conclusion"] = "failure"
        result, _ = self.verify(responses=responses)
        checks = {check["name"]: check for check in result["checks"]}
        self.assertEqual("UNVERIFIED", checks["pre_merge_ci_github_conclusion_unmapped"]["status"])
        self.assertIn("'failure'", checks["pre_merge_ci_github_conclusion_unmapped"]["detail"])
        self.assertEqual("NOT_DETERMINED_BY_THIS_TOOL", result["contract_certification"])

    def test_wrong_pr_record_url_is_rejected(self):
        evidence, _ = _fixture()
        evidence["pre_merge_review"]["record_url"] = (
            f"https://github.com/{REPOSITORY}/pull/74#pullrequestreview-601"
        )
        result, _ = self.verify(evidence=evidence)
        checks = {check["name"]: check for check in result["checks"]}
        self.assertEqual("FAIL", checks["pre_merge_attestation_record_url"]["status"])

    def test_record_posters_must_match_live_user_and_author_disclosure(self):
        evidence, _ = _fixture()
        evidence["post_merge_certification"]["attestation_poster_github_identity"] = "someone-else"
        result, _ = self.verify(evidence=evidence)
        checks = {check["name"]: check for check in result["checks"]}
        self.assertEqual("FAIL", checks["post_merge_attestation_poster_matches_record_author"]["status"])

    def test_attestation_must_follow_ci_and_merge_timing(self):
        _, responses = _fixture()
        responses[f"/repos/{REPOSITORY}/actions/runs/501"]["completed_at"] = "2026-01-01T10:30:00Z"
        result, _ = self.verify(responses=responses)
        checks = {check["name"]: check for check in result["checks"]}
        self.assertEqual("FAIL", checks["pre_merge_ci_attestation_merge_order"]["status"])


if __name__ == "__main__":
    unittest.main()
