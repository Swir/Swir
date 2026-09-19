#!/usr/bin/env python3
import base64,io,json,os,shutil,sys
from pathlib import Path
from PIL import Image,ImageChops
from playwright.sync_api import sync_playwright
import generate_robot_arm_factory as factory
ROOT=Path(__file__).resolve().parents[1]
def changed(a,b):
    x=Image.open(io.BytesIO(a)).convert('RGB'); y=Image.open(io.BytesIO(b)).convert('RGB')
    return sum(max(p)>18 for p in ImageChops.difference(x,y).getdata())
def inspect(page,sel):
    return page.eval_on_selector(sel,"e=>{const s=getComputedStyle(e),m=e.getCTM();return {opacity:Number(s.opacity),x:m.e,y:m.f}}")
def seek(page,t):
    page.evaluate('t=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=t*1000})',t); page.wait_for_timeout(20)
def verify(asset,state_path,out):
    out.mkdir(parents=True,exist_ok=True); svg=asset.read_text(); state=json.loads(state_path.read_text()); ops=state['operations']; duration=float(state['loop_seconds'])
    executable=os.environ.get('CHROMIUM_PATH') or shutil.which('chromium')
    with sync_playwright() as p:
        opts={'headless':True,'args':['--no-sandbox']}
        if executable: opts['executable_path']=executable
        browser=p.chromium.launch(**opts); page=browser.new_page(viewport={'width':factory.WIDTH,'height':factory.HEIGHT})
        data='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
        page.set_content(f'<body style="margin:0"><img id="factory" width="{factory.WIDTH}" height="{factory.HEIGHT}" src="{data}"></body>')
        page.wait_for_function('document.querySelector("img").naturalWidth>0')
        a=page.locator('#factory').screenshot(animations='allow'); page.wait_for_timeout(2300); b=page.locator('#factory').screenshot(animations='allow')
        assert changed(a,b)>200
        (out/'before.png').write_bytes(a); (out/'after.png').write_bytes(b)
        page.set_content('<body style="margin:0">'+svg)
        if ops:
            op=ops[0]; seek(page,op['pick']+.16)
            assert inspect(page,'#module-'+op['date'])['opacity']<.02; assert inspect(page,'#carry-0')['opacity']>.95
            px=inspect(page,'#carriage')['x']; seek(page,op['drop']+.04)
            assert inspect(page,'#carry-0')['opacity']<.02; assert inspect(page,'#score-0')['opacity']>.95
            assert abs(inspect(page,'#carriage')['x']-px)>50
            seek(page,duration-.05); assert inspect(page,'#module-'+op['date'])['opacity']>.95
            assert page.eval_on_selector('#carriage',"e=>getComputedStyle(e).animationIterationCount")=='infinite'
        static=factory.build_static_svg(svg); page.set_content('<body>'+static); assert page.evaluate('document.getAnimations().length')==0
        browser.close()
    report={'loop_seconds':duration,'operations':len(ops),'checks':['img-motion','pick','carry','deploy','score','reload','infinite-loop','static']}
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n'); return report
if __name__=='__main__':
    asset=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/factory.SVG_PATH
    state=Path(sys.argv[2]) if len(sys.argv)>2 else ROOT/factory.STATE_PATH
    out=Path(sys.argv[3]) if len(sys.argv)>3 else ROOT/'robot-motion-evidence'
    print(json.dumps(verify(asset,state,out),indent=2))
