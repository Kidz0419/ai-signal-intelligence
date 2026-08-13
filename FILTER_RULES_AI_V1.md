# AI Signal Intelligence Filter V1

**适用对象：** 连连支付创新产品、战略与研究团队  
**目标：** 围绕用户的四条核心关注主线，建立高精度、可持续的 AI 情报日报：模型、Agent 架构、AI 产品、AI 宏观发展。筛选重点是重大能力变化、架构演进、真实产品工作流和会改变产业格局的宏观事件，而不是泛 AI 新闻聚合。

## 1. 四条一级主线

### 1.1 模型（Model）

关注基础模型与重要专用模型的实质变化，包括：

- 新模型、重要版本和模型系列路线变化
- 预训练、后训练、推理、Scaling、对齐与安全
- 上下文、记忆、多模态、工具使用和计算机操作能力
- 模型架构、开放权重、许可、部署、价格和推理效率
- 真实能力边界、独立评测及重大研究突破

只有跑分、参数或主观体验而无法说明能力、成本、部署或产品边界的内容，不作为重点信号。

### 1.2 Agent 架构（Agent Architecture）

关注 Agent 从模型走向可靠执行系统所需的架构层：

- Planning、Reasoning、Reflection、Memory 和 Context Engineering
- Tool Use、MCP、A2A、多 Agent 协作和模型路由
- Runtime、状态管理、长任务、任务恢复和失败回退
- 权限、授权、审批、沙箱、身份、策略和人工接管
- Evals、Observability、Tracing、日志、回滚、安全与治理
- Agent 开发框架、SDK、协议和企业级控制面

普通 Agent 应用发布若没有新的架构、交互或执行机制，不进入架构主线。

### 1.3 AI 产品（AI Product）

关注已经改变真实用户操作或企业工作流的 AI 产品：

- 头部 AI 原生产品和平台的重要功能、界面与交互变化
- Agent 产品的操作对象、动作、审批与自动执行边界
- 企业采用、真实用户案例、商业模式、定价与分发变化
- 垂直专业产品及其人机协作、责任和失败边界
- 登录后导航、页面模块、字段、按钮、执行日志和回滚

必须尽量核验帮助中心、Release Notes、开发文档、官方演示或真实产品 UI；营销插画和资源包文案不能直接视为已上线功能。

### 1.4 AI 宏观发展（AI Macro）

关注足以改变 AI 产业方向、供给结构、竞争格局或采用速度的宏观事件：

- 模型公司、云平台、芯片与算力基础设施的战略变化
- 重大资本开支、并购、融资或合作，但必须改变行业结构而非普通交易新闻
- 算力供给、芯片路线、能源、数据中心和推理成本变化
- 开源与闭源格局、开发者生态和分发入口变化
- 监管、版权、数据、国家政策、标准和安全治理
- 企业 AI 采购、组织采用、劳动力与商业模式的结构性变化
- 模型大厂之间的竞争位置、平台控制权和产业链角色变化

宏观信号不要求落到单一产品功能，但必须回答“改变了什么结构、影响哪些参与者、后续用什么指标验证”。普通融资、股价波动、泛趋势评论和没有结构性影响的合作不收录。

## 2. 双层情报

1. **AI Core Signal**：四条主线中已有可信证据、发生实质变化的模型、架构、产品或宏观事件。
2. **Strategic Radar**：尚未完全落地，但可能改变技术路线、产品入口、执行边界、采购逻辑、监管要求或产业竞争格局的前置信号。

> 一条信息如果既不能解释模型/Agent/产品发生了什么变化，也不能解释 AI 产业结构将如何变化，就不进入重点信号。

## 3. 模型大厂高管长文与访谈

允许收录模型大厂关键高管、模型负责人或核心研究负责人的长文、访谈、演讲和公开发言，但必须同时满足以下边界：

