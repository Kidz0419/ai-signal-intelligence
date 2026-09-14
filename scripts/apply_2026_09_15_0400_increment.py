#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-15"
DAY = ROOT / "daily" / DATE
RUN_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")

COPILOT = "https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection"
COPILOT_DOCS = "https://docs.github.com/copilot/concepts/models/auto-model-selection"
DB_PART_2 = "https://aws.amazon.com/blogs/database/resolve-amazon-aurora-postgresql-lock-contention-with-database-insights-part-2/"
DB_PART_1 = "https://aws.amazon.com/blogs/database/troubleshooting-row-lock-contention-in-amazon-aurora-postgresql-part-1-understanding-row-lock-contention-in-postgresql/"
PCI = "https://aws.amazon.com/blogs/security/aws-security-reference-architecture-a-deep-dive-into-pci-dss-compliance/"
S3_FILES = "https://aws.amazon.com/blogs/storage/connect-workloads-to-amazon-s3-files-across-vpcs-and-accounts/"
DEVFEST = "https://blog.google/innovation-and-ai/technology/developers-tools/devfest2026/"
ANTIMICROBIALS = "https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials/"
ESTEE = "https://openai.com/index/estee-lauder/"
WILDFIRES = "https://openai.com/index/detecting-wildfires-early/"

SIGNAL = {
    "id": "2026-09-14-github-copilot-auto-model-selection-tiers",
    "demo": False,
    "topic_lane": "ai_product",
    "title": "GitHub Copilot 把自动选模拆成三档：用户选目标，系统按每个 Prompt 选模型",
    "summary": "GitHub Copilot 的自动选模新增 efficiency、balance 和 intelligence 三档。用户选择成本、质量与响应时间的偏好，路由器仍按每个 Prompt 的复杂度、系统健康和可用性选择模型；三档使用同一候选模型池。该功能正向 VS Code、Copilot CLI 和 GitHub Copilot app 推送，费用按实际选中的模型计算，付费用户通过 auto 仍享 10% 折扣。",
    "decision": "include",
    "confidence": 94,
    "relevance_level": "P1",
    "signal_type": "core",
    "content_type": "official_release",
    "information_type": "product_workflow",
    "evidence_level": "confirmed",
    "source": "GitHub",
    "url": COPILOT,
    "published_at": "2026-09-14T16:05:27Z",
    "primary_tags": ["Auto model selection", "Cost-quality control", "Per-prompt routing"],
    "secondary_tags": ["GitHub Copilot", "VS Code", "Copilot CLI", "Usage-based billing"],
    "why_it_matters_cn": "多模型产品开始把选模从隐藏的系统决定变成用户可配置的策略，但控制粒度仍停在目标偏好，而不是模型白名单、单次预算或任务规则。它把产品问题从“默认用哪个模型”推进到“谁决定路由目标、每次实际用了什么、费用如何解释”。",
    "personal_relevance_cn": "评估自动选模时，应同时检查用户偏好、管理员模型策略、任务级实际模型、费用、延迟和结果质量。只给三档入口还不够，至少要能回看每次路由结果，并区分用户偏好与组织政策谁优先。",
    "product_opportunity_cn": "把自动选模做成可审计策略对象：目标偏好、允许模型、任务类型、成本上限和回退顺序分别配置；每次响应记录候选模型、最终选择、费用、延迟和策略版本，方便复盘质量与成本。",
    "competitive_risk_cn": "GitHub 已经把自动路由扩展到多端，并允许管理员政策缩小候选模型池。当前三档仍是粗粒度控制，官方没有公开路由评分、阈值或逐任务成本预估，也没有证明 intelligence 档在真实代码任务上稳定优于 balance。",
    "recommended_action": "test",
    "questions_to_validate": [
        "三档设置是按设备、产品端、用户还是组织保存，跨端是否一致？",
        "管理员禁用模型、数据驻留和 FedRAMP 策略与用户选择的 tier 如何裁决？",
        "每次响应能看到最终模型，但能否导出路由理由、费用、延迟和策略版本？",
        "intelligence 与 balance 在同一任务集上的质量、费用和响应时间差异有多大？"
    ],
    "follow_up_triggers": [
        "Auto tiers 扩展到 GitHub 网页、JetBrains、Visual Studio、Xcode 或 Eclipse",
        "GitHub 开放任务级路由日志、成本预估或组织级 tier 策略",
        "出现独立测试比较三档在同一代码任务集上的质量、费用和延迟"
    ],
    "scores": {
        "topic_relevance": 5,
        "novelty": 4,
        "technical_or_product_significance": 4,
        "strategic_value": 4,
        "source_quality": 5,
        "model_value": 3,
        "agent_architecture_value": 4,
        "ai_product_value": 5,
        "macro_value": 2,
        "actionability": 5
    },
    "report_date": DATE,
    "event_date": "2026-09-14",
    "canonical_url": COPILOT,
    "first_seen_date": DATE,
    "last_seen_date": DATE,
    "run_dates": [DATE],
    "evidence_boundary": "GitHub Changelog 正文确认三档含义、相同候选模型池、逐 Prompt 选择、推送端、按实际模型计费和 10% auto 折扣；官方文档补充了系统健康、任务复杂度、管理员模型政策与逐响应显示实际模型。Changelog 使用 2026-09-14 日期路径，RSS 给出 2026-09-14T16:05:27Z。功能仍在 rollout，未核验所有账户可见性，也没有独立比较三档质量、费用和延迟。",
    "related_sources": [{"url": COPILOT_DOCS, "type": "official_product_documentation"}]
}

