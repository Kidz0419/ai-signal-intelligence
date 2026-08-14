#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Idempotently register primary sources discovered during the monthly backfill."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "config/signal-source-registry.json"
ADDITIONS = {
    "frontier_model_official": [
        {"name": "NVIDIA Newsroom", "url": "https://nvidianews.nvidia.com/", "type": "official_newsroom"},
        {"name": "AMD Newsroom", "url": "https://newsroom.amd.com/", "type": "official_newsroom"},
        {"name": "Meta Newsroom AI", "url": "https://about.fb.com/news/tag/ai/", "type": "official_newsroom"},
    ],
    "china_frontier_models": [
        {"name": "Moonshot AI Kimi GitHub", "url": "https://github.com/MoonshotAI/Kimi-K3", "type": "official_github"},
    ],
}

data = json.loads(PATH.read_text())
added = 0
for channel in data["channels"]:
    wanted = ADDITIONS.get(channel["id"], [])
    if not wanted:
        continue
    existing = {x["url"] for x in channel.get("sources", []) + channel.get("additional_sources", [])}
    target = channel.setdefault("additional_sources", [])
    for item in wanted:
        if item["url"] not in existing:
            target.append(item)
            existing.add(item["url"])
            added += 1
data["updated_at"] = "2026-08-14T16:30:00+08:00"
PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"added": added, "registered_total": sum(len(c.get('sources', [])) + len(c.get('additional_sources', [])) for c in data['channels'])}, ensure_ascii=False))
