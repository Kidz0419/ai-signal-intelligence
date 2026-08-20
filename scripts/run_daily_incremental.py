#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bounded daily AI Signal incremental run.

This collector is intentionally conservative:
- it scans every registered source URL to produce coverage status;
- it probes a representative subset of feed/release adapters for same-window updates;
- it writes a zero-signal day when no probed item clears the inclusion bar.

The script preserves any existing same-day selected/topics artifacts instead of overwriting
manual work, so repeated runs stay merge-safe.
"""
from __future__ import annotations

import argparse
import json
import ssl
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
TZ = ZoneInfo("Asia/Shanghai")
UTC = timezone.utc
USER_AGENT = "AISignalKB/1.0 (+personal research tool; contact: local-runner)"
HTTP_TIMEOUT = 14
MAX_BODY = 120000


def now_cn() -> datetime:
    return datetime.now(TZ)


def iso_cn(dt: datetime) -> str:
    return dt.astimezone(TZ).isoformat(timespec="seconds")


def iso_utc(dt: datetime) -> str:
    return dt.astimezone(UTC).isoformat().replace("+00:00", "Z")


def request_text(url: str, timeout: int = HTTP_TIMEOUT, use_range: bool = True) -> tuple[int, str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    if use_range:
        headers["Range"] = f"bytes=0-{MAX_BODY - 1}"
    req = Request(url, headers=headers)
    with urlopen(req, timeout=timeout, context=ssl.create_default_context()) as resp:
        raw = resp.read(MAX_BODY) if use_range else resp.read()
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.status, raw.decode(charset, "ignore"), resp.geturl()


@dataclass
class SourceStatus:
    channel: str
    name: str
    type: str
    url: str
    status: str
    http_code: str
    final_url: str | None = None
    note: str | None = None

    def as_dict(self) -> dict[str, Any]:
        payload = {
            "channel": self.channel,
            "name": self.name,
            "type": self.type,
            "url": self.url,
            "status": self.status,
            "http_code": self.http_code,
        }
        if self.final_url and self.final_url != self.url:
            payload["final_url"] = self.final_url
        if self.note:
            payload["note"] = self.note
        return payload


def classify_http(channel: str, src: dict[str, Any]) -> SourceStatus:
    url = src["url"]
    name = src["name"]
    typ = src.get("type", "unknown")
    note = None
    try:
        status, _text, final_url = request_text(url)
        if status in (401, 403):
            outcome = "access_blocked"
            if name == "OpenAI News":
                note = "curl 403; registry fallback requires browser or official article/index alternative, so this is not treated as no match."
            elif name == "SEC EDGAR":
                note = "Public endpoint requires official API or compliant User-Agent flow; plain fetch is not treated as no match."
        elif 200 <= status < 300:
            # Connectivity is not editorial inspection. Without parsing a
            # publication date or comparing a stable content hash, a 2xx page
            # must remain not_checked rather than checked_no_match.
            outcome = "not_checked"
            note = "reachable only; publication date/content delta not parsed in this adapter"
        elif status == 429:
            outcome = "mechanical_failure"
            note = "rate limited"
        else:
            outcome = "mechanical_failure"
        return SourceStatus(channel, name, typ, url, outcome, str(status), final_url, note)
    except HTTPError as e:
        code = getattr(e, "code", None)
        if code in (401, 403):
            outcome = "access_blocked"
            if name == "OpenAI News":
                note = "curl 403; registry fallback requires browser or official article/index alternative, so this is not treated as no match."
            elif name == "SEC EDGAR":
                note = "Public endpoint requires official API or compliant User-Agent flow; plain fetch is not treated as no match."
        elif code == 429:
            outcome = "mechanical_failure"
            note = "rate limited"
        else:
            outcome = "mechanical_failure"
        return SourceStatus(channel, name, typ, url, outcome, str(code or "error"), note=note)
    except URLError as e:
        return SourceStatus(channel, name, typ, url, "mechanical_failure", "url_error", note=str(e.reason))
    except Exception as e:  # noqa: BLE001
        return SourceStatus(channel, name, typ, url, "mechanical_failure", type(e).__name__, note=str(e)[:200])


@dataclass
class ProbeItem:
    title: str
    url: str
    published_at: str


@dataclass
class ProbeResult:
    name: str
    adapter: str
    source_url: str
    status: str
    checked_items: int
    recent_items: list[ProbeItem]
    note: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "adapter": self.adapter,
            "source_url": self.source_url,
            "status": self.status,
            "checked_items": self.checked_items,
            "recent_items": [item.__dict__ for item in self.recent_items],
            "note": self.note,
        }


def xml_items_from_feed(url: str, limit: int = 40) -> list[ProbeItem]:
    _status, text, _final_url = request_text(url, use_range=False)
    root = ET.fromstring(text.encode("utf-8"))

    def local(tag: str) -> str:
        return tag.split("}")[-1]

    out: list[ProbeItem] = []
    if local(root.tag) == "rss":
        channel = next((c for c in root if local(c.tag) == "channel"), None)
        if channel is None:
            return out
        for item in [c for c in channel if local(c.tag) == "item"][:limit]:
            vals = {local(c.tag): "".join(c.itertext()).strip() for c in item}
            dt = parsedate_to_datetime(vals["pubDate"]) if vals.get("pubDate") else None
            out.append(ProbeItem(vals.get("title", ""), vals.get("link", ""), iso_utc(dt) if dt else ""))
    elif local(root.tag) == "feed":
        for entry in [c for c in root if local(c.tag) == "entry"][:limit]:
            vals = {local(c.tag): "".join(c.itertext()).strip() for c in entry if local(c.tag) != "link"}
            link = ""
            for c in entry:
                if local(c.tag) == "link" and c.attrib.get("href"):
                    link = c.attrib["href"]
                    break
            raw = vals.get("updated") or vals.get("published")
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00")) if raw else None
            out.append(ProbeItem(vals.get("title", ""), link, iso_utc(dt) if dt else ""))
    return out


def xml_items_from_sitemap(url: str, limit: int = 120) -> list[ProbeItem]:
    """Return lastmod candidates; lastmod is never publication evidence."""
    _status, text, _final_url = request_text(url, use_range=False)
    root = ET.fromstring(text.encode("utf-8"))

    def local(tag: str) -> str:
        return tag.split("}")[-1]

    if local(root.tag) == "sitemapindex":
        children = []
        for node in root:
            loc = next(("".join(c.itertext()).strip() for c in node if local(c.tag) == "loc"), "")
            if loc:
                children.append(loc)
        out: list[ProbeItem] = []
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = [pool.submit(xml_items_from_sitemap, child, limit) for child in children[:50]]
            for fut in as_completed(futures):
                try:
                    out.extend(fut.result())
                except Exception:
                    continue
        return sorted(out, key=lambda item: item.published_at, reverse=True)[:limit]

    out = []
    for node in root:
        if local(node.tag) != "url":
            continue
        vals = {local(c.tag): "".join(c.itertext()).strip() for c in node}
        raw = vals.get("lastmod", "")
        if not raw:
            continue
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=UTC)
        except ValueError:
            continue
        loc = vals.get("loc", "")
        parsed = urlparse(loc)
        path = parsed.path.lower()
        host = parsed.netloc.lower()
        if host.endswith("openai.com") and not path.startswith("/index/"):
            continue
        if host.endswith("anthropic.com") and not path.startswith((
            "/news/", "/research/", "/engineering/"
        )):
            continue
        out.append(ProbeItem(loc, loc, iso_utc(dt)))
    return sorted(out, key=lambda item: item.published_at, reverse=True)[:limit]


def recent_only(items: list[ProbeItem], cutoff_utc: datetime) -> list[ProbeItem]:
    out = []
    for item in items:
        if not item.published_at:
            continue
        dt = datetime.fromisoformat(item.published_at.replace("Z", "+00:00"))
        if dt >= cutoff_utc:
            out.append(item)
    return out


def run_probe(name: str, adapter: str, url: str, cutoff_utc: datetime) -> ProbeResult:
    try:
        items = xml_items_from_sitemap(url) if adapter == "sitemap_lastmod" else xml_items_from_feed(url)
        recent = recent_only(items, cutoff_utc)
        status = "candidate_only" if recent else "checked_no_match"
        note = "lastmod is discovery-only; verify datePublished/body before selection" if adapter == "sitemap_lastmod" else ""
        return ProbeResult(name, adapter, url, status, len(items), recent, note)
    except HTTPError as e:
        if e.code in (401, 403):
            return ProbeResult(name, adapter, url, "access_blocked", 0, [], f"HTTP {e.code}")
        return ProbeResult(name, adapter, url, "mechanical_failure", 0, [], f"HTTP {e.code}")
    except Exception as e:  # noqa: BLE001
        return ProbeResult(name, adapter, url, "mechanical_failure", 0, [], f"{type(e).__name__}: {e}")


def build_brief(date: str, start: datetime, run_at: datetime, previous_count: int, total_count: int, source_counts: Counter, probe_results: list[ProbeResult]) -> str:
    blocked = source_counts.get("access_blocked", 0)
    mech = source_counts.get("mechanical_failure", 0)
    checked = source_counts.get("checked_no_match", 0)
    candidate = source_counts.get("candidate_only", 0)
    probe_lines = "\n".join(
        f"- {p.name}：{p.status}，检查 {p.checked_items} 条最近 feed/release 项。"
        for p in probe_results
    ) or "- 本轮未运行代表性 feed/release 探针。"
    return f"""# AI Signal 日报｜{date}

