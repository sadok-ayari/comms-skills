"""Validate every skill in this repository.

Checks the things a reader depends on: a parseable frontmatter block with a
name and a short description, and no client-identifying strings anywhere.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
FORBIDDEN = ["qatar", "mecc", "gggi", "oman", "arise", "nccac", "morocco", "jordan", "awal"]
SKILLS = sorted(p for p in ROOT.iterdir() if (p / "SKILL.md").exists())


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def main():
    errors = []
    if not SKILLS:
        errors.append("no skills found")
    for skill in SKILLS:
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm.get("name") != skill.name:
            errors.append(f"{skill.name}: frontmatter name is {fm.get('name')!r}, folder is {skill.name!r}")
        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{skill.name}: missing description")
        elif len(desc) > 60:
            errors.append(f"{skill.name}: description is {len(desc)} chars, limit 60")
        if len(text) < 800:
            errors.append(f"{skill.name}: suspiciously short ({len(text)} chars)")
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".py", ".yml", ".yaml"}:
            low = path.read_text(encoding="utf-8", errors="ignore").lower()
            for token in FORBIDDEN:
                if token in low and path.name != Path(__file__).name:
                    errors.append(f"{path.relative_to(ROOT)}: contains {token!r}")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print(f"OK: {len(SKILLS)} skills, frontmatter valid, no client strings")
    for s in SKILLS:
        print("  -", s.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
