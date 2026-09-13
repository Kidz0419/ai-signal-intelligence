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

SIGNAL = {
    "id": "2026-09-12-simon-chatgpt-work-compaction-provenance-gap",
    "demo": False,
    "topic_lane": "agent_architecture",
    "title": "Simon Willison 实测 ChatGPT Work：27 分钟产出可用路线，但压缩后连执行代码都取不回",
    "summary": "Simon Willison 让 ChatGPT Work 的 GPT-6 Astra（Max）基于 OpenStreetMap 生成从住址出发的 5K 和 10K 环线。任务运行 27 分钟，交付了内嵌地图、GPX 和 GeoJSON；公开 HTML 也保留了路线几何。问题出在过程证据：产品界面没有展示实际代码和完整步骤，线程压缩后又无法把执行过的 Python 代码交还给用户。作者据此主张，采用上下文压缩的 Agent 应保留压缩前文本，并允许工具调用读取。",
    "decision": "include",
    "confidence": 92,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "practitioner_statement",
    "information_type": "agent_runtime",
    "evidence_level": "primary_statement",
    "source": "Simon Willison",
    "url": "https://simonwillison.net/2026/Sep/12/astra-running-routes/",
    "published_at": "2026-09-12T23:56:42Z",
    "primary_tags": ["ChatGPT Work", "Context Compaction", "Execution Provenance"],
    "secondary_tags": ["GPT-6 Astra", "OpenStreetMap", "Artifact Export", "Observability"],
    "why_it_matters_cn": "这次实测把长任务 Agent 的一个常被忽略的问题暴露得很具体：结果文件能留下，不代表用户还能解释、复查或重跑 Agent 当时做过什么。上下文压缩如果同时吞掉代码和工具轨迹，交付物就失去可审计性。",
    "personal_relevance_cn": "评估长任务 Agent 时，不能只验收最后有没有文件，还要检查压缩前对话、执行代码、工具参数、数据来源和中间产物能否导出，并确认这些证据是否跨压缩与会话保留。",
    "product_opportunity_cn": "可把不可变执行包做成标准能力：每次运行固定保存模型版本、工具调用、代码、输入来源、产物清单和压缩前 transcript；压缩只影响当前上下文，不删除审计证据，用户还能一键导出或复跑。",
    "competitive_risk_cn": "这是单次公开实测，不是 OpenAI 的正式产品文档。页面能证明作者拿到了路线文件并遇到代码不可见、压缩后无法取回的问题，但不能确认所有 ChatGPT Work 任务都会如此，也没有独立验证路线正确性；把原因归于 compaction 是作者根据交互结果作出的判断。",
    "recommended_action": "investigate",
    "questions_to_validate": [
        "ChatGPT Work 是否在后台保留完整执行代码、工具参数和压缩前 transcript，只是没有向用户开放？",
        "线程压缩、会话重启和分享后，哪些中间产物与日志仍可导出，保留多久？",
        "用户能否从最终 GPX、GeoJSON 或可视化追溯到数据请求、计算步骤和模型版本，并复跑同一任务？"
    ],
    "follow_up_triggers": [
        "OpenAI 发布 ChatGPT Work 的运行历史、上下文压缩、日志或导出文档",
        "产品 UI 开放代码、工具调用和压缩前 transcript 的查看或下载",
        "出现更多长任务因 compaction 丢失过程证据的可复现实测或官方修复"
    ],
    "scores": {
        "topic_relevance": 5,
        "novelty": 5,
        "technical_or_product_significance": 4,
        "strategic_value": 4,
        "source_quality": 5,
        "model_value": 2,
        "agent_architecture_value": 5,
        "ai_product_value": 4,
        "macro_value": 1,
        "actionability": 5
    },
    "report_date": DATE,
    "event_date": "2026-09-12",
    "canonical_url": "https://simonwillison.net/2026/Sep/12/astra-running-routes",
    "first_seen_date": DATE,
    "last_seen_date": DATE,
    "run_dates": [DATE],
    "speaker_name": "Simon Willison",
    "speaker_role": "独立研究者、开发者工具作者、长期进行 AI 产品与模型实测的写作者",
    "speaker_type": "independent_researcher",
    "statement_topic": "长任务 Agent 在上下文压缩后的执行透明度与证据保留",
    "original_source_url": "https://simonwillison.net/2026/Sep/12/astra-running-routes/",
    "new_information": "公开了一次 27 分钟 ChatGPT Work 路线生成任务的输入、输出格式和可访问 HTML 产物，并记录了实际代码在界面不可见、线程压缩后无法取回的失败边界。",
    "evidence_artifact": "作者原始长文、路线截图、可下载 GPX/GeoJSON 的说明，以及包含完整路线几何和 D3 渲染代码的公开 Gist HTML。",
    "evidence_boundary": "Atom feed 确认精确发布时间为 2026-09-12T23:56:42Z；正文和 Gist 支持任务输入、27 分钟运行、输出格式、代码不可见与压缩后无法取回。任务执行链路、路线正确性和 compaction 的内部实现没有官方文档或独立复现。",
    "related_sources": [
        "https://gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480",
        "https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/"
    ]
}

