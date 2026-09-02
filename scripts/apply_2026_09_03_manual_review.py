#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-03"
TZ = ZoneInfo("Asia/Shanghai")
RUN_AT = datetime.now(TZ).replace(microsecond=0)
DISCOVERY_CUTOFF = datetime.fromisoformat("2026-09-03T00:01:55+08:00")
INCREMENTAL_SINCE = "2026-09-02T16:18:15+08:00"

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
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def event_date(value: str) -> str:
    return to_dt(value).astimezone(TZ).date().isoformat()


def scores(*, lane: str, novelty: int, significance: int, strategic: int, source_quality: int,
           actionability: int, model: int = 1, agent_architecture: int = 1,
           ai_product: int = 1, macro: int = 1) -> dict[str, int]:
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


def row(*, id: str, lane: str, title: str, summary: str, priority: str, signal_type: str,
        content_type: str, information_type: str, evidence_level: str, source: str,
        url: str, published_at: str, why: str, personal: str, opportunity: str,
        risk: str, boundary: str, confidence: int, primary_tags: list[str],
        secondary_tags: list[str], questions: list[str], triggers: list[str],
        score_kwargs: dict[str, int], related_sources: list[dict[str, str]] | None = None) -> dict:
    payload = {
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
        "evidence_level": evidence_level,
        "source": source,
        "url": url,
        "published_at": published_at,
        "primary_tags": primary_tags,
        "secondary_tags": secondary_tags,
        "why_it_matters_cn": why,
        "personal_relevance_cn": personal,
        "product_opportunity_cn": opportunity,
        "competitive_risk_cn": risk,
        "recommended_action": "investigate" if priority in {"P0", "P1"} else "monitor",
        "questions_to_validate": questions,
        "follow_up_triggers": triggers,
        "scores": scores(lane=lane, **score_kwargs),
        "report_date": DATE,
        "event_date": event_date(published_at),
        "canonical_url": url,
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": boundary,
    }
    if related_sources:
        payload["related_sources"] = related_sources
    return payload


