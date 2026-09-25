#!/usr/bin/env python3
"""Read-only GitHub metadata audit for HARDEN-02 v0.4.0 evidence.

This command is separate from Foundation Integrity CI. It checks GitHub-visible
relationships, but does not certify substantive review claims or change Open Work.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "docs/00_platform/working/HARDEN-02_CONTRACT_WORKING_v0.4.0.md"
DEFAULT_REPOSITORY = "JCSchoeman96/NewYou"
API_VERSION = "2026-03-10"
SHA_PATTERN = re.compile(r"[0-9a-f]{40}")
RECORD_URL_PATTERN = re.compile(
    r"https://github\.com/(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/pull/(?P<pr>[1-9][0-9]*)"
    r"#(?P<kind>pullrequestreview|issuecomment)-(?P<id>[1-9][0-9]*)"
)
RUN_URL_PATTERN = re.compile(
    r"https://github\.com/(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/actions/runs/(?P<id>[1-9][0-9]*)"
)

UNVERIFIED_CLAIMS = [
    "The named review actor performed substantive independent inspection of the exact diff.",
    "The review actor did not author or modify the candidate; the v0.4.0 fields do not identify a GitHub account or define a machine-verifiable authorship mapping.",
    "The attestation's prose outcome PASS is not inferred from a GitHub review state.",
    "GitHub Actions conclusion success is reported as success and is not relabeled as contract PASS.",
    "The recorded pre-merge head check occurred immediately before merge; GitHub does not expose that assertion as a structured event in the v0.4.0 evidence schema.",
    "A merge strategy may rewrite commits; ancestry metadata does not prove every meaning of merged_head_sha for all strategies.",
    "The post-merge review was a fresh substantive inspection rather than a replay of an earlier review.",
]


class ReadOnlyGitHubAPI(Protocol):
    def get_json(self, url_or_path: str) -> tuple[Any, dict[str, str]]: ...


class GitHubAPI:
    """Small GET-only client. All requests are restricted to api.github.com."""

    def __init__(self, token: str, *, timeout: float = 30.0) -> None:
        self._token = token
        self._timeout = timeout

    def get_json(self, url_or_path: str) -> tuple[Any, dict[str, str]]:
        url = (
            url_or_path
            if url_or_path.startswith("https://")
            else f"https://api.github.com{url_or_path}"
        )
        parsed = urlsplit(url)
        if parsed.scheme != "https" or parsed.netloc != "api.github.com":
            raise ValueError("GitHub API request URL must use api.github.com over HTTPS")
        request = Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self._token}",
                "X-GitHub-Api-Version": API_VERSION,
                "User-Agent": "NewYou-HARDEN-02-read-only-verifier",
            },
            method="GET",
        )
        try:
            with urlopen(request, timeout=self._timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
                headers = {key.lower(): value for key, value in response.headers.items()}
                return payload, headers
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"GitHub API GET failed: {exc}") from exc


def _parse_contract_spec(contract_path: Path) -> dict[str, Any]:
    text = contract_path.read_text(encoding="utf-8")
    start_marker = "<!-- HARDEN_02_CERTIFICATION_EVIDENCE_SPEC_START -->"
    end_marker = "<!-- HARDEN_02_CERTIFICATION_EVIDENCE_SPEC_END -->"
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise ValueError("contract must contain one certification evidence specification")
    region = text.split(start_marker, 1)[1].split(end_marker, 1)[0]
    match = re.search(r"```json\s*(\{.*?\})\s*```", region, re.DOTALL)
    if match is None:
        raise ValueError("contract certification evidence specification is missing JSON")
    value = json.loads(match.group(1), object_pairs_hook=_reject_duplicate_keys)
    if not isinstance(value, dict):
        raise ValueError("contract certification evidence specification must be an object")
    return value


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _parse_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys)


def _valid_sha(value: Any) -> bool:
    return isinstance(value, str) and SHA_PATTERN.fullmatch(value) is not None


def _record_url(value: Any, repository: str, pull_request: int) -> tuple[str, str] | None:
    if not isinstance(value, str):
        return None
    match = RECORD_URL_PATTERN.fullmatch(value)
    if match is None or match.group("repo").casefold() != repository.casefold():
        return None
    if int(match.group("pr")) != pull_request:
        return None
    return match.group("kind"), match.group("id")


def _run_id(value: Any, repository: str) -> str | None:
    if not isinstance(value, str):
        return None
    match = RUN_URL_PATTERN.fullmatch(value)
    if match is None or match.group("repo").casefold() != repository.casefold():
        return None
    return match.group("id")


def _all_items(api: ReadOnlyGitHubAPI, path: str) -> list[Any]:
    items: list[Any] = []
    page = 1
    while True:
        payload, headers = api.get_json(f"{path}?per_page=100&page={page}")
        if not isinstance(payload, list):
            raise ValueError(f"GitHub API list endpoint returned non-list data for {path}")
        items.extend(payload)
        link = headers.get("link", "")
        if re.search(r'<[^>]+>;\s*rel="next"', link):
            page += 1
            if page > 100:
                raise ValueError(f"GitHub API pagination exceeded 100 pages for {path}")
            continue
        return items


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _record(api_records: list[Any], kind: str, identifier: str) -> dict[str, Any] | None:
    for item in api_records:
        if isinstance(item, dict) and str(item.get("id")) == identifier:
            return item
    return None


def _add(checks: list[dict[str, str]], name: str, status: str, detail: str) -> None:
    checks.append({"name": name, "status": status, "detail": detail})


def _record_metadata(
    api: ReadOnlyGitHubAPI,
    repository: str,
    pull_request: int,
    record_url: Any,
    expected_poster: Any,
    expected_sha_tokens: list[str],
    prefix: str,
    checks: list[dict[str, str]],
) -> datetime | None:
    parsed = _record_url(record_url, repository, pull_request)
    if parsed is None:
        _add(checks, f"{prefix}_record_url", "FAIL", "record URL is outside the configured repository and PR")
        return None
    kind, identifier = parsed
    if kind == "pullrequestreview":
        records = _all_items(api, f"/repos/{repository}/pulls/{pull_request}/reviews")
    else:
        records = _all_items(api, f"/repos/{repository}/issues/{pull_request}/comments")
    record = _record(records, kind, identifier)
    if record is None:
        _add(checks, f"{prefix}_record_exists", "FAIL", "referenced GitHub record was not found on the PR")
        return None

    user = record.get("user") if isinstance(record.get("user"), dict) else {}
    actual_poster = user.get("login")
    poster_matches = (
        isinstance(expected_poster, str)
        and isinstance(actual_poster, str)
        and expected_poster.casefold() == actual_poster.casefold()
    )
    _add(
        checks,
        f"{prefix}_poster_matches_record_author",
        "PASS" if poster_matches else "FAIL",
        f"GitHub record author is {actual_poster!r}",
    )

    body = record.get("body") if isinstance(record.get("body"), str) else ""
    for index, token in enumerate(expected_sha_tokens, start=1):
        present = token in body
        # A PR review also has a machine-readable commit_id; the body need not repeat it.
        if kind == "pullrequestreview" and record.get("commit_id") == token:
            present = True
        _add(
            checks,
            f"{prefix}_sha_binding_{index}",
            "PASS" if present else "FAIL",
            "referenced record contains the expected SHA or its PR-review commit_id",
        )

    _add(
        checks,
        f"{prefix}_review_state_not_interpreted_as_pass",
        "INFO",
        f"GitHub record state is {record.get('state')!r}; this tool does not map it to contract PASS",
    )
    submitted = record.get("submitted_at") or record.get("created_at")
    return _parse_time(submitted)


def _check_run(
    api: ReadOnlyGitHubAPI,
    repository: str,
    evidence: Any,
    expected_sha: str,
    prefix: str,
    checks: list[dict[str, str]],
) -> datetime | None:
    if not isinstance(evidence, dict):
        _add(checks, f"{prefix}_evidence_shape", "FAIL", "CI evidence must be an object")
        return None
    run_id = _run_id(evidence.get("run_url"), repository)
    if run_id is None:
        _add(checks, f"{prefix}_run_url", "FAIL", "run URL is outside the configured repository")
        return None
    payload, _ = api.get_json(f"/repos/{repository}/actions/runs/{run_id}")
    if not isinstance(payload, dict):
        _add(checks, f"{prefix}_run_payload", "FAIL", "Actions endpoint returned a non-object")
        return None
    run_sha = payload.get("head_sha")
    run_name = payload.get("name")
    conclusion = payload.get("conclusion")
    status = payload.get("status")
    claimed_run_url = payload.get("html_url")
    metadata_matches = (
        run_sha == expected_sha
        and run_sha == evidence.get("head_sha")
        and run_name == "Foundation Integrity"
        and evidence.get("workflow") == "Foundation Integrity"
        and status == "completed"
        and claimed_run_url == evidence.get("run_url")
    )
    _add(
        checks,
        f"{prefix}_run_matches_claimed_sha_workflow",
        "PASS" if metadata_matches else "FAIL",
        f"GitHub reports head_sha={run_sha!r}, workflow={run_name!r}, status={status!r}",
    )
    _add(
        checks,
        f"{prefix}_github_conclusion_unmapped",
        "UNVERIFIED",
        f"GitHub reports conclusion={conclusion!r}; evidence claims {evidence.get('conclusion')!r}; this tool applies no mapping",
    )
    return _parse_time(payload.get("completed_at"))


def verify_live_metadata(
    repository: str,
    pull_request: int,
    evidence: Any,
    evidence_spec: dict[str, Any],
    api: ReadOnlyGitHubAPI,
) -> dict[str, Any]:
    checks: list[dict[str, str]] = []
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("repository must be OWNER/REPO")
    if not isinstance(pull_request, int) or isinstance(pull_request, bool) or pull_request < 1:
        raise ValueError("pull request number must be a positive integer")
    if not isinstance(evidence, dict):
        raise ValueError("evidence root must be an object")

    required_groups = ("pre_merge_review", "pre_merge_ci", "merge", "post_merge_ci", "post_merge_certification")
    shape_ok = True
    for group in required_groups:
        record = evidence.get(group)
        required_fields = evidence_spec.get(group)
        valid = (
            isinstance(record, dict)
            and isinstance(required_fields, list)
            and all(isinstance(field, str) and field in record for field in required_fields)
        )
        shape_ok = shape_ok and valid
        _add(checks, f"{group}_contract_fields", "PASS" if valid else "FAIL", "required v0.4.0 fields are present")
    if not shape_ok:
        return _report(checks)

    review = evidence["pre_merge_review"]
    pre_ci = evidence["pre_merge_ci"]
    merge = evidence["merge"]
    post_ci = evidence["post_merge_ci"]
    post_cert = evidence["post_merge_certification"]
    expected_sha = review.get("reviewed_head_sha")
    resulting_main_sha = merge.get("resulting_main_sha")
    if not _valid_sha(expected_sha) or not _valid_sha(resulting_main_sha):
        _add(checks, "evidence_sha_shape", "FAIL", "candidate and resulting-main SHA must be full lowercase Git SHAs")
        return _report(checks)

    _add(
        checks,
        "evidence_chain_sha_relationships",
        "PASS"
        if all(
            (
                review.get("outcome") == "PASS",
                review.get("reviewed_head_is_certified_head") is True,
                pre_ci.get("head_sha") == expected_sha,
                pre_ci.get("conclusion") == "PASS",
                pre_ci.get("workflow") == "Foundation Integrity",
                merge.get("certified_head_sha") == expected_sha,
                merge.get("head_sha_verified_before_merge") == expected_sha,
                merge.get("merged_head_sha") == expected_sha,
                post_ci.get("head_sha") == resulting_main_sha,
                post_ci.get("conclusion") == "PASS",
                post_ci.get("workflow") == "Foundation Integrity",
                post_cert.get("resulting_main_sha") == resulting_main_sha,
                post_cert.get("certified_head_sha") == expected_sha,
                post_cert.get("ci_head_sha") == resulting_main_sha,
                post_cert.get("ci_conclusion") == "PASS",
            )
        )
        else "FAIL",
        "evidence records use one candidate SHA and one resulting-main SHA",
    )

    base = f"/repos/{repository}"
    pull, _ = api.get_json(f"{base}/pulls/{pull_request}")
    if not isinstance(pull, dict):
        _add(checks, "pull_request_payload", "FAIL", "pull request endpoint returned a non-object")
        return _report(checks)
    pull_author = (pull.get("user") or {}).get("login") if isinstance(pull.get("user"), dict) else None
    live_head = (pull.get("head") or {}).get("sha") if isinstance(pull.get("head"), dict) else None
    base_branch = (pull.get("base") or {}).get("ref") if isinstance(pull.get("base"), dict) else None
    pr_ok = pull.get("number") == pull_request and live_head == expected_sha
    _add(
        checks,
        "pull_request_identity_and_live_head",
        "PASS" if pr_ok else "FAIL",
        f"GitHub reports PR #{pull.get('number')} head {live_head!r}",
    )
    _add(
        checks,
        "pull_request_targets_main",
        "PASS" if base_branch == "main" else "FAIL",
        f"GitHub reports base branch {base_branch!r}",
    )
    merged = pull.get("merged") is True and isinstance(pull.get("merged_at"), str)
    _add(
        checks,
        "pull_request_is_merged",
        "PASS" if merged else "FAIL",
        f"GitHub reports merged={pull.get('merged')!r} at {pull.get('merged_at')!r}",
    )

    for label, record in (("pre_merge", review), ("post_merge", post_cert)):
        declared_equals_author = record.get("poster_equals_pr_author")
        poster = record.get("attestation_poster_github_identity")
        actual_equals_author = (
            isinstance(poster, str)
            and isinstance(pull_author, str)
            and poster.casefold() == pull_author.casefold()
        )
        disclosure_matches = (
            record.get("poster_equals_pr_author_disclosed") is True
            and isinstance(declared_equals_author, bool)
            and declared_equals_author == actual_equals_author
        )
        _add(
            checks,
            f"{label}_poster_author_disclosure",
            "PASS" if disclosure_matches else "FAIL",
            f"PR author is {pull_author!r}; poster claim is {poster!r}, equals-author={declared_equals_author!r}",
        )

    pre_record_time = _record_metadata(
        api,
        repository,
        pull_request,
        review.get("record_url"),
        review.get("attestation_poster_github_identity"),
        [expected_sha],
        "pre_merge_attestation",
        checks,
    )
    post_record_time = _record_metadata(
        api,
        repository,
        pull_request,
        post_cert.get("record_url"),
        post_cert.get("attestation_poster_github_identity"),
        [expected_sha, resulting_main_sha],
        "post_merge_attestation",
        checks,
    )
    pre_ci_time = _check_run(api, repository, pre_ci, expected_sha, "pre_merge_ci", checks)
    post_ci_time = _check_run(api, repository, post_ci, resulting_main_sha, "post_merge_ci", checks)

    merged_at = _parse_time(pull.get("merged_at"))
    pre_order_ok = (
        pre_ci_time is not None
        and pre_record_time is not None
        and merged_at is not None
        and pre_ci_time <= pre_record_time <= merged_at
    )
    _add(
        checks,
        "pre_merge_ci_attestation_merge_order",
        "PASS" if pre_order_ok else "FAIL",
        "pre-merge CI completed before the durable attestation and both preceded merge",
    )
    post_order_ok = (
        post_ci_time is not None
        and post_record_time is not None
        and merged_at is not None
        and merged_at <= post_ci_time <= post_record_time
    )
    _add(
        checks,
        "post_merge_ci_attestation_order",
        "PASS" if post_order_ok else "FAIL",
        "merge preceded post-merge CI, which preceded the durable post-merge attestation",
    )

    ref, _ = api.get_json(f"{base}/git/ref/heads/main")
    current_main = (ref.get("object") or {}).get("sha") if isinstance(ref, dict) else None
    _add(
        checks,
        "current_main_matches_recorded_result",
        "PASS" if current_main == resulting_main_sha else "INFO",
        f"current main is {current_main!r}; evidence records {resulting_main_sha!r}",
    )
    comparison, _ = api.get_json(f"{base}/compare/{expected_sha}...{resulting_main_sha}")
    comparison_status = comparison.get("status") if isinstance(comparison, dict) else None
    ancestry_ok = comparison_status in {"ahead", "identical"}
    _add(
        checks,
        "candidate_head_is_ancestor_of_resulting_main",
        "PASS" if ancestry_ok else "FAIL",
        f"GitHub compare reports {comparison_status!r}",
    )
    merge_commit_sha = pull.get("merge_commit_sha")
    _add(
        checks,
        "pull_merge_commit_matches_recorded_result",
        "PASS" if merge_commit_sha == resulting_main_sha else "INFO",
        f"PR merge_commit_sha is {merge_commit_sha!r}; recorded resulting main is {resulting_main_sha!r}",
    )

    return _report(checks)


def _report(checks: list[dict[str, str]]) -> dict[str, Any]:
    failed = any(check["status"] == "FAIL" for check in checks)
    return {
        "result": "LIVE_GITHUB_METADATA_MISMATCH" if failed else "LIVE_GITHUB_METADATA_RETRIEVED",
        "metadata_consistency": "MISMATCH" if failed else "MATCH",
        "contract_certification": "NOT_DETERMINED_BY_THIS_TOOL",
        "hardening_state_mutation": "NONE",
        "checks": checks,
        "unverified_claims": UNVERIFIED_CLAIMS,
    }


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, required=True, help="JSON file with the five v0.4.0 evidence groups")
    parser.add_argument("--pull-request", type=int, required=True, help="expected recovery PR number")
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY, help="GitHub OWNER/REPO")
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT, help="v0.4.0 contract source")
    args = parser.parse_args(argv)

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        parser.error("set GH_TOKEN or GITHUB_TOKEN for read-only GitHub API access")
    try:
        result = verify_live_metadata(
            args.repository,
            args.pull_request,
            _parse_json(args.evidence),
            _parse_contract_spec(args.contract),
            GitHubAPI(token),
        )
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "VERIFICATION_ERROR", "detail": str(exc)}, indent=2))
        return 2
    print(json.dumps(result, indent=2))
    return 1 if result["metadata_consistency"] == "MISMATCH" else 0


if __name__ == "__main__":
    sys.exit(_main())
