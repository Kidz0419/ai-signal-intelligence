#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-10"
TZ = ZoneInfo("Asia/Shanghai")
RUN_AT = datetime.now(TZ).replace(microsecond=0)


def dump(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str):
        path.write_text(payload)
    else:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def scores(topic, novelty, significance, strategic, source, model, agent, product, macro, action):
    return {
        "topic_relevance": topic,
        "novelty": novelty,
        "technical_or_product_significance": significance,
        "strategic_value": strategic,
        "source_quality": source,
        "model_value": model,
        "agent_architecture_value": agent,
        "ai_product_value": product,
        "macro_value": macro,
        "actionability": action,
    }


def row(*, id, lane, title, summary, priority, signal_type, content_type,
        information_type, evidence_level, source, url, published_at, tags,
        secondary_tags, why, relevance, opportunity, risk, questions, triggers,
        score_values, evidence_boundary, related_sources=None):
    return {
        "id": id,
        "demo": False,
        "topic_lane": lane,
        "title": title,
        "summary": summary,
        "decision": "include",
        "confidence": score_values.pop("confidence"),
        "relevance_level": priority,
        "signal_type": signal_type,
        "content_type": content_type,
        "information_type": information_type,
        "evidence_level": evidence_level,
        "source": source,
        "url": url,
        "published_at": published_at,
        "primary_tags": tags,
        "secondary_tags": secondary_tags,
        "why_it_matters_cn": why,
        "personal_relevance_cn": relevance,
        "product_opportunity_cn": opportunity,
        "competitive_risk_cn": risk,
        "recommended_action": "investigate" if priority in {"P0", "P1"} else "monitor",
        "questions_to_validate": questions,
        "follow_up_triggers": triggers,
        "scores": scores(**score_values),
        "report_date": DATE,
        "event_date": published_at[:10],
        "canonical_url": url.rstrip("/"),
        "first_seen_date": DATE,
        "last_seen_date": DATE,
        "run_dates": [DATE],
        "evidence_boundary": evidence_boundary,
        "related_sources": related_sources or [],
    }


