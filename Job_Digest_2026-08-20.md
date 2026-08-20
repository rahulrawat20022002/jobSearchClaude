# Job Search Digest, 20 August 2026

## Run type and render toolchain

- Run type: scheduled Cowork Agent A run (drafting only). Fresh /tmp/JobSearch checkout, pipeline invoked via `python3 run_20aug.py`.
- Render toolchain: OK. `weasyprint 69.0`, `python-docx`, `pypdf` installed cleanly. Preflight `import weasyprint, docx, pypdf` succeeded.

## Backlog gate

- Notion data source fd974369-40b2-48c5-b660-d15256c88f52 queried at run start.
- Rows with Status = drafted at run start: **0**. Gate zone: under 8 → normal top 3 to 5 cut (28 July 2026 yield reset). Fallback to CSV was NOT needed; Notion returned successfully on first query.
- Backlog after run: 5 drafted (the five roles below). This run targets the top of the 3 to 5 range because the backlog was empty at start.

Second pass note: the first-pass digest reported 3 drafted. On re-read of the gate the run was expanded to 5 to hit the top of the "under 8 = top 3 to 5" range, and two supplemental roles (Bosch Rexroth, Ardex) were added.

## Reconciliation

Notion is the source of truth per invariant #1. Every CSV row matched a Notion row by (company, role) case insensitive. Eleven CSV rows still carrying `drafted` had already moved on in Notion; the CSV was updated to match. No Notion writes were made from the CSV side.

Drift fixed on the CSV side:

| Company | Role | CSV before | Notion truth |
|---|---|---|---|
| Retorio | Working Student, AI Engineer Agentic Systems | drafted | Not listed Anymore |
| AssetMetrix GmbH | Working Student, AI Engineering | drafted | applied |
| Phoenix Contact | Werkstudent, Data Science und KI | drafted | applied |
| BSH Home Appliances Group | Working Student, Engineering Data Analytics and Classification | drafted | rejected |
| viadee Unternehmensberatung AG | Werkstudent, Data Science und Process Mining | drafted | rejected |
| BMW Group | Werkstudent, Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse | drafted | applied |
| KfW Bankengruppe | Werkstudent, IT Data Science und KI | drafted | applied |
| Allianz Insurance | Working Student, Data Science | drafted | applied |
| Siemens Energy | Werkstudent, KI-basierte Optimierungsinitiativen | drafted | applied |
| Siemens AG | Werkstudent, Data Science im operativen Service | drafted | rejected |
| Deloitte | Werkstudent oder Praktikant, Digital und AI Analytics | drafted | rejected |

CSV backup written to `applied-log.csv.bak_20260820` before the update.

## Top cut

### 1. Amprion GmbH — Werkstudent KI (Stellen-ID 7959), Dortmund

- Freshness: posted ~2 days ago via Xing; primary source jobs.amprion.net (Company Page).
- Language track: DE (posting body in German).
- Apply method: company-portal (jobs.amprion.net; Xing routes to the company portal).
- Apply link: https://jobs.amprion.net/offer/werkstudent-ki-m-w-d/df7261d9-a116-4a2b-bc2e-70d2d113f93c
- Fit rationale: team "Unternehmensweite IT-Loesungen" runs Wissens- und Dokumentenmanagement plus digital-workplace projects; that maps directly to the Multi-Agent RAG project (LangGraph orchestrator, EN/DE end to end, LLM-as-Judge Qwen2.5 14B vs Mistral 7B, 5-dim JSON scoring, 5 retrieval + 4 generation metrics per language) and to the Movie Analytics medallion architecture on BigQuery/Cloud Run for the pipeline side.
- Projects selected: Multi-Agent RAG (P_RAG_DE), Movie Analytics medallion (P_MOVIE_DE). Auto-trim ladder dropped to 1 project + tightened SS bullets to fit 2 pages.
- Certs selected: NVIDIA (LLM Applications), AWS (Cloud Foundations), Google Data Analytics.
- Deliverables at drafts/Amprion Dortmund Werkstudent KI/: CV_Rahul_Rawat.{md,html,pdf,docx} + CoverLetter_Rahul_Rawat.{md,html,pdf,docx}. All 8 files present, CV PDF 2 pages, CL PDF 1 page (tight CSS applied).

### 2. Ed. Zueblin AG — Werkstudent Business Intelligence and Data Analytics, Stuttgart

