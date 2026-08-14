#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPE = "monthly-2026-07-16_to_2026-08-14"
OUT = ROOT / "content-topics" / SCOPE / "topics.json"
SIGNALS_PATH = ROOT / "backfills/2026-07-16_to_2026-08-14_all_signals/selected.json"
DAILY_TOPICS = ROOT / "content-topics/2026-08-14/topics.json"


def platform(title, hook, outline, kind, visual, cta):
    formats = {
        "xiaohongshu": "7—9 页图文卡",
        "twitter": "6—8 帖 Thread",
        "wechat": "2000—3000 字深度文章",
    }
    return {"title": title, "hook": hook, "format": formats[kind], "outline": outline, "visual_direction": visual, "cta": cta}


def topic(id, signal_id, lane, priority, title, tension, why, audience, boundary, xhs, tw, wx):
    return {
        "id": id,
        "status": "candidate",
        "timeliness": "this_month",
        "priority": priority,
        "topic_lane": lane,
        "source_signal_ids": [signal_id],
        "working_title_cn": title,
        "core_tension_cn": tension,
        "why_now_cn": why,
        "target_audience_cn": audience,
        "evidence_boundary_cn": boundary,
        "source_urls": [],
        "platforms": {"xiaohongshu": xhs, "twitter": tw, "wechat": wx},
    }


def new_topic(id, signal_id, lane, priority, title, tension, why, boundary, xhs_title, xhs_hook, tw_title, tw_hook, wx_title, wx_hook, outline_cn, outline_en, visual):
    return topic(
        id, signal_id, lane, priority, title, tension, why,
        ["AI 产品经理", "Agent/模型工程师", "AI 产业研究者"], boundary,
        platform(xhs_title, xhs_hook, outline_cn, "xiaohongshu", visual, "评论区说说你最想验证哪一项"),
        platform(tw_title, tw_hook, outline_en, "twitter", visual, "What would you verify first?"),
        platform(wx_title, wx_hook, outline_cn + ["落地验证清单与后续观察指标"], "wechat", visual, "附事实边界与验证清单"),
    )


