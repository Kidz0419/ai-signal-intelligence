window.DAILY_SIGNALS = [
  {
    "id": "2026-08-28-anthropic-model-hardware-standard-preview",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "Anthropic 开放 Model Hardware Standard 研究预览，把 AI agent 接到实验室和制造设备",
    "summary": "Anthropic 宣布向首批科研实验室和先进制造企业开放 Model Hardware Standard（MHS）研究预览。官方把它定义为让 AI agent 安全操作物理设备的共享规范，覆盖显微镜、液体处理器、机械臂等对象，并明确高风险决策仍需要人工审批。[1]",
    "decision": "watchlist",
    "confidence": 90,
    "relevance_level": "P1",
    "signal_type": "strategic_radar",
    "content_type": "official_release",
    "information_type": "agent_architecture",
    "evidence_level": "confirmed",
    "source": "Anthropic",
    "url": "https://www.anthropic.com/news/model-hardware-standard-research-preview",
    "published_at": "2026-08-27",
    "primary_tags": [
      "Anthropic",
      "Model Hardware Standard",
      "Physical Agents"
    ],
    "secondary_tags": [
      "Human Approval",
      "Robotics",
      "Lab Automation"
    ],
    "why_it_matters_cn": "这条不是普通研究博客。它把 Agent 的标准化对象从软件工具扩到物理仪器，开始正面回答对象协议、动作边界和高风险审批怎么定义。",
    "personal_relevance_cn": "值得重点盯住对象模型、命令语义、人工审批、暂停恢复和设备日志这些控制面字段，而不是只看“机器人+AI”叙事。",
    "product_opportunity_cn": "如果 MHS 继续扩展，做实验自动化、工业软件或具身 Agent 的团队会需要统一的设备适配层、审批流和审计日志模型。",
    "competitive_risk_cn": "当前只是首批研究预览，不代表已经形成广泛行业标准，也不代表生产环境里的安全性和责任边界已经解决。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "MHS 的对象模型、命令语义和权限分层会不会公开成可复用规范？",
      "人工审批、暂停恢复和日志字段是否会进入正式 SDK 或设备适配实现？",
      "除 Anthropic 生态外，是否会出现更多设备厂商、实验室软件或开源机器人栈的原生支持？"
    ],
    "follow_up_triggers": [
      "Anthropic 或合作方公开协议文档、SDK、参考实现或更细的审批流程",
      "Hugging Face、Raspberry Pi 等早期采用方发布可复现实例或代码",
      "出现独立生态方对 MHS 的支持、对照标准或反向兼容层"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 5,
      "technical_or_product_significance": 4,
      "strategic_value": 5,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 5,
      "ai_product_value": 2,
      "macro_value": 3,
      "actionability": 4
    },
    "report_date": "2026-08-28",
    "event_date": "2026-08-27",
    "canonical_url": "https://www.anthropic.com/news/model-hardware-standard-research-preview",
    "first_seen_date": "2026-08-28",
    "last_seen_date": "2026-08-28",
    "run_dates": [
      "2026-08-28"
    ],
    "evidence_boundary": "Anthropic 官方页面确认研究预览、首批对象类型、早期采用方和高风险审批边界；未给出广泛部署数据，也不代表已经成为正式行业标准。"
  },
  {
    "id": "2026-08-28-claude-code-21248-restricted-runtime",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "Claude Code v2.1.248 加入 restricted mode、跨会话消息和服务器托管设置诊断",
    "summary": "Claude Code v2.1.248 新增 `--restricted` / `CLAUDE_CODE_RESTRICTED=1`，可移除命令执行、代码执行和 WebFetch 等高风险内建工具，并把文件工具限制在工作目录内；同版还加入跨会话消息、agent frontmatter prompt cache TTL，以及服务器托管设置加载失败的 `/doctor` 与 `/status` 诊断。[2]",
    "decision": "include",
    "confidence": 95,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "technical_update",
    "information_type": "agent_governance",
    "evidence_level": "confirmed",
    "source": "Anthropic",
    "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.248",
    "published_at": "2026-08-27T22:12:20Z",
    "primary_tags": [
      "Claude Code",
      "Restricted Mode",
      "Cross-session Messaging"
    ],
    "secondary_tags": [
      "Prompt Cache TTL",
      "Server-managed Settings",
      "WebFetch"
    ],
    "why_it_matters_cn": "这版最值钱的不是单个修复，而是把运行权限、配置来源、会话间协作和诊断信息显式抬到控制面。Coding agent 正在从“能跑”走向“能被限制、被解释、被运维”。",
    "personal_relevance_cn": "如果自建 Agent 运行时，要优先对照 restricted mode 的默认禁用面、目录隔离、设置优先级和故障诊断出口。",
    "product_opportunity_cn": "可借鉴受限模式、跨会话消息和运行状态诊断这三块，做企业环境下更容易过审的 Coding Agent 控制面。",
    "competitive_risk_cn": "版本说明来自官方 Release；还没有公开生产指标证明 restricted mode、诊断提示或跨会话消息在复杂环境里已经足够稳定。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "restricted mode 在真实团队里默认关闭了哪些工具，是否支持细粒度白名单？",
      "跨会话消息与权限审批、日志审计、身份归因之间的关系会不会继续公开？",
      "server-managed settings 的失败原因是否会进入更正式的管理员控制面？"
    ],
    "follow_up_triggers": [
      "Anthropic 发布更完整的企业文档、管理员配置说明或真实 UI",
      "后续 Release 给出 restricted mode 的默认策略、白名单或审计能力",
      "出现独立团队对该模式的安全与可用性复盘"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 4,
      "technical_or_product_significance": 5,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 5,
      "ai_product_value": 3,
      "macro_value": 1,
      "actionability": 5
    },
    "report_date": "2026-08-28",
    "event_date": "2026-08-28",
    "canonical_url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.248",
    "first_seen_date": "2026-08-28",
    "last_seen_date": "2026-08-28",
    "run_dates": [
      "2026-08-28"
    ],
    "evidence_boundary": "官方 Release 明确列出 restricted mode、cross-session messaging、cache TTL 和诊断能力；未公开这些能力在企业生产环境中的成功率、误报率或运维成本。",
    "related_sources": [
      {
        "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.250",
        "type": "same_day_followup_release"
      }
    ]
  },
  {
    "id": "2026-08-28-github-copilot-code-review-expanded-capabilities",
    "demo": false,
    "topic_lane": "ai_product",
    "title": "GitHub Copilot code review 扩到 bot PR、大型 PR，并要求用户给出 comment resolution reason",
    "summary": "GitHub 官方 Changelog 确认，Copilot code review 现在可以完整审查由 bot 创建的 pull request，包括 Copilot cloud agent 打开的 PR；此前 300 个文件或 2 万行代码的体量限制也被移除，同时用户在关闭 Copilot review comment 时可以提交 resolution reason。[3]",
    "decision": "include",
    "confidence": 94,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "official_release",
    "information_type": "product_workflow",
    "evidence_level": "confirmed",
    "source": "GitHub",
    "url": "https://github.blog/changelog/2026-08-27-copilot-code-review-resolution-reasons-and-expanded-capabilities",
    "published_at": "2026-08-27T15:46:04-07:00",
    "primary_tags": [
      "GitHub Copilot",
      "Code Review",
      "Copilot Cloud Agent"
    ],
    "secondary_tags": [
      "Resolution Reasons",
      "Large Pull Requests"
    ],
    "why_it_matters_cn": "这说明 Copilot 正在把代码审查从“建议器”推向更完整的工作流节点：既覆盖 agent 生成的 PR，也开始记录人类为什么接受或关闭建议。",
    "personal_relevance_cn": "值得用它反推自家 Agent 产品里哪些动作必须保留人工解释字段，哪些系统日志应该沉淀成 review 证据。",
    "product_opportunity_cn": "可以研究 review reason、超大 PR 审查和 bot PR 审查能否组合成更完整的 agent execution audit trail。",
    "competitive_risk_cn": "官方页面确认了范围扩展和 resolution reason，但没有给出审查质量、误报、企业导出或审批联动数据。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "resolution reason 是否会进入团队级报表、审计导出或 policy 训练闭环？",
      "对超大 PR 的审查是否仍有隐性性能或模型配额限制？",
      "bot PR 审查与 Copilot cloud agent 的自动执行边界是否会进一步开放？"
    ],
    "follow_up_triggers": [
      "GitHub 发布管理员文档、导出能力或企业案例",
      "出现真实 UI、报表或 policy 配置页面",
      "Copilot cloud agent 的 PR 审查与合并策略进一步公开"
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
      "macro_value": 1,
      "actionability": 4
    },
    "report_date": "2026-08-28",
    "event_date": "2026-08-28",
    "canonical_url": "https://github.blog/changelog/2026-08-27-copilot-code-review-resolution-reasons-and-expanded-capabilities",
    "first_seen_date": "2026-08-28",
    "last_seen_date": "2026-08-28",
    "run_dates": [
      "2026-08-28"
    ],
    "evidence_boundary": "官方 Changelog 确认 bot PR、超大 PR 和 resolution reason 的支持范围；没有公开审查效果、审计导出或组织治理层面的完整实现。"
  },
  {
    "id": "2026-08-28-kimi-code-0390-remote-control-fork",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "Kimi Code 0.39.0 加入实验性 Remote Control，并让 subagent 可继承调用者会话快照",
    "summary": "Kimi Code 0.39.0 的官方 Release 加入实验性 Remote Control，用来远程访问本地 web session；同版还给 subagent / swarm 工具增加可选 `fork` 参数，让子代理带着调用者会话历史快照启动。[4]",
    "decision": "include",
    "confidence": 88,
    "relevance_level": "P2",
    "signal_type": "strategic_radar",
    "content_type": "technical_update",
    "information_type": "agent_runtime",
    "evidence_level": "confirmed",
    "source": "MoonshotAI",
    "url": "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.39.0",
    "published_at": "2026-08-27T11:36:28Z",
    "primary_tags": [
      "Kimi Code",
      "Remote Control",
      "Subagent Fork"
    ],
    "secondary_tags": [
      "Swarm",
      "Session Snapshot"
    ],
    "why_it_matters_cn": "远程接入本地会话和子代理继承历史快照，都是 Agent 从单轮助手走向长任务协作时会踩到的真实边界。",
    "personal_relevance_cn": "这类能力要重点盯身份、会话隔离、日志和误操作半径，尤其是 remote control 这种会放大执行面的入口。",
    "product_opportunity_cn": "如果继续演进，remote control、subagent fork 和多会话面板会组合成新的 Agent 操作台形态。",
    "competitive_risk_cn": "功能仍标记为 experimental，Release 没有给出权限模型、默认暴露面或生产使用反馈。",
    "recommended_action": "monitor",
    "questions_to_validate": [
      "Remote Control 的认证、网络暴露面和日志默认行为是什么？",
      "subagent fork 继承哪些历史和状态，是否支持敏感信息剥离？",
      "后续会不会出现更明确的审批、暂停或回滚控制？"
    ],
    "follow_up_triggers": [
      "Moonshot 发布更详细文档、真实演示或安全说明",
      "experimental 标签移除或进入默认 UI",
      "出现关于 remote control 或 subagent fork 的使用复盘"
    ],
    "scores": {
      "topic_relevance": 4,
      "novelty": 4,
      "technical_or_product_significance": 4,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 4,
      "ai_product_value": 3,
      "macro_value": 1,
      "actionability": 3
    },
    "report_date": "2026-08-28",
    "event_date": "2026-08-28",
    "canonical_url": "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.39.0",
    "first_seen_date": "2026-08-28",
    "last_seen_date": "2026-08-28",
    "run_dates": [
      "2026-08-28"
    ],
    "evidence_boundary": "官方 Release 确认 experimental Remote Control 和 subagent/swarm fork 参数；未公开权限模型、默认暴露面或生产可用性结论。"
  }
];
