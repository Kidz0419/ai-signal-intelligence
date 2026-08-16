# AI Signal 日报｜2026-08-15

**补抓范围：** 上次成功运行后至 2026-08-17；事件日与报告日分开保存。  
**正式池：** 9 条，其中 include 8、strategic radar/watchlist 1；P0 2、P1 7、P2 0。  
**一句话结论：** 旧任务的 0 条是召回故障；本次从官方 Release、RSS、Sitemap 后续正文和可信报道中恢复了 9 条事件，并保持证据等级和未签署边界。

## 四主线重点

| 主线 | 数量 |
|---|---:|
| 模型 | 2 |
| Agent 架构 | 3 |
| AI 产品 | 3 |
| AI 宏观 | 1 |

## 模型｜2 条

### Anthropic 宣布未来 Claude 模型加入文本水印：采用 SynthID-Text 变体并准备检测 API [2]

Anthropic 宣布未来 Claude 模型生成的文本将加入 SynthID-Text 路线的水印，以履行 EU AI Act 透明度要求，并计划全球上线。水印不增加 token、不携带用户或组织身份；未来将提供检测 API。短文本、事实性段落、轻度校对和代码中的可检测信号较弱，完整重写可以移除水印。

**证据边界：** 发布日期来自官方页面日期；页面未给精确时区。质量无影响来自 Anthropic 内测及其引用研究，仍需独立检验。

### Google 开源 HEIR 编译器：把预训练模型转换为同态加密推理，并公开四类示例源码 [9]

Google 展示 HEIR（Homomorphic Encryption Intermediate Representation）开源编译器，可把在明文输入上运行的预训练模型转换为处理加密输入的推理程序。官方公开推荐、信用卡欺诈检测、加密流量异常检测和热词检测四类示例及源码，当前单线程 CPU 可运行，并与多家同态加密硬件团队合作。

**证据边界：** 官方确认开源编译器、合作方、四个示例和源码；未宣称已经普遍生产可用。

## Agent 架构｜3 条

### OpenAI Agents SDK v0.21：加入无供应商请求的确定性测试，并加固中断快照、递归审批与 MCP 生命周期 [1]

OpenAI Agents SDK v0.21 新增 agents.testing、realtime.testing 和 voice.testing，可在不调用模型供应商的情况下确定性测试 Agent、Sandbox、Realtime 与 Voice 工作流；同时加固 RunState 中断快照、递归 agent-tool 审批、max-turn 收尾、流清理、敏感错误脱敏、MCP 生命周期快照隔离和重试上限。

**证据边界：** 内容来自官方 Release 与变更 PR；版本说明明确称没有已知破坏性 SDK 行为变化。

### AWS 连续公开三套生产 Agent 架构：网络层最小权限、共享文件交接与跨模型可观测 [3]

AWS 三篇官方实作分别展示：用 VPC Lattice 对 Agent→私有数据请求执行 IAM/SigV4、HTTP 方法级限制和访问日志；用 S3 Files POSIX 目录作为多 Agent 持久工作记忆与交接层，并用 access point 隔离；在 AgentCore 中路由 Bedrock 与 SageMaker OpenAI-compatible 模型，并补齐后者默认缺失的 token 级 OpenTelemetry。

**证据边界：** 三篇均为 AWS 官方技术实作并附架构/代码；它们是参考实现，不是生产效果或合规认证。

### Claude Code v2.1.233 加固企业 Runtime：用户身份透传、Bash 内存上限与权限等待恢复 [4]

Claude Code v2.1.233 增加可选 forward_user_identity，让 Apps Gateway 后方代理按用户归因支出；Linux Bash 工具可配置 memory cgroup 限额；修复云会话等待权限提示时被误判丢失、MCP v2 长连接反复重开和桌面/VS Code 权限通知 hook 不触发等问题。

**证据边界：** 官方 Release 明确列出新增项和修复项；未公开相关故障率或生产改善幅度。

## AI 产品｜3 条

### ChatGPT 8 月 14 日批次：交互测验、项目记忆切换、个性化建议与 Linux 公测 [6]

OpenAI Release Notes 的 8 月 14 日批次加入对话内交互测验、已有项目在 default/project-only memory 间切换、基于会话历史与连接工具的首页建议、Free/Go 网页手动 Think，以及 ChatGPT/Codex Linux 桌面应用公开预览。Linux 版可执行浏览器动作，但尚不能控制其他桌面应用。

