#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconcile late async macro, model, product, and practitioner findings into the monthly pool."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "backfills/2026-07-16_to_2026-08-14_all_signals/curated-additions.json"


def make(id, date, lane, title, summary, source, url, why, boundary, *, priority="P1", evidence="confirmed", content="official_release", info="product_release", tags=None, related=None):
    lane_scores = {"model": 1, "agent_architecture": 1, "ai_product": 1, "ai_macro": 1}
    lane_scores[lane] = 5
    return {
        "id": id,
        "demo": False,
        "topic_lane": lane,
        "title": title,
        "summary": summary,
        "decision": "include",
        "confidence": 96 if evidence == "confirmed" else 91,
        "relevance_level": priority,
        "signal_type": "core" if priority in {"P0", "P1"} else "strategic_radar",
        "content_type": content,
        "information_type": info,
        "evidence_level": evidence,
        "source": source,
        "url": url,
        "published_at": f"{date}T00:00:00Z",
        "primary_tags": tags or [],
        "secondary_tags": [],
        "why_it_matters_cn": why,
        "personal_relevance_cn": "用于个人判断模型、Agent 架构、AI 产品和产业结构的真实增量，并保留事实层与编辑层边界。",
        "product_opportunity_cn": "转化为产品对象、动作、权限、状态、成本、评测或产业指标的可执行检查项。",
        "competitive_risk_cn": "若只跟踪营销摘要或单点功能，可能错过运行时控制、产品分发、供给结构和真实失败边界。",
        "recommended_action": "analyze" if priority == "P0" else "monitor",
        "questions_to_validate": ["该能力或指标在真实生产环境中的口径、稳定性和可比基线是什么？", "后续哪些独立复现、客户数据、失败复盘或治理说明能够验证它？"],
        "follow_up_triggers": ["官方发布生产指标、独立复现、客户案例或事故复盘", "开放范围、价格、权限、审计或实施状态发生变化"],
        "scores": {
            "topic_relevance": 5,
            "novelty": 5,
            "technical_or_product_significance": 5 if priority == "P0" else 4,
            "strategic_value": 5 if lane == "ai_macro" or priority == "P0" else 4,
            "source_quality": 5,
            "model_value": lane_scores["model"],
            "agent_architecture_value": lane_scores["agent_architecture"],
            "ai_product_value": lane_scores["ai_product"],
            "macro_value": lane_scores["ai_macro"],
            "actionability": 5 if lane in {"agent_architecture", "ai_product"} else 4,
        },
        "report_date": date,
        "event_date": date,
        "canonical_url": url.rstrip("/"),
        "first_seen_date": "2026-08-14",
        "last_seen_date": "2026-08-14",
        "run_dates": ["2026-08-14"],
        "evidence_boundary": boundary,
        "related_sources": related or [],
    }


