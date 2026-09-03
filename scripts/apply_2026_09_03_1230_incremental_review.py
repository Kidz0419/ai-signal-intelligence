#!/usr/bin/env python
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-03"
TZ = ZoneInfo("Asia/Shanghai")
RUN_AT = datetime.now(TZ).replace(microsecond=0)
DISCOVERY_START = "2026-08-31T04:16:54+08:00"
DISCOVERY_END = "2026-09-03T12:16:54+08:00"
CANDIDATE_QUEUE_COUNT = 240
NEW_IN_RUN_COUNT = 14

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
LANE_ORDER = {"model": 0, "agent_architecture": 1, "ai_product": 2, "ai_macro": 3}


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


new_row = {
    "id": "2026-09-03-openai-codex-01530-plugin-approval-context-controls",
    "demo": False,
    "topic_lane": "agent_architecture",
    "title": "OpenAI Codex 0.153.0 把插件市场、审批路径和实验性上下文管理一起拉进可见控制面",
    "summary": "OpenAI 9 月 3 日发布 Codex 0.153.0。稳定版 release notes 写明，plugin CLI 已能从 remote marketplaces 列出、安装和移除插件；Full Access 会跳过 confirmation-only 动作的 Guardian review，User approval 模式则跳过后台 Guardian scoring 和 prewarming，但敏感动作检查与用户输入请求仍保留。正文还确认 Guardian review history 可跨 compaction、restart 和用户 fork 保留，MCP tool approvals 开始按所选 app account 隔离，并新增默认关闭的 experimental context management，可为符合条件的 Codex backend 会话打开 token-budget context、history notes 和 `new_context` 工具。",
    "decision": "include",
    "confidence": 91,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "technical_update",
    "information_type": "agent_runtime",
    "evidence_level": "confirmed",
    "source": "OpenAI",
    "url": "https://github.com/openai/codex/releases/tag/rust-v0.153.0",
    "published_at": "2026-09-03T01:37:38Z",
    "primary_tags": [
        "OpenAI Codex",
        "Plugin Marketplace",
        "Guardian Review"
    ],
    "secondary_tags": [
        "MCP Approvals",
        "Context Management",
        "Async User Input"
    ],
    "why_it_matters_cn": "这版值钱的不是 Vim undo 或配额提醒，而是插件来源、审批模式、Guardian 留痕、账号作用域和上下文预算开始被一起暴露成可见控制项。Codex 的 control plane 从单点补丁慢慢长成了一组连动配置。",
    "personal_relevance_cn": "如果你在看 coding agent 的真实运行面，最该盯的是 remote plugin marketplace、Full Access / User approval 的分流、MCP 审批按账号隔离，以及 context_management.experimental_mode 到底能不能减少长任务漂移。",
    "product_opportunity_cn": "可以把插件市场治理、审批模式切换、review history 持久化、异步用户追问和 token-budget context 管理，设计成自己的 coding agent control plane。",
    "competitive_risk_cn": "能确认的是 release notes 列出的控制项与限制；experimental context management 默认关闭且限特定 ChatGPT 计划和 Codex backend，会话默认策略、团队级审计面和成功率提升还没公开。",
    "recommended_action": "investigate",
    "questions_to_validate": [
        "remote marketplace plugin install 的 allowlist、source policy 和审计记录会怎样落到管理员配置？",
        "Full Access / User approval 跳过部分 Guardian 流程后，哪些敏感动作仍会被强制拦下或要求人工确认？",
        "experimental context management 里的 history notes 与 `new_context`，会不会真正改变长任务成功率、回滚成本和可解释性？"
    ],
    "follow_up_triggers": [
        "Codex 帮助中心或产品文档补充 plugin marketplace、approval mode 和 experimental context management 的默认策略",
        "后续 release 公布管理员配置、审计导出或更广的团队 rollout 细节",
        "出现围绕长任务、MCP 审批和 Guardian review 的真实使用复盘"
    ],
    "scores": {
        "topic_relevance": 5,
        "novelty": 4,
        "technical_or_product_significance": 4,
        "strategic_value": 4,
        "source_quality": 5,
        "model_value": 1,
        "agent_architecture_value": 5,
        "ai_product_value": 4,
        "macro_value": 1,
        "actionability": 5
    },
    "report_date": DATE,
    "event_date": DATE,
    "canonical_url": "https://github.com/openai/codex/releases/tag/rust-v0.153.0",
    "first_seen_date": DATE,
    "last_seen_date": DATE,
    "run_dates": [DATE],
    "evidence_boundary": "GitHub release notes 能确认 remote marketplace plugin CLI、Full Access / User approval 的 Guardian 行为变化、review history 持久化、account-scoped MCP approvals、异步用户输入请求，以及默认关闭的 experimental context management。release notes 不能证明这些设置的默认团队策略、最终审计面或对长任务成功率的实际提升。",
    "related_sources": [
        {
            "url": "https://github.com/openai/codex/releases/tag/rust-v0.153.0-alpha.5.1",
            "type": "same_day_prerelease"
        }
    ]
}

