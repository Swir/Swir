#!/usr/bin/env python3
"""Generate SWIR Robot Arm Factory LIVE from real GitHub contribution data.

Each active contribution day becomes one glowing module in the calendar rack.
A rail-mounted articulated arm picks modules one-by-one, carries them to DEPLOY,
drops them on a moving conveyor, credits their real contribution count, and then
reloads the rack for an infinite loop. Pure SVG/CSS; no viewer-side JS/network.
"""
from __future__ import annotations
import datetime as dt
import hashlib
import html
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG_PATH = Path('assets/github-robot-arm-factory-live.svg')
STATIC_PATH = Path('assets/github-robot-arm-factory-still.svg')
STATE_PATH = Path('assets/robot-arm-factory-state.json')
DASHBOARD_PATH = Path('assets/github-activity-live.svg')
NS = '{http://www.w3.org/2000/svg}'
WIDTH, HEIGHT = 1120, 470
GX, GY, DX, DY, CELL = 46, 174, 12, 15, 9
RAIL_Y = 111
BASE_Y = 121
L1 = 90.0
L2 = 90.0
DEPLOY_X = 806.0
DEPLOY_Y = 280.0
DEPLOY_BASE_X = 735.0
SLOT = 1.95
PICK_TIME = .70
DROP_TIME = 1.42
COLORS = ('#1F6F8E', '#1C9A8E', '#25BFA3', '#56D889', '#8AF5A7')

def f(n: float) -> str:
    return f'{n:.6f}'.rstrip('0').rstrip('.') or '0'

def rect(x, y, w, h, fill, extra='') -> str:
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}" {extra}/>'

def text(x, y, value, size=12, fill='#95B6CE', extra='') -> str:
    return (f'<text x="{f(x)}" y="{f(y)}" font-size="{size}" fill="{fill}" '
            f'{extra}>{html.escape(str(value))}</text>')

def keyframes(name: str, duration: float, frames: list[tuple[float, str]]) -> str:
    return '@keyframes '+name+'{'+''.join(f'{f(100*t/duration)}%{{{props}}}' for t, props in frames)+'}'

def window(name: str, duration: float, start: float, end: float) -> str:
    eps = min(.0001, max(.00001, (end-start)/10))
    return keyframes(name, duration, [(0,'opacity:0'),(max(0,start-eps),'opacity:0'),(start,'opacity:1'),(max(start,end-eps),'opacity:1'),(end,'opacity:0'),(duration,'opacity:0')])

def read_calendar(calendar: dict):
    weeks = calendar['weeks']
    total = calendar['totalContributions']
    if not isinstance(weeks,list) or not 1 <= len(weeks) <= 54:
        raise ValueError('Expected 1..54 contribution weeks')
    if type(total) is not int or total < 0:
        raise ValueError('Invalid totalContributions')
    days=[]
    for wi,week in enumerate(weeks):
        rows=week['contributionDays']
        if not isinstance(rows,list) or not 1 <= len(rows) <= 7:
            raise ValueError('Invalid contribution week')
        for row in rows:
            date=dt.date.fromisoformat(row['date'])
            count,weekday=row['contributionCount'],row['weekday']
            if type(count) is not int or count < 0 or type(weekday) is not int:
                raise ValueError('Invalid contribution day')
            if weekday != (date.weekday()+1)%7:
                raise ValueError('Weekday/date mismatch')
            days.append({'date':date.isoformat(),'count':count,'weekday':weekday,'week':wi})
    if not days or len(days)>371:
        raise ValueError('Invalid calendar size')
    dates=[dt.date.fromisoformat(d['date']) for d in days]
    if len(set(dates)) != len(dates):
        raise ValueError('Duplicate contribution date')
    for prev,curr in zip(days,days[1:]):
        pd,cd=dt.date.fromisoformat(prev['date']),dt.date.fromisoformat(curr['date'])
        if cd-pd != dt.timedelta(days=1):
            raise ValueError('Contribution days must be consecutive')
        if curr['week'] != prev['week'] + int(curr['weekday']==0):
            raise ValueError('Contribution week mapping is inconsistent')
    if sum(d['count'] for d in days) != total:
        raise ValueError('Calendar total mismatch')
    by_date={dt.date.fromisoformat(d['date']):d['count'] for d in days}
    cursor=dates[-1]
    if by_date[cursor]==0:
        cursor-=dt.timedelta(days=1)
    streak=0
    while by_date.get(cursor,0)>0:
        streak+=1
        cursor-=dt.timedelta(days=1)
    metrics={'total':total,'active_days':sum(d['count']>0 for d in days),'current_streak':streak,'best_day':max(d['count'] for d in days),'period_start':days[0]['date'],'period_end':days[-1]['date']}
    return days,metrics

