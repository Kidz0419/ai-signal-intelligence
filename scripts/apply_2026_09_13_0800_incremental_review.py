#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-13"
RUN_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")

NEW_SOURCES = [
    {
        "id": 6,
        "title": "Research acceleration: The view inside OpenAI",
        "url": "https://openai.com/index/research-acceleration-view-inside-openai",
        "publisher": "OpenAI",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT,
    },
    {
        "id": 7,
        "title": "Introducing ChatGPT Images 2.5",
        "url": "https://openai.com/index/introducing-chatgpt-images-2-5",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
    {
        "id": 8,
        "title": "Sighting: California Brown Pelican",
        "url": "https://simonwillison.net/2026/Sep/12/sighting-399708714",
        "publisher": "Simon Willison",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
]

NEW_REVIEWS = [
    {
        "url": "https://openai.com/index/research-acceleration-view-inside-openai/",
        "decision": "duplicate_existing_no_material_update",
        "signal_id": "2026-09-06-openai-automated-research-intern-rsi-controls",
        "published_at": "2026-09-06T08:00:00Z",
        "reason": "the first-party body still contains the same automated-research-intern milestone, internal usage metrics, human-intervention limit, and pacing controls already captured on September 10; the new sitemap lastmod adds no new evidence or status change",
    },
    {
        "url": "https://openai.com/index/two-blind-brothers/",
        "decision": "duplicate_same_day_review_no_material_update",
        "published_at": None,
        "reason": "the accessible first-party body is unchanged in editorial substance from the same-day review: it remains an accessibility customer story without a product release, new interface, control boundary, measured result, or resolvable publication date",
    },
    {
        "url": "https://openai.com/index/introducing-chatgpt-images-2-5/",
        "decision": "duplicate_existing_no_material_update",
        "signal_id": "2026-09-08-openai-chatgpt-images-2-5",
        "published_at": "2026-09-08T11:30:00Z",
        "reason": "the first-party body still describes the September 8 Images 2.5 release, Sketch, templates, image comments, prompt sharing, and the Flare and Sunburst API models already captured on September 10; another sitemap lastmod is not a new launch",
    },
    {
        "url": "https://simonwillison.net/2026/Sep/12/sighting-399708714/",
        "decision": "exclude_out_of_scope",
        "published_at": "2026-09-12T21:16:09Z",
        "reason": "the first-party page is a California Brown Pelican sighting and contains no information about models, agent architecture, AI products, AI industry structure, or practitioner AI work",
    },
]

BRIEF = '''# AI Signal 日报｜2026-09-13

**窗口：** 本轮发现窗口为北京时间 2026-09-10 00:00 至 2026-09-13 08:00，只审核 4 个跨轮新增候选；当天累计审核 9 个候选。  
**一句话结论：** 本轮没有新 Signal。两篇 OpenAI 页面早已入库，Two Blind Brothers 是同日重复出现的客户案例，Simon Willison 新条目与 AI 无关。[2][6][7][8]

## 四主线重点

| 主线 | 数量 | 本轮判断 |
|---|---:|---|
| 模型 | 0 | Images 2.5 仍是 9 月 8 日已入库版本，没有新的能力或上线状态 |
| Agent 架构 | 0 | 自动化研究实习生材料仍是 9 月 6 日原事件，没有新的控制或评测证据 |
| AI 产品 | 0 | Two Blind Brothers 仍是使用案例，没有新界面、工作流或权限边界 |
| AI 宏观 | 0 | 没有产业结构、治理或采用变化 |

## 模型｜0 条

ChatGPT Images 2.5 正文仍标注 9 月 8 日，内容与 9 月 10 日入库记录一致：Sketch、模板、图片评论、提示词分享，以及 Flare 和 Sunburst 两个 API 模型。本轮 `lastmod` 变化没有带来新模型、价格、开放范围或独立评测。[7]

## Agent 架构｜0 条

OpenAI 的研究加速报告仍是 9 月 6 日事件。自动化研究实习生目标、3.1 个 Agent 工作日，以及 4–8 小时成功任务中超过一半需要人工介入，均已收入 `2026-09-06-openai-automated-research-intern-rsi-controls`；正文没有出现新的权限、暂停、恢复、日志或外部评测证据。[6]

## AI 产品｜0 条

Two Blind Brothers 页面仍在描述视觉理解、语音导航、表格分析和邮箱连接等无障碍用法。它没有宣布新功能，也没有真实 UI、权限字段、执行日志或量化效果；正文依然没有可核验的发布日期。[2]

## AI 宏观｜0 条

本轮没有新的治理、资本、算力、监管或产业结构变化。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有模型负责人关于模型能力、训练、评测或路线的新原创内容。OpenAI 研究加速报告已有正式事件卡，本次页面修改没有带来新的负责人判断。[6]

## AI 一线实践者观点｜0 条

Simon Willison 新页面记录的是 California Brown Pelican 目击和 Pacifica Pier 近况，与 AI 构建、部署、评测或产品实践无关。[8]

## 本轮审核但未入选

- OpenAI 研究加速报告：`duplicate_existing_no_material_update`。正文日期和核心内容未形成新事件，继续归入 9 月 6 日原 Signal。[6]
- Two Blind Brothers：`duplicate_same_day_review_no_material_update`。同一天再次出现 sitemap 修改，正文仍未达到产品 Signal 门槛。[2]
- ChatGPT Images 2.5：`duplicate_existing_no_material_update`。正文仍是 9 月 8 日发布内容，继续归入原 Signal。[7]
- California Brown Pelican：`exclude_out_of_scope`。页面内容与 AI Signal 四条主线无关。[8]

## 当天此前审核但未入选

- Paul Christiano 任命没有附带治理权力或审批流程变化。[1]
- Claude Code v2.1.270 只是只读 Git 命令误触发权限询问的回归修复。[3]
- Legora 页面是已入库 Astra 事件的旧案例页再次更新 `lastmod`。[4]
- Paul Ford 条目只有一段二手引文，没有可核验的构建或评测增量。[5]

## 证据边界

- OpenAI 普通请求对部分页面返回 403；本轮通过可读正文 fallback 核验，没有把阻断当成无内容。
- 研究加速报告和 Images 2.5 的发布日期沿用此前由 OpenAI 官方 RSS 核验的时间；本轮 sitemap `lastmod` 只用于发现。[6][7]
- Two Blind Brothers 正文仍未暴露 `datePublished`，因此保持日期未确认。[2]
- 本轮只审核 `new_in_run_count=4` 的候选，没有重扫 335 条滚动窗口记录，也没有重审完整待审队列。

## 飞书短版

**一句话结论：** 本轮 4 个真新增候选完成正文核验，正式 Signal 仍为 0。  
**判断：** OpenAI 研究加速报告与 Images 2.5 都是已入库页面的再次修改；Two Blind Brothers 是同日重复客户案例；Simon Willison 新条目与 AI 无关。[2][6][7][8]  
**证据边界：** sitemap `lastmod` 不当发布日期，旧事件没有实质证据升级。  
**结果：** previous_count=0，new_count=0，updated_count=0，total_count=0。

## Sources

[1] https://openai.com/index/paul-christiano-joins-openai-foundation-board
[2] https://openai.com/index/two-blind-brothers
[3] https://github.com/anthropics/claude-code/releases/tag/v2.1.270
[4] https://openai.com/index/legora-financial-statement-review-with-astra
[5] https://simonwillison.net/2026/Sep/12/paul-ford
[6] https://openai.com/index/research-acceleration-view-inside-openai
[7] https://openai.com/index/introducing-chatgpt-images-2-5
[8] https://simonwillison.net/2026/Sep/12/sighting-399708714
'''


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    day = ROOT / "daily" / DATE
    prior_summary = json.loads((day / "run-summary.json").read_text())
    collection = json.loads((day / "collection-run-summary.json").read_text())
    prior_sources = json.loads((day / "citation-ledger.json").read_text())["sources"]
    prior_reviews = prior_summary.get("candidate_reviews", [])
    sources = prior_sources + NEW_SOURCES
    reviews = prior_reviews + NEW_REVIEWS

    summary = deepcopy(collection)
    summary.update(
        {
            "run_type": "daily_four_lane_incremental_editorial_review",
            "run_at": RUN_AT,
            "deliverable_outcome": "success",
            "scheduler_outcome": "success",
            "editorial_shortlist": 0,
            "reviewed_new_candidates": 4,
            "day_reviewed_candidates_total": len(reviews),
            "previous_count": 0,
            "new_count": 0,
            "updated_count": 0,
            "excluded_count": 4,
            "candidate_queue_count": 9,
            "new_in_run_count": 4,
            "unreviewed_candidate_count": 0,
            "total_count": 0,
            "selected": 0,
            "lane_counts": {"model": 0, "agent_architecture": 0, "ai_product": 0, "ai_macro": 0},
            "priority_counts": {"P0": 0, "P1": 0, "P2": 0, "P3": 0},
            "executive_model_longform": 0,
            "practitioner_statements": 0,
            "cross_day_duplicates_removed": 4,
            "candidate_reviews": reviews,
            "content_topics": {"topic_count": 0, "platform_variants": 0},
            "collection_contract": {
                "raw_candidates_in_rolling_window_is_not_increment": True,
                "candidate_queue_count_is_not_new_count": True,
                "sitemap_lastmod_is_not_publication_date": True,
                "feed_titles_require_body_verification": True,
                "http_2xx_is_not_checked_no_match": True,
            },
            "notes": [
                "Reviewed only the 4 cross-run new candidates; the 335-item rolling discovery pool was not rescanned.",
                "The OpenAI research-acceleration and Images 2.5 pages match events already selected on September 10; sitemap lastmod changes were not treated as new editorial events.",
                "The Two Blind Brothers page was reviewed again because it was cross-run new, but it remains the same below-threshold customer story with no resolvable publication date.",
                "The Simon Willison page is a bird sighting and was excluded as outside all four AI Signal lanes.",
                "Five candidates from earlier same-day reviews remain in candidate_reviews for audit continuity.",
            ],
        }
    )
    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "OpenAI sitemap":
            probe["note"] = "3 new lastmod candidates were body-reviewed: 2 matched existing signals and 1 repeated a same-day below-threshold customer story; lastmod was not treated as publication evidence"
        elif probe.get("name") == "Simon Willison atom":
            probe["note"] = "new California Brown Pelican sighting was body-reviewed and excluded as outside the AI Signal domain"

    dump(day / "selected.json", [])
    dump(
        day / "citation-ledger.json",
        {
            "version": 1,
            "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
            "sources": sources,
        },
    )
    dump(day / "citations.json", [{"id": source["id"], "url": source["url"]} for source in sources])
    dump(day / "daily-brief.md", BRIEF)
    dump(day / "run-summary.json", summary)
    dump(day / "collection-run-summary.json", summary)
    print(
        json.dumps(
            {
                "date": DATE,
                "reviewed_new_candidates": 4,
                "day_reviewed_candidates_total": len(reviews),
                "selected": 0,
                "excluded_or_deduped": 4,
                "citations": len(sources),
                "topics": 0,
                "platform_variants": 0,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
