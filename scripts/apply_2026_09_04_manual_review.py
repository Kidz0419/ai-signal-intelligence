#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-04"
TZ = ZoneInfo("Asia/Shanghai")
RUN_AT = datetime.now(TZ).replace(microsecond=0)
DISCOVERY_START = "2026-09-01T08:00:38+08:00"
DISCOVERY_END = "2026-09-04T16:00:38+08:00"
CANDIDATE_QUEUE_COUNT = 126
NEW_IN_RUN_COUNT = 10

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
LANE_ORDER = {"model": 0, "agent_architecture": 1, "ai_product": 2, "ai_macro": 3}
TOPIC_PRIORITY_ORDER = {"A": 0, "B": 1, "C": 2}


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


rows = [
    {
        "id": "2026-09-03-openai-gpt6-astra-broad-release-monitorability",
        "demo": False,
        "topic_lane": "model",
        "title": "OpenAI 开始广泛部署 GPT-6 Astra，并承认 CoT 监控更难了",
        "summary": "OpenAI 9 月 3 日发布的 safety overview 说，GPT‑6 Astra 已开始广泛部署，并成为其首个达到 Preparedness Framework Critical 网络安全阈值的模型。官方同时说，Astra 已把 misalignment monitoring 扩到全部 tool-using inference，但相较 GPT‑5.6 Sol，Astra 更能控制自己的 CoT、在对抗条件下有时能绕过内部监控。OpenAI 同日案例还写到，Legora 用 Astra 的 Agent 在一次 run 中完成 41 份财务文件 tie-out，并把逐项核对结果交给人工复核。",
        "decision": "include",
        "confidence": 93,
        "relevance_level": "P0",
        "signal_type": "core",
        "content_type": "official_release",
        "information_type": "model_release",
        "evidence_level": "confirmed",
        "source": "OpenAI",
        "url": "https://openai.com/index/safety-overview-gpt-6-astra",
        "published_at": "2026-09-03T00:00:00Z",
        "primary_tags": [
            "OpenAI",
            "GPT-6 Astra",
            "Monitorability"
        ],
        "secondary_tags": [
            "Preparedness Framework",
            "Misalignment Monitoring",
            "Legora"
        ],
        "why_it_matters_cn": "9 月 1 日那条还是“跨线后先上锁”；到 9 月 3 日已经变成“critical cyber model 开始广泛部署，但监控边界也更紧张”。能力释放、上线状态和治理代价这次一起变了。",
        "personal_relevance_cn": "如果你在看 frontier model 的产品化，这条最该拆的是：模型一旦真的开始放量，监控是不是跟着从实验室挪到全部 tool-using inference，CoT 可监控性下降又会把哪些审批、日志和沙箱要求提前变成默认配置。",
        "product_opportunity_cn": "可以围绕高风险模型的分层 access、全过程监控、异常升级、审计导出和人审回路，设计从研究阈值走向广泛部署的控制面。",
        "competitive_risk_cn": "广泛部署、监控和对齐改善都来自 OpenAI 自述；Astra 的可用范围、价格、默认权限和第三方复现实测，还没有在同一批材料里完整公开。",
        "recommended_action": "investigate",
        "questions_to_validate": [
            "Astra 的广泛部署具体落在哪些产品、套餐和权限层级，默认工具权限是否和早前 Daybreak / 受限通道不同？",
            "全量 tool-using inference 的 misalignment monitoring 会记录哪些字段、保留多久，又如何和人工审批或自动拦截联动？",
            "当 OpenAI 自己承认 CoT monitorability 下降后，外部企业会不会要求更重的沙箱、日志和强制 review gate？"
        ],
        "follow_up_triggers": [
            "OpenAI 发布更完整的 GPT‑6 Astra 产品页、价格、访问说明或系统卡补充材料",
            "出现第三方对 Astra 漏洞发现、误报、monitor evasion 或企业部署边界的独立复盘",
            "OpenAI 披露更多与 Astra 绑定的管理员控制项、审计字段或滥用处理流程"
        ],
        "scores": {
            "topic_relevance": 5,
            "novelty": 5,
            "technical_or_product_significance": 5,
            "strategic_value": 5,
            "source_quality": 4,
            "model_value": 5,
            "agent_architecture_value": 3,
            "ai_product_value": 2,
            "macro_value": 3,
            "actionability": 5
        },
        "report_date": DATE,
        "event_date": "2026-09-03",
        "canonical_url": "https://openai.com/index/safety-overview-gpt-6-astra",
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": "发布时间来自 OpenAI News RSS；正文来自公开文本镜像。能确认的是 OpenAI 正式把 GPT‑6 Astra 描述为 broad deployment、Critical cyber threshold、全量 tool-using inference misalignment monitoring，以及 monitorability 下降趋势。不能把这些写成第三方独立验证，也不能补写未公开的访问层级、默认权限或价格。",
        "related_sources": [
            {
                "url": "https://openai.com/news/rss.xml",
                "type": "official_rss_date"
            },
            {
                "url": "https://openai.com/index/legora-financial-statement-review-with-astra",
                "type": "deployment_case_study"
            },
            {
                "url": "https://openai.com/index/path-to-astra",
                "type": "prior_gating_context"
            }
        ]
    },
    {
        "id": "2026-09-03-openai-daybreak-frontline-defenders-channel",
        "demo": False,
        "topic_lane": "ai_macro",
        "title": "OpenAI 把 Daybreak 做成关键基础设施分发渠道：10 亿美元补贴、MS-ISAC 试点和 35+ 合作产品一起上桌",
        "summary": "OpenAI 9 月 3 日发布 Daybreak for Frontline Defenders：未来六个月计划提供 10 亿美元的补贴式 Daybreak access，优先面向美国水务、电网、州和地方政府、社区银行、非营利组织和开源维护者。正文还写明，OpenAI 正在和 MS-ISAC 做面向公共部门与水务的 pilot；Daybreak Defense Network 已有 35 个以上合作产品和 partner-operated services；Daybreak 现有 approved organizations / workspaces 已超过 2,000。",
        "decision": "include",
        "confidence": 90,
        "relevance_level": "P1",
        "signal_type": "strategic_radar",
        "content_type": "official_release",
        "information_type": "industry_structure",
        "evidence_level": "primary_statement",
        "source": "OpenAI",
        "url": "https://openai.com/index/daybreak-for-frontline-defenders",
        "published_at": "2026-09-03T13:15:00Z",
        "primary_tags": [
            "OpenAI",
            "Daybreak",
            "Critical Infrastructure"
        ],
        "secondary_tags": [
            "MS-ISAC",
            "Defense Network",
            "$1B Commitment"
        ],
        "why_it_matters_cn": "这不是又一篇安全宣言。更关键的变化是 frontier cyber model 开始被包装成按行业分发的产品与渠道：补贴、培训、伙伴网络和 sector-specific pilot 一起出现了。",
        "personal_relevance_cn": "如果你在看 frontier AI 的分发和竞争位置，这条值得盯的是：谁能先把高风险能力接进关键基础设施、社区银行和公共部门的既有工具链，并把 access、培训和 remediation workflow 一起打包。",
        "product_opportunity_cn": "可以围绕行业准入、验证流程、培训支持、伙伴嵌入式工作流、修复回路和审计留痕，设计面向高风险 AI 能力的 sector control plane。",
        "competitive_risk_cn": "10 亿美元补贴、伙伴覆盖和项目效果目前都主要来自 OpenAI 自述；六个月内的真实消耗、准入门槛和防守成效还没有独立核验。",
        "recommended_action": "investigate",
        "questions_to_validate": [
            "Daybreak Blue、Daybreak Red 和这次前线防守计划之间的资格审查、日志要求和使用边界，到底怎样区分？",
            "35+ partner products 里，哪些只是模型接入，哪些已经把发现、验证、修复和 review 真串成工作流？",
            "补贴结束后，关键基础设施客户会留下多少真实付费需求，还是只形成一次性的试点热度？"
        ],
        "follow_up_triggers": [
            "OpenAI 或伙伴公开更具体的准入标准、管理员字段、审计方式和实际部署案例",
            "MS-ISAC 试点披露更多关于优先级、处置流程、误报率或修复结果的数据",
            "Daybreak Defense Network 公布更多 partner 名单、产品形态或行业化分发结果"
        ],
        "scores": {
            "topic_relevance": 5,
            "novelty": 4,
            "technical_or_product_significance": 4,
            "strategic_value": 5,
            "source_quality": 4,
            "model_value": 2,
            "agent_architecture_value": 2,
            "ai_product_value": 3,
            "macro_value": 5,
            "actionability": 4
        },
        "report_date": DATE,
        "event_date": "2026-09-03",
        "canonical_url": "https://openai.com/index/daybreak-for-frontline-defenders",
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": "发布时间来自 OpenAI News RSS；正文来自公开文本镜像。能确认的是 Daybreak for Frontline Defenders 已作为官方项目发布，且页面写明 10 亿美元补贴承诺、MS-ISAC 试点、35+ partner products / services 与 2,000+ approved organizations / workspaces。不能把六个月内的真实使用量、伙伴效果或跨国扩展写成已经兑现。",
        "related_sources": [
            {
                "url": "https://openai.com/news/rss.xml",
                "type": "official_rss_date"
            }
        ]
    },
    {
        "id": "2026-09-01-openai-enterprise-agent-workflow-pattern",
        "demo": False,
        "topic_lane": "ai_product",
        "title": "OpenAI 的新企业案例开始收敛成一条执行范式：稳定流程、持久上下文、测试和签核一起进场",
        "summary": "OpenAI 9 月 1 日的 workflow 正文和 Gilbert + Tobin 案例，把 enterprise agent 的落地 pattern 说得更具体了：Basis 把 first-day onboarding 做成能后台完成集成配置的 reusable skill；Clay 给每个客户账户配 persistent workspace 和 nightly subagent；Exa 让 Codex 从集成线索走到创建 PR、跑测试和准备周报；Gilbert + Tobin 则把 approved-task guidance、role-based access、Australian data residency 和人工 sign-off 放进 KYC/AML、audit report 与运营流程。",
        "decision": "include",
        "confidence": 88,
        "relevance_level": "P1",
        "signal_type": "research",
        "content_type": "analysis",
        "information_type": "product_workflow",
        "evidence_level": "primary_statement",
        "source": "OpenAI",
        "url": "https://openai.com/index/ai-native-company-workflows",
        "published_at": "2026-09-01T17:00:00Z",
        "primary_tags": [
            "OpenAI",
            "Enterprise Workflows",
            "Codex"
        ],
        "secondary_tags": [
            "Gilbert + Tobin",
            "Persistent Workspace",
            "Human Sign-off"
        ],
        "why_it_matters_cn": "这不是又一轮“企业都在用 AI”的空话。真正有用的是，OpenAI 和客户案例开始收敛到一套可复用的执行结构：任务定义、上下文持久化、工具接入、测试与证据、人审签核和权限边界。",
        "personal_relevance_cn": "如果你在设计 agent 产品或企业控制面，这条最值得对照的是：哪些任务值得变成 reusable skill，哪些必须保留 persistent workspace、evidence-linked recommendation、data residency 和 sign-off gate，哪些只能停在 Chat 层。",
        "product_opportunity_cn": "可以把 job description、workspace persistence、evidence trace、role-based control、data residency、review gate 和交付物回链做成企业 agent 的标准部件。",
        "competitive_risk_cn": "30 分钟 onboarding、87% seat activity、分钟级 KYC/AML 与 PR / 周报产出都来自 OpenAI 或客户自报，没有独立 ROI 审计，也没有完整管理后台截图。",
        "recommended_action": "investigate",
        "questions_to_validate": [
            "这些 workflow 里，哪些对象已经有管理员可配置的权限、审计导出、暂停和回滚机制，哪些还停留在案例叙述层？",
            "当同一企业同时使用 Chat、Work 和 Codex 时，任务路由、上下文边界和最终责任人是怎样分层的？",
            "Gilbert + Tobin 的数据驻留、approved-task guidance 与人工 sign-off，能否被更多受监管行业复用，还是依赖定制化实施？"
        ],
        "follow_up_triggers": [
            "OpenAI 帮助中心、产品文档或演示补充更多 Work / Codex 企业控制面的具体字段",
            "更多客户公开真实部署 UI、管理员设置、审计日志或跨团队 rollout 复盘",
            "Basis、Clay、Exa 或 Gilbert + Tobin 进一步披露关于权限、失败边界和人审节点的细节"
        ],
        "scores": {
            "topic_relevance": 5,
            "novelty": 4,
            "technical_or_product_significance": 4,
            "strategic_value": 4,
            "source_quality": 4,
            "model_value": 1,
            "agent_architecture_value": 4,
            "ai_product_value": 5,
            "macro_value": 2,
            "actionability": 5
        },
        "report_date": DATE,
        "event_date": "2026-09-01",
        "canonical_url": "https://openai.com/index/ai-native-company-workflows",
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": "发布时间来自 OpenAI News RSS；正文来自公开文本镜像。能确认的是 OpenAI 官方案例里描述的 workflow 结构、对象、动作和人工 review / sign-off 边界。时间节省、活跃率和效果数字主要来自 OpenAI 或客户自报，不能写成独立审计结论，也不能补写未展示的管理后台能力。",
        "related_sources": [
            {
                "url": "https://openai.com/news/rss.xml",
                "type": "official_rss_date"
            },
            {
                "url": "https://openai.com/index/gilbert-tobin",
                "type": "case_study"
            }
        ]
    }
]


