#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "backfills/2026-05-16_to_2026-08-13_product_leaders/candidates.json"
REQUIRED = {
    "id", "decision", "window", "organization", "speaker_name", "speaker_role",
    "speaker_type", "title", "published_at", "source_name", "url", "content_format",
    "date_evidence", "body_evidence_level", "confirmed_topics", "evidence_boundary",
    "related_sources", "topic_cluster",
}
VALID_WINDOWS = {"main_90d", "adjacent_90_120d"}
VALID_BODY = {"title_only", "show_notes", "chapters", "transcript", "full_text", "demo"}


def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main():
    data = json.loads(DATA.read_text())
    rows = data.get("episodes", [])
    if not rows:
        fail("episodes is empty")
    ids = [row.get("id") for row in rows]
    urls = [row.get("url", "").rstrip("/") for row in rows]
    if len(ids) != len(set(ids)):
        fail("duplicate ids")
    if len(urls) != len(set(urls)):
        fail("duplicate canonical episode URLs")
    for row in rows:
        missing = REQUIRED - set(row)
        if missing:
            fail(f"{row.get('id')}: missing {sorted(missing)}")
        if row["decision"] != "backfill_candidate":
            fail(f"{row['id']}: invalid decision")
        if row["window"] not in VALID_WINDOWS:
            fail(f"{row['id']}: invalid window")
        if row["body_evidence_level"] not in VALID_BODY:
            fail(f"{row['id']}: invalid body evidence")
        date = datetime.fromisoformat(row["published_at"].replace("Z", "+00:00"))
        day = date.date().isoformat()
        if row["window"] == "main_90d" and not ("2026-05-16" <= day <= "2026-08-13"):
            fail(f"{row['id']}: outside main window")
        if row["window"] == "adjacent_90_120d" and not ("2026-04-16" <= day <= "2026-05-15"):
            fail(f"{row['id']}: outside adjacent window")
        if not row["date_evidence"] or not row["confirmed_topics"]:
            fail(f"{row['id']}: missing date evidence or topics")
        if row["body_evidence_level"] == "title_only" and any(len(x) > 180 for x in row["confirmed_topics"]):
            fail(f"{row['id']}: title-only topic is over-expanded")
    counts = data.get("counts", {})
    expected = {
        "episodes": len(rows),
        "main_90d": sum(r["window"] == "main_90d" for r in rows),
        "adjacent_90_120d": sum(r["window"] == "adjacent_90_120d" for r in rows),
        "people": len({r["speaker_name"] for r in rows}),
        "organizations": len({r["organization"] for r in rows}),
    }
    if counts != expected:
        fail(f"counts mismatch: expected {expected}, got {counts}")
    print(json.dumps({"status": "ok", **expected}, ensure_ascii=False))


if __name__ == "__main__":
    main()
