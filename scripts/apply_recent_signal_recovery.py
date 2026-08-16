#!/usr/bin/env python3
"""Apply the verified 2026-08-14 16:30–2026-08-17 recovery set.

This is an auditable one-shot recovery: every selected row is backed by an
opened primary page or an explicitly-labelled reported source. It never turns
search snippets, sitemap lastmod values, prerelease tags, or HTTP 200 responses
into confirmed Signals.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def scores(lane: str, source=5, significance=4, novelty=4, strategic=4, action=4):
    values = {
        "topic_relevance": 5,
        "novelty": novelty,
        "technical_or_product_significance": significance,
        "strategic_value": strategic,
        "source_quality": source,
        "model_value": 2,
        "agent_architecture_value": 2,
        "ai_product_value": 2,
        "macro_value": 2,
        "actionability": action,
    }
    values[{"model": "model_value", "agent_architecture": "agent_architecture_value", "ai_product": "ai_product_value", "ai_macro": "macro_value"}[lane]] = 5
    return values


def row(*, id, report, event, lane, title, summary, priority, signal_type, content_type,
        information_type, evidence, source, url, published, tags, why, personal,
        opportunity, risk, boundary, related=None, decision="include", confidence=94,
        score_kwargs=None):
    return {
        "id": id, "demo": False, "topic_lane": lane, "title": title,
        "summary": summary, "decision": decision, "confidence": confidence,
        "relevance_level": priority, "signal_type": signal_type,
        "content_type": content_type, "information_type": information_type,
        "evidence_level": evidence, "source": source, "url": url,
        "published_at": published, "primary_tags": tags[:3],
        "secondary_tags": tags[3:], "why_it_matters_cn": why,
        "personal_relevance_cn": personal, "product_opportunity_cn": opportunity,
        "competitive_risk_cn": risk,
        "recommended_action": "alert" if priority in {"P0", "P1"} else "track",
        "questions_to_validate": [
            "该变化在真实任务中的成功率、失败模式、成本和人工接管边界是什么？",
            "后续是否出现正式 GA、独立复现、监管细则或已签署文件？",
        ],
        "follow_up_triggers": [
            "来源方发布正式版本、实测数据或状态更新",
            "出现独立复现、已签署文件或生产采用证据",
        ],
        "scores": scores(lane, **(score_kwargs or {})),
        "report_date": report, "event_date": event,
        "canonical_url": url, "first_seen_date": report,
        "last_seen_date": report, "run_dates": [report],
        "evidence_boundary": boundary,
        **({"related_sources": related} if related else {}),
    }


D15 = [
row(
 id="2026-08-15-github-copilot-grok-46", report="2026-08-15", event="2026-08-15", lane="ai_product",
 title="GitHub Copilot 引入 Grok 4.6：覆盖 IDE、CLI 与云端 Agent，企业默认关闭并按量计费",
 summary="GitHub 开始向 Copilot Pro、Pro+、Max、Business 和 Enterprise 渐进开放 xAI Grok 4.6，覆盖 VS Code、Visual Studio、JetBrains、Xcode、Eclipse、Copilot CLI、cloud agent 与 Copilot app。Business/Enterprise 管理员必须显式开启 Grok 4.6 policy，策略默认关闭，使用量按模型供应商价格计费。",
 priority="P1", signal_type="competitor", content_type="official_release", information_type="product_workflow", evidence="confirmed", source="GitHub",
 url="https://github.blog/changelog/2026-08-14-grok-4-6-is-now-available-in-github-copilot/", published="2026-08-15T00:17:46+08:00",
 tags=["GitHub Copilot","Grok 4.6","Model Governance","Usage Billing"],
 why="模型选择已贯穿 IDE、CLI 和云端编码 Agent；默认关闭的组织策略与按量计费使模型白名单、数据政策和成本治理成为同一产品控制面。",
 personal="应比较 Grok 4.6 与 Gemini 3.7 Flash、GPT-5.6 Sol 在真实代码库长任务中的单位成功任务成本和人工接管率。",
 opportunity="可研究面向企业的模型策略、成本预算与任务级路由，而不是只做模型下拉框。",
 risk="渐进开放不等于全部用户已可见；官方未说明任务审批、暂停、日志或回滚发生变化。",
 boundary="官方确认开放范围、入口、组织策略和计费；未提供独立编码评测，也未扩大现有自动执行权限。"),
row(
 id="2026-08-15-anthropic-claude-text-watermark", report="2026-08-15", event="2026-08-14", lane="model",
 title="Anthropic 宣布未来 Claude 模型加入文本水印：采用 SynthID-Text 变体并准备检测 API",
 summary="Anthropic 宣布未来 Claude 模型生成的文本将加入 SynthID-Text 路线的水印，以履行 EU AI Act 透明度要求，并计划全球上线。水印不增加 token、不携带用户或组织身份；未来将提供检测 API。短文本、事实性段落、轻度校对和代码中的可检测信号较弱，完整重写可以移除水印。",
 priority="P0", signal_type="regulation", content_type="official_release", information_type="model_safety", evidence="confirmed", source="Anthropic",
 url="https://www.anthropic.com/news/claude-text-watermark", published="2026-08-14",
 tags=["Claude","Text Watermark","SynthID-Text","EU AI Act","C2PA"],
 why="模型输出溯源从研究机制进入头部模型默认生成路径，并直接受 EU AI Act 驱动；检测能力和误用边界会影响内容产品、合规与用户解释。",
 personal="后续应测试不同长度、改写比例、翻译和代码输出的检测召回与误报，不能把水印检测当作者身份判定。",
 opportunity="内容系统可把水印概率、C2PA 凭证和来源说明组合成分层溯源，而非二元 AI 检测。",
 risk="水印只说明 Claude 可能参与，不证明作者、所有权或具体用户；重写和短文本会降低检测能力。",
 boundary="发布日期来自官方页面日期；页面未给精确时区。质量无影响来自 Anthropic 内测及其引用研究，仍需独立检验。"),
row(
 id="2026-08-15-google-heir-private-inference", report="2026-08-15", event="2026-08-14", lane="model",
 title="Google 开源 HEIR 编译器：把预训练模型转换为同态加密推理，并公开四类示例源码",
 summary="Google 展示 HEIR（Homomorphic Encryption Intermediate Representation）开源编译器，可把在明文输入上运行的预训练模型转换为处理加密输入的推理程序。官方公开推荐、信用卡欺诈检测、加密流量异常检测和热词检测四类示例及源码，当前单线程 CPU 可运行，并与多家同态加密硬件团队合作。",
 priority="P1", signal_type="research", content_type="technical_update", information_type="model_deployment", evidence="confirmed", source="Google",
 url="https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/", published="2026-08-14",
 tags=["HEIR","Homomorphic Encryption","Private Inference","Open Source"],
 why="它把私有 AI 从只能本地推理或可信硬件扩展到纯密码学保护的云端计算路径，可能改变医疗、金融和跨机构模型部署边界。",
 personal="重点核验四个示例的真实模型规模、延迟、吞吐、密文膨胀和单位请求成本。",
 opportunity="可将高敏字段的加密推理作为混合架构的一层，而不是要求所有工作负载一次性迁移。",
 risk="同态加密仍有显著成本；官方尚未公布硬件加速后的生产延迟，所谓一键转换是愿景而非当前通用能力。",
 boundary="官方确认开源编译器、合作方、四个示例和源码；未宣称已经普遍生产可用。"),
row(
 id="2026-08-15-openai-agents-sdk-021", report="2026-08-15", event="2026-08-15", lane="agent_architecture",
 title="OpenAI Agents SDK v0.21：加入无供应商请求的确定性测试，并加固中断快照、递归审批与 MCP 生命周期",
 summary="OpenAI Agents SDK v0.21 新增 agents.testing、realtime.testing 和 voice.testing，可在不调用模型供应商的情况下确定性测试 Agent、Sandbox、Realtime 与 Voice 工作流；同时加固 RunState 中断快照、递归 agent-tool 审批、max-turn 收尾、流清理、敏感错误脱敏、MCP 生命周期快照隔离和重试上限。",
 priority="P0", signal_type="core", content_type="technical_update", information_type="agent_runtime", evidence="confirmed", source="OpenAI",
 url="https://github.com/openai/openai-agents-python/releases/tag/v0.21.0", published="2026-08-15T02:49:37Z",
 tags=["OpenAI Agents SDK","Deterministic Testing","Approval","MCP","RunState"],
 why="Agent 的可测试性、审批递归、中断恢复和敏感错误处理同时进入官方 SDK 合同，直接改善长任务和高风险执行的工程可靠性。",
 personal="应把中断、递归审批、最大轮次、流失败和 MCP 重连做成回归用例，而不是只测 happy path。",
 opportunity="可建立 provider-neutral 的 Agent 合同测试层，把模型调用与 Runtime 状态机测试解耦。",
 risk="这是 SDK 能力而非生产可靠性证明；需要核验复杂嵌套工具、并发流和自定义 provider 的边界。",
 boundary="内容来自官方 Release 与变更 PR；版本说明明确称没有已知破坏性 SDK 行为变化。"),
row(
 id="2026-08-15-claude-code-21233-runtime-controls", report="2026-08-15", event="2026-08-15", lane="agent_architecture",
 title="Claude Code v2.1.233 加固企业 Runtime：用户身份透传、Bash 内存上限与权限等待恢复",
 summary="Claude Code v2.1.233 增加可选 forward_user_identity，让 Apps Gateway 后方代理按用户归因支出；Linux Bash 工具可配置 memory cgroup 限额；修复云会话等待权限提示时被误判丢失、MCP v2 长连接反复重开和桌面/VS Code 权限通知 hook 不触发等问题。",
 priority="P1", signal_type="core", content_type="technical_update", information_type="agent_governance", evidence="confirmed", source="Anthropic",
 url="https://github.com/anthropics/claude-code/releases/tag/v2.1.233", published="2026-08-14T22:20:57Z",
 tags=["Claude Code","Identity Attribution","Resource Limit","Permission Prompt","MCP"],
 why="企业 Coding Agent 的成本归因、资源隔离、权限等待状态和 MCP 长连接恢复被放到明确控制面，而不是依赖外围脚本补救。",
 personal="应验证身份头的信任链、内存超限行为、权限等待期间的状态持久化和通知丢失率。",
 opportunity="可借鉴按用户归因的代理网关与工具级资源配额，建立多租户 Agent 的成本和故障隔离。",
 risk="身份透传和 cgroup 均为 opt-in；版本修复不代表所有云会话与 MCP 服务端组合已稳定。",
 boundary="官方 Release 明确列出新增项和修复项；未公开相关故障率或生产改善幅度。"),
row(
 id="2026-08-15-kimi-code-0361-control-plane", report="2026-08-15", event="2026-08-14", lane="ai_product",
 title="Kimi Code 0.36.1 重做多 Agent 控制面：Swarm 独立开关、子任务状态过滤与后台 Bash 可审计",
 summary="Kimi Code 0.36.1 将 Swarm 从 plan/goal 模式中拆成独立工具栏开关，重做子 Agent 卡片与状态过滤；后台 Bash 面板可按状态筛选并查看命令和输出。版本还修复第二次审批提示导致会话挂起、工具结果错序、MCP OAuth 取消后等待超时、运行中 fork 产生部分状态等问题。",
 priority="P1", signal_type="competitor", content_type="official_release", information_type="agent_product", evidence="confirmed", source="Moonshot AI",
 url="https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.36.1", published="2026-08-14T12:53:36Z",
 tags=["Kimi Code","Swarm","Subagent UI","Approval","Background Bash"],
 why="多 Agent 不再只是隐藏编排能力，而是出现可见的任务状态、后台命令输出和独立模式入口；同时暴露审批与历史一致性是实际故障面。",
 personal="应验收 Swarm 开关、子任务筛选、后台命令详情、审批恢复、长历史 fork 和失败状态是否一致。",
 opportunity="可把子 Agent、后台任务、审批和会话分叉统一为可观察、可筛选、可追溯的工作对象。",
 risk="大量变化集中在 Web UI 与缺陷修复；没有公开并发成功率、冲突率、成本和回滚能力。",
 boundary="官方 Release 和对应 PR 可核验；这不是 Kimi 基础模型或 Agent Swarm 新发布。"),
row(
 id="2026-08-15-aws-production-agent-patterns", report="2026-08-15", event="2026-08-15", lane="agent_architecture",
 title="AWS 连续公开三套生产 Agent 架构：网络层最小权限、共享文件交接与跨模型可观测",
 summary="AWS 三篇官方实作分别展示：用 VPC Lattice 对 Agent→私有数据请求执行 IAM/SigV4、HTTP 方法级限制和访问日志；用 S3 Files POSIX 目录作为多 Agent 持久工作记忆与交接层，并用 access point 隔离；在 AgentCore 中路由 Bedrock 与 SageMaker OpenAI-compatible 模型，并补齐后者默认缺失的 token 级 OpenTelemetry。",
 priority="P1", signal_type="research", content_type="technical_update", information_type="agent_architecture", evidence="confirmed", source="AWS",
 url="https://aws.amazon.com/blogs/networking-and-content-delivery/zero-trust-networking-for-agentic-ai-with-amazon-vpc-lattice/", published="2026-08-14T20:29:21Z",
 tags=["AWS","Zero Trust","Multi-agent Handoff","AgentCore","Observability"],
 why="它把 Agent 生产化的三类隐性问题——数据访问授权、跨 Agent 状态交接、异构模型成本追踪——具体化为可部署控制面。",
 personal="可复现实作并记录方法级拒绝、重复处理、目录一致性、token span 缺失和跨模型路由成本。",
 opportunity="以身份、文件状态和 trace 为统一对象，构建不依赖单一 Agent 框架的企业执行底座。",
 risk="VPC Lattice 医疗案例明确只是示例、未在临床生产验证；S3 Files 轮询和状态去重仍由应用承担。",
 boundary="三篇均为 AWS 官方技术实作并附架构/代码；它们是参考实现，不是生产效果或合规认证。",
 related=[
  {"url":"https://aws.amazon.com/blogs/storage/orchestrating-multi-agent-ai-architectures-with-amazon-s3-files/","type":"official_implementation"},
  {"url":"https://aws.amazon.com/blogs/machine-learning/building-agentic-workflows-with-sagemaker-ai-and-bedrock-agentcore/","type":"official_implementation"}
 ]),
row(
 id="2026-08-15-chatgpt-aug14-product-batch", report="2026-08-15", event="2026-08-14", lane="ai_product",
 title="ChatGPT 8 月 14 日批次：交互测验、项目记忆切换、个性化建议与 Linux 公测",
 summary="OpenAI Release Notes 的 8 月 14 日批次加入对话内交互测验、已有项目在 default/project-only memory 间切换、基于会话历史与连接工具的首页建议、Free/Go 网页手动 Think，以及 ChatGPT/Codex Linux 桌面应用公开预览。Linux 版可执行浏览器动作，但尚不能控制其他桌面应用。",
 priority="P1", signal_type="competitor", content_type="official_release", information_type="product_workflow", evidence="confirmed", source="OpenAI",
 url="https://help.openai.com/en/articles/6825453-chatgpt-release-notes", published="2026-08-14",
 tags=["ChatGPT","Project Memory","Linux","Browser Actions","Personalization"],
 why="同一批次同时改变学习交互、项目上下文隔离、个性化入口和桌面 Agent 的操作范围。",
 personal="重点核验 shared project 固定 project-only、设置延迟、连接工具使用和 Linux 浏览器动作的权限提示。",
 opportunity="可研究项目级记忆模式切换与建议入口，但需把上下文来源、共享边界和执行范围前置展示。",
 risk="滚动 Release Notes 只有日期粒度；Linux 仍为 preview，且不能控制浏览器外桌面应用。",
 boundary="官方正文确认功能与适用范围；条目仅标 August 14, 2026，无精确发布时间，文章级 updatedAt 不能当条目发布时间。",
 confidence=88),
row(
 id="2026-08-15-us-pax-silica-ai-alignment-draft", report="2026-08-15", event="2026-08-15", lane="ai_macro",
 title="美国据报拟要求 35 个 AI 合作伙伴在 Pax Silica 与中国框架之间选边",
 summary="Reuters 审阅的美国国务院内部草案拟告知 35 个 AI Opportunity Statement 签署方：若同时加入中国的竞争性 AI 合作框架，可能被排除在美国主导联盟之外。Pax Silica 涵盖 AI 模型、半导体、关键矿产、联合投资与出口控制，哈萨克斯坦目前被报道为唯一同时参与双方的国家。",
 priority="P1", signal_type="strategic_radar", content_type="media_report", information_type="regulation_policy", evidence="reported", source="Reuters via CNBC",
 url="https://www.cnbc.com/2026/08/15/us-to-tell-allies-they-must-pick-sides-in-ai-race-with-china-reuters.html", published="2026-08-16T06:49:03+08:00",
 tags=["Pax Silica","US-China AI","Export Controls","Critical Minerals"],
 why="若发送并执行，模型、芯片、关键矿产和开放权重生态可能进一步按地缘阵营分裂，影响跨国采购、供应链和模型可用性。",
 personal="跟踪正式信函、参与国回应、联盟规则、出口控制和联合投资项目，不把草案当成已生效政策。",
 opportunity="面向跨区域 AI 产品建立模型、芯片和数据供应链的政策依赖地图。",
 risk="草案未注明日期，Reuters 无法确认发送时间或最终措辞；国务院拒绝评论所谓泄露文件。",
 boundary="可信媒体获得内部草案与官员说法，但不是公开监管文件，也尚未发送或生效。",
 decision="watchlist", confidence=82, score_kwargs={"source":4,"strategic":5,"significance":5}),
]

D16 = [
row(
 id="2026-08-16-anthropic-decart-acquisition-talks", report="2026-08-16", event="2026-08-16", lane="ai_macro",
 title="Anthropic 据报接近以约 70 亿美元收购 Decart，但双方明确尚未签署协议",
 summary="Calcalist/CTech 报道 Anthropic 与以色列 AI 初创 Decart 已交换高级协议草案，创始人与主要投资者 Sequoia 倾向 Anthropic；潜在估值约 70 亿美元，多数对价预计为 Anthropic 股票。报道同时明确协议尚未签署，最快可能下月完成，Google、SpaceX 等仍可能介入。",
 priority="P2", signal_type="strategic_radar", content_type="media_report", information_type="industry_structure", evidence="reported", source="CTech",
 url="https://www.calcalistech.com/ctechnews/article/b1evv3aufg", published="2026-08-16T12:21:42+08:00",
 tags=["Anthropic","Decart","M&A","Inference Efficiency","Israel"],
 why="若完成，这将是 Anthropic 迄今最大收购之一，并可能把推理效率和实时视频能力、以色列研发中心及模型公司算力经济性合并到同一战略。",
 personal="跟踪签署文件、最终价格、技术整合、团队留任和 Anthropic 以色列研发中心，而不是提前判断交易已完成。",
 opportunity="可研究模型公司通过收购推理优化与实时生成能力来降低单位推理成本的路径。",
 risk="交易可能变更或失败；报道中的收入、IPO 和技术性能包含二手信息，不能当官方财务或性能数据。",
 boundary="CTech 明确称仍在高级谈判且无协议签署；因此仅列 strategic radar。",
 decision="watchlist", confidence=80, score_kwargs={"source":4,"strategic":5,"significance":5}),
row(
 id="2026-08-16-nvidia-sb-energy-openai-ohio-talks", report="2026-08-16", event="2026-08-15", lane="ai_macro",
 title="NVIDIA 据报拟向 SB Energy 投资至多 30 亿美元，配套 OpenAI 俄亥俄数据中心融资",
 summary="Reuters 报道 NVIDIA 正讨论向 SB Energy 投资至多 30 亿美元，作为 NVIDIA、OpenAI 与 SB Energy 围绕俄亥俄数据中心园区谈判的一部分；相关方案据报涉及约 1000 亿美元信用支持。该投资与融资安排仍处谈判阶段，尚无公司正式签署公告。",
 priority="P2", signal_type="strategic_radar", content_type="media_report", information_type="compute_infrastructure", evidence="reported", source="Reuters",
 url="https://www.reuters.com/business/nvidia-talks-invest-3-billion-sb-energy-part-openai-data-center-deal-information-2026-08-15/", published="2026-08-16T04:16:56+08:00",
 tags=["NVIDIA","SB Energy","OpenAI","Data Center","Credit Support"],
 why="若落地，芯片供应商将进一步以股权和信用支持绑定模型公司、电力与数据中心资产，重塑算力扩张的资本结构和风险分配。",
 personal="跟踪正式协议、园区容量、能源结构、信用担保方、建设节点和实际 GPU 采购。",
 opportunity="建立算力项目的芯片—能源—土地—融资关系图，识别模型公司资本开支外部化方式。",
 risk="核心数字来自媒体消息源；投资、信用支持和项目范围都可能变化，不能写成已完成交易。",
 boundary="Reuters 正文当前受访问验证限制；标题和多家转载可确认谈判口径，但无一手签署材料，故仅列 radar。",
 decision="watchlist", confidence=76, score_kwargs={"source":4,"strategic":5,"significance":5}),
]


def topic(tid, date, lane, signal_ids, title, tension, why, boundary, urls, audience, angle):
    base_outline = ["已确认发生了什么", "关键对象与工作流", "为什么现在重要", "失败与证据边界", "产品/架构判断", "下一步验证指标"]
    return {
        "id": tid, "status": "candidate", "timeliness": "this_week", "priority": "A",
        "topic_lane": lane, "source_signal_ids": signal_ids, "working_title_cn": title,
        "core_tension_cn": tension, "why_now_cn": why, "target_audience_cn": audience,
        "evidence_boundary_cn": boundary, "source_urls": urls,
        "platforms": {
            "xiaohongshu": {"title": title[:34], "hook": angle, "format": "7页图文卡", "outline": base_outline, "visual_direction": "暖中性色信息卡、对象—动作—控制面图", "cta": "你最想先验证哪一个边界？"},
            "twitter": {"title": title, "hook": angle, "format": "7帖 Thread", "outline": base_outline, "visual_direction": "one architecture/control-plane diagram", "cta": "What would you test first?"},
            "wechat": {"title": title, "hook": angle, "format": "2000—2500字深度文章", "outline": base_outline, "visual_direction": "架构图、证据边界表、验证指标清单", "cta": "文末附可复用验收清单"},
        },
    }

TOPICS15 = [
 topic("2026-08-15-watermark-is-not-authorship", "2026-08-15", "model", ["2026-08-15-anthropic-claude-text-watermark"], "Claude 文本水印上线后，为什么仍不能证明作者是谁", "可检测的模型参与不等于作者身份、所有权或内容真实性。", "头部模型开始把 EU AI Act 透明度要求写进生成路径。", "短文本、代码、轻度校对和完整重写会削弱检测。", ["https://www.anthropic.com/news/claude-text-watermark"], ["AI 产品经理","内容平台","合规与安全团队"], "水印解决的是‘模型可能参与’，不是‘谁写的’。"),
 topic("2026-08-15-agent-runtime-reliability-contract", "2026-08-15", "agent_architecture", ["2026-08-15-openai-agents-sdk-021","2026-08-15-claude-code-21233-runtime-controls","2026-08-15-kimi-code-0361-control-plane"], "三家 Agent 工具同一天修什么：审批、恢复、资源限制与可观察性", "Agent 的竞争正在从生成能力转向状态机和控制面可靠性。", "OpenAI、Anthropic、Moonshot 的正式 Release 同时暴露相似故障面。", "版本说明不等于故障率已被生产数据证明改善。", ["https://github.com/openai/openai-agents-python/releases/tag/v0.21.0","https://github.com/anthropics/claude-code/releases/tag/v2.1.233","https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.36.1"], ["Agent 工程师","AI 平台产品经理","Coding Agent 用户"], "真正难的不是多跑一个 Agent，而是它被打断、要审批、超资源后还能正确回来。"),
 topic("2026-08-15-production-agent-three-control-planes", "2026-08-15", "agent_architecture", ["2026-08-15-aws-production-agent-patterns"], "生产 Agent 的三个控制面：身份、共享状态与 Trace", "模型与工具之外，生产系统需要网络授权、跨 Agent 交接和异构模型成本追踪。", "AWS 同日公开三套有代码的参考实现。", "案例是参考架构，不是临床生产验证或合规认证。", ["https://aws.amazon.com/blogs/networking-and-content-delivery/zero-trust-networking-for-agentic-ai-with-amazon-vpc-lattice/"], ["企业架构师","Agent 平台团队","安全负责人"], "把 Agent 接进企业数据之前，先回答谁能读、状态放哪、调用如何追踪。"),
 topic("2026-08-15-copilot-model-policy", "2026-08-15", "ai_product", ["2026-08-15-github-copilot-grok-46"], "Copilot 加一个新模型，为什么企业真正要改的是策略和预算", "模型下拉框扩容会把数据政策、白名单和按量费用同时带进组织治理。", "Grok 4.6 已进入 Copilot 的 IDE、CLI 和云端 Agent 入口。", "渐进开放且企业默认关闭，未改变任务级审批与回滚。", ["https://github.blog/changelog/2026-08-14-grok-4-6-is-now-available-in-github-copilot/"], ["开发者平台产品经理","企业 IT","AI 成本负责人"], "新模型不是多一个选项，而是多一套成本、数据与任务适配决策。"),
]
TOPICS16 = [
 topic("2026-08-16-ai-infrastructure-capital-radar", "2026-08-16", "ai_macro", ["2026-08-16-anthropic-decart-acquisition-talks","2026-08-16-nvidia-sb-energy-openai-ohio-talks"], "模型公司的下一场竞争：收购推理技术，还是把算力融资绑定到芯片与能源", "两项都还未签署，却共同显示模型竞争正在向推理效率、能源和资本结构外溢。", "Anthropic–Decart 与 NVIDIA–SB Energy/OpenAI 谈判在同一周末进入公开报道。", "两项均为 reported radar，不得写成已完成交易。", ["https://www.calcalistech.com/ctechnews/article/b1evv3aufg","https://www.reuters.com/business/nvidia-talks-invest-3-billion-sb-energy-part-openai-data-center-deal-information-2026-08-15/"], ["AI 产业研究者","模型产品负责人","基础设施投资者"], "前沿模型的护城河正在从参数扩展到推理效率、能源和信用支持。"),
]


def write_day(date, rows, topics, excluded, updated_count=0):
    day = ROOT / "daily" / date
    day.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda x: (x["relevance_level"], x["topic_lane"], x["id"]))
    (day / "selected.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    ledger_sources=[]
    for i,r in enumerate(rows,1):
        ledger_sources.append({"id":i,"url":r["canonical_url"],"title":r["title"],"publisher":r["source"],"evidence_level":r["evidence_level"],"accessed":"2026-08-17"})
    ledger={"version":1,"grounding_policy":"Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.","sources":ledger_sources}
    (day/"citation-ledger.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    (day/"citations.json").write_text(json.dumps([{"id":s["id"],"url":s["url"]} for s in ledger_sources],ensure_ascii=False,indent=2)+"\n")
    lanes=Counter(r["topic_lane"] for r in rows); pri=Counter(r["relevance_level"] for r in rows); dec=Counter(r["decision"] for r in rows)
    source_lines="\n".join(f"[{s['id']}] {s['url']}" for s in ledger_sources)
    sections=[]
    labels={"model":"模型","agent_architecture":"Agent 架构","ai_product":"AI 产品","ai_macro":"AI 宏观"}
    for lane in ("model","agent_architecture","ai_product","ai_macro"):
        items=[(i+1,r) for i,r in enumerate(rows) if r["topic_lane"]==lane]
        body="\n\n".join(f"### {r['title']} [{i}]\n\n{r['summary']}\n\n**证据边界：** {r['evidence_boundary']}" for i,r in items) or "本日无新增唯一事件；不降低门槛。"
        sections.append(f"## {labels[lane]}｜{len(items)} 条\n\n{body}")
    excluded_lines="\n".join(f"- {x}" for x in excluded) or "- 无"
    sections_text = "\n\n".join(sections)
    brief=f"""# AI Signal 日报｜{date}

