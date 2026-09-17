# SWIR README PRO Migration — Status

Documentation migration ledger for existing SWIR projects. This is **README migration progress**, not application development, release readiness or runtime verification.

Canonical standards: [SWIR README PRO v2](SWIR-README-STANDARD.md) · [SWIR Progress SVG PRO](SWIR-PROGRESS-STANDARD.md).

<!-- MIGRATION-METRICS owner=66 verified=3 queued=48 delegated=12 excluded=3 priority_verified=3 priority_total=13 eligibility=INCOMPLETE -->

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-card.svg" alt="SWIR README PRO migration overall progress — N/A while eligibility review is incomplete" />
</p>

## Run status

| Item | Current state |
|---|---|
| Started | 2026-09-17 |
| Owner repositories discovered | **66**; repository search page 2 was empty, so the owner-level inventory is finite for this snapshot |
| Verified migrations | **3** — Image-To-Ico, IPTV-checker, Gist_manager |
| SVG rollout verified | **3** — the same three repositories |
| Queued / qualification pending | **48** |
| Delegated to dedicated active tasks | **12** |
| Structural exclusions recorded | **3** |
| Initial priority subset | **3 / 13 = 23.1% verified** |
| Overall migration percentage | **N/A** until every queued owner repository receives a final eligibility decision |
| Next priority | **WojThom**, then Aria2Gui and PowerBookmark |
| Completion policy | Final eligibility audit → all eligible repos verified or explicitly excepted → final audit/report → disable only this migration task |

<p align="center">
  <img width="100%" src="assets/readme/migration/progress-mini.svg" alt="Initial priority subset progress — 3 of 13 repositories verified" />
</p>

The mini bar above is **only the initial 13-repository priority subset**. It is not the overall migration percentage. The overall card stays **N/A** while 48 discovered repositories still need qualification/README review and may later move to `verified`, `excluded`, `delegated` or another justified state.

## Status contract

- `queued`: repository is discovered but still needs qualification and/or migration work.
- `in_progress`: actual migration branch/PR exists; record its link and exact head.
- `verified`: final README and required assets were read back on the default branch after the appropriate checks and merge.
- `blocked`: a concrete unresolved obstacle; record evidence and required action.
- `excluded`: outside migration scope with a specific reason; never counted as migrated.
- `delegated`: another active project task owns documentation changes; never counted as this task's verified migration.

A v2 marker, uploaded banner, open PR or green source CI alone does not prove a complete migration. Verify branding, paths, truthful claims, installation, release links, visible Search Keywords, SWIR footer and Progress SVG PRO state where applicable.

## Initial priority queue

