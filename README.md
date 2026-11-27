# Documentation

A public record of everything I study. This repo shows the **process**: what I study
every day, which research papers I reproduce (and how), and which websites I use to
practice.

## 📚 At a glance

| 📅 **Daily Logs** | 📄 **Papers** | 🌐 **Learning Sites** | 🗂 **Reference** |
| --- | --- | --- | --- |
| A log for every day I study — what I did, what I learned, what slipped. | Reproductions of research papers, one paper at a time, following a fixed pipeline. | Notes & progress for practice sites (Deep-ML, TorchLeet, LeetML, StatQuest, Brilliant). | All the source/context documents that define the plan and methods. |
| → [`daily-logs/`](daily-logs/) | → [papers section](#-papers) | → [learning sites section](#-learning-sites) | → [`reference/`](reference/) |

---

## 📅 Daily Logs — `daily-logs/`

A short, honest record of each study day in an **analyzable** format (structured labels so
you can run word2vec / sentiment later). Follows the daily plan:
[`reference/Daily-Plan-and-Learning-Map.pdf`](reference/Daily-Plan-and-Learning-Map.pdf).

- Start from [`daily-logs/_template.md`](daily-logs/_template.md).
- Filenames `YYYY-MM-DD.md`; titles use readable dates (e.g. **27 Nov 2026**).
- See [`daily-logs/ANALYSIS.md`](daily-logs/ANALYSIS.md) for how to analyze the logs.

---

## 📄 Papers

I read and **reproduce** papers, not just summarize them. Every paper follows the same
pipeline — see [`reference/paper-pipeline.md`](reference/paper-pipeline.md):

1. **Prerequisites** — fix the one missing concept first.
2. **Pass 1** (15 min) — abstract, figures, conclusion. What problem does it solve?
3. **Pass 2** (1–2 h) — full read; list every unknown term.
4. **From memory** — close it, explain in 5 lines.
5. **Code the core idea only** — the one thing the paper introduced.
6. **Experiment** — run with vs. without the idea, record numbers.
7. **Write-up** — README per paper: summary, code, results, what surprised me.

- The paper-folder template lives in [`reference/paper-template/`](reference/paper-template/).
- 16-week schedule: [`reference/16-week-paper-plan.md`](reference/16-week-paper-plan.md).
- Prerequisite checklist: [`reference/prerequisites.md`](reference/prerequisites.md).

### Paper progress
| Paper | Week | Status | Key result |
| --- | --- | --- | --- |
| *(add first paper)* |  | Not started / In progress / Done |  |

---

## 🌐 Learning Sites

Practice sites that build fluency. For the rotation, rules, and per-site log format see
[`reference/learning-sites-guide.md`](reference/learning-sites-guide.md).

### Site progress (horizontal)
| Site | Purpose | Progress |
| --- | --- | --- |
| [Deep-ML](https://deep-ml.org) | ML/math from scratch | |
| [TorchLeet](https://torch.com) | PyTorch fluency | |
| [LeetML](https://leetml) | ML coding problems | |
| [StatQuest](https://statquest.org) | Concepts, half-right fixes | |
| [Brilliant](https://brilliant.org) | Math (light) | |

---

## 🗂 Reference — `reference/`

All context/source documents (read-only originals + templates/guides):

| File | What it is |
| --- | --- |
| `Daily-Plan-and-Learning-Map.pdf` | The full daily plan + learning dependency map |
| `paper-pipeline.md` | The 7-step process for reproducing each paper |
| `16-week-paper-plan.md` | The 16-week reading list (5 phases) |
| `prerequisites.md` | Prerequisite checklist before papers |
| `inference-plan.md` | The 4-week project plan |
| `paper-template/` | The folder template for each new paper |
| `learning-sites-guide.md` | Rotation, rules & log format for practice sites |

---

## Conventions
- Daily logs: `daily-logs/YYYY-MM-DD.md`, kept short and honest.
- Each paper: use the [`reference/paper-template/`](reference/paper-template/) structure
  (`README.md`, `code/`, `results/`, `notes.md`).
- Learning sites: update the horizontal Site Progress table above.
- Reference files are treated as read-only context — don't edit them in place.

## Status
- [ ] Daily logs started
- [ ] First paper reproduced
- [ ] Learning-site progress entries added
