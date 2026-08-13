#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "backfills/2026-07-13_to_2026-08-13"
SUMMARY_DIR = Path.home() / ".hermes/cache/delegation"
SUMMARY_PATHS = [
    SUMMARY_DIR / "subagent-summary-0-20260813_164407_372870.txt",
    SUMMARY_DIR / "subagent-summary-1-20260813_164407_374483.txt",
    SUMMARY_DIR / "subagent-summary-2-20260813_164407_374608.txt",
]


def date_only(value):
    match = re.search(r"2026-\d\d-\d\d", value)
    return match.group(0) if match else "2026-08-13"


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:70]


def lane_for(item):
    text = " ".join([item.get("statement_topic", ""), item.get("lane_value", ""), item.get("title", "")]).lower()
    if any(term in text for term in ["product", "采用", "定价", "用户", "fluency"]):
        return "ai_product"
    if any(term in text for term in ["模型架构", "训练", "推理", "开放权重", "多模态", "robotics", "cyber"]):
        return "model"
    return "agent_architecture"


def scores(lane):
    result = {
        "topic_relevance": 5, "novelty": 4, "technical_or_product_significance": 5,
        "strategic_value": 4, "source_quality": 5, "model_value": 2,
        "agent_architecture_value": 2, "ai_product_value": 2, "macro_value": 2,
        "actionability": 4,
    }
    result[{"model": "model_value", "agent_architecture": "agent_architecture_value", "ai_product": "ai_product_value"}[lane]] = 5
    return result


def normalize_url(value):
    return value.rstrip("/")


def convert(item, content_type):
    date = date_only(item["published_at"])
    lane = "model" if content_type == "executive_statement" else lane_for(item)
    url = item["url"]
    return {
        "id": f"{date}-{slug(item['speaker_name'])}-{slug(item['title'])[:32]}",
        "demo": False,
        "topic_lane": lane,
        "title": item["title"],
        "summary": item["new_information"],
        "decision": "include",
        "confidence": 92,
        "relevance_level": "P1",
        "signal_type": "strategic_radar" if content_type == "executive_statement" else "research",
        "content_type": content_type,
        "information_type": "model_leader_insight" if content_type == "executive_statement" else "practitioner_insight",
        "evidence_level": "primary_statement",
        "source": item.get("organization", item["speaker_name"]),
        "url": url,
        "published_at": date + "T00:00:00+08:00",
        "primary_tags": ["模型大厂负责人" if content_type == "executive_statement" else "AI 一线实践者"],
        "secondary_tags": [],
        "why_it_matters_cn": item.get("lane_value") or item.get("statement_topic", "一线原创增量"),
        "personal_relevance_cn": "用于个人判断模型、Agent 架构或 AI 产品的真实能力边界、工作流与采用价值。",
        "product_opportunity_cn": "将可复用的一线方法转化为产品假设、评测项或运行时设计。",
        "competitive_risk_cn": "若只依赖营销发布或二手报道，可能错过真实失败模式与能力边界。",
        "recommended_action": "investigate",
        "questions_to_validate": ["结论能否在其他模型、产品或部署环境中复现？", "是否有后续数据、代码、独立评测或真实用户结果？"],
        "follow_up_triggers": ["作者发布后续实验、数据或复盘", "第三方复现或反例出现"],
        "scores": scores(lane),
        "report_date": date,
        "event_date": date,
        "canonical_url": url,
        "first_seen_date": "2026-08-13",
        "last_seen_date": "2026-08-13",
        "run_dates": ["2026-08-13"],
        "backfill_window": "2026-07-13_to_2026-08-13",
        "speaker_name": item["speaker_name"],
        "speaker_role": item["speaker_role"],
        "speaker_type": item.get("speaker_type", "model_company_leader"),
        "statement_topic": item.get("statement_topic", item.get("lane_value", "模型")),
        "original_source_url": url,
        "new_information": item["new_information"],
        "evidence_artifact": item.get("evidence_artifact", item["source_type"]),
        "evidence_excerpt": item["evidence_excerpt"],
        "evidence_boundary": item["evidence_boundary"],
    }