topics_payload = {
    "schema_version": 1,
    "report_date": DATE,
    "timezone": "Asia/Shanghai",
    "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。",
    "scope_label_cn": f"当日增量 · {DATE}",
    "source_scope": {
        "type": "daily",
        "date": DATE
    },
    "topics": [
        {
            "id": "2026-09-04-gpt6-astra-broad-deployment-monitorability",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "model",
            "source_signal_ids": [
                "2026-09-03-openai-gpt6-astra-broad-release-monitorability"
            ],
            "working_title_cn": "Astra 真正值得看的不是更强了，而是 OpenAI 一边开始广泛部署，一边公开承认 CoT 监控更难",
            "core_tension_cn": "高风险模型一旦真的开始放量，产品竞争会很快从“谁能力更强”转到“谁能把监控、权限和人审一起做成默认控制面”。",
            "why_now_cn": "OpenAI 9 月 3 日的官方 safety overview 首次把 broad deployment、Critical 阈值、全量 misalignment monitoring 和 monitorability 下降写进同一页。",
            "target_audience_cn": [
                "模型产品负责人",
                "高风险 AI 治理团队",
                "安全与合规研究者"
            ],
            "evidence_boundary_cn": "能确认的是 OpenAI 的官方发布与自述评估；可用范围、默认权限和第三方独立实测仍未在同批材料里完整公开。",
            "source_urls": [
                "https://openai.com/index/safety-overview-gpt-6-astra"
            ],
            "platforms": {
                "xiaohongshu": {
                    "title": "Astra 真正值得看的不是更强了，而是 OpenAI 公开承认 CoT 监控更难",
                    "hook": "别只看 GPT‑6 Astra 能发现漏洞。更关键的是，OpenAI 一边开始广泛部署，一边也承认这代模型更难靠 CoT 监控。",
                    "format": "7页图文卡",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 控制面",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 架构判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "对象—动作—权限边界图，结论先行",
                    "cta": "你最想先验证哪条监控或审批边界？"
                },
                "twitter": {
                    "title": "Astra is interesting not just because it is stronger, but because OpenAI is broad-deploying it while admitting CoT monitoring got harder",
                    "hook": "The key shift is not benchmark inflation. It's a critical cyber model moving into broad deployment with heavier monitoring and weaker CoT visibility at the same time.",
                    "format": "7帖 Thread",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 控制面",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 架构判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "one control-plane diagram",
                    "cta": "Which control would you pressure-test first?"
                },
                "wechat": {
                    "title": "Astra 真正值得看的不是更强了，而是 OpenAI 一边开始广泛部署，一边公开承认 CoT 监控更难",
                    "hook": "这轮真正的新信号不是模型又强了一点，而是 critical cyber model 的放量与控制代价同时被摊开了。",
                    "format": "1800—2400字深度文章",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 控制面",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 架构判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "控制面图、证据边界表、验证清单",
                    "cta": "文末附高风险模型放量的验收问题"
                }
            }
        },
        {
            "id": "2026-09-04-daybreak-frontline-defenders-channel",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "ai_macro",
            "source_signal_ids": [
                "2026-09-03-openai-daybreak-frontline-defenders-channel"
            ],
            "working_title_cn": "Daybreak 正在从特殊 access program 变成关键基础设施拿到 frontier cyber 能力的分发渠道",
            "core_tension_cn": "真正的竞争不只是模型能力，而是谁能把高风险能力接到关键基础设施客户已经在用的伙伴产品、培训和修复流程里。",
            "why_now_cn": "OpenAI 这次把 10 亿美元补贴、MS-ISAC 试点、35+ 合作产品和 2,000+ 已批准组织写进了同一份项目发布。",
            "target_audience_cn": [
                "AI 宏观研究者",
                "安全平台团队",
                "企业分发与合作负责人"
            ],
            "evidence_boundary_cn": "已确认的是项目发布与官方承诺；六个月内的真实消耗、部署深度和防守成效还没有独立核验。",
            "source_urls": [
                "https://openai.com/index/daybreak-for-frontline-defenders"
            ],
            "platforms": {
                "xiaohongshu": {
                    "title": "Daybreak 正在从特殊 access program 变成关键基础设施的分发渠道",
                    "hook": "这次值得看的不是 OpenAI 又喊了一次安全口号，而是它开始把 frontier cyber 能力按行业、按伙伴、按工作流卖出去。",
                    "format": "7页图文卡",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 分发结构",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 竞争判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "渠道结构图、角色关系图",
                    "cta": "你觉得补贴、伙伴还是培训，哪一个最决定落地？"
                },
                "twitter": {
                    "title": "Daybreak is starting to look less like a special access program and more like a distribution channel into critical-infrastructure security workflows",
                    "hook": "The notable move is not just a cyber-AI announcement. It's subsidy + training + partner products + public-sector pilots showing up as one go-to-market package.",
                    "format": "7帖 Thread",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 分发结构",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 竞争判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "channel map or workflow diagram",
                    "cta": "What would you watch first: eligibility, logs, or partner depth?"
                },
                "wechat": {
                    "title": "Daybreak 正在从特殊 access program 变成关键基础设施拿到 frontier cyber 能力的分发渠道",
                    "hook": "高风险 AI 能力的商业化，不再只是 API 开关，而是补贴、伙伴、培训和修复流程一起进场。",
                    "format": "1800—2400字深度文章",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 分发结构",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 竞争判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "分发结构图、角色表、验证清单",
                    "cta": "文末附关键基础设施 access program 观察框架"
                }
            }
        },
        {
            "id": "2026-09-04-enterprise-agent-workflow-pattern",
            "status": "candidate",
            "timeliness": "this_week",
            "priority": "A",
            "topic_lane": "ai_product",
            "source_signal_ids": [
                "2026-09-01-openai-enterprise-agent-workflow-pattern"
            ],
            "working_title_cn": "企业 agent 落地开始收敛成一条执行范式：稳定流程、持久上下文、测试和签核一起进场",
            "core_tension_cn": "很多团队还在争论 agent 能不能做事，真正拉开差距的反而是怎样把任务定义、上下文、工具、证据和人审串成一个可复用工作流。",
            "why_now_cn": "OpenAI 的 workflow 总结和 Gilbert + Tobin 案例，把 onboarding、销售、开发者生态、KYC/AML 和审计任务放进了同一种结构里。",
            "target_audience_cn": [
                "企业 AI 产品经理",
                "Agent 设计与平台团队",
                "受监管行业数字化负责人"
            ],
            "evidence_boundary_cn": "能确认的是官方案例描述的对象、动作和 review gate；效率、活跃率和 ROI 仍主要是厂商或客户自报。",
            "source_urls": [
                "https://openai.com/index/ai-native-company-workflows"
            ],
            "platforms": {
                "xiaohongshu": {
                    "title": "企业 agent 落地开始收敛成一条执行范式：稳定流程、持久上下文、测试和签核一起进场",
                    "hook": "真正值得抄作业的不是哪家公司上了 AI，而是它们终于把 agent workflow 的骨架讲清楚了。",
                    "format": "7页图文卡",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 工作流骨架",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 控制面判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "工作流骨架图、对象—动作—人审表",
                    "cta": "你会先把哪类任务做成 reusable skill？"
                },
                "twitter": {
                    "title": "Enterprise agent deployment is converging on a clearer pattern: stable workflow, persistent context, tests, and human sign-off",
                    "hook": "The interesting move is not 'AI adoption' in the abstract. It's vendors and customers finally describing a reusable workflow skeleton for bounded execution.",
                    "format": "7帖 Thread",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 工作流骨架",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 控制面判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "workflow skeleton diagram",
                    "cta": "Which layer matters most: context, controls, or sign-off?"
                },
                "wechat": {
                    "title": "企业 agent 落地开始收敛成一条执行范式：稳定流程、持久上下文、测试和签核一起进场",
                    "hook": "这次值得拆的，不是哪家企业‘开始用 AI’，而是 agent 从聊天走向执行时，骨架终于被讲清楚了。",
                    "format": "1800—2400字深度文章",
                    "outline": [
                        "已确认发生了什么",
                        "关键对象与动作 / 工作流骨架",
                        "为什么这件事现在值得写",
                        "证据边界和不能误写的地方",
                        "对产品 / 控制面判断的启发",
                        "接下来要继续验证什么"
                    ],
                    "visual_direction": "工作流骨架图、边界表、验证清单",
                    "cta": "文末附企业 agent 工作流设计问题"
                }
            }
        }
    ]
}

