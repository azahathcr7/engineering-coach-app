# Beginner Glossary

Use in beginner mode: give the analogy first, then the precise term, then how it appears in the user's task. Extend with fresh analogies when helpful.

## Contents
- Code and version control
- Environments and delivery
- Data
- APIs and integrations
- Testing and quality
- AI terms
- Operations

## Code and version control
- **Repository (repo):** the project's folder plus its full history of changes. Analogy: a shared binder with every past version of every page.
- **Git:** the tool that tracks that history. Analogy: unlimited, labeled undo.
- **Branch:** a separate working copy of the project for one change. Analogy: drafting on a photocopy before editing the master.
- **Commit:** a saved snapshot with a note on what changed.
- **Diff:** the exact lines added and removed between two versions. Always read this, not just the summary.
- **Pull request (PR):** a request to merge your branch into the main version, with discussion and checks. Analogy: submitting a draft for sign-off before it's published.
- **Merge:** combining a branch into another one.
- **Merge conflict:** two people changed the same lines; a human decides which to keep.
- **Revert:** create a new change that undoes an earlier one.
- **Main (or master):** the official branch that production is built from.
- **Fork / clone:** a copy of a repo (clone: to your machine; fork: under your own account).

## Environments and delivery
- **Local:** your own machine.
- **Dev / staging / production:** practice area / dress rehearsal / the real thing.
- **Deploy:** put code into an environment so it runs there.
- **CI/CD:** automated robots that test (CI) and ship (CD) every change.
- **Pipeline (in delivery):** the sequence of automated steps a change passes through.
- **Feature flag:** a switch that turns a feature on or off without redeploying.
- **Rollback:** returning to the previous known-good state.
- **Hotfix:** an urgent fix to production, still reviewed but faster.

## Data
- **Schema:** the structure of data: which fields exist and their types.
- **Migration (data):** moving or reshaping data from one place or structure to another.
- **Migration (schema):** a versioned script that changes a database's structure.
- **ETL / ELT:** extract, transform, load: pulling data out, cleaning it, putting it somewhere.
- **Pipeline (data):** automated flow of data from sources to destinations.
- **Idempotent:** safe to run twice; result is the same as running once. Crucial for retries.
- **Backfill:** applying a change or computation to historical data.
- **Batch:** processing records in groups rather than all at once.
- **Reconciliation:** comparing before and after (or source and destination) to prove nothing was lost or duplicated.
- **Data quality checks:** automated tests on data (no nulls here, unique ids, valid formats).
- **Lineage:** the traceable route data takes from origin to where it's used.

## APIs and integrations
- **API:** a defined way for programs to talk to each other. Analogy: a restaurant menu and waiter between you and the kitchen.
- **Endpoint:** a specific address on an API that does one kind of thing.
- **Authentication / token / API key:** proof of who you are. Treat like a password.
- **Rate limit:** how many requests you may make per time period. Exceed it and requests are refused or slowed.
- **Webhook:** the other system calls you when something happens, instead of you asking repeatedly.
- **Pagination:** getting big result sets one page at a time.
- **Retry / backoff:** trying again after a failure, waiting longer each time.

## Testing and quality
- **Unit test:** checks one small piece of logic.
- **Integration test:** checks pieces working together.
- **Dry-run:** run that shows what would happen without doing it.
- **Edge case:** unusual input that breaks assumptions (empty, huge, special characters).
- **Linting:** automatic style and mistake checking of code.
- **Code review:** another person examines a change before it merges.
- **Regression:** something that used to work and broke.

## AI terms
- **Prompt:** instructions and context given to a model.
- **Context window:** how much text a model can consider at once.
- **Retrieval (RAG):** fetching relevant documents and giving them to the model so answers are grounded in them.
- **Tool use / function calling:** letting a model request actions (search, run code, call an API).
- **Agent:** a system where a model plans and takes multiple steps with tools.
- **Evaluation (eval):** a repeatable test set that measures whether AI output is good enough.
- **Hallucination:** confident but false output.
- **Guardrail:** a rule or check limiting what an AI can do or say.
- **Fine-tuning:** further training a model on specific examples (usually not the first thing to try).

## Operations
- **Logging:** a written record of what a program did.
- **Monitoring / alert:** watching health numbers and notifying when they go wrong.
- **Incident:** an unplanned problem affecting users.
- **Runbook:** step-by-step instructions for handling a known situation.
- **Postmortem:** a write-up after an incident focused on learning, not blame.
- **SLA / SLO:** the reliability promise (to customers / internal target).
- **Blast radius:** how much can be affected if this goes wrong.
