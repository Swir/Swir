<!-- SWIR-PROGRESS-SVG-PRO:v1 -->

# SWIR Progress SVG PRO

Canonical SVG progress presentation for SWIR project tasks, approved on 2026-09-17. This supplements [SWIR README PRO v2](SWIR-README-STANDARD.md); it does not replace project-specific roadmap mathematics, release gates or safety requirements.

## SVG-only progress visuals — user correction 2026-09-18

The user explicitly rejected the remaining old ASCII/text progress bars because they duplicate the approved SVG design. This is the current presentation requirement for all SWIR project tasks and the README migration task. It supersedes historical instructions to preserve, restore or regenerate a 20-segment ASCII/Unicode progress bar, including that part of SWIR ROADMAP STYLE LOCK v1. Keep the existing v1 structural markers for compatibility; the old text-bar requirement is retired, not the roadmap data contract.

- Use the approved SVG card in README and the compact SVG in the authoritative roadmap/status document. Do not show both card and mini for the same scope in the same section.
- Remove legacy character-based progress meters from maintained README, active roadmap/status dashboards and newly produced task reports. This includes block/shade/square meters and bracketed hash/equal/dash meters, not just files or sections explicitly named ASCII.
- Keep the exact measured scope, percentage, completed/remaining/total table, checklist and source reference. Accessible fallback is an ordinary sentence or numeric table, never another character-art bar.
- Remove an obsolete meter's otherwise-empty code fence or decorative wrapper, but preserve useful text beside it. Do not delete arbitrary code blocks, command examples, directory trees, unrelated ASCII artwork, data or source-code strings.
- Update documentation generators, templates and their presentation tests so the retired bar cannot return on the next run. Replace only tests that require the obsolete visual; retain or strengthen mathematical consistency, SVG validity, geometry, embedding and release/safety checks. Never bypass CI or remove checks wholesale.
- Revisit already migrated v2/SVG repositories that still contain these duplicated meters. An unchanged percentage is not a reason to postpone this one-time presentation correction. Respect repository ownership and open work; active project tasks fix their own repositories, the migration task fixes its eligible queue and migration ledger.
- If a valid SVG cannot yet be embedded or delivered, show plain verified numbers and the concrete blocker; do not reintroduce an ASCII bar as a fallback. Do not claim SVG delivery before it is actually available.
- This changes presentation only: do not increase progress, modify verified checklist states, loosen a release gate, change application behavior, rewrite published tags/releases, alter raw historical logs or edit already delivered task messages. Archived milestone evidence remains intact.

## Required delivery

At the next safe execution, implement the actual files and embeddings in the repository owned by the task. Do not substitute a proposal, a prompt snippet or a claim that the standard exists for implementation. An unchanged project percentage does not prevent the initial SVG rollout or legacy-meter cleanup.

- `assets/readme/progress-card.svg`: project-specific card near the README status section.
- `assets/readme/progress-mini.svg`: compact companion near the authoritative roadmap/status dashboard.
- `assets/readme/progress-template.svg`: valid, reusable local template, clearly labelled TEMPLATE / NOT PROJECT DATA; never embed it as live progress.
- A deterministic local generator or existing equivalent: derive the card and mini from the same authoritative data; provide a check mode or test that detects stale output and contradictory numbers.

Respect established paths and project ownership. A roadmap in `docs/` needs `../assets/readme/progress-mini.svg`, not an incorrectly rooted relative link. Keep protected roadmap markers, checklists, tables and verified numeric values intact. SVG replaces the legacy text meter as the progress visualization; ordinary Markdown numbers remain the accessible fallback. Do not weaken mathematical, release or safety checks.

## Visual specification

Use the approved dark electric-blue/cyan family: background `#02050A` / `#07111C`, primary gradient `#0088FF` to `#62E5FF`, bright text `#F4FAFF`, muted text `#8DA8B8`. Use rounded corners, a subtle border/grid, restrained glow and readable spacing; no rainbow or animated fake advancement.

Default card canvas: 1200 x 180, track x=50 and width=1100. Default compact canvas: 900 x 72, track x=170 and width=700. Expand height when necessary for a long project/scope label rather than overlapping text. Keep the family appearance consistent across projects.

Show the project name, measured scope (e.g. current milestone, hardware gate or README migration), computed percentage or N/A, status and a correctly labelled counter. Optional last-completed/next-step text must match the actual record. Repeat essential values as normal Markdown text beside the graphic.

SVG must have a valid viewBox, title/description and escaped text. Keep it self-contained: no scripts, external fonts, remote images, foreignObject, tracking or external dependencies. All numeric attributes must be finite valid numbers, never placeholders such as `width="XXX"`. Clip the fill to the track; at zero progress omit the fill/glow instead of showing a misleading luminous sliver. At 100% the fill may not exceed the track.

