# Engineering Coach

A private, local-first engineering workflow companion. Plan work, break down tasks, run focused sessions, capture decisions, review blockers, and reflect on delivery without sending your work data to a server.

## Run it

1. Open `index.html` in a modern browser, or enable GitHub Pages for this private repository if your GitHub plan and organization settings support it.
2. The app works without a build step, package manager, API key, or backend.
3. Your data is stored in that browser's `localStorage`. Use **Export backup** regularly to save a JSON backup.

## Included

- Personal engineering dashboard and daily focus list
- Task board with priorities, status, estimates, due dates, and notes
- Guided task breakdown and blocker coaching
- Focus-session timer
- Decision and learning journal
- Weekly engineering review
- JSON export/import for backup and moving between browsers
- Responsive layout and keyboard-friendly controls

## Privacy and limitations

This is a client-side app. Tasks, notes, and settings stay in the browser profile where you use it. There is no account system, cloud sync, telemetry, or AI API integration. Importing a backup replaces the current local workspace after confirmation. Do not treat coaching prompts as a substitute for engineering judgment, security review, or production change controls.

## Project status

The repository includes the source Markdown for the Engineering Workflow Coach skill under `skills/engineering-workflow-coach/`: `SKILL.md` plus reference files for the architect path, beginner glossary, flavours, change lifecycle, role playbooks, and templates. These files preserve the supplied coaching specification. The current browser app remains a deterministic local-first companion; the Markdown skill is versioned as its coaching source of truth, but is not yet wired to a live model or runtime skill loader.

## Development

No dependencies are required. Validate by opening `index.html`, creating a task, changing its status, adding a journal entry, exporting a backup, and importing that backup into a clean browser profile.