TOPIC = {
    "id": "2026-09-15-auto-model-selection-needs-audit-log",
    "status": "candidate",
    "timeliness": "today",
    "priority": "A",
    "topic_lane": "ai_product",
    "source_signal_ids": [SIGNAL["id"]],
    "working_title_cn": "自动选模不该只是三档按钮，还要能解释每次模型和费用",
    "core_tension_cn": "用户可以选择成本、均衡或质量目标，但系统仍决定每个 Prompt 用哪个模型；没有任务级路由记录，就很难复盘质量、延迟和费用。",
    "why_now_cn": "GitHub Copilot 刚把 auto model selection 做成 efficiency、balance、intelligence 三档，并扩展到 VS Code、CLI 和 Copilot app。",
    "target_audience_cn": ["AI 产品经理", "开发者工具团队", "企业 AI 平台与成本治理团队"],
    "evidence_boundary_cn": "官方 Changelog 和文档确认三档、路由输入、管理员政策、实际模型显示与计费方式；功能仍在 rollout，路由评分和三档独立效果对比没有公开。",
    "source_urls": [SIGNAL["canonical_url"]],
    "platforms": {
        "xiaohongshu": {
            "title": "AI 自动选模型有三档了，但真正缺的是这张账单",
            "hook": "省钱、均衡、质量，选项很直观。问题是：每个任务到底用了哪个模型、花了多少、为什么这么选？",
            "format": "7页图文卡",
            "outline": ["三档分别控制什么", "每个 Prompt 怎样进入路由", "管理员政策怎样缩小模型池", "按实际模型计费", "目前能看到什么", "还缺哪些路由日志", "自动选模验收清单"],
            "visual_direction": "策略输入、候选模型、路由结果、费用与质量复盘的五段流程图",
            "cta": "你更想要一个自动档，还是一份能解释每次选择的路由账单？"
        },
        "twitter": {
            "title": "Auto model selection needs an audit trail, not just three tiers",
            "hook": "Copilot now lets users bias auto routing toward cost, balance, or quality. The router still chooses per prompt, and billing follows the model actually used.",
            "format": "6帖 Thread",
            "outline": ["three user-facing tiers", "per-prompt routing", "health and complexity inputs", "admin policy precedence", "actual-model billing", "missing route-level evidence"],
            "visual_direction": "policy-to-routing diagram with cost, latency and quality outputs",
            "cta": "Can your auto-router explain the model, cost, and policy used for every response?"
        },
        "wechat": {
            "title": "从 GitHub Copilot 三档自动选模，看多模型产品下一步该补什么",
            "hook": "自动选模开始从黑盒默认值变成用户可配置策略，但三档偏好只是入口，任务级路由记录才决定它能否被企业复盘。",
            "format": "2200—2800字产品分析",
            "outline": ["三档控制语义", "任务复杂度与系统健康", "候选模型和管理员政策", "逐响应显示与实际计费", "用户偏好和组织政策冲突", "路由日志应有哪些字段", "同任务集测试方法", "多模型控制面机会"],
            "visual_direction": "自动选模控制面字段表，区分用户策略、组织政策、运行记录和评测结果",
            "cta": "附一份自动选模产品的可观测性与成本验收表。"
        }
    }
}

