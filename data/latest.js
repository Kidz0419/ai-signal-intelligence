window.DAILY_SIGNALS = [
  {
    "id": "2026-09-01-aws-mcp-stateless-migration-contract",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "AWS 把 MCP 迁移要点写实了：无状态核心能删 sticky session，但旧客户端没退干净前别提前拆",
    "summary": "AWS 9 月 1 日的官方正文把 MCP 2026-07-28 版真正落到部署层：`initialize` 握手和 `Mcp-Session-Id` header 被拿掉，请求可直接从 tool call 开始，任何实例都能响应；旧协议时代常见的 sticky session、共享 session store 和自定义 body 解析路由不再是默认必需品，但仍服务 2025-era 客户端时不能提前删掉遗留会话基础设施。",
    "decision": "include",
    "confidence": 95,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "technical_update",
    "information_type": "agent_architecture",
    "evidence_level": "confirmed",
    "source": "AWS",
    "url": "https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected",
    "published_at": "2026-09-01T06:09:19-07:00",
    "primary_tags": [
      "AWS",
      "MCP",
      "Stateless Protocol"
    ],
    "secondary_tags": [
      "MRTR",
      "Trace Context",
      "Legacy Client Sunset"
    ],
    "why_it_matters_cn": "这篇值钱的不是复述 MCP 更新，而是把 horizontal scaling、header 路由、MRTR、idempotent retry、trace context 和遗留客户端退场顺序讲成了可执行清单。",
    "personal_relevance_cn": "如果在做 MCP 平台，最该核对的是：是不是还依赖 sticky routing、session store、body parsing，旧客户端流量什么时候归零，以及 requestState 和 ownership 校验是不是已经补上。",
    "product_opportunity_cn": "可以把 version logging、legacy lane sunset、header-based routing、tool idempotency 和 trace propagation 做成自己的 MCP 升级验收单。",
    "competitive_risk_cn": "AWS 的文章是架构指南，不是你当前部署已经自动合规；文章也没有给出迁移后的真实错误率、成本曲线或跨云适配细节。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "现在还有多少客户端仍依赖 2025-era session 语义，legacy lane 的真实退场时间表是什么？",
      "MRTR、requestState 和 ownership enforcement 在现有 MCP 服务器里有没有被完整实现，而不是只改了 transport？",
      "删掉 sticky session 和 session store 之后，真实错误率、时延和成本曲线有没有被量化？"
    ],
    "follow_up_triggers": [
      "官方 conformance suite 或主要 SDK 发布更多 2026-07-28 迁移结果",
      "大型 MCP host 公布遗留客户端流量归零和基础设施拆除复盘",
      "更多托管网关暴露 header 路由、trace 和 cacheScope 的默认策略"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 4,
      "technical_or_product_significance": 5,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 5,
      "ai_product_value": 2,
      "macro_value": 1,
      "actionability": 5
    },
    "report_date": "2026-09-02",
    "event_date": "2026-09-01",
    "canonical_url": "https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected",
    "first_seen_date": "2026-09-02",
    "last_seen_date": "2026-09-02",
    "run_dates": [
      "2026-09-02"
    ],
    "evidence_boundary": "官方正文能确认协议变更、迁移步骤和遗留客户端保留条件；它不是官方 conformance 结果，也不证明所有现有 MCP 服务器已安全迁完。",
    "related_sources": [
      {
        "url": "https://modelcontextprotocol.io/specification/2026-07-28/changelog",
        "type": "protocol_changelog"
      }
    ]
  },
  {
    "id": "2026-09-01-aws-dms-agent-review-boundary",
    "demo": false,
    "topic_lane": "ai_product",
    "title": "AWS 把 DMS Schema Conversion 的 agent 边界讲清楚了：AI 能编排迁移，但语法过关不等于语义正确",
    "summary": "AWS 9 月 1 日的 DMS Schema Conversion 正文展示了一条更像产品工作流而不是营销页的 agent 路径：agent 负责导入元数据、启动转换、等待完成、导出 assessment report 并解析 CRITICAL action items；当 deterministic rule engine 处理不了时，生成式步骤只要求输出能通过 PL/pgSQL 语法校验，并明确要求客户继续做人审和功能测试，不能把 ‘编译通过’ 当成迁移完成。",
    "decision": "include",
    "confidence": 94,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "technical_update",
    "information_type": "product_workflow",
    "evidence_level": "confirmed",
    "source": "AWS",
    "url": "https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms",
    "published_at": "2026-09-01T08:19:13-07:00",
    "primary_tags": [
      "AWS DMS",
      "Schema Conversion",
      "Human Review"
    ],
    "secondary_tags": [
      "CRITICAL Action Items",
      "Assessment Report",
      "PL/pgSQL Validation"
    ],
    "why_it_matters_cn": "很多 AI 迁移工具最容易偷换的就是‘自动化’和‘正确性’。AWS 这篇反而把那条线划得很明白：agent 能编排和解释，但最后的语义正确性、CRITICAL 修复和上线责任还在人。",
    "personal_relevance_cn": "如果要比较数据库迁移 agent，最该看的是 action item 严重度怎么暴露、导出物是不是可审计、哪些步骤自动跑、哪些步骤必须停下来让工程师做决定。",
    "product_opportunity_cn": "可以把 assessment export、人审队列、语义回归测试和最终 apply gate 设计成迁移 agent 的默认控制面，而不是事后补流程。",
    "competitive_risk_cn": "这篇是官方产品深描，不是独立迁移成功率报告；文中示例和最佳实践不能替代你自己业务存储过程的回归验证。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "assessment report 里的 AI-generated provenance 能否进入更正式的审批流或回归测试流水线？",
      "哪些 CRITICAL / HIGH action item 仍最常把团队拦在上线前，AWS 会不会继续补 deterministic rule coverage？",
      "agent 帮助修复 action items 后，最终 apply 到 target database 的人审和回滚链路是否足够清晰？"
    ],
    "follow_up_triggers": [
      "DMS 文档或 release notes 披露更正式的 GA 状态、成功率或审计出口",
      "出现真实生产迁移复盘，说明 AI-assisted conversion 在复杂存储过程上的通过率与失败模式",
      "AWS 补充更明确的 apply gate、rollback 或 change-approval 设计"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 4,
      "technical_or_product_significance": 5,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 2,
      "ai_product_value": 5,
      "macro_value": 1,
      "actionability": 5
    },
    "report_date": "2026-09-02",
    "event_date": "2026-09-01",
    "canonical_url": "https://aws.amazon.com/blogs/database/sql-server-to-aurora-postgresql-conversion-with-ai-agents-for-aws-dms",
    "first_seen_date": "2026-09-02",
    "last_seen_date": "2026-09-02",
    "run_dates": [
      "2026-09-02"
    ],
    "evidence_boundary": "官方正文确认了 agent 工作流、四步转换管线、CRITICAL action item 解释和人审边界；没有给出跨真实生产库的大样本成功率，也没有把 AI 生成代码描述成语义等价保证。"
  },
  {
    "id": "2026-09-01-huggingface-webgpu-kernel-contracts",
    "demo": false,
    "topic_lane": "model",
    "title": "Hugging Face 把浏览器推理底层单元拆成 207 个可版本化 WebGPU kernels，还顺手做了跨设备证据层",
    "summary": "Hugging Face 9 月 1 日发布 `@huggingface/kernels`，把 207 个 WebGPU kernel 作为独立、可版本化的仓库对象放到 Hub 上，每个 kernel 都带 manifest、correctness cases、bench cases 和 WGSL 模板；同时上线 Fleet，在浏览器里跑跨设备 benchmark 和正确性检查，把 WebAI 的底层算子优化从‘库内黑盒’变成可检查、可复现、可贡献证据的公共层。",
    "decision": "include",
    "confidence": 93,
    "relevance_level": "P1",
    "signal_type": "research",
    "content_type": "technical_update",
    "information_type": "model_research",
    "evidence_level": "confirmed",
    "source": "Hugging Face",
    "url": "https://huggingface.co/blog/webgpu-kernels",
    "published_at": "2026-09-01T00:00:00.739Z",
    "primary_tags": [
      "Hugging Face",
      "WebGPU",
      "Local AI"
    ],
    "secondary_tags": [
      "Kernel Contracts",
      "Fleet",
      "Browser Inference"
    ],
    "why_it_matters_cn": "这不只是又一个 local AI demo。更关键的是它把浏览器推理里的 contract、benchmark 和 variant selection 从 runtime 内部拆了出来，后面谁做 WebAI 都能直接继承这层基础设施。",
    "personal_relevance_cn": "做本地推理时，值得对照的不只是几倍加速，而是 kernel contract 是否版本化、correctness case 是否随实现走、以及跨设备证据能不能持续补进来。",
    "product_opportunity_cn": "可以把 op-level contract、硬件回传 benchmark 和版本化 kernel 仓库当成浏览器推理栈的底座，而不是只盯模型量化。",
    "competitive_risk_cn": "性能数字主要来自 Hugging Face 在 Apple M4 上的 op-level 对比，而且明确排除了加载、编译、上传和回传开销；它不是完整模型端到端时延承诺。",
    "recommended_action": "investigate",
    "questions_to_validate": [
      "Fleet 收到更多 GPU / 浏览器结果后，kernel variant selection 会不会公开成更稳定的策略接口？",
      "207 个 kernels 往完整模型端到端推理迁移时，加载、编译和 I/O 开销会吞掉多少收益？",
      "这些 contract 会不会被 ONNX Runtime Web 或其他浏览器 runtime 正式接入，而不是停留在 Hugging Face 生态内？"
    ],
    "follow_up_triggers": [
      "Hugging Face 发布更多 kernel 覆盖、更多设备实测或上游集成结果",
      "浏览器或 runtime 团队开始直接消费这些 versioned kernel artifacts",
      "出现跨设备失败案例或 correctness 回滚机制的公开说明"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 5,
      "technical_or_product_significance": 5,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 5,
      "agent_architecture_value": 2,
      "ai_product_value": 1,
      "macro_value": 1,
      "actionability": 4
    },
    "report_date": "2026-09-02",
    "event_date": "2026-09-01",
    "canonical_url": "https://huggingface.co/blog/webgpu-kernels",
    "first_seen_date": "2026-09-02",
    "last_seen_date": "2026-09-02",
    "run_dates": [
      "2026-09-02"
    ],
    "evidence_boundary": "官方正文确认 207 个 kernel、Hub 仓库结构、JavaScript loader 和 Fleet；速度优势主要是官方自测，且只覆盖通过输出一致性与计时筛选后的对比样本。"
  },
  {
    "id": "2026-09-01-aws-agentcore-payments-trust-gate",
    "demo": false,
    "topic_lane": "agent_architecture",
    "title": "t54 用 AgentCore payments 把 agent 支付拆成硬门：信任评分先过，钱才会动",
    "summary": "AWS 9 月 1 日的 t54 案例不是泛泛讲 agent 支付想象力，而是把控制面摊开：agent 发起交易前，x402-secure 会先对目标 endpoint 和支付地址做实时评分；Amazon Bedrock AgentCore payments 负责 session spending limit、credential isolation 和结算，`ProcessPayment` 返回 status 与完整 audit trail；若评分不过线或 URL 不匹配，付款在代码层直接被挡住，模型本身不能覆写。",
    "decision": "include",
    "confidence": 91,
    "relevance_level": "P2",
    "signal_type": "research",
    "content_type": "technical_update",
    "information_type": "agent_governance",
    "evidence_level": "confirmed",
    "source": "AWS",
    "url": "https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments",
    "published_at": "2026-09-01T07:50:00-08:00",
    "primary_tags": [
      "AgentCore Payments",
      "Agent Commerce",
      "Trust Gate"
    ],
    "secondary_tags": [
      "x402",
      "Spending Limit",
      "Audit Trail"
    ],
    "why_it_matters_cn": "真正让 agent 去付钱时，问题从来不只是有没有钱包，而是谁定额度、谁管密钥、谁拦高风险 endpoint、以及事后能不能把每一笔花费和信任判断串起来。",
    "personal_relevance_cn": "如果在看 agent commerce，最该拆的是 deterministic risk gate、session cap、role separation、audit trail 和失败时 spending limit 是否保持不变。",
    "product_opportunity_cn": "可以把‘先过信任门再结算’做成 agent 支付默认架构，而不是把风控留给 prompt 或人工抽查。",
    "competitive_risk_cn": "20 million transactions、拦截效果和规模都来自 AWS/t54 公开叙述，没有独立审计数据；这也还是单一客户与平台案例。",
    "recommended_action": "monitor",
    "questions_to_validate": [
      "t54 的 trust score 阈值、误拦截率和 endpoint reputation 更新频率会不会公开更多细节？",
      "`ProcessPayment` 的 audit trail 是否能直接满足企业财务或合规团队的对账要求？",
      "session spending limit、wallet provider 和 trust gate 在更多 agent marketplace 或自建工具链里是否还能保持同样的 fail-closed 约束？"
    ],
    "follow_up_triggers": [
      "出现更多 AgentCore payments 生产案例或第三方审计数据",
      "AWS 公布管理员控制、限额策略模板或失败回滚细节",
      "x402 / MCP marketplace 在更广范围内披露采用与风控效果"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 4,
      "technical_or_product_significance": 4,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 5,
      "ai_product_value": 3,
      "macro_value": 1,
      "actionability": 4
    },
    "report_date": "2026-09-02",
    "event_date": "2026-09-01",
    "canonical_url": "https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments",
    "first_seen_date": "2026-09-02",
    "last_seen_date": "2026-09-02",
    "run_dates": [
      "2026-09-02"
    ],
    "evidence_boundary": "官方正文能确认 deterministic trust gate、session-scoped spending ceiling、Secrets Manager / IAM role separation、audit trail 和 MCP marketplace 接入路径；规模与效果指标主要来自厂商自报。",
    "related_sources": [
      {
        "url": "https://aws.amazon.com/blogs/machine-learning/technical-deep-dive-agentcore-payments-and-innovation-in-agentic-commerce/",
        "type": "technical_deep_dive"
      }
    ]
  },
  {
    "id": "2026-08-31-openai-polimill-japan-public-ai-infrastructure",
    "demo": false,
    "topic_lane": "ai_macro",
    "title": "OpenAI / Polimill 给出一个不小的公共部门 AI 落地样本：约 1,050 个自治体、55 万名公职人员在用 QommonsAI",
    "summary": "OpenAI News RSS 可确认这篇 Polimill 客户案例首发于 8 月 31 日；正文称 Polimill 的公共部门产品 QommonsAI 已覆盖日本约 1,050 个自治体和约 55 万名公职人员，当前工作流包括议会答辩、公共服务、社保福利和法律检索，并通过跨自治体的议事录与行政资料标准化来做统一知识底座。文章还写到 Polimill 计划在 2026 年秋季推出 Qommons ONE，但那部分仍是 roadmap，不当作已上线事实。",
    "decision": "include",
    "confidence": 87,
    "relevance_level": "P2",
    "signal_type": "strategic_radar",
    "content_type": "official_release",
    "information_type": "enterprise_adoption",
    "evidence_level": "confirmed",
    "source": "OpenAI",
    "url": "https://openai.com/index/polimill",
    "published_at": "2026-08-31T07:00:00Z",
    "primary_tags": [
      "OpenAI",
      "Polimill",
      "Public Sector AI"
    ],
    "secondary_tags": [
      "Japan",
      "QommonsAI",
      "Enterprise Adoption"
    ],
    "why_it_matters_cn": "这条值得记的不是又一个‘某公司用了 AI’，而是公共部门 vertical AI 已经开始以跨自治体知识底座和统一工作台的形态扩张，规模也不是试点级别了。",
    "personal_relevance_cn": "如果在看行业落地，最该拆的是知识底座怎么做跨机构标准化、管理员能限制哪些模型、审计记录怎么留，以及 roadmap 中的 super agent 什么时候真的落到可见产品面。",
    "product_opportunity_cn": "可以把公共部门或强监管行业里的‘共享知识底座 + 组织策略控模 + 专业工作流代理’视为一个独立产品范式，而不只是通用聊天工具外加提示词。",
    "competitive_risk_cn": "自治体覆盖、公职人员规模和 3-5x 开发提速都来自 OpenAI/Polimill 官方表述；Qommons ONE 和 super agent 仍是计划，不是已上线能力。",
    "recommended_action": "monitor",
    "questions_to_validate": [
      "跨自治体知识底座如何做持续更新、权限隔离和审计留痕？",
      "Qommons ONE 的 super agent 到秋季 rollout 时，真实可见的对象、动作、审批和回滚边界是什么？",
      "公共部门规模采用是否会带动更正式的 procurement、预算和供应链结构变化？"
    ],
    "follow_up_triggers": [
      "Polimill 或 OpenAI 发布 Qommons ONE 的正式上线材料、真实 UI 或管理员文档",
      "出现关于公共部门采用规模、留存或 workflow outcomes 的独立验证",
      "更多国家或地区出现类似跨机构公共 AI 工作台案例"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 4,
      "technical_or_product_significance": 4,
      "strategic_value": 5,
      "source_quality": 4,
      "model_value": 1,
      "agent_architecture_value": 1,
      "ai_product_value": 3,
      "macro_value": 5,
      "actionability": 3
    },
    "report_date": "2026-09-02",
    "event_date": "2026-08-31",
    "canonical_url": "https://openai.com/index/polimill",
    "first_seen_date": "2026-09-02",
    "last_seen_date": "2026-09-02",
    "run_dates": [
      "2026-09-02"
    ],
    "evidence_boundary": "发布日期来自 OpenAI 官方 RSS；正文通过公开文本镜像核验。当前能确认的是现有 QommonsAI 的采用规模、工作流范围和管理控制，不能把秋季 rollout 计划写成已经上线。",
    "related_sources": [
      {
        "url": "https://openai.com/news/rss.xml",
        "type": "official_rss_date"
      }
    ]
  },
  {
    "id": "2026-09-01-github-copilot-billing-org-model-access",
    "demo": false,
    "topic_lane": "ai_product",
    "title": "GitHub Copilot 改了多组织 seat 的模型权限：现在只认付费组织，不再取已启用组织并集",
    "summary": "GitHub 8 月 31 日的官方 Changelog 更新了一个很具体但很实际的 Copilot 规则：如果用户同时在多个组织里持有 Copilot seat，模型可用性现在只由 ‘Usage billed to’ 对应的付费组织决定；此前只要任一组织开了某个模型，用户就能用。若访问完全来自 enterprise 或其组织，这次规则不受影响。",
    "decision": "include",
    "confidence": 89,
    "relevance_level": "P2",
    "signal_type": "competitor",
    "content_type": "official_release",
    "information_type": "product_workflow",
    "evidence_level": "confirmed",
    "source": "GitHub",
    "url": "https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans",
    "published_at": "2026-08-31T14:58:46-07:00",
    "primary_tags": [
      "GitHub Copilot",
      "Model Access",
      "Billing Governance"
    ],
    "secondary_tags": [
      "Multi-org Seats",
      "Usage billed to",
      "Policy"
    ],
    "why_it_matters_cn": "这类改动看起来不像大功能，但它把模型策略、组织治理和结算归属绑到一起了。以后企业里‘能不能选这个模型’更像预算和 policy 的结果，不只是个人偏好。",
    "personal_relevance_cn": "如果在做多组织 AI 产品，最好早点把 feature entitlement、billing owner 和 policy source of truth 统一起来，不然后面一定会出现权限和结算对不上的坑。",
    "product_opportunity_cn": "可把 billing owner 驱动的模型白名单、跨组织 seat 归属可视化和审计解释做成企业 AI 产品的基础能力。",
    "competitive_risk_cn": "这次改动只影响一类多组织 seat 场景；官方正文没有给出管理员 UI、批量迁移工具或对现有审计报表的影响。",
    "recommended_action": "monitor",
    "questions_to_validate": [
      "管理员能否更直观看到 seat 的 billing owner、模型白名单和用户最终生效权限？",
      "跨组织 seat 切换或付费归属调整时，历史审计和可用模型是否会出现短暂不一致？",
      "这套归属逻辑会不会扩展到 code review、cloud agent 或更多执行型 Copilot 能力？"
    ],
    "follow_up_triggers": [
      "GitHub 补充管理员 UI、文档或审计报表截图",
      "更多 Copilot 能力开始显式绑定 billing owner 与 policy source",
      "企业用户公开多组织 seat 的迁移或治理复盘"
    ],
    "scores": {
      "topic_relevance": 5,
      "novelty": 3,
      "technical_or_product_significance": 4,
      "strategic_value": 4,
      "source_quality": 5,
      "model_value": 1,
      "agent_architecture_value": 1,
      "ai_product_value": 5,
      "macro_value": 1,
      "actionability": 4
    },
    "report_date": "2026-09-02",
    "event_date": "2026-09-01",
    "canonical_url": "https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans",
    "first_seen_date": "2026-09-02",
    "last_seen_date": "2026-09-02",
    "run_dates": [
      "2026-09-02"
    ],
    "evidence_boundary": "官方正文确认了新旧规则差异和适用范围；没有额外披露模型策略冲突时的回退逻辑，也没有把这项规则描述成更广泛的自动执行权限升级。"
  }
];
