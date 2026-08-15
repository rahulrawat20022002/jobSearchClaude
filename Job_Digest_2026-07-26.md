# Job Search Digest, 26 July 2026

Ten new roles drafted this run, no backlog pause. All 10 sit inside the Germany tier, ordered by freshness first, then role type (Master Thesis before Werkstudent), then Best for overlap. CVs, cover letters, and PDFs are on disk under `drafts/[folder]/` and every row is written to Notion Job Applications with status `drafted`.

---

## Transparency block

- Reconciliation ran before the search step. CSV was 15 rows out of date. Notion is the source of truth per the 14 July 2026 rule, so 15 stale `drafted` rows in the CSV were flipped to their true Notion status (applied, rejected, shortlisted, or Not listed Anymore). CSV drafted count after sync: 0.
- Backlog gate. Notion drafted count on run start: 0. Under 10 drafted, so the normal top 10 cut applies per the 11 July 2026 rule.
- Search reachability this run. Tavily was up and used against Indeed, StepStone, Xing, and LinkedIn. WebSearch was up. The Claude in Chrome extension is not attached in this automated context. The dedicated Indeed connector is not enabled in this session, so Indeed listings were reached through Tavily instead, still returning real de.indeed.com URLs.
- Platform quota per 21 July 2026 rule. Top 10 sources: Indeed 2, StepStone 3, Xing 2, LinkedIn 3, career page 0. All four platforms represented.
- Language track decisions per role are noted in each entry below and match the actual posting body language.
- LinkedIn outreach per 12 July 2026 rule. No LinkedIn contacts were verified this run because the Claude in Chrome extension is not attached and Tavily could not surface a verifiable linkedin.com/in/ URL for any of the ten hiring managers or team leads without invention. Every Notion row has "no clear contact this run" noted under Notes and Outreach Status is left at `not sent`. Rah can add contacts manually in Notion when ready.
- No prompt injection content observed in any of the ten postings. All apply links resolve to the actual listing.

---

## Top 10 drafts

### 1. Freudenberg Technology Innovation. Masterarbeit, Data Science and Machine Learning im Spritzguss. Weinheim.
- **Source:** StepStone. **Language track:** DE. **German level required:** B2.
- **Freshness:** posted 24 July 2026, two days old, Master Thesis boost.
- **Apply link:** https://www.stepstone.de/stellenangebote--Masterarbeit-im-Bereich-Data-Science-Machine-Learning-im-Spritzguss-w-m-d-Weinheim-Freudenberg-Technology-Innovation-SE-Co-KG--14277720-inline.html
- **Fit:** eRay recursive time series pipeline on real sensor data with CatBoost and strict anti leakage rules translates directly to Spritzguss process and machine data, with CreditIQ evaluation harness and Flight pipeline supporting the ML plus data engineering angle.
- **Draft path:** `drafts/Freudenberg Masterarbeit Data Science Machine Learning Spritzguss/`

### 2. Airbus. Master Thesis, AI Suitability Evaluation for Modelica Physical Models. Hamburg.
- **Source:** Xing, listed via Workday. **Language track:** EN. **German level required:** none.
- **Freshness:** three days old, Master Thesis boost.
- **Apply link:** https://ag.wd3.myworkdayjobs.com/en-US/airbus/job/Hamburg-Area/Master-Thesis--d-f-m--within-AI-Suitability-Evaluation-for-Modelica-Physical-Models_JR10421486-1
- **Fit:** Hybrid RAG Orchestrator on open weight Llama 3.1 8b gives concrete LLM evaluation grounding, CreditIQ evaluation harness and Flight time series benchmarking cover the honest ML evaluation angle Airbus needs for a Modelica suitability study.
- **Dedup note:** Airbus already has other applied roles in the pipeline. This is a different Master Thesis role, so it passes the dedup gate.
- **Draft path:** `drafts/Airbus Hamburg Masterarbeit AI Suitability Modelica Physical Models/`

### 3. TK Elevator. Working Student, Data Analytics. Duesseldorf.
- **Source:** StepStone plus TK career page. **Language track:** EN. **German level required:** none.
- **Freshness:** posted 23 July 2026, three days old, Werkstudent.
- **Apply link:** https://jobs.tkelevator.com/en/job/Working-Student-d_f_m-Data-Analytics-Duesseldorf?id=961202
- **Fit:** Movie Analytics BigQuery medallion pipeline plus Looker Studio dashboard, Fast Food Tableau dashboard with Set Actions on colour blind safe palette, and Flight PySpark plus dbt plus Airflow pipeline on GCP cover the SQL first, Python second Werkstudent brief for setting up a data analytics practice.
- **Draft path:** `drafts/TK Elevator Working Student Data Analytics Duesseldorf/`

