# SWIR Development Cadence

<!-- SWIR-DEVELOPMENT-CADENCE:v1 -->

User-approved repository publication policy — 2026-09-19.

## Core rule

**Work every hour; do not merge to the default branch every hour.**

Hourly automations still inspect current state, implement real code, run tests, fix regressions and continue unfinished work. GitHub publication is split into two layers:

1. **Development checkpoint** — use an existing feature/development branch and PR when cross-run persistence is needed. A checkpoint may be pushed before the package is merge-ready so work is not lost.
2. **Default-branch integration** — merge to `main`/the repository default branch only after a coherent, meaningful package is complete and the required checks for the exact final head are green.

This policy supersedes older task-specific wording that says to commit/push/merge directly to `main` on every hourly run. It does **not** weaken CI, testing, release, safety, roadmap, evidence or ownership requirements.

## General publication rules

- Do not create a commit merely because one hour elapsed.
- Prefer one coherent functional package over multiple cosmetic/micro commits.
- Continue an existing branch/PR across hourly runs instead of opening parallel work for the same scope.
- Checkpoint commits on a development branch are allowed when needed for persistence, review, CI or recovery, but keep them meaningful and squash/clean up when appropriate before integration.
- Merge early only for a verified urgent regression/hotfix, security/safety correction, or blocker that must land before other work can continue.
- Never merge red or still-running required CI.
- If the preferred time window has elapsed but the package is not coherent/green, keep working; the clock never overrides quality.
- If a complete milestone becomes green earlier than the preferred window, it may be merged earlier.
- Releases remain governed by each project's separate release gate; a merge cadence is not a release cadence.
- Progress percentages may increase only after the underlying verified scope is actually satisfied, regardless of branch age.

## Project-specific preferred integration cadence

These are **targets, not deadlines**. The quality gate always wins.

| Repository / task | Preferred default-branch integration cadence | Integration trigger |
| --- | --- | --- |
| `Swir/BrokeDJ` | about **4–6 h** | coherent audio/UX/core slice + exact-head CI |
| `Swir/SWIR_OS` | about **4–6 h** | coherent Desktop/System milestone slice + exact-head CI |
| `Swir/SwirPhoneOS` | about **4–6 h** | coherent OS/app/device-foundation slice + exact-head CI |
| `Swir/KaliPhoneStudio` | about **4–6 h** | coherent safety/porting/evidence slice + exact-head CI |
| `Swir/SwirEngine` | about **2–4 h** | coherent engine milestone/quality slice + exact-head CI |
| `Swir/Swirui` | about **2–4 h** | coherent renderer/widget/runtime slice + exact-head CI |
| `Swir/Dragon-DiskForge` | about **2–4 h** | coherent capability/milestone slice + exact-head CI |
| `Swir/Konofix` | about **2–4 h** | coherent P2P/security/UX slice + exact-head CI |
| `Swir/GTT` | usually **2–4 h**, milestone-driven | coherent playable gameplay package + relevant green gates |
| `Swir/Tank-Revival-Overdrive` | usually **2–4 h**, milestone-driven | coherent playable warfare package + Windows qualification |
| `Swir/check-out-of-hell` | usually **2–4 h**, milestone-driven | coherent playable level/gameplay package + relevant green gates |
| `Swir/Nes_New_Life` Project #002 | usually **2–4 h**, evidence-driven | coherent launcher/HD/gameplay slice + green CI/evidence |
| `Swir/xADKiller` | about **2–3 h** per Android/Chrome track | coherent protection/privacy/UX slice + track-specific green CI |
| `Swir/BackgroundPXR` | about **2–3 h** | coherent Studio/AI/UX/reliability slice + Windows CI |
| `Swir/SwirPhotoClean` | about **2–3 h** | coherent scanner/UX/safety slice + Windows CI |

## Reporting

Hourly reports should distinguish:
- **worked/checkpointed on development branch** from
- **integrated to default branch**.

Do not describe a checkpoint branch as shipped/default-branch work. When no integration occurs because the package is still being accumulated or CI is running, that is normal and should be reported briefly rather than forcing a commit.


## Remote-write throttle — user correction 2026-09-19

The user explicitly does **not** want routine GitHub writes every hourly run. Hourly execution remains enabled, but normal remote repository writes must be throttled.

- **Do not create a GitHub commit, push, PR update, or default-branch merge merely to preserve hourly work.**
- Between publication windows, use the run for repository/CI review, diagnosis, test/result inspection, planning the next coherent package, review of an existing PR, or fixing only when a remote write is immediately justified by an actual blocker.
- The preferred cadence table above now applies to **all routine remote writes**, not only merges to the default branch.
- During a normal publication window, bundle the coherent change into the **fewest practical commits**. Prefer one meaningful commit/package when the connector/workflow allows it. Do not split code/docs/tests into many minute-apart commits just because separate API calls are convenient.
- Do not push a new checkpoint every hour. A development branch is for a real coherent package, not an hourly heartbeat.
- Exception: a verified urgent regression/security/safety fix, a CI repair required to unblock an already-open package, or recovery from a failed/incomplete remote operation may be pushed immediately.
- If the environment cannot preserve unpushed local edits between hourly runs, do **not** fake persistence. Use non-writing work on intermediate runs and perform implementation during the next allowed publication window.
- The user prefers fewer, higher-confidence GitHub updates over continuous visible activity. Quality and truthful verification matter more than commit frequency.
