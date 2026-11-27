#!/usr/bin/env python3
"""quicklog — turn compact pipe-lined notes into a structured daily entry.

One line per activity, pipe-separated. Only the TYPE is required; the rest fall
back to sensible defaults for that type.

Compact format (order):
  TYPE | TOPIC | SOURCE | TIME | DIFFICULTY | STATUS | NOTE

Types: leetcode, python, site, paper, job

Examples:
  python tools/quicklog.py --date 2026-11-27 --line \
      "leetcode | Two Sum | lc150 | 25m | 2 | solved | used a hash map"
  python tools/quicklog.py --date 2026-11-27 --line \
      "site | linear regression | deep-ml | 40m | 3 | done | got shapes wrong first"
  echo "paper | attention | 1706.03762 | 1h30m | 4 | ongoing | pass1 done" | \
      python tools/quicklog.py --date 2026-11-27

Flags:
  --date  YYYY-MM-DD (default: today)
  --line  one activity line (repeatable). If omitted, lines are read from stdin.
  --print  only print the formatted markdown, don't write to a file.
"""

import argparse
import os
import sys
from datetime import datetime

# Windows consoles default to cp1252 and can't print characters like → (U+2192).
for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")

DAILY_DIR = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "daily-logs")
)

# Defaults per activity type (filled in when not provided in the line)
DEFAULTS = {
    "leetcode": {"PIPELINE": "solo → 25-min-rule", "SOURCE": "LeetCode 150"},
    "python":   {"PIPELINE": "solo practice", "SOURCE": "(practice)"},
    "site":     {"PIPELINE": "problems-from-scratch"},
    "paper":    {"PIPELINE": "prereqs → pass1 → pass2 → memory-explain → code-core → experiment",
                 "PASS REACHED": "pass1"},
    "job":      {"PIPELINE": "application → outreach → follow-up"},
}

LABELS = {
    "leetcode": "LeetCode",
    "python": "Python practice",
    "site": "Practice site",
    "paper": "Paper",
    "job": "Internship / company",
}

LINE_ORDER = ["TYPE", "TOPIC", "SOURCE", "TIME", "DIFFICULTY", "STATUS", "NOTE"]
BLOCK_ORDER = ["TYPE", "SOURCE", "PIPELINE", "TOPIC", "TIME",
               "DIFFICULTY", "STATUS", "NOTE"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def infer_type(line):
    low = line.lower()
    if any(k in low for k in
           ["lc", "leet", "two sum", "sorted", "linked list", "dp ",
            "graph", "tree", "array", "hash", "stack", "queue"]):
        return "leetcode"
    if any(k in low for k in
           ["deep-ml", "deepml", "statquest", "brilliant", "torch",
            "leetml", "video", "khan"]):
        return "site"
    if "paper" in low or "arxiv" in low:
        return "paper"
    if any(k in low for k in ["apply", "application", "intern", "follow-up",
                              "recruiter", "outreach"]):
        return "job"
    return "python"


def parse_line(line):
    line = line.strip()
    parts = [p.strip() for p in line.split("|") if p.strip() != ""]
    raw = {}
    for i, p in enumerate(parts):
        if i < len(LINE_ORDER):
            raw[LINE_ORDER[i]] = p
    t = raw.get("TYPE", "").lower()
    if not t or t not in DEFAULTS:
        t = infer_type(line)
        raw["TYPE"] = t
    data = {"TYPE": t}
    data.update(DEFAULTS.get(t, {}))
    for k in ("SOURCE", "TIME", "DIFFICULTY", "STATUS", "NOTE"):
        if raw.get(k):
            data[k] = raw[k]
    if raw.get("TOPIC") and "TOPIC" not in data:
        data["TOPIC"] = raw["TOPIC"]
    return t, data


def format_block(idx, t, data):
    lines = [f"### {idx}. {LABELS.get(t, t.capitalize())}"]
    for k in BLOCK_ORDER:
        if k == "PIPELINE" and t == "paper":
            # put PASS REACHED right after PIPELINE for papers
            lines.append(f"- **{k}:** {data.get(k, '—')}")
            lines.append(f"- **PASS REACHED:** {data.get('PASS REACHED', 'pass1')}")
            continue
        if data.get(k):
            lines.append(f"- **{k}:** {data[k]}")
    return "\n".join(lines)


def day_name(d):
    return DAYS[d.weekday()]


def build_header(d):
    return (
        f"# Daily Log — {d.strftime('%d %b %Y')}\n"
        "\n"
        "---\n"
        f"**Day:** {day_name(d)}\n"
        "**Counts as a day?** Yes\n"
        "**Mood / energy:** (fill: 1–10)\n"
        "**Total focused time:** (fill)\n"
        "---\n"
        "\n"
        "## Activities\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    ap.add_argument("--line", action="append", default=[])
    ap.add_argument("--print", action="store_true", dest="only_print")
    args = ap.parse_args()

    lines = list(args.line)
    if not lines:
        lines = [ln for ln in sys.stdin.read().splitlines() if ln.strip()]
    if not lines:
        ap.error("no activities given")

    d = datetime.strptime(args.date, "%Y-%m-%d").date()
    path = os.path.join(DAILY_DIR, f"{args.date}.md")

    # if the day file already exists and has activity blocks, continue numbering
    base = 0
    existing = None
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            existing = f.read()
        import re
        base = len(re.findall(r"^### \d+\.", existing, re.M))

    blocks = []
    for i, ln in enumerate(lines, base + 1):
        t, data = parse_line(ln)
        blocks.append(format_block(i, t, data))

    md = build_header(d) + "\n\n".join(blocks) + "\n"

    if args.only_print:
        sys.stdout.write(md)
        return

    os.makedirs(DAILY_DIR, exist_ok=True)
    if existing is not None:
        # append new blocks inside the Activities section
        if "## Activities" in existing:
            existing = existing.rstrip() + "\n\n" + "\n\n".join(blocks) + "\n"
        else:
            existing = existing.rstrip() + "\n\n## Activities\n\n" + \
                "\n\n".join(blocks) + "\n"
        with open(path, "w", encoding="utf-8") as f:
            f.write(existing)
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
    print(f"wrote {len(blocks)} activity block(s) -> {os.path.relpath(path)}")


if __name__ == "__main__":
    main()
