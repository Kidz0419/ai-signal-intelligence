#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "2026-07-16"
END = "2026-08-14"
OUT = ROOT / "backfills" / f"{START}_to_{END}_all_signals"


def day(row):
    return (row.get("event_date") or row.get("published_at") or "")[:10]


def url(row):
    return (row.get("canonical_url") or row.get("url") or "").rstrip("/")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--additions", default=str(OUT / "curated-additions.json"))
    args = parser.parse_args()
    history = json.loads((ROOT / "data/history.json").read_text())["signals"]
    people = json.loads((ROOT / "backfills/2026-07-13_to_2026-08-13/selected.json").read_text())
    additions_path = Path(args.additions)
    additions = json.loads(additions_path.read_text()) if additions_path.exists() else []
    rows_by_id = {}
    id_by_url = {}
    for origin, batch in (("daily_history", history), ("person_original_backfill", people), ("curated_monthly_addition", additions)):
        for source in batch:
            if not START <= day(source) <= END:
                continue
            item = dict(source)
            item["monthly_backfill_window"] = f"{START}_to_{END}"
            item["monthly_origin"] = origin
            if not item.get("evidence_boundary"):
                item["evidence_boundary"] = (
                    f"原日报将本条标记为 {item.get('evidence_level', 'unknown')}，但旧数据合同未单列证据边界；"
                    "月度回溯正式发布前必须重新核验一手 URL、开放范围及厂商自报数据，当前不得据此扩写。"
                )
                item["monthly_review_status"] = "pending_evidence_reverification"
            else:
                item["monthly_review_status"] = "baseline_evidence_present"
            canonical = url(item)
            existing_id = item["id"] if item["id"] in rows_by_id else id_by_url.get(canonical)
            if existing_id and origin != "curated_monthly_addition":
                continue
            if existing_id:
                old = rows_by_id.pop(existing_id)
                old_url = url(old)
                if old_url:
                    id_by_url.pop(old_url, None)
            rows_by_id[item["id"]] = item
            if canonical:
                id_by_url[canonical] = item["id"]
    rows = list(rows_by_id.values())
    rows.sort(key=lambda r: (day(r), r.get("topic_lane", ""), r.get("title", "")))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "selected.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    counts = Counter(r["topic_lane"] for r in rows)
    summary = {
        "window": {"start": START, "end": END, "timezone": "Asia/Shanghai", "kind": "rolling_30_calendar_days_inclusive"},
        "counts": {"total": len(rows), **{lane: counts[lane] for lane in ("model", "agent_architecture", "ai_product", "ai_macro")}},
        "origins": dict(Counter(r["monthly_origin"] for r in rows)),
        "note": "产品负责人日期确认候选不自动进入正式 selected；只有满足 FILTER_RULES_AI_V1.md 正文与信息增量门槛的内容才加入。"
    }
    (OUT / "run-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