def coords(day: dict):
    return GX+day['week']*DX+CELL/2, GY+day['weekday']*DY+CELL/2

def ik(base_x: float,target_x: float,target_y: float):
    dx=target_x-base_x
    dy=target_y-BASE_Y
    r2=dx*dx+dy*dy
    cos2=max(-1.0,min(1.0,(r2-L1*L1-L2*L2)/(2*L1*L2)))
    theta2=math.acos(cos2)
    theta1=math.atan2(dy,dx)-math.atan2(L2*math.sin(theta2),L1+L2*math.cos(theta2))
    return math.degrees(theta1),math.degrees(theta2)

def module_color(count: int,best: int):
    if count<=0:
        return '#0B1A22'
    level=min(4,max(0,math.ceil(math.sqrt(count/max(1,best))*5)-1))
    return COLORS[level]

def factory_background():
    parts=[
        rect(20,86,837,292,'#06111A','rx="7" stroke="#1D485A"'),
        rect(20,86,837,42,'#091A22'),
        '<path d="M36 120H838" stroke="#234D5B" stroke-width="2"/>',
        '<path d="M36 136H838" stroke="#102F3B" stroke-width="1"/>',
        rect(35,337,808,31,'#071820','rx="5" stroke="#174553"'),
        '<path class="belt anim" d="M45 352H835" stroke="#65D7C0" stroke-opacity=".75" stroke-width="4" stroke-dasharray="10 13"/>',
        text(42,104,'GITHUB FACTORY // INPUT RACK',11,'#76C9D2','letter-spacing="1.2"'),
        text(842,104,'LIVE LINE',10,'#6BF0B5','text-anchor="end"'),
        rect(708,161,137,159,'#081B22','rx="7" stroke="#2A6D62"'),
        text(776,184,'DEPLOY',18,'#8AF5A7','text-anchor="middle" font-weight="700" letter-spacing="2"'),
        '<path d="M733 199H819V292H733Z" fill="#061319" stroke="#2F786B" stroke-width="2"/>',
        '<path d="M748 209V278M764 209V278M780 209V278M796 209V278M812 209V278" stroke="#123E38"/>',
        '<path d="M740 301H812" stroke="#74EDAF" stroke-width="3"/>',
        text(776,314,'OUTPUT',10,'#66B7A5','text-anchor="middle"'),
        rect(62,291,561,30,'#07171F','rx="4" stroke="#184652"'),
        text(76,310,'ACTIVE MODULES = CONTRIBUTION DAYS',10,'#6998A7','letter-spacing="1"'),
    ]
    for x in (82,175,268,361,454,547,640):
        parts.append(rect(x,98,2,24,'#173A45'))
        parts.append(rect(x-4,96,10,4,'#235869'))
    for x in range(50,840,46):
        parts.append(f'<circle cx="{x}" cy="353" r="7" fill="#0C2A32" stroke="#1F5660"/>')
    return ''.join(parts)

