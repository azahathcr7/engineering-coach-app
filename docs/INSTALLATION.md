# Installation and agent compatibility

## Package format

The skill is stored in `skills/engineering-workflow-coach/SKILL.md`. The package uses the Agent Skills convention: a named directory containing `SKILL.md` plus optional reference material. A host agent must support this convention or provide an equivalent way to expose instructions and supporting files.

## Skills CLI

A common cross-agent installation route is the Skills CLI:

```bash
npx skills add azahathcr7/engineering-coach-app --skill engineering-workflow-coach
```

Use `npx skills add --help` to check current options and supported agents. Review target paths before accepting installation changes.

## Claude Code

Claude Code supports project skills under `.claude/skills/` and personal skills under `~/.claude/skills/`.

Project-local copy:

```bash
mkdir -p .claude/skills
cp -R skills/engineering-workflow-coach .claude/skills/
```

Personal copy (Git Bash):

```bash
mkdir -p ~/.claude/skills
cp -R skills/engineering-workflow-coach ~/.claude/skills/
```

Refresh the agent session if required, then confirm the skill appears in its available skills list.

## Other agent runtimes

For an agent that supports Agent Skills, install the entire skill directory into its documented skills folder. Do not copy only `SKILL.md`: the reference files are part of the package.

For products without filesystem skill discovery, expose `SKILL.md` through the product's supported project-instructions or knowledge mechanism and make the references accessible. This is a compatibility fallback, not proof of native skill installation.

## Verification

1. Ask the agent to identify the available `engineering-workflow-coach` skill.
2. Ask it to plan a small, non-production engineering change.
3. Check that it uses relevant role/lifecycle guidance and reports assumptions and verification clearly.
4. Invoke `grill me` or `hallmark` and verify the response style changes.
5. Confirm it can access relevant reference files.

## Important boundaries

Installing a skill supplies instructions and reference content. It does not install tools, connect accounts, grant repository or production permissions, execute code automatically, or make every AI chat product support native skill loading.