- Freshness: posted ~1 week ago on StepStone.
- Language track: DE (posting body in German).
- Apply method: platform-native via StepStone Schnelle Bewerbung; if the flow redirects to a Zueblin or STRABAG-owned careers portal, OpenClaw will re-flag it as company-portal per the 16 Aug 2026 split.
- Apply link: https://www.stepstone.de/stellenangebote--Werkstudent-in-m-w-d-Business-Intelligence-Data-Analytics-Stuttgart-Ed-Zueblin-AG--14395739-inline.html
- Fit rationale: role owns Qlik Sense and Power BI dashboards, validation and structuring of data. Movie Analytics medallion + Looker Studio and the Fast Food Tableau dynamic-cart + parameter-driven Y-axis project cover interactive dashboard design; eRay's 3-pass outlier + z-score + sensor-exclusion evaluation gives concrete evidence of "Validierung, Bereinigung und Strukturierung von Datenbestaenden."
- Projects selected: Movie Analytics (P_MOVIE_DE), Fast Food Tableau (P_TABLEAU_DE). Auto-trim ladder dropped to 1 project.
- Certs selected: SAS Visual Business Analytics, Google Data Analytics, AWS Cloud Foundations (BI/analytics-leaning per master-projects.md routing note).
- Deliverables at drafts/Ed Zueblin Stuttgart Werkstudent BI Data Analytics/: all 8 files present, CV PDF 2 pages, CL PDF 1 page (tight CSS applied).

### 3. PwC Deutschland — Werkstudent AI Adoption and Enablement, Saarbruecken

