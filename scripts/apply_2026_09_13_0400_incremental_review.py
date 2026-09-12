#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-13"
RUN_AT = "2026-09-13T04:03:35+08:00"

SOURCES = [
    {
        "id": 1,
        "title": "Paul Christiano joins OpenAI Foundation Board",
        "url": "https://openai.com/index/paul-christiano-joins-openai-foundation-board",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
    {
        "id": 2,
        "title": "Supporting the blind community with ChatGPT",
        "url": "https://openai.com/index/two-blind-brothers",
        "publisher": "OpenAI",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT,
    },
    {
        "id": 3,
        "title": "Claude Code v2.1.270",
        "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.270",
        "publisher": "Anthropic / GitHub",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
    {
        "id": 4,
        "title": "Legora reviewed 41 documents in minutes with GPT-6 Astra",
        "url": "https://openai.com/index/legora-financial-statement-review-with-astra",
        "publisher": "OpenAI / Legora",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT,
    },
    {
        "id": 5,
        "title": "A quote from Paul Ford",
        "url": "https://simonwillison.net/2026/Sep/12/paul-ford",
        "publisher": "Simon Willison",
        "evidence_level": "reported",
        "accessed": RUN_AT,
    },
]

NEW_REVIEWS = [
    {
        "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.270",
        "decision": "exclude_below_formal_bar",
        "published_at": "2026-09-12T19:45:44Z",
        "reason": "the official release contains one narrow regression fix for read-only git commands asking for permission after a long-running session; it adds no new permission model, approval control, workflow, logging, pause, recovery, or rollback mechanism",
    },
    {
        "url": "https://openai.com/index/legora-financial-statement-review-with-astra/",
        "decision": "duplicate_existing_no_material_update",
        "signal_id": "2026-09-03-openai-gpt6-astra-broad-release-monitorability",
        "published_at": "2026-09-03",
        "reason": "the first-party article is the same September 3 Legora deployment case already attached to the Astra event; the new sitemap lastmod does not prove a new release, evidence upgrade, or workflow change",
    },
    {
        "url": "https://simonwillison.net/2026/Sep/12/paul-ford/",
        "decision": "exclude_below_practitioner_bar",
        "published_at": "2026-09-12T18:00:21Z",
        "reason": "the page reproduces a short quotation from a linked opinion article; it contains no builder case, new data, technical explanation, failure review, reusable method, or product mechanism that can be evaluated from the accessible first-party page",
    },
]

BRIEF = '''# AI Signal 日报｜2026-09-13

**窗口：** 北京时间 2026-09-09 20:00 至 2026-09-13 04:00。本轮只审核 3 个跨轮新增候选；当天此前的 2 个候选保留在审核记录中。  
**一句话结论：** 新增的 Claude Code 修复、Legora 页面改动和 Paul Ford 引文都没有形成新 Signal。一个是小范围回归修复，一个是已入库事件的旧案例页再次更新 `lastmod`，另一个只有一段二手引文。[3][4][5]

## 四主线重点

| 主线 | 数量 | 本轮判断 |
|---|---:|---|
| 模型 | 0 | Legora 页面仍是 9 月 3 日的 Astra 案例，没有新的模型能力或部署变化 |
| Agent 架构 | 0 | Claude Code 只修复误触发权限询问的回归，没有新增控制机制 |
| AI 产品 | 0 | 没有新的界面、工作流或执行边界 |
| AI 宏观 | 0 | 没有产业结构、治理或采用变化 |

## 模型｜0 条

Legora 页面日期仍是 9 月 3 日，内容仍为 Astra 在 41 份财务文件 tie-out 中的厂商案例。它已经作为相关来源并入 9 月 3 日的 Astra 事件，本轮 `lastmod` 变化没有带来新模型事实或独立评测。[4]

## Agent 架构｜0 条

Claude Code v2.1.270 只修复一个 v2.1.269 回归：长时间运行会话中，只读 Git 命令可能意外触发权限询问。修复没有引入新的权限模型、审批配置、日志、暂停恢复或回滚机制，因此不单独建卡。[3]

## AI 产品｜0 条

本轮没有可核验的新界面或产品工作流。Legora 的单次 Agent 运行、逐项记录和最终人工判断仍是已收录案例；页面没有披露新的动作对象、批准步骤或上线范围。[4]

## AI 宏观｜0 条

当天此前审核的 Paul Christiano 任命没有附带委员会权力或模型发布审批变化；Two Blind Brothers 仍是无障碍使用案例，不是结构性采用事件。[1][2]

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有模型负责人关于模型能力、训练、评测或路线的新原创内容。

## AI 一线实践者观点｜0 条

Simon Willison 页面只转载 Paul Ford 文章中的一段引文，并链接到原评论文章。可访问页面没有给出真实构建案例、新数据、失败复盘或可复用方法，不达到实践者观点门槛。[5]

## 审核但未入选

- Claude Code v2.1.270：`exclude_below_formal_bar`。官方 Release 时间为 2026-09-12 19:45:44 UTC；正文只有一项权限询问回归修复。[3]
- Legora + Astra：`duplicate_existing_no_material_update`。正文标注 2026 年 9 月 3 日，已并入 `2026-09-03-openai-gpt6-astra-broad-release-monitorability`；不把 sitemap `lastmod` 写成新事件。[4]
- Paul Ford 引文：`exclude_below_practitioner_bar`。Simon Willison 页面发布于 9 月 12 日，只提供短引文和原文链接，不能支撑更深的产品或工程判断。[5]

## 证据边界

- GitHub Release 页面和 API 给出 v2.1.270 的一致正文与发布时间。[3]
- OpenAI 正文给出 Legora 页面的 9 月 3 日日期；sitemap `lastmod` 只用于发现。[4]
- Paul Ford 原文链接受访问限制，本轮只按 Simon Willison 可读页面中的引文判断，没有补写原文观点。[5]
- 本轮没有重扫 341 条滚动窗口记录，也没有重审全部注册源。

## 飞书短版

**一句话结论：** 本轮 3 个真新增候选完成正文核验，正式 Signal 仍为 0。  
**判断：** Claude Code 是小范围回归修复；Legora 是已入库 Astra 案例的页面更新；Paul Ford 条目只有二手短引文。[3][4][5]  
**证据边界：** Release 时间已核验，OpenAI `lastmod` 不当发布时间，受限原文不做扩写。  
**结果：** previous_count=0，new_count=0，updated_count=0，total_count=0。

## Sources

[1] https://openai.com/index/paul-christiano-joins-openai-foundation-board
[2] https://openai.com/index/two-blind-brothers
[3] https://github.com/anthropics/claude-code/releases/tag/v2.1.270
[4] https://openai.com/index/legora-financial-statement-review-with-astra
[5] https://simonwillison.net/2026/Sep/12/paul-ford
'''


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def editorial_summary(collection: dict, prior_reviews: list[dict]) -> dict:
    summary = deepcopy(collection)
    reviews = prior_reviews + NEW_REVIEWS
    summary.update(
        {
            "run_type": "daily_four_lane_incremental_editorial_review",
            "run_at": RUN_AT,
            "deliverable_outcome": "success",
            "scheduler_outcome": "success",
            "editorial_shortlist": 0,
            "reviewed_new_candidates": 3,
            "day_reviewed_candidates_total": len(reviews),
            "previous_count": 0,
            "new_count": 0,
            "updated_count": 0,
            "excluded_count": 3,
            "candidate_queue_count": 5,
            "new_in_run_count": 3,
            "unreviewed_candidate_count": 0,
            "total_count": 0,
            "selected": 0,
            "lane_counts": {"model": 0, "agent_architecture": 0, "ai_product": 0, "ai_macro": 0},
            "priority_counts": {"P0": 0, "P1": 0, "P2": 0, "P3": 0},
            "executive_model_longform": 0,
            "practitioner_statements": 0,
            "cross_day_duplicates_removed": 2,
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
                "Reviewed only the 3 cross-run new candidates; the 341-item rolling discovery pool was not rescanned.",
                "Claude Code v2.1.270 was verified through the official GitHub Release page and API; its sole change is a narrow permission-prompt regression fix below the formal signal bar.",
                "The Legora article is dated September 3 and is already attached to the existing Astra event; another sitemap lastmod is not a new editorial event.",
                "The Simon Willison item is a short quotation of a linked opinion article and contains no content-level practitioner evidence that meets the inclusion threshold.",
                "The two candidates from the earlier same-day review remain in candidate_reviews for daily audit continuity.",
            ],
        }
    )
    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "Claude Code releases":
            probe["note"] = "v2.1.270 body and release timestamp reviewed; excluded as a narrow regression fix below the formal bar"
        elif probe.get("name") == "OpenAI sitemap":
            probe["note"] = "new Legora lastmod was body-reviewed and matched an existing September 3 event; lastmod was not treated as publication evidence"
        elif probe.get("name") == "Simon Willison atom":
            probe["note"] = "new Paul Ford quotation page was opened; excluded because the accessible body contains only a short secondary quotation"
    return summary


def main() -> None:
    day = ROOT / "daily" / DATE
    prior_summary = json.loads((day / "run-summary.json").read_text())
    collection = json.loads((day / "collection-run-summary.json").read_text())
    prior_reviews = prior_summary.get("candidate_reviews", [])
    summary = editorial_summary(collection, prior_reviews)

    dump(day / "selected.json", [])
    dump(
        day / "citation-ledger.json",
        {
            "version": 1,
            "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
            "sources": SOURCES,
        },
    )
    dump(day / "citations.json", [{"id": source["id"], "url": source["url"]} for source in SOURCES])
    dump(day / "daily-brief.md", BRIEF)
    dump(day / "run-summary.json", summary)
    dump(day / "collection-run-summary.json", summary)
    print(
        json.dumps(
            {
                "date": DATE,
                "reviewed_new_candidates": 3,
                "day_reviewed_candidates_total": len(summary["candidate_reviews"]),
                "selected": 0,
                "excluded_or_deduped": 3,
                "citations": len(SOURCES),
                "topics": 0,
                "platform_variants": 0,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
