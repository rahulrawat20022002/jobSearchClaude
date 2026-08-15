# Job Search Digest, 18 July 2026

## Status: RUN COMPLETED, top 10 tier

Notion is the source of truth for status per the 14 July rule. The Job Applications data source `fd974369-40b2-48c5-b660-d15256c88f52` currently holds 0 rows with status drafted at the start of this run, so the backlog gate cleared and the run proceeded at the normal top 10 tier.

Note: an earlier digest for 18 July was written earlier today under a stale CSV that showed 15 drafted rows and paused the run. That state has since been corrected. All 15 previously drafted rows are now applied, rejected, or Not listed Anymore in Notion, so this run properly executed the search, filter, and draft steps.

## Transparency block

- Notion queried successfully on first attempt, no retry needed.
- Drafted row count from Notion, 0 at run start.
- Drafted row count from applied-log.csv before reconciliation, 15. All 15 CSV rows were stale drafted, since Notion had already been updated for those rows. CSV was synced back to Notion status for Volkswagen (Not listed Anymore) and the other 14 rows (applied).
- Backlog gate tier, under 10 drafted rows, normal top 10 cut.
- Sources reachable this run: Indeed connector (reachable), Tavily search (reachable, used for StepStone, LinkedIn, SAP careers scan), SAP careers page (reachable via Tavily). Claude in Chrome extension not attached in this automated run.
- New rows appended to applied-log.csv, 10. New Notion rows created, 10. All CV and cover letter deliverables built under drafts/[Company]/.
- All 10 CVs verified at exactly 2 A4 pages via pypdf page count on the produced PDFs.
- No prompt injection content observed this run.
- LinkedIn outreach: not surfaced this run. No verifiable linkedin.com/in/ URLs were sourced within the run budget. Each Notion row's Notes field records "no clear contact this run" per the 12 July rule fallback. Rah can request a targeted outreach pass on any of the 10 rows and the next run will attempt it.
- Every role in this run is on the English track. No posting in the top 10 met both the German language body and B1 or higher German requirement threshold simultaneously, so the German deliverables track from the 14 July rule was not triggered.

## Backlog reconciliation, CSV sync summary

The 15 previously drafted rows were flipped in Notion by Rah as follows and the CSV was synced to match:

1. Volkswagen, Master Thesis Deep Learning for Autonomous Driving, Not listed Anymore.
2. Bausch and Lomb, Werkstudent Business Intelligence, applied.
3. WERTGARANTIE Group, Werkstudent Data Science, applied.
4. Sopra Steria, Werkstudent Data Engineer and Analyst, applied.
5. Picnic, Working Student Business Analyst Logistic Analytics, applied.
6. Infineon Technologies, Master Thesis AI Based Condition Monitoring for Drive Systems, applied.
7. Airbus Defence and Space, Working Student AI Models for Spacecraft FDIR, applied.
8. Wieland Group, Werkstudent Data Platform and AI Engineering, applied.
9. mitteldeutsche IT GmbH, Werkstudent KI Entwicklung, applied.
10. MTU Aero Engines, Werkstudent Business Analyst for Workflow Automation, applied.
11. Porsche, Werkstudent Data Science and Process Mining, applied.
12. DICO Drinks GmbH, Werkstudent IT Datenvisualisierung and Produktionsdaten, applied.
13. Animore, Working Student and Intern Post Training for Robot Learning, applied.
14. Fraunhofer SIT, Werkstudierende NLP Research, applied.
15. REHAU New Ventures, Working Student AI and Innovation, applied.

## Top 10 new drafts, ordered by freshness first, then role type, then Best for overlap

### 1. CeramTec GmbH, Werkstudent Digital Transformation Data Analytics Application
- Location: Plochingen. Posted 17 July 2026, freshest of the run.
- Source: Indeed. Apply link: https://to.indeed.com/aaw28977y7sm
- German level: none stated on posting. Track: English.
- Fit: Data Analyst focus. CV leads with Movie Analytics BigQuery medallion pipeline, Fast Food Tableau dashboard, and Climate Economics Random Forest study. Certificates SAS Viya, Google Data Analytics, AWS.
- Draft: drafts/CeramTec Werkstudent Data Analytics Application/