**窗口：** 北京时间 {start.strftime('%Y-%m-%d %H:%M')} 至 {run_at.strftime('%Y-%m-%d %H:%M')}  
**一句话结论：** 本轮完成 {sum(source_counts.values())} 个主注册信源的连通性审计，并对 {len(probe_results)} 个 Feed、Release 与 Sitemap 通道执行增量发现；候选只进入待核验池，不由机械脚本自动升级为正式 Signal。

## 四主线重点

| 主线 | 数量 | 今日重点 |
|---|---:|---|
| 模型 | 0 | 无达到正式入选门槛的新增事件 |
| Agent 架构 | 0 | 无达到正式入选门槛的新增事件 |
| AI 产品 | 0 | 无达到正式入选门槛的新增事件 |
| AI 宏观 | 0 | 无达到正式入选门槛的新增事件 |

## 模型｜0 条

本窗口没有发现同时满足“官方或原始证据明确、发生在当日窗口内、且对模型能力/价格/部署边界形成实质变化”的新增事件。

## Agent 架构｜0 条

代表性 GitHub Releases / Atom 与技术 feed 巡检后，没有发现落在今日窗口内、并能支撑正式架构卡片的新版本或新工件。

## AI 产品｜0 条

产品 Changelog/Help Center/官方博客的代表性巡检没有发现今日窗口内且证据足够的新工作流、权限边界或真实 UI 变化。

