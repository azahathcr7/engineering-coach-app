# Engineering Workflow Coach — Agent Skill

A portable, tool-agnostic **Agent Skill** that helps AI agents coach engineers through real software, data, platform, forward-deployed, and AI engineering work.

This repository is a skill distribution project—not an app. It contains no web UI, dashboard, browser storage, backend, service worker, or runtime application.

## What the skill does

The canonical skill lives at:

`skills/engineering-workflow-coach/SKILL.md`

It teaches an AI agent to:
- Turn ambiguous engineering work into a concrete, testable outcome.
- Inspect before changing and plan the smallest safe implementation.
- Guide work through branch, implementation, tests, PR/review, deployment, verification, and rollback.
- Coach software engineers, data engineers, FDEs, and AI engineers.
- Review AI-generated code and emphasize evidence, safety, and verification.
- Support the **Grill me**, **Ponytail**, **Hallmark**, and **Humanizer** coaching modes.
- Explain concepts from beginner level through architect-level judgment.

## Repository layout

```text
.
├── README.md
├── AGENTS.md
├── skills/
│   └── engineering-workflow-coach/
│       ├── SKILL.md
│       └── references/
│           ├── architect-path.md
│           ├── beginner-glossary.md
│           ├── flavours.md
│           ├── lifecycle.md
│           ├── roles.md
│           └── templates.md
├── docs/
│   ├── ARCHITECTURE.md
│   └── INSTALLATION.md
├── tests/
│   └── validate_skill.py
└── .github/workflows/
    └── validate.yml
```

## Install with a skills-compatible agent

The repository follows the open Agent Skills folder convention: a skill is a directory containing a `SKILL.md` file, with optional supporting references.

Using the Skills CLI:

```bash
npx skills add azahathcr7/engineering-coach-app --skill engineering-workflow-coach
```

Choose the agents and installation scope offered by the CLI. The CLI's supported agents and flags can change; use `npx skills add --help` for current options.

## Install manually

Copy the complete `skills/engineering-workflow-coach/` directory—not just `SKILL.md`—into the skills directory recognized by your agent.

### Claude Code

For a project-local installation, place it at:

```text
.claude/skills/engineering-workflow-coach/
```

For a personal installation, place it under:

```text
~/.claude/skills/engineering-workflow-coach/
```

Claude Code discovers the `SKILL.md` in that directory. Keep the `references/` folder beside it so the skill can load detailed guidance as needed.

### Other agents

Use the agent's documented skills directory and preserve this structure:

```text
<agent-skills-directory>/
└── engineering-workflow-coach/
    ├── SKILL.md
    └── references/
        └── ...
```

Some agent products expose skills through a UI, workspace configuration, or project instructions rather than a local folder. In those environments, add the skill's `SKILL.md` and make its reference files available to the agent. Do not assume every chat product has native filesystem skill discovery.

## Use

Once installed, ask the agent to:
- "Use the Engineering Workflow Coach skill to plan this migration."
- "Grill me on this PR before I merge it."
- "Use Hallmark mode to review this implementation."
- "Explain this deployment workflow in beginner mode."
- "Use Ponytail mode and trace this issue from ticket to production verification."

The skill should also activate naturally for relevant engineering tasks based on its description.

## Validate locally

Python 3.10+ is sufficient; there are no runtime dependencies.

```bash
python tests/validate_skill.py
```

## Design principles

- **Portable:** no model API, vendor SDK, app server, or framework dependency.
- **Progressive disclosure:** concise core instructions; detailed playbooks in reference files.
- **Tool-agnostic:** the host agent uses its own available tools and permissions.
- **Evidence-based:** never claim actions or checks occurred unless they did.
- **Safety-first:** production changes require backups, dry-runs, staged rollout, verification, and rollback planning.

## Contributing

Keep the core `SKILL.md` focused on agent behavior and routing. Put detailed domain material in `references/`. Add or update validation checks when the skill structure changes. Do not add app/runtime features to this repository.
