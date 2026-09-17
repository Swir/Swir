#!/usr/bin/env python3
"""Original, script-free pixel rover animation for a GitHub profile README.

Only the illuminated subsurface columns and counters encode GitHub contributions.
The landscape and vehicle are decorative, original vector art, not game assets.
Animation runs in the viewer; Actions only refreshes the data snapshot.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import html
import json
import math
import os
from pathlib import Path
import random
import sys
import urllib.error
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PATROL = ROOT / "assets/github-moon-patrol.svg"
DASHBOARD = ROOT / "assets/github-activity-live.svg"
STATE = ROOT / "assets/moon-patrol-state.json"
NS = "{http://www.w3.org/2000/svg}"


def rect(x, y, w, h, color, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" {extra}/>'


def text(x, y, value, size=12, color="#91B6CC", extra=""):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
            f'font-family="ui-monospace,Consolas,monospace" {extra}>{html.escape(str(value))}</text>')


def metrics_for(calendar: dict) -> tuple[list[dict], list[int], dict]:
    """Validate the API snapshot and measure a streak ending today or yesterday."""
    weeks = calendar["weeks"]
    total = calendar["totalContributions"]
    if type(total) is not int or total < 0 or not isinstance(weeks, list) or not weeks:
        raise ValueError("Missing or invalid GitHub contribution calendar")
    days = sorted([day for week in weeks for day in week["contributionDays"]], key=lambda d: d["date"])
    if not days or len(days) > 371:
        raise ValueError("Empty or oversized contribution calendar")
    dates = [dt.date.fromisoformat(d["date"]) for d in days]
    counts = [d["contributionCount"] for d in days]
    if len(set(dates)) != len(dates) or any(type(n) is not int or n < 0 for n in counts):
        raise ValueError("Duplicate dates or invalid contribution counts")
    if sum(counts) != total:
        raise ValueError("GitHub calendar total does not match its daily counts")
    streak, cursor = 0, dates[-1]
    by_date = dict(zip(dates, counts))
    if not by_date[cursor]:
        cursor -= dt.timedelta(days=1)
    while by_date.get(cursor, 0) > 0:
        streak += 1
        cursor -= dt.timedelta(days=1)
    weekly = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in weeks]
    return days, weekly, {"total": total, "active_days": sum(n > 0 for n in counts),
                          "current_streak": streak, "best_day": max(counts)}


def ridge(seed: int, baseline: int, height: int, fill: str, edge: str) -> str:
    """A seamless 928px pixel ridge; no external bitmaps or fonts."""
    rng = random.Random(seed)
    anchors = [rng.randint(12, height) for _ in range(8)]
    tops, parts = [], []
    for i in range(116):
        p = i * 8 / 116
        k, f = int(p), p % 1
        y = baseline - round((anchors[k] * (1 - f) + anchors[(k + 1) % 8] * f) / 4) * 4
        tops.append(y)
        parts.append(rect(i * 8, y, 8, 258 - y, fill))
        parts.append(rect(i * 8, y, 8, 4, edge))
        if i % 3 == 0:
            parts.append(rect(i * 8, y + 8, 4, 8, edge))
    return "".join(parts)


def planet() -> str:
    rng, parts = random.Random(19), []
    colors = ["#071B30", "#0C2F50", "#14517C", "#237DB0", "#4BBFEB", "#B0EDFF"]
    for y in range(-44, 45, 4):
        for x in range(-44, 45, 4):
            r = (x / 44) ** 2 + (y / 44) ** 2
            if r > 1:
                continue
            z = math.sqrt(1 - r)
            light = max(0, .75 * x / 44 - .3 * y / 44 + .4 * z)
            crater = any((x - cx) ** 2 + (y - cy) ** 2 < radius ** 2
                         for cx, cy, radius in [(12, -16, 10), (24, 12, 7), (-8, 24, 9)])
            level = max(0, min(5, int(light * 6) - int(crater) + rng.choice([0, 0, 0, 1])))
            parts.append(rect(772 + x, 132 + y, 4, 4, colors[level]))
    return "".join(parts)


def rover() -> str:
    body = (rect(0, -36, 104, 22, "#071524") + rect(4, -32, 92, 14, "#168FFF")
            + rect(8, -38, 48, 8, "#62E5FF") + rect(4, -22, 96, 6, "#B6EFFF")
            + '<path d="M58 -32V-58H80V-54H84V-50H88V-46H92V-32Z" fill="#91DFFF"/>'
            + '<path d="M64 -52H76V-48H80V-44H84V-36H64Z" fill="#0A3454"/>'
            + rect(66, -50, 8, 12, "#27C9FF") + rect(88, -32, 12, 8, "#E8F7FF")
            + rect(98, -27, 10, 6, "#62E5FF") + rect(26, -51, 22, 10, "#175181")
            + rect(22, -45, 30, 7, "#E1F6FF") + rect(32, -67, 3, 18, "#91DFFF")
            + rect(30, -70, 7, 4, "#62E5FF") + rect(12, -62, 3, 24, "#A8D6EC")
            + rect(15, -63, 20, 12, "#0D3552") + rect(18, -60, 12, 3, "#62E5FF")
            + rect(18, -56, 8, 2, "#62E5FF") + rect(14, -28, 8, 3, "#0B314D")
            + rect(28, -28, 8, 3, "#0B314D") + rect(42, -28, 8, 3, "#0B314D"))
    wheels = []
    for x in (18, 52, 86):
        wheels.append(f'<g transform="translate({x} -10)"><path d="M-7 -12H7L12 -7V7L7 12H-7L-12 7V-7Z" '
                      'fill="#03101C" stroke="#296591" stroke-width="3"/>'
                      '<g class="wheel"><path d="M-3 -9H3V-3H9V3H3V9H-3V3H-9V-3H-3Z" fill="#168FFF"/>'
                      '<rect x="-3" y="-3" width="6" height="6" fill="#C7F5FF"/></g></g>')
    return '<g class="suspension">' + body + '</g>' + "".join(wheels)


def build_patrol(calendar: dict, username: str, generated_at: str) -> str:
    days, weekly, metrics = metrics_for(calendar)
    rng = random.Random(73)
    stars = "".join(rect(rng.randrange(8, 916, 4), rng.randrange(76, 200, 4),
                         2, 2, rng.choice(["#194C74", "#3D8FB8", "#91DFFF"])) for _ in range(76))
    stars += '<path d="M452 108h12m-6 -6v12M602 170h8m-4 -4v8M872 90h10m-5 -5v10" stroke="#62E5FF"/>'
    far = ridge(4, 246, 72, "#0A1F35", "#143B60")
    near = ridge(12, 265, 48, "#10314E", "#1C5079")
    surface = rect(0, 258, 928, 42, "#081E31") + rect(0, 258, 928, 3, "#468FB4")
    for _ in range(92):
        surface += rect(rng.randrange(0, 928, 4), rng.randrange(266, 297, 4),
                        rng.choice([4, 8, 12]), 2, rng.choice(["#123B58", "#1C5070", "#246183"]))
    # The crater passes the rover at 58.4% of the shared 12-second loop.
    surface += '<path d="M740 258H748V262H756V270H796V262H804V258" fill="#020A14" stroke="#438DB7" stroke-width="3"/>'
    surface += '<path d="M734 262H744V266H752M800 266H810V262H818" fill="none" stroke="#1B4C71" stroke-width="3"/>'
    # Bar cells represent actual weekly totals. Square-root height keeps small weeks visible.
    span, maximum = 928 / len(weekly), max(weekly) or 1
    for i, value in enumerate(weekly):
        levels = math.ceil(math.sqrt(value / maximum) * 6) if value else 0
        x = round(i * span)
        surface += f'<g><title>Week {i + 1}: {value} contributions</title>'
        for j in range(max(1, levels)):
            surface += rect(x + 2, 294 - j * 4, max(3, round(span) - 5), 3,
                            ("#175C87", "#1D78AC", "#168FFF", "#27B5ED", "#27C9FF", "#62E5FF")[j]
                            if value else "#102E45")
        surface += '</g>'
    dust = "".join(f'<g transform="translate({174 - i * 8} 252)"><g class="dust" '
                   f'style="animation-delay:-{i * .2}s">{rect(0, 0, 5, 3, "#5295BA")}</g></g>' for i in range(4))
    counters = ""
    for x, label, value in [(30, "CONTRIBUTIONS / 365D", f'{metrics["total"]:,}'),
                             (286, "ACTIVE DAYS", metrics["active_days"]),
                             (498, "CURRENT STREAK", f'{metrics["current_streak"]} DAYS'),
                             (752, "BEST DAY", metrics["best_day"])]:
        counters += text(x, 320, label, 10) + text(x, 343, value, 20, "#62E5FF", 'font-weight="700"')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="368" viewBox="0 0 960 368" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(username)} Moon Patrol - animated contribution rover</title>
<desc id="desc">Original pixel-art lunar rover with continuously scrolling mountains, turning wheels, dust and a crater jump. Illuminated ground columns show {len(weekly)} weekly contribution totals from {days[0]['date']} to {days[-1]['date']}. Data snapshot: {html.escape(generated_at)}. Decorative motion is not live gameplay. Reduced-motion preferences stop animation.</desc>
<defs><clipPath id="screen"><rect x="16" y="56" width="928" height="244"/></clipPath>
<linearGradient id="sky" x2="0" y2="1"><stop stop-color="#030A14"/><stop offset="1" stop-color="#071A2D"/></linearGradient>
<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><path d="M0 0H4" stroke="#02060B" stroke-opacity=".18"/></pattern>
<g id="far-ridge">{far}</g><g id="near-ridge">{near}</g><g id="ground-strip">{surface}</g></defs>
<style>
@keyframes scroll{{to{{transform:translateX(-928px)}}}}
@keyframes jump{{0%,46%,71%,100%{{transform:translateY(0)}}52%{{transform:translateY(-40px)}}58.4%{{transform:translateY(-68px)}}64%{{transform:translateY(-42px)}}}}
@keyframes suspension{{50%{{transform:translateY(2px)}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes dust{{0%{{opacity:0;transform:translate(0,0)}}18%{{opacity:.8}}100%{{opacity:0;transform:translate(-65px,-16px)}}}}
@keyframes scout{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-156px,12px)}}}}
@keyframes glint{{50%{{opacity:.5}}}}
.far{{animation:scroll 96s linear infinite}}.near{{animation:scroll 48s linear infinite}}
.ground{{animation:scroll 12s linear infinite}}.rover{{animation:jump 12s ease-in-out infinite}}
.suspension{{animation:suspension .35s steps(2) infinite}}.wheel{{animation:spin .8s steps(8) infinite}}
.dust{{animation:dust 1s linear infinite}}.scout{{animation:scout 18s ease-in-out infinite}}
.stars{{animation:glint 6s ease-in-out infinite}}
@media(prefers-reduced-motion:reduce){{.far,.near,.ground,.rover,.suspension,.wheel,.dust,.scout,.stars{{animation:none!important}}.dust{{display:none}}}}
</style>
<rect x="1" y="1" width="958" height="366" rx="14" fill="#030A13" stroke="#174D73" stroke-width="2"/>
<path d="M16 30V16H70M890 16H944V30M16 338V352H70M890 352H944V338" fill="none" stroke="#168FFF" stroke-width="2"/>
{text(30, 38, 'SWIR // MOON PATROL', 22, '#C9F4FF', 'font-weight="700" letter-spacing="2"')}
{text(930, 36, 'AUTO PATROL  /  SECTOR GITHUB', 11, '#62E5FF', 'text-anchor="end"')}
<g clip-path="url(#screen)"><rect x="16" y="56" width="928" height="244" fill="url(#sky)"/>
<g transform="translate(16 0)"><g class="stars">{stars}</g></g>{planet()}
<g transform="translate(646 118)"><g class="scout" shape-rendering="crispEdges">
<path d="M-12 0H12V4H20V8H12V12H-12V8H-20V4H-12Z" fill="#176193"/>
<path d="M-8 -4H8V0H12V4H-12V0H-8Z" fill="#68D8F4"/><path d="M-16 6H16" stroke="#B6F3FF" stroke-width="2"/>
</g></g>
<g transform="translate(16 0)" shape-rendering="crispEdges">
<g class="far"><use href="#far-ridge"/><use href="#far-ridge" x="928"/></g>
<g class="near"><use href="#near-ridge"/><use href="#near-ridge" x="928"/></g>
<g class="ground"><use href="#ground-strip"/><use href="#ground-strip" x="928"/></g></g>
<g transform="translate(16 0)" shape-rendering="crispEdges">{dust}</g>
<g transform="translate(198 255)"><g class="rover" shape-rendering="crispEdges">{rover()}</g></g>
{text(32, 80, 'EXPLORING COMMIT TERRITORY', 10, '#6085A2', 'letter-spacing="1"')}
<rect x="16" y="56" width="928" height="244" fill="url(#scan)" pointer-events="none"/>
</g><path d="M16 300H944" stroke="#174D73"/>{counters}
{text(30, 361, 'DATA '+generated_at+'  |  BLUE COLUMNS = WEEKLY CONTRIBUTIONS', 9, '#7198B3')}
{text(930, 361, 'ORIGINAL PIXEL ART / by Swir', 9, '#62E5FF', 'text-anchor="end"')}
</svg>'''


def validate_svg(svg: str) -> None:
    root = ET.fromstring(svg)
    if root.tag != NS + "svg":
        raise ValueError("Not an SVG document")
    for element in root.iter():
        if element.tag in (NS + "script", NS + "foreignObject", NS + "image"):
            raise ValueError("Executable or external content is not allowed")
        for attr, value in element.attrib.items():
            if attr.lower().startswith("on") or (attr.endswith("href") and not value.startswith("#")):
                raise ValueError("Unsafe SVG attribute")


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(content, encoding="utf-8")
    temp.replace(path)


def main() -> int:
    # Reuse the existing authenticated calendar reader and keep its dashboard.
    from generate_profile_activity import fetch_calendar, calc_metrics, build_svg
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    username = os.environ.get("PROFILE_USER", "Swir").strip() or "Swir"
    try:
        if not token:
            raise RuntimeError("GITHUB_TOKEN is missing")
        calendar = fetch_calendar(token, username)
        days, weekly, metrics = metrics_for(calendar)
        sources = Path(__file__).read_bytes() + Path(__file__).with_name("generate_profile_activity.py").read_bytes()
        fingerprint = hashlib.sha256(sources + username.encode() + json.dumps(calendar, sort_keys=True).encode()).hexdigest()
        previous = json.loads(STATE.read_text()) if STATE.exists() else {}
        if previous.get("fingerprint") == fingerprint and PATROL.exists() and DASHBOARD.exists():
            validate_svg(PATROL.read_text())
            validate_svg(DASHBOARD.read_text())
            print("GitHub data and renderer unchanged; keeping the existing snapshot without a commit.")
            return 0
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        patrol_svg = build_patrol(calendar, username, stamp)
        _days, dashboard_weeks, dashboard_metrics = calc_metrics(calendar)
        dashboard_svg = build_svg(username, dashboard_weeks, dashboard_metrics)
        validate_svg(patrol_svg)
        validate_svg(dashboard_svg)
        state = {"schema": 1, "user": username, "source": "GitHub GraphQL contributionCalendar",
                 "fingerprint": fingerprint, "generated_at": stamp, "period_start": days[0]["date"],
                 "period_end": days[-1]["date"], "metrics": metrics, "weekly_totals": weekly}
        write_atomic(PATROL, patrol_svg)
        write_atomic(DASHBOARD, dashboard_svg)
        write_atomic(STATE, json.dumps(state, indent=2) + "\n")
        print(f"Generated Moon Patrol and activity dashboard for {username}: {metrics}")
        return 0
    except (OSError, urllib.error.URLError, RuntimeError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
        print(f"::warning::Profile refresh failed ({type(exc).__name__}); previous assets were not replaced.", file=sys.stderr)
        # First deployment must fail rather than pretend a missing asset exists.
        return 0 if PATROL.exists() and DASHBOARD.exists() else 1


if __name__ == "__main__":
    raise SystemExit(main())
