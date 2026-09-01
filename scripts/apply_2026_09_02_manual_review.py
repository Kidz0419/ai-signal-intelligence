#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-02"
TZ = ZoneInfo("Asia/Shanghai")
RUN_AT = datetime.now(TZ).replace(microsecond=0)
WINDOW_START = datetime(2026, 9, 2, 0, 0, 0, tzinfo=TZ)
INCREMENTAL_SINCE = "2026-09-02T00:00:27+08:00"


SCORE_KEYS = [
    "topic_relevance",
    "novelty",
    "technical_or_product_significance",
    "strategic_value",
    "source_quality",
    "model_value",
    "agent_architecture_value",
    "ai_product_value",
    "macro_value",
    "actionability",
]

LANE_TO_SCORE = {
    "model": "model_value",
    "agent_architecture": "agent_architecture_value",
    "ai_product": "ai_product_value",
    "ai_macro": "macro_value",
}


def iso(dt: datetime) -> str:
    return dt.isoformat()


def to_dt(value: str) -> datetime:
    if "," in value and "GMT" in value:
        return parsedate_to_datetime(value)
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def event_date(value: str) -> str:
    return to_dt(value).astimezone(TZ).date().isoformat()


def scores(*, lane: str, novelty: int, significance: int, strategic: int, source_quality: int, actionability: int,
           model: int = 1, agent_architecture: int = 1, ai_product: int = 1, macro: int = 1) -> dict[str, int]:
    data = {
        "topic_relevance": 5,
        "novelty": novelty,
        "technical_or_product_significance": significance,
        "strategic_value": strategic,
        "source_quality": source_quality,
        "model_value": model,
        "agent_architecture_value": agent_architecture,
        "ai_product_value": ai_product,
        "macro_value": macro,
        "actionability": actionability,
    }
    data[LANE_TO_SCORE[lane]] = max(data[LANE_TO_SCORE[lane]], 5)
    return data


def row(*, id: str, lane: str, title: str, summary: str, priority: str, signal_type: str, content_type: str,
        information_type: str, source: str, url: str, published_at: str, why: str, personal: str,
        opportunity: str, risk: str, boundary: str, confidence: int, primary_tags: list[str],
        secondary_tags: list[str], score_kwargs: dict[str, int], related_sources: list[dict[str, str]] | None = None) -> dict:
    return {
        "id": id,
        "demo": False,
        "topic_lane": lane,
        "title": title,
        "summary": summary,
        "decision": "include",
        "confidence": confidence,
        "relevance_level": priority,
        "signal_type": signal_type,
        "content_type": content_type,
        "information_type": information_type,
        "evidence_level": "confirmed",
        "source": source,
        "url": url,
        "published_at": published_at,
        "primary_tags": primary_tags,
        "secondary_tags": secondary_tags,
        "why_it_matters_cn": why,
        "personal_relevance_cn": personal,
        "product_opportunity_cn": opportunity,
        "competitive_risk_cn": risk,
        "recommended_action": "investigate" if priority == "P1" else "monitor",
        "questions_to_validate": [],
        "follow_up_triggers": [],
        "scores": scores(lane=lane, **score_kwargs),
        "report_date": DATE,
        "event_date": event_date(published_at),
        "canonical_url": url,
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": boundary,
        **({"related_sources": related_sources} if related_sources else {}),
    }


