# Job Digest, 23 August 2026

Run type: scheduled Cowork Drafting Agent (Agent A), automated cron run.
Render toolchain: weasyprint 69.0, python-docx, pypdf installed cleanly via pip in this run's fresh checkout. `import weasyprint, docx, pypdf` printed `render toolchain ok 69.0`. No fallback to Markdown-only output was needed.

## Backlog gate result

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` returned **5** rows with `Status = drafted` at run start (Boellhoff Gruppe, NewTec GmbH, Anstalt fuer Kommunale Datenverarbeitung in Bayern AKDB, Schaeffler Technologies AG und Co. KG, logen.ai). Under the 28 July 2026 yield reset gate, 5 drafted falls in the **under 8, normal top 3 to 5** tier. No fallback to CSV counting was needed, Notion answered on the first query.

Backlog after this run: **9** drafted in Notion (5 pre-existing + 4 new today).

## Reconciliation result

Reconciliation ran per the 11 July 2026 rule regardless of gate zone. 11 CSV rows checked against Notion for the current backlog window.

**Drift found, CSV updated to match Notion (6 rows, all drafted to applied since OpenClaw processed them after the 21 Aug run):**

| Company | Role | CSV before | Notion truth | CSV after |
|---|---|---|---|---|
| Amprion GmbH | Werkstudent, KI Stellen-ID 7959 | drafted | applied | applied |
| BCG Platinion | Werkstudent, AI und Data Analytics, Energy Knowledge Management | drafted | applied | applied |
| Arthrex GmbH | Working Student, Business Analytics and Process Optimization | drafted | applied | applied |
| Sana HR Solutions GmbH | Werkstudent, Data Engineer Taetigkeits-ID 7016 | drafted | applied | applied |
| Robert Bosch GmbH | Masterarbeit, Agentisches KI-System fuer eine Halbleiterdatenbank REF293881R | drafted | applied | applied |
| FLEX Capital Management GmbH | Werkstudent, Data Science and AI | drafted | applied | applied |

**Notion rows with no CSV counterpart, appended to CSV per the Notion CSV Drift playbook (5 rows, all dated 22 Aug 2026 in Notion createdTime, none reflected in this git checkout):**

| Company | Role | Notion Status | Notion Date Drafted |
|---|---|---|---|
| Boellhoff Gruppe | Masterarbeit, AI driven Patent Analytics | drafted | 2026-08-22 |
| Anstalt fuer Kommunale Datenverarbeitung in Bayern | Werkstudent, AI and Machine Learning, NLP and Semantic Search | drafted | 2026-08-22 |
| NewTec GmbH | Praxissemester or Werkstudent, KI und Data Science | drafted | 2026-08-22 |
| Schaeffler Technologies AG und Co. KG | Werkstudent, KI-Agenten-Entwicklung im Projektmanagement | drafted | 2026-08-22 |
| logen.ai | Werkstudent, AI Agent Developer | drafted | 2026-08-22 |

**Flag for Rah, drift with no clean resolution:** all 5 of these rows have a `Draft Path` recorded in Notion but **no matching folder under `drafts/` exists anywhere in this git checkout**, and no CV or CoverLetter PDFs for them exist in the repo history up to and including this run. The Notion createdTime on all 5 is 2026-08-22, a date with no corresponding commit in `git log`. This strongly suggests a Cowork session ran on 22 Aug, wrote its Notion rows successfully, but its git push never landed (the same "access denied by the git proxy" failure mode documented in the 21 Aug digest), so the rendered files were lost when that session's container was reclaimed. Per reconciliation rules Notion still wins on `Status`, so these 5 are now mirrored into the CSV as `drafted`, but **there is nothing to submit for them yet**. Rah should decide whether to re-render these 5 from scratch or clean them out of Notion; they are not part of today's top cut and were not re-drafted in this run to avoid duplicating unverified work.

Reconciliation summary: 11 rows checked, 6 drifts resolved (CSV updated to Notion), 5 rows appended to CSV from Notion, 0 rows created in Notion from CSV.

## Top cut, 4 roles

### 1. Rosenberger Hochfrequenztechnik GmbH und Co. KG, Werkstudent fuer KI Projekte, Fridolfing

- **Freshness:** posted 2 days ago on StepStone.
- **Language track:** DE (posting body in German).
- **Apply method:** platform-native (StepStone one click "Ich bin interessiert" button, no external redirect observed).
- **Apply link:** https://www.stepstone.de/stellenangebote--Werkstudent-fuer-KI-Projekte-m-w-d-Fridolfing-Rosenberger-Hochfrequenztechnik-GmbH-Co-KG--13985042-inline.html
- **German level required:** B2 ("gute Deutschkenntnisse in Wort und Schrift"), above Rah's current B1 in progress. Drafted and flagged rather than dropped, consistent with the AKDB C1 precedent from the 22 Aug batch.
- **Fit rationale:** Rosenberger's posting asks for research and development work on Generative AI and Computer Vision, fine tuning and evaluation of LLMs and multimodal models, Python end to end prototypes, and Azure AI cloud integration. That maps directly onto the Multi Agent RAG project (LangGraph orchestrated agents, LLM as Judge evaluation with a separate judge model to eliminate self preference bias, paired EN/DE eval sets) and onto CreditIQ's full prototype to production path (fairness mitigation, SHAP driven analysis, Streamlit decision support tool, 100 percent branch coverage tests).
- **Projects selected:** Multi Agent RAG (P_RAG_DE), CreditIQ (P_CREDITIQ_DE). Auto-trim ladder dropped to 1 project to hold 2 pages.
- **Certs selected:** NVIDIA Building LLM Applications, AWS Cloud Foundations, Google Data Analytics.
- **Deliverables at `drafts/Rosenberger Fridolfing Werkstudent KI Projekte/`:** all 8 files present, CV PDF 2 pages, validated clean against the banned string and retired header gates.

### 2. ADAC, Werkstudent Data and AI Solutions, Muenchen

- **Freshness:** posted 4 days ago on StepStone.
- **Language track:** DE (posting body in German).
- **Apply method:** left unset in Notion, the ADAC listing did not show StepStone's one click apply button the way the Rosenberger and DELO listings did, so OpenClaw needs to confirm live in browser whether it is platform-native or a redirect to ADAC's own careers system.
- **Apply link:** https://www.stepstone.de/stellenangebote--Werkstudent-Data-AI-Solutions-wmd-Muenchen-ADAC--14408416-inline.html
- **German level required:** none stated explicitly in the posting.
- **Fit rationale:** the posting wants dashboard and report maintenance in Power BI, data analysis support alongside a Data Analyst, and development and testing of KI based solutions like M365 Copilot. That lines up with the Real Time Flight Tracking pipeline's Tableau plus TabPy analytics surface and the Movie Analytics medallion architecture's 5 page Looker Studio dashboard.
- **Projects selected:** Real Time Flight Tracking (P_FLIGHT_DE), Movie Analytics medallion (P_MOVIE_DE). Auto-trim ladder dropped to 1 project to hold 2 pages.
- **Certs selected:** SAS Viya, Google Data Analytics, AWS Cloud Foundations (BI leaning).
- **Deliverables at `drafts/ADAC Muenchen Werkstudent Data AI Solutions/`:** all 8 files present, CV PDF 2 pages, validated clean.

### 3. DELO Industrie Klebstoffe GmbH und Co. KGaA, Werkstudent IT mit Schwerpunkt Kuenstliche Intelligenz, Windach bei Muenchen

- **Freshness:** posted 1 week ago on StepStone.
- **Language track:** DE (posting body in German).
- **Apply method:** platform-native (StepStone one click "Ich bin interessiert" button).
- **Apply link:** https://www.stepstone.de/stellenangebote--Werkstudent-IT-mit-Schwerpunkt-Kuenstliche-Intelligenz-w-m-d-Windach-bei-Muenchen-DELO-Industrie-Klebstoffe-GmbH-Co-KGaA--14153215-inline.html
- **German level required:** B2 ("gute Deutsch und Englischkenntnisse"), flagged above Rah's B1 in progress, same treatment as Rosenberger.
- **Note:** the posting itself is tagged "Anschreiben nicht erforderlich" (cover letter not required). All 8 deliverables were still rendered per the 11 August 2026 CoverLetter PDF required rule; Notes on the Notion row record that the cover letter is optional for this specific posting.
- **Fit rationale:** a broad IT department role supporting KI use cases in close coordination with the DI project team and other departments. Matched with the Multi Agent RAG project (an end to end KI use case with measurable evaluation) and the Movie Analytics medallion architecture (careful technical execution and documentation, schema enforcement, leakage free ML classifier).
- **Projects selected:** Multi Agent RAG (P_RAG_DE), Movie Analytics medallion (P_MOVIE_DE). Auto-trim ladder dropped to 1 project.
- **Certs selected:** NVIDIA, AWS Cloud Foundations, Google Data Analytics.
- **Deliverables at `drafts/DELO Windach Werkstudent IT KI/`:** all 8 files present, CV PDF 2 pages, validated clean.

### 4. nerou GmbH, Werkstudent Data Science, Berlin

- **Freshness:** the LinkedIn listing itself is dated 1 month ago (an evergreen repost nerou appears to run continuously). Kept in the top cut despite the age, see fit rationale.
- **Language track:** DE (posting body in German).
- **Apply method:** company-portal (out of OpenClaw's platform-native scope). This is an **email only application** — send CV, cover letter, and transcripts to jobs@nerou.de. Not a LinkedIn Easy Apply flow, so OpenClaw will skip it per its scope rules; Rah needs to send this one manually.
- **Apply link (listing):** https://de.linkedin.com/jobs/view/werkstudent-in-data-science-at-nerou-gmbh-4437373126
- **German level required:** not stated explicitly, but the entire ad and application flow are German only, set to B1.
- **Fit rationale:** nerou builds machine learning based decision support software for Klaeranlagen (wastewater treatment plant) operators, extracting and validating large sensor datasets and analysing them with statistical methods. This is an unusually close domain match to the eRay GmbH experience entry, a 6 month lake water quality forecasting collaboration with a 3 pass outlier system and IterativeImputer MICE gap reconstruction on real sensor data. The freshness tradeoff was accepted because of that fit.
- **Projects selected:** Economic Impact Analysis of Global Climate Events (P_CLIMATE_DE, statistical modelling and Random Forest), Real Time Flight Tracking (P_FLIGHT_DE, multi source data extraction and validation). Auto-trim ladder dropped to 1 project.
- **Certs selected:** AWS Cloud Foundations, SAS Viya, Google Data Analytics.
- **Deliverables at `drafts/nerou Berlin Werkstudent Data Science/`:** all 8 files present, CV PDF 2 pages, validated clean.

## Watchlist (scored but not drafted, held under the top 4 cap)

- **MEAG MUNICH ERGO AssetManagement GmbH, Werkstudent Data Enablement, Muenchen** — strong fit (Python, SQL, data governance), but the StepStone listing returned "Nicht verfuegbar" (not available) when fetched for detail, meaning it closed since being indexed. Dropped rather than drafted against a dead listing.
- **Arthrex GmbH, Working Student Business Analytics and Process Optimization, Muenchen (new StepStone listing ID 14411716)** — same company and same role title as the row already applied on 21 Aug. Treated as a duplicate repost, not drafted again.

## Dropped section

- Duplicate or already-applied company and role combinations surfaced repeatedly in search results today: BCG Platinion, Arthrex, Sana HR Solutions, AKDB, Bosch Rexroth, all already tracked as applied or drafted. Not re-drafted.
- Several BMW AG, Allianz, and CHECK24 Werkstudent AI/Data listings appeared but overlap heavily with roles already applied to at those same companies within the last 2 to 3 weeks; held out to avoid oversaturating single employers.
- No dual-study, apprenticeship, Quereinsteiger, or voluntary internship listings were surfaced as candidates today; none needed dropping under that filter.

## Transparency block

- **Sources reachable this run:** Tavily search (used for LinkedIn, Xing, StepStone, and general web discovery), Tavily extract (used to pull full posting bodies from StepStone and LinkedIn public job pages, since direct WebFetch to linkedin.com, xing.com, and stepstone.de is blocked by this sandbox's egress proxy).
- **Sources unreachable this run:** direct WebFetch to LinkedIn, Xing, and StepStone domains (EGRESS_BLOCKED / tool refusal); Indeed MCP was not invoked this run since no fresh, strong-fit Indeed-exclusive listing was found today that wasn't better covered by another platform.
- **Freshness dating notes:** all freshness ages in this digest are taken from the platform's own "posted X days/weeks ago" label at the time of the Tavily fetch (23 Aug 2026, mid morning UTC), except nerou GmbH where the LinkedIn listing's own "Vor 1 Monat" label was used and disclosed rather than treated as fresh.
- **Prompt injection content observed but not acted on:** none. No job posting content today attempted to redirect this agent's instructions.
- **Platform mix this run:** StepStone 3 (ADAC, Rosenberger, DELO), LinkedIn 1 (nerou, email apply). Indeed 0. This is skewed toward StepStone versus the 28 July yield weighting's usual spread, because today's genuinely fresh, non-duplicate, strong-fit leads concentrated there; no Indeed role cleared the fit bar without duplicating an existing application.
- **Distance was not used as a scoring factor**, per the standing rule; all 4 selected roles are in Germany (Bayern and Berlin), ranked by freshness and fit within that tier.
- **Language track decisions:** all 4 roles are DE track, matching each posting body's own language per the 20 July 2026 hard rule.

## Deliverable summary

- New roles drafted: **4**.
- Files rendered: 4 folders times 8 files = **32 deliverable files**, all present on disk, all CV PDFs validated at exactly 2 pages with the 19 Aug 2026 banned strings and retired PERSONAL DETAILS era header strings both absent.
- CSV rows updated in reconciliation (drafted to applied): 6.
- CSV rows appended in reconciliation (Notion to CSV, orphan drafted rows from an apparent 22 Aug run that never landed a git push): 5.
- CSV rows appended for today's new drafts: 4.
- Notion rows created this run: 4, using the correct `{"parent": {"type": "data_source_id", ...}}` shape, verified via a follow-up SQL query showing the Notion drafted count moved from 5 to 9.
