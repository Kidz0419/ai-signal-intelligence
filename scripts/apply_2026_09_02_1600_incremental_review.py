#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-02"
TZ = ZoneInfo("Asia/Shanghai")
DISCOVERY_CUTOFF = datetime.fromisoformat("2026-09-02T16:00:02+08:00")
REVIEWED_AT = datetime.now(TZ).replace(microsecond=0)
PREVIOUS_REVIEW_AT = "2026-09-02T00:21:46+08:00"


def iso(dt: datetime) -> str:
    return dt.isoformat()


def load_json(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def topic(*, id: str, lane: str, signal_ids: list[str], title: str, tension: str, why_now: str, boundary: str,
          urls: list[str], audience: list[str], angle: str, timeliness: str = "this_week", priority: str = "A") -> dict:
    outline = [
        "已确认发生了什么",
        "关键对象与动作 / 控制面",
        "为什么这件事现在值得写",
        "证据边界和不能误写的地方",
        "对产品 / 架构判断的启发",
        "接下来要继续验证什么",
    ]
    return {
        "id": id,
        "status": "candidate",
        "timeliness": timeliness,
        "priority": priority,
        "topic_lane": lane,
        "source_signal_ids": signal_ids,
        "working_title_cn": title,
        "core_tension_cn": tension,
        "why_now_cn": why_now,
        "target_audience_cn": audience,
        "evidence_boundary_cn": boundary,
        "source_urls": urls,
        "platforms": {
            "xiaohongshu": {
                "title": title[:34],
                "hook": angle,
                "format": "7页图文卡",
                "outline": outline,
                "visual_direction": "对象—动作—控制面流程图，少量术语，结论先行",
                "cta": "你会先验收哪一个边界？",
            },
            "twitter": {
                "title": title,
                "hook": angle,
                "format": "7帖 Thread",
                "outline": outline,
                "visual_direction": "one architecture or workflow diagram",
                "cta": "What would you test first?",
            },
            "wechat": {
                "title": title,
                "hook": angle,
                "format": "1800—2400字深度文章",
                "outline": outline,
                "visual_direction": "工作流图、证据边界表、验证清单",
                "cta": "文末附可复用的验收问题",
            },
        },
    }


day = ROOT / "daily" / DATE
selected = load_json(day / "selected.json")
by_id = {row["id"]: row for row in selected}

copilot_id = "2026-09-01-github-copilot-billing-org-model-access"
copilot = by_id[copilot_id]
copilot.update({
    "title": "GitHub Copilot 开始把模型治理收回到组织控制面：多组织 seat 只认付费组织，旧模型也按名单退场",
    "summary": "GitHub 8 月 31 日连发两条官方 Changelog，把 Copilot 的模型可用性收得更像企业策略：多组织 seat 用户的模型访问现在只由 `Usage billed to` 对应的付费组织决定，不再取已启用组织并集；另一条更新又宣布 Gemini 3.1 Pro、Claude Opus 4.5/4.6、Claude Sonnet 4.5/4.6 和 Raptor Mini 自 9 月 1 日起在大多数 Copilot 体验里弃用，管理员需要通过 model policies 启用替代模型。",
    "primary_tags": ["GitHub Copilot", "Model Governance", "Billing Owner"],
    "secondary_tags": ["Model Deprecation", "Model Policies", "Multi-org Seats"],
    "why_it_matters_cn": "这已经不是单点功能更新，而是 GitHub 把模型选择的 source of truth 明确绑回付费主体、组织策略和官方弃用节奏。企业里的“能不能选这个模型”会越来越像预算、policy 和生命周期管理的交集。",
    "personal_relevance_cn": "如果在做多组织 AI 产品，最好把 billing owner、policy source、model lifecycle 和迁移解释一起设计，不然模型下拉框很快就会和结算、合规与用户预期打架。",
    "product_opportunity_cn": "可把 billing-owner 驱动的模型白名单、弃用预警、替代模型推荐和迁移审计做成企业 AI 产品的基础能力。",
    "competitive_risk_cn": "这两条更新都来自官方 Changelog，能确认规则和弃用名单；但 GitHub 还没有给出更完整的管理员迁移 UI、历史审计影响或策略冲突时的回退逻辑。",
    "questions_to_validate": [
        "管理员能否在同一处看到 seat 的 billing owner、弃用窗口、替代模型和用户最终生效权限？",
        "跨组织 seat 切换或付费归属调整时，历史审计、模型可用性和替代建议是否会短暂不一致？",
        "billing owner + model deprecation 这套治理逻辑会不会继续扩展到 code review、cloud agent 或更多执行型 Copilot 能力？",
    ],
    "follow_up_triggers": [
        "GitHub 补充管理员 UI、迁移文档或审计报表截图",
        "更多 Copilot 能力开始显式绑定 billing owner、policy source 和 model lifecycle",
        "企业用户公开多组织 seat、模型弃用和替代迁移的治理复盘",
    ],
    "related_sources": [
        {
            "url": "https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated",
            "type": "same_day_model_deprecation"
        }
    ],
    "evidence_boundary": "官方 Changelog 能确认多组织 seat 的生效策略、受影响范围，以及一批 Copilot 模型自 9 月 1 日起在大多数体验里退场；GitHub 还没有公开更完整的管理员迁移 UI、历史审计影响或策略冲突时的回退逻辑。",
})

kimi_id = "2026-09-02-kimi-code-0400-safety-plugin-control-plane"
if kimi_id not in by_id:
    selected.append({
        "id": kimi_id,
        "demo": False,
        "topic_lane": "agent_architecture",
        "title": "Kimi Code 0.40 把默认多模型、插件市场和危险命令 hard gate 一起推到了控制面",
        "summary": "Kimi Code 0.40 把几个原本分散的控制点一起推到前台：subagent model pool `[secondary_model]` 在所有 launch mode 默认开启；Web Settings 新增 Plugins panel，可浏览、安装、启用、停用和删除插件；Auto mode 默认阻断 `shutdown`、`reboot`、`rm -rf` 等危险 shell 命令，Manual / YOLO 模式也会先询问；同版还让 Tower workers 继承 base checkout 未提交变更、记录死亡 agent，并新增 `kimi session list`。",
        "decision": "include",
        "confidence": 90,
        "relevance_level": "P2",
        "signal_type": "competitor",
        "content_type": "technical_update",
        "information_type": "agent_governance",
        "evidence_level": "confirmed",
        "source": "MoonshotAI",
        "url": "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.40.0",
        "published_at": "2026-09-02T05:59:00Z",
        "primary_tags": ["Kimi Code", "Dangerous Command Guard", "Plugin Marketplace"],
        "secondary_tags": ["secondary_model", "Tower Mode", "Session Audit"],
        "why_it_matters_cn": "coding agent 一旦同时拥有 shell、插件、subagent 和多工作区执行面，真正重要的就不是再多一个模型，而是默认模型编排、扩展分发和危险动作 hard gate 有没有进入同一套控制面。",
        "personal_relevance_cn": "如果在做 coding agent / agent IDE，最该对照的是默认多模型策略、插件市场的安装边界、危险命令 fail-closed 规则，以及 Tower / fork 这种并行执行状态怎么暴露给人。",
        "product_opportunity_cn": "可以把 plugin entitlement、dangerous-command policy、subagent pool defaults、worker-death resume hints 和 session list audit 做成团队级 coding agent 的基础能力。",
        "competitive_risk_cn": "官方 release notes 能确认这些开关和界面，但还没有给出管理员级策略、插件信任模型、误拦截率，或危险命令 guard 在真实任务里的 override 审计。",
        "recommended_action": "monitor",
        "questions_to_validate": [
            "dangerous_command_guard 后续会不会覆盖 `curl | sh`、破坏性 git、容器删除和权限升级这类高风险组合动作？",
            "Plugins panel 背后是否会公开权限作用域、来源信任或签名审核模型？",
            "secondary_model 默认开启后，成本、日志和审批表面会不会同步进入更正式的团队控制面？",
        ],
        "follow_up_triggers": [
            "Moonshot 发布更详细的插件市场、危险命令 guard 或管理员策略文档",
            "出现关于 guard 误拦截、override 审计或 Tower 恢复体验的真实使用复盘",
            "Plugins panel 暴露更明确的权限作用域、审核或来源信任机制",
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
            "actionability": 4
        },
        "report_date": DATE,
        "event_date": DATE,
        "canonical_url": "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.40.0",
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": "官方 Release 清单能确认 default secondary model pool、Plugins panel、dangerous command guard、Tower 恢复细节和 CLI session listing；还没有公开团队管理员策略、插件信任模型、override 审计或生产采用数据。"
    })

selected = sorted(selected, key=lambda row: (row["relevance_level"], row["topic_lane"], row["id"]))

topics_payload = load_json(ROOT / "content-topics" / DATE / "topics.json")
existing_topics = {row["id"]: row for row in topics_payload["topics"]}
existing_topics["2026-09-02-copilot-billing-owner-policy"] = topic(
    id="2026-09-02-copilot-billing-owner-policy",
    lane="ai_product",
    signal_ids=[copilot_id],
    title="多组织 AI 产品迟早会遇到的问题：模型权限、付费归属和弃用节奏到底听谁的",
    tension="一个用户挂在多个组织上时，feature entitlement、结算归属、policy source 和 model lifecycle 常常会互相打架。",
    why_now="GitHub 把 Copilot 的模型访问改成只认付费组织，同时又按官方名单弃用一批旧模型。",
    boundary="改动范围仍聚焦多组织 seat 与模型生命周期，不代表 Copilot 自动执行权限扩大。",
    urls=["https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans"],
    audience=["企业 AI 产品经理", "IT 管理员", "平台治理团队"],
    angle="模型下拉框背后，真正难的是 billing owner、policy source 和 deprecation lifecycle 到底怎么绑定。",
)
existing_topics["2026-09-02-coding-agent-hard-gates-and-plugin-control"] = topic(
    id="2026-09-02-coding-agent-hard-gates-and-plugin-control",
    lane="agent_architecture",
    signal_ids=[kimi_id],
    title="当 coding agent 真能跑 shell 和插件，默认安全门就不能再只是实验开关",
    tension="能力越像操作系统，真正难的越不是再接一个模型，而是哪些动作默认能做，哪些动作必须先拦。",
    why_now="Kimi Code 0.40 把 secondary model pool 默认开启、Plugins 面板拉进设置页，并让 dangerous command guard 成为 Auto mode 默认规则。",
    boundary="官方 release 能确认配置和 UI 变化，但没有管理员级审计或插件信任模型细节。",
    urls=["https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.40.0"],
    audience=["Coding agent 产品负责人", "开发者工具工程师", "安全 / 平台团队"],
    angle="别只看新功能数量，真正的分水岭是默认多模型、插件分发和危险命令 hard gate 是否进了同一套控制面。",
)

topics_order = [
    "2026-09-02-mcp-stateless-migration-checklist",
    "2026-09-02-dms-agent-human-review-boundary",
    "2026-09-02-agent-payments-hard-gates",
    "2026-09-02-coding-agent-hard-gates-and-plugin-control",
    "2026-09-02-webgpu-kernel-contracts",
    "2026-09-02-copilot-billing-owner-policy",
    "2026-09-02-public-sector-ai-shared-foundation",
]
topics_payload["topics"] = [existing_topics[key] for key in topics_order]

lane_counts = Counter(item["topic_lane"] for item in selected)
priority_counts = Counter(item["relevance_level"] for item in selected)
decision_counts = Counter(item["decision"] for item in selected)

ledger_sources = [
    {
        "id": 1,
        "title": next(row["title"] for row in selected if row["id"] == "2026-09-01-aws-mcp-stateless-migration-contract"),
        "url": "https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected",
        "publisher": "AWS",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 2,
        "title": next(row["title"] for row in selected if row["id"] == "2026-09-01-aws-dms-agent-review-boundary"),
        "url": "https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms",
        "publisher": "AWS",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 3,
        "title": next(row["title"] for row in selected if row["id"] == "2026-09-01-aws-agentcore-payments-trust-gate"),
        "url": "https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments",
        "publisher": "AWS",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 4,
        "title": next(row["title"] for row in selected if row["id"] == copilot_id),
        "url": "https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans",
        "publisher": "GitHub",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 5,
        "title": next(row["title"] for row in selected if row["id"] == "2026-09-01-huggingface-webgpu-kernel-contracts"),
        "url": "https://huggingface.co/blog/webgpu-kernels",
        "publisher": "Hugging Face",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 6,
        "title": "OpenAI News RSS",
        "url": "https://openai.com/news/rss.xml",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 7,
        "title": next(row["title"] for row in selected if row["id"] == "2026-08-31-openai-polimill-japan-public-ai-infrastructure"),
        "url": "https://r.jina.ai/http://openai.com/index/polimill/",
        "publisher": "OpenAI / r.jina.ai text mirror",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 8,
        "title": "Selected GitHub Copilot models deprecated",
        "url": "https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated",
        "publisher": "GitHub",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
    {
        "id": 9,
        "title": next(row["title"] for row in selected if row["id"] == kimi_id),
        "url": "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.40.0",
        "publisher": "MoonshotAI",
        "evidence_level": "confirmed",
        "accessed": iso(REVIEWED_AT),
    },
]

citations = [{"id": item["id"], "url": item["url"]} for item in ledger_sources]

brief = f'''# AI Signal 日报｜{DATE}

**窗口：** 北京时间 2026-09-02 00:00 至 {DISCOVERY_CUTOFF.strftime("%Y-%m-%d %H:%M")}  
**一句话结论：** 到 16:00 截止，今天的正式信号从 6 条变成 7 条。91 个真新增候选里，只有 Kimi Code 0.40 新增进正式范围；GitHub Copilot 的“模型弃用名单”则并入今早那张模型治理卡，其余增量没有越过正式门槛。[1][2][3][4][5][6][7][8][9]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 1 | Hugging Face 把 WebGPU kernel 做成独立 contract + Fleet 证据层 |
| Agent 架构 | 3 | AWS 把 MCP 迁移和 agent 支付写成控制面，Kimi 把默认多模型与危险命令硬门推到前台 |
| AI 产品 | 2 | DMS agent 的人审边界被写清，Copilot 把模型权限与弃用节奏一起绑回组织治理 |
| AI 宏观 | 1 | Polimill 公共部门 AI 覆盖面已到约 1,050 个自治体、55 万名公职人员 |

## 模型｜1 条

### Hugging Face：浏览器推理开始有自己的“底层合同”了

Hugging Face 发布 `@huggingface/kernels`，把 207 个 WebGPU kernels 作为独立、可版本化的 Hub 对象公开，每个 kernel 都带 manifest、correctness cases、bench cases 和 WGSL 模板；同时上线 Fleet，在浏览器里收集跨设备 benchmark 和正确性证据。[5]

**为什么重要：** 这不是又一个 local AI 演示页。更实在的变化是，WebAI 的底层算子终于能被单独检查、版本化和复现，而不是全都闷在 runtime 黑盒里。

## Agent 架构｜3 条

### AWS：MCP 无状态之后，哪些旧基础设施真的可以删

AWS 把 MCP 2026-07-28 版落到了部署细节：`initialize` 握手和 `Mcp-Session-Id` header 被拿掉，请求可以直接从 tool call 开始，任何实例都能响应；但只要还服务旧客户端，sticky session 和 session store 就不能提前拆。[1]

**为什么重要：** 很多团队现在最缺的不是“知道 MCP 变了”，而是知道该先记录什么流量、什么时候退遗留 lane、哪些会话基础设施终于能安全下线。

### AWS / t54：先过信任门，再让 agent 付钱

AWS 的 t54 案例把 agent 支付的硬边界写得很明确：x402-secure 先对 endpoint 和地址做实时评分，AgentCore payments 再负责 session spending limit、credential isolation 和结算；如果评分不过线或 URL 不匹配，付款直接在代码层被挡住，模型本身不能覆写。[3]

**为什么重要：** 这条真正有用的地方在于，它把“agent 会花真钱”拆成了可检查的控制点，而不是把风控继续留给 prompt 或人工抽查。

### Kimi Code 0.40：默认多模型、插件市场和危险命令 hard gate 一起进入控制面

Kimi Code 0.40 的官方 release notes 把三件原本容易散落在实验角落里的东西推到了默认路径：subagent model pool `[secondary_model]` 变成所有 launch mode 的默认设置；Web Settings 新增 Plugins panel，可浏览市场并安装、启用、停用和删除插件；Auto mode 默认阻断 `shutdown`、`reboot` 和 `rm -rf` 这类危险 shell 命令，Manual / YOLO 模式也会先询问。[9]

**为什么重要：** 这类改动值钱的地方，不是界面更热闹，而是 coding agent 的扩展面、默认模型编排和自动执行风险开始一起进入可配置控制面。

## AI 产品｜2 条

### AWS DMS：AI agent 能编排迁移，但不会替你背语义正确性

AWS DMS Schema Conversion 这篇正文展示了一条清晰的 agent 工作流：导入元数据、启动转换、等待完成、导出 assessment report、解释 CRITICAL action items；当 deterministic rule engine 兜不住时，生成式步骤只保证 PL/pgSQL 语法能过，语义正确性和最终上线责任仍然留给人审和功能测试。[2]

**为什么重要：** 这类边界越早写清楚，越不容易把“自动化很多步骤”误读成“迁移已经可直接上线”。

### GitHub Copilot：模型访问开始更明确地听命于付费组织和官方弃用名单

GitHub 8 月 31 日连发两条 Copilot Changelog：多组织 seat 的模型可用性现在只认 `Usage billed to` 对应的付费组织，不再取已启用组织并集；同时 Gemini 3.1 Pro、Claude Opus 4.5/4.6、Claude Sonnet 4.5/4.6 和 Raptor Mini 在大多数 Copilot 体验中自 9 月 1 日起弃用，管理员需要通过 model policies 启用替代模型。[4][8]

**为什么重要：** 这不是花哨新功能，但它把模型选择、组织治理和结算归属进一步绑成了一件事。企业里的“能不能选这个模型”会越来越像预算、policy 和生命周期管理的结果。

## AI 宏观｜1 条

### OpenAI / Polimill：日本公共部门 AI 已经不是小试点了

OpenAI News RSS 可确认，这篇 Polimill 客户案例首发于 8 月 31 日。正文称 QommonsAI 已覆盖日本约 1,050 个自治体和约 55 万名公职人员，当前场景包括议会答辩、公共服务、社保福利和法律检索；文中提到的 Qommons ONE 和 super agent 仍是 2026 年秋季 rollout 计划，不当作已上线事实。[6][7]

**为什么重要：** 这条值得记住，是因为它已经开始长成“共享知识底座 + 组织控模 + 专业工作流”的公共部门产品形态，而不是普通聊天工具试点。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新增满足模型主题边界和信息增量门槛的高管长文。

## AI 一线实践者观点｜0 条

本轮没有新的实践者原创内容进入正式日报。

## 排除与延后

- 85 个 OpenAI sitemap 命中先全部用官方 RSS 回填首发时间；除昨天已收录的 ChatGPT Ads 外，其余都没有形成新的当日正式信号。[6]
- OpenAI Codex 0.153.0-alpha.5 有正式 tag，但 release notes 过薄，暂时不足以开出新的正式卡片。
- Simon Willison 这轮的三条增量里，`datasette-mcp 0.2` 太轻，`GeoJSON Map Viewer` 偏工具随手作，`Rick Brewster` 则是二手引述，都没有越过今天的正式门槛。

## 证据边界

- AWS 这三条都来自官方正文，能确认对象、动作和控制面，但 t54 的交易规模、以及 DMS / MCP 迁移后的真实成功率与成本曲线仍主要缺少独立验证。[1][2][3]
- Hugging Face 的性能数字主要是 Apple M4 上的 op-level 对比，并明确排除了加载、编译、上传和回传开销；不要直接把它读成完整模型端到端时延承诺。[5]
- Copilot 这两条更新能确认规则和弃用名单，但 GitHub 还没有公开更完整的管理员迁移 UI、历史审计影响或策略冲突时的回退逻辑。[4][8]
- Kimi Code 0.40 的 release notes 能确认默认多模型、Plugins panel 和危险命令 guard 的存在，但还没有给出插件信任模型、团队管理员策略或 override 审计。[9]
- Polimill 的覆盖规模和开发提速来自 OpenAI / Polimill 官方表述，Qommons ONE 仍是计划而不是已上线能力。[6][7]

## 飞书短版

**一句话结论：** 到 16:00 截止，今天的正式信号从 6 条变成 7 条。91 个真新增候选里，只有 Kimi Code 0.40 新增进正式范围；Copilot 的模型弃用公告则并入了今早那张治理卡。  
**组织判断：** 这轮最值得记的，不是又多了几个页面，而是控制面继续往默认路径里走：谁能选模型、谁能装插件、什么命令模型绝对不能直接执行。  
**建议动作：** 把 legacy lane sunset、AI 迁移 apply gate、agent 支付 risk gate、billing-owner + deprecation policy，以及 coding agent dangerous-command guard 一起加入后续评估清单。  
**结果：** previous_count=6，new_count=1，updated_count=1，total_count=7。

## Sources

[1] https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected
[2] https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms
[3] https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments
[4] https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans
[5] https://huggingface.co/blog/webgpu-kernels
[6] https://openai.com/news/rss.xml
[7] https://r.jina.ai/http://openai.com/index/polimill/
[8] https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated
[9] https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.40.0
'''

run_summary = {
    "run_type": "daily_four_lane_incremental_manual_review",
    "run_at": iso(REVIEWED_AT),
    "deliverable_outcome": "success",
    "scheduler_outcome": "success",
    "window": {
        "timezone": "Asia/Shanghai",
        "start": "2026-09-02T00:00:00+08:00",
        "end": iso(DISCOVERY_CUTOFF),
        "incremental_since": PREVIOUS_REVIEW_AT,
    },
    "registered_sources": 111,
    "raw_candidates": 200,
    "unique_candidates": 161,
    "candidate_queue_count": 396,
    "new_in_run_count": 91,
    "reviewed_new_candidates": 91,
    "editorial_shortlist": 2,
    "previous_count": 6,
    "new_count": 1,
    "updated_count": 1,
    "excluded_count": 88,
    "unreviewed_candidate_count": 0,
    "total_count": 7,
    "selected": 7,
    "lane_counts": {
        "model": lane_counts.get("model", 0),
        "agent_architecture": lane_counts.get("agent_architecture", 0),
        "ai_product": lane_counts.get("ai_product", 0),
        "ai_macro": lane_counts.get("ai_macro", 0),
    },
    "priority_counts": {key: priority_counts.get(key, 0) for key in ("P0", "P1", "P2", "P3")},
    "decision_counts": {key: decision_counts.get(key, 0) for key in ("include", "watchlist")},
    "executive_model_longform": 0,
    "practitioner_statements": 0,
    "cross_day_duplicates_removed": 0,
    "source_status_counts": {
        "selected": 2,
        "candidate_only": 1,
        "checked_no_match": 88,
        "access_blocked": 0,
        "auth_required": 0,
        "mechanical_failure": 0,
        "not_checked": 0,
    },
    "review_notes": [
        "Reviewed only the 91 true new candidates from the 2026-09-02 16:00 baseline cycle and did not reopen the 396-item carry-forward queue.",
        "Mapped 85 OpenAI sitemap hits through the official OpenAI News RSS before judging freshness. Aside from the already-covered ChatGPT Ads URL, the remaining hits resolved to older publication dates or failed to clear the formal bar, so sitemap lastmod was never promoted as publication evidence.",
        "Read the GitHub Copilot deprecation changelog at the body level and merged it into the already-selected same-day Copilot governance event instead of opening a second near-duplicate card.",
        "Promoted one new signal after body review: Kimi Code 0.40, because the release moved default multi-model behavior, plugin distribution, and dangerous-command hard gates into the visible control plane.",
        "Left OpenAI Codex 0.153.0-alpha.5 and Simon Willison's three new posts out because the prerelease notes were too thin, the content was secondary, or the information delta stayed below the formal threshold.",
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
dump(day / "citation-ledger.json", {"version": 1, "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.", "sources": ledger_sources})
dump(day / "citations.json", citations)
dump(day / "daily-brief.md", brief)
dump(day / "run-summary.json", run_summary)
dump(ROOT / "content-topics" / DATE / "topics.json", topics_payload)

print(json.dumps({
    "date": DATE,
    "signals": len(selected),
    "topics": len(topics_payload["topics"]),
    "run_summary": str(day / "run-summary.json"),
}, ensure_ascii=False))
