# SWIR README PRO Migration — Status

Documentation migration ledger for existing SWIR projects. This is **README migration progress**, not application development, release readiness or runtime verification.

Canonical standards: [SWIR README PRO v2](SWIR-README-STANDARD.md) · [SWIR Progress SVG PRO](SWIR-PROGRESS-STANDARD.md).

<!-- MIGRATION-METRICS owner=66 verified=29 queued=20 blocked=1 delegated=12 excluded=4 priority_verified=12 priority_total=13 eligibility=INCOMPLETE -->
<!-- LEGACY-METER-CLEANUP verified=9 pending=40 blocked=1 delegated=12 excluded=4 -->

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-card.svg" alt="SWIR README PRO migration overall progress — N/A while eligibility review is incomplete" />
</p>

## Run status

| Item | Current state |
|---|---|
| Started | 2026-09-17 |
| Owner repositories discovered | **66**; the first complete owner inventory is fixed below |
| Verified migrations | **29** |
| SVG rollout verified | **29** — same repositories |
| Legacy meter cleanup | **9 verified / 40 pending / 1 blocked / 12 delegated / 4 excluded** |
| Queued / qualification pending | **20** |
| Blocked | **1** — Aria2Gui; feature PR #1 remains open and edits README plus application/UI code |
| Delegated to dedicated active tasks | **12** |
| Structural exclusions recorded | **4** |
| Initial priority subset | **12 / 13 = 92.3% verified** |
| Overall migration percentage | **N/A** until every queued owner repository receives a final eligibility decision |
| Next qualification batch | `Github-README-Generator` → `watermark-remover` → `Grosz` |
| Completion policy | Final eligibility audit → every eligible repo verified or explicitly excepted → SVG + legacy-meter cleanup verified/excepted → final audit/report → disable only this migration task |

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-mini.svg" alt="Initial priority subset progress — 12 of 13 repositories verified" />
</p>

The mini graphic measures **only the initial 13-repository priority subset**. It is not the overall migration percentage. The overall card stays **N/A** while discovered repositories still need a final eligibility decision.

## Status contract

- `queued`: discovered, but qualification and/or migration work remains.
- `in_progress`: an actual migration branch/PR exists.
- `verified`: final README and required assets were read back on the default branch after appropriate checks and merge.
- `blocked`: a concrete unresolved obstacle prevents a safe migration.
- `excluded`: outside migration scope with a specific reason; never counted as migrated.
- `delegated`: another active project task owns documentation changes; never counted as this task's verified migration.

A v2 marker, uploaded banner, open PR or green source CI alone does not prove a complete migration. Verify branding, paths, truthful claims, installation, release links, visible Search Keywords, SWIR footer and Progress SVG PRO state where applicable.

## Legacy meter cleanup contract

Approved SVG progress graphics replace old character/ASCII/Unicode progress meters in maintained documentation. Plain numeric percentages, counters, tables, checklist state and protected structural markers remain.

- `verified`: current default-branch README/status material and relevant progress generator were re-read and do not contain or regenerate a legacy character meter.
- `pending`: cleanup has not yet been re-audited after the 2026-09-18 SVG-only correction.
- `blocked`: cleanup cannot safely proceed because of a concrete conflicting work item.
- `delegated`: the dedicated active project task owns cleanup to avoid competing writes.
- `excluded`: outside this migration scope.

Current cleanup-verified repositories: `Image-To-Ico`, `IPTV-checker`, `Gist_manager`, `CyptoPriceWidget`, `Matrix-Ajax-Chat`, `Ghos-DNS`, `Torrent_downloader`, `cda-pl`, `Koder`.

## Initial priority queue

