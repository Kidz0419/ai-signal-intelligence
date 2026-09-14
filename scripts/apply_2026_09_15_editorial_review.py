#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-15"
RUN_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
DAY = ROOT / "daily" / DATE

NINTH = "https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/"
CUSTOM = "https://aws.amazon.com/blogs/machine-learning/the-generative-ai-customization-spectrum-from-prompt-engineering-to-custom-models-on-aws/"
REPLENISH = "https://aws.amazon.com/blogs/machine-learning/automate-replenishment-with-mmf-databricks-genie-and-amazon-quick/"
REPO = "https://github.com/aws-samples/sample-isv-databricks/tree/main/autonomous-retail-replenishment-genie-quick-mmf"
RDS = "https://aws.amazon.com/blogs/publicsector/from-amazon-rds-custom-for-oracle-to-whats-next-a-technical-guide-to-oracle-migration-paths-on-aws/"
GOOGLE = "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/lea-county-new-mexico/"
OPENAI = "https://openai.com/index/apple-is-getting-this-wrong/"
SIMON = "https://simonwillison.net/2026/Sep/14/laurie-voss/"
LAURIE = "https://seldo.com/posts/we-are-all-product-engineers-now/"
SELDOCOM = "https://seldo.com/"

SIGNALS = [
    {
        "id": "2026-09-14-ninth-wave-compass-tenant-grounded-multi-agent",
        "demo": False,
        "topic_lane": "agent_architecture",
        "title": "Ninth Wave 把开放金融接入拆成七个 Agent，评分留在确定性代码里",
        "summary": "Ninth Wave 的技术复盘公开了 Compass 的生产架构：一个意图路由器连接搜索、文档问答、文档分类、字段映射、差异分析、交互工作流和就绪度分析七个专用 Agent；每次调用前由应用层装配单一银行的上下文，只有就绪度分析使用 Bedrock Knowledge Bases。最值得注意的边界是 FDX 就绪分数不交给模型，而由应用代码按必填字段映射覆盖率计算。系统还按 Agent 记录调用量、token、延迟和成本，并用健康检查触发部署回滚。",
        "decision": "include",
        "confidence": 91,
        "relevance_level": "P1",
        "signal_type": "research",
        "content_type": "technical_update",
        "information_type": "agent_governance",
        "evidence_level": "confirmed",
        "source": "Ninth Wave / AWS",
        "url": NINTH,
        "published_at": "2026-09-14T15:58:57Z",
        "primary_tags": ["Multi-agent", "Tenant-scoped grounding", "Deterministic scoring"],
        "secondary_tags": ["Open finance", "AgentCore", "Audit logging", "Deployment rollback"],
        "why_it_matters_cn": "这份复盘没有把多 Agent 当成角色数量展示，而是把上下文隔离、模型路由、确定性评分、运行指标和部署回滚分开处理。对受监管业务来说，哪些判断能由模型生成、哪些结果必须由可复算代码给出，是比 Agent 数量更重要的架构决定。",
        "personal_relevance_cn": "评估企业 Agent 时，可按这条链路核对：租户身份何时绑定、检索范围在哪里收口、每个任务用什么模型、评分能否复算、工具和模型调用是否逐 Agent 计量、失败部署能否自动退回。厂商自报的 95% 时间缩短只能当案例方结果，不能当独立评测。",
        "product_opportunity_cn": "把面向外部伙伴的 Agent 工作台做成显式对象模型：租户、任务类型、上下文包、模型配置、确定性规则、运行指标和发布版本分别留痕；评分卡同时展示模型生成的叙述与代码计算的原始字段覆盖。",
        "competitive_risk_cn": "文章由方案提供方与 AWS 联合撰写，95% 时间缩短没有样本量、基线分布或独立复现。公开材料说明了基础设施回滚，却没有展示 Agent 输出错误后的业务撤销、人工审批队列或真实产品日志界面。",
        "recommended_action": "investigate",
        "questions_to_validate": [
            "七类 Agent 的路由错误、字段映射错误和就绪度叙述偏差分别如何评测，阈值由谁批准？",
            "租户上下文包、检索命中、模型输入输出和确定性评分字段能否形成同一条可导出的审计记录？",
            "交互工作流调用了哪些写动作，外部伙伴、银行工程师和 Ninth Wave 团队各自有什么审批与撤销权限？",
            "滚动部署回滚只覆盖健康检查失败，提示词或检索质量回退由什么指标触发？"
        ],
        "follow_up_triggers": [
            "Ninth Wave 公开真实产品界面、权限矩阵或完整运行日志",
            "Compass 发布独立评测、样本量和错误率，而不只是时间缩短",
            "出现业务动作审批、暂停、撤销或模型输出回滚的产品文档"
        ],
        "scores": {
            "topic_relevance": 5,
            "novelty": 4,
            "technical_or_product_significance": 5,
            "strategic_value": 4,
            "source_quality": 4,
            "model_value": 2,
            "agent_architecture_value": 5,
            "ai_product_value": 5,
            "macro_value": 2,
            "actionability": 5
        },
        "report_date": DATE,
        "event_date": "2026-09-14",
        "canonical_url": NINTH.rstrip("/"),
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": "AWS 正文和页面 metadata 确认文章发布于 2026-09-14T15:58:57Z。正文由 Ninth Wave AI Lead 与 AWS 架构师联合署名，支持架构、GA 日期、监控和部署回滚描述；95% 时间缩短为案例方自报，缺少独立复现。文章没有提供真实 UI、业务动作审批、错误输出撤销或完整审计导出证据。",
        "related_sources": []
    },
    {
        "id": "2026-09-14-aws-quick-autonomous-replenishment-loop",
        "demo": False,
        "topic_lane": "agent_architecture",
        "title": "AWS 与 Databricks 给出可复现的补货闭环：常规订单自动提交，例外才转人工",
        "summary": "AWS 与 Databricks 发布了一套带代码仓库的补货参考实现。Chronos-2 生成预测，Databricks Genie 用固定规则找出需求激增 SKU，Amazon Quick 把预测与供应商库存合并，并按可覆盖七日需求的最低价格选择供应商。常规订单可在启用 `Run with no confirmation` 后按计划自动提交；没有单一供应商能覆盖时，系统改建人工工单。官方样例还明确暴露了风险边界：演示 Order API 默认允许未认证写入，生产使用前要启用 API key 或 authorizer。",
        "decision": "include",
        "confidence": 94,
        "relevance_level": "P1",
        "signal_type": "research",
        "content_type": "technical_update",
        "information_type": "agent_runtime",
        "evidence_level": "confirmed",
        "source": "AWS / Databricks",
        "url": REPLENISH,
        "published_at": "2026-09-14T15:42:06Z",
        "primary_tags": ["Autonomous workflow", "Human exception", "Amazon Quick"],
        "secondary_tags": ["Databricks Genie", "MCP", "OpenAPI connector", "Chronos-2"],
        "why_it_matters_cn": "这套实现把预测、判断和写动作连成了真正的闭环，而且把自动执行拆成两个条件：决策规则先判定为常规，运行设置再允许无确认执行。异常不是让模型自由处理，而是转成人工工单。它比只展示聊天式 Agent 更接近可验收的业务自动化。",
        "personal_relevance_cn": "评估 Agent 自动执行时，应分别检查决策阈值、写动作凭证、运行时确认模式、例外队列、重复执行和停机开关。尤其不能把演示环境的无认证接口原样带进生产。",
        "product_opportunity_cn": "可把每次计划运行记录成不可变决策包：预测版本、规则输入、供应商快照、选择理由、写请求、响应、确认模式和例外工单放在一条时间线；同时提供幂等键、预算上限、批次暂停和批量撤销入口。",
        "competitive_risk_cn": "文章声称命令和预期输出来自工作部署，仓库也提供离线 detect→decide 测试，但没有公开真实生产运行、订单错误率或回滚演练。样例每次计划运行都会追加新订单，官方只提醒验证后关闭计划；幂等、预算和重复下单保护没有在正文中得到证明。",
        "recommended_action": "prototype",
        "questions_to_validate": [
            "计划重试或网络超时后，Order API 是否使用幂等键防止重复下单？",
            "`Run with no confirmation` 能否按动作、金额、供应商或批次设上限，而不是全局放行？",
            "人工工单处理后如何回写状态，后续计划会不会重复创建同一异常？",
            "订单已经提交后，暂停计划、撤销订单和回滚库存决策分别由哪个系统负责？"
        ],
        "follow_up_triggers": [
            "仓库增加幂等、预算、重试和重复下单测试",
            "Amazon Quick 文档开放动作级审批策略、批次暂停和审计导出",
            "出现真实企业运行指标、异常率或错误订单复盘"
        ],
        "scores": {
            "topic_relevance": 5,
            "novelty": 5,
            "technical_or_product_significance": 5,
            "strategic_value": 4,
            "source_quality": 5,
            "model_value": 3,
            "agent_architecture_value": 5,
            "ai_product_value": 5,
            "macro_value": 2,
            "actionability": 5
        },
        "report_date": DATE,
        "event_date": "2026-09-14",
        "canonical_url": REPLENISH.rstrip("/"),
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": "AWS 页面 metadata 确认文章发布于 2026-09-14T15:42:06Z。正文提供部署步骤、动作连接器、自动确认和人工例外边界；aws-samples 仓库当前 main 可见，相关目录在 2026-09-04 的提交中补充了 RequireApiKey 开关。未运行需要付费 AWS 与 Databricks 账户的整套云部署，本轮只确认公开正文、仓库和提交；生产效果、幂等与回滚没有被独立验证。",
        "related_sources": [
            {"url": REPO, "type": "official_companion_repository"},
            {"url": "https://github.com/aws-samples/sample-isv-databricks/commit/f8a48bbce857ae3c3758ecec511c2c5086882a15", "type": "api_key_control_commit"},
            {"url": "https://github.com/aws-samples/sample-isv-databricks/commit/8d42f2bab84d64bde90ba2ccb40e9c64624b5964", "type": "connector_security_documentation_commit"}
        ]
    },
    {
        "id": "2026-09-14-aws-genai-customization-escalation-spectrum",
        "demo": False,
        "topic_lane": "model",
        "title": "AWS 把模型定制做成八级升级路径，先定位失败模式再加训练成本",
        "summary": "AWS 发布了一套八级模型定制决策框架：直接使用、提示工程、RAG、提示缓存、蒸馏、微调、继续预训练和从中间检查点构建定制模型。文章要求从最低成本方案开始，只有当当前方案在准确率、延迟、领域理解或行为控制上出现明确失败模式时才升级，并把“事实缺失”“行为不匹配”“领域结构不理解”和“服务成本过高”映射到不同方案。它不是新模型发布，而是一份厂商视角的架构选择方法。",
        "decision": "include",
        "confidence": 86,
        "relevance_level": "P2",
        "signal_type": "research",
        "content_type": "analysis",
        "information_type": "research_insight",
        "evidence_level": "primary_statement",
        "source": "AWS",
        "url": CUSTOM,
        "published_at": "2026-09-14T15:47:12Z",
        "primary_tags": ["Model customization", "Escalation framework", "Failure diagnosis"],
        "secondary_tags": ["RAG", "Distillation", "Fine-tuning", "Continued pre-training"],
        "why_it_matters_cn": "很多模型项目先选技术，再补理由。这份框架把顺序倒过来：先说明当前方案具体失败在哪里，再决定是补知识、改行为、降成本还是重建领域理解。即使去掉 AWS 服务映射，这个诊断顺序仍可用于模型产品评审。",
        "personal_relevance_cn": "模型方案评审可以要求团队为每次升级提交失败证据、基线指标、数据量、成本和退出条件。没有证明提示或 RAG 为什么失败，不应直接进入微调或继续预训练。",
        "product_opportunity_cn": "把八级路径做成实验台账：每一级记录任务集、质量门槛、延迟、单次成本、数据要求、失败样本和升级理由，并允许不同工作负载停在不同层级。",
        "competitive_risk_cn": "这是 AWS 技术与产品体系内的厂商框架，服务映射和效果数字带有销售立场。文章没有独立比较其他云平台，也没有证明所有任务都按单向阶梯演进；生产系统往往会组合多种方法。",
        "recommended_action": "adopt_framework",
        "questions_to_validate": [
            "团队是否能用同一组任务和指标证明当前层级失败，而不是凭偏好升级？",
            "事实缺失、检索失败、行为偏差和领域理解不足在评测上如何区分？",
            "蒸馏、微调和继续预训练的质量收益是否覆盖数据治理、训练和维护成本？"
        ],
        "follow_up_triggers": [
            "AWS 发布可复用评测模板或跨方法成本对照",
            "出现独立团队按该框架复现实验并公开失败样本",
            "模型定制服务的支持模型、价格或数据要求发生变化"
        ],
        "scores": {
            "topic_relevance": 4,
            "novelty": 3,
            "technical_or_product_significance": 4,
            "strategic_value": 3,
            "source_quality": 4,
            "model_value": 4,
            "agent_architecture_value": 3,
            "ai_product_value": 4,
            "macro_value": 1,
            "actionability": 5
        },
        "report_date": DATE,
        "event_date": "2026-09-14",
        "canonical_url": CUSTOM.rstrip("/"),
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": "AWS 页面 metadata 确认文章发布于 2026-09-14T15:47:12Z。八级路径和升级条件来自 AWS 作者的一手技术分析，不是独立行业标准或新产品发布。文章中的服务能力和效果数字需按厂商自报处理；本轮没有独立复现实验。",
        "related_sources": []
    },
    {
        "id": "2026-09-14-laurie-voss-product-engineering-bottleneck",
        "demo": False,
        "topic_lane": "ai_macro",
        "title": "Laurie Voss：代码成本下降后，软件稀缺项会转向需求定义、品味和现场上下文",
        "summary": "npm 联合创始人、开发者 Laurie Voss 在一篇 19 分钟长文中提出十年判断：代码生成的成本已经下降，评审、修复、部署和运维也可能继续被 Agent 吞掉；如果软件需求没有上限，岗位不会简单消失，而会向理解用户、把问题定义清楚、进入客户环境交付和打磨体验的 Product Engineer 收缩。他同时指出这套判断依赖两项强假设，并承认 Agent 当前仍不擅长评审、运维和让产品好用。",
        "decision": "watchlist",
        "confidence": 82,
        "relevance_level": "P2",
        "signal_type": "strategic_radar",
        "content_type": "practitioner_statement",
        "information_type": "industry_structure",
        "evidence_level": "primary_statement",
        "source": "Laurie Voss",
        "url": LAURIE,
        "published_at": "2026-09-14",
        "primary_tags": ["Product engineering", "Software labor", "Agentic coding"],
        "secondary_tags": ["Requirements", "Design taste", "Junior training pipeline"],
        "why_it_matters_cn": "这篇文章真正有用的地方不是“程序员会不会消失”，而是把自动化后的剩余成本拆了出来：需求定义和产品判断按每个场景重新发生，难以像代码组件那样复制。如果这个判断成立，AI 产品的竞争会更多落在现场理解、责任边界和交付闭环。",
        "personal_relevance_cn": "做 AI 产品和 Agent 规划时，可以把需求澄清、好坏标准、真实用户反馈和上线后的责任人当作独立能力建设，不能假设代码生成更便宜就会自动带来正确产品。",
        "product_opportunity_cn": "围绕 Product Engineer 工作流设计一套从现场访谈到可执行规格、验收标准、运行反馈和迭代记录的工具，而不是只继续压缩写代码的时间。",
        "competitive_risk_cn": "这是作者的十年预测，不是已验证的劳动力结论。文章对 Agent 将继续接管评审和运维、软件需求近乎无限都作了明确假设；岗位名称、薪酬和招聘趋势需要回到其引用数据逐项核验。",
        "recommended_action": "track",
        "questions_to_validate": [
            "Agent 接管评审、运维和扩容的速度是否真的接近代码生成，哪些生产指标能证明？",
            "Product Engineer、Forward Deployed Engineer 等岗位的增长是周期性招聘变化还是长期结构转移？",
            "取消初级编码工作后，企业用什么机制训练需求判断、系统责任和产品品味？"
        ],
        "follow_up_triggers": [
            "主要招聘数据连续多个季度显示产品工程与现场部署岗位占比上升",
            "企业公开新的初级工程师培养路径或 Product Engineer 能力模型",
            "Agent 在代码评审、生产运维和扩容上出现可复现的长期运行数据"
        ],
        "scores": {
            "topic_relevance": 4,
            "novelty": 4,
            "technical_or_product_significance": 3,
            "strategic_value": 4,
            "source_quality": 4,
            "model_value": 1,
            "agent_architecture_value": 3,
            "ai_product_value": 4,
            "macro_value": 4,
            "actionability": 4
        },
        "report_date": DATE,
        "event_date": "2026-09-14",
        "canonical_url": LAURIE.rstrip("/"),
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "speaker_name": "Laurie Voss",
        "speaker_role": "开发者、npm Inc 联合创始人、Developer Relations 从业者",
        "speaker_type": "ai_developer",
        "statement_topic": "Agent 自动化软件生命周期后，软件岗位和稀缺能力向产品工程迁移",
        "original_source_url": LAURIE,
        "new_information": "提出一套明确的剩余成本框架：代码、评审和运维成本继续下降后，需求发现、精确定义和体验判断成为按产品重复发生、难以规模化复制的主要成本；并把初级工程师训练链断裂列为转型风险。",
        "evidence_artifact": "作者个人网站上的 19 分钟完整长文，列出两项前提假设、当前 Agent 能力缺口、岗位变化推演和可继续核验的数据来源。",
        "evidence_boundary": "原文页面确认发布日期为 2026-09-14；Simon Willison 同日只摘录了结论段，本记录回到 Laurie Voss 原文判断。作者身份由其个人网站首页说明。文章是带引用的预测和个人分析，不等于岗位结构已经完成迁移；本轮没有逐项复核其外链招聘与劳动力数据。",
        "related_sources": [
            {"url": SIMON, "type": "secondary_quote_discovery"},
            {"url": SELDOCOM, "type": "author_identity"}
        ]
    }
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
            "id": "2026-09-15-regulated-agent-deterministic-control-plane",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "agent_architecture",
            "source_signal_ids": [SIGNALS[0]["id"]],
            "working_title_cn": "受监管 Agent 最该先拆开的，不是角色，而是判断责任",
            "core_tension_cn": "模型可以生成映射解释和就绪度叙述，但最终评分、租户隔离和发布回滚必须有可复算、可追责的控制链。",
            "why_now_cn": "Ninth Wave 刚公开 Compass 的七 Agent 生产架构，并明确把 FDX 就绪分数留在应用代码中，提供了一个比“多 Agent 协作”更具体的治理样本。",
            "target_audience_cn": ["企业 AI 产品经理", "Agent 平台架构师", "金融科技安全与合规团队"],
            "evidence_boundary_cn": "架构和上线日期来自 Ninth Wave 与 AWS 联合技术复盘；95% 时间缩短是案例方自报。真实 UI、业务动作审批、错误输出撤销和独立评测仍缺失。",
            "source_urls": [SIGNALS[0]["canonical_url"]],
            "platforms": {
                "xiaohongshu": {
                    "title": "金融 Agent 不该什么都交给模型：这 5 层必须留在控制面",
                    "hook": "七个 Agent 不是重点。真正决定系统能不能进生产的，是租户隔离、确定性评分、逐 Agent 计量、发布回滚和审计记录。",
                    "format": "8页图文卡",
                    "outline": ["Compass 处理的开放金融接入问题", "七个专用 Agent 如何分工", "租户上下文在哪一层收口", "为什么就绪分数由代码计算", "逐 Agent 指标如何定位回退", "基础设施回滚与业务撤销的差别", "仍缺失的审批与日志证据", "受监管 Agent 验收清单"],
                    "visual_direction": "一张责任分层图，把模型生成、确定性计算、租户隔离、监控和回滚放在不同层",
                    "cta": "你的 Agent 里，哪些结论绝不能由模型直接给最终分？"
                },
                "twitter": {
                    "title": "The useful part of a seven-agent system is not the number seven",
                    "hook": "Ninth Wave's Compass keeps tenant grounding outside the model and computes readiness scores in deterministic application code. That separation matters more than the multi-agent diagram.",
                    "format": "7帖 Thread",
                    "outline": ["workflow and actors", "intent routing", "tenant-scoped context assembly", "deterministic readiness score", "per-agent observability", "deployment rollback versus business rollback", "open evidence gaps"],
                    "visual_direction": "control boundary diagram separating probabilistic outputs from deterministic decisions",
                    "cta": "Which outputs in your agent system must remain reproducible code?"
                },
                "wechat": {
                    "title": "七个 Agent 之外：受监管业务真正需要的确定性控制层",
                    "hook": "Ninth Wave 的开放金融案例有一个值得单独拆解的决定：Agent 负责分析和叙述，但最终就绪度评分仍由应用代码计算。",
                    "format": "2600—3200字架构分析",
                    "outline": ["开放金融接入的对象与参与者", "七类 Agent 的任务边界", "租户隔离与上下文装配", "生成式叙述和确定性评分的分工", "逐 Agent 指标与质量回退", "部署回滚为什么不等于业务撤销", "证据缺口与待验证问题", "金融 Agent 产品验收表"],
                    "visual_direction": "端到端数据流加责任矩阵，标出模型、应用代码、身份系统和运维系统",
                    "cta": "附一份可复用的受监管 Agent 控制面验收表。"
                }
            }
        },
        {
            "id": "2026-09-15-agent-auto-execution-two-gates",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "agent_architecture",
            "source_signal_ids": [SIGNALS[1]["id"]],
            "working_title_cn": "Agent 自动下单至少有两道门：决策可自动，运行才可免确认",
            "core_tension_cn": "常规与异常由业务规则判断，是否无确认执行由运行设置决定；把两者合成一个自动模式会掩盖权限、重试和重复下单风险。",
            "why_now_cn": "AWS 与 Databricks 的补货样例把预测、供应商选择、下单和人工工单连成了可复现闭环，也公开了默认无认证演示接口和计划重复运行的风险。",
            "target_audience_cn": ["Agent 产品经理", "企业自动化与供应链团队", "AI 安全与平台工程团队"],
            "evidence_boundary_cn": "正文与公开仓库能确认实现和配置边界，但本轮没有运行付费云部署。真实生产错误率、幂等、预算限制和订单撤销没有公开证据。",
            "source_urls": [SIGNALS[1]["canonical_url"]],
            "platforms": {
                "xiaohongshu": {
                    "title": "AI 自动下单前，产品至少要做这 2 道门",
                    "hook": "系统先判断这是不是常规订单，再判断这次运行能不能免确认。少任何一道，自动化都会变得危险。",
                    "format": "8页图文卡",
                    "outline": ["预测到订单的完整闭环", "第一道门：业务规则", "第二道门：运行确认模式", "异常为什么转人工工单", "默认无认证 API 的演示边界", "计划重试与重复下单", "暂停、撤销和预算控制", "自动执行验收清单"],
                    "visual_direction": "双闸门流程图，旁路标出人工工单、幂等键和暂停按钮",
                    "cta": "你的自动模式能分别配置决策门和执行门吗？"
                },
                "twitter": {
                    "title": "Autonomous ordering needs two gates, not one toggle",
                    "hook": "The AWS/Databricks replenishment sample separates policy classification from run-time confirmation. Routine decisions can qualify for automation, but writes happen unattended only when the schedule explicitly allows it.",
                    "format": "7帖 Thread",
                    "outline": ["forecast-to-action loop", "deterministic surge query", "supplier decision rule", "run without confirmation", "human exception path", "authentication and idempotency gaps", "minimum production controls"],
                    "visual_direction": "two-gate state machine with routine and exception branches",
                    "cta": "Does your agent distinguish eligible-for-automation from authorized-to-execute?"
                },
                "wechat": {
                    "title": "从补货样例看 Agent 自动执行：决策门和权限门必须分开",
                    "hook": "一套能自动下单的 Agent 参考实现，最值得看的不是模型，而是它怎样区分常规订单、人工例外和无确认运行。",
                    "format": "2600—3200字产品拆解",
                    "outline": ["预测、检测、决策、执行四段链路", "固定查询如何减少漂移", "常规与异常的业务规则", "无确认运行的权限语义", "写接口认证和凭证风险", "幂等、预算、重试与重复执行", "暂停和撤销该由谁负责", "生产化验收问题"],
                    "visual_direction": "动作控制矩阵，列出规则、凭证、确认、幂等、预算、暂停和撤销",
                    "cta": "附一份 Agent 写动作上线前检查表。"
                }
            }
        },
        {
            "id": "2026-09-15-model-customization-needs-failure-evidence",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "B",
            "topic_lane": "model",
            "source_signal_ids": [SIGNALS[2]["id"]],
            "working_title_cn": "模型定制不该从微调开始，而该从失败证据开始",
            "core_tension_cn": "事实缺失、行为偏差、领域结构不理解和成本过高不是同一个问题，却常被团队用同一种微调方案处理。",
            "why_now_cn": "AWS 新发布的八级路径把每种失败模式映射到提示、RAG、缓存、蒸馏、微调或继续预训练，可改写成一套不依赖云厂商的评审方法。",
            "target_audience_cn": ["AI 产品经理", "模型应用团队", "企业 AI 架构与采购团队"],
            "evidence_boundary_cn": "这是 AWS 作者的一手方法，不是独立标准；服务能力和效果数字带厂商立场。可复用的是失败诊断顺序，不是照搬服务清单。",
            "source_urls": [SIGNALS[2]["canonical_url"]],
            "platforms": {
                "xiaohongshu": {
                    "title": "别一上来就微调：先回答模型到底失败在哪",
                    "hook": "答不出事实、格式不对、看不懂行业术语、成本太高，四种问题对应四条路。混在一起，训练费很容易白花。",
                    "format": "7页图文卡",
                    "outline": ["八级路径全图", "事实缺失先看 RAG", "行为偏差再看微调", "成本过高考虑缓存或蒸馏", "领域结构不理解才看继续预训练", "每次升级需要什么证据", "模型定制评审模板"],
                    "visual_direction": "失败症状到技术方案的诊断树，不使用厂商服务 Logo 作为主结构",
                    "cta": "你最近一次微调，是为了解决哪一种失败？"
                },
                "twitter": {
                    "title": "Model customization should start with failure evidence",
                    "hook": "Missing facts, bad behavior, weak domain comprehension, and high serving cost are different failures. They should not all end in fine-tuning.",
                    "format": "6帖 Thread",
                    "outline": ["four failure classes", "prompting and RAG", "caching and distillation", "fine-tuning", "continued pretraining", "evidence required before escalation"],
                    "visual_direction": "failure-mode decision tree with quality, latency, cost and data gates",
                    "cta": "What evidence does your team require before moving up the customization stack?"
                },
                "wechat": {
                    "title": "模型定制的正确起点：不是选技术，而是证明当前方案怎么失败",
                    "hook": "很多团队把微调当成模型不够好的通用解法。更稳的做法是先区分知识、行为、理解和成本问题，再决定是否增加训练投入。",
                    "format": "2200—2800字方法文",
                    "outline": ["八级路径及其适用边界", "四类常见失败", "为什么事实缺失不等于需要训练", "微调能改什么、不能改什么", "继续预训练的高成本门槛", "混合架构而非单向阶梯", "实验台账和退出条件", "评审模板"],
                    "visual_direction": "实验台账示例，包含任务集、质量、延迟、成本、数据和升级理由",
                    "cta": "附一个可直接用于模型方案会的失败证据表。"
                }
            }
        },
        {
            "id": "2026-09-15-product-engineering-after-code-cost-collapse",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "B",
            "topic_lane": "ai_macro",
            "source_signal_ids": [SIGNALS[3]["id"]],
            "working_title_cn": "代码越来越便宜，产品判断为什么反而更贵",
            "core_tension_cn": "Agent 可以复制代码生产能力，但每个场景的需求定义、现场上下文和产品品味仍要重新获得，无法靠一份通用模型直接摊薄。",
            "why_now_cn": "Laurie Voss 的新长文把岗位争论转成成本结构问题，并把初级工程师训练链断裂列为长期风险，适合与单纯的失业预测分开讨论。",
            "target_audience_cn": ["AI 产品经理", "工程与产品负责人", "开发者工具和组织设计团队"],
            "evidence_boundary_cn": "这是作者基于两项强假设作出的十年预测。岗位、薪酬和招聘数字尚未在本轮逐项复核，不能写成已经发生的行业定论。",
            "source_urls": [SIGNALS[3]["canonical_url"]],
            "platforms": {
                "xiaohongshu": {
                    "title": "AI 把代码变便宜后，最贵的可能变成这 3 件事",
                    "hook": "会写代码不再稀缺，不代表软件会自动变好。理解人要什么、把问题说清楚、做出让人愿意用的东西，可能才是剩下的大头。",
                    "format": "8页图文卡",
                    "outline": ["作者的两项强假设", "代码之后还有哪些工作", "需求定义为何难复制", "产品品味为何不能批量生产", "Product Engineer 是什么", "初级工程师训练链为什么断", "哪些数据还要验证", "个人能力建设清单"],
                    "visual_direction": "软件成本结构前后对比图，把确定事实与作者预测用不同颜色分开",
                    "cta": "如果不再靠写小需求成长，下一代资深工程师怎么练出来？"
                },
                "twitter": {
                    "title": "Cheap code does not make product judgment cheap",
                    "hook": "Laurie Voss argues that as agents absorb more of the software lifecycle, the remaining cost shifts to requirements, context, and taste. His forecast is useful because he states the assumptions and the broken training loop.",
                    "format": "7帖 Thread",
                    "outline": ["two explicit assumptions", "what agents do poorly today", "non-transferable product decisions", "rise of product engineering", "broken junior training loop", "evidence still needed", "implications for AI tools"],
                    "visual_direction": "cost stack moving from code production to requirements and product judgment",
                    "cta": "How should teams train judgment when junior coding work disappears?"
                },
                "wechat": {
                    "title": "代码成本下降之后，软件行业真正稀缺的东西会变成什么",
                    "hook": "一篇关于 Product Engineer 的长文提供了一个比“AI 会不会替代程序员”更能落地的问法：软件生命周期被自动化后，哪部分成本无法复制？",
                    "format": "2600—3400字趋势分析",
                    "outline": ["先列清楚两项预测前提", "代码、评审和运维的自动化顺序", "需求定义的非规模化成本", "产品判断和设计的剩余价值", "Product Engineer 与现场部署岗位", "初级人才培养链断裂", "哪些数据支持、哪些仍待核验", "对 AI 产品团队的组织建议"],
                    "visual_direction": "事实、作者判断、待验证指标三栏证据表",
                    "cta": "把岗位预测改写成一份团队能力建设清单。"
                }
            }
        }
    ]
}

