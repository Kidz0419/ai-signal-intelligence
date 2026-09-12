#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-12"
RUN_AT = "2026-09-12T20:03:58+08:00"

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
    {
        "id": 5,
        "title": "1Password increases engineering productivity 21% with Codex",
        "url": "https://openai.com/index/1password",
        "publisher": "OpenAI / 1Password",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT,
    },
    {
        "id": 6,
        "title": "Supporting independent journalism in Ukraine",
        "url": "https://openai.com/index/supporting-independent-journalism-in-ukraine",
        "publisher": "OpenAI / WAN-IFRA / AIRPPU",
        "evidence_level": "confirmed",
        "accessed": RUN_AT,
    },
]

SIGNAL = {
    "id": "2026-09-08-1password-codex-secure-engineering-workflow",
    "demo": False,
    "topic_lane": "ai_product",
    "title": "1Password 把 Codex 接进研发全链路：密钥只在动作点注入，外部动作仍交给工程团队",
    "summary": "OpenAI 9 月 8 日发布的 1Password 客户案例，披露了 Codex 从需求拆解、跨栈实现、PR 预审、测试到生产故障调查的完整用法。1Password 让 Codex 先产出功能规格和接近完成的前端原型，再交给系统工程师接后端；调用获批内部工具时，系统只在动作点解析并注入凭据，明文不进入模型上下文。案例还给出 50 名持续使用者的内部测量和估算：生产率提升 20.9%，PR 周期中位数缩短 10.9%，年度工程产能价值约 78.4 万美元。数字均为 1Password 测量或建模，不是独立评测。",
    "decision": "include",
    "confidence": 89,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "analysis",
    "information_type": "product_workflow",
    "evidence_level": "primary_statement",
    "source": "OpenAI / 1Password",
    "url": "https://openai.com/index/1password",
    "published_at": "2026-09-08",
    "primary_tags": ["1Password", "OpenAI Codex", "Secure Engineering Workflow"],
    "secondary_tags": ["Secret Injection", "AppSec Skills", "Human Review", "Enterprise Adoption"],
    "why_it_matters_cn": "这份案例最有用的不是 ROI 大数字，而是把企业 coding agent 的边界写得比较实：模型可以拆需求、并行写代码、预审和跑测试，但后端落地仍有人接手；凭据按调用注入，不直接放进仓库或模型上下文；安全政策被做成可复用 AppSec skills。",
    "personal_relevance_cn": "评估企业 Agent 或 AI 编程产品时，可以直接追问四件事：凭据在哪个动作点解析，哪些工具需要事先批准，原型到生产由谁接手，以及 PR、测试、故障调查是否共享同一条可审计链路。",
    "product_opportunity_cn": "可以把 secret reference、按动作注入、获批工具目录、AppSec skill、人工交接点和产能测量做成企业 coding agent 的标准控制面，而不是把安全要求留在 prompt 或团队约定里。",
    "competitive_risk_cn": "页面没有展示管理员 UI、权限字段、执行日志、暂停、回滚或异常凭据处理流程。生产率与 ROI 来自厂商客户案例，且 ROI 模型依赖 40% Codex 归因和 75% 产能兑现等假设，不能外推为普遍效果。",
    "recommended_action": "investigate",
    "questions_to_validate": [
        "获批内部工具由谁配置，是否支持按仓库、环境、动作风险和时间窗口收紧授权？",
        "凭据在动作点注入后，调用日志是否能记录主体、工具、资源、结果和撤销状态，同时避免泄露明文？",
        "从近完成原型交给系统工程师后，哪些修改必须重新跑 AppSec、测试和人工批准？",
        "20.9% 生产率提升的口径如何定义，是否控制了任务难度、团队差异和选择偏差？",
    ],
    "follow_up_triggers": [
        "1Password 或 OpenAI 公布管理员界面、工具授权字段、审计日志或凭据注入架构",
        "1Password 披露内部 SRE agent 或 Knox 的失败复盘、暂停恢复和回滚流程",
        "第三方复现 PR 周期、生产率或 ROI 结果，或公开更完整的测量方法",
    ],
    "scores": {
        "topic_relevance": 5,
        "novelty": 4,
        "technical_or_product_significance": 4,
        "strategic_value": 4,
        "source_quality": 4,
        "model_value": 2,
        "agent_architecture_value": 4,
        "ai_product_value": 5,
        "macro_value": 2,
        "actionability": 5,
    },
    "report_date": DATE,
    "event_date": "2026-09-08",
    "canonical_url": "https://openai.com/index/1password",
    "first_seen_date": DATE,
    "last_seen_date": DATE,
    "run_dates": [DATE],
    "evidence_boundary": "一手页面明确标注 2026 年 9 月 8 日，并给出 1Password 的工作流、人工交接、凭据注入方式和内部测量。上线状态与效果来自 OpenAI 和 1Password 自述；页面没有真实管理员 UI、权限配置、审计日志、暂停或回滚证据。页面在 9 月 12 日因 sitemap lastmod 再次进入增量队列，本条按真实 event_date 作为 catch-up，不写成今日发布。",
    "related_sources": [],
}

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
    {
        "url": SOURCES[4]["url"],
        "decision": "selected_catch_up",
        "signal_id": SIGNAL["id"],
        "published_at": SIGNAL["published_at"],
        "reason": "the first-party case study gives a complete engineering workflow, credential-handling boundary, human handoff, and explicitly attributed measurement assumptions",
    },
    {
        "url": SOURCES[5]["url"],
        "decision": "exclude_below_formal_bar",
        "published_at": "2026-09-07",
        "reason": "the official body confirms a training and pilot programme but discloses no distinct product mechanism, operating control, measured adoption result, or structural market change",
    },
]

