# NewYou Live & Replay Evidence Index — Working v0.1.0

- **Status:** WORKING / NON-AUTHORITATIVE TRACEABILITY INDEX
- **Implementation:** NOT AUTHORISED
- **Provider-evidence revalidation date:** `2026-10-11`
- **Deep source:** `deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.1.md`
- **Purpose:** trace accepted pressure tests, upstream gaps, provider facts and historical provenance without duplicating the compact semantic contract.

## 1. Current authority evidence

Current authority was re-resolved from `docs/00_platform/README.md` and `CURRENT_AUTHORITY_MANIFEST_v1.0.0.json` at `main@086ade7b28c000de1c387acb9760e5eb08bb0413`.

| Authority | Current path |
|---|---|
| Product / North Star | `docs/00_platform/PROJECT_NORTH_STAR_AND_MVP_v1.3.0.md` |
| Platform Product Law | `docs/00_platform/00_PLATFORM_v1.6.0.md` |
| Decisions / OQs | `docs/00_platform/01_DECISIONS_v1.6.0.md` |
| Open Work | `docs/00_platform/02_OPEN_WORK_v1.2.59.md` |
| Architecture | `docs/00_platform/03_ARCHITECTURE_v1.1.1.md` |
| Domain Map | `docs/00_platform/04_DOMAIN_MAP_v1.2.0.md` |
| Roadmap | `docs/00_platform/05_ROADMAP_v1.2.0.md` |
| Operating Model | `docs/00_platform/PLATFORM_OPERATING_MODEL_v1.0.1.md` |
| FES when relevant | `docs/00_platform/FRONTEND_EXPERIENCE_SYSTEM_v1.0.1.md` |

Key routed identifiers for this pack: `FP-007`, `DEC-190`, `OQ-014`, `OQ-017`, `OQ-020`, `OQ-021`, `OQ-022`, `OQ-029`, `OQ-030`, `OQ-031`, `OQ-032`, `OQ-036`.

## 2. Canonical deep source

- **Path:** `docs/00_platform/working/live_replay/deep/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.1.md`
- **SHA-256:** `9cde26043b8e2bc53ee93b5eb5878efaa850fcc463ce980ca1c53b0b178a717c`
- **Bytes:** `84624`
- **Coverage:** Passes A–M; `LIVE-PT-001...154`; `LIVE-UPD-001...006`; `LIVE-GAP-001...014`; `LIVE-EV-001...006`.
- **Role:** complete cumulative working reasoning after Pass-M acceptance; non-authoritative.

Historical human-review cumulative source:

- `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_CUMULATIVE_WORKING_LEDGER_v0.12.0.md` — SHA-256 `e12f757253dea14738cc87d9254ffb9f2e1d001c925897a16fc55dbadce2ce3d`, 83103 bytes.

## 3. Pressure-test coverage

Exactly `LIVE-PT-001...154` are accepted working evidence after Pass-M acceptance.

| Range | Pass | Focus |
|---|---|---|
| `001...012` | A | authority/truth separation, ordinary lifecycle, initial adversarial seams |
| `013...030` | B | occurrence identity, schedule/version, access, registration, attendance |
| `031...039` | C | recording intent and raw capture |
| `040...047` | D | recording notice/permission at admission and late join |
| `048...056` | E | role/capture scope and sensitive audience material |
| `057...065` | F | post-capture purpose withdrawal |
| `066...075` | G | retention, processor deletion, reconciliation, non-resurrection |
| `076...086` | H | Full Deletion |
| `087...097` | I | replay correction/versioning/withdrawal |
| `098...109` | J | promotional derivatives |
| `110...125` | K | participant communications |
| `126...141` | L | cross-dimensional convergence and closure |
| `142...154` | M | bounded provider empirical evidence |

PT-028 is current only with the independent-review correction: cancellation is optional FP-007 scope; if included, Product authority resolves it through `LIVE-GAP-009` before Events JIT implementation.

## 4. UPD traceability

| UPD | Principal originating PTs / tranche | Compact destination |
|---|---|---|
| `LIVE-UPD-001` | PT002–003; PT012–019; PT029 | Contract §§5–6; Delta Register |
| `LIVE-UPD-002` | PT005–007; PT025–027 | Contract §8; Delta Register |
| `LIVE-UPD-003` | PT009–011 and later replay-right cases | Contract §15; Delta Register |
| `LIVE-UPD-004` | PT022 and later convergence/revocation cases | Contract §7; Delta Register |
| `LIVE-UPD-005` | PT040–047; reinforced PT048–056 | Contract §§10–11; Delta Register |
| `LIVE-UPD-006` | PT057–065; reinforced by G–J | Contract §§12–14; Delta Register |

No `LIVE-UPD-007` exists.

## 5. Gap traceability

