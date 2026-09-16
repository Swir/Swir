#!/usr/bin/env python3
"""Generate a self-hosted SVG dashboard for the SWIR GitHub profile.

The dashboard reads the contribution calendar directly from GitHub GraphQL using
the repository GITHUB_TOKEN. No third-party card/graph service is required at
README render time, so rate limits on external profile-card services cannot
break the profile.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request


GRAPHQL_URL = "https://api.github.com/graphql"
OUT_PATH = Path("assets/github-activity-live.svg")


def fetch_calendar(token: str, username: str) -> dict:
    now = dt.datetime.now(dt.timezone.utc)
    start = now - dt.timedelta(days=364)
    query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                date
                contributionCount
                weekday
              }
            }
          }
        }
      }
    }
    """
    payload = {
        "query": query,
        "variables": {
            "login": username,
            "from": start.isoformat().replace("+00:00", "Z"),
            "to": now.isoformat().replace("+00:00", "Z"),
        },
    }
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "swir-profile-live-dashboard",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))

    if data.get("errors"):
        raise RuntimeError(json.dumps(data["errors"], ensure_ascii=False))
    user = data.get("data", {}).get("user")
    if not user:
        raise RuntimeError(f"GitHub user {username!r} was not returned by GraphQL")
    return user["contributionsCollection"]["contributionCalendar"]


def calc_metrics(calendar: dict) -> tuple[list[dict], list[int], dict]:
    weeks = calendar.get("weeks", [])
    days = [day for week in weeks for day in week.get("contributionDays", [])]
    days.sort(key=lambda item: item["date"])

    active_days = sum(1 for day in days if day.get("contributionCount", 0) > 0)
    total = int(calendar.get("totalContributions", 0))
    best = max(days, key=lambda item: item.get("contributionCount", 0), default=None)

    latest_active_index = None
    for index in range(len(days) - 1, -1, -1):
        if days[index].get("contributionCount", 0) > 0:
            latest_active_index = index
            break

    streak = 0
    if latest_active_index is not None:
        index = latest_active_index
        previous_date = None
        while index >= 0 and days[index].get("contributionCount", 0) > 0:
            current_date = dt.date.fromisoformat(days[index]["date"])
            if previous_date is not None and previous_date - current_date != dt.timedelta(days=1):
                break
            streak += 1
            previous_date = current_date
            index -= 1

    weekly_totals = [
        sum(int(day.get("contributionCount", 0)) for day in week.get("contributionDays", []))
        for week in weeks
    ]

    metrics = {
        "total": total,
        "active_days": active_days,
        "recent_streak": streak,
        "best_count": int(best.get("contributionCount", 0)) if best else 0,
        "best_date": best.get("date", "—") if best else "—",
    }
    return days, weekly_totals, metrics


def compact(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        formatted = f"{value / 1_000:.1f}K"
        return formatted.replace(".0K", "K")
    return str(value)


def build_svg(username: str, weekly_totals: list[int], metrics: dict) -> str:
    width, height = 960, 330
    graph_x, graph_y, graph_w, graph_h = 44, 165, 872, 105
    max_week = max(weekly_totals or [1]) or 1

    if len(weekly_totals) <= 1:
        xs = [graph_x]
    else:
        xs = [
            graph_x + (graph_w * index / (len(weekly_totals) - 1))
            for index in range(len(weekly_totals))
        ]

    points = []
    for x, value in zip(xs, weekly_totals):
        y = graph_y + graph_h - (graph_h * value / max_week)
        points.append((x, y))

    if points:
        polyline = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        area = f"{graph_x},{graph_y + graph_h} " + polyline + f" {graph_x + graph_w},{graph_y + graph_h}"
    else:
        polyline = ""
        area = ""

    sync_time = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    safe_user = html.escape(username)
    best_date = html.escape(str(metrics["best_date"]))

    metric_items = [
        ("12M CONTRIBUTIONS", compact(metrics["total"])),
        ("ACTIVE DAYS", compact(metrics["active_days"])),
        ("RECENT STREAK", f"{metrics['recent_streak']}d"),
        ("BEST DAY", compact(metrics["best_count"])),
    ]

    cards = []
    card_w = 203
    gap = 20
    start_x = 44
    for index, (label, value) in enumerate(metric_items):
        x = start_x + index * (card_w + gap)
        cards.append(
            f'<rect x="{x}" y="74" width="{card_w}" height="67" rx="11" fill="#07111C" stroke="#173044"/>'
            f'<text x="{x + 16}" y="98" class="label">{html.escape(label)}</text>'
            f'<text x="{x + 16}" y="126" class="value">{html.escape(value)}</text>'
        )

    grids = []
    for step in range(4):
        y = graph_y + graph_h * step / 3
        grids.append(
            f'<line x1="{graph_x}" y1="{y:.1f}" x2="{graph_x + graph_w}" y2="{y:.1f}" class="grid"/>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">SWIR GitHub activity live dashboard</title>
  <desc id="desc">Self-hosted GitHub contribution metrics and weekly activity signal for {safe_user}.</desc>
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#02050A"/>
      <stop offset="1" stop-color="#06111B"/>
    </linearGradient>
    <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#27C9FF" stop-opacity="0.42"/>
      <stop offset="1" stop-color="#168FFF" stop-opacity="0.02"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .title {{ fill:#E8F7FF; font:700 22px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; letter-spacing:1.4px; }}
    .sub {{ fill:#6E91A8; font:500 11px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; letter-spacing:1px; }}
    .label {{ fill:#6E91A8; font:600 10px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; letter-spacing:.7px; }}
    .value {{ fill:#62E5FF; font:700 22px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; }}
    .grid {{ stroke:#102536; stroke-width:1; }}
    .footer {{ fill:#58758A; font:500 10px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; }}
  </style>
  <rect x="1" y="1" width="958" height="328" rx="18" fill="url(#panel)" stroke="#173044" stroke-width="2"/>
  <circle cx="45" cy="38" r="5" fill="#62E5FF" filter="url(#glow)"/>
  <text x="61" y="46" class="title">SWIR // GITHUB ACTIVITY LIVE</text>
  <text x="916" y="45" text-anchor="end" class="sub">SELF-HOSTED · NO CARD RATE LIMITS</text>
  {''.join(cards)}
  <text x="44" y="158" class="sub">52-WEEK CONTRIBUTION SIGNAL</text>
  {''.join(grids)}
  <polygon points="{area}" fill="url(#area)"/>
  <polyline points="{polyline}" fill="none" stroke="#27C9FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)"/>
  <line x1="44" y1="288" x2="916" y2="288" stroke="#173044"/>
  <text x="44" y="310" class="footer">BEST DAY: {best_date} · {metrics['best_count']} contributions</text>
  <text x="916" y="310" text-anchor="end" class="footer">SYNC {sync_time}</text>
</svg>'''


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    username = os.environ.get("PROFILE_USER", "Swir").strip() or "Swir"
    if not token:
        print("GITHUB_TOKEN is missing; keeping the last generated dashboard.")
        return 0

    try:
        calendar = fetch_calendar(token, username)
        _days, weekly_totals, metrics = calc_metrics(calendar)
        svg = build_svg(username, weekly_totals, metrics)
        OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUT_PATH.write_text(svg, encoding="utf-8")
        print(f"Generated {OUT_PATH} for {username}: {metrics}")
        return 0
    except (urllib.error.URLError, urllib.error.HTTPError, RuntimeError, ValueError, KeyError) as exc:
        # Preserve the last known-good SVG instead of replacing it with an error card.
        print(f"Dashboard refresh skipped: {exc}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