rows = [
    row(
        id="2026-09-01-aws-mcp-stateless-migration-contract",
        lane="agent_architecture",
        title="AWS 把 MCP 迁移要点写实了：无状态核心能删 sticky session，但旧客户端没退干净前别提前拆",
        summary="AWS 9 月 1 日的官方正文把 MCP 2026-07-28 版真正落到部署层：`initialize` 握手和 `Mcp-Session-Id` header 被拿掉，请求可直接从 tool call 开始，任何实例都能响应；旧协议时代常见的 sticky session、共享 session store 和自定义 body 解析路由不再是默认必需品，但仍服务 2025-era 客户端时不能提前删掉遗留会话基础设施。",
        priority="P1",
        signal_type="research",
        content_type="technical_update",
        information_type="agent_architecture",
        source="AWS",
        url="https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected",
        published_at="2026-09-01T06:09:19-07:00",
        why="这篇值钱的不是复述 MCP 更新，而是把 horizontal scaling、header 路由、MRTR、idempotent retry、trace context 和遗留客户端退场顺序讲成了可执行清单。",
        personal="如果在做 MCP 平台，最该核对的是：是不是还依赖 sticky routing、session store、body parsing，旧客户端流量什么时候归零，以及 requestState 和 ownership 校验是不是已经补上。",
        opportunity="可以把 version logging、legacy lane sunset、header-based routing、tool idempotency 和 trace propagation 做成自己的 MCP 升级验收单。",
        risk="AWS 的文章是架构指南，不是你当前部署已经自动合规；文章也没有给出迁移后的真实错误率、成本曲线或跨云适配细节。",
        boundary="官方正文能确认协议变更、迁移步骤和遗留客户端保留条件；它不是官方 conformance 结果，也不证明所有现有 MCP 服务器已安全迁完。",
        confidence=95,
        primary_tags=["AWS", "MCP", "Stateless Protocol"],
        secondary_tags=["MRTR", "Trace Context", "Legacy Client Sunset"],
        score_kwargs={"novelty": 4, "significance": 5, "strategic": 4, "source_quality": 5, "actionability": 5, "model": 1, "agent_architecture": 5, "ai_product": 2, "macro": 1},
        related_sources=[
            {"url": "https://modelcontextprotocol.io/specification/2026-07-28/changelog", "type": "protocol_changelog"}
        ],
    ),
    row(
        id="2026-09-01-aws-dms-agent-review-boundary",
        lane="ai_product",
        title="AWS 把 DMS Schema Conversion 的 agent 边界讲清楚了：AI 能编排迁移，但语法过关不等于语义正确",
        summary="AWS 9 月 1 日的 DMS Schema Conversion 正文展示了一条更像产品工作流而不是营销页的 agent 路径：agent 负责导入元数据、启动转换、等待完成、导出 assessment report 并解析 CRITICAL action items；当 deterministic rule engine 处理不了时，生成式步骤只要求输出能通过 PL/pgSQL 语法校验，并明确要求客户继续做人审和功能测试，不能把 ‘编译通过’ 当成迁移完成。",
        priority="P1",
        signal_type="research",
        content_type="technical_update",
        information_type="product_workflow",
        source="AWS",
        url="https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms",
        published_at="2026-09-01T08:19:13-07:00",
        why="很多 AI 迁移工具最容易偷换的就是‘自动化’和‘正确性’。AWS 这篇反而把那条线划得很明白：agent 能编排和解释，但最后的语义正确性、CRITICAL 修复和上线责任还在人。",
        personal="如果要比较数据库迁移 agent，最该看的是 action item 严重度怎么暴露、导出物是不是可审计、哪些步骤自动跑、哪些步骤必须停下来让工程师做决定。",
        opportunity="可以把 assessment export、人审队列、语义回归测试和最终 apply gate 设计成迁移 agent 的默认控制面，而不是事后补流程。",
        risk="这篇是官方产品深描，不是独立迁移成功率报告；文中示例和最佳实践不能替代你自己业务存储过程的回归验证。",
        boundary="官方正文确认了 agent 工作流、四步转换管线、CRITICAL action item 解释和人审边界；没有给出跨真实生产库的大样本成功率，也没有把 AI 生成代码描述成语义等价保证。",
        confidence=94,
        primary_tags=["AWS DMS", "Schema Conversion", "Human Review"],
        secondary_tags=["CRITICAL Action Items", "Assessment Report", "PL/pgSQL Validation"],
        score_kwargs={"novelty": 4, "significance": 5, "strategic": 4, "source_quality": 5, "actionability": 5, "model": 1, "agent_architecture": 2, "ai_product": 5, "macro": 1},
    ),
    row(
        id="2026-09-01-huggingface-webgpu-kernel-contracts",
        lane="model",
        title="Hugging Face 把浏览器推理底层单元拆成 207 个可版本化 WebGPU kernels，还顺手做了跨设备证据层",
        summary="Hugging Face 9 月 1 日发布 `@huggingface/kernels`，把 207 个 WebGPU kernel 作为独立、可版本化的仓库对象放到 Hub 上，每个 kernel 都带 manifest、correctness cases、bench cases 和 WGSL 模板；同时上线 Fleet，在浏览器里跑跨设备 benchmark 和正确性检查，把 WebAI 的底层算子优化从‘库内黑盒’变成可检查、可复现、可贡献证据的公共层。",
        priority="P1",
        signal_type="research",
        content_type="technical_update",
        information_type="model_research",
        source="Hugging Face",
        url="https://huggingface.co/blog/webgpu-kernels",
        published_at="2026-09-01T00:00:00.739Z",
        why="这不只是又一个 local AI demo。更关键的是它把浏览器推理里的 contract、benchmark 和 variant selection 从 runtime 内部拆了出来，后面谁做 WebAI 都能直接继承这层基础设施。",
        personal="做本地推理时，值得对照的不只是几倍加速，而是 kernel contract 是否版本化、correctness case 是否随实现走、以及跨设备证据能不能持续补进来。",
        opportunity="可以把 op-level contract、硬件回传 benchmark 和版本化 kernel 仓库当成浏览器推理栈的底座，而不是只盯模型量化。",
        risk="性能数字主要来自 Hugging Face 在 Apple M4 上的 op-level 对比，而且明确排除了加载、编译、上传和回传开销；它不是完整模型端到端时延承诺。",
        boundary="官方正文确认 207 个 kernel、Hub 仓库结构、JavaScript loader 和 Fleet；速度优势主要是官方自测，且只覆盖通过输出一致性与计时筛选后的对比样本。",
        confidence=93,
        primary_tags=["Hugging Face", "WebGPU", "Local AI"],
        secondary_tags=["Kernel Contracts", "Fleet", "Browser Inference"],
        score_kwargs={"novelty": 5, "significance": 5, "strategic": 4, "source_quality": 5, "actionability": 4, "model": 5, "agent_architecture": 2, "ai_product": 1, "macro": 1},
    ),
    row(
        id="2026-09-01-aws-agentcore-payments-trust-gate",
        lane="agent_architecture",
        title="t54 用 AgentCore payments 把 agent 支付拆成硬门：信任评分先过，钱才会动",
        summary="AWS 9 月 1 日的 t54 案例不是泛泛讲 agent 支付想象力，而是把控制面摊开：agent 发起交易前，x402-secure 会先对目标 endpoint 和支付地址做实时评分；Amazon Bedrock AgentCore payments 负责 session spending limit、credential isolation 和结算，`ProcessPayment` 返回 status 与完整 audit trail；若评分不过线或 URL 不匹配，付款在代码层直接被挡住，模型本身不能覆写。",
        priority="P2",
        signal_type="research",
        content_type="technical_update",
        information_type="agent_governance",
        source="AWS",
        url="https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments",
        published_at="2026-09-01T07:50:00-08:00",
        why="真正让 agent 去付钱时，问题从来不只是有没有钱包，而是谁定额度、谁管密钥、谁拦高风险 endpoint、以及事后能不能把每一笔花费和信任判断串起来。",
        personal="如果在看 agent commerce，最该拆的是 deterministic risk gate、session cap、role separation、audit trail 和失败时 spending limit 是否保持不变。",
        opportunity="可以把‘先过信任门再结算’做成 agent 支付默认架构，而不是把风控留给 prompt 或人工抽查。",
        risk="20 million transactions、拦截效果和规模都来自 AWS/t54 公开叙述，没有独立审计数据；这也还是单一客户与平台案例。",
        boundary="官方正文能确认 deterministic trust gate、session-scoped spending ceiling、Secrets Manager / IAM role separation、audit trail 和 MCP marketplace 接入路径；规模与效果指标主要来自厂商自报。",
        confidence=91,
        primary_tags=["AgentCore Payments", "Agent Commerce", "Trust Gate"],
        secondary_tags=["x402", "Spending Limit", "Audit Trail"],
        score_kwargs={"novelty": 4, "significance": 4, "strategic": 4, "source_quality": 5, "actionability": 4, "model": 1, "agent_architecture": 5, "ai_product": 3, "macro": 1},
        related_sources=[
            {"url": "https://aws.amazon.com/blogs/machine-learning/technical-deep-dive-agentcore-payments-and-innovation-in-agentic-commerce/", "type": "technical_deep_dive"}
        ],
    ),
    row(
        id="2026-09-01-github-copilot-billing-org-model-access",
        lane="ai_product",
        title="GitHub Copilot 改了多组织 seat 的模型权限：现在只认付费组织，不再取已启用组织并集",
        summary="GitHub 8 月 31 日的官方 Changelog 更新了一个很具体但很实际的 Copilot 规则：如果用户同时在多个组织里持有 Copilot seat，模型可用性现在只由 ‘Usage billed to’ 对应的付费组织决定；此前只要任一组织开了某个模型，用户就能用。若访问完全来自 enterprise 或其组织，这次规则不受影响。",
        priority="P2",
        signal_type="competitor",
        content_type="official_release",
        information_type="product_workflow",
        source="GitHub",
        url="https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans",
        published_at="2026-08-31T14:58:46-07:00",
        why="这类改动看起来不像大功能，但它把模型策略、组织治理和结算归属绑到一起了。以后企业里‘能不能选这个模型’更像预算和 policy 的结果，不只是个人偏好。",
        personal="如果在做多组织 AI 产品，最好早点把 feature entitlement、billing owner 和 policy source of truth 统一起来，不然后面一定会出现权限和结算对不上的坑。",
        opportunity="可把 billing owner 驱动的模型白名单、跨组织 seat 归属可视化和审计解释做成企业 AI 产品的基础能力。",
        risk="这次改动只影响一类多组织 seat 场景；官方正文没有给出管理员 UI、批量迁移工具或对现有审计报表的影响。",
        boundary="官方正文确认了新旧规则差异和适用范围；没有额外披露模型策略冲突时的回退逻辑，也没有把这项规则描述成更广泛的自动执行权限升级。",
        confidence=89,
        primary_tags=["GitHub Copilot", "Model Access", "Billing Governance"],
        secondary_tags=["Multi-org Seats", "Usage billed to", "Policy"],
        score_kwargs={"novelty": 3, "significance": 4, "strategic": 4, "source_quality": 5, "actionability": 4, "model": 1, "agent_architecture": 1, "ai_product": 5, "macro": 1},
    ),
    row(
        id="2026-08-31-openai-polimill-japan-public-ai-infrastructure",
        lane="ai_macro",
        title="OpenAI / Polimill 给出一个不小的公共部门 AI 落地样本：约 1,050 个自治体、55 万名公职人员在用 QommonsAI",
        summary="OpenAI News RSS 可确认这篇 Polimill 客户案例首发于 8 月 31 日；正文称 Polimill 的公共部门产品 QommonsAI 已覆盖日本约 1,050 个自治体和约 55 万名公职人员，当前工作流包括议会答辩、公共服务、社保福利和法律检索，并通过跨自治体的议事录与行政资料标准化来做统一知识底座。文章还写到 Polimill 计划在 2026 年秋季推出 Qommons ONE，但那部分仍是 roadmap，不当作已上线事实。",
        priority="P2",
        signal_type="strategic_radar",
        content_type="official_release",
        information_type="enterprise_adoption",
        source="OpenAI",
        url="https://openai.com/index/polimill",
        published_at="2026-08-31T07:00:00Z",
        why="这条值得记的不是又一个‘某公司用了 AI’，而是公共部门 vertical AI 已经开始以跨自治体知识底座和统一工作台的形态扩张，规模也不是试点级别了。",
        personal="如果在看行业落地，最该拆的是知识底座怎么做跨机构标准化、管理员能限制哪些模型、审计记录怎么留，以及 roadmap 中的 super agent 什么时候真的落到可见产品面。",
        opportunity="可以把公共部门或强监管行业里的‘共享知识底座 + 组织策略控模 + 专业工作流代理’视为一个独立产品范式，而不只是通用聊天工具外加提示词。",
        risk="自治体覆盖、公职人员规模和 3-5x 开发提速都来自 OpenAI/Polimill 官方表述；Qommons ONE 和 super agent 仍是计划，不是已上线能力。",
        boundary="发布日期来自 OpenAI 官方 RSS；正文通过公开文本镜像核验。当前能确认的是现有 QommonsAI 的采用规模、工作流范围和管理控制，不能把秋季 rollout 计划写成已经上线。",
        confidence=87,
        primary_tags=["OpenAI", "Polimill", "Public Sector AI"],
        secondary_tags=["Japan", "QommonsAI", "Enterprise Adoption"],
        score_kwargs={"novelty": 4, "significance": 4, "strategic": 5, "source_quality": 4, "actionability": 3, "model": 1, "agent_architecture": 1, "ai_product": 3, "macro": 5},
        related_sources=[
            {"url": "https://openai.com/news/rss.xml", "type": "official_rss_date"}
        ],
    ),
]

