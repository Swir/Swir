<!-- SWIR-README-STANDARD:v1 -->

# SWIR README PRO — Canonical Repository Standard

This file is the canonical README design and content standard for active `Swir/*` projects.

The goal is **one recognizable SWIR family** across repositories without making every README a copy. Each project keeps its own identity, icon, screenshots, wording, features and technology stack, while sharing the same professional visual language and information architecture.

## 1. Visual identity

Match the current SWIR GitHub profile style:

- dark base: `#02050A` / GitHub dark surfaces
- primary electric cyan: `#62E5FF`
- secondary blue: `#0088FF`
- clean cyber/electric presentation, not cluttered “hacker” decoration
- centered project hero/header
- consistent `for-the-badge` technology/platform badges near the top
- smaller `flat-square` author/stars/release/license badges where appropriate
- use the shared SWIR divider when a divider improves readability:

```html
<img width="100%" src="https://raw.githubusercontent.com/Swir/Swir/main/assets/power-divider-v4.svg" alt="SWIR electric divider" />
```

Do not overload a README with badges, animated widgets, emojis or repeated separators. Professional readability wins over decoration.

## 2. Project hero — required

Every main README should begin with a clean centered hero.

Preferred structure:

```html
<div align="center">

<!-- Use the repository's own icon/logo/banner when available. -->

# ⚡ PROJECT NAME

### One clear sentence explaining what the project is

**Short capability line • Key platform • Main use case**

<!-- 3–5 primary technology/platform badges -->
<!-- optional secondary row: Author / Stars / Latest Release / License -->

</div>
```

Rules:

- use the project's **own icon/logo** if the repository has one;
- do not reuse another project's logo;
- do not claim platforms, versions or features that are not actually supported;
- keep the tagline understandable to a new visitor in a few seconds;
- repository-facing README content should normally be in English for global discoverability unless the repository has a deliberate language-specific audience.

## 3. Required information architecture

Adapt section names naturally to the project, but a professional README should normally cover these areas in this order:

1. **Hero / identity**
2. **Project status** — Alpha/Beta/Stable/Development + truthful current milestone when relevant
3. **What is it? / Overview** — short, practical explanation
4. **Highlights / Features** — preferably a compact table for larger projects
5. **Screenshots / Demo / Preview** — only when real current media exists
6. **Quick Start / Installation**
7. **Requirements / Compatibility**
8. **Usage** — commands or workflow where useful
9. **Technology / Architecture** — concise, factual
10. **Roadmap / Progress** — link to the authoritative roadmap; never invent completion percentages
11. **Releases / Downloads** — link to real releases or clearly say when no public release exists yet
12. **Project structure** — only when it helps contributors/users
13. **Security / Responsible use / Limitations** — when relevant to the project
14. **Search Keywords** — mandatory
15. **Footer / SWIR profile links**

Small utilities may combine sections. Large systems can add architecture, device support, API, contributing or troubleshooting sections.

## 4. Badge style

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

Only show badges whose values are known and maintained. Avoid decorative or misleading “100%”, “best”, “ultra fast”, download-count or compatibility badges that are not backed by real data.

## 5. Feature presentation

For feature-rich projects prefer a compact table:

```markdown
| Feature | What it does |
|---|---|
| ⚡ Feature name | Clear user-facing explanation |
```

Describe **what the user gains**, not only internal implementation names.

## 6. Screenshots and media

- Prefer real current screenshots, GIFs or demo images from the repository.
- Do not show obsolete UI as the primary screenshot.
- Do not add empty screenshot placeholders.
- Keep image sizes reasonable and avoid a wall of media.
- For desktop applications, showing one strong current UI screenshot is usually better than many redundant images.

## 7. Installation quality

The README must give the shortest reliable path from a fresh machine to a working project.

When applicable, distinguish clearly between:

- **Recommended:** GitHub Release / installer / portable build
- **From source:** clone + dependencies + run/build commands

Commands must match the actual repository. Never publish guessed filenames, dependencies or installation steps.

## 8. Roadmap and release truthfulness

- Link to the authoritative roadmap when one exists.
- Keep README progress/status synchronized with the real project state.
- Never inflate completion because a skeleton, placeholder or CI job exists.
- Never describe a release as available until it actually exists.
- Preserve project-specific roadmap standards and release gates.

## 9. Search Keywords — mandatory

Every maintained project README must contain a visible section near the bottom:

```markdown
## 🔎 Search Keywords

`keyword one` • `keyword two` • `keyword three` • `keyword four`
```

Keyword rules:

- normally use **8–20** highly relevant phrases;
- include the project category, platform, main technology and primary use cases;
- include common search variants only when genuinely relevant;
- prefer useful multi-word phrases such as `python windows gui`, `disk image tool`, `unreal engine tractor game`;
- do **not** keyword-stuff, repeat near-identical phrases or add unrelated trending terms;
- do not use competitor/trademark names merely to attract search traffic;
- update keywords when the project's real scope changes.

The section is for discoverability, but the README should still read naturally to humans first.

## 10. Footer — required family signature

Use a restrained SWIR footer, for example:

```html
<div align="center">

### `BUILD • TEST • RELEASE • EVOLVE`

⭐ **If this project is useful, consider leaving a star.**

[**← SWIR profile**](https://github.com/Swir) · [**All projects →**](https://github.com/Swir?tab=repositories)

</div>
```

The short slogan may be customized to fit the project, but profile/repository navigation should remain clean and consistent.

## 11. Quality rules

A SWIR README must be:

- accurate before impressive;
- visually consistent with the profile but recognizable as its own project;
- concise enough to scan, detailed enough to install and understand;
- free of dead links, stale version claims and fake capability statements;
- updated when real user-visible behavior, installation, compatibility, releases or roadmap state changes;
- compatible with GitHub Markdown rendering in both dark and light themes where practical.

## 12. Automation rule

Any automated task that actively develops a `Swir/*` repository should:

1. read this standard before materially changing `README.md`;
2. bring an outdated README toward this standard when doing so is safe and does not displace higher-priority release-blocking work;
3. treat a missing **Search Keywords** section as README debt and add it with project-specific terms;
4. preserve project-specific legal, safety, compatibility, roadmap and release information;
5. never blindly copy another repository's feature list, commands, badges or claims;
6. keep the README synchronized with verified project state after meaningful milestones.

The reference aesthetic is the current SWIR GitHub profile plus the clean information hierarchy used by ARIA2 Ultimate PRO, with this document taking precedence as the newer standard.
