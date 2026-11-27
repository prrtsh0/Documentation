# Research Paper Reproductions

I reproduce papers, not just read them. One folder per paper.

Each paper follows the fixed pipeline in
[`reference/paper-pipeline.md`](../reference/paper-pipeline.md):

1. **Prerequisites** — if I can't follow it, fix the one missing concept first.
2. **Pass 1** (15 min) — abstract, figures, conclusion. What problem does it solve?
3. **Pass 2** (1–2 h) — full read, skip proofs the first go. List every unknown term.
4. **From memory** — close it, explain in 5 lines (problem, idea, how, results, limits).
5. **Code the core idea only** — the one thing the paper introduced, not the whole system.
6. **Experiment** — run with and without the idea, record the numbers.
7. **Write-up** — README per paper: summary, code, results, what surprised me.

The 16-week schedule and prerequisites checklist are in `reference/`:
- [`reference/16-week-paper-plan.md`](../reference/16-week-paper-plan.md)
- [`reference/prerequisites.md`](../reference/prerequisites.md)

## Paper folder template

Copy `_template/` to a new folder named after the paper:

```
papers/<paper-name>/
├── README.md    # summary, code, results, what surprised you
├── code/        # the code for the core idea (and the experiment)
├── results/     # numbers, loss curves, comparisons
└── notes.md     # pass-1 and pass-2 notes, unknown terms
```

## Index (add one row per paper)
| Paper | Week | Status | Key result |
| --- | --- | --- | --- |
| *(add first paper)* |  | Not started / In progress / Done |  |