## AI 宏观｜0 条

本窗口没有发现同时满足“结构发生变化、受影响者明确、存在后续可验证指标”的宏观事件。

## 模型大厂高管模型长文 / 访谈｜0 条

本轮没有发现进入正式日报的模型负责人高价值原创长内容更新。

## AI 一线实践者观点｜0 条

本轮没有发现带新数据、真实案例、失败复盘、技术解释或原创框架的一手实践者内容达到正式入选门槛。

## 代表性探针结果

{probe_lines}

## 覆盖与缺口

- 主注册信源连通性状态：not_checked {source_counts.get('not_checked', 0)}（仅可访问、未解析内容变化）、access_blocked {blocked}、mechanical_failure {mech}。
- 日期解析探针状态：checked_no_match {sum(p.status == 'checked_no_match' for p in probe_results)}、candidate_only {sum(p.status == 'candidate_only' for p in probe_results)}。
- OpenAI News / Research 等普通抓取仍可能返回 403；本轮如实记录为 access_blocked，没有把 403 写成无内容。
- X 官方 API 仍未配置 OAuth；只使用公开网页与非 X 替代源，不声称完成闭源或登录墙覆盖。

## 今日判断

1. 早晨窗口天然偏静默，尤其是需要欧美官方正文或产品变更的主线。
2. 代表性 feed/release 巡检没有给出足够强的新证据，因此维持高阈值比凑日报更重要。
3. 本轮主要价值在于确认“没有正式新增”并同步覆盖状态，而不是重复昨日事件。