NEW_SOURCES = [
    (DB_PART_2, "Resolve Aurora PostgreSQL lock contention with Database Insights: Part 2", "AWS", "confirmed"),
    (DB_PART_1, "Troubleshooting row lock contention in Aurora PostgreSQL: Part 1", "AWS", "confirmed"),
    (PCI, "AWS Security Reference Architecture PCI DSS deep dive", "AWS", "confirmed"),
    (S3_FILES, "Connect workloads to Amazon S3 Files across VPCs and accounts", "AWS", "confirmed"),
    (COPILOT, "Configure cost and quality in Copilot auto model selection", "GitHub", "confirmed"),
    (COPILOT_DOCS, "About Copilot auto model selection", "GitHub Docs", "confirmed"),
    (DEVFEST, "DevFest 2026: Google Developer Events", "Google", "confirmed"),
    (ANTIMICROBIALS, "How a researcher uses Codex and ChatGPT to search for new antimicrobial molecules", "OpenAI", "confirmed"),
    (ESTEE, "Data-driven beauty: Estée Lauder and ChatGPT", "OpenAI", "primary_statement"),
    (WILDFIRES, "Using ChatGPT to detect wildfires early", "OpenAI", "primary_statement")
]

NEW_REVIEWS = [
    {"url": DB_PART_2, "decision": "checked_no_match", "published_at": "2026-09-14T16:02:16Z", "reason": "body and RSS describe PostgreSQL lock analysis and contention mitigation; the workload example contains no material model, agent, AI product or AI market event"},
    {"url": DB_PART_1, "decision": "checked_no_match", "published_at": "2026-09-14T16:02:08Z", "reason": "body and RSS describe PostgreSQL locking internals and monitoring; it is database engineering rather than an AI signal"},
    {"url": PCI, "decision": "checked_no_match", "published_at": "2026-09-14T17:46:56Z", "reason": "body and RSS confirm a PCI DSS security reference guide, but it does not introduce an AI model, agent workflow, AI product control or AI market-structure change"},
    {"url": S3_FILES, "decision": "checked_no_match", "published_at": "2026-09-14T17:10:24Z", "reason": "body and RSS document cross-VPC and cross-account file-system networking; mentions of agents and generative-AI workloads are examples, not a new agent capability or workflow"},
    {"url": COPILOT, "decision": "include", "signal_id": SIGNAL["id"], "published_at": "2026-09-14T16:05:27Z", "reason": "official changelog and product documentation confirm a user-visible three-tier routing control, per-prompt model choice, policy constraints, actual-model disclosure and usage-based billing"},
    {"url": DEVFEST, "decision": "checked_no_match", "published_at": "2026-09-14", "reason": "the first-party body is an event invitation and agenda overview; it announces no material model, agent architecture, product workflow or structural market change"},
    {"url": ANTIMICROBIALS, "decision": "outside_incremental_window_no_material_update", "published_at": "2026-09-10", "reason": "the first-party body is dated September 10; the September 14 sitemap lastmod does not establish a new publication or material update inside the 80-hour window"},
    {"url": ESTEE, "decision": "candidate_only_missing_published_at", "published_at": None, "reason": "the first-party body was readable and describes an enterprise case study, but no datePublished or documented update date was exposed; sitemap lastmod alone cannot satisfy the strict window"},
    {"url": WILDFIRES, "decision": "candidate_only_missing_published_at", "published_at": None, "reason": "the first-party body was readable and describes a ChatGPT-assisted wildfire workflow, but no datePublished or documented update date was exposed; sitemap lastmod alone cannot satisfy the strict window"}
]


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise AssertionError(f"expected one match, found {text.count(old)}: {old[:80]}")
    return text.replace(old, new, 1)