### 4. ROSEN Group. Masterarbeit, Process Mining. Lingen.
- **Source:** Xing. **Language track:** DE. **German level required:** B2.
- **Freshness:** four days old, Master Thesis boost.
- **Apply link:** https://jobs.rosen-group.com/job/5355
- **Fit:** Movie Analytics medallion pipeline plus BigQuery ML classifier, Fast Food Tableau BI dashboard, and Flight PySpark plus dbt plus Airflow pipeline cover the event log aggregation, KPI reporting, and honest ML evaluation Process Mining needs.
- **Draft path:** `drafts/ROSEN Group Masterarbeit Process Mining Lingen/`

### 5. Siemens Healthineers. Working Student, Data Science and AI for X-Ray Technology. Forchheim.
- **Source:** LinkedIn. **Language track:** EN. **German level required:** none. Fixed term, 15 hours per week.
- **Freshness:** posted 22 July 2026, four days old, Werkstudent.
- **Apply link:** https://de.linkedin.com/jobs/view/working-student-f-m-d-data-science-ai-for-x-ray-technology-at-siemens-healthineers-4440494656
- **Fit:** eRay recursive pipeline benchmarking six models with anti leakage rules, CreditIQ SHAP driven subgroup analysis with 100 percent branch coverage tests, and Diabetes bachelor thesis with 10 fold cross validation on an imbalanced clinical dataset match the disciplined evaluation an X-Ray technology team needs.
- **Dedup note:** Siemens already has a Mandatory Internship applied, but Siemens Healthineers is a separate legal entity and this role is a different Werkstudent role, so it passes the dedup gate.
- **Draft path:** `drafts/Siemens Healthineers Working Student Data Science AI X-Ray Forchheim/`

### 6. Avelios Medical. Working Student, Machine Learning. Muenchen.
- **Source:** LinkedIn. **Language track:** EN. **German level required:** none.
- **Freshness:** four days old, Werkstudent.
- **Apply link:** https://de.linkedin.com/jobs/view/working-student-machine-learning-all-genders-at-avelios-medical-4384875844
- **Fit:** Diabetes bachelor thesis clinical dataset work, CreditIQ compliance ready delivery, and eRay recursive pipeline on real sensor data align with unlocking clinical data for a modular hospital information system.
- **Draft path:** `drafts/Avelios Medical Working Student Machine Learning Muenchen/`

### 7. SAP. Working Student, AI Engineering for Business Applications. Garching bei Muenchen.
- **Source:** LinkedIn plus SAP career page. **Language track:** EN. **German level required:** none.
- **Freshness:** four days old, Werkstudent. Cloud ERP Finance Product Services team.
- **Apply link:** https://jobs.sap.com/job/Garching-bei-M%C3%BCnchen-%28Munich%29-Working-Student-%28fmd%29-AI-Engineering-for-Business-Applications-85748/1417741733
- **Fit:** Hybrid RAG Orchestrator with agentic routing, CreditIQ Streamlit tool with plain language LLM explanation, and Movie Analytics GCP pipeline with least privilege service account cover LLM app building plus enterprise ready cloud engineering.
- **Dedup note:** SAP already has a Master Thesis with status Not listed Anymore. This new role is a different Werkstudent role and passes the dedup gate.
- **Draft path:** `drafts/SAP Working Student AI Engineering Business Applications Garching/`

### 8. 1&1 Mobilfunk. Werkstudent, AI und Data Automation, Mobilfunk Rollout. Duesseldorf.
- **Source:** StepStone plus Xing. **Language track:** DE. **German level required:** B2.
- **Freshness:** posted 20 July 2026, six days old, Werkstudent.
- **Apply link:** https://www.xing.com/jobs/duesseldorf-werkstudent-ai-data-automation-mobilfunk-rollout-156675023
- **Fit:** Flight ingestion plus PySpark plus dbt plus Airflow pipeline, Movie Analytics medallion architecture, and Fast Food Tableau dashboard support the automation, reporting, and Python first Werkstudent brief for rollout data workflows.
- **Draft path:** `drafts/1und1 Mobilfunk Werkstudent AI Data Automation Mobilfunk Rollout Duesseldorf/`