rows = [
    row(
        id="2026-09-06-openai-automated-research-intern-rsi-controls",
        lane="agent_architecture",
        title="OpenAI 称自动化研究实习生里程碑已达成，但 4–8 小时任务过半仍需人工介入",
        summary="OpenAI 在 9 月 6 日的内部数据报告中称，已经达到“自动化研究实习生”目标：系统可在人类指导下完成原本需要熟练研究者数日的明确任务。到 8 月中旬，研究组织每个人人工作日对应 3.1 个 Agent 工作日；不过，在有可判定结果的成功任务里，超过一半的 4–8 小时任务至少需要一次人工介入。OpenAI 首席科学家 Jakub Pachocki 同日长文把自动化 AI 研究、对齐与监控绑在一起，并主张安全信心不足时减速。",
        priority="P0",
        signal_type="core",
        content_type="executive_statement",
        information_type="agent_runtime",
        evidence_level="primary_statement",
        source="OpenAI / Jakub Pachocki",
        url="https://openai.com/index/research-acceleration-view-inside-openai",
        published_at="2026-09-06T08:00:00Z",
        tags=["OpenAI", "Automated AI Researcher", "RSI"],
        secondary_tags=["Human Steering", "Research Agents", "Safety Controls"],
        why="这批材料第一次把研发 Agent 的组织用量、任务时长、人工介入率和训练暂停放在同一套叙述里。它说明自动化研发不是未来概念，但离无人监督也很远。",
        relevance="对 Agent 产品和控制面设计，最有用的不是“3.1 个 Agent 工作日”这个大数，而是长任务仍频繁需要人工介入，以及人类继续掌握优先级、扩训、暂停和部署决定。",
        opportunity="可把并发任务、干预点、实验证据、环境权限、暂停原因和恢复条件做成研发 Agent 的标准运行记录，而不是只展示最终代码或结论。",
        risk="所有效率和使用数据都来自 OpenAI 内部统计；样本定义、失败任务、真实研究产出和外部可复现性没有独立审计。Jakub 的路线判断是负责人表态，不等于 RSI 已实现。",
        questions=[
            "4–8 小时任务需要人工介入时，最常见的是澄清目标、修复环境、判断结果还是权限升级？",
            "研究环境被加固后，哪些工具、网络和训练权限被收紧，恢复条件如何审计？",
            "OpenAI 所称 2028 年自动化研究员目标将用什么外部可复现指标验收？",
        ],
        triggers=[
            "OpenAI 发布自动化研究实习生的任务集、失败率或独立评测",
            "出现更具体的研究环境权限、暂停、恢复和审计文档",
            "其他模型实验室披露可比较的 AI 研发产出与人工介入数据",
        ],
        score_values=dict(topic=5, novelty=5, significance=5, strategic=5, source=4, model=4, agent=5, product=4, macro=5, action=5, confidence=91),
        evidence_boundary="发布时间由 OpenAI 官方 RSS 确认。数据报告和 Jakub Pachocki 长文均为 OpenAI 一手材料；内部用量、成功率和研发提速尚无独立复核。两篇同日、同主题材料按一个自动化研发事件合并。",
        related_sources=[
            {"url": "https://openai.com/news/rss.xml", "type": "official_rss_date"},
            {"url": "https://openai.com/index/an-alien-mind", "type": "executive_longform_context"},
        ],
    ),
    row(
        id="2026-09-08-openai-chatgpt-images-2-5",
        lane="model",
        title="OpenAI 发布 Images 2.5：多轮局部编辑、Sketch 和双 API 模型同时上线",
        summary="OpenAI 9 月 8 日发布 ChatGPT Images 2.5，并称已向 ChatGPT、ChatGPT Work 和 Codex 全档位滚动开放。产品新增 Sketch、模板和图片评论；API 同时提供 GPT-Image-2.5 Flare 与 Sunburst。官方称相较 Images 2.0，默认 Flare 的延迟降低 50%，多轮编辑和参考图主体保持更稳定。",
        priority="P1",
        signal_type="core",
        content_type="official_release",
        information_type="model_release",
        evidence_level="confirmed",
        source="OpenAI",
        url="https://openai.com/index/introducing-chatgpt-images-2-5",
        published_at="2026-09-08T11:30:00Z",
        tags=["OpenAI", "ChatGPT Images 2.5", "GPT-Image-2.5"],
        secondary_tags=["Sketch", "Multi-turn Editing", "API"],
        why="模型、交互入口和 API 分层在同一批上线。图片生成从一次性出图继续转向可反复局部修改的工作流。",
        relevance="做 AI 产品时可重点验证评论定位、参考图保持和多轮修改是否真的降低返工，而不是只看官方样例。",
        opportunity="围绕局部批注、版本对比、素材锁定和品牌元素保护，可设计更完整的创意审批与资产生产流程。",
        risk="质量、50% 延迟改善和主体保持都来自厂商自报；不同套餐的额度、实际速度和复杂编辑稳定性仍需实测。",
        questions=[
            "图片评论对应的是区域坐标、蒙版还是自然语言引用，能否审计每次修改？",
            "Flare 与 Sunburst 的价格、延迟、分辨率和编辑一致性差异有多大？",
            "多轮编辑在人物、文字和品牌素材上经过多少轮后开始漂移？",
        ],
        triggers=[
            "API 价格、限制和模型卡补充",
            "独立多轮编辑与参考图保持测试",
            "ChatGPT 中出现版本历史、批注协作或企业审批能力",
        ],
        score_values=dict(topic=5, novelty=5, significance=4, strategic=4, source=5, model=5, agent=2, product=5, macro=2, action=5, confidence=94),
        evidence_boundary="发布时间来自 OpenAI 官方 RSS；正文确认产品与 API 已发布。性能和质量提升为 OpenAI 自报，尚未独立复现。",
        related_sources=[{"url": "https://openai.com/news/rss.xml", "type": "official_rss_date"}],
    ),
    row(
        id="2026-09-08-openai-codex-quantum-lab-agent",
        lane="ai_product",
        title="MIT 团队把 Codex 接进量子实验闭环：能连跑测量，也会在弱信号下卡住",
        summary="OpenAI 9 月 8 日案例称，MIT EQuS 团队把 GPT-5.6 Sol/Codex 接到实验室软件，让 Agent 选择参数、运行量子芯片测量、分析数据，并决定是继续细化还是保存结果进入下一步。团队已让 Agent 夜间运行常规测量，研究者可用手机查看和纠偏；弱或噪声信号仍会拖慢任务，并需要有经验的研究者介入。",
        priority="P1",
        signal_type="research",
        content_type="practitioner_statement",
        information_type="product_workflow",
        evidence_level="primary_statement",
        source="OpenAI / MIT EQuS",
        url="https://openai.com/index/codex-quantum-computing-experiments",
        published_at="2026-09-08T17:00:00Z",
        tags=["Codex", "MIT EQuS", "Lab Agent"],
        secondary_tags=["Quantum Calibration", "Skills", "Human Steering"],
        why="这里有完整的感知、分析、决策和再执行闭环，也把失败边界说清楚了：明确流程可以长时间自治，模糊物理信号仍要专家接管。",
        relevance="这类物理世界 Agent 最值得借鉴的是任务限定、远程查看和随时纠偏，而不是简单照搬“无人实验室”叙事。",
        opportunity="可把实验技能、参数范围、异常阈值、手机检查点和人工接管记录做成通用科学 Agent 控制层。",
        risk="案例由 OpenAI 发布，时间节省和常规使用情况来自单一团队自述；没有公开完整运行日志、失败率或安全联锁细节。",
        questions=[
            "Agent 能修改哪些实验参数，硬件和安全边界由软件还是独立联锁限制？",
            "手机查看能否暂停任务、回退参数并确认异常处置？",
            "多 Agent 并发时如何避免资源冲突、错误累积和不可逆实验动作？",
        ],
        triggers=[
            "MIT EQuS 发布技术论文、代码或完整实验日志",
            "出现异常阈值、暂停、回滚或硬件联锁的产品细节",
            "同类科学实验从单团队案例扩展到可复现平台",
        ],
        score_values=dict(topic=5, novelty=5, significance=4, strategic=4, source=4, model=3, agent=5, product=5, macro=2, action=5, confidence=88),
        evidence_boundary="发布时间来自 OpenAI 官方 RSS。正文是 OpenAI 与 MIT 研究者的一手案例，能确认工作流与研究者描述的限制；不能视为独立评测或普遍可复制效果。",
        related_sources=[{"url": "https://openai.com/news/rss.xml", "type": "official_rss_date"}],
    ),
    row(
        id="2026-09-09-kimi-code-0-42-agent-control-plane",
        lane="agent_architecture",
        title="Kimi Code 0.42 把 Remote Control 和多模型池转正，并补上任务进度与会话可靠性",
        summary="Kimi Code 0.42.0 的正式 Release 将 Remote Control、subagent model pool、minidb 会话索引和搜索 worker 从实验开关转为默认能力；新增可分页查看主 Agent 与子 Agent 进度的实验性 Updates 面板、只读 /btw side agent、后台任务模型显示，并修复长会话压缩后恢复错误请求。版本还为未信任项目跳过 MCP server 时增加明确警告。",
        priority="P1",
        signal_type="core",
        content_type="technical_update",
        information_type="agent_governance",
        evidence_level="confirmed",
        source="MoonshotAI / Kimi Code",
        url="https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.42.0",
        published_at="2026-09-09T06:24:42Z",
        tags=["Kimi Code", "Remote Control", "Subagent Model Pool"],
        secondary_tags=["Updates Panel", "MCP Trust", "Session Recovery"],
        why="这不是一次单点 UI 更新。远程控制、模型分工、进度可见性和长会话恢复一起进入更稳定的默认路径，Agent 控制面正在补齐。",
        relevance="可直接对照编码 Agent 的桌面控制设计：谁在运行、用了哪个模型、压缩后恢复哪个请求、未信任项目为何跳过 MCP，都应有明确状态。",
        opportunity="把主/子 Agent 进度、模型、上下文压缩点、远程连接和 MCP 信任状态汇总为可审计任务面板。",
        risk="Updates 面板仍需实验变量开启；Release 没有给出远程控制的权限粒度、认证方式和企业审计字段。",
        questions=[
            "Remote Control 默认开启后，认证、会话撤销和网络暴露边界是什么？",
            "Updates 面板何时转正，能否关联到具体工具调用、失败和人工接管？",
            "上下文压缩恢复修复是否覆盖多任务并发、排队输入和子 Agent 回写？",
        ],
        triggers=[
            "Remote Control 安全文档或管理员控制项发布",
            "Updates 面板转为默认并增加暂停、重试或审计导出",
            "会话恢复与多 Agent 并发出现公开回归测试或复盘",
        ],
        score_values=dict(topic=5, novelty=4, significance=4, strategic=4, source=5, model=1, agent=5, product=4, macro=2, action=5, confidence=94),
        evidence_boundary="GitHub Release API 确认正式版本和发布时间；功能描述来自 Release 与关联 PR。Updates 面板仍为实验能力，不能写成默认上线。",
    ),
    row(
        id="2026-09-09-google-finland-ai-infrastructure-energy",
        lane="ai_macro",
        title="Google 计划两年向芬兰投 130 亿欧元，AI 数据中心开始和核电延寿、风电与储能一起签",
        summary="Google 9 月 9 日宣布，计划在 2027–2028 年向芬兰数字基础设施投入至少 130 亿欧元，覆盖 Hamina、Kajaani、Muhos 和 Vaala 的数据中心及配套设施。配套能源方案包括与 Fortum 签署 22 年 Loviisa 核电站延寿 PPA、把在芬兰签约的新增陆上风电扩至 629MW，以及支持一套计划 2027 年投运的 94MW 电池系统。",
        priority="P1",
        signal_type="strategic_radar",
        content_type="official_release",
        information_type="compute_infrastructure",
        evidence_level="primary_statement",
        source="Google",
        url="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-ai-commitment-to-finland",
        published_at="2026-09-09T07:00:00Z",
        tags=["Google", "Finland", "AI Infrastructure"],
        secondary_tags=["Nuclear PPA", "Wind", "Battery Storage"],
        why="算力扩张和长期电力安排被打成一个项目包。大型模型公司的竞争继续外溢到选址、核电资产、风电和电网灵活性。",
        relevance="做 AI 宏观与产品成本判断时，这类项目比单看 GPU 采购更有用：供给约束已经落到两年建设期和二十多年电力合同。",
        opportunity="持续跟踪区域算力、电价、建设进度和能源合同，可为模型成本、区域可用性和数据驻留判断建立前置指标。",
        risk="130 亿欧元、就业和 GDP 影响均来自 Google 与其委托分析；多数设施仍处于计划或建设前阶段，不能写成算力已经上线。",
        questions=[
            "130 亿欧元中数据中心、网络、土地和能源配套各占多少？",
            "新设施的计算容量、上电时间和 Gemini 训练/推理占比何时披露？",
            "核电延寿、629MW 风电和 94MW 电池能覆盖多少新增负荷？",
        ],
        triggers=[
            "建设许可、开工、上电或具体算力容量公开",
            "Fortum、风电开发商或 Fingrid 披露合同与并网进度",
            "Google 更新欧洲 AI 基础设施资本开支与区域服务能力",
        ],
        score_values=dict(topic=5, novelty=5, significance=5, strategic=5, source=5, model=2, agent=1, product=2, macro=5, action=4, confidence=93),
        evidence_boundary="Google 官方页面与新闻稿确认的是投资计划和已宣布/签署的能源安排。2027–2028 年建设、就业、GDP 和电力效果尚未兑现；两篇同日材料按一个基础设施事件合并。",
        related_sources=[{"url": "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/clean-energy-finland", "type": "energy_contract_details"}],
    ),
    row(
        id="2026-09-09-aws-ray-serve-dlc",
        lane="agent_architecture",
        title="AWS 推出 Ray Serve DLC，为退出维护的 TorchServe 提供受维护的推理容器路径",
        summary="AWS 9 月 9 日发布 Ray Serve Deep Learning Containers，提供面向 EKS、EC2 和 SageMaker 的 CPU/GPU 镜像，把 PyTorch、Ray Serve、FastAPI、Uvicorn 与 GPU 依赖打包为测试组合。官方教程展示了视觉语言模型在单 GPU EKS 节点上的部署，并明确指出 TorchServe 已停止积极维护和安全更新。",
        priority="P2",
        signal_type="core",
        content_type="technical_update",
        information_type="agent_runtime",
        evidence_level="confirmed",
        source="AWS",
        url="https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers",
        published_at="2026-09-09T15:51:29Z",
        tags=["AWS", "Ray Serve DLC", "Model Serving"],
        secondary_tags=["TorchServe", "EKS", "SageMaker"],
        why="受维护的镜像、版本组合和安全补丁路径，比单纯换一个 serving 框架更影响真实迁移成本。",
        relevance="对自建模型或 Agent runtime 团队，这条适合转成迁移清单：镜像、GPU 栈、伸缩、监控和安全补丁分别由谁负责。",
        opportunity="可围绕 TorchServe 迁移评估、兼容性测试、灰度切换和运行监控提供标准化工具或服务。",
        risk="官方教程只覆盖单 GPU 基础部署，没有给出高并发、自动伸缩、回滚、成本和生产故障数据。",
        questions=[
            "Ray Serve DLC 的补丁 SLA、镜像保留和 CVE 响应机制是什么？",
            "从 TorchServe 迁移时模型 handler、批处理和指标如何映射？",
            "EKS 与 SageMaker 版本在伸缩、日志和回滚能力上有何差异？",
        ],
        triggers=[
            "AWS 发布正式迁移指南、兼容矩阵或生产基准",
            "Ray Serve DLC 增加多节点、自动伸缩或可观测性模板",
            "TorchServe 用户公开迁移成本与故障复盘",
        ],
        score_values=dict(topic=4, novelty=4, significance=4, strategic=3, source=5, model=4, agent=4, product=3, macro=2, action=5, confidence=91),
        evidence_boundary="AWS 官方正文和发布日期元数据确认容器与教程已发布。生产性能、迁移成本和安全运维效果没有独立数据。",
    ),
    row(
        id="2026-09-09-ibm-granite-time-series-r2",
        lane="model",
        title="IBM 开源 Granite 时间序列模型 r2：385M 参数、8192 上下文和可复现零样本评测",
        summary="IBM Research 9 月 9 日发布 Granite Time Series PatchTST-FM-r2，开放权重、架构、推理流程和复现代码，并提供 Apache 2.0 / OpenMDW 1.0 双许可。r2 改用结合注意力与时间卷积的 Conformer block，支持 8192 步上下文、99 分位概率预测和缺失值插补。IBM 称其在 GIFT-Eval 可复现零样本模型中综合排名第二，并在宽松商业许可模型中排名第一。",
        priority="P2",
        signal_type="research",
        content_type="official_release",
        information_type="model_release",
        evidence_level="confirmed",
        source="IBM Research / Hugging Face",
        url="https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series",
        published_at="2026-09-09T15:36:24Z",
        tags=["IBM Granite", "Time Series", "Open Weights"],
        secondary_tags=["GIFT-Eval", "Conformer", "Apache 2.0"],
        why="这是少见的可商用、可复现专用基础模型更新，直接覆盖需求、价格、能耗、流量和遥测预测。",
        relevance="对产品团队，价值不在“第二名”本身，而在小模型、零样本、概率输出和宽松许可能否降低每条业务序列单独训练的成本。",
        opportunity="可用公开代码做交易量、商户需求或系统负载的零样本基线，再与现有统计模型和微调模型比较。",
        risk="排行榜筛选口径和领先结论由 IBM 自报；模型对业务分布漂移、长尾序列和在线成本的表现仍需独立测试。",
        questions=[
            "在真实业务数据上，零样本效果与简单统计基线、TimesFM-3 和微调模型差多少？",
            "99 分位输出的校准质量能否支撑库存、容量或风险决策？",
            "双许可在模型衍生、托管服务和数据使用上有哪些差异？",
        ],
        triggers=[
            "GIFT-Eval 排名或复现结果更新",
            "独立业务数据集测试与成本对比",
            "Confluent 流式集成从 Early Access 转为正式可用",
        ],
        score_values=dict(topic=4, novelty=4, significance=4, strategic=3, source=5, model=5, agent=1, product=3, macro=2, action=4, confidence=90),
        evidence_boundary="Hugging Face 上的 IBM Research 原文、模型页和代码确认发布与开放工件。GIFT-Eval 排名和性能比较为 IBM 截至 9 月 8 日的自报口径。",
    ),
]

priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
lane_order = {"model": 0, "agent_architecture": 1, "ai_product": 2, "ai_macro": 3}
rows.sort(key=lambda x: (priority_order[x["relevance_level"]], lane_order[x["topic_lane"]], x["published_at"], x["id"]))

def platform_variants(title, hook, visual, cta_cn, cta_en):
    outline = ["事实与发布日期", "对象、动作与工作流", "证据边界", "产品判断", "验证清单"]
    return {
        "xiaohongshu": {"title": title, "hook": hook, "format": "7页图文卡", "outline": outline, "visual_direction": visual, "cta": cta_cn},
        "twitter": {"title": title, "hook": hook, "format": "6帖 Thread", "outline": outline, "visual_direction": visual, "cta": cta_en},
        "wechat": {"title": title, "hook": hook, "format": "1800—2400字分析", "outline": outline, "visual_direction": visual + "，附证据表", "cta": cta_cn},
    }

def topic(signal_id, title, tension, why_now, audience, boundary, url, priority, lane, hook, visual, cta_cn, cta_en, timeliness="this_week"):
    return {
        "id": f"{DATE}-{signal_id.split('-', 3)[-1]}",
        "status": "candidate",
        "timeliness": timeliness,
        "priority": priority,
        "topic_lane": lane,
        "source_signal_ids": [signal_id],
        "working_title_cn": title,
        "core_tension_cn": tension,
        "why_now_cn": why_now,
        "target_audience_cn": audience,
        "evidence_boundary_cn": boundary,
        "source_urls": [url.rstrip("/")],
        "platforms": platform_variants(title, hook, visual, cta_cn, cta_en),
    }

