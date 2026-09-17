# SWIR README PRO Migration — Status

Documentation migration ledger for existing SWIR projects. This is **README migration progress**, not application development, release readiness or runtime verification.

Canonical standard: [SWIR README PRO v2](SWIR-README-STANDARD.md).

## Run status

| Item | Current state |
|---|---|
| Started | 2026-09-17 |
| Automation | SWIR README PRO Migration — hourly |
| Phase | Initial README triage; full eligible-repository inventory pending |
| Initial READMEs inspected | 3 |
| Migrations verified by this task | 0 |
| Priority candidates below | 13; this is NOT the total migration scope |
| Overall migration percentage | Not calculated until the full eligible inventory is recorded |
| Completion policy | Final audit, final report, then disable only the migration task |

The scheduled task has been created. Its first completed scheduled run has not been verified in this initial entry. The initial audit below was performed interactively and made no changes to the three application repositories.

## Initial audit — 2026-09-17

These observations come from full README reads on each repository's default branch. They do not assert that an unreferenced banner or icon is absent from the repository; asset trees, application sources and release metadata still need inspection before migration.

| Repository | Observed README blob SHA | Findings | State |
|---|---|---|---|
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `d44f68d70d9c5dd11caec9227d52e9f01f0fa984` | No v2 marker or local hero reference in README; older mixed-color badges; eight keyword phrases under `Discoverability`, not the required `Search Keywords`; installation and feature claims need source review. | `queued` |
| [IPTV-checker](https://github.com/Swir/IPTV-checker) | `3cd7732b9a67cf955cada331b5fb63046c744a09` | Existing project icon and useful detailed instructions; no v2 marker, local hero reference or Search Keywords section. Preserve stream-checking limits, authorization notes and launch/build instructions. | `queued` |
| [Gist_manager](https://github.com/Swir/Gist_manager) | `4474299926ce8326d19c04992c3467bfbe79fcac` | No v2 marker or local hero reference; seven phrases under `Discoverability`; project SVG listed in structure but not displayed in the header. Preserve token-handling caveats and verify the documented release against actual metadata. | `queued` |

Re-read the current branch and file SHA before any write. These blob SHAs are audit evidence, not a license to overwrite newer content.

## Priority queue

This is the initial preferred order, not an exhaustive inventory. Inspect repository metadata, README, source files, assets, release state and open pull requests before selecting each candidate.

| Order | Repository | State | Next step |
|---|---|---|---|
| 1 | [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `queued` | Inspect sources/assets/releases; prepare complete v2 documentation change. |
| 2 | [IPTV-checker](https://github.com/Swir/IPTV-checker) | `queued` | Retain useful existing content; add project hero and accurate keywords. |
| 3 | [Gist_manager](https://github.com/Swir/Gist_manager) | `queued` | Verify launch/release details; display its own icon and migrate layout. |
| 4 | [WojThom](https://github.com/Swir/WojThom) | `queued` | Inspect before deciding changes. |
| 5 | [Aria2Gui](https://github.com/Swir/Aria2Gui) | `queued` | Inspect before deciding changes; preserve project-specific instructions. |
| 6 | [PowerBookmark](https://github.com/Swir/PowerBookmark) | `queued` | Inspect before deciding changes. |
| 7 | [InfoPulse-PL](https://github.com/Swir/InfoPulse-PL) | `queued` | Inspect before deciding changes; retain justified localization. |
| 8 | [WAV-to-MP3-converter](https://github.com/Swir/WAV-to-MP3-converter) | `queued` | Inspect before deciding changes. |
| 9 | [PolSilver_Bluetooth](https://github.com/Swir/PolSilver_Bluetooth) | `queued` | Verify platform limits and authorized diagnostic scope. |
| 10 | [FASTIPTVPlayer](https://github.com/Swir/FASTIPTVPlayer) | `queued` | Inspect before deciding changes. |
| 11 | [Matrix_Windows_Commander](https://github.com/Swir/Matrix_Windows_Commander) | `queued` | Inspect before deciding changes. |
| 12 | [BackgroundPXR](https://github.com/Swir/BackgroundPXR) | `queued` | Inspect before deciding changes. |
| 13 | [SwirPhotoClean](https://github.com/Swir/SwirPhotoClean) | `queued` | Inspect before deciding changes. |

After these priorities, continue through **all remaining eligible owned repositories** discovered by a complete paginated inventory. Do not stop merely because this priority list is exhausted. Record the complete finite scope and its denominator explicitly; log any later additions or exclusions.

## Work owned by other active tasks

At setup, dedicated development tasks already cover `SWIR_OS`, `SwirEngine`, `Swirui`, `SwirPhoneOS`, `KaliPhoneStudio`, `Dragon-DiskForge`, `GTT`, `Tank-Revival-Overdrive`, `Nes_New_Life`, `check-out-of-hell`, `Konofix` and `xADKiller`.

Check current ownership before each run. Audit these repositories without competing README rewrites. Record any actual deficiency as `delegated`, not `verified`. Their current README compliance was **not re-audited** during this initial three-repository triage.

The profile README in `Swir/Swir` and the portfolio site `swir.github.io` are not redesign targets. This ledger may be maintained in the profile repository without changing the profile page.

## Verification and status contract

- `queued`: awaiting full review or implementation.
- `in_progress`: actual migration branch/PR exists; record its link and exact head.
- `verified`: final README and assets have been read back on the default branch after appropriate checks and merge; record commit and verification scope.
- `blocked`: a concrete unresolved obstacle; record evidence and the required action.
- `excluded`: outside scope, with an explicit reason; never counted as migrated.
- `delegated`: another active task owns the work; never counted as this task's completed migration.

A v2 marker, an updated prompt, an uploaded banner, an open PR or green source CI alone does not demonstrate a complete README migration.

Verify readable project branding, actual local image references, SVG/XML validity and rendering where available, accurate badges, a textual project name/description, usable installation instructions, explicit compatibility, preserved important content, valid navigation and release links, a visible `## 🔎 Search Keywords` section with 8–20 relevant phrases, and a SWIR footer. Preserve superior existing artwork. Never claim a preview render, working install or runtime test that was not performed.

Use current source/release evidence; do not turn old README claims into new guarantees. Do not change program behavior, dependencies, versions, release tags, published assets or licenses as part of a documentation migration. Respect branch protection and required checks. A blocked migration must not prevent useful work on independent queued repositories.

Do not rebrand unrelated upstream forks, unarchive repositories, invent products for empty repositories, publish private project details, or improve the promotion or use instructions of abusive software. Record justified exceptions separately.

## Completed migrations

None verified by this migration task yet.

## Execution log

| Date | Work actually performed | Result |
|---|---|---|
| 2026-09-17 | Read canonical v2 standard; checked active task ownership; created the hourly migration task; read the complete READMEs of Image-To-Ico, IPTV-checker and Gist_manager. | Initial deficiencies recorded; application README writes not yet performed; full inventory and migrations remain pending. |

On subsequent runs, update this ledger from fresh evidence rather than repeatedly appending planning-only entries. Report completed migrations, remaining work and exceptions separately. Disable only the migration task after its defined scope is actually finished and the final audit/report is complete.