SOURCES = [
    (NINTH, "How Ninth Wave built AI-powered open finance onboarding on Amazon Bedrock", "Ninth Wave / AWS", "confirmed"),
    (CUSTOM, "The generative AI customization spectrum", "AWS", "primary_statement"),
    (REPLENISH, "Automate replenishment with MMF, Databricks Genie, and Amazon Quick", "AWS / Databricks", "confirmed"),
    (REPO, "Autonomous retail replenishment companion repository", "AWS Samples / GitHub", "confirmed"),
    (RDS, "RDS Custom for Oracle migration guide", "AWS", "confirmed"),
    (GOOGLE, "Potential Lea County data center", "Google", "primary_statement"),
    (OPENAI, "Apple is getting this wrong", "OpenAI", "primary_statement"),
    (SIMON, "A quote from Laurie Voss", "Simon Willison", "primary_statement"),
    (LAURIE, "We are all Product Engineers now", "Laurie Voss", "primary_statement"),
    (SELDOCOM, "Laurie Voss author profile", "Laurie Voss", "confirmed")
]

REVIEWS = [
    {"url": NINTH, "decision": "include", "signal_id": SIGNALS[0]["id"], "published_at": "2026-09-14T15:58:57Z", "reason": "body and metadata document a production multi-agent architecture with tenant-scoped grounding, deterministic readiness scoring, per-agent observability and deployment rollback; launch timing and performance remain vendor-reported"},
    {"url": CUSTOM, "decision": "include", "signal_id": SIGNALS[2]["id"], "published_at": "2026-09-14T15:47:12Z", "reason": "the body provides a durable eight-step customization and escalation framework tied to explicit failure modes; selected as P2 research, not a product launch"},
    {"url": REPLENISH, "decision": "include", "signal_id": SIGNALS[1]["id"], "published_at": "2026-09-14T15:42:06Z", "reason": "body and companion repository expose a reproducible detect-decide-act workflow, unattended-write configuration, human exception routing and authentication boundaries"},
    {"url": RDS, "decision": "checked_no_match", "published_at": "2026-09-14T16:01:44Z", "reason": "the body is an Oracle database migration guide; Oracle 26ai is a database version name and the article contains no material model, agent, AI product or AI industry-structure event"},
    {"url": GOOGLE, "decision": "checked_no_match", "published_at": "2026-09-14T14:00:00Z", "reason": "the page confirms only that Google is exploring a possible Lea County data center; it gives no size, capital commitment, capacity, AI workload, energy agreement or executed project state"},
    {"url": OPENAI, "decision": "outside_incremental_window_no_material_update", "published_at": "2026-08-03", "reason": "the first-party page is dated August 3 with visible updates through September 1; the September 14 sitemap lastmod does not identify a new filing, product event or body update"},
    {"url": SIMON, "decision": "include_primary_source_replacement", "signal_id": SIGNALS[3]["id"], "published_at": "2026-09-14T14:34:29Z", "reason": "Simon Willison's post is only a quotation; editorial selection was moved to Laurie Voss's complete first-party article, which states its assumptions, thesis, current agent limits and long-term training risk"}
]


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def build_ledger() -> list[dict]:
    return [
        {"id": i, "title": title, "url": url, "publisher": publisher, "evidence_level": level, "accessed": RUN_AT}
        for i, (url, title, publisher, level) in enumerate(SOURCES, 1)
    ]