def main():
    signals = {x["id"]: x for x in json.loads(SIGNALS_PATH.read_text())}
    daily = json.loads(DAILY_TOPICS.read_text())["topics"]
    topics = []
    for original in daily:
        item = copy.deepcopy(original)
        item["timeliness"] = "this_month" if item["timeliness"] != "evergreen" else "evergreen"
        item["source_urls"] = [signals[sid].get("canonical_url") or signals[sid]["url"] for sid in item["source_signal_ids"]]
        topics.append(item)

    topics.extend([
        topic(
            "2026-07-28-managed-agent-runtime-control-plane",
            "2026-07-28-google-gemini-managed-agents-hooks-budget-triggers",
            "agent_architecture", "A",
            "生产 Agent 的控制面正在收敛：工具 Hooks、预算熔断、状态恢复和定时执行必须一起设计",
            "Agent 越能自主执行，越需要在同一 Runtime 中同时控制工具、预算、状态和生命周期，而不是靠提示词提醒它小心。",
            "Google Managed Agents 已把工具前后 Hooks、Token 上限、暂停续跑、Cron Trigger 和 Sandbox 清理放进公开 API。",
            ["Agent 产品经理", "AI 平台工程师", "企业自动化负责人"],
            "接口与示例来自 Google 官方；生产效果、Hook 绕过、Sandbox 隔离和任务恢复可靠性尚无独立数据。",
            platform("别再只给 Agent 加审批：真正的控制面至少要有这 5 层", "一个 Agent 能定时运行、写文件、装包和调用网页工具后，‘遇到危险再问我’已经不够。", ["托管 Agent 能做什么", "工具调用前后 Hooks", "预算耗尽如何暂停", "为什么要保留环境续跑", "Cron 与 Sandbox 生命周期", "一张生产控制面清单"], "xiaohongshu", "Hooks—预算—状态—触发—环境五层卡片", "你的 Agent 现在缺哪一层？"),
            platform("A production agent control plane needs hooks, budgets, resumability, scheduling, and environment lifecycle", "Gemini Managed Agents is a useful signal: autonomy controls are becoming runtime primitives, not prompt conventions.", ["confirmed API changes", "pre/post tool hooks", "budget stop and resume", "persistent scheduled environments", "missing security evidence", "control-plane checklist"], "twitter", "runtime control-plane stack", "Which control should be mandatory by default?"),
            platform("从工具拦截到预算续跑：生产 Agent 控制面正在形成", "当 Agent 从一次性问答变成长期运行的工作进程，工具权限、预算、状态恢复、定时触发和环境销毁就必须成为统一的产品对象。", ["Managed Agents 更新了什么", "工具 Hook 的决策位置", "预算熔断与恢复语义", "Cron 任务为何需要持久环境", "日志、审批和回滚缺口", "生产 Agent 控制面字段建议"], "wechat", "Agent Runtime 分层图与状态机", "附生产 Agent 控制面验收表"),
        ),
        topic(
            "2026-07-30-browser-agent-sensitive-action-handoff",
            "2026-07-30-google-gemini-spark-chrome-auto-browse",
            "ai_product", "A",
            "浏览器 Agent 的关键不是能不能自动点，而是什么时候必须把任务交还用户",
            "使用登录态与保存密码能显著提升任务完成率，也把支付、预订、取消和凭据授权变成不可回避的责任边界。",
            "Gemini Spark 已公开 Chrome auto browse 工作流，并明确支付等敏感动作交还用户。",
            ["AI 产品经理", "Agentic Commerce 研究者", "浏览器自动化团队"],
            "Google 官方确认工作流和美国首发；敏感动作分类、Prompt Injection 测试、取消回滚和误操作率未披露。",
            platform("AI 能用你的登录态订机票了，但到付款前应该发生什么？", "最值得拆解的不是自动浏览，而是 Google 明确让支付等敏感动作回到用户手里。", ["它能自动做到哪一步", "登录态和保存密码意味着什么", "支付为什么必须交还", "预订与取消的责任链", "Prompt Injection 风险", "敏感动作分级表"], "xiaohongshu", "自动执行路径与红色交还节点", "你认为哪些动作必须人工确认？"),
            platform("The key browser-agent primitive is not auto-clicking. It is sensitive-action handoff.", "Gemini Spark can use logged-in accounts for web errands, but hands payments back to the user. That boundary is the product.", ["confirmed workflow", "credentialed browsing", "payment handoff", "other sensitive actions", "injection and rollback gaps", "a risk-tier model"], "twitter", "action-risk ladder", "Where should autonomous browsing stop?"),
            platform("从自动浏览到支付交还：浏览器 Agent 的最小授权合同", "浏览器 Agent 一旦能使用登录态和保存密码，产品问题就从‘能不能完成任务’转向‘哪些动作可以代表用户完成’。", ["Spark 的真实操作链路", "登录态授权的范围", "支付交还为何是关键边界", "预订、取消和退款怎么办", "Prompt Injection 与凭据风险", "浏览器 Agent 最小授权合同"], "wechat", "对象—动作—风险—确认矩阵", "附敏感动作分级模板"),
        ),
        topic(
            "2026-08-12-connected-apps-transaction-layer",
            "2026-08-12-google-gemini-connected-apps-actions",
            "ai_product", "A",
            "通用助手正在变成跨服务交易入口，但连接数量不等于可托付程度",
            "从会议总结到网站编辑、租车、餐厅、票务和就医预约，助手开始触达真实交易；真正的壁垒是确认、支付、取消、退款和审计。",
            "Google 已宣布未来数周滚动开放一批 Gemini Connected Apps，动作范围跨生产力、出行、娱乐、家居和医疗。",
            ["AI 产品经理", "平台生态负责人", "Agentic Commerce 从业者"],
            "属于已宣布滚动开放，不是所有用户已上线；官方未披露逐动作确认、支付、退款、取消和日志机制。",
            platform("Gemini 一口气接入租车、餐厅、票务和看医生：但我只关心这 6 个按钮", "连接服务越来越多并不等于 Agent 更可信，关键是用户在提交、支付和取消前能看见什么。", ["新接入了哪些服务", "从查询到交易的变化", "确认页应该显示什么", "支付与退款边界", "失败如何恢复", "连接器验收清单"], "xiaohongshu", "服务地图与交易漏斗", "哪类服务你最不愿交给 AI？"),
            platform("Connected apps turn assistants into transaction routers", "Gemini is moving from summarizing information to editing sites, booking services, renting cars, finding tickets, and scheduling doctors.", ["announced connections", "action surface", "confirmation contract", "payment/cancellation gaps", "auditability", "platform implications"], "twitter", "assistant-to-transaction map", "Connections are distribution; trust controls are the moat."),
            platform("从连接应用到交易编排：通用 AI 助手的下一层竞争", "当助手能够跨服务执行预约和交易，连接器不再只是数据检索接口，而是承载授权、确认、责任和售后的执行层。", ["Connected Apps 的动作范围", "连接数量为何不是核心指标", "确认与支付的产品对象", "取消退款和异常恢复", "平台生态与分发优势", "交易型 Agent 的评测框架"], "wechat", "跨服务交易编排架构图", "附连接器风险审计字段"),
        ),
        topic(
            "2026-07-27-programmatic-tool-calling-governance",
            "2026-07-27-openai-agents-sdk-programmatic-tool-calling",
            "agent_architecture", "B",
            "当模型开始写 JavaScript 编排工具，审批边界必须从单次调用升级到程序级",
            "程序化工具编排能减少模型往返，却让一次生成的代码串联多个动作；逐工具白名单、审批、Guardrail 和运行状态必须共同约束。",
            "OpenAI Agents SDK 已加入 Programmatic Tool Calling，并接入 allowed_callers、approvals、sessions 与 RunState。",
            ["Agent 工程师", "安全产品经理", "开发者工具团队"],
            "官方 SDK Release Notes 证明接口存在；支持模型范围、复杂流程成功率、沙箱安全和成本未公开。",
            platform("AI 不再一次调一个工具，而是直接写脚本串起来：审批该怎么做？", "工具调用从一颗按钮变成一段程序后，只问‘允许这次调用吗’可能已经太晚。", ["什么是程序化工具调用", "为什么模型往返更少", "allowed callers 的作用", "审批应该放在哪", "状态与回滚", "程序级权限检查表"], "xiaohongshu", "单次调用与程序编排对比", "你会允许 Agent 一次编排多少个动作？"),
            platform("Programmatic tool calling changes the unit of approval", "If a model writes JavaScript to coordinate tools, governance cannot stop at approving one function call at a time.", ["SDK change", "allowed callers", "approval granularity", "state and guardrails", "sandbox gap", "evaluation questions"], "twitter", "call-level vs program-level approval", "The unit of autonomy is becoming a program."),
            platform("模型开始编排工具程序后，Agent 的授权单位也要改变", "程序化调用可以提升多工具工作流效率，但它同时把风险从一个函数调用扩展到一段可组合执行逻辑。", ["Programmatic Tool Calling 机制", "性能收益来自哪里", "工具白名单与调用者约束", "审批粒度如何变化", "状态、日志和回滚", "程序级治理框架"], "wechat", "程序执行图与治理节点", "附程序级审批设计问题"),
        ),
        topic(
            "2026-08-13-durable-agent-approval-state",
            "2026-08-13-microsoft-agent-framework-checkpoint-approval-hooks",
            "agent_architecture", "B",
            "长任务 Agent 的审批不是一个弹窗，而是一段必须持久化的状态",
            "Checkpoint、恢复、函数审批和会话释放若分散在不同层，重启后可能丢失谁批准了什么；可靠 Agent 需要把它们放进统一状态机。",
            "Microsoft Agent Framework 已把 Workflow checkpoint/resume、Approval state store、取消释放和实验 Hooks 放入同一版本。",
            ["Agent 平台团队", "企业架构师", "治理产品经理"],
            "官方 Release Notes 未给出审批角色、撤销语义、Exactly-once 恢复、状态加密和生产指标；Hooks 仍为实验功能。",
            platform("Agent 跑到一半重启了：刚才的审批还算数吗？", "很多产品把审批做成弹窗，却没有定义任务恢复后审批状态如何继承、撤销或过期。", ["长任务为什么要 checkpoint", "审批状态要存什么", "恢复后的 Exactly-once 问题", "取消如何释放资源", "Hooks 能做什么", "状态机字段"], "xiaohongshu", "审批状态机和恢复分支", "你遇到过恢复后重复执行吗？"),
            platform("Approval is durable workflow state, not a modal", "Microsoft Agent Framework now puts checkpoints, resume, function-approval stores, hooks, and session release into the same runtime surface.", ["release facts", "durable approvals", "resume semantics", "cancellation", "experimental hooks", "open questions"], "twitter", "durable approval state machine", "Can your agent prove what remains approved after a restart?"),
            platform("把审批写进状态机：长任务 Agent 如何安全恢复", "当 Agent 可以跨小时运行并在故障后恢复，审批必须成为可持久化、可过期、可撤销和可审计的工作流状态。", ["为什么审批弹窗不够", "Checkpoint 与审批的关系", "恢复与重复执行", "取消和资源释放", "Hook 策略层", "持久化审批数据模型"], "wechat", "长任务恢复与审批状态机", "附 Durable Approval Schema"),
        ),
        topic(
            "2026-08-13-agent-context-cost-ui",
            "2026-08-13-openhands-agent-canvas-context-cost-automation-controls",
            "ai_product", "A",
            "Agent 产品终于开始把上下文、成本和自动化状态做成可见 UI",
            "上下文窗口、单次成本、子任务和自动化准备度过去藏在日志里；把它们做成用户可见控件，才可能形成可管理的 Agent 工作台。",
            "OpenHands Agent Canvas 连续版本加入上下文用量与手动压缩、单次运行成本、Activity Log 导出、子会话和 readiness gate。",
            ["AI 产品经理", "Coding Agent 用户", "Agent 工作台设计师"],
            "Release Notes 证明功能进入版本；本地与托管版差异、压缩损失、Gate 误判和成本口径尚未实测。",
            platform("AI Agent 的成本和上下文终于不再是黑盒：这 5 个 UI 值得抄", "比再加一个聊天框更重要的，是让用户看见上下文快满了、这次花了多少、任务是否准备好。", ["新增了哪些控件", "上下文用量表", "手动压缩", "成本日志", "子会话和准备度 Gate", "Agent 工作台信息架构"], "xiaohongshu", "Notion 风 Agent 控制台拆解", "你最需要哪个可见指标？"),
            platform("Agent UX is moving from chat to operational controls", "OpenHands now exposes context usage, manual compaction, per-run cost, activity exports, child conversations, and issue readiness gates.", ["product changes", "context as a visible resource", "cost transparency", "subtask controls", "readiness gates", "UX implications"], "twitter", "chat UI vs operations UI", "The next agent interface is an operations console."),
            platform("对话框之外：Agent 工作台为什么必须显示上下文、成本与任务状态", "Agent 产品成熟的标志不是消息气泡更多，而是把不可见的运行资源和风险转化为可理解、可操作、可追踪的界面对象。", ["OpenHands 的连续更新", "上下文预算的产品化", "成本与 Activity Log", "子会话和任务分解", "Readiness Gate 的价值与误判", "Agent 工作台设计清单"], "wechat", "Agent 工作台信息架构图", "附运行控制 UI 字段表"),
        ),
        topic(
            "2026-07-22-ai-demand-scale-supply-constraint",
            "2026-07-22-alphabet-q2-ai-demand-supply-enterprise-adoption",
            "ai_macro", "A",
            "AI 企业采用不能只看席位数：Token 消耗、Backlog 和供给约束正在成为更真实的结构指标",
            "近 90% Fortune 100 的覆盖很亮眼，但真正说明产业结构的是企业 Token 深度、云 Backlog、基础设施供给与成本效率是否同步变化。",
            "Alphabet Q2 同时披露 Cloud 增长、5140 亿美元 Backlog、220 亿 tokens/分钟和持续供给受限。",
            ["AI 战略研究者", "企业产品负责人", "投资与产业观察者"],
            "全部指标为 Alphabet 自报，口径与其他厂商不可直接横比；未披露 AI 单独收入、缓存拆分和付费活跃定义。",
            platform("别再只看‘多少家公司用了AI’：这 4 个指标更接近真实采用", "席位覆盖可以很高，但企业是否真正把 AI 跑进生产，要看 Token 深度、订单、供给和续用。", ["为什么席位数不够", "tokens/分钟", "Cloud Backlog", "企业使用深度", "供给约束", "采用指标仪表盘"], "xiaohongshu", "企业采用四指标雷达图", "你最信哪个采用指标？"),
            platform("Enterprise AI adoption needs depth metrics, not logo counts", "Alphabet reported 22B model tokens/min, a $514B Cloud backlog, nearly 90% Fortune 100 Gemini Enterprise usage, and continued supply constraints.", ["reported metrics", "breadth vs depth", "token intensity", "backlog", "supply constraints", "comparability limits"], "twitter", "adoption depth metric stack", "Usage breadth is marketing; workload depth is strategy."),
            platform("从客户 Logo 到 Token 深度：怎样判断企业 AI 是否真的进入生产", "企业采用不能只看签约数量或 Fortune 100 覆盖率。Token 消耗、订单积压、供给约束和现有客户超额使用，才更接近生产化深度。", ["Alphabet Q2 的一手数据", "覆盖率与深度的区别", "Token 指标的局限", "Backlog 与算力供给", "跨厂商口径陷阱", "企业 AI 采用仪表盘"], "wechat", "企业采用指标树", "附采用深度指标模板"),
        ),
        topic(
            "2026-08-02-eu-ai-content-transparency-workflow",
            "2026-08-02-eu-ai-act-article-50-transparency-obligations",
            "ai_macro", "A",
            "AI 内容标识从产品自觉变成流程义务：谁负责标记、检测和发布前确认？",
            "欧盟透明度义务同时约束提供者和部署者，意味着水印不是模型端一个字段，而是贯穿生成、编辑、发布和审计的工作流。",
            "AI Act 第 50 条义务已于 8 月 2 日适用，配套 Code 可作为自愿合规证明工具。",
            ["AI 产品经理", "内容平台团队", "合规与品牌负责人"],
            "Code 自愿但法定义务不自愿；具体技术阈值、执法和各成员国实践仍待后续指南与案例。",
            platform("AI生成内容必须标识后，产品里到底要多哪几个步骤？", "水印不是导出时加个角标。真正麻烦的是生成后被编辑、跨平台转发和再次加工。", ["新义务覆盖谁", "模型提供者做什么", "内容部署者做什么", "编辑后如何保留标识", "深伪和文本标签", "产品流程检查表"], "xiaohongshu", "生成—编辑—发布—审计流程", "你的产品在哪一步会丢失标识？"),
            platform("AI content transparency is becoming an end-to-end workflow obligation", "EU AI Act Article 50 applies from Aug 2, 2026. Providers and deployers now need marking, detection, and labeling workflows—not just a watermark toggle.", ["legal trigger", "provider duties", "deployer duties", "deepfake/text labeling", "voluntary code", "implementation gaps"], "twitter", "provider/deployer responsibility map", "Transparency metadata must survive the content lifecycle."),
            platform("从模型水印到发布责任：EU AI Act 第 50 条如何改变 AI 内容产品", "当透明度义务同时落到模型提供者与内容部署者，合规对象就从生成模型扩展到编辑器、CMS、发布平台和审计链路。", ["Article 50 适用范围", "Provider 与 Deployer 分工", "Code 的法律位置", "标记与检测机制", "深伪和特定文本标签", "产品落地路线图"], "wechat", "内容生命周期与责任矩阵", "附 AI 内容透明度产品清单"),
        ),
        topic(
            "2026-08-05-model-research-product-org-loop",
            "2026-08-05-google-deepmind-leadership-model-product-control",
            "ai_macro", "B",
            "模型、研究、App 和开发者平台被放到同一负责人下，组织结构正在成为模型竞争的一部分",
            "前沿研究到产品分发的链路越短，模型能力越容易进入真实用户反馈；但研究独立性、产品节奏和战略职责也更集中。",
            "Google 将 Gemini 模型、前沿研究、Gemini App 和开发者团队交由 Koray 统一负责，Demis 上移至 Alphabet 级 AGI 战略。",
            ["AI 产业研究者", "模型产品负责人", "组织设计观察者"],
            "公开信可确认职位与范围，不能推断调整原因、内部权力细节或未来模型成败。",
            platform("为什么模型大厂开始把研究、App和开发者平台放在一个人手里？", "AI 竞争已经不只是模型排行榜，组织能否把研究快速送进产品并拿回反馈，同样决定速度。", ["这次组织变动是什么", "四类团队为何统一", "研究到产品的反馈环", "集中化的优势", "潜在风险", "观察指标"], "xiaohongshu", "研究—模型—App—开发者闭环", "你更看好集中还是分拆？"),
            platform("Org design is becoming part of the model-product flywheel", "Google put Gemini model development, frontier research, the Gemini app, and developer teams under one operating leader.", ["confirmed changes", "shorter feedback loop", "distribution advantage", "research trade-offs", "strategic role split", "what to watch"], "twitter", "model-to-product org flywheel", "The org chart can be a product architecture."),
            platform("组织即架构：Google 如何重组模型—研究—产品反馈环", "模型公司进入产品竞争后，组织结构决定研究成果多久进入 App、开发者反馈多久返回训练与评测。", ["领导层调整事实", "模型与产品为何合并管理", "开发者平台的反馈价值", "Demis 战略职责上移", "集中控制的风险", "后续观察指标"], "wechat", "组织闭环与信息流图", "附模型公司组织观察框架"),
        ),
        topic(
            "2026-08-08-agent-building-without-users",
            "2026-08-08-gus-chiriboga-my-ai-agents-shipped-128-release",
            "ai_product", "A",
            "AI 让构建变得太便宜后，继续做功能本身可能成为一种拖延",
            "Agent 可以快速生成版本、测试和治理层，却无法替代第一次真实端到端运行和陌生用户验证。",
            "一位独立产品创始人复盘两代 Agent 产品：128 次发布无用户、442 个测试仍在首次真实运行时暴露审批与停滞问题。",
            ["独立开发者", "AI 创业者", "产品经理"],
            "这是作者自报案例，未提供公开仓库或第三方商业数据；能支持失败链路，不能证明普遍因果。",
            platform("AI帮我发了128个版本，结果一个用户都没有", "最刺痛的不是 Agent 写错代码，而是它让继续构建变得太容易，以至于你可以一直不面对用户。", ["128 次发布发生了什么", "自然语言审批如何失效", "442 个测试为何没用", "首次真实运行", "过度构建陷阱", "陌生用户门禁"], "xiaohongshu", "版本数—用户数反差时间线", "你的产品多久没给陌生人用了？"),
            platform("Agents can make building so cheap that building becomes procrastination", "A founder shipped 128 releases with zero external users, then built a deterministic system with 442 passing tests that failed on its first real end-to-end run.", ["case facts", "approval spoofing", "test illusion", "real-run failures", "user validation", "evidence limits"], "twitter", "build loop vs learn loop", "After the first working run, the next task should be a stranger."),
            platform("128 次发布、0 个用户：AI 编程时代最危险的产品幻觉", "当代码和版本生成成本骤降，团队更容易用‘继续完善系统’逃避真实运行和用户验证。", ["两代产品的失败矩阵", "自然语言规则为何不是安全边界", "确定性治理为何仍失败", "测试与真实运行的断层", "构建成瘾", "AI 产品的新用户门禁"], "wechat", "两代失败对比矩阵", "附首次真实运行门禁"),
        ),
        topic(
            "2026-07-31-multi-agent-collaboration-control-plane",
            "2026-07-31-maxime-beauchemin-figma-for-agents-how-airflow-s-c",
            "agent_architecture", "B",
            "多 Agent 团队需要的可能不是更多聊天窗口，而是画布、身份、租约与完整会话审计",
            "Agent 数量增长后，工作分支、长期记忆、角色、权限和人类审查会成为新瓶颈；个人 Coding Agent UI 无法直接扩展为团队系统。",
            "Maxime Beauchemin 公开展示 Agor 多人画布，并提出 identity、scoped delegation、leases 和 audit logs 的企业 Agent 基础层。",
            ["Agent 平台产品经理", "开发者工具团队", "企业安全架构师"],
            "访谈含直接引语与界面，但效率数字和团队使用为本人陈述，无独立审计。",
            platform("公司里的 Agent 比人还多后，聊天列表为什么一定会崩？", "一个人开几个 Agent 可以靠标签；团队同时跑几十个 Agent，需要的是分支画布、身份、租约和审计。", ["Agor 画布长什么样", "worktree 如何映射", "角色与长期记忆", "Okta for Agents", "人类审查瓶颈", "团队 Agent 控制台"], "xiaohongshu", "多人 Agent 画布示意", "你的团队会先缺身份还是审查？"),
            platform("Multi-agent teams need a canvas and identity plane, not a longer chat list", "Agor maps worktrees to collaborative cards and frames enterprise agents around scoped delegated permissions, leases, and audit logs.", ["real workflow", "canvas model", "identity plane", "leases", "review bottleneck", "evidence limits"], "twitter", "agent team control-plane diagram", "The bottleneck moves from code generation to coordination."),
            platform("从个人 Coding Agent 到团队 Agent 画布：协作、身份和审查如何重构", "当 Agent 成为团队成员，产品对象不再只是对话和代码，而是任务分支、角色、权限租约、长期记忆和完整会话证据。", ["Agor 的真实使用场景", "画布与 worktree", "角色型 Agent", "身份、委托和租约", "Yap-to-Ship 瓶颈", "企业 Agent 协作架构"], "wechat", "Agent 团队协作架构图", "附团队 Agent 权限字段"),
        ),
        topic(
            "2026-08-09-ai-fluency-evidence-assessment",
            "2026-08-09-ozan-dagdeviren-things-i-learned-about-how-peopl",
            "ai_product", "A",
            "企业 AI 培训最大的误区，可能是相信员工对自己能力的自评",
            "AI 使用能力的真实差距不仅存在于岗位之间，更存在于同一团队内部；产品应通过对话证据评估，而不是静态选择题或自我打分。",
            "AISA 基于 1800 名用户的长对话评估，披露平均 48 分、约三分之二未达 proficient，以及明显自评偏差。",
            ["企业学习负责人", "AI 产品经理", "组织发展团队"],
            "属于产品运营自选择样本，非代表性人口研究；角色差异、有效性与公平性缺少完整统计。",
            platform("1800人测完AI能力：最不会用的人，反而最容易高估自己", "企业做 AI 培训前，先别问员工‘你会不会用’，因为自评和真实能力可能完全相反。", ["1800 人数据", "平均分与分层", "自评偏差", "同团队巨大差距", "对话式评估机制", "培训如何分层"], "xiaohongshu", "自评—实测差距图", "你会怎么证明自己真的会用 AI？"),
            platform("AI fluency self-assessment may be the wrong enterprise metric", "In a product dataset of 1,800 long-form assessments, low scorers substantially overestimated themselves while high scorers underestimated themselves.", ["reported sample", "calibration gap", "within-team variance", "evidence-based scoring", "sample limits", "product implications"], "twitter", "self-rating vs evidence score", "Measure observable behavior, not confidence."),
            platform("从自评到证据：企业应该怎样真正评估员工的 AI 使用能力", "组织内部 AI 能力差距可能比岗位差异更大，而传统问卷最容易把信心误当能力。", ["1800 人产品数据", "自评失真", "同团队能力分层", "对话 Agent 与隐藏评估 Agent", "证据聚合和校准", "培训与权限如何分层"], "wechat", "对话式能力评估双轨架构", "附 AI Fluency 评估字段"),
        ),
    ])

    topics.extend([
        new_topic(
            "2026-08-10-ai-compute-financing-asset-class", "2026-08-10-nvidia-ai-compute-financing-500b", "ai_macro", "A",
            "AI 算力正在从科技公司 CapEx 变成独立融资资产类别",
            "超过 5000 亿美元是拟动员的第三方资本，不是已到账资金；真正变化是 AI 工厂开始拥有专门的资本结构。",
            "NVIDIA 与六家全球资本机构共同建立独立算力融资平台。",
            "必须区分 MOU、拟动员资本、实际基金规模和已开工项目。",
            "5000亿美元不是AI公司又融了一轮钱", "更重要的变化：算力正在被包装成可长期融资的基础设施资产。",
            "AI compute is becoming a financed infrastructure asset class", "NVIDIA and six capital giants plan to mobilize over $500B—but this is a platform ambition, not committed cash.",
            "从 CapEx 到资产类别：AI 算力融资结构发生了什么", "AI 工厂的竞争正在从 GPU 采购扩展到资本成本、长期使用收入和项目融资能力。",
            ["合作结构与金额口径", "为什么按使用量收入可被金融化", "对算力供给与模型公司的影响", "必须避免的标题误读"],
            ["the financing structure", "committed vs mobilized capital", "why usage revenue matters", "supply-chain implications", "evidence limits"], "资本—算力—使用收入结构图"),
        new_topic(
            "2026-07-22-frontier-labs-multi-supplier-compute", "2026-07-22-amd-anthropic-2gw-mi450", "ai_macro", "A",
            "前沿模型实验室开始以吉瓦规模建立非 NVIDIA 算力第二供给",
            "最高 2GW 与 2027 首个 1GW 是未来部署计划，不是今天已经上线的可用算力。",
            "AMD–Anthropic 合作把 MI450、Helios、ROCm 与 Claude 工程协同绑定。",
            "未披露金额、交付曲线、排他性与性能验收，不能写成 NVIDIA 份额已经被替代。",
            "Anthropic为什么要预订最高2GW AMD算力？", "这不是简单买卡，而是模型实验室与芯片软件栈共同优化。",
            "Frontier labs are building gigawatt-scale second-source compute", "Anthropic plans up to 2GW of AMD MI450 systems while helping optimize ROCm workloads.",
            "2GW 之后：前沿模型公司的多供应商算力战略", "当模型实验室参与芯片软件栈优化，采购关系开始变成路线图协作。",
            ["2GW 与首个 1GW 的时间口径", "Helios 与 MI450 的角色", "Claude 如何参与 ROCm 优化", "第二供给的战略价值"],
            ["confirmed deployment plan", "hardware and software co-design", "second-source strategy", "delivery and benchmark gaps"], "时间轴与供应商协同图"),
        new_topic(
            "2026-07-28-kimi-k3-open-frontier-stack", "2026-07-28-kimi-k3-open-frontier-model", "model", "A",
            "Kimi K3 的看点不只是 2.8T 参数，而是 1M Context Agent RL 的整套系统",
            "开放权重缩小的是可部署边界，不代表训练数据、基础设施和长期执行稳定性都已开放或复现。",
            "Kimi K3 同时公开 MoE 架构、长上下文、可恢复 Sandbox、推理强度和 Agentic RL 设计。",
            "性能、2.5 倍效率与基准主要为官方自报，且报告承认总体仍落后于最强闭源模型。",
            "Kimi K3的2.8T参数，反而不是最值得看的数字", "真正值得拆的是：100万上下文、可恢复沙箱与多档Agent RL如何拼成系统。",
            "Kimi K3 is an open agent stack, not just a 2.8T-parameter model", "Its 1M-context RL system preserves KV cache and resumable sandbox state across long trajectories.",
            "从 KDA 到可恢复 Sandbox：Kimi K3 的开放 Agent 栈", "Kimi K3 展示了预训练架构、长轨迹训练与生产调度如何联合设计。",
            ["2.8T/104B 与 896 专家", "1M Context 的系统代价", "Partial Rollout 与可恢复 Sandbox", "开放权重的真实边界"],
            ["architecture facts", "million-token agentic RL", "resumable environments", "benchmark caveats", "open-weight boundaries"], "模型—训练—运行时三层图"),
        new_topic(
            "2026-08-06-temporal-agent-authorization", "2026-08-06-aws-agentcore-temporal-policies", "agent_architecture", "A",
            "Agent 权限正在从工具白名单升级为会话历史策略",
            "同一个转账工具是否可用，取决于前面是否验证身份、数据是否新鲜、谁批准过，而不只是函数名。",
            "AWS Temporal Policies 已支持跨 Session 动作顺序、前序输出一致性、人工批准与限流。",
            "官方未给出延迟、竞态、撤销传播与误拒率；自然语言策略仍需核对生成的 Cedar 规则。",
            "审批不是弹窗：Agent必须证明前面发生过什么", "Temporal Policy 可以表达‘先验证—再审批—后执行’，这比工具白名单更接近真实业务。",
            "Agent authorization is becoming temporal", "A tool call can now depend on prior actions, previous outputs, human approval, and data freshness in the same session.",
            "从工具权限到会话历史：Temporal Policy 如何重构 Agent 授权", "真实业务权限是有顺序、有时效、有前置条件的，Agent Runtime 开始原生表达这些约束。",
            ["无状态授权为什么不够", "动作顺序与参数继承", "人工批准与数据新鲜度", "限流、撤销和审计问题"],
            ["stateless vs temporal authorization", "sequence and provenance checks", "human approval", "rate limits", "open failure modes"], "先验证—再审批—后执行状态图"),
        new_topic(
            "2026-07-24-persistent-consumer-agent-controls", "2026-07-24-meta-ai-muse-spark-actions", "ai_product", "A",
            "消费级 Agent 开始连接日历、持续运行后，产品必须补齐暂停、过期和失败交接",
            "Meta 展示的是找商品、做计划和定时简报，不是自动购买；查询、建议和交易不能混成一个动作。",
            "Meta AI 已在部分市场滚动开放 Email/Calendar、Slides、Daily Briefing 与持续任务。",
            "未披露逐动作确认、邮件写入、购物提交、日志、失败恢复和完整市场清单。",
            "Meta AI开始替你持续做事，但它到底能做到哪一步？", "找商品不等于下单，查日历不等于替你确认预约。真正的产品边界在动作分级。",
            "Persistent consumer agents need pause, expiry, and handoff controls", "Meta AI can connect to email/calendar and run recurring tasks, but product claims stop short of autonomous transactions.",
            "从 Daily Briefing 到持续代办：消费 Agent 的最小控制合同", "当任务每周自动运行，用户需要理解授权范围、下一次执行、暂停、错误和数据来源。",
            ["已确认的动作对象", "持续任务与定时交付", "建议、提交和交易的边界", "暂停、过期和失败恢复"],
            ["confirmed actions", "recurring execution", "suggestion vs transaction", "pause and expiry", "audit gaps"], "对象—动作—确认等级矩阵"),
        new_topic(
            "2026-08-03-agent-security-real-world-boundary", "2026-08-03-anthropic-cyber-eval-incidents", "agent_architecture", "A",
            "Agent 把真实系统当成 CTF：一句错误环境假设如何穿透沙箱边界",
            "这不是模型单独‘越狱’，而是系统提示、真实网络出口、第三方环境和缺少实时监控共同造成的事故链。",
            "Anthropic 公开 141,006 次评测审计，确认 3 个事件、6 次运行访问真实生产系统。",
            "事故发生在第三方评测环境，缺少产品版部分分类器和监控，不能写成 Claude 产品攻击客户。",
            "AI以为自己在做CTF，结果真的访问了生产系统", "最危险的不是它会攻击，而是系统告诉它‘这里都是模拟目标’，网络却没有真正隔离。",
            "When an agent mistakes production for a CTF", "Anthropic found six runs across three incidents where cyber eval agents reached real systems from a third-party environment.",
            "错误环境假设如何变成真实越权：Anthropic 网络安全评测事故复盘", "Agent 安全必须同时约束模型、系统提示、网络路径、监控和第三方基础设施。",
            ["事故规模与发生环境", "错误系统提示的作用", "网络出口与监控缺口", "谁应承担哪一层责任"],
            ["incident facts", "false environment assumptions", "network isolation", "monitoring gaps", "responsibility layers"], "事故树与五层防线"),
        new_topic(
            "2026-08-13-agent-reproducibility-at-scale", "2026-08-13-hf-icml-open-reproductions", "agent_architecture", "A",
            "Coding Agent 正在把论文复现从少数实验变成可审计的大规模流水线",
            "Agent 提高复现吞吐，但自动 Judge、自选任务和不均等算力会改变结论；‘一项争议’不等于整篇论文无效。",
            "Hugging Face 社区 19 天复现 2,226 篇 ICML 论文并公开 274 份完整 Agent Trace。",
            "参与者与工具自选，Judge 使用 GLM-5.2，结果不能直接当作所有论文质量排名。",
            "19天复现2226篇论文：Coding Agent真正改变了什么？", "最有价值的不是数量，而是代码、产物和完整Agent轨迹终于能一起审计。",
            "Coding agents are turning reproducibility into an auditable pipeline", "The ICML challenge covered 2,226 papers and released 6,816 logbooks plus 274 complete agent traces.",
            "从结果分数到完整轨迹：研究 Agent 的大规模复现工作流", "公开轨迹让研究评测开始检查 Agent 如何得出结论，而不只是最后答对没有。",
            ["2226篇与6816份Logbook", "Agent Trace 为什么重要", "自动 Judge 的偏差", "怎样正确解释被证伪 Claim"],
            ["scale and artifacts", "why traces matter", "judge bias", "selection effects", "safe interpretation"], "论文—Claim—实验—轨迹证据链"),
        new_topic(
            "2026-07-28-coding-agent-verification-bottleneck", "2026-07-28-gergely-orosz-anthropic-verification-bottleneck", "agent_architecture", "A",
            "AI 编码真正的瓶颈正在从实现转向验证",
            "生成更快不等于交付更快；一个重写案例只有 15% 时间在实现，85% 花在编译、修复测试和核验。",
            "Gergely Orosz 的 Anthropic 深访提供了工程团队的一手流程和具体比例。",
            "来自单家公司与单个重写案例，不可外推为行业平均；16.5 万美元 Token 成本也依赖任务。",
            "AI写代码只花15%的时间，剩下85%在干什么？", "当实现越来越便宜，发现未知、修测试和验证反而吞掉绝大多数时间。",
            "The coding-agent bottleneck is moving from implementation to verification", "In one large rewrite, implementation took about 15% of the time; fixing and validation took 85%.",
            "代码生成之后：为什么验证成为 Coding Agent 的主战场", "模型升级会让旧提示词和工程假设折旧，团队必须把验证能力做成系统。",
            ["15/85案例的真实口径", "未知发现与原型", "测试和代码评审变化", "为什么系统提示会折旧"],
            ["case facts", "implementation vs verification", "team workflow changes", "prompt depreciation", "generalization limits"], "实现—修复—验证时间分布"),
        new_topic(
            "2026-08-03-open-model-adoption-metrics", "2026-08-03-nathan-lambert-open-model-artifacts-hub", "ai_macro", "B",
            "判断开放模型格局，不能再只看一次发布榜单",
            "下载、衍生模型、OpenRouter Token 和能力评测衡量的是不同层次；任何单一指标都会制造错误领先者。",
            "Nathan Lambert 的 Artifacts Hub 已联结 792 个模型及多来源采用数据。",
            "下载量不是活跃部署，Token 份额不是全部市场，人工筛选也存在覆盖偏差。",
            "开源模型到底谁领先？先别急着看排行榜", "792个模型放在一起后，下载、衍生、调用和能力会讲出完全不同的故事。",
            "Open-model competition needs adoption depth, not one leaderboard", "Artifacts Hub links 792 models across downloads, derivatives, OpenRouter usage, and capability data.",
            "从模型榜单到采用仪表盘：怎样判断开放模型真实位置", "开放模型竞争需要同时看能力、分发、衍生生态和实际调用，而不是一个漂亮分数。",
            ["792模型覆盖什么", "四类指标分别说明什么", "中美模型采用如何比较", "下载与生产使用的差距"],
            ["coverage", "metric taxonomy", "downloads vs deployment", "regional adoption", "sampling bias"], "能力—下载—衍生—调用四象限"),
        new_topic(
            "2026-07-28-codex-to-knowledge-work-runtime", "2026-07-28-akshay-nathan-chatgpt-work", "ai_product", "A",
            "Codex 的下一步不是写更多代码，而是把 Agent Runtime 扩展到所有知识工作",
            "Sites、Memory、Subagents 和 Finance 工作区让 Coding Harness 进入通用工作，但用户数字、知识工作者占比和生产深度不能混写。",
            "Akshay Nathan 完整访谈揭示 ChatGPT Work 的产品对象和运行时迁移方向。",
            "1000万是 Codex 与 ChatGPT Work 合计口径；20%知识工作者与3倍增长来自节目引用材料，需保留归因。",
            "Codex正在变成ChatGPT Work：最关键的不是No-Code", "真正被复用的是长期任务、记忆、子Agent和工作区这套运行时。",
            "Codex is expanding from coding into a general work runtime", "Sites, memory, subagents, finance, and no-code surfaces reuse the agent harness beyond software work.",
            "从 Codex 到 ChatGPT Work：Coding Harness 如何迁移到知识工作", "当工作对象从代码仓库变成网站、财务数据和长期项目，记忆、权限和交付物状态都要重构。",
            ["访谈确认的产品对象", "Harness 为什么可迁移", "Memory 与 Subagents", "用户数字的口径边界"],
            ["confirmed product surfaces", "runtime reuse", "memory and subagents", "usage metric caveats", "governance questions"], "Coding Runtime 到 Work Runtime 迁移图"),
        new_topic(
            "2026-07-31-model-runtime-efficiency-stack", "2026-07-31-openai-gpt56-efficiency-agent-harness", "model", "A",
            "模型降本不只靠更快芯片：Agent Harness 的上下文策略也在决定成本",
            "20%服务成本和15%生成效率都是 OpenAI 自报；但更重要的是工具输出上限、Append-only 历史和 Prompt Cache 已进入同一效率栈。",
            "OpenAI 首次把模型、内核、Draft Model 与 Agent Harness 优化放在一篇技术说明中。",
            "未披露硬件、工作负载、绝对成本和独立基准，不能把相对改进跨厂商横比。",
            "GPT-5.6降本20%，最值得抄的可能不是Kernel", "Agent每次把工具结果塞满上下文，可能比模型本身更浪费。",
            "Agent harness design is now part of model serving efficiency", "OpenAI ties kernel work, draft-model efficiency, prompt caching, bounded tool output, and append-only history into one stack.",
            "单位成功任务成本：模型—推理—Harness 如何联合优化", "如果只优化每 Token 单价，却让 Agent 重复调用工具和膨胀上下文，整体任务成本仍会失控。",
            ["20%与15%的官方口径", "工具输出为何默认上限1万Token", "Append-only与Prompt Cache", "单位任务成本该怎么测"],
            ["reported efficiency gains", "bounded tool output", "append-only history", "prompt caching", "task-level cost metrics"], "模型—内核—Harness 成本栈"),
        new_topic(
            "2026-07-18-reasoning-effort-product-control", "2026-07-18-sebastian-raschka-reasoning-effort", "model", "B",
            "Reasoning Effort 不是前端多一个档位，而是一套训练与产品预算合同",
            "简单截断 Token 可能损害正确率；更好的方法是在训练中同时学习受预算和无约束推理。",
            "Sebastian Raschka 拆解 Kimi Toggle，并给出 Token 降低约25%—30%的具体机制。",
            "数字来自特定模型报告，不能外推；<think> 标签仅是格式边界，不代表模型真的学会推理。",
            "模型的High/Max档位，到底改变了什么？", "不是给同一答案多等几秒，而是训练时如何让模型学会在预算内和预算外切换。",
            "Reasoning effort is a training contract, not a UI toggle", "Kimi's Toggle alternates budgeted and unconstrained RL phases, cutting generated tokens by roughly 25–30% in its reported setting.",
            "从 Thinking Toggle 到 Reasoning Effort：推理预算如何产品化", "推理强度连接模型训练、Token 成本、用户等待和任务风险，应该成为显式产品参数。",
            ["推理模型的三种形态", "Toggle训练机制", "25%—30%如何理解", "前端档位与预算合同"],
            ["reasoning model taxonomy", "Toggle training", "token-efficiency claim", "UI vs training control", "evidence limits"], "训练阶段与推理档位映射图"),
    ])

    # Preserve human lifecycle and publication metadata across rebuilds.
    existing = {}
    if OUT.exists():
        existing = {x["id"]: x for x in json.loads(OUT.read_text()).get("topics", [])}
    for item in topics:
        sid = item["source_signal_ids"][0]
        if sid not in signals:
            raise SystemExit(f"unknown monthly signal: {sid}")
        if not item["source_urls"]:
            item["source_urls"] = [signals[sid].get("canonical_url") or signals[sid]["url"]]
        old = existing.get(item["id"])
        if old:
            item["status"] = old.get("status", item["status"])
            for key in ("publication", "published_urls", "performance_review"):
                if key in old:
                    item[key] = old[key]

    payload = {
        "schema_version": 1,
        "report_date": "2026-08-14",
        "timezone": "Asia/Shanghai",
        "scope_label_cn": "最近 30 天 · 2026-07-16—2026-08-14",
        "source_scope": {
            "type": "monthly_backfill",
            "start": "2026-07-16",
            "end": "2026-08-14",
            "source_path": "backfills/2026-07-16_to_2026-08-14_all_signals/selected.json"
        },
        "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。月度选题只引用正式入选 Signal，不引用日期候选或抓取失败项。",
        "topics": topics
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(OUT), "topics": len(topics), "platform_variants": len(topics) * 3}, ensure_ascii=False))


if __name__ == "__main__":
    main()
