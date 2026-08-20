# build_html.py Overview

The single render module. Everything that turns a per-role `cfg` dict into deliverables goes through here. Called by `run_YYYYMMDD.py` for each role in `role_configs_YYYYMMDD.py` during [[01 Agent A - Cowork Drafting]] STEP 5. See [[File Structure]] for the surrounding files.

Total ~1200 lines. Line numbers below are approximate and drift as the file changes; use `grep -n` to locate exact positions.

## Public entry points

| Symbol | Line (approx) | Purpose |
|---|---|---|
| `html_cv(cfg)` | ~358 | Returns the HTML string for the CV. Reads `cfg['lang']` to pick EN or DE. Emits the Ojas-style header, the grouped skills table (see [[Skills Buckets]]), the three Experience entries (per 2 Aug 2026 rule), Projects, Education, Certifications, Languages block. |
| `docx_cv(cfg)` | ~800 | Word render. Emits the same content with docx-specific styling. No section footers with `PAGE` fields (19 Aug 2026 rule 5). |
| `html_cover_letter(cfg)` | ~900 | HTML render of the cover letter. |
| `docx_cover_letter(cfg)` | ~950 | Word render of the cover letter. |
| `render_role(cfg)` | ~1000 | Top-level orchestrator. Drives the overflow ladder, writes all 8 deliverables into `drafts/[folder]/`. This is what `run_YYYYMMDD.py` calls per role. |

## The skill buckets

Defined at ~line 320:

```
SKILL_BUCKETS_EN = [
    ("AI and Agents", [...]),
    ("Data and ML",   [...]),
    ("Cloud and Orchestration", [...]),
    ("Dashboards", [...]),
    ("Web", [...]),
]
SKILL_BUCKETS_DE = [
    ("KI und Agenten", [...]),
    ("Daten und ML",   [...]),
    ("Cloud und Orchestrierung", [...]),
    ("Dashboards", [...]),
    ("Web", [...]),
]
```

Full contents in [[Skills Buckets]]. `_skill_buckets(cfg)` at ~line 341 returns the right list based on `cfg['lang']`, or the per-role override at `cfg['skill_buckets']` when set.

`DEFAULT_SKILLS` and `_skills_line(cfg)` are legacy holdovers kept only so any external caller of `_skills_line()` still resolves. The current render pipeline does NOT use them.

## The header block (19 August 2026 layout)

`html_cv()` starts by picking `HDR_EN` or `HDR_DE`, then emits five text elements before the divider:

1. **Name** — from `cfg['name']` or the static default.
2. **Positioning tag** — `cfg['tag']` per role. Fallback to `cfg['role_strip']` (the posting title) if `cfg['tag']` is missing. Rule 9 of [[19 August 2026 Rules]].
3. **Contact line 1** — `City · phone · email`. Localised: `Mannheim, Germany` (EN) vs `Mannheim, Deutschland` (DE).
4. **Contact line 2** — `portfolio · github · linkedin`. Bare URLs, no `Portfolio:` / `GitHub:` labels. Rule 7 of [[19 August 2026 Rules]].
5. **Italic status line** — `enrollment · availability · visa`. EN: `Enrolled through April 2027 · Available immediately · Student visa with work permit`. DE: `Immatrikuliert bis April 2027 · Sofort verfügbar · Studentenvisum mit Arbeitserlaubnis`.

The retired `PERSONAL DETAILS` block, `Portfolio:` / `Date of birth:` / `Nationality:` / `Availability:` rows, and the header photo are all gone.

## The language block

Emitted after Certifications, before the divider that closes the CV body. Hard-coded per rule 4 of [[19 August 2026 Rules]]:

- EN track: `English: fluent`, `German: B1, in progress`
- DE track: `Englisch: fließend`, `Deutsch: B1, laufend`

Hindi is not emitted regardless of what `master-projects.md` says (rule 3 dropped it explicitly).

## The overflow ladder (`render_role`)

Around line 1030 to 1090. Enforces rule 6 (2 page hard cap):

1. Start from defaults: up to 2 projects at 3 bullets each, eRay 3 bullets, SS FT 2 bullets, SS intern 1 bullet, all certs kept, all research bullets kept.
2. Render the CV, run `weasyprint.HTML(...).write_pdf(...)`, count pages with `pypdf.PdfReader(...).pages`.
3. If `pages <= 2` → done, write the HTML and continue.
4. Else, tighten the config per the next ladder rung and retry.

Ladder rungs in order:

- Drop trailing Personal Projects entries, one at a time (least relevant first, since `master-projects.md` orders projects by relevance).
- Drop trailing Personal Projects entries with 2 bullets per entry instead of 3.
- Keep 1 project + 2 PP bullets + reduce SS FT to 1 bullet.
- 19 Aug 2026 additions: drop the 4th eRay bullet, then the 3rd.
- Drop certificates one at a time from the tail.
- Trim research bullets from the tail.
- Densest possible: 1 project, 1 PP bullet, SS FT 1, SS intern 1, eRay 1, 1 cert, 1 research bullet.

If the ladder exhausts and `pages` is still > 2, `render_role` raises:

```
RuntimeError: CV PDF for [folder] still N pages after full overflow ladder
    (19 Aug 2026 hard 2 page cap). Steps tried: [...].
    Tighten the profile paragraph in the config or drop a certificate for this role.
```

See [[Playbook - 2 Page Cap Exceeded]] for the fix flow.

## The docx path (parallel structure)

`docx_cv()` mirrors `html_cv()` but emits the header as paragraph blocks with docx run formatting, and emits the skills buckets as `Label: items` paragraphs instead of a two column table (rule 8's docx form).

The docx does NOT add section footers with `PAGE` fields (rule 5). This is enforced at the template level: `CV_Template.docx` has no footer defined.

## Where the SS Engineers bullets come from

`role_configs.py` exports:

- `SATENDRA_FT_BULLETS_EN` / `SATENDRA_FT_BULLETS_DE`
- `SATENDRA_INTERN_BULLETS_EN` / `SATENDRA_INTERN_BULLETS_DE`

`html_cv()` at ~line 382 imports these and truncates by `cfg['ss_ft_max_bullets']` and `cfg['ss_intern_max_bullets']` (both driven by the overflow ladder). `master-projects.md` remains the source of truth; the constants above are its curated CV-ready form.

## Related tools

- `sample_cv_render.py` — smoke test a header change without running the full pipeline.
- `render_ats_sample.py` — dump an ATS-safe sample into `ats_sample_preview/`.
- `pipeline_diagram.drawio` — source for the diagram embedded in [[Pipeline Overview]]. Regenerate PNG and SVG when the pipeline changes.

## See also

- [[19 August 2026 Rules]] for the rules this module enforces
- [[Skills Buckets]] for the current bucket contents
- [[Playbook - 2 Page Cap Exceeded]] when the overflow ladder exhausts
- [[Playbook - Render Toolchain Failed]] when weasyprint or python-docx fails to import
