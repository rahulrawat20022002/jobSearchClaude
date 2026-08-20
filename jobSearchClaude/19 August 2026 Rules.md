# 19 August 2026 CV Content Rules

Added after Rah reviewed a sample CV against a friend's Daimler-hire CV (the "Ojas comparison") on 19 August 2026. **Binding on every future draft**. Overrides any conflicting wording in older dated rules or existing `role_configs`. See [[CV Rules]] for the full historical sequence.

## Rule 1 — No hyphens or dashes anywhere in CV text

Not in project titles, not in bullets, not in the Skills line, not in the role tag under the name.

- `Multi-Agent RAG` → `Multi Agent RAG`
- `LLM-as-Judge` → `LLM as Judge`
- `fairness-by-design` → `fairness by design`
- `end-to-end` → `end to end`

This includes en dashes (`–`) and em dashes (`—`) as well as ASCII hyphens (`-`). The only exception is inside an identifier that must be reproduced verbatim to remain valid (a package name, a URL inside the contact block); such identifiers should not appear in bullet prose in the first place.

## Rule 2 — No parentheses or square brackets in bullets

Enumerations that used `(a, b, c)` are rewritten as a colon list `... on N dimensions: a, b, c ...` or as inline prose `... a, b, and c ...`. Same rule for German CVs.

## Rule 3 — Languages section = English + German only

Hindi is removed from the CV entirely. `master-projects.md` remains the source of truth for what appears on the CV; if a language is not listed there, it does not appear on the CV.

## Rule 4 — German level wording is locked

EN track prints exactly:

> `German: B1, in progress`

DE track prints exactly:

> `Deutsch: B1, laufend`

No `toward B2`, no `Richtung B2`, no other embellishment. Any actual level change must be made in `master-projects.md` first, then reflected in `build_html.py`.

## Rule 5 — No page numbers, headers, or footers in the CV PDF

The header of page 1 is name + role tag; every subsequent page starts directly with the next section entry. `build_html.py` must not emit CSS `@page` running headers or `counter(page)` footers, and the docx renderer must not add section footers with `PAGE` fields.

## Rule 6 — CV hard cap = 2 pages

Tightened from the 4 August 2026 three page cap (see [[CV Rules]]). The overflow ladder in `build_html.py` (see [[build_html.py Overview]]) must trim until `pages <= 2`. A role that cannot fit 2 pages after the full ladder halts per invariant #3 (halting beats a false success); Rah decides what to cut. See [[Playbook - 2 Page Cap Exceeded]].

## Rule 7 — Header layout is Ojas-style, PERSONAL DETAILS block retired

After Rah's 19 Aug 2026 comparison against a friend's Daimler-hire CV, the CV header is now:

```
name
positioning tag (cfg['tag'] or fallback cfg['role_strip'])
contact line 1 (City · phone · email)
contact line 2 (portfolio · github · linkedin, bare URLs, no labels)
italic status line (enrollment · availability · visa)
divider
```

Address, DOB, and formal nationality phrasing are removed. The old `PERSONAL DETAILS` section header and all `Portfolio: / Date of birth: / Nationality: / Availability:` rows **must NOT appear** on any new CV.

## Rule 8 — Skills grouped into functional buckets, not a flat comma line

Five buckets (see [[Skills Buckets]] for the full contents):

1. `AI and Agents` / `KI und Agenten`
2. `Data and ML` / `Daten und ML`
3. `Cloud and Orchestration` / `Cloud und Orchestrierung`
4. `Dashboards`
5. `Web`

Rendered as a two-column table in HTML and PDF, and as `Label: items` paragraphs in docx.

**Removed** as they are not evidenced in any project bullet (keyword stuffing violates invariant #3): `Databricks`, `Delta Lake`, `LangChain`, `PyTorch`.

## Rule 9 — Positioning tag under the name is a pitch, not the posting title

Author `cfg['tag']` per role. Examples:

For agentic-AI roles:

> `Data Science Master's Student | RAG Evaluation & Credit Fairness | Python + LangGraph`

For BI/analytics roles:

> `Data Science Master's Student | Analytics Pipelines & Dashboards | Python + SQL + BigQuery`

When `cfg['tag']` is omitted the header falls back to `cfg['role_strip']` (the posting title), which is acceptable but suboptimal.

## Rule 10 — Overrides the STEP 4 validation gate

The scheduled task prompt's STEP 4 gate says `the second line under the name contains rahulrawat2r@gmail.com`. That rule was written for the retired `PERSONAL DETAILS` layout. Under the new header the second line is the positioning tag; email lives on line 3 (contact line 1).

**Treat as SATISFIED** under the new header:

- `email on line 2` check
- `SKILLS\n` banned string check
- `PERSONAL DETAILS` banned string check

**Still binding** and enforced by the build:

- `toward B2` banned string
- `Databricks` banned string
- `Delta Lake` banned string
- `LangChain` banned string
- `PyTorch` banned string
- The 2 page requirement

## See also

- [[CV Rules]] for the full historical sequence
- [[Skills Buckets]] for what belongs in each of the five buckets
- [[build_html.py Overview]] for how these rules are enforced