new_topic = {
    "id": "2026-09-03-codex-plugin-approval-context-control-plane",
    "status": "candidate",
    "timeliness": "this_week",
    "priority": "A",
    "topic_lane": "agent_architecture",
    "source_signal_ids": [
        "2026-09-03-openai-codex-01530-plugin-approval-context-controls"
    ],
    "working_title_cn": "Codex 正在把插件分发、审批路径和上下文预算收进同一层 agent control plane",
    "core_tension_cn": "很多 coding agent 还停在“会不会写代码”，真正拉开差距的却越来越像基础设施问题：谁能装插件、谁能跳过复核、上下文怎么控预算、历史怎么保留。",
    "why_now_cn": "Codex 0.153.0 稳定版把 remote marketplace plugin CLI、Guardian 模式分流、account-scoped MCP approvals 和 experimental context management 一起公开了。",
    "target_audience_cn": [
        "Coding agent 产品团队",
        "Agent runtime 工程师",
        "平台安全与治理团队"
    ],
    "evidence_boundary_cn": "release notes 能确认配置项和行为变化；experimental context management 默认关闭，且只限特定 ChatGPT 计划 / Codex backend，会话默认策略与真实成功率增益还没公开。",
    "source_urls": [
        "https://github.com/openai/codex/releases/tag/rust-v0.153.0"
    ],
    "platforms": {
        "xiaohongshu": {
            "title": "Codex 正在把插件分发、审批路径和上下文预算收进同一层控制面",
            "hook": "别只盯着模型会不会写代码。真正的产品差距，越来越落在插件来源、审批模式、留痕和上下文预算这些基础设施细节上。",
            "format": "7页图文卡",
            "outline": [
                "已确认发生了什么",
                "关键对象与动作 / 控制面",
                "为什么这件事现在值得写",
                "证据边界和不能误写的地方",
                "对产品 / 架构判断的启发",
                "接下来要继续验证什么"
            ],
            "visual_direction": "对象—动作—权限边界图，少量术语，结论先行",
            "cta": "你会先把哪条控制项做成产品默认值？"
        },
        "twitter": {
            "title": "Codex 正在把插件分发、审批路径和上下文预算收进同一层 agent control plane",
            "hook": "The interesting part is no longer just code generation. It's plugin source policy, approval modes, review history, and context budgets becoming explicit runtime controls.",
            "format": "7帖 Thread",
            "outline": [
                "已确认发生了什么",
                "关键对象与动作 / 控制面",
                "为什么这件事现在值得写",
                "证据边界和不能误写的地方",
                "对产品 / 架构判断的启发",
                "接下来要继续验证什么"
            ],
            "visual_direction": "one workflow or control-plane diagram",
            "cta": "Which control would you test first?"
        },
        "wechat": {
            "title": "Codex 正在把插件分发、审批路径和上下文预算收进同一层 agent control plane",
            "hook": "这次更值得盯的不是又一个版本号，而是 coding agent 的插件来源、审批模式、历史留痕和上下文预算开始被一起产品化。",
            "format": "1800—2400字深度文章",
            "outline": [
                "已确认发生了什么",
                "关键对象与动作 / 控制面",
                "为什么这件事现在值得写",
                "证据边界和不能误写的地方",
                "对产品 / 架构判断的启发",
                "接下来要继续验证什么"
            ],
            "visual_direction": "工作流图、证据边界表、验证清单",
            "cta": "文末附 coding agent control plane 验收问题"
        }
    }
}


