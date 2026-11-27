# Daily Logs

A log for every day I study. Keep it honest and short — but **structured the same way
every time**, so we can analyze it later (topics via word2vec, mood via sentiment).

Follow the daily plan in
[`reference/Daily-Plan-and-Learning-Map.pdf`](../reference/Daily-Plan-and-Learning-Map.pdf).
Key rules from that plan:

- **One resource per block.** Never mix sites inside a block.
- **Bad-day floor:** 1 LeetCode problem, 1 hour on the paper, 5 applications, 1 client
  message. If I hit these, the day counts.
- **Gap rule:** if something doesn't click, step down one level and fix the single
  prerequisite (at most 1 day), then come back.

## How to log a day
1. Copy `_template.md` → `YYYY-MM-DD.md` (filename stays machine-friendly; the title inside
   uses the readable date, e.g. **27 Nov 2026**).
2. Fill **only** the activities you actually did — don't pad.
3. Keep the **same labels** (`TYPE`, `SOURCE`, `PIPELINE`, `TOPIC`, `TIME`,
   `DIFFICULTY`, `STATUS`, `NOTE`) so every entry is parseable.
4. Keep `NOTE` free-form — that's the text used for word2vec/sentiment later.

## Log index (newest last)
| Date | Day | Mood | Total time | Activities | Status |
| --- | --- | --- | --- | --- | --- |
| 27 Nov 2026 | Fri | 7 — focused | 4h30m | leetcode, paper, statquest, job | *(example)* |

## Analysis
See [`ANALYSIS.md`](ANALYSIS.md) for how to turn these logs into vectors/sentiment.
