# SWIR README PRO Migration — Status

Documentation migration ledger for existing SWIR projects. This is **README migration progress**, not application development, release readiness or runtime verification.

Canonical standards: [SWIR README PRO v2](SWIR-README-STANDARD.md) · [SWIR Progress SVG PRO](SWIR-PROGRESS-STANDARD.md).

<!-- MIGRATION-METRICS owner=66 verified=15 queued=35 blocked=1 delegated=12 excluded=3 priority_verified=12 priority_total=13 eligibility=INCOMPLETE -->

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-card.svg" alt="SWIR README PRO migration overall progress — N/A while eligibility review is incomplete" />
</p>

## Run status

| Item | Current state |
|---|---|
| Started | 2026-09-17 |
| Owner repositories discovered | **66**; repository search page 2 was empty for the discovery snapshot |
| Verified migrations | **15** |
| SVG rollout verified | **15** — same repositories |
| Queued / qualification pending | **35** |
| Blocked | **1** — Aria2Gui; feature PR #1 remains open and edits README plus application/UI code |
| Delegated to dedicated active tasks | **12** |
| Structural exclusions recorded | **3** |
| Initial priority subset | **12 / 13 = 92.3% verified** |
| Overall migration percentage | **N/A** until every queued owner repository receives a final eligibility decision |
| Next qualification batch | **Spamer** safety/eligibility review → `plugin.swir` → `Transformer-3-Pro-T303UA-i5-6200-hackintosh` |
| Completion policy | Final eligibility audit → every eligible repo verified or explicitly excepted → final audit/report → disable only this migration task |

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-mini.svg" alt="Initial priority subset progress — 12 of 13 repositories verified" />
</p>

The mini bar above measures **only the initial 13-repository priority subset**. It is not the overall migration percentage. The overall card stays **N/A** while discovered repositories still need a final eligibility decision.

## Status contract

- `queued`: repository is discovered but still needs qualification and/or migration work.
- `in_progress`: an actual migration branch/PR exists.
- `verified`: final README and required assets were read back on the default branch after appropriate checks and merge.
- `blocked`: a concrete unresolved obstacle prevents a safe migration.
- `excluded`: outside migration scope with a specific reason; never counted as migrated.
- `delegated`: another active project task owns documentation changes; never counted as this task's verified migration.

A v2 marker, uploaded banner, open PR or green source CI alone does not prove a complete migration. Verify branding, paths, truthful claims, installation, release links, visible Search Keywords, SWIR footer and Progress SVG PRO state where applicable.

## Initial priority queue

