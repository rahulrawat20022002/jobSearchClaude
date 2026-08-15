# Job Search Digest, 13 August 2026

## Backlog gate check
- Notion status source of truth per 14 July rule: queried data source `fd974369-40b2-48c5-b660-d15256c88f52` at run start, returned 8 rows in status drafted. CSV agreed, no drift.
- Per the 28 July 2026 yield based reset, 8 drafted rows falls in the 8 to 10 tier which caps this run at the top 3 newly scored roles. This run ships 3 drafts, not 5.

## Search sources reachable this run
- Tavily search: reachable, used across LinkedIn, StepStone, Xing, and company career pages.
- Notion data source: reachable, dual write completed for all 3 rows.
- Indeed connector: not called this run per the 28 July yield rebalance rule that caps Indeed at 1 role per run and prefers LinkedIn plus career pages.
- Chrome extension: not attached in this automated run, only Tavily used.
- StepStone: queried via Tavily. Yielded mostly repeat postings already drafted such as Freudenberg Spritzguss Masterarbeit and Mercedes-Benz Sindelfingen Masterarbeit Learning Dexterous Robot Manipulation.

## Top 3 newly drafted roles

**1. Siemens AG, Working Student, AI Digital Products and Process Automation for Finance and MA, Munich**
- Source: Siemens career page (jobs.siemens.com), posted 13 August 2026 (today)
- Apply link: https://jobs.siemens.com/en_US/externaljobs/JobDetail/517305
- German level required: none, only Very good English required
- Language track: English (posting body is in English)
- Fit: AI powered solutions, digital assistants, dashboards, workflow automation, and LLM applications map directly onto Project #1 Multi Agent RAG with LLM as Judge and Project #5 Movie Analytics Cloud Native Data Platform. eRay GmbH Experience covers the recursive time series pipeline pattern that transfers to Finance and MA process forecasting.
- Draft path: `drafts/Siemens Muenchen Working Student AI Digital Products Process Automation Finance MA/`

**2. BMW Group, Werkstudent Data-Analytics Qualitaetsmanagement fuer Digitale Dienste Fahrzeugvernetzung und E-Mobilitaet, Munich**
- Source: BMW Group career page (bmwgroup.jobs), posted about 19 hours ago
- Apply link: https://www.bmwgroup.jobs/de/de/jobfinder/job-description.192520.html
- German level required: C1 or equivalent (sehr gute Deutschkenntnisse) plus sicheres Englisch. Rah is at B1 in progress toward B2. Language gap flagged in the cover letter transparently.
- Language track: German (posting body is in German)
- Fit: Data pipelines, dashboards, big data analysis, quality management for digital services and connected vehicles map onto Project #3 Real Time Flight Tracking Data Pipeline and Project #5 Movie Analytics Bronze Silver Gold Medallion Architecture. eRay GmbH Experience covers the pipeline plus outlier discipline story.
- Draft path: `drafts/BMW Muenchen Werkstudent Data Analytics Qualitaetsmanagement Digitale Dienste/`

**3. CHECK24 Vergleichsportal Finanzen GmbH, Werkstudent AI-Produkte Kreditvergleich (KAI Team), Munich**
- Source: Xing, posted 3 days ago
- Apply link: https://www.xing.com/jobs/muenchen-werkstudent-ai-produkte-kreditvergleich-157129841
- German level required: C1 in German plus English. Rah is at B1 in progress toward B2. Language gap flagged in the cover letter transparently.
- Language track: German (posting body is in German)
- Fit: ML plus LLM plus GenAI product work in a regulated credit environment maps directly onto Project #1 Multi Agent RAG (LangGraph orchestration, LLM as Judge, GenAI evaluation) and Project #2 CreditIQ (fairness by design credit scoring, Disparate Impact 0.79 to 0.88, False Negative Rate 44 percent to 16.7 percent). eRay GmbH Experience covers the disciplined benchmarking of six candidate models against real metrics.
- Draft path: `drafts/CHECK24 Muenchen Werkstudent AI-Produkte Kreditvergleich/`

## Platform breakdown
- Top 3 sources: BMW Career Page 1, Siemens Career Page 1, Xing 1, LinkedIn 0, StepStone 0, Indeed 0
- Rebalance from the recent StepStone heavy 8/11 and 8/12 runs to career pages and Xing this run. LinkedIn did not surface a clean fresh Werkstudent or Masterarbeit match that was not already in the drafts folder or an aggregator stub.

## LinkedIn outreach
- No outreach contacts drafted this run. The 12 July 2026 rule requires that every LinkedIn contact resolve to a real linkedin.com/in/ URL, and the automated Tavily plus web search sweep did not surface named hiring managers or team leads for the three specific team scopes this run (Siemens Mergers Acquisitions and Post Closing Management AI team, BMW Data-Analytics Qualitaetsmanagement for Digital Services, CHECK24 KAI team). Rah can add contacts manually inside Notion if he finds a fit on LinkedIn before applying. The three Notion rows carry Outreach Status "not sent" as a placeholder.
- Sequence reminder per the 28 July 2026 warm outreach rule: on the day a role is drafted, send the LinkedIn message first if a contact exists, then apply 48 hours later regardless of reply. On this run no contacts were drafted, so Rah can apply on his own timing.