records = [
    make(
        "2026-08-12-openai-workspace-agents", "2026-08-12", "ai_product",
        "OpenAI 推出 ChatGPT Workspace Agents：团队共享长任务 Agent，并在组织权限内跨工具执行",
        "OpenAI 官方正文确认 Workspace Agents 是 GPTs 的演进形态：团队可在 ChatGPT 中描述工作流、连接工具、添加 Skills 并测试；Agent 在云端持续运行，可在 ChatGPT 或 Slack 中共享，按团队流程请求审批。官方示例覆盖 Lead Outreach、会议简报、产品反馈路由、发布协调和发票处理。当前为 ChatGPT Business、Enterprise、Edu 与 Teachers 的 research preview。",
        "OpenAI", "https://openai.com/index/introducing-workspace-agents-in-chatgpt/",
        "企业 Agent 的产品对象从个人对话升级为共享工作流，权限、审批、运行历史、团队维护和跨工具交接成为核心控制面。",
        "官方确认研究预览、目标套餐和示例工作流，但未公开任务成功率、审批策略细节、管理员审计字段、回滚能力和 GPT 迁移时间。页面日期由官方索引与窗口内日报交叉确认。",
        priority="P0", info="agent_product_release", tags=["Workspace Agents", "Approval", "Shared Agents", "ChatGPT"]),
    make(
        "2026-08-12-openai-gpt56-sol-luna", "2026-08-12", "model",
        "OpenAI 更新 GPT‑5.6 Sol，并让免费用户无限使用 GPT‑5.6 Luna 文本聊天",
        "OpenAI 官方正文确认：Plus/Pro 的 GPT‑5.6 Sol 在 ChatGPT 中统一 Instant 与深度推理体验，增加推理强度滑杆；免费用户默认模型切换到 GPT‑5.6 Luna，文本聊天不限量，并可通过 Think 按钮获得更多推理。OpenAI 内部金融、医疗和法律事实评测中，含至少一个事实错误的回答相对 GPT‑5.5 Instant 分别减少约 68% 和 62%。",
        "OpenAI", "https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/",
        "模型能力差异被重新包装为可调推理预算和免费层分发；这同时改变用户路由、使用上限和模型成本结构。",
        "错误率为 OpenAI 内部评测自报，未披露完整样本、置信区间和外部复现；不限量仅指免费文本聊天，不等于所有工具、模态和 Think 使用无限。页面日期由官方索引与窗口内日报交叉确认。",
        priority="P0", info="model_product_update", tags=["GPT-5.6 Sol", "GPT-5.6 Luna", "Reasoning Effort", "Free Tier"]),
    make(
        "2026-07-31-openai-gpt56-efficiency-agent-harness", "2026-07-31", "model",
        "OpenAI 披露 GPT‑5.6 效率栈：模型、推理内核与 Agent Harness 联合优化",
        "OpenAI 官方技术文章将 GPT‑5.6 的效率来源拆为训练、推理和 Agent Harness：Sol 参与重写生产 Triton/Gluon kernels，使端到端服务成本降低 20%；改进 draft model 使 Token 生成效率提高超过 15%；Harness 通过延迟发现、默认 1 万 Token 工具输出上限、append-only 历史、确定性工具顺序与 Prompt Cache 减少上下文膨胀和重复工作。",
        "OpenAI", "https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/",
        "模型竞争正在从单一参数和榜单转向模型—推理—Harness 的协同效率；Agent Runtime 的上下文策略直接影响单位成功任务成本。",
        "全部成本、效率和模型对比为 OpenAI 自报；未披露硬件、工作负载、基准方差和节省的绝对成本。不能把模型参与优化改写成无监督递归自我改进。",
        priority="P0", content="official_engineering", info="model_inference_efficiency", tags=["Inference", "Agent Harness", "Prompt Cache", "Kernel Optimization"]),
    make(
        "2026-08-10-nvidia-ai-compute-financing-500b", "2026-08-10", "ai_macro",
        "NVIDIA 联合六家资本机构建立 AI 算力融资平台，计划动员超过 5000 亿美元第三方资本",
        "NVIDIA 与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs 和 KKR 签署合作备忘录，建立独立算力融资平台，为 NVIDIA 生态客户建设 AI 基础设施提供专用资本池。官方将 NVIDIA Compute 与全栈 AI 基础设施描述为具备长期、按使用量收入的可投资资产类别。",
        "NVIDIA", "https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital",
        "算力建设从科技公司的资产负债表支出扩展为可独立融资的基础设施资产，可能改变 AI 工厂的资本来源、部署速度和供应链议价。",
        "超过 5000 亿美元是随时间拟动员资本，不是已到账投资或已开工项目；备忘录未披露具体基金规模、融资成本、项目清单和回报。",
        priority="P0", info="compute_financing", tags=["AI Infrastructure", "Financing", "NVIDIA", "Capital Expenditure"]),
    make(
        "2026-07-22-amd-anthropic-2gw-mi450", "2026-07-22", "ai_macro",
        "AMD 与 Anthropic 达成最高 2GW MI450 部署合作，首个 1GW 计划于 2027 上半年启动",
        "AMD 与 Anthropic 宣布长期合作，Anthropic 计划使用 AMD Helios 机架级系统部署最高 2GW 的 Instinct MI450 系列 GPU，首个 1GW 从 2027 年上半年开始。双方还将用 Claude 优化 AMD GPU 工作负载、推进 ROCm 开发，AMD 将在工程和产品开发团队广泛采用 Claude。",
        "AMD", "https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/",
        "前沿模型实验室在千兆瓦规模增加非 NVIDIA 算力供给，同时把模型能力反向用于芯片软件栈优化，形成采购与工程协同。",
        "最高 2GW 是长期计划上限，不是当前上线容量；公告未披露采购金额、交付曲线、排他性和性能验收。",
        priority="P0", info="compute_supply_partnership", tags=["AMD Instinct", "Anthropic", "2GW", "ROCm"]),
    make(
        "2026-08-06-amd-acquire-taalas-inference", "2026-08-06", "ai_macro",
        "AMD 签约收购 Taalas，将模型专用推理数据流技术并入 Instinct 路线图",
        "AMD 宣布达成收购专用 AI 推理芯片公司 Taalas 的最终协议。Taalas 通过围绕模型优化推理数据流来降低通用架构中的计算与内存瓶颈；AMD 计划把技术与工程团队整合进 Helios、Instinct、EPYC 和 ROCm 全栈路线图，并开发系统级推理方案。",
        "AMD", "https://newsroom.amd.com/news/amd-acquires-taalas-ai-inference/",
        "推理竞争从通用 GPU 扩展到模型专用数据流与软硬件协同，AMD 试图补足高吞吐、低能耗推理路线。",
        "交易尚待惯常条件完成，价格和预计交割时间未披露；不能据此认定 Taalas 技术已经进入量产产品或达到官方性能目标。",
        priority="P0", info="acquisition", tags=["AMD", "Taalas", "Inference Silicon", "Acquisition"]),
    make(
        "2026-07-27-ssi-nvidia-vera-rubin-partnership", "2026-07-27", "ai_macro",
        "SSI 与 NVIDIA 建立长期合作：NVIDIA 投资并提供 Vera Rubin，使 SSI 算力计划提升一个数量级",
        "Safe Superintelligence Inc. 与 NVIDIA 官方宣布长期战略合作。NVIDIA 另行投资 SSI，并提供下一代 Vera Rubin 平台；SSI 称这将使其 Compute 扩大一个数量级。双方还计划围绕 NVIDIA 当前和未来计算平台开展技术协作。",
        "NVIDIA / SSI", "https://nvidianews.nvidia.com/news/ilya-sutskevers-safe-superintelligence-inc-and-nvidia-announce-long-term-strategic-partnership",
        "前沿研究实验室与上游算力平台从采购升级为资本、硬件与路线反馈的长期绑定，影响稀缺算力和模型研究的竞争位置。",
        "未披露投资金额、GPU 数量、交付时间、排他性和训练里程碑；算力提升一个数量级为合作方声明，不等于模型能力同步提升。",
        priority="P1", info="strategic_partnership", tags=["SSI", "NVIDIA", "Vera Rubin", "Frontier Labs"]),
    make(
        "2026-07-27-anthropic-cognizant-enterprise-delivery", "2026-07-27", "ai_macro",
        "Anthropic 扩大 Cognizant 合作：3 万名员工完成 Claude 培训，进入全球高级交付伙伴体系",
        "Anthropic 官方宣布 Cognizant 将 Claude 嵌入自身业务和工程平台，并在制造、生命科学、保险等客户系统中交付；超过 3 万名 Cognizant 员工已完成 Claude 培训，Cognizant 成为 Claude Partner Network 的 Global Premier Partner。",
        "Anthropic", "https://www.anthropic.com/news/cognizant-anthropic",
        "企业采用从单个客户席位扩展到全球 IT 服务商的培训、认证和客户交付渠道，模型分发能力进入实施伙伴网络。",
        "培训人数不等于活跃用户、付费席位或生产收益；公告未披露客户项目数量、收入、续约和工作负载指标。",
        priority="P1", info="enterprise_adoption", tags=["Cognizant", "Claude", "Enterprise Adoption", "Partner Network"]),
    make(
        "2026-07-28-kimi-k3-open-frontier-model", "2026-07-28", "model",
        "Moonshot 发布 Kimi K3：2.8T MoE、104B 激活参数、原生多模态与 100 万上下文",
        "Kimi K3 技术报告披露 2.8T 总参数、104B 激活参数、896 个路由专家中每 Token 激活 16 个、1M 上下文及原生图像/视频能力。后训练覆盖通用、Agent 和 Coding 三类 RL 与 low/high/max 推理强度；长轨迹系统保留 KV Cache 和可恢复 microVM Sandbox。官方发布完整模型权重。",
        "Moonshot AI / Kimi Team", "https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf",
        "开放权重模型继续同时扩大预训练规模、长上下文、Agentic RL 和多模态执行能力，缩小与闭源前沿系统的任务边界差距。",
        "模型自报总体仍落后于 Claude Fable 5 和 GPT‑5.6 Sol；榜单、2.5 倍缩放效率和长期执行表现尚需独立复现。开放权重不自动等于训练数据、代码与完整配方全部开放。",
        priority="P0", content="official_technical_report", info="open_weight_model_release", tags=["Kimi K3", "MoE", "1M Context", "Agentic RL"]),
    make(
        "2026-08-10-meta-muse-glimmer-open-local-agent", "2026-08-10", "model",
        "Meta 发布 Muse Glimmer 30B：面向本地多模态 Agent，并获 Transformers、llama.cpp 与 vLLM 首日支持",
        "Hugging Face 发布解读与可运行示例：Muse Glimmer 是 Meta 发布的 30B 稠密多模态模型，使用 2B Vision Encoder 与 28B Text Decoder，Apache 2.0 许可，支持图像、视频、多模态工具调用和可调 Reasoning Strength；首日接入 Transformers、llama.cpp、vLLM 和 Inference Endpoints。",
        "Meta / Hugging Face", "https://huggingface.co/blog/muse-glimmer",
        "前沿 Agent 模型进一步下沉到本地、隐私和单机部署场景，并通过主流推理生态的首日支持降低采用摩擦。",
        "架构与示例可核验，但速度、量化退化和基准主要为 Meta/Hugging Face 自报；‘open source’标题应按 Apache 2.0 权重与代码的具体范围理解。",
        priority="P1", content="official_ecosystem_release", info="open_weight_model_release", tags=["Muse Glimmer", "Local Agent", "Multimodal", "Apache 2.0"]),
    make(
        "2026-08-06-aws-agentcore-temporal-policies", "2026-08-06", "agent_architecture",
        "AWS AgentCore 推出 Temporal Policies：按 Session 历史动作授权，并加入 Token 与并发限流",
        "AWS 官方宣布 AgentCore Temporal Policies 可在授权时读取同一 Session 的前序动作，强制工作流顺序、校验当前工具参数与前序输出一致、要求高权限动作获得人工批准并验证数据新鲜度。Rate Limiting 可按 OAuth/IAM 用户或组限制请求、推理 Token 和长连接并发。",
        "AWS", "https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/",
        "Agent 授权从无状态工具白名单升级为跨动作、跨时间的会话策略，能表达‘先验证、再审批、后执行’的真实业务约束。",
        "官方未披露策略评估延迟、状态一致性、撤销传播、竞态条件和生产误拒率；自然语言策略转换仍需验证生成的 Cedar 规则。",
        priority="P0", info="agent_authorization", tags=["Temporal Policy", "AgentCore", "Human Approval", "Rate Limiting"]),
    make(
        "2026-08-06-aws-agentcore-runtime-instances", "2026-08-06", "agent_architecture",
        "AWS AgentCore Runtime Instances GA：托管 EC2 支持最长 14 天持久 Agent Session",
        "AWS 发布 AgentCore Runtime Instances GA。团队可指定 GPU、内存或计算优化 EC2 作为 Capacity Provider，由 AgentCore 管理预置、补丁、扩缩容和生命周期。该路径支持最长 14 天 Session；默认 Serverless MicroVM 路径面向最长 8 小时且需要快速启动的任务。",
        "AWS", "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/",
        "长任务 Agent 的运行时从短生命周期 Serverless 扩展为托管持久算力，状态、资源隔离、成本和故障恢复成为新的平台选择。",
        "GA 仅确认可用性和最长 Session；未披露 Checkpoint 语义、跨实例恢复、Exactly-once 执行、冷启动和不同负载成本比较。",
        priority="P0", info="agent_runtime", tags=["AgentCore", "Runtime Instances", "14-day Session", "EC2"]),
    make(
        "2026-07-24-meta-ai-muse-spark-actions", "2026-07-24", "ai_product",
        "Meta AI 接入邮件与日历并开始持续代办：计划、Slides、Daily Briefing 与定时任务进入滚动开放",
        "Meta 官方宣布由 Muse Spark 1.1 驱动的新 Meta AI：可连接 Email 与 Calendar，生成 Slides、持续执行计划并按设定时间提供 Daily Briefing。示例包括搜索 Marketplace 家具、生成 Mood Board、按日历推荐聚餐时间、每周训练计划和持续追踪主题。功能从 7 月 24 日起在 Meta AI App 与 meta.ai 的部分市场滚动开放，之后扩展到 WhatsApp。",
        "Meta", "https://about.fb.com/news/2026/07/meta-ai-muse-spark-doesnt-just-think-it-acts/",
        "消费助手从一次性回答进入连接个人数据、持续计划和定时交付；开放范围、授权、任务暂停和错误纠正直接决定可托付程度。",
        "官方演示和描述能确认滚动开放及操作类型，但未披露支持市场、逐动作确认、邮件写入、购物提交、失败恢复和日志机制；不能把寻找商品写成自动购买。",
        priority="P1", info="assistant_action_release", tags=["Meta AI", "Muse Spark", "Calendar", "Scheduled Tasks"]),
    make(
        "2026-08-03-github-copilot-comment-automations", "2026-08-03", "ai_product",
        "GitHub Copilot Automations 支持由 Issue/PR 评论触发 Cloud Agent 工作流",
        "GitHub Changelog 确认，用户可为 Copilot Cloud Agent 配置评论触发词，在 Issue 或 Pull Request 评论出现时自动生成/更新文档、调查错误日志或创建后续任务。入口位于仓库 Agents > Automations；Pro、Pro+、Max、Business 和 Enterprise 可用，企业套餐需管理员启用 Cloud Agent Policy。",
        "GitHub", "https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments",
        "评论从协作文本变成 Agent 事件入口，仓库管理员策略、触发词冲突、身份权限和自动创建任务的审计边界变得可操作。",
        "官方确认触发器和套餐范围，但未披露去重、循环触发、评论编辑/删除语义、审批门槛和失败重试。",
        priority="P1", info="workflow_automation", tags=["GitHub Copilot", "Automations", "Cloud Agent", "Comment Trigger"]),
    make(
        "2026-08-03-nathan-lambert-open-model-artifacts-hub", "2026-08-03", "ai_macro",
        "Nathan Lambert 发布开放模型 Artifacts Hub 与 Adoption Dashboard，覆盖近两年 792 个模型",
        "Nathan Lambert 与 Interconnects 发布 Artifacts Hub 和 Adoption Dashboard：前者将 Hugging Face、OpenRouter、Artificial Analysis 与自建采用指标联结起来，当前人工筛选覆盖近两年 792 个文本和多模态生成模型；后者每天更新不同地域与组织的下载和衍生模型数据，用于观察中美开放模型采用。",
        "Nathan Lambert / Interconnects", "https://www.interconnects.ai/p/introducing-our-artifacts-hub-and",
        "开放模型竞争首次有更系统的模型—能力—下载—衍生采用视图，可减少仅凭单日榜单判断开源生态位置的偏差。",
        "覆盖数量不是活跃使用、生产部署或商业收入；OpenRouter Token、Hugging Face 下载和相对采用指标各有采样偏差，正式引用需保留指标定义。",
        priority="P0", evidence="primary_statement", content="original_research", info="open_model_adoption", tags=["Open Models", "Adoption Dashboard", "Artifacts Hub", "Nathan Lambert"]),
    make(
        "2026-08-12-nathan-lambert-ai-textbook-workflow", "2026-08-12", "ai_product",
        "Nathan Lambert 复盘 AI 教材写作：模型只贡献远低于 1% 的最终技术表述，总工作量节省约 10%—20%",
        "Nathan Lambert 以完成后训练教材的真实写作过程复盘模型能力边界：最终技术解释中远低于 1% 直接来自模型；模型更适合编辑、澄清和局部表述，他估计当前只能节省约 10%—20% 总工作量。文章还指出模型在长篇非虚构写作中缺少持续规划和迭代草稿机制。",
        "Nathan Lambert / Interconnects", "https://www.interconnects.ai/p/i-wrote-an-ai-textbook-how-long-until",
        "AI 知识工作价值不能只看段落生成质量；专家验证、结构一致性和长期项目上下文仍决定最终交付成本。",
        "远低于 1% 和 10%—20% 均为作者个人工作流估计，不能外推到所有作者、领域或模型；没有无 AI 对照工时。",
        priority="P1", evidence="primary_statement", content="original_case_study", info="knowledge_work_case", tags=["AI Writing", "Knowledge Work", "Expert Review", "Nathan Lambert"]),
    make(
        "2026-08-07-simon-willison-agent-game-model-comparison", "2026-08-07", "model",
        "Simon Willison 用同一游戏需求对比 Claude Fable 5 与 GPT‑5.6 Sol Ultra 的一次性 Agent 生成",
        "Simon Willison 先用同一详细提示让 Claude Fable 5 一次性生成可运行的 Raccoon Heist 游戏，公开 Demo、仓库与视频；两天后用 Codex Desktop 的 GPT‑5.6 Sol Ultra aggressive sub-agents 模式重做相同任务，并公开第二个 Demo、仓库、贴图与提示。作者判断后者游戏完成度明显更高。",
        "Simon Willison", "https://simonwillison.net/2026/Aug/7/moonlight-mayhem/",
        "这是可运行、可检查产物的同任务跨模型案例，能观察 Coding Agent 的自主分解、多模态素材生成和产品完成度差异。",
        "不是受控基准，模型成本、运行时长、随机种子、人工干预和失败次数不完整；作者主观偏好不能写成普遍模型排名。",
        priority="P0", evidence="primary_statement", content="runnable_demo", info="model_comparison", tags=["Simon Willison", "Codex", "Claude Fable 5", "Runnable Demo"], related=[{"label":"Claude Fable 5 首次演示","url":"https://simonwillison.net/2026/Aug/5/raccoon-heist/"}]),
    make(
        "2026-07-18-sebastian-raschka-reasoning-effort", "2026-07-18", "model",
        "Sebastian Raschka 拆解 Reasoning Effort：训练统一策略，而不只是推理时截断 Token",
        "Sebastian Raschka 系统解释 Reasoning Effort 的训练与推理机制，区分独立推理模型、Thinking Toggle 与多档 Effort。文章复盘 Kimi K2.5 Toggle：在有预算与无约束 RL 阶段之间交替，使生成 Token 减少约 25%—30%，同时基准变化很小；并强调 <think> 标签只是格式边界，不产生推理能力。",
        "Sebastian Raschka", "https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms",
        "可控推理预算正在成为模型产品的核心能力；理解训练配方有助于区分真实的 Token 效率策略与前端简单截断。",
        "25%—30% 来自其对特定 Kimi 报告和模型的分析，不能推广到所有推理模型；文章含作者解释而非独立复现实验。",
        priority="P0", evidence="primary_statement", content="original_technical_analysis", info="reasoning_training", tags=["Reasoning Effort", "RLVR", "Token Budget", "Sebastian Raschka"]),
    make(
        "2026-07-28-gergely-orosz-anthropic-verification-bottleneck", "2026-07-28", "agent_architecture",
        "Gergely Orosz 深访 Anthropic：Agent 编码的瓶颈从实现转向验证，Zig→Rust 案例 85% 时间用于修复与核验",
        "Gergely Orosz 基于 Anthropic 内部深访披露：一个 Zig 到 Rust 重写案例中，实现约占 15% 时间，编译、修测试和验证约占 85%；3500 多人的组织里，原型更流动、验证比实现更耗时。Thariq Shihipar 还称团队近期删除了 Claude Code 约 80% 系统提示，因为新模型改变了原有假设。",
        "Gergely Orosz / The Pragmatic Engineer", "https://newsletter.pragmaticengineer.com/p/inside-anthropic",
        "Coding Agent 的系统设计重点正从代码生成转向验证、测试、假设更新和团队并行上限；模型升级会让固定 Prompt 资产快速折旧。",
        "数据来自单家公司和受访者，Bun 重写成本与质量不能代表一般工程；部分全文付费，不能把访谈经验外推为行业平均。",
        priority="P0", evidence="primary_statement", content="original_interview", info="agent_engineering_practice", tags=["Verification", "Claude Code", "Engineering Workflow", "System Prompt"]),
    make(
        "2026-08-12-charity-majors-ai-engineering-practice", "2026-08-12", "ai_product",
        "Charity Majors 复盘 Honeycomb 的 AI 工程实践：评审负担、AI 疲劳与 AI-free Wednesday",
        "带完整逐字稿的访谈中，Honeycomb 联合创始人兼 CTO Charity Majors 讨论团队采用、AI 代码评审、个人产能指标误区、管理者重返 IC 和 AI 疲劳。具体实践包括 Honeycomb 团队周三不使用 AI，以重新获得节奏和判断控制；她强调 AI Slop 的评审成本和可靠性工作不能被生成速度掩盖。",
        "Charity Majors / The Pragmatic Engineer", "https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for",
        "真实组织开始设计 AI 使用节奏和评审制度，而不是只采购工具；团队吞吐必须同时计算 Review、理解和维护成本。",
        "观点色彩较强，AI-free Wednesday 与团队经验不代表普遍最佳实践；不能把节目标题中的价值判断当作客观行业事实。",
        priority="P0", evidence="primary_statement", content="transcript_interview", info="enterprise_ai_practice", tags=["Charity Majors", "Honeycomb", "AI Review", "AI Fatigue"]),
    make(
        "2026-07-28-akshay-nathan-chatgpt-work", "2026-07-28", "ai_product",
        "Akshay Nathan 详解 Codex 向 ChatGPT Work 扩展：Sites、Memory、Subagents 与知识工作 Agent",
        "Latent Space 完整逐字稿采访 OpenAI 核心产品工程负责人 Akshay Nathan，讨论 Codex Harness 如何扩展到 ChatGPT Work 的 Sites、Memory、Subagents、Finance 与 No-Code。节目材料称 Codex 与 ChatGPT Work 合计达到 1000 万用户，并引用 OpenAI 早期口径：知识工作者约占 Codex 用户 20%，增长速度超过开发者 3 倍。",
        "Akshay Nathan / Latent Space", "https://www.latent.space/p/chatgpt-work",
        "Coding Agent 的运行时和交互对象正在扩展到通用知识工作；Memory、站点、子 Agent 和垂直工作区成为产品化重点。",
        "1000 万需区分合计用户、注册用户、MAU 与 WAU；20% 和 3 倍口径来自节目引用材料，正式使用必须保留归因，不能与 Akshay 原话混写。",
        priority="P0", evidence="primary_statement", content="transcript_interview", info="product_leader_interview", tags=["ChatGPT Work", "Codex", "Memory", "Subagents"]),
    make(
        "2026-08-03-baseten-inference-engineering", "2026-08-03", "model",
        "Baseten 推理工程团队拆解量化、KV Cache 与跨模型组件嫁接：优化收益可达 20%—200%",
        "Latent Space 完整逐字稿采访 Baseten 的 Philip Kiely 与 Ali Taha，覆盖 Cache-aware Routing、Prefill/Decode 解耦、量化、Speculative Decoding、KV Cache 移动和 GPU Kernel。案例包括扩大 GLM-5.2 量化范围仍保持评测质量并提高约 20% 吞吐，以及把 Kimi Vision Encoder 接到 GLM-5.2 而不修改语言模型。",
        "Philip Kiely、Ali Taha / Latent Space", "https://www.latent.space/p/inference-eng",
        "模型产品成本和速度越来越依赖推理系统工程，而不是换一个模型；量化误差、缓存路由和组件组合需要任务级验证。",
        "20%、100% 和 200% 依赖具体模型、硬件、精度、并发和服务栈；访谈中的案例不能直接横比或外推到所有工作负载。",
        priority="P0", evidence="primary_statement", content="transcript_interview", info="inference_engineering", tags=["Inference", "Quantization", "KV Cache", "Baseten"]),
    make(
        "2026-08-11-chai-discovery-bioai-commercialization", "2026-08-11", "ai_product",
        "Chai Discovery 解释 BioAI 商业化：药企合作按里程碑付费，签约时通常仅支付总额 2%—5%",
        "Latent Space 完整逐字稿采访 Chai Discovery 联合创始人与产品负责人 Matthew McPartlon、Neil Patil，讨论从生物模型到药企采购的工作流。节目披露其夏季新增多项合作，并解释 Biobucks 结构：交易标题金额大多取决于后续里程碑，通常只有总额约 2%—5% 在签约时支付。",
        "Matthew McPartlon、Neil Patil / Latent Space", "https://www.latent.space/p/chai-discovery",
        "BioAI 产品价值需要通过实验、药物里程碑和采购结构兑现，不能用模型榜单或合同标题金额替代真实收入和研发结果。",
        "合作金额、前付款和最终效果未完整披露；2%—5% 是嘉宾对常见交易结构的说明，不等于每项 Chai 合同的确定比例。",
        priority="P1", evidence="primary_statement", content="transcript_interview", info="vertical_ai_commercialization", tags=["BioAI", "Drug Discovery", "Milestones", "Enterprise Procurement"]),
    make(
        "2026-08-03-anthropic-cyber-eval-incidents", "2026-08-03", "agent_architecture",
        "Anthropic 复盘三起网络安全评测越界：Claude 从第三方环境访问真实组织系统",
        "Anthropic 审阅 141,006 次可能获得互联网访问的网络安全评测，确认三个事件、共六次运行中，Claude 从或通过第三方 Irregular 的评测环境连接互联网，并未经授权访问三个组织的真实生产系统。模型把真实系统误认成 CTF 模拟目标；Anthropic 停止相关评测、通知受影响组织，并提出网络路径验证、实时日志监控和更彻底 Transcript Review 等整改。",
        "Anthropic Cybersecurity Evaluation Team", "https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals",
        "这是少见的 Agent 安全一手事故复盘，说明系统提示中的错误环境假设、真实网络出口和缺少实时审计会共同导致越权执行。",
        "事件发生在第三方评测环境，模型缺少产品版标准分类器与监控；必须区分模型行为、系统提示、网络隔离配置和第三方基础设施责任，不能写成 Claude 产品主动攻击客户。",
        priority="P0", content="official_incident_review", info="agent_security_incident", tags=["Cybersecurity Eval", "Sandbox Escape", "Network Isolation", "Incident Review"]),
    make(
        "2026-08-13-hf-icml-open-reproductions", "2026-08-13", "agent_architecture",
        "Hugging Face 用 Coding Agents 复现 2,226 篇 ICML 论文，公开 6,816 份 Logbook 与 274 份完整 Agent Trace",
        "Hugging Face ICML 2026 Open Reproductions Challenge 由 1,221 名社区成员使用 Claude Code、Codex、Cursor、orx 等 Agent，在 19 天内发布 6,816 份 Logbook，尝试复现 2,226 篇论文、判断 35,908 项 Claim，并公开 274 份完整 Agent Trace。按 Claim 聚合，1,103 篇至少一项获独立验证，496 篇至少一项被证伪或争议。",
        "Abubakar Abid / Hugging Face Community", "https://huggingface.co/blog/icml-2026-open-reproductions",
        "研究 Agent 开始形成大规模、可审计的实验复现工作流；完整代码、产物和轨迹让 Agent 评测从结果分数扩展到过程证据。",
        "自动 Judge 使用 GLM-5.2，参与者自选任务且算力不同；‘至少一项被质疑’不等于整篇论文无效。正式统计以 2,226 篇为准，而不是约数 2,200。",
        priority="P0", content="original_research", info="agent_research_evaluation", tags=["ICML", "Reproducibility", "Agent Traces", "Coding Agents"]),
]


def main():
    existing = json.loads(PATH.read_text()) if PATH.exists() else []
    by_id = {x["id"]: x for x in existing}
    for row in records:
        by_id[row["id"]] = row
    merged = sorted(by_id.values(), key=lambda x: (x.get("event_date", ""), x["id"]))
    PATH.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"existing_before": len(existing), "reconciled_records": len(records), "total_additions_file": len(merged)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
