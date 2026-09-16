# Profile Activity Automation

The SWIR profile keeps its activity presentation resilient by generating key visual assets inside the profile repository instead of depending entirely on third-party card services.

## Live assets

- `assets/github-activity-live.svg` is generated from GitHub contribution data.
- `assets/github-contribution-grid-snake.svg` and the dark variant are refreshed automatically.
- The profile README references repository-hosted SVG assets so temporary external card rate limits cannot replace the profile with error cards.

## Maintenance

The activity workflow refreshes generated assets on a schedule and only commits when generated output changes. This keeps the profile current while avoiding unnecessary commits.

This document records the collaboration and maintenance design behind the profile activity section.