def robot_art(carry_groups: str):
    return f'''<g transform="translate(0 {BASE_Y})"><g id="carriage" class="arm-carriage anim" style="transform:translateX(260px)">
  <g transform="translate(0 {-BASE_Y})">
    <rect x="-31" y="{RAIL_Y-13}" width="62" height="25" rx="5" fill="#172731" stroke="#F0A33C" stroke-width="2"/>
    <circle cx="-18" cy="{RAIL_Y-1}" r="5" fill="#FFBA52"/><circle cx="18" cy="{RAIL_Y-1}" r="5" fill="#FFBA52"/>
  </g>
  <circle r="12" fill="#27343A" stroke="#FFAF3F" stroke-width="4"/>
  <g id="shoulder" class="arm-shoulder anim">
    <rect x="0" y="-9" width="{L1}" height="18" rx="8" fill="#E8912C" stroke="#FFD27A" stroke-width="2"/>
    <rect x="12" y="-4" width="53" height="8" fill="#8B4E16" opacity=".55"/>
    <g transform="translate({L1} 0)">
      <circle r="11" fill="#27343A" stroke="#FFB84F" stroke-width="4"/>
      <g id="elbow" class="arm-elbow anim">
        <rect x="0" y="-8" width="{L2}" height="16" rx="7" fill="#F0A039" stroke="#FFD98A" stroke-width="2"/>
        <rect x="12" y="-3" width="54" height="6" fill="#8A4D16" opacity=".55"/>
        <g transform="translate({L2} 0)">
          <g id="gripper" class="gripper anim">
            <circle r="8" fill="#1D2D34" stroke="#77E6BE" stroke-width="3"/>
            <path d="M-7 6V17H-13M7 6V17H13" fill="none" stroke="#8AF5A7" stroke-width="4"/>
            <rect x="-10" y="18" width="20" height="5" rx="2" fill="#1C4B45"/>
            {carry_groups}
          </g>
        </g>
      </g>
    </g>
  </g>
</g></g>'''