- Freshness: posted ~1 week ago on LinkedIn.
- Language track: DE (LinkedIn listing carries `w/m/d` marker and PwC's public AI Enablement portfolio at pwc.de is fully in German for this line of service).
- Apply method: company-portal likely (PwC's LinkedIn Apply typically redirects to jobs.pwc.de). Left as company-portal on the Notion row so OpenClaw will not attempt an auto-submission per the 16 Aug 2026 split.
- Apply link: https://de.linkedin.com/jobs/view/werkstudent-ai-adoption-enablement-w-m-d-at-pwc-deutschland-4454990009
- Fit rationale: PwC AI Adoption & Enablement covers Change & Adoption for AI, People Upskilling, and AI Governance. The Multi-Agent RAG project's EvalAgent produces KPI-driven, per-language A/B evidence for a rollout, which is exactly the "data-driven tracking of AI adoption rate" language on pwc.de. CreditIQ carries the regulated-AI Governance signal end to end: EU AI Act Article 14 human-in-the-loop, AGG 80 percent fairness ratio 0,79 → 0,88, SHAP subgroup analysis, four-way threshold matrix, false-negative rate 44 → 16,7 percent, accuracy 75 percent, Streamlit decision support with plain-language LLM explanation.
- Projects selected: Multi-Agent RAG (P_RAG_DE), CreditIQ (P_CREDITIQ_DE). Auto-trim ladder dropped to 1 project.
- Certs selected: NVIDIA, AWS, Google Data Analytics.
- Deliverables at drafts/PwC Deutschland Werkstudent AI Adoption Enablement/: all 8 files present, CV PDF 2 pages, CL PDF 1 page (tight CSS applied).

### 4. Bosch Rexroth AG — Werkstudent Data & AI gestuetzte Informationsverarbeitung (JobID REF294246D), Lohr am Main

- Freshness: posted 2026/08/17 on jobs.bosch.de (~3 days ago).
- Language track: DE (posting body in German on the German career page).
- Apply method: company-portal (jobs.bosch.de).
- Apply link: https://jobs.bosch.de/en/job/Werkstudent-Data-AI-gestuetzte-Informationsverarbeitung-w_m_div.-Lohr-am-Main?id=e5b8b80f-646a-464b-8a9e-aa73fdb7d8fd
- Fit rationale: Bosch Rexroth Zentralbereiche runs Data & AI initiatives at the "Schnittstelle zwischen Daten, Kuenstlicher Intelligenz und wirkungsvoller Kommunikation." That maps directly onto the Multi-Agent RAG project (EN/DE end to end, LLM-as-Judge, EvalAgent with per-language KPIs) and the Movie Analytics medallion architecture on BigQuery/Cloud Run. Bosch Rexroth is a separate Bosch legal entity from prior applications; different team and different work type under the "different roles at the same company" rule.
- Projects selected: Multi-Agent RAG (P_RAG_DE), Movie Analytics medallion (P_MOVIE_DE). Auto-trim ladder dropped to 1 project.
- Certs selected: NVIDIA, AWS, Google Data Analytics.
- Deliverables at drafts/Bosch Rexroth Lohr Werkstudent Data AI Informationsverarbeitung/: all 8 files present, CV PDF 2 pages, CL PDF 1 page (tight CSS applied).

### 5. Ardex GmbH — Werkstudent AI and Innovation, Witten

- Freshness: posted ~2 days ago on Xing.
- Language track: DE (Xing listing body in German).
- Apply method: platform-native via Xing; if the Xing "Bewerben" flow redirects to an Ardex-owned portal, OpenClaw will re-flag it as company-portal.
- Apply link: https://www.xing.com/jobs/witten-werkstudent-ai-innovation-156857879
- Fit rationale: role is explicitly framed as beyond classical Werkstudent work, on "strategisch relevanten AI und Innovationsprojekten mit globaler Reichweite" with international stakeholders and Top-Management contact. That is the exact shape of the Multi-Agent RAG project (KPI-driven evaluation of an AI initiative) plus CreditIQ (regulated AI governance with a real business outcome). Ardex is not previously in the log; clean new-company pick.
- Projects selected: Multi-Agent RAG (P_RAG_DE), CreditIQ (P_CREDITIQ_DE). Auto-trim ladder dropped to 1 project.
- Certs selected: NVIDIA, AWS, Google Data Analytics.
- Deliverables at drafts/Ardex Witten Werkstudent AI Innovation/: all 8 files present, CV PDF 2 pages, CL PDF 1 page (tight CSS applied).

## Watchlist (scored but not drafted under the cap)

- BMW Motorrad — Praktikum Digitalisierung & Data Analytics Gesamtfahrzeug, Muenchen (BMW career page). Pflichtpraktikum-shaped; strong overlap with Flight Tracking + Movie Analytics. Held for a future run to keep BMW cadence sane (BMW already featured heavily in Aug 15 and Aug 13 runs).
- LEG Technologie und Digitalisierung — AI Engineer Agents & Integration, Duesseldorf (Xing, ~7 days ago). Interesting agentic role but titled as full role rather than Werkstudent; needs a re-read against the "Full-time and Junior full roles stay out of scope" filter before shipping.
- Generali Deutschland AG — Werkstudent Machine Learning Engineering, Saarbruecken (LinkedIn). Similar geographic tier and language track to PwC pick this run; deferred to keep company diversity.
- Korian Deutschland — Werkstudent KI & Data Analytics, Muenchen (Xing, ~6 days). Solid fit; held to keep this run at 5 and preserve diversity for the next run.

## Dropped

- Duales Studium / Duale Studien across BSH, Deutsche Post, Deutsche Telekom, IU, Schwarz Digits, Theo Foerch, Telefonica: excluded per master-projects.md filter (dual-study programmes are out of scope).
- Freiwilliges Praktikum listings (unpaid non-mandatory internships): excluded per master-projects.md filter.
- Junior full-time roles at IBM, statworx, KHS, adesso, HIBA and similar: excluded per master-projects.md work-type filter (Full-time and Junior full roles out of scope).

## Transparency block

- Sources reachable this run: LinkedIn (jobs listings), Xing (jobs listings), StepStone, company career pages (pwc.de, jobs.amprion.net), Tavily search API. Indeed MCP was not queried this run because the platform mix already had a fresher and more targeted signal on the other four platforms, and the 28 July 2026 yield-based reset caps Indeed at 1 per run.
- Sources unreachable: none this run.
- Freshness dating: cross-checked from the Xing "Vor N Tagen veroeffentlicht" strings and Amprion / PwC portfolio pages. Amprion was ~2 days ago; Ed. Zueblin and PwC ~1 week.
- Prompt-injection content observed and not acted on: none this run.
- Platform mix delivered: LinkedIn 1 (PwC), StepStone 1 (Ed. Zueblin), Company Page 2 (Amprion jobs.amprion.net, Bosch Rexroth jobs.bosch.de), Xing 1 (Ardex), Indeed 0.
- Distance / commute was NOT used as a scoring factor per master-projects.md.
- Language level: all three postings are DE track. Rah's B1 laufend is below the C1 bars that some PwC / Ed. Zueblin roles typically state; both cover letters name this explicitly. This does not filter listings per the standing rule; Rah decides at the apply step whether to press forward.

## Deliverable summary

- New drafts written: 5.
- Files rendered per draft: 8 (CV .md/.html/.pdf/.docx, CoverLetter .md/.html/.pdf/.docx). 40 files total across the five folders.
- CSV writes: 5 new drafted rows appended, plus 11 pre-existing `drafted` rows reconciled to their Notion Status.
- Notion writes: 5 new `drafted` rows created.

## Failures and halts this run

- None. All five roles cleared the STEP 4 validation gate (page count 2, banned strings absent, header per the 19 Aug 2026 Ojas-style layout). Auto-trim messages printed during render for all five roles are normal per the ladder and are not failures.