topics = [
    topic(rows[0]["id"], "OpenAI 说自动化研究实习生已经到了，但长任务过半仍要人救场", "Agent 工作量已经超过人类工时，真正限制自动化研发的却还是干预、环境安全和停止权。", "OpenAI 同日公开内部使用数据与首席科学家的路线长文，首次把研发提速和减速条件摆在一起。", ["AI 研发负责人", "Agent 平台团队", "模型治理研究者"], "内部数据和路线判断均来自 OpenAI，尚无独立复核。", rows[0]["canonical_url"], "A", "agent_architecture", "3.1 个 Agent 工作日听上去很猛，但 4–8 小时成功任务过半仍需人工介入。", "研发闭环与干预点图", "你会把哪一个停止权留给人？", "Which stop condition would you keep human-owned?"),
    topic("2026-09-08-openai-chatgpt-images-2-5", "Images 2.5 真正的新入口不是更会画，而是让人能在图上直接改", "生成模型开始从一次性输出变成可批注、可多轮局部编辑的创意工作台。", "OpenAI 同时上线模型、Sketch、图片评论和两个 API 档位。", ["AI 产品经理", "创意工具团队", "多模态开发者"], "功能已发布；质量和速度数字是厂商自报。", "https://openai.com/index/introducing-chatgpt-images-2-5", "A", "model", "别只盯 50% 延迟。图片评论和多轮局部修改更可能改变真实工作流。", "图片编辑对象与版本流", "你最想先压测哪种局部编辑？", "Which editing failure would you test first?"),
    topic("2026-09-08-openai-codex-quantum-lab-agent", "量子实验 Agent 已经能通宵跑，但弱信号一来还是得叫人", "物理世界 Agent 可以接管明确流程，却不能把模糊结果的责任交给模型。", "MIT EQuS 案例给出了参数选择、测量、分析、再决策和手机纠偏的完整闭环。", ["科学智能产品团队", "Agent 架构师", "实验自动化负责人"], "这是单一团队的一手案例，不是普遍性能结论。", "https://openai.com/index/codex-quantum-computing-experiments", "A", "ai_product", "最有价值的不是“Agent 进实验室”，而是它在哪些信号条件下必须把控制权还给研究者。", "实验闭环与人工接管图", "你会把异常阈值设在哪一层？", "Where would you put the handoff threshold?"),
    topic("2026-09-09-kimi-code-0-42-agent-control-plane", "Kimi Code 0.42 把几个实验开关转正，编码 Agent 的控制面开始像个产品了", "远程控制和多 Agent 分工一旦默认开启，进度、信任状态和会话恢复必须跟上。", "0.42 同时改了 Remote Control、模型池、Updates 面板、MCP 警告和压缩恢复。", ["编码 Agent 产品经理", "开发工具工程师", "企业安全团队"], "正式 Release 可确认默认能力；Updates 面板仍是实验功能。", "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.42.0", "A", "agent_architecture", "真正该看的不是功能数，而是远程控制默认开启后，用户还能不能看清谁在做什么。", "控制面状态与信任边界图", "哪个状态缺失最容易出事故？", "Which missing state is most dangerous?"),
    topic("2026-09-09-google-finland-ai-infrastructure-energy", "Google 的 130 亿欧元芬兰计划，把 AI 算力竞争一路签到了核电站", "模型公司争的已经不只是 GPU，还包括二十多年电力合同和地区电网承载力。", "同日材料把数据中心、核电延寿、629MW 风电和 94MW 储能放在一张项目表里。", ["AI 宏观研究者", "云与算力团队", "能源科技从业者"], "投资与建设多为未来计划，不能写成容量已经上线。", "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-ai-commitment-to-finland", "A", "ai_macro", "130 亿欧元很显眼，但更值得看的是 22 年核电 PPA 和 2027 年才投运的电池。", "算力建设与能源合同时间轴", "你会先盯资本开支还是上电进度？", "Would you track capex or energization first?"),
    topic("2026-09-09-aws-ray-serve-dlc", "TorchServe 停更之后，AWS 想把迁移路径收进一套受维护的 Ray Serve 镜像", "换 serving 框架不难，难的是谁长期负责 CUDA 组合、安全补丁和回滚。", "AWS 新 DLC 已覆盖 EKS、EC2 和 SageMaker，但公开教程仍停在单 GPU。", ["模型平台工程师", "MLOps 团队", "AI 基础设施产品经理"], "产品与教程已发布，生产规模效果没有公开数据。", "https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers", "B", "agent_architecture", "TorchServe 用户真正要迁的不是 API，而是整条依赖和补丁责任链。", "迁移责任矩阵", "你的 serving 栈由谁负责打补丁？", "Who owns patching in your serving stack?"),
    topic("2026-09-09-ibm-granite-time-series-r2", "一个 385M 的开源时间序列模型，可能比大模型更适合先做业务预测", "零样本和宽松许可降低试错成本，但排行榜不能替代自己的业务基线。", "IBM 同时开放权重、架构、推理代码和复现材料。", ["数据产品经理", "预测系统工程师", "开源模型研究者"], "发布与工件可确认；排行榜结论由 IBM 自报。", "https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series", "B", "model", "先别被“SOTA”带跑。真正值得试的是 385M、零样本和 99 分位输出能否打赢你的简单基线。", "模型选择与验证清单", "你会先拿哪类序列做盲测？", "Which time series would you blind-test first?"),
]

