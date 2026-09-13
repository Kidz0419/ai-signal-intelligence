#!/usr/bin/env python3
"""Reconcile 2026-09-14 sitemap lastmod churn against earlier daily discovery artifacts."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-14"
DAY = ROOT / "daily" / DATE


def load(path: Path):
    return json.loads(path.read_text())


def save(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def normalized_url(value: str) -> str:
    return value.rstrip("/")


def prior_seen_dates(url: str) -> list[str]:
    target = normalized_url(url)
    dates: list[str] = []
    for path in sorted((ROOT / "daily").glob("*/discovery-candidates.json")):
        date = path.parent.name
        if date >= DATE:
            continue
        payload = load(path)
        observations = (payload.get("new_candidates") or []) + (payload.get("candidates") or [])
        if any(normalized_url(item.get("url", "")) == target for item in observations):
            dates.append(date)
    return dates


def main() -> None:
    discovery_path = DAY / "discovery-candidates.json"
    summary_path = DAY / "run-summary.json"
    discovery = load(discovery_path)
    summary = load(summary_path)
    observations = discovery.get("new_candidates") or []

    assert len(observations) == 18, len(observations)
    assert all(item.get("adapter") == "sitemap_lastmod" for item in observations)

    reviews = []
    for item in observations:
        dates = prior_seen_dates(item["url"])
        assert dates, item["url"]
        reviews.append(
            {
                "url": item["url"],
                "decision": "cross_run_duplicate",
                "published_at": None,
                "first_seen_date": min(dates),
                "last_seen_before_run": max(dates),
                "reason": "sitemap lastmod changed, but the canonical URL already appeared in an earlier daily discovery artifact; lastmod alone is not publication or body-change evidence",
            }
        )

    discovery["candidate_count"] = 0
    discovery["new_in_run_count"] = 0
    discovery["new_candidates"] = []
    discovery["candidates"] = []
    discovery["cursor_reconciliation"] = {
        "reconciled_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds"),
        "raw_lastmod_observations": len(observations),
        "cross_run_duplicates_removed": len(reviews),
        "true_increment_count": 0,
        "reason": "All observations were previously seen OpenAI sitemap URLs whose lastmod values changed without independent publication or content-hash evidence.",
    }
    save(discovery_path, discovery)

    summary.update(
        {
            "run_type": "daily_four_lane_incremental_cursor_reconciliation",
            "deliverable_outcome": "success",
            "scheduler_outcome": "initial_script_error_recovered",
            "candidate_queue_count": 0,
            "new_in_run_count": 0,
            "reviewed_new_candidates": 0,
            "reviewed_cursor_false_positives": len(reviews),
            "editorial_shortlist": 0,
            "previous_count": 0,
            "new_count": 0,
            "updated_count": 0,
            "excluded_count": 0,
            "unreviewed_candidate_count": 0,
            "total_count": 0,
            "selected": 0,
            "cross_run_candidate_duplicates_removed": len(reviews),
            "review_breakdown": {
                "cross_run_duplicate": len(reviews),
                "selected": 0,
                "watchlist": 0,
                "unresolved": 0,
            },
            "review_notes": [
                "Reconciled only the 18 entries marked new by the collector; the rolling candidate pool was not rescanned.",
                "Every entry was a sitemap_lastmod observation for a canonical URL already present in earlier daily discovery artifacts, so none qualifies as a true cross-run increment.",
                "Body fallbacks were opened for the 18 URLs. Their accessible publication dates were historical or absent; GPT-6 Astra was already represented by stable event 2026-09-03-openai-gpt6-astra-broad-release-monitorability.",
                "The initial publication script committed locally but its first GitHub connection failed with LibreSSL SSL_ERROR_SYSCALL. A later push and three-layer public verification recovered the deliverable.",
            ],
            "candidate_reviews": reviews,
            "collection_contract": {
                "raw_candidates_in_rolling_window_is_not_increment": True,
                "candidate_queue_count_is_not_new_count": True,
                "sitemap_lastmod_is_discovery_only": True,
                "previously_seen_sitemap_url_requires_content_hash_change": True,
                "true_increment_source": "new_in_run_count and new_candidates after cursor reconciliation",
            },
        }
    )
    save(summary_path, summary)

    print(
        json.dumps(
            {
                "date": DATE,
                "raw_lastmod_observations": len(observations),
                "cross_run_duplicates_removed": len(reviews),
                "true_increment_count": 0,
                "selected": 0,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
