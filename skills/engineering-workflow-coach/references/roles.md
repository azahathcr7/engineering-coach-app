# Role Playbooks

Four roles, one shared loop (see lifecycle.md). What differs is the *emphasis*: what each role worries about, what a normal day contains, and what separates the best from the average. Roles blur in practice, so pick the lens that fits the task and say when two apply.

## Contents
- Software engineer
- Data engineer
- Forward deployed engineer (FDE)
- AI engineer
- Which lens for which task

## Software engineer

**Core job:** Build and maintain the products and systems people use, reliably, over years.

**A typical day**
- Morning: check alerts, messages, review requests; stand-up (short team sync).
- Pick up a ticket, read the code around it first, plan, write a small change with tests.
- Open a PR, respond to reviews, review teammates' PRs (a big part of the job).
- Debug: reproduce the problem, form a hypothesis, narrow down with logs and tests.
- Meetings: planning, design discussions, occasional incident response.

**Habits of the best**
- Read much more code than they write; understand before changing.
- Small PRs, fast turnaround, kind and specific review comments.
- Write tests for behavior, not for lines.
- Make the next engineer's life easier: naming, comments on *why*, docs.
- Prefer boring, proven solutions. Complexity is a cost.

**What to measure yourself on:** changes that ship safely, bugs caught before production, how quickly others can understand your code.

**Typical artifacts:** tickets, PRs, tests, design docs, runbooks, release notes.

## Data engineer

**Core job:** Move, clean and organize data so it is trustworthy and available for apps, analytics and AI.

**A typical day**
- Check pipeline health: did last night's jobs run? Are row counts and freshness normal?
- Investigate data quality issues (duplicates, nulls, wrong formats, late data).
- Build or modify pipelines (extract from a source, transform, load to a destination).
- Write and run migrations; coordinate cutovers with the people who own the systems.
- Talk to analysts and product owners about what a field *actually means*.

**Habits of the best**
- Treat data as a product: documented, tested, versioned.
- Idempotent jobs: running twice gives the same result as once.
- Always know the data's lineage: where each field came from and what touched it.
- Validate at boundaries: row counts, uniqueness, null checks, before/after comparisons.
- Backfills and migrations in batches with checkpoints, dry-runs and reconciliation reports.
- Keep raw data untouched; transform into new layers so you can always replay.

**What to measure yourself on:** data correctness, pipeline reliability, time to detect bad data.

**Typical artifacts:** pipeline code, schemas, data contracts, quality checks, reconciliation reports, migration runbooks.

**Migration pattern (live system):** export and back up, map fields old to new, dry-run report of planned changes, small batch, reconcile counts, widen, final verification, keep backup for an agreed period.

## Forward deployed engineer (FDE)

**Core job:** Embed with a customer or business team, understand their real problem, and deliver working solutions fast, often by configuring, integrating and building on top of a core product or platform.

**A typical day**
- Talk to stakeholders; translate messy business needs into a concrete, testable scope.
- Explore their systems and data to find what's actually true (not what the docs say).
- Prototype quickly, show it, adjust. Ship something small that works, then iterate.
- Integrate with their tools (APIs, databases, ERP/CRM, e-commerce platforms).
- Write up what was done and hand over so the customer can run it.
- Feed patterns back to the product team ("five customers asked for this").

**Habits of the best**
- Clarify the outcome before the solution: "What will be different on Monday if this works?"
- Fast feedback loops with the customer; demo early and often.
- Treat the customer's production systems with extra caution: they own the risk.
- Communicate in the customer's language; document decisions and assumptions.
- Balance speed with safety: prototypes quickly, production changes carefully.
- Know when to stop customizing and push a general fix to the product.

**What to measure yourself on:** customer outcomes, time to first value, trust, how reusable the work is.

**Typical artifacts:** scoping notes, prototypes, integration code, demo scripts, handover docs, feedback to product.

## AI engineer

**Core job:** Build applications and systems that use AI models reliably: prompts, retrieval, tools, agents, evaluation and monitoring.

**A typical day**
- Define the task the AI should do and how success will be measured.
- Build and refine prompts, retrieval (feeding the model the right documents), and tool connections.
- Create evaluation sets: realistic test inputs with expected qualities, and run them after every change.
- Investigate failures: wrong answers, cost spikes, latency, unsafe outputs.
- Add guardrails, logging, fallbacks and human review where stakes are high.
- Track cost, speed and quality trade-offs between models.

**Habits of the best**
- Evaluation first: no change ships without comparing against the eval set.
- Version prompts and configs like code; review them in PRs.
- Log inputs, outputs and decisions (while respecting privacy) so failures are debuggable.
- Design for failure: the model will sometimes be wrong; the system must cope.
- Keep humans in the loop for irreversible or high-stakes actions.
- Start simple (a good prompt) before adding complexity (agents, fine-tuning).

**What to measure yourself on:** quality on real tasks, reliability, cost per task, safety incidents.

**Typical artifacts:** prompts, eval sets and reports, retrieval pipelines, tool definitions, monitoring dashboards, model comparison notes.

## Which lens for which task

| Task | Primary lens | Also borrow from |
|---|---|---|
| Fix wrong data on a live store | Data engineer | FDE (customer care), Software (PR flow) |
| Build an integration between two systems | Software / FDE | Data (mapping, validation) |
| Automate a business process with AI | AI engineer | FDE (requirements), Software (shipping) |
| Customer wants something quickly, scope unclear | FDE | Whichever fits the technical core |
| Slow or flaky nightly pipeline | Data engineer | Software (debugging, tests) |
