<!-- SWIR-README-STANDARD:v2 -->

# SWIR README PRO v2 — Canonical Repository Standard

This file is the canonical README design and content standard for maintained `Swir/*` projects.

The goal is **one instantly recognizable SWIR family** across repositories without making every README a clone. Each project keeps its own identity, icon, screenshots, wording, features and technology stack while sharing a premium visual system, information architecture and discoverability rules.

The visual reference is the current SWIR GitHub profile: deep dark surfaces, electric cyan/blue energy lines, clean geometry and strong readability. ARIA2 Ultimate PRO remains a useful information-hierarchy reference, but this v2 standard takes precedence.

## 1. Core visual identity

Use the current SWIR profile language:

- base: `#02050A`
- dark surface: `#07111C`
- primary electric cyan: `#62E5FF`
- secondary blue: `#0088FF`
- muted text: `#8DA8B8`
- bright text: `#F4FAFF`
- subtle grid/electric-line motifs instead of noisy hacker decoration
- clean spacing and strong hierarchy
- no rainbow badge walls, excessive GIFs or visual clutter

The family should feel related to the profile, not like a generic template marketplace README.

## 2. Project hero system — required for major maintained projects

Every major maintained project should have its own local hero asset:

```text
assets/readme/hero.svg
```

Recommended canvas:

```text
1200 × 320 px
```

The hero should normally contain:

- a subtle `SWIR PROJECT` family label;
- the project's own icon or simple symbolic mark;
- project name in large type;
- one short descriptive tagline;
- one compact category/platform line;
- restrained electric cyan/blue accents;
- dark profile-compatible background;
- no fake metrics, fake version numbers or unsupported platform claims.

Preferred README opening:

```html
<div align="center">

<img width="100%" src="assets/readme/hero.svg" alt="PROJECT NAME — short project description" />

<br>

<!-- 3–5 primary badges -->
<!-- optional secondary row: Author / Stars / Release / License -->

</div>
```

Keep an accessible Markdown/HTML project description in the README even when the title appears inside the SVG. The banner must not be the only source of essential information.

### Hero family rules

All SWIR hero assets should share:

- the same dark/cyan visual DNA;
- comparable margins and typography hierarchy;
- the same small `SWIR PROJECT` family signal;
- similar electric-line/grid treatment;
- local project iconography and project-specific subtitle.

They must **not** share another project's icon, screenshots or feature claims.

Use `templates/readme/hero-template.svg` in `Swir/Swir` as the canonical starting point.

## 3. Project-local README asset layout

For maintained projects prefer this layout when applicable:

```text
assets/
├── app_icon.png / app_icon.svg / existing project icon
└── readme/
    ├── hero.svg
    ├── preview.png        # optional, real/current only
    └── screenshots/       # optional
```

Do not create empty placeholders just to satisfy the structure.

## 4. Shared divider

When a divider improves readability, use the shared profile-compatible divider:

```html
<img width="100%" src="https://raw.githubusercontent.com/Swir/Swir/main/assets/power-divider-v4.svg" alt="SWIR electric divider" />
```

Use it sparingly — normally 2–5 times in a long README, not between every section.

## 5. Badge system

Primary badges should visually match the profile:

```text
background: 02050A
logo/accent: 62E5FF
style: for-the-badge
```

Example:

```markdown
![Python](https://img.shields.io/badge/Python-3.11%2B-02050A?style=for-the-badge&logo=python&logoColor=62E5FF)
```

Secondary badges may use `flat-square` with `0088FF` accents.

Rules:

- normally 3–5 primary badges;
- only show facts that are maintained and true;
- avoid decorative or misleading `100%`, `BEST`, `ULTRA`, download-count or compatibility badges without reliable backing;
- prefer platform/runtime/build badges that help a visitor understand the project.

## 6. Optional quick navigation row

For larger READMEs, add a compact navigation row below the hero/badges:

```markdown
[**Features**](#-highlights) · [**Install**](#-quick-start) · [**Roadmap**](#-roadmap) · [**Releases**](#-releases)
```

Keep anchor names aligned with the actual headings.

## 7. Required information architecture

Adapt names naturally to the project, but a professional README should normally cover these areas in roughly this order:

1. **Hero / identity**
2. **Project status** — Development / Alpha / Beta / Stable + truthful milestone when relevant
3. **Overview / What is it?** — short practical explanation
4. **Highlights / Features** — compact table for feature-rich projects
5. **Preview / Screenshot / Demo** — only when real current media exists
6. **Quick Start / Installation / Download**
7. **Requirements / Compatibility**
8. **Usage / Controls / Workflow** — where useful
9. **Technology / Architecture** — concise and factual
10. **Roadmap / Progress** — authoritative link, truthful numbers only
11. **Releases / Downloads** — real releases only; otherwise clearly state that no public release exists yet
12. **Project structure** — only when useful
13. **Security / Responsible use / Limitations / Legal notes** — when relevant
14. **Search Keywords** — mandatory
15. **SWIR family footer**

Small utilities may combine sections. Large systems may add API, device matrix, troubleshooting, contributing, packaging or architecture sections.

## 8. Project status block

For active complex projects, make status easy to scan. A small table is preferred over vague prose:

