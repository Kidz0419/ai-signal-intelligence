# AI Signal 日报｜2026-09-13

**窗口：** 12:00 增量只核验本轮新增的 2 个候选；当天累计核验 11 个跨轮新增候选。发现窗口截至北京时间 2026-09-13 12:00，正式判断使用正文和 Atom 时间，不把 sitemap `lastmod` 当发布日期。
**一句话结论：** 新增 1 条 P1 Signal。Simon Willison 的长任务实测把 ChatGPT Work 的一个可审计性缺口说清楚了：地图和文件成功交付，实际执行代码却在界面中不可见，线程压缩后也无法取回。[9][10][11]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 本轮没有新模型、价格、开放范围或独立评测 |
| Agent 架构 | 1 | 长任务的上下文压缩不能吞掉代码、工具轨迹和压缩前 transcript |
| AI 产品 | 0 | Two Blind Brothers 仍是同一客户案例，没有产品上线或界面变化 |
| AI 宏观 | 0 | 没有产业结构、监管、算力或资本变化 |

## 模型｜0 条

本轮没有新的模型发布、能力边界、训练方法、定价或独立评测。GPT-6 Astra 只作为被实测的模型出现，不能从一次路线任务外推模型整体能力。[9]

## Agent 架构｜1 条

### ChatGPT Work 完成长任务，却没有留下可取回的执行代码

Simon Willison 给 ChatGPT Work 的 GPT-6 Astra（Max）一个具体任务：根据住址和 OpenStreetMap 数据生成 5K、10K 环线。任务运行 27 分钟后交付了内嵌地图、GPX 和 GeoJSON；作者公开的 HTML 还保留了完整路线几何和 D3 渲染代码。[9][11]

结果能用，过程却断了。ChatGPT 自述使用 Nominatim 定位地址、Overpass 下载道路与步道，再在本地计算环线，但产品界面没有展示实际代码和完整步骤。等作者要求取回 Python 代码时，线程已经压缩，ChatGPT 无法再提供。作者据此主张，采用 compaction 的 LLM 系统应保存压缩前文本，并允许 Agent 的工具调用访问这些记录。[9]

**为什么重要：** 长任务的完成标准不能只有最终文件。模型版本、工具调用、代码、输入来源、中间产物和压缩前 transcript 如果没有独立留存，用户就难以复查、复跑或解释结果是怎么来的。

**建议动作：** 把“不可变执行包”列入 Agent 验收：上下文压缩只改变当前推理窗口，不删除审计存储；每次运行固定保存代码、工具参数、数据来源、产物清单和模型版本，并允许用户导出。

## AI 产品｜0 条

Two Blind Brothers 页面仍在描述视觉理解、语音导航、表格分析和邮箱连接等无障碍用法。正文没有新功能、真实 UI、权限字段、执行日志或量化结果，也没有可核验发布日期；本轮再次变化的只有 sitemap `lastmod`。[2]

## AI 宏观｜0 条

本轮没有新的治理、资本、算力、监管或产业结构变化。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有模型负责人关于模型能力、训练、评测或路线的新原创内容。

## AI 一线实践者观点｜1 条

Simon Willison 的内容达到实践者门槛：有真实任务、明确运行时长、可访问产物和具体失败复盘。证据只支持这一次公开实测，不证明所有 ChatGPT Work 会话都会在压缩后丢失代码，也没有独立验证路线正确性；compaction 的内部实现仍待 OpenAI 文档确认。[9][11]

## 本轮审核但未入选

- Two Blind Brothers：`duplicate_same_day_review_no_material_update`。同一页面第三次因 sitemap 修改进入增量队列，正文仍没有发布日期或达到正式门槛的产品变化。[2]

## 当天此前审核但未入选

- Paul Christiano 任命没有附带治理权力或审批流程变化。[1]
- Claude Code v2.1.270 只是只读 Git 命令误触发权限询问的回归修复。[3]
- Legora 页面是已入库 Astra 事件的旧案例页再次更新 `lastmod`。[4]
- Paul Ford 条目只有一段二手引文，没有可核验的构建或评测增量。[5]
- OpenAI 研究加速报告与 Images 2.5 都是已入库页面再次修改。[6][7]
- California Brown Pelican 与 AI Signal 四条主线无关。[8]

## 证据边界

- Atom feed 给出的精确发布时间是 2026-09-12T23:56:42Z，即北京时间 9 月 13 日 07:56；页面显示的自然日仍是 9 月 12 日，因此事件保留 `event_date=2026-09-12`。[9][10]
- 路线 HTML 能确认交付产物及路线几何存在；执行代码不可见、压缩后无法取回和原因判断来自作者本人，不是 OpenAI 的正式说明。[9][11]
- OpenAI 普通请求对部分页面返回 403；Two Blind Brothers 通过可读正文 fallback 核验，没有把阻断当成无内容。[2]
- 本轮只审核 `new_in_run_count=2` 的候选，没有重扫 329 条滚动窗口记录，也没有重审完整候选队列。

## 飞书短版

**一句话结论：** 12:00 的 2 个真新增候选完成正文核验，新增 1 条 P1 Agent 架构 Signal。
**重点：** ChatGPT Work 用 27 分钟交付了路线地图、GPX 和 GeoJSON，但实际执行代码在 UI 中不可见，线程压缩后也无法取回。[9][11]
**判断：** 长任务 Agent 的交付不能只有最终文件，还要保留代码、工具轨迹、数据来源、模型版本和压缩前 transcript。
**边界：** 这是 Simon Willison 的单次实测；路线正确性和 compaction 内部机制没有独立复现或官方文档。[9]
**建议动作：** 把不可变执行包和压缩前记录导出加入 Agent 产品验收。
**结果：** previous_count=0，new_count=1，updated_count=0，total_count=1。

## Sources

[1] https://openai.com/index/paul-christiano-joins-openai-foundation-board
[2] https://openai.com/index/two-blind-brothers
[3] https://github.com/anthropics/claude-code/releases/tag/v2.1.270
[4] https://openai.com/index/legora-financial-statement-review-with-astra
[5] https://simonwillison.net/2026/Sep/12/paul-ford
[6] https://openai.com/index/research-acceleration-view-inside-openai
[7] https://openai.com/index/introducing-chatgpt-images-2-5
[8] https://simonwillison.net/2026/Sep/12/sighting-399708714
[9] https://simonwillison.net/2026/Sep/12/astra-running-routes
[10] https://simonwillison.net/atom/everything/
[11] https://gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480
