#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-14"
RUN_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
DAY = ROOT / "daily" / DATE

SIGNAL_ID = "2026-09-14-kimi-code-043-dynamic-tools-steering-controls"
KIMI_RELEASE = "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.43.0"
KIMI_ATOM = "https://github.com/MoonshotAI/kimi-code/releases.atom"
PR_DYNAMIC_TOOLS = "https://github.com/MoonshotAI/kimi-code/pull/3667"
PR_STEERING = "https://github.com/MoonshotAI/kimi-code/pull/3697"
PR_COMPACTION = "https://github.com/MoonshotAI/kimi-code/pull/3750"
PR_PERMISSION_REMINDER = "https://github.com/MoonshotAI/kimi-code/pull/3728"
PR_TMP_GUARD = "https://github.com/MoonshotAI/kimi-code/pull/3714"
CODEX_RELEASE = "https://github.com/openai/codex/releases/tag/rust-v0.155.0-alpha.4"
FYXER = "https://openai.com/index/fyxer"
OPENAI_RSS = "https://openai.com/news/rss.xml"
FYXER_VIDEO = "https://www.youtube.com/watch?v=uA5PiAXKGis"

SIGNAL = {
    "id": SIGNAL_ID,
    "demo": False,
    "topic_lane": "agent_architecture",
    "title": "Kimi Code 0.43 把 MCP 工具改成按需披露，并让人工指令打断后台等待",
    "summary": "Kimi Code 0.43.0 的正式 Release 补上了两段控制链路。模型声明支持动态工具后，MCP server 可显式设为 `deferred: true`，不再把全部工具 schema 固定塞进顶层工具列表，而由实验性的 `select_tools` 按需加载；默认仍是 inline，`disallowedTools` 仍可否决。另一项更新让用户 steering 消息以非错误结果中断 `WaitFor`，保留工具历史且不终止后台任务。版本还开放 compaction 最大尝试次数，并细化权限提示与临时目录删除确认边界。",
    "decision": "include",
    "confidence": 94,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "technical_update",
    "information_type": "agent_governance",
    "evidence_level": "confirmed",
    "source": "MoonshotAI / Kimi Code",
    "url": KIMI_RELEASE,
    "published_at": "2026-09-14T12:03:30Z",
    "primary_tags": ["Kimi Code", "Dynamic Tool Loading", "Human Steering"],
    "secondary_tags": ["MCP Deferred Disclosure", "Context Compaction", "Permission Guard"],
    "why_it_matters_cn": "这次更新处理的不是工具数量本身，而是工具何时进入模型上下文、人工指令何时能抢回控制、后台任务是否继续，以及重试和确认由谁配置。Agent 控制面开始从单一权限模式拆成可组合的运行时策略。",
    "personal_relevance_cn": "评估 Agent 平台时，可把工具披露、人工 steering、后台任务生命周期、压缩重试和命令确认分开验收。尤其要检查默认值、覆盖优先级、事件日志，以及“打断等待”是否被误解成“取消任务”。",
    "product_opportunity_cn": "可设计一套显式控制面：按 server 展示 inline/deferred、实际选中的工具和策略否决；把 steering、wait interrupted、后台任务继续运行、compaction 重试与危险命令例外写入同一条运行时间线，并提供暂停、取消和审计导出。",
    "competitive_risk_cn": "动态工具加载仍依赖实验性 `tool-select`，且模型与服务端都要声明能力；Release 没有证明大规模 MCP 工具集的 token、准确率或延迟收益。steering 只中断等待，不会停止后台任务。`/tmp`、`/temp` 下字面路径的 `rm -rf` 可跳过确认，但混合目标、通配符、变量和 `..` 仍会保留危险判定。没有看到面向用户的完整审计日志或回滚说明。",
    "recommended_action": "investigate",
    "questions_to_validate": [
        "deferred MCP server 的工具何时被 `select_tools` 选中，选择理由、参数和策略否决是否写入可导出的运行日志？",
        "用户 steering 中断 `WaitFor` 后，如何继续、暂停或取消仍在运行的后台任务，连续多条 steering 如何排序？",
        "compaction 失败次数、原因和缩减路径是否可观测，配置能否被团队策略设上限？",
        "临时目录删除免确认如何处理挂载点、符号链接和审计记录，管理员能否关闭该例外？"
    ],
    "follow_up_triggers": [
        "`tool-select` 退出实验状态，并公布动态工具加载的 token、延迟或任务成功率评测",
        "Kimi Code 增加工具选择、steering、后台任务和 compaction 的统一审计时间线",
        "权限策略增加团队级配置、例外审计、暂停/取消与恢复说明"
    ],
    "scores": {
        "topic_relevance": 5,
        "novelty": 5,
        "technical_or_product_significance": 5,
        "strategic_value": 4,
        "source_quality": 5,
        "model_value": 2,
        "agent_architecture_value": 5,
        "ai_product_value": 4,
        "macro_value": 1,
        "actionability": 5
    },
    "report_date": DATE,
    "event_date": DATE,
    "canonical_url": KIMI_RELEASE,
    "first_seen_date": DATE,
    "last_seen_date": DATE,
    "run_dates": [DATE],
    "evidence_boundary": "GitHub Release API 确认 0.43.0 为非 prerelease，并给出 2026-09-14T12:03:30Z 发布时间；Atom 的 12:14:33Z 是 feed 更新时间。功能边界来自 Release 与已合并 PR。动态工具加载仍需实验性 tool-select；AI session title 的服务端转正不等于预构建 Web UI 已同步；性能收益、完整日志和回滚能力没有公开验证。",
    "related_sources": [
        {"url": PR_DYNAMIC_TOOLS, "type": "merged_pr_dynamic_tool_loading"},
        {"url": PR_STEERING, "type": "merged_pr_human_steering"},
        {"url": PR_COMPACTION, "type": "merged_pr_compaction_retry_config"},
        {"url": PR_PERMISSION_REMINDER, "type": "merged_pr_permission_context_boundary"},
        {"url": PR_TMP_GUARD, "type": "merged_pr_dangerous_command_exception"},
        {"url": KIMI_ATOM, "type": "official_atom_timestamp"}
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
            "id": "2026-09-14-agent-control-is-more-than-permission-mode",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "agent_architecture",
            "source_signal_ids": [SIGNAL_ID],
            "working_title_cn": "Agent 控制权不该只有一个“自动模式”开关",
            "core_tension_cn": "工具披露、人工打断、后台任务、上下文压缩和危险命令确认是五种不同控制权，压成一个自动/手动开关会掩盖风险。",
            "why_now_cn": "Kimi Code 0.43 同时改了 MCP 工具按需披露、steering 中断等待、compaction 重试和 `rm -rf` 确认例外，正好提供了一组可落到字段与日志的 Agent 控制面样本。",
            "target_audience_cn": ["AI 产品经理", "Agent Runtime 开发者", "企业 AI 安全与治理团队"],
            "evidence_boundary_cn": "依据 Kimi Code 正式 Release 和已合并 PR。动态工具选择仍为实验能力，官方没有公开性能收益；steering 只释放等待，不等于取消后台任务；日志、暂停和回滚仍需产品实测。",
            "source_urls": [KIMI_RELEASE],
            "platforms": {
                "xiaohongshu": {
                    "title": "Agent 的“自动模式”太粗了：至少要拆成 5 个开关",
                    "hook": "能不能自动执行，只回答了一小部分问题。工具何时给模型、用户能否插话、后台任务是否停、压缩失败怎么重试、哪些命令免确认，都得单独设计。",
                    "format": "8页图文卡",
                    "outline": [
                        "为什么自动/手动二分不够",
                        "工具披露：inline 与 deferred",
                        "人工 steering：打断等待但不取消任务",
                        "后台任务的继续、暂停与取消",
                        "上下文压缩的重试预算",
                        "危险命令的确认例外",
                        "统一审计时间线应该记录什么",
                        "Agent 控制面验收清单"
                    ],
                    "visual_direction": "一张五层控制面剖面图，分别标出默认值、用户动作、后台状态和审计事件",
                    "cta": "你现在用的 Agent，能分清“打断等待”和“取消任务”吗？"
                },
                "twitter": {
                    "title": "Agent control is not one autonomy toggle",
                    "hook": "Kimi Code 0.43 separates tool disclosure, human steering, background-task lifecycle, compaction retries, and command confirmation. Those controls need different defaults and logs.",
                    "format": "7帖 Thread",
                    "outline": [
                        "why one autonomy toggle fails",
                        "deferred MCP tool disclosure",
                        "policy veto with disallowedTools",
                        "steering versus cancellation",
                        "compaction retry budgets",
                        "dangerous-command exceptions",
                        "minimum audit timeline"
                    ],
                    "visual_direction": "state machine showing wait interrupted while the background task remains running",
                    "cta": "Which of these controls does your agent expose and log today?"
                },
                "wechat": {
                    "title": "别再用一个“自动模式”管理 Agent：控制面至少要拆成五层",
                    "hook": "Kimi Code 0.43 的价值不在又多了几个配置项，而在它把工具披露、人工插话、后台任务、压缩重试和命令确认拆成了不同的运行时契约。",
                    "format": "2500—3200字产品分析",
                    "outline": [
                        "从 0.43 Release 看 Agent 控制权的拆分",
                        "工具 schema 为什么不该全部常驻上下文",
                        "按需加载的能力声明与策略否决",
                        "steering、暂停、取消三个动作的差别",
                        "compaction 重试预算如何进入运维",
                        "危险命令例外的边界与审计",
                        "统一运行时间线与管理员策略",
                        "产品验收问题清单"
                    ],
                    "visual_direction": "控制面字段表加状态机：配置层、策略层、运行层、审计层分开标注",
                    "cta": "附一份可直接用于 Agent 产品评审的控制面字段清单。"
                }
            }
        }
    ]
}

