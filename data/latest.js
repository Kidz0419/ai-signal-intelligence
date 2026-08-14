window.DAILY_SIGNALS = [
  {
    "id": "2026-08-14-google-gemini-37-flash",
    "demo": false,
    "topic_lane": "model",
    "title": "Google 发布 Gemini 3.7 Flash：编码与 Agent 能力提升，年内以 3.6 Flash 半价进入 API 与 Spark",
    "summary": "Google 官方发布 Gemini 3.7 Flash，定位为面向编码和 Agent 的高性价比工作模型。相较 3.6 Flash，官方报告 FrontierCode 1.1 Main 为 43.6% 对 34.4%、DeepSWE v1.1 为 65.3% 对 49.0%、GDP.pdf 为 34.0% 对 22.0%、AutomationBench 为 30.4% 对 17.0%。模型年内采用每百万输入/输出 token 0.75/3.75 美元的介绍价，并于当日进入 Gemini API、AI Studio、Android Studio、Google Antigravity、Gemini Enterprise Agent Platform 和 Gemini Spark。Spark 已实际切换该模型，以改进 Workspace 工具调用和多技能知识工作；所有成绩和效率判断仍主要来自 Google 自报。",
    "decision": "include",
    "confidence": 97,
    "relevance_level": "P0",
    "signal_type": "core",
    "content_type": "official_release",
    "information_type": "model_release",
    "evidence_level": "confirmed",
    "source": "Google",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "published_at": "2026-08-13T17:00:00Z",
    "primary_tags": [
      "Gemini 3.7 Flash",
      "Coding",
      "Agent Workflows"
    ],
    "secondary_tags": [
      "API Pricing",
      "Gemini Spark",
      "Tool Use",
      "Enterprise Automation"
    ],
    "why_it_matters_cn": "这是模型能力、价格、API/企业入口和实际 Agent 产品切换同时发生的事件；Flash 级模型开始以更低单位成本争夺长链路编码、文档理解和企业工作流。",
    "personal_relevance_cn": "应把 Gemini 3.7 Flash 加入个人真实编码、复杂文档和多工具任务评测，重点比较相对 3.6 Flash、Grok 4.6 与高价模型的单位成功任务成本、重试次数和人工监督负担。",
    "product_opportunity_cn": "可测试在模型路由中用 3.7 Flash 承接高频编码、文档理解和 Workspace 多技能任务，并保留更昂贵模型处理失败升级。",
    "competitive_risk_cn": "年内半价与 Spark、Enterprise Agent Platform 同日切换会放大 Google 的模型—工具—分发闭环；若真实成功率接近高价模型，会压缩中间层模型和独立 Agent 产品的成本空间。",
    "recommended_action": "alert",
    "questions_to_validate": [
      "在真实代码库中，43.6% FrontierCode 与 65.3% DeepSWE 的提升能否复现，回归缺陷和重试次数如何？",
      "0.75/3.75 美元介绍价结束后的正式价格、速率限制和上下文缓存成本是什么？",
      "Spark 的 Workspace 工具调用准确率、越权率、人工接管率和任务恢复表现如何？"
    ],
    "follow_up_triggers": [
      "第三方发布 Gemini 3.7 Flash 编码与 Agent 评测",
      "Google 公布年末之后正式价格或调整介绍价",
      "Gemini Spark 发布工具调用、安全或真实采用数据"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 5,
      "technical_or_product_significance": 5,
      "strategic_value": 5,
      "source_quality": 5,
      "model_value": 5,
      "agent_architecture_value": 4,
      "ai_product_value": 5,
      "macro_value": 3,
      "actionability": 5
    },
    "report_date": "2026-08-14",
    "event_date": "2026-08-14",
    "canonical_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash",
    "first_seen_date": "2026-08-14",
    "last_seen_date": "2026-08-14",
    "run_dates": [
      "2026-08-14"
    ]
  }
];
