#!/usr/bin/env python3
"""Generate/check SWIR README migration progress SVGs from README-MIGRATION-STATUS.md."""
from __future__ import annotations

import argparse
import math
import re
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "README-MIGRATION-STATUS.md"
OUT = ROOT / "assets" / "readme" / "migration"
METRICS_RE = re.compile(
    r"<!-- MIGRATION-METRICS owner=(\d+) verified=(\d+) queued=(\d+) blocked=(\d+) delegated=(\d+) "
    r"excluded=(\d+) priority_verified=(\d+) priority_total=(\d+) eligibility=(INCOMPLETE|COMPLETE) -->"
)

TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="180" viewBox="0 0 1200 180" role="img" aria-labelledby="title desc">
<title id="title">SWIR README migration progress template</title>
<desc id="desc">Reusable local template. TEMPLATE ONLY — NOT LIVE MIGRATION DATA.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#02050A"/><stop offset="1" stop-color="#07111C"/></linearGradient><linearGradient id="fill" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#0088FF"/><stop offset="1" stop-color="#62E5FF"/></linearGradient></defs>
<rect x="1" y="1" width="1198" height="178" rx="24" fill="url(#bg)" stroke="#62E5FF" stroke-opacity=".22"/>
<text x="50" y="46" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="18" font-weight="700">SWIR MIGRATION PROGRESS · TEMPLATE ONLY</text>
<text x="50" y="82" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="30" font-weight="800">SCOPE NAME</text>
<text x="50" y="108" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="15">Replace values only from the canonical migration ledger.</text>
<text x="1090" y="82" text-anchor="end" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="34" font-weight="800">N/A</text>
<rect x="50" y="126" width="1100" height="24" rx="12" fill="#08131F" stroke="#62E5FF" stroke-opacity=".14"/>
<text x="50" y="169" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">Do not embed this template as live progress.</text>
</svg>
'''


def parse_metrics() -> dict[str, int | str]:
    text = LEDGER.read_text(encoding="utf-8")
    match = METRICS_RE.search(text)
    if not match:
        raise SystemExit("MIGRATION-METRICS marker missing or malformed")
    owner, verified, queued, blocked, delegated, excluded, p_verified, p_total, eligibility = match.groups()
    values: dict[str, int | str] = {
        "owner": int(owner),
        "verified": int(verified),
        "queued": int(queued),
        "blocked": int(blocked),
        "delegated": int(delegated),
        "excluded": int(excluded),
        "priority_verified": int(p_verified),
        "priority_total": int(p_total),
        "eligibility": eligibility,
    }
    counted = (
        int(values["verified"])
        + int(values["queued"])
        + int(values["blocked"])
        + int(values["delegated"])
        + int(values["excluded"])
    )
    if counted != int(values["owner"]):
        raise SystemExit("migration state counts do not add up to owner inventory")
    if int(values["priority_total"]) <= 0 or int(values["priority_verified"]) > int(values["priority_total"]):
        raise SystemExit("invalid priority subset counts")
    if values["eligibility"] == "COMPLETE" and int(values["queued"]) != 0:
        raise SystemExit("eligibility cannot be COMPLETE while queued repositories remain")
    return values


def render_card(m: dict[str, int | str]) -> str:
    complete = m["eligibility"] == "COMPLETE"
    verified = int(m["verified"])
    queued = int(m["queued"])
    blocked = int(m["blocked"])
    measurable = verified + blocked
    overall = f"{100.0 * verified / measurable:.1f}%" if complete and measurable else "N/A"
    status = "ELIGIBILITY COMPLETE" if complete else "ELIGIBILITY AUDIT"
    scope_line = (
        "Eligible migration scope · qualification complete"
        if complete
        else "Overall eligible scope · qualification audit is still in progress"
    )
    footer = (
        f"Eligible migration completion: {verified} verified · {blocked} blocked"
        if complete
        else "Overall percentage stays N/A until every owner repository has a final eligibility state."
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="200" viewBox="0 0 1200 200" role="img" aria-labelledby="title desc">
<title id="title">SWIR README PRO migration progress</title>
<desc id="desc">Overall migration percentage is {overall}. {m["owner"]} owner repositories discovered, {verified} verified migrations, {queued} queued for qualification, {blocked} blocked, {m["delegated"]} delegated, and {m["excluded"]} structural exclusions.</desc>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#02050A"/><stop offset="1" stop-color="#07111C"/></linearGradient>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#0088FF"/><stop offset="1" stop-color="#62E5FF"/></linearGradient>
  <pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse"><path d="M26 0H0V26" fill="none" stroke="#62E5FF" stroke-opacity=".05"/></pattern>
</defs>
<rect x="1" y="1" width="1198" height="198" rx="24" fill="url(#bg)" stroke="#62E5FF" stroke-opacity=".24"/>
<rect x="1" y="1" width="1198" height="198" rx="24" fill="url(#grid)"/>
<text x="50" y="42" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="17" font-weight="700" letter-spacing="4">SWIR PROGRESS</text>
<text x="50" y="77" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="30" font-weight="800">README PRO MIGRATION</text>
<text x="50" y="103" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="15">{scope_line}</text>
<text x="1090" y="77" text-anchor="end" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="34" font-weight="800">{overall}</text>
<text x="1090" y="103" text-anchor="end" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="700">{status}</text>
<rect x="50" y="122" width="1100" height="22" rx="11" fill="#08131F" stroke="#62E5FF" stroke-opacity=".16"/>
<path d="M70 133H1130" stroke="url(#accent)" stroke-width="2" stroke-dasharray="8 12" opacity=".35"/>
<text x="50" y="169" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">Owner inventory: {m["owner"]} · verified: {verified} · queued: {queued} · blocked: {blocked}</text>
<text x="1150" y="169" text-anchor="end" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">delegated: {m["delegated"]} · structural exclusions: {m["excluded"]}</text>
<text x="50" y="188" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="12">{footer}</text>
</svg>
'''


