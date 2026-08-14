#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALID_PLATFORMS = {"xiaohongshu", "twitter", "wechat"}
VALID_STATUS = {"candidate", "selected", "drafting", "published", "archived"}
VALID_TIMELINESS = {"today", "this_week", "this_month", "evergreen"}
VALID_PRIORITY = {"A", "B", "C"}
PLATFORM_REQUIRED = {"title", "hook", "format", "outline", "visual_direction", "cta"}


def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else "2026-08-14"
    path = ROOT / "content-topics" / date / "topics.json"
    data = json.loads(path.read_text())
    topics = data.get("topics", [])
    if not topics:
        fail("empty topics")
    scope = data.get("source_scope", {"type": "daily", "date": date})
    source_path = None
    if scope.get("type") == "daily":
        if data.get("report_date") != date:
            fail("report_date mismatch")
        source_path = ROOT / "daily" / scope.get("date", date) / "selected.json"
    elif scope.get("type") == "monthly_backfill":
        source_path = ROOT / scope["source_path"]
        if not scope.get("start") or not scope.get("end"):
            fail("monthly source scope is incomplete")
    else:
        fail(f"unsupported source scope: {scope.get('type')}")
    assert source_path is not None
    source_signals = {row["id"]: row for row in json.loads(source_path.read_text())}
    ids = [row.get("id") for row in topics]
    if len(ids) != len(set(ids)):
        fail("duplicate topic ids")
    for row in topics:
        required = {"id", "status", "timeliness", "priority", "topic_lane", "source_signal_ids", "working_title_cn", "core_tension_cn", "why_now_cn", "target_audience_cn", "evidence_boundary_cn", "source_urls", "platforms"}
        missing = required - set(row)
        if missing:
            fail(f"{row.get('id')}: missing {sorted(missing)}")
        if row["status"] not in VALID_STATUS or row["timeliness"] not in VALID_TIMELINESS or row["priority"] not in VALID_PRIORITY:
            fail(f"{row['id']}: invalid enum")
        if set(row["platforms"]) != VALID_PLATFORMS:
            fail(f"{row['id']}: platform coverage must be exactly {sorted(VALID_PLATFORMS)}")
        missing_signals = set(row["source_signal_ids"]) - set(source_signals)
        if missing_signals:
            fail(f"{row['id']}: unknown signal ids {sorted(missing_signals)}")
        source_urls = set(row["source_urls"])
        declared_urls = {source_signals[sid].get("canonical_url") or source_signals[sid].get("url") for sid in row["source_signal_ids"]}
        if not source_urls <= declared_urls:
            fail(f"{row['id']}: source URL is not declared by linked signals")
        for platform, variant in row["platforms"].items():
            missing = PLATFORM_REQUIRED - set(variant)
            if missing or not variant["outline"]:
                fail(f"{row['id']}/{platform}: incomplete variant")
    variants = len(topics) * len(VALID_PLATFORMS)
    print(json.dumps({"status": "ok", "scope": date, "source_type": scope["type"], "topics": len(topics), "platform_variants": variants}, ensure_ascii=False))


if __name__ == "__main__":
    main()