def build_brief(sources: list[dict]) -> str:
    ids = {source["url"].rstrip("/"): source["id"] for source in sources}
    c = lambda url: f"[{ids[url.rstrip('/')] }]"
    source_block = "\n".join(f'[{source["id"]}] {source["url"]}' for source in sources)
    return f'''# AI Signal 日报｜{DATE}

**窗口：** 00:00 增量只核验本轮 7 个 `new_candidates`，没有重扫 171 条滚动候选，也没有重审完整队列。四条正式记录都在北京时间 9 月 14 日晚间发布，本日报按 catch-up 收录并保留 `event_date=2026-09-14`。
**一句话结论：** 新增 4 条 Signal。两条 P1 把 Agent 的生产控制边界说得很具体：开放金融案例把租户隔离与确定性评分留在应用层，补货样例则把业务规则、无确认运行和人工例外拆成不同控制。{c(NINTH)}{c(REPLENISH)}{c(REPO)}

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 1 | 用失败证据决定提示、RAG、蒸馏、微调或继续预训练 |
| Agent 架构 | 2 | 确定性评分与自动写动作都不能被一个“Agent 自动模式”吞掉 |
| AI 产品 | 0 | 两个生产案例归入架构主线，没有把厂商自报效果另建产品卡 |
| AI 宏观 | 1 | Product Engineering 岗位迁移进入 Strategic Radar，仍是带强假设的预测 |

## 模型｜1 条

### 模型定制先诊断失败，再增加训练成本

AWS 把模型定制分成八级：直接使用、提示工程、RAG、提示缓存、蒸馏、微调、继续预训练和定制模型构建。文章要求团队先证明当前方案在哪项指标上失败，再升级；事实缺失、行为不匹配、领域结构不理解和服务成本过高分别对应不同路径。{c(CUSTOM)}

这不是模型发布，也不是行业标准。可复用的是评审顺序：每次升级要带任务集、质量门槛、延迟、成本、数据要求和退出条件。AWS 的服务映射和效果数字仍按厂商观点处理。{c(CUSTOM)}

## Agent 架构｜2 条

### 1. Ninth Wave Compass：七个 Agent，但最终分数不交给模型

Compass 由一个路由器连接七类专用 Agent。应用层在调用前装配单一银行的 API 文档、配置和历史上下文；只有就绪度分析使用 Bedrock Knowledge Bases。FDX 就绪分数由应用代码按必填字段映射覆盖率计算，不由模型估计。系统还按 Agent 记录调用量、token、延迟和成本，部署健康检查失败时触发回滚。{c(NINTH)}

文章由 Ninth Wave AI Lead 与 AWS 架构师联合署名。它称产品在 2026 年 6 月 1 日 GA，并自报 API 映射与分析时间缩短 95%；没有公开样本量、错误率或独立复现。正文能确认基础设施部署回滚，但没有展示错误输出后的业务撤销、人工审批队列或完整审计 UI。{c(NINTH)}

**判断：** 受监管 Agent 的核心不是角色数量，而是哪些内容由模型生成，哪些结论必须由可复算代码给出，以及租户、模型版本、检索、指标和发布版本能否串成同一条记录。

### 2. 补货闭环：常规订单自动提交，例外转人工

AWS 与 Databricks 的参考实现把预测、检测、决策和执行连起来：Chronos-2 预测需求，固定的 Genie 查询找出激增 SKU，Amazon Quick 根据供应商覆盖能力与价格选出供应商，再调用 Order API。规则无法找到单一供应商覆盖需求时，系统创建人工工单。{c(REPLENISH)}{c(REPO)}

自动执行还有第二道门。计划只有在启用 `Run with no confirmation` 后才会无人工确认提交写动作；交互运行仍展示确认表单。样例 Order API 默认接受未认证写入，官方要求非监督演示启用 API key 或 authorizer。公开仓库在 9 月 4 日补上了 `RequireApiKey` 开关和对应说明。{c(REPLENISH)}{c(REPO)}

**判断：** “规则判断可自动”和“当前运行被授权自动写入”是两个状态。生产版还要补幂等键、金额或批次上限、重试去重、计划暂停和订单撤销，正文与仓库目前没有证明这些能力。

## AI 产品｜0 条

Ninth Wave 与补货样例都涉及真实业务工作流，但本轮把它们按架构事件记录，避免把同一份证据拆成重复产品卡。厂商自报效果没有独立评测，不另建产品采用信号。{c(NINTH)}{c(REPLENISH)}

## AI 宏观｜1 条

### Laurie Voss：代码更便宜后，产品判断可能成为主要成本

Laurie Voss 在 9 月 14 日的长文中提出两项前提：Agent 会继续接管评审、修复、部署和运维；软件需求没有上限。在这两个前提下，岗位不会简单消失，而会向需求发现、精确定义、现场交付和产品体验收缩，也就是他所说的 Product Engineering。{c(LAURIE)}

这条只进入 P2 Strategic Radar。作者明确承认 Agent 当前仍不擅长评审、运维和让产品好用；岗位、薪酬和招聘趋势需要回到外链数据逐项核验。更值得跟踪的问题是，初级编码工作减少后，组织如何训练下一代工程师的上下文、责任判断和产品品味。{c(LAURIE)}{c(SELDOCOM)}

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有模型负责人关于训练、能力、评测或模型路线的新原创内容。

## AI 一线实践者观点｜1 条

Simon Willison 的候选只是摘录 Laurie Voss 的结论段，本轮回到 19 分钟原文建立主记录。Laurie Voss 的个人网站把他介绍为开发者、npm Inc 联合创始人和 Developer Relations 从业者；正式卡只归纳原文明确提出的假设和岗位框架，没有把十年预测改写成既成事实。{c(SIMON)}{c(LAURIE)}{c(SELDOCOM)}

## 本轮审核但未入选

- RDS Custom for Oracle 迁移指南：`checked_no_match`。正文是数据库迁移与支持终止指南，Oracle 26ai 的名称不能把它变成 AI Signal。{c(RDS)}
- Google Lea County：`checked_no_match`。正文只说仍在探索潜在数据中心，没有规模、资本承诺、容量、AI 工作负载、能源协议或已执行项目。{c(GOOGLE)}
- OpenAI 与 Apple 诉讼页面：`outside_incremental_window_no_material_update`。正文日期是 8 月 3 日，可见更新截至 9 月 1 日；9 月 14 日 Sitemap `lastmod` 不能证明出现了新事件。{c(OPENAI)}

## 覆盖与缺口

- 7 个真新增候选都完成了正文和日期核验；Sitemap `lastmod` 没有被当作发布日期。
- AWS 三篇文章的 HTML metadata 与 RSS 时间一致。RDS 条目因领域不符排除；Google 因仍是缺少规模和执行承诺的探索排除。
- OpenAI 普通采集曾返回 403，本轮通过可读官方正文确认原始日期和更新边界，没有把 403 当成无内容。{c(OPENAI)}
- 补货样例核对了公开仓库和相关提交，但没有使用付费 AWS 与 Databricks 账户运行整套云部署；该限制已写入 Signal 证据边界。{c(REPO)}

## 建议行动

1. 用 Ninth Wave 案例检查现有 Agent：租户装配、模型路由、确定性评分、逐 Agent 指标和版本回滚是否分层留痕。
2. 用补货样例检查写动作：业务规则、运行授权、人工例外、认证、幂等、预算、暂停和撤销是否各有独立状态。
3. 模型定制项目增加“失败证据”评审；没有基线和退出条件，不直接升级到微调或继续预训练。
4. 持续观察 Product Engineer 与现场部署岗位，但暂不把十年预测当作劳动力事实。

## 证据边界

- 两条 P1 都来自厂商或方案参与方的一手技术材料。架构与公开代码可确认，性能和业务效果仍是自报。{c(NINTH)}{c(REPLENISH)}{c(REPO)}
- AWS 模型定制路径是分析框架，不是产品发布或独立标准。{c(CUSTOM)}
- Laurie Voss 条目是具名作者的预测；两项前提、当前能力缺口和未复核的数据边界均保留。{c(LAURIE)}

## 飞书短版

**一句话结论：** 7 个真新增候选完成正文核验，新增 4 条 Signal：P1 两条、P2 两条。

**重点 1：** Ninth Wave 的七 Agent 架构把租户上下文装配放在应用层，FDX 就绪分数由确定性代码计算，不交给模型。{c(NINTH)}

**重点 2：** AWS/Databricks 补货闭环只有在业务规则判定常规、且计划启用无确认运行后才自动写订单；例外转人工。样例默认无认证接口不能照搬生产。{c(REPLENISH)}{c(REPO)}

**判断：** Agent 自动化要把“能否判断”“是否获权执行”“失败后怎么停和撤销”分开；模型定制也要先证明失败模式，再增加训练成本。

**边界：** 两个案例的效果数字都不是独立评测；Product Engineering 岗位迁移仍是带强假设的 P2 预测。{c(NINTH)}{c(LAURIE)}

**结果：** previous_count=0，new_count=4，updated_count=0，total_count=4。

## Sources

{source_block}
'''