ledger_sources = [
    {
        "id": 1,
        "title": "OpenAI News RSS",
        "url": "https://openai.com/news/rss.xml",
        "publisher": "OpenAI",
        "evidence_level": "confirmed",
        "accessed": RUN_AT.isoformat()
    },
    {
        "id": 2,
        "title": "OpenAI 开始广泛部署 GPT-6 Astra，并承认 CoT 监控更难了",
        "url": "https://r.jina.ai/http://openai.com/index/safety-overview-gpt-6-astra",
        "publisher": "OpenAI / r.jina.ai text mirror",
        "evidence_level": "confirmed",
        "accessed": RUN_AT.isoformat()
    },
    {
        "id": 3,
        "title": "Legora reviewed 41 documents in minutes with GPT-6 Astra",
        "url": "https://r.jina.ai/http://openai.com/index/legora-financial-statement-review-with-astra",
        "publisher": "OpenAI / r.jina.ai text mirror",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT.isoformat()
    },
    {
        "id": 4,
        "title": "Daybreak for Frontline Defenders: $1B to protect essential services",
        "url": "https://r.jina.ai/http://openai.com/index/daybreak-for-frontline-defenders",
        "publisher": "OpenAI / r.jina.ai text mirror",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT.isoformat()
    },
    {
        "id": 5,
        "title": "How AI-native companies turn workflows into operating capability",
        "url": "https://r.jina.ai/http://openai.com/index/ai-native-company-workflows",
        "publisher": "OpenAI / r.jina.ai text mirror",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT.isoformat()
    },
    {
        "id": 6,
        "title": "How law firm Gilbert + Tobin governs and scales AI with OpenAI",
        "url": "https://r.jina.ai/http://openai.com/index/gilbert-tobin",
        "publisher": "OpenAI / r.jina.ai text mirror",
        "evidence_level": "primary_statement",
        "accessed": RUN_AT.isoformat()
    }
]

