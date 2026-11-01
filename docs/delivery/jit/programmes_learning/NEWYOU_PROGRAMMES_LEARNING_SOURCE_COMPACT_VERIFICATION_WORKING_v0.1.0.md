# NewYou Programmes & Learning Source ↔ Compact Verification Working v0.1.0

- **Status:** PASS — MECHANICALLY CERTIFIED / NON-AUTHORITATIVE
- **Authority:** NONE
- **Implementation authority:** NONE
- **Certification basis:** exact repository bytes immediately before the compression commit

# 1. Repository provenance checked

```text
repository = JCSchoeman96/NewYou
source / merge-base main at freeze = 086ade7b28c000de1c387acb9760e5eb08bb0413
live main at certification = f856b247bce8d41b57047a432db70d2c84148627
compression parent / acceptance head = 3712fc5f412ac748d34bdc699085b0cee554f197
frozen semantic handoff commit = 8041d0fdaa53bd8f008b4bba01c576c9882df5d8
branch relation to live main before commit = 28 ahead / 1 behind
```

The compression was assembled from the canonical append-only source ledgers already tracked at the acceptance head. No historical ledger was rewritten to create the archive.

# 2. Historical byte-preservation proof

All 28 canonical source ledgers were checked **before** move against the expected Git blob SHA and byte count, moved with `git mv`, then rechecked **after** move for the same Git blob SHA, byte count and SHA-256.