## 建议行动

- 继续等待同日后续窗口；如果欧美官方源在北京时间白天/晚间发布正式材料，再进入同日合并。
- 对 access_blocked 的关键站点优先准备浏览器或官方 API 替代路径，避免把封锁误判成静默。
- 保持 topics 候选池为空，不自动制造选题。

## 证据边界

- 本轮没有正式入选事件，因此没有外部事实卡片和引用账本条目。
- 结论仅表示“在本次有界代表性巡检中未见达到门槛的新增正式信号”，不代表全网没有任何 AI 动态。

## 飞书短版

**一句话结论：** 本轮完成 {sum(source_counts.values())} 个注册源连通性审计和 {len(probe_results)} 个增量发现探针；候选等待正文与发布日期核验。  
**判断：** 不为数量降标，继续等同日后续窗口。  
**覆盖：** not_checked {source_counts.get('not_checked', 0)}，access_blocked {blocked}，mechanical_failure {mech}；日期解析探针 checked_no_match {sum(p.status == 'checked_no_match' for p in probe_results)}。  
**结果：** previous_count={previous_count}，new_count=0，updated_count=0，total_count={total_count}。
"""


def build_empty_topics(date: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "report_date": date,
        "timezone": "Asia/Shanghai",
        "disclaimer_cn": "个人独立 AI 研究内容，不代表任何公司或机构。",
        "scope_label_cn": f"当日增量 · {date}",
        "source_scope": {"type": "daily", "date": date},
        "topics": [],
    }


def build_empty_ledger() -> dict[str, Any]:
    return {
        "version": 1,
        "grounding_policy": "Each factual claim in daily-brief.md must cite an entry in this independent ledger. Sources are mechanically rendered by ascending id.",
        "sources": [],
    }


def load_json(path: Path, default: Any) -> Any:
    if path.exists():
        return json.loads(path.read_text())
    return default


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args()
    root = args.root

    run_at = now_cn()
    date = run_at.strftime("%Y-%m-%d")
    day_dir = root / "daily" / date
    signal_registry = json.loads((root / "config" / "signal-source-registry.json").read_text())
    person_registry = json.loads((root / "config" / "person-source-registry.json").read_text())

    # Rolling recovery window: if the gateway is down for several days, the
    # next successful run still discovers missed entries instead of looking
    # only at the current calendar day.
    start = run_at - timedelta(hours=80)
    cutoff_utc = start.astimezone(UTC)

    existing_rows = load_json(day_dir / "selected.json", [])
    existing_topics = load_json(day_dir.parent.parent / "content-topics" / date / "topics.json", build_empty_topics(date))
    existing_citations = load_json(day_dir / "citations.json", None)
    existing_ledger = load_json(day_dir / "citation-ledger.json", None)
    existing_brief = (day_dir / "daily-brief.md").read_text() if (day_dir / "daily-brief.md").exists() else None
    existing_run_summary = load_json(day_dir / "run-summary.json", None)
    previous_count = len(existing_rows)

    sources = []
    channel_totals: dict[str, Counter] = {}
    with ThreadPoolExecutor(max_workers=24) as pool:
        futures = []
        for channel in signal_registry["channels"]:
            batch = channel.get("sources", []) + channel.get("additional_sources", [])
            for src in batch:
                futures.append(pool.submit(classify_http, channel["id"], src))
        for fut in as_completed(futures):
            result = fut.result()
            sources.append(result)
            channel_totals.setdefault(result.channel, Counter())[result.status] += 1

    sources.sort(key=lambda s: (s.channel, s.name.lower()))
    status_counts = Counter(s.status for s in sources)

    person_records = []
    for channel in person_registry["channels"]:
        urls = channel.get("sources", [])
        if not urls:
            person_records.append({
                "channel": channel["id"],
                "status": "auth_required" if "auth_required" in channel.get("status", "") else "not_checked",
                "checked": 0,
                "note": channel.get("limitation") or channel.get("alternative") or channel.get("scope", ""),
            })
            continue
        checked = 0
        failures = 0
        for src in urls[: min(4, len(urls))]:
            checked += 1
            if classify_http(channel["id"], src).status == "mechanical_failure":
                failures += 1
        person_records.append({
            "channel": channel["id"],
            "status": "mechanical_failure" if failures == checked and checked else "not_checked",
            "checked": checked,
            "registered": len(urls),
            "note": channel.get("limitation") or channel.get("scope", ""),
        })

    probes = [
        ("Google Innovation & AI RSS", "rss", "https://blog.google/innovation-and-ai/rss/"),
        ("Google Products & Platforms RSS", "rss", "https://blog.google/products-and-platforms/rss/"),
        ("Google Security RSS", "rss", "https://blog.google/security/rss/"),
        ("AWS ML Blog RSS", "rss", "https://aws.amazon.com/blogs/machine-learning/feed/"),
        ("AWS Architecture RSS", "rss", "https://aws.amazon.com/blogs/architecture/feed/"),
        ("AWS Security RSS", "rss", "https://aws.amazon.com/blogs/security/feed/"),
        ("AWS Storage RSS", "rss", "https://aws.amazon.com/blogs/storage/feed/"),
        ("AWS Database RSS", "rss", "https://aws.amazon.com/blogs/database/feed/"),
        ("AWS Public Sector RSS", "rss", "https://aws.amazon.com/blogs/publicsector/feed/"),
        ("AWS Networking RSS", "rss", "https://aws.amazon.com/blogs/networking-and-content-delivery/feed/"),
        ("GitHub Copilot Changelog feed", "rss", "https://github.blog/changelog/label/copilot/feed/"),
        ("Hugging Face Blog", "rss", "https://huggingface.co/blog/feed.xml"),
        ("Simon Willison atom", "atom", "https://simonwillison.net/atom/everything/"),
        ("OpenAI sitemap", "sitemap_lastmod", "https://openai.com/sitemap.xml"),
        ("Anthropic sitemap", "sitemap_lastmod", "https://www.anthropic.com/sitemap.xml"),
        ("Google Blog sitemap", "sitemap_lastmod", "https://blog.google/en-us/sitemap.xml"),
    ]

    # Every concrete GitHub repository in the registry gets a Releases Atom
    # adapter. Organization landing pages are deliberately skipped.
    for channel in signal_registry["channels"]:
        for src in channel.get("sources", []) + channel.get("additional_sources", []):
            parsed = urlparse(src["url"])
            parts = [p for p in parsed.path.split("/") if p]
            if parsed.netloc.lower() == "github.com" and len(parts) == 2:
                repo_url = f"https://github.com/{parts[0]}/{parts[1]}"
                probes.append((f"{src['name']} releases", "atom", repo_url + "/releases.atom"))

    # High-signal product repos not represented as concrete registry repos.
    for name, repo in (
        ("OpenAI Codex", "openai/codex"),
        ("Claude Code", "anthropics/claude-code"),
        ("Kimi Code", "MoonshotAI/kimi-code"),
    ):
        probes.append((f"{name} releases", "atom", f"https://github.com/{repo}/releases.atom"))

    deduped = []
    seen_probe_urls = set()
    for spec in probes:
        if spec[2] in seen_probe_urls:
            continue
        seen_probe_urls.add(spec[2])
        deduped.append(spec)
    probes = deduped
    probe_results = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        future_to_spec = {
            pool.submit(run_probe, name, adapter, url, cutoff_utc): (name, url)
            for name, adapter, url in probes
        }
        for fut in as_completed(future_to_spec):
            try:
                probe_results.append(fut.result())
            except Exception as exc:  # noqa: BLE001
                name, url = future_to_spec[fut]
                probe_results.append(ProbeResult(name, "unknown", url, "mechanical_failure", 0, [], str(exc)[:200]))
    probe_results.sort(key=lambda p: p.name.lower())
    raw_candidates = sum(len(p.recent_items) for p in probe_results)
    unique_candidates = len({item.url for p in probe_results for item in p.recent_items})

    # No formally selected events in this bounded run. Preserve any existing same-day rows if present.
    selected_rows = existing_rows
    total_count = len(selected_rows)
    lane_counts = {
        "model": sum(row.get("topic_lane") == "model" for row in selected_rows),
        "agent_architecture": sum(row.get("topic_lane") == "agent_architecture" for row in selected_rows),
        "ai_product": sum(row.get("topic_lane") == "ai_product" for row in selected_rows),
        "ai_macro": sum(row.get("topic_lane") == "ai_macro" for row in selected_rows),
    }
    priority_counts = {k: sum(row.get("relevance_level") == k for row in selected_rows) for k in ("P0", "P1", "P2", "P3")}

    save_json(day_dir / "selected.json", selected_rows)
    # Never erase a richer editorial artifact on a later mechanical run.
    if existing_citations is None:
        save_json(day_dir / "citations.json", [])
    if existing_ledger is None:
        save_json(day_dir / "citation-ledger.json", build_empty_ledger())
    if existing_brief is None:
        (day_dir / "daily-brief.md").write_text(build_brief(date, start, run_at, previous_count, total_count, status_counts, probe_results))

    existing_discovery = load_json(day_dir / "discovery-candidates.json", {"candidates": []})
    state_path = root / ".cache" / "discovery-state.json"
    state_payload = load_json(state_path, {"timestamps": {}})
    seen_timestamps = state_payload.get("timestamps", {})
    if not seen_timestamps:
        # Migration path: the first upgraded run may already have written a
        # candidate queue before the persistent cursor existed.
        seen_timestamps = {
            f"{item.get('adapter', 'unknown')}|{item.get('url', '')}": item.get("published_or_lastmod_at", "")
            for item in existing_discovery.get("candidates", [])
            if item.get("url")
        }

    discovered_this_run = []
    for probe in probe_results:
        for item in probe.recent_items:
            candidate = {
                "source_name": probe.name,
                "adapter": probe.adapter,
                "source_url": probe.source_url,
                "title": item.title,
                "url": item.url,
                "published_or_lastmod_at": item.published_at,
                "evidence_boundary": (
                    "sitemap lastmod only; verify article datePublished and body"
                    if probe.adapter == "sitemap_lastmod"
                    else "feed/release timestamp; body and inclusion still require editorial verification"
                ),
            }
            state_key = f"{probe.adapter}|{item.url}"
            if seen_timestamps.get(state_key) != item.published_at:
                discovered_this_run.append(candidate)
            seen_timestamps[state_key] = item.published_at

    def keep_queued_candidate(item: dict[str, Any]) -> bool:
        if item.get("adapter") != "sitemap_lastmod":
            return True
        parsed = urlparse(item.get("url", ""))
        path = parsed.path.lower()
        host = parsed.netloc.lower()
        if host.endswith("openai.com"):
            return path.startswith("/index/")
        if host.endswith("anthropic.com"):
            return path.startswith(("/news/", "/research/", "/engineering/"))
        return True

    queued_by_key = {
        (item.get("url"), item.get("published_or_lastmod_at")): item
        for item in existing_discovery.get("candidates", [])
        if keep_queued_candidate(item)
    }
    for item in discovered_this_run:
        queued_by_key[(item["url"], item["published_or_lastmod_at"])] = item
    discovery_candidates = list(queued_by_key.values())
    discovery_candidates.sort(key=lambda x: (x["published_or_lastmod_at"], x["url"]), reverse=True)
    save_json(state_path, {"schema_version": 1, "timestamps": seen_timestamps})
    save_json(day_dir / "discovery-candidates.json", {
        "schema_version": 1,
        "generated_at": iso_cn(run_at),
        "window": {"start": iso_cn(start), "end": iso_cn(run_at), "timezone": "Asia/Shanghai"},
        "candidate_count": len(discovery_candidates),
        "new_in_run_count": len(discovered_this_run),
        "new_candidates": discovered_this_run,
        "candidates": discovery_candidates,
        "contract": {
            "candidate_is_not_signal": True,
            "sitemap_lastmod_is_not_publication_date": True,
            "search_or_feed_title_requires_body_verification": True,
        },
    })

    topics_path = root / "content-topics" / date / "topics.json"
    if topics_path.exists():
        topics_payload = existing_topics
    else:
        topics_payload = build_empty_topics(date)
    save_json(topics_path, topics_payload)

    channel_summary = {}
    for channel in signal_registry["channels"]:
        counts = channel_totals.get(channel["id"], Counter())
        channel_summary[channel["id"]] = {
            key: counts.get(key, 0)
            for key in ("selected", "candidate_only", "checked_no_match", "access_blocked", "auth_required", "mechanical_failure", "not_checked")
        }

    run_summary = {
        "run_type": "daily_four_lane_incremental",
        "run_at": iso_cn(run_at),
        "deliverable_outcome": "success",
        "scheduler_outcome": "success",
        "window": {
            "timezone": "Asia/Shanghai",
            "start": iso_cn(start),
            "end": iso_cn(run_at),
            "incremental_since": None,
        },
        "registered_sources": len(sources),
        "raw_candidates": raw_candidates,
        "unique_candidates": unique_candidates,
        "editorial_shortlist": 0,
        "previous_count": previous_count,
        "new_count": 0,
        "updated_count": 0,
        "excluded_count": 0,
        "unreviewed_candidate_count": raw_candidates,
        "total_count": total_count,
        "selected": total_count,
        "lane_counts": lane_counts,
        "priority_counts": priority_counts,
        "executive_model_longform": sum(row.get("content_type") == "executive_statement" for row in selected_rows),
        "practitioner_statements": sum(row.get("content_type") == "practitioner_statement" for row in selected_rows),
        "cross_day_duplicates_removed": 0,
        "collection_errors": status_counts.get("access_blocked", 0) + status_counts.get("mechanical_failure", 0),
        "source_coverage": {
            "registered": len(sources),
            "status_counts": {key: status_counts.get(key, 0) for key in ("selected", "candidate_only", "checked_no_match", "access_blocked", "auth_required", "mechanical_failure", "not_checked")},
            "channel_counts": channel_summary,
            "records": [s.as_dict() for s in sources],
        },
        "person_source_coverage": {
            "registered_channels": len(person_registry["channels"]),
            "records": person_records,
        },
        "representative_probes": [p.as_dict() for p in probe_results],
        "content_topics": {
            "topic_count": len(topics_payload.get("topics", [])),
            "platform_variants": len(topics_payload.get("topics", [])) * 3,
        },
        "notes": [
            f"{raw_candidates} discovery candidates were found across {len(probe_results)} adapters; they remain unreviewed until publication date and body verification.",
            "A successful HTTP response is recorded as not_checked unless publication dates or content deltas were parsed.",
            "Static pages were not promoted as fresh based on collected_at alone.",
            "OpenAI and other curl-blocked pages are recorded as access_blocked rather than no-match.",
        ],
    }
    save_json(day_dir / "collection-run-summary.json", run_summary)
    if existing_run_summary is None or existing_run_summary.get("run_type") == "daily_four_lane_incremental":
        save_json(day_dir / "run-summary.json", run_summary)
    print(json.dumps({"date": date, "selected": total_count, "topics": len(topics_payload.get("topics", [])), "registered_sources": len(sources), "raw_candidates": raw_candidates}, ensure_ascii=False))


if __name__ == "__main__":
    main()