def main():
    data = [json.loads(path.read_text()) for path in SUMMARY_PATHS]
    leaders = [data[0]["qualified"][index] for index in (0, 2, 3)]
    # John Ward is a broader AI SaaS commercial postmortem rather than a core model/agent
    # practitioner signal. Vasuman's ratios lack disclosed samples/raw dashboards and the X
    # context cannot yet be systematically audited without OAuth, so keep both outside the
    # formal selected set (they remain preserved in discovered/rejected audit artifacts).
    product = [item for index, item in enumerate(data[1]["qualified"]) if index not in (0, 3)]
    combined = product + data[2]["qualified"]
    practitioners = []
    seen_titles = set()
    seen_urls = set()
    for item in combined:
        title_key = re.sub(r"[^a-z0-9]+", " ", item["title"].lower()).strip()
        url_key = normalize_url(item["url"])
        if title_key in seen_titles or url_key in seen_urls:
            continue
        seen_titles.add(title_key)
        seen_urls.add(url_key)
        practitioners.append(item)
    assert len(leaders) == 3
    assert len(practitioners) == 10, len(practitioners)
    rows = [convert(item, "executive_statement") for item in leaders]
    rows.extend(convert(item, "practitioner_statement") for item in practitioners)
    assert len(rows) == 13
    assert len({row["id"] for row in rows}) == 13
    assert len({normalize_url(row["canonical_url"]) for row in rows}) == 13

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "selected.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    rejected = [item for result in data for item in result["rejected_examples"]]
    all_qualified = [item for result in data for item in result["qualified"]]
    (OUT / "discovered.json").write_text(json.dumps({"qualified_candidates": all_qualified, "rejected_examples": rejected}, ensure_ascii=False, indent=2) + "\n")
    (OUT / "shortlist.json").write_text(json.dumps({"selected_count": 13, "model_company_leaders": leaders, "practitioners": practitioners, "selection_note": "模型负责人仅保留可核验身份和模型增量的 3 条；实践者按规范 URL 与标题双重去重，并排除较泛的 AI SaaS 商业复盘。"}, ensure_ascii=False, indent=2) + "\n")

    ledger = {"sources": [{"id": index, "title": row["title"], "url": row["url"], "source_type": row["content_type"], "evidence_excerpt": row["evidence_excerpt"], "evidence_boundary": row["evidence_boundary"]} for index, row in enumerate(rows, 1)]}
    (OUT / "citation-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    coverage = {
        "window": {"timezone": "Asia/Shanghai", "start": "2026-07-13T00:00:00+08:00", "end": "2026-08-13T17:00:00+08:00"},
        "conclusion": "此前两个 0 条存在明显信源不足导致的假阴性；补充个人博客、GitHub、完整访谈与公开 X Article 后核验出 13 条合格原创内容。",
        "selected_counts": {"total": 13, "model_company_leaders": 3, "practitioner_statements": 10},
        "coverage_gaps": [
            {"channel": "X official API", "status": "xurl installed; no app/OAuth configured", "impact": "无法系统检索全部公开长帖和 X Articles。", "alternative": "个人博客、GitHub、官方站点及可公开访问的 X 页面。"},
            {"channel": "YouTube transcripts", "status": "runtime IP blocked by transcript API", "impact": "无正文的访谈不能凭标题正式入库。", "alternative": "发布者文字稿、博客整理和官方描述。"},
            {"channel": "Chinese closed platforms", "status": "partial", "impact": "微信公众号、视频号与登录墙内访谈覆盖不完整。", "alternative": "公司官网、公开演讲页和可访问原文。"},
        ],
        "enabled_sources": ["模型公司官方博客/Research/站点地图", "个人博客与 RSS", "GitHub 原始长文/实验/发布", "完整访谈与播客发现", "公开 X Article"],
        "rejected_policy": "正文不可读、身份不可核验、只有标题/营销、时间不在窗口或无原创增量者不入库。",
    }
    (OUT / "source-coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# AI Signal 人物信源审计与近一个月回溯", "", "> 个人独立 AI 情报工具；不代表任何公司或机构。", "",
        "**窗口：** 2026-07-13 00:00—2026-08-13 17:00（Asia/Shanghai）  ",
        "**结论：** 此前‘模型大厂高管 0 / 一线实践者 0’存在明显信源不足。补充人物一手源后，本轮正式核验 **13 条**。", "",
        "## 入库概览", "", "- 模型大厂高管/模型负责人：**3 条**", "- AI 一线实践者：**10 条**",
        "- 不按知名度补数；Anthropic 多 Agent 研究已在 8 月 13 日日报，不重复入库。", "", "## 正式入库", "",
    ]
    for index, row in enumerate(rows, 1):
        lines.extend([f"### {index}. {row['title']}", f"- **日期 / 主线 / 人物：** {row['event_date']}｜{row['topic_lane']}｜{row['speaker_name']}", f"- **核心增量：** {row['new_information']}", f"- **证据边界：** {row['evidence_boundary']}", f"- **来源：** [{index}]", ""])
    lines.extend(["## 信源审计结论", "", "1. 旧流程过度依赖新闻/RSS/官方发布索引，容易漏掉个人博客、GitHub 长文、播客/演讲和 X Article。", "2. `xurl` 已安装，但无用户应用/OAuth；系统仍不能自动检索 X。授权可拒绝，其他公开源会继续运行。", "3. YouTube Transcript API 对当前运行环境 IP 阻断；没有正文的访谈只留候选，不凭标题补写。", "4. 中文封闭平台和登录墙仍是主要盲区。", "", "## Sources", ""])
    lines.extend(f"[{item['id']}] {item['url']}" for item in ledger["sources"])
    (OUT / "backfill-report.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"selected": 13, "executive": 3, "practitioner": 10, "rejected": len(rejected)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
