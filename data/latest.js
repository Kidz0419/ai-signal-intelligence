window.DAILY_SIGNALS = [
  {
    "id": "2026-09-12-simon-chatgpt-work-compaction-provenance-gap",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "Simon Willison 实测 ChatGPT Work：27 分钟产出可用路线，但压缩后连执行代码都取不回",
    "summary": "Simon Willison 让 ChatGPT Work 的 GPT-6 Astra（Max）基于 OpenStreetMap 生成从住址出发的 5K 和 10K 环线。任务运行 27 分钟，交付了内嵌地图、GPX 和 GeoJSON；公开 HTML 也保留了路线几何。问题出在过程证据：产品界面没有展示实际代码和完整步骤，线程压缩后又无法把执行过的 Python 代码交还给用户。作者据此主张，采用上下文压缩的 Agent 应保留压缩前文本，并允许工具调用读取。",
    "decision": "include",
    "confidence": 92,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "practitioner_statement",
    "information_type": "agent_runtime",
    "evidence_level": "primary_statement",
    "source": "Simon Willison",
    "url": "https://simonwillison.net/2026/Sep/12/astra-running-routes/",
    "published_at": "2026-09-12T23:56:42Z",
    "primary_tags": [
      "ChatGPT Work",
      "Context Compaction",
      "Execution Provenance"
    ],
    "secondary_tags": [
      "GPT-6 Astra",
      "OpenStreetMap",
      "Artifact Export",
      "Observability"
    ],
    "why_it_matters_cn": "这次实测把长任务 Agent 的一个常被忽略的问题暴露得很具体：结果文件能留下，不代表用户还能解释、复查或重跑 Agent 当时做过什么。上下文压缩如果同时吞掉代码和工具轨迹，交付物就失去可审计性。",
    "personal_relevance_cn": "评估长任务 Agent 时，不能只验收最后有没有文件，还要检查压缩前对话、执行代码、工具参数、数据来源和中间产物能否导出，并确认这些证据是否跨压缩与会话保留。",
    "product_opportunity_cn": "可把不可变执行包做成标准能力：每次运行固定保存模型版本、工具调用、代码、输入来源、产物清单和压缩前 transcript；压缩只影响当前上下文，不删除审计证据，用户还能一键导出或复跑。",
    "competitive_risk_cn": "这是单次公开实测，不是 OpenAI 的正式产品文档。页面能证明作者拿到了路线文件并遇到代码不可见、压缩后无法取回的问题，但不能确认所有 ChatGPT Work 任务都会如此，也没有独立验证路线正确性；把原因归于 compaction 是作者根据交互结果作出的判断。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "ChatGPT Work 是否在后台保留完整执行代码、工具参数和压缩前 transcript，只是没有向用户开放？",
      "线程压缩、会话重启和分享后，哪些中间产物与日志仍可导出，保留多久？",
      "用户能否从最终 GPX、GeoJSON 或可视化追溯到数据请求、计算步骤和模型版本，并复跑同一任务？"
    ],
    "follow_up_triggers": [
      "OpenAI 发布 ChatGPT Work 的运行历史、上下文压缩、日志或导出文档",
      "产品 UI 开放代码、工具调用和压缩前 transcript 的查看或下载",
      "出现更多长任务因 compaction 丢失过程证据的可复现实测或官方修复"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 5,
      "technical_or_product_significance": 4,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 2,
      "agent_architecture_value": 5,
      "ai_product_value": 4,
      "macro_value": 1,
      "actionability": 5
    },
    "report_date": "2026-09-13",
    "event_date": "2026-09-12",
    "canonical_url": "https://simonwillison.net/2026/Sep/12/astra-running-routes",
    "first_seen_date": "2026-09-13",
    "last_seen_date": "2026-09-13",
    "run_dates": [
      "2026-09-13"
    ],
    "speaker_name": "Simon Willison",
    "speaker_role": "独立研究者、开发者工具作者、长期进行 AI 产品与模型实测的写作者",
    "speaker_type": "independent_researcher",
    "statement_topic": "长任务 Agent 在上下文压缩后的执行透明度与证据保留",
    "original_source_url": "https://simonwillison.net/2026/Sep/12/astra-running-routes/",
    "new_information": "公开了一次 27 分钟 ChatGPT Work 路线生成任务的输入、输出格式和可访问 HTML 产物，并记录了实际代码在界面不可见、线程压缩后无法取回的失败边界。",
    "evidence_artifact": "作者原始长文、路线截图、可下载 GPX/GeoJSON 的说明，以及包含完整路线几何和 D3 渲染代码的公开 Gist HTML。",
    "evidence_boundary": "Atom feed 确认精确发布时间为 2026-09-12T23:56:42Z；正文和 Gist 支持任务输入、27 分钟运行、输出格式、代码不可见与压缩后无法取回。任务执行链路、路线正确性和 compaction 的内部实现没有官方文档或独立复现。",
    "related_sources": [
      "https://gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480",
      "https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/"
    ]
  }
];