NEW_SOURCE_SPECS = [
    (KIMI_RELEASE, "Kimi Code 0.43.0 release", "MoonshotAI / GitHub", "confirmed"),
    (KIMI_ATOM, "Kimi Code Releases Atom feed", "MoonshotAI / GitHub", "confirmed"),
    (PR_DYNAMIC_TOOLS, "Dynamic tool loading and per-server MCP deferred disclosure", "MoonshotAI / GitHub", "confirmed"),
    (PR_STEERING, "Human steering can interrupt background-task waits", "MoonshotAI / GitHub", "confirmed"),
    (PR_COMPACTION, "Configurable compaction attempt limit", "MoonshotAI / GitHub", "confirmed"),
    (PR_PERMISSION_REMINDER, "Permission-mode reminder injection switch", "MoonshotAI / GitHub", "confirmed"),
    (PR_TMP_GUARD, "Temporary-directory rm -rf confirmation exception", "MoonshotAI / GitHub", "confirmed"),
    (CODEX_RELEASE, "OpenAI Codex 0.155.0-alpha.4 prerelease", "OpenAI / GitHub", "confirmed"),
    (FYXER, "How Fyxer built an AI executive assistant people trust", "OpenAI", "primary_statement"),
    (OPENAI_RSS, "OpenAI News RSS", "OpenAI", "confirmed"),
    (FYXER_VIDEO, "How Fyxer built an AI executive assistant people trust", "OpenAI / YouTube", "primary_statement"),
]