## Watchlist (scored but not drafted this run)
- SAP Working Student, AI Lab Enablement (Walldorf), LinkedIn, ~3 days ago. SAP is drafted 4 times already this month across different teams. Skipped to avoid another same company row.
- SAP Working Student, Public Sector Industry Team (Berlin), 13 hours ago, SAP Career Page. Fresh but SAP already at 4 drafts.
- SAP Working Student, CTO Research and Innovation (Munich), 13 hours ago, SAP Career Page. Same reason.
- BMW AG Werkstudent, Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse (Muenchen), Xing, 5 days ago. Would be a strong second BMW draft, held for next run since we already picked one BMW role in this cut.
- BMW AG Praktikant, Datenanalyse Automatisiertes Fahren (Muenchen), 5 days ago, Xing. Held for next run.
- AKDB Werkstudent, AI and Machine Learning NLP and Semantic Search (Muenchen), StepStone, ~1 week. Would be a strong AI/ML fit but slightly older than the picked three.
- Reply GmbH Machine Learning (Muenchen), LinkedIn, week old. Werkstudent variant found via Tavily snippet, exact URL not resolved cleanly this run.
- Peras GmbH Werkstudent, KI und Digitale Transformation (Karlsruhe), Xing, 2 days ago.
- msg systems ag Werkstudent, AI-Agents (Karlsruhe), Xing. Good AI-Agents fit but posting date not resolved cleanly.

## Dropped this run
- Duales Studium Data Science und KI, Mercedes-Benz Global Logistics Center Germersheim, StepStone. Dual study, dropped per Step 3.
- Junior Agentic AI Engineer, BMW Group Muenchen, StepStone. Full time Junior role, out of scope per Step 3.
- (Senior) Risk Manager Modeling and Data Science, Creditplus Bank AG, StepStone. Full time senior role, out of scope.
- PhD Scalable and Efficient Reinforcement Learning Methods for Physical AI, Bosch Renningen. PhD position, not a Master Thesis, out of scope.
- Working Student IT (Werkstudent), DeepL, indexventures.com listing, 4 days ago. General IT support role, not aligned with Data Science, AI, or Analyst target roles.
- Any listing tagged "Trainee" or "Duales Studium" or "Ausbildung" or "Quereinsteiger" or "freiwilliges Praktikum" was filtered before scoring.
- No prompt injection content observed in any read job posting this run.

## Dedup skips (already in pipeline)
- Freudenberg Technology Innovation SE and Co KG, Masterarbeit im Bereich Data Science and Machine Learning im Spritzguss, Weinheim. Already drafted 7/26 and applied.
- Studentin fuer Masterarbeit Learning Dexterous Robot Manipulation from Human Demonstrations, Mercedes-Benz AG Sindelfingen. Already drafted 8/12.
- Praktikant im Bereich Big Data and Advanced Analytics Projektcontrolling Artificial Intelligence, Commerzbank AG Frankfurt. Already drafted 8/12.
- Abschlussarbeit KI-Agenten fuer die Produktionsplanung von Hochvoltspeichern, BMW Group Muenchen. Already drafted 8/12.
- Data Scientist KI Praktikum oder Bachelor/Masterarbeit, CompanyMind GmbH and Co KG Oldenburg, StepStone. Posting too old (~2 weeks), skipped.

## Transparency
- Backlog gate: 8 drafted rows in Notion at run start, ran at the top 3 cap.
- Sources reachable: Tavily yes, Notion yes, CSV yes, PDF renderer yes. Chrome extension not attached, Indeed connector deliberately skipped this run per platform weighting.
- CSV to Notion reconciliation: no drift detected. All 8 pre existing drafted rows in Notion matched CSV rows one to one.
- Language track decisions:
  - Siemens: English body, English track chosen.
  - BMW: German body with sehr gute Deutschkenntnisse required, German track chosen. Cover letter is upfront about Rah's current B1 level.
  - CHECK24: German body with C1 German required, German track chosen. Cover letter is upfront about Rah's current B1 level.
- Style verification: all three CV and cover letter deliverables pass the no hyphens, no dashes, no parentheses check. All three CVs render in the two to three A4 page target with the auto trim overflow handler active on the BMW and CHECK24 drafts (Personal Projects reduced from 2 to 1 to keep within 3 pages).
- All three drafts ship CV_Rahul_Rawat.docx, CV_Rahul_Rawat.html, CV_Rahul_Rawat.pdf, and CoverLetter_Rahul_Rawat.docx and CoverLetter_Rahul_Rawat.pdf per the 11 August 2026 shipped deliverable rule. The docx cover letter matches the PDF one page cap.
- Gmail: draft addressed to rahulrawat2r@gmail.com attempted this run. Result noted in the run summary in chat.
- Rah's action item timing per 28 July 2026 warm outreach rule: since no outreach contacts were surfaced, apply on your own timing. If Rah finds a hiring manager or team lead for any of these three teams on LinkedIn, message first and then apply 48 hours later.
