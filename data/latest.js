window.DAILY_SIGNALS = [
  {
    "id": "2026-09-15-google-ai-science-workflow-bottlenecks",
    "demo": false,
    "topic_lane": "ai_macro",
    "title": "Google 调研 637 名科学家：AI 每周省近 7 小时，但瓶颈转向验证和实验",
    "summary": "Google、Google DeepMind 与 MIT FutureTech 发布 AI in Science 研究。报告结合约 1500 万条 Gemini、AI Mode 与 API 匿名交互、2690 个有论文和代码关联的专业科学模型，以及 637 名英美科学家问卷。受访者中约 47% 每天使用某种 AI，平均自报每周节省 6.9 小时；但团队把更多时间花在核验 AI 输出，未测试假设开始积压，物理实验和临床验证等下游环节成为新瓶颈。",
    "decision": "include",
    "confidence": 91,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "analysis",
    "information_type": "enterprise_adoption",
    "evidence_level": "primary_statement",
    "source": "Google / Google DeepMind / MIT FutureTech",
    "url": "https://blog.google/innovation-and-ai/technology/ai/ai-economy-atlas-september-2026",
    "published_at": "2026-09-15",
    "primary_tags": [
      "AI Adoption",
      "Scientific Workflow",
      "Workflow Bottlenecks"
    ],
    "secondary_tags": [
      "Google ATLAS",
      "Output Validation",
      "AI Productivity"
    ],
    "why_it_matters_cn": "这批数据没有把节省时间直接等同于更多科研产出。AI 加快检索、写作和分析后，核验、实验和临床验证可能接过瓶颈，组织收益取决于能否重排整条科研生产流程。",
    "personal_relevance_cn": "评估企业 AI 采用时，应同时追踪任务耗时、输出核验成本、待处理队列和下游瓶颈，而不是只看活跃率或员工自报节省时间。这个框架也适用于产品、运营和合规流程。",
    "product_opportunity_cn": "可把 AI 采用看板从席位和调用量扩展到任务级证据：节省在哪一步、增加了多少复核、积压转移到哪里、哪些结论必须进入实验或专家审批，并按流程阶段配置责任人和 SLA。",
    "competitive_risk_cn": "交互日志只覆盖 Google 自有 Gemini、AI Mode 和 API 样本，企业流量被排除；科学任务由分类器推断。6.9 小时来自英美 637 名科学家的自报问卷，不是随机对照或实际产出测量，不能外推为全行业生产率。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "不同科研阶段的时间节省、复核时间和错误率能否用同一任务日志而非问卷复现？",
      "未测试假设积压增加后，团队如何分配实验、临床验证和专家审批容量？",
      "Google ATLAS 排除企业流量后，组织内协作、权限和合规成本会不会改变结论？"
    ],
    "follow_up_triggers": [
      "Google 发布后续 ATLAS 波次、可复核数据或跨期科研产出指标",
      "出现独立机构对 AI 科研节时、核验成本和下游瓶颈的复现",
      "科研 AI 产品增加假设队列、证据链、审批和实验容量管理"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 5,
      "technical_or_product_significance": 4,
      "strategic_value": 5,
      "source_quality": 4,
      "model_value": 2,
      "agent_architecture_value": 3,
      "ai_product_value": 4,
      "macro_value": 5,
      "actionability": 5
    },
    "report_date": "2026-09-16",
    "event_date": "2026-09-15",
    "canonical_url": "https://blog.google/innovation-and-ai/technology/ai/ai-economy-atlas-september-2026",
    "first_seen_date": "2026-09-16",
    "last_seen_date": "2026-09-16",
    "run_dates": [
      "2026-09-16"
    ],
    "evidence_boundary": "Google 官方博客明确标注 Sep 15, 2026，正文和联合研究 PDF 支持样本、问卷与结果。博客页面只给日期没有时区和时分，本记录保留 date-only。所有使用率、节时和瓶颈结论均来自 Google 主导的数据与受访者自报，尚无独立复现。",
    "related_sources": [
      {
        "url": "https://ai.google/static/documents/AI-in-Science.pdf",
        "type": "joint_research_report"
      },
      {
        "url": "https://ai.google/economy/atlas/",
        "type": "interactive_dataset_interface"
      }
    ]
  },
  {
    "id": "2026-09-08-ibm-altk-evolve-consistency-gap",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "IBM 把 Agent 可靠性拆成 Pass^k：平均成功 77.4%，连续五次全过只有 53%",
    "summary": "IBM Research 团队提出用 Pass^k 衡量同一任务重复 k 次时每次都成功的比例，并把它与平均通过率 Mean@k 的差称为 consistency gap。在 AppWorld test_normal 的 168 个任务上，GPT-4.1 ReAct Agent 的 Mean@5 为 77.4%，Pass^5 只有 53.0%。团队用单条轨迹逐决策点重采样，定位容易翻转的步骤，再把诊断生成可复用指南；其自报评测把 Pass^5 提升到 69.0%，Mean@5 提升到 81.0%。",
    "decision": "include",
    "confidence": 92,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "technical_update",
    "information_type": "research_insight",
    "evidence_level": "primary_statement",
    "source": "IBM Research / ALTK-Evolve",
    "url": "https://huggingface.co/blog/ibm-research/altk-evolve-consistency",
    "published_at": "2026-09-15T16:00:44Z",
    "primary_tags": [
      "Agent Reliability",
      "Pass^k",
      "Consistency Analyzer"
    ],
    "secondary_tags": [
      "AppWorld",
      "Trajectory Resampling",
      "Episodic Guidelines"
    ],
    "why_it_matters_cn": "平均准确率会把时好时坏的任务藏起来。对支付核对、合同检查或其他高责任工作流，用户要的是同一条件下可重复成功；Pass^k 可以把这种可靠性从能力均值里单独量出来。",
    "personal_relevance_cn": "Agent 评测应在 Mean@k 之外加入同任务重复运行、Pass^k、失败翻转点和干预率，并把 Pass^k 与可验证后重试的 Pass@k 分开。上线门槛要按任务风险设定，不能只看一次成功。",
    "product_opportunity_cn": "可在 Agent 运行平台增加重复任务评测、决策点稳定度、轨迹差异和指南版本记录；对不稳定步骤设置人工确认、确定性工具或更窄的操作策略，再比较修复前后的 Pass^k 和平均准确率。",
    "competitive_risk_cn": "结果来自作者团队在单一 AppWorld 测试集、ReAct 架构和 GPT-4.1 上的评测，没有独立复现。诊断会增加每个决策点的离线模型调用，且只用一条轨迹和黑盒重采样不能覆盖工具副作用、环境漂移或真实生产并发。代码仓库在博客发布前已存在 consistency 实现，9 月 15 日的新信息主要是论文与完整评测解释，不应写成当天首次上线。",
    "recommended_action": "prototype",
    "questions_to_validate": [
      "在支付、合同和数据分析任务上，Mean@k 与 Pass^k 的差距有多大，失败是否集中在少数工具决策点？",
      "固定温度、固定种子、模型版本和工具环境后，剩余不一致分别来自模型、路由、工具还是外部状态？",
      "生成的 consistency guideline 能跨任务、跨模型和跨版本保持效果多久，何时需要失效或回滚？"
    ],
    "follow_up_triggers": [
      "出现对 arXiv:2609.08832 的独立复现或更多模型、基准结果",
      "ALTK-Evolve 发布与论文对应的稳定版本、配置和完整复现实验",
      "主流 Agent eval 平台开始同时报告 Mean@k、Pass^k、Pass@k 和干预率"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 5,
      "technical_or_product_significance": 5,
      "strategic_value": 4,
      "source_quality": 4,
      "model_value": 3,
      "agent_architecture_value": 5,
      "ai_product_value": 4,
      "macro_value": 2,
      "actionability": 5
    },
    "report_date": "2026-09-16",
    "event_date": "2026-09-08",
    "canonical_url": "https://huggingface.co/blog/ibm-research/altk-evolve-consistency",
    "first_seen_date": "2026-09-16",
    "last_seen_date": "2026-09-16",
    "run_dates": [
      "2026-09-16"
    ],
    "evidence_boundary": "Hugging Face 上的 IBM Research 原文标注 2026-09-15，RSS 给出 2026-09-15T16:00:44Z；arXiv 论文 v1 于 2026-09-08 提交，因此事件日期保留为 9 月 8 日并作为 catch-up。数字均为作者自报实验。GitHub 精确 commit bfff8238a0a8 显示 consistency pipeline 与测试在 8 月已进入代码，能确认实现工件存在，但当前仓库状态和 9 月 14 日 v1.2.0 不能被解释为 9 月 15 日首次发布该方法。",
    "related_sources": [
      {
        "url": "https://arxiv.org/abs/2609.08832",
        "type": "technical_report_v1"
      },
      {
        "url": "https://github.com/AgentToolkit/altk-evolve/commit/bfff8238a0a897d591a7fee14953038f7adfdf4b",
        "type": "source_commit_consistency_pipeline"
      },
      {
        "url": "https://github.com/AgentToolkit/altk-evolve",
        "type": "open_source_repository"
      }
    ]
  }
];
