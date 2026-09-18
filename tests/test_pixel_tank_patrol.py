"""Deterministic synthetic fixtures: never used as published profile activity."""
import datetime as dt
import math
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import generate_pixel_tank_patrol as tank


def calendar(counts, start=dt.date(2026, 8, 1)):
    weeks = []
    for i, count in enumerate(counts):
        date = start+dt.timedelta(days=i)
        weekday = (date.weekday()+1) % 7
        if not weeks or weekday == 0:
            weeks.append({'contributionDays': []})
        weeks[-1]['contributionDays'].append({'date': date.isoformat(), 'weekday': weekday,
                                              'contributionCount': count})
    return {'weeks': weeks, 'totalContributions': sum(counts)}


class PixelTankTests(unittest.TestCase):
    def test_exact_metrics(self):
        days, m = tank.read_calendar(calendar([0, 2, 3, 0, 5, 1, 4]))
        self.assertEqual(len(days), 7)
        self.assertEqual([m[k] for k in ('total','active_days','current_streak','best_day')], [15, 5, 3, 5])

    def test_today_incomplete_yesterday_streak(self):
        self.assertEqual(tank.read_calendar(calendar([2, 3, 0]))[1]['current_streak'], 2)

    def test_old_streak_is_not_current(self):
        self.assertEqual(tank.read_calendar(calendar([2, 3, 0, 0]))[1]['current_streak'], 0)

    def test_every_active_day_exactly_one_target(self):
        days, _ = tank.read_calendar(calendar([0, 4, 1, 0, 999, 2, 0]))
        shots = tank.plan_shots(days)
        self.assertEqual([s.day.date for s in shots], [d.date for d in days if d.count])
        self.assertEqual(sum(s.day.count for s in shots), sum(d.count for d in days))
        self.assertEqual(len({s.day.date for s in shots}), len(shots))

    def test_muzzle_and_target_are_on_the_aimed_ray(self):
        days, _ = tank.read_calendar(calendar([i % 11 for i in range(365)]))
        for s in tank.plan_shots(days):
            dx, dy = s.day.x-s.tank_x, s.day.y-tank.TANK_Y
            self.assertAlmostEqual(math.atan2(dy, dx), math.radians(s.angle))
            self.assertAlmostEqual(math.hypot(s.muzzle_x-s.tank_x, s.muzzle_y-tank.TANK_Y), 46)
            self.assertAlmostEqual((s.muzzle_x-s.tank_x)*dy-(s.muzzle_y-tank.TANK_Y)*dx, 0)
            self.assertLess(s.fire, s.hit)
            self.assertLess(s.hit+.3, (s.index+1)*tank.SLOT)

    def test_partial_first_week_coordinates(self):
        days, _ = tank.read_calendar(calendar([1, 2, 3]))
        self.assertEqual([(d.week, d.weekday) for d in days], [(0, 6), (1, 0), (1, 1)])
        self.assertEqual(days[0].y, tank.GY+6*tank.DY+tank.CELL/2)

    def test_empty_weeks_fail(self):
        with self.assertRaises(ValueError):
            tank.read_calendar({'weeks': [], 'totalContributions': 0})

    def test_incorrect_total_fails(self):
        c = calendar([1, 2]); c['totalContributions'] = 100
        with self.assertRaises(ValueError):
            tank.read_calendar(c)

    def test_negative_count_fails(self):
        with self.assertRaises(ValueError):
            tank.read_calendar(calendar([2, -1]))

    def test_duplicate_or_gap_fails(self):
        c = calendar([1, 2, 3])
        c['weeks'][1]['contributionDays'][1] = c['weeks'][1]['contributionDays'][0]
        with self.assertRaises(ValueError):
            tank.read_calendar(c)

    def test_weekday_mismatch_fails(self):
        c = calendar([1]); c['weeks'][0]['contributionDays'][0]['weekday'] = 0
        with self.assertRaises(ValueError):
            tank.read_calendar(c)

    def test_zero_days_no_fake_shots_still_patrols(self):
        svg, state = tank.build_svg(calendar([0]*365), 'Swir', 'TEST ONLY')
        self.assertEqual(state['target_count'], 0)
        self.assertNotIn('id="shell-', svg)
        self.assertIn('NO ACTIVE DAYS', svg)
        self.assertIn('animation:drive 6s linear infinite', svg)

    def test_full_year_size_and_target_metadata(self):
        svg, state = tank.build_svg(calendar([2]*365), 'Swir', 'TEST ONLY')
        self.assertLess(len(svg.encode()), 1_500_000)
        self.assertEqual(state['target_count'], 365)
        root = ET.fromstring(svg)
        cells = [e for e in root.iter() if e.get('data-date')]
        self.assertEqual(len(cells), 365)
        self.assertEqual(sum(int(e.get('data-count')) for e in cells), 730)

    def test_deterministic_rendering(self):
        c = calendar([1, 9, 5])
        self.assertEqual(tank.build_svg(c, 'Swir', 'TEST'), tank.build_svg(c, 'Swir', 'TEST'))

    def test_xml_escaping_and_unsafe_login(self):
        svg, _ = tank.build_svg(calendar([2]), 'Swir', 'TEST & "ONLY" <not live>')
        ET.fromstring(svg)
        self.assertIn('&amp;', svg)
        with self.assertRaises(ValueError):
            tank.build_svg(calendar([2]), '<script>', 'TEST')

    def test_infinite_animation_and_motion_preference(self):
        svg, _ = tank.build_svg(calendar([1, 9, 5]), 'Swir', 'TEST')
        self.assertIn('animation-iteration-count:infinite', svg)
        self.assertIn('prefers-reduced-motion:reduce', svg)
        self.assertNotIn('animation-play-state:paused', svg)
        self.assertNotIn(':hover', svg)
        self.assertIn('@keyframes shell0', svg)
        self.assertIn('@keyframes cell0', svg)
        self.assertIn('@keyframes hit0', svg)

    def test_no_scripts_external_assets_events_or_dtd(self):
        for payload in ['<script/>', '<image href="https://example.org/a.png"/>',
                        '<rect onclick="alert(1)"/>', '<use href="https://example.org/#x"/>',
                        '<style>@import "https://example.org/font.css";</style>']:
            with self.assertRaises(ValueError):
                tank.validate_svg('<svg xmlns="http://www.w3.org/2000/svg">'+payload+'</svg>')
        with self.assertRaises(ValueError):
            tank.validate_svg('<!DOCTYPE svg><svg xmlns="http://www.w3.org/2000/svg"/>')

    def test_missing_token_is_failure(self):
        fake_legacy = mock.Mock()
        with mock.patch.dict(sys.modules, {'generate_profile_activity': fake_legacy}), mock.patch.dict('os.environ', {'GITHUB_TOKEN': ''}):
            self.assertEqual(tank.main(), 1)
        fake_legacy.fetch_calendar.assert_not_called()

    def test_stage_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tank.publish_outputs(root, {Path('assets/a.svg'): '<svg/>', Path('assets/b.json'): '{}'})
            self.assertEqual((root/'assets/a.svg').read_text(), '<svg/>')
            self.assertEqual((root/'assets/b.json').read_text(), '{}')
            self.assertFalse(list(root.glob('.tank-stage-*')))


if __name__ == '__main__':
    unittest.main()
