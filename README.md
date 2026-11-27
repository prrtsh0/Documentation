# Documentation

A public record of everything I study. This repo shows the **process**: what I study
every day, and which websites I use to practice. All study-method context lives in
[`reference/`](reference/).

## 📚 At a glance

| 📅 **Daily Logs** | 🌐 **Learning Sites** | 🗂 **Reference** |
| --- | --- | --- |
| A log for every day I study — what I did, what I learned, what slipped. | Notes & progress for practice sites (Deep-ML, TorchLeet, LeetML, StatQuest, Brilliant). | All the source/context documents that define the plan and methods. |
| → [`daily-logs/`](daily-logs/) | → [learning sites section](#-learning-sites) | → [`reference/`](reference/) |

---

## 📅 Daily Logs — `daily-logs/`

A short, honest record of each study day in an **analyzable** format (structured labels so
you can run word2vec / sentiment later). Follows the daily plan:
[`reference/Daily-Plan-and-Learning-Map.pdf`](reference/Daily-Plan-and-Learning-Map.pdf).

- Start from [`daily-logs/_template.md`](daily-logs/_template.md).
- Filenames `YYYY-MM-DD.md`; titles use readable dates (e.g. **27 Nov 2026**).
- See [`daily-logs/ANALYSIS.md`](daily-logs/ANALYSIS.md) for how to analyze the logs.

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

## 🎯 Harada Method — Open Window 64 (AI Engineer)

Goal: **become a job-ready AI Engineer by Dec 31, 2026**. Method: 1 central goal →
8 sub-goals → 64 actions. Full plan: [`reference/harada-method-ai-engineer.md`](reference/harada-method-ai-engineer.md)
· Interactive chart: [`reference/harada-chart.html`](reference/harada-chart.html)
· Rendered PNG: [`reference/harada-chart.png`](reference/harada-chart.png).

### Master chart (3×3)

| Pillar 1 · LLM Fundamentals & Inference | Pillar 2 · Embeddings & Vector Databases | Pillar 3 · RAG System Implementation |
| --- | --- | --- |
| Pillar 4 · Prompt Engineering | **🟡 CENTER — BECOME A JOB-READY AI ENGINEER (by Dec 31, 2026)** | Pillar 5 · Agents & Tool Use |
| Pillar 6 · Multimodal AI | Pillar 7 · Evaluation & Reliability | Pillar 8 · Deployment & Job-Readiness |

### The 64 actions (8 pillars × 8)

| Pillar | 8 actions |
| --- | --- |
| **1 · LLM Fundamentals & Inference** | Reproduce Self-Attention from scratch · GPT-style block · run 3 hosted models · serve locally (llama.cpp/Ollama) · benchmark HF vs vLLM vs API · sampling note · quantize (GGUF/int8) · read Week-3 attention paper |
| **2 · Embeddings & Vector DBs** | pgvector/Qdrant up · embed 200+ docs · compare chunking · top-k retrieval · reranking · metadata filters · similarity-search demo · pgvector vs Qdrant vs FAISS note |
| **3 · RAG System** | pick messy dataset · ingest pipeline · answer(question) · citations · graceful 'I don't know' · history layer · log every query · README with numbers |
| **4 · Prompt Engineering** | system prompt ×3 · few-shot · retrieval prompt · JSON structured output · edge cases · robustness test · eval-compare · cheat-sheet |
| **5 · Agents & Tools** | 3 tool schemas · agent loop · sandbox (Docker) · tool-call parser · error handling · tool budget · agentic workflow · trajectory logging |
| **6 · Multimodal AI** | Vision API · Whisper · image gen · CLIP · LangChain/LlamaIndex loaders · OCR scanned PDF · vision-augmented retrieval compare · when-it-matters note |
| **7 · Evaluation & Reliability** | 40+ eval harness · trajectory logging · cost/latency per run · tracing/dashboard · 3 before/after changes · eval report · benchmark report · 3 mock system-design interviews |
| **8 · Deployment & Job-Ready** | FastAPI service · auth/RBAC/PII · client integration · deploy live · 5-min demo · case study · resume/GitHub/LinkedIn · 20+ applications |

### 5-week timeline → Dec 31

| Week | Dates | Focus | Exit test |
| --- | --- | --- | --- |
| 1 | Nov 30 – Dec 6 | Foundations, dataset, model baseline | embed 200 docs + top-5 retrieval works |
| 2 | Dec 7 – 13 | Build the RAG core | answer() works end-to-end with citations |
| 3 | Dec 14 – 20 | Evals, agents, multimodal | prove a measurable improvement after a change |
| 4 | Dec 21 – 27 | Deployment, benchmark, demo | service live; self-hosted benchmarked vs API |
| 5 | Dec 28 – 31 | Polish, demo, applications | all "done" checklist items checked |

---

## Conventions
- Daily logs: `daily-logs/YYYY-MM-DD.md`, kept short and honest.
- Learning sites: update the horizontal Site Progress table above.
- Reference files are treated as read-only context — don't edit them in place.

## Status
- [ ] Daily logs started
- [ ] Learning-site progress entries added
