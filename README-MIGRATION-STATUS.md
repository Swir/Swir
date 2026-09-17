# SWIR README PRO Migration — Status

Documentation migration ledger for existing SWIR projects. This is **README migration progress**, not application development, release readiness or runtime verification.

Canonical standard: [SWIR README PRO v2](SWIR-README-STANDARD.md).

## Run status

| Item | Current state |
|---|---|
| Started | 2026-09-17 |
| Automation | SWIR README PRO Migration — hourly |
| Phase | First documentation migration merged and read back; full eligible-repository inventory pending |
| Initial READMEs inspected | 3 |
| Migrations verified in this queue | 1 — Image-To-Ico, completed interactively |
| Priority candidates below | 13 total, 1 verified and 12 queued; this is NOT the total migration scope |
| Next priority | IPTV-checker, then Gist_manager |
| Overall migration percentage | Not calculated until the full eligible inventory is recorded |
| Completion policy | Final audit, final report, then disable only the migration task |

The initial audit and first completed migration were performed interactively. This entry does not claim that a scheduled run has finished. Image-To-Ico is now migrated on its default branch; the original three-repository triage is retained below as historical evidence.

## Initial audit — 2026-09-17

These historical observations come from full README reads on each repository's default branch before migration. They do not assert that an unreferenced banner or icon was absent from a repository. Use the priority queue and completed-migrations table for current state.

| Repository | Observed README blob SHA | Findings at initial triage | Initial state |
|---|---|---|---|
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `d44f68d70d9c5dd11caec9227d52e9f01f0fa984` | No v2 marker or local hero reference in README; older mixed-color badges; eight keyword phrases under `Discoverability`, not the required `Search Keywords`; installation and feature claims needed source review. | `queued` |
| [IPTV-checker](https://github.com/Swir/IPTV-checker) | `3cd7732b9a67cf955cada331b5fb63046c744a09` | Existing project icon and useful detailed instructions; no v2 marker, local hero reference or Search Keywords section. Preserve stream-checking limits, authorization notes and launch/build instructions. | `queued` |
| [Gist_manager](https://github.com/Swir/Gist_manager) | `4474299926ce8326d19c04992c3467bfbe79fcac` | No v2 marker or local hero reference; seven phrases under `Discoverability`; project SVG listed in structure but not displayed in the header. Preserve token-handling caveats and verify the documented release against actual metadata. | `queued` |

Re-read the current branch and file SHA before any write. These blob SHAs are audit evidence, not a license to overwrite newer content.

## Priority queue

This is the initial preferred order, not an exhaustive inventory. Inspect repository metadata, README, source files, assets, release state and open pull requests before selecting each candidate.

| Order | Repository | State | Next step |
|---|---|---|---|
| 1 | [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | `verified` | [PR #1](https://github.com/Swir/Image-To-Ico/pull/1) merged; final README and both SVGs read back on main. Do not redo this migration. |
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

Check current ownership before each run. Audit these repositories without competing README rewrites. Record any actual deficiency as `delegated`, not `verified`. Their current README compliance was **not re-audited** during the initial three-repository triage or the Image-To-Ico migration.

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

| Repository | Date | PR / merged commit | Verification |
|---|---|---|---|
| [Image-To-Ico](https://github.com/Swir/Image-To-Ico) | 2026-09-17 | [PR #1](https://github.com/Swir/Image-To-Ico/pull/1), [f7e83af](https://github.com/Swir/Image-To-Ico/commit/f7e83af1130757a0af6e30fb08f6aab26b0605df) | v2 marker, 12 keywords, local hero/icon, truthful status and usage, source-based installation workaround, anchors/paths, SVG parsing/render review and offline 1280/390 px layout checks. Main README and both SVG contents match the locally checked files. |

Image-To-Ico verification evidence:

- README blob: `752332fb549b22be381e8a2a1820d22be8c341c5`.
- Hero blob: `bd77ed61504c3a2d27539b188085e1581c559684`.
- Project icon blob: `ee2839caa91ba5d989b469e343a39d8677daf0ff`.
- Original application source checked byte-for-byte: `dcd6943d6ff3b60b54942d3060a28c1aada2cb7d`.
- The PR changed exactly four documentation/artwork files. No application, dependencies, release workflow, version, license or binary changes.
- The existing workflow has no PR trigger. Final PR head had no check runs or commit statuses; GitHub reported clean mergeability. Local verification is not presented as a new Windows CI pass.
- Bounded source smoke: PNG/JPG selection, Tk preview, actual single-image ICO export/reopening, empty selection, save cancellation and last-added removal passed under Linux/Xvfb. Existing two-input export failed with `KeyError: 'ICO'` and is documented, not claimed fixed. The published EXE was not tested.
- Full evidence and reproduction: [README-VERIFICATION.md](https://github.com/Swir/Image-To-Ico/blob/main/docs/README-VERIFICATION.md).

### Application issues found, outside documentation-migration scope

Image-To-Ico still needs separate application maintenance for its invalid requirements file and multi-image export behavior. The new README provides a usable direct dependency-install command and clearly limits the verified workflow to one image. Do not mark these underlying application issues resolved because the README migration is complete.

## Execution log

| Date | Work actually performed | Result |
|---|---|---|
| 2026-09-17 | Read canonical v2 standard; checked active task ownership; created the hourly migration task; read the complete READMEs of Image-To-Ico, IPTV-checker and Gist_manager. | Initial deficiencies recorded; no application README writes at that initial step. |
| 2026-09-17 | Completed Image-To-Ico source/release review, original-source smoke tests, project-specific artwork and full v2 README. Opened and squash-merged PR #1, then read back main README and both SVGs and matched their blob hashes to locally checked contents. | 1 verified migration. Existing runtime/dependency limitations documented without changing code or Releases. Next: IPTV-checker; full inventory still pending. |

On subsequent runs, update this ledger from fresh evidence rather than repeatedly appending planning-only entries. Report completed migrations, remaining work and exceptions separately. Disable only the migration task after its defined scope is actually finished and the final audit/report is complete.