def main() -> None:
    selected_path = DAY / "selected.json"
    selected = load(selected_path)
    if not any(row["id"] == SIGNAL["id"] for row in selected):
        selected.append(SIGNAL)
    dump(selected_path, selected)

    ledger_path = DAY / "citation-ledger.json"
    ledger = load(ledger_path)
    known = {row["url"].rstrip("/") for row in ledger["sources"]}
    next_id = max(row["id"] for row in ledger["sources"]) + 1
    for url, title, publisher, level in NEW_SOURCES:
        if url.rstrip("/") in known:
            continue
        ledger["sources"].append({"id": next_id, "title": title, "url": url.rstrip("/"), "publisher": publisher, "evidence_level": level, "accessed": RUN_AT})
        known.add(url.rstrip("/"))
        next_id += 1
    for source in ledger["sources"]:
        source["url"] = source["url"].rstrip("/")
    dump(ledger_path, ledger)
    dump(DAY / "citations.json", [{"id": row["id"], "url": row["url"]} for row in ledger["sources"]])
    cite = {row["url"].rstrip("/"): f'[{row["id"]}]' for row in ledger["sources"]}
    c = lambda url: cite[url.rstrip("/")]

    brief_path = DAY / "daily-brief.md"
    brief = brief_path.read_text()
    brief = replace_once(brief, "**窗口：** 00:00 增量只核验本轮 7 个 `new_candidates`，没有重扫 171 条滚动候选，也没有重审完整队列。四条正式记录都在北京时间 9 月 14 日晚间发布，本日报按 catch-up 收录并保留 `event_date=2026-09-14`。", "**窗口：** 04:00 增量只核验本轮 9 个 `new_candidates`，没有重扫 166 条滚动候选，也没有重审完整队列。加上 00:00 已核验的 7 个候选，本日累计核验 16 个；五条正式记录都保留真实 `event_date=2026-09-14`。")
    brief = replace_once(brief, "**一句话结论：** 新增 4 条 Signal。两条 P1 把 Agent 的生产控制边界说得很具体：开放金融案例把租户隔离与确定性评分留在应用层，补货样例则把业务规则、无确认运行和人工例外拆成不同控制。[1][3][4]", f"**一句话结论：** 本日累计新增 5 条 Signal。三条 P1 分别把确定性评分、自动写动作和自动选模的控制权拆开：模型可以参与判断，但最终分数、执行授权、路由目标与费用都要留下可复盘记录。[1][3]{c(COPILOT)}")
    brief = replace_once(brief, "| AI 产品 | 0 | 两个生产案例归入架构主线，没有把厂商自报效果另建产品卡 |", "| AI 产品 | 1 | Copilot 自动选模新增成本、均衡、质量三档，并按实际模型计费 |")
    brief = replace_once(brief, "## AI 产品｜0 条\n\nNinth Wave 与补货样例都涉及真实业务工作流，但本轮把它们按架构事件记录，避免把同一份证据拆成重复产品卡。厂商自报效果没有独立评测，不另建产品采用信号。[1][3]", f'''## AI 产品｜1 条

### Copilot 自动选模：用户选目标，系统逐 Prompt 选模型

GitHub Copilot 的 auto model selection 新增 efficiency、balance 和 intelligence 三档。用户表达成本、综合权衡或质量偏好；系统仍结合任务复杂度、实时健康和可用性逐 Prompt 选模型。三档使用同一候选模型池，管理员政策、订阅、数据驻留和 FedRAMP 限制可以进一步缩小范围。{c(COPILOT)}{c(COPILOT_DOCS)}

该功能正向 VS Code、Copilot CLI 和 GitHub Copilot app 推送。费用按实际选中的模型计算，付费用户通过 auto 仍享 10% 折扣；官方文档称用户可查看每次响应实际使用的模型。当前没有公开路由评分、阈值或三档在同一任务集上的质量与成本对照。{c(COPILOT)}{c(COPILOT_DOCS)}

**判断：** 三档偏好把自动路由从黑盒默认值变成了用户策略，但企业控制面还需要任务级路由日志：策略版本、候选池、实际模型、费用、延迟、质量和回退原因。''')
    brief = replace_once(brief, "- OpenAI 与 Apple 诉讼页面：`outside_incremental_window_no_material_update`。正文日期是 8 月 3 日，可见更新截至 9 月 1 日；9 月 14 日 Sitemap `lastmod` 不能证明出现了新事件。[7]", f'''- OpenAI 与 Apple 诉讼页面：`outside_incremental_window_no_material_update`。正文日期是 8 月 3 日，可见更新截至 9 月 1 日；9 月 14 日 Sitemap `lastmod` 不能证明出现了新事件。[7]
- Aurora PostgreSQL 锁争用两篇：`checked_no_match`。正文是数据库锁、监控和吞吐优化，没有模型、Agent 或 AI 产品增量。{c(DB_PART_1)}{c(DB_PART_2)}
- AWS PCI DSS Deep Dive：`checked_no_match`。它是支付卡数据环境的安全参考架构，不是 AI 或 Agent 治理更新。{c(PCI)}
- S3 Files 跨 VPC / 账户接入：`checked_no_match`。正文讲文件系统网络与权限，Agent 只是工作负载示例。{c(S3_FILES)}
- Google DevFest 2026：`checked_no_match`。正文是活动邀请和议程概览，没有发布新能力。{c(DEVFEST)}
- OpenAI 抗菌分子案例：`outside_incremental_window_no_material_update`。官方正文日期为 9 月 10 日，9 月 14 日 Sitemap `lastmod` 不能把它改成窗口内事件。{c(ANTIMICROBIALS)}
- OpenAI Estée Lauder 与野火案例：`candidate_only_missing_published_at`。两篇正文可读，但页面没有暴露可核验的发布日期或更新日期；只保留候选，不进入正式日桶。{c(ESTEE)}{c(WILDFIRES)}''')
    brief = replace_once(brief, "- 7 个真新增候选都完成了正文和日期核验；Sitemap `lastmod` 没有被当作发布日期。", "- 04:00 的 9 个真新增候选都完成正文核验；两篇 OpenAI 页面因缺少可核验日期保留为 `candidate_only`，没有把 Sitemap `lastmod` 当成发布日期。")
    brief = replace_once(brief, "- AWS 三篇文章的 HTML metadata 与 RSS 时间一致。RDS 条目因领域不符排除；Google 因仍是缺少规模和执行承诺的探索排除。", "- AWS Database、Security、Storage 的五篇新增正文均与 AI 四主线无实质关系；GitHub Copilot Changelog 与官方文档共同确认三档控制、逐 Prompt 路由、政策边界和实际模型计费。")
    brief = replace_once(brief, "4. 持续观察 Product Engineer 与现场部署岗位，但暂不把十年预测当作劳动力事实。", "4. 对 Copilot 三档做同任务集对照，记录实际模型、费用、延迟和完成质量；不要只比较档位名称。\n5. 持续观察 Product Engineer 与现场部署岗位，但暂不把十年预测当作劳动力事实。")
    brief = replace_once(brief, "- Laurie Voss 条目是具名作者的预测；两项前提、当前能力缺口和未复核的数据边界均保留。[9]", f"- Laurie Voss 条目是具名作者的预测；两项前提、当前能力缺口和未复核的数据边界均保留。[9]\n- Copilot 三档与计费来自官方发布和文档；仍处于 rollout，路由规则与独立效果对比未公开。{c(COPILOT)}{c(COPILOT_DOCS)}")
    brief = replace_once(brief, "**一句话结论：** 7 个真新增候选完成正文核验，新增 4 条 Signal：P1 两条、P2 两条。", "**一句话结论：** 本日两轮共核验 16 个真新增候选，累计新增 5 条 Signal：P1 三条、P2 两条。")
    brief = replace_once(brief, "**判断：** Agent 自动化要把“能否判断”“是否获权执行”“失败后怎么停和撤销”分开；模型定制也要先证明失败模式，再增加训练成本。", f"**重点 3：** Copilot 自动选模新增成本、均衡、质量三档，系统仍逐 Prompt 选模型，并按实际模型计费。{c(COPILOT)}{c(COPILOT_DOCS)}\n\n**判断：** Agent 自动化要把“能否判断”“是否获权执行”“失败后怎么停和撤销”分开；自动选模还要能解释实际模型与费用。")
    brief = replace_once(brief, "**结果：** previous_count=0，new_count=4，updated_count=0，total_count=4。", "**结果：** 04:00 增量 previous_count=4，new_count=1，updated_count=0，total_count=5。")
    brief = brief[:brief.index("## Sources\n")] + "## Sources\n\n" + "\n".join(f'[{row["id"]}] {row["url"]}' for row in ledger["sources"]) + "\n"
    brief_path.write_text(brief)

    topics_path = ROOT / "content-topics" / DATE / "topics.json"
    topics = load(topics_path)
    if not any(row["id"] == TOPIC["id"] for row in topics["topics"]):
        topics["topics"].append(TOPIC)
    dump(topics_path, topics)

    summary_path = DAY / "run-summary.json"
    summary = load(summary_path)
    known_reviews = {row["url"].rstrip("/") for row in summary.get("candidate_reviews", [])}
    summary.setdefault("candidate_reviews", []).extend(row for row in NEW_REVIEWS if row["url"].rstrip("/") not in known_reviews)
    summary.update({
        "run_type": "daily_four_lane_incremental_editorial_review",
        "run_at": RUN_AT,
        "deliverable_outcome": "success",
        "scheduler_outcome": "success",
        "window": load(DAY / "discovery-candidates.json")["window"],
        "raw_candidates": 166,
        "unique_candidates": 125,
        "editorial_shortlist": 1,
        "previous_count": 4,
        "new_count": 1,
        "updated_count": 0,
        "excluded_count": 6,
        "unreviewed_candidate_count": 0,
        "total_count": 5,
        "selected": 5,
        "lane_counts": {"model": 1, "agent_architecture": 2, "ai_product": 1, "ai_macro": 1},
        "priority_counts": {"P0": 0, "P1": 3, "P2": 2, "P3": 0},
        "candidate_queue_count": 16,
        "new_in_run_count": 9,
        "reviewed_new_candidates": 9,
        "day_reviewed_candidates_total": 16,
        "review_breakdown": {"selected": 1, "below_formal_bar": 5, "outside_incremental_window": 1, "duplicate_or_merged": 0, "unresolved": 2},
        "content_topics": {"topic_count": 5, "platform_variants": 15},
        "review_notes": [
            "Reviewed only the 9 candidates newly observed by the 04:00 baseline; the 166-item rolling pool, full registry and 16-item queue were not rescanned.",
            "GitHub Copilot auto-model tiers cleared the P1 product gate after the changelog body and product documentation confirmed routing, policy, model disclosure and billing semantics.",
            "Five AWS/Google items were body-verified and excluded because they were database, security, storage or event content without a material AI change.",
            "The OpenAI antimicrobials page is dated September 10 and remained outside the 80-hour window despite a newer sitemap lastmod.",
            "The Estée Lauder and wildfire pages were readable but exposed no verifiable publication/update date, so they remain candidate_only rather than checked_no_match.",
            "Across both September 15 increments, 16 new candidates were reviewed and five durable signals were selected; all selected events retain event_date 2026-09-14."
        ]
    })
    dump(summary_path, summary)

    discovery_path = DAY / "discovery-candidates.json"
    discovery = load(discovery_path)
    discovery["editorial_review"] = {
        "completed_at": RUN_AT,
        "reviewed_new_candidates": 9,
        "selected": 1,
        "excluded": 6,
        "candidate_only": 2,
        "reviews": NEW_REVIEWS
    }
    dump(discovery_path, discovery)

    collection_path = DAY / "collection-run-summary.json"
    collection = load(collection_path)
    collection["editorial_handoff"] = {
        "completed_at": RUN_AT,
        "new_in_run_count": 9,
        "reviewed_new_candidates": 9,
        "selected": 1,
        "excluded": 6,
        "candidate_only": 2,
        "final_day_signal_count": 5
    }
    dump(collection_path, collection)

    print(json.dumps({"date": DATE, "reviewed_new_candidates": 9, "selected_increment": 1, "candidate_only": 2, "final_signals": 5, "topics": 5, "platform_variants": 15}, ensure_ascii=False))


if __name__ == "__main__":
    main()
