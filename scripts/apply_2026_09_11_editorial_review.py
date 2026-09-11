#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-11"
RUN_AT = "2026-09-11T16:11:31+08:00"


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


signal = {
    "id": "2026-09-10-google-adk-python-2-9-resilience-resume",
    "demo": False,
    "topic_lane": "agent_architecture",
    "title": "Google ADK 2.9.0 加入模型自动故障转移，但恢复失败节点可能重复外部动作",
    "summary": "Google ADK Python 2.9.0 正式加入 FallbackModel，可在主模型报错时自动切换备用模型；同时新增 LiveKit 语音与电话 runner、YAML 图工作流、MCP SDK 2.x 兼容和 OTLP 日志导出。更值得注意的是恢复语义变化：失败节点现在会重新执行，若节点在报错前已产生外部副作用，恢复后可能再次执行，因此官方明确要求节点逻辑具备幂等性。版本还把 GCS 工具的本地文件访问限制在 local_file_root 内，未配置时直接拒绝。",
    "decision": "include",
    "confidence": 96,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "technical_update",
    "information_type": "agent_runtime",
    "evidence_level": "confirmed",
    "source": "Google Agent Development Kit",
    "url": "https://github.com/google/adk-python/releases/tag/v2.9.0",
    "published_at": "2026-09-10T21:22:43Z",
    "primary_tags": ["Google ADK", "FallbackModel", "Workflow Resume"],
    "secondary_tags": ["Idempotency", "LiveKit", "MCP 2.x", "OTLP"],
    "why_it_matters_cn": "这版把可用性、任务恢复和副作用风险放进同一个运行时问题里。模型自动切换能减少中断，但工作流恢复如果没有幂等设计，可能把一次失败变成重复扣款、重复发信或重复写入。",
    "personal_relevance_cn": "评估 Agent 框架时，不能只问有没有 retry 和 failover。还要核对重放边界、幂等键、外部动作日志、人工确认点，以及恢复时到底重跑哪个节点。",
    "product_opportunity_cn": "可把模型故障转移记录、节点 checkpoint、副作用幂等键、恢复预览和人工批准做成统一控制面，并允许按动作风险设置自动恢复或停下等待。",
    "competitive_risk_cn": "Release 证明代码和语义已进入正式版本，但没有给出生产故障转移成功率、切换策略、成本上限或重复副作用的自动检测与补偿机制。",
    "recommended_action": "investigate",
    "questions_to_validate": [
        "FallbackModel 按什么错误类型和顺序切换，是否支持预算、延迟与区域约束？",
        "失败节点恢复时是否有稳定 execution ID、幂等键或补偿事务，谁负责阻止重复外部动作？",
        "OTLP 日志能否串起主模型失败、备用模型接管、HITL 暂停和恢复后的完整链路？",
    ],
    "follow_up_triggers": [
        "Google 发布 FallbackModel 的生产指标、策略配置或故障复盘",
        "ADK 增加副作用检测、幂等键、补偿事务或恢复前预览",
        "YAML 图工作流和 LiveKit runner 出现权限、审计或暂停恢复文档",
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
        "macro_value": 2,
        "actionability": 5,
    },
    "report_date": DATE,
    "event_date": "2026-09-10",
    "canonical_url": "https://github.com/google/adk-python/releases/tag/v2.9.0",
    "first_seen_date": DATE,
    "last_seen_date": DATE,
    "run_dates": [DATE],
    "evidence_boundary": "GitHub Release 页面和 API 确认 v2.9.0 于 2026-09-10T21:22:43Z 发布，正文明确列出自动模型故障转移、恢复语义、路径限制、LiveKit、YAML 工作流、MCP 2.x 与 OTLP 日志。生产可靠性、成本和补偿机制没有公开数据。",
    "related_sources": [
        {"url": "https://github.com/google/adk-python/commit/c300b8ded62b8bc4168cdede4c85bec66d1aa8ee", "type": "fallback_model_commit"},
        {"url": "https://github.com/google/adk-python/commit/2fb877cd0ea5f866d2b66153b00749ebb61bdce4", "type": "workflow_resume_commit"},
        {"url": "https://github.com/google/adk-python/commit/6d145180611956b2065704189517fd6a0ff1a063", "type": "nested_hitl_commit"},
    ],
}

rows = [signal]
ledger = {
    "version": 1,
    "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
    "sources": [
        {
            "id": 1,
            "title": "Google Agent Development Kit Python v2.9.0",
            "url": signal["canonical_url"],
            "publisher": "Google / GitHub",
            "evidence_level": "confirmed",
            "accessed": RUN_AT,
        }
    ],
}
citations = [{"id": 1, "url": signal["canonical_url"]}]

