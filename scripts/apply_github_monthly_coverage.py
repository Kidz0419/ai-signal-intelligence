#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "backfills/2026-07-16_to_2026-08-14_all_signals/source-coverage.json"
CHECKED_AT = "2026-08-14T15:46:54+08:00"
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
    "https://digital-strategy.ec.europa.eu/en/policies/ai-office": ("selected", 1, ["2026-08-02-eu-ai-act-article-50-transparency-obligations"], "通过 European Commission AI Office 官方页面核验 Article 50 适用日期、义务范围与 Code 合规关系。")
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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"updated": found}, ensure_ascii=False))


if __name__ == "__main__":
    main()
