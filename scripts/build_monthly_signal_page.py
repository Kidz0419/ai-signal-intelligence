#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "backfills/2026-07-16_to_2026-08-14_all_signals"
OUTPUT = ROOT / "monthly-signal-2026-07-16-to-2026-08-14.html"
LANES = {
    "model": "模型",
    "agent_architecture": "Agent 架构",
    "ai_product": "AI 产品",
    "ai_macro": "AI 宏观"
}


def esc(value):
    return html.escape(str(value or ""))


def main():
    rows = json.loads((DIR / "selected.json").read_text())
    summary = json.loads((DIR / "run-summary.json").read_text())
    coverage = json.loads((DIR / "source-coverage.json").read_text())
    pending = sum(x.get("monthly_review_status") == "pending_evidence_reverification" for x in rows)
    cards = []
    for row in reversed(rows):
        status = "待复核旧证据" if row.get("monthly_review_status") == "pending_evidence_reverification" else "证据字段完整"
        cards.append(f'''<article class="card" data-lane="{esc(row['topic_lane'])}">
          <div class="meta"><span class="badge">{esc(LANES[row['topic_lane']])}</span><span>{esc((row.get('event_date') or row.get('published_at',''))[:10])}</span><span>{esc(row.get('relevance_level'))}</span><span>{esc(row.get('evidence_level'))}</span><span>{esc(status)}</span></div>
          <h2>{esc(row['title'])}</h2>
          <p>{esc(row['summary'])}</p>
          <h3>为什么重要</h3><p>{esc(row['why_it_matters_cn'])}</p>
          <h3>证据边界</h3><p class="boundary">{esc(row['evidence_boundary'])}</p>
          <div class="foot"><span>来源层：{esc(row['monthly_origin'])}</span><a href="{esc(row.get('canonical_url') or row.get('url'))}" target="_blank" rel="noreferrer">查看来源 ↗</a></div>
        </article>''')
    buttons = ''.join(f'<button data-lane="{k}">{v} {summary["counts"][k]}</button>' for k,v in LANES.items())
    coverage_rows = ''.join(
        f'<tr><td>{esc(channel)}</td><td>{item["registered"]}</td><td>{item["selected"]}</td><td>{item["candidate_only"]}</td><td>{item["checked_no_match"]}</td><td>{item["access_blocked"] + item["mechanical_failure"]}</td><td>{item["not_checked"]}</td></tr>'
        for channel,item in coverage["channels"].items()
    )
    page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI Signal · 最近 30 天全量回溯</title>
<style>:root{{--bg:#f7f5f2;--paper:#fff;--ink:#292724;--muted:#76716a;--line:#e5e0d8;--accent:#6b5b45;--soft:#faf8f4}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}main{{width:min(1120px,calc(100% - 28px));margin:36px auto 80px}}a{{color:var(--accent)}}.back{{text-decoration:none}}header,.panel{{margin-top:20px;padding:28px;background:var(--paper);border:1px solid var(--line);border-radius:16px}}.eyebrow{{font-size:12px;letter-spacing:.14em;color:var(--muted)}}h1{{margin:7px 0;font-size:34px}}header p{{max-width:850px;color:var(--muted)}}.metrics{{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:22px}}.metric{{padding:15px;background:var(--soft);border:1px solid var(--line);border-radius:12px}}.metric strong{{display:block;font-size:24px}}.audit{{padding:17px 20px;background:#fff8e9;border-left:4px solid #b49a72;border-radius:8px;margin-top:18px}}.filters{{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0}}button{{padding:8px 12px;border:1px solid var(--line);background:var(--paper);border-radius:999px;cursor:pointer;color:var(--ink)}}button.active{{background:#302d29;color:#fff}}.grid{{display:grid;gap:14px}}.card{{padding:24px;background:var(--paper);border:1px solid var(--line);border-radius:14px}}.meta,.foot{{display:flex;gap:9px;flex-wrap:wrap;color:var(--muted);font-size:12px}}.badge{{background:#eee8de;color:#5d503e;padding:2px 8px;border-radius:999px}}h2{{margin:11px 0 7px;font-size:20px}}h3{{margin:16px 0 3px;font-size:13px}}.boundary{{color:var(--muted)}}.foot{{justify-content:space-between;margin-top:15px}}table{{width:100%;border-collapse:collapse;font-size:13px}}th,td{{padding:9px;border-bottom:1px solid var(--line);text-align:left}}th{{color:var(--muted)}}footer{{margin-top:28px;color:var(--muted);font-size:13px}}@media(max-width:780px){{.metrics{{grid-template-columns:repeat(2,1fr)}}.panel{{overflow:auto}}h1{{font-size:27px}}}}</style></head><body><main><a class="back" href="./">← 返回 AI Signal 日报</a><header><div class="eyebrow">30-DAY SIGNAL BACKFILL · COVERAGE AUDIT</div><h1>最近 30 天 AI Signal 全量回溯</h1><p>窗口：2026-07-16—2026-08-14（Asia/Shanghai，首尾均含）。正式 Signal、日期候选和信源覆盖分开统计；扩源提高召回率，不降低正式入选标准。</p><div class="metrics"><div class="metric"><strong>{len(rows)}</strong><span>当前正式基线</span></div><div class="metric"><strong>{summary['counts']['model']}</strong><span>模型</span></div><div class="metric"><strong>{summary['counts']['agent_architecture']}</strong><span>Agent 架构</span></div><div class="metric"><strong>{summary['counts']['ai_product']}</strong><span>AI 产品</span></div><div class="metric"><strong>{summary['counts']['ai_macro']}</strong><span>AI 宏观</span></div><div class="metric"><strong>{coverage['counts']['registered']}</strong><span>注册信源</span></div></div><div class="audit">当前仍有 <strong>{pending}</strong> 条旧日报记录等待一手来源与证据边界复核；在复核结束前，本页属于回溯工作集，而非最终月度结论。</div></header>
<section class="panel"><h2>信源覆盖审计</h2><p>“未检查、访问受限、机械失败”不等于没有新增；“候选”也不计为正式 Signal。</p><table><thead><tr><th>通道</th><th>注册</th><th>入选</th><th>候选</th><th>已查无合格</th><th>受限/失败</th><th>未检查</th></tr></thead><tbody>{coverage_rows}</tbody></table></section>
<div class="filters"><button class="active" data-lane="all">全部 {len(rows)}</button>{buttons}</div><section class="grid">{''.join(cards)}</section><footer>个人独立研究工具，不代表任何公司或机构。厂商自报、负责人陈述和独立验证保持分层。</footer></main><script>document.querySelectorAll('button[data-lane]').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('button').forEach(x=>x.classList.remove('active'));b.classList.add('active');document.querySelectorAll('.card').forEach(c=>c.hidden=b.dataset.lane!=='all'&&c.dataset.lane!==b.dataset.lane)}}));</script></body></html>'''
    OUTPUT.write_text(page)
    print(json.dumps({"output": str(OUTPUT), "signals": len(rows), "registered_sources": coverage["counts"]["registered"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
