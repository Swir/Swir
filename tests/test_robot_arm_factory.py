import datetime as dt
import math
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import generate_robot_arm_factory as factory

def calendar(counts,start=dt.date(2026,8,1)):
    weeks=[]
    for i,count in enumerate(counts):
        date=start+dt.timedelta(days=i); wd=(date.weekday()+1)%7
        if not weeks or wd==0: weeks.append({'contributionDays':[]})
        weeks[-1]['contributionDays'].append({'date':date.isoformat(),'weekday':wd,'contributionCount':count})
    return {'weeks':weeks,'totalContributions':sum(counts)}

class RobotArmFactoryTests(unittest.TestCase):
    def test_metrics(self):
        days,m=factory.read_calendar(calendar([0,2,3,0,5,1,4]))
        self.assertEqual(len(days),7); self.assertEqual((m['total'],m['active_days'],m['current_streak'],m['best_day']),(15,5,3,5))
    def test_every_active_day_becomes_one_operation(self):
        svg,state=factory.build_svg(calendar([0,4,1,0,7,2,0]),'Swir','TEST')
        self.assertEqual(state['target_count'],4); self.assertEqual([o['count'] for o in state['operations']],[4,1,7,2])
        self.assertEqual(sum(o['count'] for o in state['operations']),14)
        for o in state['operations']: self.assertIn('id="module-'+o['date']+'"',svg)
    def test_ik_reaches_target(self):
        for tx,ty,bx in [(280,180,240),(310,240,240),(factory.DEPLOY_X,factory.DEPLOY_Y,factory.DEPLOY_BASE_X)]:
            a1,a2=factory.ik(bx,tx,ty)
            x=bx+factory.L1*math.cos(math.radians(a1))+factory.L2*math.cos(math.radians(a1+a2))
            y=factory.BASE_Y+factory.L1*math.sin(math.radians(a1))+factory.L2*math.sin(math.radians(a1+a2))
            self.assertAlmostEqual(x,tx,places=4); self.assertAlmostEqual(y,ty,places=4)
    def test_infinite_motion_contract(self):
        svg,state=factory.build_svg(calendar([1,3,5]),'Swir','TEST')
        self.assertIn('infinite',svg); self.assertIn('ROBOT ARM FACTORY',svg); self.assertIn('PICK → PROCESS → DEPLOY → REPEAT',svg)
        self.assertEqual(state['motion'],'continuous'); self.assertIn('@keyframes carriageMove',svg); self.assertIn('@keyframes beltFlow',svg); self.assertIn('id="carry-0"',svg)
    def test_zero_activity_still_moves(self):
        svg,state=factory.build_svg(calendar([0]*30),'Swir','TEST')
        self.assertEqual(state['target_count'],0); self.assertIn('FACTORY IDLE SWEEP',svg)
    def test_invalid_total_fails(self):
        c=calendar([1,2]); c['totalContributions']=99
        with self.assertRaises(ValueError): factory.read_calendar(c)
    def test_static_has_no_keyframes(self):
        svg,_=factory.build_svg(calendar([1,2,0,4]),'Swir','TEST'); static=factory.build_static_svg(svg)
        self.assertNotIn('@keyframes',static); self.assertIn('STATIC / NO MOTION',static); ET.fromstring(static)
    def test_no_remote_or_script(self):
        svg,_=factory.build_svg(calendar([1,2]),'Swir','TEST'); factory.validate_svg(svg)
        self.assertNotIn('<script',svg); self.assertNotIn('<image',svg); self.assertNotIn('https://',svg)

if __name__=='__main__': unittest.main()