NEW_REVIEWS = [
    {
        "url": KIMI_RELEASE,
        "decision": "include",
        "signal_id": SIGNAL_ID,
        "published_at": "2026-09-14T12:03:30Z",
        "reason": "the non-prerelease body and merged PRs document a distinct agent-control update: per-server deferred MCP tool disclosure, policy-vetoable on-demand selection, steering that interrupts waits while preserving background tasks, configurable compaction attempts, and explicit permission exceptions"
    },
    {
        "url": CODEX_RELEASE,
        "decision": "checked_no_match",
        "published_at": "2026-09-14T11:48:08Z",
        "reason": "the GitHub API confirms a prerelease, but its body only says 'Release 0.155.0-alpha.4' and provides no changelog, workflow, capability boundary, evaluation, or other substantive increment"
    },
    {
        "url": FYXER + "/",
        "decision": "outside_incremental_window_no_material_update",
        "published_at": "2026-08-13T12:00:00Z",
        "reason": "OpenAI's official RSS resolves the canonical article to August 13, not September 14. The September 14 official video repeats the same customer-story architecture and vendor-reported metrics; the sitemap lastmod alone is not a new product event"
    }
]


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def normalized(value: str) -> str:
    return value.rstrip("/")


def build_sources(prior_sources: list[dict]) -> list[dict]:
    sources = deepcopy(prior_sources)
    by_url = {normalized(item["url"]): item for item in sources}
    next_id = max((item["id"] for item in sources), default=0) + 1
    for url, title, publisher, level in NEW_SOURCE_SPECS:
        key = normalized(url)
        if key in by_url:
            continue
        item = {
            "id": next_id,
            "title": title,
            "url": url,
            "publisher": publisher,
            "evidence_level": level,
            "accessed": RUN_AT
        }
        sources.append(item)
        by_url[key] = item
        next_id += 1
    return sources