def main() -> None:
    collection = json.loads((DAY / "collection-run-summary.json").read_text())
    summary = deepcopy(collection)

    for probe in summary.get("representative_probes", []):
        name = probe.get("name")
        if name == "AWS ML Blog RSS":
            probe["status"] = "selected"
            probe["note"] = "Three cross-run new articles were body-reviewed: two P1 architecture cases and one P2 model-customization framework selected"
        elif name == "AWS Public Sector RSS":
            probe["status"] = "checked_no_match"
            probe["note"] = "The only cross-run new article is an Oracle database migration guide outside the four AI lanes"
        elif name == "Google Blog sitemap":
            probe["status"] = "checked_no_match"
            probe["note"] = "The Lea County article date and body were reviewed; it only describes an exploratory data-center conversation without scale or commitment"
        elif name == "OpenAI sitemap":
            probe["status"] = "candidate_only"
            probe["note"] = "The new lastmod points to an August 3 legal statement with updates only through September 1; lastmod was not used as publication evidence"
        elif name == "Simon Willison atom":
            probe["status"] = "selected"
            probe["note"] = "The quote-only candidate was replaced by Laurie Voss's complete first-party September 14 article and selected as P2 strategic radar"

    summary.update({
        "run_type": "daily_four_lane_incremental_editorial_review",
        "run_at": RUN_AT,
        "deliverable_outcome": "success",
        "scheduler_outcome": "success",
        "editorial_shortlist": 4,
        "reviewed_new_candidates": 7,
        "day_reviewed_candidates_total": 7,
        "previous_count": 0,
        "new_count": 4,
        "updated_count": 0,
        "excluded_count": 3,
        "candidate_queue_count": 7,
        "new_in_run_count": 7,
        "unreviewed_candidate_count": 0,
        "total_count": 4,
        "selected": 4,
        "lane_counts": {"model": 1, "agent_architecture": 2, "ai_product": 0, "ai_macro": 1},
        "priority_counts": {"P0": 0, "P1": 2, "P2": 2, "P3": 0},
        "executive_model_longform": 0,
        "practitioner_statements": 1,
        "cross_day_duplicates_removed": 0,
        "candidate_reviews": REVIEWS,
        "review_breakdown": {"selected": 4, "below_formal_bar": 2, "outside_incremental_window": 1, "duplicate_or_merged": 0, "unresolved": 0},
        "content_topics": {"topic_count": 4, "platform_variants": 12},
        "collection_contract": {
            "raw_candidates_in_rolling_window_is_not_increment": True,
            "candidate_queue_count_is_not_new_count": True,
            "sitemap_lastmod_is_discovery_only": True,
            "feed_titles_require_body_verification": True,
            "http_2xx_is_not_checked_no_match": True,
            "true_increment_source": "new_in_run_count and new_candidates followed by body-level editorial review"
        },
        "review_notes": [
            "Reviewed only the 7 cross-run new candidates; the 171-item rolling pool and full registry were not rescanned.",
            "All four selected records retain event_date 2026-09-14 and are published in the September 15 day bucket as catch-up findings.",
            "The Simon Willison quotation was treated as discovery and replaced by Laurie Voss's complete first-party article.",
            "The OpenAI sitemap lastmod was rejected as freshness evidence after the body resolved to an August 3 article with visible updates only through September 1.",
            "The Google data-center page was excluded because exploration without size, commitment, capacity or AI workload does not clear the macro gate.",
            "The replenishment companion repository and security-control commits were inspected, but the paid cloud deployment was not executed."
        ]
    })

    sources = build_ledger()
    dump(DAY / "selected.json", SIGNALS)
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
        "reviewed_new_candidates": 7,
        "selected": 4,
        "excluded": 3,
        "citations": len(sources),
        "topics": 4,
        "platform_variants": 12
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