TOPICS = {
    "schema_version": 1,
    "report_date": DATE,
    "timezone": "Asia/Shanghai",
    "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。自动流程只生成 candidate，不自动发布。",
    "scope_label_cn": f"当日增量 · {DATE}",
    "source_scope": {"type": "daily", "date": DATE},
    "topics": [
        {
            "id": "2026-09-13-agent-compaction-execution-provenance",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "agent_architecture",
            "source_signal_ids": [SIGNAL["id"]],
            "working_title_cn": "Agent 交付了结果，却交不出它做过什么",
            "core_tension_cn": "长任务靠上下文压缩才能继续运行，但压缩不能顺手删掉代码、工具轨迹和可复查证据。",
            "why_now_cn": "Simon Willison 的 27 分钟路线任务成功交付地图与文件，却无法从 ChatGPT Work 取回实际执行代码；这把 Agent 的结果正确性和过程可审计性拆成了两个验收项。",
            "target_audience_cn": ["AI 产品经理", "Agent 平台与运行时团队", "企业 AI 治理与审计团队"],
            "evidence_boundary_cn": "这是单次一线实测，不是 OpenAI 官方文档。公开页面和 HTML 产物能证明输出存在及代码不可见，但不能确认普遍发生，也没有独立验证路线正确性或 compaction 内部实现。",
            "source_urls": [SIGNAL["canonical_url"]],
            "platforms": {
                "xiaohongshu": {
                    "title": "AI 跑了 27 分钟，最后却交不出它写过的代码",
                    "hook": "地图、GPX、GeoJSON 都有，唯独执行代码和完整过程拿不回来。长任务 Agent 的验收不能只看结果文件。",
                    "format": "8页图文卡",
                    "outline": [
                        "任务输入与 27 分钟执行",
                        "Agent 交付了哪些文件",
                        "真正缺失的过程证据",
                        "上下文压缩为什么会影响审计",
                        "结果正确不等于可复查",
                        "产品应保留的执行包",
                        "长任务 Agent 验收清单"
                    ],
                    "visual_direction": "左侧是地图、GPX、GeoJSON，右侧把代码、工具轨迹和压缩前 transcript 标成缺失",
                    "cta": "你会把只有结果、没有执行记录的 Agent 任务算作完成吗？"
                },
                "twitter": {
                    "title": "An agent result without its execution trace is not a reproducible deliverable",
                    "hook": "ChatGPT Work spent 27 minutes producing a map, GPX and GeoJSON. The output survived; the Python code and exact execution path did not remain available after compaction.",
                    "format": "6帖 Thread",
                    "outline": [
                        "task and outputs",
                        "what the UI hid",
                        "what compaction removed from reach",
                        "artifact versus provenance",
                        "minimum immutable run bundle",
                        "evidence boundary"
                    ],
                    "visual_direction": "run bundle diagram linking prompt, tool calls, code, data sources and exported artifacts",
                    "cta": "Does your agent preserve pre-compaction transcripts and executable traces?"
                },
                "wechat": {
                    "title": "长任务 Agent 的交付标准：文件出来了，执行过程也必须取得回来",
                    "hook": "一次成功的路线生成任务暴露了更难处理的问题：Agent 能交付最终文件，却无法交付当时运行的代码和完整步骤。",
                    "format": "2200—2800字分析",
                    "outline": [
                        "实测任务与可核验证据",
                        "最终产物和过程证据的区别",
                        "上下文压缩带来的产品缺口",
                        "为什么这会影响复查、复跑和责任界定",
                        "不可变执行包应该包含什么",
                        "日志、暂停、恢复与导出设计",
                        "企业 Agent 验收问题清单"
                    ],
                    "visual_direction": "上下文层与审计存储层分离的架构图，标出压缩不应删除的证据",
                    "cta": "附一份长任务 Agent 的可复查性交付清单。"
                }
            }
        }
    ]
}