for item in rows:
    if item["id"] == "2026-09-01-aws-mcp-stateless-migration-contract":
        item["questions_to_validate"] = [
            "现在还有多少客户端仍依赖 2025-era session 语义，legacy lane 的真实退场时间表是什么？",
            "MRTR、requestState 和 ownership enforcement 在现有 MCP 服务器里有没有被完整实现，而不是只改了 transport？",
            "删掉 sticky session 和 session store 之后，真实错误率、时延和成本曲线有没有被量化？",
        ]
        item["follow_up_triggers"] = [
            "官方 conformance suite 或主要 SDK 发布更多 2026-07-28 迁移结果",
            "大型 MCP host 公布遗留客户端流量归零和基础设施拆除复盘",
            "更多托管网关暴露 header 路由、trace 和 cacheScope 的默认策略",
        ]
    elif item["id"] == "2026-09-01-aws-dms-agent-review-boundary":
        item["questions_to_validate"] = [
            "assessment report 里的 AI-generated provenance 能否进入更正式的审批流或回归测试流水线？",
            "哪些 CRITICAL / HIGH action item 仍最常把团队拦在上线前，AWS 会不会继续补 deterministic rule coverage？",
            "agent 帮助修复 action items 后，最终 apply 到 target database 的人审和回滚链路是否足够清晰？",
        ]
        item["follow_up_triggers"] = [
            "DMS 文档或 release notes 披露更正式的 GA 状态、成功率或审计出口",
            "出现真实生产迁移复盘，说明 AI-assisted conversion 在复杂存储过程上的通过率与失败模式",
            "AWS 补充更明确的 apply gate、rollback 或 change-approval 设计",
        ]
    elif item["id"] == "2026-09-01-huggingface-webgpu-kernel-contracts":
        item["questions_to_validate"] = [
            "Fleet 收到更多 GPU / 浏览器结果后，kernel variant selection 会不会公开成更稳定的策略接口？",
            "207 个 kernels 往完整模型端到端推理迁移时，加载、编译和 I/O 开销会吞掉多少收益？",
            "这些 contract 会不会被 ONNX Runtime Web 或其他浏览器 runtime 正式接入，而不是停留在 Hugging Face 生态内？",
        ]
        item["follow_up_triggers"] = [
            "Hugging Face 发布更多 kernel 覆盖、更多设备实测或上游集成结果",
            "浏览器或 runtime 团队开始直接消费这些 versioned kernel artifacts",
            "出现跨设备失败案例或 correctness 回滚机制的公开说明",
        ]
    elif item["id"] == "2026-09-01-aws-agentcore-payments-trust-gate":
        item["questions_to_validate"] = [
            "t54 的 trust score 阈值、误拦截率和 endpoint reputation 更新频率会不会公开更多细节？",
            "`ProcessPayment` 的 audit trail 是否能直接满足企业财务或合规团队的对账要求？",
            "session spending limit、wallet provider 和 trust gate 在更多 agent marketplace 或自建工具链里是否还能保持同样的 fail-closed 约束？",
        ]
        item["follow_up_triggers"] = [
            "出现更多 AgentCore payments 生产案例或第三方审计数据",
            "AWS 公布管理员控制、限额策略模板或失败回滚细节",
            "x402 / MCP marketplace 在更广范围内披露采用与风控效果",
        ]
    elif item["id"] == "2026-09-01-github-copilot-billing-org-model-access":
        item["questions_to_validate"] = [
            "管理员能否更直观看到 seat 的 billing owner、模型白名单和用户最终生效权限？",
            "跨组织 seat 切换或付费归属调整时，历史审计和可用模型是否会出现短暂不一致？",
            "这套归属逻辑会不会扩展到 code review、cloud agent 或更多执行型 Copilot 能力？",
        ]
        item["follow_up_triggers"] = [
            "GitHub 补充管理员 UI、文档或审计报表截图",
            "更多 Copilot 能力开始显式绑定 billing owner 与 policy source",
            "企业用户公开多组织 seat 的迁移或治理复盘",
        ]
    elif item["id"] == "2026-08-31-openai-polimill-japan-public-ai-infrastructure":
        item["questions_to_validate"] = [
            "跨自治体知识底座如何做持续更新、权限隔离和审计留痕？",
            "Qommons ONE 的 super agent 到秋季 rollout 时，真实可见的对象、动作、审批和回滚边界是什么？",
            "公共部门规模采用是否会带动更正式的 procurement、预算和供应链结构变化？",
        ]
        item["follow_up_triggers"] = [
            "Polimill 或 OpenAI 发布 Qommons ONE 的正式上线材料、真实 UI 或管理员文档",
            "出现关于公共部门采用规模、留存或 workflow outcomes 的独立验证",
            "更多国家或地区出现类似跨机构公共 AI 工作台案例",
        ]

