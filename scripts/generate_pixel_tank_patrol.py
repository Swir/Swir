#!/usr/bin/env python3
"""A continuously animated, data-driven contribution tank for GitHub README.

One target is one actual active calendar day. Every shell hits that day's cell,
which clears until the next loop. Scores sum real contribution counts, not shots.
Pure SVG/CSS: no scripts, images, external fonts, APIs or hover needed by viewers.
"""
from __future__ import annotations

from dataclasses import dataclass
import datetime as dt
import hashlib
import html
import json
import math
import os
from pathlib import Path
import random
import re
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG_PATH = Path('assets/github-pixel-tank-patrol.svg')
STATE_PATH = Path('assets/pixel-tank-state.json')
DASHBOARD_PATH = Path('assets/github-activity-live.svg')
NS = '{http://www.w3.org/2000/svg}'
WIDTH, HEIGHT = 1120, 462
GX, GY, DX, DY, CELL = 62, 155, 14, 17, 11
TANK_Y, SLOT, LEAD, FLIGHT = 323, 1.1, .4, .30
COLORS = ('#1C527E', '#1A82CE', '#168FFF', '#36C7F4', '#89EEFF')


def f(n: float) -> str:
    return f'{n:.4f}'.rstrip('0').rstrip('.') or '0'


def rect(x, y, w, h, fill, extra=''):
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}" {extra}/>'


def text(x, y, value, size=12, fill='#95B6CE', extra=''):
    return (f'<text x="{f(x)}" y="{f(y)}" font-size="{size}" fill="{fill}" '
            f'{extra}>{html.escape(str(value))}</text>')


def keyframes(name: str, duration: float, frames: list[tuple[float, str]]) -> str:
    return '@keyframes '+name+'{'+''.join(f'{f(100*t/duration)}%{{{props}}}' for t, props in frames)+'}'


def window(name: str, duration: float, start: float, end: float) -> str:
    """A discrete visibility window, hidden before/after and repeated each loop."""
    eps = min(.0001, (end-start)/10)
    return keyframes(name, duration, [(0, 'opacity:0'), (max(0, start-eps), 'opacity:0'),
                                      (start, 'opacity:1'), (end-eps, 'opacity:1'),
                                      (end, 'opacity:0'), (duration, 'opacity:0')])


@dataclass(frozen=True)
class Day:
    date: str
    count: int
    weekday: int
    week: int

    @property
    def x(self):
        return GX + self.week*DX + CELL/2

    @property
    def y(self):
        return GY + self.weekday*DY + CELL/2


@dataclass(frozen=True)
class Shot:
    day: Day
    index: int
    tank_x: float
    angle: float
    muzzle_x: float
    muzzle_y: float

    @property
    def fire(self):
        return self.index*SLOT + LEAD

    @property
    def hit(self):
        return self.fire + FLIGHT


