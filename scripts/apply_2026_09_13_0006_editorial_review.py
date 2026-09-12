#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-13"
RUN_AT = "2026-09-13T00:06:08+08:00"

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
]

REVIEWS = [
    {
        "url": "https://openai.com/index/paul-christiano-joins-openai-foundation-board/",
        "decision": "duplicate_prior_review_below_formal_bar",
        "published_at": "2026-09-09T17:00:00Z",
        "prior_review_date": "2026-09-12",
        "reason": "the official article still describes the same board and Safety and Security Committee appointment; it discloses no new committee powers, approval process, operating control, or model-level information, so another sitemap lastmod change is not a new event",
    },
    {
        "url": "https://openai.com/index/two-blind-brothers/",
        "decision": "exclude_below_formal_bar_date_unresolved",
        "published_at": None,
        "reason": "the first-party customer story describes accessibility and nonprofit workflows, but no distinct product release, interface change, control boundary, measured result, or structural adoption change; the article body exposes no publication date and sitemap lastmod is not substituted for one",
    },
]

BRIEF = '''# AI Signal 日报｜2026-09-13

**窗口：** 本轮只审核跨轮新增的 2 个 OpenAI Sitemap 候选；发现窗口为北京时间 2026-09-09 16:00 至 2026-09-13 00:00。正式判断以一手正文和可核验发布时间为准，不把 sitemap `lastmod` 当作发布日期。  
**一句话结论：** 2 个候选都没有形成新 Signal。Paul Christiano 的任命已在前一日审核过，本次只是同一页面再次修改；Two Blind Brothers 是无障碍使用案例，没有新的产品机制、界面、权限边界或可核验效果数据。[1][2]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 没有模型能力、训练、价格或部署边界的新变化 |
| Agent 架构 | 0 | 没有 runtime、权限、审批、日志或回滚的新机制 |
| AI 产品 | 0 | Two Blind Brothers 页面是使用案例，不是产品更新 |
| AI 宏观 | 0 | 董事任命没有附带治理权力或运行规则变化 |

## 模型｜0 条

本轮没有模型发布或模型层新信息。Paul Christiano 页面提到其对齐与前沿模型评估经历，但正文事件仍是董事及委员会任命。[1]

## Agent 架构｜0 条

两篇正文都没有披露新的 Agent runtime、工具授权、人工审批、执行日志、暂停、恢复或回滚机制。[1][2]

## AI 产品｜0 条

Two Blind Brothers 页面描述了几类真实用法：把视觉信息转成可听取和执行的信息，用语音导航，分析表格异常，连接邮箱筛选待办，并为公益项目制作材料。页面没有宣布新功能，也没有真实 UI、权限字段、执行日志或量化效果证据，因此不单独建卡。[2]

## AI 宏观｜0 条

OpenAI 9 月 9 日宣布 Paul Christiano 加入 Foundation Board 和 Safety and Security Committee，并担任 OpenAI Group PBC Board 的无投票权观察员。正文没有改变委员会权限、模型发布审批或安全治理流程；同一页面已经在 9 月 12 日审核，本轮不因再次出现 sitemap `lastmod` 而重复入库。[1]

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新的模型负责人原创内容。任命公告只有简短引语，没有模型能力、训练、评测或路线层面的信息增量。[1]

## AI 一线实践者观点｜0 条

Two Blind Brothers 的一手案例有具体使用场景，但它是厂商客户故事，不是带新数据、失败复盘或可复用工程方法的实践者原创。[2]

## 审核但未入选

- Paul Christiano 任命：`duplicate_prior_review_below_formal_bar`。官方日期为 9 月 9 日；前一日已核验，页面本次修改没有形成新的治理事件。[1]
- Two Blind Brothers：`exclude_below_formal_bar_date_unresolved`。正文可读，但没有公开文章发布日期；不拿 sitemap `lastmod` 补日期。内容是现有 ChatGPT 的无障碍与公益运营用法，没有达到产品 Signal 门槛。[2]

## 证据边界

- OpenAI 普通 `curl` 请求返回 403；本轮通过可读取的一手页面正文 fallback 完成内容核验，没有把阻断写成无内容。
- Two Blind Brothers 页面没有给出可核验 `datePublished`，因此保留日期未确认状态。
- 本轮只审核 `new_in_run_count=2` 的候选，没有重扫 339 条滚动窗口记录，也没有重审既有队列。

## 飞书短版

**一句话结论：** 本轮 2 个真新增候选完成正文核验，正式 Signal 仍为 0。  
**判断：** Paul Christiano 任命是已审核页面的再次修改；Two Blind Brothers 是无障碍使用案例，不是新的产品或架构事件。[1][2]  
**证据边界：** 后者正文没有公开发布日期，sitemap `lastmod` 不替代发布时间。  
**结果：** previous_count=0，new_count=0，updated_count=0，total_count=0。

## Sources

[1] https://openai.com/index/paul-christiano-joins-openai-foundation-board
[2] https://openai.com/index/two-blind-brothers
'''


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
            "editorial_shortlist": 0,
            "reviewed_new_candidates": 2,
            "previous_count": 0,
            "new_count": 0,
            "updated_count": 0,
            "excluded_count": 2,
            "candidate_queue_count": 2,
            "new_in_run_count": 2,
            "unreviewed_candidate_count": 0,
            "total_count": 0,
            "selected": 0,
            "lane_counts": {"model": 0, "agent_architecture": 0, "ai_product": 0, "ai_macro": 0},
            "priority_counts": {"P0": 0, "P1": 0, "P2": 0, "P3": 0},
            "executive_model_longform": 0,
            "practitioner_statements": 0,
            "cross_day_duplicates_removed": 1,
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
                "Reviewed only the 2 cross-run new candidates; the 339-item rolling discovery pool was not rescanned.",
                "Both OpenAI sitemap candidates were opened at the first-party article URL through the available public-text fallback after direct curl returned HTTP 403.",
                "Paul Christiano's September 9 appointment was already reviewed on September 12 and remains below the formal bar because the page discloses no change to governance powers or operating controls.",
                "The Two Blind Brothers customer story was excluded below the formal product bar: it documents accessibility and nonprofit workflows but no new feature, UI, control boundary, measured result, or structural adoption change.",
                "The Two Blind Brothers article date remains unresolved; sitemap lastmod was not used as publication evidence.",
            ],
        }
    )
    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "OpenAI sitemap":
            probe.update(
                {
                    "status": "candidate_only",
                    "recent_count": 120,
                    "note": "2 cross-run lastmod changes were body-reviewed; both were excluded and neither lastmod was treated as publication evidence",
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
    dump(day / "citations.json", [{"id": source["id"], "url": source["url"]} for source in SOURCES])
    dump(day / "daily-brief.md", BRIEF)
    for name in ("run-summary.json", "collection-run-summary.json"):
        path = day / name
        dump(path, update_summary(json.loads(path.read_text())))
    print(
        json.dumps(
            {
                "date": DATE,
                "reviewed_new_candidates": 2,
                "selected": 0,
                "excluded": 2,
                "citations": len(SOURCES),
                "topics": 0,
                "platform_variants": 0,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
