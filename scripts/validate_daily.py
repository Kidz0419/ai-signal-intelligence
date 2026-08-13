#!/usr/bin/env python3
"""Strictly validate immutable daily artifacts and grounded citations."""
import argparse
import json
import re
from pathlib import Path

LANES = {"model", "agent_architecture", "ai_product", "ai_macro"}
SCORE_KEYS = {
    "topic_relevance", "novelty", "technical_or_product_significance",
    "strategic_value", "source_quality", "model_value",
    "agent_architecture_value", "ai_product_value", "macro_value", "actionability",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    day = args.root / "daily" / args.date
    rows = json.loads((day / "selected.json").read_text())
    citations = json.loads((day / "citations.json").read_text())
    ledger = json.loads((day / "citation-ledger.json").read_text())
    brief = (day / "daily-brief.md").read_text()
    assert isinstance(rows, list)
    ids, urls = set(), set()
    for row in rows:
        assert row["id"] not in ids; ids.add(row["id"])
        assert row["topic_lane"] in LANES
        assert row["decision"] in {"include", "watchlist"}
        assert row["relevance_level"] in {"P0", "P1", "P2", "P3"}
        assert row["signal_type"] and row["content_type"] and row["information_type"] and row["evidence_level"]
        assert SCORE_KEYS == set(row["scores"])
        assert all(isinstance(v, int) and 0 <= v <= 5 for v in row["scores"].values())
        assert max(row["scores"][k] for k in ("model_value", "agent_architecture_value", "ai_product_value", "macro_value")) >= 4
        assert row["canonical_url"] not in urls; urls.add(row["canonical_url"])
        for key in ("summary", "why_it_matters_cn", "personal_relevance_cn", "product_opportunity_cn", "competitive_risk_cn", "recommended_action", "questions_to_validate", "follow_up_triggers"):
            assert row.get(key), (row["id"], key)
    simple = [{"id": s["id"], "url": s["url"]} for s in ledger["sources"]]
    assert citations == simple
    cited = sorted({int(x) for x in re.findall(r"\[(\d+)\]", brief)})
    declared = [s["id"] for s in ledger["sources"]]
    assert cited == declared
    source_lines = re.findall(r"^\[(\d+)\] (https?://\S+)$", brief, re.M)
    assert source_lines == [(str(s["id"]), s["url"]) for s in ledger["sources"]]
    # The first historical brief predates the four-lane presentation; preserve it as an immutable archive.
    if args.date >= "2026-08-13":
        for heading in ("模型｜", "Agent 架构｜", "AI 产品｜", "AI 宏观｜", "模型大厂高管模型长文 / 访谈"):
            assert heading in brief
    # New briefs must expose the practitioner lane; historical briefs remain immutable.
    if args.date >= "2026-08-14":
        assert "AI 一线实践者观点" in brief
    practitioner_rows = [r for r in rows if r["content_type"] == "practitioner_statement"]
    for row in practitioner_rows:
        for key in ("speaker_name", "speaker_role", "speaker_type", "statement_topic", "original_source_url", "new_information", "evidence_artifact"):
            assert row.get(key), (row["id"], key)
        assert row["speaker_type"] in {"ai_product_leader", "ai_developer", "open_source_maintainer", "independent_researcher"}
    print(json.dumps({"date": args.date, "signals": len(rows), "citations": len(declared), "status": "strict-ok"}, ensure_ascii=False))


if __name__ == "__main__":
    main()