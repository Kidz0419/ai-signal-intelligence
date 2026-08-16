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

    def test_person_backfill_contract(self):
        root = ROOT / "backfills" / "2026-07-13_to_2026-08-13"
        rows = json.loads((root / "selected.json").read_text())
        self.assertEqual(len(rows), 13)
        self.assertEqual(sum(row["content_type"] == "executive_statement" for row in rows), 3)
        self.assertEqual(sum(row["content_type"] == "practitioner_statement" for row in rows), 10)
        self.assertEqual(len({row["id"] for row in rows}), len(rows))
        self.assertEqual(len({row["canonical_url"].rstrip("/") for row in rows}), len(rows))
        required = {"speaker_name", "speaker_role", "new_information", "evidence_artifact", "evidence_excerpt", "evidence_boundary"}
        self.assertTrue(all(required <= set(row) for row in rows))
        coverage = json.loads((root / "source-coverage.json").read_text())
        self.assertEqual(coverage["selected_counts"], {"total": 13, "model_company_leaders": 3, "practitioner_statements": 10})
        self.assertIn("backfill-2026-07-13-to-2026-08-13.html", self.html)
        self.assertTrue((ROOT / "backfill-2026-07-13-to-2026-08-13.html").exists())

    def test_product_leader_backfill_contract(self):
        root = ROOT / "backfills" / "2026-05-16_to_2026-08-13_product_leaders"
        data = json.loads((root / "candidates.json").read_text())
        rows = data["episodes"]
        self.assertGreaterEqual(len(rows), 1)
        self.assertEqual(data["counts"]["episodes"], len(rows))
        self.assertEqual(len({row["id"] for row in rows}), len(rows))
        self.assertEqual(len({row["url"].rstrip("/") for row in rows}), len(rows))
        required = {
            "speaker_name", "speaker_role", "published_at", "date_evidence",
            "body_evidence_level", "confirmed_topics", "evidence_boundary",
        }
        self.assertTrue(all(required <= set(row) for row in rows))
        self.assertTrue(all(row["decision"] == "backfill_candidate" for row in rows))
        page = "product-leader-backfill-2026-05-16-to-2026-08-13.html"
        self.assertIn(page, self.html)
        self.assertTrue((ROOT / page).exists())

    def test_monthly_signal_backfill_contract(self):
        root = ROOT / "backfills" / "2026-07-16_to_2026-08-14_all_signals"
        rows = json.loads((root / "selected.json").read_text())
        summary = json.loads((root / "run-summary.json").read_text())
        coverage = json.loads((root / "source-coverage.json").read_text())
        self.assertGreaterEqual(len(rows), 33)
        self.assertEqual(summary["counts"]["total"], len(rows))
        self.assertEqual(len({row["id"] for row in rows}), len(rows))
        self.assertEqual(len({(row.get("canonical_url") or row["url"]).rstrip("/") for row in rows}), len(rows))
        self.assertTrue(all("2026-07-16" <= (row.get("event_date") or row["published_at"])[:10] <= "2026-08-14" for row in rows))
        self.assertTrue(all(row.get("evidence_boundary") for row in rows))
        registry = json.loads((ROOT / "config" / "signal-source-registry.json").read_text())
        registered = sum(len(channel.get("sources", [])) + len(channel.get("additional_sources", [])) for channel in registry["channels"])
        self.assertEqual(coverage["counts"]["registered"], registered)
        self.assertEqual(sum(coverage["counts"][key] for key in ("selected", "candidate_only", "checked_no_match", "access_blocked", "auth_required", "mechanical_failure", "not_checked")), registered)
        page = "monthly-signal-2026-07-16-to-2026-08-14.html"
        self.assertIn(page, self.html)
        self.assertTrue((ROOT / page).exists())

    def test_content_topic_studio_contract(self):
        date = self.history["latest_date"]
        data = json.loads((ROOT / "content-topics" / date / "topics.json").read_text())
        topics = data["topics"]
        self.assertEqual(len({row["id"] for row in topics}), len(topics))
        self.assertTrue(all(set(row["platforms"]) == {"xiaohongshu", "twitter", "wechat"} for row in topics))
        daily_ids = {row["id"] for row in json.loads((ROOT / "daily" / date / "selected.json").read_text())}
        self.assertTrue(all(set(row["source_signal_ids"]) <= daily_ids for row in topics))
        self.assertIn("content-topic-studio.html", self.html)
        page = (ROOT / "content-topic-studio.html").read_text()
        self.assertEqual(page.count('class="card"'), 1)  # One JS template renders one card per verified topic.
        self.assertIn("CONTENT TOPIC STUDIO", page)
        if topics:
            self.assertEqual(len(topics) * 3, sum(len(row["platforms"]) for row in topics))


if __name__ == "__main__":
    unittest.main()
