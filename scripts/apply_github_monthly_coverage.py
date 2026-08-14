#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "backfills/2026-07-16_to_2026-08-14_all_signals/source-coverage.json"
CHECKED_AT = "2026-08-14T15:46:54+08:00"
VALID = {"checked_no_match", "selected", "candidate_only", "access_blocked", "auth_required", "mechanical_failure", "not_checked"}
UPDATES = {
    "https://github.com/NVIDIA/NeMo": ("selected", 1, ["2026-08-07-nvidia-nemo-speech-3"], "NeMo Speech 3.0 进入正式 Signal；仓库已拆分并重定向至 NVIDIA-NeMo/Speech。"),
    "https://github.com/a2aproject/A2A": ("checked_no_match", 0, [], "窗口内未发现 GitHub Release；仅代表 Release 通道无候选，不代表提交与讨论无变化。"),
    "https://github.com/openai/openai-agents-python": ("selected", 7, ["2026-07-27-openai-agents-sdk-programmatic-tool-calling", "2026-08-11-openai-agents-sdk-resumable-input-sandbox-guards"], "7 个原始 Release，经正文核验和主题去重后形成 2 条正式 Signal。"),
    "https://github.com/google/adk-python": ("selected", 9, ["2026-07-16-google-adk-cloud-run-sandbox-mcp-agent", "2026-07-30-google-adk-a2a-auth-oauth-command-logs", "2026-08-13-google-adk-model-capability-history-media-tools"], "9 个原始 Release，经正文核验和主题去重后形成 3 条正式 Signal。"),
    "https://github.com/microsoft/agent-framework": ("selected", 10, ["2026-08-13-microsoft-agent-framework-checkpoint-approval-hooks"], "10 个原始 Release；将 checkpoint/resume、Approval state、Hooks 和会话释放合并为 1 条正式 Signal，其余版本降噪。"),
    "https://github.com/langchain-ai/langgraph": ("candidate_only", 6, [], "6 个 Release；当前主要为 TracePolicy、checkpoint 修复和依赖更新，保留候选但未达到正式增量门槛。"),
    "https://github.com/run-llama/llama_index": ("checked_no_match", 0, [], "窗口内未发现 GitHub Release；仅代表 Release 通道无候选。"),
    "https://github.com/crewAIInc/crewAI": ("candidate_only", 17, [], "17 个高频 Release；执行上下文与追踪变化暂缺足够产品/架构增量，未按版本号灌入。"),
    "https://github.com/microsoft/autogen": ("checked_no_match", 0, [], "窗口内未发现 GitHub Release；仅代表 Release 通道无候选。"),
    "https://github.com/browser-use/browser-use": ("candidate_only", 3, [], "3 个 Release 主要为浏览器管理与交互 bugfix，未达到正式 Signal 门槛。"),
    "https://github.com/All-Hands-AI/OpenHands": ("selected", 12, ["2026-08-13-openhands-agent-canvas-context-cost-automation-controls"], "12 个高频 Release，按 Agent Canvas 的上下文、成本、自动化与 readiness 控件合并为 1 条正式 Signal。"),
    "https://github.com/SWE-agent/SWE-agent": ("checked_no_match", 0, [], "窗口内未发现 GitHub Release；仅代表 Release 通道无候选。"),
    "https://blog.google/innovation-and-ai/": ("selected", 5, ["2026-07-22-alphabet-q2-ai-demand-supply-enterprise-adoption", "2026-07-28-google-gemini-managed-agents-hooks-budget-triggers", "2026-07-30-google-gemini-spark-chrome-auto-browse", "2026-08-05-google-deepmind-leadership-model-product-control", "2026-08-12-google-gemini-connected-apps-actions"], "通过官方 Sitemap 定向发现并逐页核验，形成财报采用、Managed Agents、Spark Chrome、DeepMind 组织调整和 Connected Apps 五条正式 Signal。"),
    "https://digital-strategy.ec.europa.eu/en/policies/ai-office": ("selected", 1, ["2026-08-02-eu-ai-act-article-50-transparency-obligations"], "通过 European Commission AI Office 官方页面核验 Article 50 适用日期、义务范围与 Code 合规关系。"),
    "https://openai.com/news/": ("selected", 3, ["2026-07-31-openai-gpt56-efficiency-agent-harness", "2026-08-12-openai-gpt56-sol-luna", "2026-08-12-openai-workspace-agents"], "通过官方正文和索引核验 GPT-5.6 效率、Sol/Luna 更新与 Workspace Agents，并替换两条 Google News 索引。"),
    "https://www.anthropic.com/news": ("selected", 2, ["2026-07-27-anthropic-cognizant-enterprise-delivery", "2026-08-03-anthropic-cyber-eval-incidents"], "逐页核验 Cognizant 企业交付伙伴关系和网络安全评测事故复盘。"),
    "https://aws.amazon.com/about-aws/whats-new/machine-learning/": ("selected", 2, ["2026-08-06-aws-agentcore-runtime-instances", "2026-08-06-aws-agentcore-temporal-policies"], "AWS What's New 官方页确认 AgentCore Runtime Instances 与 Temporal Policies。"),
    "https://huggingface.co/blog": ("selected", 2, ["2026-08-10-meta-muse-glimmer-open-local-agent", "2026-08-13-hf-icml-open-reproductions"], "浏览器核验 Muse Glimmer 生态发布与 ICML Open Reproductions 完整正文。"),
    "https://nvidianews.nvidia.com/": ("selected", 2, ["2026-07-27-ssi-nvidia-vera-rubin-partnership", "2026-08-10-nvidia-ai-compute-financing-500b"], "NVIDIA Newsroom 官方核验 SSI 合作与 AI Compute 融资平台。"),
    "https://newsroom.amd.com/": ("selected", 2, ["2026-07-22-amd-anthropic-2gw-mi450", "2026-08-06-amd-acquire-taalas-inference"], "AMD Newsroom 官方核验 Anthropic 2GW 计划与 Taalas 收购协议。"),
    "https://about.fb.com/news/tag/ai/": ("selected", 1, ["2026-07-24-meta-ai-muse-spark-actions"], "Meta Newsroom 正文确认 Email/Calendar、Slides、Daily Briefing 与部分市场滚动开放。"),
    "https://github.com/MoonshotAI/Kimi-K3": ("selected", 1, ["2026-07-28-kimi-k3-open-frontier-model"], "下载并抽取官方技术报告，核验模型架构、Agentic RL、Sandbox 与开放权重边界。"),
    "https://www.interconnects.ai/": ("selected", 2, ["2026-08-03-nathan-lambert-open-model-artifacts-hub", "2026-08-12-nathan-lambert-ai-textbook-workflow"], "核验 Nathan Lambert 的开放模型采用数据和 AI 教材真实工作流复盘。"),
    "https://simonwillison.net/": ("selected", 2, ["2026-08-04-simon-willison-new-release-of-llm-adds-support-", "2026-08-07-simon-willison-agent-game-model-comparison"], "核验 Simon Willison 的可运行演示、仓库与同任务跨模型案例。"),
    "https://magazine.sebastianraschka.com/": ("selected", 1, ["2026-07-18-sebastian-raschka-reasoning-effort"], "核验 Reasoning Effort、Toggle 与 Token 效率技术分析。"),
    "https://newsletter.pragmaticengineer.com/": ("selected", 2, ["2026-07-28-gergely-orosz-anthropic-verification-bottleneck", "2026-08-12-charity-majors-ai-engineering-practice"], "核验 Anthropic 工程深访和 Charity Majors 完整逐字稿。"),
    "https://www.latent.space/": ("selected", 3, ["2026-07-28-akshay-nathan-chatgpt-work", "2026-08-03-baseten-inference-engineering", "2026-08-11-chai-discovery-bioai-commercialization"], "核验产品负责人、推理工程和 BioAI 商业化三期完整逐字稿。")
}


def main():
    data = json.loads(PATH.read_text())
    found = 0
    for item in data["sources"]:
        if item["url"] not in UPDATES:
            continue
        status, candidate_count, selected_ids, note = UPDATES[item["url"]]
        item.update(
            status=status,
            checked_at=CHECKED_AT,
            candidate_count=candidate_count,
            selected_signal_ids=selected_ids,
            note=note,
            fallback_used="GitHub REST API via gh；服务端裁剪 Release 字段以避免大响应截断。"
        )
        found += 1
    if found != len(UPDATES):
        raise SystemExit(f"coverage URL mismatch: {found}/{len(UPDATES)}")
    status_counts = Counter(x["status"] for x in data["sources"])
    data["counts"] = {"registered": len(data["sources"]), **{s: status_counts[s] for s in sorted(VALID)}}
    channel_ids = list(data["channels"])
    data["channels"] = {
        channel_id: {
            "registered": len(batch := [x for x in data["sources"] if x["channel_id"] == channel_id]),
            **{s: sum(x["status"] == s for x in batch) for s in sorted(VALID)},
        }
        for channel_id in channel_ids
    }
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"updated": found, **data["counts"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
