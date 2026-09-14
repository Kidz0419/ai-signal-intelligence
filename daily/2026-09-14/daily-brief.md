# AI Signal 日报｜2026-09-14

**窗口：** 20:25 增量只核验本轮 3 个 `new_candidates`；当天累计完成 23 个跨轮候选判断。Kimi Release 使用 GitHub API 的真实发布时间；OpenAI Sitemap `lastmod` 只用于发现。
**一句话结论：** 新增 1 条 P1 Agent 架构 Signal。Kimi Code 0.43 把 MCP 工具披露、人工 steering、后台等待、压缩重试和命令确认拆成了可分别配置的运行时控制。[3][5][6]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 没有新模型、价格、开放范围或独立评测 |
| Agent 架构 | 1 | MCP 工具按需披露，人工指令可打断等待但不会取消后台任务 |
| AI 产品 | 0 | Fyxer 是 8 月旧客户案例的页面更新，不是 9 月 14 日产品发布 |
| AI 宏观 | 0 | 没有产业结构、监管、算力或资本变化 |

## 模型｜0 条

OpenAI Codex `0.155.0-alpha.4` 的 GitHub API 时间落在本轮，但它是 prerelease，正文只有版本名，没有功能、工作流、评测或边界说明，不能仅凭版本号进入模型或 Agent 主线。[10]

## Agent 架构｜1 条

### Kimi Code 0.43：工具不必全部常驻，用户插话也不必等后台任务

Kimi Code 0.43.0 是正式版本。它允许每个 MCP server 显式配置 `deferred: true`：只有当模型声明 `dynamically_loaded_tools` 且启用实验性 `tool-select` 时，该 server 的工具才会退出顶层 `tools[]`，由 `select_tools` 按需加载。默认仍是 inline，`disallowedTools` 可以继续否决工具。[3][4][5]

用户控制也更细了。模型等待后台任务时，新的 steering 消息会让 `WaitFor` 返回非错误的 `interrupted`，工具历史保留，后台任务继续运行；同一批其他前台工具仍会完成，再进入下一次模型请求。这个动作是“打断等待”，不是“取消任务”。[3][6]

版本还把 compaction 的最大总尝试次数开放为正整数配置，默认 5；关闭 permission-mode reminder 只移除注入模型上下文的提示，不改变 auto mode 的审批语义。对字面位于 `/tmp` 或 `/temp` 下、且不含通配符、变量、混合目标或 `..` 的 `rm -rf`，危险命令策略可跳过确认。[7][8][9]

**为什么重要：** Agent 控制权不该只剩“自动/手动”一个开关。工具何时暴露、用户能否插话、后台任务是否继续、压缩失败重试多少次、哪些命令免确认，都需要不同的默认值和审计事件。

**建议动作：** 用这五层检查现有 Agent 控制面：记录实际披露和选择的工具、策略否决、steering、wait interrupted、后台任务状态、compaction 尝试及危险命令例外；把暂停、取消和恢复做成独立动作，避免用户把“已打断”等同于“已停止”。

## AI 产品｜0 条

Fyxer 页面这次是 Sitemap 修改，不是新发布。OpenAI 官方 RSS 给出的文章发布时间是 2026-08-13T12:00:00Z；9 月 14 日上传的官方短视频继续讲同一套邮件理解、上下文重排、用户反馈和厂商自报指标，没有形成新的产品上线状态或控制边界。[11][12][13]

## AI 宏观｜0 条

本轮没有新的治理、资本、算力、监管或产业结构变化。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有模型负责人关于模型能力、训练、评测或路线的新原创内容。

## AI 一线实践者观点｜0 条

Fyxer 视频是 3 分多钟的官方客户案例短片，核心材料已出现在 8 月文章中；它不是新的长访谈、失败复盘或独立评测。[12][13]

## 本轮审核但未入选

- OpenAI Codex `0.155.0-alpha.4`：`checked_no_match`。prerelease 正文只有版本名，没有可判断的信息增量。[10]
- Fyxer：`outside_incremental_window_no_material_update`。官方 RSS 把文章日期解析为 8 月 13 日；9 月 14 日视频重复旧客户案例，Sitemap `lastmod` 不能把它改写成今日发布。[11][12][13]

## 当天此前审核但未入选

- `commit-rewriter 0.1` 是 Git 历史清理工具，没有新的 Agent 运行时或产品工作流。[1]
- `shot-scraper 1.12` 只增加 WebP 输出和质量参数，属于普通截图工具维护。[2]
- 早些时候的 18 个 OpenAI Sitemap 观察均是跨轮旧 URL 的 `lastmod` 变化，没有独立发布日期或内容哈希证据，因此没有重复建卡。

## 覆盖与缺口

- 当前机械采集仍有 78 个 `mechanical_failure` 和 2 个 `access_blocked`；本轮新候选通过 GitHub Release/API、Atom、OpenAI 官方 RSS 和官方 YouTube fallback 完成内容判断。
- Kimi 的功能与边界由 Release 和已合并 PR 确认，但 `tool-select` 仍是实验能力；官方没有公开 token、延迟或任务成功率收益。
- Release 没有给出统一运行日志、暂停、回滚或团队级策略 UI，不能从代码合并推断这些产品能力已经存在。
- 本轮只审核 3 个真新增候选，没有重扫 167 条滚动窗口记录，也没有重审 5 条队列记录。

## 证据边界

- Kimi Release API 的 `published_at` 是 2026-09-14T12:03:30Z；Atom 的 12:14:33Z 是 feed 更新时间，未用来覆盖正式发布时间。[3][4]
- Fyxer 直接页面请求触发 Cloudflare 403；正文发现由检索辅助，正式日期与排除判断只依赖成功获取的 OpenAI RSS、官方视频元数据、描述和字幕。[12][13]
- `rm -rf` 免确认只覆盖 PR 明示的字面临时目录目标；没有把它扩写成通用自动授权。[9]

## 飞书短版

**一句话结论：** 3 个真新增候选完成正文核验，新增 1 条 P1 Agent 架构 Signal。

**重点：** Kimi Code 0.43 支持把 MCP server 工具设为 deferred，并让 steering 打断 `WaitFor`；后台任务仍继续，工具策略仍可否决。[5][6]

**判断：** Agent 控制面至少要拆开工具披露、人工打断、后台任务、压缩重试和命令确认，不能只做一个自动模式开关。

**边界：** 动态工具选择仍为实验能力；性能收益、统一日志、暂停和回滚没有公开验证。[3]

**建议动作：** 把这五层及其默认值、覆盖优先级和审计事件加入 Agent 产品验收。

**结果：** previous_count=0，new_count=1，updated_count=0，total_count=1。

## Sources

[1] https://simonwillison.net/2026/Sep/14/commit-rewriter/
[2] https://simonwillison.net/2026/Sep/13/shot-scraper/
[3] https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.43.0
[4] https://github.com/MoonshotAI/kimi-code/releases.atom
[5] https://github.com/MoonshotAI/kimi-code/pull/3667
[6] https://github.com/MoonshotAI/kimi-code/pull/3697
[7] https://github.com/MoonshotAI/kimi-code/pull/3750
[8] https://github.com/MoonshotAI/kimi-code/pull/3728
[9] https://github.com/MoonshotAI/kimi-code/pull/3714
[10] https://github.com/openai/codex/releases/tag/rust-v0.155.0-alpha.4
[11] https://openai.com/index/fyxer
[12] https://openai.com/news/rss.xml
[13] https://www.youtube.com/watch?v=uA5PiAXKGis
