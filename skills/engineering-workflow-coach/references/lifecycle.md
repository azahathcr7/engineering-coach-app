# The Change Lifecycle

Every engineering role runs this same loop. Tools change; the loop doesn't. When coaching, tailor each step to the user's task and skip only what truly doesn't apply.

## Contents
1. Define the problem
2. Plan
3. Branch
4. Build (with AI)
5. Test and dry-run
6. Commit
7. Pull request
8. Review and automated checks
9. Merge and deploy
10. Verify
11. Rollback and aftercare

## 1. Define the problem
**What:** Write down what is broken or wanted, what "done" looks like, and what the change can touch (the blast radius).
**Why:** Vague problems produce vague fixes. A precise definition of done is also how you know when to stop.
**Output:** 3 to 5 lines: problem, desired result, scope (what's in and out), risk level (low: internal tool; high: live customers or money).
**Example (store data fix):** "Products imported last month have SKUs with trailing spaces. Done = all 2,300 SKUs trimmed, no product lost, no price changed. Touches live catalog. High risk."

## 2. Plan
**What:** Decide the approach before coding. For anything beyond trivial, ask the AI for a written plan and read it.
**Why:** Fixing a wrong plan costs minutes; fixing wrong code on live data costs hours or trust.
**Output:** A short list: inputs, transformation, outputs, how it's tested, how it's undone. For larger work, a design doc (template in templates.md).
**Senior habit:** Ask "what's the simplest thing that could work?" and "what would make me regret this in a week?"

## 3. Branch
**What:** A branch is a private parallel copy of the code where you work without disturbing the main version.
**Why:** `main` is what the team and production rely on. Work happens beside it, then gets merged after review.
**Convention:** Short, descriptive names, often with a type prefix: `fix/trim-sku-whitespace`, `feat/add-order-export`, `chore/update-deps`. Branch from the latest main.
**Generic commands:** `git checkout main`, `git pull`, `git checkout -b fix/trim-sku-whitespace`.

## 4. Build (with AI)
**What:** Direct the AI to write the change in small, reviewable pieces.
**Why:** Small changes are easy to review and easy to undo. Large AI-generated changes hide bugs.
**How:**
- Give context: what the system is, the plan, constraints, what must not change.
- Ask for a dry-run mode, logging, and no hardcoded secrets.
- One purpose per change. If the AI proposes extra "improvements", decline or split them out.
- Read the diff. If a line is unclear, ask the AI to explain it before accepting.

## 5. Test and dry-run
**What:** Prove the change works before it touches anything real.
**Layers (use what fits):**
- *Unit tests:* tiny checks that a function does what it should.
- *Dry-run:* the script reports what it *would* change without changing anything. Essential for data work.
- *Sample run:* run on a copy, dev environment, or 5 records.
- *Staging:* a near-copy of production for realistic testing.
**Why:** Production is the most expensive place to discover a bug.
**Widening rings for data changes:** 1 record, then 10, then 100, then all. Inspect results after each ring.
**Also test the unhappy paths:** empty values, duplicates, special characters, records that already changed, the network failing halfway.

## 6. Commit
**What:** A commit is a saved snapshot with a message. Make several small ones, not one giant one.
**Why:** History becomes a readable story, and a bad piece can be reverted alone.
**Message pattern:** imperative, specific. "Trim whitespace from SKUs before import" beats "fixes".
**Never commit:** passwords, API keys, tokens, customer data exports. If it happens, treat the secret as leaked and rotate it.

## 7. Pull request (PR)
**What:** A request to merge your branch into main, with a description and a place for review. (Called a "merge request" in some tools.)
**Why:** It's the checkpoint where a second pair of eyes (and automated checks) look before the change goes live. It's also documentation of why the change happened.
**Good PR:** small, one purpose, description answers: What changed? Why? How was it tested? Risk? How to roll back? (Template in templates.md.)
**Tip:** Review your own PR first, line by line, before asking anyone else.

## 8. Review and automated checks
**What:** Humans comment and approve. Automated checks (CI: continuous integration) run tests, linting, security scans.
**Why:** People catch logic and context mistakes; machines catch consistency and known-bad patterns.
**How to respond to review:** Treat comments as questions about the code, not about you. Fix, or explain why not. Push changes to the same branch; the PR updates itself.
**If you're the solo reviewer** (common): use a checklist, take a break before reviewing, and have a second AI session critique the diff as an adversarial reviewer.

## 9. Merge and deploy
**What:** Merge combines the branch into main. Deploy is putting that code into an environment.
**Environments, in order:** dev, staging, production. Each step is a chance to catch problems.
**Release safety tools:** feature flags (turn the change on for few users first), canary releases (small slice of traffic), maintenance windows, change freezes.
**Data migrations:** run as a controlled job with logging, not ad hoc from a laptop, when possible.

## 10. Verify
**What:** Confirm the change did what you intended in the real environment.
**How:** Spot-check actual records, compare counts before and after, watch error logs and dashboards, confirm with the person who reported the problem.
**Why:** "The script finished" is not the same as "the problem is fixed". Define the verification checks in step 1.

## 11. Rollback and aftercare
**Rollback:** the ability to undo. Code: revert the merge or redeploy the previous version. Data: restore from the backup/export you took beforehand, or run an inverse script. Decide and test this before deploying.
**Aftercare:** monitor for a while, note what you learned, update docs or runbooks. For incidents, a short blameless postmortem: what happened, why, what changes so it doesn't recur.

## Quick version (for chat replies)
Problem, plan, branch, build small, dry-run in rings, commit, PR with rollback note, review, deploy to staging then prod, verify with spot checks, keep the backup until confident.
