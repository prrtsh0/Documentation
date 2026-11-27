# Analyzing your study logs

Each daily log is written as flat, labeled records, which is exactly what you need to run
word2vec and sentiment analysis. Here's the plan.

## What the data looks like
Every activity is a set of consistent fields:
`TYPE`, `SOURCE`, `PIPELINE`, `TOPIC`, `TIME`, `DIFFICULTY`, `STATUS`, `NOTE`.

Plus per-day metadata: `DAY`, `MOOD` (1–10), `TOTAL TIME`, and a free-text
`NOTE`/`what I learned` field.

## Step 1 — Parse logs into a table
Two simple options (both parse the consistent labels):
- A small Python script using `re` to match the `**FIELD:** value` lines and build a
  Pandas DataFrame (one row per activity).
- Or: **YAML frontmatter** (we can migrate to it later if you prefer strict data over
  readability — the current Markdown keeps it human-friendly while being regex-parseable).

## Step 2 — Word2vec (topic & similarity)
- Corpus = all `NOTE` fields (+ `what I learned`).
- Train `gensim.Word2Vec` (or use a pretrained model) over tokenized notes.
- Use it to:
  - Cluster notes into recurring themes (what you actually study most).
  - Find which `TOPIC`s are "similar" to each other.
  - Detect shifts: "did my notes about X get richer over time?"

## Step 3 — Sentiment (mood vs. outcome)
- Label source: `MOOD` (1–10) is your ground-truth sentiment seed.
- Optionally classify `NOTE` text with `TextBlob`/`VADER`.
- Correlate:
  - `MOOD` → `STATUS` (does a low mood correlate with `half-solved`/`blocked`?)
  - Sentiment of notes → `DIFFICULTY` (negative sentiment when difficulty is high?)
  - Mood over time vs. study volume (`TOTAL TIME`, count of activities).

## Step 4 — Pipeline effectiveness (the payoff)
- Group by `PIPELINE` (and `PASS REACHED` for papers).
- Compute "success rate" = share of activities with `STATUS: done/solved`.
- Answer: *which pipeline actually leads to done?* That's the study-method signal.

## Minimal starter (pandas + gensim + textblob)
```python
import glob
import re, pandas as pd
import gensim.downloader as api
from textblob import TextBlob

def parse_log(path):
    txt = open(path, encoding="utf-8").read()
    rows, keys = [], ["TYPE","SOURCE","PIPELINE","TOPIC","TIME",
                      "DIFFICULTY","STATUS","NOTE"]
    for block in re.split(r"\n### ", txt)[1:]:
        row = {}
        for k in keys:
            m = re.search(rf"\*\*{k}:\*\* (.*)", block)
            row[k] = m.group(1).strip() if m else None
        rows.append(row)
    return pd.DataFrame(rows)

# combine all daily-logs/*.md
all_dfs = [parse_log(p) for p in glob.glob("daily-logs/2026-*.md")]
df = pd.concat(all_dfs).dropna(subset=["NOTE"])

# word2vec on notes
wv = api.load("glove-wiki-gigaword-100")
# sentiment
df["sentiment"] = df["NOTE"].apply(lambda n: TextBlob(n).sentiment.polarity)
print(df[["TYPE","TOPIC","STATUS","sentiment"]])
```

> Keep the labels intact and this whole analysis stays runnable with the same script forever.
