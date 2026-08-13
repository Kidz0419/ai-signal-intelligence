#!/usr/bin/env python3
import json
import re
import unittest
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value.lower()).strip()


class DailyHistoryContractTest(unittest.TestCase):
    def setUp(self):
        self.history = json.loads((ROOT / "data/history.json").read_text())
        self.html = (ROOT / "index.html").read_text()

    def test_contains_initial_daily_bucket(self):
        dates = [day["date"] for day in self.history["days"]]
        selected_dates = sorted(
            p.parent.name for p in (ROOT / "daily").glob("*/selected.json")
        )
        self.assertEqual(sorted(dates), selected_dates)
        self.assertEqual(self.history["latest_date"], max(selected_dates))

    def test_latest_day_has_four_lane_contract(self):
        latest = json.loads((ROOT / "data/latest.json").read_text())
        valid = {"model", "agent_architecture", "ai_product", "ai_macro"}
        self.assertTrue(all(row.get("topic_lane") in valid for row in latest))
        self.assertIn("四主线重点", (ROOT / "daily" / self.history["latest_date"] / "daily-brief.md").read_text())

    def test_event_ids_and_canonical_urls_are_unique_across_days(self):
        signals = self.history["signals"]
        ids = [s["id"] for s in signals]
        self.assertEqual(len(ids), len(set(ids)))
        urls = [s["canonical_url"] for s in signals if s.get("canonical_url")]
        self.assertEqual(len(urls), len(set(urls)))

    def test_near_duplicate_titles_do_not_cross_days(self):
        signals = self.history["signals"]
        for i, left in enumerate(signals):
            for right in signals[i + 1:]:
                if left["report_date"] == right["report_date"]:
                    continue
                ratio = SequenceMatcher(None, normalized_title(left["title"]), normalized_title(right["title"])).ratio()
                self.assertLess(ratio, 0.92, (left["id"], right["id"], ratio))

    def test_each_signal_points_to_a_declared_day(self):
        days = {d["date"] for d in self.history["days"]}
        for signal in self.history["signals"]:
            self.assertIn(signal["report_date"], days)
            self.assertFalse(signal.get("demo", True))

    def test_day_view_contract_is_present(self):
        self.assertIn('data/history.js', self.html)
        self.assertIn('data-view="daily"', self.html)
        self.assertIn('id="dayPicker"', self.html)
        self.assertIn('window.DAILY_HISTORY', (ROOT / "data/history.js").read_text())


if __name__ == "__main__":
    unittest.main()
