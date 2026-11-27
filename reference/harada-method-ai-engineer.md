# Harada Method — AI Engineer Plan (Open Window 64)

> Goal: **Become a job-ready AI Engineer by New Year's Eve 2026 (Dec 31).**
> Method: Harada "Open Window 64" — 1 central goal → 8 sub-goals → 64 actions.
> Start date: Fri 27 Nov 2026 · Finish: Thu 31 Dec 2026 (~5 weeks).

---

## 1. Central Goal (yellow center)

> **"Become a job-ready AI Engineer by Dec 31, 2026."**

**Definition of "done" (verifiable):**
- [ ] One deployed AI project (Support Ops Agent) live behind an API, documented on GitHub
      with architecture, numbers, and failures.
- [ ] An eval harness (40+ test cases) + a benchmark report (API model vs self-hosted model).
- [ ] A 5-minute demo + a written case study a non-engineer understands.
- [ ] Resume + GitHub + LinkedIn rewritten for the AI Engineer role.
- [ ] 3 timed mock system-design interviews completed; 20+ job applications sent.

---

## 2. The 8 Sub-goals (pillars)

Each pillar becomes the center of its own outer grid. 8 pillars × 8 actions = **64 tasks**.

| # | Pillar | Why it supports the central goal |
| --- | --- | --- |
| 1 | LLM Fundamentals & Inference | You must understand how the models you serve actually work |
| 2 | Embeddings & Vector Databases | The retrieval half of every RAG system |
| 3 | RAG System Implementation | The spine project — this IS your portfolio piece |
| 4 | Prompt Engineering | The cheap lever that separates good agents from confused ones |
| 5 | Agents & Tool Use | Modern AI engineering is agent + tool orchestration |
| 6 | Multimodal AI | Vision/audio/embedding APIs broaden the roles you can target |
| 7 | Evaluation & Reliability | Evals are what separate a serious candidate from a chatbot builder |
| 8 | Deployment & Job-Readiness | Serving, security, GitHub, demo, applications |

---

## 3. The 64 Actions

### Pillar 1 — LLM Fundamentals & Inference
1. Reproduce **Self-Attention** (paper 1706.03762) in PyTorch from scratch.
2. Build a small **GPT-style block** (masked attention + MLP) on a toy corpus.
3. Run 3 hosted models (OpenAI, Anthropic, Cohere) and compare token rates + cost/1k.
4. Serve a model locally: **llama.cpp / Ollama** weights + inference script.
5. Benchmark the SAME model across: raw HF pipeline → vLLM/HF → served API.
6. Write a 1-page note on **temperature / top-p / sampling** with concrete examples.
7. Quantize a model (GGUF/int8) and measure quality vs speed trade-off.
8. Read + summarize the 16-week plan paper on attention (Week-3 paper) in `reference/`.

### Pillar 2 — Embeddings & Vector Databases
1. Set up **pgvector** (or Qdrant) locally with a working insert/query loop.
2. Generate embeddings for 200+ messy documents with a BGE / text-embedding model.
3. Implement **chunking** strategies (fixed, recursive, sentence) and compare retrieval quality.
4. Implement a **top-k retrieval** query and inspect what it returns.
5. Add **reranking** (cross-encoder) and measure recall improvement.
6. Store metadata + filters (source, date, tag) in the vector store.
7. Build a tiny similarity-search demo (ask a question → get top 5 chunks).
8. Write a comparison note: pgvector vs Qdrant vs FAISS (when to pick which).

### Pillar 3 — RAG System Implementation (spine project)
1. Pick a **real, messy dataset** (PDFs, CSVs, support tickets).
2. Build the ingest pipeline: parse → clean → chunk → embed → store.
3. Wire retrieval + prompt + LLM into one `answer(question)` function.
4. Add **citations** to every answer (which chunk source it came from).
5. Handle "I don't know" — make it refuse gracefully when no good chunk exists.
6. Add a conversation/history layer so follow-ups work.
7. Log every query (question, chunks retrieved, model answer, latency).
8. Write a README with architecture diagram + the numbers (latency, cost, recall).