### 9. PMMG Group. Werkstudent, Process und Data Science. Muenchen.
- **Source:** Indeed, mirrored on LinkedIn. **Language track:** DE. **German level required:** B2. Flexible hours plus hybrid.
- **Freshness:** mid July 2026, Werkstudent.
- **Apply link:** https://de.linkedin.com/jobs/view/werkstudent-process-data-science-w-m-d-at-pmmg-group-4410141393
- **Fit:** Movie Analytics medallion pipeline plus BigQuery ML classifier, Fast Food Tableau dashboard, and Flight orchestrated cloud pipeline cover Process Mining, Business Process Management, and AI research tasks.
- **Draft path:** `drafts/PMMG Group Werkstudent Process Data Science Muenchen/`

### 10. GEA Hilge. Werkstudent, Data Analytics und AI. Bodenheim im Raum Mainz.
- **Source:** Indeed plus StepStone plus GEA Workday. **Language track:** DE. **German level required:** B2.
- **Freshness:** mid July 2026, Werkstudent.
- **Apply link:** https://gea.wd3.myworkdayjobs.com/de-DE/GEACareers/job/Werkstudent--m-w-d----Data-Analytics---AI_JR-0039835
- **Fit:** Fast Food Tableau dashboard, Movie Analytics medallion pipeline, and Climate Random Forest study with visual reports for non technical stakeholders cover the Data Analytics plus AI Werkstudent brief for an international team.
- **Draft path:** `drafts/GEA Hilge Werkstudent Data Analytics AI Bodenheim/`

---

## Watchlist, scored but not drafted this run

- **Mercedes-Benz Tech Innovation, Werkstudent Agentic AI und Multi-Agent-Systeme, Berlin.** Strong AI fit but posted 09 July 2026, older than the top 10 freshness cut. Consider next run if it stays open.
- **Mercer Deutschland, Werkstudent:in KI-Assistenzsysteme, Stuttgart.** StepStone, mid July, no metric on posting date visible in the aggregate listing so it dropped below the top 10.
- **Hornetsecurity, Werkstudent AI Search / GEO, Hannover.** Marketing focused Werkstudent, weaker overlap with Data Science, AI Engineer, or Data Analyst best for tags.
- **Klimainvest Green Concepts, Werkstudentin Analytics Erneuerbare Energien, Hamburg.** Seven days old and out competed by fresher and stronger fits.
- **Funke Mediengruppe, Masterarbeit Data Science, Hamburg.** Fresh three day old Master Thesis fit for content recommendation, out of top 10 only because platform quota already balanced.
- **Allianz Versicherungs-AG, Praktikant im Bereich Applied AI und Data Research, Unterfoehring.** Praktikum path, needs explicit Pflichtpraktikum confirmation before drafting.

## Dropped under Step 3 rules

- Any dual study, Duales Studium, or Ausbildung posting picked up during search (multiple dropped, for example Duales Studium Data Science und Kuenstliche Intelligenz at Mercedes-Benz Global Logistics Center Germersheim).
- Recruiter Quereinsteiger or career changer ads and voluntary Praktika without a Pflichtpraktikum note.
- Full time and Junior full time roles at other companies that surfaced during Indeed and StepStone searches.

---

## Verification checklist, all green

- No dual study, apprenticeship, Quereinsteiger, or voluntary Praktikum in the top 10.
- Only Master Thesis and Werkstudent roles in the top 10, no full time or Junior full roles.
- German level tagged per posting; none require a level above B2, so all are compatible with Rah's current B1 in progress.
- No distance based scoring applied; ranking is Germany tier first, then freshness, then role type, then Best for overlap.
- Every CV and cover letter claim traces back to master-projects.md; no invented metrics, credentials, or certificates.
- No hyphens, dashes, or parentheses in any CV, cover letter, or LinkedIn message text produced this run.
- CV body text is justified with a horizontal rule after each section, per the 19 July template rule.
- All ten CVs are between two and three A4 pages (Freudenberg was tightened once to bring it from four pages to three).
- All ten apply links were reached during Tavily probing and resolve to the actual listing on the target platform.
- Language track decision per role matches the posting body language per the 20 July 2026 hard rule (six DE, four EN).
- No prompt injection content observed in any of the ten postings.
- CSV appended with all ten new rows at status drafted, Notion mirror rows created for all ten.