| Gap | Source focus | Compact destination |
|---|---|---|
| `LIVE-GAP-001` | occurrence lifecycle/schedule semantics | Delta Register; related Contract section(s) |
| `LIVE-GAP-002` | OQ-020 provider path | Delta Register; related Contract section(s) |
| `LIVE-GAP-003` | OQ-021 recording/privacy + inherited retention/deletion routes | Delta Register; related Contract section(s) |
| `LIVE-GAP-004` | attendance meaning | Delta Register; related Contract section(s) |
| `LIVE-GAP-005` | replay-right policy | Delta Register; related Contract section(s) |
| `LIVE-GAP-006` | promised communications | Delta Register; related Contract section(s) |
| `LIVE-GAP-007` | future event commerce | Delta Register; related Contract section(s) |
| `LIVE-GAP-008` | in-progress access | Delta Register; related Contract section(s) |
| `LIVE-GAP-009` | registration/cancellation if included | Delta Register; related Contract section(s) |
| `LIVE-GAP-010` | weak/public attendance | Delta Register; related Contract section(s) |
| `LIVE-GAP-011` | capture/finalisation | Delta Register; related Contract section(s) |
| `LIVE-GAP-012` | capture→governed-media JIT seam | Delta Register; related Contract section(s) |
| `LIVE-GAP-013` | recording-aware provider enforcement | Delta Register; related Contract section(s) |
| `LIVE-GAP-014` | processor deletion/non-resurrection | Delta Register; related Contract section(s) |

No `LIVE-GAP-015` exists.

## 6. Accepted provider evidence — LIVE-EV-001...006

Provider facts below are current first-party documentation evidence, originally retrieved 2026-10-10 and revalidated 2026-10-11. They are not Product authority, controlled proof or gate closure.

| EV | Provider | Current first-party source(s) | Accepted factual claim | Evidence limit / route | Related PT/gap |
|---|---|---|---|---|---|
| `LIVE-EV-001` | Restream | `https://support.restream.io/en/articles/369436-stream-to-a-custom-rtmp-channel` | Custom RTMP requires paid plan; RTMPS supported; API-dependent Chat/Analytics unavailable for custom channels. | Capability evidence only; OQ-020 remains open. | PT142; GAP002 |
| `LIVE-EV-002` | Restream | `https://support.restream.io/en/articles/10599465-where-is-my-recording`; `https://support.restream.io/en/articles/4379939-download-your-recordings` | Current plan-bounded recording retention/duration; manual deletion permanent; paid recording path is a material constraint. | No documented general disable control found is **not proof none exists**. OQ-020/OQ-021 remain required. | PT142, PT150–151; GAP002/003/014 |
| `LIVE-EV-003` | Cloudflare Stream | `https://developers.cloudflare.com/stream/stream-live/start-stream-live/`; Live Input create/update API | RTMPS/SRT; recording `off|automatic`; `timeoutSeconds`; signed-URL policy; scheduled recording deletion field. | Provider mechanism only; recording/publication/access authority remains NewYou-owned. | PT146–147, PT152; GAP011/013 |
| `LIVE-EV-004` | Cloudflare Stream | `https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/create/` | Account-scoped idempotency key, ≤255 bytes, six-hour expiry, 409 on deleted-key reuse before expiry. | Bounded provider idempotency; not NewYou durable idempotency. | PT144–145; GAP002 |
| `LIVE-EV-005` | Cloudflare Stream | troubleshooting + Live Webhooks + video webhooks first-party docs | Connected input can be non-playable; live-input and video-processing evidence planes are distinct. | Controlled duplicate/reorder/loss/timing proof still required. | PT143, PT148; GAP002/011 |
| `LIVE-EV-006` | Cloudflare Stream | `https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/delete/` | Deleting Live Input retains existing recordings; recording/video deletion is separate. | Strengthens GAP014; not representation-complete deletion proof. | PT149, PT151; GAP014 |

## 7. Historical source inventory

The compression commit relocates historical source files under `deep/archive/` using the **same Git blob object**. Matching Git blob SHA is the repository-level byte-identity proof; byte counts are recorded here. SHA-256 certification is recorded in the final pack manifest where mechanically available.