TOPICS = {
    "schema_version": 1,
    "report_date": DATE,
    "timezone": "Asia/Shanghai",
    "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。自动流程只生成 candidate，不自动发布。",
    "scope_label_cn": f"当日增量 · {DATE}",
    "source_scope": {"type": "daily", "date": DATE},
    "topics": [
        {
            "id": "2026-09-12-coding-agent-secret-injection-control-plane",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "ai_product",
            "source_signal_ids": [SIGNAL["id"]],
            "working_title_cn": "企业 Coding Agent 的安全边界，不该只写在 Prompt 里",
            "core_tension_cn": "Agent 要深入研发链路才能产生价值，但凭据、工具授权和生产交接不能跟着自动化一起失控。",
            "why_now_cn": "1Password 首次公开了 Codex 覆盖需求、实现、PR、测试和故障调查的用法，也写明凭据只在获批工具调用的动作点注入。",
            "target_audience_cn": ["AI 产品经理", "企业开发平台负责人", "Agent 安全与治理团队"],
            "evidence_boundary_cn": "工作流和内部测量来自 OpenAI 与 1Password 客户案例；没有真实管理员 UI、审计日志、暂停和回滚证据，ROI 也不是独立评测。",
            "source_urls": [SIGNAL["canonical_url"]],
            "platforms": {
                "xiaohongshu": {
                    "title": "AI 写代码可以，凭什么拿到你的生产密钥？",
                    "hook": "1Password 把 Codex 接进整条研发链路，但明文凭据不进模型上下文，只在获批工具真正执行时注入。",
                    "format": "8页图文卡",
                    "outline": ["完整研发链路", "模型能自动做什么", "人工在哪里接手", "secret reference 怎么工作", "AppSec skill 的位置", "缺失的日志与回滚证据", "企业评估清单"],
                    "visual_direction": "从需求到生产的泳道图，标出凭据注入点和人工交接点",
                    "cta": "你的 Agent 在哪个动作点才拿到凭据？",
                },
                "twitter": {
                    "title": "The useful part of 1Password's Codex case is secret injection, not the ROI headline",
                    "hook": "Codex spans planning, implementation, review, testing, and incident investigation at 1Password. Plaintext credentials stay out of model context and are injected only when an approved tool acts.",
                    "format": "7帖 Thread",
                    "outline": ["case-study boundary", "workflow map", "human handoff", "secret references", "AppSec skills", "self-reported metrics", "missing controls"],
                    "visual_direction": "tool-call authorization and secret-injection sequence diagram",
                    "cta": "Where does your coding agent receive credentials, and who can revoke them?",
                },
                "wechat": {
                    "title": "Coding Agent 进入企业研发链路后，凭据、工具和人审应该怎么分层",
                    "hook": "1Password 的案例给出了一条可拆解的企业路径：Agent 覆盖研发全链路，但凭据按动作注入，后端生产落地仍交给工程师。",
                    "format": "2000—2600字分析",
                    "outline": ["案例事实与自报边界", "研发工作流拆解", "凭据按动作注入", "AppSec skill 与工具授权", "人工交接和责任链", "日志、暂停、回滚缺口", "企业控制面清单"],
                    "visual_direction": "对象—动作—凭据—审批—日志矩阵",
                    "cta": "附一份企业 Coding Agent 上线前核对表。",
                },
            },
        }
    ],
}


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def source_block() -> str:
    return "\n".join(f'[{source["id"]}] {source["url"]}' for source in SOURCES)


