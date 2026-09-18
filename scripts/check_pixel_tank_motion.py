#!/usr/bin/env python3
"""Browser regression: test the actual generated SVG in <img>, not a mockup.

Dependencies for this optional integration check: playwright==1.57.0, Pillow.
Normal scheduled data refreshes do not need them. No network is used by the test.
"""
from __future__ import annotations
import base64
import io
import json
import os
from pathlib import Path
import shutil
import sys

from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright
import generate_pixel_tank_patrol as tank

ROOT = Path(__file__).resolve().parents[1]


def changed(a: bytes, b: bytes, box=None) -> int:
    left, right = Image.open(io.BytesIO(a)).convert('RGB'), Image.open(io.BytesIO(b)).convert('RGB')
    if box:
        left, right = left.crop(box), right.crop(box)
    diff = ImageChops.difference(left, right)
    return sum(max(p) > 20 for p in diff.getdata())


def inspect(page, selector):
    return page.eval_on_selector(selector, """e => {
      const s = getComputedStyle(e), m = e.getCTM();
      return {opacity:Number(s.opacity), display:s.display,
        x:m.e,y:m.f,animation:s.animationName};
    }""")


def seek(page, seconds: float):
    page.evaluate('t => document.getAnimations().forEach(a => {a.pause(); a.currentTime=t*1000;})', seconds)
    page.evaluate('() => document.documentElement.getBoundingClientRect()')
    page.wait_for_timeout(25)


def verify(asset: Path, state_path: Path, out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    svg = asset.read_text(encoding='utf-8')
    state = json.loads(state_path.read_text(encoding='utf-8'))
    days, _ = tank.read_calendar(state['calendar'])
    shots = tank.plan_shots(days)
    duration = float(state['loop_seconds'])
    report = {'asset': asset.name, 'target_count':len(shots), 'loop_seconds':duration, 'contexts':{}}
    executable = os.environ.get('CHROMIUM_PATH') or shutil.which('chromium')
    with sync_playwright() as p:
        for reduced in (False, True):
            mode = 'os-reduced-motion' if reduced else 'normal'
            opts = {'headless':True, 'args':['--no-sandbox'] + (['--force-prefers-reduced-motion'] if reduced else [])}
            if executable:
                opts['executable_path'] = executable
            browser = p.chromium.launch(**opts)
            page = browser.new_page(viewport={'width':tank.WIDTH, 'height':tank.HEIGHT},device_scale_factor=1)
            data = 'data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
            # Simulate the collapsed section used by GitHub README, then reveal it.
            page.set_content('<!doctype html><body style="margin:0"><details><summary>Activity</summary>'
                             f'<img id="tank" width="{tank.WIDTH}" height="{tank.HEIGHT}" src="{data}"></details>')
            page.wait_for_timeout(150)
            page.locator('details').evaluate('(e)=>e.open=true')
            page.wait_for_function('document.querySelector("img").naturalWidth > 0')
            page.wait_for_timeout(150)
            image = page.locator('#tank')
            before = image.screenshot(animations='allow')
            page.wait_for_timeout(2100)
            after = image.screenshot(animations='allow')
            body_changes = changed(before, after, (22,280,850,369))
            assert body_changes > 100, f'{mode}: tank is static in an image element ({body_changes} changed pixels)'
            (out/f'{mode}-before.png').write_bytes(before)
            (out/f'{mode}-after.png').write_bytes(after)
            result = {'image_tank_changed_pixels':body_changes, 'checks':[]}
            # Inspect geometry/timing at controlled times in the exact same SVG.
            page.set_content('<body style="margin:0">'+svg)
            page.wait_for_timeout(30)
            if shots:
                first = shots[0]
                for base in (0.0, duration):
                    seek(page,base+first.fire+.20)
                    shell = inspect(page, '#shell-0')
                    assert shell['opacity'] > .98 and shell['display'] != 'none', f'{mode}: missing visible shell'
                    u=.20/tank.FLIGHT
                    ex=first.muzzle_x+(first.day.x-first.muzzle_x)*u
                    ey=first.muzzle_y+(first.day.y-first.muzzle_y)*u
                    assert abs(shell['x']-ex)<1 and abs(shell['y']-ey)<1, f'{mode}: shell misses target ray'
                    seek(page,base+first.hit+.07)
                    assert inspect(page,'#day-'+first.day.date)['opacity']<.01, f'{mode}: hit cell did not disappear'
                    assert inspect(page,'#score-0')['opacity']>.98, f'{mode}: score not credited'
                    if len(shots)>1:
                        assert inspect(page,'#day-'+shots[1].day.date)['opacity']>.98, f'{mode}: unhit cell disappeared'
                    result['checks'].append('first-shot-hit-clear-score-cycle-'+str(1+int(base>0)))
                seek(page,duration-.04)
                assert inspect(page,'#day-'+first.day.date)['opacity']>.98, f'{mode}: grid did not reload'
                result['checks'].append('grid-restored')
            # Explicit static alternative is still available and really motionless.
            static=tank.build_static_svg(svg)
            page.set_content('<body style="margin:0">'+static)
            assert not page.evaluate('document.getAnimations().length'), 'Static alternative has animations'
            if shots:
                assert inspect(page,'#day-'+shots[0].day.date)['opacity']>.98
            result['checks'].append('explicit-static-view')
            report['contexts'][mode]=result
            browser.close()
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report


if __name__ == '__main__':
    asset=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/tank.SVG_PATH
    state=Path(sys.argv[2]) if len(sys.argv)>2 else ROOT/tank.STATE_PATH
    out=Path(sys.argv[3]) if len(sys.argv)>3 else ROOT/'motion-evidence'
    print(json.dumps(verify(asset,state,out),indent=2))