brief = f'''# AI Signal 日报｜{DATE}

**窗口：** 本轮只审核跨轮新增的 10 个候选；发现时间覆盖滚动 80 小时，正式判断以北京时间当日增量和一手发布日期为准。  
**一句话结论：** 新增 1 条正式 Signal。Google ADK Python 2.9.0 补上模型自动故障转移，却也把一个容易被忽略的恢复风险写进正式 Release：失败节点会重跑，外部副作用如果不幂等，恢复可能造成重复执行。[1]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | OpenAI Astra 新页面属于既有发布主题，且独立发布日期未从一手页面恢复，不重复建卡 |
| Agent 架构 | 1 | ADK 2.9.0 同时更新故障转移、恢复语义、HITL、路径限制和遥测 |
| AI 产品 | 0 | 4 个 OpenAI 客户故事的正文日期均早于本轮，不伪装成今日产品增量 |
| AI 宏观 | 0 | Election safeguards 页面没有恢复可用的一手 datePublished，sitemap lastmod 不作发布日期 |

## 模型｜0 条

GPT-6 Astra 的两个页面能读到正式正文，但内容仍属于 9 月 3 日已收录的 Astra 发布与治理事件。其中 business 页面增加企业管理员控制、确认策略和自动审查等说明，但页面没有恢复可核验的一手 datePublished；本轮先留在 `candidate_only`，不靠 sitemap lastmod 制造新事件。

## Agent 架构｜1 条

### Google ADK 2.9.0：自动切备用模型之后，恢复语义成了更大的坑

Google ADK Python 2.9.0 于北京时间 9 月 11 日 05:22 发布。版本加入 `FallbackModel`，主模型报错时可自动切到备用模型；还新增 LiveKit runner、YAML 图工作流、MCP SDK 2.x 兼容，以及向 Google telemetry endpoint 导出 OTLP 日志的能力。[1]

更值得产品和架构团队注意的是 breaking change。工作流恢复时，失败节点现在会重新执行，而不是像之前那样按已完成节点回放。官方直接提醒：如果节点先完成了外部副作用再报错，每次恢复都可能再次执行，所以节点体必须幂等。GCS 工具的本地文件访问也被收紧到 `local_file_root`，没有配置就拒绝访问。[1]

**为什么重要：** failover 解决的是模型不可用，恢复语义处理的是任务执行到一半后该从哪里接着跑。两者如果没有稳定 execution ID、幂等键和补偿机制，系统看上去更“自动恢复”，实际可能更容易重复扣款、发信或写数据。

**建议动作：** 把 ADK 2.9.0 加入 Agent runtime 评测：模拟主模型失败、节点完成外部动作后报错、HITL 暂停与恢复，核对日志能否串起切换和重放，并验证高风险动作是否能在恢复前强制人工确认。

## AI 产品｜0 条

CRED、Model ML、John Deere 和 Speak 页面都能恢复正文与页面日期，但分别发表于 2025 年 11 月、7 月、5 月和4 月。它们是 sitemap 重写或 lastmod 噪声，不是本轮新增。

## AI 宏观｜0 条

Election safeguards 正文可读，但一手页面日期没有恢复。搜索摘要和 sitemap lastmod 只保留为发现线索，不升级为正式事件。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新的模型负责人原创内容达到主题与信息增量门槛。

## AI 一线实践者观点｜0 条

本轮没有新的实践者原创内容达到正式入选门槛。

## 审核但未入选

- OpenAI Codex 两个 alpha tag 只有版本号或空白 Release 文案，没有可解释的功能、工作流或边界变化；其中 `alpha.3.6` 的 Release API 已返回 404。
- GPT-6 Astra 两个页面并入既有事件判断，不新建重复卡；business 页面缺少一手发布日期，暂不做跨日证据升级。
- OpenAI Election safeguards 页面缺少可核验的一手发布日期，保持 `candidate_only`。
- 4 个 OpenAI 客户故事有完整正文，但页面日期都在 2025 年，按静态页噪声排除。

## 证据边界

- ADK 的发布、功能和 breaking change 由官方 GitHub Release 确认；生产切换成功率、成本和自动补偿能力没有公开证据。[1]
- OpenAI 页面正文可访问不等于本轮新发布。没有一手 `datePublished` 时，本轮不把 sitemap lastmod 当作事件时间。

## 飞书短版

**一句话结论：** 本轮 10 个真新增候选完成正文核验，新增 1 条正式 Signal：Google ADK 2.9.0 加入模型自动故障转移，但失败节点恢复会重跑，外部动作必须幂等。  
**个人判断：** Agent runtime 的可靠性不能只看 retry/failover，还要看 checkpoint、幂等键、补偿事务和恢复前审批。  
**建议动作：** 用一次“外部动作已成功、节点随后报错”的故障注入，检查恢复是否重复执行以及日志能否完整追踪。  
**结果：** previous_count=0，new_count=1，updated_count=0，total_count=1。

## Sources

[1] {signal["canonical_url"]}
'''

