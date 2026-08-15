# Job Digest, 20 July 2026, supplemental

## Purpose

This is a one off supplemental digest. It does not add new roles and it does not change the applied log or the Notion mirror. It records the manual regeneration of seven previously drafted CVs and cover letters from the 18 July 2026 top ten run, which had been rendered on the English track even though the postings themselves were German language postings requiring at least B1. This regeneration is an explicit exception to the standing rule "do not regenerate or restyle any CV, cover letter, or digest already produced before this date", requested by Rah on 20 July 2026 during a review of the German language deliverables rule from 14 July 2026.

## What changed

The 18 July 2026 run generated 10 tailored CVs and cover letters. The initial run set `"lang": "en"` on all 10 entries in `role_configs_18jul.py`, which meant even German language postings requiring B1 or higher were rendered with English headings, English bullets, English profile, and English cover letter greeting and closing. That contradicts the 14 July 2026 rule, which activates the German track when both the posting body is in German and the stated German requirement is at least B1.

Rah asked to flip seven of the ten to the German track as a one off exception. The remaining two after that pass, RSG Group Werkstudent Data Analytics and SAP Master Thesis SCM on Agentic AI, were left on the English track because their postings do not clearly satisfy both conditions of the 14 July gate.

Later in the same session, Rah pushed back on the ATRIVIO decision after seeing the actual Indeed listing. The ATRIVIO posting is fully written in German including title, brief, "Dein Profil" section, and closing, but the posting does not state a required German level. On the strict reading of the 14 July gate ATRIVIO would stay English, since only one of the two conditions is met. On the practical reading a Kempten software house running the entire posting in German expects German speaking staff, and the intent of the rule is to send a language matched deliverable. ATRIVIO was therefore also flipped to the German track as a documented judgment call outside the strict gate, taking the eight regenerated total to eight.

For ATRIVIO specifically, the cover letter was retailored to the actual thesis brief. The mail2many newsletter system currently sends every recipient at the same user defined time, and the thesis goal is to build an AI method for per recipient optimal send times with an A/B based self learning loop and honest measurement of the effect on open and click rates. The cl_paragraphs reference this brief directly, along with Rah's eRay time series work, CreditIQ statistical evaluation and 100 percent branch coverage, and the RAG orchestrator's iterative feedback debugging.

## Eight roles regenerated on the German track

CeramTec Werkstudent Data Analytics Application, Plochingen. `drafts/CeramTec Werkstudent Data Analytics Application/`.
CeramTec Werkstudent Computer Vision, Plochingen. `drafts/CeramTec Werkstudent Computer Vision/`.
Draeger Abschlussarbeit Software Programmierung Computer Vision und Machine Learning, Lübeck. `drafts/Draeger Abschlussarbeit Computer Vision ML/`.
Debeka Werkstudent Data Intelligence Center DWH und BI, Koblenz. `drafts/Debeka Werkstudent Data Intelligence Center DWH BI/`.
MVV Energie Werkstudent Digital Empowerment GenAI und Analytics, Mannheim. `drafts/MVV Energie Werkstudent GenAI Analytics/`.
1KOMMA5 Werkstudent Quality Control Analyst Wärmepumpe, Home Office. `drafts/1KOMMA5 Werkstudent Quality Control Analyst Waermepumpe/`.
JOST-Werke Werkstudent Industrial AI und Process Innovation, Neu-Isenburg. `drafts/JOST-Werke Werkstudent Industrial AI/`.
ATRIVIO Masterarbeit KI gestützte Zeitpunktoptimierung für mail2many, Kempten Allgäu. `drafts/ATRIVIO Masterarbeit/`.

## What the pipeline produced this time

For each of the seven, `build_html.py` regenerated the docx CV, the html CV, the pdf CV, the docx cover letter, and the CV and cover letter markdown fallbacks, all in German. Verified for each role: section headings render as Persönliche Daten, Profil, Berufserfahrung, Ausbildung, Persönliche Projekte, Forschung und Abschlussarbeit, Zertifikate, Auszeichnungen, Sprachen. The Sprachen row shows Deutsch: B1 laufend Richtung B2. The contact line ends with Mannheim, Deutschland. The Berufserfahrung date range renders as Okt 2025 bis Mrz 2026. Cover letter greeting is Sehr geehrte Damen und Herren, closing is Mit freundlichen Grüßen, subject prefix is Bewerbung. All bullets, profile paragraphs, and cl_paragraphs are translated to German while keeping every real metric verbatim from `master-projects.md`.

Style pass done. No hyphens, no dashes, no parentheses in generated CV or cover letter content across all seven roles. Font floor, justified body, section dividers, entry level page break rules, and the navy plus rust palette are inherited from the shared template so they still hold.

Page count check on the seven regenerated PDFs, all landed at 3 A4 pages, which sits within the 19 July 2026 revised page length window of 2 to 3 pages. No CV needed manual overflow surgery.

## Applied log and Notion

Not touched. The seven rows already exist in `applied-log.csv` with status drafted from the 18 July 2026 run and mirror to the Notion Job Applications database, data source `fd974369-40b2-48c5-b660-d15256c88f52`. No new rows, no status changes, and the `Draft Path` values on the Notion rows still point at the same `drafts/[company]/` folders. Only the file contents inside those folders were replaced.

## Sources reachable this session

This session did not run the search step. No Indeed, StepStone, Xing, Glassdoor, LinkedIn Jobs, Tavily, or company page calls were made. This was purely a template and language track fix on already drafted roles.

## Note for the next scheduled run

The default `"lang": "en"` habit in the config generation step is the actual bug. When drafting a new posting, the config author must:

1. Read the posting body language.
2. Read the required German level.
3. If both hit the 14 July 2026 gate (body in German plus level at least B1), set `"lang": "de"` and use the `_DE` variants of `ERAY_BULLETS`, `DIABETES_BULLETS`, the project entries, the certificates, and `ACH_USAII`, all imported from `role_configs`.
4. Translate `profile`, `cl_subject`, `cl_date`, and every `cl_paragraphs` entry into German.

`build_html.py` did not need any change. The rendering side already switches all headings, dates, contact line country, greeting, and closing correctly when `cfg["lang"] == "de"`.
