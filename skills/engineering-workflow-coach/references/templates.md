# Templates

Copy and fill these for the user's actual task. Replace the bracketed parts. Keep outputs short enough to be used.

## Contents
1. Task brief
2. Plan-first prompt for the coding AI
3. Small-change prompt
4. Dry-run and safety prompt
5. AI code review prompt (adversarial reviewer)
6. Branch and commit naming
7. PR description
8. Pre-deploy checklist
9. Rollback plan
10. Verification checklist
11. One-page design doc
12. Decision record
13. Blameless postmortem

## 1. Task brief
```
Problem: [what is broken or wanted]
Done means: [observable result]
Scope: in: [...]  out: [...]
Touches: [systems, data, who is affected]
Risk: [low / medium / high] because [reason]
Deadline or window: [...]
```

## 2. Plan-first prompt for the coding AI
```
Context: [system, tools, constraints].
Goal: [done means ...].
Do NOT write code yet. First give me:
1. A step-by-step plan.
2. Assumptions you are making that I should confirm.
3. Risks and what could go wrong on real data.
4. How we will test it and how we will undo it.
Wait for my approval before coding.
```

## 3. Small-change prompt
```
Implement only step [N] of the approved plan.
Keep the change small and focused on one purpose.
Do not refactor unrelated code or add extra features.
Explain in plain language what you changed and why.
```

## 4. Dry-run and safety prompt
```
Add a --dry-run mode that prints exactly what would change (record id, old value, new value) without changing anything.
Add logging of every change with timestamps.
Make the script safe to re-run (idempotent) and able to process in batches of [N] with a pause between batches.
Read credentials from environment variables; never hardcode them.
Write a backup export of the records before changing them.
```

## 5. AI code review prompt (adversarial reviewer)
```
Act as a skeptical senior engineer reviewing this diff before it touches production.
List: (a) bugs, (b) data-loss or corruption risks, (c) unhandled edge cases (empty, duplicate, unusual characters, partial failure), (d) security problems, (e) anything you do not understand.
Rank by severity. Do not rewrite the code; just find problems.
```

## 6. Branch and commit naming
Branch: `[type]/[short-description]` with types `fix`, `feat`, `chore`, `docs`, `refactor`.
Commit: `[type]: [imperative summary under about 70 characters]`, optional body explaining why.
Example: `fix: trim trailing whitespace from SKUs before update`

## 7. PR description
```
## What
[one or two sentences on what changed]

## Why
[problem or ticket link; who is affected]

## How it was tested
- [dry-run output / sample of N records / staging check]
- [edge cases tried]

## Risk and blast radius
[what could go wrong, what it touches]

## Rollback
[exact steps; where the backup is]

## Notes for reviewer
[where to look closely; anything unsure]
```

## 8. Pre-deploy checklist
- [ ] Tested via dry-run and a small real sample
- [ ] Backup/export taken and stored safely
- [ ] Rollback steps written and tried on a copy
- [ ] Reviewed (human and/or adversarial AI review)
- [ ] No secrets in code or commits
- [ ] Batch size and rate limits set
- [ ] Time window chosen (low-traffic) and affected people informed
- [ ] Monitoring ready: logs, error counts, a before-count to compare
- [ ] Stop condition defined (what makes us halt)

## 9. Rollback plan
```
Trigger: [what tells us to roll back]
Owner: [who decides and who executes]
Steps: 1. Stop the job. 2. [restore from backup X / revert merge Y / run inverse script Z]. 3. Verify [checks].
Time to execute: [estimate]
Data not recoverable by rollback: [anything]
```

## 10. Verification checklist
- [ ] Counts match expected (before, changed, after)
- [ ] [N] random records spot-checked on the live system
- [ ] Known-problem records confirmed fixed
- [ ] No new errors in logs for [period]
- [ ] Requester confirms the problem is resolved
- [ ] Backup retention date noted

## 11. One-page design doc
```
Title / Author / Date
Context: why now, what problem
Goals and non-goals
Options considered: A, B, C with pros and cons
Decision and why
Design: components, data flow, a simple diagram
Failure modes and mitigations
Testing and rollout plan
Open questions
```

## 12. Decision record
```
Decision: [what we chose]
Date: [ ]
Context: [the situation and constraints]
Options considered: [A, B, C]
Why this one: [trade-offs]
Consequences: [what gets easier, what gets harder]
Revisit when: [trigger]
```

## 13. Blameless postmortem
```
Summary: [what happened, impact, duration]
Timeline: [key moments]
Root causes: [system and process causes, not people]
What went well / what went badly
Action items: [owner, date]
```