def build_brief(sources: list[dict]) -> str:
    ids = {normalized(source["url"]): source["id"] for source in sources}
    c = lambda url: f"[{ids[normalized(url)]}]"
    source_block = "\n".join(f'[{source["id"]}] {source["url"]}' for source in sources)
    return f'''# AI Signal 日报｜{DATE}

**窗口：** 20:25 增量只核验本轮 3 个 `new_candidates`；当天累计完成 23 个跨轮候选判断。Kimi Release 使用 GitHub API 的真实发布时间；OpenAI Sitemap `lastmod` 只用于发现。
**一句话结论：** 新增 1 条 P1 Agent 架构 Signal。Kimi Code 0.43 把 MCP 工具披露、人工 steering、后台等待、压缩重试和命令确认拆成了可分别配置的运行时控制。{c(KIMI_RELEASE)}{c(PR_DYNAMIC_TOOLS)}{c(PR_STEERING)}

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 没有新模型、价格、开放范围或独立评测 |
| Agent 架构 | 1 | MCP 工具按需披露，人工指令可打断等待但不会取消后台任务 |
| AI 产品 | 0 | Fyxer 是 8 月旧客户案例的页面更新，不是 9 月 14 日产品发布 |
| AI 宏观 | 0 | 没有产业结构、监管、算力或资本变化 |

## 模型｜0 条

OpenAI Codex `0.155.0-alpha.4` 的 GitHub API 时间落在本轮，但它是 prerelease，正文只有版本名，没有功能、工作流、评测或边界说明，不能仅凭版本号进入模型或 Agent 主线。{c(CODEX_RELEASE)}

## Agent 架构｜1 条

### Kimi Code 0.43：工具不必全部常驻，用户插话也不必等后台任务

Kimi Code 0.43.0 是正式版本。它允许每个 MCP server 显式配置 `deferred: true`：只有当模型声明 `dynamically_loaded_tools` 且启用实验性 `tool-select` 时，该 server 的工具才会退出顶层 `tools[]`，由 `select_tools` 按需加载。默认仍是 inline，`disallowedTools` 可以继续否决工具。{c(KIMI_RELEASE)}{c(KIMI_ATOM)}{c(PR_DYNAMIC_TOOLS)}

用户控制也更细了。模型等待后台任务时，新的 steering 消息会让 `WaitFor` 返回非错误的 `interrupted`，工具历史保留，后台任务继续运行；同一批其他前台工具仍会完成，再进入下一次模型请求。这个动作是“打断等待”，不是“取消任务”。{c(KIMI_RELEASE)}{c(PR_STEERING)}

版本还把 compaction 的最大总尝试次数开放为正整数配置，默认 5；关闭 permission-mode reminder 只移除注入模型上下文的提示，不改变 auto mode 的审批语义。对字面位于 `/tmp` 或 `/temp` 下、且不含通配符、变量、混合目标或 `..` 的 `rm -rf`，危险命令策略可跳过确认。{c(PR_COMPACTION)}{c(PR_PERMISSION_REMINDER)}{c(PR_TMP_GUARD)}

**为什么重要：** Agent 控制权不该只剩“自动/手动”一个开关。工具何时暴露、用户能否插话、后台任务是否继续、压缩失败重试多少次、哪些命令免确认，都需要不同的默认值和审计事件。

**建议动作：** 用这五层检查现有 Agent 控制面：记录实际披露和选择的工具、策略否决、steering、wait interrupted、后台任务状态、compaction 尝试及危险命令例外；把暂停、取消和恢复做成独立动作，避免用户把“已打断”等同于“已停止”。

## AI 产品｜0 条

Fyxer 页面这次是 Sitemap 修改，不是新发布。OpenAI 官方 RSS 给出的文章发布时间是 2026-08-13T12:00:00Z；9 月 14 日上传的官方短视频继续讲同一套邮件理解、上下文重排、用户反馈和厂商自报指标，没有形成新的产品上线状态或控制边界。{c(FYXER)}{c(OPENAI_RSS)}{c(FYXER_VIDEO)}

## AI 宏观｜0 条

本轮没有新的治理、资本、算力、监管或产业结构变化。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有模型负责人关于模型能力、训练、评测或路线的新原创内容。

## AI 一线实践者观点｜0 条

Fyxer 视频是 3 分多钟的官方客户案例短片，核心材料已出现在 8 月文章中；它不是新的长访谈、失败复盘或独立评测。{c(OPENAI_RSS)}{c(FYXER_VIDEO)}

## 本轮审核但未入选

- OpenAI Codex `0.155.0-alpha.4`：`checked_no_match`。prerelease 正文只有版本名，没有可判断的信息增量。{c(CODEX_RELEASE)}
- Fyxer：`outside_incremental_window_no_material_update`。官方 RSS 把文章日期解析为 8 月 13 日；9 月 14 日视频重复旧客户案例，Sitemap `lastmod` 不能把它改写成今日发布。{c(FYXER)}{c(OPENAI_RSS)}{c(FYXER_VIDEO)}

## 当天此前审核但未入选

- `commit-rewriter 0.1` 是 Git 历史清理工具，没有新的 Agent 运行时或产品工作流。{c('https://simonwillison.net/2026/Sep/14/commit-rewriter/')}
- `shot-scraper 1.12` 只增加 WebP 输出和质量参数，属于普通截图工具维护。{c('https://simonwillison.net/2026/Sep/13/shot-scraper/')}
- 早些时候的 18 个 OpenAI Sitemap 观察均是跨轮旧 URL 的 `lastmod` 变化，没有独立发布日期或内容哈希证据，因此没有重复建卡。

## 覆盖与缺口

- 当前机械采集仍有 78 个 `mechanical_failure` 和 2 个 `access_blocked`；本轮新候选通过 GitHub Release/API、Atom、OpenAI 官方 RSS 和官方 YouTube fallback 完成内容判断。
- Kimi 的功能与边界由 Release 和已合并 PR 确认，但 `tool-select` 仍是实验能力；官方没有公开 token、延迟或任务成功率收益。
- Release 没有给出统一运行日志、暂停、回滚或团队级策略 UI，不能从代码合并推断这些产品能力已经存在。
- 本轮只审核 3 个真新增候选，没有重扫 167 条滚动窗口记录，也没有重审 5 条队列记录。

## 证据边界

- Kimi Release API 的 `published_at` 是 2026-09-14T12:03:30Z；Atom 的 12:14:33Z 是 feed 更新时间，未用来覆盖正式发布时间。{c(KIMI_RELEASE)}{c(KIMI_ATOM)}
- Fyxer 直接页面请求触发 Cloudflare 403；正文发现由检索辅助，正式日期与排除判断只依赖成功获取的 OpenAI RSS、官方视频元数据、描述和字幕。{c(OPENAI_RSS)}{c(FYXER_VIDEO)}
- `rm -rf` 免确认只覆盖 PR 明示的字面临时目录目标；没有把它扩写成通用自动授权。{c(PR_TMP_GUARD)}

## 飞书短版

**一句话结论：** 3 个真新增候选完成正文核验，新增 1 条 P1 Agent 架构 Signal。

**重点：** Kimi Code 0.43 支持把 MCP server 工具设为 deferred，并让 steering 打断 `WaitFor`；后台任务仍继续，工具策略仍可否决。{c(PR_DYNAMIC_TOOLS)}{c(PR_STEERING)}

**判断：** Agent 控制面至少要拆开工具披露、人工打断、后台任务、压缩重试和命令确认，不能只做一个自动模式开关。

**边界：** 动态工具选择仍为实验能力；性能收益、统一日志、暂停和回滚没有公开验证。{c(KIMI_RELEASE)}

**建议动作：** 把这五层及其默认值、覆盖优先级和审计事件加入 Agent 产品验收。

**结果：** previous_count=0，new_count=1，updated_count=0，total_count=1。

## Sources

{source_block}
'''