rows = sorted(rows, key=lambda r: (r["relevance_level"], r["topic_lane"], r["id"]))

ledger_sources = [
    {"id": 1, "title": rows[0]["title"], "url": "https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected", "publisher": "AWS", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 2, "title": next(r["title"] for r in rows if r["id"] == "2026-09-01-aws-dms-agent-review-boundary"), "url": "https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms", "publisher": "AWS", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 3, "title": next(r["title"] for r in rows if r["id"] == "2026-09-01-aws-agentcore-payments-trust-gate"), "url": "https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments", "publisher": "AWS", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 4, "title": next(r["title"] for r in rows if r["id"] == "2026-09-01-github-copilot-billing-org-model-access"), "url": "https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans", "publisher": "GitHub", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 5, "title": next(r["title"] for r in rows if r["id"] == "2026-09-01-huggingface-webgpu-kernel-contracts"), "url": "https://huggingface.co/blog/webgpu-kernels", "publisher": "Hugging Face", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 6, "title": "OpenAI News RSS", "url": "https://openai.com/news/rss.xml", "publisher": "OpenAI", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 7, "title": next(r["title"] for r in rows if r["id"] == "2026-08-31-openai-polimill-japan-public-ai-infrastructure"), "url": "https://r.jina.ai/http://openai.com/index/polimill/", "publisher": "OpenAI / r.jina.ai text mirror", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
]

citations = [{"id": item["id"], "url": item["url"]} for item in ledger_sources]

brief = f'''# AI Signal 日报｜{DATE}

**窗口：** 北京时间 2026-09-02 00:00 至 {RUN_AT.strftime("%Y-%m-%d %H:%M")}   
**一句话结论：** 00:00 的基线循环先把今天写成了 0 条，但对 98 个真新增候选补做正文核验后，正式补入 6 条：AWS 拿出 3 篇能直接抄到控制面的正文，Hugging Face 把浏览器本地推理拆成可版本化 kernel 层，GitHub Copilot 收紧多组织模型权限，OpenAI / Polimill 则给出一个不小的日本公共部门 AI 落地样本。[1][2][3][4][5][6][7]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 1 | Hugging Face 把 WebGPU kernel 做成独立 contract + Fleet 证据层 |
| Agent 架构 | 2 | AWS 把 MCP 无状态迁移和 agent 支付 trust gate 都讲成了控制面 |
| AI 产品 | 2 | DMS agent 的人审边界被写清，Copilot 把模型权限绑回付费组织 |
| AI 宏观 | 1 | Polimill 公共部门 AI 覆盖面已到约 1,050 个自治体、55 万名公职人员 |

## 模型｜1 条

### Hugging Face：浏览器推理开始有自己的“底层合同”了

Hugging Face 发布 `@huggingface/kernels`，把 207 个 WebGPU kernels 作为独立、可版本化的 Hub 对象公开，每个 kernel 都带 manifest、correctness cases、bench cases 和 WGSL 模板；同时上线 Fleet，在浏览器里收集跨设备 benchmark 和正确性证据。[5]

**为什么重要：** 这不是又一个 local AI 演示页。更实在的变化是，WebAI 的底层算子终于能被单独检查、版本化和复现，而不是全都闷在 runtime 黑盒里。

## Agent 架构｜2 条

### AWS：MCP 无状态之后，哪些旧基础设施真的可以删

AWS 把 MCP 2026-07-28 版落到了部署细节：`initialize` 握手和 `Mcp-Session-Id` header 被拿掉，请求可以直接从 tool call 开始，任何实例都能响应；但只要还服务旧客户端，sticky session 和 session store 就不能提前拆。[1]

**为什么重要：** 很多团队现在最缺的不是“知道 MCP 变了”，而是知道该先记录什么流量、什么时候退遗留 lane、哪些会话基础设施终于能安全下线。

### AWS / t54：先过信任门，再让 agent 付钱

AWS 的 t54 案例把 agent 支付的硬边界写得很明确：x402-secure 先对 endpoint 和地址做实时评分，AgentCore payments 再负责 session spending limit、credential isolation 和结算；如果评分不过线或 URL 不匹配，付款直接在代码层被挡住，模型本身不能覆写。[3]

**为什么重要：** 这条真正有用的地方在于，它把“agent 会花真钱”拆成了可检查的控制点，而不是把风控继续留给 prompt 或人工抽查。

## AI 产品｜2 条

### AWS DMS：AI agent 能编排迁移，但不会替你背语义正确性

AWS DMS Schema Conversion 这篇正文展示了一条清晰的 agent 工作流：导入元数据、启动转换、等待完成、导出 assessment report、解释 CRITICAL action items；当 deterministic rule engine 兜不住时，生成式步骤只保证 PL/pgSQL 语法能过，语义正确性和最终上线责任仍然留给人审和功能测试。[2]

**为什么重要：** 这类边界越早写清楚，越不容易把“自动化很多步骤”误读成“迁移已经可直接上线”。

### GitHub Copilot：多组织用户现在只认付费组织的模型策略

GitHub 更新了 Copilot 的模型访问规则：如果用户同时在多个组织里持有 seat，模型可用性现在只由 `Usage billed to` 对应的付费组织决定；此前只要任一组织开了某个模型，用户就能用。纯 enterprise 来源的访问不受这次变化影响。[4]

**为什么重要：** 这不是花哨新功能，但它把模型选择、组织治理和结算归属绑成了一件事。企业里的“能不能选这个模型”以后会更像预算和 policy 的结果。

## AI 宏观｜1 条

### OpenAI / Polimill：日本公共部门 AI 已经不是小试点了

OpenAI News RSS 可确认，这篇 Polimill 客户案例首发于 8 月 31 日。正文称 QommonsAI 已覆盖日本约 1,050 个自治体和约 55 万名公职人员，当前场景包括议会答辩、公共服务、社保福利和法律检索；文中提到的 Qommons ONE 和 super agent 仍是 2026 年秋季 rollout 计划，不当作已上线事实。[6][7]

**为什么重要：** 这条值得记住，是因为它已经开始长成“共享知识底座 + 组织控模 + 专业工作流”的公共部门产品形态，而不是普通聊天工具试点。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新增满足模型主题边界和信息增量门槛的高管长文。

## AI 一线实践者观点｜0 条

本轮没有新的实践者原创内容进入正式日报。

## 排除与延后

- 83 个 OpenAI sitemap 命中先全部用官方 RSS 回填首发时间；其中 81 个是更早旧文，1 个是昨天已收录的 ChatGPT Ads，只有 Polimill 还保留为本轮可评正文。[6]
- Anthropic 那篇 `improving-alignment-security-efforts` 还是昨天同一条 canonical URL，没有看到足够开新卡的正文级增量。
- Google Security 这组是 Android 网络与数字身份安全，不进本 feed 的模型、agent、AI 产品或 AI 宏观正式范围。
- AWS hybrid cloud、ZS、Boomi、Wickr 和 Simon Willison 这些候选各有信息量，但今天没有一条同时满足正式范围与信息增量门槛。

## 证据边界

- AWS 这三条都来自官方正文，能确认对象、动作和控制面，但 t54 的交易规模、以及 DMS / MCP 迁移后的真实成功率与成本曲线仍主要缺少独立验证。[1][2][3]
- Hugging Face 的性能数字主要是 Apple M4 上的 op-level 对比，并明确排除了加载、编译、上传和回传开销；不要直接把它读成完整模型端到端时延承诺。[5]
- Copilot 这次改动只影响多组织 seat 场景；GitHub 没有把它描述成更广泛的自动执行权限升级。[4]
- Polimill 的覆盖规模和开发提速来自 OpenAI / Polimill 官方表述，Qommons ONE 仍是计划而不是已上线能力。[6][7]

## 飞书短版

**一句话结论：** 今天不是 0 条。对 98 个真新增候选补做正文核验后，正式补入 6 条，其中最值得看的三条都在 AWS：MCP 无状态迁移、DMS 迁移 agent 的人审边界、以及 AgentCore payments 的 trust gate。  
**组织判断：** 真正有价值的不是又多了几个新页面，而是控制面有没有写清楚，哪里必须停下来让人决定，哪里能被硬规则挡住。  
**建议动作：** 把 legacy lane sunset、AI 迁移 apply gate、agent 支付 risk gate、billing-owner entitlement 和 browser inference kernel contract 这五个点加入后续评估清单。  
**结果：** previous_count=0，new_count=6，updated_count=0，total_count=6。

## Sources

[1] https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected
[2] https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms
[3] https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments
[4] https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans
[5] https://huggingface.co/blog/webgpu-kernels
[6] https://openai.com/news/rss.xml
[7] https://r.jina.ai/http://openai.com/index/polimill/
'''

base_outline = [
    "已确认发生了什么",
    "关键对象与动作 / 控制面",
    "为什么这件事现在值得写",
    "证据边界和不能误写的地方",
    "对产品 / 架构判断的启发",
    "接下来要继续验证什么",
]


def topic(*, id: str, lane: str, signal_ids: list[str], title: str, tension: str, why_now: str, boundary: str,
          urls: list[str], audience: list[str], angle: str, timeliness: str = "this_week", priority: str = "A") -> dict:
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
                "outline": base_outline,
                "visual_direction": "对象—动作—控制面流程图，少量术语，结论先行",
                "cta": "你会先验收哪一个边界？",
            },
            "twitter": {
                "title": title,
                "hook": angle,
                "format": "7帖 Thread",
                "outline": base_outline,
                "visual_direction": "one architecture or workflow diagram",
                "cta": "What would you test first?",
            },
            "wechat": {
                "title": title,
                "hook": angle,
                "format": "1800—2400字深度文章",
                "outline": base_outline,
                "visual_direction": "工作流图、证据边界表、验证清单",
                "cta": "文末附可复用的验收问题",
            },
        },
    }