def read_calendar(calendar: dict) -> tuple[list[Day], dict]:
    weeks = calendar['weeks']
    total = calendar['totalContributions']
    if not isinstance(weeks, list) or not 1 <= len(weeks) <= 54:
        raise ValueError('Expected between 1 and 54 calendar weeks')
    if type(total) is not int or total < 0:
        raise ValueError('Invalid contribution total')
    days = []
    for wi, week in enumerate(weeks):
        rows = week['contributionDays']
        if not isinstance(rows, list) or not 1 <= len(rows) <= 7:
            raise ValueError('Invalid week')
        for row in rows:
            date = dt.date.fromisoformat(row['date'])
            count, weekday = row['contributionCount'], row['weekday']
            if type(count) is not int or count < 0 or type(weekday) is not int:
                raise ValueError('Invalid day count or weekday')
            if weekday != (date.weekday()+1) % 7:
                raise ValueError('Weekday/date mismatch')
            days.append(Day(date.isoformat(), count, weekday, wi))
    dates = [dt.date.fromisoformat(d.date) for d in days]
    if not 1 <= len(days) <= 371 or len(set(dates)) != len(dates):
        raise ValueError('Invalid or duplicate calendar dates')
    for prev, curr in zip(days, days[1:]):
        if dt.date.fromisoformat(curr.date)-dt.date.fromisoformat(prev.date) != dt.timedelta(days=1):
            raise ValueError('Calendar days must be consecutive and ordered')
        if curr.week != prev.week + int(curr.weekday == 0):
            raise ValueError('Calendar week mapping is inconsistent')
    if sum(d.count for d in days) != total:
        raise ValueError('Calendar total does not match daily contributions')
    by_date = {dt.date.fromisoformat(d.date): d.count for d in days}
    cursor, streak = dates[-1], 0
    if not by_date[cursor]:
        cursor -= dt.timedelta(days=1)
    while by_date.get(cursor, 0) > 0:
        streak += 1
        cursor -= dt.timedelta(days=1)
    return days, {'total': total, 'active_days': sum(d.count > 0 for d in days),
                  'current_streak': streak, 'best_day': max(d.count for d in days),
                  'period_start': days[0].date, 'period_end': days[-1].date}


def plan_shots(days: list[Day]) -> list[Shot]:
    shots = []
    for i, day in enumerate(d for d in days if d.count > 0):
        tx = max(100, min(762, day.x - 62))
        angle = math.atan2(day.y-TANK_Y, day.x-tx)
        shots.append(Shot(day, i, tx, math.degrees(angle),
                          tx+46*math.cos(angle), TANK_Y+46*math.sin(angle)))
    return shots


def scene_art() -> str:
    rng = random.Random(21)
    art = ''
    # Deliberately faint scenery: contributions remain the focal point.
    for _ in range(44):
        art += rect(rng.randrange(28, 835), rng.randrange(118, 337), 2, 2, '#163249')
    art += '<path d="M22 350V297L57 258L92 291L139 235L180 280L213 260L253 318L301 269L340 317L385 271L452 331L514 276L572 322L630 249L671 281L702 261L754 319L802 278L850 325V368H22Z" fill="#081C2B"/>'
    for x in range(23, 842, 24):
        top = rng.randrange(294, 340, 4)
        art += rect(x, top, 20, 358-top, '#0B2539')
        for y in range(top+7, 348, 13):
            if rng.random() < .6:
                art += rect(x+4, y, 3, 2, '#154263')
    return art


def tank_art() -> str:
    art = '<g id="tank-chassis" shape-rendering="crispEdges">'
    art += '<path d="M-45 15H43L53 25V39L43 46H-43L-53 36V26Z" fill="#071321" stroke="#246693" stroke-width="3"/>'
    art += '<path class="tracks anim" d="M-43 20H40L47 27V35L40 41H-40L-47 34V27Z" fill="none" stroke="#71D7FA" stroke-width="3" stroke-dasharray="4 6"/>'
    for x in (-34, -12, 10, 32):
        art += f'<g transform="translate({x} 31)"><circle r="7" fill="#15486E"/><g class="wheels anim"><path d="M-2 -6H2V-2H6V2H2V6H-2V2H-6V-2H-2Z" fill="#1A9DE1"/></g><rect x="-2" y="-2" width="4" height="4" fill="#B9F4FF"/></g>'
    art += '<path d="M-40 9H29L36 15H45V22H-48V16H-40Z" fill="#168FFF" stroke="#70DAF8" stroke-width="2"/>'
    art += rect(-30, 3, 52, 12, '#185C91') + rect(-37, 13, 20, 3, '#B4F2FF')
    art += rect(30, 15, 12, 4, '#BCF6FF') + rect(-45, 18, 8, 3, '#0B243D')
    art += rect(-28, -21, 2, 26, '#4792BC') + rect(-26, -21, 19, 11, '#0E395D')
    art += '<path d="M-23 -17H-13M-23 -13H-17" stroke="#62E5FF" stroke-width="2"/>'
    art += rect(-7, 7, 15, 7, '#09203A') + text(0, 14, 'S', 8, '#AEEFFF', 'text-anchor="middle"')
    art += '</g><g class="aim anim"><g class="recoil anim">'
    art += '<path d="M-19 -8H-12V-13H7L16 -7V6H-21Z" fill="#218CD4" stroke="#83DCFA" stroke-width="2"/>'
    art += rect(-10, -9, 9, 4, '#A3ECFF') + rect(9, -4, 37, 7, '#73D4EF')
    art += rect(15, -1, 27, 3, '#1D68A0') + rect(41, -6, 6, 11, '#43ABE0')
    art += '</g><g class="muzzle anim"><path d="M48 -3L54 -3L51 -10L61 -4L66 -1L58 4L52 9L54 3H48Z" fill="#BFF9FF"/></g></g>'
    return art