rows = [
    row(
        id="2026-09-01-openai-astra-critical-cyber-threshold",
        lane="model",
        title="OpenAI 首次把 Astra 划进 Critical 网络安全阈值，并把最强能力先锁进小范围防守通道",
        summary="OpenAI 9 月 1 日的官方更新说，Astra 已达到 Preparedness Framework 的 Critical cybersecurity capability threshold：在合适工具和访问条件下，它能自己发现未知漏洞并构造针对加固系统的利用链。OpenAI 同时披露，为了补强滥用防护和未授权行动防护，团队推迟了 Astra 的部分开发与发布；最强网络安全能力会先给一小组测试者，之后再通过 Daybreak Blue 扩大到防守场景。",
        priority="P0",
        signal_type="strategic_radar",
        content_type="official_release",
        information_type="model_capability",
        evidence_level="primary_statement",
        source="OpenAI",
        url="https://openai.com/index/path-to-astra",
        published_at="2026-09-01T13:00:00Z",
        why="这不是普通 benchmark 更新。真正的信号是模型能力、发布节奏和访问控制一起变了：一旦厂商自己认定跨过 critical 线，先改的往往不是 UI，而是训练暂停、门控发布和 defender-only 通道。",
        personal="如果你在看 frontier model 风险和商业化节奏，这条最值得拆的是：阈值判定靠什么证据、哪些能力先不进默认面、Daybreak Blue 这类受限通道会不会成为高风险模型的标准发售路径。",
        opportunity="可以把高风险能力的 staged access、组织级审计、用途限制和 defender program，当成模型产品化的一层基础控制面。",
        risk="目前能确认的是 OpenAI 的官方自我判定、延后开发/发布和受限访问计划；系统卡、外部复现和真实攻击或防守效果还没公开。",
        boundary="首发时间来自 OpenAI News RSS；正文来自公开文本镜像。页面确认的是 OpenAI 对 Astra 能力阈值、开发延后和受限发布路径的官方表述，不等于独立第三方已经复现这些能力，也不能把“soon”写成正式全面发布。",
        confidence=92,
        primary_tags=["OpenAI", "Astra", "Cybersecurity Threshold"],
        secondary_tags=["Preparedness Framework", "Daybreak Blue", "Staged Access"],
        questions=[
            "OpenAI 会在系统卡里披露多少外部基准、真实漏洞链和防护失效率，而不是只给结论？",
            "Astra 的默认配置和 Daybreak Blue 之间到底隔着哪些工具权限、网络权限和用途限制？",
            "这种先卡住高风险能力、再走受限通道放量的模式，会不会成为下一批 frontier cyber 模型的默认发售方式？",
        ],
        triggers=[
            "OpenAI 发布 Astra system card、Preparedness 补充说明或外部评测结果",
            "Daybreak Blue 开始公开接入对象、审计字段或用量限制",
            "出现关于 Astra 漏洞发现、误报或滥用拦截效果的第三方复盘",
        ],
        score_kwargs={"novelty": 5, "significance": 5, "strategic": 5, "source_quality": 4, "actionability": 4, "model": 5, "agent_architecture": 2, "ai_product": 1, "macro": 3},
        related_sources=[
            {"url": "https://openai.com/news/rss.xml", "type": "official_rss_date"},
        ],
    ),
    row(
        id="2026-09-02-google-gemini-38-flash-cyber-fairwind",
        lane="model",
        title="Google 把 Gemini 3.8 Flash / Flash Cyber 一起推上台面：主力模型 GA，最强 cyber 能力只走 Fairwind",
        summary="Gemini API Changelog 已把 `gemini-3.8-flash` 标成 GA，定位是 long-horizon software engineering、autonomous agents 和 complex enterprise workflows。Google 同日的模型正文则把 3.8 Flash 定在 3.7 Flash 的同价位：每百万 input tokens 0.75 美元、output tokens 3.75 美元；同时发布 3.8 Flash Cyber，并通过 Fairwind Program + CodeMender 向受信防守方提供漏洞发现、验证和自动补丁能力。",
        priority="P0",
        signal_type="core",
        content_type="official_release",
        information_type="model_release",
        evidence_level="confirmed",
        source="Google",
        url="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
        published_at="2026-09-02T15:00:00Z",
        why="这次有意思的不是单一 benchmark 分数，而是 Google 把一个更强的 Flash 主力模型做成 GA，同时把最敏感的 cyber 能力装进受限项目和修复 harness 里。价格、分发和安全门是一套一起上的。",
        personal="如果你在做 agent、coding 或 security 产品，这条值得对照的是：同一基础模型怎么拆成公开 GA 面和 defender-only 面，哪些工作流会直接被 CodeMender 这类 harness 吸走。",
        opportunity="可以围绕低成本 frontier coding model、受限安全能力接入、补丁验证链路和 trusted-access onboarding 设计产品。",
        risk="性能、patch recall 和 Fairwind 参与规模都来自 Google 或合作方自报；3.8 Flash Cyber 也不是面向所有开发者的广泛 GA。",
        boundary="Gemini API changelog 能确认 3.8 Flash GA；Google Blog 与 Fairwind 页面能确认价格、Cyber 定位、CodeMender 集成和受限访问计划。外部基准与大规模实战效果仍主要依赖官方或合作方叙述。",
        confidence=94,
        primary_tags=["Google", "Gemini 3.8 Flash", "Fairwind"],
        secondary_tags=["Gemini 3.8 Flash Cyber", "CodeMender", "Cyber Defense"],
        questions=[
            "3.8 Flash 的真实单位任务成本，和 3.7 Flash 以及更高价 frontier 模型相比会差多少？",
            "Fairwind 的接入门槛、日志审计和输出限制，会不会成为企业拿到高风险模型能力的标配流程？",
            "CodeMender + Flash Cyber 的补丁验证链，能不能扩展到更多 CI、安全平台和企业内部代码库？",
        ],
        triggers=[
            "Google 发布更多 3.8 Flash 生产定价、配额或外部基准复盘",
            "Fairwind 披露更明确的 access policy、审计能力或 partner case study",
            "更多第三方公开比较 Flash Cyber 的漏洞发现、误报和 patch 质量",
        ],
        score_kwargs={"novelty": 5, "significance": 5, "strategic": 5, "source_quality": 5, "actionability": 4, "model": 5, "agent_architecture": 3, "ai_product": 2, "macro": 2},
        related_sources=[
            {"url": "https://ai.google.dev/gemini-api/docs/changelog", "type": "api_changelog"},
            {"url": "https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/", "type": "access_program"},
        ],
    ),
    row(
        id="2026-09-01-openai-chatgpt-healthcare-ehr-connectors",
        lane="ai_product",
        title="OpenAI 把 ChatGPT for Healthcare 接到 Epic 和 9 个官方医疗数据源，医疗问答开始贴着授权病历跑",
        summary="OpenAI 9 月 1 日的官方更新为 ChatGPT for Healthcare 新增 Epic EHR integration，并推出 Healthcare Public Data plugin，把 ClinicalTrials.gov、CMS Coverage、RxNorm、DailyMed 和 PubMed 等 9 个官方来源带进同一工作区。页面还写明两种落点：在 ChatGPT 内拉取授权病历上下文，或把 ChatGPT 直接嵌进 EHR workflow；官方医生评测给出 4,363 次打分中 99.1% safe，以及 5 个连接数据源上 93% 以上“good or better” accuracy。",
        priority="P1",
        signal_type="core",
        content_type="official_release",
        information_type="product_workflow",
        evidence_level="confirmed",
        source="OpenAI",
        url="https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources",
        published_at="2026-09-01T12:00:00Z",
        why="真正的新点不是又多一个医疗场景页，而是 ChatGPT 开始直接贴着授权 EHR 和可枚举的官方数据源工作，临床前置准备、药物核对和 trial 查询从开放问答走向受控工作流。",
        personal="如果你在做垂直 AI 产品，这条值得学的是：先把高价值上下文源接进来，再把引用、病历回链和 workflow embedding 做完整；这比单纯调高模型分数更像真正落地。",
        opportunity="可以围绕受权数据接入、source-backed answer、chart back-links、EHR embedded workflow 和领域评测，构建行业 AI 产品。",
        risk="安全率和准确率来自 OpenAI 的官方医生打分，不是独立临床试验，也不等同于自动诊疗许可。",
        boundary="首发时间来自 OpenAI News RSS；正文来自公开文本镜像。页面能确认 Epic 连接、Healthcare Public Data plugin、9 个官方来源和两种工作流形态；评测数字属于官方自报，不能写成独立临床验证。",
        confidence=90,
        primary_tags=["OpenAI", "ChatGPT for Healthcare", "Epic"],
        secondary_tags=["EHR Integration", "Healthcare Public Data", "Clinical Workflow"],
        questions=[
            "授权病历回链、引用展示和审计导出，在真实部署里会做到什么粒度？",
            "这套连接能力会先停留在回答层，还是继续扩展到更深的 order、handoff 或 care-ops workflow？",
            "当公开医疗数据和本地 EHR 信息冲突时，产品会怎样暴露来源、版本和人工复核节点？",
        ],
        triggers=[
            "OpenAI 公布更多医院或 payer 的真实部署、管理员控制面或 UI 细节",
            "Epic 集成开始出现更具体的上线范围、权限模型或合规材料",
            "第三方披露 connected EHR workflow 的安全性、准确率或使用复盘",
        ],
        score_kwargs={"novelty": 4, "significance": 5, "strategic": 4, "source_quality": 4, "actionability": 5, "model": 2, "agent_architecture": 2, "ai_product": 5, "macro": 1},
        related_sources=[
            {"url": "https://openai.com/news/rss.xml", "type": "official_rss_date"},
        ],
    ),
    row(
        id="2026-09-02-aws-strands-dynamodb-durable-storage",
        lane="agent_architecture",
        title="AWS 给 Strands Agents 补了一个持久存储后端：会话快照、长期记忆和 transcript 可以落在同一张 DynamoDB 表",
        summary="AWS 9 月 2 日发布 `strands-dynamodb-storage`，把 Strands 的 Storage contract 落成单表 DynamoDB 后端：session snapshot、memory、context offload 和 transcript 共用同一套 `write / read / delete / list` 接口。正文还给出几项真正影响运行面的细节：大于 400KB 的值可选 S3 offload，可选 gzip、TTL 和 multi-tenant prefix，并明确 backend 不自动创建表，基础设施权限与加密策略由使用方自己控制。",
        priority="P2",
        signal_type="research",
        content_type="technical_update",
        information_type="agent_runtime",
        evidence_level="confirmed",
        source="AWS",
        url="https://aws.amazon.com/blogs/database/introducing-strands-dynamodb-storage-durable-agent-storage-for-the-strands-agents-sdk/",
        published_at="2026-09-02T08:48:06-07:00",
        why="很多 agent 框架嘴上都有 memory，真正难的是把 session、long-term memory 和 transcript 放进一套明确 contract，且能在无状态 compute 上跑得住。这个后端把这层运维现实写出来了。",
        personal="如果你在做长任务或多租户 agent，最该对照的是单表 key 设计、超大 payload offload、TTL 清理和谁来管建表与权限，不是只看“支持 memory”这几个字。",
        opportunity="可以把 durable storage contract、租户隔离、归档策略和大对象 offload，做成 agent runtime 的标准能力。",
        risk="这还是 AWS / DynamoDB 路线，不是跨云抽象的通用答案；性能和成本曲线也没有给出大规模独立对比。",
        boundary="官方正文能确认 package 发布、接口映射、S3 offload、TTL、租户前缀和权限边界；不能把它写成 Strands 默认托管存储或通用 vector memory 标准。",
        confidence=88,
        primary_tags=["AWS", "Strands Agents", "DynamoDB"],
        secondary_tags=["Durable Storage", "TTL", "S3 Offload"],
        questions=[
            "这个 storage contract 在高并发长任务下会不会暴露新的一致性、压缩和 offload 读取瓶颈？",
            "多租户前缀和 TTL 策略，能不能直接满足团队级审计、保留期和删除要求？",
            "Strands 之后会不会把向量检索、回放审计或更细粒度的 state policy 也收进同一 contract？",
        ],
        triggers=[
            "AWS 或 Strands 团队发布更多生产性能、成本或故障恢复细节",
            "出现围绕 durable storage、tenant isolation 或 transcript retention 的真实部署复盘",
            "Strands 补充更多官方存储后端或管理控制面能力",
        ],
        score_kwargs={"novelty": 4, "significance": 4, "strategic": 3, "source_quality": 5, "actionability": 4, "model": 1, "agent_architecture": 5, "ai_product": 2, "macro": 1},
    ),
]