```markdown
| Item | Status |
|---|---|
| Current stage | Alpha / Beta / Development |
| Platform | Windows / Linux / etc. |
| Latest public release | vX.Y.Z / Not published yet |
| Roadmap | Linked authoritative roadmap |
```

Never infer or invent a release or compatibility claim.

## 9. Feature presentation

For feature-rich projects prefer:

```markdown
| Feature | What it does |
|---|---|
| ⚡ Feature name | Clear user-facing explanation |
```

Describe **what the user gains**, not only internal implementation names.

## 10. Screenshots and media

- Prefer real current screenshots, GIFs or demo images from the repository.
- Do not show obsolete UI as the primary screenshot.
- Do not add empty screenshot placeholders.
- Keep image sizes reasonable.
- One excellent current desktop screenshot is often better than six redundant images.
- Never present a mockup as a real application screenshot unless clearly labeled as a concept.

## 11. Installation quality

The README must give the shortest reliable path from a fresh machine to a working project.

When applicable, distinguish clearly between:

- **Recommended:** GitHub Release / installer / portable build
- **From source:** clone + dependencies + run/build commands

Commands must match the actual repository. Never publish guessed filenames, dependencies or installation steps.

## 12. Architecture / technology

Only include architecture details that help users or contributors. Use concise diagrams/tables when they improve understanding.

Good examples:

- runtime + native core separation;
- client/server layers;
- device-profile model;
- rendering or packaging pipeline;
- supported provider/adapter model.

Avoid turning README into an internal design dump. Link to deeper architecture docs when they exist.

## 13. Roadmap and release truthfulness

- Link to the authoritative roadmap when one exists.
- Keep README status synchronized with verified project state.
- Never inflate completion because a skeleton, placeholder or CI job exists.
- Never describe a release as available until it actually exists.
- Preserve project-specific roadmap standards and release gates.

## 14. Search Keywords — mandatory

Every maintained project README must contain a visible section near the bottom:

```markdown
## 🔎 Search Keywords

`keyword one` • `keyword two` • `keyword three` • `keyword four`
```

Rules:

- normally **8–20** highly relevant phrases;
- include category, platform, main technology and primary use cases;
- include common search variants only when genuinely relevant;
- prefer useful multi-word phrases such as `python windows gui`, `disk image tool`, `unreal engine tractor game`;
- no keyword stuffing;
- no unrelated trending terms;
- do not use competitor/trademark names merely to attract search traffic;
- update keywords when the real scope changes.

Human readability comes first. Keywords are a discoverability aid, not a spam block.

## 15. SWIR family footer — required

Use a restrained footer, for example:

```html
<div align="center">

### `BUILD • TEST • RELEASE • EVOLVE`

⭐ **If this project is useful, consider leaving a star.**

[**← SWIR profile**](https://github.com/Swir) · [**All projects →**](https://github.com/Swir?tab=repositories)

</div>
```

The slogan may be customized to the project, but profile/repository navigation should remain consistent.

## 16. README skeleton

Use `templates/readme/README-SKELETON.md` in `Swir/Swir` as the preferred starting structure for new or heavily redesigned READMEs.

Do not paste it blindly. Remove sections that do not apply and replace every placeholder with verified project-specific information.

## 17. Quality gate

A SWIR README must be:

- accurate before impressive;
- visually consistent with the profile but recognizable as its own project;
- concise enough to scan, detailed enough to install and understand;
- free of dead links, stale versions and fake capability statements;
- updated when real user-visible behavior, installation, compatibility, releases or roadmap state changes;
- readable in GitHub dark and light themes where practical;
- backed by local project assets where visuals are used.

### README PRO v2 completion checklist

- [ ] `assets/readme/hero.svg` exists for major maintained projects
- [ ] project icon/branding is unique to that repository
- [ ] top badges are truthful and profile-compatible
- [ ] project status is clear
- [ ] Features/Highlights explain user value
- [ ] installation/download path is current
- [ ] compatibility is explicit
- [ ] real preview media is used only when available
- [ ] roadmap/release links are current
- [ ] `## 🔎 Search Keywords` contains 8–20 relevant phrases
- [ ] SWIR footer is present
- [ ] no fake metrics/features/releases/platforms

## 18. Automation rule — highest priority documentation standard

Any automated task that actively develops a `Swir/*` repository should:

1. read this standard before materially changing `README.md`;
2. use marker `<!-- SWIR-README-STANDARD:v2 -->` when it intentionally tracks this standard;
3. create or maintain `assets/readme/hero.svg` for major maintained projects when safe and appropriate;
4. use the v2 hero template as a starting point, then customize project iconography, name, tagline and category line;
5. bring an outdated README toward this standard when doing so is safe and does not displace release-blocking work;
6. treat a missing **Search Keywords** section as README debt and add it with project-specific terms;
7. preserve project-specific legal, safety, compatibility, roadmap and release information;
8. never blindly copy another repository's feature list, commands, badges, screenshots or claims;
9. keep README synchronized with verified project state after meaningful milestones;
10. never replace a unique, already-superior project hero with a generic banner merely for conformity.

This v2 document is the canonical source of truth for the SWIR repository presentation system.