topics = [
    topic(
        id="2026-09-02-mcp-stateless-migration-checklist",
        lane="agent_architecture",
        signal_ids=["2026-09-01-aws-mcp-stateless-migration-contract"],
        title="MCP 无状态之后，哪些基础设施真的可以删，哪些现在还不能动",
        tension="协议变无状态不等于应用天然无状态，删基础设施太早会把旧客户端直接打断。",
        why_now="AWS 把 sticky session、session store、MRTR、trace 和 legacy lane 的迁移顺序讲成了可执行清单。",
        boundary="这是一份官方迁移指南，不是所有现网 MCP 服务器已经安全迁完的证明。",
        urls=["https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected"],
        audience=["Agent 平台团队", "基础设施工程师", "MCP 工具开发者"],
        angle="别只记住‘MCP 变无状态了’，更关键的是你还剩多少旧客户端，以及什么时候才能真的拆掉 session 基建。",
    ),
    topic(
        id="2026-09-02-dms-agent-human-review-boundary",
        lane="ai_product",
        signal_ids=["2026-09-01-aws-dms-agent-review-boundary"],
        title="AI 迁移工具最容易偷换的一件事：语法过关，不等于迁移已经正确",
        tension="团队容易把 agent 自动跑完流程误读成代码语义已经没问题。",
        why_now="AWS DMS 这篇把 deterministic rule、AI-assisted conversion、assessment report 和 CRITICAL action item 的人审边界都写清楚了。",
        boundary="官方正文确认工作流和 review gate，但没有把 AI 生成代码描述成语义等价保证。",
        urls=["https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms"],
        audience=["数据库迁移负责人", "企业架构师", "AI 产品经理"],
        angle="真正该设计的不是‘一键迁移’，而是 assessment export、人审队列、回归测试和 apply gate。",
    ),
    topic(
        id="2026-09-02-agent-payments-hard-gates",
        lane="agent_architecture",
        signal_ids=["2026-09-01-aws-agentcore-payments-trust-gate"],
        title="当 agent 真开始花钱，最重要的不是钱包，而是那道不能被模型绕过的硬门",
        tension="给 agent 钱包很容易，真正难的是额度、密钥、风险和审计谁来控制。",
        why_now="t54 案例把 trust score、session cap、credential isolation、audit trail 和 fail-closed gate 全部写到了正文里。",
        boundary="规模和效果数字主要来自 AWS / t54 自报，不是独立审计。",
        urls=["https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments"],
        audience=["Agent 产品负责人", "风控团队", "支付与平台工程师"],
        angle="别把 agent 支付理解成 API 调用加钱包地址，关键是信任判断必须先发生，且模型不能覆写。",
    ),
    topic(
        id="2026-09-02-webgpu-kernel-contracts",
        lane="model",
        signal_ids=["2026-09-01-huggingface-webgpu-kernel-contracts"],
        title="浏览器本地 AI 的关键变化，可能不在模型，而在底层 kernel contract 开始独立出来",
        tension="大家都在聊 local AI 模型和量化，真正难复用的却常常是底层算子实现和跨设备证据。",
        why_now="Hugging Face 把 207 个 WebGPU kernels、manifest、correctness cases 和 Fleet 一起公开了。",
        boundary="性能对比主要是官方 op-level 基准，不能直接当成完整模型端到端时延承诺。",
        urls=["https://huggingface.co/blog/webgpu-kernels"],
        audience=["WebAI 开发者", "前端工程师", "模型部署工程师"],
        angle="这次真正新鲜的不是‘浏览器也能跑 AI’，而是底层 kernel 开始拥有可版本化、可 benchmark、可验证的公共接口。",
    ),
    topic(
        id="2026-09-02-copilot-billing-owner-policy",
        lane="ai_product",
        signal_ids=["2026-09-01-github-copilot-billing-org-model-access"],
        title="多组织 AI 产品迟早会遇到的问题：模型权限到底听谁的，用户还是付费组织",
        tension="一个用户挂在多个组织上时，feature entitlement、结算归属和政策来源常常会互相打架。",
        why_now="GitHub 直接把 Copilot 的模型访问规则改成只认付费组织。",
        boundary="改动范围很具体，只影响多组织 seat 场景，不代表 Copilot 自动执行权限扩大。",
        urls=["https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans"],
        audience=["企业 AI 产品经理", "IT 管理员", "平台治理团队"],
        angle="模型下拉框背后，真正难的是 policy source of truth 和 billing owner 到底怎么绑定。",
    ),
    topic(
        id="2026-09-02-public-sector-ai-shared-foundation",
        lane="ai_macro",
        signal_ids=["2026-08-31-openai-polimill-japan-public-ai-infrastructure"],
        title="日本公共部门 AI 的下一步，也许不是更多聊天机器人，而是共享知识底座和统一工作台",
        tension="公共部门 AI 若只停在单点问答，很难形成跨机构的长期产品壁垒。",
        why_now="Polimill 案例给出了 1,050 个自治体、55 万名公职人员的采用规模，并把跨自治体知识底座写成了核心结构。",
        boundary="覆盖规模和成效来自官方表述；Qommons ONE 与 super agent 仍是 roadmap。",
        urls=["https://openai.com/index/polimill"],
        audience=["行业研究者", "政务产品团队", "企业战略负责人"],
        angle="真正值得盯的不是‘政府也在用 AI’，而是公共部门 vertical AI 正在长成共享知识底座加组织控模的产品形态。",
    ),
]

