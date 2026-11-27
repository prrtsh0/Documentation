#!/usr/bin/env python3
"""Render the Harada "Open Window 64" chart for the AI Engineer plan as PNG.

Output: reference/harada-chart.png

Layout:
  Top   -> Master 3x3 grid (central goal + 8 pillars).
  Below -> 8 expanded pillar grids (each pillar center + 8 action cells).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ---------- palette ----------
CENTER  = "#ffe066"; CENTER_B = "#f0c419"
BG      = "#f4f6f8"; INK = "#1c2733"; MUTED = "#5b6b7a"
CARD    = "#ffffff"; LINE = "#d9e0e6"

PILLARS = [
    ("1", "LLM Fundamentals &\nInference", "#e8f0fe", "#3b6fd8"),
    ("2", "Embeddings &\nVector Databases", "#e6f8e9", "#2f9e57"),
    ("3", "RAG System\nImplementation", "#fdeee7", "#d96b2b"),
    ("4", "Prompt\nEngineering", "#f2ebfd", "#7b51d1"),
    ("5", "Agents &\nTool Use", "#fdf3e0", "#c98a1b"),
    ("6", "Multimodal\nAI", "#e7f6f7", "#199a9d"),
    ("7", "Evaluation &\nReliability", "#fbeaea", "#cf3d3d"),
    ("8", "Deployment &\nJob-Readiness", "#eef0ea", "#6a7a3c"),
]

ACTIONS = {
 "1": ["Reproduce Self-Attention (1706.03762) from scratch",
       "Build a masked-attention GPT-style block on a toy corpus",
       "Run 3 hosted models (OpenAI, Anthropic, Cohere); compare cost/latency",
       "Serve locally via llama.cpp / Ollama",
       "Benchmark same model: HF pipeline vs vLLM vs served API",
       "Write 1-page note on temperature / top-p / sampling",
       "Quantize a model (GGUF/int8); measure quality vs speed",
       "Read + summarize the Week-3 attention paper"],
 "2": ["Set up pgvector (or Qdrant) with insert/query loop",
       "Embed 200+ messy docs with a BGE/text-embedding model",
       "Implement chunking (fixed / recursive / sentence); compare quality",
       "Implement top-k retrieval; inspect results",
       "Add reranking (cross-encoder); measure recall gain",
       "Store metadata + filters (source, date, tag)",
       "Build similarity-search demo: question -> top-5 chunks",
       "Write comparison note: pgvector vs Qdrant vs FAISS"],
 "3": ["Pick a real, messy dataset (PDFs, CSVs, tickets)",
       "Build ingest: parse -> clean -> chunk -> embed -> store",
       "Wire retrieval + prompt + LLM into answer(question)",
       "Add citations to every answer (source chunk)",
       "Handle 'I don't know' — refuse gracefully",
       "Add conversation/history layer for follow-ups",
       "Log every query (question, chunks, answer, latency)",
       "README: architecture + numbers (latency, cost, recall)"],
 "4": ["Write a system prompt; iterate on 3 versions",
       "Build a few-shot set (5 examples); measure accuracy change",
       "Refine retrieval prompt: use ONLY provided context",
       "Add structured-output (JSON schema) for answer + citations",
       "Handle edge cases: empty context, off-topic, ambiguous",
       "Test robustness: rephrase the same question 5 ways",
       "Compare prompt versions with the eval harness",
       "Write a personal prompt cheat-sheet"],
 "5": ["Define 3 tools (search, calculator, DB-lookup) with schemas",
       "Wire tools into the agent loop (LLM decides tool call)",
       "Run tools in a sandbox (Docker with limits); validate outputs",
       "Add a tool-call parser that reliably extracts args",
       "Handle tool errors (bad args, timeout) with retry/fallback",
       "Limit tool budget (max N calls) to prevent runaway loops",
       "Add agentic workflow: query -> retrieve -> decide -> tool -> answer",
       "Log trajectory (every step) for eval analysis"],
 "6": ["Call OpenAI Vision API on an image; extract text/objects",
       "Transcribe audio with Whisper API (or local)",
       "Generate an image (DALL-E / image model); describe it back",
       "Load an HF multimodal model (CLIP); image-text similarity",
       "Use LangChain/LlamaIndex multimodal loaders on PDF with images",
       "Add small multimodal feature (e.g. OCR a scanned PDF)",
       "Compare text-only vs vision-augmented retrieval on scanned docs",
       "Write note: when multimodal matters vs overkill"],
 "7": ["Build the eval harness with 40+ test cases (pass/fail)",
       "Add trajectory logging (every tool + model call per run)",
       "Record cost and latency per run for every eval",
       "Add tracing (OpenTelemetry / Langfuse) + failure dashboard",
       "Before/after comparisons for >=3 changes (prompt, retrieval, model)",
       "Write the eval report (accuracy, failure modes, regressions)",
       "Write the benchmark report (hosted vs self-hosted model)",
       "Do 3 timed mock system-design interviews"],
 "8": ["Run the agent behind an API (FastAPI) with clean endpoints",
       "Add auth + RBAC + audit logs + PII redaction",
       "Integrate with a client system (auth'd API / CSV export / webhook)",
       "Deploy to a server/container a recruiter can hit live",
       "Record the 5-minute demo aimed at a non-technical buyer",
       "Write the case study: problem -> build -> numbers -> what failed",
       "Rewrite resume + GitHub + LinkedIn for AI Engineer roles",
       "Send 20+ applications (log them in daily-logs/)"],
}

def rounded_box(ax, x, y, w, h, fc, ec, lw=1.2, r=0.06):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={r}",
                       fc=fc, ec=ec, lw=lw)
    ax.add_patch(p)
    return p

def master_chart(ax):
    """Master 3x3 grid: center goal + 8 pillars."""
    gap = 0.04
    cell = (1.0 - 2 * gap) / 3.0
    cells = {}  # (col,row) -> pillar index (0..7)
    order = [[0,1,2],[3,None,4],[5,6,7]]
    x0, y0 = 0.0, 0.0
    for r in range(3):
        for c in range(3):
            x = x0 + c * (cell + gap)
            y = y0 + (2 - r) * (cell + gap)
            idx = order[r][c]
            if idx is None:
                rounded_box(ax, x, y, cell, cell, CENTER, CENTER_B, lw=2.4)
                ax.text(x + cell/2, y + cell/2,
                        "BECOME A\nJOB-READY\nAI ENGINEER\n\nby Dec 31, 2026",
                        ha="center", va="center", fontsize=11, fontweight="bold",
                        color="#6b5300")
                continue
            num, name, fc, ec = PILLARS[idx]
            rounded_box(ax, x, y, cell, cell, fc, ec, lw=1.6)
            ax.text(x + cell/2, y + cell/2, f"{num}\n{name}",
                    ha="center", va="center", fontsize=8.2, fontweight="bold",
                    color=ec)

def pillar_chart(ax, idx):
    """8 mini-grids (3x3 each) with pillar-centered + 8 actions."""
    num, name, fc, ec = PILLARS[idx]
    gap = 0.03
    cell = (1.0 - 2 * gap) / 3.0
    acts = ACTIONS[num]
    order = [[0,1,2],[3,None,4],[5,6,7]]
    for r in range(3):
        for c in range(3):
            x = c * (cell + gap)
            y = (2 - r) * (cell + gap)
            o = order[r][c]
            if o is None:
                rounded_box(ax, x, y, cell, cell, ec, ec, lw=1.8)
                ax.text(x + cell/2, y + cell/2, name,
                        ha="center", va="center", fontsize=6.4,
                        fontweight="bold", color="white", wrap=True,
                        linespacing=1.3)
                continue
            rounded_box(ax, x, y, cell, cell, CARD, LINE, lw=0.9)
            ax.text(x + cell/2, y + cell/2, f"{o+1}. {acts[o]}",
                    ha="center", va="center", fontsize=5.4,
                    color=INK, wrap=True, linespacing=1.35)

# ---------- build figure ----------
W = 12.0
master_h = 4.2
pillar_h = 2.6
n_cols = 2
n_rows = 4
H = master_h + 0.4 + n_rows * pillar_h + 1.6
fig = plt.figure(figsize=(W, H), dpi=150)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.axis("off")

# Title
ax.text(0.5, 0.995, "Harada Method — Open Window 64 · AI Engineer Plan",
        ha="center", va="top", fontsize=16, fontweight="bold", color=INK)
ax.text(0.5, 0.985, "1 central goal → 8 sub-goals → 64 actions · Nov 27 → Dec 31, 2026",
        ha="center", va="top", fontsize=9.5, color=MUTED)

# Master chart area
master_top = 0.965
master_h_n = 0.30
ax.text(0.02, master_top, "1 · Master Chart",
        fontsize=11, fontweight="bold", color=INK)
m_ax = fig.add_axes([0.02, master_top - master_h_n, 0.96, master_h_n])
m_ax.set_xlim(0, 1); m_ax.set_ylim(0, 1); m_ax.axis("off")
master_chart(m_ax)

# Pillar grids
sec_top = master_top - master_h_n - 0.02
ax.text(0.02, sec_top, "2 · Expand each pillar → 8 actions (the 64)",
        fontsize=11, fontweight="bold", color=INK)
g_w = (0.96 - 0.03) / n_cols
g_h = 0.20
for i in range(8):
    col = i % n_cols
    row = i // n_cols
    gx = 0.02 + col * (g_w + 0.03)
    gy = sec_top - 0.015 - (row + 1) * (g_h + 0.012)
    g = fig.add_axes([gx, gy, g_w, g_h])
    g.set_xlim(0, 1); g.set_ylim(0, 1); g.axis("off")
    pillar_chart(g, i)
    num, name, fc, ec = PILLARS[i]
    g.text(0.5, -0.02, f"Pillar {num} · {name.replace(chr(10),' ')}",
           ha="center", va="top", fontsize=6.4, fontweight="bold", color=ec)

fig.savefig("reference/harada-chart.png", dpi=150, facecolor=BG)
print("saved reference/harada-chart.png")