NEW_SOURCES = [
    {
        "id": 9,
        "title": "Generating running routes with GPT-6 Astra and ChatGPT Work",
        "url": "https://simonwillison.net/2026/Sep/12/astra-running-routes",
        "publisher": "Simon Willison",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT
    },
    {
        "id": 10,
        "title": "Simon Willison's Weblog Atom feed",
        "url": "https://simonwillison.net/atom/everything/",
        "publisher": "Simon Willison",
        "evidence_level": "confirmed",
        "accessed": RUN_AT
    },
    {
        "id": 11,
        "title": "El Granada harbor loop HTML artifact",
        "url": "https://gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480",
        "publisher": "Simon Willison / GitHub Gist",
        "evidence_level": "confirmed",
        "accessed": RUN_AT
    }
]

NEW_REVIEWS = [
    {
        "url": "https://openai.com/index/two-blind-brothers/",
        "decision": "duplicate_same_day_review_no_material_update",
        "published_at": None,
        "reason": "the first-party body remains the same accessibility customer story already reviewed twice today; the latest sitemap lastmod exposes no publication date, product release, interface change, control boundary, measured result, or other material evidence update"
    },
    {
        "url": "https://simonwillison.net/2026/Sep/12/astra-running-routes/",
        "decision": "include",
        "signal_id": SIGNAL["id"],
        "published_at": "2026-09-12T23:56:42Z",
        "reason": "the first-party article and linked runnable HTML artifact document a 27-minute ChatGPT Work task, concrete exported outputs, and a reproducibility failure: the executed code was hidden and could not be recovered after thread compaction"
    }
]


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def source_block(sources: list[dict]) -> str:
    return "\n".join(f'[{source["id"]}] {source["url"]}' for source in sources)