**证据边界：** 官方正文确认功能与适用范围；条目仅标 August 14, 2026，无精确发布时间，文章级 updatedAt 不能当条目发布时间。

### GitHub Copilot 引入 Grok 4.6：覆盖 IDE、CLI 与云端 Agent，企业默认关闭并按量计费 [7]

GitHub 开始向 Copilot Pro、Pro+、Max、Business 和 Enterprise 渐进开放 xAI Grok 4.6，覆盖 VS Code、Visual Studio、JetBrains、Xcode、Eclipse、Copilot CLI、cloud agent 与 Copilot app。Business/Enterprise 管理员必须显式开启 Grok 4.6 policy，策略默认关闭，使用量按模型供应商价格计费。

**证据边界：** 官方确认开放范围、入口、组织策略和计费；未提供独立编码评测，也未扩大现有自动执行权限。

### Kimi Code 0.36.1 重做多 Agent 控制面：Swarm 独立开关、子任务状态过滤与后台 Bash 可审计 [8]

Kimi Code 0.36.1 将 Swarm 从 plan/goal 模式中拆成独立工具栏开关，重做子 Agent 卡片与状态过滤；后台 Bash 面板可按状态筛选并查看命令和输出。版本还修复第二次审批提示导致会话挂起、工具结果错序、MCP OAuth 取消后等待超时、运行中 fork 产生部分状态等问题。

**证据边界：** 官方 Release 和对应 PR 可核验；这不是 Kimi 基础模型或 Agent Swarm 新发布。

## AI 宏观｜1 条

### 美国据报拟要求 35 个 AI 合作伙伴在 Pax Silica 与中国框架之间选边 [5]

Reuters 审阅的美国国务院内部草案拟告知 35 个 AI Opportunity Statement 签署方：若同时加入中国的竞争性 AI 合作框架，可能被排除在美国主导联盟之外。Pax Silica 涵盖 AI 模型、半导体、关键矿产、联合投资与出口控制，哈萨克斯坦目前被报道为唯一同时参与双方的国家。

**证据边界：** 可信媒体获得内部草案与官员说法，但不是公开监管文件，也尚未发送或生效。

## 模型大厂高管模型长文 / 访谈

本次没有把高管泛观点纳入；Dario Amodei 关于行业信任的发言因不以模型能力、训练、评测或路线为主而排除。

## AI 一线实践者观点

本次优先恢复正式发布与可复现架构；没有将搜索摘要或普通论坛帖子升级为实践者正式卡。

## 排除与延后

- OpenAI Sitemap 中 FedRAMP、Rosalind、Sora 等为旧页面近期 lastmod，按真实发布日期排除。
- HF State of Open Models 发布于北京时间 8 月 14 日 08:00，早于恢复窗口。
- Anthropic 多 Agent 研究发布于 8 月 13 日，早于恢复窗口。
- Codex 0.148 alpha Release 只有标签、无变更正文，不升正式卡。
- Dario Amodei 的信任危机发言不以模型本身为主题，按高管边界排除。

## 证据边界

- `confirmed` 均已打开官方正文、Release 或代码；RSS/Sitemap 仅用于发现和日期核验。
- `reported` 项保留为 strategic radar；草案、谈判和拟投资均未写成已签署或已生效。
- 同一事件跨平台转载已合并；Codex alpha 空 Release、普通补丁和旧页面 lastmod 未进入正式池。

## 来源

[1] https://github.com/openai/openai-agents-python/releases/tag/v0.21.0
[2] https://www.anthropic.com/news/claude-text-watermark
[3] https://aws.amazon.com/blogs/networking-and-content-delivery/zero-trust-networking-for-agentic-ai-with-amazon-vpc-lattice/
[4] https://github.com/anthropics/claude-code/releases/tag/v2.1.233
[5] https://www.cnbc.com/2026/08/15/us-to-tell-allies-they-must-pick-sides-in-ai-race-with-china-reuters.html
[6] https://help.openai.com/en/articles/6825453-chatgpt-release-notes
[7] https://github.blog/changelog/2026-08-14-grok-4-6-is-now-available-in-github-copilot/
[8] https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.36.1
[9] https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/
