# Skill architecture

## Purpose

The repository packages one portable Agent Skill: `engineering-workflow-coach`. It is loaded by a compatible host agent and changes how that agent reasons about and responds to engineering-workflow requests.

It is not an executable application. There is no UI, database, API server, background worker, model integration, browser storage, or autonomous execution engine in this repository.

## Package structure

```text
skills/engineering-workflow-coach/
├── SKILL.md
└── references/
    ├── architect-path.md
    ├── beginner-glossary.md
    ├── flavours.md
    ├── lifecycle.md
    ├── roles.md
    └── templates.md
```

### Core instructions

`SKILL.md` contains skill metadata, mission, behavior, safety boundaries, workflow, role/mode routing, and a reference index. Keep it focused on **how the agent should behave and where to look**, not every detailed playbook.

### Reference material

- `lifecycle.md`: end-to-end engineering change lifecycle.
- `roles.md`: software, data, FDE, and AI engineering lenses.
- `architect-path.md`: growth ladder and system-design judgment.
- `templates.md`: reusable engineering artifacts and prompts.
- `beginner-glossary.md`: plain-language definitions.
- `flavours.md`: user-invoked coaching modes.

The agent loads only references relevant to the current request (progressive disclosure).

## Runtime contract

The host agent supplies all execution capabilities. The skill interprets the request, selects relevant guidance, uses only tools already available and authorized, produces grounded guidance/artifacts, and reports completed, failed, and unperformed actions accurately.

The skill does not grant access to GitHub, terminals, cloud accounts, production systems, or model APIs. It does not bypass confirmation requirements or organizational controls.

## Portability

The package uses a simple directory convention with `SKILL.md` and Markdown references. Provider-specific discovery paths and installation procedures belong in `INSTALLATION.md`, not in provider-neutral skill instructions.

## Change policy

- Keep one canonical copy of each reference.
- Avoid hard-coding vendor-specific commands unless clearly labeled as examples.
- Do not put secrets, customer data, or private environment details in the package.
- Add validation for metadata, required references, and relative links.
- Keep product/application code out of this repository.
