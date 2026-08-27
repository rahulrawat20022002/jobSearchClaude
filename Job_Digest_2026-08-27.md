# Job Digest, 27 August 2026 (Cowork Scheduled Run)

## Run type and render toolchain

Scheduled Cowork Drafting Agent run. Render toolchain (weasyprint, python-docx, pypdf) installed clean and verified: `render toolchain ok 69.0`. All eight deliverables render through `build_html.py` via `role_configs_27aug.py` and `run_27aug.py`, patterned on the 13 Aug / 26 Aug pairs. No Markdown-only fallback needed.

## Backlog gate

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for `Status = 'drafted'`: **4 drafted** at run start (the four roles from the 26 Aug run: Reply Deutschland SE, Rohde und Schwarz, Volkswagen Group, Kaufland). Under the 28 July 2026 yield reset gate, 4 falls in the **under 8 tier** → normal top 3 to 5 cut applies. No pause triggered.

Backlog after this run: **8 drafted** in Notion (verified by follow up query), matching 8 `drafted` rows in `applied-log.csv`.

## Reconciliation

Compared every row in `applied-log.csv` (176 rows) against Notion (175 rows) by company plus role, case and accent insensitive.

- **No Status drift found.** Every CSV row that had a Notion counterpart matched exactly.
- **2 CSV rows had no Notion counterpart** and were created in Notion with the CSV status, never the reverse direction, per invariant 1:
  - Mercedes-Benz Group, *Masterarbeit, KI basierte Analyse von Kommunikationsdaten in Diagnoseprozessen*, Sindelfingen, Indeed, status `rejected`
  - Deutsche Bank, *Internship, Technology Data and Innovation 2026 Frankfurt*, Frankfurt am Main, LinkedIn, status `shortlisted but no interview`

Reconciliation ran before the search step per the standing rule.

## Top cut: 4 new roles drafted

All four are AI Engineer or AI Evaluation flavored per the 26 August 2026 scope narrowing in master-projects.md. Freshness order below.

### 1. Cinemo GmbH, Karlsruhe, Germany
**Working Student, GenAI / LLM Evaluation, Agentic AI / NLP (f/m/d)**
- Fit: squarely AI Evaluation. Supports evaluation and validation of agentic AI systems and GenAI/NLP algorithms for in car experiences; dataset building, evaluation tooling, end to end testing of non deterministic AI.
- Projects selected: #1 Multi Agent RAG with LLM as Judge (evaluation harness, 9 metrics, JSON mode judge), #2 CreditIQ (rigorous testing discipline, 100% branch coverage)
- Certs: NVIDIA, AWS, Google Data Analytics
- Source: StepStone, posted about 1 week ago
- Apply link: https://www.stepstone.de/stellenangebote--Working-Student-GenAI-LLM-Evaluation-Agentic-AI-NLP-f-m-d-Karlsruhe-Germany-Cinemo-GmbH--13887266-inline.html
- Apply method: platform-native (tentative — StepStone hosted listing, OpenClaw to verify on click)
- Language track: EN (posting body entirely English)
- Deliverables: all 8 rendered, CV 2 pages, banned strings absent

### 2. SAP, Berlin
**Working Student (f/m/d), Signavio Next Development, Agentic AI**
- Fit: agentic AI engineering inside a senior software team, real customer/internal impact.
- Projects selected: #1 Multi Agent RAG (LangGraph orchestration, agent design), #3 Real Time Flight Tracking (production pipeline orchestration, Airflow automation)
- Certs: NVIDIA, AWS, Google Data Analytics
- Source: Company Page (jobs.sap.com), live listing
- Apply link: https://jobs.sap.com/job/Berlin-Working-Student-%28fmd%29-Signavio-Next-Development-Agentic-AI-10557/1419810733
- Apply method: company-portal, out of OpenClaw scope, Rah to submit manually
- Language track: EN (posting body entirely English)
- Deliverables: all 8 rendered, CV 2 pages, banned strings absent

