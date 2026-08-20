# Repo File Structure

The repo lives at `github.com/rahulrawat20022002/jobSearchClaude`. In-flight cloud runs use `/tmp/JobSearch`, Rah's Mac uses `~/Desktop/jobSearchClaude`. Both are working checkouts of the same tracked history. Git is the source of truth for content per invariant #2 (see [[Pipeline Overview]]).

## Top level

| Path | What it is |
|---|---|
| `CLAUDE.md` | Rule book for both agents. Read at run start by both. Edited by Rah only. |
| `README.md` | Placeholder; the real entry point is `CLAUDE.md`. |
| `master-projects.md` | Source of truth for what the CV can claim: projects, bullets, languages, certifications. See [[Skills Buckets]] for the "must be evidenced in a bullet" rule. |
| `pipeline-context.md` | Short context primer for onboarding a fresh session; do not treat it as a rule source. |
| `.gitignore` | OS + Python noise + `.env` + (as of 19 Aug 2026) the Obsidian vault folder. |

## Render pipeline

| Path | What it is |
|---|---|
| `build_html.py` | The render module. Contains `html_cv()`, `docx_cv()`, `html_cover_letter()`, `docx_cover_letter()`, `render_role()` (which drives the overflow ladder), `SKILL_BUCKETS_EN`/`SKILL_BUCKETS_DE`. See [[build_html.py Overview]]. |
| `role_configs.py` | Long-lived config for the CV header, contact block, static Experience entries, static Certifications, static Research bullets. Also holds `SATENDRA_FT_BULLETS_EN/DE` and `SATENDRA_INTERN_BULLETS_EN/DE`. |
| `role_configs_YYYYMMDD.py` | Per-run config file authored fresh each day by [[01 Agent A - Cowork Drafting]] STEP 5. Contains the per-role `cfg` dict for every role drafted that day. |
| `run_YYYYMMDD.py` | Per-run entry point. Imports the matching `role_configs_YYYYMMDD.py` and calls `render_role()` for each cfg. |
| `sample_cv_render.py` | One-off script for smoke testing a header change or a bucket update without running the full pipeline. |
| `render_ats_sample.py` | Renders an ATS-safe sample for template review. Not part of the daily flow. |

## Data files

| Path | What it is |
|---|---|
| `applied-log.csv` | Mirror of Notion for offline browsing and quick greps. Notion always wins on drift (see [[Playbook - Notion CSV Drift]]). Written by [[01 Agent A - Cowork Drafting]] STEP 6. |
| `applied-log.csv.bak*` | Timestamped backups written before each STEP 6 append. Kept for audit. |

## Deliverables

| Path | What it is |
|---|---|
| `drafts/[folder]/` | One folder per drafted role. Folder name = `Company_Role_Location_YYYYMMDD` or similar. Contains all 8 deliverables per the 11 August 2026 rule. See [[01 Agent A - Cowork Drafting]] STEP 5. |
| `drafts/[folder]/CV_Rahul_Rawat.md` | Markdown source of the CV. |
| `drafts/[folder]/CV_Rahul_Rawat.html` | HTML render of the CV. |
| `drafts/[folder]/CV_Rahul_Rawat.pdf` | PDF render (what OpenClaw uploads for platform native). |
| `drafts/[folder]/CV_Rahul_Rawat.docx` | Word render. |
| `drafts/[folder]/CoverLetter_Rahul_Rawat.{md,html,pdf,docx}` | Same four formats for the cover letter. PDF is required per 11 August 2026 rule. |
| `additional documents/` | Supporting uploads for company portal submissions: `Certificate_of_Enrolment.pdf`, `transcript.pdf`, `highest_degree.pdf`, `ausweis (1).pdf`. Never upload the ID unless explicitly required. |

## Daily digests

| Path | What it is |
|---|---|
| `Job_Digest_YYYY-MM-DD.md` | Written by [[01 Agent A - Cowork Drafting]] STEP 7. Contains top cut, watchlist, dropped roles, transparency block, backlog gate result, platform breakdown, language track decisions, and apply method per role. |
| `Job_Digest_YYYY-MM-DD_supplemental.md` | Written when a same-day PM run adds roles after a morning run. |
| `OpenClaw_Apply_Run_YYYY-MM-DD.md` | Written by [[02 Agent B - OpenClaw Submission]] STEP 6. Never git committed by Agent B (Agent B forbids itself from touching tracked files). Rah commits and pushes it manually if he wants it in history. |

## Templates and reference

| Path | What it is |
|---|---|
| `CV_Template.docx` | Blank docx template that `build_html.py`'s docx renderer opens as base. |
| `CoverLetter_Template.docx` | Same for the cover letter docx renderer. |
| `CV_Preview_v1.html` / `CV_Preview_v2.html` / `CV_Preview_v3.html` | Historical CV preview iterations. Not touched by the render pipeline. |
| `CV_Sample_ThreeExperience.{html,pdf}` | Reference sample used during the 2 August 2026 SS Engineers split. |
| `ats_sample_preview/` | Output folder of `render_ats_sample.py`. |
| `LinkedIn_eRay_Experience.md` | Reference bullet source for the eRay experience block. |
| `SKILL_updated_2026-07-02.md` | Historical skills brainstorm; superseded by [[Skills Buckets]]. |

## Diagrams

| Path | What it is |
|---|---|
| `pipeline_diagram.drawio` | Source (draw.io / diagrams.net) for the pipeline diagram. Edit here first. |
| `pipeline_diagram.png` | Rasterised diagram. Embedded in [[Pipeline Overview]]. Regenerate from the drawio when the pipeline changes. |
| `pipeline_diagram.svg` | Vector export for embedding in HTML digests. |

## One-offs and backups

| Path | What it is |
|---|---|
| `one-offs/` | Ad hoc experiments and one-shot renders that do not belong in the daily flow. |
| `_regen_backups/` | Snapshots of prior render output kept during pipeline changes. |
| `_p1.png` / `_p2.png` / `_p3.png` / `_preview*.png` | Per-page rasterisations produced by the render for eyeballing. |
| `certificates/` | Source images and scans of Rah's certificates for the Certifications block. |
| `photo.png` / `photo_rah.jpg` | Header photo (unused in the 19 Aug 2026 layout, which is text only). |
| `Screenshot 2026-07-30 at 19.02.58.png` | Ad hoc screenshot kept for reference. |

## See also

- [[build_html.py Overview]] for what the render module actually does
- [[01 Agent A - Cowork Drafting]] STEP 5 for how per-run configs are authored
- [[Daily Workflow]] for how these files flow through a normal day