def build_brief() -> str:
    return f'''# AI Signal 日报｜{DATE}

**窗口：** 20:00 增量只核验新出现的 2 个候选；当天累计核验 6 个跨轮新增候选。发现窗口截至北京时间 2026-09-12 20:00，正式判断使用一手页面日期，不使用 sitemap `lastmod` 代替发布时间。  
**一句话结论：** 新增 1 条 catch-up Signal。1Password 的 Codex 案例发表于 9 月 8 日，今天因 sitemap 更新再次进入队列；正文提供了从需求到生产的完整研发链路、人工交接和按动作注入凭据的边界。乌克兰新闻业合作项目没有达到正式门槛。[5][6]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 两个 Astra 页面继续并入 9 月 3 日既有发布事件，不重复建卡 |
| Agent 架构 | 0 | 1Password 案例有工具授权与凭据边界，但主事件是企业研发工作流 |
| AI 产品 | 1 | 1Password 把 Codex 用到规划、实现、PR、测试和故障调查，密钥只在获批工具执行时注入 |
| AI 宏观 | 0 | 新闻业培训合作没有形成新的产业结构变化 |

## 模型｜0 条

GPT-6 Astra 主发布页与企业工作页仍属于 9 月 3 日已入库事件。企业页虽补充白名单、上传下载、浏览历史、确认策略和自动审查，但没有独立发布日期或新的上线状态，本轮不拆卡。[2][3]

## Agent 架构｜0 条

1Password 案例涉及获批工具、secret reference、AppSec skill 和人工交接，但没有公开管理员权限字段、执行日志、暂停、恢复或回滚机制。它更适合作为企业 AI 产品工作流案例，而不是新的 Agent runtime 发布。[5]

## AI 产品｜1 条

### Catch-up｜1Password 把 Codex 接进研发全链路，凭据只在动作点出现

这篇客户案例标注 9 月 8 日。1Password 称，Codex 已用于需求拆解、依赖检查、跨 Rust 和 TypeScript 实现、PR 预审、测试，以及跨事故管理、遥测、源码、值班和 feature flag 的生产调查。前端原型接近完成后仍交给系统工程师接后端，PR 也保留人工审查。[5]

凭据处理比 ROI 标题更值得看。仓库只存 secret reference；Codex 调用获批内部工具时，1Password 才解析并注入凭据，因此明文不会进入模型上下文。团队还把安全政策做成可复用 AppSec skills，让检查跟着研发流程走。[5]

1Password 报告核心使用群体的生产率提升 20.9%，PR 周期中位数缩短 10.9%。约 78.4 万美元年度产能价值和 553% ROI 都是模型估算，假设包括 50 名持续使用者、40% 的 Codex 归因和 75% 的产能兑现。这些数字来自厂商与客户自报，不能当成独立效果评测。[5]

**为什么重要：** 企业 coding agent 的边界开始从抽象安全原则落到具体动作：仓库里放引用，不放明文；工具先获批，执行时再拿凭据；Agent 做到近完成原型，生产后端仍有人接手。

**建议动作：** 用这条链路检查现有 Agent 控制面：谁能批准工具，凭据按什么范围注入，调用是否有不泄密的审计记录，异常动作能否暂停和撤销，人工接手后是否强制重跑 AppSec 与测试。

## AI 宏观｜0 条

OpenAI、WAN-IFRA 与 AIRPPU 的页面标注 9 月 7 日，确认了面向乌克兰独立新闻机构的培训、实施路线图、10 家机构试点和 API credits。它是采用支持项目，但正文没有新的产品机制、运行控制、量化结果或足以改变 AI 产业结构的变化，因此不入正式 Signal。[6]

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新的模型负责人原创内容达到主题与信息增量门槛。

## AI 一线实践者观点｜0 条

本轮没有新的实践者原创内容达到正式入选门槛。

## 审核但未入选

- Election safeguards：正文日期是 5 月 27 日；重复 sitemap `lastmod` 没有证明正文发生可报道更新。[1]
- GPT-6 Astra 两个页面：继续归入历史事件 `2026-09-03-openai-gpt6-astra-broad-release-monitorability`。[2][3]
- Paul Christiano 任命：页面日期为 9 月 9 日，但正文没有披露委员会权力、审批流程或运行控制发生变化。[4]
- 乌克兰新闻业项目：合作和试点已确认，信息仍停留在培训、路线图与 API credits，没有通过产品或宏观门槛。[6]

## 证据边界

- 1Password 的日期、工作流、人工交接与凭据处理来自一手页面；生产率和 ROI 是 1Password 测量或建模，并由 OpenAI 客户案例发布，不是独立审计。[5]
- 两个新候选都来自 sitemap `lastmod` 变化，但 `lastmod` 只负责发现。1Password 以页面真实日期作为 9 月 8 日 catch-up，乌克兰项目也保留 9 月 7 日事件日期。[5][6]
- OpenAI 普通抓取路径仍返回 403；本轮通过可读取的一手页面正文 fallback 完成核验，阻断没有被写成无内容。

## 飞书短版

**一句话结论：** 20:00 的 2 个真新增候选完成正文核验，补入 1 条 9 月 8 日 catch-up Signal。  
**重点：** 1Password 已把 Codex 用到规划、实现、PR、测试和故障调查；仓库只存 secret reference，获批工具执行时才注入凭据，生产后端仍由工程师接手。[5]  
**边界：** 20.9% 生产率提升、10.9% PR 周期缩短和 553% ROI 都是厂商/客户自报或建模；没有管理员 UI、审计日志、暂停和回滚证据。  
**建议动作：** 按“工具批准—凭据注入—人工交接—审计—撤销”检查企业 Coding Agent 的控制面。  
**结果：** previous_count=0，new_count=1，updated_count=0，total_count=1。

## Sources

{source_block()}
'''


