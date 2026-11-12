---
name: bilingual-parity-check
description: Use before a bilingual AR/EN document is signed or sent.
---

# Bilingual parity check

Two versions of one document are not two documents. They are one object that has to say the same thing twice. This is the pass that catches drift before a counterpart does.

## When to run it

Before any Arabic/English pair leaves the building: a brief, a concept note, a press release, a deck, a ministerial letter. Run it every time, including when the second version was a quick translation.

## The six checks, in order

1. **Numbers.** Every figure in one version must appear in the other, with the same digits. Count them programmatically if you can. Currency, percentages, dates, years, hectares, tonnes, headcount.
2. **Names and titles.** Ministry names, programme names, personal names, job titles. A title that is more senior in one language is a political error, not a translation problem.
3. **Section order.** Same headings, same sequence, same nesting. A section that exists in one version and not the other is either an omission or an addition nobody approved.
4. **Commitments.** Sentences that promise, commit, request or approve. These must match in strength. "Will" is not "may"; "request" is not "note".
5. **Terms.** Every technical or institutional term uses the register's approved wording, consistently, from first use to last. One concept, one term, both languages.
6. **Direction.** Arabic layout right to left: paragraph direction, table column order, bullet position, page mirroring. Check the rendered file, not the source text.

## How to report

Not prose. A table:

| # | Location | Issue | AR | EN | Fix |
|---|---|---|---|---|---|

Severity on each row: **blocking** (fact or commitment differs), **major** (term, title, missing section), **minor** (style, spacing).

Close with one line: `Parity: CLEAR` or `Parity: N blocking, M major`.

## Rules that keep it honest

- **Do not translate to fix it.** If the versions differ, decide which one is right, then change the other. Translating the wrong sentence produces a polished error.
- **The Arabic is not the translation and the English is not the original.** Whichever version the counterpart will sign is the version of record; the other follows it.
- **A near-match is a mismatch.** Two different numbers that are close in value are worse than two obviously different ones, because nobody catches them.
- **If you cannot read both languages, say so.** Then check items 1 to 4 only, which need no fluency, and flag the rest.
