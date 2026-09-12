#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-12"
RUN_AT = "2026-09-12T17:46:04+08:00"

SOURCES = [
    {
        "id": 1,
        "title": "Election information and safeguards in 2026",
        "url": "https://openai.com/index/election-safeguards-2026",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
    {
        "id": 2,
        "title": "GPT-6 Astra: The next generation in intelligence for work",
        "url": "https://openai.com/index/gpt-6-astra-next-generation-work",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
    {
        "id": 3,
        "title": "GPT-6 Astra: A new generation of intelligence",
        "url": "https://openai.com/index/gpt-6-astra",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
    {
        "id": 4,
        "title": "Paul Christiano joins OpenAI Foundation Board",
        "url": "https://openai.com/index/paul-christiano-joins-openai-foundation-board",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
]

REVIEWS = [
    {
        "url": SOURCES[0]["url"],
        "decision": "exclude_outside_window",
        "published_at": "2026-05-27",
        "reason": "official article date and body confirm an older policy page; repeated sitemap lastmod changes do not prove a new editorial event",
    },
    {
        "url": SOURCES[1]["url"],
        "decision": "duplicate_existing",
        "signal_id": "2026-09-03-openai-gpt6-astra-broad-release-monitorability",
        "published_at": None,
        "reason": "official body describes the same Astra launch and enterprise controls already reviewed; no standalone first-party publication date or proven new event was recovered",
    },
    {
        "url": SOURCES[2]["url"],
        "decision": "duplicate_existing",
        "signal_id": "2026-09-03-openai-gpt6-astra-broad-release-monitorability",
        "published_at": "2026-09-03",
        "reason": "official launch body belongs to the Astra release already stored under the stable event ID; sitemap lastmod is not a new publication timestamp",
    },
    {
        "url": SOURCES[3]["url"],
        "decision": "exclude_outside_window_below_formal_bar",
        "published_at": "2026-09-09",
        "reason": "official page confirms a board and committee appointment, but no change to committee powers, policy, approval process, or operating controls is disclosed",
    },
]

BRIEF = f'''# AI Signal 日报｜{DATE}

**窗口：** 本轮只复核跨轮新增的 4 个候选；增量发现窗口为北京时间 2026-09-09 08:20 至 2026-09-12 16:20，正式入选仍按真实发布日期、正文增量和事件级去重判断。  
**一句话结论：** 4 个新候选均完成一手正文核验，没有新增正式 Signal。两个 GPT-6 Astra 页面属于 9 月 3 日已入库事件；另外两个页面分别发表于 5 月 27 日和 9 月 9 日，不能用今天的 sitemap `lastmod` 冒充今日事件。[1][2][3]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 两个 Astra 页面并入既有发布事件，不重复建卡 |
| Agent 架构 | 0 | 没有独立的新架构事件 |
| AI 产品 | 0 | Astra 企业控制说明没有可核验的新发布日期或独立上线事件 |
| AI 宏观 | 0 | 两个治理页面均非今日事件，且没有足以单独升级的结构变化 |

## 模型｜0 条

GPT-6 Astra 主发布页与企业工作页正文都可读取。主发布页仍是 9 月 3 日已收录的 Astra 发布主题；企业工作页补充了网站和桌面应用白名单、上传下载、浏览历史、确认策略与自动审查，但页面没有给出可核验的独立发布日期。本轮不把同一发布拆成新卡，也不把 sitemap `lastmod` 当成发布时间。[2][3]

## Agent 架构｜0 条

Astra 页面中的确认策略、自动审查和越权动作监控属于既有发布的控制边界，没有形成新的独立架构事件。[2][3]

## AI 产品｜0 条

企业工作页描述了 ChatGPT Work 与 Codex 的管理员控制，但当前证据只能确认官方页面正文，不能确认这些说明在本轮首次上线或发生了新的产品状态变化。[2]

## AI 宏观｜0 条

Election safeguards 页面标注 2026 年 5 月 27 日；Paul Christiano 加入 OpenAI Foundation Board 和 Safety and Security Committee 的页面标注 9 月 9 日。后者没有披露委员会权力、审批流程或运行控制发生变化，因此不做迟到的宏观治理卡。[1][4]

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新的模型负责人原创内容达到主题与信息增量门槛。

## AI 一线实践者观点｜0 条

本轮没有新的实践者原创内容达到正式入选门槛。

## 审核但未入选

- Election safeguards：正文和页面日期确认是 5 月 27 日旧事件；连续两天出现新的 sitemap `lastmod`，但没有跨轮正文哈希证据证明发生了可报道更新。[1]
- GPT-6 Astra 企业工作页：正文可读，仍围绕同一模型发布；缺少独立 `datePublished`，保持事件合并，不新建卡。[2]
- GPT-6 Astra 主发布页：与历史事件 `2026-09-03-openai-gpt6-astra-broad-release-monitorability` 重复。[3]
- Paul Christiano 任命：官方日期为 9 月 9 日，且正文只确认人事与委员会席位，没有公开新的治理权限或流程。[4]

## 证据边界

- 一手正文通过公开页面提取读取；本机普通 `urllib` 访问四个 OpenAI 页面均返回 HTTP 403，所以 403 仍记录为抓取路径阻断，不解释成无内容。
- Sitemap `lastmod` 只用于变化发现。没有真实发布日期或可证明的正文增量时，不升级为正式 Signal。
- 今日正式 Signal 为 0，因此不派生自媒体选题。

## 飞书短版

**一句话结论：** 本轮 4 个真新增候选已完成正文核验，正式新增 0 条。  
**判断：** 两个 Astra 页面是 9 月 3 日既有事件；Election safeguards 和 Paul Christiano 任命分别是 5 月 27 日与 9 月 9 日旧页面。  
**边界：** sitemap `lastmod` 不等于发布时间，重复更新不制造新卡。  
**结果：** previous_count=0，new_count=0，updated_count=0，total_count=0。

## Sources

[1] {SOURCES[0]["url"]}
[2] {SOURCES[1]["url"]}
[3] {SOURCES[2]["url"]}
[4] {SOURCES[3]["url"]}
'''

TOPICS = {
    "schema_version": 1,
    "report_date": DATE,
    "timezone": "Asia/Shanghai",
    "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。自动流程只生成 candidate，不自动发布。",
    "scope_label_cn": f"当日增量 · {DATE}",
    "source_scope": {"type": "daily", "date": DATE},
    "topics": [],
}


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def update_summary(original: dict) -> dict:
    summary = deepcopy(original)
    summary.update(
        {
            "run_type": "daily_four_lane_incremental_editorial_review",
            "run_at": RUN_AT,
            "deliverable_outcome": "success",
            "scheduler_outcome": "success",
            "editorial_shortlist": 4,
            "reviewed_new_candidates": 4,
            "previous_count": 0,
            "new_count": 0,
            "updated_count": 0,
            "excluded_count": 4,
            "candidate_queue_count": 208,
            "new_in_run_count": 4,
            "unreviewed_candidate_count": 208,
            "total_count": 0,
            "selected": 0,
            "lane_counts": {"model": 0, "agent_architecture": 0, "ai_product": 0, "ai_macro": 0},
            "priority_counts": {"P0": 0, "P1": 0, "P2": 0, "P3": 0},
            "executive_model_longform": 0,
            "practitioner_statements": 0,
            "cross_day_duplicates_removed": 2,
            "candidate_reviews": REVIEWS,
            "content_topics": {"topic_count": 0, "platform_variants": 0},
            "collection_contract": {
                "raw_candidates_in_rolling_window_is_not_increment": True,
                "candidate_queue_count_is_not_new_count": True,
                "sitemap_lastmod_is_not_publication_date": True,
                "feed_titles_require_body_verification": True,
                "http_2xx_is_not_checked_no_match": True,
            },
            "notes": [
                "Only the 4 cross-run new candidates were reviewed; the 208-item standing queue was not rescanned.",
                "All four candidates came from OpenAI sitemap lastmod changes and were opened at the first-party article URL through the available public-text fallback.",
                "The two Astra pages were merged with the existing 2026-09-03 event rather than emitted as duplicate cards.",
                "The election and board-appointment pages retained their first-party May 27 and September 9 dates; sitemap lastmod was not used as event time.",
            ],
        }
    )
    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "OpenAI sitemap":
            probe.update(
                {
                    "status": "candidate_only",
                    "note": "the 4 cross-run lastmod changes were body-reviewed; two were old pages and two belonged to the existing Astra launch event",
                }
            )
    return summary


def main() -> None:
    day = ROOT / "daily" / DATE
    dump(day / "selected.json", [])
    dump(
        day / "citation-ledger.json",
        {
            "version": 1,
            "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
            "sources": SOURCES,
        },
    )
    dump(day / "citations.json", [{"id": s["id"], "url": s["url"]} for s in SOURCES])
    dump(day / "daily-brief.md", BRIEF)
    for name in ("run-summary.json", "collection-run-summary.json"):
        path = day / name
        dump(path, update_summary(json.loads(path.read_text())))
    dump(ROOT / "content-topics" / DATE / "topics.json", TOPICS)
    print(
        json.dumps(
            {
                "date": DATE,
                "reviewed_new_candidates": len(REVIEWS),
                "selected": 0,
                "excluded_or_merged": len(REVIEWS),
                "citations": len(SOURCES),
                "topics": 0,
                "platform_variants": 0,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