### Pillar 4 — Prompt Engineering
1. Write a **system prompt** for the agent; iterate on 3 versions.
2. Build a **few-shot** set (5 good examples) and measure accuracy change.
3. Refine retrieval prompt: instruct the model to use ONLY provided context.
4. Add structured-output prompting (JSON schema) for the answer + citations.
5. Handle **edge cases**: empty context, off-topic, ambiguous question.
6. Test prompt robustness: rephrase the same question 5 ways.
7. Use the eval harness to compare prompt versions (before/after numbers).
8. Write a personal **prompt cheat-sheet** (what worked, what didn't).

### Pillar 5 — Agents & Tool Use
1. Define 3 tools (e.g. search, calculator, DB-lookup) with clear schemas.
2. Wire the tools into the agent loop (LLM decides tool call).
3. Run tools in a **sandbox** (Docker with limits); validate outputs.
4. Add a **tool-call parser** that reliably extracts tool args.
5. Handle **tool errors** (bad args, timeout) with retry/fallback.
6. Limit tool budget (max N calls) to prevent runaway loops.
7. Add a simple **agentic workflow**: query → retrieve → decide → tool → answer.
8. Log trajectory (every step) for later eval analysis.

### Pillar 6 — Multimodal AI
1. Call **OpenAI Vision API** on an image and extract text/objects.
2. Transcribe audio with **Whisper API** (or local whisper).
3. Generate an image with a **DALL-E / image model**. and describe it back.
4. Load a **Hugging Face multimodal model** (e.g. CLIP) and compute image-text similarity.
5. Use **LangChain/LlamaIndex** multimodal loaders on a PDF with images.
6. Add a small multimodal feature to the project (e.g. OCR a scanned PDF).
7. Compare text-only vs vision-augmented retrieval on scanned docs.
8. Write a 1-page note on when multimodal matters vs when it's overkill.

### Pillar 7 — Evaluation & Reliability
1. Build the **eval harness** with 40+ test cases (pass/fail grading).
2. Add **trajectory logging** (every tool call + model call per run).
3. Record **cost and latency per run** for every eval.
4. Add **tracing** (OpenTelemetry or Langfuse) + a failure-mode dashboard.
5. Run before/after comparisons for **at least 3 changes** (prompt, retrieval, model).
6. Write the **eval report** (accuracy, failure modes, regression notes).
7. Write the **benchmark report** (hosted model vs self-hosted model).
8. Do 3 **timed mock system-design interviews** (RAG, multi-agent, chat app).

### Pillar 8 — Deployment & Job-Readiness
1. Run the agent behind an **API** (FastAPI) with clean endpoints.
2. Add **auth + RBAC + audit logs + PII redaction** to the service.
3. Integrate with a **client system** (auth'd API / CSV export / webhook).
4. Deploy to **a server/container** that a recruiter can hit live.
5. Record the **5-minute demo** aimed at a non-technical buyer.
6. Write the **case study**: problem → what you built → numbers → what failed.
7. Rewrite **resume + GitHub + LinkedIn** for AI Engineer roles.
8. Send **20+ applications** (and log them in `daily-logs/`).

---

## 4. Timeline to New Year (5 weeks)

Today **Fri 27 Nov 2026**. Weeks run Monday→Sunday, finishing Thu 31 Dec.

### Week 1 — Nov 30 – Dec 6 · Foundations, Dataset, Model Baseline
- [ ] Pillar 1: actions 1, 3, 4, 5, 6 (attention repro, hosted models, local serving, benchmark)
- [ ] Pillar 2: actions 1, 2, 5 (vector DB up, embeddings, top-k)
- [ ] Pillar 3: actions 1, 2 (pick dataset, ingest pipeline)
- [ ] LeetCode: 2–3 problems. Push GitHub scaffold + README skeleton.

**Week-1 exit test:** I can embed 200 docs, ask a question, and get top-5 chunks back.

### Week 2 — Dec 7–13 · Build the RAG Core
- [ ] Pillar 3: actions 3, 4, 5, 6, 7 (answer fn, citations, refuse, history, logging)
- [ ] Pillar 4: actions 1, 2, 3 (system prompt, few-shot, retrieval prompt)
- [ ] Pillar 7: action 1 (scaffold the 40-case eval harness)
- [ ] LeetCode: 2–3 problems. First GitHub commit with numbers.

**Week-2 exit test:** `answer()` works end-to-end with citations and graceful refusal.

### Week 3 — Dec 14–20 · Evals, Agents, Multimodal
- [ ] Pillar 7: actions 2, 3, 4, 5, 6 (trajectory, cost/latency, tracing, before/after, eval report)
- [ ] Pillar 5: actions 1, 2, 3, 4, 5 (tools, sandbox, parser, error handling)
- [ ] Pillar 6: actions 1, 2, 4 (vision, whisper, CLIP)
- [ ] LeetCode: 2–3 problems. Write week-2 write-up.

**Week-3 exit test:** I can prove a slow (improvement after a prompt/retrieval change.

### Week 4 — Dec 21–27 · Deployment, Benchmark, Demo
- [ ] Pillar 8: actions 1, 2, 3, 4 (API, auth/RBAC/PII, client integration, deploy)
- [ ] Pillar 1: action 7 + Pillar 7: action 7 (self-hosted model + benchmark report)
- [ ] Pillar 5: actions 6, 7, 8 (tool budget, agentic workflow, trajectory)
- [ ] LeetCode: 2–3 problems. Case study first draft.

**Week-4 exit test:** the service is live, the self-hosted model is benchmarked against the API model.

### Week 5 — Dec 28–31 · Polish, Demo, Applications
- [ ] Pillar 8: actions 5, 6, 7, 8 (demo, final case study, resume/GitHub/LinkedIn, 20 applications)
- [ ] Pillar 7: action 8 (3rd mock system-design interview)
- [ ] Pillar 6: action 8 (multimodal note) — only if time permits
- [ ] Final GitHub push: README, eval report, benchmark report, case study, demo link.

**Week-5 exit test (definition of done):** all checklist items in section 1 are checked.

---

## 5. Daily Cadence (fits your `daily-logs/` format)

Use `tools/quicklog.py` every day with the existing `TYPE` tags:
- `site` → Deep-ML / StatQuest / learning sites (rotation per `learning-sites-guide.md`)
- `paper` → the 16-week paper plan (attention repro in Week 1)
- `leetcode` → a few problems per week (never skip; bad-day floor = 1)
- `job` → applications, outreach, interview prep
- The spine project is your main "paper/site" substitute in Weeks 1–5.

**Rules (from your existing plan):**
- One resource per block, never mix sites in a block.
- Bad-day floor: 1 LeetCode + 1 hour on the project + 1 application → day still counts.
- Gap rule: if something doesn't click, step down one level, fix the single prerequisite
  (at most 1 day), then come back.

---

## 6. Sources wired in

- **Spine project (Support Ops Agent)** — `reference/inference-plan.md`
- **Paper reading (16-week plan)** — `reference/16-week-paper-plan.md`
- **Learning-site rotation + log rules** — `reference/learning-sites-guide.md`
- **AI Engineer roadmap (multimodal / platforms / APIs)** — `reference/ai-engineer.pdf`
- **Daily logging** — `daily-logs/_template.md` + `tools/quicklog.py`