def build_brief(sources: list[dict]) -> str:
    return f'''# AI Signal 日报｜{DATE}

**窗口：** 12:00 增量只核验本轮新增的 2 个候选；当天累计核验 11 个跨轮新增候选。发现窗口截至北京时间 2026-09-13 12:00，正式判断使用正文和 Atom 时间，不把 sitemap `lastmod` 当发布日期。
**一句话结论：** 新增 1 条 P1 Signal。Simon Willison 的长任务实测把 ChatGPT Work 的一个可审计性缺口说清楚了：地图和文件成功交付，实际执行代码却在界面中不可见，线程压缩后也无法取回。[9][10][11]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 本轮没有新模型、价格、开放范围或独立评测 |
| Agent 架构 | 1 | 长任务的上下文压缩不能吞掉代码、工具轨迹和压缩前 transcript |
| AI 产品 | 0 | Two Blind Brothers 仍是同一客户案例，没有产品上线或界面变化 |
| AI 宏观 | 0 | 没有产业结构、监管、算力或资本变化 |

## 模型｜0 条

本轮没有新的模型发布、能力边界、训练方法、定价或独立评测。GPT-6 Astra 只作为被实测的模型出现，不能从一次路线任务外推模型整体能力。[9]

## Agent 架构｜1 条

### ChatGPT Work 完成长任务，却没有留下可取回的执行代码

Simon Willison 给 ChatGPT Work 的 GPT-6 Astra（Max）一个具体任务：根据住址和 OpenStreetMap 数据生成 5K、10K 环线。任务运行 27 分钟后交付了内嵌地图、GPX 和 GeoJSON；作者公开的 HTML 还保留了完整路线几何和 D3 渲染代码。[9][11]

结果能用，过程却断了。ChatGPT 自述使用 Nominatim 定位地址、Overpass 下载道路与步道，再在本地计算环线，但产品界面没有展示实际代码和完整步骤。等作者要求取回 Python 代码时，线程已经压缩，ChatGPT 无法再提供。作者据此主张，采用 compaction 的 LLM 系统应保存压缩前文本，并允许 Agent 的工具调用访问这些记录。[9]

**为什么重要：** 长任务的完成标准不能只有最终文件。模型版本、工具调用、代码、输入来源、中间产物和压缩前 transcript 如果没有独立留存，用户就难以复查、复跑或解释结果是怎么来的。

**建议动作：** 把“不可变执行包”列入 Agent 验收：上下文压缩只改变当前推理窗口，不删除审计存储；每次运行固定保存代码、工具参数、数据来源、产物清单和模型版本，并允许用户导出。

## AI 产品｜0 条

Two Blind Brothers 页面仍在描述视觉理解、语音导航、表格分析和邮箱连接等无障碍用法。正文没有新功能、真实 UI、权限字段、执行日志或量化结果，也没有可核验发布日期；本轮再次变化的只有 sitemap `lastmod`。[2]

## AI 宏观｜0 条

本轮没有新的治理、资本、算力、监管或产业结构变化。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有模型负责人关于模型能力、训练、评测或路线的新原创内容。

## AI 一线实践者观点｜1 条

Simon Willison 的内容达到实践者门槛：有真实任务、明确运行时长、可访问产物和具体失败复盘。证据只支持这一次公开实测，不证明所有 ChatGPT Work 会话都会在压缩后丢失代码，也没有独立验证路线正确性；compaction 的内部实现仍待 OpenAI 文档确认。[9][11]

## 本轮审核但未入选

- Two Blind Brothers：`duplicate_same_day_review_no_material_update`。同一页面第三次因 sitemap 修改进入增量队列，正文仍没有发布日期或达到正式门槛的产品变化。[2]

## 当天此前审核但未入选

- Paul Christiano 任命没有附带治理权力或审批流程变化。[1]
- Claude Code v2.1.270 只是只读 Git 命令误触发权限询问的回归修复。[3]
- Legora 页面是已入库 Astra 事件的旧案例页再次更新 `lastmod`。[4]
- Paul Ford 条目只有一段二手引文，没有可核验的构建或评测增量。[5]
- OpenAI 研究加速报告与 Images 2.5 都是已入库页面再次修改。[6][7]
- California Brown Pelican 与 AI Signal 四条主线无关。[8]

## 证据边界

- Atom feed 给出的精确发布时间是 2026-09-12T23:56:42Z，即北京时间 9 月 13 日 07:56；页面显示的自然日仍是 9 月 12 日，因此事件保留 `event_date=2026-09-12`。[9][10]
- 路线 HTML 能确认交付产物及路线几何存在；执行代码不可见、压缩后无法取回和原因判断来自作者本人，不是 OpenAI 的正式说明。[9][11]
- OpenAI 普通请求对部分页面返回 403；Two Blind Brothers 通过可读正文 fallback 核验，没有把阻断当成无内容。[2]
- 本轮只审核 `new_in_run_count=2` 的候选，没有重扫 329 条滚动窗口记录，也没有重审完整候选队列。

## 飞书短版

**一句话结论：** 12:00 的 2 个真新增候选完成正文核验，新增 1 条 P1 Agent 架构 Signal。
**重点：** ChatGPT Work 用 27 分钟交付了路线地图、GPX 和 GeoJSON，但实际执行代码在 UI 中不可见，线程压缩后也无法取回。[9][11]
**判断：** 长任务 Agent 的交付不能只有最终文件，还要保留代码、工具轨迹、数据来源、模型版本和压缩前 transcript。
**边界：** 这是 Simon Willison 的单次实测；路线正确性和 compaction 内部机制没有独立复现或官方文档。[9]
**建议动作：** 把不可变执行包和压缩前记录导出加入 Agent 产品验收。
**结果：** previous_count=0，new_count=1，updated_count=0，total_count=1。

## Sources

{source_block(sources)}
'''


