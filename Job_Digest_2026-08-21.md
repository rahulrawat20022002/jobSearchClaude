# Job Digest, 21 August 2026

## Run type and render toolchain

- Scheduled Cowork Agent A run on the cloud sandbox at /tmp/JobSearch.
- Render toolchain: weasyprint 69.0 + python-docx + pypdf installed successfully. `import weasyprint, docx, pypdf` returned "render toolchain ok".
- Owner boundary: Agent A only. Zero writes to Notion Status out of drafted, zero Date Applied writes, zero LinkedIn or Xing compose windows touched.

## Backlog gate result

- Notion data source fd974369-40b2-48c5-b660-d15256c88f52 queried directly.
- Rows with Status = drafted at run start: **0**.
- Gate zone: **under 8 drafted, normal top 3 to 5 cut** per 28 July 2026 yield reset.
- Backlog after this run: **4 drafted in Notion** (the 3 newly drafted today plus 1 Amprion Werkstudent KI row reconciled into Notion in Step 3).

## Reconciliation result

CSV drift found and fixed against Notion, per 14 July 2026 status source of truth rule and Step 3 rules:

| Company | Role | CSV before | Notion truth | CSV after |
|---|---|---|---|---|
| Amprion GmbH | Masterarbeit, Initiativbewerbung KI und Wissensmanagement | drafted | applied | applied |
| Ed. Zueblin AG | Werkstudent, Business Intelligence and Data Analytics | drafted | applied | applied |
| PwC Deutschland | Werkstudent, AI Adoption and Enablement | drafted | applied | applied |
| Bosch Rexroth AG | Werkstudent, Data and AI gestuetzte Informationsverarbeitung REF294246D | drafted | applied | applied |
| Ardex GmbH | Werkstudent, AI and Innovation | drafted | Not listed Anymore | Not listed Anymore |

Additionally, one CSV row (Amprion GmbH, Werkstudent, KI Stellen-ID 7959) had no Notion counterpart. Per Step 3, created the missing Notion row with Status = drafted, Apply Method = company-portal, Apply Link = jobs.amprion.net, and a Notes entry marking it as a reconciliation catch-up from the 20 Aug run.

## Top cut, 3 roles

### 1. Sana HR Solutions GmbH, Werkstudent Data Engineer, Muenchen

