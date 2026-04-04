#!/usr/bin/env python3
"""
x_search.py — X/Twitter search for Claude Code skill (Windows-optimized)

Cross-platform (Windows/Mac/Linux). No curl, no bash escaping issues.

Usage:
    python3 x_search.py "query here"                          # Recent search (last 7 days)
    python3 x_search.py "query" --max 100                     # More results
    python3 x_search.py "query" --sort recency                # Sort by time
    python3 x_search.py "query" --next TOKEN                  # Paginate
    python3 x_search.py "query" --archive                     # Full-archive search (all time)
    python3 x_search.py "query" --archive --since 2025-10-01  # Archive from specific date
    python3 x_search.py "query" --archive --since 2025-10-01 --until 2025-12-31  # Date range
    python3 x_search.py "query" --since 2026-02-01            # Recent with start date
    python3 x_search.py --test                                # Test API connection (recent)
    python3 x_search.py --test-archive                        # Test full-archive access
    python3 x_search.py --estimate "query" --pages 3          # Estimate cost before searching
"""

import sys
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone, timedelta

RECENT_URL = "https://api.x.com/2/tweets/search/recent"
ARCHIVE_URL = "https://api.x.com/2/tweets/search/all"
TWEET_FIELDS = "created_at,public_metrics,author_id,conversation_id,entities"
EXPANSIONS = "author_id"
USER_FIELDS = "username,name,public_metrics"

# Cost estimates (pay-per-use, approximate)
COST_PER_TWEET = 0.005
COST_PER_USER = 0.010


def get_token():
    token = os.environ.get("X_BEARER_TOKEN", "")
    if not token:
        print("ERROR: X_BEARER_TOKEN is not set.", file=sys.stderr)
        print("Run: set X_BEARER_TOKEN=your_token (CMD) or $env:X_BEARER_TOKEN='your_token' (PowerShell)", file=sys.stderr)
        sys.exit(1)
    return token


def api_request(url, token):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "XResearchSkill/2.0"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"ERROR: HTTP {e.code}: {body}", file=sys.stderr)
        if e.code == 401:
            print("Token invalid or expired. Regenerate at developer.x.com", file=sys.stderr)
        elif e.code == 403:
            print("Forbidden. Check credits at console.x.com or endpoint access.", file=sys.stderr)
        elif e.code == 429:
            print("Rate limited. Wait a few minutes and retry.", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Connection failed: {e.reason}", file=sys.stderr)
        sys.exit(1)


def test_connection(token, archive=False):
    endpoint = ARCHIVE_URL if archive else RECENT_URL
    label = "full-archive" if archive else "recent"
    url = f"{endpoint}?query=test&max_results=10&tweet.fields=public_metrics"
    try:
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "XResearchSkill/2.0"
        })
        with urllib.request.urlopen(req) as resp:
            print(f"OK - {label} search API working (HTTP {resp.status})")
            return True
    except urllib.error.HTTPError as e:
        print(f"ERROR: {label} search HTTP {e.code}", file=sys.stderr)
        if e.code == 401:
            print("Token invalid or expired. Regenerate at developer.x.com", file=sys.stderr)
        elif e.code == 403:
            if archive:
                print("Full-archive search not available on your account.", file=sys.stderr)
                print("Check your plan at console.x.com", file=sys.stderr)
            else:
                print("Forbidden. Check credits at console.x.com", file=sys.stderr)
        elif e.code == 429:
            print("Rate limited. Wait a few minutes and retry.", file=sys.stderr)
        return False


def estimate_cost(query, max_results, pages, archive=False):
    """Estimate cost before running a search."""
    total_tweets = max_results * pages
    tweet_cost = total_tweets * COST_PER_TWEET
    # User lookups are deduplicated, estimate ~60% unique authors
    user_cost = int(total_tweets * 0.6) * COST_PER_USER
    total = tweet_cost + user_cost
    endpoint = "full-archive" if archive else "recent (7 days)"

    print(f"=== COST ESTIMATE ===")
    print(f"Endpoint: {endpoint}")
    print(f"Query: {query}")
    print(f"Max results/page: {max_results}")
    print(f"Pages: {pages}")
    print(f"Est. tweets: ~{total_tweets}")
    print(f"Est. tweet reads: ~${tweet_cost:.2f}")
    print(f"Est. user lookups: ~${user_cost:.2f}")
    print(f"Est. TOTAL: ~${total:.2f}")
    print(f"=====================")
    print(f"(Actual cost may vary. Deduplication within 24h reduces cost.)")


def parse_iso_date(date_str):
    """Parse a date string like 2025-10-01 or 2025-10-01T00:00:00Z into ISO format."""
    if not date_str:
        return None
    # If it's already full ISO format
    if "T" in date_str:
        return date_str
    # If it's just a date like 2025-10-01
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        print(f"ERROR: Invalid date format '{date_str}'. Use YYYY-MM-DD or ISO format.", file=sys.stderr)
        sys.exit(1)