def main() -> None:
    day = ROOT / "daily" / DATE
    collection = json.loads((day / "collection-run-summary.json").read_text())
    prior_summary = json.loads((day / "run-summary.json").read_text())
    prior_sources = json.loads((day / "citation-ledger.json").read_text())["sources"]
    prior_reviews = prior_summary.get("candidate_reviews", [])

    existing_urls = {source["url"].rstrip("/") for source in prior_sources}
    sources = list(prior_sources)
    for source in NEW_SOURCES:
        if source["url"].rstrip("/") not in existing_urls:
            sources.append(source)
            existing_urls.add(source["url"].rstrip("/"))

    summary = deepcopy(collection)
    coverage = summary.get("source_coverage", {})
    counts = coverage.get("status_counts", {})
    if counts.get("not_checked", 0) > 0:
        counts["not_checked"] -= 1
        counts["selected"] = counts.get("selected", 0) + 1
    channel = coverage.get("channel_counts", {}).get("practitioner_and_product_leader_longform", {})
    if channel.get("not_checked", 0) > 0:
        channel["not_checked"] -= 1
        channel["selected"] = channel.get("selected", 0) + 1
    for record in coverage.get("records", []):
        if record.get("name") == "Simon Willison":
            record["status"] = "selected"
            record["note"] = "Atom timestamp and first-party body reviewed; one practitioner signal selected from the current increment"

    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "OpenAI sitemap":
            probe["note"] = "The new Two Blind Brothers lastmod was body-reviewed and matched the same same-day below-threshold customer story; lastmod was not used as publication evidence"
        elif probe.get("name") == "Simon Willison atom":
            probe["status"] = "selected"
            probe["note"] = "The new running-route article was body-reviewed with its linked HTML artifact; selected for the concrete compaction and execution-provenance failure"

    reviews = prior_reviews + NEW_REVIEWS
    summary.update({
        "run_type": "daily_four_lane_incremental_editorial_review",
        "run_at": RUN_AT,
        "deliverable_outcome": "success",
        "scheduler_outcome": "success",
        "editorial_shortlist": 1,
        "reviewed_new_candidates": 2,
        "day_reviewed_candidates_total": len(reviews),
        "previous_count": 0,
        "new_count": 1,
        "updated_count": 0,
        "excluded_count": 1,
        "candidate_queue_count": 11,
        "new_in_run_count": 2,
        "unreviewed_candidate_count": 0,
        "total_count": 1,
        "selected": 1,
        "lane_counts": {"model": 0, "agent_architecture": 1, "ai_product": 0, "ai_macro": 0},
        "priority_counts": {"P0": 0, "P1": 1, "P2": 0, "P3": 0},
        "executive_model_longform": 0,
        "practitioner_statements": 1,
        "cross_day_duplicates_removed": 1,
        "candidate_reviews": reviews,
        "content_topics": {"topic_count": 1, "platform_variants": 3},
        "collection_contract": {
            "raw_candidates_in_rolling_window_is_not_increment": True,
            "candidate_queue_count_is_not_new_count": True,
            "sitemap_lastmod_is_not_publication_date": True,
            "feed_titles_require_body_verification": True,
            "http_2xx_is_not_checked_no_match": True
        },
        "notes": [
            "Reviewed only the 2 cross-run new candidates; the 329-item rolling discovery pool and 11-item queue were not rescanned.",
            "The Two Blind Brothers page was body-reviewed again because its sitemap lastmod changed, but no publication date or material product evidence changed.",
            "Simon Willison's article and linked HTML artifact document a distinct long-task reproducibility failure: final artifacts survived while executed code was not visible and could not be recovered after thread compaction.",
            "The Simon item is kept separate from the August 30 ChatGPT Work overview because it is a new experiment, a new canonical source, and a distinct execution-provenance finding.",
            "Nine candidates from earlier same-day reviews remain in candidate_reviews for audit continuity."
        ]
    })

    dump(day / "selected.json", [SIGNAL])
    dump(day / "citation-ledger.json", {
        "version": 1,
        "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
        "sources": sources
    })
    dump(day / "citations.json", [{"id": source["id"], "url": source["url"]} for source in sources])
    dump(day / "daily-brief.md", build_brief(sources))
    dump(day / "run-summary.json", summary)
    dump(ROOT / "content-topics" / DATE / "topics.json", TOPICS)

    print(json.dumps({
        "date": DATE,
        "reviewed_new_candidates": 2,
        "day_reviewed_candidates_total": len(reviews),
        "selected": 1,
        "excluded_or_deduped": 1,
        "citations": len(sources),
        "topics": 1,
        "platform_variants": 3
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