- **Freshness:** posted 17 Aug 2026 (4 days ago) via Sana careers portal (SmartRecruiters), also on Indeed.
- **Language track:** DE (posting body in German).
- **Apply method:** company-portal (Sana SmartRecruiters portal).
- **Apply link:** https://to.indeed.com/aan49kxw2vy8
- **Fit rationale:** Sana HR Solutions runs a dbt + Power BI + Oracle Analytics stack over their HR data platform, with focus on ETL, connector development, requirements engineering, Linux shell, and CI/CD. That maps directly onto the Real Time Flight Tracking pipeline (Python collectors, PySpark cleaning on GCP, dbt modelling, Airflow orchestration on GCS + Dataproc, Tableau + TabPy) and the Movie Analytics medallion architecture (Bronze/Silver/Gold in BigQuery on Cloud Run with automated Cloud Scheduler triggers and a leakage-free BigQuery ML classifier). eRay GmbH data quality work (3-pass outlier system, sensor exclusion, rolling z-score) covers the "Datenqualität vor Modell" angle.
- **Projects selected:** Real Time Flight Tracking (P_FLIGHT_DE), Movie Analytics medallion (P_MOVIE_DE). Auto-trim ladder dropped to 1 project + tightened SS bullets to fit 2 pages.
- **Certs selected:** AWS Cloud Foundations, SAS Viya, Google Data Analytics (BI/analytics slant).
- **Deliverables at drafts/Sana HR Solutions Muenchen Werkstudent Data Engineer/**: CV_Rahul_Rawat.{md,html,pdf,docx} + CoverLetter_Rahul_Rawat.{md,html,pdf,docx}. All 8 files present, CV PDF 2 pages, CL PDF 1 page (tight CSS applied).

### 2. Robert Bosch GmbH, Masterarbeit Agentisches KI-System fuer eine Halbleiterdatenbank, Renningen

- **Freshness:** posted 11 Aug 2026 (10 days ago) on jobs.bosch.de, also on Indeed.
- **Language track:** DE (posting body in German).
- **Apply method:** company-portal (jobs.bosch.de, ref REF293881R).
- **Apply link:** https://jobs.bosch.de/job/Masterarbeit_-Agentisches-KI-System-fuer-eine-Halbleiterdatenbank-w_m_div.-Renningen?id=7c44c060-25f7-4616-88ba-264de32fd3d7
- **Fit rationale:** Bosch is looking for a Masterarbeit candidate to build an agentic KI system on the Bosch semiconductor DB, train it against DB schema, and evaluate how well it translates natural language intents into deterministic DB operations plus autonomous reasoning loops vs classical human-in-the-loop workflows. That maps directly onto the Multi-Agent RAG project (LangGraph orchestrator, LanguageAgent, JudgeAgent scoring 5 dimensions in JSON mode at temperature 0, judge Qwen2.5 14B distinct from generator Mistral 7B to kill self-preference bias, EvalAgent with 5 retrieval + 4 generation metrics per language into JSON/Markdown reports). Movie Analytics medallion supplies the SQL + schema-enforcement + leakage-aware evaluation angle. Rah has hands-on with LangGraph and Model Context Protocol in agent projects; presence in Renningen is achievable from Mannheim.
- **Projects selected:** Multi Agent RAG (P_RAG_DE), Movie Analytics medallion (P_MOVIE_DE). Auto-trim ladder dropped to 1 project + tightened SS bullets to fit 2 pages.
- **Certs selected:** NVIDIA LLM Applications, AWS Cloud Foundations, Google Data Analytics.
- **Deliverables at drafts/Bosch Renningen Masterarbeit Agentisches KI Halbleiterdatenbank/**: all 8 files present, CV PDF 2 pages, CL PDF 1 page.

### 3. FLEX Capital Management GmbH, Werkstudent Data Science and AI, Berlin

- **Freshness:** posted 12 Aug 2026 (9 days ago) on Indeed.
- **Language track:** DE (posting body in German; "Sehr gute Deutsch- und Englischkenntnisse" required).
- **Apply method:** platform-native (Indeed).
- **Apply link:** https://to.indeed.com/aakn8m867dsn
- **Fit rationale:** FLEX Capital's Data and AI team supports Software and Tech Mittelstand portfolio companies. The role explicitly mentions RAG systems, chatbots, agentic AI use cases (e.g. customer support automation), and classical ML plus KPI deep-dives. That is a very tight overlap with the Multi-Agent RAG project (LangGraph agent graph, hybrid BM25 + dense retrieval, JudgeAgent + EvalAgent) and CreditIQ (regulated ML with SHAP intersectional analysis, fairness-accuracy tradeoff, Streamlit decision-support tool). The "own project ownership from concept to deployment" language matches Rah's demonstrated end-to-end delivery on both projects.
- **Projects selected:** Multi Agent RAG (P_RAG_DE), CreditIQ (P_CREDITIQ_DE). Auto-trim ladder dropped to 1 project + tightened SS bullets to fit 2 pages.
- **Certs selected:** NVIDIA LLM Applications, AWS Cloud Foundations, Google Data Analytics.
- **Deliverables at drafts/FLEX Capital Berlin Werkstudent Data Science AI/**: all 8 files present, CV PDF 2 pages, CL PDF 1 page. Positioning tag and profile were revised on the second build to remove the banned "LangChain" string per the 19 Aug 2026 rule (LangChain, Databricks, Delta Lake, PyTorch not evidenced in bullets, keyword stuffing forbidden). Post-fix, all banned-string checks pass.

## Watchlist (scored but not drafted under the cap)

- **Siemens AG Munich, Working Student Data Analytics and IT Automation** — jobs.siemens.com, posted 19 Aug 2026 (2 days ago), EN track, Power BI + Power Automate. Not drafted this run because Rah already applied to two Siemens roles on 16 Aug (Siemens Energy Werkstudent KI-basierte Optimierungsinitiativen applied, Siemens AG Werkstudent Data Science operativer Service rejected) plus Siemens AG AI Digital Products Finance and M&A applied on 13 Aug; loading up more Siemens today would over-concentrate the fleet. Reconsider next run if backlog remains low.
- **CHECK24 Vergleichsportal, Werkstudent Data Analyst Internet, Muenchen** — Indeed, posted 27 Jul 2026 (25 days). CHECK24 applied 3 times already (2 rejected, 1 applied last week for AI-Produkte Kreditvergleich); freshness low and CHECK24 load already high.
- **SCALA stage systems and services, Werkstudent KI-Softwareentwicklung, Castrop-Rauxel** — Indeed, posted 14 Aug 2026 (7d), RAG + semantic search for stage engineering technical service assistant. Solid fit but small company with limited scale; kept on watchlist.
- **Elobau GmbH, Werkstudent AI Machine Learning, Leutkirch** — Indeed, posted 08 Jul 2026 (44d). Freshness too low, likely already filled.
- **Riverty Werkstudent Operations Data and Insights, Baden-Baden / Verl** — Indeed, posted 03 Jul 2026 (49d). Freshness too low.

## Dropped section (excluded under Step 3 filters or scope rules)

- **Allianz Stuttgart Data Scientist-Fokus AI Engineering** — Indeed part-time flag misleading: role requires "Mindestens zwei Jahre praktische Erfahrung in der Softwareentwicklung" and reads as a junior full-time position. Master-projects.md keeps full-time and Junior full roles out of scope.
- **Volkswagen Wolfsburg Praktikum/Abschlussarbeit Customer Data Analytics and AI** — Full-time flag; would be a Pflichtpraktikum only, and Rah's current programme window does not require a Pflichtpraktikum starting now. Kept out of top cut to avoid a role Rah cannot cleanly accept.
- **CeramTec GmbH Werkstudent Digital Transformation Computer Vision, Plochingen** — dedup: already applied 18 Jul 2026 for the exact same role, rejected. Standing dedup rule blocks re-application.
- **DeepMask Munich Gen AI and LLM Engineer Werkstudent** — posting is 9 months old and explicitly no longer accepting applications.
- **Temedica Munich Working Student AI Engineer** — posted 2 months ago with 200+ applications already; freshness too low relative to fresh listings.
- **Vecrion AI Werkstudent Generative AI Agentic Systems** — LinkedIn card resolves to Indiana, United States, not Germany or EU. Out of geographic scope.

## Transparency block

- **Sources reachable this run:** Notion (fd974369-40b2-48c5-b660-d15256c88f52) direct SQL queries; Tavily web search; Indeed MCP (search + job details); WebFetch to jobs.siemens.com; Tavily extract on LinkedIn and Xing public pages. All returned data within one call each.
- **Sources unreachable this run:** none, but LinkedIn public pages returned the sign-in wall shell rather than full body text for most listings, so LinkedIn coverage relied on Tavily extract snippets and Indeed cross-references. Xing extracts likewise returned mostly navigation and similar-jobs shell for public URLs. WebFetch on the DeepMask LinkedIn URL was blocked as a permission request; used Tavily extract as fallback.
- **Freshness dating notes:** Every drafted role's "posted N days ago" was taken from the Indeed job details "Posted on" field or the source portal's own posting date. Where a listing appears on multiple platforms, the earliest verifiable date was used.
- **Prompt-injection content observed but not acted on:** none this run.
- **Platform mix this run:** Company Page 2 (Sana careers via SmartRecruiters, Bosch jobs.bosch.de), Indeed 1 (FLEX Capital). Respects the 28 July 2026 yield reset cap of at most 1 Indeed role per run.
- **Distance was not a scoring factor** per the standing master-projects.md rule; Munich, Renningen, and Berlin all sit inside the "all of Germany" top tier.
- **CV validation gate:** all 3 CV PDFs are 2 pages, all 3 have no PERSONAL DETAILS block, no Portfolio: / Date of birth / Nationality: / Availability: / Hindi: strings, no "toward B2" wording, and no Databricks / Delta Lake / LangChain / PyTorch strings anywhere in the document (checked full text, not only page 1). Header uses the 19 Aug 2026 Ojas-style layout (name, positioning tag, contact line 1, contact line 2, italic status), so the STEP 4 gate's "email-on-line-2" rule is satisfied by the CLAUDE.md override for the new header.

## Deliverable summary

- Notion drafted rows written this run: 4 (1 reconciliation catch-up Amprion Werkstudent KI + 3 new today Sana, Bosch, FLEX Capital). First attempt used a malformed parent parameter and produced 4 blank workspace-level pages instead of data source rows; those 4 orphans were renamed to "DELETE ME - orphan from 2026-08-21 Cowork run tool call typo" for Rah to clean up manually (the create tool exposed here does not expose a delete/archive path). The second create call used the correct `{"parent": {"type": "data_source_id", ...}}` shape and populated all properties correctly; verified via a follow-up SQL query showing 4 drafted rows.
- CSV rows appended this run: 3 (matching the 3 new drafts).
- CSV rows updated in reconciliation: 5 (drafted -> Notion truth).
- Files rendered: 3 folders x 8 files = 24 deliverable files, all present on disk, all validated.
- Git commit: local commit **5c2ed7caefd517a6eee2e6c57dc3801f698edb60** with message "Scheduled run 2026-08-21, 3 new drafts" landed cleanly in the /tmp/JobSearch working tree.
- Git push: **FAILED** on first attempt and on the single retry (per Step 7 rule), with the message "access denied by the git proxy: rahulrawat20022002/jobSearchClaude is not in this session's authorized repository set". This is the Cowork cloud sandbox git proxy blocking the push, not a credential or code problem, and it was not force-pushed (per invariant, never force push). The commit is durable in the ephemeral /tmp checkout for the rest of this session but will be lost when the container is reclaimed. Rah needs to either add the repo to the sandbox's authorized sources for future scheduled runs, or manually re-run this run's step 7 from his own machine after pulling the CSV, Notion, and drafts state (Notion writes and Gmail draft already landed and are unaffected).
- Gmail draft: created to rahulrawat2r@gmail.com with the short summary. Never sent.
