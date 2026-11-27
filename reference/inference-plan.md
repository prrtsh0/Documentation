Reality check

Four weeks won't make you good at four roles. It can give you one deployed project that shows credible skill in all four. These roles share a spine (an LLM system with tools, reliability, serving, and a real user), so build one project and look at it through four lenses. If you already have an agent project, use it as the base instead of starting fresh.

Spine project: "Support Ops Agent"
An agent that answers questions over a messy document and data set, calls tools, runs behind an API, and is measured by an eval harness. In week 3 you swap its model for a self-hosted one and benchmark it.

Week 1: AI engineer (build the thing)
[ ] Pick a real, messy dataset (PDFs, CSVs, support tickets). This is also your FDE material later.
[ ] Build RAG: chunking, embeddings, pgvector or Qdrant, top-k retrieval with reranking
[ ] Add tool calling with 3 tools (e.g., SQL query, search, calculator) through a provider API
[ ] Wrap it in FastAPI with streaming, Postgres for state, and Redis caching
[ ] Dockerize it and deploy it somewhere public
[ ] Study: sections 7, 9, 11 of the roadmap
[ ] System design: URL shortener and rate limiter

Done when: a stranger can hit your URL and get a grounded answer with sources.

Week 2: Harness engineer (make it reliable and measurable)
[ ] Rewrite the agent loop from scratch without a framework: plan, act, observe, with a step limit
[ ] Add retries with backoff, timeouts, a circuit breaker, and graceful degradation when the model or a tool fails
[ ] Run tools in a sandbox (a Docker container with limits) and validate their outputs
[ ] Build an eval harness with 40+ test cases: pass/fail grading, trajectory logging, cost and latency per run
[ ] Add tracing (OpenTelemetry or Langfuse) and a dashboard of failure modes
[ ] Run before/after comparisons for at least 3 changes (prompt, retrieval, model)
[ ] Study: sections 13, 15, 19
[ ] System design: notification system and job scheduler

Done when: you can say "this change improved pass rate from X% to Y%" and prove it.

Week 3: Inference engineer (the hard week)
[ ] Learn KV cache, attention memory math, continuous batching, and paged attention. Read the vLLM paper and work out the KV cache size for a 7B model by hand.
[ ] Serve a small open model with vLLM on a free or cheap GPU (Colab, Kaggle, or a rented hourly GPU)
[ ] Benchmark throughput and latency (time to first token, tokens per second) at batch sizes 1, 8, 32 and 64
[ ] Compare FP16 against a 4-bit or 8-bit quantized version for speed, memory, and eval score
[ ] Point your Week 2 agent at the self-hosted model and re-run your evals
[ ] Write a one-page benchmark report with charts
[ ] Study: sections 3, 14, 21, plus GPU basics

Done when: you have a table showing the speed, memory, and quality trade-offs, with numbers you measured yourself.

This is the shallowest week by necessity. After the four weeks, GPU and serving internals need a separate 2-3 month path (CUDA basics, Triton, profiling). This week proves you can start.

Week 4: FDE (customer-facing, ship it)
[ ] Write a one-page scoping doc for a fictional client: problem, constraints, success metric, risks
[ ] Integrate with a "client system": an auth'd API, a legacy CSV export, or a webhook
[ ] Add auth, RBAC, audit logs, and PII redaction (section 16)
[ ] Record a 5-minute demo aimed at a non-technical buyer
[ ] Write a case study with the problem, what you built, the numbers from Weeks 2-3, and what failed
[ ] Do 3 timed mock system design interviews: RAG assistant, multi-agent platform, chat app
[ ] System design: payment system and real-time analytics

Done when: a non-engineer could watch the demo and understand the value.

Weekly habit across all 4 weeks
[ ] LeetCode: a few problems per week. You still need coding rounds, and no project replaces them.
[ ] Push to GitHub with a README that has architecture, numbers, and failures
[ ] One short write-up per week
What you'll have at the end

One repo, one deployed service, an eval report, a benchmark report, a case study, and a demo. That is credible for AI engineer and FDE roles, decent for harness roles, and an entry signal for inference roles.

If you can only do part of this, drop the inference week, not the eval harness. Evals are what separate a serious candidate from someone who built a chatbot.