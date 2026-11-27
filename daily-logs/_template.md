# Daily Log — <27 Nov 2026>

> File name stays `YYYY-MM-DD.md` (e.g. `2026-11-27.md`) so entries sort & parse reliably.
> Dates inside use the readable format: `27 Nov 2026`.

---
**Day:** Mon / Tue / Wed / Thu / Fri / Sat / Sun
**Counts as a day?** Yes / No (bad-day floor met)
**Mood / energy:** (1–10, e.g. `7 — focused`) → used as the sentiment seed
**Total focused time:** (e.g. `5h`)
---

## Activities

> Every activity follows the same shape. Keep `NOTE` free-form (this is the text you'll
> run word2vec/sentiment on). Use the **same labels** every day so the data stays consistent.

### 1. LeetCode
- **TYPE:** leetcode
- **SOURCE:** LeetCode 150 | Grind 75 | NeetCode | contest
- **PIPELINE:** solo | 25-min-rule | re-solve-next-day
- **TOPIC:** arrays / hash map / stack / dp / trees / graphs ...
- **TIME:** (e.g. 25m)
- **DIFFICULTY:** 1–5 (1 = trivial → 5 = very hard)
- **STATUS:** solved / half-solved / looked-at-solution / skipped
- **NOTE:** (free text, 1–3 lines — what tripped you up, what you learned)

### 2. Paper
- **TYPE:** paper
- **SOURCE:** (paper title / arxiv id)
- **PIPELINE:** prereqs → pass1 → pass2 → explain-from-memory → code-core → experiment → writeup
- **PASS REACHED:** pass1 / pass2 / memory-explain / coded / experimented / written
- **TOPIC:** attention / transformers / optimizers / RL / diffusion ...
- **TIME:** (e.g. 1h30m)
- **DIFFICULTY:** 1–5
- **STATUS:** ongoing / done / blocked
- **NOTE:** (free text — what you understood, what was unclear, the one half-right idea)

### 3. Practice site
- **TYPE:** site
- **SOURCE:** deep-ml | torchleet | leetml | statquest | brilliant
- **PIPELINE:** problems-from-scratch | 25-min-rule | videos-in-one-sitting
- **TOPIC:** (e.g. linear regression / backprop / chain rule)
- **TIME:** (e.g. 40m)
- **DIFFICULTY:** 1–5
- **STATUS:** done / stuck / half-done
- **NOTE:** (free text — what you had wrong/half-right)

### 4. Internship / company
- **TYPE:** job
- **SOURCE:** company / role
- **PIPELINE:** application | outreach | follow-up | interview | chat
- **TIME:** (e.g. 30m)
- **STATUS:** sent / replied / scheduled / rejected / no-response
- **NOTE:** (free text)

## What I learned today (the actual takeaway)
- (free-form bullet points — 1–3 lines each)

## What slipped / I'd do differently
- (one honest line)

---
## Why this shape (for later analysis)
- Each activity is a flat, labeled record → easy to parse into a table/dataframe.
- `NOTE` fields are your free-text corpus for **word2vec** (topic clustering) and
  **sentiment analysis** (pair with `MOOD`/`STATUS` for labels).
- `PIPELINE` + `PASS REACHED` let you see which study method actually leads to `STATUS: done`.
