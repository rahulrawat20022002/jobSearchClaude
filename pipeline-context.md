# Pipeline Context — paste into any new project chat for full handoff

> Copy everything below the line into the first message of a new chat (inside the
> Job Search project) so a fresh Claude has the full picture without re-explaining.
> Keep this file updated if the pipeline changes — otherwise it drifts out of sync.

---

**Context: my automated job-search pipeline (already built — help me run/improve it, don't rebuild from scratch)**

Who I am: Rahul Rawat, based in Mannheim, Germany. MSc Data Science & Analytics at SRH Heidelberg. German level A2.2. Targeting roles: Data Engineer, Data Analyst, Business Analyst, Data Scientist, AI/ML Engineer — Werkstudent/part-time and internship (including a mandatory internship). Location: anywhere in Germany, or remote in the EU.

What I've built: a semi-automated job-search pipeline running in **Claude Cowork** (desktop, Mac, Pro plan, Sonnet 4.6). Connectors live: Indeed, Gmail, Google Drive, Google Calendar, and Claude in Chrome.

Folder: `~/JobSearch` on my Mac, containing:
- `CLAUDE.md` — folder instructions the pipeline obeys every run
- `master-projects.md` — my profile, target roles, filtering rules, and 9 projects each tagged with the role types they fit
- `applied-log.csv` — application tracker (columns: date, company, role, location, source, status, draft_path)
- `CV_Template.docx` and `CoverLetter_Template.docx` — fixed-layout templates with `[[placeholder]]` slots filled per role
- `drafts/[company]/` — generated tailored CVs + cover letters

How the pipeline works: every 2 days it searches Indeed (DE + remote EU) and browses Xing/StepStone/Glassdoor/company career pages via Claude in Chrome. It drops dual-study/apprenticeship programmes and recruiter "Quereinsteiger/career-changer" ads, but keeps German-language listings (tagging each with required German level). It scores roles on recency, distance from Mannheim/remote, and overlap with my projects' tags. Dedup is on **company + role** (multiple different roles at one company are allowed; the same company+role is not re-drafted). For the top 5 it copies the templates, replaces only the `[[placeholders]]`, and saves both `.docx` and `.pdf` into `drafts/[company]/`, then appends rows to `applied-log.csv` (status `drafted`) and emails me a digest. It never auto-submits — I apply manually.

Two fixed rules in the templates: the CV's **Experience section contains only the eRay GmbH × SRH "Lake Water Quality Forecasting" industry collaboration** — nothing else. And the layout is never restructured, only the placeholders get filled.

Key constraints: Cowork's scheduled runs only fire when the Desktop app is open and my Mac is awake. On Pro, the Claude-in-Chrome (Xing/StepStone) leg runs on a weaker model and is the most fragile part — login walls can make it return thin results, while Indeed stays reliable.

Health-check prompt I paste when a digest looks off: *"Run a pipeline health check, don't search for new jobs. Report: (1) did Indeed return results; (2) did Claude in Chrome load Xing/StepStone or hit a login wall; (3) how many companies in applied-log.csv and how many skipped as duplicates; (4) did the digest email send. 4-line status."*

Confirm you've got this context, then I'll tell you what I need today.