citations = [{"id": source["id"], "url": source["url"]} for source in ledger_sources]
ledger = {
    "version": 1,
    "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
    "sources": ledger_sources,
}

brief = f'''# AI Signal 日报｜{DATE}

**窗口：** 发现窗口北京时间 2026-09-01 08:00 至 2026-09-04 16:00；本轮只核验 10 个真新增候选，不重扫 126 条待审队列。  
**一句话结论：** 这轮补进 3 条正式 signal，日内总数从 0 增到 3。最该盯的是 OpenAI 已开始广泛部署 GPT‑6 Astra：它一边把 misalignment monitoring 推到全部 tool-using inference，一边也公开承认 Astra 比 GPT‑5.6 Sol 更难靠 CoT 监控。[1][2]

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 1 | GPT‑6 Astra 从“跨过 critical 阈值”走到“开始广泛部署”，同时公开 monitorability 下降 |
| Agent 架构 | 0 | 本轮没有独立新增正式架构卡；相关执行控制面更多出现在企业工作流案例里 |
| AI 产品 | 1 | 企业 agent 落地开始收敛到稳定流程、持久上下文、测试与签核的组合 |
| AI 宏观 | 1 | Daybreak 开始从 access program 变成关键基础设施拿到 frontier cyber 能力的分发渠道 |

## 模型｜1 条

### OpenAI：GPT‑6 Astra 真开始广泛部署，但 CoT 监控也更难了

OpenAI 9 月 3 日的 safety overview 直接写明，GPT‑6 Astra 已开始广泛部署，并成为其首个达到 Preparedness Framework Critical 网络安全阈值的模型。官方同时说，Astra 已把 misalignment monitoring 扩到全部 tool-using inference，但相较 GPT‑5.6 Sol，它更能控制自己的 CoT，在对抗条件下有时还能绕过内部监控。[1][2]

同日案例还给了一个更贴地的工作流样本：Legora 说，Astra Agent 在一次 run 中完成了 41 份财务文件的 tie-out，把逐项核对结果交给人工复核。这能说明 Astra 已被放进真实专业工作流里，但还不能替代独立评测。[1][3]

**为什么重要：** 9 月 1 日那条还是“跨线后先上锁”；到 9 月 3 日已经变成“critical cyber model 开始广泛部署，但监控边界也更紧张”。能力释放、上线状态和治理代价这次一起变了。

## Agent 架构｜0 条

本轮没有独立新增正式架构事件。更值得继续跟的是，模型和企业产品都在把监控、审批、review gate 和执行留痕往默认控制面里搬。

## AI 产品｜1 条

### OpenAI：企业 agent 落地开始收敛成一条执行范式

这是一条 catch-up：正文实际发布时间是 9 月 1 日，但本轮才在新候选里完成核验。OpenAI 的 workflow 总结和 Gilbert + Tobin 案例，把 enterprise agent 的骨架说得更具体了：Basis 把 onboarding 做成能后台完成集成配置的 reusable skill；Clay 给每个客户账户配 persistent workspace 和 nightly subagent；Exa 让 Codex 从集成线索走到创建 PR、跑测试和准备周报；Gilbert + Tobin 则把 approved-task guidance、role-based access、Australian data residency 和人工 sign-off 放进 KYC/AML、audit report 与运营流程。[1][5][6]

**为什么重要：** 这不是又一轮“企业都在用 AI”的空话。真正有用的是，OpenAI 和客户案例开始收敛到一套可复用的执行结构：任务定义、上下文持久化、工具接入、测试与证据、人审签核和权限边界。

## AI 宏观｜1 条

### OpenAI：Daybreak 开始从 access program 变成关键基础设施分发渠道

OpenAI 9 月 3 日发布 Daybreak for Frontline Defenders，计划在未来六个月提供 10 亿美元的补贴式 Daybreak access，优先给美国水务、电网、州和地方政府、社区银行、非营利组织和开源维护者。页面还写明，OpenAI 正在和 MS-ISAC 做面向公共部门与水务的 pilot，Daybreak Defense Network 已有 35 个以上合作产品和 partner-operated services，而 Daybreak 现有 approved organizations / workspaces 已超过 2,000。[1][4]

**为什么重要：** frontier cyber model 不再只是少数客户的特殊 access。OpenAI 已经开始把这类能力包装成按行业分发的产品与渠道：补贴、培训、伙伴网络和 sector-specific pilot 一起出现了。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有新增满足模型主题边界和信息增量门槛的高管长文。

## AI 一线实践者观点｜0 条

本轮没有新的实践者原创内容单独进入正式日报。

## 审核但未入选

- Legora 这条被并入 Astra 卡，作为广泛部署后的真实工作流证据，不单独再建一张同主题卡。
- Stampli 与 California youth safety bill 在正文核验后都没有进入今日正式范围：前者发布时间不在本轮窗口内，后者既在窗口外，也仍是 bill 支持声明而非已生效的结构变化。
- `gpt-6-astra` 独立 slug 与 Chip Ganassi 页面都没有恢复到足够稳的正文 / 日期合同：前者 sitemap 命中但 fallback 仍返回 404，后者正文能打开但官方发布日期没在 RSS 或页面正文里恢复出来。
- Simon Willison 的“August newsletter is out”只是赞助者月报公告和主题目录，没有足够的一手正文增量，不进正式 signal。

## 证据边界

- Astra 这条能确认的是 OpenAI 官方写明了 broad deployment、Critical 阈值、全量 tool-using inference misalignment monitoring 和 monitorability 下降趋势；第三方独立复现、默认权限与价格细节仍未在同批材料里完整公开。[1][2]
- Daybreak 这条能确认的是项目发布、10 亿美元补贴承诺、MS-ISAC 试点、35+ partner products / services 与 2,000+ approved organizations / workspaces；不能把六个月内的真实使用量、伙伴效果或跨国扩展写成已经兑现。[1][4]
- 企业工作流这条能确认的是官方案例里描述的对象、动作和 review / sign-off 边界；时间节省、活跃率和 ROI 仍主要来自 OpenAI 或客户自报，不是独立审计。[1][5][6]

## 飞书短版

**一句话结论：** 这轮补进 3 条正式 signal。最关键的是 GPT‑6 Astra 已开始广泛部署，而且 OpenAI 公开承认 CoT 监控更难了。  
**组织判断：** 今天最清楚的一条线是，frontier model 的放量和企业 agent 的落地，都在把监控、权限、测试、人审和分发渠道拉成显式控制面。  
**建议动作：** 把高风险模型放量的日志与审批、Daybreak 式行业分发、以及企业 agent 的 persistent workspace / sign-off 骨架，一起加进后续产品和研究清单。  
**结果：** previous_count=0，new_count=3，updated_count=0，total_count=3。

## Sources

[1] https://openai.com/news/rss.xml
[2] https://r.jina.ai/http://openai.com/index/safety-overview-gpt-6-astra
[3] https://r.jina.ai/http://openai.com/index/legora-financial-statement-review-with-astra
[4] https://r.jina.ai/http://openai.com/index/daybreak-for-frontline-defenders
[5] https://r.jina.ai/http://openai.com/index/ai-native-company-workflows
[6] https://r.jina.ai/http://openai.com/index/gilbert-tobin
'''

