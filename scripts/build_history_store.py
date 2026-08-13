#!/usr/bin/env python3
"""Build an event-unique history store from immutable per-day selected.json files."""
import argparse
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "ref", "source"}


def canonical_url(value: str) -> str:
    if not value:
        return ""
    p = urlsplit(value.strip())
    query = urlencode(sorted((k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if k.lower() not in TRACKING))
    path = re.sub(r"/+", "/", p.path).rstrip("/") or "/"
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), path, query, ""))


def title_key(value: str) -> str:
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value.lower()).strip()


def duplicate_of(candidate, accepted):
    url = canonical_url(candidate.get("canonical_url") or candidate.get("url", ""))
    for existing in accepted:
        if candidate["id"] == existing["id"]:
            return existing
        if url and url == existing.get("canonical_url"):
            return existing
        ratio = SequenceMatcher(None, title_key(candidate["title"]), title_key(existing["title"])).ratio()
        same_org = (candidate.get("source") or "").lower() == (existing.get("source") or "").lower()
        if ratio >= 0.92 or (same_org and ratio >= 0.86):
            return existing
    return None


def build(root: Path, dates):
    accepted = []
    days = []
    duplicate_log = []
    for date in sorted(dates, reverse=True):
        path = root / "daily" / date / "selected.json"
        rows = json.loads(path.read_text()) if path.exists() else []
        ids = []
        for raw in rows:
            item = dict(raw)
            item["demo"] = False
            item["report_date"] = date
            item["event_date"] = item.get("event_date") or (item.get("published_at") or date)[:10]
            item["canonical_url"] = canonical_url(item.get("canonical_url") or item.get("url", ""))
            item["first_seen_date"] = item.get("first_seen_date") or date
            item["last_seen_date"] = date
            item["run_dates"] = sorted(set(item.get("run_dates", []) + [date]))
            existing = duplicate_of(item, accepted)
            if existing:
                existing["last_seen_date"] = max(existing["last_seen_date"], date)
                existing["run_dates"] = sorted(set(existing["run_dates"] + [date]))
                duplicate_log.append({"dropped_id": item["id"], "kept_id": existing["id"], "date": date})
                continue
            accepted.append(item)
            ids.append(item["id"])
        day_rows = [x for x in accepted if x["id"] in ids]
        days.append({
            "date": date,
            "signal_ids": ids,
            "counts": {
                "total": len(ids),
                "P0": sum(x.get("relevance_level") == "P0" for x in day_rows),
                "P1": sum(x.get("relevance_level") == "P1" for x in day_rows),
                "P2": sum(x.get("relevance_level") == "P2" for x in day_rows),
            },
        })
    return {"schema_version": 1, "latest_date": max(dates), "days": days, "signals": accepted, "duplicate_log": duplicate_log}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dates", nargs="+", required=True)
    args = parser.parse_args()
    data = build(args.root, args.dates)
    out = args.root / "data"
    out.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    (out / "history.json").write_text(text)
    (out / "history.js").write_text("window.DAILY_HISTORY = " + text.rstrip() + ";\n")
    latest = next(d for d in data["days"] if d["date"] == data["latest_date"])
    by_id = {s["id"]: s for s in data["signals"]}
    latest_rows = [by_id[x] for x in latest["signal_ids"]]
    (out / "latest.json").write_text(json.dumps(latest_rows, ensure_ascii=False, indent=2) + "\n")
    (out / "latest.js").write_text("window.DAILY_SIGNALS = " + json.dumps(latest_rows, ensure_ascii=False, indent=2) + ";\n")
    print(json.dumps({"days": len(data["days"]), "signals": len(data["signals"]), "duplicates_removed": len(data["duplicate_log"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