## One source of truth

Read the authoritative roadmap or structured progress ledger before generating output. Store source path, exact scope and the calculation method in generator configuration or verification notes, not as a second independently edited progress ledger.

For an ordinary unweighted checklist:

`fraction = verified_completed / total_in_scope`

`percentage = fraction * 100`

`fill_width = track_width * fraction`

Count only the canonical scope, not historical roadmaps, examples, template checklists or duplicated summaries. Use the unrounded fraction for geometry. Normally display one decimal place; do not round incomplete work up to 100.0%. Use extra precision or an explicit '<100%' when necessary.

Preserve an existing documented weighted calculation. For example, one of ten weighted milestones does NOT necessarily mean 10%; label the counter as milestones and explain that the percentage is weighted. Do not silently convert weighted project progress into a raw checkbox percentage. If a percentage has no reproducible basis, show N/A and state the missing evidence rather than copying an unsupported estimate.

An empty or unknown denominator is N/A, not 0% or 100%. Never infer completion from elapsed time, commit count, version numbers, generated scaffolding, test count or the existence of a release. A decoration-only change does not raise application progress.

Sanity example: 1 of 13 equally weighted items is 7.7%, not 73.0%. The displayed text, counter, fill, accessible description and Markdown summary must all agree.

## Scope and status

Use IN PROGRESS, BLOCKED, PLANNING, HARDENING or RELEASE PREP as appropriate. BLOCKED requires a named real blocker and may still have nonzero verified progress. COMPLETE applies only to the explicitly named, fully verified scope; a completed historical milestone does not make the current product complete. BETA READY requires the project's actual beta gate to have passed, including required runtime/hardware/manual evidence. Neither 100% nor green source CI automatically authorizes a release or task shutdown.

Maintain separate data for project completion, current milestone and release readiness when their scopes differ. Do not merge incomparable scopes for a nicer number.

For multi-project repositories, each active subproject owns its own SVG pair. The master may mirror that active project's exact labelled scope; do not average unrelated games. For dual-track projects, show Android and browser-extension progress separately unless an explicit combined model exists. Do not confuse ad-blocking benchmark percentages with development completion.

## README migration task

Apply these assets to all eligible repositories in the migration queue, including ones already migrated to README v2 but missing SVG progress or still displaying a duplicated legacy text meter. Preserve the queue's exclusions and avoid competing writes to repositories owned by active development tasks. Track legacy-meter cleanup separately from historical README/SVG completion evidence; do not silently claim previously verified repositories are already clean.

For a legacy utility with no trustworthy product roadmap, use a clearly labelled N/A product-progress card; do not invent an application-completion percentage or pretend that a documentation checklist measures software readiness.

The migration task's own graphics belong under `Swir/Swir/assets/readme/migration/` and are embedded in `README-MIGRATION-STATUS.md`, not the profile README. Until a complete eligible inventory exists, its overall percentage is N/A; a priority subset can be shown separately and explicitly labelled as that subset. Excluded, blocked and delegated entries are not completed migrations.

## Update, verification and reporting

1. Re-read current source/branch and ongoing work; do not overwrite concurrent edits.
2. Implement or update the generator, valid local template and two generated SVGs; retire legacy text-meter emission from maintained documentation outputs.
3. Embed the card and mini in the actual README/roadmap or established status document, each in its appropriate location. Remove the old character meter and any empty wrapper, retaining normal numeric fallback and the full roadmap data contract.
4. Verify source mathematics, XML validity, finite/bounded geometry, matching values, relative links, accessible text and absence of duplicated legacy meters in the edited dashboards. Cover zero, complete, partial, unknown/empty denominator and long labels; test weighted sources where used. Confirm regeneration does not restore the retired meter.
5. Render and inspect at desktop and narrow/mobile widths when tooling permits. State clearly when visual rendering or remote badge checks were not performed.
6. Follow existing branch/PR/CI policies; no force push, bypassed checks, version bump or release for this documentation change. No-op when inputs and outputs are unchanged.
7. Read back committed assets and embeddings. Only then report SVG rollout and legacy-meter cleanup as implemented, with commit/PR and links; otherwise report pending or blocked plus the concrete reason.

In automated reports, deliver the visible progress preview required below, link the exact committed SVG and include the exact textual progress as ordinary numbers, not a character-art bar. Saving or linking an SVG in GitHub is not equivalent to showing the progress card in the task's result message. Static committed SVGs update when regenerated from verified source changes.


## Concise remote notifications — HARD OUTPUT CAP 2026-09-18

This is the user's latest reporting preference and it OVERRIDES every older task-specific instruction that asks for a longer hourly/final report. It changes reporting verbosity only; all implementation, testing, CI, safety, roadmap, release and verification work remains unchanged.

