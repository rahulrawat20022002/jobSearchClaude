# CV Rules, Historical Dated Rules In Date Order

Every rule below was created on the date shown and either still binds or is explicitly marked superseded. When in doubt about the exact wording of a historical rule, consult the digest that first cited it or the routing notes in `master-projects.md`. The current authoritative shape of the CV is defined in [[19 August 2026 Rules]].

Cross-cutting reference: shared invariant #8 in [[Pipeline Overview]] says "historical dated rules remain binding".

## 11 July 2026 — Reconciliation on paused runs

The CSV-Notion reconciliation step ([[01 Agent A - Cowork Drafting]] STEP 3) runs even when the backlog gate says pause. Rah still wants drift caught on days no new drafting happens. See [[Playbook - Notion CSV Drift]].

## 12 July 2026 — Warm outreach

For every drafted role, look up a plausible LinkedIn contact (recruiter, hiring manager, or team lead in the target function) and populate `LinkedIn Profile` + `LinkedIn Message` fields in Notion. The outreach itself is executed by [[02 Agent B - OpenClaw Submission]] STEP 4, paste-only, Rah clicks send.

## 14 July 2026 — Notion is the source of truth for row status

Retroactively overrides earlier CSV-first behaviour. The `Status` column in Notion wins over the same column in `applied-log.csv` whenever the two disagree. CSV is a mirror only. Written as shared invariant #1.

## 18 July 2026 — XYZ bullet format

Every experience bullet follows the XYZ shape: "Accomplished X (metric) by doing Y (approach) resulting in Z (outcome)". Bullets that read as pure responsibilities without a Z clause are rewritten.

## 19 July 2026 — Lebenslauf CV layout

German CVs (DE track) follow the Lebenslauf convention: reverse-chronological blocks with role/company/dates aligned, then bullets. Applies to the DE render only.

## 20 July 2026 — Language match

Every deliverable inherits its language from the posting body language. DE posting → DE CV + DE cover letter. EN posting → EN CV + EN cover letter. No mixing.

## 28 July 2026 — Yield reset (backlog gate)

Overrides earlier flat daily caps. Backlog gate:

- Under 8 drafted in Notion → normal top 3 to 5
- 8 to 10 → cap at top 3
- 11 or more → hard pause, skip drafting

Indeed source is capped at 1 per run under the same yield weighting (Indeed's yield of interview-track responses per drafted role was measured lowest across sources).

## 2 August 2026 — SS Engineers, two Experience entries

The SS Engineers role at Rah's earlier stint is split into two Experience entries (different job titles held), not merged into one. This rule fixed a specific miscount and applies to that employer only. Documented here so future edits do not accidentally re-merge.

## 4 August 2026 — CV three page hard cap (SUPERSEDED)

Original cap was three pages. Superseded on 19 August 2026 by the two page hard cap. Preserved here because older digests reference the three page rule.

## 4 August 2026 — Projects cap

Projects section caps at N entries selected by relevance to the target role. Beyond that, drop least-relevant projects from the render, not just visually truncate.

## 4 August 2026 — Signature retired

The typed signature block at the end of the cover letter (name in italics under `Sincerely,`) was dropped. Cover letter now ends at the closing line.

## 11 August 2026 — Reconciliation, tightened

Reconciliation is now step 3 of the Cowork run (not step 5 as it briefly was in July). Runs before drafting so Notion state is fresh before quota decisions are made. See [[01 Agent A - Cowork Drafting]] STEP 3.

## 11 August 2026 — CoverLetter PDF required

Every drafted role must produce all eight deliverables including `CoverLetter_Rahul_Rawat.pdf`. This closed a loophole where cover letters were sometimes shipped as docx only, which [[02 Agent B - OpenClaw Submission]] could not upload via its DataTransfer method.

## 11 August 2026 — ATS section order

The ATS-safe section order in the CV is: Header → Profile → Skills → Experience → Education → Certifications → Languages. Projects sit between Experience and Education when included. No `PERSONAL DETAILS` section (retired 19 Aug 2026, but the intent traces back to this rule making the layout ATS-first).

## 11 August 2026 — CV strip retired

The `[EN] / [DE]` language strip that briefly appeared under the name was retired. Language is inferred from the posting per the 20 July 2026 rule; no visible marker on the CV.

## 12 August 2026 — Freshness

Only postings from the last 14 days are candidates for scoring. Older postings are dropped in STEP 4 filter unless explicitly re-surfaced by Rah.

## 13 August 2026 — Platform native + DataTransfer

Two-part rule:

1. [[02 Agent B - OpenClaw Submission]] scope is narrowed to platform native listings only. Company portal listings become out of scope, see [[03 Rah Manual - Company Portals]].
2. Platform native uploads use the JavaScript DataTransfer injection method rather than the direct file-input click, which some platforms reject. Verify `input.files[0].name` and size after injection.

## 19 August 2026 — Current authoritative CV shape

All ten rules in [[19 August 2026 Rules]] are binding on every future draft and override any conflicting wording in older dated rules or existing `role_configs`. This includes:

- No hyphens or dashes anywhere in CV text
- No parentheses or square brackets in bullets
- Languages section = English + German only (Hindi removed)
- German level locked to `B1, in progress` / `B1, laufend`
- No page numbers, headers, or footers in the CV PDF
- CV hard cap = 2 pages (tightened from 4 Aug 3 page cap)
- Header layout is Ojas-style, `PERSONAL DETAILS` block retired
- Skills grouped into functional buckets, see [[Skills Buckets]]
- Positioning tag under the name is a pitch, not the posting title
- Overrides the STEP 4 validation gate's `email on line 2` and `SKILLS\n / PERSONAL DETAILS` banned strings (they were written for the retired PD layout)

## See also

- [[19 August 2026 Rules]] — full text of the current rules
- [[Skills Buckets]] — the five buckets and their contents
- [[build_html.py Overview]] — how the render enforces these rules
