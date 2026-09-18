# SWIR README PRO Migration — Status

Documentation migration ledger for existing SWIR projects. This tracks **README migration**, not application development, release readiness or runtime verification.

Canonical standards: [SWIR README PRO v2](SWIR-README-STANDARD.md) · [SWIR Progress SVG PRO](SWIR-PROGRESS-STANDARD.md).

<!-- MIGRATION-METRICS owner=68 verified=49 queued=0 in_progress=0 blocked=1 delegated=13 excluded=5 priority_verified=12 priority_total=13 eligibility=COMPLETE -->
<!-- LEGACY-METER-CLEANUP verified=38 pending=11 blocked=1 delegated=13 excluded=5 -->

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-card.svg" alt="SWIR README PRO eligible migration progress — 98.0%, 49 verified and 1 blocked" />
</p>

## Run status

| Item | Current state |
|---|---|
| Started | 2026-09-17 |
| Owner repositories discovered | **68** — original 66-repository snapshot plus `BrokeDJ` and later-discovered `SilentCryptoMiner`, both appended explicitly on 2026-09-18 |
| Verified migrations | **49** |
| SVG rollout verified | **49** — same repositories |
| Legacy meter cleanup | **38 verified / 11 pending / 1 blocked / 13 delegated / 5 excluded** |
| Queued / qualification pending | **0** |
| In progress | **0** |
| Blocked | **1** — `Aria2Gui`; feature PR #1 changes README plus application/UI code |
| Delegated to dedicated active tasks | **13** |
| Structural / safety exclusions recorded | **5** |
| Initial priority subset | **12 / 13 = 92.3% verified** |
| Eligible migration completion | **49 / 50 = 98.0%** — blocked repositories remain incomplete; delegated/excluded repositories are not counted as completed migrations |
| Next cleanup batch | `WojThom` → `SwirTube` → `Matrix_Windows_Commander` |

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-mini.svg" alt="Initial priority subset progress — 12 of 13 repositories verified" />
</p>

The mini graphic measures **only the initial 13-repository priority subset**. It is not the overall eligible migration percentage.

## Status contract

- `queued`: discovered, qualification and/or migration remains.
- `in_progress`: migration branch/PR exists but is not verified on the default branch.
- `verified`: final README and required assets were read back on the default branch after appropriate checks and merge.
- `blocked`: concrete unresolved obstacle prevents a safe migration.
- `excluded`: outside migration scope with a recorded reason.
- `delegated`: another active project task owns documentation changes; never counted as this task's verified migration.

An open PR, marker, banner or green source CI alone does not prove complete migration. Verify branding, paths, truthful claims, install/release links, visible Search Keywords, SWIR footer and Progress SVG PRO state.

## Legacy meter cleanup contract

Approved SVG progress graphics replace retired character/ASCII/Unicode documentation progress meters. Plain numeric percentages, counters, tables, checklist state and structural markers remain.

- `verified`: current default-branch README/status and relevant generator were re-read and do not contain or regenerate a retired character meter.
- `pending`: cleanup not yet re-audited after the SVG-only correction.
- `blocked`, `delegated`, `excluded`: follow the same ownership/scope rules as migration state.

Current cleanup-verified repositories: `Image-To-Ico`, `IPTV-checker`, `Gist_manager`, `CyptoPriceWidget`, `Matrix-Ajax-Chat`, `Ghos-DNS`, `Torrent_downloader`, `cda-pl`, `Koder`, `Github-README-Generator`, `Grosz`, `watermark-remover`, `Py-Converter-to-exe`, `Image-to-txt`, `Titanium-APK-Bulider`, `czatpythom`, `NeonShift-X`, `ASCITEXT`, `Github_Webste`, `Dreambox-scaner`, `Torrent_downloaderv2`, `MacTrix`, `Czateria_PLUS_Android`, `Matrix-czat-pythom`, `Ryzen-5-5600G-A320M-`, `Procent-calkulator`, `Ghost-APK-Builder`, `CrossAim_power`, `Multichain-Tracker`, `Hex-kolor`, `Driver-tool`, `Youtube-VLC`, `Spamer`, `Transformer-3-Pro-T303UA-i5-6200-hackintosh`, `XBookmark`, `Worker-Time-list-generator`, `InfoPulse-PL`, `keygenerator`.

## Initial priority queue

