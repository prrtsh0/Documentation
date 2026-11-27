# Documentation

A public record of everything I study. The goal of this repo is not to show finished
projects — it's to show the **process**: what I study every day, which research papers I
reproduce (and how), and which websites I use to practice.

## Repo layout

| Folder | What lives here |
| --- | --- |
| [`daily-logs/`](daily-logs/) | A log for every day I study. What I did, what I learned, what slipped. |
| [`papers/`](papers/) | Research paper reproductions. One folder per paper, following a fixed pipeline. |
| [`learning-sites/`](learning-sites/) | Notes and progress for the practice websites (Deep-ML, TorchLeet, LeetML, StatQuest, Brilliant, ...). |
| [`reference/`](reference/) | The source documents that define my plan and methods (read-only). |

## The three kinds of documentation

### 1. Everyday study logs — `daily-logs/`
A short, honest record of each study day. It follows my daily plan
(see [`reference/Daily-Plan-and-Learning-Map.pdf`](reference/Daily-Plan-and-Learning-Map.pdf)):
one resource per block, and the "bad-day floor" (1 LeetCode, 1 paper hour, 5 applications,
1 client message) that makes a day count.

Start from [`daily-logs/_template.md`](daily-logs/_template.md).

### 2. Research paper reproductions — `papers/`
I read and **reproduce** papers, not just summarize them. Every paper follows the same
pipeline from [`reference/paper-pipeline.md`](reference/paper-pipeline.md):

1. Prerequisites — fix the one missing concept before reading.
2. Pass 1 (15 min) — abstract, figures, conclusion; what problem does it solve?
3. Pass 2 (1–2 h) — full read; list every term I don't understand.
4. Close it and explain from memory in 5 lines.
5. Code the **core idea only** (not the whole system).
6. Run an experiment — with vs. without the idea, record the numbers.
7. Write it up in the paper's README: summary, code, results, what surprised me.

The 16-week reading schedule lives in [`reference/16-week-paper-plan.md`](reference/16-week-paper-plan.md).

### 3. Learning websites — `learning-sites/`
Practice sites that build fluency: Deep-ML, TorchLeet, LeetML, StatQuest, Brilliant, and
more. One note per site, tracking what I did, what I got wrong, and what I improved.

## Conventions
- Each paper is its own folder in `papers/` with a README, `code/`, `results/`, and notes.
- Daily logs are named `YYYY-MM-DD.md` in `daily-logs/`.
- Keep entries gap — a daily log is a few bullet points, not an essay.
- Every entry should be a step toward something, or a honest record of what slipped.

## Status
- [ ] Daily logs started
- [ ] First paper reproduced
- [ ] Learning-site notes started