def search(query, token, max_results=50, sort_order="relevancy", next_token=None,
           archive=False, since=None, until=None):
    """
    Search tweets. Uses /recent (7 days) or /all (full archive) endpoint.
    """
    base_url = ARCHIVE_URL if archive else RECENT_URL

    # Archive endpoint supports up to 500 results per request
    if archive:
        max_results = min(max_results, 500)
    else:
        max_results = min(max_results, 100)

    params = {
        "query": query,
        "max_results": str(max_results),
        "tweet.fields": TWEET_FIELDS,
        "expansions": EXPANSIONS,
        "user.fields": USER_FIELDS,
    }

    # sort_order is only available on recent search
    if not archive:
        params["sort_order"] = sort_order

    if next_token:
        if archive:
            params["next_token"] = next_token
        else:
            params["pagination_token"] = next_token

    # Date filters
    if since:
        params["start_time"] = parse_iso_date(since)
    if until:
        params["end_time"] = parse_iso_date(until)

    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    # Print search info
    label = "FULL-ARCHIVE" if archive else "RECENT (7d)"
    print(f"[{label}] Searching: {query} (max {max_results})")
    if since or until:
        print(f"  Date range: {since or 'earliest'} -> {until or 'now'}")
    print()

    data = api_request(url, token)

    meta = data.get("meta", {})
    tweets = data.get("data", [])
    users = {u["id"]: u for u in data.get("includes", {}).get("users", [])}

    result_count = meta.get("result_count", 0)
    next_t = meta.get("next_token", "")

    print(f"Results: {result_count} tweets")
    if next_t:
        print(f"Next page: --next {next_t}")
    print("-" * 60)
    print()

    for t in tweets:
        author_id = t.get("author_id", "")
        u = users.get(author_id, {})
        username = u.get("username", "unknown")
        m = t.get("public_metrics", {})
        followers = u.get("public_metrics", {}).get("followers_count", "?")
        likes = m.get("like_count", 0)
        impressions = m.get("impression_count", 0)
        retweets = m.get("retweet_count", 0)
        created = t.get("created_at", "")
        tweet_id = t["id"]

        # Tweet header
        print(f"@{username} ({followers}) | {likes}L {retweets}RT {impressions}I | {created} | https://x.com/{username}/status/{tweet_id}")

        # Tweet text (safe encoding for Windows console)
        text = t.get("text", "")[:400]
        safe_text = text.encode("ascii", errors="replace").decode("ascii")
        print(f"  {safe_text}")

        # URLs
        urls_list = []
        for url_entity in t.get("entities", {}).get("urls", []):
            expanded = url_entity.get("expanded_url", "")
            if expanded:
                urls_list.append(expanded)
        for link in urls_list[:3]:
            print(f"  -> {link}")

        # Thread indicator
        conv_id = t.get("conversation_id", "")
        if conv_id and conv_id != t["id"]:
            print(f"  [part of thread: conversation_id={conv_id}]")

        print()

    # Cost estimate for this request
    est_cost = len(tweets) * COST_PER_TWEET + len(users) * COST_PER_USER
    print(f"--- Est. cost this page: ~${est_cost:.3f} ---")

    return meta


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python3 x_search.py \"query\" [options]")
        print()
        print("Options:")
        print("  --max N              Max results per page (recent: 100, archive: 500)")
        print("  --sort relevancy|recency  Sort order (recent search only)")
        print("  --next TOKEN         Pagination token for next page")
        print("  --archive            Use full-archive search (all time, not just 7 days)")
        print("  --since YYYY-MM-DD   Start date (works with both recent and archive)")
        print("  --until YYYY-MM-DD   End date")
        print("  --test               Test recent search API connection")
        print("  --test-archive       Test full-archive search API access")
        print("  --estimate           Estimate cost (use with --max and --pages)")
        print("  --pages N            Number of pages for cost estimate (default: 1)")
        sys.exit(0)

    token = get_token()

    # Test modes
    if args[0] == "--test":
        test_connection(token, archive=False)
        return
    if args[0] == "--test-archive":
        test_connection(token, archive=True)
        return

    # Parse arguments
    query = None
    max_results = 50
    sort_order = "relevancy"
    next_token = None
    archive = False
    since = None
    until = None
    estimate_mode = False
    pages = 1

    i = 0
    while i < len(args):
        if args[i] == "--max" and i + 1 < len(args):
            max_results = int(args[i + 1])
            i += 2
        elif args[i] == "--sort" and i + 1 < len(args):
            sort_order = args[i + 1]
            i += 2
        elif args[i] == "--next" and i + 1 < len(args):
            next_token = args[i + 1]
            i += 2
        elif args[i] == "--archive":
            archive = True
            i += 1
        elif args[i] == "--since" and i + 1 < len(args):
            since = args[i + 1]
            i += 2
        elif args[i] == "--until" and i + 1 < len(args):
            until = args[i + 1]
            i += 2
        elif args[i] == "--estimate":
            estimate_mode = True
            i += 1
        elif args[i] == "--pages" and i + 1 < len(args):
            pages = int(args[i + 1])
            i += 2
        elif not args[i].startswith("--"):
            query = args[i]
            i += 1
        else:
            i += 1

    if not query:
        print("ERROR: No query provided.", file=sys.stderr)
        sys.exit(1)

    # Auto-detect: if --since is more than 7 days ago, suggest archive
    if since and not archive:
        try:
            since_dt = datetime.strptime(since, "%Y-%m-%d")
            days_ago = (datetime.now() - since_dt).days
            if days_ago > 7:
                print(f"NOTE: --since {since} is {days_ago} days ago. Switching to --archive mode automatically.")
                print()
                archive = True
        except ValueError:
            pass

    if estimate_mode:
        estimate_cost(query, max_results, pages, archive)
        return

    search(query, token, max_results, sort_order, next_token, archive, since, until)


if __name__ == "__main__":
    main()