1. **主体边界**：仅限主要模型公司及其模型业务关键负责人，例如 OpenAI、Anthropic、Google DeepMind、Meta、xAI、Microsoft AI、Amazon AGI、Apple Foundation Models，以及具有重要基础模型影响力的中国模型公司。普通科技公司、支付公司、SaaS 公司和应用公司的高管不因讨论 AI 而自动纳入。
2. **主题边界**：内容必须主要讨论模型本身，包括模型能力、训练方法、推理、Scaling、后训练、对齐、安全、评测、成本、上下文、多模态、工具使用、模型架构、开源策略或模型路线图。
3. **排除泛观点**：仅谈“AI 改变世界”、公司管理、宏观产业、融资估值、个人经历或一般产品营销，不收录。
4. **新信息要求**：必须包含新的事实、具体判断、技术解释、能力边界、路线变化、时间表或值得长期引用的模型框架；重复既有观点不收录。
5. **证据表达**：原始长文、官方访谈、完整演讲或可核验逐字稿标记为 `primary_statement`；媒体转述标记为 `reported`。高管判断不等于模型已经发布或能力已经得到独立验证。
6. **默认分流**：有正式模型发布或技术材料佐证时可进入 `core / P1`；只有高价值路线判断时进入 `research` 或 `strategic_radar / P2`；重大路线转向可提升优先级。

## 4. 默认排除

- 只有模型跑分、参数规模或主观体验，无法对应产品能力变化
- 套壳工具、无真实 UI/文档/用户证据的“AI 产品发布”
- 非模型大厂高管的泛 AI 长文、访谈、播客或营销观点
- 模型大厂高管谈组织管理、融资、宏观产业或一般产品营销，但没有模型层新信息
- 单纯融资、股价、人物八卦和营销表态
- 无新增事实的趋势文章、转载和内容农场
- 与产品经理决策无关的纯学术增量；重大能力突破除外

## 5. 栏目

`signal_type`：`core`、`strategic_radar`、`competitor`、`regulation`、`research`  
`content_type`：`official_release`、`technical_update`、`executive_statement`、`media_report`、`analysis`、`regulatory`  
`topic_lane`：`model`、`agent_architecture`、`ai_product`、`ai_macro`  
`information_type`：`model_capability`、`model_release`、`model_research`、`agent_architecture`、`agent_runtime`、`agent_governance`、`agent_product`、`developer_ecosystem`、`enterprise_adoption`、`product_workflow`、`compute_infrastructure`、`industry_structure`、`regulation_policy`、`company_strategy`、`research_insight`

## 6. 证据等级

- `confirmed`：官方产品页、帮助中心、开发文档、代码、监管文件或可实际访问的产品
- `primary_statement`：具名负责人一手表态，不等于已上线
- `reported`：可信媒体报道，尚待一手材料确认
- `inferred`：从招聘、代码或生态痕迹推断
- `speculative`：预测或传闻；默认不推送

## 7. 十项评分（0–5）

基础五项：`topic_relevance`、`novelty`、`technical_or_product_significance`、`strategic_value`、`source_quality`。

用户价值五项：`model_value`、`agent_architecture_value`、`ai_product_value`、`macro_value`、`actionability`。

四条主线分别评分，不要求每条信号四项都高。至少一个主线价值应达到 4；宏观信号可以 `product_impact` 较低，但 `macro_value` 与 `strategic_value` 必须高。

## 8. 优先级

- **P0**：头部平台或关键基础设施出现立即影响产品路线、风险或竞争位置的变化
- **P1**：值得进入当日日报并启动调研的正式产品、技术、采用或治理信号
- **P2**：值得持续追踪的早期方向、媒体报道或研究
- **P3**：归档，不主动推送

关键词只负责召回；最终纳入必须基于正文、证据等级和产品影响判断。允许静默日为 0 条，不为凑数降低标准。

## 9. 每条入库记录必须回答

- 发生了什么，以及证据边界
- 为什么重要
- 对模型、Agent 架构、AI 产品或宏观格局有什么影响
- 产品机会与竞争风险
- 建议行动
- 待验证问题与后续触发器
