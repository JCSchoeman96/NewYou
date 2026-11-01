from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / 'docs/00_platform/CURRENT_AUTHORITY_ROUTER_v1.0.0.json'
SUCCESSOR = 'docs/00_platform/working/FP-001_IDENTITY_RESEND_SEMANTIC_SUCCESSOR_v0.3.0.md'


class ResendContractTest(unittest.TestCase):
    def test_current_identity_route_preserves_resend_truth_and_registration_scope(self):
        routes = json.loads(ROUTER.read_text())['working_semantic_routes']
        self.assertIn(SUCCESSOR, routes)
        self.assertNotIn('docs/00_platform/working/FP-001_IDENTITY_ACCESS_JIT_DOMAIN_DOSSIER_WORKING_v0.2.0.md', routes)
        text = (ROOT / SUCCESSOR).read_text()
        for clause in (
            'private Identity-owned `ResendOperation` Ash Resource',
            '`RegistrationOperation` remains registration-only',
            'Token cleanup cannot delete or release the operation ID',
            'permanent anti-rebinding tombstone',
            'replay never supersedes a newer challenge',
            'exactly one current active verification challenge',
            'no central Audit `EvidenceObligation` or Audit durable schedule',
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, text)

    def test_p8_05_routes_to_same_owner_contract(self):
        spec = (ROOT / 'docs/execution/p8-05-registration-jit-spec.md').read_text()
        self.assertIn(SUCCESSOR, spec)
        self.assertIn('Token cleanup cannot release an already used resend operation ID', spec)


if __name__ == '__main__':
    unittest.main()