**补抓范围：** 上次成功运行后至 2026-08-17；事件日与报告日分开保存。  
**正式池：** {len(rows)} 条，其中 include {dec['include']}、strategic radar/watchlist {dec['watchlist']}；P0 {pri['P0']}、P1 {pri['P1']}、P2 {pri['P2']}。  
**一句话结论：** 旧任务的 0 条是召回故障；本次从官方 Release、RSS、Sitemap 后续正文和可信报道中恢复了 {len(rows)} 条事件，并保持证据等级和未签署边界。

## 四主线重点

| 主线 | 数量 |
|---|---:|
| 模型 | {lanes['model']} |
| Agent 架构 | {lanes['agent_architecture']} |
| AI 产品 | {lanes['ai_product']} |
| AI 宏观 | {lanes['ai_macro']} |

{sections_text}

## 模型大厂高管模型长文 / 访谈

本次没有把高管泛观点纳入；Dario Amodei 关于行业信任的发言因不以模型能力、训练、评测或路线为主而排除。

## AI 一线实践者观点

本次优先恢复正式发布与可复现架构；没有将搜索摘要或普通论坛帖子升级为实践者正式卡。

## 排除与延后

{excluded_lines}

## 证据边界

- `confirmed` 均已打开官方正文、Release 或代码；RSS/Sitemap 仅用于发现和日期核验。
- `reported` 项保留为 strategic radar；草案、谈判和拟投资均未写成已签署或已生效。
- 同一事件跨平台转载已合并；Codex alpha 空 Release、普通补丁和旧页面 lastmod 未进入正式池。

