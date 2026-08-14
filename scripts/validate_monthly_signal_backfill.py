#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "backfills/2026-07-16_to_2026-08-14_all_signals"
VALID_LANES = {"model", "agent_architecture", "ai_product", "ai_macro"}
VALID_EVIDENCE = {"confirmed", "primary_statement", "reported", "inferred", "speculative"}


def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main():
    rows = json.loads((DIR / "selected.json").read_text())
    summary = json.loads((DIR / "run-summary.json").read_text())
    if not rows:
        fail("monthly selected is empty")
    ids = [r.get("id") for r in rows]
    urls = [(r.get("canonical_url") or r.get("url") or "").rstrip("/") for r in rows]
    if len(ids) != len(set(ids)):
        fail("duplicate ids")
    if len([u for u in urls if u]) != len(set(u for u in urls if u)):
        fail("duplicate canonical URLs")
    for row in rows:
        day = (row.get("event_date") or row.get("published_at") or "")[:10]
        if not "2026-07-16" <= day <= "2026-08-14":
            fail(f"{row.get('id')}: outside window")
        if row.get("topic_lane") not in VALID_LANES:
            fail(f"{row.get('id')}: invalid topic lane")
        if row.get("evidence_level") not in VALID_EVIDENCE:
            fail(f"{row.get('id')}: invalid evidence")
        for key in ("title", "summary", "why_it_matters_cn", "evidence_boundary", "monthly_origin"):
            if not row.get(key):
                fail(f"{row.get('id')}: missing {key}")
    expected = {"total": len(rows), **{lane: sum(r["topic_lane"] == lane for r in rows) for lane in sorted(VALID_LANES)}}
    if summary.get("counts") != expected:
        fail(f"count mismatch: {summary.get('counts')} != {expected}")
    print(json.dumps({"status": "ok", **expected}, ensure_ascii=False))


if __name__ == "__main__":
    main()