def main() -> None:
    collection = load(DAY / "collection-run-summary.json")
    prior_summary = load(DAY / "run-summary.json")
    prior_sources = load(DAY / "citation-ledger.json")["sources"]
    sources = build_sources(prior_sources)

    prior_reviews = [
        item for item in prior_summary.get("candidate_reviews", [])
        if normalized(item.get("url", "")) not in {normalized(r["url"]) for r in NEW_REVIEWS}
    ]
    reviews = prior_reviews + NEW_REVIEWS

    summary = deepcopy(collection)
    for probe in summary.get("representative_probes", []):
        if probe.get("name") == "Kimi Code releases":
            probe["status"] = "selected"
            probe["note"] = "0.43.0 Release API body and merged PRs reviewed; one agent-governance signal selected"
        elif probe.get("name") == "OpenAI Codex releases":
            probe["status"] = "checked_no_match"
            probe["note"] = "The only cross-run new item, 0.155.0-alpha.4, is a prerelease whose body contains no substantive changelog"
        elif probe.get("name") == "OpenAI sitemap":
            probe["status"] = "candidate_only"
            probe["note"] = "The new Fyxer lastmod was reviewed against official RSS and video; the article dates to August 13 and has no material September 14 product update"

    summary.update({
        "run_type": "daily_four_lane_incremental_editorial_review",
        "run_at": RUN_AT,
        "deliverable_outcome": "success",
        "scheduler_outcome": "success_after_fallback_retries",
        "editorial_shortlist": 1,
        "reviewed_new_candidates": 3,
        "day_reviewed_candidates_total": len(reviews),
        "previous_count": 0,
        "new_count": 1,
        "updated_count": 0,
        "excluded_count": 4,
        "candidate_queue_count": 5,
        "new_in_run_count": 3,
        "unreviewed_candidate_count": 0,
        "total_count": 1,
        "selected": 1,
        "lane_counts": {"model": 0, "agent_architecture": 1, "ai_product": 0, "ai_macro": 0},
        "priority_counts": {"P0": 0, "P1": 1, "P2": 0, "P3": 0},
        "executive_model_longform": 0,
        "practitioner_statements": 0,
        "cross_day_duplicates_removed": 0,
        "candidate_reviews": reviews,
        "review_breakdown": {
            "cross_run_duplicate": 18,
            "below_formal_bar": 3,
            "outside_incremental_window": 1,
            "selected": 1,
            "watchlist": 0,
            "unresolved": 0
        },
        "content_topics": {"topic_count": 1, "platform_variants": 3},
        "collection_contract": {
            "raw_candidates_in_rolling_window_is_not_increment": True,
            "candidate_queue_count_is_not_new_count": True,
            "sitemap_lastmod_is_discovery_only": True,
            "feed_titles_require_body_verification": True,
            "http_2xx_is_not_checked_no_match": True,
            "true_increment_source": "new_in_run_count and new_candidates followed by body-level editorial review"
        },
        "review_notes": [
            "Reviewed only the 3 cross-run new candidates from the 20:25 collection; the 167-entry rolling pool and full 5-entry queue were not rescanned.",
            "Kimi Code 0.43.0 was selected as a distinct release-level event because its official body and merged PRs change tool disclosure, steering, background-wait, compaction-retry, and permission-exception contracts.",
            "Codex 0.155.0-alpha.4 was excluded because the prerelease body has no substantive changelog.",
            "Fyxer was excluded from the daily increment after OpenAI RSS resolved the article to August 13; the September 14 official video repeats the same customer story rather than adding a new product state.",
            "Direct GitHub and OpenAI requests were retried after SSL/Cloudflare failures; unresolved HTTP blocking was not treated as no-match."
        ]
    })

    dump(DAY / "selected.json", [SIGNAL])
    dump(DAY / "citation-ledger.json", {
        "version": 1,
        "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
        "sources": sources
    })
    dump(DAY / "citations.json", [{"id": source["id"], "url": source["url"]} for source in sources])
    dump(DAY / "daily-brief.md", build_brief(sources))
    dump(DAY / "run-summary.json", summary)
    dump(ROOT / "content-topics" / DATE / "topics.json", TOPICS)

    print(json.dumps({
        "date": DATE,
        "reviewed_new_candidates": 3,
        "day_reviewed_candidates_total": len(reviews),
        "selected": 1,
        "excluded": 2,
        "citations": len(sources),
        "topics": 1,
        "platform_variants": 3
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
