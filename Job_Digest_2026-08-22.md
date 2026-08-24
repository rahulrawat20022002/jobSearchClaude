# Job Digest, 22 August 2026 — Cowork Scheduled Run

**Run type:** Scheduled Cowork drafting run (Agent A). Render toolchain: weasyprint 69.0, python-docx, pypdf all installed and verified before proceeding.

## Backlog gate

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` (source of truth) returned **0 rows** in Status = `drafted` at run start. Under 8 drafted falls in the **normal top 3 to 5** tier under the 28 July 2026 yield reset. Morning pass held to **top 3**; Rah then asked Cowork to continue searching, with a focus on AI Engineer roles specifically, to fill out the remaining room in the band. Afternoon supplemental pass added **2 more**, for **5 total today** — the top of the normal range. One candidate across both passes was scored but not drafted (see Watchlist).

## Reconciliation

Found and fixed drift: **6 CSV rows** were stale at `drafted` while Notion already showed `applied` for the same company plus role (OpenClaw had processed them since the last Cowork run but the CSV mirror hadn't caught up). Per invariant #1, Notion is the source of truth — CSV updated to match, never the reverse:

| Company | Role | CSV was | Notion says | CSV now |
|---|---|---|---|---|
| Amprion GmbH | Werkstudent, KI Stellen-ID 7959 | drafted | applied | applied |
| BCG Platinion | Werkstudent, AI und Data Analytics, Energy Knowledge Management | drafted | applied | applied |
| Arthrex GmbH | Working Student, Business Analytics and Process Optimization | drafted | applied | applied |
| Sana HR Solutions GmbH | Werkstudent, Data Engineer Taetigkeits-ID 7016 | drafted | applied | applied |
| Robert Bosch GmbH | Masterarbeit, Agentisches KI-System fuer eine Halbleiterdatenbank REF293881R | drafted | applied | applied |
| FLEX Capital Management GmbH | Werkstudent, Data Science and AI | drafted | applied | applied |

No CSV row was missing a Notion counterpart (full 154-row cross check, both directions).

## Top cut (5 new roles drafted across two passes)

### 1. NewTec GmbH — Praxissemester/Werkstudent, KI und Data Science
- **Location:** Ulm | **Source:** Xing (posted ~11 hours before draft, very fresh) | **Apply method:** platform-native
- **Apply link:** https://www.xing.com/jobs/ulm-praxissemester-werkstudent-ki-data-science-157353273
- **Language track:** DE (posting body in German) | **German level required:** not explicitly stated beyond German-language posting; Rah's B1 in progress noted in the cover letter
- **Fit rationale:** Posting centers on SQL database work and building in-house AI use cases end to end. Tailored around the Flight Tracking pipeline (SQL-adjacent dbt modeling, 128K+ record joins) and the Multi-Agent RAG project (idea-to-measurable-evaluation AI use case pattern).
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed.

### 2. Anstalt fuer Kommunale Datenverarbeitung in Bayern (AKDB) — Werkstudent, AI and Machine Learning, NLP and Semantic Search
- **Location:** Muenchen | **Source:** StepStone (posted ~1 day before draft) | **Apply method:** company-portal (public-authority career portal reached via StepStone; not a confirmed in-aggregator Easy Apply flow — flagged for OpenClaw to verify before attempting submission)
- **Apply link:** https://www.stepstone.de/stellenangebote--Werkstudent-AI-and-Machine-Learning-NLP-and-Semantic-Search-m-w-d-Muenchen-Anstalt-fuer-Kommunale-Datenverarbeitung-in-Bayern-AKDB--14368530-inline.html
- **Language track:** DE | **German level required:** **C1** (verhandlungssicher), well above Rah's current B1 — disclosed openly in the cover letter's final paragraph, shipped anyway per the standing rule that language level does not filter listings.
- **Fit rationale:** Role builds a knowledge base on text embeddings and semantic search (FAISS/Weaviate/Milvus/Pinecone-class stack). Directly mirrors the Multi-Agent RAG project's migration to a shared multilingual Pinecone vector space and its EN/DE cross-language retrieval.
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed.

### 3. Boellhoff Gruppe — Masterarbeit, AI driven Patent Analytics
- **Location:** Bielefeld | **Source:** Company Page (jobs.boellhoff.com) | **Apply method:** company-portal (Rah submits manually, out of OpenClaw scope)
- **Apply link:** https://jobs.boellhoff.com/Masterarbeit-mit-optionalem-Praktikum-Werkstudententaetigk-de-j5807.html
- **Language track:** DE | **German level required:** not stated on the posting
- **Fit rationale:** Masterarbeit in the Patentwesen department applying AI methods (LLM fine-tuning, RAG, NLP, time series, graph ML) to extract insight from patent data. Tailored around the RAG project's evaluation harness (5 retrieval + 4 generation metrics) and CreditIQ's SHAP-driven subgroup analysis, both framed as "systematic, measurable insight extraction from a large unstructured corpus."
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed.

## Afternoon supplemental pass (AI Engineer focus, per Rah's request)

### 4. logen.ai — Werkstudent, AI Agent Developer
- **Location:** Berlin | **Source:** Other (Arbeitnow aggregator — hosts its own application form rather than redirecting to a company career page) | **Apply method:** company-portal (platform ambiguous, defaulted out of OpenClaw scope per the standing rule)
- **Apply link:** https://www.arbeitnow.com/jobs/companies/logenai/werkstudentin-ai-agent-developer-berlin-314047
- **Language track:** DE | **German level required:** not stated
- **Fit rationale:** Small Berlin AI startup building production AI agents and voicebots for customer service automation (own SaaS product, AIdapt). Posting explicitly wants hands-on agent development — code, API debugging, conversation flows — not proof-of-concept work. Tailored around the RAG project's multi-agent LangGraph orchestration and the Movie Analytics pipeline's fully unattended production automation.
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed.

### 5. Schaeffler Technologies AG und Co. KG — Werkstudent, KI-Agenten-Entwicklung im Projektmanagement
- **Location:** Herzogenaurach | **Source:** Company Page (jobs.schaeffler.com) | **Apply method:** company-portal (Rah submits manually, out of OpenClaw scope)
- **Apply link:** https://jobs.schaeffler.com/job/Herzogenaurach-Werkstudent-KI-Agenten-Entwicklung-im-Projektmanagement-(dmw)-91074/1423788133
- **Language track:** DE | **German level required:** not stated
- **Fit rationale:** Werkstudent role on the "Drive to Performance" project — building KI agents, prompt engineering, technical documentation, testing and analysis of KI/LLM applications. Tailored around the RAG project's structured JSON-mode evaluation harness and CreditIQ's test-and-document discipline (100% branch coverage, full regulatory writeup). 12-month term starting immediately.
- **Skill honesty note:** the posting mentions Python and TypeScript. master-projects.md documents React/JavaScript experience but not TypeScript specifically, so TypeScript is not claimed anywhere in this CV or cover letter — only Python and LangGraph, which are actually on record.
- **Deliverables:** all 8 rendered, CV 2 pages, validation gate passed.

## Watchlist (scored, not drafted)

- **ADAC — Werkstudent Data & AI Solutions (w|m|d), Muenchen, StepStone, posted ~2 days ago.** Strong-looking fit (KI-based solutions incl. M365 Copilot, new AI use case identification), but **every mirror checked** (StepStone, Bundesagentur fuer Arbeit / arbeitsagentur.de, finest-jobs.com, bebee.com) rendered the "Deine Aufgaben" and "Dein Profil" sections **blank behind client-side JavaScript** — only a thin, unverifiable fragment of task text could be recovered from a stale search snippet. Per CLAUDE.md invariant #3 (never fabricate), no CV or cover letter was tailored against unread requirements. Carrying forward as a watchlist item for a future run or for Rah to check manually: https://karriere.adac.de/stellenanzeige/werkstudent-data-ai-solutions-wmd-de-j16758.html
- **Infineon Technologies — Internship, AI Engineering and MLOps, Muenchen, LinkedIn, posted ~1 day ago (afternoon pass).** Same blocked-readability pattern as ADAC — the LinkedIn listing rendered completely blank behind a login wall with no recoverable task or profile text from any angle tried. Not tailored, per invariant #3.

## Dropped

Nothing excluded under Step 3 filters this run — no dual-study/apprenticeship, Quereinsteiger, or voluntary-internship listings surfaced in the search results reviewed.

## Transparency block

- **Sources reachable this run:** Tavily web search/extract (used for LinkedIn, Xing, StepStone, Indeed, and company career pages — no dedicated Indeed MCP tool was available this session, so Indeed leads were checked via Tavily search of indeed.com and de.indeed.com instead of a connector).
- **Sources checked but yielding no fresh, verifiable, non-duplicate lead this run:** LinkedIn (day-range search returned no relevant new postings), Indeed (results were mostly stale cached snapshots with mismatched dates, e.g. "19. März 2026" / "29. November 2025" pages, or already-seen roles) — Indeed is capped at 1/run under the 28 July yield reset and 0 were used today since nothing cleared the freshness/fit bar.
- **Freshness dating:** NewTec Ulm posted ~11 hours before draft (Xing "Vor 11 Stunden"); AKDB Muenchen posted ~1 day before draft (StepStone "Erschienen: vor 1 Tag"); Boellhoff Bielefeld freshness not date-stamped on the posting itself, confirmed as a live open requisition via direct PDF/career-page fetch this week.
- **Prompt-injection content observed:** none.
- **Platform mix across both passes:** StepStone 1 (AKDB), Xing 1 (NewTec), Company Page 2 (Boellhoff, Schaeffler), Other 1 (logen.ai, via Arbeitnow aggregator), Indeed 0, LinkedIn 0.
- **Distance/commute was NOT used as a scoring factor**, per standing rule — Ulm, Muenchen, Bielefeld, Berlin, and Herzogenaurach are noted as plain location information only.

## Deliverable summary

- **5 new roles drafted** across the morning and afternoon passes, all 8 deliverables each (CV/.md/.html/.pdf/.docx + CoverLetter/.md/.html/.pdf/.docx) — 40 files total, all present on disk.
- **CSV:** 5 new `drafted` rows appended; 6 rows reconciled `drafted` → `applied`.
- **Notion:** 5 new pages created under Status `drafted`, verified present via follow-up query.
- **Backlog after this run:** 5 drafted in Notion.