topics_payload = {
    "schema_version": 1,
    "report_date": DATE,
    "timezone": "Asia/Shanghai",
    "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。",
    "scope_label_cn": f"当日增量 · {DATE}（含 9 月 6–9 日迟到补录）",
    "source_scope": {"type": "daily", "date": DATE},
    "topics": topics,
}

ledger_sources = [
    (1, "OpenAI News RSS", "https://openai.com/news/rss.xml", "OpenAI", "confirmed"),
    (2, "Research acceleration: The view inside OpenAI", "https://openai.com/index/research-acceleration-view-inside-openai", "OpenAI", "primary_statement"),
    (3, "An Alien Mind", "https://openai.com/index/an-alien-mind", "OpenAI / Jakub Pachocki", "primary_statement"),
    (4, "Introducing ChatGPT Images 2.5", "https://openai.com/index/introducing-chatgpt-images-2-5", "OpenAI", "confirmed"),
    (5, "How GPT-5.6 Sol helps run quantum computing experiments", "https://openai.com/index/codex-quantum-computing-experiments", "OpenAI / MIT EQuS", "primary_statement"),
    (6, "Kimi Code 0.42.0 release", "https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.42.0", "MoonshotAI", "confirmed"),
    (7, "Ray Serve Deep Learning Containers", "https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers", "AWS", "confirmed"),
    (8, "Google AI infrastructure investment in Finland", "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-ai-commitment-to-finland", "Google", "primary_statement"),
    (9, "Google clean energy growth in Finland", "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/clean-energy-finland", "Google", "primary_statement"),
    (10, "IBM Granite Time Series PatchTST-FM-r2", "https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series", "IBM Research / Hugging Face", "confirmed"),
]
ledger = {
    "version": 1,
    "grounding_policy": "Each factual claim in daily-brief.md cites an entry in this ledger. Sources are rendered mechanically by ascending id.",
    "sources": [
        {"id": i, "title": title, "url": url, "publisher": publisher, "evidence_level": level, "accessed": RUN_AT.isoformat()}
        for i, title, url, publisher, level in ledger_sources
    ],
}
citations = [{"id": s["id"], "url": s["url"]} for s in ledger["sources"]]