rows = sorted(rows, key=lambda r: (r["relevance_level"], r["topic_lane"], r["id"]))

ledger_sources = [
    {"id": 1, "title": "OpenAI News RSS", "url": "https://openai.com/news/rss.xml", "publisher": "OpenAI", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 2, "title": next(r["title"] for r in rows if r["id"] == "2026-09-01-openai-astra-critical-cyber-threshold"), "url": "https://r.jina.ai/http://openai.com/index/path-to-astra/", "publisher": "OpenAI / r.jina.ai text mirror", "evidence_level": "primary_statement", "accessed": iso(RUN_AT)},
    {"id": 3, "title": "Gemini API changelog", "url": "https://ai.google.dev/gemini-api/docs/changelog", "publisher": "Google", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 4, "title": next(r["title"] for r in rows if r["id"] == "2026-09-02-google-gemini-38-flash-cyber-fairwind"), "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/", "publisher": "Google", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 5, "title": "Fairwind Program", "url": "https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/", "publisher": "Google", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 6, "title": next(r["title"] for r in rows if r["id"] == "2026-09-01-openai-chatgpt-healthcare-ehr-connectors"), "url": "https://r.jina.ai/http://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/", "publisher": "OpenAI / r.jina.ai text mirror", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
    {"id": 7, "title": next(r["title"] for r in rows if r["id"] == "2026-09-02-aws-strands-dynamodb-durable-storage"), "url": "https://aws.amazon.com/blogs/database/introducing-strands-dynamodb-storage-durable-agent-storage-for-the-strands-agents-sdk/", "publisher": "AWS", "evidence_level": "confirmed", "accessed": iso(RUN_AT)},
]

citations = [{"id": item["id"], "url": item["url"]} for item in ledger_sources]

brief = f'''# AI Signal 日报｜{DATE}

**窗口：** 北京时间 2026-09-03 00:00 至 {DISCOVERY_CUTOFF.strftime("%Y-%m-%d %H:%M")}  
**一句话结论：** 这轮不是 0 条。对 92 个真新增候选补做正文核验后，正式补入 4 条：两条是昨晚漏后补证的 OpenAI catch-up，两条是 9 月 2 日深夜刚出现的一手更新。

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 2 | OpenAI 把 Astra 划进 Critical 阈值；Google 发布 Gemini 3.8 Flash / Flash Cyber + Fairwind |
| Agent 架构 | 1 | AWS 把 Strands 的持久存储 contract 真正写到运行面 |
| AI 产品 | 1 | OpenAI 把 ChatGPT for Healthcare 接进 Epic 与官方医疗数据源 |
| AI 宏观 | 0 | 无达到正式入选门槛的新增结构事件 |

## 模型｜2 条

### OpenAI：Astra 先跨线，再上锁

OpenAI 通过官方文章表示，Astra 已达到 Preparedness Framework 的 Critical cybersecurity capability threshold；文中说，该模型在合适工具和访问条件下可以发现未知漏洞并构造针对加固系统的利用链。OpenAI 同时披露，团队因此推迟了部分开发与发布，并计划先把最强 cyber 能力放给小范围测试者，再通过 Daybreak Blue 扩大到防守方。[1][2]

**为什么重要：** 一旦厂商自己认定模型跨过 critical 线，最先变化的往往不是功能页，而是训练节奏、权限边界和发售路径。

### Google：Gemini 3.8 Flash 公开 GA，Flash Cyber 则被装进 Fairwind

Gemini API changelog 已把 `gemini-3.8-flash` 标成 GA。Google 同日正文写明，3.8 Flash 维持 3.7 Flash 的定价，也就是每百万 input tokens 0.75 美元、output tokens 3.75 美元；同批发布的 3.8 Flash Cyber 则通过 Fairwind Program 和 CodeMender 面向受信防守方，Fairwind 页面还写到当前已有 650 多个参与伙伴。[3][4][5]

**为什么重要：** 这次不是单纯换个更强的 Flash 版本。Google 把公开主力模型、受限 cyber 能力和自动补丁 harness 一起推到了台前。

## Agent 架构｜1 条

### AWS：Strands 的 memory 不再只是一层抽象

AWS 新发的 `strands-dynamodb-storage`，把 Strands 的 storage contract 落成了单表 DynamoDB 后端：session snapshot、memory、context offload 和 transcript 共用同一套 `write / read / delete / list` 接口。正文还确认了几项会直接影响运行面的细节：大于 400KB 的值可选 S3 offload，可选 gzip、TTL 和 multi-tenant prefix，而且表、备份、标签和加密策略都由使用方自己管。[7]

**为什么重要：** 很多 agent 框架都说自己有 memory，真正难的是把状态和留痕放进一套能在无状态计算环境里跑得住的 contract。

## AI 产品｜1 条

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
- ChatGPT for Healthcare 这条能确认 Epic 连接、9 个官方数据源和两种工作流形态；99.1% safe 与 93% 以上 accuracy 仍属于 OpenAI 官方医生评测，不是独立临床验证。[1][6]
- AWS 这条能确认 storage contract、S3 offload、TTL 和租户前缀，但它仍是 DynamoDB 路线，不是跨云通用答案，也没有给出大规模独立成本对比。[7]

## 飞书短版

**一句话结论：** 这轮不是 0 条，补进了 4 条正式 signal。最重的两条在模型层：OpenAI 先把 Astra 划进 critical 线，再谈受限放量；Google 则把 Gemini 3.8 Flash 的 GA 和 Flash Cyber 的 Fairwind 分发一起推了出来。  
**组织判断：** 这轮最值得盯的，不只是模型更强，而是谁开始把高风险能力放进受限通道，谁又把行业工作流直接接到了真实上下文源上。  
**建议动作：** 把 high-risk model gating、defender-only access、行业数据连接、EHR embedded workflow 和 agent durable storage contract 一起加进后续评估清单。  
**结果：** previous_count=0，new_count=4，updated_count=0，total_count=4。

## Sources

[1] https://openai.com/news/rss.xml
[2] https://r.jina.ai/http://openai.com/index/path-to-astra/
[3] https://ai.google.dev/gemini-api/docs/changelog
[4] https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
[5] https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
[6] https://r.jina.ai/http://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
[7] https://aws.amazon.com/blogs/database/introducing-strands-dynamodb-storage-durable-agent-storage-for-the-strands-agents-sdk/
'''

base_outline = [
    "已确认发生了什么",
    "关键对象与动作 / 控制面",
    "为什么这件事现在值得写",
    "证据边界和不能误写的地方",
    "对产品 / 架构判断的启发",
    "接下来要继续验证什么",
]


def topic(*, id: str, lane: str, signal_ids: list[str], title: str, tension: str, why_now: str,
          boundary: str, urls: list[str], audience: list[str], angle: str,
          timeliness: str = "this_week", priority: str = "A") -> dict:
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
                "visual_direction": "对象—动作—权限边界图，少量术语，结论先行",
                "cta": "你最想先验证哪条控制边界？",
            },
            "twitter": {
                "title": title,
                "hook": angle,
                "format": "7帖 Thread",
                "outline": base_outline,
                "visual_direction": "one workflow or control-plane diagram",
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
        id="2026-09-03-high-risk-model-gating-astra",
        lane="model",
        signal_ids=["2026-09-01-openai-astra-critical-cyber-threshold"],
        title="当模型真的跨过 critical 线，先变化的往往不是功能，而是权限、隔离和发售路径",
        tension="大家容易盯着模型更强了，却忽略了高风险能力一旦跨线，真正难的是谁能拿到、怎么审计、何时放量。",
        why_now="OpenAI 把 Astra 划进 Critical 网络安全阈值，并把最强能力先锁进小范围测试与 Daybreak Blue 通道。",
        boundary="这仍是 OpenAI 官方自我判定，不是第三方独立复现，也不是全面开放。",
        urls=["https://openai.com/index/path-to-astra"],
        audience=["模型产品负责人", "安全团队", "AI 策略研究者"],
        angle="别只看模型更强了。更关键的是，高风险能力以后可能先以受限 access program 的形式卖给你。",
    ),
    topic(
        id="2026-09-03-gemini38-public-ga-vs-fairwind",
        lane="model",
        signal_ids=["2026-09-02-google-gemini-38-flash-cyber-fairwind"],
        title="Google 这次发的不是单一模型，而是“公开主力 Flash + 受限 cyber access”组合",
        tension="同一基础模型能力越强，公开 GA 面和受限高风险面往往会越分裂。",
        why_now="Gemini 3.8 Flash 已 GA，同日的 Flash Cyber 则被装进 Fairwind 和 CodeMender，走 defender-only 路线。",
        boundary="性能与 partner 覆盖规模仍主要来自 Google 或合作方叙述，Flash Cyber 也不是广泛 GA。",
        urls=["https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/"],
        audience=["Agent / coding 产品团队", "安全平台团队", "开发者工具从业者"],
        angle="真正值得看的是，谁开始把公开模型、受限 access 和自动补丁 harness 打包成一套发行策略。",
    ),
    topic(
        id="2026-09-03-healthcare-ai-needs-real-context",
        lane="ai_product",
        signal_ids=["2026-09-01-openai-chatgpt-healthcare-ehr-connectors"],
        title="医疗 AI 真正的门槛，不是回答更像医生，而是能不能贴着授权病历和官方数据源工作",
        tension="没有真实上下文源和回链，再好的模型也容易停在演示层。",
        why_now="OpenAI 把 ChatGPT for Healthcare 接进 Epic 和 9 个官方医疗来源，还支持嵌入 EHR workflow。",
        boundary="页面里的安全率和准确率属于官方医生评测，不是独立临床验证。",
        urls=["https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources"],
        audience=["垂直 AI 产品经理", "医疗信息化团队", "行业研究者"],
        angle="真正该学的不是模型分数，而是上下文接入、回链、workflow embedding 和审计边界怎么一起落地。",
    ),
    topic(
        id="2026-09-03-agent-durable-storage-contract",
        lane="agent_architecture",
        signal_ids=["2026-09-02-aws-strands-dynamodb-durable-storage"],
        title="Agent memory 进入基础设施期：session、memory 和 transcript 开始被收进同一套存储 contract",
        tension="大家都说 agent 需要 memory，但很少有人把大对象、TTL、多租户和权限边界真正讲清。",
        why_now="AWS 给 Strands Agents 发了 DynamoDB 持久存储后端，把 offload、TTL 和租户隔离写进了正文。",
        boundary="这是 DynamoDB 路线，不是跨云通用标准，也没有给出独立的大规模成本对比。",
        urls=["https://aws.amazon.com/blogs/database/introducing-strands-dynamodb-storage-durable-agent-storage-for-the-strands-agents-sdk/"],
        audience=["Agent runtime 工程师", "平台团队", "多租户应用开发者"],
        angle="别再只写“支持 memory”了。真正难的是把状态、留痕和大对象 offload 放进一套跑得住的 runtime contract。",
        priority="B",
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
        "start": "2026-09-03T00:00:00+08:00",
        "end": iso(DISCOVERY_CUTOFF),
        "incremental_since": INCREMENTAL_SINCE,
    },
    "registered_sources": 111,
    "raw_candidates": 210,
    "unique_candidates": 165,
    "candidate_queue_count": 92,
    "new_in_run_count": 92,
    "reviewed_new_candidates": 92,
    "editorial_shortlist": 6,
    "previous_count": 0,
    "new_count": 4,
    "updated_count": 0,
    "excluded_count": 88,
    "unreviewed_candidate_count": 0,
    "total_count": 4,
    "selected": 4,
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
        "selected": 4,
        "candidate_only": 0,
        "checked_no_match": 88,
        "access_blocked": 0,
        "auth_required": 0,
        "mechanical_failure": 0,
        "not_checked": 0,
    },
    "review_notes": [
        "Reviewed only the 92 true new candidates from the 2026-09-03 00:01 baseline cycle and did not rescan the 210-item rolling discovery pool.",
        "Mapped 78 OpenAI sitemap hits through the official OpenAI News RSS before freshness judgment. 75 resolved to older publication dates or already-covered URLs; only three late-discovered pages merited full body review, and only Astra plus the healthcare EHR integration cleared the formal bar.",
        "Used public text-mirror fallback for OpenAI pages that still block direct body retrieval from this environment. Sitemap lastmod values and HTTP reachability were never promoted as publication evidence.",
        "Promoted four signals after body review: OpenAI Astra critical-threshold gating, OpenAI healthcare EHR integration, Google Gemini 3.8 Flash / Flash Cyber with Fairwind gating, and AWS Strands durable storage for agent state.",
        "Left Anthropic worker retraining out because the page resolves to an Aug 12 publication date; left Kimi Code 0.40.1 and Codex 0.153.0-alpha.6 out because the release notes were too thin; left Google MrBeast, West Virginia energy, and OpenAI AI-native workflows out because they were off-scope or below the formal signal threshold.",
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