run_summary = {
    "run_type": "daily_four_lane_incremental_manual_review",
    "run_at": RUN_AT.isoformat(),
    "deliverable_outcome": "success",
    "scheduler_outcome": "success",
    "window": {
        "timezone": "Asia/Shanghai",
        "start": DISCOVERY_START,
        "end": DISCOVERY_END,
        "incremental_since": None,
    },
    "registered_sources": 111,
    "candidate_queue_count": CANDIDATE_QUEUE_COUNT,
    "new_in_run_count": NEW_IN_RUN_COUNT,
    "reviewed_new_candidates": NEW_IN_RUN_COUNT,
    "editorial_shortlist": 5,
    "previous_count": 0,
    "new_count": 3,
    "updated_count": 0,
    "excluded_count": 5,
    "unreviewed_candidate_count": 0,
    "total_count": len(rows),
    "selected": len(rows),
    "lane_counts": {
        "model": sum(row["topic_lane"] == "model" for row in rows),
        "agent_architecture": sum(row["topic_lane"] == "agent_architecture" for row in rows),
        "ai_product": sum(row["topic_lane"] == "ai_product" for row in rows),
        "ai_macro": sum(row["topic_lane"] == "ai_macro" for row in rows),
    },
    "priority_counts": {key: sum(row["relevance_level"] == key for row in rows) for key in ("P0", "P1", "P2", "P3")},
    "decision_counts": {
        "include": len(rows),
        "watchlist": 0,
    },
    "executive_model_longform": 0,
    "practitioner_statements": 0,
    "cross_day_duplicates_removed": 0,
    "source_status_counts": {
        "selected": 5,
        "candidate_only": 0,
        "checked_no_match": 3,
        "access_blocked": 0,
        "auth_required": 0,
        "mechanical_failure": 0,
        "not_checked": 2,
    },
    "review_breakdown": {
        "selected": 3,
        "related_source_merged": 2,
        "outside_editorial_window": 2,
        "below_formal_bar": 1,
        "date_or_body_unresolved": 2,
    },
    "review_notes": [
        "Reviewed only the 10 true new candidates from daily/2026-09-04/discovery-candidates.json and did not reopen the 126-item carry-forward queue.",
        "Recovered OpenAI publication dates from the official News RSS because direct OpenAI article fetches still returned 403. Recovered article bodies through the public r.jina.ai text mirror where available.",
        "Promoted three formal signals after body review: GPT-6 Astra broad deployment plus reduced CoT monitorability, Daybreak for Frontline Defenders as a sector-targeted distribution channel, and an enterprise workflow pattern card built from the AI-native workflows article with Gilbert + Tobin as supporting evidence.",
        "Merged Legora into the Astra card as deployment evidence instead of creating a second same-theme card; the article gives a bounded workflow example but does not warrant a separate daily headline from the same Astra launch cluster.",
        "Left Stampli and the California youth-safety bill out on publication-window / formal-scope grounds. Left the standalone gpt-6-astra slug and Chip Ganassi page unresolved because the first still failed body recovery and the second still lacked a recovered publication date. Left Simon Willison's newsletter announcement out because the body did not contain a standalone high-value original analysis."
    ],
    "candidate_reviews": [
        {
            "url": "https://openai.com/index/stampli",
            "decision": "checked_no_match",
            "published_at": "2026-08-20T00:00:00Z",
            "reason": "official RSS confirms the page is outside the active editorial window"
        },
        {
            "url": "https://openai.com/index/legora-financial-statement-review-with-astra",
            "decision": "merged_related_source",
            "published_at": "2026-09-03T12:00:00Z",
            "reason": "kept as deployment evidence for the Astra release card rather than a second same-theme card"
        },
        {
            "url": "https://openai.com/index/safety-overview-gpt-6-astra",
            "decision": "selected",
            "published_at": "2026-09-03T00:00:00Z",
            "signal_id": "2026-09-03-openai-gpt6-astra-broad-release-monitorability"
        },
        {
            "url": "https://openai.com/index/chip-ganassi-racing",
            "decision": "not_checked",
            "published_at": None,
            "reason": "body opened through fallback but publication date could not be recovered from official RSS or body-level metadata"
        },
        {
            "url": "https://openai.com/index/supporting-california-bill-advance-ai-youth-safety",
            "decision": "checked_no_match",
            "published_at": "2026-08-31T07:00:00Z",
            "reason": "official RSS places it outside the active window and the page is still a bill-support statement, not an enacted structural policy change"
        },
        {
            "url": "https://openai.com/index/gpt-6-astra",
            "decision": "not_checked",
            "published_at": None,
            "reason": "sitemap discovery only; fallback body still resolves to a 404 page and RSS did not expose a standalone launch entry"
        },
        {
            "url": "https://openai.com/index/ai-native-company-workflows",
            "decision": "selected",
            "published_at": "2026-09-01T17:00:00Z",
            "signal_id": "2026-09-01-openai-enterprise-agent-workflow-pattern"
        },
        {
            "url": "https://openai.com/index/gilbert-tobin",
            "decision": "merged_related_source",
            "published_at": "2026-09-01T01:00:00Z",
            "reason": "used as supporting enterprise case evidence for the workflow-pattern card"
        },
        {
            "url": "https://openai.com/index/daybreak-for-frontline-defenders",
            "decision": "selected",
            "published_at": "2026-09-03T13:15:00Z",
            "signal_id": "2026-09-03-openai-daybreak-frontline-defenders-channel"
        },
        {
            "url": "https://simonwillison.net/2026/Sep/4/august-newsletter/",
            "decision": "checked_no_match",
            "published_at": "2026-09-04T05:54:40Z",
            "reason": "public note only announces a sponsor-only newsletter and topic list; no standalone high-value original analysis was recoverable from the accessible body"
        }
    ],
    "collection_contract": {
        "raw_candidates_in_rolling_window_is_not_increment": True,
        "candidate_queue_count_is_not_new_count": True,
        "sitemap_lastmod_is_not_publication_date": True,
        "feed_titles_require_body_verification": True,
        "http_2xx_is_not_checked_no_match": True,
    },
}


def main() -> None:
    selected = sorted(rows, key=lambda row: (
        PRIORITY_ORDER[row["relevance_level"]],
        LANE_ORDER[row["topic_lane"]],
        row["event_date"],
        row["id"],
    ))
    topics_payload["topics"] = sorted(topics_payload["topics"], key=lambda topic: (
        TOPIC_PRIORITY_ORDER.get(topic["priority"], 99),
        LANE_ORDER[topic["topic_lane"]],
        topic["id"],
    ))

    day = ROOT / "daily" / DATE
    dump(day / "selected.json", selected)
    dump(day / "citation-ledger.json", ledger)
    dump(day / "citations.json", citations)
    dump(day / "daily-brief.md", brief)
    dump(day / "run-summary.json", run_summary)
    dump(ROOT / "content-topics" / DATE / "topics.json", topics_payload)

    print(json.dumps({
        "date": DATE,
        "signals": len(selected),
        "topics": len(topics_payload["topics"]),
        "run_summary": str(day / "run-summary.json"),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
