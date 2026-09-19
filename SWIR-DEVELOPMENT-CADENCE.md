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


## Remote development persistence — user correction 2026-09-19

The user wants **maximum real engineering progress on every hourly run** while still avoiding noisy default-branch churn. Remote tasks cannot rely on an unpushed local workspace surviving into the next run, so meaningful implementation must be allowed to persist on a development branch.

### Hourly development branch rule

- Every hourly run should make the **largest safe, coherent, high-impact implementation step** it can actually complete and verify. Do not downgrade a run into analysis-only work merely because the default-branch merge window has not arrived.
- When a real code/test/UX/gameplay package is implemented and verified enough to preserve, **push it to the existing development/feature branch and update the same PR**. This is allowed even when less than the default-branch integration interval has elapsed.
- Prefer **one coherent remote checkpoint per run at most**. Bundle code, tests and necessary docs together where practical instead of producing many minute-apart commits.
- A development-branch checkpoint must contain meaningful implementation, a regression fix, a measurable test/benchmark improvement, or a concrete blocker-removal step. Never create heartbeat, timestamp, report-only or cosmetic-only commits just to prove activity.
- Continue the same active branch/PR across runs. Do not create a fresh branch every hour for the same milestone.
- If a run can safely finish more than one tightly related roadmap deliverable in one package, do so. **MAX WORK takes precedence over artificial small-scope commits.**
- A green checkpoint on a development branch is not shipped/default-branch work and must be reported as such.

### Default-branch integration throttle

The project-specific cadence table applies to **merges/integration into the default branch**, not to meaningful development-branch persistence.

- BrokeDJ, SWIR OS, SwirPhoneOS, KaliPhoneStudio: target default-branch integration about **4–6 h**.
- SwirEngine, SwirUI, Dragon DiskForge, Konofix: about **2–4 h**.
- GTT, Tank Revival, Checkout of Hell, Tiny Toon when enabled: usually **2–4 h**, milestone-driven.
- xADKiller, BackgroundPXR, SwirPhotoClean: about **2–3 h**.
- Merge earlier only when a substantial milestone is fully coherent and exact-head required CI is green, or for a verified urgent hotfix/safety/security blocker.
- Never delay useful development-branch implementation simply to satisfy the merge clock.
- Never merge red or still-running required CI.

### Progress-first / big-step behavior

- Start each run from the authoritative roadmap/status and identify the highest-value open deliverables.
- Prefer implementation that **closes or materially advances real roadmap scope** over repeated auditing, presentation work, documentation-only hardening or extra framework layers.
- When several related open checklist items can safely be completed in one run, intentionally pursue the larger package.
- Do not game percentages. A gate/checklist item changes only when its acceptance evidence is real.
- If a gate is physically blocked by hardware/manual/user evidence, do not burn every hourly run re-auditing the same blocker. Move to the next safe high-impact implementation that prepares or advances another real deliverable, while keeping the blocker truthful.
- The goal is visible engineering movement: larger gameplay/features/runtime systems, stronger integration and closed roadmap items — not a high commit count.

### Commit shape

A normal productive run should usually end in one of these states:

1. **Large coherent branch checkpoint + green/pending CI** — normal and preferred.
2. **Merge of an accumulated green package to default branch** — only when the integration cadence and quality gate justify it.
3. **No remote write** — only when genuinely blocked, waiting for CI/evidence, or when no safe meaningful change exists.

Multiple minute-apart commits in one run are discouraged. They are acceptable only when needed to repair the same exact-head package after CI failure or because the connector requires staged writes; squash/clean history when appropriate before integration.

## Reporting

Keep the existing concise-report rule. Distinguish:
- **development branch progress**,
- **default-branch integration**,
- **release readiness**.

Do not describe a branch checkpoint as shipped. A run that makes a substantial branch package is real progress even when the main percentage cannot truthfully change yet.