| Order | Repository | State | Current evidence / next step |
|---|---|---|---|
| 1 | [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `verified` | README v2 via PR #1; SVG rollout via [PR #2](https://github.com/Swir/Image-To-Ico/pull/2), merged as `dba8219`. Main README and progress card read back. |
| 2 | [IPTV-checker](https://github.com/Swir/IPTV-checker) | `verified` | [PR #2](https://github.com/Swir/IPTV-checker/pull/2) merged as `c1b113e`; PR CI passed; main README/progress card read back. |
| 3 | [Gist_manager](https://github.com/Swir/Gist_manager) | `verified` | [PR #3](https://github.com/Swir/Gist_manager/pull/3) merged as `c22fde0`; PR CI passed; main README/progress card read back. |
| 4 | [WojThom](https://github.com/Swir/WojThom) | `queued` | Next full source/release/README qualification and migration candidate. |
| 5 | [Aria2Gui](https://github.com/Swir/Aria2Gui) | `queued` | Inspect current README/assets first; preserve any superior existing presentation. |
| 6 | [PowerBookmark](https://github.com/Swir/PowerBookmark) | `queued` | Inspect scope and current browser-extension/bookmarklet documentation before editing. |
| 7 | [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `queued` | Preserve justified localization after source review. |
| 8 | [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `queued` | Inspect before deciding changes. |
| 9 | [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `queued` | Verify platform limits and authorized diagnostic scope. |
| 10 | [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `queued` | Inspect before deciding changes. |
| 11 | [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `queued` | Inspect before deciding changes. |
| 12 | [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `queued` | Inspect current app state, README assets and releases. |
| 13 | [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `queued` | Inspect current app state, README assets and releases. |

## Complete owner inventory snapshot

The list below was captured from the owner repository search with `per_page=100`; the second page returned no repositories. This is a **complete owner-level discovery snapshot**, but not yet a final eligible-migration denominator. `queued` entries still require content, fork, safety, legal and project-state qualification before they can be counted in final completion math.

| Repository | Default branch | State | Note |
|---|---|---|---|
| [Hex-kolor](https://github.com/Swir/Hex-kolor) | `main` | `queued` | qualification/readme audit pending |
| [swir.github.io](https://github.com/Swir/swir.github.io) | `main` | `excluded` | portfolio/status site, not a README migration target |
| [Aria2Gui](https://github.com/Swir/Aria2Gui) | `main` | `queued` | qualification/readme audit pending |
| [Driver-tool](https://github.com/Swir/Driver-tool) | `main` | `queued` | qualification/readme audit pending |
| [Youtube-VLC](https://github.com/Swir/Youtube-VLC) | `main` | `queued` | qualification/readme audit pending |
| [Spamer](https://github.com/Swir/Spamer) | `main` | `queued` | eligibility/safety review required before any edit |
| [plugin.swir](https://github.com/Swir/plugin.swir) | `master` | `queued` | qualification/readme audit pending |
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `main` | `verified` | README v2 + SVG rollout verified on main |
| [Transformer-3-Pro-T303UA-i5-6200-hackintosh](https://github.com/Swir/Transformer-3-Pro-T303UA-i5-6200-hackintosh) | `main` | `queued` | qualification/readme audit pending |
| [Tank-Revival-Overdrive](https://github.com/Swir/Tank-Revival-Overdrive) | `main` | `delegated` | dedicated active development task |
| [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `main` | `queued` | qualification/readme audit pending |
| [XBookmark](https://github.com/Swir/XBookmark) | `main` | `queued` | qualification/readme audit pending |
| [Worker-Time-list-generator](https://github.com/Swir/Worker-Time-list-generator) | `main` | `queued` | qualification/readme audit pending |
| [WojThom](https://github.com/Swir/WojThom) | `main` | `queued` | qualification/readme audit pending |
| [keygenerator](https://github.com/Swir/keygenerator) | `main` | `queued` | purpose/safety review required before any edit |
| [Y6-gamestick](https://github.com/Swir/Y6-gamestick) | `main` | `excluded` | metadata reports size 0; do not invent a product |
| [SwirTube](https://github.com/Swir/SwirTube) | `main` | `queued` | qualification/readme audit pending |
| [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `main` | `queued` | qualification/readme audit pending |
| [Swir](https://github.com/Swir/Swir) | `main` | `excluded` | profile repo; only migration standards/ledger/tooling are maintained here |
| [File.io_Downloaderup](https://github.com/Swir/File.io_Downloaderup) | `main` | `queued` | qualification/readme audit pending |
| [Nes_New_Life](https://github.com/Swir/Nes_New_Life) | `main` | `delegated` | dedicated active development task |
| [TimeListe-Generator](https://github.com/Swir/TimeListe-Generator) | `main` | `queued` | qualification/readme audit pending |
| [CyptoPriceWidget](https://github.com/Swir/CyptoPriceWidget) | `main` | `queued` | qualification/readme audit pending |
| [Matrix-Ajax-Chat](https://github.com/Swir/Matrix-Ajax-Chat) | `main` | `queued` | qualification/readme audit pending |
| [Ghos-DNS](https://github.com/Swir/Ghos-DNS) | `main` | `queued` | qualification/readme audit pending |
| [Torrent_downloader](https://github.com/Swir/Torrent_downloader) | `main` | `queued` | qualification/readme audit pending |
| [cda-pl](https://github.com/Swir/cda-pl) | `main` | `queued` | legal/content scope review required before any edit |
| [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `main` | `queued` | qualification/readme audit pending |
| [Koder](https://github.com/Swir/Koder) | `main` | `queued` | qualification/readme audit pending |
| [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `main` | `queued` | qualification/readme audit pending |
| [Gist_manager](https://github.com/Swir/Gist_manager) | `main` | `verified` | README v2 + SVG rollout verified on main |
| [Github-README-Generator](https://github.com/Swir/Github-README-Generator) | `main` | `queued` | qualification/readme audit pending |
| [watermark-remover](https://github.com/Swir/watermark-remover) | `main` | `queued` | qualification/readme audit pending |
| [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `main` | `queued` | qualification/readme audit pending |
| [Grosz](https://github.com/Swir/Grosz) | `main` | `queued` | qualification/readme audit pending |
| [Py-Converter-to-exe](https://github.com/Swir/Py-Converter-to-exe) | `main` | `queued` | qualification/readme audit pending |
| [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `main` | `queued` | qualification/readme audit pending |
| [Image-to-txt](https://github.com/Swir/Image-to-txt) | `main` | `queued` | qualification/readme audit pending |
| [Titanium-APK-Bulider](https://github.com/Swir/Titanium-APK-Bulider) | `main` | `queued` | qualification/readme audit pending |
| [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `main` | `queued` | qualification/readme audit pending |
| [czatpythom](https://github.com/Swir/czatpythom) | `main` | `queued` | qualification/readme audit pending |
| [NeonShift-X](https://github.com/Swir/NeonShift-X) | `main` | `queued` | qualification/readme audit pending |
| [IPTV-checker](https://github.com/Swir/IPTV-checker) | `main` | `verified` | README v2 + SVG rollout verified on main |
| [ASCITEXT](https://github.com/Swir/ASCITEXT) | `main` | `queued` | qualification/readme audit pending |
| [Github_Webste](https://github.com/Swir/Github_Webste) | `main` | `queued` | qualification/readme audit pending |
| [Dreambox-scaner](https://github.com/Swir/Dreambox-scaner) | `main` | `queued` | qualification/readme audit pending |
| [PowerBookmark](https://github.com/Swir/PowerBookmark) | `main` | `queued` | qualification/readme audit pending |
| [Torrent_downloaderv2](https://github.com/Swir/Torrent_downloaderv2) | `main` | `queued` | qualification/readme audit pending |
| [MacTrix](https://github.com/Swir/MacTrix) | `main` | `queued` | qualification/readme audit pending |
| [Dragon-DiskForge](https://github.com/Swir/Dragon-DiskForge) | `main` | `delegated` | dedicated active development task |
| [Konofix](https://github.com/Swir/Konofix) | `main` | `delegated` | dedicated active development task |
| [check-out-of-hell](https://github.com/Swir/check-out-of-hell) | `main` | `delegated` | dedicated active development task |
| [xADKiller](https://github.com/Swir/xADKiller) | `main` | `delegated` | dedicated active development task |
| [SWIR_OS](https://github.com/Swir/SWIR_OS) | `main` | `delegated` | dedicated active development task |
| [Czateria_PLUS_Android](https://github.com/Swir/Czateria_PLUS_Android) | `main` | `queued` | qualification/readme audit pending |
| [Matrix-czat-pythom](https://github.com/Swir/Matrix-czat-pythom) | `main` | `queued` | qualification/readme audit pending |
| [KaliPhoneStudio](https://github.com/Swir/KaliPhoneStudio) | `main` | `delegated` | dedicated active development task |
| [GTT](https://github.com/Swir/GTT) | `main` | `delegated` | dedicated active development task |
| [SwirEngine](https://github.com/Swir/SwirEngine) | `main` | `delegated` | dedicated active development task |
| [Ryzen-5-5600G-A320M-](https://github.com/Swir/Ryzen-5-5600G-A320M-) | `main` | `queued` | qualification/readme audit pending |
| [Procent-calkulator](https://github.com/Swir/Procent-calkulator) | `main` | `queued` | qualification/readme audit pending |
| [Swirui](https://github.com/Swir/Swirui) | `main` | `delegated` | dedicated active development task |
| [Ghost-APK-Builder](https://github.com/Swir/Ghost-APK-Builder) | `main` | `queued` | qualification/readme audit pending |
| [CrossAim_power](https://github.com/Swir/CrossAim_power) | `main` | `queued` | qualification/readme audit pending |
| [SwirPhoneOS](https://github.com/Swir/SwirPhoneOS) | `main` | `delegated` | dedicated active development task |
| [Multichain-Tracker](https://github.com/Swir/Multichain-Tracker) | `main` | `queued` | qualification/readme audit pending |

State totals are deliberately machine-checkable from `MIGRATION-METRICS`: **3 verified + 48 queued + 12 delegated + 3 excluded = 66 owner repositories**.

## Work owned by other active tasks

The following are delegated rather than edited by this migration task: `SWIR_OS`, `SwirEngine`, `Swirui`, `SwirPhoneOS`, `KaliPhoneStudio`, `Dragon-DiskForge`, `GTT`, `Tank-Revival-Overdrive`, `Nes_New_Life`, `check-out-of-hell`, `Konofix`, `xADKiller`.

Audit them for missing standards only when useful; do not compete with their active branches. Their own tasks are responsible for README v2 and Progress SVG PRO rollout.

## Completed migrations

| Repository | Date | PR / merged commit | README / SVG verification |
|---|---|---|---|
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | 2026-09-17 | README: [PR #1](https://github.com/Swir/Image-To-Ico/pull/1), `f7e83af`; SVG: [PR #2](https://github.com/Swir/Image-To-Ico/pull/2), `dba8219` | Main README blob `4115c575...`; v2 marker, 12 keywords, original hero/icon and prior source-test evidence preserved; progress card blob `851f2558...` reports N/A because no roadmap. No PR CI trigger exists, so no new CI/Windows runtime pass is claimed. |
| [IPTV-checker](https://github.com/Swir/IPTV-checker) | 2026-09-17 | [PR #2](https://github.com/Swir/IPTV-checker/pull/2), `c1b113e` | CI run `35269150780` passed on the final PR head. Main README blob `0763c42c...`; progress card blob `495f37fb...`. v2 hero, 12 keywords, current v2.0.0 Windows release, bounded health-check behavior and responsible-use limits verified from source/release evidence. |
| [Gist_manager](https://github.com/Swir/Gist_manager) | 2026-09-17 | [PR #3](https://github.com/Swir/Gist_manager/pull/3), `c22fde0` | CI run `35269318152` passed on the final PR head. Main README blob `a61a6863...`; progress card blob `88a87259...`. v2 hero, 12 keywords, v2.0.0 release assets and token/QSettings caveats preserved. |

### Image-To-Ico application issues outside documentation scope

The invalid legacy `requirements.txt` content and existing multi-image ICO export failure remain application-maintenance issues. The README documents them and provides a direct dependency-install workaround; documentation completion does not mark those runtime issues fixed.

## SVG rollout rules for this migration

- Each eligible migrated project receives `progress-card.svg`, `progress-mini.svg`, `progress-template.svg` and a deterministic generator/check.
- Legacy utilities without a trustworthy product roadmap report **N/A** product completion rather than inventing 0%, 100% or a documentation score.
- Release readiness, benchmark effectiveness and product completion remain separate measurements.
- This migration ledger uses dedicated assets under `assets/readme/migration/`; the profile `README.md` remains untouched.
- `tools/generate_migration_progress.py` reads the metrics marker above, checks that owner-state counts add up and validates the priority-subset fill math.

## Execution log

| Date | Work actually performed | Result |
|---|---|---|
| 2026-09-17 | Initial standards read and three-README triage. | Image-To-Ico, IPTV-checker and Gist_manager deficiencies identified. |
| 2026-09-17 | Image-To-Ico full README v2 migration, source/release review and bounded source smoke; PR #1 merged and read back. | First verified README migration. |
| 2026-09-17 | Migrated IPTV-checker and Gist_manager to README v2 + Progress SVG PRO on isolated branches. Verified source/release claims, created N/A product-progress graphics and deterministic checks, waited for successful PR CI, squash-merged, then read back main. | Verified migrations increased to 3; both CI-backed PRs passed. |
| 2026-09-17 | Retrofitted Image-To-Ico with Progress SVG PRO through PR #2 and read back main; no PR-triggered CI exists for that repo. | SVG rollout verified for all 3 currently migrated repos. |
| 2026-09-17 | Completed owner-level repository discovery: 66 repositories on page 1 and none on page 2. Recorded all names/default branches and provisional states; added machine-readable migration metrics and dedicated ledger progress graphics. | Owner discovery is finite; eligibility audit is still incomplete, so overall migration progress remains N/A. Next: WojThom. |

Do not silently change the denominator. Any later `queued → excluded/delegated/verified` decision must update the inventory row, state totals, metrics marker and generated SVGs together. Disable only this migration task after every discovered repository has a final eligibility state and every eligible migration/SVG rollout is verified or explicitly blocked with a required action.