def update_summary(original: dict) -> dict:
    summary = deepcopy(original)
    summary.update(
        {
            "run_type": "daily_four_lane_incremental_editorial_review",
            "run_at": RUN_AT,
            "deliverable_outcome": "success",
            "scheduler_outcome": "success",
            "editorial_shortlist": 2,
            "reviewed_new_candidates": 2,
            "day_reviewed_candidates_total": 6,
            "previous_count": 0,
            "new_count": 1,
            "updated_count": 0,
            "excluded_count": 1,
            "candidate_queue_count": 210,
            "new_in_run_count": 2,
            "unreviewed_candidate_count": 210,
            "total_count": 1,
            "selected": 1,
            "lane_counts": {"model": 0, "agent_architecture": 0, "ai_product": 1, "ai_macro": 0},
            "priority_counts": {"P0": 0, "P1": 1, "P2": 0, "P3": 0},
            "executive_model_longform": 0,
            "practitioner_statements": 0,
            "cross_day_duplicates_removed": 2,
            "candidate_reviews": REVIEWS,
            "content_topics": {"topic_count": 1, "platform_variants": 3},
            "collection_contract": {
                "raw_candidates_in_rolling_window_is_not_increment": True,
                "candidate_queue_count_is_not_new_count": True,
                "sitemap_lastmod_is_not_publication_date": True,
                "feed_titles_require_body_verification": True,
                "http_2xx_is_not_checked_no_match": True,
            },
            "notes": [
                "Only the 2 cross-run new candidates from the 20:00 cycle were reviewed; the 210-item standing queue was not rescanned.",
                "Both candidates came from OpenAI sitemap lastmod changes and were opened at the first-party article URL through the available public-text fallback.",
                "The 1Password case was selected as a September 8 catch-up because its body adds a complete engineering workflow, credential injection boundary, human handoff, and attributed measurement assumptions.",
                "The Ukrainian newsroom programme was excluded below the formal bar: the official body confirms training and pilots, not a distinct product mechanism, measured result, or structural market change.",
                "The four candidates from the earlier same-day review remain in candidate_reviews for daily audit continuity.",
            ],
        }
    )
    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "OpenAI sitemap":
            probe.update(
                {
                    "status": "candidate_only",
                    "note": "the 2 cross-run lastmod changes were body-reviewed; one September 8 catch-up signal was selected and one partnership programme was excluded below the formal bar",
                }
            )
    return summary


def main() -> None:
    day = ROOT / "daily" / DATE
    dump(day / "selected.json", [SIGNAL])
    dump(
        day / "citation-ledger.json",
        {
            "version": 1,
            "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
            "sources": SOURCES,
        },
    )
    dump(day / "citations.json", [{"id": source["id"], "url": source["url"]} for source in SOURCES])
    dump(day / "daily-brief.md", build_brief())
    for name in ("run-summary.json", "collection-run-summary.json"):
        path = day / name
        dump(path, update_summary(json.loads(path.read_text())))
    dump(ROOT / "content-topics" / DATE / "topics.json", TOPICS)
    print(
        json.dumps(
            {
                "date": DATE,
                "reviewed_new_candidates": 2,
                "selected": 1,
                "excluded": 1,
                "citations": len(SOURCES),
                "topics": 1,
                "platform_variants": 3,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
