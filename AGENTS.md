# Repository guidance for AI coding agents

This repository distributes the Engineering Workflow Coach Agent Skill.

- Treat `skills/engineering-workflow-coach/SKILL.md` as the canonical skill definition.
- Read only relevant files under `skills/engineering-workflow-coach/references/` (progressive disclosure).
- Keep the repository skill-only: do not add a web app, dashboard, backend, service worker, browser storage, or product runtime.
- Preserve the Agent Skills directory convention: one skill directory with a `SKILL.md` and optional references.
- Keep provider-specific installation notes in `docs/INSTALLATION.md`; keep core coaching behavior provider-neutral.
- Validate changes with `python tests/validate_skill.py`.
- Do not claim a skill is installed in an agent unless installation was actually performed and verified.
