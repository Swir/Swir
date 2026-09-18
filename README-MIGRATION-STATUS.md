# SWIR README PRO Migration — Status

Documentation migration ledger for existing SWIR projects. This is **README migration progress**, not application development, release readiness or runtime verification.

Canonical standards: [SWIR README PRO v2](SWIR-README-STANDARD.md) · [SWIR Progress SVG PRO](SWIR-PROGRESS-STANDARD.md).

<!-- MIGRATION-METRICS owner=66 verified=35 queued=14 in_progress=0 blocked=1 delegated=12 excluded=4 priority_verified=12 priority_total=13 eligibility=INCOMPLETE -->
<!-- LEGACY-METER-CLEANUP verified=15 pending=34 blocked=1 delegated=12 excluded=4 -->

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-card.svg" alt="SWIR README PRO migration overall progress — N/A while eligibility review is incomplete" />
</p>

## Run status

| Item | Current state |
|---|---|
| Started | 2026-09-17 |
| Owner repositories discovered | **66**; fixed owner inventory below |
| Verified migrations | **35** |
| SVG rollout verified | **35** — same repositories |
| Legacy meter cleanup | **15 verified / 34 pending / 1 blocked / 12 delegated / 4 excluded** |
| Queued / qualification pending | **14** |
| In progress | **0** |
| Blocked | **1** — Aria2Gui; feature PR #1 remains open and edits README plus application/UI code |
| Delegated to dedicated active tasks | **12** |
| Structural exclusions recorded | **4** |
| Initial priority subset | **12 / 13 = 92.3% verified** |
| Overall migration percentage | **N/A** until every owner repository receives a final eligibility decision |
| Next qualification batch | `czatpythom` → `NeonShift-X` → `ASCITEXT` |
| Completion policy | Final eligibility audit → every eligible repo verified or explicitly excepted → SVG + legacy-meter cleanup verified/excepted → final audit/report → disable only this migration task |

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-mini.svg" alt="Initial priority subset progress — 12 of 13 repositories verified" />
</p>

The mini graphic measures **only the initial 13-repository priority subset**. It is not the overall migration percentage. The overall card stays **N/A** while discovered repositories still need a final eligibility decision.

## Status contract

- `queued`: discovered, but qualification and/or migration work remains.
- `in_progress`: an actual migration branch/PR exists and is not yet verified on the default branch.
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

Current cleanup-verified repositories: `Image-To-Ico`, `IPTV-checker`, `Gist_manager`, `CyptoPriceWidget`, `Matrix-Ajax-Chat`, `Ghos-DNS`, `Torrent_downloader`, `cda-pl`, `Koder`, `Github-README-Generator`, `Grosz`, `watermark-remover`, `Py-Converter-to-exe`, `Image-to-txt`, `Titanium-APK-Bulider`.

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