topics_payload = {
    "schema_version": 1,
    "report_date": DATE,
    "timezone": "Asia/Shanghai",
    "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。",
    "scope_label_cn": f"当日增量 · {DATE}",
    "source_scope": {"type": "daily", "date": DATE},
    "topics": topics,
}

lane_counts = Counter(item["topic_lane"] for item in rows)
priority_counts = Counter(item["relevance_level"] for item in rows)
decision_counts = Counter(item["decision"] for item in rows)

run_summary = {
    "run_type": "daily_four_lane_incremental_manual_review",
    "run_at": iso(RUN_AT),
    "deliverable_outcome": "success",
    "scheduler_outcome": "success",
    "window": {
        "timezone": "Asia/Shanghai",
        "start": iso(WINDOW_START),
        "end": iso(RUN_AT),
        "incremental_since": INCREMENTAL_SINCE,
    },
    "registered_sources": 111,
    "raw_candidates": 170,
    "unique_candidates": 132,
    "candidate_queue_count": 98,
    "new_in_run_count": 98,
    "reviewed_new_candidates": 98,
    "editorial_shortlist": 6,
    "previous_count": 0,
    "new_count": 6,
    "updated_count": 0,
    "excluded_count": 92,
    "unreviewed_candidate_count": 0,
    "total_count": 6,
    "selected": 6,
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
        "selected": 6,
        "candidate_only": 0,
        "checked_no_match": 92,
        "access_blocked": 0,
        "auth_required": 0,
        "mechanical_failure": 0,
        "not_checked": 0,
    },
    "review_notes": [
        "Reviewed only the 98 true new candidates from the 2026-09-02 00:00 baseline cycle and did not reopen the older queue.",
        "Mapped all 83 OpenAI sitemap hits through the official OpenAI News RSS before judging freshness. 81 resolved to older publication dates, one mapped to the already-selected ChatGPT Ads event from 2026-09-01, and only Polimill remained as a current reviewable body.",
        "Used direct first-party pages where available and a public text-mirror fallback for OpenAI pages that still returned 403 from this environment. Sitemap lastmod values and HTTP reachability were never promoted as publication evidence.",
        "Promoted six signals after body review: three AWS workflow/control-plane pieces, one Hugging Face browser inference infrastructure update, one GitHub Copilot governance update, and one OpenAI/Polimill public-sector adoption catch-up.",
        "Left Anthropic duplicate coverage, Google Security items, AWS hybrid cloud / Wickr / ZS / Boomi, and Simon Willison's Python item out because they were already represented, off-scope, or below the formal signal threshold.",
    ],
    "collection_contract": {
        "raw_candidates_in_rolling_window_is_not_increment": True,
        "candidate_queue_count_is_not_new_count": True,
        "sitemap_lastmod_is_not_publication_date": True,
        "feed_titles_require_body_verification": True,
        "http_2xx_is_not_checked_no_match": True,
    },
}


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


day = ROOT / "daily" / DATE
dump(day / "selected.json", rows)
dump(day / "citation-ledger.json", {"version": 1, "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.", "sources": ledger_sources})
dump(day / "citations.json", citations)
dump(day / "daily-brief.md", brief)
dump(day / "run-summary.json", run_summary)
dump(ROOT / "content-topics" / DATE / "topics.json", topics_payload)

print(json.dumps({
    "date": DATE,
    "signals": len(rows),
    "topics": len(topics),
    "run_summary": str(day / "run-summary.json"),
}, ensure_ascii=False))
