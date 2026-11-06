from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "engineering-workflow-coach"
SKILL = SKILL_DIR / "SKILL.md"

REQUIRED_REFERENCES = [
    "architect-path.md",
    "beginner-glossary.md",
    "flavours.md",
    "lifecycle.md",
    "roles.md",
    "templates.md",
]

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)

if not SKILL.is_file():
    fail("Missing skills/engineering-workflow-coach/SKILL.md")

content = SKILL.read_text(encoding="utf-8")
if not content.startswith("---\n"):
    fail("SKILL.md must start with YAML frontmatter")

frontmatter = content.split("---", 2)
if len(frontmatter) < 3:
    fail("Malformed SKILL.md frontmatter")

meta = frontmatter[1]
name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", meta)
description = re.search(r"(?m)^description:\s*(.+)$", meta)
if not name or name.group(1) != "engineering-workflow-coach":
    fail("Skill name metadata is missing or invalid")
if not description or len(description.group(1).strip()) < 20:
    fail("Skill description metadata is missing or too short")

for ref in REQUIRED_REFERENCES:
    path = SKILL_DIR / "references" / ref
    if not path.is_file():
        fail(f"Missing reference: {path.relative_to(ROOT)}")

for md in [SKILL, *sorted((SKILL_DIR / "references").glob("*.md"))]:
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        local = (md.parent / target.split("#", 1)[0]).resolve()
        if not local.exists():
            fail(f"Broken relative link in {md.relative_to(ROOT)}: {target}")

for retired in ["index.html", "manifest.json", "sw.js"]:
    if (ROOT / retired).exists():
        fail(f"Retired app file must not exist: {retired}")

print("PASS: skill metadata, references, links, and skill-only repository checks")