topic = {
    "id": "2026-09-11-google-adk-resume-idempotency",
    "status": "candidate",
    "timeliness": "today",
    "priority": "A",
    "topic_lane": "agent_architecture",
    "source_signal_ids": [signal["id"]],
    "working_title_cn": "Agent 会自动恢复，不代表业务动作不会执行两次",
    "core_tension_cn": "模型 failover 提高了可用性，但失败节点重跑会把幂等、补偿和审批变成产品级问题。",
    "why_now_cn": "Google ADK 2.9.0 同时发布自动模型故障转移和新的工作流恢复语义，并明确提醒外部副作用可能重复执行。",
    "target_audience_cn": ["Agent 产品经理", "Agent 平台工程师", "企业自动化负责人"],
    "evidence_boundary_cn": "正式 Release 已确认语义变化；生产故障率、成本与补偿效果没有公开数据。",
    "source_urls": [signal["canonical_url"]],
    "platforms": {
        "xiaohongshu": {
            "title": "Agent 自动恢复后，为什么可能扣两次钱？",
            "hook": "Google ADK 2.9.0 的 breaking change 把一个真实风险写明了：失败节点会重跑，外部动作不幂等就可能重复执行。",
            "format": "7页图文卡",
            "outline": ["版本变化", "故障转移流程", "失败节点重跑", "重复副作用案例", "幂等与审批清单"],
            "visual_direction": "主模型失败到备用模型接管、节点重放与外部副作用的时序图",
            "cta": "你的 Agent 恢复前会检查幂等键吗？",
        },
        "twitter": {
            "title": "Agent failover is not enough: resumed nodes can repeat side effects",
            "hook": "Google ADK 2.9.0 adds automatic model failover, but its resume semantics expose the harder problem: a failed node may run again after an external action already succeeded.",
            "format": "6帖 Thread",
            "outline": ["Release fact", "Failover path", "Replay boundary", "Side-effect failure case", "Control checklist"],
            "visual_direction": "Failover and replay sequence diagram",
            "cta": "Where do you enforce idempotency in your agent runtime?",
        },
        "wechat": {
            "title": "Agent 自动恢复之后，谁来保证业务动作不会执行两次",
            "hook": "Google ADK 2.9.0 同时带来模型 failover 和节点重跑语义，可靠性问题已经从“能不能恢复”转到“恢复后会不会重复执行”。",
            "format": "1800—2400字分析",
            "outline": ["版本事实", "模型故障转移", "checkpoint 与重放语义", "幂等、补偿与人工审批", "故障注入测试清单"],
            "visual_direction": "恢复语义架构图，附风险动作测试表",
            "cta": "先挑一个高风险动作，做一次恢复故障注入。",
        },
    },
}
topics_payload = {
    "schema_version": 1,
    "report_date": DATE,
    "timezone": "Asia/Shanghai",
    "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。自动流程只生成 candidate，不自动发布。",
    "scope_label_cn": f"当日增量 · {DATE}",
    "source_scope": {"type": "daily", "date": DATE},
    "topics": [topic],
}

reviews = [
    {"url": signal["canonical_url"], "decision": "selected", "signal_id": signal["id"], "published_at": signal["published_at"], "reason": "official release body confirms material agent-runtime changes and breaking resume semantics"},
    {"url": "https://github.com/openai/codex/releases/tag/rust-v0.155.0-alpha.3.7", "decision": "exclude", "reason": "official release contains only the version label; no substantive body or workflow delta"},
    {"url": "https://github.com/openai/codex/releases/tag/rust-v0.155.0-alpha.3.6", "decision": "exclude", "reason": "release body is empty and the tag-specific GitHub Release API returned 404"},
    {"url": "https://openai.com/index/election-safeguards-2026", "decision": "candidate_only", "reason": "official body was retrieved but first-party datePublished was not recovered; sitemap lastmod is discovery-only"},
    {"url": "https://openai.com/index/gpt-6-astra-next-generation-work", "decision": "candidate_only", "reason": "same Astra launch theme as an existing event; official body adds controls but first-party datePublished was not recovered"},
    {"url": "https://openai.com/index/gpt-6-astra", "decision": "duplicate_existing", "reason": "same release and governance event already stored as 2026-09-03-openai-gpt6-astra-broad-release-monitorability"},
    {"url": "https://openai.com/index/cred-swamy-seetharaman", "decision": "exclude_outside_window", "published_at": "2025-11-05", "reason": "old customer story surfaced by sitemap lastmod"},
    {"url": "https://openai.com/index/model-ml-chaz-englander", "decision": "exclude_outside_window", "published_at": "2025-07-23", "reason": "old customer story surfaced by sitemap lastmod"},
    {"url": "https://openai.com/index/john-deere-justin-rose", "decision": "exclude_outside_window", "published_at": "2025-05-06", "reason": "old customer story surfaced by sitemap lastmod"},
    {"url": "https://openai.com/index/speak-connor-zwick", "decision": "exclude_outside_window", "published_at": "2025-04-22", "reason": "old customer story surfaced by sitemap lastmod"},
]


