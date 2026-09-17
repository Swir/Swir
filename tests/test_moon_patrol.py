"""Offline regression checks; fixtures are synthetic and never published."""
import datetime as dt
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from generate_moon_patrol import build_patrol, metrics_for, validate_svg


def calendar(counts):
    first = dt.date(2026, 8, 1)
    days = [{"date": (first + dt.timedelta(days=i)).isoformat(), "contributionCount": n,
             "weekday": (first + dt.timedelta(days=i)).isoweekday() % 7} for i, n in enumerate(counts)]
    return {"totalContributions": sum(counts),
            "weeks": [{"contributionDays": days[i:i+7]} for i in range(0, len(days), 7)]}


class MoonPatrolTests(unittest.TestCase):
    def test_counters_and_streak(self):
        _, weekly, m = metrics_for(calendar([0, 2, 3, 0, 5, 1, 4]))
        self.assertEqual(weekly, [15])
        self.assertEqual(m, {"total": 15, "active_days": 5, "current_streak": 3, "best_day": 5})

    def test_today_may_be_incomplete(self):
        self.assertEqual(metrics_for(calendar([2, 3, 0]))[2]["current_streak"], 2)

    def test_old_streak_is_not_current(self):
        self.assertEqual(metrics_for(calendar([2, 3, 0, 0]))[2]["current_streak"], 0)

    def test_zero_contributions(self):
        c = calendar([0] * 365)
        validate_svg(build_patrol(c, "Swir", "TEST DATA"))
        self.assertEqual(metrics_for(c)[2]["best_day"], 0)

    def test_missing_calendar_fails(self):
        with self.assertRaises(ValueError):
            metrics_for({"weeks": [], "totalContributions": 0})

    def test_wrong_total_fails(self):
        c = calendar([1, 2, 3])
        c["totalContributions"] = 10
        with self.assertRaises(ValueError):
            metrics_for(c)

    def test_duplicate_date_fails(self):
        c = calendar([1, 2])
        c["weeks"][0]["contributionDays"][1]["date"] = c["weeks"][0]["contributionDays"][0]["date"]
        with self.assertRaises(ValueError):
            metrics_for(c)

    def test_xml_escaping_and_safe_local_references(self):
        svg = build_patrol(calendar([1, 2]), '<Swir & "test">', 'TEST & "ONLY"')
        validate_svg(svg)
        root = ET.fromstring(svg)
        ids = {e.get("id") for e in root.iter() if e.get("id")}
        for e in root.iter():
            if "href" in e.attrib:
                self.assertIn(e.get("href")[1:], ids)
        self.assertIn('&lt;Swir &amp;', svg)

    def test_animation_and_accessibility_contract(self):
        svg = build_patrol(calendar([0, 2, 7]), "Swir", "TEST DATA")
        for expected in ['@keyframes scroll', '@keyframes spin', '@keyframes jump',
                         'prefers-reduced-motion:reduce', 'animation:none!important',
                         'viewBox="0 0 960 368"', 'BLUE COLUMNS = WEEKLY CONTRIBUTIONS']:
            self.assertIn(expected, svg)
        self.assertLess(len(svg.encode()), 180_000)

    def test_deterministic_rendering(self):
        c = calendar([1, 2, 4, 8, 16])
        self.assertEqual(build_patrol(c, "Swir", "TEST"), build_patrol(c, "Swir", "TEST"))

    def test_disallow_scripts_and_remote_resources(self):
        for payload in ['<script/>', '<image href="https://example.org/a.png"/>',
                        '<rect onclick="alert(1)"/>', '<use href="https://example.org/#x"/>']:
            with self.assertRaises(ValueError):
                validate_svg('<svg xmlns="http://www.w3.org/2000/svg">'+payload+'</svg>')


if __name__ == "__main__":
    unittest.main()