### 2. CeramTec GmbH, Werkstudent Digital Transformation Computer Vision
- Location: Plochingen. Posted 17 July 2026.
- Source: Indeed. Apply link: https://to.indeed.com/aad8hyqlg829
- German level: none stated on posting. Track: English.
- Fit: AI/ML Engineer focus. CV leads with Hybrid RAG Orchestrator, CreditIQ evaluation discipline, and Real Time Flight Tracking pipeline. Certificates NVIDIA LLM, AWS, Google Data Analytics.
- Draft: drafts/CeramTec Werkstudent Computer Vision/

### 3. Draeger, Praktikum or Abschlussarbeit Software Programmierung Computer Vision and Machine Learning
- Location: Luebeck. Posted 16 July 2026. Master Thesis boost within same day, only Thesis eligible candidate this day.
- Source: Indeed. Apply link: https://to.indeed.com/aaffv724wv9m
- German level: none stated on posting. Track: English.
- Fit: Master Thesis in medical CV and ML. CV leads with Hybrid RAG Orchestrator, CreditIQ regulatory grade evaluation, Real Time Flight Tracking pipeline. Diabetes Thesis Research and Thesis section supports the safety critical evaluation angle.
- Draft: drafts/Draeger Abschlussarbeit Computer Vision ML/

### 4. ATRIVIO GmbH, Bachelor or Masterarbeit
- Location: Kempten (Allgaeu). Posted 14 July 2026, Thesis boost within same day.
- Source: Indeed. Apply link: https://to.indeed.com/aanr9w4ky4vp
- German level: none stated on posting. Track: English.
- Fit: Open Master Thesis collaboration, framed as data science or ML topic. CV leads with Hybrid RAG Orchestrator, Movie Analytics BigQuery pipeline, and CreditIQ evaluation.
- Draft: drafts/ATRIVIO Masterarbeit/

### 5. RSG Group GmbH, Werkstudent Data and Analytics 20h per week
- Location: Berlin head office. Posted 14 July 2026.
- Source: Indeed. Apply link: https://to.indeed.com/aazywqrjv2mh
- German level: none stated on posting. Track: English.
- Fit: Data Analyst focus. CV leads with Movie Analytics BigQuery pipeline, Fast Food Tableau dashboard, and Climate Economics BI study. Certificates SAS Viya, Google Data Analytics, AWS.
- Draft: drafts/RSG Group Werkstudent Data Analytics/

### 6. SAP, Master Thesis Student Supply Chain Management Data Science on Agentic AI
- Location: Garching bei Muenchen. Sourced from SAP career page via Tavily. Undated on listing, treated as posted seven days ago per freshness rule.
- Source: Company Page. Apply link: https://jobs.sap.com/go/Germany/8806101/
- German level: none stated on posting. Track: English.
- Fit: Master Thesis on Agentic AI for SCM. Perfect overlap with Hybrid RAG Orchestrator agentic routing, Movie Analytics medallion pipeline, and CreditIQ evaluation rigour. Certificates NVIDIA LLM, AWS, SAS.
- Draft: drafts/SAP Master Thesis SCM Data Science Agentic AI/

### 7. MVV Energie, Werkstudent Digital Empowerment GenAI and Analytics
- Location: Mannheim, local to Rah.
- Posted 8 July 2026.
- Source: Indeed. Apply link: https://to.indeed.com/aadld762dnhr
- German level: none stated on posting. Track: English.
- Fit: GenAI plus analytics enablement, ideal for Hybrid RAG Orchestrator, Movie Analytics BigQuery pipeline, and CreditIQ. Certificates NVIDIA LLM, Google Data Analytics, AWS.
- Draft: drafts/MVV Energie Werkstudent GenAI Analytics/

### 8. Debeka, Werkstudent Data Intelligence Center DWH and BI
- Location: Koblenz. Posted 6 July 2026.
- Source: Indeed. Apply link: https://to.indeed.com/aagm99l4sbtn
- German level: none stated on posting. Track: English.
- Fit: DWH and BI focus. CV leads with Movie Analytics BigQuery medallion pipeline, Real Time Flight Tracking dbt orchestration, and Fast Food Tableau dashboard. Certificates SAS Viya, Google Data Analytics, AWS.
- Draft: drafts/Debeka Werkstudent Data Intelligence Center DWH BI/