For every normal remote-task run:
- Show the required verified SVG/PNG progress preview first when that task uses the SWIR progress system.
- After the preview output **no more than 5 short lines total**.
- Use only these fields when applicable: **Done**, **Commit/PR**, **Tests/CI**, **Progress/Blocker**, **Next**.
- Each line should normally be one sentence. Combine related facts instead of expanding them.
- Do NOT add tables, file inventories, repeated architecture/background explanations, repeated policy text, full test matrices, historical recap, long release-gate explanations, or a second summary.
- Do NOT repeat SVG status boilerplate unless it is abnormal; fold it into Progress/Blocker when needed.
- Do NOT list every changed file unless a specific file is the blocker.
- A normal successful hourly report should stay roughly within **60–120 words after the image**.
- If nothing meaningful changed, one or two lines are enough.

A longer report is allowed only for a real exception: failed CI needing diagnosis, destructive/safety risk, release publication, major compatibility break, important scope change, or explicit user action required. Even then, lead with the five-line summary and add only the minimum explanation necessary.

This HARD OUTPUT CAP supersedes any older sentence in an individual task prompt such as “report all changed areas/files/tests/statuses” when those details can be compressed into the five lines above. It does not permit hiding a blocker, inventing success, skipping required work, weakening verification, or changing schedules.
## Visible remote-task reports — correction 2026-09-18

This reporting requirement supersedes the previous optional-inline-rendering sentence. It applies to each project task and to the README migration task that reads this standard, without changing its development scope, schedule, release gate or repository ownership.

- Begin each substantive final task report with a visible preview of the actual progress card, followed by its measured scope, exact counter/percentage and source commit/branch. Preserve the approved SVG artwork as the source; do not replace it with an AI mockup or manually invented numbers. Do not add an ASCII/Unicode meter below or instead of the preview.
- When direct SVG display is not supported or has not been verified for the output channel, rasterize that exact validated SVG to PNG with an available renderer, inspect the result and embed the PNG as an image in the report. Also provide the original SVG as an attachment or a verified committed-file link. PNG is only the display copy; SVG remains the canonical design.
- Use a real output attachment or a verified accessible image URL supported by the execution environment. Never invent a sandbox path, reuse an inaccessible file from a previous run, emit raw SVG code as though it were an image, or claim an image is visible merely because a link was sent. Do not expose credentials or private repository content through public image hosting.
- Keep image and text tied to the same verified source snapshot. If the graphic exists only on a development branch, label that branch and report default-branch rollout as pending. Never merge unrelated application changes to make a progress image visible. If a new percentage has not passed its verification gate, show the last verified state and describe pending work separately.
- For the migration report, use its own ledger card, not an arbitrary application's progress. Overall N/A and any separately named priority subset must remain honest. Unknown product progress is still displayed as N/A, never silently converted into 0%.
- If rendering or delivery is unavailable, state `Report preview: blocked` with the concrete limitation, then provide verified text and the SVG link. Do not repeatedly report full visual completion while this delivery step is missing. If the preview is attached but client-side display was not observable, say it was attached; do not claim to have verified the user's screen.
- Distinguish `Repository SVG: main / development branch / missing` from `Report preview: attached / blocked` and `Legacy meter cleanup: verified / pending / blocked`. Record the actual file/ref. Keep the report compact and retain all required project-specific test, blocker and release information.

This changes the contents of task-result messages only. It does not customize the built-in ChatGPT task-list cards, edit already delivered historical reports, or provide a live execution-time meter. Do not promise those capabilities.

## Development / default-branch publication cadence — user correction 2026-09-19

Before repository work, read and follow [SWIR-DEVELOPMENT-CADENCE.md](SWIR-DEVELOPMENT-CADENCE.md). That file defines the current user-approved split between hourly development and less-frequent default-branch integration, including a project-specific preferred cadence table.

This cadence rule OVERRIDES older task-specific instructions that require committing, pushing or merging directly to `main` on every hourly run. Hourly development continues unchanged; when cross-run persistence is needed, use the existing feature/development branch and PR. Merge to the default branch only when a coherent package is complete and the required exact-head checks are green. Quality/safety/release gates always override the clock.

## Rollout priority and preservation

Initial SVG adoption and removal of duplicated legacy meters are required at the next safe run, not indefinitely postponed until another milestone. Finish any in-flight conflicting work first, then integrate the documentation package without changing application behavior. Preserve README PRO v2 and Search Keywords, unique branding, all safety/compatibility requirements, release freezes and roadmap structural markers, checklist data and numeric tables. The old text-meter portion of roadmap style locks is explicitly superseded by the user's SVG-only correction above. Historical README v1 references must not downgrade an existing v2 README. Task schedules and enabled states remain unchanged by this standard.
