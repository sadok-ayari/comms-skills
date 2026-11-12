# comms-skills

Agent skills for institutional communications: the checks that decide whether a document is fit to sign.

Each folder holds one `SKILL.md`. Drop a folder into your agent's skills directory and it loads when the task matches. No dependencies, no build step.

| Skill | What it delivers | Use it when |
|---|---|---|
| [`bilingual-parity-check`](bilingual-parity-check/SKILL.md) | A severity-ranked table proving the Arabic and English versions of one document say the same thing | Before any bilingual brief, release, deck or letter is sent or signed |
| [`terminology-register`](terminology-register/SKILL.md) | A sourced, maintainable register of a counterpart's official wording | Drafting anything that carries an institution's names, programmes or titles |
| [`press-release-review`](press-release-review/SKILL.md) | A marked-up draft plus the list of what is missing and who must supply it | Before a release circulates internally or to a journalist |

## Install

**Claude Code**: copy the folders into `.claude/skills/` in your project, or `~/.claude/skills/` for every project.

```bash
cp -R bilingual-parity-check terminology-register press-release-review ~/.claude/skills/
```

**Any other agent** that reads `SKILL.md` frontmatter: point it at this directory. The format is plain YAML plus Markdown.

**No agent at all**: read the skill and follow it by hand. These are procedures, and they work on paper.

## Why these three and not more

They are the checks that fail silently. Grammar checkers, style guides and translation tools all pass a document whose Arabic and English disagree on a number, whose programme name changed last month, or whose quote does not survive contact with a journalist.

Each one is written to be run by a person as well as a model, and to end in a verdict rather than an opinion.

## House rules they encode

1. Every claim carries a source, or it does not ship.
2. The voice belongs to the counterpart, never to the adviser.
3. Write in the language of the room, and mean the same thing in each.
4. Automate the assembly, never the judgement.

## What is deliberately absent

Client registers, campaign content and counterpart vocabularies. Those belong to the institutions that own them, and they are not in this repository.

## Check it yourself

```bash
python3 check_skills.py
```

Validates frontmatter in every `SKILL.md`, checks description length, and asserts the repository carries no client-identifying strings.

## Licence

MIT. Written by Sadok Ayari.