lane_rows = {lane: [r for r in rows if r["topic_lane"] == lane] for lane in ("model", "agent_architecture", "ai_product", "ai_macro")}
priority_counts = Counter(r["relevance_level"] for r in rows)

brief = f"""# AI Signal 日报｜{DATE}

**窗口：** 北京时间 2026-09-06 16:00 至 2026-09-10 00:00  
**一句话结论：** 本轮 77 个真正新增候选已完成正文与日期核验，合并为 7 个正式 Signal；最值得盯的是 OpenAI 自动化研发的人工接管边界，以及 Google 把 AI 算力扩张和长期能源合同绑在一起。

> 迟到补录说明：7 条事件实际发生于 9 月 6–9 日。本次按真实 `event_date` 入库，没有把 Sitemap `lastmod` 伪装成发布日期。

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | {len(lane_rows['model'])} | Images 2.5；Granite 时间序列模型 r2 |
| Agent 架构 | {len(lane_rows['agent_architecture'])} | 自动化研发干预边界；Kimi Code 控制面；Ray Serve DLC |
| AI 产品 | {len(lane_rows['ai_product'])} | Codex 接入量子实验闭环 |
| AI 宏观 | {len(lane_rows['ai_macro'])} | Google 芬兰算力与能源项目 |

## 模型｜{len(lane_rows['model'])} 条

### P1｜OpenAI 发布 Images 2.5，模型、局部编辑入口和双 API 档位一起上线

Images 2.5 已开始向 ChatGPT、ChatGPT Work 和 Codex 全档位滚动开放，并新增 Sketch、模板和图片评论。API 同时上线 Flare 与 Sunburst 两个模型；OpenAI 自报 Flare 相比 Images 2.0 延迟降低 50%。[1][4]

判断：图片生成继续从一次性出图转成可批注、可多轮局部修改的工作流。质量、速度和主体保持仍需独立压测，尤其要看复杂编辑经过多轮后是否漂移。

### P2｜IBM 开源 Granite 时间序列模型 r2

IBM Research 发布约 385M 参数的 PatchTST-FM-r2，开放权重、架构、推理流程和复现代码，支持 8192 步上下文、99 分位概率预测和缺失值插补。IBM 自报其在 GIFT-Eval 可复现零样本模型中综合第二，在宽松商业许可模型中第一。[10]

判断：这类小型专用基础模型适合直接拿业务序列做盲测。先比较简单统计基线，再谈“SOTA”。

## Agent 架构｜{len(lane_rows['agent_architecture'])} 条

### P0｜OpenAI 称自动化研究实习生目标已达成，但长任务过半仍需人工介入

OpenAI 称已经达到自动化研究实习生里程碑：系统可在人类指导下完成原本需要熟练研究者数日的明确任务。到 8 月中旬，研究组织每个人人工作日对应 3.1 个 Agent 工作日；在可判定结果的成功任务里，超过一半的 4–8 小时任务至少需要一次人工介入。[1][2]

同日，OpenAI 首席科学家 Jakub Pachocki 把自动化 AI 研究、对齐和监控放进同一条路线，并主张在安全信心不足时减速。该判断是负责人表态，不代表 RSI 已经实现。[3]

判断：Agent 工作量已经很大，但控制权仍在人。最该产品化的是干预、环境权限、暂停原因和恢复条件，而不是只展示最终代码。

### P1｜Kimi Code 0.42 把 Remote Control 和多模型池转正

Kimi Code 0.42.0 将 Remote Control、subagent model pool、minidb 会话索引和搜索 worker 从实验开关转为默认能力。版本还加入实验性 Updates 面板、后台任务模型显示、未信任项目跳过 MCP server 的警告，并修复长会话压缩后恢复错误请求。[6]

判断：远程控制和模型分工默认开启后，谁在运行、用了哪个模型、从哪个上下文恢复，都必须成为明确状态。Updates 面板仍是实验能力，不能写成默认上线。

### P2｜AWS 推出 Ray Serve DLC，给 TorchServe 用户一条受维护的迁移路径

AWS 发布面向 EKS、EC2 和 SageMaker 的 Ray Serve Deep Learning Containers，把 PyTorch、Ray Serve、FastAPI、Uvicorn 与 GPU 依赖打包为测试组合。官方教程覆盖单 GPU 部署，同时明确 TorchServe 已停止积极维护和安全更新。[7]

判断：真正的迁移成本在 CUDA 组合、安全补丁、监控和回滚。当前材料还没有高并发或生产故障数据。

## AI 产品｜{len(lane_rows['ai_product'])} 条

### P1｜MIT 团队把 Codex 接入量子实验闭环，也公开了失败边界

MIT EQuS 团队让 GPT-5.6 Sol/Codex 选择测量参数、操作量子芯片、分析结果，并决定继续细化还是保存结果进入下一步。团队称 Agent 已能夜间运行常规测量，研究者可通过手机查看和纠偏；遇到弱或噪声信号时仍需要专家介入。[1][5]

判断：这是一个完整的执行闭环，但不是“无人实验室”。任务范围、异常阈值、硬件联锁和接管记录决定它能否从案例变成产品。

## AI 宏观｜{len(lane_rows['ai_macro'])} 条

### P1｜Google 计划两年向芬兰投 130 亿欧元，并配套长期能源合同

Google 宣布计划在 2027–2028 年向芬兰数字基础设施投入至少 130 亿欧元，覆盖四地数据中心及配套设施。能源方案包括 22 年 Loviisa 核电站延寿 PPA、累计 629MW 新增陆上风电，以及计划 2027 年投运的 94MW 电池系统。[8][9]

判断：这批容量尚未上线。它更像一个前置信号，说明 AI 算力竞争已经深入选址、电网和二十多年期能源合同。

## 模型大厂高管模型长文 / 访谈｜1 条

Jakub Pachocki 的《An Alien Mind》值得保留为路线原文。他区分 goal alignment 与 value alignment，认为 CoT monitoring 的可靠性正在下降，并把自动化 AI 研究、减速条件和第三方安全门槛连在一起。[3]

## AI 一线实践者观点｜1 条

MIT EQuS 研究者 Beatriz Yankelevich 给出的增量很具体：明确测量流程可长时间交给 Agent，模糊物理信号仍需要专家判断；研究者可远程查看并调整方向。[5]

## 候选处置

- 77 个本轮新增候选全部完成正文或官方 Release/API 核验。
- 9 个候选来源合并成 7 个事件：OpenAI 同日自动化研发材料合并 1 次；Google 芬兰基础设施与能源材料合并 1 次。
- 68 个候选未入选：52 个是 Sitemap `lastmod` 重新浮出的旧页面，10 个属于泛案例、普通教程或维护补丁，6 个 Codex alpha Release 没有可判断的变更正文。
- Anthropic Sitemap 的 39 个页面正文日期分布在 5 月 14 日至 8 月 18 日，另有 1 个团队页无发布日期；本轮没有把这些 `lastmod` 当成新事件。

## 建议行动

1. 先拆 OpenAI 研发 Agent 的人工干预点和暂停条件，形成一份可复用的长任务控制面检查表。
2. 实测 Images 2.5 的多轮局部编辑，并用真实业务序列对 Granite r2 做盲测。
3. 对 Google 芬兰项目只跟踪许可、开工、上电和能源合同进度，不把投资计划写成已投产容量。

## 证据边界

- OpenAI 研发提速、MIT 实验效果、Google 经济影响和 IBM 榜单均含厂商或参与方自报，已在正文中归因。
- OpenAI 普通网页抓取返回 403，本轮通过官方 RSS确认发布日期，并通过公开文本镜像核验正文；403 没有被写成无内容。
- 公开材料没有完整披露研发 Agent、量子实验或 Remote Control 的全部权限、日志、暂停和回滚字段。

## 飞书短版

**结论：** 77 个新增候选核验后形成 7 条正式 Signal，P0 1 条、P1 4 条、P2 2 条。  
**最该看：** OpenAI 称自动化研究实习生目标已达成，但 4–8 小时成功任务过半仍需人工介入；Google 的芬兰 AI 基础设施计划则把数据中心和 22 年核电 PPA 放进同一项目。  
**动作：** 先做研发 Agent 干预/暂停检查表，再实测 Images 2.5 和 Granite r2；Google 项目只跟踪实际开工与上电。  
**边界：** 多项指标来自厂商或参与方自报，计划投资不等于已投产。

## Sources

""" + "\n".join(f"[{s['id']}] {s['url']}" for s in ledger["sources"]) + "\n"

