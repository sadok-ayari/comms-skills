---
name: terminology-register
description: Use when one institution's wording must be used exactly.
---

# Terminology register

An institution does not have vocabulary. It has a position, expressed in words: the legal name of a department, the official name of a programme, the term a minister uses in the chamber. Get one of those wrong and the document reads as foreign, whatever else it does well.

This skill builds and maintains the register that keeps you inside it.

## Build the register first

One file per counterpart, in the vault or beside the project. Before drafting a record, confirm the owner: which body signs this, which department owns it, which spelling is legal.

```yaml
counterpart: <name>
sources:
  - <official site or document>  # where the wording was verified
terms:
  - en: <English term>
    ar: <Arabic term>
    status: official | internal | deprecated
    source: <url or document reference>
    note: <what it replaced, and when>
```

## The four rules

1. **Verify at the source, not from memory.** The body's own site, its own publications, its own letterhead. Model memory of official names is unreliable and fails silently.
2. **Record renames as facts.** Programmes and departments get renamed. Keep the old term with `status: deprecated` and the date. A register that forgets the old name cannot explain a document from last year.
3. **One concept, one term.** If the register says a word, use that word everywhere, in both languages. Synonyms are drift.
4. **Quote the source line.** Every entry carries where it came from. An entry without a source is a guess wearing a uniform.

## Use it while drafting, not after

Check terms at the point of writing. A post-hoc terminology sweep rewrites sentences that were built around the wrong word, and the repair shows.

## When the register has no entry

Stop and say so. `[Unverified]` beside the term, and a line to the counterpart's own communications office. Never substitute a plausible translation for an official one, and never let a plausible one survive into a signed document.

## Handover

The register belongs to the counterpart, not to the adviser. On handover, give the file, the sources and the open questions. That is the difference between a deliverable and a dependency.
