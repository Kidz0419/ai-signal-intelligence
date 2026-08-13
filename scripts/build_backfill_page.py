#!/usr/bin/env python3
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "backfills/2026-07-13_to_2026-08-13/selected.json"
OUTPUT = ROOT / "backfill-2026-07-13-to-2026-08-13.html"


def main():
    rows = json.loads(SOURCE.read_text())
    executive = sum(row["content_type"] == "executive_statement" for row in rows)
    practitioner = sum(row["content_type"] == "practitioner_statement" for row in rows)
    cards = []
    for row in rows:
        badge = "模型大厂负责人" if row["content_type"] == "executive_statement" else "AI 一线实践者"
        cards.append(f'''<article class="card">
          <div class="meta"><span class="badge">{badge}</span><span>{html.escape(row['event_date'])}</span><span>{html.escape(row['topic_lane'])}</span></div>
          <h2>{html.escape(row['title'])}</h2>
          <p class="person">{html.escape(row['speaker_name'])} · {html.escape(row['speaker_role'])}</p>
          <h3>核心增量</h3><p>{html.escape(row['new_information'])}</p>
          <h3>证据边界</h3><p class="boundary">{html.escape(row['evidence_boundary'])}</p>
          <a href="{html.escape(row['url'])}" target="_blank" rel="noreferrer">查看一手来源 ↗</a>
        </article>''')
    page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI Signal · 人物观点近一个月回溯</title>
<style>:root{{--bg:#f7f5f2;--paper:#fff;--ink:#292724;--muted:#76716a;--line:#e5e0d8;--accent:#6b5b45}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}main{{width:min(1020px,calc(100% - 32px));margin:42px auto 80px}}a{{color:var(--accent)}}.back{{display:inline-block;margin-bottom:24px;text-decoration:none}}header{{padding:32px;background:var(--paper);border:1px solid var(--line);border-radius:16px}}.eyebrow{{font-size:12px;text-transform:uppercase;letter-spacing:.15em;color:var(--muted)}}h1{{margin:8px 0;font-size:34px}}header p{{max-width:760px;color:var(--muted)}}.metrics{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:24px}}.metric{{padding:16px;background:#faf9f7;border:1px solid var(--line);border-radius:12px}}.metric strong{{display:block;font-size:25px}}.audit{{margin:20px 0;padding:20px 24px;border-left:4px solid #b49a72;background:#fffaf1;border-radius:8px}}.grid{{display:grid;gap:16px;margin-top:20px}}.card{{padding:26px;background:var(--paper);border:1px solid var(--line);border-radius:14px}}.meta{{display:flex;gap:10px;align-items:center;color:var(--muted);font-size:12px}}.badge{{padding:3px 8px;border-radius:999px;background:#eee8de;color:#5d503e}}h2{{margin:12px 0 4px;font-size:21px}}h3{{margin:18px 0 4px;font-size:13px}}.person,.boundary{{color:var(--muted)}}footer{{margin-top:28px;color:var(--muted);font-size:13px}}@media(max-width:650px){{.metrics{{grid-template-columns:1fr}}h1{{font-size:27px}}}}</style></head><body><main><a class="back" href="./">← 返回 AI Signal 日报</a><header><div class="eyebrow">PERSON SOURCE AUDIT · ONE-MONTH BACKFILL</div><h1>人物观点近一个月回溯</h1><p>窗口：2026-07-13 00:00—2026-08-13 17:00（Asia/Shanghai）。本页只收录可核验的一手原创增量，不按职位或知名度补数；它是历史回溯，不会伪装成 8 月 13 日当天新增。</p><div class="metrics"><div class="metric"><strong>{len(rows)}</strong><span>正式入库</span></div><div class="metric"><strong>{executive}</strong><span>模型大厂负责人</span></div><div class="metric"><strong>{practitioner}</strong><span>AI 一线实践者</span></div></div></header><section class="audit"><strong>审计结论：</strong>此前两个栏目为 0，确有信源不足造成的假阴性。旧流程偏重新闻/RSS/官方发布索引，漏掉个人博客、GitHub 原始实验、完整访谈和公开 X Article。当前仍有三类缺口：X 未配置用户 OAuth、YouTube 逐字稿接口受运行环境 IP 限制、中国封闭平台覆盖不完整。</section><section class="grid">{''.join(cards)}</section><footer>个人独立 AI 情报工具，不代表任何公司或机构。详细机器可读数据见 <a href="backfills/2026-07-13_to_2026-08-13/selected.json">selected.json</a>、<a href="backfills/2026-07-13_to_2026-08-13/source-coverage.json">source-coverage.json</a> 与 <a href="backfills/2026-07-13_to_2026-08-13/backfill-report.md">完整报告</a>。</footer></main></body></html>'''
    OUTPUT.write_text(page)
    print(json.dumps({"output": str(OUTPUT), "rows": len(rows)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