# Enrich the practitioner row with required provenance fields.
for item in rows:
    if item["id"] == "2026-09-08-openai-codex-quantum-lab-agent":
        item.update({
            "speaker_name": "Beatriz Yankelevich",
            "speaker_role": "Graduate student, MIT Engineering Quantum Systems Group",
            "speaker_type": "ai_developer",
            "statement_topic": "Agent-controlled quantum measurement workflows and human intervention boundaries",
            "original_source_url": item["canonical_url"],
            "new_information": "Codex can run routine qubit calibration loops for hours, but weak or noisy signals still require expert guidance.",
            "evidence_artifact": "OpenAI case study with a named MIT researcher, workflow description, limitations, and experiment screenshots.",
        })

# Update operational summaries while preserving the full collected source inventory.
def update_summary(payload):
    payload.update({
        "run_at": RUN_AT.isoformat(),
        "deliverable_outcome": "success",
        "scheduler_outcome": payload.get("scheduler_outcome", "success"),
        "editorial_shortlist": 9,
        "previous_count": 0,
        "new_count": len(rows),
        "updated_count": 0,
        "excluded_count": 68,
        "unreviewed_candidate_count": 0,
        "total_count": len(rows),
        "selected": len(rows),
        "lane_counts": dict(Counter(r["topic_lane"] for r in rows)),
        "priority_counts": {p: priority_counts.get(p, 0) for p in ("P0", "P1", "P2", "P3")},
        "executive_model_longform": 1,
        "practitioner_statements": 1,
        "cross_day_duplicates_removed": 0,
        "editorial_merges": 2,
        "editorial_review": {
            "new_in_run_count": 77,
            "reviewed_count": 77,
            "promoted_source_candidates": 9,
            "selected_event_count": len(rows),
            "merged_source_candidates": 2,
            "excluded_count": 68,
            "exclusion_reasons": {
                "stale_or_outside_window_sitemap_lastmod": 52,
                "insufficient_domain_or_editorial_increment": 10,
                "empty_alpha_release_notes": 6,
            },
            "date_policy": "Official RSS, article datePublished, feed timestamp, or GitHub Release API. Sitemap lastmod is discovery-only.",
            "catch_up_policy": "Events retain actual event_date and are labeled as late additions in the 2026-09-10 daily bucket.",
        },
    })
    coverage = payload.get("source_coverage")
    if coverage and coverage.get("records"):
        selected_names = {"AWS Machine Learning Blog", "Google Innovation & AI", "Hugging Face Blog", "OpenAI News"}
        for source_record in coverage["records"]:
            if source_record.get("name") in selected_names:
                source_record["status"] = "selected"
                source_record["note"] = "Content-level verification completed; at least one current-window event selected."
        counts = Counter(r.get("status", "not_checked") for r in coverage["records"])
        for key in ("selected", "candidate_only", "checked_no_match", "access_blocked", "auth_required", "mechanical_failure", "not_checked"):
            coverage["status_counts"][key] = counts.get(key, 0)
        channel_counts = {}
        for r in coverage["records"]:
            ch = r.get("channel", "unknown")
            channel_counts.setdefault(ch, {k: 0 for k in ("selected", "candidate_only", "checked_no_match", "access_blocked", "auth_required", "mechanical_failure", "not_checked")})
            channel_counts[ch][r.get("status", "not_checked")] += 1
        coverage["channel_counts"] = channel_counts
    if payload.get("probe_summary"):
        dispositions = {
            "Anthropic sitemap": ("checked_no_match", "39 dated pages were stale; 1 team page had no publication date. Sitemap lastmod was not used as freshness evidence."),
            "AWS Database RSS": ("checked_no_match", "New database tutorials did not meet the AI Signal domain gate."),
            "AWS ML Blog RSS": ("selected", "Ray Serve DLC selected after article date and body verification."),
            "Google Blog sitemap": ("selected", "Two same-day Finland pages merged into one infrastructure event after datePublished/body verification."),
            "Hugging Face Blog": ("selected", "IBM Granite Time Series r2 selected after model artifact and body verification."),
            "Kimi Code releases": ("selected", "Kimi Code 0.42.0 selected after GitHub Release API/body verification."),
            "OpenAI Agents SDK releases": ("checked_no_match", "v0.22.2 is a maintenance patch below the daily editorial threshold."),
            "OpenAI Codex releases": ("checked_no_match", "Six alpha releases had no substantive release body; they were bundled as non-editorial maintenance."),
            "OpenAI sitemap": ("selected", "Official RSS plus text-mirror fallback verified four current-window sources; older lastmod churn was excluded."),
        }
        for probe in payload["probe_summary"]:
            if probe.get("name") in dispositions:
                probe["status"], probe["note"] = dispositions[probe["name"]]
    return payload

run_summary_path = ROOT / "daily" / DATE / "run-summary.json"
collection_summary_path = ROOT / "daily" / DATE / "collection-run-summary.json"
run_summary = update_summary(json.loads(run_summary_path.read_text()))
collection_summary = update_summary(json.loads(collection_summary_path.read_text()))

dump(ROOT / "daily" / DATE / "selected.json", rows)
dump(ROOT / "daily" / DATE / "citation-ledger.json", ledger)
dump(ROOT / "daily" / DATE / "citations.json", citations)
dump(ROOT / "daily" / DATE / "daily-brief.md", brief)
dump(ROOT / "daily" / DATE / "run-summary.json", run_summary)
dump(ROOT / "daily" / DATE / "collection-run-summary.json", collection_summary)
dump(ROOT / "content-topics" / DATE / "topics.json", topics_payload)

print(json.dumps({
    "date": DATE,
    "selected": len(rows),
    "topics": len(topics),
    "reviewed_new_candidates": 77,
    "merged_source_candidates": 2,
    "excluded": 68,
    "run_at": RUN_AT.isoformat(),
}, ensure_ascii=False))
