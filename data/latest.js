window.DAILY_SIGNALS = [
  {
    "id": "2026-08-26-github-copilot-customize-tab-ga",
    "demo": false,
    "topic_lane": "ai_product",
    "title": "GitHub Copilot app 的 Customize tab 正式 GA，把 MCP servers、plugins、skills 和 canvases 收到同一入口",
    "summary": "GitHub 官方 Changelog 确认，GitHub Copilot app 的 Customize tab 已正式 GA。这个入口把 MCP servers、plugins、skills 和 canvases 放到同一处，并支持按类型浏览、查看精选项，以及按类别查找 MCP servers。[1]",
    "decision": "include",
    "confidence": 92,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "official_release",
    "information_type": "product_workflow",
    "evidence_level": "confirmed",
    "source": "GitHub",
    "url": "https://github.blog/changelog/2026-08-25-github-copilot-app-customize-tab-is-generally-available/",
    "published_at": "2026-08-25T13:05:26-07:00",
    "primary_tags": [
      "GitHub Copilot",
      "MCP",
      "Customize tab"
    ],
    "secondary_tags": [
      "plugins",
      "skills",
      "canvases"
    ],
    "why_it_matters_cn": "这不是单个小功能。GitHub 正在把 Copilot 的外部工具、知识和工作流扩展收口到统一控制面，MCP 从协议概念更进一步变成产品分发入口。",
    "personal_relevance_cn": "值得拿它对照自有 Agent 产品的扩展入口设计：入口是否统一，扩展是否按类型管理，团队是否能看见哪些能力正在被启用。",
    "product_opportunity_cn": "可以研究“扩展市场 + 运行入口 + 团队治理”三层是否需要拆开，以及 MCP server 的发现、安装、权限提示和结果可见性该怎么做。",
    "competitive_risk_cn": "如果 Copilot 先把扩展生态和默认工作流入口做顺，开发者会更习惯在一个主界面里接入工具与知识，其他 Agent 产品的分发成本会变高。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "组织管理员能否控制哪些 MCP servers、plugins、skills 或 canvases 对团队可见？",
      "Customize tab 当前覆盖 Web、Desktop 还是只限特定 Copilot app 入口？",
      "扩展安装、启用和权限提示是否会进入后续的审计日志或团队治理面板？"
    ],
    "follow_up_triggers": [
      "GitHub 发布更详细的产品文档或管理员控制说明",
      "出现真实 UI 演示、管理员权限页或企业版 rollout 细节",
      "MCP Registry、skills 和 plugins 在 Copilot 中的排序或推荐机制进一步公开"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 4,
      "technical_or_product_significance": 4,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 4,
      "ai_product_value": 5,
      "macro_value": 2,
      "actionability": 4
    },
    "report_date": "2026-08-26",
    "event_date": "2026-08-26",
    "canonical_url": "https://github.blog/changelog/2026-08-25-github-copilot-app-customize-tab-is-generally-available",
    "first_seen_date": "2026-08-26",
    "last_seen_date": "2026-08-26",
    "run_dates": [
      "2026-08-26"
    ]
  }
];