def build_svg(calendar: dict, username: str, stamp: str) -> tuple[str, dict]:
    if not re.fullmatch(r'[A-Za-z0-9-]{1,39}', username):
        raise ValueError('Invalid GitHub login')
    days, metrics = read_calendar(calendar)
    shots = plan_shots(days)
    duration = max(6.0, len(shots)*SLOT+2.0)
    reload_start = duration-.55
    css = [f'.cycle{{animation-duration:{f(duration)}s;animation-timing-function:linear;animation-iteration-count:infinite}}']
    tank_x = shots[0].tank_x if shots else 145
    angle = shots[0].angle if shots else -36
    pos_frames, aim_frames = [(0, f'transform:translateX({f(tank_x)}px)')], [(0, f'transform:rotate({f(angle)}deg)')]
    flash_frames, recoil_frames = [(0, 'opacity:0')], [(0, 'transform:translateX(0)')]
    progress_frames = [(0, 'transform:scaleX(0)')]
    targets, effects, labels, scores = [], [], [], []
    active = {s.day.date: s for s in shots}
    highest = metrics['best_day'] or 1
    grid = []
    for day in days:
        x, y = day.x-CELL/2, day.y-CELL/2
        grid.append(rect(x, y, CELL, CELL, '#0A1B29', 'rx="1" stroke="#16334A" stroke-width=".6"'))
        if not day.count:
            continue
        s = active[day.date]
        idx = min(4, max(0, math.ceil(math.sqrt(day.count/highest)*5)-1))
        css.append(keyframes(f'cell{s.index}', duration, [(0, 'opacity:1'), (s.hit, 'opacity:1'),
                    (s.hit+.02, 'opacity:0'), (reload_start, 'opacity:0'), (duration-.1, 'opacity:1'), (duration, 'opacity:1')]))
        grid.append(f'<g id="day-{day.date}" class="cycle anim cell" style="animation-name:cell{s.index}" data-date="{day.date}" data-count="{day.count}"><title>{day.date}: {day.count} contributions</title>'+rect(x, y, CELL, CELL, COLORS[idx], 'rx="1" stroke="#79D9FD" stroke-opacity=".45" stroke-width=".8"')+'</g>')
    credited = 0
    for s in shots:
        i, day = s.index, s.day
        move_start = i*SLOT
        hold_end = (i+1)*SLOT
        pos_frames += [(move_start+.30, f'transform:translateX({f(s.tank_x)}px)'), (hold_end, f'transform:translateX({f(s.tank_x)}px)')]
        aim_frames += [(move_start+.30, f'transform:rotate({f(s.angle)}deg)'), (hold_end, f'transform:rotate({f(s.angle)}deg)')]
        flash_frames += [(s.fire-.001, 'opacity:0'), (s.fire, 'opacity:1'), (s.fire+.085, 'opacity:1'), (s.fire+.086, 'opacity:0')]
        recoil_frames += [(s.fire, 'transform:translateX(0)'), (s.fire+.045, 'transform:translateX(-4px)'), (s.fire+.17, 'transform:translateX(0)')]
        css.append(keyframes(f'shell{i}', duration, [(0, f'opacity:0;transform:translate({f(s.muzzle_x)}px,{f(s.muzzle_y)}px)'),
            (s.fire-.0001, f'opacity:0;transform:translate({f(s.muzzle_x)}px,{f(s.muzzle_y)}px)'),
            (s.fire, f'opacity:1;transform:translate({f(s.muzzle_x)}px,{f(s.muzzle_y)}px)'),
            (s.hit, f'opacity:1;transform:translate({f(day.x)}px,{f(day.y)}px)'),
            (s.hit+.0001, f'opacity:0;transform:translate({f(day.x)}px,{f(day.y)}px)'), (duration, 'opacity:0')]))
        effects.append(f'<g id="shell-{i}" class="cycle anim transient" opacity="0" style="animation-name:shell{i}"><g transform="rotate({f(s.angle)})"><path d="M-14 0H1" stroke="#168FFF" stroke-width="6" stroke-opacity=".4"/><path d="M-8 0H2" stroke="#A8F6FF" stroke-width="3"/></g></g>')
        css.append(keyframes(f'hit{i}', duration, [(0, 'opacity:0;transform:scale(.2)'), (s.hit-.0001, 'opacity:0;transform:scale(.2)'),
            (s.hit, 'opacity:1;transform:scale(.3)'), (s.hit+.08, 'opacity:.95;transform:scale(1)'),
            (s.hit+.30, 'opacity:0;transform:scale(1.65)'), (duration, 'opacity:0;transform:scale(1.65)')]))
        effects.append(f'<g transform="translate({f(day.x)} {f(day.y)})"><g id="hit-{i}" class="cycle anim transient" opacity="0" style="animation-name:hit{i}" shape-rendering="crispEdges"><path d="M-3 -11H3V-3H11V3H3V11H-3V3H-11V-3H-3Z" fill="#D1FAFF"/><path d="M-16 -13H-11V-8H-16ZM12 -14H16V-10H12ZM-14 12H-10V16H-14ZM12 11H17V16H12Z" fill="#36C7F4"/></g></g>')
        css.append(window(f'lock{i}', duration, move_start+.01, hold_end))
        targets.append(f'<g class="cycle anim transient" opacity="0" style="animation-name:lock{i}"><path d="M{f(day.x-9)} {f(day.y-4)}v-5h5M{f(day.x+4)} {f(day.y-9)}h5v5M{f(day.x+9)} {f(day.y+4)}v5h-5M{f(day.x-4)} {f(day.y+9)}h-5v-5" fill="none" stroke="#C9F7FF" stroke-width="1.5"/></g>')
        labels.append(f'<g class="cycle anim transient" opacity="0" style="animation-name:lock{i}">'+text(40, 402, f'TARGET {day.date}  //  {day.count:,} CONTRIBUTIONS', 13, '#A2EBFF')+'</g>')
        credited += day.count
        end_score = shots[i+1].hit if i+1 < len(shots) else reload_start
        css.append(window(f'score{i}', duration, s.hit, end_score))
        scores.append(f'<g id="score-{i}" class="cycle anim transient" opacity="0" style="animation-name:score{i}">'+text(40, 424, f'CLEARED {i+1:03}/{len(shots):03} DAYS    SCORE {credited:,} / {metrics["total"]:,}', 13, '#62E5FF')+'</g>')
        progress_frames += [(s.hit-.0001, f'transform:scaleX({f(i/max(1,len(shots)))})'), (s.hit, f'transform:scaleX({f((i+1)/max(1,len(shots)))})')]
    if shots:
        pos_frames += [(duration, f'transform:translateX({f(tank_x)}px)')]
        aim_frames += [(duration, f'transform:rotate({f(angle)}deg)')]
    else:
        pos_frames += [(duration/2, 'transform:translateX(740px)'), (duration, f'transform:translateX({tank_x}px)')]
        aim_frames += [(duration/2, 'transform:rotate(-100deg)'), (duration, f'transform:rotate({angle}deg)')]
        labels.append(text(40, 402, 'NO ACTIVE DAYS IN THIS CALENDAR // PATROLLING', 13, '#A2EBFF'))
    flash_frames.append((duration, 'opacity:0'))
    recoil_frames.append((duration, 'transform:translateX(0)'))
    progress_frames += [(reload_start, 'transform:scaleX(1)' if shots else 'transform:scaleX(0)'), (duration-.1, 'transform:scaleX(0)'), (duration, 'transform:scaleX(0)')]
    for name, frames in [('drive', pos_frames), ('aiming', aim_frames), ('flash', flash_frames), ('kick', recoil_frames), ('progress', progress_frames)]:
        css.append(keyframes(name, duration, frames))
    css.append(window('ready', duration, 0.0001, shots[0].hit if shots else duration-.0001))
    scores.append('<g class="cycle anim transient" style="animation-name:ready" opacity="0">'+text(40, 424, f'CLEARED 000/{len(shots):03} DAYS    SCORE 0 / {metrics["total"]:,}', 13, '#62E5FF')+'</g>')
    if shots:
        css.append(window('reload', duration, len(shots)*SLOT, duration-.0001))
        labels.append('<g class="cycle anim transient" style="animation-name:reload" opacity="0">'+text(40, 402, 'SECTOR CLEARED // RELOADING CONTRIBUTION GRID', 13, '#A2EBFF')+'</g>')
    css += [f'.drive{{animation:drive {f(duration)}s linear infinite}}.aim{{animation:aiming {f(duration)}s linear infinite}}',
            f'.muzzle{{opacity:0;animation:flash {f(duration)}s linear infinite}}.recoil{{animation:kick {f(duration)}s linear infinite}}',
            f'.progress{{transform-origin:0 0;animation:progress {f(duration)}s linear infinite}}',
            '@keyframes tracks{to{stroke-dashoffset:-20}}.tracks{animation:tracks .75s linear infinite}',
            '@keyframes wheels{to{transform:rotate(360deg)}}.wheels{animation:wheels .75s linear infinite}',
            '@keyframes radar{50%{opacity:.4}}.radar{animation:radar 2s linear infinite}',
            '.still{display:none}@media(prefers-reduced-motion:reduce){.anim{animation:none!important}.transient,.muzzle{display:none}.still{display:inline}.cell{opacity:1}}']
    months, last_month, last_x = [], None, -100
    for d in days:
        mon = d.date[:7]
        if mon != last_month and d.x-last_x > 35:
            months.append(text(d.x-CELL/2, 142, dt.date.fromisoformat(d.date).strftime('%b'), 10, '#7799B3'))
            last_month, last_x = mon, d.x
    rhs = ''
    for y, label, value in [(116, 'CONTRIBUTIONS', f'{metrics["total"]:,}'), (194, 'ACTIVE DAYS', metrics['active_days']),
                             (272, 'CURRENT STREAK', f'{metrics["current_streak"]} DAYS'), (350, 'BEST DAY', metrics['best_day'])]:
        rhs += rect(874, y-17, 223, 70, '#071625', 'rx="7" stroke="#194B70"')
        rhs += text(892, y+2, label, 11, '#7BAAC6', 'letter-spacing="1"')
        rhs += text(892, y+33, value, 26, '#89EEFF', 'font-weight="700"')
        rhs += '<path d="M1080 '+str(y+25)+'h5v9h-5zM1072 '+str(y+29)+'h5v5h-5zM1064 '+str(y+31)+'h5v3h-5z" fill="#168FFF"/>'
    desc = (f'Original pixel tank automatically aims and fires at every active GitHub calendar day, once per loop. '
            f'Hit cells vanish, the score credits their actual contributions, and the grid returns. '
            f'{metrics["period_start"]} to {metrics["period_end"]}; {metrics["total"]} contributions in {len(shots)} active days. '
            f'Continuous {f(duration)} second animation; snapshot {stamp}. This is a visualization, not a playable game. '
            'Reduced-motion preferences display the intact grid without animation.')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(username)} // Pixel Tank Patrol LIVE</title><desc id="desc">{html.escape(desc)}</desc>