| Historical source | Role | Git blob SHA | Bytes | Archive path |
|---|---|---:|---:|---|
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.1.0.md` | Pass A | `b7551c4ae975ad2478106a53ee585a97f7a43c0a` | 42726 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.1.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.2.0.md` | Pass B | `ef5b4aa538da8a9fec5dcb5e7e88c9e40ace5f53` | 37157 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.2.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.3.0.md` | Pass C | `2d02b22e0adbb754d65a2fc697fe4d62e5f34754` | 38903 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.3.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.4.0.md` | Pass D | `b40fdec497f5e873ad299dad0b002279a06d9f9d` | 34225 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.4.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.5.0.md` | Pass E | `c74cdc5c47965418a983b3556967db6e45075de9` | 36577 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.5.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.6.0.md` | Pass F | `938843dee63dfb79d86b385a562fb4e6eb712bd6` | 41633 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.6.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.7.0.md` | Pass G | `17a49bd12e9e6fde3695bee3dde4f85dd1cb4b24` | 38705 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.7.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.8.0.md` | Pass H | `b08f1c157e61d6b2980732d8d355795eeb0733bf` | 50616 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.8.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.9.0.md` | Pass I | `a858462a30a304a609069bffde1851de4f269505` | 43789 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.9.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.10.0.md` | Pass J | `0d3a12c38a28dd5483f9bf8304892bb54528128b` | 44195 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.10.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.11.0.md` | Pass K | `a0121c056824c767daf1a6ce61c13d9574384f42` | 62576 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.11.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.12.0.md` | Pass L | `ed053916bd7a632dfc7a595b7e22d868192b86bb` | 46805 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.12.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.13.0.md` | Pass M | `4602015c98ceae1c49d32048cfbc2509da79c19f` | 46405 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_DISCOVERY_WORKING_v0.13.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.1.0.md` | initial register | `c138175d9b18550505c4d1fc042d64f2d48d408a` | 20947 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.1.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.0.md` | Pass D proposed | `c2b3e0511b847237bc927df8c1557d4a05a44165` | 10371 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.1.md` | Pass D accepted | `e1486777b3035bdd797aa7671d6eeb1d2d6a6f51` | 8413 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.2.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.3.0.md` | Pass E proposed | `8d65b623cd7a692c64d3ba7cde0a7f55e0bfb6ca` | 8808 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.3.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.3.1.md` | Pass E accepted | `12085004333cee0cd1c4251a2d4e7d677760d937` | 9891 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.3.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.4.0.md` | Pass F proposed | `1c0336cde0dff8195a3436c7ab09eed89b931a86` | 11031 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.4.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.4.1.md` | Pass F accepted | `d85d12061a9348db22deaaa9e46a5601c9113988` | 8967 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.4.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.5.0.md` | Pass G proposed | `82f87ade12c31fc1c9aadd96be9aa0e4c48e697a` | 10680 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.5.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.5.1.md` | Pass G accepted | `ea1ab650abf08a5267a7d3d727235fb9177cda24` | 8925 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.5.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.6.0.md` | Pass H proposed | `ea8f26acd49c31b7246828bca96ab4c46ef8836b` | 10941 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.6.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.6.1.md` | Pass H accepted | `3ce77644496c01281883f6fa7805ad7dad8cddb2` | 10144 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.6.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.7.0.md` | Pass I proposed | `646846013e927091cc2799b445769201e603faeb` | 12549 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.7.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.7.1.md` | Pass I accepted | `1c42122e8b7a9070bd8127128ef2d1966b884458` | 9000 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.7.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.8.0.md` | Pass J proposed | `3dd5dfadbd2197f0217bd5ca3b199e9135a57b7a` | 11774 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.8.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.8.1.md` | Pass J accepted | `05471a1682791d5e13c536ba14434d5a68bef7ed` | 9954 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.8.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.9.0.md` | Pass K proposed | `919d42421d0b748d0c3cd75e7fe6d6c43ecfcb99` | 16346 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.9.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.9.1.md` | Pass K accepted | `b28840e6ee6eafff302447afa15caf5de68dac89` | 7218 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.9.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.10.0.md` | Pass L proposed | `ee675f566c0882acb2400b6b7bcfc373b9f1a00f` | 12353 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.10.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.10.1.md` | Pass L accepted/parked | `8c28074df9313e72b0a7aa7299449ad0e9a52657` | 8125 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.10.1.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.11.0.md` | independent-review correction successor | `00f867afca055f7914ca8abc6b46eccfc7e09ec2` | 9167 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.11.0.md` |
| `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.0.md` | Pass M proposed | `7ef232addd6e97e1fa8db05e63352a96e14d3dcf` | 11998 | `deep/archive/NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.0.md` |

Accepted status successor `NEWYOU_LIVE_REPLAY_PREJIT_WORKING_REGISTER_v0.12.1.md` is preserved under `deep/` as current deep status/provenance, not as a competing root semantic contract.

## 8. Provider gate state

```text
OQ-020 = OPEN
OQ-021 = OPEN
provider documentation = evidence only
controlled proof = still required
```

`OQ-036` applies according to included/promised communications. `OQ-017` remains conditional on reminders. `OQ-029...032` apply according to existing retention/deletion classifications. `OQ-014` applies to protected playback/correction propagation where relevant. `OQ-022` remains future event-commerce scope.

## 9. Phase / closure state

```text
FP-007 = NOT SELECTED / NOT PHASE-7 AUTHORISED
IMPLEMENTATION = NOT AUTHORISED
BROAD LIVE & REPLAY PRE-JIT = PARKED
PASS N = NOT JUSTIFIED BY DEFAULT
```