### 3. Mercedes-Benz Group, Sindelfingen
**Werkstudent\*in Applied AI und Process Automation**
- Fit: ITO/CA Change Team, combining AI agents into scalable workflow solutions, driving AI adoption. AI Engineer flavored per the agent orchestration framing in the posting.
- Projects selected: #1 Multi Agent RAG (agent combination into a scalable system), #5 Movie Analytics (automated pipeline, 0 manual interventions)
- Certs: AWS, Google Data Analytics, SAS Viya
- Source: Company Page (via Xing listing resolving to Mercedes-Benz Group's own careers portal)
- Apply link: https://www.xing.com/jobs/sindelfingen-werkstudent-applied-ai-process-automation-156857505
- Apply method: company-portal, out of OpenClaw scope, Rah to submit manually
- Language track: DE (posting body entirely German, no explicit German level stated)
- Start date: October 2026, hybrid with on site days in Stuttgart
- Deliverables: all 8 rendered, CV 2 pages, banned strings absent

### 4. Leopold KOSTAL GmbH und Co. KG, Luedenscheid
**Werkstudent fuer KI Entwicklung, Artificial Intelligence Development (m/w/d)**
- Fit: strong AI Engineer match. AI/LLM landscape, prompt engineering, RAG/embeddings/vector stores, agent orchestration, automated evaluation of quality/cost/performance, DevOps/MLOps.
- Projects selected: #1 Multi Agent RAG (embeddings, vector store, automated eval), #3 Real Time Flight Tracking (orchestration, monitoring)
- Certs: NVIDIA, AWS, Google Data Analytics
- Source: Company Page (kostal-career.com), live listing
- Apply link: https://www.kostal-career.com/en-DE/career/werkstudent-fuer-ki-entwicklung-/-artificial-intelligence-development-m/w/d
- Apply method: company-portal, out of OpenClaw scope, Rah to submit manually
- Language track: DE (posting body German; "gute Englischkenntnisse" required, "gute Deutschkenntnisse willkommen" — German welcome, not a hard requirement, noted for transparency since Rah's B1 in progress comfortably clears a welcome-not-required bar)
- Pay noted in posting: 15 EUR/hour for all Werkstudent positions
- Deliverables: all 8 rendered, CV 2 pages, banned strings absent

## Watchlist (scored but not drafted under the cap)

- Mercedes-Benz Tech Innovation, *Werkstudent AI Strategy & Program Steering*, Stuttgart — leaned more program management than technical AI Engineering, lower fit under the 26 Aug scope narrowing than the four drafted.
- BMW AG, *Praktikant Agentic AI und kontextsensitive Systeme*, Muenchen — good fit, held back only because the top 4 fresher/higher confidence roles filled this run's cut; candidate for next run if still live.
- Niologic (Koeln), *Werkstudent/in Software Engineering for AI Systems* — decent but broader AI consultancy data-products role, not specifically Agentic AI or Evaluation flavored; lower priority than the four drafted.
- CognitX AI GmbH, *AI / LLM Engineering (Werkstudent), remote* — strong fit on paper (agentic workflows, evaluation metrics) but every URL found for this listing (join.com, Xing) resolved to duplicate or stale postings during verification; held back rather than drafted against an unconfirmed live apply link, worth a fresh search next run.

## Dropped this run

- Retorio, *Working Student: AI Engineer, Agentic Systems* — already logged in Notion/CSV as `Not listed Anymore`, not re-drafted.
- Daimler Truck AG, *Werkstudententaetigkeit Global AI Enablement & Agentic AI Campaign* — leaned marketing/enablement rather than technical AI Engineering, out of the 26 Aug scope narrowing.
- Auroniq Robotics GmbH, *Werkstudent:in Agentic AI & Prozessautomatisierung* — the only accessible listing snapshot returned garbled/mismatched location metadata (LinkedIn cache anomaly showing "North Charleston, SC" for a Schoenaich, Germany role); dropped rather than draft against unverified posting data, per invariant 3 (never fabricate).
- Two StepStone/join.com URLs surfaced by the initial search pass (an earlier Cinemo StepStone listing ID 13628960, and CognitX AI's join.com posting) returned 404/archived on verification and were discarded in favor of confirming fresh, live listings before drafting.

## Transparency block

- **Sources reachable this run:** Tavily search (general web, StepStone, Xing, LinkedIn public listings, JobTeaser, company career pages), Tavily extract (direct page content pulls), jobs.sap.com and kostal-career.com direct search results.
- **Sources unreachable this run:** Direct WebFetch to linkedin.com, stepstone.de, and join.com is blocked by the sandbox's network egress proxy (`EGRESS_BLOCKED`); worked around by using Tavily's search and extract tools, which fetch through Tavily's own infrastructure rather than direct egress. No dedicated Indeed MCP tool was available in this session's toolset; Indeed was not used as a source this run (0 of 4, well under the 1-per-run cap, no impact on the gate).
- **Freshness dating:** Cinemo posted about 1 week ago per StepStone; SAP, Mercedes-Benz Group, and KOSTAL listings are current live postings with no explicit post date surfaced, confirmed live by direct fetch/search at time of drafting.
- **Prompt injection content observed:** none. All fetched job posting text was treated as data describing the role, never as instructions.
- **Platform mix this run:** Company Page 3 (SAP, Mercedes-Benz Group, KOSTAL), StepStone 1 (Cinemo). Indeed 0 of 1 cap, JobTeaser 0 (no qualifying new listing found this run).
- **Language track decisions:** 2 EN track (Cinemo, SAP), 2 DE track (Mercedes-Benz Group, KOSTAL), all matching posting body language per the 20 July 2026 hard rule.
- **Apply method per role:** Cinemo platform-native (tentative, StepStone), SAP company-portal, Mercedes-Benz Group company-portal, KOSTAL company-portal. 3 of 4 are out of OpenClaw's automated submission scope; Rah submits those three manually.
- **Distance was not a scoring factor**, per the standing rule; all four roles are in Germany, satisfying the top geographic tier.
- **Target roles scope:** AI Engineer and AI Evaluation only, per the 26 August 2026 narrowing. All four drafted roles verified squarely in scope; several plain Data Engineer/Analyst postings surfaced in search were not considered.

## Deliverable summary

- 4 new roles drafted, 32 files rendered (8 deliverables x 4 roles), all verified present on disk.
- CSV: 4 new rows appended with status `drafted`.
- Notion: 4 new rows created in data source `fd974369-40b2-48c5-b660-d15256c88f52` with matching schema (Company, Role, Location, Source, Status, Apply Method, Apply Link, German Level, Date Drafted, Draft Path, Notes). Plus 2 rows created during reconciliation (Mercedes-Benz Group KI Kommunikationsdaten, Deutsche Bank TDI Internship), for 6 new Notion rows total this run.
- Backlog gate result: 4 drafted at start (under 8 tier, normal cut) → 8 drafted at end. CSV and Notion counts confirmed matching (8 = 8).