## 来源

{source_lines}
"""
    (day/"daily-brief.md").write_text(brief)
    run={
      "run_type":"three_day_recovery","run_at":"2026-08-17T03:03:00+08:00",
      "window":{"timezone":"Asia/Shanghai","start":"2026-08-14T16:30:00+08:00","end":"2026-08-17T03:03:00+08:00"},
      "raw_candidates": len(rows)+len(excluded), "unique_candidates":len(rows)+len(excluded),
      "editorial_shortlist":len(rows),"previous_count":0,"new_count":len(rows),"updated_count":updated_count,"total_count":len(rows),"selected":len(rows),
      "lane_counts":dict(lanes),"priority_counts":{k:pri[k] for k in ("P0","P1","P2","P3")},
      "decision_counts":dict(dec),"cross_day_duplicates_removed":0,"exclusions":excluded,
      "collection_contract":{"http_2xx_is_not_checked_no_match":True,"search_snippets_are_discovery_only":True,"sitemap_lastmod_is_not_publication_date":True}
    }
    (day/"run-summary.json").write_text(json.dumps(run,ensure_ascii=False,indent=2)+"\n")
    (day/"discovered-news.json").write_text(json.dumps({"window":run["window"],"selected_ids":[r["id"] for r in rows],"excluded_or_deferred":excluded},ensure_ascii=False,indent=2)+"\n")
    tdir=ROOT/"content-topics"/date; tdir.mkdir(parents=True,exist_ok=True)
    payload={"schema_version":1,"report_date":date,"timezone":"Asia/Shanghai","disclaimer_cn":"个人独立 AI 研究内容，不代表任何公司或机构。自动流程只生成 candidate，不自动发布。","scope_label_cn":f"最近三天补抓 · {date}","source_scope":{"type":"daily","date":date},"topics":topics}
    (tdir/"topics.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n")


def update_deepseek_status():
    p=ROOT/"daily/2026-08-14/selected.json"; rows=json.loads(p.read_text())
    for r in rows:
        if r["id"]=="2026-08-14-deepseek-v4-pro":
            r["last_seen_date"]="2026-08-17"
            r["run_dates"]=sorted(set(r.get("run_dates",[])+["2026-08-17"]))
            r["evidence_boundary"]="模型上线、API 兼容和价格来自 DeepSeek 官方；production gains 未给任务集。此前公告的峰谷定价已于 2026-08-16 16:00 UTC（北京时间 8 月 17 日 00:00）进入生效时点，仍需核验线上账单与缓存口径。"
    p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n")


def main():
    write_day("2026-08-15",D15,TOPICS15,[
      "OpenAI Sitemap 中 FedRAMP、Rosalind、Sora 等为旧页面近期 lastmod，按真实发布日期排除。",
      "HF State of Open Models 发布于北京时间 8 月 14 日 08:00，早于恢复窗口。",
      "Anthropic 多 Agent 研究发布于 8 月 13 日，早于恢复窗口。",
      "Codex 0.148 alpha Release 只有标签、无变更正文，不升正式卡。",
      "Dario Amodei 的信任危机发言不以模型本身为主题，按高管边界排除。",
    ])
    write_day("2026-08-16",D16,TOPICS16,[
      "Qwen 30 亿下载里程碑只有受阻媒体页面，缺少可访问的一手口径和统计定义，延后核验。",
      "NVIDIA 开发者论坛的个人量化帖子不是 NVIDIA 官方产品发布。",
      "普通融资、泛 AI 观点和内容农场转载全部排除。",
    ])
    update_deepseek_status()
    write_day("2026-08-17",[],[],[
      "截至补抓完成时，没有新增唯一正式事件；DeepSeek V4-Pro 峰谷定价生效按同一事件更新 8 月 14 日原卡，不重复建卡。",
      "Codex alpha Release 仅版本标签、无正式变更说明。",
    ],updated_count=1)
    print(json.dumps({"days":{"2026-08-15":len(D15),"2026-08-16":len(D16),"2026-08-17":0},"updated_existing":1,"topics":{"2026-08-15":len(TOPICS15),"2026-08-16":len(TOPICS16)}},ensure_ascii=False))

if __name__=="__main__": main()
