#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATE="${1:-$(TZ=Asia/Shanghai date +%F)}"
REPO="Kidz0419/ai-signal-intelligence"
PUBLIC_URL="https://kidz0419.github.io/ai-signal-intelligence/"

cd "$ROOT"

for file in \
  "daily/$DATE/selected.json" \
  "daily/$DATE/daily-brief.md" \
  "daily/$DATE/citations.json" \
  "daily/$DATE/citation-ledger.json" \
  "daily/$DATE/run-summary.json"; do
  test -f "$file" || { echo "missing required artifact: $file" >&2; exit 1; }
done

python3 scripts/validate_daily.py "$DATE"
mapfile_dates=()
while IFS= read -r d; do mapfile_dates+=("$d"); done < <(find daily -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | LC_ALL=C sort)
python3 scripts/build_history_store.py --dates "${mapfile_dates[@]}"
python3 tests/test_daily_history.py -v

# Keep the public branch linear and refuse silent overwrite if remote diverged.
git pull --ff-only origin main

git add \
  .gitignore .nojekyll README.md FILTER_RULES_AI_V1.md index.html \
  data/history.json data/history.js data/latest.json data/latest.js \
  scripts tests \
  "daily/$DATE/selected.json" \
  "daily/$DATE/daily-brief.md" \
  "daily/$DATE/citations.json" \
  "daily/$DATE/citation-ledger.json" \
  "daily/$DATE/run-summary.json"

if git diff --cached --quiet; then
  echo "public source already current for $DATE"
else
  git commit -m "data: publish AI Signal daily for $DATE"
  git push origin main
fi

# Confirm GitHub Pages is built and the public dataset exposes this date.
for attempt in 1 2 3 4 5 6 7 8 9 10; do
  pages_status="$(gh api "repos/$REPO/pages" --jq '.status' 2>/dev/null || true)"
  published_date="$(curl -LfsS "$PUBLIC_URL/data/history.json?date=$DATE&attempt=$attempt" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("latest_date", ""))' 2>/dev/null || true)"
  if [[ "$pages_status" == "built" && "$published_date" == "$DATE" ]]; then
    echo "published: $PUBLIC_URL date=$published_date pages=$pages_status"
    exit 0
  fi
  sleep 10
done

echo "push succeeded but public verification did not expose $DATE in time" >&2
exit 1