def main() -> None:
    day = ROOT / "daily" / DATE
    selected = json.loads((day / "selected.json").read_text())
    if not any(row["id"] == new_row["id"] for row in selected):
        selected.append(new_row)
    selected.sort(key=lambda row: (
        PRIORITY_ORDER[row["relevance_level"]],
        LANE_ORDER[row["topic_lane"]],
        row["event_date"],
        row["id"],
    ))

    ledger = json.loads((day / "citation-ledger.json").read_text())
    if not any(source["id"] == 9 for source in ledger["sources"]):
        ledger["sources"].append({
            "id": 9,
            "title": new_row["title"],
            "url": new_row["url"],
            "publisher": "OpenAI",
            "evidence_level": "confirmed",
            "accessed": RUN_AT.isoformat(),
        })
        ledger["sources"].sort(key=lambda source: source["id"])
    citations = [{"id": source["id"], "url": source["url"]} for source in ledger["sources"]]

    topics_path = ROOT / "content-topics" / DATE / "topics.json"
    topics_payload = json.loads(topics_path.read_text())
    topics = topics_payload["topics"]
    if not any(topic["id"] == new_topic["id"] for topic in topics):
        topics.append(new_topic)
    topics.sort(key=lambda topic: (topic["priority"], LANE_ORDER[topic["topic_lane"]], topic["id"]))
    topics_payload["topics"] = topics

    lane_counts = {
        "model": sum(row["topic_lane"] == "model" for row in selected),
        "agent_architecture": sum(row["topic_lane"] == "agent_architecture" for row in selected),
        "ai_product": sum(row["topic_lane"] == "ai_product" for row in selected),
        "ai_macro": sum(row["topic_lane"] == "ai_macro" for row in selected),
    }
    priority_counts = {key: sum(row["relevance_level"] == key for row in selected) for key in ("P0", "P1", "P2", "P3")}

    brief = f'''# AI Signal 日报｜{DATE}

**窗口：** 发现窗口北京时间 2026-08-31 04:16 至 2026-09-03 12:16；本轮只核验 14 个真新增候选，不重扫 240 条待审队列。  
**一句话结论：** 这轮又补进 1 条正式 signal，日内总数从 5 条增到 6 条。新增最值得盯的是 OpenAI Codex 0.153.0：比起界面小修，这次更关键的是插件分发、审批路径、Guardian 留痕和实验性上下文管理一起被拉进了可见控制面。[9]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 2 | OpenAI 把 Astra 划进 Critical 阈值；Google 发布 Gemini 3.8 Flash / Flash Cyber + Fairwind |
| Agent 架构 | 2 | Codex 把插件市场、审批和上下文预算拉进控制面；AWS 把 Strands 的持久存储 contract 真写到运行面 |
| AI 产品 | 2 | Anthropic 把高风险企业控制面产品化；OpenAI 把 ChatGPT for Healthcare 接进 Epic 与官方医疗数据源 |
| AI 宏观 | 0 | 本轮没有新增正式结构事件 |

## 模型｜2 条

### OpenAI：Astra 先跨线，再上锁

OpenAI 通过官方文章表示，Astra 已达到 Preparedness Framework 的 Critical cybersecurity capability threshold；文中说，该模型在合适工具和访问条件下可以发现未知漏洞并构造针对加固系统的利用链。OpenAI 同时披露，团队因此推迟了部分开发与发布，并计划先把最强 cyber 能力放给小范围测试者，再通过 Daybreak Blue 扩大到防守方。[1][2]

**为什么重要：** 一旦厂商自己认定模型跨过 critical 线，最先变化的往往不是功能页，而是训练节奏、权限边界和发售路径。

### Google：Gemini 3.8 Flash 公开 GA，Flash Cyber 则被装进 Fairwind

Gemini API changelog 已把 `gemini-3.8-flash` 标成 GA。Google 同日正文写明，3.8 Flash 维持 3.7 Flash 的定价，也就是每百万 input tokens 0.75 美元、output tokens 3.75 美元；同批发布的 3.8 Flash Cyber 则通过 Fairwind Program 和 CodeMender 面向受信防守方，Fairwind 页面还写到当前已有 650 多个参与伙伴。[3][4][5]

**为什么重要：** 这次不是单纯换个更强的 Flash 版本。Google 把公开主力模型、受限 cyber 能力和自动补丁 harness 一起推到了台前。

## Agent 架构｜2 条

### OpenAI：Codex 开始把插件、审批和上下文预算放进同一层控制面

OpenAI 发布 Codex 0.153.0。稳定版 release notes 写明，plugin CLI 已能从 remote marketplaces 列出、安装和移除插件；Full Access 会跳过 confirmation-only 动作的 Guardian review，User approval 模式则跳过后台 Guardian scoring 和 prewarming，但敏感动作检查与用户输入请求仍保留。正文还确认 Guardian review history 可跨 compaction、restart 和用户 fork 保留，MCP tool approvals 开始按所选 app account 隔离，并新增默认关闭的 experimental context management，可为符合条件的 Codex backend 会话打开 token-budget context、history notes 和 `new_context` 工具。[9]

**为什么重要：** 真正该看的是 Codex 的 control plane 开始从单点 patch 变成一组连动配置：插件来源、审批模式、历史留痕、账号作用域和上下文预算一起上桌了。

### AWS：Strands 的 memory 不再只是一层抽象

AWS 新发的 `strands-dynamodb-storage`，把 Strands 的 storage contract 落成了单表 DynamoDB 后端：session snapshot、memory、context offload 和 transcript 共用同一套 `write / read / delete / list` 接口。正文还确认了几项会直接影响运行面的细节：大于 400KB 的值可选 S3 offload，可选 gzip、TTL 和 multi-tenant prefix，而且表、备份、标签和加密策略都由使用方自己管。[7]

**为什么重要：** 很多 agent 框架都说自己有 memory，真正难的是把状态和留痕放进一套能在无状态计算环境里跑得住的 contract。

## AI 产品｜2 条

### Anthropic：frontier 模型企业化，开始把日志归属和人工复核拆开

Anthropic 9 月 1 日发布 Enterprise Frontier Safeguards（EFS）。正文写明，用于监测的 activity data 可以放在客户自有云账户里，由客户自己控制存储、密钥、访问策略和审计日志；检测到 serious misuse 的 flag 直接发给客户团队处理，不需要 Anthropic 员工人工复核。Anthropic 还说，这套控制不改变 model behavior、API pricing 或 rate limits，并将于今年秋季稍晚分阶段 rollout。[8]

**为什么重要：** 这条真正的信号不是“更安全”这四个字，而是 frontier model 的企业交付开始多出一层独立控制面：谁持有日志、谁握着密钥、谁看告警，正在决定它能不能真的进 regulated workflow。

### OpenAI：医疗工作流开始贴着授权病历和官方数据源跑

OpenAI 为 ChatGPT for Healthcare 新增 Epic EHR integration，并推出 Healthcare Public Data plugin，把 ClinicalTrials.gov、CMS Coverage、RxNorm、DailyMed 和 PubMed 等 9 个官方来源带进同一工作区。页面还写明两种落点：在 ChatGPT 内拉取授权病历上下文，或把 ChatGPT 直接嵌进 EHR workflow；官方医生评测给出 4,363 次打分中 99.1% safe，以及 5 个连接数据源上 93% 以上“good or better” accuracy。[1][6]

**为什么重要：** 真正的新点不是多了一个医疗场景页，而是 ChatGPT 开始直接贴着授权 EHR 和可枚举的官方数据源工作，临床前置准备、药物核对和 trial 查询从开放问答走向受控工作流。

## AI 宏观｜0 条

本轮没有进入正式范围的新增结构事件。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新增满足模型主题边界和信息增量门槛的高管长文。

## AI 一线实践者观点｜0 条

本轮没有新的实践者原创内容进入正式日报。

## 证据边界

- Astra 这条目前仍是 OpenAI 的官方自我判定：能确认阈值结论、开发延后和受限发售路径，不能写成第三方已经独立复现，更不能写成全面开放。[1][2]
- Gemini 3.8 Flash 的 GA 与公开定价可确认，但 Flash Cyber 的性能、patch 效果和 Fairwind 覆盖规模仍主要来自 Google 或合作方表述，而且 Flash Cyber 不是面向所有开发者的广泛 GA。[3][4][5]
- Codex 0.153.0 能确认 remote marketplace plugin CLI、Guardian 模式分流、review history 持久化、account-scoped MCP approvals 和默认关闭的 experimental context management；它还不能证明这些控制项的默认团队策略、最终审计面或长任务成功率已经改善。[9]
- Anthropic 这条能确认发布日期、customer-owned storage、customer-managed keys、direct flag routing 和 no Anthropic human review，但它现在仍是 phased rollout 方案，不能写成已全面 GA，也不能把自动监测效果写成独立验证结论。[8]
- ChatGPT for Healthcare 这条能确认 Epic 连接、9 个官方数据源和两种工作流形态；99.1% safe 与 93% 以上 accuracy 仍属于 OpenAI 官方医生评测，不是独立临床验证。[1][6]
- AWS 这条能确认 storage contract、S3 offload、TTL 和租户前缀，但它仍是 DynamoDB 路线，不是跨云通用答案，也没有给出大规模独立成本对比。[7]

## 飞书短版

**一句话结论：** 这轮多 1 条，日内正式 signal 从 5 条增到 6 条；新增最值得补记的是 Codex 0.153.0 把 plugin marketplace、approval mode 和 context management 一起拖进了 visible control plane。  
**组织判断：** 今天更清楚的一条线是，frontier model 和 coding agent 都在把权限、审批、日志、上下文预算这些原本藏在实现里的东西，慢慢做成显式控制面。  
**建议动作：** 把 high-risk model gating、customer-owned telemetry、customer-managed keys、EHR embedded workflow、plugin source policy 和 agent durable storage contract 一起加进后续评估清单。  
**结果：** previous_count=5，new_count=1，updated_count=0，total_count=6。

## Sources

[1] https://openai.com/news/rss.xml
[2] https://r.jina.ai/http://openai.com/index/path-to-astra/
[3] https://ai.google.dev/gemini-api/docs/changelog
[4] https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
[5] https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
[6] https://r.jina.ai/http://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
[7] https://aws.amazon.com/blogs/database/introducing-strands-dynamodb-storage-durable-agent-storage-for-the-strands-agents-sdk/
[8] https://www.anthropic.com/news/enterprise-frontier-safeguards
[9] https://github.com/openai/codex/releases/tag/rust-v0.153.0
'''

    run_summary = {
        "run_type": "daily_four_lane_incremental_manual_review",
        "run_at": RUN_AT.isoformat(),
        "deliverable_outcome": "success",
        "scheduler_outcome": "success",
        "window": {
            "timezone": "Asia/Shanghai",
            "start": DISCOVERY_START,
            "end": DISCOVERY_END,
            "incremental_since": None,
        },
        "registered_sources": 111,
        "raw_candidates": 229,
        "unique_candidates": 195,
        "candidate_queue_count": CANDIDATE_QUEUE_COUNT,
        "new_in_run_count": NEW_IN_RUN_COUNT,
        "reviewed_new_candidates": NEW_IN_RUN_COUNT,
        "editorial_shortlist": 5,
        "previous_count": 5,
        "new_count": 1,
        "updated_count": 0,
        "excluded_count": 13,
        "unreviewed_candidate_count": 0,
        "total_count": len(selected),
        "selected": len(selected),
        "lane_counts": lane_counts,
        "priority_counts": priority_counts,
        "decision_counts": {
            "include": len(selected),
            "watchlist": 0,
        },
        "executive_model_longform": 0,
        "practitioner_statements": 0,
        "cross_day_duplicates_removed": 0,
        "source_status_counts": {
            "selected": 1,
            "candidate_only": 0,
            "checked_no_match": 13,
            "access_blocked": 0,
            "auth_required": 0,
            "mechanical_failure": 0,
            "not_checked": 0,
        },
        "review_breakdown": {
            "selected": 1,
            "outside_editorial_window": 8,
            "already_selected_same_day": 2,
            "below_formal_bar": 3,
        },
        "review_notes": [
            "Reviewed only the 14 true new candidates from the 2026-09-03 12:16 baseline cycle and did not reopen the 240-item carry-forward queue.",
            "Mapped all 12 OpenAI sitemap hits through the official OpenAI News RSS before freshness judgment. Eight resolved to publication dates before the active 80-hour editorial window, so ChatGPT Ads Europe, teachers, Stampli, Thailand accelerator, Cursor, loveholidays, Admin plugin, and the Enterprise Signals write-up all stayed out of today’s bucket on date alone.",
            "Reopened the in-window OpenAI Astra and healthcare URLs at body level. The current sitemap appearances did not add a new first-hand state change beyond the already-selected same-day cards, so they were treated as checked duplicates rather than new events.",
            "Promoted one new signal after body review: Codex 0.153.0. The stable release moved remote plugin marketplaces, approval-mode Guardian behavior, account-scoped MCP approvals, review-history persistence, and experimental context management into the visible control plane. The same-day alpha tag was merged as prerelease context instead of becoming a second card.",
            "Left the California youth-safety bill page out because it is a company policy endorsement for a bill not yet in force, not a completed structural policy change."
        ],
        "collection_contract": {
            "raw_candidates_in_rolling_window_is_not_increment": True,
            "candidate_queue_count_is_not_new_count": True,
            "sitemap_lastmod_is_not_publication_date": True,
            "feed_titles_require_body_verification": True,
            "http_2xx_is_not_checked_no_match": True,
        },
    }

    dump(day / "selected.json", selected)
    dump(day / "citation-ledger.json", ledger)
    dump(day / "citations.json", citations)
    dump(day / "daily-brief.md", brief)
    dump(day / "run-summary.json", run_summary)
    dump(topics_path, topics_payload)

    print(json.dumps({
        "date": DATE,
        "signals": len(selected),
        "topics": len(topics),
        "run_summary": str(day / "run-summary.json"),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
