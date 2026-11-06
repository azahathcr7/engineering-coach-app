# Coaching model

## Purpose
Help an individual engineer move from ambiguity to a concrete, testable next step. The app is intentionally a structured prompt tool, not an autonomous engineering decision-maker.

## Modes
- **Task breakdown:** outcome, boundaries, unknowns, checkpoints, definition of done.
- **Debugging:** expected/actual behavior, reproduction, hypothesis testing, evidence, regression prevention.
- **Blocker:** classify the blocker, separate facts from assumptions, identify the decision owner, prepare an unblock request.
- **Code review:** intent, correctness, edge cases, tests, maintainability, security, operations, communication.
- **Design:** requirements, interfaces, trust boundaries, alternatives, trade-offs, failure modes, decision record.
- **Learning:** narrow capability, baseline, reference, practice, retrieval, spaced follow-up.

## Operating principles
1. Prefer observable outcomes over vague activity.
2. Reduce work into small checkpoints.
3. Separate evidence from assumptions.
4. Make risks and unknowns explicit.
5. Prefer reversible experiments where uncertainty is high.
6. Record decisions and close communication loops.
7. Do not equate task counts with engineering quality.

## Important limitation
The coaching plans are deterministic templates embedded in the browser. They do not inspect source code, connect to repositories, execute tests, or call an AI model. They should be adapted to the team's engineering standards and production controls.