This is the fixed 66-repository owner discovery snapshot. No repository is added or removed from the denominator silently.

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
| [Swir](https://github.com/Swir/Swir) | `main` | `excluded` | profile repo; only standards, migration ledger and migration tooling maintained here |
| [File.io_Downloaderup](https://github.com/Swir/File.io_Downloaderup) | `main` | `verified` | PR #1 → `bc40f89` |
| [Nes_New_Life](https://github.com/Swir/Nes_New_Life) | `main` | `delegated` | dedicated active development task |
| [TimeListe-Generator](https://github.com/Swir/TimeListe-Generator) | `main` | `verified` | PR #1 → `ee6839a` |
| [CyptoPriceWidget](https://github.com/Swir/CyptoPriceWidget) | `main` | `verified` | PR #4 → `489f88d`; cleanup verified |
| [Matrix-Ajax-Chat](https://github.com/Swir/Matrix-Ajax-Chat) | `main` | `verified` | PR #3 → `51f7ced`; cleanup verified |
| [Ghos-DNS](https://github.com/Swir/Ghos-DNS) | `main` | `verified` | PR #1 → `5ba3e21`; cleanup verified |
| [Torrent_downloader](https://github.com/Swir/Torrent_downloader) | `main` | `verified` | PR #1 → `efca9a1`; SVG-only N/A progress + generator; cleanup verified |
| [cda-pl](https://github.com/Swir/cda-pl) | `main` | `verified` | PR #1 → `2c8f0a3`; lawful-use scope; cleanup verified |
| [Koder](https://github.com/Swir/Koder) | `main` | `verified` | PR #1 → `310c9d7`; XOR security limits; cleanup verified |
| [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `main` | `verified` | PR #1 → `50f2d2a`; 1.0 gate SVG from STATUS.md 6/7 |
| [Gist_manager](https://github.com/Swir/Gist_manager) | `main` | `verified` | PR #3 → `c22fde0`; cleanup verified |
| [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `main` | `verified` | PR #1 → `c640e8f` |
| [Github-README-Generator](https://github.com/Swir/Github-README-Generator) | `main` | `verified` | PR #1 → `04344ee`; source/release audited; SVG-only N/A progress; cleanup verified |
| [watermark-remover](https://github.com/Swir/watermark-remover) | `main` | `verified` | PR #3 → `8f80970`; CI passed Python 3.10–3.13; v2.1.0 release/responsible-use scope preserved; cleanup verified |
| [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `main` | `verified` | PR #4 → `3d996ef9` |
| [Grosz](https://github.com/Swir/Grosz) | `main` | `verified` | PR #1 → `7322749`; asset-only scope; no releases; SVG-only N/A progress; cleanup verified |
| [Py-Converter-to-exe](https://github.com/Swir/Py-Converter-to-exe) | `main` | `verified` | PR #1 → `69de7b4`; source/release audited; PyInstaller-only behavior documented; cleanup verified |
| [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `main` | `verified` | PR #1 → `5283cc87` |
| [Image-to-txt](https://github.com/Swir/Image-to-txt) | `main` | `verified` | PR #1 → `d0305a2`; source limitations/no releases documented; cleanup verified |
| [Titanium-APK-Bulider](https://github.com/Swir/Titanium-APK-Bulider) | `main` | `verified` | PR #11 → `dd71a04`; v10.0 release criteria 10/10 scope + SVG; cleanup verified |
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

State totals: **35 verified + 14 queued + 0 in progress + 1 blocked + 12 delegated + 4 excluded = 66 owner repositories**.

## Work owned by other active tasks

The following remain delegated rather than edited by this migration task: `SWIR_OS`, `SwirEngine`, `Swirui`, `SwirPhoneOS`, `KaliPhoneStudio`, `Dragon-DiskForge`, `GTT`, `Tank-Revival-Overdrive`, `Nes_New_Life`, `check-out-of-hell`, `Konofix` and `xADKiller`.

Their README/SVG/legacy-meter compliance may be audited, but documentation edits remain with their dedicated task while it is active to avoid competing branches and stale rewrites.

## Verified migrations

| Repository | Merge / evidence | README v2 | SVG PRO | Legacy meter cleanup | Verification note |
|---|---|---:|---:|---:|---|
| Image-To-Ico | README PR #1; SVG PR #2 → `dba8219` | ✅ | ✅ | ✅ | main README + generator re-audited 2026-09-18 |
| IPTV-checker | PR #2 → `c1b113e` | ✅ | ✅ | ✅ | migration CI passed; main README + generator re-audited |
| Gist_manager | PR #3 → `c22fde0` | ✅ | ✅ | ✅ | migration CI passed; main README + generator re-audited |
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
| Torrent_downloader | PR #1 → `efca9a1` | ✅ | ✅ | ✅ | source/release audited; final main read back |
| cda-pl | PR #1 → `2c8f0a3` | ✅ | ✅ | ✅ | lawful-use/source audit; final main read back |
| Koder | PR #1 → `310c9d7` | ✅ | ✅ | ✅ | source/release/workflow audited; final main read back |
| Github-README-Generator | PR #1 → `04344ee` | ✅ | ✅ | ✅ | source + v1.0.0 release audited; no PR docs CI; final main README/card read back |
| Grosz | PR #1 → `7322749` | ✅ | ✅ | ✅ | asset-only scope and existing artwork preserved; no releases; final main README/generator read back |
| watermark-remover | PR #3 → `8f80970` | ✅ | ✅ | ✅ | exact final-head CI passed Python 3.10–3.13; main README/card read back |
| Py-Converter-to-exe | PR #1 → `69de7b4` | ✅ | ✅ | ✅ | source/release audited; no PR docs CI; final main README/card read back |
| Image-to-txt | PR #1 → `d0305a2` | ✅ | ✅ | ✅ | source limitations and absence of releases documented; no PR CI; final main README read back |
| Titanium-APK-Bulider | PR #11 → `dd71a04` | ✅ | ✅ | ✅ | v10.0 criteria 10/10; docs-only paths do not trigger v10 source CI; final main README/card read back |

## Exclusions

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
| 2026-09-17 | Created canonical ledger; completed fixed owner discovery of 66 repositories; began priority migrations. | Denominator and truthfulness rules fixed. |
| 2026-09-18 | Reached 12/13 verified in the initial priority subset; Aria2Gui remained blocked by its feature PR. | Priority subset 92.3%. |
| 2026-09-18 | Expanded migration through legacy utilities and added explicit SVG-only legacy-meter cleanup tracking. | 26 verified; cleanup tracking active. |
| 2026-09-18 | Migrated Torrent_downloader, cda-pl and Koder. | 29 verified; cleanup 9 verified. |
| 2026-09-18 | Migrated Github-README-Generator, Grosz and watermark-remover; watermark-remover merged only after exact final-head CI passed. | 32 verified; cleanup 12 verified. |
| 2026-09-18 | Migrated Py-Converter-to-exe, Image-to-txt and Titanium-APK-Bulider through documentation-only PRs; corrected historical capability claims, preserved real releases, and applied SVG-only progress. | **35 verified; 14 queued; 0 in progress; 1 blocked; 12 delegated; 4 excluded. Cleanup: 15 verified / 34 pending / 1 blocked / 12 delegated / 4 excluded.** |

Do not silently change the denominator. Every later state decision must update the inventory row, state totals, metrics marker and generated migration SVGs together. Legacy-meter cleanup state is independent and must also be updated after each re-audit. Disable only this migration task after every discovered repository has a final eligibility state and every eligible migration/SVG rollout/legacy-meter cleanup is verified or explicitly excepted according to the completion policy.
