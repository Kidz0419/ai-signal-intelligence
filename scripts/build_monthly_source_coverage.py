#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config/signal-source-registry.json"
OUT_DIR = ROOT / "backfills/2026-07-16_to_2026-08-14_all_signals"
OUT = OUT_DIR / "source-coverage.json"
VALID = {"checked_no_match", "selected", "candidate_only", "access_blocked", "auth_required", "mechanical_failure", "not_checked"}


def main():
    registry = json.loads(REGISTRY.read_text())
    existing = {}
    if OUT.exists():
        old = json.loads(OUT.read_text())
        existing = {x["url"]: x for x in old.get("sources", [])}
    rows = []
    for channel in registry["channels"]:
        sources = channel.get("sources", []) + channel.get("additional_sources", [])
        for src in sources:
            previous = existing.get(src["url"], {})
            status = previous.get("status", "not_checked")
            if status not in VALID:
                raise SystemExit(f"invalid status {status}: {src['url']}")
            rows.append({
                "channel_id": channel["id"],
                "name": src["name"],
                "url": src["url"],
                "source_type": src["type"],
                "status": status,
                "checked_at": previous.get("checked_at"),
                "candidate_count": previous.get("candidate_count", 0),
                "selected_signal_ids": previous.get("selected_signal_ids", []),
                "note": previous.get("note", "尚未完成本窗口定向检查。"),
                "fallback_used": previous.get("fallback_used")
            })
    status_counts = Counter(x["status"] for x in rows)
    channel_counts = {}
    for channel in registry["channels"]:
        batch = [x for x in rows if x["channel_id"] == channel["id"]]
        channel_counts[channel["id"]] = {
            "registered": len(batch),
            **{s: sum(x["status"] == s for x in batch) for s in sorted(VALID)}
        }
    payload = {
        "schema_version": 1,
        "window": {"start": "2026-07-16", "end": "2026-08-14", "timezone": "Asia/Shanghai"},
        "registry_updated_at": registry["updated_at"],
        "counts": {"registered": len(rows), **{s: status_counts[s] for s in sorted(VALID)}},
        "channels": channel_counts,
        "sources": rows,
        "interpretation": "not_checked、access_blocked 或 mechanical_failure 均不能解释为该信源没有高质量新增；candidate_only 也不计入正式 Signal。"
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(payload["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
