#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "backfills/2026-05-16_to_2026-08-13_product_leaders/candidates.json"
OUTPUT = ROOT / "product-leader-backfill-2026-05-16-to-2026-08-13.html"


def esc(value):
    return html.escape(str(value or ""))


def main():
    data = json.loads(SOURCE.read_text())
    episodes = data["episodes"]
    main_count = sum(x["window"] == "main_90d" for x in episodes)
    adjacent_count = sum(x["window"] == "adjacent_90_120d" for x in episodes)
    companies = len({x["organization"] for x in episodes})
    cards = []
    for row in episodes:
        topics = "".join(f"<li>{esc(topic)}</li>" for topic in row["confirmed_topics"])
        sources = "".join(
            f'<a href="{esc(item["url"])}" target="_blank" rel="noreferrer">{esc(item["label"])} ↗</a>'
            for item in row.get("related_sources", [])
        )
        window = "90 天主窗口" if row["window"] == "main_90d" else "90—120 天邻近窗口"
        cards.append(f'''<article class="card">
          <div class="meta"><span class="badge">{esc(window)}</span><span>{esc(row['published_at'][:10])}</span><span>{esc(row['organization'])}</span><span>{esc(row['body_evidence_level'])}</span></div>
          <h2>{esc(row['title'])}</h2>
          <p class="person">{esc(row['speaker_name'])} · {esc(row['speaker_role'])}</p>
          <h3>可确认主题</h3><ul>{topics}</ul>
          <p class="boundary"><strong>证据边界：</strong>{esc(row['evidence_boundary'])}</p>
          <div class="links"><a href="{esc(row['url'])}" target="_blank" rel="noreferrer">主来源 ↗</a>{sources}</div>
        </article>''')
    page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI Signal · AI 产品负责人近期回溯</title>
<style>:root{{--bg:#f7f5f2;--paper:#fff;--ink:#292724;--muted:#76716a;--line:#e5e0d8;--accent:#6b5b45}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}main{{width:min(1040px,calc(100% - 32px));margin:42px auto 80px}}a{{color:var(--accent)}}.back{{display:inline-block;margin-bottom:24px;text-decoration:none}}header{{padding:32px;background:var(--paper);border:1px solid var(--line);border-radius:16px}}.eyebrow{{font-size:12px;letter-spacing:.15em;color:var(--muted)}}h1{{margin:8px 0;font-size:34px}}header p{{max-width:820px;color:var(--muted)}}.metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:24px}}.metric{{padding:16px;background:#faf9f7;border:1px solid var(--line);border-radius:12px}}.metric strong{{display:block;font-size:25px}}.audit{{margin:20px 0;padding:20px 24px;border-left:4px solid #b49a72;background:#fffaf1;border-radius:8px}}.grid{{display:grid;gap:16px;margin-top:20px}}.card{{padding:26px;background:var(--paper);border:1px solid var(--line);border-radius:14px}}.meta{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;color:var(--muted);font-size:12px}}.badge{{padding:3px 8px;border-radius:999px;background:#eee8de;color:#5d503e}}h2{{margin:12px 0 4px;font-size:21px}}h3{{margin:18px 0 4px;font-size:13px}}.person,.boundary{{color:var(--muted)}}.links{{display:flex;gap:14px;flex-wrap:wrap;margin-top:14px}}footer{{margin-top:28px;color:var(--muted);font-size:13px}}@media(max-width:700px){{.metrics{{grid-template-columns:1fr 1fr}}h1{{font-size:27px}}}}</style></head><body><main><a class="back" href="./">← 返回 AI Signal 日报</a><header><div class="eyebrow">PRODUCT LEADER SOURCE AUDIT · RECENT BACKFILL</div><h1>AI 产品负责人近期原创内容回溯</h1><p>主窗口：2026-05-16—2026-08-13；邻近窗口：2026-04-16—2026-05-15（Asia/Shanghai）。发布日期由节目页、官方频道、RSS 或 Apple Podcasts 公开元数据确认即可登记候选。没有逐字稿时只保留标题、身份、日期和节目方明确列出的主题，不补写嘉宾观点。</p><div class="metrics"><div class="metric"><strong>{len(episodes)}</strong><span>日期确认节目</span></div><div class="metric"><strong>{main_count}</strong><span>90 天主窗口</span></div><div class="metric"><strong>{adjacent_count}</strong><span>邻近窗口</span></div><div class="metric"><strong>{companies}</strong><span>覆盖组织</span></div></div></header><div class="audit"><strong>证据说明：</strong>Show Notes 和章节只能证明节目方列出的讨论主题；只有逐字稿、正文或可核验演示，才能进一步提炼具体观点、数据和方法。视频、音频和不同平台版本按同一节目去重。</div><section class="grid">{''.join(cards)}</section><footer>个人独立 AI 情报工具；不代表任何公司或机构。生成时间：{esc(data['generated_at'])}。</footer></main></body></html>'''
    OUTPUT.write_text(page)
    print(json.dumps({"output": str(OUTPUT), "episodes": len(episodes), "main_90d": main_count, "adjacent": adjacent_count}, ensure_ascii=False))


if __name__ == "__main__":
    main()