<defs><linearGradient id="panel" x2="1" y2="1"><stop stop-color="#030B14"/><stop offset="1" stop-color="#061828"/></linearGradient><clipPath id="scene"><rect x="22" y="89" width="829" height="280" rx="7"/></clipPath></defs>
<style>text{{font-family:ui-monospace,Consolas,monospace}}{''.join(css)}</style>
<rect x="1" y="1" width="1118" height="460" rx="14" fill="url(#panel)" stroke="#1B5176" stroke-width="2"/>
<path d="M18 40V18H62M1058 18H1102V40M18 422V444H62M1058 444H1102V422" fill="none" stroke="#168FFF" stroke-width="3"/>
{text(32, 28, 'SWIR // ORIGINAL ARCADE', 11, '#62E5FF', 'letter-spacing="2"')}
{text(32, 61, 'PIXEL TANK PATROL', 29, '#C4F5FF', 'font-weight="700" letter-spacing="2"')}
<circle class="radar anim" cx="954" cy="43" r="4" fill="#62E5FF"/>{text(969, 48, 'LIVE / AUTO LOOP', 12, '#62E5FF')}
<path d="M22 77H1097" stroke="#174967"/>
<rect x="22" y="89" width="829" height="280" rx="7" fill="#050F1B" stroke="#1B4661"/>
<g clip-path="url(#scene)">{scene_art()}
{text(40, 114, 'TARGET GRID // 1 CELL = 1 DAY', 12, '#9ECDE7')}
{text(832, 114, 'AIM > FIRE > CLEAR', 11, '#62E5FF', 'text-anchor="end"')}
{''.join(months)}{text(31, GY+DY+9, 'MON', 9)}{text(31, GY+3*DY+9, 'WED', 9)}{text(31, GY+5*DY+9, 'FRI', 9)}
{''.join(grid)}{''.join(targets)}
<path d="M23 369H850M23 371H850" stroke="#327AA6" stroke-width="2"/>
<g transform="translate(0 {TANK_Y})"><g class="drive anim" style="transform:translateX({f(tank_x)}px)">{tank_art()}</g></g>
{''.join(effects)}
</g>{rhs}
{''.join(labels)}{''.join(scores)}
<g class="still">{text(40, 402, 'CONTRIBUTION TARGETS // REDUCED MOTION', 12)}{text(40, 424, f'{len(shots)} ACTIVE DAYS / {metrics["total"]:,} CONTRIBUTIONS', 13, '#62E5FF')}</g>
<rect x="638" y="418" width="194" height="5" fill="#10334B"/><g transform="translate(638 418)"><rect class="progress anim" width="194" height="5" fill="#36C7F4"/></g>
{text(638, 401, 'SECTOR PROGRESS', 10, '#79A8C3')}
{text(40, 449, 'DATA '+stamp+'  /  '+metrics['period_start']+' — '+metrics['period_end'], 10, '#658EA9')}
{text(1094, 431, 'HIT. CLEAR. ADVANCE.', 11, '#7BAAC6', 'text-anchor="end"')}
{text(1094, 448, 'SELF-HOSTED / by Swir', 11, '#62E5FF', 'text-anchor="end"')}
</svg>'''
    validate_svg(svg)
    state = {'schema': 1, 'user': username, 'source': 'GitHub GraphQL contributionCalendar',
             'generated_at': stamp, 'metrics': metrics, 'loop_seconds': duration,
             'target_count': len(shots), 'shot_interval_seconds': SLOT,
             'calendar': calendar}
    return svg, state


def validate_svg(svg: str) -> None:
    if '<!DOCTYPE' in svg.upper() or '<!ENTITY' in svg.upper():
        raise ValueError('DTD or entity declarations are prohibited')
    root = ET.fromstring(svg)
    if root.tag != NS+'svg':
        raise ValueError('Not SVG')
    if len(svg.encode()) > 1_500_000:
        raise ValueError('Unexpectedly large SVG')
    ids = [e.get('id') for e in root.iter() if e.get('id')]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate SVG IDs')
    for element in root.iter():
        if element.tag in (NS+'script', NS+'foreignObject', NS+'image', NS+'iframe'):
            raise ValueError('Executable or external content is prohibited')
        for attr, value in element.attrib.items():
            if attr.lower().startswith('on') or (attr.endswith('href') and not value.startswith('#')):
                raise ValueError('Unsafe SVG attribute')
        if element.tag == NS+'style':
            css = element.text or ''
            if '@import' in css or any(not u.strip('\'\" ').startswith('#') for u in re.findall(r'url\(([^)]+)\)', css)):
                raise ValueError('External CSS resource prohibited')


def publish_outputs(root: Path, outputs: dict[Path, str]) -> None:
    """Stage every file before replacement; API/validation failures never get here."""
    with tempfile.TemporaryDirectory(prefix='.tank-stage-', dir=root) as tmp:
        staged = []
        for i, (relpath, value) in enumerate(outputs.items()):
            dst = root/relpath
            dst.parent.mkdir(parents=True, exist_ok=True)
            src = Path(tmp)/str(i)
            src.write_text(value, encoding='utf-8')
            staged.append((src, dst))
        for src, dst in staged:
            os.replace(src, dst)


def main() -> int:
    try:
        from generate_profile_activity import fetch_calendar, calc_metrics, build_svg as dashboard_svg
        token = os.environ.get('GITHUB_TOKEN', '').strip()
        username = os.environ.get('PROFILE_USER', 'Swir').strip() or 'Swir'
        if not token:
            raise RuntimeError('GITHUB_TOKEN is required')
        calendar = fetch_calendar(token, username)
        read_calendar(calendar)
        version = Path(__file__).read_bytes() + Path(__file__).with_name('generate_profile_activity.py').read_bytes()
        digest = hashlib.sha256(version+username.encode()+json.dumps(calendar, sort_keys=True).encode()).hexdigest()
        try:
            previous = json.loads((ROOT/STATE_PATH).read_text(encoding='utf-8'))
        except (OSError, ValueError):
            previous = {}
        if previous.get('fingerprint') == digest and (ROOT/SVG_PATH).exists() and (ROOT/DASHBOARD_PATH).exists():
            validate_svg((ROOT/SVG_PATH).read_text(encoding='utf-8'))
            validate_svg((ROOT/DASHBOARD_PATH).read_text(encoding='utf-8'))
            print('Contribution data and renderer unchanged; no commit needed.')
            return 0
        stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        svg, state = build_svg(calendar, username, stamp)
        _, weekly, legacy_metrics = calc_metrics(calendar)
        legacy_metrics['recent_streak'] = state['metrics']['current_streak']
        dashboard = dashboard_svg(username, weekly, legacy_metrics)
        validate_svg(dashboard)
        state['fingerprint'] = digest
        publish_outputs(ROOT, {SVG_PATH: svg, DASHBOARD_PATH: dashboard,
                               STATE_PATH: json.dumps(state, indent=2)+'\n'})
        print(f'Published {state["target_count"]} actual daily targets; looping every {state["loop_seconds"]:.1f}s.')
        return 0
    except (OSError, ValueError, RuntimeError, KeyError, TypeError, ET.ParseError) as exc:
        # No raw response/credentials are printed. Last published images remain available.
        print(f'::error::Pixel Tank data refresh failed ({type(exc).__name__}); keeping previously published assets.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