| # | Repository | State | Evidence |
|---:|---|---|---|
| 1 | [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `verified` | README/SVG verified; cleanup re-audited |
| 2 | [IPTV-checker](https://github.com/Swir/IPTV-checker) | `verified` | PR #2 → `c1b113e`; cleanup verified |
| 3 | [Gist_manager](https://github.com/Swir/Gist_manager) | `verified` | PR #3 → `c22fde0`; cleanup verified |
| 4 | [WojThom](https://github.com/Swir/WojThom) | `verified` | PR #8 → `ba38c17` |
| 5 | [Aria2Gui](https://github.com/Swir/Aria2Gui) | `blocked` | Feature PR #1 remains open; re-audit after owner task resolves it |
| 6 | [PowerBookmark](https://github.com/Swir/PowerBookmark) | `verified` | PR #1 → `64be655` |
| 7 | [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `verified` | PR #1 → `1639025`; cleanup verified |
| 8 | [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `verified` | PR #1 → `5283cc87` |
| 9 | [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `verified` | PR #4 → `714e44bb` |
| 10 | [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `verified` | PR #4 → `3d996ef9` |
| 11 | [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `verified` | PR #4 → `5402a9d`; CI passed |
| 12 | [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `verified` | PR #1 → `c640e8f` |
| 13 | [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `verified` | PR #1 → `50f2d2a`; STATUS.md 6/7 gate |

## Complete owner inventory

The original 66-repository discovery snapshot is preserved. `BrokeDJ` and later-discovered `SilentCryptoMiner` were appended explicitly on 2026-09-18; the owner denominator is now **68**. `SilentCryptoMiner` is recorded without modification because GitHub blocks repository access and the hidden-miner category is outside the safe migration scope.

| Repository | Default | State | Evidence / note |
|---|---|---|---|
| [Hex-kolor](https://github.com/Swir/Hex-kolor) | `main` | `verified` | PR #1 → `b0971040`; cleanup verified |
| [swir.github.io](https://github.com/Swir/swir.github.io) | `main` | `excluded` | Portfolio/status site; not a README migration target |
| [Aria2Gui](https://github.com/Swir/Aria2Gui) | `main` | `blocked` | Feature PR #1 changes README + application/UI; avoid competing writes |
| [Driver-tool](https://github.com/Swir/Driver-tool) | `main` | `verified` | PR #1 → `977c05ec`; cleanup verified |
| [Youtube-VLC](https://github.com/Swir/Youtube-VLC) | `main` | `verified` | PR #3 → `6bc578f1`; CI passed; cleanup verified |
| [Spamer](https://github.com/Swir/Spamer) | `main` | `verified` | PR #1 → `4e5773a`; controlled-use framing; cleanup verified |
| [plugin.swir](https://github.com/Swir/plugin.swir) | `master` | `excluded` | Placeholder only; no product invented |
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `main` | `verified` | README/SVG verified; cleanup re-audited |
| [Transformer-3-Pro-T303UA-i5-6200-hackintosh](https://github.com/Swir/Transformer-3-Pro-T303UA-i5-6200-hackintosh) | `main` | `verified` | PR #3 → `20a65a5`; cleanup verified |
| [Tank-Revival-Overdrive](https://github.com/Swir/Tank-Revival-Overdrive) | `main` | `delegated` | Dedicated active development task owns documentation |
| [XBookmark](https://github.com/Swir/XBookmark) | `main` | `verified` | main `7fd4019`; README v2 + SVG PRO; cleanup verified |
| [Worker-Time-list-generator](https://github.com/Swir/Worker-Time-list-generator) | `main` | `verified` | main `c685c1a`; CI passed; cleanup verified |
| [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `main` | `verified` | PR #1 → `1639025`; cleanup verified |
| [keygenerator](https://github.com/Swir/keygenerator) | `main` | `verified` | main `3671502`; safety-reviewed generator; cleanup verified |
| [WojThom](https://github.com/Swir/WojThom) | `main` | `verified` | PR #8 → `ba38c17` |
| [Y6-gamestick](https://github.com/Swir/Y6-gamestick) | `main` | `excluded` | Empty repository; no product invented |
| [SwirTube](https://github.com/Swir/SwirTube) | `main` | `verified` | PR #1 → `ab1a668` |
| [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `main` | `verified` | PR #4 → `5402a9d`; CI passed |
| [Swir](https://github.com/Swir/Swir) | `main` | `excluded` | Profile repo; standards/ledger/tooling only |
| [File.io_Downloaderup](https://github.com/Swir/File.io_Downloaderup) | `main` | `verified` | PR #1 → `bc40f89` |
| [Nes_New_Life](https://github.com/Swir/Nes_New_Life) | `main` | `delegated` | Dedicated active development task owns documentation |
| [TimeListe-Generator](https://github.com/Swir/TimeListe-Generator) | `main` | `verified` | PR #1 → `ee6839a` |
| [CyptoPriceWidget](https://github.com/Swir/CyptoPriceWidget) | `main` | `verified` | PR #4 → `489f88d`; cleanup verified |
| [Matrix-Ajax-Chat](https://github.com/Swir/Matrix-Ajax-Chat) | `main` | `verified` | PR #3 → `51f7ced`; cleanup verified |
| [Ghos-DNS](https://github.com/Swir/Ghos-DNS) | `main` | `verified` | PR #1 → `5ba3e21`; cleanup verified |
| [Torrent_downloader](https://github.com/Swir/Torrent_downloader) | `main` | `verified` | PR #1 → `efca9a1`; cleanup verified |
| [cda-pl](https://github.com/Swir/cda-pl) | `main` | `verified` | PR #1 → `2c8f0a3`; cleanup verified |
| [Koder](https://github.com/Swir/Koder) | `main` | `verified` | PR #1 → `310c9d7`; cleanup verified |
| [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `main` | `verified` | PR #1 → `50f2d2a`; STATUS.md 6/7 gate |
| [Gist_manager](https://github.com/Swir/Gist_manager) | `main` | `verified` | PR #3 → `c22fde0`; cleanup verified |
| [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `main` | `verified` | PR #1 → `c640e8f` |
| [Github-README-Generator](https://github.com/Swir/Github-README-Generator) | `main` | `verified` | PR #1 → `04344ee`; cleanup verified |
| [watermark-remover](https://github.com/Swir/watermark-remover) | `main` | `verified` | PR #3 → `8f80970`; exact-head CI passed; cleanup verified |
| [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `main` | `verified` | PR #4 → `3d996ef9` |
| [Grosz](https://github.com/Swir/Grosz) | `main` | `verified` | PR #1 → `7322749`; cleanup verified |
| [Py-Converter-to-exe](https://github.com/Swir/Py-Converter-to-exe) | `main` | `verified` | PR #1 → `69de7b4`; cleanup verified |
| [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `main` | `verified` | PR #1 → `5283cc87` |
| [Image-to-txt](https://github.com/Swir/Image-to-txt) | `main` | `verified` | PR #1 → `d0305a2`; cleanup verified |
| [Titanium-APK-Bulider](https://github.com/Swir/Titanium-APK-Bulider) | `main` | `verified` | PR #11 → `dd71a04`; cleanup verified |
| [czatpythom](https://github.com/Swir/czatpythom) | `main` | `verified` | PR #3 → `5a0c462`; exact-head CI passed; cleanup verified |
| [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `main` | `verified` | PR #4 → `714e44bb` |
| [NeonShift-X](https://github.com/Swir/NeonShift-X) | `main` | `verified` | PR #1 → `c19d4e3`; docs CI passed; cleanup verified |
| [IPTV-checker](https://github.com/Swir/IPTV-checker) | `main` | `verified` | PR #2 → `c1b113e`; cleanup verified |
| [ASCITEXT](https://github.com/Swir/ASCITEXT) | `main` | `verified` | PR #1 → `822893c`; docs CI passed; cleanup verified |
| [Github_Webste](https://github.com/Swir/Github_Webste) | `main` | `verified` | PR #1 → `53fd211`; cleanup verified |
| [Dreambox-scaner](https://github.com/Swir/Dreambox-scaner) | `main` | `verified` | PR #4 → `703b621`; exact-head CI passed; v6.2.0 preserved; cleanup verified |
| [Torrent_downloaderv2](https://github.com/Swir/Torrent_downloaderv2) | `main` | `verified` | PR #1 → `96c0a2e`; v1.0.0 preserved; cleanup verified |
| [MacTrix](https://github.com/Swir/MacTrix) | `main` | `verified` | PR #3 → `aac3840`; exact-head CI passed; v2.1.0 preserved; cleanup verified |
| [PowerBookmark](https://github.com/Swir/PowerBookmark) | `main` | `verified` | PR #1 → `64be655` |
| [Dragon-DiskForge](https://github.com/Swir/Dragon-DiskForge) | `main` | `delegated` | Dedicated active development task owns documentation |
| [Konofix](https://github.com/Swir/Konofix) | `main` | `delegated` | Dedicated active development task owns documentation |
| [check-out-of-hell](https://github.com/Swir/check-out-of-hell) | `main` | `delegated` | Dedicated active development task owns documentation |
| [xADKiller](https://github.com/Swir/xADKiller) | `main` | `delegated` | Dedicated active development task owns documentation |
| [SWIR_OS](https://github.com/Swir/SWIR_OS) | `main` | `delegated` | Dedicated active development task owns documentation |
| [Czateria_PLUS_Android](https://github.com/Swir/Czateria_PLUS_Android) | `main` | `verified` | PR #1 → `499e173`; v0.6.3 APK/SHA preserved; no repo CI; cleanup verified |
| [Matrix-czat-pythom](https://github.com/Swir/Matrix-czat-pythom) | `main` | `verified` | PR #1 → `83e9ffe`; runtime layout limitation documented; no repo CI; cleanup verified |
| [KaliPhoneStudio](https://github.com/Swir/KaliPhoneStudio) | `main` | `delegated` | Dedicated active development task owns documentation |
| [SwirEngine](https://github.com/Swir/SwirEngine) | `main` | `delegated` | Dedicated active development task owns documentation |
| [GTT](https://github.com/Swir/GTT) | `main` | `delegated` | Dedicated active development task owns documentation |
| [Ryzen-5-5600G-A320M-](https://github.com/Swir/Ryzen-5-5600G-A320M-) | `main` | `verified` | PR #1 → `ad653615`; README Docs CI passed; product progress N/A; cleanup verified |
| [Procent-calkulator](https://github.com/Swir/Procent-calkulator) | `main` | `verified` | PR #1 → `be42f1f`; v1.0.0 preserved; README Docs CI passed; cleanup verified |
| [Swirui](https://github.com/Swir/Swirui) | `main` | `delegated` | Dedicated active development task owns documentation |
| [Ghost-APK-Builder](https://github.com/Swir/Ghost-APK-Builder) | `main` | `verified` | PR #9 → `64a74d08`; v17 94% model and beta.2 preserved; README Docs + Ghost v17 CI passed; cleanup verified |
| [CrossAim_power](https://github.com/Swir/CrossAim_power) | `main` | `verified` | PR #2 → `51a0853`; README Docs CI passed; v1.2.0 + MIT preserved; cleanup verified |
| [SwirPhoneOS](https://github.com/Swir/SwirPhoneOS) | `main` | `delegated` | Dedicated active development task owns documentation |
| [Multichain-Tracker](https://github.com/Swir/Multichain-Tracker) | `main` | `verified` | PR #1 → `26c8f59`; README Docs CI passed; v1.0.0 preserved; cleanup verified |
| [BrokeDJ](https://github.com/Swir/BrokeDJ) | `main` | `delegated` | Dedicated active development task owns documentation |
| [SilentCryptoMiner](https://github.com/Swir/SilentCryptoMiner) | `master` | `excluded` | GitHub access is blocked (TOS); hidden-miner category is outside safe migration scope; no modification |

State totals: **49 verified + 0 queued + 0 in progress + 1 blocked + 13 delegated + 5 excluded = 68**.

## Work owned by active project tasks

Delegated: `Tank-Revival-Overdrive`, `Nes_New_Life`, `Dragon-DiskForge`, `Konofix`, `check-out-of-hell`, `xADKiller`, `SWIR_OS`, `KaliPhoneStudio`, `SwirEngine`, `GTT`, `Swirui`, `SwirPhoneOS`, `BrokeDJ`. Migration may audit compliance, but edits remain with those tasks while active.

## Verification highlights

- `CrossAim_power`: PR #2 → `51a0853`; README v2, hero, preserved project icon, N/A product-progress SVG pair/template and deterministic docs check were verified on `main`; README Docs passed on exact PR head; real v1.2.0 release and MIT license preserved.
- `Multichain-Tracker`: PR #1 → `26c8f59`; README v2, project icon/hero, N/A product-progress SVG pair/template and deterministic docs check were verified on `main`; README Docs passed on exact PR head; v1.0.0 preserved and transaction-history scope corrected to Ethereum/Etherscan.
- `Ryzen-5-5600G-A320M-`: PR #1 → `ad653615`; final README/STATUS/card/mini/template/generator read back on `main`; README Docs CI passed on exact PR head; progress correctly N/A for the hardware-reference scope.
- `Procent-calkulator`: PR #1 → `be42f1f`; final README/STATUS/card/mini/template/generator read back on `main`; README Docs CI passed; real v1.0.0 release preserved and product progress remains N/A.
- `Ghost-APK-Builder`: PR #9 → `64a74d08`; final README/ROADMAP/card/mini/template/generator read back on `main`; README Docs and Ghost v17 CI passed; documented 94% v17 model and v17.0.0-beta.2 preserved; stable gate still requires real physical-device evidence.

## Exclusions

- `swir.github.io`: portfolio/status site.
- `plugin.swir`: placeholder only.
- `Y6-gamestick`: empty repository.
- `Swir`: profile repository; standards/ledger/tooling only.
- `SilentCryptoMiner`: GitHub access is blocked under TOS; hidden-miner tooling is outside the safe migration scope, so no README promotion or usage improvements were made.

## Blocker

`Aria2Gui` remains blocked while feature PR #1 modifies README and application/UI files. Re-audit fresh `main` after that work is resolved.

## Execution log

| Date | Work performed | Result |
|---|---|---|
| 2026-09-17 | Created canonical ledger and 66-repository owner snapshot. | Denominator and truthfulness rules fixed. |
| 2026-09-18 | Reached 12/13 verified in initial priority subset. | Aria2Gui remained blocked. |
| 2026-09-18 | Expanded legacy migration and SVG-only cleanup tracking. | 26 verified. |
| 2026-09-18 | Migrated Torrent_downloader, cda-pl and Koder. | 29 verified; cleanup 9. |
| 2026-09-18 | Migrated Github-README-Generator, Grosz and watermark-remover. | 32 verified; cleanup 12. |
| 2026-09-18 | Migrated Py-Converter-to-exe, Image-to-txt and Titanium-APK-Bulider. | 35 verified; cleanup 15. |
| 2026-09-18 | Migrated czatpythom, NeonShift-X and ASCITEXT. | 38 verified; cleanup 18. |
| 2026-09-18 | Migrated Github_Webste, Dreambox-scaner and Torrent_downloaderv2; appended BrokeDJ as delegated. | 41 verified; cleanup 21; owner denominator 67. |
| 2026-09-18 | Migrated MacTrix, Czateria_PLUS_Android and Matrix-czat-pythom. | 44 verified; cleanup 24; 5 queued remain. |
| 2026-09-18 | Verified Ryzen-5-5600G-A320M-, Procent-calkulator and Ghost-APK-Builder on final main after merged docs PRs and exact-head checks. | 47 verified; cleanup 27; 2 queued remain. |
| 2026-09-18 | Migrated CrossAim_power and Multichain-Tracker; completed all remaining queued qualification. Full inventory re-audit discovered SilentCryptoMiner and recorded it as excluded without modification. | 49 verified; 0 queued; cleanup 29; owner denominator 68. |
| 2026-09-18 | Re-audited Hex-kolor, Driver-tool and Youtube-VLC on current main; README v2, SVG card/mini/template and deterministic generator contain no retired character meter, and no conflicting open PR exists. | Migration count unchanged at 49; cleanup 32; 17 pending. |
| 2026-09-18 | Re-audited Spamer, Transformer-3-Pro-T303UA-i5-6200-hackintosh and XBookmark on current main; README v2, SVG card/mini/template and progress generators contain no retired character meter, and no conflicting open PR exists. | Migration count unchanged at 49; cleanup 35; 14 pending. |
| 2026-09-18 | Re-audited Worker-Time-list-generator, InfoPulse-PL and keygenerator on current main; README v2, SVG card/mini/template and deterministic progress generators contain no retired character meter, and no conflicting open PR exists. | Migration count unchanged at 49; cleanup 38; 11 pending. |

Do not silently change the denominator. Every later state decision must update inventory, metrics marker and generated migration SVGs together. Legacy-meter cleanup is independent. Disable only this migration task after every discovered repository has a final eligibility state and every eligible migration/SVG rollout/cleanup is verified or explicitly excepted.