| Order | Repository | State | Evidence / next step |
|---:|---|---|---|
| 1 | [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `verified` | README PR #1; SVG PR #2 → `dba8219`; main README/progress assets read back. |
| 2 | [IPTV-checker](https://github.com/Swir/IPTV-checker) | `verified` | PR #2 → `c1b113e`; PR CI passed; main README/progress assets read back. |
| 3 | [Gist_manager](https://github.com/Swir/Gist_manager) | `verified` | PR #3 → `c22fde0`; PR CI passed; main README/progress assets read back. |
| 4 | [WojThom](https://github.com/Swir/WojThom) | `verified` | PR #8 → `ba38c17`; main README/card read back; app workflows path-filtered. |
| 5 | [Aria2Gui](https://github.com/Swir/Aria2Gui) | `blocked` | Feature PR #1 remains open and edits README + application/UI files; re-audit after it is resolved. |
| 6 | [PowerBookmark](https://github.com/Swir/PowerBookmark) | `verified` | PR #1 → `64be655`; README v2 + SVG PRO read back. |
| 7 | [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `verified` | PR #1 → `1639025`; README v2 + SVG PRO read back. |
| 8 | [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `verified` | PR #1 → `5283cc87`; README/card read back; unsupported AI-evasion claims removed. |
| 9 | [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `verified` | PR #4 → `714e44bb`; CI passed Python 3.10–3.14 + Windows smoke. |
| 10 | [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `verified` | PR #4 → `3d996ef9`; CI passed Python 3.10–3.14 + Windows GUI smoke. |
| 11 | [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `verified` | PR #4 → `5402a9d`; CI passed Python 3.10–3.14 + Windows GUI smoke. |
| 12 | [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `verified` | PR #1 → `c640e8f`; Windows workflow passed; truthful N/A product progress. |
| 13 | [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `verified` | PR #1 → `50f2d2a`; Windows tests/build/EXE smoke; progress 6/7 from STATUS.md. |

## Complete owner inventory snapshot

This is the fixed 66-repository owner discovery snapshot. `queued` entries still require content, fork, safety, legal and project-state qualification before the final eligible-migration denominator can be closed.

| Repository | Default branch | State | Note |
|---|---|---|---|
| [Hex-kolor](https://github.com/Swir/Hex-kolor) | `main` | `verified` | README v2 + SVG verified; PR #1 → `b0971040` |
| [swir.github.io](https://github.com/Swir/swir.github.io) | `main` | `excluded` | portfolio/status site, not a README migration target |
| [Aria2Gui](https://github.com/Swir/Aria2Gui) | `main` | `blocked` | feature PR #1 changes README + application/UI code |
| [Driver-tool](https://github.com/Swir/Driver-tool) | `main` | `verified` | PR #1 → `977c05ec` |
| [Youtube-VLC](https://github.com/Swir/Youtube-VLC) | `main` | `verified` | PR #3 → `6bc578f1`; CI passed |
| [Spamer](https://github.com/Swir/Spamer) | `main` | `verified` | PR #1 → `4e5773a`; controlled-use safety framing |
| [plugin.swir](https://github.com/Swir/plugin.swir) | `master` | `excluded` | placeholder only; no source/config/release |
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `main` | `verified` | README/SVG verified; cleanup re-audited |
| [Transformer-3-Pro-T303UA-i5-6200-hackintosh](https://github.com/Swir/Transformer-3-Pro-T303UA-i5-6200-hackintosh) | `main` | `verified` | PR #3 → `20a65a5` |
| [Tank-Revival-Overdrive](https://github.com/Swir/Tank-Revival-Overdrive) | `main` | `delegated` | dedicated active development task |
| [XBookmark](https://github.com/Swir/XBookmark) | `main` | `verified` | main `7fd4019`; README v2 + SVG PRO |
| [Worker-Time-list-generator](https://github.com/Swir/Worker-Time-list-generator) | `main` | `verified` | main `c685c1a`; CI passed |
| [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `main` | `verified` | PR #1 → `1639025` |
| [keygenerator](https://github.com/Swir/keygenerator) | `main` | `verified` | main `3671502`; safety-reviewed synthetic string generator |
| [WojThom](https://github.com/Swir/WojThom) | `main` | `verified` | PR #8 → `ba38c17` |
| [Y6-gamestick](https://github.com/Swir/Y6-gamestick) | `main` | `excluded` | empty repository; do not invent a product |
| [SwirTube](https://github.com/Swir/SwirTube) | `main` | `verified` | PR #1 → `ab1a668` |
| [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `main` | `verified` | PR #4 → `5402a9d` |
| [Swir](https://github.com/Swir/Swir) | `main` | `excluded` | profile repo; only migration standards/ledger/tooling maintained here |
| [File.io_Downloaderup](https://github.com/Swir/File.io_Downloaderup) | `main` | `verified` | PR #1 → `bc40f89` |
| [Nes_New_Life](https://github.com/Swir/Nes_New_Life) | `main` | `delegated` | dedicated active development task |
| [TimeListe-Generator](https://github.com/Swir/TimeListe-Generator) | `main` | `verified` | PR #1 → `ee6839a` |
| [CyptoPriceWidget](https://github.com/Swir/CyptoPriceWidget) | `main` | `verified` | PR #4 → `489f88d`; cleanup verified |
| [Matrix-Ajax-Chat](https://github.com/Swir/Matrix-Ajax-Chat) | `main` | `verified` | PR #3 → `51f7ced`; cleanup verified |
| [Ghos-DNS](https://github.com/Swir/Ghos-DNS) | `main` | `verified` | PR #1 → `5ba3e21`; cleanup verified |
| [Torrent_downloader](https://github.com/Swir/Torrent_downloader) | `main` | `verified` | PR #1 → `efca9a1`; README v2 + SVG-only N/A progress + deterministic check read back; cleanup verified |
| [cda-pl](https://github.com/Swir/cda-pl) | `main` | `verified` | PR #1 → `2c8f0a3`; lawful-use scope verified; README v2 + SVG-only N/A progress read back; cleanup verified |
| [Koder](https://github.com/Swir/Koder) | `main` | `verified` | PR #1 → `310c9d7`; XOR security limits and v1.0.0 release documented; cleanup verified |
| [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `main` | `verified` | PR #1 → `50f2d2a`; 1.0 gate SVG from STATUS.md 6/7 |
| [Gist_manager](https://github.com/Swir/Gist_manager) | `main` | `verified` | PR #3 → `c22fde0`; cleanup verified |
| [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `main` | `verified` | PR #1 → `c640e8f` |
| [Github-README-Generator](https://github.com/Swir/Github-README-Generator) | `main` | `queued` | qualification/readme audit pending |
| [watermark-remover](https://github.com/Swir/watermark-remover) | `main` | `queued` | qualification/readme audit pending |
| [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `main` | `verified` | PR #4 → `3d996ef9` |
| [Grosz](https://github.com/Swir/Grosz) | `main` | `queued` | qualification/readme audit pending |
| [Py-Converter-to-exe](https://github.com/Swir/Py-Converter-to-exe) | `main` | `queued` | qualification/readme audit pending |
| [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `main` | `verified` | PR #1 → `5283cc87` |
| [Image-to-txt](https://github.com/Swir/Image-to-txt) | `main` | `queued` | qualification/readme audit pending |
| [Titanium-APK-Bulider](https://github.com/Swir/Titanium-APK-Bulider) | `main` | `queued` | qualification/readme audit pending |
| [czatpythom](https://github.com/Swir/czatpythom) | `main` | `queued` | qualification/readme audit pending |
| [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `main` | `verified` | PR #4 → `714e44bb` |
| [NeonShift-X](https://github.com/Swir/NeonShift-X) | `main` | `queued` | qualification/readme audit pending |
| [IPTV-checker](https://github.com/Swir/IPTV-checker) | `main` | `verified` | PR #2 → `c1b113e`; cleanup verified |
| [ASCITEXT](https://github.com/Swir/ASCITEXT) | `main` | `queued` | qualification/readme audit pending |
| [Github_Webste](https://github.com/Swir/Github_Webste) | `main` | `queued` | qualification/readme audit pending |
| [Dreambox-scaner](https://github.com/Swir/Dreambox-scaner) | `main` | `queued` | qualification/readme audit pending |
| [Torrent_downloaderv2](https://github.com/Swir/Torrent_downloaderv2) | `main` | `queued` | qualification/readme audit pending |
| [MacTrix](https://github.com/Swir/MacTrix) | `main` | `queued` | qualification/readme audit pending |
| [PowerBookmark](https://github.com/Swir/PowerBookmark) | `main` | `verified` | PR #1 → `64be655` |
| [Dragon-DiskForge](https://github.com/Swir/Dragon-DiskForge) | `main` | `delegated` | dedicated active development task |
| [Konofix](https://github.com/Swir/Konofix) | `main` | `delegated` | dedicated active development task |
| [check-out-of-hell](https://github.com/Swir/check-out-of-hell) | `main` | `delegated` | dedicated active development task |
| [xADKiller](https://github.com/Swir/xADKiller) | `main` | `delegated` | dedicated active development task |
| [SWIR_OS](https://github.com/Swir/SWIR_OS) | `main` | `delegated` | dedicated active development task |
| [Czateria_PLUS_Android](https://github.com/Swir/Czateria_PLUS_Android) | `main` | `queued` | qualification/readme audit pending |
| [Matrix-czat-pythom](https://github.com/Swir/Matrix-czat-pythom) | `main` | `queued` | qualification/readme audit pending |
| [KaliPhoneStudio](https://github.com/Swir/KaliPhoneStudio) | `main` | `delegated` | dedicated active development task |
| [SwirEngine](https://github.com/Swir/SwirEngine) | `main` | `delegated` | dedicated active development task |
| [GTT](https://github.com/Swir/GTT) | `main` | `delegated` | dedicated active development task |
| [Ryzen-5-5600G-A320M-](https://github.com/Swir/Ryzen-5-5600G-A320M-) | `main` | `queued` | qualification/readme audit pending |
| [Procent-calkulator](https://github.com/Swir/Procent-calkulator) | `main` | `queued` | qualification/readme audit pending |
| [Swirui](https://github.com/Swir/Swirui) | `main` | `delegated` | dedicated active development task |
| [Ghost-APK-Builder](https://github.com/Swir/Ghost-APK-Builder) | `main` | `queued` | qualification/readme audit pending |
| [CrossAim_power](https://github.com/Swir/CrossAim_power) | `main` | `queued` | qualification/readme audit pending |
| [SwirPhoneOS](https://github.com/Swir/SwirPhoneOS) | `main` | `delegated` | dedicated active development task |
| [Multichain-Tracker](https://github.com/Swir/Multichain-Tracker) | `main` | `queued` | qualification/readme audit pending |

State totals: **29 verified + 20 queued + 1 blocked + 12 delegated + 4 excluded = 66 owner repositories**.

## Work owned by other active tasks

The following remain delegated rather than edited by this migration task: `SWIR_OS`, `SwirEngine`, `Swirui`, `SwirPhoneOS`, `KaliPhoneStudio`, `Dragon-DiskForge`, `GTT`, `Tank-Revival-Overdrive`, `Nes_New_Life`, `check-out-of-hell`, `Konofix` and `xADKiller`.

Their README/SVG/legacy-meter compliance may be audited, but documentation edits remain with their dedicated task while it is active to avoid competing branches and stale rewrites.

## Verified migrations

| Repository | Merge / evidence | README v2 | SVG PRO | Legacy meter cleanup | Verification note |
|---|---|---:|---:|---:|---|
| Image-To-Ico | README PR #1; SVG PR #2 → `dba8219` | ✅ | ✅ | ✅ | main README + generator re-audited 2026-09-18 |
| IPTV-checker | PR #2 → `c1b113e` | ✅ | ✅ | ✅ | migration CI passed; main README + generator re-audited 2026-09-18 |
| Gist_manager | PR #3 → `c22fde0` | ✅ | ✅ | ✅ | migration CI passed; main README + generator re-audited 2026-09-18 |
| WojThom | PR #8 → `ba38c17` | ✅ | ✅ | ⏳ | cleanup re-audit pending |
| PowerBookmark | PR #1 → `64be655` | ✅ | ✅ | ⏳ | cleanup re-audit pending |
| InfoPulse-PL | PR #1 → `1639025` | ✅ | ✅ | ⏳ | cleanup re-audit pending |
| WAV-to-MP3-converter | PR #1 → `5283cc87` | ✅ | ✅ | ⏳ | cleanup re-audit pending |
| PolSilver_Bluetooth | PR #4 → `714e44bb` | ✅ | ✅ | ⏳ | CI passed Python 3.10–3.14 + Windows smoke |
| FASTIPTVPlayer | PR #4 → `3d996ef9` | ✅ | ✅ | ⏳ | CI passed Python 3.10–3.14 + Windows GUI smoke |
| Matrix_Windows_Commander | PR #4 → `5402a9d` | ✅ | ✅ | ⏳ | CI passed Python 3.10–3.14 + Windows GUI smoke |
| BackgroundPXR | PR #1 → `c640e8f` | ✅ | ✅ | ⏳ | Windows workflow passed |
| SwirPhotoClean | PR #1 → `50f2d2a` | ✅ | ✅ | ⏳ | Windows tests/build/EXE smoke; STATUS.md 6/7 gate |
| Hex-kolor | PR #1 → `b0971040` | ✅ | ✅ | ⏳ | no PR CI workflow |
| Driver-tool | PR #1 → `977c05ec` | ✅ | ✅ | ⏳ | simulation-only update documented |
| Youtube-VLC | PR #3 → `6bc578f1` | ✅ | ✅ | ⏳ | CI passed Python 3.10–3.14 + Windows GUI smoke |
| Spamer | PR #1 → `4e5773a` | ✅ | ✅ | ⏳ | controlled-use safety framing; no PR CI workflow |
| Transformer-3-Pro-T303UA-i5-6200-hackintosh | PR #3 → `20a65a5` | ✅ | ✅ | ⏳ | hardware/release facts preserved |
| XBookmark | main `7fd4019` | ✅ | ✅ | ⏳ | channel manifests audited |
| Worker-Time-list-generator | main `c685c1a` | ✅ | ✅ | ⏳ | CI passed; v3.1.0 assets verified |
| keygenerator | main `3671502` | ✅ | ✅ | ⏳ | source safety-reviewed; v1.0.0 assets verified |
| SwirTube | PR #1 → `ab1a668` | ✅ | ✅ | ⏳ | source/releases audited |
| File.io_Downloaderup | PR #1 → `bc40f89` | ✅ | ✅ | ⏳ | release-only workflow |
| TimeListe-Generator | PR #1 → `ee6839a` | ✅ | ✅ | ⏳ | v5 source/release audited |
| CyptoPriceWidget | PR #4 → `489f88d` | ✅ | ✅ | ✅ | CI passed; final README/card/generator read back |
| Matrix-Ajax-Chat | PR #3 → `51f7ced` | ✅ | ✅ | ✅ | CI passed; final README/card read back |
| Ghos-DNS | PR #1 → `5ba3e21` | ✅ | ✅ | ✅ | no CI workflow; docs/XML/read-back validation |
| Torrent_downloader | PR #1 → `efca9a1` | ✅ | ✅ | ✅ | source/release audited; no PR CI run; local docs/SVG/generator check passed; final main read back |
| cda-pl | PR #1 → `2c8f0a3` | ✅ | ✅ | ✅ | lawful-use/source audit; no PR CI workflow; local docs/SVG/generator check passed; final main read back |
| Koder | PR #1 → `310c9d7` | ✅ | ✅ | ✅ | source/release/workflow audited; no PR CI run; local docs/SVG/generator check passed; final main read back |

## Exclusions added by qualification

- `plugin.swir`: placeholder README only; no source, release or configuration files. No speculative product was invented.
- `Y6-gamestick`: empty repository; no speculative product was invented.
- `swir.github.io`: portfolio/status site, intentionally outside this migration.
- `Swir/Swir`: profile repository; only standards, migration ledger and migration tooling are maintained here.

## Blockers

### Aria2Gui

`Aria2Gui` still has open [feature PR #1](https://github.com/Swir/Aria2Gui/pull/1), which modifies `README.md` and application/UI files. It remains intentionally **blocked** for this documentation-only migration to avoid overwriting concurrent feature work.

Required action: let the owning feature work resolve that PR; then fetch fresh `main`, re-audit the resulting README/source/release state and perform README v2 + SVG PRO migration from that state.

## Execution log

| Date | Work actually performed | Result |
|---|---|---|
| 2026-09-17 | Created canonical migration ledger and audited the initial priority repositories. | Queue and truthfulness rules established. |
| 2026-09-17 | Migrated Image-To-Ico, IPTV-checker and Gist_manager; completed owner discovery of 66 repositories. | 3 verified; overall eligibility incomplete. |
| 2026-09-17 | Migrated WojThom, PowerBookmark and InfoPulse-PL; blocked Aria2Gui due its conflicting feature PR. | 6 verified; 1 blocked. |
| 2026-09-18 | Migrated WAV-to-MP3-converter, PolSilver_Bluetooth and FASTIPTVPlayer. | 9 verified. |
| 2026-09-18 | Migrated Matrix_Windows_Commander, BackgroundPXR and SwirPhotoClean. | 12 verified; priority subset 12/13. |
| 2026-09-18 | Migrated Hex-kolor, Driver-tool and Youtube-VLC. | 15 verified; 35 queued; overall progress N/A. |
| 2026-09-18 | Safety-qualified and migrated Spamer; excluded empty placeholder `plugin.swir`; migrated the T303UA OpenCore EFI reference. | 17 verified; 32 queued; 1 blocked; 12 delegated; 4 excluded. |
| 2026-09-18 | Verified already-landed README PRO v2 + SVG PRO migrations for XBookmark, Worker-Time-list-generator and keygenerator. | 20 verified; 29 queued. |
| 2026-09-18 | Audited and migrated SwirTube. | 21 verified; 28 queued. |
| 2026-09-18 | Migrated File.io_Downloaderup and TimeListe-Generator. | 23 verified; 26 queued. |
| 2026-09-18 | Migrated CyptoPriceWidget, Matrix-Ajax-Chat and Ghos-DNS; began explicit SVG-only legacy-meter cleanup. | 26 verified; 23 queued; cleanup 6 verified. |
| 2026-09-18 | Migrated Torrent_downloader, cda-pl and Koder through docs-only PRs; audited source/release/legal/security facts, verified SVG-only N/A progress, deterministic generators and final default-branch files. | **29 verified; 20 queued; 1 blocked; 12 delegated; 4 excluded. Legacy meter cleanup: 9 verified / 40 pending / 1 blocked / 12 delegated / 4 excluded.** |

Do not silently change the denominator. Every later `queued → excluded/delegated/verified/blocked` decision must update the inventory row, state totals, metrics marker and generated migration SVGs together. Legacy-meter cleanup state is independent and must also be updated after each re-audit. Disable only this migration task after every discovered repository has a final eligibility state and every eligible migration/SVG rollout/legacy-meter cleanup is verified or explicitly excepted according to the completion policy.
