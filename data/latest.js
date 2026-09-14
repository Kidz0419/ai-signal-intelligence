window.DAILY_SIGNALS = [
  {
    "id": "2026-09-14-ninth-wave-compass-tenant-grounded-multi-agent",
    "demo": false,
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
    "url": "https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/",
    "published_at": "2026-09-14T15:58:57Z",
    "primary_tags": [
      "Multi-agent",
      "Tenant-scoped grounding",
      "Deterministic scoring"
    ],
    "secondary_tags": [
      "Open finance",
      "AgentCore",
      "Audit logging",
      "Deployment rollback"
    ],
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
    "report_date": "2026-09-15",
    "event_date": "2026-09-14",
    "canonical_url": "https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock",
    "first_seen_date": "2026-09-15",
    "last_seen_date": "2026-09-15",
    "run_dates": [
      "2026-09-15"
    ],
    "evidence_boundary": "AWS 正文和页面 metadata 确认文章发布于 2026-09-14T15:58:57Z。正文由 Ninth Wave AI Lead 与 AWS 架构师联合署名，支持架构、GA 日期、监控和部署回滚描述；95% 时间缩短为案例方自报，缺少独立复现。文章没有提供真实 UI、业务动作审批、错误输出撤销或完整审计导出证据。",
    "related_sources": []
  },
  {
    "id": "2026-09-14-aws-quick-autonomous-replenishment-loop",
    "demo": false,
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
    "url": "https://aws.amazon.com/blogs/machine-learning/automate-replenishment-with-mmf-databricks-genie-and-amazon-quick/",
    "published_at": "2026-09-14T15:42:06Z",
    "primary_tags": [
      "Autonomous workflow",
      "Human exception",
      "Amazon Quick"
    ],
    "secondary_tags": [
      "Databricks Genie",
      "MCP",
      "OpenAPI connector",
      "Chronos-2"
    ],
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
    "report_date": "2026-09-15",
    "event_date": "2026-09-14",
    "canonical_url": "https://aws.amazon.com/blogs/machine-learning/automate-replenishment-with-mmf-databricks-genie-and-amazon-quick",
    "first_seen_date": "2026-09-15",
    "last_seen_date": "2026-09-15",
    "run_dates": [
      "2026-09-15"
    ],
    "evidence_boundary": "AWS 页面 metadata 确认文章发布于 2026-09-14T15:42:06Z。正文提供部署步骤、动作连接器、自动确认和人工例外边界；aws-samples 仓库当前 main 可见，相关目录在 2026-09-04 的提交中补充了 RequireApiKey 开关。未运行需要付费 AWS 与 Databricks 账户的整套云部署，本轮只确认公开正文、仓库和提交；生产效果、幂等与回滚没有被独立验证。",
    "related_sources": [
      {
        "url": "https://github.com/aws-samples/sample-isv-databricks/tree/main/autonomous-retail-replenishment-genie-quick-mmf",
        "type": "official_companion_repository"
      },
      {
        "url": "https://github.com/aws-samples/sample-isv-databricks/commit/f8a48bbce857ae3c3758ecec511c2c5086882a15",
        "type": "api_key_control_commit"
      },
      {
        "url": "https://github.com/aws-samples/sample-isv-databricks/commit/8d42f2bab84d64bde90ba2ccb40e9c64624b5964",
        "type": "connector_security_documentation_commit"
      }
    ]
  },
  {
    "id": "2026-09-14-aws-genai-customization-escalation-spectrum",
    "demo": false,
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
    "url": "https://aws.amazon.com/blogs/machine-learning/the-generative-ai-customization-spectrum-from-prompt-engineering-to-custom-models-on-aws/",
    "published_at": "2026-09-14T15:47:12Z",
    "primary_tags": [
      "Model customization",
      "Escalation framework",
      "Failure diagnosis"
    ],
    "secondary_tags": [
      "RAG",
      "Distillation",
      "Fine-tuning",
      "Continued pre-training"
    ],
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
    "report_date": "2026-09-15",
    "event_date": "2026-09-14",
    "canonical_url": "https://aws.amazon.com/blogs/machine-learning/the-generative-ai-customization-spectrum-from-prompt-engineering-to-custom-models-on-aws",
    "first_seen_date": "2026-09-15",
    "last_seen_date": "2026-09-15",
    "run_dates": [
      "2026-09-15"
    ],
    "evidence_boundary": "AWS 页面 metadata 确认文章发布于 2026-09-14T15:47:12Z。八级路径和升级条件来自 AWS 作者的一手技术分析，不是独立行业标准或新产品发布。文章中的服务能力和效果数字需按厂商自报处理；本轮没有独立复现实验。",
    "related_sources": []
  },
  {
    "id": "2026-09-14-laurie-voss-product-engineering-bottleneck",
    "demo": false,
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
    "url": "https://seldo.com/posts/we-are-all-product-engineers-now/",
    "published_at": "2026-09-14",
    "primary_tags": [
      "Product engineering",
      "Software labor",
      "Agentic coding"
    ],
    "secondary_tags": [
      "Requirements",
      "Design taste",
      "Junior training pipeline"
    ],
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
    "report_date": "2026-09-15",
    "event_date": "2026-09-14",
    "canonical_url": "https://seldo.com/posts/we-are-all-product-engineers-now",
    "first_seen_date": "2026-09-15",
    "last_seen_date": "2026-09-15",
    "run_dates": [
      "2026-09-15"
    ],
    "speaker_name": "Laurie Voss",
    "speaker_role": "开发者、npm Inc 联合创始人、Developer Relations 从业者",
    "speaker_type": "ai_developer",
    "statement_topic": "Agent 自动化软件生命周期后，软件岗位和稀缺能力向产品工程迁移",
    "original_source_url": "https://seldo.com/posts/we-are-all-product-engineers-now/",
    "new_information": "提出一套明确的剩余成本框架：代码、评审和运维成本继续下降后，需求发现、精确定义和体验判断成为按产品重复发生、难以规模化复制的主要成本；并把初级工程师训练链断裂列为转型风险。",
    "evidence_artifact": "作者个人网站上的 19 分钟完整长文，列出两项前提假设、当前 Agent 能力缺口、岗位变化推演和可继续核验的数据来源。",
    "evidence_boundary": "原文页面确认发布日期为 2026-09-14；Simon Willison 同日只摘录了结论段，本记录回到 Laurie Voss 原文判断。作者身份由其个人网站首页说明。文章是带引用的预测和个人分析，不等于岗位结构已经完成迁移；本轮没有逐项复核其外链招聘与劳动力数据。",
    "related_sources": [
      {
        "url": "https://simonwillison.net/2026/Sep/14/laurie-voss/",
        "type": "secondary_quote_discovery"
      },
      {
        "url": "https://seldo.com/",
        "type": "author_identity"
      }
    ]
  },
  {
    "id": "2026-09-14-github-copilot-auto-model-selection-tiers",
    "demo": false,
    "topic_lane": "ai_product",
    "title": "GitHub Copilot 把自动选模拆成三档：用户选目标，系统按每个 Prompt 选模型",
    "summary": "GitHub Copilot 的自动选模新增 efficiency、balance 和 intelligence 三档。用户选择成本、质量与响应时间的偏好，路由器仍按每个 Prompt 的复杂度、系统健康和可用性选择模型；三档使用同一候选模型池。该功能正向 VS Code、Copilot CLI 和 GitHub Copilot app 推送，费用按实际选中的模型计算，付费用户通过 auto 仍享 10% 折扣。",
    "decision": "include",
    "confidence": 94,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "official_release",
    "information_type": "product_workflow",
    "evidence_level": "confirmed",
    "source": "GitHub",
    "url": "https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection",
    "published_at": "2026-09-14T16:05:27Z",
    "primary_tags": [
      "Auto model selection",
      "Cost-quality control",
      "Per-prompt routing"
    ],
    "secondary_tags": [
      "GitHub Copilot",
      "VS Code",
      "Copilot CLI",
      "Usage-based billing"
    ],
    "why_it_matters_cn": "多模型产品开始把选模从隐藏的系统决定变成用户可配置的策略，但控制粒度仍停在目标偏好，而不是模型白名单、单次预算或任务规则。它把产品问题从“默认用哪个模型”推进到“谁决定路由目标、每次实际用了什么、费用如何解释”。",
    "personal_relevance_cn": "评估自动选模时，应同时检查用户偏好、管理员模型策略、任务级实际模型、费用、延迟和结果质量。只给三档入口还不够，至少要能回看每次路由结果，并区分用户偏好与组织政策谁优先。",
    "product_opportunity_cn": "把自动选模做成可审计策略对象：目标偏好、允许模型、任务类型、成本上限和回退顺序分别配置；每次响应记录候选模型、最终选择、费用、延迟和策略版本，方便复盘质量与成本。",
    "competitive_risk_cn": "GitHub 已经把自动路由扩展到多端，并允许管理员政策缩小候选模型池。当前三档仍是粗粒度控制，官方没有公开路由评分、阈值或逐任务成本预估，也没有证明 intelligence 档在真实代码任务上稳定优于 balance。",
    "recommended_action": "test",
    "questions_to_validate": [
      "三档设置是按设备、产品端、用户还是组织保存，跨端是否一致？",
      "管理员禁用模型、数据驻留和 FedRAMP 策略与用户选择的 tier 如何裁决？",
      "每次响应能看到最终模型，但能否导出路由理由、费用、延迟和策略版本？",
      "intelligence 与 balance 在同一任务集上的质量、费用和响应时间差异有多大？"
    ],
    "follow_up_triggers": [
      "Auto tiers 扩展到 GitHub 网页、JetBrains、Visual Studio、Xcode 或 Eclipse",
      "GitHub 开放任务级路由日志、成本预估或组织级 tier 策略",
      "出现独立测试比较三档在同一代码任务集上的质量、费用和延迟"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 4,
      "technical_or_product_significance": 4,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 3,
      "agent_architecture_value": 4,
      "ai_product_value": 5,
      "macro_value": 2,
      "actionability": 5
    },
    "report_date": "2026-09-15",
    "event_date": "2026-09-14",
    "canonical_url": "https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection",
    "first_seen_date": "2026-09-15",
    "last_seen_date": "2026-09-15",
    "run_dates": [
      "2026-09-15"
    ],
    "evidence_boundary": "GitHub Changelog 正文确认三档含义、相同候选模型池、逐 Prompt 选择、推送端、按实际模型计费和 10% auto 折扣；官方文档补充了系统健康、任务复杂度、管理员模型政策与逐响应显示实际模型。Changelog 使用 2026-09-14 日期路径，RSS 给出 2026-09-14T16:05:27Z。功能仍在 rollout，未核验所有账户可见性，也没有独立比较三档质量、费用和延迟。",
    "related_sources": [
      {
        "url": "https://docs.github.com/copilot/concepts/models/auto-model-selection",
        "type": "official_product_documentation"
      }
    ]
  }
];
