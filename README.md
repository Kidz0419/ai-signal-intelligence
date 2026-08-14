# AI Signal Intelligence

个人使用的 AI 产品与 Agent 情报知识库，覆盖模型、Agent 架构、AI 产品和 AI 宏观发展。

> 本项目为个人独立信息工具，不代表任何公司或机构；内容仅用于个人研究与产品判断。

- `FILTER_RULES_AI_V1.md`：筛选口径
- `daily/YYYY-MM-DD/`：不可变日报产物
- `data/history.json`：跨日去重事件库
- `backfills/YYYY-MM-DD_to_YYYY-MM-DD/`：人物观点等历史回溯产物（与当日日报分离）
- `backfill-2026-07-13-to-2026-08-13.html`：近一个月人物信源审计与回溯页面
- `config/person-source-registry.json`：人物原创信源注册表及覆盖缺口
- `config/signal-source-registry.json`：模型、Agent、AI 产品、宏观、研究与人物长内容的 107 个召回入口
- `backfills/2026-07-16_to_2026-08-14_all_signals/`：最近 30 天四主线正式 Signal、增补数据与信源覆盖审计
- `monthly-signal-2026-07-16-to-2026-08-14.html`：最近 30 天全量回溯浏览页；正式 Signal、日期候选和抓取失败分开统计
- `content-topics/YYYY-MM-DD/topics.json`：从当日 Signal 派生的跨平台选题候选
- `CONTENT_TOPIC_RULES_V1.md`：小红书、X / Twitter、公众号选题与证据规则
- `content-topic-studio.html`：自媒体选题工作台
- `index.html`：Notion 风格浏览界面

## 在线访问

GitHub Pages：https://kidz0419.github.io/ai-signal-intelligence/

## 本地运行

运行 `python3 -m http.server 8766`，打开 `http://127.0.0.1:8766/`。