def render_mini(m: dict[str, int | str]) -> str:
    done = int(m["priority_verified"])
    total = int(m["priority_total"])
    fraction = done / total
    percent = 100.0 * fraction
    width = 700.0 * fraction
    if not math.isfinite(width) or not 0 <= width <= 700:
        raise SystemExit("invalid priority fill width")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="72" viewBox="0 0 900 72" role="img" aria-labelledby="title desc">
<title id="title">SWIR README PRO initial priority subset progress</title>
<desc id="desc">Initial priority subset: {done} of {total} repositories verified, {percent:.1f} percent.</desc>
<defs><linearGradient id="fill" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#0088FF"/><stop offset="1" stop-color="#62E5FF"/></linearGradient></defs>
<rect x="1" y="1" width="898" height="70" rx="18" fill="#02050A" stroke="#62E5FF" stroke-opacity=".22"/>
<text x="24" y="27" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700" letter-spacing="2">INITIAL PRIORITY SUBSET</text>
<text x="24" y="52" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="20" font-weight="800">{percent:.1f}%</text>
<rect x="170" y="24" width="700" height="20" rx="10" fill="#08131F"/>
<rect x="170" y="24" width="{width:.10f}" height="20" rx="10" fill="url(#fill)"/>
<text x="870" y="58" text-anchor="end" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">{done} / {total} verified · not overall migration progress</text>
</svg>
'''


def validate_svg(text: str) -> None:
    root = ET.fromstring(text)
    if root.tag.split("}")[-1] != "svg":
        raise SystemExit("root element is not svg")
    for value in root.attrib["viewBox"].split():
        if not math.isfinite(float(value)):
            raise SystemExit("non-finite viewBox")
    for elem in root.iter():
        for key in ("x", "y", "width", "height", "rx", "ry"):
            if key in elem.attrib and not math.isfinite(float(elem.attrib[key])):
                raise SystemExit(f"non-finite {key}")


def expected() -> dict[str, str]:
    metrics = parse_metrics()
    return {
        "progress-card.svg": render_card(metrics),
        "progress-mini.svg": render_mini(metrics),
        "progress-template.svg": TEMPLATE,
    }


def render() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, text in expected().items():
        validate_svg(text)
        (OUT / name).write_text(text, encoding="utf-8")


def check() -> None:
    for name, text in expected().items():
        validate_svg(text)
        path = OUT / name
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            raise SystemExit(f"missing or stale {path.relative_to(ROOT)}")
    ledger = LEDGER.read_text(encoding="utf-8")
    for name in ("progress-card.svg", "progress-mini.svg"):
        if f"assets/readme/migration/{name}" not in ledger:
            raise SystemExit(f"ledger does not embed {name}")
    print("SWIR README migration progress assets are consistent with the ledger metrics marker.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    check() if args.check else render()