| Order | Repository | State | Evidence / next step |
|---:|---|---|---|
| 1 | [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `verified` | README PR #1; SVG PR #2 → `dba8219`; main README/progress assets read back. |
| 2 | [IPTV-checker](https://github.com/Swir/IPTV-checker) | `verified` | PR #2 → `c1b113e`; PR CI passed; main README/progress assets read back. |
| 3 | [Gist_manager](https://github.com/Swir/Gist_manager) | `verified` | PR #3 → `c22fde0`; PR CI passed; main README/progress assets read back. |
| 4 | [WojThom](https://github.com/Swir/WojThom) | `verified` | PR #8 → `ba38c17`; main README/card read back; app workflows path-filtered. |
| 5 | [Aria2Gui](https://github.com/Swir/Aria2Gui) | `blocked` | Feature PR #1 remains open and edits README + application/UI files; re-audit after it is resolved. |
| 6 | [PowerBookmark](https://github.com/Swir/PowerBookmark) | `verified` | PR #1 → `64be655`; README v2 + SVG PRO read back; unsupported JSON-backup claim corrected. |
| 7 | [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `verified` | PR #1 → `1639025`; README v2 + SVG PRO read back; Polish app identity preserved. |
| 8 | [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `verified` | PR #1 → `5283cc87`; README/card read back; unsupported AI-evasion claims removed. |
| 9 | [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `verified` | PR #4 → `714e44bb`; CI passed Python 3.10–3.14 + Windows smoke. |
| 10 | [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `verified` | PR #4 → `3d996ef9`; CI passed Python 3.10–3.14 + Windows GUI smoke. |
| 11 | [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `verified` | PR #4 → `5402a9d`; CI passed Python 3.10–3.14 + Windows GUI smoke. |
| 12 | [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `verified` | PR #1 → `c640e8f`; Windows workflow passed; truthful N/A product progress. |
| 13 | [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `verified` | PR #1 → `50f2d2a`; Windows workflow passed tests/build/EXE smoke; progress 6/7 from STATUS.md. |

## Complete owner inventory snapshot

This is the finite 66-repository owner discovery snapshot. `queued` entries still require content, fork, safety, legal and project-state qualification before the final eligible-migration denominator can be closed.

| Repository | Default branch | State | Note |
|---|---|---|---|
| [Hex-kolor](https://github.com/Swir/Hex-kolor) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #1 → `b0971040`; N/A product progress, no PR CI workflow |
| [swir.github.io](https://github.com/Swir/swir.github.io) | `main` | `excluded` | portfolio/status site, not a README migration target |
| [Aria2Gui](https://github.com/Swir/Aria2Gui) | `main` | `blocked` | feature PR #1 remains open and changes README + application/UI code; defer migration |
| [Driver-tool](https://github.com/Swir/Driver-tool) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #1 → `977c05ec`; simulation-only driver update documented; no PR CI workflow |
| [Youtube-VLC](https://github.com/Swir/Youtube-VLC) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #3 → `6bc578f1`; CI run `35290479980` passed Python 3.10–3.14 + Windows GUI smoke |
| [Spamer](https://github.com/Swir/Spamer) | `main` | `queued` | eligibility/safety review required before any edit |
| [plugin.swir](https://github.com/Swir/plugin.swir) | `master` | `queued` | qualification/readme audit pending |
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `main` | `verified` | README v2 + SVG rollout verified on main; README PR #1, SVG PR #2 → `dba8219` |
| [Transformer-3-Pro-T303UA-i5-6200-hackintosh](https://github.com/Swir/Transformer-3-Pro-T303UA-i5-6200-hackintosh) | `main` | `queued` | qualification/readme audit pending |
| [Tank-Revival-Overdrive](https://github.com/Swir/Tank-Revival-Overdrive) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [XBookmark](https://github.com/Swir/XBookmark) | `main` | `queued` | qualification/readme audit pending |
| [Worker-Time-list-generator](https://github.com/Swir/Worker-Time-list-generator) | `main` | `queued` | qualification/readme audit pending |
| [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #1 → `1639025` |
| [keygenerator](https://github.com/Swir/keygenerator) | `main` | `queued` | purpose/safety review required before any edit |
| [WojThom](https://github.com/Swir/WojThom) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #8 → `ba38c17` |
| [Y6-gamestick](https://github.com/Swir/Y6-gamestick) | `main` | `excluded` | metadata reports size 0; do not invent a product |
| [SwirTube](https://github.com/Swir/SwirTube) | `main` | `queued` | qualification/readme audit pending |
| [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #4 → `5402a9d` |
| [Swir](https://github.com/Swir/Swir) | `main` | `excluded` | profile repo; only migration standards/ledger/tooling are maintained here |
| [File.io_Downloaderup](https://github.com/Swir/File.io_Downloaderup) | `main` | `queued` | qualification/readme audit pending |
| [Nes_New_Life](https://github.com/Swir/Nes_New_Life) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [TimeListe-Generator](https://github.com/Swir/TimeListe-Generator) | `main` | `queued` | qualification/readme audit pending |
| [CyptoPriceWidget](https://github.com/Swir/CyptoPriceWidget) | `main` | `queued` | qualification/readme audit pending |
| [Matrix-Ajax-Chat](https://github.com/Swir/Matrix-Ajax-Chat) | `main` | `queued` | qualification/readme audit pending |
| [Ghos-DNS](https://github.com/Swir/Ghos-DNS) | `main` | `queued` | qualification/readme audit pending |
| [Torrent_downloader](https://github.com/Swir/Torrent_downloader) | `main` | `queued` | qualification/readme audit pending |
| [cda-pl](https://github.com/Swir/cda-pl) | `main` | `queued` | legal/content scope review required before any edit |
| [Koder](https://github.com/Swir/Koder) | `main` | `queued` | qualification/readme audit pending |
| [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #1 → `50f2d2a`; 1.0 gate SVG from STATUS.md 6/7 |
| [Gist_manager](https://github.com/Swir/Gist_manager) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #3 → `c22fde0` |
| [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #1 → `c640e8f` |
| [Github-README-Generator](https://github.com/Swir/Github-README-Generator) | `main` | `queued` | qualification/readme audit pending |
| [watermark-remover](https://github.com/Swir/watermark-remover) | `main` | `queued` | qualification/readme audit pending |
| [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #4 → `3d996ef9` |
| [Grosz](https://github.com/Swir/Grosz) | `main` | `queued` | qualification/readme audit pending |
| [Py-Converter-to-exe](https://github.com/Swir/Py-Converter-to-exe) | `main` | `queued` | qualification/readme audit pending |
| [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #1 → `5283cc87` |
| [Image-to-txt](https://github.com/Swir/Image-to-txt) | `main` | `queued` | qualification/readme audit pending |
| [Titanium-APK-Bulider](https://github.com/Swir/Titanium-APK-Bulider) | `main` | `queued` | qualification/readme audit pending |
| [czatpythom](https://github.com/Swir/czatpythom) | `main` | `queued` | qualification/readme audit pending |
| [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #4 → `714e44bb` |
| [NeonShift-X](https://github.com/Swir/NeonShift-X) | `main` | `queued` | qualification/readme audit pending |
| [IPTV-checker](https://github.com/Swir/IPTV-checker) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #2 → `c1b113e` |
| [ASCITEXT](https://github.com/Swir/ASCITEXT) | `main` | `queued` | qualification/readme audit pending |
| [Github_Webste](https://github.com/Swir/Github_Webste) | `main` | `queued` | qualification/readme audit pending |
| [Dreambox-scaner](https://github.com/Swir/Dreambox-scaner) | `main` | `queued` | qualification/readme audit pending |
| [Torrent_downloaderv2](https://github.com/Swir/Torrent_downloaderv2) | `main` | `queued` | qualification/readme audit pending |
| [MacTrix](https://github.com/Swir/MacTrix) | `main` | `queued` | qualification/readme audit pending |
| [PowerBookmark](https://github.com/Swir/PowerBookmark) | `main` | `verified` | README v2 + SVG rollout verified on main; PR #1 → `64be655` |
| [Dragon-DiskForge](https://github.com/Swir/Dragon-DiskForge) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [Konofix](https://github.com/Swir/Konofix) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [check-out-of-hell](https://github.com/Swir/check-out-of-hell) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [xADKiller](https://github.com/Swir/xADKiller) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [SWIR_OS](https://github.com/Swir/SWIR_OS) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [Czateria_PLUS_Android](https://github.com/Swir/Czateria_PLUS_Android) | `main` | `queued` | qualification/readme audit pending |
| [Matrix-czat-pythom](https://github.com/Swir/Matrix-czat-pythom) | `main` | `queued` | qualification/readme audit pending |
| [KaliPhoneStudio](https://github.com/Swir/KaliPhoneStudio) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [SwirEngine](https://github.com/Swir/SwirEngine) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [GTT](https://github.com/Swir/GTT) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [Ryzen-5-5600G-A320M-](https://github.com/Swir/Ryzen-5-5600G-A320M-) | `main` | `queued` | qualification/readme audit pending |
| [Procent-calkulator](https://github.com/Swir/Procent-calkulator) | `main` | `queued` | qualification/readme audit pending |
| [Swirui](https://github.com/Swir/Swirui) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [Ghost-APK-Builder](https://github.com/Swir/Ghost-APK-Builder) | `main` | `queued` | qualification/readme audit pending |
| [CrossAim_power](https://github.com/Swir/CrossAim_power) | `main` | `queued` | qualification/readme audit pending |
| [SwirPhoneOS](https://github.com/Swir/SwirPhoneOS) | `main` | `delegated` | dedicated active development task; migration edits delegated |
| [Multichain-Tracker](https://github.com/Swir/Multichain-Tracker) | `main` | `queued` | qualification/readme audit pending |

State totals: **15 verified + 35 queued + 1 blocked + 12 delegated + 3 excluded = 66 owner repositories**.

## Work owned by other active tasks

The following remain delegated rather than edited by this migration task: `SWIR_OS`, `SwirEngine`, `Swirui`, `SwirPhoneOS`, `KaliPhoneStudio`, `Dragon-DiskForge`, `GTT`, `Tank-Revival-Overdrive`, `Nes_New_Life`, `check-out-of-hell`, `Konofix` and `xADKiller`.

Their README/SVG compliance may be audited, but documentation edits remain with their dedicated task while it is active to avoid competing branches and stale rewrites.

## Verified migrations

| Repository | Merge / evidence | README v2 | SVG PRO | Verification note |
|---|---|---:|---:|---|
| Image-To-Ico | README PR #1; SVG PR #2 → `dba8219` | ✅ | ✅ | main read-back; docs path had no dedicated PR CI |
| IPTV-checker | PR #2 → `c1b113e` | ✅ | ✅ | migration CI passed; main read-back |
| Gist_manager | PR #3 → `c22fde0` | ✅ | ✅ | migration CI passed; main read-back |
| WojThom | PR #8 → `ba38c17` | ✅ | ✅ | main README/card read back; no app-CI claim |
| PowerBookmark | PR #1 → `64be655` | ✅ | ✅ | main README/card read back |
| InfoPulse-PL | PR #1 → `1639025` | ✅ | ✅ | main README/card read back |
| WAV-to-MP3-converter | PR #1 → `5283cc87` | ✅ | ✅ | main README/card read back; no PR CI workflow |
| PolSilver_Bluetooth | PR #4 → `714e44bb` | ✅ | ✅ | CI `35280673281` passed Python 3.10–3.14 + Windows smoke |
| FASTIPTVPlayer | PR #4 → `3d996ef9` | ✅ | ✅ | CI `35280688386` passed Python 3.10–3.14 + Windows GUI smoke |
| Matrix_Windows_Commander | PR #4 → `5402a9d` | ✅ | ✅ | CI `35285949024` passed Python 3.10–3.14 + Windows GUI smoke |
| BackgroundPXR | PR #1 → `c640e8f` | ✅ | ✅ | Windows workflow `35286106534` passed |
| SwirPhotoClean | PR #1 → `50f2d2a` | ✅ | ✅ | Windows workflow `35286267897` passed tests/build/packaged EXE smoke; STATUS.md 6/7 gate |
| Hex-kolor | PR #1 → `b0971040` | ✅ | ✅ | main README/card read back; no PR CI workflow; Tkinter install guidance corrected |
| Driver-tool | PR #1 → `977c05ec` | ✅ | ✅ | main README/card read back; no PR CI workflow; simulation-only update documented |
| Youtube-VLC | PR #3 → `6bc578f1` | ✅ | ✅ | CI `35290479980` passed Python 3.10–3.14 + Windows GUI smoke; main README/card read back |

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
| 2026-09-18 | Migrated WAV-to-MP3-converter, PolSilver_Bluetooth and FASTIPTVPlayer. | 9 verified; priority subset 9/13. |
| 2026-09-18 | Migrated Matrix_Windows_Commander, BackgroundPXR and SwirPhotoClean. | 12 verified; priority subset 12/13; overall progress N/A. |
| 2026-09-18 | Migrated Hex-kolor, Driver-tool and Youtube-VLC. Corrected Hex Tkinter install guidance, documented Driver Tool's simulation-only update path, and preserved VLCTube v3.1 behavior/safety. VLCTube PR CI passed Python 3.10–3.14 and Windows GUI smoke. Final README/progress cards were read back from `main`. | **15 verified; 35 queued; 1 blocked; 12 delegated; 3 excluded.** Initial priority remains 12/13 because Aria2Gui is blocked; overall progress remains N/A. Next: Spamer safety/eligibility review. |

Do not silently change the denominator. Every later `queued → excluded/delegated/verified/blocked` decision must update the inventory row, state totals, metrics marker and generated migration SVGs together. Disable only this migration task after every discovered repository has a final eligibility state and every eligible migration/SVG rollout is verified or explicitly excepted according to the completion policy.
