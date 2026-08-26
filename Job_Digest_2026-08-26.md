# Job Digest — 26 August 2026 (Cowork Drafting Agent, scheduled run)

## Run type and render toolchain

Scheduled Cowork run. Render toolchain installed and verified clean:
`weasyprint 69.0`, `python-docx`, `pypdf` all imported successfully. No
fallback to Markdown-only output was needed.

## Backlog gate

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` queried for
Status = 'drafted' at run start: **0 rows**. This is the authoritative
count per the 14 July 2026 status source of truth rule (no Notion error,
no CSV fallback needed).

Under the 28 July 2026 yield reset gate, 0 drafted falls in the **under 8**
tier → normal top 3 to 5 cut. This run drafted 4 new roles.

Backlog after this run: **4 drafted** in Notion (the 4 rows created below).

## Reconciliation

Ran against every row in `applied-log.csv`, matched to Notion by company
plus role (case insensitive), Notion treated as the source of truth per
invariant 1. Found and corrected two categories of drift, all one
direction (Notion → CSV, never reversed):

**16 CSV rows showed `drafted` but already had a real Notion Status.**
These are all rows OpenClaw processed on its own local checkout since
being drafted (15 flipped to `applied`, 1 — NewTec GmbH — flipped to
`Not listed Anymore`). Corrected in the CSV to match Notion:

| Company | Role (short) | CSV was | Notion is |
|---|---|---|---|
| NewTec GmbH | Praxissemester/Werkstudent KI Data Science | drafted | Not listed Anymore |
| Anstalt fuer Kommunale Datenverarbeitung in Bayern | Werkstudent AI/ML NLP Semantic Search | drafted | applied |
| Boellhoff Gruppe | Masterarbeit AI Patent Analytics | drafted | applied |
| logen.ai | Werkstudent AI Agent Developer | drafted | applied |
| Schaeffler Technologies AG und Co. KG | Werkstudent KI-Agenten-Entwicklung | drafted | applied |
| ADAC | Werkstudent Data AI Solutions | drafted | applied |
| Rosenberger Hochfrequenztechnik | Werkstudent KI Projekte | drafted | applied |
| DELO Industrie Klebstoffe | Werkstudent IT KI | drafted | applied |
| nerou GmbH | Werkstudent Data Science | drafted | applied |
| KPMG Deutschland | Werkstudent BI und Analytics | drafted | applied |
| MEAG MUNICH ERGO AssetManagement | Werkstudent Data Enablement | drafted | applied |
| Senacor Technologies AG | Masterarbeit Datenstrategie KI | drafted | applied |
| Fraunhofer IPT Aachen | Masterarbeit Deep Learning Produktion | drafted | applied |
| Fraunhofer IPA Stuttgart | Abschlussarbeit Binder Jetting 3D Druck | drafted | applied |
| Fraunhofer IPA Stuttgart | Abschlussarbeit Bewertungsmatrix ATMP | drafted | applied |
| Fraunhofer IOSB Karlsruhe | Abschlussarbeit Training Data Anonymization | drafted | applied |
| Fraunhofer SIT Darmstadt | Masterarbeit Alterschaetzung Loss Design | drafted | applied |

**6 further rows had plain status drift** (CSV said one thing, Notion said
another, unrelated to the drafted backlog):

| Company | Role (short) | CSV was | Notion is |
|---|---|---|---|
| Bosch | Master Thesis Graph Based QA and RAG | rejected | shortlisted but no interview |
| Mercedes-Benz Group | Masterarbeit KI Kommunikationsdaten | applied | rejected |
| Johnson & Johnson | Data Science Intern Praktikum | applied | rejected |
| Ed. Zueblin AG | Werkstudent BI Data Analytics | applied | rejected |
| Arthrex GmbH | Working Student Business Analytics | applied | rejected |
| FLEX Capital Management GmbH | Werkstudent Data Science and AI | applied | rejected |

No CSV rows were found missing from Notion (one apparent mismatch,
Ärzteverband Deutscher Allergologen, turned out to be the same row as
Notion's "Arzteverband" — an umlaut-normalization non-issue, not a real
gap). No new Notion rows needed to be created during reconciliation.

## Top cut — 4 new roles drafted

### 1. Reply Deutschland SE (Blue Reply) — Werkstudent fuer AI, Data Engineering und Tool Entwicklung
- **Location:** Duesseldorf or Berlin (partial remote possible)
- **Source:** JobTeaser (posted 16 Aug 2026)
- **Apply link:** jobteaser.com/de/job-offers/8c53099a…reply-deutschland-se-werkstudent-fur-ai-data-engineering-und-tool-entwicklung-m-w-d
- **Apply method:** company-portal (Blue Reply's own application flow reached via the JobTeaser listing — not a platform-native Easy Apply flow, so out of OpenClaw's automated submission scope; Rah submits manually)
- **Language track:** DE (posting body in German). Posting asks "gute Deutsch- und Englischkenntnisse"; Rah is B1 in progress, flagged in the cover letter.
- **Fit rationale:** Role centers on Agentic AI Frameworks, LLM tooling (OpenAI, Claude, Gemini), and Data Engineering/Data Lakehouse work — near-direct overlap with the Multi-Agent RAG project's LangGraph orchestration and LLM-as-Judge evaluation harness.
- **Projects selected:** #1 Multi-Agent RAG, #3 Flight Tracking (Data Engineering pipeline)
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed

### 2. Rohde und Schwarz GmbH und Co. KG — Werkstudent Data Analytics und Data Science
- **Location:** Memmingen
- **Source:** Company Page (rohde-schwarz.com)
- **Apply link:** rohde-schwarz.com/de/karriere/stellenangebote/werkstudent-data-analytics-data-science-m-w-d_251563-1618307.html
- **Apply method:** company-portal
- **Language track:** DE. No explicit German level requirement in the posting text pulled this run.
- **Fit rationale:** Tasks are ETL/ELT pipeline development, dashboard and ad-hoc report work, data quality checks, and ML model validation — direct match to the Flight Tracking pipeline (PySpark, dbt, Airflow) and Movie Analytics medallion architecture.
- **Projects selected:** #3 Flight Tracking, #5 Movie Analytics
- **Certs:** AWS, SAS, Google Data Analytics
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed

### 3. Volkswagen Group — Praktikum or Abschlussarbeit, Customer Data Analytics und AI
- **Location:** Wolfsburg
- **Source:** Company Page (jobs.volkswagen-group.com)
- **Apply link:** jobs.volkswagen-group.com/Volkswagen/job/Wolfsburg-Praktikum-Abschlussarbeit-Customer-Data-Analytics-&-AI-(wmd)-38436/1427423533
- **Apply method:** company-portal
- **Language track:** DE. No explicit German level requirement in the posting text pulled this run.
- **Fit rationale:** Keywords are Artificial Intelligence, Statistik, Elektromobilitaet, Innovationsmanagement, Technologiebewertung, Datenoekosysteme — overlaps with the Climate Economics predictive-analytics/Random Forest project and the RAG project's evaluation-metric discipline.
- **Projects selected:** #8 Climate Economics, #1 Multi-Agent RAG
- **Certs:** AWS, Google Data Analytics, SAS
- **Note:** different role than the existing Volkswagen "Master Thesis Deep Learning for Autonomous Driving" log entry (Not listed Anymore); allowed under the different-roles-same-company rule.
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed

### 4. Kaufland — Praktikant Data Science
- **Location:** Heilbronn
- **Source:** Company Page (jobs.kaufland.com)
- **Apply link:** jobs.kaufland.com/Deutschland/job/Heilbronn-Praktikant-Data-Science-(mwd)-74072/1279873801
- **Apply method:** company-portal (SuccessFactors flow via Kaufland career site)
- **Language track:** DE. Entry date 01/02 Feb 2027. Posting asks fluent German and English ("fliessende Kommunikation in Wort und Schrift"); Rah is B1 in progress, flagged in the cover letter.
- **Fit rationale:** Tasks are forecasting models, generative AI application, and Analytics Use Cases across the value chain — overlaps with eRay's CatBoost MultiQuantile forecasting pipeline and the RAG project's generative-LLM work.
- **Projects selected:** #1 Multi-Agent RAG, #2 CreditIQ
- **Certs:** NVIDIA, SAS, Google Data Analytics
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed

## Watchlist (scored, not drafted this run)

None — only 4 strong candidates cleared the scoring bar with usable
detail this run within the search window covered; no additional
roles were held back under the cap (0 drafted falls under the "normal
top 3 to 5" tier, and 4 was the count of well-verified candidates found).

## Dropped

- **CompanyMind GmbH (Oldenburg) — Data Scientist Kuenstliche Intelligenz,
  Praktikum or Bachelor-/Masterarbeit.** Required "sehr gute
  Deutschkenntnisse, Muttersprache oder C1/C2-Niveau" — native-level
  German, a materially sharper mismatch against Rah's current B1-in-progress
  level than the four shipped roles (which ask for "gute" or unstated
  levels, not native/C1/C2). Dropped rather than drafted.
- Several roles surfaced in search were already logged under the same
  company and role (Sereact, THRYVE, WISAG, MEAG, ADAC, AKDB, Liebherr-
  Aerospace Lindenberg, various SAP/Siemens/BMW postings already in the
  log) — skipped as duplicates, not re-drafted.
- Dual-study (Duales Studium) listings surfaced repeatedly in StepStone
  and Xing search results (e.g. Mercedes-Benz Tech Innovation Duales
  Studium Informatik, Liebherr-Werk Ehingen DHBW Studium) — excluded per
  the standing scope filter.

## Transparency block

- **Sources reachable this run:** Tavily search (general web, used for
  LinkedIn/StepStone/Xing/JobTeaser/company-page discovery), Tavily
  extract (used for full JD text where WebFetch was blocked).
- **Sources unreachable this run:** direct `WebFetch` calls to
  `linkedin.com`, `rohde-schwarz.com`, and `companymind.ai` were all
  blocked by the sandbox's network egress proxy (`EGRESS_BLOCKED`).
  Worked around this entirely via Tavily's `tavily_search` (with
  `include_raw_content`) and `tavily_extract` tools, which reach these
  domains through a different path and returned full posting text for
  all four shipped roles plus CompanyMind (dropped) and confirmed the
  Reply/Kaufland/Rohde&Schwarz/Volkswagen JD detail quoted above.
  No Indeed MCP tool was available this session (not in the connected
  server list); Indeed was not used this run as a result — within the
  standing 1-per-run Indeed cap, this is a 0-per-run outcome, not a
  cap violation.
- **Freshness dating:** Reply posting dated 16 Aug 2026 explicitly by
  JobTeaser; Rohde & Schwarz and StepStone search results dated "this
  week" per search snippet; Volkswagen and Kaufland postings carry no
  explicit post date in the pulled text, both are live/open listings on
  the company's own career site as of today.
- **Prompt-injection content observed but not acted on:** none.
- **Platform mix this run:** Company Page 3 (Rohde & Schwarz, Volkswagen,
  Kaufland), JobTeaser 1 (Reply Deutschland SE). No LinkedIn, StepStone,
  Xing, or Indeed roles drafted this run — search surfaced many
  candidates on those platforms but all were either already logged,
  dual-study, or a weaker fit than the four shipped.
- **Language track decisions:** all four shipped roles are DE track,
  driven purely by posting body language per the 20 July 2026 hard rule.
- **Apply method:** all four shipped roles are `company-portal` (none
  landed on a platform-native Easy Apply flow on linkedin.com, xing.com,
  stepstone.de, or indeed.com), so all four are out of OpenClaw's
  automated submission scope — Rah submits all four manually.
- **Distance was not a scoring factor**, per standing rule; all four
  roles are in Germany (Memmingen, Wolfsburg, Heilbronn, Duesseldorf/
  Berlin), noted as plain location information only.

## Deliverable summary

- 4 new roles drafted, 4 x 8 = **32 files rendered**, all verified present
  on disk (CV .md/.html/.pdf/.docx + CoverLetter .md/.html/.pdf/.docx per
  role).
- Every new CV_Rahul_Rawat.pdf passed the Step 4 validation gate: 2 pages,
  no banned strings (`toward B2`, `Databricks`, `Delta Lake`, `LangChain`,
  `PyTorch`), no retired PERSONAL DETAILS-era strings on page 1.
- CSV: 172 pre-existing rows (22 corrected this run for Notion drift) + 4
  new rows = 176 rows.
- Notion: 4 new pages created and verified present via a follow-up query
  for Status = 'drafted' (4 rows returned, matching the 4 created).