def update_summary(summary: dict) -> dict:
    summary = deepcopy(summary)
    summary.update({
        "run_at": RUN_AT,
        "deliverable_outcome": "success",
        "scheduler_outcome": "success",
        "editorial_shortlist": 10,
        "previous_count": 0,
        "new_count": 1,
        "updated_count": 0,
        "excluded_count": 9,
        "candidate_queue_count": 274,
        "new_in_run_count": 10,
        "unreviewed_candidate_count": 274,
        "total_count": 1,
        "selected": 1,
        "lane_counts": {"model": 0, "agent_architecture": 1, "ai_product": 0, "ai_macro": 0},
        "priority_counts": {"P0": 0, "P1": 1, "P2": 0, "P3": 0},
        "executive_model_longform": 0,
        "practitioner_statements": 0,
        "cross_day_duplicates_removed": 1,
        "candidate_reviews": reviews,
        "content_topics": {"topic_count": 1, "platform_variants": 3},
        "notes": [
            "Only the 10 cross-run new candidates were reviewed; the 274-item standing queue was not rescanned.",
            "One official Google ADK release passed the body, date, relevance, and event-deduplication gates.",
            "OpenAI sitemap lastmod values were kept as discovery metadata and were not used as publication dates.",
            "The Astra pages were not turned into duplicate cards; one remains candidate_only pending a first-party publication date.",
        ],
    })
    coverage = summary.get("source_coverage", {})
    records = coverage.get("records", [])
    for record in records:
        if record.get("name") == "Google Agent Development Kit":
            record.update({
                "status": "selected",
                "http_code": "200",
                "final_url": signal["canonical_url"],
                "note": "v2.9.0 release timestamp and body verified through the official GitHub Release page/API",
            })
    statuses = ["selected", "candidate_only", "checked_no_match", "access_blocked", "auth_required", "mechanical_failure", "not_checked"]
    counts = Counter(r.get("status") for r in records)
    coverage["status_counts"] = {s: counts.get(s, 0) for s in statuses}
    channels = {}
    for channel in sorted({r.get("channel") for r in records}):
        subset = Counter(r.get("status") for r in records if r.get("channel") == channel)
        channels[channel] = {s: subset.get(s, 0) for s in statuses}
    coverage["channel_counts"] = channels
    coverage["registered"] = len(records)
    summary["source_coverage"] = coverage
    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "Google Agent Development Kit releases":
            probe.update({"status": "selected", "note": "v2.9.0 official release body and timestamp verified; one formal signal selected"})
        elif probe.get("name") == "OpenAI Codex releases":
            probe.update({"status": "checked_no_match", "note": "the two cross-run new alpha tags had no substantive release body"})
        elif probe.get("name") == "OpenAI sitemap":
            probe.update({"status": "candidate_only", "note": "new sitemap hits were body-reviewed; missing first-party dates, old page dates, and duplicate Astra pages were not promoted"})
    return summary


day = ROOT / "daily" / DATE
dump(day / "selected.json", rows)
dump(day / "citation-ledger.json", ledger)
dump(day / "citations.json", citations)
dump(day / "daily-brief.md", brief)
for name in ("run-summary.json", "collection-run-summary.json"):
    path = day / name
    dump(path, update_summary(json.loads(path.read_text())))
dump(ROOT / "content-topics" / DATE / "topics.json", topics_payload)

print(json.dumps({
    "date": DATE,
    "reviewed_new_candidates": len(reviews),
    "selected": len(rows),
    "excluded_or_deferred": len(reviews) - len(rows),
    "topics": len(topics_payload["topics"]),
    "platform_variants": len(topics_payload["topics"]) * 3,
}, ensure_ascii=False))