### 9. 1KOMMA5, Werkstudent Quality Control Analyst Waermepumpe
- Location: Home Office, fully remote. Posted 6 July 2026.
- Source: Indeed. Apply link: https://to.indeed.com/aalqbynxfrpw
- German level: none stated on posting. Track: English.
- Fit: Quality analytics on heat pump fleet data. CV leads with Movie Analytics BigQuery pipeline, Climate Economics Random Forest BI, and Real Time Flight Tracking enrichment.
- Draft: drafts/1KOMMA5 Werkstudent Quality Control Analyst Waermepumpe/

### 10. JOST-Werke Deutschland GmbH, Werkstudent Industrial AI and Process Innovation
- Location: Neu-Isenburg. Posted 25 June 2026.
- Source: Indeed. Apply link: https://to.indeed.com/aa2vz4gmlqz7
- German level: none stated on posting. Track: English.
- Fit: Industrial AI use cases. CV leads with Hybrid RAG Orchestrator, Movie Analytics BigQuery pipeline, and CreditIQ evaluation.
- Draft: drafts/JOST-Werke Werkstudent Industrial AI/

## Watchlist, scored but not drafted this run

These roles were on the shortlist but sat just below the top 10 cut. They stay in the pipeline for a future run if they remain live.

- Witt-Gruppe, Praktikum KI und Machine Learning 50 percent Remote, Weiden. Posted 15 July. Held because posting does not explicitly state Pflichtpraktikum; voluntary internships are out of scope from the 2 July rule.
- Alcon, Praxissemester or Pflichtpraktikum Image Processing and Machine Learning, Grosswallstadt. Posted 13 June, worth a look on the next run.
- Rohde and Schwarz, Masters Thesis AI Agents in Operations Management, Muenchen. Posted 2 June, thesis eligible.
- FIO SYSTEMS AG, Werkstudent Data and Reporting Analyst, Leipzig. Posted 23 June.
- Hypoport B.V., Werkstudent Data and Reporting Analyst, Leipzig. Posted 23 June.
- Fraunhofer IIS, Working Student, Internship, or Master Thesis on innovative EDA software, Dresden. Posted 2 June.
- HMS Analytical Software, Werkstudent Software Development Data and AI, Berlin. Posted 30 April.
- DLR Braunschweig, Praktikum or Abschlussarbeit KI gestuetzte Geodatenanalyse fuer sichere Radinfrastruktur. Posted 7 April.
- Bosch, Master Thesis AI Driven Tolerance Sensitivity Analysis of Worm Gears, Renningen. Posted 11 May.
- Estateanfrage, Werkstudent AI Engineer, Muenchen. Posted 19 June.

## Dropped from results

- Encavis, Berufsbegleitendes Studium Data Science and Artificial Intelligence Master at Encavis, Hamburg. Dropped as dual study or Duales Studium, out of scope per 2 July rule.
- Voluntary internships and Praxissemester ads where the posting did not state Pflichtpraktikum. Voluntary internships are out of scope for this run.
- BMW Group, Werkstudent Data Analyst Programmplanung Antrieb, Muenchen. Already rejected in prior applied-log row.
- 4flow, AI Engineer im Bereich Consulting, Berlin. Full time, out of scope.
- voize, Technical Support Working Student, Berlin. Full time and not target role.
- Stadt Nuernberg, Werkstudent IT. Too broad and not a data or AI role.
- FIR e V an der RWTH Aachen, Master Thesis Adaptation of MLOps and Use of AI in Maintenance. Posted 16 January 2025, too old to treat as fresh under the freshness rule.
- Various OST BAU and TTI Europe controlling roles, out of target role scope.

## Sources reachable this run

- Indeed connector: reachable, exercised across Werkstudent Data Science, Werkstudent Data Engineer, Werkstudent Data Analyst, Werkstudent AI Engineer, Werkstudent Business Intelligence, Masterarbeit Machine Learning, Master Thesis AI, Abschlussarbeit Machine Learning, and Pflichtpraktikum Data Science.
- Tavily general search: reachable, exercised against StepStone, LinkedIn, Xing, Glassdoor, and the SAP career page priority target.
- SAP career page: reachable via Tavily, produced the Master Thesis Supply Chain Management Data Science on Agentic AI listing that made the top 10.
- Claude in Chrome extension: not attached in this automated run.
- StepStone and Xing: reachable via Tavily but no unique fresh matches beyond Indeed and SAP this run.