def build_svg(calendar: dict,username: str,stamp: str):
    if not re.fullmatch(r'[A-Za-z0-9-]{1,39}',username):
        raise ValueError('Invalid GitHub login')
    days,metrics=read_calendar(calendar)
    active=[d for d in days if d['count']>0]
    duration=max(7.0,len(active)*SLOT+2.2)
    reload_start=duration-.75
    best=metrics['best_day'] or 1
    css=[]; grid=[]; selectors=[]; pickup_fx=[]; deploy_fx=[]; labels=[]; scores=[]; carry_groups=[]; deployed_boxes=[]; operations=[]
    carriage_frames=[(0,'transform:translate(260px,0)')]
    shoulder_frames=[(0,'transform:rotate(78deg)')]
    elbow_frames=[(0,'transform:rotate(24deg)')]
    gripper_frames=[(0,'transform:scale(1)')]
    progress_frames=[(0,'transform:scaleX(0)')]
    for day in days:
        x,y=coords(day)
        grid.append(rect(x-CELL/2,y-CELL/2,CELL,CELL,'#0B1A22','rx="1" stroke="#173541" stroke-width=".6"'))
        if day['count']<=0:
            continue
        idx=len(operations)
        base_x=max(76.0,min(650.0,x-38.0))
        a1,a2=ik(base_x,x,y)
        d1,d2=ik(DEPLOY_BASE_X,DEPLOY_X,DEPLOY_Y)
        t0=idx*SLOT
        arrive=t0+.34; pick=t0+PICK_TIME; carry=pick+.12; deploy_arrive=t0+1.18; drop=t0+DROP_TIME; settle=min((idx+1)*SLOT,drop+.34)
        color=module_color(day['count'],best)
        operations.append({'index':idx,'date':day['date'],'count':day['count'],'pick':pick,'drop':drop,'x':x,'y':y,'base_x':base_x,'target_angles':[a1,a2]})
        css.append(keyframes(f'module{idx}',duration,[(0,'opacity:1'),(pick,'opacity:1'),(pick+.015,'opacity:0'),(reload_start,'opacity:0'),(duration-.12,'opacity:1'),(duration,'opacity:1')]))
        grid.append(f'<g id="module-{day["date"]}" class="module anim" style="animation:module{idx} {f(duration)}s linear infinite" data-date="{day["date"]}" data-count="{day["count"]}"><title>{day["date"]}: {day["count"]} contributions</title>'+rect(x-CELL/2,y-CELL/2,CELL,CELL,color,'rx="1" stroke="#B8FFD8" stroke-opacity=".6"')+'</g>')
        css.append(window(f'select{idx}',duration,arrive,pick+.02))
        selectors.append(f'<g class="anim transient" style="opacity:0;animation:select{idx} {f(duration)}s linear infinite"><path d="M{f(x-8)} {f(y-5)}v-4h4M{f(x+4)} {f(y-9)}h4v4M{f(x+8)} {f(y+5)}v4h-4M{f(x-4)} {f(y+9)}h-4v-4" fill="none" stroke="#9AFFBF" stroke-width="1.4"/></g>')
        css.append(window(f'pickup{idx}',duration,pick,pick+.26))
        pickup_fx.append(f'<g transform="translate({f(x)} {f(y)})" class="anim transient pickup-spark" style="opacity:0;animation:pickup{idx} {f(duration)}s linear infinite"><path d="M-2 -12H2V-4H11V2H3V11H-3V3H-11V-3H-3Z" fill="#C9FFE0"/></g>')
        css.append(window(f'carry{idx}',duration,carry,drop))
        carry_groups.append(f'<g id="carry-{idx}" class="anim transient" style="opacity:0;animation:carry{idx} {f(duration)}s linear infinite">'+rect(-6,23,12,12,color,'rx="2" stroke="#D1FFE1"')+'</g>')
        css.append(window(f'deploy{idx}',duration,drop,drop+.28))
        deploy_fx.append(f'<g transform="translate({DEPLOY_X} {DEPLOY_Y})" class="anim transient" style="opacity:0;animation:deploy{idx} {f(duration)}s linear infinite"><circle r="17" fill="none" stroke="#8AF5A7" stroke-width="3"/></g>')
        css.append(keyframes(f'box{idx}',duration,[(0,'opacity:0;transform:translateX(0)'),(drop-.001,'opacity:0;transform:translateX(0)'),(drop,'opacity:1;transform:translateX(0)'),(min(reload_start,drop+2.2),'opacity:.8;transform:translateX(95px)'),(reload_start,'opacity:0;transform:translateX(130px)'),(duration,'opacity:0;transform:translateX(130px)')]))
        deployed_boxes.append(f'<g transform="translate(758 342)"><g class="anim transient" style="opacity:0;animation:box{idx} {f(duration)}s linear infinite">'+rect(0,0,15,12,color,'rx="2" stroke="#CFFFE0"')+'</g></g>')
        carriage_frames += [(arrive,f'transform:translate({f(base_x)}px,0)'),(pick+.05,f'transform:translate({f(base_x)}px,0)'),(deploy_arrive,f'transform:translate({f(DEPLOY_BASE_X)}px,0)'),(drop+.08,f'transform:translate({f(DEPLOY_BASE_X)}px,0)'),(settle,f'transform:translate({f(DEPLOY_BASE_X)}px,0)')]
        shoulder_frames += [(arrive,f'transform:rotate({f(a1)}deg)'),(pick+.05,f'transform:rotate({f(a1)}deg)'),(deploy_arrive,f'transform:rotate({f(d1)}deg)'),(drop+.08,f'transform:rotate({f(d1)}deg)'),(settle,'transform:rotate(78deg)')]
        elbow_frames += [(arrive,f'transform:rotate({f(a2)}deg)'),(pick+.05,f'transform:rotate({f(a2)}deg)'),(deploy_arrive,f'transform:rotate({f(d2)}deg)'),(drop+.08,f'transform:rotate({f(d2)}deg)'),(settle,'transform:rotate(24deg)')]
        gripper_frames += [(pick-.05,'transform:scale(1)'),(pick,'transform:scale(.78)'),(pick+.1,'transform:scale(.78)'),(drop-.05,'transform:scale(.78)'),(drop,'transform:scale(1)'),(settle,'transform:scale(1)')]
        css.append(window(f'label{idx}',duration,arrive,drop+.01))
        labels.append(f'<g class="anim transient" style="opacity:0;animation:label{idx} {f(duration)}s linear infinite">'+text(42,407,f'PICK {day["date"]} // {day["count"]:,} CONTRIBUTIONS → DEPLOY',13,'#A9F7C5')+'</g>')
        credited=sum(op['count'] for op in operations)
        next_drop=(idx+1)*SLOT+DROP_TIME if idx+1<len(active) else reload_start
        css.append(window(f'score{idx}',duration,drop,next_drop))
        scores.append(f'<g id="score-{idx}" class="anim transient" style="opacity:0;animation:score{idx} {f(duration)}s linear infinite">'+text(42,430,f'PROCESSED {idx+1:03}/{len(active):03} DAYS   OUTPUT {credited:,}/{metrics["total"]:,}',13,'#6FF0B0')+'</g>')
        progress_frames += [(drop-.001,f'transform:scaleX({f(idx/max(1,len(active)))})'),(drop,f'transform:scaleX({f((idx+1)/max(1,len(active)))})')]
    if not active:
        carriage_frames += [(duration/2,'transform:translate(620px,0)'),(duration,'transform:translate(260px,0)')]
        shoulder_frames += [(duration/2,'transform:rotate(112deg)'),(duration,'transform:rotate(78deg)')]
        elbow_frames += [(duration/2,'transform:rotate(38deg)'),(duration,'transform:rotate(24deg)')]
        labels.append(text(42,407,'NO ACTIVE MODULES // FACTORY IDLE SWEEP',13,'#A9F7C5'))
    carriage_frames.append((duration,'transform:translate(260px,0)'))
    shoulder_frames.append((duration,'transform:rotate(78deg)'))
    elbow_frames.append((duration,'transform:rotate(24deg)'))
    gripper_frames.append((duration,'transform:scale(1)'))
    progress_frames += [(reload_start,'transform:scaleX(1)' if active else 'transform:scaleX(0)'),(duration-.12,'transform:scaleX(0)'),(duration,'transform:scaleX(0)')]
    css += [keyframes('carriageMove',duration,carriage_frames),keyframes('shoulderMove',duration,shoulder_frames),keyframes('elbowMove',duration,elbow_frames),keyframes('gripperMove',duration,gripper_frames),keyframes('factoryProgress',duration,progress_frames),f'.arm-carriage{{animation:carriageMove {f(duration)}s linear infinite}}',f'.arm-shoulder{{transform-origin:0 0;animation:shoulderMove {f(duration)}s linear infinite}}',f'.arm-elbow{{transform-origin:0 0;animation:elbowMove {f(duration)}s linear infinite}}',f'.gripper{{transform-origin:0 0;animation:gripperMove {f(duration)}s linear infinite}}',f'.progress{{transform-origin:0 0;animation:factoryProgress {f(duration)}s linear infinite}}','@keyframes beltFlow{to{stroke-dashoffset:-46}}.belt{animation:beltFlow .9s linear infinite}','@keyframes beacon{50%{opacity:.28}}.beacon{animation:beacon 1.4s linear infinite}','@media(prefers-reduced-motion:reduce){.beacon{animation:none}.pickup-spark{visibility:hidden}}']
    if active:
        css.append(window('ready',duration,.001,operations[0]['drop']))
        scores.append('<g class="anim transient" style="opacity:0;animation:ready '+f(duration)+'s linear infinite">'+text(42,430,f'PROCESSED 000/{len(active):03} DAYS   OUTPUT 0/{metrics["total"]:,}',13,'#6FF0B0')+'</g>')
        css.append(window('reload',duration,len(active)*SLOT,duration-.001))
        labels.append('<g class="anim transient" style="opacity:0;animation:reload '+f(duration)+'s linear infinite">'+text(42,407,'SHIFT COMPLETE // RELOADING CONTRIBUTION MODULES',13,'#A9F7C5')+'</g>')
    months=[]; last_month=None; last_x=-100
    for day in days:
        x,_=coords(day); mon=day['date'][:7]
        if mon != last_month and x-last_x>32:
            months.append(text(x-CELL/2,161,dt.date.fromisoformat(day['date']).strftime('%b'),9,'#678998'))
            last_month,last_x=mon,x
    rhs=''
    for y,label,value in [(119,'CONTRIBUTIONS',f'{metrics["total"]:,}'),(199,'ACTIVE DAYS',metrics['active_days']),(279,'CURRENT STREAK',f'{metrics["current_streak"]} DAYS'),(359,'BEST DAY',metrics['best_day'])]:
        rhs += rect(875,y-17,222,70,'#071720','rx="7" stroke="#1D5B50"') + text(893,y+2,label,11,'#7CB8AE','letter-spacing="1"') + text(893,y+33,value,26,'#8AF5A7','font-weight="700"')
    desc=f'Robot Arm Factory LIVE processes every active GitHub contribution day exactly once per loop. {metrics["total"]} contributions in {len(active)} active days. Continuous {f(duration)} second loop; snapshot {stamp}.'
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(username)} // Robot Arm Factory LIVE</title><desc id="desc">{html.escape(desc)}</desc>
<defs><linearGradient id="panel" x2="1" y2="1"><stop stop-color="#030B10"/><stop offset="1" stop-color="#071A1D"/></linearGradient></defs>
<style>text{{font-family:ui-monospace,Consolas,monospace}}{''.join(css)}</style>
<rect x="1" y="1" width="1118" height="468" rx="14" fill="url(#panel)" stroke="#1B5B55" stroke-width="2"/>
<path d="M18 40V18H62M1058 18H1102V40M18 430V452H62M1058 452H1102V430" fill="none" stroke="#36D9A0" stroke-width="3"/>
{text(32,28,'SWIR // BUILD SYSTEM',11,'#6EF0B0','letter-spacing="2"')}{text(32,62,'ROBOT ARM FACTORY',29,'#D6FFE3','font-weight="700" letter-spacing="2"')}
<circle class="beacon anim" cx="948" cy="42" r="5" fill="#8AF5A7"/>{text(964,47,'LIVE / AUTO PRODUCTION',12,'#8AF5A7')}<path d="M22 78H1097" stroke="#1A514B"/>
{factory_background()}<path d="M38 {RAIL_Y}H846" stroke="#874F19" stroke-width="8"/><path d="M38 {RAIL_Y}H846" stroke="#FFB64D" stroke-width="2" stroke-dasharray="18 10"/>
{text(40,147,'INPUT CALENDAR // 1 MODULE = 1 DAY',11,'#78A9AD')}{''.join(months)}{text(29,GY+DY+7,'MON',9)}{text(29,GY+3*DY+7,'WED',9)}{text(29,GY+5*DY+7,'FRI',9)}
{''.join(grid)}{''.join(selectors)}{robot_art(''.join(carry_groups))}{''.join(pickup_fx)}{''.join(deploy_fx)}{''.join(deployed_boxes)}{rhs}{''.join(labels)}{''.join(scores)}
<g class="still" style="display:none">{text(42,407,'ROBOT ARM FACTORY // STATIC VIEW',12,'#A9F7C5')}{text(42,430,f'{len(active)} ACTIVE MODULES / {metrics["total"]:,} CONTRIBUTIONS',13,'#6FF0B0')}</g>
<rect x="645" y="420" width="194" height="5" fill="#12372F"/><g transform="translate(645 420)"><rect class="progress anim" width="194" height="5" fill="#56D889"/></g>{text(645,403,'SHIFT PROGRESS',10,'#78A995')}
{text(42,456,'DATA '+stamp+' / '+metrics['period_start']+' — '+metrics['period_end'],10,'#658C83')}{text(1095,437,'PICK → PROCESS → DEPLOY → REPEAT',11,'#79BAA5','text-anchor="end"')}{text(1095,455,'SELF-HOSTED / by Swir',11,'#8AF5A7','text-anchor="end"')}
</svg>'''
    validate_svg(svg)
    state={'schema':1,'renderer_version':'1.0','motion':'continuous','user':username,'source':'GitHub GraphQL contributionCalendar','generated_at':stamp,'metrics':metrics,'loop_seconds':duration,'target_count':len(active),'slot_seconds':SLOT,'operations':operations,'calendar':calendar}
    return svg,state

def build_static_svg(svg: str):
    root=ET.fromstring(svg)
    for element in root.iter(NS+'style'):
        element.text='text{font-family:ui-monospace,Consolas,monospace}.transient{display:none}.module{opacity:1}.still{display:inline!important}.progress{transform:scaleX(0)}'
    for element in root.iter(NS+'text'):
        if element.text=='LIVE / AUTO PRODUCTION':
            element.text='STATIC / NO MOTION'
    ET.register_namespace('',NS[1:-1])
    result=ET.tostring(root,encoding='unicode')
    validate_svg(result)
    return result

def validate_svg(svg: str):
    upper=svg.upper()
    if '<!DOCTYPE' in upper or '<!ENTITY' in upper:
        raise ValueError('DTD/entities prohibited')
    root=ET.fromstring(svg)
    if root.tag != NS+'svg':
        raise ValueError('Not SVG')
    if len(svg.encode()) > 1600000:
        raise ValueError('SVG unexpectedly large')
    ids=[e.get('id') for e in root.iter() if e.get('id')]
    if len(ids)!=len(set(ids)):
        raise ValueError('Duplicate SVG IDs')
    for element in root.iter():
        if element.tag in (NS+'script',NS+'foreignObject',NS+'image',NS+'iframe'):
            raise ValueError('Executable/external content prohibited')

def publish_outputs(root: Path,outputs: dict[Path,str]):
    with tempfile.TemporaryDirectory(prefix='.factory-stage-',dir=root) as tmp:
        staged=[]
        for i,(relpath,value) in enumerate(outputs.items()):
            dst=root/relpath; dst.parent.mkdir(parents=True,exist_ok=True)
            src=Path(tmp)/str(i); src.write_text(value,encoding='utf-8'); staged.append((src,dst))
        for src,dst in staged:
            os.replace(src,dst)

def main():
    try:
        from generate_profile_activity import fetch_calendar,calc_metrics,build_svg as dashboard_svg
        token=os.environ.get('GITHUB_TOKEN','').strip()
        username=os.environ.get('PROFILE_USER','Swir').strip() or 'Swir'
        if not token:
            raise RuntimeError('GITHUB_TOKEN is required')
        calendar=fetch_calendar(token,username)
        read_calendar(calendar)
        version=Path(__file__).read_bytes()+Path(__file__).with_name('generate_profile_activity.py').read_bytes()
        digest=hashlib.sha256(version+username.encode()+json.dumps(calendar,sort_keys=True).encode()).hexdigest()
        try:
            previous=json.loads((ROOT/STATE_PATH).read_text(encoding='utf-8'))
        except (OSError,ValueError):
            previous={}
        if previous.get('fingerprint')==digest and (ROOT/SVG_PATH).exists() and (ROOT/STATIC_PATH).exists() and (ROOT/DASHBOARD_PATH).exists():
            validate_svg((ROOT/SVG_PATH).read_text()); validate_svg((ROOT/STATIC_PATH).read_text()); validate_svg((ROOT/DASHBOARD_PATH).read_text())
            print('Factory data and renderer unchanged; no commit needed.')
            return 0
        stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        svg,state=build_svg(calendar,username,stamp)
        _,weekly,legacy_metrics=calc_metrics(calendar)
        legacy_metrics['recent_streak']=state['metrics']['current_streak']
        dashboard=dashboard_svg(username,weekly,legacy_metrics)
        validate_svg(dashboard)
        state['fingerprint']=digest
        publish_outputs(ROOT,{SVG_PATH:svg,STATIC_PATH:build_static_svg(svg),DASHBOARD_PATH:dashboard,STATE_PATH:json.dumps(state,indent=2)+'\n'})
        print(f'Published Robot Arm Factory with {state["target_count"]} real modules; loop {state["loop_seconds"]:.1f}s.')
        return 0
    except (OSError,ValueError,RuntimeError,KeyError,TypeError,ET.ParseError) as exc:
        print(f'::error::Robot Arm Factory refresh failed ({type(exc).__name__}); keeping previous assets.',file=sys.stderr)
        return 1

if __name__=='__main__':
    raise SystemExit(main())
