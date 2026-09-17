# SWIR Moon Patrol

An original animated pixel-art contribution panel that replaces the profile's contribution snake. The existing activity dashboard and the rest of the profile remain in place.

## What actually moves

- Three independently scrolling layers: far mountains, near mountains and lunar ground.
- An original three-wheel rover with rotating wheel hubs, moving suspension, dust and a timed crater jump.
- A slowly moving scout craft and gently changing star brightness.

The delivered asset is `assets/github-moon-patrol.svg`, not the earlier concept illustration. It is a continuously animated SVG with internal CSS keyframes, embedded vector shapes and local SVG references only. There is no JavaScript, iframe, external font, raster background or third-party card service. It is a decorative animation, not a playable game or an emulation of the commercial arcade game. The rover and landscape are original artwork.

## Real data, separate from motion

`python3 scripts/generate_moon_patrol.py` reuses the existing GitHub GraphQL calendar reader. A single API snapshot generates both the existing dashboard and Moon Patrol.

Illuminated blue subsurface columns represent actual weekly contribution totals; their height uses square-root scaling for readability. The counters show contributions, active days, current streak and best day for the returned calendar period. The scenery and vehicle are decorative; they do not manufacture contributions. Current streak must end on the calendar's latest date or the preceding day, rather than on an arbitrarily old active day.

Animation runs continuously in the viewer. `.github/workflows/profile-activity.yml` requests data refresh every five minutes, but GitHub scheduling, contribution processing and image caching may delay visible updates. This is not second-by-second data streaming. The `DATA` timestamp identifies the displayed snapshot, not the time the viewer opened the page.

A source/data fingerprint avoids new commits when the dataset and renderer are unchanged. Validation/API failures retain previously published assets. A first run without an actual generated patrol fails instead of publishing invented numbers or a missing image.

## Validation and accessibility

Run the offline regression tests:

```sh
python3 -m unittest discover -s tests -p 'test_moon_patrol.py' -v
```

The tests cover counters, current-streak edge cases, empty/invalid calendars, XML escaping, internal references, deterministic output, animation declarations, size and unsafe-content rejection. Test fixtures are synthetic and are never published as profile statistics.

The SVG includes accessible title/description and a `prefers-reduced-motion` rule. A browser with reduced motion enabled may intentionally display a still frame. Actual image-element animation was separately checked in Chromium during implementation; unit tests alone do not prove rendering in every GitHub client.

Legacy snake SVG files remain in repository history/assets for compatibility, but the new workflow no longer generates them.

## References

- [GitHub Actions scheduling and possible delays](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [SVG as an image and its restrictions](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image)

## Search Keywords

SWIR Moon Patrol, animated GitHub profile, contribution animation, pixel art rover, lunar patrol, self-hosted SVG, GitHub Actions, blue neon README, Python SVG generator.
