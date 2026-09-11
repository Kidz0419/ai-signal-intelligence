window.DAILY_SIGNALS = [
  {
    "id": "2026-09-10-google-adk-python-2-9-resilience-resume",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "Google ADK 2.9.0 加入模型自动故障转移，但恢复失败节点可能重复外部动作",
    "summary": "Google ADK Python 2.9.0 正式加入 FallbackModel，可在主模型报错时自动切换备用模型；同时新增 LiveKit 语音与电话 runner、YAML 图工作流、MCP SDK 2.x 兼容和 OTLP 日志导出。更值得注意的是恢复语义变化：失败节点现在会重新执行，若节点在报错前已产生外部副作用，恢复后可能再次执行，因此官方明确要求节点逻辑具备幂等性。版本还把 GCS 工具的本地文件访问限制在 local_file_root 内，未配置时直接拒绝。",
    "decision": "include",
    "confidence": 96,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "technical_update",
    "information_type": "agent_runtime",
    "evidence_level": "confirmed",
    "source": "Google Agent Development Kit",
    "url": "https://github.com/google/adk-python/releases/tag/v2.9.0",
    "published_at": "2026-09-10T21:22:43Z",
    "primary_tags": [
      "Google ADK",
      "FallbackModel",
      "Workflow Resume"
    ],
    "secondary_tags": [
      "Idempotency",
      "LiveKit",
      "MCP 2.x",
      "OTLP"
    ],
    "why_it_matters_cn": "这版把可用性、任务恢复和副作用风险放进同一个运行时问题里。模型自动切换能减少中断，但工作流恢复如果没有幂等设计，可能把一次失败变成重复扣款、重复发信或重复写入。",
    "personal_relevance_cn": "评估 Agent 框架时，不能只问有没有 retry 和 failover。还要核对重放边界、幂等键、外部动作日志、人工确认点，以及恢复时到底重跑哪个节点。",
    "product_opportunity_cn": "可把模型故障转移记录、节点 checkpoint、副作用幂等键、恢复预览和人工批准做成统一控制面，并允许按动作风险设置自动恢复或停下等待。",
    "competitive_risk_cn": "Release 证明代码和语义已进入正式版本，但没有给出生产故障转移成功率、切换策略、成本上限或重复副作用的自动检测与补偿机制。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "FallbackModel 按什么错误类型和顺序切换，是否支持预算、延迟与区域约束？",
      "失败节点恢复时是否有稳定 execution ID、幂等键或补偿事务，谁负责阻止重复外部动作？",
      "OTLP 日志能否串起主模型失败、备用模型接管、HITL 暂停和恢复后的完整链路？"
    ],
    "follow_up_triggers": [
      "Google 发布 FallbackModel 的生产指标、策略配置或故障复盘",
      "ADK 增加副作用检测、幂等键、补偿事务或恢复前预览",
      "YAML 图工作流和 LiveKit runner 出现权限、审计或暂停恢复文档"
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
      "macro_value": 2,
      "actionability": 5
    },
    "report_date": "2026-09-11",
    "event_date": "2026-09-10",
    "canonical_url": "https://github.com/google/adk-python/releases/tag/v2.9.0",
    "first_seen_date": "2026-09-11",
    "last_seen_date": "2026-09-11",
    "run_dates": [
      "2026-09-11"
    ],
    "evidence_boundary": "GitHub Release 页面和 API 确认 v2.9.0 于 2026-09-10T21:22:43Z 发布，正文明确列出自动模型故障转移、恢复语义、路径限制、LiveKit、YAML 工作流、MCP 2.x 与 OTLP 日志。生产可靠性、成本和补偿机制没有公开数据。",
    "related_sources": [
      {
        "url": "https://github.com/google/adk-python/commit/c300b8ded62b8bc4168cdede4c85bec66d1aa8ee",
        "type": "fallback_model_commit"
      },
      {
        "url": "https://github.com/google/adk-python/commit/2fb877cd0ea5f866d2b66153b00749ebb61bdce4",
        "type": "workflow_resume_commit"
      },
      {
        "url": "https://github.com/google/adk-python/commit/6d145180611956b2065704189517fd6a0ff1a063",
        "type": "nested_hitl_commit"
      }
    ]
  }
];