| Version | Final path | Bytes | SHA-256 | Git blob SHA | Result |
|---|---|---:|---|---|---|
| `v0.1.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.1.0.md` | 52869 | `c23a92dbbc4f3873127adeca77a6fcaf8abf95324df0e0b1868b39722a448ae5` | `326fbdfe0e0cae19437c175171db5e794d539b71` | PASS |
| `v0.2.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.2.0.md` | 31686 | `a803257d809843b3d8fe0eef85786f2ec5d06cd3c3c99f3af8646f116bbd71aa` | `6313e0b5cf3277907e50ab29d975e3f419bdfc11` | PASS |
| `v0.3.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.3.0.md` | 30673 | `480dfad03605a2ea1fd1c53ce45c210b7f9b89197a3975c18dc9dea52cccbec0` | `4681b70a03b83e51c44ca1ae99e82ee1c318d195` | PASS |
| `v0.4.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.4.0.md` | 39703 | `803053362c132f18e22de4fa1667d17ffa5c2ec13f8e5b3f28163fdd2abe8139` | `85d0c650235746bc8f720450240d0f394eaa7154` | PASS |
| `v0.5.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.5.0.md` | 49700 | `06a03887f38a3c93578988870b95cc15de18ad5e506873f2c171d2db9f101a61` | `13b855c20499c7d5a1a7d4e71d4e7c19aa9e7983` | PASS |
| `v0.6.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.6.0.md` | 49646 | `457b0ad7e9ef0d47054f0adf0726cfd5de3f39d58e7ce3fea00a521167d982d6` | `9abdee3278f451c1aa5cd35f2d39440cebba358e` | PASS |
| `v0.7.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.7.0.md` | 43712 | `1fc2bd0698994c4ad25edbf6c1986b5ac8358de938310073cbdc8096d468755e` | `55e55ad04b71aa10d897df9084f1f5eaf4958c81` | PASS |
| `v0.8.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.8.0.md` | 49067 | `d7e7ed0a9ccf6c56d2de2f938c05fd0a0fdd7a11d726bf7fb15d1811256b07df` | `b473e793dbb96acb7d21e50e7c54484720d049bc` | PASS |
| `v0.9.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.9.0.md` | 47728 | `428aeccd4470c435f3ddd3b82bb279d72a7c72fe9d8d6106a82b431729df4b5b` | `2e45d5197bd9c7f61c24ef528f5018b0bd82ffde` | PASS |
| `v0.10.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.10.0.md` | 45406 | `c1a1d32e53040cd6414f189a31f4fce4f9bb7d5daa9f41b9c6b419f017807b20` | `acc231f8f11c03a2952ecdeb9b01d5143e4913ab` | PASS |
| `v0.11.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.11.0.md` | 48058 | `70d59327a8d4af905d4782e96e95873f877354f6e8190b86692ebdba5b2f3b50` | `af974ca80f0e1d5860c1f4f1cab6bb0a2fad1f5a` | PASS |
| `v0.12.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.12.0.md` | 52355 | `d11a907a280d0d1ae8b1049150193782b39638c960c81e1e6f85502957aeec13` | `b9bbde915b8d2794127448ca5fa445abcf9b542c` | PASS |
| `v0.12.1` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.12.1.md` | 4978 | `c738443bafdcfc68c29adc331ac17e389cbf1d493a1bf785ed1369d4f8681124` | `57394962ac310986ec1750c888df3825e8b2cc0f` | PASS |
| `v0.13.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.13.0.md` | 51911 | `91eb5d01ebcd3d1722b1b8680e29f773ad535623a7ec0edf865164ce76da50ec` | `db25bf622dae1e12bd875a1a7e384bbacde31465` | PASS |
| `v0.14.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.14.0.md` | 58049 | `5b700818549ff2bfe9feacbdca0b22c8530e534ed2a6aa2292d0bb6a417e6dc0` | `1569b258b591f700a7b7720fd631874892fa8d2d` | PASS |
| `v0.15.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.15.0.md` | 64461 | `2d7e30fec000d9e3cf4c7a5488ed39ba06a5d04f86781e5b6531e76a58ede1cc` | `99c65365adf6878c0bbc6d6f43da3df03b2076e7` | PASS |
| `v0.16.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.16.0.md` | 58402 | `798bfb552e309641609a2f33d490a45fd434d38417234d2441cc9283537a4729` | `3c7c70284f0157e9f84db9f3b77f7050d901f57c` | PASS |
| `v0.17.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.17.0.md` | 56100 | `24c09fa0ff14d2023d12b36132f4fadedc67d46558907d3927507f1f2a187886` | `1518438024e860dd7f10e36cef0b8cedc18cd4b5` | PASS |
| `v0.18.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.18.0.md` | 39803 | `bc1f4294d8c1336563d8c87b5197605af1d414a6c9aa180d60284bf01a3e744b` | `2699239eb92db92f0637f39e70c771af670815bb` | PASS |
| `v0.19.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.19.0.md` | 12941 | `146b203f4cedfdae0e5f38a984f4d2e4456cd55500974016e3d3e60219201699` | `3683303eac4cafd188cdba757b4e4a17237f3f4e` | PASS |
| `v0.20.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.20.0.md` | 26094 | `afd4bd1618fbf3bddd7b4d7bd9ed7bc73d98ce7715c7feb75026581e3fcb40b1` | `9d7c5223fcffd9fdf57579115fe00dc7275c80c7` | PASS |
| `v0.21.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.21.0.md` | 32533 | `a2602eeb0d86ef8103b0ab1e0ab09f977b5a915556e5621f61af7bdae4c9211d` | `1bba5a471f2d89374508af496e528a59d51803c5` | PASS |
| `v0.22.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.22.0.md` | 31137 | `1cd2b60db4a05abcebbd2380cb9925a34860f1a9887d988685e5269e9edfa540` | `f6b17b3f3502b60490093f84a0405eb068c201bd` | PASS |
| `v0.23.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.23.0.md` | 32393 | `59bfc8f5b9de7fedcd052d9db95dee5a3f68344f30d5a864c6244d62bb56f7f7` | `ad4cf822439ff890c3cd44ebc39825bd4daeb774` | PASS |
| `v0.24.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.24.0.md` | 33396 | `ea0e295fc056931183b8853867516c46cebe260d6bd804a11d74c5261c6dbe72` | `7ded256c48d07e6eb9d893e33761e298b6ad2a99` | PASS |
| `v0.25.0` | `docs/history/delivery-packs/programmes_learning/deep/archive/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.25.0.md` | 40901 | `5cf187dcc4ef45e1f5a60fa6324e46bb57b23e3930795d423caa10b54467e4d3` | `32bf9eadefdc512768cf812914f4b67766dd6e9c` | PASS |
| `v0.25.1` | `docs/delivery/jit/programmes_learning/deep/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.25.1.md` | 34254 | `9bfecbbbba17ac352545262b43b986579ab4c8ddf6c53ebc9c63a1baebe40a37` | `afc5a9f8d081f4132c252160d441cf062b68fc72` | PASS |
| `v0.25.2` | `docs/delivery/jit/programmes_learning/deep/NEWYOU_PROGRAMMES_LEARNING_PREJIT_DISCOVERY_WORKING_v0.25.2.md` | 8421 | `d3e2d269585682e8e5a0d8d4db5159aadcac1bd107f78e224f026763f003a19c` | `74096905610eb6be4b7c7c869e7d5066829550c9` | PASS |

Result: **PASS — 28/28 source ledgers preserve exact content identity.**

- `v0.1.0…v0.25.0`: archived under `deep/archive/`.
- `v0.25.1`: exact frozen semantic source under `deep/`.
- `v0.25.2`: exact acceptance/provenance source under `deep/`.
- cumulative v0.25.2 navigation/review copy: `NEWYOU_PROGRAMMES_LEARNING_PREJIT_CUMULATIVE_WORKING_REGISTER_v0.25.2.md`, 1143871 bytes, SHA-256 `560ceda55843c10b3ad275ddce09ff18ed831d1a072ba685999e225be17ecf9b`.

# 3. Identifier-definition integrity

The mechanically scanned heading definitions across the 28 exact source ledgers are:

```text
PRG-EV-001...465 = COMPLETE / contiguous
PRG-PT-001...1082 = COMPLETE / contiguous
PRG-REF-001...386 = COMPLETE / contiguous
PRG-GAP-001...011 = EXACT current identifier union
PRG-GAP-012 = ABSENT as a definition
PRG-UPD-001 = EXACT named update union
PRG-UPD-002 = ABSENT as a definition
```

Negative prose references such as “do not create PRG-GAP-012” are not counted because the scan counts identifier **definitions in Markdown headings**, not arbitrary mentions.

# 4. Compact semantic guard checks

Required positive assertions found in the compact contract (12/12):

- PASS — reusable semantic centre
- PASS — governed hierarchy
- PASS — one durable truth one owner
- PASS — current access separate from Enrolment
- PASS — source-domain evidence ownership
- PASS — fail-closed lifecycle
- PASS — Product lifecycle decision
- PASS — Product-first award correction
- PASS — Product-first withdrawn content
- PASS — scheduled Edition exceptional lifecycle
- PASS — no default Pass 25
- PASS — implementation not authorised

Forbidden unqualified overreach assertions absent (10/10):

- PASS — universal completion terminality
- PASS — universal abandonment terminality
- PASS — technical first-commit Product precedence
- PASS — Edition auto completion
- PASS — Cohort universal
- PASS — Analytics business authority
- PASS — Audit source truth
- PASS — Facebook completion authority
- PASS — universal replay substitution
- PASS — generic LMS authorisation

This is a mechanical guard, not a replacement for the completed semantic review. The semantic compression itself remains frozen; this certification adds no Product meaning.

# 5. Reference and package checks

- compact-pack local references: **PASS — zero unresolved references after manifest creation**;
- required `deep/archive/`: **present**;
- root convenience concatenation `PROGRAMMES_LEARNING_COMPACT_PACK_ALL_MARKDOWN.md`: **absent**;
- required `PACK_MANIFEST_v0.1.0.json`: **generated and JSON-validated**;
- authored/generated root-artifact whitespace check: **PASS**;
- byte-preserved `deep/` provenance: **not normalized for whitespace**; historical whitespace may remain only where exact-byte preservation requires it;
- Foundation Integrity audit: **FOUNDATION INTEGRITY AUDIT: PASS**;
- CI: **NOT CLAIMED** — this script does not treat local/static checks as CI.

# 6. Frozen-source relationship

- `v0.25.1` @ `8041d0fdaa53bd8f008b4bba01c576c9882df5d8` remains the frozen semantic handoff;
- `v0.25.2` @ `3712fc5f412ac748d34bdc699085b0cee554f197` remains acceptance/current-gap/provenance hygiene only;
- `v0.25.0` remains superseded where corrected by v0.25.1;
- broad Programmes/Learning discovery remains `WORKING_FROZEN / HANDOFF-READY`;
- default broad Pass 25 remains **NO**;
- implementation remains **NOT AUTHORISED**.

# 7. Certification conclusion

```text
SOURCE ↔ COMPACT MECHANICAL CERTIFICATION
=> PASS

HISTORICAL BYTE PRESERVATION
=> PASS

IDENTIFIER COVERAGE
=> PASS

PACK-LOCAL REFERENCES
=> PASS

NEW PRODUCT AUTHORITY
=> NONE

IMPLEMENTATION AUTHORITY
=> NONE
```
